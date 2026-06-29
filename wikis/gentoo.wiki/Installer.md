** Important**\
This page is no longer useful. Currently relevant pages: [Installation](https://wiki.gentoo.org/wiki/Installation "Installation"), [Category:Installation](https://wiki.gentoo.org/wiki/Category:Installation "Category:Installation"), [Gentoo installation tips and tricks](https://wiki.gentoo.org/wiki/Gentoo_installation_tips_and_tricks "Gentoo installation tips and tricks").

**[] Archived article**\
\

This article is **archived (obsolete)**. Contents are surely incorrect for current usage, and are intended for historical reference only.

\
TLDR: **Do not use this article!**

\

**Resources**

[[]][Home](https://github.com/ChrisADR/installer)

installer is designed to aid users during the installation process of Gentoo Linux. It is capable of walking a beginner user through the regular installation process following key topics from the Gentoo Handbook. It is ChrisADR\'s personal project, the official installer project is in charge of designing the official Gentoo installer.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
-   [[3] [Removal]](#Removal)
    -   [[3.1] [Unmerge]](#Unmerge)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Installation]

installer is designed to be part of the Gentoo Live CD image, but it can also be installed via Portage.

### [Emerge]

`root `[`#`]`emerge --ask app-admin/installer`

## [Usage]

Once inside the live environment, it is ready to begin an installation process from scratch via:

`root `[`#`]`installer beginner`

You can also resume in a specific point of installation with:

`root `[`#`]`installer beginner -s N `

`root `[`#`]`installer beginner --step N`

Where N is a number between 1 and 11.

or

`root `[`#`]`installer beginner -t `

`root `[`#`]`installer beginner --tui `

installer can also be used by root to generate stageX tarball, which contains some configuration files that may help as backup configuration or in further installations, via:

`root `[`#`]`installer generate`

## [Removal]

Since installer will be only available by default in the live CD image, the only reason to unmerge installer is if you already installed it with Portage.

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose app-admin/installer`

## [See also]

-   [Project:Installer](https://wiki.gentoo.org/wiki/Project:Installer "Project:Installer") --- an attempt to increase the usability of Gentoo and related Linux distributions by providing an interface for users to backup and recover existing installations. Official Installer Project for Gentoo Linux

## [External resources]

-   [ChrisADR\'s guide of installer](https://blogs.gentoo.org/chrisadr/2018/05/02/installer-a-basic-gentoo-system-anyone-can-install/) - a Blog post which describes installer functionalities.