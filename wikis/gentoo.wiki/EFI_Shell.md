**Resources**

[[]][Home](https://www.tianocore.org)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Unified_Extensible_Firmware_Interface#UEFI_shell "wikipedia:Unified Extensible Firmware Interface")

[[]][SourceForge](https://sourceforge.net/projects/efi-shell)

UEFI firmware is great. It\'s easy to use and transparent - the booting happens from a FAT formatted partition called the [EFI System Partition](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition") (ESP). The files that can be loaded are in the EFI executable format and have a `.efi` suffix. UEFI implementations are supposed to provide users with a built-in boot manager whose entries are stored in the NVRAM. This boot manager should allow the registration and selection of entries. The entries can be adjusted using [Efibootmgr](https://wiki.gentoo.org/wiki/Efibootmgr "Efibootmgr"). The kernel can be configured with an [EFI stub](https://wiki.gentoo.org/wiki/EFI_stub_kernel "EFI stub kernel") which allows it to be directly booted by the firmware. Therefore UEFI has effectively rendered separate boot loaders obsolete, at least for most use cases.

Bootloaders only have a couple of advantages left over the firmware bootloader:

-   consistency - UEFI implementations can vary strongly in functionality and standards compliance
-   recovery solutions

While [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB") provides the grub command line for recovering from a misconfigured system, with minimal effort it is possible to provide the same level of functionality using UEFI components. The goal of this guide is to provide a standardized UEFI based recovery solution.

## Contents

-   [[1] [EFI Shell]](#EFI_Shell)
    -   [[1.1] [Obtaining/installing the UEFI shell]](#Obtaining.2Finstalling_the_UEFI_shell)
    -   [[1.2] [Obtaining filesystem drivers]](#Obtaining_filesystem_drivers)
-   [[2] [Loading the modules]](#Loading_the_modules)
    -   [[2.1] [Testing under Qemu]](#Testing_under_Qemu)
-   [[3] [Summary]](#Summary)
-   [[4] [References]](#References)

## [EFI Shell]

A part of the UEFI specification is a sub-specification for a shell. This shell is based on DOS and Unix shells and its purpose is to allow manual running of EFI applications and interacting with the firmware. Basic usage instructions for the UEFI shell can be found in ^[\[1\]](#cite_note-intel-uefi-shell-1)^. For more details it is best to dive directly into the specification ^[\[2\]](#cite_note-uefi-shell-spec-2)^.

There are two problems with this shell:

-   it is not provided with all distributed firmware
-   it has limited file system support

Only FAT filesystem support is mandatory for UEFI firmware. Some vendors (like Apple, for obvious reasons) implement drivers for other filesystems. If the shell is to be useful for recovery purposes both points need to be addressed.

### [][Obtaining/installing the UEFI shell]

In the case of firmware with the shell built-in, it should be accessible by choosing it from the boot menu which can usually be accessed by pressing `F12` during boot.

The [Tianocore EDKII](http://www.tianocore.org/edk2/) project provides a toolkit for building EFI applications. It provides the source code for an UEFI Shell executable and until 2020 also provided a binary version^[\[3\]](#cite_note-3)^. The binary can still be retrieved from the last release that included it [here](https://github.com/tianocore/edk2/releases/download/edk2-stable202002/ShellBinPkg.zip).

To install the shell simply place it in your ESP partition. The existence of an [fstab](https://wiki.gentoo.org/wiki/Fstab "Fstab") entry for this partition at the standard [/boot/efi] location will be assumed.

`root `[`#`]`wget `[`https://github.com/tianocore/edk2/releases/download/edk2-stable202002/ShellBinPkg.zip`](https://github.com/tianocore/edk2/releases/download/edk2-stable202002/ShellBinPkg.zip)` -O ~/ShellBinPkg.zip `

`root `[`#`]`mount /boot/efi `

`root `[`#`]`cd /boot/efi `

`root `[`#`]`mkdir -p efi/boot/ `

`root `[`#`]`cd efi/boot `

`root `[`#`]`unzip -jp ~/ShellBinPkg.zip ShellBinPkg/UefiShell/X64/Shell.efi > bootx64.efi `

The shell executable has been saved in the default boot location for UEFI firmware. In the absence of a better boot entry, the default behaviour is to boot a hard drive by finding the first ESP and executing [\\EFI\\BOOT\\BOOTX64.EFI] (`\` path separators and lack of case sensitivity are both properties of the FAT filesystem).

### [Obtaining filesystem drivers]

Filesystem drivers in the EFI format can be obtained from [http://efi.akeo.ie/](http://efi.akeo.ie/). All that needs to be done with them is to place them somehwere on the ESP partition.

`root `[`#`]`cd /boot/efi `

`root `[`#`]`mkdir -p efi/shell `

`root `[`#`]`cd efi/shell `

`root `[`#`]`wget -nd -np -r -A efi `[`http://efi.akeo.ie/downloads/efifs-0.7/x64/`](http://efi.akeo.ie/downloads/efifs-0.7/x64/)` `

This package contains drivers for all commonly used filesystems, among others:

-   ext4/xfs/btrfs for Linux
-   ufs/zfs for \*BSD
-   HFS+ for OSX

## [Loading the modules]

A startup script can load the filesystem drivers on every start of the UEFI shell. This startup script is shown below.

[FILE] **`startup.nsh`**

    echo -off
    cd efi\shell\drivers
    echo "Loading drivers:"
    for %d in *.efi
            load %d
    endfor

    echo "Reloading filesystems"
    map -r

This script should be located in the root of the ESP partition, which has been mounted at [/boot/efi]

### [Testing under Qemu]

The above configuration should be tested before relying on it. Thankfully this can be done without leaving your system by using [Qemu](https://wiki.gentoo.org/wiki/Qemu "Qemu"). First we need to obtain an UEFI implementation for use with Qemu. This is also provided by Tianocore under the name [OVMF](http://www.tianocore.org/ovmf/).

`user `[`$`]`wget `[`http://sourceforge.net/projects/edk2/files/OVMF/OVMF-X64-r15214.zip`](http://sourceforge.net/projects/edk2/files/OVMF/OVMF-X64-r15214.zip)` `

`user `[`$`]`unzip OVMF-X64-r15241.zip OVMF.fd `

We will allow qemu direct access to the ESP so make let\'s make a packup of it before.

`root `[`#`]`cd /boot `

`root `[`#`]`tar cf efi.tar efi/ `

`root `[`#`]`umount /boot/efi `

Assuming the block device on which the ESP is located is [/dev/sda1] the following qemu invocation will allow us to test our recovery solution:

`user `[`$`]`qemu-system-x86_64 -bios OVMF.fd -hda /dev/sda1 -boot c`

Newer builds of OVMF are available in [this Fedora repository](https://www.kraxel.org/repos/jenkins/edk2/). They need to be unpacked using [[[app-arch/rpm2targz]](https://packages.gentoo.org/packages/app-arch/rpm2targz)[]].

## [Summary]

This guide has prepared a recovery solution for times when the boot configuration of a UEFI based system is wrong. An UEFI Shell application will be launched when the firmware is told to boot from the harddrive and will load drivers for all conceivable filesystems. This allows access to many different filesystems which allows booting other EFI applcations or even to recover data by moving it between filesystems.

## [References]

\<references\> ^[\[1\]](#cite_note-intel-uefi-shell-1)^ ^[\[2\]](#cite_note-uefi-shell-spec-2)^

1.  [[↑ ^[1.0](#cite_ref-intel-uefi-shell_1-0)^ ^[1.1](#cite_ref-intel-uefi-shell_1-1)^] [Intel\'s articles on the [UEFI shell](https://software.intel.com/en-us/articles/uefi-shell) and [scripting it](https://software.intel.com/en-us/articles/efi-shells-and-scripting/)]]
2.  [[↑ ^[2.0](#cite_ref-uefi-shell-spec_2-0)^ ^[2.1](#cite_ref-uefi-shell-spec_2-1)^] [The [UEFI shell specification](http://www.uefi.org/sites/default/files/resources/UEFI_Shell_Spec_2_0.pdf) v2.0]]
3.  [[[↑](#cite_ref-3)] [[https://edk2.groups.io/g/devel/topic/patch_shellbinpkg_remove/31209298](https://edk2.groups.io/g/devel/topic/patch_shellbinpkg_remove/31209298)]]