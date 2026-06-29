**Resources**

[[]][Home](https://vice-emu.sourceforge.io/)

[[]][Official documentation](https://vice-emu.sourceforge.io/vice_toc.html)

[[]][Package information](https://packages.gentoo.org/packages/app-emulation/vice)

[[]][Wikipedia](https://en.wikipedia.org/wiki/VICE "wikipedia:VICE")

[[]][Bugs (upstream)](https://sourceforge.net/p/vice-emu/bugs/)

[[]][[comp.emulators.cbm](news:comp.emulators.cbm) ([weblink](https://www.novabbs.com/devel/thread.php?group=comp.emulators.cbm))]

[[]][[#vice-dev](ircs://irc.libera.chat/#vice-dev)] ([[webchat](https://web.libera.chat/#vice-dev)])

**VICE** is the **V**ersat**I**le **C**ommodore **E**mulator for Commodore computers of the 8-bit era that has been in continuous development since 1993. The emulators produced by the VICE team are famously accurate and include nearly every 8-bit Commodore machines ever released, along with an entire ecosystem of vintage hardware devices.

The systems emulated by VICE include:

-   [xpet] PET --- (1977--1982) an early personal computer sold in multiple configurations, widely used in the business and education market prior to the Apple II. The system supported either 40 or 80 column text output and no graphics or sound support.
-   [xvic] VIC 20 --- (1982--1985) personal computer with minimal RAM and a 22-column display targeting the home market with simple graphics and sound. The VIC-20 was mostly a game system with many titles using cartridges to help overcome the system\'s anemic (even by the standards of the era) 5kB of RAM.
-   [x64sc] Commodore 64 --- (1982--1994) the most popular home computer of all time with 64k of RAM, a 40 column display, 16 colors, and the best sound chip of any PC of the era.
-   [x64dtv] C64 Direct-to-TV --- (2004--present) slightly enhanced C64 implemented on an FPGA in a joystick formfactor.
-   [xscpu64] CMD SuperCPU 64 --- (1997--2001) a rare accelerator cartridge for the C64 that appeared very late in the system\'s life. It included a WDC 65816 CPU running at 20MHz and supported up to 16MB of RAM.
-   [x128] Commodore 128 --- (1985--1989) a personal computer with 128kB of RAM, 80 column graphics and text, a C64 compatibility mode, and a CP/M Z80 mode.
-   [xplus4] Plus/4 --- (1984--1985) a personal computer with a built in productivity suite that failed to find a market.

Very few Commodore systems remain unemulated. The most notable gaps are:

-   The Commdore 65 an unreleased Commodore intended to be semi-compatible with the C64 but include enhanced graphics and sound. An enhanced version of this product exists in the open source [MEGA65](https://mega65.org/) which has its own emulator.
-   The Commodore LCD an unreleased laptop intended to compete against the TRS-80 Model 100.
-   CMD SuperCPU 128 an accelerator cartridge for the C64 that appeared very late in the system\'s life. It included a WDC 65816 CPU running at 20MHz and supported up to 16MB of RAM. This product was released but is unclear if any software was ever written specifically for it. This device even more rare than its C64 counterpart.

Emulators can be built with either a GTK interface for conventional GUI support or SDL for a more immersive user experience. Additionally VICE has a number of tools that are useful for developers who write games or other software targeting these systems.

## Contents

-   [[1] [VICE Development Tools]](#VICE_Development_Tools)
    -   [[1.1] [Remote Monitor]](#Remote_Monitor)
    -   [[1.2] [Binary Monitor]](#Binary_Monitor)
    -   [[1.3] [PETCAT]](#PETCAT)
    -   [[1.4] [c1541]](#c1541)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [USE flags]](#USE_flags)
    -   [[2.2] [Emerge]](#Emerge)
    -   [[2.3] [Files]](#Files)
-   [[3] [Usage]](#Usage)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Inability to access CPU history in the monitor]](#Inability_to_access_CPU_history_in_the_monitor)
    -   [[4.2] [How do I convert a BASIC game to ASCII text or vice-versa?]](#How_do_I_convert_a_BASIC_game_to_ASCII_text_or_vice-versa.3F)
    -   [[4.3] [Is it possible to port CBM BASIC to a modern BASIC implementation?]](#Is_it_possible_to_port_CBM_BASIC_to_a_modern_BASIC_implementation.3F)
    -   [[4.4] [How do I configure VICE to use JiffyDOS or other Third Party Kernal?]](#How_do_I_configure_VICE_to_use_JiffyDOS_or_other_Third_Party_Kernal.3F)
    -   [[4.5] [I am a C64 developer/demo coder, how do I make unit testing with VICE\'s monitor faster?]](#I_am_a_C64_developer.2Fdemo_coder.2C_how_do_I_make_unit_testing_with_VICE.27s_monitor_faster.3F)
-   [[5] [Removal]](#Removal)
    -   [[5.1] [Unmerge]](#Unmerge)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

### [VICE Development Tools]

#### [Remote Monitor]

The remote monitor can be run by passing [(emulator) -remotemonitor] at runtime. The monitor then becomes available over tcp/6510 via [telnet] or [netcat]. This allows the user to manually interrogate the state of the emulated machine, view memory, watch execution, mark breakpoints, etc.

#### [Binary Monitor]

Similar functionality to the remote monitor but with some key differences:

-   It is invoked with [(emulator) -binarymonitor] and listens to tcp/6502.
-   All commands are prefixed with byte `0x02`.
-   It\'s designed to be accessed via an external scripting language of the developer\'s choice rather than accessed directly by a human.

#### [PETCAT]

Commodore BASIC like other BASIC implementations of the era use single byte tokens to represent BASIC keywords. For example, the `DATA` command is byte `0x83` and the `PRINT` command is byte `0x99`. This saves RAM in an era when every byte was a precious resource.

The [petcat] command allows for the tokenization and detokenization of BASIC source code. Source code extracted from the emulated system will be converted to an ASCII text file that can be modified by any plain text editor such as [vim](https://wiki.gentoo.org/wiki/Vim "Vim") or [emacs](https://wiki.gentoo.org/wiki/Emacs "Emacs"). PETSCII control codes without ASCII counterparts will be converted into macros in curly braces.

While it is primarily used to handle BASIC files, petcat can also convert PETSCII encoded text documents to plain ASCII and vice-versa.

#### [c1541]

The [c1541] tool allows for most Commodore disk images. New disks images can be created, files can be extracted, or new files added.

## [Installation]

### [USE flags]

### [USE flags for] [app-emulation/vice](https://packages.gentoo.org/packages/app-emulation/vice) [[]] [Versatile Commodore Emulator]

  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+gtk`](https://packages.gentoo.org/useflags/+gtk)               Add support for x11-libs/gtk+ (The GIMP Toolkit)
  [`alsa`](https://packages.gentoo.org/useflags/alsa)               Add support for media-libs/alsa-lib (Advanced Linux Sound Architecture)
  [`curl`](https://packages.gentoo.org/useflags/curl)               Add support for client-side URL transfer library
  [`debug`](https://packages.gentoo.org/useflags/debug)             Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`doc`](https://packages.gentoo.org/useflags/doc)                 Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`ethernet`](https://packages.gentoo.org/useflags/ethernet)       Enable ethernet emulation
  [`flac`](https://packages.gentoo.org/useflags/flac)               Add support for FLAC: Free Lossless Audio Codec
  [`gif`](https://packages.gentoo.org/useflags/gif)                 Add GIF image support
  [`headless`](https://packages.gentoo.org/useflags/headless)       Include the headless variant of the emulator
  [`lame`](https://packages.gentoo.org/useflags/lame)               Add support for MP3 encoding using LAME
  [`mpg123`](https://packages.gentoo.org/useflags/mpg123)           Enable mp3@64 cartridge support
  [`ogg`](https://packages.gentoo.org/useflags/ogg)                 Add support for the Ogg container format (commonly used by Vorbis, Theora and flac)
  [`openmp`](https://packages.gentoo.org/useflags/openmp)           Build support for the OpenMP (support parallel computing), requires \>=sys-devel/gcc-4.2 built with USE=\"openmp\"
  [`oss`](https://packages.gentoo.org/useflags/oss)                 Add support for OSS (Open Sound System)
  [`parport`](https://packages.gentoo.org/useflags/parport)         Enable parallel port SID support
  [`pci`](https://packages.gentoo.org/useflags/pci)                 Enable PCI device discovery using sys-apps/pciutils
  [`png`](https://packages.gentoo.org/useflags/png)                 Add support for libpng (PNG images)
  [`portaudio`](https://packages.gentoo.org/useflags/portaudio)     Add support for the crossplatform portaudio audio API
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)   Add sound server support via media-libs/libpulse (may be PulseAudio or PipeWire)
  [`sdl`](https://packages.gentoo.org/useflags/sdl)                 Add support for Simple Direct Layer (media library)
  [`usb`](https://packages.gentoo.org/useflags/usb)                 Add USB support to applications that have optional USB support (e.g. cups)
  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-20 03:35] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-emulation/vice`

### [Files]

-   [\~/.config/vice] --- Local (per user) configuration file.

## [Usage]

## [Troubleshooting]

### [Inability to access CPU history in the monitor]

The remote monitor\'s CPU history feature is disabled by default. To enable it, VICE must be compiled with the *cpu_history* use flag.

### [][How do I convert a BASIC game to ASCII text or vice-versa?]

The syntax for petcat is somewhat counterintuitive. Different BASIC versions require different options and, because CBM BASIC had many overlapping extensions provided by third parties the specific BASIC version cannot be autodetected. Assuming a CBM BASIC v2 file from a VIC-20 or C64, to tokenize it run the following command:

`user `[`$`]`petcat -w2 -o tokenized-file.prg -- detokenized-text-file.bas`

Similarly, to convert a tokenized BASIC file to ASCII text, do the following:

`user `[`$`]`petcat -w2 -o program.bas -- program.prg`

### [][Is it possible to port CBM BASIC to a modern BASIC implementation?]

Yes, with effort --- assuming the code isn\'t heavily laden with 6502 machine language instructions packed into `DATA` statements.

In principal, once a CBM BASIC file is detokenized into ASCII there several modern BASICs which can serve as a migration target. In practice, [FreeBASIC](https://wiki.gentoo.org/wiki/FreeBASIC "FreeBASIC") which was originally an open source clone of QuickBASIC makes an ideal target because it supports both legacy BASIC programming styles and a modern fully featured BASIC dialect. Further, unlike many BASIC implementations FreeBASIC is compiled, not interpreted.

The downside is that the FreeBASIC compiler lacks sprite support. So the use of a bitmap graphics library that supports sprites will be necessary. Also, while FreeBASIC supports `PEEK` and `POKE` keywords in \"qb\" mode the memory map is completely different. So replacing these with their functional equivalents is likely to be tedious.

### [][How do I configure VICE to use JiffyDOS or other Third Party Kernal?]

First, you must legally obtain a JiffyDOS license from [Retro Innovations](https://store.go4retro.com/). (Yes, that\'s right, the JiffyDOS firmware is *sill* commercially available nearly 40 years after its initial release.) Once you have a copy of the JiffyDOS kernal and drive ROMS edit [\~/.config/vice] as follows:

[FILE] **`~/.config/vice/vicerc`Adding JiffyDOS support to VICE**

    [C64]
    DosName1541="/location/of/rom/jiffydos-1541.bin"
    KernalName="/location/of/rom/jiffydos-kernal.bin"

The foregoing assumes the most common configuration: a C64 paired with the 1541 floppy disk drive. The above example can be easily modified for other configurations. Please note that with JiffyDOS enabled the kernal disables tape drive support if present.

### [][I am a C64 developer/demo coder, how do I make unit testing with VICE\'s monitor faster?]

When the C64 emulator starts the kernal performs a memory test and returns the number of free bytes available to the system. Since it\'s an emulated machine and virtual RAM does not fail, it\'s possible to disable this test. After making a copy of your kernal from whatever version suits you, perform a binary edit with [xxd] as follows:

`user `[`$`]`echo "1d69: 9f" `

`user `[`$`]` xxd -r - kernal-quick-memtest`

Once you have your edited kernal ROM, modify your *vicerc* or pass this modified kernal at runtime. This will shave \~3 seconds off the start up time of the emulated system. This saves a lot of time when performing rapid unit testing, especially of such unit tests are performed in serial.

Lastly, consider using a unit testing tool that supports thread safe async. Multiple overlapping tests will complete faster. If you take this approach, each instance of the vice monitor will need to be run on a different port. This can be accomplished with the

`user `[`$`]`x64sc.gtk -remotemonitoraddress 127.0.0.1:65xx`

where xx is the desired port. This same trick will work with the binary monitor. Note the default ports for the remote monitor is tcp/6510 and tcp/6502 for the binary monitor.

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose app-emulation/vice`

## [See also]

-   [xa](https://wiki.gentoo.org/wiki/Xa "Xa") --- a high-speed, two-pass portable cross-assembler for the 6502 CPU with a C-like preprocessor
-   [FreeBASIC](https://wiki.gentoo.org/wiki/FreeBASIC "FreeBASIC") --- a modern, self-hosting, object oriented, [BASIC](https://wiki.gentoo.org/wiki/BASIC "BASIC") compiler that is optionally backwards compatible with [QuickBASIC](https://en.wikipedia.org/wiki/QuickBASIC "wikipedia:QuickBASIC")

## [External resources]

-   [Codebase64](https://codebase64.org/) a wiki devoted to C64 development.
-   [64tass](http://tass64.sourceforge.net/) a powerful and expressive macro assembler for the 6502-based computers.
-   [C64 Wiki](https://www.c64-wiki.com/) a wiki devoted to all things C64.
-   The [Commander X16](https://www.commanderx16.com/) The 8-bit Guy\'s \"8-bit dream machine\" built with discrete components intended as a learning tool. An open source [emulator](https://github.com/commanderx16/x16-emulator/) is available on GitHub.
-   The [MEGA65](https://mega65.org/) an open source greatly enhanced clone of the unreleased Commodore 65 home computer designed around an FPGA and currently currently in production. An open source [emulator](https://github.lgb.hu/xemu/) is also available on GitHub.