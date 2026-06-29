**CMOS BIOS Memory** is a few *bytes* of battery-backed SRAM used to preserve [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS") settings and Real Time Clock data when a PC is off. It is the historical antecedent to [UEFI NVRAM](https://wiki.gentoo.org/index.php?title=UEFI_NVRAM&action=edit&redlink=1 "UEFI NVRAM (page does not exist)"), which serves the same purpose on UEFI systems but typically uses flash memory instead of SRAM.

CMOS BIOS memory contains 128-bytes of battery-backed SRAM as standard. The on ISA systems, the layout looks like this:

  -------- -------- ---------- -------------------------------------------------------------------
  Start    Stop     Bytes      Description
  `0x00`   `0x0f`   16 bytes   Real Time Clock
  `0x10`   `0x2f`   32 bytes   ISA configuration data
  `0x30`   `0x3f`   16 bytes   BIOS specific configuration data
  `0x40`   `0x7f`   64 bytes   Extended System Configuration Data (ESCD) with Plug and Play data
  -------- -------- ---------- -------------------------------------------------------------------

  : CMOS BIOS Memory Layout

Past the RTC data exact byte details differ somewhat by implementation. QEMU\'s SeaBIOS is commonly used as a reference for the creation of modern BIOS implementations.

## [CMOS Battery]

On reasonably modern systems the BIOS battery is nearly always a CR2032 lithium coin cell. Older boards may have nickel-cadmium (Ni--Cd) batteries which can leak as they age and damage or destroy their host systems.

## [Troubleshooting]

### [Date and time are lost when the system is unplugged]

The CMOS BIOS battery is past its useful life. Discard the battery and replace it with a new one.

## [See Also]

-   [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS") --- the standard firmware of IBM-PC-compatible computers until it was phased out in 2020.
-   [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") --- a firmware standard for boot ROM designed to provide a stable API for interacting with system hardware. On [x86](https://en.wikipedia.org/wiki/x86 "wikipedia:x86") it replaced the legacy [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS").

## [External Resourcse]

-   [SeaBIOS CMOS Memory Map](https://github.com/coreboot/seabios/blob/master/src/hw/rtc.h)
-   [BIOS Central CMOS Memory Map](https://www.bioscentral.com/misc/cmosmap.htm)
-   [GLaBIOS](https://glabios.org/) a modern, scratch-built, open-source ROM [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS") for PC, XT, 8088 PCs.