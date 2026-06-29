**Resources**

[[]][Home](https://www.torproject.org/)

[[]][Package information](https://packages.gentoo.org/packages/net-vpn/tor)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Tor_(anonymity_network) "wikipedia:Tor (anonymity network)")

[[]][Official documentation](https://www.torproject.org/docs/documentation.html.en)

[[]][[#tor](ircs://irc.libera.chat/#tor)] ([[webchat](https://web.libera.chat/#tor)])

[[]][r/TOR](https://reddit.com/r/TOR)

**Tor** is an onion routing Internet anonymity system.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Alternative installation]](#Alternative_installation)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Sandbox]](#Sandbox)
    -   [[2.2] [Disabling non-Tor traffic]](#Disabling_non-Tor_traffic)
    -   [[2.3] [Rules for Tor circuits]](#Rules_for_Tor_circuits)
        -   [[2.3.1] [Restrict exit nodes]](#Restrict_exit_nodes)
        -   [[2.3.2] [Restrict node count]](#Restrict_node_count)
        -   [[2.3.3] [Restrict traffic entirely]](#Restrict_traffic_entirely)
    -   [[2.4] [Outbound Node Firewall]](#Outbound_Node_Firewall)
    -   [[2.5] [Stream isolation]](#Stream_isolation)
    -   [[2.6] [HTTP proxy]](#HTTP_proxy)
    -   [[2.7] [Using bridges]](#Using_bridges)
        -   [[2.7.1] [OpenRC]](#OpenRC)
        -   [[2.7.2] [systemd]](#systemd)
    -   [[2.8] [Running a relay]](#Running_a_relay)
        -   [[2.8.1] [Running an Exit]](#Running_an_Exit)
    -   [[2.9] [Running a Hidden service]](#Running_a_Hidden_service)
    -   [[2.10] [Service]](#Service)
        -   [[2.10.1] [OpenRC]](#OpenRC_2)
        -   [[2.10.2] [systemd]](#systemd_2)
-   [[3] [Application Proxy Configuration]](#Application_Proxy_Configuration)
    -   [[3.1] [Browsers]](#Browsers)
        -   [[3.1.1] [Any browser via PAC file]](#Any_browser_via_PAC_file)
        -   [[3.1.2] [Firefox]](#Firefox)
    -   [[3.2] [SSH]](#SSH)
    -   [[3.3] [git]](#git)
    -   [[3.4] [DNS]](#DNS)
        -   [[3.4.1] [DNS Resolver]](#DNS_Resolver)
    -   [[3.5] [torsocks]](#torsocks)
        -   [[3.5.1] [Transparent Tor Proxy]](#Transparent_Tor_Proxy)
    -   [[3.6] [Simple command-line file downloading]](#Simple_command-line_file_downloading)
    -   [[3.7] [Portage]](#Portage)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Check if using Tor]](#Check_if_using_Tor)
    -   [[4.2] [Checking for network leaks]](#Checking_for_network_leaks)
        -   [[4.2.1] [Local network admin or ISP]](#Local_network_admin_or_ISP)
        -   [[4.2.2] [Machine admin]](#Machine_admin)
        -   [[4.2.3] [Attackers with physical access]](#Attackers_with_physical_access)
        -   [[4.2.4] [The websites/services to which the user connects]](#The_websites.2Fservices_to_which_the_user_connects)
    -   [[4.3] [Troubleshooting downloaded Tor Browser]](#Troubleshooting_downloaded_Tor_Browser)
        -   [[4.3.1] [libcrypto.so: version \`OPENSSL_x.x.x\' not found]](#libcrypto.so:_version_.60OPENSSL_x.x.x.27_not_found)
-   [[5] [Tips]](#Tips)
-   [[6] [See also]](#See_also)
-   [[7] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [net-vpn/tor](https://packages.gentoo.org/packages/net-vpn/tor) [[]] [Anonymizing overlay network for TCP]

  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+man`](https://packages.gentoo.org/useflags/+man)               Build and install man pages
  [`+server`](https://packages.gentoo.org/useflags/+server)         Enable tor\'s relay module so it can operate as a relay/bridge/authority
  [`caps`](https://packages.gentoo.org/useflags/caps)               Use Linux capabilities library to control privilege
  [`doc`](https://packages.gentoo.org/useflags/doc)                 Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`hardened`](https://packages.gentoo.org/useflags/hardened)       Activate default security enhancements for toolchain (gcc, glibc, binutils)
  [`lzma`](https://packages.gentoo.org/useflags/lzma)               Support for LZMA compression algorithm
  [`scrypt`](https://packages.gentoo.org/useflags/scrypt)           Use app-crypt/libscrypt for the scrypt algorithm
  [`seccomp`](https://packages.gentoo.org/useflags/seccomp)         Enable seccomp (secure computing mode) to perform system call filtering at runtime to increase security of programs
  [`selinux`](https://packages.gentoo.org/useflags/selinux)         !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`systemd`](https://packages.gentoo.org/useflags/systemd)         Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  [`zstd`](https://packages.gentoo.org/useflags/zstd)               Enable support for ZSTD compression
  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-08 21:28] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

** Important**\
For Web browsing via Tor, an easy alternative is the official portable [Tor Browser](https://www.torproject.org/projects/torbrowser.html). Even if also using Tor for other purposes, when web browsing over Tor always use Tor Browser.

`root `[`#`]`emerge --ask net-vpn/tor`

** Note**\
Old Tor Browser versions require Wayland to avoid [Firefox Bug](https://bugzilla.mozilla.org/) 1746715, which prevents Tor Browser from running. Current versions do not have this limitation.

### [Alternative installation]

-   [Tor/Docker container image](https://wiki.gentoo.org/wiki/Tor/Docker_container_image "Tor/Docker container image") --- A single binary, statically linked [Docker](https://wiki.gentoo.org/wiki/Docker "Docker") image can be created in a few steps.

## [Configuration]

[[[net-vpn/tor]](https://packages.gentoo.org/packages/net-vpn/tor)[]] ships with a minimal configuration at [/etc/tor/torrc], which works out of the box:

[FILE] **`/etc/tor/torrc`**

    User tor
    PIDFile /run/tor/tor.pid
    Log notice syslog
    DataDirectory /var/lib/tor/data

** Note**\
This configuration runs a *SOCKS5* at [127.0.0.1:9050].

** Tip**\
Configuration option descriptions are available in the manual pages, and can be read with: [man tor].

### [Sandbox]

Tor has own sandbox features. It may provide increased protection of the system if Tor is compromised.

When enabled, the following options cannot be changed once [tor] is running:

-   *Address*
-   *ConnLimit*
-   *CookieAuthFile*
-   *DirPortFrontPage*
-   *ExtORPortCookieAuthFile*
-   *Logs*
-   *ServerDNSResolvConfFile*
-   *ClientOnionAuthDir*

Additionally, usage of the *\"GETINFO address\"* command through the *ControlPort* is disabled.

** Important**\
If using `%include` directives in the [tor] configuration, configuration reloading is disallowed if new configuration files or directories have been added when *Sandbox* mode is enabled.

To use the Sandbox, Tor must be built with the **seccomp** *USE* flag:

[FILE] **`/etc/portage/package.use/tor`**

    # Build Tor with libseccomp for sandbox
    net-vpn/tor seccomp

If this *USE* flag was not already enabled, [[[net-vpn/tor]](https://packages.gentoo.org/packages/net-vpn/tor)[]] can be rebuilt with:

`root `[`#`]`emerge --ask tor`

Finally, `Sandbox 1` can be added to [/etc/tor/torrc]:

[FILE] **`/etc/tor/torrc`Enable sandbox mode.**

    Sandbox 1

### [Disabling non-Tor traffic]

The following iptables rules will prevent non-Tor traffic leaving the host and disable all new connections from outside in case if the host must be configured as a Tor client:

`root `[`#`]`iptables -F `

`root `[`#`]`iptables -P OUTPUT DROP `

`root `[`#`]`iptables -A OUTPUT -s 127.0.0.1 -d 127.0.0.1 -j ACCEPT `

`root `[`#`]`iptables -A OUTPUT -m owner --uid-owner tor -j ACCEPT `

`root `[`#`]`iptables -P INPUT DROP `

`root `[`#`]`iptables -A INPUT -s 127.0.0.1 -d 127.0.0.1 -j ACCEPT `

`root `[`#`]`iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT `

And to flush these and any other existing rules:

`root `[`#`]`iptables -F `

`root `[`#`]`iptables -X `

### [Rules for Tor circuits]

** Warning**\
These options may significantly reduce the total number of usable relays. Modifying the defaults parameters is unwise. Using an exit node in a country with a prominent intelligence agency should pose very little risk \-- the same risks exist with *any* exit node. Any exit node can capture sensitive information transmitted in plaintext.

** Important**\
GeoIP is inherently unreliable, see [DeTor](https://detor.cs.umd.edu/).

In the following examples, connections to [ECHELON](https://en.wikipedia.org/wiki/ECHELON) and [Five Eyes](https://en.wikipedia.org/wiki/Five_Eyes) will be restricted to varying degrees.

** Note**\
*AU*stralia, *CA*nada, *GB*ritian, *NZ*ealand, and *US*states make up the [Five Eyes](https://en.wikipedia.org/wiki/Five_Eyes).

#### [Restrict exit nodes]

To restrict exit traffic from using nodes from these countries:

[FILE] **`/etc/tor/torrc`Restrict FVEY exit traffic.**

    ExcludeExitNodes , , , ,

** Tip**\
Node fingerprints or IPv4 and IPv6 addresses/networks can be used instead of country codes.

#### [Restrict node count]

To treat nodes from these countries as if they are a single organization:

[FILE] **`/etc/tor/torrc`Treat FVEY nodes as a single entity.**

    NodeFamily , , , ,

#### [Restrict traffic entirely]

To entirely disallow traffic through or to nodes from these countries:

[FILE] **`/etc/tor/torrc`Disallow FVEY traffic.**

    StrictNodes  1  # Force ExcludeNodes to all circuits, even if it breaks functionality
    ExcludeNodes , , , ,

** Note**\
*StrictNodes* only applies to *ExcludeNodes*, not *ExcludeExitNodes*, *ExitNodes*, *MiddleNodes*, or *MapAddress*.

### [Outbound Node Firewall]

** Important**\
Only do this if absolutely necessary, as it will greatly decrease the number of connectable nodes.

If the network where Tor is being used is restricted, such that traffic is only allows to certain IPs or ports, **ReachableAddresses** can be configured so Tor only attempts outbound connections matching the defined criteria:

[FILE] **`/etc/tor/torrc`Restrict tor to**

    # A comma-separated list of IP addresses and ports that your firewall allows you to connect to.
    ReachableAddresses *:443, *:80

** Tip**\
**ReachableAddresses** can be configured using the same format as **ExitPolicy**.

** Note**\
`ReachableAddresses reject *:* ` is implied as a final rule when accepted ranges are defined.

### [Stream isolation]

The user might not want to mix [GPG](https://wiki.gentoo.org/wiki/GPG "GPG") traffic with web browser traffic or to mix irssi circuits with bitcoin wallet circuits. In all cases an exit node can make correlation between separate activities. Stream isolation provides an easy way to separate different Tor circuits and make different applications use isolated streams.

By default, multiple \*Port lines (SocksPort, DNSPort, TransPort) will never share circuits. To do stream isolation on a single \*Port option, one might add one or more of the following isolation flags to \*Port options: IsolateClientAddr, IsolateSOCKSAuth, IsolateClientProtocol, IsolateDestPort, IsolateDestAddr.

Some are enabled by default already and more isolation flags does not necessarily mean more security/anonymity/privacy. To see the most up-to-date list of stream isolation flags, see \`man tor\`.

So to ensure GPG client and instant messenger don\'t put streams on the same circuit, the easiest procedure is adding the following to [torrc] and point them at different SocksPorts.

[FILE] **`/etc/tor/torrc`torrc configuration**

    # gpg client
    SocksPort 127.0.0.1:9100
    # instant messenger
    SocksPort 127.0.0.1:9150
    # More isolation:
    SOCKSPort 9200 IsolateClientAddr IsolateSOCKSAuth IsolateClientProtocol IsolateDestPort IsolateDestAddr
    # etc...

### [HTTP proxy]

Some applications do not support routing their traffic through a SOCKS proxy. However, they more often than not do support using an HTTP proxy instead. By utilizing the `HTTPTunnelPort` [torrc] configuration option, Tor can be configured to expose an HTTP proxy, which actually just instructs the Tor client to use HTTP CONNECT instead of SOCKS to listen for proxy connections, while still ultimately routing traffic through the Tor network^[\[1\]](#cite_note-1)^:

[FILE] **`/etc/tor/torrc`torrc configuration**

    # This option exposes an HTTP proxy at port 9080
    HTTPTunnelPort 9080

Applications that support talking to an HTTP proxy can then be instructed to connect to the configured proxy at port 9080.

### [Using bridges]

Tor is blocked in some countries, to evade the blockage one might use bridges. To use bridges, first lyrebird package needs to be installed:

`root `[`#`]`emerge --ask net-proxy/lyrebird`

After installation is finished, add the following to tor configuration file:

[FILE] **`/etc/tor/torrc`torrc configuration**

    ClientTransportPlugin meek_lite,obfs4,webtunnel exec /usr/bin/lyrebird

    Bridge <PROTOCOL> <IP>:<PORT> <RSA> cert=<CERT> iat-mode=<X>
    # ... add more bridge lines if needed

    UseBridges 1

** Tip**\
For bridge lines visit: [https://bridges.torproject.org/options](https://bridges.torproject.org/options)

After configuration changes are done, restart the tor service:

#### [OpenRC]

`root `[`#`]`rc-service tor restart`

#### [systemd]

`root `[`#`]`systemctl restart tor.service`

### [Running a relay]

** Note**\
As of Tor 0.4.6.1-alpha, non-authoritative relays will not publish their **DirPort**, but it can still be used to serve a configured **DirPortFrontPage**.

To configure [tor] to run as a relay, define **ORPort**:

[FILE] **`/etc/tor/torrc`**

    ORPort 9001

#### [Running an Exit]

** Warning**\
Please read [tips for running an exit node](https://blog.torproject.org/tips-running-exit-node/) before even considering running an exit!!

Relays can be configured to forward exit traffic by setting `ExitRelay 1` or by configuring an exit policy:

[FILE] **`/etc/tor/torrc`**

    ORPort 9001
    ReducedExitPolicy 1

** Important**\
By default, the relay will not act as an exit unless **ExitPolicy**, **ReducedExitPolicy**, or **IPv6Exit** is set.

### [Running a Hidden service]

Running a Tor hidden service is easy, simply configure the following:

-   **HiddenServiceDir** - Path to the directory used to store hidden service keys.
-   **HiddenServicePort** - The first arg is the port used within the TOR network, the second is the target it forwards traffic to.

[FILE] **`/etc/tor/torrc`**

    HiddenServiceDir /var/lib/tor/data/hiddenservice
    HiddenServicePort 80 127.0.0.1:80

** Note**\
Multiple **HiddenServicePorts** can be defined per **HiddenServiceDir**; **HiddenServicePorts** apply to the last defined **HiddenServiceDir**.

** Tip**\
The onion hostname will generated at [/var/lib/tor/data/hiddenservice/hostname] once the service is running.

### [Service]

#### [OpenRC]

To start immediately:

`root `[`#`]`rc-service tor start`

To start the Tor service on system boot, add it to the default runlevel:

`root `[`#`]`rc-update add tor default`

#### [systemd]

To start immediately:

`root `[`#`]`systemctl start tor.service`

To start the Tor service on system boot:

`root `[`#`]`systemctl enable tor.service`

## [Application Proxy Configuration]

### [Browsers]

** Important**\
Use [Tor Browser](https://www.torproject.org/projects/torbrowser.html) from [https://torproject.org](https://torproject.org).

\

Read the recommended configuration changes *Using a system-installed Tor process with Tor Browser*, in the Tor Browser package file [./tor-browser/Browser/start-tor-browser].

#### [Any browser via PAC file]

A PAC file can delegate browser requests to different proxies. Here connections to localhost are handled directly (no proxy); Eepsites are handled by i2p proxy on port 4444 and other traffic goes via Tor SOCKS proxy on port 9050.

[FILE] **`/usr/local/proxy.pac`**

    function FindProxyForURL(url, host)


Save this file as [/usr/local/proxy.pac], and point the browser to it. Most browsers accept Proxy configuration URL, where one can specify `file:///usr/local/proxy.pac`.

#### [Firefox]

Hamburger menu \> Settings \> General \> Network Settings

    manual proxy configuration:
    http proxy           port: 0
    ssl proxy            port: 0
    ftp proxy            port: 0
    socks host 127.0.0.1 port: 9050
    check SOCKS v4
    No Proxy for: localhost, 127.0.0.1

\'SOCKS v4\' is actually SOCKS 4a internally. SOCKS v5 needs more configuration for [safe DNS](#DNS), .

Type [about:config] into the URL bar and set the following:

    network.proxy.socks_remote_dns    true
    network.dns.disablePrefetch       true
    network.dns.disableIPv6           true

This way Firefox will resolve host names via Tor, preventing DNS leaks.

    media.peerconnection.enabled    false

This prevents leaking the system IP address through WebRTC requests.

### [SSH]

[[[net-misc/openssh]](https://packages.gentoo.org/packages/net-misc/openssh)[]] doesn\'t have any native support for SOCKS5, so install [[[net-analyzer/openbsd-netcat]](https://packages.gentoo.org/packages/net-analyzer/openbsd-netcat)[]] and modify the SSH config. It is possible with [[[net-analyzer/netcat]](https://packages.gentoo.org/packages/net-analyzer/netcat)[]] also but the configuration below uses flags specific to the OpenBSD variant.

`root `[`#`]`emerge --ask net-analyzer/openbsd-netcat`

For all hosts:

[FILE] **`~/.ssh/config`**

    Host *
        # Tell SSH to pass its connections through netcat, using a SOCKS5 proxy at 127.0.0.1:9050 (Tor default).
        ProxyCommand nc -X 5 -x 127.0.0.1:9050 %h %p

        # Privacy protections
        # Prevents SSH from telling the remote server about all of your public keys, potentially revealing your ID
        ForwardAgent no
        IdentitiesOnly yes

        # Merges connections to a server to prevent expensive reconnections
        # To avoid this, invoke ssh as: ssh -o 'ControlMaster no' ...
        ControlMaster auto
        ControlPath ~/.ssh/master-%r@%n:%p

        # Compression for low bandwidth lines (like Tor)
        Compression yes

For a specific host:

[FILE] **`~/.ssh/config`**

    Host yourserver.com
            ProxyCommand nc -X 5 -x 127.0.0.1:9050 %h %p

For *.onion* addresses only:

[FILE] **`~/.ssh/config`**

    Host *.onion
            ProxyCommand nc -X 5 -x 127.0.0.1:9050 %h %p

### [git]

Since git can use either SSH or HTTP(S) to fetch data, the proxy setup is dependent on the URL.

For SSH fetching, e.g. git@foo.example:vcs.git, follow the SSH example above for this server.

For HTTP fetching, set the configuration^[\[2\]](#cite_note-2)^:

`user `[`$`]`git config --global http.proxy socks5://127.0.0.1:9050`

This configuration, however, will make Git resolve the hostname of the requested site locally, which may have privacy implications. One way of solving this is to use `socks5h` as the protocol above instead of `socks5`. Doing so instructs the proxy to resolve the hostname instead.

### [DNS]

Some applications may leak DNS requests. The easiest way to check if this really happens is to look at system logs.

`user `[`$`]`sudo tail -f /var/log/messages`

If an application is configured correctly, nothing shows in the logs. Below is an example of a message for a misconfigured application or for a web page that stores links in form of IP addresses:

    Oct 14 14:44:44 localhost Tor[666]: Your application (using socks5 to port 80) is giving Tor only an IP address.
    Applications that do DNS resolves themselves may leak information.  Consider using Socks4A (e.g. via privoxy or socat) instead.
    For more information, please see https://wiki.torproject.org/TheOnionRouter/TorFAQ#SOCKSAndDNS.

In order to check how this works, one needs to give an application an IP address instead of a domain name, retrieved by running the tor-resolve command for example.

#### [DNS Resolver]

Tor can work like a regular DNS server, and resolve the domain via the Tor network. A downside is that it is only able to resolve DNS queries for A-records. MX and NS queries are never answered.

To enable the built-in DNS resolver, add the following lines to the [/etc/tor/torrc] file and restart the daemon:

[FILE] **`/etc/tor/torrc`Tor DNS Resolver**

    ...
    ## Torified DNS
    DNSPort 127.0.0.1:9053
    AutomapHostsOnResolve 1

Then to prevent leak DNS requests make Tor the **ONLY** system default DNS resolver in [/etc/resolv.conf]:

[FILE] **`/etc/resolv.conf`Local Tor DNS Resolver**

    nameserver 127.0.0.1

If using **dhcpcd**, then change its settings in [/etc/dhcpcd.conf] so it does not alter the [resolv.conf] configuration file:

[FILE] **`/etc/dhcpcd.conf`Local Tor DNS Resolver**

    nohook resolv.conf

If using **pppoe**, then change its settings in [/etc/ppp/pppoe.conf] so it does not alter the [resolv.conf] configuration file:

[FILE] **`/etc/ppp/pppoe.conf`Local Tor DNS Resolver**

    DNSTYPE=NOCHANGE

Finally, redirect ALL DNS requests on the system from port 53 to 127.0.0.1:9053 where the Tor DNS listens for requests. Redirect any DNS to the the local (torified) nameserver:

`root `[`#`]`iptables -t nat -A OUTPUT -p TCP --dport 53 -j DNAT --to-destination 127.0.0.1:9053 `

`root `[`#`]`iptables -t nat -A OUTPUT -p UDP --dport 53 -j DNAT --to-destination 127.0.0.1:9053 `

If also using IPv6, do the same for [ip6tables]. When done using Tor, to disable the aforementioned rules use:

`root `[`#`]`iptables -t nat -F `

`root `[`#`]`iptables -t nat -X `

This also disables any other existing NAT rules.

### [torsocks]

`root `[`#`]`emerge --ask net-proxy/torsocks`

For applications lacking support for proxies or Tor, the [torsocks] command can force their traffic through the Tor network, as in [torsocks irssi -c irc.afraidirc.net] or [torify irssi -c mqctemuqfc3tp5ji.onion].

#### [Transparent Tor Proxy]

Tor can work like a transparent proxy.

To enable built-in transparent proxy add the following lines to the [/etc/tor/torrc] file and restart the daemon:

[FILE] **`/etc/tor/torrc`Tor Transparent Proxy**

    ...
    ## Transparent proxy
    TransPort 127.0.0.1:9040

Finally, redirect ALL non-Tor outgoing traffic to a Tor transparent proxy:

`root `[`#`]`iptables -t nat -A OUTPUT -p TCP -m owner ! --uid-owner tor -j DNAT --to-destination 127.0.0.1:9040 `

### [Simple command-line file downloading]

The popular wget utility cannot talk to socks proxy. However, [[[net-misc/curl]](https://packages.gentoo.org/packages/net-misc/curl)[]] can download over Tor any resource located at a given URL and save it in a FILE using:

`user `[`$`]`curl --socks5-hostname 127.0.0.1:9050 -o FILE URL`

The `--socks5-hostname` means that hostnames are resolved via Tor instead of the system\'s DNS resolution, thus preventing DNS leaks.

### [Portage]

Portage can be configured to sync its tree and fetch packages via Tor. Add the following to [/etc/portage/make.conf]:

[FILE] **`/etc/portage/make.conf`**

    FETCHCOMMAND="curl --socks5-hostname 127.0.0.1:9050 --retry 3 --connect-timeout 60 -o \"\$/\$\" \"\$\""
    RESUMECOMMAND="curl -C - --socks5-hostname 127.0.0.1:9050 --retry 3 --connect-timeout 60 -o \"\$/\$\" \"\$\""

All the extra quoting is necessary. Have a look at [man curl] for more customization options.

Curl doesn\'t follow 302 redirects by default (cf. [[[bug #543268]](https://bugs.gentoo.org/show_bug.cgi?id=543268)[]]). Pass `-L` to enable that behaviour.

[emerge \--sync] cannot be used to update the Portage tree via Tor, because `rsync` cannot use SOCKS. In order to sync the Portage tree via Tor, first [configure Tor to expose an HTTP proxy](https://wiki.gentoo.org/wiki/Tor#HTTP_proxy "Tor"), then, given that the HTTP proxy is listening on port 9080, use the command:

`root `[`#`]`http_proxy=127.0.0.1:9080 emerge-webrsync`

This fetches the portage tree snapshot over HTTP. Passing the `http_proxy` environment variable to `emerge-webrsync` is necessary, because [Gemato](https://wiki.gentoo.org/wiki/Gemato "Gemato"), which is what `emerge-webrsync` uses to verify the downloaded snapshot\'s signature, does not support fetching signatures\' associated public keys over SOCKS, but do support doing so over an HTTP proxy, which `http_proxy` enables.

One negative effect is that only daily repository snapshots are retrieved. Issues that are fixed in the interim will not be available until the following daily snapshot. Installing or updating is done as usual, e.g.:

`root `[`#`]`emerge --ask some-package`

## [Troubleshooting]

### [Check if using Tor]

Visit: [https://check.torproject.org/](https://check.torproject.org/)

For web browsing, just get [Tor Browser](https://www.torproject.org/projects/torbrowser.html) from [https://torproject.org](https://torproject.org). Change the security slider if desired, but do not add \"privacy\" add-ons. The more the browser is changed, the more it stands out from the crowd.

Many websites can test anonymity. One of the best is **[whoer.net](https://whoer.net/)**. Another nice one: **[ipleak.net](https://ipleak.net/)**.

To hide more information with a generic web browser, one can try **disabling**: [Javascript](https://noscript.net/), WebRTC. To hide HTML headers use \[[https://prism-break.org/en/projects/random-agent-spoofer/](https://prism-break.org/en/projects/random-agent-spoofer/) Random Agent Spoofer\] and/or [[[net-proxy/privoxy]](https://packages.gentoo.org/packages/net-proxy/privoxy)[]]. Some useful Mozilla add-ons include [Request Policy](https://requestpolicycontinued.github.io/), [Privacy Badger](https://www.eff.org/privacybadger) and [others](https://prism-break.org/en/categories/gnu-linux/#web-browser-addons).

\

### [Checking for network leaks]

Tor is a great tool for enhancing privacy in many situations, but, unlike common belief, does not guarantee 100% anonymity. Let\'s have a brief look at how privacy changes with Tor up and running.

#### [Local network admin or ISP]

These people can no longer easily see which other hosts the user contacts.

However, this only works for programs which were configured to use Tor and do not leak DNS requests. There might be some non-Tor traffic due to other browsers, email, IRC, instant messenger, video conferencing, games, BitTorrent, bitcoin, remote desktop, other machines NATing through the user\'s box, and all other network software.

Even though the ISP cannot see exactly what is done through Tor, they can still detect Tor USAGE, and WHEN and HOW MUCH data is downloaded and uploaded via Tor. Let\'s say an adversary is observing a website. They can see that user X accessed it via Tor to download 2670kB at 9:22AM, upload 340kB at 9:27AM and download 9885kB at 9:31AM. The ISP can see that at these precise times user Y\'s Tor activity was almost the same size. Then if the adversary observing the website can also get that ISP traffic summary, they can determine X and Y are the same. Just a few timestamps like this can connect the identities beyond doubt. A solution is to have lots of Tor traffic entering and leaving the user\'s system at all times.

#### [Machine admin]

If some other people have administrative privileges on the user\'s machine, or gain her user or root\'s privileges through an attack, they can easily monitor all she does, type, and browse, in real time, or later by inspecting history, and then Tor doesn\'t help. Therefore, make sure to administer the system yourself and treat security as an important constituent of anonymity.

#### [Attackers with physical access]

It\'s as easy to install e.g. a small hardware key logger as it was before using Tor, so no privacy gains here.

#### [][The websites/services to which the user connects]

From the websites browsed by the user, Tor only hide the IP address. However, the IP address has not been used as a very useful tool to track and spy on users. The vast majority of Internet users have a dynamic IP address or share one with a large number of other users. Therefore the parties interested in tracking and spying have developed amazingly advanced fingerprinting and tracking techniques without knowing the IP address. Some of the most obvious tracking techniques are:

-   Cookies, supercookies, DOM/HTML5 storage easily track users. Solution: never enable cookies while using Tor.
-   Browser fingerprinting. Your browser sends a huge amount of system information to any visited website, thus identifying the user. For an illustration, visit [panopticlick.eff.org](https://panopticlick.eff.org/). This also applies to other protocol clients as well. Solution: use a special privacy-oriented browser (Tor Browser) or try some privacy plugins for your generic browser.
-   JavaScript or other browser-native scripting. Scripts running in the browser can gather enormous amount of system information, thus identifying the user. For an example, open the browser\'s JS developer tools (F12 in Firefox) and look at the \'navigator\' built-in variable. Websites can also monitor the precise timing of keystrokes to create a typing fingerprint. The same goes for mouse movements over the browser window while browsing. Solution: disable JavaScript in your browser.
-   Geolocation. Websites can ask the browser for geographic location. Solution: disable geolocation in your browser.
-   HTTP headers. Some headers like Referer or ETag track the user as she browses between various websites. Solution: Referer header can be disabled in Firefox in about:config, by setting network.http.sendRefererHeader to 0. **FIXME**: Any ETag solutions?
-   Login. Logging in to any service connects that account with the Tor connection. Solution: Never ever log in to web mail, social network, or any other website while using Tor. It might be better to run another browser not via Tor for the websites where log in is needed. Never use the same browser for both Tor and non-Tor traffic.
-   Browsers\' bugs. Browsers have a lot of bugs that trackers and spies use to reduce or eliminate. Examples include a search giant using cookie preferences bug to set cookies even though disabled, or recent Chrome\'s bug that allows a website to access microphone and monitor speech: [https://tech.slashdot.org/story/14/01/22/2156235/chrome-bugs-lets-sites-listen-to-your-private-conversations](https://tech.slashdot.org/story/14/01/22/2156235/chrome-bugs-lets-sites-listen-to-your-private-conversations)
-   Java. Far worse than JavaScript. A signed Java applet has access to the filesystem, and can read and write files without asking for permission. It can also figure out the IP address which Tor tries to hide, create sockets, or send files to some server without the user\'s knowledge. Solution: never install Java for the browser. **FIXME**: major web browsers have long ago discontinued Java plugin support as of July 2024?
-   [Flash](https://en.wikipedia.org/wiki/Adobe_Flash_Player). Just as large privacy threat as Java. Solution: Never install Flash. Avoid any browser with it preinstalled. Note that Flash Player was officially discontinued on 31 December 2020, and its download page was removed two days later. Since 12 January 2021, Flash Player (original global variants) versions newer than 32.0.0.371, released in May 2020, refuse to play Flash content and instead display a static warning message. The software remained supported in mainland China and in some enterprise variants until 2022.

This list is not exhaustive.

### [Troubleshooting downloaded Tor Browser]

Run

`user `[`$`]`/path/to/torbrowser/Browser/start-tor-browser --verbose`

to help diagnosing.

#### [][libcrypto.so: version \`OPENSSL_x.x.x\' not found]

A workaround for `` ./TorBrowser/Tor/libcrypto.so.3: version `OPENSSL_x.x.x' not found (required by /usr/lib64/libcryptsetup.so.12) `` is to delete the file [Browser/TorBrowser/Tor/libcrypto.so.3] so that the system\'s libcrypto is used instead of the bundled one.

## [Tips]

Here are some tips to remain anonymous while using Tor:

-   Advertisers and social media. This is by far the most widespread privacy threat faced on the web, simply because of the coverage. Almost all popular websites display ads from some giant ad provider. Similarly most websites include small pieces of code from many social networks, e.g. to display the \"like\" buttons, microblogging links, \"login with FooBar\" authentication dialogs, etc. These few Internet giants have their code injected into almost any website people visit. This way they can easily track and spy on anyone visiting almost any website. Some other institutions are known to tap into this tracking/spying datastream. It\'s relatively difficult to eliminate this threat. Most of the ads can be blocked by an ad blocking browser add-ons. Similarly, browser add-ons may eliminate social network components, external authentication, and other third-party content.
-   Browsers\' extensions. Some of the extensions that can be installed in browsers can in fact track the user. E.g. social network integration plugins, extensions that observe your browsing, etc.
-   Browsers\' usage statistics. Some browsers gather info about the user\'s browsing habits and send them to the developers. In Firefox this can be disabled in Settings \> Privacy and Security \> Firefox Data Collection and Use.
-   Custom links. Let\'s say a friend uses a website to invite the user to do something. Then the website sends her an email with a link like website.domain/enGm7IKS. By opening the link, her Tor connection has been identified to be hers, because the enGm7IKS part is unique for her email address.
-   Tor attacks. There are known attacks that can detorify the user. E.g. if the adversary controls both her entry and exit nodes for Tor network, they could after some time correlate her common activities and figure out who she is.
-   Sometimes just using Tor makes the user quite special: [https://yro.slashdot.org/story/13/12/18/047246/harvard-bomb-hoax-perpetrator-caught-despite-tor-use](https://yro.slashdot.org/story/13/12/18/047246/harvard-bomb-hoax-perpetrator-caught-despite-tor-use)

Some institutions with smart people and billions of dollars at their disposal are in the business of tracking and spying on users. This includes advertising giants, social networks and states. The revelations coming from whistle-blowers have shown us the extent of some of the current surveillance. To protect privacy and anonymity, a lot more is necessary. Remain paranoid. Above all please educate yourself about how the Tor network works, what are the common problems, and what could be done to prevent it. Also, read about some recent state attacks on the Tor network. In some countries most Tor nodes might be run by an adversary. Also, read about browser fingerprinting and how it can be prevented. Find out about other non-Tor-related privacy attacks. The privacy war will be a life-long one against giant opponents. Welcome aboard and good luck.

## [See also]

-   [I2P](https://wiki.gentoo.org/wiki/I2P "I2P") --- an anonymous network, similar to [Tor].
-   [Usenet](https://wiki.gentoo.org/wiki/Usenet "Usenet") --- a federated and decentralized worldwide Internet forum and the world\'s oldest digital social network

## [References]

1.  [[[↑](#cite_ref-1)] [[https://forums.whonix.org/t/tor-can-now-serve-as-http-proxy-httptunnelport/5373](https://forums.whonix.org/t/tor-can-now-serve-as-http-proxy-httptunnelport/5373)]]
2.  [[[↑](#cite_ref-2)] [[https://cms-sw.github.io/tutorial-proxy.html](https://cms-sw.github.io/tutorial-proxy.html)]]