[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Ledger&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines") ([missing lead-in sentences](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines#Use_lead-in_sentences "Gentoo Wiki:Guidelines"), empty sections). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**Resources**

[[]][Home](https://www.ledger-cli.org/)

[[]][Official documentation](https://www.ledger-cli.org/docs.html)

[[]][Package information](https://packages.gentoo.org/packages/app-office/ledger)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Ledger_(software) "wikipedia:Ledger (software)")

[[]][GitHub](https://github.com/ledger/ledger)

[[]][Bugs (upstream)](https://github.com/ledger/ledger/issues)

[[]][Man page](http://man7.org/linux/man-pages/man1/ledger.1.html)

[[]][[#ledger](ircs://irc.libera.chat/#ledger)] ([[webchat](https://web.libera.chat/#ledger)])

**[ledger]** is a scriptable double-entry accounting system for the command-line. Unlike most other accounting software, [ledger] eschews opaque binary file formats and embraces a simple but well structured text file as its file format of choice. The file format [ledger] uses has the advantage of being trivial for both computers and humans to parse. So much so that [ledger] single-handedly spawned the [Plain Text Accounting](https://plaintextaccounting.org/) movement. This has lead to dozens of clones and support tools that all embrace [ledger]\'s file format, the most prominent of which are [[hledger](https://wiki.gentoo.org/index.php?title=Hledger&action=edit&redlink=1 "Hledger (page does not exist)")] ([Haskell](https://wiki.gentoo.org/wiki/Haskell "Haskell")) and [Beancount](https://wiki.gentoo.org/index.php?title=Beancount&action=edit&redlink=1 "Beancount (page does not exist)") ([Python](https://wiki.gentoo.org/wiki/Python "Python")).

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Environment variables]](#Environment_variables)
    -   [[1.4] [Files]](#Files)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [How do I import a CSV file into ledger?]](#How_do_I_import_a_CSV_file_into_ledger.3F)
    -   [[3.2] [How do I convert files from Quickbooks?]](#How_do_I_convert_files_from_Quickbooks.3F)
    -   [[3.3] [How do I import files from GNUCash?]](#How_do_I_import_files_from_GNUCash.3F)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [app-office/ledger](https://packages.gentoo.org/packages/app-office/ledger) [[]] [Double-entry accounting system with a command-line reporting interface]

  --------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`debug`](https://packages.gentoo.org/useflags/debug)     Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`doc`](https://packages.gentoo.org/useflags/doc)         Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`gpg`](https://packages.gentoo.org/useflags/gpg)         Enable support for encrypted journals
  [`python`](https://packages.gentoo.org/useflags/python)   Add optional support/bindings for the Python language
  --------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-01-28 04:53] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-office/ledger`

### [Environment variables]

[ledger] has an extensive list of command-line options detailed in its man page, nearly any one of which can be turned into an environment variable. When an environment variable conflicts with a command-line option, the command-line option takes precedence.

### [Files]

-   [\~/.ledgerrc] - user specific configuration file.

## [Usage]

### [Invocation]

## [Troubleshooting]

### [][How do I import a CSV file into [ledger]?]

[ledger] comes with a *convert* command that readily accepts a CSV file as input. The only issue is that it must be told how to parse and date codes it encounters as there are several standards in use internationally:

[ledger convert download.csv \--input-date-format \"%Y/%m/%d\"]

### [][How do I convert files from Quickbooks?]

This is not directly supported, but there are third party tools that will do this, such as:

-   [outofit](https://github.com/rcaputo/outofit) (Perl)
-   [qb2ledger](https://gist.github.com/genegoykhman/3765100) (Ruby)
-   [QIFtoLedger](https://github.com/Kolomona/QIFtoLedger) (Ruby)

### [][How do I import files from GNUCash?]

This isn\'t directly supported either but simple third party scripts can do this, such as:

-   [gcash2ledger.py](https://gist.github.com/nonducor/ddc97e787810d52d067206a592a35ea7)

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose app-office/ledger`

## [See also]

-   [hledger](https://wiki.gentoo.org/index.php?title=Hledger&action=edit&redlink=1 "Hledger (page does not exist)")
-   [Beancount](https://wiki.gentoo.org/index.php?title=Beancount&action=edit&redlink=1 "Beancount (page does not exist)")
-   [bc](https://wiki.gentoo.org/wiki/Bc "Bc") --- arbitrary-precision fixed-point mathematical scripting language
-   [sc-im](https://wiki.gentoo.org/wiki/Sc-im "Sc-im") --- a terminal-based spreadsheet and calculator with [[vim](https://wiki.gentoo.org/wiki/Vim "Vim")]-like key bindings

## [External resources]

-   [https://plaintextaccounting.org/](https://plaintextaccounting.org/)