# DNS over HTTPS servers

DNS, since its inception, has been unencrypted on UDP/53, and later TCP/53, making it susceptible to snooping attacks. For additional information on the available protocols that can be used to address this vulnerability, see Domain name resolution#Privacy and security. This article covers two of the three available protocols for DNS servers with the necessary proxy configuration to provide both DNS over HTTPS (DoH) and DNS over TLS (DoT). Multiple DoH utilities are available in the AUR including ,  and . Which of the available solutions is appropriate, depends on the needs of your network.

 provides both a caching, non-authoritative DNS server, and DoH services (citation needed).

,  all provide an HTTP listener for proxying behind your existing HTTPS server, and a stub resolver to forward regular queries on UDP/53 to a secure DNS server. Additionally,  provide a standalone HTTPS/2 server.

## DoH server/proxy software configuration
## coreDNS
Install the  package.

You can use coreDNS as DoH/DoT/gRPC DNS server and/or DoT proxy. Default configuration file should be located at .

The example of simple configuration file looks like this:

{{hc|/etc/coredns/Corefile|
protocol://domain:port {
    forward domain forward_to
    tls_servername domain_of_dot_server
    tls cert_path key_path
}
}}

First string is listener, you can use next protocols:  for plain DNS protocol,  for DNS over HTTPS,  for DNS over TLS and  for gRPC (see If you leave protocol empty (e.g. example.com:53), dns:// will be choosen as default. The  is for matching queried domains, you can use specific one (e.g. dns: //example.com: 53) or use  (e.g. dns: //.: 53) to match all domains. And by  you can set listening port, you can leave it empty and will be chosen 53 port.

 string is for where DNS query will be forward. Use  for  to match all domains. In  set upstream DNS server where to send queries, you can specify  protocol for DoT server. If you using upstream DoT server, you need to set  for TLS negotiation.

 string mandatory if you use DoH, DoT or gRPC protocols. Put here certificate and private key paths in given order.

Example of configuration simple DoT proxy listening 53 port and using Cloudflare DoT server

{{hc|/etc/coredns/Corefile|
. {
    forward . tls://1.1.1.1 {
        tls_servername cloudflare-dns.com
    }
}
}}

Also, you can use several instances and forward plugins:

{{hc|/etc/coredns/Corefile|
https://.:443 {
    forward . 127.0.0.1 {
    forward example1.com 8.8.8.8
    tls cert.pem key.pem
}

tls://example2.com:853 {
    tls cert.pem key.pem
    forward . tls://9.9.9.9 {
        tls_servername dns.quad9.net
    }
}
}}

Start/enable the  unit.

## dns-over-https
At first, install  and after setting will not forget to enable and start needed service.

## Stub resolver
You can start using it right after install with default settings. Defaults ports for listening is 53 and 5380, if one of them is already binded, it will be ignored. Start/enable .

Configuration file locate at . You can change desired ports at section . There are many included third-parted DoH servers in configuration file, you need just uncomment one you needed or write unspecified. You can use several resolvers as well. One of them will be chosen randomly for each request. To force dns-over-https use resolvers in the required order set  to  or  and change weight value at resolvers in use.

## DoH proxy
Configuration file for use as doh server locate at . At  section can set desired upstream resolver and its protocol for use. You can use dns-over-https as standalone service or together with HTTPS services like nginx or apache.

For standalone use you need to set port to 443 and specify proper cert and key:

If you want use HTTP server for caching or using along with other HTTPS services leave empty cert and key strings in  and use next examples for configuration desired HTTP server. Note that there using default dns-over-https port.

nginx:

