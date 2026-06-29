This page contains [[changes](https://wiki.gentoo.org/index.php?title=Raspberry_Pi_Install_Guide&diff=1433716)] which are not marked for translation.

** Tip**\
This guide is intended to apply to all Raspberry Pis that can boot from removable storage

## Contents

-   [[1] [Overview]](#Overview)
    -   [[1.1] [Hardware table]](#Hardware_table)
    -   [[1.2] [Raspberry Pi Booting]](#Raspberry_Pi_Booting)
-   [[2] [High Level Steps]](#High_Level_Steps)
-   [[3] [Prerequisites]](#Prerequisites)
-   [[4] [The detail]](#The_detail)
    -   [[4.1] [Preparing the disks]](#Preparing_the_disks)
    -   [[4.2] [Installing the Gentoo installation files]](#Installing_the_Gentoo_installation_files)
    -   [[4.3] [Installing the Raspberry Pi Foundation files]](#Installing_the_Raspberry_Pi_Foundation_files)
        -   [[4.3.1] [Fetch the Raspberry Pi Foundation files]](#Fetch_the_Raspberry_Pi_Foundation_files)
        -   [[4.3.2] [Populate boot]](#Populate_boot)
        -   [[4.3.3] [Copy the kernel modules]](#Copy_the_kernel_modules)
        -   [[4.3.4] [Raspberry Pi 5 WiFi/Bluetooth Firmware]](#Raspberry_Pi_5_WiFi.2FBluetooth_Firmware)
            -   [[4.3.4.1] [WIFI]](#WIFI)
            -   [[4.3.4.2] [Bluetooth]](#Bluetooth)
-   [[5] [Recap]](#Recap)
-   [[6] [Minimal Configuration]](#Minimal_Configuration)
    -   [[6.1] [cmdline.txt]](#cmdline.txt)
    -   [[6.2] [config.txt]](#config.txt)
    -   [[6.3] [fstab]](#fstab)
    -   [[6.4] [Networking Information]](#Networking_Information)
    -   [[6.5] [root password]](#root_password)
    -   [[6.6] [conf.d/keymaps]](#conf.d.2Fkeymaps)
    -   [[6.7] [configure sshd]](#configure_sshd)
        -   [[6.7.1] [OpenRC]](#OpenRC)
        -   [[6.7.2] [Systemd]](#Systemd)
-   [[7] [Tidy up and Test in the Pi]](#Tidy_up_and_Test_in_the_Pi)
-   [[8] [IMPORTANT After the First Boot]](#IMPORTANT_After_the_First_Boot)
    -   [[8.1] [ WarningFIX YOUR SECURITY]](#WarningFIX_YOUR_SECURITY)
    -   [[8.2] [Setting portage up]](#Setting_portage_up)
    -   [[8.3] [Making the system time monotonic]](#Making_the_system_time_monotonic)
        -   [[8.3.1] [OpenRC]](#OpenRC_2)
        -   [[8.3.2] [systemd]](#systemd_2)
    -   [[8.4] [CPU governor]](#CPU_governor)
    -   [[8.5] [Clear the install leftovers]](#Clear_the_install_leftovers)
    -   [[8.6] [Fix inittab]](#Fix_inittab)
    -   [[8.7] [CPU Temperature and clock monitoring]](#CPU_Temperature_and_clock_monitoring)
-   [[9] [Everything skipped in the handbook]](#Everything_skipped_in_the_handbook)
    -   [[9.1] [Configuring compile options]](#Configuring_compile_options)
    -   [[9.2] [Chrooting]](#Chrooting)
    -   [[9.3] [Gentoo ebuild repository]](#Gentoo_ebuild_repository)
    -   [[9.4] [Reading news items]](#Reading_news_items)
    -   [[9.5] [Choosing the right profile]](#Choosing_the_right_profile)
    -   [[9.6] [Copy DNS info]](#Copy_DNS_info)
    -   [[9.7] [Mounting the necessary filesystems]](#Mounting_the_necessary_filesystems)
    -   [[9.8] [Entering the new environment]](#Entering_the_new_environment)
    -   [[9.9] [Preparing for a bootloader]](#Preparing_for_a_bootloader)
    -   [[9.10] [Configure locales]](#Configure_locales)
    -   [[9.11] [Selecting mirrors]](#Selecting_mirrors)
    -   [[9.12] [Timezone]](#Timezone)
    -   [[9.13] [Updating the \@world set]](#Updating_the_.40world_set)
    -   [[9.14] [dhcpcd]](#dhcpcd)
    -   [[9.15] [Configuring the Linux kernel]](#Configuring_the_Linux_kernel)
    -   [[9.16] [Filesystem information]](#Filesystem_information)
    -   [[9.17] [System information]](#System_information)
    -   [[9.18] [Installing system tools]](#Installing_system_tools)
    -   [[9.19] [Time synchronization - Important with no RTC]](#Time_synchronization_-_Important_with_no_RTC)
    -   [[9.20] [Filesystem tools]](#Filesystem_tools)
    -   [[9.21] [Networking tools]](#Networking_tools)
    -   [[9.22] [Configuring the bootloader]](#Configuring_the_bootloader)
    -   [[9.23] [Finalizing]](#Finalizing)
-   [[10] [Further Reading]](#Further_Reading)
    -   [[10.1] [Cross compiling]](#Cross_compiling)
    -   [[10.2] [QEMU chroot]](#QEMU_chroot)
    -   [[10.3] [Cross distcc]](#Cross_distcc)
-   [[11] [Random Hints, Tips and Did You Know]](#Random_Hints.2C_Tips_and_Did_You_Know)
    -   [[11.1] [Unreliable USB Attached SCSI]](#Unreliable_USB_Attached_SCSI)
    -   [[11.2] [Enable discard over USB]](#Enable_discard_over_USB)
    -   [[11.3] [www-client/chromium]](#www-client.2Fchromium)
    -   [[11.4] [Widevine DRM]](#Widevine_DRM)
    -   [[11.5] [Default kernel configuration]](#Default_kernel_configuration)
    -   [[11.6] [Zram]](#Zram)
    -   [[11.7] [GPIO]](#GPIO)
-   [[12] [Raspberry Pi 3]](#Raspberry_Pi_3)
    -   [[12.1] [Wifi]](#Wifi_2)
    -   [[12.2] [Bluetooth]](#Bluetooth_2)
-   [[13] [Raspberry Pi 4]](#Raspberry_Pi_4)
-   [[14] [Raspberry Pi 5]](#Raspberry_Pi_5)

## [Overview]

Having produced several arm64 Raspberry Pi install guides, first the the Pi3, then the Pi4, building on one another and the handbook, with the arrival of the Pi5, it\'s becoming a house of cards. A new approach is required.

This Pi install guide aims to cover a general method, rather than a step by step guide. The method will work for any Pi and it will only depend on the handbook for the generic Gentoo things. The method should work for the Pi6 and beyond.

No chrooting into an arm/arm64 environment will be required. It will be installed to a (micro)SD card, including enough setup to boot and login before the arm/arm64 environment is required.

In short, it\'s a Gentoo arm or arm64 stage3 on top of a Raspberry Pi Foundation binary kernel with some text files added to make it work. No target CPU code will be executed during the install.

** Tip**\
This page is already too big. The main page should be essential installation steps only. Steps for the different Pis should be on sub pages. Steps to add functionality (like wifi after first boot) should be sub pages too. The idea is to have all the information easy to find from one page without cluttering the install steps.

\

### [Hardware table]

  -------------------------------- --------- -------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------
  Model                            CPU       Architecture   Stage3
  Raspberry PI Zero                BCM2708   ARM            [ARMv6j stage 3](//gentoo.org/downloads/#arm)
  Raspberry PI (Original)          BCM2708   ARM            [ARMv6j stage 3](//gentoo.org/downloads/#arm)
  Raspberry PI Zero w              BCM2708   ARM            [ARMv6j stage 3](//gentoo.org/downloads/#arm)
  Raspberry PI 2b Before Ver 1.2   BCM2709   ARM            [ARMv7a stage 3](//gentoo.org/downloads/#arm)
  Raspberry PI 2b Ver 1.2          BCM2710   ARM/ARM64      [ARMv7a stage 3](//gentoo.org/downloads/#arm) or [arm64 stage3](//gentoo.org/downloads/#arm64)
  Raspberry PI 3b                  BCM2710   ARM/ARM64      [ARMv7a stage 3](//gentoo.org/downloads/#arm) or [arm64 stage3](//gentoo.org/downloads/#arm64)
  Raspberry PI 3b+                 BCM2710   ARM/ARM64      [ARMv7a stage 3](//gentoo.org/downloads/#arm) or [arm64 stage3](//gentoo.org/downloads/#arm64)
  Raspberry PI Zero 2              BCM2710   ARM/ARM64      [ARMv7a stage 3](//gentoo.org/downloads/#arm) or [arm64 stage3](//gentoo.org/downloads/#arm64)
  Raspberry PI Zero 2 w            BCM2710   ARM/ARM64      [ARMv7a stage 3](//gentoo.org/downloads/#arm) or [arm64 stage3](//gentoo.org/downloads/#arm64)
  Raspberry PI 4b                  BCM2711   ARM/ARM64      [ARMv7a stage 3](//gentoo.org/downloads/#arm) or [arm64 stage3](//gentoo.org/downloads/#arm64)
  Raspberry PI CM4                 BCM2711   ARM/ARM64      [ARMv7a stage 3](//gentoo.org/downloads/#arm) or [arm64 stage3](//gentoo.org/downloads/#arm64)
  Raspberry PI 5                   BCM2712   ARM/ARM64      [ARMv7a stage 3](//gentoo.org/downloads/#arm) or [arm64 stage3](//gentoo.org/downloads/#arm64)
  Raspberry PI CM5                 BCM2712   ARM/ARM64      [ARMv7a stage 3](//gentoo.org/downloads/#arm) or [arm64 stage3](//gentoo.org/downloads/#arm64)
  Raspberry PI 6                   TBD       TBD
  -------------------------------- --------- -------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------

** Tip**\
The CM3 was the first Pi to be fitted with eMMC as a manufacturing option. It requires some extra \'hands on\' steps to make the eMMC externally accessible.

** Note**\
Just because some Pi Zeros are 64 bit capable does not mean that its a good idea.

** Warning**\
It is not possible to copy a running install as files opened for writing will be corrupt in the copy.

### [Raspberry Pi Booting]

The very first Pi can be approximated to a mobile phone chip with an ARM CPU grafted on. [Raspberry_Pi_Install_Guide/Pi Booting](https://wiki.gentoo.org/wiki/Raspberry_Pi_Install_Guide/Pi_Booting "Raspberry Pi Install Guide/Pi Booting")

## [High Level Steps]

In handbook order

-   [Preparing the disks](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Disks "Handbook:AMD64/Installation/Disks")
-   [Installing the Gentoo installation files](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Stage "Handbook:AMD64/Installation/Stage")
-   Installing the Raspberry Pi Foundation files
-   [Configuring the system](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/System "Handbook:AMD64/Installation/System")

\
The handbook uses a working Gentoo Install (the minimal ISO) to perform the install and requires that the host and target for the install are compatible. This guide assumes that the host and target are incompatible. No attempt is made to execute any target code on the install host.

## [Prerequisites]

-   A Raspberry Pi and peripherals
-   Target media for the install
-   A Linux install to write the target media (Random live media will probably work)

## [The detail]

Extra steps to expose the Compute Module eMMC as USB storage before Preparing the disk is possible (only to install directly to eMMC). [Raspberry Pi Install Guide/Exposing the eMMC](https://wiki.gentoo.org/wiki/Raspberry_Pi_Install_Guide/Exposing_the_eMMC "Raspberry Pi Install Guide/Exposing the eMMC")

### [Preparing the disks]

These are standard handbook, outside the chroot steps and have been moved to the [Raspberry Pi Install Guide/Preparing the disks](https://wiki.gentoo.org/wiki/Raspberry_Pi_Install_Guide/Preparing_the_disks "Raspberry Pi Install Guide/Preparing the disks") sub page.

** Warning**\
A blank NVMe card in a CM5/CM5 IO board does not work. The boot loader powers up the NVMe, finds nothing to boot and powers it down again so there is no /dev entry.

### [Installing the Gentoo installation files]

Mount the newly created root filesystem. The traditional mount point is [/mnt/gentoo], which will be used here.

`root `[`#`]`mount /dev/sdi4 /mnt/gentoo`

`root `[`#`]`cd /mnt/gentoo`

Choose the correct stage3 for your Pi from [stage 3 downloads](https://www.gentoo.org/downloads/) or the arm or arm64 sub pages with the help of the [Hardware table](https://wiki.gentoo.org/wiki/Raspberry_Pi_Install_Guide#Hardware_table "Raspberry Pi Install Guide") above.

Readers wanting to try MUSL are welcome to contribute.

Copy the link of your choice from [https://www.gentoo.org/downloads/](https://www.gentoo.org/downloads/) or one of its sub pages. Then [wget] it into [/mnt/gentoo]. Do check the prompt.

This example uses the [stage3-arm64-desktop-openrc] stage3

`/mnt/gentoo #``wget `[`https://distfiles.gentoo.org/releases/arm64/autobuilds/20231015T223200Z/stage3-arm64-desktop-openrc-20231015T223200Z.tar.xz`](https://distfiles.gentoo.org/releases/arm64/autobuilds/20231015T223200Z/stage3-arm64-desktop-openrc-20231015T223200Z.tar.xz)` `

The checks for validating the stage 3 tarball described in the handbook are optional and only serve to authenticate the image contents.

Untar the stage 3. If this is done incorrectly it can destroy your host install.

Do check that the present working directory is [/mnt/gentoo]

`/mnt/gentoo #``ls `

    lost+found  stage3-arm64-desktop-openrc-20231015T223200Z.tar.xz

There is no root filesystem hierarchy there until the next step is complete.

`/mnt/gentoo #``tar xpvf stage3-*.tar.xz --xattrs-include='*.*' --numeric-owner`

The \"v\" tar option writes filenames to the console, which slows things down. It can be omitted.

If all is well, there is a root filesystem hierarchy in [/mnt/gentoo] together with the stage3 than provided it.

`/mnt/gentoo #``ls`

    bin   dev  home  lib64       media  opt   root  sbin                                                 sys  usr
    boot  etc  lib   lost+found  mnt    proc  run   stage3-arm64-desktop-openrc-20231015T223200Z.tar.xz  tmp  var

### [Installing the Raspberry Pi Foundation files]

#### [Fetch the Raspberry Pi Foundation files]

Some workspace and access to boot is required, so mount both [/dev/sdi1] and [/dev/sdi3] in our growing Raspberry Pi root filesystem tree.

`/mnt/gentoo #``mount /dev/sdi1 /mnt/gentoo/boot`

`/mnt/gentoo #``mount /dev/sdi3 /mnt/gentoo/home`

The Pi /home can be used as workspace.

`/mnt/gentoo #``cd /mnt/gentoo/home`

Check that its empty

`/mnt/gentoo/home #``ls`

    lost+found

Fetch the binary kernel and Pi firmware from github

`/mnt/gentoo/home #``git clone --depth=1 `[`https://github.com/raspberrypi/firmware`](https://github.com/raspberrypi/firmware)

This is all the Raspberry Pi Foundation binary code to support the entire family of Raspberry Pis. Even Pi5 support is included.

`/mnt/gentoo/home #``ls firmware/`

    boot  documentation  extra  hardfp  modules  opt  README.md

For a 64 bit install, only boot and modules will be used.

#### [Populate boot]

Copy the content of boot to the vfat partition

`/mnt/gentoo/home #``cp -a firmware/boot/* /mnt/gentoo/boot/`

and verify that it worked

`/mnt/gentoo/home #``ls /mnt/gentoo/boot`

    bcm2708-rpi-b.dtb  bcm2709-rpi-cm2.dtb   bcm2711-rpi-400.dtb     bootcode.bin   fixup.dat        kernel.img        start_cd.elf
    bcm2708-rpi-b-plus.dtb  bcm2710-rpi-2-b.dtb   bcm2711-rpi-4-b.dtb     COPYING.linux  fixup_db.dat     LICENCE.broadcom  start_db.elf
    bcm2708-rpi-b-rev1.dtb  bcm2710-rpi-3-b.dtb   bcm2711-rpi-cm4.dtb     fixup4cd.dat   fixup_x.dat      overlays          start.elf
    bcm2708-rpi-cm.dtb  bcm2710-rpi-3-b-plus.dtb  bcm2711-rpi-cm4-io.dtb  fixup4.dat     kernel_2712.img  start4cd.elf      start_x.elf
    bcm2708-rpi-zero.dtb    bcm2710-rpi-cm3.dtb   bcm2711-rpi-cm4s.dtb    fixup4db.dat   kernel7.img      start4db.elf
    bcm2708-rpi-zero-w.dtb  bcm2710-rpi-zero-2.dtb    bcm2712-rpi-5-b.dtb     fixup4x.dat    kernel7l.img     start4.elf
    bcm2709-rpi-2-b.dtb     bcm2710-rpi-zero-2-w.dtb  boot                    fixup_cd.dat   kernel8.img      start4x.elf

#### [Copy the kernel modules]

Install the kernel modules

`/mnt/gentoo/home #`` cp -a firmware/modules /mnt/gentoo/lib/`

and verify

`/mnt/gentoo/home #``ls /mnt/gentoo/lib/modules/`

    6.1.58+  6.1.58-v7+  6.1.58-v7l+  6.1.58-v8+  6.1.58-v8_16k+

Kernel versions will change with time but the suffixes are probably fixed.

#### [][Raspberry Pi 5 WiFi/Bluetooth Firmware]

** Note**\
The Pi3 and Pi4 also have wifi/bluetooth but require different firmware files

** Warning**\
Working WiFi at first boot also requires userspace tools that cannot be emerged until after the Pi has booted.

To use WIFI and bluetooth, firmware files need to be copied to [/mnt/gentoo/lib/firmware] folder.

##### [WIFI]

1\. Clone wifi firmware repository

`root `[`#`]`git clone --depth=1 `[`https://github.com/RPi-Distro/firmware-nonfree.git`](https://github.com/RPi-Distro/firmware-nonfree.git)

2\. Create [/mnt/gentoo/lib/firmware/brcm] if it doesn\'t exist

`root `[`#`]`mkdir -p /mnt/gentoo/lib/firmware/brcm`

3\. The wifi mode for raspberry pi 5 is **brcmfmc43455**, so we only need to copy files for brcmfmc43455.

`root `[`#`]`cp firmware-nonfree/debian/config/brcm80211/cypress/cyfmac43455-sdio-standard.bin /mnt/gentoo/lib/firmware/brcm/brcmfmac43455-sdio.bin `

`root `[`#`]`cp firmware-nonfree/debian/config/brcm80211/cypress/cyfmac43455-sdio.clm_blob /mnt/gentoo/lib/firmware/brcm/brcmfmac43455-sdio.clm_blob `

`root `[`#`]`cp firmware-nonfree/debian/config/brcm80211/brcm/brcmfmac43455-sdio.txt /mnt/gentoo/lib/firmware/brcm/`

4\. When raspberry pi 5 boots, it looks for firmware names with model name, like raspberry,5-model-b, so we need to create symlinks for the firmware files, make sure you have following symlinks.

`root `[`#`]`ls -l /mnt/gentoo/lib/firmware/brcm/`

    -rw-r--r-- 1 root root 643651 Jan 21 12:20 brcmfmac43455-sdio.bin
    -rw-r--r-- 1 root root   2676 Jan 21 12:18 brcmfmac43455-sdio.clm_blob
    lrwxrwxrwx 1 root root     22 Jan 21 12:23 brcmfmac43455-sdio.raspberrypi,5-model-b.bin -> brcmfmac43455-sdio.bin
    lrwxrwxrwx 1 root root     27 Jan 21 12:23 brcmfmac43455-sdio.raspberrypi,5-model-b.clm_blob -> brcmfmac43455-sdio.clm_blob
    lrwxrwxrwx 1 root root     22 Jan 21 12:24 brcmfmac43455-sdio.raspberrypi,5-model-b.txt -> brcmfmac43455-sdio.txt
    -rw-r--r-- 1 root root   2074 Jan 21 12:19 brcmfmac43455-sdio.txt

##### [Bluetooth]

1\. Clone bluetooth firmware repository

`root `[`#`]`git clone --depth=1 `[`https://github.com/RPi-Distro/bluez-firmware.git`](https://github.com/RPi-Distro/bluez-firmware.git)

2\. Create [/mnt/gentoo/lib/firmware/brcm] if it doesn\'t exist

`root `[`#`]`mkdir -p /mnt/gentoo/lib/firmware/brcm`

3\. For bluetooth, only **BCM4345C0.hcd** is needed.

`root `[`#`]`cp bluez-firmware/debian/firmware/broadcom/BCM4345C0.hcd /mnt/gentoo/lib/firmware/brcm/`

4\. Similarly, we need to create a symlink for raspberry pi 5.

`root `[`#`]`ln -s /mnt/gentoo/lib/firmware/brcm/BCM4345C0.hcd /mnt/gentoo/lib/firmware/brcm/BCM4345C0.raspberrypi,5-model-b.hcd`

** Important**\
You can\'t have wifi for the first boot, network tools must be installed before you can use wifi. **NetworkManager** is recommended to set up wifi.

-   If you have ethernet, you can boot raspberrypi and use ethernet for emerging networkmanager.
-   If not, you can use emerge -pf networkmanager to download all the files you need and copy them to [/mnt/gentoo/var/cache/distfiles/].

## [Recap]

The selected Gentoo stage3 is now installed on top of a universal Raspberry Pi Foundation set of kernels and GPU firmware. The Kernel and GPU firmware will work on any Pi as it is all there and what is required is auto detected at boot.

The stage3 is not so flexible.

This process will work for any Raspberry Pi provided the correct stage3 is selected.

## [Minimal Configuration]

This involves describing the install to the Pi, from the Pi\'s view of the world.

No matter how the install host saw the target SD card, the Pi will see it as [/dev/mmcblk0]. As the files below here will be written on the install host to be read and used by the target, references to the SD card become [/dev/mmcblk0].

Some text files need to be created so that the Pi will boot.

`/mnt/gentoo/home``cd /mnt/gentoo`

\

** Warning**\
There is no leading / on file names below. That would make the commands operate on the host install.

### [cmdline.txt]

`/mnt/gentoo/``nano boot/cmdline.txt`

[FILE] **`/mnt/gentoo/boot/cmdline.txt`cmdline.txt**

    dwc_otg.lpm_enable=0 console=tty root=/dev/mmcblk0p4 rootfstype=ext4 rootwait cma=256M@256M net.ifnames=0

** Tip**\
cmdline.txt must be a single line

** Note**\
If your raspberry pi fails to boot, try mmcblk0p2 instead.

### [config.txt]

[config.txt] is used to enable features, and if missing or empty will prevent a Pi5 from booting.

Documentation regarding [config.txt] options can be found on the [Raspberry Pi website](https://www.raspberrypi.com/documentation/computers/config_txt.html).

`/mnt/gentoo/``nano boot/config.txt`

[FILE] **`/mnt/gentoo/boot/config.txt`config.txt**

    # If using arm64 on a Pi3, select a 64 bit kernel
    arm_64bit=1

    # have a properly sized image
    disable_overscan=1

    # Enable audio (loads snd_bcm2835)
    dtparam=audio=on

    # Enable DRM VC4 V3D (graphics) driver
    dtoverlay=vc4-kms-v3d

### [fstab]

** Important**\
Users installing to a SD card in a USB to SD adapter will find that their /dev/sd\* during install becomes /dev/mmcblk0 at boot time

`/mnt/gentoo/``nano etc/fstab`

[FILE] **`/mnt/gentoo/etc/fstab`fstab**

    # <fs>                  <mountpoint>    <type>          <opts>          <dump>

    #LABEL=boot             /boot           ext4            defaults        1 2
    #UUID=58e72203-57d1-4497-81ad-97655bd56494              /               xfs             defaults                0 1
    #LABEL=swap             none            swap            sw              0 0
    #/dev/cdrom             /mnt/cdrom      auto            noauto,ro       0 0

    /dev/mmcblk0p1          /boot           vfat            noatime,noauto,nodev,nosuid,noexec  1 2
    /dev/mmcblk0p2          swap            swap            defaults                                0 0
    /dev/mmcblk0p3          /home           ext4            noatime,nodev,nosuid,noexec             0 0
    /dev/mmcblk0p4          /               ext4            noatime                                 0 0

### [Networking Information]

Set the [hostname](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/System#Hostname "Handbook:AMD64/Installation/System").

Its not possible to install dhcpcd yet but the Pi will use dhcp to get started anyway.

Delay the dhcpcd install until after the \@world update.

### [root password]

Set the root password hash by editing the shadow file directly Replace the root line with the line shown below.

`/mnt/gentoo/``nano etc/shadow`

[FILE] **`/mnt/gentoo/etc/shadow`root password hash**

    root:$6$xxPVR/Td5iP$/7Asdgq0ux2sgNkklnndcG4g3493kUYfrrdenBXjxBxEsoLneJpDAwOyX/kkpFB4pU5dlhHEyN0SK4eh/WpmO0::0:99999:7:::
    halt:*:9797:0:::::
    ...

This sets the root password to **raspberry**. Don\'t leave it like that.

### [][conf.d/keymaps]

Skip this step if the default QWERTY US keymap works.

`/mnt/gentoo/``nano etc/conf.d/keymaps`

[FILE] **`/mnt/gentoo/etc/conf.d/keymaps`keyboard setting**

    # Use keymap to specify the default console keymap.  There is a complete tree
    # of keymaps in /usr/share/keymaps to choose from.
    #keymap="us"
    keymap="dvorak-uk"

### [configure sshd]

Are you really not going to watch the console before the first login?

`/mnt/gentoo/``nano etc/ssh/sshd_config`

[FILE] **`/mnt/gentoo/etc/ssh/sshd_config`Allow password root logins**

    ...
    #LoginGraceTime 2m
    #PermitRootLogin prohibit-password
    PermitRootLogin yes
    #StrictModes yes
    ...

Add the `PermitRootLogin yes` entry. Its a security hazard, revert that as soon as possible. Adding a ssh key is preferred.

#### [OpenRC]

Start the sshd service at boot time by adding a symbolic link to the default runlevel.

`/mnt/gentoo/``cd /mnt/gentoo/etc/runlevels/default/`

`/mnt/gentoo/etc/runlevels/default``ln -s ../../init.d/sshd sshd`

#### [Systemd]

Start the sshd service at boot time by adding a symbolic link to the service.

`/mnt/gentoo/``cd /mnt/gentoo/etc/systemd/system/multi-user.target.wants`

`/mnt/gentoo/etc/systemd/system/multi-user.target.wants``ln -s ../../../../usr/lib/systemd/system/sshd.service sshd.service`

## [Tidy up and Test in the Pi]

`root `[`#`]`cd `

`root `[`#`]`umount /mnt/gentoo/boot `

`root `[`#`]`umount /mnt/gentoo/home `

`root `[`#`]`umount /mnt/gentoo`

Remove the drive from the install host. Connect to the Pi and power up.

## [IMPORTANT After the First Boot]

### []

** Warning**\
FIX YOUR SECURITY

It a really bad idea to use a root password from the internet - Change it as soon as your Pi boots.

`root `[`#`]`passwd`

and follow the on screen instructions.

Permitting a root password login over ssh is not much better. Use key based authentication or create a normal user with membership of the wheel group, then set up sudo. Key based ssh authentication everywhere is preferred.

Revert the `/etc/ssh/sshd_config` change as soon as possible.

### [Setting portage up]

Unless the system time is approximately correct, web site certificates will appear to be invalid.

Time will start at `Thu Jan 1 00:00:00 -00 1970` every power on.

You can set the system time with

`root `[`#`]`date -s "YYYY-MM-DD HH:MM"`

Afterwards, to configure all the repositories for portage you can run

`root `[`#`]`emerge-webrsync`

### [Making the system time monotonic]

The default `hwclock` is not useful without a battery backed RTC, as the time will reset upon every reboot. This has the ability to break many packages and build systems as the time would stop flowing in a single direction.

To make clock be monotonic the following steps need to be taken

##### [OpenRC]

Remove `hwclock` from the default runlevel and replace it with `swclock`. `swclock` will ensure that time is monotonic by saving the time at shutdown and restoring it at power up.

`root `[`#`]`rc-update add swclock boot`

     * service swclock added to runlevel boot

`root `[`#`]`rc-update del hwclock boot`

     * service hwclock removed from runlevel boot

##### [systemd]

There is no `swclock` for systemd. The recommendation is to just install NTP service and run it. Either you can install and enable it with

`root `[`#`]`emerge -v net-misc/openntpd`

`root `[`#`]`systemctl enable ntpd.service`

`root `[`#`]`systemctl start ntpd.service`

Refer to [NTP for systemd](https://wiki.gentoo.org/wiki/NTP "NTP") for the details.

** Tip**\
Do this every boot until NTP time is available

### [CPU governor]

The Raspberry Pi Foundation binary kernel is built to use the powersave CPU governor by default. That keeps the CPU at the lowest possible clock speed at all times. That\'s a bad choice for Gentoo. Changing it and actually making use of the change, requires a CPU heatsink since the Pi firmware looks after CPU thermal throttling, not the kernel.

`root `[`#`]`cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor`

    powersave

Make the file `/etc/local.d/cpu_gov.start` to set the schedutil CPU governor.

`root `[`#`]`nano /etc/local.d/cpu_gov.start`

[FILE] **`/etc/local.d/cpu_gov.start`Set schedutil as CPU governor**

    #!/bin/bash
    echo schedutil > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor

    # fixes all 4 CPUs

make it an executable file.

`root `[`#`]`chmod +x /etc/local.d/cpu_gov.start`

### [Clear the install leftovers]

The stage 3 file in / and the firmware in /home are no longer required and may be removed.

### [Fix inittab]

The stage3 tries to spawn agetty on the serial port at /dev/ttyAMA0 but the serial port is not set up or needed here. Console users will see repeated postings \"INIT: Id \"f0\" respawning too fast: disabled for 5 minutes\" every 5 minutes. To stop the repeated postings, disable agetty on the port by commenting out the last line of /etc/inittab and marking your edit as follows

`localhost #``nano /etc/inittab`

[FILE] **`/etc/inittab`inittab**

    # Architecture specific features
    # [date][your id]: disabling as not needed for Raspberry Pi
    # f0:12345:respawn:/sbin/agetty 9600 ttyAMA0 vt100

### [CPU Temperature and clock monitoring]

`localhost #``cat /sys/class/thermal/thermal_zone0/temp `

    60374

Temp in milliCelcius or 60.374 Deg C.

`localhost #``cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq `

    1500000

CPU clock in kHz. or 1.5GHz

## [Everything skipped in the handbook]

Not quite everything as some steps need to be omitted by design and others have already been accomplished by other means.

Until NTP is installed and configured, at every boot, time will be set from swclock, that is, the time at the last power off. Correct operation of https:// requires reasonably accurate time, so use date -s to set the time at every boot. This avoids \"Certificate not valid errors\" from the web.

The ordering is not the same as the handbook as some steps require packages to be installed and used. That requires a working emerge command. In turn that requires the ::gentoo repo to be installed.

### [Configuring compile options]

** Important**\
`/mnt/gentoo` is not required in path names as the Pi has already booted. Some of the steps below are intended to be performed outside of the chroot

Setting `COMMON_FLAGS` requires a working portage and is covered below

`COMMON_FLAGS="-march=native ... `should be avoided on arm and arm64 systems.

### [Chrooting]

This step has been avoided by design.

### [Gentoo ebuild repository]

Fetch the [::gentoo repo](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Installing_a_Gentoo_ebuild_repository_snapshot_from_the_web "Handbook:AMD64/Installation/Base") snapshot from the web and update it.

** Tip**\
We will use emerge to install some tools to provide data for the setup. emerge won\'t work without the ::gentoo repo, order matters.

### [Reading news items]

Continue with [reading the news](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Reading_news_items "Handbook:AMD64/Installation/Base").

** Important**\
Missing some news, or not acting on it, can render the install unbootable

so it really is important that reading the news is a part of regular updates.

### [Choosing the right profile]

The stage3 will have a profile already set. Follow [choosing a profile](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Choosing_the_right_profile "Handbook:AMD64/Installation/Base") to review and change it.

The profile will have /arm/ in its name for 32 bit installs or /arm64/ for 64 bit installs, not amd64 as illustrated. Arm64 does not support multilib, so that is not an option

### [Copy DNS info]

The Pi is using the default DHCP to obtain DNS information so this step is not required unless networking is reconfigured later.

### [Mounting the necessary filesystems]

Not Required. This step is preparation for chrooting.

### [Entering the new environment]

Not Required. This step is entering the chroot.

### [Preparing for a bootloader]

Already complete. The Pi has booted.

### [Configure locales]

Follow [configure locales](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Configure_locales "Handbook:AMD64/Installation/Base") to configure and select the system locales.

### [Selecting mirrors]

Copy `GENTOO_MIRRORS` from make.conf on the install host, or follow [Selecting mirrors](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Optional:_Selecting_mirrors "Handbook:AMD64/Installation/Base") on the Pi.

Follow [configuring the Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Gentoo_ebuild_repository "Handbook:AMD64/Installation/Base").

** Important**\
The handbook performs this step before the chroot. The [/mnt/gentoo] part of the pathnames must not be used on the pathnames

### [Timezone]

Follow [Setting the timezone](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Timezone "Handbook:AMD64/Installation/Base").

** Important**\
Some networking configurations, such as wifi, require the correct time to be set. Failure to set the timezone may result in interrupted network connectivity.

### [][Updating the \@world set]

The handbook lists [updating \@world](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Updating_the_.40world_set "Handbook:AMD64/Installation/Base") next. That can cause rebuilds due to changed USE settings later. Users building on the Pi may choose to configure the [USE settings](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Configuring_the_USE_variable "Handbook:AMD64/Installation/Base") first, as this may save some rebuilds.

The `VIDEO_CARDS` variable is internally to portage, a USE flag too. Users intending to install a GUI set [VIDEO_CARDS](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#VIDEO_CARDS "Handbook:AMD64/Installation/Base") now.

Only fbdev, v3d and vc4 are useful on a Pi.

The tool cited in [CPU_FLAGS](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#CPU_FLAGS_.2A "Handbook:AMD64/Installation/Base") will emit CPU_FLAGS_ARM. That\'s used on both arm and arm64.

`root `[`#`]`emerge -av app-misc/resolve-march-native`

Then run it. A Pi Zero W reports.

`root `[`#`]`resolve-march-native`

    -march=armv6kz+fp

** Note**\
The BCM2708/BCM2835 contains a arm1176jzf-s core (built on the armv6 architecture) which includes a Variable Floating Point unit v2 (VFP).\
The following CFLAGS work with the Raspberry Pi (Original) and Raspberry Pi Zero W:

    -march=armv6kz+fp -mcpu=arm1176jzf-s -mtune=arm1176jzf-s -mfpu=vfp -mfloat=hard

A Pi 3 reports.

`root `[`#`]`resolve-march-native`

    -mcpu=cortex-a53+crc

** Note**\
There is no -march setting

A Pi 4 reports.

`root `[`#`]`resolve-march-native`

    -mcpu=cortex-a72+crc

** Note**\
There is no -march setting

A Pi 5 reports.

`root `[`#`]`resolve-march-native`

    -mcpu=cortex-a76+crc+crypto

\
Use the output in `COMMON_FLAGS`. Add `-OX -pipe` where X is the selected optimisation level. `-O3` should probably be avoided on RAM constrained systems, like the Pi.

** Note**\
`-mtune` defaults to -mcpu if it is unset which breaks [[[media-libs/libvpx]](https://packages.gentoo.org/packages/media-libs/libvpx)[]] and probably others.

Set -mtune=\<CPU without the optional extras\>

e.g. `COMMON_FLAGS="-mcpu=cortex-a76+crc+crypto -mtune=cortex-a76 -O2 -pipe"` for a Pi5.

With `USE`, `VIDEO_CARDS`, `COMMON_FLAGS`, and `CPU_FLAGS_ARM` all set, its time to actually update the \@world set \... or maybe not.

Users wishing to run the \@world update remotely will need to install [[[app-misc/screen]](https://packages.gentoo.org/packages/app-misc/screen)[]] or [[[app-misc/tmux]](https://packages.gentoo.org/packages/app-misc/tmux)[]] first.

`root `[`#`]`emerge -uDUav --jobs=2 --keep-going @world`

Portage will warn

** Warning**\
\* Determining the location of the kernel source code

-   Unable to find kernel sources at /usr/src/linux
-   Please make sure that /usr/src/linux points at your running kernel,
-   (or the kernel you wish to build against).

which is expected as no kernel source tree is installed.

ebuilds are unable to run kernel configuration checks.

### [dhcpcd]

Follow [Network settings](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/System#Network "Handbook:AMD64/Installation/System").

** Note**\
This step was deliberately delayed until the Pi was booted

### [Configuring the Linux kernel]

Not required as this guide installs the Raspberry Pi Foundation binary kernel. There are no kernel sources installed to configure.

At the time of writing, only the Pi 4 can use the upstream kernel. Pi 5 is being upstreamed, so will be able to at some time in the future.

The other Pis depend on patches that will not (or cannot) be upstreamed.

Users intent on building a kernel should follow [Raspberry Pi official documentation](https://www.raspberrypi.com/documentation/computers/linux_kernel.html). Building a kernel on a Pi takes considerable time, therefore setting up a [crossdev toolchain](https://wiki.gentoo.org/wiki/Crossdev "Crossdev") and cross-compiling the kernel will save time.

For reference on a Pi 5, build times for a \`bcm2712_defconfig\` kernel can take from 40 - 60 minutes, depending on other tasks the Pi is also running. Older Pi models take considerably longer which makes the use of cross-compiling more time efficient.

### [Filesystem information]

[/etc/fstab] is already complete.

-   Networking information

### [System information]

Follow [System information](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/System#System_information "Handbook:AMD64/Installation/System")

### [Installing system tools]

Follow [Installing system tools](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Tools "Handbook:AMD64/Installation/Tools").

** Tip**\
File indexing may not be useful as it\'s very slow.

### [Time synchronization - Important with no RTC]

Follow [Time synchronization](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Tools#Time_synchronization "Handbook:AMD64/Installation/Tools").

### [Filesystem tools]

Follow [Filesystem tools](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Tools#Filesystem_tools "Handbook:AMD64/Installation/Tools"). Both sys-fs/e2fsprogs and sys-fs/dosfstools are required.

Choices for the root filesystem are limited by the filesystems built into the Raspberry Pi Foundation binary kernel.

Readers that can build their own kernel or kernel and initrd before the first boot, can use whatever root filesystem they choose.

### [Networking tools]

Follow [Networking tools](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Tools#Networking_tools "Handbook:AMD64/Installation/Tools").

Wireless networking tools are required but not sufficient to use WiFi. The kernel drivers are present but the firmware is not.

** Tip**\
Users of USB WiFi dongles will need the tools described here too.

### [Configuring the bootloader]

The Pi uses [/boot/config.txt] and [/boot/cmdline.txt]

Both are read by the GPU code at boot time. Reboot to test new configurations

### [Finalizing]

Follow [Finalizing](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Finalizing "Handbook:AMD64/Installation/Finalizing").

## [Further Reading]

### [Cross compiling]

Once a cross toolchain is installed, pure cross compiling then installing the resulting binary packages is only a small step away.

It\'s not a silver bullet. Some packages have broken build systems, so that they are not cross compile aware. Others are cross compile hostile, as they build code for the target during the build then continue by attempting to execute it on the build host.

See the [Crossdev](https://wiki.gentoo.org/wiki/Crossdev "Crossdev") guide.

### [QEMU chroot]

A [QEMU chroot](https://wiki.gentoo.org/wiki/Embedded_Handbook/General/Compiling_with_qemu_user_chroot "Embedded Handbook/General/Compiling with qemu user chroot") allows the build host to emulate (at the register level) the target CPU. It can bring the build hosts RAM, HDD space and CPU cores to bear but at reduced speed, due to the requirement to emulate the target CPU in software.

Its also possible to use cross distcc running on the host (outside the QEMU chroot) from inside the chroot. This exchanges the host CPU cycles required to emulate gcc with host CPU cycles for network emulation.

### [Cross distcc]

That\'s ordinary [distcc](https://wiki.gentoo.org/wiki/Distcc "Distcc") with a [cross compiler](https://wiki.gentoo.org/wiki/Cross_build_environment "Cross build environment") on the helpers. See also [distcc cross compiling](https://wiki.gentoo.org/wiki/Distcc/Cross-Compiling "Distcc/Cross-Compiling").

** Warning**\
Cross distcc is only included here for completeness. The gains are not what may be expected and its not problem free either.

Only compiling is distributed. The Pi still performs the configure and link steps. Not everything can be distributed.

Do set up and test standard distcc before adding cross compiler(s). It will make debug easier.

Keeping versions of gcc in sync is a manual process which distcc cannot check.

## [][Random Hints, Tips and Did You Know]

### [Unreliable USB Attached SCSI]

If you have a Raspberry Pi 4 and are getting bad speeds transferring data to/from USB3.0 SSDs or seeing USB disconnects/resets with USB3.0 to SATA adapters (`uas_eh_device_reset_handler` in [dmesg]), this could be due to your device not properly implementing the [[][[[USB Attached SCSI (UAS)]](https://en.wikipedia.org/wiki/USB_Attached_SCSI "wikipedia:USB Attached SCSI")[][[USB Attached SCSI []](https://en.wikipedia.org/wiki/USB_Attached_SCSI "wikipedia:USB Attached SCSI")]][[[][0]]]] specification. Refer to [STICKY: If you have a Raspberry Pi 4 and are getting bad speeds transferring data to/from USB3.0 SSDs, read this](https://forums.raspberrypi.com/viewtopic.php?t=245931) and [#3070 USB3.0 to SATA adapter causes problems](https://github.com/raspberrypi/linux/issues/3070).

### [Enable discard over USB]

[SSD/NVMe over USB](https://wiki.gentoo.org/wiki/Discard_over_USB "Discard over USB") users only. Trimming SD cards works by default, provided the SD card supports trim.

### [][www-client/chromium]

Given at least 1G of swap, its possible to emerge www-client/chromium on an 8G Pi 4.

`root `[`#`]`genlop -t chromium`

     * www-client/chromium

         Thu Oct 26 23:08:54 2023 >>> www-client/chromium-119.0.6045.21
           merge time: 3 days, 10 hours, 26 minutes and 57 seconds.

but it will probably be out of date by the time the emerge completes.

### [Widevine DRM]

Digital Rights Management for Chromium and Firefox on arm64. Not required on 32 bit installs.

Install [[[sys-fs/squashfs-tools]](https://packages.gentoo.org/packages/sys-fs/squashfs-tools)[]] as the widevine-installer script needs it.

`root `[`#`]`emerge sys-fs/squashfs-tools`

`root `[`#`]`git clone `[`https://github.com/AsahiLinux/widevine-installer`](https://github.com/AsahiLinux/widevine-installer)

as it has to be run as root anyway.

`root `[`#`]`cd widevine-installer`

and read the widevine-installer script. Satisfy yourself that it will not do anything nasty beyond downloading a widewine squashfs image, unpacking and installing it for both Chromium and Firefox.

`root `[`#`]`./widevine-installer`

to install widevine and configure both Chromium and Firefox to use it.

If the browser(s) are already running, log out and back in again.

### [Default kernel configuration]

`root `[`#`]`modprobe configs`

will provide [/proc/config.gz] which is the configuration file for the running kernel.

### [Zram]

Users with small SD cards may want to consider [zram](https://wiki.gentoo.org/wiki/Raspberry_Pi4_64_Bit_Install#Zram "Raspberry Pi4 64 Bit Install") which is a compressed area of ram for swap and other frequently written things. The idea being to avoid SD card writes.

### [GPIO]

For most things related to the GPIO pins, please see [Raspberry_Pi_Install_Guide/Raspberry_Pi_GPIO](https://wiki.gentoo.org/wiki/Raspberry_Pi_Install_Guide/Raspberry_Pi_GPIO "Raspberry Pi Install Guide/Raspberry Pi GPIO").

## [Raspberry Pi 3]

TODO Include the [Pi3 specific parts](https://wiki.gentoo.org/wiki/Raspberry_Pi_3_64_bit_Install "Raspberry Pi 3 64 bit Install") here, then deprecate that page.

** Note**\
Only tested on a Raspberry Pi 3 Model B Plus Rev 1.3

### [Wifi]

There is nothing to track down. The firmware is in [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]]. As always, a method of dealing with the wifi encryption is required.

### [Bluetooth]

The defaults tell

    [   11.495833] Bluetooth: hci0: BCM: firmware Patch file not found, tried:
    [   11.495864] Bluetooth: hci0: BCM: 'brcm/BCM4345C0.raspberrypi,3-model-b-plus.hcd'
    [   11.495875] Bluetooth: hci0: BCM: 'brcm/BCM4345C0.hcd'
    [   11.495884] Bluetooth: hci0: BCM: 'brcm/BCM.raspberrypi,3-model-b-plus.hcd'
    [   11.495894] Bluetooth: hci0: BCM: 'brcm/BCM.hcd'

BCM4345C0.hcd is available from \[[Debian](https://salsa.debian.org/bluetooth-team/bluez-firmware/-/blob/debian/sid/debian/firmware/broadcom/BCM4345C0.hcd?ref_type=heads%7C)\]

## [Raspberry Pi 4]

TODO Include the [Pi4 specific](https://wiki.gentoo.org/wiki/Raspberry_Pi4_64_Bit_Install "Raspberry Pi4 64 Bit Install") parts here, then deprecate that page.

## [Raspberry Pi 5]

The Raspberry Pi 5 specific items have moved the [Raspberry_Pi_Install_Guide/Pi5](https://wiki.gentoo.org/wiki/Raspberry_Pi_Install_Guide/Pi5 "Raspberry Pi Install Guide/Pi5") subpage.