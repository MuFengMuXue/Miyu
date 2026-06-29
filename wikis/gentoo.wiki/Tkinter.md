[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Tkinter&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

Tkinter (tkinter in Python 3.x) claims to be \"most portable GUI toolkit for Python\"[\[1\]](http://tkinter.unpythonic.net/wiki/) and is Python\'s \"de-facto standard GUI (Graphical User Interface) package\"[\[2\]](https://wiki.python.org/moin/TkInter). Although there are several other graphical toolkits for Python, Tkinter is the one most often used in GUI development with Python.

tkinter uses [[[dev-lang/tk]](https://packages.gentoo.org/packages/dev-lang/tk)[]] internally.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [make.conf]](#make.conf)
    -   [[1.2] [package.use]](#package.use)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
-   [[3] [See also]](#See_also)
-   [[4] [External Links]](#External_Links)

## [Installation]

### [make.conf]

Getting Tkinter can be accomplished by enabling the `tk` USE flag. This can be set for specifically for Python, or for all packages system-wide in the [make.conf] file.

[FILE] **`/etc/portage/make.conf`Add tk to the system\'s USE flags**

    USE="tk"

### [package.use]

For an approach more limited in scope, modify a [package.use] file for Python only.

[FILE] **`/etc/portage/package.use/python`Add the tk USE flag for dev-lang/python**

    dev-lang/python tk

### [Emerge]

Finally, re-emerge the [\@world set](https://wiki.gentoo.org/wiki/World_set_(Portage) "World set (Portage)") using this command:

`root `[`#`]`emerge --ask -uvDU @world`

That is it! Tkinter should now be installed.

## [Usage]

When attempting to use Tkinter in Python code, depending on the version(s) of Python are currently installed on the system, import Tkinter might need performed in different ways:

-   When using Python 2.x.: use `import Tkinter`
-   When using Python 3.x: use `import tkinter` (note the lower case **T**).

## [See also]

-   [Python](https://wiki.gentoo.org/wiki/Python "Python") --- an extremely popular cross-platform object oriented programming language.

## [External Links]

-   [The official tkinter wiki](https://wiki.python.org/moin/TkInter)
-   [Another tkinter wiki](http://tkinter.unpythonic.net/wiki/)