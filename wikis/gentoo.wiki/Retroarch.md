**RetroArch** (RA) is a frontend to the LibRetro API. In laymen\'s terms, it\'s a one-stop-shop for video game emulation.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [GURU]](#GURU)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Assets]](#Assets)
        -   [[1.3.1] [Configuration]](#Configuration)
    -   [[1.4] [Cores]](#Cores)
        -   [[1.4.1] [Installing the Cores]](#Installing_the_Cores)
        -   [[1.4.2] [Installing the Core Info Files]](#Installing_the_Core_Info_Files)
    -   [[1.5] [Enabling achievements]](#Enabling_achievements)

## [Installation]

### [GURU]

RA is not part of the Gentoo repository. Before installing it, the [GURU](https://wiki.gentoo.org/wiki/Project:GURU/Information_for_End_Users "Project:GURU/Information for End Users") repository must be enabled.

### [Emerge]

`root `[`#`]`emerge --ask games-emulation/RetroArch`

### [Assets]

Sometimes, when RA is installed, the Assets are missing. This can result in issues like broken fonts and missing icons. If this is the case, then the Assets must be installed.

You can do so via the built-in Online Updater feature. Make sure the `network` `USE` flag is enabled, then navigate to Main Menu \> Online Updater \> Update Assets.

Alternatively, you can install the Assets manually. Download a tarball at [https://github.com/libretro/retroarch-assets/releases](https://github.com/libretro/retroarch-assets/releases). Then extract it via

`user `[`$`]`tar xf v*.tar.gz`

Next, go into the source directory:

`user `[`$`]`cd retroarch-assets-*/`

And open the makefile in the desired text editor.

`user `[`$`]`nano Makefile`

There will be a line near the beginning of the file that looks like this:

[FILE] **`Makefile`**

    INSTALLDIR := $(PREFIX)/share/libretro/assets

`INSTALLDIR` is the directory where the Assets will be put---henceforth called the *Assets directory*. Like all other RA Resource directories, it can (in theory) be any directory in the filesystem with the proper permissions. In practice, however, the Assets directory is usually set to either [\~/.config/retroarch/assets] for user-wide access or [/usr/share/libretro/assets] for system-wide access. Whatever the case may be, `INSTALLDIR` should be set to the desired location of the Assets directory.

[FILE] **`Makefile`**

    INSTALLDIR := /path/to/Assets/directory/

Once `INSTALLDIR` is set, save and quit the file and run make to install the Assets to the Assets directory:

`user `[`$`]`make install`

#### [Configuration]

[retroarch.cfg] (by default located at [\~/.config/retroarch/retroarch.cfg]) should have `assets_directory` set to match the path to the Assets directory. If this is not done, **RA will not be able to find the assets.** (This applies also to every RA Resource type---whether they be Cores, Thumbnails, Cheats, etc.).

[FILE] **`retroarch.cfg`**

    assets_directory = "/path/to/Assets/directory/"

### [Cores]

Sometimes, when RA is installed, the Core Info Files and Cores are missing. The main issue caused by this is not being able to play Content. If this is the case, then the Core Info Files and Cores must be installed.

1.  **Core Info Files**
    1.  Contain Core information used by RA. The information includes things such as which platforms the cores are compatible with. Their file extension is `.info`
2.  **Cores**
    1.  Used to emulate systems. Their file extension is `.so`.

#### [Installing the Cores]

Many Cores are available as packages both in the main tree and in the [GURU](https://wiki.gentoo.org/wiki/Project:GURU/Information_for_End_Users "Project:GURU/Information for End Users") repository (e.g., [[[games-emulation/libretro-bnes]](https://packages.gentoo.org/packages/games-emulation/libretro-bnes)[]]).

Prebuilt Cores are found in a 7zip archive located on the [LibRetro BuildBot](https://buildbot.libretro.com). Navigate to `/ > <nightly/stable> > <version> > linux > x86_64` and download `RetroArch_cores.7z`. The archive has to be extracted before the Cores can be used, however.

Before extracting a 7zip archive, [7-Zip](https://wiki.gentoo.org/wiki/7-Zip "7-Zip") must be installed on the system if it isn\'t already:

`root `[`#`]`emerge --ask app-arch/7zip`

The files can be then extracted with:

`user `[`$`]`7zz x RetroArch_cores.7z`

A directory named [RetroArch-Linux-x86_64] will appear in the working directory. The Cores are found in this directory, but not in the root---they\'re in [RetroArch-Linux-x86_64/RetroArch-Linux-x86_64.AppImage.home/.config/retroarch/cores/]. Copy the files to the Cores directory:

`user `[`$`]`cp RetroArch-Linux-x86_64/RetroArch-Linux-x86_64.AppImage.home/.config/retroarch/cores/* /path/to/Cores/directory/`

The Cores directory is usually set to be either [\~/.config/retroarch/cores] for user-wide access or [/usr/share/libretro/cores] for system-wide access---similar to the Assets directory.

Just as with the Assets directory, [retroarch.cfg] must be edited to reflect the location of the Cores directory. The variable determining where RA searches for Cores is `libretro_directory`.

[FILE] **`retroarch.cfg`**

    libretro_directory = "/path/to/Cores/directory/"

#### [Installing the Core Info Files]

You can install the Core Info Files via the built-in Online Updater feature. Make sure the `network` `USE` flag is enabled, then navigate to Main Menu \> Online Updater \> Update Core Info Files.

Alternatively, you can install the Core Info manually. Download a tarball at [https://github.com/libretro/libretro-core-info/releases](https://github.com/libretro/libretro-core-info/releases). Then extract it via

`user `[`$`]`tar xf v*.tar.gz`

And copy the contents of the newly created `libretro-core-info-<version>` directory to the Core Info Files directory.

`user `[`$`]`cp libretro-core-info-*/* /path/to/CoreInfo/directory/`

The Core Info Files directory is usually the same directory as the Cores directory.

Once again, edit [retroarch.cfg] to reflect the location of the core directory. The variable to be changed is `libretro_directory`.

[FILE] **`retroarch.cfg`**

    libretro_directory = "/path/to/CoreInfo/directory/"

### [Enabling achievements]

RetroArch RetroAchievements are handled by `cheevos`. To enable them, add `USE="cheevos"`.