[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Sed&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.gnu.org/software/sed/)

[[]][Official documentation](https://www.gnu.org/software/sed/manual/)

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/sed)

[[]][Wikipedia](https://en.wikipedia.org/wiki/sed "wikipedia:sed")

[[]][Man page](http://man7.org/linux/man-pages/man1/sed.1.html)

[[]][[#sed](ircs://irc.libera.chat/#sed)] ([[webchat](https://web.libera.chat/#sed)])

**sed** (*s*tream *ed*itor) is a program that uses regular expressions to programmatically modify streams of text. In meany ways [sed] is an evolved [ed] with significantly more advanced scripting capabilities than its predecessor. Where [ed] sees occasional use as a means to edit individual lines within a file [sed] is commonly used to transform entire documents. In this capacity [sed] has historically been second only to [Perl](https://wiki.gentoo.org/wiki/Perl "Perl") --- which has the advantage of being a complete programming language it its own right --- in its ability to rapidly manipulate large quantities of text with regular expressions. In modern environments that require grapheme-level Unicode support or recursive grammars, [Raku](https://wiki.gentoo.org/wiki/Raku "Raku") occasionally edges-out both [sed] and Perl for such workloads.

The [sed] utility is [specified by](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/sed.html#tag_20_109) [POSIX](https://wiki.gentoo.org/wiki/POSIX "POSIX"). By default, Gentoo installs [GNU sed](https://www.gnu.org/software/sed/), [[[sys-apps/sed]](https://packages.gentoo.org/packages/sys-apps/sed)[]], as part of the \@system set; it can be called with the `--posix` option to behave as required by POSIX.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Usage]](#Usage)
    -   [[1.4] [Unmerge]](#Unmerge)
-   [[2] [See also]](#See_also)
-   [[3] [External references]](#External_references)

## [Installation]

sed is part of [\@system](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)") and needs no separate installation.

### [USE flags]

### [USE flags for] [sys-apps/sed](https://packages.gentoo.org/packages/sys-apps/sed) [[]] [Super-useful stream editor]

  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`acl`](https://packages.gentoo.org/useflags/acl)                 Add support for Access Control Lists
  [`nls`](https://packages.gentoo.org/useflags/nls)                 Add Native Language Support (using gettext - GNU locale utilities)
  [`selinux`](https://packages.gentoo.org/useflags/selinux)         !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`static`](https://packages.gentoo.org/useflags/static)           !!do not set this during bootstrap!! Causes binaries to be statically linked instead of dynamically
  [`test-full`](https://packages.gentoo.org/useflags/test-full)     Run expensive tests (mostly CPU intensive).
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-18 14:03] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask sys-apps/sed`

### [Usage]

The article in the [devmanual](https://devmanual.gentoo.org/tools-reference/sed/index.html) might help.

`user `[`$`]`sed --help`

    Usage: sed [OPTION]...  [input-file]...

      -n, --quiet, --silent
                     suppress automatic printing of pattern space
          --debug
                     annotate program execution
      -e script, --expression=script
                     add the script to the commands to be executed
      -f script-file, --file=script-file
                     add the contents of script-file to the commands to be executed
      --follow-symlinks
                     follow symlinks when processing in place
      -i[SUFFIX], --in-place[=SUFFIX]
                     edit files in place (makes backup if SUFFIX supplied)
      -l N, --line-length=N
                     specify the desired line-wrap length for the `l' command
      --posix
                     disable all GNU extensions.
      -E, -r, --regexp-extended
                     use extended regular expressions in the script
                     (for portability use POSIX -E).
      -s, --separate
                     consider files as separate rather than as a single,
                     continuous long stream.
          --sandbox
                     operate in sandbox mode (disable e/r/w commands).
      -u, --unbuffered
                     load minimal amounts of data from the input files and flush
                     the output buffers more often
      -z, --null-data
                     separate lines by NUL characters
          --help     display this help and exit
          --version  output version information and exit

    If no -e, --expression, -f, or --file option is given, then the first
    non-option argument is taken as the sed script to interpret.  All
    remaining arguments are names of input files; if no input files are
    specified, then the standard input is read.

    GNU sed home page: <https://www.gnu.org/software/sed/>.
    General help using GNU software: <https://www.gnu.org/gethelp/>.
    E-mail bug reports to: <bug-sed@gnu.org>.

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose sys-apps/sed`

## [See also]

-   [ed](https://wiki.gentoo.org/wiki/Ed "Ed") --- a [line-based](https://en.wikipedia.org/wiki/Line_editor "wikipedia:Line editor") text editor with support for regular expressions
-   [grep](https://wiki.gentoo.org/wiki/Grep "Grep") --- a tool for searching text files with regular expressions
-   [awk](https://wiki.gentoo.org/wiki/Awk "Awk") --- a scripting language for data extraction
-   [Perl](https://wiki.gentoo.org/wiki/Perl "Perl") --- a general purpose interpreted programming language with a powerful regular expression engine.
-   [Raku](https://wiki.gentoo.org/wiki/Raku "Raku") --- a high-level, general-purpose, and gradually typed programming language with low boilerplate objects, optionally immutable data structures, and an advanced macro system.

## [External references]

-   [sed documentation in the devmanual](https://devmanual.gentoo.org/tools-reference/sed/index.html)
-   [https://edoras.sdsu.edu/doc/sed-oneliners.html](https://edoras.sdsu.edu/doc/sed-oneliners.html)
-   [https://learnbyexample.github.io/learn_gnused/](https://learnbyexample.github.io/learn_gnused/)