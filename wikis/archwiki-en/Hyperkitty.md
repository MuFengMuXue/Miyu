# Hyperkitty

Hyperkitty is a Django based archiver and archive interface for Mailman.

## Installation
To use Hyperkitty, a working web server setup is required (e.g. using Apache HTTP Server to forward to the WSGI directly, or using Nginx forwarding requests to an application server such as UWSGI).

Install the  package.

## Configuration
The web application is configured in  (which is included by the default configuration in ).

Change the default secret for the application:

Make sure to disable debugging when running in production:

Add a valid email configuration (so that the Django application can verify subscribers):

To connect with a running mailman instance's REST API, configuration options have to be added to hyperkitty's configuration.

To configure the archive integration with a mailman instance first setup the  integration with hyperkitty on mailman's side and then configure hyperkitty to accept those connections:

The valid hosts or domain names for the application need to be defined:

## Hosting
## Nginx and uWSGI
Hyperkitty comes with a working uWSGI configuration file in .

Install  and , create a per-application socket for uWSGI (see UWSGI#Accessibility of uWSGI socket for reference) and activate the  unit.

For a local test setup, serving Hyperkitty at http://localhost/hyperkitty/ add the following Nginx configuration to your setup:

{{hc|/etc/nginx/hyperkitty.conf|
server {
  listen 80;
  server_name localhost;
  charset utf-8;
  client_max_body_size 75M;
  root /usr/share/webapps/hyperkitty;
  access_log /var/log/nginx/access.hyperkitty.log;
  error_log /var/log/nginx/error.hyperkitty.log;

  location /hyperkitty_static {
    alias /var/lib/hyperkitty/static;
  }

  location ~^/(hyperkitty|user-profile)/(.*)$ {
    include /etc/nginx/uwsgi_params;
    uwsgi_pass unix:/run/hyperkitty/hyperkitty.sock;
  }
}
}}

## Setup
After first installation make sure to generate a database:

 django-admin migrate --pythonpath /usr/share/webapps/hyperkitty/ --settings settings

Afterwards, the static data for the application needs to be collected:

 [hyperkitty$ django-admin collectstatic --pythonpath /usr/share/webapps/hyperkitty/ --settings settings

To compress the data, run the following:

 django-admin compress --pythonpath /usr/share/webapps/hyperkitty/ --settings settings

Enable and start the  systemd service for required asynchronous operations on the web application.

Populate the database with default data (when setting up for the first time):

 [hyperkitty$ django-admin loaddata --pythonpath /usr/share/webapps/hyperkitty/ --settings settings first_start

Create a superuser account for the Django application:

 django-admin createsuperuser --pythonpath /usr/share/webapps/hyperkitty --settings settings

Log in to the admin interface of the Django application at http://localhost/hyperkitty/admin to be able to add more  besides the default  or to add additional .

## Tips and tricks
## Importing mailman2 archives
Hyperkitty can import archives from mailman }} tag
* : the content will appear before the  tag
* : the content will appear before the  tag

## Xapian search backend
Hyperkitty can make use of a Xapian based search backend. Install the  package and configure the backend:

{{hc|/etc/webapps/hyperkitty/settings_local.py|2=
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'xapian_backend.XapianEngine',
        'PATH': "/var/lib/hyperkitty/data/xapian_index",
    },
}
}}

Make sure to create the search index for all lists afterwards. Run the following command as the  user (e.g. using sudo or su):

 [hyperkitty$ django-admin update_index --pythonpath /usr/share/webapps/hyperkitty --settings settings

## Troubleshooting
## SMTP AUTH extension not supported by server
If upon first login with the admin user a  is thrown (logged to ), make sure to verify the  settings in .

By default e.g.  is set to  which might trigger a failed login via SMTP.
