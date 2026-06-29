[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Scan_modem&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[scanModem] a software tool that finds a suitable driver for a connected modem. [scanModem] is not available in gentoo.git, so it has to be manually downloaded and extracted:

`user `[`$`]`wget `[`https://web.archive.org/web/20190722162705/http://linmodems.technion.ac.il/packages/scanModem.gz`](https://web.archive.org/web/20190722162705/http://linmodems.technion.ac.il/packages/scanModem.gz)` `

`user `[`$`]`gunzip scanModem.gz `

`user `[`$`]`chmod +x scanModem `

`user `[`$`]`./scanModem `

It will create a folder [Modem] and the file [scanout.something] contains the wanted information. If a modem is detected, the driver is named next to *Drivers*, e.g. for a HSF modem:

[FILE] **`./Modem/scanout.something`**

    Driver=hsfmodem-drivers