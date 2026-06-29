[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Vifm&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][GitHub](https://github.com/vifm/vifm)

[[]][Package information](https://packages.gentoo.org/packages/app-misc/vifm)

**Vifm** is curses based Vim-like file manager extended with some useful ideas from mutt. If you use Vim, Vifm gives you complete keyboard control over your files without having to learn a new set of commands. It goes not just about Vim-like keybindings, but also about modes, options, registers, commands and other things you might already like in Vim.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
-   [[3] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [app-misc/vifm](https://packages.gentoo.org/packages/app-misc/vifm) [[]] [Console file manager with vi(m)-like keybindings]

  ------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------
  [`+extended-keys`](https://packages.gentoo.org/useflags/+extended-keys)   Support for extended keys (arrows, home etc)
  [`+magic`](https://packages.gentoo.org/useflags/+magic)                   Add support for file type detection via magic bytes (usually via libmagic from sys-apps/file)
  [`+vim`](https://packages.gentoo.org/useflags/+vim)                       Install the vifm vim plugin and vim-compatible documentation
  [`+vim-syntax`](https://packages.gentoo.org/useflags/+vim-syntax)         Pulls in related vim syntax scripts
  [`X`](https://packages.gentoo.org/useflags/X)                             Add support for X11
  [`glib`](https://packages.gentoo.org/useflags/glib)                       Use dev-libs/glib:2 to determine mimetypes
  ------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-07-29 06:52] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-misc/vifm`

## [Usage]

Vifm can be used with one command:

`user `[`$`]`vifm`

### [Invocation]

`user `[`$`]`vifm --help`

    vifm usage:

      To read list of files from stdin use

        vifm -

      To start in a specific directory give the directory path.

        vifm /path/to/start/dir/one
        or
        vifm /path/to/start/dir/one  /path/to/start/dir/two

      To open file using associated program pass its path to vifm.

      If no path is given vifm will start in the current working directory.

      vifm --select
        open parent directory of the given path and select specified file
        in it.

      vifm -f
        makes vifm instead of opening files write selection to
        $VIFM/vimfiles and quit.

      vifm --choose-files |-
        sets output file to write selection into on exit instead of
        opening files.  "-" means standard output.

      vifm --choose-dir |-
        sets output file to write last visited directory into on exit.
        "-" means standard output.

      vifm --delimiter <delimiter>
        sets separator for list of file paths written out by vifm.

      vifm --on-choose <command>
        sets command to be executed on selected files instead of opening
        them.  Command can use any of command macros.

      vifm --logging[=<startup log path>]
        log some operational details $VIFM/log.  If the optional startup
        log path is specified and permissions allow to open it for
        writing, then logging of early initialization (before value of
        $VIFM is determined) is put there.

      vifm --server-list
        list available server names and exit.

      vifm --server-name <name>
        name of target or this instance.

      vifm --remote
        passes all arguments that left in command line to vifm server.

      vifm --remote-expr <expr>
        passes expression to vifm server and prints result.

      vifm -c <command> | +<command>
        run <command> on startup.

      vifm --help | -h
        show this help message and quit.

      vifm --version | -v
        show version number and quit.

      vifm --no-configs
        don't read vifmrc and vifminfo.

## [External resources]

-   [vifm](https://github.com/vifm/vifm)