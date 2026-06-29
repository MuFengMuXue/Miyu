## Name

systemd-pty-forward — Run a command with a custom terminal background color or title

## Synopsis

`systemd-pty-forward` \[OPTIONS...\] {COMMAND}

## Description

**systemd-pty-forward** can be used to run a command with a custom terminal background color or title.

## Options

The following options are understood:

`--background=`*`COLOR`*  
Change the terminal background color to the specified ANSI color as long as the command runs. The color specified should be an ANSI X3.64 SGR background color, i.e. strings such as "`40`", "`41`", …, "`47`", "`48;2;…`", "`48;5;…`". See ANSI Escape Code (Wikipedia) for details.

Example: "`--background=44`" for a blue background.

Added in version 258.

`--title=`*`TITLE`*  
Change the terminal title to the specified string as long as the command runs.

Added in version 258.

`--quiet`, `-q`  
Suppresses additional informational output while running.

Added in version 258.

`--read-only`  
Do not accept any user input on standard input.

Added in version 258.

`-h`, `--help`  
Print a short help text and exit.

`--version`  
Print a short version string and exit.
