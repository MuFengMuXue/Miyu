[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Grep&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.gnu.org/software/grep/)

[[]][Official documentation](https://www.gnu.org/software/grep/manual/)

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/grep)

[[]][Wikipedia](https://en.wikipedia.org/wiki/grep "wikipedia:grep")

[[]][Man page](http://man7.org/linux/man-pages/man1/grep.1.html)

**grep** is a tool for searching text files with regular expressions. Its name is a play on the [[ed](https://wiki.gentoo.org/wiki/Ed "Ed")] command [g/re/p] which would globally search a document for a given regular expression and print the results.

There are multiple implementations of [grep]. By default, Gentoo installs [GNU Grep](https://www.gnu.org/s/grep/manual/grep.html) ([[[sys-apps/grep]](https://packages.gentoo.org/packages/sys-apps/grep)[]]), as part of the \@system set. GNU Grep can be configured to behave [as required by](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/grep.html#tag_20_55) [POSIX](https://wiki.gentoo.org/wiki/POSIX "POSIX") via the `POSIXLY_CORRECT` environment variable; refer to the GNU [[[grep(1)]](https://man.archlinux.org/man/grep.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page for further information.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Environment variables]](#Environment_variables)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [sys-apps/grep](https://packages.gentoo.org/packages/sys-apps/grep) [[]] [GNU regular expression matcher]

  --------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+egrep-fgrep`](https://packages.gentoo.org/useflags/+egrep-fgrep)   Install deprecated \'egrep\' and \'fgrep\' wrappers for \'grep -E\' and \'grep -F\' respectively. GNU grep 3.8 onwards warns about their usage by default, but the versions installed by this flag do not. No deprecation warnings are emitted when this flag is enabled.
  [`nls`](https://packages.gentoo.org/useflags/nls)                     Add Native Language Support (using gettext - GNU locale utilities)
  [`pcre`](https://packages.gentoo.org/useflags/pcre)                   Add support for Perl Compatible Regular Expressions
  [`static`](https://packages.gentoo.org/useflags/static)               !!do not set this during bootstrap!! Causes binaries to be statically linked instead of dynamically
  [`test-full`](https://packages.gentoo.org/useflags/test-full)         Run expensive tests (mostly CPU intensive).
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)       Verify upstream signatures on distfiles
  --------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-01-15 17:58] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[sys-apps/grep]](https://packages.gentoo.org/packages/sys-apps/grep)[]]:

`root `[`#`]`emerge --ask sys-apps/grep`

## [Configuration]

### [Environment variables]

-   `GREP_COLOR` (deprecated) colorizes matching text, by default this is set to 01;31 which is a bold red.
-   `GREP_COLORS` sets the color of various parts of output, not just matches.
-   `LC_ALL`, `LC_COLLATE`, `LANG` specify the locale for the collating sequence.
-   `LC_ALL`, `LC_CTYPE`, `LANG` determines the encoding of characters and their attributes.
-   `LC_ALL, LC_MESSAGES, LANG` determines the language grep uses for messages.
-   `POSIXLY_CORRECT` treat all input after a file name as an additional file name among other things.

## [Usage]

** See also**\
For more information see [devmanual](https://devmanual.gentoo.org/tools-reference/grep/).

### [Invocation]

To see grep usage information:

`user `[`$`]`grep --help`

    Usage: grep [OPTION]... PATTERNS [FILE]...
    Search for PATTERNS in each FILE.
    Example: grep -i 'hello world' menu.h main.c
    PATTERNS can contain multiple patterns separated by newlines.

    Pattern selection and interpretation:
      -E, --extended-regexp     PATTERNS are extended regular expressions
      -F, --fixed-strings       PATTERNS are strings
      -G, --basic-regexp        PATTERNS are basic regular expressions
      -P, --perl-regexp         PATTERNS are Perl regular expressions
      -e, --regexp=PATTERNS     use PATTERNS for matching
      -f, --file=FILE           take PATTERNS from FILE
      -i, --ignore-case         ignore case distinctions in patterns and data
          --no-ignore-case      do not ignore case distinctions (default)
      -w, --word-regexp         match only whole words
      -x, --line-regexp         match only whole lines
      -z, --null-data           a data line ends in 0 byte, not newline

    Miscellaneous:
      -s, --no-messages         suppress error messages
      -v, --invert-match        select non-matching lines
      -V, --version             display version information and exit
          --help                display this help text and exit

    Output control:
      -m, --max-count=NUM       stop after NUM selected lines
      -b, --byte-offset         print the byte offset with output lines
      -n, --line-number         print line number with output lines
          --line-buffered       flush output on every line
      -H, --with-filename       print file name with output lines
      -h, --no-filename         suppress the file name prefix on output
          --label=LABEL         use LABEL as the standard input file name prefix
      -o, --only-matching       show only nonempty parts of lines that match
      -q, --quiet, --silent     suppress all normal output
          --binary-files=TYPE   assume that binary files are TYPE;
                                TYPE is 'binary', 'text', or 'without-match'
      -a, --text                equivalent to --binary-files=text
      -I                        equivalent to --binary-files=without-match
      -d, --directories=ACTION  how to handle directories;
                                ACTION is 'read', 'recurse', or 'skip'
      -D, --devices=ACTION      how to handle devices, FIFOs and sockets;
                                ACTION is 'read' or 'skip'
      -r, --recursive           like --directories=recurse
      -R, --dereference-recursive  likewise, but follow all symlinks
          --include=GLOB        search only files that match GLOB (a file pattern)
          --exclude=GLOB        skip files that match GLOB
          --exclude-from=FILE   skip files that match any file pattern from FILE
          --exclude-dir=GLOB    skip directories that match GLOB
      -L, --files-without-match  print only names of FILEs with no selected lines
      -l, --files-with-matches  print only names of FILEs with selected lines
      -c, --count               print only a count of selected lines per FILE
      -T, --initial-tab         make tabs line up (if needed)
      -Z, --null                print 0 byte after FILE name

    Context control:
      -B, --before-context=NUM  print NUM lines of leading context
      -A, --after-context=NUM   print NUM lines of trailing context
      -C, --context=NUM         print NUM lines of output context
      -NUM                      same as --context=NUM
          --group-separator=SEP  print SEP on line between matches with context
          --no-group-separator  do not print separator for matches with context
          --color[=WHEN],
          --colour[=WHEN]       use markers to highlight the matching strings;
                                WHEN is 'always', 'never', or 'auto'
      -U, --binary              do not strip CR characters at EOL (MSDOS/Windows)

    When FILE is '-', read standard input.  With no FILE, read '.' if
    recursive, '-' otherwise.  With fewer than two FILEs, assume -h.
    Exit status is 0 if any line is selected, 1 otherwise;
    if any error occurs and -q is not given, the exit status is 2.

    Report bugs to: bug-grep@gnu.org
    GNU grep home page: <https://www.gnu.org/software/grep/>
    General help using GNU software: <https://www.gnu.org/gethelp/>

## [Removal]

### [Unmerge]

Remove [[[sys-apps/grep]](https://packages.gentoo.org/packages/sys-apps/grep)[]]:

`root `[`#`]`emerge --ask --depclean --verbose sys-apps/grep`

## [See also]

-   [awk](https://wiki.gentoo.org/wiki/Awk "Awk") --- a scripting language for data extraction
-   [ed](https://wiki.gentoo.org/wiki/Ed "Ed") --- a [line-based](https://en.wikipedia.org/wiki/Line_editor "wikipedia:Line editor") text editor with support for regular expressions
-   [Perl](https://wiki.gentoo.org/wiki/Perl "Perl") --- a general purpose interpreted programming language with a powerful regular expression engine.
-   [Raku](https://wiki.gentoo.org/wiki/Raku "Raku") --- a high-level, general-purpose, and gradually typed programming language with low boilerplate objects, optionally immutable data structures, and an advanced macro system.
-   [ripgrep](https://wiki.gentoo.org/wiki/Ripgrep "Ripgrep") --- search tool that can recursively search directories for regex search patterns
-   [sed](https://wiki.gentoo.org/wiki/Sed "Sed") --- a program that uses regular expressions to programmatically modify streams of text