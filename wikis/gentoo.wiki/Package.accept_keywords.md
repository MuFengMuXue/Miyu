\
**[package.accept_keywords]** and **[package.keywords]** are files or directories of files containing definitions for per-package `ACCEPT_KEYWORDS` statements. They are useful for mixing unstable packages in with a normally stable system packages or vice versa.

These two locations allow `ACCEPT_KEYWORDS` to be augmented for single packages. If both [package.accept_keywords] and [package.keywords] are present, both will be used; values from [package.accept_keywords] will override values from [package.keywords]. The [package.accept_keywords] location is intended to replace the [package.keywords] location, since profiles support a different form of [package.keywords] which modifies effective `KEYWORDS` (rather than `ACCEPT_KEYWORDS`).

** See also**\
See [Knowledge Base:Accepting a keyword for a single package](https://wiki.gentoo.org/wiki/Knowledge_Base:Accepting_a_keyword_for_a_single_package "Knowledge Base:Accepting a keyword for a single package") and [the handbook on mixing stable and testing branches](https://wiki.gentoo.org/wiki/Handbook:AMD64/Portage/Branches#Mixing_stable_with_testing "Handbook:AMD64/Portage/Branches").

## Contents

-   [[1] [File format]](#File_format)
-   [[2] [Usage examples]](#Usage_examples)
-   [[3] [Maintenance]](#Maintenance)
    -   [[3.1] [Comments]](#Comments)
    -   [[3.2] [\~ARCH system-wide]](#.7EARCH_system-wide)
    -   [[3.3] [Use stable packages on testing systems]](#Use_stable_packages_on_testing_systems)
    -   [[3.4] [Unkeyworded packages]](#Unkeyworded_packages)
    -   [[3.5] [Live ebuilds]](#Live_ebuilds)
-   [[4] [Additional information]](#Additional_information)
-   [[5] [Find obsolete entries]](#Find_obsolete_entries)
    -   [[5.1] [Using eix]](#Using_eix)
    -   [[5.2] [Using portpeek]](#Using_portpeek)
-   [[6] [See also]](#See_also)

## [File format]

-   Comment lines begin with `#` (no inline comments).
-   One DEPEND atom per line followed by additional `KEYWORDS`.
-   Lines without any `KEYWORDS` imply unstable host arch.

## [Usage examples]

For specific packages, allow installation from the testing branch, or restrict to installation from the stable branch:

[FILE] **`/etc/portage/package.accept_keywords`package.accept_keywords single file example**

    # Always use unstable libgd
    media-libs/libgd ~amd64

    # Only use stable (LTS) kernel
    sys-kernel/gentoo-kernel -~amd64

    # Always use unstable netcat
    net-analyzer/netcat

Use [Distribution Kernel](https://wiki.gentoo.org/wiki/Project:Distribution_Kernel "Project:Distribution Kernel") from testing branch:

[FILE] **`/etc/portage/package.accept_keywords/kernel`package.accept_keywords as a directory example**

    # Always use mainline dist-kernel
    sys-kernel/gentoo-kernel-bin
    virtual/dist-kernel

Use a specific version of package:

[FILE] **`/etc/portage/package.accept_keywords/netcat`package.accept_keywords as a directory example**

    # Always use testing version 110.20180111-r2 until stable catches up
    =net-analyzer/netcat-110.20180111-r2

## [Maintenance]

### [Comments]

When adding a USE flag or keyword, it is always helpful to leave a comment to why it was set in the first place.

[FILE] **`/etc/portage/package.accept_keywords/scummvm`p.a_k example**

    # Using ~amd64 package due to bug XXXX
    games-emulation/scummvm

It is generally good practice to use the testing package until the stable version becomes greater than the testing version; then the system would switch back over to tracking the stable package.

[FILE] **`/etc/portage/package.accept_keywords/engrampa`Explicitly setting version example**

    # engrampa 1.28.1 has issues with extracting encrypted zip files
    =app-arch/engrampa-1.28.2

### [][\~ARCH system-wide]

A common trap new and experienced users fall into, is mixing too many stable and testing packages on their system.

If a user has over 100 packages in their [/etc/portage/package.accept_keywords], then it\'s time to think if the user is managing their system correctly or not. One of the main issues of running such a large [/etc/portage/package.accept_keywords] is that [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") is much more likely to run into conflicts.

** Warning**\
Once a system has been switched to testing, a user cannot simply just downgrade back to stable. Although this can be done, it is highly recommend to reinstall instead.

**Some examples:**

1\. A user is running a stable system where they always want the latest [GNOME](https://wiki.gentoo.org/wiki/GNOME "GNOME"), [Firefox](https://wiki.gentoo.org/wiki/Firefox "Firefox"), [LibreOffice](https://wiki.gentoo.org/wiki/LibreOffice "LibreOffice") and [Kernel](https://wiki.gentoo.org/wiki/Project:Distribution_Kernel "Project:Distribution Kernel").

      In this case, the user would most likely be better off by switching to a full ~ARCH system.

2\. A user is running a stable system and notice the next version of the desktop environment [MATE](https://wiki.gentoo.org/wiki/MATE "MATE") has a fix to an issue they are currently having.

      In this example, the user would pin the MATE dependencies in /etc/portage/package.accept_keywords/mate           (i.e. =mate-base/mate-1.30). This would mean the system would pull all the 1.30 versions from testing and once stable catches up, portage will start tracking the stable branch again.

3\. A user has lots of \~ARCH keywords for games or [Haskell](https://wiki.gentoo.org/wiki/Haskell "Haskell")

      These packages rarely get stable keyword so are fine to run with a stable system in most cases.

### [Use stable packages on testing systems]

Sometimes a user will want a few packages to be stable only. The normally usage case for this is using the kernel with out of tree modules, such as ZFS, where it is recommended to stick to the LTS releases. To do this see the below example:

[FILE] **`/etc/portage/package.accept_keywords`package.accept_keywords example**

    # Only use stable (LTS) kernel
    sys-kernel/gentoo-kernel -~amd64

\

### [Unkeyworded packages]

Packages that are not yet tested to an acceptable state for testing are added to Gentoo without a keyword such as **\~am64**.

For the correct way to set these packages see [Knowledge_Base:Missing_keywords_and_keyword_requests](https://wiki.gentoo.org/wiki/Knowledge_Base:Missing_keywords_and_keyword_requests "Knowledge Base:Missing keywords and keyword requests") and if require, how to request the package to be keyworded.

### [Live ebuilds]

Live ebuilds (also known as 9999 releases in Gentoo) are ebuilds that pull the source code directly from the upstream project\'s git sources. While not useful for most users, the examples below will list two examples of when they might reasonable be a better choice for a user to consider:

A general user need may be to test a feature that is only available from a project\'s current git repository. An emulator needing a fix to run a new game would be an example of this need.

A system admin may find it useful when an upstream project they rely on is in code freeze ready for a big release, and the user wishes to help test how it will preform on a real system and report back the bugs they uncover. Remembering to switch back to the versioned releases once the test cycle is complete.

See [Live_ebuilds](https://wiki.gentoo.org/wiki/Live_ebuilds "Live ebuilds") for more information on managing a system with live ebuilds.

## [Additional information]

Note: In addition to the normal values from `ACCEPT_KEYWORDS` [package.keywords] supports three special tokens:

-   `*` - Package is visible if it is stable on any architecture.
-   `~*` - Package is visible if it is in testing on any architecture.
-   `**` - Package is always visible (`KEYWORDS` are ignored completely).

Additional note: If you encounter the `-* KEYWORD`, this indicates that the package is known to be broken on all systems which are not otherwise listed in `KEYWORDS`. For example, a binary only package which is built for **[amd64]** will look like:

[FILE] **`games-fps/quake3-demo-1.11.ebuild`Broken on all but amd64 example**

    KEYWORDS="-* amd64"

To accept this package anyway, use one of the other keywords in [package.accept_keywords] like this:

[FILE] **`/etc/portage/package.accept_keywords`Accept anyways example**

    games-fps/quake3-demo amd64

## [Find obsolete entries]

### [Using eix]

Using [[[app-portage/eix]](https://packages.gentoo.org/packages/app-portage/eix)[]]:

`user `[`$`]`eix-test-obsolete`

    Redundant in /etc/portage/package.keywords:

    ... considered as REDUNDANT_IF_NO_CHANGE
    [I] app-text/pdftk (3.0.0@09/06/2018): gcj-free version of pdftk written in Java
    [I] dev-java/commons-lang (3.6(3.6)@03/30/2018): Commons components to manipulate core java classes
    Found 2 matches

### [Using portpeek]

Using [[[app-portage/portpeek]](https://packages.gentoo.org/packages/app-portage/portpeek)[]]:

`user `[`$`]`portpeek --keyword`

## [See also]

-   [ACCEPT KEYWORDS](https://wiki.gentoo.org/wiki/ACCEPT_KEYWORDS "ACCEPT KEYWORDS")
-   [Accepting a keyword for a single package](https://wiki.gentoo.org/wiki/Knowledge_Base:Accepting_a_keyword_for_a_single_package "Knowledge Base:Accepting a keyword for a single package")
-   [Cleaning /etc/portage/package.\* from unused entries](https://wiki.gentoo.org/wiki/User:Tillschaefer/cleanup_package "User:Tillschaefer/cleanup package")