**Resources**

[[]][Home](http://www.mariadb.org)

[[]][Official documentation](https://mariadb.com/kb/en/library/documentation/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/MariaDB "wikipedia:MariaDB")

[[]][[#maria](ircs://irc.libera.chat/#maria)] ([[webchat](https://web.libera.chat/#maria)])

**MariaDB** is an enhanced, drop-in [MySQL](https://wiki.gentoo.org/wiki/MySQL "MySQL") replacement.

In Gentoo, [[[dev-db/mariadb]](https://packages.gentoo.org/packages/dev-db/mariadb)[]] is the default package for items that depend on [[[virtual/mysql]](https://packages.gentoo.org/packages/virtual/mysql)[]].

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Preliminary configuration]](#Preliminary_configuration)
        -   [[1.3.1] [Preliminary configuration troubleshooting]](#Preliminary_configuration_troubleshooting)
    -   [[1.4] [Service]](#Service)
        -   [[1.4.1] [OpenRC]](#OpenRC)
        -   [[1.4.2] [systemd]](#systemd)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [In-database configuration]](#In-database_configuration)
    -   [[2.2] [Custom options]](#Custom_options)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Compiling against libmariadb.so]](#Compiling_against_libmariadb.so)
        -   [[3.1.1] [MYSQL_SERVER_VERSION]](#MYSQL_SERVER_VERSION)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [dev-db/mariadb](https://packages.gentoo.org/packages/dev-db/mariadb) [[]] [An enhanced, drop-in replacement for MySQL]

  --------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+backup`](https://packages.gentoo.org/useflags/+backup)                   Build mariadb-backup which supports SST and hot backup of InnoDB, Aria and MyISAM including compression and encryption
  [`+perl`](https://packages.gentoo.org/useflags/+perl)                       Add optional support/bindings for the Perl language
  [`+server`](https://packages.gentoo.org/useflags/+server)                   Build the server program
  [`aws-km`](https://packages.gentoo.org/useflags/aws-km)                     Add support for using the AWS Key Management plugin
  [`bindist`](https://packages.gentoo.org/useflags/bindist)                   Flag to enable or disable options for prebuilt (GRP) packages (eg. due to licensing issues)
  [`columnstore`](https://packages.gentoo.org/useflags/columnstore)           Build the ColumnStore storage engine
  [`cracklib`](https://packages.gentoo.org/useflags/cracklib)                 Support for cracklib strong password checking
  [`debug`](https://packages.gentoo.org/useflags/debug)                       Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`extraengine`](https://packages.gentoo.org/useflags/extraengine)           Add support for alternative storage engines (Archive, CSV, Blackhole, Federated(X), Partition)
  [`galera`](https://packages.gentoo.org/useflags/galera)                     Enables galera replication
  [`innodb-lz4`](https://packages.gentoo.org/useflags/innodb-lz4)             Enables lz4 compression methods for InnoDB/XtraDB
  [`innodb-lzo`](https://packages.gentoo.org/useflags/innodb-lzo)             Enables lzo compression methods for InnoDB/XtraDB
  [`innodb-snappy`](https://packages.gentoo.org/useflags/innodb-snappy)       Enables snappy compression methods for InnoDB/XtraDB using app-arch/snappy
  [`jdbc`](https://packages.gentoo.org/useflags/jdbc)                         Enable the CONNECT engine to access foreign databases via JDBC
  [`jemalloc`](https://packages.gentoo.org/useflags/jemalloc)                 Use dev-libs/jemalloc for memory management
  [`kerberos`](https://packages.gentoo.org/useflags/kerberos)                 Add kerberos support
  [`latin1`](https://packages.gentoo.org/useflags/latin1)                     Use LATIN1 encoding instead of UTF8
  [`mroonga`](https://packages.gentoo.org/useflags/mroonga)                   Add support for the Mroonga engine for interfacing with the Groonga text search
  [`numa`](https://packages.gentoo.org/useflags/numa)                         Enable NUMA support using sys-process/numactl (NUMA kernel support is also required)
  [`odbc`](https://packages.gentoo.org/useflags/odbc)                         Add ODBC Support (Open DataBase Connectivity)
  [`oqgraph`](https://packages.gentoo.org/useflags/oqgraph)                   Add support for the Open Query GRAPH engine
  [`pam`](https://packages.gentoo.org/useflags/pam)                           Enable the optional PAM authentication plugin for the server
  [`profiling`](https://packages.gentoo.org/useflags/profiling)               Add support for statement profiling (requires USE=community).
  [`rocksdb`](https://packages.gentoo.org/useflags/rocksdb)                   Add support for RocksDB; a key/value, LSM database optimized for flash storage
  [`s3`](https://packages.gentoo.org/useflags/s3)                             Build the S3 storage engine
  [`selinux`](https://packages.gentoo.org/useflags/selinux)                   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`sphinx`](https://packages.gentoo.org/useflags/sphinx)                     Add suport for the sphinx full-text search engine
  [`sst-mariabackup`](https://packages.gentoo.org/useflags/sst-mariabackup)   Add tools needed to support the mariabackup SST method
  [`sst-rsync`](https://packages.gentoo.org/useflags/sst-rsync)               Add tools needed to support the rsync SST method
  [`static`](https://packages.gentoo.org/useflags/static)                     !!do not set this during bootstrap!! Causes binaries to be statically linked instead of dynamically
  [`systemd`](https://packages.gentoo.org/useflags/systemd)                   Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`systemtap`](https://packages.gentoo.org/useflags/systemtap)               Build support for profiling and tracing using dev-debug/systemtap
  [`tcmalloc`](https://packages.gentoo.org/useflags/tcmalloc)                 Use the dev-util/google-perftools libraries to replace the malloc() implementation with a possibly faster one
  [`test`](https://packages.gentoo.org/useflags/test)                         Install upstream testsuites for end use.
  [`xml`](https://packages.gentoo.org/useflags/xml)                           Add support for XML files
  [`yassl`](https://packages.gentoo.org/useflags/yassl)                       Enable SSL connections and crypto functions using the bundled yaSSL
  --------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-07 19:06] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[dev-db/mariadb]](https://packages.gentoo.org/packages/dev-db/mariadb)[]]:

`root `[`#`]`emerge --ask dev-db/mariadb`

### [Preliminary configuration]

Gentoo MariaDB package maintainers provide setup assistance for MariaDB through the configuration option in the ebuild. Before starting the service, pass the `--config` option to create the database directories, set proper permissions, and assist in creating an setting a secure root password (Note - this is for the MariaDB root user account, which is not the same as the operating system\'s root user account!):

`root `[`#`]`emerge --config dev-db/mariadb`

Be sure to save the database root user\'s password in a secure enclave for safe keeping!

#### [Preliminary configuration troubleshooting]

** Note**\
When configuring MariaDB on a system with `localhost` as its hostname, the *\"Your machine must NOT be named localhost\"* error is produced. The following steps will allow configuration by changing the hostname.

In the event MariaDB configuration fails due to `localhost` as hostname, update the system hostname variable to a name other than `localhost` in [/etc/conf.d/hostname]:

`root `[`#`]`sed -i 's/localhost/larry/g' /etc/conf.d/hostname`

Restart the hostname service:

`root `[`#`]`rc-service hostname restart`

Then, run the configuration command:

`root `[`#`]`emerge --config dev-db/mariadb`

### [Service]

#### [OpenRC]

To have MariaDB start automatically at boot, add it to the default runlevel:

`root `[`#`]`rc-update add mysql default`

If MariaDB is ready to start, then start the service:

`root `[`#`]`rc-service mysql start`

#### [systemd]

For MariaDB versions less than 10.1:

`root `[`#`]`systemctl enable --now mysqld.service`

For MariaDB versions greater than or equal to 10.1.8:

`root `[`#`]`systemctl enable --now mariadb.service`

** Note**\
MariaDB 10.1.8 includes a unit named [mariadb.service] that uses notify instead of a script to check if the system is alive.

## [Configuration]

### [In-database configuration]

When the database is set up and running, connect to MariaDB using the [mysql] client application.

`user `[`$`]`mysql -u root -p -h localhost`

    Enter root password:
    Welcome to the MariaDB monitor.  Commands end with ; or \g.
    Your MariaDB connection id is 86415
    Server version: 5.5.32-MariaDB-log Source distribution

    Copyright (c) 2000, 2013, Oracle, Monty Program Ab and others.

    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

    MariaDB [(none)]>

### [Custom options]

Beginning with MariaDB 10.2, the configuration file [my.cnf], includes a single directive to include [/etc/mysql/mariadb.d] and all files located within. Gentoo includes a file for server settings and one for client settings. Create your own files in this directory and they will be added together in alphabetical order. The base configuration accepts almost all the defaults and only tweaks paths. Tune your server to your liking.

## [Troubleshooting]

### [Compiling against libmariadb.so]

Beginning with MariaDB 10.2, a new LGPL client library is included.

With MariaDB 10.2.8, the server and client headers were separated. This causes compilation errors in some programs which previously relied on server features.

#### [MYSQL_SERVER_VERSION]

One example is `MYSQL_SERVER_VERSION`. A quick fix can be:

    #if defined MARIADB_CLIENT_VERSION_STR && !defined MYSQL_SERVER_VERSION
      #define MYSQL_SERVER_VERSION MARIADB_CLIENT_VERSION_STR
    #endif

Ultimately, `MYSQL_SERVER_VERSION` should be removed and the `MYSQL_VERSION_ID` integer be used in it\'s place for version identification.

## [See also]

-   [MySQL/Startup_Guide](https://wiki.gentoo.org/wiki/MySQL/Startup_Guide "MySQL/Startup Guide") --- outlines basic instructions for users on setting up and using MySQL on Linux.
-   [PostgreSQL](https://wiki.gentoo.org/wiki/PostgreSQL "PostgreSQL") --- a free and open source relational database management system (RDBMS).

## [External resources]

-   [MariaDB VS MySQL features](https://mariadb.com/kb/en/mariadb-vs-mysql-features/)
-   [MariaDB VS MySQL compatibility](https://mariadb.com/kb/en/mariadb-vs-mysql-compatibility/)
-   [Moving from MySQL](https://mariadb.com/kb/en/moving-from-mysql/)