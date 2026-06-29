[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=PRoot&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://proot-me.github.io)

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/proot)

[[]][GitHub](https://github.com/proot-me/PRoot)

[[]][Bugs (upstream)](https://github.com/proot-me/proot/issues)

PRoot is a user-space implementation of chroot, mount \--bind, and binfmt_misc.

## Contents

-   [[1] [Prerequisites]](#Prerequisites)
    -   [[1.1] [Setting up the environment]](#Setting_up_the_environment)
    -   [[1.2] [Unpacking system files and the Portage tree (new installations)]](#Unpacking_system_files_and_the_Portage_tree_.28new_installations.29)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Emerge]](#Emerge)
-   [[3] [Usage]](#Usage)
-   [[4] [Troubleshooting]](#Troubleshooting)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Prerequisites]

### [Setting up the environment]

When creating a new rootfs, the first thing needed is a directory for the rootfs to reside in. For example, a rootfs could be created in [\~/tmp/gentoo]:

`user `[`$`]`mkdir -p ~/tmp/gentoo `

`user `[`$`]`cd ~/tmp/gentoo `

If an installation has been previously created in a sub directory of the current root file system the above steps can be skipped.

### [][Unpacking system files and the Portage tree (new installations)]

When building a new install, the next step is to download the stage3 tarball and unpack it to the rootfs location. For more information on this process please see [Downloading the stage tarball](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Stage#Downloading_the_stage_tarball "Handbook:AMD64/Installation/Stage") and [Unpacking the stage tarball](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Stage#Unpacking_the_stage_tarball "Handbook:AMD64/Installation/Stage") in the Gentoo [Handbook](https://wiki.gentoo.org/wiki/Handbook:Main_Page "Handbook:Main Page").

`user `[`$`]`curl -LO `[`http://distfiles.gentoo.org/releases/amd64/autobuilds/latest-stage3-amd64-openrc.txt`](http://distfiles.gentoo.org/releases/amd64/autobuilds/latest-stage3-amd64-openrc.txt)` `

`user `[`$`]`LATEST=$(cat latest-stage3-amd64-openrc.txt | tail -n1 | awk '') `

`user `[`$`]`curl -LO "http://distfiles.gentoo.org/releases/amd64/autobuilds/$" `

`user `[`$`]`tar xpvf stage3-*.tar.xz --xattrs-include='*.*' --numeric-owner`

## [Installation]

### [Emerge]

`root `[`#`]`emerge --ask sys-apps/proot`

## [Usage]

`user `[`$`]`proot -S ~/tmp/gentoo /bin/bash`

    ~ #

## [Troubleshooting]

`user `[`$`]`PROOT_NO_SECCOMP=1 proot echo "disable seccomp mode"`

## [See also]

-   [Chroot](https://wiki.gentoo.org/wiki/Chroot "Chroot")

## [External resources]

-   [https://wiki.termux.com/wiki/PRoot](https://wiki.termux.com/wiki/PRoot)