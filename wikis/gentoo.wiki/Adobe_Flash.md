**[] Archived article**\
\

This article is **archived (obsolete)**. Contents are surely incorrect for current usage, and are intended for historical reference only.

\
TLDR: **Do not use this article!**

\

**Resources**

[[]][Home](https://www.adobe.com/products/flashplayer.html)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Adobe_Flash "wikipedia:Adobe Flash")

** Warning**\
As of December 31, 2020, Adobe Flash is end of life. It has been removed from gentoo.git in [[[bug #754192]](https://bugs.gentoo.org/show_bug.cgi?id=754192)[]]. The Gentoo project recommends avoiding the use of Adobe Flash. Review possible [alternatives](#Alternatives) below.

## [Alternatives]

Alternatives to Adobe Flash may be available.

An alternative to using Adobe Flash Player when only playing video streams from YouTube, Vimeo, Twitch, Internet TV stream, etc., is to install [[[media-video/mpv]](https://packages.gentoo.org/packages/media-video/mpv)[]] with the `lua` USE flag, and [[[media-video/ffmpeg]](https://packages.gentoo.org/packages/media-video/ffmpeg)[]] or [[[media-video/libav]](https://packages.gentoo.org/packages/media-video/libav)[]] with the `openssl` USE flag. The `lua` USE flag allows [[[net-misc/youtube-dl]](https://packages.gentoo.org/packages/net-misc/youtube-dl)[]] to work in mpv, and the `openssl` USE flag allows FFmpeg/Libav to open [https://] streams. Next, install the [Open-with Firefox add-on](https://addons.mozilla.org/en-US/firefox/addon/open-with/) and configure it in the following way:

-   Open [about:openwith], select [Add\...]
-   In the dialog select a video streaming capable player (e.g. [/usr/bin/mpv]).
-   (Optional step) Choose how to display the dialogs using the left panel of Open-with add-on.
-   Right click on links or visit pages containing videos. If the site is supported, the player will be open as expected.

The same procedure can be used to associate other video downloaders such as [[[net-misc/youtube-dl]](https://packages.gentoo.org/packages/net-misc/youtube-dl)[]].

## [External resources]

-   [Adobe Flash Player on Arch Linux Wiki](https://wiki.archlinux.org/index.php/Browser_plugins#Adobe_Flash_Player)