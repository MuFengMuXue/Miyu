# Nmap

From the official website:

:Nmap (“Network Mapper”) is an open source tool for network exploration and security auditing. It was designed to rapidly scan large networks, although it works fine against single hosts. Nmap uses raw IP packets in novel ways to determine what hosts are available on the network, what services (application name and version) those hosts are offering, what operating systems (and OS versions) they are running, what type of packet filters/firewalls are in use, and dozens of other characteristics. While Nmap is commonly used for security audits, many systems and network administrators find it useful for routine tasks such as network inventory, managing service upgrade schedules, and monitoring host or service uptime.

## Installation
Install the  package.

Nmap has a GUI called  that can be installed separately, but this article will cover only command-line usage.

## Usage
See .

## Specifying the target
There are a number of ways to tell Nmap the list of IP addresses to scan.  The simplest form is to just pass the address or domain name:

 $ nmap scanme.nmap.org
 $ nmap 74.207.244.221

## Specifying multiple targets
Using CIDR notation, for example to scan all 256 addresses beginning with :

 $ nmap 10.1.1.0/24

Using the dash, for example to scan ,  and :

 $ nmap 10.1.50-52.1

Using commas (does what you expect):

 $ nmap 10.1.50,51,52,57,59.1

All combined:

 $ nmap 10.1,2.50-52.1/30 10.1.1.1 10.1.1.2

## List scan
The list scan option () is useful for making sure that correct addresses are specified before doing the real scan:

 $ nmap -sL 10.1,2.50-52.1/30 10.1.1.1 10.1.1.2

List scan simply prints the specified addresses without sending a single packet to the target.

## Default options
If you specify only an IP address or domain name and no other options:

 $ nmap 74.207.244.221

Nmap will do the following:

# The IP address is reverse-DNS resolved to domain name, or vice-versa in case a domain name is specified (to disable, pass )
# Ping scanning using TCP ACK:80 and ICMP.  This is equivalent to  (to disable, pass )
# Scans the host(s)'s top 1000 most popular ports.  When running as root, SYN stealth scan is used.  When running as user, connect scan is used.

## Ping scan
Ping scanning (host discovery) is a technique for determining whether the specified computers are up and running.  Nmap performs ping scan by default before port scan to avoid wasting time on hosts that are not even connected.  To instruct Nmap to only perform ping scan:

 $ nmap -sn 10.1.1.1/8

This will cause Nmap to ping every one of the specified addresses and then report the list of hosts which did respond to the ping.

Nmap uses different kinds of ping packets when run with user or root privileges and when scanning the same or different subnets:

{| class="wikitable"
!
! External IP
! Local IP
|-
! User privileges
| TCP SYN at ports 80 & 443
| TCP SYN at ports 80 & 443 and ARP
|-
! Root privileges
| TCP SYN at ports 80 & 443 and IGMP
| ARP
|}

## Ping scan types
{| class="wikitable"
! Option     || Ping scan type
|-
|  || Disable ping scan entirely
|-
|  || TCP SYN (default at port 80)
|-
|  || TCP ACK (default at port 80)
|-
|  || UDP
|-
|  || SCTP INIT
|-
|  || ICMP Echo
|-
|  || ICMP timestamp
|-
|  || ICMP address mask
|-
|  || Other IP protocol
|-
|  || ARP scan
|}

 is useful when the machine is heavily firewalled, TCP 80 and 443 ports and IGMP requests are blocked, but the IP address might still have a machine listening on other less common ports.

## Port scan
There are 3 main states a port can be in:

*  - there is a program listening and responding to requests on this port
*  - the host replies with an "error: no program listening on this port" reply to requests to this port
*  - the host doesn't reply at all.  This can be due to restrictive firewall rules, which "drop" a packet without sending a reply

In addition to these there are 3 more states that Nmap can classify a port.  These are used when Nmap cannot reliably determine the state but suspects two of the three possible states:

*  () - the port is either open or closed
*  - the port is either closed or filtered
*  - the port is either open or filtered

By default Nmap scans the 1000 most popular ports found in .  To specify a different number of common ports:

 $ nmap --top-ports 1000 10.1.1.1

To specify custom port numbers, use :

 $ nmap -p -25,135-137 10.1.1.1

Dashes and commas work just like in #Specifying the target. In addition, it is possible to specify all ports before/after given one by skipping the starting/ending port when using a dash.  For example to scan all possible 65535 ports (except port number 0):

 $ nmap -p -

