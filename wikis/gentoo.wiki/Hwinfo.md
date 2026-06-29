[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Hwinfo&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/hwinfo)

[[]][GitHub](https://github.com/openSUSE/hwinfo)

Hardware Information Tool (**hwinfo**) is a small utility created by OpenSUSE to gather information on system hardware.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Usage]](#Usage)
-   [[4] [See also]](#See_also)

## [Installation]

### [Emerge]

[hwinfo] can be installed with a simple [emerge]:

`root `[`#`]`emerge --ask sys-apps/hwinfo`

## [Configuration]

Since the tool is so lightweight, configuration is not necessary.

## [Usage]

To probe for hardware information simply issue:

`root `[`#`]`hwinfo`

To probe for all hardware information use:

`root `[`#`]`hwinfo +all`

This usually takes longer, but provides oodles of information.

To shorten information to a more human-friendly format, add the `--short` option to the command:

`root `[`#`]`hwinfo --short all`

To specify a log file for hwinfo to write, use `log=`. This is different from standard redirection, but should be used for [hwinfo]:

`root `[`#`]`hwinfo log=hardware.txt all`

## [See also]

-   [Hardware detection](https://wiki.gentoo.org/wiki/Hardware_detection "Hardware detection") --- lists and describes utilities used to detect and provide information on hardware.
-   [Lspci](https://wiki.gentoo.org/wiki/Lspci "Lspci") --- contains various utilities dealing with the [PCI bus](https://en.wikipedia.org/wiki/Peripheral_Component_Interconnect "wikipedia:Peripheral Component Interconnect") (primarily [lspci]).
-   [Usbutils](https://wiki.gentoo.org/wiki/Usbutils "Usbutils") --- a collection various utilities for querying the the Universal Serial Bus (USB).