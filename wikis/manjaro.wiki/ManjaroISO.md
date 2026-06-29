Other languages:

[English] • ‎[Türkçe](//wiki.manjaro.org/index.php?title=ManjaroISO/tr "ManjaroISO (26% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=ManjaroISO/ru "ManjaroISO (100% translated)")

## Contents

-   [[1] [What is ManjaroISO?]](#What_is_ManjaroISO.3F)
-   [[2] [How to get started?]](#How_to_get_started.3F)
    -   [[2.1] [Create a work directory]](#Create_a_work_directory)
    -   [[2.2] [Update your system]](#Update_your_system)
    -   [[2.3] [Install ManjaroISO]](#Install_ManjaroISO)
    -   [[2.4] [Understanding ManjaroISO Profiles]](#Understanding_ManjaroISO_Profiles)
    -   [[2.5] [Modifying a ManjaroISO Profile]](#Modifying_a_ManjaroISO_Profile)
    -   [[2.6] [Building 32 bit and 64 bit install-medias]](#Building_32_bit_and_64_bit_install-medias)
-   [[3] [Building an install-media]](#Building_an_install-media)
    -   [[3.1] [Troubleshooting]](#Troubleshooting)
-   [[4] [Links]](#Links)
-   [[5] [Further reading]](#Further_reading)
-   [[6] [See also]](#See_also)

\

**Warning**

------------------------------------------------------------------------

As of March 2015 manjaroiso is deprecated, [Manjaro-tools](//wiki.manjaro.org/index.php?title=Manjaro-tools "Manjaro-tools") is the way!

\

# [][What is ManjaroISO?]

ManjaroISO is a small set of bash scripts that is capable of building fully functional Manjaro Linux based live medias. It is a very generic tool, so it could potentially be used to generate anything from rescue systems, to install disks, to special interest live CD systems, and who knows what else. Simply put, if it involves Manjaro on a shiny coaster, it can do it.

\

# [][How to get started?]

## [Create a work directory]

The first thing you should probably do is create a directory to work in, and cd to it. This\'ll help keep things organized.

     mkdir -p ~/work/manjaroiso

## [Update your system]

To update your system

     sudo pacman -Syu

## [Install ManjaroISO]

Next, install manjaroiso and its profiles. If you do not need the community profiles, do not install their package.

     sudo pacman -S manjaroiso manjaroiso-profiles manjaroiso-community-profiles

Copy ManjaroISOs profiles to your work directory:

     cp -a /usr/share/manjaroiso/configs/ ~/work/manjaroiso/configs/

There is an [Alternative way to install ManjaroISO](//wiki.manjaro.org/index.php?title=Alternative_way_to_install_ManjaroISO "Alternative way to install ManjaroISO") available using `git clone` to download the latest ManjaroISO packages from Github.

## [Understanding ManjaroISO Profiles]

Depending on your ManjaroISO version you find followed directories in \~/work/manjaroiso:

     build  cinnamon  e17  kde  lxde  mate  net  openbox  shared  sysmenu  xfce

In this example we work with the **e17** folder. This folder is not available anymore and got replaced by the **enlightenment** folder, but it serves well for demonstration purposes. All profile folders look very similar. Change to it and take a look at the files and folders in it:

    Packages       isolinux         overlay           pacman-x86_64.conf
    Packages-E17   isomounts        overlay-livecd    syslinux
    Packages-Xorg  mkinitcpio.conf  pacman-gfx.conf   efiboot
    e17-overlay    options.conf     pacman-i686.conf

-   Packages includes the common packages of all editions.
-   Packages-E17 includes all packages especially for the E17 Edition
-   Packages-Xorg includes all common Xorg packages
-   e17-overlay includes files and folders modified to get E17 Edition working
-   isolinux includes isolinux.cfg file to start syslinux bootloader
-   isomounts holds the information of all overlay-images and their bootorder: It tells the kernel in which order (from top to bottom) to load all overlay images
-   mkinitcpio.conf holds the information of all needed modules need to be added to the live-media kernel
-   options.conf defines basic settings for the live-media
-   overlay includes common files and folders modified to get all edition working
-   overlay-livecd includes common files and folders modified for all editions getting the live-session working
-   pacman-gfx.conf includes the common pacman.conf file for pkgs-image overlay
-   pacman-i686.conf includes the common pacman.conf for all 32bit Manjaro Editions
-   pacman-x86_64.conf includes the common pacman.conf for all 64bit Manjaro Editions
-   syslinux includes the bootloader for all Manjaro Editions
-   efiboot includes UEFI bootloader stuff for all Manjaro Editions

## [Modifying a ManjaroISO Profile]

In this example we work with the **e17** folder. Following files and folders are most important for the E17 Profile:

-   Packages-E17
-   e17-overlay

\
Current Packages-E17 file looks like this:

    ### Manjaro Packages

    ## E17 Main Packages
    enlightenment17
    faenza-green-icon-theme
    gksu
    libgnomeui
    lxdm
    network-manager-applet
    system-tools
    xcursor-simpleandsoft
    xcursor-vanilla-dmz-aa

    ## Applications
    blueman
    epdfview
    midori
    mplayer
    gparted
    #manjaro-installer
    sylpheed
    xchat
    xnoise

    ## Packages for Sound and Audio
    gstreamer0.10-bad-plugins
    gstreamer0.10-ffmpeg
    gstreamer0.10-ugly-plugins

    ## Package management
    pacman-gui

You can add any missing package like *connman*, the E17 network manager, to this file and save it. You do not need to worry about dependencies.

Please keep in mind that you can only add packages from the manjaro repositories and **not** from the **AUR**. Read this wiki page, if you want to add packages from the AUR: [How to install AUR packages in ManjaroISO](//wiki.manjaro.org/index.php?title=How_to_install_AUR_packages_in_ManjaroISO&action=edit&redlink=1 "How to install AUR packages in ManjaroISO (page does not exist)")

\
The **e17-overlay** folder looks like this atm:

    e17-overlay
    |-etc
    |---skel
    |-----.config
    |-------epdfview
    |-------gtk-2.0
    |-------midori
    |-----.local
    |-------share
    |---------applications
    |---systemd
    |-----system
    |-usr
    |---share
    |-----icons
    |-------default

It includes configuration files like `etc/systemd/system/display-manager.service` to define the used bootloader. You can change or add any files to that folder to get included to the installed Manjaro system and also added to the live-session if not overwritten by the same file in overlay-livecd.

\
The **overlay-livecd** folder looks like this atm:

    overlay-livecd
    |-etc
    |---gdm
    |---lightdm
    |---manjaro
    |---pam.d
    |---samba
    |---skel
    |-----.config
    |-------autostart
    |-----.kde4
    |-------share
    |---------config
    |-----Desktop
    |---sudoers.d
    |---systemd
    |-----system
    |-------multi-user.target.wants
    |-root
    |---.config
    |-usr
    |---bin
    |---lib
    |-----systemd
    |-------system
    |---sbin
    |---share
    |-----icons

Any file added to this folder gets **only** added to the **live-session**. In some cases, this can be important.

## [Building 32 bit and 64 bit install-medias]

The **options.conf** file found in the *shared* subfolder (in our example: `~/work/manjaroiso/configs/shared/` ) or the subfolder of the desktop environment you are trying to build (in our example: `~/work/manjaroiso/configs/e17/` ) contains the following code:

    arch=`uname -m`
    #arch=i686

This will build a 32bit install-media, if you are on a 32bit Manjaro system and a 64bit install-media, if you are on a 64bit Manjaro system.

If you are on a 64bit Manjaro system and want to build a 32bit install-media, please change the code to this:

    #arch=`uname -m`
    arch=i686

# [Building an install-media]

Please change into the profile folder you want to build, if you have not already done this. In our example this is:

    cd ~/work/manjaroiso/configs/e17/

Now, use buildiso to build your install-media:

     sudo buildiso

buildiso will create a new folder `work-x86_64` or `work-i686` depending on the architecture of the install-media you want to build. buildiso will work in that folder exclusively. When buildiso is finished, the .iso file with your install-media will appear in your profile folder (in our example: `~/work/manjaroiso/configs/e17/` ).

## [Troubleshooting]

In case anything goes wrong buildiso will display an error. Try to fix this error and restart buildiso. If there is a severe error in buildiso or if you want to build a completely new install-media, it might be necessary to delete buildiso\'s work folder. In our example this is (for a 64bit architecture installation-media):

    sudo rm -rfv ~/work/manjaroiso/configs/e17/work-x86_64

**Attention:** The `work-x86_64` folder will **not** be completely deleted, because parts of it are mounted.

In severe cases, please reboot your system before and after you try to remove the `work-x86_64` folder.

# [Links]

-   [Basic Video Tutorial](https://www.youtube.com/watch?v=89TsITpY3h0)
-   [Video tutorial](http://vimeo.com/63063954)

<!-- -->

-   [ManjaroISO Tutorial](https://forum.manjaro.org/index.php?topic=4295.0)

<!-- -->

-   [Manjaro subforum dedicated to ManjaroISO](https://forum.manjaro.org/index.php?board=27.0)

\

# [Further reading]

-   [Alternative way to install ManjaroISO](//wiki.manjaro.org/index.php?title=Alternative_way_to_install_ManjaroISO "Alternative way to install ManjaroISO")
-   [How to install AUR packages in ManjaroISO](//wiki.manjaro.org/index.php?title=How_to_install_AUR_packages_in_ManjaroISO&action=edit&redlink=1 "How to install AUR packages in ManjaroISO (page does not exist)")

# [See also]

-   [manjaro-tools](//wiki.manjaro.org/index.php?title=Manjaro-tools "Manjaro-tools")