## Scan types
{| class="wikitable"
! Option     || Port scan type
|-
|  || Ping scan only
|-
|  || TCP SYN (stealth) (Default as root)
|-
|  || TCP connect (Default as user)
|-
|  || TCP ACK
|-
|  || TCP FIN
|-
|  || TCP FIN, SYN, ACK
|-
|  || TCP window
|-
|  || TCP Maimon
|-
|  || UDP scan
|-
|  || Idle scan
|-
|   || FTP bounce scan
|-
|  || Other IP protocol
|}

## Anti-scanning techniques
## iptables PSD module
PSD is an extension module of iptables. It is used on some linux-based commercial routers as well.

It has 4 parameters:

* , default value:
: Total weight of the latest TCP/UDP packets with different destination ports coming from the same host to be treated as port scan sequence.
* , default value:  (3 seconds)
: Delay (in hundredths of second) for the packets with different destination ports coming from the same host to be treated as possible port scan subsequence.
* , default value:
: Weight of the packet with privileged (=1024) destination port.

The principle behind PSD is simple. If requests from a single IP have gained a value more than threshold in delay seconds, then the IP is classified as a port scanner. In a math expression:

 lo_ports_weight * REQUESTS_LOW + hi_ports_weight * REQUESTS_HIGH >= threshold

where

 REQUESTS_LOW = number of requests to privileged (0 to 1023) ports within last delay seconds
 REQUESTS_HI = number of requests to non-privileged (1024 to 65535) ports within last delay seconds

Here are some examples:

* With default parameters, if at least 7 privileged ports are hit within 3 seconds, it is classified as a port scan.
* With default parameters, if at least 21 non-privileged ports are hit withing 3 seconds, it is classified as a port scan.
* With default parameters, if 4 privileged ports and 9 non-privileged ports are hit within 3 seconds, it is classified as a port scan, because .

## Avoiding detection
One of the simplest ways to avoid PSD is to simply scan slowly. For default values this parameter would suffice:

 $ nmap --scan-delay 3.1 192.168.56.1

Another interesting fact about PSD is that it does not detect a request as a port scan when the  or  flags are set (See the function  in xt_psd.c)

Also, if you are port scanning a host and the latter has an HTTP(S) service running on it, nmap will use  as default user agent. Your action will thus be easily detected, especially if an administrator or a robot are taking measures if such an user agent appears in the logs. Thankfully, nmap allows us to change that string easily: just pass .== Tips and tricks ==

## Limiting scan speed
Nmap scans are fast. While this is often a desirable feature, it can be counter-productive as well. For example when you want to test your system's firewall without disabling any activated flood detection rules, or when you want to run a long-term test for a specific port/service. The following options specify how fast Nmap sends packets.

To send a packet at most every 3.333 seconds:

 $ nmap --max-rate 0.3 192.168.56.1

Alternatively, to send a packet every 3.1 seconds:

 $ nmap --scan-delay 3.1 192.168.56.1

For other timing and parallelization options, see .

## Specify targets input from a list file
Often it is necessary to scan a large number of non-adjacent addresses.  Passing them on the command line is usually not convenient.  For this reason Nmap supports input from a list file ():

 $ nmap -iL addresses.txt

Addresses in the file must be separated with a whitespace.

Alternatively, Nmap can read the list from standard input (the  means standard input in many command-line programs):

 $ echo "10.1.1.1 10.1.1.2 10.1.1-10.3" | nmap -iL -

## Specify targets to exclude from scan
 $ nmap 10.1.1.1-10 --exclude 10.1.1.5,7

The same from a file:

 $ nmap 10.1.1.1-10 --excludefile excludeaddr.txt

## Spoofing
To spoof source IP:

 $ nmap -S 192.168.56.35 -e vboxnet0 192.168.56.11

To spoof the source MAC address:

 $ nmap --spoof-mac 01:02:03:04:05:06 192.168.56.11

To spoof source port:

 $ nmap --source-port 22 192.168.56.11

## Speeding up the scan
By default, Nmap performs DNS/reverse-DNS resolution on targets.  To tell Nmap never do any DNS resolution, pass the  option:

 $ nmap -n 192.168.56.0/24

This will speed the scan about 2 times.

## Scan port number 0
By default port 0 is skipped from scans, even if  is specified.  To scan it, it must be explicitly specified.  For example to scan every possible port:

 $ nmap -p 0-65535

Remember that this port number is invalid in RFC standards.  However it can be used by malware and the like to avoid more naive port scanners.

## File output formats
Nmap has built-in support for for file output alongside with terminal output:

*
: Normal output, same as the terminal output
*
: XML output, contains very detailed information about the scan, easy to parse with software
*
: Grepable output, deprecated
*
: All of the above combined. Creates files called ,  and

For example to output to the terminal, to file and to XML file:

 $ nmap -oN output.txt -oX output.xml scanme.nmap.org
