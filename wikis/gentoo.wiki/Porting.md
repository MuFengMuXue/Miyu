As developers expand Gentoo to new architectures and platforms, they may find there is not any real collection of knowledge which explains all the little details of Portage and moving a platform into the experimental release stage. This document aims to address porting Gentoo to new architectures/platforms/etc\...

The example used will port Gentoo Linux to the SuperH (**[sh]**) architecture, but the details should be pretty straightforward for other architectures and operating systems.

## Contents

-   [[1] [Getting the system running]](#Getting_the_system_running)
-   [[2] [Converting to Gentoo]](#Converting_to_Gentoo)
-   [[3] [Preparing a seed for Catalyst]](#Preparing_a_seed_for_Catalyst)
-   [[4] [Preparing a tree snapshot for Catalyst]](#Preparing_a_tree_snapshot_for_Catalyst)
    -   [[4.1] [Alternative]](#Alternative)
-   [[5] [Pushing work into the Gentoo repository]](#Pushing_work_into_the_Gentoo_repository)
    -   [[5.1] [Create the profiles]](#Create_the_profiles)
    -   [[5.2] [Start committing KEYWORDS]](#Start_committing_KEYWORDS)

## [Getting the system running]

This is the hardest step by far (really!). There are two ways to get going:

1.  Either start with an existing Linux port out there (Debian, RedHat, some random hobbyist distribution, etc\...), or
2.  cross compile the entire system

The first route is the easiest, and will be be the focus of this guide.

Simply boot up the system with the existing port and make sure it has all the important packages installed for development. A quick checklist (with recommended minimum versions):

-   binutils (2.20)
-   gcc (4.4)
-   glibc (2.11)
-   python (2.7)
-   rsync
-   wget
-   tar
-   gzip
-   bzip2
-   bash (must be 2.05b or newer, ver 3 is best, accessible as [/bin/bash])

## [Converting to Gentoo]

Once these prerequisite packages are installed, Portage can easily be installed too. This script has been written to do the task. Simply download it and run:

`root `[`#`]`wget `[`https://dev.gentoo.org/~vapier/bootstrap-portage`](https://dev.gentoo.org/~vapier/bootstrap-portage)` `

`root `[`#`]`sh ./bootstrap-portage `

Todo: [ **Todo:**]

-   Move this file to the Gentoo repository and parse the [[[sys-apps/portage]](https://packages.gentoo.org/packages/sys-apps/portage)[]] ebuild\...

\

Make a [profile](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)") for the new architecture: first create a local [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") (overlay) with the new profile, then activate both the repository and the profile:

`root `[`#`]`mkdir -p /var/db/repos/local/profiles/default/linux/sh `

`root `[`#`]`cd /var/db/repos/local/profiles/default/linux/sh `

`root `[`#`]`echo '..' > parent `

`root `[`#`]`cat << EOF > make.defaults`\
`ARCH="sh"`\
`ACCEPT_KEYWORDS="sh"`\
`GRP_STAGE23_USE="pam"`\
`EOF `

`root `[`#`]`mkdir -p /etc/portage `

`root `[`#`]`cd /etc/portage `

`root `[`#`]`echo "PORTDIR_OVERLAY=/var/db/repos/local" >> make.conf `

`root `[`#`]`ln -sfT ../var/db/repos/local/profiles/default/linux/sh make.profile `

** Note**\
To use a newer version of Portage than provided by the bootstrap script, additional steps may be necessary to set up the local ebuild repository and the profile. See the [Profile (Portage)](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)") and [Ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") wiki pages for more information.

Finally, sync up to have a Gentoo tree!

`root `[`#`]`emerge --sync`

## [Preparing a seed for Catalyst]

None of the ebuilds in the tree \"know\" about the new arch, but it is possible to \"cheat\", with [package.keywords] and using **[amd64]** as the reference architecture:

`root `[`#`]`mkdir -p /etc/portage `

`root `[`#`]`cd /etc/portage `

`root `[`#`]`printf '%s x86\n' $(USE="-*" ACCEPT_KEYWORDS=amd64 emerge @system -qep --cols | awk '') >> package.keywords `

Emerge the system into a new ROOT and create a seed file with the result:

`root `[`#`]`env ROOT=~/gentoo-seed/ USE="-*" emerge @system `

`root `[`#`]`tar jpcf ~/seed.tar.bz2 ~/gentoo-seed/ `

## [Preparing a tree snapshot for Catalyst]

Add the **[sh]** KEYWORD to all ebuilds in the [\@system](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)") set. It is possible to use the [[ekeyword]](https://devmanual.gentoo.org/tools-reference/ekeyword/index.html) command from [[[app-portage/gentoolkit]](https://packages.gentoo.org/packages/app-portage/gentoolkit)[]], to automatically update the ebuilds and their manifests:

** Warning**\
The following command modifies the ebuilds in-place. Use [ekeyword -n] instead of [ekeyword -m] for a dry-run.

`root `[`#`]`ekeyword -m $(ACCEPT_KEYWORDS="x86" USE="-*" emerge @system -qep --cols | awk '' | sed -e 's_^\([^ /]*\)/\([^ ]*\) \(.*\)$_sh /var/db/repos/gentoo/\1/\2/\2-\3.ebuild_' | sort -u | tr '\n' ' ')`

** Note**\
As of December 8, 2018, [ekeyword] can only handle arches from the official repository (\'::gentoo\'). Hence, if using an entirely new arch not yet supported by Gentoo, it may be possible to add the arch to [/var/db/repos/gentoo/profiles/arch.list] as a workaround. See [[[bug #672728]](https://bugs.gentoo.org/show_bug.cgi?id=672728)[]] for details.

Once the tree has been updated, create a Catalyst snapshot:

`root `[`#`]`catalyst -C target=snapshot version_stamp=sh`

Before making [stages](https://wiki.gentoo.org/wiki/Stage_file "Stage file") with [catalyst], teach it something about the new arch. Go into [/usr/lib/catalyst/arch/] and copy one of the small [\*.py] modules to [sh.py]. Then edit it to reflect the **[sh]** architecture. Finally edit the [generic_stage_target.py] file in [/usr/lib/catalyst/modules/].

Only need to update the `targetmap` and `machinemap` variables.

Then try building a stage1 with [catalyst] and the seed.

`root `[`#`]`mkdir -p /var/tmp/catalyst/builds `

`root `[`#`]`mv ~/seed.tar.bz2 /var/tmp/catalyst/builds/ `

`root `[`#`]`catalyst -C \`\
`  snapshot=sh version_stamp=sh \`\
`  subarch=sh profile=default/linux/sh \`\
`  rel_type=default target=stage1 \`\
`  source_subpath=seed`

If everything goes well, there should now be a [stage 1 file](https://wiki.gentoo.org/wiki/Stage_file#Stage_1 "Stage file") which can be used to build a stage 2 and a stage 3.

### [Alternative]

For those who dislike the idea of running [catalyst] by hand, grab [this script](http://dev.gentoo.org/~vapier/build-stages) which will generate the repository snapshot and [stage](https://wiki.gentoo.org/wiki/Stage_file "Stage file") 1/2/3 files instead. Simply edit the settings at the top of the script (see above for proper settings).

At the end, the seed file must still be moved manually to the catalyst directory.

## [Pushing work into the Gentoo repository]

So that all this work isn\'t for nothing, share it :).

Here\'s what needs to be updated to not commit half broken work (and making other developers very angry).

### [Create the profiles]

The first profile was just a \'make it work\' solution. Now a much more complete one must be created. After the profile is committed, update the following files in the [profiles/] subdir:

-   [arch.list]
-   [profiles.desc]

Declare the profile status in [profiles.desc] as `exp` for now (it\'ll keep people from yelling).

### [Start committing KEYWORDS]

At this point, it\'s time to start updating ebuilds in the tree with the new KEYWORD.