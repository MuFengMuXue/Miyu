** Important**\
This is not a help page. It\'s a don\'t-do-these-things-unless-you-have-a-good-reason-to page. Once upon a time they may have been \'verygoodthings\', but no more.

** Tip**\
Style for this page only. Heading level 2 is the myth. The following paragraphs explain why it\'s now a myth.

** Warning**\
Help, if any, should be included by reference, or this page will be added to myths as the help goes out of date and and passes into Gentoo mythology.

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [Binhost systems aren\'t real Gentoo]](#Binhost_systems_aren.27t_real_Gentoo)
-   [[3] [Putting PORTAGE_TMPDIR into tmpfs Speeds Up Builds]](#Putting_PORTAGE_TMPDIR_into_tmpfs_Speeds_Up_Builds)
-   [[4] [Not Having a Swap Partition/File Prevents the Kernel Swapping]](#Not_Having_a_Swap_Partition.2FFile_Prevents_the_Kernel_Swapping)
-   [[5] [Using -O3 in make.conf Speeds Up Execution Times]](#Using_-O3_in_make.conf_Speeds_Up_Execution_Times)
    -   [[5.1] [Intel/AMD Only]](#Intel.2FAMD_Only)
-   [[6] [MAKEOPTS threads+1]](#MAKEOPTS_threads.2B1)
-   [[7] [Only n00bs use the distribution kernel]](#Only_n00bs_use_the_distribution_kernel)
-   [[8] [app-misc/ckermit was named after a frog]](#app-misc.2Fckermit_was_named_after_a_frog)
-   [[9] [dev-lang/python was named after a flying circus]](#dev-lang.2Fpython_was_named_after_a_flying_circus)
-   [[10] [distcc will speed up my compiles]](#distcc_will_speed_up_my_compiles)

## [Introduction]

Like the IBM PC (launched 1981) and its offspring, Gentoo (Oct 1999) has got old and gnarly now. See the [Gentoo History Project](https://wiki.gentoo.org/wiki/Project:Gentoo_History "Project:Gentoo History").

Try your hand at installing [Gentoo as it was in 2003](https://wiki.gentoo.org/wiki/User:NeddySeagoon/Historical_Gentoo "User:NeddySeagoon/Historical Gentoo").

Like lore everywhere, this ageing process has given rise to beliefs and reconsolidations that have their origins in some old part-truths but are no longer true today with modern hardware. Some were never true.

In no particular order:

## [][Binhost systems aren\'t real Gentoo]

A common myth say is that a user must compile everything in Gentoo or that the [Project:Binhost](https://wiki.gentoo.org/wiki/Project:Binhost "Project:Binhost") is anti-Gentoo. The irony being that Gentoo was created to be all about user choice, and all the [binhost] provides is a choice to its users. Using the [binhost] doesn\'t prevent a user from compiling the packages they want to modify, as both binary and source-built packages can coexist seamlessly.

## [Putting PORTAGE_TMPDIR into tmpfs Speeds Up Builds]

That has not been true for many years now, if it ever even was.

[tmpfs] is the kernel disk cache but with no permanent backing store. The kernel will serve everything from the cache, without reading the HDD if it can. It follows that if you have the RAM for `PORTAGE_TMPDIR` in [tmpfs] the kernel is already doing it.

The main point in favour of `PORTAGE_TMPDIR` in [tmpfs] is that it saves writes that will never be read. That may be considered a good thing by users who are worried about SSD writes wearing out the SSD.

The detail discussion can be found in [TMPDIR in tmpfs](https://wiki.gentoo.org/wiki/Portage_TMPDIR_on_tmpfs "Portage TMPDIR on tmpfs").

## [][Not Having a Swap Partition/File Prevents the Kernel Swapping]

False. The Swap Partition/File is only used for contents of dynamically allocated RAM. That includes the content of [tmpfs].

The kernel has several other thing it can do to \'swap\'. Not having even a small swap space, that may never be used, removes an indicator to pressure on RAM. Use of a small amount of swap, particularly after a long uptime is normal.

The kernel does not load anything into real physical RAM until its required, its mmapped. When something is needed but not present, a page fault is generated and the CPU does something else while the page is loaded.

This loading on demand means that pages can be dropped and reloaded as needed. That\'s swapping without using swap space.

Clean pages, that do not need to be written to disk can just be dropped and reloaded later.

Dirty pages, not yet committed to HDD, must be written before they can be dropped. Note that \'dirty pages\' are never written to swap.

An interesting side effect of this [mmap]ing is that the kernel can execute programs that are too big to fit into RAM as several virtual memory pages can be mapped to the same physical page.

## [Using -O3 in make.conf Speeds Up Execution Times]

The clue here is in the name `-O` for *optimise*, which implies a trade-off. While it will be optimum for some things, it will be suboptimal for others.

Premature optimisation is the root of all evil.

All computers wait at the same speed. Do you really care if `$EDITOR` waits longer between your keypresses?

You may want to squeeze the pips on QEMU but this may well not be the way to do it.

`-O3` makes the code bigger to try to reduce execution time. That\'s OK as long as the bigger code does not displace wanted code in the CPU cache, or if it does, the prefetch takes care of potential cache misses before they happen. It\'s all very cache size dependent and requires to be benchmarked on a case by case basis. Probably on a function by function basis.

### [][Intel/AMD Only]

These systems have an interesting \'bug\' called the Excess Precision Bug, inherited from the 8087. The FPU internally works to 80 bits but RAM and other floating point data are only 64 bits. Thus different -O levels give different floating point results for the same source code. It all depends on how intermediate results are passed. In FPU registers or in RAM.

## [][MAKEOPTS threads+1]

Using `MAKEOPTS="thread+1"` (or similar) was a common practice to ensure that there is always one more job than the number of available CPU threads. This approach used to help keep the CPU busy back in the single core days, even if some jobs are waiting for I/O operations or other resources. Nowadays in our multi core world this does more harm than good so the 2GB of RAM per thread rule of thumb should be applied.

[Demonstration](https://blogs.gentoo.org/ago/2013/01/14/makeopts-jcore-1-is-not-the-best-optimization/).

## [Only n00bs use the distribution kernel]

Various Gentoo developers use (or are responsible for creating) this kernel configuration. It\'s suitable for [advanced configuration](https://wiki.gentoo.org/wiki/Project:Distribution_Kernel#Modifying_kernel_configuration "Project:Distribution Kernel") through the `USE=savedconfig` flag or [/etc/kernel/config.d] directory. Additional build-time steps [can be performed](https://wiki.gentoo.org/wiki//etc/portage/bashrc "/etc/portage/bashrc") by hooking ebuild functions through the [/etc/portage/env/sys-kernel/gentoo-kernel] script.

Configuring the kernel in this way automates the kernel update process, allowing you to forget about it once it\'s set up.

## [][[[[app-misc/ckermit]](https://packages.gentoo.org/packages/app-misc/ckermit)[]] was named after a frog]

That\'s not a myth.

## [][[[[dev-lang/python]](https://packages.gentoo.org/packages/dev-lang/python)[]] was named after a flying circus]

That\'s not a myth either.

## [distcc will speed up my compiles]

While it may seem faster to use distcc a on core2duo laptop then, offload the compiling to a 12 thread desktop. In reality, the core2duo still has to do most of the work as all linking is done on the client machine. Creating your own private binary packages on the desktop is the most fastest and less issue causing method nowadays. See [Binary package guide](https://wiki.gentoo.org/wiki/Binary_package_guide "Binary package guide") for more information.