**[] Deprecated article**\
\
This article is **deprecated (obsolete)**. Contents are [no longer relevant], and are intended for historical reference only!

Removed from Gentoo repositories and no 3rd party support.

\
TLDR: **Do not use this article!**

**Resources**

[[]][Home](https://www.openshot.org/)

[[]][Official documentation](https://openshot.org/files/libopenshot/)

[[]][Package information](https://packages.gentoo.org/packages/media-video/openshot)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Openshot "wikipedia:Openshot")

[[]][GitHub](https://github.com/OpenShot/openshot-qt)

[[]][Official project wiki](https://www.openshot.org/user-guide/)

**OpenShot** is an open source, cross-platform, video editor, written in Python and C++. It is dedicated to delivering high quality video editing and animation solutions.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Overview]](#Overview)
        -   [[1.3.1] [System Requirements]](#System_Requirements)
    -   [[1.4] [Video library libopenshot]](#Video_library_libopenshot)
        -   [[1.4.1] [Hardware Acceleration]](#Hardware_Acceleration)
        -   [[1.4.2] [API]](#API)
    -   [[1.5] [Audio library libopenshot-audio]](#Audio_library_libopenshot-audio)
    -   [[1.6] [openshot-qt]](#openshot-qt)
-   [[2] [Troubleshooting]](#Troubleshooting)

## [Installation]

### [USE flags]

Note that OpenShot uses [FFmpeg](https://wiki.gentoo.org/wiki/FFmpeg "FFmpeg") and [ALSA](https://wiki.gentoo.org/wiki/ALSA "ALSA") for audio output when previewing a video. If using [PipeWire](https://wiki.gentoo.org/wiki/PipeWire "PipeWire") as the sound server, ensure that it has been built with the [pipewire-alsa] `USE` flag.

### [Emerge]

`root `[`#`]`emerge --ask media-video/openshot`

### [Overview]

The OpenShot Video Editor consists of three main components:

-   C++ video library ([[[media-libs/libopenshot]](https://packages.gentoo.org/packages/media-libs/libopenshot)[]])
-   C++ audio library ([[[media-libs/libopenshot-audio]](https://packages.gentoo.org/packages/media-libs/libopenshot-audio)[]])
-   Python and PyQt user interface video editor ([openshot-qt](https://github.com/OpenShot/openshot-qt))

OpenShot has many features, and covering them all would go beyond the scope of this wiki. Nonetheless, a brief summary of some important features is provided here, although certainly not exhaustive. For further, more detailed functions and instructions, end users should consult the [OpenShot User Guide](https://www.openshot.org/user-guide/) as a helpful resource.

#### [System Requirements]

The process of video editing can place high demands on computational resources and requires a substantial amount of processing power to complete efficiently. To efficiently process videos using OpenShot, the following system requirements are recommended:^[\[1\]](#cite_note-:0-1)^

  ------------- ----------- --------- ------------------- -------- -------------------------
                CPU Cores   Threads   Turbo Clock speed   RAM      Disk space
  minimum       2           4         2.7 Ghz             4 GB     1 GB (install & useage)
  recommended   6+          6+        3.4+ Ghz            16+ GB   50+ GB (incl. media)
  ------------- ----------- --------- ------------------- -------- -------------------------

Furthermore, the system should have a CPU with 64-bit support and a 64-bit operating system installed.

Optional components are:

-   A [SSD](https://wiki.gentoo.org/wiki/SSD "SSD"), if utilizing disk-caching the add of additional 10 GB hard-disk space are required.^[\[1\]](#cite_note-:0-1)^
-   If enabling Hardware Acceleration (experimental), a GPU with the appropriate features listed in the Hardware Acceleration section should be used. Hardware Acceleration is optional and experimental.

### [Video library libopenshot]

The OpenShot video library [libopenshot](https://github.com/OpenShot/libopenshot) provides high quality video editing and animation with support for all [FFmpeg](https://wiki.gentoo.org/wiki/FFmpeg "FFmpeg") formats and Codecs (video, audio and images). This allows the rendering of videos in many codecs and formats.

The video library supports, but is not limited to, the following points:

-   Multi-Layer Compositing (the combining of multiple layers of visual elements into a single final image or video sequence)
-   Image overlays and watermarks
-   Audio Plug-ins and Drivers
-   Additional Video and Audio effects, color adjustment, chroma key, etc. \[\...\]
-   Animation Curves
-   Time Mapping, speed control features, time direction (reverse time etc.)
-   Multi-Processor Support
-   Frame accuracy, allows to step through the video frame by frame
-   Digital video effects, including brightness, gamma, hue, greyscale and many more
-   Clip manipulation (resizing, x,y-adjustment, alpha, scaling, trimming, snapping, rotation, cutting \... )
-   Powerful curve-based Key frame animations, with an unlimited number of keyframes ( quadratic bezier curves, linear, or constant)
-   Over 400 video transitions with real-time previews for fading

#### [Hardware Acceleration]

Experimental hardware acceleration is available for one or more GPUs, which can significantly speed up encoding and decoding if the hardware meets the corresponding power and feature requirements. However, hardware acceleration can also slow down performance if it is not set up properly, if the hardware does not have enough power, or if the necessary features are not supported by the hardware.

The supported features for hardware acceleration with OpenShot and instructions how to enable, disable and control them, can be found in the [Hardware Acceleration section of OpenShot](https://github.com/OpenShot/libopenshot/blob/develop/doc/HW-ACCEL.md). Some of the supported hardware acceleration features are [VAAPI](https://wiki.gentoo.org/wiki/VAAPI "VAAPI"), [VDPAU](https://wiki.gentoo.org/wiki/VDPAU "VDPAU") and NVDEC. To enable hardware acceleration in general, the [Gentoo Hardware Acceleration Guide](https://wiki.gentoo.org/wiki/Xorg/Hardware_3D_acceleration_guide "Xorg/Hardware 3D acceleration guide") provides detailed instructions for doing so.

#### [API]

A full C++ API to the libopenshot library is provided.^[\[2\]](#cite_note-:1-2)^ The following examples are a rough excerpt from the official documentation.^[\[2\]](#cite_note-:1-2)^

To use the API the header file must be included:

[CODE]

    #include "OpenShot.h"

The basic components of the API consist of four parts:^[\[2\]](#cite_note-:1-2)^

-   **Readers** are used to read multimedia files, streams and return openshot::Frame objects.
-   **Writers** are consuming openshot::Frame objects and are used to write / create video, audio, image files or streams.
-   **Timeline** allows many openshot::Clip objects to be trimmed, arranged, and layered together.
-   **Keyframes** are used to change values of properties over time on the timeline.

This example from the documentation shows, how to use a reader to access frames of a video file:^[\[2\]](#cite_note-:1-2)^

[CODE]

    // Create a reader for a video
    FFmpegReader r("MyAwesomeVideo.webm");
    r.Open(); // Open the reader

    // Get frame number 1 from the video
    std::shared_ptr<Frame> f = r.GetFrame(1);

    // Now that we have an openshot::Frame object, lets have some fun!
    f->Display(); // Display the frame on the screen
    f->DisplayWaveform(); // Display the audio waveform as an image
    f->Play(); // Play the audio through your speaker

    // Close the reader
    r.Close();

For further implementation details and use of the API, the [OpenShot documentation](https://openshot.org/files/libopenshot/) should be consulted.

### [Audio library libopenshot-audio]

The [libopenshot-audio](https://github.com/OpenShot/libopenshot-audio) provides high quality audio editing and playback. ^[\[3\]](#cite_note-:2-3)^

Some features, according to the GitHub project page are:^[\[3\]](#cite_note-:2-3)^

-   Audio Drivers (ASIO, WASAPI, DirectSound, CoreAudio, iPhone Audio, ALSA, JACK, and Android)
-   Audio Plug-ins (VST & AU)
-   Audio Mixing & Resampling
-   Audio Playback

### [openshot-qt]

[openshot-qt](https://github.com/OpenShot/openshot-qt) provides several features, some of them are:^[\[4\]](#cite_note-4)^

-   Unlimited tracks / layers
-   Advanced timeline control (drag & drop, zoom, snapping, panning, scroling \... )
-   3D animated titles and effects, powered by [Blender](https://wiki.gentoo.org/wiki/Blender "Blender"), with render properties
-   Desktop integration (drag and drop support)
-   Title templates, support of custom title creation for svg vector titles, sub-titles
-   2D animation support (image sequences)
-   SVG friendly, to create and include vector titles and credits
-   Scrolling motion picture credits
-   Widely supported export & import formats

## [Troubleshooting]

Bugs and Issues to the corresponding parts of OpenShot can easily reported and looked up on their related GitHub issue pages.

For libopenshot the reports can be found [here](https://github.com/OpenShot/libopenshot/issues). For problems related with libopenshot-audio the reports can be found [here](https://github.com/OpenShot/libopenshot-audio/issues).

For problems not related to a specific library, but rather to OpenShot itself, the issue section can be found [here](https://github.com/OpenShot/openshot-qt/issues).

1.  [[↑ ^[1.0](#cite_ref-:0_1-0)^ ^[1.1](#cite_ref-:0_1-1)^] [[https://www.openshot.org/user-guide/](https://www.openshot.org/user-guide/)]]
2.  [[↑ ^[2.0](#cite_ref-:1_2-0)^ ^[2.1](#cite_ref-:1_2-1)^ ^[2.2](#cite_ref-:1_2-2)^ ^[2.3](#cite_ref-:1_2-3)^] [[https://openshot.org/files/libopenshot/](https://openshot.org/files/libopenshot/)]]
3.  [[↑ ^[3.0](#cite_ref-:2_3-0)^ ^[3.1](#cite_ref-:2_3-1)^] [[https://github.com/OpenShot/libopenshot-audio](https://github.com/OpenShot/libopenshot-audio)]]
4.  [[[↑](#cite_ref-4)] [[https://github.com/OpenShot/openshot-qt](https://github.com/OpenShot/openshot-qt)]]