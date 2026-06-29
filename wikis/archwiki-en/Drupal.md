# Drupal

"Drupal is a free and open source content management system (CMS) and Content Management framework (CMF) written in PHP and distributed under the GNU General Public License." - Wikipedia

This article describes how to setup Drupal and configure Apache HTTP Server, MySQL or PostgreSQL, PHP, and Postfix to work with it. It is assumed that you have some sort of LAMP (Linux, Apache, MySQL, PHP), LAPP (Linux, Apache, PostgreSQL, PHP) or LASP (Linux, Apache, SQLite, PHP) server already setup.

## Installation
Install the  package.

## Configuration
## PHP
Edit :

* To enable support for image manipulation uncomment the line

For database support enable a PDO extension for your database
* To enable support for SQLite uncomment the line
* To enable support for MySQL uncomment the line
* To enable support for PostgreSQL uncomment the line

Apache will fail to start with an error finding php_admin_value, below fixes this:

Install the  package.

In , comment the line:
 #LoadModule mpm_event_module modules/mod_mpm_event.so
and uncomment the line:
 LoadModule mpm_prefork_module modules/mod_mpm_prefork.so

Place this at the end of the  list:
 LoadModule php7_module modules/libphp7.so
 AddHandler php7-script .php
Place this at the end of the  list:
 Include conf/extra/php7_module.conf

Restart  using systemd.

Apache will fail to start with an error finding open_basedir, below fixes this:

In , uncomment and suffix  to look like this:

 open_basedir = /etc/webapps

## Apache
Copy the example Apache configuration file:
 # cp /etc/webapps/drupal/apache.example.conf /etc/httpd/conf/extra/drupal.conf

And include it at the bottom of :
 Include conf/extra/drupal.conf

In , also uncomment the  line.

## Drupal
Edit  and replace  by .

Finally, restart Apache (). You can now access the Drupal installation at http://localhost/drupal .

## Commandline tools
## Drush
Drush is a command line shell and Unix scripting interface for Drupal. Drush core ships with lots of useful commands for interacting with code like modules/themes/profiles. Similarly, it runs update.php, executes sql queries and DB migrations, and misc utilities like run cron or clear cache. Drush can be extended by 3rd party commandfiles.
It can be installed with the  package.

## Drupalconsole
Drupalconsole is a CLI tool to generate boilerplate code, interact and debug Drupal 8.
It can be installed with the  package.

## PHP-Codesniffer-Drupal
PHP-Codesniffer-Drupal checks your Drupal code against coding standards and other best practices.
It can be installed with the  package.

## Tips and tricks
## Sending Mail
Drupal needs a Sendmail-compatible MTA like Sendmail, Postfix or Exim if you plan to send mail from your local setup.
Alternatively there are multiple solutions to send mail via external mail servers through SMTP or other means like SMTP or PHPMailer. Use the search page to find more possibilities.

## Scheduling with Cron
Drupal recommends running cron jobs hourly. Cron can be executed from the browser by visiting http://localhost/drupal/cron. It is also possible to run cron via script by copying the appropriate file from the "scripts" folder into  and making it executable.

## Upload progress not enabled
Upon successful installation you may see the following message in the Status Report:

First, install the  package.
Next, use the pecl command to automatically download, compile and install the library:
 # pecl install uploadprogress
Finally, add to
 extension=uploadprogress
Restart Apache.
