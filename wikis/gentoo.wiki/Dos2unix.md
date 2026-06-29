[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Dos2unix&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](http://waterlan.home.xs4all.nl/dos2unix.html)

[dos2unix] is a tool to convert text files from DOS line endings (carriage return + line feed) to Unix line endings (line feed). It is also capable of conversion between UTF-16 to UTF-8. Invoking the [unix2dos] command can be used to convert *from* Unix *to* DOS. This tool comes in handy when sharing files between Windows and Linux machines.

## Contents

-   [[1] [Installation]](#Installation)
-   [[2] [Usage]](#Usage)
-   [[3] [External resources]](#External_resources)

## [Installation]

`root `[`#`]`emerge --ask app-text/dos2unix`

## [Usage]

To convert a file that has DOS line endings to Unix format:

`user `[`$`]`dos2unix my_file.txt`

    dos2unix: converting file my_file.txt to Unix format...

To convert a file that has Unix line endings to DOS format:

`user `[`$`]`unix2dos my_file.txt`

    unix2dos: converting file my_file.txt to DOS format...

## [External resources]

-   [man dos2unix]