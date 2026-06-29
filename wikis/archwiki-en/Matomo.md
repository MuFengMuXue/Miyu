# Matomo

Matomo, formerly Piwik, is an open source web analysis tool licensed under the GNU General Public License 3. The software is written in PHP and is accessed over the web browser. The core idea of the project is privacy as when using third party website analysis providers website owners are giving away all of their users' data.

With one running instance, multiple websites can be analysed by loading some JavaScript on the target websites.

## Installation
## PHP configuration
PHP needs to be configured properly for Matomo to install and work.

First, enable MySQL support as described in PHP#MySQL/MariaDB. Do so by editing . Uncomment  and  by removing the preceding semicolon each.

In general, comments are indicated by preceding semicolons.

Moreover, enable  and .

## Matomo
Install the package  or .

## Application configuration
## Disable development mode
Run .

## Geolocation
This feature can be deactivated or, with no installation needed, Matomo can guess the visitors' location by their set browser language which is not reliable information for geographical locations.

 already comes with a geolocation database. To replicate, download the  file from https://db-ip.com/db/download/ip-to-city-lite and install it to .

Alternatively, use  and starting/enabling . Beware that a MaxMind account is needed.

The last option to choose is to use an HTTP module like .

## FastCGI
Use any programme for FastCGI to run PHP websites. Instructions are given for the most common application .

## PHP-FPM
Install the  package and start/enable  (see Nginx#PHP implementation).

Because of new restrictions on  since version 7.4, where  is set to prevent Matomo to function correctly (unable to installing plugins, changing configuration etc.), the ability to access certain files needs to be set manually.

The file  below fixes the issue while not exposing more than necessary and still allows the user to change ACL as described in the installation manifest if this is not desired.

## Server setup (Nginx)
Create the server by modifying . Add the following template to the  context. Alternatively, take a look at Matomo's instructions on GitHub.

{{bc|1=
include /etc/nginx/mime.types;

server
{
    index index.php;
    listen 443 ssl;
    listen :::443 ssl;
    root /usr/share/webapps/matomo/;
    server_name matomo.example.com;

    location ~ ^/(\.git/config/core/lang/tmp/)
    {
        return 403;
    }

    location ~ \.php$
    {
        try_files $uri =404;

        # FastCGI
        include fastcgi.conf;
        fastcgi_pass unix:/run/php-fpm/php-fpm.sock;
        fastcgi_index index.php;
    }

    location ~ \.(avicsseotgifhtmhtmlicojpgjsjsonmp3mp4oggpngsvgttfwavwoffwoff2)$
    {
        try_files $uri =404;
    }

    location ~ ^/(libs/misc/node_modules/plugins/vendor/)
    {
        return 403;
    }
}
}}

To use encryption, you can get free certificates from letsencrypt. After requesting and installing your certificates, use them by adding the following code to the  or  context.

Run the Nginx server by starting/enabling .

## Final steps
All major settings are done. Call your Matomo website in your browser and complete the small installation guide which is not more than checking that everything needed is available and set up and writing your configuration file.
