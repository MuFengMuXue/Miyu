This page contains [[changes](https://wiki.gentoo.org/index.php?title=Zig&oldid=1422694&diff=1435168)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Zig/de "Zig (21% translated)")
-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Zig/hu "Zig (28% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Zig/ru "Zig/ru (78% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Zig/ja "Zig (35% translated)")

**Resources**

[[]][Home](https://ziglang.org)

[[]][Official documentation](https://ziglang.org/learn/)

[[]][Package information](https://packages.gentoo.org/packages/dev-lang/zig)

[[]][Binary package information](https://packages.gentoo.org/packages/dev-lang/zig-bin)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Zig_(programming_language) "wikipedia:Zig (programming language)")

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/zig)

[![Codeberg Logo](/images/thumb/c/cc/Codeberg-logo.png/30px-Codeberg-logo.png)][Codeberg](https://codeberg.org/ziglang/zig)

[[]][Bugs (upstream)](https://github.com/ziglang/zig/issues)

[[]][[#zig](ircs://irc.libera.chat/#zig)] ([[webchat](https://web.libera.chat/#zig)])

[[]][Blog](https://ziglang.org/devlog/)

**Zig** is a general-purpose programming language and toolchain for maintaining robust, optimal and reusable software.

Zig positions itself as a modern alternative to [C language](https://wiki.gentoo.org/wiki/C "C"), with greater expressiveness, enhanced safety, and increased power --- in some areas operating at an even lower level than C.

Official Zig toolchain from Zig Software Foundation contains:

-   compiler, formatter, and test runner for Zig code,
-   compiler for [C](https://wiki.gentoo.org/wiki/C "C"), [C++](https://wiki.gentoo.org/wiki/C%2B%2B "C++") and Objective-C code; and automatic translator from C to Zig (based on [Clang](https://wiki.gentoo.org/wiki/LLVM/Clang "LLVM/Clang") or own [Aro](https://github.com/Vexu/arocc) compiler),
-   build system, which integrates all tools above in one package and targets pure-Zig, pure-C/C++, or mixed projects.

\
Thanks to the last 2 points, Zig has easy interoperability with libraries and programs that have C ABI support, and can call or define C functions without FFI.

** Important**\
Unless specified otherwise, the information in this article applies to Zig 0.14.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Prerequisites]](#Prerequisites)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Choosing variant]](#Choosing_variant)
    -   [[1.4] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Environment variables]](#Environment_variables)
        -   [[2.1.1] [ZIG_TARGET]](#ZIG_TARGET)
        -   [[2.1.2] [ZIG_CPU]](#ZIG_CPU)
        -   [[2.1.3] [ZBS_ARGS_EXTRA]](#ZBS_ARGS_EXTRA)
    -   [[2.2] [Setting a default slot]](#Setting_a_default_slot)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Caching system]](#Caching_system)
    -   [[3.2] [Optimize modes]](#Optimize_modes)
    -   [[3.3] [IDE and editor support]](#IDE_and_editor_support)
    -   [[3.4] [Freestanding]](#Freestanding)
    -   [[3.5] [Authoring ebuilds]](#Authoring_ebuilds)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [\"undefined reference to \...\" during emerging]](#.22undefined_reference_to_....22_during_emerging)
    -   [[4.2] [warning: Encountered error: UnexpectedEndOfFile, falling back to default ABI and dynamic linker.]](#warning:_Encountered_error:_UnexpectedEndOfFile.2C_falling_back_to_default_ABI_and_dynamic_linker.)
-   [[5] [Removal]](#Removal)
    -   [[5.1] [Unmerge]](#Unmerge)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)
-   [[8] [References]](#References)

## [[] Installation]

### [[] Prerequisites]

** Note**\
TODO: Cover how Zig is compiled using WASM transpiler to C, and how [WASM seed can be reproduced without binaries](https://jakstys.lt/2024/zig-reproduced-without-binaries/) (apparently to be used by Guix^[\[1\]](#cite_note-1)^).

Zig requires Linux kernel version 4.19+. If building from source, it must be built with same compiler as LLVM/Clang, or the user will get in trouble (see relevant section in [Troubleshooting](https://wiki.gentoo.org/wiki/Zig#Troubleshooting "Zig") below).

### [[] USE flags]

### [USE flags for] [dev-lang/zig](https://packages.gentoo.org/packages/dev-lang/zig) [[]] [A robust, optimal, and maintainable programming language]

  ----------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------
  [`+llvm`](https://packages.gentoo.org/useflags/+llvm)             Build with LLVM backend and extensions enabled.
  [`debug`](https://packages.gentoo.org/useflags/debug)             Build with debug extensions enabled.
  [`doc`](https://packages.gentoo.org/useflags/doc)                 Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-06 08:13] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [USE flags for] [dev-lang/zig-bin](https://packages.gentoo.org/packages/dev-lang/zig-bin) [[]] [A robust, optimal, and maintainable programming language]

  ----------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------
  [`doc`](https://packages.gentoo.org/useflags/doc)                 Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-20 18:03] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [[] Choosing variant]

Gentoo repository provides two package variants for the Zig toolchain. Both provide latest tagged releases, as well as versions specific to each variant.

All Zig versions are slotted and can be installed side-by-side if needed.

[[[dev-lang/zig]](https://packages.gentoo.org/packages/dev-lang/zig)[]]: based on official source code. Recommended:

-   For users who need more configurability, such as enabling compiler debugging to investigate crashes or contribute fixes upstream.
-   When required version of the LLVM suite is already installed.
-   If nightly version (9999) is needed.

[[[dev-lang/zig-bin]](https://packages.gentoo.org/packages/dev-lang/zig-bin)[]]: based on official binaries. Recommended:

-   For users who don\'t want to spend time building Zig and/or LLVM suite.
-   If version with old async/await implementation (0.10.1) is needed.

** Tip**\
If LLVM compiling is deemed too long, but compiling Zig itself is acceptable, user can try to enable [Gentoo binary host](https://wiki.gentoo.org/wiki/Gentoo_Binary_Host_Quickstart "Gentoo Binary Host Quickstart") and use pre-built LLVM.

Alternatively, `llvm` USE-flag can be disabled for [[[dev-lang/zig]](https://packages.gentoo.org/packages/dev-lang/zig)[]] instead.

However, note that not all architectures or packages support it. At the moment of writing, it\'s limited to x86-64 architecture.

### [[] Emerge]

To emerge the package:

`root `[`#`]`emerge --ask dev-lang/zig`

** Note**\
Replace [[[dev-lang/zig]](https://packages.gentoo.org/packages/dev-lang/zig)[]] with [[[dev-lang/zig-bin]](https://packages.gentoo.org/packages/dev-lang/zig-bin)[]] to use Zig\'s binary package.

## [[] Configuration]

### [[] Environment variables]

All ebuilds that inherit from [[zig.eclass]](https://devmanual.gentoo.org/eclass-reference/zig.eclass/index.html) or [[zig-utils.eclass]](https://devmanual.gentoo.org/eclass-reference/zig-utils.eclass/index.html) use following environment variables to configure build process:

** Important**\
It\'s recommended to not touch these variables unless a specific need arises. Default values should be good enough for any system:

-   `ZIG_TARGET`: auto-detect by Zig, or follow [`CHOST`](https://wiki.gentoo.org/wiki/CHOST "CHOST") and [`CFLAGS`](https://wiki.gentoo.org/wiki/GCC_optimization "GCC optimization").
-   `ZIG_CPU`: follow [`CFLAGS`](https://wiki.gentoo.org/wiki/GCC_optimization "GCC optimization") and [`CHOST`](https://wiki.gentoo.org/wiki/CHOST "CHOST").
-   `ZBS_ARGS_EXTRA`: follow [`MAKEOPTS`](https://wiki.gentoo.org/wiki/MAKEOPTS "MAKEOPTS") for job thread count, compile with ReleaseSafe optimization mode.

#### [[] ZIG_TARGET]

`ZIG_TARGET` specifies the Zig target tuple. It\'s closest analog from C toolchains is `CHOST`.

It corresponds to `-Dtarget` option in [zig build] or `-target` option in [zig build-exe].

By default it\'s set to `native` (enables auto-detection by Zig). If cross-compiling is enabled, [zig-utils.eclass] tries to make correct value by converting content of `CHOST` and `CFLAGS` to `ZIG_TARGET` format.

It\'s recommended to not change this variable and let it follow C settings, unless translation by eclass or auto-detection by Zig fails.

[FILE] **`/etc/portage/make.conf/zig`Setting ZIG_TARGET**

    # General format:
    <arch>-<os>-<abi>
    # Optionally, after <os> and <abi> their version can be specified.

    # Let Zig detect automatically for host
    ZIG_TARGET="native"

    # Linux x86-64 system, with glibc
    ZIG_TARGET="x86_64-linux-gnu"
    # With versions limit (Linux kernel 6.1.12+ and glibc 2.38+)
    ZIG_TARGET="x86_64-linux.6.1.12...6.6.16-gnu.2.38"

    # Linux PPC64 little-endian system, with musl
    ZIG_TARGET="powerpc64le-linux-musl"

#### [[] ZIG_CPU]

`ZIG_CPU` specifies the Zig target CPU. It\'s closest analog from C toolchains is [`CFLAGS` (part with `-march`, `-mcpu` and other flags)](https://wiki.gentoo.org/wiki/GCC_optimization#cpu-type "GCC optimization").

It corresponds to `-Dcpu` option in [zig build] or `-mcpu` option in [zig build-exe].

By default [zig-utils.eclass] tries to make correct value by converting content of `CFLAGS` and `CHOST` to `ZIG_CPU` format.

It can be changed safely at any time, but it\'s still recommended to let it be auto-filled by eclass using C environment variables.

[FILE] **`/etc/portage/make.conf/zig`Setting ZIG_CPU**

    # General format:
    <cpu>
    # Optionally, after <cpu> list of enabled and disabled features can be specified.
    # + means it is enabled, and - means disabled.

    # Let Zig detect automatically for host
    ZIG_CPU="native"

    # AMD Zen 2 processor
    ZIG_CPU="znver2"
    # Generic x86-64 processor, supporting X87 instructions, but not SSE2
    ZIG_CPU="x86_64+x87-sse2"

#### [[] ZBS_ARGS_EXTRA]

`ZBS_ARGS_EXTRA` specifies additional arguments passed to [zig build]. It\'s closest analog from C toolchains is `MAKEOPTS` and [`CFLAGS` (part with `-O` flags)](https://wiki.gentoo.org/wiki/GCC_optimization#-O "GCC optimization").

By default it is empty, and eclass tries to get job count (like `-j8`) from `MAKEOPTS`. If `ZBS_ARGS_EXTRA` is set, eclass will try to get job count from it instead.

[FILE] **`/etc/portage/make.conf/zig`Setting ZBS_ARGS_EXTRA**

    # By default, ebuilds will use ReleaseSafe optimization mode (analog of -O2).

    # Allow using up to 8 threads and compile in ReleaseSmall if possible (analog of -Os)
    ZBS_ARGS_EXTRA="-j8 --release=small"
    # Compile in Debug if possible (analog of -Og)
    ZBS_ARGS_EXTRA="--release=none"

### [[] Setting a default slot]

The [eselect] command can be used to manipulate a [/usr/bin/zig] symlink.

`user `[`$`]`eselect zig help`

    Manage Zig versions
    Usage: eselect zig <action> <options>
    Standard actions:
      help                      Display help text
      usage                     Display usage information
      version                   Display version information
    Extra actions:
      list                      List available Zig versions
      set <target>              Set active Zig version
        target                    Target name or number (from 'list' action)
      show                      Show current Zig version
      update                    Automatically update the zig symlink
        ifunset                   Do not override currently set version

`user `[`$`]`eselect zig list`

    Available Zig versions:
      [1]   zig-0.10.1 *
      [2]   zig-bin-0.10.1

## [[] Usage]

### [[] Caching system]

Some sub-commands of Zig toolchain such as [zig build], [zig run] and [zig test] use integrated caching system. This system stores compiled artifacts, generated source files, and other intermediate data to improve compiler performance and avoid redundant work.

** Warning**\
The caching system does not currently support automatic cleanup of old entries^[\[2\]](#cite_note-2)^. Over time, this can cause the cache to grow significantly, potentially consuming several tens of gigabytes. It\'s recommended to clean it up manually from time to time.

The caching system is divided into two parts: the global cache and the local cache.

The **global cache** is used to store data shared across different compilations. By default, it is located at [\$/zig], or if `XDG_CACHE_HOME` is not set, at [\$/.cache/zig]. It typically contains:

-   Fetched Zig packages,
-   Cached binaries of JIT-executed sub-commands, such as Aro C compiler or [zig std] documentation browser.

The **local cache** is specific to a single project and stores artifacts related to the current compilation. By default, it is stored in the [.zig-cache] subdirectory located next to the project\'s [build.zig] file. It typically contains:

-   Translated C headers generated during [zig translate-c] process,
-   Compiled binaries and generated source code for current project.

** Note**\
Before Zig 0.13, the local cache was stored in a directory named [zig-cache].

Both cache locations can be configured explicitly using command-line options:

-   `--global-cache-dir`: sets a custom path for the global cache.
-   `--cache-dir`\': sets a custom path for the local (project-specific) cache.

Alternatively, the behavior of the caching system can be customized using the following environment variables:

-   `ZIG_GLOBAL_CACHE_DIR`: Specifies the directory used for the global cache.
-   `ZIG_LOCAL_CACHE_DIR`: Specifies the directory used for the local cache.

### [[] [] Optimize modes]

Zig has 4 *[optimize modes](https://ziglang.org/documentation/0.14.1/#Build-Mode)*, which define how final binary should be optimized, in same manner as `-O` options from CFLAGS:

+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| Feature                                                                                                                  | [Debug](https://ziglang.org/documentation/0.14.1/#Debug) (default for Zig) | [ReleaseSafe](https://ziglang.org/documentation/0.14.1/#ReleaseSafe) (default for eclass) | [ReleaseFast](https://ziglang.org/documentation/0.14.1/#ReleaseFast) | [ReleaseSmall](https://ziglang.org/documentation/0.14.1/#ReleaseSmall) |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| Compilation speed                                                                                                        | Fast                                                                                                       | Slow                                                                                                                      | Slow                                                                                                 | Slow                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| [Safety checks](https://ziglang.org/documentation/0.14.1/#Undefined-Behavior) at runtime | Enabled                                                                                                    | Enabled                                                                                                                   | Disabled                                                                                             | Disabled                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| Optimizations                                                                                                            | Disabled                                                                                                   | For performance                                                                                                           | For performance                                                                                      | For minimal size                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| Reproducible                                                                                                             | Not guaranteed                                                                                             | Guaranteed                                                                                                                | Guaranteed                                                                                           | Guaranteed                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| C equivalent (for interop/compiling)                                                                                     | `-O0 -D_DEBUG`                                                                                             | `-O2 -D_FORTIFY_SOURCE=2`                                                                                                 | `-O2 -DNDEBUG`                                                                                       | `-Os -DNDEBUG`                                                                                         |
|                                                                                                                          |                                                                                                            |                                                                                                                           |                                                                                                      |                                                                                                        |
| ^[\[3\]](#cite_note-3)^ ^[\[4\]](#cite_note-4)^                                                                          |                                                                                                            |                                                                                                                           |                                                                                                      |                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

For Gentoo ebuilds, ReleaseSafe is used by default, unless user, ebuild or project set their own preferences.

** Note**\
Code authors can override safety checks by using [\@setRuntimeSafety](https://ziglang.org/documentation/0.10.1/#setRuntimeSafety).

### [[] IDE and editor support]

Most of editors and IDEs plugins for Zig leverage unofficial language server called [ZLS](https://github.com/zigtools/zls). It is available as [[[dev-zig/zls]](https://github.com/gentoo/guru/tree/master/dev-zig/zls)[]] package in [GURU repository](https://wiki.gentoo.org/wiki/Project:GURU "Project:GURU").

For installing follow [this](https://wiki.gentoo.org/wiki/Project:GURU/Information_for_End_Users "Project:GURU/Information for End Users") guide to enable GURU repository, [accept testing branch for this package](https://wiki.gentoo.org/wiki/Knowledge_Base:Accepting_a_keyword_for_a_single_package "Knowledge Base:Accepting a keyword for a single package") and run:

`root `[`#`]`emerge --ask dev-zig/zls::guru`

After that, visit this [list of tools](https://ziglang.org/learn/tools/#text-editors) curated by the Zig developers.

### [[] Freestanding]

User might want to take a look at posts [Using Zig to build a bare metal RISCV32 binary](https://www.ringtailsoftware.co.uk/zig-baremetal/) and [Build an IoT App with Zig and LoRaWAN](https://lupyuen.github.io/articles/iot).

### [[] Authoring ebuilds]

Before creating ebuilds for programs or libraries written in Zig, it is highly recommended to read the documentation for [Zig Build System](https://ziglang.org/learn/build-system/), [[zig.eclass]](https://devmanual.gentoo.org/eclass-reference/zig.eclass/index.html), and [[zig-utils.eclass]](https://devmanual.gentoo.org/eclass-reference/zig-utils.eclass/index.html).

After that, read the documentation for [zig-ebuilder](https://github.com/BratishkaErik/zig-ebuilder) and install it. It is available as [[[app-portage/zig-ebuilder]](https://github.com/gentoo/guru/tree/master/app-portage/zig-ebuilder)[]] package in [GURU repository](https://wiki.gentoo.org/wiki/Project:GURU "Project:GURU").

## [[] Troubleshooting]

### [][[] \"undefined reference to \...\" during emerging]

This issue most commonly occurs when LLVM and Clang packages were built using a different C++ compiler or C++ standard library than Zig. Make sure the same compiler and standard library are used, then re-emerge the affected packages.

### [][[] warning: Encountered error: UnexpectedEndOfFile, falling back to default ABI and dynamic linker.]

When targeting the host system, the Zig compiler relies on the presence of [/usr/bin/env] to help determine the appropriate [libc](https://wiki.gentoo.org/wiki/Libc "Libc").

To do this, it examines whether [/usr/bin/env] is:

-   a regular ELF executable, or
-   a symbolic link to another file, or
-   a script that starts with a shebang line (i.e. `#!`) pointing to another file.

This resolution is performed recursively until a valid ELF binary is found.

Once located, Zig attempts to extract libc information from that ELF file.

If this process fails, Zig falls back to default assumptions for the libc and ABI --- for example, using musl on Linux. This can lead to unexpected behavior or incorrect builds.

To avoid detection issues, explicitly pass the target by setting `ZIG_TARGET`.

If this occurs outside of ebuilds (for example, during regular use of Zig commands), target should be specified explicitly, as shown below:

`user `[`$`]`zig build -Dtarget=<target>`

`user `[`$`]`zig build-exe -target <target>`

Here, `target` is the desired target tuple, such as:

-   `native-native-gnu`
-   `native-native-musl`

See the [ZIG_TARGET](https://wiki.gentoo.org/wiki/Zig#ZIG_TARGET "Zig") section for more details on the target format.

## [[] Removal]

### [[] Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose dev-lang/zig`

## [[] See also]

-   [C](https://wiki.gentoo.org/wiki/C "C") --- a programming language developed for Bell Labs in the early 1970s
-   [Clang](https://wiki.gentoo.org/wiki/LLVM/Clang "LLVM/Clang") --- a C/C++/Objective-C/C++, CUDA, and RenderScript language front-end for the LLVM project
-   [Rust](https://wiki.gentoo.org/wiki/Rust "Rust") --- a general-purpose, multi-paradigm, compiled, programming language.
-   [Go](https://wiki.gentoo.org/wiki/Go "Go") --- an open source, statically typed, compiled programming language
-   [Zig/Internals](https://wiki.gentoo.org/wiki/Zig/Internals "Zig/Internals") --- describes how [Zig] compiles Zig source code into executable

## [[] External resources]

-   Official [list](https://github.com/ziglang/zig/wiki/Community) of the community spaces
-   Official [list](https://github.com/ziglang/zig/wiki/Community-Projects) of community projects and [awesome-zig](https://github.com/catdevnull/awesome-zig) list
-   [Ziglings](https://codeberg.org/ziglings/exercises) --- learn Zig by fixing tiny broken programs, inspired by Rustlings
-   [Differences](https://github.com/ziglang/zig/wiki/zig-cc-compatibility-with-clang) between [zig cc] and [clang]

## [[] References]

1.  [[[↑](#cite_ref-1)] [[Bootstrapping Zig with no Binary Blobs (Guix issue)](https://issues.guix.gnu.org/74217)]]
2.  [[[↑](#cite_ref-2)] [[https://github.com/ziglang/zig/issues/15358](https://github.com/ziglang/zig/issues/15358)]]
3.  [[[↑](#cite_ref-3)] [[https://github.com/ziglang/zig/blob/0.14.1/src/Compilation.zig#L6083-L6105](https://github.com/ziglang/zig/blob/0.14.1/src/Compilation.zig#L6083-L6105)]]
4.  [[[↑](#cite_ref-4)] [[https://github.com/ziglang/zig/blob/0.14.1/src/Compilation.zig#L5774-L5785](https://github.com/ziglang/zig/blob/0.14.1/src/Compilation.zig#L5774-L5785)]]