This page contains [[changes](https://wiki.gentoo.org/index.php?title=Zswap&diff=1421016)] which are not marked for translation.

\

*Not to be confused with [Swap](https://wiki.gentoo.org/wiki/Swap "Swap").*

**Resources**

[[]][Home](https://www.kernel.org/doc/html/latest/admin-guide/mm/zswap.html)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Zswap "wikipedia:Zswap")

**Zswap** is a lightweight compressed cache for swap pages.

Zswap is a kernel feature that provides a compressed RAM cache for swap memory pages. Pages which would otherwise typically be swapped out to hard disk are instead compressed and stored into a memory pool in RAM. Once this memory pool is full or the available RAM is exhausted, the least recently used ([LRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_.28LRU.29 "wikipedia:Cache replacement policies")) page is decompressed and written to swap on hard disk, as if it had not been intercepted by zswap. After the page has been moved to swap, the compressed version in the memory pool can be freed and used again.

** Note**\
Next to zswap there is something related called [zram](https://wiki.gentoo.org/wiki/Zram "Zram"). Zram can also be used to create a swap device for compressed pages in memory.

## Contents

-   [[1] [Zswap and Gentoo]](#Zswap_and_Gentoo)
-   [[2] [Differences between zswap and zram based swap]](#Differences_between_zswap_and_zram_based_swap)
-   [[3] [Kernel configuration]](#Kernel_configuration)
-   [[4] [Interactive configuration]](#Interactive_configuration)
-   [[5] [Making the configuration permanent]](#Making_the_configuration_permanent)
    -   [[5.1] [Using the kernel commandline]](#Using_the_kernel_commandline)
    -   [[5.2] [Alternative: using local.d]](#Alternative:_using_local.d)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

## [Zswap and Gentoo]

Zswap is particularly interesting for Gentoo, because it can help make the most of limited RAM resources when emerging (compiling) large packages. It uses a part of the available RAM as compressed swap space.

Imagine a system with 8 GB of RAM with zswap using up to 25% of it, and zswap reaching a compression ratio of a factor two. The system will then have 25% of 8GB times two, what is 4GB of swap space in memory which only costs 2 GB of RAM. Not only is this a very effective use of RAM memory, but it can be faster than swap files on older mechanical hard drives.

For systems with swap files on SSD, zswap might help to relieve wear on the SSDs.

## [Differences between zswap and zram based swap]

A short overview:

-   Zswap works in conjunction with regular [swap](https://wiki.gentoo.org/wiki/Swap "Swap") while a [zram](https://wiki.gentoo.org/wiki/Zram "Zram") based swap device does not require a backing swap device and may work standalone (if no swap on hard disk is required, i.e. on SSD or kind of flash memory).
-   Zswap is a compressed swap cache in RAM and works as a type of proxy for regular swap (in this context also called backing swap device). Zswap gets filled up first and evicts pages from compressed cache on an [LRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_.28LRU.29 "wikipedia:Cache replacement policies") basis to the backing swap device when the compressed pool reaches its size limit. This not only speeds up swap usage but also reduces hits on backing swap device (i.e. SSD).
-   A zram based swap on the other hand works like regular swap (but compressed in RAM) without the opportunity to evict pages. So it gets filled up gradually until it's full. After that, the next (but probably slower) swap in order (i.e. on hard disk) fills up. This way, it is possible to have stored less frequently used memory pages within the faster zram based swap, while newer frequently used memory pages get swapped to slower hard disk.

## [Kernel configuration]

The kernel needs to have swap, frontswap, options for zswap and compression algorithms enabled:

[KERNEL] **Enable zswap**

    Memory Management options  --->
        [*] Support for paging of anonymous memory (swap) --->
            [*] Compressed cache for swap pages
            [ ] Enable the compressed cache for swap pages by default
            -*- Common API for compressed memory storage
            Default allocator (zsmalloc) --->
            < > Low (Up to 2x) density storage for compressed pages
            < > Up to 3x density storage for compressed pages
        -*- N:1 compression allocator (zsmalloc)
        [*] Enable frontswap to cache swap pages if tmem is present (below 6.5)
    Cryptographic API  --->
           Deflate compression algorithm
        -*-   LZO compression algorithm
        <*>   LZ4 compression algorithm
        <*>   LZ4HC compression algorithm
        <*>   Zstd compression algorithm

## [Interactive configuration]

The zswap parameters can be examined as follows:

`root `[`#`]`cd /sys/module/zswap/parameters `

`root `[`#`]`grep "" *`

    compressor:lzo
    enabled:N
    max_pool_percent:20
    same_filled_pages_enabled:Y
    zpool:zbud

** Note**\
Details about these parameters and what they do can be found [here](https://docs.kernel.org/admin-guide/mm/zswap.html) (docs.kernel.org).

Enabling zswap can be done by writing \"1\" to the enabled file:

`root `[`#`]`echo 1 > /sys/module/zswap/parameters/enabled `

or:

`root `[`#`]`echo Y > /sys/module/zswap/parameters/enabled `

** Note**\
Next to zswap there is something related called [zram](https://wiki.gentoo.org/wiki/Zram "Zram"). Zram can also be used to create a swap device for compressed pages in memory.

LZ4 is a popular choice for the compression algorithm:

`root `[`#`]`echo lz4 > /sys/module/zswap/parameters/compressor`

## [Making the configuration permanent]

### [Using the kernel commandline]

Zswap can be configured permanently using the kernel commandline, e.g when using [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB"):

[FILE] **`/etc/default/grub`**

    GRUB_CMDLINE_LINUX="zswap.enabled=1 zswap.compressor=lz4"

Do not forget to regenerate the GRUB configuration.

### [Alternative: using local.d]

Create a file in /etc/local.d:

[FILE] **`/etc/local.d/50-zswap.start`**

    # configure zswap
    echo lz4 > /sys/module/zswap/parameters/compressor
    echo 1 > /sys/module/zswap/parameters/enabled

Make the file executable:

`root `[`#`]`chmod +x /etc/local.d/50-zswap.start`

## [See also]

-   [Swap](https://wiki.gentoo.org/wiki/Swap "Swap") --- refers to both the act of moving memory pages between memory and a secondary storage.
-   [Zram](https://wiki.gentoo.org/wiki/Zram "Zram") --- a [Linux kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") feature and set of userspace tools for creating compressible RAM-based block devices.

## [External resources]

-   [Arch Linux zswap wiki page](https://wiki.archlinux.org/index.php/zswap)
-   [Linuxreviews zswap page](https://linuxreviews.org/Zswap)
-   [Linuxreviews compression algorithms comparaison](https://linuxreviews.org/Comparison_of_Compression_Algorithms)
-   [The Linux kernel user's and administrator's guide Zswap page](https://www.kernel.org/doc/html/latest/admin-guide/mm/zswap.html)
-   [The Linux kernel user's and administrator's guide z3fold allocator page](https://www.kernel.org/doc/html/latest/mm/z3fold.html)
-   [The Linux kernel user's and administrator's guide zsmalloc allocator page](https://www.kernel.org/doc/html/latest/mm/zsmalloc.html)
-   [LWN.net Transcendent memory in a nutshell](https://lwn.net/Articles/454795/)