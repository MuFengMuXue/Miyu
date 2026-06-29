[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Moodle&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](http://www.moodle.org/)

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Moodle "wikipedia:Moodle")

**Moodle** is a LAMP stack content management system for educators.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [System Arrangement]](#System_Arrangement)
    -   [[1.3] [Merge]](#Merge)
    -   [[1.4] [Adjust Settings]](#Adjust_Settings)
    -   [[1.5] [Mysql]](#Mysql)
    -   [[1.6] [Adjust Configs]](#Adjust_Configs)
-   [[2] [Web end]](#Web_end)

## [Installation]

### [USE flags]

### [USE flags for] [www-apps/moodle](https://packages.gentoo.org/packages/www-apps/moodle) [[]] [The Moodle Course Management System]

  ------------------------------------------------------------- --------------------------------------------------------------------------------------
  [`imap`](https://packages.gentoo.org/useflags/imap)           Add support for IMAP (Internet Mail Application Protocol)
  [`ldap`](https://packages.gentoo.org/useflags/ldap)           Add LDAP support (Lightweight Directory Access Protocol)
  [`mssql`](https://packages.gentoo.org/useflags/mssql)         Add support for Microsoft SQL Server database
  [`mysqli`](https://packages.gentoo.org/useflags/mysqli)       Add support for the improved mySQL libraries
  [`odbc`](https://packages.gentoo.org/useflags/odbc)           Add ODBC Support (Open DataBase Connectivity)
  [`postgres`](https://packages.gentoo.org/useflags/postgres)   Add support for the postgresql database
  [`vhosts`](https://packages.gentoo.org/useflags/vhosts)       Add support for installing web-based applications into a virtual-hosting environment
  ------------------------------------------------------------- --------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-22 00:13] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [System Arrangement]

`root `[`#`]

    echo "www-apps/moodle mysqli" >> /etc/portage/package.use
    echo "app-eselect/eselect-php apache2" >> /etc/portage/package.use
    echo "dev-lang/php gd xmlrpc zip mysqli intl curl soap apache2" >> /etc/portage/package.use
    echo "www-apps/moodle" >> /etc/portage/package.accept_keywords

### [Merge]

`root `[`#`]`emerge --ask moodle`

### [Adjust Settings]

Add -D PHP5 in APACHE2_OPTS to /etc/conf.d/apache

`root `[`#`]

    APACHEPHP=$(cat /etc/conf.d/apache2 | grep -c PHP); if [ "$APACHEPHP" = 1 ] ;\
     then echo "done"; else sed -i -e 's/S="/S="-D PHP5 /' /etc/conf.d/apache2; fi

Link moodle to the web root.

`root `[`#`]`ln -s /usr/share/webapps/moodle/2.5.1/htdocs/ /var/www/localhost/htdocs/moodle`

### [Mysql]

Create a database for moodle to interact with.

** Important**\
change the changeme\'s to your own password

`root `[`#`]`mysql -u root -p `

    mysql> SET GLOBAL binlog_format = 'ROW';
    mysql> CREATE DATABASE IF NOT EXISTS `moodle_db` DEFAULT CHARACTER SET `utf8` COLLATE `utf8_unicode_ci`;
    mysql> CREATE USER 'moodle_user'@'localhost' IDENTIFIED BY 'changeme';
    mysql> GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER ON `moodle_db`.* TO 'moodle_user'@'localhost' IDENTIFIED BY 'changeme';
    mysql> \q

### [Adjust Configs]

`root `[`#`]`nano /var/www/localhost/htdocs/moodle/config.php`

Adjust \$CFG-\>dbpass to your password. If you intend on using this program with a domain name, insert domain name now.

\

## [Web end]

Point your browser at [http://localhost/moodle](http://localhost/moodle)

-   continue
-   continue
-   continue (probably bottom left under spell checker module install)
-   fill out & update profile
-   name your site, save changes