[djbdns](http://cr.yp.to/djbdns.html) is Daniel J. Bernstein (DJB)\'s suite of DNS tools. It includes both a caching nameserver (dnscache) and an authoritative one (tinydns) amongst other things.

## Contents

-   [[1] [Components]](#Components)
    -   [[1.1] [tinydns]](#tinydns)
    -   [[1.2] [dnscache]](#dnscache)
    -   [[1.3] [axfrdns]](#axfrdns)
    -   [[1.4] [The rest]](#The_rest)
-   [[2] [Daemontools]](#Daemontools)
-   [[3] [Installation]](#Installation)
-   [[4] [Patches]](#Patches)

## [Components]

### [tinydns]

[Tinydns](http://cr.yp.to/djbdns/tinydns.html) is an authoritative nameserver. If you run DNS servers for your own domains, tinydns can do that.

### [dnscache]

[Dnscache](http://cr.yp.to/djbdns/dnscache.html) is a caching-only nameserver. It can perform lookups recursively, or by forwarding them to a (list of) upstream nameservers.

Why is the caching daemon separate from the authoritative one, unlike BIND? [The importance of separating DNS caches from DNS servers](http://cr.yp.to/djbdns/separation.html).

### [axfrdns]

[Axfrdns](http://cr.yp.to/djbdns/axfrdns.html) serves zone transfers. These days, zone transfers are rarely used legitimately, so the daemon runs separately (from, say, tinydns) for security purposes.

There is an associated client, [axfr-get](http://cr.yp.to/djbdns/axfr-get.html).

### [The rest]

These two are rarely used. See the official docs for more information.

-   [walldns](http://cr.yp.to/djbdns/walldns.html), [How to set up a reverse DNS wall](http://cr.yp.to/djbdns/wall.html)
-   [rbldns](http://cr.yp.to/djbdns/rbldns.html), use [rbldnsd](http://www.corpit.ru/mjt/rbldnsd.html) instead

## [Daemontools]

The djbdns daemons all use a service monitor called [daemontools](http://cr.yp.to/daemontools.html) to start and monitor themselves. They sidestep the Gentoo RC (/etc/init.d) system entirely.

The program that starts/monitors each daemon is called **svscan**, and the daemontools ebuild will create an init script for it. So usually, you\'ll want to,

`root `[`#`]`rc-update add svscan default`

At this point, svscan will run on boot, but do nothing. To have it start any daemons, you need to create symlinks to those daemons\' directories in the **/service** directory. For example,

`root `[`#`]`ln -s /var/dnscache /service/dnscache`

After this, daemontools will handle the rest.

## [Installation]

All parts of djbdns can be installed with,

`root `[`#`]`emerge djbdns`

After the installation, you\'ll need to run a configuration command according to the documentation:[axfrdns-conf](http://cr.yp.to/djbdns/axfrdns-conf.html), [dnscache](http://cr.yp.to/djbdns/run-cache-x-home.html), [tinydns](http://cr.yp.to/djbdns/run-server.html).

Gentoo creates users for these three daemons automatically, so if you just want to get started, you can run one or more of the following commands, depending on which daemons you\'re going to use:

`root `[`#`]`axfrdns-conf tinydns dnslog /var/axfrdns /var/tinydns $ip `

`root `[`#`]`dnscache-conf dnscache dnslog /var/dnscache $ip `

`root `[`#`]`tinydns-conf tinydns dnslog /var/tinydns $ip`

You\'ll need to replace \$ip in the commands above with the ip address on which the server will run.

You will also need to inform daemontools of the new services. If you used the commands above,

`root `[`#`]`ln -s /var/axfrdns /service/axfrdns `

`root `[`#`]`ln -s /var/dnscache /service/dnscache `

`root `[`#`]`ln -s /var/tinydns /service/tinydns`

## [Patches]

Djbdns is no longer being developed upstream. All changes now come in the form of patches, most of which will *not* be incorporated into the ebuild. Below is a list of patches that work on Gentoo. The djbdns ebuild support user patches, so to apply these, simply add them to [/etc/portage/patches/net-dns/djbdns].

-   [CVE-2012-1191 Fix](http://michael.orlitzky.com/code/releases/djbdns-1.05-CVE-2012-1911.patch) (by Peter Conrad). References: [CVE-2012-1191](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2012-1191), [Gentoo bug #404959](https://bugs.gentoo.org/show_bug.cgi?id=404959).