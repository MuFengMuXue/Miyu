Other languages:

[English] • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Snap/tr "Snap (8% translated)") • ‎[français](//wiki.manjaro.org/index.php?title=Snap/fr "Snap (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Snap/ru "Snap (100% translated)") • ‎[فارسی](//wiki.manjaro.org/index.php?title=Snap/fa "اسنپ (100% translated)")

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Installing Support for Snaps]](#Installing_Support_for_Snaps)
-   [[3] [Using Snaps]](#Using_Snaps)
    -   [[3.1] [Managing Snaps via Discover]](#Managing_Snaps_via_Discover)
    -   [[3.2] [Managing Snaps via Gnome Software]](#Managing_Snaps_via_Gnome_Software)
-   [[4] [Managing Snaps via the CLI]](#Managing_Snaps_via_the_CLI)
    -   [[4.1] [Finding and Installing Snaps]](#Finding_and_Installing_Snaps)
    -   [[4.2] [Displaying Detailed Snap Information]](#Displaying_Detailed_Snap_Information)
    -   [[4.3] [Getting a list of installed Snaps]](#Getting_a_list_of_installed_Snaps)
    -   [[4.4] [Removing Snaps]](#Removing_Snaps)
    -   [[4.5] [Removing Snap Support]](#Removing_Snap_Support)

### [Overview]

[Snaps](https://snapcraft.io/) are a distro independent method for packaging and distributing Linux software.

\
Using software distributed by Snap has a couple of distinct advantages:

-   Software that is not compatible with current system libraries will still work when packaged as a Snap
-   Snaps are automatically updated

\
There are some other considerations to be aware of:

-   Snaps do not always integrate with system themes
-   Snaps may need to install shared run-times which consume disk space

[![Snapcraft.png](/images/thumb/1/18/Snapcraft.png/250px-Snapcraft.png)](//wiki.manjaro.org/index.php?title=File:Snapcraft.png)

\

### [Installing Support for Snaps]

To use Snaps you to install and configure the Snap Daemon. It is available in the Manjaro repos as `snapd`, with `libpamac-snap-plugin` and can be installed with your favorite package manager or using the command

[user \$ ][ pamac install snapd libpamac-snap-plugin [COPY TO CLIPBOARD]]

\

Once installed, you need to enable snapd using the command:

[user \$ ][ sudo systemctl enable \--now snapd.socket [COPY TO CLIPBOARD]]

\

[user \$ ][ sudo systemctl enable \--now snapd.apparmor [COPY TO CLIPBOARD]]

\

If you also want support for classic snaps you can use the command:

[user \$ ][ sudo ln -s /var/lib/snapd/snap /snap [COPY TO CLIPBOARD]]

\

### [Using Snaps]

#### [Managing Snaps via Discover]

[![Kdediscover.png](/images/thumb/8/82/Kdediscover.png/400px-Kdediscover.png)](//wiki.manjaro.org/index.php?title=File:Kdediscover.png)

One way to manage your Snaps is with the application [Discover](https://userbase.kde.org/Discover) from the KDE project. You need a special version of Discover that can be found in the repos to manage snaps. This is now installed by default in some Manjaro editions that include Discover. If it isn\'t, you can install the package `discover-snap` with your favorite package manager or the command:

[user \$ ][ pamac install discover-snap [COPY TO CLIPBOARD]]

\

Once installed you can run **Discover** and you will be able to browse and install Snaps with a familiar store interface.

**tip**

------------------------------------------------------------------------

Discover can also install and update software from the Manjaro repos if you install the package `packagekit-qt5`

#### [Managing Snaps via Gnome Software]

[![Gnomesoftware.png](/images/thumb/a/a0/Gnomesoftware.png/400px-Gnomesoftware.png)](//wiki.manjaro.org/index.php?title=File:Gnomesoftware.png)

Another way to manage your Snaps is with the application [Gnome Software](https://wiki.gnome.org/Apps/Software) from the Gnome project. You need a special version of Gnome Software that has support for managing snaps. This now comes pre-installed in several Manjaro editions. If it isn\'t, you can install the package `gnome-software-snap` with your favorite package manager or the command:

[user \$ ][ pamac install gnome-software-snap [COPY TO CLIPBOARD]]

\

Once installed you can run **Software** and you will be able to browse and install Snaps with a familiar store interface.

**tip**

------------------------------------------------------------------------

Gnome Software can also install and update software from the Manjaro repos

### [Managing Snaps via the CLI]

#### [Finding and Installing Snaps]

You can use the command `snap search` to search for available Snaps. For example, if you wanted to install VLC here is what it might look like:

[user \$ ][ snap search vlc [COPY TO CLIPBOARD]]

\

    Name            Version                 Publisher  Notes  Summary
    vlc             3.0.6                   videolan✓  -      The ultimate media player
    dav1d           0.2.0-1-ge29cb9a        videolan✓  -      AV1 decoder from VideoLAN
    mjpg-streamer   2.0                     ogra       -      UVC webcam streaming tool
    audio-recorder  3.0.5+rev1432+pkg-7b07  brlin      -      A free audio-recorder for Linux

From this output we can see that VLC and some related applications are avialable. To install VLC, we would use the command

[user \$ ][ snap install vlc [COPY TO CLIPBOARD]]

\

This will install the application as well as any required run-times. Once the application is installed you should be able to run it from your menu as you would with any application.

#### [Displaying Detailed Snap Information]

You can get more details about a specific Snap using the command `snap info`. For example:

[user \$ ][ snap info vlc [COPY TO CLIPBOARD]]

\

```
name:      vlc
summary:   The ultimate media player
publisher: VideoLAN✓
contact:   https://www.videolan.org/support/
license:   GPL-2.0+
description: |
  VLC is the VideoLAN project's media player.

  Completely open source and privacy-friendly, it plays every multimedia file and streams.

  It notably plays MKV, MP4, MPEG, MPEG-2, MPEG-4, DivX, MOV, WMV, QuickTime, WebM, FLAC, MP3,
  Ogg/Vorbis files, BluRays, DVDs, VCDs, podcasts, and multimedia streams from various network
  sources. It supports subtitles, closed captions and is translated in numerous languages.
snap-id: RT9mcUhVsRYrDLG8qnvGiy26NKvv6Qkd
channels:
  stable:    3.0.6                      2019-01-10  (770) 212MB -
  candidate: 3.0.6                      2019-01-10  (770) 212MB -
  beta:      3.0.6-341-g18d7d08         2019-05-24 (1020) 212MB -
  edge:      4.0.0-dev-8011-gfdbf7317e0 2019-05-24 (1019) 335MB -
```

#### [Getting a list of installed Snaps]

To show a list of all the Snaps and run-times that are currently installed you can use the command:

[user \$ ][ snap list [COPY TO CLIPBOARD]]

\

\

#### [Removing Snaps]

You can remove Snaps with the command `snap remove`. For example:

[user \$ ][ snap remove vlc [COPY TO CLIPBOARD]]

\

\

#### [Removing Snap Support]

If you want to remove support for snaps from the system, you can do so with a few simple steps.

First, check if you have `gnome-software-snap` or `discover-snap` installed.

[user \$ ][ pamac list -i [COPY TO CLIPBOARD]]

\

If you find either of those packages, replace them with the non-snap versions. For example, if `gnome-software-snap` was on that list you can replace it with:

[user \$ ][ pamac install gnome-software [COPY TO CLIPBOARD]]

\

Next, remove snapd itself

[user \$ ][ pamac remove snapd [COPY TO CLIPBOARD]]

\

Optionally, you can also remove the remaining snapd files which would include any installed snaps.

[user \$ ][ sudo rm -r /var/lib/snapd [COPY TO CLIPBOARD]]

\