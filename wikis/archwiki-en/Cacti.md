# Cacti

Cacti is a web-based system monitoring and graphing solution.

## Installation
To use cacti, you need a working web server (e.g. Nginx or Apache HTTP Server) setup, that forwards requests to an application server (e.g. uWSGI or ).

Next, install  and configure MariaDB, if a local MySQL server will be used.

## Configuration
To serve cacti top level instead of under  (i.e.  instead of ) use the  configuration option:

## PHP
Cacti requires the following PHP extensions to be enabled:

Cacti needs certain directories and executables in PHP's  to function properly:

 /tmp/:/usr/share/webapps/cacti:/etc/webapps/cacti:/var/cache/cacti:/var/lib/cacti:/var/log/cacti:/proc/meminfo:/usr/bin/rrdtool:/usr/bin/snmpget:/usr/bin/snmpwalk:/usr/bin/snmpbulkwalk:/usr/bin/snmpgetnext:/usr/bin/snmptrap:/usr/bin/sendmail:/usr/bin/php:/usr/bin/spine:/usr/share/fonts/TTF/

Cacti requires  to be set in . Check upstream documentation [https://www.php.net/manual/en/datetime.configuration.php#ini.date.timezone and time zone for reference.

## SNMP
If it is necessary for cacti to monitor the machine that it is running on, configure snmpd.

## MySQL
Cacti needs its own database in which to store its data, and a database user account to access the database.

Run the following commands as root:

Alternatively, use PhpMyAdmin to achieve the same results:

* Create an empty database called .
* Import the file  into the  database.
* Create a user , and grant this user privileges to access the  database.

Add the database details:

## Hosting
## Apache
The apache web server can serve dynamic web applications with the help of modules, such as mod_proxy_fcgi or mod_proxy_uwsgi.

## php-fpm
Install and configure Apache HTTP Server with php-fpm.
Use a pool run as user and group .
The socket file should be accessible by the  user and/or group, but needs to be located below .

Include the following configuration in your Apache HTTP Server configuration (i.e. ) and restart the web server:

The file  also controls access. Configure or remove it.

## Nginx
Nginx can proxy application servers such as  and uWSGI, that run a dynamic web application.
The following examples describe a folder based setup over a non-default port (for simplicity).

## php-fpm
Install . Setup nginx with php-fpm and use a pool run as user and group .
The socket file should be accessible by the  user and/or group, but needs to be located below . This can be achieved by adding the following lines to the php-fpm configuration and restarting it.

Add the following configuration for nginx and restart it.
{{hc|/etc/nginx/sites-available/cacti.conf|
server {
  listen 8081;
  server_name cacti;
  root /usr/share/webapps/cacti/;
  index index.php;
  charset utf-8;

  access_log /var/log/nginx/cacti-access.log;
  error_log /var/log/nginx/cacti-error.log;

  location / {
    try_files $uri $uri/ index.php;
  }

  location ~* \.php$ {
    fastcgi_split_path_info ^(.+\.php)(/.+)$;
    include fastcgi_params;
    fastcgi_pass unix:/run/cacti/cacti.sock;
    fastcgi_index index.php;
    include fastcgi_params;
    fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
    fastcgi_buffer_size 16k;
    fastcgi_buffers 4 16k;
  }
}
}}

## uWSGI
Install , create a per-application socket for uWSGI (see UWSGI#Accessibility of uWSGI socket for reference) and enable and start the  unit.

Add the following configuration for nginx and restart nginx.

{{hc|/etc/nginx/sites-available/cacti.conf|
    server {
      listen 8081;
      server_name cacti;
      root /usr/share/webapps/cacti/;
      index index.php;
      charset utf-8;

      access_log /var/log/nginx/cacti-access.log;
      error_log /var/log/nginx/cacti-error.log;

      location / {
        try_files $uri $uri/ index.php;
      }

      # pass all .php or .php/path urls to uWSGI
      location ~ ^(.+\.php)(.*)$ {
        include uwsgi_params;
        uwsgi_modifier1 14;
        uwsgi_pass unix:/run/cacti/cacti.sock;
      }
    }
}}

## Setup
Open a browser and go to http://your_server/cacti/. You should be welcomed with the cacti installer.

* Login with username "admin" and password "admin".
* Change the password as requested, click Save.
* Follow the remaining install steps and recommendations.
* (Optional) If you chose to install spine, follow these instructions to set it up.
** Click on Settings, on the left panel of the Console tab.
** Select the Poller tab.
** Change Poller Type to spine.
** Adjust any other settings on the page as desired, then click Save.
** Select the Paths tab.
** Set Spine Poller File Path to  and click Save.

## Tips and tricks
## Spine
Optionally, install , a faster poller for cacti. configure it with database access details:

## systemd
Cacti uses a poller to collect data, so create a systemd service to run , and a timer to run the service every 5 minutes:
