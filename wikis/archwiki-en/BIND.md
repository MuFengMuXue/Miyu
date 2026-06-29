# BIND

BIND (or named) is the most widely used Domain Name System (DNS) server.

## Installation
Install the  package.

Start/enable the  systemd unit.

To use the DNS server locally, use the  nameserver (meaning clients like Firefox resolve via 127.0.0.1), see Domain name resolution. This will however require you to #Allow recursion while a firewall might block outside queries to your local named.

## Configuration
BIND is configured in . The available options are documented in .

Reload the  unit to apply configuration changes.

## Enable rndc access
In order to control BIND using , you need to set up TSIG key for it and tell BIND to allow name server control with that key.

First, generate TSIG key for this purpose:

{{bc|
$ tsig-keygen console
key "console" {
    algorithm hmac-sha256;
    secret "secret";
};
}}

Copy the output to both  and .

In , append default name server connection:

{{hc|/etc/rndc.conf|
...
options {
    default-key "console";
    default-server 127.0.0.1;
    default-port 953;
};
}}

Allow  control from localhost in
:

{{hc|/etc/named.conf|
...
controls {
    inet 127.0.0.1 port 953 allow { 127.0.0.1; } keys { "console"; };
};
...
}}

Now you can use  to control the local DNS server. For example, to check server status:

Reloading server configuration can also be done by:

## Restrict access to localhost
BIND by default listens on port  of all interfaces and IP addresses. To only allow connections from localhost, add the following line to the  section in :

 listen-on { 127.0.0.1; };
 listen-on-v6 { ::1; };

## Set up DNS forwarding
To make BIND forward DNS queries to another DNS server, add the  clause to the  section.

For example, to make BIND forward to the Google Public DNS servers using DNS over TLS:

{{bc|
tls google {
    remote-hostname "dns.google";
};

options {
...
    forward only;
    forwarders port 853 tls google {
        8.8.8.8; 2001:4860:4860::8888;
        8.8.4.4; 2001:4860:4860::8844;
    };
};
}}

Specific zones can also be forwarded by defining a forward zone. This is useful if you want to resolve internal domains or domains that are otherwise not publicly accessible on the Internet:

{{bc|
zone domain.tld {
    type forward;
    forwarders {
        10.20.30.40;
        10.20.30.45;
    };
    forward only;
};
}}

## Serve DNS over TLS or HTTPS
To enable serving DNS over TLS or HTTPS in BIND, define a tls block specifying your certificate, then add listen-on clauses enabling DNS over TLS and HTTPS listeners (as well as a standard DNS listener).

{{hc|/etc/named.conf|2=
tls mycert {
    cert-file "path.crt";
    key-file "path.key";
};

options {
    // Standard port 53 listeners need to be re-added explicitly
    listen-on    { any; };
    listen-on-v6 { any; };

    // Add a DNS over TLS listener on standard port 853
    listen-on    tls mycert { any; };
    listen-on-v6 tls mycert { any; };

    // Add a DNS over HTTPS listener on standard HTTPS port 443
    listen-on    tls mycert http default { any; };
    listen-on-v6 tls mycert http default { any; };

    // If needed, add a cleartext HTTP listener for a reverse proxy
    //listen-on    port 8443 tls none http default { 127.0.0.1; };
    //listen-on-v6 port 8443 tls none http default { ::1; };
};
...
}}

Note that {{ic|tls{}}} is defined at the top level, not inside the {{ic|options{}}} block.

## A configuration template for running a domain
Following is a simple home nameserver being set up, using domain.tld as the domain being served world-wide like this wiki's archlinux.org domain is.

A more elaborate example is DNS server with BIND9, while this shows how to set up internal network name resolution.

## Creating a zonefile
Create .

 defines the default suffix for all names which do not already end with a  (dot), e.g.  will be expanded to  ⇒  everywhere.

 defines the default time-to-live (i.e. cache expiry time) for all records which do not have their own TTL specified. Here it is 2 hours.

Serial must be incremented manually before reloading named every time you change a resource record for the zone. Otherwise secondary servers (replicas or slaves) will not re-transfer the zone: they only do it if the serial is greater than that of the last time they transferred the zone. This example uses the somewhat common  format, but this is not required; the serial number can also just start at 1.

