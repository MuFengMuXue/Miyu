** See also**\
Users may prefer using Gentoo\'s build tool [catalyst] to do this task. See [Catalyst/Custom Media Image](https://wiki.gentoo.org/wiki/Catalyst/Custom_Media_Image "Catalyst/Custom Media Image") for more information.

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Examine the structure of the ISO:]](#Examine_the_structure_of_the_ISO:)
-   [[3] [Create The Work Space]](#Create_The_Work_Space)
-   [[4] [Build kernel]](#Build_kernel)
-   [[5] [The customrescuecd64 directory must contain these subdirectories:]](#The_customrescuecd64_directory_must_contain_these_subdirectories:)
-   [[6] [Creating the squashfs]](#Creating_the_squashfs)
-   [[7] [Bootloader]](#Bootloader)
-   [[8] [Syslinux]](#Syslinux)
-   [[9] [Grub]](#Grub)

## [Overview]

This document will walk readers through the steps to create a Gentoo stage4 inside a squashfs and subsequently use it in a bootable ISO9660 image.

The steps are to make a Gentoo Install inside a directory. Add or remove packages to the usage needs. This will become customrescuecd-squash, which will be the root filesystem in the CD. This will then be packaged with a syslinux /boot to make the bootable ISO9660 image.

Burning the image to a CD or making a bootable USB stick will not be addressed.

## [Examine the structure of the ISO:]

-   ./boot/grub/font.pf2
-   ./boot/grub/grub.cfg \<\-- Grub Configuration File for EFI BOOT
-   ./boot/grub/x86_64-efi
-   ./boot/grub/x86_64-efi/all_video.mod
-   ./boot/grub/x86_64-efi/efi_gop.mod
-   ./boot/grub/x86_64-efi/efi_uga.mod
-   ./boot/grub/x86_64-efi/gfxterm.mod
-   ./boot/grub/x86_64-efi/video.mod
-   ./boot/grub/x86_64-efi/videoinfo.mod
-   ./boot/grub/x86_64-efi/videotest.mod
-   ./boot/memtest86plus/memtest
-   ./boot/memtest86plus/memtest.bin \<\-- Memtest kernel for bios boot
-   ./boot/syslinux/chain.c32
-   ./boot/syslinux/syslinux.cfg \<\-\-- Main Syslinux Configuration File
-   ./boot/syslinux/customresccd.cfg
-   ./boot/syslinux/customresccd_head.cfg
-   ./boot/syslinux/customresccd_pxe.cfg
-   ./boot/syslinux/customresccd_sys.cfg
-   ./boot/syslinux/customresccd_tail.cfg
-   ./boot/syslinux/isohdpfx.bin \<\-\-- Syslinux MBR for Bios Boot
-   ./boot/syslinux/isolinux.bin \<\-\-- Syslinux Image
-   ./boot/syslinux/boot.cat \<\-\-- Syslinux Boot Catalogue
-   ./boot/syslinux/ldlinux.c32
-   ./boot/syslinux/ldlinux.sys
-   ./boot/syslinux/libcom32.c32
-   ./boot/syslinux/libutil.c32
-   ./boot/syslinux/memdisk
-   ./boot/syslinux/poweroff.c32
-   ./boot/syslinux/pxelinux.0
-   ./boot/syslinux/reboot.c32
-   ./boot/syslinux/vesamenu.c32
-   ./boot/syslinux/whichsys.c32
-   ./boot/x86_64/customrescue64 \<\-- CustomRescueCd KERNEL
-   ./customresccd/x86_64/customrescuecd.sfs \<\-\-- SquashFS
-   ./customresccd/x86_64/customrescuecd.sha512 \<\-\-\-- Sha512 of Squashfs
-   ./EFI/boot/bootx64.efi \< \-\-\-- Grub Efi Executable for usb stick boot
-   ./EFI/customiso/grub.img \<\-\-- Grub Partition in append to iso for efi boot that contain .efi executable

## [Create The Work Space]

It is recommended to keep two terminals open, one for the stage 4 chroot and another needed to create the squash and the iso ahead.

[/mnt/customrescuecd-squash] is for the stage4. This will be turned into a squashfs later.

[/mnt/customrescuecd64] is for the files that will become the ISO9660 filesystem, including the squashfs above.

`root `[`#`]`mkdir /mnt/customrescuecd-squash /mnt/customrescuecd64 /mnt/customrescuecd64/boot`

Download a Gentoo Stage 3, unpack it to [/mnt/customrescuecd-squash], and chroot into it and build the system following the Gentoo [Handbook](https://wiki.gentoo.org/wiki/Handbook "Handbook") and other guides as necessary.

Install necessary tools to the system:

`root `[`#`]`emerge -1avn squashfs-tools syslinux grub genkernel gentoo-sources`

## [Build kernel]

Use [genkernel] to make a kernel and initramfs, add extra parameters as necessary (see [Genkernel](https://wiki.gentoo.org/wiki/Genkernel "Genkernel") for details):

`root `[`#`]`genkernel --bootdir=/mnt/customrescuecd64/boot --firmware all`

## [The customrescuecd64 directory must contain these subdirectories:]

-   boot/syslinux
-   boot/grub/x86_64-efi
-   boot/memtest86plus
-   boot/x86_64
-   EFI/boot
-   EFI/customiso
-   customresccd/x86_64

## [Creating the squashfs]

Make an excludes file with the following content.

[FILE] **`exclude.txt`**

    proc/*
    sys/*
    dev/*
    run/*
    boot/*
    root/*
    var/cache/edb/*
    var/db/pkg/*
    var/db/repos/gentoo/*
    var/db/repos/local/*
    var/db/repos/palemoon/*
    var/tmp/portage/*
    var/cache/distfiles/*
    var/cache/binpkgs/*
    var/log/*
    var/tmp/*
    usr/include/*
    usr/src/*
    etc/kernels/*
    etc/portage/*

Add any other files and directories to be excluded from the squashfs

Build the squashfs using the exclude.txt file created above:

`root `[`#`]`mksquashfs /mnt/customresccd-squash/ /mnt/customrescuecd64/customresccd/x86_64/customrescuecd.sfs -wildcards -ef exclude.txt -b 1024K -comp xz -progress -processors 4 -Xdict-size 100%`

## [Bootloader]

## [Syslinux]

Download the syslinux cfg from [syslinux.cfg.tar.xz](//sourceforge.net/projects/customrescuecd/files/SDK/syslinux.cfg.tar.xz) and explode into customrescuecd64/boot/syslinux/ the content of this directory must be the one that follow! All \*.c32 and memdisk isolinux.bin boot.cat pxelinux.0 isohdpfx.bin file, then copy the stage4 at folder /usr/share/syslinux/

-   customresccd_tail.cfg
-   poweroff.c32
-   customresccd_head.cfg
-   boot.cat
-   syslinux.cfg
-   pxelinux.0
-   reboot.c32
-   isohdpfx.bin
-   libcom32.c32
-   whichsys.c32
-   chain.c32
-   ldlinux.sys
-   memdisk
-   vesamenu.c32
-   isolinux.bin
-   customresccd_pxe.cfg
-   ldlinux.c32
-   customresccd_sys.cfg
-   customresccd.cfg
-   libutil.c32

## [Grub]

in the directory customrescuecd64/boot/grub/x86_64-efi/ copy the files all_video.mod efi_gop.mod efi_uga.mod gfxterm.mod videoinfo.mod videotest.mod from /usr/lib/grub/x86_64-efi/ of your stage4

download the [font.pf2](//sourceforge.net/projects/customrescuecd/files/SDK/font.pf2) in the directory customrescuecd64/boot/grub/

Create the file [/mnt/customrescuecd64/boot/grub/grub.cfg] adjusting kernel and initramfs versions as necessary:

[FILE] **`/mnt/customrescuecd64/boot/grub/grub.cfg`**

    set timeout=90
    set default=0
    set fallback=1
    set pager=1

    if loadfont /boot/grub/font.pf2 ; then
        set gfxmode=auto
        insmod efi_gop
        insmod efi_uga
        insmod gfxterm
        insmod all_video
        insmod videotest
        insmod videoinfo
        terminal_output gfxterm
    fi

    menuentry "Boot CustomRescueCd"

cd into customrescuecd64/EFI/customiso/

create a empty file named grub.img to create the boot efi partition

`root `[`#`]`dd if=/dev/zero of=grub.img bs=1M count=2`

format it with FAT12 filesystem

`root `[`#`]` mkfs.vfat -f 1 -F 32 grub.img `

mount grub.img into /boot/efi of your stage4

`root `[`#`]` mount -t vfat grub.img customrescuecd-squash/boot/efi/ `

from your stage4 chroot

`root `[`#`]` mkdir -p /boot/efi/efi/boot `

`root `[`#`]` cd /boot/efi/efi/boot `

create the grub image efi boot executable

`root `[`#`]` grub-mkimage -o bootx64.efi -O x86_64-efi -p /boot/grub boot linux linux16 normal configfile part_gpt part_msdos fat iso9660 udf test keystatus loopback regexp probe efi_gop efi_uga all_video gfxterm font echo read help ls cat halt reboot `