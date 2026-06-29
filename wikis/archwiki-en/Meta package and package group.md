# Meta package and package group

A meta package and a package group can be defined by the packager to denote a set of related packages. Both can allow to install or uninstall this set of packages simultaneously by using the meta package or the group name as a substitute for each individual package name. While a group is not a package, it can be installed in a similar fashion to a package, see pacman#Installing package groups and PKGBUILD#groups.

## Difference between meta package and package group
The difference between a meta package and a regular package is that a meta package is empty and exists purely to link related packages together via dependencies. A meta package, often (though not always) titled with the "-meta" suffix, provides similar functionality to a package group in that it enables multiple related packages to be installed or uninstalled simultaneously.

Each solution has advantages and disadvantages:

meta package:

* Meta packages can be installed just like any other package (see pacman#Installing specific packages).
* Meta packages can be removed like any other package (see pacman#Removing packages).
* Any new member packages will be installed when the meta package itself is updated with a new set of dependencies.
* Users cannot choose which meta package dependencies they wish to install.
* Users cannot remove meta package dependencies without having to uninstall the meta package itself.

group:

* Package groups will prompt users to select the packages from the group that they wish to install (see pacman#Installing package groups).
* Users cannot uninstall a group, because they installed a list of packages. Instead,  tries to remove all members of the group.
* New group members will not be automatically installed. Instead, the command {{ic|comm -23 <(pacman -Sg package_group  awk '{print $2}'  sort) <(pacman -Qq  sort)}} can be run to show which members of a  are not installed on the system.
* Users can choose which group members they wish to install.
* Users can uninstall group members without having to remove the entire group.

## Meta packages
The most important meta package is . It contains a minimal package set that defines a basic Arch Linux installation. It includes:

* basics such as  and bash,
* distribution related things such as pacman and systemd,
* POSIX tools such as core utilities, process, file and file compression utilities,
* networking tools such as .

The kernel is an optional dependency. See the announcement when it was introduced, and reasoning why base is a meta package.

An other common meta package is . It contains a complete build environment for makepkg. See the reasoning why it has become a meta package.

## Groups
Package groups are commonly used to facilitate the installation of desktop environments. See Desktop environment#List of desktop environments.

An other example is the  group for the professional audio software available in the official repositories.

See the list of all package groups.
