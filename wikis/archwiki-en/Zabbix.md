# Zabbix

Zabbix is a full-featured monitoring solution for larger networks. It can discover all kind of networking devices using different methods, check machine states and applications, sending pre-defined alarm messages and visualize complex data correlations.

## Server setup
## Installation
## Server Installation
Install the  package. This includes the necessary scripts for use with MariaDB or PostgreSQL.

## Database Installation
Install either the  package or the  package.

## Frontend Installation
Install the  package. You should choose a web server with PHP support, e.g.:

* Apache HTTP Server
* Lighttpd
* nginx

You can also choose one of the servers found in Web server.

## Configuration
Symlink the Zabbix web application directory to your http document root, e.g.:

 $ ln -s /usr/share/webapps/zabbix /srv/http/zabbix

To get Apache working out-of-the-box, you need to enable PHP integration:

* see Using php-fpm and mod_proxy_fcgi

Adjust following variables in :

 extension=bcmath
 extension=gd
 extension=gettext
 extension=ldap
 extension=mysqli
 extension=sockets
 post_max_size = 16M
 max_execution_time = 300
 max_input_time = 300
 date.timezone = "UTC"

## Database Initialization
## MariaDB
In this example, we create on localhost a MariaDB database called  for the user  identified by the password  and then import the database templates. This connection will be later used by the Zabbix server and web application.

If your MariaDB installation uses a  account with a password, use the following:
 $ mariadb -u root -p -e "create database zabbix character set utf8 collate utf8_bin"
 $ mariadb -u root -p -e "grant all on zabbix.* to zabbix@localhost identified by 'test'"

If your MariaDB installation uses a  account without a password, use the following:
 # mariadb -e "create database zabbix character set utf8 collate utf8_bin"
 # mariadb -e "grant all on zabbix.* to zabbix@localhost identified by 'test'"

Use the following to import the database templates:

 $ mariadb -u zabbix -p -D zabbix
 ServerActive=
}}

Further make sure the port  on your device being monitored is not blocked and is properly forwarded.

## Starting
Enable and start the  unit.

## Tips and tricks
## Debugging a Zabbix agent
On the client site, you can check the state of an item like this:

 $ zabbix_agentd -t hdd.smartOn the server/monitoring site, try this:

 $ zabbix_get -s host -k hdd.smart[sda,Temperature_Celsius

## Monitor Arch Linux system updates
Here is an approach on how to monitor your Arch Linux clients for available system update using a custom :

You have to restart  to apply the new configuration. The keyword for the item you later use in the web frontend is . It returns an integer representing the count of available updates. (the  utility comes from the  package)

## Troubleshooting
## Error "Specified key was too long; max key length is 767 bytes"
While importing the databases, you might get this error message. In order to solve this, you will have to change the code page configuration for your MariaDB database: MariaDB#Using UTF8MB4.

## Unable to start Zabbix server due to unsupported MariaDB database version
Database version can easily exceeds the maximum alloved version. To bypass this add the following to the configuration file:
