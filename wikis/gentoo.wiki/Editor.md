This page contains [[changes](https://wiki.gentoo.org/index.php?title=Text_editor&oldid=1411866&diff=1417836)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Text_editor/de "Text editor/de (11% translated)")
-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Text_editor/hu "Szövegszerkesztő (82% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Text_editor/ja "テキストエディタ (100% translated)")

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Text_editor "wikipedia:Text editor")

A **text editor** is a program to create and edit text files. Although it is not impossible to edit files without using one, text editors make it easy, and are handy for editing configuration files.

The Gentoo [\@system](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)") set contains the [[[virtual/editor]](https://packages.gentoo.org/packages/virtual/editor)[]] package to make sure at least one editor is installed.

## Contents

-   [[1] [Default, fallback, and virtual packages]](#Default.2C_fallback.2C_and_virtual_packages)
-   [[2] [Available software]](#Available_software)
    -   [[2.1] [CLI editors]](#CLI_editors)
    -   [[2.2] [GUI editors]](#GUI_editors)
    -   [[2.3] [Visudo editor]](#Visudo_editor)
-   [[3] [Setting system default]](#Setting_system_default)
    -   [[3.1] [Setup with eselect]](#Setup_with_eselect)
    -   [[3.2] [Manual setup]](#Manual_setup)
-   [[4] [Caveats]](#Caveats)
    -   [[4.1] [Binary files]](#Binary_files)
-   [[5] [See also]](#See_also)
-   [[6] [References]](#References)

## [][Default, fallback, and virtual packages]

As with most things Gentoo, text editor choice is up to the user. As a text editor will be necessary during and just after installation, the [virtual package](https://wiki.gentoo.org/wiki/Virtual_packages "Virtual packages"), [[[virtual/editor]](https://packages.gentoo.org/packages/virtual/editor)[]] (part of the [system set](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)")), will pull in [[[app-editors/nano]](https://packages.gentoo.org/packages/app-editors/nano)[]]^[\[1\]](#cite_note-1)^ (as the first \"any of many\" dependency of the ebuild) as a *fallback* - until another [\"virtual/editor\" package](https://packages.gentoo.org/packages/virtual/editor/dependencies) is emerged.

Thus, after a [stage 3](https://wiki.gentoo.org/wiki/Stage_file#Stage_3 "Stage file") installation, the [nano] command will be available once [chrooted](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Entering_the_new_environment "Handbook:AMD64/Installation/Base") to a newly installed Gentoo. As the stage 3 files only contain packages that are strictly necessary for every system, Nano will be the only text editor available in the stage 3 chroot. A replacement editor may be emerged on the new system, as soon as the [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository") is [installed and optionally updated](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Optional:_Updating_the_Gentoo_ebuild_repository "Handbook:AMD64/Installation/Base").

The *default* editors for the CLI will be used by many programs to determine which text editor to start up, when needed. Programs such as CLI file managers will use this default, or when invoking an editor from bash using [Ctrl]+[x] [Ctrl]+[e]. The default editors are set using the `VISUAL` and `EDITOR` [environment variables](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/EnvVar "Handbook:AMD64/Working/EnvVar"). Generally, `VISUAL` will take precedence over `EDITOR`, which is used for less capable terminals.

See the [setting system default](https://wiki.gentoo.org/wiki/Text_editor#Setting_system_default "Text editor") section.

** Tip**\
The Minimal Installation CD, [available for download](https://www.gentoo.org/downloads/) from the Gentoo website, includes the [Nano](https://wiki.gentoo.org/wiki/Nano "Nano"), [Emacs](https://wiki.gentoo.org/wiki/Emacs "Emacs"), and [vi](https://wiki.gentoo.org/wiki/Vi "Vi") editors. After [chrooting](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Entering_the_new_environment "Handbook:AMD64/Installation/Base") to a new environment for installation, the same editors will not all be available, though any editor of choice may now be installed.

** Note**\
When the first editor that is a [dependency of the virtual/editor](https://packages.gentoo.org/packages/virtual/editor/dependencies) package is emerged, this will satisfy the \"any of many\" dependency, so Nano will no longer be required. [emerge \--select app-editors/nano] to add Nano to the [world set](https://wiki.gentoo.org/wiki/World_set_(Portage) "World set (Portage)"), to prevent [emerge \--ask \--depclean] from uninstalling Nano.

## [Available software]

Text editor options can be found online in the [app-editors](https://packages.gentoo.org/categories/app-editors) category or by running:

`user `[`$`]`eix "app-editors/*"`

### [CLI editors]

  ----------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------- ---------- ----------------------------------------------------------------------------------------------------------
  Name                                                        Package                                                                                                                                                                                                                                                                                                                                                                           Skill level   Features   Description
  [Emacs](https://wiki.gentoo.org/wiki/Emacs "Emacs")         [[[app-editors/emacs]](https://packages.gentoo.org/packages/app-editors/emacs)[]]         Advanced      Huge       Class of powerful, extensible, self-documenting text editors.
  [Helix](https://wiki.gentoo.org/wiki/Helix "Helix")         [[[app-editors/helix]](https://packages.gentoo.org/packages/app-editors/helix)[]]         Medium        Advanced   Modal text editor with built-in LSP support, tree-sitter syntax highlighting, and minimal configuration.
  [Kakoune](https://wiki.gentoo.org/wiki/Kakoune "Kakoune")   [[[app-editors/kakoune]](https://packages.gentoo.org/packages/app-editors/kakoune)[]]   Medium        Advanced   Modern, actively developed editor for the command line, inspired by vi.
  Micro                                                       [[[app-editors/micro]](https://packages.gentoo.org/packages/app-editors/micro)[]]         Easy          Advanced   Modern and intuitive terminal-based text editor. Still in testing branch as of 2022-11.
  [Nano](https://wiki.gentoo.org/wiki/Nano "Nano")            [[[app-editors/nano]](https://packages.gentoo.org/packages/app-editors/nano)[]]            Easy          Advanced   Easy to use text editor.
  [Neovim](https://wiki.gentoo.org/wiki/Neovim "Neovim")      [[[app-editors/neovim]](https://packages.gentoo.org/packages/app-editors/neovim)[]]      Advanced      Huge       Vim fork focused on extensibility and agility.
  [Vim](https://wiki.gentoo.org/wiki/Vim "Vim")               [[[app-editors/vim]](https://packages.gentoo.org/packages/app-editors/vim)[]]               Advanced      Huge       Text editor based on the vi text editor.
  ----------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------- ---------- ----------------------------------------------------------------------------------------------------------

See the [vi](https://wiki.gentoo.org/wiki/Vi "Vi") article for more vi(like) editors.

### [GUI editors]

  ------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------
  Name                                                                                                    Package                                                                                                                                                                                                                                                                                                                                                                                          Description
  [Emacs](https://wiki.gentoo.org/wiki/Emacs "Emacs")                                                     [[[app-editors/emacs]](https://packages.gentoo.org/packages/app-editors/emacs)[]]                        Class of powerful, extensible, self-documenting text editors.
  [FeatherPad](https://en.wikipedia.org/wiki/Featherpad "wikipedia:Featherpad")                   [[[app-editors/featherpad]](https://packages.gentoo.org/packages/app-editors/featherpad)[]]         Lightweight Qt5 Plain-Text Editor for Linux.
  [Gedit](https://wiki.gentoo.org/wiki/Gedit "Gedit")                                                     [[[app-editors/gedit]](https://packages.gentoo.org/packages/app-editors/gedit)[]]                        Text editor for the GNOME desktop.
  [GVim](https://wiki.gentoo.org/wiki/Vim#Gvim "Vim")                                                     [[[app-editors/gvim]](https://packages.gentoo.org/packages/app-editors/gvim)[]]                           GUI-based version of the vi text editor.
  [Leafpad](https://wiki.gentoo.org/wiki/Leafpad "Leafpad")                                               [[[app-editors/leafpad]](https://packages.gentoo.org/packages/app-editors/leafpad)[]]                  Simple GTK2 text editor
  [jEdit](https://en.wikipedia.org/wiki/Jedit "wikipedia:Jedit")                                  [[[app-editors/jedit]](https://packages.gentoo.org/packages/app-editors/jedit)[]]                        jEdit is a programmer\'s text editor written in Java.
  [Kate](https://en.wikipedia.org/wiki/Kate_(text_editor) "wikipedia:Kate (text editor)")         [[[kde-apps/kate]](https://packages.gentoo.org/packages/kde-apps/kate)[]]                                    KDE text editor. Development oriented.
  [Mousepad](https://en.wikipedia.org/wiki/Mousepad_(software) "wikipedia:Mousepad (software)")   [[[app-editors/mousepad]](https://packages.gentoo.org/packages/app-editors/mousepad)[]]               Bare-bones text editor for Xfce that starts up extremely quickly.
  [NEdit](https://en.wikipedia.org/wiki/NEdit "wikipedia:NEdit")                                  [[[app-editors/nedit]](https://packages.gentoo.org/packages/app-editors/nedit)[]]                        Motif-based editor for X11.
  [Pluma](https://en.wikipedia.org/wiki/Pluma_(text_editor) "wikipedia:Pluma (text editor)")      [[[app-editors/pluma]](https://packages.gentoo.org/packages/app-editors/pluma)[]]                        A fork of Gedit 2 by MATE. Small and lightweight UTF-8 text editor for the MATE environment.
  [SciTE](https://en.wikipedia.org/wiki/Scite "wikipedia:Scite")                                  [[[app-editors/scite]](https://packages.gentoo.org/packages/app-editors/scite)[]]                        Very powerful editor for programmers. Oriented towards source editing.
  [Sublime Text](https://en.wikipedia.org/wiki/Sublime_Text "wikipedia:Sublime Text")             [[[app-editors/sublime-text]](https://packages.gentoo.org/packages/app-editors/sublime-text)[]]   Editor for code, markup and prose.
  [VSCode](https://wiki.gentoo.org/wiki/Vscode "Vscode")                                                  [[[app-editors/vscode]](https://packages.gentoo.org/packages/app-editors/vscode)[]]                     Highly extensible, electron-based text editor from Microsoft.
  [VSCodium](https://wiki.gentoo.org/wiki/Vscode "Vscode")                                                [[[app-editors/vscodium]](https://packages.gentoo.org/packages/app-editors/vscodium)[]]               Free/Libre Open Source Software Binaries of Microsoft\'s VSCode.
  [Zed](https://en.wikipedia.org/wiki/Zed_(text_editor) "wikipedia:Zed (text editor)")            [[[app-editors/zed]](https://packages.gentoo.org/packages/app-editors/zed)[]]                              Fast text editor with collaboration features written in Rust.
  ------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------

### [Visudo editor]

Due to the sensitive nature of [/etc/sudoers] it may only edited via the [visudo] command which in turn is limited to a predefined selection of editors. Type [man visudo] for more information.

## [[] Setting system default]

The `EDITOR` [environment variable](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/EnvVar "Handbook:AMD64/Working/EnvVar") defines the default text editor for the CLI interface. Gentoo provides methods for setting environment variables globally in [/etc/env.d/]. Users may override these defaults for a running shell, or in their shell configuration files.

The old method of setting the `EDITOR` variable in [/etc/rc.conf] is no longer supported. See [this](https://wiki.gentoo.org/wiki/OpenRC/Baselayout_1_to_2_migration#EDITOR_and_PAGER "OpenRC/Baselayout 1 to 2 migration") article for details.

** Note**\
[sudo](https://wiki.gentoo.org/wiki/Sudo "Sudo") does not preserve the user\'s environment variables, so when using [sudo], expect that the default editor may not be the same as the currently running user\'s.

### [Setup with eselect]

The default editor can be set with the [eselect] utility, which will automatically modify [/etc/env.d/99editor] to set the `EDITOR` environment variable.

To list editors that are installed and available to be set with [eselect]:

`root `[`#`]`eselect editor list`

    Available targets for the EDITOR variable:
      [1]   /bin/nano
      [2]   /bin/ed
      [3]   /usr/bin/emacs
      [4]   /usr/bin/ex
      [5]   /usr/bin/vi
      [ ]   (free form)

If using Vim or Neovim, select vi, then see the [this article](https://wiki.gentoo.org/wiki/Vi#.2Fusr.2Fbin.2Fvi_symlink "Vi").

To set a new editor, replace `<NUMBER>` in the following command with a number corresponding to the text editor of choice:

`root `[`#`]`eselect editor set <NUMBER>`

Next, the current environment must be updated by running the following command (for bash compatible shells):

`root `[`#`]`. /etc/profile`

The `EDITOR` environment variable should now be set to the new value for the current shell.

** Tip**\
The `VISUAL` variable may also be set with [eselect visual], for users who wish to set that environment variable.

### [Manual setup]

A system wide default text editor can be defined in the [/etc/env.d/99editor] file (this file is not present on a new installation, but can be created), for example:

[FILE] **`/etc/env.d/99editor`System wide text editor default**

    EDITOR="/usr/bin/vim"

After editing this file, run [env-update] to update the environment files:

`root `[`#`]`env-update`

Finally, update the current environment (for bash compatible shells):

`root `[`#`]`. /etc/profile`

## [Caveats]

### [Binary files]

Many text editors won\'t be able to handle [binary files](https://en.wikipedia.org/wiki/Binary_file "wikipedia:Binary file"). Use a [hex editor](https://wiki.gentoo.org/wiki/Hex_editor "Hex editor") for such files.

If binary data gets improperly output to the terminal, it can sometimes \"garble\" the display, see [this section](https://wiki.gentoo.org/wiki/Terminal_emulator#Garbled_display "Terminal emulator") of the [terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator") article for help.

## [See also]

-   [Knowledge Base:Edit a configuration file](https://wiki.gentoo.org/wiki/Knowledge_Base:Edit_a_configuration_file "Knowledge Base:Edit a configuration file")
-   [Hex editor](https://wiki.gentoo.org/wiki/Hex_editor "Hex editor") --- an application to allow viewing and editing of [binary files](https://en.wikipedia.org/wiki/Binary_file "wikipedia:Binary file"), as opposed to [text files].
-   [Pager](https://wiki.gentoo.org/wiki/Pager "Pager") --- a tool for displaying the contents of files or other output on the terminal, in a user friendly way, across several screens if needed.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://flameeyes.blog/2009/10/07/more-explanations-why-nano-is-gentoo-s-default-editor/](https://flameeyes.blog/2009/10/07/more-explanations-why-nano-is-gentoo-s-default-editor/)]]