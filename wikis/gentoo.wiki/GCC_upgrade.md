**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Toolchain "Project:Toolchain")][Project](https://wiki.gentoo.org/wiki/Project:Toolchain "Project:Toolchain")

[[]][Home](https://gcc.gnu.org/)

[[]][Official documentation](https://gcc.gnu.org/onlinedocs/)

[[]][Package information](https://packages.gentoo.org/packages/sys-devel/gcc)

[[]][Wikipedia](https://en.wikipedia.org/wiki/GNU_Compiler_Collection "wikipedia:GNU Compiler Collection")

[[]][GitWeb](https://gcc.gnu.org/cgit/gcc/)

[[]][GitHub (mirror)](https://github.com/gcc-mirror/gcc)

[[]][Official project wiki](https://gcc.gnu.org/wiki)

[[]][Bugs (upstream)](https://gcc.gnu.org/bugzilla/)

[[]][[#gcc](ircs://irc.libera.chat/#gcc)] ([[webchat](https://web.libera.chat/#gcc)])

**GCC** or the **GNU Compiler Collection** is among the most widely used compiler toolchains in the world with official support for: [C](https://wiki.gentoo.org/wiki/C "C"), [C++](https://wiki.gentoo.org/wiki/C%2B%2B "C++"), [Objective-C](https://en.wikipedia.org/wiki/Objective-C "wikipedia:Objective-C"), [Objective-C++](https://en.wikipedia.org/wiki/Objective-C%2B%2B "wikipedia:Objective-C++"), [Modula-2](https://en.wikipedia.org/wiki/Modula-2 "wikipedia:Modula-2"), [Fortran](https://wiki.gentoo.org/wiki/Fortran "Fortran"), [Ada](https://wiki.gentoo.org/wiki/Ada "Ada"), [Go](https://wiki.gentoo.org/wiki/Go "Go"), [COBOL](https://en.wikipedia.org/wiki/COBOL "wikipedia:COBOL"), and [D](https://en.wikipedia.org/wiki/D_(programming_language) "wikipedia:D (programming language)"). Third-party front ends exist for the [Pascal](https://en.wikipedia.org/wiki/Pascal_(programming_language) "wikipedia:Pascal (programming language)"), [Modula-3](https://en.wikipedia.org/wiki/Modula-3 "wikipedia:Modula-3"), and [VHDL](https://en.wikipedia.org/wiki/VHDL "wikipedia:VHDL") programming languages.^[\[1\]](#cite_note-1)^

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Invocation]](#Invocation)
-   [[2] [Upgrading]](#Upgrading)
    -   [[2.1] [Quick guide to GCC upgrades]](#Quick_guide_to_GCC_upgrades)
    -   [[2.2] [Extended guide to GCC upgrades]](#Extended_guide_to_GCC_upgrades)
        -   [[2.2.1] [libtool]](#libtool)
        -   [[2.2.2] [ABI changes]](#ABI_changes)
            -   [[2.2.2.1] [Before GCC 5.1]](#Before_GCC_5.1)
            -   [[2.2.2.2] [The special case C++11 (and C++14)]](#The_special_case_C.2B.2B11_.28and_C.2B.2B14.29)
            -   [[2.2.2.3] [Downgrading GCC]](#Downgrading_GCC)
    -   [[2.3] [Which packages are known to need a rebuild?]](#Which_packages_are_known_to_need_a_rebuild.3F)
    -   [[2.4] [Rebuilding everything]](#Rebuilding_everything)
-   [[3] [Configuration]](#Configuration)
-   [[4] [Debugging]](#Debugging)
    -   [[4.1] [ICE Reporting Guide]](#ICE_Reporting_Guide)
-   [[5] [Tips]](#Tips)
    -   [[5.1] [Skip stage 1 build]](#Skip_stage_1_build)
-   [[6] [Writing a GCC Frontend]](#Writing_a_GCC_Frontend)
-   [[7] [Troubleshooting]](#Troubleshooting)
    -   [[7.1] [Rebuild of Boost]](#Rebuild_of_Boost)
    -   [[7.2] [libstdc++.so.6: version \`GLIBCXX_3.4.15\' not found]](#libstdc.2B.2B.so.6:_version_.60GLIBCXX_3.4.15.27_not_found)
    -   [[7.3] [undefined reference to \`\_\_cxa_call_terminate@CXXABI_1.3.15\']](#undefined_reference_to_.60_cxa_call_terminate.40CXXABI_1.3.15.27)
-   [[8] [See also]](#See_also)
-   [[9] [External resources]](#External_resources)
-   [[10] [References]](#References)

## [[] Installation]

### [[] USE flags]

### [USE flags for] [sys-devel/gcc](https://packages.gentoo.org/packages/sys-devel/gcc) [[]] [The GNU Compiler Collection]

  --------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+cxx`](https://packages.gentoo.org/useflags/+cxx)                                                       Build support for C++ (bindings, extra libraries, code generation, \...)
  [`+fortran`](https://packages.gentoo.org/useflags/+fortran)                                               Add support for fortran
  [`+nls`](https://packages.gentoo.org/useflags/+nls)                                                       Add Native Language Support (using gettext - GNU locale utilities)
  [`+openmp`](https://packages.gentoo.org/useflags/+openmp)                                                 Build support for the OpenMP (support parallel computing), requires \>=sys-devel/gcc-4.2 built with USE=\"openmp\"
  [`+pie`](https://packages.gentoo.org/useflags/+pie)                                                       Build programs as Position Independent Executables (a security hardening technique)
  [`+sanitize`](https://packages.gentoo.org/useflags/+sanitize)                                             Build support for various sanitizer functions (ASAN/TSAN/etc\...) to find runtime problems in applications.
  [`+ssp`](https://packages.gentoo.org/useflags/+ssp)                                                       Build packages with stack smashing protection on by default
  [`ada`](https://packages.gentoo.org/useflags/ada)                                                         Build the Ada language (GNAT) frontend
  [`algol68`](https://packages.gentoo.org/useflags/algol68)                                                 Build the Algol 68 frontend
  [`cet`](https://packages.gentoo.org/useflags/cet)                                                         Enable support for control flow hijacking protection. On amd64, this provides Intel Control Flow Enforcement Technology (CET). On arm64, this provides Branch Target Identification (BTI) and Pointer Authentication Code (PAC) support. This is only effective on amd64 or arm64. Only provides benefits on newer CPUs. For Intel, the CPU must be at least as new as Tiger Lake. For AMD, it must be at least as new as Zen 3. This is harmless on older CPUs, but provides no benefit either. For ARM64, PAC was introduced in armv8.3-a, and BTI was introduced in armv8.5-a. When combined with USE=hardened on amd64, GCC will set -fcf-protection by default when building software. The effect is minimal on systems which do not support it, other than a possible small increase in codesize for the NOPs. The generated code is therefore compatible with i686 at the earliest. On arm64, GCC will set -mbranch-protection=standard by default when building software.
  [`cobol`](https://packages.gentoo.org/useflags/cobol)                                                     Enable support for the COBOL programming language
  [`custom-cflags`](https://packages.gentoo.org/useflags/custom-cflags)                                     Build with user-specified CFLAGS (unsupported)
  [`d`](https://packages.gentoo.org/useflags/d)                                                             Enable support for the D programming language
  [`debug`](https://packages.gentoo.org/useflags/debug)                                                     Enables GCC\'s \'checking\' (assertions) facility. For released GCCs: \* USE=debug sets \--enable-checking=yes,extra,rtl \* USE=-debug sets \--enable-checking=release For unreleased GCCs: \* USE=debug sets \--enable-checking=yes,extra,rtl \* USE=-debug sets \--enable-checking=yes,extra This adds checks to various compiler passes for integrity and input validation. This can help catch possible miscompilations early as well as latent bugs which could become real problems in future, but at the cost of slower compile times when using GCC. Unrelated to backtraces.
  [`default-stack-clash-protection`](https://packages.gentoo.org/useflags/default-stack-clash-protection)   Build packages with stack clash protection on by default as a hardening measure. This enables -fstack-clash-protection by default which protects against large memory allocations allowing stack smashing. May cause slightly increased codesize, but modern compilers have been adapted to optimize well for this case, as this mitigation is now quite common. See https://developers.redhat.com/blog/2020/05/22/stack-clash-mitigation-in-gcc-part-3 and https://www.qualys.com/2017/06/19/stack-clash/stack-clash.txt.
  [`default-znow`](https://packages.gentoo.org/useflags/default-znow)                                       Request full relocation on start from ld.so by default. This sets the -z,now (BIND_NOW) flag by default on all linker invocations. By resolving all dynamic symbols at application startup, parts of the program can be made read-only as a hardening measure. This is closely related to RELRO which is also separately enabled by default. In some applications with many unresolved symbols (heavily plugin based, for example), startup time may be impacted.
  [`doc`](https://packages.gentoo.org/useflags/doc)                                                         Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`fixed-point`](https://packages.gentoo.org/useflags/fixed-point)                                         Enable fixed-point arithmetic support for MIPS targets in gcc (Warning: significantly increases compile time!)
  [`go`](https://packages.gentoo.org/useflags/go)                                                           Build the GCC Go language frontend.
  [`graphite`](https://packages.gentoo.org/useflags/graphite)                                               Add support for the framework for loop optimizations based on a polyhedral intermediate representation
  [`hardened`](https://packages.gentoo.org/useflags/hardened)                                               Activate default security enhancements for toolchain (gcc, glibc, binutils)
  [`ieee-long-double`](https://packages.gentoo.org/useflags/ieee-long-double)                               Use accelerated 128-bit IEEE long double ABI (ppc64le only)
  [`jit`](https://packages.gentoo.org/useflags/jit)                                                         Enable libgccjit so other applications can embed gcc for Just-In-Time compilation.
  [`libgdiagnostics`](https://packages.gentoo.org/useflags/libgdiagnostics)                                 Provide libgdiagnostics (https://gcc.gnu.org/wiki/libgdiagnostics). This also installs the \'sarif-replay\' tool.
  [`libssp`](https://packages.gentoo.org/useflags/libssp)                                                   Build SSP support into a dedicated library rather than use the code in the C library (DO NOT ENABLE THIS IF YOU DON\'T KNOW WHAT IT DOES)
  [`lto`](https://packages.gentoo.org/useflags/lto)                                                         Build using Link Time Optimizations (LTO). Note that GCC is always built with support for building other programs with LTO. This USE flag is for whether GCC itself is built and optimized with LTO.
  [`modula2`](https://packages.gentoo.org/useflags/modula2)                                                 Build the GCC Modula-2 language frontend.
  [`multilib`](https://packages.gentoo.org/useflags/multilib)                                               On 64bit systems, if you want to be able to compile 32bit and 64bit binaries
  [`objc`](https://packages.gentoo.org/useflags/objc)                                                       Build support for the Objective C code language
  [`objc++`](https://packages.gentoo.org/useflags/objc++)                                                   Build support for the Objective C++ language
  [`objc-gc`](https://packages.gentoo.org/useflags/objc-gc)                                                 Build support for the Objective C code language Garbage Collector
  [`pch`](https://packages.gentoo.org/useflags/pch)                                                         Enable precompiled header support for faster compilation at the expense of disk space and memory
  [`pgo`](https://packages.gentoo.org/useflags/pgo)                                                         Build GCC using Profile Guided Optimization (PGO). GCC will build itself and then analyze the just-built binary and then rebuild itself using the data obtained from analysis of codepaths taken. It does not affect whether GCC itself supports PGO when building other software. This substantially increases the build time needed for building GCC itself.
  [`rust`](https://packages.gentoo.org/useflags/rust)                                                       Build support for the Rust language, installs gccrs.
  [`systemtap`](https://packages.gentoo.org/useflags/systemtap)                                             Enable enhanced debugging hooks/interface via SystemTap static probe points in libgcc and libstdc++. Note that this isn\'t exclusive to SystemTap, despite the name. This provides an interface which dev-debug/gdb optionally uses, see https://sourceware.org/gdb/wiki/LinkerInterface and https://sourceware.org/gdb/wiki/DistroAdvice#sys.2Fsdt.h_probes.
  [`test`](https://packages.gentoo.org/useflags/test)                                                       Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`time64`](https://packages.gentoo.org/useflags/time64)                                                   Use 64-bit time_t type instead of the regular 32-bit type. This flag is forced on time64 profiles, and masked elsewhere. It should be only used when detection of type width is not possible (e.g. for SRC_URI)
  [`valgrind`](https://packages.gentoo.org/useflags/valgrind)                                               Enable annotations for accuracy. May slow down runtime slightly. Safe to use even if not currently using dev-debug/valgrind
  [`vanilla`](https://packages.gentoo.org/useflags/vanilla)                                                 Do not add extra patches which change default behaviour; DO NOT USE THIS ON A GLOBAL SCALE as the severity of the meaning changes drastically
  [`vtv`](https://packages.gentoo.org/useflags/vtv)                                                         Build support for virtual table verification (a C++ hardening feature). This does not control whether GCC defaults to using VTV\> Note that actually using VTV breaks ABI and hence the whole system must be built with -fvtable-verify.
  [`zstd`](https://packages.gentoo.org/useflags/zstd)                                                       Enable support for ZSTD compression
  --------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-24 23:11] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

The [[[graphite]](https://packages.gentoo.org/useflags/graphite)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") is needed for the `-ftree-loop-optimize`, `-fgraphite-identity`, `-floop-nest-optimize`, and `-floop-parallelize-all` options. ^[\[2\]](#cite_note-2)^

### [[] Emerge]

Since [[[sys-devel/gcc]](https://packages.gentoo.org/packages/sys-devel/gcc)[]] is installed by default, it does not need to be installed manually. If for some reason it needs to be reinstalled, for example due to [USE flag](#USE_flags) change, the following command should be used.

`root `[`#`]`emerge --ask --oneshot sys-devel/gcc`

** Note**\
`--oneshot` is used in the above command because [[[sys-devel/gcc]](https://packages.gentoo.org/packages/sys-devel/gcc)[]] is included in the [system set](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)"), so it should not be added to the [selected set](https://wiki.gentoo.org/wiki/Selected_set_(Portage) "Selected set (Portage)") ([/var/lib/portage/world] file).

### [[] Invocation]

`user `[`$`]`gcc --help`

    Usage: gcc [options] file...
    Options:
      -pass-exit-codes         Exit with highest error code from a phase.
      --help                   Display this information.
      --target-help            Display target specific command line options (including assembler and linker options).
      --help=[,...].
                               Display specific types of command line options.
      (Use '-v --help' to display command line options of sub-processes).
      --version                Display compiler version information.
      -dumpspecs               Display all of the built in spec strings.
      -dumpversion             Display the version of the compiler.
      -dumpmachine             Display the compiler's target processor.
      -foffload=<targets>      Specify offloading targets.
      -print-search-dirs       Display the directories in the compiler's search path.
      -print-libgcc-file-name  Display the name of the compiler's companion library.
      -print-file-name=<lib>   Display the full path to library <lib>.
      -print-prog-name=  Display the full path to compiler component .
      -print-multiarch         Display the target's normalized GNU triplet, used as
                               a component in the library path.
      -print-multi-directory   Display the root directory for versions of libgcc.
      -print-multi-lib         Display the mapping between command line options and
                               multiple library search directories.
      -print-multi-os-directory Display the relative path to OS libraries.
      -print-sysroot           Display the target libraries directory.
      -print-sysroot-headers-suffix Display the sysroot suffix used to find headers.
      -Wa,<options>            Pass comma-separated <options> on to the assembler.
      -Wp,<options>            Pass comma-separated <options> on to the preprocessor.
      -Wl,<options>            Pass comma-separated <options> on to the linker.
      -Xassembler <arg>        Pass <arg> on to the assembler.
      -Xpreprocessor <arg>     Pass <arg> on to the preprocessor.
      -Xlinker <arg>           Pass <arg> on to the linker.
      -save-temps              Do not delete intermediate files.
      -save-temps=<arg>        Do not delete intermediate files.
      -no-canonical-prefixes   Do not canonicalize paths when building relative
                               prefixes to other gcc components.
      -pipe                    Use pipes rather than intermediate files.
      -time                    Time the execution of each subprocess.
      -specs=<file>            Override built-in specs with the contents of <file>.
      -std=<standard>          Assume that the input sources are for <standard>.
      --sysroot=<directory>    Use <directory> as the root directory for headers
                               and libraries.
      -B <directory>           Add <directory> to the compiler's search paths.
      -v                       Display the programs invoked by the compiler.
      -###                     Like -v but options quoted and commands not executed.
      -E                       Preprocess only; do not compile, assemble or link.
      -S                       Compile only; do not assemble or link.
      -c                       Compile and assemble, but do not link.
      -o <file>                Place the output into <file>.
      -pie                     Create a dynamically linked position independent
                               executable.
      -shared                  Create a shared library.
      -x <language>            Specify the language of the following input files.
                               Permissible languages include: c c++ assembler none
                               'none' means revert to the default behavior of
                               guessing the language based on the file's extension.

    Options starting with -g, -f, -m, -O, -W, or --param are automatically
     passed on to the various sub-processes invoked by gcc.  In order to pass
     other options on to these processes the -W<letter> options must be used.

    For bug reporting instructions, please see:
    <https://bugs.gentoo.org/>.

## [Upgrading]

GCC upgrades should generally be handled gracefully with [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") and the usual Gentoo tools, [see next section](https://wiki.gentoo.org/wiki/GCC#Quick_guide_to_GCC_upgrades "GCC"). If ever there are more involved updates that require user intervention, they should be accompanied by a corresponding [news item](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Reading_news_items "Handbook:AMD64/Installation/Base"), that should be read and followed.

*Downgrading* GCC might have unwanted side effects. Refer to the [troubleshooting section](https://wiki.gentoo.org/wiki/GCC#Troubleshooting "GCC") for some commonly reported issues.

### [[] Quick guide to GCC upgrades]

Most GCC upgrades are as simple as switching the compiler version (here from 10.3.0 to 11.2.0) and rebuilding [[[dev-build/libtool]](https://packages.gentoo.org/packages/dev-build/libtool)[]]:

`root `[`#`]`emerge --ask --oneshot sys-devel/gcc`

`root `[`#`]`gcc-config --list-profiles`

    [1] x86_64-pc-linux-gnu-10.3.0 *
    [2] x86_64-pc-linux-gnu-11.2.0

`root `[`#`]`gcc-config 2 `

`root `[`#`]`source /etc/profile `

`root `[`#`]`emerge --ask --oneshot --usepkg=n dev-build/libtool`

Check the current version number and then uninstall the old version:

`root `[`#`]`gcc --version`

`root `[`#`]`emerge --ask --depclean sys-devel/gcc:10.3.0`

Enjoy the new compiler!

### [Extended guide to GCC upgrades]

GCC upgrading has always been mystified, with suggestions ranging from \"users do not need to do anything\" to \"users will need to rebuild the entire system twice\". The uncertainty was caused by confusion about ABI incompatibility, something that nowadays rarely causes problems.

#### [libtool]

The reason we need to rebuild libtool after the upgrade of [gcc] versions is because of its main purpose: *libtool* is a toolset that aggregates platform-specific code in a generic interface, allowing applications to build against shared libraries without needing to deal with the platform-specific aspects of shared libraries. To fulfill its function properly, the [libtool] script uses various library locations that have hard-coded [gcc] version information in them.

See [[[bug #88596]](https://bugs.gentoo.org/show_bug.cgi?id=88596)[]].

#### [ABI changes]

##### [Before GCC 5.1]

An ABI ([Application Binary Interface](https://en.wikipedia.org/wiki/Application_binary_interface "wikipedia:Application binary interface")), is a set of conventions used by all tools that deal with binary representation of programs, including compilers, assemblers, linkers, and language runtime support (source: [GCC Binary Compatibility](https://gcc.gnu.org/onlinedocs/gcc/Compatibility.html)). When the ABI used for binary applications and libraries is changed, there is a risk getting linker errors or malfunctioning programs unless all libraries using C++ code are rebuilt.

When upgrading to GCC 4.1, or GCC 5.1, it is likely to encounter ABI issues. To prevent this, the [revdep-rebuild] command should be run against the [libstdc++.so.5] library when moving from GCC 3 to GCC 4.1, or [libstdc++.so.6] when moving from GCC 4 to GCC 5.1.

`root `[`#`]`revdep-rebuild --library 'libstdc++.so.6' -- --exclude gcc`

This is only needed till GCC 4.1/5.1 because from that version onward, GCC uses a forward-compatible ABI, which removes the need for rebuilding applications and libraries. Of course, guarantees can never be given indefinitely, but when an incompatibility occurs again, we\'ll definitely document it here and release a news item. In that case, the version of the [libstdc++.so] library will probably be increased.

##### [][The special case C++11 (and C++14)]

While GCC (or more specifically, libstdc++) goes to great lengths to guarantee stability of the ABI, this guarantee does not extend to all parts of C++ within libstdc++. Formally, with versions starting from 3.4, GCC/libstdc++ only guarantees C++98/C++03 ABI stability and not more. This is crucial for packages that depend on C++11. GCC only makes C++11 ABI stability guarantees beginning with version 5.1. This means that switching (even minor) versions of gcc (say from 4.7.3 -\> 4.7.4) might cause ABI breakage for binaries built from C++11 code.

For more information and some examples, see:

-   [[[bug #513386]](https://bugs.gentoo.org/show_bug.cgi?id=513386)[]]
-   [https://gcc.gnu.org/bugzilla/show_bug.cgi?id=61758](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=61758)
-   [https://blogs.gentoo.org/blueness/2015/03/10/the-c11-abi-incompatibility-problem-in-gentoo/](https://blogs.gentoo.org/blueness/2015/03/10/the-c11-abi-incompatibility-problem-in-gentoo/)
-   [https://stackoverflow.com/questions/16190269/g-always-backward-compatible-with-older-static-libraries/16196475#16196475](https://stackoverflow.com/questions/16190269/g-always-backward-compatible-with-older-static-libraries/16196475#16196475)

##### [[] Downgrading GCC]

For the aforementioned reasons, if downgrading GCC or choosing an older slot with [gcc-config], it is necessary to run [revdep-rebuild] to catch `libstdc++` consumers requiring newer symbols:

`root `[`#`]`revdep-rebuild --library 'libstdc++.so.6' -- --exclude gcc`

### [][Which packages are known to need a rebuild?]

The following table gives the packages that, *if installed*, need to be rebuilt and why.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Package                                                                                                                                                                                                                                                                                                                                                                     Rebuild needed because \...
  [[[dev-build/libtool]](https://packages.gentoo.org/packages/dev-build/libtool)[]]   libtool has hardcoded paths towards GCC internal libraries, see [[[bug #88596]](https://bugs.gentoo.org/show_bug.cgi?id=88596)[]].
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`root `[`#`]`emerge --ask --oneshot --usepkg=n --verbose dev-build/libtool`

Some collections of packages need to be built with the same compiler (for example, the various [qt-\*] packages). Such packages are usually bumped by package maintainers simultaneously, so they will always be built with the same GCC version. Cherry-picking re-installs on these packages might prove to be troublesome.

### [Rebuilding everything]

** Tip**\
This isn\'t necessary but is described here so people know how to do it thoroughly if they desire.

Some people swear that they need to rebuild every single package on their system when a new GCC version is made available. Of course, that doesn\'t make sense, since there are many applications that are not using GCC for their build and install process anyhow, so they would never be affected by such changes.

That, however, doesn\'t mean they are completely incorrect: newer GCC versions often include better support for the processors\' instruction set, which might influence the performance of some applications in a positive way.

Apart from such \"benign\" benefits, rebuilding everything from scratch may be necessary in some cases to fix problems that don\'t seem to have any obvious cause.

Some software problems are inherently difficult to diagnose and yet could be solved by simply rebuilding one or more appropriate packages. If such a problem has arisen following a GCC upgrade and persists after using the revdep-rebuild approach described above (and after rebuilding any other obviously relevant packages), a complete system rebuild may be the answer.

The \"safest\" but slowest way to accomplish this is to use the `--emptytree` (`-e`) option of emerge to rebuild the [system set](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)") and then the [world set](https://wiki.gentoo.org/wiki/World_set_(Portage) "World set (Portage)"):

`root `[`#`]`emerge --ask --emptytree --usepkg=n @system`

`root `[`#`]`emerge --ask --emptytree --usepkg=n @world`

Try this approach before reporting bugs that might have been caused by a GCC upgrade.

** Note**\
The commands above will cause the packages in the system set to be rebuilt twice, which is necessary to be *absolutely certain* that every package gets built in the same presumably \"problem-free\" environment. Any problems that remain after doing this are due to either \"genuine bugs\" that should be reported or poor system configuration.

## [Configuration]

Refer to [GCC optimization](https://wiki.gentoo.org/wiki/GCC_optimization "GCC optimization").

## [Debugging]

### [ICE Reporting Guide]

Refer to [ICE Reporting Guide](https://wiki.gentoo.org/wiki/GCC/ICE_Reporting_Guide "GCC/ICE Reporting Guide").

## [Tips]

### [Skip stage 1 build]

** Warning**\
This is **unsupported** and can **break** the system so this should not be used lightly. Refer to [[[bug #705406]](https://bugs.gentoo.org/show_bug.cgi?id=705406)[]] for more info.

It is possible to skip building stage 1 in the 3 stage build process by adding [EXTRA_ECONF=\"\--disable-bootstrap\"] via [[/etc/portage/package.env](https://wiki.gentoo.org/wiki//etc/portage/package.env "/etc/portage/package.env")].

## [Writing a GCC Frontend]

See this [link](https://wiki.gentoo.org/wiki/GCC/Frontend "GCC/Frontend").

## [[] Troubleshooting]

### [Rebuild of Boost]

If [[[dev-libs/boost]](https://packages.gentoo.org/packages/dev-libs/boost)[]] needs to be rebuilt, one will get the following error message:

`root `[`#`]`emerge ... `

    checking for the Boost _____ library... no
    configure: error: cannot find the flags to link with Boost _____

One can rebuild with:

`root `[`#`]`emerge --ask --oneshot --usepkg=n --verbose dev-libs/boost`

### [][libstdc++.so.6: version \`GLIBCXX_3.4.15\' not found]

During updates, it\'s possible to encounter an error like the following:

[CODE] **GLIBCXX_x.y.z not found**

    cmake_bootstrap_28021_test: /usr/lib/gcc/i486-pc-linux-gnu/4.1.2/libstdc++.so.6:
    version `GLIBCXX_3.4.11' not found

This implies an attempt to build a package with an *older* GCC version than that with which some depending libraries were built. The C++ ABI is forward-compatible, but it ensures only that *higher* (or same) GCC versions can be used when building applications and linking libraries (compared to the GCC version used to build those libraries).

To rebuild all the packages depending on libstdc++, see the [revdep-rebuild] [instructions](https://wiki.gentoo.org/wiki/GCC#Downgrading_GCC "GCC") above.

### [][undefined reference to \`\_\_cxa_call_terminate@CXXABI_1.3.15\']

This is usually a result of compiling a package that had its dependencies built with a newer GCC version than with the current one selected. An example output might be:

[CODE] **undefined reference to \_\_cxa_call_terminate@CXXABI_1.3.15**

    /usr/lib/gcc/x86_64-pc-linux-gnu/13/../../../../x86_64-pc-linux-gnu/bin/ld: /usr/lib64/libgtest.so: undefined reference to `__cxa_call_terminate@CXXABI_1.3.15'

What this means is the package that is emerging is building with, for example, GCC 13 but the package that provides `libgtest.so` was built with a newer version of GCC, 14 in this case.

If hitting this, first, if not deliberately downgrading GCC, make sure to select the latest toolchain versions:

`root `[`#`]`binutils-config latest && gcc-config latest && . /etc/profile`

If deliberately downgrading GCC, read on. The solution to this problem is rather simple but can be hard to figure out if the package providing the file is unknown. [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") supports emerging file paths directly so running [emerge -1 /path/to/file.so] might detect the file.

In the example, try emerging [/usr/lib64/libgtest.so]

`root `[`#`]`emerge -1a /usr/lib64/libgtest.so`

    Calculating dependencies -

    !!! '/usr/lib/libgtest.so' is not claimed by any package.
    ... done!

Unfortunately the file needed was not claimed, but another utility exists to find files installed by packages, [Pfl](https://wiki.gentoo.org/wiki/Pfl "Pfl"). Using [e-file], it is possible to find the package that installs the needed file.

`user `[`$`]`e-file libgtest.so`

    ...
    [I] dev-cpp/gtest
            Seen Versions:          1.13.0 1.14.0
            Portage Versions:       1.13.0 1.14.0 9999
            Installed Versions:     1.14.0(Fri Nov 24 04:35:00 2023)
            Homepage:               https://github.com/google/googletest
            Description:            Google C++ Testing Framework
            Matched Files:          /usr/lib/libgtest.so; /usr/lib64/libgtest.so
    ...

In this case, [[[dev-cpp/gtest]](https://packages.gentoo.org/packages/dev-cpp/gtest)[]] is causing the build issue, re-merging it with:

`root `[`#`]`emerge --ask --oneshot dev-cpp/gtest`

should fix the issue and allow the continuation of emerging the original package.

** Note**\
For larger packages, it is likely to encounter this more than once while rebuilding a package with a lower version of GCC, keep following the above steps to eventually succeed in recompiling the package with GCC 13

## [[] See also]

-   [Clang](https://wiki.gentoo.org/wiki/LLVM/Clang "LLVM/Clang") --- a C/C++/Objective-C/C++, CUDA, and RenderScript language front-end for the LLVM project
-   [GCC_optimization](https://wiki.gentoo.org/wiki/GCC_optimization "GCC optimization") --- an introduction to optimizing compiled code using safe, sane [`CFLAGS` and `CXXFLAGS`](https://en.wikipedia.org/wiki/CFLAGS "wikipedia:CFLAGS").
-   [GCC/Frontend](https://wiki.gentoo.org/wiki/GCC/Frontend "GCC/Frontend") --- describes how to write a [frontend](https://en.wikipedia.org/wiki/Compiler#Front_end) for [GCC] using [JIT](https://gcc.gnu.org/onlinedocs/jit/)
-   [ICE Reporting Guide](https://wiki.gentoo.org/wiki/GCC/ICE_Reporting_Guide "GCC/ICE Reporting Guide") --- guide to debugging **GCC Internal Compiler Errors** (ICEs)

## [[] External resources]

-   [Installing GCC: Building](https://gcc.gnu.org/install/build.html) - Details about building gcc including stages and bootstrap

## [[] References]

1.  [[[↑](#cite_ref-1)] [[Wikipedia:GNU_Compiler_Collection](https://en.wikipedia.org/wiki/GNU_Compiler_Collection "wikipedia:GNU Compiler Collection")]]
2.  [[[↑](#cite_ref-2)] [[https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html#Optimize-Options](https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html#Optimize-Options) Retrieved on Feb 7 2023]]