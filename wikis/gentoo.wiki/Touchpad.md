[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Touchpad&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

This meta article acts as a hub of shared knowledge for FOSS touchpad configuration efforts. Improving the state of touchpads is a continual improvement effort in the Linux ecosystem. With support enabled in the kernel, configuration can be performed in a variety of locations. Modern desktop environments build off device drivers exposed from [libinput](https://wiki.gentoo.org/wiki/Libinput "Libinput").

## Contents

-   [[1] [Known components]](#Known_components)
-   [[2] [Available software]](#Available_software)
    -   [[2.1] [Desktop environments]](#Desktop_environments)
    -   [[2.2] [Other]](#Other)
-   [[3] [Features]](#Features)
    -   [[3.1] [Disable while typing]](#Disable_while_typing)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Known components]

  ----------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------
  Name                                                              Linux hardware                                                                                                                                                      Description
  [Alps_PS/2](https://wiki.gentoo.org/wiki/Alps_PS/2 "Alps PS/2")   [Device \'ALPS AlpsPS/2 DualPoint TouchPad\'](https://linux-hardware.org/index.php?id=ps/2:alps-0008-alpsps-2-dualpoint-touchpad)   CONFIG_MOUSE_PS2_ALPS
  ----------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------

## [Available software]

### [Desktop environments]

Desktop environments generally include their own controls for touchpads customization. These can include hot corners, scroll behavior, pinch to zoom, etc.

-   [GNOME](https://wiki.gentoo.org/wiki/GNOME "GNOME")
    -   Graphically the Settings menu ([[[gnome-base/gnome-settings-daemon]](https://packages.gentoo.org/packages/gnome-base/gnome-settings-daemon)[]] - included with GNOME) and GNOME Tweaks ([[[gnome-extra/gnome-tweaks]](https://packages.gentoo.org/packages/gnome-extra/gnome-tweaks)[]]).
    -   From the commandline via [gsettings] (available via [[[dev-libs/glib]](https://packages.gentoo.org/packages/dev-libs/glib)[]]).
-   [KDE Plasma](https://wiki.gentoo.org/wiki/KDE_Plasma "KDE Plasma")
    -   ?
-   [Xfce](https://wiki.gentoo.org/wiki/Xfce "Xfce")
-   System settings
-   [LXDE](https://wiki.gentoo.org/wiki/LXDE "LXDE")
    -   ?
-   [Sway](https://wiki.gentoo.org/wiki/Sway "Sway")
-   [i3](https://wiki.gentoo.org/wiki/I3 "I3")

### [Other]

-   [Xorg](https://wiki.gentoo.org/wiki/Xorg "Xorg") can be used to configure touchpad behavior directly in the [[xorg.conf](https://wiki.gentoo.org/wiki/Xorg.conf "Xorg.conf")] file. Various drivers, such as [Libinput](https://wiki.gentoo.org/wiki/Libinput "Libinput") or [Synaptics](https://wiki.gentoo.org/wiki/Synaptics "Synaptics") can be used to drive the hardware via Xorg.

## [Features]

### [Disable while typing]

Disable while typing (DWT) support can be activated as a feature of the desktop environment or [directly via libinput driver](https://wayland.freedesktop.org/libinput/doc/latest/palm-detection.html#disable-while-typing). Each DE has a different settings path in order to activate the feature.^[\[1\]](#cite_note-1)^

## [See also]

-   [libinput](https://wiki.gentoo.org/wiki/Libinput "Libinput") --- an input device driver for [Wayland compositors](https://wiki.gentoo.org/wiki/Wayland_Desktop_Landscape#Compositors "Wayland Desktop Landscape") and [X.org](https://wiki.gentoo.org/wiki/Xorg "Xorg") window system.

## [External resources]

-   [https://linuxtouchpad.org/](https://linuxtouchpad.org/) - A project dedicated to making touchpads on Linux systems behave in a manner similar to touchpads on MacBooks.

1.  [[[↑](#cite_ref-1)] [[https://linuxtouchpad.org/libinput/2022/05/07/disable-while-typing.html](https://linuxtouchpad.org/libinput/2022/05/07/disable-while-typing.html)]]