# Pydio

Pydio (formerly AjaXplorer) is an open source web application, written in PHP, for file sharing and synchronization.

## Installation
Install the  package. Further you will need a database (e.g. MariaDB), a web server (Apache HTTP Server, Lighttpd or Nginx) with PHP-support. You may refer following sites:

## Configuration
Make sure to adjust following variables to these minimal values in your :

In this configuration, we will configure the Nginx web server to serve Pydio on localhost in the root location without SSL enabled (even though it is recommended to use it with SSL). First, place a copy of the Pydio Nginx configuration
 # cp /usr/share/doc/pydio/nginx.conf.sample /etc/webapps/pydio/nginx.conf
replace the domain name
 # sed -i 's/pydio.example.com/localhost/g' /etc/webapps/pydio/nginx.conf
and reference this configuration file in the main nginx.conf:
{{hc|/etc/nginx/nginx.conf|

http {
    include /etc/webapps/pydio/nginx.conf;
    [...
 }
}}
Here is an example on how you could setup a database for Pydio with MariaDB called  for the user  identified by the password :

Do not forget to (re)start your services (e.g.  and )!

Visit the installation wizard page at http://127.0.0.1/ and follow the instructions.
