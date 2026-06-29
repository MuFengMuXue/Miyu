# Unbound

Unbound is a validating, recursive, and caching DNS resolver. According to Wikipedia:
:Unbound has supplanted the Berkeley Internet Name Domain (BIND) as the default, base-system name server in several open source projects, where it is perceived as smaller, more modern, and more secure for most applications.

## Installation
Install the  package.

Additionally, the  package is required for #DNSSEC validation.

## Configuration
A default configuration is already included at . The following sections highlight different settings for the configuration file. See  for other settings and more details.

Unless otherwise specified, any options listed in this section are to be placed under the  section in the configuration like so:

## Local DNS server
If you want to use unbound as your local DNS server, set your nameserver to the loopback addresses  and  in :

Make sure to protect  from modification as described in Domain name resolution#Overwriting of /etc/resolv.conf.

See Domain name resolution#Lookup utilities on how to test your settings.

Check specifically that the server being used is  or  after making permanent changes to resolv.conf.

You can now setup unbound such that it is #Forwarding queries, perhaps all queries, to the DNS servers of your choice.

## Root hints
For recursively querying a host that is not cached as an address, the resolver needs to start at the top of the server tree and query the root servers, to know where to go for the top level domain for the address being queried. Unbound comes with default builtin hints. Therefore, if the package is updated regularly, no manual intervention is required. Otherwise, it is good practice to use a root-hints file since the builtin hints may become outdated.

First point unbound to the  file:

 root-hints: root.hints

Then, put a root hints file into the unbound configuration directory. The simplest way to do this is to run the command:

When actually using this file, and not the builtin hints, it is a good idea to update  every six months or so in order to make sure the list of root servers is up to date. This can be done manually or by using a systemd timer. See #Roothints systemd timer for an example.

## DNSSEC validation
To use DNSSEC validation, the following setting for the server trust anchor should be under :

This setting is already enabled in the default configuration file.

 is copied from , which is provided by the  dependency, whose PKGBUILD generates the file with .

DNSSEC validation will only be done if the DNS server being queried supports it. If general #Forwarding queries have been set to DNS servers that do not support DNSSEC, their answers, whatever they are, should be considered insecure since no DNSSEC validation could be performed.

## Testing validation
To test if DNSSEC is working, after starting , do:

 $ unbound-host -vDr test.dnscheck.tools

The response should be the IP address with the word  next to it.

 $ unbound-host -vDr badsig.test.dnscheck.tools

Here the response should include .

Additionally you can use drill to test the resolver as follows:

 $ drill badsig.test.dnscheck.tools
 $ drill test.dnscheck.tools

The first command should give an  of . The second should give an  of .

## Forwarding queries
If you only want to forward queries to an external DNS server, skip ahead to #Forward all remaining requests.

## Allow local network to use DNS
## Using openresolv
If your network manager supports openresolv, you can configure it to provide local DNS servers and search domains to Unbound:

Run  to generate the file.

Configure Unbound to read the openresolv's generated file and allow replies with private IP address rangesAdditionally you may want to disable DNSSEC validation for private DNS namespaces (see RFC 6762 Appendix G):

## Exclude local subnets from answers
Will be useful to exclude local networks from DNS answers because it would protect against DNS rebinding attacks. By default this feature is not active but you can add any subnet you want in configuration file:

 private-address: local_subnet/subnet_mask

You can add all private and link-local subnets by this strings:

 private-address:  10.0.0.0/8
 private-address:  172.16.0.0/12
 private-address:  192.168.0.0/16
 private-address:  169.254.0.0/16
 private-address:  fd00::/8
 private-address:  fe80::/10

Note that Unbound may have adresses from excluded subnets in answers if they belong to domains from  or specified by , so you need to define  how described at #Using openresolv to able query local domains adresses.

## Include local DNS server
To include a local DNS server for both forward and reverse local addresses a set of lines similar to these below is necessary with a forward and reverse lookup (choose the IP address of the server providing DNS for the local network accordingly by changing 10.0.0.1 in the lines below):

 local-zone: "10.in-addr.arpa." transparent

This line above is important to get the reverse lookup to work correctly.

 forward-zone:
 name: "mynetwork.com."
 forward-addr: 10.0.0.1

 forward-zone:
 name: "10.in-addr.arpa."
 forward-addr: 10.0.0.1

