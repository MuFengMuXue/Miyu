# Arch User Repository

The Arch User Repository (AUR) is a community-driven repository for Arch Linux users. It contains package descriptions (PKGBUILDs) that allow you to compile a package from source with makepkg and then install it via pacman. The AUR was created to organize and share new packages from the community and to help expedite popular packages' inclusion into the extra repository. This document explains how users can access and utilize the AUR.

A good number of new packages that enter the official repositories start in the AUR. In the AUR, users are able to contribute their own package builds ( and related files). The AUR community has the ability to vote for packages in the AUR. If a package becomes popular enough—provided it has a compatible license and good packaging technique—it may be entered into the extra repository (directly accessible by pacman or from the Arch build system).

## Getting started
Users can search and download s from the AUR Web Interface. These s can be built into installable packages using makepkg, then installed using pacman.

* Ensure  is installed.
* Glance over the #Frequently asked questions for answers to the most common questions.
* You may wish to adjust  to optimize the build process to your system prior to building packages from the AUR. A significant improvement in package build times can be realized on systems with multi-core processors by adjusting the  variable, by using multiple cores for compression, or by using different compression algorithm. Users can also enable hardware-specific compiler optimizations via the  variable. See makepkg#Optimization for more information.

if you have set up AUR SSH authentication then it is also possible to interact with the AUR through SSH: type  for a list of available commands.

## Installing and upgrading packages
Installing packages from the AUR is a relatively simple process. Essentially:

# Acquire the build files, including the  and possibly other required files, like systemd units and patches (often not the actual code).
# Verify that the  and accompanying files are not malicious or untrustworthy.
# Run  in the directory where the files are saved. This will download the code, compile it, and package it.
# Run  to install the package onto your system.

## Prerequisites
First, ensure that the necessary tools are installed by installing ; this meta package has  and other tools needed for compiling from source, listed as dependencies.

Next, choose an appropriate build directory. A build directory is simply a directory where the package will be made or "built" from source, and can be any directory. The examples in the following sections will use  as the build directory.

## Acquire build files
Locate the package in the AUR. This is done using the search field at the top of the AUR home page. Clicking the application's name in the search list brings up an information page on the package. Read through the description to confirm that this is the desired package, note when the package was last updated, and read any comments.

There are several methods for acquiring the build files for a package:

* Clone its git repository, labeled "Git Clone URL" in the "Package Details" on its AUR page. This is the preferred method, an advantage of which is that you can easily get updates to the package via .
:
* Download a snapshot, either by clicking the "Download snapshot" link under "Package Actions" on the right hand side of its AUR page, or in a terminal:
:
:
* Use the read-only mirror archlinux/aur on GitHub, where every package is located in a branch. It is recommended to clone only a single branch (the whole repository is too big and performance would be low). You can do this with one of the following two methods:
** Use :
** Do a partial clone of this repository () and add branches selectively:
::

## Acquire a PGP public key if needed
Check if a signature file in the form of .sig or .asc is part of the  source array. If that is the case, then acquire one of the public keys listed in the PKGBUILD validpgpkeys array. Refer to makepkg#Signature checking for more information.

## Build the package
Change directories to the directory containing the package .

 $ cd package_name

View the contents of all provided files. For example, to use the pager less to view , do:

 $ less PKGBUILD

Make the package. After manually confirming the contents of the files, run makepkg as a normal user. Some helpful flags:

* / automatically resolves and installs any dependencies with pacman before building. If the package depends on other AUR packages, you will need to manually install them first.
* / installs the package if it is built successfully. This lets you skip the next step that is usually done manually.
* / removes build-time dependencies after the build, as they are no longer needed. However, these dependencies may need to be reinstalled the next time the package is updated.
* / cleans up temporary build files after the build, as they are no longer needed. These files are usually needed only when debugging the build process.

## Install the package
The package can now be installed with pacman:

 # pacman -U package_name-version-architecture.pkg.tar.zst

