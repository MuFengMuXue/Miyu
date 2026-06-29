This page contains [[changes](https://wiki.gentoo.org/index.php?title=Bugzilla/Bug_report_guide&oldid=1271862&diff=1425547)] which are not marked for translation.

Other languages:

-   [English]
-   [italiano](https://wiki.gentoo.org/wiki/Bugzilla/Bug_report_guide/it "Bugzilla/Guida ai rapporti dei Bug (62% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Bugzilla/Bug_report_guide/hu "Bugzilla/Hibabejelentés útmutatója (100% translated)")
-   [čeština](https://wiki.gentoo.org/wiki/Bugzilla/Bug_report_guide/cs "Bugzilla/Bug report guide/cs (6% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Bugzilla/Bug_report_guide/ru "Bugzilla/Bug report guide/ru (45% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Bugzilla/Bug_report_guide/zh-cn "Bugzilla/漏洞报告指南 (34% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Bugzilla/Bug_report_guide/ja "Bugzilla/バグ報告ガイド (55% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Bugzilla/Bug_report_guide/ko "Bugzilla/Bug report guide/ko (47% translated)")

This article explains how to report bugs using Gentoo\'s Bugzilla instance, which may be lightly customized to collect specific details for each Gentoo project area.

See [Bugzilla/Guide](https://wiki.gentoo.org/wiki/Bugzilla/Guide "Bugzilla/Guide") for the recommended method of forensically troubleshooting and reporting helpful details on bugs related to Gentoo development.

## Contents

-   [[1] [Best practices]](#Best_practices)
-   [[2] [Gentoo Linux: Ebuilds (packages)]](#Gentoo_Linux:_Ebuilds_.28packages.29)
    -   [[2.1] [Report a build-time bug (emerge failed)]](#Report_a_build-time_bug_.28emerge_failed.29)
    -   [[2.2] [Report a run-time bug]](#Report_a_run-time_bug)
    -   [[2.3] [Report a version bump; a newer upstream release is available since a while]](#Report_a_version_bump.3B_a_newer_upstream_release_is_available_since_a_while)
        -   [[2.3.1] [Optional]](#Optional)
    -   [[2.4] [Request for a new package; ebuild request]](#Request_for_a_new_package.3B_ebuild_request)
    -   [[2.5] [Request stabilization]](#Request_stabilization)
    -   [[2.6] [Requesting Keywords]](#Requesting_Keywords)
-   [[3] [Kernel]](#Kernel)
-   [[4] [Supplemental information for bug reports]](#Supplemental_information_for_bug_reports)
-   [[5] [Trackers]](#Trackers)
-   [[6] [See also]](#See_also)
-   [[7] [External references]](#External_references)

## [Best practices]

-   **Reread the text before submission**, the text cannot be edited afterwards. Also any text entered into a bug report will be usually e-mailed immediately to many people. Write in precise and clean language and avoid colloquial speech. **Hint:** Imagine you have **only one chance in your life** to write this very important bug report. You know that the recipient can read English, but it is not their native language.

<!-- -->

-   **Search for duplicates**, before creating a new bug.

<!-- -->

-   **Stay on topic** - A bug ticket is used for technical reports and chitchat should be avoided. Keep discussions in the [support channels](https://www.gentoo.org/support/) (forums, IRC or mailing lists).
-   **Confirm the existence of a problem only once.** - It does not help solving the problem, if you and another person report it twice. But if your and the confirmer\'s systems differ in an obvious way and that would be helpful to know, add this information.
-   **Open one bug ticket per topic** - Usually this means no more than one package and one bug per ticket. If your problem is not discussed in a bug, search for one related to your issue or create a new report. Do not hijack bugs.
-   **No talk on TRACKER bugs.** - Those bugs are meta bugs. If you want to add useful information, add them to a related sub bug or create a new bug.
-   Optional: [Gentoo consultants](https://wiki.gentoo.org/wiki/Foundation:Consultants "Foundation:Consultants") provide also **commercial support** for bugs and ebuilds.
-   [Attach the logs to the bug ticket](https://wiki.gentoo.org/wiki/Attach_the_logs_to_the_bug_ticket "Attach the logs to the bug ticket") if the ticket is about problems during runtime or installation.

## [][Gentoo Linux: Ebuilds (packages)]

You should always add information about your system configuration to the bug. To do so, create a new attachment and paste the contents of:

`user `[`$`]`emerge --info > /tmp/emerge--info.txt`

### [][Report a build-time bug (emerge failed)]

[![](/images/thumb/2/21/Bugzilla_screenshot_summary-keyword.png/300px-Bugzilla_screenshot_summary-keyword.png)](https://wiki.gentoo.org/wiki/File:Bugzilla_screenshot_summary-keyword.png)

[](https://wiki.gentoo.org/wiki/File:Bugzilla_screenshot_summary-keyword.png "Enlarge")

Use the **Add an attachment** button below the description text box in order to attach files in bugzilla.

-   First write the exact version of the package in the title of the bug report e.g. *sys-apps/package-2.3-r4*
-   Add a short description to the title.
-   **[Attach the logs to the bug ticket](https://wiki.gentoo.org/wiki/Attach_the_logs_to_the_bug_ticket "Attach the logs to the bug ticket")**

### [Report a run-time bug]

Files and information of interest ordered by priority:

-   The exact version of the package in the title of the bug report e.g. *sys-apps/package-2.3-r4 crashes with error: Cannot proceed\...*
-   Description of the problem, so that other can reproduce it:
    -   How is the program run (on the console, in a terminal, as a daemon, in which init runlevel etc.)
    -   Any error output
    -   What makes the program crash, behave wrong, not start
    -   Is there a workaround?
    -   What was the last working version of the package, if any?
    -   What changed to make it not work?
-   **[Attach the logs to the bug ticket](https://wiki.gentoo.org/wiki/Attach_the_logs_to_the_bug_ticket "Attach the logs to the bug ticket")**

### [][Report a version bump; a newer upstream release is available since a while]

-   Search Bugzilla before posting a bump request - is there already a bug open? **Has the local Portage tree been synced lately**; is it already in Portage?
-   Avoid [zero-day bump requests](https://wiki.gentoo.org/wiki/Zero-day_bump_requests "Zero-day bump requests") (wait at least **48 hours** after the release announcement)
-   Has it actually been **released** by upstream sources, **or is it just marked** in the source tree? Some projects mark a release in the tree a long time before it is officially released.
-   Be sure to **mention if it compiles and runs well on your arch**. Any other helpful information you can provide is most welcome.
-   Add a link to the upstream website if there is an announcement or release notes.
-   Give a link or list of fixed bugs or new features (sometimes called **changelog**)
-   Write a **summary** in the form *app-editors/vim-12.3.5: version bump*

#### [Optional]

-   Does a simple copy work, or does the ebuild need changes? (changed dependencies, obsolete patch files, compared build system changes, read release notes carefully)
-   [Test the ebuild](https://wiki.gentoo.org/wiki/Package_testing "Package testing") in a local repository before submitting attachments
-   Provide patches for proposed ebuild edits, with ideally some explanation of changes (file name should match the new version number, not old)
-   Provide additional files (OpenRC init scripts, systemd unit files) as separate attachments (as needed)
-   Do not paste files directly into comments; [use attachments.](https://wiki.gentoo.org/wiki/Attach_the_logs_to_the_bug_ticket "Attach the logs to the bug ticket")

### [][Request for a new package; ebuild request]

If you request a new ebuild for a software to be added to the Gentoo repository, you must find or become a maintainer for the package.

If a bug report already exists for the package, you can help the effort by keeping information about the package up to date. If you add a -VERSION component to the package atom in the summary/title, then this can be updated with new releases over time while the bug report remains open to show there is a continuing interest in seeing it integrated into the Gentoo repository.

If no bug report exists for the prospective new package, you can file a bug report under the **Gentoo Linux** project and the component **New package**.

The **Summary** of your bug report should list a (preliminary) package atom *category/package*, perhaps with a *-VERSION* suffix, followed by a canonical short description of the package (the DESCRIPTION variable in an ebuild). It is important to disambiguate the name of the new package: if upstream uses different names for the same software, perhaps an abbreviation as well as the full name, you should mention both (all) of these in the Summary so that other people can find bug reports about the same software. If several (groups of) people track different bug reports about virtually the same ebuild request, this will duplicate the effort of ebuild research and development, and will divide people who have a common interest.

You should link to the upstream website (the HOMEPAGE variable in an ebuild) using the **URL** field. You should provide a list of features in the **Description** of the bug report. This may well be taken directly from the upstream website or from a manual or other documentation, and could be used later for the *longdescription* tag in metadata.xml.

You can attach an ebuild and related files that should go into the Gentoo repository directly to the bug report, or you can use the **See also** field to refer to a git [pull request](https://wiki.gentoo.org/wiki/Github_Pull_Requests "Github Pull Requests").

You can help develop the package by setting up a [local repository](https://wiki.gentoo.org/wiki/Creating_an_ebuild_repository "Creating an ebuild repository") with your ebuilds, metadata, patches and other auxiliary files. If you need technical support with your ebuild development, many people would be glad to [help](https://www.gentoo.org/support/).

### [Request stabilization]

** Tip**\
For developers, the [devmanual](https://devmanual.gentoo.org/keywording/index.html#moving-from-arch-to-arch) has more extensive information on stable requests.

A bug ticket can be used for a [stable request](https://wiki.gentoo.org/wiki/Stable_request "Stable request").

Everybody can request a stabilization. **Users do not need to worry about filling all fields or details in the bug.** The maintainer (or Proxied Maintainer) will CC the arches by adding **CC-ARCHES** to the *Keywords* field on the bug when appropriate.

A stable request can be filed either using the [pkgdev](https://wiki.gentoo.org/wiki/Pkgdev "Pkgdev") utility, or manually.

For the [pkgdev bugs] route:

`user `[`$`]`pkgdev bugs -s =dev-java/bndlib-7.0.0`

```
Checking =dev-java/bndlib-7.0.0 on 'amd64 arm64 ppc64'
Checking =dev-java/bnd-annotation-7.0.0 on 'amd64 arm64 ppc64'
Checking =dev-java/bnd-util-7.0.0 on 'amd64 arm64 ppc64'
Checking =dev-java/libg-7.0.0 on 'amd64 arm64 ppc64'
Checking =dev-java/osgi-service-log-1.3.0 on 'amd64 arm64 ppc64'
Merging =dev-java/bnd-util-7.0.0 into =dev-java/bndlib-7.0.0
Merging =dev-java/osgi-service-log-1.3.0 into =dev-java/bndlib-7.0.0, =dev-java/bnd-util-7.0.0
```

Eventually an [API key](https://bugs.gentoo.org/userprefs.cgi?tab=apikey) needs to be copied to [\~/.bugz_token].

To request stabilization of a package manually, [file a new bug](https://bugs.gentoo.org/enter_bug.cgi?product=Gentoo%20Linux) under the `Stabilization` component taking care to complete two special [bug fields](https://bugs.gentoo.org/page.cgi?id=fields.html):

-   `Package list` - a fully qualified package per line, optionally followed by a space-delimited list of architectures to target. Formerly, this field was called `Atoms to stabilize` and contained fully qualified atoms, which is also still supported. [Nattka](https://wiki.gentoo.org/wiki/Nattka "Nattka") can be used with `make-package-list` to generate the appropriate format for this field. Architectures should no longer be manually added to the `CC` field.
-   `Runtime testing required` - see [https://bugs.gentoo.org/page.cgi?id=fields.html#cf_runtime_testing_required](https://bugs.gentoo.org/page.cgi?id=fields.html#cf_runtime_testing_required)

Examples:

+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Summary                           | foo-libs/libbar-1.2.3 stabilization request                                                                                                                                                                |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Runtime testing required          | No                                                                                                                                                                                                         |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Package list                      | foo-libs/libbar-1.2.3 (*old syntax, still supported:* =foo-libs/libbar-1.2.3)                                                                                                                              |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Explanation                       | -   foo-libs/libbar-1.2.3 will be stabilized for **[amd64]** and **[x86]** |
|                                   | -   Build and tests passing is sufficient to stabilize                                                                                                                                                     |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Summary                           | app-foo/bar-1.2.3 and app-foo/baz-4.5.6 stabilization request                                                                                                                                                                                                                      |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Runtime testing required          | Yes                                                                                                                                                                                                                                                                                |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Package list                      | app-foo/bar-1.2.3                                                                                                                                                                                                                                                                  |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                   | app-foo/baz-4.5.6 amd64 x86                                                                                                                                                                                                                                                        |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Explanation                       | -   app-foo/bar-1.2.3 will be stabilized for **[amd64]**, **[arm]**, and **[x86]** |
|                                   | -   app-foo/baz-4.5.6 will be stabilized for **[amd64]**, and **[x86]**                                                                            |
|                                   | -   It is requested additional runtime testing of the package is performed after it is merged                                                                                                                                                                                      |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

### [Requesting Keywords]

** Important**\
Before submitting keyword requests for every package that is not keyworded for an arch, please consider if there is a need for the package to be keyworded. If it is not already keyworded then it can stem from a range of reasons: lack of interest, obtuse compile errors, tests failing, or the maintainer simply does not wish to keyword it. This is not meant to discourage keyword requests, but merely to ask users to be mindful of the packages they are requesting keywords for and to consider if it is warranted.

A bug ticket can be used for a keyword request.

As with [request stabilization](https://wiki.gentoo.org/wiki/Bugzilla/Bug_report_guide#Request_stabilization "Bugzilla/Bug report guide"), everybody can request a keyword. **Users do not need to worry about filling all fields or details in the bug.** The maintainer (or Proxied Maintainer) will CC the arches by adding **CC-ARCHES** to the *Keywords* field on the bug when appropriate.

\
To request a new keyword for a package, [file a new bug](https://bugs.gentoo.org/enter_bug.cgi?product=Gentoo%20Linux) under the `Keywording` component taking care to complete two special [bug fields](https://bugs.gentoo.org/page.cgi?id=fields.html):

-   `Package list` - a fully qualified package per line, optionally followed by a space-delimited list of architectures to target. If no architecture list is provided, all architectures in `CC` are assumed. Formerly, this field was called `Atoms to stabilize` and contained fully qualified atoms, which is also still supported.
-   `Runtime testing required` - indicates if additional runtime testing should be performed beyond build and tests passing. If *undefined* the arch tester should use their best judgement

+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Summary                           | foo-libs/libbar-1.2.3: add \~ppc keyword                                                                                    |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Runtime testing required          | No                                                                                                                          |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Package list                      | foo-libs/libbar-1.2.3 \~ppc (*old syntax, still supported:* =foo-libs/libbar-1.2.3)                                         |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Explanation                       | -   foo-libs/libbar-1.2.3 will be keyworded for **[\~ppc]** |
|                                   | -   Build and tests passing is sufficient to keyword                                                                        |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------+

## [Kernel]

Files and information of interest for kernel bug reports ordered by priority:

-   Which kernel and version is used, on what architecture e.g. *gentoo-sources-3.4.2-r2* on *x86_64*
-   The kernel configuration file should be attached to the bug report ([/usr/src/linux/.config])
-   A list of all devices in the system can be acquired with *lspci -k*
-   Log files during kernel initialization should be attached ([/var/log/dmesg] or [/var/log/messages])

** Note**\
On request a [kernel git-bisect](https://wiki.gentoo.org/wiki/Kernel_git-bisect "Kernel git-bisect") could be done to identify bad patches.

## [Supplemental information for bug reports]

  --------------------------------- ----------------------- --------------------------------------------------------------------------------------------------------------------------------------------------
  Information                       When needed             How to collect
  `SRC_URI` reachable?   download failed         [GENTOO_MIRRORS=\"\" ebuild foo-1.2.ebuild fetch]
  OpenGL version                    Games with OpenGL       [glxinfo -B]
  Linked libraries                  Dependency is missing   Add missing dependency, compile, check with [lddtree]
  --------------------------------- ----------------------- --------------------------------------------------------------------------------------------------------------------------------------------------

## [Trackers]

Tracker bugs are virtual or meta bugs to cluster bugs with the same topic or focus area:

-   [Active tracker bugs](https://bugs.gentoo.org/buglist.cgi?cmdtype=runnamed&list_id=6064741&namedcmd=active%20TRACKER)

## [See also]

-   [Attach the logs to the bug ticket](https://wiki.gentoo.org/wiki/Attach_the_logs_to_the_bug_ticket "Attach the logs to the bug ticket") --- explains how to **attach log files to a bug ticket**
-   [Bugzilla/Guide](https://wiki.gentoo.org/wiki/Bugzilla/Guide "Bugzilla/Guide") --- covers the recommended method of forensically reporting *specific details* of bugs within Gentoo.
-   [Contributing to Gentoo](https://wiki.gentoo.org/wiki/Contributing_to_Gentoo "Contributing to Gentoo") --- explains how users can **contribute to the development of Gentoo**
-   [Support](https://wiki.gentoo.org/wiki/Support "Support") --- provide **support** for technical issues encountered when installing or using Gentoo Linux
-   [Troubleshooting](https://wiki.gentoo.org/wiki/Troubleshooting "Troubleshooting") --- provide users with a set of techniques and tools to troubleshoot and fix problems with their Gentoo setups.

## [External references]

-   [Gentoo\'s Bugzilla site](https://bugs.gentoo.org/)