You can set up the localhost forward and reverse lookups with the following lines:

 local-zone: "localhost." static
 local-data: "localhost. 10800 IN NS localhost."
 local-data: "localhost. 10800 IN SOA localhost. nobody.invalid. 1 3600 1200 604800 10800"
 local-data: "localhost. 10800 IN A 127.0.0.1"
 local-zone: "127.in-addr.arpa." static
 local-data: "127.in-addr.arpa. 10800 IN NS localhost."
 local-data: "127.in-addr.arpa. 10800 IN SOA localhost. nobody.invalid. 2 3600 1200 604800 10800"
 local-data: "1.0.0.127.in-addr.arpa. 10800 IN PTR localhost."

## Forward all remaining requests
## Using openresolv
If your network manager supports openresolv, you can [https://roy.marples.name/projects/openresolv/configuration/ configure it to provide upstream DNS servers to Unbound.

Run  to generate the file.

Finally configure Unbound to read the openresolv's generated fileinclude: "/etc/unbound/resolvconf.conf"

## Manually specifying DNS servers
To use specific servers for default forward zones that are outside of the local machine and outside of the local network add a forward zone with the name  to the configuration file. In this example, all requests are forwarded to Google's DNS servers:

 forward-zone:
   name: "."
   forward-addr: 8.8.8.8
   forward-addr: 8.8.4.4

## Forwarding using DNS over TLS
To use DNS over TLS, you will need to enable the  option, allow unbound to forward TLS requests and also specify any number of servers that allow DNS over TLS.

For each server you will need to specify the connection port using  and its domain name with . The domain name is required for TLS authentication and also allows setting stub-zones and using the  command with domain names. There should not be any spaces in the  specification.

## Access control
You can specify the interfaces to answer queries from by IP address. The default, is to listen on localhost.

To listen on all interfaces, use the following:

 interface: 0.0.0.0
 interface: ::0

To control which systems can access the server by IP address, use the  option:

 access-control: subnet action

For example:

 access-control: 192.168.1.0/24 allow

action can be one of  (drop message),  (polite error reply),  (recursive ok), or  (recursive and nonrecursive ok). By default everything is refused except for localhost.

## Usage
## Starting Unbound
Start/enable the  systemd service.

## Remotely control Unbound
unbound ships with the  utility which enables us to remotely administer the unbound server. It is similar to the pdnsd-ctl command of .

## Setting up unbound-control
Before you can start using it, the following steps need to be performed:

1) Firstly, you need to run the following command

 # unbound-control-setup

which will generate a self-signed certificate and private key for the server, as well as the client. These files will be created in the  directory.

2) After that, edit  and put the following contents in that. The  option is necessary, the rest can be adjusted as required.

 remote-control:
     # Enable remote control with unbound-control(8) here.
     # set up the keys and certificates with unbound-control-setup.
     control-enable: yes

     # what interfaces are listened to for remote control.
     # give 0.0.0.0 and ::0 to listen to all interfaces.
     control-interface: 127.0.0.1

     # port number for remote control operations.
     control-port: 8953

     # unbound server key file.
     server-key-file: "/etc/unbound/unbound_server.key"

     # unbound server certificate file.
     server-cert-file: "/etc/unbound/unbound_server.pem"

     # unbound-control key file.
     control-key-file: "/etc/unbound/unbound_control.key"

     # unbound-control certificate file.
     control-cert-file: "/etc/unbound/unbound_control.pem"

## Using unbound-control
Some of the commands that can be used with unbound-control are:

* print statistics without resetting them:
* dump cache to stdout:
* flush cache and reload configuration:

Please refer to  for a detailed look at the operations it supports.

## Tips and tricks
## Domain blacklisting
To blacklist a domain, use .

Save the blacklist as a separate file (e.g. ) for ease of management and include it from . For example:

