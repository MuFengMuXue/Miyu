[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Darcs&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://darcs.net)

[[]][Official documentation](https://darcs.net/Using)

[[]][Package information](https://packages.gentoo.org/packages/dev-vcs/darcs)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Darcs "wikipedia:Darcs")

[[]][[#darcs](ircs://irc.libera.chat/#darcs)] ([[webchat](https://web.libera.chat/#darcs)])

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/darcs)

**Darcs** (**[darcs]** is a distributed version control system created by David Roundy. Contrary to other systems like git that are snapshot-based, Darcs is patched-based. As such, a repository can be seen as a set of patches, where each patch is not necessarily ordered with respect to other patches.

\

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [Tips]](#Tips)
-   [[5] [Troubleshooting]](#Troubleshooting)
-   [[6] [Removal]](#Removal)
    -   [[6.1] [Unmerge]](#Unmerge)
-   [[7] [See Also]](#See_Also)

## [Installation]

### [Emerge]

`root `[`#`]`emerge --ask dev-vcs/darcs`

## [Configuration]

### [Files]

## [Usage]

### [Invocation]

## [Tips]

## [Troubleshooting]

Darcs is case-insentive by default so it will refuse to add a file that has it case changed. This can be solved with

`user `[`$`]`darcs add --case-ok`

Beware that it can lead to strange behaviours on case-insentivie filesystems (like [Windows](https://learn.microsoft.com/en-us/windows/wsl/case-sensitivity)).

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose dev-vcs/darcs`

## [See Also]

-   [Git](https://wiki.gentoo.org/wiki/Git "Git") --- widely used, open source, distributed [version control system](https://wiki.gentoo.org/wiki/Version_control_systems "Version control systems")
-   [Subversion](https://wiki.gentoo.org/index.php?title=Subversion&action=edit&redlink=1 "Subversion (page does not exist)")