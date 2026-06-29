**Resources**

[[]][Home](http://www.asus.com/Tablets/Eee_Pad_Transformer_Prime_TF201/)

**Installing Gentoo on the Asus Transformer Prime (TF201)**

This is an introduction to installing gentoo on the Asus Transformer Prime (TF201). At the moment, we can get it to boot and launch X, but there are quite a few problems. Hopefully, this site will invite others to share their own experiences, and maybe even generate some solutions to these problems.

## Contents

-   [[1] [News]](#News)
-   [[2] [Installation instructions]](#Installation_instructions)
    -   [[2.1] [Preliminaries]](#Preliminaries)
    -   [[2.2] [Create Gentoo chroot]](#Create_Gentoo_chroot)
        -   [[2.2.1] [Create from stage 3]](#Create_from_stage_3)
        -   [[2.2.2] [Do the chroot]](#Do_the_chroot)
        -   [[2.2.3] [Configure Gentoo via chroot]](#Configure_Gentoo_via_chroot)
    -   [[2.3] [Installing root_chooser]](#Installing_root_chooser)
        -   [[2.3.1] [Configure root_chooser]](#Configure_root_chooser)
        -   [[2.3.2] [flashing the boot.blob]](#flashing_the_boot.blob)
            -   [[2.3.2.1] [Fastboot method]](#Fastboot_method)
            -   [[2.3.2.2] [diskdump method on device]](#diskdump_method_on_device)
            -   [[2.3.2.3] [Nvflash method]](#Nvflash_method)
    -   [[2.4] [Generate a test.blob]](#Generate_a_test.blob)
        -   [[2.4.1] [Compile the host kernel]](#Compile_the_host_kernel)
        -   [[2.4.2] [compile kernel_chooser and create initrd]](#compile_kernel_chooser_and_create_initrd)
        -   [[2.4.3] [make the blob]](#make_the_blob)
-   [[3] [Gentoo Configuration]](#Gentoo_Configuration)
    -   [[3.1] [Network / Wifi]](#Network_.2F_Wifi)
    -   [[3.2] [Update gentoo]](#Update_gentoo)
    -   [[3.3] [Sound]](#Sound)
    -   [[3.4] [xorg-server with fbdev]](#xorg-server_with_fbdev)
    -   [[3.5] [Proprietary Nvidia Tegra 3 driver]](#Proprietary_Nvidia_Tegra_3_driver)
        -   [[3.5.1] [Automatic]](#Automatic)
        -   [[3.5.2] [Manual]](#Manual)
    -   [[3.6] [Sandbox]](#Sandbox)
    -   [[3.7] [OpenTegra driver]](#OpenTegra_driver)
    -   [[3.8] [Keyboard]](#Keyboard)
    -   [[3.9] [Atmel Maxtouch touchscreen]](#Atmel_Maxtouch_touchscreen)
    -   [[3.10] [Battery]](#Battery)
    -   [[3.11] [Touchpad]](#Touchpad)
-   [[4] [Known bugs]](#Known_bugs)
-   [[5] [Tips]](#Tips)
-   [[6] [Contribute]](#Contribute)

## [News]

Created a mailing list: [linux-tf201](https://groups.google.com/group/linux-tf201). Please join! Discussion is not limited to just Gentoo.

The formerly called programm root_chooser has been renamed to kernel_chooser. kernel_chooser is installed via blob as bootloader to the TF201 and can start android directly. If you want to start to linux you need root_chooser in addition. That means kernel_chooser starts root_chooser and root chooser starts linux. Thats it.

There is another loader programm android_chooser. It should start android-like and cyanogenmod-based operating systems like Ubuntu Touch and Sailfish OS.

**State of this site:**

    2.3.1 configure rootchooser is OUT-OF-DATE

Updates:

    04.2015
     * Sandbox.
     * Small typos.
    03.2015
     * 2.2.3 Configure gentoo via chroot
     * 3.1 Network / Wifi
     * 3.2 Update gentoo
     * 3.3 Sound
     * 3.4 xorg-server with fbdev
     * 3.5 Proprietary Nvidia Tegra 3 driver
     * 3.7 Installing Xfce4
    02.2015
     * 2.2 Create gentoo chroot
     * 2.4 Generate a test.blob
     * 2.3.2 flashing the boot.blob (minor changes)

## [Installation instructions]

The basic steps are as follows:

### [Preliminaries]

This guide requires the Jelly Bean bootloader from ASUS, and will assume you already have it installed. This guide is a work in progress: check back often for updates! (Check the history.)

** Warning**\
We are not responsible for any damage done to your TFP!

### [Create Gentoo chroot]

We describe how you set up a Gentoo for your TF201.

#### [Create from stage 3]

The first thing you\'ll want to do is generate a gentoo \"rootFS\". You can either do this by using a [cross-compiler](https://wiki.gentoo.org/wiki/Embedded_Handbook "Embedded Handbook") on another computer or on the TFP within a chroot environment. This guide assumes that you are doing the latter. It further assumes that you will be installing the rootFS on the microSD card (mmcblk1p1) which you have mounted on the TFP in the directory /sdcard/gentoo.

Follow the standard Gentoo Installation Guide. You should use the [armv7a-hardfp](http://distfiles.gentoo.org/releases/arm/autobuilds/current-stage3-armv7a_hardfp/) stage3.

This the method if you will do it on your TP via chroot.

`root `[`#`]`cd /sdcard `

`root `[`#`]`wget http://distfiles.gentoo.org/releases/arm/autobuilds/current-stage3-armv7a_hardfp/stage3-armv7a_hardfp-<date>.tar.bz2 `

`root `[`#`]`mkdir gentoo `

`root `[`#`]`sudo mount -t ext4 /dev/block/mmcblk1p1 /sdcard/gentoo `

`root `[`#`]`cd gentoo/ `

`root `[`#`]`tar -xvjf ../stage3-armv7a_hardfp-<date>.tar.bz2 `

`root `[`#`]`cd .. `

`root `[`#`]`sudo umount gentoo/ `

#### [Do the chroot]

Changeroot to gentoo on the microSD card. You will also need to establish [/etc/resolv.conf] by hand, by adding \"nameserver x.x.x.x\" to use it inside the chroot. You can get the in Android by running getprop. I found that mounting [/dev/pts] to [/sdcard/gentoo/dev/pts] before you chroot allows tmux to work.

Mount all you may need.

`root `[`#`]`mount -t ext4 /dev/block/mmcblk1p1 /sdcard/gentoo `

`root `[`#`]`busybox mount -o bind /dev /sdcard/gentoo/dev `

`root `[`#`]`busybox mount -o bind /dev/pts /sdcard/gentoo/dev/pts `

`root `[`#`]`busybox mount -o bind /sys /sdcard/gentoo/sys `

`root `[`#`]`busybox mount -t proc /proc /sdcard/gentoo/proc `

Configure all files to have a connection to the internet.

`root `[`#`]`sysctl -w net.ipv4.ip_forward=1 `

`root `[`#`]`echo "nameserver 8.8.8.8" > /sdcard/gentoo/etc/resolv.conf # google DNS-Server for simplicity `

`root `[`#`]`echo "nameserver 8.8.4.4" >> /sdcard/gentoo/etc/resolv.conf # google DNS-Server for simplicity `

`root `[`#`]`echo "127.0.0.1 localhost" > /sdcard/gentoo/etc/hosts `

Do the chroot and source the profile

`root `[`#`]`chroot gentoo/ /bin/su `

`root `[`#`]`source /etc/profile `

** Note**\
If you write a script for mount and unmount, you are more comfortable while using chroot.

#### [Configure Gentoo via chroot]

This is how you configure a gentoo which runns standalone on the TF201 without X.

Download and extract [root_patch.tar.gz](https://github.com/tux-mind/tf201-dev/blob/master/v3/root_patch.tar.gz) inside your chroot. This will install some configuration files and the kernel modules and the (binary) firmware.

If you don\'t trust us, then run:

`root `[`#`]`emerge --ask linux-firmware`

Or just:

`root `[`#`]`mkdir /lib/firmware`

`root `[`#`]`mkdir /system && ln -s /lib /system/vendor && ln -s /lib/firmware /system/etc`

Outside chroot:

`root `[`#`]`cp -R /system/vendor/firmware/* /system/etc/*.txt /sdcard/gentoo/lib/firmware`

TODO: Not all of these files are necessary. We should weed out the ones that aren\'t. AFAIK, just the bcm4329 firmware is required. See make menuconfig for more information.

**Start the configuration**

First start to make some configurations. It is important to set the password for the root user.

`root `[`#`]`passwd`

Type in your root password two times. And give your TF201 a nice name.

[FILE] **`/etc/hostname`**

    # Set the hostname variable to the selected host name
    YourHostname

Configure your timezone:

[FILE] **`/etc/timezone`**

    Europe/Brussels

Enabling US and DE locales with the appropriate character formats. Search the gentoo documentation and forums to get information for your own language settings.

[FILE] **`/etc/locale.gen`**

    en_US ISO-8859-1
    en_US.UTF-8 UTF-8
    de_DE ISO-8859-1
    de_DE@euro ISO-8859-15
    de_DE.UTF-8 UTF-8

Generare the locales.

`root `[`#`]`locale-gen`

Print the locales which were generated.

`root `[`#`]`eselect locale list`

    Available targets for the LANG variable:
      [1] C
      [2] POSIX
      [3] en_US
      [4] en_US.iso88591
      [5] en_US.utf8
      [6] de_DE
      [7] de_DE.iso88591
      [8] de_DE.iso885915
      [9] de_DE.utf8
      [ ] (free form)

Select your locales.

`root `[`#`]`eselect locale set 9`

Now reload the environment:

`root `[`#`]`env-update && source /etc/profile`

Verify if you have the right profile (armv7a with desktop if you like to have XFCE, LXDE, LXQT, Enlightenment, razor-qt etc.)

`root `[`#`]`eselect profile list `

    ------------- 8< --------
    [28] default/linux/arm/13.0/armv7a
    [29] default/linux/arm/13.0/armv7a/desktop *
    [30] default/linux/arm/13.0/armv7a/desktop/gnome
    [31] default/linux/arm/13.0/armv7a/desktop/kde
    [32] default/linux/arm/13.0/armv7a/developer
    ------------- 8< --------

Comment all serial consoles and ttyX where X \> 1 in your [/etc/inittab] and in [/etc/syslog-ng/syslog-ng.conf], if you use syslog-ng

[FILE] **`/etc/inittab`**

    # ------ 8< --
    # TERMINALS
    c1:12345:respawn:/sbin/agetty 38400 tty1 linux
    #c2:2345:respawn:/sbin/agetty 38400 tty2 linux
    #c3:2345:respawn:/sbin/agetty 38400 tty3 linux
    #c4:2345:respawn:/sbin/agetty 38400 tty4 linux
    #c5:2345:respawn:/sbin/agetty 38400 tty5 linux
    #c6:2345:respawn:/sbin/agetty 38400 tty6 linux

    # SERIAL CONSOLES
    #s0:12345:respawn:/sbin/agetty -L 9600 ttyS0 vt100
    #s1:12345:respawn:/sbin/agetty -L 9600 ttyS1 vt100
    # ------ >8 --

Add to [/etc/conf.d/modules]:

[FILE] **`/etc/conf.d/modules`**

    modules="bcm4329"
    module_bcm4329_args="iface_name=wlan0"

You can either add -userfetch to [make.conf] FEATURES (to fix an emerge error about the user being unable to fetch packages) or add the portage user to the 3003 group. See [AndroidSecurityUserAndGroups](https://github.com/keesj/gomo/wiki/AndroidSecurityUserAndGroups). See also CONFIG_ANDROID_PARANOID_NETWORK=y.

`root `[`#`]`groupadd -g 3003 inet `

`root `[`#`]`usermod -aG inet portage `

** Note**\
Usually portage should not be in the inet group - this is just for chroot environment.

Sync the portage-tree the first time and update portage itself.

`root `[`#`]`emerge --sync `

`root `[`#`]`emerge --oneshot portage `

You must install [[[net-wireless/wpa_supplicant]](https://packages.gentoo.org/packages/net-wireless/wpa_supplicant)[]], [[[net-misc/dhcpcd]](https://packages.gentoo.org/packages/net-misc/dhcpcd)[]], and [[[net-misc/openssh]](https://packages.gentoo.org/packages/net-misc/openssh)[]] and add them to the default run-level. It would be easiest to disable qt4 USE flag with respect to wpa_supplicant (for now).

Adjust the [/etc/portage/make.conf] to your needs. At least deactivate the qt4 flag.

[FILE] **`/etc/portage/make.conf`**

    # ------ 8< --
    USE="bindist -qt4"
    # ------ >8 --

`root `[`#`]`emerge --ask wpa_supplicant dhcpcd openssh`

`root `[`#`]`rc-update add sshd default`

** Note**\
You may need to emerge swig, m2crypto and crda this way if wpa_supplicant fails to emerge with a python/crypto error.

`root `[`#`]`emerge --ask -v1 =dev-lang/swing-3.0.4 dev-python/m2crypto net-wireless/crda`

The configuration of wireless network is described in section 3 Gentoo Configuration -\> 3.1 Network / Wifi after a your first start direct into gentoo.

In Gentoo you need to choose a syslogger like sysklogd, syslog-ng, metalog, etc. Here is the example how to install syslog-ng:

`root `[`#`]`emerge --ask syslog-ng`

`root `[`#`]`rc-update add syslog-ng default`

You need to uncomment the ttyX \> tty1. For me it was quickfix to uncomment these lines complete so you will not get any syslogs. If you use /dev/tty1 you will get syslog on tty1, which could be annoying.

[FILE] **`/etc/syslog-ng/syslog-ng.conf`**

    # ------ 8< --
    # By default messages are logged to tty12...
    #destination console_all ;
    destination console_all ;
    # ------ >8 --

Adjust the [/etc/fstab]:

[FILE] **`/etc/fstab`**

    # <fs>                  <mountpoint>    <type>          <opts>          <dump/pass>
    # NOTE: If your BOOT partition is ReiserFS, add the notail option to opts.
    /dev/mmcblk1p1          /               ext4            noatime         0 1
    #/dev/mmcblk1p2        /home       ext4        defaults    0 2
    #/dev/mmcblk0pX        /media/andro    ext4        noauto,ro   0 0
    #/dev/SWAP              none            swap            sw              0 0

See the Tips-Section at the end and create a 2G swap partition.

Compile your own kernel to populate [/lib/modules]. The kernel sources for the \"all linux\" kernel are from [tux-mind TF201 kernel](https://github.com/tux-mind/tf201-kernel)

`root `[`#`]`wget `[`https://github.com/tux-mind/tf201-kernel/archive/master.zip`](https://github.com/tux-mind/tf201-kernel/archive/master.zip)` `

`root `[`#`]`unzip master.zip -d /usr/src `

`root `[`#`]`ln -s /usr/src/tf201-kernel-master /usr/src/linux `

`root `[`#`]`cd /usr/src/linux `

`root `[`#`]`make menuconfig `

`root `[`#`]`make && make modules_install `

The fresh compiled kernel is /usr/src/linux/arch/arm/boot/zImage, which belongs to kernel_choosers /data/boot (but you can still use the \"3.1.10 kernel for \'any\' distro\").

You should now have a gentoo which can start a terminal without X. So exit the chroot environment and umount devices.

`root `[`#`]`exit `

`root `[`#`]`busybox umount -l /sdcard/gentoo/proc `

`root `[`#`]`busybox umount -l /sdcard/gentoo/sys `

`root `[`#`]`busybox umount -l /sdcard/gentoo/dev/pts `

`root `[`#`]`busybox umount -l /sdcard/gentoo/dev `

`root `[`#`]`busybox umount -l /sdcard/gentoo `

**smaller problem solving tips:**

If you get a \"sandbox violation\" error while emerging, you have to emerge the single package that cause you this as follows (ideally, these should be reported as bug reports to [Gentoo Bugzilla](https://bugs.gentoo.org/)):

`root `[`#`]`FEATURES="-sandbox" emerge -1 packagename`

If you have emerge errors like \"/dev/fd/\<number\> file or directory not found\", needs to be done after every chroot:

`root `[`#`]`cd /dev `

`root `[`#`]`ln -s /proc/self/fd `

If you have emerge errors because you have no internet connection:

`root `[`#`]`chmod 644 /etc/resolv.conf`

** Note**\
check/disable your Android firewall if you can ping but not emgerge (terminal emulator, su, etc.)

### [Installing root_chooser]

#### [Configure root_chooser]

** Warning**\
Section Configure root_chooser is for old versions. You better look at [lifeinarootshell](http://lifeinarootshell.blogspot.it/2013/03/howto.html)

The blob and LNX files we provide in git include a modified initrd. What we did is overwrite \'init\' with [root_chooser](https://github.com/tux-mind/tf201-dev/tree/master/root_chooser). Rootchooser will mount the 8th (/data) partition of your eMMC, read the first line of the root-level file \'.root\', which will be parsed as \"blkdev:root_directory_or_image:init_path init_args\" where:

-   \'blkdev\' is the block device to mount, e.g. [/dev/mmcblk0p8], [/dev/mmcblk1p1], or [/dev/sda1].
-   \'root_directory_or_image\' is the directory inside the previous device where your installation lives, e.g. [/gentoo] or [/]. It can also be the path to an ext4 formatted image to use.
-   \'init_path\' is the init script location in your rootfs, usually [/sbin/init].
-   \'init_args\' are optional arguments for the init program.

If anything goes wrong, rootchooser will boot into Android.

Hence, if you have gentoo on the microSD card, .root will be:

    /dev/mmcblk1p1:/:/sbin/init

If it is on /data/gentoo, then:

    /dev/mmcblk0p8:/gentoo:/sbin/init

If on the usb stick:

    /dev/sda1:/:/sbin/init

If from a ext FS image file in /data/media:

    /dev/mmcblk0p8:/media/ubuntu.img:/:/sbin/init

If you would like to test a configuration, or boot into another system once the .root.tmp file may be used instead. It follows the same syntax as .root, and will be removed upon the next reboot.

** Note**\
If the first character is a \'#\' rootchooser boot into android, ignoring the file\'s content.

Once you have created this file, reboot and it should boot into Linux. However, unless you have configured your Gentoo to automatically start Xorg, you will see nothing but the ASUS logo. In order to verify that it worked, either ssh in or reboot back into Android and check [/sdcard/gentoo/var/log/messages]. You can debug problems by checking root_chooser.log which is generated in the root (/) of the Android filesystem.

#### [flashing the boot.blob]

** Note**\
For more detailed and better documentation look at [lifeinarootshell](http://lifeinarootshell.blogspot.it/2013/03/howto.html)

There are at present three ways to install the bootloader on the TF201: nvflash and fastboot from another computer and diskdump from internal. Once you have installed the new bootloader (which includes kernel_chooser) on the TFP and reboot, per default your machine will not boot into Android or any other OS. In order to have it boot into Android or Linux, you need to configure the kernel_chooser.

See the section above.

** Warning**\
Keep a boot partition backup! (Can do this from your recovery) You will need it if you have no or not valid root_chooser configuration or if you made an own blob that could be faulty

** Note**\
flashing blobs via fastboot is the savest method!

##### [Fastboot method]

** Warning**\
As usual, Fastboot and the TFP are cranky and so what follows might \"brick\" your device. Please research the Fastboot utility beforehand.

In order to do fastboot, do the following:

-   Download the blob file to your computer: [latest_fastboot.blob](https://www.dropbox.com/s/42dvjpt315iywup/lastest_fastboot.blob)
-   Put the TFP in \'fastboot\' mode: connect it to the computer via a usb cable, install ClockworkModRecovery app on the TFP, reboot the TFP and hold down VOLUMEDOWN upon reboot until some text shows up about going into recovery. Release VOLUMEDOWN and wait, then select the USB ICON (VOLUMEDOWN to move, VOLUMEUP to select). This is all standard, and documented elsewhere.
-   Flash the blob to your TFP:

`user `[`$`]`fastboot -i 0x0b05 flash boot latest_fastboot.blob`

-   NB: \'flashboot devices\' will claim there is no device. But it is there.

##### [diskdump method on device]

In order to do fastboot directly from the TFP, do the following:

-   Download the blob file to your computer: [latest_fastboot.blob](https://www.dropbox.com/s/42dvjpt315iywup/lastest_fastboot.blob)
-   Run:

`root `[`#`]`dd if=fastboot.blob of=/dev/mmcblk0p4 # or /dev/block/mmcblk0p4 if you are on android`

-   reboot
-   NB: you should see a blue bar after rebooting

##### [Nvflash method]

** Warning**\
As usual, Nvflash and the TFP are cranky. It might \"brick\" your device. Please research Wheelie and Nvflash beforehand.

** Warning**\
Wheelie is a binary with no open source (yet), and as with any binary you should be worried.

In order to do the nvflash method, do the following:

-   Download the LNX file: [lastest_nvflash.LNX](https://www.dropbox.com/s/3ghqkbdt6us1ful/lastest_nvflash.LNX)
-   Put the TFP in nvflash APX mode (reboot + VOLUMEUMP; this will yield a blank screen, but check dmesg to see that it is in APX mode).
-   Run wheelie ([mysecret.blob] is the blob you created when you installed wheelie):

`user `[`$`]`wheelie --blob mysecret.blob`

-   Flash the LNX file to your TFP:

`user `[`$`]`nvflash -r --download 6 nvflash.LNX`

-   Reboot the TFP (this sometimes won\'t reboot the machine):

`user `[`$`]`nvflash -r --go`

### [Generate a test.blob]

** Note**\
You DON\'T need to do this step to install root_chooser. You can use the `latest_fastboot.blob` or `lastest_nvflash.LNX` from \'lifeinarootshell\' as bootloader.

To generate a blob you need to compile a kernel with kexec hardboot capabilities, an initial ramdisk which contains the kernel_loader as init and the kernel, and put all together in a flashable blob.

#### [Compile the host kernel]

Regenerate the zImage (kernel): you will want to apply the JB15.patch (update: not any more in tux-minds git repo). The kernel we used was the one from ASUS: [kernel_v10_4_2_15.zip]. The patch also applies our [.config] file.

`user `[`$`]`wget `[`http://dlcdnet.asus.com/pub/ASUS/EeePAD/TF201/kernel_V10_4_2_15.zip`](http://dlcdnet.asus.com/pub/ASUS/EeePAD/TF201/kernel_V10_4_2_15.zip)

Now unzip and untar the kernel sources. Go to the directory and insert the patch and configure it to your needs. The patch contains a \'.config\' which should fit your needs. In addition there are more features and \'problem solvers\' for example kexec hardboot, keyboard layout, \...

`user `[`$`]`$ cd asus_kernel_v10_4_2_15/ `

`user `[`$`]`$ patch -p1 < ../JB15.patch `

`user `[`$`]`make oldconfig `

`user `[`$`]`make menuconfig `

The kernel needs the property of hardboot and is called host kernel. It can load and start another kernel a so called guest kernel. At least you will need following configurations. The configuration has these flags set, just check it. Well you see it is experimental, but seems to work. You can find additional infos at [XDA KexecHardboot guest kernel](http://forum.xda-developers.com/showthread.php?t=2104706)

[KERNEL]

    Boot options  --->
        [*] Kexec system call (EXPERIMENTAL)
           [*]   Export atags in procfs
           [*]   Support hard booting to a kexec kernel

Now compile the kernel.

`user `[`$`]` make -j<X>`

If all went fine your kernel is at `arch/arm/boot/zImage`

** Note**\
For crosscmpiling you should sth. like \'make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- menuconfig\' and for compiling \'make -j\<X\> ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf-\' where X is a number to define the number of cores used for compilation. make -j2 will compile using 2 cores. Use less cores than your Computer has or it will be unresponsive.

#### [compile kernel_chooser and create initrd]

You need the sources of tux-minds repository. You will get it via git.

`user `[`$`]`git clone `[`https://github.com/tux-mind/tf201-dev`](https://github.com/tux-mind/tf201-dev)` `

`user `[`$`]`cd tf201-dev/kernel_chooser`

The kernel_chooser is made very comfortable. With \'make\' you start the compile process and the packing to an initial ramdisk. In the Makefile you can change the flag \'Development\' to \'1\' to get a rescue shell for the kernel_chooser. The filesystem is in the directory initramfs. It contains busybox and mdev as binraies. If you would like to have additional programms, feel free to add what you need. The Blob has an maximum size of \~8MB.

** Note**\
You should compile the root_chooser via chroot because it uses some libraries. The libraries are statically linked, so croscompile will not work unless you don\'t use explicitly arm binary libs.

`user `[`$`]`make `

`user `[`$`]`mv initrd.gz initrd.img`

The result will be the ready to use initrd.gz, which is an gz-packed initial ramdisk. Rename it to `initrd.img`

** Note**\
Execute the new kernel automatically on a system crash is done if \"KEXEC_ON_CRASH\" flag is activated. The kernel_chooser does not set up a crash kernel properly. see [kexec manpage KEXEC_ON_CRASH](http://man7.org/linux/man-pages/man2/kexec_load.2.html)

#### [make the blob]

You need your already generated files, these are `zImage` from [asus_kernel_v10_4_2_15/arch/arm/boot/zImage], the `initrd.img`, and an old unpacked test.blob, also `test.blob.LNX`. You will find blobpack at [AndroidRoot](https://github.com/AndroidRoot/android_device_asus_tf201) TODO: link for blobunpack.

Unpack the blob and regenerate the .LNX file:

`user `[`$`]`blobunpack test.blob `

`user `[`$`]`abootimg --create test.blob.LNX -r initrd.img -k zImage`

Pack the new blob:

`user `[`$`]`blobpack newTest.blob LNX test.blob.LNX`

Now you have `newTest.blob` and you can flash it via fastboot.

** Note**\
Be sure you have the right blobpack program for the TF201, there exists a different one for the TF101

## [Gentoo Configuration]

### [][Network / Wifi]

The wifi is configured via wpa_supplicant if you use WPA2 in your network. Add to [/etc/conf.d/net]:

[FILE] **`/etc/conf.d/net`**

    modules="wpa_supplicant"
    wpa_supplicant_wlan0="-Dwext"
    config_wlan0="dhcp"

Configure wpa_supplicant with WPA2:

[FILE] **`/etc/wpa_supplicant/wpa_supplicant.conf`**

    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=wheel
    # ensure that only root can read the wpa configuration
    ctrl_interface_group=0
    # let wpa_supplicant take care of scanning and AP selection
    ap_scan=1
    #update_config=1
    network=

Test if the configuration works:

`root `[`#`]`root # wpa_supplicant -Dwext -iwlan0 -c/etc/wpa_supplicant/wpa_supplicant.conf -B dhcpcd wlan0 -dd`

If your configuration establishes a connection, you can add an init script and start wifi:

`root `[`#`]`ln -s /etc/init.d/net.lo /etc/init.d/net.wlan0 `

`root `[`#`]`/etc/init.d/net.wlan0 start `

A wifi-connection which starts automatically is done by a rc-update:

`root `[`#`]`rc-update add net.wlan0 default`

With this configuration your connection will be established after boot-stage.

** Warning**\
Configuration of the network with networkmanager-1.0.0 and nm-applet-1.0.0 will result in a unreliable connection. NetworkManager with flag USE \"dhcpcd\" estabishes a connection for a 30 seconds duration every time you manually connect. NetworkManager with USE \"dhclient\" works for a long time, but with \~60% packet loss. Maybe you figure out a working configuration.

### [Update gentoo]

Now that you have an internet connection you can update gentoo for the first time.

`root `[`#`]`emerge --sync `

`root `[`#`]`emerge -auvDN @world `

** Note**\
If you run into emerge problems with openrc, do the following:

`root `[`#`]`emerge -av1 procps `

`root `[`#`]`emerge -auv1 openrc udev-init-scripts `

`root `[`#`]`emerge -auvDN @world `

### [Sound]

The Prime has no hardware controlled sound. Try to change PCM in alsamixer and you will notice that you can\'t change the volume for audio out.

So the solution is the configuration via alsa. At least you need to configure a `default output`. In addition you will like to have a mixer (`dmixer`) which multiplexes many output streams instead of exclusively only one at a time. And last but no least you like to change the volume, so you need a `software volume` controller. You will get all this for the internal speaker with the following alsa configuration.

** Note**\
Check in your desktop-mixer/alsamixer that the internal speaker, PCM and speaker mixers are unmuted.

The following [/etc/asound.conf] defines a `Master` which you can controll with alsamixer, xfce4-mixer-plugin, volwheel, and maybe many more mixers.

[FILE] **`/etc/asound.conf`**

    pcm.!softvol
        control
    }
    pcm.!dmixer
            bindings
    }
    ctl.dmixer
    pcm.!default
    ctl.!default

** Note**\
Extend the configuration to have sound on headphones and with HDMI.

Test your configuration:

`root `[`#`]`/etc/init.d/alsasound start`

** Note**\
Your configuration needs an initial play to get recognized by alsa.

`user `[`$`]`speaker-test -t sine -f 400`

Add it to openrc for automatic startup:

`root `[`#`]`root # rc-update add alsasound default`

### [xorg-server with fbdev]

emerge xorg-server to get a working X11 and add INPUT_DEVICES to [/etc/portage/package.use]

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* fbdev

[FILE] **`/etc/portage/package.use/00input`**

    */* INPUT_DEVICES: evdev synaptics

`root `[`#`]`emerge -av xorg-server `

`root `[`#`]`env-update && source /etc/profile `

Test if all went fine.

`root `[`#`]`startx -- vt1`

If X11 started and quit with \"Server teminated successfully (0)\", you\'re lucky.

Now configure gentoo to start X always on vt1:

[FILE] **`/etc/X11/xinint/xserverrc`**

    exec /usr/bin/X -nolisten tcp "$@" vt01

Start emerging a desktop-environment of your choice.

A classic and simple one is TWM:

`root `[`#`]`emerge -av twm xclock xterm `

`root `[`#`]`startx `

TWM should now be working with touchpad and touchscreen and you have windows. exit all xterms and your get back to console.

### [Proprietary Nvidia Tegra 3 driver]

The actual Xorg-server version is 19 and Nvidias last release of the tegra driver is version 14. So you need to mask Xorg-server to versions bigger than 1.14.

** Note**\
Masking \>=xorg-server-1.15.2-r1 results in xorg-server-1.12.4, which is not 1.14. Maybe it is possible to get better masks in the dependancies of Xorg-server.

[FILE] **`/etc/portage/package.mask`**

    >=x11-base/xorg-server-1.15.2-r1
    >=x11-drivers/xf86-input-synaptics-1.8.0
    >=app-eselect/eselect-opengl-1.3.1-r2
    >=media-libs/mesa-10.3.7-r2
    >=x11-proto/glproto-1.4.17-r1
    >=x11-base/xorg-drivers-1.17

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* tegra

[FILE] **`/etc/portage/package.use/00input`**

    */* INPUT_DEVICES: evdev synaptics mouse keyboard

Install X11:

`root `[`#`]`emerge --ask xorg-server`

#### [Automatic]

I (tux1c) have started maintaining a tf201 specific overlay, which also contains the tegra3 drivers. In order to add the repo, please emerge eselect-repository first:

`root `[`#`]`emerge --ask --noreplace app-eselect/eselect-repository dev-vcs/git`

Now, add the tf201 overlay:

`root `[`#`]`eselect repository enable tf201 `

`root `[`#`]`emerge --sync tf201`

Install tegra 3 drivers: (also installs the codecs)

`root `[`#`]`emerge --ask tegra3-driver`

And set the driver abi version.

`root `[`#`]`cd /usr/lib/xorg/modules/drivers/drivers `

`root `[`#`]`ln -s tegra_drv.so tegra_drv.abi12.so `

Overlay\'s git is located at [https://github.com/Tux1c/tf201-overlay](https://github.com/Tux1c/tf201-overlay).

#### [Manual]

Download the latest Cardu driver package from Nvidia ([https://developer.nvidia.com/linux-tegra](https://developer.nvidia.com/linux-tegra)). Here is an example to download the Version r16.5:

`root `[`#`]`wget `[`http://developer.download.nvidia.com/mobile/tegra/l4t/r16.5.0/cardhu_release_armhf/Tegra30_Linux_R16.5_armhf.tbz2`](http://developer.download.nvidia.com/mobile/tegra/l4t/r16.5.0/cardhu_release_armhf/Tegra30_Linux_R16.5_armhf.tbz2)

Extract the package and copy `config.tbz2` and `nvidia_drivers.tgz` to roots home directory.

`root `[`#`]`cd /root `

`root `[`#`]`tar -xvjf Tegra30_Linux_R16.5_armhf.tbz2 `

`root `[`#`]`mv Linux_for_Tegra/nv_tegra/config.tbz2 . `

`root `[`#`]`mv Linux_for_Tegra/nv_tegra/nvidia_drivers.tbz2 . `

`root `[`#`]`rm -r Linux_for_Tegra `

Extract the driver and the config files.

`root `[`#`]`cd / `

`root `[`#`]`tar xvjf root/nvidia_drivers.tbz2 `

`root `[`#`]`tar xvjf root/config.tbz2 `

** Note**\
The two files [libjpeg.so] and [libEGL.so.1] are overwritten (TODO: test the conflicts))

There are some different builds of the tegra driver in [/usr/lib/xorg/modules/drivers] for Xorg versions, which differ in ABI (application binary interface) versions. Get to know your Xorg-server version:

`root `[`#`]`Xorg -version `

    X.Org S Server 1.12.4

`tegra_drv.so` needs to be linked to the ABI version of the X-server.

`root `[`#`]`cd /usr/lib/xorg/modules/drivers `

`root `[`#`]`ln -s tegra_drv.abi12.so tegra_drv.so `

Clean up the files config files. [/etc/wpa_supplicant.conf] is unnecessary and in the wrong place. Place the contents [/etc/init/nv.conf] in an local.d/mystart.start (I\'m not sure what these do, but they cause cpufreq-set to not work and give us wonderful new messages in messages). The [/etc/init/ttyS0.conf]

`root `[`#`]`rm /etc/wpa_supplicant.conf `

`root `[`#`]`cat /etc/init/nv.conf > /etc/local.d/mystart.start `

`root `[`#`]`cd /etc `

`root `[`#`]`rm -rf init `

Add \"vt01\" to the end of the command line in [/etc/X11/xinit/xserverrc] (see FAQ below for details).

Run \"startx\" or \"startx \--vt01\" if xserverrc is not configured. If no window/desktop manager is configured but everything is working you\'ll get a usual X output log and then dumped back at the command prompt; if you have configured a window/desktop manager (e.g. \'echo \"startxfce4\" \> \~/.xinitrc\') it should start; if the system is misconfigured a hang followed by reboot is possible.

The following xorg.conf is in most parts from the TF700 wiki with changes to make the touchpad working.

** Warning**\
The HDMI output is working \"a little bit\", but not perfectly

[FILE] **`/etc/X11/xorg.conf`**

    Section "ServerLayout"
        Identifier    "Layout0"
        Screen      0 "ScreenLVDS" 0 0
    EndSection

    Section "Extensions"
        Option "Composite" "Enable"
    EndSection

    Section "Module"
        Load  "glx"
        Load  "record"
        Load  "i2c"
    EndSection

    Section "Screen"
        Identifier    "ScreenLVDS"
        Device        "DeviceLVDS"
        Monitor       "MonitorLVDS"
        DefaultDepth   24
    EndSection

    Section "Device"
        Identifier    "DeviceLVDS"
        Driver        "tegra"
        Option        "ARGBHWCursor"
        Option        "RenderAccel" "true"
        Option        "AllowGLXWithComposite" "true"
        Option        "Monitor-HDMI-1"  "MonitorHDMI"
    EndSection

    Section "Monitor"
        Identifier    "MonitorLVDS"
        VendorName    "Nvidia"
        ModelName     "T30 Tegra3"
        Option        "DPMS" "true"
    #    DisplaySize   218 136
    EndSection

    Section "Monitor"
        Identifier    "MonitorHDMI"
        VendorName    "Nvidia"
        ModelName     "T30 Tegra3"
        Option        "DPMS" "true"
    EndSection

    Section "InputClass"
        Identifier       "catched touchpad"
        Driver           "synaptics"   #"multitouch"
        MatchIsTouchpad   "on"
            Option  "TapButton1"    "1"
            Option  "TapButton2"    "2"
            Option  "TapButton3"    "3"
            Option  "VertEdgeScroll"        "On"
            Option  "VerTwoFingerScroll"    "On"
        Option "CorePointer" "true"
    EndSection

    Section "InputClass"
        Identifier       "catched touchscreen"
        Driver           "mtev"
        MatchDevicePath  "/dev/input/event*"
        MatchProduct     "elan-touchscreen"
        Option           "CorePointer"     "true"
    EndSection

    Section "InputClass"
        Identifier      "tf201 keyboard"
        Driver          "evdev"
        MatchDevicePath "/dev/input/event*"
        MatchIsKeyboard "true"
        MatchProduct    "asusdec"
        Option "AutoRepeat"   "200 50"
        Option "XkbModel"     "pc104"
        Option "XkbLayout"    "us"
    EndSection

Now you can activate the USE-flags `"gles1 gles2"` in [/etc/portage/make.conf].

### [Sandbox]

Some packages might fail to emerge when using the proprietary driver, because they rely on the sandbox feature. A fix would be granting sandbox access to the needed /dev devices:

[FILE] **`/etc/sandbox.conf`**

    #----------
    # Needed for NVIDIA Drivers
    SANDBOX_WRITE="/dev/mem:/dev/knvmap:/dev/nvmap:/dev/nvhost-ctrl"

### [OpenTegra driver]

Recently (December 2012 / January 2013), Stephen Warren and Thierry Reding have been working on getting an open tegra implementation in the kernel and also an xorg driver associated with that. Purportedly, this will be in the 3.8 kernel. We\'ll be keeping an eye on this over the next few weeks! If anyone has given it a go, drop me a line! Thierry\'s git is: [https://gitorious.org/thierryreding/xf86-video-opentegra](https://gitorious.org/thierryreding/xf86-video-opentegra)

### [Keyboard]

It is possible to change the keyboard layout to be similar to a normal desktop\'s. If you are using at least the [v3 kernel](https://github.com/tux-mind/tf201-dev/tree/master/v3/images) you\'re able to modify the kernel keyboard layout using setkeycodes. Give a look to the [/etc/local.d/00-setkeycodes.start](https://github.com/tux-mind/tf201-dev/blob/master/scripts/00-setkeycodes.start) script installed from the root_patch. Otherwise you have to change the way Xorg translate keycodes throught xmodmap (it is slower, do it only if you have a kernel version minor than the v3).

`root `[`#`]`emerge --ask xmodmap`

Create a config file:

`user `[`$`]`xmodmap -pke > ~/.Xmodmap`

Edit the key bindings.

[FILE] **`~/.Xmodmap`**

    # For example to change home to windows key (Super). Change
    keycode 180 = XF86HomePage NoSymbol XF86HomePage
    # to
    keycode 180 = Super_L NoSymbol Super_L

** Note**\
You can use xev to get the keycode and name of a button press.

Add the following to [\~/.xinitrc] to automatically apply this configuration

`user `[`$`]`xmodmap ~/.Xmodmap`

### [Atmel Maxtouch touchscreen]

I\'ll be busy over the next few weeks, so here\'s a status quaestionis:

The nvidia tegra drivers (Linux For Tegra RC16.2, documented on the wiki) seem to work. There will be conflicts with two files, and it would be nice to package things in an ebuild.

As a result, `xrandr -o left/right/normal/inverted` work!

But xinput set-prop 8 \"Evdev Axis Inversion\" 1, 1 && xinput set-prop \"Evdev Axes Swap\" 1 don\'t (i.e. I can\'t get the input to switch its coordiantes when I rotate the screen).

** Note**\
Fiddling with xinput set-prop 8 \"Coordinate Transformation Matrix\" does change the input coordinates, but it is strange. I fiddled with this for a while.

The problem must be with the Atmel-Maxtouch code. I did some digging around and comparison to other atmel_maxtouch.c files located in:

-   [https://github.com/EnJens/kernel_tf201_stock](https://github.com/EnJens/kernel_tf201_stock): this seems to have an older version, although Rayman doesn\'t document where he patched it from.
-   [https://github.com/AndroidRoot/android_kernel_asus_tf201/tree/10.4.2.17-mr1](https://github.com/AndroidRoot/android_kernel_asus_tf201/tree/10.4.2.17-mr1): Rayman recommended this as the latest and greatest, and it has the latest Asus kernel_V10_4_2_17.zip (We should probably upgrade at some point!), but the files in question related to atmel_maxtouch are the same as Asus 10.4.2.15 (our version).
-   [https://github.com/atmel-maxtouch/linux/tree/maxtouch-v3.0/drivers/input/touchscreen](https://github.com/atmel-maxtouch/linux/tree/maxtouch-v3.0/drivers/input/touchscreen): this looks promising. CFR [http://forum.xda-developers.com/showthread.php?t=1496246](http://forum.xda-developers.com/showthread.php?t=1496246)

And that\'s where I am at. So if you ever get around to thinking about this problem \-- and solve it or have more hints \-\-- let me know.

### [Battery]

I had no problems with the battery. If do you have any trouble with this try installing your DesktopEnvironment\'s power manager. For those curious, the battery information files are stored in /sys/class/power_supply/

### [Touchpad]

Please install the [v1 kernel](https://github.com/tux-mind/tf201-dev/tree/master/v1/images). Use [touchpad_control](https://github.com/tux-mind/tf201-dev/tree/master/touchpad_control) to enable and disable the touchpad.

## [Known bugs]

-   Problem: After I launch X and I kill X, the screen is blank. Solution: There is none. Make sure you have sshd installed.
-   Problem: X goes blank and won\'t go unblank. Solution: Disable X blanking. `xset -dpms `or `xset s off` or `xset s noblank` (or all three)
-   Problem: With Tegra Drivers (RC16.2) installed, `xinput set-int-prop 8 "Evdev Axes Swap" 8 1` and `xinput set-int-prop 8 "Evdev Axis Inversion" 8 1 0` get registered in, e.g., `xinput list-props` but fail to have an actual effect on the input x/y coordinates. Solution: None yet. (See above)
-   Problem: With Tegra Drivers (RC16.2) installed, I also get some further cpu spam messages. Solution: None yet.
-   Problem: `xrandr -o left/right/normal/inverted` don\'t work. Solution: Install the tegra_drv (xorg driver) from RC16.2 of their Linux For Tegra release (see above)

<!-- -->

-   FIXED My messages is spammed up with asusdec_kp_key and asusdec_keypad_processing debugging statements in [/var/log/messages]. Solution: install at least the [v2 kernel](https://github.com/tux-mind/tf201-dev/tree/master/v2/images).
-   FIXED Compositing doesn\'t work due to unavailable graphics shared memory. Solution: Upgrade to Tegra Drivers (RC16.2)
-   FIXED In login screen keyboard has a wrong layout. Solution: add that line \'Option \"XkbLayout\" \"\$YOUR_KEYBOARD_LAYOUT\"\' to [/usr/share/X11/xorg.conf.d/10-evdev.conf] in the InputClass with \"evdev keyboard catchall\" as Identifier.
-   FIXED Xorg crash with v3 kernel. Solution: append vt01 to [/etc/X11/xinit/xserverrc] to make X always use vt1. Other vt\'s will cause a crash.
-   FIXED Cannot emerge firefox. Solution: you have to upgrade gcc to 4.6.\*, emerge firefox with a swapfile, you\'ll get an error on install. swapoff. ebuild /usr/portage/www-client/firefox-17.0.3/firefox-\....ebuil install qmerge celan
-   FIXED The touchpad (on the ASUS Keyboard Dock) doesn\'t work. Solution: See above
-   FIXED Sound doesn\'t work. Solution: See above.

## [Tips]

Here are some tips:

-   if you are using a kernel previous then the v3 one edit [/etc/inittab] and comment out the c\* and s\* entries.
-   mount [/var/tmp] and [/tmp] as tmpfs
-   make a 2G swapfile
-   /dev/mmcblk0p1,2,8 are ext4; mount these in /mnt as system, cache, data respectively.
-   sudo -u yourusername startx in /etc/local.d/mystuff.start for a quick and dirty test
-   cpufreq-set -c 0 -g performance\|powersave (do this for 0-3) (For some reason, placing [/etc/init/nv.conf] contents in local.d/start.start causes cpufreq-set to stop working,s o whatever those things do, they broke this.)

## [Contribute]

Please feel free to add new problems! Even better: new solutions!

The current [TODO list](https://github.com/tux-mind/tf201-dev/blob/master/TODO) is on github.

Please contact peter period hartman at utoronto period ca a.k.a. wart\_ in #gentoo-embedded (and elsewhere)\
Or contact massimo period dragano at gmail period com a.k.a tux_mind all over the internet