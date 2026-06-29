# Uncomplicated Firewall

From the project home page:
:Ufw stands for Uncomplicated Firewall, and is a program for managing a netfilter firewall. It provides a command line interface and aims to be uncomplicated and easy to use.

## Installation
Install the  package.

Start and enable  to make it available at boot. Note that this will not work if  is also enabled (and same for its ipv6 counterpart).

## Basic configuration
A very simplistic configuration which will deny all by default, allow any protocol from inside a 192.168.0.1-192.168.0.255 LAN, and allow incoming Deluge and rate limited SSH traffic from anywhere:

 # ufw default deny
 # ufw allow from 192.168.0.0/24
 # ufw allow Deluge
 # ufw limit ssh

To allow a port instead from anywhere use the following example to allow port 51312 UDP and TCP, port 51312 only UDP or a port range from 51312 to 51314:

 # ufw allow 51312
 # ufw allow 51312/udp
 # ufw allow 51312:51314

The next line is only needed once the first time you install the package:

 # ufw enable

Finally, query the rules being applied via the status command:

Extra information, including the default policies, can be seen with
 # ufw status verbose
but this is still limited to user-specified rules. In order to see all rules setup
 # ufw show raw
may be used, as well as further reports listed in the manpage. Since these reports also summarize traffic, they may be somewhat difficult to read. Another way to check for accepted traffic:
 # iptables -S | grep ACCEPT
 # ip6tables -S | grep ACCEPT
While this works just fine for reporting, keep in mind not to enable the  service as long as you use  for managing it.

## Forward policy
Users needing to run a VPN such as OpenVPN or WireGuard can adjust the DEFAULT_FORWARD_POLICY variable in  from a value of "DROP" to "ACCEPT" to forward all packets regardless of the settings of the user interface. To forward for a specific interface like wg0, user can add the following line in the *filter block

You may also need to uncomment

## Adding other applications
The PKG comes with some defaults based on the default ports of many common daemons and programs.  Inspect the options by looking in the  directory or by listing them in the program itself:

 # ufw app list

If users are running any of the applications on a non-standard port, it is recommended to simply make  containing the needed data using the defaults as a guide.

Example, deluge with custom tcp ports that range from 20202-20205:

Should you require to define both tcp and udp ports for the same application, simply separate them with a pipe as shown: this app opens tcp ports 10000-10002 and udp port 10003:
 ports=10000:10002/tcp|10003/udp

One can also use a comma to define ports if a range is not desired.  This example opens tcp ports 10000-10002 (inclusive) and udp ports 10003 and 10009

 ports=10000:10002/tcp|10003,10009/udp

## Deleting applications
Drawing on the Deluge/Deluge-my example above, the following will remove the standard Deluge rules and replace them with the Deluge-my rules from the above example:

 # ufw delete allow Deluge
 # ufw allow Deluge-my

Query the result via the status command:

## Black listing IP addresses
It might be desirable to add ip addresses to a blacklist which is easily achieved simply by editing  and inserting an iptables DROP line at the bottom of the file right above the "COMMIT" word.

## Rate limiting with ufw
ufw has the ability to deny connections from an IP address that has attempted to initiate 6 or more connections in the last 30 seconds.  Users should consider using this option for services such as SSH.

Using the above basic configuration, to enable rate limiting we would simply replace the allow parameter with the limit parameter.  The new rule will then replace the previous.

## User rules
All user rules are stored in  and  for IPv4 and IPv6 respectively.

## Tips and tricks
## Disable remote ping
Change  to  in the following lines:

If you use IPv6, related rules are in .

## Disable IPv6 handling
Change  to  in  and reload rules. This removes previously-generated rules as well as generation of new ones.

## Disable UFW logging
Disabling logging may be useful to stop UFW filling up the kernel (dmesg) and message logs:

 # ufw logging off

## UFW and Docker
Docker in standard mode writes its own iptables rules and ignores ufw ones, which could lead to security issues. A solution can be found at https://github.com/chaifeng/ufw-docker.

## GUI frontends
If you are using KDE Plasma, you can just go to Wi-Fi & Networking > Firewall to access and adjust firewall configurations given  is installed.

## Gufw
 is a GTK front-end for Ufw that aims to make managing a Linux firewall as accessible and easy as possible. It features presets for common ports and p2p applications. It requires , , and GTK support.
