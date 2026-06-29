# PhpPgAdmin

phpPgAdmin is a web-based tool to help manage PostgreSQL databases using an PHP frontend.

## Installation
PhpPgAdmin requires a web server with PHP, such as Apache. To set it up, see Apache HTTP Server and Apache HTTP Server#PHP.

Install the  package.

## Configuration
## PHP
You need to enable the  extension in PHP by editing  and uncommenting the following line:

 extension=pgsql

You need to make sure that PHP can access . Add it to  in  if necessary:

 open_basedir = /srv/http/:/home/:/tmp/:/usr/share/pear/:/usr/share/webapps/:/etc/webapps

## Web server
## Apache
Create the Apache configuration file:

And include it in :

 # phpPgAdmin configuration
 Include conf/extra/phppgadmin.conf

You also need to connect php7:

 Include conf/extra/php7_module.conf
 LoadModule php7_module modules/libphp7.so

By default, everyone can see the phpPgAdmin page, to change this, edit  to your liking. For example, if you only want to be able to access it from the same machine, replace  by .

## Lighttpd
The php setup for lighttpd is exactly the same as for apache.
Make an alias for phppgadmin in your lighttpd config.

  alias.url = ( "/phppgadmin" => "/usr/share/webapps/phppgadmin/")

Then enable mod_alias, mod_fastcgi and mod_cgi in your config ( server.modules section )

Make sure lighttpd is setup to serve php files, Lighttpd#FastCGI

Restart lighttpd and browse to http://localhost/phppgadmin/index.php

## nginx
Make sure to set up nginx#FastCGI with separate configuration file for PHP as shown in nginx#nginx configuration.

Using this method, you will access PhpPgAdmin as .

You can setup a sub domain (or domain) with a server block such as:

{{bc|
server {
    server_name     phppgadmin.;
    root    /usr/share/webapps/phppgadmin;
    index   index.php;
    include php.conf;
}
}}

## phpPgAdmin configuration
phpPgAdmin's configuration file is located at .

If your PostgreSQL server is on the , you may need to edit the following line:

 $conf= '';

to

 $conf['servers'= 'localhost';

## Accessing your phpPgAdmin installation
Your phpPgAdmin installation is now complete. Before start using it you need to restart your apache server by restarting .

You can access your phpPgAdmin installation by going to http://localhost/phppgadmin/

## Troubleshooting
## Login disallowed for security reasons
If extra login security is true, then logins via phpPgAdmin with no password or certain usernames (pgsql, postgres, root, administrator) will be denied. Only set this to  once you have read the FAQ and understand how to change PostgreSQL's  to enable passworded local connections.

Edit  and change the following line:

 $conf['extra_login_security' = true;

to:

 $conf'extra_login_security' = false;

Then restart .
