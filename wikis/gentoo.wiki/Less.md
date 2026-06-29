**Resources**

[[]][Home](https://www.greenwoodsoftware.com/less/)

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/less)

**[less]** is a [pager](https://wiki.gentoo.org/wiki/Pager "Pager") for displaying text files.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Usage]](#Usage)
-   [[4] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [sys-apps/less](https://packages.gentoo.org/packages/sys-apps/less) [[]] [Excellent text file viewer]

  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`pcre`](https://packages.gentoo.org/useflags/pcre)               Add support for Perl Compatible Regular Expressions
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-16 16:04] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

**less** is part of [the \@system set](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)"), so is installed by default.

`root `[`#`]`emerge --ask sys-apps/less`

## [Configuration]

**less** is configured via various environment variables and files. For detailed information, refer to the [[[less(1)]](https://man.archlinux.org/man/less.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page.

  --------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Variable                    Description
  `LESS`           Command-line options to pass to every invocation of **less**.
  `LESSHISTFILE`   Path to the file in which store a history of commands issued while using **less**. By default, this file will be one of [\$XDG_STATE_HOME/lesshst], [\$HOME/.local/state/lesshst], [\$XDG_DATA_HOME/lesshst] or [\$HOME/.lesshst].
  `LESSKEYIN`      Path to a file containing custom keybinding definitions, as described in the [[[lesskey(1)]](https://man.archlinux.org/man/lesskey.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page.
  --------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [Usage]

`user `[`$`]`less file.txt`

To view line `n` of the input, provide an argument of `+``n`:

`user `[`$`]`less +40 file.txt`

There are many bindings available for movement within **less**; refer to the [[[less(1)]](https://man.archlinux.org/man/less.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page for details. Some basic keybindings:

-   To move line-by-line, use the vi keys ([j] to move down, [k] to move up) or the arrow keys.

<!-- -->

-   To move down a page, use [Space].

<!-- -->

-   To jump to the beginning, use [g]; to jump to the end, use [G].

To search for text within **less**, type `/``text`, followed by [Enter]. For example, to search for the text \"less\", type `/less` [Enter]; if the text is found after the current position of the cursor, it will be highlighted. To search for the next match, type [n]. To clear highlighting of matches, type [ESC][u]. Note that search is case-sensitive by default; this can be changed by passing the `-I` / `--IGNORE-CASE` option to the **less** command.

To access a summary of **less** commands, type [h].

To exit **less**, type [q].

By default, input to **less** is piped through [[[lesspipe(1)]](https://man.archlinux.org/man/lesspipe.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] before being displayed. **lesspipe** performs various types of preprocessing, based on the input contents (e.g. if the input is HTML), in order to display them appropriately. To disable this, pass the `-L` / `--no-lessopen` option to the **less** command. Alternatively, a different preprocessor can be specified via the `LESSOPEN` environment variable.

## [See also]

-   The [[[less(1)]](https://man.archlinux.org/man/less.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page