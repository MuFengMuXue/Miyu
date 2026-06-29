[[]][Home](https://github.com/X11Libre/xserver)

**Xlibre** is a fork of the [Xorg](https://wiki.gentoo.org/wiki/Xorg "Xorg") server which describes itself as *lots of code cleanups and enhanced functionality*. It was forked from Xorg after the Xorg developers claimed the author\'s many recent contributions suffer from poor quality control and numerous regressions. The *enhanced functionality* is not described or listed.

** Warning**\
This project is in early stages. [Here be dragons!](https://en.wikipedia.org/wiki/Here_be_dragons) There may be issues with your system, so only proceed if you are happy to debug and report what you find to upstream.

** Warning**\
This project only uses live ebuild packages for most drivers, users should know how to update a system using live ebuilds before using the repository.

** Warning**\
This project changes ABI, so proprietary drivers, such as Nvidia\'s (which has no timeline for availability), ***may not work*** without explicit support from their respective sources.

## [Installation]

Xlibre is not available in the main Gentoo repository. It can be obtained from an unofficial overlay operated by the Xlibre developers:

To add the `xlibre` overlay, run:

`root `[`#`]`emerge -va app-eselect/eselect-repository `

`root `[`#`]`eselect repository enable xlibre `

`root `[`#`]`emaint sync -r xlibre `

xlibre-server is not compatible with xorg-server. When switching to this overlay first fetch the XLibre server package and then remove the X.Org Server and drivers packages.

`root `[`#`]`emerge -f x11-base/xlibre-server `

`root `[`#`]`emerge -C x11-base/xorg-server `

`root `[`#`]`emerge -C x11-base/xorg-drivers `

`root `[`#`]`emerge x11-base/xlibre-server `

`root `[`#`]`emerge @x11-module-rebuild `

`root `[`#`]`emerge @preserved-rebuild `

Use following portage setting to install the software:

`root `[`#`]`echo "*/*::xlibre ~`*`arch`*`" > /etc/portage/package.accept_keywords/xlibre`

## [Nvidia]

Proprietary Nvidia drivers will not work due to ABI changes. The following workaround is available:

** Note**\
As of xlibre version 25.0.0.16 and newer, this workaround is no longer required.

[FILE] **`/usr/share/X11/xorg.conf.d/10-nvidia.conf`**

    Section "ServerFlags"
        Option "IgnoreABI" "1"
    EndSection

** Warning**\
This can sometimes cause instability (crashes, glitches), because the mismatch might break things. But it is handy when you need it to work.

## [Reporting bugs]

Bugs must be reported to [https://github.com/X11Libre/ports-gentoo/issues](https://github.com/X11Libre/ports-gentoo/issues)