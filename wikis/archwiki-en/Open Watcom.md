# Open Watcom

Open Watcom is a Fortran/C/C++' compiler with many cross-compilation targets. Those old enough most likely fondly remember old DOS games ending with the DOS4GW extender, where the "W" stands for "watcom". In general it was a very popular compiler for high-end games at the time for producing very efficient binaries in memory-constrained environments (like DOS). Watcom lives on as Open Watcom, with an official release at version 1.9 and an unofficial fork at version 2.0.

## Installation
The unofficial 2.0 release can be installed with the  package.

## Wmake
Open Watcom comes with its own make utility (wmake). On Windows and Linux hosts, CMake supports generating wmake files. OW tools usage with CMake is describing how to generate wmake files for cross compilation with CMake on Linux or Windows.

## Using the Open Watcom package in Wine
The  package includes executables for all supported host platforms by default. This can be quite handy sometimes if one for example wants to debug a cross-compiled binary using the watcom debugger wd. In principle, the same could be done also with DOS emulators for example.
Steps to set up a WINEPREFIX to use the already existing Watcom install:
* create a fresh WINEPREFIX (for example $HOME/.watcom) by WINEPREFIX=$HOME/.watcom winecfg
* cd to $WINEPREFIX/drive_c and make a symlink to /opt/watcom named watcom (ln -s /opt/watcom watcom)
* run regedit
* under HKEY_CURRENT_USER/Environment , add the following string variables
* WATCOM = C:\WATCOM
* PATH = C:\WATCOM\BINNT
* EDPATH = C:\WATCOM\EDDAT
* WIPFC = C:\WATCOM\WIPFC

## Compilers
Open Watcom comes with a very efficient native 16-bit compiler supporting DOS and Win16 targets and a 32-bit x86 compiler targeting many different OSes (NT/Win32, OS/2, NetWare, Linux, ...). There is also experimental support for PowerPC, Alpha AXP, MIPS and SPARC architectures. A major aim for the v2 development is support for x86_64 and ARM architectures. The two most obvious "competitors" of Open Watcom would be the GCC-based MinGW (for Win32-targets) and DJGPP (for DOS targets).

## 16-bit x86 compilers
The 16-bit x86 compilers finds its OS-independent libraries in the  directory and its OS-dependent libraries in {{ic|1=$WATCOM/lib286/${target_os}}} sub-directory.
Some OSes might need extra library paths, which can be added by the  environment variable.

* : the 16-bit "compile only" C compiler
* : the 16-bit "compile only" C++ compiler
* : the 16-bit "compile and link" utility for C/C++
* : the 16-bit "compile only" Fortran compiler
* : the 16-bit "compile and link" utility for Fortran
* : the POSIX compatible "compile and link" utility. Set CC=owcc in a project depending on GNU makefiles.

## 32-bit x86 compilers
The 32-bit x86 compilers finds its OS-independent libraries in the  directory and its OS-dependent libraries in {{ic|1=$WATCOM/lib386/${target_os}}} sub-directory.
Some OSes might need extra library paths, which can be added by the  environment variable.

* : the 32-bit "compile only" C compiler
* : the 32-bit "compile only" C++ compiler
* : the 32-bit "compile and link" utility for C/C++
* : the 32-bit "compile only" Fortran compiler
* : the 32-bit "compile and link" utility for Fortran
*  : the POSIX compatible "compile and link" utility. Set CC=owcc in a project depending on GNU makefiles.

## Comparisons to other (cross-) compilers
A striking difference compared to the -based compilers (, ) when used as a cross compiler is that Open watcom only uses a single compiler (one for each target CPU architecture) and the target OS is determined by a compilation flag (see "cross compiling" below). Further, many OS-independent libraries lives in a generic architecture-specific location ($WATCOM/lib286 and $WATCOM/lib386) and only libraries with OS-specific features are put into OS-specific sub-directories - this is thanks to the Open Watcom C runtime that is distributed together with the compiler. This means that it is very easy to use a single install of Open Watcom as a cross compiler for a wide range of OSes. In contrast, a cross-compile toolchain based on binutils typically requires building a target-specific "trinity" of binutils, compiler and libc. Another advantage of Open Watcom as a Win32 cross compiler is that the resulting binaries and libraries integrate nicely with the target OS. For example, Python compiled with Open Watcom can load plugins compiled with MSVC. This is similar to how the different binutils-based compilers (often) can use libraries built with another binutils-based compiler. At this moment, the resulting binaries are not as optimized as those made by GCC.

## Compiler optimization flags and other options
The Watcom compilers do not follow the same standard as GCC for flags (for example, it will not understand -O3 by default). It has a rich set of options to define target architecture, optimizations and other things.

## (Cross-) compilation : Common settings
To cross compile, set the correct environment variables and a compile flag telling the compiler which target is intended.
Without compile flags defining target, a native build is assumed.

Common for all targets:

 export WATCOM=/opt/watcom
 export PATH=$WATCOM/binl:$PATH
 export EDPATH=$WATCOM/eddat
 export WIPFC=$WATCOM/wipfc

A small overview of all build targets can be found here.

## Linux
for C, use compilers: ,  or
add  for wcc386 or  for wcl386 or  for owcc. Flags not absolutely needed since the compiler assumes a native build if nothing else is added.

## DOS (16-bit)
add  for wcc or  for wcl or  for owcc

## DOS (32-bit DOS4GW Extender)
add  for wcc386 or  for wcl386 or  for owcc

## WIN16
add  for wcc or  for wcl or  for owcc

## WIN32
add  for wcc386 or  for wcl386 or  for owcc

## OS/2 (16-bit)
add  for wcc or  for wcl or  for owcc

 export INCLUDE=$WATCOM/h:$WATCOM/h/os21x
 export LIBPATH=$WATCOM/binp/dll:$LIBPATH

## OS/2 (32-bit)
add  for wcc386 or  for wcl386 or  for owcc

 export INCLUDE=$WATCOM/h:$WATCOM/h/os2
 export LIBPATH=$WATCOM/binp/dll:$LIBPATH

## Netware
add  for wcc386 or  for wcl386 or  for owcc

 export INCLUDE=$WATCOM/h:$WATCOM/novh
 export LIBPATH=$WATCOM/nlm:$LIBPATH

Some packages may need a proprietary set of libraries and headers from Novell, which can be downloaded on the Micro Focus website

## QNX
The Watcom compiler also supports QNX as a target, but since the libraries were not redistributable with the open source Open Watcom distribution, it has not been well-tested ever since. In theory, it might be possible to still compile for QNX if a C library is built for Watcom

## Packaged third-party libraries and utilities
The packaging should conform to the MinGW packaging guidelines, but with the difference that they are packaged as much as possible as split packages. One exception to the split package aim is when one target has unique (or proprietary) build dependencies. Pre-packaged libraries and compiler front ends are meant to make it easy for someone to start using the cross compiler. Below are some resources packaged for Arch linux:

## Extra languages
One area where GCC is stronger than Open Watcom is language support. To mitigate this, some source-to-source compilers can be built on/for Watcom.
