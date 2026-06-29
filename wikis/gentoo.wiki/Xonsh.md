[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Xonsh&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://xon.sh)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Xonsh "wikipedia:Xonsh")

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/xonsh)

[[]][GitHub](https://github.com/xonsh/xonsh)

**Xonsh** combines a traditional [shell](https://wiki.gentoo.org/wiki/Shell "Shell") with the full power of Python, allowing POSIX shell style constructs used along with standard Python code.

Xonsh is multi platform, and is designed for interactive use, but can also be useful for scripting. Xonsh is very customizable, and there is a plugin system called xontribs.

## Contents

-   [[1] [Installation]](#Installation)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
-   [[3] [See also]](#See_also)

## [Installation]

Xonsh is not currently present in the [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository"), though it may be installed by following instructions from the project\'s website. Care must however be taken to keep Xonsh up to date, independently of [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") software.

## [Configuration]

To set Xonsh as the default shell with [chsh], it will have to be added to [/etc/shells]. See [https://xon.sh/customization.html#set-xonsh-as-my-default-shell](https://xon.sh/customization.html#set-xonsh-as-my-default-shell) for how to do this.

### [Files]

The main Xonsh user configuration file is either [\~/.xonshrc] or, [\~/.config/xonsh/rc.xsh] - choose one upon first use. There can also be a system-wide config file at [/etc/xonshrc].

If a there is a [\~/.config/xonsh/rc.d] directory, any *\*.xsh* files in it will get \"sourced\" on startup.

## [See also]

-   [Shell](https://wiki.gentoo.org/wiki/Shell "Shell") --- command-line interpreter that provides a text-based interface to users