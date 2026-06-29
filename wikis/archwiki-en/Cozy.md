# Cozy

Cozy is a personal cloud platform free, and self-hostable, written in Go (the former version, v2, was written in Node.js instead).

The platform aims at simplifying the use of a personal cloud and at allowing the users to take back ownership of their privacy. Its base applications’ features include hosting, sharing and synchronising files & pictures and collecting your data from several providers. Some other apps are on the roadmap, like a contacts manager and a calendar.

Third-party apps are also available through a marketplace.

## Installation
Install the  package. It provides the core plus related configuration files, as well as the minimum required dependencies.

You might also want to install  to run Konnectors in isolated environments, as well as an SMTP server to let Cozy send emails to your users.

## Configuration
Almost everything happens in . Some defaults are already set, while some placeholders will be replaced during configuration. You can also find an example file at .

## Configuring CouchDB
Cozy stores everything (but actual files) in a CouchDB database, and needs a CouchDB administrator to manage this database.
This administrator’s credentials must be specified as part of the  setting in  so that Cozy can use them.
The following supposes you have a running CouchDB instance, if not you can follow the corresponding wiki page to setup one as single node.

You can generate the credentials with  for example. Once you have them ( and ), edit your configuration as follow:

And register them to CouchDB (replace  and  with your CouchDB admin credentials):

 $ curl -X PUT http://:@127.0.0.1:5984/_node//_config/admins/ -d "\"\""

You can retrieve the correct node name with:

 $ curl -X GET http://:@127.0.0.1:5984/_membership

## Configuring Cozy admin password
Cozy itself requires an admin password for all operations at the stack level.
Create it as the cozy user:

 cozy-stack -c /dev/null config passwd /etc/cozy/cozy-admin-passphrase

You will be prompted to enter a passphrase.

## Creating vault keys
Cozy uses a vault to store some user passwords. To create the vault keys with right ownership and permissions, just proceed as the cozy user:

 [cozy$ cozy-stack -c /dev/null config gen-keys /etc/cozy/vault

## Starting the stack
At this point, you should start/enable the  daemon.

You can check everything is right by running:

 $ curl http://localhost:8080/version

## Creating an instance
To add an instance (you will be prompted for your Cozy admin password, you might also pass it using COZY_ADMIN_PASSWORD env var):

 $ cozy-stack instances add .example.tld --apps home,settings,store

This will output you a registration token. You can also specify an email using  at which the registration token will be sent (this require having set a smtp server in ).

You will then need to visit , which requires you to have setup a reverse proxy (see below).

## Reverse proxying
As a security measure, Cozy needs to be served over HTTPS, which means it needs a reverse proxy in front of it. This can managed by either a proxying software like HAproxy or a webserver such as Apache HTTP Server, nginx or Caddy.

Cozy needs a full domain name for the instance (something like ) and use one domain name per application, in the form of .

Thus, you have to setup your domain zone with something like this:

     1h IN A x.x.x.x
    *. 1h IN CNAME

You will also need SSL certificates, either a wildcard one covering  and  or a certificate for  with apps domains added as SAN.
Currently, the list of apps is: home, banks, contacts, drive, notes, passwords, photos, settings, store and mespapiers.
However, this may grow over time, so you could have to expand your certificate.
Thus, getting a wildcard one is advised.

Below is an example configuration file for nginx.

## nginx
{{hc|/etc/nginx/sites-available/instance.conf|2=

# Always redirect http:// to https://
server {
    listen 80;
    server_name .instance.example.tld instance.example.tld;

    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl http2;
    listen :::443 ssl http2;
    server_name .instance.example.tld instance.example.tld;

    ssl_certificate /etc/cozy/instance.crt;
    ssl_certificate_key /etc/cozy/instance.key;

    # Limit max upload size
    client_max_body_size 1g;

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_http_version 1.1;
        proxy_redirect http:// https://;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection $connection_upgrade;
    }
}
}}
