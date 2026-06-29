# PostfixAdmin

PostfixAdmin is a web interface for Postfix used to manage mailboxes, virtual domains and aliases.

## Installation
To use PostfixAdmin, you need a working web server setup. You can either choose a web server, that can serve the web application directly (such as Apache HTTP Server), or a setup in which a web server (e.g Nginx) forwards requests to an application server (e.g. UWSGI or ).

Next, install the  package.

## Configuration
Edit the PostfixAdmin configuration file, globally change all instances of change-this-to-your.domain.tld to an appropriate value:

If installing dovecot and you changed the password scheme in dovecot (to SHA512-CRYPT for example), reflect that with Postfix

As of dovecot 2, dovecotpw has been deprecated.  You will also want to ensure that your configuration reflects the new binary name.

## Hosting
## Apache
The apache web server can serve dynamic web applications with the help of modules, such as mod_proxy_fcgi or mod_proxy_uwsgi.

## php-fpm
Install and configure Apache HTTP Server with php-fpm.
Use a pool run as user and group .
The socket file should be accessible by the  user and/or group.

Include the following configuration in your Apache HTTP Server configuration (i.e. ) and restart the web server:

Create a pool for postfixadmin and restart php-fpm.service:

To only allow localhost access to postfixadmin (for heightened security), add this to the previous  directive:
    Order Deny,Allow
    Deny from all
    Allow from 127.0.0.1

## Nginx
Nginx can proxy application servers such as  and uWSGI, that run a dynamic web application.
The following examples describe a folder based setup over a non-default port (for simplicity).

## php-fpm
Install  and . Setup nginx with php-fpm and use a pool run as user and group .
The socket file should be accessible by the  user and/or group, but needs to be located below . This can be achieved by adding the following lines.

You will need to at least activate ,  and  extensions in . Make sure you also add  to  in your . Restart  for all these to take effect.

Add the following configuration for nginx and restart it.
{{hc|/etc/nginx/sites-available/postfixadmin.conf|
    server {
      listen 8081;
      server_name postfixadmin;
      root /usr/share/webapps/postfixadmin/public/;
      index index.php;
      charset utf-8;

      access_log /var/log/nginx/postfixadmin-access.log;
      error_log /var/log/nginx/postfixadmin-error.log;

      location / {
        try_files $uri $uri/ index.php;
      }

      location ~* \.php$ {
        fastcgi_split_path_info ^(.+\.php)(/.+)$;
        include fastcgi_params;
        fastcgi_pass unix:/run/postfixadmin/postfixadmin.sock;
        fastcgi_index index.php;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_buffer_size 16k;
        fastcgi_buffers 4 16k;
      }
    }
}}

## uWSGI
Install , create a per-application socket for uWSGI (see UWSGI#Accessibility of uWSGI socket for reference) and activate the  unit.

Add the following configuration for nginx and restart nginx.

{{hc|/etc/nginx/sites-available/postfixadmin.conf|
    server {
      listen 8081;
      server_name postfixadmin;
      root /usr/share/webapps/postfixadmin/public/;
      index index.php;
      charset utf-8;

      access_log /var/log/nginx/postfixadmin-access.log;
      error_log /var/log/nginx/postfixadmin-error.log;

      location / {
        try_files $uri $uri/ index.php;
      }

      # pass all .php or .php/path urls to uWSGI
      location ~ ^(.+\.php)(.*)$ {
        include uwsgi_params;
        uwsgi_modifier1 14;
        uwsgi_pass unix:/run/postfixadmin/postfixadmin.sock;
      }
    }
}}

## Setup
Finally, navigate to http://127.0.0.1/postfixadmin/setup.php if having used Apache or http://127.0.0.1:8081/setup.php for Nginx  to finish the setup. Generate your setup password hash at the bottom of the page once it is done. Write the hash to the configuration file

Now you can create a superadmin account at http://127.0.0.1/postfixadmin/setup.php if having used Apache or http://127.0.0.1:8081/setup.php for Nginx.

## Tips and tricks
## Pacman hook
Sometimes the database needs to be upgraded after a version bump. You will see a message saying 'The PostfixAdmin database layout is outdated' on the login page in such case.

You can set up a hook that runs the needed upgrade.php script automatically via a pacman hook:

## Troubleshooting
## Configuration not found
If you go to yourdomain/postfixadmin/setup.php and the application states, that it is unable to find config.inc.php, add  to the  line in  (see PHP#Configuration for reference).

## Blank page on access
If you get a blank page check the syntax of the configuration with .
