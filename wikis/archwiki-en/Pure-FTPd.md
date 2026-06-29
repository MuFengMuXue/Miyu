# Pure-FTPd

Pure-FTPd is an FTP server designed with security in mind.

## Installation
 can be installed from the Arch User Repository.

Start and enable .

## Configuration
Pure-FTPd configuration is completely done with its startup arguments.

There is a wrapper script, which reads . It then starts Pure-FTPd with the corresponding arguments.

## Set up virtual users
With Pure-FTPd, it is possible to use virtual users instead of real system users.

The available users need to be provided by one or more backends. See backends.

For simplicity and demonstration purposes, the PureDB backend will be used. Uncomment the following two lines:

Now only authenticated users can connect. To add users to the PureDB we need to create a -like file which is then used to create the PureDB.

To create, view, or modify the  file, we use the  command.

 # pure-pw useradd someuser -u ftp -d /srv/ftp

This creates the user someuser which runs as the FTP system user. By default, the user is chrooted to . In the event that that's undesirable, replace  with .

Before this account is usable, we need to commit our changes:

 # pure-pw mkdb

The virtual user can now access everything in .

The command  creates the file mentioned earlier called , which houses all information related to your virtual users. There is no need to restart your service when issuing this command as it is updated on the fly and changes take effect immediately.

## Changing user password
For example, to change a user's password, type the command:

 # pure-pw passwd someuser

Afterwards, commit your changes by updating :

 # pure-pw mkdb

## Removing user
To remove a user, type the command:

 # pure-pw userdel someuser

The user's home directory is not removed via this command; therefore, it must be removed manually.

## Checking user settings
To check a user's current account settings, type the command:

 # pure-pw show someuser

## Backends
You need to specify one or more backends. If you specify more than one, Pure-FTPd will respect the order in which they are specified. It will use the first backend which contains the requested user.

Available backends are:

*
* MySQL
* LDAP
* PostgreSQL
* PAM
* PureDB
* Or you can write your own

## PAM
To enable PAM backend, create the following file:

and uncomment the PAMAuthentication line in the config file like so:

## Set up TLS
## Create a certificate
Refer to the documentation for more information. The short version is this:

Create a Self-Signed Certificate:

 # mkdir -p /etc/ssl/private
 # openssl req -x509 -nodes -days 7300 -newkey rsa:2048 -sha256 -keyout /etc/ssl/private/pure-ftpd.pem -out /etc/ssl/private/pure-ftpd.pem

Make it private:
 # chmod 600 /etc/ssl/private/*.pem

## Enable TLS
Towards the bottom of  you should find a section for TLS. Uncomment and change the  setting to  to enable both FTP and FTPS:

Now restart the  unit and you should be able to log in with FTPS-capable clients, e.g.  or SmartFTP.
