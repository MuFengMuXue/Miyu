**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Linux_kernel#Live_patching "wikipedia:Linux kernel")

Kernel live patching is an \'update-and-coming\' kernel feature being developed by a few corporate Linux companies. Several companies have open sourced their development efforts, making it possible to bring kernel live patching to Gentoo.

A note of caution: Kernel live patching is risky. Count on hard freezing or panics to become normal\...

If at all possible, it\'s recommended to instead pursue making kernel upgrades as automated and painless as possible, like by using a [Distribution Kernel](https://wiki.gentoo.org/wiki/Distribution_Kernel "Distribution Kernel") which builds like a regular package.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
-   [[2] [Available software]](#Available_software)
-   [[3] [References]](#References)

## [Installation]

### [Kernel]

The Linux kernel must be version 4.0 or higher in order to have `LIVEPATCH` support.^[\[1\]](#cite_note-1)^

[KERNEL] **Enable `CONFIG_LIVEPATCH` support**

    Processor type and features  --->
       [*] Kernel Live Patching

## [Available software]

Here are some live patch packages available in Gentoo:

  ----------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Name                                                                                                                                                  Package                                                                                                       Homepage                                                                                             Description
  [[kpatch](https://wiki.gentoo.org/wiki/Kpatch "Kpatch")]   [sys-kernel/kpatch](https://packages.gentoo.org/packages/sys-kernel/kpatch)   [https://github.com/dynup/kpatch](https://github.com/dynup/kpatch)   Dynamic kernel patching for Linux.
  [ksplice]                                                  N/A                                                                                                           [http://www.ksplice.com/](http://www.ksplice.com/)                   Rebootless Linux kernel security updates. Absorbed by Oracle in 2011 and available only by paid support. The 2011 version can be [found on GitHub](https://github.com/jirislaby/ksplice).
  ----------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [References]

1.  [[[↑](#cite_ref-1)] [[https://cateee.net/lkddb/web-lkddb/LIVEPATCH.html](https://cateee.net/lkddb/web-lkddb/LIVEPATCH.html)]]