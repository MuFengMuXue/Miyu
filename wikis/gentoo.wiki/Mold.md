**Resources**

[[]][GitHub](https://github.com/rui314/mold)

[[]][Package information](https://packages.gentoo.org/packages/sys-devel/mold)

**mold** is a linker that aims to provide drop-in compatibility with existing Unix linkers. It is many times faster than the BFD linker from GNU\'s [binutils](https://wiki.gentoo.org/wiki/Binutils "Binutils") and slightly faster than the [LLD linker](https://wiki.gentoo.org/wiki/LLVM/LLD "LLVM/LLD") from [LLVM](https://wiki.gentoo.org/wiki/LLVM "LLVM") in some use cases. Its speed is achieved through the usage of optimized data structures and parallelization.^[\[1\]](#cite_note-1)^ mold is still in the early stages of development and as features are added to be on par with the other linkers^[\[2\]](#cite_note-2)^, this could affect the speedy nature of mold.

** Note**\
LTO (Link-time optimization) support has been added since mold-1.1.1.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [GCC 12+ & Clang]](#GCC_12.2B_.26_Clang)
    -   [[2.2] [GCC 11]](#GCC_11)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Package fails to build using mold]](#Package_fails_to_build_using_mold)
    -   [[3.2] [Failed llvm lto with mold]](#Failed_llvm_lto_with_mold)
-   [[4] [See also]](#See_also)
-   [[5] [References]](#References)

## [[] Installation]

### [[] Emerge]

The mold linker is in the Gentoo package repository and can be installed using the following command:

`root `[`#`]`emerge --ask sys-devel/mold`

## [[] Usage]

### [][[] GCC 12+ & Clang]

[GCC 12+](https://wiki.gentoo.org/wiki/C "C") and [Clang](https://wiki.gentoo.org/wiki/LLVM/Clang "LLVM/Clang") support adding `-fuse-ld=mold` to `LDFLAGS` in the [[make.conf]](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf") file so that [mold] is used to link all packages:

[FILE] **`/etc/portage/make.conf`**

    LDFLAGS="$ -fuse-ld=mold"

### [[] GCC 11]

** Note**\
As of 2022-09-15, the following patch does not apply cleanly to gcc 11.3.1_p20220909.

A [patch](https://gist.github.com/00-matt/dda791a36318bafb68576b8576b1d283/raw/fuse-ld-mold.patch) that allows GCC 11 to invoke mold as a linker is also available. The patch can be placed in [/etc/portage/patches](https://wiki.gentoo.org/wiki//etc/portage/patches "/etc/portage/patches"):

`root `[`#`]`mkdir -p /etc/portage/patches/sys-devel/gcc-11.2.1_p20211127 `

`root `[`#`]`curl -Lo /etc/portage/patches/sys-devel/gcc-11.2.1_p20211127/fuse-ld-mold.patch \`\
`    https://gist.github.com/00-matt/dda791a36318bafb68576b8576b1d283/raw/fuse-ld-mold.patch`

## [[] Troubleshooting]

### [[] Package fails to build using mold]

Some packages do not build with mold (see [[[bug #830404]](https://bugs.gentoo.org/show_bug.cgi?id=830404)[]] for a list). An [environment](https://wiki.gentoo.org/wiki//etc/portage/package.env "/etc/portage/package.env") can be created to selectively disable it for some packages:

[FILE] **`/etc/portage/env/no-mold`**

    LDFLAGS="-Wl,-O1 -Wl,--as-needed"

[FILE] **`/etc/portage/package.env`**

    # mold does not support linker scripts; it cannot be used to link the kernel
    sys-kernel/vanilla-kernel no-mold

### [[] Failed llvm lto with mold]

If some packages fail to build in report-LLVMgold.so cannot open shared subject, when you declare -flto and -fuse-ld=mold. Then you probably lack LLVMgold (linker plugin) which can make you secure.

`root `[`#`]`emerge --ask llvm-core/llvm[binutils-plugin]`

## [[] See also]

-   [Gold](https://wiki.gentoo.org/wiki/Gold "Gold") --- a linker intended as a replacement for the [ld.bfd] linker.

## [[] References]

1.  [[[↑](#cite_ref-1)] [[Why is mold so fast?](https://github.com/rui314/mold#why-is-mold-so-fast), GitHub. Retrieved on January 8, 2022]]
2.  [[[↑](#cite_ref-2)] [[Why isn\'t ld.lld faster?](https://maskray.me/blog/2021-12-19-why-isnt-ld.lld-faster) LLD developer, maskray\'s blog December 12, 2021]]