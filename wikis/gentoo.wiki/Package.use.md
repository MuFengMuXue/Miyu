Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki//etc/portage/package.use/de "/etc/portage/package.use/de (57% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki//etc/portage/package.use/es "/etc/portage/package.use (65% translated)")
-   [français](https://wiki.gentoo.org/wiki//etc/portage/package.use/fr "/etc/portage/package.use/fr (57% translated)")
-   [italiano](https://wiki.gentoo.org/wiki//etc/portage/package.use/it "/etc/portage/package.use/it (22% translated)")
-   [magyar](https://wiki.gentoo.org/wiki//etc/portage/package.use/hu "/etc/portage/package.use (65% translated)")
-   [русский](https://wiki.gentoo.org/wiki//etc/portage/package.use/ru "/etc/portage/package.use (39% translated)")
-   [українська](https://wiki.gentoo.org/wiki//etc/portage/package.use/uk "/etc/portage/package.use/uk (57% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki//etc/portage/package.use/zh-cn "/etc/portage/package.use/zh-cn (22% translated)")
-   [日本語](https://wiki.gentoo.org/wiki//etc/portage/package.use/ja "/etc/portage/package.use (100% translated)")

**[/etc/portage/package.use]** provides a more fine grained **[per-package control](https://wiki.gentoo.org/wiki/Handbook:Parts/Working/USE#Declaring_USE_flags_for_individual_packages "Handbook:Parts/Working/USE") of [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag")** than the `USE` variable in [[/etc/portage/make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf#USE "/etc/portage/make.conf")].

** Note**\
[/etc/portage/package.use] can either be a single file or a directory containing per-package [files](https://wiki.gentoo.org/wiki/Handbook:Parts/Working/USE#Declaring_USE_flags_for_individual_packages "Handbook:Parts/Working/USE").

With the default [`USE_ORDER`](https://wiki.gentoo.org/wiki/USE_ORDER "USE ORDER") setting, the [/etc/portage/package.use] file or directory will override individual package settings coming from all locations except for the `USE` environment variable.

## Contents

-   [[1] [Example]](#Example)
-   [[2] [Format]](#Format)
-   [[3] [Automatically generated content]](#Automatically_generated_content)
-   [[4] [Finding USE flags set]](#Finding_USE_flags_set)
-   [[5] [External resources]](#External_resources)

## [Example]

[FILE] **`/etc/portage/package.use`Example with this location as a single file**

    # Globally disable the unwanted USE flags which were enabled by the profile
    */* -bluetooth -dbus -ldap -libnotify -nls -udisks

    # enable the offensive USE flag for app-admin/sudo
    app-admin/sudo offensive

    # disable mysql support for dev-lang/php
    dev-lang/php -mysql

    # enable java and set the python interpreter version for libreoffice
    app-office/libreoffice java PYTHON_SINGLE_TARGET: python3_11

[FILE] **`/etc/portage/package.use/openrct`Example with this location as a directory**

    # Disable Vorbis support in OpenRCT2
    games-simulation/openrct2 -vorbis

For more details see [the Handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/USE#Declaring_USE_flags_for_individual_packages "Handbook:AMD64/Working/USE").

## [Format]

-   One `DEPEND` atom per line with space-delimited [USE flags](https://wiki.gentoo.org/wiki/Handbook:Parts/Working/USE "Handbook:Parts/Working/USE").
-   Comment lines begin with `#` (hash).

** Note**\
See [version specifier](https://wiki.gentoo.org/wiki/Version_specifier "Version specifier") for information on how to format the package atoms.

** Tip**\
If a package atom specifies a version, a comparison operator must be used.

## [Automatically generated content]

[emerge] has the `--autounmask` option enabled by default (see [man 1 emerge]), so it can generate [package.use] settings as necessary to satisfy dependencies.

** Tip**\
When [/usr/portage/package.use] is a directory, `--autounmask` will write its changes to the *lexicographically last* file in that directory. Users might find it useful to [create such a file](https://wiki.gentoo.org/wiki/Knowledge_Base:Autounmask-write "Knowledge Base:Autounmask-write") ahead of time. Otherwise, a confusing (but otherwise harmless) situation can result where changes for one package are appended to a file pertaining to a different package.

## [Finding USE flags set]

With all the will in the world, mistakes will happen so below are some tips to help find a USE flag that was set and can no longer be found.

In this example, the [[[lua]](https://packages.gentoo.org/useflags/lua)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag was set for [[[media-video/obs-studio]](https://packages.gentoo.org/packages/media-video/obs-studio)[]], but is no longer required.

`user `[`$`]`grep --recursive "lua" /etc/portage/ `

/etc/portage/package.use/obs:media-video/obs-studio nvenc browser speex fdk lua python qsv v4l vlc

/etc/portage/package.use/scummvm:games-engines/scummvm fluidsynth -fribidi lua mpeg2 sndio speech theora unsupported

/etc/portage/package.use/zz-automask:\>=dev-lua/lgi-0.9.2-r100 lua_targets_luajit

It can be seen that the USE flag is in [/etc/portage/package.use/obs] and can be quickly added and removed.

## [External resources]

-   [https://packages.gentoo.org/useflags](https://packages.gentoo.org/useflags) - USE flags on Gentoo Packages Database
-   [Portage man page](https://dev.gentoo.org/~zmedico/portage/doc/man/portage.5.html)
-   [Setting USE_EXPAND flags in package.use](https://blog.cafarelli.fr/2016/02/setting-use_expand-flags-in-package-use/) - blog post by Bernard Cafarelli
-   [Cleaning /etc/portage/package.\* from unused entries](https://wiki.gentoo.org/wiki/User:Tillschaefer/cleanup_package "User:Tillschaefer/cleanup package")
-   [Find obsolete USE flags in /etc/portage/package.use](https://forums.gentoo.org/viewtopic-t-897206-start-11.html) - Gentoo forums thread