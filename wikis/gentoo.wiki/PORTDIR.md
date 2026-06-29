**[] Deprecated article**\
\

This article is **deprecated (obsolete)**. Contents are [no longer relevant], and are intended for historical reference only!

\
TLDR: **Do not use this article!**

Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/PORTDIR/es "PORTDIR (57% translated)")
-   [français](https://wiki.gentoo.org/wiki/PORTDIR/fr "PORTDIR (57% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/PORTDIR/it "PORTDIR (14% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/PORTDIR/hu "PORTDIR (100% translated)")
-   [polski](https://wiki.gentoo.org/wiki/PORTDIR/pl "PORTDIR (14% translated)")
-   [русский](https://wiki.gentoo.org/wiki/PORTDIR/ru "PORTDIR (100% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/PORTDIR/zh-cn "PORTDIR (14% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/PORTDIR/ja "PORTDIR (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/PORTDIR/ko "PORTDIR (14% translated)")

The `PORTDIR` variable was^[\[1\]](#cite_note-1)^ used to point to the main package repository hosted on the system. It has since been [[[deprecated]](https://bugs.gentoo.org/show_bug.cgi?id=546210)[]] in favor of the `location` attribute (whose default value is [[/var/db/repos/gentoo](https://wiki.gentoo.org/wiki//var/db/repos/gentoo "/var/db/repos/gentoo")]) of the Gentoo repository configuration inside [[/etc/portage/repos.conf](https://wiki.gentoo.org/wiki//etc/portage/repos.conf "/etc/portage/repos.conf")].

The current value of the `location` attribute can be obtained by using [portageq](https://wiki.gentoo.org/wiki/Portageq "Portageq"):

`user `[`$`]`portageq get_repo_path / gentoo`

    /var/db/repos/gentoo

## [External resources]

-   [[[bug #378603]](https://bugs.gentoo.org/show_bug.cgi?id=378603)[]]

## [References]

1.  [[[↑](#cite_ref-1)] [[https://gitweb.gentoo.org/proj/pms.git/commit/?id=3abcd75afc8a8ed4400ecd66cc4f129a4bf46330](https://gitweb.gentoo.org/proj/pms.git/commit/?id=3abcd75afc8a8ed4400ecd66cc4f129a4bf46330)]]