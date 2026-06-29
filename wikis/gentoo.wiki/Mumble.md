[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Mumble&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://wiki.mumble.info/wiki/Main_Page)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Mumble_(software) "wikipedia:Mumble (software)")

[[]][GitHub](https://github.com/mumble-voip/mumble)

Mumble is an open source, cross platform, low-latency, high quality voice over IP (VoIP) client. Mumble uses a client/server architecture and is primarily used by gamers, but can be used for any VoIP purpose.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Removal]](#Removal)
    -   [[2.1] [Unmerge]](#Unmerge)
-   [[3] [See also]](#See_also)

## [Installation]

### [Kernel]

Many laptops have built-in USB microphones (almost always paired with USB web cameras). The kernel needs the `SND_USB_AUDIO` option enabled to support USB audio (input) devices.

[KERNEL] **Enable support for USB microphones (`SND_USB_AUDIO`)**

    Device Drivers -->
       Sound card support -->
          Advanced Linux Sound Architecture -->
             USB sound devices -->
                <*> USB Audio/MIDI driver

### [USE flags]

### [USE flags for] [net-voip/mumble](https://packages.gentoo.org/packages/net-voip/mumble) [[]] [Open source, low-latency, high quality voice chat software]

  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+alsa`](https://packages.gentoo.org/useflags/+alsa)             Add support for media-libs/alsa-lib (Advanced Linux Sound Architecture)
  [`+rnnoise`](https://packages.gentoo.org/useflags/+rnnoise)       Enable alternative noise suppression option based on RNNoise.
  [`debug`](https://packages.gentoo.org/useflags/debug)             Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`jack`](https://packages.gentoo.org/useflags/jack)               Add support for the JACK Audio Connection Kit
  [`multilib`](https://packages.gentoo.org/useflags/multilib)       On 64bit systems, if you want to be able to compile 32bit and 64bit binaries
  [`nls`](https://packages.gentoo.org/useflags/nls)                 Add Native Language Support (using gettext - GNU locale utilities)
  [`pipewire`](https://packages.gentoo.org/useflags/pipewire)       Enable pipewire support for audio output.
  [`portaudio`](https://packages.gentoo.org/useflags/portaudio)     Add support for the crossplatform portaudio audio API
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)   Add sound server support via media-libs/libpulse (may be PulseAudio or PipeWire)
  [`speech`](https://packages.gentoo.org/useflags/speech)           Enable text-to-speech support
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`zeroconf`](https://packages.gentoo.org/useflags/zeroconf)       Support for DNS Service Discovery (DNS-SD)
  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-02 05:02] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install Mumble:

`root `[`#`]`emerge --ask net-voip/mumble`

## [Removal]

### [Unmerge]

Uninstall Mumble by issuing:

`root `[`#`]`emerge --ask --depclean --verbose net-voip/mumble`

## [See also]

-   [Murmur](https://wiki.gentoo.org/wiki/Murmur "Murmur") --- the server component to [Mumble] built on the Qt framework.
-   [UMurmur](https://wiki.gentoo.org/wiki/UMurmur "UMurmur") --- a minimalistic server for Mumble designed to run on embedded systems (DD-WRT or OpenWRT) or older PC hardware.