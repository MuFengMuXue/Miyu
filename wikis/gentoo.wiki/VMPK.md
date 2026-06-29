[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=VMPK&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://sourceforge.net/projects/vmpk/)

[[]][Package information](https://packages.gentoo.org/packages/media-sound/vmpk)

**VMPK**, **V**irtual **M**IDI **P**iano **K**eyboard, is a virtual [MIDI](https://wiki.gentoo.org/wiki/MIDI "MIDI") controller for Linux, Windows and OSX.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)

## [Installation]

### [USE flags]

### [USE flags for] [media-sound/vmpk](https://packages.gentoo.org/packages/media-sound/vmpk) [[]] [Virtual MIDI Piano Keyboard]

  ----------------------------------------------------- --------------------------------------------------------------------------
  [`dbus`](https://packages.gentoo.org/useflags/dbus)   Enable dbus support for anything that needs it (gpsd, gnomemeeting, etc)
  ----------------------------------------------------- --------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-01-29 15:59] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask media-sound/vmpk`

## [Usage]

Launch the virtual keyboard by running [vmpk]:

`user `[`$`]`vmpk`

By default, mouse input is disabled; it can be enabled via Edit -\> Preferences -\> Input.

Once VMPK is running, connect its output to a MIDI input on an [ALSA](https://wiki.gentoo.org/wiki/ALSA "ALSA") client, using e.g. [[[aconnect(1)]](https://man.archlinux.org/man/aconnect.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] (provided by [[[media-sound/alsa-utils]](https://packages.gentoo.org/packages/media-sound/alsa-utils)[]]) or a GUI tool, such as [[[media-sound/helvum]](https://packages.gentoo.org/packages/media-sound/helvum)[]] or [[[media-sound/qjackctl]](https://packages.gentoo.org/packages/media-sound/qjackctl)[]]. For example, to use [aconnect] to connect VMPK to a running instance of [amsynth](https://wiki.gentoo.org/wiki/Amsynth "Amsynth"), first run `aconnect -l` to find the MIDI output port of VMPK and the MIDI input port of amsynth:

`user `[`$`]`aconnect -l`

    client 0: 'System' [type=kernel]
        0 'Timer           '
        Connecting To: 142:0
        1 'Announce        '
        Connecting To: 142:0
    client 128: 'amsynth' [type=user,pid=16405]
        0 'MIDI IN         '
        1 'MIDI OUT        '
    client 129: 'VMPK Input' [type=user,pid=16752]
        0 'in              '
    client 130: 'VMPK Output' [type=user,pid=16752]
        0 'out             '
    client 142: 'PipeWire-System' [type=user,pid=3553]
        0 'input           '
        Connected From: 0:1, 0:0
    client 143: 'PipeWire-RT-Event' [type=user,pid=3553]
        0 'input           '

Then, to connect VMPK out (130:0) to amsynth MIDI in (128:0):

`user `[`$`]`aconnect 130:0 128:0`

Use of the VMPK keyboard should now result in audio output from amsynth.