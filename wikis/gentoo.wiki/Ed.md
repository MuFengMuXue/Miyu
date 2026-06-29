[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Ed&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.gnu.org/software/ed/)

[[]][Official documentation](https://www.gnu.org/software/ed/manual/ed_manual.html)

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/ed)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Ed_(text_editor) "wikipedia:Ed (text editor)")

[[]][Man page](http://man7.org/linux/man-pages/man1/ed.1.html)

**ed** (pronounced *E.D.*) is a [line-based](https://en.wikipedia.org/wiki/Line_editor "wikipedia:Line editor") text editor with support for regular expressions.

[ed] is one of the oldest text editors that still sees use today, and has its place deep in the history of UNIX(like) operating systems. The line-based nature of [ed] is a result of the fact that it was written at a time when teletype machines were the common user interface of the day, and CRT monitors --- then often called \"glass teletypes\" --- were rare and expensive.

[ed] inspired the clone [ex](https://en.wikipedia.org/wiki/Ex_(text_editor) "wikipedia:Ex (text editor)"), which served as the basis for [vi](https://wiki.gentoo.org/wiki/Vi "Vi"). vi still has an ex mode, analogous to ed.

In current practice it is uncommon to use [ed] interactively, but it sees occasional use as an embedded means to automate edits to files from within a shell script.

The [ed] utility is [specified by the](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/ed.html) [POSIX](https://wiki.gentoo.org/wiki/POSIX "POSIX") standard.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
    -   [[1.2] [Files]](#Files)
    -   [[1.3] [Invocation]](#Invocation)
-   [[2] [Removal]](#Removal)
    -   [[2.1] [Unmerge]](#Unmerge)
-   [[3] [See also]](#See_also)

## [Installation]

### [Emerge]

`root `[`#`]`emerge --ask sys-apps/ed`

### [Files]

-   [./ed.hup] or [\$HOME/ed.hup] - where [ed] dumps the current write buffer if the terminal hangs up unexpectedly.

### [Invocation]

`user `[`$`]`ed --help`

    GNU ed is a line-oriented text editor. It is used to create, display,
    modify and otherwise manipulate text files, both interactively and via
    shell scripts. A restricted version of ed, red, can only edit files in
    the current directory and cannot execute shell commands. Ed is the
    'standard' text editor in the sense that it is the original editor for
    Unix, and thus widely available. For most purposes, however, it is
    superseded by full-screen editors such as GNU Emacs or GNU Moe.

    Usage: ed [options] [file]

    Options:
      -h, --help                 display this help and exit
      -V, --version              output version information and exit
      -E, --extended-regexp      use extended regular expressions
      -G, --traditional          run in compatibility mode
      -l, --loose-exit-status    exit with 0 status even if a command fails
      -p, --prompt=STRING        use STRING as an interactive prompt
      -r, --restricted           run in restricted mode
      -s, --quiet, --silent      suppress diagnostics, byte counts and '!' prompt
      -v, --verbose              be verbose; equivalent to the 'H' command

    Start edit by reading in 'file' if given.
    If 'file' begins with a '!', read output of shell command.

    Exit status: 0 for a normal exit, 1 for environmental problems (file
    not found, invalid flags, I/O errors, etc), 2 to indicate a corrupt or
    invalid input file, 3 for an internal consistency error (eg, bug) which
    caused ed to panic.

    Report bugs to bug-ed@gnu.org
    Ed home page: http://www.gnu.org/software/ed/ed.html
    General help using GNU software: http://www.gnu.org/gethelp

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose sys-apps/ed`

## [See also]

-   [sed](https://wiki.gentoo.org/wiki/Sed "Sed") --- a program that uses regular expressions to programmatically modify streams of text
-   [grep](https://wiki.gentoo.org/wiki/Grep "Grep") --- a tool for searching text files with regular expressions
-   [awk](https://wiki.gentoo.org/wiki/Awk "Awk") --- a scripting language for data extraction
-   [Perl](https://wiki.gentoo.org/wiki/Perl "Perl") --- a general purpose interpreted programming language with a powerful regular expression engine.
-   [Raku](https://wiki.gentoo.org/wiki/Raku "Raku") --- a high-level, general-purpose, and gradually typed programming language with low boilerplate objects, optionally immutable data structures, and an advanced macro system.