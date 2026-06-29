This page contains [[changes](//wiki.manjaro.org/index.php?title=GRUB/Restore_the_GRUB_Bootloader&oldid=37374&diff=49920)] which are not marked for translation.

Other languages:

[Deutsch](//wiki.manjaro.org/index.php?title=GRUB/Restore_the_GRUB_Bootloader/de "GRUB/Den GRUB Bootloader Wiederherstellen (94% translated)") • ‎[English] • ‎[Türkçe](//wiki.manjaro.org/index.php?title=GRUB/Restore_the_GRUB_Bootloader/tr "GRUB/GRUB Önyükleyicisini Geri Yükle (56% translated)") • ‎[français](//wiki.manjaro.org/index.php?title=GRUB/Restore_the_GRUB_Bootloader/fr "GRUB/Restaurer le programme de d'amorçage GRUB (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=GRUB/Restore_the_GRUB_Bootloader/ru "GRUB/Восстановление загрузчика GRUB (100% translated)")

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Preparation]](#Preparation)
-   [[3] [Load Manjaro Installation Media]](#Load_Manjaro_Installation_Media)
-   [[4] [Identify partitions]](#Identify_partitions)
-   [[5] [Use root context]](#Use_root_context)
-   [[6] [Chroot environment]](#Chroot_environment)
    -   [[6.1] [Identify system partitions]](#Identify_system_partitions)
    -   [[6.2] [Use manjaro-chroot]](#Use_manjaro-chroot)
    -   [[6.3] [Manual chroot]](#Manual_chroot)
-   [[7] [Reinstall GRUB]](#Reinstall_GRUB)
    -   [[7.1] [BIOS System]](#BIOS_System)
    -   [[7.2] [EFI System]](#EFI_System)
-   [[8] [Updating grub]](#Updating_grub)
    -   [[8.1] [Additional Information]](#Additional_Information)
        -   [[8.1.1] [package version of grub]](#package_version_of_grub)
        -   [[8.1.2] [grub-bootloader version]](#grub-bootloader_version)
        -   [[8.1.3] [update-grub]](#update-grub)
    -   [[8.2] [install-grub]](#install-grub)
-   [[9] [Troubleshooting]](#Troubleshooting)
    -   [[9.1] [Manjaro is not recognized]](#Manjaro_is_not_recognized)
-   [[10] [See also]](#See_also)

## [Overview]

In order to load the operating system, a Linux-capable boot loader such as GRUB, rEFInd or Syslinux needs to be installed to the Master Boot Record (MBR) or the GUID Partition Table (GPT) of the media containing the Operating System. Installations created using Manjaro ISO defaults to GRUB.

For various reasons - it happens the bootloader get\'s corrupted, erased or misconfigured resulting to a black screen with a failure message during boot, like **No boot loaders found in /dev/\...**. To restore system operation without re-installing your OS or losing your data you will need to use your Manjaro installation media, such as, a CD/DVD or USB Flashdrive.

**Archlinux Boot Process**

------------------------------------------------------------------------

More information about the boot process on Archlinux based distributions is available at [Archwiki](https://wiki.archlinux.org/index.php/Arch_boot_process)

## [Preparation]

Identify the type of system you are attempted to resque as the commands involved are slightly different.

-   BIOS/MBR/GPT system
-   EFI/GPT system

## [Load Manjaro Installation Media]

**System Boot Override**

------------------------------------------------------------------------

To override system boot order the vendor has a dedicated key. Most laptop keyboard has multiple use for the function keys and the primary function may be reversed. In such case a [Fn] key must be used with the function key. If you don\'t know consult your system documentation. Manjaro ISO default usernames and passwords

  ------------------ ------------------
  Default Username   Default Password
  manjaro            manjaro
  root               manjaro
  ------------------ ------------------

## [Identify partitions]

To identify your partitions and their designated use you need to run a partition manager. Depending on environment there is various tools. GTK based ISO offers GpartEd, QT based ISO offers KParted and common to all is the CLI tools.

[user \$ ][ lsblk -o PATH,PTTYPE,PARTTYPE,FSTYPE,PARTTYPENAME [COPY TO CLIPBOARD]]

\

More comprehensive information can be found using `fdisk` (requires superuser) and you can limit the probed device e.g. */dev/sda* or */dev/nvme0n1*

[user \$ ][ sudo fdisk -l /dev/sda [COPY TO CLIPBOARD]]

\

The clues to look for is *mbr* vs. *gpt* and the presence of a small partition - usually the first - formatted with the *vfat* filesystem followed by a larger partition formatted as *ext4*.

\

**Info**

------------------------------------------------------------------------

This document and the content should **never** be used as a copy/paste resource. The remainder of this document will use pseudo names and partition numbering. Devices will be referred as **/dev/sdy** and partitions referred as **/dev/sdyA** and you will have to subtitute those with the real values from your system.

\

## [Use root context]

When you have loaded the live ISO - depending on environment - open a terminal and switch to *root* context. Use above mentioned root:password combination.

[user \$ ][ su [COPY TO CLIPBOARD]]

\

## [Chroot environment]

Chroot is a method to restrict various tasks to a restricted area e.g. package installation and other system maintenance tasks. Follow the [link](https://wiki.archlinux.org/index.php/Change_Root) to read more about chroot on the Arch wiki.

### [Identify system partitions]

From the above we assume you have identified the relevant partitions on your system and this document will refer the partitions as follows. Partitions not needed for this kind of maintenance has intentionally been left out (e.g. *home*, *swap*).

  ------------------------------------------------------------------ ------------ -----------------------------------------------------------------------------------------------
  Partition                                                          Usage        Comment
  `/dev/sdyA`   EFI system   Required for EFI system and mounted on */boot/efi*
  `/dev/sdyB`   boot         Optional but mounted on */boot* The primary use is when GRUB cannot write to */* (eg. *f2fs*)
  `/dev/sdyC`   root         Required and for the root filesystem and mounted on */* - usually formatted using *ext4*
  ------------------------------------------------------------------ ------------ -----------------------------------------------------------------------------------------------

**Info**

------------------------------------------------------------------------

If your system is a BIOS/MBR system there is no efi partition. If your system is a BIOS/GPT system you will find an unformatted partion size 1-32MB of the bios boot partition type.

\

### [Use manjaro-chroot]

Manjaro deploys a script called `manjaro-chroot` takes an optional argument which will search the visible devices - scan the partitions for signs of an operating system. If more than one Linux operating system is found you will get a choice of which system to chroot otherwise the file */etc/fstab* from the system is used to mount the partitions and chroot into this system.This script is only available in live iso by default but you can get it in an installed system by installing `manjaro-tools-base` package.

[root \# ][ pamac install manjaro-tools-base [COPY TO CLIPBOARD]]

\

[root \# ][ manjaro-chroot -a [COPY TO CLIPBOARD]]

\

### [Manual chroot]

(Unnecessary if you have used `manjaro-chroot`) Mount the partitions using the designated temporary mountpoint and **always** start with *root*

[root \# ][ mount /dev/sdyC /mnt [COPY TO CLIPBOARD]]

\

**Info**

------------------------------------------------------------------------

With a [BTRFS filesystem](//wiki.manjaro.org/index.php?title=Btrfs "Btrfs"), you should note that the subvolumes must be mounted. That would be in such a case:

[root \# ][ mount -o subvol=@ /dev/sdyC /mnt [COPY TO CLIPBOARD]]

\

\
Then - if applicable - mount *boot*

[root \# ][ mount /dev/sdyB /mnt/boot [COPY TO CLIPBOARD]]

\

Then - if applicable - mount *efi*

[root \# ][ mount /dev/sdyA /mnt/boot/efi [COPY TO CLIPBOARD]]

\

Create the chroot environment and use bash as shell

[root \# ][ manjaro-chroot /mnt /bin/bash [COPY TO CLIPBOARD]]

\

\

## [Reinstall GRUB]

One possible cause why you are reading this document - is an unfinished update - which in turn can be caused by several situations - situation we will not dive into. To fix what ever caused this you should run a full system update including grub to ensure everything is in place.

[root \# ][ pacman -Syu grub [COPY TO CLIPBOARD]]

\

When the transaction as completed continue below using the section matching your system

### [BIOS System]

On a BIOS/GPT system there is no MBR and therefore no place to store the loader. The GPT partition specification allows for an unformatted partition of the BIOS boot partition type (0xEF02). The size of this partition can be as small as 1 mebibyte. The Calamares installer uses a fixed size of 32 mebibyte. On a BIOS/MBR system a part of the bootloader is written to the Master Boot Record for the primary disk.

The device is the **disk** (**not a partition**)

[root \# ][ grub-install \--force \--target=i386-pc \--recheck \--boot-directory=/boot /dev/sdy [COPY TO CLIPBOARD]]

\

Make sure the grub configuration is up-to-date

[root \# ][ grub-mkconfig -o /boot/grub/grub.cfg [COPY TO CLIPBOARD]]

\

### [EFI System]

**Info**

------------------------------------------------------------------------

You need to be in chroot for this procedure.

\
Reinstall grub

[root \# ][ grub-install \--target=x86_64-efi \--efi-directory=/boot/efi \--bootloader-id=manjaro \--recheck [COPY TO CLIPBOARD]]

\

Update the grub configuration

[root \# ][ grub-mkconfig -o /boot/grub/grub.cfg [COPY TO CLIPBOARD]]

\

\

**EFI grub install messages**

------------------------------------------------------------------------

EFI variables are not supported on this system.

Verify the existance of an EFI system partition

[root \# ][ lsblk -o PATH,PTTYPE,PARTTYPE,FSTYPE,PARTTYPENAME [COPY TO CLIPBOARD]]

\

Verify the efi filesystem is loaded

[root \# ][ ls /sys/firmware/efi [COPY TO CLIPBOARD]]

\

Exit chroot

[root \# ][ exit [COPY TO CLIPBOARD]]

\

Try loading the efi filesystem

[root \# ][ modprobe efivarfs [COPY TO CLIPBOARD]]

\

Re-enter chroot

[root \# ][ manjaro-chroot /mnt /bin/bash [COPY TO CLIPBOARD]]

\

Then mount the efi filesystem

[root \# ][ mount -t efivarfs efivarfs /sys/firmware/efi/efivars [COPY TO CLIPBOARD]]

\

Verify the efi filesystem is loaded

[root \# ][ ls /sys/firmware/efi [COPY TO CLIPBOARD]]

\

If successfull re-run above installation commands

## [Updating grub]

Sometimes there is an update for the GRUB package itself. So far, the grub package is updated, but the new GRUB Version is not automatically installed in the boot area.

You can do this manually following the instructions above. Or you can install the Grub Maintainer Script *install-grub*. It should work flawless for the majority of people, but SecureBoot, ZFS and fancy encryptions are not supported yet.

[root \# ][ pacman -Syu install-grub [COPY TO CLIPBOARD]]

\

Then once run

[root \# ][ install-grub [COPY TO CLIPBOARD]]

\

The package includes a hook that will reinstall the bootloader when needed from now on at every update of grub.

### [Additional Information]

Some things around grub can be confusing.

#### [package version of grub]

Its the version of the grub-package present in your filesystem. But this version changing does *not* update the installed grub-bootloader.

#### [grub-bootloader version]

This can only been shown while you are in the Grub menu (that won't show up while booting by default, you need to hit \[shift\] during boot). Hit the key \[E\] and your will see the Grub version on top.

#### [update-grub]

Does *not* update the installed bootloader. The 'update' is more about updating configuration. Think of this more as 'applying settings'. (\~ equal to grub-mkconfig -o /boot/grub/grub.cfg)

### [install-grub]

is the script (background maintainer) that does update the installed bootloader when you download a Stable Release/Unstable Release Version, which included a new Grub Version.

## [Troubleshooting]

### [Manjaro is not recognized]

If Manjaro wasn\'t recognized after an update-grub then probably your Manjaro installation is missing the package lsb-release.

## [See also]

-   [UEFI Install Guide](http://wiki.manjaro.org/index.php?title=UEFI_-_Install_Guide)
-   [GRUB on Arch wiki](https://wiki.archlinux.org/index.php/GRUB)