{{hc|/etc/nginx/nginx/site-available/doh|
server {
  listen       443 ssl http2 default_server;
  listen       [:::443 ssl http2 default_server;
  server_name  MY_SERVER_NAME;

  ssl_certificate /path/to/your/server/certificates/fullchain.pem;
  ssl_certificate_key /path/to/your/server/certificates/privkey.pem;
  location /dns-query {
    proxy_pass       http://localhost:8053/dns-query;
    proxy_set_header Host      $host;
    proxy_set_header X-Real-IP $remote_addr;
  }
}
}}

caddy:

{{hc|/etc/caddy/Caddyfile|
MY_SERVER_NAME {
        reverse_proxy * localhost:8053
        tls my@email.address
        try_files {path} {path}/index.php /index.php?{query}
}
}}

apache:

After setting up, start/enable .

## doh-proxy
## Standalone DNS server configuration
## BIND
BIND 9.18 natively supports serving both DNS over HTTPS and DNS over TLS. See BIND#Configuration for details.

## As resolver, with TLS proxy
Typical: If using ISC bind as the current DNS provider, and you will be providing both forwarding services for legacy clients and DoH to modern clients, you will likely want to configure named to forward all non-local queries to your stub resolver, comment out any forwarding lines to forward to the stub resolver (omit forward only if you would like to fall back to roots):

{{hc|/etc/named.conf|
options {
...
    //forwarders { 8.8.8.8; 8.8.4.4; };
    forwarders { 127.0.0.1 port 54; };
    forward only;
...
};
...}}

If you want to forward to an external TLS proxy (via stunnel), do the same but use only TCP/54 (see stunnel configuration below):

{{hc|/etc/named.conf|
options {
...
    //forwarders { 8.8.8.8; 8.8.4.4; };
    forwarders { 127.0.0.1 port 54; };
    forward only;
...
};
...
server 127.0.0.1 {
    tcp-only yes;
};
...}}

Optional: If using ISC bind as the current DNS provider, and you will be providing both forwarding services for legacy clients and DoH to modern clients, you might want to configure named to listen on an alternate port, for example TCP|UDP/54, rather than the default of 53 so that your stub resolver will listen on the standard port. Comment out any existing 'listen' lines and add the following (omit the v6 line if not needed):

{{hc|/etc/named.conf|
...
    //listen-on { any; };
    listen-on port 54 { any; };
    listen-on-v6 port 54 { any; };
...}}

## Unbound
You can easily set up DoT server by adding to your configuration file port 853 to listening and specify certificate and key paths:

DoH server setup is same as DoT, but needed port is 443:

## Web server configuration
## Apache httpd proxy configuration
Configure a proxy in your primary httpd.conf or appropriate vhost listening on 443:

## nginx proxy configuration
## DoT Proxy
With Nginx stream module you can setup proxy to upstream DNS. Note that you can use local dns as well as third parties.

{{hc|/etc/nginx/nginx.conf|
...
stream {
    upstream dns {
        zone dns 64k;
        server 8.8.8.8:53;
    }

    server {
        listen 853 ssl;
        ssl_certificate /etc/nginx/ssl/certs/public.pem;
        ssl_certificate_key /etc/nginx/ssl/private/private.pem;
        proxy_pass dns;
    }
}
...}}

## DoH Proxy
For DoH implementation you need for use additional NJS scripts. You need to get it from this GitHub's page, put it to  and be sure package  is installed.

At first you need to setup stream service, which will be get DNS request from nginx's HTTP/2 service, process it with  to find DNS packets and pass it to upstream DNS server.

{{hc|/etc/nginx/nginx.conf|
...
stream {
    upstream dns {
        zone dns 64k;
        server 1.1.1.1:53;

    server {
        listen 127.0.0.1:8053;
        js_filter doh_filter_request;
        proxy_ssl on;
        proxy_pass dns;
        }
}
...
}}

Then, setup HTTP/2 service to listen DNS requests at URI /dns-query and relay them to stream service. Note that to a need change certificates to valid

{{hc|/etc/nginx/nginx.conf|
...
upstream dohloop {
   zone dohloop 64k;
   server 127.0.0.1:8053;
}

server {
    listen 443 ssl http2;
    ssl_certificate /etc/nginx/ssl/certs/public.pem;
    ssl_certificate_key /etc/nginx/ssl/private/private.pem;

    location /dns-query {
        proxy_http_version 1.0;
        proxy_pass http://dohloop;
   }
}
...}}

You can use both DoT and DoH services at same time, caching and multiple upstream DNS. For more examples see these configuration files

## DNS over TLS configuration via stunnel
Configure stunnel to listen on TCP/853 for TLS connections, and forward to your local DNS provider:

Configure stunnel to listen on TCP/54 and forward to an upstream secure provider:

## DNS over HTTPS server Docker images
See https://hub.docker.com/r/satishweb/doh-server.
