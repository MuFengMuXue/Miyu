# InvoicePlane

InvoicePlane is a self-hosted open source application for managing your quotes, invoices, clients and payments.

## Installation
Install the  package.

## Configuration
## Database
Here is an example on how you could setup a database for Invoiceplane with MariaDB called  for the user  identified by the password :

## Web Server
## Apache
Create the Apache HTTP Server configuration file:

And include it in :
 # InvoicePlane configuration
 Include conf/extra/invoiceplane.conf

## Lighttpd
Make an alias for invoiceplane in your Lighttpd configuration.

  alias.url = ( "/invoiceplane" => "/usr/share/webapps/invoiceplane/")

Then enable ,  and  in the  section.

## nginx
Here is an example configuration to include in  for a subdomain with php-fpm:

{{hc|/etc/nginx/sites-available/invoiceplane.conf|
server {

listen 443 ssl http2;
listen ssl http2;

        add_header X-Frame-Options "SAMEORIGIN";

        root /usr/share/webapps/invoiceplane;
        index index.php;

        server_name invoice.domain.tld;

        client_body_timeout 60;

    location / {
        try_files $uri $uri/ /index.php?q=$uri&$args;
    }

    location ~ \.php$ {
        fastcgi_param PHP_ADMIN_VALUE open_basedir=/tmp:/usr/share/webapps/invoiceplane:/dev/urandom:/usr/share/php;
        fastcgi_split_path_info ^(.+\.php)(/.+)$;
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $realpath_root$fastcgi_script_name;
        fastcgi_param DOCUMENT_ROOT $realpath_root;
        fastcgi_param PATH_INFO $fastcgi_path_info;
        fastcgi_pass unix:/run/php-fpm/php-fpm.sock;
        client_max_body_size 100M;
    }
}
}}

## Explicitly permit InvoicePlane directories for php-fpm
Since version 7.4 php-fpm is hardened per default and revokes read/write access on  (and sub-directories). Therefore it is also necessary to explicitly give permissions on  directories.

Create a drop-in file for .

Add and save it with the following content:

Afterwards restart the  service and assign write permissions to the  user.

## Installation wizard
Once database and webserver have been setup, visit the installation wizard page at  and follow the instructions.

## Localization
If you want to choose a different language than English visit [https://wiki.invoiceplane.com/en/1.0/system/translation-localization Translation / Localization.
