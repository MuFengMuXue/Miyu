[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Libcamera&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Video "Project:Video")][Project](https://wiki.gentoo.org/wiki/Project:Video "Project:Video")

[[]][Home](https://libcamera.org/)

[[]][Official documentation](https://libcamera.org/introduction.html)

[[]][Package information](https://packages.gentoo.org/packages/media-libs/libcamera)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Libcamera "wikipedia:Libcamera")

[[]][Bugs (upstream)](https://gitlab.freedesktop.org/camera/libcamera/-/issues)

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/libcamera)

**libcamera** is an open-source software library for image signal processors and embedded cameras.. The developers describe libcamera as a continuation of V4L2^[\[1\]](#cite_note-1)^.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
    -   [[1.4] [Additional software]](#Additional_software)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Failed to open /dev/udmabuf: Permission denied]](#Failed_to_open_.2Fdev.2Fudmabuf:_Permission_denied)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)
-   [[7] [References]](#References)

## [Installation]

### [Kernel]

The libcamera software ISP requires the operating system to provide access to either the DMA heap or udmabuf devices. ^[\[2\]](#cite_note-2)^

[KERNEL] **Enable support for DMA buffers\>**

    Device Drivers --->
      DMABUF options --->
         DMA-BUF Userland Memory Heaps Search for <code>CONFIG_DMABUF_HEAPS</code> to find this item.

** Note**\
V4L2 may need to be configured too.

### [USE flags]

### [USE flags for] [media-libs/libcamera](https://packages.gentoo.org/packages/media-libs/libcamera) [[]] [Complex camera support library]

  --------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+udev`](https://packages.gentoo.org/useflags/+udev)           Enable virtual/udev integration (device discovery, power and storage device support, etc)
  [`drm`](https://packages.gentoo.org/useflags/drm)               Build with drm support for cam tool
  [`elfutils`](https://packages.gentoo.org/useflags/elfutils)     Build with improved debugging using dev-libs/elfutils
  [`gstreamer`](https://packages.gentoo.org/useflags/gstreamer)   Add support for media-libs/gstreamer (Streaming media)
  [`gui`](https://packages.gentoo.org/useflags/gui)               Build QCam extra tool
  [`jpeg`](https://packages.gentoo.org/useflags/jpeg)             Add JPEG image support
  [`openssl`](https://packages.gentoo.org/useflags/openssl)       Verify IPA modules signatures using dev-libs/openssl. Note:dev-libs/openssl is also required at build time to sign IPA modules.
  [`sdl`](https://packages.gentoo.org/useflags/sdl)               Build Cam extra tool with SDL sink support (requires USE=gui)
  [`test`](https://packages.gentoo.org/useflags/test)             Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`tiff`](https://packages.gentoo.org/useflags/tiff)             Add support for the TIFF image format
  [`tools`](https://packages.gentoo.org/useflags/tools)           Build extra tools (including cam, qcam and lc-compliance). Note: \'qcam\' requires also USE=\"gui\"
  [`trace`](https://packages.gentoo.org/useflags/trace)           Build with tracing capabilities
  [`unwind`](https://packages.gentoo.org/useflags/unwind)         Build with improved debugging using sys-libs/libunwind (has no effect if USE=elfutils is set)
  [`v4l`](https://packages.gentoo.org/useflags/v4l)               Enable support for video4linux (using linux-headers or userspace libv4l libraries)
  --------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-07 02:00] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask media-libs/libcamera`

### [Additional software]

Wireplumber offers support for capture devices using the libcamera stack via the Pipewire libcamera SPA (Single Plugin API) module. \"libcamera\" USE flag must be set for pipewire.

## [Usage]

### [Invocation]

`user `[`$`]`cam --help`

    Options:
      -c, --camera camera ...                               Specify which camera to operate on, by id or by index
      -h, --help                                            Display this help message
      -I, --info                                            Display information about stream(s)
      -l, --list                                            List all cameras
          --list-controls                                   List cameras controls
      -p, --list-properties                                 List cameras properties
      -m, --monitor                                         Monitor for hotplug and unplug camera events

    Options valid in the context of --camera:
      -C, --capture[=count]                                 Capture until interrupted by user or until <count> frames captured
      -o, --orientation orientation                         Desired image orientation (rot0, rot180, mirror, flip)
      -D, --display[=connector]                             Display viewfinder through DRM/KMS on specified connector
      -F, --file[=filename]                                 Write captured frames to disk
                                                            If the file name ends with a '/', it sets the directory in which
                                                            to write files, using the default file name. Otherwise it sets the
                                                            full file path and name. The first '#' character in the file name
                                                            is expanded to the camera index, stream name and frame sequence number.
                                                            If the file name ends with '.dng', then the frame will be written to
                                                            the output file(s) in DNG format.
                                                            If the file name ends with '.ppm', then the frame will be written to
                                                            the output file(s) in PPM format.
                                                            The default file name is 'frame-#.bin'.
      -S, --sdl                                             Display viewfinder through SDL
      -s, --stream key=value[,key=value,...] ...            Set configuration of a camera stream
              colorspace=string                             Color space
              height=integer                                Height in pixels
              pixelformat=string                            Pixel format name
              role=string                                   Role for the stream (viewfinder, video, still, raw)
              width=integer                                 Width in pixels
          --strict-formats                                  Do not allow requested stream format(s) to be adjusted
          --metadata                                        Print the metadata for completed requests
          --script script                                   Load a capture session configuration script from a file

`user `[`$`]`qcam --help`

    Options:
      -c, --camera camera                                   Specify which camera to operate on
      -h, --help                                            Display this help message
      -r, --renderer renderer                               Choose the renderer type  (default: qt)
      -s, --stream key=value[,key=value,...] ...            Set configuration of a camera stream
              colorspace=string                             Color space
              height=integer                                Height in pixels
              pixelformat=string                            Pixel format name
              role=string                                   Role for the stream (viewfinder, video, still, raw)
              width=integer                                 Width in pixels
      -v, --verbose                                         Print verbose log messages

## [Troubleshooting]

### [][Failed to open /dev/udmabuf: Permission denied]

This error indicates udmabuf special device provided by kernel is not accessible.

To fix this, add a custom udev rule:

[FILE] **`/etc/udev/rules.d/99-uaccess.rules`udmabuf udev rule**

    ACTION="add", SUBSYSTEM=="misc", KERNEL=="udmabuf", TAG+="uaccess"

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose media-libs/libcamera`

## [See also]

-   [Wireplumber](https://wiki.gentoo.org/wiki/Wireplumber "Wireplumber") --- a modular session / policy manager for [PipeWire](https://wiki.gentoo.org/wiki/PipeWire "PipeWire")
-   [Pipewire](https://wiki.gentoo.org/wiki/Pipewire "Pipewire") --- low-latency, graph-based, processing engine and server, for interfacing with audio and video devices.
-   [V4l-utils](https://wiki.gentoo.org/wiki/V4l-utils "V4l-utils") --- a set of utilities for handling media devices
-   [Webcam](https://wiki.gentoo.org/wiki/Webcam "Webcam") --- information on setting up and using a **webcam** on Gentoo using [v4l-utils](https://wiki.gentoo.org/wiki/V4l-utils "V4l-utils").

## [External resources]

-   [Introduction to libcamera](https://libcamera.org/introduction.html) --

## [References]

1.  [[[↑](#cite_ref-1)] [[\[1\]](https://libcamera.org/faq.html#how-is-libcamera-different-from-v4l2)FAQ - How is libcamera different from V4L2]]
2.  [[[↑](#cite_ref-2)] [[\[2\]](https://libcamera.org/faq.html#why-do-i-need-dma-heaps-or-udmabuf)FAQ - Why do I need DMA heaps or udmabuf]]