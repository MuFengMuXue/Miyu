# NaïveProxy

NaïveProxy is a cross-platform proxy that uses Chromium's network stack to camouflage traffic and provides strong censorship resistence and low detectablility when bypassing the Great Firewall of China. It can mitigate TLS fingerprint issues which lead to detection and survived large scale blocking of TLS-based censorship circumvention tools in China. It requires a  client and requires a Caddy server with  module to work.

## Installation
Install  and run . Here is an example config file:

{{hc|config.json|
{
  "listen": "socks://127.0.0.1:1080",
  "proxy": "https://myUsername:myStrongPassword@my.domain"
}
}}

## Configuration
Naiveproxy cannot run without a caddy server with forwardproxy module. You can build it with :

Then, config caddy:

{{hc|/etc/caddy/Caddyfile|
{
  order forward_proxy before file_server
}
:443, my.domain:443 {
  tls /etc/caddy/ssl.cer /etc/caddy/ssl.key
  forward_proxy {
    basic_auth myUsername myStrongPassword
    hide_ip
    hide_via
    probe_resistance
  }
  file_server {
    root /var/www/html
  }
}
}}

Note that  must appear first for this Caddyfile to work. See Caddyfile docs for how to configure TLS certificates.

Then start caddy server:

 # setcap cap_net_bind_service+ep ./caddy && ./caddy start

You may also want to run caddy as a daemon.
