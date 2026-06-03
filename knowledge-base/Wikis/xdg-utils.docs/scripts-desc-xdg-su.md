# Scripts / Desc / Xdg Su

2006

Kevin

Krammer

kevin.krammer@gmx.at

Jeremy

White

jwhite@codeweavers.com

This is release 0.5 of the xdg-su Manual.

xdg-su

1

xdg-su

run a GUI program as another user (typically root) after prompting for that user's password

xdg-su

-u

user

-c

command

xdg-su

--help

--manual

--version

# Description

xdg-su provides a graphical dialog that prompts the user for a password to run \<command\> as \<user\> or as root if no user was specified.

xdg-su is for use inside a desktop session only.

xdg-su discards any stdout and stderr output from \<command\>.

# Options

`-c command`
the command to run. This argument is mandatory.

`-u user`
run \<command\> as \<user\>. The default is to run as root.

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

`su(1)`, `xdg-utils-common(7)`

# Examples

    xdg-su -u root -c "/opt/shinythings/bin/install-GUI --install fast"

Runs the /opt/shinythings/bin/install-GUI command with root permissions.
