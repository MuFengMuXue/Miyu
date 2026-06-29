[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Audacious&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://audacious-media-player.org/)

[[]][Package information](https://packages.gentoo.org/packages/media-sound/audacious)

[[]][Package information](https://packages.gentoo.org/packages/media-plugins/audacious-plugins)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Audacious_(software) "wikipedia:Audacious (software)")

**Audacious** is a media player and library manager, similar to XMMS, and Winamp.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
        -   [[1.1.1] [Audacious]](#Audacious)
        -   [[1.1.2] [Audacious plugins]](#Audacious_plugins)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [PipeWire]](#PipeWire)
    -   [[3.2] [Context Menu opens wrong application]](#Context_Menu_opens_wrong_application)
    -   [[3.3] [No option shown for CD playback]](#No_option_shown_for_CD_playback)

## [Installation]

### [USE flags]

#### [Audacious]

### [USE flags for] [media-sound/audacious](https://packages.gentoo.org/packages/media-sound/audacious) [[]] [Lightweight and versatile audio player]

  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`gtk`](https://packages.gentoo.org/useflags/gtk)     Add support for x11-libs/gtk+ (The GIMP Toolkit)
  [`qt6`](https://packages.gentoo.org/useflags/qt6)     Add support for the Qt 6 application and UI framework
  [`test`](https://packages.gentoo.org/useflags/test)   Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-10 07:03] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

#### [Audacious plugins]

### [USE flags for] [media-plugins/audacious-plugins](https://packages.gentoo.org/packages/media-plugins/audacious-plugins) [[]] [Lightweight and versatile audio player]

  ----------------------------------------------------------------------- ----------------------------------------------------------------------------------
  [`+alsa`](https://packages.gentoo.org/useflags/+alsa)                   Add support for media-libs/alsa-lib (Advanced Linux Sound Architecture)
  [`+mp3`](https://packages.gentoo.org/useflags/+mp3)                     Add support for reading mp3 files
  [`X`](https://packages.gentoo.org/useflags/X)                           Add support for X11
  [`aac`](https://packages.gentoo.org/useflags/aac)                       Enable support for MPEG-4 AAC Audio
  [`ampache`](https://packages.gentoo.org/useflags/ampache)               Support controlling audacious via ampache
  [`bs2b`](https://packages.gentoo.org/useflags/bs2b)                     Enable Bauer Bauer stereophonic-to-binaural headphone filter
  [`cdda`](https://packages.gentoo.org/useflags/cdda)                     Add Compact Disk Digital Audio (Standard Audio CD) support
  [`cue`](https://packages.gentoo.org/useflags/cue)                       Support CUE sheets using the libcue library
  [`ffmpeg`](https://packages.gentoo.org/useflags/ffmpeg)                 Enable ffmpeg/libav-based audio/video codec support
  [`flac`](https://packages.gentoo.org/useflags/flac)                     Add support for FLAC: Free Lossless Audio Codec
  [`fluidsynth`](https://packages.gentoo.org/useflags/fluidsynth)         Support FluidSynth as MIDI synth backend
  [`gme`](https://packages.gentoo.org/useflags/gme)                       Support various gaming console music formats
  [`gtk`](https://packages.gentoo.org/useflags/gtk)                       Add support for x11-libs/gtk+ (The GIMP Toolkit)
  [`http`](https://packages.gentoo.org/useflags/http)                     Support HTTP streams through neon
  [`jack`](https://packages.gentoo.org/useflags/jack)                     Add support for the JACK Audio Connection Kit
  [`lame`](https://packages.gentoo.org/useflags/lame)                     Add support for MP3 encoding using LAME
  [`libnotify`](https://packages.gentoo.org/useflags/libnotify)           Enable desktop notification support
  [`libsamplerate`](https://packages.gentoo.org/useflags/libsamplerate)   Build with support for converting sample rates using libsamplerate
  [`lirc`](https://packages.gentoo.org/useflags/lirc)                     Add support for lirc (Linux\'s Infra-Red Remote Control)
  [`mms`](https://packages.gentoo.org/useflags/mms)                       Support for Microsoft Media Server (MMS) streams
  [`modplug`](https://packages.gentoo.org/useflags/modplug)               Add libmodplug support for playing SoundTracker-style music files
  [`opengl`](https://packages.gentoo.org/useflags/opengl)                 Add support for OpenGL (3D graphics)
  [`openmpt`](https://packages.gentoo.org/useflags/openmpt)               Add support for OpenMPT
  [`opus`](https://packages.gentoo.org/useflags/opus)                     Enable Opus audio codec support
  [`pipewire`](https://packages.gentoo.org/useflags/pipewire)             Build the PipeWire output plugin
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)         Add sound server support via media-libs/libpulse (may be PulseAudio or PipeWire)
  [`qt6`](https://packages.gentoo.org/useflags/qt6)                       Add support for the Qt 6 application and UI framework
  [`qtmedia`](https://packages.gentoo.org/useflags/qtmedia)               Enable playback via dev-qt/qtmultimedia
  [`scrobbler`](https://packages.gentoo.org/useflags/scrobbler)           Build with scrobbler/LastFM submission support
  [`sdl`](https://packages.gentoo.org/useflags/sdl)                       Add support for Simple Direct Layer (media library)
  [`sid`](https://packages.gentoo.org/useflags/sid)                       Enable SID (Commodore 64 audio) file support
  [`sndfile`](https://packages.gentoo.org/useflags/sndfile)               Add support for libsndfile
  [`soxr`](https://packages.gentoo.org/useflags/soxr)                     Build with SoX Resampler support
  [`speedpitch`](https://packages.gentoo.org/useflags/speedpitch)         Enable speed/pitch effects
  [`streamtuner`](https://packages.gentoo.org/useflags/streamtuner)       Build the streamtuner plugin
  [`vorbis`](https://packages.gentoo.org/useflags/vorbis)                 Add support for the OggVorbis audio codec
  [`wavpack`](https://packages.gentoo.org/useflags/wavpack)               Add support for wavpack audio compression tools
  [`wayland`](https://packages.gentoo.org/useflags/wayland)               Enable dev-libs/wayland backend
  ----------------------------------------------------------------------- ----------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-10 07:03] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[media-sound/audacious]](https://packages.gentoo.org/packages/media-sound/audacious)[]] and [[[media-plugins/audacious-plugins]](https://packages.gentoo.org/packages/media-plugins/audacious-plugins)[]]:

`root `[`#`]`emerge --ask media-sound/audacious media-plugins/audacious-plugins`

## [Usage]

-   To put Audacious in classic Winamp mode, go to *View \> Interface \> Winamp Classic Interface*.
-   To insert classical Winamp EQ presets:

`user `[`$`]`wget -O $HOME/.config/audacious/eq.preset https://gist.github.com/666threesixes666/6017524/raw/6f92831829453dd659f063299ba1bdf775a893ac/wapresets`

## [Troubleshooting]

### [PipeWire]

When running Audacious with PipeWire, you may experience the following error:

`user `[`$`]`audacious`

    ERROR ../src/pipewire/pipewire.cc:341 [init_core]: PipeWireOutput: unable to initialize loop

Switching to PulseAudio or ALSA in settings should resolve this.

### [Context Menu opens wrong application]

When right-clicking a song from the playlist, \"Open Containing Folder\" does not respect the preferred file manager. This can be fixed by changing the default application in the desktop environment (e. g. [Xfce](https://wiki.gentoo.org/wiki/Xfce "Xfce")). The corresponding MIME-Type is called **inode/directory**.

### [No option shown for CD playback]

If [CDROM](https://wiki.gentoo.org/wiki/CDROM "CDROM") is configured correctly, \"Play CD\" should appear beneath the \"Services\" button. If not, the USE-Flag setting for *media-plugins/audacious-plugins*:^[\[1\]](#cite_note-1)^ may be misconfigured.

\

[FILE] **`/etc/portage/package.use`Enabling cdda locally**

    media-plugins/audacious-plugins cdda

1.  [[[↑](#cite_ref-1)] [[https://forums.gentoo.org/viewtopic-p-5925585.html](https://forums.gentoo.org/viewtopic-p-5925585.html)]]