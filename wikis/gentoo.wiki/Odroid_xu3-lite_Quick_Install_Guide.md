[] The information in this article is probably **outdated**. You can help the Gentoo community by verifying and [updating this article](https://wiki.gentoo.org/index.php?title=Hardkernel_ODROID-XU3_Lite&action=edit).

[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**Resources**

[[]][Product Information](https://www.hardkernel.com/shop/odroid-xu3-lite/)

[[]][ODROID](https://en.wikipedia.org/wiki/ODROID "wikipedia:ODROID")

Installing Gentoo onto an Odroid XU3-Lite is not a difficult task. To do it in an easy way, we will need two micro SD memory cards of 8GB. We will use a hard disk of 40GB via USB. We will use the disk to improve speed; but actually you can not use it at all.

## Contents

-   [[1] [Starting up the main board]](#Starting_up_the_main_board)
-   [[2] [Getting more resources]](#Getting_more_resources)
-   [[3] [Partitioning the disk]](#Partitioning_the_disk)
-   [[4] [Installing gentoo]](#Installing_gentoo)
    -   [[4.1] [Downloading the files]](#Downloading_the_files)
    -   [[4.2] [Installing the gentoo environment]](#Installing_the_gentoo_environment)
        -   [[4.2.1] [Chroot]](#Chroot)
        -   [[4.2.2] [Preparing make.conf]](#Preparing_make.conf)
        -   [[4.2.3] [Installing packages]](#Installing_packages)
        -   [[4.2.4] [Configuring NTP]](#Configuring_NTP)
        -   [[4.2.5] [The network]](#The_network)
        -   [[4.2.6] [Other configuration files]](#Other_configuration_files)
        -   [[4.2.7] [Activating the services]](#Activating_the_services)
        -   [[4.2.8] [Setting the root password]](#Setting_the_root_password)
    -   [[4.3] [Chroot exit]](#Chroot_exit)
-   [[5] [Preparing the media for Gentoo]](#Preparing_the_media_for_Gentoo)
    -   [[5.1] [Universal boot]](#Universal_boot)
    -   [[5.2] [Mounting the file system]](#Mounting_the_file_system)
        -   [[5.2.1] [Extracting the kernel binaries]](#Extracting_the_kernel_binaries)
        -   [[5.2.2] [Preparing the files]](#Preparing_the_files)
        -   [[5.2.3] [Preparing the boot.ini file]](#Preparing_the_boot.ini_file)
        -   [[5.2.4] [Preparing fstab]](#Preparing_fstab)
        -   [[5.2.5] [Optimizing our gentoo]](#Optimizing_our_gentoo)
-   [[6] [Finally]](#Finally)
-   [[7] [Other Thoughts]](#Other_Thoughts)
    -   [[7.1] [The purchase of]](#The_purchase_of)

### [Starting up the main board]

Download the appropriate Ubuntu image and copy it to the micro SD card.

`root `[`#`]` wget `[`https://dn.odroid.com/5422/ODROID-XU3/Ubuntu/ubuntu-14.04.1lts-lubuntu-odroid-xu3-20141105.img.xz`](https://dn.odroid.com/5422/ODROID-XU3/Ubuntu/ubuntu-14.04.1lts-lubuntu-odroid-xu3-20141105.img.xz)` `

`root `[`#`]` xz -d -c ubuntu-14.04.1lts-lubuntu-odroid-xu3-20141105.img.xz | pv | dd of=/dev/sdb `

If there is another image, normally you can use the new one.

Activate boot from micro SD using the corresponding switch

[![ODROID-XU3 Lite Boot Switch.jpg](/images/c/c5/ODROID-XU3_Lite_Boot_Switch.jpg)](https://wiki.gentoo.org/wiki/File:ODROID-XU3_Lite_Boot_Switch.jpg)

You can get more information about this procedure [using this link](https://www.cnx-software.com/2014/12/14/odroid-xu3-lite-board-ubuntu-review-setup-usability-and-performance/)

Insert the card into the card reader and switch on the PC

### [Getting more resources]

Because I will not need the graphical user interface I will get rid of it. You can login using ssh or the UART terminal, ssh is recommended.

user: root password: odroid.

`root `[`#`]`echo "manual" > /etc/init/cups.override `

`root `[`#`]`echo "manual" > /etc/init/cups-browsed.override `

`root `[`#`]`echo "manual" > /etc/init/lightdm.override `

`root `[`#`]`echo "manual" > /etc/init/bluetooth.override `

`root `[`#`]`/etc/init.d/ntp stop `

`root `[`#`]`ntpdate my.time.server.com `

`root `[`#`]`echo "Europe/Zurich" > /etc/timezone `

`root `[`#`]`dpkg-reconfigure tzdata `

`root `[`#`]`nano -w /etc/ntp.conf `

[FILE] **`/etc/ntp.conf`ntp related settings**

    server my.time.server.com

`root `[`#`]`shutdown -r now`

### [Partitioning the disk]

Connect the disk and make a partition with ext4 to hold on the Ubuntu File System, 6GB should be enough more will be better ;-).

`root `[`#`]`parted /dev/sda`

    (parted) mklabel msdos
    (parted) mkpart primary 1MiB 20GiB
    (parted) quit

`root `[`#`]`partprobe`

`root `[`#`]`mkfs.ext4 /dev/sda1 `

`root `[`#`]`mkdir /mnt/repository `

`root `[`#`]`mount /dev/sda1 /mnt/repository `

### [Installing gentoo]

In this part I will go really fast it is just the normal gentoo installation process.

#### [Downloading the files]

We will need some files to do the installation. The stage 3 for arm, the last portage, the kernel binary and the kernel source. Actually we do not need the whole tree of the kernel but I do not know git very well. I used the kernel 3.10.63 with date 31 de diciembre del 2014. Yes, I was working that day.

`root `[`#`]`cd /mnt/repository `

`root `[`#`]`wget `[`http://mirror.gentoo/releases/arm/autobuilds/current-stage3-armv7a_hardfp/stage3-armv7a_hardfp-YYYYMMDD.tar.bz2`](http://mirror.gentoo/releases/arm/autobuilds/current-stage3-armv7a_hardfp/stage3-armv7a_hardfp-YYYYMMDD.tar.bz2)` `

`root `[`#`]`wget `[`https://gentoo.osuosl.org/snapshots/portage-latest.tar.xz`](https://gentoo.osuosl.org/snapshots/portage-latest.tar.xz)` `

`root `[`#`]`wget `[`http://builder.mdrjr.net/kernel-3.10/00-LATEST/odroidxu3.tar.xz`](http://builder.mdrjr.net/kernel-3.10/00-LATEST/odroidxu3.tar.xz)` `

`root `[`#`]`git clone --depth 1 `[`https://github.com/hardkernel/linux.git`](https://github.com/hardkernel/linux.git)` -b odroidxu3-3.10.y linux-odroidxu3-3.10 `

#### [Installing the gentoo environment]

`root `[`#`]`mkdir gentoo `

`root `[`#`]`cd gentoo `

`root `[`#`]`tar -xvjpf ../stage3-armv7a_hardfp-YYYYMMDD.tar.bz2 `

`root `[`#`]`cd usr `

`root `[`#`]`tar xjvf ../../portage-latest.tar.bz2 `

`root `[`#`]`cd /mnt/repository `

##### [Chroot]

`root `[`#`]`cd `

`root `[`#`]`mount -t proc none /mnt/repository/gentoo/proc `

`root `[`#`]`mount -o bind /sys /mnt/repository/gentoo/sys `

`root `[`#`]`mount -o bind /dev /mnt/repository/gentoo/dev `

`root `[`#`]`cp -L /etc/resolv.conf /mnt/repository/gentoo/etc/ `

`root `[`#`]`chroot /mnt/repository/gentoo /bin/bash `

`root `[`#`]`env-update && source /etc/profile `

`root `[`#`]`export PS1="(chroot) $PS1" `

##### [Preparing make.conf]

`root `[`#`]`nano -w /etc/portage/make.conf `

[FILE] **`/etc/portage/make.conf`related settings**

    # Please consult /usr/share/portage/config/make.conf.example for a more
    # detailed example.
    CFLAGS="-O2 -pipe -march=armv7-a -mfpu=vfpv3-d16 -mfloat-abi=hard"
    CXXFLAGS="$"
    CHOST="armv7a-hardfloat-linux-gnueabi"

    # These are the USE flags that were used in addition to what is provided by the
    # profile used for building.
    USE="-bindist threads -X"

    MAKEOPTS="-j9"

    PORTDIR="/usr/portage"
    DISTDIR="$/distfiles"
    PKGDIR="$/packages"
    PORTAGE_TMPDIR=/tmp

[FILE] **`/etc/portage/package.use/00localization`**

    */* LINGUAS: en

##### [Installing packages]

We will emerge some key packages, the rest you can do it later.

`root `[`#`]`emerge syslog-ng vixie-cron dhcp ntp`

##### [Configuring NTP]

This is really important!!!.

This motherboard does not have any real time clock (RTC), so we will need some software to do de job.

`root `[`#`]`emerge ntp `

`root `[`#`]`echo "Europe/Zurich" > /etc/timezone `

`root `[`#`]`emerge --config timezone-data `

Edit the contents of /etc/ntp.conf and /etc/conf.d/ntp-client with nano if you know what to put in.

[FILE] **`/etc/ntp.conf`ntp related settings**

    server my.time.server.com

[FILE] **`/etc/conf.d/ntp-client`ntp-client related settings**

    NTPCLIENT_OPTS="-s -b -u my.time.server.com"

In may case, dhclient, set up my ntp.conf. ntp-client is not essential, but for me it helps a lot ;-)

##### [The network]

Nothing new here, but remember, we will set up the mac address in the file \"boot.ini\"

`root `[`#`]`cd /etc/init.d `

`root `[`#`]`ln -s net.lo net.localnet `

Edit the contents of /etc/udev/rules.d/70-persistent-net.rules and /etc/conf.d/net to setup the behavior of the network interface

[FILE] **`/etc/udev/rules.d/70-persistent-net.rules`udev rule for network interface**

    SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR=="00:1e:06:61:7a:39", ATTR=="0x0", ATTR=="1", KERNEL=="eth*", NAME="localnet"

[FILE] **`/etc/conf.d/net`**

    config_localnet="dhclient"
    dhclient_localnet="-q"

##### [Other configuration files]

We should define the hostname of our workstation

`root `[`#`]`nano -w /etc/conf.d/hostname `

[FILE] **`/etc/conf.d/hostname`**

    HOSTNAME="odroid-xu3"

our keymap

`root `[`#`]`nano -w /etc/conf.d/keymaps`

[FILE] **`/etc/conf.d/keymaps`**

    keymap="us-acentos"

I change the syslog-ng configuration to avoid the use of the filesystem. You could not do this, but I did it.

`root `[`#`]`nano -w /etc/syslog-ng/syslog-ng.conf`

[FILE] **`/etc/conf.d/hostname`**

    #log ;

Because we do not have a RTC, we need to avoid fsck to verify the system time. With this setting e2fsck will always assume that the system clock can not be trusted.

`root `[`#`]`nano -w /etc/e2fsck.conf`

[FILE] **`/etc/e2fsck.conf`**

    [options]
    broken_system_clock = true

##### [Activating the services]

`root `[`#`]`rc-update add syslog-ng default `

`root `[`#`]`rc-update add vixie-cron default `

`root `[`#`]`rc-update add sshd default `

`root `[`#`]`rc-update add net.localnet default `

`root `[`#`]`rc-update add ntp-client default `

`root `[`#`]`rc-update add ntpd default `

##### [Setting the root password]

This will be the password for our new environment

`root `[`#`]` password root `

We are done here. We will now close the chroot and finish installation.

#### [Chroot exit]

`root `[`#`]`exit `

`root `[`#`]`umount /mnt/repository/gentoo/ `

We are in ubuntu land again. A few more steps to complete the installation.

### [Preparing the media for Gentoo]

Now we need to connect the second micro SD card using an USB interface to the computer. In my case /dev/sdb I will create a new partition table and put two new primary partitions. One for the kernel and some boot files and the other one for the system. We need 2MiB free before the firs partition, you will know later why.

`root `[`#`]`parted /dev/sdb`

    (parted) mklabel msdos
    (parted) mkpart primary 2MiB 128MiB
    (parted) mkpart primary 128MiB 3GiB
    (parted) quit

`root `[`#`]`partprobe `

`root `[`#`]`mkfs.vfat /dev/sdb1 `

`root `[`#`]`mkfs.ext4 /dev/sdb2 `

`root `[`#`]`blkid`

    ...
    /dev/sdb1: SEC_TYPE="msdos" UUID="612A-ED6F" TYPE="vfat"
    /dev/sdb2: UUID="788af328-b4be-4393-9da0-260b2412275f" TYPE="ext4"
    ...

#### [Universal boot]

We need to install the u-boot into the same space we let free in our last step. For this:

`root `[`#`]`cd /mnt/repository/linux-odroidxu3-3.10/tools/hardkernel/prebuilt_uboot/ `

`root `[`#`]`sh ./sd_fusing.sh /dev/sdb `

Follow the instructions and be careful with the name of the device.

#### [Mounting the file system]

We have now two partitions, but they are empty. To fix that we will use the kernel binaries and the Gentoo\'s file system tree that we already did.

`root `[`#`]`cd /mnt/repository/ `

`root `[`#`]`mkdir bootFS `

`root `[`#`]`mkdir rootFS `

`root `[`#`]`mount /dev/sdb1 bootFS `

`root `[`#`]`mount /dev/sdb2 rootFS `

##### [Extracting the kernel binaries]

We will use this time the kernel binaries. We will use the kernel source in another tutorial.

`root `[`#`]`mkdir odroidxu3 `

`root `[`#`]`cd odroidxu3 `

`root `[`#`]`tar -xvJf ../odroidxu3.tar.xz `

##### [Preparing the files]

What do we do now?

We copy the \"boot\" folder from the kernel binaries to the micro SD boot partition. We copy the \"lib\" folder to the Gentoo\'s file system tree. We copy the Gentoo\'s file system tree to the microSD card.

`root `[`#`]`cd /mnt/repository `

`root `[`#`]`cp -a -f -v odroidxu3/boot/* bootFS/ `

`root `[`#`]`cp -a -f -v odroidxu3/lib/* /mnt/repository/gentoo/lib/ `

`root `[`#`]`cp -a -f -v /mnt/repository/gentoo/* rootFS/ `

##### [Preparing the boot.ini file]

I will copy the boot.ini from ubuntu to my micro SD card. Then, I will modify the root devide (It did not work for me using UUID). In this file you will find also the mac address to be assigned to the ethernet card.

`root `[`#`]`cp /media/boot/boot.ini bootFS/ `

`root `[`#`]`nano -w bootFS/boot.ini `

[FILE] **`bootFS/boot.ini`**

    setenv bootrootfs "console=tty1 console=ttySAC2,115200n8 root=/dev/mmcblk0p2 rootwait ro"

##### [Preparing fstab]

Using UUID for the fstab is normally a god thing to do. You can modify this file using device names or volume labels. It is your choice.

`root `[`#`]` nano -w rootFS/etc/fstab `

[FILE] **`rootFS/etc/fstab`**

    UUID=788af328-b4be-4393-9da0-260b2412275f  /   ext4    errors=remount-ro,noatime,nodiratime        0 1
    UUID=612A-ED6F  /boot   vfat    defaults,rw,owner,flush,umask=000   0 0
    tmpfs       /tmp    tmpfs   nodev,nosuid,mode=1777          0 0

##### [Optimizing our gentoo]

In my case I will use this computer as server. I will not use screen, mouse or keyboard on it. I will claim back some resources optimizing rootFS/etc/inittab.

[FILE] **`rootFS/etc/inittab`**

    ...
    # TERMINALS
    c1:12345:respawn:/sbin/agetty 38400 tty1 linux
    #c2:2345:respawn:/sbin/agetty 38400 tty2 linux
    ...
    # SERIAL CONSOLES
    s0:12345:respawn:/sbin/agetty -L 115200 ttySAC2 xterm
    #s1:12345:respawn:/sbin/agetty -L 9600 ttyS1 vt100
    ...

### [Finally]

Shutdown the whole system

`root `[`#`]` shutdown -h now `

exchange the cards ubuntu \<-\> gentoo.

In the next start up, you should see a pretty fast Gentoo up and running :-)

### [Other Thoughts]

I would like to share some facts about this main board. It is just my own experience nothing else.

#### [The purchase of]

I bought this motherboard through the web site of hardkernel. I have to say that I did not receive any kind of confirmation from the web site when I did it.

I tried to contact the support by mail, with the confirmation from paypal, but they consider yahoo as spam!!! I tried then from gmail and that time, they answered me.

They shipped the parcel using UPS. It was really fast but extremely expensive.

The hardware was really good. The package content was exactly as described. Actually, I recommended it.

In my case, the power source got lock into my electrical extension cord. Now I can not pull out the power source and I can not use the extension for any other use.

The fan is really noisy, even if they have some kind of smart controller. I would prefer a bigger one but more silent.

The software support is really good. You can find whatever you need online. Hardkernel provides a kernel and some binary tools with the correct documentation.