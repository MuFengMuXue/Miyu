[kpatch] is a GPLv2 licensed dynamic kernel patching tool developed by RedHat.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Workflow]](#Workflow)
-   [[3] [References]](#References)

## [Installation]

### [Kernel]

The Linux kernel must be version 4.0 or higher in order to have `LIVEPATCH` support.^[\[1\]](#cite_note-1)^

[KERNEL] **Enable `CONFIG_LIVEPATCH` support**

    General setup  --->
       [*] Configure standard kernel features (expert users)  --->
          -*-   Load all symbols for debugging/ksymoops
             [*]     Include all symbols in kallsyms
    [*] Enable loadable module support  --->
    Processor type and features  --->
       [*] Kernel Live Patching
    Kernel hacking  --->
       [*] Tracers  --->
          [*]   Kernel Function Tracer
    File systems  --->
       Pseudo filesystems  --->
          -*- sysfs file system support

### [USE flags]

### [USE flags for] [sys-kernel/kpatch](https://packages.gentoo.org/packages/sys-kernel/kpatch) [[]] [Dynamic kernel patching for Linux]

  ----------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+kpatch`](https://packages.gentoo.org/useflags/+kpatch)                     Enable a command-line tool which allows a user to manage a collection of patch modules.
  [`+kpatch-build`](https://packages.gentoo.org/useflags/+kpatch-build)         Enable tools which convert a source diff patch to a patch module.
  [`+strip`](https://packages.gentoo.org/useflags/+strip)                       Allow symbol stripping to be performed by the ebuild for special files
  [`contrib`](https://packages.gentoo.org/useflags/contrib)                     Enable contrib kpatch services files.
  [`dist-kernel`](https://packages.gentoo.org/useflags/dist-kernel)             Enable subslot rebuilds on Distribution Kernel upgrades
  [`kmod`](https://packages.gentoo.org/useflags/kmod)                           Enable a kernel module (.ko file) which provides an interface for the patch modules to register new functions for replacement.
  [`modules-compress`](https://packages.gentoo.org/useflags/modules-compress)   Install compressed kernel modules (if kernel config enables module compression)
  [`modules-sign`](https://packages.gentoo.org/useflags/modules-sign)           Cryptographically sign installed kernel modules (requires CONFIG_MODULE_SIG=y in the kernel)
  [`test`](https://packages.gentoo.org/useflags/test)                           Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-11-04 09:36] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask sys-kernel/kpatch`

## [Usage]

`user `[`$`]`kpatch --help`

### [Workflow]

`root `[`#`]`Kpatch-build foo.patch `

`root `[`#`]`insmod kpatch-foo.ko `

## [References]

1.  [[[↑](#cite_ref-1)] [[https://cateee.net/lkddb/web-lkddb/LIVEPATCH.html](https://cateee.net/lkddb/web-lkddb/LIVEPATCH.html)]]