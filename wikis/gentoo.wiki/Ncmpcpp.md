**Resources**

[[]][Home](https://rybczak.net/ncmpcpp/)

[[]][GitHub](https://github.com/ncmpcpp/ncmpcpp)

[ncmpcpp] (**N**Curses **M**usic **P**layer **C**lient **P**lus **P**lus) is a [[[sys-libs/ncurses]](https://packages.gentoo.org/packages/sys-libs/ncurses)[]] based [MPD](https://wiki.gentoo.org/wiki/MPD "MPD") (**M**usic **P**layer **D**aemon) client similar to [ncmpc], with some new and improved features.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Local]](#Local)
-   [[3] [See also]](#See_also)

## [Installation]

** Note**\
Ncmpcpp cannot play music by itself. The [MPD](https://wiki.gentoo.org/wiki/MPD "MPD") backend is required to be installed locally (or on the remote server) which will be managed using the ncmpcpp frontend.

### [USE flags]

### [USE flags for] [media-sound/ncmpcpp](https://packages.gentoo.org/packages/media-sound/ncmpcpp) [[]] [Featureful ncurses based MPD client inspired by ncmpc]

  ----------------------------------------------------------------- -------------------------------------------------------------------
  [`clock`](https://packages.gentoo.org/useflags/clock)             Enable clock screen
  [`outputs`](https://packages.gentoo.org/useflags/outputs)         Enable outputs screen
  [`taglib`](https://packages.gentoo.org/useflags/taglib)           Enable tagging support with taglib
  [`visualizer`](https://packages.gentoo.org/useflags/visualizer)   Enable visualizer screen with sound wave/frequency spectrum modes
  ----------------------------------------------------------------- -------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-01-19 00:16] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask media-sound/ncmpcpp`

## [Configuration]

### [Local]

After installation the user should make a [.ncmpcpp] directory within their specific [/home] directory. This is where ncmpcpp will read the configuration file and output any error messages.

`user `[`$`]`mkdir ~/.ncmpcpp && touch ~/.ncmpcpp/config`

Below is an example of a local user\'s ncmpcpp configuration file:

[FILE] **`~/.ncmpcpp/config`**

    ncmpcpp_directory =         "~/.ncmpcpp"
    mpd_host =                  "localhost"
    mpd_port =                  "6600"
    mpd_music_dir =               "/var/lib/mpd/music/"

## [See also]

-   [MPD](https://wiki.gentoo.org/wiki/MPD "MPD") - Documentation on MPD, a necessary ncmpcpp component.