This page contains [[changes](https://wiki.gentoo.org/index.php?title=Gentoo_installation_tips_and_tricks&oldid=1045939&diff=1310100)] which are not marked for translation.

Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/Gentoo_installation_tips_and_tricks/es "Consejos y trucos para instalar Gentoo (100% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/Gentoo_installation_tips_and_tricks/it "Installazione di Gentoo: suggerimenti e trucchi (1% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Gentoo_installation_tips_and_tricks/hu "Gentoo telepítési tippek és trükkök (100% translated)")
-   [polski](https://wiki.gentoo.org/wiki/Gentoo_installation_tips_and_tricks/pl "Gentoo installation tips and tricks/pl (1% translated)")
-   [português do Brasil](https://wiki.gentoo.org/wiki/Gentoo_installation_tips_and_tricks/pt-br "Dicas e truques da instalação do Gentoo (70% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Gentoo_installation_tips_and_tricks/ru "Полезные советы по установке Gentoo (100% translated)")
-   [српски (ћирилица)‎](https://wiki.gentoo.org/wiki/Gentoo_installation_tips_and_tricks/sr-ec "Gentoo installation tips and tricks/sr-ec (30% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Gentoo_installation_tips_and_tricks/zh-cn "Gentoo安装提示和技巧 (43% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Gentoo_installation_tips_and_tricks/ja "Gentoo インストールのヒントとトリック (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Gentoo_installation_tips_and_tricks/ko "젠투 설치 요령 (72% translated)")

The Gentoo installation allows for very flexible approaches to the various installation methods. As it is almost impossible to insert every single tip or trick in the installation instructions this document tries to deal with all submitted tips and tricks for reference purposes.

This document contains various **tips and tricks** for the Gentoo/x86 installation. Most of them are discussed in a dense way - they are meant as an addendum to the installation instructions and not as a replacement.

## Contents

-   [[1] [Advanced Installations]](#Advanced_Installations)
    -   [[1.1] [Software RAID]](#Software_RAID)
    -   [[1.2] [ATA RAID using 2.4 kernels]](#ATA_RAID_using_2.4_kernels)
    -   [[1.3] [Using the Installation CD kernel]](#Using_the_Installation_CD_kernel)
-   [[2] [Simplifying the installation]](#Simplifying_the_installation)
    -   [[2.1] [Leaving the terminal]](#Leaving_the_terminal)
-   [[3] [Fixing errors and issues]](#Fixing_errors_and_issues)
    -   [[3.1] [Extensive testing of the disks]](#Extensive_testing_of_the_disks)
    -   [[3.2] [Recovering from a malfunctioning installation]](#Recovering_from_a_malfunctioning_installation)

## [Advanced Installations]

### [Software RAID]

** Note**\
If not familiar with software RAID, please read the [Software RAID HOWTO](https://raid.wiki.kernel.org/index.php/Linux_Raid).

Once booted from the Installation CD, load the appropriate RAID modules. For instance, if planning on using RAID-1:

`root `[`#`]`modprobe raid1`

When partitioning disks, make sure that the partitions use `fd` (Linux RAID autodetect) as Partition Type instead of `83` (Linux native). The partition type can be altered using the `t` command in `fdisk`.

Before creating the RAID arrays, the metadevice nodes must be created:

`root `[`#`]`mknod /dev/md1 b 9 1 `

`root `[`#`]`mknod /dev/md2 b 9 2 `

`root `[`#`]`mknod /dev/md3 b 9 3`

After partitioning, create the [/etc/mdadm.conf] file (yes, indeed, on the Installation CD environment) using `mdadm`, an advanced tool for RAID management. For instance, to have the boot, swap and root partition mirrored (RAID-1) covering [/dev/sda] and [/dev/sdb], it is possible to use:

`root `[`#`]`mdadm --create --verbose /dev/md1 --level=1 --raid-devices=2 --metadata=0.90 /dev/sda1 /dev/sdb1 `

`root `[`#`]`mdadm --create --verbose /dev/md2 --level=1 --raid-devices=2 --metadata=0.90 /dev/sda2 /dev/sdb2 `

`root `[`#`]`mdadm --create --verbose /dev/md3 --level=1 --raid-devices=2 --metadata=0.90 /dev/sda3 /dev/sdb3`

** Important**\
Do not use any form of striping such as RAID-0 or RAID-5 on the boot partition. Also, the `--metadata=0.90` is only necessary for these critical file systems. Other filesystems can use more recent metadata formats.

The Linux Software RAID driver will start creating the metadevices. See its progress in [/proc/mdstat]. Wait until the metadevices are completely finished before proceeding.

`root `[`#`]`mdadm --detail --scan > /etc/mdadm.conf`

From now onwards, use [/dev/md1] for the boot partition, [/dev/md2] for the swap partition and [/dev/md3] for the root partition.

Right before chrooting, don\'t forget to copy over [/etc/mdadm.conf] to [/mnt/gentoo/etc].

When configuring the kernel, make sure to have the appropriate RAID support *in* the kernel and not as module.

When installing extra tools, emerge [[[sys-fs/mdadm]](https://packages.gentoo.org/packages/sys-fs/mdadm)[]] as well. Note that this isn\'t available on all Installation CDs so it might not be possible to install Gentoo on a Software RAID when using a networkless installation!

When configuring the bootloader, make sure it gets installed in the MBR of *both* disks if using mirroring.

### [ATA RAID using 2.4 kernels]

Make sure to boot the Installation CD using the `doataraid` option. Once booted, check the contents of [/dev/ataraid]. It should contain various [disc\*] directories for each hard disk available in the ATA RAID. An entire disk is displayed as [disc] while partitions are [part\*].

Write down the various [/dev/ataraid/disc\*/\*] device files that used to install Gentoo on. Substitute the [/dev/sda] examples in the installation with this path.

Before chrooting, bind-mount the [/dev] structure in the new environment:

`root `[`#`]`mount --rbind /dev /mnt/gentoo/dev`

When configuring the kernel, make sure to enable support for the ATA RAID chipset and options. For instance, a popular ATA RAID system is a *Promise FastTrack built-in RAID* in which case `Promise FastTrack Options` will definately need to be built in into the kernel.

When configuring GRUB, first create a GRUB bootdisk. This is not particularly hard. First install GRUB as normal, but when coming to the part where GRUB is getting installed in the MBR, follow the following instructions:

`root `[`#`]`cd /boot/grub `

`root `[`#`]`dd if=stage1 of=/dev/fd0 bs=512 count=1 `

`root `[`#`]`dd if=stage2 of=/dev/fd0 bs=512 seek=1`

Write the [grub.conf] file. This is no different from the installation instructions, just make sure that `root=` points to the ATA RAID device.

After finishing the installation, boot with the GRUB bootdisk. A GRUB prompt should appear. Now configure GRUB to boot from the ATA RAID device:

`grub>``root (hd0,x)`

`grub>``setup (hd0) `

`grub>``quit`

Now reboot (with the GRUB bootfloppy removed).

LILO users can safely use the instructions mentioned in the installation instructions.

### [Using the Installation CD kernel]

If not wanting to compile a kernel, it is possible to use the kernel from the Installation CD and copy it to the system. When coming to the point where asked to compile a kernel, go to another terminal (press [Alt] + [F2]) and log in with the root password supplied at the beginning of the installation.

Copy over the kernel and modules to the Gentoo system:

** Note**\
\$ is the kernel name, usually something like \'gentoo\' or \'smp\'.

`root `[`#`]`cp /mnt/cdrom/isolinux/$ /mnt/cdrom/isolinux/$.igz /mnt/gentoo/boot `

`root `[`#`]`mkdir -p /mnt/gentoo/lib/modules `

`root `[`#`]`` cp -Rp /lib/modules/`uname -r` /mnt/gentoo/lib/modules ``

To have all modules that are currently running (from the Installation CD) loaded during bootup of the Gentoo system, run the following command from within the chrooted environment:

`root `[`#`]`mkdir -p /etc/modules-load.d `

`root `[`#`]`cut -d ' ' -f 1 /proc/modules >> /etc/modules-load.d/local.conf `

Verify the [/etc/modules-load.d/local.conf] content and update appropriately.

## [Simplifying the installation]

### [Leaving the terminal]

Many people want to leave their system when it\'s compiling. In certain cases this is rather difficult as the installation is done in a public environment. If this is the case, it would be preferable to perform the compilation in the background and log out from all terminals.

There are several possible solutions for this. The first one is to use [[screen](https://wiki.gentoo.org/wiki/Screen "Screen")]. After booting the Installation CD, set the root password and start a [screen] session:

** Note**\
Not all Installation CDs provide screen. If this is the case, use one of the other methods described in this section.

`root `[`#`]`screen -S gentoo`

Once inside the screen session the entire installation may be performed. When leaving a terminal, press [Ctrl] + [a], [d] (that is, [Ctrl] and [a] at the same time, then followed by a [d]) to *detach* the screen session. It is now safe to log out of the system (without losing work).

To regain access to the terminal, log in as root again and *attach* to the running screen session:

`root `[`#`]`screen -x gentoo`

If screen is not an option, there is still a way to leave the terminal. Follow the installation instructions, but when a long-term compilation begins (for instance the [./scripts/bootstrap.sh] step), use [nohup] which allows for a process to continue even when the session closed with a log out. Don\'t forget the trailing \"&\", otherwise the process will not be placed in the background! Remember the current directory (the [pwd] command will show that) as this will be needed later on.

`root `[`#`]`pwd`

    /var/db/repos/gentoo

`root `[`#`]`nohup ./scripts/bootstrap.sh &`

Now exit the chrooted environment ([exit]) and the Installation CD session. The compilation will continue in the background.

To check the compilation, log in as root (on the Installation CD) and chroot back into the environment, then go to the directory where the session was left off:

`root `[`#`]`chroot /mnt/gentoo /bin/bash `

`root `[`#`]`env-update && source /etc/profile `

`root `[`#`]`cd /var/db/repos/gentoo`

Now use the [less] command on the [nohup.out] file that is situated inside that directory. The compilation will append its output to that file, so if it is desired to follow the compilation progress, run [less nohup.out] and press [F] to follow the changes. When the compilation is finished, continue with the next step of the installation instructions.

When finished following the changes, press [Ctrl] + [c] followed by a [q]. This won\'t stop the compilation process, only the [less] process.

## [Fixing errors and issues]

### [Extensive testing of the disks]

If a disk needs to be thoroughly checked for consistency (bad sectors and such), can use the `-c` option while placing the ext2/ext3/ext4 filesystem on it (using `mke2fs`). This will format, perform a read-test and mark all bad blocks as such. If really paranoid, use `-c -c` to format the disk and perform an extensive read/write test.

`root `[`#`]`mke2fs -j -c /dev/sda3`

### [Recovering from a malfunctioning installation]

If for some reason the Gentoo installation fails, it is not required to redo the installation all over again. Instead, it is possible to safely \"go\" to the point where an issue occurred (or where it might be suspected the instructions are flawed) and try a different approach.

First of all chroot back into the Gentoo Linux environment. Follow the instructions again, but ignore the partitioning steps as the partitions are already created and even populated. It is possible to immediately mount those partitions at [/mnt/gentoo]. Ignore the steps about stage extraction and modifying [make.conf] - so as to not overwrite files.

Once chrooted inside the Gentoo Linux environment, immediately go to the step where it is thought a different approach should be tried. Don\'t redo all the steps like bootstrapping and such unless that is the place where things might have gone wrong.

For instance, if suspecting a wrongly configured [grub.conf], fire up an editor to update [/boot/grub/grub.conf].

Once a different approach has been tried, consider how much of the subsequent steps need to be performed again. If the subsequent steps are depending on this latest change, they will need to be redone.

For instance:

-   if a variable inside [make.conf] has been changed, all subsequent compiling since those depend on the settings inside [make.conf] will need to be redone
-   if [/boot/grub/grub.conf] has been altered, it is possible to immediately exit the chrooted environment and reboot as no subsequent steps are depending on [grub.conf]
-   if the kernel has been recompiled, just make sure that the bootloader configuration points to the correct kernel image (double-check that [/boot] is mounted!), then exit the chrooted environment and reboot
-   if [/etc/fstab] changed, exit the chrooted environment and reboot

For most recovery operations, a reboot may be done immediately. Only in certain cases will the subsequent installation steps need to be redone.

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Xavier Neys, nightmorph**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*