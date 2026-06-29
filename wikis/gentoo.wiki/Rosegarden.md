[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Rosegarden&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://rosegardenmusic.com)

[[]][Package information](https://packages.gentoo.org/packages/media-sound/rosegarden)

[[]][Official documentation](https://rosegardenmusic.com/wiki/doc:manual-en)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Rosegarden "wikipedia:Rosegarden")

**Rosegarden** is a music composition and editing environment based around a MIDI sequencer that features a rich understanding of music notation and includes basic support for digital audio.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Kernel]](#Kernel)
    -   [[2.2] [Software synth]](#Software_synth)
    -   [[2.3] [Usage]](#Usage)
        -   [[2.3.1] [Exporting to MP3]](#Exporting_to_MP3)
-   [[3] [See also]](#See_also)

## [Installation]

### [Emerge]

`root `[`#`]`emerge --ask media-sound/rosegarden`

## [Configuration]

### [Kernel]

[KERNEL] **Enable sequencer support**

    Device Drivers --->
      <*> Sound card support Search for <code>CONFIG_SOUND</code> to find this item. --->
        <*> Advanced Linux Sound Architecture Search for <code>CONFIG_SND</code> to find this item. --->
          <*> Sequencer support Search for <code>CONFIG_SND_SEQUENCER</code> to find this item.

Each of the above kernel configuration options can instead be built as a module (`<M>`), but in that case the system must be configured to load the `snd-seq-midi` module and its dependencies at boot. To do so, add a file in the [/etc/modules-load.d/] directory, creating the directory if necessary:

[FILE] **`sequencer.conf`**

    snd-seq-midi

### [Software synth]

Install a software synth that can be used by Rosegarden. [Qsynth](https://wiki.gentoo.org/wiki/Qsynth "Qsynth") ([[[media-sound/qsynth]](https://packages.gentoo.org/packages/media-sound/qsynth)[]]) is a [Qt](https://wiki.gentoo.org/wiki/Qt "Qt") GUI frontend to [FluidSynth](https://wiki.gentoo.org/wiki/FluidSynth "FluidSynth") ([[[media-sound/fluidsynth]](https://packages.gentoo.org/packages/media-sound/fluidsynth)[]]).

### [Usage]

Before starting Rosegarden, ensure the software synth (e.g. Qsynth) is running:

`user `[`$`]`qsynth`

Start Rosegarden:

`user `[`$`]`rosegarden`

If not using [JACK](https://wiki.gentoo.org/wiki/JACK "JACK"), but instead using e.g. PipeWire, ensure that the following Rosegarden settings, available via Edit -\> Audio, are **disabled**:

-   Make default JACK connections for audio outputs
-   Make default JACK connections for audio inputs
-   Start JACK automatically

#### [Exporting to MP3]

Rosegarden can export a composition to a MIDI file, which can then be converted to an MP3 via the use of [TiMidity++](https://wiki.gentoo.org/wiki/TiMidity%2B%2B "TiMidity++") and [ffmpeg](https://wiki.gentoo.org/wiki/Ffmpeg "Ffmpeg") (see those respective articles for installation instructions).

In Rosegarden\'s main window, select File -\> Export -\> Export MIDI file, and specify an appropriate filename, e.g. [composition.mid].

See the [TiMidity++ article section on converting MIDI to mp3](https://wiki.gentoo.org/wiki/TiMidity%2B%2B#Convert_a_MIDI_file_to_mp3 "TiMidity++") for instructions on how to convert this exported MIDI file to mp3.

## [See also]

-   [JACK](https://wiki.gentoo.org/wiki/JACK "JACK") --- describes the setup of a playing sound with **JACK** (**J**ACK **A**udio **C**onnection **K**it).
-   [MIDI](https://wiki.gentoo.org/wiki/MIDI "MIDI") --- a set of technical specifications that enable devices to interoperate in order to work with a digital representation of music
-   [PipeWire](https://wiki.gentoo.org/wiki/PipeWire "PipeWire") --- low-latency, graph-based, processing engine and server, for interfacing with audio and video devices.