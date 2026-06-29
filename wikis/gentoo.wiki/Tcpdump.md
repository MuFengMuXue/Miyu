**Resources**

[[]][Home](http://www.tcpdump.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Tcpdump "wikipedia:Tcpdump")

[[]][GitHub](https://github.com/the-tcpdump-group/tcpdump)

[tcpdump] is a command-line network monitoring and data acquisition tool. It is capable of sniffing packets and \"dumping\" information.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [SUID]](#SUID)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
    -   [[3.2] [Listing interfaces]](#Listing_interfaces)
    -   [[3.3] [Specifying an interface]](#Specifying_an_interface)
    -   [[3.4] [Write output to a file]](#Write_output_to_a_file)
    -   [[3.5] [Read input from a file]](#Read_input_from_a_file)
    -   [[3.6] [Capture network traffic over ssh and wireshark]](#Capture_network_traffic_over_ssh_and_wireshark)
-   [[4] [Advanced Usage]](#Advanced_Usage)
    -   [[4.1] [Filter Showing Nmap NSE Script Testing]](#Filter_Showing_Nmap_NSE_Script_Testing)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [net-analyzer/tcpdump](https://packages.gentoo.org/packages/net-analyzer/tcpdump) [[]] [Tool for network monitoring and data acquisition]

  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+caps`](https://packages.gentoo.org/useflags/+caps)             Use Linux capabilities library to control privilege
  [`+samba`](https://packages.gentoo.org/useflags/+samba)           Add support for SAMBA (Windows File and Printer sharing)
  [`+smi`](https://packages.gentoo.org/useflags/+smi)               Build with net-libs/libsmi to load MIBs on the fly to decode SNMP packets
  [`+ssl`](https://packages.gentoo.org/useflags/+ssl)               Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  [`suid`](https://packages.gentoo.org/useflags/suid)               Enable setuid root program(s)
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-05 00:24] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [tcpdump]:

`root `[`#`]`emerge --ask net-analyzer/tcpdump`

## [Configuration]

### [SUID]

In order for normal users to run [tcpdump] the program should be built with the `suid` flag enabled and the user(s) should be added to the pcap group.

`root `[`#`]`USE="suid" emerge -a --changed-use tcpdump`

Do this by using the [usermod] command where `<username>` is user\'s username:

`root `[`#`]`usermod -a -G pcap <username>`

## [Usage]

### [Invocation]

The root user can invoke [tcpdump] at any time:

`root `[`#`]`tcpdump -h`

    Usage: tcpdump [-aAbdDefhHIJKlLnNOpqRStuUvxX#] [ -B size ] [ -c count ]
                    [ -C file_size ] [ -E algo:secret ] [ -F file ] [ -G seconds ]
                    [ -i interface ] [ -j tstamptype ] [ -M secret ] [ --number ]
                    [ -Q in|out|inout ]
                    [ -r file ] [ -s snaplen ] [ --time-stamp-precision precision ]
                    [ --immediate-mode ] [ -T type ] [ --version ] [ -V file ]
                    [ -w file ] [ -W filecount ] [ -y datalinktype ] [ -z command ]
                    [ -Z user ] [ expression ]

When [tcpdump] has been set with SUID permissions normal users can invoke it, however since the [/usr/sbin] directory is not included in a normal user\'s path, the full path must be specified:

`user `[`$`]`/usr/sbin/tcpdump`

### [Listing interfaces]

To discover the interfaces available to [tcpdump] issue the following command:

`user `[`$`]`/usr/sbin/tcpdump --list-interfaces`

### [Specifying an interface]

After an output of available interfaces has been displayed it is possible to select a specific interface upon which to listen:

`user `[`$`]`/usr/sbin/tcpdump -i <interface_name>`

Where `<interface_name>` is either the number of the interface or the string version of the name.

### [Write output to a file]

Running [tcpdump] with the `-w` instructs the program to write output to a file. This is helpful to future analysis:

`user `[`$`]`/usr/sbin/tcpdump -w /tmp/output`

### [Read input from a file]

`user `[`$`]`/usr/sbin/tcpdump -r /tmp/output`

### [Capture network traffic over ssh and wireshark]

`user `[`$`]`ssh foo@hostname.com 'tcpdump -s0 -c 1000 -nn -w - not port 22' | wireshark -k -i -`

## [Advanced Usage]

Low Output

`root `[`#`]`tcpdump -nnvvS`

Medium Output

`root `[`#`]`tcpdump -nnvvXS`

Heavy Output

`root `[`#`]`tcpdump -nnvvXSs `

Heavy Output and maximally human-readable timestamp

`root `[`#`]`tcpdump -ttttnnvvXSs `

Show all URG packets

`root `[`#`]`tcpdump 'tcp[13] & 32 != 0'`

Show all ACK packets

`root `[`#`]`tcpdump'tcp[13] & 16 != 0'`

Show all PSH packets

`root `[`#`]`tcpdump 'tcp[13] & 8 != 0'`

Show all RST packets

`root `[`#`]`tcpdump'tcp[13] & 4 != 0'`

Show all SYN packets

`root `[`#`]`tcpdump'tcp[13] & 2 != 0'`

Show all FIN packets

`root `[`#`]`tcpdump'tcp[13] & 1 != 0'`

Show all SYN-ACK packets

`root `[`#`]`tcpdump 'tcp[13] = 18'`

Show all traffic with both SYN and RST flags set: (that should never happen)

`root `[`#`]`tcpdump'tcp[13] = 6'`

Show all traffic with the "evil bit" set

`root `[`#`]`tcpdump 'ip[6] & 128 != 0'`

Display all IPv6 Traffic

`root `[`#`]`tcpdump ip6`

Print Captured Packets in ASCII

`root `[`#`]`tcpdump -A -i eth0`

Display Captured Packets in HEX and ASCII

`root `[`#`]`tcpdump -XX -i eth0`

Capture and Save Packets in a File

`root `[`#`]`tcpdump -w 0001.pcap -i eth0`

Read Captured Packets File

`root `[`#`]`tcpdump -r 0001.pcap`

Capture IP address Packets

`root `[`#`]`tcpdump -n -i eth0`

Capture only TCP Packets.

`root `[`#`]`tcpdump -i eth0 tcp`

Capture Packet from Specific Port

`root `[`#`]`tcpdump -i eth0 port 22`

Capture Packets from source IP

`root `[`#`]`tcpdump -i eth0 src 192.168.0.2`

Capture Packets from destination IP

`root `[`#`]`tcpdump -i eth0 dst 50.116.66.139`

Capture any packed coming from x.x.x.x

`root `[`#`]`tcpdump -n src host x.x.x.x`

Capture any packet coming from or going to x.x.x.x

`root `[`#`]`tcpdump -n host x.x.x.x`

Capture any packet going to x.x.x.x

`root `[`#`]`tcpdump -n dst host x.x.x.x`

Capture any packed coming from x.x.x.x

`root `[`#`]`tcpdump -n src host x.x.x.x`

Capture any packet going to network x.x.x.0/24

`root `[`#`]`tcpdump -n dst net x.x.x.0/24`

Capture any packet coming from network x.x.x.0/24

`root `[`#`]`tcpdump -n src net x.x.x.0/24`

Capture any packet with destination port x

`root `[`#`]`tcpdump -n dst port x`

Capture any packet coming from port x

`root `[`#`]`tcpdump -n src port x`

Capture any packets from or to port range x to y

`root `[`#`]`tcpdump -n dst(or src) portrange x-y`

Capture any tcp or udp port range x to y

`root `[`#`]`tcpdump -n tcp(or udp) dst(or src) portrange x-y`

Capture any packets with dst ip x.x.x.x and port y

`root `[`#`]`tcpdump -n "dst host x.x.x.x and dst port y"`

Print only useful packets from the HTTP traffic

`root `[`#`]`tcpdump -A -s 0 -q -t -i eth0 'port 80 and ( ((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12:2]&0xf0)>>2)) != 0)'`

Dump sip traffic

`root `[`#`]`tcpdump -nq -s 0 -A -vvv port 5060 and host 1.2.3.4`

Capture SMTP / POP3 Email

`root `[`#`]`tcpdump -nn -l port 25 | grep -i 'MAIL FROM\|RCPT TO'`

Capture ftp or ftp-data traffic

`root `[`#`]`tcpdump -vvAs0 port ftp or ftp-data`

Find SSH Connections

`root `[`#`]`tcpdump 'tcp[(tcp[12]>>2):4] = 0x5353482D'`

Find traffic with evil bits

`root `[`#`]`tcpdump 'ip[6] & 128 != 0'`

** Warning**\
Use this example for educational purposes only

Capture all the plaintext passwords

`root `[`#`]`tcpdump -i any port http or port ftp or port smtp or port imap or port pop3 or port telnet -l -A | egrep -i -B5 'pass=|pwd=|log=|login=|user=|username=|pw=|passw=|passwd=|password=|pass:|user:|username:|password:|login:|pass |user '`

### [Filter Showing Nmap NSE Script Testing]

On client

`root `[`#`]`nmap -p 80 --script=http-enum.nse targetip`

On Server

`root `[`#`]`tcpdump -nn port 80 | grep "GET /"`

\

## [See also]

-   [Metasploit](https://wiki.gentoo.org/wiki/Metasploit "Metasploit") --- provides information about security vulnerabilities and aids in penetration testing and IDS signature development.
-   [Nmap](https://wiki.gentoo.org/wiki/Nmap "Nmap") --- an open source recon tool used to check for open ports, what is running on those ports, and metadata about the daemons servicing those ports.
-   [Wireshark](https://wiki.gentoo.org/wiki/Wireshark "Wireshark") --- a free and open-source packet analyzer.

## [External resources]

-   [http://www.tcpdump.org/manpages/pcap.3pcap.html](http://www.tcpdump.org/manpages/pcap.3pcap.html) - The tcpdump man page hosted on the web.