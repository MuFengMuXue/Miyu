This page contains [[changes](https://wiki.gentoo.org/index.php?title=Proxychains&diff=1224605)] which are not marked for translation.

[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Proxychains&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines") (Needs to follow blueprint; Improve explanations). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

\

**Resources**

[[]][Home](https://github.com/rofl0r/proxychains-ng/)

[[]][Package information](https://packages.gentoo.org/packages/net-misc/proxychains)

[[]][GitHub](https://github.com/rofl0r/proxychains-ng)

[[]][Official documentation](http://sourceforge.net/projects/proxychains-ng/files)

[proxychains] force any tcp connections to flow through a proxy (or proxy chain). Tool used to secure internet connections.

## [Installation]

[[[net-misc/proxychains]](https://packages.gentoo.org/packages/net-misc/proxychains)[]] does not have USE flags right now.

`root `[`#`]`emerge --ask net-misc/proxychains`

## [DNS leakage]

Proxy chains has \"proxy_dns\" option in /etc/proxychains.conf to prevent \"DNS leaks\", but this options will work only if application support \"Proxy DNS when using socks5\", like Firefox has.

To test if application leaks DNS you can use [Tcpdump](https://wiki.gentoo.org/wiki/Tcpdump "Tcpdump") tool.

To block all DNS request for user ff (simple sandbox for Firefox) in [nftables](https://wiki.gentoo.org/wiki/Nftables "Nftables") use command:

`root `[`#`]`nft add rule filter output meta skuid ff ip daddr !=  drop`

To prevent leakage [[[net-proxy/dnsproxy]](https://packages.gentoo.org/packages/net-proxy/dnsproxy)[]] can be used on remote SSH server with following commands.

At local machine:

`user `[`$`]`ssh -L 6667:0.0.0:6667 root@remove_ssh_ip`

At server:

`root `[`#`]`socat tcp4-listen:6667,reuseaddr,fork UDP:127.0.0.1:53000`

At local machine:

`root `[`#`]`socat udp-listen:53,reuseaddr,fork TCP:127.0.0.1:6667 &`

`root `[`#`]`echo "nameserver 127.0.0.1" > /etc/resolv.conf`

`root `[`#`]`chattr +i /etc/resolv.conf`

Check dnsproxy with command:

`root `[`#`]`dig @127.0.0.1 -p 53 gentoo.org`