[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Typst&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://typst.app/)

[[]][GitHub](https://github.com/typst/typst)

**Typst** is a new markup-based typesetting system that is designed to be as powerful as LaTeX while being much easier to learn and use.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Compiling a document]](#Compiling_a_document)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Error compiling]](#Error_compiling)

## [Installation]

### [Emerge]

[[[app-text/typst]](https://github.com/gentoo/guru/tree/master/app-text/typst)[]] is currently in [GURU](https://wiki.gentoo.org/wiki/GURU "GURU"):

`root `[`#`]`emerge --ask app-text/typst::guru`

## [Usage]

The example document used is:

[FILE] **`hello.typ`**

    = Hello, World!

    Hello, Gentoo!

    == Things to do

    + Write Wiki page for Typst
      - Mention usage
    + Bump ebuild for category/foo

    == Definition of a derivative

    $lim_(h arrow.r 0) (f(x + h) - f(x)) / h$

### [Compiling a document]

To build a document, use [typst compile]:

`user `[`$`]`typst compile hello.typ`

If the document was successfully compiled, nothing should be output.

## [Troubleshooting]

### [Error compiling]

If Typst encounters an issue in the document given, it will provide an error message detailing where the issue is:

`user `[`$`]`typst compile hello.typ`

    error: unclosed delimiter
       ┌─ hello.typ:13:0
       │
    13 │ $lim_(h arrow.r 0) (f(x + h) - f(x) / h)
       │ ^