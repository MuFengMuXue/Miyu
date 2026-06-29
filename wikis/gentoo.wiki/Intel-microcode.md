This page contains [[changes](https://wiki.gentoo.org/index.php?title=Intel_microcode&oldid=1305909&diff=1339487)] which are not marked for translation.

Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Intel_microcode/hu "Intel mikrokód (100% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Intel_microcode/zh-cn "Intel微码 (20% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Intel_microcode/ja "Intel マイクロコード (100% translated)")

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Microcode "wikipedia:Microcode")

[[]][Package information](https://packages.gentoo.org/packages/sys-firmware/intel-microcode)

This article describes the process of updating the [microcode](https://wiki.gentoo.org/wiki/Microcode "Microcode") on Intel processors.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Genkernel]](#Genkernel)
    -   [[2.2] [Syslinux]](#Syslinux)
    -   [[2.3] [GRUB Legacy]](#GRUB_Legacy)
    -   [[2.4] [GRUB]](#GRUB)
    -   [[2.5] [rEFInd]](#rEFInd)
    -   [[2.6] [systemd-boot]](#systemd-boot)
    -   [[2.7] [Xen (EFI)]](#Xen_.28EFI.29)
-   [[3] [New method without initram-fs/disk (efistub compatible)]](#New_method_without_initram-fs.2Fdisk_.28efistub_compatible.29)
    -   [[3.1] [Software]](#Software)
    -   [[3.2] [Kernel]](#Kernel_2)
-   [[4] [Verification]](#Verification)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)
-   [[7] [References]](#References)

## [[] Installation]

### [[] Kernel]

The following kernel support is required to be built-in:

[KERNEL] **Enable CONFIG_BLK_DEV_INITRD, CONFIG_MICROCODE, and CONFIG_MICROCODE_INTEL**

    General setup  --->
        [*] Initial RAM filesystem and RAM disk (initramfs/initrd) support
    Processor type and features  --->
        <*> CPU microcode loading support
        [*]   Intel microcode loading support

** Warning**\
Modules do not work for early microcode, so make sure microcode loading is built-in.

** Important**\
Since kernel version 6.6, the **microcode** loading support is **enabled by default**, and the above configuration no longer exists:`CONFIG_MICROCODE_INTEL` was replaced with `CONFIG_CPU_SUP_INTEL`. ^[\[1\]](#cite_note-1)^

### [USE flags]

### [USE flags for] [sys-firmware/intel-microcode](https://packages.gentoo.org/packages/sys-firmware/intel-microcode) [[]] [Intel IA32/IA64 microcode update data]

  --------------------------------------------------------------------- -------------------------------------------------------------------------------
  [`+initramfs`](https://packages.gentoo.org/useflags/+initramfs)       Install a small initramfs for use with CONFIG_MICROCODE_EARLY
  [`+split-ucode`](https://packages.gentoo.org/useflags/+split-ucode)   Install the split binary ucode files (used by the kernel directly)
  [`dist-kernel`](https://packages.gentoo.org/useflags/dist-kernel)     Delegate microcode initramfs generation to sys-kernel/installkernel
  [`hostonly`](https://packages.gentoo.org/useflags/hostonly)           Only install ucode(s) supported by currently available (=online) processor(s)
  [`vanilla`](https://packages.gentoo.org/useflags/vanilla)             Only install microcode updates from Intel\'s official microcode tarball
  --------------------------------------------------------------------- -------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-20 17:02] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [[] Emerge]

Install the microcode firmware package and the manipulation tool:

`root `[`#`]`emerge --ask --noreplace sys-firmware/intel-microcode`

## [[] Configuration]

** Note**\
If the `initramfs` USE flag is active the `intel-microcode` ebuild will ensure that a cpio archive of all microcode is either directly installed into [/boot/intel-uc.img], or it will instruct [installkernel](https://wiki.gentoo.org/wiki/Installkernel "Installkernel") to generate one when the kernel is installed.

To manually generate the microcode [cpio](https://wiki.gentoo.org/wiki/Cpio "Cpio") archive use [iucode_tool]:

`root `[`#`]`iucode_tool -S --write-earlyfw=/boot/early_ucode.cpio /lib/firmware/intel-ucode/*`

    iucode_tool: system has processor(s) with signature 0x000306c3
    iucode_tool: Writing selected microcodes to: /boot/early_ucode.cpio

### [[] Genkernel]

If [genkernel] is used to generate the initrd then add the [\--microcode-initramfs] option to have it prepend an early cpio with the Intel and AMD microcode inside. No modifications to the bootloader config are necessary below.

### [[] Syslinux]

Multiple initrd files are separated by commas in the `INITRD` line. Set [early_ucode.cpio] to load first:

[FILE] **`/boot/syslinux.cfg`**

    LABEL gentoo
        MENU LABEL Gentoo Linux 4.4.6
        LINUX /vmlinuz-4.4.6-gentoo
        INITRD /early_ucode.cpio,/initrd-4.4.6-gentoo.img

### [[] GRUB Legacy]

Add the generated microcode to the kernel command-line as the first `initrd`. The root initramfs goes second separated by space. This step is necessary even if the system does not use an initrd image in order to boot. The microcode update merely leverages the initrd hooks:

[FILE] **`/boot/grub/grub.conf`Example GRUB Legacy configuration for microcode update**

    title Gentoo Linux 4.4.6
    root (hd0,0)
    kernel /boot/vmlinuz-4.4.6-gentoo root=/dev/sda3
    initrd /boot/intel-uc.img /boot/initrd.img

### [[] GRUB]

Starting with version 2.02-r1, GRUB supports loading an early microcode. If the microcode file is named after one of the following: [intel-uc.img], [intel-ucode.img], [amd-uc.img], [amd-ucode.img], [early_ucode.cpio], or [microcode.cpio], it will be automatically detected when running [grub-mkconfig]. To declare a microcode file named differently, e.g. [ucode.cpio], add this line to [/etc/default/grub]:

[FILE] **`/etc/default/grub`**

    GRUB_EARLY_INITRD_LINUX_CUSTOM="ucode.cpio"

Regenerate the [grub.cfg] with:

`root `[`#`]`grub-mkconfig -o /boot/grub/grub.cfg`

    Generating grub configuration file ...
    Found linux image: /boot/vmlinuz-4.6.3-gentoo
    Found initrd image: /boot/early_ucode.cpio /initramfs-genkernel-x86_64-4.6.3-gentoo
    done

Or, for earlier versions than 2.02-r1, edit [grub.cfg] directly to add the [early_ucode.cpio] as the first initrd:

[FILE] **`/boot/grub/grub.cfg`**

    menuentry 'Gentoo Linux 4.14'

Finally, reboot.

### [[] rEFInd]

[FILE] **`/efi/EFI/refind/refind.conf`**

    menuentry Linux
    }

This example system has the EFI partition [/dev/sda1] mounted to [/efi]. The Linux kernel and initrd files have been placed in [/boot] on the Linux rootfs.

If using the **initrd** keyword instead of the **options** keyword for specifying initrd, then try specifying multiple initrd files via separate **initrd** keywords, or migrate the declarations into **options**. Specifying multiple initrd via one **initrd** keyword fails on rEFInd. As always, make sure [boot/early_code.cpio] is the first initrd specified.

Review and edit the kernel `cmdline` options from the rEFInd bootloader. With the Gentoo OS entry highlighted, press [F2] to access the menu entries, and press [F2] again over the desired entry to review and edit. This is very useful for quick experimenting without need to edit [refind.conf].

[FILE] **`/boot/refind_linux.conf`**

    "Boot using default options"     "root=PARTUUID=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX rw initrd=boot\intel-ucode.img initrd=boot\amd-ucode.img initrd=boot\initramfs-%v.img"

Finalize the configuration in [/boot/refind_linux.conf]. Keep in mind that rEFInd searches initramfs relatively partition, so if the /boot partition is separate, search it with \"initrd=intel-ucode.img initrd=initramfs-%v.img\" (because boot partition don\'t have /boot folder). Use backslashes \\, or the kernel may not find the files. See [refind.conf] for keyword descriptions and [The rEFInd Homepage](https://www.rodsbooks.com/refind/) for more on how to use rEFInd.

### [[] systemd-boot]

Add the microcode as an argument to an **initrd** line. If an initrd line already exists, ensure the microcode entry occurs first. The path to the microcode should be absolute to the root of the ESP.

[FILE] **`/boot/EFI/loader/entries/example`**

    title      Gentoo/Linux
    version    4.13.13
    options    root=/dev/sda1
    linux      /4.13.13/linux
    initrd     /4.13.13/intel_ucode
    initrd     /4.13.13/initrd

For more information, see [The Boot Loader Specification](https://www.freedesktop.org/wiki/Specifications/BootLoaderSpec/).

### [][[] Xen (EFI)]

Add a line to the [xen.cfg] with the `ucode` option. The path to the microcode is relative to the [xen.efi] binary. Ensure to write the microcode into the correct location (default is [/boot/EFI/Gentoo]) or copy it there.

[FILE] **`/boot/EFI/Gentoo/xen.cfg`**

    [global]
    default=gentoo

    [gentoo]
    kernel=vmlinuz-4.4.6-gentoo root=/dev/sda1
    ramdisk=initrd-4.4.6-gentoo.img
    ucode=early_ucode.cpio

For more information, see the [Xen EFI](https://xenbits.xen.org/docs/unstable/misc/efi.html) documentation.

## [][[] New method without initram-fs/disk (efistub compatible)]

** Warning**\
This will only work on a 64-bit kernel and will have no effect otherwise. 32-bit systems need to use an initramfs.

** Note**\
This method should be preferable, especially for EFI-Stub systems (some motherboard firmware might have issues with parsing/passing custom boot command line options), since these changes are less likely to leave the system unbootable (and possibly unrepairable without an EFI compatible rescue disk which can be very tricky on headless machines) the way a broken firmware boot entry and/or incorrect initram-fs/disk would, while it also works on BIOS systems or EFI systems with custom bootloaders on disk.

### [[] Software]

The [[[sys-firmware/intel-microcode]](https://packages.gentoo.org/packages/sys-firmware/intel-microcode)[]]-20171117-r1 package has been rewritten to use [iucode_tool] to process microcode data files. Users can now use the `MICROCODE_SIGNATURES` variable to install only a subset of microcode data files.

To install microcode data files for the system processor(s):

[FILE] **`/etc/portage/make.conf`**

    MICROCODE_SIGNATURES="-S"

To install microcode data files for a specific processor use `MICROCODE_SIGNATURES="-s 0x000306c3"`, or `MICROCODE_SIGNATURES="-s !0x000306c3"` to exclude a specific processor. An empty or undefined `MICROCODE_SIGNATURES` variable will install all microcode data files.

Install the microcode data files:

`root `[`#`]`emerge --ask sys-firmware/intel-microcode`

The [[[sys-firmware/intel-microcode]](https://packages.gentoo.org/packages/sys-firmware/intel-microcode)[]]-20171117-r1 installs [iucode_tool] which can be used to identify the processor signature(s).

`user `[`$`]`iucode_tool -S`

    iucode_tool: system has processor(s) with signature 0x000306c3

To find the appropriate filename(s) for the listed signature(s) use:

`user `[`$`]`iucode_tool -S -l /lib/firmware/intel-ucode/*`

    iucode_tool: system has processor(s) with signature 0x000306c3
    [...]
    microcode bundle 49: /lib/firmware/intel-ucode/06-3c-03
    [...]
    selected microcodes:
      049/001: sig 0x000306c3, pf_mask 0x32, 2017-01-27, rev 0x0022, size 22528

The signature is found in microcode bundle `49`, so the filename to use is [/lib/firmware/intel-ucode/06-3c-03].

** See also**\
See the [intel ucode for Core i7-8650U](https://forums.gentoo.org/viewtopic-p-8798002.html#8798002) forums post for an easier way to get the necessary microcode file.

### [[] Kernel]

Enable and configure the `CONFIG_MICROCODE`, `CONFIG_MICROCODE_INTEL`, `CONFIG_FIRMWARE_IN_KERNEL`, `CONFIG_EXTRA_FIRMWARE` and `CONFIG_EXTRA_FIRMWARE_DIR` kernel options.

** Warning**\
Every option *must* be set as built into the kernel, not as a kernel module.

[KERNEL] **Enabling Microcode Loading Support**

    Processor type and features  --->
        <*> CPU microcode loading support
        [*]   Intel microcode loading support

    Device Drivers  --->
      Generic Driver Options  --->
        Firmware Loader  --->
          -*-   Firmware loading facility
          (intel-ucode/06-3c-03) Build named firmware blobs into the kernel binary
          (/lib/firmware) Firmware blobs root directory

** Note**\
The `CONFIG_EXTRA_FIRMWARE` and `CONFIG_EXTRA_FIRMWARE_DIR` options need to be set to the values identified by [iucode_tool]. In this example for an Intel i7-4790K processor, `CONFIG_EXTRA_FIRMWARE` is set to `intel-ucode/06-3c-03` and `CONFIG_EXTRA_FIRMWARE_DIR` is set to `/lib/firmware`.

** Note**\
The `CONFIG_EXTRA_FIRMWARE` option allows specifying multiple firmware files by listing them space-separated.

[Rebuild and install](https://wiki.gentoo.org/wiki/Kernel/Rebuild "Kernel/Rebuild") the kernel as usual.

## [[] Verification]

After the next reboot, the loaded microcode revision can be verified by running:

`user `[`$`]`grep microcode /proc/cpuinfo`

    microcode  : 0x22
    microcode   : 0x22

The [dmesg] output should include:

`root `[`#`]`dmesg | grep microcode`

    [    0.000000] microcode: microcode updated early to revision 0x22, date = 2017-01-27
    [    1.153262] microcode: sig=0x306c3, pf=0x2, revision=0x22
    [    1.153815] microcode: Microcode Update Driver: v2.2.

Here is an example of a CPU with no available microcode updates (microcode already current) or the system was not configured to load them properly:

`root `[`#`]`dmesg | grep microcode`

    [    1.196567] microcode: CPU0 sig=0x6fd, pf=0x80, revision=0xa3
    [    1.196575] microcode: CPU1 sig=0x6fd, pf=0x80, revision=0xa3
    [    1.196623] microcode: Microcode Update Driver: v2.01 <tigran@aivazian.fsnet.co.uk>, Peter Oruba

Here is the same CPU but with microcode updates being applied successfully:

`root `[`#`]`dmesg | grep microcode`

    [    0.000000] microcode: microcode updated early to revision 0xa4, date = 2010-10-02
    [    1.207385] microcode: CPU0 sig=0x6fd, pf=0x80, revision=0xa4
    [    1.207393] microcode: CPU1 sig=0x6fd, pf=0x80, revision=0xa4
    [    1.207445] microcode: Microcode Update Driver: v2.01 <tigran@aivazian.fsnet.co.uk>, Peter Oruba

** Note**\
If genkernel and legacy GRUB are used, the first line may be absent. Instead, check the microcode revision before and after the changes.

** Note**\
Note how this is the very first step of the kernel logs now.

** Important**\
It is possible the microcode has already been fully updated by your [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS") vendor. In that case the [dmesg] output does not contain the update log message.

** Note**\
Be aware that injecting the microcode update directly into the motherboard firmware (which might sound tempting) might result in CPU0 being updated but the rest of the CPUs (or CPU cores in a multi-core system) being left at their initial revision (which might cause more problems than running them all at the same initial version). And, since most stock motherboard firmware has some microcode updates (even in their initial release versions), it\'s probably a good enough reason for everybody to make sure their kernel tries to update all CPUs (and cores) to the same version (so, let this update driver running even if the kernel has the same version which is stored in the motherboard firmware). Injecting the microcode into the firmware might be desirable still (to make sure it\'s loaded for the boot CPU before the kernel is loaded and able to update the rest of the microcode).

## [[] See also]

-   [Microcode](https://wiki.gentoo.org/wiki/Microcode "Microcode") --- describes various ways to update a CPU\'s microcode in Gentoo.
-   [AMD microcode](https://wiki.gentoo.org/wiki/AMD_microcode "AMD microcode") --- describes updating the [microcode](https://wiki.gentoo.org/wiki/Microcode "Microcode") for [AMD](https://wiki.gentoo.org/wiki/AMD "AMD") processors.

## [[] External resources]

-   [http://www.win-raid.com/t154f16-Tool-Guide-News-quot-UEFI-BIOS-Updater-quot-UBU.html](http://www.win-raid.com/t154f16-Tool-Guide-News-quot-UEFI-BIOS-Updater-quot-UBU.html) - An example unofficial source for microcodes
-

** Important**\
The microcode-ctl utility has been deprecated as of version 1.28-r1 (Gentoo unstable)^[\[2\]](#cite_note-2)^ and was [removed from the Gentoo repository](https://gitweb.gentoo.org/repo/gentoo.git/commit/sys-apps/microcode-ctl?id=6915ad825559f329b8d2989ab232932906a8cbf4).

## [[] References]

1.  [[[↑](#cite_ref-1)] [[https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=e6bcfdd75d53390a67f67237f4eafc77d9772056](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=e6bcfdd75d53390a67f67237f4eafc77d9772056)]]
2.  [[[↑](#cite_ref-2)] [[https://gitweb.gentoo.org/repo/gentoo.git/commit/?id=719cc5ef240b766953ddbe1e7a6593f8091eed12](https://gitweb.gentoo.org/repo/gentoo.git/commit/?id=719cc5ef240b766953ddbe1e7a6593f8091eed12) The microcode-ctl utility has been deprecated as of version 1.28-r1 (Gentoo unstable) and no longer contains the init script. It also does not work on certain CPUs such as Intel Haswells.]]