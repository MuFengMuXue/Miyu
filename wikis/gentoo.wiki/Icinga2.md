[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Icinga2&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://icinga.com)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Icinga2 "wikipedia:Icinga2")

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Gentoo host]](#Gentoo_host)
        -   [[2.1.1] [IcingaWeb2]](#IcingaWeb2)
        -   [[2.1.2] [Hardware monitoring through lm-sensors]](#Hardware_monitoring_through_lm-sensors)
        -   [[2.1.3] [Graphs through pnp4nagios]](#Graphs_through_pnp4nagios)
        -   [[2.1.4] [Trees and maps with NagVis]](#Trees_and_maps_with_NagVis)
    -   [[2.2] [Gentoo remote]](#Gentoo_remote)

## [Introduction]

Icinga2 is similar to [Icinga](https://wiki.gentoo.org/wiki/Icinga "Icinga") and [Nagios](https://wiki.gentoo.org/wiki/Nagios "Nagios") and was officially released in 2014. It enables monitoring of hosts and services. This includes:

-   A local host running Gentoo Linux, e.g. a server at home
-   A remote host offering Icinga2 services
-   Any remote host offering services like SSH or HTTP, not running any part of Icinga2

** Warning**\
A monitoring tool adds attack surface to the host it runs on. Plan carefully exposed ports, accounts and privileges. Also, backup the configuration including data stored in databases.

** Warning**\
Do not copy passwords from here. Instead, create unique secrets for each installation. Also, reflect upon suggestions from external sources. For example, PostgreSQL\'s pg_hba.conf must not contain md5 as password hashing.

## [Installation]

### [Gentoo host]

The following steps setup Icinga2-monitoring with web interface on a host running Gentoo. The Icinga2-service can then be used to monitor remote hosts, too. But the focus is on monitoring of the Icinga2-enabled host. [PostgreSQL](https://wiki.gentoo.org/wiki/PostgreSQL "PostgreSQL") is the authentication backend and will hold monitoring data, too.

Packages:

-   [[[dev-db/postgresql]](https://packages.gentoo.org/packages/dev-db/postgresql)[]]
-   [[[net-analyzer/icinga2]](https://packages.gentoo.org/packages/net-analyzer/icinga2)[]]
-   [[[net-analyzer/monitoring-plugins]](https://packages.gentoo.org/packages/net-analyzer/monitoring-plugins)[]]
-   [[[www-apps/icingaweb2]](https://packages.gentoo.org/packages/www-apps/icingaweb2)[]]

Optional:

-   [[[sys-apps/lm-sensors]](https://packages.gentoo.org/packages/sys-apps/lm-sensors)[]] for hardware monitoring

What will be monitored out of the box:

-   /proc statistics, load
-   mounted volumes/ disks
-   HTTP-endpoints
-   validity of TLS-certificates

Add apache user to group icingaweb2 so resources can be accessed:

`root `[`#`]`gpasswd -a apache icingaweb2`

PostgreSQL[\[1\]](https://icinga.com/docs/icinga-2/latest/doc/02-installation/#setting-up-the-postgresql-database):

`user `[`$`]`psql -c "CREATE ROLE icinga WITH ENCRYPTED LOGIN PASSWORD 'yourSecret'" `

`user `[`$`]`createdb -O icinga -E UTF8 icinga `

Configure DB-access:

[FILE] **`/etc/icinga2/features-enabled/ido-pgsql.conf`**

    object IdoPgsqlConnection "ido-pgsql"

#### [IcingaWeb2]

PostgreSQL:

    create user icingaweb2 with encrypted password 'icingaweb2';
    create database icingaweb2;
    GRANT ALL PRIVILEGES ON DATABASE icingaweb2 TO icingaweb2;

1.  use [/usr/share/icingaweb2/bin/icingacli]
2.  create token
3.  configure rest through web interface

** Warning**\
Setup TLS to protect the web interface. Especially basic authentication without TLS leaks username and password of icingaadmin in plain text

** Note**\
Without admin module in Icingaweb2 it is necessary to create dashboards in /etc/icingaweb2/dashboards/icingaadmin/dashboard.ini. Afterwards it is possible to add Dashlets from within Icingaweb2 without file editing.

** Note**\
Check the project web page regularly for database upgrades. From time to time scripts are shipped in [/usr/share/icingaweb2/etc/schema/] for MySQL and PostgreSQL.

#### [Hardware monitoring through lm-sensors]

-   broken configuration, see [[[bug #759595]](https://bugs.gentoo.org/show_bug.cgi?id=759595)[]]
-   create local shell script
-   setup CheckCommand manually

** Note**\
Icinga2\'s linked wrapper for sensors is broken. Argument order yields only error output. Also scraping of sensors\' output is broken. See [https://github.com/jackbenny/check_temp/issues/9](https://github.com/jackbenny/check_temp/issues/9) and [https://github.com/jackbenny/check_temp/issues/9](https://github.com/jackbenny/check_temp/issues/9).

#### [Graphs through pnp4nagios]

-   Package: [[[net-analyzer/pnp4nagios]](https://packages.gentoo.org/packages/net-analyzer/pnp4nagios)[]], USE=-nagios icinga
-   Package: [[[www-apps/icingaweb2-module-pnp4nagios]](https://packages.gentoo.org/packages/www-apps/icingaweb2-module-pnp4nagios)[]]
-   module pnp must be enabled in icinga2web
-   [/etc/icinga2/features-enabled] +perfdata.conf (issues with icingacli, must be done as root/ manually)
-   filling perfdata.conf is a bit fragile, default paths after installation don\'t match between icinga2 and npcd ingester

** Note**\
Host- and service-template are missing. So there are no action_url-properties in icingaweb2. Must be added manually to templates.conf.

** Note**\
It is useful to link directly from Icingaweb2 to Graphs. Icinga2/ IcingaWeb2 deprecated action_url-properties. Instead navigation/host-actions.ini is to be used.

** Warning**\
This does not work out of the box, Permissions/ ownership of perdata-directory is wrong. Log file of icingaweb2 complains about missing permissions

[FILE] **`/etc/icingaweb2/navigation/host-actions.ini`**

    [Graphs]
    type = "host-action"
    target = "_blank"
    url = "/pnp4nagios?host=$host_name$"
    owner = "icingaadmin"
    groups = "icinga2admins"

[FILE] **`/etc/icinga2/features-enabled/perdata.conf`**

    /**
     * The PerfdataWriter type writes performance data files and rotates
     * them in a regular interval.
     */
    object PerfdataWriter "perfdata"

Not running out of the box:

-   [https://github.com/lingej/pnp4nagios/issues/148](https://github.com/lingej/pnp4nagios/issues/148)

\

#### [Trees and maps with NagVis]

[NagVis](https://www.nagvis.org/) works with current Icinga and IcingaWeb2 through [icingaweb2-module-nagvis](https://github.com/Icinga/icingaweb2-module-nagvis).

\

-   install NagVis to [/usr/local/nagvis] to keep it out of portage controlled paths
-   copy into icingaweb2-module-nagvis [/usr/share/icingaweb2/modules/] so IcingaWeb2 can pick it up

### [Gentoo remote]

** Note**\
Collecting statistics from a Gentoo remote host