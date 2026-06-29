This page contains [[changes](https://wiki.gentoo.org/index.php?title=Rsyslog&oldid=1396905&diff=1421090)] which are not marked for translation.

**Resources**

[[]][Home](http://www.rsyslog.com)

[[]][Official documentation](http://www.rsyslog.com/doc/master/index.html)

[[]][Package information](https://packages.gentoo.org/packages/app-admin/rsyslog)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Rsyslog "wikipedia:Rsyslog")

[[]][GitHub](https://github.com/rsyslog/rsyslog)

[[]][[#rsyslog](ircs://irc.libera.chat/#rsyslog)] ([[webchat](https://web.libera.chat/#rsyslog)])

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/rsyslog)

[[]]This article has some todo items:\

-   add simple IPv6 example
-   wikify
-   add systemd

**Rsyslog** is an open source system for high performance log processing. More than a regular system logger, it is a versatile tool that can take input from many sources and output to many destinations.

Rsyslog supports forwarding log messages over an IP network, to databases, email, etc. and extends the basic syslog protocol with powerful filtering capabilities. It provides powerful configuration options to adapt to specific needs.

As of July 2025, the company which controls and drives rsyslog development has [declared](https://www.rsyslog.com/rsyslog-goes-ai-first-a-new-chapter-begins/) that it is going \"AI first\". It is unclear what this means for the future of rsyslog.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Environment Variables]](#Environment_Variables)
    -   [[2.2] [Files]](#Files)
        -   [[2.2.1] [Configuration File]](#Configuration_File)
    -   [[2.3] [Severity]](#Severity)
    -   [[2.4] [Facility]](#Facility)
    -   [[2.5] [Filtering]](#Filtering)
    -   [[2.6] [Local logging]](#Local_logging)
    -   [[2.7] [Remote logging]](#Remote_logging)
        -   [[2.7.1] [Client]](#Client)
        -   [[2.7.2] [Server]](#Server)
    -   [[2.8] [Database logging]](#Database_logging)
    -   [[2.9] [Services]](#Services)
        -   [[2.9.1] [OpenRC]](#OpenRC)
-   [[3] [Templates]](#Templates)
-   [[4] [Usage]](#Usage)
    -   [[4.1] [Invocation]](#Invocation)
    -   [[4.2] [Validate Configuration Files]](#Validate_Configuration_Files)
-   [[5] [Removal]](#Removal)
-   [[6] [Troubleshooting]](#Troubleshooting)
-   [[7] [See also]](#See_also)
-   [[8] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [app-admin/rsyslog](https://packages.gentoo.org/packages/app-admin/rsyslog) [[]] [An enhanced multi-threaded syslogd with database support and more]

  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+gcrypt`](https://packages.gentoo.org/useflags/+gcrypt)               Add support for encrypted log files using dev-libs/libgcrypt
  [`+openssl`](https://packages.gentoo.org/useflags/+openssl)             Build the OpenSSL network stream driver (requires dev-libs/openssl)
  [`+ssl`](https://packages.gentoo.org/useflags/+ssl)                     Add support for encrypted client/server communication (requires net-libs/gnutls)
  [`+uuid`](https://packages.gentoo.org/useflags/+uuid)                   Include UUIDs in messages (requires sys-apps/util-linux)
  [`clickhouse`](https://packages.gentoo.org/useflags/clickhouse)         Build the ClickHouse output module (requires net-misc/curl)
  [`curl`](https://packages.gentoo.org/useflags/curl)                     Enable http_request() function in RainerScript (requires net-misc/curl)
  [`dbi`](https://packages.gentoo.org/useflags/dbi)                       Build the general database output module (requires dev-db/libdbi)
  [`debug`](https://packages.gentoo.org/useflags/debug)                   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`doc`](https://packages.gentoo.org/useflags/doc)                       Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`elasticsearch`](https://packages.gentoo.org/useflags/elasticsearch)   Build the Elasticsearch output module (requires net-misc/curl)
  [`gnutls`](https://packages.gentoo.org/useflags/gnutls)                 Build the GnuTLS network stream driver (requires net-libs/gnutls)
  [`imdocker`](https://packages.gentoo.org/useflags/imdocker)             Build the docker input module (requires net-misc/curl)
  [`imhttp`](https://packages.gentoo.org/useflags/imhttp)                 Build the http input module (requires www-servers/civetweb)
  [`impcap`](https://packages.gentoo.org/useflags/impcap)                 Build the pcap input module (requires net-libs/libpcap)
  [`kafka`](https://packages.gentoo.org/useflags/kafka)                   Build the Apache Kafka input/output module (requires dev-libs/librdkafka)
  [`kerberos`](https://packages.gentoo.org/useflags/kerberos)             Build the GSSAPI input and output module (requires virtual/krb5)
  [`kubernetes`](https://packages.gentoo.org/useflags/kubernetes)         Build the kubernetes modify plugin (requires net-misc/curl)
  [`mdblookup`](https://packages.gentoo.org/useflags/mdblookup)           Build the MaxMind DB lookup message modify plugin using dev-libs/libmaxminddb
  [`mongodb`](https://packages.gentoo.org/useflags/mongodb)               Build the MongoDB output module (requires dev-libs/mongo-c-driver)
  [`mysql`](https://packages.gentoo.org/useflags/mysql)                   Build the MySQL database output module (requires virtual/mysql)
  [`normalize`](https://packages.gentoo.org/useflags/normalize)           Build the normalize modify module (requires dev-libs/libee and dev-libs/liblognorm)
  [`omhttp`](https://packages.gentoo.org/useflags/omhttp)                 Build the http output module (requires net-misc/curl)
  [`omhttpfs`](https://packages.gentoo.org/useflags/omhttpfs)             Build the httpfs output module (requires net-misc/curl)
  [`omudpspoof`](https://packages.gentoo.org/useflags/omudpspoof)         Build the udpspoof output module (requires net-libs/libnet)
  [`postgres`](https://packages.gentoo.org/useflags/postgres)             Build the PostgreSQL database output module (requires dev-db/postgresql)
  [`rabbitmq`](https://packages.gentoo.org/useflags/rabbitmq)             Build the RabbitMQ output module (requires net-libs/rabbitmq-c)
  [`redis`](https://packages.gentoo.org/useflags/redis)                   Build the Redis output module using (requires dev-libs/hiredis)
  [`relp`](https://packages.gentoo.org/useflags/relp)                     Build the Reliable Event Logging Protocol (RELP) output module (requires dev-libs/librelp)
  [`rfc3195`](https://packages.gentoo.org/useflags/rfc3195)               Build the rfc3195 input module (requires dev-libs/liblogging)
  [`rfc5424hmac`](https://packages.gentoo.org/useflags/rfc5424hmac)       Build the rfc5424hmac modify module (requires dev-libs/openssl)
  [`snmp`](https://packages.gentoo.org/useflags/snmp)                     Build the snmp modify and output module (requires net-analyzer/net-snmp)
  [`systemd`](https://packages.gentoo.org/useflags/systemd)               Build the journal input and output module (requires sys-apps/systemd)
  [`test`](https://packages.gentoo.org/useflags/test)                     Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`usertools`](https://packages.gentoo.org/useflags/usertools)           Installs the user tools (rsgtutil, rscryutil\...) corresponding to the set USE flags
  [`xxhash`](https://packages.gentoo.org/useflags/xxhash)                 Enable xxHash support in fmhash module (requires dev-libs/xxhash)
  [`zeromq`](https://packages.gentoo.org/useflags/zeromq)                 Build the ZeroMQ input and output modules (requires net-libs/czmq)
  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-15 16:34] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[app-admin/rsyslog]](https://packages.gentoo.org/packages/app-admin/rsyslog)[]]:

`root `[`#`]`emerge --ask app-admin/rsyslog`

** Warning**\
It is a bad idea to run more than one system logger on a physical host. Other local loggers should be removed or disabled.

## [Configuration]

### [Environment Variables]

A list of all environment variables that are read and checked by the [rsyslogd] command:

\

-   `RSYSLOG_DEBUG` - CSV-options are `debug`, `debugondemand`, `lologtimestamp`, `nostdout`, `outputtidtostderr`. Use `RSYSLOG_DEBUG=help` for more options.
-   `RSYSLOG_MODDIR` - full directory path to modules used (defaults to [/usr/lib/\<GNU-trigraph\>/rsyslog])
-   `RSYSLOG_DEBUGLOG` - full file specification to debug log file (no default)
-   `RSYSLOG_DEBUG_TIMEOUTS_TO_STDERR` - Timeout interval for debug output (in seconds).
-   `RSYSLOG_DFLT_LOG_INTERNAL` - Used by testbench and certain startup sequences. \`1\` is equivalent to `$processInternalMessage=on`
-   `LISTEN_PID` - full file specification to the process ID (`PID`) file

[/etc/rsyslog.conf] may contain [environment] parameter keyword(s) that creates an additional environment variable.

Modules may also use other environment variables to modify its processing characteristics. See source code of specific modules for any `getenv()` system calls.

### [Files]

Files that are read by [rsyslogd] command:

-   [/etc/rsyslog.conf] - [rsyslogd] configuration file
-   [/usr/lib/x86_64-linux-gnu/rsyslog/] - module library for [rsyslogd]
-   [/proc/self/ns/net]
-   [/var/run/netns/%s]
-   [/dev/urandom] - kernel random number source device

Files that are written by [rsyslogd] command:

-   (various log files)
-   [/dev/console]
-   [/run/rsyslog.pid%s]

#### [Configuration File]

There are three formats of [/etc/rsyslog.conf]: advanced, basic, legacy(obsoleted).

  ------------------------ ---------------- -------------
  Format type              Versions used    Description
  **advanced**             7.0 to 8.2338+
  **basic**                5.0 to 6.9999
  **legacy (obsoleted)**   before 4.999
  ------------------------ ---------------- -------------

This wiki page only covers both **basic** and **advanced**.

Basic rsyslog configuration:

[FILE] **`/etc/rsyslog.conf`**

    $IncludeConfig /etc/rsyslog.d/
    $FileCreateMode 0640

    *.info;mail.none;authpriv.none;cron.none                -/var/log/messages
    authpriv.*                                              /var/log/secure
    mail.*                                                  -/var/log/maillog
    cron.*                                                  -/var/log/cron
    *.emerg                                                 .*

Typically messages are logged to files, the file has to be specified with full pathname. Rsyslog uses a simple syntax to filter incoming messages. Syslog messages are classified by facility and severity. According to [RFC5424](http://www.ietf.org/rfc/rfc5424.txt) following severity groups have been defined:

### [Severity]

  ---------------- ---------- ----------------------------------
  Numerical Code   Severity   Description
  0                emerg      system is unusable
  1                alert      action must be taken immediately
  2                crit       critical conditions
  3                error      error conditions
  4                warning    warning conditions
  5                notice     normal but significant condition
  6                info       informational messages
  7                debug      debug-level messages
  ---------------- ---------- ----------------------------------

### [Facility]

List of facilities used by rsyslog. Most facilities names are self explanatory. Facilities local0 - local7 common usage is f.e. as network logs facilities for nodes and network equipment. Generally it depends on the situation how to classify logs and put them to facilities. See facilities more as a tool rather than a directive to follow.

Facilities can be adjusted to meet the needs of the user:

  ---------------- ---------- ------------------------------------------
  Numerical Code   Facility   Description
  0                kern       kernel messages
  1                user       user-level messages
  2                mail       mail system
  3                daemon     system daemons
  4                auth       security/authorization messages
  5                syslog     messages generated internally by syslogd
  6                lpr        line printer subsystem
  7                news       network news subsystem
  8                uucp       UUCP subsystem
  9                cron       clock daemon
  10               security   security/authorization messages
  11               ftp        FTP daemon
  12               ntp        NTP subsystem
  13               logaudit   log audit
  14               logalert   log alert
  15               clock      clock daemon (note 2)
  16               local0     local use 0 (local0)
  17               local1     local use 1 (local1)
  18               local2     local use 2 (local2)
  19               local3     local use 3 (local3)
  20               local4     local use 4 (local4)
  21               local5     local use 5 (local5)
  22               local6     local use 6 (local6)
  23               local7     local use 7 (local7)
  ---------------- ---------- ------------------------------------------

  : Facility

### [Filtering]

List of filtering examples:

-   Redirect all incoming messages from all facilities and with all severeties to [/var/log/syslog]

<!-- -->

     *.* -/var/log/syslog

-   Filter out messages with severity critical and save to file [/var/log/critical]

<!-- -->

     *.crit -/var/log/critical

-   Do NOT redirect facilities mail, authentication and cron and mail to [/var/log/messages], look for the keyword **none**

<!-- -->

     mail.none;authpriv.none;cron.none -/var/log/messages

### [Local logging]

Enable local logging from all facilities, to see local events at all.

     $ModLoad imuxsock.so

### [Remote logging]

To use remote logging to a syslog server, specify a client to log to a specific server or servers. And a server to receive messages sent by clients. Before configuring choose the protocol. Syslog messages can be sent using UDP or TCP. UDP is the default protocol and supported on most platforms. Not all platforms support TCP for syslog.

#### [Client]

To enable syslog UDP messages sending add following line to the [/etc/rsyslog.conf] file. In this example rsyslog sends all facilities and all priorities *\*.\** using protocol UDP *@* to remote server *192.0.2.1*

     *.*       @192.0.2.1

To enable TCP support for syslog messages, put following line to the rsyslog configuraton file, TCP is enabled by adding *@@*.

     *.*       @@192.0.2.1

If desired, hostnames can be substituted in for IP addresses.

** Important**\
Substitute `192.0.2.1` with the IP address of the remote rsyslog server that is configured and running to receive any syslog of over its matching port number using UDP or TCP.

Below a example syslog client configuration to send syslog messages to a remote server via TCP.

[FILE] **`/etc/rsyslog.conf`**

    $ModLoad imuxsock.so
    *.*   @@192.0.2.1:10514

    *.info;mail.none;authpriv.none;cron.none      /var/log/messages
    authpriv.*                                    /var/log/secure
    mail.*                                        /var/log/maillog
    cron.*                                        /var/log/cron
    *.emerg                                       *
    uucp,news.crit                                /var/log/spooler
    local7.*                                      /var/log/boot.log

#### [Server]

To Provide UDP log reception and run the server on port 514. Running syslog with UDP is the default configuration.

     $ModLoad imudp
     $UDPServerRun 514

UDP is not a reliable protocol. For more reliability run the server with TCP logging support.

     $ModLoad imtcp
     $InputTCPServerRun 10514

To bind the UDP Port to an IP interface configure following entry, ensure the right sequence of definitions if binding to an interface:

     $ModLoad imudp
     $UDPServerAddress 192.0.2.1 # this entry MUST be before the $UDPServerRun directive
     $UDPServerRun 514

A simple configuration (in basic layout) would look like this one:

[FILE] **`/etc/rsyslog.conf`**

    $ModLoad imuxsock.so
    $ModLoad imtcp.so
    $InputTCPServerAddress 192.0.2.1
    $InputTCPServerRun 10514
    $ModLoad imudp.so
    $UDPServerAddress 192.0.2.1
    $UDPServerRun 514
    *.info;mail.none;authpriv.none;cron.none      /var/log/messages
    authpriv.*                                    /var/log/secure
    mail.*                                        /var/log/maillog
    cron.*                                        /var/log/cron
    *.emerg                                       *
    uucp,news.crit                                /var/log/spooler
    local7.*                                      /var/log/boot.log

### [Database logging]

Rsyslog supports logging to following databases:

-   [MariaDB](https://wiki.gentoo.org/wiki/MariaDB "MariaDB")
-   [MySQL](https://wiki.gentoo.org/wiki/MySQL "MySQL")
-   [PostgreSQL](https://wiki.gentoo.org/wiki/PostgreSQL "PostgreSQL")
-   Oracle

After choosing the database logs will be stored to a proper USE flag needs to be enabled and rsyslog has to be rebuild before continuing. This example uses a MySQL database.

** Note**\
Next steps assume a working MySQL database server running on localhost, for installation details follow the [MySQL](https://wiki.gentoo.org/wiki/MySQL "MySQL") article.

The package ships a SQL script named createDB.sql to create the database layout.

[FILE] **`/usr/share/rsyslog/scripts/mysql/createDB.sql`**

    CREATE DATABASE Syslog;
    USE Syslog;
    CREATE TABLE SystemEvents
    (
            ID int unsigned not null auto_increment primary key,
            CustomerID bigint,
            ReceivedAt datetime NULL,
            DeviceReportedTime datetime NULL,
            Facility smallint NULL,
            Priority smallint NULL,
            FromHost varchar(60) NULL,
            Message text,
            NTSeverity int NULL,
            Importance int NULL,
            EventSource varchar(60),
            EventUser varchar(60) NULL,
            EventCategory int NULL,
            EventID int NULL,
            EventBinaryData text NULL,
            MaxAvailable int NULL,
            CurrUsage int NULL,
            MinUsage int NULL,
            MaxUsage int NULL,
            InfoUnitID int NULL ,
            SysLogTag varchar(60),
            EventLogType varchar(60),
            GenericFileName VarChar(60),
            SystemID int NULL
    );
    CREATE TABLE SystemEventsProperties
    (
            ID int unsigned not null auto_increment primary key,
            SystemEventID int NULL ,
            ParamName varchar(255) NULL ,
            ParamValue text NULL
    );

Import the [/usr/share/rsyslog/scripts/mysql/createDB.sql] file to create the `Syslog` database.

`user `[`$`]`mysql -u root -p < /usr/share/rsyslog/scripts/mysql/createDB.sql`

Create a database user for the Syslog database:

`mysql>``GRANT ALL ON Syslog.* TO rsyslog-user@localhost IDENTIFIED BY - 'MySecretPassword'; `

`mysql>``FLUSH PRIVILEGES; `

To provide SQL database logging support, enable the needed module in [/etc/rsyslog.conf]

     $ModLoad ommysql.so

Tell rsyslog to forward all data to the database, add following to the end of the [/etc/rsyslog.conf] file:

     *.* :ommysql:localhost,Syslog,rsyslog-user,MySecretPassword

Finally Restart the rsyslog server to adapt new settings

`root `[`#`]`rc-service rsyslog restart`

### [Services]

** Warning**\
There is considerable conflict between **systemd** and **rsyslogd**. Try not to use both simultaneously or, worse, configure them to report to each other, as this can result in 100% CPU usage. For maximum flexibility and security, use **rsyslogd**.

#### [OpenRC]

To add the [rsyslogd] daemon to the default runlevel, so that logging starts with the system:

`root `[`#`]`rc-update add rsyslog default`

After the emerge has finished, rsyslog should work out of the box with the default configuration; at least for local logging.

To start the [rsyslogd] daemon:

`root `[`#`]`rc-service rsyslog start`

Check file [/var/log/messages] for syslog entries:

`root `[`#`]`tail -f /var/log/messages`

    2024-01-30T23:24:27.462647+01:00 server rsyslogd: [origin software="rsyslogd" swVersion="8.2212.0" x-pid="2404" x-info="https://www.rsyslog.com"] start

## [Templates]

Many vendors format their syslog messages differently. If the network equipment logs to a central rsyslog server the difference in logging will be easy to notice. After some time of log dumping it will be difficult to filter the syslog server messages for a certain

-   Date
-   Facility
-   Severity
-   Host
-   Syslogtag
-   ProcessID
-   MessageType
-   Message

To unify syslog messages to a certain or preferred format, Rsyslog uses templates which parse arriving messages and \"rewrites\" them to the desired format.

To maintain a simple and modular configuration, templates are stored within the [/etc/rsyslog.d/] directory. To include files stored within the rsyslog.d directory add following line to [/etc/rsyslog.conf] file:

     $IncludeConfig /etc/rsyslog.d/*.conf

Templates should be stored to the [/etc/rsyslog.d/] directory.

`root `[`#`]`cd /etc/rsyslog.d/`

** Important**\
Following templates are working very good, but are not perfect.

Here a simple template for a cisco IOS host which logs to rsyslogd:

[FILE] **`/etc/rsyslog.d/template_cisco.conf`**

    $template mysql_cisco, "insert into SystemEvents (Message, Facility, FromHost, Priority, DeviceReportedTime, ReceivedAt, InfoUnitID, SysLogTag) values ('%msg:R,ERE,1,DFLT:%[A-Z0-9_-]+: (.*)--end%', %syslogfacility%, '%fromhost%', %syslog
    priority%, '%timereported:::date-mysql%', '%timegenerated:::date-mysql%', %iut%, '%msg:R,ERE,0,DFLT:%[A-Z0-9_-]+:--end%')",SQL

Here a simple template for a ScreenOS host which logs to rsyslogd:

[FILE] **`/etc/rsyslog.d/template_netscreen.conf`**

    $template mysql_netscreen, "insert into SystemEvents (Message, Facility, FromHost, Priority, DeviceReportedTime, ReceivedAt, InfoUnitID, SysLogTag) values ('%msg:R,ERE,1,DFLT:[a-zA-Z0-9-]+: (.*)--end%', %syslogfacility%, '%fromhost%', %s
    yslogpriority%, '%timereported:::date-mysql%', '%timegenerated:::date-mysql%', %iut%, '%msg:R,ERE,0,DFLT:[a-zA-Z0-9-]+:--end%')",SQL

Here a simple template for Linux host which logs to rsyslogd:

[FILE] **`/etc/rsyslog.d/template_linux.conf`**

    $template mysql_linux, "insert into SystemEvents (Message, Facility, FromHost, Priority, DeviceReportedTime, ReceivedAt, IntoUnitID, SysLogTag) values ('%msg%', %syslogfacility%, '%HOSTNAME%', %syslogpriority%, '%timereported:::
    date-mysql%', '%timegenerated:::date-mysql%', %iut%, '%syslogtag:R,ERE,1,FIELD:(.+)(\[[0-9]\]).*--end%')" ,SQL

Configure rsyslogd which predefined template to apply to which facility, add following template references to the end of the [/etc/rsyslog.conf] file:

-   All messages arriving at facility **local4**, are Cisco IOS messages:

<!-- -->

     local4.* :ommysql:localhost,Syslog,rsyslog-user,MySecretPassword;mysql_cisco

-   All messages arriving at facility **local5** , are ScreenOS messages:

<!-- -->

     local5.* :ommysql:localhost,Syslog,rsyslog-user,MySecretPassword;mysql_netscreen

-   All messages arriving at syslog consider as Linux messages, and ignore **local4** and **local5** facilities which have their own templates.

<!-- -->

     *.*;local4.none;local5.none :ommysql:localhost,Syslog,rsyslog-user,MySecretPassword;mysql_linux

The following is an example of how the [/etc/rsyslog.conf] file could look on a syslog **server** with working templates:

[FILE] **`/etc/rsyslog.conf`**

    $ModLoad imudp
    $UDPServerRun 514
    $ModLoad ommysql.so
    $IncludeConfig /etc/rsyslog.d/*.conf

    *.info;mail.none;authpriv.none;cron.none    -/var/log/messages
    authpriv.*                  /var/log/secure
    mail.*                      -/var/log/maillog
    cron.*                      -/var/log/cron
    *.emerg                     *
    uucp,news.crit                  -/var/log/spooler
    local7.*                    /var/log/boot.log

    local4.* :ommysql:localhost,Syslog,rsyslog-user,MySecretPassword;mysql_cisco
    local5.* :ommysql:localhost,Syslog,rsyslog-user,MySecretPassword;mysql_netscreen
    *.*;local4.none;local5.none :ommysql:localhost,Syslog,rsyslog-user,MySecretPassword;mysql_linux

Reload rsyslog server to apply new changes:

`root `[`#`]`rc-service rsyslog reload`

Further examples can be found [here](http://www.rsyslog.com/doc/rsyslog_conf_templates.html).

## [Usage]

There is only one executable, a daemon called [rsyslogd].

### [Invocation]

Command line options are NOT embedded into the [rsyslogd]. For that address to [[[rsyslogd(8)]](https://linux.die.net/man/8/rsyslogd)][[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page").

### [Validate Configuration Files]

To syntax check the default configuration files ([/etc/rsyslog.conf]) for rsyslogd, validate the config file by executing:

`root `[`#`]`rsyslogd -N1`

    rsyslogd: version 8.2302.0, config validation run (level 1), master config /etc/rsyslog.conf
    rsyslogd: End of config validation run. Bye.

To validate configuration files in non-root testing environment, execute:

`user `[`$`]`/usr/sbin/rsyslogd -N1 -f /usr/share/doc/rsyslog/examples/rsyslog.d/console.conf`

    rsyslogd: version 8.2302.0, config validation run (level 1), master config /usr/share/doc/rsyslog/examples/rsyslog.d/console.conf
    rsyslogd: End of config validation run. Bye.

## [Removal]

Removal of [rsyslog] package (toolkit & library) can be done by executing:

`root `[`#`]`emerge --ask --depclean --verbose app-admin/rsyslog`

## [Troubleshooting]

Check if a syslog process is running :

`root `[`#`]`ps ux | grep rsyslog`

    root     9161  0.0  0.0 1323652  3424 ?        Sl   00:51   0:00 /usr/sbin/rsyslogd -c5 -i /var/run/rsyslogd.pid -f /etc/rsyslog.conf

Verify network configuration:

`root `[`#`]`ss -tulpn | grep rsyslog`

    udp   UNCONN 0      0            0.0.0.0:514       0.0.0.0:*    users:(("rsyslogd",pid=1710,fd=6))
    udp   UNCONN 0      0            0.0.0.0:514       0.0.0.0:*    users:(("rsyslogd",pid=1710,fd=4))
    udp   UNCONN 0      0               [::]:514          [::]:*    users:(("rsyslogd",pid=1710,fd=7))
    udp   UNCONN 0      0               [::]:514          [::]:*    users:(("rsyslogd",pid=1710,fd=5))

Verify with the command logger, if messages are arriving in at the syslogserver:

`user `[`$`]`logger -t test my syslog-test-message`

Following message should appear in the [/var/log/messages] file if rsyslog is working properly:

`root `[`#`]`tail /var/log/messages`

    ...
    2011-11-23T00:47:05+01:00 Rsyslogserver test: my syslog-test-message

## [See also]

-   [Metalog](https://wiki.gentoo.org/wiki/Metalog "Metalog") --- an alternative syslog daemon
-   [Sysklogd](https://wiki.gentoo.org/wiki/Sysklogd "Sysklogd") --- utility that reads and logs messages to the system console, logs files, other machines and/or users as specified by its configuration file.
-   [Syslog-ng](https://wiki.gentoo.org/wiki/Syslog-ng "Syslog-ng") --- a powerful, highly configurable monitoring and logging daemon.

## [External resources]

-   [Official documentation](https://www.rsyslog.com/doc/master/index.html)
-   [Rsyslog Templates HOWTO](http://www.rsyslog.com/doc/rsyslog_conf_templates.html)
-   [RFC 5424 - The Syslog Protocol](https://tools.ietf.org/html/rfc5424)