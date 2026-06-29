[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**Resources**

[[]][Home](https://www.rocketleague.com)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Rocket_League "wikipedia:Rocket League")

Rocket League is a popular cross-platform \"car soccer\" game published by Psyonix, now owned by Epic Games. It can be played on PC using [Steam](https://wiki.gentoo.org/wiki/Steam "Steam").

While Rocket League is officially not supported on Linux ^[\[1\]](#cite_note-march-update-1)^, it can be played using various compatibility tools.

\

## Contents

-   [[1] [Running on Steam with Proton]](#Running_on_Steam_with_Proton)
    -   [[1.1] [Proton customizations]](#Proton_customizations)
-   [[2] [Running on Steam with PlayOnLinux]](#Running_on_Steam_with_PlayOnLinux)
    -   [[2.1] [Install PlayOnLinux]](#Install_PlayOnLinux)
    -   [[2.2] [Install Steam within PlayOnLinux]](#Install_Steam_within_PlayOnLinux)
    -   [[2.3] [Final tweaks]](#Final_tweaks)
-   [[3] [Historical notes]](#Historical_notes)
-   [[4] [External resources]](#External_resources)
-   [[5] [References]](#References)

## [Running on Steam with Proton]

For users who have purchased Rocket League through Steam and have the Steam client for Linux installed, the game can be played with Proton, which is Valve\'s compatibility tool for Linux (based on [Wine](https://wiki.gentoo.org/wiki/Wine "Wine")).

You will need [[[media-libs/mesa]](https://packages.gentoo.org/packages/media-libs/mesa)[]] to be installed with [Vulkan](https://wiki.gentoo.org/wiki/Vulkan "Vulkan") support.

[FILE] **`/etc/portage/package.use`**

    media-libs/mesa vulkan

Then once you have the game installed in Steam, open the \"Properties\" dialog for the game either by right-clicking on Rocket League in the game list or by selecting it and clicking the settings icon. Click \"Set Launch Options\...\" and in the dialog that pops up, type in

[CODE] **Set Launch Options\...**

    %command% -dx11

Still in the \"Properties\" dialog, check the box \"Force the use of a specific Steam Play compatibility tool\", and in the menu, choose `Proton 5.0-10` (or a different version of Proton, if you want to give it a try). Then you should be able to start Rocket League as normal.

### [Proton customizations]

ProtonDB has [a page on Rocket League](https://www.protondb.com/app/252950) in which users can suggest various tweaks they found useful. Several reports suggest that using [GloriousEggroll\'s custom version of Proton](https://github.com/GloriousEggroll/proton-ge-custom) gives a better experience.

## [Running on Steam with PlayOnLinux]

** Warning**\
The original version of these instructions was written in August 2016. It\'s not known whether they still work as of September 2020. If you can confirm one way or another, please edit accordingly or drop a note on the discussion page.

This section of the guide reflects one user\'s experience playing Rocket League using Steam and PlayOnLinux.

This section is based on kernel 4.7.2 and the `default/linux/amd64/13.0/desktop` profile, with an i7 2600k processor and an Nvidia GTX 980 video card using `=x11-drivers/nvidia-drivers-370.23`.

### [Install PlayOnLinux]

PlayOnLinux was [removed from the Portage tree](https://gitweb.gentoo.org/repo/gentoo.git/commit/app-emulation/playonlinux?id=3831172264494f42d621e760593f4d066900d922) in July 2020 due to its dependency on Python 2. You will need to either install it outside of Portage, or acquire old ebuilds for it and its dependencies (possibly through an overlay).

### [Install Steam within PlayOnLinux]

1.  Open PlayOnLinux
2.  Click Install
3.  Search for Steam, highlight Steam, and click install
4.  Follow all directions to complete the installation of Steam
5.  After Steam has been installed you should see the icon in the main PlayOnLinux window. Highlight this icon and click \"Configure\"
6.  Optionally update to the newest Wine version as PlayOnLinux will install an older version, but you can skip this if you want to
    1.  Click the plus button next to\"Wine version\".
    2.  Under \"Available Wine versions:\" highlight the newest staging version of Wine and click the greater than arrow (\>) to install it. These directions were written using 1.9.17-staging.
    3.  Now that this version is actually installed, be sure to select this new version from the dropdown next to \"Wine version\".
7.  Click on the \"Install components tab\"
8.  Install the following:
    1.  `directx9`
    2.  `d3dx9_43`
    3.  `vcrun2008`
    4.  `vcrun2010`
    5.  `vcrun2012`
9.  Click the \"Display\" tab
10. Set the \"Video memory size\" correctly depending on your video card, e.g. 4096

### [Final tweaks]

At this point you may wish to test Rocket League to see if it will open for you. If not, you may need the following 32 bit libraries: `lib32-gnutls`, `lib32-alsa-lib`, `lib32-alsa-plugins`, `lib32-libxml2`, and `lib32-libldap` ^[\[2\]](#cite_note-2)^. The game might work without 32 bit alsa-plugins. To mirror the suggested setup, enable 32-bit mode for the following libraries:

[FILE] **`/etc/portage/package.use`**

    net-libs/gnutls abi_x86_32 pkcs11
    media-libs/alsa-lib abi_x86_32
    dev-libs/libxml2 abi_x86_32
    net-nds/openldap abi_x86_32

The `pkcs11` `USE` flag to `gnutls` may be required to play online, otherwise Rocket League might not find any servers. Feel free to test on your own system.

Adding your user account to the `input` group will probably be necessary to use controllers.

`root `[`#`]`usermod -a -G input username`

## [Historical notes]

On September 23, 2020, Rocket League was removed from the Steam store and added to the Epic Games store^[\[3\]](#cite_note-3)^, although people who have bought the game on Steam will continue to be able to use the Steam version and receive future updates ^[\[4\]](#cite_note-4)^.

A native Linux port of Rocket League was available on Steam from September 8, 2016 ^[\[5\]](#cite_note-5)^, through March 10, 2020 ^[\[1\]](#cite_note-march-update-1)^. People who installed the Linux port during that time can still use it, but it doesn\'t support online play or other features that require connecting to a server, and it doesn\'t receive updates.

## [External resources]

1.  [https://www.reddit.com/r/Gentoo/comments/4z7zek/rocket_league_on_gentoo/](https://www.reddit.com/r/Gentoo/comments/4z7zek/rocket_league_on_gentoo/) gives more information on running Rocket League using PlayOnLinux
2.  [[[bug #674206]](https://bugs.gentoo.org/show_bug.cgi?id=674206)[]] concerns adding Phoenicis, the new name for version 5 of PlayOnLinux, to the Portage tree

## [References]

1.  [[↑ ^[1.0](#cite_ref-march-update_1-0)^ ^[1.1](#cite_ref-march-update_1-1)^] [Max Parker. [March Update Releases March 10](https://www.rocketleague.com/news/march-update-releases-march-10/), [rocketleague.com](https://www.rocketleague.com), March 6, 2020. Retrieved September 2, 2020.]]
2.  [[[↑](#cite_ref-2)] [Daerandin. [Rocket League Guide](https://www.gamersonlinux.com/forum/threads/rocket-league-guide.1543/), [Gamers on Linux](https://www.gamersonlinux.com/forum/), Aug 21, 2015. Retrieved September 2, 2020.]]
3.  [[[↑](#cite_ref-3)] [Matthew Reynolds. [Rocket League free-to-play release time, plus Season 1 update detailed](https://www.eurogamer.net/articles/rocket-league-free-to-play-season-1-release-update-7049), September 23, 202. Retrieved July 4, 2021.]]
4.  [[[↑](#cite_ref-4)] [Psyonix Team. [Rocket League Going Free To Play This Summer](https://www.rocketleague.com/news/rocket-league-going-free-to-play-this-summer/), [rocketleague.com](https://www.rocketleague.com), July 21, 2020. Retrieved September 2, 2020.]]
5.  [[[↑](#cite_ref-5)] [Joey Sneddon. [Rocket League Launches on Linux This Week](https://www.omgubuntu.co.uk/2016/09/rocket-league-linux-download-rumble-update-september), [OMG! Ubuntu!](https://www.omgubuntu.co.uk/), September 9, 2016. Retrieved September 2, 2020.]]