# Joomla

Joomla! is a free and open-source content management system (CMS) for publishing web content. It is written in PHP and stores the data in a MySQL, PostgreSQL or MS SQL database.

Among the supported features are page caching, RSS feeds, printable versions of pages, news flashes, blogs, search, and support for language internationalization.

## Installation
In order for Joomla to function, the following components need to be installed and configured:
* An HTTP server with support for PHP (in the following example Apache HTTP Server will be used)
* A PHP libraries
* An SQL engine (PostgreSQL, MySQL)

## In place of a PHP server
Install the  package.

## From scratch
Start by installing all of the necessary packages:

For MySQL (MariaDB) or PostgreSQL see #Choosing between MySQL and PostgreSQL

## Configuration
## Apache
See Apache HTTP Server#Configuration

After following the instructions you should have a running copy of Apache.

Now to enable PHP support we need to get back to editing :
PHP is known not to work with  module. So we need to disable it in favor of  like this:
 #LoadModule mpm_event_module modules/mod_mpm_event.so
 LoadModule mpm_prefork_module modules/mod_mpm_prefork.so

Now we need to add(uncomment) the following line after the  module:
 LoadModule php_module modules/libphp.so

Add the handler:
 AddHandler php-script php

Append at the end of the  list:

 Include conf/extra/php_module.conf

And we are done!

## MySQL
## Choosing between MySQL and PostgreSQL
When choosing between MySQL(MariaDB) and PostgreSQL one should consider that MySQL's design is supposed to be fast and light vs more solid all-in-one PostgreSQL approach. For the purpose of this article MySQL was chosen because:
* it is more lightweight
* it is licensed under GPL(vs MIT)

See MariaDB to install.

After the base installation and configuration has been completed, it is time to perform some more detailed setup.

First, create the database for your future website:

 $ mysqladmin -u root -p create joomla

The naming convention is optional, but for the sake of clarity the database will be called 'joomla'

It is recommended to avoid using root MySQL account for everyday tasks. In order to create another user one must first invoke mysql interface with:

 $ mysql -u root -p

It will prompt you for MySQL's root password. If everything went OK and MySQL server is running, you sould end up with MariaDB prompt akin to this one:
 MariaDB In order to create a privileged user issue a following command:

 GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER, CREATE TEMPORARY TABLES, \
 LOCK TABLES ON joomla.* TO '$USER'@'localhost' IDENTIFIED BY '$PASSWD';

If you are setting up a personal server feel free to experiment with the $USER and $PASSWD values.

Now, to apply these settings:

 FLUSH PRIVILEGES;
 quit

## PHP
Now to setup our PHP server. We will be running it using Apache.
Edit :

A minimal configuration goes as follows:
* Comment out
 ;output_buffering = 4096
* Edit the following value for a more verbose error reporting
 error_reporting = E_ALL & ~E_DEPRECATED & ~E_STRICT
 display_errors = On
* Optional: enable logging
 log_errors = On
* Enable MySQL support(uncomment the following options):
 extension=pdo_mysql
 extension=mysqli

To test whether PHP was configured properly add this line somewhere in the body of a simple html page file:

 Hello World'; ?>

Save this as some_page.php

Now restart httpd and navigate to http://localhost/some_page.php

## Joomla
By now you should have a working instance of Apache with PHP and MySQL up and running.

Now to get started with joomla, copy the contents of  to your document root.

Navigate to your [http://localhost/ localhost

You should be presented with the Joomla! installation screen.

## Troubleshooting
## The file Cache Storage is not supported on this platform
It is most likely that Apache does not have write permissions on

Since by default Apache is ran as 'http' user, those must be tweaked accordingly for  and
