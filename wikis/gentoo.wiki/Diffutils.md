[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Diffutils&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.gnu.org/software/diffutils/)

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/diffutils)

**Diffutils** is a package that contains several utilities for identifying the differences in two different files.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [cmp]](#cmp)
        -   [[2.1.1] [Comparing two files]](#Comparing_two_files)
    -   [[2.2] [diff]](#diff)
        -   [[2.2.1] [Basic comparisons]](#Basic_comparisons)
        -   [[2.2.2] [Columns]](#Columns)
    -   [[2.3] [diff3]](#diff3)
        -   [[2.3.1] [Comparing three different files]](#Comparing_three_different_files)
    -   [[2.4] [sdiff]](#sdiff)
        -   [[2.4.1] [Displaying the difference]](#Displaying_the_difference)
        -   [[2.4.2] [Merging the differences]](#Merging_the_differences)

## [Installation]

### [USE flags]

### [USE flags for] [sys-apps/diffutils](https://packages.gentoo.org/packages/sys-apps/diffutils) [[]] [Tools to make diffs and compare files]

  ----------------------------------------------------------------- --------------------------------------------------------------------
  [`nls`](https://packages.gentoo.org/useflags/nls)                 Add Native Language Support (using gettext - GNU locale utilities)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- --------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-01-06 10:53] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask sys-apps/diffutils`

## [Usage]

The two files used in the examples are:

[FILE] **`one`**

    Hello, World!
    Second Line
    Gentoo Linux
    Another Line

[FILE] **`two`**

    Goodbye, World!
    Second Line
    Gentoo Linux
    Different Line

### [cmp]

[cmp] is used to compare two files byte by byte and reports the first byte difference.

#### [Comparing two files]

Finding where the first byte difference is similar to using [diff]:

`user `[`$`]`cmp one two`

    one two differ: byte 1, line 1

To print the bytes that differ, use `-b`:

`user `[`$`]`cmp one two`

    one two differ: byte 1, line 1 is 110 H 107 G

### [diff]

diff compares two files line by line

#### [Basic comparisons]

The most basic way to check the differences in two files is by using [diff].

`user `[`$`]`diff one two`

    1c1
    < Hello, World!
    ---
    > Goodbye, World!
    4c4
    < Another Line
    ---
    > Different Line

What this says is the file on the left (one) has \"Hello, World!\" while the file on the right (two) has \"Goodbye, World\".

#### [Columns]

To show the differences in column format to compare side-by-side, use the `-y` argument.

`user `[`$`]`diff -y one two`

    Hello, World!   | Goodbye, World!
    Second Line   Second Line
    Gentoo Linux      Gentoo Linux
    Another Line    | Different Line

### [diff3]

[diff3] compares three different files line-by-line. This will use the file output from the sdiff section in its examples.

#### [Comparing three different files]

Comparing files with this is similar to using [diff]:

`user `[`$`]`diff3 one two output`

    ====2
    1:1c
    3:1c
      Hello, World!
    2:1c
      Goodbye, World!
    ====1
    1:4c
      Another Line
    2:4c
    3:4c
      Different Line

### [sdiff]

[sdiff] is similar to using diff\'s `-y` argument to display columns

#### [Displaying the difference]

`user `[`$`]`sdiff one two`

    Hello, World! | Goodbye, World!
    Second Line   Second Line
    Gentoo Linux      Gentoo Linux
    Another Line    | Different Line

#### [Merging the differences]

To go line-by-line and pick the differences to include in an output file, use the `-o` argument:

`user `[`$`]`sdiff one two -o output`

    Hello, World! | Goodbye, World!
    %?
    ed: Edit then use both versions, each decorated with a header.
    eb: Edit then use both versions.
    el or e1:   Edit then use the left version.
    er or e2:   Edit then use the right version.
    e:  Discard both versions then edit a new one.
    l or 1: Use the left version.
    r or 2: Use the right version.
    s:  Silently include common lines.
    v:  Verbosely include common lines.
    q:  Quit.
    %l
    Second Line   Second Line
    Gentoo Linux      Gentoo Linux
    Another Line    | Different Line
    %r

This should now be in the output file:

[FILE] **`output`**

    Hello, World!
    Second Line
    Gentoo Linux
    Different Line