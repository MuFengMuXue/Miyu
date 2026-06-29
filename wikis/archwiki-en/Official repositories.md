# Official repositories

A software repository is a storage location from which software packages are retrieved for installation.

Arch Linux official repositories contain essential and popular software, readily accessible via pacman. They are maintained by package maintainers.

Packages in the official repositories are constantly upgraded: when a package is upgraded, its old version is removed from the repository. There are no major Arch releases: each package is upgraded as new versions become available from upstream sources.

Each repository is always coherent, i.e. the packages that it hosts always have reciprocally compatible versions.

## Stable repositories
## core
This repository can be found in  on your favorite mirror.

core contains packages for:

* booting Arch Linux
* connecting to the Internet
* building packages
* management and repair of supported file systems
* the system setup process (e.g. )
as well as dependencies of the above (not necessarily makedepends) and the  meta package.

core has fairly strict quality requirements. Developers/users need to signoff on updates before package updates are accepted. For packages with low usage, a reasonable exposure is enough: informing people about update, requesting signoffs, keeping in core-testing up to a week depending on the severity of the change, lack of outstanding bug reports, along with the implicit signoff of the package maintainer.

## extra
This repository can be found in  on your favorite mirror.

extra contains all packages that do not fit in core.
This repository is jointly maintained by the Package Maintainers and Arch Developers.
Examples: Xorg, window managers, web browsers, media players, tools for working with languages such as Python and Ruby, and a lot more.

## multilib
This repository can be found in  on your favorite mirror.

multilib contains 32-bit software and libraries that can be used to run and build 32-bit applications on 64-bit installs (e.g. Steam etc.).

With the multilib repository enabled, the 32-bit compatible libraries are located under .

## Enabling multilib
To enable multilib repository, uncomment the  section in :

Then upgrade the system and install the desired multilib packages.

## Disabling multilib
Execute the following command to remove all packages that were installed from multilib:

 # pacman -R $(comm -12 <(pacman -Qq | sort) <(pacman -Slq multilib | sort))

If you have conflicts with gcc-libs reinstall the  package and the dependencies of the  package (see Pacman/Tips and tricks#Dependencies of a package).

Comment out the  section in :

Then upgrade the system.

## Testing repositories
The intended purpose of the testing repositories is to provide a staging area for packages to be placed prior to acceptance into the main repositories. Package maintainers (and general users) can then access these testing packages to make sure that there are no problems integrating the new package. Once a package has been tested and no errors are found, the package can then be moved to the primary repositories.

Not all packages need to go through this testing process. New packages go into a testing repository if:

* They are destined for the core repository. Everything in core must go through core-testing.
* They are expected to break something on update and need to be tested first.
* They affect many packages (such as  or ).
* They are built by a Junior Package Maintainer.

The testing repositories are also usually used for new releases of large collections of packages such as GNOME and KDE.

## core-testing
This repository can be found in  on your favorite mirror.

core-testing contains packages that are candidates for the core repository.

core-testing is the only repository that can have name collisions with any of the other official repositories. If enabled, it has to be the first repository listed in your  file.

## extra-testing
This repository is similar to the core-testing repository, but for packages that are candidates for the extra repository.

## multilib-testing
This repository is similar to the core-testing repository, but for packages that are candidates for the multilib repository.

## gnome-unstable
This repository contains testing packages for pre-releases (Alpha, Beta, RC) as well as stable versions of the GNOME desktop environment, prior to their transition to the main extra-testing repository.

To enable it, add the following lines to :

The gnome-unstable entry should be at the top in the list of repositories (i.e., above the enabled core-testing entry; see warnings above).

Please report packaging related bugs in Arch's GitLab, while anything else should be reported upstream to GNOME GitLab.

For additional assistance and information regarding this repository, please join the Matrix Group.

## kde-unstable
This repository contains the latest beta or Release Candidate of KDE Plasma and Applications.

To enable it, add the following lines to :

The kde-unstable entry should be at the top in the list of repositories (i.e., above the enabled core-testing entry; see warnings above).

Make sure you make bug reports if you find any problems.

## Disabling testing repositories
If you enabled testing repositories, but later on decided to disable them, you should:

# Remove (comment out) them from
# Perform a  to "rollback" your updates from these repositories.

The second item is optional, but keep it in mind if you notice any problems.

## Staging repositories
This repository contains broken packages and is used solely by developers during rebuilds of many packages at once. In order to rebuild packages that depend on, for example, a new shared library, the shared library itself must first be built and uploaded to the staging repositories to be made available to other developers. As soon as all dependent packages are rebuilt, the group of packages is then moved to the testing or the main repositories, whichever is more appropriate.

See the announcement of the introduction of the staging repositories for more historical details.

## Historical background
Most of the repository splits are for historical reasons. Originally, when Arch Linux was used by very few users, there was only one repository known as official (now core). At the time, official basically contained Judd Vinet's preferred applications. It was designed to contain one of each "type" of program — one DE, one major browser etc.

There were users back then that did not like Judd's selection, so since the Arch build system is so easy to use, they created packages of their own. These packages went into a repository called unofficial, and were maintained by developers other than Judd. Eventually, the two repositories were both considered equally supported by the developers, so the names official and unofficial no longer reflected their true purpose. They were subsequently renamed to current and extra sometime near the release version 0.5.

Shortly after the 2007.8.1 release, current was renamed core in order to prevent confusion over what exactly it contains. The repositories are now more or less equal in the eyes of the developers and the community, but core does have some differences. The main distinction is that packages used for Installation CDs and release snapshots are taken only from core. This repository still gives a complete Linux system, though it may not be the Linux system you want.

Some time around 0.5/0.6, there were a lot of packages that the developers did not want to maintain. Jason Chu set up the "Trusted User Repositories", which were unofficial repositories in which trusted users could place packages they had created. There was a staging repository where packages could be promoted into the official repositories by one of the Arch Linux developers, but other than this, the developers and trusted users were more or less distinct.

This worked for a while, but not when trusted users got bored with their repositories, and not when other users wanted to share their own packages. This led to the development of the AUR. The Trusted Users were conglomerated into a more closely knit group, and they now collectively maintained the community repository. The TUs were still a separate group from the Arch Linux developers, and there was not a lot of communication between them. However, popular packages were still promoted from community to extra on occasion. The AUR also allows all users to submit PKGBUILDs.

After a kernel in core broke many user systems, the "core signoff policy" was introduced. Since then, all package updates for core need to go through the core-testing repository first, and only after multiple signoffs from other developers or people on the Arch Testing Team are then allowed to move. Over time, it was noticed that various core packages had low usage, and user signoffs or even lack of bug reports became informally accepted as criteria to accept such packages.

In late 2009/the beginning of 2010, with the advent of some new filesystems and the desire to support them during installation, along with the realization that core was never clearly defined (just "important packages, handpicked by developers"), the repository received a more accurate description.

Starting in 2021, and finalized in late 2023, the "Trusted Users" were renamed to "Package Maintainers".

In 2023 after years of prior work the distribution migrated their back-end services to git and in the same run also switched to a new repository layout. In the new layout extra would contain all packages that were previously in community and the testing repositories were split from testing to core-testing and extra-testing, community-testing was removed entirely. From that point on the Package Maintainers were also able to push new packages to extra.
