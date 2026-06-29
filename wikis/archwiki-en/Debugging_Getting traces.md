# Debugging/Getting traces

This article aims to help debugging software by providing traces and debug information. This information can then be used for the bug report to the (upstream) software developers or package maintainers.

## Introduction
Usually, executable files are stripped of human readable context to make them smaller. Obtaining traces without debugging information available drastically reduces their usefulness. For example, a trace from a  session where debugging information is not available may look as follows:

 Backtrace was generated from '/usr/bin/epiphany'

 (no debugging symbols found)
 Using host libthread_db library "/lib/libthread_db.so.1".
 (no debugging symbols found)
 [Thread debugging using libthread_db enabled
 Thread -1241265952 (LWP 12630)
 (no debugging symbols found)
 0xb7f25410 in __kernel_vsyscall ()
 #0  0xb7f25410 in __kernel_vsyscall ()
 #1  0xb741b45b in ?? () from /lib/libpthread.so.0
 shows where debugging info is missing, as well as the name of library or executable which called the function. Similarly, when  appears, you should look for the stated file names.

To obtain a proper trace that is useful to the program developers, follow the next sections. Separate debug files are available for most official Arch packages and can be downloaded with Debuginfod (see #Getting the trace). When enhanced debugging information was not added to the executable in the first place, one has to rebuild the package with debugging symbols enabled.

Use the complete stack trace to inform developers of a bug you have discovered before. This will be highly appreciated by them and will help to improve your favorite program.

## Getting the trace
The actual backtrace (or stack trace) can be obtained via , the GNU Debugger. It can be used in several ways, depending on whether it should start a new instance of a program, attach to an existing process, or examine a previous crash.

## Starting a new instance of a program
Start gdb with an executable program that can be found in  (or a full path):

 $ gdb application

gdb automatically tries to download debug information and symbols for packages in the official repositories. When gdb asks whether Debuginfod should be enabled in the debugging session, answer :

Then, within gdb, type  followed by any arguments you wish the program to start with:

 (gdb) run arguments

Now do whatever is necessary to evoke the bug. gdb will automatically halt the application when it crashes and prompt for commands. In case of freezes or similar issues, press  and you will be returned to the command prompt, too.

Then enable logging to a file:

 (gdb) set logging enabled on

And finally have the backtrace written to the specified file in the current working directory:

 (gdb) thread apply all backtrace full

## Attaching to an existing process
If the program you want to debug is already running, you need to first find its process ID. Tools such as  or  are available. For example:

When the output does not give a unique ID, you can try more filtering or look at the output of  or .

Attaching as regular user does not work by default due to restricted ptrace scope. The restriction can be lowered temporarily with  or you can run gdb as a privileged user, e.g. using sudo.

Start gdb attaching it to the process:

 $ gdb --pid=PID

gdb will ask if Debuginfod should be enabled in this debugging session, to which you should answer .

Note that attaching to a process has stopped it and it needs to be explicitly continued. This replaces the  command from the workflow in the #Starting a new instance of a program section:

 (gdb) continue

Now do whatever is necessary to evoke the bug in the attached process. Then proceed with enabling logging and obtaining the trace same as in #Starting a new instance of a program.

## Examining a previous crash
To debug an application that has already crashed, you will want to invoke gdb on its core dump. See Core dump#Analyzing a core dump for details.

If debugging information for the crashed program is not available and a proper backtrace was not obtained, you may need to rebuild the package and reproduce the crash again.

## Manually getting debug info
The first thing to do is to obtain the names of the packages which require rebuilding or the install of a debug package.

 [...
 Backtrace was generated from '/usr/bin/epiphany'

 (no debugging symbols found)
 Using host libthread_db library "/lib/libthread_db.so.1".
 (no debugging symbols found)
 For example for the above extract from a trace, the package name for the associated package can be obtained with pacman:

The package is called  in version 2.5-8. Repeat this step for every package that needs debugging information.

## Installing debug packages
A few mirrors currently distribute debug packages in accessible repositories. These are sponsored mirrors controlled by Arch Linux and are given access to the debug repositories.

* https://geo.mirror.pkgbuild.com (GeoDNS mirror)

To install a package you can install it directly from the repository. For example:

 # pacman -U https://geo.mirror.pkgbuild.com/core-debug/os/x86_64/zstd-debug-1.5.2-2-x86_64.pkg.tar.zst

Another option is to add the repositories to your pacman configuration.

Place a mirror with debug packages as the first one in the mirrorlist file:

## Rebuilding packages
If debug information is not exposed through debuginfod (for example, when the package originates from the AUR), then it can be rebuilt from source. See ABS for packages in the official repositories, or AUR#Acquire build files for packages in the AUR.

To set the required #Compilation options, you can modify the makepkg configuration if you will only use makepkg for debug purposes. In other cases, you should modify package's  file only for each package you would like to rebuild.

## Compilation options
As of pacman 4.1,  has debug compilation flags in  and . To use them, enable the  makepkg option, and disable .

These settings will force compilation with debug symbols and will disable their stripping from executables.

To apply this setting to a single package, modify the :

Alternatively you can put the debug information in a separate package by enabling both  and , debug symbols will then be stripped from the main package and placed, together with source files to aid in stepping through the debugger, in a separate  package. This is advantageous if the package contains very large binaries (e.g. over a GB with debug symbols included) as it might cause freezing and other strange, unwanted behavior occurring.

## glibc
Certain packages such as glibc are stripped regardless. Check the  for sections such as:

{{bc|
strip $STRIP_BINARIES usr/bin/{gencat,getconf,getent,iconv,iconvconfig} \
                      usr/bin/{ldconfig,locale,localedef,makedb} \
                      usr/bin/{pcprofiledump,pldd,rpcgen,sln,sprof} \
                      usr/lib/getconf/*

strip $STRIP_STATIC usr/lib/*.a

strip $STRIP_SHARED usr/lib/{libanl,libBrokenLocale,libcidn,libcrypt}-*.so \
                    usr/lib/libnss_{compat,db,dns,files,hesiod,nis,nisplus}-*.so \
                    usr/lib/{libdl,libm,libnsl,libresolv,librt,libutil}-*.so \
                    usr/lib/{libmemusage,libpcprofile,libSegFault}.so \
                    usr/lib/{audit,gconv}/*.so
}}

And remove them where appropriate.

## Clang
Packages using Clang as the compiler will not build with the  option due to the debug flag  not being handled (e.g. the previous [https://gitlab.archlinux.org/archlinux/packaging/packages/js78/-/blob/main/PKGBUILD js78 PKGBUILD).

Add the following at the top of the  function to only remove the flag for the affected package:

{{bc|1=
build() {
  CFLAGS=${CFLAGS/-fvar-tracking-assignments}
  CXXFLAGS=${CXXFLAGS/-fvar-tracking-assignments}
}}

## LTO
Using Link-time optimization (LTO) will, both during compiling and in a debugger, use more memory[https://pp.ipd.kit.edu/uploads/publikationen/weinreuter16bachelorarbeit.pdf#section.4.3Depending on the application, especially if it is a large one like Firefox or Qt, it might exceed the available memory. Build the application without LTO if this happens.

All packages in the official repositories are generally built with LTO.

## Building and installing the package
Build the package from source using  while in the 's directory. This could take some time:

 $ makepkg

Then install the built package:

 # pacman -U glibc-2.26-1-x86_64.pkg.tar.gz
