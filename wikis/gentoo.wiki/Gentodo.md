[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Gentodo&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[[]][GitHub](https://github.com/csfore/gentodo)

**Gentodo** is a todo program designed for a Gentoo development workflow.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Adding an item]](#Adding_an_item)
    -   [[2.2] [Listing entries]](#Listing_entries)
    -   [[2.3] [Deleting an item]](#Deleting_an_item)
-   [[3] [Files]](#Files)
    -   [[3.1] [Storage]](#Storage)
    -   [[3.2] [Configuration]](#Configuration)
-   [[4] [Tips]](#Tips)

## [Installation]

** Warning**\
Gentodo is currently very much in a testing phase and might have breaking changes upon a stable release.

### [Emerge]

Install [[[app-misc/gentodo::guru]](https://github.com/gentoo-mirror/guru/tree/master/app-misc/gentodo)[]] from the [GURU](https://wiki.gentoo.org/wiki/GURU "GURU") repository:

`root `[`#`]`emerge --ask app-misc/gentodo`

## [Usage]

### [Adding an item]

To add an item to the todo list:

`user `[`$`]`gentodo add -t Title -d Details`

It is also possible to not have a description:

`user `[`$`]`gentodo add -t Title`

### [Listing entries]

To list entries:

`user `[`$`]`gentodo`

To get item IDs (required for deletion):

`user `[`$`]`gentodo -v`

### [Deleting an item]

First get the item ID and then:

`user `[`$`]`gentodo del 123`

## [Files]

### [Storage]

To find your `todo.json` file, go to `~/.local/share/gentodo/todo.json`, an example of which looks like:

[FILE] **`~/.local/share/gentodo/todo.json`**


    }

### [Configuration]

**Gentodo** will eventually store its config in `~/.config/gentodo/config.toml`. For now, this is an example of a config file:

[FILE] **`~/.config/gentodo/config.toml`**

    [gentodo]
    token = "insert random gibberish here"

## [Tips]

A handy use for this program is to add it to the user\'s [\~/.bashrc] so every time they open a new terminal they will be reminded of upcoming tasks that they need to look at.

\

[FILE] **`~/.bashrc`**

    # Put your fun stuff here.

    # TODO list
    echo "===== TODO List ====="
    echo ""
    gentodo --brief