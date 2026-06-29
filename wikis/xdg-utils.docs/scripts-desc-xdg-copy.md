# Scripts / Desc / Xdg Copy

2006

Kevin

Krammer

kevin.krammer@gmx.at

Jeremy

White

jwhite@codeweavers.com

This is release 0.5 of the xdg-copy Manual.

xdg-copy

1

xdg-copy

command line tool for copying files between desktop URIs

xdg-copy

source

destination

xdg-copy

--help

--manual

--version

# Description

xdg-copy copies \<source\> to \<destination\> and provides visual feedback to the user during the operation. Both \<source\> and \<destination\> can either be a file or URL. Supported URL types are file, ftp, http and https. Additional URL types may be supported depending on the desktop environment.

xdg-copy is for use inside a desktop session only. It is not recommended to use xdg-copy as root.

# Options

`--help`
Show command synopsis.

`--manual`
Show this manual page.

`--version`
Show the xdg-utils version information.

# Exit Codes

An exit code of 0 indicates success while a non-zero exit code indicates failure. The following failure codes can be returned:

`1`
Error in command line syntax.

`2`
One of the files passed on the command line did not exist.

`3`
A required tool could not be found.

`4`
The action failed.

# See Also

`xdg-utils-common(7)`

# Examples

    xdg-copy "http://portland.freedesktop.org/png/freedesktop-logo.png" .

    xdg-copy "/tmp/foobar.png" "/home/user/foobar-copy.png"
