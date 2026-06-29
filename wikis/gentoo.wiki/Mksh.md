**Resources**

[[]][Home](http://www.mirbsd.org/mksh.htm)

[[]][Package information](https://packages.gentoo.org/packages/app-shells/mksh)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Korn_shell "wikipedia:Korn shell")

[[]][[#!/bin/mksh](irc://irc.oftc.net/#!/bin/mksh) (on [irc://irc.oftc.net](irc://irc.oftc.net)])

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/mksh)

[mksh] is the MirBSD Korn Shell, an actively developed free implementation of the Korn Shell programming language and a successor to the Public Domain Korn Shell ([pdksh]). It is developed as part of [the MirOS Project](https://www.mirbsd.org/main.htm) as native Bourne/POSIX/Korn shell for MirOS BSD, but also to be readily available under other UNIX-like operating systems. It targets users who desire a compact, fast, reliable, secure shell not cut off modern extensions, with unicode support.

Because of its speed, POSIX compliance, and advanced features, it is ideally suited for scripting. But it can serve very well as a login shell too. It is used as default shell on [Android](https://wiki.gentoo.org/wiki/Android "Android").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Set default login shell]](#Set_default_login_shell)
    -   [[2.2] [Files]](#Files)
        -   [[2.2.1] [Local]](#Local)
-   [[3] [Removal]](#Removal)
    -   [[3.1] [Unmerge]](#Unmerge)
-   [[4] [See also]](#See_also)

## [Installation]

### [Emerge]

Install [mksh]:

`root `[`#`]`emerge --ask app-shells/mksh`

Installed size is about 280K on an amd64 system (vs. 721K for bash-4).

## [Configuration]

### [Set default login shell]

To make [mksh] the default login shell, run:

`user `[`$`]`chsh -s /bin/mksh`

### [Files]

#### [Local]

The local configuration file used is [\~/.mkshrc] --- see [/usr/share/doc/mksh-\*/dot.mkshrc\*] for an example that is shipped with the package.

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose app-shells/mksh`

## [See also]

-   [Shell](https://wiki.gentoo.org/wiki/Shell "Shell") --- command-line interpreter that provides a text-based interface to users