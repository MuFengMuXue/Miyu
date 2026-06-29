[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Vivaldi&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://vivaldi.com)

[[]][Package information](https://packages.gentoo.org/packages/www-client/vivaldi)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Vivaldi_(web_browser) "wikipedia:Vivaldi (web browser)")

**Vivaldi** is a browser for our friends.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Types]](#Types)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [File selection dialog does not appear]](#File_selection_dialog_does_not_appear)
    -   [[3.2] [DRM-protected content not playing]](#DRM-protected_content_not_playing)
-   [[4] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [www-client/vivaldi](https://packages.gentoo.org/packages/www-client/vivaldi) [[]] [A browser for our friends]

  --------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------
  [`ffmpeg-chromium`](https://packages.gentoo.org/useflags/ffmpeg-chromium)         Use Chromium FFmpeg fork (media-video/ffmpeg-chromium) rather than mainline FFmpeg (media-video/ffmpeg)
  [`gtk`](https://packages.gentoo.org/useflags/gtk)                                 Add support for x11-libs/gtk+ (The GIMP Toolkit)
  [`proprietary-codecs`](https://packages.gentoo.org/useflags/proprietary-codecs)   Use system FFmpeg library to support patent-encumbered media codecs
  [`qt6`](https://packages.gentoo.org/useflags/qt6)                                 Add support for the Qt 6 application and UI framework
  [`widevine`](https://packages.gentoo.org/useflags/widevine)                       Unsupported closed-source DRM capability (required by Netflix VOD)
  --------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-24 00:33] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Vivaldi is distributed as only pre-built binaries. To install:

`root `[`#`]`emerge --ask www-client/vivaldi`

Alternatively, there is Vivaldi-Snapshot, the work-in-progress build of the browser. Vivaldi-Snapshot is distributed as only pre-built binaries. To install:

`root `[`#`]`emerge --ask www-client/vivaldi-snapshot`

## [Types]

Currently there are 2 packages for Vivaldi: [[[www-client/vivaldi]](https://packages.gentoo.org/packages/www-client/vivaldi)[]] and [[[www-client/vivaldi-snapshot]](https://packages.gentoo.org/packages/www-client/vivaldi-snapshot)[]]

vivaldi-snapshot is a preview version of Vivaldi

## [Troubleshooting]

### [File selection dialog does not appear]

Some [DEs](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment")/[WMs](https://wiki.gentoo.org/wiki/Window_manager "Window manager") don\'t provide an [xdg-desktop-portal](https://wiki.gentoo.org/wiki/Xdg-desktop-portal "Xdg-desktop-portal") by default ([[[bug #934819]](https://bugs.gentoo.org/show_bug.cgi?id=934819)[]]). This can be solved by running:

`root `[`#`]`emerge --ask sys-apps/xdg-desktop-portal-gtk`

### [DRM-protected content not playing]

Ensure the `proprietary-codecs` and `widevine` USE flags are enabled for Vivaldi, and that the `vivaldi:components` page lists \"Widevine Content Decryption Module\" and is up-to-date. To enable Widevine, in Settings, search for `widevine`, which should bring up the \"Plugins\" section and the \"Enable Widevine Plugin\" checkbox.

## [See also]

-   [Chrome](https://wiki.gentoo.org/wiki/Chrome "Chrome") --- Google\'s proprietary (closed source) web browser.
-   [Chromium](https://wiki.gentoo.org/wiki/Chromium "Chromium") --- the open source browser that [Google Chrome](https://wiki.gentoo.org/wiki/Google_Chrome "Google Chrome") and many other browsers are based on.
-   [Firefox](https://wiki.gentoo.org/wiki/Firefox "Firefox") --- [open source](https://en.wikipedia.org/wiki/Open_source "wikipedia:Open source"), [multiplatform](https://en.wikipedia.org/wiki/Cross-platform_software "wikipedia:Cross-platform software"), [web browser](https://wiki.gentoo.org/wiki/Recommended_applications#Web_browsers "Recommended applications") developed by [Mozilla](https://en.wikipedia.org/wiki/Mozilla "wikipedia:Mozilla").
-   [Recommended applications](https://wiki.gentoo.org/wiki/Recommended_applications "Recommended applications") --- applications recommended for use in a graphical environment ([X11](https://wiki.gentoo.org/wiki/Xorg "Xorg"), [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland")) - [web browser section](https://wiki.gentoo.org/wiki/Recommended_applications#Web_browsers "Recommended applications").