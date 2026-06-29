[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**Resources**

[[]][Home](http://www.hardkernel.com/main/products/prdt_info.php?g_code=G143703355573)

**This wiki is describing how to get a working kodi on the framebuffer with video acceleration to work on an Odroid C1+**

## Contents

-   [[1] [Installation of the ground system]](#Installation_of_the_ground_system)
    -   [[1.1] [Prepare the SD card an boot the system]](#Prepare_the_SD_card_an_boot_the_system)
    -   [[1.2] [Preparing the disk]](#Preparing_the_disk)
    -   [[1.3] [Mounting the USB disk and installing the stage archive]](#Mounting_the_USB_disk_and_installing_the_stage_archive)
    -   [[1.4] [Mounting the necessary filesystems]](#Mounting_the_necessary_filesystems)
    -   [[1.5] [Entering the new environment]](#Entering_the_new_environment)
    -   [[1.6] [Downloading the portage-tree and adding some overlays]](#Downloading_the_portage-tree_and_adding_some_overlays)
    -   [[1.7] [Editing make.conf]](#Editing_make.conf)
    -   [[1.8] [Installing the kernel sources and necessary packages]](#Installing_the_kernel_sources_and_necessary_packages)
    -   [[1.9] [Build the kernel]](#Build_the_kernel)
    -   [[1.10] [Install the kernel]](#Install_the_kernel)
    -   [[1.11] [Finish installation]](#Finish_installation)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Java]](#Java)
    -   [[2.2] [Kodi]](#Kodi)

## [Installation of the ground system]

### [Prepare the SD card an boot the system]

At first you must install a linux image to sdcard to boot the odroid. I\'m recommending the [ARM Image](http://archlinuxarm.org/platforms/armv7/amlogic/odroid-c1). Follow the instructions on this site. I\'m descriping how to install Gentoo on an USB hard disc.

I\'m describing here the base steps. For more information see the [Handbook](https://wiki.gentoo.org/wiki/Handbook:X86 "Handbook:X86").

### [Preparing the disk]

At first you must prepare the USB disc at which we install gentoo. You need 2 partitions. A swap an a root partition.

`root `[`#`]`fdisk -l /dev/sda`

    Disk /dev/sda: 74.5 GiB, 80026361856 bytes, 156301488 sectors
    Units: sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disklabel type: dos
    Disk identifier: 0x702c75f2

    Device     Boot   Start       End   Sectors  Size Id Type
    /dev/sda1          2048   4196351   4194304    2G 82 Linux swap / Solaris
    /dev/sda2       4196352 156301311 152104960 72.5G 83 Linux

Now you need a filesystem.

`root `[`#`]`mkswap /dev/sda1 `

`root `[`#`]`mkfs.ext4 /dev/sda2 `

### [Mounting the USB disk and installing the stage archive]

`root `[`#`]`mkdir /mnt/gentoo `

`root `[`#`]`mount /dev/sda2 /mnt/gentoo `

Now download the stage3 archive and extract it.

`root `[`#`]`cd /mnt/gentoo `

`root `[`#`]`wget `[`http://distfiles.gentoo.org/releases/arm/autobuilds/current-stage3-armv7a_hardfp/stage3-armv7a_hardfp-20151025.tar.bz2`](http://distfiles.gentoo.org/releases/arm/autobuilds/current-stage3-armv7a_hardfp/stage3-armv7a_hardfp-20151025.tar.bz2)` `

`root `[`#`]`tar -xjpf stage3-armv7a_hardfp-20151025.tar.bz2 `

### [Mounting the necessary filesystems]

`root `[`#`]`mount -t proc proc /mnt/gentoo/proc `

`root `[`#`]`mount --rbind /sys /mnt/gentoo/sys `

`root `[`#`]`mount --rbind /dev /mnt/gentoo/dev `

`root `[`#`]`mount /dev/mmvblk0p1 /mnt/gentoo/boot `

### [Entering the new environment]

No we enter the new environment.

`root `[`#`]`chroot /mnt/gentoo /bin/bash `

`root `[`#`]`source /etc/profile `

`root `[`#`]`env-update `

### [Downloading the portage-tree and adding some overlays]

To download the portage-tree, type in:

`root `[`#`]`emerge-webrsync`

Now we add 2 overlays which we need for our odroid c1+.

The [odroidc1 overlay](https://github.com/tbe/odroidc1-overlay.git) and the [odroidberry](https://github.com/dsiggi/odroidberry.git) containing the necessary files.

To add the overlays edit [/etc/portage/repos.conf/overlays].

[FILE] **`/etc/portage/repos.conf/overlays`Overlay configuration**

    [odroidberry]
    location = /usr/local/portage/odroidberry
    sync-type = git
    sync-uri = git://github.com/dsiggi/odroidberry
    auto-sync = yes

    [odroidc1-overlay]
    location = /usr/local/portage/odroidc1
    sync-type = git
    sync-uri = git://github.com/tbe/odroidc1-overlay
    auto-sync = yes

Now create the directories for the overlays and sync them

`root `[`#`]`mkdir /usr/local/portage `

`root `[`#`]`emaint sync -a `

### [Editing make.conf]

Here is my sample make.conf. This on should work for you but you can change it your choice.

[FILE] **`/etc/portage/make.conf`Example of my make.conf**

    # These settings were set by the catalyst build script that automatically
    # built this stage.
    # Please consult /usr/share/portage/config/make.conf.example for a more
    # detailed example.
    CFLAGS="-O3 -pipe -march=armv7-a -mtune=cortex-a5 -mfpu=vfpv3-d16 -mfloat-abi=hard"
    CXXFLAGS="$"
    # WARNING: Changing your CHOST is not something that should be done lightly.
    # Please consult http://www.gentoo.org/doc/en/change-chost.xml before changing.
    CHOST="armv7a-hardfloat-linux-gnueabi"
    # These are the USE flags that were used in addition to what is provided by the
    # profile used for building.
    LDFLAGS="-Wl,-O1 -Wl,--as-needed"
    MAKEOPTS="-j5"

    #MAKEOPTS="-j9 -l4" #With distcc and a 4 core server
    #FEATURES="distcc distcc-pump" #For distcc

    USE="bindist -X nls unicode -gles -gles1 -gles2 -egl -opengl"

    PORTDIR="/var/db/repos/gentoo"
    DISTDIR="/var/cache/distfiles"
    PKGDIR="/var/cache/binpkgs"
    PORTDIR_OVERLAY="/usr/local/portage/odroidc1 /usr/local/portage/odroidberry"

    GENTOO_MIRRORS="http://ftp.uni-erlangen.de/pub/mirrors/gentoo"

[FILE] **`/etc/portage/package.use/00localization`**

    */* LINGUAS: de

### [Installing the kernel sources and necessary packages]

Now you can install the kernel, u-boot-tools and dracut.

`root `[`#`]`emerge --ask =odroidc1-sources-3.10.80-r20151008`

`root `[`#`]`emerge --ask u-boot-tools-odroidc1`

`root `[`#`]`emerge --ask dracut`

### [Build the kernel]

Do the following:

`root `[`#`]`cd /usr/src/linux `

`root `[`#`]`make odroidc_defconfig `

Now you have a standard config for your odroid c1+. If you wish you can configure the kernel like you want.

To build the kernel do the following:

`root `[`#`]`make uImage `

`root `[`#`]`make modules `

`root `[`#`]`make dtbs `

`root `[`#`]`make modules_install `

### [Install the kernel]

To install the kernel you must do the following.

`root `[`#`]`dracut --kver 3.10.80-r20151008-odroidc1 `

`root `[`#`]`mkimage -A arm -O linux -T ramdisk -C none -a 0 -e 0 -n "uInitrd 3.10.80-r20151008-odroidc1" -d /boot/initramfs-3.10.80-r20151008-odroidc1.img /boot/uInitrd-gentoo `

`root `[`#`]`cp /usr/src/linux/arch/arm/boot/uImage /boot/uImage-gentoo `

`root `[`#`]`cp /usr/src/linux/arch/arm/boot/dts/meson8b_odroidc.dtb /boot/ `

No edit [/boot/boot.ini] and change the variable \"bootargs\" to match to your root device. Then also change the 2 lines unter \"# Booting\" to match to your uImage and uImagerd.

[FILE] **`/boot/boot.ini`Example of my boot.ini**

    ODROIDC-UBOOT-CONFIG

    # Possible screen resolutions
    # Uncomment only a single Line! The line with setenv written.
    # At least one mode must be selected.

    # setenv m "vga"             # 640x480
    # setenv m "480p"            # 720x480
    # setenv m "576p"            # 720x576
    # setenv m "800x480p60hz"    # 800x480
    # setenv m "800x600p60hz"    # 800x600
    # setenv m "1024x600p60hz"   # 1024x600
    # setenv m "1024x768p60hz"   # 1024x768
    # setenv m "1360x768p60hz"   # 1360x768
    # setenv m "1440x900p60hz"   # 1440x900
    # setenv m "1600x900p60hz"   # 1600x900
    # setenv m "1680x1050p60hz"  # 1680x1050
    # setenv m "720p"            # 720p 1280x720
    # setenv m "800p"            # 1280x800
    # setenv m "sxga"            # 1280x1024
    # setenv m "1080i50hz"          # 1080I@50Hz
    # setenv m "1080p24hz"          # 1080P@24Hz
    # setenv m "1080p50hz"          # 1080P@50Hz
    setenv m "1080p"                # 1080P@60Hz
    # setenv m "1920x1200"       # 1920x1200

    # HDMI DVI Mode Configuration
    setenv vout_mode "hdmi"
    # setenv vout_mode "dvi"

    # HDMI BPP Mode
    setenv m_bpp "32"
    # setenv m_bpp "24"
    # setenv m_bpp "16"

    # HDMI Hotplug Force (HPD)
    # 1 = Enables HOTPlug Detection
    # 0 = Disables HOTPlug Detection and force the connected status
    setenv hpd "0"

    # CEC Enable/Disable (Requires Hardware Modification)
    # 1 = Enables HDMI CEC
    # 0 = Disables HDMI CEC
    setenv cec "0"

    # PCM5102 I2S Audio DAC
    # PCM5102 is an I2S Audio Dac Addon board for ODROID-C1+
    # Uncomment the line below to __ENABLE__ support for this Addon board.
    # setenv enabledac "enabledac"

    # UHS Card Configuration
    # Uncomment the line below to __DISABLE__ UHS-1 MicroSD support
    # This might break boot for some brand models of cards.
    setenv disableuhs "disableuhs"

    # Disable VPU (Video decoding engine, Saves RAM!!!)
    # 0 = disabled
    # 1 = enabled
    setenv vpu "1"

    # Disable HDMI Output (Again, saves ram!)
    # 0 = disabled
    # 1 = enabled
    setenv hdmioutput "1"

    # Default Console Device Setting
    # setenv condev "console=ttyS0,115200n8"        # on serial port
    # setenv condev "console=tty0"                    # on display (HDMI)
    setenv condev "console=ttyS0,115200n8 console=tty0"   # on both

    ###########################################

    if test "$" = "0"; then setenv hdmi_hpd "disablehpd=true"; fi
    if test "$" = "1"; then setenv hdmi_cec "hdmitx=cecf"; fi

    # Boot Arguments
    #ARCH
    #setenv bootargs "root=UUID=e139ce78-9841-40fe-8823-96a304a09859 rootwait ro $ no_console_suspend vdaccfg=0xa000 logo=osd1,loaded,0x7900000,720p,full dmfc=3 cvbsmode=576cvbs hdmimode=$ m_bpp=$ vout=$ $ $ $ $"
    #Gentoo
    setenv bootargs "root=UUID=350cd0e3-6fab-4532-b64b-bdb6994263a5 rootwait ro $ no_console_suspend vdaccfg=0xa000 logo=osd1,loaded,0x7900000,720p,full dmfc=3 cvbsmode=576cvbs hdmimode=$ m_bpp=$ vout=$ $ $ $ $"

    # Booting
    fatload mmc 0:1 0x21000000 uImage-gentoo
    fatload mmc 0:1 0x22000000 uInitrd-gentoo
    fatload mmc 0:1 0x21800000 meson8b_odroidc.dtb
    fdt addr 21800000

    if test "$" = "0"; then fdt rm /mesonstream; fdt rm /vdec; fdt rm /ppmgr; fi

    if test "$" = "0"; then fdt rm /mesonfb; fi

### [Finish installation]

At first you must install a small script to get and output on your screen.

`root `[`#`]`wget `[`https://raw.githubusercontent.com/mdrjr/c1_bootini/master/c1_init.sh`](https://raw.githubusercontent.com/mdrjr/c1_bootini/master/c1_init.sh)` -O /usr/bin/c1_init `

`root `[`#`]`chmod +x /usr/bin/c1_init `

To get the script to work you must install fbset:

`root `[`#`]`emerge --ask fbset`

No we need an init.d-script for it:

[FILE] **`/etc/init.d/c1_init`c1_init.d-script**

    #!/sbin/openrc-run
    # Distributed under the terms of the GNU General Public License v2

    description="Setting up framebuffer"

    depend()

    start()  "Execution of \"c1_init\" failed."
    }

Activating the script:

`root `[`#`]`rc-update add c1_init boot`

Now do all the remaining steps from the Handbook, eg install an cron daemon an editing the config files. Then you can reboot your system.

## [Installation]

### [Java]

Java is required to install Kodi. The official Java implementation ([[[dev-java/oracle-jdk-bin]](https://packages.gentoo.org/packages/dev-java/oracle-jdk-bin)[]]) was used in this guide, although it may be possible to use icedtea with the odroid:

`root `[`#`]`echo "dev-java/oracle-jdk-bin -awt -fontconfig -nsplugin" >> /etc/portage/package.use`

`root `[`#`]`emerge --ask dev-java/oracle-jdk-bin`

### [Kodi]

When using ALSA audio output can be directed to a HDMI sound output *or* a USB soundcard. To use both `pulseaudio` must be enabled.

Add the `alsa` or `pulseaudio` USE flag values to the [/etc/portage/package.use] file.

To be able to shutdown the odroid from kodi and use a keyboard as input device the `dbus`, `upower`, `udisks`, and `usb` USE flags should be enabled. After setting the flags as desired, emerge Kodi:

The `odroidc1` USE flag is necessary to add odroidc1 compatibility.

`root `[`#`]`emerge --ask kodi::odroidberry`