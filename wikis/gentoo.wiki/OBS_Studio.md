Other languages:

-   [English]

**Resources**

[[]][Home](https://obsproject.com/)

[[]][GitHub](https://github.com/obsproject/obs-studio)

[[]][Package information](https://packages.gentoo.org/packages/media-video/obs-studio)

**OBS Studio** is free software for video recording and live streaming.

Built with [Qt](https://wiki.gentoo.org/wiki/Qt "Qt"), C and C++ and maintained by the OBS Project, the software provides real-time device capture, scene composition, recording, broadcasting and source capture functions with presets for streaming to popular services such as YouTube, Twitch, Instagram and Facebook^[\[1\]](#cite_note-1)^.

In 2014, development started on a rewrite of the software, known as OBS Multiplatform, which included a larger feature set, multi-platform support and broader plugin support^[\[2\]](#cite_note-2)^. As of 2016, the software was rebranded as OBS Studio, with the older OBS Classic being deprecated.^[\[3\]](#cite_note-3)^

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Additional software]](#Additional_software)
        -   [[1.3.1] [Audio]](#Audio)
        -   [[1.3.2] [VLC]](#VLC)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
-   [[3] [Removal]](#Removal)
    -   [[3.1] [Unmerge]](#Unmerge)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Pipewire audio]](#Pipewire_audio)
    -   [[4.2] [Wayland]](#Wayland)
        -   [[4.2.1] [Shortcuts]](#Shortcuts)
        -   [[4.2.2] [Video capturing]](#Video_capturing)
    -   [[4.3] [Virtual camera]](#Virtual_camera)
-   [[5] [External Resources]](#External_Resources)
-   [[6] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [media-video/obs-studio](https://packages.gentoo.org/packages/media-video/obs-studio) [[]] [Software for Recording and Streaming Live Video Content]

  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+alsa`](https://packages.gentoo.org/useflags/+alsa)             Add support for media-libs/alsa-lib (Advanced Linux Sound Architecture)
  [`browser`](https://packages.gentoo.org/useflags/browser)         Enable browser source support via (precompiled) CEF.
  [`decklink`](https://packages.gentoo.org/useflags/decklink)       Build the Decklink plugin.
  [`fdk`](https://packages.gentoo.org/useflags/fdk)                 Build with LibFDK AAC support.
  [`jack`](https://packages.gentoo.org/useflags/jack)               Add support for the JACK Audio Connection Kit
  [`lua`](https://packages.gentoo.org/useflags/lua)                 Enable Lua scripting support
  [`mpegts`](https://packages.gentoo.org/useflags/mpegts)           Enable native SRT/RIST mpegts output.
  [`nvenc`](https://packages.gentoo.org/useflags/nvenc)             Add support for NVIDIA Encoder/Decoder (NVENC/NVDEC) API for hardware accelerated encoding and decoding on NVIDIA cards (requires x11-drivers/nvidia-drivers)
  [`pipewire`](https://packages.gentoo.org/useflags/pipewire)       Build with PipeWire support.
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)   Add sound server support via media-libs/libpulse (may be PulseAudio or PipeWire)
  [`python`](https://packages.gentoo.org/useflags/python)           Build with scripting support for Python 3.
  [`qsv`](https://packages.gentoo.org/useflags/qsv)                 Build with Intel Quick Sync Video support.
  [`sndio`](https://packages.gentoo.org/useflags/sndio)             Build with sndio support.
  [`speex`](https://packages.gentoo.org/useflags/speex)             Build with Speex noise suppression filter support.
  [`test-input`](https://packages.gentoo.org/useflags/test-input)   Build and install input sources used for testing.
  [`truetype`](https://packages.gentoo.org/useflags/truetype)       Add support for FreeType and/or FreeType2 fonts
  [`v4l`](https://packages.gentoo.org/useflags/v4l)                 Enable support for video4linux (using linux-headers or userspace libv4l libraries)
  [`vlc`](https://packages.gentoo.org/useflags/vlc)                 Build with VLC media source support.
  [`wayland`](https://packages.gentoo.org/useflags/wayland)         Enable dev-libs/wayland backend
  [`websocket`](https://packages.gentoo.org/useflags/websocket)     Build with WebSocket API support.
  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-19 13:04] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

For a standard streaming setup that uses a [webcam](https://wiki.gentoo.org/wiki/Webcam "Webcam"), [PulseAudio](https://wiki.gentoo.org/wiki/PulseAudio "PulseAudio"), has a [NVIDIA](https://wiki.gentoo.org/wiki/NVIDIA "NVIDIA") graphics card and integrates with major streaming services one might add to [/etc/portage/package.use]

[FILE] **`/etc/portage/package.use/obs-studio`**

    media-video/obs-studio lua nvenc pulseaudio speex v4l

### [Emerge]

Install [[[media-video/obs-studio]](https://packages.gentoo.org/packages/media-video/obs-studio)[]]:

`root `[`#`]`emerge --ask media-video/obs-studio`

### [Additional software]

#### [Audio]

OBS Studio can be paired with [JACK](https://wiki.gentoo.org/wiki/JACK "JACK"), [PulseAudio](https://wiki.gentoo.org/wiki/PulseAudio "PulseAudio") or [PipeWire](https://wiki.gentoo.org/wiki/PipeWire "PipeWire") for audio.

#### [VLC]

OBS Studio supports integration with [VLC media player](https://wiki.gentoo.org/wiki/VLC_media_player "VLC media player") services. VLC support behaves much like the ordinary media source, however in addition it accepts a list of files to play as well as provides a way to play every path, URL or media source that VLC is able to play.

## [Usage]

### [Invocation]

OBS Studio can be invoked from the command line as follows:

`user `[`$`]`obs --help`

    --help, -h: Get list of available commands.

    --startstreaming: Automatically start streaming.
    --startrecording: Automatically start recording.
    --startreplaybuffer: Start replay buffer.
    --startvirtualcam: Start virtual camera (if available).

    --collection <string>: Use specific scene collection.
    --profile <string>: Use specific profile.
    --scene <string>: Start with specific scene.

    --studio-mode: Enable studio mode.
    --minimize-to-tray: Minimize to system tray.
    --portable, -p: Use portable mode.
    --multi, -m: Don't warn when launching multiple instances.

    --verbose: Make log more verbose.
    --always-on-top: Start in 'always on top' mode.

    --unfiltered_log: Make log unfiltered.

    --disable-updater: Disable built-in updater (Windows/Mac only)

    --disable-high-dpi-scaling: Disable automatic high-DPI scaling

    --version, -V: Get current version.

## [Removal]

### [Unmerge]

Remove [[[media-video/obs-studio]](https://packages.gentoo.org/packages/media-video/obs-studio)[]]:

`root `[`#`]`emerge --ask --depclean --verbose media-video/obs-studio`

## [Troubleshooting]

### [Pipewire audio]

Install [pipewire plugin for OBS](https://obsproject.com/forum/resources/pipewire-audio-capture.1458/).

### [Wayland]

#### [Shortcuts]

As it\'s known, some wayland DE (i.e. KDE plasma) do not have a good support for shortcuts with wayland.

You can use `obs-studio` with `websocket` USE flag enabled and control OBS via sending commands to its websocket interface.

Check [this project](https://github.com/wordhater/obs-wayland-shortcuts-kde) for details.

#### [Video capturing]

If OBS Studio isn\'t able to capture windows or the fullscreen using Pipewire on a Wayland compositor, set the `pipewire` and `dbus` USE flags for [[[media-video/obs-studio]](https://packages.gentoo.org/packages/media-video/obs-studio)[]] and [[[media-video/pipewire]](https://packages.gentoo.org/packages/media-video/pipewire)[]] respectively:

[FILE] **`/etc/portage/package.use`**

    media-video/obs-studio pipewire
    media-video/pipewire dbus

Re-emerge these packages to apply the USE flag changes:

`root `[`#`]`emerge --ask media-video/obs-studio media-video/pipewire`

Emerge [[[gui-libs/xdg-desktop-portal-wlr]](https://packages.gentoo.org/packages/gui-libs/xdg-desktop-portal-wlr)[]]:

`root `[`#`]`emerge --ask gui-libs/xdg-desktop-portal-wlr`

** Note**\
This applies to window managers. If you\'re using a desktop environment such as KDE Plasma or GNOME, make sure to emerge the appropriate variant from the [XDG/xdg-desktop-portal](https://wiki.gentoo.org/wiki/XDG/xdg-desktop-portal "XDG/xdg-desktop-portal") page instead.

The `screencast` and `gstreamer` and `gles2` global use flags may also be required for some desktop environments.

[FILE] **`/etc/portage/make.conf`make.conf file**

    USE="screencast gstreamer gles2"

You may also need the package `qtwebkit`:

`root `[`#`]`emerge --ask dev-qt/qtwebkit`

### [Virtual camera]

For virtual camera support within OBS Studio, emerge the v4l2loopback kernel module:

`root `[`#`]`emerge --ask media-video/v4l2loopback`

For OBS Studio to initialize the kernel module, give it the appropriate permissions, this can be done by running it as root or using a polkit agent.

## [External Resources]

-   [OBS Tutorials](https://obstutorials.com/) - Tips and tricks for OBS Studio.
-   [OBS Project](https://obsproject.com/) - The OBS Project main site.
-   [OBS Documentation](https://obsproject.com/docs/) - Detailed information for developers and users alike.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://www.pcgamer.com/2012/12/04/how-to-set-up-open-broadcaster-a-free-lightweight-livestreaming-application/](https://www.pcgamer.com/2012/12/04/how-to-set-up-open-broadcaster-a-free-lightweight-livestreaming-application/)]]
2.  [[[↑](#cite_ref-2)] [[https://web.archive.org/web/20160309230843/https://obsproject.com/index](https://web.archive.org/web/20160309230843/https://obsproject.com/index)]]
3.  [[[↑](#cite_ref-3)] [[https://obsproject.com/forum/threads/obs-classic-is-no-longer-supported-heres-how-to-easily-switch-to-obs-studio.55820/](https://obsproject.com/forum/threads/obs-classic-is-no-longer-supported-heres-how-to-easily-switch-to-obs-studio.55820/)]]