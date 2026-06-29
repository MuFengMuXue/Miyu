**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:LLVM "Project:LLVM")][Project](https://wiki.gentoo.org/wiki/Project:LLVM "Project:LLVM")

[[]][Home](https://llvm.org/)

[[]][Official documentation](https://llvm.org/docs/)

[[]][Package information](https://packages.gentoo.org/packages/llvm-core/llvm)

[[]][GitHub](https://github.com/llvm/llvm-project)

[[]][Wikipedia](https://en.wikipedia.org/wiki/LLVM "wikipedia:LLVM")

[[]][[#llvm](irc://irc.oftc.net/#llvm) (on [irc://irc.oftc.net](irc://irc.oftc.net)])

The **LLVM** Project is a collection of modular and reusable compiler and toolchain technologies.

\"LLVM\" is an orphan initialism; originally an acronym standing for *Low Level Virtual Machine*, LLVM today has little to do with [virtual machines](https://wiki.gentoo.org/wiki/Virtualization "Virtualization") under the contemporary understanding of the term.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [LLVM_TARGETS]](#LLVM_TARGETS)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [LLVM components]](#LLVM_components)
-   [[3] [Advanced Usage]](#Advanced_Usage)
    -   [[3.1] [LLVM profiles]](#LLVM_profiles)
        -   [[3.1.1] [Desktop LLVM profiles]](#Desktop_LLVM_profiles)
    -   [[3.2] [Using libcxx]](#Using_libcxx)
    -   [[3.3] [Kernel]](#Kernel)
        -   [[3.3.1] [Distribution Kernel]](#Distribution_Kernel)
    -   [[3.4] [Bootstrapping the LLVM toolchain]](#Bootstrapping_the_LLVM_toolchain)
        -   [[3.4.1] [Preparing the environment]](#Preparing_the_environment)
        -   [[3.4.2] [Finalizing]](#Finalizing)
    -   [[3.5] [Bootstrapping Rust]](#Bootstrapping_Rust)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [ld.lld: error: undefined symbol: \... std::\_\_1::basic_string]](#ld.lld:_error:_undefined_symbol:_..._std::_1::basic_string)
    -   [[4.2] [Compiling with GCC on LLVM profile]](#Compiling_with_GCC_on_LLVM_profile)
    -   [[4.3] [error: cannot open crtbeginS.o: No such file or directory]](#error:_cannot_open_crtbeginS.o:_No_such_file_or_directory)
-   [[5] [Notes]](#Notes)

## [Installation]

### [USE flags]

### [USE flags for] [llvm-core/llvm](https://packages.gentoo.org/packages/llvm-core/llvm) [[]] [Low Level Virtual Machine]

  ----------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+binutils-plugin`](https://packages.gentoo.org/useflags/+binutils-plugin)   Build the binutils plugin
  [`+debug`](https://packages.gentoo.org/useflags/+debug)                       Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`+libffi`](https://packages.gentoo.org/useflags/+libffi)                     Enable support for Foreign Function Interface library
  [`debuginfod`](https://packages.gentoo.org/useflags/debuginfod)               Install llvm-debuginfod (requires net-misc/curl and dev-cpp/cpp-httplib)
  [`doc`](https://packages.gentoo.org/useflags/doc)                             Build and install the HTML documentation and regenerate the man pages
  [`exegesis`](https://packages.gentoo.org/useflags/exegesis)                   Enable performance counter support for llvm-exegesis tool that can be used to measure host machine instruction characteristics
  [`libedit`](https://packages.gentoo.org/useflags/libedit)                     Use the libedit library (replacement for readline)
  [`ncurses`](https://packages.gentoo.org/useflags/ncurses)                     Support querying terminal properties using ncurses\' terminfo
  [`test`](https://packages.gentoo.org/useflags/test)                           Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)               Verify upstream signatures on distfiles
  [`xar`](https://packages.gentoo.org/useflags/xar)                             Support dumping LLVM bitcode sections in Mach-O files (uses app-arch/xar)
  [`xml`](https://packages.gentoo.org/useflags/xml)                             Add support for XML files
  [`z3`](https://packages.gentoo.org/useflags/z3)                               Enable support for sci-mathematics/z3 constraint solver
  [`zstd`](https://packages.gentoo.org/useflags/zstd)                           Enable support for ZSTD compression
  ----------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-21 09:37] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [LLVM_TARGETS]

** Warning**\
Overriding LLVM_TARGETS is not recommended: one should only change these if the inherent risks are fully understood. For further information, refer to [this forum post](https://forums.gentoo.org/viewtopic-t-1161113.html).

In this example, LLVM_TARGET_AArch64 will be removed from `LLVM_TARGETS`. In [/etc/portage/profile/package.use.mask](https://wiki.gentoo.org/wiki//etc/portage/profile/package.use.mask "/etc/portage/profile/package.use.mask"), create a file with the following contents:

[FILE] **`/etc/portage/profile/package.use.mask/llvm_targets`**

    llvm-core/llvm LLVM_TARGETS: AArch64
    llvm-core/clang LLVM_TARGETS: AArch64

Finally, rebuild LLVM and Clang:

`root `[`#`]`emerge --ask --oneshot llvm-core/llvm llvm-core/clang`

### [Emerge]

`root `[`#`]`emerge --ask llvm-core/llvm`

## [LLVM components]

LLVM is comprised of the following components:

-   [LLVM Core]
-   BOLT
-   [Clang](https://wiki.gentoo.org/wiki/LLVM/Clang "LLVM/Clang")
-   compiler-rt
-   [Flang](https://wiki.gentoo.org/wiki/Fortran#Flang "Fortran")
-   libcxx
-   libc^[\[note\ 1\]](#cite_note-not-supported-1)^
-   libclc
-   [LLD](https://wiki.gentoo.org/wiki/LLVM/LLD "LLVM/LLD")
-   LLDB
-   MLIR
-   OpenMP
-   [polly](https://wiki.gentoo.org/wiki/LLVM/Polly "LLVM/Polly")

## [Advanced Usage]

### [LLVM profiles]

** Warning**\
Most people do not want these even if choosing to use Clang to build most packages.

The LLVM profiles in Gentoo are experimental and intended for playing around with pure-LLVM systems (no GCC).

**Most people do not want these** even if choosing to use Clang to build most packages.

They come with **no guarantees** of support or stability and are *not* simply the same as setting `CC` and `CXX` for Clang; the LLVM profiles use libcxx which means they\'re ABI-incompatible with the regular profiles using libstdc++.

See also the following bugs:

-   LLVM profiles: rename libcxx-using profiles to include libcxx in the name - [[[bug #944478]](https://bugs.gentoo.org/show_bug.cgi?id=944478)[]]
-   LLVM profiles: add separate libstdc++ profiles - [[[bug #944482]](https://bugs.gentoo.org/show_bug.cgi?id=944482)[]]
-   LLVM profile links should have a warning above them - [[[bug #944483]](https://bugs.gentoo.org/show_bug.cgi?id=944483)[]].

#### [Desktop LLVM profiles]

Desktop profiles for LLVM can be created by following [Combining multiple profiles from the Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Profile_(Portage)#Example_1:_Combining_multiple_profiles_from_the_Gentoo_ebuild_repository "Profile (Portage)") at one\'s own risk.

### [Using libcxx]

Using libcxx / libc++ breaks ABI. Doing so means that GCC cannot be used as a fallback. See the LLVM profile section for more.

### [Kernel]

The Linux kernel can be compiled with Clang and the LLVM toolchain by defining a kernel environment variable.

`root `[`#`]`LLVM=1`

To configure Clang specific kernel options such as link-time optimizations or control flow integrity, run the following command:

`root `[`#`]`LLVM=1 make menuconfig`

The above example demonstrates using `menuconfig`. Other options are `nconfig` and `xconfig`. Next, compile the kernel as normal.

`root `[`#`]`LLVM=1 make -j$N`

In the past, it was necessary to pass `LLVM_IAS=1` to use the Clang internal assembler for a complete LLVM toolchain built kernel. This is no longer required since `LLVM=1` now defaults to include the Clang internal assembler. Use `LLVM_IAS=0` to disable the internal assembler if desired, otherwise stick to the default behavior.

#### [Distribution Kernel]

Compile the [distribution kernels](https://wiki.gentoo.org/wiki/Project:Distribution_Kernel "Project:Distribution Kernel") (for clarity\'s sake, not including the binary kernel) with LLVM using the following configs **in addition** to the values in package.env or make.conf as described in [LLVM/Clang](https://wiki.gentoo.org/wiki/LLVM/Clang#Configuration "LLVM/Clang"):

[FILE] **`/etc/portage/env/llvm-kernel`**

    LLVM=1

and

[FILE] **`/etc/portage/package.env/gentoo-kernel`**

    sys-kernel/gentoo-kernel llvm-kernel

### [Bootstrapping the LLVM toolchain]

For a \"pure\" Clang toolchain, one can build the whole LLVM stack using itself; this is unnecessary, but users may do so for fun.

Advanced users can choose to bootstrap [LLVM/Clang](https://wiki.gentoo.org/wiki/LLVM/Clang "LLVM/Clang") by building it using the full LLVM toolchain, thus fully dogfooding with clang.

Be warned that due to LLVM\'s internal structure and style of packaging, this is liable to break across upgrades of major versions.

This is *required* only if looking to move a system to be entirely [GCC](https://wiki.gentoo.org/wiki/GCC "GCC")-free (which is currently not possible on [Glibc](https://wiki.gentoo.org/wiki/Glibc "Glibc") systems). **This is not yet supported and is dangerous**.

Mixing Clang and GCC should be fine, unless using [[[default-libcxx]](https://packages.gentoo.org/useflags/default-libcxx)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")]; otherwise, the two should always produce output with the same ABI.

#### [Preparing the environment]

Prepare the environment for the Clang toolchain:

[FILE] **`/etc/portage/env/compiler-clang`**

    COMMON_FLAGS="-march=native -O2 -pipe"
    CFLAGS="$"
    CXXFLAGS="$"

    CC="clang"
    CXX="clang++"

    LDFLAGS="-fuse-ld=lld -rtlib=compiler-rt -unwindlib=libunwind -Wl,--as-needed"

This example replaces not only the compiler but also the GNU linker [ld.bfd] with the LLVM linker [lld] which is a drop-in replacement that is significantly faster than the bfd linker.

Set USE flags `default-compiler-rt default-lld llvm-libunwind` for Clang via [/etc/portage/package.use]:

[FILE] **`/etc/portage/package.use/clang`**

    llvm-core/clang-common default-compiler-rt default-lld llvm-libunwind

Then install Clang, LLVM, compiler-rt, llvm-runtimes/libunwind, and lld with the default GCC environment:

`root `[`#`]`emerge llvm-core/clang llvm-core/llvm llvm-runtimes/compiler-rt llvm-runtimes/libunwind llvm-core/lld`

It is also possible to add the `default-libcxx` USE flag to use LLVM\'s C++ STL with clang, however this is **heavily** discouraged because libstdc++ and libc++ are not ABI compatible (i.e., a program built against libstdc++ will likely break when using a library built against libc++, and vice versa).

Note that [[[llvm-runtimes/libunwind]](https://packages.gentoo.org/packages/llvm-runtimes/libunwind)[]] deals with linking issues that [[[sys-libs/libunwind]](https://packages.gentoo.org/packages/sys-libs/libunwind)[]] has, so it is preferred to use and replace the non-llvm libunwind package if installed (it builds with `-lgcc_s` to resolve issues with `__register_frame` / `__deregister_frame` undefined symbols).

#### [Finalizing]

Enable the Clang environment for these packages now:

[FILE] **`/etc/portage/package.env`**

    llvm-core/clang compiler-clang
    llvm-core/llvm compiler-clang
    llvm-runtimes/libcxx compiler-clang
    llvm-runtimes/libcxxabi compiler-clang
    llvm-runtimes/compiler-rt compiler-clang
    llvm-runtimes/compiler-rt-sanitizers compiler-clang
    llvm-runtimes/libunwind compiler-clang
    llvm-core/lld compiler-clang

Repeat the emerge step with the new environment - the toolchain will be rebuilt using itself instead of GCC:

`root `[`#`]`emerge llvm-core/clang llvm-core/llvm llvm-runtimes/libcxx llvm-runtimes/libcxxabi llvm-runtimes/compiler-rt llvm-runtimes/compiler-rt-sanitizers llvm-runtimes/libunwind llvm-core/lld`

Clang may now be used with other packages!

### [Bootstrapping Rust]

On LLVM-based systems using musl, packages may break if dev-lang/rust-bin is the active Rust installation, and is therefore masked ([[[bug #912154]](https://bugs.gentoo.org/show_bug.cgi?id=912154)[]]). Emerge dev-lang/rust requires a Rust installation, which leads to a circular dependency that cannot be resolved.

In this case Rust can be built in two ways:

-   [Bootstrapping Rust via (non-LLVM) stage file](https://wiki.gentoo.org/wiki/Bootstrapping_Rust_via_stage_file "Bootstrapping Rust via stage file") on the same host
-   [Bootstrapping Rust via cross compilation](https://wiki.gentoo.org/wiki/Bootstrapping_Rust_via_cross_compilation "Bootstrapping Rust via cross compilation") from another host via cross compilation

\

## [Troubleshooting]

### [ld.lld: error: undefined symbol: \... std::\_\_1::basic_string]

This means that libc++ has been enabled instead of libstdc++ as the default C++ standard library for Clang by either switching to the [LLVM profile](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)"), installing [[[llvm-core/clang-common]](https://packages.gentoo.org/packages/llvm-core/clang-common)[]] with `USE=default-libcxx`, or by adding `--stdlib=libc++` directly in `CXXFLAGS`. Switching to libc++ breaks ABI compatibility for libraries with a C++ public interface (for example, libLLVM), because libc++ uses the `std::__1` namespace; to use libc++, such libraries must be recompiled with `emerge -av1 llvm-core/llvm && emerge @preserved-rebuild` before installing other software.

### [Compiling with GCC on LLVM profile]

/usr/src/debug/sys-libs/glibc-2.37-r3/glibc-2.37/csu/../sysdeps/x86_64/start.S:103: undefined reference to \`main\'

Use bfd linker. Add `-fuse-ld=bfd` to `CFLAGS`, `CXXFLAGS`, and `LDFLAGS` at the `/etc/portage/env/compiler-gcc-lto` or `/etc/portage/env/compiler-gcc` configuration files.

### [error: cannot open crtbeginS.o: No such file or directory]

`musl-ld: error: cannot open crtbeginS.o: No such file or directory`\
`musl-ld: error: unable to find library -lgcc`\
`musl-ld: error: unable to find library -lgcc_s`\
`musl-ld: error: unable to find library -lgcc`\
`musl-ld: error: unable to find library -lgcc_s`

[Bug 951445](https://bugs.gentoo.org/951445): `emerge --oneshot --nodeps clang-runtime` after merging compiler-rt: you should then be able to upgrade libcxxabi without trouble.

## [Notes]

1.  [[[↑](#cite_ref-not-supported_1-0)] [Not supported by Gentoo, as of 2025-01-06]]