**Resources**

[[]][Home](https://www.joomla.org/)

**Joomla!** is a powerful open source [PHP](https://wiki.gentoo.org/wiki/PHP "PHP")-based content management system.

## Contents

-   [[1] [Preinstallation]](#Preinstallation)
    -   [[1.1] [OpenRC]](#OpenRC)
-   [[2] [Install]](#Install)
    -   [[2.1] [Ebuild install]](#Ebuild_install)
    -   [[2.2] [Backend]](#Backend)
    -   [[2.3] [Frontend]](#Frontend)
        -   [[2.3.1] [MySQL]](#MySQL)
        -   [[2.3.2] [Ftp]](#Ftp)
-   [[3] [Extensions]](#Extensions)
-   [[4] [See also]](#See_also)

## [Preinstallation]

Edit [/etc/portage/make.conf] and append \"apache2 php gd pdo\" to the `USE` variable.

[FILE] **`/etc/portage/make.conf`Portage configuration file**

    USE="apache2 php gd pdo"

Edit [/etc/portage/package.use] and add the following USE flags to the PHP package, then emerge the LAMP stack:

[FILE] **`/etc/portage/package.use`Portage configuration file**

    dev-lang/php mysql mysqli postgres

PHP5 notes:

[[[dev-lang/php]](https://packages.gentoo.org/packages/dev-lang/php)[]] must be built with `pcre` and `session` USE flags.

When rebuilding php5 and changing USE flags, be sure to restart the web server. In this case, Apache.

`root `[`#`]`emerge --ask apache mysql php`

Scroll up into the emerge log and setup the root user for mysql running the command printed.

Edit [/etc/conf.d/apache2] and add `-D PHP5` to the `APACHE2_OPTS` line.

### [OpenRC]

Start up the LAMP stack:

`root `[`#`]`rc-service mysql start`

`root `[`#`]`rc-service apache2 start`

Set the LAMP stack to start upon boot:

`root `[`#`]`rc-update add mysql default`

`root `[`#`]`rc-update add apache2 default`

## [Install]

### [Ebuild install]

It is possible to install Joomla! from Portage, but the last version keep on 1.7.

Now we can get on with emerging:

`root `[`#`]`emerge --ask joomla`

### [Backend]

The ebuilds for Joomla! are very out of date (last ebuild 1.7), for the latest versions proceed manually.

Setup a directory for Joomla! in your web server

`root `[`#`]`mkdir /var/www/localhost/htdocs/joomla`

Pull the latest to your web server:

`root `[`#`]`wget -o /var/www/localhost/htdocs/joomla/joomla.zip https://downloads.joomla.org/cms/joomla3/3-9-2/Joomla_3-9-2-Stable-Full_Package.zip`

Unpack the zip:

`root `[`#`]`unzip joomla.zip`

### [Frontend]

Point a browser @ [http://127.0.0.1/joomla/installation/index.php](http://127.0.0.1/joomla/installation/index.php)

-   Step 1

Name, and describe your site, point at your email and password the admin account. (change the admin account name if you so choose, more secure)

Click next.

-   Step 2

#### [MySQL]

It is a good idea to setup an unprivileged mysql user and database for Joomla!:

`root `[`#`]`mysql -u root -p `

    mysql> CREATE DATABASE IF NOT EXISTS `joomla` DEFAULT CHARACTER SET `utf8` COLLATE `utf8_unicode_ci`;
    mysql> CREATE USER 'joomla'@'localhost' IDENTIFIED BY 'dbpass!!! change me';
    mysql> GRANT LOCK TABLES, SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER ON `joomla`.* TO 'joomla'@'localhost' IDENTIFIED BY 'dbpass!!! change me';
    mysql> \q

In the web page enter joomla for username and joomla for database

Press next

-   Step 3

#### [Ftp]

Select no for now.

-   Step4

Delete the install directory, and go to [http://127.0.0.1/joomla/index.php](http://127.0.0.1/joomla/index.php) to see your website, and [http://127.0.0.1/joomla/administrator/index.php](http://127.0.0.1/joomla/administrator/index.php) to administer your website.

## [Extensions]

Joomla! can be crafted into many things with extensions. It can be used for forums, chat, classified ads, web stores, blogs, guest books, and more.

[Joomla! Extensions Directory](https://extensions.joomla.org/extensions/)

## [See also]

-   [MediaWiki](https://wiki.gentoo.org/wiki/MediaWiki "MediaWiki") --- a [PHP](https://wiki.gentoo.org/wiki/PHP "PHP")-powered web application used by the Gentoo wiki and the various Wikimedia Project websites (including Wikipedia).