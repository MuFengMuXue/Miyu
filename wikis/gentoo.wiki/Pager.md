[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Pager&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Terminal_pager "wikipedia:Terminal pager")

A pager is a tool for displaying the contents of files or other output on the terminal, in a user friendly way, across several screens if needed.

## [Available software]

This is just a partial selection of pagers available in Gentoo.

  -------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Name                                                           Package                                                                                                                                                                                                                                                                                                                                                                           Description
  Bat                                                            [[[sys-apps/bat]](https://packages.gentoo.org/packages/sys-apps/bat)[]]                        cat(1) clone with syntax highlighting and Git integration.
  [Less](https://wiki.gentoo.org/wiki/Less "Less")               [[[sys-apps/less]](https://packages.gentoo.org/packages/sys-apps/less)[]]                     Free, open-source file pager, almost ubiquitous on Linux. Included in the [\@system set](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)").
  [More](https://wiki.gentoo.org/wiki/Util-linux "Util-linux")   [[[sys-apps/util-linux]](https://packages.gentoo.org/packages/sys-apps/util-linux)[]]   Basic pager, part or [util-linux](https://wiki.gentoo.org/wiki/Util-linux "Util-linux") included in the [\@system set](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)").
  Most                                                           [[[sys-apps/most]](https://packages.gentoo.org/packages/sys-apps/most)[]]                     Paging program that displays, one windowful at a time, the contents of a file.
  Nvimpager                                                      [[[app-editors/neovim]](https://packages.gentoo.org/packages/app-editors/neovim)[]]      Use nvim as a pager to view manpages, diffs, etc with nvim\'s syntax highlighting.
  -------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Also consider emerging [[[app-editors/vim]](https://packages.gentoo.org/packages/app-editors/vim)[]] with `USE=vim-pager`.

## [Default pager]

The default pager can be configured by setting the `PAGER` [environment variable](https://wiki.gentoo.org/wiki/Handbook:Parts/Working/EnvVar "Handbook:Parts/Working/EnvVar"), and similarly, the default [manpager](https://wiki.gentoo.org/wiki/Man_page#Pager "Man page") can be configured by setting the `MANPAGER` environment variable:

[FILE] **`~/.bashrc`Set PAGER and MANPAGER variable**

    PAGER="less"
    MANPAGER="less"

The default pager can be modified using the [eselect](https://wiki.gentoo.org/wiki/Eselect#Pager "Eselect") command.

## [See also]

-   [Hex editor](https://wiki.gentoo.org/wiki/Hex_editor "Hex editor") --- an application to allow viewing and editing of [binary files](https://en.wikipedia.org/wiki/Binary_file "wikipedia:Binary file"), as opposed to [text files](https://wiki.gentoo.org/wiki/Text_editor "Text editor").
-   [Terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator") --- emulates a video terminal within another display architecture (e.g. in [X](https://wiki.gentoo.org/wiki/X_server "X server")).
-   [Text editor](https://wiki.gentoo.org/wiki/Text_editor "Text editor") --- a program to create and edit text files.