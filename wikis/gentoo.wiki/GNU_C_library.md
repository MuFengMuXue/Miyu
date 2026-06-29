[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Glibc&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.gnu.org/software/libc/)

[[]][Package information](https://packages.gentoo.org/packages/sys-libs/glibc)

[[]][Official project wiki](https://sourceware.org/glibc/wiki)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Glibc "wikipedia:Glibc")

[[]][Bugs (upstream)](https://www.gnu.org/software/libc/bugs.html)

The *GNU C library*, aka **glibc**, is the default [C library](https://wiki.gentoo.org/wiki/Libc "Libc") included with Gentoo Linux.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Upgrades]](#Upgrades)
        -   [[1.2.1] [OpenRC]](#OpenRC)
        -   [[1.2.2] [systemd]](#systemd)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Glibc locale system]](#Glibc_locale_system)
-   [[3] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [sys-libs/glibc](https://packages.gentoo.org/packages/sys-libs/glibc) [[]] [GNU libc C library]

  --------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+clone3`](https://packages.gentoo.org/useflags/+clone3)                         Enable the new clone3 syscall within glibc. Can be disabled to allow compatibility with older Electron applications.
  [`+crypt`](https://packages.gentoo.org/useflags/+crypt)                           build and install libcrypt and crypt.h
  [`+multiarch`](https://packages.gentoo.org/useflags/+multiarch)                   enable optimizations for multiple CPU architectures (detected at runtime)
  [`+ssp`](https://packages.gentoo.org/useflags/+ssp)                               protect stack of glibc internals
  [`+static-libs`](https://packages.gentoo.org/useflags/+static-libs)               Build static versions of dynamic libraries as well
  [`audit`](https://packages.gentoo.org/useflags/audit)                             Enable support for Linux audit subsystem using sys-process/audit
  [`caps`](https://packages.gentoo.org/useflags/caps)                               Use Linux capabilities library to control privilege
  [`cet`](https://packages.gentoo.org/useflags/cet)                                 Enable Intel Control-flow Enforcement Technology (needs binutils 2.29 and gcc 8)
  [`clang`](https://packages.gentoo.org/useflags/clang)                             Allow building with clang (if proper environment is set). Highly experimental. Disable to auto-force gcc usage.
  [`compile-locales`](https://packages.gentoo.org/useflags/compile-locales)         build \*all\* locales in src_install; this is generally meant for stage building only as it ignores /etc/locale.gen file and can be pretty slow
  [`custom-cflags`](https://packages.gentoo.org/useflags/custom-cflags)             Build with user-specified CFLAGS (unsupported)
  [`debug`](https://packages.gentoo.org/useflags/debug)                             When USE=hardened, allow fortify/stack violations to dump core (SIGABRT) and not kill self (SIGKILL)
  [`doc`](https://packages.gentoo.org/useflags/doc)                                 Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`experimental-loong`](https://packages.gentoo.org/useflags/experimental-loong)   Add experimental LoongArch patchset
  [`gd`](https://packages.gentoo.org/useflags/gd)                                   build memusage and memusagestat tools
  [`hash-sysv-compat`](https://packages.gentoo.org/useflags/hash-sysv-compat)       enable sysv linker hashes in glibc for compatibility with binary software (EAC via wine/proton)
  [`headers-only`](https://packages.gentoo.org/useflags/headers-only)               Install only C headers instead of whole package. Mainly used by sys-devel/crossdev for toolchain bootstrap.
  [`multilib`](https://packages.gentoo.org/useflags/multilib)                       On 64bit systems, if you want to be able to compile 32bit and 64bit binaries
  [`multilib-bootstrap`](https://packages.gentoo.org/useflags/multilib-bootstrap)   Provide prebuilt libgcc.a and crt files if missing. Only needed for ABI switch.
  [`nscd`](https://packages.gentoo.org/useflags/nscd)                               Build, and enable support for, the Name Service Cache Daemon
  [`perl`](https://packages.gentoo.org/useflags/perl)                               Install additional scripts written in Perl
  [`profile`](https://packages.gentoo.org/useflags/profile)                         Add support for software performance analysis (will likely vary from ebuild to ebuild)
  [`selinux`](https://packages.gentoo.org/useflags/selinux)                         !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`sframe`](https://packages.gentoo.org/useflags/sframe)                           enable building with sframe backtrace support
  [`stack-realign`](https://packages.gentoo.org/useflags/stack-realign)             Realign the stack in the 32-bit build for compatibility with older binaries at some performance cost
  [`static-pie`](https://packages.gentoo.org/useflags/static-pie)                   Enable static PIE support (runtime files for -static-pie gcc option).
  [`suid`](https://packages.gentoo.org/useflags/suid)                               Make internal pt_chown helper setuid \-- not needed if using Linux and have /dev/pts mounted with gid=5
  [`systemd`](https://packages.gentoo.org/useflags/systemd)                         Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`systemtap`](https://packages.gentoo.org/useflags/systemtap)                     Enable enhanced debugging hooks/interface via SystemTap static probe points. Note that this isn\'t exclusive to SystemTap, despite the name. This provides an interface which dev-debug/gdb optionally uses, see https://sourceware.org/gdb/wiki/LinkerInterface.
  [`test`](https://packages.gentoo.org/useflags/test)                               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`vanilla`](https://packages.gentoo.org/useflags/vanilla)                         Do not add extra patches which change default behaviour; DO NOT USE THIS ON A GLOBAL SCALE as the severity of the meaning changes drastically
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)                   Verify upstream signatures on distfiles
  --------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-20 17:42] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Upgrades]

When glibc is upgraded it is wise to reload the running init system.

#### [OpenRC]

`root `[`#`]`telinit u`

#### [systemd]

`root `[`#`]`systemctl daemon-reload`

## [Usage]

### [Glibc locale system]

** See also**\
See the [`Localization/Guide`](https://wiki.gentoo.org/wiki/Localization/Guide#Locale_system "Localization/Guide") article for more information.

** See also**\
See the [`Configure locales`](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Configure_locales "Handbook:AMD64/Installation/Base") section (Gentoo Handbook) for more information.

## [See also]

-   [GCC](https://wiki.gentoo.org/wiki/GCC "GCC") --- among the most widely used compiler toolchains in the world with official support for: [C](https://wiki.gentoo.org/wiki/C "C"), [C++](https://wiki.gentoo.org/wiki/C%2B%2B "C++"), [Objective-C](https://en.wikipedia.org/wiki/Objective-C "wikipedia:Objective-C"), [Objective-C++](https://en.wikipedia.org/wiki/Objective-C%2B%2B "wikipedia:Objective-C++"), [Modula-2](https://en.wikipedia.org/wiki/Modula-2 "wikipedia:Modula-2"), [Fortran](https://wiki.gentoo.org/wiki/Fortran "Fortran"), [Ada](https://wiki.gentoo.org/wiki/Ada "Ada"), [Go](https://wiki.gentoo.org/wiki/Go "Go"), [COBOL](https://en.wikipedia.org/wiki/COBOL "wikipedia:COBOL"), and [D](https://en.wikipedia.org/wiki/D_(programming_language) "wikipedia:D (programming language)")
-   [LLVM](https://wiki.gentoo.org/wiki/LLVM "LLVM") --- a collection of modular and reusable compiler and toolchain technologies