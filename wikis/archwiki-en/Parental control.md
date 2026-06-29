# Parental control

Several methods exist to protect and limit child activity on a computer.

## Applications
*
*
*

## Restrict opening applications
 allows setting access restrictions for  based applications.

 malcontent-client set-app-filter timmy x-scheme-handler/http
This will disallow the user timmy from opening a web browser provided by Flatpak.

## Whitelist with Tinyproxy and Firehol
The following description will enable you to filter any user's access to the internet with a whitelist of url-s using  and  (or ).

 consists of the following changes:

 FilterURLs On
 FilterDefaultDeny Yes
 Filter "/etc/tinyproxy/whitelist"

 should hold the url's that will be only allowed accessed by selected users. A silly example:

 (www|wiki|static).archlinux.org
 google.com
 should contain the following line:
 transparent_proxy "80 443" 8888 "nobody root bin myaccount"
where myaccount is my account that should not be filtered by Tinyproxy.

## OpenDNS Parental Control
OpenDNS provides free DNS services as an alternative to your ISP's default servers. Furthermore, they provide optional filtering capabilities. Different levels of filtering is possible; see the OpenDNS main page for details.

For dynamic IP addresses, it is a good idea to keep them updated on OpenDNS. Use  and edit  as follows:

 # OpenDNS.com account-configuration
 use=web, web=myip.dnsomatic.com
 server=updates.opendns.com
 protocol=dyndns2
 login=myopendns@email.address
 password=myopendnspassword
 myhostname

You may sometimes even set up your router to use OpenDNS, therefore allowing protection spanning on all devices connected to that router.

## Editing /etc/hosts
You may configure your /etc/hosts file to block access to certain domains. A more draconian approach is to only allow domains explicitly stated in , as described here. If you do this, please remember that this will affect your whole system, so for example pacman may be unable to connect to the update server unless you make a proper binding in your .

## Blocklisting using named
See also: BIND

Create stub zone file ("/var/named/denied.zone") that redirects everything to localhost

 @                               1D IN SOA   ns1.example.com. root.example.com. (
                                    42    ; serial (yyyymmdd##)
                                    3H    ; refresh
                                    15M   ; retry
                                    1W    ; expiry
                                    1D )  ; minimum ttl
                                1D  IN  NS      ns.example.com.
                       1D  IN  A       127.0.0.1
                       1D  IN  AAAA    ::1

 *                      1D  IN  A       127.0.0.1
 *                      1D  IN  AAAA    ::1

Add
 zone "SOME-DOMAIN-1.TLD" IN { type master; file "denied.zone"; };
 ...
 zone "SOME-DOMAIN-N.TLD" IN { type master; file "denied.zone"; };
to named.conf.

Recent named versions support DoT and DoH, so you can expose named to internet and use it from outside your lan.
(For example Firefox can use DoH, android devices has global "private DNS server" setting for DoT)

## Squid
Squid  is feature reach proxy that supports authorization, caching, TLS bumping, transparency with firewall, access lists based on MAC, IP, domain, and TLS SNI.
It has separate article.
In combination with nftables, Squid can be used to fully control which websites can be browsed by the children (see https://archtemis.readthedocs.io/en/latest/network.html#parental-controls).

## Browser add-ons
Several add-ons exist for web browsers to filter web content. Some of them can even block out pages examining on their body, not only on their URL. Be warned, however, that this is not a very secure way. Starting Firefox in safe mode, messing with the Firefox profile directory or Firefox profile manager are obvious ways to attempt to shut down Firefox-based add-ons. If all else fails, the kid may simply use a different browser.
