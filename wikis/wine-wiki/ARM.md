# ARM support

### Motivation

Windows apps are mostly compiled for x86 and they won't run on ARM with
bare Wine, likewise ARM applications won't run on x86(_64) with bare
Wine, so this is not our motivation.

The original motivation was to be able to run winelib-apps on ARM, that
even was before it got public that win8 will run on ARM devices.
Meanwhile we support these new ARM PEs for win8!

### Status

- Yes, It works! (TM)
- Running win8 ARM PEs also works.
- Already ported Putty to ARM as winelib application.
- Wine on ARM already gets packaged by Debian (since 1.7.35), Fedora,
  Maemo and openSUSE.
- Good debugger/disassembler support.
- Relay tracing.
- Relocation.
- Linux Kernel patched upstream for running Windows RT applications
  see ~~#31322~~

### Todo

- [wine-gecko](Gecko) ARM port (waiting for mingw-w64-arm).
- [wine-mono](Wine-Mono) ARM port (requires JIT/seh code
  modification, and a few non-essential support libraries fail to
  build).
- DCOM

### How to help

- Run winetest and report your results.
- Fix test failures or analyse them, see below.
- Report bugs with winelib or Windows RT applications.
- Write tests for missing functions.

### Compiling

Toolchains: Every toolchain with Thumb support should work as we are
independent from the crti.o mode since wine-1.5.8

Compiling on the ARM Device is recommended:

`../configure && make`

Anyway here is a crosscompiling example:

`../configure --host=arm-linux-gnueabihf host_alias=arm-linux-gnueabihf --with-wine-tools=../path/to/your/native/wine/build && make`

Maybe you also should append something like:

`CFLAGS="-mcpu=yourcpu -g -O2" LDFLAGS="-mcpu=yourcpu"`

Fixme/Todo: Compiling inside a chroot

### Running Windows RT Applications

You can find a list of such ported applications at
[forum.xda-developers.com](https://forum.xda-developers.com/showthread.php?p=36534446).
To run them you'll need a recent Wine and a Linux Kernel with the
[tpidrurw
patch](https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/commit/?id=a4780adeefd042482f624f5e0d577bf9cdcbb760),
it's included since Kernel 3.11-rc1. When you're unsure if the Kernel
you are using supports it, you can clone, make and run
[tpidrurw-test](https://github.com/AndreRH/tpidrurw-test), it'll tell
you if your Kernel is suitable.

### Running Windows CE Applications

That's still pre-alpha/proof-of-concept and not part of official Wine,
don't expect any success. WineCE can be found at
[github](https://github.com/AndreRH/wine/tree/winece).

### Running Windows/x86 Applications

See [Emulation](Emulation)

### Analyzed/Known Test Failures

- d3dx9_36:mesh
  - Crashes, bug #43945
- mscoree:mscoree
  - no wine-mono for arm, bug #43937
- mshtml:\* (FIXME: also applies to several others)
  - no wine-gecko for arm, bug #43938
- msi:action
  - bug #43944
- msvcr100:msvcr100
  - softfloat vs. hardfloat
- rpcrt4:cstub
  - bug #43960
- user32:class
  - per dissonant compile time checks the testsuite expects the x86
    value for cbWndExtra, whereas the code uses the pointer size

### Wine and Valgrind

Currently a work in progress - Austin English

- [running valgrind + wine on armv7l gives illegal
  opcode](https://bugs.kde.org/show_bug.cgi?id=386425)

### See also

- Wine On [Android](Android)

- [ARM Bugs](https://bugs.winehq.org/buglist.cgi?query_format=advanced&rep_platform=arm&list_id=88611&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&bug_status=RESOLVED)

- AArch64: [ARM64](ARM64)

- André Hentschel and Vincent Povirk's slides can be found here:
  [FOSDEM 2013](WineConf/FOSDEM-2013)

- For Windows RT recompiled applications check: [at
  xda-developers](https://forum.xda-developers.com/showthread.php?t=2092348)

- Examples of [Winelib](Winelib) ports: [- on
  OpenPandora](https://pyra-handheld.com/boards/threads/wine-qemu.58585/)

- Example use of [Qemu](https://fabrice.bellard.free.fr/qemu/) for
  running x86 code: [Wine for PPC (per qemu usermode
  emulation)](https://lists.fixstars.com/pipermail/yellowdog-general/2004-June/014468.html)

- There was some experience using Qemu to run the Wine x86 binary under
  Zaurus's ARM Debian:
  <https://www.oesf.org/forum/index.php?showtopic=14829>

- Qemu Backend success story:
  <https://forum.winehq.org/viewtopic.php?t=13286> and
  <https://forum.winehq.org/viewtopic.php?t=13330>

- Mixed topic, including ARM discussions:
  <https://forum.winehq.org/viewtopic.php?p=67218>

- Some x86-to-ARM translation strategies were also discussed:
  <https://forum.openhandhelds.org/viewtopic.php?f=16&t=1088>

- Android running x86 wine and solitaire (by using ubuntu hack and
  binfmt): <https://forum.xda-developers.com/showthread.php?t=1258506>

- Winulator ([Android APP](https://www.winulator.com/)) claims it is
  not wine-based, but does somewhat the same a Wine x86_2_ARM would
  do: <https://docs.winulator.com/faq>

- [win86emu](https://forum.xda-developers.com/showthread.php?t=2095934)
  is Bochs and [DOSBox](DOSBox) based and run x86 Applications on
  Windows RT

- Limbo is an Intel x86 PC Emulator for Android based on QEMU,also
  uses code from
  [android-vnc-viewer](https://code.google.com/p/android-vnc-viewer)
  and [glib](https://developer.gnome.org/glib) among others:
  <https://code.google.com/p/limbo-android/>

- Eltechs' [ExaGear
  RPG](https://eltechs.com/product/exagear-mobile/exagear-rpg/) allows
  x86 applications to run on Android using wine.
