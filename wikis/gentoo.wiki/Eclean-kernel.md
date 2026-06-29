This page contains [[changes](https://wiki.gentoo.org/index.php?title=Kernel/Removal&oldid=1408182&diff=1439123#Using_eclean-kernel)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Kernel/Removal/de "Kernel/Deinstallation (61% translated)")
-   [English]
-   [Türkçe](https://wiki.gentoo.org/wiki/Kernel/Removal/tr "Çekirdek/Kaldırma (32% translated)")
-   [español](https://wiki.gentoo.org/wiki/Kernel/Removal/es "Núcleo/Eliminación (35% translated)")
-   [français](https://wiki.gentoo.org/wiki/Kernel/Removal/fr "Noyau/Suppression (71% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/Kernel/Removal/it "Kernel/Rimozione (35% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Kernel/Removal/hu "Kernel/Eltávolítás (71% translated)")
-   [português do Brasil](https://wiki.gentoo.org/wiki/Kernel/Removal/pt-br "Kernel/Remoção (61% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Kernel/Removal/ru "Ядро/Удаление (94% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Kernel/Removal/zh-cn "内核/移除 (32% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Kernel/Removal/ja "カーネル/削除 (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Kernel/Removal/ko "Kernel/Removal (32% translated)")

This article describes the **removal of old [kernels](https://wiki.gentoo.org/wiki/Kernel "Kernel")**.

## Contents

-   [[1] [Removing kernel sources]](#Removing_kernel_sources)
    -   [[1.1] [Protecting kernel sources]](#Protecting_kernel_sources)
-   [[2] [Removing kernel leftovers]](#Removing_kernel_leftovers)
    -   [[2.1] [Using eclean-kernel]](#Using_eclean-kernel)
    -   [[2.2] [Manual removal]](#Manual_removal)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Can not clean old kernels with eclean-kernel]](#Can_not_clean_old_kernels_with_eclean-kernel)

## [Removing kernel sources]

After a new kernel is installed and if it works satisfactorily, the old kernel can be removed. To remove the old kernel sources, emerge\'s *\--depclean* option (short form *-c*) can be used to remove all old or unused versions of a slotted package, e.g. for [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]].

`root `[`#`]`emerge --ask --depclean gentoo-sources:xx.yy.zzz`

Be sure to verify that it is not removing the sources for the currently running kernel (See [kernel upgrade](https://wiki.gentoo.org/wiki/Kernel/Upgrade "Kernel/Upgrade") article on how to upgrade.)

### [Protecting kernel sources]

If newer kernel sources has been merged and [emerge \--depclean] is run before switching to the newer sources, the current sources will be removed. To stay with the current sources, this removal is not wanted, because the sources may be needed e.g. for updating external kernel modules. It\'s therefore good practice to add the specific kernel version to the world file to protect it from `--depclean` operations.

`root `[`#`]`emerge --ask --noreplace gentoo-sources:xx.yy.zzz`

Alternatively, you can explicitly exclude the sources from `--depclean`:

`root `[`#`]`emerge --depclean --exclude=sys-kernel/gentoo-sources`

This will leave all of your kernel source build directories alone during cleanup, which you can then clean up with tools like eclean-kernel, referenced below.

Another way to prevent removal of the kernel sources located in [/usr/src] is to add the path to the `UNINSTALL_IGNORE` variable in [make.conf]:

[FILE] **`/etc/portage/make.conf`Prevent kernel sources from being removed**

    UNINSTALL_IGNORE="/lib/modules/* /usr/src/linux-*"

This won\'t prevent removal of the package version, but will protect the files. Note that `/lib/modules/*` is the Portage default, and the new filename pattern is added to it.

## [Removing kernel leftovers]

### [Using eclean-kernel]

[[[app-admin/eclean-kernel]](https://packages.gentoo.org/packages/app-admin/eclean-kernel)[]] is a simple tool for old kernel cleanup/removal. It removes both built kernel files and build directories if they\'re no longer reference by any preserved kernel.

See [eclean-kernel \--help] post-installation for usage instructions:

`user `[`$`]`eclean-kernel --help`

    usage: eclean-kernel [-h] [-V] [-A] [-l] [-p] [-b BOOTLOADER] [-L LAYOUT] [-r ROOT] [-a] [-d] [-n NUM] [-s SORT_ORDER]
                          [-D] [-M] [--no-bootloader-update] [--no-kernel-install] [-x EXCLUDE]

     Remove old kernel versions, keeping either N newest kernels (with -n) or only those which are referenced by a bootloader
     (with -a).

     optional arguments:
       -h, --help            show this help message and exit
       -V, --version         show program's version number and exit

     action control:
       -A, --ask             Ask before removing each kernel
       -l, --list-kernels    List kernel files and exit
       -p, --pretend         Print the list of kernels to be removed and exit

     system configuration:
       -b BOOTLOADER, --bootloader BOOTLOADER
                             Bootloader used (auto, lilo, grub2, grub, yaboot, symlinks)
       -L LAYOUT, --layout LAYOUT
                             Layout used (auto, blspec, std)
       -r ROOT, --root ROOT  Alternate filesystem root to use

     kernel selection:
       -a, --all             Remove all kernels unless used by bootloader
       -d, --destructive     Destructive mode: remove kernels even when referenced by bootloader
       -n NUM, --num NUM     Leave only newest NUM kernels (see also: --sort-order)
       -s SORT_ORDER, --sort-order SORT_ORDER
                             Kernel sort order (mtime, version); default: version

     misc options:
       -D, --debug           Enable debugging output
       -M, --no-mount        Disable (re-)mounting /boot if necessary
       --no-bootloader-update
                             Do not update bootloader configuration after removing kernels (if supported by the bootloader
       --no-kernel-install   Do not call kernel-install while removing kernels (if installed)
       -x EXCLUDE, --exclude EXCLUDE
                             Exclude kernel parts from being removed (comma-separated, supported parts: vmlinuz, systemmap,
                             config, initramfs, modules, build, misc, emptydir)

For example, to keep three newest kernels around:

`root `[`#`]`eclean-kernel -n 3`

** Warning**\
If you use [eclean-kernel -n 1], be sure to check the boot entries. It may be empty, if you reboot at this time, and you will only be able to rewrite the boot entry through a liveCD.

### [Manual removal]

[Portage](https://wiki.gentoo.org/wiki/Portage "Portage") however only removes the files it installed - the files generated during the kernel build and installation remain. They can be safely removed.

-   When a kernel is built in the source directory, files generated during the build process remain, and are not removed by Portage:

`root `[`#`]`rm -r /usr/src/linux-X.Y.Z`

-   During kernel setup, the kernel modules are copied to a sub directory of [/lib/modules/]:

`root `[`#`]`rm -r /lib/modules/X.Y.Z`

-   The old files in [/boot] can also be removed:

`root `[`#`]`rm /boot/vmlinuz-X.Y.Z`

`root `[`#`]`rm /boot/System.map-X.Y.Z`

`root `[`#`]`rm /boot/config-X.Y.Z`

`root `[`#`]`rm /boot/initramfs-X.Y.Z`

-   Lastly, remove all leftover entries from the [bootloader\'s](https://wiki.gentoo.org/wiki/Bootloader "Bootloader") config file.

## [Troubleshooting]

### [Can not clean old kernels with eclean-kernel]

This may have triggered a known bug in eclean-kernel: [[[bug #946132]](https://bugs.gentoo.org/show_bug.cgi?id=946132)[]]. Here is a possible scenario for reference: if your system initially used [systemd-boot] and later switched to [grub2], but the residual file layout under [/efi] was not cleared, then this bug may be triggered. The solution is to clean up the [/efi] layout or specify layout `-L std`.