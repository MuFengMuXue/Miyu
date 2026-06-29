## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [Chrony with hardware timestamping]](#Chrony_with_hardware_timestamping)
    -   [[2.1] [Host list]](#Host_list)
    -   [[2.2] [Kernel support]](#Kernel_support)
    -   [[2.3] [Chrony config on the Internet-facing, PTP-synchronized servers]](#Chrony_config_on_the_Internet-facing.2C_PTP-synchronized_servers)
    -   [[2.4] [Chrony config on a local peer]](#Chrony_config_on_a_local_peer)
    -   [[2.5] [chrony with hardware timestamping in action]](#chrony_with_hardware_timestamping_in_action)

## [Introduction]

On a local-area network, [Network Time Protocol](https://wiki.gentoo.org/wiki/NTP "NTP") can achieve time-synchronization accuracy of in the order of 1 millisecond. While more than enough if getting reference time from another, remote NTP server, using it in conjunction with a more precise time source such as a [Precision Time Protocol (PTP) (wikipedia)](https://en.wikipedia.org/wiki/Precision_Time_Protocol "wikipedia:Precision Time Protocol") master or a satellite-navigation (e.g. GPS) clock results in a loss of several orders of magnitude of accuracy. One alternative would of course be to use such a time source directly but that is not always possible, for instance due to the cost and complexity of equipping servers with individual GNSS receivers or due to older network infrastructure not handling PTP traffic correctly. Under such circumstances, recent versions of Chrony offer an additional solution in the form of using hardware clocks available on many modern network-interface cards to improve accuracy of NTP itself.

## [Chrony with hardware timestamping]

** Warning**\
It is assumed here that PTP time synchronization is already configured on systems which will use it, using e.g. the [ptp4l] daemon from the [[[net-misc/linuxptp]](https://packages.gentoo.org/packages/net-misc/linuxptp)[]] package. Chrony itself does not speak PTP so if the NIC clock is not accurate, it will be marked as a false ticker at best or actually degrade the synchronization accuracy at worst.

### [Host list]

This guide uses an example network that has several NTP peers:

-   parry, topshelf - Internet-facing servers whose NIC clocks are synchronized with a PTP master over a dedicated network link, running chrony. All of their Ethernet devices can support hardware timestamping
-   mater, mike - internal servers with NICs supporting hardware timestamping, running chrony
-   thufir - internal embedded server running a different implementation of NTP which does not support timestamping

as well as an unnamed PTP master whose configuration is beyond the scope of this guide.

### [Kernel support]

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

### [][Chrony config on the Internet-facing, PTP-synchronized servers]

topshelf and parry have multiple network adapters and are directly connected to the Internet, with firewalls keeping out the unwashed masses. Their chrony config will differ from the other hosts because they will talk to upstream ntp.org and gentoo.org ntp servers at a higher stratum, and also because they will use their respective PTP-synchronized NIC clocks as reference time sources. The local home network is the private 192.168.1.0 class C subnet.

[FILE] **`/etc/chrony/chrony.conf`Customized chrony config file for topshelf**

    # Record the rate at which the system clock gains/loses time.
    driftfile /var/lib/chrony/drift

    # Allow the system clock to be stepped in the first three updates
    # if its offset is larger than 1 second.
    makestep 1.0 3

    # Enable kernel synchronization of the real-time clock (RTC).
    rtcsync

    allow 192.168.1.0/24
    cmdallow 192.168.1.0/24

    # Outside pools are the public ntp.org and the gentoo ntp pool. Leave polling intervals at the default of 64 seconds to not
    # abuse the public services. Use iburst for initial startup only.
    pool pool.ntp.org iburst
    server 0.gentoo.pool.ntp.org iburst
    server 1.gentoo.pool.ntp.org iburst
    server 2.gentoo.pool.ntp.org iburst
    server 3.gentoo.pool.ntp.org iburst

    # parry is another Internet-facing peer so mark it as preferred...
    peer parry.example.com minpoll 0 maxpoll 0 xleave prefer

    # ...and use it as reference during chrony startup in case the clock needs a large adjustment.
    initstepslew 30 parry.example.com

    # Interleaving further improves accuracy if timestamping (both hardware and software) is used,
    # just remember that it must be enabled on both ends or synchronization will not be bi-directional.
    # Also, 1-second polling interval is recommended for hardware-timestamped NTP.
    peer mater.example.com minpoll 0 maxpoll 0 xleave
    peer mike.example.com minpoll 0 maxpoll 0 xleave

    # thufir's NTP server does not support timestamping and by extension no interleaved mode,
    # therefore leave off the xleave directive. We still use 1-second polling though, because why not
    # - it's an internal server after all.
    peer thufir.example.com minpoll 0 maxpoll 0

    #
    # On topshelf, /dev/ptp3 is the hardware clock of the NIC used for PTP synchronization.
    # Note that since PTP uses TAI and not UTC, it is necessary to either provide the current TAI-UTC offset
    # and update it whenever a new leap second is introduced (these are announced around 6 months in advance,
    # in January and July every year; see https://www.iers.org/SharedDocs/News/EN/BulletinC.html) or use this
    # clock for sub-second accuracy only (in which case it is *required* to have another time source, like the
    # NTP pool, to complete the samples).
    #

    # Option 1: use an external database of leap seconds. Depends on sys-libs/timezone-data[leaps-timezone],
    # as well as a one-time manual hack:
    #    mkdir /usr/share/zoneinfo/right
    #    ln -s ../../zoneinfo-leaps/UTC /usr/share/zoneinfo/right/
    # Will update automatically (i.e. without restarting chronyd) but make sure to update the database
    # at least 12 hours before the newly announced leap second for it to take effect.
    leapsectz right/UTC
    refclock PHC /dev/ptp2 tai

    # Option 2: set the TAI-UTC offset manually. As of mid-July 2020 the offset is -37 seconds
    # and will remain so until at least 2021-06-30. Obviously, changing this will require
    # restarting chronyd.
    #refclock PHC /dev/ptp2 offset -37

    # Option 3: use the PTP clock for sub-second accuracy but rely on NTP sources configured above
    # for everything else.
    #refclock PHC /dev/ptp2 pps

    # Enable hardware timestamping of NTP packets for all interfaces. Only really used on the interface
    # facing local peers but essentially harmless to enable globally.
    hwtimestamp *

    dumpdir /run/chronyd
    dumponexit
    hwclockfile /etc/adjtime

    logdir /var/log/chrony
    log tracking rtc

The first part of the file uses the public pool of ntp.org and gentoo ntp servers for our upstream sources. The iburst option allows topshelf and parry to have an initially larger amount of ntp transactions pack and forth with the upstream servers until the accurate time gets settled upon. However that may not necessarily happen since the initstepslew directive will take effect first. That directive will quickly slew the clock into shape upon startup if the time is off by 30 seconds or more.

The prefer option on these two designates them to be treated with higher priority amongst all of the peers. Thus either parry or topshelf will show up as the reference clock when issuing a tracking command to chronyc from other machine on this network.

The xleave option causes chrony to send transmit timestamps captured after actual transmissions, which helps to reduce jitter and improve accuracy. It supports both hardware and software timestamping, and is harmless to enable for server connections even if the server does not support this mode. On the other hand, in case of peer connections interleaved mode must be supported by and enabled on both ends.

The refclock directive has the host use the NIC clock 3 (which on topshelf is the clock associated with the NIC facing the PTP master) as an additional reference source. It will show up as the PHC0 source in the first line of a *chronyc sources*. As previously mentioned, chrony will make no attempt to actually synchronize this clock with any other source.

The hwtimestamp \* directive tells chrony to enable hardware timestamping on all the NICs it may use that support it, to timestamp incoming and outgoing NTP packets.

### [Chrony config on a local peer]

[FILE] **`/etc/chrony/chrony.conf`Customized chrony config file for mater**

    # Record the rate at which the system clock gains/loses time.
    driftfile /var/lib/chrony/drift

    # Allow the system clock to be stepped in the first three updates
    # if its offset is larger than 1 second.
    makestep 1.0 3

    # Enable kernel synchronization of the real-time clock (RTC).
    rtcsync

    allow 192.168.1.0/24
    cmdallow 192.168.1.0/24

    # parry and topshelf are Internet-facing peers so mark them as preferred...
    peer parry.example.com minpoll 0 maxpoll 0 prefer
    peer topshelf.example.com minpoll 0 maxpoll 0 prefer

    # ...and use them as reference during chrony startup in case the clock needs a large adjustment.
    initstepslew 30 parry.example.com topshelf.example.com

    # Interleaving further improves accuracy if timestamping (both hardware and software) is used,
    # just remember that it must be enabled on both ends or synchronization will not be bi-directional.
    # Also, 1-second polling interval is recommended for hardware-timestamped NTP.
    peer mike.example.com minpoll 0 maxpoll 0 xleave

    # thufir's NTP server does not support timestamping and by extension no interleaved mode,
    # therefore leave off the xleave directive. We still use 1-second polling though, because why not
    # - it's an internal server after all.
    peer thufir.example.com minpoll 0 maxpoll 0

    # Enable hardware timestamping of NTP packets for all interfaces. Only really used on the interface
    # facing local peers but essentially harmless to enable globally.
    hwtimestamp *

    dumpdir /run/chronyd
    dumponexit
    hwclockfile /etc/adjtime

    logdir /var/log/chrony
    log tracking rtc

The local peers rely on topshelf and parry to provide NTP time so external sources have been removed. There is also no refclock line because the NIC clocks are not PTP-synchronized.

### [chrony with hardware timestamping in action]

This is the output of a \'chronyc sources\' and tracking report on mike after the newly configured chrony has been pushed out to all of the hosts and has been running for a while. topshelf shows with \"=\*\" since it is the reference clock. parry shows \"=+\" since it is regarded highly enough to be considered in the clock adjustment combining algorithm. The other peers show as \"=-\" since they are not currently being regarded as sources for adjustments.

`root `[`#`]`chronyc`

    chrony version 3.3
    Copyright (C) 1997-2003, 2007, 2009-2018 Richard P. Curnow and others
    chrony comes with ABSOLUTELY NO WARRANTY.  This is free software, and
    you are welcome to redistribute it under certain conditions.  See the
    GNU General Public License version 2 for details.

    chronyc> sources
    210 Number of sources = 4
    MS Name/IP address         Stratum Poll Reach LastRx Last sample
    ===============================================================================
    =+ parry.example.com             3   0   365     3    -48ns[  -48ns] +/-   15ms
    =* topshelf.example.com.>        2   0   377     7   -390ns[ -438ns] +/-   15ms
    =- thufir.example.com            3   0   165    10    +49us[  +49us] +/-   15ms
    =- mater.example.com             3   0   377     0  -4842ns[-4842ns] +/-   15ms
    chronyc> tracking
    Reference ID    : C0A80B21 (topshelf.example.com.1.168.192.in-addr.arpa)
    Stratum         : 3
    Ref time (UTC)  : Thu Mar 21 20:57:24 2019
    System time     : 0.000000522 seconds fast of NTP time
    Last offset     : +0.000000025 seconds
    RMS offset      : 0.000001429 seconds
    Frequency       : 0.321 ppm fast
    Residual freq   : -0.000 ppm
    Skew            : 0.007 ppm
    Root delay      : 0.025426105 seconds
    Root dispersion : 0.002194689 seconds
    Update interval : 5.4 seconds
    Leap status     : Normal
    chronyc>