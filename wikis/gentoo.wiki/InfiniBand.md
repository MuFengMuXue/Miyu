**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/InfiniBand "wikipedia:InfiniBand")

[[]][InfiniBand® Trade Association](http://www.infinibandta.org)

**InfiniBand** is a switched fabric communications link used in high-performance computing and enterprise data centers. Its features include high throughput, low latency, quality of service and failover, and it is designed to be scalable. The InfiniBand architecture specification defines a connection between processor nodes and high performance I/O nodes such as storage devices.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
        -   [[1.1.1] [Modules]](#Modules)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [IP over InfiniBand (IPoIB)]](#IP_over_InfiniBand_.28IPoIB.29)
        -   [[2.1.1] [Performance tuning]](#Performance_tuning)
            -   [[2.1.1.1] [Automatic]](#Automatic)
            -   [[2.1.1.2] [Manual]](#Manual)
-   [[3] [Performance testing]](#Performance_testing)
    -   [[3.1] [sys-fabric/qperf]](#sys-fabric.2Fqperf)
    -   [[3.2] [net-misc/iperf]](#net-misc.2Fiperf)
-   [[4] [References]](#References)

## [Installation]

### [Kernel]

Users of Mellanox hardware MSX6710, MSX8720, MSB7700, MSN2700, MSX1410, MSN2410, MSB7800, MSN2740, and MSN2100 need at least kernel 4.9.^[\[1\]](#cite_note-1)^

The following kernel options must be activated:

[KERNEL] **Enable InfiniBand support (`CONFIG_INFINIBAND`)**

    Device Drivers  --->
       <*> InfiniBand support  --->
          <*> InfiniBand userspace MAD support
          <*> InfiniBand userspace access (verbs and CM)
          <M> Mellanox HCA support
          <M> QLogic PCIe HCA support
          <M> Ammasso 1100 HCA support
          <M> Mellanox ConnectX HCA support
          <M> NetEffect RNIC Driver
          <M> Emulex One Connect HCA support
          <M> IP-over-InfiniBand
             [*] IP-over-InfiniBand Connected Mode support
          <M>   InfiniBand SCSI RDMA Protocol

** Note**\
In this example everything is selected. Most likely the userspace API (first two options) and the HCA (host channel/control adapter) drivers are needed for system specific hardware. IP-over-InfiniBand or srp modules may also be needed if they are required features.

#### [Modules]

If built as modules, some of them don\'t necessarily get loaded automatically. The following file is an example for [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") and OpenRC systems.

[FILE] **`/etc/modules-load.d/InfiniBand.conf`modules-load.d InfiniBand modules**

    # Some necessary modules for InfiniBand

    ib_core
    # Next one if for certain Mellanox harware. Pick appropiate for your hardware.
    ib_mthca
    ib_cm
    ib_ipoib
    ib_uverbs
    # umad is recommended, not mandatory, unless you explicitly use programs that need libibumad.
    ib_umad
    # For RDMA. You propably want these three if you have InfiniBand hardware, unless using IP-over-IB only.
    rpcrdma
    rdma_cm
    rdma_ucm

Also make sure the module loading systemd service is enabled:

`root `[`#`]`systemctl enable systemd-modules-load.service`

Note: some module already loaded by [[[sys-cluster/rdma-core]](https://packages.gentoo.org/packages/sys-cluster/rdma-core)[]] when using systemd or OpenRC.

### [USE flags]

### [USE flags for] [sys-cluster/rdma-core](https://packages.gentoo.org/packages/sys-cluster/rdma-core) [[]] [Userspace components for the Linux Kernel\'s drivers/infiniband subsystem]

  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------
  [`lttng`](https://packages.gentoo.org/useflags/lttng)               Enable support for the LTTng tracer
  [`neigh`](https://packages.gentoo.org/useflags/neigh)               Enable iwpmd support
  [`python`](https://packages.gentoo.org/useflags/python)             Enable pyverbs support
  [`static-libs`](https://packages.gentoo.org/useflags/static-libs)   Build static versions of dynamic libraries as well
  [`systemd`](https://packages.gentoo.org/useflags/systemd)           Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`valgrind`](https://packages.gentoo.org/useflags/valgrind)         Enable annotations for accuracy. May slow down runtime slightly. Safe to use even if not currently using dev-debug/valgrind
  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-10-15 16:07] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [USE flags for] [sys-fabric/opensm](https://packages.gentoo.org/packages/sys-fabric/opensm) [[]] [OpenSM - InfiniBand Subnet Manager and Administration for OpenIB]

  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`selinux`](https://packages.gentoo.org/useflags/selinux)   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`tools`](https://packages.gentoo.org/useflags/tools)       Install ssld extra tool
  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-19 09:51] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

If your software package is relatively new, you can try

`root `[`#`]`emerge --ask sys-cluster/rdma-core sys-fabric/opensm`

Among them, infiniband-diags has been DEPRECATED by upstream, and its function has been included in the code of [[[sys-cluster/rdma-core]](https://packages.gentoo.org/packages/sys-cluster/rdma-core)[]]

## [Usage]

### [][IP over InfiniBand (IPoIB)]

Users of InfiniBand can also use it to carry IP-networking packets, thus allowing it to replace ethernet in some cases. From at least kernel version 4.10 onwards users can compile IP-over-IB in-kernel (`CONFIG_INFINIBAND_IPOIB`). However if that\'s not the case and the support is compiled as kernel module it may be possible that the module isn\'t automatically loaded. The module is named **ib_ipoib**:

`root `[`#`]`modprobe ib_ipoib`

InfiniBand network interfaces are usually named as `ib<number>`:

`user `[`$`]`ifconfig ib0`

    ib0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 2044
    Infiniband hardware address can be incorrect! Please read BUGS section in ifconfig(8).
            infiniband 00:00:04:04:FE:80:00:00:00:00:00:00:00:00:00:00:00:00:00:00  txqueuelen 256  (InfiniBand)
            RX packets 0  bytes 0 (0.0 B)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 0  bytes 0 (0.0 B)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

#### [Performance tuning]

When using IP over InfiniBand, the performance is usually low by default. This is because the default MTU of each InfiniBand IP interface is set to a low value.

##### [Automatic]

The most convenient way is to change MTU automatically when kernel adds the interface to the system. Before MTU can be changed the mode of the interface must be changed to \'connected\' from \'datagram\' Next example uses udev rules to accomplish that.

[FILE] **`/etc/udev/rules.d/2-InfiniBand.rules`udev rules for InfiniBand IP networking interfaces**

    # Rules to set InfiniBand device attributes.

    # Change mode to connected and change mtu to maximum for best performance.
    ACTION=="add", KERNEL=="ib[0-9]*", SUBSYSTEM=="net", ATTR="connected", ATTR="65520"

It has been reported^[\[2\]](#cite_note-2)[\[3\]](#cite_note-3)^ that the rule above does not work. Users with this problem may use the following instead:

[FILE] **`/etc/udev/rules.d/2-InfiniBand.rules`udev rules for InfiniBand IP networking interfaces**

    # Rules to set InfiniBand device attributes.

    # Change mode to connected and change mtu to maximum for best performance.
    ACTION=="add", KERNEL=="ib[0-9]*", SUBSYSTEM=="net", RUN+="/bin/sh -c 'echo connected > /sys/class/net/%k/mode && echo 65520 > /sys/class/net/%k/mtu'"

If your system is relatively new, and the above method does not work, you can use the following method:

[FILE] **`/etc/udev/rules.d/90-persistent-ibsettings.rules`udev rules for InfiniBand IP networking interfaces**

    # Rules to set InfiniBand device attributes.

    # Change mode to connected and change mtu to maximum for best performance.
    # ATTR=="32" is IPoIB interfaces
    ACTION=="add", SUBSYSTEM=="net", DRIVERS=="?*", ATTR=="32", ENV!="", NAME="$env", RUN+="/bin/sh -c 'echo connected > /sys/class/net/%E/mode && echo 65520 > /sys/class/net/%E/mtu'"

##### [Manual]

Mode and mtu can also be changed manually in run time. Next commands assume the interface in question is named `ib0`.

`root `[`#`]`echo connected > /sys/class/net/ib0/mode`

`root `[`#`]`echo 65520 > /sys/class/net/ib0/mtu`

## [Performance testing]

There are several ways to test InfiniBand performance. When [IP-over-InfiniBand](#IP_over_InfiniBand_.28IPoIB.29) has been set up propely users can use normal network performance testing tools for IP networks like [[[net-misc/iperf]](https://packages.gentoo.org/packages/net-misc/iperf)[]]. Most users however may want to use [[[sys-fabric/qperf]](https://packages.gentoo.org/packages/sys-fabric/qperf)[]] since it has the capability of testing the [RDMA](https://en.wikipedia.org/wiki/RDMA "wikipedia:RDMA") performance too. For example [NFS](https://wiki.gentoo.org/wiki/Nfs-utils "Nfs-utils") can utilize RDMA in conjunction with IP networking^[\[4\]](#cite_note-4)^.

### [][sys-fabric/qperf]

Start [qperf] in one of the nodes:

`root `[`#`]`qperf`

This node now acts as a server.

Run tests on any client that has connection to the node(s) that now runs [qperf] in server mode. The following example runs TCP, UDP and some RDMA performance tests and assumes the qperf server node has an IP address of [10.0.10.1]:

`root `[`#`]`qperf 10.0.10.1 ud_lat ud_bw rc_rdma_read_bw rc_rdma_write_bw uc_rdma_write_bw tcp_bw tcp_lat udp_bw udp_lat`

    ud_lat:
        latency  =  27.6 us
    ud_bw:
        send_bw  =  676 MB/sec
        recv_bw  =  660 MB/sec
    rc_rdma_read_bw:
        bw  =  855 MB/sec
    rc_rdma_write_bw:
        bw  =  738 MB/sec
    uc_rdma_write_bw:
        send_bw  =  768 MB/sec
        recv_bw  =  735 MB/sec
    tcp_bw:
        bw  =  656 MB/sec
    tcp_lat:
        latency  =  51.2 us
    udp_bw:
        send_bw  =  719 MB/sec
        recv_bw  =  626 MB/sec
    udp_lat:
        latency  =  49.2 us

After the needed tests are complete, stop the server process(es) just by hitting [Ctrl]+[c] on the terminal where the server-side [qperf] runs.

### [][net-misc/iperf]

### [USE flags for] [net-misc/iperf](https://packages.gentoo.org/packages/net-misc/iperf) [[]] [TCP, UDP, and SCTP network bandwidth measurement tool]

  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`debug`](https://packages.gentoo.org/useflags/debug)   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`sctp`](https://packages.gentoo.org/useflags/sctp)     Support for Stream Control Transmission Protocol
  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-14 06:19] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

[iperf3], like qperf, needs a listening side to be started before actual performance testing.

Simplest way to start a iperf server process is:

`root `[`#`]`iperf3 -s`

However to reduce the output of the statistics on the server side users may want to limit the interval of the status updates. Next example set the interval to 10 seconds from the 1 second default:

`root `[`#`]`iperf3 -s -i 10`

Or suppress all normal output so that only errors are displayed:

`root `[`#`]`iperf3 -s > /dev/null`

Next run the client side [iperf3] - again assuming the server has an IP address of 10.0.10.1:

`root `[`#`]`iperf3 -c 10.0.10.1 -n 256G -i 60`

    Connecting to host 10.0.10.1, port 5201
    [  4] local 10.0.10.2 port 37670 connected to 10.0.10.1 port 5201
    [ ID] Interval           Transfer     Bandwidth       Retr  Cwnd
    [  4]   0.00-60.00  sec  40.2 GBytes  5.76 Gbits/sec    0   3.25 MBytes
    [  4]  60.00-120.00 sec  40.2 GBytes  5.75 Gbits/sec    0   3.25 MBytes
    [  4] 120.00-180.00 sec  40.2 GBytes  5.75 Gbits/sec    0   3.25 MBytes
    [  4] 180.00-240.00 sec  40.2 GBytes  5.75 Gbits/sec    0   3.25 MBytes
    [  4] 240.00-300.00 sec  40.2 GBytes  5.76 Gbits/sec    0   3.25 MBytes
    [  4] 300.00-360.00 sec  40.2 GBytes  5.76 Gbits/sec    0   3.25 MBytes
    [  4] 360.00-382.07 sec  14.8 GBytes  5.75 Gbits/sec    0   3.25 MBytes
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bandwidth       Retr
    [  4]   0.00-382.07 sec   256 GBytes  5.76 Gbits/sec    0             sender
    [  4]   0.00-382.07 sec   256 GBytes  5.76 Gbits/sec                  receiver

    iperf Done.

The command above really puts the IP connection to a stress test by transferring 256 **gigabytes** of data which took over six minutes on this example. Users who just want quickly to see the bandwidth may run the following:

`root `[`#`]`iperf3 -c 10.0.10.1 -n 25G -i 5`

\... which transfers 25 gigabytes with 5 second interval between statistic reporting.

Refer to the [iperf3 \--help] for more:

`user `[`$`]`iperf3 --help`

    Usage: iperf [-s|-c host] [options]
           iperf [-h|--help] [-v|--version]

    Server or Client:
      -p, --port      #         server port to listen on/connect to
      -f, --format    [kmgKMG]  format to report: Kbits, Mbits, KBytes, MBytes
      -i, --interval  #         seconds between periodic bandwidth reports
      -F, --file name           xmit/recv the specified file
      -A, --affinity n/n,m      set CPU affinity
      -B, --bind      <host>    bind to a specific interface
      -V, --verbose             more detailed output
      -J, --json                output in JSON format
      --logfile f               send output to a log file
      --forceflush              force flushing output at every interval
      -d, --debug               emit debugging output
      -v, --version             show version information and quit
      -h, --help                show this message and quit
    Server specific:
      -s, --server              run in server mode
      -D, --daemon              run the server as a daemon
      -I, --pidfile file        write PID file
      -1, --one-off             handle one client connection then exit
    Client specific:
      -c, --client    <host>    run in client mode, connecting to <host>
      -u, --udp                 use UDP rather than TCP
      -b, --bandwidth #[KMG][/#] target bandwidth in bits/sec (0 for unlimited)
                                (default 1 Mbit/sec for UDP, unlimited for TCP)
                                (optional slash and packet count for burst mode)
      --fq-rate #[KMG]          enable fair-queuing based socket pacing in
                                bits/sec (Linux only)
      -t, --time      #         time in seconds to transmit for (default 10 secs)
      -n, --bytes     #[KMG]    number of bytes to transmit (instead of -t)
      -k, --blockcount #[KMG]   number of blocks (packets) to transmit (instead of -t or -n)
      -l, --len       #[KMG]    length of buffer to read or write
                                (default 128 KB for TCP, dynamic or 1 for UDP)
      --cport             bind to a specific client port (TCP and UDP, default: ephemeral port)
      -P, --parallel  #         number of parallel client streams to run
      -R, --reverse             run in reverse mode (server sends, client receives)
      -w, --window    #[KMG]    set window size / socket buffer size
      -C, --congestion <algo>   set TCP congestion control algorithm (Linux and FreeBSD only)
      -M, --set-mss   #         set TCP/SCTP maximum segment size (MTU - 40 bytes)
      -N, --no-delay            set TCP/SCTP no delay, disabling Nagle's Algorithm
      -4, --version4            only use IPv4
      -6, --version6            only use IPv6
      -S, --tos N               set the IP 'type of service'
      -L, --flowlabel N         set the IPv6 flow label (only supported on Linux)
      -Z, --zerocopy            use a 'zero copy' method of sending data
      -O, --omit N              omit the first n seconds
      -T, --title str           prefix every output line with this string
      --get-server-output       get results from server
      --udp-counters-64bit      use 64-bit counters in UDP test packets

    [KMG] indicates options that support a K/M/G suffix for kilo-, mega-, or giga-

    iperf3 homepage at: http://software.es.net/iperf/
    Report bugs to:     https://github.com/esnet/iperf

After the needed tests are complete stop the server process(es) just by hitting [Ctrl]+[c] on the terminal where the server-side [iperf3] runs.

## [References]

1.  [[[↑](#cite_ref-1)] [[Phoronix - Mellanox Platform Support Coming In Linux 4.9](http://www.phoronix.com/scan.php?page=news_item&px=Mellanox-Linux-4.9)]]
2.  [[[↑](#cite_ref-2)] [[Gentoo forums - post 8060796](https://forums.gentoo.org/viewtopic-p-8060796.html#8060796) - Udev rules don\'t work on ib interface]]
3.  [[[↑](#cite_ref-3)] [[Gentoo wiki - User Zucca](https://wiki.gentoo.org/wiki/User:Zucca/wip/InfiniBand/resources#Udev_rules "User:Zucca/wip/InfiniBand/resources") - InfiniBand resources]]
4.  [[[↑](#cite_ref-4)] [[NFS over RDMA](https://www.kernel.org/doc/Documentation/filesystems/nfs/nfs-rdma.txt)]]