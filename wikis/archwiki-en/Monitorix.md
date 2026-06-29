# Monitorix

Monitorix is an open source, lightweight system monitoring tool designed to monitor as many services and system resources as possible. It has been created to be used under production UNIX/Linux servers, but due to its simplicity and small size many use it on embedded devices as well.

## Installation
Install the package .

## Configuration
Edit  to match graphing options and system-specific variables.  For a complete list of options and features, see .

Most of the user settings are self explanatory based on the commented text within the configuration file itself.

Monitorix comes with a light, built-in webserver; via the dependency . It is, however, disabled by default. To use it, change the configuration option as follows:

See the configuration file for the other related options, for example access restrictions, or #Configure an external webserver.

## Start and viewing data
Start/enable .

To view system stats, using the perl-http-server, simply point a browser to http://localhost:8080/monitorix to see the data.

## Configure an external webserver
## Lighttpd
 is another option.

By default, cgi support is not enabled in lighttpd.  To enable it and to assign perl to process .cgi files, add the following two lines to :

 server.modules		= ( "mod_cgi" )
 cgi.assign		= ( ".cgi" => "/usr/bin/perl" )

## Apache
 is yet another option.

## Nginx
 can be used as a reverse proxy/webserver by adding the following server block the nginx config:
{{bc|
server {
    listen       80;
    server_name  your.domain.com;

    location / {
       proxy_pass http://127.0.0.1:8080;
       proxy_buffering off;
    }

    location ~ ^/monitorix/(.+\.(csspng))$ {
        alias /srv/http/monitorix/$1;
    }
}
}}

Also add  to .

## Using tmpfs to Store RRD databases
 is a package which provides a pseudo-daemon that makes use of tmpfs to store RRD Databases for Monitorix.  Doing so will greatly reduce hdd reads/writes.
