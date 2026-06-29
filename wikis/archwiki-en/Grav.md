# Grav

From Wikipedia:

:Grav is a free software, self-hosted content management system (CMS) written in the PHP programming language and based on the Symfony web application framework. It uses a flat file database for both backend and frontend.

:Grav is designed to have a shallow learning curve, and to be easy to set up. The focus of Grav is speed and simplicity, rather than an abundance of built-in features that come at the expense of complexity.

## Prerequisites
Grav comes with surprisingly few prerequisites by itself. Of course as a web application written in PHP it needs PHP. The only required PHP module is . A few others are also required but already part of the bare PHP installation. The following PHP modules are optional but highly recommended for better performance:

*  for increased cache performance
*  for native YAML processing dramatically increasing performance

Although Grav can serve the content on its own this article describes a setup with a full blown web server in front. So you need:

* A web server: Apache HTTP Server or nginx or others
* An application server: uWSGI (together with ) or FPM

The following combinations will be covered:

* nginx &rarr; uWSGI (plus uwsgi-plugin-php)
* nginx &rarr; FPM,
* Apache (using mod_proxy_uwsgi) &rarr; uWSGI (plus uwsgi-plugin-php)
* Apache (using mod_proxy_fcgi) &rarr; FPM

The installation of Grav complies with Arch Linux' web application package guidelines. This means among other details that Grav must be run with its own system user (grav). So it is not possible anymore to execute the PHP code directly in the Apache process by means of .

## Installation
Install the  package. This automatically takes care of installing the two requires dependencies  and . Also install  and  - preferrably as a dependency (). Comment the only line in . Do not modify , i.e. leave the only line commented. Activating these two extensions for Grav will be taken care of in other places (see below).

## Application server
There are two prevalent application servers that can be used to process PHP code: uWSGI or FPM. FPM as the name suggests is specialized on PHP. The protocol used between the web server and FPM is fastcgi. The tool is has been part of the PHP distribution since many years and is actively maintained. The downside being that the official documentation leaves much room for improvement. uWSGI on the other hand can serve code written in a handful of languages by means of language specific plugins. The protocol used is uwsgi (lowercase). The tool is extensively documented - albeit the sheer amount of documentation can become confusing and unwieldy. Maintainance has slowed down significantly - this applies especially for the PHP plugin.

## uWSGI
uWSGI has its own article. A lot of useful information can be found there. Install  and the plugin  - preferrably as dependencies, i.e. with . Setup of your Grav application requires only copying one file and defining one systemd service.

## grav.ini
Copy the Grav specific uWSGI setup file to the appropriate location.

 # cp /usr/share/webapps/grav/webserver-configs/uwsgi-grav.ini /etc/uwsgi/grav.ini

Make sure  is owned and only writeable by root, i.e. . This configuration is functional but feel free to adapt it to your liking. E.g. you might like to change  to your preferred timezone.

## systemd service
The package  provides a template unit file (). The instance ID (here grav) is used to pick up the right configuration file. So we start/enable .

In case you have more than a few (e.g. 2) services started like this and get the impression this is a waste of resource you might consider using emperor mode.

## FPM
In case you opt to use FPM as your application server install  - preferrably as a dependent package ().

You have to tweak its configuration a little bit.

## php-fpm.ini
It is a good practice to run FPM with its own version of . You thus avoid cluttering the standard INI file () with stuff only needed by FPM. There is a copy of a functional INI file in . Copy it to .

 # cp /usr/share/webapps/grav/webserver-configs/php-fpm.ini /etc/php

Make sure it is owned and only writeable by root. Something along . Feel free to customize the configuration as you see fit.

## grav.conf
You have to create a so called pool file for FPM. It is responsible for spawning a dedicated FPM process for the Grav application. Copy the version provided by the  package.

 # cp /usr/share/webapps/grav/webserver-configs/php-fpm.d/grav.conf /etc/php/php-fpm.d

