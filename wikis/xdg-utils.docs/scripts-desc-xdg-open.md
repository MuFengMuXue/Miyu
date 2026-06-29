# Scripts / Desc / Xdg Open

2006

Kevin

Krammer

kevin.krammer@gmx.at

Jeremy

White

jwhite@codeweavers.com

xdg-utils 1.0

xdg-open

1

xdg-open

opens files and/or URLs in the user's preferred applications

xdg-open

--nowait

--

file

URL

xdg-open

--help

--manual

--version

# Description

xdg-open opens the given files and/or URLs in the user's preferred applications.

xdg-open is for use inside a desktop session only. It is not recommended to use xdg-open as root.

As xdg-open can not handle arguments that begin with a “-” it is recommended to pass filepaths in one of the following ways:

- Pass absolute paths, i.e. by using `xdg-realpath` as a preprocessor.

- Prefix known relative filepaths with a “./”. For example using `sed -E 's|^[^/]|./\0|'`.

- Pass a file URL.

# Options

`--`
Indicate that whatever follows is a filename or URL, not an option.

This option is new and incompatible with older releases! Consider escaping or using realpath instead.

Internally this will the prefix escaping strategy for filenames that begin with hyphens outlined above.

`--nowait`
Do not wait for the opener to exit after launching the last URL.

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
At least one file or URL could not be opened.

In case of success the process launched from the .desktop file will not be forked off and therefore may result in xdg-open running for a very long time. This behaviour intentionally differs from most desktop specific openers to allow terminal based applications to run using the same terminal xdg-open was called from.

# Environment

xdg-open honors the following environment variables:

`BROWSER`
May contain a command that is used to open a filepath or URL when no other appropriate opener was found. The Path or URL will be appended as the last argument.

No parsing beyond splitting arguments on space characters should be assumed. Quoting is not supported. Be careful with ':' and '%' characters.

The following two features are supported in xdg-open only, but not by other applications that make use of the `BROWSER` variable. Using them is no longer recommended.

This environment variable may contain a colon separated list of commands if one command fails the command after it will be tried.

When using `%s` as a placeholder the first instance of it will be replaced with the filepath or URL to be opened instead of appending it as the last argument.

# Reporting Issues

Please keep in mind `xdg-open` inherits most of the flaws of its configuration and the underlying opener.

In case the command `xdg-mime query default "$(xdg-mime query filetype path/to/troublesome_file)"` names the program responsible for any unexpected behaviour you can fix that by setting a different handler. (If the program is broken let the developers know)

Also see the security note on `xdg-mime(1)` for the `default` subcommand.

If a flaw is reproducible using the desktop specific opener (and isn't a configuration issue): Please report to whoever is responsible for that first (reporting to xdg-utils is better than not reporting at all, but since the xdg-utils are maintained in very little spare time a fix will take much longer)

In case an issue specific to xdg-open please report it to <https://gitlab.freedesktop.org/xdg/xdg-utils/-/issues> .

# See Also

`xdg-mime(1)`, `xdg-settings(1)`, `xdg-realpath(1)`, `xdg-utils-common(7)`, [MIME applications associations specification](http://www.freedesktop.org/wiki/Specifications/mime-apps-spec/)

# Examples

    xdg-open 'http://www.freedesktop.org/'

Opens the freedesktop.org website in the user's default browser.

    xdg-open /tmp/foobar.png

Opens the PNG image file /tmp/foobar.png in the user's default image viewing application.
