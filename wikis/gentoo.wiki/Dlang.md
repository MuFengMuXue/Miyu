**Resources**

[[]][Home](http://dlang.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/D_(programming_language) "wikipedia:D (programming language)")

[[]][[#d](ircs://irc.libera.chat/#d)] ([[webchat](https://web.libera.chat/#d)])

**The D programming language** is a multi-paradigm systems programming language.

## Contents

-   [[1] [Dlang overlay]](#Dlang_overlay)
    -   [[1.1] [Usage]](#Usage)
    -   [[1.2] [Executables paths]](#Executables_paths)
    -   [[1.3] [Configuration files]](#Configuration_files)
    -   [[1.4] [Imports]](#Imports)
    -   [[1.5] [Libraries]](#Libraries)
-   [[2] [Q & A]](#Q_.26_A)
    -   [[2.1] [Why are D libraries not installed in their default locations?]](#Why_are_D_libraries_not_installed_in_their_default_locations.3F)
    -   [[2.2] [Why is there a library directory for each version of each D compiler?]](#Why_is_there_a_library_directory_for_each_version_of_each_D_compiler.3F)
    -   [[2.3] [DMD depends on itself]](#DMD_depends_on_itself)
-   [[3] [Compilers]](#Compilers)
    -   [[3.1] [DMD]](#DMD)
    -   [[3.2] [GDC]](#GDC)
    -   [[3.3] [LDC]](#LDC)
    -   [[3.4] [Which compiler to use]](#Which_compiler_to_use)

## [Dlang overlay]

There is a long history of projects to bring a D compiler to Gentoo. There were ebuilds in the tree, several overlays and later some ebuilds in [Sunrise](https://wiki.gentoo.org/wiki/Sunrise "Sunrise"). Now the most current ebuilds can be found in the dlang overlay, which can be installed like this:

`root `[`#`]`emerge --ask --noreplace app-eselect/eselect-repository dev-vcs/git `

`root `[`#`]`eselect repository enable dlang `

`root `[`#`]`emerge --sync dlang`

This overlay aims to make parallel installation of D compilers easy. The current offerings are:

-   Installation of DMD, GDC and LDC in parallel
-   Customizable `CFLAGS` for each D compiler
-   GDC is integrated with GCC for the best compatibility
-   Slotted installation of previous D compiler versions
-   Shared library support when using DMD
-   Easily compile debug builds with DMD and release builds with LDC/GDC even when they depend on libraries like GtkD. (Note: This depends on availability of libraries in this repository.)

### [Usage]

The overlay supports linker and compiler flags, though some package build scripts may not be patched to use them (e.g. DMD). For D packages, the `LDFLAGS` variable is rewritten to match the D compilers linker prefix. For DMD, this is `-L` and for LDC, this is `-L=`. If you have not set up `LDFLAGS` in make.conf, the Gentoo default will be used, which is currently `-Wl,--as-needed -Wl,-O1`. Taking this example, in a compilation using DMD this would be rewritten to `LDFLAGS=-L--as-needed -L-O1`.

Compiler flags on the other hand are commonly passed into build scripts as `DCFLAGS`, but since there is no common command-line syntax for all D compilers they are split up into `DMDFLAGS`, `GDCFLAGS`, and `LDCFLAGS` respectively in [/etc/portage/make.conf]. An example configuration could be:

[CODE] **Setting D compiler flags in /etc/portage/make.conf**

    DMDFLAGS="-O"
    GDCFLAGS="-march=native -O3 -pipe -frelease"
    LDCFLAGS="-O4 -release"

You may experiment with `-ffunction-sections`, `-fdata-sections` and the corresponding linker flag `--gc-sections`, but this caused broken exception handling in the past.

When you install libraries, no compilers will be selected to work with. Please run [emerge -pv \<lib\>] to list available compiler use flags for a library and use [/etc/portage/package.use] to activate them. A note about compilation times: Most build tools compile one module at a time, which causes a considerable overhead in compile times compared to passing multiple modules to the compiler at once. The use of several compilers in several versions and multilib installs all multiply the compile times. GtkD with no optional features compiled for \*one\* version of DMD, GDC and LDC took me 1 hour 10 minutes on a dual core 2 GHz notebook.

### [Executables paths]

-   DMD: [/opt/dmd-\<version\>/bin/dmd]
-   GDC: [/usr/\<abi\>-pc-linux-gnu/gcc-bin/\<version\>/gdc]
-   LDC: [/opt/ldc2-\<version\>/bin/ldc2]

An eselect script will create symlinks to these executables, so they can be called by their original names with the exception of GDC which is managed by [gcc-config].

### [Configuration files]

For DMD the configuration files lie side-by-side with the executable, to allow different path setups for each installation.

### [Imports]

-   DMD: [/opt/dmd-\<version\>/import]
-   GDC: [/usr/include/d/\<version\>]
-   LDC: [/opt/ldc2-\<version\>/include/d]

### [Libraries]

Dynamic and static libraries are installed into:

-   DMD: [/opt/dmd-\<version\>/lib]
-   GDC: [/usr/lib/gcc/\<abi\>-pc-linux-gnu/\<version\>\[/32\]]
-   LDC: [/opt/ldc2-\<version\>/lib]

Include files should be placed in [/usr/include/dlang/\<library\>].

## [][Q & A]

### [][Why are D libraries not installed in their default locations?]

D compilers have ABIs that are incompatible with each other. This means either sticking to one compiler for anything D, or to change the default location and allow for one installation per compiler. Since the author\'s motivation was to use dmd for debug builds and one of the others for releases, he chose the second option. He could have just added prefixes or suffixes to the library names, but that means build scripts need to be aware of this change. Giving each compiler eco system its own library directory and seting up the path in the compiler should ideally allow us to build a D program with any compiler and link to libraries with no further configuration change.

### [][Why is there a library directory for each version of each D compiler?]

It might seem overkill at first, but we have no guarantee about D ABI stability at this point. Libraries compiled with 2.064 might not work with libraries compiled with 2.065. To be on the safe side, I decided to separate D specifications the same way as compilers.

### [DMD depends on itself]

Since version 2.069, DMD is a self-hosting compiler and requires another D compiler to build. The use flags provide the list of choices for that and include the version about to be installed. This creates a dependency on itself, but the option is there if you want to recompile the latest compiler with itself **after** the initial installation. USE flags are not meant to added dynamically based on installed packages.

## [Compilers]

At the time of writing, there are three major compilers for D that share the front-end but use a different back-end to generate the code. There is also work going on to port this front-end from C++ to D as well as attempts to implement a D compiler from scratch from the language specifications. As these are still unstable, we will focus on the three major players.

### [DMD]

Digital Mars D is the original language implementation based off a C++ compiler. It is where the main language development happens and acts as the reference compiler. It is known for its fast compile times, which help a lot during development. The back-end optimizations are not state of the art anymore, though.

-   [GitHub: DMD source code](https://github.com/D-Programming-Language/dmd)

### [GDC]

The GDC project attaches the D front-end to GCC as an additional language, so it can use the advanced back-end optimizations and the wide spread of GCC as the standard compiler.

### [LDC]

LDC uses the younger LLVM back-end, which is not as wide spread as GCC, but was written as a reusable library making front-end and back-end more modular.

### [Which compiler to use]

DMD is a clear favorite when you want the absolute latest version or compilation speed is important and you can limit yourself to x86/amd64. GDC and LDC on the other hand can more easily support other architectures and their code optimizers are now pretty much on the same high level. If in doubt and you are on x86/amd64, start with DMD since it is the official reference compiler and very fast to compile and install.

For a more detailed overview of the three compilers, take a look at the [Dlang Wiki](http://wiki.dlang.org/Compilers)