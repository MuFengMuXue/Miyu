[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Bcache&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://bcache.evilpiepirate.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Bcache "wikipedia:Bcache")

[[]][[#bcache](ircs://irc.libera.chat/#bcache)] ([[webchat](https://web.libera.chat/#bcache)])

[[]][GitWeb](https://evilpiepirate.org/git/bcache-tools)

**bcache** is a Linux [kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") block layer cache. It allows one or more fast disk drives such as flash-based solid state drives ([SSDs](https://wiki.gentoo.org/wiki/SSD "SSD")) to act as a cache for one or more slower disk drives.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [See also]](#See_also)
-   [[3] [External resources]](#External_resources)

## [Installation]

### [Kernel]

Activate the following kernel options:

[KERNEL] **Enable block device support in the Kernel (`CONFIG_BCACHE`)**

    Device Drivers --->
       Multiple devices driver support (RAID and LVM) --->
          <*>   Block device as cache

### [Emerge]

Install [[[sys-fs/bcache-tools]](https://packages.gentoo.org/packages/sys-fs/bcache-tools)[]]:

`root `[`#`]`emerge --ask sys-fs/bcache-tools`

## [See also]

-   [Bcachefs](https://wiki.gentoo.org/wiki/Bcachefs "Bcachefs") --- a fully-featured [B-tree](https://en.wikipedia.org/wiki/B-tree "wikipedia:B-tree") [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") based on [bcache].

## [External resources]

-   [Howto bcache](https://forums.gentoo.org/viewtopic-t-959542.html) - A Gentoo Forums thread on using bcache.
-   [Arch wiki](https://wiki.archlinux.org/index.php/Bcache) - The Bcache article on found on the Arch wiki.
-   [Patrick\'s Blog](http://gentooexperimental.org/~patrick/weblog/archives/2014-09.html#e2014-09-21T13_59_16.txt) - [Patrick Lauer (Patrick) ](https://wiki.gentoo.org/wiki/User:Patrick "User:Patrick"), a Gentoo developer, wrote a few short entries on his blog concerning the use of bcache and a multi-disk SATA array back in September, 2014. Read about it here.
-   [Pommi\'s blog - SSD caching using Linux and bcache](https://cloud-infra.engineer/ssd-caching-using-linux-and-bcache/) - A 2013 blog entry containing details of setting up bcache.