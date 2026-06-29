[] The information in this article is probably **outdated**. You can help the Gentoo community by verifying and [updating this article](https://wiki.gentoo.org/index.php?title=Old_Fashioned_Gentoo_Install&action=edit).

This document describes how to install Gentoo without the hand holding automation features that users have come to take for granted over the last 10 years. It gives you an install as it was before devfs was added to the kernel.

** Warning**\
This page was created around 2013. It\'s outdated

## Contents

-   [[1] [Overview]](#Overview)
    -   [[1.1] [Synopsis]](#Synopsis)
    -   [[1.2] [Overview]](#Overview_2)
    -   [[1.3] [Introduction]](#Introduction)
-   [[2] [Getting started]](#Getting_started)
    -   [[2.1] [Partitioning and filesystem creation]](#Partitioning_and_filesystem_creation)
-   [[3] [Chrooting]](#Chrooting)
    -   [[3.1] [Making the chroot]](#Making_the_chroot)
    -   [[3.2] [Entering the chroot]](#Entering_the_chroot)
    -   [[3.3] [Setting up package.mask]](#Setting_up_package.mask)
    -   [[3.4] [Setting up package.use]](#Setting_up_package.use)
    -   [[3.5] [Setting USE in make.conf]](#Setting_USE_in_make.conf)
    -   [[3.6] [Adding to /dev]](#Adding_to_.2Fdev)
    -   [[3.7] [Populating /etc/conf.d/modules]](#Populating_.2Fetc.2Fconf.d.2Fmodules)
    -   [[3.8] [Setting up a static overlay]](#Setting_up_a_static_overlay)
-   [[4] [Getting ready to reboot]](#Getting_ready_to_reboot)
    -   [[4.1] [Making the kernel]](#Making_the_kernel)
-   [[5] [Making the initrd]](#Making_the_initrd)
    -   [[5.1] [Preparing for usr/gen_init_cpio]](#Preparing_for_usr.2Fgen_init_cpio)
    -   [[5.2] [Populating /etc/fstab]](#Populating_.2Fetc.2Ffstab)
    -   [[5.3] [Configuring the system]](#Configuring_the_system)
    -   [[5.4] [Installing necessary system tools]](#Installing_necessary_system_tools)
    -   [[5.5] [Setting up the boot loader]](#Setting_up_the_boot_loader)
-   [[6] [Hints for Xorg]](#Hints_for_Xorg)
    -   [[6.1] [xorg.conf]](#xorg.conf)
-   [[7] [Hints for a desktop environment]](#Hints_for_a_desktop_environment)
    -   [[7.1] [GNOME or KDE Plasma]](#GNOME_or_KDE_Plasma)
    -   [[7.2] [Xfce 4]](#Xfce_4)
    -   [[7.3] [The gentoo-static overlay]](#The_gentoo-static_overlay)
-   [[8] [External resources]](#External_resources)

## [Overview]

### [Synopsis]

Its possible to start with the official stage3 files. This has only been tested on an amd64/no-multilib install.

** Warning**\
Still reading \... don\'t say you were never warned. The usual caveat applies, if it breaks, you can keep the pieces. You might even try a post in Unsupported Software on the Gentoo Forums.

As this document is aimed at users with at least one Gentoo install to their credit, it is not a keystroke by keystroke guide, unlike the Handbook. The handbook steps are not repeated here, there is just some general references to it from time to time.

### [Overview]

The install will use root in Logical Volume Manager (LVM) on NVMe, with separate /usr and /var. /home, \$DISTFILES and \$PACKAGES will be in LVM on rotating rust RAID as Conventional Magnetic Recording (CMR) drives are quite good at sequential access of large files. Thus we need an initrd to get started.

Its unlikely that grub2 will be used as the boot loader.

The steps include:

-   Partition the target drive following the handbook.
-   Install the stage3 tarball.
-   Install the portage snapshot.
-   Set up package.mask to keep out unwanted junk.
-   Set up global USE flags to be consistent with [package.mask].
-   Replace udev with [[[sys-fs/static-dev]](https://packages.gentoo.org/packages/sys-fs/static-dev)[]].
-   Follow the handbook to install cron, a logger and a bootloader of choice.
-   Install a kernel.
-   Configure the grub bootloader.
-   Review and edit configuration settings.
-   Reboot to test.

### [Introduction]

This document describes how to install Gentoo with a static [/dev] using the packages from a stage3 tarball.

**What You Get**

A modern Gentoo base system but without all the bells and whistles added in recent years. Olde Fashioned Gentooee is more about what you don\'t get. You do *not* get:

-   udev - instead a static dev is used
-   systemd - why would you want it anyway
-   pulseaudio - I\'ve not known this to actually add anything
-   hotplug support
-   auto mounting of any sort - use mount by label
-   auto module loading
-   device detection in Xorg

Separate [/usr] should just work as there is no udev to require that [/usr] is mounted before udev starts. If udev starts on your box you have done something wrong. Separate [/usr] is not tested as I\'m using root in lvm, so while my [/usr] is separate, bad habits have made me mount it in the initrd.

Access to the [Gentoo Handbook](https://wiki.gentoo.org/wiki/Handbook:Main_Page "Handbook:Main Page") is required as this guide makes frequent references to it, there is no point in repeating the handbook here.

## [Getting started]

### [Partitioning and filesystem creation]

**Making the filesystem tree**

Follow the [Gentoo Handbook](https://wiki.gentoo.org/wiki/Handbook:Main_Page "Handbook:Main Page") up to and including making the filesystems and mounting all the bits at the [/mnt/gentoo] directory.

I will be using Logical Volumes on top of raid5 because its easier to recycle the volumes than it is with real partitions and if the logical volumes are the wrong size, they can be resized. I happen to have lvm on raid5 space free. This means that I will also describe the initramfs to get the raid assembled and Logical Volumes active. Users installing to real partitions should not need the initramfs.

## [Chrooting]

### [Making the chroot]

Mount [/proc] and but not [/dev] inside the chroot. We will be using a static [/dev], so we have to [emerge dev-static]. With [/dev] bind mounted in the normal way, our static dev would go into the parents devtmpfs which is in RAM. If you are very very lucky, the static [/dev] provided by the stage3 may be enough to get you started.

The stage3 tarball is provided with a static [/dev] that includes sda \... sdd inclusive. If you need more that that, use [mknod] to make the extra [/dev] entries. Likewise, there ale no md entries for raid or dm enteries for LVM.

Mount the special filesystems

`root `[`#`]`mount -t proc proc /mnt/gentoo/proc`

### [Entering the chroot]

Enter the chroot:

`root `[`#`]`chroot /mnt/gentoo /bin/bash`

\
Set the chroot environment:

`root `[`#`]`env-update `

`root `[`#`]`source /etc/profile `

`root `[`#`]`export PS1="(chroot) $PS1" `

### [Setting up package.mask]

This is important. Enter the package atoms that you do not want to be installed ever.

[FILE] **`/etc/portage/package.mask`Content of package.mask**

    # go back to a static /dev
    sys-fs/eudev
    sys-fs/udev
    sys-auth/polkit
    sys-auth/consolekit
    media-sound/pulseaudio
    sys-apps/systemd

Add in anything else you can think of they you really don\'t want. Always use `-av` with emerge and add more things as they come to mind. mdev might need to be there too.

### [Setting up package.use]

This section is only required if you use raid, or lvm. You will need some packages built with the static USE flag.

[FILE] **`/etc/portage/package.use`Content of package.use**

    # static bits and pieces for an initrd
    sys-fs/lvm2 static
    sys-fs/mdadm static
    sys-apps/busybox static

Removing udev and Friends

There is a bug in the static-dev ebuild [[[bug #469620]](https://bugs.gentoo.org/show_bug.cgi?id=469620)[]] that prevents it installing if /proc/mounts reports that a dynamic /dev manager is in use. Either patch static-dev in the overlay or unmount /proc from /mnt/gentoo/proc while static-dev is emerged.

Replacing udev with static-dev:

`root `[`#`]`emerge --ask --unmerge sys-fs/udev`

\

`root `[`#`]`emerge --ask sys-fs/static-dev`

\...see [[[bug #469620]](https://bugs.gentoo.org/show_bug.cgi?id=469620)[]].

emerge sys-fs/static-dev will report some file collisions. That is expected as some elements of a static [/dev] are provided by the stage3.

`root `[`#`]`emerge --ask --depclean`

The last command should offer to remove the following packages:

-   [[[sys-apps/hwids]](https://packages.gentoo.org/packages/sys-apps/hwids)[]]
-   [[[sys-fs/udev-init-scripts]](https://packages.gentoo.org/packages/sys-fs/udev-init-scripts)[]]
-   [[[sys-libs/libcap]](https://packages.gentoo.org/packages/sys-libs/libcap)[]]
-   [[[dev-util/gperf]](https://packages.gentoo.org/packages/dev-util/gperf)[]]
-   [[[virtual/udev]](https://packages.gentoo.org/packages/virtual/udev)[]]

Let it run, they all depend on udev, which is no longer installed.

### [Setting USE in make.conf]

Some of my USE flags are AMD specific. The flags that are set off here are for avoidance of optional support for packages we have already masked. Optional support being on would attempt to pull those packages in and emerge would complain about masked packages.

[FILE] **`/etc/portage/make.conf`USE flags**

    USE="X alsa device-mapper apng mp3 python jpeg lock session startup-notification thunar curl ffmpeg odf pdf raw gtk cairo -consolekit -dso -firmware-loader -gbm -kmod  -ldap -networkmanager -nss -oss -qt4 -systemd -tools -udev -zeroconf"

The `-zeroconfig` flag is a special case. Zeroconfig wasn\'t around 10 years ago so really should be excluded here.

### [][Adding to /dev]

static-dev is a good start but its not moved on in a very long time. Add some of the newer entries required. See [/usr/src/linux/Documentation/devices.txt] for a list

-   mknod all of the /dev/sd\* entries you need
-   mknod any /dev/md\* kernel multipe device entries required
-   mknod any /dev/dm-X device mapper entries required
-   mknod any /dev/srX devices for your optical drive(s)
-   mknod any other /dev nodes you might want. They can be added at any time

Do not forget nodes for removable storage devices.

DRI users, that\'s almost everyone except those who use nvidia-drivers for Xorg will need to make [/dev/dri/\*]. What is needed here is driver dependent.

### [][Populating /etc/conf.d/modules]

Only you know what you need here. When you reboot, its a good idea to have keyboard support and udev isn\'t going to load it for you any more.

** Important**\
Review your lsmod to decide what you need

### [Setting up a static overlay]

A number of packages that are required for a modern Gentoo system require udev. In some the dependency can be avoided by careful use of USE flags. Others like lvm2 and Xorg have udev included in IUSE. Make a local overlay called static_dev, copy these ebuilds there and remove all references to udev.

** Warning**\
This may break these packages in ways I\'m totally unaware of - yet

## [Getting ready to reboot]

### [Making the kernel]

Follow the instructions at [http://www.kernel-seeds.org](http://www.kernel-seeds.org) which is mirrored at [http://kernel-seeds.grytpype-thynne.org](http://kernel-seeds.grytpype-thynne.org) ( [http://kernel-seeds.bloodnoc.org/](http://kernel-seeds.bloodnoc.org/) ) with the following changes

** Warning**\
kernel-seeds.org is under new management. The mirror is no longer maintained and will go away soon.

[KERNEL] **Key kernel options**

    ()  path to uevent helper
    [ ] Maintain a devtmpfs filesystem to mount at /dev
    [*]   Unix98 PTY support
    [ ]   Legacy (BSD) PTY support
        (256)   Maximum number of legacy PTY in use
    [ ]   Dynamic device file minor numbers

We can leave off the hair shirts. Unix98PTY support does work but the permissions on /dev/ptmx need to be set correctly and /dev/ptmx needs to be mounted crw-rw\-\-\-- 1 root tty 5, 2 Mar 18 21:47 /dev/ptmx

Genkernel users are on their own here.

Provided your kernel can boot unaided, no initrd is required

## [Making the initrd]

### [][Preparing for usr/gen_init_cpio]

To make everything robust and independent of what filesystem gets attached to which /dev node, we will use the filesystem UUIDs everywhere.

** Warning**\
The kernel cannot mount root by UUID unless you use the userspace mount command, which requires an initramfs

There are several ways to make an initramfs, we will use the kernel provided usr/gen_init_cpio script.

The script needs two things, a list of files to include in the initramfs and an init sctipt to execute. The use of usr/gen_init_cpio is well documented in the kernel.

Make a directory to hold the two files. I like /root/initrd. The two files that follow go there.

[FILE] **`/root/initrd/initramfs_list`**

    # directory structure
    dir /proc       755 0 0
    dir /usr        755 0 0
    dir /bin        755 0 0
    dir /sys        755 0 0
    dir /var        755 0 0
    #dir /lib        755 0 0
    dir /lib64      755 0 0
    dir /sbin       755 0 0
    dir /mnt        755 0 0
    dir /mnt/root   755 0 0
    dir /etc        755 0 0
    dir /root       700 0 0
    dir /dev        755 0 0
    dir /dev/mapper 755 0 0

    # we have a static /dev so we need all dev entries too
    # e.g. /dev/console below
    nod /dev/console        0600 0 0 c 5 1
    nod /dev/null           0666 0 0 c 1 5

    # dev/sda and partitions
    nod /dev/sda            0660 0 0 b 8 0
    nod /dev/sda1           0660 0 0 b 8 1
    nod /dev/sda2           0660 0 0 b 8 2
    nod /dev/sda4           0660 0 0 b 8 4
    nod /dev/sda5           0660 0 0 b 8 5
    nod /dev/sda6           0660 0 0 b 8 6

    # dev/sdb and partitions
    nod /dev/sdb            0660 0 0 b 8 16
    # ...
    # dev/sdc and partitions
    nod /dev/sdc            0660 0 0 b 8 32
    # ...

    # three raid nodes
    nod /dev/md125           0660 0 0 b 9 125
    nod /dev/md126           0660 0 0 b 9 126
    nod /dev/md127           0660 0 0 b 9 127

    # all the lvm nodes I need
    nod /dev/dm-0            0660 0 0 b 253 0
    nod /dev/dm-1            0660 0 0 b 253 1
    nod /dev/dm-2            0660 0 0 b 254 2
    # ...

    slink /dev/stderr                       /proc/self/fd/2                 777 0 0
    slink /dev/stdin                        /proc/self/fd/0                 777 0 0
    slink /dev/std/out                      /proc/self/fd/1                 777 0 0

    # busybox
    file /bin/busybox /bin/busybox  755 0 0

    # for raid on lvm
    file /sbin/mdadm                /sbin/mdadm              755 0 0
    file /sbin/mdadm                /sbin/mdadm              755 0 0
    file /sbin/lvm.static           /sbin/lvm.static         755 0 0

    # libraries required by /sbin/fsck.ext4 and /sbin/fsck

    slink   /lib                            /lib64                          777 0 0
    file    /lib64/ld-linux-x86-64.so.2     /lib64/ld-linux-x86-64.so.2     755 0 0
    file    /lib64/libext2fs.so.2           /lib64/libext2fs.so.2           755 0 0
    file    /lib64/libcom_err.so.2          /lib64/libcom_err.so.2          755 0 0
    file    /lib64/libpthread.so.0          /lib64/libpthread.so.0          755 0 0
    file    /lib64/libblkid.so.1            /lib64/libblkid.so.1            755 0 0
    file    /lib64/libuuid.so.1             /lib64/libuuid.so.1             755 0 0
    file    /lib64/libe2p.so.2              /lib64/libe2p.so.2              755 0 0
    file    /lib64/libc.so.6                /lib64/libc.so.6                755 0 0
    file    /lib64/libmount.so.1            /lib64/libmount.so.1            755 0 0

    file    /sbin/fsck              /sbin/fsck                      755 0 0
    file    /sbin/fsck.ext4         /sbin/fsck.ext4                 755 0 0

    # our init script
    file    /init                   /root/initrd/init               755 0 0

I\'m sure there is a sh one liner to feed to busybox mknod as a part of the init script, so I don\'t need the huge list of nod statements but I don\'t know it.

If you use files systems other than extX on /usr and / or /var, which the initrd checks and mounts, you need your filesystem tools listed here. Feel free to add other things you find useful when booting fails too.

[FILE] **`/root/initrd/init`**

    #!/bin/busybox sh

    rescue_shell()

    # allow the use of UUIDs or filesystem lables
    uuidlabel_root()

    check_filesystem()

    # start for real here

    # temporarily mount proc and sys
    mount -t proc none /proc
    mount -t sysfs none /sys

    # assemble the raid set(s) - they got renumbered from md1, md5 and md6

    # not needed on SSD but we may want to maintain it
    # /boot
    /sbin/mdadm --assemble /dev/md125 /dev/sda1 /dev/sdb1 /dev/sdc1 /dev/sdd1
    # don't care if /boot fails to assemble

    # not needed on SSD
    # /  (root)  I wimped out of root on lvm for this box
    /sbin/mdadm --assemble /dev/md126 /dev/sda5 /dev/sdb5 /dev/sdc5 /dev/sdd5 || rescue_shell
    # if root won't assemble, we are stuck

    # LVM for everything else
    # /home and everything portge related
    /sbin/mdadm --assemble /dev/md127 /dev/sda6 /dev/sdb6 /dev/sdc6 /dev/sdd6 || rescue_shell
    # and if the LVM space won't assemble there is no /usr or /var so we are really in a mess
    # TODO could auto cope with degraded raid operation

    # lvm runs as whatever its called as
    ln -s /sbin/lvm.static /sbin/vgchange

    # everything on the SDD
    /sbin/vgchange -ay ssd | rescue_shell

    # start the vg volume group - /home and everything for portage - need not die here
    /sbin/vgchange -ay vg || rescue_shell

    # get here with raid sets assembled and logical volumes available
    # mounting rootfs on /mnt/root
    uuidlabel_root || rescue_shell "Error with uuidlabel_root"

    # space separated list of mountpoints that ...
    mountpoints="/usr /var"

    # ... we want to find in /etc/fstab ...
    ln -s /mnt/root/etc/fstab /etc/fstab

    # ... to check filesystems and mount our devices.
    for m in $mountpoints ; do

    #echo $m

        check_filesystem $m

        echo "Mounting $m"
        # mount the device and ...
        mount $m || rescue_shell "Error while mounting $m"

        # ... move the tree to its final location
        mount --move $m "/mnt/root"$m || rescue_shell "Error while moving $m"
    done

    echo "All done. Switching to real root."

    # clean up. The init process will remount proc sys and dev later
    umount /proc
    umount /sys

    # switch to the real root and execute init
    exec switch_root /mnt/root /sbin/init

Now to feed the [/root/initrd/initramfs_list] file to usr/gen_init_cpio. Make sure [/boot] is mounted.

Running usr/gen_init_cpio:

`root `[`#`]`cd /usr/src/linux `

`root `[`#`]`usr/gen_init_cpio /root/initrd/initramfs_list > /boot/initramfs_static `

This what the kernel build system does if you choose to build the initramfs into the kernel binary but if you don\'t get it right first time, you can fix your kernel without rebuilding your initramfs and vice versa.

### [][Populating /etc/fstab]

Run blkid to discover the UUIDs of all your block devices. Paste the output into /etc/fstab, so its easy to refer to in the future. Delete lines that provide the UUIDS of block devices that are not filesystesms, e.g. lvm members, md devices. Comment out the other entries, so they can stay in the file.

Populating [/etc/fstab] as normal, but use UUIDs:

[FILE] **`/etc/fstab`**

    UUID=741183c2-1392-4022-a1d3-d0af8ba4a2a8          /boot           ext2            noauto,noatime            1 2
    UUID=bcd0b621-2027-4471-ac26-99c5f95ee2d3          /               ext4            noatime,discard           0 1
    UUID=0f7610bd-67c9-40c6-8a16-70d617ef09d3          /var            ext4            noatime,noauto,discard    1 0
    UUID=3e82328c-e85f-435e-8836-5c63b38df620          /usr            ext4            noatime,noauto,discard    1 0

** Note**\
Be sure to use system specific UUIDs, mount point,s and mount options. The UUIDs in the filebox above are simply given for an example.

As there is no auto mounting, do not forget entries for optical drives.

Floppy disk users need to remember /dev/fdX and friends. Users who have not formatted a floppy with a static [/dev] are in for a treat.

### [Configuring the system]

Follow [Configuring the system](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/System "Handbook:AMD64/Installation/System") in the **[amd64]** handbook.

### [Installing necessary system tools]

Follow [Installing system tools](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Tools "Handbook:AMD64/Installation/Tools") in the **[amd64]** handbook.

### [Setting up the boot loader]

The Grand Unified Bootloader (GRUB) has already been installed to [/boot].

Follow [Configuring the bootloader](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Bootloader "Handbook:AMD64/Installation/Bootloader") to install GRUB to the Master Boot Record (MBR) or to configure properly when using a GUID Partition Table (GPT). Associated GRUB configuration file(s) will also be needed.

## [Hints for Xorg]

### [xorg.conf]

You need a whole [xorg.conf], just like in the good/bad old days. evdev depends on udev auto detecting devices, so that is out.

## [Hints for a desktop environment]

### [GNOME or KDE Plasma]

Gnome is not an option. I suspect that KDE Plasma is out too.

### [Xfce 4]

Xfce almost works out of the box. You need a patched mesa ebuild to build without udev.

### [The gentoo-static overlay]

hwids works but the ebuild needs to be patched to remove the dependency on udev

mesa

I need to get round to publishing the overlay.

## [External resources]

-   [http://swift.siphos.be/linux_sea/](http://swift.siphos.be/linux_sea/) - An ebook that offers a gentle yet technical (from end-user perspective) introduction to the Linux operating system, using Gentoo Linux as the example Linux distribution. (Link included with permission from the author.)

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **neddyseagoon**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*