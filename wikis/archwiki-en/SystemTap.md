# SystemTap

SystemTap provides free software (GPL)
infrastructure to simplify the gathering of information about the running Linux system.

## Installation
Simply install the  package.

## Standard kernel
You will need at least the  package installed.

Because Arch permanently strips debugging data from its distributed binaries (including the kernel),
many normal/fancier systemtap capabilities are simply not available, so many examples at  will not work.  However, see  for the NON-DWARF and AUTO-DWARF probe types for what should still work, for example:

* kernel tracepoints: kernel.trace("*")
* user-space probes: process("...").function("...")  (for programs you build yourself with -g)
* user-space markers: process("...").mark("...")   (if they were configured with the '''' markers)
* perfctr-based probes: perf.*
* non-dwarf kernel probes: kprobe.function("...") and nd_syscall.* tapset  (if a /boot/System.map* file is available, see below).

## Kernel rebuild
You may consider to build a linux-custom package to run SystemTap, but rebuilding the  package is easy and efficient.

## Prepare
First, follow the steps at Kernel/Arch build system#Getting the ingredients to get the original kernel build files.
Then use  to get the additional files. By performing the verification, you can safely skip the steps on "Update checksum".

## Modify config
Edit , turn on these options:

*
*
*
*
*
*
*
*
*
*

By default only CONFIG_DEBUG_INFO and CONFIG_DEBUG_INFO_REDUCED are not set.

With the current linux kernel (tested with 3.15.2) you can simply append these lines into :

## Update checksum
Run  to get a new sha256sum.

In PKGBUILD file, the  has the same order with
, put your new sha256sum in the right place.

## Build and install
Optional: It is recommended to set  in  to speed up the compilation.

The rebuilt  and  packages should be reinstalled,  does not matter.

Via this method, external modules (e.g.  and ) do not need to be rebuilt.

## Build custom kernel
Please reference this README

## Troubleshooting
## Pass 4 fails when launching
If you get the following error message, try into install

 /usr/share/systemtap/runtime/stat.c:214:2: error: 'cpu_possible_map' undeclared (first use in this function)

## System.map is missing
You can recover it where you build your linux kernel with DEBUG_INFO enabled

 # cp src/linux-3.6/System.map /boot/System.map-3.6.7-1-ARCH

Alternatively,

 # cp /proc/kallsyms /boot/System.map-$(uname -r)

## Process return probes not available
If you are sure that your kernel configuration is correct, but on launching  you get both of the following messages:

 WARNING: Kernel function symbol table missing warning::symbols
 semantic error: process return probes not available error::inode-uprobes

then SystemTap may have failed to verify support for this feature. You can fix this by following the steps in #System.map is missing.