## Configuring primary server
Add your zone to :

{{bc|
 zone "domain.tld" IN {
         type primary;
         file "domain.tld.zone";
         allow-update { none; };
 };
}}

Reload the  unit to apply the configuration change.

## Configuring secondary server
In case you have two or more servers, you can set up all but one of them as secondary, where the zone is retrieved from primary via AXFR transfer.

On primary, explicitly allow zone transfers from secondary:

{{bc|
zone "domain.tld" IN {
        ...
        allow-transfer { 198.51.100.5; 20001:db8:113::4; };
};
}}

On secondary, add the zone to :

{{bc|
zone "domain.tld" IN {
        type secondary;
        file "domain.tld.zone";
        primaries { 203.0.113.4; 2001:db8:113::4; };
};
}}

Reload  or use  to reload both primary and secondary servers configuration.

## Allow recursion
If you are running your own DNS server, you may want it to perform recursive lookups (i.e., resolve domains it is not authoritative for) on behalf of clients — either for your own machine or for a local network. This requires enabling recursion in BIND and carefully limiting which clients are allowed to use it.

By default, to mitigate DNS amplification attacks, recursion is disabled for all clients except the loopback interface in the default Arch . This is typically configured with:

 allow-recursion { 127.0.0.1; ::1; };

To allow recursive queries from clients on your LAN (e.g., 192.168.0.0/24), you must explicitly define an ACL and use it with  and . For example:

{{hc|/etc/named.conf|
acl "trusted" {
    127.0.0.1;
    ::1;
    192.168.0.0/24;
    fd01:2345:6789::/64;
};
options {
    // Allow authoritative queries from any client
    allow-query       { any; };
    // Allow recursive lookups and cached results only for trusted clients
    allow-recursion   { trusted; };
    allow-query-cache { trusted; };
};
}}

This setup permits:

* Authoritative responses (for zones this server is responsible for) to anyone.
* Recursive lookups and cached results only to trusted clients on your local network and loopback interfaces.

See What has changed in the behavior of "allow-recursion" and "allow-query-cache"?

## Configuring BIND to serve DNSSEC signed zones
BIND makes it easy to serve DNSSEC-signed zones with Key and Signing Policy (KASP) facility, where it takes care of zone signing and key management automatically for you using user-defined policy.

Create separate directory to store keys, writable by the server:

Instruct BIND to store keys in aforementioned directory:

{{hc|/etc/named.conf|
options {
    ...
    key-directory "/var/named/keys";
    ...
};
}}

Now zones can be signed by applying the desired policy. In most cases, you can apply up-to-date DNSSEC best practices with  policy:

{{hc|/etc/named.conf|
zone "domain.tld" IN {
        ...
        dnssec-policy default;
};
}}

This will sign the zone with single  combined signing key (CSK) with unlimited key lifetime, signed via  where the server generates the signed zone separately without having to set-up dynamic DNS.

If needed, a custom policy can be defined with  block. For example, the  policy signs the zone with traditional key signing key (KSK, rotated yearly) and zone signing key (ZSK, rotated monthly) split, alongside with timing parameters and NSEC3 denial-of-existence:

{{hc|/etc/named.conf|
dnssec-policy main {
    keys {
        ksk lifetime P1Y algorithm ecdsap256sha256;
        zsk lifetime P1M algorithm ecdsap256sha256;
    };
    publish-safety 1h;
    retire-safety 1h;
    purge-keys 1h;
    signatures-refresh P3D;
    signatures-validity P3W;
    signatures-validity-dnskey P3W;
    inline-signing yes;
    nsec3param iterations 0 optout no salt-length 0;
};
...
}}

The custom policy can be applied in the same way as default policy earlier:

{{hc|/etc/named.conf|
zone "domain.tld" IN {
    ...
    dnssec-policy main;
};
}}

Increment the zone's serial and reload the server configuration.

The last step is to establish chain of trust with parent zone. First, check DNSSEC status of the zone:

Here, the KSK key ID is 58785. Yours will be different.

