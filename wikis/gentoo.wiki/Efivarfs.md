This page contains [[changes](https://wiki.gentoo.org/index.php?title=Efivarfs&oldid=1278647&diff=1307047)] which are not marked for translation.

[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Efivarfs&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Efivarfs/hu "Efivarfs (100% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Efivarfs/ja "efivarfs (100% translated)")

**Resources**

[[]][Home](https://docs.kernel.org/6.1/filesystems/efivarfs.html)

The [efivarfs] is a filesystem in the Linux [kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") that enables users to create, delete, and modify [(U)EFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") variables. [efivarfs] is typically (and automatically) mounted to [/sys/firmware/efi/efivars]; if it needs to be mounted manually the following command can be used:

`root `[`#`]`mount -t efivarfs none /sys/firmware/efi/efivars`

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [Kernel]](#Kernel)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [EFI-CSM: BIOS mode]](#EFI-CSM:_BIOS_mode)
    -   [[3.2] [EFI runtime unavailable]](#EFI_runtime_unavailable)
-   [[4] [See also]](#See_also)
-   [[5] [References]](#References)

### [Introduction]

[efivarfs] was created to address the shortcomings of using entries in [sysfs](https://wiki.gentoo.org/wiki/Sysfs "Sysfs") to maintain EFI variables: the old sysfs EFI variables code only supported variables of up to 1024 bytes. This was originally a limitation in version 0.99 of the EFI specification which was was removed before any full releases^[\[1\]](#cite_note-Kernel_Docs-1)^.

** Note**\
Due to the presence of numerous firmware bugs where removing non-standard UEFI variables causes the system firmware to fail to POST, [efivarfs] files that are not well-known standardized variables are created as immutable files. This doesn't prevent removal---`chattr -i` will work---but it does prevent this from happening accidentally.

** Tip**\
When the content of an UEFI variable in [/sys/firmware/efi/efivars] is viewed, pay attention to the first 4 bytes of the output - they represent the UEFI variable attributes, in little-endian format. As a practical matter, each [efivar] is in the following format: `4_bytes_of_attributes + efivar_data`.

### [[] Kernel]

`CONFIG_EFIVAR_FS` support needs to be enabled:

[KERNEL] **Enable EFI Variable filesystem support**

    Device Drivers  --->
      Firmware Drivers  --->
        EFI (Extensible Firmware Interface) Support --->
          [ ] Disable EFI runtime services support by default Search for <code>CONFIG_EFI_DISABLE_RUNTIME</code> to find this item.
    File systems  --->
      Pseudo filesystems  --->
        <*> EFI Variable filesystem Search for <code>CONFIG_EFIVAR_FS</code> to find this item.

## [Troubleshooting]

### [EFI-CSM: BIOS mode]

On [x86](https://en.wikipedia.org/wiki/x86 "wikipedia:x86") UEFI replaced the legacy [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS"), to enable backwards compatibility during the transitional period, UEFI on x86 included a BIOS emulation, called *Compatibility Support Module (CSM)*. When [EFI-CSM] is activated and in use, it will behave like a legacy BIOS, including hiding UEFI facilities from the operating system.

** Tip**\
If this filesystem does not exist on UEFI-capable hardware it probably means that the hardware was booted in *Legacy (BIOS) Mode* i.e. EFI-CSM.

In most cases is a safe assumption that a computer or laptop manufactured after 2020 is a pure UEFI system that cannot be in BIOS mode; as an additional point of interest when Secure Boot is enabled EFI-CSM is automatically deactivated.

### [EFI runtime unavailable]

All (U)EFI functions can be disabled with the kernel parameter `efi=noruntime`, or activated with `efi=runtime`. A kernel booted without EFI runtime functions will not be able to alter any EFI settings and variables, including the boot configuration.

## [See also]

-   [Efibootmgr](https://wiki.gentoo.org/wiki/Efibootmgr "Efibootmgr") --- a tool for managing [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") boot entries.

## [References]

1.  [[[↑](#cite_ref-Kernel_Docs_1-0)] [[https://docs.kernel.org/6.1/filesystems/efivarfs.html](https://docs.kernel.org/6.1/filesystems/efivarfs.html)]]