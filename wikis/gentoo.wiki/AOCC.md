**Resources**

[[]][Home](https://developer.amd.com/amd-aocc/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/AMD_Optimizing_C/C%2B%2B_Compiler "wikipedia:AMD Optimizing C/C++ Compiler")

**AOCC** ([AMD](https://wiki.gentoo.org/wiki/AMD "AMD") Optimizing C/C++ Compiler) compiler system is a high performance, production quality code generation tool.

The AOCC environment provides various options to developers when building and optimizing C, C++, and Fortran applications targeting 32-bit and 64-bit Linux® platforms. The AOCC compiler system offers a high level of advanced optimizations, multi-threading and processor support that includes global optimization, vectorization, inter-procedural analyses, loop transformations, and code generation. AMD also provides highly optimized libraries, which extract the optimal performance from each x86 processor core when utilized. The AOCC Compiler Suite simplifies and accelerates development and tuning for x86 applications.

## Contents

-   [[1] [Installation]](#Installation)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [With \"AOCC_PATH\" in make.conf / package.env]](#With_.22AOCC_PATH.22_in_make.conf_.2F_package.env)
    -   [[2.2] [Via /etc/env.d]](#Via_.2Fetc.2Fenv.d)
    -   [[2.3] [package.env]](#package.env)
    -   [[2.4] [make.conf]](#make.conf)
    -   [[2.5] [llvm.eclass]](#llvm.eclass)
-   [[3] [Switching to AOCC]](#Switching_to_AOCC)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [\"/opt/aocc/bin/clang: file not found!\"]](#.22.2Fopt.2Faocc.2Fbin.2Fclang:_file_not_found.21.22)
    -   [[4.2] [\"error while loading shared libraries: libLLVM-11.so\"]](#.22error_while_loading_shared_libraries:_libLLVM-11.so.22)
    -   [[4.3] [multilib system, \"multilib-strict check failed!\"]](#multilib_system.2C_.22multilib-strict_check_failed.21.22)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation]

** Warning**\
This is a highly experimental and unsupported package! Don\'t make bug reports for build failures with AOCC!

First [download the latest version from AOCC\'s homepage](https://developer.amd.com/amd-aocc/). Read the EULA carefully before accepting it. Choose a location to **run it from**,

`root `[`#`]`cd /opt `

`root `[`#`]`tar -xvf /tmp/aocc-compiler-2.3.0.tar`

Optional: Make a symlink for future upgrades:

`root `[`#`]`ln -s aocc-compiler-2.3.0/ aocc`

Unarchived media has a script to check for all prerequisities:

`root `[`#`]`cd aocc/ `

`root `[`#`]`sh AOCC-prerequisites-check.sh`

** Note**\
The prerequisities check may return errors for multiple checks; If you don\'t need these features, they can be ignored.

## [Usage]

You should try to match the symlinks of AOCC to [Clang](https://wiki.gentoo.org/wiki/LLVM/Clang "LLVM/Clang")\'s.

`root `[`#`]`cd /opt/aocc/bin `

`root `[`#`]`ln -s clang x86_64-pc-linux-gnu-clang `

`root `[`#`]`ln -s clang++ x86_64-pc-linux-gnu-clang++ `

`root `[`#`]`ln -s clang++-11 x86_64-pc-linux-gnu-clang++-11 `

`root `[`#`]`ln -s clang-11 x86_64-pc-linux-gnu-clang-11 `

`root `[`#`]`ln -s clang-cl-11 x86_64-pc-linux-gnu-clang-cl `

`root `[`#`]`ln -s clang-cl-11 x86_64-pc-linux-gnu-clang-cl-11 `

`root `[`#`]`ln -s clang-cpp-11 x86_64-pc-linux-gnu-clang-cpp `

`root `[`#`]`ln -s clang-cpp-11 x86_64-pc-linux-gnu-clang-cpp-11 `

### [][With \"AOCC_PATH\" in make.conf / package.env]

Please see [[/etc/portage/package.env](https://wiki.gentoo.org/wiki//etc/portage/package.env "/etc/portage/package.env")] to see how [package.env] works.

[FILE] **`/etc/portage/env/aocc.conf`**

    AOCC_PATH="/opt/aocc/bin/"

    CC="$clang"
    CXX="$clang++"

    LDFLAGS="-fuse-ld=lld"

Add LLVM AR, NM and RANLIB if needed:

[FILE] **`/etc/portage/env/aocc.conf`**

    AOCC_PATH="/opt/aocc/bin/"
    CC="$clang"
    CXX="$clang++"

    AR="$llvm-ar"
    NM="$llvm-nm"
    RANLIB="$llvm-ranlib"

    LDFLAGS="-fuse-ld=lld -rtlib=compiler-rt -unwindlib=libunwind"

### [][Via /etc/env.d]

** Note**\
This is optional, and not really needed. Please see [#Switching to aocc](#Switching_to_aocc) below.

`root `[`#`]`cd /etc/env.d`

[FILE] **`/etc/env.d/50aocc`**

    PATH="/opt/aocc/bin"
    # we need to duplicate it in ROOTPATH for Portage to respect...
    ROOTPATH="/opt/aocc/bin"
    MANPATH="/opt/aocc/bin/share/man"
    LDPATH="/opt/aocc/lib/:/opt/aocc/lib/lib32:/opt/aocc/lib/lib64"

** Note**\
we use [50aocc] so it gets placed **before** the default LLVM directory in to your `$PATH`. Suggestion is to use **full path** via `AOCC_PATH` in your [make.conf] or [package.env] to avoid mistakes.

`root `[`#`]`env-update`

** Important**\
Relog for the changes take effect!

Test that it works:

`user `[`$`]`clang -v`

[CODE] **clang -v**

    ''
    AMD clang version 11.0.0 (CLANG: AOCC_2.3.0-Build#85 2020_11_10) (based on LLVM Mirror.Version.11.0.0)
    Target: x86_64-unknown-linux-gnu
    Thread model: posix
    InstalledDir: /opt/aocc/bin/
    Selected GCC installation: /usr/lib/gcc/x86_64-pc-linux-gnu/10.2.0
    Candidate multilib: .;@m64
    Candidate multilib: 32;@m32
    Selected multilib: .;@m64

### [package.env]

Please see [[/etc/portage/package.env](https://wiki.gentoo.org/wiki//etc/portage/package.env "/etc/portage/package.env")] to see how [package.env] works.

`root `[`#`]`cd /etc/portage/env`

[FILE] **`/etc/portage/env/aocc.conf`**

    CC="clang"
    CXX="clang++"

    LDFLAGS="-fuse-ld=lld"

Add LLVM AR, NM and RANLIB if needed:

[FILE] **`/etc/portage/env/aocc.conf`**

    CC="clang"
    CXX="clang++"

    AR="llvm-ar"
    NM="llvm-nm"
    RANLIB="llvm-ranlib"

    LDFLAGS="-fuse-ld=lld"

If you don\'t wish to replace vanilla-clang via [/etc/env.d], AOCC can be used per-package with:

[FILE] **`/etc/portage/env/aocc.conf`**

    AOCC_PATH="/opt/aocc/bin/"

    CC="$clang"
    CXX="$clang++"

** Important**\
Plainly trusting in this method does not work with every ebuild inheriting *llvm.eclass*, ie [[[www-client/firefox]](https://packages.gentoo.org/packages/www-client/firefox)[]]

### [make.conf]

AOCC can be used globally by defining it in [make.conf]:

[FILE] **`/etc/portage/make.conf`**

    CC="clang"
    CXX="clang++"

    LDFLAGS="-fuse-ld=lld"

Please see [creating a GCC fallback environment](https://wiki.gentoo.org/wiki/LLVM/Clang#GCC_fallback_environment "LLVM/Clang").

** Note**\
Again if you don\'t wish to pollute your vanilla-clang, you can define `AOCC_PATH` in [make.conf] and use that.

### [llvm.eclass]

## [Switching to AOCC]

Please read the [#Installation](#Installation) part above. Continue from there, without choosing method of usage first.

Add following USE flags to your [/etc/portage/make.conf]

[FILE] **`/etc/portage/make.conf`**

    USE="clang compiler-rt default-compiler-rt default-libcxx libcxx libcxxabi libunwind"

Compile LLVM/clang toolchain with your (working) system default compiler first:

`root `[`#`]`emerge -1avt clang llvm libcxx libcxxabi compiler-rt libunwind lld`

After it is done, switch to AOCC:

** Important**\
These are pretty aggressive settings, AOCC can be used without `-stdlib=libc++, -rtlib=compiler-rt -unwindlib=libunwind` etc.

[FILE] **`/etc/portage/make.conf`**

    AOCC_PATH="/opt/aocc-compiler-2.3.0/bin/"

    CC="$clang"
    CXX="$clang++"

    BUILD_CC="$"
    BUILD_CXX="$"

    CFLAGS="-march=native -O2 -pipe"
    CXXFLAGS="-stdlib=libc++ $"
    LDFLAGS="-fuse-ld=lld -rtlib=compiler-rt -unwindlib=libunwind"

** Tip**\
Add rest of LLVM tools if desired needed.

[FILE] **`/etc/portage/make.conf`**

    AR="$llvm-ar"
    NM="$llvm-nm"
    RANLIB="$llvm-ranlib"

** Important**\
Set up GCC fallback for packages which won\'t compile with clang!

[FILE] **`/etc/portage/env/compiler-gcc.conf`**

    CC="gcc"
    CXX="g++"
    CXXFLAGS="$"
    LDFLAGS=""

[FILE] **`/etc/portage/env/ldflags-lgcc_s.conf`**

    LDFLAGS="$ -lgcc_s"

[FILE] **`/etc/portage/env/ldflags-lm.conf`**

    LDFLAGS="$ -lm"

And add known packages to workaround-list:

[FILE] **`/etc/portage/package.env`**

    ### system-clang
    ###

    # Doesn't compile with clang and needs gcc
    dev-libs/elfutils compiler-gcc.conf
    dev-libs/libgcrypt compiler-gcc.conf
    dev-libs/popt compiler-gcc.conf
    sys-apps/busybox compiler-gcc.conf
    sys-apps/sandbox compiler-gcc.conf
    sys-apps/sysvinit compiler-gcc.conf
    sys-boot/efibootmgr compiler-gcc.conf
    sys-devel/gcc compiler-gcc.conf
    sys-libs/binutils-libs compiler-gcc.conf
    sys-libs/glibc compiler-gcc.conf

    # Needs -lgcc_s in LDFLAGS,
    # resolve __register_frame / __deregister_frame undefined symbols
    sys-devel/llvm ldflags-lgcc_s.conf

    # Needs -lm in LDFLAGS,
    # "undefined symbol: sqrt" and "undefined symbol: log10" link errors
    sys-devel/gettext ldflags-lm.conf

** Note**\
Depending on your installed packages, this list will most likely grow to match your system.

Rebuild clang.

`root `[`#`]`emerge -1avt clang llvm libcxx libcxxabi compiler-rt libunwind lld`

Check that your config works:

`root `[`#`]`cat /var/db/pkg/sys-devel/llvm-11.0.0/CC`

[CODE] **cat /var/db/pkg/sys-devel/llvm-11.0.0/CC**

    ''
    /opt/aocc-compiler-2.3.0/bin/clang

Rebuild your system.

`root `[`#`]`emerge -vt -e @world`

** Tip**\
Avoid using `--keep-going`, but `--resume` and `--resume --skipfirst` might come handy.

Please see the [original forum post](https://forums.gentoo.org/viewtopic-t-1102590-start-0.html) for where these steps came from.

** Note**\
This method is rather foolproof and keeps your system vanilla LLVM/clang separated from the AOCC, but it doesn\'t work with **every** package inheriting *llvm.eclass* in Gentoo. Mesa, Firefox and Thunderbird are problematic ones to name a few. They need local hacks to work with AOCC.

## [Troubleshooting]

### [][\"/opt/aocc/bin/clang: file not found!\"]

For some reason the symlink was wiped few times during `-e @world`. It seems to be related to packages calling `eselect compiler-shadow` during their **emerge**. There are a couple core packages doing so. Beware of this, and avoid using *\--keep-going*.

### [][\"error while loading shared libraries: libLLVM-11.so\"]

If you get an error saying *clang: error while loading shared libraries: libLLVM-11.so: cannot open shared object file: No such file or directory* you most likely attempted to symlink or override all system LLVM settings. Don\'t do that.

### [][multilib system, \"multilib-strict check failed!\"]

It seems like AOCC doesn\'t work very well on a [multilib](https://wiki.gentoo.org/wiki/Multilib "Multilib") system, might be due to missing i686 compatible compiler. Workarounds for using system-clang might be needed.

## [See also]

-   [AMD](https://wiki.gentoo.org/wiki/AMD "AMD") --- a semiconductor company. AMD is best known for producing CPUs based on [x86 intruction set](https://en.wikipedia.org/wiki/x86 "wikipedia:x86"), motherboard chipsets and their own line of GPUs.
-   [Clang](https://wiki.gentoo.org/wiki/LLVM/Clang "LLVM/Clang") --- a C/C++/Objective-C/C++, CUDA, and RenderScript language front-end for the LLVM project

## [External resources]

-   [Phoronix web](https://www.phoronix.com/scan.php?page=search&q=AOCC) presenting benchmarks between AOCC, clang and GCC
-   [AOCC 2.3 vs clang 11 vs GCC10](https://www.phoronix.com/scan.php?page=article&item=amd-aocc-23)