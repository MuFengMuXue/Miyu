# Arch terminology

This page is intended to be a page to demystify common terms used among the Arch Linux community.

## ABS
ABS stands for Arch build system.

## Arch Linux
Arch should be referred to as:

* Arch Linux,
* Arch (Linux implied),
* archlinux (UNIX name).

Archlinux, ArchLinux, archLinux, aRcHlInUx, etc. are all weird, and weirder mutations.

Officially, the "Arch" in "Arch Linux" is pronounced /ɑːrtʃ/ as in an "archer" (bowman) or "archnemesis", and not as in "ark" or "archangel".

## Arch Linux Archive
The Arch Linux Archive (a.k.a. ALA), formerly known as Arch Linux Rollback Machine (a.k.a. ARM), stores official repositories snapshots, ISO images and bootstrap tarballs across time.

## ArchWiki
ArchWiki is a place to find documentation about Arch Linux. Anyone can contribute to the wiki.

## AUR
The Arch User Repository (AUR) is a community-driven repository for Arch users. It contains package descriptions—PKGBUILDs—that allow you to build a package from source with makepkg and then install it via pacman. The AUR was created to organize and share new packages from the community and to help expedite popular packages' inclusion into the extra repository.

A good number of new packages that enter the official repositories start in the AUR. In the AUR, users are able to contribute their own package builds——and related files. The AUR community has the ability to vote for packages in the AUR. If a package becomes popular enough—provided it has a compatible license and good packaging technique—it may be entered into the extra repository (directly accessible by pacman or the ABS).

You can access the Arch Linux User Community Repository at https://aur.archlinux.org.

## BBS
Bulletin board system, but in Arch's case, it is just the support forum.

## core
The core repository contains the bare packages needed for an Arch Linux system. core has everything needed to get a working command-line system.

## Custom repository
Anyone can create a custom local repository and put it online for other users. To create a repository, you need a set of packages and a pacman-compatible database file for your packages. Host your files online and everyone will be able to use your repository by adding it as a regular repository.

## Developer
Half-gods working to improve Arch for no financial gain. Developers are outranked only by our gods, Judd Vinet and Aaron Griffin, who in turn are outranked by tacos.

## extra
Arch core package set is fairly streamlined, but we supplement this with a larger, more complete extra repository. This repository is constantly growing with the help of packages submitted from our strong community.

This is where GUI tools—such as desktop environments and window managers—and common programs are found.

## initramfs/initrd
See Arch boot process#initramfs.

## KISS
KISS principle (Keep It Simple, Stupid)—simplicity is a main principle Arch Linux tries to achieve.

## makepkg
makepkg will build packages for you. makepkg will read the metadata required from a PKGBUILD file. All it needs is a build-capable Linux platform, , and some build scripts. The advantage to a script-based build is that you only really do the work once. Once you have the build script for a package, you just need to run makepkg and it will do the rest: download and validate source files, check dependencies, configure the build time settings, build the package, install the package into a temporary root, make customization, generate meta-info, and package the whole thing up for pacman to use.

## namcap
namcap is a package analysis utility that looks for problems with Arch Linux packages or their PKGBUILD files. It can apply rules to the file list, the files themselves, or individual  files.

## Package
See pacman#Installing packages.

## Package maintainer
The role of a package maintainer is to update packages as new versions become available upstream, and to field support questions relating to bugs in said packages. The term applies to:

* Arch staff previously called Trusted Users who maintain packages in the extra repository and oversee the AUR. They are appointed by a majority vote by the existing package maintainers and they follow the AUR Package Maintainer guidelines and Package Maintainer Bylaws.
* Developers who maintain packages in the official repositories (core in particular).
* All users who maintain PKGBUILD files in the AUR.

The maintainer of a package is the person currently responsible for the package. Previous maintainers should be listed as contributors in the  along with others who have contributed to the package.

## PKGBUILD
PKGBUILDs are small Bash scripts that are used to build Arch Linux packages. See Creating packages for more detail.

## Repository
A repository—informally referred as "repo"—has the pre-built packages of PKGBUILDs.

Official repositories are split into different parts for easy maintenance.

Pacman uses repositories to search for packages and install them.

A repository can be local (i.e. on your own computer) or remote (i.e. the packages are downloaded before they are installed).

See also #Custom repository.

## RTFM
RTFM (Read The Friendly Manual)—this simple message is replied to some newcomers who ask about the functionality of a program when it is clearly defined in a program's manual.

This acronym is an invitation to self-care, not an insult. It is often used when a user is seen as failing to make any attempt to find a solution to the problem themselves. If someone tells you this, they are not trying to offend you—they are just feeling frustrated with a perceived lack of effort.

The best thing to do if you are told to do this is to read the manual page.

If you do not find the answer to your question in the program manual, there are more ways to find the answer. You can:

* search the ArchWiki,
* search the BBS,
* search the mailing lists,
* search the web.

## Testing repositories
They are the repositories where major package updates are kept prior to release into the main repositories, so they can be bug tested and upgrade issues can be found. They are disabled by default but can be enabled in .

## The Arch Way
The unofficial term traditionally used to refer to the main Arch Linux principles.

## Trusted User
Trusted User (TU) is the old name for the package maintainer role.

## User repository
The same as Custom repository.

## Wiki
The same as ArchWiki.
