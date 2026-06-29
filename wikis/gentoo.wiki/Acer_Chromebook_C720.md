**Resources**

[[]][Home](https://www.chromebookspecs.com/acer-c720-chromebook-32gb)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Chromebook "wikipedia:Chromebook")

A short guide containing relevant instructions to get Gentoo running on an Acer C720 chromebook.

## Contents

-   [[1] [Preinstallation]](#Preinstallation)
    -   [[1.1] [Firmware wipe]](#Firmware_wipe)
    -   [[1.2] [Developer mode]](#Developer_mode)
    -   [[1.3] [Enable the legacy bootloader]](#Enable_the_legacy_bootloader)
    -   [[1.4] [Loading bootable media]](#Loading_bootable_media)
    -   [[1.5] [Create a backup of the current OS]](#Create_a_backup_of_the_current_OS)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Kernel]](#Kernel)
    -   [[2.2] [Wireless networking]](#Wireless_networking)
    -   [[2.3] [Trackpad configuration]](#Trackpad_configuration)
-   [[3] [Additional information]](#Additional_information)
    -   [[3.1] [Swap partition]](#Swap_partition)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Preinstallation]

### [Firmware wipe]

** Warning**\
It should be noted that there is a chance that Mr. Chromebox\'s script might fail, causing the device to brick.

If the user would like to completely remove Chrome OS from their computer, they can choose to run the Chrome OS Firmware Utility Script written by Mr. Chromebox. However, this script is entirely optional.

** Important**\
Removing the Write-protect is essential to completely remove ChromeOS from the chromebook but will void your warranty. A detailed image of the Chromebook motherboard are listed on the [The Chromium Project\'s Acer C720 & C720P & C740 Chromebook](https://www.chromium.org/chromium-os/developer-information-for-chrome-os-devices/acer-c720-chromebook) page. Disassemble with care.

-   After successfully running this script the remaining [Preinstallation] sections can be skipped. Additionally, the computer is effectively a \"regular\" computer and the [AMD64 Handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64 "Handbook:AMD64") guide can be followed.

### [Developer mode]

In order get lower-level access to the hardware to install Gentoo, it is necessary to put the system into [developer mode](https://sites.google.com/site/chromeoswikisite/home/what-s-new-in-dev-and-beta/developer-mode).

Follow these steps to gain access to developer mode:

1.  Reboot the system to the login screen, then do not login.
2.  At the login screen hold [Esc]+[⟳] (the [F2] key) then press the Power button (top right).
3.  The machine should boot to a special recovery screen, when it gets there press [Ctrl]+[d]. The system will reboot.

### [Enable the legacy bootloader]

1.  Presuming the system in a a powered down state, power up the unit.
2.  When the login screen appears, hold [Ctrl]+[Alt] and press[→]. This should enter the developer console.
3.  Login by entering `chronos` at the prompt, and pressing the [Enter] key.
4.  [sudo bash] to gain a [bash] shell.
5.  [crossystem dev_boot_usb=1 dev_boot_legacy=1]
6.  Type [reboot] and then press [Enter].
7.  The system will reboot again.

### [Loading bootable media]

After downloading a 64-bit minimal installation CD, proceed to make it USB drive bootable with [isohybrid]. Copy the [.iso] image to a USB drive with [dd]:

`root `[`#`]`dd if=/path/to/install-amd64-minimal-.iso of=/path/to/raw/dev/device/file`

1.  Once the dd process is complete, insert the USB to a USB port on the Chromebook.
2.  If the Chromebook was powered down or waiting at the legacy bootload screen, restart the Chromebook by pressing the power button.
3.  At the recovery screen, press [Ctrl]+[l] to load legacy boot options.
4.  The SeaBIOS bootloader should appear prompting a press of the [Esc] key. Press [Esc].
5.  Select the appropriate bootable device by pressing the associated integer number on the keyboard.
6.  The Gentoo ISO Linux prompt should appear. Press [Enter] to boot the minimal CD.

-   If the init process gets stuck, try adding `edd=off` to the kernel command-line parameters.

Once the init process completes the system is ready to receive a Gentoo install!

### [Create a backup of the current OS]

It may be a good idea to create a backup of the Chromebook\'s installation on embedded flash disk (typically [/dev/sda]) before proceeding. If the Chromebook may be transferred to a new owner one day, the backup of the original OS could be restored. After configuring networking and enabling the SSH daemon, something like the following command should suffice:

`root `[`#`]`ssh user@remote "dd if=/dev/sda | gzip -1 -" | dd of=chromebook_image.gz`

This will send the entire contents of [/dev/sda] over the network to the current running directory. Be sure there\'s enough free space in the current partition to receive the file!

To restore the backup, boot the Gentoo minimal install CD again (or alternative live media) and issue:

`root `[`#`]`dd if=chromebook_image.gz | gzip -d | ssh user@local dd of=/dev/sda`

## [Installation]

** Important**\
The following disk options depend on whether the chromebook firmware is stock or was flashed by MrChromebox\'s firmware utility.

-   Continue following the MBR disk partitioning path if the firmware is stock.
-   Continue following either the MBR or GPT disk partitioning paths if the firmware was flashed using MrChromebox\'s firmware utility.

For installation instructions on either MBR or GPT disk partitioning, follow the [AMD64 Handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64 "Handbook:AMD64").

### [Kernel]

[KERNEL] **Enable c720 chromebook support**

    Device Drivers  --->
       [*] Platform support for Chrome hardware  --->
           <*> Chrome OS Laptop
           <*> Chrome OS pstore support
           < > ChromeOS Tablet Switch Controller
           < > Backlight LED support for Chrome OS keyboards

Atheros ath9k wireless card

[KERNEL] **Enable ath9k support**

    Device Drivers  --->
       [*] Network device support --->
          [*] Wireless LAN --->
             [*] Atheros/Qualcomm devices
                [*/ ] Atheros wireless debugging
                   [*/ ] Atheros wireless tracing
                < > Atheros 5xxx wireless cards support
                [ ] Atheros 5xxx PCI bus support
                [*/ ] Atheros bluetooth coexistence support
                <*> Atheros 802.11n wireless cards support
                   [*] Atheros ath9k PCI/PCIe bus support
                   [ ] Atheros ath9k AHB bus support
                   [*/ ] Atheros ath9k debugging
                      [*/ ] Detailed station statistics

Cypress APA I2C touchpad support

[KERNEL] **Enable Cypress APA touchpad support**

    Processor type and features --->
        [*] Intel Low Power Subsystem Support
    Device Drivers  --->
        Input device support --->
           [*] Mice --->
              <*/M> Cypress APA I2C Trackpad support
        I2C support --->
           I2C Hardware Bus support --->
              <*> Synopsys DesignWare Platform
              <*> Synopsys DesignWare PCI

### [Wireless networking]

The setup of wireless networking is detailed in the [wpa supplicant](https://wiki.gentoo.org/wiki/Wpa_supplicant "Wpa supplicant") and [Wifi](https://wiki.gentoo.org/wiki/Wifi "Wifi") articles.

### [Trackpad configuration]

** Important**\
The user must have a basic Xorg environment **before** using or configuring the trackpad. To establish a working Xorg environment follow the gentoo wiki [Xorg/Guide](https://wiki.gentoo.org/wiki/Xorg/Guide "Xorg/Guide").

-   Although the trackpad will work, after enabling required kernel options, in a basic X environment, some users may desire further configuration. A fantastic source with friendly documentation is located in a page of the [Ubuntu manuals](https://manpages.ubuntu.com/manpages/xenial/man4/libinput.4.html). Among other features the manual displays options for disabling the trackpad while typing or tap-to-click.

<!-- -->

-   If users desire disabling the trackpad while typing or enabling tap-to-click, they can download the Acer C720 X*org* configuration file written by github user sedwardsmarsh.

    ::::: cmd-box


    `root `[`#`]`cd /etc/X11/xorg.conf.d/`





    `root `[`#`]`wget https://github.com/sedwardsmarsh/Acer-C720-X-Conf-File/blob/master/47-touchpad.conf`


    :::::

## [Additional information]

### [Swap partition]

-   Since the stock SSD provided in the Acer C720 chromebook is only 16GB, free space is valuable. Space can be saved when creating disk partitions: instead of creating a separate partition for swap space create a swap file instead. This way, the amount required for swap space can be resized when needed.

** Important**\
However, this method doesn\'t guarantee readily available swap space, like a swap partition does.

1.  To create a swap file, run the following command, *Since count=1M equals 512MB, count=8M equals 4,096MB or 4GB.*

    :::: cmd-box


    `root `[`#`]`dd if=/dev/zero of=/swapfile count=8M`


    ::::
2.  Use mkswap to get your file ready for swaping:

    :::: cmd-box


    `root `[`#`]`mkswap /swapfile`


    ::::
3.  Make an fstab entry:

    :::: cmd-box


    `/swapfile none swap sw,loop 0 0`


    ::::
4.  Run as root to activate your file swap space:

    :::: cmd-box


    `root `[`#`]`swapon -a`


    ::::

## [See also]

-   [Power management/Guide](https://wiki.gentoo.org/wiki/Power_management/Guide "Power management/Guide") --- a guide to setup power management features of a laptop.
-   [SSD](https://wiki.gentoo.org/wiki/SSD "SSD") --- provides guidelines for basic maintenance, such as enabling discard/trim support, for **SSD**s ([Solid State Drives](https://en.wikipedia.org/wiki/Solid-state_drive "wikipedia:Solid-state drive")) on Linux.

## [External resources]

-   [swapfile configuration](https://forums.gentoo.org/viewtopic-p-5099313.html) - link to Gentoo Forums post where swap file tutorial was copied from.
-   [https://www.chromium.org/chromium-os/developer-information-for-chrome-os-devices/acer-c720-chromebook](https://www.chromium.org/chromium-os/developer-information-for-chrome-os-devices/acer-c720-chromebook) - A very informative chromium projects page contains information about the Acer C720, C720P, and C740 chromebook models.
-   [https://wiki.archlinux.org/index.php/Acer_C720_Chromebook](https://wiki.archlinux.org/index.php/Acer_C720_Chromebook) - The Acer C720 archlinux wiki page.
-   [https://www.linux.com/learn/how-install-linux-acer-c720-chromebook](https://www.linux.com/learn/how-install-linux-acer-c720-chromebook) - A Linux.com article on installing Ubuntu/Bodhi Linux.