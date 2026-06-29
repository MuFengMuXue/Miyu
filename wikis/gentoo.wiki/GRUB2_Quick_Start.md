This page contains [[changes](https://wiki.gentoo.org/index.php?title=GRUB2_Quick_Start&oldid=1245962&diff=1292468)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/GRUB2_Quick_Start/de "GRUB2 Quick Start (100% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/GRUB2_Quick_Start/es "Guía rápida de GRUB2 (43% translated)")
-   [français](https://wiki.gentoo.org/wiki/GRUB2_Quick_Start/fr "GRUB2 Démarrage Rapide (43% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/GRUB2_Quick_Start/hu "GRUB2 gyorstalpaló (100% translated)")
-   [português do Brasil](https://wiki.gentoo.org/wiki/GRUB2_Quick_Start/pt-br "GRUB2 Começo Rápido (24% translated)")
-   [русский](https://wiki.gentoo.org/wiki/GRUB2_Quick_Start/ru "GRUB2 — Быстрый старт (100% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/GRUB2_Quick_Start/ja "GRUB2 クイックスタート (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/GRUB2_Quick_Start/ko "GRUB2 간단하게 시작하기 (43% translated)")

This article provides information on how to get up and running with **[GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB")** in the simplest configurations. For a migration from [GRUB Legacy](https://wiki.gentoo.org/wiki/GRUB_Legacy "GRUB Legacy") to GRUB2, see [GRUB2 Migration](https://wiki.gentoo.org/wiki/GRUB2_Migration "GRUB2 Migration").

## Contents

-   [[1] [Installing GRUB software]](#Installing_GRUB_software)
-   [[2] [Activating the GRUB boot loader]](#Activating_the_GRUB_boot_loader)
-   [[3] [Automatic configuration]](#Automatic_configuration)
    -   [[3.1] [Kernel naming scheme]](#Kernel_naming_scheme)
    -   [[3.2] [Silent kernel decompression]](#Silent_kernel_decompression)
    -   [[3.3] [systemd]](#systemd)
    -   [[3.4] [Loading another operating system]](#Loading_another_operating_system)
-   [[4] [Manual configuration]](#Manual_configuration)
-   [[5] [See also]](#See_also)

## [[] Installing GRUB software]

To install GRUB, first set the `GRUB_PLATFORMS` variable with one or more appropriate values in the system\'s [make.conf]. If unset, GRUB will guess which platform to use on the system. It guesses `pc` (which is the MBR style of installation) for **[x86]**/**[amd64]** architectures.

Standard PC (BIOS) support:

[FILE] **`/etc/portage/make.conf`PC BIOS GRUB_PLATFORMS example**

    GRUB_PLATFORMS="pc"

UEFI on amd64:

[FILE] **`/etc/portage/make.conf`64-bit UEFI GRUB_PLATFORMS example**

    GRUB_PLATFORMS="efi-64"

Both standard PC (BIOS) and UEFI support:

[FILE] **`/etc/portage/make.conf`Multiple GRUB_PLATFORMS example**

    GRUB_PLATFORMS="efi-64 pc"

After the variable is set, emerge the software:

`root `[`#`]`emerge --ask sys-boot/grub`

## [[] Activating the GRUB boot loader]

Mount [/boot] if applicable:

`root `[`#`]`mount /boot`

When using an EFI platform, make sure that the [EFI System Partition](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition") is available (mounted) at [/boot/efi]. This can either be through a specific mount point (at [/boot/efi]) or by having an entire [/boot] partition formatted with the FAT filesystem. This will effectually render [/boot] into a large EFI System Partition.

Presuming only [/boot/efi] is FAT:

`root `[`#`]`mount /boot/efi`

Run the [grub-install] utility to copy the relevant files to [/boot/grub]. On the PC platform, this also installs a boot image to the Master Boot Record (MBR) or a partition\'s boot sector.

To install GRUB to the MBR:

`root `[`#`]`grub-install /dev/sda`

    Installation finished. No error reported.

To install GRUB on an EFI capable system:

`root `[`#`]`grub-install --target=x86_64-efi`

    Installation finished. No error reported.

The [grub-install] command accepts a `--target` option to specify which CPU/Platform to install. If unspecified, [grub-install] will make a guess: on **[x86]**/**[amd64]** it will use the `i386-pc` value by default.

## [[] Automatic configuration]

GRUB is configured by using the [grub-mkconfig] program to generate a configuration file.

[grub-mkconfig] generates the configuration file based on template sections located in [/etc/grub.d]. The default templates should cover most common boot setups.

`user `[`$`]`ls /etc/grub.d`

    00_header  10_linux  20_linux_xen  30_os-prober  40_custom  41_custom  README

The behavior of these templates can be controlled by setting variables in [/etc/default/grub]. See the [GRUB manual](http://www.gnu.org/software/grub/manual/html_node/Simple-configuration.html) for more information.

### [[] Kernel naming scheme]

In order for [grub-mkconfig] to detect the available Linux kernel(s), their names must start with [vmlinuz-] or [kernel-].

For example:

[CODE] **Example kernel names that GRUB can detect**

    /boot/vmlinuz-3.4.3
     /boot/kernel-2.6.39-gentoo
     /boot/kernel-genkernel-x86_64-3.17.1-gentoo-r1

When using an [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs"), its name should start with [initramfs-] or [initrd-] and end with [.img]. The version must match one of a kernel image. File names generated by [[genkernel](https://wiki.gentoo.org/wiki/Genkernel "Genkernel")] will also work.

For example:

[CODE] **Example initramfs names that GRUB can detect**

    /boot/initrd.img-3.4.3
     /boot/initrd-3.4.3.img
     /boot/initrd-3.4.3.gz
     /boot/initrd-3.4.3
     /boot/initramfs-3.4.3.img
     /boot/initramfs-genkernel-3.4.3-gentoo
     /boot/initramfs-genkernel-x86_64-2.6.39-gentoo

To generate the [grub.cfg] file, execute the [grub-mkconfig] command like so:

`root `[`#`]`grub-mkconfig -o /boot/grub/grub.cfg`

    Generating grub.cfg ...
    Found linux image: /boot/vmlinuz-3.2.9
    done

### [[] Silent kernel decompression]

To silence kernel decompression at boot time, edit [/etc/default/grub] and add `quiet` to the `GRUB_CMDLINE_LINUX_DEFAULT` variable.

[FILE] **`/etc/default/grub`Silent decompression example**

    GRUB_CMDLINE_LINUX_DEFAULT="quiet"

### [[] systemd]

To boot systemd while using GRUB configure the `GRUB_CMDLINE_LINUX` variable look like this:

** Important**\
This is no longer necessary with [[[sys-apps/systemd]](https://packages.gentoo.org/packages/sys-apps/systemd)[]] when the `sysv-utils` USE is enabled. This defaults to on with at least version 239 in Gentoo

[FILE] **`/etc/default/grub`Systemd example**

    GRUB_CMDLINE_LINUX="init=/usr/lib/systemd/systemd"

### [[] Loading another operating system]

[grub-mkconfig] can also generate configurations to load *other* operating systems. This requires the [[[sys-boot/os-prober]](https://packages.gentoo.org/packages/sys-boot/os-prober)[]] package.

To boot Windows, the [[[sys-fs/ntfs3g]](https://packages.gentoo.org/packages/sys-fs/ntfs3g)[]] also needs to be installed. It allows for the [grub-mkconfig] utility to probe NTFS filesystems.

## [[] Manual configuration]

Use of [grub-mkconfig] is not required. The [grub.cfg] file can be edited manually as well.

Migrating from the GRUB Legacy config format to the GRUB 2 config format is usually quite simple, requiring a few minor syntax changes.

[DIFF] [grub.conf]

GRUB Legacy

    timeout 5

    title Gentoo Linux 3.2.12
    root (hd0,0)
    kernel /boot/kernel-3.2.12-gentoo root=/dev/sda3

GRUB

    timeout=5

    menuentry 'Gentoo Linux 3.2.12'

** Note**\
GRUB Legacy partition numbers start at 0, while GRUB\'s start at 1. Drive numbers start at 0 with both bootloaders.

## [[] See also]

-   [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB") - The \'full\' GRUB article contains more information and an extensive list of resources.