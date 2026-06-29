# Bareos

Bareos (Backup Archiving Recovery Open Sourced) is a backup software, originally forked from the Bacula project. It is network-based, multi-client and very flexible with an architecture oriented towards scalability. Thus the learning curve might be considered somewhat steep. The project is backed by the commercial company Bareos GmbH & Co. KG, based in Germany.

The open-source project site is located at https://www.bareos.com/, the source code is hosted on Github https://github.com/bareos/

## Installation
There is a group of packages in AUR that will install the software, but there is some minor manual labour necessary to make it run. It is recommended to use Bareos with PostgreSQL, since use with MariaDB/MySQL was deprecated with version 19.0.

Install the requirements first:

*  Apache Webserver
*  Apache PHP module
*  PostgreSQL Database
*  PostgreSQL module for PHP

It is recommended to install the following packages for a minimum working featureset, backing up to local storage with postgresql catalog support:

*
*
*
*
*
*
*

Additionally, install these packages for a management webapp:
*
*  (if you would rather use nginx instead of apache)

## Configuration
## Pre-Configuration
Minimal configuration for Apache HTTP Server and PHP:

* Follow the steps described in Apache HTTP Server#Using libphp
* You will also need to enable the  module, to do this, modify  and uncomment:

 LoadModule rewrite_module modules/mod_rewrite.so

If you are using a standard configuration file, change the following lines to the following:

 #LoadModule mpm_event_module modules/mod_mpm_event.so
 LoadModule mpm_prefork_module modules/mod_mpm_prefork.so

 # bareos-webui
 Include conf/extra/bareos-webui.conf

 LoadModule php_module modules/libphp.so
 Include conf/extra/php_module.conf

To use PHP7 you need to make the following fixes:

 LoadModule php7_module modules/libphp7.so
 Include conf/extra/php7_module.conf

* Then enable the  extension in PHP as listed in PHP#PostgreSQL
* And enable the  extension in PHP

Fixes in /etc/php7/php.ini or /etc/php7/php.ini:

 open_basedir = /tmp/:/usr/share/bareos-webui/:/etc/bareos-webui:
 extension=gettext
 extension=pgsql

Minimal configuration for PostgreSQL

* Initialize the database by following PostgreSQL#Initial configuration

Start/enable  and .

## Initial setup
These steps mostly follow the Instructions from docs.bareos.org, and include some Arch-specifics.

* Setup the Bareos database

 $ /usr/lib/bareos/scripts/create_bareos_database
 $ /usr/lib/bareos/scripts/make_bareos_tables
 $ /usr/lib/bareos/scripts/grant_bareos_privileges

* Copy default configuration files to the  directory

 # cp -r /usr/share/bareos/config/* /etc/bareos/
 # chown -R bareos:bareos /etc/bareos

* In versions prior to v21: Set the correct DB driver in the catalog configuration file

* Now enable/start ,  and

## Configure Web-UI
## Add a user for the webui
* to start the interactive management shell, run:

 $ bconsole

* inside the shell, you get a  as prompt, where you can enter the following commands:

 *reload
 *configure add console name=admin password=password profile=webui-admin tlsenable=false
 *quit

{{Warning|The password you specify here will be saved in a plain text configuration file as {{ic|/etc/bareos/bareos-dir.d/console/{username}.conf}}.}}

## Setup Apache
* we need to fix a path in two lines:

* in the file  add the line:

 Include conf.d/extra/bareos-webui.conf

* restart Apache

Now you can now login to Bareos Webui at  and login using the account you just created with .
