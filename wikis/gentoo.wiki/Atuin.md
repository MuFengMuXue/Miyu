[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Atuin&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://atuin.sh/#cli-section)

[[]][Official documentation](https://docs.atuin.sh/)

[[]][Package information](https://packages.gentoo.org/packages/app-shells/atuin)

[[]][GitHub](https://github.com/atuinsh/atuin)

**Atuin** is a [shell](https://wiki.gentoo.org/wiki/Shell "Shell") history manager supporting encrypted synchronization. It replaces shell command history records with a SQLite database providing greater flexibility for searching and synchronization. The standard [Ctrl][r]-bound history overview gets superseded by an advanced TUI.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Service]](#Service)
        -   [[2.2.1] [config]](#config)
        -   [[2.2.2] [systemd]](#systemd)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [Troubleshooting]](#Troubleshooting)

## [Installation]

### [USE flags]

### [USE flags for] [app-shells/atuin](https://packages.gentoo.org/packages/app-shells/atuin) [[]] [Shell history manager supporting encrypted synchronisation]

  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+client`](https://packages.gentoo.org/useflags/+client)               Enable the autin client
  [`+daemon`](https://packages.gentoo.org/useflags/+daemon)               Enable the autin background daemon on the client
  [`+sync`](https://packages.gentoo.org/useflags/+sync)                   Enable the server-sync feature in the autin client
  [`debug`](https://packages.gentoo.org/useflags/debug)                   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`server`](https://packages.gentoo.org/useflags/server)                 Enable the autin server
  [`system-sqlite`](https://packages.gentoo.org/useflags/system-sqlite)   Use the system SQLite instead of the bundled one. WARNING: enabling this has a negative performance impact (https://bugs.gentoo.org/959120)
  [`test`](https://packages.gentoo.org/useflags/test)                     Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-08 19:26] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-shells/atuin`

If using Bash, note that either [ble.sh](https://github.com/akinomyoga/ble.sh) or [bash-preexec](https://github.com/rcaloras/bash-preexec) is required for capturing commands. See the [Atuin docs](https://docs.atuin.sh/cli/guide/installation/#installing-the-shell-plugin) for details.

## [Configuration]

It is possible to customize Atuin behavior, such as configuring filtering or search modes.

### [Files]

-   [\~/.config/atuin/config.toml] - Local (per user) configuration file.

### [Service]

Atuin package comes with the background daemon functionality, which helps with lowering latency of database writes, supported by default. The daemon can be started manually via [atuin daemon].

#### [config]

To make atuin aware of the daemon, add following lines to the config file:

[FILE] **`~/.config/atuin/config.toml`**

    [daemon]
    enabled = true
    systemd_socket = true

#### [systemd]

To enable the daemon functionality run:

`user `[`$`]`systemctl enable --now --user atuin-daemon.socket`

## [Usage]

### [Invocation]

Simply hit [Ctrl][r] to start browsing shell history.

## [Troubleshooting]

There is the [atuin doctor] utility dedicated to perform self-diagnosis of Atuin and its environment.