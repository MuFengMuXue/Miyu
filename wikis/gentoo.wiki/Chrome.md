[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Google_Chrome&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](http://www.google.com/chrome/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Google_Chrome "wikipedia:Google Chrome")

[[]][Blog](http://chrome.blogspot.com/)

[[]][Package information](https://packages.gentoo.org/packages/www-client/google-chrome)

**Chrome** is Google\'s proprietary (closed source) web browser. Much of the source code is released in parallel as [Chromium](https://wiki.gentoo.org/wiki/Chromium "Chromium"), however there are binary blobs present in Chrome including a Pepper-based version PPAPI of the Adobe Flash Player.^[\[1\]](#cite_note-1)^

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Accept License]](#Accept_License)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Screensharing with Pipewire]](#Screensharing_with_Pipewire)
    -   [[2.2] [Policies]](#Policies)
    -   [[2.3] [No emojis?]](#No_emojis.3F)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Last open pages not restored with info: \"Google Chrome didn\'t shut down correctly\"]](#Last_open_pages_not_restored_with_info:_.22Google_Chrome_didn.27t_shut_down_correctly.22)
        -   [[3.1.1] [Systemd]](#Systemd)
-   [[4] [See also]](#See_also)
-   [[5] [References]](#References)

## [Installation]

Currently there are several versions of Google Chrome available in the main Gentoo repository:

-   [[[www-client/google-chrome]](https://packages.gentoo.org/packages/www-client/google-chrome)[]] - A stable version of the web browser from Google.
-   [[[www-client/google-chrome-beta]](https://packages.gentoo.org/packages/www-client/google-chrome-beta)[]] - A beta version of the web browser of Google.
-   [[[www-client/google-chrome-unstable]](https://packages.gentoo.org/packages/www-client/google-chrome-unstable)[]] - An unstable version of the web browser from Google.

### [USE flags]

Each of the packages listed above contains the following USE flags:

### [USE flags for] [www-client/google-chrome](https://packages.gentoo.org/packages/www-client/google-chrome) [[]] [The web browser from Google]

  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`qt6`](https://packages.gentoo.org/useflags/qt6)           Add support for the Qt 6 application and UI framework
  [`selinux`](https://packages.gentoo.org/useflags/selinux)   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-24 00:33] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Accept License]

In order to install Google Chrome, the user needs to accept the \'google-chrome\' license agreement. A copy of the license can be found at \'/var/db/repos/gentoo/licenses/google-chrome\'. Read with:

`user `[`$`]`less /var/db/repos/gentoo/licenses/google-chrome`

And to agree:

`root `[`#`]`echo "www-client/google-chrome google-chrome" >> /etc/portage/package.license`

### [Emerge]

Select one of the Chrome packages to [emerge] above. Here the primary stable Chrome package will be installed:

`root `[`#`]`emerge --ask www-client/google-chrome`

## [Configuration]

Most configuration aspects can be found in the [Chromium article](https://wiki.gentoo.org/wiki/Chromium "Chromium"). Head over there for configuration information.

### [Screensharing with Pipewire]

Change \'WebRTC PipeWire support\' to \'Enabled\' in chrome://flags

### [Policies]

To configure custom policies in Chrome, the policy section in the Chromium article can be used: [Chromium#Policies](https://wiki.gentoo.org/wiki/Chromium#Policies "Chromium").

However, please note that the directory where Google Chrome looks for policies can be slightly different. According to the documentation the lookup path for installed policies should be: [/etc/opt/chrome/policies]^[\[2\]](#cite_note-2)^

### [][No emojis?]

Emerge [[[media-fonts/noto-emoji]](https://packages.gentoo.org/packages/media-fonts/noto-emoji)[]].

## [Troubleshooting]

### [][Last open pages not restored with info: \"Google Chrome didn\'t shut down correctly\"]

#### [Systemd]

1.  Create a service file with your favourite editor:

    ::: box-caption
    [FILE] **`/etc/systemd/system/kill-chrome-gracefully.service`**
    :::

    :::
        [Unit]
        Description=Help Chrome close gracefully
        DefaultDependencies=no
        Before=shutdown.target

        [Service]
        Type=oneshot
        User=root
        Group= root
        ExecStart=killall chrome --wait

        [Install]
        WantedBy=halt.target reboot.target shutdown.target
    :::
2.  Load it:

    :::: cmd-box


    `root `[`#`]`systemctl daemon-reload`


    ::::
3.  Enable it:

    :::: cmd-box


    `root `[`#`]`systemctl enable kill-chrome-gracefully.service`


    ::::

## [See also]

-   [Chromium](https://wiki.gentoo.org/wiki/Chromium "Chromium") --- the open source browser that [Google Chrome] and many other browsers are based on.
-   [Firefox](https://wiki.gentoo.org/wiki/Firefox "Firefox") --- [open source](https://en.wikipedia.org/wiki/Open_source "wikipedia:Open source"), [multiplatform](https://en.wikipedia.org/wiki/Cross-platform_software "wikipedia:Cross-platform software"), [web browser](https://wiki.gentoo.org/wiki/Recommended_applications#Web_browsers "Recommended applications") developed by [Mozilla](https://en.wikipedia.org/wiki/Mozilla "wikipedia:Mozilla").

## [References]

1.  [[[↑](#cite_ref-1)] [[http://www.chromium.org/nativeclient/getting-started/getting-started-background-and-basics#TOC-Pepper-Plugin-API-PPAPI-](http://www.chromium.org/nativeclient/getting-started/getting-started-background-and-basics#TOC-Pepper-Plugin-API-PPAPI-)]]
2.  [[[↑](#cite_ref-2)] [[https://support.google.com/chrome/a/answer/9027408?hl=en&ref_topic=9025817](https://support.google.com/chrome/a/answer/9027408?hl=en&ref_topic=9025817)]]