Little-endian ARMv7-A from Genesi US.

## Contents

-   [[1] [Documentation]](#Documentation)
-   [[2] [Genesi Efika MX specifications]](#Genesi_Efika_MX_specifications)
-   [[3] [/proc/cpuinfo]](#.2Fproc.2Fcpuinfo)
-   [[4] [External resources]](#External_resources)

## [Documentation]

The Genesi USA Efika MX Smarttop is supported on Gentoo, thanks to [Genesi USA](http://www.genesi-usa.com/) who provided us with hardware to bring this forward.

-   [Documentation about installing Gentoo on the Genesi USA Efika MX Smarttop](https://web.archive.org/web/20120627181550/https://dev.gentoo.org/~darkside/arm/efikamx/install/)

## [Genesi Efika MX specifications]

Board specifications:

[CODE]

    # Freescale i.MX51 SoC
    # ARMv7-A 800MHz ARM Cortex-A8 processor
    # 512MB DDR2 RAM
    # 8GB SSD Flash
    # Ralink RT3070USB Wireless card
    # ASIX AX88772 USB 2.0 Ethernet card
    # Soundcard
    #
    # 1x SDHC slot
    # 2x USB 2.0 ports
    # 1x HDMI out
    # 1x Audio IN
    # 1x Audio OUT
    # 1x Ethernet 100Mbps
    # Power button
    #
    # Board with serial and JTAG

## [][/proc/cpuinfo]

CPU info:

[FILE] **`/proc/cpuinfo`**

    Code Listing 3.1: CPU Info
    Processor   : ARMv7 Processor rev 1 (v7l)
    BogoMIPS    : 799.53
    Features    : swp half thumb fastmult vfp edsp
    CPU implementer : 0x41
    CPU architecture: 7
    CPU variant : 0x2
    CPU part    : 0xc08
    CPU revision    : 1

    Hardware    : Genesi Efika MX
    Revision    : 51025
    Serial      : 0000000000000000

## [External resources]

-   [Genesi USA](http://www.genesi-usa.com/)
-   [PowerDeveloper.org](http://www.powerdeveloper.org/)

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Mike Frysinger, Ned Ludd, Robin H. Johnson, Alex Tarkovsky, Alexey Shvetsov, Raúl Porcel, Joshua Saddler on April 28, 2013.**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*