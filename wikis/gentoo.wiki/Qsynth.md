[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Qsynth&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://qsynth.sourceforge.io/)

[[]][Package information](https://packages.gentoo.org/packages/media-sound/qsynth)

**Qsynth** is a GUI frontend to [FluidSynth](https://wiki.gentoo.org/wiki/FluidSynth "FluidSynth").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
    -   [[1.2] [Usage]](#Usage)
-   [[2] [See also]](#See_also)

## [Installation]

### [Emerge]

`root `[`#`]`emerge --ask media-sound/qsynth`

### [Usage]

To start Qsynth from the command line:

`user `[`$`]`qsynth`

A soundfont will need to be specified for [FluidSynth](https://wiki.gentoo.org/wiki/FluidSynth "FluidSynth") to use. Two soundfonts are provided by the [[[media-sound/fluid-soundfont]](https://packages.gentoo.org/packages/media-sound/fluid-soundfont)[]] package, [FluidR3_GM.sf2] and [FluidR3_SM.sf2].

In Qsynth, the soundfont can be specified via Settings -\> Soundfonts; once the [[[media-sound/fluid-soundfont]](https://packages.gentoo.org/packages/media-sound/fluid-soundfont)[]] package is installed, [FluidR3_GM.sf2] can be be found in [/usr/share/sounds/sf2/].

To use Qsynth with PipeWire, specify PipeWire as the audio driver via Settings -\> Audio.

## [See also]

-   [FluidSynth](https://wiki.gentoo.org/wiki/FluidSynth "FluidSynth") --- a real-time software synthesizer based on the SoundFont 2 specifications
-   [MIDI controller guide](https://wiki.gentoo.org/wiki/MIDI_controller_guide "MIDI controller guide") --- musical equipment including keyboards, pads, pot/fader controls and much more
-   [TiMidity++](https://wiki.gentoo.org/wiki/TiMidity%2B%2B "TiMidity++") --- software synthesizer that can interpret MIDI information