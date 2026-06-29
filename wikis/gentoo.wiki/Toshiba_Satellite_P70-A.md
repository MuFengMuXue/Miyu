**Resources**

[[]][Home](http://www.toshiba.eu/discontinued-products/satellite-p70-a-104/)

## Contents

-   [[1] [Summary]](#Summary)
-   [[2] [Hardware]](#Hardware)
-   [[3] [Installation]](#Installation)
    -   [[3.1] [Microcode]](#Microcode)
    -   [[3.2] [Network - Wi-Fi and Ethernet drivers:]](#Network_-_Wi-Fi_and_Ethernet_drivers:)
    -   [[3.3] [SD card reader]](#SD_card_reader)
-   [[4] [ACPI]](#ACPI)
-   [[5] [Graphics and Xorg]](#Graphics_and_Xorg)
-   [[6] [Touchpad]](#Touchpad)
-   [[7] [Sample configuration files]](#Sample_configuration_files)

## [Summary]

Everything works for me. I\'ve had this laptop for nearly three years now. The build quality is outstanding, it has travelled a lot and taken a lot of bashing. It has a large display which is why I bought it (no loss of pixels yet), very decent performance and two hard drive bays. I replaced one of the discs with a SSD about 18 months ago and it is close to perfect for me. It does run hot when emerge is crunching through a long list of compiles but is not uncomfortable.

I really don\'t see this machine needing replacing for probably another two years yet. Maybe the discs might need replacing before then but SMART will help with that.

I list some basic configuration files in use on mine at the end of these notes.

## [Hardware]

-   Intel Core i7 G4 - \"Haswell\". Quad core with hyperthreading
-   16 GB RAM
-   2 x 1TB hybrid SATA hard disks with 8GB of SSD each
-   Built in Intel graphics and a discrete Nvidia card which can be accessed via Optimus
-   17.3\" LED
-   Wifi + Ethernet - both are Intel
-   4 USB3 interfaces
-   Multi finger sense Synaptics touchpad

## [Installation]

You can install Linux without having to accept the Windows 8 license. Enter the BIOS by holding Esc and mashing F2 or F12. Disable SecureBoot and enable booting from DVD/CD. If you get an absolutely black screen, pass acpi_backlight=vendor to the kernel command line. Proceed as normal.

If you enable \"Fast boot\" hold down F12 before powering on to get to the boot menu, then select Setup menu to enter the BIOS.

There are two hard disks already fitted so you could consider using software RAID at install time

### [Microcode]

Install this: sys-apps/microcode-ctl, configure and run it. I\'m fairly sure that Optimus (at least) will not work properly without it.

### [Network - Wi-Fi and Ethernet drivers:]

Install the ebuild [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] to get the required firmware. The kernel driver is iwlwifi.

### [SD card reader]

## [ACPI]

## [Graphics and Xorg]

I have eventually got it all working Intel + NVidia proprietary driver (using [Bumblebee](https://wiki.gentoo.org/wiki/NVIDIA/Bumblebee "NVIDIA/Bumblebee")) with a framebuffer console.

Get the Intel graphics working first. Add user to video group. In the kernel config I\'ve got these enabled. No need to enable any other frame buffers - no need for uvesafb etc.

[KERNEL]

    Device drivers --->
     Graphics Support --->
      * /dev/agpgart (AGP Support) --->
       * Intel 440LX/BX/GX, I8XX and E7x05 chipset support (Necessary?)
      * Laptop Hybrid Graphics - GPU switching support (Needed with BB?)
      * Direct Rendering Manager ... --->
      * Intel 8xx/9xx/G3x/G4x/HD Graphics
      * Enable modesetting on intel by default
      * Enable legacy fbdev support ... intel driver  (Necessary?)
      * Enable preliminary support for prerelease Intel hardware by default
      * Support for frame buffer devices --->
       * Enable firmware EDID
       * Enable Video Mode Handling Helpers
       * Backlight and LCD device support --->
        (All built as modules)
      * Console display driver support --->
       * VGA text console
       * Framebuffer console support

You should also be able to enable fast boot and get a graphical console from grub2 through to X. You should be able to use all the features of the Intel GPU. I was able to get Chrome to fully support WebGL etc by disabling the blacklist in chrome://flags and get a full green set of enabled GPU options in chrome://gpu.

Now install bbswitch, bumblebee and nvidia-drivers. I was able to leave all of that pretty much at defaults in their configs. systemctl enable bumblebeed and reboot

These should return two different sets of working details:

`root `[`#`]`glxinfo `

`root `[`#`]`optirun glxinfo `

## [Touchpad]

-   Add Synaptics xorg driver to INPUT_DEVICES and ensure that x11-drivers/xf86-input-synaptics gets built

[FILE] **`/etc/portage/make.conf`Gentoo make.conf**

    INPUT_DEVICES="evdev synaptics mouse"

-   This can be used to get you started in configuring it

`root `[`#`]`cp /usr/share/X11/xorg.conf.d/50-synaptics.conf /etc/X11/xorg.conf.d/`

-   For KDE Plasma, [[[kde-plasma/desktop]](https://packages.gentoo.org/packages/kde-plasma/desktop)[]] is providing a GUI control module if USE `touchpad` is enabled.

## [Sample configuration files]

[FILE] **`/etc/portage/make.conf`Gentoo make.conf**

    CFLAGS="-march=native -O2 -pipe -fomit-frame-pointer"
    CXXFLAGS="$"

    MAKEOPTS="-j9"

    FEATURES="parallel-fetch sandbox usersandbox userfetch userpriv"
    PORTAGE_RSYNC_RETRIES=5
    PORTAGE_ELOG_CLASSES="error warn log"
    PORTAGE_ELOG_SYSTEM="save"
    PORTDIR="/usr/portage"
    PORT_LOGDIR="/var/log/portage"
    DISTDIR="$/distfiles"
    PKGDIR="$/packages"

    ACCEPT_KEYWORDS="~amd64"
    ACCEPT_LICENSE="*"

    INPUT_DEVICES="evdev synaptics mouse"
    VIDEO_CARDS="nvidia intel i965"
    LINGUAS="en_GB"

    USE="64bit X Xaw3d a52 aac acl acpi activefilter additions admin \
         administrator ads agent alsa amarok2 apache2 apng asf bash-completion \
         bcmath bluetooth bluray branding bzip2 cairo calendar cdb cdda cddax \
         cddb cdparanoia cdr cdrom cgi chm clamav clamd clamdtop cleartype \
         client config-file crypt css ctype curl custom-optimization customlog \
         daap dba declarative dga divx dmi dragonplayer dv dvb dvd dvdr dvdread \
         embedded enca encode epson exif exim exiscan exiscan-acl expat \
         extensions extras ffmpeg fftw filter flac flash flexresp2 fontconfig \
         foomaticdb fts3 fuse g3dvl g722 g729 gd geoip geolocation groupwise \
         h224 h281 hash hbci html imagemagick imap iproute2 john jpeg jumpplay \
         kde kerberos kexi kipi latex lcms ldap logrotate lua lzo mad maildir \
         math mhash mime ming mjpeg mmkeys mmx mmxext mng mozsvg mp3 mp3tunes \
         mp4 mp4live mpd mpeg mpeg2 mplayer mtp multipath multiuser musepack \
         musicbrainz mysql mysqli nas no-helper nsplugin ntfs objc ofx ogg \
         on-the-fly-crypt openexr opengl ospfapi overlays passwordsave pcap pcre \
         pda pdf php pic pipechan plasma plotutils pmu png policykit posix \
         postgresql ppds pulseaudio qemu qt3support quotes realmedia realms \
         reload reload-error-restart rss samba scanner screen script sdl \
         secure-delete semantic-desktop sensord session smp sna sni soap sockets \
         spf spl sql sqlite srt sse sse2 sse3 sse4 sse4_1 sse4a ssse3 \
         startup-notification suexec syslog systemd templates theora tiff tools \
         transcode truetype udev udisks udisks2 underscores unicode upcall upnp \
         usb v4l v4l2 vaapi vboxbfe vcd vdpau virt-network visualization vlc \
         vorbis wallpapers watchdog wav wavpack webkit webrtc-aec winbind \
         winetools winpopup wma wmf wmp x264 xanim xattr xcb xinerama xml \
         xmlreader xmlrpc xmlwriter xulrunner xv xvid xvmc xvnc yv12 zeo zip \
         -gstreamer -handbook -jabber -jingle -speex"