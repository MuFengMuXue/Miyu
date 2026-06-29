[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Troubleshooting_parallel_builds&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines") (no intro to explain what article is about). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

## Contents

-   [[1] [Parallel build fails, because the build system needs to work sequentially]](#Parallel_build_fails.2C_because_the_build_system_needs_to_work_sequentially)
    -   [[1.1] [Parallel build fails in src_compile]](#Parallel_build_fails_in_src_compile)
    -   [[1.2] [Workaround for the user]](#Workaround_for_the_user)
    -   [[1.3] [Resources]](#Resources)

## [][Parallel build fails, because the build system needs to work sequentially]

### [Parallel build fails in src_compile]

-   Please report the bug upstream, if upstream is still active, as it was done for example in [[[bug #482542]](https://bugs.gentoo.org/show_bug.cgi?id=482542)[]].
-   Please add comment with a bug id, so that others know the reason for the workaround. For example:

[CODE] **Typical workaround in a compile section**

    export MAKEOPTS=-j1 #660754

-   GNU make 4.4 and newer now supports [\--shuffle]. It will also report the shuffle seed used which allows reproducing build failures.

### [Workaround for the user]

The broken package entitled \"foo\" can still be installed with the following workaround:

`root `[`#`]`MAKEOPTS="-j1" emerge app-misc/foo`

### [Resources]

-   Tracker [[[bug #351559]](https://bugs.gentoo.org/show_bug.cgi?id=351559)[]]