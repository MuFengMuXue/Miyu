[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Dolphin_emulator&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

*Not to be confused with [KDE's file manager](https://wiki.gentoo.org/wiki/Dolphin "Dolphin").*

**Resources**

[[]][Home](https://dolphin-emu.org/)

[[]][Package information](https://packages.gentoo.org/packages/games-emulation/dolphin)

[[]][GitHub](https://github.com/dolphin-emu/dolphin)

**Dolphin** is an emulator for two recent Nintendo video game consoles: the GameCube and the Wii.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Troubleshooting]](#Troubleshooting)
        -   [[1.3.1] [Unable to start an emulation session on Wayland]](#Unable_to_start_an_emulation_session_on_Wayland)

## [Installation]

### [USE flags]

### [USE flags for] [games-emulation/dolphin](https://packages.gentoo.org/packages/games-emulation/dolphin) [[]] [Gamecube and Wii game emulator]

  --------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+evdev`](https://packages.gentoo.org/useflags/+evdev)                           Enable evdev input support
  [`+gui`](https://packages.gentoo.org/useflags/+gui)                               Enable support for a graphical user interface
  [`alsa`](https://packages.gentoo.org/useflags/alsa)                               Add support for media-libs/alsa-lib (Advanced Linux Sound Architecture)
  [`bluetooth`](https://packages.gentoo.org/useflags/bluetooth)                     Enable Bluetooth Support
  [`discord`](https://packages.gentoo.org/useflags/discord)                         Enables Discord Rich Presence, show the current game on Discord
  [`doc`](https://packages.gentoo.org/useflags/doc)                                 Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`egl`](https://packages.gentoo.org/useflags/egl)                                 Enable EGL (Embedded-System Graphics Library, interfacing between windowing system and OpenGL/GLES) support
  [`ffmpeg`](https://packages.gentoo.org/useflags/ffmpeg)                           Enable ffmpeg/libav-based audio/video codec support
  [`llvm`](https://packages.gentoo.org/useflags/llvm)                               Enables LLVM support, for disassembly
  [`log`](https://packages.gentoo.org/useflags/log)                                 Increase logging output
  [`mgba`](https://packages.gentoo.org/useflags/mgba)                               Enables GBA controllers emulation with games-emulation/mgba
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)                   Add sound server support via media-libs/libpulse (may be PulseAudio or PipeWire)
  [`retro-achievements`](https://packages.gentoo.org/useflags/retro-achievements)   Enables integration with retroachievements.org
  [`sdl`](https://packages.gentoo.org/useflags/sdl)                                 Add support for Simple Direct Layer (media library)
  [`systemd`](https://packages.gentoo.org/useflags/systemd)                         Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`telemetry`](https://packages.gentoo.org/useflags/telemetry)                     Send anonymized usage information to upstream so they can better understand our users
  [`test`](https://packages.gentoo.org/useflags/test)                               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`upnp`](https://packages.gentoo.org/useflags/upnp)                               Enable UPnP port mapping support
  [`vulkan`](https://packages.gentoo.org/useflags/vulkan)                           Add support for 3D graphics and computing via the Vulkan cross-platform API
  --------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-05 06:55] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Emerge Dolphin:

`root `[`#`]`emerge --ask games-emulation/dolphin`

### [Troubleshooting]

#### [Unable to start an emulation session on Wayland]

** Important**\
This workaround should not be used as upstream might support Wayland later and has already implemented the workaround within code with release 2506. In prior releases, the workaround is already defined in desktop file. See [[[bug #956364]](https://bugs.gentoo.org/show_bug.cgi?id=956364)[]].

Dolphin does not yet (as of 2025-06-06 with releases 2503 and 2506) directly support Wayland: [dolphin-emu fails to initialize OpenGL or Vulkan with QT_QPA_PLATFORM=wayland](https://bugs.dolphin-emu.org/issues/11807)

So trying to start an emulation session under a Wayland compositor can result in errors such as \"Failed to create Vulkan surface\", \"Failed to initialize video backend\" or \"Failed to create OpenGL window\".

As workarounds:

-   for releases 2506 and later, nothing to do, workaround is within code;
-   for releases prior 2506, either:
    -   use desktop file containing environment variable `QT_QPA_PLATFORM` set to `xcb`;
    -   run Dolphin explicitly with environment variable `QT_QPA_PLATFORM` set to `xcb`.

`user `[`$`]`env QT_QPA_PLATFORM=xcb dolphin-emu`