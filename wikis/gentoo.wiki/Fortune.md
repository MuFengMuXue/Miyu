[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Fortune&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][GitHub](https://github.com/shlomif/fortune-mod)

[[]][Package information](https://packages.gentoo.org/packages/games-misc/fortune-mod)

**fortune** is a command-line utility which displays a random quotation from a collection of quotes.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
    -   [[2.2] [Configuration]](#Configuration)
    -   [[2.3] [Cowsay]](#Cowsay)

## [Installation]

### [USE flags]

### [USE flags for] [games-misc/fortune-mod](https://packages.gentoo.org/packages/games-misc/fortune-mod) [[]] [The notorious fortune program]

  --------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`offensive`](https://packages.gentoo.org/useflags/offensive)   Enable potentially offensive items in packages
  [`pcre`](https://packages.gentoo.org/useflags/pcre)             Add support for Perl Compatible Regular Expressions
  [`test`](https://packages.gentoo.org/useflags/test)             Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  --------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-09-02 17:00] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask games-misc/fortune-mod`

## [Usage]

### [Invocation]

`user `[`$`]`fortune -h`

    fortune-mod version 3.18.0
    fortune [-afilsw] [-m pattern] [-n number] [ [#%] file/directory/all

### [Configuration]

The fortune quote database is stored in separate files for different categories of quotes in the /usr/share/fortune directory. To add fortunes to the database, edit any of the text files in the directory, with a % before and after the quote, as an example,

[FILE] **`/usr/share/fortune/fortunes`**

    %
    Larry the Cow beckons you to explore the Gentoo Wiki!
    %

### [Cowsay]

Fortune supports the cowsay package.

First, emerge cowsay:

`root `[`#`]`emerge --ask games-misc/cowsay`

Then, use the following command to have cowsay write a fortune.

`user `[`$`]`fortune | cowsay`

     _________________________________________
    / Bounders get bound when they are caught \
    | bounding.                               |
    |                                         |
    \ -- Ralph Lewin                          /
     -----------------------------------------
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||