[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=V4l-utils&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Video "Project:Video")][Project](https://wiki.gentoo.org/wiki/Project:Video "Project:Video")

[[]][Home](https://www.linuxtv.org/)

[[]][Package information](https://packages.gentoo.org/packages/media-libs/libv4l)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Video4Linux "wikipedia:Video4Linux")

**v4l-utils** is a set of utilities for handling media devices contained in the Video4Linux library package which can be installed by enabling the [[[utils]](https://packages.gentoo.org/useflags/utils)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag").

** See also**\
See the [webcam](https://wiki.gentoo.org/wiki/Webcam "Webcam") article for instructions on how to use v4l-utils to set up a webcam for video capture.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Additional packages]](#Additional_packages)
        -   [[1.3.1] [gtk-v4l]](#gtk-v4l)
        -   [[1.3.2] [v4l-dvb-saa716x]](#v4l-dvb-saa716x)
        -   [[1.3.3] [v4l2loopback]](#v4l2loopback)
        -   [[1.3.4] [gst-plugins-v4l2]](#gst-plugins-v4l2)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
    -   [[2.2] [libcamera]](#libcamera)
-   [[3] [Removal]](#Removal)
    -   [[3.1] [Unmerge]](#Unmerge)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)
-   [[6] [References]](#References)

## [Installation]

** Note**\
[v4l-utils] was previously available as a separate package named **media-tv/v4l-utils**, but is now part of [[[media-libs/libv4l]](https://packages.gentoo.org/packages/media-libs/libv4l)[]]. Some older documentation around the web still refers to the old package.

### [USE flags]

### [USE flags for] [media-libs/libv4l](https://packages.gentoo.org/packages/media-libs/libv4l) [[]] [v4l-utils libraries and optional utilities]

  --------------------------------------------------------- ----------------------------------------------------------------------------------------------------------
  [`+utils`](https://packages.gentoo.org/useflags/+utils)   Build the v4l-utils collection of utilities
  [`bpf`](https://packages.gentoo.org/useflags/bpf)         Enable support for IR BPF decoders
  [`doc`](https://packages.gentoo.org/useflags/doc)         Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`dvb`](https://packages.gentoo.org/useflags/dvb)         Add support for DVB (Digital Video Broadcasting)
  [`jpeg`](https://packages.gentoo.org/useflags/jpeg)       Add JPEG image support
  [`qt6`](https://packages.gentoo.org/useflags/qt6)         Add support for the Qt 6 application and UI framework
  [`tracer`](https://packages.gentoo.org/useflags/tracer)   Build the v4l2-tracer tool and library
  --------------------------------------------------------- ----------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-19 09:51] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[media-libs/libv4l]](https://packages.gentoo.org/packages/media-libs/libv4l)[]]:

`root `[`#`]`emerge --ask media-libs/libv4l`

### [Additional packages]

#### [gtk-v4l]

The GTK+ package [[[media-tv/gtk-v4l]](https://packages.gentoo.org/packages/media-tv/gtk-v4l)[]] is available for controlling webcam v4l preferences.

### [USE flags for] [media-tv/gtk-v4l](https://packages.gentoo.org/packages/media-tv/gtk-v4l) [[]] [A GTK+ application for controlling V4L preferences of a web cam device]

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2021-11-25 15:42] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

#### [v4l-dvb-saa716x]

A driver for saa716x-based dvb cards is available at [[[media-tv/v4l-dvb-saa716x]](https://packages.gentoo.org/packages/media-tv/v4l-dvb-saa716x)[]].

### [USE flags for] [media-tv/v4l-dvb-saa716x](https://packages.gentoo.org/packages/media-tv/v4l-dvb-saa716x) [[]] [driver for saa716x based dvb cards like TT S2-6400 or Skystar 2 eXpress HD]

  ----------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------
  [`+strip`](https://packages.gentoo.org/useflags/+strip)                       Allow symbol stripping to be performed by the ebuild for special files
  [`dist-kernel`](https://packages.gentoo.org/useflags/dist-kernel)             Enable subslot rebuilds on Distribution Kernel upgrades
  [`modules-compress`](https://packages.gentoo.org/useflags/modules-compress)   Install compressed kernel modules (if kernel config enables module compression)
  [`modules-sign`](https://packages.gentoo.org/useflags/modules-sign)           Cryptographically sign installed kernel modules (requires CONFIG_MODULE_SIG=y in the kernel)
  ----------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2024-06-23 19:43] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

#### [v4l2loopback]

[[[media-video/v4l2loopback]](https://packages.gentoo.org/packages/media-video/v4l2loopback)[]] provides a v4l2 loopback device whose output is its own input.

### [USE flags for] [media-video/v4l2loopback](https://packages.gentoo.org/packages/media-video/v4l2loopback) [[]] [v4l2 loopback device whose output is its own input]

  ----------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------
  [`+strip`](https://packages.gentoo.org/useflags/+strip)                       Allow symbol stripping to be performed by the ebuild for special files
  [`dist-kernel`](https://packages.gentoo.org/useflags/dist-kernel)             Enable subslot rebuilds on Distribution Kernel upgrades
  [`examples`](https://packages.gentoo.org/useflags/examples)                   Install examples, usually source code
  [`modules-compress`](https://packages.gentoo.org/useflags/modules-compress)   Install compressed kernel modules (if kernel config enables module compression)
  [`modules-sign`](https://packages.gentoo.org/useflags/modules-sign)           Cryptographically sign installed kernel modules (requires CONFIG_MODULE_SIG=y in the kernel)
  ----------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-18 07:12] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

#### [gst-plugins-v4l2]

Finally, a gstreamer plugin package is available: [[[media-plugins/gst-plugins-v4l2]](https://packages.gentoo.org/packages/media-plugins/gst-plugins-v4l2)[]].

### [USE flags for] [media-plugins/gst-plugins-v4l2](https://packages.gentoo.org/packages/media-plugins/gst-plugins-v4l2) [[]] [plugin for gstreamer]

  ----------------------------------------------------- -------------------------------------------------------------------------------------------
  [`udev`](https://packages.gentoo.org/useflags/udev)   Enable virtual/udev integration (device discovery, power and storage device support, etc)
  ----------------------------------------------------- -------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-08 17:01] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

## [Usage]

### [Invocation]

`user `[`$`]`v4l2-ctl --help`

    General/Common options:
      --all              display all information available
      -C, --get-ctrl <ctrl>[,<ctrl>...]
                         get the value of the controls [VIDIOC_G_EXT_CTRLS]
      -c, --set-ctrl <ctrl>=<val>[,<ctrl>=<val>...]
                         set the value of the controls [VIDIOC_S_EXT_CTRLS]
      -D, --info         show driver info [VIDIOC_QUERYCAP]
      -d, --device <dev> use device <dev> instead of /dev/video0
                         if <dev> starts with a digit, then /dev/video<dev> is used
                         Otherwise if -z was specified earlier, then <dev> is the entity name
                         or interface ID (if prefixed with 0x) as found in the topology of the
                         media device with the bus info string as specified by the -z option.
      -e, --out-device <dev> use device <dev> for output streams instead of the
                         default device as set with --device
                         if <dev> starts with a digit, then /dev/video<dev> is used
                         Otherwise if -z was specified earlier, then <dev> is the entity name
                         or interface ID (if prefixed with 0x) as found in the topology of the
                         media device with the bus info string as specified by the -z option.
      -E, --export-device <dev> use device <dev> for exporting DMA buffers
                         if <dev> starts with a digit, then /dev/video<dev> is used
                         Otherwise if -z was specified earlier, then <dev> is the entity name
                         or interface ID (if prefixed with 0x) as found in the topology of the
                         media device with the bus info string as specified by the -z option.
      -z, --media-bus-info <bus-info>
                         find the media device with the given bus info string. If set, then
                         -d, -e and -E options can use the entity name or interface ID to refer
                         to the device nodes.
      -h, --help         display this help message
      --help-all         all options
      --help-io          input/output options
      --help-meta        metadata format options
      --help-misc        miscellaneous options
      --help-overlay     overlay format options
      --help-sdr         SDR format options
      --help-selection   crop/selection options
      --help-stds        standards and other video timings options
      --help-streaming   streaming options
      --help-subdev      sub-device options
      --help-tuner       tuner/modulator options
      --help-vbi         VBI format options
      --help-vidcap      video capture format options
      --help-vidout      vidout output format options
      --help-edid        edid handling options
      -k, --concise      be more concise if possible.
      -l, --list-ctrls   display all controls and their values [VIDIOC_QUERYCTRL]
      -L, --list-ctrls-menus
                display all controls and their menus [VIDIOC_QUERYMENU]
      -r, --subset <ctrl>[,<offset>,<size>]+
                         the subset of the N-dimensional array to get/set for control <ctrl>,
                         for every dimension an (<offset>, <size>) tuple is given.
      -w, --wrapper      use the libv4l2 wrapper library.
      --list-devices     list all v4l devices. If -z was given, then list just the
                         devices of the media device with the bus info string as
                         specified by the -z option.
      --log-status       log the board status in the kernel log [VIDIOC_LOG_STATUS]
      --get-priority     query the current access priority [VIDIOC_G_PRIORITY]
      --set-priority
                         set the new access priority [VIDIOC_S_PRIORITY]
                          is 1 (background), 2 (interactive) or 3 (record)
      --silent           only set the result code, do not print any messages
      --sleep <secs>     sleep <secs>, call QUERYCAP and close the file handle
      --verbose          turn on verbose ioctl status reporting

### [libcamera]

media-libs/libcamera is available in Gentoo repository.

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose media-libs/libv4l`

## [See also]

-   [darktable](https://wiki.gentoo.org/wiki/Darktable "Darktable") --- a photography workflow application and [RAW](https://en.wikipedia.org/wiki/Raw_image_format "wikipedia:Raw image format") developer.
-   [Droidcam](https://wiki.gentoo.org/wiki/Droidcam "Droidcam") --- a tool to use a smartphone\'s cameras as webcam on a computer
-   [Ffmpeg](https://wiki.gentoo.org/wiki/Ffmpeg "Ffmpeg") --- a cross platform, free, open source media encoder/decoder toolkit.
-   [gPhoto](https://wiki.gentoo.org/wiki/GPhoto "GPhoto")
-   [Jellyfin](https://wiki.gentoo.org/wiki/Jellyfin "Jellyfin") --- installation and management of the **jellyfin** media server
-   [Kodi](https://wiki.gentoo.org/wiki/Kodi "Kodi") --- an open source home theater application.
-   [Motion](https://wiki.gentoo.org/wiki/Motion "Motion")
-   [MythTV](https://wiki.gentoo.org/wiki/MythTV "MythTV") --- a powerful media center and video recording software system.
-   [OBS Studio](https://wiki.gentoo.org/wiki/OBS_Studio "OBS Studio") --- free software for video recording and live streaming.
-   [OpenShot](https://wiki.gentoo.org/wiki/OpenShot "OpenShot") --- an open source, cross-platform, video editor, written in Python and C++
-   [Streamlink](https://wiki.gentoo.org/wiki/Streamlink "Streamlink") --- a command-line utility that can extract video streams and pipe them into a video player.
-   [TV Tuner](https://wiki.gentoo.org/wiki/TV_Tuner "TV Tuner") --- configuring and using **television (TV) tuners** with Gentoo Linux
-   [Libcamera](https://wiki.gentoo.org/wiki/Libcamera "Libcamera") --- an open-source software library for image signal processors and embedded cameras.

## [External resources]

-   [Part I - Video for Linux API](https://www.kernel.org/doc/html/latest/userspace-api/media/v4l/v4l2.html) - the V4L2 API kernel specification.
-   [Video for Linux version 2 (V4L2) examples](https://github.com/kmdouglass/v4l2-examples)

## [References]