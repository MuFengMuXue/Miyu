[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Regenworld&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Portage "Project:Portage")][Project](https://wiki.gentoo.org/wiki/Project:Portage "Project:Portage")

The [regenworld] script, which is distributed with [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"), regenerates the Portage world file by checking the Portage log file for all actions performed in the past. It ignores any arguments except the `--help` option.

## [Usage]

### [Invocation]

** Warning**\
It is highly recommended a backup of the system\'s existing world file ([/var/lib/portage/world]) be created before using the [regenworld] script! Run the following command to create a backup:

`root `[`#`]`cp /var/lib/portage/world /var/lib/portage/world.bak`

`root `[`#`]`regenworld --help`

    This script regenerates the portage world file by checking the portage
    logfile for all actions that you've done in the past. It ignores any
    arguments except --help. It is recommended that you make a backup of
    your existing world file (/var/lib/portage/world) before using this tool.