# PhpLDAPadmin

phpLDAPadmin is an web-based LDAP adminstration interface.

## Pre-Installation
See LAMP for a guide to setting up Apache, MySQL, and PHP.

## Installation
Install the  package.

## Configuration
## Apache
Create the Apache configuration file:

And include it in :
 # phpLDAPadmin configuration
 Include conf/extra/phpldapadmin.conf

By default, everyone can see the phpLDAPadmin page, to change this, edit  to your liking. For example, if you only want to be able to access it from the same machine, replace  by .

## PHP
You need to enable the  and  extensions in PHP by editing  and uncommenting the following lines:
 extension=ldap
 extension=gettext

You need to make sure that PHP can access  and . Add them to  in  :
 open_basedir = /srv/http/:/home/:/tmp/:/usr/share/pear/:/usr/share/webapps/:/etc/webapps

## phpLDAPadmin configuration
phpLDAPadmin's configuration file is located at . If you have a local LDAP server, it should be usable without making any modifications.

If your LDAP server is not on the localhost, uncomment and edit the following line:
 $servers->setValue('server','host','127.0.0.1');

Although not strictly necessary you can name your server by editing the following line:
 $servers->setValue('server','name','My LDAP server');

## Accessing your phpLDAPadmin installation
Your phpLDAPadmin installation is now complete. Before start using it you need to restart Apache.

You can access your phpLDAPadmin installation by going to http://localhost/phpldapadmin/
