*Not to be confused with [World file (Portage)](https://wiki.gentoo.org/wiki/World_file_(Portage) "World file (Portage)").*

The **world set**, also referred to as **\@world**, is the combination of the [*system set*](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)"), the [*selected set*](https://wiki.gentoo.org/wiki/Selected_set_(Portage) "Selected set (Portage)"), and the *\@profile set*.

Later, when a world update is requested (through [emerge -uDN \@world] or similar command), Portage will use the world set as the base for its update calculations. A long command version of the command would be as follows:

`root `[`#`]`emerge --update --deep --newuse @world`

## [See also]

-   [System set (Portage)](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)") --- the software packages required for a standard Gentoo Linux installation to run properly.
-   [Selected set (Portage)](https://wiki.gentoo.org/wiki/Selected_set_(Portage) "Selected set (Portage)") --- contains the packages the admin has explicitly installed
-   [Selected-packages set (Portage)](https://wiki.gentoo.org/wiki/Selected-packages_set_(Portage) "Selected-packages set (Portage)") --- contains the user-selected \"world\" packages that are listed in the [/var/lib/portage/world] file.
-   [/etc/portage/sets](https://wiki.gentoo.org/wiki//etc/portage/sets "/etc/portage/sets") --- an optional directory that is used to create user defined package sets
-   [Knowledge Base: Remove orphaned packages](https://wiki.gentoo.org/wiki/Knowledge_Base:Remove_orphaned_packages#Analysis "Knowledge Base:Remove orphaned packages") - The process of finding orphaned dependencies explained.