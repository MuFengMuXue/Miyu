**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Microcode "wikipedia:Microcode")

**Article status**

[[]]This article has some todo items:\

-   Mention that recommended way to load microcode is using sys-firmware/intel-microcode\[initramfs\] or sys-kernel/linux-firmware\[initramfs\]

CPU **microcode** is a form of [firmware](https://en.wikipedia.org/wiki/Firmware "wikipedia:Firmware") that controls the processor\'s internals. This document describes various ways to update a CPU\'s microcode in Gentoo.

In modern [x86](https://en.wikipedia.org/wiki/X86 "wikipedia:X86") processors, the microcode often handles execution of complex and highly specialized instructions. Parts of the microcode also act as firmware for the processor\'s embedded controllers, and it is even used to fix or to mitigate **processor design/implementation errata/bugs**. Given the complexity of modern processors, a CPU may have over a hundred such errata^[\[1\]](#cite_note-1)^.

## Contents

-   [[1] [Microcode updates]](#Microcode_updates)
-   [[2] [Microcode firmware blobs]](#Microcode_firmware_blobs)
-   [[3] [Kernel configuration]](#Kernel_configuration)
-   [[4] [Dracut]](#Dracut)
-   [[5] [The manual way]](#The_manual_way)
    -   [[5.1] [Manual initramfs creation (AMD)]](#Manual_initramfs_creation_.28AMD.29)
    -   [[5.2] [Early microcode loading]](#Early_microcode_loading)
    -   [[5.3] [Late microcode loading]](#Late_microcode_loading)
-   [[6] [Specifics]](#Specifics)
    -   [[6.1] [AMD specifics]](#AMD_specifics)
    -   [[6.2] [Intel specifics]](#Intel_specifics)
-   [[7] [See also]](#See_also)
-   [[8] [External resources]](#External_resources)
-   [[9] [References]](#References)

## [Microcode updates]

** Important**\
For security and stability reasons it is highly recommended to load updated microcode as soon as possible. Aside from keeping the system firmware up-to-date, when the kernel is used to load updated microcode of the CPU this should be done as early as possible in the boot process.

Recent processors have the ability to patch their microcode via *microcode updates*. Active microcode updates are stored in volatile memory and thus have to be *applied during each system boot*.

The system firmware can perform a microcode update early in the boot process. This kind of microcode update is provided by the system manufacturer in the firmware, on x86 by the [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS") or [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI"). Since the system firmware can be upgraded like most firmware via a [BIOS update](https://wiki.gentoo.org/wiki/BIOS_Update "BIOS Update"), the shipped microcode version depends on the motherboard and/or system firmware vendor.

** Note**\
The most prominent and widely used system has historically been the x86-based IBM PC compatible computer and its BIOS, which is why system firmware is sometimes called a BIOS even when it is not an IBM PC compatible BIOS, such as the AlphaBIOS or the OpenBIOS. EFI/UEFI, the successor of the PC BIOS, is also often called \"(U)EFI-BIOS\". Hence, the term \"[BIOS update](https://wiki.gentoo.org/wiki/BIOS_Update "BIOS Update")\" often refers to a system firmware update that is not really a PC BIOS.

Only on x86, the [kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") itself can also perform a microcode update^[\[2\]](#cite_note-2)^ from [firmware binary blobs](https://wiki.gentoo.org/wiki/Linux_firmware "Linux firmware") during boot. Common use cases are e.g. when the vendor of a system (or mainboard) does not supply firmware updates (BIOS updates, which include microcode updates) in a timely manner, when it is preferred to stay on an older version of the system firmware (BIOS, UEFI) for some reason, or when a system is out of warranty and does not receive further updates for the BIOS or its successor UEFI. In any case, the kernel microcode update facility allows patching the CPU\'s microcode, provided microcode firmware files are made available for the specific CPU by its manufacturer, Intel or AMD. When out of warranty (i.e. too old), Intel and AMD may also stop providing microcode updates for the specific CPU, resulting in newly discovered bugs no longer being fixed and security issues not fully mitigated.

** Note**\
Severity of processor errata patched by microcode updates varies. The issues concerned range from extremely rare system instabilities, to data corruption, or severe hardware vulnerabilities.^[\[3\]](#cite_note-3)^

Because [Gentoo is about customization](https://wiki.gentoo.org/wiki/Complete_Handbook/Making_a_choice "Complete Handbook/Making a choice") there is *a choice* of ways to update a CPU\'s microcode. Please choose the workflow which best suits the affected system.

** Note**\
If using a dist-kernel, dracut will handle this automatically so long as the necessary firmware files are installed in /lib/firmware.

## [Microcode firmware blobs]

It may be necessary to tell [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") to [accept the relevant license](https://wiki.gentoo.org/wiki//etc/portage/package.license "/etc/portage/package.license") before emerging:

`root `[`#`]`echo "sys-kernel/linux-firmware @BINARY-REDISTRIBUTABLE" >> /etc/portage/package.license`

Install [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] (which includes, among others, AMD x86 microcode) and/or [[[sys-firmware/intel-microcode]](https://packages.gentoo.org/packages/sys-firmware/intel-microcode)[]] (for Intel x86 microcode):

`root `[`#`]`emerge --ask sys-kernel/linux-firmware sys-firmware/intel-microcode`

## [Kernel configuration]

** Note**\
Refer to [Intel microcode](https://wiki.gentoo.org/wiki/Intel_microcode "Intel microcode") for x86 CPUs from Intel and/or [AMD microcode](https://wiki.gentoo.org/wiki/AMD_microcode "AMD microcode") for x86 CPUs from AMD.

If initrd is to be used, enable it:

[KERNEL] **Enable initramfs/initrd support (CONFIG_BLK_DEV_INITRD)**

    General setup  --->
        [*] Initial RAM filesystem and RAM disk (initramfs/initrd) support

** Important**\
Since kernel version 6.6, **microcode** loading is **enabled by default**. `CONFIG_MICROCODE_AMD` and `CONFIG_MICROCODE_INTEL` no longer exist. They were replaced with `CONFIG_CPU_SUP_AMD` and `CONFIG_CPU_SUP_INTEL`. ^[\[4\]](#cite_note-4)^ ^[\[5\]](#cite_note-5)^

The only way to load microcode is through the kernel. While at least one CPU make must be enabled, it does not hurt to choose both AMD and Intel:

[KERNEL] **Configuring a kernel to support microcode loading**

    Processor type and features --->
       [*] CPU microcode loading support
       [*]   Intel microcode loading support
       [*]   AMD microcode loading support

## [Dracut]

[[dracut]](https://wiki.gentoo.org/wiki/Dracut "Dracut") is an [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") infrastructure which can be used to load microcode at boot. [dracut] embeds installed microcode to generated initramfs images.

Since version 047, [dracut] has the `early_microcode` option enabled by default. Therefore on systems using [dracut] the microcode should get loaded automatically.

However, it is still possible to specify the microcode embedding by a configuration file:

[FILE] **`/etc/dracut.conf.d/microcode.conf`Explicit microcode loading enablement**

    early_microcode="yes"

Or by using the dedicated parameter:

`root `[`#`]`dracut --early-microcode`

** Tip**\
For further details about [dracut] usage see the dedicated [Dracut article](https://wiki.gentoo.org/wiki/Dracut "Dracut").

## [The manual way]

### [][Manual initramfs creation (AMD)]

Using this method the microcode is built-in to (an additional) [initrd](https://en.wikipedia.org/wiki/Initial_ramdisk "wikipedia:Initial ramdisk"). This way the microcode is kept separate from both the kernel and the main initramfs/initrd, and therefore can be updated without recompiling either.

In any case the system will require a reboot to apply updated microcode files.

Create the specified directory and [cd] into it. It might be a different dir than [/tmp]. The [kernel/x86/microcode] part is important.

`user `[`$`]`mkdir -p /tmp/amd-ucode/kernel/x86/microcode `

`user `[`$`]`cd /tmp/amd-ucode `

Concatenate the AMD firmware files into a single file. The path and filename of the output file must not be altered.

`user `[`$`]`cat /lib/firmware/amd-ucode/microcode_amd*.bin > kernel/x86/microcode/AuthenticAMD.bin`

Create a [cpio](https://wiki.gentoo.org/wiki/Cpio "Cpio") archive in [/boot/amd-uc.img] using [bsdcpio] from [[[app-arch/libarchive]](https://packages.gentoo.org/packages/app-arch/libarchive)[]]:

`root `[`#`]`echo kernel/x86/microcode/AuthenticAMD.bin | bsdcpio -o -H newc -R 0:0 > /boot/amd-uc.img`

The initrd/initramfs kernel option must be enabled (`BLK_DEV_INITRD=y`). Genkernel may be used to automatically copy relevant microcode into the initrd. This also requires the `initramfs` USE flag for the relevant [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] or [[[sys-firmware/intel-microcode]](https://packages.gentoo.org/packages/sys-firmware/intel-microcode)[]] package.

### [Early microcode loading]

For early microcode leading, microcode is provided as the first initramfs (aka initrd, in cpio format) to the kernel during boot. Grub (both legacy and grub2) permits specifying multiple cpio images separated by space in the initrd command.

GRUB2 supports loading an early microcode. If the microcode file is named after one of the following: [intel-uc.img], [intel-ucode.img], [amd-uc.img], [amd-ucode.img], [early_ucode.cpio], or [microcode.cpio], it will be automatically detected when running [grub-mkconfig]. To declare a microcode file named differently, e.g. ucode.cpio, add this line to [/etc/default/grub]:

[FILE] **`/etc/default/grub`**

    GRUB_EARLY_INITRD_LINUX_CUSTOM="ucode.cpio"

Regenerate the [grub.cfg] with:

`root `[`#`]`grub-mkconfig -o /boot/grub/grub.cfg`

    Generating grub configuration file ...
    Found linux image: /boot/vmlinuz-4.6.3-gentoo
    Found initrd image: /boot/early_ucode.cpio /initramfs-genkernel-x86_64-4.6.3-gentoo
    done

The output above is similar to what should be seen, minus the initramfs if one is not used by the system, when microcode is loaded through GRUB.

### [Late microcode loading]

To manually instruct the kernel to reload microcodes, run:

`root `[`#`]`echo 1 > /sys/devices/system/cpu/microcode/reload`

Be sure to watch [dmesg] for any errors. This loading mechanism looks for microcode blobs in the [/lib/firmware/ location.

** Note**\
The previous command must be run after every reboot or firmware package update to keep microcode updated!

With kernel **version 6.1** a late microcode loading is not possible anymore because it is now disabled by default. If needed it must be enabled in the kernel configuration. Of course it is not recommended.

[KERNEL] **Kernels 6.1+**

    Processor type and features  --->
        [ ]   Late microcode loading (DANGEROUS)

## [Specifics]

\<Please help!\>

### [AMD specifics]

AMD microcodes are bundled in the [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] package. A more lengthy guide is found in the [AMD microcode](https://wiki.gentoo.org/wiki/AMD_microcode "AMD microcode") article.

### [Intel specifics]

Intel microcodes are bundled in the [[[sys-firmware/intel-microcode]](https://packages.gentoo.org/packages/sys-firmware/intel-microcode)[]] package. Detailed instructions can be found in the [Intel microcode](https://wiki.gentoo.org/wiki/Intel_microcode "Intel microcode") article.

## [See also]

-   [Linux firmware](https://wiki.gentoo.org/wiki/Linux_firmware "Linux firmware") --- is a package distributed alongside the Linux kernel that contains firmware [binary blobs](https://en.wikipedia.org/wiki/binary_blob "wikipedia:binary blob") necessary for partial or full functionality of certain hardware devices.
-   [AMD microcode](https://wiki.gentoo.org/wiki/AMD_microcode "AMD microcode") --- describes updating the [microcode] for [AMD](https://wiki.gentoo.org/wiki/AMD "AMD") processors.
-   [Intel microcode](https://wiki.gentoo.org/wiki/Intel_microcode "Intel microcode") --- describes the process of updating the [microcode] on Intel processors.

## [External resources]

-   [Reverse Engineering x86 Processor Microcode](https://www.usenix.org/system/files/conference/usenixsecurity17/sec17-koppe.pdf) Paper describing microcode in common x86 processors.

## [References]

1.  [[[↑](#cite_ref-1)] [[6th Generation Intel® Processor Family](https://web.archive.org/web/20190803114003/https://www.intel.com/content/dam/www/public/us/en/documents/specification-updates/desktop-6th-gen-core-family-spec-update.pdf#page=27), Intel. Retrieved on October 24, 2018]]
2.  [[[↑](#cite_ref-2)] [Fenghua Yu, Borislav Petkov, [The Linux Microcode Loader](https://www.kernel.org/doc/Documentation/x86/microcode.txt), kernel.org. Retrieved on October 24, 2018]]
3.  [[[↑](#cite_ref-3)] [[Microcode Revision Guidance](https://web.archive.org/web/20220816223205/https://newsroom.intel.com/wp-content/uploads/sites/11/2018/04/microcode-update-guidance.pdf), Intel. Retrieved on October 24, 2018]]
4.  [[[↑](#cite_ref-4)] [[https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=e6bcfdd75d53390a67f67237f4eafc77d9772056](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=e6bcfdd75d53390a67f67237f4eafc77d9772056)]]
5.  [[[↑](#cite_ref-5)] [[https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=4d2b748305e96fb76202a0d1072a285b1500bff3](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=4d2b748305e96fb76202a0d1072a285b1500bff3)]]