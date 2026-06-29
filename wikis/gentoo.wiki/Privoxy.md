**Resources**

[[]][Home](https://www.privoxy.org/)

[[]][Official User manual](https://www.privoxy.org/user-manual/index.html)

[[]][Package information](https://packages.gentoo.org/packages/net-proxy/privoxy)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Privoxy "wikipedia:Privoxy")

[[]][Man page](https://www.privoxy.org/man-page/privoxy-man-page.html)

**Privoxy** is a non-caching web proxy server with advanced filtering capabilities which can improve privacy. It works by removing or modifying elements of a HTTP request and its response, either on the headers or on the body of the request.

Although comparable to some browser extensions, being a server, it allows different programs to use it, removing the need to add extensions to each browser and with it, its potential associated problems like incompatibilities between extensions. It also helps to reduce browser fingerprinting thanks to the reduction of installed extensions.

It may be combined with caching proxies like [squid](https://wiki.gentoo.org/wiki/Squid "Squid") to improve its overall speed.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Service]](#Service)
        -   [[1.3.1] [OpenRC]](#OpenRC)
        -   [[1.3.2] [systemd]](#systemd)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Enable logging]](#Enable_logging)
    -   [[2.2] [Clients]](#Clients)
        -   [[2.2.1] [Firefox]](#Firefox)
        -   [[2.2.2] [Chromium]](#Chromium)
    -   [[2.3] [Advanced configuration]](#Advanced_configuration)
        -   [[2.3.1] [Web configuration]](#Web_configuration)
        -   [[2.3.2] [Editing configuration files manually]](#Editing_configuration_files_manually)
            -   [[2.3.2.1] [To change the default port where Privoxy listens]](#To_change_the_default_port_where_Privoxy_listens)
            -   [[2.3.2.2] [To block specific sites]](#To_block_specific_sites)
-   [[3] [Testing]](#Testing)
    -   [[3.1] [lsof]](#lsof)
    -   [[3.2] [nmap]](#nmap)
    -   [[3.3] [On a browser]](#On_a_browser)
-   [[4] [Usage]](#Usage)
    -   [[4.1] [By itself]](#By_itself)
    -   [[4.2] [Forwarding traffic through Tor]](#Forwarding_traffic_through_Tor)
    -   [[4.3] [Using Squid as cache proxy]](#Using_Squid_as_cache_proxy)
    -   [[4.4] [Using Squid + Privoxy + Tor]](#Using_Squid_.2B_Privoxy_.2B_Tor)
-   [[5] [Caveats]](#Caveats)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [net-proxy/privoxy](https://packages.gentoo.org/packages/net-proxy/privoxy) [[]] [A web proxy with advanced filtering capabilities for enhancing privacy]

  ----------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+acl`](https://packages.gentoo.org/useflags/+acl)                                       Add support for Access Control Lists
  [`+fast-redirects`](https://packages.gentoo.org/useflags/+fast-redirects)                 Support fast redirects
  [`+force`](https://packages.gentoo.org/useflags/+force)                                   Allow single-page disable (force load)
  [`+image-blocking`](https://packages.gentoo.org/useflags/+image-blocking)                 Allows the +handle-as-image action, to send \"blocked\" images instead of HTML
  [`+jit`](https://packages.gentoo.org/useflags/+jit)                                       Enable PCRE jit (recommended)
  [`+mbedtls`](https://packages.gentoo.org/useflags/+mbedtls)                               Use net-libs/mbedtls for HTTPS filtering
  [`+stats`](https://packages.gentoo.org/useflags/+stats)                                   Keep statistics
  [`+threads`](https://packages.gentoo.org/useflags/+threads)                               Enable POSIX threads. Highly recommended, otherwise both build and run-time features may not work properly.
  [`+zlib`](https://packages.gentoo.org/useflags/+zlib)                                     Decompress zlib compressed data using virtual/zlib before filtering
  [`brotli`](https://packages.gentoo.org/useflags/brotli)                                   Decompress brotli compressed data using app-arch/brotli before filtering
  [`client-tags`](https://packages.gentoo.org/useflags/client-tags)                         Enable support for client-specific tags
  [`compression`](https://packages.gentoo.org/useflags/compression)                         Allow privoxy to compress buffered content before sending to the client, if it supports it
  [`editor`](https://packages.gentoo.org/useflags/editor)                                   Enable the web-based actions file editor
  [`extended-host-patterns`](https://packages.gentoo.org/useflags/extended-host-patterns)   Enable and require PCRE syntax in host patterns. You must convert action files to PCRE, see privoxy-url-pattern-translator.pl (see tools USE flag). Use at your own risk!
  [`extended-statistics`](https://packages.gentoo.org/useflags/extended-statistics)         Gather extended statistics
  [`external-filters`](https://packages.gentoo.org/useflags/external-filters)               Allow to filter content with scripts and programs. Experimental
  [`fuzz`](https://packages.gentoo.org/useflags/fuzz)                                       Exposes Privoxy internals to input from files or stdout. Intended for fuzzing testing
  [`graceful-termination`](https://packages.gentoo.org/useflags/graceful-termination)       Allow to shutdown Privoxy through the webinterface
  [`ipv6`](https://packages.gentoo.org/useflags/ipv6)                                       Add support for IP version 6
  [`lfs`](https://packages.gentoo.org/useflags/lfs)                                         Support large files (\>2GB) on 32-bit systems
  [`openssl`](https://packages.gentoo.org/useflags/openssl)                                 Use dev-libs/openssl for HTTPS filtering
  [`png-images`](https://packages.gentoo.org/useflags/png-images)                           Use PNG format instead of GIF for built-in images
  [`sanitize`](https://packages.gentoo.org/useflags/sanitize)                               Enable asan, msan and usan sanitizers. Your compiler must support them
  [`selinux`](https://packages.gentoo.org/useflags/selinux)                                 !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`ssl`](https://packages.gentoo.org/useflags/ssl)                                         HTTPS inspection support. Enables privoxy to perform SSL MITM filtering, see docs, use with care
  [`toggle`](https://packages.gentoo.org/useflags/toggle)                                   Support temporary disable toggle via web interface
  [`tools`](https://packages.gentoo.org/useflags/tools)                                     Install log parser, regression tester and user agent generator tools
  [`whitelists`](https://packages.gentoo.org/useflags/whitelists)                           Support trust files (white lists)
  ----------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-20 01:44] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

To install [[[net-proxy/privoxy]](https://packages.gentoo.org/packages/net-proxy/privoxy)[]]:

`root `[`#`]`emerge --ask net-proxy/privoxy`

### [Service]

#### [OpenRC]

To have privoxy start at boot:

`root `[`#`]`rc-update add privoxy default`

To start manually:

`root `[`#`]`rc-service privoxy start`

#### [systemd]

To have privoxy start at boot:

`root `[`#`]`systemctl enable privoxy.service`

To start manually:

`root `[`#`]`systemctl start privoxy.service`

## [Configuration]

Once the server is running, clients have to be made aware of it, to do so, the proxy configuration can be adjusted on each program. But many applications, such as browsers, [Wget](https://wiki.gentoo.org/wiki/Wget "Wget"), [Yt-dlp](https://wiki.gentoo.org/wiki/Yt-dlp "Yt-dlp"), and others, evaluate a system variable and no longer need to be manually configured to use the web proxy. Create a new file, e.g., [/etc/env.d/99proxy] with:

[FILE] **`/etc/env.d/99proxy`**

    export http_proxy="http://127.0.0.1:8118"
    export https_proxy="http://127.0.0.1:8118"

and activate it:

`root `[`#`]`env-update`

** Important**\
By default Privoxy will listen for connections on port 8118 and the local address (localhost / 127.0.0.1).

### [Enable logging]

These are the recommended settings:

[FILE] **`/etc/privoxy/config`**

    debug     1 # Log the destination for each request. See also debug 1024.
    debug  1024 # Log the destination for requests Privoxy didn't let through, and the reason why.
    debug  4096 # Startup banner and warnings
    debug  8192 # Non-fatal errors

### [Clients]

#### [Firefox]

Edit \> Settings \> Network Settings \> Settings \> Manual proxy configuration

**HTTP Proxy** 127.0.0.1 **Port** 8118

Mark the checkbox *Also use this proxy for HTTPS*

#### [Chromium]

`user `[`$`]`chromium --proxy-server="localhost:8118"`

### [Advanced configuration]

The default values on Privoxy should work well for most cases, but further configuration can be made using the following methods.

** Important**\
Remember to read the comments of the files or check the [online manual](https://www.privoxy.org/user-manual/index.html).

#### [Web configuration]

Pointing a browser like [Firefox](https://wiki.gentoo.org/wiki/Firefox "Firefox") to [status and configuration page](http://config.privoxy.org/show-status).

#### [Editing configuration files manually]

All the configuration files are located at [/etc/privoxy].

The following are two common cases for modifying the base configuration:

##### [To change the default port where Privoxy listens]

Look for:

[FILE] **`/etc/privoxy/config`**

    listen-address  192.168.0.1:8118

Change it to the desired port, for instance, if the desired port is 8080:

[FILE] **`/etc/privoxy/config`**

    listen-address  192.168.0.1:8080

##### [To block specific sites]

Using a text editor as root edit [/etc/privoxy/user.action], and add this at the end:

[FILE] **`/etc/privoxy/user.action`**

     }
    .example.com
    .example2.com

## [Testing]

Once the server is running, different tools and methods can be used to test if it is working properly.

### [lsof]

If no client has been used yet, only the first line will be present. If a client has issued a request then more results will be present on the output of the command:

`root `[`#`]`lsof -i | grep privoxy`

    privoxy    5482 privoxy    4u  IPv4  15135      0t0  TCP localhost:8118 (LISTEN)
    privoxy    5482 privoxy    7u  IPv4 246374      0t0  TCP localhost:8118->localhost:54486 (ESTABLISHED)
    privoxy    5482 privoxy    9u  IPv4 246376      0t0  TCP localhost:55012->localhost:9050 (ESTABLISHED)

### [nmap]

`root `[`#`]`nmap -sS 127.0.0.1 -p 8118`

    Starting Nmap 7.92 ( https://nmap.org ) at 2021-10-20 10:07 CEST
    Nmap scan report for localhost (127.0.0.1)
    Host is up (0.000050s latency).

    PORT     STATE SERVICE
    8118/tcp open  privoxy

    Nmap done: 1 IP address (1 host up) scanned in 0.09 seconds

### [On a browser]

Following the link [config.privoxy.org](http://config.privoxy.org/) will trigger a default filter on privoxy which will serve a page with the text:

**This is Privoxy 3.0.32 on localhost (127.0.0.1), port 8118, enabled**

a section with the Privoxy Menu and a section with support links.

## [Usage]

### [By itself]

Once clients are made aware of the proxy by adjusting their settings to point to the privoxy server they will start using it, including any changes made to the configuration files since the server doesn\'t have to be restarted to update its behaviour

### [Forwarding traffic through Tor]

[Tor](https://wiki.gentoo.org/wiki/Tor "Tor") is a powerful tool for the anonymity seekers and for many years has been used in combination with privoxy.

As root edit [/etc/privoxy/config], look for:

[FILE] **`/etc/privoxy/`**

    #        forward-socks5t             /     127.0.0.1:9050 .

Change it to:

[FILE] **`/etc/privoxy/`**

    forward-socks5t             /     127.0.0.1:9050 .

### [Using Squid as cache proxy]

After installing [Squid](https://wiki.gentoo.org/wiki/Squid "Squid") and Privoxy, set the clients to use Squid and set Squid to forward traffic to Privoxy.

For instance, change the proxy configuration on [Firefox](https://wiki.gentoo.org/wiki/Firefox "Firefox") following [the steps mentioned above](#Firefox) but instead of port 8118 set it to 3128. After that, as root edit [/etc/squid/squid.conf] and add the following lines:

[FILE] **`/etc/squid/squid.conf`**

    # Forward request to Privoxy
    cache_peer 127.0.0.1 parent 8118 7 no-query default no-digest no-netdb-exchange
    # ACL for FTP
    acl ftp proto FTP
    # No FTP through Privoxy
    always_direct allow ftp
    # Immediate restart
    shutdown_lifetime 0 seconds
    httpd_suppress_version_string on
    forwarded_for off
    never_direct allow all

### [][Using Squid + Privoxy + Tor]

After following all the steps above, the full chain should be working. To confirm that everything is working fine, visit the following 2 URLs.

1.  [config.privoxy.org](http://config.privoxy.org/)
2.  [Tor check](https://check.torproject.org/)

The first URL should get the same result as the [browser test done before](#On_a_browser).

The second URL should end in a page with the text **Congratulations. This browser is configured to use Tor**.

## [Caveats]

Although removing elements from the page makes it lighter and the privoxy process tiself is not big or slow, if too many filters are working at the same time, the final result may be a bit slower than browsing without privoxy.

## [See also]

-   [Squid](https://wiki.gentoo.org/wiki/Squid "Squid") --- a web cache and a proxy server application used speed up web browsing.
-   [Tor](https://wiki.gentoo.org/wiki/Tor "Tor") --- an onion routing Internet anonymity system.

## [External resources]

-   [Quickstart to Using Privoxy](https://www.privoxy.org/user-manual/quickstart.html)
-   [Privoxy Frequently Asked Questions](https://www.privoxy.org/faq/index.html)
-   [Official User manual](https://www.privoxy.org/user-manual/index.html)
-   [Privoxy questions on StackExchange](https://stackexchange.com/search?q=privoxy)
-   [Onion link to the Privoxy Home page](http://l3tczdiiwoo63iwxty4lhs6p7eaxop5micbn7vbliydgv63x5zrrrfyd.onion/)
-   [Test of a request page (only works if Privoxy is working)](http://config.privoxy.org/show-request)
-   [Check rules applied to a page (only works if Privoxy is working)](http://config.privoxy.org/show-url-info)