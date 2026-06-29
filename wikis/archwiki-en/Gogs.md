# Gogs

Gogs (Go Git Service) is a Self Hosted Git service, which was written in the Go programming language.

## Installation
Before installing the Gogs package ( or  for the development version), you need to choose a database backend if you are planning to host Gogs on the same machine as the database:

* SQLite:  - For configuration of Gogs with SQLite see #SQLite.
* PostgreSQL:  - Read PostgreSQL#Installation to set it up and start the daemon and for configuration of Gogs with PostgreSQL see #PostgreSQL.
* MariaDB:  - Read MariaDB#Installation to set it up and start the daemon and for configuration of Gogs with MariaDB see #MariaDB.

Each package provides multiple options for configuring the backend/storage for the service, see #Configuration

If you plan to use SSH to interact with your repositories, make sure to add the  user to the  entry in .

## First start
After starting , you can access the running service over the url . At first load, you will be redirected to the installation page where you can configure some options.

In order to be able to save changes made using the initial configuration page the permissions of the configuration directory (owned by root) will have to be modified (either temporary or permanently), for example:

 # chown -R gogs:gogs /etc/gogs/

You also need to create a drop-in file to allow  to change  contents:

Then do a daemon-reload and restart . After installing you can revert these changes to improve security.

In the configuration file , you can change more values (for example the port number).

## Configuration
The Gogs configuration file is located at . When you want to edit a configuration option, you need to edit this file and restart the Gogs service before changes will take effect.

## SSH
In order to interact with the git repositories using ssh, and to be able to use the uploaded public keys:

* set  in  to  (see also documentation), and ensure that  is .

* Add  to  in .

* create  and hand over ownership to the  user:
 > mkdir -p /var/lib/gogs/.ssh
 > chown -R gogs:gogs /var/lib/gogs/.ssh

Public keys will be added by the  user to

## .gitignore and license files
A set of gitignore and license files are included in the package and are stored at  and  respectively.

You can get or create your own .gitignore files here.

## Database
## SQLite
Install  and select SQLite on the installation page. Use an absolute path in  ( variable in the  section) for the SQLite database file. To be consistent with the other settings, use  (see also issue 4298).

## PostgreSQL
Install  and select Postgresql on the installation page.

 # su - postgres -c
 # createuser -P gogs
 # createdb -O gogs gogs

## MariaDB
Install  and setup a user and database:

 # CREATE DATABASE `ishouldchangethisdatabasename` DEFAULT CHARACTER SET `utf8` COLLATE `utf8_unicode_ci`;
 # CREATE USER 'ishouldchangethisusername'@'localhost' IDENTIFIED BY 'ishouldchangethispassword';
 # GRANT ALL ON `ishouldchangethisdatabasename`.* TO 'ishouldchangethisusername'@'localhost';

On the installation page select mysql and insert your configured user, password and database name.

## Theme
The current package (gogs-git* and gogs>=0.4.2) support custom themes. The location for Gogs themes is . Gogs comes with one default theme, but you can easily create your own theme. Just copy the default  directory and change whatever you want. JavaScript, stylesheet and font files are in the  directory, and HTML templates are in the  directory. The current selected theme can be changed over the  configuration parameter . Change it with the absolute path to the new theme.

## Restart after Upgrade
Gogs needs to be restarted after every upgrade because the paths of javascript/css assets will change and therefore break the website.
To automate this the following pacman hook can be inserted at :

 Type = Path
 Operation = Upgrade
 Target = usr/share/gogs/gogs
 [Action
 Description = Restart gogs...
 When = PostTransaction
 Exec = /usr/bin/systemctl try-restart gogs.service

## SSH port
If you are using a non-default port for your SSH server, you will get not-so-pretty clone URLs. You can make gogs start its own SSH server, listening on port 22.

Allow gogs binary to bind privileged ports:

 # setcap CAP_NET_BIND_SERVICE=+eip /usr/share/gogs/gogs

Configure gogs SSH server in :

 START_SSH_SERVER       = true
 SSH_PORT               = 22
 SSH_LISTEN_PORT        = 22
