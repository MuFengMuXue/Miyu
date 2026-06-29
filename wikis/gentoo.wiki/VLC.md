Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/VLC/es "VLC (65% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/VLC/hu "VLC (100% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/VLC/zh-cn "VLC (32% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/VLC/ja "VLC (100% translated)")

**Resources**

[[]][Home](https://www.videolan.org/vlc/)

[[]][Package information](https://packages.gentoo.org/packages/media-video/vlc)

[[]][Wikipedia](https://en.wikipedia.org/wiki/VLC_media_player "wikipedia:VLC media player")

[[]][Official documentation](https://wiki.videolan.org/Main_Page/)

[[]][GitHub](https://github.com/videolan/vlc)

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Video/VLC "Project:Video/VLC")][Project](https://wiki.gentoo.org/wiki/Project:Video/VLC "Project:Video/VLC")

**VLC** media player is a wildly popular, cross platform video player and streamer. VLC media player has been quickly achieving its goal of world domination^[\[1\]](#cite_note-1)^ since its initial release in February of 2001.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Streaming online multimedia]](#Streaming_online_multimedia)
    -   [[1.3] [WebM support]](#WebM_support)
    -   [[1.4] [VLSub]](#VLSub)
    -   [[1.5] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Alternate interfaces]](#Alternate_interfaces)
        -   [[2.1.1] [HTTP]](#HTTP)
    -   [[2.2] [Hotkeys]](#Hotkeys)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)
-   [[5] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [media-video/vlc](https://packages.gentoo.org/packages/media-video/vlc) [[]] [Media player and framework with support for most multimedia files and streaming]

  ------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+X`](https://packages.gentoo.org/useflags/+X)                                       Enable support for e.g. fullscreen mode via X and the X C-language binding. It does not build a graphical interface
  [`+dvbpsi`](https://packages.gentoo.org/useflags/+dvbpsi)                             Enable support for Mpeg-TS files (.ts, .m2ts, .mts) via media-libs/libdvbpsi
  [`+encode`](https://packages.gentoo.org/useflags/+encode)                             Enable streaming-output support and videolan manager to control multiple streams from within one instance
  [`+ffmpeg`](https://packages.gentoo.org/useflags/+ffmpeg)                             Enable ffmpeg/libav-based audio/video codec support
  [`+gcrypt`](https://packages.gentoo.org/useflags/+gcrypt)                             Enable cryptography support via libgcrypt
  [`+gui`](https://packages.gentoo.org/useflags/+gui)                                   Enable support for a graphical user interface
  [`+libsamplerate`](https://packages.gentoo.org/useflags/+libsamplerate)               Build with support for converting sample rates using libsamplerate
  [`a52`](https://packages.gentoo.org/useflags/a52)                                     Enable support for decoding ATSC A/52 streams used in DVD
  [`alsa`](https://packages.gentoo.org/useflags/alsa)                                   Add support for media-libs/alsa-lib (Advanced Linux Sound Architecture)
  [`aom`](https://packages.gentoo.org/useflags/aom)                                     Enable AV1 encoding/decoding support using media-libs/libaom
  [`archive`](https://packages.gentoo.org/useflags/archive)                             Enable support for libarchive stream extractor
  [`aribsub`](https://packages.gentoo.org/useflags/aribsub)                             Enable support for decoding ARIB STD-B24 subtitles
  [`bidi`](https://packages.gentoo.org/useflags/bidi)                                   Enable bidirectional language support
  [`bluray`](https://packages.gentoo.org/useflags/bluray)                               Enable libbluray for Blu-ray disc support
  [`cddb`](https://packages.gentoo.org/useflags/cddb)                                   Access cddb servers to retrieve and submit information about compact disks
  [`chromaprint`](https://packages.gentoo.org/useflags/chromaprint)                     Enable libchromaprint for Chromaprint based audio fingerprinter support
  [`chromecast`](https://packages.gentoo.org/useflags/chromecast)                       Enable experimental support for Google Chromecast
  [`dav1d`](https://packages.gentoo.org/useflags/dav1d)                                 Enable support for media-libs/dav1d AV1 decoder
  [`dbus`](https://packages.gentoo.org/useflags/dbus)                                   Enable dbus support for anything that needs it (gpsd, gnomemeeting, etc)
  [`dc1394`](https://packages.gentoo.org/useflags/dc1394)                               Enable IIDC cameras support
  [`debug`](https://packages.gentoo.org/useflags/debug)                                 Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`directx`](https://packages.gentoo.org/useflags/directx)                             Enable Win32 DirectX, D3D11va and DxVA2 support
  [`dts`](https://packages.gentoo.org/useflags/dts)                                     Enable DTS Coherent Acoustics decoder support
  [`dvd`](https://packages.gentoo.org/useflags/dvd)                                     Add support for DVDs
  [`faad`](https://packages.gentoo.org/useflags/faad)                                   Enable AAC audio decoding library support via media-libs/faad2
  [`fdk`](https://packages.gentoo.org/useflags/fdk)                                     Enable the Fraunhofer AAC codec library
  [`flac`](https://packages.gentoo.org/useflags/flac)                                   Add support for FLAC: Free Lossless Audio Codec
  [`fluidsynth`](https://packages.gentoo.org/useflags/fluidsynth)                       Enable Fluidsynth MIDI software synthesis (with external sound fonts)
  [`fontconfig`](https://packages.gentoo.org/useflags/fontconfig)                       Support for configuring and customizing font access via media-libs/fontconfig
  [`gme`](https://packages.gentoo.org/useflags/gme)                                     Enable support for media-libs/game-music-emu for playing various video game music formats
  [`gstreamer`](https://packages.gentoo.org/useflags/gstreamer)                         Enable GStreamer based decoding support (currently supports only video decoding)
  [`ieee1394`](https://packages.gentoo.org/useflags/ieee1394)                           Enable FireWire/iLink IEEE1394 support (dv, camera, \...)
  [`jack`](https://packages.gentoo.org/useflags/jack)                                   Add support for the JACK Audio Connection Kit
  [`jpeg`](https://packages.gentoo.org/useflags/jpeg)                                   Add JPEG image support
  [`kate`](https://packages.gentoo.org/useflags/kate)                                   Adds support for Ogg Kate subtitles via libkate
  [`keyring`](https://packages.gentoo.org/useflags/keyring)                             Enable support for freedesktop.org Secret Service API password store
  [`libass`](https://packages.gentoo.org/useflags/libass)                               SRT/SSA/ASS (SubRip / SubStation Alpha) subtitle support
  [`libcaca`](https://packages.gentoo.org/useflags/libcaca)                             Add support for colored ASCII-art graphics
  [`libdrm`](https://packages.gentoo.org/useflags/libdrm)                               Enable kernel mode setting video output plugin via x11-libs/libdrm
  [`libnotify`](https://packages.gentoo.org/useflags/libnotify)                         Enable desktop notification support
  [`libplacebo`](https://packages.gentoo.org/useflags/libplacebo)                       Enable support for GPU accelerated video rendering with media-libs/libplacebo
  [`libtiger`](https://packages.gentoo.org/useflags/libtiger)                           Enable Ogg Kate subtitles rendering using libtiger
  [`linsys`](https://packages.gentoo.org/useflags/linsys)                               Enable support for Linux Linear Systems Ltd. SDI and HD-SDI input cards
  [`lirc`](https://packages.gentoo.org/useflags/lirc)                                   Add support for lirc (Linux\'s Infra-Red Remote Control)
  [`live`](https://packages.gentoo.org/useflags/live)                                   Enable live555 streaming media support (client support for rtsp)
  [`loudness`](https://packages.gentoo.org/useflags/loudness)                           Enable loudness normalisation according to the EBU R128 standard using media-libs/libebur128
  [`lua`](https://packages.gentoo.org/useflags/lua)                                     Enable Lua scripting support, needed for including support for Jamendo (online music platform) and similar things
  [`macosx-notifications`](https://packages.gentoo.org/useflags/macosx-notifications)   Enable Mac OS X notifications module (formerly growl)
  [`mad`](https://packages.gentoo.org/useflags/mad)                                     Add support for mad (high-quality mp3 decoder library and cli frontend)
  [`matroska`](https://packages.gentoo.org/useflags/matroska)                           Enable matroska support using reference libraries (fallback on other existing matroska support if disabled, i.e., matroska enabled FFmpeg)
  [`modplug`](https://packages.gentoo.org/useflags/modplug)                             Add libmodplug support for playing SoundTracker-style music files
  [`mp3`](https://packages.gentoo.org/useflags/mp3)                                     Add support for reading mp3 files
  [`mpeg`](https://packages.gentoo.org/useflags/mpeg)                                   Add libmpeg2 support for mpeg-1 and mpeg-2 video streams
  [`mtp`](https://packages.gentoo.org/useflags/mtp)                                     Enable support for Media Transfer Protocol
  [`musepack`](https://packages.gentoo.org/useflags/musepack)                           Enable support for the musepack audio codec
  [`ncurses`](https://packages.gentoo.org/useflags/ncurses)                             Add ncurses support (console display library)
  [`nfs`](https://packages.gentoo.org/useflags/nfs)                                     Enable support for nfs protocol via net-fs/libnfs
  [`ogg`](https://packages.gentoo.org/useflags/ogg)                                     Add support for the Ogg container format (commonly used by Vorbis, Theora and flac)
  [`omxil`](https://packages.gentoo.org/useflags/omxil)                                 Enable OpenMAX Integration Layer codec module
  [`optimisememory`](https://packages.gentoo.org/useflags/optimisememory)               Enable optimisation for memory rather than performance
  [`opus`](https://packages.gentoo.org/useflags/opus)                                   Enable Opus audio codec support
  [`png`](https://packages.gentoo.org/useflags/png)                                     Add support for libpng (PNG images)
  [`projectm`](https://packages.gentoo.org/useflags/projectm)                           Enable the projectM visualization plugin
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)                       Add sound server support via media-libs/libpulse (may be PulseAudio or PipeWire)
  [`run-as-root`](https://packages.gentoo.org/useflags/run-as-root)                     Allows vlc to start for root. Don\'t enable this unless you have a very specific (e.g. embedded) need for it!
  [`samba`](https://packages.gentoo.org/useflags/samba)                                 Add support for SAMBA (Windows File and Printer sharing)
  [`sdl-image`](https://packages.gentoo.org/useflags/sdl-image)                         Enable sdl image video decoder (depends on sdl)
  [`selinux`](https://packages.gentoo.org/useflags/selinux)                             !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`sftp`](https://packages.gentoo.org/useflags/sftp)                                   Enable libssh2 to support SFTP file transfer
  [`shout`](https://packages.gentoo.org/useflags/shout)                                 Enable libshout output
  [`sid`](https://packages.gentoo.org/useflags/sid)                                     Enable SID (Commodore 64 audio) file support
  [`skins`](https://packages.gentoo.org/useflags/skins)                                 Enable support for the skins2 interface
  [`soxr`](https://packages.gentoo.org/useflags/soxr)                                   Enable SoX Resampler support via media-libs/soxr
  [`speex`](https://packages.gentoo.org/useflags/speex)                                 Add support for the speex audio codec (used for speech)
  [`srt`](https://packages.gentoo.org/useflags/srt)                                     Enable support for Secure Reliable Transport (SRT) via net-libs/srt
  [`ssl`](https://packages.gentoo.org/useflags/ssl)                                     Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  [`svg`](https://packages.gentoo.org/useflags/svg)                                     Add support for SVG (Scalable Vector Graphics)
  [`taglib`](https://packages.gentoo.org/useflags/taglib)                               Enable tagging support with taglib
  [`test`](https://packages.gentoo.org/useflags/test)                                   Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`theora`](https://packages.gentoo.org/useflags/theora)                               Add support for the Theora Video Compression Codec
  [`tremor`](https://packages.gentoo.org/useflags/tremor)                               Enable tremor, a fixed-point version of the Ogg Vorbis decoder
  [`truetype`](https://packages.gentoo.org/useflags/truetype)                           Add support for FreeType and/or FreeType2 fonts
  [`twolame`](https://packages.gentoo.org/useflags/twolame)                             Enable twolame support (MPEG Audio Layer 2 encoder)
  [`udev`](https://packages.gentoo.org/useflags/udev)                                   Enable virtual/udev integration (device discovery, power and storage device support, etc)
  [`upnp`](https://packages.gentoo.org/useflags/upnp)                                   Enable support for the Intel SDK stack based UPnP discovery module instead of CyberLink
  [`v4l`](https://packages.gentoo.org/useflags/v4l)                                     Enable support for video4linux (using linux-headers or userspace libv4l libraries)
  [`vaapi`](https://packages.gentoo.org/useflags/vaapi)                                 Enable Video Acceleration API for hardware decoding
  [`vdpau`](https://packages.gentoo.org/useflags/vdpau)                                 Enable the Video Decode and Presentation API for Unix acceleration interface
  [`vnc`](https://packages.gentoo.org/useflags/vnc)                                     Enable VNC (remote desktop viewer) support
  [`vpx`](https://packages.gentoo.org/useflags/vpx)                                     Add support for VP8/VP9 codecs (usually via media-libs/libvpx)
  [`wayland`](https://packages.gentoo.org/useflags/wayland)                             Enable dev-libs/wayland backend
  [`x264`](https://packages.gentoo.org/useflags/x264)                                   Enable H.264 encoding using x264
  [`x265`](https://packages.gentoo.org/useflags/x265)                                   Support X265 Encoder
  [`xml`](https://packages.gentoo.org/useflags/xml)                                     Add support for XML files
  [`zeroconf`](https://packages.gentoo.org/useflags/zeroconf)                           Enable support for zero-configuration networking via avahi
  [`zvbi`](https://packages.gentoo.org/useflags/zvbi)                                   Enable support for teletext subtitles via the zvbi library
  ------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-26 00:38] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

According to VideoLAN some certain USE flags need to be set in order to not get a very bare bones version of VLC.^[\[2\]](#cite_note-2)^ Many of them might be obsolete or be set by the selected [profile](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)").

### [Streaming online multimedia]

VLC provides users with the option to stream multimedia objects (YouTube, Vimeo, music, and more). To enable this functionality, simply enable the `lua` USE flag. If [[[app-portage/gentoolkit]](https://packages.gentoo.org/packages/app-portage/gentoolkit)[]] is installed (it is a highly recommended package to have), simply issue:

`root `[`#`]`euse -E lua -p media-video/vlc`

After proper configuration and installation, streams can be opened via [Media \--\> Open Network Stream\...]. Enter URLs to popular multimedia websites, such as YouTube or other websites.

### [WebM support]

WebM is a popular video format. To have it work the [[[vorbis]](https://packages.gentoo.org/useflags/vorbis)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")], [[[vpx]](https://packages.gentoo.org/useflags/vpx)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")], and [[[matroska]](https://packages.gentoo.org/useflags/matroska)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flags must be enabled.

### [VLSub]

VLSub is an optional lua extension to automatically download subtitles from [www.opensubtitles.org](https://www.opensubtitles.org). To use it the [[[lua]](https://packages.gentoo.org/useflags/lua)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] and [[[archive]](https://packages.gentoo.org/useflags/archive)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] flags must be enabled.

### [Emerge]

After setting desired USE flags for the initial installation, [emerge] VLC:

`root `[`#`]`emerge --ask media-video/vlc`

## [Usage]

### [Alternate interfaces]

VLC provides multiple interfaces in addition to the default GUI interface. There is an ncurses-based interface, and a HTTP interface that can be used for streaming or as a remote control. The VLC wiki has [a section dedicated to explaining the alternative interfaces](https://wiki.videolan.org/Documentation:Alternative_Interfaces).

#### [HTTP]

When connecting to the HTTP interface, make sure a password is set.

[Leave the user name field blank](https://wiki.videolan.org/Documentation:Modules/http_intf/#Access_control) when entering credentials on the web page.

### [Hotkeys]

VLC supports a host of hotkeys^[\[3\]](#cite_note-3)^ for more efficient operation. There is [an article](https://wiki.videolan.org/QtHotkeys/) on the VLC wiki detailing all available hotkeys for the Qt interface.

## [See also]

-   [MPlayer](https://wiki.gentoo.org/wiki/MPlayer "MPlayer") --- a powerful command-line media player
-   [Mpv](https://wiki.gentoo.org/wiki/Mpv "Mpv") --- a free and open source command-line media player.

## [External resources]

-   [https://www.hongkiat.com/blog/vlc-tips-tricks/](https://www.hongkiat.com/blog/vlc-tips-tricks/) - Tips and tricks for VLC.
-   [https://lifehacker.com/the-best-hidden-features-of-vlc-1654434241](https://lifehacker.com/the-best-hidden-features-of-vlc-1654434241) - A lifehacker article on hidden features in VLC.
-   [https://www.shortcutworld.com/en/win/vlc-media-player.html](https://www.shortcutworld.com/en/win/vlc-media-player.html) - A list of keyboard shortcuts for VLC. Highly useful if VLC is frequently used!

## [References]

1.  [[[↑](#cite_ref-1)] [[https://trac.videolan.org/vlc/ticket/35](https://trac.videolan.org/vlc/ticket/35)]]
2.  [[[↑](#cite_ref-2)] [[VideoLAN - VLC media player for Gentoo Linux](https://www.videolan.org/vlc/download-gentoo.html), [VideoLAN - VLC: Official site - Free multimedia solutions for all OS!](https://www.videolan.org/). Retrieved on February 17th, 2016.]]
3.  [[[↑](#cite_ref-3)] [[https://wiki.videolan.org/Documentation:Hotkeys/](https://wiki.videolan.org/Documentation:Hotkeys/)]]