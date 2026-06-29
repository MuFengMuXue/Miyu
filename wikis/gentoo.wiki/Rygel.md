[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**Resources**

[[]][Home](https://wiki.gnome.org/Projects/Rygel)

**Rygel** is a home media solution (UPnP AV MediaServer).

## Contents

-   [[1] [Setup using an init script]](#Setup_using_an_init_script)
    -   [[1.1] [Setup Rygel upnp/dlna media server]](#Setup_Rygel_upnp.2Fdlna_media_server)
    -   [[1.2] [Installation]](#Installation)
        -   [[1.2.1] [USE flags]](#USE_flags)
        -   [[1.2.2] [Emerge]](#Emerge)
    -   [[1.3] [create user and group]](#create_user_and_group)
    -   [[1.4] [copy files]](#copy_files)
    -   [[1.5] [Modify config file]](#Modify_config_file)
-   [[2] [Setup using shell-session]](#Setup_using_shell-session)

## [Setup using an init script]

** Important**\
This setup is unsupported by Gentoo, do ***not*** report bugs or complain to the maintainer if things do not work.

### [][Setup Rygel upnp/dlna media server]

For this howto we can not (yet) use the tracker and dbus interface. The reason is that we start rygel as a daemon with an init script. This is means we do not have a dbus user session and thus can not use tracker and have to rely on the media export plugin\'s ability to scan the directories.

This howto is split over the following sections:

-   USE flags and merging rygel
-   create user and group
-   copy/create the files
-   The init script + config file
-   Modify the config file

### [Installation]

#### [USE flags]

### [USE flags for] [net-misc/rygel](https://packages.gentoo.org/packages/net-misc/rygel) [[]] [Rygel is an open source UPnP/DLNA MediaServer]

  ------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+introspection`](https://packages.gentoo.org/useflags/+introspection)   Add support for GObject based introspection
  [`+sqlite`](https://packages.gentoo.org/useflags/+sqlite)                 Add support for sqlite - embedded sql database
  [`gtk`](https://packages.gentoo.org/useflags/gtk)                         Add support for x11-libs/gtk+ (The GIMP Toolkit)
  [`gtk-doc`](https://packages.gentoo.org/useflags/gtk-doc)                 Build and install gtk-doc based developer documentation for dev-util/devhelp, IDE and offline use
  [`test`](https://packages.gentoo.org/useflags/test)                       Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`tracker`](https://packages.gentoo.org/useflags/tracker)                 Install dependencies for the tracker plugin
  [`transcode`](https://packages.gentoo.org/useflags/transcode)             Install dependencies for transcoding support
  ------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-24 17:14] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

** Note**\
Enabling the `tracker` USE flag brings in most of X and GNOME. No D-Bus session is available so there is no way to connect to tracker.

#### [Emerge]

Install Rygel:

`root `[`#`]`emerge --ask net-misc/rygel`

** Note**\
Rygel relies on GStreamer so check [[[media-plugin/gst-plugins-meta]](https://packages.gentoo.org/packages/media-plugin/gst-plugins-meta)[]] and the individual *media-plugins/gst-plugin-\*\'* packages for additional video/audio format support.

### [create user and group]

`root `[`#`]`useradd --system -c "Rygel media server" --user-group --create-home --base-dir /var/lib --shell /sbin/nologin rygel`

### [copy files]

Copy the 2 files to the respective folders and you should be able to start the server.

[FILE] **`/etc/init.d/rygel`**

    #!/sbin/openrc-run
    # Copyright 1999-2012 Gentoo Foundation
    # Distributed under the terms of the GNU General Public License v2
    # $Header: $

    depend()

    start()  -m 644 $
            ebegin "Starting Rygel"
            start-stop-daemon --start  --background --quiet \
                    --make-pidfile \
                    --pidfile $ \
                    --user $ \
                    --group $ \
                    --stdout $ \
                    --stderr $ \
                    --exec /usr/bin/rygel -- --config $ \
                    $
            eend $?
    }

    stop()
            eend $?
    }

[FILE] **`/etc/conf.d/rygel`**

    # /etc/conf.d/rygel: config file for /etc/init.d/rygel

    #Rygel pid file
    RYGEL_PIDFILE="/var/run/rygel.pid"
    #Log file
    RYGEL_LOGFILE="/var/log/rygel.log"
    #Run as user
    RYGEL_USER="rygel"
    #Rygel group
    RYGEL_GROUP="rygel"
    #Path to config file
    RYGEL_CONFIG="/etc/rygel.conf"
    #Rygel options
    #RYGEL_OPTIONS="--disable-transcoding"

### [Modify config file]

If started with the init script you will want to modify the uri option. Add the directories you like it to search for media.

[FILE] **`/etc/rygel.conf`**

    [MediaExport]
    enabled=true
    title=@REALNAME@'s media
    # List of URIs to export. Following variables are automatically substituted by
    # the appropriate XDG standard media folders by Rygel for you.
    #
    #       * @MUSIC@: The standard music folder (typically $/Music).
    #       * @VIDEOS@: The standard videos folder (typically $/Videos).
    #       * @PICTURES@: The standard pictures folder (typically $/Pictures).
    #
    #uris=@MUSIC@;@VIDEOS@;@PICTURES@
    uris=@MUSIC@;@VIDEOS@;@PICTURES@;/path/to/music;/path/to/video
    extract-metadata=true
    monitor-changes=true

## [Setup using shell-session]

shell-session is a script created by eva and is available from [github](https://github.com/EvaSDK/shell-session/blob/master/shell-session). It is supposed to create a dbus session for rygel under a regular user and from /home/\<user\> and then start /etc/xdg/autostart (which has en entry for rygel). I tried this and it seems to not work very well for me. At this point I can\'t really recommend this but if someone has more success please update this wiki page.