This page contains [[changes](https://wiki.gentoo.org/index.php?title=MPlayer&diff=1325042)] which are not marked for translation.

**Resources**

[[]][Home](http://www.mplayerhq.hu)

[[]][Wikipedia](https://en.wikipedia.org/wiki/MPlayer "wikipedia:MPlayer")

[[]][[#mplayer](ircs://irc.libera.chat/#mplayer)] ([[webchat](https://web.libera.chat/#mplayer)])

**MPlayer** is a powerful command-line media player.

** Note**\
MPlayer is not very actively maintained anymore, but still alive. However, its fork [MPV](https://wiki.gentoo.org/wiki/Mpv "Mpv") is active and it comes with some extra features too.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [GUI tools]](#GUI_tools)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Streaming videos from websites]](#Streaming_videos_from_websites)
-   [[4] [Tips]](#Tips)
    -   [[4.1] [Disable screensaver while playing a video]](#Disable_screensaver_while_playing_a_video)
    -   [[4.2] [OSD menu]](#OSD_menu)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [My video won\'t play!]](#My_video_won.27t_play.21)

## [Installation]

### [USE flags]

### [USE flags for] [media-video/mplayer](https://packages.gentoo.org/packages/media-video/mplayer) [[]] [Media Player for Linux]

  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+X`](https://packages.gentoo.org/useflags/+X)                         Add support for X11
  [`+alsa`](https://packages.gentoo.org/useflags/+alsa)                   Add support for media-libs/alsa-lib (Advanced Linux Sound Architecture)
  [`+cdio`](https://packages.gentoo.org/useflags/+cdio)                   Use libcdio for CD support (instead of cdparanoia)
  [`+dvd`](https://packages.gentoo.org/useflags/+dvd)                     Add support for DVDs
  [`+dvdnav`](https://packages.gentoo.org/useflags/+dvdnav)               Use forked libdvdnav, navigate menus in GUIs
  [`+enca`](https://packages.gentoo.org/useflags/+enca)                   Enables support for charset discovery and conversion
  [`+encode`](https://packages.gentoo.org/useflags/+encode)               Add support for encoding of audio or video files
  [`+iconv`](https://packages.gentoo.org/useflags/+iconv)                 Enable support for the iconv character set conversion library
  [`+libass`](https://packages.gentoo.org/useflags/+libass)               SRT/SSA/ASS (SubRip / SubStation Alpha) subtitle support
  [`+network`](https://packages.gentoo.org/useflags/+network)             Enables network streaming support
  [`+osdmenu`](https://packages.gentoo.org/useflags/+osdmenu)             Enables support for on-screen display (OSD) menus
  [`+shm`](https://packages.gentoo.org/useflags/+shm)                     Enable support for shm
  [`+truetype`](https://packages.gentoo.org/useflags/+truetype)           Add support for FreeType and/or FreeType2 fonts
  [`+unicode`](https://packages.gentoo.org/useflags/+unicode)             Add support for Unicode
  [`+xscreensaver`](https://packages.gentoo.org/useflags/+xscreensaver)   Add support for XScreenSaver extension
  [`+xv`](https://packages.gentoo.org/useflags/+xv)                       Add in optional support for the Xvideo extension (an X API for video playback)
  [`a52`](https://packages.gentoo.org/useflags/a52)                       Enable support for decoding ATSC A/52 streams used in DVD
  [`aalib`](https://packages.gentoo.org/useflags/aalib)                   Add support for media-libs/aalib (ASCII-Graphics Library)
  [`aqua`](https://packages.gentoo.org/useflags/aqua)                     Include support for the Mac OS X Aqua (Carbon/Cocoa) GUI
  [`bidi`](https://packages.gentoo.org/useflags/bidi)                     Enable bidirectional language support
  [`bl`](https://packages.gentoo.org/useflags/bl)                         Blinkenlights video output
  [`bluray`](https://packages.gentoo.org/useflags/bluray)                 Enable playback of Blu-ray filesystems
  [`bs2b`](https://packages.gentoo.org/useflags/bs2b)                     Enable Bauer stereophonic-to-binaural headphone filter
  [`cddb`](https://packages.gentoo.org/useflags/cddb)                     Access cddb servers to retrieve and submit information about compact disks
  [`cdparanoia`](https://packages.gentoo.org/useflags/cdparanoia)         Enable cdparanoia (audio CD ripper) support
  [`cpudetection`](https://packages.gentoo.org/useflags/cpudetection)     Enables runtime CPU detection (useful for binpkgs, compatibility on other CPUs)
  [`debug`](https://packages.gentoo.org/useflags/debug)                   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`dga`](https://packages.gentoo.org/useflags/dga)                       Add DGA (Direct Graphic Access) support for X
  [`doc`](https://packages.gentoo.org/useflags/doc)                       Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`dts`](https://packages.gentoo.org/useflags/dts)                       Enable DTS Coherent Acoustics decoder support
  [`dv`](https://packages.gentoo.org/useflags/dv)                         Enable support for a codec used by many camcorders
  [`dvb`](https://packages.gentoo.org/useflags/dvb)                       Add support for DVB (Digital Video Broadcasting)
  [`faac`](https://packages.gentoo.org/useflags/faac)                     Use external faac library for AAC encoding
  [`faad`](https://packages.gentoo.org/useflags/faad)                     Use external faad library for AAC decoding
  [`fbcon`](https://packages.gentoo.org/useflags/fbcon)                   Add framebuffer support for the console, via the kernel
  [`ftp`](https://packages.gentoo.org/useflags/ftp)                       Add FTP (File Transfer Protocol) support
  [`ggi`](https://packages.gentoo.org/useflags/ggi)                       Add support for media-libs/libggi (non-X video api/drivers)
  [`gsm`](https://packages.gentoo.org/useflags/gsm)                       Add support for the gsm lossy speech compression codec
  [`ipv6`](https://packages.gentoo.org/useflags/ipv6)                     Add support for IP version 6
  [`jack`](https://packages.gentoo.org/useflags/jack)                     Add support for the JACK Audio Connection Kit
  [`joystick`](https://packages.gentoo.org/useflags/joystick)             Add support for joysticks in all packages
  [`jpeg`](https://packages.gentoo.org/useflags/jpeg)                     Add JPEG image support
  [`ladspa`](https://packages.gentoo.org/useflags/ladspa)                 Enable the ability to support ladspa plugins
  [`libcaca`](https://packages.gentoo.org/useflags/libcaca)               Add support for colored ASCII-art graphics
  [`libmpeg2`](https://packages.gentoo.org/useflags/libmpeg2)             Build support for mpeg2 over media-libs/libmpeg2 rather than using ffmpeg.
  [`lirc`](https://packages.gentoo.org/useflags/lirc)                     Add support for lirc (Linux\'s Infra-Red Remote Control)
  [`live`](https://packages.gentoo.org/useflags/live)                     Enables live.com streaming media support
  [`lzo`](https://packages.gentoo.org/useflags/lzo)                       Enable support for lzo compression
  [`mad`](https://packages.gentoo.org/useflags/mad)                       Add support for mad (high-quality mp3 decoder library and cli frontend)
  [`md5sum`](https://packages.gentoo.org/useflags/md5sum)                 Enables md5sum video output
  [`mng`](https://packages.gentoo.org/useflags/mng)                       MNG input support
  [`mp3`](https://packages.gentoo.org/useflags/mp3)                       Add support for reading mp3 files
  [`nas`](https://packages.gentoo.org/useflags/nas)                       Add support for network audio sound
  [`openal`](https://packages.gentoo.org/useflags/openal)                 Add support for the Open Audio Library
  [`opengl`](https://packages.gentoo.org/useflags/opengl)                 Add support for OpenGL (3D graphics)
  [`oss`](https://packages.gentoo.org/useflags/oss)                       Add support for OSS (Open Sound System)
  [`png`](https://packages.gentoo.org/useflags/png)                       Add support for libpng (PNG images)
  [`pnm`](https://packages.gentoo.org/useflags/pnm)                       Add PNM video output option, to create PPM/PGM/PGMYUV images
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)         Add sound server support via media-libs/libpulse (may be PulseAudio or PipeWire)
  [`pvr`](https://packages.gentoo.org/useflags/pvr)                       Enable Video4Linux2 MPEG PVR
  [`radio`](https://packages.gentoo.org/useflags/radio)                   Enable V4L2 radio interface and support
  [`rar`](https://packages.gentoo.org/useflags/rar)                       Enable Unique RAR File Library
  [`rtc`](https://packages.gentoo.org/useflags/rtc)                       Enables usage of the linux real time clock. The alternative is software emulation of rtc
  [`rtmp`](https://packages.gentoo.org/useflags/rtmp)                     Enables RTMPDump Streaming Media support
  [`samba`](https://packages.gentoo.org/useflags/samba)                   Add support for SAMBA (Windows File and Printer sharing)
  [`sdl`](https://packages.gentoo.org/useflags/sdl)                       Add support for Simple Direct Layer (media library)
  [`selinux`](https://packages.gentoo.org/useflags/selinux)               !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`speex`](https://packages.gentoo.org/useflags/speex)                   Add support for the speex audio codec (used for speech)
  [`tga`](https://packages.gentoo.org/useflags/tga)                       Enables Targa video output
  [`theora`](https://packages.gentoo.org/useflags/theora)                 Add support for the Theora Video Compression Codec
  [`toolame`](https://packages.gentoo.org/useflags/toolame)               Enable toolame MPEG-2 encoding
  [`tremor`](https://packages.gentoo.org/useflags/tremor)                 Enable internal support for Vorbis
  [`twolame`](https://packages.gentoo.org/useflags/twolame)               Enable twolame MPEG-2 encoding
  [`v4l`](https://packages.gentoo.org/useflags/v4l)                       Enable support for video4linux (using linux-headers or userspace libv4l libraries)
  [`vcd`](https://packages.gentoo.org/useflags/vcd)                       Enables VCD support
  [`vdpau`](https://packages.gentoo.org/useflags/vdpau)                   Enable the Video Decode and Presentation API for Unix acceleration interface
  [`vidix`](https://packages.gentoo.org/useflags/vidix)                   Support for vidix video output
  [`vorbis`](https://packages.gentoo.org/useflags/vorbis)                 Add support for the OggVorbis audio codec
  [`x264`](https://packages.gentoo.org/useflags/x264)                     Enable H.264 encoding using x264
  [`xinerama`](https://packages.gentoo.org/useflags/xinerama)             Add support for querying multi-monitor screen geometry through the Xinerama API
  [`xvid`](https://packages.gentoo.org/useflags/xvid)                     Add support for xvid.org\'s open-source mpeg-4 codec
  [`yuv4mpeg`](https://packages.gentoo.org/useflags/yuv4mpeg)             Enables yuv4mpeg video output
  [`zoran`](https://packages.gentoo.org/useflags/zoran)                   Enables ZR360\[56\]7/ZR36060 video output
  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-11-04 09:36] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[media-video/mplayer]](https://packages.gentoo.org/packages/media-video/mplayer)[]]:

`root `[`#`]`emerge --ask media-video/mplayer`

## [Configuration]

### [GUI tools]

There are a number of different GUI\'s for MPlayer with different levels of functionality. Some notable ones include:

-   [[[media-video/gnome-mplayer]](https://packages.gentoo.org/packages/media-video/gnome-mplayer)[]]
-   [[[media-video/kmplayer]](https://packages.gentoo.org/packages/media-video/kmplayer)[]]
-   [[[media-video/smplayer]](https://packages.gentoo.org/packages/media-video/smplayer)[]]

## [Usage]

### [Streaming videos from websites]

MPlayer has the ability to stream videos from websites. As a prerequisite, [[[media-video/ffmpeg]](https://packages.gentoo.org/packages/media-video/ffmpeg)[]] must have the `openssl` and `gnutls` USE flags enabled. To do this, simply enter the command:

`user `[`$`]`mplayer `*`url`*

Where *url* is the URL of the video.

## [Tips]

### [Disable screensaver while playing a video]

Using qdbus (Qt/KDE):

[FILE] **`~/.mplayer/config`**

    heartbeat-cmd="qdbus org.freedesktop.ScreenSaver /ScreenSaver SimulateUserActivity"

For systems using xscreensaver alone:

[FILE] **`~/.mplayer/config`**

    heartbeat-cmd="xscreensaver-command -deactivate >&- 2>&- &"

See [this FAQ entry](https://www.jwz.org/xscreensaver/faq.html#dvd) for more informations.

### [OSD menu]

By default, the OSD display will only give information about the actions related to its key and mouse bindings. To add MPlayer main OSD menu, do:

`user `[`$`]`cp /etc/mplayer/input.conf ~/.mplayer/input.conf`

[FILE] **`~/.mplayer/input.conf`**

    # main OSD menu; can be any key (or mouse button)
    # "m" is already assigned to the mute function.
    h menu main

Then start

`user `[`$`]`mplayer -menu`

or edit:

[FILE] **`~/.mplayer/config`**

    }}

Note: I don\'t know why that FileBox doesn\'t work. The text to add is *menu=yes*.

See [MPlayer - OSD Menu](https://en.wikibooks.org/wiki/MPlayer#OSD_Menu) for more on that matter.

## [Troubleshooting]

### [][My video won\'t play!]

MPlayer uses USE flags to enable and disable support for various codecs. If a particular type of file will not play in MPlayer, first check which USE flags MPlayer was emerged with. Update the USE flags to support for the format you are trying to play and recompile.