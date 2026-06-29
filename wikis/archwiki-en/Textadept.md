# Textadept

Textadept describes itself as "a fast, minimalist, and remarkably extensible cross-platform text editor".

With a very lightweight code base written in C, it relies on Lua for its extensibility. The editor works both in a graphical (GTK) and in a CLI environment (Curses).

## Installation
Install the  package. It features 2 executables:

* textadept
* textadept-curses

The curses version runs in a CLI environment.

## Configuration
On first start, Textadept will create a  folder. You can edit  to start customizing the editor. From there you can define new functions, key bindings, themes, and even modules, as explained in the manual and the API.

Textadept sample configuration

## Modules
By default, Textadept features modules for its core only, that is ANSI C, Lua and itself, however the AUR package also embeds some of the official modules.

More contributed modules and functions are listed in the wiki.

A convenient way to install modules is by cloning the repository in . For instance you can fetch textadept-vi from there:

 $ cd ~/.textadept/modules
 $ git clone https://github.com/jugglerchris/textadept-vi.git

You can easily keep up to date all your modules with version control tools.
