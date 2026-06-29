# Pufferpanel

From Pufferpanel:

:PufferPanel is an open source game server management panel designed to be easy to use and easy to install. PufferPanel supports Minecraft, Spigot, Sponge, Source Dedicated Servers, BungeeCord, PocketMine, Forge, and much more.

## Installation
Install the  package.

In order to be able to login to the web interface, and configure the installation you will need to create a user:

 # pufferpanel user add

This will bring up a command line interactive prompt.

After creating the admin user, you can Start/enable .

## Configuration
Pufferpanel configuration can be found under . Within this directory you will find a  file which contains all the configuration for the instance. Email templates can be found within , this allows for the configuration of the notification emails sent to users.

You can configure the panel through the web interface, by logging in as the administrator account which you created during #Installation and going to the .

## Reverse proxy
By default, pufferpanel does not support TLS encryption, it relies on other web servers to reverse proxy to provide TLS support.

## Nginx
Ensure you have installed nginx, then follow the upstream guide ==== Apache ====

Ensure you have installed Apache, then follow the upstream guide [https://docs.pufferpanel.com/en/latest/guides/apache.html.

## Caddy
Ensure you have installed Caddy, then follow the upstream guide === Database ===

By default, pufferpanel uses a sqlite3 database, located at .

Other, external databases, are also supported for scalability and redundancy, along with the ability to change the path of the embedded sqlite3 database.

## MySQL/MariaDB
Ensure you have installed MariaDB and configured MariaDB, then follow the configuration provided by upstream [https://docs.pufferpanel.com/en/latest/guides/database.html#mysql-mariadb.

## PostgreSQL
Ensure you have installed PostgreSQL, followed initial configuration and created a user and database, then follow the configuration provided by upstream ==== Microsoft SQL Server ====

Follow the configuration provided by upstream [https://docs.pufferpanel.com/en/latest/guides/database.html#microsoft-sql-server.
