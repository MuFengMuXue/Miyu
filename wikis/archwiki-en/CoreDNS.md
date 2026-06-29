# CoreDNS

CoreDNS is a DNS server/forwarder, written in Go, that chains plugins. Each plugin performs a (DNS) function making it very flexible. If some functionality is not provided out of the box you can add it by writing a plugin.

CoreDNS can listen for DNS requests coming in over UDP/TCP (Do53), DNS over TLS (DoT, RFC 7858) and DNS over HTTPS (DoH, RFC 8484).

## Installation
Install the  package.

## Configuration
See the documentation on configuration.

 will look for  and fail to start if the file is missing. After creating the configuration file in that location, Start/enable .

Below is an example configuration with useful plugins. CoreDNS will start on port , serve DNS to the listed subnets and forward everything to Wikimedia DNS servers. You can use drill command to verify that CoreDNS is working locally: .

{{hc|/etc/coredns/Corefile|2=
.:53 {
       bind 127.0.0.1 ::1 192.168.1.254 192.0.0.1
       bufsize 1232
       acl {
               allow net 192.168.0.0/16 172.16.0.0/12 10.0.0.0/8 192.0.0.0/24
               block
       }
       hosts {
               reload 0
               fallthrough
       }
       loadbalance
       forward . tls://185.71.138.138 tls://2001:67c:930::1 {
               tls_servername wikimedia-dns.org
       }
       cache {
               success 4096
               denial  1024
               prefetch 512
       }
       prometheus :9153
       errors
       log
}
}}

## Forwarding
To forward queries to a different resolver, use the forward plugin. It supports regular DNS and DNS over TLS. For DNS over TLS, use the  protocol and specify the server hostname with .

For example, to forward everything using DNS over TLS to Wikimedia DNS, edit  as follows:

{{hc|/etc/coredns/Corefile|
.:53 {
    bind 127.0.0.1 ::1
    forward . tls://185.71.138.138 tls://2001:67c:930::1 {
        tls_servername wikimedia-dns.org
    }
}
}}

Configure  and  as your nameserver; see Domain name resolution. Restart  after that.

Run  as root to verify things are working by default. The resolver will now listen on port .

If the resolver should be accessible from other hosts, configure other network interfaces or IP addresses in  with . Also the acl plugin can be used to block ranges that should be use the server for recursion. Refer to CoreDNS plugin documentation for more information.

If the resolver should respect entries from the  file, add a  line to . See .
