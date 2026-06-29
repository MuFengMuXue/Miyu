[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Input_methods&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

An **input method** is a way to use any data as input, for example to use a standard Latin keyboard for writing Chinese characters. Gentoo has several input method frameworks available:

-   [fcitx](https://wiki.gentoo.org/wiki/Fcitx "Fcitx") --- supporting multiple languages and IMEs, mostly for Simplified Chinese, but also other scripts
-   [IBus](https://wiki.gentoo.org/wiki/IBus "IBus") --- supporting multiple languages and IMEs
-   [SCIM](https://wiki.gentoo.org/wiki/SCIM "SCIM") --- supporting multiple languages and IMEs
-   [uim](https://wiki.gentoo.org/wiki/Uim "Uim") --- supporting multiple languages and IMEs

The [gentoo-zh](https://github.com/microcai/gentoo-zh) overlay includes some more packages (and not just for Chinese).

On [GTK](https://wiki.gentoo.org/wiki/GTK "GTK") based applications, the key sequence for hexadecimal Unicode input is [Ctrl]+[Shift]+[u]+`<hex digit>`. As an example, the unicode character ✔ which has unicode number [U+2714](http://unicode-table.com/en/2714/) can be written as [Ctrl]+[Shift]+[u]+`2714`+`ENTER`, being rendered as `✔`. [IBus](https://wiki.gentoo.org/wiki/IBus "IBus") is needed for support in other applications.