[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Amlogic+TV+boxes&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Amlogic_TV_boxes "Amlogic TV boxes (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Amlogic_TV_boxes/tr "Amlogic TV kutuları (3% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Amlogic_TV_boxes/ru "ТВ-приставки Amlogic (100% translated)")

## Contents

-   [[1] [Amlogic TV boxes]](#Amlogic_TV_boxes)
    -   [[1.1] [General disclaimer and warning]](#General_disclaimer_and_warning)
    -   [[1.2] [Identifying your box]](#Identifying_your_box)
    -   [[1.3] [Installation]](#Installation)
        -   [[1.3.1] [Configure uEnv.ini]](#Configure_uEnv.ini)
        -   [[1.3.2] [Booting from USB]](#Booting_from_USB)
        -   [[1.3.3] [Enable multi-boot mode]](#Enable_multi-boot_mode)
    -   [[1.4] [Reflashing Android]](#Reflashing_Android)
        -   [[1.4.1] [Installing aml-flash-tool]](#Installing_aml-flash-tool)
        -   [[1.4.2] [Reflashing with flash-tool.sh]](#Reflashing_with_flash-tool.sh)
        -   [[1.4.3] [External Amlogic TV box firmware download links]](#External_Amlogic_TV_box_firmware_download_links)
    -   [[1.5] [Rooting Android]](#Rooting_Android)
    -   [[1.6] [dtb files]](#dtb_files)
        -   [[1.6.1] [Recommended .dtb files]](#Recommended_.dtb_files)
        -   [[1.6.2] [Useful device tree commands]](#Useful_device_tree_commands)
        -   [[1.6.3] [dtb/SoC code names]](#dtb.2FSoC_code_names)
    -   [[1.7] [Tips and tricks]](#Tips_and_tricks)
        -   [[1.7.1] [Enable graphics acceleration]](#Enable_graphics_acceleration)
        -   [[1.7.2] [Hardware accelerated video playback]](#Hardware_accelerated_video_playback)
        -   [[1.7.3] [CH340-fan-control]](#CH340-fan-control)
        -   [[1.7.4] [HDMI audio script]](#HDMI_audio_script)
        -   [[1.7.5] [Unbricking]](#Unbricking)

# [Amlogic TV boxes]

## [General disclaimer and warning]

It is possible to install and run Manjaro on several affordable Android TV boxes using Amlogic chipsets such as the S905, S922 and A311 series of processors. These TV boxes can be purchased for a fraction of the price of a similar spec single board computer whilst coming complete with a case, remote and cables but there are a few catches to be aware of.

The Android TV box market is awash with fakes and clones. It has been known for manufacturers to re-use the exact same model name yet use a different WiFi/Bluetooth chipset or use an entirely different SoC. For example, there are at least eight versions of the X96 Air but they all have exactly the same case. The TV box manufacturers rarely if ever provide updates for their Android-based OS\'s and they provide zero support for users wanting to run alternate operating systems so achieving full support for every box is almost impossible.

Physical build quality is another frequent issue with TV boxes, in particular poor thermal designs are quite common. You may have to cut a hole or two in the case and place a USB powered fan over the SoC to get the best performance out of your TV box but this shouldn\'t be required for normal use. Most Amlogic-based TV boxes have proven to be quite reliable.

\

## [Identifying your box]

Under Android, go to **Settings -\> System -\> About phone**

The device name given under **About phone** is often the best one to use to identify your box but you can also run:

[user \$ ][ cat /proc/device-tree/amlogic-dt-id [COPY TO CLIPBOARD]]

\

Under an Android terminal to show your boxes device tree ID.

\

## [Installation]

Manjaro can be installed from and to micro uSD card or USB disk. After installation it is possible to use /boot/install-aml-emmc.sh to copy your installation onto eMMC on some Amlogic TV boxes. Beelink S922x based boxes are known not to currently work with this script and there are likely other models that also won\'t work booting from eMMC so use the script at your own risk.

### [Configure uEnv.ini]

After using a disk imaging tool such as [balenaEthcher](https://www.balena.io) or **gnome-disks** to write one of the [AM6 Plus](https://github.com/manjaro-arm/am6-plus-images) or [GT King Pro](https://github.com/manjaro-arm/gtking-pro-images) Manjaro ARM images to an SD card or USB disk, mount the disk and edit **BOOT_MNJRO/uEnv.ini**. You must edit the line that begins with **dtb_name=** to point to the dtb file that you wish to use to configure your device tree.

If there isn\'t an exact match dtb for your box within the dtbs folder and you can\'t find a suitable dtb on this wiki or in the Manjaro forums then you should try **meson-g12a-x96-max.dtb**, **meson-g12a-sei510.dtb** or **meson-sm1-sei610.dtb** first:

`dtb_name=/dtbs/amlogic/meson-g12a-x96-max.dtb`

### [Booting from USB]

If you are booting Manjaro from a USB disk or via a USB SATA adapter/enclosure, there is a good chance that you will be required to add a **usb-storage.quirks** kernel parameter to the **APPEND** statement in **extlinux.conf** like so:

    APPEND root=PARTUUID=5418e4d8-02 rootflags=data=writeback rw console=ttyAML0,115200n8 console=tty0 no_console_suspend consoleblank=0 fsck.fix=yes fsck.repair=yes net.ifnames=0 quiet splash plymouth.ignore-serial-consoles usb-storage.quirks=152d:1561:u

You must replace **152d:1561** with the correct USB vendor and product IDs for your USB device. You can find these identifiers by running **lsusb** when you have your disk or adapter connected to a Linux box. It is recommended you boot from USB without setting the USB storage quirks parameter where possible.

\

### [Enable multi-boot mode]

If this is your first time attempting to boot from an SD card or USB disk, you must enable multi-boot mode. Insert your Manjaro micro SD card or attach the Manjaro USB disk then hold down the button in the AV port by inserting a paper clip, a pin or something similar and keep it depressed while powering the device on. Keep the button pressed until you see the boot screen of your box. After a few seconds it should reboot off your SD card or USB disk. You are only required to do this once unless you reflash your eMMC.

\

## [Reflashing Android]

In emergency situations, like when Manjaro stops booting due to your bootloader having been modified or corrupted, you may need to reflash Android. If you have a suitable installation image for your box and a USB A to A cable then you can use **aml-flash-tool** to reflash your TV box.

**WARNING** You must back up everything stored on your TV box before flashing an image because all data stored on the eMMC will be wiped. Be careful to only flash images built specifically for your box or you could \'brick\' your box, which means it won\'t boot and you can\'t enable multi-boot mode.

### [Installing aml-flash-tool]

**aml-flash-tool** requires that you install the old (0.1.x) libusb libraries. Debian and Ubuntu users have to install **libusb-dev** whilst Arch and Manjaro Linux users have to install **libusb-compat**.

Clone the **aml-flash-tool** repo:

[user \$ ][ git clone [https://github.com/osmc/aml-flash-tool.git](https://github.com/osmc/aml-flash-tool.git) [COPY TO CLIPBOARD]]

\

Copy **aml_image_v2_packer** and the amlogic **update** program into your path:

[user \$ ][ cp ./aml-flash-tool/tools/linux-x86/\* \~/.local/bin [COPY TO CLIPBOARD]]

\

You are now prepared to run **flash-tool.sh**

### [Reflashing with flash-tool.sh]

Disconnect the power from your TV box and plug a USB A to USB A cable into your TV box. It varies which port to use but usually only one port will work for reflashing. Now insert a pin or similar into the AV hole, depress the button and keep it pressed as you connect the USB A to A cable to your other machine. You will know when your TV box is ready to be flashed with **flash-tool.sh** because you will see an Amlogic device listed when you run **lsusb**.

When you can see your TV box is connected, you can flash it using a command such as:

[user \$ ][ ./flash-tool.sh \--img=X96AIR_Q1000_20210127-2121.img \--parts=all \--wipe \--soc=sm1 [COPY TO CLIPBOARD]]

\

Replacing **X96AIR_Q1000_20210127-2121.img** with the path to the image you wish to flash. You do not need to run **flash-tool.sh** as root.

### [External Amlogic TV box firmware download links]

Download and flash these firmware files at your own risk! These sites and manufacturers are in no way connected to Manjaro and so the Manjaro developers will not provide any support for installing these.

[Firmware for the X96 Air family of boxes.](https://tinhte.vn/thread/tong-hop-cac-ban-firmware-cua-android-tv-box-x96-air.3050996/)

[Turewell firmware for the T95 boxes.](https://www.turewell.com/pages/tvbox-document)

[Evolution TV](https://www.evolutiontv-vs.com/uncategorized/%D0%B1%D0%BB%D0%BE%D0%B3-%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%BD%D1%8B%D1%85-%D1%84%D0%B0%D0%B9%D0%BB%D0%BE%D0%B2.html) has firmware downloads for several TV boxes.

[SLIMBOX](https://forum.xda-developers.com/t/project-slimbox.4152049/) is a custom Android firmware for Amlogic TV boxes.

## [Rooting Android]

Having root access under Android is useful because this lets you copy your dtb file(s). Whilst you cannot use Android dtbs with the Manjaro mainline kernels, you can decompile them to dts files and this info can be useful when customising dts/dtb files that work with your kernel, if you have the skills and time to dedicate towards developing or modifying device tree files.

Some TV boxes come pre-rooted whilst others include an app to easily enable root/sudo access. You can use the Android Root Checker app to test if you have root access. If your TV box doesn\'t offer any root support then you can use **TWRP** and **Magisk** to root it. Note this isn\'t a permanent root solution and you will be required to boot off a Magisk modified SD card to enable root access.

Download the latest [X96 Max (u212) build of TWRP](https://twrp.me/amlogic/amlogicu212.html). This build of TWRP should boot on most Amlogic TV boxes, not just the X96 Max.

Format a micro SD card as FAT32 and copy the twrp image (**twrp-3.5.2_9-0-u212.img**) onto it and rename it to **recovery.img**. Insert the micro SD into your TV box then hold in the multiboot AV button in whilst inserting the power until you see the boot screen. Your TV box should then reboot into TWRP.

Swipe (drag the button with your USB mouse) to allow modifications. On the main **TWRP** menu, choose **Backup**. The only partition we want to backup is the **Boot** partition, which should already be selected. Deselect the **Data** partition if that is auto-selected then click **Select Storage**, choose the **Micro SD card** then swipe to backup the boot partition. It should only take a few seconds before you are given the option to reboot.

Next, install and run [Magisk](https://github.com/topjohnwu/Magisk/releases) under Android. When installing Magisk, choose **Recovery mode** then select the **Select and Patch a File** method. You will then be asked to locate the backup of the boot partition we created with TWRP so navigate to **SD card/TWRP/BACKUPS/1234567890/SOMEDATE/boot.emmc.win** and double-click the boot partition image file then choose **Let\'s go**. Magisk will then patch the ramdisk within the boot image and create a new recovery image called **magisk_patched-something.img** that gets saved to your Android **Downloads** directory. Copy this new image file from **Downloads** onto a micro SD card and rename it **recovery.img** so that you can multiboot from it, rooted.

\

## [dtb files]

A DTB file is a Linux Device Tree Blob. Device Tree Compiler (dtc) converts between the human editable device tree source \"dts\" format and the compact device tree blob \"dtb\" representation usable by the Linux kernel. A DTB file is required on ARM Linux devices to configure and enable certain types of hardware supported by the Linux kernel.

The Ugoo AM6 images use the linux-khadas kernel by default. You are more likely to get your TV box\'s onboard wifi working by installing the linux-odroid kernel instead.

\

### [Recommended .dtb files]

This is a list of Amlogic TV boxes and the dtbs that offer the best support. Please provide a download link if the dtb is not packaged with the Manjaro vim or aml kernel.

\
**A95X F2** - meson-g12a-u200.dtb - Boots but no ethernet, wifi or bluetooth.

**Beelink GT King Pro** - meson-g12b-gtkingpro-pro.dtb or meson-g12b-ugoos-am6.dtb - works with the older **linux-vim** 5.9.y or 5.10.y series and current mainline linux 5.12.y kernels.

**X92 v2** - meson-gxm-q201.dtb

**X96 Air Q1000** - [meson-sm1-sei610-qca9377-bt](https://github.com/danboid/meson-sm1-sei610-qca9377-bt) - Tested with linux-aml kernel 5.12. Working gigabit ethernet, WiFi and HDMI audio. No support for onboard audio or LED display. Onboard bluetooth was working but it has stopped working under recent Manjaro releases.

**X96 Max Plus** - [meson-sm1-x96maxplus-vim100m.dtb](https://drive.google.com/file/d/1yHJFJl2CdAwLfR-3tJKHU4I-B9iB2Iqm/view?usp=sharing) - There are [several versions of the X96 Max Plus](https://4pda.to/forum/index.php?showtopic=1002233&st=9500#entry102780026). This dtb is configured for those with the rtl8822cs WiFi chipset in which case you should get HDMI audio, WiFi, Bluetooth and 100Mb ethernet if you install the rtl8822cs DKMS kernel module package.

### [Useful device tree commands]

Decompile dtb to dts:

[user \$ ][ dtc -I dtb -O dts -o devicetree.dts devicetree.dtb [COPY TO CLIPBOARD]]

\

Compile a dts to a dtb:

[user \$ ][ dtc -O dtb -o devicetree.dtb devicetree.dts [COPY TO CLIPBOARD]]

\

[DTB extractor](https://github.com/PabloCastellano/extract-dtb) - Tool to split a kernel image with appended dtbs into separated kernel and dtb files.

### [][dtb/SoC code names]

This is the dtb naming scheme used for the various Amlogic SoC\'s, which may help you find a working dtb:

    gxbb → S905
    gxl → S905X
    g12a → S905X2
    g12b → S922X
    gxm → S912
    sm1 → S905X3

## [Tips and tricks]

### [Enable graphics acceleration]

Edit **/etc/X11/xorg.conf.d/01-panfrost.conf** and change **AccelMethod** from **none** to **glamor**.

The mesa Mali driver, [Panfrost](https://docs.mesa3d.org/drivers/panfrost.html), is optimised for use under Wayland so you should get better GPU performance using Wayland-based desktops.

\

### [Hardware accelerated video playback]

The **meson-vdec** kernel module offers support for decoding MPEG 1/2/4, h264, h265/HEVC and VP9 in hardware but it currently only seems to work with **mpv** for some codecs up to Full HD / 1080p resolution @ 30 fps, despite the hardware supporting 4K.

[user \$ ][ mpv \--vo=gpu \--hwdec=v4l2m2m-copy \--hwdec=auto videofile [COPY TO CLIPBOARD]]

\

You can add these options to **\~/.config/mpv/mpv.conf** to avoid typing them every time you run **mpv**.

\

### [CH340-fan-control]

[CH340-fan-control](https://github.com/danboid/CH340-fan-control) is a python script to control a USB fan.

\

### [HDMI audio script]

Some users have reported running [g12_sound.sh](https://gitlab.manjaro.org/manjaro-arm/packages/community/oc4-post-install/-/blob/master/g12_sound.sh) has fixed their HDMI audio. If you are having HDMI audio issues, you will likely already have **g12_sound.sh** installed so run the script then:

[user \$ ][ sudo systemctl enable sound [COPY TO CLIPBOARD]]

\

Reboot and test!

\

### [Unbricking]

If you\'ve bricked your AMlogic TV box but suspect the hardware is still OK you could try [creating a bootable recovery uSD card](https://www.cnx-software.com/2016/11/19/how-to-create-a-bootable-recovery-sd-card-for-amlogic-tv-boxes/) to or you could try using the Amlogic burn card maker tool under Windows to re-flash your firmware from a uSD card but I\'ve not had any success with these methods.

The best bet for unbricking your TV box is to search for the location of the maskrom contact pads or pins as you can usually revive your box by [shorting a couple of contact pads or chip legs on the motherboard](https://www.youtube.com/watch?v=OyZJVD5SbSY). This requires opening your TV box which will likely invalidate your warranty, if you have one.