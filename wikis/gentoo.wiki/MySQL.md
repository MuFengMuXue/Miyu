This page contains [[changes](https://wiki.gentoo.org/index.php?title=MySQL&oldid=767149&diff=1340595)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/MySQL/de "MySQL (100% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/MySQL/es "MySQL (100% translated)")
-   [français](https://wiki.gentoo.org/wiki/MySQL/fr "MySQL (100% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/MySQL/hu "MySQL (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/MySQL/ru "MySQL (100% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/MySQL/zh-cn "MySQL (100% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/MySQL/ja "MySQL (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/MySQL/ko "MySQL (60% translated)")

**Resources**

[[]][Home](https://www.mysql.com/)

[[]][Official documentation](https://dev.mysql.com/doc/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/MySQL "wikipedia:MySQL")

[[]][Package information](https://packages.gentoo.org/packages/dev-db/mysql)

[[]][GitHub](https://github.com/mysql/mysql-server)

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/mysql)

**MySQL** is a popular, free software relational database management system. It is often used in conjunction with web applications (such as many [PHP](https://wiki.gentoo.org/wiki/PHP "PHP") sites), but has gained many more enterprise-level features since its start in 1994.

An alternative fork and drop-in replacement is [MariaDB](https://wiki.gentoo.org/wiki/MariaDB "MariaDB").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Preliminary configuration]](#Preliminary_configuration)
    -   [[2.3] [In-database configuration]](#In-database_configuration)
    -   [[2.4] [Erasing command history]](#Erasing_command_history)
-   [[3] [Service]](#Service)
    -   [[3.1] [OpenRC]](#OpenRC)
    -   [[3.2] [systemd]](#systemd)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Removing an old database]](#Removing_an_old_database)
-   [[5] [See also]](#See_also)

## [Installation]

### [USE flags]

Before installing [[[dev-db/mysql]](https://packages.gentoo.org/packages/dev-db/mysql)[]], carefully consider the USE flags that influence the package deployment and features. The following table gives an overview of the package\'s supported USE flags:

### [USE flags for] [dev-db/mysql](https://packages.gentoo.org/packages/dev-db/mysql) [[]] [Fast, multi-threaded, multi-user SQL database server]

  --------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+perl`](https://packages.gentoo.org/useflags/+perl)                 Add optional support/bindings for the Perl language
  [`+server`](https://packages.gentoo.org/useflags/+server)             Build the server program
  [`cjk`](https://packages.gentoo.org/useflags/cjk)                     Add CJK support for InnoDB fulltext search using app-text/mecab
  [`cracklib`](https://packages.gentoo.org/useflags/cracklib)           Support for cracklib strong password checking
  [`debug`](https://packages.gentoo.org/useflags/debug)                 Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`jemalloc`](https://packages.gentoo.org/useflags/jemalloc)           Use dev-libs/jemalloc for memory management
  [`latin1`](https://packages.gentoo.org/useflags/latin1)               Use LATIN1 encoding instead of UTF8
  [`numa`](https://packages.gentoo.org/useflags/numa)                   Enable NUMA support using sys-process/numactl (NUMA kernel support is also required)
  [`profiling`](https://packages.gentoo.org/useflags/profiling)         Add support for statement profiling (requires USE=community).
  [`router`](https://packages.gentoo.org/useflags/router)               Build the MySQL router program
  [`selinux`](https://packages.gentoo.org/useflags/selinux)             !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`tcmalloc`](https://packages.gentoo.org/useflags/tcmalloc)           Use the dev-util/google-perftools libraries to replace the malloc() implementation with a possibly faster one
  [`test`](https://packages.gentoo.org/useflags/test)                   Install upstream testsuites for end use.
  [`test-install`](https://packages.gentoo.org/useflags/test-install)   Install testsuite for manual execution by the user
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)       Verify upstream signatures on distfiles
  --------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-03 14:32] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Once the proper USE flags have been set, install MySQL:

`root `[`#`]`emerge --ask dev-db/mysql`

## [Configuration]

### [Files]

Configuration files:

-   [/etc/mysql/my.cnf]
-   [/etc/mysql/mysql.d/50-distro-server.cnf]
-   [/etc/mysql/mysql.d/50-distro-client.cnf]

Command history:

-   [/root/.my.cnf] - Potentially stores the root database user\'s password.
-   [\~/.mysql_history] - Each user\'s SQL history. ***Note:** Unless disabled, history is recorded here. This includes passwords in plain text.*

Data directory:

-   [/var/lib/mysql] - MySQL\'s default data directory. This can be adjusted in the [50-distro-server.cnf] file above. Databases will be stored here.

### [Preliminary configuration]

The [[[dev-db/mysql]](https://packages.gentoo.org/packages/dev-db/mysql)[]] package handles the preliminary setup of MySQL through the `--config` option:

`root `[`#`]`emerge --config dev-db/mysql`

This will initialize the [datadir], create a database, set proper permissions on the database, and assist in creating a good [root] password (this is for the MySQL [root] account, which is not related to the Linux [root] account).

To purge anonymous users and test databases from the installation, run [mysql_secure_installation] after the preliminary setup:

`root `[`#`]`mysql_secure_installation`

### [In-database configuration]

When the database is up and running, connect to it using the [mysql] client application.

`user `[`$`]`mysql -u root -p -h localhost`

    Enter root password:
    Welcome to the MySQL monitor. Commands end with ; or \g.
    Your MySQL connection id is 1 to server version: 5.5.1

    Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

    mysql>

From this point, a session to the MySQL instance is open, allowing for queries and administrative commands to be serviced.

### [Erasing command history]

By default MySQL logs every action, including leaving plain text passwords in its history file.

To remove the history file:

`root `[`#`]`rm /root/.mysql_history`

Alternatively, history logging can be permanently disabled with the following:

`root `[`#`]`ln -sf /dev/null /root/.mysql_history`

## [Service]

### [OpenRC]

To have the database(s) started automatically at boot, add the mysql init script to the default runlevel:

`root `[`#`]`rc-update add mysql default`

Once the database is configured, start the mysql service:

`root `[`#`]`rc-service mysql start`

### [systemd]

To have the database(s) started automatically at boot, enable it:

`root `[`#`]`systemctl enable mysqld.service`

Once the database is configured, start the mysql service:

`root `[`#`]`systemctl start mysqld.service`

## [Removal]

### [Removing an old database]

By default, the [/var/lib/mysql] directory is used as the SQL data directory; once databases have been created, they will be stored here. To remove old databases and start fresh, this directory can be renamed or removed so that a new database can be created.

`root `[`#`]`mv /var/lib/mysql /var/lib/mysql.bak `

`root `[`#`]`mkdir /var/lib/mysql `

`root `[`#`]`chown mysql:mysql /var/lib/mysql `

## [See also]

-   [MySQL/Startup_Guide](https://wiki.gentoo.org/wiki/MySQL/Startup_Guide "MySQL/Startup Guide") --- outlines basic instructions for users on setting up and using MySQL on Linux.
-   [MySQL Migration to version 5.0](https://wiki.gentoo.org/wiki/MySQL/Migrate_to_5.0 "MySQL/Migrate to 5.0")
-   [PostgreSQL](https://wiki.gentoo.org/wiki/PostgreSQL "PostgreSQL") --- a free and open source relational database management system (RDBMS).