**Resources**

[[]][Home](https://www.syslog-ng.com/products/open-source-log-management/)

[[]][Package information](https://packages.gentoo.org/packages/app-admin/syslog-ng)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Syslog-ng "wikipedia:Syslog-ng")

[[]][GitHub](https://github.com/balabit/syslog-ng)

[[]][[#syslog-ng](ircs://irc.libera.chat/#syslog-ng)] ([[webchat](https://web.libera.chat/#syslog-ng)])

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/syslog-ng)

**syslog-ng** is a powerful, highly configurable monitoring and logging daemon.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Additional software]](#Additional_software)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Network Server]](#Network_Server)
        -   [[2.1.1] [Relays]](#Relays)
        -   [[2.1.2] [Using logger with a network source]](#Using_logger_with_a_network_source)
    -   [[2.2] [Global Options]](#Global_Options)
    -   [[2.3] [Object types]](#Object_types)
        -   [[2.3.1] [Source]](#Source)
            -   [[2.3.1.1] [Receive logs networked to localhost]](#Receive_logs_networked_to_localhost)
            -   [[2.3.1.2] [Create a separate source for traffic on a LAN interface]](#Create_a_separate_source_for_traffic_on_a_LAN_interface)
        -   [[2.3.2] [Destination]](#Destination)
        -   [[2.3.3] [Filter]](#Filter)
        -   [[2.3.4] [Templates]](#Templates)
            -   [[2.3.4.1] [Hash]](#Hash)
            -   [[2.3.4.2] [Anonymizing IP addresses]](#Anonymizing_IP_addresses)
            -   [[2.3.4.3] [Format messages in Python]](#Format_messages_in_Python)
    -   [[2.4] [Security Handbook]](#Security_Handbook)
    -   [[2.5] [Example configuration]](#Example_configuration)
    -   [[2.6] [Service]](#Service)
        -   [[2.6.1] [OpenRC]](#OpenRC)
        -   [[2.6.2] [systemd]](#systemd)
    -   [[2.7] [Docker Image]](#Docker_Image)
        -   [[2.7.1] [Starting for the first time]](#Starting_for_the_first_time)
        -   [[2.7.2] [Testing]](#Testing)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Incorrect timestamps on musl-based systems]](#Incorrect_timestamps_on_musl-based_systems)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)
-   [[6] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [app-admin/syslog-ng](https://packages.gentoo.org/packages/app-admin/syslog-ng) [[]] [syslog replacement with advanced filtering features]

  --------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`amqp`](https://packages.gentoo.org/useflags/amqp)                   Enable support for AMQP destinations
  [`caps`](https://packages.gentoo.org/useflags/caps)                   Use Linux capabilities library to control privilege
  [`dbi`](https://packages.gentoo.org/useflags/dbi)                     Enable dev-db/libdbi (database-independent abstraction layer) support
  [`geoip2`](https://packages.gentoo.org/useflags/geoip2)               Add support for geo lookup based on IPs via dev-libs/libmaxminddb
  [`grpc`](https://packages.gentoo.org/useflags/grpc)                   Enable GRPC based driver support (OpenTelemetry) via net-libs/grpc
  [`http`](https://packages.gentoo.org/useflags/http)                   Enable support for HTTP destinations
  [`json`](https://packages.gentoo.org/useflags/json)                   Enable support for JSON template formatting via dev-libs/json-c
  [`kafka`](https://packages.gentoo.org/useflags/kafka)                 Enable support for Kafka destinations
  [`mongodb`](https://packages.gentoo.org/useflags/mongodb)             Enable support for mongodb destinations
  [`mqtt`](https://packages.gentoo.org/useflags/mqtt)                   Enable MQTT support via net-libs/paho-mqtt-c
  [`pacct`](https://packages.gentoo.org/useflags/pacct)                 Enable support for reading Process Accounting files (EXPERIMENTAL, Linux only)
  [`python`](https://packages.gentoo.org/useflags/python)               Add optional support/bindings for the Python language
  [`redis`](https://packages.gentoo.org/useflags/redis)                 Enable support for Redis destinations
  [`smtp`](https://packages.gentoo.org/useflags/smtp)                   Enable support for SMTP destinations
  [`snmp`](https://packages.gentoo.org/useflags/snmp)                   Add support for the Simple Network Management Protocol if available
  [`spoof-source`](https://packages.gentoo.org/useflags/spoof-source)   Enable support for spoofed source addresses
  [`systemd`](https://packages.gentoo.org/useflags/systemd)             Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`tcpd`](https://packages.gentoo.org/useflags/tcpd)                   Add support for TCP wrappers
  [`test`](https://packages.gentoo.org/useflags/test)                   Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  --------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-17 11:55] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[app-admin/syslog-ng]](https://packages.gentoo.org/packages/app-admin/syslog-ng)[]]:

`root `[`#`]`emerge --ask app-admin/syslog-ng`

** Warning**\
It is a bad idea to run more than one system logger on a physical host. Other local loggers should be removed or disabled.

### [Additional software]

When using a system logger such as [syslog-ng], it is a wise idea to install log rotation software to appropriately trim the logs as they consume more disk space. Logrotate is a fine option:

`root `[`#`]`emerge --ask app-admin/logrotate`

## [Configuration]

[syslog-ng] is configured using [C](https://wiki.gentoo.org/wiki/C "C") syntax. Directives are defined with an **object type**, **identifier** (name), and **parameters**.

** Note**\
Depending on the object type, certain parameters may be required.

Required parameters have a pre-defined order, while optional ones can be defined in any order.

*Option* directives start with an **identifier**, while *main body* directives must first be defined with an **object type**.

** Tip**\
Commas can be used to separate options and parameters for readability, they are ignored by the processor.

The default configuration provided by the ebuild is located at [/etc/syslog-ng/syslog-ng.conf] and contains the following:

[FILE] **`/etc/syslog-ng/syslog-ng.conf`syslog-ng.conf version 4.0**

    @version: 4.0
    #
    # Syslog-ng default configuration file for Gentoo Linux

    # https://bugs.gentoo.org/426814
    @include "scl.conf"

    options ;

    source src ;

    destination messages ;

    # By default messages are logged to tty12...
    destination console_all ;
    # ...if you intend to use /dev/console for programs like xconsole
    # you can comment out the destination line above that references /dev/tty12
    # and uncomment the line below.
    #destination console_all ;

    log ;
    log ;

** Note**\
[syslog-ng] 3.2+ captures messages using the kernel\'s log device at [/dev/log] to the **system()** driver.

** Note**\
Option and parameter names (reserved words) can be written with either [\_] or [-]. For example, **chain_hostnames**, and **chain-hostnames** are processed identically.

### [Network Server]

When it comes to syslog, most people still think about [RFC3164](https://datatracker.ietf.org/doc/html/rfc3164), which is also often called legacy syslog. It is old, not really well-standardized, as it just tries to describe existing practice. Still, most syslog messages arrive in this format.

[RFC5424](https://datatracker.ietf.org/doc/html/rfc5424) is a well-standardized format for syslog messages, right from the beginning. It has a more precise timestamp, and can forward name-value pairs. However, it is not widely used.

What we can see a lot more often is that if someone wants to forward name-value pairs between syslog servers, they use a legacy [RFC3164](https://datatracker.ietf.org/doc/html/rfc3164) syslog header, and a JSON formatted message part.

When it comes to collecting log messages over a network, [syslog-ng] has three modes of operation:

-   **Client mode** - syslog-ng is collecting logs from the client and sending them to the central server directly or through a relay.
-   **Relay mode** - syslog-ng is collecting logs from clients through the network and sending them to the central server directly or through another relay.
-   **Server mode** - syslog-ng is collecting logs from clients and / or relays and storing them either locally or in a non-syslog destination-driver.

Of course, in the real world, these modes are not so strictly separated. Some relays might both store and forward log messages.

#### [Relays]

Relays have many important roles in a logging infrastructure. Many devices use UDP for log transport. UDP is an unreliable protocol, so you want to collect these log messages as close to the source as possible.

Using relays can give structure and additional security to your logging infrastructure. You can install a relay for each department or site. This is especially important when the central server is at a remote location. Relays ensure that log messages leave clients immediately even if the central server is unavailable due to maintenance or network problems.

[FILE] **`/etc/syslog-ng/netsource.conf`netsource.conf version 4.0**

    @version: 4.0

    source s_tcp ;
    destination d_file ;
    log ;

Stop the running syslog implementation and start [syslog-ng] with this configuration in the foreground with debug information enabled:

`root `[`#`]`syslog-ng -Fvde -f /etc/syslog-ng/netsource.conf`

With [syslog-ng] started in the foreground and with debugging enabled, you should see the incoming log message on the screen. The file /var/log/fromnet should show your test message at the end.

#### [Using logger with a network source]

From another terminal we can use the logger command to generate test messages.

-   **-T** - TCP
-   **-n** - Hostname or IP
-   **-P** - Port
-   **test message** - Log message

`root `[`#`]`logger -T -n 127.0.0.1 -P 514 test message`

### [Global Options]

Global options, specified with the **options** statement are applied to applicable objects, some include:

-   **threaded** - Used to enable threading.
-   **chain_hostnames** - Used to enable hostname chaining, enabling this can interfere with how [syslog-ng] counts hosts.
-   **stats_freq** - Adjusts how often [syslog-ng] prints a stats line to the logs.
-   **mark_freq** - Adjusts how often [syslog-ng] prints a mark line in the logs.

** Tip**\
A comprehensive overview of configuration options is available at [syslog-ng admin guide](https://www.syslog-ng.com/technical-documents/doc/syslog-ng-open-source-edition/3.37/administration-guide/).

### [Object types]

-   **source**^[\[1\]](#cite_note-1)^ - Defined with a driver, a ingress tool.
-   **destination** - Egress point for log information. Log records received by any source can be sent to one or more destinations.
-   **log** - Defines the path between a **source** and **destination**, without **log** directives, **source**s and **destination**s are independent objects.
-   **filter** - Filters can be added to **log** directives to change which records will be sent to the **destination**.
-   **parser** - Segments log contents into different fields to assist in log processing and handling.
-   **rewrite rule** - Used to rewrite the contents of a log record.
-   **template**^[\[2\]](#cite_note-2)^ - Templates can be used to define formats using macros or parameters.

#### [Source]

The default source is defined as:

[FILE] **`/etc/syslog-ng/syslog-ng.conf`Define the default **source** as being the *system* logger**

    source src ;

** Tip**\
The name *src* is arbitrary, but must be used consistently.

** Note**\
*system()* references [/dev/log]^[\[3\]](#cite_note-3)^.

##### [Receive logs networked to localhost]

[FILE] **`/etc/syslog-ng/syslog-ng.conf`Define *src* to receive logs on udp://localhost:514**

    source src ;

##### [Create a separate source for traffic on a LAN interface]

[FILE] **`/etc/syslog-ng/syslog-ng.conf`Define *lan_src* to receive logs on ://192.168.0.2:514**

    source lan_src ;

** Note**\
Using TCP is recommended for logging over a network, as [syslog] implementations generally have no mechanism for ensuring logs are received.

** Important**\
Older implementations of [syslog] may only support UDP, as it is defined in [RC3164](https://datatracker.ietf.org/doc/html/rfc3164#section-2).

#### [Destination]

To define a **destination** log file, *test_log*, which writes to [/var/log/test.log], the following configuration can be used:

[FILE] **`/etc/syslog-ng/syslog-ng.conf`Define *test_log* to write to [/var/log/test.log]**

    destination test_log ;

** Important**\
**syslog-ng** will create destination files, but will not create destination directories.

#### [Filter]

To add a **filter** which matches log messages starting with \"Test string\|\", the following configuration can be used:

[FILE] **`/etc/syslog-ng/syslog-ng.conf`Define *f_test* to match messages starting with \"Test string\|\"**

    filter f_test ;

To add a **filter** which matches logs coming from hosts \"10.10.10.1\" \"10.10.10.3\" and \"10.10.10.5\":

[FILE] **`/etc/syslog-ng/syslog-ng.conf`Define *f_test2* to match messages from 10.10.10.\"**

    filter f_test2 ;

#### [Templates]

The [syslog-ng] application allows you to define message templates, and reference them from every object that can use a template. Templates can include strings, macros (for example date, the hostname, and so on), and template functions. For example, you can use templates to create standard message formats or filenames. For a list of macros available in [syslog-ng] Open Source Edition, see Macros of [syslog-ng] Fields from the structured data (SD) part of messages using the new IETF-syslog standard can also be used as macros.

[FILE] **`/etc/syslog-ng/syslog-ng.conf`Example how to use filters on a destination source**

    template template_date_format -$-$ | $:$:$ | $]\: $$\n");
        template_escape(no);
    };

    destination messages ;
    log ;

Template objects have a single option called template-escape(), which is disabled by default (template-escape(no)). This behavior is useful when the messages are passed to an application that cannot handle escaped characters properly. Enabling template escaping (template-escape(yes)) causes [syslog-ng] to escape the \', \", and backslash characters from the messages.

If you do not want to enable the template-escape() option (which is rarely needed), you can define the template without the enclosing braces.

Templates can also be used inline, if they are used only at a single location.

[FILE] **`/etc/syslog-ng/syslog-ng.conf`**

    destination d_file  $ $\n") );
    };

The following file destination uses macros to daily create separate logfiles for every client host.

[FILE] **`/etc/syslog-ng/syslog-ng.conf`**

    destination d_file .$.$/$.log");
    };

The following example shows how to use this template function to store log messages in JSON format:

[FILE] **`/etc/syslog-ng/syslog-ng.conf`**

    destination d_json  USE flag and then `tfhash` module has to loaded.

The following example calculates the SHA256 hash of the hostname of the message:

[FILE] **`/etc/syslog-ng/syslog-ng.conf`**

    $(sha256 $HOST)

The following example calculates the SHA256 hash of the hostname, using the salted string to salt the result:

[FILE] **`/etc/syslog-ng/syslog-ng.conf`**

    $(sha1 $HOST salted)

To replace the hostname with its hash, use a rewrite rule:

[FILE] **`/etc/syslog-ng/syslog-ng.conf`**

    rewrite r_rewrite_hostname;

##### [Anonymizing IP addresses]

The following example replaces every IPv4 address in the MESSAGE part with its SHA256 hash:

[FILE] **`/etc/syslog-ng/syslog-ng.conf`**

    rewrite pseudonymize_ip_addresses_in_message ;

** Note**\
sha256 can be one of md5, md4, sha1, sha256, sha512 and \"hash\", which is equivalent to md5. Macros are expected as arguments, and they are concatenated without the use of additional characters.

##### [Format messages in Python]

** Note**\
Formatting messages in python requires [syslog-ng] to be installed with the python useflag enabled.

Getting log messages into the desired format can sometimes be a problem, but with [syslog-ng] you can use Python to get exactly the format that is neededed. The [syslog-ng] Python template function allows you to write custom templates for [syslog-ng] in Python. The Python template function can work on the whole log message which is passed on to it automatically as an object or on the data received as argument.

Here is a complete working configuration customized to test the Python template function and replace [/etc/syslog/syslog-ng.conf] with it:

[FILE] **`/etc/syslog-ng/syslog-ng.conf`syslog-ng.conf version 4.0**

    @version: 4.0

    source s_internal ;
    destination d_internal ;
    log ;

    python ;

    destination d_local  Host: $(python resolve_host $) IP: $\n")
        );
    };

    log ;
        destination(d_local);
    };

Restart [syslog-ng] and open a second terminal and send a message using the logger command to the port defined in the configuration:

`user `[`$`]`logger -n 127.0.0.1 -T -P 1234 --rfc3164 8.8.8.8`

A new file [resolve.txt] should be created in the [/var/log] directory. Should it possibly not appear, make sure [syslog-ng] has the python useflag enabled.

`2023-05-20T21:46:26+02:00 Host: dns.google IP: 8.8.8.8`

### [Security Handbook]

The Gentoo Security Handbook [Logging](https://wiki.gentoo.org/wiki/Security_Handbook/Logging "Security Handbook/Logging") provides more information on the security aspects of logging.

For a more comprehensive configuration see the configuration provided by [Security Handbook: Hardened Syslog-ng logging](https://wiki.gentoo.org/wiki/Security_Handbook/Logging#Syslog-ng "Security Handbook/Logging").

Alternatively, this configuration can be viewed using [bzcat], part of [[[app-arch/bzip2]](https://packages.gentoo.org/packages/app-arch/bzip2)[]], and is available at:

[/usr/share/doc/syslog-ng-\*/syslog-ng.conf.gentoo.hardened.bz2]

### [Example configuration]

The default **source** for system messages, *src*, can be defined with:

[FILE] **`/etc/syslog-ng/syslog-ng.conf`Define the default **source** as being the *system* logger**

    source src ;

A **destination** must be configured, otherwise nothing can be logged:

[FILE] **`/etc/syslog-ng/syslog-ng.conf`Define the **destination** *messages* as a file at [/var/log/message]**

    destination messages ;

To direct logs being received through *src* to *messages*:

[FILE] **`/etc/syslog-ng/syslog-ng.conf`Log everything received by *src* to *messages***

    log ;

### [Service]

#### [OpenRC]

To add the [syslog-ng] daemon to the *default* runlevel, so that logging starts with the system:

`root `[`#`]`rc-update add syslog-ng default`

To start the [syslog-ng] daemon:

`root `[`#`]`rc-service syslog-ng start`

#### [systemd]

** Important**\
If the system is running [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd"), the default **source** needs to be changed to the following^[\[4\]](#cite_note-4)^:

[FILE] **`/etc/syslog-ng/syslog-ng.conf`Define the default **source** for Systemd**

    source src ;

To start the [syslog-ng] daemon with the system, the service can be enabled with:

`root `[`#`]`systemctl enable syslog-ng@default`

To start the daemon:

`root `[`#`]`systemctl start syslog-ng@default`

### [Docker Image]

Your central log server can also run in a Docker container. If you wish to deploy your log server running [syslog-ng] in a Docker container, it is available as a ready-to-use image from the Docker Hub, already passing 500K pulls. The image is based on the latest Debian and the latest stable version of [syslog-ng]. It has all modules, including Java modules and experimental modules from the incubator.

It is possible to to issue a single command to download the image and run it in a container on your host machine. In addition to, of course, sharing that command with you, my goal in this post is to explain how it is made up and what it does.

To be able to use them, we need enable these ports both in the [syslog-ng] configuration ([syslog-ng.conf]) and in the command line starting the Docker container.

#### [Starting for the first time]

If you do not have a configuration file at hand for testing, create one. Here is a simple syslog-ng.conf, which listens to the legacy syslog protocol on UDP port 514, the new syslog protocol on TCP port 601, and stores any incoming log messages in a file called /var/log/syslog.

[FILE] **`/data/syslog-ng/conf/syslog-ng.conf:/etc/syslog-ng/syslog-ng.conf`syslog-ng.conf version 4.1**

    @version: 4.1

    source s_net ;

    destination d_file ;

    log ;
    )

You can map files or directories from your host into the container. In the case of [syslog-ng.conf], you have a simple configuration file with all the settings in a single file and you do not have any encryption keys, so mapping the configuration file is the easiest. In any other scenario, you should map a complete directory for the configuration.

If you store all your log messages in a database, there is not much need for persistent storage for your container. If your central log server also stores data, there is a good chance that you will want to have access to those logs even if you switch to another [syslog-ng] image. In this case, you should map a directory from the host machine, so your log storage is independent from your Docker containers.

If you have your [syslog-ng.conf] under [/data/syslog-ng/conf] and plan to store your logs in the [/data/syslog-ng/logs] directory, you can use the following command line to get started. It 1) starts the container in interactive mode, 2) maps two network ports from the host to the container, 3) maps the configuration file and log directory, and 4) adds some debug options to [syslog-ng]. The name of the container will be "syslog-ng" and Docker will use the latest available [syslog-ng] image from the Docker Hub.

`user `[`$`]`docker run -it -v /data/syslog-ng/conf/syslog-ng.conf:/etc/syslog-ng/syslog-ng.conf -v /data/syslog-ng/logs:/var/log -p 514:514 -p 601:601 -name syslog-ng balabit/syslog-ng:latest -edv`

When you first execute this command, it can take a few minutes until [syslog-ng] is up and running, as the image is downloaded over the Internet. On subsequent executions, Docker will use the local copy and start immediately.

#### [Testing]

Using the **docker ps** command from an other terminal you can check, that your container is up and running. You can see many information about the image, including the opened network ports.

`user `[`$`]`docker ps`

    CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
    b947a3411c1a balabit/syslog-ng:latest “/usr/sbin/syslog-ng” 18 seconds ago Up 17 seconds 0.0.0.0:514->514/tcp, 514/udp, 0.0.0.0:601->601/tcp, 6514/tcp syslog-ng

The [loggen] command can generate you a few sample logs. If you used the above configuration and directories, you should see a flood of messages on the screen where you started the container and also new messages in the file /data/syslog-ng/logs/syslog

`user `[`$`]`loggen -i -S -P localhost 601`

    average rate = 1006.53 msg/sec, count=10066, time=10.000, (average) msg size=260, bandwidth=255.42 kB/sec

## [[] Troubleshooting]

### [Incorrect timestamps on musl-based systems]

If the time zone is set according to [the musl usage guide](https://wiki.gentoo.org/wiki/Musl#Timezones "Musl"), the system will still send messages in UTC format. If the logger is additionally configured to read messages from a file (e.g. [/proc/kmsg]), the messages will be in the specified time zone. This causes the logger to output a log file with incorrectly written timestamps. To fix this problem, it is possible to specify the same time zone that is used in the system:

[FILE] **`/etc/syslog-ng/syslog-ng.conf`**

    options ;

** Important**\
The workaround requires [[[sys-libs/timezone-data]](https://packages.gentoo.org/packages/sys-libs/timezone-data)[]] to be installed, POSIX time zone codes are not supported ^[\[5\]](#cite_note-5)^.

## [See also]

-   [syslog-ng (Security Handbook)](https://wiki.gentoo.org/wiki/Security_Handbook/Logging#Syslog-ng "Security Handbook/Logging") - The system logging with syslog-ng is covered in the [Security Handbook](https://wiki.gentoo.org/wiki/Security_Handbook "Security Handbook").
-   [Metalog](https://wiki.gentoo.org/wiki/Metalog "Metalog") --- an alternative syslog daemon
-   [Rsyslog](https://wiki.gentoo.org/wiki/Rsyslog "Rsyslog") --- open source system for high performance log processing.
-   [Sysklogd](https://wiki.gentoo.org/wiki/Sysklogd "Sysklogd") --- utility that reads and logs messages to the system console, logs files, other machines and/or users as specified by its configuration file.

## [External resources]

-   [https://wiki.archlinux.org/title/Syslog-ng](https://wiki.archlinux.org/title/Syslog-ng)

## [References]

1.  [[[↑](#cite_ref-1)] [[https://www.syslog-ng.com/technical-documents/doc/syslog-ng-open-source-edition/3.37/administration-guide/17#TOPIC-1828968](https://www.syslog-ng.com/technical-documents/doc/syslog-ng-open-source-edition/3.37/administration-guide/17#TOPIC-1828968)]]
2.  [[[↑](#cite_ref-2)] [[https://www.syslog-ng.com/technical-documents/doc/syslog-ng-open-source-edition/3.30/administration-guide/67](https://www.syslog-ng.com/technical-documents/doc/syslog-ng-open-source-edition/3.30/administration-guide/67)]]
3.  [[[↑](#cite_ref-3)] [[https://www.syslog-ng.com/technical-documents/doc/syslog-ng-open-source-edition/3.37/administration-guide/28#TOPIC-1829013](https://www.syslog-ng.com/technical-documents/doc/syslog-ng-open-source-edition/3.37/administration-guide/28#TOPIC-1829013)]]
4.  [[[↑](#cite_ref-4)] [Balabit. [Collecting messages from the systemd-journal system log storage](https://www.balabit.com/sites/default/files/documents/syslog-ng-ose-latest-guides/en/syslog-ng-ose-guide-admin/html/configuring-sources-journal.html), [The syslog-ng Open Source Edition 3.7 Administrator Guide](https://www.balabit.com/sites/default/files/documents/syslog-ng-ose-latest-guides/en/syslog-ng-ose-guide-admin/html/index.html), January 22nd, 2016. Retrieved on January 30th, 2016.]]
5.  [[[↑](#cite_ref-5)] [[https://syslog-ng.github.io/admin-guide/060_Sources/030_Wildcard-file/000_Wildcard-file_options#time-zone](https://syslog-ng.github.io/admin-guide/060_Sources/030_Wildcard-file/000_Wildcard-file_options#time-zone)]]