[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=PCSX2&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://pcsx2.net/)

[[]][Package information](https://packages.gentoo.org/packages/games-emulation/pcsx2)

[[]][GitHub](https://github.com/PCSX2/pcsx2)

**PCSX2** is a free and open-source PlayStation 2 emulator for x86 computers. It supports most PlayStation 2 games with high compatibility rates and can apply enhancements to gameplay, including features like widescreen patches, improved resolutions or use of custom textures.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
        -   [[1.2.1] [Unstable version]](#Unstable_version)
    -   [[1.3] [Flatpak]](#Flatpak)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [PCSX2 requires a PS2 BIOS in order to run]](#PCSX2_requires_a_PS2_BIOS_in_order_to_run)
    -   [[3.2] [Games run slow or have graphical glitches]](#Games_run_slow_or_have_graphical_glitches)
-   [[4] [See also]](#See_also)

## [Installation]

### [[] USE flags]

### [USE flags for] [games-emulation/pcsx2](https://packages.gentoo.org/packages/games-emulation/pcsx2) [[]] [PlayStation 2 emulator]

  ----------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+clang`](https://packages.gentoo.org/useflags/+clang)           Use Clang compiler to build (the only compiler that is currently supported by upstream on Linux, do not report bugs if force-disabled)
  [`+filecaps`](https://packages.gentoo.org/useflags/+filecaps)     Use Linux file capabilities to control privilege rather than set\*id (this is orthogonal to USE=caps which uses capabilities at runtime e.g. libcap)
  [`alsa`](https://packages.gentoo.org/useflags/alsa)               Add support for media-libs/alsa-lib (Advanced Linux Sound Architecture)
  [`jack`](https://packages.gentoo.org/useflags/jack)               Add support for the JACK Audio Connection Kit
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)   Add sound server support via media-libs/libpulse (may be PulseAudio or PipeWire)
  [`sndio`](https://packages.gentoo.org/useflags/sndio)             Enable support for the media-sound/sndio backend
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`wayland`](https://packages.gentoo.org/useflags/wayland)         Enable dev-libs/wayland backend
  ----------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-27 03:48] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

PCSX2 is available in the main Gentoo repository. You can install it by issuing:

`root `[`#`]`emerge --ask games-emulation/pcsx2`

#### [Unstable version]

PCSX2 is a fast moving piece of software, and lots of bugs and compatibility issues are fixed daily. Upstream usually recommends using the unstable version of PCSX2, which may be enabled via adding PCSX2 to [package.accept_keywords]. An example file may look like this:

[FILE] **`/etc/portage/package.accept_keywords/pcsx2`**

    games-emulation/pcsx2 **

Then PCSX2 should be built:

`root `[`#`]`emerge --ask games-emulation/pcsx2`

### [Flatpak]

PCSX2 is also available on Flathub, the main [Flatpak](https://wiki.gentoo.org/wiki/Flatpak "Flatpak") repository. To add the flathub repository:

`user `[`$`]`flatpak remote-add --user --if-not-exists flathub `[`https://flathub.org/repo/flathub.flatpakrepo`](https://flathub.org/repo/flathub.flatpakrepo)

And then install the PCSX2 package:

`user `[`$`]`flatpak install --user flathub net.pcsx2.PCSX2`

## [Configuration]

PCSX2\'s configuration folder is automatically set to [\~/.config/PCSX2] (or [\~/.var/app/net.pcsx2.PCSX2/config/PCSX2] for Flatpak installations). This folder contains subfolders where BIOS files, virtual Memory Cards, save states, screenshots and cheats are stored by default, amongst other resources. These paths can be changed inside PCSX2\'s GUI configuration menu.

## [Troubleshooting]

### [PCSX2 requires a PS2 BIOS in order to run]

Because of copyright law, PCSX2 can\'t nor will ever provide any BIOS files with the emulator. Check the official documentation at [https://pcsx2.net/docs/setup/bios](https://pcsx2.net/docs/setup/bios) to learn how to dump the BIOS files from an original PlayStation 2 to a computer, necessary to run games on PCSX2.

### [Games run slow or have graphical glitches]

The PlayStation 2 may not be as easy to emulate as previous, older video game consoles. A game running slow may be because of underpowered hardware, a rendering or compatibility issue with the specific game, or a combination of the two. PCSX2\'s minimum (and recommended) hardware requirements are listed at [https://pcsx2.net/docs/setup/requirements](https://pcsx2.net/docs/setup/requirements), and there\'s a full game compatibility list at [https://pcsx2.net/compat/](https://pcsx2.net/compat/) for users to check if a video game is considered playable in the first place.

## [See also]

-   [Games/emulation](https://wiki.gentoo.org/wiki/Games/emulation "Games/emulation") --- provides an overview of game emulators available in the ::gentoo ebuild repository.