## Upgrading packages
In the directory containing the package's , you must first update the files and changes by using the command

 $ git pull

then follow the previous build and install instructions.

## Updating packages
The AUR is unsupported, so any packages you install are your responsibility to update, not pacman's. If packages in the official repositories are updated, you will need to rebuild any AUR packages that depend on those libraries. The  tool and  hook from  can help find packages needing rebuilt.

## Account status
## Suspension
When editing a user as a Package Maintainer, the Suspended field can be set, which suspends the target user. When a user is suspended, they cannot:

* Login to https://aur.archlinux.org
* Receive notifications
* Interact with the git interface

## Inactivity
When editing your own account or another as a Package Maintainer, the Inactive field can be set. Inactive accounts are used for two reasons:

* Display the date someone was marked inactive on their account page
* Generate a current count of active Package Maintainer based on their inactivity for new proposals

## Feedback
## Commenting on packages
The AUR Web Interface has a comments facility that allows users to provide suggestions and feedback on improvements to the  contributor.

Python-Markdown provides basic Markdown syntax to format comments.

## Voting for packages
One of the easiest activities for all Arch users is to browse the AUR and vote for their favourite packages using the online interface. All packages are eligible for adoption by a Package Maintainer for inclusion in the extra repository, and the vote count is one of the considerations in that process; it is in everyone's interest to vote!

Sign up on the AUR website to get a "Vote for this package" option while browsing packages. After signing up, it is also possible to vote from the commandline with .

Alternatively, if you have set up AUR SSH authentication, you can directly vote from the command line using your ssh key. This means that you will not need to save or type in your AUR password.

 $ ssh aur@aur.archlinux.org vote package_name

## Flagging packages out-of-date
First, you should flag the package out-of-date indicating details on why the package is outdated, preferably including links to the release announcement or the new release tarball.

You should also try to reach out to the maintainer directly by email. If there is no response from the maintainer after two weeks, you can file an orphan request. See AUR submission guidelines#Requests for details.

## Debugging the package build process
# Ensure your build environment is up-to-date by upgrading before building anything.
# Ensure you have  installed.
# Use the  option with  to check and install all dependencies needed before starting the build process.
# Try the default makepkg configuration.
# See Makepkg#Troubleshooting for common issues.

If you are having trouble building a package, first read its  and the comments on its AUR page.

It is possible that a  is broken for everyone. If you cannot figure it out on your own, report it to the maintainer (e.g. by posting the errors you are getting in the comments on the AUR page). You may also seek help in the AUR Issues, Discussion & PKGBUILD Requests forum.

The reason might not be trivial after all. Custom ,  and  can cause failures. To avoid problems caused by your particular system configuration, build packages in a clean chroot. If the build process still fails in a clean chroot, the issue is probably with the .

See Creating packages#Checking package sanity about using namcap. If you would like to have a  reviewed, post it on the aur-general mailing list to get feedback from the Package Maintainers and fellow AUR members, or the Creating & Modifying Packages forum. You could also seek help in the IRC channel #archlinux-aur on the Libera Chat network.

## Submitting packages
Users can share s using the Arch User Repository. See AUR submission guidelines for details.

## Web interface translation
See i18n.md in the AUR source tree for information about creating and maintaining translation of the AUR Web Interface.

## History
In the beginning, there was , and people contributed by simply uploading the , the needed supplementary files, and the built package itself to the server. The package and associated files remained there until a "Trusted user" (renamed as Package Maintainer) saw the program and adopted it.

Then the Trusted User Repositories were born. Certain individuals in the community were allowed to host their own repositories for anyone to use. The AUR expanded on this basis, with the aim of making it both more flexible and more usable. In fact, the AUR maintainers were referred to as TUs (Trusted Users) until the change in naming to Package Maintainers.

