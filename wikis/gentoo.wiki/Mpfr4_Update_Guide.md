[[[dev-libs/mpfr]](https://packages.gentoo.org/packages/dev-libs/mpfr)[]] version 4 introduced an ABI and soname change that has the potential of breaking the compiler toolchain. In order to minimize potential problems it is strongly recommended to rebuild [[[dev-libs/mpc]](https://packages.gentoo.org/packages/dev-libs/mpc)[]] and [[[sys-devel/gcc]](https://packages.gentoo.org/packages/sys-devel/gcc)[]] immediately after mpfr.

## Contents

-   [[1] [The problem]](#The_problem)
-   [[2] [Preparatory steps]](#Preparatory_steps)
-   [[3] [Detailed upgrade steps]](#Detailed_upgrade_steps)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Mixed linkage]](#Mixed_linkage)
    -   [[4.2] [Warning about preserved libraries]](#Warning_about_preserved_libraries)
    -   [[4.3] [Missing mpfr-4 library]](#Missing_mpfr-4_library)

### [The problem]

[libmpfr.so] is used by [libmpc.so] (provided by [[[dev-libs/mpc]](https://packages.gentoo.org/packages/dev-libs/mpc)[]]), as well as internal executables (e.g. [cc1], [cc1plus]) of [[[sys-devel/gcc]](https://packages.gentoo.org/packages/sys-devel/gcc)[]]. Appropriate subslots in mpfr and slot-operators in dependencies in mpc and gcc will cause a rebuild of mpc and gcc after an upgrade of mpfr.

However, after [[[dev-libs/mpfr]](https://packages.gentoo.org/packages/dev-libs/mpfr)[]] version 4 is installed and [[[dev-libs/mpc]](https://packages.gentoo.org/packages/dev-libs/mpc)[]] rebuilt, but **before** [[[sys-devel/gcc]](https://packages.gentoo.org/packages/sys-devel/gcc)[]] is rebuilt, the gcc compiler will be in an inconsistent state wherein symbols from incorrect library versions of mpfr might get used. This can result in segmentation faults and internal compiler errors. It is therefore important to rebuild gcc immmediately after mpc.

### [Preparatory steps]

Make sure that you have enabled the \"preserved libs\" feature:

`user `[`$`]`emerge --info | grep preserve-libs `

    FEATURES="... preserve-libs ..."

### [Detailed upgrade steps]

Update and rebuild all affected packages as atomically as possible:

`root `[`#`]`emerge --ask --oneshot ">=dev-libs/mpfr-4" dev-libs/mpc sys-devel/gcc`

Check that [cc1] is dynamically linked against the new mpfr version. First identify the absolute path of the [cc1] executable by running

`user `[`$`]`qlist gcc | grep -P "cc1$"`

    /usr/libexec/gcc/x86_64-pc-linux-gnu/7.3.0/cc1

Then, use ldd to list all dynamically linked libraries:

`user `[`$`]`ldd /usr/libexec/gcc/x86_64-pc-linux-gnu/7.3.0/cc1 | grep mpfr`

            libmpfr.so.6 => /usr/lib64/libmpfr.so.6 (0x00007fe37e9df000)

You might want to use this ldd invocation to list all dynamically linked libraries for any installed gcc compilers:

`user `[`$`]`for i in /usr/libexec/gcc/*-pc-linux-gnu/*/cc1; do echo $i; ldd $i | grep mpfr ; done;`

    /usr/libexec/gcc/i686-pc-linux-gnu/6.4.0/cc1
            libmpfr.so.6 => /usr/lib/libmpfr.so.6 (0xf7747000)
    /usr/libexec/gcc/i686-pc-linux-gnu/7.3.0/cc1
            libmpfr.so.6 => /usr/lib/libmpfr.so.6 (0xf7b70000)
    /usr/libexec/gcc/x86_64-pc-linux-gnu/7.3.0/cc1
            libmpfr.so.6 => /usr/lib/libmpfr.so.6 (0xf7797000)

You should only see [libmpfr.so.6] and **not** the old [libmpfr.so.4] in the output of ldd.

## [Troubleshooting]

### [Mixed linkage]

If the ldd command in the previous step returns two library versions,

`user `[`$`]`ldd /usr/libexec/gcc/x86_64-pc-linux-gnu/7.3.0/cc1 | grep mpfr`

            libmpfr.so.4 => /usr/lib64/libmpfr.so.4 (0x00007fe37fa02000)
            libmpfr.so.6 => /usr/lib64/libmpfr.so.6 (0x00007fe37e9df000)

You have rebuilt [[[sys-libs/mpc]](https://packages.gentoo.org/packages/sys-libs/mpc)[]] against the new mpfr version, but not [[[sys-devel/gcc]](https://packages.gentoo.org/packages/sys-devel/gcc)[]] (or vice versa). Rebuild the mpc library and the gcc executable immediately:

`root `[`#`]`emerge --ask --oneshot dev-libs/mpc sys-devel/gcc`

### [Warning about preserved libraries]

If you get the following warning you had the preserve-libs feature disabled:

     * Messages for package dev-libs/mpfr-4.0.1:

     * Old versions of installed libraries were detected on your system.
     * In order to avoid breaking packages that depend on these old libs,
     * the libraries are not being removed.  You need to run revdep-rebuild
     * in order to remove these old dependencies.  If you do not have this
     * helper program, simply emerge the 'gentoolkit' package.
     *
     *   # revdep-rebuild --library '/usr/lib64/libmpfr.so.4' && rm '/usr/lib64/libmpfr.so.4

Follow above instructions immediately and check that the link interface is consistent before you remove the [libmpfr.so.4] library. [ldd] must return exactly one mpfr library:

`user `[`$`]`ldd /usr/libexec/gcc/x86_64-pc-linux-gnu/7.3.0/cc1 | grep mpfr`

            libmpfr.so.6 => /usr/lib64/libmpfr.so.6 (0x00007fe37e9df000)

\

### [Missing mpfr-4 library]

If you encounter internal compiler errors of the form

`/usr/libexec/gcc/x86_64-pc-linux-gnu/7.3.0/cc1plus: error while loading shared libraries: libmpfr.so.4: cannot open shared object file: No such file or directory`

The [libmpfr.so.4] library got removed before mpc and gcc had been both rebuilt. The preserve-libs feature and the manual check mentioned above should have prevented this.

There is a workaround to bring the system back into working order:

** Warning**\
This is a very fragile workaround and only meant as last resort. Under normal circumstances, you should refrain from changing sonames in such manner.

`root `[`#`]` ln -s /usr/lib64/libmpfr.so.6 /usr/lib64/libmpfr.so.4`

`root `[`#`]` emerge --ask --oneshot dev-libs/mpc sys-devel/gcc`

`root `[`#`]` rm /usr/lib64/libmpfr.so.4`

`root `[`#`]` revdep-rebuild`

Make sure that the link interface is consistent after above steps:

`user `[`$`]`ldd /usr/libexec/gcc/x86_64-pc-linux-gnu/7.3.0/cc1 | grep mpfr`

            libmpfr.so.6 => /usr/lib64/libmpfr.so.6 (0x00007fe37e9df000)