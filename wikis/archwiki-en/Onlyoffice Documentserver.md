# Onlyoffice Documentserver

Onlyoffice Documentserver is a full-featured backend for editing different office documents like Open Document, Word, Excel, etc. online in your browser. The software is open source and can be easily deployed and integrated into existing server software. Available frontends are Nextcloud or the Onlyoffice CommunityServer. It can be also used in own software, see following examples for PHP, Nodejs, etc.

## Installation
Install the  package. Further you will need PostgreSQL or MariaDB as a database backend and the Redis and  services installed.

Alternatively, install via docker and run:

 $ docker pull onlyoffice/documentserver
 $ docker run -i -t -d -p PORT:80 --restart=always onlyoffice/documentserver

Where PORT can be either 80, if not already in use by another web server, or different, e.g. 9980.

## Configuration
## local.json
You can create local.json in /etc/webapps/onlyoffice/documentserver, where are possible to overwrite any parts of config (below full local.json with rabbitmq, mariadb, redis and accesskey configuration:

{{hc|/etc/webapps/onlyoffice/documentserver/local.json|
{
        "queue": {
                "type": "rabbitmq"
        },
        "rabbitmq": {
                "url": "amqp://onlyoffice:onlyoffice@127.0.0.1:5672/onlyoffice"
        },
        "services": {
                "CoAuthoring": {
                        "sql": {
                                "type": "mariadb",
                                "dbHost": "127.0.0.1",
                                "dbPort": 3306,
                                "dbName": "onlyoffice",
                                "dbUser": "onlyoffice",
                                "dbPass": "ONLYOFFICE_DB_PASSWD"
                        },
                        "redis": {
                                "name": "redis",
                                "host": "127.0.0.1",
                                "port": 6379,
                                "db": "10"
                        },
                        "server": {
                                "port": 8000,
                                "workerpercpu": 1,
                                "mode": "production"
                        },
                        "secret": {
                                "browser": {"string": "YOUR SECRET IN NEXTCLOUD"},
                                "inbox": {"string": "YOUR SECRET IN NEXTCLOUD"},
                                "outbox": {"string": "YOUR SECRET IN NEXTCLOUD"},
                                "session": {"string": "YOUR SECRET IN NEXTCLOUD"}
                        },
                        "token": {
                                "enable": {
                                        "browser": true,
                                        "request": {
                                                "inbox": true,
                                                "outbox": true
                                        }
                                 }
                        }
}
}
}
}}

You should NOT edit the default.json config file.

## RabbitMQ
You may create vhost in your RabbitMQ for onlyoffice and select it in local.json:

 $ rabbitmqctl add_vhost onlyoffice
 $ rabbitmqctl add_user onlyoffice onlyoffice
 $ rabbitmqctl set_permissions -p onlyoffice onlyoffice ".*" ".*" ".*"

## Database
## PostgreSQL
The PostgreSQL database backend needs to be configured. Here is an example database setup:

 psql -c "CREATE DATABASE onlyoffice;"
 [postgres$ psql -c "CREATE USER onlyoffice WITH password 'onlyoffice';"
 psql -c "GRANT ALL privileges ON DATABASE onlyoffice TO onlyoffice;"

As of PostgreSQL 15, it's required to give admin privileges to the onlyoffice user in psql so that the database schema migration command successfully executes:

 [postgres$ psql -c "ALTER DATABASE onlyoffice OWNER TO onlyoffice;"

To migrate the documentserver database schema, run following command:

 $ psql -hlocalhost -Uonlyoffice -d onlyoffice -f /usr/share/webapps/onlyoffice/documentserver/server/schema/postgresql/createdb.sql

## MariaDB
Login to mariadb and create a database and a user:

 $ create database onlyoffice;
 $ create user 'onlyoffice'@'localhost' identified by ONLYOFFICE_DB_PASSWD;
 $ grant all on onlyoffice.* to 'onlyoffice'@'localhost';
 $ flush privileges;

Then import schemadb:

 $ mysql -uonlyoffice -p onlyoffice  Administration Settings > ONLYOFFICE''.

## Webserver
## Nginx / no SSL
Here is an example for the Nginx webserver:

{{hc|/etc/nginx/sites-available/onlyoffice-documentserver|
map $http_host $this_host {
  "" $host;
  default $http_host;
}
map $http_x_forwarded_proto $the_scheme {
  default $http_x_forwarded_proto;
  "" $scheme;
}
map $http_x_forwarded_host $the_host {
  default $http_x_forwarded_host;
  "" $this_host;
}
map $http_upgrade $proxy_connection {
  default upgrade;
  "" close;
}
proxy_set_header Host $http_host;
proxy_set_header Upgrade $http_upgrade;
proxy_set_header Connection $proxy_connection;
proxy_set_header X-Forwarded-Host $the_host;
proxy_set_header X-Forwarded-Proto $the_scheme;
server {
  listen 0.0.0.0:80;
  listen default_server;
  server_tokens off;
  rewrite ^\/OfficeWeb(\/apps\/.*)$ /web-apps$1 redirect;
  location / {
    proxy_pass http://localhost:8000;
    proxy_buffers 4 256k;
    proxy_max_temp_file_size 0;
  }
  location /spellchecker/ {
    proxy_pass http://localhost:8080/;
  }
}
}}

## Nginx / reverse proxy with SSL
Create a Nginx configuration file like the following:

{{hc|/etc/nginx/conf.d/onlyoffice.conf|
upstream docservice {
  server 127.0.0.1:PORT;
}

map $http_host $this_host {
    "" $host;
    default $http_host;
}

map $http_x_forwarded_proto $the_scheme {
     default $http_x_forwarded_proto;
     "" $scheme;
}

map $http_x_forwarded_host $the_host {
    default $http_x_forwarded_host;
    "" $this_host;
}

map $http_upgrade $proxy_connection {
  default upgrade;
  "" close;
}

proxy_set_header Upgrade $http_upgrade;
proxy_set_header Connection $proxy_connection;
proxy_set_header X-Forwarded-Host $the_host;
proxy_set_header X-Forwarded-Proto $the_scheme;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

server {
    listen 0.0.0.0:443 ssl;
    listen [:::443 ssl default_server;
    server_name SERVER_NAME
    server_tokens off;
    root /usr/share/nginx/html;

    ssl_certificate SSL_CERT;
    ssl_certificate_key SSL_KEY;
    ssl_verify_client off;
    ssl_ciphers "EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH";
    ssl_protocols  TLSv1 TLSv1.1 TLSv1.2;
    ssl_session_cache  builtin:1000  shared:SSL:10m;
    ssl_prefer_server_ciphers   on;

    add_header X-Content-Type-Options nosniff;
    location / {
      proxy_pass http://docservice;
      proxy_http_version 1.1;
  }
}
}}

Fill in PORT (default 8000), SERVER_NAME, SSL_CERT and SSL_KEY. This was taken from the nginx reference config.

Reload Nginx:

 $ nginx -t
 $ nginx -s reload

## Starting
Enable/start the following services if you wish to use them locally on the same machine:

*
*
*

Finally, start the documentserver services:

*
*

## Nextcloud app
Install the ONLYOFFICE app within Nextcloud. Enter Nextcloud > Settings > ONLYOFFICE and fill in Onlyoffice Docs address with https://SERVER_NAME.

## Troubleshooting
## Onlyoffice Docker container on ZFS
When running onlyoffice/documentserver as a Docker container with the  pointing to a ZFS device, e.g. when  is mounted as a ZFS pool,  might fail with .

In this case, let Docker have its  on an ext4 partition, for instance :

{{hc|/etc/docker/daemon.json|
{
    "data-root": "/var_ext4/lib/docker"
}
}}

## Pkg: Error reading from file.
If docservice exits with the above error, set the OPTIONS in  to the given default before building:

## ONLYOFFICE cannot be reached after upgrade to 8.2.0
Flush your redis database e.g. by executing

 $ redis-cli flushall