Again make sure this pool file is owned and only writeable by root (i.e. ). You may tweak some settings (especially  and  to your liking.

## systemd service
FPM is run as a systemd service. You have to modify the service configuration to be able to run Grav. This is best achieved by means of a drop-in file.

The drop-in file has three purposes.

* It replaces the  line by a start command that uses the  covered in the previous section.
* It explicitly enables read/write access on  that would otherwise be inhibited by  in .
* It disables the  option set in  as this doesn't work together with  in .

Do not forget to start/enable .

## Web server
There is an abundance of web servers you can choose from. Whatever option you finally choose you have to keep in mind that the Grav application needs to be run with its own system user grav. So you probably need to forward your requests to one of the above mentioned application servers.

## nginx
Configuration of nginx is way beyond the scope of this article. See the relevant article for further information. The package  comes with a sample configuration file . This file is not functional as is. Use it as a starting point for your own configuration. Most likely you will have to copy it into  with an appropriate name and create the corresponding symbolic link in .

The sample file assumes you are using SSL/TLS and some ACME client (e.g. Certbot) to get your certificates. OCSP stapling is not configured.

Things you might have to adapt (not exhaustive):

* Your server name ( clauses 2x), i.e. the server part of the URL your Grav installation will be reachable with.
* The name of the certificate and key you use for SSL / TLS.
* If and where you want an access log written to.
* The location where Certbot (or any other ACME client) will put the domain verification challenges.
* The path under which your Grav installation will be reachable. (The part right to the server name &amp; port section in the URL.)
* What application server (uWSGI or FPM) you are using, i.e. how and where nginx will pass requests that need to trigger some PHP code.

There is no need to install any additional modules since nginx natively supports both protocols FastCGI and uwsgi.

Grav's documentation also covers setting up Grav with nginx. But be aware that the instructions are Ubuntu / Debian centric and do not mention uWSGI.

## Apache HTTP Server
Unfortunately upstream Grav does not provide a sample configuration file for Apache HTTP Server. At least there is a section in this wiki about how to integrate Apache with PHP by means of FPM and mod_proxy_fcgi. uWSGI's documentation has some information about how to integrate Apache with PHP by means of uWSGI and mod_proxy_uwsgi. Mind that the  package comes with both modules mod_proxy_fcgi and mod_proxy_uwsgi. They need to be loaded as required.

## Plugins
A lot of Grav's power comes from the large set of plugins that can be installed. Just follow the instructions on Grav's documentation how to install plugins.

Currently there are no grav-plugin-... packages that allow installing plugins via  (or some AUR wrapper). This will probably not change in the foreseeable future.

## Content
See the extensive documentation on Grav's website on how to create content with this CMS.

## Skeletons
Chances are the big empty board named Grav appears too intimidating to you. In this case you may want to use one of the many skeletons as a starting point. Skeletons are prefabricated bundles of Grav itself, some plugins, a theme and some sample content that give you some bits and pieces to play around with. Skeletons are supposed to be installed instead of a bare Grav installation. Unfortunately this makes it impossible to use a skeleton together with the  package.

With a bit of fiddling you can import the content of an arbitrary skeleton into your existing Grav installation.

# Download the desired skeleton.
# Extract the  directory:
# Replace the directories ,  and  in  with the corresponding directories from the extracted  directory.
# Fix ownership and permissions {{bc|# chown -R grav:http /var/lib/grav/user/{pages,plugins,themes}# chmod -R 640 /var/lib/grav/user/{pages,plugins,themes}# find /var/lib/grav/user/{pages,plugins,themes} -type d -exec chmod 750 {} \;}}
# Replace the configuration files   in  with the corresponding files from the extracted .
# Fix ownership and permissions {{bc|# chown grav:grav /etc/webapps/grav/config/{site,system}.yaml# chmod 644 /etc/webapps/grav/config/{site,system}.yaml}}

## Migrating from v1.6 to v1.7
Migrating from earlier package versions (< 1.7) will most likely require manual intervention. Errors may happen. So backup your data before trying an upgrade from earlier version! This comprises at least the  directory.

The upgrade will probably fail right away with lots of error messages complaining about files already existing under . Just delete this directory.

Since the last package of version 1.6 (v1.6.28, 2020-11-18)  has been upgraded from version 7 to 8. This may render some of your plugins non-functional.

Grav v1.7 has become stricter in many ways. See Grav's migration guide about details.

Do not try to tweak your setup to use system user http as used to be. For good reasons Arch Linux' web application package guidelines dictates to use a dedicated system user (here grav) to run the application.

Probably the best migration strategy is to backup the  directory, uninstall Grav and all dependent packages, remove all remnants of the Grav installation (including all Grav specific configurations with your web server and application server), update your system (including PHP) and then install Grav from scratch. When everything is set up and your server successfully presents Grav's default page you can start to restore your previous content.

## Upgrade
Upgrading Grav itself must exclusively be done by pacman (or some AUR wrapper)!

Unlike upgrading Grav itself, upgrading plugins and themes must be done with  or via the admin plugin.

Also not recommended is to download Grav releases as ZIP archives directly from Grav's GitHub project site and copy around stuff in the filesystem. Only do so when you know exactly what you are doing.
