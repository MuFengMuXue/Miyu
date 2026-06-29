[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=MIDI&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/MIDI "wikipedia:MIDI")

**MIDI** (Musical Instrument Digital Interface) is a set of technical specifications that enable devices to interoperate in order to work with a digital representation of music.

MIDI controllers (often in the form of a MIDI keyboard) are used to create music in the form a MIDI signal that can be sent to a number of other MIDI-compatible devices, such as a MIDI instrument to convert the MIDI signal to sound (\"play\" it), a MIDI sequencer to record the MIDI data, or to a computer.

Computers allow great flexibility in the processing of MIDI data, such as playing the MIDI signal on virtual MIDI instruments, recording the MIDI information to file, editing the MIDI data, representing the MIDI signal as musical notes in notation software, etc.

** Tip**\
The terms MIDI controller and MIDI instrument can be a little confusing: a MIDI controller produces MIDI information and is often the physical device that a user \"plays\". A MIDI instrument interprets this MIDI information to produce an actual audio signal. To add to the confusion, digital musical instruments often integrate both a MIDI controller and a MIDI instrument. An example would be an analogue synthesizer with both MIDI output and input: such instruments can produce a MIDI signal to be sent to other devices, and in that case act as a MIDI controller, but such a device can also receive a MIDI signal to command the analogue synthesizer to \"play\" it\'s notes, acting as a MIDI instrument.

** See also**\
See the [MIDI controller guide](https://wiki.gentoo.org/wiki/MIDI_controller_guide "MIDI controller guide") for how to set up MIDI controllers on Gentoo.

## Contents

-   [[1] [Available software]](#Available_software)
    -   [[1.1] [Packages with MIDI support]](#Packages_with_MIDI_support)
-   [[2] [See also]](#See_also)
-   [[3] [External resources]](#External_resources)

## [Available software]

These packages can interpret MIDI information to produce audio output:

  ------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------
  Name                                                                     Package                                                                                                                                                                                                                                                                                                                                                                                    Description
  [FluidSynth](https://wiki.gentoo.org/wiki/FluidSynth "FluidSynth")       [[[media-sound/fluidsynth]](https://packages.gentoo.org/packages/media-sound/fluidsynth)[]]   Software real-time synthesizer based on the Soundfont 2 specifications
  [Rosegarden](https://wiki.gentoo.org/wiki/Rosegarden "Rosegarden")       [[[media-sound/rosegarden]](https://packages.gentoo.org/packages/media-sound/rosegarden)[]]   A music composition and editing environment based around a MIDI sequencer
  [TiMidity++](https://wiki.gentoo.org/wiki/TiMidity%2B%2B "TiMidity++")   [[[media-sound/timidity++]](https://packages.gentoo.org/packages/media-sound/timidity++)[]]   Handy MIDI to WAV converter with OSS and ALSA output support
  ------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------

### [Packages with MIDI support]

Several packages use the [[[midi]](https://packages.gentoo.org/useflags/midi)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag"). These packages may be of interest to anyone looking to use MIDI on Gentoo.

To see a list of some of the packages that provide USE flags containing the keyword `midi`, [quse](https://wiki.gentoo.org/wiki/Q_applets "Q applets") can help:

`user `[`$`]`quse -ve midi`

## [See also]

-   [MIDI controller guide](https://wiki.gentoo.org/wiki/MIDI_controller_guide "MIDI controller guide") --- musical equipment including keyboards, pads, pot/fader controls and much more
-   [Music production](https://wiki.gentoo.org/wiki/Music_production "Music production") --- Gentoo can be a good platform for **music production**.
-   [Project:Sound/How to Enable Realtime for Multimedia Applications](https://wiki.gentoo.org/wiki/Project:Sound/How_to_Enable_Realtime_for_Multimedia_Applications "Project:Sound/How to Enable Realtime for Multimedia Applications")

## [External resources]

-   [Ted\'s Linux MIDI Guide](http://www.tedfelix.com/linux/linux-midi.html)