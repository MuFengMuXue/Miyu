**Resources**

[[]][Home](https://piwik.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/piwik "wikipedia:piwik")

[[]][GitHub](https://github.com/piwik/piwik)

[[]][[#piwik](ircs://irc.libera.chat/#piwik)] ([[webchat](https://web.libera.chat/#piwik)])

This article describes the installation and configuration of Piwik Web Analytics software.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [php.ini]](#php.ini)
    -   [[2.2] [Services]](#Services)
        -   [[2.2.1] [OpenRC]](#OpenRC)
    -   [[2.3] [Piwik software]](#Piwik_software)
    -   [[2.4] [Database]](#Database)
        -   [[2.4.1] [MySQL]](#MySQL)
-   [[3] [See also]](#See_also)

## [Installation]

### [USE flags]

Piwik uses the `gd`, `mysqli`, `pdo`, and `truetype` USE flags on [[[dev-lang/php]](https://packages.gentoo.org/packages/dev-lang/php)[]]. Be sure they are enabled by editing [/etc/portage/package.use]:

[FILE] **`/etc/portage/package.use/php`**

    dev-lang/php fpm -exif mysqli pdo gd truetype
    # required by dev-lang/php-5.6.10::gentoo
    # required by dev-lang/php (argument)
    >=app-eselect/eselect-php-0.7.1-r4 fpm

### [Emerge]

`root `[`#`]`emerge --ask --verbose dev-lang/php`

In order to see geographical IP addresses, the geoip PHP extention is required:

`root `[`#`]`emerge --ask dev-php/pecl-geoip`

## [Configuration]

### [php.ini]

Piwik requires the following change in [php.ini]:

[FILE] **`/etc/php/fpm-php5.6/php.ini`FPM PHP 5.6 configuration file**

    always_populate_raw_post_data = -1

### [Services]

#### [OpenRC]

Restart the web server and php services. In the example below the Nginx server is used:

`root `[`#`]`/etc/init.d/php-fpm restart `

`root `[`#`]`/etc/init.d/nginx restart `

### [Piwik software]

Change to web server public directory:

`root `[`#`]`cd /var/www/localhost/htdocs`

Download and extract piwik analytics:

`root `[`#`]`wget `[`https://builds.piwik.org/piwik.zip`](https://builds.piwik.org/piwik.zip)` `

`root `[`#`]`unzip piwik.zip `

### [Database]

#### [MySQL]

Create a database and user for Piwik (using mysql example):

`user `[`$`]`mysql -u root -p`

    mysql> CREATE DATABASE piwik;
    mysql> USE piwik;
    mysql> grant all privileges on piwik.* to user@localhost identified by 'password';
    mysql> grant all privileges on piwik.* to user@'%' identified by 'password';

Create directories and change write permissions required by Piwik:

`root `[`#`]`mkdir /var/www/localhost/piwikconfig`

`root `[`#`]`chmod a+w /var/www/localhost/htdocs/piwikconfig`

`root `[`#`]`chmod a+w /var/www/localhost/htdocs/piwik/tmp`

`root `[`#`]`chmod a+w /var/www/localhost/htdocs/piwik/config`

In a browser navigate to piwik and follow the configuration instructions.

[http://localhost/piwik](http://localhost/piwik)

Change back the write permission on directories except on [/var/www/localhost/htdocs/piwik/tmp]:

`root `[`#`]`chmod a-w /var/www/localhost/htdocs/piwikconfig`

`root `[`#`]`chmod a-w /var/www/localhost/htdocs/piwik/config`

## [See also]

-   [Apache](https://wiki.gentoo.org/wiki/Apache "Apache") - The most popular HTTP server used the Internet.
-   [Nginx](https://wiki.gentoo.org/wiki/Nginx "Nginx") - A robust, small, high performance web server and reverse proxy server.
-   [Lighttpd](https://wiki.gentoo.org/wiki/Lighttpd "Lighttpd") - A fast, lightweight web server.