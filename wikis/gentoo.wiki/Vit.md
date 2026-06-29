[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Visual_Interactive_Taskwarrior&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Package information](https://packages.gentoo.org/packages/app-misc/vit)

[[]][GitHub](https://github.com/vit-project/vit)

[[]][Bugs (upstream)](https://github.com/vit-project/vit/issues)

[[]][[#taskwarrior](ircs://irc.libera.chat/#taskwarrior)] ([[webchat](https://web.libera.chat/#taskwarrior)])

**Visual Interactive Taskwarrior** (**vit**) is an curses-based front-end for [Taskwarrior](https://wiki.gentoo.org/wiki/Taskwarrior "Taskwarrior") with [vim](https://wiki.gentoo.org/wiki/Vim "Vim")-like keybindings. Like vim, [vit] has extensive internal online help documentation. While intended to be intuitive to vim users [vit] is highly configurable and alternative key bindings entirely possible.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Additional software]](#Additional_software)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Environment variables]](#Environment_variables)
    -   [[2.2] [Files]](#Files)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [app-misc/vit](https://packages.gentoo.org/packages/app-misc/vit) [[]] [A lightweight, fast, curses-based front end to Taskwarrior]

  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`test`](https://packages.gentoo.org/useflags/test)   Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-22 23:17] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-misc/vit`

### [Additional software]

As the name *Visual Interactive Taskwarrior* suggests, Taskwarrior (task) is required for [vit] to function.

## [Configuration]

### [Environment variables]

-   `$VIT_DIR` - specifies the location of the [vit] configuration directory.

### [Files]

The `$VIT_DIR` can force a configuration directory location to a location other than the default or an XDG directory.

-   [\~/.vit/config.ini] - the default location for the [vit] configuration file directory.
-   [\<any valid xdg dir\>/vit/config.ini] - the XDG compliant configuration file location.

The default [config.ini] is heavily commented and intended to be studied by the end user for maximum customization.

## [Usage]

### [Invocation]

`user `[`$`]`vit --help`

    vit --help
    usage: vit [options] [report] [filters]

    VIT (Visual Interactive Taskwarrior)

    options:
      -h, --help      show this help message and exit
      -v, --version   show program's version number and exit
      --list-actions  list all available actions
      --list-pids     list all pids found in pid_dir, if configured

    VIT (Visual Interactive Taskwarrior) is a lightweight, curses-based front end for
    Taskwarrior that provides a convenient way to quickly navigate and process tasks.
    VIT allows you to interact with tasks in a Vi-intuitive way.

    A goal of VIT is to allow you to customize the way in which you use Taskwarrior's
    core commands as well as to provide a framework for easily dispatching external
    commands.

    While VIT is running, type :help followed by enter to review basic command/navigation actions.

    See https://github.com/vit-project/vit for more information.

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose app-misc/vit`

## [See also]

-   [Taskwarrior](https://wiki.gentoo.org/wiki/Taskwarrior "Taskwarrior") --- to-do list manager for the command line
-   [Timewarrior](https://wiki.gentoo.org/wiki/Timewarrior "Timewarrior") --- a time management tool for the terminal.