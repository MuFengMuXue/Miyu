# Scripts / Desc / Xdg Realpath

2023

Slatian

baschdel+xdg-utils@disroot.org

Kevin

Krammer

Jeremy

White

xdg-utils 1.2

xdg-realpath

1

xdg-realpath

Canonicalizes filepaths in a consistent way.

xdg-realpath

--

file

xdg-realpath

--get-backend

xdg-realpath

--help

--manual

--version

# Description

xdg-realpath canonicalizes filepaths using the installed `realpath` or `readlink -f` implementation, automatically choosing the right calling conventions so you don't have to worry about it.

Canonicalization happens by resolving relative paths and symbolic links resulting in an absolute path to a file. It fails if the path does not lead to any kind file or directory.

It is strongly recommended to call xdg-realpath using the `--` option.

When using xdg-realpath with multiple files and one of the given paths leads directly or indirectly to a missing file a message will be printed to stdout and xdg-realpath will continue resolving until it has finished with all given paths. If at least one path does not resolve, it will return an exit code 2.

Unlike `realpath` or `readlink -f` xdg-realpath will error if one attempts to resolve a non-existing file in an existing directory. If such behavior is added in the future it will be behind a command line flag.

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

# Environment Variables

xdg-realpath honours the following environment variables:

XDG_UTILS_REALPATH_BACKEND
When left empty (recommended) xdg-realpath automatically chooses an appropriate backend. Possible values are `realpath`, `busybox-realpath` and `readlink`. This is also used by other scripts from the xdg-utils family.

Setting this variable has the possibility to break a lot of things. It is primarily intended for testing and quick-fixing. *If you are not the local system administrator or a distribution maintainer leave it alone!*

The `--get-backend` option will print the used backend.

# See Also

`realpath(1)`, `readlink(1)`, `xdg-utils-common(7)`

# Examples

    xdg-realpath -- /./bin

Canonicalizes the path to `/./bin`, on most systems the output will be `/bin` or `/usr/bin`.

    xdg-realpath -- foo.txt

Will print the absolute path of the file foo.txt or inform you that foo.txt doesn't exist.

    xdg-realpath -- .

Will print the present working directory path with symbolic links resolved.
