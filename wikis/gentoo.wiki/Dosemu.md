**Resources**

[[]][Home](http://www.dosemu.org/)

[[]][Official documentation](http://www.dosemu.org/docs/README/1.4/)

[[]][Package information](https://packages.gentoo.org/packages/app-emulation/dosemu)

[[]][Wikipedia](https://en.wikipedia.org/wiki/DOSEMU "wikipedia:DOSEMU")

[[]][Bugs (upstream)](https://sourceforge.net/p/dosemu/bugs/)

**DOSEMU** is an application compatibility layer for [MS-DOS](https://en.wikipedia.org/wiki/MS-DOS "wikipedia:MS-DOS") geared more towards running MS-DOS applications than running games. Despite its name, DOSEMU is not an MS-DOS emulator. Similar to [Wine](https://wiki.gentoo.org/wiki/Wine "Wine"), it is an application compatibility later that provides just enough hardware virtualization give DOS applications with a familiar execution environment; MS-DOS compatible system files are required for it to actually work. In modern times, [FreeDOS](https://www.freedos.org/) is usually the preferred alternative to MS-DOS. Lastly, DOSEMU makes no provision for CPU emulation on non-x86 architectures. So, DOSEMU is bound to the x86/amd64 instruction set architecture. Therefore, it will not work on common single board computers such as the [Raspberry Pi](https://wiki.gentoo.org/wiki/Raspberry_Pi "Raspberry Pi").

Command line programs that do not require historical IBM PC graphics modes can run in a terminal window without difficulty, just like any other terminal application. Applications that require graphics and sound work too, provided DOSEMU has been adequately configured.

DOSEMU cannot be used to run 16-bit versions of Microsoft Windows, such as Windows 3.*x*.

## Contents

-   [[1] [History]](#History)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [USE flags]](#USE_flags)
    -   [[2.2] [Emerge]](#Emerge)
    -   [[2.3] [Additional software]](#Additional_software)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Files]](#Files)
-   [[4] [Usage]](#Usage)
    -   [[4.1] [Invocation]](#Invocation)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [I can\'t build DOSEMU with LLVM/Clang]](#I_can.27t_build_DOSEMU_with_LLVM.2FClang)
    -   [[5.2] [Why are file names longer than 8 characters all messed up?]](#Why_are_file_names_longer_than_8_characters_all_messed_up.3F)
-   [[6] [Removal]](#Removal)
    -   [[6.1] [Unmerge]](#Unmerge)
-   [[7] [See also]](#See_also)
-   [[8] [External resources]](#External_resources)

## [History]

First released in 1992 --- only a year after the first public release of Linux --- DOSEMU quickly became a mainstay among early Linux. MS-DOS was dominant operating system in the the PC market at the time and would remain so until the mid 1990\'s. While the GNU project had furnished Linux with many important userland tools, some very popular development tools of the period were MS-DOS only applications. Further, common office applications of the era wouldn\'t see open source counterparts emerge for almost a decade. In time, DOSEMU would allow the Linux users of the era ready access business critical applications such as the word processor WordPerfect and spreadsheet application Lotus 1-2-3.

In the very early 2000\'s [DOSBox](https://wiki.gentoo.org/index.php?title=DOSBox&action=edit&redlink=1 "DOSBox (page does not exist)") would emerge as a competitor to DOSEMU. By the middle part of the decade DOSEMU development would slow, and by 2007 it would see its final release. While DOSEMU remains popular among those who wish to use MS-DOS software on Linux, the full-fledged emulator DOSBox now sees wide usage among MS-DOS gamers.

DOSEMU is still available on Gentoo for those seeking a comparatively lightweight MS-DOS compatibility layer. Unfortunately, the passage of time has not been kind to DOSEMU. Over several major releases the Linux kernel API has changed such that some previously valid DOSEMU configurations behave unexpectedly or outright fail. To minimize this effect Gentoo has accumulated a number of custom patches to the DOSEMU codebase intended to keep DOSEMU stable. Unfortunately, the situation is a bit tenuous and users who encounter serious stability issues are encouraged to file a bug report.

While the original DOSEMU project has fizzled out, DOSEMU itself is not dead. A revitalized fork of the project, called [dosemu2](https://dosemu2.github.io/dosemu2/), began in 2012. Currently the project is in a pre-release state but boasts a native 64-bit DOS kernel called fdpp which leverages [KVM](https://wiki.gentoo.org/wiki/KVM "KVM") for virtualization, a native command.com compatible shell with long file name support, and a reworked security model. Also, a lightweight x86 CPU emulator is in currently in development which will allow future versions of dosemu2 to run on non-x86 architectures.

The dosemu2 fork is not yet available as a Gentoo ebuild.

## [Installation]

### [USE flags]

### [USE flags for] [app-emulation/dosemu](https://packages.gentoo.org/packages/app-emulation/dosemu) [[]] [DOS Emulator]

  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`X`](https://packages.gentoo.org/useflags/X)                     Add support for X11
  [`alsa`](https://packages.gentoo.org/useflags/alsa)               Add support for media-libs/alsa-lib (Advanced Linux Sound Architecture)
  [`debug`](https://packages.gentoo.org/useflags/debug)             Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`fluidsynth`](https://packages.gentoo.org/useflags/fluidsynth)   use media-sound/fluidsynth for MIDI emulation
  [`gpm`](https://packages.gentoo.org/useflags/gpm)                 Add support for sys-libs/gpm (Console-based mouse driver)
  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-09-28 14:31] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-emulation/dosemu`

### [Additional software]

By default DOSEMU comes with FreeDOS 1.0 installed. To install the latest OS kernel, do the following:

1.  Go to [FreeDOS.org](https://freedos.org) and download the latest CD-ROM [.iso] file.
2.  Extract the following files:
    -   [COMMAND.COM]
    -   [KERNEL.SYS]
    -   [fdconfig.sys]
3.  Copy the files to [\$HOME/.dosemu/drive_c/] making sure to overwrite the originals FreeDOS 1.0 files.

## [Configuration]

### [Files]

-   [/etc/dosemu/dosemu.conf] --- system-wide configuration file.
-   [\$HOME/.dosemurc] --- per-user configuration file.
-   [\$HOME/.dosemu/boot.log] --- debug logging.
-   [\$HOME/.dosemu/drive_c/] --- local user DOSEMU instance containing the root of DOS drive [C:\\].

## [Usage]

### [Invocation]

`user `[`$`]`dosemu --help`

    dosemu-1.4.0.8

    USAGE:
      dosemu [options] [ [-E] linux path or dos command ]

        -2,3,4,5,6 choose 286, 386, 486 or 586 or 686 CPU
        -A boot from first defined floppy disk (A)
        -B boot from second defined floppy disk (B) (#)
        -C boot from first defined hard disk (C)
        -c use PC console video (!%)
        -d detach console
        -X run in X Window (#)
        -S run in SDL (#)
        -D set debug-msg mask to flags
           #=default int                       A=ASPI
           C=CDROM                             D=dos int 21h
           E=EMS                               I=IPC
           M=DPMI                              P=Packet driver
           Q=Mapping driver                    R=disk READ
           S=SOUND                             T=I/O trace
           W=disk WRITE                        X=X support
           Z=PCI                               a=Set all levels
           c=configuration                     d=disk msgs
           e=cpu-emu                           g=general messages
           h=hardware                          i=i/o instructions (in/out)
           j=joystick                          k=keyboard
           m=mouse                             n=IPX network
           p=printer                           q=DMA
           r=PIC request                       s=serial
           u=Unicode translation               v=video
           w=warnings                          x=XMS
        -E STRING pass DOS command on command line (but don't exit afterwards)
        -e SIZE enable SIZE K EMS RAM
        -F use File as global config-file
        -f use dosrcFile as user config-file
        --Fusers bypass /etc/dosemu.users (^^)
        --Flibdir change keymap and FreeDOS location
        --Fimagedir bypass systemwide boot path
        -n bypass the system configuration file (^^)
        -L load and execute DEXE File
        -I insert config statements (on commandline)
        -i[bootdir] (re-)install a DOS from bootdir or interactively
        -h dump configuration to stderr and exit (sets -D+c)
           0=no parser debug, 1=loop debug, 2=+if_else debug
        -H wait for dosdebug terminal at startup and pass dflags
        -k use PC console keyboard (!)
        -M set memory size to SIZE kilobytes (!)
        -m toggle internal mouse driver
        -N No boot of DOS
        -O write debug messages to stderr
        -o FILE put debug messages in file
        -P copy debugging output to FILE
        -p stop for prompting with a non-fatal configuration problem
        -s enable direct hardware access (full feature) (!%)
        -t use terminal (S-Lang) mode
        -u set user configuration variable 'confvar' prefixed by 'u_'.
        -V use BIOS-VGA video modes (!#%)
        -v NUM force video card type
        -w toggle windowed/fullscreen mode in X
        -x SIZE enable SIZE K XMS RAM
        -U PIPES calls init_uhook(PIPES) (???)

        (!) BE CAREFUL! READ THE DOCS FIRST!
        (%) require DOSEMU be run as root (i.e. suid)
        (^^) require DOSEMU not be run as root (i.e. not suid)
        (#) options do not fully work yet

      xdosemu [options]   == dosemu [options] -X

      dosemu --help
      dosemu --version    print version of dosemu (and show this help)
    dosemu --help (return code: 0)
    can't create local /root/.dosemu/run directory
    dosemu-1.4.0.

    USAGE:
      dosemu [options] [ [-E] linux path or dos command ]

        -2,3,4,5,6 choose 286, 386, 486 or 586 or 686 CPU
        -A boot from first defined floppy disk (A)
        -B boot from second defined floppy disk (B) (#)
        -C boot from first defined hard disk (C)
        -c use PC console video (!%)
        -d detach console
        -X run in X Window (#)
        -S run in SDL (#)
        -D set debug-msg mask to flags
           #=default int                       A=ASPI
           C=CDROM                             D=dos int 21h
           E=EMS                               I=IPC
           M=DPMI                              P=Packet driver
           Q=Mapping driver                    R=disk READ
           S=SOUND                             T=I/O trace
           W=disk WRITE                        X=X support
           Z=PCI                               a=Set all levels
           c=configuration                     d=disk msgs
           e=cpu-emu                           g=general messages
           h=hardware                          i=i/o instructions (in/out)
           j=joystick                          k=keyboard
           m=mouse                             n=IPX network
           p=printer                           q=DMA
           r=PIC request                       s=serial
           u=Unicode translation               v=video
           w=warnings                          x=XMS
        -E STRING pass DOS command on command line (but don't exit afterwards)
        -e SIZE enable SIZE K EMS RAM
        -F use File as global config-file
        -f use dosrcFile as user config-file
        --Fusers bypass /etc/dosemu.users (^^)
        --Flibdir change keymap and FreeDOS location
        --Fimagedir bypass systemwide boot path
        -n bypass the system configuration file (^^)
        -L load and execute DEXE File
        -I insert config statements (on commandline)
        -i[bootdir] (re-)install a DOS from bootdir or interactively
        -h dump configuration to stderr and exit (sets -D+c)
           0=no parser debug, 1=loop debug, 2=+if_else debug
        -H wait for dosdebug terminal at startup and pass dflags
        -k use PC console keyboard (!)
        -M set memory size to SIZE kilobytes (!)
        -m toggle internal mouse driver
        -N No boot of DOS
        -O write debug messages to stderr
        -o FILE put debug messages in file
        -P copy debugging output to FILE
        -p stop for prompting with a non-fatal configuration problem
        -s enable direct hardware access (full feature) (!%)
        -t use terminal (S-Lang) mode
        -u set user configuration variable 'confvar' prefixed by 'u_'.
        -V use BIOS-VGA video modes (!#%)
        -v NUM force video card type
        -w toggle windowed/fullscreen mode in X
        -x SIZE enable SIZE K XMS RAM
        -U PIPES calls init_uhook(PIPES) (???)

        (!) BE CAREFUL! READ THE DOCS FIRST!
        (%) require DOSEMU be run as root (i.e. suid)
        (^^) require DOSEMU not be run as root (i.e. not suid)
        (#) options do not fully work yet

      xdosemu [options]   == dosemu [options] -X

      dosemu --help
      dosemu --version    print version of dosemu (and show this help)

## [Troubleshooting]

### [][I can\'t build DOSEMU with LLVM/Clang]

This is a known issue. It\'s not a bug in DOSEMU, it\'s a limitation of Clang. On Intel-based platforms LLVM assumes that the Pentium processor is the minimum CPU target, so is not possible to generate 16-bit 8086 assembly with Clang. The workaround is to use [GCC](https://wiki.gentoo.org/wiki/GCC "GCC") to compile DOSEMU. See [[[bug #729240]](https://bugs.gentoo.org/show_bug.cgi?id=729240)[]].

### [][Why are file names longer than 8 characters all messed up?]

MS-DOS was limited to 8 character file names with a 3 character extension. This is sometimes referred to as the \"8.3\" file name convention. So, file names such as [foobar.exe] were valid, but not [my_very_foobar.exe]. This is a limitation of the FAT12 (floppies) and FAT16 (hard drives). With the release of [Windows 95](https://en.wikipedia.org/wiki/Windows_95 "wikipedia:Windows 95") a modified version of FAT, called VFAT, added support for long file names in a backwards compatible way. Regardless of the underlying file system of [\$HOME/.dosemu/drive_c/] DOSEMU must access the data in a DOS compatible way, this means treating all file operations as if the underlying volume was VFAT. So, even on a very modern Linux file system DOSEMU will only \"see\" the files as if they\'re on a VFAT partition.

Many native FreeDOS applications support long file names, notably its own version of [command.com] but most legacy DOS applications cannot natively support long file names. Hence the weirdly abbreviated file names that tend to follow the pattern of [letters\~ or similar. It is sometimes possible to improve the situation by updating to the latest version of [DOSLFN](http://adoxa.altervista.org/doslfn/).

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose app-emulation/dosemu`

## [See also]

-   [DOSBox](https://wiki.gentoo.org/index.php?title=DOSBox&action=edit&redlink=1 "DOSBox (page does not exist)")
-   [Wine](https://wiki.gentoo.org/wiki/Wine "Wine") --- an application compatibility layer that allows [Microsoft Windows](https://en.wikipedia.org/wiki/Microsoft_Windows "wikipedia:Microsoft Windows") software to run on Linux and other [POSIX](https://en.wikipedia.org/wiki/POSIX "wikipedia:POSIX")-compliant operating systems.
-   [KVM](https://wiki.gentoo.org/wiki/KVM "KVM") --- a generic, open-source hardware emulator and virtualization suite.
-   [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU") --- a generic, open-source hardware emulator and virtualization suite.

## [External resources]

-   [FreeDOS](https://freedos.org) an open source MS-DOS compatible operating system.
-   [dosemu2](https://dosemu2.github.io/dosemu2/) the eventual replacement for the original DOSEMU.