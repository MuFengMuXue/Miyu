[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Amsynth&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://amsynth.github.io/)

[[]][Package information](https://packages.gentoo.org/packages/media-sound/amsynth)

[[]][GitHub](https://github.com/amsynth/amsynth)

**amsynth** is an easy-to-use software synth with a classic subtractive synthesizer topology.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)

## [Installation]

### [USE flags]

### [USE flags for] [media-sound/amsynth](https://packages.gentoo.org/packages/media-sound/amsynth) [[]] [Virtual analogue synthesizer]

  ----------------------------------------------------- -------------------------------------------------------------------------
  [`alsa`](https://packages.gentoo.org/useflags/alsa)   Add support for media-libs/alsa-lib (Advanced Linux Sound Architecture)
  [`dssi`](https://packages.gentoo.org/useflags/dssi)   Enable support for DSSI Soft Synth Interface
  [`gtk`](https://packages.gentoo.org/useflags/gtk)     Add support for x11-libs/gtk+ (The GIMP Toolkit)
  [`jack`](https://packages.gentoo.org/useflags/jack)   Add support for the JACK Audio Connection Kit
  [`lash`](https://packages.gentoo.org/useflags/lash)   Add LASH Audio Session Handler support
  [`lv2`](https://packages.gentoo.org/useflags/lv2)     Add support for Ladspa V2
  [`nsm`](https://packages.gentoo.org/useflags/nsm)     Build support for Non Session Manager
  [`oss`](https://packages.gentoo.org/useflags/oss)     Add support for OSS (Open Sound System)
  [`vst`](https://packages.gentoo.org/useflags/vst)     Build VST plug-in
  ----------------------------------------------------- -------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2024-06-11 09:18] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

By default, amsynth is installed with only the `alsa` USE flag enabled. As a result, running it will not display a UI. To enable the UI, enable the `gtk` USE flag.

### [Emerge]

`root `[`#`]`emerge --ask media-sound/amsynth`

## [Usage]

To start amsynth:

`user `[`$`]`amsynth`

Refer to the [[[amsynth(1)]](https://man.archlinux.org/man/amsynth.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page for available options.

amsynth can then produce output by being connected to a [MIDI controller](https://wiki.gentoo.org/wiki/MIDI_controller_guide "MIDI controller guide"), such as [VMPK](https://wiki.gentoo.org/wiki/VMPK "VMPK"), by connecting the output of the controller to the MIDI input of amsynth, e.g. via [[[aconnect(1)]](https://man.archlinux.org/man/aconnect.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] (provided by [[[media-sound/alsa-utils]](https://packages.gentoo.org/packages/media-sound/alsa-utils)[]]):

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

`user `[`$`]`aconnect 130:0 128:0`

Other tools available for connecting clients include [[[media-sound/helvum]](https://packages.gentoo.org/packages/media-sound/helvum)[]] and [[[media-sound/qjackctl]](https://packages.gentoo.org/packages/media-sound/qjackctl)[]], both of which provide a GUI.