{{Tip|
* In order to return some OK statuses on those hosts, you can change the 127.0.0.1 redirection to a server you control and have that server respond with empty 204 replies, see [https://www.shadowandy.net/2014/04/adblocking-nginx-serving-1-pixel-gif-204-content.htm this page
* To convert a hosts file from another source to the unbound format do: {{bc|$ grep '^0\.0\.0\.0' hostsfile  awk '{print "local-zone: \""$2"\" always_refuse"}' > /etc/unbound/blacklist.conf}}
* A list of potential sources for the blacklist can be found in OpenWrt's adblock package's README.
}}

## Adding an authoritative DNS server
For users who wish to run both a validating, recursive, caching DNS server as well as an authoritative DNS server on a single machine then it may be useful to refer to the wiki page NSD which gives an example of a configuration for such a system.  Having one server for authoritative DNS queries and a separate DNS server for the validating, recursive, caching DNS functions gives increased security over a single DNS server providing all of these functions. Many users have used Bind as a single DNS server, and some help on migration from Bind to the combination of running NSD and Bind is provided in the NSD wiki page.

## WAN facing DNS
It is also possible to change the configuration files and interfaces on which the server is listening so that DNS queries from machines outside of the local network can access specific machines within the LAN. This is useful for web and mail servers which are accessible from anywhere, and the same techniques can be employed as has been achieved using bind for many years, in combination with suitable port forwarding on firewall machines to forward incoming requests to the right machine.

## Roothints systemd timer
Here is an example systemd service and timer that update  monthly using the method in #Root hints:

Start/enable the  systemd timer.

## Keeping DNS cache always up to date
unbound supports prefetching where cached DNS entries are automatically updated before they expire to keep the cache always up to date. To quote the  man page, turning it on gives about 10 percent more traffic and load on the machine, but popular items do not expire from the cache. This is particularly useful on mobile links with high RTT.

To enable prefetching, add this under the  section:

 prefetch: yes

## Serving expired records
In March 2020, RFC 8767 was published that specifies when and how a resolver can serve stale data from its cache. If the data is unable to be authoritatively refreshed when the TTL expires, the record MAY be used as though it is unexpired. Since version 1.6.0, Unbound has the ability to answer with expired records.

To enable serving expired records, add this under the  section:

 serve-expired: yes
 serve-expired-ttl: 172800  # between 86400 (1 day) and 259200 (3 days)
 serve-expired-client-timeout: 1800  # RFC 8767 recommended value

## Troubleshooting
## Issues concerning num-threads
 mentions:

      outgoing-range:
              Number of ports to open. This number of file  descriptors  can  be  opened  per thread.

and some sources suggest that the  parameter should be set to the number of cpu cores. The sample  file merely has:

        # number of threads to create. 1 disables threading.
        # num-threads: 1

However it is not possible to arbitrarily increase  above  without causing unbound to start with warnings in the logs about exceeding the number of file descriptors. In reality for most users running on small networks or on a single machine it should be unnecessary to seek performance enhancement by increasing  above . If you do wish to do so then refer to official documentation and the following rule of thumb should work:

:Set  equal to the number of CPU cores on the system. E.g. for 4 CPUs with 2 cores each, use 8.

Set the  to as large a value as possible, see the sections in the referred web page above on how to overcome the limit of  in total. This services more clients at a time. With 1 core, try . With 2 cores, try . With 4 cores try . The  is best set at half the number of the .

Because of the limit on  thus also limits , it is better to compile with , so that there is no  limit on . If you need to compile this way for a heavy duty DNS server then you will need to compile the programme from source instead of using the  package.

## First lookup fails after start
Without a storage backend configured,  will start with a completely empty cache on every boot and every service (re)start. With an empty cache the first request will fire of a relatively large amount of queries to upstream/remote DNS servers. That number of requests will quickly hit an  quotum. The default  1.22.0 configuration limits the number of upstream queries to 128. Even a future release with a default of 200 will not solve this issue completely.

The result is that your first DNS lookup will fail, and the second lookup succeeds. With error logging enabled, you will see a message like:

 error: SERVFAIL : all servers for this domain failed, at zone 1.1.1.in-addr.arpa. no server to query no addresses for nameservers}}

In debug mode the log will show something like:

 debug: request 1.1.1.1.in-addr.arpa. has exceeded the maximum global quota on number of upstream queries 131}}

Change your unbound.conf and restart , to increase the default quotum to a more relaxed value according to other users experiencing this issue, for example:

 max-global-quota: 300

## Timeout on (recursive) lookup
Even with a 1 Gbit/s FTTH connection, the default  configuration might lead to timeouts on recursive lookups. In debug mode, log will show:

 debug: drop reply, it is older than discard-timeout

In case you want to wait a little longer for an answer then 1.9 seconds, the default time-out, change your :

 discard-timeout: 3800  # in milliseconds
