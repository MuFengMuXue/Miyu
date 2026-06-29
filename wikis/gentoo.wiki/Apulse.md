[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Apulse&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[[]][Package information](https://packages.gentoo.org/packages/media-sound/apulse)

[[]][GitHub](https://github.com/i-rinat/apulse)

**apulse** provides [PulseAudio](https://wiki.gentoo.org/wiki/PulseAudio "PulseAudio") emulation for [ALSA](https://wiki.gentoo.org/wiki/ALSA "ALSA"). This allows sound from applications that use the Pulse API (e.g. [Firefox](https://wiki.gentoo.org/wiki/Firefox "Firefox")) on a pure-ALSA system.

> Internally, no separate sound mixing daemon is used. Instead, apulse relies on ALSA\'s `dmix`, `dsnoop`, and `plug` plugins to handle multiple sound sources and capture streams running at the same time. \[The\] `dmix` plugin muxes multiple playback streams; \[the\] `dsnoop` plugin allow multiple applications to capture from a single microphone; and \[the\] `plug` plugin transparently converts audio between various sample formats, sample rates and channel numbers.

## [Installation]

### [USE flags]

### [USE flags for] [media-sound/apulse](https://packages.gentoo.org/packages/media-sound/apulse) [[]] [PulseAudio emulation for ALSA]

  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`debug`](https://packages.gentoo.org/useflags/debug)   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`sdk`](https://packages.gentoo.org/useflags/sdk)       Install PulseAudio headers and pkg-config files. Be aware apulse is not a full PulseAudio replacement by design and some functionality may be missing.
  [`test`](https://packages.gentoo.org/useflags/test)     Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-07 01:24] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

** Warning**\
The `sdk` USE flag blocks [[[media-libs/libpulse]](https://packages.gentoo.org/packages/media-libs/libpulse)[]].

### [Emerge]

Emerge apulse:

`root `[`#`]`emerge --ask media-sound/apulse`