**Resources**

[[]][Home](http://www.phpbb.com/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/phpBB "wikipedia:phpBB")

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Webapps "Project:Webapps")][Project](https://wiki.gentoo.org/wiki/Project:Webapps "Project:Webapps")

**phpBB** is open-source bulletin board software, an internet forum package, that runs on the [PHP](https://wiki.gentoo.org/wiki/PHP "PHP") scripting language.

## Contents

-   [[1] [Install]](#Install)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Enabling Apache PHP support]](#Enabling_Apache_PHP_support)
    -   [[2.2] [Creating a database]](#Creating_a_database)
    -   [[2.3] [Completing the phpBB install]](#Completing_the_phpBB_install)
-   [[3] [See also]](#See_also)

## [Install]

Before installing **phpBB**, it is recommended to peruse the configuration options for [Apache](https://wiki.gentoo.org/wiki/Apache "Apache")/[nginx](https://wiki.gentoo.org/wiki/Nginx "Nginx"), [MariaDB](https://wiki.gentoo.org/wiki/MariaDB "MariaDB")/[MySQL](https://wiki.gentoo.org/wiki/MySQL "MySQL"), and [PHP](https://wiki.gentoo.org/wiki/PHP "PHP") as well.

### [USE flags]

### [USE flags for] [www-apps/phpBB](https://packages.gentoo.org/packages/www-apps/phpBB) [[]] [An open-source PHP-based bulletin board package]

  ------------------------------------------------------------- --------------------------------------------------------------------------------------
  [`ftp`](https://packages.gentoo.org/useflags/ftp)             Add FTP (File Transfer Protocol) support
  [`gd`](https://packages.gentoo.org/useflags/gd)               Add support for media-libs/gd (to generate graphics on the fly)
  [`mssql`](https://packages.gentoo.org/useflags/mssql)         Add support for Microsoft SQL Server database
  [`mysqli`](https://packages.gentoo.org/useflags/mysqli)       Add support for the improved mySQL libraries
  [`postgres`](https://packages.gentoo.org/useflags/postgres)   Add support for the postgresql database
  [`sqlite`](https://packages.gentoo.org/useflags/sqlite)       Add support for sqlite - embedded sql database
  [`vhosts`](https://packages.gentoo.org/useflags/vhosts)       Add support for installing web-based applications into a virtual-hosting environment
  [`zlib`](https://packages.gentoo.org/useflags/zlib)           Add support for zlib compression
  ------------------------------------------------------------- --------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-08-03 21:44] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

When using Apache, it is important to enable PHP support for [[[www-servers/apache]](https://packages.gentoo.org/packages/www-servers/apache)[]] by installing [[[dev-lang/php]](https://packages.gentoo.org/packages/dev-lang/php)[]] with the `apache2` USE-flag.

For nginx, the `fpm` flag should be enabled on [[[dev-lang/php]](https://packages.gentoo.org/packages/dev-lang/php)[]].

With MariaDB/MySQL, [[[dev-lang/php]](https://packages.gentoo.org/packages/dev-lang/php)[]] will need to have been built with the `mysql` and `mysqli` flags enabled.

### [Emerge]

`root `[`#`]`emerge --ask www-apps/phpBB`

## [Configuration]

### [Enabling Apache PHP support]

** Important**\
With \>=[app-eselect/eselect-php-0.8.1](https://packages.gentoo.org/packages/app-eselect/eselect-php), the `APACHE2_OPTS` variable changed to `-D PHP` instead of `-D PHP5`. This allows for future major versions to flow smoothly.

[FILE] **`/etc/conf.d/apache2`Enabling the PHP module**

    APACHE2_OPTS="... -D PHP"

### [Creating a database]

Refer to [MySQL/Startup Guide](https://wiki.gentoo.org/wiki/MySQL/Startup_Guide "MySQL/Startup Guide") for detailed instructions.

`root `[`#`]`/etc/init.d/mysql start`

`user `[`$`]`mysql -u root -p `

    mysql> CREATE DATABASE IF NOT EXISTS <database> DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
    mysql> CREATE USER '<username>'@'localhost' IDENTIFIED BY '';
    mysql> GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER ON <database>.* TO '<username>'@'localhost' IDENTIFIED BY '';
    mysql> quit

### [Completing the phpBB install]

Browsing to the root of the install, [http://localhost/phpBB](http://localhost/phpBB) for example (`https` for SSL installs), should now bring up the phpBB introduction web page with an overview and install tabs, which will work as a guide through the rest of the installation process.

** Important**\
The forum will be accessible to administrators only, until the `install` directory is removed from the root directory of the phpBB install.

## [See also]

-   [MediaWiki](https://wiki.gentoo.org/wiki/MediaWiki "MediaWiki") --- a [PHP](https://wiki.gentoo.org/wiki/PHP "PHP")-powered web application used by the Gentoo wiki and the various Wikimedia Project websites (including Wikipedia).