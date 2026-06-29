[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Wireshark&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.wireshark.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Wireshark "wikipedia:Wireshark")

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/wireshark)

[[]][GitWeb](https://code.wireshark.org/review/gitweb?p=wireshark.git;a=tree)

Wireshark is a free and open-source packet analyzer. It is used for network troubleshooting, analysis, software and communications protocol development, and education.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Permissions]](#Permissions)
-   [[3] [Fixing common problems with Wireshark]](#Fixing_common_problems_with_Wireshark)
    -   [[3.1] [libxxhash.so.0]](#libxxhash.so.0)
    -   [[3.2] [libwireshark.so.19]](#libwireshark.so.19)
-   [[4] [Wireshark over SSH]](#Wireshark_over_SSH)
    -   [[4.1] [Capture traffic remotely over SSH and Wireshark (ssh)]](#Capture_traffic_remotely_over_SSH_and_Wireshark_.28ssh.29)
    -   [[4.2] [Capture router traffic via wireshark (router)]](#Capture_router_traffic_via_wireshark_.28router.29)
    -   [[4.3] [Capture network traffic via Wireshark (android)]](#Capture_network_traffic_via_Wireshark_.28android.29)
    -   [[4.4] [Capture radio/sms/gsm traffic via wireshark (android)]](#Capture_radio.2Fsms.2Fgsm_traffic_via_wireshark_.28android.29)
-   [[5] [Techniques]](#Techniques)
    -   [[5.1] [Network Name Resolution]](#Network_Name_Resolution)
    -   [[5.2] [Filter packets to a specific IP Address]](#Filter_packets_to_a_specific_IP_Address)
-   [[6] [Terminal-based Wireshark]](#Terminal-based_Wireshark)
-   [[7] [Example Usage]](#Example_Usage)
    -   [[7.1] [Print http data in a tree]](#Print_http_data_in_a_tree)
-   [[8] [Wireguard]](#Wireguard)
    -   [[8.1] [Filter WireGuard traffic while capturing]](#Filter_WireGuard_traffic_while_capturing)
-   [[9] [Dumpcap]](#Dumpcap)
    -   [[9.1] [Example Usage]](#Example_Usage_2)
-   [[10] [See also]](#See_also)
-   [[11] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [net-analyzer/wireshark](https://packages.gentoo.org/packages/net-analyzer/wireshark) [[]] [Network protocol analyzer (sniffer)]

  --------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+capinfos`](https://packages.gentoo.org/useflags/+capinfos)         Install capinfos, to print information about capture files
  [`+captype`](https://packages.gentoo.org/useflags/+captype)           Install captype, to print the file types of capture files
  [`+dftest`](https://packages.gentoo.org/useflags/+dftest)             Install dftest, to display filter byte-code, for debugging dfilter routines
  [`+dumpcap`](https://packages.gentoo.org/useflags/+dumpcap)           Install dumpcap, to dump network traffic from inside wireshark
  [`+editcap`](https://packages.gentoo.org/useflags/+editcap)           Install editcap, to edit and/or translate the format of capture files
  [`+filecaps`](https://packages.gentoo.org/useflags/+filecaps)         Use Linux file capabilities to control privilege rather than set\*id (this is orthogonal to USE=caps which uses capabilities at runtime e.g. libcap)
  [`+gui`](https://packages.gentoo.org/useflags/+gui)                   Enable support for a graphical user interface
  [`+mergecap`](https://packages.gentoo.org/useflags/+mergecap)         Install mergecap, to merge two or more capture files into one
  [`+minizip`](https://packages.gentoo.org/useflags/+minizip)           Build with zip file compression support
  [`+netlink`](https://packages.gentoo.org/useflags/+netlink)           Use dev-libs/libnl
  [`+pcap`](https://packages.gentoo.org/useflags/+pcap)                 Use net-libs/libpcap for network packet capturing (build dumpcap, rawshark)
  [`+plugins`](https://packages.gentoo.org/useflags/+plugins)           Install plugins
  [`+randpkt`](https://packages.gentoo.org/useflags/+randpkt)           Install randpkt, a utility for creating pcap trace files full of random packets
  [`+randpktdump`](https://packages.gentoo.org/useflags/+randpktdump)   Install randpktdump, an extcap interface to provide access to the random packet generator (randpkt)
  [`+reordercap`](https://packages.gentoo.org/useflags/+reordercap)     Install reordercap, to reorder input file by timestamp into output file
  [`+sharkd`](https://packages.gentoo.org/useflags/+sharkd)             Install sharkd, the daemon variant of wireshark
  [`+text2pcap`](https://packages.gentoo.org/useflags/+text2pcap)       Install text2pcap, to generate a capture file from an ASCII hexdump of packets
  [`+tshark`](https://packages.gentoo.org/useflags/+tshark)             Install tshark, to dump and analyzer network traffic from the command line
  [`+udpdump`](https://packages.gentoo.org/useflags/+udpdump)           Install udpdump, to get packets exported from a source (like a network device or a GSMTAP producer) that are dumped to a pcap file
  [`+zstd`](https://packages.gentoo.org/useflags/+zstd)                 Enable support for ZSTD compression
  [`androiddump`](https://packages.gentoo.org/useflags/androiddump)     Install androiddump, an extcap interface to capture from Android devices
  [`bcg729`](https://packages.gentoo.org/useflags/bcg729)               Use media-libs/bcg729 for G.729 codec support in RTP Player
  [`brotli`](https://packages.gentoo.org/useflags/brotli)               Enable Brotli compression support
  [`ciscodump`](https://packages.gentoo.org/useflags/ciscodump)         Install ciscodump, extcap interface to capture from a remote Cisco router
  [`doc`](https://packages.gentoo.org/useflags/doc)                     Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`dpauxmon`](https://packages.gentoo.org/useflags/dpauxmon)           Install dpauxmon, an external capture interface (extcap) that captures DisplayPort AUX channel data from linux kernel drivers
  [`http2`](https://packages.gentoo.org/useflags/http2)                 Enable support for the HTTP/2 protocol
  [`http3`](https://packages.gentoo.org/useflags/http3)                 Install net-libs/nghttp3 for enhanced HTTP3 analysis
  [`ilbc`](https://packages.gentoo.org/useflags/ilbc)                   Build with iLBC support in RTP Player using media-libs/libilbc
  [`kerberos`](https://packages.gentoo.org/useflags/kerberos)           Add kerberos support
  [`lua`](https://packages.gentoo.org/useflags/lua)                     Enable Lua scripting support
  [`lz4`](https://packages.gentoo.org/useflags/lz4)                     Enable support for lz4 compression (as implemented in app-arch/lz4)
  [`maxminddb`](https://packages.gentoo.org/useflags/maxminddb)         Use dev-libs/libmaxminddb for IP address geolocation
  [`opus`](https://packages.gentoo.org/useflags/opus)                   Enable Opus audio codec support
  [`pkcs11`](https://packages.gentoo.org/useflags/pkcs11)               Add support for PKCS in net-libs/gnutls
  [`sbc`](https://packages.gentoo.org/useflags/sbc)                     Use media-libs/sbc for playing back SBC encoded packets
  [`sdjournal`](https://packages.gentoo.org/useflags/sdjournal)         Install sdjournal, an extcap that captures systemd journal entries
  [`selinux`](https://packages.gentoo.org/useflags/selinux)             !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`smi`](https://packages.gentoo.org/useflags/smi)                     Use net-libs/libsmi to resolve numeric OIDs into human readable format
  [`snappy`](https://packages.gentoo.org/useflags/snappy)               Enable support for Snappy compression (as implemented in app-arch/snappy)
  [`spandsp`](https://packages.gentoo.org/useflags/spandsp)             Use media-libs/spandsp for for G.722 and G.726 codec support in the RTP Player
  [`sshdump`](https://packages.gentoo.org/useflags/sshdump)             Install sshdump, an extcap interface to capture from a remote host through SSH
  [`ssl`](https://packages.gentoo.org/useflags/ssl)                     Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  [`test`](https://packages.gentoo.org/useflags/test)                   Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)       Verify upstream signatures on distfiles
  [`wifi`](https://packages.gentoo.org/useflags/wifi)                   Install wifidump, to dump and analyse 802.11 traffic
  [`xxhash`](https://packages.gentoo.org/useflags/xxhash)               Enable dev-libs/xxhash support for hashing
  [`zlib`](https://packages.gentoo.org/useflags/zlib)                   Add support for zlib compression
  --------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-20 13:22] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask net-analyzer/wireshark`

** Note**\
To install Wireshark with all of the extra features, the following `USE` flag should be enabled: `kerberos`.

## [Configuration]

### [Permissions]

** Warning**\
Running Wireshark as root can be dangerous and is unnecessary. See the [Wireshark Security](https://wiki.wireshark.org/Security/) page for more details.

As wireshark captures from hardware, it needs permissions set to enable capturing. To use wireshark as a normal user, add user to the pcap group (note, replace `$` by the user\'s actual login name):

`root `[`#`]`gpasswd -a $ pcap`

To make the session aware of this new group without having to log in again, enter this command before launching wireshark:

`user `[`$`]`newgrp pcap`

## [Fixing common problems with Wireshark]

### [libxxhash.so.0]

`user `[`$`]`wireshark`\
`wireshark: error while loading shared libraries: libxxhash.so.0: cannot open shared object file: No such file or directory`

Solution is installing [dev-libs/xxhash](https://packages.gentoo.org/packages/dev-libs/xxhash)

`root `[`#`]`emerge dev-libs/xxhash `

### [libwireshark.so.19]

`user `[`$`]`tshark`\
`tshark: symbol lookup error: /usr/lib64/libwireshark.so.19: undefined symbol: gnutls_pkcs11_token_get_url, version GNUTLS_3_4`

OR

`user `[`$`]`wireshark`\
`tshark: symbol lookup error: /usr/lib64/libwireshark.so.19: undefined symbol: gnutls_pkcs11_token_get_url, version GNUTLS_3_4`

GnuTLS needs to be rebuilt with the `pkcs11` USE flag enabled to expose full PKCS#11 token support symbols like `gnutls_pkcs11_token_get_url ` (introduced post-3.4).

`root `[`#`]`echo "net-libs/gnutls pkcs11" >> /etc/portage/package.use/gnutls`

## [Wireshark over SSH]

Source system (the server you want to capture packets on) that you have SSH access to, with tcpdump installed, and available to your user (either directly, or via sudo without password). Destination system (where you run graphical Wireshark) with wireshark installed and working, and mkfifo available. Procedure:

#### [][Capture traffic remotely over SSH and Wireshark (ssh)]

** Note**\
Include -U for prevent buffering when using tcpdump instead of tshark

`user `[`$`]`ssh root@server.com 'tshark -f "port !22" -w -' | wireshark -k -i -`

#### [][Capture router traffic via wireshark (router)]

** Note**\
Include -U for prevent buffering when using tcpdump instead of tshark

`user `[`$`]`ssh root@192.168.1.1 tcpdump -i any -U -s0 -w - 'not port 22' | wireshark -k -i -`

#### [][Capture network traffic via Wireshark (android)]

** Warning**\
This require root on your android device

`user `[`$`]`adb shell su -c tcpdump -nn -i wlan0 -U -s0 -w - 'not port 5555' | wireshark -k -i -`

#### [][Capture radio/sms/gsm traffic via wireshark (android)]

** Warning**\
This require root on your android device

`user `[`$`]`adb exec-out "su -c tcpdump -i any -U -w - 2>/dev/null" | wireshark -k -S -i -`

## [Techniques]

#### [Network Name Resolution]

To automatically resolve IP addresses to domain names, open the preferences window from [Edit -\> Preferences], clicking the [Name Resolution] panel and selecting the **Resolve network (IP) addresses** check box.

** Note**\
Enabling Network Name Resolution will increase the captured traffic due to additional DNS requests.

### [Filter packets to a specific IP Address]

To see all incoming and outgoing traffic for a specific address, enter [ip.addr] == [w.x.y.z] in the filter box, replacing [w.x.y.z] with the relevant IP address. Additionally, to view only incoming traffic, replace [ip.addr] with [ip.src]; to view only outgoing traffic, replace [ip.addr] with [ip.dst].

## [Terminal-based Wireshark]

TShark is a network protocol analyzer. It lets you capture packet data from a live network, or read packets from a previously saved capture file, either printing a decoded form of those packets to the standard output or writing the packets to a file. TShark\'s native capture file format is pcapng format, which is also the format used by Wireshark and various other tools.

Without any options set, TShark will work much like tcpdump. It will use the pcap library to capture traffic from the first available network interface and displays a summary line on the standard output for each received packet.

`user `[`$`]`tshark -h`

For example, to capture packets across a specified network interface and save the results, enter

`user `[`$`]`tshark -i wlan0 -w capture-output.pcap`

Replace [wlan0] with the desired network interface and [capture-output] with the desired filename.

** Note**\
Color output text similarly to the Wireshark GUI, requires a terminal with 24-bit color support Also supplies color attributes to pdml and psml formats

`user `[`$`]`tshark -i any --color`

\

## [Example Usage]

Show only filetypes that begin with \"text\"



    `user `[`$`]`tshark -Y 'http.content_type[0:4] == "text"'`


    ::::

Show only javascript



    `user `[`$`]`tshark -Y tshark -i wlp2s0 -Y 'http.content_type contains "javascript"'`


    ::::

Show all http with content-type=\"image/(gif\|jpeg\|png\|etc)\"



    `user `[`$`]`tshark -Y 'http.content_type[0:5] == "image"'`


    ::::

Show all http with content-type=\"image/gif\"



    `user `[`$`]`tshark -Y http.content_type == "image/gif"`


    ::::

Do not show content http, only headers



    `user `[`$`]`tshark -Y http.response !=0 || http.request.method != "TRACE"`


    ::::

To match IP addresses ending in 255 in a block of subnets (172.16 to 172.31)



    `user `[`$`]`tshark -Y string(ip.dst) matches r"^172\.(1[6-9]|2[0-9]|3[0-1])\.[0-9]\.255`


    ::::

To match odd frame numbers



    `user `[`$`]`tshark -Y string(frame.number) matches "[13579]$"`


    ::::

To see just the file header for any capture type, capture no packets and send to xxd
    :::: cmd-box


    `user `[`$`]`tshark -f ipx -a duration:1 -F pcap -w - 2>/dev/null | xxd -u`


    ::::

### [Print http data in a tree]

`user `[`$`]`tshark -q -i any -Y http -z http,tree`

    =======================================================================================================================================
    HTTP/Packet Counter:
    Topic / Item            Count         Average       Min Val       Max Val       Rate (ms)     Percent       Burst Rate    Burst Start
    ---------------------------------------------------------------------------------------------------------------------------------------
    Total HTTP Packets      1                                                                     100%          0.0100        2.255
     HTTP Request Packets   1                                                                     100.00%       0.0100        2.255
      GET                   1                                                                     100.00%       0.0100        2.255
     Other HTTP Packets     0                                                                     0.00%         -             -
     HTTP Response Packets  0                                                                     0.00%         -             -
      ???: broken           0                                                                                   -             -
      5xx: Server Error     0                                                                                   -             -
      4xx: Client Error     0                                                                                   -             -
      3xx: Redirection      0                                                                                   -             -
      2xx: Success          0                                                                                   -             -
      1xx: Informational    0                                                                                   -             -

    ---------------------------------------------------------------------------------------------------------------------------------------

## [Wireguard]

WireGuard was initially started by [Jason A. Donenfeld (zx2c4)](https://wiki.gentoo.org/wiki/User:Zx2c4 "User:Zx2c4") in 2015 as a Linux kernel module. As of January 2020, it has been accepted for Linux v5.6. Support for other platforms (macOS, Android, iOS, BSD, and Windows) is provided by a cross-platform wireguard-go implementation.

#### [Filter WireGuard traffic while capturing]

`user `[`$`]`tshark -i any udp[8:1] >= 1 and udp[8:1] <= 4 and udp[9:1] == 0 and udp[10:2] == 0`

Assuming that your WireGuard traffic goes over the wlan0 interface using port 51820

[download extract-handshakes.sh](https://git.zx2c4.com/wireguard-tools/tree/contrib/extract-handshakes/extract-handshakes.sh)

`user `[`$`]`extract-handshakes.sh > wg.keys & tshark -i wlan0 -owg.keylog_file:wg.keys -f 'udp port 51820'`

Step-by-step instructions for these are not yet available for the version merged in Linux v5.6. What you basically have to do is to build offset-finder.c with the headers from [drivers/net/wireguard/](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/net/wireguard) and kernel headers and config matching your current kernel.

## [Dumpcap]

Dumpcap is a network traffic dump tool. It captures packet data from a live network and writes the packets to a file. Dumpcap's native capture file format is pcapng, which is also the format used by Wireshark.

By default, Dumpcap uses the pcap library to capture traffic from the first available network interface and writes the received raw packet data, along with the packets' time stamps into a pcapng file. The capture filter syntax follows the rules of the pcap library.

Dumpcap can benefit from an enabled BPF JIT compiler if available. You might want to enable it by executing:

`user `[`$`]`echo 1 > /proc/sys/net/core/bpf_jit_enable`

** Warning**\
Note that this can make your system less secure so change it back when your capture is done

### [Example Usage]

Capture packets from interface any interface until 60s passed into output.pcapng



    `user `[`$`]`dumpcap -i any -a duration:60 -w output.pcapng`


    ::::

    :::
    ** Tip**\
    Use Ctrl-C to stop capturing at any time
    :::

Another example that will capture packets by size, duration, packets and files



    `user `[`$`]`dumpcap -a duration:100 -a files:10 -a filesize:10000 -a packets:10000 -b duration:100 -b files:1000 -b filesize:1024 -b packets:20 -w file.pcap`


    ::::

## [See also]

-   [Metasploit](https://wiki.gentoo.org/wiki/Metasploit "Metasploit") --- provides information about security vulnerabilities and aids in penetration testing and IDS signature development.
-   [Nmap](https://wiki.gentoo.org/wiki/Nmap "Nmap") --- an open source recon tool used to check for open ports, what is running on those ports, and metadata about the daemons servicing those ports.
-   [Tcpdump](https://wiki.gentoo.org/wiki/Tcpdump "Tcpdump") --- a command-line network monitoring and data acquisition tool.

## [External resources]

-   [https://tshark.dev](https://tshark.dev) - tshark.dev

<!-- -->

-   [https://wiki.wireshark.org/DisplayFilters](https://wiki.wireshark.org/DisplayFilters) - Display Filters
-   [https://wiki.wireshark.org/Development/LibpcapFileFormat](https://wiki.wireshark.org/Development/LibpcapFileFormat) - Libpcap File Format
-   [https://www.wireshark.org/download/docs/user-guide.pdf](https://www.wireshark.org/download/docs/user-guide.pdf) Wireshark User\'s Guide.