Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/Xrandr/es "Xrandr (100% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Xrandr/hu "Xrandr (100% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Xrandr/zh-cn "Xrandr (100% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Xrandr/ja "Xrandr (100% translated)")

**Resources**

[[]][Home](http://www.x.org/wiki/Projects/XRandR/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/RandR "wikipedia:RandR")

[[]][GitWeb](http://cgit.freedesktop.org/xorg/app/xrandr/)

The **RandR** (**R**esize **and** **R**otate)^[\[1\]](#cite_note-1)^ [X](https://wiki.gentoo.org/wiki/X "X") protocol extension and its CLI tool [xrandr] are used to manage screen resolutions, rotation and screens with multiply displays in X.

With version 1.4 support for multiply graphics cards was introduced, future versions (\>1.5) will also support monitors attached via USB (this will probably be merged with xorg-server 1.13 with support for [DisplayLink](https://wiki.gentoo.org/wiki/DisplayLink "DisplayLink")^[\[2\]](#cite_note-2)^).

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [GUI tools]](#GUI_tools)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Screen query]](#Screen_query)
    -   [[3.2] [Screen manipulation]](#Screen_manipulation)
    -   [[3.3] [Screen modes]](#Screen_modes)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)
-   [[6] [References]](#References)

## [Installation]

The [[[x11-apps/xrandr]](https://packages.gentoo.org/packages/x11-apps/xrandr)[]] package can be installed with the following command:

`root `[`#`]`emerge --ask x11-apps/xrandr`

** Note**\
This tool should automatically install with most [window managers](https://wiki.gentoo.org/wiki/Window_manager "Window manager") since it is used to manage the displays.

### [GUI tools]

There are several GUI tools to use [xrandr]. Here is a list of tools supported in Gentoo:

-   [[[x11-misc/arandr]](https://packages.gentoo.org/packages/x11-misc/arandr)[]] -- Another XRandR GUI (an independent GUI tool)
-   [[[lxde-base/lxrandr]](https://packages.gentoo.org/packages/lxde-base/lxrandr)[]] -- [LXDE](https://wiki.gentoo.org/wiki/LXDE "LXDE") GUI interface to RandR extension

## [Configuration]

A common way to execute [X](https://wiki.gentoo.org/wiki/Xorg "Xorg") related scripts is the use of [\~/.xinitrc] or [\~/.xprofile] files in a user\'s home directory. Put the line of code for [xrandr] in one of these files and it will be executed on every X startup to make settings permanent. For example, for [i3](https://wiki.gentoo.org/wiki/I3 "I3"):

[FILE] **`~/.xinitrc`**

    ~/.screenlayout/two-displays.sh &
    exec dbus-run-session i3

## [Usage]

[xrandr] uses the monitors *Extended Display Identification Data* ([EDID](https://en.wikipedia.org/wiki/Extended_Display_Identification_Data "wikipedia:Extended Display Identification Data")) to identify its capabilities. Faulty hardware might report wrong or bad EDIDs, in those cases it is still possible to use custom made setups by trial and error.

** Warning**\
Some graphic drivers like the binary [NVIDIA](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers "NVIDIA/nvidia-drivers") or [AMD](https://wiki.gentoo.org/wiki/AMDGPU-PRO "AMDGPU-PRO"), may not support [xrandr].

### [Screen query]

Running [xrandr] without any arguments will list all available display output interfaces and display devices along with their current state and capabilities:

`user `[`$`]`xrandr`

    Screen 0: minimum 320 x 200, current 1440 x 900, maximum 8192 x 8192
    VGA-1 disconnected (normal left inverted right x axis y axis)
    LVDS-1 connected 1440x900+0+0 (normal left inverted right x axis y axis) 304mm x 190mm
       1440x900       60.1*+
       1024x768       60.0
       800x600        60.3
       640x480        59.9

A [xrandr] query result contains all available interfaces labeled as `<interface_name>-<index>`. Each shows its connection status and the reported screen modes. The connected device\'s current mode is hinted by `*`, the preferred mode is hinted by `+`.

The *RandR* naming scheme for common display interfaces:

-   `LVDS` - [Laptop screen](https://en.wikipedia.org/wiki/FPD-Link "wikipedia:FPD-Link")
-   `HDMI` - [High-Definition Multimedia Interface](https://en.wikipedia.org/wiki/HDMI "wikipedia:HDMI")
-   `DVI` - [Digital Visual Interface](https://en.wikipedia.org/wiki/Digital_Visual_Interface "wikipedia:Digital Visual Interface")
-   `DP` - [DisplayPort](https://en.wikipedia.org/wiki/DisplayPort "wikipedia:DisplayPort")
-   `VGA` - [Video Graphics Array](https://en.wikipedia.org/wiki/Video_Graphics_Array "wikipedia:Video Graphics Array")
-   `TV` - [Composite Video](https://en.wikipedia.org/wiki/Composite_video "wikipedia:Composite video")
-   `S-video` - [S-Video](https://en.wikipedia.org/wiki/S-Video "wikipedia:S-Video")

### [Screen manipulation]

It is possible to manipulate output interfaces discovered via a [xrandr] query. Examples of common tasks:

Set the primary display if more than one device is attached:

`user `[`$`]`xrandr --output LVDS-1 --primary`

Extend to an external display attached on a known interface (*left-of*, *right-of*, *above*, *below*, *same-as*):

`user `[`$`]`xrandr --output DVI-1 --auto --left-of LVDS-1`

Rotate a display (*normal*, *left*, *right*, *inverted*):

`user `[`$`]`xrandr --output LVDS-1 --rotate left`

Turn off the device:

`user `[`$`]`xrandr --output LVDS-1 --off`

### [Screen modes]

A mode always consists of a resolution and a refresh-rate. With a [xrandr] query the hardware reports which modes are supported. It is possible to define own modes in case the hardware reports wrong information. To change the mode for an attached device:

`user `[`$`]`xrandr --output LVDS-1 --mode 1024x768`

It will use the highest refresh-rate in that mode, to also change the refresh-rate (in Hz):

`user `[`$`]`xrandr --output LVDS-1 --mode 1024x768 --rate 75`

The changes apply immediately and on the hardware listed above it might either produce an error or the screen goes blank, because 75Hz is not supported. This will last until the next session, using [Ctrl]+[Alt]+[Backspace] will terminate the session and restart [X](https://wiki.gentoo.org/wiki/X "X") in case something goes wrong.

To add a 75Hz mode, the tool [cvt] ([[[x11-libs/libxcvt]](https://packages.gentoo.org/packages/x11-libs/libxcvt)[]]) can be used to get a proper modeline:

`user `[`$`]`cvt 1024 768 75`

Everything after *Modeline* needs to be appended to the following command:

`user `[`$`]`xrandr --newmode "1024x768_75.00" 109.00 1280 1368 1496 1712 1024 1027 1034 1063 -hsync +vsync`

Running the query again should list the newly added mode.

** Note**\
Adding the mode manually does not make the display device work in the mode if it did not work before.

## [See also]

-   [Non root Xorg](https://wiki.gentoo.org/wiki/Non_root_Xorg "Non root Xorg") --- describes how an unprivileged user can run [Xorg](https://wiki.gentoo.org/wiki/Xorg "Xorg") without using suid.
-   [Xorg](https://wiki.gentoo.org/wiki/Xorg "Xorg") --- an open source implementation of the [X server](https://wiki.gentoo.org/wiki/X_server "X server").
-   [Xorg/Guide](https://wiki.gentoo.org/wiki/Xorg/Guide "Xorg/Guide") --- explains what Xorg is, how to install it, and the various configuration options.
-   [X server](https://wiki.gentoo.org/wiki/X_server "X server") --- the main component of the X Window system which abstracts the hardware and provides the foundation for most graphical user interfaces, like [desktop environments](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") or [window managers](https://wiki.gentoo.org/wiki/Window_manager "Window manager"), and their applications.

## [External resources]

-   [xrandr man page](http://linux.die.net/man/1/xrandr)

## [References]

1.  [[[↑](#cite_ref-1)] [[https://cgit.freedesktop.org/xorg/proto/randrproto/tree/randrproto.txt](https://cgit.freedesktop.org/xorg/proto/randrproto/tree/randrproto.txt)]]
2.  [[[↑](#cite_ref-2)] [[http://keithp.com/blogs/hotplug-displaylink/](http://keithp.com/blogs/hotplug-displaylink/)]]