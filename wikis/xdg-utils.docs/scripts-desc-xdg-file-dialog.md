# Scripts / Desc / Xdg File Dialog

2006

Kevin

Krammer

kevin.krammer@gmx.at

This is release 0.5 of the xdg-mime Manual.

xdg-file-dialog

1

xdg-file-dialog

command line tool for providing file and directory selection dialogs

xdg-file-dialog

openfilename

--title

TITLE

FILENAME

xdg-file-dialog

openfilenamelist

--title

TITLE

FILENAME

xdg-file-dialog

savefilename

--title

TITLE

FILENAME

xdg-file-dialog

directory

--title

TITLE

DIRNAME

xdg-file-dialog

--help

--manual

--version

# Description

The xdg-file-dialog program can be used to let the native file selection dialog handle file and directory input.

xdg-file-dialog is for use inside a desktop session only. It is not recommended to use xdg-file-dialog as root.

# Commands

openfilename
Returns the filename with path for a file to read from. \<FILENAME\> can optionally be used to specify path and filename of a preselection.

openfilenamelist
Returns one or more filenames with path for files to read from, each on a new line. \<FILENAME\> can optionally be used to specify path and filename of a preselection.

savefilename
Returns the filename with path for file to write to. \<FILENAME\> can optionally be used to specify path and filename of a preselection.

directory
Returns the path for an existing directory. \<DIRNAME\> can optionally be used to specify a path of a preselection.

# Options

`--title` \<TITLE\>
Sets the dialog's title (caption) to the specified text.

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

    xdg-file-dialog savefilename /tmp/foobar.png

Asks for a save file name starting in directory /tmp and suggesting foobar.png as the filename

    xdg-file-dialog directory --title "Select a target folder" /tmp

Asks for a directory name starting in directory /tmp using the text "Select a target folder" as the dialog's title/caption.