Between 2015-06-08 and 2015-08-08, the AUR transitioned from version 3.5.1 to 4.0.0, introducing the use of Git repositories for publishing the s.
Existing packages were dropped unless manually migrated to the new infrastructure by their maintainers.

## Git repositories for AUR3 packages
The AUR Archive on GitHub has a repository for every package that was in AUR 3 at the time of the migration.
Alternatively, there is the aur3-mirror repository which provides the same.

## Frequently asked questions
## What kind of packages are permitted on the AUR?
The packages on the AUR are merely "build scripts", i.e. recipes to build binaries for pacman. For most cases, everything is permitted, subject to usefulness and scope guidelines, as long as you are in compliance with the licensing terms of the content. For other cases, where it is mentioned that "you may not link" to downloads, i.e. contents that are not redistributable, you may only use the file name itself as the source. This means and requires that users already have the restricted source in the build directory prior to building the package. When in doubt, ask.

## How can I vote for packages in the AUR?
See #Voting for packages.

## What is a package maintainer?
See Arch terminology#Package maintainer.

## What is the difference between the Arch User Repository and the extra repository?
The Arch User Repository is where all s that users submit are stored, and must be built manually with makepkg. When s receive enough community interest and the support of a Package Maintainer, they are moved into the extra repository (maintained by the Package Maintainers), where the binary packages can be installed with pacman.

## Foo in the AUR is outdated; what should I do?
See #Flagging packages out-of-date.

In the meantime, you can try updating the package yourself by editing the  locally. Sometimes, updates do not require changes to the build or package process, in which case simply updating the  or  array is sufficient.

## Foo in the AUR does not compile when I run makepkg; what should I do?
You are probably missing something trivial; see #Debugging the package build process.

## ERROR: One or more PGP signatures could not be verified!; what should I do?
Most likely, you do not have the required public key(s) in your personal keyring to verify downloaded files. See Makepkg#Signature checking for details.

## How do I create a PKGBUILD?
Consult the AUR submission guidelines#Rules of submission, then see creating packages.

## I have a PKGBUILD I would like to submit; can someone check it to see if there are any errors?
There are several channels available to submit your package for review; see #Debugging the package build process.

## How to get a PKGBUILD into the extra repository?
Usually, at least 10 votes are required for something to move into extra. However, if a Package Maintainer wants to support a package, it will often be found in the repository.

Reaching the required minimum of votes is not the only requirement; there has to be a package maintainer willing to maintain the package. Package Maintainers are not required to move a package into the extra repository even if it has thousands of votes.

Usually, when a very popular package stays in the AUR, it is because:

* Arch Linux already has another version of a package in the repositories
* Its license prohibits redistribution
* It helps retrieve user-submitted s. AUR helpers are unsupported by definition.

See also Rules for Packages Entering the extra repository

## How can I speed up repeated build processes?
See Makepkg#Improving build times.

## What is the difference between foo and foo-git packages?
Many AUR packages come in "stable" release and "unstable" development versions. Development packages usually have a suffix denoting their Version Control System and are not intended for regular use, but may offer new features or bugfixes. Because these packages only download the latest available source when you execute , their  in the AUR does not reflect upstream changes. Likewise, these packages cannot perform an authenticity checksum on any VCS source.

See also System maintenance#Use proven software packages.

## Why has foo disappeared from the AUR?
It is possible the package has been adopted by a Package Maintainer and is now in the extra repository.

Packages may be deleted if they did not fulfill the rules of submission. See the aur-requests archives for the reason for deletion.

## How do I find out if any of my installed packages disappeared from AUR?
The simplest way is to check the HTTP status of the package's AUR page:

 $ comm -23 <(pacman -Qqm | sort) <(curl https://aur.archlinux.org/packages.gz | gzip -cd | sort)

## How can I obtain a list of all AUR packages?
* https://aur.archlinux.org/packages.gz
* Use  from
* New AUR Metadata Archives
