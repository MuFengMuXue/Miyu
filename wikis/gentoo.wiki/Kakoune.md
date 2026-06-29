[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Kakoune&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](http://kakoune.org/)

[[]][Package information](https://packages.gentoo.org/packages/app-editors/kakoune)

[[]][GitHub](https://github.com/mawww/kakoune)

[[]][Official documentation](https://github.com/mawww/kakoune/blob/master/README.asciidoc)

**Kakoune** is a modern, actively developed [editor](https://wiki.gentoo.org/wiki/Text_editor "Text editor") for the [command line](https://wiki.gentoo.org/wiki/Shell "Shell"), inspired by [vi](https://wiki.gentoo.org/wiki/Vi "Vi").

A modal editor, Kakoune uses keystrokes as a text editing language, for powerful and flexible text editing - doing things faster and in fewer keystrokes. Multiple selections allow for sweeping changes with very few commands, and it\'s orthogonal design assures predictable operation.

Modal editors generally have a steep learning curve, but that is rewarded with powerful and fast text manipulation skills. Kakoune helps level the leaning curve with strong focus on interactivity, showing immediate and incremental results.

## [Installation]

### [Emerge]

Kakoune is currently in the [testing branch](https://wiki.gentoo.org/wiki/Handbook:X86/Portage/Branches#Testing "Handbook:X86/Portage/Branches"), and may need to be [made available for installation.](https://wiki.gentoo.org/wiki/Knowledge_Base:Accepting_a_keyword_for_a_single_package#Using_--autounmask-write_emerge_command_option "Knowledge Base:Accepting a keyword for a single package")

On a system running the [stable branch](https://wiki.gentoo.org/wiki/Handbook:X86/Portage/Branches#Stable "Handbook:X86/Portage/Branches"), first accept the installation of [[[app-editors/kakoune]](https://packages.gentoo.org/packages/app-editors/kakoune)[]] from the testing branch:

`root `[`#`]`emerge --ask --autounmask=y --autounmask-write app-editors/kakoune`

[Validate](https://wiki.gentoo.org/wiki/Dispatch-conf "Dispatch-conf") the changes:

`root `[`#`]`dispatch-conf`

Install:

`root `[`#`]`emerge --ask app-editors/kakoune`

## [See also]

-   [Knowledge Base:Edit a configuration file](https://wiki.gentoo.org/wiki/Knowledge_Base:Edit_a_configuration_file "Knowledge Base:Edit a configuration file")
-   [Text editor](https://wiki.gentoo.org/wiki/Text_editor "Text editor") --- a program to create and edit text files.