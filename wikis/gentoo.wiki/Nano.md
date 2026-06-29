This page contains [[changes](https://wiki.gentoo.org/index.php?title=Nano&oldid=1397523&diff=1440687)] which are not marked for translation.

Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Nano/hu "Nano (100% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Nano/ja "Nano (100% translated)")

**Resources**

[[]][Home](https://www.nano-editor.org/)

[[]][Guide](https://wiki.gentoo.org/wiki/Nano/Guide "Nano/Guide")

[[]][Wikipedia](https://en.wikipedia.org/wiki/GNU_nano "wikipedia:GNU nano")

**GNU nano** is an easy to use [terminal](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator")-based [text editor](https://wiki.gentoo.org/wiki/Text_editor "Text editor") that also provides some more advanced functionality. nano allows just anyone to jump into editing text files, but still provides useful productivity features that don\'t get in the way of wanting to just open a file and edit away.

By default, at the bottom of the screen, nano displays some useful pointers on basic functionality and how to find more help, so that first-time users can start to find their way around (this is configurable). It of course comes with classic basic features, such as copy/paste, undo/redo, syntax highlighting, interactive search-and-replace, auto-indentation, macros, etc.

nano\'s small size, portability, and ease of use, have lead to it being the editor that gets included in Gentoo\'s official [stage3](https://wiki.gentoo.org/wiki/Stage_file#Stage_3 "Stage file") installation seeds (a text editor is an absolute requirement in these stage3 files, and nano is as good as any, if not arguably better). This makes it a staple of Gentoo installations, and though of course it can be easily [replaced with another text editor](https://wiki.gentoo.org/wiki/Text_editor#Default.2C_fallback.2C_and_virtual_packages "Text editor"), a working text editor is such an essential part of the Gentoo operating system (particularly in the case of system issues) that keeping nano installed as a backup is usually for the best.

** Note**\
Technically, nano gets included by default in stage3 files because it is the first \"one of many\" dependency of the [[[virtual/editor]](https://packages.gentoo.org/packages/virtual/editor)[]] package, which is part of the [system set](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)"). It is not however in the [world set](https://wiki.gentoo.org/wiki/World_set_(Portage) "World set (Portage)"). In order to avoid surprises when performing system maintenance, it is useful to be informed about the basics of how [default, fallback, and virtual packages](https://wiki.gentoo.org/wiki/Text_editor#Default.2C_fallback.2C_and_virtual_packages "Text editor") work in Gentoo, and the implications on choosing and installing text editors (notably nano can sometimes get unintentionally [depcleaned](https://wiki.gentoo.org/wiki/Emerge#Remove_.28uninstall_.2F_depclean.29_packages "Emerge") after installing certain other text editors, if not paying attention).

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [First steps]](#First_steps)
    -   [[2.2] [Cut, copy, and paste]](#Cut.2C_copy.2C_and_paste)
    -   [[2.3] [Search]](#Search)
    -   [[2.4] [More shortcuts]](#More_shortcuts)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Syntax highlighting]](#Syntax_highlighting)
-   [[4] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [app-editors/nano](https://packages.gentoo.org/packages/app-editors/nano) [[]] [GNU GPL\'d Pico clone with more functionality]

  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------
  [`+spell`](https://packages.gentoo.org/useflags/+spell)           Add dictionary support
  [`debug`](https://packages.gentoo.org/useflags/debug)             Enable debug messages and assert warnings. Note that these will all be sent straight to stderr rather than some logging facility.
  [`justify`](https://packages.gentoo.org/useflags/justify)         Enable justify/unjustify functions for text formatting.
  [`magic`](https://packages.gentoo.org/useflags/magic)             Add magic file support (sys-apps/file) to automatically detect appropriate syntax highlighting
  [`minimal`](https://packages.gentoo.org/useflags/minimal)         Disable all fancy features, including ones that otherwise have a dedicated USE flag (such as spelling).
  [`ncurses`](https://packages.gentoo.org/useflags/ncurses)         Add ncurses support (console display library)
  [`nls`](https://packages.gentoo.org/useflags/nls)                 Add Native Language Support (using gettext - GNU locale utilities)
  [`unicode`](https://packages.gentoo.org/useflags/unicode)         Add support for Unicode
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-10 07:03] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-editors/nano`

## [Usage]

### [First steps]

Start nano by typing [nano] in a terminal followed by options or a file. Passing a file name is the most common use:

`user `[`$`]`nano filename`

Nano now shows the content of the text file and which can be modified as desired. Navigate through the text with the arrow keys.

At the bottom nano shows shortcuts for common actions, e.g. save or exit. The shortcut to save is shown as `^O`. Prefix the shortcut with the [Ctrl] key. So to save a document (after editing it) press [Ctrl]+[O]. To exit press [Ctrl]+[X].

** Warning**\
Prior to ***nano 4.0***, when editing *configuration files*, always pass [nano] the `-w` option. Without this option, long lines are wrapped by inserting newlines - this will often break configuration files.

To see an overview over all options run [nano \--help]

### [][Cut, copy, and paste]

Lines can be cut with the shortcut [Ctrl]+[K] (copied with [Alt]+[\^]) and paste with [Ctrl]+[U]. To cut or copy multiple lines press the shortcut multiple times.

### [Search]

Search the text with [Ctrl]+[W]. Continue the search with [Alt]+[W].

### [More shortcuts]

  ---------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Action                             Shortcut                                                                                                                                                                                                                                                                                                                                   Other shortcut
  Show the help                      [Ctrl]+[G]   [F1]
  Close file                         [Ctrl]+[X]   [F2]
  Save file                          [Ctrl]+[O]   [F3]
  Search text                        [Ctrl]+[W]   [F6]
  Continue search                    [Alt]+[W]    [F16]
  Copy line to clipboard             [Alt]+[\^]   [Alt]+[6]
  Cut line to clipboard              [Ctrl]+[K]   [F9]
  Paste line from clipboard          [Ctrl]+[U]   [F10]
  Go to the first line of the file   [Alt]+[\\]   [Ctrl]+[Home]
  Go to the end line of the file     [Alt]+[/]    [Ctrl]+[End]
  ---------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [Configuration]

Set options permanently in the [/etc/nanorc] configuration file. This configuration applies system wide to all users. To change options only for one user, set the option in the user\'s [\~/.nanorc] file. As a general rule, files present in a user\'s home directory override system wide settings.

### [Syntax highlighting]

Support for syntax highlight is achieved through plugins and include statements in nano\'s configuration file ([\~/.nanorc] for individual users).

`user `[`$`]`mkdir ~/.nano`

Copy the plugin into the [\~/.nano] directory, then reference it with a include statement. For example:

[FILE] **`~/.nanorc`Apply ebulid specific syntax highlighting for nano**

    # Ebuild specific highlighting
    include "~/.nano/gentoo.nanorc"

## [See also]

-   [Knowledge Base:Edit a configuration file](https://wiki.gentoo.org/wiki/Knowledge_Base:Edit_a_configuration_file "Knowledge Base:Edit a configuration file")
-   [Nano/Guide](https://wiki.gentoo.org/wiki/Nano/Guide "Nano/Guide") --- covers basic operations in [nano], and is meant to be very concise.
-   [Text editor](https://wiki.gentoo.org/wiki/Text_editor "Text editor") --- a program to create and edit text files.