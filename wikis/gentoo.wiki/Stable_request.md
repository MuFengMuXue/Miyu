This article describes the procedure for moving an ebuild from testing to stable.

** Tip**\
Users should request stabilization from the maintainers of a package if it is working well and has been in tree long enough. Stabilization, especially first-time instances, only occurs when a need arises or a request is made.

** Warning**\
Users should **not** manually CC arch teams. Users should let the maintainer handle that in case they want to use a different version or it is not ready.

## Contents

-   [[1] [Invocation]](#Invocation)
-   [[2] [Checklist for a stabilization request]](#Checklist_for_a_stabilization_request)
-   [[3] [Responsibility]](#Responsibility)
-   [[4] [Requesting stabilization]](#Requesting_stabilization)
-   [[5] [Sanity check]](#Sanity_check)
-   [[6] [Simultaneous stabilization on all architectures]](#Simultaneous_stabilization_on_all_architectures)
-   [[7] [See also]](#See_also)
-   [[8] [External resources]](#External_resources)

## [Invocation]

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

## [Checklist for a stabilization request]

** Important**\
Users only need to ensure the package works correctly for them and has ideally been in the tree for \~30 days. Developers will handle the rest. Checking more is just a nice bonus.

The requirements for stabilization can be found in the [Section Keywording of the Developer Manual](https://devmanual.gentoo.org/keywording/index.html). Go through this checklist before opening a new stabilization request.

-   Live ebuilds (-9999) cannot be stabilized
-   See [KEYWORDS](https://wiki.gentoo.org/wiki/KEYWORDS "KEYWORDS") for more information on stable/unstable branch
-   Did you test the version you want to become stable thoroughly?
-   Do tests pass? (`FEATURES=test`) (not necessary to check as a user)
-   Are there other bug reports regarding this package (focus on regressions)?
-   Is the ebuild older than **30 days** (sooner for security issues or serious regressions)?
-   Are its dependencies all marked stable? (This can be handled in the same bug)
-   The stabilization requires developer time. Until we have automatic stabilization it makes sense to limit stabilization requests to ebuilds which benefit somehow from a stabilization.

## [Responsibility]

The primary purpose of the stabilization process is to ensure an [ebuild](https://wiki.gentoo.org/wiki/Ebuild "Ebuild") is ready for all users in the [official Gentoo ebuild repository](https://gitweb.gentoo.org/repo/gentoo.git/tree/). This can involve maintaining the consistency of the dependency graph, basic compatibility checks with other packages, and smoke testing of the package itself.

Stabilization is not intended to relieve a package maintainer of their responsibility to ship a quality package - the primary responsibility of ensuring that a package is a good stable candidate remains with the person approving the stabilization request. The stabilization process does not include more than basic functionality checks unless explicitly requested.

## [Requesting stabilization]

Everybody can request stabilization by means of a [stabilization bug ticket](https://wiki.gentoo.org/wiki/Bugzilla/Bug_report_guide#Request_stabilization "Bugzilla/Bug report guide"). Please request stabilization if a package you use and enjoy is not marked stable.

## [Sanity check]

Periodically [NATTkA](https://wiki.gentoo.org/wiki/Nattka "Nattka") will review stabilization requests for completeness and complain if there are invalid or missing atoms, setting a `sanity-check+` or `sanity-check-` flag as appropriate. This allows arch team members to filter out requests that are not known-good if they wish. A series of architecture-specific [saved searches](https://bugs.gentoo.org/userprefs.cgi?tab=saved-searches) are available for convenience.

## [Simultaneous stabilization on all architectures]

** Important**\
Developers [should](https://devmanual.gentoo.org/keywording/#simultaneous-stabilization-on-all-architectures) add `<stabilize-allarches>` to metadata.xml to ensure consistency.

Maintainers of architecture-independent packages (data files, icons, pure Perl,\...) may request that the package is stabilized on all arches at once. When filing the stabilization bug please add the keyword `ALLARCHES` in addition and CC the arches.

`ALLARCHES` advises the arch teams to stabilize all CCed arches, if their tests for a single arch succeeded.

## [See also]

-   [Package testing](https://wiki.gentoo.org/wiki/Package_testing "Package testing") - An article describing how to configure a Gentoo system for testing ebuilds.
-   [Bugzilla/Bug report guide#Request_stabilization](https://wiki.gentoo.org/wiki/Bugzilla/Bug_report_guide#Request_stabilization "Bugzilla/Bug report guide")
-   [Devmanual/Keywording](https://devmanual.gentoo.org/keywording/)

## [External resources]

-   [https://bugs.gentoo.org/userprefs.cgi?tab=apikey](https://bugs.gentoo.org/userprefs.cgi?tab=apikey)
-   [https://github.com/mgorny/nattka/#filing-keywordingstabilization-bugs](https://github.com/mgorny/nattka/#filing-keywordingstabilization-bugs)
-   [https://devmanual.gentoo.org/keywording/#moving-from-arch-to-arch](https://devmanual.gentoo.org/keywording/#moving-from-arch-to-arch)