Generate the DS record (replace key ID as appropriate):

Submit DS to the parent zone (for example, by filling the web form on your registrar).

When you've confirmed that the DS record has been published in the parent zone, you can signal BIND as such by:

## Custom trust anchors
In case your DNSSEC-signed zone is internal and you need to take advantage of DNSSEC validation, you need to instead add its trust anchor to resolvers that will be used to resolve it. This can be done by adding  block:

{{hc|/etc/named.conf|
trust-anchors {
    . initial-key 257 3 8 "AwEAAa96jeuknZlaeSrvyAJj6ZHv28hhOKkx3rLGXVaC6rXTsDc449/cidltpkyGwCJNnOAlFNKF2jBosZBU5eeHspaQWOmOElZsjICMQMC3aeHbGiShvZsx4wMYSjH8e7Vrhbu6irwCzVBApESjbUdpWWmEnhathWu1jo+siFUiRAAxm9qyJNg/wOZqqzL/dL/q8PkcRU5oUKEpUge71M3ej2/7CPqpdVwuMoTvoB+ZOT4YeGyxMvHmbrxlFzGOHOijtzN+u1TQNatX2XBuzZNQ1K+s2CXkPIZo7s6JgZyvaBevYtxPvYLw4z9mR7K2vaF18UYH9Z9GNUUeayffKC73PYc";
    . initial-key 257 3 8 "AwEAAaz/tAm8yTn4Mfeh5eyI96WSVexTBAvkMgJzkKTOiW1vkIbzxeF3+/4RgWOq7HrxRixHlFlExOLAJr5emLvN7SWXgnLh4+B5xQlNVz8Og8kvArMtNROxVQuCaSnIDdD5LKyWbRd2n9WGe2R8PzgCmr3EgVLrjyBxWezF0jLHwVN8efS3rCj/EWgvIWgb9tarpVUDK/b58Da+sqqls3eNbuv7pr+eoZG+SrDK6nWeL3c6H5Apxz7LjVc1uTIdsIXxuOLYA4/ilBmSVIzuDWfdRUfhHdY6+cn8HFRm+2hM8AnXGXws9555KrUB5qihylGa8subX2Nn6UwNR1AkUTV74bU";
    domain.tld. initial-ds 58785 13 2 "hash";
};
}}

## Automatically listen on new interfaces
By default, BIND scans for new interfaces and stops listening on interfaces which no longer exist every hour. You can tune this value by adding:

{{hc|/etc/named.conf|
options {
    interface-interval rescan-timeout-in-minutes;
};
}}

The max value is 28 days (40320 min). You can disable this feature by setting its value to 0.

Then restart the service.

## Running BIND in a chrooted environment
Running in a chroot environment is not required but improves security.

## Creating the jail house
In order to do this, we first need to create a place to keep the jail, we shall use , and then put the required files into the jail.

 # mkdir -p /srv/named/{dev,etc,usr/lib/engines,var/{run,log,named}}

Copy over required system files:

 # cp -av /etc/{localtime,named.conf} /srv/named/etc/
 # cp -av /usr/lib/engines-1.1/* /srv/named/usr/lib/engines/
 # cp -av /var/named/* /srv/named/var/named/.

Set up required nodes in :

 # mknod /srv/named/dev/null c 1 3
 # mknod /srv/named/dev/random c 1 8

Set ownership of the files:

 # chown -R named:named /srv/named

This should create the required file system for the jail.

## Service unit
Next we need a replacement unit file so that the service calls bind which will allow force bind into the chroot:

Now, reload systemd with daemon-reload, and start the .

## Serve the root zone locally
If you do not want to rely on third-party DNS services, you can serve the root zone locally following RFC:7706. This can be achieved by using BIND as a DNS recursive resolver.

To manage a recursive resolver, you typically need to configure a root hints file. This file contains the names and IP addresses of the authoritative name servers for the root zone.

Grab the file from IANA website and place it into .

Edit your server config, adding the respective file:

{{hc|/etc/named.conf|
zone "." IN {
    type hint;
    file "named.root";
};
}}

Recursion also should be allowed in the config. See #Allow recursion.
