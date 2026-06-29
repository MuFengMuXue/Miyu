[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=HexChat&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://hexchat.github.io/)

[[]][Package information](https://packages.gentoo.org/packages/net-irc/hexchat)

[[]][GitHub](https://github.com/hexchat)

**HexChat** is a graphical IRC client based on XChat. It is written using the GTK+ windowing framework.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [SSL]](#SSL)
    -   [[2.3] [Auto-reconnect]](#Auto-reconnect)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [net-irc/hexchat](https://packages.gentoo.org/packages/net-irc/hexchat) [[]] [Graphical IRC client based on XChat]

  --------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+gtk`](https://packages.gentoo.org/useflags/+gtk)                         Add support for x11-libs/gtk+ (The GIMP Toolkit)
  [`dbus`](https://packages.gentoo.org/useflags/dbus)                         Enable dbus support for anything that needs it (gpsd, gnomemeeting, etc)
  [`debug`](https://packages.gentoo.org/useflags/debug)                       Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`libcanberra`](https://packages.gentoo.org/useflags/libcanberra)           Enable sound event support using media-libs/libcanberra
  [`lua`](https://packages.gentoo.org/useflags/lua)                           Enable Lua scripting support
  [`perl`](https://packages.gentoo.org/useflags/perl)                         Add optional support/bindings for the Perl language
  [`plugin-checksum`](https://packages.gentoo.org/useflags/plugin-checksum)   Build Checksum plugin (needs plugins)
  [`plugin-fishlim`](https://packages.gentoo.org/useflags/plugin-fishlim)     Build FiSHLiM plugin (needs plugins )
  [`plugin-sysinfo`](https://packages.gentoo.org/useflags/plugin-sysinfo)     Build SysInfo plugin (needs plugins)
  [`python`](https://packages.gentoo.org/useflags/python)                     Add optional support/bindings for the Python language
  [`ssl`](https://packages.gentoo.org/useflags/ssl)                           Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  [`theme-manager`](https://packages.gentoo.org/useflags/theme-manager)       Build the theme manager (mono)
  --------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-21 05:26] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Emerge hexchat:

`root `[`#`]`emerge --ask net-irc/hexchat`

## [Configuration]

### [Files]

HexChat stores user specific configuration files in the [\~/.config/hexchat/] directory.

Settings can be modified graphically via the [Settings] tab or using the [/set] command from the command-line interface.

### [SSL]

In HexChat, enable SSL connections in [Network List] ([Ctrl]+[s])[\> Libera.Chat \> Edit].

### [Auto-reconnect]

In order to automatically reconnect after sleep/hibernate mode, enter the [/set net_ping_timeout 31] command.

## [See also]

-   [IRC](https://wiki.gentoo.org/wiki/IRC "IRC") --- a stable, mature, text-based chat (instant messaging) system. IRC is one of the primary avenues of communication for those involved at all levels in the [Gentoo project](https://wiki.gentoo.org/wiki/Project:Gentoo "Project:Gentoo").

## [External resources]

-   [HexChat User Documentation](https://hexchat.readthedocs.org/en/latest/)