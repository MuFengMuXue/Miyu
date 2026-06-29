[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Elsw&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[[]][Package information](https://packages.gentoo.org/packages/app-portage/elsw)

[[]][GitLab](https://gitlab.com/xgqt/python-elsw/)

**elsw** is a command line tool that provides a nice way to view the [World file (Portage)](https://wiki.gentoo.org/wiki/World_file_(Portage) "World file (Portage)").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
-   [[3] [See also]](#See_also)

## [Installation]

### [Emerge]

`root `[`#`]`emerge --ask app-portage/elsw`

## [Usage]

[elsw] can be run with no arguments to display the world file:

`user `[`$`]`elsw`

### [Invocation]

`user `[`$`]`elsw --help`

    usage: elsw [-h] [-V] [-a] [-i] [-w] [-s] [-e EXCLUDE]

    elsw - View the Portage world file

    options:
      -h, --help            show this help message and exit
      -V, --version         show program's version number and exit
      -a, --all             List all available packages
      -i, --installed       List @installed packages
      -w, --world           List @world set(s) packages
      -s, --sets            List non-@world packages
      -e, --exclude EXCLUDE
                            Exclude package categories from being listed (pass in
                            a delimited list string)

## [See also]

-   [World file (Portage)](https://wiki.gentoo.org/wiki/World_file_(Portage) "World file (Portage)") --- contains the user-selected \"world\" packages that are listed in the [/var/lib/portage/world] file.
-   [World set (Portage)](https://wiki.gentoo.org/wiki/World_set_(Portage) "World set (Portage)") --- the combination of the [*system set*](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)"), the [*selected set*](https://wiki.gentoo.org/wiki/Selected_set_(Portage) "Selected set (Portage)"), and the *\@profile set*.