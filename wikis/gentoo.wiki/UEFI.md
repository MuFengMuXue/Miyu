**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/UEFI "wikipedia:UEFI")

**UEFI**, short for **Unified Extensible Firmware Interface**, is a firmware standard for boot ROM designed to provide a stable API for interacting with system hardware. On [x86](https://en.wikipedia.org/wiki/x86 "wikipedia:x86") it replaced the legacy [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS").

It was developed by Intel as *Extensible Firmware Interface*, short **EFI**, for the Itanium architecture (\"[IA-64](https://wiki.gentoo.org/wiki/Project:IA64 "Project:IA64")\" or *Intel Architecture 64-bit*). Like [Open Firmware](https://wiki.gentoo.org/wiki/Open_Firmware "Open Firmware") it is designed to be an architecture independent platform available to different CPU instruction sets. It was ported to 32-bit x86 \"[IA-32](https://wiki.gentoo.org/wiki/Project:X86 "Project:X86")\" (also i386 and x86-32), 64-bit x86 \"[x86-64](https://wiki.gentoo.org/wiki/Project:AMD64 "Project:AMD64")\" (also x64, AMD64 and Intel 64), [ARM](https://wiki.gentoo.org/wiki/Project:ARM "Project:ARM"), [RISC-V](https://wiki.gentoo.org/wiki/Project:RISC-V "Project:RISC-V"), and [LoongArch](https://wiki.gentoo.org/wiki/Project:LoongArch "Project:LoongArch").

Any boot ROM that conforms to the UEFI specification is a UEFI ROM. There are multiple implementations, including the open source TianoCore EDK II which serves as the UEFI reference implementation. It is sometimes also called UEFI-BIOS, which is due to it being the BIOS successor on x86, even when it is not BIOS compatible (i.e. in native EFI mode, and after \~2020 missing the BIOS compatibility mode \"CSM\" entirely).

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [Kernel configuration]](#Kernel_configuration)
-   [[3] [Alternatives]](#Alternatives)
-   [[4] [See Also]](#See_Also)
-   [[5] [External resources]](#External_resources)
-   [[6] [References]](#References)

## [Introduction]

The UEFI architecture defines a system initialization process which differs from the classic BIOS one. The main difference happens after a successful self-check and device initialization---on internal drives UEFI then selects one of its stored boot entries (see [[efibootmgr]](https://wiki.gentoo.org/wiki/Efibootmgr "Efibootmgr")), determines the location of the corresponding EFI application (EFI [bootloaders](https://wiki.gentoo.org/wiki/Category:Bootloaders "Category:Bootloaders") or [EFI stubs](https://wiki.gentoo.org/wiki/EFI_stub "EFI stub")) on the [EFI System Partition](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition") (ESP) and launches it. This process is very different to the BIOS approach, which simply reads the first 512-byte sector, like the [Master Boot Record](https://wiki.gentoo.org/wiki/Master_Boot_Record "Master Boot Record") (MBR), of the first in the list of available devices (Boot Drive) and runs it. Instead, (U)EFI has to load the bootloader from the ESP, making the GPT partitioning scheme as well as the [FAT](https://wiki.gentoo.org/wiki/FAT "FAT") file system of the ESP part of the firmware specification. The EFI application\'s binary formats have to correspond with the architecture from which is being booted. On [removable media](https://wiki.gentoo.org/wiki/Removable_media "Removable media") bootloaders for various platforms may be included, see [removable media boot path](https://wiki.gentoo.org/wiki/EFI_System_Partition#Removable_media "EFI System Partition") on the ESP.

UEFI also brings support for features like:

-   [Secure Boot](https://wiki.gentoo.org/wiki/Secure_Boot "Secure Boot")
-   large disk partitions using the mandatory [GUID Partition Table](https://wiki.gentoo.org/wiki/GUID_Partition_Table "GUID Partition Table") (GPT)
-   rich pre-OS boot environment

## [Kernel configuration]

In order to support native (U)EFI, the kernel needs to be configured with EFI support.

[KERNEL] **Enable basic (U)EFI boot support**

    Processor type and features  --->
       [*] EFI runtime service support Search for <code>CONFIG_EFI</code> to find this item.
       [ ]   EFI stub support Search for <code>CONFIG_EFI_STUB</code> to find this item.
       [ ]     EFI mixed-mode support Search for <code>CONFIG_EFI_MIXED</code> to find this item.

\
The [EFI stub](https://wiki.gentoo.org/wiki/EFI_stub "EFI stub") support is required to boot the kernel directly as an EFI executable, as is the EFI mixed-mode support in case a 64-bit kernel is to be booted directly from a 32-bit EFI implementation.

In order to provide access to the EFI functions from a booted system, additional kernel features must be enabled.

[KERNEL] **(U)EFI kernel features**

    File systems  --->
       Pseudo filesystems  --->
           <M/*> EFI Variable filesystem Search for <code>CONFIG_EFIVAR_FS</code> to find this item.
    Device Drivers  --->
       Firmware Drivers  --->
           EFI (Extensible Firmware Interface) Support  --->
               <M/*> Register efivars backend for pstore Search for <code>CONFIG_EFI_VARS_PSTORE</code> to find this item.
                 [*]   Disable using efivars as a pstore backend by default Search for <code>CONFIG_EFI_VARS_PSTORE_DEFAULT_DISABLE</code> to find this item.
               <*> Export efi runtime maps to sysfs Search for <code>CONFIG_EFI_RUNTIME_MAP</code> to find this item.
               [*] Reserve EFI Specific Purpose Memory Search for <code>CONFIG_EFI_SOFT_RESERVE</code> to find this item.

\

** Note**\
`CONFIG_EFI_VARS` was removed in 2023.^[\[1\]](#cite_note-1)^

Especially `efivarfs` must be loaded in order for [efibootmgr] to work. See [efibootmgr](https://wiki.gentoo.org/wiki/Efibootmgr "Efibootmgr") for further details.

** Tip**\
All (U)EFI functions can be disabled with the kernel parameter `efi=noruntime`, or activated with `efi=runtime`. A kernel booted without EFI runtime functions will not be able to alter any EFI settings and variables, including the boot configuration.

## [Alternatives]

The open source hardware initializer ROM [Coreboot](https://wiki.gentoo.org/wiki/Coreboot "Coreboot") can deploy UEFI, BIOS, and Open Firmware boot ROMs among others.

## [See Also]

-   [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS") --- the standard firmware of IBM-PC-compatible computers until it was phased out in 2020.
-   [Coreboot](https://wiki.gentoo.org/wiki/Coreboot "Coreboot") --- a free and opensource hardware initializing firmware which supports multiple boot ROM payloads.
-   [Open Firmware](https://wiki.gentoo.org/wiki/Open_Firmware "Open Firmware") --- an [IEEE 1275-1994](https://ieeexplore.ieee.org/document/763383) standard for hardware independent firmware built on top of a [Forth](https://wiki.gentoo.org/wiki/Forth "Forth") machine.

## [External resources]

-   [UEFI Specifications](https://uefi.org/specifications)
-   [Unified Extensible Firmware Interface Forum](https://uefi.org/)
-   [coreboot](https://www.coreboot.org/) --- open source firmware that can deploy [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS") and [UEFI] (among others) as second stage payloads.
-   [GLaBIOS](https://glabios.org/) --- A modern, scratch-built, open-source ROM [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS") for PC, XT, 8088 PCs.
-   [CSMWrap](https://github.com/CSMWrap/CSMWrap) --- an FOSS EFI application designed to restore BIOS compatibility to UEFI systems that drop support for it.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://lore.kernel.org/lkml/20230117124310.16594-3-johan+linaro@kernel.org/T/](https://lore.kernel.org/lkml/20230117124310.16594-3-johan+linaro@kernel.org/T/)]]