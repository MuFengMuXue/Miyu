[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Buku&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[[]][Home](https://github.com/jarun/buku)

[[]][Package information](https://packages.gentoo.org/packages/www-misc/buku)

buku is a command-line manager for your bookmark, which can be seen as a *personal textual mini-web* according to the author. It allows to look for tags or keywords easily and can help you manage large amount of bookmarks. Data is stored on a local database but can easily be exported to the text format.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Files]](#Files)
-   [[2] [Usage]](#Usage)
-   [[3] [Removal]](#Removal)
    -   [[3.1] [Unmerge]](#Unmerge)

## [Installation]

### [USE flags]

### [USE flags for] [www-misc/buku](https://packages.gentoo.org/packages/www-misc/buku) [[]] [Powerful command-line bookmark manager]

  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`test`](https://packages.gentoo.org/useflags/test)   Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-11 13:43] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask www-misc/buku`

### [Files]

-   [\~/.local/share/buku/bookmarks.bd] - Local SQLite database for the bookmarks.

## [Usage]

Add a link with tags:

`user `[`$`]`buku -a `[`http://lol.html`](http://lol.html)` tag1,tag2`

Add a link with a custom title:

`user `[`$`]`buku -a `[`http://lol.html`](http://lol.html)` --title Test`

Search for keyword:

`user `[`$`]`buku -s context`

Open a link, where 1 is the number of the result

`user `[`$`]`buku -s context`

`user `[`$`]`1`

Edit a bookmark in your editor:

`user `[`$`]`buku -w 320`

Update a title (requires to know the bookmark id) :

`user `[`$`]`buku -u 320 --title "Nouveau titre"`

Search by tag:

`user `[`$`]`buku neovim`

Export to markdown and save to git

`user `[`$`]`cd ~/.local/share/buku && buku -e bookmarks.md && git add bookmarks.md && git commit -am "Save" && git push`

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose www-misc/buku`