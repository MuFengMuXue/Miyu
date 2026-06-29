# Icinga

Icinga is an open source host, service and network monitoring program. It monitors specified hosts and services, alerting you to any developing issues, errors or improvements. This article describes the installation and configuration of Icinga.

## Installation
Install .

You may also want to install .

Start/enable the .

## Icinga Web 2
Install  and optionally .

Enable the  if you installed the director module.

## Configure web server
If you use php-fpm, you will have to override the unit - make sure to replace  with  if you use that:

You will also have to add your webserver to the group  to be able to create and change configuration files from the web app directly, assuming  is the webserver user:

 # usermod -a -G icingaweb2 http

## nginx
Example server block, with php-legacy, the sock path in the example becomes  instead:

{{bc|
server {
	listen 80;
	listen server_name localhost;
	root /usr/share/webapps/icingaweb2/public;
	location ~ ^/icingaweb2/index\.php(.*)$ {
		fastcgi_pass unix:/run/php-fpm/php-fpm.sock;
		fastcgi_index index.php;
		include fastcgi_params;
		fastcgi_param SCRIPT_FILENAME /usr/share/webapps/icingaweb2/public/index.php;
		fastcgi_param ICINGAWEB_CONFIGDIR /etc/icingaweb2;
		fastcgi_param REMOTE_USER $remote_user;
	}
	location ~ ^/icingaweb2(.+)? {
		alias /usr/share/webapps/icingaweb2/public;
		index index.php;
		try_files $1 $uri $uri/ /icingaweb2/index.php$is_args$args;
	}
}
}}

## Apache
If you get HTTP/503 errors, check in the configuration file to see if you are allowed to access the page:

  Order allow,deny
  Allow from all

This has to be located in the  and  sections.

## Configure PHP
Uncomment the following extensions:

If  is set in , you need to authorize  and you need to create  environment variable to  to avoid an  error on  at line 740.

## Configure Icinga
You can choose either PostgreSQL or MariaDB to use as a backend for Icinga.

By default Icinga uses the following files and directories:

*  — Contains Icinga 2 configuration files.
*  — The Icinga 2 binary.
*  — Documentation files that come with Icinga 2.
*  — The Icinga Template Library and plugin command configuration.
*  — PID file.
*  — Command pipe and Livestatus socket.
*  — /,  files
*  — Used for performance data spool files.
*  — Icinga 2 state file, cluster log, local CA and configuration files.
*  —	Log file location and compat/ directory for the CompatLogger feature.

## Automatically
Generate a setup token and let Icinga Web 2 handle it by using the setup page:

 # icingacli setup config directory --group icingaweb2;
 # icingacli setup token create;

http://localhost/icingaweb2/setup

## Manually
In case you do not want to use Icinga Web 2 to configure everything for you.

## MariaDB
https://icinga.com/docs/icinga-2/latest/doc/02-installation/

https://icinga.com/docs/icinga-web/latest/doc/02-Installation/

Create icinga user and db:
 # mysql -u root -p
 > CREATE DATABASE icinga;
 > GRANT SELECT, INSERT, UPDATE, DELETE, DROP, CREATE VIEW, INDEX, EXECUTE ON icinga.* TO 'icinga'@'localhost' IDENTIFIED BY 'supersecretpassword';
 > quit

Create icingaweb2 user and db:
 # mysql -u root -p
 > CREATE DATABASE icingaweb2;
 > GRANT ALL ON icingaweb2.* TO 'icingaweb2'@'localhost' IDENTIFIED BY 'anothersecurepassword';
 > quit

Import the icinga schema:
 # mysql -u root -p icinga  CREATE DATABASE director CHARACTER SET 'utf8';
 > CREATE USER director@localhost IDENTIFIED BY 'directorpassword';
 > GRANT ALL ON director.* TO director@localhost;

Create a user to login to Icinga Web 2:
 $ php -r 'echo password_hash("yourwebpassword", PASSWORD_DEFAULT);'

Use the hash you got from the previous command, replacing the hash in this example to insert a new user into the database:
 # mysql -u root -p
 > USE icingaweb2;
 > INSERT INTO icingaweb_user (name, active, password_hash) VALUES ('icingaadmin', 1, '$2y$10$G.qLnALysvw3yr5wP70sF.KtlwB/xDYypRU3x2WZd6x3N0oBAXuIi');

Edit  with your SQL details.

Enable ido-mysql:
 # icinga2 feature enable ido-mysql

## PostgreSQL
https://icinga.com/docs/icinga2/latest/doc/02-installation/#installing-postgresql-database-server

As the postgres user, create icinga user and db:

 [postgres$ psql -c "CREATE ROLE icinga WITH LOGIN PASSWORD 'supersecretpassword'"
 createdb -O icinga -E UTF8 icinga

Create icingaweb2 user and db:

 [postgres$ psql -c "CREATE ROLE icingaweb2 WITH LOGIN PASSWORD 'anothersecurepassword'"
 createdb -O icingaweb2 -E UTF8 icingaweb2

Import the icinga schema:

 # psql -U icinga -d icinga < /usr/share/icinga2-ido-pgsql/schema/pgsql.sql

Import the icingaweb2 schema:

 # psql -U icingaweb2 -d icingaweb2 < /usr/share/webapps/icingaweb2/etc/schema/pgsql.schema.sql

Create director database and user:

 [postgres$ psql -q -c "CREATE DATABASE director WITH ENCODING 'UTF8';"
 psql director -q -c "CREATE USER director WITH PASSWORD 'directorpassword'; GRANT ALL PRIVILEGES ON DATABASE director TO director; CREATE EXTENSION pgcrypto;"

Create a user to login to Icinga Web 2:

 $ php -r 'echo password_hash("yourwebpassword", PASSWORD_DEFAULT);'

Use the hash you got from the previous command, replacing the hash in this example to insert a new user into the database:

 [postgres$ psql -d icingaweb2
 icingaweb2=# INSERT INTO icingaweb_user (name, active, password_hash) VALUES ('icingaadmin', 1, '$2y$10$G.qLnALysvw3yr5wP70sF.KtlwB/xDYypRU3x2WZd6x3N0oBAXuIi');

Edit  with your SQL details.

Enable ido-pgsql:

 # icinga2 feature enable ido-pgsql

## Finally
Enable Icinga api:
 # icinga2 api setup

Enable director module and its dependencies:
 # icingacli module enable incubator
 # icingacli module enable director

Create Director database schema:
 # icingacli director migration run --verbose

Restart  for the changes to apply.

If you chose to use Icinga Web 2, create appropriate .ini files (Use  and  for db and port if you use MariaDB):

The following is the currently default config, the important non-default part is .

One can instead generate this file through http://localhost/icingaweb2/config/general instead.

Go to http://localhost/icingaweb2/ and try to login as 'icingaadmin' and your chosen password - if all works, you are done with the basic setup!

## Upgrade database
New versions usually require an upgrade of the database. You can find the SQL upgrade scripts in the following folders:
 /usr/share/icinga2-ido-mysql/schema/upgrade
 /usr/share/icinga2-ido-pgsql/schema/upgrade
 /usr/share/webapps/icingaweb2/schema/mysql-upgrades
 /usr/share/webapps/icingaweb2/schema/pgsql-upgrades
To do the upgrade,  into the appropriate folder as written above and import the schema, examples:
 # mysql -u root -p icinga < ./2.8.1.sql
 # mysql -u root -p icingaweb2 < ./2.12.0.sql
 # psql -U icinga -d icinga < ./2.8.1.sql
 # psql -U icingaweb2 -d icingaweb2 < ./2.12.0.sql

Restart  for the changes to apply.
