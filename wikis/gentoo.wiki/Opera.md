[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Opera&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.opera.com/browsers/opera)

[[]][Package information](https://packages.gentoo.org/packages/www-client/opera)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Opera_(web_browser) "wikipedia:Opera (web browser)")

**Opera** is a multi-platform web browser.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Accept License]](#Accept_License)
    -   [[1.3] [Emerge]](#Emerge)
    -   [[1.4] [Using Opera as a media player]](#Using_Opera_as_a_media_player)
-   [[2] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [www-client/opera](https://packages.gentoo.org/packages/www-client/opera) [[]] [A fast and secure web browser]

  ----------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------
  [`+ffmpeg-chromium`](https://packages.gentoo.org/useflags/+ffmpeg-chromium)         Use Chromium FFmpeg fork (media-video/ffmpeg-chromium) rather than mainline FFmpeg (media-video/ffmpeg)
  [`+proprietary-codecs`](https://packages.gentoo.org/useflags/+proprietary-codecs)   Enable codecs for patent-encumbered audio and video formats.
  [`+suid`](https://packages.gentoo.org/useflags/+suid)                               Enable setuid root program(s)
  [`qt6`](https://packages.gentoo.org/useflags/qt6)                                   Add support for the Qt 6 application and UI framework
  ----------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-24 00:33] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Accept License]

In order to install Opera, the user needs to accept the \'OPERA-2018\' license agreement. A copy of the license can be found at \'/var/db/repos/gentoo/licenses/OPERA-2018\'. Read with:

`user `[`$`]`less /var/db/repos/gentoo/licenses/OPERA-2018`

And to agree:

`root `[`#`]`echo "www-client/opera OPERA-2018" >> /etc/portage/package.license`

### [Emerge]

Opera is distributed as only pre-built binaries. To install:

`root `[`#`]`emerge --ask www-client/opera`

### [Using Opera as a media player]

You can play media files in opera as a basic media player:

`user `[`$`]`opera ~/Videos/example.mp4`

## [See also]

-   [Vivaldi](https://wiki.gentoo.org/wiki/Vivaldi "Vivaldi") --- a browser for our friends.
-   [Chrome](https://wiki.gentoo.org/wiki/Chrome "Chrome") --- Google\'s proprietary (closed source) web browser.
-   [Chromium](https://wiki.gentoo.org/wiki/Chromium "Chromium") --- the open source browser that [Google Chrome](https://wiki.gentoo.org/wiki/Google_Chrome "Google Chrome") and many other browsers are based on.
-   [Firefox](https://wiki.gentoo.org/wiki/Firefox "Firefox") --- [open source](https://en.wikipedia.org/wiki/Open_source "wikipedia:Open source"), [multiplatform](https://en.wikipedia.org/wiki/Cross-platform_software "wikipedia:Cross-platform software"), [web browser](https://wiki.gentoo.org/wiki/Recommended_applications#Web_browsers "Recommended applications") developed by [Mozilla](https://en.wikipedia.org/wiki/Mozilla "wikipedia:Mozilla").
-   [Recommended applications](https://wiki.gentoo.org/wiki/Recommended_applications "Recommended applications") --- applications recommended for use in a graphical environment ([X11](https://wiki.gentoo.org/wiki/Xorg "Xorg"), [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland")) - [web browser section](https://wiki.gentoo.org/wiki/Recommended_applications#Web_browsers "Recommended applications").