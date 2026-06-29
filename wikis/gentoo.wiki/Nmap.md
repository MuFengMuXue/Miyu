[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Nmap&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://nmap.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Nmap "wikipedia:Nmap")

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/nmap)

Nmap ( **N**etwork **Map**per) is an open source recon tool used to check for open ports, what is running on those ports, and metadata about the daemons servicing those ports.

Nmap was written by Gordon Lyon.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
    -   [[1.2] [USE flags]](#USE_flags)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [OS fingerprinting]](#OS_fingerprinting)
    -   [[2.2] [Easter eggs]](#Easter_eggs)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Installation]

### [Emerge]

Installing Nmap is a standard emerge; no configuration should be required. Pay attention to the optional USE flags in case there are some \"non-stock\" features that you might find useful. See the USE flags list below before running the following command:

`root `[`#`]`emerge --ask net-analyzer/nmap`

A quick way to add many USE flags at once for Nmap:

`root `[`#`]`echo ">=net-analyzer/nmap-6.25 gtk ipv6 lua nls ssl ncat ndiff nmap-update nping" >> /etc/portage/package.use`

### [USE flags]

### [USE flags for] [net-analyzer/nmap](https://packages.gentoo.org/packages/net-analyzer/nmap) [[]] [Network exploration tool and security / port scanner]

  ----------------------------------------------------------------- --------------------------------------------------------------------------------------
  [`+nse`](https://packages.gentoo.org/useflags/+nse)               Include support for the Nmap Scripting Engine (NSE)
  [`ipv6`](https://packages.gentoo.org/useflags/ipv6)               Add support for IP version 6
  [`libssh2`](https://packages.gentoo.org/useflags/libssh2)         Enable SSH support through net-libs/libssh2
  [`ncat`](https://packages.gentoo.org/useflags/ncat)               Install the ncat utility
  [`ndiff`](https://packages.gentoo.org/useflags/ndiff)             Install the ndiff utility
  [`nls`](https://packages.gentoo.org/useflags/nls)                 Add Native Language Support (using gettext - GNU locale utilities)
  [`nping`](https://packages.gentoo.org/useflags/nping)             Install the nping utility
  [`ssl`](https://packages.gentoo.org/useflags/ssl)                 Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  [`symlink`](https://packages.gentoo.org/useflags/symlink)         Install symlink to nc
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  [`zenmap`](https://packages.gentoo.org/useflags/zenmap)           Install the GTK+ based nmap GUI, zenmap
  ----------------------------------------------------------------- --------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-16 22:44] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

## [Usage]

Nmap is an extremely powerful tool. Entire books have been written about its use, and there is more information than we could possibly do justice to here. The following section will a brief overview in order to give users a feel for its output. If you\'d like a more thorough tutorial, the [man page](https://linux.die.net/man/1/nmap) is an excellent guide.

To see if port 80 was open at example.com, run nmap with the `-p` option to specify the port:

`user `[`$`]`nmap example.com -p 80`

To check multiple ports, port 80 and port 8080 for example, separate each port with a comma:

`user `[`$`]`nmap example.com -p 80,8080,443`

To check for open SQL ports, run:

`user `[`$`]`nmap example.com -p 1433,3306,5432`

To check a wide range of ports, such as ports 1-1000, separate the low-end & high-end of the range with a - (dash):

`user `[`$`]`nmap example.com -p 1-1000`

Specify multiple port ranges by:

`user `[`$`]`nmap example.com -p 6660-6670,6690-6700`

To find out if a server was running an IRC daemon, and then find out information about that IRC daemon do the same as above but add the `-sV` option:

`user `[`$`]`nmap -sV irc.afraidirc.net -p 6660-6670,6690-6700`

    Starting Nmap 6.25 ( http://nmap.org ) at 2013-09-07 20:11 CDT
    Nmap scan report for irc.afraidirc.net (174.122.223.81)
    Host is up (0.060s latency).
    rDNS record for 174.122.223.81: 51.df.7aae.static.theplanet.com
    PORT     STATE  SERVICE  VERSION
    6660/tcp closed unknown
    6661/tcp closed unknown
    6662/tcp closed radmind
    6663/tcp closed unknown
    6664/tcp closed unknown
    6665/tcp open   irc      ratbox, charybdis, or ircd-seven ircd
    6666/tcp open   irc
    6667/tcp open   irc      ratbox, charybdis, or ircd-seven ircd
    6668/tcp open   irc
    6669/tcp open   irc
    6670/tcp closed irc
    6690/tcp closed unknown
    6691/tcp closed unknown
    6692/tcp closed unknown
    6693/tcp closed unknown
    6694/tcp closed unknown
    6695/tcp open   irc      ratbox, charybdis, or ircd-seven ircd
    6696/tcp open   irc      ratbox, charybdis, or ircd-seven ircd
    6697/tcp open   irc      ratbox, charybdis, or ircd-seven ircd
    6698/tcp open   irc      ratbox, charybdis, or ircd-seven ircd
    6699/tcp open   irc      ratbox, charybdis, or ircd-seven ircd
    6700/tcp closed carracho
    Service Info: Host: BloodyMary.AfraidIRC.net

    Service detection performed. Please report any incorrect results at http://nmap.org/submit/
    Nmap done: 1 IP address (1 host up) scanned in 12.14 seconds

The output above shows the hostname as defined in the IRC daemon configuration, as well as the IRC daemon version name. In this case, it happens to be *Charybdis*, which is a fork of ratbox. ircd-seven is also a fork of ratbox, so Nmap is unable to tell exactly which IRC daemon is in use. It is capable of providing the IRC daemon \"family\".

Similar port scans can be invoked in order to get information about web servers, or other services running on a target machines. The following example will get the web server and the operating system running on a machine at Google.com:

`user `[`$`]`nmap -sV -p 80 google.com`

    Starting Nmap 6.25 ( http://nmap.org ) at 2013-09-07 20:16 CDT
    Nmap scan report for google.com (74.125.224.66)
    Host is up (0.022s latency).
    rDNS record for 74.125.224.66: lax17s02-in-f2.1e100.net
    PORT   STATE SERVICE VERSION
    80/tcp open  http    Google httpd 2.0 (GFE)
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

    Service detection performed. Please report any incorrect results at http://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 6.50 seconds

### [OS fingerprinting]

To fingerprint an operating system, use:

`root `[`#`]`nmap -O -v localhost`

### [Easter eggs]

At least one Easter egg is contained within Nmap, if more are found please document them here in the wiki!

`user `[`$`]`nmap -oS - google.com`

    STArt1nG Nmap 6.25 ( Http://nMAp.oRg ) aT 2013-09-07 20:22 CDT
    Nmap ScaN rEpOrt f0r g00gLe.c0m (74.125.224.71)
    H0St |s up (0.012z lat3ncy).
    rdNS r3coRd For 74.125.224.71: lax17S02-in-f7.1E100.n3t
    Not Sh0wn: 998 F!lTErEd p0rt$
    PORT    $T4T3 seRVIc3
    80/Tcp  0p3n  HTTp
    443/tCP Open  hTtps

    Nmap d0nE: 1 Ip adDr3SS (1 Host up) $canned 1N 5.05 $3condz

## [See also]

-   [Wireshark](https://wiki.gentoo.org/wiki/Wireshark "Wireshark") --- a free and open-source packet analyzer.

## [External resources]