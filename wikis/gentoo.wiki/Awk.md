[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Awk&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.gnu.org/software/gawk/)

[[]][Official documentation](https://www.gnu.org/software/gawk/manual/)

[[]][Package information](https://packages.gentoo.org/packages/app-alternatives/awk)

[[]][Wikipedia](https://en.wikipedia.org/wiki/awk "wikipedia:awk")

[[]][Official project wiki](http://awk.freeshell.org/)

[[]][Man page](http://man7.org/linux/man-pages/man1/awk.1p.html)

[[]][Man page](http://man7.org/linux/man-pages/man1/gawk.1.html)

[[]][[comp.lang.awk](news:comp.lang.awk) ([weblink](https://www.novabbs.com/devel/thread.php?group=comp.lang.awk))]

[[]][[#awk](ircs://irc.libera.chat/#awk)] ([[webchat](https://web.libera.chat/#awk)])

**awk** is a scripting language for data extraction often used in tandem with [[sed](https://wiki.gentoo.org/wiki/Sed "Sed")] and [[grep](https://wiki.gentoo.org/wiki/Grep "Grep")] for complex reporting needs. While large [awk] programs are possible, the language itself was intended primarily to be used to construct one-liners to filter data and perform simple computations.

The [awk] utility [is specified by](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/awk.html#tag_20_06) [POSIX](https://wiki.gentoo.org/wiki/POSIX "POSIX"); several versions of awk are provided by Gentoo. A specific implementation may be selected with [Project:Base/Alternatives](https://wiki.gentoo.org/wiki/Project:Base/Alternatives "Project:Base/Alternatives"). By default [GNU awk](https://www.gnu.org/software/gawk/), [[[sys-apps/gawk]](https://packages.gentoo.org/packages/sys-apps/gawk)[]], will be pulled in, and that implementation will be used as an example for this article. However, the behavior required by POSIX can be requested via the `-P`/`--posix` option or the `POSIXLY_CORRECT` environment variable; refer to the [[[gawk(1)]](https://man.archlinux.org/man/gawk.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page for further information.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Environment variables]](#Environment_variables)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
    -   [[3.2] [Usage in ebuilds]](#Usage_in_ebuilds)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation]

Installation usually happens by [Unpacking the stage tarball](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Stage#Unpacking_the_stage_tarball "Handbook:AMD64/Installation/Stage").

### [USE flags]

The [[[app-alternatives/awk]](https://packages.gentoo.org/packages/app-alternatives/awk)[]] [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag") select which version of awk to pull in:

### [USE flags for] [app-alternatives/awk](https://packages.gentoo.org/packages/app-alternatives/awk) [[]] [/bin/awk and /usr/bin/awk symlinks]

  --------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------
  [`+gawk`](https://packages.gentoo.org/useflags/+gawk)           Symlink to sys-apps/gawk
  [`busybox`](https://packages.gentoo.org/useflags/busybox)       Symlink to sys-apps/busybox
  [`mawk`](https://packages.gentoo.org/useflags/mawk)             Symlink to sys-apps/mawk (warning: mawk is not fully POSIX-compliant)
  [`nawk`](https://packages.gentoo.org/useflags/nawk)             Symlink to sys-apps/nawk
  [`split-usr`](https://packages.gentoo.org/useflags/split-usr)   Enable behavior to support maintaining /bin, /lib\*, /sbin and /usr/sbin separately from /usr/bin and /usr/lib\*
  --------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-19 09:51] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

By default, [[[sys-apps/gawk]](https://packages.gentoo.org/packages/sys-apps/gawk)[]] will be pulled in. To use a different implementation of awk, set the appropriate USE flags on [[[app-alternatives/awk]](https://packages.gentoo.org/packages/app-alternatives/awk)[]] in [package.use](https://wiki.gentoo.org/wiki//etc/portage/package.use "/etc/portage/package.use").

USE flags for [[[sys-apps/gawk]](https://packages.gentoo.org/packages/sys-apps/gawk)[]]:

### [USE flags for] [sys-apps/gawk](https://packages.gentoo.org/packages/sys-apps/gawk) [[]] [GNU awk pattern-matching language]

  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------
  [`+mpfr`](https://packages.gentoo.org/useflags/+mpfr)             Use dev-libs/mpfr for high precision arithmetic (-M / \--bignum)
  [`nls`](https://packages.gentoo.org/useflags/nls)                 Add Native Language Support (using gettext - GNU locale utilities)
  [`pma`](https://packages.gentoo.org/useflags/pma)                 Experimental Persistent Memory Allocator (PMA) support which allows persistence of variables, arrays, and user-defined functions across runs.
  [`readline`](https://packages.gentoo.org/useflags/readline)       Enable support for libreadline, a GNU line-editing library that almost everyone wants
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-02 17:50] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install awk:

`root `[`#`]`emerge --ask app-alternatives/awk`

## [Configuration]

### [Environment variables]

-   `AWKPATH` a list of directories searches to find file names passed at runtime with the `--file` option.
-   `AWKLIBPATH` a list of directories searches to find file names passed at runtime with the `--load` option.
-   `GAWK_READ_TIMEOUT` the amount of time (in milliseconds) awk waits for input before giving up. (for [[[sys-apps/gawk]](https://packages.gentoo.org/packages/sys-apps/gawk)[]])
-   `GAWK_SOCK_RETRIES` the total number of retries when reading data from a socket. (for [[[sys-apps/gawk]](https://packages.gentoo.org/packages/sys-apps/gawk)[]])
-   `GAWK_MSEC_SLEEP` the amount of time (in milliseconds) awk sleeps between retries. (for [[[sys-apps/gawk]](https://packages.gentoo.org/packages/sys-apps/gawk)[]])
-   `POSIXLY_CORRECT` duplicates the `--posix` switch.

## [Usage]

### [Invocation]

Invocation information for [[[sys-apps/gawk]](https://packages.gentoo.org/packages/sys-apps/gawk)[]]:

`user `[`$`]`awk --help`

    Usage: awk [POSIX or GNU style options] -f progfile [--] file ...
    Usage: awk [POSIX or GNU style options] [--] 'program' file ...
    POSIX options:      GNU long options: (standard)
        -f progfile     --file=progfile
        -F fs           --field-separator=fs
        -v var=val      --assign=var=val
    Short options:      GNU long options: (extensions)
        -b          --characters-as-bytes
        -c          --traditional
        -C          --copyright
        -d[file]        --dump-variables[=file]
        -D[file]        --debug[=file]
        -e 'program-text'   --source='program-text'
        -E file         --exec=file
        -g          --gen-pot
        -h          --help
        -i includefile      --include=includefile
        -I          --trace
        -l library      --load=library
        -L[fatal|invalid|no-ext]    --lint[=fatal|invalid|no-ext]
        -M          --bignum
        -N          --use-lc-numeric
        -n          --non-decimal-data
        -o[file]        --pretty-print[=file]
        -O          --optimize
        -p[file]        --profile[=file]
        -P          --posix
        -r          --re-interval
        -s          --no-optimize
        -S          --sandbox
        -t          --lint-old
        -V          --version

    To report bugs, see node `Bugs' in `gawk.info'
    which is section `Reporting Problems and Bugs' in the
    printed version.  This same information may be found at
    https://www.gnu.org/software/gawk/manual/html_node/Bugs.html.
    PLEASE do NOT try to report bugs by posting in comp.lang.awk,
    or by using a web forum such as Stack Overflow.

    gawk is a pattern scanning and processing language.
    By default it reads standard input and writes standard output.

    Examples:
        awk '; END ' file
        awk -F: '' /etc/passwd

### [Usage in ebuilds]

[CODE] **Example for using awk in an ebuild (dev-java/protobuf-java)**

    src_prepare() ' \
            java/core/generate-test-sources-build.xml || die
    }

## [Removal]

Removal is not recomended since [awk] is a member of [\@system](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)").

### [Unmerge]

Uninstall package:

`root `[`#`]`emerge --ask --depclean --verbose app-alternatives/awk`

## [See also]

-   [ed](https://wiki.gentoo.org/wiki/Ed "Ed") --- a [line-based](https://en.wikipedia.org/wiki/Line_editor "wikipedia:Line editor") text editor with support for regular expressions
-   [sed](https://wiki.gentoo.org/wiki/Sed "Sed") --- a program that uses regular expressions to programmatically modify streams of text
-   [grep](https://wiki.gentoo.org/wiki/Grep "Grep") --- a tool for searching text files with regular expressions
-   [Perl](https://wiki.gentoo.org/wiki/Perl "Perl") --- a general purpose interpreted programming language with a powerful regular expression engine.
-   [Raku](https://wiki.gentoo.org/wiki/Raku "Raku") --- a high-level, general-purpose, and gradually typed programming language with low boilerplate objects, optionally immutable data structures, and an advanced macro system.

## [External resources]

-   [\"AWK\" Wikibook](https://en.wikibooks.org/wiki/AWK)
-   [\"An Awk Primer\" Wikibook](https://en.wikibooks.org/wiki/An_Awk_Primer)
-   [\"Handy One-Line Scripts For awk\", by Eric Pement](https://www.pement.org/awk/awk1line.txt)
-   [The awk(1p) man page](https://man7.org/linux/man-pages/man1/awk.1p.html) - awk as defined by [POSIX](https://wiki.gentoo.org/wiki/POSIX "POSIX")