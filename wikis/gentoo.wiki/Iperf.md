**Resources**

[[]][Homepage (v2)](http://iperf.sourceforge.net/)

[[]][Homepage (v3)](http://software.es.net/iperf/)

[[]][Package information](https://packages.gentoo.org/packages/net-misc/iperf)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Iperf "wikipedia:Iperf")

[[]][GitHub (v3)](https://github.com/esnet/iperf)

[iperf] is a network testing utility helpful for determining network performance.

On Gentoo, [iperf] and [iperf3] are slotted, therefore both version 2 and version 3 of the utility can be installed concurrently.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
        -   [[1.1.1] [Version 3]](#Version_3)
    -   [[1.2] [Emerge]](#Emerge)
        -   [[1.2.1] [Version 2]](#Version_2)
        -   [[1.2.2] [Version 3]](#Version_3_2)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Environment variables]](#Environment_variables)
    -   [[2.2] [Files]](#Files)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
        -   [[3.1.1] [Version 2]](#Version_2_2)
        -   [[3.1.2] [Version 3]](#Version_3_3)
    -   [[3.2] [Running tests]](#Running_tests)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation]

### [USE flags]

#### [Version 3]

### [USE flags for] [net-misc/iperf](https://packages.gentoo.org/packages/net-misc/iperf) [[]] [TCP, UDP, and SCTP network bandwidth measurement tool]

  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`debug`](https://packages.gentoo.org/useflags/debug)   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`sctp`](https://packages.gentoo.org/useflags/sctp)     Support for Stream Control Transmission Protocol
  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-14 06:19] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

#### [Version 2]

`root `[`#`]`emerge --ask net-misc/iperf:2`

#### [Version 3]

`root `[`#`]`emerge --ask net-misc/iperf:3`

## [Configuration]

### [Environment variables]

### [Files]

-   [/etc/init.d/iperf3] - Init file for iperf3 running as a service on [OpenRC.](https://wiki.gentoo.org/wiki/OpenRC "OpenRC")
-   [/etc/conf.d/iperf3] - Init configuration file for iperf3 running as a service on [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC"). This is the file that should be adjusted as necessary when starting iperf from OpenRC.

## [Usage]

### [Invocation]

#### [Version 2]

`user `[`$`]`iperf --help`

    Usage: iperf [-s|-c host] [options]
           iperf [-h|--help] [-v|--version]

    Client/Server:
      -f, --format    [kmKM]   format to report: Kbits, Mbits, KBytes, MBytes
      -i, --interval  #        seconds between periodic bandwidth reports
      -l, --len       #[KM]    length of buffer to read or write (default 8 KB)
      -m, --print_mss          print TCP maximum segment size (MTU - TCP/IP header)
      -o, --output    <filename> output the report or error message to this specified file
      -p, --port      #        server port to listen on/connect to
      -u, --udp                use UDP rather than TCP
      -w, --window    #[KM]    TCP window size (socket buffer size)
      -B, --bind      <host>   bind to <host>, an interface or multicast address
      -C, --compatibility      for use with older versions does not sent extra msgs
      -M, --mss       #        set TCP maximum segment size (MTU - 40 bytes)
      -N, --nodelay            set TCP no delay, disabling Nagle's Algorithm
      -V, --IPv6Version        Set the domain to IPv6

    Server specific:
      -s, --server             run in server mode
      -U, --single_udp         run in single threaded UDP mode
      -D, --daemon             run the server as a daemon

    Client specific:
      -b, --bandwidth #[KM]    for UDP, bandwidth to send at in bits/sec
                               (default 1 Mbit/sec, implies -u)
      -c, --client    <host>   run in client mode, connecting to <host>
      -d, --dualtest           Do a bidirectional test simultaneously
      -n, --num       #[KM]    number of bytes to transmit (instead of -t)
      -r, --tradeoff           Do a bidirectional test individually
      -t, --time      #        time in seconds to transmit for (default 10 secs)
      -F, --fileinput <name>   input the data to be transmitted from a file
      -I, --stdin              input the data to be transmitted from stdin
      -L, --listenport #       port to receive bidirectional tests back on
      -P, --parallel  #        number of parallel client threads to run
      -T, --ttl       #        time-to-live, for multicast (default 1)
      -Z, --linux-congestion <algo>  set TCP congestion control algorithm (Linux only)

    Miscellaneous:
      -x, --reportexclude [CDMSV]   exclude C(connection) D(data) M(multicast) S(settings) V(server) reports
      -y, --reportstyle C      report as a Comma-Separated Values
      -h, --help               print this message and quit
      -v, --version            print version information and quit

    [KM] Indicates options that support a K or M suffix for kilo- or mega-

    The TCP window size option can be set by the environment variable
    TCP_WINDOW_SIZE. Most other options can be set by an environment variable
    IPERF_<long option name>, such as IPERF_BANDWIDTH.

    Report bugs to <iperf-users@lists.sourceforge.net>

#### [Version 3]

`user `[`$`]`iperf3`

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
      -t, --time      #         time in seconds to transmit for (default 10 secs)
      -n, --bytes     #[KMG]    number of bytes to transmit (instead of -t)
      -k, --blockcount #[KMG]   number of blocks (packets) to transmit (instead of -t or -n)
      -l, --len       #[KMG]    length of buffer to read or write
                                (default 128 KB for TCP, 8 KB for UDP)
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

### [Running tests]

To test bandwidth speed or otherwise stress test a network, iperf will need to be started as a server on one node and a client on the other(s).

To start iperf in server mode:

`root `[`#`]`iperf3 --server`

On the client node, the IP address or hostname of the server node will be needed:

`root `[`#`]`iperf3 --client <IPv4_address>`

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose net-misc/iperf`

## [See also]

-   [[stress](https://wiki.gentoo.org/index.php?title=Stress&action=edit&redlink=1 "Stress (page does not exist)")] - A tool to stress test system hardware (pun intended).

## [External resources]

-   [https://arstechnica.com/gadgets/2016/01/numbers-dont-lie-its-time-to-build-your-own-router/](https://arstechnica.com/gadgets/2016/01/numbers-dont-lie-its-time-to-build-your-own-router/) - An article where [iperf3] was used to determine side-by-side comparison of router throughput, which is a good example of performance testing.