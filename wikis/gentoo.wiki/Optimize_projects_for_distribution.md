Open source software developers (upstream projects) are glad to see their software distributed by the different Linux distributions. This also makes users and the ebuild maintainers happy as well, since more software is available to be installed through the distributions package manager.

This article presents how to help ebuild maintainers to distribute upstream software.

Most aspects apply for all Linux distributions.

## Contents

-   [[1] [Description]](#Description)
-   [[2] [Dependencies]](#Dependencies)
-   [[3] [Tests]](#Tests)
-   [[4] [Versions]](#Versions)
-   [[5] [License]](#License)
-   [[6] [Folder structure]](#Folder_structure)
-   [[7] [File formats]](#File_formats)

### [Description]

-   Provide a short (\<= 79 characters), **neutral description** what the program does. Most distributions can copy and paste this line on demand.
    -   Good example: \"svg2bmp converts scalable vector graphics to black and white bitmap files\"
    -   Bad example: \"yat is a very sophisticated t00l which will blow your mind away it is the Swiss army knife for experts.\"
-   Provide a long (\~100 - 500 characters), neutral description too. Most distributions can copy and paste this to their package metadata.
-   List the names of the authors.
-   List the names of the package maintainers.
-   Where should bugs be sent to?

### [Dependencies]

-   Provide a list of dependencies. Which exact versions are required.
-   **Avoid to bundle libraries.** Do not mix external code in the tar ball of the project. This is very difficult to maintain. Bundled libraries usually get no bugfixes and security fixes. The license of the complete file set (tar ball) is often very complicate.

### [Tests]

-   Provide tests with **descriptive** names/messages.
-   Help the distributor to see, if a test failed, because it was run in a **sandbox**. Some tests require access to the filesystem.

### [Versions]

-   Use a well defined versioning system. See for example [semver.org](http://semver.org/)
    -   Package maintainers need this version number in the package.
-   If possible, tag a release on the version control system with the version number.
    -   Version number can be used in Gentoo for simple version bumps from foo-1.0.2 to foo-1.0.3.
-   Never change software after release without increasing the version number. If the checksum changes, it brakes the package.
-   Provide a compressed file for every versioned release.

### [License]

-   Provide a LICENSE (or COPYING) file in the root directory.
-   Verify, that the license information about the project is the same in the file header, manual, website\...
-   Avoid inventing a new license.
-   In the case of GPL, please add the version. Do you provide the software as GPL-2 or later (we call it GPL-2+), or only as GPL-2?
-   Do not modify an open source license with personal edits (unless the license is something like the MIT license which has fill-in-the-blank spots for the copyright holders name and year).

### [Folder structure]

-   [README](https://en.wikipedia.org/wiki/README "wikipedia:README") (or README.\*) in the root folder describes what the program does and how to install it.
-   [CHANGELOG](https://en.wikipedia.org/wiki/Changelog "wikipedia:Changelog") describes what changed between the releases. For packagers it is important to find here if a bug was fixed, or dependencies changed.

### [File formats]

-   [.tar.gz], [.tar.bz2], and [.tar.xz] are perfect since each format is part of the [\@system](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)") set.
-   [.zip] files are fine too, but require an additional dependency ([[[app-arch/unzip]](https://packages.gentoo.org/packages/app-arch/unzip)[]]) on Gentoo.