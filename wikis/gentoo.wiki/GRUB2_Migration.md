This page contains [[changes](https://wiki.gentoo.org/index.php?title=GRUB2_Migration&oldid=1245986&diff=1308894)] which are not marked for translation.

**[] Archived article**\
\
This article is **archived (obsolete)**. Contents are surely incorrect for current usage, and are intended for historical reference only.

[GRUB2](https://wiki.gentoo.org/wiki/GRUB2 "GRUB2") has been out for a very long time, these instructions will probably rarely be needed nowadays.

\
TLDR: **Do not use this article!**

Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/GRUB2_Migration/es "Migración de GRUB2 (84% translated)")
-   [français](https://wiki.gentoo.org/wiki/GRUB2_Migration/fr "GRUB2 Migration (100% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/GRUB2_Migration/hu "GRUB2 migráció (100% translated)")
-   [polski](https://wiki.gentoo.org/wiki/GRUB2_Migration/pl "GRUB2 Migration/pl (2% translated)")
-   [português do Brasil](https://wiki.gentoo.org/wiki/GRUB2_Migration/pt-br "GRUB2 Migração (57% translated)")
-   [čeština](https://wiki.gentoo.org/wiki/GRUB2_Migration/cs "Přechod na GRUB2 (33% translated)")
-   [русский](https://wiki.gentoo.org/wiki/GRUB2_Migration/ru "Миграция на GRUB2 (100% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/GRUB2_Migration/zh-cn "GRUB2 迁移 (59% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/GRUB2_Migration/ja "GRUB2への移行 (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/GRUB2_Migration/ko "GRUB2 Migration (82% translated)")

This guide provides instructions for smooth migration from [GRUB Legacy](https://wiki.gentoo.org/wiki/GRUB_Legacy "GRUB Legacy") to [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB").

## Contents

-   [[1] [Background]](#Background)
    -   [[1.1] [What\'s GRUB?]](#What.27s_GRUB.3F)
    -   [[1.2] [Why migrate?]](#Why_migrate.3F)
-   [[2] [Migration to GRUB2]](#Migration_to_GRUB2)
    -   [[2.1] [Boot drive]](#Boot_drive)
    -   [[2.2] [Installing and configuring GRUB2]](#Installing_and_configuring_GRUB2)
    -   [[2.3] [Chainloading GRUB2 from GRUB Legacy to test the setup]](#Chainloading_GRUB2_from_GRUB_Legacy_to_test_the_setup)
    -   [[2.4] [Replacing and removing GRUB Legacy]](#Replacing_and_removing_GRUB_Legacy)
-   [[3] [Maintaining GRUB2]](#Maintaining_GRUB2)

## [Background]

### [][What\'s GRUB?]

GRUB is one of the most commonly found boot loaders in use on non-embedded Linux machines. The role of GRUB is to facilitate the Linux kernel being loaded from the disk into memory and start executing the Linux kernel.

### [][Why migrate?]

Firstly, GRUB Legacy is no longer maintained and as such no longer receives updates. GRUB Legacy was created at a time when the developers felt safe in making several assumptions which no longer hold true today. For example, GRUB Legacy is unable to boot from disks larger than 2 TB and assumes that newer filesystems wouldn\'t come to replace [/boot].

GRUB2 aims to be more robust, more portable, more powerful and is maintained with a cleaner code base. GRUB2 supports more hardware configurations, more filesystems and more drive layouts than its predecessor.

## [Migration to GRUB2]

Migration to GRUB2 is fairly straightforward: it will be pulled in as part of the regular upgrade process by the package manager. If it is not pulled in automatically, it can always be merged via the `sys-boot/grub:2` package atom:

`root `[`#`]`emerge --ask sys-boot/grub:2`

### [Boot drive]

The first important part is to understand which drive is bootable. For those who followed the Gentoo Handbook it should be [/dev/sda]. For those who are uncertain, the easiest way to find out is to look at the existing GRUB Legacy configuration. Viewing the [/boot/grub/grub.conf] file is the main place to check.

** Note**\
Be sure the [/boot] partition is mounted to be able to view these files. It should be as simple as

`root `[`#`]`mount /boot`

The [grub.conf] file will look something like this:

[FILE] **`/boot/grub/grub.conf`**

    default 0
    timeout 30
    splashimage=(hd0,0)/boot/grub/splash.xpm.gz

    title Gentoo Linux 3.2.12
    root (hd0,0)
    kernel /boot/kernel-3.2.12-gentoo root=/dev/sda3 quiet dolvm
    initrd /boot/initramfs-genkernel-x86_64-3.2.12-gentoo

Based on the above file it is possible to know that `(hd0)` is the boot drive but we must map this to a real device. To know this, look at the [/boot/grub/device.map] file. An example one is provided below.

[FILE] **`/boot/grub/device.map`**

    (fd0) /dev/fd0
    (hd0) /dev/sda
    (hd1) /dev/sdb

** Note**\
When suspecting that [/boot/grub/device.map] is not accurate, run the following command to recreate the file:

`root `[`#`]`grub-install --recheck /dev/sda`

Based on the above file we know that [/dev/sda] is the boot drive.

### [Installing and configuring GRUB2]

The next step is to install and configure GRUB2 for the [/boot] partition without removing GRUB Legacy from the drive\'s Master Boot Record (MBR). The example below uses [/dev/sda] --- replace it with the correct boot drive path.

First install the necessary GRUB2 files to [/boot/grub].

`root `[`#`]`grub-install --grub-setup=/bin/true /dev/sda`

    Installation finished. No error reported.

** Warning**\
The `--grub-setup=/bin/true` option tells [grub-install] to *not* install GRUB2 in the MBR. If this option is omitted, GRUB Legacy will be overwritten and [chainloading GRUB2 from GRUB Legacy later on](https://wiki.gentoo.org/wiki/GRUB2_Migration#Chainloading_GRUB2_from_GRUB_Legacy_to_test_the_setup "GRUB2 Migration") will not be possible.

Now we can scan the available kernels and generate a suitable config file to [/boot/grub/grub.cfg]. Skip this step when using a [Manual Configuration](https://wiki.gentoo.org/wiki/GRUB2_Quick_Start#Manual_configuration "GRUB2 Quick Start").

`root `[`#`]`grub-mkconfig -o /boot/grub/grub.cfg`

    Generating grub.cfg ...
    Found linux image: /boot/kernel-3.2.12-gentoo
    Found initrd image: /boot/initramfs-genkernel-x86_64-3.2.12-gentoo
    done

** Warning**\
GRUB2 uses the configuration file [/boot/grub/grub.**cfg**] whereas GRUB Legacy used [/boot/grub/grub.**conf**] so please make sure not to use the old file by mistake, e.g. by using tab-completion if the old file is still there.

** Note**\
[grub-mkconfig] has strict naming requirements for kernels and initramfs images. A kernel must be named `kernel-$` or `vmlinuz-$` while an initramfs must be named `initramfs-$.img`, `initramfs-genkernel-$`, `initramfs-genkernel-$-$`, `initrd-$.img`, `initrd.img-$`, `initrd-$.gz`, or `initrd-$`. These files must be available in [/boot].

** Note**\
The file [/etc/default/grub] controls the operation of [grub-mkconfig]. If parameters need to be passed on to the kernel (for instance when using genkernel and booting from LVM or software RAID), edit that file before generating [/boot/grub/grub.cfg] like so:

`root `[`#`]`nano /etc/default/grub`

Have a look at [GRUB configuration](https://wiki.gentoo.org/wiki/GRUB#Configuration "GRUB") on the Gentoo Wiki or the [official GRUB2 manual](http://www.gnu.org/software/grub/manual/html_node/Simple-configuration.html) to decide how to modify the file. Most users will need to change `GRUB_CMDLINE_LINUX` to specify parameters to be passed on the kernel command line.

### [[] Chainloading GRUB2 from GRUB Legacy to test the setup]

Because a broken GRUB configuration could mean an unbootable system, we want to test our GRUB2 configuration before making it permanent. To do this we will chainload GRUB2 from GRUB Legacy. This is done by adding a new section into [/boot/grub/grub.conf]. An example is shown below.

** Note**\
Be aware that the root partition may be different from `(hd0,0)` used in the example, and make sure to reuse the same root value from the [/boot/grub/grub.conf] configuration file.

[FILE] **`/boot/grub/grub.conf`**

    default 0
    timeout 30
    splashimage=(hd0,0)/boot/grub/splash.xpm.gz

    title GRUB2 Chainload
    root (hd0,0)
    kernel /boot/grub/i386-pc/core.img
    boot

    title Gentoo Linux 3.2.12
    root (hd0,0)
    kernel /boot/kernel-3.2.12-gentoo root=/dev/sda3 quiet dolvm
    initrd /boot/initramfs-genkernel-x86_64-3.2.12-gentoo

At this point the machine should be rebooted, and `GRUB2 Chainload` selected from the GRUB menu when the machine begins to boot. Another GRUB menu will be presented which should advertise itself as GRUB 2.0.0 or higher at the top and show the available kernel(s) to boot. Should this not work, simply reboot the system and pick the normal boot option instead of `GRUB2 Chainload`.

### [Replacing and removing GRUB Legacy]

If everything worked successfully, replace GRUB Legacy and remove it from the system.

** Warning**\
Since the system has been rebooted, it might be necessary to mount [/boot] again. Make sure to use the right boot drive path instead of [/dev/sda] as this is merely an example. If [/boot] is not mounted before running [grub-install], the system will become unbootable.

** Note**\
As previously mentioned, if GRUB2 was emerged with the `multislot` USE flag then [grub2-install] must be used instead of [grub-install]. In this case, after GRUB Legacy is removed from the system in the next step, GRUB2 should be re-emerged without the `multislot` USE flag so that [grub-install] and [grub-mkconfig] can become GRUB2 commands.

`root `[`#`]`grub-install /dev/sda`

    Installation finished. No error reported.

At this point use the package manager to remove `sys-boot/grub:0`.

`root `[`#`]`emerge --ask -vc sys-boot/grub:0`

The migration is now complete.

## [Maintaining GRUB2]

Whenever a new kernel is installed, perform the next step so that the GRUB2 configuration recognizes the new kernel (except when using a [manual configuration](https://wiki.gentoo.org/wiki/GRUB2_Quick_Start#Manual_configuration "GRUB2 Quick Start")).

** Note**\
Make sure the [/boot] partition is mounted for this step.

`root `[`#`]`grub-mkconfig -o /boot/grub/grub.cfg`

    Generating grub.cfg ...
    Found linux image: /boot/kernel-3.3.8-gentoo
    Found initrd image: /boot/initramfs-genkernel-x86_64-3.3.8-gentoo
    Found linux image: /boot/kernel-3.2.12-gentoo
    Found initrd image: /boot/initramfs-genkernel-x86_64-3.2.12-gentoo
    done

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Cardoe**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*