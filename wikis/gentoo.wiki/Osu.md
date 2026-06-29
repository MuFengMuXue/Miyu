**Resources**

[[]][Home](https://osu.ppy.sh)

[[]][Package information](https://packages.gentoo.org/packages/games-arcade/osu-lazer)

[[]][Wikipedia](https://en.wikipedia.org/wiki/osu! "wikipedia:osu!")

[[]][GitHub](https://github.com/ppy/osu)

**osu!** is a free-to-win, cross-platform rhythm game. **osu!lazer** is the open-source client intended to eventually replace the legacy osu! client, which is only available for Windows and macOS.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [License]](#License)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
    -   [[1.4] [Alternative: AppImage release]](#Alternative:_AppImage_release)
        -   [[1.4.1] [Required old-format AppImage package]](#Required_old-format_AppImage_package)
        -   [[1.4.2] [AppImage download]](#AppImage_download)
-   [[2] [Legacy client]](#Legacy_client)

## [Installation]

### [License]

Installing [[[games-arcade/osu-lazer]](https://packages.gentoo.org/packages/games-arcade/osu-lazer)[]] requires accepting the [all-rights-reserved](https://gitweb.gentoo.org/repo/gentoo.git/plain/licenses/all-rights-reserved) license.

### [USE flags]

### [USE flags for] [games-arcade/osu-lazer](https://packages.gentoo.org/packages/games-arcade/osu-lazer) [[]] [A free-to-win rhythm game and a final iteration of the osu! game client]

  --------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+pipewire`](https://packages.gentoo.org/useflags/+pipewire)   Use pipewire to enable sound output
  [`debug`](https://packages.gentoo.org/useflags/debug)           Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  --------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-07-13 11:52] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

** Note**\
Sound will still be possible (through ALSA) without PipeWire; the [[[pipewire]](https://packages.gentoo.org/useflags/pipewire)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] use flag merely configures the build to use it.

### [Emerge]

** Important**\
As of 20 May 2025, [[[games-arcade/osu-lazer]](https://packages.gentoo.org/packages/games-arcade/osu-lazer)[]] will build the developer build of osu!, and thus it will have a watermark informing the user of this at the bottom of the main menu. Users wishing to avoid this may consider using the AppImage, as documented below.

`root `[`#`]`emerge --ask games-arcade/osu-lazer`

### [Alternative: AppImage release]

lazer is also provided as a pre-built [AppImage](https://wiki.gentoo.org/wiki/AppImage "AppImage").

[FUSE](https://wiki.gentoo.org/wiki/FUSE "FUSE") is required to run the AppImage. See the instructions at [FUSE](https://wiki.gentoo.org/wiki/FUSE "FUSE") to set up AppImage support if not already present.

#### [Required old-format AppImage package]

** Important**\
As of 20 May 2025, osu!\'s AppImage requires [[[sys-fs/fuse:0]](https://packages.gentoo.org/packages/sys-fs/fuse:0)[]], and won\'t run using just [[[sys-fs/fuse]](https://packages.gentoo.org/packages/sys-fs/fuse)[]].

In order to be able to run the osu!lazer AppImage, the below emerge will be required:

`root `[`#`]`emerge --ask sys-fs/fuse:0`

If a distrubution kernel is being used, then this step should be sufficient by itself for being able to run osu!. (Otherwise, FUSE support will simply also need to be enabled within the kernel.)

#### [AppImage download]

`user `[`$`]`wget `[`https://github.com/ppy/osu/releases/latest/download/osu.AppImage`](https://github.com/ppy/osu/releases/latest/download/osu.AppImage)

`user `[`$`]`chmod +x osu.AppImage`

`user `[`$`]`./osu.AppImage`

## [Legacy client]

The old osu! client (i.e., not lazer) is only natively supported on Windows and macOS. Users have reported success running it with [Wine](https://wiki.gentoo.org/wiki/Wine "Wine"), however, so users who would prefer to stick to the old, and still more popular, client may attempt to run the Windows build available from the [osu! website](https://osu.ppy.sh).