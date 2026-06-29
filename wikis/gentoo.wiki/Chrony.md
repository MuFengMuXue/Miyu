This page contains [[changes](https://wiki.gentoo.org/index.php?title=Chrony&oldid=1424760&diff=1429462)] which are not marked for translation.

Other languages:

-   [English]
-   [日本語](https://wiki.gentoo.org/wiki/Chrony/ja "Chrony (100% translated)")

**Resources**

[[]][Home](https://chrony.tuxfamily.org/)

[[]][Package information](https://packages.gentoo.org/packages/net-misc/chrony)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Chrony "wikipedia:Chrony")

*Not to be confused with [cronie](https://wiki.gentoo.org/wiki/Cron#cronie "Cron").*

**chrony** is a versatile implementation of the [Network Time Protocol](https://wiki.gentoo.org/wiki/Network_Time_Protocol "Network Time Protocol") (NTP). It can synchronize the [system clock](https://wiki.gentoo.org/wiki/System_time "System time") with NTP servers, reference clocks (e.g. GPS receiver), and manual input using wristwatch and keyboard. It can also operate as an NTPv4 (RFC 5905) server and peer to provide a time service to other computers in the network.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Enable Network Time Security (NTS)]](#Enable_Network_Time_Security_.28NTS.29)
    -   [[2.3] [Use UTC time]](#Use_UTC_time)
    -   [[2.4] [Acting as a local NTP server]](#Acting_as_a_local_NTP_server)
    -   [[2.5] [DHCP]](#DHCP)
        -   [[2.5.1] [netifrc]](#netifrc)
-   [[3] [Advanced Configuration]](#Advanced_Configuration)
    -   [[3.1] [Hardware Timestamping and PTP Integration]](#Hardware_Timestamping_and_PTP_Integration)
        -   [[3.1.1] [Kernel support]](#Kernel_support)
        -   [[3.1.2] [Configuration with hardware timestamping]](#Configuration_with_hardware_timestamping)
-   [[4] [Usage]](#Usage)
    -   [[4.1] [chronyc Client Interface Tool]](#chronyc_Client_Interface_Tool)
    -   [[4.2] [chronyd service]](#chronyd_service)
        -   [[4.2.1] [OpenRC]](#OpenRC)
        -   [[4.2.2] [systemd]](#systemd)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [net-misc/chrony](https://packages.gentoo.org/packages/net-misc/chrony) [[]] [NTP client and server programs]

  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`+caps`](https://packages.gentoo.org/useflags/+caps)               Use Linux capabilities library to control privilege
  [`+cmdmon`](https://packages.gentoo.org/useflags/+cmdmon)           Support for command and monitoring
  [`+nettle`](https://packages.gentoo.org/useflags/+nettle)           Use dev-libs/nettle for hash functions or nts
  [`+nts`](https://packages.gentoo.org/useflags/+nts)                 Support for Network Time Security (NTS). Uses net-libs/gnutls
  [`+phc`](https://packages.gentoo.org/useflags/+phc)                 Support for the PTP (Precision Time Protocol) Hardware Clock (PHC) interface
  [`+readline`](https://packages.gentoo.org/useflags/+readline)       Enable support for libreadline, a GNU line-editing library that almost everyone wants
  [`+refclock`](https://packages.gentoo.org/useflags/+refclock)       Support for reference clocks
  [`+rtc`](https://packages.gentoo.org/useflags/+rtc)                 Support for the Linux Real Time Clock interface
  [`+seccomp`](https://packages.gentoo.org/useflags/+seccomp)         Enable seccomp (secure computing mode) to perform system call filtering at runtime to increase security of programs
  [`+sechash`](https://packages.gentoo.org/useflags/+sechash)         Enable support for hashes other than MD5
  [`debug`](https://packages.gentoo.org/useflags/debug)               Get DEBUG_LOG output from chronyd when passing -dd parameter
  [`html`](https://packages.gentoo.org/useflags/html)                 Install HTML documentation
  [`libtomcrypt`](https://packages.gentoo.org/useflags/libtomcrypt)   Support different hashes via dev-libs/libtomcrypt
  [`nss`](https://packages.gentoo.org/useflags/nss)                   Use dev-libs/nss for hash functions
  [`pps`](https://packages.gentoo.org/useflags/pps)                   Support for the Linux Pulse Per Second (PPS) interface
  [`samba`](https://packages.gentoo.org/useflags/samba)               Add support for SAMBA (Windows File and Printer sharing)
  [`selinux`](https://packages.gentoo.org/useflags/selinux)           !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)     Verify upstream signatures on distfiles
  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-03 17:17] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install the chrony package:

`root `[`#`]`emerge --ask net-misc/chrony`

## [Configuration]

### [Files]

Chrony maintains following important files:

-   [/etc/chrony/chrony.conf] - Main configuration file
-   [/var/lib/chrony/drift] - Stores the system clock drift rate learned over time
-   [/var/lib/chrony/rtc] - Real-time clock correction data (if rtcsync enabled)
-   [/var/run/chronyd.pid] - Process ID file
-   [/var/log/chrony/] - Log directory (if logging enabled)

The drift file contains two values: the drift rate in parts per million and the estimated error. This file should be preserved across system updates to maintain timing accuracy.

[/etc/chrony/chrony.conf] is the configuration file for [chronyd]. The default configuration is populated with:

[FILE] **`/etc/chrony/chrony.conf`**

    # Use public NTP servers from the pool.ntp.org project.
    server 0.gentoo.pool.ntp.org iburst
    server 1.gentoo.pool.ntp.org iburst
    server 2.gentoo.pool.ntp.org iburst
    server 3.gentoo.pool.ntp.org iburst

    # Record the rate at which the system clock gains/losses time.
    driftfile /var/lib/chrony/drift

    # Allow the system clock to be stepped in the first three updates
    # if its offset is larger than 1 second.
    makestep 1.0 3

    # Enable kernel synchronization of the real-time clock (RTC).
    rtcsync

    hwclockfile /etc/adjtime

** Note**\
Time zones and location of the server do not matter for the NTP protocol; it synchronizes via [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time "wikipedia:Coordinated Universal Time").

On systems where a network connection is not always available at boot (laptops, etc.), it might help to change the pool line in the server configuration:

[FILE] **`/etc/chrony/chrony.conf`**

    pool pool.ntp.org iburst auto_offline

This tells chronyd that the machine will be assumed to have gone offline when 2 requests have been sent to it without receiving a response.

Use the [chronyc online] command to re-enable polling (See below)

### [][Enable Network Time Security (NTS)]

NTS provides cryptographic security on NTP client-server connections using Transport Layer Security (TLS) and Authenticated Encryption with Associated Data (AEAD) [RFC8915](https://datatracker.ietf.org/doc/html/rfc8915). In order to use this, set specific servers supporting NTS:

[FILE] **`/etc/chrony/chrony.conf`**

    # List of NTS servers:

    # Anycast Cloudflare servers
    server time.cloudflare.com              iburst nts

    # Servers from System76 located in USA
    server virginia.time.system76.com       iburst nts
    server ohio.time.system76.com           iburst nts
    server oregon.time.system76.com         iburst nts

    # Anycast servers located in Sweden
    server nts.netnod.se                    iburst nts

    # NTS pool located in Netherlands
    server ntppool1.time.nl                 iburst nts
    server ntppool2.time.nl                 iburst nts

    # NTS pool located in Germany
    server ptbtime1.ptb.de                  iburst nts
    server ptbtime2.ptb.de                  iburst nts
    server ptbtime3.ptb.de                  iburst nts

    # NTS cookie jar to minimise NTS-KE requests upon chronyd restart
    ntsdumpdir /var/lib/chrony

** Important**\
Most NTP pools do not support NTS. See [Public NTS server list](https://netfuture.ch/public-nts-server-list/) for available NTS-aware pools.

** Tip**\
NTS uses TCP/4460 while standard NTP uses UDP/123.

### [Use UTC time]

**chronyd** assumes by default that the RTC keeps local time (including any daylight saving changes). To use UTC instead use:

[FILE] **`/etc/chrony/chrony.conf`**

    rtconutc

### [Acting as a local NTP server]

By default, [chronyd] only synchronizes the local machine time. By adding allow and deny rules, it will act as a local NTP source:

[FILE] **`/etc/chrony/chrony.conf`**

    # Note order does not matter for this example, order does matter with 'allow all' or 'deny all'
    # Allow a specific IP
    allow 192.0.2.1
    # Deny the 198.51.100.0/24 subnet (example)
    deny 198.51.100
    # Allow all of the 192.0.2.0 subnet
    allow 192.0.2

### [DHCP]

To avoid DHCP replacing the local NTP config and the DHCP server is configured with NTP destinations (rare in home use), consider the following configuration options:

#### [netifrc]

[FILE] **`/etc/conf.d/net`**

    dhcp="nontp"

## [Advanced Configuration]

### [Hardware Timestamping and PTP Integration]

On a local-area network, [Network Time Protocol](https://wiki.gentoo.org/wiki/Network_Time_Protocol "Network Time Protocol") can achieve time-synchronization accuracy of in the order of 1 millisecond. While more than enough if getting reference time from another, remote NTP server, using it in conjunction with a more precise time source such as a [Precision Time Protocol (PTP)](https://en.wikipedia.org/wiki/Precision_Time_Protocol "wikipedia:Precision Time Protocol") master or a satellite-navigation (e.g. GPS) clock results in a loss of several orders of magnitude of accuracy. One alternative would of course be to use such a time source directly but that is not always possible, for instance due to the cost and complexity of equipping servers with individual GNSS receivers or due to older network infrastructure not handling PTP traffic correctly. Under such circumstances, recent versions of Chrony offer an additional solution in the form of using hardware clocks available on many modern network-interface cards to improve accuracy of NTP itself.

** Tip**\
It is assumed here that PTP time synchronization is already configured on systems which will use it, using e.g. the [ptp4l] daemon from the [[[net-misc/linuxptp]](https://packages.gentoo.org/packages/net-misc/linuxptp)[]] package. Chrony itself does not speak PTP so if the NIC clock is not accurate, it will be marked as a false ticker at best or actually degrade the synchronization accuracy at worst.

#### [Kernel support]

When dealing with hardware clocks, it is necessary to enable support for them in the kernel. As of mid-2020, all the gentoo-sources kernels available in the tree (4.4 and newer) can be built with PTP-clock support (CONFIG_PTP_1588_CLOCK). Note that the terminology is a bit misleading - enabling this only allows access to the NIC clocks, it has nothing to do with PTP time synchronization except that *ptp4l* also needs to have this enabled.

In addition to the PTP-clock support itself, check the configuration options available for the system\'s NIC drivers - for some (e.g. Cadence MACB/GEM, *macb*) hardware timestamping has to be explicitly enabled, for some others (e.g. Intel PRO/1000 PCIe, *e1000e*) there are switches for additional timestamping-related features. Alternatively, when building a kernel for a KVM guest, enable CONFIG_PTP_1588_CLOCK_KVM. Last but not least, set up network PHY device support for the line of adapters if not yet completed.

[KERNEL]

    PTP Clock Support
      PTP Clock Support
      KVM virtual PTP clock
    Network device support
      PHY Device support and infrastructure

After rebooting to the new kernel verify access to the NIC clocks by emerging [[[sys-apps/ethtool]](https://packages.gentoo.org/packages/sys-apps/ethtool)[]] and running [ethtool -T]. Example for an interface with all the required features:

`root `[`#`]`ethtool -T eth2`

    Time stamping parameters for eth2:
    Capabilities:
            hardware-transmit     (SOF_TIMESTAMPING_TX_HARDWARE)
            software-transmit     (SOF_TIMESTAMPING_TX_SOFTWARE)
            hardware-receive      (SOF_TIMESTAMPING_RX_HARDWARE)
            software-receive      (SOF_TIMESTAMPING_RX_SOFTWARE)
            software-system-clock (SOF_TIMESTAMPING_SOFTWARE)
            hardware-raw-clock    (SOF_TIMESTAMPING_RAW_HARDWARE)
    PTP Hardware Clock: 2
    Hardware Transmit Timestamp Modes:
            off                   (HWTSTAMP_TX_OFF)
            on                    (HWTSTAMP_TX_ON)
    Hardware Receive Filter Modes:
            none                  (HWTSTAMP_FILTER_NONE)
            all                   (HWTSTAMP_FILTER_ALL)
        ptpv1-l4-sync         (HWTSTAMP_FILTER_PTP_V1_L4_SYNC)
        ptpv1-l4-delay-req    (HWTSTAMP_FILTER_PTP_V1_L4_DELAY_REQ)
        ptpv2-l4-sync         (HWTSTAMP_FILTER_PTP_V2_L4_SYNC)
        ptpv2-l4-delay-req    (HWTSTAMP_FILTER_PTP_V2_L4_DELAY_REQ)
        ptpv2-l2-sync         (HWTSTAMP_FILTER_PTP_V2_L2_SYNC)
        ptpv2-l2-delay-req    (HWTSTAMP_FILTER_PTP_V2_L2_DELAY_REQ)
        ptpv2-event           (HWTSTAMP_FILTER_PTP_V2_EVENT)
        ptpv2-sync            (HWTSTAMP_FILTER_PTP_V2_SYNC)
        ptpv2-delay-req       (HWTSTAMP_FILTER_PTP_V2_DELAY_REQ)

Confirm that [/dev/ptp2], the device node associated with this interface according to the \"PTP Hardware Clock\" line, exists and has got sane permissions. Note on the receive filter modes: some NICs can only timestamp PTP packets, i.e. have no HWTSTAMP_FILTER_ALL mode. Such interfaces will be of limited use with NTP because chrony will be unable to hardware-timestamp received packets.

If the device doesn\'t have PTP-clock support, the [ethtool] output looks like:

`root `[`#`]`ethtool -T eth0`

    Time stamping parameters for eth0:
    Capabilities:
            software-transmit     (SOF_TIMESTAMPING_TX_SOFTWARE)
            software-receive      (SOF_TIMESTAMPING_RX_SOFTWARE)
            software-system-clock (SOF_TIMESTAMPING_SOFTWARE)
    PTP Hardware Clock: none
    Hardware Transmit Timestamp Modes: none
    Hardware Receive Filter Modes: none

#### [Configuration with hardware timestamping]

For Internet-facing servers with PTP-synchronized NIC clocks:

[FILE] **`/etc/chrony/chrony.conf`Chrony with hardware timestamping**

    # Record the rate at which the system clock gains/loses time.
    driftfile /var/lib/chrony/drift

    # Allow the system clock to be stepped in the first three updates
    # if its offset is larger than 1 second.
    makestep 1.0 3

    # Enable kernel synchronization of the real-time clock (RTC).
    rtcsync

    allow 192.168.1.0/24
    cmdallow 192.168.1.0/24

    # Outside pools are the public ntp.org and the gentoo ntp pool.
    pool pool.ntp.org iburst
    server 0.gentoo.pool.ntp.org iburst
    server 1.gentoo.pool.ntp.org iburst
    server 2.gentoo.pool.ntp.org iburst
    server 3.gentoo.pool.ntp.org iburst

    # Enable interleaved mode for improved accuracy with timestamping
    # Use 1-second polling interval for hardware-timestamped NTP
    peer ntp-peer1.example.com minpoll 0 maxpoll 0 xleave prefer
    peer ntp-peer2.example.com minpoll 0 maxpoll 0 xleave

    # Use PTP-synchronized NIC clock as reference
    # Option 1: with leap second database
    leapsectz right/UTC
    refclock PHC /dev/ptp2 tai

    # Option 2: manual TAI-UTC offset (update as needed)
    #refclock PHC /dev/ptp2 offset -37

    # Option 3: sub-second accuracy only
    #refclock PHC /dev/ptp2 pps

    # Enable hardware timestamping for all interfaces
    hwtimestamp *

    dumpdir /run/chronyd
    dumponexit
    hwclockfile /etc/adjtime

    logdir /var/log/chrony
    log tracking rtc

The [xleave] option enables interleaved mode for improved accuracy. The [hwtimestamp \*] directive enables hardware timestamping on all supported NICs. The [refclock PHC] line uses the hardware clock as an additional reference source.

For local peers without PTP synchronization:

[FILE] **`/etc/chrony/chrony.conf`Local peer configuration**

    # Record the rate at which the system clock gains/loses time.
    driftfile /var/lib/chrony/drift

    # Allow the system clock to be stepped in the first three updates
    # if its offset is larger than 1 second.
    makestep 1.0 3

    # Enable kernel synchronization of the real-time clock (RTC).
    rtcsync

    allow 192.168.1.0/24
    cmdallow 192.168.1.0/24

    # Use Internet-facing peers as preferred sources
    peer server1.example.com minpoll 0 maxpoll 0 prefer
    peer server2.example.com minpoll 0 maxpoll 0 prefer

    # Enable interleaved mode with other local peers
    peer peer1.example.com minpoll 0 maxpoll 0 xleave

    # Enable hardware timestamping for all interfaces
    hwtimestamp *

    dumpdir /run/chronyd
    dumponexit
    hwclockfile /etc/adjtime

    logdir /var/log/chrony
    log tracking rtc

## [Usage]

### [chronyc Client Interface Tool]

[chronyc] is a command-line interface program which can be used to monitor chronyd\'s performance and to change various operating parameters whilst it is running. A full list of commands can be found in the manual, [man 1 chronyc]

Examples:

`root `[`#`]`chronyc offline # Set all sources offline `

`root `[`#`]`chronyc online # Set all sources online `

### [chronyd service]

#### [OpenRC]

Add chronyd to the default runlevel to start it at boot, so time will be synchronized automatically:

`root `[`#`]`rc-update add chronyd default`

To start the chronyd service now:

`root `[`#`]`rc-service chronyd start`

The OpenRC service can be configured via [/etc/conf.d/chronyd]:

[FILE] **`/etc/conf.d/chronyd`**

    # /etc/conf.d/chronyd

    CFGFILE="/etc/chrony/chrony.conf"

    # Configuration dependant options :
    #      -s - Set system time from RTC if rtcfile directive present
    #      -r - Reload sample histories if dumponexit directive present
    #
    # The combination of "-s -r" allows chronyd to perform long term averaging of
    # the gain or loss rate across system reboots and shutdowns.

    ARGS=" -u ntp -F 2"

Common options in [ARGS]:

-   [-u ntp] - Run as the ntp user for security
-   [-F 2] - Enable seccomp system call filtering (level 2)
-   [-s] - Set system time from RTC if rtcfile directive present
-   [-r] - Reload sample histories if dumponexit directive present

To monitor status of the server:

`root `[`#`]`rc-service chronyd status`

#### [systemd]

To run the [chronyd] sync service:

`root `[`#`]`systemctl start chronyd.service`

To have the [chronyd] sync service start at boot:

`root `[`#`]`systemctl enable chronyd.service`

To monitor status of the [chronyd] service:

`root `[`#`]`systemctl status chronyd.service`

## [See also]

-   [Gentoo Handbook: Time synchronization](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Tools#Time_synchronization "Handbook:AMD64/Installation/Tools")
-   [OpenNTPD](https://wiki.gentoo.org/wiki/OpenNTPD "OpenNTPD") --- a lightweight [NTP](https://wiki.gentoo.org/wiki/Network_Time_Protocol "Network Time Protocol") server ported from OpenBSD.
-   [Network Time Protocol](https://wiki.gentoo.org/wiki/Network_Time_Protocol "Network Time Protocol") --- used to synchronize the [system time](https://wiki.gentoo.org/wiki/System_time "System time") with other devices over the network.
-   [System time](https://wiki.gentoo.org/wiki/System_time "System time") --- is used in Unix systems to keep track of time.
-   [Home router](https://wiki.gentoo.org/wiki/Home_router "Home router") --- how to turn an old Gentoo machine into a router for connecting a home network to the Internet.

## [External resources]

-   [https://www.netnod.se/time-and-frequency/network-time-security](https://www.netnod.se/time-and-frequency/network-time-security)