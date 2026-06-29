**Resources**

[[]][Home](https://gerbera.io/)

[[]][GitHub](https://github.com/gerbera/gerbera)

[[]][Official documentation](http://docs.gerbera.io/en/latest/)

**Gerbera** is an open source [UPnP](https://en.wikipedia.org/wiki/Universal_Plug_and_Play "wikipedia:Universal Plug and Play") media server that streams digital media through a home network to UPnP compatible devices. Gerbera is based on [MediaTomb](https://sourceforge.net/projects/mediatomb/) 0.12.1, which is no longer maintained.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Network]](#Network)
    -   [[2.2] [MySQL]](#MySQL)
    -   [[2.3] [Transcoding]](#Transcoding)
        -   [[2.3.1] [Alternative transcoders]](#Alternative_transcoders)
            -   [[2.3.1.1] [VLC]](#VLC)
            -   [[2.3.1.2] [MPlayer]](#MPlayer)
    -   [[2.4] [DLNA]](#DLNA)
    -   [[2.5] [Video thumbnails]](#Video_thumbnails)
    -   [[2.6] [Raw images]](#Raw_images)
    -   [[2.7] [Service]](#Service)
        -   [[2.7.1] [OpenRC]](#OpenRC)
        -   [[2.7.2] [systemd]](#systemd)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Mimetype mapping]](#Mimetype_mapping)
-   [[4] [See also]](#See_also)
-   [[5] [References]](#References)

## [Installation]

### [Kernel]

Gerbera requires IP multicast support for automatic discovery by UPnP devices.

[KERNEL] **Enabling IP multicast support**

    [*] Networking support --->
                Networking options --->
                  [*] TCP/IP networking
                  [*]   IP: multicasting

Gerbera supports [inotify](https://en.wikipedia.org/wiki/Inotify "wikipedia:Inotify"), which is a file-monitoring mechanism that allows Gerbera to be notified about changes to files immediately. For more information, please consult the Gerbera [trail operations](http://docs.gerbera.io/en/latest/ui.html#trail-operations) documentation.

[KERNEL] **Enabling inotify support**

        File systems --->
          [*] Inotify support for userspace

### [USE flags]

### [USE flags for] [net-misc/gerbera](https://packages.gentoo.org/packages/net-misc/gerbera) [[]] [UPnP Media Server]

  ------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+exif`](https://packages.gentoo.org/useflags/+exif)                           Add support for reading EXIF headers from JPEG and TIFF images
  [`+ffmpeg`](https://packages.gentoo.org/useflags/+ffmpeg)                       Enable ffmpeg/libav-based audio/video codec support
  [`+javascript`](https://packages.gentoo.org/useflags/+javascript)               Enable javascript support
  [`+magic`](https://packages.gentoo.org/useflags/+magic)                         Add support for file type detection via magic bytes (usually via libmagic from sys-apps/file)
  [`+matroska`](https://packages.gentoo.org/useflags/+matroska)                   Add support for the matroska container format (extensions .mkv, .mka and .mks)
  [`+taglib`](https://packages.gentoo.org/useflags/+taglib)                       Use media-libs/taglib for reading files\' metadata
  [`curl`](https://packages.gentoo.org/useflags/curl)                             Support HTTP media sources (e.g. internet radio)
  [`debug`](https://packages.gentoo.org/useflags/debug)                           Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`doc`](https://packages.gentoo.org/useflags/doc)                               Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`exiv2`](https://packages.gentoo.org/useflags/exiv2)                           Use media-gfx/exiv2 to extract EXIF information
  [`ffmpegthumbnailer`](https://packages.gentoo.org/useflags/ffmpegthumbnailer)   Enable video thumbnail support with media-video/ffmpegthumbnailer
  [`mysql`](https://packages.gentoo.org/useflags/mysql)                           Use dev-db/mysql as backend rather than SQLite3
  [`systemd`](https://packages.gentoo.org/useflags/systemd)                       Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`test`](https://packages.gentoo.org/useflags/test)                             Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-18 16:30] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

After setting any USE configuration, proceed to install Gerbera:

`root `[`#`]`emerge --ask net-misc/gerbera`

## [Configuration]

### [Network]

-   To set the network interface that Gerbera binds to, add the following to the `GERBERA_OPTIONS` variable, and substitute `network_interface` with the appropriate value e.g. `GERBERA_OPTIONS="-e eth0"`

[FILE] **`/etc/conf.d/gerbera`**

    GERBERA_OPTIONS="-e network_interface"

-   To set the IP address that Gerbera binds to, add the following to the `GERBERA_OPTIONS` variable, and substitute `ip_address` with the appropriate value e.g. `GERBERA_OPTIONS="-i 192.168.0.1"`

[FILE] **`/etc/conf.d/gerbera`**

    GERBERA_OPTIONS="-i ip_address"

### [MySQL]

** Important**\
[MySQL](https://wiki.gentoo.org/wiki/MySQL "MySQL") support requires the `USE` flag `mysql` to be enabled for the [[[net-misc/gerbera]](https://packages.gentoo.org/packages/net-misc/gerbera)[]] package.

-   To enable MySQL support, set the `enabled` attribute to `yes` for the `<mysql>` element:

[FILE] **`/etc/gerbera/config.xml`**

          <mysql enabled="yes">

-   Set the `enabled` attribute to `no` for the `<sqlite3>` element:

[FILE] **`/etc/gerbera/config.xml`**

          <sqlite3 enabled="no">

-   Set the `<host>`, `<database>`, `<username>` and `` elements:

[FILE] **`/etc/gerbera/config.xml`**

            <host>host</host>
            <database>database</database>
            <username>username</username>
            password</password>

-   Login to MySQL and create the Gerbera database and user, using the `host`, `database`, `username` and `password` values set in the Gerbera configuration file:

`mysql>``CREATE DATABASE database; `

`mysql>``GRANT ALL ON database.* TO 'username'@'host' IDENTIFIED BY 'password'; `

### [Transcoding]

Gerbera supports transcoding media files to formats that are supported by the UPnP device being used. The default Gentoo configuration file uses FFmpeg to transcode FLAC, Flash, Theora and Vorbis files. For more information, please consult the Gerbera [transcoding configuration](http://docs.gerbera.io/en/latest/config-transcode.html) documentation.

-   To enable transcoding support, set the `enabled` attribute to `yes` for the `<transcoding>` element:

[FILE] **`/etc/gerbera/config.xml`**

      <transcoding enabled="yes">

-   For every additional mimetype that requires transcoding, add the following section in between the `<mimetype-profile-mappings>` and `</mimetype-profile-mappings>` elements and substitute `mimetype` and `profile` with the appropriate values e.g. `<transcode mimetype="video/quicktime" using="video2mpeg"/>`

[FILE] **`/etc/gerbera/config.xml`**

          <transcode mimetype="mimetype" using="profile"/>

-   Install FFmpeg:

** Important**\
Transcoding support requires the `USE` flag `encode` to be enabled for the [[[media-video/ffmpeg]](https://packages.gentoo.org/packages/media-video/ffmpeg)[]] package.

`root `[`#`]`emerge --ask --noreplace media-video/ffmpeg`

#### [Alternative transcoders]

Gerbera\'s transcoding support is very flexible and any application capable of transcoding can be used. For more information, please consult the Gerbera [transcoding](http://docs.gerbera.io/en/latest/transcoding.html) documentation.

##### [VLC]

**Audio**

-   To enable VLC audio transcoding, replace the `<agent>` element for the `audio2pcm` profile with the following:

[FILE] **`/etc/gerbera/config.xml`**

            <agent command="vlc" arguments="%in -I dummy --sout=#transcode:standard vlc://quit"/>

-   Set the `<accept-url>` element to `yes` for the `audio2pcm` profile:

[FILE] **`/etc/gerbera/config.xml`**

            <accept-url>yes</accept-url>

**Video**

-   To enable VLC video transcoding, replace the `<agent>` element for the `video2mpeg` profile with the following:

[FILE] **`/etc/gerbera/config.xml`**

            <agent command="vlc" arguments="%in -I dummy --sout=#transcode:standard vlc://quit"/>

-   Set the `<accept-url>` element to `yes` for the `video2mpeg` profile:

[FILE] **`/etc/gerbera/config.xml`**

            <accept-url>yes</accept-url>

-   Install VLC:

** Important**\
Transcoding support requires the `USE` flags `ffmpeg` and `encode` to be enabled for the [[[media-video/vlc]](https://packages.gentoo.org/packages/media-video/vlc)[]] package. It also requires the `USE` flag `encode` to be enabled for the [[[media-video/ffmpeg]](https://packages.gentoo.org/packages/media-video/ffmpeg)[]] package.

`root `[`#`]`emerge --ask --noreplace media-video/vlc`

##### [MPlayer]

**Video**

-   To enable MPlayer video transcoding, replace the `<agent>` element for the `video2mpeg` profile with the following:

[FILE] **`/etc/gerbera/config.xml`**

            <agent command="mencoder" arguments="%in -o %out -ovc lavc -oac lavc -lavcopts vcodec=mpeg2video:vbitrate=4096:vrc_minrate=0:vrc_maxrate=9800:vrc_buf_size=1835:keyint=15:vstrict=0:acodec=mp2:abitrate=192 -vf harddup -af lavcresample=48000:channels=2 -srate 48000 -ofps 25 -of mpeg -mpegopts format=mpeg2:tsaf"/>

-   Set the `<accept-url>` element to `yes` for the `video2mpeg` profile:

[FILE] **`/etc/gerbera/config.xml`**

            <accept-url>yes</accept-url>

-   Install MPlayer:

** Important**\
Transcoding support requires the `USE` flag `encode` to be enabled for the [[[media-video/mplayer]](https://packages.gentoo.org/packages/media-video/mplayer)[]] package.

`root `[`#`]`emerge --ask --noreplace media-video/mplayer`

### [DLNA]

** Note**\
Gerbera is not a [DLNA](https://en.wikipedia.org/wiki/Digital_Living_Network_Alliance "wikipedia:Digital Living Network Alliance") media server. Gerbera does have partial DLNA support for some DLNA devices e.g. PlayStation 3.

-   To enable DLNA support, set the `extend` attribute to `yes` for the `` element:

[FILE] **`/etc/gerbera/config.xml`**



-   For DLNA enabled TVs (e.g. Samsung), add the following section in between the `<server>` and `</server>` elements:

[FILE] **`/etc/gerbera/config.xml`**

        <custom-http-headers>
          <add header="transferMode.dlna.org: Streaming"/>
          <add header="contentFeatures.dlna.org: DLNA.ORG_OP=01;DLNA.ORG_CI=0;DLNA.ORG_FLAGS=01500000000000000000000000000000"/>
        </custom-http-headers>

** Note**\
Support for custom headers requires =[[[net-libs/libupnp]](https://packages.gentoo.org/packages/net-libs/libupnp)[]]-1.8.5 or later^[\[1\]](#cite_note-1)^.

### [Video thumbnails]

** Important**\
Video thumbnail support requires the USE flags `ffmpeg` and `ffmpegthumbnailer` to be enabled for the [[[net-misc/gerbera]](https://packages.gentoo.org/packages/net-misc/gerbera)[]] package.

-   To enable video thumbnail support, set the `enabled` attribute to `yes` for the `<ffmpegthumbnailer>` element:

[FILE] **`/etc/gerbera/config.xml`**

          <ffmpegthumbnailer enabled="yes">

-   To overlay a filmstrip border on the generated thumbnail, set the `<filmstrip-overlay>` element to `yes`:

[FILE] **`/etc/gerbera/config.xml`**

            <filmstrip-overlay>yes</filmstrip-overlay>

-   For [DLNA](#DLNA) enabled devices that support video thumbnails (e.g. PlayStation 3), set the `extend` attribute to `yes` for the `` element:

[FILE] **`/etc/gerbera/config.xml`**



### [Raw images]

-   To enable (Canon CR2 and Nikon NEF) [raw image](https://en.wikipedia.org/wiki/Raw_image_format "wikipedia:Raw image format") support, enable [transcoding](#Transcoding) and add the following section in between the `` and `</profile>` elements:

[FILE] **`/etc/gerbera/config.xml`**


            <mimetype>image/jpeg</mimetype>
            <accept-url>no</accept-url>
            <first-resource>yes</first-resource>
            <hide-original-resource>yes</hide-original-resource>
            <use-chunked-encoding>no</use-chunked-encoding>
            <agent command="/usr/local/bin/gerbera-raw2jpeg" arguments="%in %out"/>
            <buffer size="524288" chunk-size="512" fill-size="1024"/>
          </profile>

-   Add the following section in between the `<mimetype-profile-mappings>` and `</mimetype-profile-mappings>` elements:

[FILE] **`/etc/gerbera/config.xml`**

          <transcode mimetype="image/raw" using="raw2jpeg"/>

-   For every additional raw image format (supported by [dcraw](http://www.cybercom.net/~dcoffin/dcraw/)), add the following section in between the `<extension-mimetype ignore-unknown="no">` and `</extension-mimetype>` elements, and substitute `extension` with the appropriate value e.g. `<map from="kdc" to="image/raw"/>`

[FILE] **`/etc/gerbera/config.xml`**

            <map from="extension" to="image/raw"/>

-   Since dcraw only outputs to stdout, the output will need to be redirected with the following script:

[FILE] **`/usr/local/bin/gerbera-raw2jpeg`**

    #!/bin/sh

    DCRAW_PATH="/usr/bin/dcraw"
    INPUT="$1"
    OUTPUT="$2"

    exec "$" -e -c "$" > "$"

-   Install dcraw:

`root `[`#`]`emerge --ask --noreplace media-gfx/dcraw`

### [Service]

#### [OpenRC]

-   To start Gerbera:

`root `[`#`]`rc-service gerbera start`

-   To start Gerbera at boot:

`root `[`#`]`rc-update add gerbera default`

#### [systemd]

Start Gerbera:

`root `[`#`]`systemctl start gerbera`

Start Gerbera at boot:

`root `[`#`]`systemctl enable gerbera`

## [Troubleshooting]

### [Mimetype mapping]

** Important**\
After adding or changing a mimetype mapping, media needs to be imported again since mimetype mappings are only set during import.

Gerbera (via libmagic) may identify the mimetype of some files incorrectly. A common case is where *videos* with the `mp4` extension are identified as the mimetype `audio/mp4`. To override the mimetype returned by libmagic, add the following section in between the `<extension-mimetype ignore-unknown="no">` and `</extension-mimetype>` elements, and substitute `extension` and `mimetype` with the appropriate values e.g. `<map from="mp4" to="video/mp4"/>`

[FILE] **`/etc/gerbera/config.xml`**

            <map from="extension" to="mimetype"/>

## [See also]

-   [MiniDLNA](https://wiki.gentoo.org/wiki/MiniDLNA "MiniDLNA") --- a media server aiming to be DLNA/UPnP-AV compliant.

## [References]

1.  [[[↑](#cite_ref-1)] [seppbiersack. [Samsung TV Support](https://github.com/gerbera/gerbera/issues/352), [Gerbera GitHub](https://github.com/gerbera/gerbera), September 26th, 2018. Retrieved on March 7th, 2019.]]