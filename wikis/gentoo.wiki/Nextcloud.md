**Resources**

[[]][Home](https://nextcloud.com/)

[[]][Official documentation](https://docs.nextcloud.com/server/latest/admin_manual/)

[[]][Package information](https://packages.gentoo.org/packages/www-apps/nextcloud)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Nextcloud "wikipedia:Nextcloud")

[[]][GitHub](https://github.com/nextcloud/server)

[[]][GitLab](https://gitlab.com/nextcloud/server)

[[]][[#nextcloud](ircs://irc.libera.chat/#nextcloud)] ([[webchat](https://web.libera.chat/#nextcloud)])

[[]][Blog](https://nextcloud.com/blog/)

**Nextcloud** is a free and open source cloud hub primarily intended for file synchronization and sharing. It features a rich ecosystem of different [apps](https://apps.nextcloud.com/) .

This installation document was written with Nextcloud 26 as a target and attempts to provide a fast installation on Gentoo systems.^[\[1\]](#cite_note-1)^

** Note**\
This guide is about installing the web server components of Nextcloud. It contains no instructions on installing the (optional) desktop client.

## Contents

-   [[1] [Requirements]](#Requirements)
    -   [[1.1] [PHP]](#PHP)
        -   [[1.1.1] [Caching]](#Caching)
        -   [[1.1.2] [Signed SSL certificate (Let\'s Encrypt)]](#Signed_SSL_certificate_.28Let.27s_Encrypt.29)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [USE flags]](#USE_flags)
    -   [[2.2] [Emerge]](#Emerge)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Files]](#Files)
    -   [[3.2] [Service]](#Service)
        -   [[3.2.1] [Database]](#Database)
            -   [[3.2.1.1] [MySQL and MariaDB]](#MySQL_and_MariaDB)
            -   [[3.2.1.2] [Postgres]](#Postgres)
        -   [[3.2.2] [OpenRC]](#OpenRC)
        -   [[3.2.3] [systemd]](#systemd)
-   [[4] [notify_push support]](#notify_push_support)
    -   [[4.1] [Emerge]](#Emerge_2)
    -   [[4.2] [Service]](#Service_2)
        -   [[4.2.1] [OpenRC]](#OpenRC_2)
        -   [[4.2.2] [systemd]](#systemd_2)
    -   [[4.3] [Reverse proxy]](#Reverse_proxy)
        -   [[4.3.1] [Nginx]](#Nginx)
    -   [[4.4] [Setup]](#Setup)
-   [[5] [References]](#References)

## [Requirements]

Nextcloud requires software components from the standard [(L)AMP stack](https://en.wikipedia.org/wiki/LAMP_(software_bundle) "wikipedia:LAMP (software bundle)"): a web server, a database, and PHP (php-fpm). [Apache](https://docs.nextcloud.com/server/latest/admin_manual/installation/source_installation.html#apache-web-server-configuration) and [Nginx](https://docs.nextcloud.com/server/latest/admin_manual/installation/nginx.html) are supported web servers.

### [PHP]

Before (re-)emerging PHP in order to get supported modules, see upstream\'s list of supported PHP versions and associated modules^[\[2\]](#cite_note-2)^ which are necessary for correct operation of Nextcloud.

** Warning**\
These USE flags for [[[dev-lang/php]](https://packages.gentoo.org/packages/dev-lang/php)[]] are required in order for Nextcloud to function correctly: `ctype curl fileinfo filter gd iconv ssl posix session simplexml xmlreader xmlwriter zip zlib`

** Important**\
Please choose one of PostgreSQL, MySQL/MariaDB or sqlite (only lite installations only) databases to hold Nextcloud\'s data. This tutorial will use PostgreSQL (recommended) as the database, thus adding the `postgres` and `pdo` USE flags. MySQL would use `mysql` while sqlite would employ `sqlite`.

Generally recommended USE flags are `bzip2 gmp bcmath exif intl sysvipc`.

You can emerge PHP with:

`root `[`#`]`emerge --ask dev-lang/php`

Verify one of three possible modules exist for PHP\'s database connector:

`user `[`$`]`php -m | grep -i 'pdo_pgsql'`

    pdo_pgsql

After installing or uninstalling any PHP modules, the web server, and/or php-fpm depending on the configuration, each service will need to be restarted to register the changes.

#### [Caching]

Recommended for enhanced server performance is to pair Nextcloud with [memcached](https://www.memcached.org/) or others. This PHP module is a PHP Extension Community Library (PECL) extension and [is installed separately from PHP itself](https://www.php.net/manual/en/memcached.installation.php):

`root `[`#`]`emerge --ask dev-php/pecl-memcached`

memcached package must also be installed:

`root `[`#`]`emerge --ask net-misc/memcached`

Verify the memcached module is available to PHP:

`user `[`$`]`php -m | grep -i 'mem'`

    memcached

#### [][Signed SSL certificate (Let\'s Encrypt)]

[Let\'s Encrypt](https://wiki.gentoo.org/wiki/Let%27s_Encrypt "Let's Encrypt") can be used to obtain free certificates which have been signed by a recognized signing authority.

`root `[`#`]`certbot --apache --rsa-key-size 4096 --staple-ocsp --hsts`

Simply choose a desired domain and request the certificate.

** Note**\
For nginx, simply use this command instead:

`root `[`#`]`certbot --nginx --rsa-key-size 4096 --staple-ocsp --hsts`

## [Installation]

Once PHP, Apache and (optionally) the caching service have been installed, simply set the USE flags for nextcloud and emerge the service.

### [USE flags]

### [USE flags for] [www-apps/nextcloud](https://packages.gentoo.org/packages/www-apps/nextcloud) [[]] [Personal cloud that runs on your own server]

  --------------------------------------------------------------------- --------------------------------------------------------------------------------------
  [`+curl`](https://packages.gentoo.org/useflags/+curl)                 Add support for client-side URL transfer library
  [`+imagemagick`](https://packages.gentoo.org/useflags/+imagemagick)   Enable optional support for the ImageMagick or GraphicsMagick image converter
  [`+sqlite`](https://packages.gentoo.org/useflags/+sqlite)             Add support for sqlite - embedded sql database
  [`mysql`](https://packages.gentoo.org/useflags/mysql)                 Add mySQL Database support
  [`postgres`](https://packages.gentoo.org/useflags/postgres)           Add support for the postgresql database
  [`vhosts`](https://packages.gentoo.org/useflags/vhosts)               Add support for installing web-based applications into a virtual-hosting environment
  --------------------------------------------------------------------- --------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-03 19:54] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask www-apps/nextcloud`

The following command is a recommendation for webapp-config:

`root `[`#`]`webapp-config -h /nextcloud -d / -I nextcloud 26.0.0`

## [Configuration]

### [Files]

[/var/www/nextcloud/htdocs] - Contains the nextcloud files if the install was performed using the recommended method.

### [Service]

#### [Database]

##### [MySQL and MariaDB]

MySQL or MariaDB databases are the [recommended database engines.](https://docs.nextcloud.com/server/latest/admin_manual/configuration_database/linux_database_configuration.html)

To enable on Gentoo, set the `mysql` USE flag. It is recommended to disable `sqlite` and `postgres` when using a MySQL-based database implementation.

[FILE] **`/etc/portage/package.use/nextcloud`Enable MySQL database support**

    www-apps/nextcloud mysql

Ask Portage to rebuild the world set:

`root `[`#`]`emerge --ask --update --deep --newuse @world`

Run the configuration step to create and set proper permissions on the database directories and assist setting the database root user\'s password (Note - this is for the MariaDB root user account, which is *not* the same as the operating system\'s root user account!):

`root `[`#`]`emerge --ask --config dev-db/mariadb`

Be sure to save the database root user\'s password in a secure enclave for safe keeping!

The MariaDB server can be enabled and started:

`root `[`#`]`systemctl enable --now mariadb.service`

##### [Postgres]

When running a Postgres databases, instantiate before running the service. This will create appropriate runtime directories, etc.

`root `[`#`]`emerge --config dev-db/postgresql:16`

#### [OpenRC]

On an OpenRC system Nextcloud does not have a specific service, but runs on services from the LAMP stack:

`root `[`#`]`rc-update add postgresql-16 default `

`root `[`#`]`rc-update add apache2 default `

#### [systemd]

`root `[`#`]`systemctl enable --now postgresql-16 `

`root `[`#`]`systemctl enable --now apache2 `

## [[notify_push] support]

Normally, clients pull updates from the server periodically. With many clients it can create a significant load on your server. The [Client Push](https://apps.nextcloud.com/apps/notify_push) application can help you to reduce it.

### [Emerge]

Install the daemon:

`root `[`#`]`emerge --ask www-apps/nextcloud-notify_push`

### [Service]

To start the daemon at boot, run the following commands:

#### [OpenRC]

`root `[`#`]`rc-service nextcloud-notify_push start `

`root `[`#`]`rc-update add nextcloud-notify_push default `

#### [systemd]

`root `[`#`]`systemctl start nextcloud-notify_push.service `

`root `[`#`]`systemctl enable nextcloud-notify_push.service `

### [Reverse proxy]

The daemon should listen on the [/push/] location of your Nextcloud installation.

#### [Nginx]

[CODE]

    location ^~ /push/

### [Setup]

To finish the configuration, run:

`user `[`$`]`php occ notify_push:setup https://cloud.example.com/push`

## [References]

1.  [[[↑](#cite_ref-1)] [[https://docs.nextcloud.com/server/latest/admin_manual/installation/source_installation.html#](https://docs.nextcloud.com/server/latest/admin_manual/installation/source_installation.html#)]]
2.  [[[↑](#cite_ref-2)] [[https://docs.nextcloud.com/server/latest/admin_manual/installation/source_installation.html#prerequisites-for-manual-installation](https://docs.nextcloud.com/server/latest/admin_manual/installation/source_installation.html#prerequisites-for-manual-installation)]]