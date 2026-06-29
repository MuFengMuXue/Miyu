**Resources**

[[]][Official documentation](https://github.com/andmarti1424/sc-im/blob/main/Readme.md)

[[]][Package information](https://packages.gentoo.org/packages/app-office/sc-im)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Sc_(spreadsheet_calculator) "wikipedia:Sc (spreadsheet calculator)")

[[]][GitHub](https://github.com/andmarti1424/sc-im)

[[]][Bugs (upstream)](https://github.com/andmarti1424/sc-im/issues)

**[sc-im]** short for **Spreadsheet Calculator Improvised** is a terminal-based spreadsheet and calculator with [[vim](https://wiki.gentoo.org/wiki/Vim "Vim")]-like key bindings. The program is fairly advanced and capable spreadsheet application with most of the features modern spreadsheet users have come to expect in GUI-based spreadsheet applications. Additionally, [sc-im] can be used non-interactively as a simple calculator tool somewhat like [bc].

Development of the original program, then called [sc], began in 1981 but stalled sometime in 2002. Around 2015 a group of [sc] enthusiasts decided to resume development under the name [sc-im]. In late 2022 the maintained package [[[app-office/sc-im]](https://packages.gentoo.org/packages/app-office/sc-im)[]] fork was migrated from [GURU](https://wiki.gentoo.org/wiki/GURU "GURU") to the main Gentoo package repository and the unmaintained `app-office/sc` was removed from the tree via [[[bug #877051]](https://bugs.gentoo.org/show_bug.cgi?id=877051)[]].

[sc-im] has a number of use-cases. It can be used non-interactively as a filter to translate incompatible spreadsheets to the text-based [.sc] format. It is also popular among [[mutt](https://wiki.gentoo.org/wiki/Mutt "Mutt")] users who wish to have a way to view spreadsheets attached to emails without exiting the terminal.

## Contents

-   [[1] [Supported File Formats]](#Supported_File_Formats)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [USE flags]](#USE_flags)
    -   [[2.2] [Emerge]](#Emerge)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Files]](#Files)
-   [[4] [Usage]](#Usage)
    -   [[4.1] [Invocation]](#Invocation)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Issues loading spreadsheets larger that 65,536 rows]](#Issues_loading_spreadsheets_larger_that_65.2C536_rows)
    -   [[5.2] [Converting between spreadsheet formats non-interactively]](#Converting_between_spreadsheet_formats_non-interactively)
    -   [[5.3] [Unmerge]](#Unmerge)
-   [[6] [See also]](#See_also)

### [Supported File Formats]

The following file formats can be imported or exported:

-   Spreadsheet Calculator [.sc] files.
-   Comma Seperated Values [.csv] files.
-   Tab Separated Values [.tsv] files.
-   Markdown Table [.md] files.
-   Plain Text [.txt] files.

The following formats are supported, but only as import filters:

-   [LibreOffice](https://wiki.gentoo.org/wiki/LibreOffice "LibreOffice") OpenDocument Spreadsheet [.ods] files.
-   Legacy Microsoft Excel [.xls] files.
-   Microsoft Office Open XML [.xlsx] files.

## [Installation]

### [USE flags]

### [USE flags for] [app-office/sc-im](https://packages.gentoo.org/packages/app-office/sc-im) [[]] [Ncurses based, vim-like spreadsheet calculator]

  ----------------------------------------------------------- ----------------------------------------------------
  [`X`](https://packages.gentoo.org/useflags/X)               Use x11-misc/xclip for clipboard copy/paste
  [`lua`](https://packages.gentoo.org/useflags/lua)           Enable Lua scripting support
  [`ods`](https://packages.gentoo.org/useflags/ods)           Add ods import support
  [`plots`](https://packages.gentoo.org/useflags/plots)       Add sci-visualization/gnuplot for plotting support
  [`tmux`](https://packages.gentoo.org/useflags/tmux)         Use app-misc/tmux for clipboard copy/paste
  [`wayland`](https://packages.gentoo.org/useflags/wayland)   Use gui-apps/wl-clipboard for clipboard copy/paste
  [`xls`](https://packages.gentoo.org/useflags/xls)           Add xls support
  [`xlsx`](https://packages.gentoo.org/useflags/xlsx)         Add xlsx support
  ----------------------------------------------------------- ----------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-09-24 01:15] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-office/sc-im`

## [Configuration]

### [Files]

-   [\$HOME/.config/sc-im/scimrc] --- Per-user configuration file.

## [Usage]

The [sc-im] spreadsheet editor is closely modeled after [vim] text editor. The program has several different modes:

-   Normal Mode: where cell navigation occurs.
-   Insert Mode: where new values are entered into cells.
-   Edit Mode: to modify existing cells.
-   Command Mode: For entering commands to modify application settings.
-   Visual Mode: For selecting ranges of cells in a visually intuitive manner.

Basic navigation is performed with keys on a QWERTY keyboard\'s home row. As a result [H] moves the cursor up one cell, [J] moves the cursor down one cell, [K] moves the cursor right one cell, and the [L] moves the cursor right one cell. That said, the [←], [↑], [→], and the [↓] cursor keys work as expected. The [PgUp] and [PgDn] key works the same way it does with the [less](https://wiki.gentoo.org/wiki/Less "Less") or [more](https://wiki.gentoo.org/index.php?title=More&action=edit&redlink=1 "More (page does not exist)") screen pagers. The following table details the major keyboard navigation and editing functions:

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Key                                                                                                                                                                                                                                                                                                                                                                                                                                                  Function
  [=]                                                                                                                                                                                                                                                                                   Insert a numeric value
  [\\]                                                                                                                                                                                                                                                                                  Insert a text value
  [E]                                                                                                                                                                                                                                                                                   Edit a numeric value
  [SHIFT]+[E]                                                                                                            Edit a string value
  [X]                                                                                                                                                                                                                                                                                   Delete current cell content
  [J]                                                                                                                                                                                                                                                                                   Move down
  [K]                                                                                                                                                                                                                                                                                   Move up
  [H]                                                                                                                                                                                                                                                                                   Move left
  [L]                                                                                                                                                                                                                                                                                   Move right
  [U]                                                                                                                                                                                                                                                                                   Undo last change
  [CTRL]+[R]                                                                                                             Redo last change undone
  [Y],[Y]                                                                                                                Copy current cell
  [V]                                                                                                                                                                                                                                                                                   Select a range using the [H], [J], [K], and [L] home keys keys
  [P]                                                                                                                                                                                                                                                                                   Paste a previously yanked cell or range
  [I],[R]                                                                                                                Insert row
  [I],[C]                                                                                                                Insert column
  [D],[R]                                                                                                                Delete row
  [D],[C]                                                                                                                Delete column
  [G],[O],[\<col\>,\<row\>]   Go to exact *off screen* cell.
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Like vim, sc-im has a built-in command mode. The [: help] command is perhaps the most useful for new users as it provides an extensive overview of internal sc-im commands. The most commonly used commands are:

  -------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------
  Command                                                                                                        Function
  [:q]                Quit the app
  [:h]                See help
  [:w \<filename\>]   Save current spreadsheet in [.sc] file format
  -------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------

### [Invocation]

`user `[`$`]`sc-im --help`

    SC-IM - SC Improved

    Usage: sc-im [arguments] [file]          specified file
       or: sc-im [arguments] -               read text from stdin

    Arguments:

      --autocalc                  Set variable 'autocalc'.
      --copy_to_clipboard_delimited_tab  Set variable 'copy_to_clipboard_delimited_tab'
      --debug                     Set variable 'debug'
      --default_copy_to_clipboard_cmd=COMMAND  set variable 'default_copy_from_clipboard_cmd'
      --default_paste_from_clipboard_cmd=COMMAND  set variable 'default_paste_from_clipboard_cmd'
      --default_open_file_under_cursor_cmd=COMMAND  set variable 'default_open_file_under_cursor_cmd'
      --export_csv                Export to csv without interaction
      --export_tab                Export to tab without interaction
      --export_txt                Export to txt without interaction
      --export_mkd                Export to markdown without interaction
      --external_functions        Set variable 'external_functions'
      --half_page_scroll          Set variable 'half_page_scroll'
      --ignorecase                Set variable 'ignorecase'
      --import_delimited_as_text Import text as
      --newline_action=   Set variable 'newline_action'
      --nocurses                  Run interactive but without ncurses interface.
      --numeric                   Set variable 'numeric'
      --numeric_decimal           Set variable 'numeric_decimal'
      --output=FILE               Save the results in FILE
      --overlap                   Set variable 'overlap variable'
      --quit_afterload            Quit after loading all the files
      --show_cursor               Make the screen cursor follow the active cell
      --tm_gmtoff=       set gmt offset used for converting datetimes to localtime.
      --txtdelim=  Sets delimiter when opening a .tab of .csv file

      --version                   Print version information and exit
      --help                      Print Help (this message) and exit

## [Troubleshooting]

### [][Issues loading spreadsheets larger that 65,536 rows]

By default [sc-im] limits its spreadsheets to 65,536 rows. This was a sane limit when the software was first released but as time passed spreadsheets began to be treated as \"poor man\'s databases\" and have grown ever larger. Eventually a compile-time option was added to raise this figure to a new maximum of 1,048,576 rows. Starting with `sc-im-0.8.3-r1` the compile time option of 1,048,576 rows is set. If you\'re having issues opening large spreadsheets upgrade to at least that version.

Currently, [sc-im] is limited to a maximum 702 columns.

### [Converting between spreadsheet formats non-interactively]

It\'s possible to use [sc-im] to convert between spreadsheet file formats. In fact, this is a popular use of the program. Assuming you\'re trying to convert a modern Microsoft Excel [.xlsx] file to [.csv] the command would look something like this:

`user `[`$`]`sc-im --nocurses --export_csv --quit_afterload infile.xlsx > outfile.csv`

Other options are possible, but at this time only [.csv], [.tsv], [.txt], and [.md] files have output filters.

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose app-office/sc-im`

## [See also]

-   [bc](https://wiki.gentoo.org/wiki/Bc "Bc") --- arbitrary-precision fixed-point mathematical scripting language