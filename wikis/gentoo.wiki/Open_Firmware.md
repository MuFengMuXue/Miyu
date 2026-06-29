[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Open_Firmware&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

*Not to be confused with [System76\'s UEFI-based product, also called Open Firmware](https://wiki.gentoo.org/wiki/UEFI "UEFI").*

**Resources**

[[]][Home](https://www.openfirmware.info)

[[]][Official documentation](https://www.openfirmware.info/IEEE_1275-1994)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Open_Firmware "wikipedia:Open Firmware")

**Open Firmware** is an [IEEE 1275-1994](https://ieeexplore.ieee.org/document/763383) standard for hardware independent firmware built on top of a [Forth](https://wiki.gentoo.org/wiki/Forth "Forth") machine. Open Firmware was initially used on early SPARCstations under the name **OpenBoot** but was later popularized by [PowerPC](https://wiki.gentoo.org/wiki/PowerPC "PowerPC") Macs. Despite the demise of that platform in favor of the x86 and ARM-based Macs, Open Firmware sees continued use with the [OpenBIOS](https://github.com/openbios/openbios) project as an optional firmware payload. Open Firmware was designed to be modular and noticeably easier to port to new architectures compared to other options such as legacy [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS") or [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") firmware.

Of note, Open Firmware was the system firmware of choice for the ill-fated [OLPC XO-1 laptop](https://wiki.gentoo.org/wiki/OLPC_XO-1_laptop "OLPC XO-1 laptop") project. This might have proved Open Firmware\'s swan song were it not for the efforts of the OpenBIOS community which continues the firmware\'s development. Largely as a result of their efforts, Open Firmware remains a reasonably common payload for the system initializer [Coreboot](https://wiki.gentoo.org/wiki/Coreboot "Coreboot"), allowing anyone to deploy OpenBIOS implementation of Open Firmware on coreboot supported hardware. Today it is most commonly encountered \"in the wild\" on *very* high security workstations and servers. It is also relatively popular as a payload for the [Raspberry Pi](https://wiki.gentoo.org/wiki/Raspberry_Pi "Raspberry Pi") Pico RP2040.

## Contents

-   [[1] [Accessing Open Firmware]](#Accessing_Open_Firmware)
    -   [[1.1] [Using the Forth Interpreter]](#Using_the_Forth_Interpreter)
-   [[2] [See Also]](#See_Also)
-   [[3] [External Resources]](#External_Resources)
    -   [[3.1] [Open Firmware Distributions]](#Open_Firmware_Distributions)

## [Accessing Open Firmware]

-   On a New World Mac at boot time, Open Firmware\'s Forth prompt can be accessed [Option]+[Command]+[O]+[F].
-   On a SPARC system with OpenBoot (Open Firmware) at boot time, the Forth prompt can be accessed via [Stop]+[a].
-   On an OLPC at boot time, when the chime sounds hit [Esc] but do not hold it down.
-   Alternatively, on a running OLPC system type [echo y \> /proc/sysrq-trigger].

### [Using the Forth Interpreter]

The Forth interpreter prompt should closely resemble:

    ok
    0 >

Most recent Open Firmware implementations implement a line-editor with [Emacs](https://wiki.gentoo.org/wiki/Emacs "Emacs")-like keybindings. This is an optional feature that the PPC-era Macs popularized and its presence is still common.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------
  **Keyboard Shortcut**                                                                                                                                                                                                                                                                                                                             **Function**
  [Control]+[Space]   Word completion.
  [Control]+[/]       Display all possible completed words.
  [Control]+[A]       Move cursor to start of line.
  [Esc]+[B]           Move the cursor backwards one character.
  [Control]+[D]       Delete the character at the current cursor position.
  [Esc]+[D]           Delete all characters from the current cursor position to the end of the current word.
  [Control]+[E]       Go to end of line.
  [Control]+[F]       Advance the cursor one character.
  [Esc]+[F]           Advance the cursor one word.
  [Control]+[H]       Delete the previous character.
  [Esc]+[H]           Delete all characters before the current cursor position out to the beginning of the word.
  [Control]+[K]       Delete the contents of the current line.
  [Control]+[L]       Display command-line history.
  [Control]+[N]       Advance the cursor to the next line.
  [Control]+[P]       Move the cursor back one line.
  [Control]+[U]       Delete the entire line.
  [Control]+[Y]       Insert the contents of the copy/paste buffer into the current line.
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------

## [See Also]

-   [Coreboot](https://wiki.gentoo.org/wiki/Coreboot "Coreboot") --- a free and opensource hardware initializing firmware which supports multiple boot ROM payloads.
-   [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS") --- the standard firmware of IBM-PC-compatible computers until it was phased out in 2020.
-   [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") --- a firmware standard for boot ROM designed to provide a stable API for interacting with system hardware. On [x86](https://en.wikipedia.org/wiki/x86 "wikipedia:x86") it replaced the legacy [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS").
-   [Forth](https://wiki.gentoo.org/wiki/Forth "Forth") --- a heavily stack-oriented self-compiling procedural programming language that is only slightly more abstract than [assembly](https://wiki.gentoo.org/wiki/Assembly_language "Assembly language").

## [External Resources]

-   [OpenBIOS](https://openfirmware.info/) a wiki dedicated to Open Firmware-based projects.
-   [Building Open Firmware for QEMU](https://www.openfirmware.info/Building_OFW_for_QEMU).
-   [Building Open Firmware as a x86 BIOS Payload](https://www.openbios.org/Building_OFW_to_Load_from_BIOS).
-   [Building Open Firmware as a Coreboot Payload](https://www.openbios.org/OFW_as_a_Coreboot_Payload).
-   [Building Open Firmware for ARM](https://www.openbios.org/Building_OFW_for_ARM).

### [Open Firmware Distributions]

-   [C Forth](https://github.com/MitchBradley/cforth) a modernized fork of the [OLPC](https://wiki.gentoo.org/wiki/OLPC_XO-1_laptop "OLPC XO-1 laptop") firmware and Forth interpreter.
-   [OpenBIOS](https://github.com/openbios/openbios) the first published Open Source IEEE 1275-1994 Open Firmware implementation.
-   [Open Firmware](https://github.com/openbios/openfirmware) as used by the [OLPC](https://wiki.gentoo.org/wiki/OLPC_XO-1_laptop "OLPC XO-1 laptop") laptop among others.
-   [SmartFirmware](https://github.com/openbios/smartfirmware) Codegen\'s implementation of Open Firmware.
-   [OpenBoot](https://github.com/openbios/openboot) Sun\'s implementation of Open Firmware.
-   [Slimline Open Firmware](https://gitlab.com/slof/slof) (SLOF) for virtualized guests on [IBM POWER](https://wiki.gentoo.org/wiki/PPC64 "PPC64") architecture.