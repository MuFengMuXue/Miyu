[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Ltunify&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://lekensteyn.nl/logitech-unifying.html)

[[]][Package information](https://packages.gentoo.org/packages/app-misc/ltunify)

[[]][GitHub](https://github.com/Lekensteyn/ltunify)

Many Logitech input peripherals - mostly mouse and keyboards, but also numpads, presenters, trackballs and touchpads - come with a unique USB receiver. If your peripherals and receiver are not paired from fabric, but support the [Logitech Unifying technology](http://support.logitech.com/en_us/software/unifying), you can still pair them using the [[[app-misc/ltunify]](https://packages.gentoo.org/packages/app-misc/ltunify)[]] package.

The package is available for **[\~amd64]** and **[\~x86]** only.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
-   [[3] [External resources]](#External_resources)

## [Installation]

### [Emerge]

`root `[`#`]`emerge --ask app-misc/ltunify`

## [Usage]

The usage is trivial.

`root `[`#`]`ltunify list`

shows the devices actually paired.

`root `[`#`]`ltunify unpair idx`

removes a listed paired devices that doesn\'t exist anymore.

`root `[`#`]`ltunify pair`

adds a device simply asking to switch it off and on.

`root `[`#`]`ltunify --help`

shows a complete help.

## [External resources]

[Source code](https://git.lekensteyn.nl/ltunify/)