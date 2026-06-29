[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=WordPress&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**WordPress** is a blog application content management system.

## Contents

-   [[1] [Preinstall]](#Preinstall)
-   [[2] [Install]](#Install)
    -   [[2.1] [MySQL]](#MySQL)
-   [[3] [5 minute installer]](#5_minute_installer)
-   [[4] [Administration and use]](#Administration_and_use)
    -   [[4.1] [Plugins and themes]](#Plugins_and_themes)

## [Preinstall]

The following applications will need to be installed in order for WordPress to have everything that\'s needed to work properly.

`root `[`#`]`emerge --ask www-servers/apache dev-db/mysql dev-lang/php`

To add PHP support into apache, you must follow the directions in the main [Apache](https://wiki.gentoo.org/wiki/Apache "Apache") article.

## [Install]

### [USE flags for] [www-apps/wordpress](https://packages.gentoo.org/packages/www-apps/wordpress) [[]] [Wordpress PHP and MySQL based content management system (CMS)]

  ------------------------------------------------------------- --------------------------------------------------------------------------------------
  [`+akismet`](https://packages.gentoo.org/useflags/+akismet)   Installs Akismet comment spam plug-in
  [`+themes`](https://packages.gentoo.org/useflags/+themes)     Installs themes (including default theme)
  [`examples`](https://packages.gentoo.org/useflags/examples)   Install examples, usually source code
  [`vhosts`](https://packages.gentoo.org/useflags/vhosts)       Add support for installing web-based applications into a virtual-hosting environment
  ------------------------------------------------------------- --------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-21 08:02] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

First unmask [[[www-apps/wordpress]](https://packages.gentoo.org/packages/www-apps/wordpress)[]]:

`root `[`#`]`echo "www-apps/wordpress" >> /etc/portage/package.accept_keywords`

Then install Wordpress:

`root `[`#`]`emerge --ask wordpress`

Fix permissions to enable uploading content (such as banners):

`root `[`#`]`chown apache:apache /var/www/localhost/htdocs/wordpress/wp-content`

### [MySQL]

First visit the Gentoo wiki on [MySQL](https://wiki.gentoo.org/wiki/MySQL "MySQL") and get it ready.

Then, create a database for WordPress to interact with:

`root `[`#`]`mysql -u root -p `

    mysql> CREATE DATABASE IF NOT EXISTS `wordpress` DEFAULT CHARACTER SET `utf8` COLLATE `utf8_unicode_ci`;
    mysql> CREATE USER 'wordpress'@'localhost' IDENTIFIED BY 'changeme';
    mysql> GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER ON `wordpress`.* TO 'wordpress'@'localhost';
    mysql> \q

Configure WordPress to interact with the database created. Generate goodies for this file with with [Wordpress\' key generator](https://api.wordpress.org/secret-key/1.1/salt/)

`root `[`#`]`nano /var/www/localhost/htdocs/wordpress/wp-config.php`

Database and database user are \"wordpress\" and passwords are what you set in the mysql database generation step. (changeme fields)

## [5 minute installer]

Point a web browser to [http://localhost/wordpress/](http://localhost/wordpress/)

If it complains about not being able to connect to the MySQL database you set in wp-config.php, make sure to change define(\'DB_HOST\', \'localhost\') to define(\'DB_HOST\', \'127.0.0.1\') in the file.

Name the website, and make create default administrator password.

## [Administration and use]

Administer the WordPress installation at [http://localhost/wordpress/wp-admin/](http://localhost/wordpress/wp-admin/)

The shiny new blog is located at [http://localhost/wordpress/](http://localhost/wordpress/)

### [Plugins and themes]

Wordpress is a bit of a permissions nightmare. Themes and plugins will ask for ftp access due to permission problems.

`root `[`#`]`cd /var/www/localhost/htdocs/wordpress`

`root `[`#`]`chown -R apache:apache wp-admin wp-includes wp-content`

In case of using [nginx](https://wiki.gentoo.org/wiki/Nginx "Nginx") as the webserver, first edit:

`root `[`#`]` nano /etc/php/fpm-php*/fpm.d/www.conf`

and set the user and group entries to ***nginx.*** The default values are ***nobody*** which creates problems with the permission. Then set the permission accordingly:

`root `[`#`]`cd /var/www/localhost/htdocs/wordpress`

`root `[`#`]`chown -R nginx:nginx wp-admin wp-includes wp-content`

This clearly is breaking the security of the webapp. To restore security once all is set how you want it.

`root `[`#`]`chown -R root:root /var/www/localhost/htdocs/wordpress`