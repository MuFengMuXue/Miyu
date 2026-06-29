This page contains [[changes](https://wiki.gentoo.org/index.php?title=MediaWiki&diff=1322001)] which are not marked for translation.

\

**Resources**

[[]][Home](https://www.mediawiki.org)

[[]][Official documentation](https://www.mediawiki.org/wiki/Manual:What_is_MediaWiki%3F)

[[]][Package information](https://packages.gentoo.org/packages/www-apps/mediawiki)

[[]][Wikipedia](https://en.wikipedia.org/wiki/MediaWiki "wikipedia:MediaWiki")

[[]][Bugs (upstream)](https://phabricator.wikimedia.org/)

[[]][[#mediawiki](ircs://irc.libera.chat/#mediawiki)] ([[webchat](https://web.libera.chat/#mediawiki)])

**MediaWiki** is a [PHP](https://wiki.gentoo.org/wiki/PHP "PHP")-powered web application used by the Gentoo wiki and the various Wikimedia Project websites (including Wikipedia).

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Prerequisites]](#Prerequisites)
    -   [[1.2] [www-apps/mediawiki]](#www-apps.2Fmediawiki)
-   [[2] [Setup]](#Setup)
-   [[3] [Advanced configuration]](#Advanced_configuration)
-   [[4] [External resources]](#External_resources)

## [Installation]

### [Prerequisites]

-   Install [PHP](https://wiki.gentoo.org/wiki/PHP "PHP"). Enable the *xmlreader* USE flag, because MediaWiki requires it:

`root `[`#`]`echo "dev-lang/php xmlreader" >> /etc/portage/package.use`

-   Install a web server and set it up for use of PHP:
    -   [Apache](https://wiki.gentoo.org/wiki/Apache "Apache") --- an efficient, extensible [web server](https://wiki.gentoo.org/wiki/Category:Web_servers "Category:Web servers"). It is one of the most popular web servers used the Internet.
    -   [Lighttpd](https://wiki.gentoo.org/wiki/Lighttpd "Lighttpd") --- a fast and lightweight [web server](https://wiki.gentoo.org/wiki/Category:Web_servers "Category:Web servers").
    -   [Nginx](https://wiki.gentoo.org/wiki/Nginx "Nginx") --- a robust, small, high performance [web server](https://wiki.gentoo.org/wiki/Category:Web_servers "Category:Web servers") and reverse proxy server.

<!-- -->

-   Install [MySQL](https://wiki.gentoo.org/wiki/MySQL "MySQL") ([MariaDB](https://wiki.gentoo.org/wiki/MariaDB "MariaDB") is a suitable alternative and the default virtual/mysql provider on Gentoo). Create a database for MediaWiki:

`root `[`#`]`mysql -u root -p `

    mysql> CREATE DATABASE IF NOT EXISTS `mediawiki` DEFAULT CHARACTER SET `utf8` COLLATE `utf8_unicode_ci`;
    mysql> CREATE USER 'mediawiki'@'localhost' IDENTIFIED BY 'password';
    mysql> GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER ON `mediawiki`.* TO 'mediawiki'@'localhost' IDENTIFIED BY 'password';
    mysql> FLUSH PRIVILEGES;
    mysql> \q

-   If the database (MariaDB or MySQL) server is on a different server than MediaWiki, set these USE flags:

[FILE] **`/etc/portage/package.use`**

    www-apps/mediawiki mysql
    dev-db/mariadb -backup -pam -perl -server
    virtual/mysql -server

### [][www-apps/mediawiki]

### [USE flags for] [www-apps/mediawiki](https://packages.gentoo.org/packages/www-apps/mediawiki) [[]] [The MediaWiki wiki web application (as used on wikipedia.org)]

  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`+sqlite`](https://packages.gentoo.org/useflags/+sqlite)           Add support for sqlite - embedded sql database
  [`imagemagick`](https://packages.gentoo.org/useflags/imagemagick)   Enable optional support for the ImageMagick or GraphicsMagick image converter
  [`mysql`](https://packages.gentoo.org/useflags/mysql)               Add mySQL Database support
  [`postgres`](https://packages.gentoo.org/useflags/postgres)         Add support for the postgresql database
  [`selinux`](https://packages.gentoo.org/useflags/selinux)           !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`vhosts`](https://packages.gentoo.org/useflags/vhosts)             Add support for installing web-based applications into a virtual-hosting environment
  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-25 01:32] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

Install [[[www-apps/mediawiki]](https://packages.gentoo.org/packages/www-apps/mediawiki)[]]:

`root `[`#`]`emerge --ask www-apps/mediawiki`

## [Setup]

-   Copy mediawiki files from /usr/share/webapps/mediawiki//htdocs to /var/www/localhost/htdocs/mediawiki
-   Point a browser at [http://127.0.0.1/mediawiki](http://127.0.0.1/mediawiki) and follow the instructions.
    -   If there is no GUI on the computer running mediawiki, then log in from another machine using http://\<server\>/mediawiki instead, where \<server\> is the name or IP address of the server (see [/etc/hosts](https://wiki.gentoo.org/wiki/Handbook:Parts/Installation/System/en#The_hosts_file "Handbook:Parts/Installation/System/en")).
-   Page \"Welcome to MediaWiki!\":
    -   \"Database name\" is \"mediawiki\"
    -   \"Database username\" is \"mediawiki\"
    -   \"Database password\" is \"changeme\" (or what else is setup)
-   Page \"Connect to database\":
    -   Database character set\" should be \"UTF-8\"
-   Page \"Name\"
    -   \"Name of wiki\" has to be set
    -   Setup admin user and password
-   Page \"Complete!\"
    -   Download the [LocalSettings.php] configuration and move it to [/var/www/localhost/htdocs/mediawiki/LocalSettings.php].
-   Point a browser at [http://127.0.0.1/mediawiki/](http://127.0.0.1/mediawiki/) (or the address used above) to see the newly installed and configured wiki.

## [Advanced configuration]

-   To use a [shorter URL](https://www.mediawiki.org/wiki/Manual:Short_URL/Apache) make the following modifications:

add this somewhere (does not matter exactly where):

[FILE] **`/var/www/localhost/htdocs/mediawiki/LocalSettings.php`**

    $wgArticlePath = "/wiki/$1";
    $wgUsePathInfo = true;

and add this between \<Directory\> tags:

[FILE] **`/etc/apache2/vhosts.d/default_vhost.include`**

    RewriteEngine On
    RewriteRule ^/?wiki(/.*)?$ %/mediawiki/index.php [L]

-   By default the landing page in MediaWiki is unlocked for anyone to edit. Login as admin. By the top right of the page is an arrow that points down, click it and the 3rd option down is \"protect\" to lock down the page.

<!-- -->

-   Set an avatar for the wiki. Add to the bottom of [/var/www/localhost/htdocs/mediawiki/LocalSettings.php]:

[FILE] **`/var/www/localhost/htdocs/mediawiki/LocalSettings.php`**

    $wgLogo = "/mediawiki/wiki.png";

## [External resources]

-   [MediaWiki manual for developers and administrators](https://www.mediawiki.org/wiki/Manual)
-   [spam combat manual](https://www.mediawiki.org/wiki/Manual:Combating_spam)
-   [MediaWiki Extensions](https://www.mediawiki.org/wiki/Extensions)