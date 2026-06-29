**[] Archived article**\
\

This article is **archived (obsolete)**. Contents are surely incorrect for current usage, and are intended for historical reference only.

\
TLDR: **Do not use this article!**

\
The Gentoo security audit project handled patching the Linux kernel sources and informing users about global kernel security status. The aim of the project was also to audit Gentoo kernel\'s for potential flaws.

## Contents

-   [[1] [Kernel sources]](#Kernel_sources)
    -   [[1.1] [Supported kernel sources]](#Supported_kernel_sources)
    -   [[1.2] [Unsupported Kernel sources]](#Unsupported_Kernel_sources)
    -   [[1.3] [Making a new kernel source]](#Making_a_new_kernel_source)

## [Kernel sources]

### [Supported kernel sources]

  ---------------------------------- -----------------------------------------------------------------------------------------------------------------------
  Kernel source                      Security liaison
  gentoo-sources                     [Gentoo Kernel project](https://wiki.gentoo.org/wiki/Project:Kernel "Project:Kernel")
  gentoo-kernel, gentoo-kernel-bin   [Distribution Kernel project](https://wiki.gentoo.org/wiki/Project:Distribution_Kernel "Project:Distribution Kernel")
  ---------------------------------- -----------------------------------------------------------------------------------------------------------------------

### [Unsupported Kernel sources]

  --------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Kernel source         Security liaison
  git-sources           [Mike Pagano (mpagano) ](https://wiki.gentoo.org/wiki/User:Mpagano "User:Mpagano")
  mips-sources          [Joshua Kinard (kumba) ](https://wiki.gentoo.org/wiki/User:Kumba "User:Kumba")
  pf-sources            [Joonas Niilola (juippis) ](https://wiki.gentoo.org/wiki/User:Juippis "User:Juippis")
  raspberrypi-sources   [Sam James (sam) ](https://wiki.gentoo.org/wiki/User:Sam "User:Sam")
  rt-sources            [Arisu Tachibana (Alicef) ](https://wiki.gentoo.org/wiki/User:Alicef "User:Alicef")
  vanilla-sources       [Agostino Sarubbo (ago) ](https://wiki.gentoo.org/wiki/User:Ago "User:Ago"), [Gentoo Kernel project](https://wiki.gentoo.org/wiki/Project:Kernel "Project:Kernel")
  --------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Making a new kernel source]

Adding a new kernel source into the main Gentoo repository is not recommended by the Gentoo Kernel Security project unless it is a kernel source that could be used by a wide number of users. Please end consideration here and simply use an overlay to distribute custom or one-off kernel sources.

If you do believe that it is, you must be willing to become the security maintainer. Being the security maintainer for a kernel source means being willing to devote a significant amount of time to closing security bugs for that kernel source. Additionally, you must take care that your kernel source never falls into hard masking. If it does, your kernel source will automatically lose Gentoo Security support, and may be subject to removal from the repository.