# Apache HTTP Server/mod perl

From the project:

:mod_perl brings together the full power of the Perl programming language and the Apache HTTP Server. You can use Perl to manage Apache, respond to requests for web pages and much more.

## Installation
Install the  package.

## Configuration
Load the module via the main Apache configuration file:

## Allow perl to execute scripts for certain directories
There are two possible methods to enable the  module:

* #Using virtual hosts, or
* #For a subdirectory.

## Using virtual hosts
Add a virtual host with settings. For example:

Ensure  includes the created virtual host:

 Include conf/extra/httpd-vhosts.conf

Make sure it does not have !

Add "perlwebtest" as localhost in , using the machine's hostname for :

 127.0.0.1	localhost yourhostname perlwebtest

## For a subdirectory
Add the following to the main configuration file:

## Turn on perl for directory listings
Create  as well:

Then include it in :

## Try it out
Create  in :

Restart Apache's  and let it reload the configuration.

Finally, depending on chosen alternative configuration, visit

* http://perlwebtest for #Using virtual hosts, or
* http://localhost/perlwebtest for #For a subdirectory.
