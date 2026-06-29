[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Bat&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][GitHub](https://github.com/sharkdp/bat)

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/bat)

**bat** is a cat(1) clone with syntax highlighting and [Git](https://wiki.gentoo.org/wiki/Git "Git") integration.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Printing a file]](#Printing_a_file)
    -   [[2.2] [Listing languages]](#Listing_languages)
    -   [[2.3] [Selecting a language]](#Selecting_a_language)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Default config]](#Default_config)
    -   [[3.2] [Use terminal colors]](#Use_terminal_colors)
    -   [[3.3] [Make bat work more like cat]](#Make_bat_work_more_like_cat)

## [Installation]

### [USE flags]

### [USE flags for] [sys-apps/bat](https://packages.gentoo.org/packages/sys-apps/bat) [[]] [cat(1) clone with syntax highlighting and Git integration]

  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`debug`](https://packages.gentoo.org/useflags/debug)   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-19 07:17] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask sys-apps/bat`

## [Usage]

### [Printing a file]

To print the contents of a file, run [bat]:

`user `[`$`]`bat file.txt`

### [Listing languages]

To list available languages, use `-L` or `--list-languages`:

`user `[`$`]`bat --list-languages`

### [Selecting a language]

To select a language type of the file, use the `-l` or `--language` arguments:

`user `[`$`]`bat --language py script`

## [Configuration]

#### [Default config]

To generate the default config one can run

`user `[`$`]`bat --generate-config-file`

\

#### [Use terminal colors]

To make bat use terminal colors instead of it\'s built-in colorscheme one can use

`user `[`$`]`bat --theme ansi`

or

Set the theme in the config file

[FILE] **`~/.config/bat/config`bat config**

    --theme="ansi"

\

#### [Make bat work more like cat]

Set the pager to never and the style to plain in the config file

[FILE] **`~/.config/bat/config`bat config**

    --pager=never
    --style=plain