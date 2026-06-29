[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Wiremix&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[[]][Package information](https://packages.gentoo.org/packages/media-sound/wiremix)

[[]][GitHub](https://github.com/tsowell/wiremix)

**wiremix** is a simple TUI audio mixer for [PipeWire](https://wiki.gentoo.org/wiki/PipeWire "PipeWire") / [WirePlumber](https://wiki.gentoo.org/wiki/WirePlumber "WirePlumber"):

> \[U\]se it to adjust volumes, route audio between devices and applications, and configure audio device settings like input/output ports and profiles. wiremix\'s interface is more or less a clone of the wonderful ncpamixer which was itself inspired by [[[pavucontrol(1)]](https://man.archlinux.org/man/pavucontrol.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")], so users of either should find it familiar.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Usage]](#Usage)

## [Installation]

### [USE flags]

### [USE flags for] [media-sound/wiremix](https://packages.gentoo.org/packages/media-sound/wiremix) [[]] [A TUI mixer for PipeWire]

  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`debug`](https://packages.gentoo.org/useflags/debug)   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-06 23:59] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Emerge wiremix:

`root `[`#`]`emerge --ask media-sound/wiremix`

## [Configuration]

Refer to the project\'s [annotated [wiremix.toml] file](https://github.com/tsowell/wiremix/blob/main/wiremix.toml):

> It is recommended to start with an empty configuration file and to use this file only as a reference. Anything specified in the configuration file will be merged with wiremix\'s defaults.

## [Usage]

To start [wiremix] from the command line:

`user `[`$`]`wiremix`

Refer to the output of [wiremix \--help] for command-line options, such as `-t` / `--theme` and `-v` / `--tab`.

Once wiremix has started, press [?] for help.