**Resources**

[[]][Home](http://www.munin-monitoring.org)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Munin_(network_monitoring_application) "wikipedia:Munin (network monitoring application)")

[[]]This article has some todo items:\

-   Master side Nagios integration.

**Munin** is a networked resource monitoring tool that can help analyze resource trends and \"what just happened to kill our performance?\" problems.

Munin implements a master and slave node structure; one master node with many slave nodes. The master node gathers data from the slave nodes, and produces HTML output. Generally these will be placed in the directory accessible via a web server, and can be viewed with a web browser.

## Contents

-   [[1] [USE flags]](#USE_flags)
-   [[2] [Installation and setup]](#Installation_and_setup)
    -   [[2.1] [Node (client)]](#Node_.28client.29)
    -   [[2.2] [Master]](#Master)
        -   [[2.2.1] [cron configuration]](#cron_configuration)
        -   [[2.2.2] [Generating reports through cron]](#Generating_reports_through_cron)
        -   [[2.2.3] [Generating report through CGI]](#Generating_report_through_CGI)
            -   [[2.2.3.1] [Graph-only CGI]](#Graph-only_CGI)
            -   [[2.2.3.2] [Full CGI]](#Full_CGI)
            -   [[2.2.3.3] [Static reports with CGI zoom]](#Static_reports_with_CGI_zoom)
            -   [[2.2.3.4] [Update permissions]](#Update_permissions)
    -   [[2.3] [SSH Transport and Munin Async]](#SSH_Transport_and_Munin_Async)
-   [[3] [Integration with Nagios or Icinga]](#Integration_with_Nagios_or_Icinga)
    -   [[3.1] [Nagios/Icinga host side]](#Nagios.2FIcinga_host_side)
-   [[4] [Gentoo Linux exclusives]](#Gentoo_Linux_exclusives)
-   [[5] [Troubleshooting]](#Troubleshooting)
-   [[6] [See Also]](#See_Also)
-   [[7] [External resources]](#External_resources)

## [USE flags]

The USE flags for Munin are handled in a peculiar way: most of the flags are related to the node, rather than the master (with a few, more or less obvious, exceptions), and are designed to bring in the required dependencies. When the flags are disabled, the plugins are **not** removed from the package, which means that it\'s sufficient to just merge the dependencies to get them working, instead of rebuilding Munin. This has been decided because the plugins are generally static, for what concern dependencies.

A notable exception is the `java` USE flag that actually does remove some plugins. The reason is simply that for the plugins to work, you need a JAR library that is part of Munin, and is thus only built with the flag enabled, so you\'d still be rebuilding the package to enable or disable it.

### [USE flags for] [net-analyzer/munin](https://packages.gentoo.org/packages/net-analyzer/munin) [[]] [Munin Server Monitoring Tool]

  --------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`apache2`](https://packages.gentoo.org/useflags/apache2)       Add Apache2 support
  [`asterisk`](https://packages.gentoo.org/useflags/asterisk)     Install the packages required for monitoring Asterisk. Disabling the flag does not remove any plugin files.
  [`cgi`](https://packages.gentoo.org/useflags/cgi)               Install the CGI-compatible scripts for on-the-fly generation of web pages and graphs. This is only meaningful if the minimal USE flag is disabled.
  [`dhcpd`](https://packages.gentoo.org/useflags/dhcpd)           Install dev-perl/Net-IP, dev-perl/HTTP-Date and net-misc/dhcp to monitor DHCP lease usage. This only works if the server is on the same system as the node, so the server is also brought in. Disabling the flag does not remove any plugin file.
  [`doc`](https://packages.gentoo.org/useflags/doc)               Build and install a local copy of the HTML documentation for the whole software. This requires dev-python/sphinx to process the documentation sources.
  [`http`](https://packages.gentoo.org/useflags/http)             Install dev-perl/libwww-perl required for monitoring HTTP-based services such as Apache and nginx. Disabling the flag does not remove any plugin file.
  [`ipmi`](https://packages.gentoo.org/useflags/ipmi)             Install sys-apps/ipmitool required for monitoring IPMI sensors. Disabling the flag does not remove any plugin file.
  [`ipv6`](https://packages.gentoo.org/useflags/ipv6)             Add support for IPv6 in munin-node. IPv6 support for the master is always enabled, but the node requires a newer version of dev-perl/Net-Server, capable of listening to IPv6 sockets.
  [`irc`](https://packages.gentoo.org/useflags/irc)               Install the packages required for monitoring IRC. Disabling the flag does not remove any plugin files.
  [`java`](https://packages.gentoo.org/useflags/java)             Build the Java-based plugins to monitor JMX-compatible applications. Disabling the flag removes the jmx monitoring plugins.
  [`ldap`](https://packages.gentoo.org/useflags/ldap)             Add LDAP support (Lightweight Directory Access Protocol)
  [`memcached`](https://packages.gentoo.org/useflags/memcached)   Install the packages required for memcached monitoring. Disabling the flag does not remove any plugin files.
  [`minimal`](https://packages.gentoo.org/useflags/minimal)       Only install munin-node and its plugins. This excludes the scripts to generate the web pages and the graphs.
  [`mysql`](https://packages.gentoo.org/useflags/mysql)           Install the packages required for monitoring MySQL. Disabling the flag does not remove any plugin files.
  [`postgres`](https://packages.gentoo.org/useflags/postgres)     Install the packages required for monitoring PostgreSQL. Disabling the flag does not remove any plugin files.
  [`selinux`](https://packages.gentoo.org/useflags/selinux)       !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`ssl`](https://packages.gentoo.org/useflags/ssl)               Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  [`syslog`](https://packages.gentoo.org/useflags/syslog)         Configure the node by default to log on syslog. This requires the presence of virtual/perl-Sys-Syslog. As of version 2.0.2, the master scripts only log to file, and not to syslog.
  [`test`](https://packages.gentoo.org/useflags/test)             Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  --------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-26 17:08] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

## [Installation and setup]

The installation of Munin is easy enough, as it only requires to install the one package [[[net-analyzer/munin]](https://packages.gentoo.org/packages/net-analyzer/munin)[]], and contains no extra plugins or anything, by default.

`root `[`#`]`emerge --ask munin`

But since Munin is fundamentally made of two components -- the *node* and the *master* -- you should first decide which of the two configurations you want to set up for any given box.

Note: some of the configuration coming up is going to use the [sudo] command. This is required because by default the plugins and the master scripts are executed as the munin user. If you prefer you can easily perform the actions using [su] instead.

### [][Node (client)]

Munin nodes have the task of reporting the results of a series of scripts (called plugins), which report data in a structured format so that the master can log the values and generate a report. Usually you set up one node for each box you intend to monitor, including the master.

To set up a simple node, which only has to gather data and does not have to produce the reports, you\'re recommended to enable the `minimal` USE flag --- by doing so, you\'re avoiding a number of extra dependencies that only involve the master, namely [[[net-analyzer/rrdtool]](https://packages.gentoo.org/packages/net-analyzer/rrdtool)[]]. Disabling `minimal` it\'s also necessary to disable `cgi` which is a default starting from version 2.0.2.

[FILE] **`/etc/portage/package.use`**

    net-analyzer/munin minimal -cgi

The nodes shouldn\'t in general need any particular configuration specific to Gentoo, so you can follow the upstream manual just fine. In general you can use the [munin-node-configure] command to enable all the plugins that can be used on a system; this is not recommended though, simply because some of the data might not be of interest and would simply add load to the system when executed.

You can use the following command to identify which plugins would be enabled:

`root `[`#`]`sudo -u munin munin-node-configure --shell`

**Some of the plugins that are installed might not be functional due to missing dependencies; check [the USE flags description](https://wiki.gentoo.org/wiki/Munin#USE_flags "Munin") for further information.**

If the selection sounds correct, you can execute the script by using the following command, or simply manually link the plugins you\'re interested in.

`root `[`#`]`sudo -u munin munin-node-configure --shell | /bin/bash`

Finally you have to start up the service and set it for automatic start.

`root `[`#`]`/etc/init.d/munin-node start `

`root `[`#`]`rc-update add munin-node default `

### [Master]

The Munin master has the task of fetching the values reported by the nodes and producing a report, composed of HTML pages and PNG graphs. This can be done either within the cron job (so that the pages are generated statically) or via the CGI scripts that come installed by default. In either case you\'re likely going to need a [web server](https://wiki.gentoo.org/wiki/Category:Web_servers "Category:Web servers") to display the reports.

When setting up a Munin master you have to make sure the `minimal` USE flag is not enabled.

[FILE] **`/etc/portage/package.use`**

    net-analyzer/munin -minimal

Starting from version 2, it\'s possible to have both the HTML pages and the graph images generated by CGI scripts. While this was for a while enabled by default upstream, at the moment, this is disabled. Starting from ebuild 2.0.7-r6, the support for CGI in the ebuild is nigh-complete.

#### [cron configuration]

The Munin master needs to executed periodically a script that gathers the data from the configured nodes; this can be set up in cron by simply using the following command:

`root `[`#`]`emerge --config net-analyzer/munin`

This will set up a cron job for the `munin` user to execute every five minutes. It is designed to work with vixie-cron, [dcron](https://wiki.gentoo.org/index.php?title=Dcron&action=edit&redlink=1 "Dcron (page does not exist)") and [fcron](https://wiki.gentoo.org/index.php?title=Fcron&action=edit&redlink=1 "Fcron (page does not exist)") (as of version 2.0.3). The user should already be listed in the `cron` group required to use the service.

#### [Generating reports through cron]

If you want to generate the reports statically, you might want to disable the `cgi` USE flag. Please note that disabling the cgi USE flag will also stop you from zooming into graph.

[FILE] **`/etc/portage/package.use`**

    net-analyzer/munin -minimal -cgi

The default configuration will put the generated files in [/var/www/localhost/htdocs/munin] which makes it work out of the box with Apache2 and lighttpd as [http://localhost/munin/](http://localhost/munin/) --- but this might not be suitable or desirable for your setup. If you want to change the path where the files are placed, either to change it to a different virtual host or to a different path, you just have to edit [/etc/munin/munin.conf]:

[FILE] **`/etc/munin/munin.conf`**

    graph_strategy cron
    html_strategy cron

    # we want to use http://localhost/monitor/ to access the report
    htmldir /var/www/localhost/htdocs/monitor

#### [Generating report through CGI]

For generating the graphs, and/or the HTML pages, through CGI, you need to make sure the `cgi` USE flag is enabled, and if you use Apache, you need to enable `apache` USE flag as well.

[FILE] **`/etc/portage/package.use`**

    net-analyzer/munin -minimal cgi # apache

By default, the ebuild will assume that if you want to use Apache, the `apache` user will be the one executing the CGI, but if you don\'t enable it, it\'ll default to `munin`. Make sure that however you set up your CGI setting, it uses the correct user.

Please note that for CGI to work, the user executing the scripts need to have access to [/var/log/munin/munin-cgi-graph.log] and [/var/cache/munin-cgi/].

##### [Graph-only CGI]

[FILE] **`/etc/munin/munin.conf`**

    cgitmpdir /var/cache/munin-cgi/
    cgiurl_graph /munin-cgi/munin-cgi-graph
    graph_strategy cgi
    html_strategy cron

    htmldir /var/www/localhost/htdocs/munin

[FILE] **`/etc/apache2/vhosts.d/default_vhost.include`**

    Include /etc/apache2/vhosts.d/munin.include

##### [Full CGI]

[FILE] **`/etc/munin/munin.conf`**

    cgitmpdir /var/cache/munin-cgi/
    cgiurl_graph /munin-cgi/munin-cgi-graph
    graph_strategy cgi
    html_strategy cgi

    htmldir /var/www/localhost/htdocs/munin

[FILE] **`/etc/conf.d/apache2`**

    APACHE2_OPTS="-D DEFAULT_VHOST -D INFO -D MUNIN_HTML_CGI"

[FILE] **`/etc/apache2/vhosts.d/default_vhost.include`**

    Include /etc/apache2/vhosts.d/munin.include

##### [Static reports with CGI zoom]

[FILE] **`/etc/munin/munin.conf`**

    cgitmpdir /var/cache/munin-cgi/
    cgiurl_graph /munin-cgi/munin-cgi-graph
    graph_strategy cron
    html_strategy cron

    htmldir /var/www/localhost/htdocs/munin

[FILE] **`/etc/apache2/vhosts.d/default_vhost.include`**

    Include /etc/apache2/vhosts.d/munin.include

[FILE] **`/etc/apache2/vhosts.d/munin.include`**

    # -*- apache -*-

    &lt;IfDefine MUNIN_HTML_CGI&gt;
    RewriteEngine on

    RewriteRule ^/favicon.ico /static/favicon.ico [L]

    RewriteCond % (/|\.html)$
    RewriteCond % !/static
    RewriteRule ^/(.*) /munin-cgi/munin-cgi-html/$1 [PT,L]
    RewriteRule ^/munin-cgi/munin-cgi-graph/(.*) /$1
    RewriteCond % !^/static
    RewriteRule ^/(.*.png) /munin-cgi/munin-cgi-graph/$1? [L,PT]

    ScriptAlias /munin-cgi/munin-cgi-graph /usr/libexec/munin/cgi/munin-cgi-graph
    ScriptAlias /munin-cgi/munin-cgi-html /usr/libexec/munin/cgi/munin-cgi-html
    &lt;/IfDefine&gt;

    Alias /static /etc/munin/static
    &lt;Directory /etc/munin/static&gt;
            Require all granted
    &lt;/Directory&gt;

    &lt;Directory /usr/libexec/munin/cgi/&gt;
            Options +ExecCGI
            Require all granted

            &lt;IfModule mod_fcgid.c&gt;
                    SetHandler fcgid-script
            &lt;/IfModule&gt;
            &lt;IfModule !mod_fcgid.c&gt;
                    SetHandler cgi-script
            &lt;/IfModule&gt;
    &lt;/Directory&gt;

##### [Update permissions]

`root `[`#`]`find /var/www/localhost/htdocs/munin -type d | xargs setfacl -m d:g:apache:rwx,g:apache:rwx - `

### [SSH Transport and Munin Async]

** Note**\
This section discuss Munin async as it\'s implemented from version 2.0.7-r5 onward. Anything before that is completely messed up and is not worth trying.

Starting from version 2, Munin supports a direct implementation of SSH transport, which allows to gather data from remote nodes that only allow SSH access through the firewall. Using this method allows for people to authenticate all requests.

This is implemented by generating SSH keypairs for the `munin` user on the master, and accepting them on the nodes for a compatible user. Since the `munin` user should not be allowed to log-in, as this can induce security issues, it\'s important to choose a different user to connect to, such as `scponly`. The Munin ebuild is providing an adequate user in form of `munin-async` which is also usable for the asynchronous node access.

The public keys to use for allowing access to Munin are generated by `emerge --config net-analyzer/munin` and are stored as [/var/lib/munin/.ssh/id_rsa.pub] and [/var/lib/munin/.ssh/id_ecdsa.pub]. You\'re suggested to use the latter if your SSH supports it. To use the `munin-async` user, you should copy one or both of them in [/var/spool/munin-async/.ssh/authorized_keys].

After Munin gets access to the box you have to provide a way for it to contact the Munin node; Munin expects the standard input/output streams of the SSH process to connect straight into the node itself, so the upstream-suggested command to provide is `/usr/bin/nc localhost 4949`. If you have a recent enough OpenSSH, though, there is a simpler way by using the `-W` option, by leaving the command section empty:

[FILE] **`/etc/munin/munin.conf`**

    [node.example.com]
    address ssh://munin-async@node.example.com/ -W localhost:4949

This will automatically forward input and output to the given address pair without having to execute any other command on the server side. It\'s quite useful if you have one SSH-able gateway and a number of nodes that are available behind it.

Alternatively it\'s possible to use the Asynchronous Node. This requires enabling the `munin-async` service on the node itself, so that it fetches and stores locally the plugins\' output, and then sends them to the master when it starts up. For a more thorough description of the Asynchronous Node, please see [this post by Flameeyes](https://flameeyes.blog/2012/10/21/asynchronous-munin/) until more proper documentation is available.

To use the asynchronous node, you just need to provide a slightly different command to the SSH protocol for munin:

[FILE] **`/etc/munin/munin.conf`**

    [node.example.com]
    address ssh://munin-async@node.example.com/usr/libexec/munin/munin-async --spoolfetch

The `--spoolfetch` option provides a batch of updates to the master since last time it connected to that particular node, and helps avoiding blank spaces in the graph itself caused by network congestions.

It\'s also possible to access an Async node running locally without using SSH, this is achieved by using the **cmd://** protocol:

[FILE] **`/etc/munin/munin.conf`**

    [node.example.com]
    address cmd:///usr/libexec/munin/munin-async --spoolfetch

Please note that there are *three* slashes after the protocol definition, because the hostname has to be kept emtpy.

## [Integration with Nagios or Icinga]

While Munin already provides some degree of warning notification when the nodes\' data reaches given thresholds, it doesn\'t even come near the flexibility of dedicated software such as [Nagios](https://wiki.gentoo.org/wiki/Nagios "Nagios") or Icinga. Luckily, instead of having to set up the tests twice to provide the data to the two of them, it\'s possible to make the Munin master forward the problem statuses to Nagios or Icinga through the NSCA software available in [[[net-analyzer/nsca]](https://packages.gentoo.org/packages/net-analyzer/nsca)[]].

The *nsca* package needs to be installed on both the Munin master, which will send the data for the passive check, and on the Nagios host (which will receive it). If they are both on the same system, that simplifies it just a little. For split systems, it\'s possible to enable the `minimal` USE flag for [[[net-analyzer/nsca]](https://packages.gentoo.org/packages/net-analyzer/nsca)[]] on Munin master, to only get the [send_nsca] command.

### [][Nagios/Icinga host side]

Make sure that *nsca* is installed in full:

[FILE] **`/etc/portage/package.use`**

    net-analyzer/nsca -minimal

The package will install configuration files for both Nagios and Icinga, with the default users and paths as the two packages install by default. To select one or the other, you have to change [/etc/conf.d/nsca]. The default configurations should be fine for everybody, with the exception at most of the server address.

[FILE] **`/etc/conf.d/nsca`**

    CFGFILE=/etc/icinga/nsca.cfg
    # CFGFILE=/etc/nagios/nsca.cfg

On the Nagios/Icinga side itself, your configuration will depend on the title of the graph that Munin exports; for instance if you\'re receiving a warning from the **df** plugin, you should pick up as title *Disk usage in percent*. (There were some titles that are not valid check names for Nagios, but as of [[[net-analyzer/munin-2.0.7-r5]](https://packages.gentoo.org/packages/net-analyzer/munin-2.0.7-r5)[]] all the default plugins\' titles are cleaned up.) Then you need to create a passive service check for it in your configuration, similar to this:

[CODE]

    define service

    define service

(This is a template-based service, which makes it very simple to add further service checks using Munin\'s alerts.)

## [Gentoo Linux exclusives]

There are a few things in Munin that are only available with the Gentoo Linux ebuilds, either because they fit better our design or because upstream is not ready (yet) for them.

In particular as of August 2012, the IPMI plugin shipping with Munin 2.0 and later is not the official one shipped by upstream, but a new one, developed by [Flameeyes](https://wiki.gentoo.org/wiki/User:Flameeyes "User:Flameeyes") and based off FreeIPMI. The reason of this change is that the previous plugin, using ipmitool, would time out on most HP and SuperMicro servers when fetching sensors\' data.

The new plugin is not available in the official Munin package because it requires a fairly recent FreeIPMI version (much newer than the latest available for Debian and Fedora) even to get near the feature list of the original plugin, while it requires an unreleased, or patched, version to surpass the original plugin. In Portage this is mandated by depending on version 1.1.6-r1 or later (which has been patched to support outputting thresholds, otherwise available only on 1.2.x series).

This IPMI plugin is also able to monitor foreign hosts, and is backward compatible with both **ipmi\_** and **ipmi_sensor\_**. Finally, it does not require the use of **gawk** but works with any POSIX-compatible awk implementation.

## [Troubleshooting]

The most common problem is graphs are not generated. Check for problems by executing `/usr/bin/munin-cron`

`root `[`#`]`sudo -u munin /usr/bin/munin-cron`

Common errors include not restarting `munin-node` after adding plugins.

## [See Also]

-   [Collectd-web](https://wiki.gentoo.org/wiki/Collectd-web "Collectd-web") --- a web-based Perl CGI front-end for RRD data collected by [collectd](https://wiki.gentoo.org/wiki/Collectd "Collectd").
-   [Munin maintenance](https://wiki.gentoo.org/wiki/Munin_maintenance "Munin maintenance") --- **for package maintainers**, to describe the maintenance tasks to consider when working on [Munin].

## [External resources]

-   [Missing graphs](http://munin-monitoring.org/wiki/FAQ_no_graphs)
-   [Flameeyes\'s Munin-related posts](https://flameeyes.blog/tag/munin/)
-   [Official Munin Documentation](https://munin.readthedocs.org)