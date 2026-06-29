[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Build+Manjaro+ISOs+with+buildiso&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Build_Manjaro_ISOs_with_buildiso "Build Manjaro ISOs with buildiso (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Build_Manjaro_ISOs_with_buildiso/ru "Создание ISO-файлов Manjaro с помощью buildiso (100% translated)") • ‎[فارسی](//wiki.manjaro.org/index.php?title=Build_Manjaro_ISOs_with_buildiso/fa "ISO های مانجارو را با bulidiso بسازید (17% translated)")

## Contents

-   [[1] [Prerequisites]](#Prerequisites)
    -   [[1.1] [Install Manjaro Tools]](#Install_Manjaro_Tools)
-   [[2] [ISO profile]](#ISO_profile)
    -   [[2.1] [Download the latest ISO profiles]](#Download_the_latest_ISO_profiles)
    -   [[2.2] [ISO profile overview]](#ISO_profile_overview)
    -   [[2.3] [Modifying an ISO profile]](#Modifying_an_ISO_profile)
        -   [[2.3.1] [desktop-overlay]](#desktop-overlay)
        -   [[2.3.2] [Clone Custom Wallpaper Desktop]](#Clone_Custom_Wallpaper_Desktop)
        -   [[2.3.3] [Example]](#Example)
        -   [[2.3.4] [profile.conf]](#profile.conf)
        -   [[2.3.5] [Packages-Desktop]](#Packages-Desktop)
        -   [[2.3.6] [Adding AUR packages]](#Adding_AUR_packages)
-   [[3] [manjaro-tools.conf]](#manjaro-tools.conf)
-   [[4] [Build your ISO]](#Build_your_ISO)
    -   [[4.1] [Example:]](#Example:)
-   [[5] [Cleaning your hard drive]](#Cleaning_your_hard_drive)
-   [[6] [Tips & Tricks]](#Tips_.26_Tricks)
    -   [[6.1] [Building a minimal ISO]](#Building_a_minimal_ISO)
-   [[7] [See also]](#See_also)

# [Prerequisites]

This is a detailed walkthrough of installation and configuration of the tools and build process.

It is a requirement to either download and install the latest version of [Manjaro](https://manjaro.org/products/download/x86) or be running a well maintained Manjaro system. **It is vital your system is updated** with the latest available kernel and packages.

## [Install Manjaro Tools]

To get started you need to the following packages

[user \$ ][ pamac install manjaro-tools-iso-git git [COPY TO CLIPBOARD]]

\

We will be working with the official XFCE to help you understand what you need to do.

# [ISO profile]

## [Download the latest ISO profiles]

The latest profiles can be found in the Manjaro gitlab. You can download them directly using the command:

[user \$ ][ git clone https://gitlab.manjaro.org/profiles-and-settings/iso-profiles.git \~/iso-profiles [COPY TO CLIPBOARD]]

\

## [ISO profile overview]

The ISO profile for xfce can now be found at

[user \$ ][ ls -l \~/iso-profiles/manjaro/xfce [COPY TO CLIPBOARD]]

\

Let\'s take a closer look at the XFCE profile folder (marked above):

    desktop-overlay
    live-overlay -> ../../shared/manjaro/live-overlay
    Packages-Desktop
    Packages-Live -> ../../shared/Packages-Live
    Packages-Mhwd -> ../../shared/Packages-Mhwd
    Packages-Root -> ../../shared/Packages-Root
    profile.conf

-   **desktop-overlay**: After every successful installation of your ISO the files and folders in here will get copied over.
-   *live-overlay*: Similar to *desktop-overlay*. Files and folders in here will only get copied over to the LiveCD of your ISO.
-   **Packages-Desktop**: This file contains packages for the ISO installation. All packages will also get installed on LiveCDs.
-   *Packages-Live*: This file contains packages, which will only get installed on the LiveCD.
-   *Packages-Mhwd*: This file contains Mhwd packages important to all Manjaro installations and LiveCDs.
-   *Packages-Root*: This file contains base packages important to all Manjaro installations and LiveCDs.
-   **profile.conf** contains basic settings for your ISO installation and LiveCD.

As you have probably noticed, several are only symlinks to the `shared` ISO profile. It is good practice to never change files or folders in the `shared` ISO profile. If you ever want to change them, first copy them to your ISO profile folder and delete the symlink.

All folders and files specific to your ISO are **in bold**. You can change them to your liking.

## [Modifying an ISO profile]

The most common places to tweak and customize an ISO profile are the 3 folders marked above: *desktop-overlay*, *profile.conf*, *Packages-Desktop*:

### [desktop-overlay]

The *desktop-overlay* folder looks like this:

\

[\$] [tree \~/iso-profiles/manjaro/xfce/desktop-overlay/etc]\

    ../iso-profiles/manjaro/xfce/desktop-overlay/
    ├── etc
    │   ├── fonts
    │   │   └── conf.d
    │   │       └── 70-no-bitmaps.conf
    │   └── lightdm
    │       ├── lightdm.conf
    │       └── lightdm-gtk-greeter.conf
    └── usr
        └── share
            └── icons
                └── default
                    └── index.theme

\
Go to this directory.

[user \$ ][ cd \~/iso-profiles/manjaro/xfce/desktop-overlay/etc/ [COPY TO CLIPBOARD]]

\

Then create **skel** folder. This is where you can clone everything you see on your Desktop Screen to ISO.

[user \$ ][ mkdir skel [COPY TO CLIPBOARD]]

\

After the ISO has been successfully installed all files and folder in *desktop-overlay* folder get copied over to the installed system. This includes settings/config files but also themes and backgrounds/pictures.

All files and folder in here will get copied to the home folder. Most hidden files and their structure in `~/iso-profiles/manjaro/xfce/desktop-overlay/etc/skel/` should be already familiar to you, because your home folder looks very similar.

### [Clone Custom Wallpaper Desktop]

To clone your Custom Wallpaper Desktop. Open a New File Manager and go to this file.

    ~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-desktop.xml

Change all image directories to where your Custom Wallpaper was located at. For example:

     /usr/share/backgrounds/<YOUR IMAGE HERE>

### [Example]

[A sample \`xfce4-desktop.xml\` can be viewed by unfolding this block]

     <?xml version="1.0" encoding="UTF-8"?>

     <channel name="xfce4-desktop" version="1.0">



             '''"/>
             '''"/>
             '''"/>

           </property>




               '''"/>
             </property>



               '''"/>
             </property>
           </property>
         </property>
       </property>




         </property>

       </property>
     </channel>

Go to this directory:

[user \$ ][ cd \~/iso-profiles/manjaro/xfce/desktop-overlay/ [COPY TO CLIPBOARD]]

\

Then create `usr/share/backgrounds` and place your Custom Wallpaper at this directory.

[user \$ ][ mkdir ./usr/share/backgrounds [COPY TO CLIPBOARD]]

\

[user \$ ][ cp \~/Pictures/Wallpapers/your-wallpaper.png \~/iso-profiles/manjaro/xfce/desktop-overlay/usr/share/backgrounds [COPY TO CLIPBOARD]]

\

### [profile.conf]

[The full content of an example profile.conf can be viewed by unfolding this block. It is always best to use the latest version instead of copying this one.]

    ##########################################
    ###### use this file in the profile ######
    ##########################################

    # use multilib packages; x86_64 only
    # multilib="true"

    displaymanager="lightdm"

    # Set to false to disable autologin in the livecd
    # autologin="true"

    # nonfree mhwd drivers
    # nonfree_mhwd="true"

    # use extra packages as defined in pkglist to activate a full profile
    #extra="true"

    ################ install ################

    # unset defaults to given value
    # efi_boot_loader="grub"

    # configure calamares for netinstall
    # netinstall="false"

    # configure calamares to use chrootcfg instead of unpackfs
    # chrootcfg="false"

    # use geoip for localization
    # geoip='true'

    # unset defaults to given values
    # names must match systemd service names
    enable_systemd=('avahi-daemon' 'bluetooth' 'cronie' 'ModemManager' 'NetworkManager' 'cups' 'haveged' 'ufw' 'apparmor' 'snapd.apparmor' 'snapd' 'systemd-timesyncd')
    enable_systemd_timers=('fstrim' 'pacman-filesdb-refresh')
    disable_systemd=('pacman-init')

    # add strict snaps: strict_snaps="snapd core core18 gnome-3-28-1804 gtk-common-themes snap-store"
    # strict_snaps=""
    # add classic snaps: classic_snaps="code"
    # classic_snaps=""
    # choose the snap channel. Possible options are: stable, candidate, beta, edge
    # snap_channel="candidate"

    # the same workgroup name if samba is used
    # smb_workgroup=""

    ################# livecd #################

    # unset defaults to given value
    # hostname="manjaro"

    # unset defaults to given value
    # username="manjaro"

    # unset defaults to given value
    # password="manjaro"

    # the login shell
    # defaults to bash
    # login_shell=/bin/bash

    # unset defaults to given values
    # addgroups="lp,network,power,wheel"

    # unset defaults to given values
    # names must match systemd service names
    # services in enable_systemd array don't need to be listed here
    # enable_systemd_live=('manjaro-live' 'mhwd-live' 'pacman-init' 'mirrors-live')
    disable_systemd_live=('tlp' 'tlp-sleep')

    custom_boot_args=('splash')

This config file contains setting options. All default settings are commented. If you want to change them, uncomment them (remove the `#` symbol in front) and change it.

The following settings are noteworthy:

-   `multilib=` setting belongs to the `>multilib` flag in your package lists. multilib will install basic 32bit libraries on 64bit systems. This increases compatibility for 32bit applications on 64bit systems.
-   `displaymanager=` sets the display / login manager your system uses. You need to list your display manager in your package list, too.
-   `kernel=` lets you set the installed kernel. Do **not** include any kernels in your package list! This setting is all you need.
-   `enable_systemd=` let\'s you set systemd services, which get started on the installed system (and with a similar setting on the livecd).

### [Packages-Desktop]

[An example \`Packages-Desktop\` file can be viewed by unfolding this block. It is always best to use the latest version instead of copying this one.]

    ## Network
    avahi
    networkmanager
    networkmanager-openconnect
    networkmanager-openvpn
    networkmanager-pptp
    networkmanager-vpnc
    nss-mdns # NSS support for mDNS (optdepend for avahi)
    ntp
    mobile-broadband-provider-info
    modemmanager
    openresolv
    openssh
    samba
    usb_modeswitch

    ## Libraries for Sound/Audio/Video
    alsa-firmware
    alsa-utils
    ffmpeg
    gst-libav
    gst-plugins-bad
    gst-plugins-base
    gst-plugins-good
    gst-plugins-ugly
    libdvdcss
    >multilib manjaro-alsa
    manjaro-pulse
    pulseaudio-bluetooth
    pulseaudio-ctl
    pulseaudio-zeroconf

    ## Connect Packages
    android-tools
    android-udev
    gvfs
    gvfs-afc
    gvfs-gphoto2
    gvfs-mtp
    gvfs-nfs
    gvfs-smb
    mtpfs
    udiskie
    udisks2

    ## AUR Support/Development
    # Missing base-devel packages
    autoconf
    automake
    binutils
    bison
    fakeroot
    flex
    gcc
    >multilib gcc-libs-multilib
    >multilib gcc-multilib
    libtool
    m4
    make
    patch
    pkg-config
    >multilib lib32-flex
    # Extra packages for AUR support
    >extra git
    >extra patchutils
    >extra subversion

    ## Fonts
    cantarell-fonts
    # noto-fonts             # default font
    # noto-fonts-cjk         # big package, ~76 mb compressed
    # >extra noto-fonts-emoji
    terminus-font
    ttf-bitstream-vera       # xfce4-terminal default Monospace
    # ttf-dejavu             # Installed as gnome-themes-standard dependency
    >extra ttf-inconsolata
    >extra ttf-indic-otf
    >extra ttf-liberation
    >extra ttf-droid

    ## Games
    >extra steam-manjaro

    ## Package management
    pamac
    flatpak

    ## Java
    >extra jdk8-openjdk
    >extra jre8-openjdk-headless
    >extra jre8-openjdk

    ## Printing
    >extra cups
    >extra cups-pdf
    >extra cups-pk-helper
    >extra ghostscript
    >extra gsfonts
    >extra gtk3-print-backends
    >extra hplip
    >extra splix
    >extra system-config-printer

    ## Optional dependencies for hplip
    >extra pyqt5-common # For hplip
    >extra python-pillow # For hplip
    >extra python-pip # For hplip
    >extra python-pyqt5  # For hplip gui
    >extra python-reportlab # For hplip

    ## Display manager
    lightdm
    lightdm-gtk-greeter
    lightdm-gtk-greeter-settings
    accountsservice  # Enhanced user accounts handling

    ## GTK3
    gtk3-classic
    >multilib lib32-gtk3-classic

    ## XFCE Group
    exo-gtk3
    garcon-gtk3
    thunar-gtk3
    thunar-volman
    tumbler
    xfce4-appfinder-gtk3
    xfce4-panel-gtk3
    xfce4-power-manager-gtk3
    xfce4-session-gtk3
    xfce4-settings-gtk3
    xfce4-terminal
    xfconf-gtk3
    xfdesktop-gtk3
    xfwm4-gtk3

    ## XFCE Extras
    blueman
    ffmpegthumbnailer  # tumbler - for video thumbnails
    freetype2          # tumbler - for font thumbnails
    gksu
    gnome-keyring      # fix wlan segfault
    libgsf             # tumbler - for ODF thumbnails
    libopenraw         # tumbler - for RAW thumbnails
    light-locker
    network-manager-applet
    menulibre
    orage
    poppler-glib       # tumbler - for PDF thumbnails
    thunar-archive-plugin
    file-roller
    thunar-media-tags-plugin
    # >extra xfce4-artwork
    xfce4-battery-plugin
    xfce4-clipman-plugin
    >extra xfce4-cpufreq-plugin
    >extra xfce4-cpugraph-plugin
    # xfce4-datetime-plugin
    >extra xfce4-dict
    >extra xfce4-diskperf-plugin
    >extra xfce4-fsguard-plugin
    >extra xfce4-genmon-plugin
    >extra xfce4-mailwatch-plugin
    >extra xfce4-mount-plugin
    >extra xfce4-mpc-plugin
    >extra xfce4-netload-plugin
    >extra xfce4-notes-plugin
    xfce4-notifyd-gtk3
    xfce4-screenshooter
    >extra xfce4-sensors-plugin
    >extra xfce4-smartbookmark-plugin
    >extra xfce4-systemload-plugin
    xfce4-taskmanager
    >extra xfce4-time-out-plugin
    >extra xfce4-timer-plugin
    >extra xfce4-verve-plugin
    >extra xfce4-wavelan-plugin
    >extra xfce4-weather-plugin
    xfce4-whiskermenu-plugin-gtk3
    xfce4-xkb-plugin
    xfce4-pulseaudio-plugin
    pavucontrol

    ## Themes
    >extra manjaro-wallpapers-18.0
    >extra wallpapers-2018
    gnome-icon-theme
    gnome-themes-standard
    grub-theme-manjaro
    matcha-gtk-theme
    xcursor-simpleandsoft
    xcursor-vanilla-dmz-aa

    ## Applications
    >extra catfish
    dmidecode # optional dependency inxi
    engrampa
    >extra firefox
    # >extra flashplugin
    >extra galculator-gtk2
    gcolor2
    >extra gimp
    gparted
    gufw
    >extra audacious
    >extra hexchat
    htop
    qpdfview
    inxi
    >extra libreoffice-still
    ms-office-online
    manjaro-hello
    manjaro-application-utility
    manjaro-settings-manager
    manjaro-settings-manager-notifier
    >basic midori
    >extra mlocate
    mousepad
    mugshot
    >basic parole # media player
    >extra pidgin
    powertop
    screenfetch
    >extra poppler-data  # CKJ support for pdf
    >basic sylpheed # mail client
    >extra thunderbird
    >extra vlc
    >extra viewnior
    >extra xfburn
    >extra yelp

    # Optional dependencies engrampa
    p7zip  # 7Z and ARJ archive support
    unace  # ACE archive support
    unrar  # RAR archive support

    ## Documentation
    manjaro-documentation-en

    ## Settings packages
    >extra manjaro-xfce-gtk3-settings
    >basic manjaro-xfce-gtk3-minimal-settings
    manjaro-browser-settings

    ## Xorg Input Drivers
    xf86-input-elographics
    xf86-input-evdev
    xf86-input-keyboard
    xf86-input-libinput
    xf86-input-mouse
    xf86-input-void

    ## Xorg Server and Graphics
    >multilib lib32-libva-intel-driver
    >multilib lib32-libva-mesa-driver
    >multilib lib32-libva-vdpau-driver
    libva-intel-driver
    libva-mesa-driver
    libva-vdpau-driver
    mesa-demos
    >multilib lib32-mesa-demos
    numlockx
    xdg-user-dirs
    xorg-server
    xorg-twm
    xorg-xinit
    xorg-xkill

    ## Desktop Utils
    perl-file-mimeinfo
    xdg-utils
    xdg-su

    ## Misc
    manjaro-hotfixes

This file contains a list of packages, which will get installed on your installed ISO (XFCE) **and** the LiveCD (the packages in Packages-Live file only get installled on the live ISO). This is a package list with Xfce specific packages (and packages you like to add to your custom Manjaro ISO) of multiple package lists in your ISO profile. The other package lists are more generic.

You can add or remove package names from this list as you like. You do not need to worry about dependencies when adding package names, just make sure the package name is spelled correctly and the package is available in the Manjaro repositories.

`#` marks a comment. The rest of the line after the `#` symbol gets ignored.

### [Adding AUR packages]

If you want to add AUR packages to your ISO, you need to create a online repository and add it to a file **user-repos.conf** beside your **profile.conf**.

**Only use your own http enabled repo.**

    [your-repo-name]
    SigLevel = Optional TrustAll
    Server = http://repo.server.tld/your-repo-name

The article [Buildiso with AUR packages: Using buildpkg](//wiki.manjaro.org/index.php?title=Buildiso_with_AUR_packages:_Using_buildpkg "Buildiso with AUR packages: Using buildpkg") contains more detailed information on this process.

\

# [manjaro-tools.conf]

`manjaro-tools.conf` is the central configuration file for all tools part of *manjaro-tools*. Only edit the general and the \"buildiso\" part to not exceed the scope of this tutorial. If you are not sure what and how to edit it, do **not** edit it. You can always use arguments with the `buildiso` command later.

By default, the systemwide config file is installed in

    /etc/manjaro-tools/manjaro-tools.conf

Best practice is to leave the systemwide file untouched and copy the system wide config to your home directory here:

    ~/.config/manjaro-tools

If the userconfig is present, *manjaro-tools*/*buildiso* will load the userconfig values. Best practice is to leave the systemwide file untouched. By default it is commented and shows just initialization values done in code.

# [Build your ISO]

Build your ISO with the following command:

[user \$ ][ buildiso -p xfce [COPY TO CLIPBOARD]]

\

You need to specify the name of your ISO profile after the `-p` argument. In this case, it is `xfce`.

If the build process fails with an error, start it again.

**Attention:** The build process needs at least 10 minutes to complete or much longer when you are using HDDs, slow CPUs, or large ISOs.

When the build process finishes successfully, the ISO file and the package list will appear in this folder:

    /var/cache/manjaro-tools/iso/

### [Example:]

You can use arguments with the `buildiso` command for more build options:

[user \$ ][ buildiso -f -p xfce -b stable [COPY TO CLIPBOARD]]

\

-   `-f` let\'s you specify if you want the full ISO. If omitted a minimal ISO will be build.
-   `-b` let\'s you specify the branch. You can also set this in your `manjaro-tools.conf` file.

You can find other examples of builds using different arguments for *buildiso* [here](https://wiki.manjaro.org/index.php?title=Manjaro-tools#buildiso).

# [Cleaning your hard drive]

After a successful or failed build, you can get rid of most data (the \"raw\" ISO with all downloaded packages) by deleting this folder:

[user \$ ][ sudo rm -r /var/lib/manjaro-tools/buildiso/ [COPY TO CLIPBOARD]]

\

To clean your system of packages files of packages not installed on your system (this includes all the package files downloaded for your custom ISO):

[user \$ ][ sudo paccache -ruk0 [COPY TO CLIPBOARD]]

\

You can also manually look into

    /var/cache/manjaro-tools/

and delete folders or files to your liking. If you want to delete all ISO images, package lists, and cached Xorg packages do:

[user \$ ][ sudo rm -r /var/cache/manjaro-tools/ [COPY TO CLIPBOARD]]

\

Please remember that all these packages and files are saved for your convenience. If you clean your system like suggested above, you have to download **all** packages and build **all** images again the next time you want to build your own Manjaro ISO.

By default, your `manjaro-tools.conf` file is saved. If you want to delete it, use

[user \$ ][ rm -r \~/.config/manjaro-tools [COPY TO CLIPBOARD]]

\

\

# [][Tips & Tricks]

## [Building a minimal ISO]

A minimal ISO is easy to create by modifying an entry in the profile.conf file. Find the section

     # use extra packages as defined in pkglist to activate a full profile
     # extra="false"
     extra="true"

and remove the **\#** mark in front of **extra = \"false\"** and add a **\#** in front of **extra = \"true\"**.

If you prefer not to change this you can always use the **-f** with buildiso to build a full profile.

# [See also]

-   Source: [Manjaro Gitlab ISO Profiles](https://gitlab.manjaro.org/profiles-and-settings/iso-profiles) (master branch may be unstable - select the branch for latest release)
-   Video: [Building Manjaro ISO by Philip Müller](https://youtu.be/B--je--m0VI)(Tutorial Video)
-   Wiki: [Buildiso with AUR packages: Using buildpkg](//wiki.manjaro.org/index.php?title=Buildiso_with_AUR_packages:_Using_buildpkg "Buildiso with AUR packages: Using buildpkg")