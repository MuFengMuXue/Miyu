[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Caddy&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://caddyserver.com/)

[[]][Official documentation](https://caddyserver.com/docs/)

[[]][GitHub](https://github.com/caddyserver/caddy)

[[]][Package information](https://packages.gentoo.org/packages/www-servers/caddy)

**Caddy** is a fast and extensible multi-platform HTTP/1-2-3 [web server](https://wiki.gentoo.org/wiki/Category:Web_servers "Category:Web servers") with automatic HTTPS. It provides an extensible platform which can be used as a HTTP server, reverse proxy, or static file server. Caddy and its extensions are written in [Go](https://wiki.gentoo.org/wiki/Go "Go").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Simple text response]](#Simple_text_response)
    -   [[2.2] [Using a domain]](#Using_a_domain)
    -   [[2.3] [Reverse proxies]](#Reverse_proxies)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Services]](#Services)
        -   [[3.1.1] [OpenRC]](#OpenRC)
        -   [[3.1.2] [Systemd]](#Systemd)
    -   [[3.2] [Command line usage]](#Command_line_usage)
        -   [[3.2.1] [Using a specified config file]](#Using_a_specified_config_file)
        -   [[3.2.2] [Reloading]](#Reloading)
-   [[4] [See also]](#See_also)
-   [[5] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [www-servers/caddy](https://packages.gentoo.org/packages/www-servers/caddy) [[]] [Fast and extensible multi-platform HTTP/1-2-3 web server with automatic HTTPS]

  ------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+filecaps`](https://packages.gentoo.org/useflags/+filecaps)                         Use Linux file capabilities to control privilege rather than set\*id (this is orthogonal to USE=caps which uses capabilities at runtime e.g. libcap)
  [`dns-alidns`](https://packages.gentoo.org/useflags/dns-alidns)                       Adds module which allows to manage Aliyun DNS zones using Caddy https://caddyserver.com/docs/modules/dns.providers.alidns
  [`dns-azure`](https://packages.gentoo.org/useflags/dns-azure)                         Adds module which allows to manage Azure hosted DNS zones using Caddy https://caddyserver.com/docs/modules/dns.providers.azure
  [`dns-cloudflare`](https://packages.gentoo.org/useflags/dns-cloudflare)               Adds module which allows to manage Cloudflare hosted DNS zones using Caddy https://caddyserver.com/docs/modules/dns.providers.cloudflare
  [`dns-cloudns`](https://packages.gentoo.org/useflags/dns-cloudns)                     Adds module which allows to manage ClouDNS hosted DNS zones using Caddy https://caddyserver.com/docs/modules/dns.providers.cloudns
  [`dns-digitalocean`](https://packages.gentoo.org/useflags/dns-digitalocean)           Adds module which allows to manage DigitalOcean hosted DNS zones using Caddy https://caddyserver.com/docs/modules/dns.providers.digitalocean
  [`dns-duckdns`](https://packages.gentoo.org/useflags/dns-duckdns)                     Adds module which allows to manage Duck DNS hosted DNS zones using Caddy https://caddyserver.com/docs/modules/dns.providers.duckdns
  [`dns-dynv6`](https://packages.gentoo.org/useflags/dns-dynv6)                         Adds module which allows to manage Dynv6 hosted DNS zones using Caddy
  [`dns-gandi`](https://packages.gentoo.org/useflags/dns-gandi)                         Adds module which allows to manage Gandi hosted DNS zones using Caddy https://caddyserver.com/docs/modules/dns.providers.gandi
  [`dns-godaddy`](https://packages.gentoo.org/useflags/dns-godaddy)                     Adds module which allows to manage Godaddy hosted DNS zones using Caddy https://caddyserver.com/docs/modules/dns.providers.godaddy
  [`dns-googleclouddns`](https://packages.gentoo.org/useflags/dns-googleclouddns)       Adds module which allows to manage Google Cloud hosted DNS zones using Caddy https://caddyserver.com/docs/modules/dns.providers.googleclouddns
  [`dns-he`](https://packages.gentoo.org/useflags/dns-he)                               Adds module which allows to manage Hurricane Electric hosted DNS zones using Caddy https://caddyserver.com/docs/modules/dns.providers.he
  [`dns-hetzner`](https://packages.gentoo.org/useflags/dns-hetzner)                     Adds module which allows to manage Hetzner hosted DNS zones using Caddy https://caddyserver.com/docs/modules/dns.providers.hetzner
  [`dns-huaweicloud`](https://packages.gentoo.org/useflags/dns-huaweicloud)             Adds module which allows to manage Huawei Cloud hosted DNS zones using Caddy https://caddyserver.com/docs/modules/dns.providers.huaweicloud
  [`dns-linode`](https://packages.gentoo.org/useflags/dns-linode)                       Adds module which allows to manage Linode hosted DNS zones using Caddy https://caddyserver.com/docs/modules/dns.providers.linode
  [`dns-mailinabox`](https://packages.gentoo.org/useflags/dns-mailinabox)               Adds module which allows to manage Mail-in-a-Box hosted DNS zones using Caddy https://caddyserver.com/docs/modules/dns.providers.mailinabox
  [`dns-namecheap`](https://packages.gentoo.org/useflags/dns-namecheap)                 Adds module which allows to manage Namecheap hosted DNS zones using Caddy https://caddyserver.com/docs/modules/dns.providers.namecheap
  [`dns-netcup`](https://packages.gentoo.org/useflags/dns-netcup)                       Adds module which allows to manage netcup hosted DNS zones using Caddy https://caddyserver.com/docs/modules/dns.providers.netcup
  [`dns-netlify`](https://packages.gentoo.org/useflags/dns-netlify)                     Adds module which allows to manage Netlify hosted DNS zones using Caddy https://caddyserver.com/docs/modules/dns.providers.netlify
  [`dns-ovh`](https://packages.gentoo.org/useflags/dns-ovh)                             Adds module which allows to manage OVHcloud hosted DNS zones using Caddy https://caddyserver.com/docs/modules/dns.providers.ovh
  [`dns-porkbun`](https://packages.gentoo.org/useflags/dns-porkbun)                     Adds module which allows to manage porkbun hosted DNS zones using Caddy https://caddyserver.com/docs/modules/dns.providers.porkbun
  [`dns-powerdns`](https://packages.gentoo.org/useflags/dns-powerdns)                   Adds module which allows to manage DNS zones of net-dns/pdns using Caddy https://caddyserver.com/docs/modules/dns.providers.powerdns
  [`dns-rfc2136`](https://packages.gentoo.org/useflags/dns-rfc2136)                     Adds module which allows to manage DNS zones using RFC2136 Dynamic Updates within Caddy https://caddyserver.com/docs/modules/dns.providers.rfc2136
  [`dns-route53`](https://packages.gentoo.org/useflags/dns-route53)                     Adds module which allows to manage AWS route53 hosted DNS zones using Caddy https://caddyserver.com/docs/modules/dns.providers.route53
  [`dns-vultr`](https://packages.gentoo.org/useflags/dns-vultr)                         Adds module which allows to manage Vultr hosted DNS zones using Caddy https://caddyserver.com/docs/modules/dns.providers.vultr
  [`dynamicdns`](https://packages.gentoo.org/useflags/dynamicdns)                       Adds module which allows querying an endpoint to get dynamic public IP and updating records with DNS providers https://caddyserver.com/docs/modules/dynamic_dns
  [`events-handlers-exec`](https://packages.gentoo.org/useflags/events-handlers-exec)   Adds module which lets user exec command on Caddy events https://caddyserver.com/docs/modules/events.handlers.exec https://caddyserver.com/docs/caddyfile/options#event-options
  [`security`](https://packages.gentoo.org/useflags/security)                           Authentication, Authorization, and Accounting. LDAP, OAuth, SAML, MFA, 2FA, JWT etc.. https://caddyserver.com/docs/modules/security
  [`webdav`](https://packages.gentoo.org/useflags/webdav)                               Adds module which implements an HTTP handler for responding to WebDAV clients https://caddyserver.com/docs/modules/http.handlers.webdav
  ------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-06 20:27] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask www-servers/caddy`

## [Configuration]

Caddy\'s default config file when using the Gentoo package is [/etc/caddy/Caddyfile].

### [Simple text response]

To configure a basic HTTP server that responds with simple text, using a Caddyfile ^[\[1\]](#cite_note-1)^ is the easiest way to get started. The config for this looks like:

[FILE] **`Caddyfile`**

    localhost

### [Using a domain]

For a more real-world setup where you have a domain you would like to host a web server on, the config will look like the following:

[FILE] **`Caddyfile`**

    example.com

### [Reverse proxies]

Caddy allows you to use a reverse proxy to allow HTTPS connections over the Internet without having port conflicts. For reverse proxying a web server listening on port `8080` using Caddy, the following config will allow you to do so:

[FILE] **`Caddyfile`**

    sub.example.com

## [Usage]

### [Services]

#### [OpenRC]

To start Caddy using OpenRC, run

`root `[`#`]`rc-service caddy start`

and to have it run on boot, run

`root `[`#`]`rc-update add caddy default`

#### [Systemd]

To start Caddy on Systemd, run

`root `[`#`]`systemctl start caddy`

and to have it start on boot, run

`root `[`#`]`systemctl enable caddy`

### [Command line usage]

#### [Using a specified config file]

To start Caddy with a config file that is not [/etc/caddy/Caddyfile], run

`user `[`$`]`caddy run --config /path/to/Caddyfile`

#### [Reloading]

Caddy config can be reloaded in a zero-downtime fashion. To reload Caddy from the command-line, you can run

`user `[`$`]`caddy reload`

or for reloading the service:

`root `[`#`]`rc-service caddy reload`

`root `[`#`]`systemctl reload caddy`

## [[] See also]

-   [Apache](https://wiki.gentoo.org/wiki/Apache "Apache") --- an efficient, extensible [web server](https://wiki.gentoo.org/wiki/Category:Web_servers "Category:Web servers"). It is one of the most popular web servers used the Internet.
-   [Nginx](https://wiki.gentoo.org/wiki/Nginx "Nginx") --- a robust, small, high performance [web server](https://wiki.gentoo.org/wiki/Category:Web_servers "Category:Web servers") and reverse proxy server.

## [References]

1.  [[[↑](#cite_ref-1)] [[The Caddyfile --- Caddy Documentation](https://caddyserver.com/docs/caddyfile), caddyserver. Retrieved on May 24, 2024]]