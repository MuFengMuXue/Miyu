[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Timewarrior&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://timewarrior.net/)

[[]][Official documentation](https://timewarrior.net/docs/)

[[]][Package information](https://packages.gentoo.org/packages/app-misc/timew)

[[]][GitHub](https://github.com/GothenburgBitFactory/timewarrior)

[[]][Bugs (upstream)](https://github.com/GothenburgBitFactory/timewarrior/issues)

[[]][[#taskwarrior](ircs://irc.libera.chat/#taskwarrior)] ([[webchat](https://web.libera.chat/#taskwarrior)])

**Timewarrior** (**timew**) is a time management tool for the terminal. At its heart is a stopwatch-like timer that tags blocks of time with descriptive text. Data is stored locally in JSON format to ensure portability. From this data detailed time tracking reports can be generated. Like its sibling Taskwarrior, the Timewarrior application has a large ecosystem of [related tools](https://timewarrior.net/tools/) that have grown up around it.

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
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Timewarrior is not respecting the XDG Directory Specification]](#Timewarrior_is_not_respecting_the_XDG_Directory_Specification)
-   [[5] [Removal]](#Removal)
    -   [[5.1] [Unmerge]](#Unmerge)
-   [[6] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [app-misc/timew](https://packages.gentoo.org/packages/app-misc/timew) [[]] [Tracks your time from the command line, and generates reports]

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-24 23:26] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-misc/timew`

### [Additional software]

Timewarrior is designed to optionally integrate into [Taskwarrior](https://wiki.gentoo.org/wiki/Taskwarrior "Taskwarrior") by means of event-based hooks. To integrate the two programs [/usr/share/doc/timew-\<ver\>/ext/on-modify.timewarrior] must be copied to the [.task/] directory inside of the user\'s home.

## [Configuration]

### [Environment variables]

-   `$TIMEWARRIORDB` - specifies the location of the [timewarrior] directory.

### [Files]

-   [\~/.timewarrior/timewarrior.cfg] - the default location of user configuration data.
-   [\~/.timewarrior/data/YYYY-MM.data] - time tracking data files separated by year and month.

## [Usage]

If [timew] is run without any arguments it will provide information on any active tracking the application is performing:

`user `[`$`]`timew`

    There is no active time tracking.

Starting the time tracking process is as simple as:

`user `[`$`]`timew start`

The timer will run until it is stopped by user action:

`user `[`$`]`timew stop`

To get a summary of recently logged time:

`user `[`$`]`timew summary`

    Wk  Date       Day Tags    Start      End    Time   Total
    ‾‾  ‾‾‾‾       ‾‾‾ ‾‾‾‾    ‾‾‾‾‾      ‾‾‾    ‾‾‾‾   ‾‾‾‾‾
    W17 2023-04-26 Wed      19:31:26 19:34:00 0:02:34 0:02:34

                                                      _______
                                                      0:02:34

Tagging allows the user to track time for specific projects. Tags can be single words or, if enclosed in single quotes, multiple words long.

`user `[`$`]`timew start 'wiki edits'`

This could then display as:

`user `[`$`]`timew summary`

    Wk  Date       Day Tags          Start      End    Time   Total
    ‾‾  ‾‾‾‾       ‾‾‾ ‾‾‾‾          ‾‾‾‾‾      ‾‾‾    ‾‾‾‾   ‾‾‾‾‾
    W17 2023-04-26 Wed            19:31:26 19:34:00 0:02:34
                       wiki edits 19:57:47 19:59:28 0:01:41 0:04:15

                                                            _______
                                                            0:04:15

### [Invocation]

`user `[`$`]`timew --help`

    Usage: timew [--version]
           timew annotate @<id> [@<id> ...] <annotation>
           timew cancel
           timew config [<name> [<value> | '']]
           timew continue [@<id>] [<date>|<interval>]
           timew day [<interval>] [<tag> ...]
           timew delete @<id> [@<id> ...]
           timew diagnostics
           timew export [<interval>] [<tag> ...]
           timew extensions
           timew gaps [<interval>] [<tag> ...]
           timew get <DOM> [<DOM> ...]
           timew help [<command> | dates | dom | durations | hints | ranges]
           timew join @<id> @<id>
           timew lengthen @<id> [@<id> ...] <duration>
           timew modify (start|end) @<id> <date>
           timew month [<interval>] [<tag> ...]
           timew move @<id> <date>
           timew [report] <report> [<interval>] [<tag> ...]
           timew shorten @<id> [@<id> ...] <duration>
           timew show
           timew split @<id> [@<id> ...]
           timew start [<date>] [<tag> ...]
           timew stop [<tag> ...]
           timew summary [<interval>] [<tag> ...]
           timew tag @<id> [@<id> ...] <tag> [<tag> ...]
           timew tags [<interval>] [<tag> ...]
           timew track <interval> [<tag> ...]
           timew undo
           timew untag @<id> [@<id> ...] <tag> [<tag> ...]
           timew week [<interval>] [<tag> ...]

    Additional help:
           timew help <command>
           timew help dates
           timew help dom
           timew help durations
           timew help hints
           timew help ranges
    Additional help:
           timew help <command>
           timew help dates
           timew help dom
           timew help durations
           timew help hints
           timew help ranges

    Interval:
           [from] <date>
           [from] <date> to/- <date>
           [from] <date> for <duration>
           <duration> before/after <date>
           <duration> ago
           [for] <duration>

    Tag:
           Word
           'Single Quoted Words'
           "Double Quoted Words"
           Escaped\ Spaces

    Configuration overrides:
           rc.<name>=<value>

## [Troubleshooting]

### [Timewarrior is not respecting the XDG Directory Specification]

Curently Timewarrior has partial support for the XDG Directory specification. If the `$TIMEWARRIORDB` variable is set then [timew] will store its data at the location specified by the variable. If the directory [\~/.timewarrior/] exists and the `$TIMEWARRIORDB` variable is not set, then this directory is used by [timew] to store data. If neither of these conditions are true, [\$XDG_CONFIG_HOME/timewarrior/] is used instead.

Provided [timew] is not running, moving an existing Timewarrior data directory from its legacy location to its XDG location should be as simple as:

`user `[`$`]`mv ~/.timewarrior $XDG_CONFIG_HOME/timewarrior`

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose app-misc/timew`

## [See also]

-   [Taskwarrior](https://wiki.gentoo.org/wiki/Taskwarrior "Taskwarrior") --- to-do list manager for the command line
-   [Visual Interactive Taskwarrior](https://wiki.gentoo.org/wiki/Visual_Interactive_Taskwarrior "Visual Interactive Taskwarrior") --- curses-based front-end for [Taskwarrior](https://wiki.gentoo.org/wiki/Taskwarrior "Taskwarrior") with [vim](https://wiki.gentoo.org/wiki/Vim "Vim")-like keybindings.