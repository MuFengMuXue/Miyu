[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-GNOME&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=GNOME "GNOME (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=GNOME/tr "GNOME (15% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=GNOME/ru "GNOME (100% translated)") • ‎[فارسی](//wiki.manjaro.org/index.php?title=GNOME/fa "گنوم (77% translated)")

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Installation]](#Installation)
-   [[3] [Appearance]](#Appearance)
    -   [[3.1] [Desktop Icons]](#Desktop_Icons)
-   [[4] [See also]](#See_also)

# [Overview]

GNOME is a desktop environment that aims to be simple and easy to use. It is a part of the [GNU Project](https://en.wikipedia.org/wiki/GNU).

\

[![Gnome-de-18.jpg](/images/thumb/d/d8/Gnome-de-18.jpg/600px-Gnome-de-18.jpg)](//wiki.manjaro.org/index.php?title=File:Gnome-de-18.jpg)

\

# [Installation]

Instructions for installing GNOME can be found on the [Install Desktop Environments](//wiki.manjaro.org/index.php?title=Install_Desktop_Environments#Gnome_3 "Install Desktop Environments") page.

\

# [Appearance]

#### [Desktop Icons]

Beginning in versions 3.29 the desktop icons functionality was removed and disabled by GNOME. If you wish to restore the desktop icons you have a few options:

-   Replace nautilus with another file manager that supports desktop icons, such as `nemo`.

<!-- -->

-   Replace nautilus with its legacy version, `nautilus-legacy`.
    -   Afterwards to enable desktop icons use `gnome-tweaks` or `dconf-editor` ( org.gnome.desktop.background \> show-desktop-icons \> TRUE )

To manually control which system icons appear on the desktop use `dconf-editor` to navigate to `org.gnome.nautilus.desktop` then toggle \<NAME\>-icon-visible to TRUE or FALSE.

\

# [See also]

[Archwiki:GNOME](https://wiki.archlinux.org/index.php/GNOME)\
[Wikipedia:GNOME](https://en.wikipedia.org/wiki/GNOME)\
[Wikipedia:The GNOME Project](https://en.wikipedia.org/wiki/The_GNOME_Project)\
\