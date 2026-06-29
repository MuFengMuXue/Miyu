**System initialization on the x86 platform** is the process of bringing an Intel x86 system up from a cold start. Even on a legacy [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS") environment the process is complex and to the uninitiated can seem convoluted.

## Contents

-   [[1] [Cold Start]](#Cold_Start)
-   [[2] [Boot Strap Stage]](#Boot_Strap_Stage)
-   [[3] [Power-On Self Test (POST)]](#Power-On_Self_Test_.28POST.29)
-   [[4] [The Master Boot Record (MBR)]](#The_Master_Boot_Record_.28MBR.29)
-   [[5] [See Also]](#See_Also)
-   [[6] [External Resources]](#External_Resources)

## [Cold Start]

On system power up, the Processor Control Register sets the Protection Enable bit flag to 0. This means that the CPU is in Real Mode and all memory locations addressed by the CPU correspond to their actual physical locations in the system\'s memory map. This mode is a precondition for allowing the CPU to address ROM code as though it is RAM. This is in contrast to protected mode addressing which gives every process its own virtual memory space, a precondition for memory mapped swap space. If the concept of addressing modes are alien to you, see the [Assembly Language](https://wiki.gentoo.org/wiki/Assembly_Language "Assembly Language") article. On system startup, the Code Segment (CS) register is set to `0xffff` and the Instruction Pointer (IP) register is set to `0x0000`. This can be represented as `0xffff:0000` or `0xffff0`.

The very first instruction that any CPU executes is the code stored at the CPU\'s reset vector. This code is almost invariably ROM code that has been mapped into a memory address location. This memory address may fall outside of what the system physically has installed and may occur even before system RAM has been initialized and made available to the CPU. On system startup of the original 8086, the Code Segment (CS) register is set to `0xffff` and the Instruction Pointer (IP) register is set to `0x0000`. This can be represented as `0xffff:0000` or `0xffff0`; they are different ways of representing the same value. At this point, the system can only address the top `0xffff0000` -- `0xffffffff` of memory which, again, is likely ROM mapped to a memory address and not actual RAM.

For the sake of completeness: historically, in the era before ROM-based startup routines were the norm, system operators would manually enter the startup sequence via a series of toggle switches to bring the system up. Once operational, the system would hand over execution to a mass storage device; those days often punched paper tape or an 80 column punch card reader.

On the x86 architecture, the reset vector is very near the bottom of the memory map. Thus, actual location moves around based upon the width of the system\'s Instruction Pointer:

  ------------------------------------------------------------------------------------------ --------------- ---------------------- ---------------------------------
  CPU                                                                                        Address Width   Reset Vector Address   Comment
  [Intel 8080](https://en.wikipedia.org/wiki/Intel_8080 "wikipedia:Intel 8080")      16 bits         `0xfff0`               The first 16 bytes below 64KiB.
  [Intel 8086](https://en.wikipedia.org/wiki/Intel_8086 "wikipedia:Intel 8086")      20 bits         `0xffff0`              The first 16 bytes below 1MiB.
  [Intel 80286](https://en.wikipedia.org/wiki/Intel_80286 "wikipedia:Intel 80286")   24 bits         `0xfffff0`             The first 16 bytes below 16MiB.
  [Intel 80386](https://en.wikipedia.org/wiki/Intel_80386 "wikipedia:Intel 80386")   32 bits         `0xfffffff0`           The first 16 bytes below 4GiB.
  ------------------------------------------------------------------------------------------ --------------- ---------------------- ---------------------------------

Perhaps confusingly, x86_64 processors do NOT have a 64-bit reset vector at `0xfffffffffffffff0`. This is because 64-bit addressing does not support real mode. Thus these systems use the same reset vector as the 80386 at system start.

## [Boot Strap Stage]

The first word of the reset vector must be a valid x86 instruction. It is not a pointer value as is the case with some other architectures.

A typical example performs a quick jump to a convenient nearby memory location, switches to Protected Mode as quickly as possible, and then performs a far jump to the start of the BIOS and begins execution. The first task a BIOS typically performs is a Power-On Self Test (POST).

\
The BIOS must map to a non-contiguous memory area of 384KiB. It was possible but extremely tedious to partially side-step this restriction to a *very limited extent* using techniques such as [memory overlay](https://en.wikipedia.org/wiki/Overlay_(programming) "wikipedia:Overlay (programming)") --- essentially the software equivalent of [bank switching](https://en.wikipedia.org/wiki/Bank_switching "wikipedia:Bank switching") --- but this made development more difficult.

For the sake of completeness: the original IBM PC contained an 8KiB BIOS and a 8KiB [BASIC](https://wiki.gentoo.org/wiki/BASIC "BASIC") interpreter, IBM Cassette BASIC, available on startup; the BASIC interpreter was its own OS. Later systems grew to 16KiB of ROM space to enable support for hard disks. Though BASIC remained a popular language for some time, the build in BASIC ROM was quickly abandoned in favor of interpreters that could be loaded from disk.

## [][Power-On Self Test (POST)]

The Power-On Self Test performs the following checks:

-   Verifies the CPU registers are functional.
-   Verifies the integrity of the BIOS code, typically with a simple checksum.
-   Initialize RAM, prior to this step the CPU may only have its registers and CPU cache available.
-   Verifies interrupts and DMA are working as expected.
-   Initialize the chipset.
-   Initialize the system bus.
-   Fetches the contents of [CMOS](https://wiki.gentoo.org/index.php?title=CMOS&action=edit&redlink=1 "CMOS (page does not exist)") (a small amount of battery backed RAM) restoring the system configuration.

If anything goes wrong most BIOSes are configured to provide a beep code. Some also flash an LED for the sake of the hearing impaired. BIOS beep codes usually involve a series of short and long beeps, but are manufacture specific. As such, they are inscrutable without the manufacture\'s documentation.

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

## [][The Master Boot Record (MBR)]

If a default boot device is correctly configured and accessible to the system a single disk sector --- called the [Master Boot Record](https://wiki.gentoo.org/wiki/Master_Boot_Record "Master Boot Record") (MBR) --- is read into `0x00007c00`. Once done, a `jmp` instruction is executed pointing to that memory location. The first byte must be a valid x86 instruction. In most cases, the initial payload must fit within the first 446-bytes of the 512-byte disk sector. The total available code can exceed 446-bytes only to the extent that clever use of compression techniques permit. Classically, the remaining 66-bytes are a data structure that defines Master Boot Record or MBR-style partition tables. In practice, modern MBR tables are even more pressed for space.

## [See Also]

-   [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS") --- the standard firmware of IBM-PC-compatible computers until it was phased out in 2020.
-   [CMOS](https://wiki.gentoo.org/index.php?title=CMOS&action=edit&redlink=1 "CMOS (page does not exist)")
-   [Coreboot](https://wiki.gentoo.org/wiki/Coreboot "Coreboot") --- a free and opensource hardware initializing firmware which supports multiple boot ROM payloads.
-   [Master Boot Record](https://wiki.gentoo.org/wiki/Master_Boot_Record "Master Boot Record") --- the *de facto* standard boot sector of an IBM PC compatible with [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS") as its system firmware.
-   [Partition Table](https://wiki.gentoo.org/index.php?title=Partition_Table&action=edit&redlink=1 "Partition Table (page does not exist)")
-   [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") --- a firmware standard for boot ROM designed to provide a stable API for interacting with system hardware. On [x86](https://en.wikipedia.org/wiki/x86 "wikipedia:x86") it replaced the legacy [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS").

## [External Resources]

-   [Wikibooks: x86 Assembly Language](https://en.wikibooks.org/wiki/X86_Assembly).