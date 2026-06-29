This page contains [[changes](https://wiki.gentoo.org/index.php?title=Crossdev&diff=1429324)] which are not marked for translation.

\

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Crossdev "Project:Crossdev")][Project](https://wiki.gentoo.org/wiki/Project:Crossdev "Project:Crossdev")

[[]][Package information](https://packages.gentoo.org/packages/sys-devel/crossdev)

[[]][GitWeb](https://gitweb.gentoo.org/proj/crossdev.git)

**Article status**

[[]]This article needs wikification.

**crossdev** is a set of [bash] scripts that utilize [emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge") to provide a system integrated cross-compilation capability.

A Gentoo ***host*** machine\'s toolchain is leveraged by compiling for the specified ***target***; by overriding several environment variables.^[\[1\]](#cite_note-1)[\[2\]](#cite_note-2)^

** Important**\
Crossdev does not create a cross compiler for a target that matches the host tuple, e.g. a host x86_64-pc-linux-musl and a target with the same name will fail. When compiling for the same architecture, just use a chroot.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
    -   [[1.2] [Crossdev overlay]](#Crossdev_overlay)
        -   [[1.2.1] [eselect creation]](#eselect_creation)
        -   [[1.2.2] [Manual creation]](#Manual_creation)
        -   [[1.2.3] [Repository search order]](#Repository_search_order)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
-   [[3] [Build packages with crossdev]](#Build_packages_with_crossdev)
    -   [[3.1] [Set up the base system]](#Set_up_the_base_system)
        -   [[3.1.1] [Manual build]](#Manual_build)
        -   [[3.1.2] [Stage3 tarball]](#Stage3_tarball)
    -   [[3.2] [Set profiles]](#Set_profiles)
    -   [[3.3] [Setting emerge options]](#Setting_emerge_options)
    -   [[3.4] [Emerge a single package]](#Emerge_a_single_package)
    -   [[3.5] [Emerge all the packages in system set]](#Emerge_all_the_packages_in_system_set)
    -   [[3.6] [Binary packages]](#Binary_packages)
-   [[4] [Advanced usage]](#Advanced_usage)
    -   [[4.1] [User Patches]](#User_Patches)
    -   [[4.2] [Toolchains for unsupported architectures]](#Toolchains_for_unsupported_architectures)
    -   [[4.3] [17.x to 23.0 migration]](#17.x_to_23.0_migration)
-   [[5] [Removal]](#Removal)
    -   [[5.1] [Unmerge]](#Unmerge)
-   [[6] [Gentoo\'s target tuples]](#Gentoo.27s_target_tuples)
-   [[7] [Troubleshooting]](#Troubleshooting)
-   [[8] [See also]](#See_also)
-   [[9] [References]](#References)

## [Installation]

### [Emerge]

`root `[`#`]`emerge --ask sys-devel/crossdev`

### [Crossdev overlay]

** Warning**\
Improperly using [crossdev] may \"pollute\" ebuild repositories: [crossdev] operates by adding packages to an ebuild repository, so care must be taken to ensure [crossdev] adds packages to a separate repository. Follow **one** of the creation methods below to create a separate repository for [crossdev].

#### [eselect creation]

To use [[eselect-repository]](https://wiki.gentoo.org/wiki/Eselect/Repository "Eselect/Repository") to create the repository, first install the package.

`root `[`#`]`emerge --ask app-eselect/eselect-repository`

Then, create the repository with:

`root `[`#`]`eselect repository create crossdev`

#### [Manual creation]

To manually create a `crossdev` repository:

`root `[`#`]`mkdir -p /var/db/repos/crossdev/ `

`root `[`#`]`echo 'crossdev' > /var/db/repos/crossdev/profiles/repo_name `

`root `[`#`]`echo 'masters = gentoo' > /var/db/repos/crossdev/metadata/layout.conf `

`root `[`#`]`chown -R portage:portage /var/db/repos/crossdev `

If the Gentoo ebuild repository is synchronized using Git, or any other method with Manifest files that do not include checksums for ebuilds, prevent \"masked by: corruption\" errors with:

[FILE] **`/var/db/repos/crossdev/metadata/layout.conf`**

    masters = gentoo
    thin-manifests = true

Instruct Portage, and subsequently crossdev, to use the new ebuild repository by enabling it:

[FILE] **`/etc/portage/repos.conf/crossdev.conf`**

    [crossdev]
    location = /var/db/repos/crossdev
    priority = 10
    masters = gentoo
    auto-sync = no

#### [Repository search order]

In order of precedence, [crossdev] will make use of a Portage repository specified by:

1.  The command-line option: `--ov-output` (`-oO`)
2.  `$`
3.  Repository with name `cross-$`
4.  Repository with name `crossdev`

## [Usage]

** Important**\
The `-S` option (for stable) should not be used on arches with no stable keywords or a mixed (unstable, inconsistent) profile, e.g. **[mips]** or **[riscv]**.

### [Invocation]

`user `[`$`]`crossdev --help`

    Usage: crossdev [options] --target TARGET

    Options:
        -L,  --llvm              Use LLVM/Clang as a cross compiler
        --b, --binutils ver      Specify version of binutils to use
        --g, --gcc ver           Specify version of gcc to use
        --k, --kernel ver        Specify version of kernel headers to use
        --l, --libc ver          Specify version of libc to use
                                    Note: versions support depend atom syntaxes:
                                     e.g. ">=2.20" "~4.6.1" "=2.13.1-r3"
        -A, --abis abis          Specify ABIs to build, first one is the default
        --host-abi abi           Specify the ABI of the compiler itself
        --env env                Specify env settings for all packages (see below)
        --[bdgkl]env env         Specify env settings for binutils/gdb/gcc/kernel/libc
                                    Note: make sure to quote: 'VAR="some value"\nFOO="cow"'
        --[bdgkl]cat category    Use binutils/gdb/gcc/kernel/libc package from category
        --[bdgkl]pkg pkg         Use binutils/gdb/gcc/kernel/libc package with given name
        -f, --force              I don't need a seat belt!
        -S, --stable             Use latest stable versions as default
        -C, --clean target       Uninstall specified target
        -P, --portage opts       Options to pass to emerge (see emerge(1))
        --with[out]-headers      Build C library headers before C compiler?
        --show-fail-log          If the build fails, dump the failing log

    Overlay Options:
        -oS, --overlays list     Space delimited list of overlays to search
                                    [default: `portageq repositories_configuration`]
        -oO, --ov-output path    Parent directory of overlay to write crossdev package links
                                    [default: uses repo with name 'crossdev', or
                                     'cross-$', or falls back to first
                                     from --overlays list]
        -ob, --ov-binutils path  Overlay for binutils ebuilds [default: search]
        -od, --ov-gdb path       Overlay for gdb ebuilds [default: search]
        -og, --ov-gcc path       Overlay for gcc ebuilds [default: search]
        -ok, --ov-kernel path    Overlay for kernel ebuilds [default: search]
        -ol, --ov-libc path      Overlay for C library ebuilds [default: search]
        -ox, --ov-extra path     Overlay for extra packages [default: search]

    Stage Options:
        -s0, --stage0            Build just binutils
        -s1, --stage1            Also build a bare C compiler (no C library/
                                    C++/shared GCC libs/C++ exceptions/etc...)
        -s2, --stage2            Also build kernel headers
        -s3, --stage3            Also build the C library
        -s4, --stage4            Also build a full compiler [default]
                                    (shared libs GCC/various lang frontends/etc...)

    External Tooling Options:
        --show-target-cfg        Display target settings that crossdev will use
        --init-target            Setup config/overlay/etc... files only

    Extra Fun (must be run after above stages):
        --ex-only                Skip the stage steps above
        --ex-gcc                 Build extra gcc targets (gcj/ada/etc...)
        --ex-gdb                 Build a cross gdb
        --ex-pkg pkg             Build extra packages (may be used multiple times)

    LLVM/Clang Specific Options (--llvm):
        --r, --crt ver           Specify version of compiler-rt to use
        --c, --ccw ver           Specify version of clang-crossdev-wrapper to use
        --[rc]env env            Specify env settings for compiler-rt/clang-crossdev-wrapper
        --[rc]cat category       Use compiler-rt/clang-crossdev-wrapper package from category
        --[rc]pkg pkg            Use compiler-rt/clang-crossdev-wrapper package with given name
        -or, --ov-crt path       Overlay for compiler-rt ebuilds [default: search]
        -oc, --ov-ccw path       Overlay for clang-crossdev-wrapper ebuilds [default: search]

    Target (-t) takes a tuple ARCHITECTURE-VENDOR-OS-LIBC; see 'crossdev -t help'

To see the supported architectures, C libraries, and special targets:

`user `[`$`]`crossdev --target help`

    Target (-t) takes a tuple ARCHITECTURE-VENDOR-OS-LIBC:

    Supported Architectures (ARCHITECTURE):
       - alpha
       - arm / armeb / aarch64
       - hppa (parisc)
       - ia64
       - i386 / i486 / i586 / i686 (x86)
       - m68k
       - mips / mipsel / mips64 / mips64el
       - or1k
       - powerpc (ppc) / powerpc64 (ppc64)
       - riscv32 / riscv64
       - sparc / sparc64
       - s390 / s390x
       - sh / sh[1-5] / sh64
       - x86_64 (amd64)
    Supported C Libraries (LIBC):
       - glibc (gnu)
       - klibc       [prob wont work]
       - musl
       - newlib      [bare metal/no operating system]
       - uclibc      [not all arches are ported]
    Special Targets (full tuple):
       - avr      http://www.nongnu.org/avr-libc/
       - bfin     http://blackfin.uclinux.org/
       - h8300    http://h8300-hms.sourceforge.net/
       - mingw64  http://mingw-w64.sourceforge.net/
       - mmix     http://www-cs-faculty.stanford.edu/~knuth/mmix.html
       - msp430   http://www.ti.com/msp430
       - nds32    http://github.com/nds32
       - nios2    http://www.altera.com/products/ip/processors/nios2/ni2-index.html
       - xc16x    http://www.infineon.com/
       - ppu / spu (cell) [Cell/Playstation 3 targets]
    Softfloat toolchains:
       Include 'softfloat' in the 'vendor' field
       e.g. armeb-softfloat-linux-uclibc  powerpc-booya_softfloat-linux-gnu

To build a cross toolchain, specify the target with the `--target` flag, such as:

`root `[`#`]`crossdev --target aarch64-unknown-linux-gnu`

To use the host LLVM toolchain as a cross compiler instead of compiling a target specific GCC toolchain, use the `--llvm` flag.

`root `[`#`]`crossdev --llvm --target aarch64-gentoo-linux-musl`

** Important**\
It is currently not possible to compile glibc with LLVM/Clang, therefore any -gnu triplet will fail with the `--llvm` flag. There are also several CPU architectures not fully supported by the compiler-rt builtins library, which is needed for LLVM crossdev.

** Note**\
C++ and unwinding is currently not supported by LLVM crossdev, but it is planned for the near future. It is therefore recommended to set `USE="-cxx"` in the meantime.

## [Build packages with crossdev]

To cross compile packages it is now possible to use [\$CHOST-emerge], using an aarch64 glibc cross compiler it would look like [aarch64-unknown-linux-gnu-emerge] then use Portage\'s commands as normal.

### [Set up the base system]

Crossdev sets up only the cross compiler and runtime. By itself, it doesn\'t install the base system or any libraries.

There are two ways to set up a base crossdev environment:

-   Manual build of the base system. It works well for GCC-based environments, but has no guarantee to work with LLVM-based ones, **or**
-   Using a stage3 tarball.

#### [Manual build]

Manual build consists of installation of [glibc] and [\@system] without recording them in [\@world].

`root `[`#`]`USE=build aarch64-unknown-linux-gnu-emerge -v1 baselayout `

`root `[`#`]`aarch64-unknown-linux-gnu-emerge -v1 sys-libs/glibc `

`root `[`#`]`aarch64-unknown-linux-gnu-emerge -v1 @system `

#### [Stage3 tarball]

First, download a desired stage3 archive, which matches your architecture and environment. For [aarch64-unknown-linux-musl], that would be:

`root `[`#`]`wget `[`https://gentoo.osuosl.org/releases/arm64/autobuilds/current-stage3-arm64-musl-llvm/stage3-arm64-musl-llvm-XXXXXXXXXXXXXXXX.tar.xz`](https://gentoo.osuosl.org/releases/arm64/autobuilds/current-stage3-arm64-musl-llvm/stage3-arm64-musl-llvm-XXXXXXXXXXXXXXXX.tar.xz)` -O stage3-arm64-musl-llvm-latest.tar.xz`

Then unpack it into the target root directory (which **must be empty**):

`root `[`#`]`tar -xJpf stage3-arm64-musl-llvm-latest.tar.xz -C /usr/aarch64-unknown-linux-musl --exclude=dev --skip-old-files`

### [Set profiles]

Profiles can be set like on normal system by doing the following.

First, list the available profiles:

`root `[`#`]`PORTAGE_CONFIGROOT=/usr/aarch64-unknown-linux-gnu eselect profile list `

      [1]  default/linux/arm64/23.0 (exp) *
      [2]  default/linux/arm64/23.0/hardened (exp)
      [3]  default/linux/arm64/23.0/hardened/selinux (exp)
      [4]  default/linux/arm64/23.0/hardened/selinux/systemd (exp)
      [5]  default/linux/arm64/23.0/desktop (exp)
      [6]  default/linux/arm64/23.0/desktop/gnome (exp)
      [7]  default/linux/arm64/23.0/desktop/gnome/systemd (exp)
      [8]  default/linux/arm64/23.0/desktop/plasma (exp)
      [9]  default/linux/arm64/23.0/desktop/plasma/systemd (exp)
      [10]  default/linux/arm64/23.0/desktop/systemd (exp)
      [11]  default/linux/arm64/23.0/systemd (exp)
      [12]  default/linux/arm64/23.0/llvm (exp)
      [13]  default/linux/arm64/23.0/llvm/systemd (exp)
      [14]  default/linux/arm64/23.0/split-usr (exp)
      [15]  default/linux/arm64/23.0/split-usr/hardened (exp)
      [16]  default/linux/arm64/23.0/split-usr/hardened/selinux (exp)
      [17]  default/linux/arm64/23.0/split-usr/desktop (exp)
      [18]  default/linux/arm64/23.0/split-usr/desktop/gnome (exp)
      [19]  default/linux/arm64/23.0/split-usr/desktop/plasma (exp)
      [20]  default/linux/arm64/23.0/split-usr/llvm (exp)
      [21]  default/linux/arm64/23.0/big-endian (exp)
      [23]  default/linux/arm64/23.0/big-endian/systemd (exp)
      [24]  default/linux/arm64/23.0/split-usr/big-endian (exp)
      [25]  default/linux/arm64/23.0/musl (exp)
      [26]  default/linux/arm64/23.0/musl/llvm (exp)
      [27]  default/linux/arm64/23.0/musl/hardened (exp)
      [28]  default/linux/arm64/23.0/musl/hardened/selinux (exp)
      [29]  default/linux/arm64/23.0/split-usr/musl (exp)
      [30]  default/linux/arm64/23.0/split-usr/musl/llvm (exp)
      [31]  default/linux/arm64/23.0/split-usr/musl/hardened (exp)
      [32]  default/linux/arm64/23.0/split-usr/musl/hardened/selinux (exp)

Then pick the required profile for the system needs.

`root `[`#`]`PORTAGE_CONFIGROOT=/usr/aarch64-unknown-linux-gnu eselect profile set default/linux/arm64/23.0`

### [Setting emerge options]

[crossdev] allows the same configuration as [/etc/portage] by editing `make.conf, package.use, package.accept_keywords` etc in the [/usr/aarch64-unknown-linux-gnu/etc/portage] directory. See Portage documentation for more information.

### [Emerge a single package]

To emerge a single package then just run:

`root `[`#`]`emerge-aarch64-unknown-linux-gnu --ask app-editors/nano`

Replacing the package with the one required for the system.

### [Emerge all the packages in system set]

To emerge all packages in `@system` then run:

`root `[`#`]`emerge-aarch64-unknown-linux-gnu --ask --verbose --oneshot @system`

### [Binary packages]

By default crossdev will create packages in [/usr/aarch64-unknown-linux-gnu/var/cache/binpkgs] which can be used to set up a [Binary Host](https://wiki.gentoo.org/wiki/Binary_package_guide "Binary package guide") to install packages on a much weaker system which would take days, if not weeks otherwise.

## [Advanced usage]

### [User Patches]

Because crossdev makes the ebuilds via symlinks, the default patch directory becomes [/etc/portage/patches/cross-\$/\$/]. For example, to apply [foobar.patch] to [[[sys-libs/glibc]](https://packages.gentoo.org/packages/sys-libs/glibc)[]] on the target system, the patch file should be placed in in [/etc/portage/patches/cross-aarch64-unknown-linux-gnu/glibc/foobar.patch].

### [Toolchains for unsupported architectures]

Sometimes a user needs to build a cross compiler for a CPU arch which isn\'t supported by Gentoo however the toolchain does.

Visit [packages.gentoo.org](http://Packages.gentoo.org) and find the current versions for the packages [[[sys-devel/binutils]](https://packages.gentoo.org/packages/sys-devel/binutils)[]], [[[sys-devel/gcc]](https://packages.gentoo.org/packages/sys-devel/gcc)[]] and [[[sys-libs/glibc]](https://packages.gentoo.org/packages/sys-libs/glibc)[]] or [[[sys-libs/musl]](https://packages.gentoo.org/packages/sys-libs/musl)[]].

  ---------- ------------------
  GCC        14.1.1_p20240622
  Binutils   2.42-r2
  Glibc      2.39-r9
  ---------- ------------------

With these version we can force crossdev to use the required versions in this usage case with the following:

`root `[`#`]`ACCEPT_KEYWORDS="**" crossdev -s4 --binutils 2.42-r2 --libc 2.39-r9 --gcc 14.1.1_p20240622 sh4-unknown-linux-gnu`

**ACCEPT_KEYWORDS=\"\*\*\"** Tells portage to temporarily accept any architecture keyword.

**\--binutils** Explicitly set the binutils version

**\--gcc** Explicitly set the GCC version

**\--libc** Explicitly set the Glibc or musl version (crossdev selects the correct libc based on the triple provided.)

**sh4-unknown-linux-gnu** Triple required for cross compiler.

This will build a very basic cross compiler without profile support.

### [17.x to 23.0 migration]

Users that have cross toolchain profiles created for 17.x profiles are recommend to delete the cross compiler and then recreate them again using a 23.0 profile to prevent multiple issues and assure the correct USE flags are set.

Please follow below for removal steps then see [Crossdev#Usage](https://wiki.gentoo.org/wiki/Crossdev#Usage "Crossdev") on how to create them again.

## [Removal]

** Important**\
Specifying the same [machine-vendor-kernel-operating system](https://wiki.gentoo.org/wiki/Embedded_Handbook/Tuples "Embedded Handbook/Tuples") as the host utils during removal could result in breakages that are irrecoverable without a proper backup method!

** Important**\
To remove a LLVM/Clang crossdev target you need to explicitly pass `--llvm`.

** Tip**\
Optionally, please see [make.conf](https://devmanual.gentoo.org/eclass-reference/make.conf/index.html) for setting up regular backups via binpkg & Portage\'s built-in features!

To remove a crossdev-generated toolchain, set the `--clean` flag **before** the `--target` flag using the target tuple to remove, for example:

`root `[`#`]`crossdev --clean --target arm-none-eabi`

     * Uninstalling target 'arm-none-eabi' ...
    *** unmerging cross-arm-none-eabi/newlib-4.1.0-r1
    *** unmerging cross-arm-none-eabi/binutils-2.37_p1-r1
    *** unmerging cross-arm-none-eabi/gcc-11.2.1_p20211127
     * gcc-config: Could not locate profile # !
    Cleaning up masquerade for ccache ...
    removed 'arm-none-eabi-gcc'
    removed 'arm-none-eabi-gcc-11.2.1'
     * Removing last cross-compiler instance. Deleting dangling symlinks.
    rm: cannot remove '/usr/arm-none-eabi/usr': Is a directory
    /usr/arm-none-eabi: directory still exists; remove recursively? [y/N] y

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose sys-devel/crossdev`

## [][Gentoo\'s target tuples]

Below is a list of the target tuples (the `CHOST` variable) utilized by Gentoo. For more examples for systems that take advantage of musl or time64, check the official Gentoo repository [here](https://github.com/gentoo/gentoo/tree/master/profiles/arch)

  ------------ ----------------------------------
  Arch         Tuple
  alpha        alpha-unknown-linux-gnu
  amd64        x86_64-pc-linux-gnu
  arm          arm-unknown-linux-gnu
  armv4        armv4l-unknown-linux-gnu
  armv4t       armv4tl-softfloat-linux-gnueabi
  armv5te      armv5tel-softfloat-linux-gnueabi
  armv6j       armv6j-unknown-linux-gnueabihf
  armv7a       armv7a-unknown-linux-gnueabihf
  arm64        aarch64-unknown-linux-gnu
  arm64-be     aarch64_be-unknown-linux-gnu
  hppa         hppa-unknown-linux-gnu
  hppa1.1      hppa1.1-unknown-linux-gnu
  hppa2.0      hppa2.0-unknown-linux-gnu
  loong        loongarch64-unknown-linux-gnu
  m68k         m68k-unknown-linux-gnu
  mips32       mips-unknown-linux-gnu
  mips64       mips64-unknown-linux-gnu
  mips64el     mips64el-unknown-linux-gnu
  ppc          powerpc-unknown-linux-gnu
  ppc64        powerpc64-unknown-linux-gnu
  ppc64le      powerpc64le-unknown-linux-gnu
  riscv        riscv64-unknown-linux-gnu
  riscv32      riscv32-unknown-linux-gnu
  s390         s390-ibm-linux-gnu
  s390x        s390x-ibm-linux-gnu
  sparc64      sparc64-unknown-linux-gnu
  sparc32      sparc-unknown-linux-gnu
  x86          i686-pc-linux-gnu
  x86 (i486)   i486-pc-linux-gnu
  ------------ ----------------------------------

Last updated: 2025-11-29

## [Troubleshooting]

While using crossdev emerge (eg. /usr/bin/emerge-i686-unknown-linux-gnu), error \"ERROR: 23.0 merged-usr profile, but disk is split-usr\" error.\

Solution, convert split layout crossdev /usr/i686-unknown-linux-gnu sub-directories into using symbolic linked directories.\

\# emerge sys-apps/merge-usr\
\# merge-usr \--prefix /usr/i686-unknown-linux-gnu \--dryrun\
\
If satisfied, execute without dryrun option.\

## [See also]

-   [ARM](https://wiki.gentoo.org/wiki/ARM "ARM") --- compiling code for an ARM processor, taking advantage of its [FPU](https://en.wikipedia.org/wiki/Floating-point_unit "wikipedia:Floating-point unit").
-   [Catalyst](https://wiki.gentoo.org/wiki/Catalyst "Catalyst") --- a tool to build [stage files](https://wiki.gentoo.org/wiki/Stage_file "Stage file") and [live-images](https://wiki.gentoo.org/wiki/Live_image "Live image") for Gentoo
-   [Creating a cross-compiler (Embedded Handbook)](https://wiki.gentoo.org/wiki/Embedded_Handbook/General/Creating_a_cross-compiler "Embedded Handbook/General/Creating a cross-compiler")
-   [Joshua Kinard (kumba)](https://wiki.gentoo.org/wiki/User:Kumba "User:Kumba")  - original crossdev author.

## [References]

1.  [[[↑](#cite_ref-1)] [Gentoo Gitweb: [\"Crossdev Script\"](https://gitweb.gentoo.org/proj/crossdev.git/tree/crossdev)]]
2.  [[[↑](#cite_ref-2)] [crossdev was originally written by: [Joshua Kinard (kumba)](https://wiki.gentoo.org/wiki/User:Kumba "User:Kumba") ]]