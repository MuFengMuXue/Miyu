This article covers bootstraping [Rust](https://wiki.gentoo.org/wiki/Rust "Rust") for a [LLVM](https://wiki.gentoo.org/wiki/LLVM "LLVM") profile using a (non-LLVM) [Stage 3 file](https://wiki.gentoo.org/wiki/Stage_file#Stage_3 "Stage file").

\

## Contents

-   [[1] [Precondition]](#Precondition)
-   [[2] [Setting up a Build-Environment]](#Setting_up_a_Build-Environment)
    -   [[2.1] [Getting a Stage File]](#Getting_a_Stage_File)
    -   [[2.2] [Entering the Environment]](#Entering_the_Environment)
        -   [[2.2.1] [Option 1: via Chroot]](#Option_1:_via_Chroot)
        -   [[2.2.2] [Option 2: via Podman]](#Option_2:_via_Podman)
    -   [[2.3] [Configuring Portage]](#Configuring_Portage)
    -   [[2.4] [Veryfing the Profile]](#Veryfing_the_Profile)
-   [[3] [Building Rust]](#Building_Rust)
    -   [[3.1] [Building Rust with stdlibc++]](#Building_Rust_with_stdlibc.2B.2B)
    -   [[3.2] [Building Rust with libc++]](#Building_Rust_with_libc.2B.2B)
        -   [[3.2.1] [Select the corresponding llvm profile]](#Select_the_corresponding_llvm_profile)
        -   [[3.2.2] [Emerge llvm-core/clang-runtime]](#Emerge_llvm-core.2Fclang-runtime)
        -   [[3.2.3] [Confirm working default-libcxx]](#Confirm_working_default-libcxx)
        -   [[3.2.4] [Rebuild the toolchain]](#Rebuild_the_toolchain)
        -   [[3.2.5] [Rebuild Rust & create a binary package]](#Rebuild_Rust_.26_create_a_binary_package)
-   [[4] [Installing Rust]](#Installing_Rust)
    -   [[4.1] [Optional: Rebuilding with custom USE-flags]](#Optional:_Rebuilding_with_custom_USE-flags)
-   [[5] [See Also]](#See_Also)

## [Precondition]

On LLVM-based systems using musl, packages may break if dev-lang/rust-bin is the active Rust installation, and it is therefore masked ([bug #912154](https://bugs.gentoo.org/show_bug.cgi?id=912154)). Emerge dev-lang/rust requires a Rust installation, which leads to a circular dependency that cannot be resolved.

Verify that the profile is a musl/llvm profile:

`root `[`#`]`eselect profile list`

    Available profile symlink targets:
      [46]  default/linux/arm64/23.0/musl/llvm (exp) *

## [Setting up a Build-Environment]

### [Getting a Stage File]

Choose a [Stage 3 file](https://wiki.gentoo.org/wiki/Stage_file#Stage_3 "Stage file") that matches the architecture and profile, but does not use LLVM: e.g.

-   `default/linux/arm64/23.0/musl/llvm` -\> `default/linux/arm64/23.0/musl`
-   `default/linux/amd64/23.0/musl/llvm` -\> `default/linux/amd64/23.0/musl`
-   \...

Before downloading the stage file, the current directory should be set to the location where the environment shall be set up:

`user `[`$`]`mkdir ~/gentoo-rootfs`

`user `[`$`]`cd ~/gentoo-rootfs`

Once downloaded, [extract](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Stage#Installing_a_stage_file "Handbook:AMD64/Installation/Stage") the stage file:

`user `[`$`]`fakeroot tar xpvf stage3-*.tar.xz --xattrs-include='*.*' --numeric-owner`

### [Entering the Environment]

One thing still remains to be done before entering the new environment and that is copying over the DNS information in /etc/resolv.conf.

`user `[`$`]`cp --dereference /etc/resolv.conf ./etc`

#### [Option 1: via Chroot]

As described in the [Chrooting](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Chrooting "Handbook:AMD64/Installation/Base") section in the handbook.

#### [Option 2: via Podman]

`user `[`$`]`podman run -it --rootfs $(pwd) /bin/bash`

### [Configuring Portage]

Install a snapshot of the Gentoo ebuild repository

`root `[`#`]`emerge-webrsync`

### [Veryfing the Profile]

Verify that the profile is a musl, non-llvm profile:

`root `[`#`]`eselect profile list`

    Available profile symlink targets:
      [25]  default/linux/arm64/23.0/musl (dev) *

## [Building Rust]

### [][Building Rust with stdlibc++]

First a working setup with rust and llvm is built.

`root `[`#`]`emerge --ask llvm-core/clang llvm-core/llvm llvm-runtimes/compiler-rt llvm-runtimes/libunwind llvm-core/lld dev-lang/rust`

### [][Building Rust with libc++]

Then switch the toolchain to `default-libcxx`.

#### [Select the corresponding llvm profile]

`root `[`#`]`eselect profile list`

      [25]  default/linux/arm64/23.0/musl (dev) *
      [26]  default/linux/arm64/23.0/musl/llvm (exp)

`root `[`#`]`eselect profile set 26`

    !!! Warning: Profile default/linux/arm64/23.0/musl/llvm is experimental

#### [][Emerge `llvm-core/clang-runtime`]

The USE-flags `default-compiler-rt`, `default-libcxx`, `default-lld` and `llvm-libunwind` are set by the profile.

`root `[`#`]`emerge --ask llvm-runtimes/clang-runtime`

    [ebuild   R    ] llvm-runtimes/libunwind USE="static-libs*"
    [ebuild  N     ] llvm-runtimes/libcxxabi USE="(clang) static-libs -test -verify-sig"
    [ebuild  N     ] llvm-runtimes/libcxx    USE="(clang) (libcxxabi) static-libs -test -verify-sig"
    [ebuild   R    ] llvm-runtimes/clang-runtime USE="(default-compiler-rt*) (default-libcxx*) (default-lld*) libcxx* (llvm-libunwind*) -sanitize*"

** Note**\
If there is no profile or switching profile is not possible, follow [Bootstrapping the LLVM toolchain](https://wiki.gentoo.org/wiki/LLVM#Bootstrapping_the_LLVM_toolchain "LLVM")

#### [Confirm working `default-libcxx`]

`user `[`$`]`cat > test.cpp <<'EOF'`

    #include <iostream>
    int main()
    EOF

`user `[`$`]`clang++ test.cpp`

`user `[`$`]`ldd ./a.out | grep -E 'libc\+\+|libstdc\+\+' `

           libc++.so.1 => /lib/libc++.so.1 (0xffff95926000)
           libc++abi.so.1 => /lib/libc++abi.so.1 (0xffff958d5000)

** Warning**\
If you see `libstdc++.so.6` the toolchain is still using stdlibc++

#### [Rebuild the toolchain]

`root `[`#`]`emerge --ask llvm-core/clang llvm-core/llvm llvm-runtimes/libcxx llvm-runtimes/libcxxabi llvm-runtimes/compiler-rt llvm-runtimes/compiler-rt-sanitizers llvm-runtimes/libunwind llvm-core/lld`

#### [][Rebuild Rust & create a binary package]

Emerge Rust with the new toolchain and USE-flags and [build a binary package](https://wiki.gentoo.org/wiki/Binary_package_guide#Using_--buildpkg_as_an_emerge_optionbuild_a_package "Binary package guide"):

`root `[`#`]`emerge --ask --buildpkg dev-lang/rust`

    [ebuild   R    ] dev-lang/rust USE="(llvm-libunwind*)"

## [Installing Rust]

Leave the build environment

`root `[`#`]`exit`

Backup the hosts package cache

`root `[`#`]`[ -d /var/cache/binpkgs ] && mv /var/cache/binpkgs /var/cache/binpkgs-tmp`

Copy the build environment package cache to the host

`root `[`#`]`cp -r ./var/cache/binpkgs /var/cache/binpkgs`

Install Rust

`root `[`#`]`emerge --ask --usepkgonly dev-lang/rust`

Remove the cache

`root `[`#`]`rm -r /var/cache/binpkgs`

Restore the hosts package cache

`root `[`#`]`[ -d /var/cache/binpkgs-tmp ] && mv /var/cache/binpkgs-tmp /var/cache/binpkgs`

### [Optional: Rebuilding with custom USE-flags]

Once installed, rebuild Rust with the desired USE-flags.

## [See Also]

-   [Rust](https://wiki.gentoo.org/wiki/Rust "Rust") --- a general-purpose, multi-paradigm, compiled, programming language.
-   [LLVM](https://wiki.gentoo.org/wiki/LLVM "LLVM") --- a collection of modular and reusable compiler and toolchain technologies
-   [Musl](https://wiki.gentoo.org/wiki/Musl "Musl") --- a [standard C library](https://wiki.gentoo.org/wiki/Libc "Libc") implementation that strives to be lightweight and correct in the sense of standards
-   [Bootstrapping_Rust_via_cross_compilation](https://wiki.gentoo.org/wiki/Bootstrapping_Rust_via_cross_compilation "Bootstrapping Rust via cross compilation") --- covers using [crossdev](https://wiki.gentoo.org/wiki/Crossdev "Crossdev") to bootstrap [Rust](https://wiki.gentoo.org/wiki/Rust "Rust") for a specific architecture