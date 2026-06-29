[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=AppImage&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://appimage.org/)

[[]][Official documentation](https://docs.appimage.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/AppImage "wikipedia:AppImage")

[[]][GitHub](https://github.com/AppImage/appimagekit)

[[]][Official project wiki](https://github.com/AppImage/AppImageKit/wiki)

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/appimage)

**AppImage** is portable software that do not require root permission to be run.

## Contents

-   [[1] [Additional software]](#Additional_software)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
    -   [[2.2] [Creation of AppImage]](#Creation_of_AppImage)
-   [[3] [External resources]](#External_resources)

## [Additional software]

Most AppImages require [[[sys-fs/fuse]](https://packages.gentoo.org/packages/sys-fs/fuse)[]] on slot 0:

`user `[`$`]`./ExamplePackage.AppImage`

    dlopen(): error loading libfuse.so.2

AppImages require [FUSE](https://wiki.gentoo.org/wiki/Filesystem_in_Userspace "Filesystem in Userspace") to run. You might still be able to extract the contents of this AppImage if you run it with the `--appimage-extract` option.

** Tip**\
See the dedicated [official wiki FUSE article](https://github.com/AppImage/AppImageKit/wiki/FUSE) for more information.

This error can be solved by installing [[[sys-fs/fuse]](https://packages.gentoo.org/packages/sys-fs/fuse)[]] in slot 0. Slot 0 has version 2 of FUSE required by most AppImages. Whereas [[[sys-fs/fuse]](https://packages.gentoo.org/packages/sys-fs/fuse)[]] in slot 3 which has version 3 of fuse. The highest version available is installed by default, currently in slot 3, if no slot is specified and doesn\'t solve the dependency problem.

`root `[`#`]`emerge --ask sys-fs/fuse:0`

## [Usage]

### [Invocation]

AppImages can be run without root permission:

`user `[`$`]`chmod +x ExamplePackage.AppImage `

`user `[`$`]`./ExamplePackage.AppImage `

### [Creation of AppImage]

This guide provides instructions for creating an AppImage of [ripgrep], a line-oriented search tool that recursively searches directories for a specified pattern. The AppImage allows you to run [ripgrep] on compatible Linux systems without the need for installation.

**Step 1: Set up your build environment**

Make sure you have the necessary tools and dependencies installed on your system, including [gcc], [cmake], [pkg-config], and [appimagetool].

**Step 2: Clone the ripgrep repository**

`root `[`#`]`git clone `[`https://github.com/BurntSushi/ripgrep.git`](https://github.com/BurntSushi/ripgrep.git)

**Step 3: Navigate to the ripgrep directory**

`root `[`#`]`cd ripgrep`

**Step 4: Build ripgrep**

`root `[`#`]`cargo build --release`

**Step 5: Install the AppStream CLI (optional)**

If you want to include AppStream metadata in your AppImage, you can install the [appstreamcli] tool. This step is optional but recommended.

**Step 6: Create the AppDir**

Create the AppDir using [appimagetool] with the following command:

`root `[`#`]`appimagetool --appimage-extract`

**Step 7: Copy ripgrep files**

Copy the ripgrep binary and any necessary files to the appropriate locations within the AppDir. Use the following commands:

`root `[`#`]`cp target/release/rg squashfs-root/usr/bin/rg`

**Step 8: Create an AppRun file**

Create a file named [AppRun] within the AppDir and make it executable. Add the following content to the file:

[FILE] **`AppRun`AppRun**

    #!/bin/sh
    exec "$(dirname "$0")"/squashfs-root/usr/bin/rg "$@"

**Step 9: Set permissions**

Ensure that the AppRun file is executable by running the following command:

`root `[`#`]`chmod +x squashfs-root/AppRun`

**Step 10: Generate the AppImage**

Finally, generate the AppImage using [appimagetool] with the following command:

`root `[`#`]`appimagetool squashfs-root`

After following these steps, you will have an AppImage file named something like [ripgrep-x.x.x-x86_64.AppImage], where [x.x.x] represents the version number of [ripgrep].

This AppImage can be distributed and run on compatible Linux systems without the need for installation.

## [External resources]

-   [Reddit - Appimage : /r/Gentoo](https://www.reddit.com/r/Gentoo/comments/fgifnd/appimage/g0vx53o/?context=3)