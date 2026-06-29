This page contains [[changes](https://wiki.gentoo.org/index.php?title=Selected-packages_set_(Portage)&oldid=1246242&diff=1441232)] which are not marked for translation.

Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Selected-packages_set_(Portage)/hu "Válogatott szoftvercsomagkészletek (Portage) (100% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Selected-packages_set_(Portage)/ja "selected-packages 集合 (Portage) (100% translated)")

**[Portage - the heart of Gentoo](https://wiki.gentoo.org/wiki/Portage "Portage")**\
[emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge") --- [configuration](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf") --- [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") --- [dispatch-conf](https://wiki.gentoo.org/wiki/Dispatch-conf "Dispatch-conf")\
[\
[world file] --- [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag") --- [ebuilds](https://wiki.gentoo.org/wiki/Ebuild "Ebuild") --- [profiles](https://wiki.gentoo.org/wiki/Portage/Profiles "Portage/Profiles")\
[upgrades](https://wiki.gentoo.org/wiki/Upgrading_Gentoo "Upgrading Gentoo") --- [using testing packages](https://wiki.gentoo.org/wiki/Knowledge_Base:Accepting_a_keyword_for_a_single_package "Knowledge Base:Accepting a keyword for a single package") --- [Gentoo binhost](https://wiki.gentoo.org/wiki/Gentoo_Binary_Host_Quickstart "Gentoo Binary Host Quickstart")\
[tools](https://wiki.gentoo.org/wiki/Useful_Portage_tools "Useful Portage tools") --- [gentoolkit](https://wiki.gentoo.org/wiki/Gentoolkit "Gentoolkit") --- [eselect](https://wiki.gentoo.org/wiki/Eselect "Eselect")\
[Portage FAQ](https://wiki.gentoo.org/wiki/Project:Portage/FAQ "Project:Portage/FAQ") --- [cheat sheet](https://wiki.gentoo.org/wiki/Gentoo_Cheat_Sheet "Gentoo Cheat Sheet") --- [FAQ](https://wiki.gentoo.org/wiki/FAQ "FAQ")\
[all articles](https://wiki.gentoo.org/wiki/Category:Portage "Category:Portage")\
]

*Not to be confused with [World set (Portage)](https://wiki.gentoo.org/wiki/World_set_(Portage) "World set (Portage)").*

The **selected-packages set** contains the user-selected \"world\" packages that are listed in the [/var/lib/portage/world] file. The selected-packages set is colloquially referred to as the **world file**.

** See also**\
See [package sets](https://wiki.gentoo.org/wiki/Package_sets "Package sets") for a list of other sets available in Gentoo

## Contents

-   [[1] [Managing the selected-packages set]](#Managing_the_selected-packages_set)
    -   [[1.1] [Listing the selected-packages set]](#Listing_the_selected-packages_set)
    -   [[1.2] [Emerge a package without adding it to the world file]](#Emerge_a_package_without_adding_it_to_the_world_file)
    -   [[1.3] [Checking the world file]](#Checking_the_world_file)
    -   [[1.4] [Adding an atom without recompilation]](#Adding_an_atom_without_recompilation)
-   [[2] [Tips]](#Tips)
    -   [[2.1] [Editing world file by hand]](#Editing_world_file_by_hand)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Managing the selected-packages set]

### [Listing the selected-packages set]

[eix](https://wiki.gentoo.org/wiki/Eix "Eix") can be used to list the selected-packages set:

`user `[`$`]`eix -c --selected-file`

### [Emerge a package without adding it to the world file]

In order to avoid problems in dependency resolution when updating the system, the [/var/lib/portage/world] file should contain as few dependencies as possible. So use the `--oneshot` (`-1`) option for emerging dependencies.

`root `[`#`]`emerge --ask --oneshot <category/atom>`

### [Checking the world file]

The [emaint] command can be used to see if any problems exist in the world file:

`user `[`$`]`/usr/sbin/emaint --check world`

    Emaint: check world        100% [============================================>]

If any problems are found then run the following:

`root `[`#`]`/usr/sbin/emaint --fix world`

### [Adding an atom without recompilation]

To add a package to the selected-packages set without *recompiling* the package:

`root `[`#`]`emerge --ask --noreplace <category/atom>`

It will add the atom to the [/var/lib/portage/world] file without compiling it again.

## [Tips]

### [Editing world file by hand]

Though the [emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge") man page says that the world file can \"safely\" be edited by hand, Portage will aggressively rewrite that file. Comments or changes in order of packages will be lost and there will be no checking for typos.

The `--deselect` (`-W`) or `--noreplace` (`-n`) options to the emerge command may be used to add or remove packages from the world file, without actually performing package installation or removal.

## [See also]

-   [Package sets](https://wiki.gentoo.org/wiki/Package_sets "Package sets") --- describes package sets in high detail and includes a list of all typically available sets on a Gentoo system.
-   [/etc/portage/sets](https://wiki.gentoo.org/wiki//etc/portage/sets "/etc/portage/sets") --- an optional directory that is used to create user defined package sets
-   [User:Sam/Portage help/Maintaining a Gentoo system#World file hygiene](https://wiki.gentoo.org/wiki/User:Sam/Portage_help/Maintaining_a_Gentoo_system#World_file_hygiene "User:Sam/Portage help/Maintaining a Gentoo system")
-   [User:Vaukai/checkworldfile](https://wiki.gentoo.org/wiki/User:Vaukai/checkworldfile "User:Vaukai/checkworldfile") ([alternative version](https://wiki.gentoo.org/wiki/User:Luttztfz/checkworldfile "User:Luttztfz/checkworldfile"))

## [External resources]

-   [https://forums.gentoo.org/viewtopic-t-1075276.html](https://forums.gentoo.org/viewtopic-t-1075276.html) - Cleaning the world file (wiki) - check the script.