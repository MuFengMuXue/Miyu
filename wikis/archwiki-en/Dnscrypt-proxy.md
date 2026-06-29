# Dnscrypt-proxy

dnscrypt-proxy is a DNS proxy client with support for the encrypted DNS protocols DNS over HTTPS and DNSCrypt, which can be used to prevent man-in-the-middle attacks and eavesdropping. dnscrypt-proxy is also compatible with DNSSEC.

## Installation
Install the  package.

## Configuration
The default configuration file referred to is at .

## Startup
The service can be started in two mutually exclusive ways (i.e. only one of the two may be enabled):

# With the systemd service .
#* The  option must be configured (e.g. ) in the configuration file when using the service.
# Through socket activation using .
#* The  option must be set to empty (i.e. ) in the configuration file, since systemd is taking care of the socket configuration.

## Select resolver
By leaving  commented out in the configuration file, dnscrypt-proxy will choose the fastest server from the sources already configured under  The lists will be downloaded, verified, and automatically updated [https://github.com/jedisct1/dnscrypt-proxy/wiki/Configuration-Sources#what-is-the-point-of-these-lists. Thus, configuring a specific set of servers is optional.

To manually set which server is used, uncomment the  variable in the configuration file and select one or more of the servers. For example, to use Cloudflare's servers:

 server_names = 'cloudflare-ipv6'

A full list of resolvers is located at the upstream page or Github. If dnscrypt-proxy has run successfully on the system before,  will also contain a list. Look at the description for servers note which validate DNSSEC, do not log, and are uncensored. These requirements can be configured globally with the , ,  options.

## Modify resolv.conf and coordinate with other local domain name resolvers
Modify the resolv.conf file and replace the current set of resolver addresses with the loopback IP addresses and optionsNext, existing services doing domain name resolution must be configured not to overwrite the settings. See resolv.conf#Overwriting of /etc/resolv.conf for details.
They can be used, if they are configured to bind to different addresses than localhost and forward DNS requests to localhost port . For example, systemd-resolved uses address  by default.

## Disable any services bound to port 53
To see if any programs are using port , run:

 $ ss -lp 'sport = :domain'

If the output contains more than the first line of column names, you need to disable whatever service is using port . For example, NetworkManager may try to activate a resolver automatically, but other network managers may have analogous components. You are ready to proceed once the above command outputs nothing more than the header line:

 Netid State   Recv-Q  Send-Q   Local Address:Port     Peer Address:Port Process

## Start systemd service
Finally, start/enable the  unit or , depending on which method you chose above.

## Check if dnscrypt-proxy is working
Open the browser and head to [https://dnsleaktest.com DnsLeakTest and do an extended test, if the results show servers that you have set in the configuration files it means that dnscrypt-proxy is working, otherwise something is wrong.

## Tips and tricks
## Enabling, downloading and auto-updating filter lists / block lists
Configure filter list sources in /usr/share/dnscrypt-proxy/utils/generate-domains-blocklist/domains-blocklist.conf. For example:

 # NextDNS CNAME cloaking list
 https://raw.githubusercontent.com/nextdns/cname-cloaking-blocklist/master/domains
 # AdGuard Simplified Domain Names filter
 https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt
 # OISD.NL Big:
 https://big.oisd.nl/domainswild
 # HaGeZi Multi Pro
 https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/pro-onlydomains.txt
 # HaGeZi Thread Intelligence Feeds
 https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/tif-onlydomains.txt

Create a service to download & combine filter lists.
/etc/systemd/system/dnscrypt-filterlist-update.service:

 Description=DNSCrypt Filterlist Update

 [Service
 Type=oneshot
 User=root
 WorkingDirectory=/usr/share/dnscrypt-proxy/utils/generate-domains-blocklist/
 ExecStart=generate-domains-blocklist -a domains-allowlist.txt -o blocklist.txt ; sleep 2 ; systemctl restart dnscrypt-proxy.service

 WantedBy=multi-user.target

Create a time to run on boot but also every 5 hours.
/etc/systemd/system/dnscrypt-filterlist-update.timer:

 [Unit
 Description=Run 15min after boot and every 5 hours (DNSCrypt Filterlist Update)

 OnBootSec=15min
 OnUnitActiveSec=5h

 [Install
 WantedBy=timers.target

Enable the timer:
 systemctl daemon-reload
 systemctl enable dnscrypt-filterlist-update.timer

Configure DNSCrypt to apply the created filter rules.
/etc/dnscrypt-proxy/dnscrypt-proxy.toml:

 blocked_names_file = '/usr/share/dnscrypt-proxy/utils/generate-domains-blocklist/blocklist.txt'
 log_file = '/var/log/dnscrypt-proxy/blocked-names.log'

## Local DNS cache configuration
It is recommended to run dnscrypt-proxy as a forwarder for a local DNS cache if not using dnscrypt-proxy's cache feature; otherwise, every single query will make a round-trip to the upstream resolver. Any local DNS caching program should work. In addition to setting up dnscrypt-proxy, you must setup your local DNS cache program.

## Change port
In order to forward queries from a local DNS cache, dnscrypt-proxy should listen on a port different from the default , since the DNS cache itself needs to listen on  and query dnscrypt-proxy on a different port. Port number  is used as an example in this section.

There are two methods for changing the default port:

Socket method

Edit  with the following contents:

 ListenStream=
 ListenDatagram=
 ListenStream=127.0.0.1:54
 ListenStream=[::1:54
 ListenDatagram=127.0.0.1:54
 ListenDatagram=When queries are forwarded from the local DNS cache to ,  will start .

Service method

Edit the  option in  with the following:

 listen_addresses = ['127.0.0.1:54', '::1:54'

## Example local DNS cache configurations
The following configurations should work with dnscrypt-proxy and assume that it is listening on port .

## Unbound
Configure Unbound to your liking (in particular, see Unbound#Local DNS server) and add the following lines to the end of the  section in :

   do-not-query-localhost: no
 forward-zone:
   name: "."
   forward-addr: ::1@54
   forward-addr: 127.0.0.1@54

Restart  to apply the changes.

## dnsmasq
Configure dnsmasq as a local DNS cache. The basic configuration to work with dnscrypt-proxy:

If you configured dnscrypt-proxy to use a resolver with enabled DNSSEC validation, make sure to enable it also in dnsmasq:

Restart  to apply the changes.

## pdnsd
Install pdnsd. A basic configuration to work with dnscrypt-proxy is:

{{hc|/etc/pdnsd.conf|2=
global {
    perm_cache = 1024;
    cache_dir = "/var/cache/pdnsd";
    run_as = "pdnsd";
    server_ip = 127.0.0.1;
    status_ctl = on;
    query_method = udp_tcp;
    min_ttl = 15m;       # Retain cached entries at least 15 minutes.
    max_ttl = 1w;        # One week.
    timeout = 10;        # Global timeout option (10 seconds).
    neg_domain_pol = on;
    udpbufsize = 1024;   # Upper limit on the size of UDP messages.
}

server {
    label = "dnscrypt-proxy";
    ip = 127.0.0.1;
    port = 54;
    timeout = 4;
    proxy_only = on;
}

source {
    owner = localhost;
    file = "/etc/hosts";
}
}}

Restart  to apply the changes.

## Enable EDNS0
Extension Mechanisms for DNS that, among other things, allows a client to specify how large a reply over UDP can be.

Add the following line to your :

 options edns0

## Test EDNS0
Make use of the DNS Reply Size Test Server, use the drill command line tool to issue a TXT query for the name rs.dns-oarc.net:

 $ drill rs.dns-oarc.net TXT

With EDNS0 supported, the "answer section" of the output should look similar to this:

 rst.x3827.rs.dns-oarc.net.
 rst.x4049.x3827.rs.dns-oarc.net.
 rst.x4055.x4049.x3827.rs.dns-oarc.net.
 "2a00:d880:3:1::a6c1:2e89 DNS reply size limit is at least 4055 bytes"
 "2a00:d880:3:1::a6c1:2e89 sent EDNS buffer size 4096"

## Troubleshooting
## "read-only file system" or "no such file or directory" when caching file
Set the correct ownership of , usually .
