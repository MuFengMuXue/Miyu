[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Webcam&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Webcam "wikipedia:Webcam")

[[]]This article has some todo items:\

-   Check kernel options

This article will provide information on setting up and using a **webcam** on Gentoo using [v4l-utils](https://wiki.gentoo.org/wiki/V4l-utils "V4l-utils").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
    -   [[1.4] [Additional software]](#Additional_software)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Configuration GUI and settings test]](#Configuration_GUI_and_settings_test)
    -   [[2.2] [Get settings from video device]](#Get_settings_from_video_device)
    -   [[2.3] [Settings example]](#Settings_example)
        -   [[2.3.1] [Check settings]](#Check_settings)
        -   [[2.3.2] [Make options persistent]](#Make_options_persistent)
-   [[3] [See also]](#See_also)

## [Installation]

### [Kernel]

[KERNEL] **Enable Webcam support**

    Device Drivers --->
      LED Support --->
         LED Class Support Search for <code>CONFIG_LEDS_CLASS</code> to find this item.
        <*> LED Flash Class Support Search for <code>CONFIG_LEDS_CLASS_FLASH</code> to find this item.
      <*> Multimedia support Search for <code>CONFIG_MEDIA_SUPPORT</code> to find this item. --->
        [*] Filter media drivers Search for <code>CONFIG_MEDIA_SUPPORT_FILTER</code> to find this item.
        Media device types --->
          [*] Cameras and video grabbers Search for <code>CONFIG_CAMERA_SUPPORT</code> to find this item.
        Video4Linux options --->
          <M> V4L2 flash API for LED flash class devices Search for <code>CONFIG_V4L2_FLASH_LED_CLASS</code> to find this item.
        Media drivers  --->
          [*] Media USB Adapters Search for <code>CONFIG_MEDIA_USB_SUPPORT</code> to find this item. --->
            <M> USB Video Class (UVC) Search for <code>CONFIG_USB_VIDEO_CLASS</code> to find this item.
            [*] UVC input events device support Search for <code>CONFIG_USB_VIDEO_CLASS_INPUT_EVDEV</code> to find this item.

** Note**\
To enable sound on webcams equipped with a microphone, separate options, such as \"USB Audio/MIDI driver\" (CONFIG_SND_USB_AUDIO), may need to be configured.

### [USE flags]

Recommended USE flags for v4l include: `qt6` - at least `qt6` will be needed to follow on with this article.

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

### [Additional software]

There are several webcam viewer applications in the [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository"), a few examples are:

  -------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------
  Name                                                     Package                                                                                                                                                                                                                                                                                                                                                                              Description
  Cheese                                                   [[[media-video/cheese]](https://packages.gentoo.org/packages/media-video/cheese)[]]         Cheesy program to take pictures and videos from a webcam.
  guvcview                                                 [[[media-video/guvcview]](https://packages.gentoo.org/packages/media-video/guvcview)[]]   Simple Qt6 or GTK+3 interface for capturing and viewing video from v4l2 devices.
  kamoso                                                   [[[kde-apps/kamoso]](https://packages.gentoo.org/packages/kde-apps/kamoso)[]]                  Application to take pictures and videos from a webcam, by KDE.
  [Motion](https://wiki.gentoo.org/wiki/Motion "Motion")   [[[media-video/motion]](https://packages.gentoo.org/packages/media-video/motion)[]]         Software motion detector.
  -------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------

Media players like [VLC](https://wiki.gentoo.org/wiki/VLC "VLC") or [mpv](https://wiki.gentoo.org/wiki/Mpv "Mpv") may be used to view or sometimes record video from a webcam. Most webcams are recognized and accessible through a device in [/dev/video0], wherein the number in the name indicates which webcam it is, in this case the first one. Thus reading from the [/dev/video0] device with the video player of your choice, will give you the image of your webcam.

See [media-video](https://packages.gentoo.org/categories/media-video) for more video software.

## [Configuration]

v4l-utils is used here to check/set the camera\'s preferences.

### [Configuration GUI and settings test]

Launch the v4l GUI:

`user `[`$`]`qv4l2`

** Note**\
The availability of [qv4l2] depends on the [[[qt6]](https://packages.gentoo.org/useflags/qt6)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] flag for the [[[media-tv/v4l-utils]](https://packages.gentoo.org/packages/media-tv/v4l-utils)[]] package.

### [Get settings from video device]

Example of using the video4linux control application to display supported video formats:

`user `[`$`]`v4l2-ctl --list-formats-ext`

### [Settings example]

Some cheap USB cameras (like integrated models in ThinkPad laptops) default to a 640x480 resolution even when they are capable of higher resolutions. It is possible to override this with [v4l2-ctl]:

`user `[`$`]`v4l2-ctl --set-parm=30 --set-fmt-video=width=1280,height=720,pixelformat=MJPG --device /dev/video0`

**Explanation**

`--set-parm` = Framerate (integer)

`--set-fmt-video` = Resolution + Compression

#### [Check settings]

Launch the v4l2 video capture viewer to test if the settings are working:

`user `[`$`]`qvidcap`

** Note**\
The availability of [qvidcap] depends on the [[[qt6]](https://packages.gentoo.org/useflags/qt6)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] flag for the [[[media-tv/v4l-utils]](https://packages.gentoo.org/packages/media-tv/v4l-utils)[]] package.

#### [Make options persistent]

Getting device info:

`root `[`#`]`lsusb | grep Cam`

    Bus 003 Device 007: ID 5986:0268 Acer, Inc SunplusIT INC. Integrated Camera

Creating a rule:

[FILE] **`/etc/udev/rules.d/99-v4linux.rules`Example udev rule**

    SUBSYSTEM=="video4linux", SUBSYSTEMS=="usb", ATTRS=="5986", ATTRS=="0268", PROGRAM="/usr/bin/v4l2-ctl --set-parm=30 --set-fmt-video=width=1280,height=720,pixelformat=MJPG --device /dev/%k"

## [See also]

-   [v4l-utils](https://wiki.gentoo.org/wiki/V4l-utils "V4l-utils") --- a set of utilities for handling media devices