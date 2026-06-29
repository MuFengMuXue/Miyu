**Resources**

[[]][Home](http://www.net-snmp.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Net-SNMP "wikipedia:Net-SNMP")

From Wikipedia, the free encyclopedia:

***Net-SNMP** is a suite of software for using and deploying the **SNMP** protocol (v1, v2c and v3 and the AgentX subagent protocol). It supports IPv4, IPv6, IPX, AAL5, Unix domain sockets and other transports. It contains a generic client library, a suite of command line applications, a highly extensible SNMP agent, perl modules and python modules.*

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Agent configuration]](#Agent_configuration)
    -   [[2.1] [SNMPv3 Users]](#SNMPv3_Users)
        -   [[2.1.1] [net-snmp-create-v3-user]](#net-snmp-create-v3-user)
        -   [[2.1.2] [Manual creation]](#Manual_creation)
    -   [[2.2] [Agent Configuration]](#Agent_Configuration_2)
        -   [[2.2.1] [agentAddress]](#agentAddress)
        -   [[2.2.2] [EngineID]](#EngineID)
        -   [[2.2.3] [Access Control]](#Access_Control)
            -   [[2.2.3.1] [SNMPv3]](#SNMPv3)
            -   [[2.2.3.2] [SNMPv1 and SNMPv2c]](#SNMPv1_and_SNMPv2c)
        -   [[2.2.4] [Contact information]](#Contact_information)
        -   [[2.2.5] [Monitoring]](#Monitoring)
            -   [[2.2.5.1] [Network Interfaces]](#Network_Interfaces)
-   [[3] [Client configuration]](#Client_configuration)
    -   [[3.1] [Adding MIBs]](#Adding_MIBs)
-   [[4] [Usage]](#Usage)
    -   [[4.1] [OpenRC]](#OpenRC)
    -   [[4.2] [SNMPWalk]](#SNMPWalk)
        -   [[4.2.1] [SNMPv3]](#SNMPv3_2)
        -   [[4.2.2] [SNMPv2c]](#SNMPv2c)
-   [[5] [Troubleshooting]](#Troubleshooting)

## [Installation]

### [USE flags]

### [USE flags for] [net-analyzer/net-snmp](https://packages.gentoo.org/packages/net-analyzer/net-snmp) [[]] [Software for generating and retrieving SNMP data]

  --------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------
  [`X`](https://packages.gentoo.org/useflags/X)                         Add support for X11
  [`bzip2`](https://packages.gentoo.org/useflags/bzip2)                 Enable bzip2 compression support
  [`doc`](https://packages.gentoo.org/useflags/doc)                     Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`elf`](https://packages.gentoo.org/useflags/elf)                     Enable the use of elf utils to check uptime on some systems
  [`ipv6`](https://packages.gentoo.org/useflags/ipv6)                   Add support for IP version 6
  [`kmem`](https://packages.gentoo.org/useflags/kmem)                   Enable usage of /dev/kmem
  [`lm-sensors`](https://packages.gentoo.org/useflags/lm-sensors)       Add linux lm-sensors (hardware sensors) support
  [`mfd-rewrites`](https://packages.gentoo.org/useflags/mfd-rewrites)   Use MFD rewrites of mib modules where available
  [`minimal`](https://packages.gentoo.org/useflags/minimal)             Install a very minimal build (disables, for example, plugins, fonts, most drivers, non-critical features)
  [`mysql`](https://packages.gentoo.org/useflags/mysql)                 Add mySQL Database support
  [`pcap`](https://packages.gentoo.org/useflags/pcap)                   Install snmppcap which reads from PCAP files and writes to the SNMP transport
  [`pci`](https://packages.gentoo.org/useflags/pci)                     Use libpci (from sys-apps/pciutils) to look up network interface description. This feature is only available on Linux.
  [`pcre`](https://packages.gentoo.org/useflags/pcre)                   Add support for Perl Compatible Regular Expressions in process table filtering.
  [`perl`](https://packages.gentoo.org/useflags/perl)                   Add optional support/bindings for the Perl language
  [`python`](https://packages.gentoo.org/useflags/python)               Add optional support/bindings for the Python language
  [`rpm`](https://packages.gentoo.org/useflags/rpm)                     Enable monitoring of app-arch/rpm. This flag requires the bzip2 and zlib flags to be enabled as well.
  [`selinux`](https://packages.gentoo.org/useflags/selinux)             !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`smux`](https://packages.gentoo.org/useflags/smux)                   Enable support for the legacy smux protocol (superseded by agentx)
  [`ssl`](https://packages.gentoo.org/useflags/ssl)                     Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  [`tcpd`](https://packages.gentoo.org/useflags/tcpd)                   Add support for TCP wrappers
  [`ucd-compat`](https://packages.gentoo.org/useflags/ucd-compat)       Build UCD compatibility library. Increases significantly the install size.
  [`valgrind`](https://packages.gentoo.org/useflags/valgrind)           Enable annotations for accuracy. May slow down runtime slightly. Safe to use even if not currently using dev-debug/valgrind
  [`zlib`](https://packages.gentoo.org/useflags/zlib)                   Add support for zlib compression
  --------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-21 05:26] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

The global USE flag *snmp* enables support for SNMP in other packages. Enabling this USE flag will pull in [[[net-analyzer/net-snmp]](https://packages.gentoo.org/packages/net-analyzer/net-snmp)[]] automatically:

[FILE] **`/etc/portage/make.conf`**

    USE="... snmp ..."

### [Emerge]

After setting the *snmp* USE flag globally, your system must be updated for the changes take effect:

`root `[`#`]`emerge --ask --changed-use --deep @world`

To install [[[net-analyzer/net-snmp]](https://packages.gentoo.org/packages/net-analyzer/net-snmp)[]] manually, if it isn\'t already pulled in:

`root `[`#`]`emerge --ask net-snmp`

## [Agent configuration]

** Warning**\
NEVER use the default communities which are called **public** and **private**, these are a potential security risk, even if SNMP access is secured with an IP access list.

Net-SNMP\'s Agent typically uses 3 configuration files:

-   [/etc/snmp/snmpd.conf] - The main configuration file.
-   [/usr/share/snmp/snmpd.conf] - Secondary configuration files, where SNMPv3 users are defined when using [net-snmp-create-v3-user].
-   [/var/lib/net-snmp/snmpd.conf] - The agent service file, rarely edited manually.

### [SNMPv3 Users]

** Important**\
SNMPv3 users can only be modified while the agent ([snmpd]) is stopped.

If using SNMPv3, users must be created before the agent is configured. They can be added by using [net-snmp-create-v3-user], or manually editing [/var/lib/net-snmp/snmpd.conf] before the agent starts.

#### [net-snmp-create-v3-user]

[net-snmp-create-v3-user] can be used to create SNMPv3 users. By default it will create a *read-write* user with **MD5** authentication and **DES** encryption.

To add a *read-only* user with **SHA-512** authentication and **AES** encryption.

`root `[`#`]`net-snmp-create-v3-user -ro -A "super secret auth passphrase" -X "super secret priv passphrase" -a SHA-512 -x AES my_user`

    adding the following line to /var/lib/net-snmp/snmpd.conf:
       createUser my_ser SHA "super secret auth passphrase" AES "super secret priv passphrase"
    adding the following line to /usr/share/snmp/snmpd.conf:
       rouser my_user

#### [Manual creation]

** Important**\
The config file for SNMPv3 users is under [/var/lib/] not [/etc/].

[FILE] **`/var/lib/net-snmp/snmpd.conf`Add a user with a SHA1 authentication and AES128 encryption.**

    createUser my_user SHA "super secret auth passphrase" AES "super secret priv passphrase"

[FILE] **`/var/lib/net-snmp/snmpd.conf`Add a user with a SHA512 authentication and AES128 encryption.**

    createUser my_user SHA-512 "super secret auth passphrase" AES "super secret priv passphrase"

** Tip**\
More information is available under the *SNMPv3 USM Users* section of [man snmpd.conf].

### [Agent Configuration]

SNMP Agent configuration is specified in [/etc/snmp/snmpd.conf]. An example is available at [/etc/snmp/snmpd.conf.example].

** Tip**\
More examples are available under [man snmpd.examples].

#### [agentAddress]

The `agentAddress` config directive defines what interfaces **snmpd** will listen on. To which specific IP interface the SNMP daemon will be bound to:

[FILE] **`/etc/snmp/snmpd.conf`Make **snmpd** listen on *198.51.100.1:161***

    agentAddress  udp:198.51.100.1:161

** Tip**\
If left undefined, **snmpd** will listen on `udp:127.0.0.1:161`.

#### [EngineID]

By default, Net-SNMP derives the management engine ID from the *eth0\'*s MAC address, to change which network interface is used:

[FILE] **`/etc/snmp/snmpd.conf`Derive the *EngineID* from `ens4f0`**

    engineIDNic ens4f0

#### [Access Control]

##### [SNMPv3]

To allow *read-only* access from the `my_user` *user*:

[FILE] **`/usr/share/snmp/snmpd.conf`Allow *read-only* from **my_user****

    rouser my_user

** Tip**\
This entry is automatically added when using [net-snmp-create-v3-user].

** Note**\
This can be configured in either [/usr/share/snmp/snmpd.conf] or [/etc/snmp/snmpd.conf].

##### [SNMPv1 and SNMPv2c]

To allow *read-only* access from the from `192.0.2.0/24` network using the `my-own-SNMP-community`:

[FILE] **`/etc/snmp/snmpd.conf`**

    # Which SNMP MIB's are accessible on this system, here 'all'
    view all    included  .1                               80

    # From which IP network SNMP polling is allowed. Here 'my-own-SNMP-community' for Read-Only access.
    rocommunity  my-own-SNMP-community 192.0.2.0/24

#### [Contact information]

It is suggested to put valid data into the *system* group fields. This data will be visible in monitoring software if alerts are thrown. Failure to provide descriptive system information can make alert responses much more difficult.

[FILE] **`/etc/snmp/snmpd.conf`**

    #Location and system contact data
    sysLocation London
    sysContact Admin <Admin@example.com>
    sysName gentoo-nfs.example.com
    sysDescr Gentoo NFS Server Node1

** Note**\
In a large networks or enterprises, it can be hard to describe where particular network equipment has been placed. A descriptive location can seriously help, and should make sense to someone who has never worked with the alerting device before. The person responding to the alert will likely be thankful that a location tag was helpful.

#### [Monitoring]

By default, [smnpd] will monitor network interfaces, disk usage, processes, and system load.

##### [Network Interfaces]

To restrict the agent to only list information about specific network interfaces:

[FILE] **`/etc/snmp/snmpd.conf`Only gather stats about `ens4f0`**

    include_ifmib_iface_prefix ens4f0

## [Client configuration]

[net-snmp] tools read config from [\~/.snmp].

### [Adding MIBs]

To add a MIB, create [\~/.snmp/mibs] then copy the file there:

`user `[`$`]`mkdir --parents ~/.snmp/mibs`

`user `[`$`]`cp ~/Downloads/my-new.mib ~/.snmp/mibs`

## [Usage]

### [OpenRC]

To start the SNMP daemon:

`root `[`#`]`rc-service snmpd start`

### [SNMPWalk]

To test access to a SNMP agent, [snmpwalk] can be used:

#### [SNMPv3]

`user `[`$`]`snmpwalk -v 3 -a SHA-512 -A "super secret auth passphrase" -x AES -X "super secret priv passphrase" -u my_user -l authPriv 198.51.100.1`

#### [SNMPv2c]

To test SNMP access the SNMP polling host has be within the allowed IP range of *192.0.2.0/24*.

-   Substitute the IP **198.51.100.1** with the target host where SNMP access has been enabled
-   Substitute the SNMP community **my-own-SNMP-community** with your own SNMP community

This test command is executed from polling client into the target IP network:

`user `[`$`]`snmpwalk -v2c -c my-own-SNMP-community 198.51.100.1`

## [Troubleshooting]

Verify the SNMP daemon is running on a particular host:

`root `[`#`]`ss -tulpn | grep snmp`

    udp   UNCONN 0      0            0.0.0.0:161        0.0.0.0:*    users:(("snmpd",pid=2138,fd=6))