**Resources**

[[]][Home](https://kodi.tv/)

[[]][GitHub](https://github.com/xbmc/xbmc)

[[]][Official documentation](https://kodi.wiki/)

[[]][[#kodi](ircs://irc.libera.chat/#kodi)] ([[webchat](https://web.libera.chat/#kodi)])

**Kodi** (formerly XBMC) is an open source home theater application.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Create user]](#Create_user)
-   [[3] [Services]](#Services)
    -   [[3.1] [Emerge]](#Emerge_2)
    -   [[3.2] [Configure]](#Configure)
    -   [[3.3] [Service]](#Service)
        -   [[3.3.1] [OpenRC]](#OpenRC)
        -   [[3.3.2] [systemd]](#systemd)
-   [[4] [Gentoo Hardened]](#Gentoo_Hardened)
-   [[5] [Usage]](#Usage)
    -   [[5.1] [Shutdown]](#Shutdown)
-   [[6] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [media-tv/kodi](https://packages.gentoo.org/packages/media-tv/kodi) [[]] [A free and open source media-player and entertainment hub]

  ------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+css`](https://packages.gentoo.org/useflags/+css)                       Enable reading of encrypted DVDs
  [`+optical`](https://packages.gentoo.org/useflags/+optical)               Enable Audio CD playback, optical disks detection and reading (CD-ROM, Video CD, and others), and ISO optical disk images direct reading. DVD disks may require additional \'udf\' flag.
  [`+system-ffmpeg`](https://packages.gentoo.org/useflags/+system-ffmpeg)   Use system ffmpeg instead of the bundled one
  [`+xslt`](https://packages.gentoo.org/useflags/+xslt)                     Enable metadata XSLT scrapers support with dev-libs/libxslt
  [`X`](https://packages.gentoo.org/useflags/X)                             Add support for X11
  [`airplay`](https://packages.gentoo.org/useflags/airplay)                 enable AirPlay support
  [`alsa`](https://packages.gentoo.org/useflags/alsa)                       Add support for media-libs/alsa-lib (Advanced Linux Sound Architecture)
  [`bluetooth`](https://packages.gentoo.org/useflags/bluetooth)             Enable JSON-RPC over BT for remote control connected via bluetooth
  [`bluray`](https://packages.gentoo.org/useflags/bluray)                   Enable playback of Blu-ray filesystems
  [`caps`](https://packages.gentoo.org/useflags/caps)                       Use sys-libs/libcap to bind to privileged ports as non-root
  [`cec`](https://packages.gentoo.org/useflags/cec)                         Enable support for HDMI-CEC devices via libcec
  [`dbus`](https://packages.gentoo.org/useflags/dbus)                       Enable dbus support for anything that needs it (gpsd, gnomemeeting, etc)
  [`doc`](https://packages.gentoo.org/useflags/doc)                         Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`eventclients`](https://packages.gentoo.org/useflags/eventclients)       Install full set of Kodi python eventclients and eventclients examples
  [`gbm`](https://packages.gentoo.org/useflags/gbm)                         Use the Graphics Buffer Manager for EGL on KMS.
  [`gles`](https://packages.gentoo.org/useflags/gles)                       Use simplified OpenGLES instead of full-scale OpenGL
  [`lcms`](https://packages.gentoo.org/useflags/lcms)                       Add lcms support (color management engine)
  [`libusb`](https://packages.gentoo.org/useflags/libusb)                   Use virtual/libusb for usb device hotplug support. This flag should only be enabled if you\'re running a non-Linux kernel or you don\'t want to use udev.
  [`lirc`](https://packages.gentoo.org/useflags/lirc)                       Enable support for IR remote controls using app-misc/lirc
  [`mariadb`](https://packages.gentoo.org/useflags/mariadb)                 Enable support store of media library metadata on local or remote MariaDB
  [`mysql`](https://packages.gentoo.org/useflags/mysql)                     Enable support store of media library metadata on local or remote MySQL
  [`nfs`](https://packages.gentoo.org/useflags/nfs)                         Enable NFS client support
  [`pipewire`](https://packages.gentoo.org/useflags/pipewire)               Enable pipewire support
  [`postproc`](https://packages.gentoo.org/useflags/postproc)               Use bundled libpostproc to postprocess and deinterlace video
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)           Add sound server support via media-libs/libpulse (may be PulseAudio or PipeWire)
  [`samba`](https://packages.gentoo.org/useflags/samba)                     Add support for SAMBA (Windows File and Printer sharing)
  [`soc`](https://packages.gentoo.org/useflags/soc)                         Use additional media-video/ffmpeg patches for efficient playback on some SoCs (e.g. ARM, RISC-V)
  [`test`](https://packages.gentoo.org/useflags/test)                       Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`udev`](https://packages.gentoo.org/useflags/udev)                       Use udev rules to handle devices\' permissions and hotplug support. Unless you know what you\'re doing do not disable this flag on Linux kernels. This is provided as an option for completeness.
  [`udf`](https://packages.gentoo.org/useflags/udf)                         Enable UDF support. Required for playing blurays.
  [`upnp`](https://packages.gentoo.org/useflags/upnp)                       Enable UPnP port mapping support
  [`vaapi`](https://packages.gentoo.org/useflags/vaapi)                     Enable Video Acceleration API for hardware decoding
  [`vdpau`](https://packages.gentoo.org/useflags/vdpau)                     Enable the Video Decode and Presentation API for Unix acceleration interface
  [`wayland`](https://packages.gentoo.org/useflags/wayland)                 Enable dev-libs/wayland backend
  [`webserver`](https://packages.gentoo.org/useflags/webserver)             Enable internal webserver
  [`zeroconf`](https://packages.gentoo.org/useflags/zeroconf)               Support for DNS Service Discovery (DNS-SD)
  ------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-03 22:16] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask media-tv/kodi`

## [Configuration]

### [Create user]

First create the [kodi] user:

`root `[`#`]`useradd -m -G audio,cdrom,video,cdrw,usb,users kodi`

To add support for HDMI CEC:

`root `[`#`]`gpasswd --add kodi dialout`

## [Services]

### [Emerge]

`root `[`#`]`emerge --ask x11-misc/lightdm`

### [Configure]

[FILE] **`/etc/conf.d/display-manager`**

    DISPLAYMANAGER="lightdm"

[FILE] **`/etc/lightdm/lightdm.conf`**

    [Seat:*]
    autologin-user=kodi
    user-session=kodi
    session-wrapper=/etc/lightdm/Xsession

### [Service]

#### [OpenRC]

Add dbus and display-manager to the default runlevel if it needs to be started automatically:

`root `[`#`]`rc-update add dbus default `

`root `[`#`]`rc-update add display-manager default `

`root `[`#`]`rc-service dbus start `

`root `[`#`]`rc-service display-manager start`

#### [systemd]

`root `[`#`]`systemctl enable lightdm `

`root `[`#`]`systemctl start lightdm`

## [Gentoo Hardened]

Running Kodi on a [Hardened Gentoo](https://wiki.gentoo.org/wiki/Hardened/Introduction_to_Hardened_Gentoo "Hardened/Introduction to Hardened Gentoo") installation is possible. To avoid grsecurity interfering with network connectivity, the `CONFIG_GRKERNSEC_PROC_USER` kernel option must not be enabled.

Should you require a restricted [/proc] filesystem, use `CONFIG_GRKERNSEC_PROC_USERGROUP` and set `GRKERNSEC_PROC_GID` to the ID of a group that the user running Kodi is a member of.

## [Usage]

### [Shutdown]

Allow the [kodi] user to issue an shutdown via [polkit](https://wiki.gentoo.org/wiki/Polkit "Polkit"), resulting in a shutdown option in the Kodi menu:

[FILE] **`/etc/polkit-1/rules.d/60-kodi.rules`**

    polkit.addRule(function(action, subject)
    });

** Note**\
Ensure the `udev` USE flag is set for shutdown to work.

## [External resources]

-   [Unofficial Kodi Overlay](https://github.com/frace/kodi-overlay)