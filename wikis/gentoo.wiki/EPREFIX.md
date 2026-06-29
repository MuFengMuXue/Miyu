Technical documentation on Gentoo Prefix

## Contents

-   [[1] [Changes to Portage]](#Changes_to_Portage)
    -   [[1.1] [Global]](#Global)
    -   [[1.2] [Search pathes]](#Search_pathes)
    -   [[1.3] [Technical state]](#Technical_state)
    -   [[1.4] [Repository state]](#Repository_state)
-   [[2] [Ebuild modifications]](#Ebuild_modifications)
    -   [[2.1] [EPREFIX variable]](#EPREFIX_variable)
    -   [[2.2] [The variables ED and EROOT]](#The_variables_ED_and_EROOT)
    -   [[2.3] [Using EPREFIX and EROOT]](#Using_EPREFIX_and_EROOT)
    -   [[2.4] [prefix.eclass]](#prefix.eclass)
    -   [[2.5] [Ebuild inter-revisions]](#Ebuild_inter-revisions)
-   [[3] [Gentoo Prefix tree developer policies]](#Gentoo_Prefix_tree_developer_policies)
    -   [[3.1] [Main tree migrations]](#Main_tree_migrations)

## [Changes to Portage]

### [Global]

What does Gentoo Prefix do more? For short, it allows to install packages into an offset, without root privileges. The longer answer includes how this is done, and why. To start with the latter one, let\'s see how the land of the package manager (Portage) looks like.

A package manager can be primary, or secondary. In the first case, the package manager is responsible for building the (core) system, while in the latter case, the package manager builds on top of an existing system to enhance it. Please note that this is by no means meant as a formal definition of the general concept \"package manager\". Within this document it is used as entity that is natively responsible for managing software packages on the OS it works on. Effectively, this means that Gentoo Portage is not the primary package manager on Mac OS X, Solaris, Debian, Ubuntu, etc. Gentoo Portage is the primary package manager on its Gentoo GNU/Linux distribution, and as such, the Gentoo repository matches this goal.

The Portage version we use in Gentoo Prefix is meant to be a secondary package manager. Therefore it doesn\'t require root privileges, and has to install into another place than [/], because there the primary package manager is already in charge.

This Portage version started as a set of patches by Michael Haubenwallner, that were finally applied to a new branch of portage development: Prefix. In this branch, initially managed by Brian Harring, then later by Kito Dietrich, lots of development made Prefix portage into what it is currently. Fabian Groffen did lots of work on getting the Portage sources usable for everyday Prefix use. Currently, the Prefix branch of the Gentoo repository benefits a lot from the efforts of Zac Medico to make Prefix a first class feature of Portage.

### [Search pathes]

Usage of the Gentoo Prefix consists of using everything from this prefix, before even looking at what the main operating system has installed. It simply changes the search paths such that the prefix comes first. Compilers and linkers installed by Portage in the prefix are configured such that they look into the prefix first as well. Not only that, but also does it make sure that compiled programs will keep on looking in the prefix via *rpath* directions. Programs compile and run using prefix provided tools and libraries.

In Linux-based Gentoo Prefix, glibc is also able to be installed and run from a prefix. For these systems, *rpath* is not needed. The runtime dynamic loader, shipped with Prefix glibc, looks into Prefix for dynamic libraries. The compiler is modified so that produced binary has dynamic loader field pointed to the one in Prefix. This approach makes Prefix more compatible with mainline Gentoo and lifts the burden of ebuild maintenance in Prefix. In addition, as glibc is installed from Gentoo portage tree, the host libc restrictions, like bugs or obsoleteness, are eliminated.

The differences between the approaches are summarized in this table.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------
                                                                                                                                                                                                                                                                                                                                                                                                      prefix-rpath (classic)                                                                         prefix-standalone (sysroot method)
  Feature name                                                                                                                                                                                                                                                                                                                                                                                        prefix-rpath                                                                                   prefix-standalone
  Linux profile                                                                                                                                                                                                                                                                                                                                                                                       prefix/linux                                                                                   prefix/linux-standalone
  Linux keyword                                                                                                                                                                                                                                                                                                                                                                                       \~ARCH-linux                                                                                   ARCH \~ARCH
  Portage                                                                                                                                                                                                                                                                                                                                                                                             [prefix.git](https://gitweb.gentoo.org/repo/proj/prefix.git)   [gentoo.git](https://gitweb.gentoo.org/repo/gentoo.git/)
  [[[sys-devel/gcc]](https://packages.gentoo.org/packages/sys-devel/gcc)[]]                                                                                                                                      EXTRA_ECONF+=(\--with-sysroot=\$EPREFIX) but do not pass \--sysroot to ld, prefix dynamic loader
  [[[sys-devel/binutils]](https://packages.gentoo.org/packages/sys-devel/binutils)[]]                                                                                                                       prefixify NATIVE_LIB_DIRS
  [[[sys-devel/binutils-config]](https://packages.gentoo.org/packages/sys-devel/binutils-config)[]]   inject -rpath and -R
  [[[sys-libs/glibc]](https://packages.gentoo.org/packages/sys-libs/glibc)[]]                                    No                                                                                             Yes prefixify hardcoded /etc,/usr,/var,/bin
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------

### [Technical state]

In Linux-based Gentoo Prefix, the `master` branch of portage is used.

The Portage version used in non-Linux-based Gentoo Prefix resides in the [prefix] branch of the main Portage git repository. Its sources can be inspected at [https://gitweb.gentoo.org/proj/portage.git/log/?id=refs/heads/prefix](https://gitweb.gentoo.org/proj/portage.git/log/?id=refs/heads/prefix). Currently, the Portage in this branch code is very close to the `master` branch in git. Patches made in `master` usually apply cleanly to the `prefix` branch. Hence, it is easy to keep the two synchronised using frequent merge operations.

### [Repository state]

In Linux-based Gentoo Prefix, the [Gentoo main repository](https://gitweb.gentoo.org/repo/gentoo.git/) is used.

In non-Linux-based Gentoo Prefix, since the [Gentoo main repository](https://gitweb.gentoo.org/repo/gentoo.git/) is not always compatible, an overlay has been created, which is currently hosted on [https://gitweb.gentoo.org/repo/proj/prefix.git](https://gitweb.gentoo.org/repo/proj/prefix.git). This overlay is really overlaid on the main Gentoo repository, and provided as such to Prefix users from the Prefix rsync mirror. Keeping the copied packages in the overlay synchronised with the main repository is facilitated by a script that is capable of applying the diffs with some intelligence between revisions. Also \"cross-diffs\", diffs between versions to create a new ebuild version, retaining as much changes as added in the previous version are implemented, keeping the maintenance overhead rather low.

## [Ebuild modifications]

### [EPREFIX variable]

Since Portage will install in an offset, called a \"prefix\", in some cases it might be necessary to directly handle with this offset. Some configure scripts for example require paths to be given next to `--prefix`, `--libdir`, etc. (all what `econf` covers), or some packages can\'t use `econf` at all. For those occasions the `EPREFIX` variable is available in ebuilds and eclasses, pointing to the root of the offset. For an offset [/home/user/gentoo] for example, the `EPREFIX` variable would contain [/home/user/gentoo]. This allows to easily use it for example like `econf --with-some-app="$"/usr/bin/some-app`.

### [The variables ED and EROOT]

In normal ebuilds, `$` refers to the destination directory in a temporary location before all files are actually merged into the live filesystem. Since in Gentoo Prefix `configure` is run with `--prefix=$/usr` in principle no changes are required. However, for all modifications to the build image, as is common practise in many ebuilds, `$$/` should be used. While this is a clean and logical result of using an offset, it increases the burden of \"porting\" ebuilds. For this purpose the variable `$` was introduced. It contains the value of `$$/` and functions as handy shortcut, which is easy to change. Usually, all but one occurrences of `$` in an ebuild (or eclass) have to be replaced by `$` to work properly in the prefix. Remember that when using `make DESTDIR="$" install` the `$` should in general *not* be changed, as configure was called with `--prefix="$"/usr`.

The variable `$` has for the same purpose a corresponding `$` which contains `$$/`. Often when `$` is being used, this can be replaced by `$` to add Gentoo Prefix support.

### [Using EPREFIX and EROOT]

Given that `$` is `$$/`, using `$` or `$` is defined by the following rule. The rule is simple and automatable, whether or not it is \"correct\", for Gentoo Prefix this rule always holds:

*If the main tree ebuild uses* `$` *, we respect* `$` *and usually use* `$` *, however if the main tree does not use* `$` *, we only add the offset,* `$` *.*

This rule basically means that you *never* add `$` yourself, if there isn\'t a `$` in the main tree ebuild. Repeating: whether or not that is \"correct\", for Gentoo Prefix this rule always holds. Rationale is simple: if it is a bug, it is a bug that should be fixed \"upstream\" (in the main repository), and that fix propagated to Gentoo Prefix. We don\'t want any extra differences between main repository and Gentoo Prefix, to keep maintenance and the amount of unrelated changes low.

### [prefix.eclass]

In some cases, the offset prefix needs to be hardcoded into files. Examples are shebangs with arguments or references to config files. The `prefix.eclass` provides the function `eprefixify`, which replaces each occurrence of `@GENTOO_PORTAGE_EPREFIX@` with the offset prefix as known by Portage. To use the eprefixify function on files (e.g. after patching), one needs to inherit the prefix eclass.

### [Ebuild inter-revisions]

** Note**\
This subsection **only** applies to the Prefix Overlay, not the main Gentoo Linux repository, and the use of inter-revisions is highly discouraged!

Gentoo Prefix ebuilds are currently merged from the main tree, and kept in sync. This process is half automated using scripts and in short takes differences from the main tree to apply them on the Prefix tree. This process insures that changes made to the Prefix tree are not lost, where it still is possible to merge most changes. For this to work, the ebuilds need to keep the same filename as in the main tree though. This way an ebuild in the Prefix tree can be compared to the same ebuild in the main tree. Since in Prefix also fixes need to be pushed to users, a revision of an ebuild cannot be simply bumped, since this would break synchronisation and result in collisions when the main tree does a revision bump too. For this purpose, *inter-revisions* have been implemented in Gentoo Prefix. They allow to specify a higher version to an ebuild, while maintaining the connection with the main tree. Inter-revisions are simple sub-revisions of main revisions, meaning that for every revision, a numbered sub-revision (inter-revision) version can exist. To make Portage distinguish normal and inter-revisions, the latter ones start with a 0 followed by the normal revision number. The inter-revision is added as dot and the number. An example inter-revision 2 of revision 3 would be `-r03.2`. Note that the inter-revision of a revision *less* ebuild is the inter-revision of revision 0. For example: `-r00.1`.

The effect of inter-revisions on Portage is that the sub-revision part is taken into account when comparing the versions. A normal revision has a sub-revision of 0, hence `-r01.1` is greater than `-r1`. This allows to bump a package in Prefix only. For the update scripts, however, the inter-revision is not taken into account. Hence, when an inter-revision ebuild is compared with the main tree, it is compared to the revision part only, thereby not breaking the connection between the Prefix tree and the main tree.

## [Gentoo Prefix tree developer policies]

### [Main tree migrations]

In principle, all ebuilds in the Gentoo Prefix tree are modified copies from their versions in the main tree, as used by Gentoo Linux. This means that each ebuild is copied and hence needs to be kept in sync with the main tree version. Since ebuilds in the Prefix tree all have manual modifications (those not automatically scriptable), the process of keeping the Prefix tree in sync with the main tree is not as straight forward as simply running a script. Instead, a complex script, `eupdate` is used to apply the differences made to an ebuild in the main tree, to the version in the Prefix tree. Also when new versions of ebuilds are added to the main tree, the `eupdate` script derives a new version in the Prefix tree, based on the differences between the latest two versions of the ebuilds in the main tree. This process is called a *cross-diff* . Both updating strategies may fail depending on modifications made to the ebuild in the Prefix tree. In 90% of the cases, both update strategies apply without problems, and semi-automatic propagation relies on that to currently merge changes from the main tree on a daily basis, with a limited investment of time on (manually) resolving the conflicts.

Mainly because manually resolving conflicts is a tedious job, the main policy in the Prefix tree with regard to modifications made to the main tree version is sound and simple: **avoid any change that is not strictly necessary**!. This boils down to the following concrete rules that need to be taken into account. Quoting of variables is a often confusing job. Underquoting results in problems when spaces are being used, overquoting is just unnecessary work. In many cases, the quoting of variables is done wrong in the main tree ebuilds, hence the problem is also carried over onto the Prefix tree. Fixing these quoting problems should *not* be done, unless this is necessary to solve a Prefix specific problem, which happens only in rare cases. Along the same line, adding or removing white space, indenting, rewriting to make more optimal in execution and similar changes which are not essentially necessary, should be avoided.

When changes need to be made, such as adding an `epatch` line, or adding a platform specific statement, such as an configure option, care needs to be taken to try to reduce the size of the differences introduced. The smaller the difference, the bigger the chance that semi-automatic updating succeeds without problems.

The good news is that Gentoo Prefix lives for a great deal in gx86, these days. Thus, the prefix overlay is being emptied, by migrating its packages to gx86. This requires contacting the gx86 maintainers and getting them to accept the changes necessary. Often, ebuilds in the prefix overlay need cleaning up, and reevaluation if hacks, patches and other changes are still necessary. Remember that many ebuilds have grown over years in the prefix overlay, and hence not necessarily are the cleanest solution. We aim not to add anything to our overlay any more, and move more and more towards acceptance in gx86. The migration progress is tracked by [[[bug #315803]](https://bugs.gentoo.org/show_bug.cgi?id=315803)[]].

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **[Fabian Groffen (grobian)](https://wiki.gentoo.org/wiki/User:Grobian "User:Grobian") **\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*