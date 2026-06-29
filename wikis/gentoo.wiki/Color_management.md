** Note**\
This article has been postponed for at least 2 years, because the author does not feel competent enough on this complicated topic but alas no one else seems intending to write one, so better something than nothing. Hence readers are recommended to take everything with two pinches of salt and some pepper. And please help improve it if you actually know this stuff.

Color management at its simplest definition is a computer technique for ensuring colors stay the same or at least as close as possible between devices. Colors may differ due to different physical characteristics between devices and even imperfections between displays of the same model and ageing of a display.

## Contents

-   [[1] [Basic theory behind computer color]](#Basic_theory_behind_computer_color)
    -   [[1.1] [Shortcomings of RGB]](#Shortcomings_of_RGB)
    -   [[1.2] [sRGB]](#sRGB)
-   [[2] [Color management systems (CMS)]](#Color_management_systems_.28CMS.29)
    -   [[2.1] [KDE (Plasma 5)]](#KDE_.28Plasma_5.29)
    -   [[2.2] [GNOME]](#GNOME)
    -   [[2.3] [Others]](#Others)
-   [[3] [Application support]](#Application_support)
    -   [[3.1] [GIMP]](#GIMP)
    -   [[3.2] [Firefox]](#Firefox)
    -   [[3.3] [mpv]](#mpv)
    -   [[3.4] [Darktable]](#Darktable)
-   [[4] [External resources]](#External_resources)
-   [[5] [TODO]](#TODO)
-   [[6] [References]](#References)

## [Basic theory behind computer color]

Despite the title of the section basic grasp of [RGB](https://en.wikipedia.org/wiki/RGB_color_model "wikipedia:RGB color model") is assumed until someone writes about the basics here.

### [Shortcomings of RGB]

More fundamentally RGB is a relative scale that most commonly has a mere 256 states per channel which is largely insufficient to represent the vividness of the real world. For better or worse our eyes see the world in a logarithmic fashion with greater distinction between darker tones. This can be exploited to avoid encoding many bright tones that seem roughly the same to humans. Nevertheless color management and using the correct gamma function are not the same thing although both are required for correct end results.

Another issue is the aforementioned relativity where the color space is defined by the display characteristics, meaning that #FF0000, #00FF00, #0000FF and by extension #FFFFFF are in fact different tones from device to device.

### [sRGB]

[sRGB](https://en.wikipedia.org/wiki/SRGB "wikipedia:SRGB") is Microsoft\'s attempt at fixing shortcomings of RGB, chiefly lack of absolute reference points and clarifies which gamma curve to use. On the down side, that curve itself is non-linear, adding complexity to proper sRGB support. Despite this sRGB is the de facto standard for RGB24/32 images and if it lacks a color profile then sRGB is the safest bet for files produced in the past 15 or so years.

## [][Color management systems (CMS)]

On Linux the two main solutions for display color management are Oyranos ([[[media-libs/oyranos]](https://packages.gentoo.org/packages/media-libs/oyranos)[]]) and [colord] ([[[x11-misc/colord]](https://packages.gentoo.org/packages/x11-misc/colord)[]]).

### [][KDE (Plasma 5)]

Enable the `colord` USE flag and rebuild the [world set](https://wiki.gentoo.org/wiki/World_set_(Portage) "World set (Portage)"). Emerge [[[kde-misc/colord-kde]](https://packages.gentoo.org/packages/kde-misc/colord-kde)[]] to provide interfaces and session daemon to [colord]. [[[media-gfx/displaycal-py3]](https://packages.gentoo.org/packages/media-gfx/displaycal-py3)[]] can be used to calibrate the devices instead of [GNOME](https://wiki.gentoo.org/wiki/Gnome "Gnome") Color Management as noted in [KDE](https://wiki.gentoo.org/wiki/KDE "KDE") Plasma application System Settings -\> Hardware -\> Color Corrections.

### [GNOME]

By default, GNOME uses [[[gnome-base/gnome-settings-daemon]](https://packages.gentoo.org/packages/gnome-base/gnome-settings-daemon)[]] to communicate with [colord]. Enable the `colord` USE flag and rebuild the [world set](https://wiki.gentoo.org/wiki/World_set_(Portage) "World set (Portage)"). For at least non-lite version of GNOME that should be all that is required.

### [Others]

Desktop environments like [LXDE](https://wiki.gentoo.org/wiki/LXDE "LXDE"), [Xfce](https://wiki.gentoo.org/wiki/Xfce "Xfce"), or [i3](https://wiki.gentoo.org/wiki/I3 "I3") do not feature native means of communication with [colord]. However, it is possible to use [xiccd] ([[[x11-misc/xiccd]](https://packages.gentoo.org/packages/x11-misc/xiccd)[]]) which acts as an independent alternative to GNOME/KDE daemons. The display profiles can be associated with devices using [colord]\'s [colormgr] tool.

First, import the display profile file and obtain its newly assigned `Profile ID`:

`user `[`$`]`colormgr import-profile display_profile.icc | grep "Profile ID"`

    Profile ID:    icc-d1c6fc06dd1a4fa72f5fe241aef755d7

Then get the `Device ID` of your device:

`user `[`$`]`colormgr get-devices | grep "Device ID"`

    Device ID:     xrandr-LVDS-1

Now it is possible to associate the profile with the device, followed by making the new profile default by:

`user `[`$`]`colormgr device-add-profile xrandr-LVDS-1 icc-d1c6fc06dd1a4fa72f5fe241aef755d7`

`user `[`$`]`colormgr device-make-profile-default xrandr-LVDS-1 icc-d1c6fc06dd1a4fa72f5fe241aef755d7`

Verify the association has been made correctly:

`user `[`$`]`colormgr device-get-default-profile xrandr-LVDS-1`

Finally, make sure both [colord] and [xiccd] are set to start automatically and reboot the system.

## [Application support]

### [GIMP]

In theory [GIMP](https://wiki.gentoo.org/wiki/GIMP "GIMP") has had color management for a bit longer than most applications, but if someone understands how to configure it to work properly with a CMS, go ahead, till then consider it broken.

### [Firefox]

Go to [about:config] and set `gfx.color_management.mode` to `1` from the default value of `2`. This will make [Firefox](https://wiki.gentoo.org/wiki/Firefox "Firefox") treat untagged images as sRGB which generally is what you want.

Support for ICC v4 profiles^[\[1\]](#cite_note-1)^ can be enabled by setting `gfx.color_management.enablev4` to `true`. The support can be verified by a dedicated [ICC\'s test page](https://www.color.org/version4html.xalter).

For best results also install a color management system or alternatively set the `gfx.color_management.display_profile` to the correct color profile file. Naturally, this will not work with two displays.

### [mpv]

When using [mpv](https://wiki.gentoo.org/wiki/Mpv "Mpv")\'s [OpenGL](https://en.wikipedia.org/wiki/Opengl "wikipedia:Opengl") presentation driver (not the legacy one inherited from MPlayer!) it\'s possible to configure it to always output sRGB which usually is already the case but could not be the case for nowadays more exotic or old content. Alternatively when built with [LittleCMS](https://en.wikipedia.org/wiki/Little_CMS "wikipedia:Little CMS") (`lcms` USE flag) support the same OpenGL presentation driver can also do full color management including with profile set in window properties but currently it will not tag the surface appropriately so care should be taken that the display color manager does not apply the display color profile again.

For detailed description see [the article on mpv](https://wiki.gentoo.org/wiki/Mpv#Example_user_mpv.conf "Mpv").

### [Darktable]

By default [Darktable](https://wiki.gentoo.org/wiki/Darktable "Darktable") uses the `_ICC_PROFILE` X atom^[\[2\]](#cite_note-2)^ to obtain the color profile. The `colord` USE flag enables additional support for [colord]. Darktable can be set to use one of those methods or both.

The package bundles a standalone binary utility [darktable-cmstest]^[\[3\]](#cite_note-3)^ which provides a convenient overview of system CMS\' configuration.

## [External resources]

-   [MinutePhysics video on non-linear gamma curves and why it\'s important to get them right (YouTube)](https://www.youtube.com/watch?v=LKnqECcg6Gw)
-   [Wikipedia article on gamma correction](https://en.wikipedia.org/wiki/Gamma_correction)
-   [Oyranos blog article on Linux color management](https://www.oyranos.org/2013/03/firefox-19-0-colour-management/)
-   [A blog post on Linux color management](https://encrypted.pcode.nl/blog/2012/01/29/color-management-on-linux/)
-   [Darkable - Display Profile guide](https://www.darktable.org/usermanual/en/special-topics/color-management/display-profile/)
-   [Greg Benz Photography - Web Browser Color Management tests](https://gregbenzphotography.com/photography-tips/how-to-setup-proper-color-management-in-a-web-browser/)

## [TODO]

-   Color calibration section or even an outright article as it\'s probably complicated enough on its own on Linux.
-   More applications such as \[\[Inkscape, Blender and other graphics processing tools.

## [References]

1.  [[[↑](#cite_ref-1)] [[Version 4 ICC Specification](https://www.color.org/v4spec.xalter), ICC. Retrieved on September 19, 2022]]
2.  [[[↑](#cite_ref-2)] [[ICC Profiles In X Specification](http://www.burtonini.com/computing/x-icc-profiles-spec-0.2.html) (20 Feb 2007, Ross Burton)]]
3.  [[[↑](#cite_ref-3)] [[darktable 3.4 user manual - darktable-cmstest](https://www.darktable.org/usermanual/en/special-topics/program-invocation/darktable-cmstest/)]]