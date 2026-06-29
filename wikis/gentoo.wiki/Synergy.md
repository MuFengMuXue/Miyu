[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Synergy&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://symless.com/synergy/)

[[]][Package information](https://packages.gentoo.org/packages/x11-misc/synergy)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Synergy_(software) "wikipedia:Synergy (software)")

[[]][GitHub](https://github.com/symless/synergy-core)

Synergy is open source, cross platform software used to manage multiple displays (running on an Xorg display server) with a single keyboard and mouse. It can be thought of as a KVM - but only supporting keyboard and mouse. As of 2023-07-06, Synergy does not support compositors running on the Wayland protocol.^[\[1\]](#cite_note-1)^

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Service]](#Service)
    -   [[2.3] [Encryption]](#Encryption)
-   [[3] [Usage]](#Usage)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Wayland support]](#Wayland_support)
-   [[5] [Removal]](#Removal)
    -   [[5.1] [Unmerge]](#Unmerge)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

## [Installation]

### [USE flags]

Cannot load package information. Is the atom *x11-misc/synergy* correct?

### [Emerge]

`root `[`#`]`emerge --ask x11-misc/synergy`

## [Configuration]

### [Files]

-   [/etc/synergy.conf] - Global (system wide) configuration file.
-   [\~/.synergy] - Local (per user) configuration directory.

### [Service]

See [man 1 synergys] for Synergy service options.

Gentoo does not presently include OpenRC or systemd service scripts for Synergy.

### [Encryption]

The Synergy wiki upstream provides details for enabling encryption between the client/server connection(s).

In short, copy the bundled encryption plugin to the Synergy user\'s home directory:

`user `[`$`]`mkdir -p ~/.synergy/plugins `

`user `[`$`]`cp /usr/lib64/synergy/plugins/libns.so ~/.synergy/plugins `

Next, generate the certificate:

## [Usage]

There are a few executable files that are merged after the compilation:

-   [/usr/bin/syntool]
-   [/usr/bin/synergyc] - Used to connect to a Synergy mouse/keyboard sharing server.
-   [/usr/bin/synergys] - Starts and controls the synergy mouse/keyboard sharing server. See [man 1 synergys] for options.
-   [/usr/bin/qsynergy] - Graphical user interface for Synergy. This can be disabled via the `gui` USE flag.

## [Troubleshooting]

### [Wayland support]

No, Synergy is not presently supported in environments running compositors using the Wayland protocol as a backend. Follow upstream\'s [GitHub issue #4090](https://github.com/symless/synergy-core/issues/4090) to stay in the loop.

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose x11-misc/synergy`

## [See also]

-   [TigerVNC](https://wiki.gentoo.org/wiki/TigerVNC "TigerVNC") --- a client/server software package allowing remote network access to graphical desktops.

## [External resources]

-   [https://github.com/symless/synergy-core/wiki](https://github.com/symless/synergy-core/wiki) - Upstream\'s project wiki.
-   [https://brahma-dev.github.io/synergy-stable-builds/](https://brahma-dev.github.io/synergy-stable-builds/) - A third party site that hosts compiled binaries for Windows and OSX.

1.  [[[↑](#cite_ref-1)] [[GitHub issue](https://github.com/symless/synergy-core/issues/4090)]]