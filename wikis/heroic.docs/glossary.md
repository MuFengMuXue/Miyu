# Glossary

Here is a glossary of terms you may encounter when using the Heroic Game Launcher.  (Please keep this list in alphabetical order when adding entries.)

# EAAC
EA (Electronic Arts) AntiCheat, an anti-cheat system from EA, announced in September 2022.

Not to be confused with [EAC](#eac)

# EAC
Easy Anti-Cheat, an anti-cheat system commonly used in multi-player games.  Games using EAC almost always require additional workarounds to get working under Wine or Proton, and many are unplayable under Wine/Proton.

Not to be confused with [EAAC](#eaac)

# EOS Overlay
Epic Online Services Overlay, the in-game overlay for games from the Epic Games Store.  The EGS counterpart to the Steam Overlay and GOG Galaxy Overlay.

# ESync
Wine eventfd-based synchronization, a wineserver feature to reduce overhead for synchronization objects.  See the Lutris [How To Esync](https://github.com/lutris/docs/blob/master/HowToEsync.md) guide for how to check whether your system supports ESync.

See also FSync.

# FSync

A more performant ESync, but one that requires kernel-level support.  This is available in the mainline Linux kernel from 5.16 onwards[*](https://forums.lutris.net/t/fsync/14179/2).

See also ESync

# [Feral GameMode](https://github.com/FeralInteractive/gamemode)
GameMode is
> a daemon/lib combo for Linux that allows games to request a set of optimisations be temporarily applied to the host OS and/or a game process.

# FSR
AMD FideltyFX Super Resolution, a hardware-assisted upscaling feature on AMD GPUs.

# GameMode
See [Feral GameMode](#feral-gamemode)

# GE
A common abbreviation of [GloriousEggroll](https://github.com/GloriousEggroll), aka Thomas Crider, author of custom Wine and Proton builds.

# [MangoHud](https://github.com/flightlessmango/MangoHud)
MangoHud is an overlay for monitoring FPS, temperatures, CPU/GPU load, etc. for Vulkan and OpenGL applications.

# [Proton](https://github.com/ValveSoftware/Proton)
Valve's fork of [Wine](#wine) with additional components and patches.  Some changes eventually make it into upstream Wine.

# Resizable BAR
An optional feature on NVIDIA 30xx cards that gives the CPU access to the whole GPU framebuffer at once, which may improve performance on some games.

# scout
The codename for Steam Runtime version 1, which uses `LD_LIBRARY_PATH` and is used for native Linux games and by Proton 5.0 and earlier.

See also [Steam Linux Runtime](#steam-linux-runtime) and [scout](#scout)

# soldier
The codename for Steam Runtime version 2, which uses containers and is used by Proton 5.13 and later.

See also [Steam Linux Runtime](#steam-linux-runtime) and [soldier](#soldier)

# [Steam Linux Runtime](https://github.com/ValveSoftware/steam-runtime)
The Steam Linux runtime is a binary linux environment under which native Linux games can be run to avoid having to manually install all the game's dependencies, or to avoid dependency hell for games that are binary-incompatible with the library versions shipped by your distribution.

# [Wine](https://www.winehq.org/)
> Wine (originally an acronym for "Wine Is Not an Emulator") is a compatibility layer capable of running Windows applications on several POSIX-compliant operating systems, such as Linux, macOS, & BSD. Instead of simulating internal Windows logic like a virtual machine or emulator, Wine translates Windows API calls into POSIX calls on-the-fly, eliminating the performance and memory penalties of other methods and allowing you to cleanly integrate Windows applications into your desktop.

See also [Proton](#proton)
