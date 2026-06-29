[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=OpenConnect&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[[]][Home](https://www.infradead.org/openconnect/)

[[]][Package information](https://packages.gentoo.org/packages/net-vpn/openconnect)

[[]][Wikipedia](https://en.wikipedia.org/wiki/OpenConnect "wikipedia:OpenConnect")

[[]][GitLab](https://gitlab.com/openconnect/openconnect)

[[]][Official project wiki](https://project.org/wiki/)

[[]][Bugs (upstream)](https://gitlab.com/openconnect/openconnect/-/issues)

**OpenConnect** is a cross-platform multi-protocol SSL VPN client which supports a number of VPN protocols:

-   Cisco AnyConnect (\--protocol=anyconnect)
-   Array Networks SSL VPN (\--protocol=array)
-   Juniper SSL VPN (\--protocol=nc)
-   Pulse Connect Secure (\--protocol=pulse)
-   Palo Alto Networks GlobalProtect SSL VPN (\--protocol=gp)
-   F5 Big-IP SSL VPN (\--protocol=f5)
-   Fortinet Fortigate SSL VPN (\--protocol=fortinet)

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Additional software]](#Additional_software)
    -   [[1.4] [Kernel]](#Kernel)
        -   [[1.4.1] [Snippet]](#Snippet)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Environment variables]](#Environment_variables)
    -   [[2.2] [Files]](#Files)
    -   [[2.3] [Service]](#Service)
        -   [[2.3.1] [OpenRC]](#OpenRC)
        -   [[2.3.2] [runit]](#runit)
        -   [[2.3.3] [systemd]](#systemd)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [Troubleshooting]](#Troubleshooting)
-   [[5] [Removal]](#Removal)
    -   [[5.1] [Unmerge]](#Unmerge)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)
-   [[8] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [net-vpn/openconnect](https://packages.gentoo.org/packages/net-vpn/openconnect) [[]] [Free client for Cisco AnyConnect SSL VPN software]

  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+gnutls`](https://packages.gentoo.org/useflags/+gnutls)         Prefer net-libs/gnutls as SSL/TLS provider (ineffective with USE=-ssl)
  [`doc`](https://packages.gentoo.org/useflags/doc)                 Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`gssapi`](https://packages.gentoo.org/useflags/gssapi)           Build GSSAPI support
  [`libproxy`](https://packages.gentoo.org/useflags/libproxy)       Enable proxy support
  [`lz4`](https://packages.gentoo.org/useflags/lz4)                 Enable support for lz4 compression (as implemented in app-arch/lz4)
  [`nls`](https://packages.gentoo.org/useflags/nls)                 Add Native Language Support (using gettext - GNU locale utilities)
  [`pskc`](https://packages.gentoo.org/useflags/pskc)               Enable PSKC file storage of HOTP/TOTP keys
  [`selinux`](https://packages.gentoo.org/useflags/selinux)         !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`smartcard`](https://packages.gentoo.org/useflags/smartcard)     Enable smartcard support
  [`stoken`](https://packages.gentoo.org/useflags/stoken)           Enable stoken support
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-05 16:57] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[net-vpn/openconnect]](https://packages.gentoo.org/packages/net-vpn/openconnect)[]]:

`root `[`#`]`emerge --ask net-vpn/openconnect`

### [Additional software]

-   [[[net-vpn/vpnc-scripts]](https://packages.gentoo.org/packages/net-vpn/vpnc-scripts)[]]

### [Kernel]

[KERNEL] **Enable support for TUN**

    Device Drivers --->
     [*] Network device support Search for <code>CONFIG_NETDEVICE</code> to find this item. --->
       [*] Network core driver support Search for <code>CONFIG_NET_CORE</code> to find this item. --->
         <*/M> Universal TUN/TAP device driver support Search for <code>CONFIG_TUN</code> to find this item.

#### [Snippet]

Example shows building as a module:

[FILE] **`/etc/kernel/config.d/tun.config`**

    CONFIG_TUN=m

## [Configuration]

### [Environment variables]

-   `VAR1`
-   `VAR2`

### [Files]

-   [/etc/conf.d/openconnect] - Global (system wide) configuration file.
-   [/etc/openconnect/vpn0.password] - Non-interactive (optional) user password configuration file.

### [Service]

#### [OpenRC]

Start the OpenConnect service:

`root `[`#`]`rc-service openconnect start`

Add OpenConnect to the default runlevel (optional):

`root `[`#`]`rc-update add openconnect default`

Restart the OpenConnect service:

`root `[`#`]`rc-service openconnect restart`

Reload OpenConnect configuration files:

`root `[`#`]`rc-service openconnect reload`

#### [runit]

#### [systemd]

## [Usage]

### [Invocation]

`user `[`$`]`openconnect --help`

    Usage:  openconnect [options] <server>
    Open client for multiple VPN protocols, version v9.12-unknown

    Using GnuTLS 3.8.0. Features present: TPM, TPMv2, PKCS#11, HOTP software token, TOTP software token, System keys, DTLS, ESP
          --config=CONFIGFILE         Read options from config file
      -V, --version                   Report version number
      -h, --help                      Display help text

    Set VPN protocol:
          --protocol=anyconnect       Compatible with Cisco AnyConnect SSL VPN, as well as ocserv (default)
          --protocol=nc               Compatible with Juniper Network Connect
          --protocol=gp               Compatible with Palo Alto Networks (PAN) GlobalProtect SSL VPN
          --protocol=pulse            Compatible with Pulse Connect Secure SSL VPN
          --protocol=f5               Compatible with F5 BIG-IP SSL VPN
          --protocol=fortinet         Compatible with FortiGate SSL VPN
          --protocol=array            Compatible with Array Networks SSL VPN

    Authentication:
      -u, --user=NAME                 Set login username
          --no-passwd                 Disable password/SecurID authentication
          --non-inter                 Do not expect user input; exit if it is required
          --passwd-on-stdin           Read password from standard input
          --authgroup=GROUP           Select GROUP from authentication dropdown (may be known
                                      as "realm", "domain", "gateway"; protocol-dependent)
      -F, --form-entry=FORM:OPT=VALUE Provide authentication form responses
      -c, --certificate=CERT          Use SSL client certificate CERT
      -k, --sslkey=KEY                Use SSL private key file KEY
      -e, --cert-expire-warning=DAYS  Warn when certificate lifetime < DAYS
      -g, --usergroup=GROUP           Set path of initial request URL
      -p, --key-password=PASS         Set key passphrase or TPM SRK PIN
          --external-browser=BROWSER  Set external browser executable
          --key-password-from-fsid    Key passphrase is fsid of file system
          --token-mode=MODE           Software token type: rsa, totp, hotp or oidc
          --token-secret=STRING       Software token secret or oidc token
                                      (NOTE: libstoken (RSA SecurID) disabled in this build)
                                      (NOTE: Yubikey OATH disabled in this build)

    Server validation:
          --servercert=FINGERPRINT    Accept only server certificate with this fingerprint
          --no-system-trust           Disable default system certificate authorities
          --cafile=FILE               Cert file for server verification

    Internet connectivity:
          --server=SERVER             Set VPN server
      -P, --proxy=URL                 Set proxy server
          --proxy-auth=METHODS        Set proxy authentication methods
          --no-proxy                  Disable proxy
          --libproxy                  Use libproxy to automatically configure proxy
                                      (NOTE: libproxy disabled in this build)
          --reconnect-timeout=SECONDS Reconnection retry timeout (default is 300 seconds)
          --resolve=HOST:IP           Use IP when connecting to HOST
          --sni=HOST                  Always send HOST as TLS client SNI (domain fronting)
          --passtos                   Copy TOS / TCLASS field into DTLS and ESP packets
          --dtls-local-port=PORT      Set local port for DTLS and ESP datagrams

    Authentication (two-phase):
      -C, --cookie=COOKIE             Use authentication cookie COOKIE
          --cookie-on-stdin           Read cookie from standard input
          --authenticate              Authenticate only and print login info
          --cookieonly                Fetch and print cookie only; don't connect
          --printcookie               Print cookie before connecting

    Process control:
      -b, --background                Continue in background after startup
          --pid-file=PIDFILE          Write the daemon's PID to this file
      -U, --setuid=USER               Drop privileges after connecting

    Logging (two-phase):
      -l, --syslog                    Use syslog for progress messages
      -v, --verbose                   More output
      -q, --quiet                     Less output
          --dump-http-traffic         Dump HTTP authentication traffic (implies --verbose)
          --timestamp                 Prepend timestamp to progress messages

    VPN configuration script:
      -i, --interface=IFNAME          Use IFNAME for tunnel interface
      -s, --script=SCRIPT             Shell command line for using a vpnc-compatible config script
                                      default: "/etc/vpnc/vpnc-script"
      -S, --script-tun                Pass traffic to 'script' program, not tun

    Tunnel control:
          --disable-ipv6              Do not ask for IPv6 connectivity
      -x, --xmlconfig=CONFIG          XML config file
      -m, --mtu=MTU                   Request MTU from server (legacy servers only)
          --base-mtu=MTU              Indicate path MTU to/from server
      -d, --deflate                   Enable stateful compression (default is stateless only)
      -D, --no-deflate                Disable all compression
          --force-dpd=INTERVAL        Set Dead Peer Detection interval (in seconds)
          --pfs                       Require perfect forward secrecy
          --no-dtls                   Disable DTLS and ESP
          --dtls-ciphers=LIST         OpenSSL ciphers to support for DTLS
      -Q, --queue-len=LEN             Set packet queue limit to LEN pkts

    Local system information:
          --useragent=STRING          HTTP header User-Agent: field
          --local-hostname=STRING     Local hostname to advertise to server
          --os=STRING                 OS type to report. Allowed values are the following:
                                      linux, linux-64, win, mac-intel, android, apple-ios
          --version-string=STRING     reported version string during authentication
                                      (default: v9.12-unknown)

    Trojan binary (CSD) execution:
          --csd-user=USER             Drop privileges during trojan execution
          --csd-wrapper=SCRIPT        Run SCRIPT instead of trojan binary
          --force-trojan=INTERVAL     Set minimum interval between trojan runs (in seconds)

    Server bugs:
          --no-external-auth          Do not offer or use auth methods requiring external browser
          --no-http-keepalive         Disable HTTP connection re-use
          --no-xmlpost                Do not attempt XML POST authentication
          --allow-insecure-crypto     Allow use of the ancient, insecure 3DES and RC4 ciphers

    Multiple certificate authentication (MCA):
          --mca-certificate=MCACERT   Use MCA certificate MCACERT
          --mca-key=MCAKEY            Use MCA key MCAKEY
          --mca-key-password=MCAPASS  Passphrase MCAPASS for MCACERT/MCAKEY

    For assistance with OpenConnect, please see the web page at
      https://www.infradead.org/openconnect/mail.html

## [Troubleshooting]

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose net-vpn/openconnect`

## [See also]

-   [OpenVPN](https://wiki.gentoo.org/wiki/OpenVPN "OpenVPN") --- software that enables the creation of secure point-to-point or site-to-site connections.
-   [vpnc](https://wiki.gentoo.org/wiki/Vpnc "Vpnc") --- IPsec (Cisco/Juniper) VPN concentrator client

## [External resources]

-   [https://wiki.archlinux.org/title/OpenConnect](https://wiki.archlinux.org/title/OpenConnect)
-   [https://deepwiki.com/openconnect/openconnect/1.2-command-line-usage](https://deepwiki.com/openconnect/openconnect/1.2-command-line-usage)

## [References]