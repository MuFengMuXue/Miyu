# Postorius

Postorius is a Django based management interface for Mailman.

## Installation
To use Postorius, a working web server setup is required (e.g. using Apache HTTP Server to forward to the WSGI directly, or using Nginx forwarding requests to an application server such as UWSGI).

Install the  package.

## Configuration
The web application is hosted on Django and is almost entirely configured through it: the web application is configured in  which is included by the default configuration in .

Change the default secret for the application:

Make sure to disable debugging when running in production:

To be able to configure a running mailman instance configuration options for its REST API have to be added to postorius' configuration.

Add a valid email configuration (so that the Django application can verify subscribers):

The valid hosts or domain names for the application need to be defined:

## Hosting
## Nginx and uWSGI
Postorius comes with a working uWSGI configuration file in .

Install  and , create a per-application socket for uWSGI (see UWSGI#Accessibility of uWSGI socket for reference) and enable .

For a local test setup, serving Postorius at http://127.0.0.1:80/postorius add the following Nginx configuration to your setup:

{{hc|/etc/nginx/postorius.conf|
server {
  listen 80;
  server_name localhost;
  charset utf-8;
  client_max_body_size 75M;
  root /usr/share/webapps/postorius;
  access_log /var/log/nginx/access.postorius.log;
  error_log /var/log/nginx/error.postorius.log;

  location /postorius_static {
    alias /var/lib/postorius/static;
  }

  location ~^/(accounts|admin|postorius)/(.*)$ {
    include /etc/nginx/uwsgi_params;
    uwsgi_pass unix:/run/postorius/postorius.sock;
  }
}
}}

## Setup
After first installation make sure to generate a database:

 django-admin migrate --pythonpath /usr/share/webapps/postorius/ --settings settings

Afterwards, the static data for the application needs to be collected:

 [postorius$ django-admin collectstatic --pythonpath /usr/share/webapps/postorius/ --settings settings

Create a superuser account for the Django application:

 django-admin createsuperuser --pythonpath /usr/share/webapps/postorius/ --settings settings

## Tips and tricks
## Set an Alias Domain
To use a domain in a [https://www.postfix.org/ADDRESS_CLASS_README.html#virtual_alias_class virtual alias domain setup with with postfix it is necessary to set the domain's . The domain name does not have to exist.

To set the , log in using the admin user (i.e.  by default) and alter the domain's settings it in the  menu.
