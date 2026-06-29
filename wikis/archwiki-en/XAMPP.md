# XAMPP

XAMPP is an easy to install Apache distribution containing MariaDB, PHP, Perl and ProFTPD. It contains: Apache, MariaDB, PHP & PEAR, Perl, ProFTPD, phpMyAdmin, OpenSSL, GD, Freetype2, libjpeg, libpng, gdbm, zlib, expat, Sablotron, libxml, Ming, Webalizer, pdf class, ncurses, mod_perl, FreeTDS, gettext, mcrypt, mhash, eAccelerator, SQLite and IMAP C-Client.

## Installation
Install the  package.

## Configuration
The default configuration should work out of the box. Setting the individual parts of XAMPP can by made by editing following files:

*  — Apache configuration. For example you can change folder with web page's source files.
*  — PHP configuration.
*  — phpMyAdmin configuration.
*  — ProFTPD configuration.
*  — MySQL configuration.

If you would like to set up security of server, just run

 # /opt/lampp/xampp security

You will be asked step by step to choose passwords for web page's access, user "pma" for phpMyAdmin, user "root" for MySQL and user "daemon" for ProFTPD.

## Usage
Use the following commands to control XAMPP:

 # /opt/lampp/xampp start,stop,restart

Alternatively, you can start, stop, or restart .

## Autostart on boot
In order to start XAMPP at boot, enable .

## Tips and tricks
## Hosting files outside the htdocs directory
The document root (web root) directory is located at . All files placed in this directory will be processed by the web server.

To host other files on your system with XAMPP, you can configure an alias with Apache.

* Edit Apache's  with your favorite editor.
* Find , you will see something like:

* In the next line after  paste this:

* Next find the :

* And before the  paste this:

 Alias /yourAlias /yourDirectory/

* Next find the :

* And change the  with  and :

 User yourUser
 Group yourGroup

* Now do not forget to restart Apache:
 # /opt/lampp/xampp restart

This will allow you to host files from your home directory (or any other directory) with XAMPP.

In the above example, you can access the files by pointing your web browser to .

## Debugging and profiling with Xdebug and XAMPP
See https://xdebug.org/find-binary.php for detailed instructions.

You must first download the XAMPP Development Tools from the same download page, https://www.apachefriends.org/en/xampp-linux.html.

Extract this into your XAMPP directory:

 # tar xvfz xampp-linux-devel-x.x.x.tar.gz -C /opt

You should be able to successfully run  in your xdebug folder.

## Local test server security
Apache, MySQL and ProFTPD can be configured so that they only listen to requests from your own computer. For most test systems this is fine and it greatly reduces the risk because the services are not reachable from the Internet.

Before you start XAMPP for the first time find and edit these files:

For Apache edit the files  and . Look for lines starting with "Listen" such as

 Listen 80

and replace them with

 Listen 127.0.0.1:80

For MySQL open the file  find the section "and add this line

 bind-address=localhost

For ProFTPD, add the following lines to  under the "DefaultServer" section

 DefaultAddress 127.0.0.1
 SocketBindTight on

After starting the services, verify the result by going to a command window and start and execute:

 $ ss -tln

The local address column should always start with 127.0.0.1 or ::1, never with 0.0.0.0.

## Manual installation
To install XAMPP manually instead of following #Installation, download the installer from [https://www.apachefriends.org/index.html the website, make it executable and run it by typing:

 # ./xampp-linux-x64-version-installer.run

You can now create a systemd service for XAMPP:

## Manual removal
If you have installed XAMPP manually you will need to remove it manually as well. Be sure to stop all XAMPP services.

 # /opt/lampp/xampp stop

All the files needed by XAMPP to be installed are located in the previous  folder. So, to uninstall XAMPP:

 # rm /etc/systemd/system/xampp.service
 # rm -r /opt/lampp

## Troubleshooting
## PhpMyAdmin 403 Access Forbidden
If your http://localhost/phpmyadmin returns "403 Access Forbidden", you need to edit the following settings in :

 	AllowOverride AuthConfig Limit
 	#Order allow,deny
 	#Allow from all
 	Require all granted
