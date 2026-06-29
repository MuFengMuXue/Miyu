**Resources**

[[]][Home](http://www.wolfire.com/overgrowth)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Overgrowth "wikipedia:Overgrowth")

Overgrowth is a third person, 3D, fast paced, cross-platform action computer game developed by Wolfire Games. It has been in development since September 17, 2008^[\[1\]](#cite_note-1)^.

## Contents

-   [[1] [Installation]](#Installation)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [User groups]](#User_groups)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [S3TC support]](#S3TC_support)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)
-   [[6] [References]](#References)

## [Installation]

At this point, since the game is currently in development, the install requirements might change. Hopefully this wiki page will reflect package requirements accordingly. At minimum the following packages are required for Overgrowth to run properly:

`root `[`#`]`emerge --ask --verbose gnome-base/gconf media-libs/freeimage media-libs/freealut media-libs/libpng`

## [Configuration]

### [User groups]

Make sure the users that will be running the game have the proper group permissions. Substitute `<username>` in the command below for each user that will require permission to play Overgrowth:

`root `[`#`]`gpasswd -a <username> audio `

`root `[`#`]`gpasswd -a <username> video `

## [Troubleshooting]

### [S3TC support]

If the game display a white box during the loading screen it might be because S3TC support is missing. This is fixable by installing the [[[media-libs/libtxc_dxtn]](https://packages.gentoo.org/packages/media-libs/libtxc_dxtn)[]] package:

** Note**\
Installing the [[[media-libs/libtxc_dxtn]](https://packages.gentoo.org/packages/media-libs/libtxc_dxtn)[]] package is no longer necessary since the S3TC patent expired on October 2, 2017. S3TC support is now enabled by default with Mesa 17.3^[\[2\]](#cite_note-2)^.

`root `[`#`]`emerge --ask --verbose media-libs/libtxc_dxtn`

## [See also]

-   [Steam](https://wiki.gentoo.org/wiki/Steam "Steam") --- a video game digital distribution service by Valve.

## [External resources]

-   [Wolfire Games](https://www.wolfire.com/) - The parent company of Overgrowth.
-   [Wolfire blog](http://blog.wolfire.com/) - Used to post status updates for *Overgrowth*
-   [What is *Overgrowth* Video](https://www.youtube.com/watch?v=Vb9NK2t2JuQ) - A video explaining Overgrowth.
-   [Official Wolfire Wiki](https://wiki.wolfire.com/index.php/Main_Page)
-   [Overgrowth on Linux (Official Wolfire Wiki)](https://wiki.wolfire.com/index.php/Overgrowth_Linux)
-   [Wolfires Overgrowth Comics](https://www.wolfire.com/comic) - The Lore of Overgrowth.

## [References]

1.  [[[↑](#cite_ref-1)] [[http://blog.wolfire.com/2008/09/announcing-overgrowth/](http://blog.wolfire.com/2008/09/announcing-overgrowth/)]]
2.  [[[↑](#cite_ref-2)] [Matt Turner. [Import libtxc_dxtn\'s S3TC code into Mesa](https://lists.freedesktop.org/archives/mesa-dev/2017-October/171265.html), [The mesa-dev Archives](https://lists.freedesktop.org/archives/mesa-dev/), October 2nd, 2017. Retrieved on August 4th, 2019.]]