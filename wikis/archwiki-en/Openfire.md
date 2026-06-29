# Openfire

From Wikipedia:

:Openfire (previously known as Wildfire, and Jive Messenger) is an instant messaging (IM) and groupchat server for the Extensible Messaging and Presence Protocol (XMPP).
:It is written in Java and licensed under the Apache License 2.0.

## Installation
Install the  package.

## Configuration
## Create database
Openfire can create its own flat file database (which is a list of mysql commands, executed and kept in RAM), that should be considered as an alternative because the java program does not support unix sockets out of the box. Check if TCP/IP is disabled:

(comment out the option / use  instead to allow loopback TCP/IP or alternatively #Add unix socket support)

A working MySQL server needs to be installed to create an external database for Openfire like this:

 # mysql -u root -p
 mysql> CREATE DATABASE openfire_db;
 mysql> CREATE USER 'openfire_usr'@'localhost';
 mysql> GRANT ALL PRIVILEGES ON openfire_db.* TO 'openfire_usr'@'localhost' IDENTIFIED BY 'password';

## Starting the server
The Openfire admin interface will listen on port  and  of your server by default. Adding  can probably (untested) be used to temporarily secure the server if the ports are not properly firewalled.

Start  on the remote server. Test if the admin interface is accessible locally with :

 $ curl -v 127.0.0.1:9090 && echo Yay, it works!

## Remote server firewall rules
A list of ports can be found on the index page of the administration interface or with . Assuming no enabled components need UDP (like jingle media proxy?) and you do not want the admin web interface exposed to the world, the following iptables rules should suffice to make Openfire work:

## Usage
## First remote connect
The server should not be accessible from the client yet:

 $ curl -v example.com:9090 && echo Oh no, it works!

Start an ssh tunnel from your PC to your server:

 $ ssh -L -N 9090:localhost:9090 yourserver.example.com -p22

Now connecting to the remote web interface should work - use a web-browser to access , which should start setup and guide through the process.

Database for setup:

 jdbc:mysql://localhost:3306/openfire_db?rewriteBatchedStatements=true

(Use and the username / password as created earlier)

After the setup is complete, log in with the user name  (just "admin". Not as the previous web form suggests "the email address for admin").

## Default settings of special interest
Openfire is configured "ready to go" by default. Before the server is exposed to the world, the following settings should be checked to make sure this is really what the instance is supposed to do / allow.

* Server > Server Settings > Registration & Login:
** New users accounts can automatically be created by everyone through applications that support it
** Anonymous login without accounts is allowed
* Server > Server Settings > Offline Messages:
** Each user can store up to 100kb of data
* Server > Server Settings > File Transfer Settings:
** Openfire acts as a file transfer proxy

## Tips and tricks
## Add unix socket support
Connecting to database via unix socket with a java application requires a jdbc driver with an implementation of socketFactory. MariaDB Connector/J supports auth over socket since version 1.4. and can be install via , which also requires  (Java Native Access) to work with unix sockets. Install both.

Instead this works for now (but is kind of ugly):

 # ln /usr/share/java/mariadb-jdbc/mariadb-java-client.jar /usr/lib/openfire/
 # ln /usr/share/java/jna.jar /usr/lib/openfire/

If openfire setup was already completed using a TCP/IP connection to the same database, switch to the new driver by changing the xml configuration:

When using the setup interface instead, choose "MySQL" and enter the values of driver and serverURL into the "JDBC Driver Class" and "Database URL" fields of the web form respectively.

Restart the  - it may be necessary to start the setup interface again (#First remote connect) afterwards.

## Using multiple domains
Openfire does not support multiple domains / vhosts like prosody does, but it works with an LDAP-server that provides authentication for multiple domains.

Users from different domains can then login and communicate normally, but this is messy; side-effects may include but are not limited to:

* unlisted users
* need to create users manually
* users from other domains showing up as members of default domain
* users from other domains conflicting with same name users from other domains
* SSL certificate errors (separate certificates for different domains not possible)

## Test installation on local PC
For a large local LAN make sure the PC that is supposed to run the Openfire server is safe / behind a firewall - as soon as it is started, the admin interfaces becomes available to anyone who has access to port  and .

For a local server on a PC, the integrated Database of Openfire will suffice under most circumstances. If an unusual amount of traffic is expected and the PC lacks RAM, a MySQL database can be used instead (See #Create database).

Install  and start the .

Open  in a web browser to complete the setup process, then log in as  and review the settings.
