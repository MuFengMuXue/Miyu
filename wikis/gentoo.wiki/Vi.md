[[]][Wikipedia](https://en.wikipedia.org/wiki/Vi "wikipedia:Vi")

[vi] is a powerful *modal* [text-based editor](https://wiki.gentoo.org/wiki/Text_editor "Text editor") with a long history in the Unix(like) operating system. The original vi has served as a basis for many clones and derivatives over the years, notably [vim](https://wiki.gentoo.org/wiki/Vim "Vim").

A new Gentoo installation includes [nano](https://wiki.gentoo.org/wiki/Nano "Nano") by default - emerge a package from the following section to provide a vi-like editor. Beware that emerging a vi editor on a new installaton may allow nano to be [depclean]ed - see the [default, fallback, and virtual packages section](https://wiki.gentoo.org/wiki/Text_editor#Default.2C_fallback.2C_and_virtual_packages "Text editor") in the text editor article.

Although not part of the [GNU Coreutils](https://wiki.gentoo.org/wiki/GNU_Coreutils "GNU Coreutils"), a vi-like editor is almost universally included in Linux distributions. vi has parentage with the [ed](https://wiki.gentoo.org/wiki/Ed "Ed") [line editor](https://en.wikipedia.org/wiki/Line_editor "wikipedia:Line editor").

** See also**\
The [Vim](https://wiki.gentoo.org/wiki/Vim "Vim") article provides general information on vi-like editors. See the [Vim guide](https://wiki.gentoo.org/wiki/Vim/Guide "Vim/Guide") for an introductory tutorial on vi-like editor usage. See the [text editor](https://wiki.gentoo.org/wiki/Text_editor "Text editor") article for general information on installing and configuring text editors in Gentoo.

## Contents

-   [[1] [Available software]](#Available_software)
-   [[2] [Launch vi(like) editor]](#Launch_vi.28like.29_editor)
-   [[3] [/usr/bin/vi symlink]](#.2Fusr.2Fbin.2Fvi_symlink)
-   [[4] [See also]](#See_also)

## [Available software]

  -------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------
  Name                                                     Package                                                                                                                                                                                                                                                                                                                                                                        Description
  levee                                                    [[[app-editors/levee]](https://packages.gentoo.org/packages/app-editors/levee)[]]      Really tiny vi clone.
  [Neovim](https://wiki.gentoo.org/wiki/Neovim "Neovim")   [[[app-editors/neovim]](https://packages.gentoo.org/packages/app-editors/neovim)[]]   Neovim is a hyperextensible Vim-based text editor.
  pyvim                                                    [[[app-editors/pyvim]](https://packages.gentoo.org/packages/app-editors/pyvim)[]]      Implementation of Vim in Python.
  [Vim](https://wiki.gentoo.org/wiki/Vim "Vim")            [[[app-editors/vim]](https://packages.gentoo.org/packages/app-editors/vim)[]]            Modern vi(like) editor, probably the most used clone. Optional GUI called Gvim.
  vis                                                      [[[app-editors/vis]](https://packages.gentoo.org/packages/app-editors/vis)[]]            A vi-like editor based on Plan 9\'s structural regular expressions.
  -------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------

More vi-like editors can be found online in the [app-editors](https://packages.gentoo.org/categories/app-editors) category or by running:

`user `[`$`]`eix "app-editors/*"`

## [][Launch vi(like) editor]

A vi-like editor can usually be launched with the [vi] command. Vim can be launched with the [vim] command. [Neovim](https://wiki.gentoo.org/wiki/Neovim "Neovim") is launched with the [nvim] command.

If a vi-like editor is not installed, [busybox\'s vi](https://wiki.gentoo.org/wiki/Busybox#vi "Busybox") may be available, try:

`user `[`$`]`busybox vi -h`

    BusyBox v1.34.1 (2021-11-23 09:49:04 CET) multi-call binary.

    Usage: vi [-c CMD] [-R] [-H] [FILE]...

    Edit FILE

            -c CMD  Initial command to run ($EXINIT also available)
            -R      Read-only
            -H      List available features

## [][/usr/bin/vi symlink]

If [Vim](https://wiki.gentoo.org/wiki/Vim "Vim") is installed, the [vi] and [vim] commands become synonymous due to the following link:

`user `[`$`]`ls -al /usr/bin/vi`

    lrwxrwxrwx 1 root root 3 Nov 25 19:59 /usr/bin/vi -> vim

Use [eselect vi] to manage this link, from the [[[app-eselect/eselect-vi]](https://packages.gentoo.org/packages/app-eselect/eselect-vi)[]] package. [eselect vi] can currently select between the following: *vim, nvim, nvi, elvis, vile, gvim, qvim, xvile, pyvim, and busybox.*

The synonymous use also holds when setting [editor defaults](https://wiki.gentoo.org/wiki/Text_editor#Setting_system_default "Text editor").

## [See also]

-   [Text editor](https://wiki.gentoo.org/wiki/Text_editor "Text editor") --- a program to create and edit text files.
-   [Vim](https://wiki.gentoo.org/wiki/Vim "Vim") --- a [vi]-like [text editor](https://wiki.gentoo.org/wiki/Text_editor "Text editor"), originally descended from the [Stevie](https://en.wikipedia.org/wiki/Stevie_(text_editor) "wikipedia:Stevie (text editor)") vi clone.
-   [Vim/Guide](https://wiki.gentoo.org/wiki/Vim/Guide "Vim/Guide") --- explain basic usage for users new to [vi-like](https://en.wikipedia.org/wiki/vi "wikipedia:vi") text editors in general, and vim in particular.