\
**\@preserved-rebuild** is a [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") [package set](https://wiki.gentoo.org/wiki/Package_sets "Package sets"). During library updates, the old version of the library is often being kept because other packages are still being built against this library. [[emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge")] could solve this by updating all these packages that are still built against the old version. However, this can have undesired effect like a long installation time when updating a library. So [emerge] does not update the depending libraries, but put them into a set instead: **\@preserved-rebuild**.

After finishing a library update, it is possible to clean up the old library version via:

`root `[`#`]`emerge --ask @preserved-rebuild`

If prompted to by emerge after a full \@world set update, it is recommended to execute this command after a depclean operation in emerge. This will reduce the possibility of unnecessarily rebuilding orphaned packages that would only be deleted otherwise.

## [See also]

-   [preserve-libs](https://wiki.gentoo.org/wiki/Preserve-libs "Preserve-libs") --- a [Portage feature](https://wiki.gentoo.org/wiki/FEATURES "FEATURES")
-   [World set (Portage)](https://wiki.gentoo.org/wiki/World_set_(Portage) "World set (Portage)") --- the combination of the [*system set*](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)"), the [*selected set*](https://wiki.gentoo.org/wiki/Selected_set_(Portage) "Selected set (Portage)"), and the *\@profile set*.
-   [System set (Portage)](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)") --- the software packages required for a standard Gentoo Linux installation to run properly.
-   [Selected set (Portage)](https://wiki.gentoo.org/wiki/Selected_set_(Portage) "Selected set (Portage)") --- contains the packages the admin has explicitly installed
-   [Selected-packages set (Portage)](https://wiki.gentoo.org/wiki/Selected-packages_set_(Portage) "Selected-packages set (Portage)") --- contains the user-selected \"world\" packages that are listed in the [/var/lib/portage/world] file.