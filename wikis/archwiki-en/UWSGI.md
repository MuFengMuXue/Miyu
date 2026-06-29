# UWSGI

uWSGI is a fast, self-healing and developer/sysadmin-friendly application container server coded in pure C.

There are alternatives written in Python such as .

## Installation
Install the  package. Plugins need to be installed separately (their package names start with ).

## Configuration
Web applications served by uWSGI are configured in , where each of them requires its own configuration file (ini-style). Details can be found in the uWSGI documentation.

Alternatively, you can run uWSGI in Emperor mode (configured in ). It enables a single uWSGI instance to run a set of different apps (called vassals) using a single main supervisor (called emperor).

## Web applications
uWSGI supports many different languages and thus also many web applications.
As an example the configuration file  and the prior installation of the plugin needed for your web application is assumed.

## Python
The following is a simple example for a Python application.

It is also possible to run uWSGI separately with the following syntax for instance:

 $ uwsgi --socket 127.0.0.1:3031 --plugin python2 --wsgi-file ~/foo.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191 --uid --gid

You should avoid running this command as root.

## PHP
The following is a simple example for a PHP based website.

## Web server
uWSGI can be the backend to many web servers, that support the forwarding of access. The following are examples for configurations.

## Nginx
nginx can redirect access towards unix sockets or ports (on localhost or remote machine), depending on your web application.

{{hc|/etc/nginx/example.conf|
# ...
# forward all access to / towards
location / {
  root /usr/share/nginx/html;
  index index.html index.htm;
  include uwsgi_params;
  # this is the correct uwsgi_modifier1 parameter for a php based application
  uwsgi_modifier1 14;
  # uncomment the following if you want to use the unix socket instead
  # uwsgi_pass unix:/var/run/uwsgi/example.sock;
  # access is redirected to localhost:3031
  uwsgi_pass 127.0.0.1:3031;
}
# ...
}}

## Nginx (in chroot)
First create ini file that will point to your application:

Since we are chrooting to  above configuration will result in following unix socket being created

You will need to disable notifications within your service file:

After modification make sure to reload to incorporate the new or changed units.

You are then free to enable and start .

Edit  and add new  section within it that would contain at least following:
{{hc|/srv/http/etc/nginx/nginx.conf|
...
    server
    {
        listen       80;
        server_name  127.0.0.1;
        location /
        {
            root   /www/application1;
            include uwsgi_params;
            uwsgi_pass unix:/run/application1.sock;
        }

        error_page   500 502 503 504  /50x.html;
        location = /50x.html
        {
            root   /usr/share/nginx/html;
        }
    }
...
}}

Make sure to now restart  to have your  be served at .

## Running uWSGI
If you plan on using a web application all the time (without it being activated on demand), you can simply start and enable .

If you plan on having your web application be started on demand you can start and enable .

To use the Emperor mode, start and enable .

To use socket activation of this mode start and enable .

## Tips and tricks
Some functionality, that uWSGI offers is not accessible by using the systemd service files provided in the official repositories.
Changes to them are explained in the following sections. For further information see === Socket activation ===

Using socket activation, you want to
* direct your web server to a unix socket and thereby start your uWSGI instance running the application
* you most likely want to have the application be closed by uWSGI after a certain idle time
* you want your web server be able to start the application again, once it is accessed

uWSGI offers settings, with which you can have the instance close the application:

The current  file however does not allow this, because systemd treats non-zero exit codes as failure and thereby marking the unit as failed and additionally the  directive makes a closing after idle time useless.
A fix for this is to add the exit codes, that uWSGI may provide after closing an application by itself to a list, that systemd will treat as success by using the  directive (for further information see [https://sleepmap.de/2016/securely-serving-webapps-using-uwsgi/).

This will allow for proper socket activation with kill-after-idle functionality.

## Hardening uWSGI service
Web applications are exposed to the wild and depending on their quality and the security of their underlying languages, some are more dangerous to run, than others.
A good way to start dealing with possible unsafe web applications is to jail them. systemd has some functionality, that can be put to use.
Have a look at the following example (and for further information see  and === Accessibility of uWSGI socket ===

The default (per application) socket unit () in  allows read and write access to any user on the system.
However, systemd allows for a more finely granulated access management (see ), with which the access to a unix socket can be made more restrictive.

By creating it below a webapp specific directory below  (needs to be created using tmpfiles beforehand - for reference see Web application package guidelines) and modifying its group and file permissions, the socket is only accessible to root and the web server and allows the web application to run as its own user:

## Troubleshooting
## Apache httpd
## AH00957: uwsgi: attempt to connect to 127.0.0.1:0 (*) failed
The default uWSGI port (3031) does not work (currently?) with Apache httpd server. See [https://github.com/unbit/uwsgi/issues/1491 for details.
