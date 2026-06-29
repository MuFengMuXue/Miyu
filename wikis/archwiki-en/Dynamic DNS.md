# Dynamic DNS

According to Wikipedia:

:Dynamic DNS (DDNS or DynDNS) is a method of automatically updating a name server in the Domain Name System (DNS), often in real time, with the active DDNS configuration of its configured hostnames, addresses or other information.

:The term is used to describe two different concepts. The first is "dynamic DNS updating" which refers to systems that are used to update traditional DNS records without manual editing. These mechanisms are explained in RFC 2136, and use the TSIG mechanism to provide security. The second kind of dynamic DNS permits lightweight and immediate updates often using an update client, which do not use the RFC2136 standard for updating DNS records. These clients provide a persistent addressing method for devices that change their location, configuration or IP address frequently.

For RFC2136 there is  from . For dynamic DNS services there are several packages available, see #Update clients.

## Router
If the device needing DDNS sits behind a router, you should first check if the router itself can update any DDNS services. Although the selection of services may be limited, there are several advantages to using the router: it will probably be easier to set up, will require little to no maintenance, and will have no downtime (if the router is down you will not have Internet anyway).

## Update clients
Note that some dynamic DNS providers do not require a dedicated client and can be updated with cURL.

## Multi-service clients
*
*
*
*

## Single-service clients
*
*
*

## ddclient
 is compatible with many DDNS services and is the recommended tool for updating DDNS if your router is not an option. It includes systemd support.

After installing, edit the configuration file  to set up your DDNS provider (it includes many examples). Then enable and start .

The configuration can be tested by running  in the foreground:

 # ddclient --foreground --debug --verbose

Some of the compatible services are listed below, but you can also check the examples and protocols for more.

{| class="wikitable"
|+ ddclient compatible services
! Service
! Configuration notes
|-
! Now-DNS
| example
|-
! ChangeIP
| example
|-
! Duck DNS
| example
|-
! FreeDNS
| example
|-
! No-IP
| Use protocol , server
|-
! nsupdate.info
| Use protocol
|-
! Dyn DNS
| example
|-
! Namecheap
| example
|-
! Dynu
| example
|}

## Use an external website to determine IP address
If ddclient is unable to detect your IP address, you can configure ddclient to fetch your IP from an external webpage such as checkip.dyndns.org. This address is used by default when  is specified. It is also recommended to increase the check interval to avoid frequent requests to the IP check service:

An alternative IP check service can be specified with the  key:

## Use a local script to determine IPv6 address
ddclient often gets the wrong IPv6 address or none at all, but instead of an external website the IPv6 address can be determined locally. This script can be used:

{{hc|/usr/local/bin/get-ip|2=

#!/bin/sh
ip -6 -o addr show scope global | awk -F '[ \t]+|/' '$4 ~ /^23/ {print $4}'

}}

Make the script executable and tell ddclient to use it:

## Use UPnP or NAT-PMP to determine external IPv4 address
If your router supports UPnP, install  and use the external-ip utility:

For NAT-PMP, install  and create a script wrapping the  output.

Make the script executable and tell ddclient to use it:

## Other providers
Other DDNS providers are not compatible with ddclient so updating your IP with them may require a special tool or some custom scripting. Remember that if the service allows you to update your IP using the command line, you can automate the process using tools such as cron or systemd/Timers.
