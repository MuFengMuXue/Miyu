Proxied maintainers and Gentoo developers are invited to work on this page and collect FAQ and common mistakes here. Please also see the [style guide](https://wiki.gentoo.org/wiki/Project:Proxy_Maintainers/User_Guide/Style_Guide "Project:Proxy Maintainers/User Guide/Style Guide").

## Contents

-   [[1] [Adding acct-/packages as a proxied maintainer]](#Adding_acct-.7Bgroup.2Cuser.7D.2Fpackages_as_a_proxied_maintainer)
-   [[2] [Breaking tests in parallel building mode]](#Breaking_tests_in_parallel_building_mode)
-   [[3] [\"Copy/paste\" style of contributions]](#.22Copy.2Fpaste.22_style_of_contributions)
-   [[4] [Handling an extra file which size exceeds 20 KiB]](#Handling_an_extra_file_which_size_exceeds_20_KiB)
-   [[5] [Keywording after EAPI bump]](#Keywording_after_EAPI_bump)
-   [[6] [Retiring from proxied maintainer status]](#Retiring_from_proxied_maintainer_status)
-   [[7] [Sorting of KEYWORDS]](#Sorting_of_KEYWORDS)
-   [[8] [Use the latest EAPI for a pull request]](#Use_the_latest_EAPI_for_a_pull_request)
-   [[9] [Using a sub-slot binder]](#Using_a_sub-slot_binder)
-   [[10] [When an ebuild needs a revbump (-r1)]](#When_an_ebuild_needs_a_revbump_.28-r1.29)
-   [[11] [When and how to stabilize a package?]](#When_and_how_to_stabilize_a_package.3F)

### []/packages_as_a_proxied_maintainer}[Adding acct-/packages as a proxied maintainer]

Check the latest state of [uid-gid.txt](https://gitweb.gentoo.org/data/api.git/tree/files/uid-gid.txt) file, and choose the first available number when counting downwards from 500. There\'s a helper script in [data/api.git], `./bin/ used_free_uidgids.sh` to aid with picking free numbers. Creating a pull request to api.gentoo.org reserving an ID is not necessary - if it\'s taken while your submission is being reviewed, new first available number will be assigned while merging your contribution.

### [Breaking tests in parallel building mode]

Tests after an ebuild has successfully finished the compile phase run in the same mode (environment). Individual (source-) files can be translated and compiled concurrently and independently from each other. However test-commands can fail when run in parallel!

Parallelism for the [**make** utility](https://www.gnu.org/software/make/) is handled via the [**-j or \--jobs Option to make**](https://www.gnu.org/software/make/manual/html_node/Parallel.html) i.e.: `MAKEOPTS`.

In those cases the tests and test-commands should be run with the **\--jobs** option explicitly set to **1** i.e.: `-j1`.

[CODE]

    src_test()

Alternatively:

[CODE]

    src_test()

Using the [**cmake.eclass**](https://devmanual.gentoo.org/eclass-reference/cmake.eclass/index.html) allows for a direct setting of the **\--jobs** Option `-j1`:

[CODE]

    # When cmake.eclass src_test function
      src_test()

### [][\"Copy/paste\" style of contributions]

If you commit new version bump and base your new ebuild on an old ebuild that uses old EAPI and has multiple modern QA issues, you are asked to update your new ebuild contribution to match today\'s Gentoo standards. However if you fix a bug on a current ebuild that requires a revbump and therefore a new ebuild copy, we will use common sense and accept the contribution to current ebuild revision.

Unfortunately ::gentoo tree is full of outdated ebuilds by modern standards. You can read the [devmanual](https://devmanual.gentoo.org/) and [QA Policy Guide](https://projects.gentoo.org/qa/policy-guide/), in addition to EAPI [6](https://blogs.gentoo.org/mgorny/2015/11/13/the-ultimate-guide-to-eapi-6/) & [7](https://dev.gentoo.org/~mgorny/articles/the-ultimate-guide-to-eapi-7.html) guides if unsure about state of the current ebuild you\'re working on.

### [Handling an extra file which size exceeds 20 KiB]

Per [devmanual](https://devmanual.gentoo.org/ebuild-maintenance/new-ebuild/index.html) a file inside `$` mustn\'t exceed the file size of 20 KiB. These files get synced to everyone, yet not many users necessarily need them. They influence the overall size of portage tree, and worldwide bandwith caps.

You can host a file exceeding 20 KiB in your Github, Gitlab etc hosting service, add it to `SRC_URI` and call either `PATCHES=( "$/$-fix-qt-5.15-headers.patch" )` or `eapply "$/$-fix-qt-5.15-headers.patch"`. This is flagged by the [[[dev-util/pkgcheck]](https://packages.gentoo.org/packages/dev-util/pkgcheck)[]] tool.

### [Keywording after EAPI bump]

An EAPI bump requires usually that all keywords are set to \`\~\` (unstable). This can be done with:

`user `[`$`]`ekeyword ~all foo-2.0.ebuild`

From the package [[[app-portage/gentoolkit]](https://packages.gentoo.org/packages/app-portage/gentoolkit)[]].

However there are some special cases where a stabilization can remain, if the developer can be 100% sure, that the EAPI change does not change anything. But this is not the case for usual packages.

### [Retiring from proxied maintainer status]

We get it, sometimes life happens, distro hop happens. If you have packages assigned to you and you wish to stop being a proxied maintainer for them, please open a pull request where you update metadata.xml files putting maintainer status to `<!-- maintainer-needed -->`, using a `Closes:` tag against your proxy-maint bug, and sending a [\"packages up for grabs\" e-mail to gentoo-dev mailing list](https://archives.gentoo.org/gentoo-dev/message/fc7652e75cbb7ee0c2a7e72de91acc04).

Or at least please inform us by messaging your updated status in your proxy-maint bug, and we will do the rest for you.

### [Sorting of KEYWORDS]

We usually sort the `KEYWORDS` values as ekeyword does. This makes comparison between packages easier. Simply run ekeyword on the ebuild to let it sort.

`user `[`$`]` ekeyword foo-2.0.ebuild`

### [Use the latest EAPI for a pull request]

We always try to use the latest EAPI if possible. If a required eclass is not yet compatible with the latest EAPI this can not be fulfilled directly.

### [Using a sub-slot binder]

[Refer to devmanual](https://devmanual.gentoo.org/general-concepts/slotting/index.html#Sub-Slots) in case sub-slots are not familiar to you. Sub-slot binders should only be used when your program links to specific SONAME of a library during build-time. It can be used even if the dependency doesn\'t have a subslot already defined, as long as your program properly links to a library.

### [][When an ebuild needs a revbump (-r1)]

Refer to the [devmanual](https://devmanual.gentoo.org/general-concepts/ebuild-revisions/index.html).

### [][When and how to stabilize a package?]

[Common rules for stabilization](https://wiki.gentoo.org/wiki/Stable_request "Stable request"). If you don\'t want to keep a calendar and count days for stabilization, [[[dev-util/pkgcheck]](https://packages.gentoo.org/packages/dev-util/pkgcheck)[]] tool can be utilized to help.

`user `[`$`]`pkgcheck scan app-emulation/lxd dev-libs/efl dev-python/python-efl media-libs/rlottie -c StableRequestCheck`

    app-emulation/lxd
      StableRequest: version 4.0.1: slot(0) no change in 30 days for unstable keyword: [ ~amd64 ]

    dev-python/python-efl
      StableRequest: version 1.24.0: slot(0) no change in 45 days for unstable keywords: [ ~amd64, ~x86 ]

Stabilization is [requested through bugzilla](https://wiki.gentoo.org/wiki/Bugzilla/Bug_report_guide#Request_stabilization "Bugzilla/Bug report guide") which uses [nattka tool](https://github.com/mgorny/nattka/#filing-keywordingstabilization-bugs) for its syntax. If nattka informs that sanity check succeeds, sit back and relax, arch teams will handle the stabilization next. If sanity check doesn\'t succeed, most likely some required dep is [not stabilized/keyworded](https://devmanual.gentoo.org/keywording/index.html#equal-visibility-requirement) yet, and you will either need to handle it in a new bug, or add it to package list.