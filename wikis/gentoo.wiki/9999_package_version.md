Live ebuilds are ebuilds with a version number of 9999. These ebuilds fetch updates directly from the upstream project\'s source code repository and will build the associated package from the latest commit.

** Warning**\
There are **serious risks** when using live ebuilds. They should only be used in exceptional circumstances, and with caution.

-   A live ebuild could potentially install malicious code if its repository has been compromised.
-   The \'version\' used by a live ebuild could change from one minute to the next, and may not even build or work.

Live ebuilds are *extremely* unstable, remove at least two layers of defence against malicious code, and therefore are [always] keyword masked. In general, only unmask a particular live ebuild if instructed by a Gentoo developer, or someone known to be trustworthy.

## Contents

-   [[1] [Live ebuilds are different than regular ebuilds]](#Live_ebuilds_are_different_than_regular_ebuilds)
-   [[2] [Unmasking live ebuilds]](#Unmasking_live_ebuilds)
    -   [[2.1] [A single package]](#A_single_package)
    -   [[2.2] [System wide]](#System_wide)
-   [[3] [Updating live packages]](#Updating_live_packages)
    -   [[3.1] [Smart live rebuild]](#Smart_live_rebuild)
-   [[4] [See also]](#See_also)

## [Live ebuilds are different than regular ebuilds]

Most Gentoo systems are built entirely from **versioned** ebuilds, which build **one specific version** of a package. This is one meaning of the word *stable*: unchanging and predictable results (USE flags not withstanding) from a single ebuild.

Conversely, a *live* ebuild has a fake version number of 9999. Instead of building from a specific version, it always fetches the very latest source (sometimes called *tip of tree*) from the package\'s upstream repository. This version could change from one minute to the next, depending on activity within the upstream project.

This is what the above warning means by \"extremely unstable\": not necessarily buggy or broken, but **unpredictable**. Because it is impossible to know the state of the build ahead of time, a live ebuild can\'t be *tested* in the same way a versioned ebuild is tested.

For example, the upstream project may make a change which requires a different version of one of its dependencies, or a new dependency altogether. If the maintainer of the Gentoo ebuild has not yet had a chance to reflect this change in the ebuild, there will likely be problems with building or running the package.

As noted below, packages installed from live ebuilds are not routinely updated with [emerge \--update]

For these reasons, using live ebuilds should be done with careful consideration of the ramifications, or used when advised by someone who has made these considerations.

## [Unmasking live ebuilds]

### [A single package]

Live builds will require manual unmasking in order to be installed by the package manager. For example, to unmask the live version of [[[app-emulation/wine-staging]](https://packages.gentoo.org/packages/app-emulation/wine-staging)[]], the following

[FILE] **`/etc/portage/package.accept_keywords`Unmasking a single live ebuilds**

    # Note: Accepting all keywords removes all levels of quality assurance from the system
    # and is likely to result in build failures, unstable software, or other problems.
    # Here be dragons! Proceed keeping these risks in mind...
    app-emulation/wine-staging **

### [System wide]

While possible to set system wide, there is very little to gain from doing so, as even the bug reports produced have so many unknown quirks that it makes them unreliable.

Consider this as a banned practice in Gentoo.

## [Updating live packages]

All presently installed live packages can be updated by re-installing via the \@live-rebuild set. This is a crude and effective approach, since Portage will re-pull and then recompile each of the packages in the set, which take a considerable amount of time.

`root `[`#`]`emerge --ask @live-rebuild`

** Important**\
The package manager will *not* automatically update packages with a version number of 9999, since they are already considered to be at their maximum version. Running [emerge \--update \@live-rebuild] will perform no action, which is why the set is simply re-installed in the example above.

### [Smart live rebuild]

The [[[app-portage/smart-live-rebuild]](https://packages.gentoo.org/packages/app-portage/smart-live-rebuild)[]] package provides a framework which will intelligently *pull* updates from each upstream source code repository for each live package installed on the system. It will only update packages which have a newer set of changes available upstream, therefore avoiding the crude approach of having to recompile all packages within the \@live-rebuild set.

## [See also]

-   [/etc/portage/package.accept_keywords](https://wiki.gentoo.org/wiki//etc/portage/package.accept_keywords "/etc/portage/package.accept keywords") --- files or directories of files containing definitions for per-package `ACCEPT_KEYWORDS` statements.
-   [ACCEPT_KEYWORDS](https://wiki.gentoo.org/wiki/ACCEPT_KEYWORDS "ACCEPT KEYWORDS")
-   [Bisecting_with_live_ebuilds](https://wiki.gentoo.org/wiki/Bisecting_with_live_ebuilds "Bisecting with live ebuilds") --- Using live ebuilds and [git bisect] can be enormously helpful for debugging issues.