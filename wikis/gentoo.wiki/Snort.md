[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Snort&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.snort.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Snort_(software) "wikipedia:Snort (software)")

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/snort)

\
**Snort** is an intrusion prevention system, network monitor, and alert daemon. Snort is the de facto standard in intrusion detection.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Command line mode]](#Command_line_mode)
    -   [[2.2] [Gentoo daemon mode]](#Gentoo_daemon_mode)
    -   [[2.3] [Snort rules]](#Snort_rules)
    -   [[2.4] [Updating rules (or sustaining snort)]](#Updating_rules_.28or_sustaining_snort.29)
-   [[3] [Analyzing data]](#Analyzing_data)
    -   [[3.1] [Analysis tools]](#Analysis_tools)
    -   [[3.2] [Rule adjustment]](#Rule_adjustment)
    -   [[3.3] [Sensor placement]](#Sensor_placement)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [white_list.rules and black_list.rules file not found]](#white_list.rules_and_black_list.rules_file_not_found)
    -   [[4.2] [FATAL ERROR: Can\'t initialize DAQ afpacket (-1) -]](#FATAL_ERROR:_Can.27t_initialize_DAQ_afpacket_.28-1.29_-)
-   [[5] [Boot services]](#Boot_services)
    -   [[5.1] [OpenRC]](#OpenRC)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

## [Installation]

Start Here: [https://www.snort.org/documents](https://www.snort.org/documents)

Gentoo offers net-analyzer/snort-2.9.17-r1. Once Snort3 is offered, we will move to that. Snort3 rules have more options to apply alert/block actions. [https://blog.snort.org/2020/08/snort-3-2-differences.html](https://blog.snort.org/2020/08/snort-3-2-differences.html)

### [USE flags]

Do some research on the USE flags. They have been stable for a while. The notes on [[[net-analyzer/snort]](https://packages.gentoo.org/packages/net-analyzer/snort)[]] are better than most USE flag notes.

### [USE flags for] [net-analyzer/snort](https://packages.gentoo.org/packages/net-analyzer/snort) [[]] [The de facto standard for intrusion detection/prevention]

  ------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+active-response`](https://packages.gentoo.org/useflags/+active-response)           Enables support for automatically sending TCP resets and ICMP unreachable messages to terminate connections. Used with inline deployments.
  [`+flexresp3`](https://packages.gentoo.org/useflags/+flexresp3)                       Enables support for new flexable response preprocessor for enabling connection tearing for inline deployments. Replaces flexresp and flexresp2.
  [`+gre`](https://packages.gentoo.org/useflags/+gre)                                   Enable support for inspecting and processing Generic Routing Encapsulation (GRE) packet headers. Only needed if you are monitoring GRE tunnels.
  [`+libtirpc`](https://packages.gentoo.org/useflags/+libtirpc)                         Build against net-libs/libtirpc for RPC support
  [`+non-ether-decoders`](https://packages.gentoo.org/useflags/+non-ether-decoders)     Enable decoding of non-ethernet protocols such as TokenRing, FDDI, IPX, etc.
  [`+perfprofiling`](https://packages.gentoo.org/useflags/+perfprofiling)               Enables support for preprocessor and rule performance profiling using the perfmonitor preprocessor.
  [`+ppm`](https://packages.gentoo.org/useflags/+ppm)                                   Enables support for setting per rule or per packet latency limits. Helps protect against introducing network latency with inline deployments.
  [`+react`](https://packages.gentoo.org/useflags/+react)                               Enables support for the react rule keyword. Supports interception, termination, and redirection of HTTP connections.
  [`+threads`](https://packages.gentoo.org/useflags/+threads)                           Add threads support for various packages. Usually pthreads
  [`control-socket`](https://packages.gentoo.org/useflags/control-socket)               Enables Snort\'s control socket.
  [`debug`](https://packages.gentoo.org/useflags/debug)                                 Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`file-inspect`](https://packages.gentoo.org/useflags/file-inspect)                   Enables extended file inspection capabilities.
  [`high-availability`](https://packages.gentoo.org/useflags/high-availability)         Enables high-availability state sharing.
  [`inline-init-failopen`](https://packages.gentoo.org/useflags/inline-init-failopen)   Enables support to allow traffic to pass (fail-open) through inline deployments while snort is starting and not ready to begin inspecting traffic. If this option is not enabled, network traffic will not pass (fail-closed) until snort has fully started and is ready to perform packet inspection.
  [`large-pcap-64bit`](https://packages.gentoo.org/useflags/large-pcap-64bit)           Allows Snort to read pcap files that are larger than 2 GB. ONLY VALID FOR 64bit SYSTEMS!
  [`linux-smp-stats`](https://packages.gentoo.org/useflags/linux-smp-stats)             Enable accurate statistics reporting through /proc on systems with multiple processors.
  [`open-appid`](https://packages.gentoo.org/useflags/open-appid)                       Enable OpenAppID, an open, application-focused detection language and processing module for Snort that enables users to create, share, and implement application detection. Requires dev-lang/luajit.
  [`reload-error-restart`](https://packages.gentoo.org/useflags/reload-error-restart)   Enables support for completely restarting snort if an error is detected during a reload.
  [`selinux`](https://packages.gentoo.org/useflags/selinux)                             !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`shared-rep`](https://packages.gentoo.org/useflags/shared-rep)                       Enables the use of shared memory for the Reputation Preprocessor (Only available on Linux systems)
  [`side-channel`](https://packages.gentoo.org/useflags/side-channel)                   Enables Snort\'s side channel.
  [`sourcefire`](https://packages.gentoo.org/useflags/sourcefire)                       Enables Sourcefire specific build options, which include \--enable-perfprofiling and \--enable-ppm.
  ------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-01-25 06:44] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Like any other package, do:

`root `[`#`]`emerge --ask net-analyzer/snort`

Snort will be masked by the \~amd64 keyword. This is probably best. Hopefully, this document will help you decide to permanently unmask net-analyzer/snort, and start to apply signatures of badness to your network traffic.

Unmasking an \"unstable\" arch package is easy. Knowing what you are getting yourself into is something altogether different. You should probably look upstream ([https://www.snort.org/documents](https://www.snort.org/documents)) first. If you have run snort on other platforms, you are ahead of that game. The big danger is filling the partition collecting your logs. The next biggest danger is ignoring those logs!!! But we digress\...

To unmask snort:

`root `[`#`]`echo 'net-analyzer/snort ~amd64' >> /etc/portage/package.accept_keywords/file`

** Important**\
**Always Append (\>\>) to files in /etc/portage/package\* \*\*\***

This file can be edited using a favorite editor later. Portage will read files in /etc/portage/package.accept_keywords. Having several files reduces the damage done if you clobber a file. Change \"file\" to a name of your choice.

It is also wise to look at USE flags on the [[[net-libs/libpcap]](https://packages.gentoo.org/packages/net-libs/libpcap)[]] and the [[[net-libs/daq]](https://packages.gentoo.org/packages/net-libs/daq)[]] packages.

## [Configuration]

Snort alerts on what it can hear. If your network is not connected to the internet, Snort will only hear traffic of your devices. Generally, IDS sensors are placed on network boundaries. The alerts and drops you log are from that context.

Gentoo does not supply rules! Fear not! The Snort Developers offer their own rules, and a set of community rules. [https://www.snort.org/downloads#rules](https://www.snort.org/downloads#rules) Next to those rules are several guides for writing your own. There is also the Emerging Threat Rule Set. [https://rules.emergingthreatspro.com/open/snort-2.9.0/](https://rules.emergingthreatspro.com/open/snort-2.9.0/) There are also more up to date and propietary rules you can add on your own (read: buy). See the discussion of sustainable updates below.

**[And!]** You can write, and operationalize your own rules - privately if you are so inclined.

### [Command line mode]

Snort will run from the command line, in the foreground. It will ignore the daemon configuration in /etc/conf.d/snort, so you have to tell it which interface to read (eth0?, a file?) You can use this to run an ad hoc IDS, test a config, dump packets, read captured packets, or more. If you want permanent coverage, don\'t do it from the command line!

Examples:

`root `[`#`]`snort -i eth0 -T -c /etc/snort/snort.conf`

    Running in Test mode

            --== Initializing Snort ==--

    [...]

    Snort successfully validated the configuration!

    Snort exiting

There will be A LOT of output between the square brackets. You know what you changed. You will have to find it. The output is sent to standard error. To capture the output to a file you will have to redirect standard error to standard out. To wit:

`root `[`#`]`snort -i eth0 -T -c /etc/snort/snort.conf > conftest 2>&1`

The Ad Hoc IDS can be had by removing the -T. It will dump the same verbose operating parameters to standard error. The Gentoo Devs have put the logs in /var/log/snort. They also capture the alerted packets, FWIW. You can analyze those with tcpdump or wireshark.

`root `[`#`]`snort -i eth0 -b --daq-dir /usr/lib64/daq`

You can even test or capture without rules! Snort tells you how it intialized, but it complains about not having preprocessors configured - once for every packet it logs\... hmmm. Redirection (as above) is useful here too. Add -F \<file\> to point to a file of Berkeley Packet Filter (BPF) macros to fine tune your captures.

### [Gentoo daemon mode]

Now for the Big Machine stuff!!!

Gentoo requires snort users to define the interface being monitored the [/etc/conf.d/snort] configuration file.

Snort ships with an example config that must be copied and edited:

`root `[`#`]`cp /etc/snort/snort.conf.distrib /etc/snort/snort.conf`

**The items at the end of this article tell you how to start Snort as a daemon as Gentoo has shipped it!**

The shipped file is the root of an \"*include*\" tree. That is to say that you can point to a lot of other files to configure snort. Each set of rules has its own snort.conf file. Merging these rule sets into one takes some doing. We will start with the [snortrules-snapshot] from Talos (Cisco nee SourceFire). You have to register to get those rules.

Registration is free. You get the chance to receive any (or none) of four mailing lists. If you are putting snort in production, you want this. Otherwise, you get the community rules.

The shipped snort.conf is heavily documented by the Snort Dev\'s. To start, you should edit ipvar HOME_NET. Change \"any\" to a CIDR notation of your external addresses. If you need an example, see ipvar AIM_SERVERS in the shipped snort.conf. You can list several networks, separated by commas. This is how you tell snort which direction to look.

There are several \"ipvar\" keys right under the HOME_NET key. If you know them, set them. It will reduce the load on your snort process and the number of log entries you have to work.

Going deeper into the config file should only be done as you learn your network, and Snort. The portvar HTTP_PORTS key in the shipped file has far fewer ports than the config that comes with the [snortrules-snapshot]. Before you shave those off, remember that attacks get pointed at browsers, and many other services use the HTTP protocol.

Some snort.conf lines end with a trailing backslash ( \\ ). These are parsed by snort as if they are on one line. Don\'t remove the backslashes!

The diff(1) tool is your friend IF you kept a copy of the original snort.conf.distrib file. Generally, snort -T will point out your problem. The snort.conf.distrib file shows you the default settings.

The Snort Dev\'s have put a lot of effort into making the defaults make sense. They can\'t know every network. Preprocessors have been written to improve performance, and reduce false positives, et al. You may never be done with tweaking snort.conf.

So\... Let\'s load some rules!

### [Snort rules]

The more rules you load into snort, the busier the pig will be! Keep that in mind when provisioning your sensors. There are 32 MB of rules in the [snortrules-snapshot] set. They all get loaded into RAM. But Yes! I want more rules.

There are three categories of rules in the [snortrules-snapshot]. They are standard rules, preproc_rules, and so_rules. The so_rules need to be compiled. Per the doc:

Commonly referred to as "Shared Object rules", "SO rules", "pre-compiled rules", or "Shared Objects" are detection that is written in the Shared Object rule language, which is, essentially, "C". This allows for primarily two things for the Snort platform:

1.  Detection that is not possible under the regular Snort rules language. Since Shared Object rules are "C" based, they can essentially be coded to detect a much greater set of conditions than regular Snort rules can. One of the common misconceptions about Shared Object rules are that they are closed source, and while under certain conditions that may be true, they are not inherently closed source. You can, in fact write your own shared object rules
2.  It allows for obfuscation of exact detection in the rule language. Under certain conditions (Agreements with vendors, use of Shared Object rules in 'classified' environments, Sourcefire 0-day detection, etc) it may be necessary to obfuscate how detection is performed with a particular rule. Since Shared Object rules have to be compiled in order to use them, that's why Talos distributes "pre-compiled" rules.

[https://www.snort.org/faq/shared-object-rules](https://www.snort.org/faq/shared-object-rules)

But the rules I downloaded today had no binary precompiled rules in them. The \"official solution\" is subscribe (Read: Buy)!

There is an etc directory in the package. These files will conflict with the files in the distribution. You can do

`root `[`#`]`diff -W 125 -y  /etc/snort/<shipped file> | less`

To compare the files and make your decisions. The only advice I have is to stick with Gentoo\'s shipped unicode.map file, and carefully merge the snort.conf files.

The above command will show that Gentoo has shaved **portvar HTTP_PORTS**, provided a **daq** config, worked **preprocessor stream5_tcp**, and tweaked a couple other things. The Snort Package has 121 lines of include. You probably dont need them all. You decide!

From here, shut down the snort daemon if you have started it. Use snort to check your config (above). Restart the snort daemon, and watch /var/log/snort/alert!

Pulled Pork is not shipped by Gentoo. OinkMaster throws an error on the URL provided by Snort.org (https support, I believe).

### [][Updating rules (or sustaining snort)]

Is outside of Gentoo!

Events in the security realm are high impact and fast moving. Going through the above process is slow and tedious. PulledPork(.pl: PERL) works. Just run it, and it will keep you in the community and emerging-threat rules reality zone. You will get an \"OinkCode\" when you register. PulledPork uses that in its config. It also facilitates the paid rules at snort.org. All the better!

Several Snort support tools claim to update rules. OK, great! Describe them here if you have them working.

The bottom line is that you should automate updating rules on a regular periodic basis. Emerging Threats puts out an update every week day. Snort.Org updates their rules weekly, or more often, driven by events. Keeping up with the changes helps point where attackers are going, today, this week, this month.

You should create a Cron Job to update your rules. Yes, that means you have check the change log every day or two. Just Do It. Its good for you and your company.

## [Analyzing data]

OK! So you have text filling up /var/log/snort/alert! It looks a lot like this:

\[\*\*\] \[129:12:1\] Consecutive TCP small segments exceeding threshold \[\*\*\]\
\[Classification: Potentially Bad Traffic\] \[Priority: 2\]\
07/11-23:41:43.911676 My.Net.Here.99:59074 -\> My.Net\>Here.51:22\
TCP TTL:64 TOS:0x48 ID:34979 IpLen:20 DgmLen:88 DF\
\*\*\*AP\*\*\* Seq: 0x60D23E91  Ack: 0x4687D126  Win: 0x1F5  TcpLen: 32\
TCP Options (3) =\> NOP NOP TS: 1718788634 2054611035\

And there are a bunch of them. Some are six lines, some are five, and some have hexadecimal blobs. How do you even count them? This one looks like its totally internal, and going to an SSH server - that you set up - that you were logged into - working! \... Yeah, its a false positive. Remember context?

This format is not conducive to analysis. We need\... something! The community came through in spades. We have lots of options! Within Gentoo? Well, not completely!

### [Analysis tools]

Sguil is a TCL GUI tool. With the \"perfmonitor\" preprocessor, it will show you the status of your snort daemon. Sguil also has a SQL query builder, and lets you edit that SQL after the results are shown. You can also send gpg signed reports by email.

Sguil has built in DNS and WHOIS. There are check boxes to disable them. You may have OPSEC issues to avoid these queries. The WHOIS operators are known to block heavy query sources. There are plenty of places on the web to get those queries answered. You choose!

The Sguil-client is in portage, but the Sguil server and sensor agent are needed to feed the interface. You\'ll need BarnYard, or BarnYard2, or something else to shovel your snort alerts to Sguil. You point your middleware at the Sguil Sensor, which forwards it to the Sguil Server. If you go upstream to get them, the version bump there means you have to overlay the new version. Its TCL, which calls the TCLsh interpreter. That means no compiling.

BarnYard2 gets pointed at the Sguil sensor agent (port 7735, or your choice). It has an issue with backticks on MariaDB (and I assume MySQL) that has lingered for some time. I have not tried PostGreSQL. A patch for BarnYard2 has been submitted. Not that you have to point BarnYard2 at a database. You can just point it at the Sguil sensor agent.

Gentoo has a LAMP platform that will support ADODB and Base ([https://sourceforge.net/projects/secureideas/](https://sourceforge.net/projects/secureideas/)), but only ADODB is available in Portage. Base is smooth, and clean. It has a single line search function. It was in portage, but as a LAMP application, all you have to do is add ADODB, dump the code into a place Apache (?) can work it, and go to town! SSL (TLS?) is Apaches Job. This seems like the cleanest solution - if you want to run a webserver to analyze your snort logs. That may be the right answer in a permanent infrastructure installation.

The modern method of analysis involves Security Information Enterprise Management (SIEM) tools. These tools run mostly on RESTful platforms, using Java, json, node-js, etc. They ARE pretty! Gentoo offers ElasticSearch (The ELK stack). You can download and run Splunk on one machine. These are great tools, with robust version and access control built in. The important thing is to collect packets, and apply signatures to them. SIEM\'s just offer the environment.

[![Sguil Application on Gentoo](/images/thumb/6/6a/Sguil.png/300px-Sguil.png)](https://wiki.gentoo.org/wiki/File:Sguil.png)

[](https://wiki.gentoo.org/wiki/File:Sguil.png "Enlarge")

Populated Sguil fed by Snort running on Gentoo

### [Rule adjustment]

And don\'t forget adjusting your rule set. Snort has a file called threshold.conf that can limit reports. That file has a lot of instructions. Using this file will expose a bit about rules. There are many \"generators\" within snort (GIDs). They are listed in [gen-msg.map] in [/etc/snort]. The SIDs are in [sid-msg.map].

From [threshold.conf]:\
\# Threshold commands are formatted as:\
\#\
\# event_filter gen_id gen-id, sig_id sig-id, \\\
\# type limit\|threshold\|both, track by_src\|by_dst, \\\
\# count n , seconds m

\
You can \"threshold\" entire ranges of rules. The comma is the delimiter!

You can also eliminate entire classes of signatures in the [snortrules-snapshot] rules from snort.org (that you have to register for :( ), by removing their include in snort.conf. With any rule set, you can \"comment out\" (put a \# at the start of the line) for any troublesome rule. This is your response to false positives. The signature mailing lists were formed to receive false positive reports. YMMV.

Snort also accepts BPF macro filters in a file to adjust what it hears with a bit more resolution. You can also set network ACLs if the event indicates such a measure. The more answers you can build in, the less noise you and your tools will have to go through.

### [Sensor placement]

In the modern age of VLANS, switches, QoS, and other networking technologies, where your sensor is listening is as important as its settings. We talked about context above. You wont have time to ask each individual if \"this was you\" - if you can identify them. Carefully consider which borders your IDS is placed on. You can place as many Snort sensors as you have hardware to support. Data Mining techniques within Sguil, or Base, or Bash and Awk, can support dozens or hundreds, if your Foo is good. The considerations are often more people and authority oriented than not. Engage your stakeholders. Be a part of the team.

## [Troubleshooting]

### [white_list.rules and black_list.rules file not found]

PROBLEM: Unable to open address file /etc/snort/white_list.rules or /etc/snort/black_list.rules, Error: No such file or directory

SOLUTION: create those 2 files in /etc/snort/ or /etc/snort/rules/ directory and change the location appropriately in /etc/snort/snort.conf

### [][FATAL ERROR: Can\'t initialize DAQ afpacket (-1) -]

PROBLEM: Snort daemon fails to load with the error \'FATAL ERROR: Can\'t initialize DAQ afpacket (-1) -\'

SOLUTION: Install the package net-libs/libnetfilter_queue and enable the kernel option CONFIG_NETFILTER_NETLINK_QUEUE, after that in snort.conf change the option config daq: afpacket too config daq: pcap

## [Boot services]

#### [OpenRC]

To start snort at boot:

`root `[`#`]`rc-update add snort default`

To start snort immediately:

`root `[`#`]`rc-service snort start`

## [See also]

-   [Wireshark](https://wiki.gentoo.org/wiki/Wireshark "Wireshark") --- a free and open-source packet analyzer.
-   [tcpdump](https://wiki.gentoo.org/wiki/Tcpdump "Tcpdump") --- a command-line network monitoring and data acquisition tool.
-   [postgresql](https://wiki.gentoo.org/wiki/Postgresql "Postgresql") --- a free and open source relational database management system (RDBMS).
-   [apache2](https://wiki.gentoo.org/wiki/Apache2 "Apache2") --- an efficient, extensible [web server](https://wiki.gentoo.org/wiki/Category:Web_servers "Category:Web servers"). It is one of the most popular web servers used the Internet.
-   [MySQL](https://wiki.gentoo.org/wiki/MySQL "MySQL") --- a popular, free software relational database management system. / [MariaDB](https://wiki.gentoo.org/wiki/MariaDB "MariaDB") --- is an enhanced, drop-in [MySQL](https://wiki.gentoo.org/wiki/MySQL "MySQL") replacement.

## [External resources]

-   [https://www.snort.org/documents](https://www.snort.org/documents)
-   [https://wiki.archlinux.org/index.php/Snort](https://wiki.archlinux.org/index.php/Snort)
-   [http://oinkmaster.sourceforge.net/](http://oinkmaster.sourceforge.net/)