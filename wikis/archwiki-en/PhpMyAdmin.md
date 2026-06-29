# PhpMyAdmin

phpMyAdmin is a web-based tool to help manage MariaDB or MySQL databases, written primarily in PHP and distributed under the GNU GPL.

## Installation
Install the  package.

## Running
## PHP
Make sure the PHP mariadb and  extensions have been enabled.

Optionally you can enable  and  for compression support.

## Apache
Set up Apache to use PHP as outlined in the Apache HTTP Server#PHP article.

Create the Apache configuration file:

And include it:

After making changes to the Apache configuration file, restart .

## Lighttpd
Configuring Lighttpd, make sure it is able to serve PHP files and  has been enabled.

Add the following alias for PhpMyAdmin to the config:

 alias.url = ( "/phpmyadmin" => "/usr/share/webapps/phpMyAdmin/")

## Nginx
Make sure to set up nginx#FastCGI and use nginx#Server blocks to make management easier.

By preference, access phpMyAdmin by subdomain, e.g. :
{{hc|/etc/nginx/sites-available/pma.domain.tld|2=
server {
    server_name pma.domain.tld;
    ; listen 80; # also listen on http
    ; listen listen 443 ssl;
    listen [:::443 ssl;
    http2 on;
    index index.php;
    access_log /var/log/nginx/pma.access.log;
    error_log /var/log/nginx/pma.error.log;

    # Allows limiting access to certain client addresses.
    ; allow 192.168.1.0/24;
    ; allow my-ip;
    ; deny all;

    root /usr/share/webapps/phpMyAdmin;
    location / {
        try_files $uri $uri/ =404;
    }

    error_page 404 /index.php;

    location ~ \.php$ {
        try_files $uri $document_root$fastcgi_script_name =404;

        fastcgi_split_path_info ^(.+\.php)(/.*)$;
        fastcgi_pass unix:/run/php-fpm/php-fpm.sock;
        fastcgi_index index.php;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;

        fastcgi_param HTTP_PROXY "";
        fastcgi_param HTTPS on;
        fastcgi_request_buffering off;
   }
}
}}

Or by subdirectory, e.g. :
{{hc|/etc/nginx/sites-available/domain.tld|2=
server {
    server_name domain.tld;
    listen 443 ssl;
    listen ssl;
    http2 on;
    index index.php;
    access_log /var/log/nginx/domain.tld.access.log;
    error_log /var/log/nginx/domain.tld.error.log;

    root /srv/http/domain.tld;
    location / {
        try_files $uri $uri/ =404;
    }

    location /phpMyAdmin {
        root /usr/share/webapps/phpMyAdmin;
    }

    # Deny static files
    location ~ ^/phpMyAdmin/(README|LICENSE|ChangeLog|DCO)$ {
       deny all;
    }

    # Deny .md files
    location ~ ^/phpMyAdmin/(.+\.md)$ {
      deny all;
   }

   # Deny setup directories
   location ~ ^/phpMyAdmin/(doc|sql|setup)/ {
      deny all;
   }

   #FastCGI config for phpMyAdmin
   location ~ /phpMyAdmin/(.+\.php)$ {
      try_files $uri $document_root$fastcgi_script_name =404;

      fastcgi_split_path_info ^(.+\.php)(/.*)$;
      fastcgi_pass unix:/run/php-fpm/php-fpm.sock;
      fastcgi_index index.php;
      fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
      include fastcgi_params;

      fastcgi_param HTTP_PROXY "";
      fastcgi_param HTTPS on;
      fastcgi_request_buffering off;
   }
}
}}

## Configuration
The main configuration file is located at .

## Define a remote MySQL server
If the MySQL server is a remote host, append the following line to the configuration file:
 $cfg['Servers'= 'example.com';

## Using setup script
To allow the usage of the phpMyAdmin setup script (e.g. http://localhost/phpmyadmin/setup), make sure  is writable for the  user:

 # mkdir /usr/share/webapps/phpMyAdmin/config
 # chown http:http /usr/share/webapps/phpMyAdmin/config
 # chmod 750 /usr/share/webapps/phpMyAdmin/config

## Add blowfish_secret passphrase
It is required to enter a unique 32 characters long string to fully use the blowfish algorithm used by phpMyAdmin, thus preventing the message  ERROR: The configuration file now needs a secret passphrase (blowfish_secret):

## Enabling Configuration Storage
Extra options such as table linking, change tracking, PDF creation, and bookmarking queries are disabled by default, displaying The phpMyAdmin configuration storage is not completely configured, some extended features have been deactivated. on the homepage.

In , uncomment (remove the leading "//"s), and change them to your desired credentials if needed:

## Setup database
Two options are available to create the required tables:

* Import  by using PhpMyAdmin.
* Execute  in the command line.

## Setup database user
To apply the required permissions for , execute the following query:

In order use the bookmark and relation features, set the following permissions:
 GRANT SELECT, INSERT, UPDATE, DELETE ON phpmyadmin.* TO 'pma'@'localhost';

Re-login to ensure the new features are activated.

## Enabling template caching
Edit  to add the line:

 $cfg['TempDir' = '/tmp/phpmyadmin';

## Remove config directory
Remove temporary configuration directory once configuration is done. This will also suppress warning from web interface:

 # rm -r /usr/share/webapps/phpMyAdmin/config

## Install themes
Themes are located in . You can find new themes in https://www.phpmyadmin.net/themes/

You can simply download and extract the new theme and it will work after phpmyadmin refresh. However, you have to download theme for the correct version of phpmyadmin, themes for older versions will not work.
