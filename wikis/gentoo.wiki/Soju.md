[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Soju&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://soju.im/)

[[]][Official documentation](https://codeberg.org/emersion/soju/src/branch/master/doc/getting-started.md)

[![Codeberg Logo](/images/thumb/c/cc/Codeberg-logo.png/30px-Codeberg-logo.png)][Codeberg](https://codeberg.org/emersion/soju)

[[]][Bugs (upstream)](https://codeberg.org/emersion/soju/issues/)

[[]][[#soju](ircs://irc.libera.chat/#soju)] ([[webchat](https://web.libera.chat/#soju)])

[[]][Package information](https://packages.gentoo.org/packages/net-irc/soju)

[soju] is a user-friendly IRC bouncer:

> soju connects to upstream IRC servers on behalf of the user to provide extra functionality. soju supports many features such as multiple users, numerous IRCv3 extensions, chat history playback and detached channels.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Service]](#Service)
        -   [[2.1.1] [OpenRC]](#OpenRC)
        -   [[2.1.2] [systemd]](#systemd)
    -   [[2.2] [Adding networks]](#Adding_networks)
-   [[3] [External resources]](#External_resources)
-   [[4] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [net-irc/soju](https://packages.gentoo.org/packages/net-irc/soju) [[]] [soju is a user-friendly IRC bouncer]

  ----------------------------------------------------------------------- ----------------------------------------------------------------------------------------
  [`+sqlite`](https://packages.gentoo.org/useflags/+sqlite)               Add support for sqlite - embedded sql database
  [`moderncsqlite`](https://packages.gentoo.org/useflags/moderncsqlite)   Use moderncsqlite, a cgo-free port of SQLite
  [`pam`](https://packages.gentoo.org/useflags/pam)                       Add support for PAM (Pluggable Authentication Modules) - DANGEROUS to arbitrarily flip
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)         Verify upstream signatures on distfiles
  ----------------------------------------------------------------------- ----------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-15 11:04] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask net-irc/soju`

## [Configuration]

An example configuration file is provided below; refer to the [[[soju(1)]](https://man.archlinux.org/man/soju.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page for a detailed list of configuration options.

[FILE] **`/etc/soju/config`Example configuration**

    db sqlite3 /var/lib/soju/main.db
    listen irc+insecure://192.168.0.1:6667

### [Service]

#### [OpenRC]

To start the [soju] OpenRC service:

`root `[`#`]`rc-service soju start`

To start the [soju] service on system boot, add it to the default runlevel:

`root `[`#`]`rc-update add soju default`

#### [systemd]

To start the [soju] systemd service:

`root `[`#`]`systemctl start soju.service`

To start the [soju] systemd service at boot, enable it:

`root `[`#`]`systemctl enable soju.service`

### [Adding networks]

Once the [soju] service is running, connect to it via an [IRC client](https://wiki.gentoo.org/wiki/IRC#Available_software "IRC"), and send a \"help\" message to the BouncerServ service to get a list of available commands:

    /msg BouncerServ help

The BouncerServ channel can be used to ask for help on specific commands:

    <user> help network create
    <BouncerServ> network create -addr <addr> [-name name] [-username username]
                  [-pass pass] [-realname realname] [-certfp fingerprint] [-nick
                  nick] [-auto-away auto-away] [-enabled enabled]
                  [-connect-command command]...: add a new network

and to run those commands.

For example, to add the Libera.chat network:

    <user> network create -addr ircs://irc.libera.chat -name libera -nick <nick> -enabled true -connect-command "PRIVMSG NickServ :IDENTIFY <nick-password>" -connect-command "PRIVMSG NickServ :RELEASE <nick>" -connect-command "PRIVMSG NickServ :REGAIN <nick>"

Note that the `-name` and `-username` options are for server access, not nick management; however, the default value for `-nick` is the value of `-username`.

## [External resources]

-   [[[soju(1)]](https://man.archlinux.org/man/soju.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page
-   [soju client list](https://codeberg.org/emersion/soju/src/branch/master/contrib/clients.md) -- Instructions for setting up various IRC clients to connect to soju

## [References]