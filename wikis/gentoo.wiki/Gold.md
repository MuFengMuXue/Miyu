This page contains [[changes](https://wiki.gentoo.org/index.php?title=Gold&diff=1370724)] which are not marked for translation.

** Warning**\
gold is [less active](https://www.phoronix.com/scan.php?page=news_item&px=GNU-Gold-Stagnate-F31) than it once was, e.g. gold\'s commit [history](https://sourceware.org/git/?p=binutils-gdb.git;a=history;f=gold;hb=HEAD) vs bfd\'s commit [history](https://sourceware.org/git/?p=binutils-gdb.git;a=history;f=ld;hb=HEAD). Users seeking an alternative linker may be interested in LLVM\'s [lld](https://wiki.gentoo.org/wiki/LLVM/LLD "LLVM/LLD").

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Gold_(linker) "wikipedia:Gold (linker)")

GNU **gold** is a linker intended as a replacement for the [ld.bfd] linker.

The two installed linkers are available directly as [ld.bfd] and [ld.gold] respectively. Additionally, the default linker is also installed as [ld] - and this binary is used by compilers.

## [Installation]

Gold can be enabled by setting the `gold` USE flag for [[[sys-devel/binutils]](https://packages.gentoo.org/packages/sys-devel/binutils)[]]. Additionally, setting `default-gold` will make [ld.gold] the default linker.

[FILE] **`/etc/portage/package.use/gold`**

    # enable gold and set it as default
    sys-devel/binutils      gold default-gold

After setting the USE flags, re-install binutils:

`root `[`#`]`emerge --ask --changed-use --deep --oneshot --verbose sys-devel/binutils`

## [See also]

-   [Mold](https://wiki.gentoo.org/wiki/Mold "Mold") --- a linker that aims to provide drop-in compatibility with existing Unix linkers.