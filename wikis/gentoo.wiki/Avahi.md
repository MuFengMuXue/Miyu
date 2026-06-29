**Resources**

[[]][Home](https://www.avahi.org/)

[[]][Package information](https://packages.gentoo.org/packages/net-dns/avahi)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Avahi_(software) "wikipedia:Avahi (software)")

**avahi** is a zeroconf service discovery and publishing program. A common use for it is to be able to connect to machines via `yourhostname.local` within your LAN.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Server]](#Server)
    -   [[1.4] [Client]](#Client)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Server Services]](#Server_Services)
        -   [[2.1.1] [systemd]](#systemd)
        -   [[2.1.2] [OpenRC]](#OpenRC)
    -   [[2.2] [Client Files]](#Client_Files)
    -   [[2.3] [Service Discovery]](#Service_Discovery)
-   [[3] [Troubleshooting]](#Troubleshooting)
-   [[4] [External resources]](#External_resources)

## [Installation]

### [Kernel]

[KERNEL] **Required options**

     Networking support  --->
       Networking options  --->
         [*] IP: multicasting Search for <code>CONFIG_IP_MULTICAST</code> to find this item.

### [USE flags]

Some packages are aware of the [[[zeroconf]](https://packages.gentoo.org/useflags/zeroconf)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") pulling in avahi.

### [USE flags for] [net-dns/avahi](https://packages.gentoo.org/packages/net-dns/avahi) [[]] [System which facilitates service discovery on a local network]

  ------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+dbus`](https://packages.gentoo.org/useflags/+dbus)                                 Enable dbus support for anything that needs it (gpsd, gnomemeeting, etc)
  [`+introspection`](https://packages.gentoo.org/useflags/+introspection)               Add support for GObject based introspection
  [`autoipd`](https://packages.gentoo.org/useflags/autoipd)                             Build and install the IPv4LL (RFC3927) network address configuration daemon
  [`bookmarks`](https://packages.gentoo.org/useflags/bookmarks)                         Install the avahi-bookmarks application (requires dev-python/twisted)
  [`doc`](https://packages.gentoo.org/useflags/doc)                                     Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`gdbm`](https://packages.gentoo.org/useflags/gdbm)                                   Add support for sys-libs/gdbm (GNU database libraries)
  [`gtk`](https://packages.gentoo.org/useflags/gtk)                                     Use gtk3 for the avahi utilities to build the avahi-ui-gtk3 library
  [`howl-compat`](https://packages.gentoo.org/useflags/howl-compat)                     Enable compat libraries for howl
  [`mdnsresponder-compat`](https://packages.gentoo.org/useflags/mdnsresponder-compat)   Enable compat libraries for mDNSResponder
  [`nls`](https://packages.gentoo.org/useflags/nls)                                     Add Native Language Support (using gettext - GNU locale utilities)
  [`python`](https://packages.gentoo.org/useflags/python)                               Add optional support/bindings for the Python language
  [`qt6`](https://packages.gentoo.org/useflags/qt6)                                     Add support for the Qt 6 application and UI framework
  [`selinux`](https://packages.gentoo.org/useflags/selinux)                             !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`systemd`](https://packages.gentoo.org/useflags/systemd)                             Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`test`](https://packages.gentoo.org/useflags/test)                                   Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-21 05:26] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Server]

[[[net-dns/avahi]](https://packages.gentoo.org/packages/net-dns/avahi)[]] allows your host to offer services on the `.local` domain.

`root `[`#`]`emerge --ask net-dns/avahi`

### [Client]

[[[sys-auth/nss-mdns]](https://packages.gentoo.org/packages/sys-auth/nss-mdns)[]] allows clients on your host to access services on the `.local` domain.

`root `[`#`]`emerge --ask sys-auth/nss-mdns`

## [Configuration]

### [Server Services]

#### [systemd]

Enable the server to start whenever [systemd] thinks it is appropriate:

`root `[`#`]`systemctl enable avahi-daemon.service`

If you want to use it right away, also start the service:

`root `[`#`]`systemctl start avahi-daemon.service`

#### [OpenRC]

Be sure to add the service to the default runlevel for the server daemon to start on system boot. Do so with the [rc-update] command:

`root `[`#`]`rc-update add avahi-daemon default`

Start the service (without restarting) with the [rc-service] command:

`root `[`#`]`rc-service avahi-daemon start`

### [Client Files]

Add the appropriate mdns into the hosts line in [/etc/nsswitch.conf], An example line looks like:

[FILE] **`/etc/nsswitch.conf`**

    hosts:       files mdns_minimal [NOTFOUND=return] dns mdns

Once this is installed it should be possible to ping the hostname of the machine appending `.local`. For example:

`user `[`$`]`ping yourhostname.local`

### [Service Discovery]

To configure Avahi to advertise zeroconf services to clients, add configurations in `/etc/avahi/services`. For example, this snippet in `/etc/avahi/services/smb.service` which will make SMB services discoverable

    <?xml version="1.0" standalone='no'?>
    <!DOCTYPE service-group SYSTEM "avahi-service.dtd">
    <service-group>
     <name replace-wildcards="yes">%h</name>
     <service>
       <type>_smb._tcp</type>
       445</port>
     </service>
     <service>
       <type>_device-info._tcp</type>
       0</port>
       <txt-record>model=RackMac</txt-record>
     </service>
    </service-group>

## [Troubleshooting]

Check [avahi-daemon] is running and listen for 5353 UDP:

`root `[`#`]`ss -ltunp | grep 5353`

Output:

    udp   UNCONN 0      0                          0.0.0.0:5353        0.0.0.0:*     users:(("avahi-daemon",pid=4072,fd=13))
    udp   UNCONN 0      0                                *:5353              *:*     users:(("avahi-daemon",pid=4072,fd=14))

Commands like [[[host(1)]](https://man.archlinux.org/man/host.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] and [[[dig(1)]](https://man.archlinux.org/man/dig.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] don\'t use [[[nsswitch.conf(5)]](https://man.archlinux.org/man/nsswitch.conf.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")], so they can\'t be used for Avahi diagnostics. Instead, use [[[getent(1)]](https://man.archlinux.org/man/getent.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]. For example:

`user `[`$`]`getent hosts gentoo-desktop.local`

Output when [mdns_minimal] in [/etc/nsswitch.conf]:

`fe80::bbbd:5967:6af8:9d27 gentoo-desktop.local`

## [External resources]

-   [RFC6762: Multicast DNS](https://www.rfc-editor.org/rfc/rfc6762.html)
-   [RFC6763: DNS-Based Service Discovery](https://datatracker.ietf.org/doc/html/rfc6763)
-   [RFC8882: DNS-Based Service Discovery (DNS-SD) Privacy and Security Requirements](https://www.rfc-editor.org/rfc/rfc8882.html)