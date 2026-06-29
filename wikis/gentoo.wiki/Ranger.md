[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Ranger&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://ranger.github.io/)

[[]][Package information](https://packages.gentoo.org/packages/app-misc/ranger)

[[]][Wikipedia](https://en.wikipedia.org/wiki/ranger_(file_manager) "wikipedia:ranger (file manager)")

[[]][GitHub](https://github.com/ranger/ranger)

[[]][[#ranger](ircs://irc.libera.chat/#ranger)] ([[webchat](https://web.libera.chat/#ranger)])

**ranger** is a console file manager with VI key bindings. It provides a minimalistic and nice curses interface with a view on the directory hierarchy.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Additional software]](#Additional_software)
        -   [[1.3.1] [Dragon]](#Dragon)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Image Preview on Wayland]](#Image_Preview_on_Wayland)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [app-misc/ranger](https://packages.gentoo.org/packages/app-misc/ranger) [[]] [Vim-inspired file manager for the console]

  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`test`](https://packages.gentoo.org/useflags/test)   Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-06-30 15:26] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-misc/ranger`

### [Additional software]

Ranger can be extended with additional tools, this section will discuss some possibilities of note.

#### [Dragon]

[Dragon](https://github.com/mwh/dragon) is a drag and drop functionality for X/Wayland, that can be used in conjunction with Ranger.

Dragon is not currently present in the [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository"), however it is available at the [GURU](https://wiki.gentoo.org/wiki/Project:GURU "Project:GURU") [overlay](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository").

In a pinch, Dragon can be installed by compiling from the git repo, to a user\'s home. First, create a directory to hold the source if one does not yet exist, clone the git repository, and enter the source directory:

`user `[`$`]`mkdir --parents ~/.local/src `

`user `[`$`]`cd ~/.local/src `

`user `[`$`]`git clone https://github.com/mwh/dragon.git `

`user `[`$`]`cd dragon `

Install Dragon, prefixing to a directory in the user\'s home dir:

`user `[`$`]`make prefix="~/.local" install`

The [\~/.local/bin] directory can be added to the `PATH` [environment variable](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/EnvVar#User_specific "Handbook:AMD64/Working/EnvVar"), to allow invocation of [dragon] from the command line - and in scripts - without specifying the full path to the executable.

To use Dragon in Ranger, add to the configuration files:

[FILE] **`/.config/ranger/rc.conf`**

    map <C-d> shell dragon -a -x %p --and-exit

[FILE] **`~/.config/ranger/rifle.conf`**

    has dragon, X, flag f = dragon -a -x "$@"

It should now be possible to press [Ctrl]+[d] in ranger to open a GUI popup with the selected folder, which can be used to drag and drop.

## [Configuration]

### [Files]

All configuration files can be copied to [\~/.config/ranger/] using the following command:

`user `[`$`]`ranger --copy-config=all`

** Note**\
There are other possible values for this option to copy specific configuration files. Visit the man page section for more info

** Tip**\
To disable loading of the global configuration files, export RANGER_LOAD_DEFAULT_RC=FALSE to the shell environment.

### [Image Preview on Wayland]

Ueberzugpp serves as a drop in replacement for ueberzug, adding wayland support.

[FILE] **`~/.config/ranger/rc.conf`**

    set preview_images_method ueberzug

If low quality pixel image is previewed, [change the layer output to kitty](https://github.com/jstkdng/ueberzugpp/issues/81#issuecomment-1623923211) even if kitty is not installed.

[FILE] **`~/.config/ueberzugpp/config.json`**

     }

## [Usage]

### [Invocation]

`user `[`$`]`ranger --help`

                                                                                                                                                                                                                                         Usage: ranger [options] [path]

    Options:
      --version             show program's version number and exit
      -h, --help            show this help message and exit
      -d, --debug           activate debug mode
      -c, --clean           don't touch/require any config files.
      --logfile=file        log file to use, '-' for stderr
      --cachedir=dir        change the cache directory. (/home/chr/.cache/ranger)
      -r dir, --confdir=dir
                            change the configuration directory.
                            (/home/chr/.config/ranger)
      --datadir=dir         change the data directory.
                            (/home/chr/.local/share/ranger)
      --copy-config=which   copy the default configs to the local config
                            directory. Possible values: all, rc, rifle, commands,
                            commands_full, scope
      --choosefile=OUTFILE  Makes ranger act like a file chooser. When opening a
                            file, it will quit and write the name of the selected
                            file to OUTFILE.
      --choosefiles=OUTFILE
                            Makes ranger act like a file chooser for multiple
                            files at once. When opening a file, it will quit and
                            write the name of all selected files to OUTFILE.
      --choosedir=OUTFILE   Makes ranger act like a directory chooser. When ranger
                            quits, it will write the name of the last visited
                            directory to OUTFILE
      --selectfile=filepath
                            Open ranger with supplied file selected.
      --show-only-dirs      Show only directories, no files or links
      --list-unused-keys    List common keys which are not bound to any action.
      --list-tagged-files=tag
                            List all files which are tagged with the given tag,
                            default: *
      --profile             Print statistics of CPU usage on exit.
      --cmd=COMMAND         Execute COMMAND after the configuration has been read.
                            Use this option multiple times to run multiple
                            commands.

## [External resources]

-   [LF](https://github.com/gokcehan/lf) - a terminal file manager inspired by ranger, written in Go.
-   [[[app-misc/nnn]](https://packages.gentoo.org/packages/app-misc/nnn)[]] - the \"missing terminal file browser\" for X.
-   [Yazi](https://github.com/sxyazi/yazi) - a blazing fast terminal file manager inspired by ranger, written in Rust. It is available at the [GURU](https://wiki.gentoo.org/wiki/Project:GURU "Project:GURU") [overlay](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository").