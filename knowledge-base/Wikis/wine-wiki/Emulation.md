# Emulation

Wine can run on different architectures, still most available Windows
applications are x86 ones. As Wine Is Not an Emulator, all those
applications can't run on other architectures with Wine alone. Here, we
want to discuss some options on how to use Wine together with emulators
to achieve what Wine can't do alone.

### System emulation

The easiest thing, but slowest, is to use an emulator to run a full x86
Linux installation in it. For example you can grab an image from
[stacklet](https://stacklet.com/), [this
list](https://wiki.qemu.org/Testing/System_Images) or somewhere else and
run it with [QEMU](https://www.qemu.org). There are many instructions
for that on the Internet and you can also use different emulators, like
e.g. \[Bochs <https://bochs.sourceforge.net/>\]. Still, this solution
involves even booting the system and doesn't integrate very good into
your desktop.

### User-Space-Emulation

<small><small>(Or User-Mode Emulation)</small></small>
At least on Linux it is possible to use QEMU to jump out of emulation at
syscall level. This means your native kernel is used and there is no
need to emulate one. This approach also integrates well into your
Desktop and doesn't require a big image file. Still you need Wine
compiled for x86 and all it's dependencies, which could be done with
[Buildroot](Buildroot) or tools like
[debootstrap](https://wiki.debian.org/Debootstrap). There is an old
thread on the Forums on how to setup Wine for User-Space-Emulation: [I
got Wine/x86 1.5.11 to run on Linux/ARM with
qemu!](https://forum.winehq.org/viewtopic.php?f=2&t=17701). If your QEMU
is not too old, you most likely don't have to patch and/or compile it
yourself. You still might need a x86 WINEPREFIX from a different
machine.
It seems a ready-to-use version for Raspberry Pis can be found here:
[github/AlbrechtL/RPi-QEMU-x86-wine](https://github.com/AlbrechtL/RPi-QEMU-x86-wine)

Faster emulators for that are [Box86](https://github.com/ptitSeb/box86)/[Box64](https://github.com/ptitSeb/box64) and [FEX](https://github.com/FEX-Emu/FEX/):

Box86/Box64 don't require a x86 rootfs, only a x86/x86_64 Wine. There are Wine specific instructions [here](https://github.com/ptitSeb/box86/blob/master/docs/X86WINE.md) and [here](https://github.com/ptitSeb/box64/blob/main/docs/X64WINE.md).

FEX requires a [rootfs](https://wiki.fex-emu.com/index.php/Development:Setting_up_RootFS) which can be automatically downloaded by the installer from the [quick start guide](https://github.com/FEX-Emu/FEX/?tab=readme-ov-file#quick-start-guide)

### Hangover (since Version 9.20)

Besides the WoW64 mechanism for 32-bit emulation it also supports ARM64EC for 64-bit emulation.
It works for win32 (arm & i386) and win64 (x86_64) applications on
[ARM64](ARM64) and partly x86_64 and RISC-V. The code can be found at
[GitHub](https://github.com/AndreRH/hangover).

### Hangover (since Version 0.8.1)

This new approach uses the WoW64 mechanism to plug in an emulator. Here
we jump out of emulation at the win32 syscall level. This means you only
need one Wine build including all the PE architectures you want to run
on. It works for win32 applications (arm & i386) on
[ARM64](ARM64) and x86_64. The code can be found at
[GitHub](https://github.com/AndreRH/hangover).

### Hangover (classic, before Version 0.8.1)

Similar to User-Space-Emulation, but much faster. Here we jumped out
of emulation at the win32 API level. This means you only need a native
Wine installation, some wrapper DLLs and some Wine DLLs comiled for
Windows.  It worked on [ARM64](ARM64), ppc64le and x86_64 with Linux,
Mac or [Android](Android). The code can be found at
[GitHub](https://github.com/AndreRH/hangover). See also
[WineConf 2017](WineConf/WineConf-2017#hangover-project-by-stefan-d%C3%B6singer-and-andr%C3%A9-hentschel).
