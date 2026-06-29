**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/BIOS "wikipedia:BIOS")

[[]][[alt.comp.bios](news:alt.comp.bios) ([weblink](https://www.novabbs.com/devel/thread.php?group=alt.comp.bios))]

The **BIOS** (**B**asic **I**nput/**O**utput **S**ystem) was the standard firmware of IBM-PC-compatible computers until it was phased out in 2020. On a cold start, the BIOS performs [system initialization](https://wiki.gentoo.org/wiki/System_Initialization_of_Intel_x86_with_BIOS_Firmware "System Initialization of Intel x86 with BIOS Firmware"), then loads the boot sector of the boot device specified in [CMOS](https://wiki.gentoo.org/wiki/CMOS_BIOS_Memory "CMOS BIOS Memory") memory, and hands off execution to it. In most cases this boot sector is a [Master Boot Record](https://wiki.gentoo.org/wiki/Master_Boot_Record "Master Boot Record").

When it was originally released in 1981, the ROM BIOS was an entirely proprietary IBM product. Eventually, companies [reverse engineered](https://en.wikipedia.org/wiki/reverse_engineer "wikipedia:reverse engineer") and documented the inner workings of the BIOS leading to a *de facto* standard. At first, this compatibility was incomplete but it grew and evolved over time until essentially 100% software compatibility existed between BIOS vendors.

Early BIOSes were implemented in ROM. This meant that upgrading the BIOS required physically replacing the ROM chip. This is contrast to later BIOS implementations, starting in the 1990ies, and modern [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") implementations (on PCs the BIOS successor) where the firmware code is stored in EPROM, EEPROM or flash memory (usually NOR flash). This change from read-only memory to erasable and reprogrammable memory has security implications: while BIOS updates can address security issues (as well as bug fixes, with or without security implications), now malicious code can theoretically^[\[1\]](#cite_note-1)^---and proven practically^[\[2\]](#cite_note-2)^---also attach itself to the firmware flash storage. This type of malware is called Rootkit. It is very hard to remove, because it will always be active when the system is turned on, putting it in the position to both evade detection and removal. To remove malicious BIOS code, the specific chip has to be reprogrammed directly, requiring external access to the memory chip on the main circuit board.

## Contents

-   [[1] [Configuration]](#Configuration)
    -   [[1.1] [Set boot drive and order]](#Set_boot_drive_and_order)
-   [[2] [BIOS Memory Map]](#BIOS_Memory_Map)
-   [[3] [BIOS as a UEFI Application for Backwards Compatibility]](#BIOS_as_a_UEFI_Application_for_Backwards_Compatibility)
    -   [[3.1] [BIOS and coreboot]](#BIOS_and_coreboot)
-   [[4] [Boot Sector]](#Boot_Sector)
-   [[5] [See Also]](#See_Also)
-   [[6] [External Resources]](#External_Resources)
-   [[7] [References]](#References)

## [Configuration]

In order to configure the system, users need to enter the BIOS setup program by pressing a specific key at startup, usually within 2 seconds of hearing the start-up beep. This key press is not initially standardized and required users to check documentation in order to gain access to the system\'s firmware settings. By the mid 1990\'s a *de facto* standard began to emerge around a few possible keyboard combinations, with [F2] being the most common.

-   [Esc] used by [Coreboot](https://wiki.gentoo.org/wiki/Coreboot "Coreboot").
-   [Del]
-   [F1]
-   [F2] used by [Phoenix](https://en.wikipedia.org/wiki/Phoenix_Technologies "wikipedia:Phoenix Technologies") BIOS.

By the late 1980\'s some BIOS manufacturers printed a notice on cold start indicating what button combination to press in order to enter the firmware configuration screen. Unfortunately, this practice was not uniform and early systems could have quite obscure keyboard input combintation requirements. This often lead to system administrators performing cold boots and simply guessing as to the correct keyboard input combination until their attempts were sucessful or all known combinations had been tried.

In the setup program\'s menu, users can configure several features:

-   Enable or disable built-in hardware devices.
-   Configure hardware features.
-   Set date and time.
-   Select boot drives and set a preference order.
-   Specify a boot password.

To operate the setup program with a USB keyboard, users may have to enable a function called **USB Legacy**, or something similar.

### [Set boot drive and order]

Users can use the BIOS setup menu to change the boot drive and to set a preference order. They should set the drive where they installed the bootloader as their first preference, to speed up boot time. It takes time to check optical and floppy disk drives for a valid boot loader, so if those are placed first, the system will not boot as quickly as it might.

For [USB](https://wiki.gentoo.org/wiki/USB "USB") boot drives users must enable a function called **USB Legacy**, or something similar.

Newer BIOS versions let users press a key during boot to open a menu, where they can select the boot drive. This is handy, if they want to boot from a LiveCD. Possible keys are:

-   [F11]
-   [F12]

Users can find the right key in their motherboard or computer manual, but it may also be shown at boot time, right after after power on. To show the boot option menu, users must press the right key about two seconds after power on, even if there is no screen displayed.

## [BIOS Memory Map]

Once the BIOS has been initialized, RAM below 1MiB looks like this:

  -------------- -------------- ---------- -------------------------------------------------
  Start          Stop           Size       Description
  `0x00000000`   `0x000003ff`   1KiB       Interrupt Vector Table (IVT) in Protected Mode.
  `0x00000400`   `0x000004ff`   256B       BIOS Data Area (BDA).
  `0x00000500`   `0x00007bff`   29.75KiB   Conventional memory available to programs.
  `0x00007c00`   `0x00007dff`   512B       Reserved for Boot Sector.
  `0x00007e00`   `0x0007ffff`   480.5KiB   Conventional memory available to programs.
  `0x00080000`   `0x0009ffff`   128KiB     Extended BIOS Data Area (EBDA).
  `0x000a0000`   `0x000bffff`   128KiB     Video memory.
  `0x000c0000`   `0x000c7fff`   32KiB      Video card BIOS.
  `0x000c8000`   `0x000effff`   160KiB     BIOS Extensions.
  `0x000f0000`   `0x000fffff`   64KiB      Motherboard BIOS
  -------------- -------------- ---------- -------------------------------------------------

## [BIOS as a UEFI Application for Backwards Compatibility]

When a EFI or UEFI system is set to BIOS compatibility mode, then an EFI application called *Compatibility Support Module* (CSM) is loaded. The CSM operates as a shim that intercepts BIOS system calls and translates them into their UEFI equivalents, effectively acting as a BIOS emulation.

Booting from a Master Boot Record (MBR) partition means that the firmware must give the system a BIOS-like environment as a starting point, so that BIOS bootsectors and BIOS bootloaders continue to work. When an EFI/UEFI system (with Secure Boot disabled) is booted with an MBR partitioned media, the firmware will automatically load the CSM. It is not available when Secure Boot is enabled, which is the standard setting on computers with Microsoft Windows 10 and newer.

In UEFI after 2020 the Compatibility Support Module was discontinued, and with it all BIOS compatibility. In native (U)EFI mode, the firmware will directly load a compatible EFI bootloader from the *EFI System Partition* (ESP), which requires a [GUID Partition Table](https://wiki.gentoo.org/wiki/GPT "GPT") (GPT). In response to the eventual removal of BIOS compatibility, [CSMWrap](https://github.com/CSMWrap/CSMWrap) was created as a EFI application to restore this functionality to systems that ship without it.

### [BIOS and coreboot]

[Coreboot](https://wiki.gentoo.org/wiki/Coreboot "Coreboot") provides just enough firmware to initialize a system from a cold start and pass execution to a designated payload. While coreboot itself provides any of several payloads, a [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") payload is perhaps the most common. Several coreboot distributions reject UEFI and prefer a [SeaBIOS](https://www.seabios.org) payload by default, but offer alternatives such as booting directly to GRUB or a Linux kernel. From the perspective these coreboot forks, such as [Libreboot](https://libreboot.org/), there is a simple reason for preferring a BIOS payload: it provides a *much* smaller attack surface relative to a UEFI implementation.

## [Boot Sector]

It is a common misunderstanding that a BIOS will analyze the partition layout of the Master Boot Record and boot the active partition, although there are BIOS implementations that will check for an active partition and refuse to boot, if in fact no partition is set active.^[\[3\]](#cite_note-3)^ Some BIOSes also support special service partitions, and will boot a very specific system from it when the function is requested. Examples include the BIOS Setup for certain Compaq models^[\[4\]](#cite_note-4)^ (which is unavailable if that specific partition is missing), or the Hidden Protected Area (HPA) of ThinkPads (sometimes also called Predesktop Area or Rescue and Recovery).

Normally, a system firmware fully compatible with the original IBM PC\'s ROM BIOS will not do any of that. Instead it will simply verify if the signature of the boot sector, the last two bytes at offset `0x01FE` (or `510` decimal), are `0xAA55`, load the sector into memory and execute it in 16 bit x86 Real Mode. If the BIOS is unable to find a valid boot sector on any drive, that is in the list of bootable devices, it will display a simple text message, such as `NO BOOTABLE DEVICE`.

** Note**\
Error messages are unique to each software. Different BIOS versions will display different messages, such as e.g. `Operating System Not Found`,^[\[5\]](#cite_note-5)^ an error message very similar to the one generated by the standard [Master Boot Record](https://wiki.gentoo.org/wiki/Master_Boot_Record "Master Boot Record") (MBR): `Missing operating system`.^[\[6\]](#cite_note-6)^ Other BIOS versions and bootloaders add to this pool of different error messages and variants, often leading to confusion to exactly which part of the boot process actually has failed at that point: the BIOS, the MBR, the partition bootloader (VBR) or any other subsequent booloader in the chain.

## [See Also]

-   [BIOS Update](https://wiki.gentoo.org/wiki/BIOS_Update "BIOS Update") --- describes how to apply a BIOS update on a Gentoo system.
-   [CMOS BIOS Memory](https://wiki.gentoo.org/wiki/CMOS_BIOS_Memory "CMOS BIOS Memory") --- a few *bytes* of battery-backed SRAM used to preserve [BIOS] settings and Real Time Clock data when a PC is off.
-   [Coreboot](https://wiki.gentoo.org/wiki/Coreboot "Coreboot") --- a free and opensource hardware initializing firmware which supports multiple boot ROM payloads.
-   [dmidecode](https://wiki.gentoo.org/wiki/Dmidecode "Dmidecode") --- a software tool that enables extraction of detailed hardware information from a system by decoding the DMI (Desktop Management Interface) table
-   [Master Boot Record](https://wiki.gentoo.org/wiki/Master_Boot_Record "Master Boot Record") --- the *de facto* standard boot sector of an IBM PC compatible with [BIOS] as its system firmware.
-   [Open Firmware](https://wiki.gentoo.org/wiki/Open_Firmware "Open Firmware") --- an [IEEE 1275-1994](https://ieeexplore.ieee.org/document/763383) standard for hardware independent firmware built on top of a [Forth](https://wiki.gentoo.org/wiki/Forth "Forth") machine.
-   [System Initialization of Intel x86 with BIOS Firmware](https://wiki.gentoo.org/wiki/System_Initialization_of_Intel_x86_with_BIOS_Firmware "System Initialization of Intel x86 with BIOS Firmware") --- the process of bringing an Intel x86 system up from a cold start.
-   [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") --- a firmware standard for boot ROM designed to provide a stable API for interacting with system hardware. On [x86](https://en.wikipedia.org/wiki/x86 "wikipedia:x86") it replaced the legacy [BIOS].

## [External Resources]

-   [How to enter BIOS on old computers](https://medium.com/@andrew.perfiliev/how-to-enter-bios-on-old-computers-a838486e1701)
-   [coreboot](https://www.coreboot.org/) --- open source firmware that can deploy [BIOS] and [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") (among others) as second stage payloads.
-   [GLaBIOS](https://glabios.org/) --- A modern, scratch-built, open-source ROM [BIOS] for PC, XT, 8088 PCs.
-   [CSMWrap](https://github.com/CSMWrap/CSMWrap) --- an FOSS EFI application designed to restore BIOS compatibility to UEFI systems that drop support for it.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://www.blackhat.com/presentations/bh-europe-06/bh-eu-06-Heasman.pdf](https://www.blackhat.com/presentations/bh-europe-06/bh-eu-06-Heasman.pdf)]]
2.  [[[↑](#cite_ref-2)] [[https://www.theregister.com/2011/09/14/bios_rootkit_discovered/](https://www.theregister.com/2011/09/14/bios_rootkit_discovered/)]]
3.  [[[↑](#cite_ref-3)] [[https://www.rodsbooks.com/gdisk/bios.html](https://www.rodsbooks.com/gdisk/bios.html)]]
4.  [[[↑](#cite_ref-4)] [[https://www.seriss.com/people/erco/compaq-deskpro-2000/](https://www.seriss.com/people/erco/compaq-deskpro-2000/)]]
5.  [[[↑](#cite_ref-5)] [[https://support.us.vaio.com/knowledge-base/vaio_pc-it-shows-operating-system-not-found-and-cannot-startup-windows/](https://support.us.vaio.com/knowledge-base/vaio_pc-it-shows-operating-system-not-found-and-cannot-startup-windows/)]]
6.  [[[↑](#cite_ref-6)] [[https://thestarman.pcministry.com/asm/mbr/STDMBR.htm](https://thestarman.pcministry.com/asm/mbr/STDMBR.htm)]]