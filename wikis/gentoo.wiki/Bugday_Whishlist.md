### [Example of a bad topic]

Version bumps. A user who just copies [foo-1.0.ebuild] to [foo-2.0.ebuild] does not save any time for us. Compare:

-   User:

1.  Copy [foo-1.0.ebuild] to [foo-2.0.ebuild] (10 seconds)

-   Developer:

1.  Review PR (10 minutes)
2.  Ask to fix the PR, many comments (20 minutes)
3.  Test the PR (20-120 minutes)
4.  Merge with comments and attributions (10 minutes)

### [Example of a good topic]

-   A **generic bug** affecting **many packages**.
-   Ideally the bugs are already organized in one of the active [TRACKER](https://bugs.gentoo.org/buglist.cgi?cmdtype=runnamed&list_id=4640770&namedcmd=active%20TRACKER)s
-   The problem has typically an **easy fix** and requires **no discussion** and **no changes in eclasses**
-   Most of the workload can be provided by the contributor and relieves the Gentoo developers
-   Fixing variable names as in [[[bug #705764]](https://bugs.gentoo.org/show_bug.cgi?id=705764)[]] for gcc-10 support is a good example.

### [Suggestions]

Enter **your suggestion** for the next [Bugday](https://wiki.gentoo.org/wiki/Bugday "Bugday") **here**.

-   Testing pypy3 on more Python packages
-   Search old bug tickets and check, if it is solved already / still reproducible with latest version
-   Test, if programs which require CD/DVD/restricted downloads still install properly. (The [developers have access to very few discs](https://wiki.gentoo.org/wiki/List_of_discs_by_developers "List of discs by developers"). This topic requires users who have access to the media.)
-   Packages broken with Qt 5.15 [[[bug #726178]](https://bugs.gentoo.org/show_bug.cgi?id=726178)[]] (most have just a missing include line)
-   Improve the wiki pages about Ebuild/Package testing.
-   Properly define BDEPEND or port to EAPI 7 in the first place to fix building sysroots ([bug list](https://bugs.gentoo.org/buglist.cgi?quicksearch=%22EAPI%207%22%7C%22EAPI%3D7%22%7CBDEPEND))
-   [desktop-misc](https://wiki.gentoo.org/wiki/Project:Desktop_Miscellaneous "Project:Desktop Miscellaneous") is on the way to get dissolved. There are many open bug tickets, which would be easy to fix with a PR now.
-   Migrate ebuilds to the new lua eclass. Tracker: [[[bug #657722]](https://bugs.gentoo.org/show_bug.cgi?id=657722)[]]