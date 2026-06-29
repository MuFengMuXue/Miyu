**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/SDCard "wikipedia:SDCard")

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [Find out basic parameters]](#Find_out_basic_parameters)
-   [[3] [Partition alignment]](#Partition_alignment)
-   [[4] [Filesystem]](#Filesystem)
    -   [[4.1] [Solution 1: Vendor default FAT]](#Solution_1:_Vendor_default_FAT)
    -   [[4.2] [Solution 2: Tuned ext4]](#Solution_2:_Tuned_ext4)
    -   [[4.3] [Solution 3: Squashfs]](#Solution_3:_Squashfs)
-   [[5] [Appendix: Benchmarks]](#Appendix:_Benchmarks)
-   [[6] [See also]](#See_also)

## [Introduction]

In [Gentoo on Android](https://wiki.gentoo.org/wiki/Project:Android "Project:Android"), it is often preferable to install into SD card to prevent internal flash from wearing out, which is non-exchangeable. In addition, quite a lot of embedded systems, for example [Raspberry Pi](https://wiki.gentoo.org/wiki/Raspberry_Pi "Raspberry Pi"), use SD card as the default root filesystem.

Flash based storage (which SD card belongs to) is fundamentally different from magnetic-rotational counterparts (such as a hard disk), partitioning them under-optimized can result in severe I/O overhead which drains system performance and user experience.

Several studies and review articles are devoted on this topic, including [Optimizing Linux with cheap flash drives](http://lwn.net/Articles/428584/), [Solid-state revolution: in-depth on how SSDs really work](https://arstechnica.com/information-technology/2012/06/inside-the-ssd-revolution-how-solid-state-disks-really-work) and [The SSD Anthology: Understanding SSDs and New Drives from OCZ](https://www.anandtech.com/show/2738). These provide the foundations to the strategies in this article.

SD card is similar to [SSD](https://wiki.gentoo.org/wiki/SSD "SSD"), except its management layer is thiner and less smarter than those in [SSD](https://wiki.gentoo.org/wiki/SSD "SSD"). In this survey, we document those which are not covered by [SSD](https://wiki.gentoo.org/wiki/SSD "SSD").

## [Find out basic parameters]

There are some intrinsic parameters associated with each SD card, which determines the optimized units to do I/O operation. They are different kinds of access units, such as *pages*, *erase blocks*, *allocation groups*. A survey of such parameters from different SD card available in the market can be found in the [Linaro wiki](https://wiki.linaro.org/WorkingGroups/KernelArchived/Projects/FlashCardSurvey).

If your card is not listed, or you want to figure the parameters out by yourself, it is always possible to test and observe to time response of different access patterns by the [flashbench tool](https://git.linaro.org/gitweb?p=people/arnd/flashbench.git). By following the README in the git repo, essentially you get a test result like this:

`root `[`#`]`flashbench -a <device>`

    align 8589934592        pre 1.42ms      on 2.46ms       post 1.02ms     diff 1.24ms
    align 4294967296        pre 1.34ms      on 2.38ms       post 1.06ms     diff 1.19ms
    align 2147483648        pre 1.52ms      on 2.5ms        post 1.17ms     diff 1.16ms
    align 1073741824        pre 1.27ms      on 2.04ms       post 1.09ms     diff 868µs
    align 536870912 pre 1.35ms      on 2.18ms       post 1.16ms     diff 931µs
    align 268435456 pre 1.43ms      on 2.31ms       post 1.15ms     diff 1.03ms
    align 134217728 pre 1.51ms      on 2.48ms       post 1.2ms      diff 1.13ms
    align 67108864  pre 1.5ms       on 2.47ms       post 1.2ms      diff 1.12ms
    align 33554432  pre 1.51ms      on 2.45ms       post 1.15ms     diff 1.12ms
    align 16777216  pre 1.51ms      on 2.43ms       post 1.2ms      diff 1.07ms
    align 8388608   pre 1.54ms      on 2.46ms       post 1.19ms     diff 1.09ms
    align 4194304   pre 1.55ms      on 2.45ms       post 1.2ms      diff 1.07ms
    align 2097152   pre 1.71ms      on 2.26ms       post 1.18ms     diff 813µs
    align 1048576   pre 1.71ms      on 2.29ms       post 1.19ms     diff 835µs
    align 524288    pre 1.71ms      on 2.29ms       post 1.17ms     diff 848µs
    align 262144    pre 1.69ms      on 2.25ms       post 1.19ms     diff 813µs
    align 131072    pre 1.69ms      on 2.29ms       post 1.2ms      diff 850µs
    align 65536     pre 1.71ms      on 2.29ms       post 1.19ms     diff 841µs
    align 32768     pre 1.71ms      on 2.27ms       post 1.18ms     diff 822µs
    align 16384     pre 1.7ms       on 2.29ms       post 1.17ms     diff 852µs
    align 8192      pre 1.81ms      on 1.8ms        post 1.24ms     diff 277µs
    align 4096      pre 1.86ms      on 1.85ms       post 1.25ms     diff 301µs
    align 2048      pre 1.9ms       on 1.91ms       post 1.92ms     diff 2.18µs

That is a class 10 32GB micro SD card by PQI tested by the author. Attention should be paid on the large jumps in the last column. In the example, from 1G to 2G (allocation group), 2M to 4M (erase block), 8k to 16k (multi-plane access), 2k to 4k (page). Despite of being only a reasonable guess not perfectly reliable, it do give us a guideline in tuning the filesystem parameter which result in performance boost in I/O.

## [Partition alignment]

Make sure the partition is aligned to and allocated by erase blocks (in the above example 4M). At the time of writing, fdisk is the only tool known to support fine tuning of the alignment. (Neither sfdisk nor parted supports this.)

As this is not intended to be yet another tutorial on fdisk, you are referred to the *repartition* section of the article [Optimizing fs on sd-card for Linux/Fedora on Dreamplug](http://blogofterje.wordpress.com/2012/01/14/optimizing-fs-on-sd-card).

## [Filesystem]

There are candidates for the filesystem. The survey is not yet completed and the recommendation is by no means final. You are always encouraged to extend this study with more insights and tests.

### [Solution 1: Vendor default FAT]

Most of the case an SD card is optimized to video streaming, in which large files are read/written continuously. Preformatted FAT partition is optimized for this purpose.

In order to support POSIX features required by Gentoo on FAT, [posixovl](http://sourceforge.net/projects/posixovl) can be used. However, the test by the author indicates this solution is suboptimal. A reasonable guess is that, FAT does not perform well with lots of small files, and the overhead of fuse by posixovl degrades performance notably on embedded systems where CPU power are bottlenecks. At the time of writing there is no such kind of overlay filesystem in kernel space yet.

### [Solution 2: Tuned ext4]

**This is the recommend solution.** RAID feature of ext4 is exploited to match the I/O pattern of the SD card. As this tuning shares the same rationale with [SSD](https://wiki.gentoo.org/wiki/SSD "SSD").

The recommend recipe is,

    filesystem block = page
    stride = multi-plane access / page
    stripe-width = erase block / page

In the case above,

    filesystem block = 4k
    stride = 4
    stripe-width = 1024

Mount the tuned ext4 with *noatime* option.

At the time of writing, there are some inconsistency and confusion in the community for which parameter to choose and which definition to use, reflected partially by a survey of [Magic soup: ext4 with SSD, stripes and strides](http://thelastmaimou.wordpress.com/2013/05/04/magic-soup-ext4-with-ssd-stripes-and-strides). You are always encouraged to test out by yourself to find out the best parameters instead of following guides blindly.

### [Solution 3: Squashfs]

[Squashfs](https://wiki.gentoo.org/wiki/SquashFS "SquashFS") has been the best candidate filesystem for LiveCD/LiveUSB. However the Linux kernel of Android usually lacks squashfs and aufs. [squashfuse](http://sourceforge.net/projects/squashfuse) or [unionfs-fuse](http://podgorny.cz/moin/UnionFsFuse) suffers from one of the same issue as posixovl, namely the impact of fuse overhead on embedded systems.

## [Appendix: Benchmarks]

The recommendation of ext4 results from the following test. Its environment is Motorola Droid Razr XT910 with PQI class 10 32GB micro SD card, running Gentoo RAP. Squashfs mounted by *squashfuse*, overlayed with *unionfs-fuse*.

In the following table, *block size* is that of squashfs, *comp* is the compression algorithm of squashfs, *overlay fs* is the RW layer of unionfs-fuse on top of RO layer of the squashfs, *host fs* is the filesystem holding the squashfs image, *emerge --help* and *lddtree \`which mount.posixovl\`* are two commands used for benchmarking.

The filesystems used are, *ext3* from internal flash of the XT910, *ext4* aligned and tuned ext4, *fat32* vendor preformatted fat32, *fat32* reformatted and tuned fat32.

  --------------- ------ ---------------- ---------- ------------------- --------------------------------------
  block size(k)   comp   overlay fs       host fs    emerge --help (s)   lddtree \`which mount.posixovl\` (s)
  4               xz     \-               fat32      1.084               1.406
  4               xz     \-               fat32(r)   2.602               3.103
  4               xz     posixovl/fat32   fat32      4.406               4.789
  4               xz     ext3             fat32      3.592               4.271
  4               xz     ext4             fat32(r)   3.775               4.268
  16              gz     \-               fat32      1.068               1.389
  16              gz     \-               ext4       1.089               1.256
  16              gz     \-               fat32(r)   1.047               1.230
  16              gz     posixovl/fat32   fat32      4.435               4.974
  16              gz     ext3             fat32      1.800               2.132
  16              gz     ext4             fat32(r)   2.038               2.141
  256             xz     \-                          5.402               5.891
  256             xz     posixovl/fat32              8.340               9.375
  256             xz     ext3                        5.713               6.220
  \-              \-     posixovl/fat32              2.812               \-
  \-              \-     ext4                        0.380               0.623
  --------------- ------ ---------------- ---------- ------------------- --------------------------------------

## [See also]

-   [SSD](https://wiki.gentoo.org/wiki/SSD "SSD") --- provides guidelines for basic maintenance, such as enabling discard/trim support, for **SSD**s ([Solid State Drives](https://en.wikipedia.org/wiki/Solid-state_drive "wikipedia:Solid-state drive")) on Linux.