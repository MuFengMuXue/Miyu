**Resources**

[[]][Home](http://gondor.apana.org.au/~herbert/dash/)

[[]][Package information](https://packages.gentoo.org/packages/app-shells/dash)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Debian_Almquist_shell "wikipedia:Debian Almquist shell")

[[]][GitWeb](https://git.kernel.org/pub/scm/utils/dash/dash.git)

**dash** is the Debian Almquist shell: a small, fast, and [POSIX](https://wiki.gentoo.org/wiki/POSIX "POSIX")-compliant [shell](https://wiki.gentoo.org/wiki/Shell "Shell"). It is well-suited for startup scripts, and is used on Debian (and derivative distributions) as [/bin/sh].

As some shell scripts may have \"bashisms\" in them, dash is not guaranteed to work as a [/bin/sh] replacement on Gentoo, out-of-the-box.

See the [terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator#General_usage "Terminal emulator") article for some general usage pointers, though dash is not often used in interactive mode.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Garbled display]](#Garbled_display)
-   [[4] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [app-shells/dash](https://packages.gentoo.org/packages/app-shells/dash) [[]] [Debian Almquist Shell]

  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------
  [`libedit`](https://packages.gentoo.org/useflags/libedit)   Use the libedit library (replacement for readline)
  [`static`](https://packages.gentoo.org/useflags/static)     !!do not set this during bootstrap!! Causes binaries to be statically linked instead of dynamically
  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-09 21:13] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-shells/dash`

## [Configuration]

See the article on on [shell configuration](https://wiki.gentoo.org/wiki/Shell#Configuration "Shell") for more info.

## [Troubleshooting]

### [Garbled display]

The output of a shell can, in some conditions, become corrupt. See the [terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator#Garbled_display "Terminal emulator") article for instructions to help fix this.

## [See also]

-   [Shell](https://wiki.gentoo.org/wiki/Shell "Shell") --- command-line interpreter that provides a text-based interface to users
-   [Bash](https://wiki.gentoo.org/wiki/Bash "Bash") --- the default shell on Gentoo systems and a popular [shell](https://wiki.gentoo.org/wiki/Shell "Shell") program found on many Linux systems.
-   [Fish](https://wiki.gentoo.org/wiki/Fish "Fish") --- a smart and user-friendly command line [shell](https://wiki.gentoo.org/wiki/Shell "Shell") for OS X, Linux, and the rest of the family.
-   [Zsh](https://wiki.gentoo.org/wiki/Zsh "Zsh") --- an interactive login shell that can also be used as a powerful scripting language interpreter.
-   [Nushell](https://wiki.gentoo.org/wiki/Nushell "Nushell") --- a new kind of [shell](https://wiki.gentoo.org/wiki/Shell "Shell") for OS X, Linux, and Windows.