# AUR submission guidelines

Users can share PKGBUILD scripts using the Arch User Repository.  It does not contain any binary packages but allows users to upload s that can be downloaded by others. These s are completely unofficial and have not been thoroughly vetted, so they should be used at your own risk.

## Submitting packages
If you are unsure in any way about the package or the build/submission process even after reading this section twice, submit the  to the AUR mailing list, the AUR forum on the Arch forums, or ask on our IRC channel for public review before adding it to the AUR.

## Rules of submission
When submitting a package to the AUR, observe the following rules:

* The submitted s must not build applications already in any of the official binary repositories under any circumstances. Check the official package database for the package. If any version of it exists, do not submit the package. If the official package is out-of-date, flag it as such. If the official package is broken or is lacking a feature, then please file a bug report.
:Exception to this strict rule may only be packages having extra features enabled and/or patches in comparison to the official ones. In such an occasion the  should be different to express that difference. For example, a package for GNU screen containing the sidebar patch could be named . Additionally the  array should be used in order to avoid conflicts with the official package.

* Check the AUR if the package already exists. If it is currently maintained, changes can be submitted in a comment for the maintainer's attention. If it is unmaintained or the maintainer is unresponsive, the package can be adopted and updated as required. Do not create duplicate packages.

* Make sure the package you want to upload is useful. Will anyone else want to use this package? Is it extremely specialized? If more than a few people would find this package useful, it is appropriate for submission.

:The AUR and official repositories are intended for packages which install general software and software-related content, including one or more of the following: executable(s); configuration file(s); online or offline documentation for specific software or the Arch Linux distribution as a whole; media intended to be used directly by software.

* Packages that do not support the  architecture are not allowed in the AUR.

* Do not use  in an AUR  unless the package is to be renamed, for example when Ethereal became Wireshark. If the package is an alternate version of an already existing package, use  (and  if that package is required by others). The main difference is: after syncing (-Sy) pacman immediately wants to replace an installed, 'offending' package upon encountering a package with the matching  anywhere in its repositories; , on the other hand, is only evaluated when actually installing the package, which is usually the desired behavior because it is less invasive.

* Packages that build from a version control system and are not tied to a specific version need to have an appropriate suffix,  for git and so on, see VCS package guidelines#Package naming for a full list.

* Packages that use prebuilt deliverables, when the sources are available, must use the  suffix. An exception to this is with Java. The AUR should not contain the binary tarball created by makepkg, nor should it contain the filelist. If you are packaging a non-free software, see also Nonfree applications package guidelines#Package naming regarding usage of  suffix.

* Packages that build from source using a specific version do not use a suffix.

* Please add a comment line to the top of the  file which contains information about the current maintainers and previous contributors, respecting the following format. Remember to disguise your email to protect against spam. Additional lines are optional.

:

:If you are assuming the role of maintainer for an existing , add your name to the top like this
:
:If there were previous maintainers, put them as contributors. The same applies for the original submitter if this is not you. If you are a co-maintainer, add the names of the other current maintainers as well.
:

* Add a  file and/or a REUSE.toml file to your repository. You are encouraged to follow the Arch package guidelines#Package sources licenses and license your submission under the 0BSD license.
:

## Authentication
For write access to the AUR, you need to have an SSH key pair. The content of the public key needs to be copied to your profile in My Account, and the corresponding private key configured for the  host. For example:

You should create a new key pair rather than use an existing one, so that you can selectively revoke the keys should something happen:

 $ ssh-keygen -f ~/.ssh/aur

## Creating package repositories
If you are creating a new package from scratch, establish a local Git repository and an AUR remote by cloning the intended pkgbase. If the package does not yet exist, the following warning is expected:

If you already have a package, initialize it as a Git repository if it is not one:

 $ git -c init.defaultBranch=master init

and add an AUR remote:

 $ git remote add label ssh://aur@aur.archlinux.org/pkgbase.git

Then fetch this remote to initialize it in the AUR.

## Publishing new package content
When releasing a new version of the packaged software, update the pkgver or pkgrel variables to notify all users that an upgrade is needed. Do not update those values if only minor changes to the PKGBUILD such as the correction of a typo are being published.

Do not commit mere  bumps for VCS packages. They are not considered out of date when the upstream has new commits. Only do a new commit when other changes are introduced, such as changing the build process.

Be sure to regenerate .SRCINFO whenever  metadata changes, such as  updates; otherwise the AUR will not show updated version numbers.

To upload or update a package:

* add at least  and ,
* add any additional new or modified helper files (such as .install files or local source files such as patches),
* add a package source license,
* commit with a meaningful commit message,
* push the changes to the AUR.

For example:

 $ makepkg --printsrcinfo > .SRCINFO
 $ git add PKGBUILD .SRCINFO
 $ git commit -m "useful commit message"
 $ git push

## Maintaining packages
* Check for feedback and comments from other users and try to incorporate any improvements they suggest; consider it a learning process!
* Please do not leave a comment containing the version number every time you update the package. This keeps the comment section usable for valuable content mentioned above.
* Please do not just submit and forget about packages! It is the maintainer's job to maintain the package by checking for updates and improving the .
* If you do not want to continue to maintain the package for some reason,  the package using the AUR web interface and/or post a message to the AUR Mailing List. If all maintainers of an AUR package disown it, it will become an "orphaned" package.
* Automation is a valuable tool for maintainers, but it can not replace manual intervention (e.g. projects can change license, add or remove dependencies, and other notable changes even for "minor" releases). Automated  updates are used at your own risk and any malfunctioning accounts and their packages may be removed without prior notice.

## Requests
Deletion, merge, and orphan requests can be created by clicking on the "Submit Request" link under "Package Actions" on the right hand side. This dispatches notification emails to the current package maintainer and to the aur-requests mailing list for discussion. Package Maintainers will then either accept or reject the request.

## Deletion
Request to unlist a  from the AUR. A short note explaining the reason for deletion is required, as well as supporting details (like when a package is provided by another package, if you are the maintainer yourself, it is renamed and the original owner agreed, etc).

## Merge
Request to delete a  and transfer its votes and comments to another . The name of the package to merge into is required.

This is the action to use if, for example, an upstream has renamed their project.

## Orphan
Request that a  be disowned. These requests will be granted after two weeks if the current maintainer did not react. The exception is if a package was flagged out-of-date for at least 180 days; orphan requests are then automatically accepted.
