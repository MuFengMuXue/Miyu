This page is designed **for package maintainers**, to describe the maintenance tasks to consider when working on [Munin](https://wiki.gentoo.org/wiki/Munin "Munin").

## Contents

-   [[1] [Source code repository]](#Source_code_repository)
-   [[2] [New features]](#New_features)
    -   [[2.1] [IPMI]](#IPMI)
-   [[3] [TODO]](#TODO)

## [Source code repository]

Upstream moved their main source repository to [GitHub](https://github.com/munin-monitoring/munin/) which makes maintenance much simpler. All the patching is handled on GitHub as well, in the [Gentoo Linux fork](https://github.com/gentoo/munin).

For each release that needs to be patched, a new Gentoo branch is created starting from the upstream branch

`user `[`$`]`git clone `[`git://github.com/munin-monitoring/munin.git`](git://github.com/munin-monitoring/munin.git)` `

`user `[`$`]`cd munin `

`user `[`$`]`git remote add gentoo git@github.com:gentoo/munin.git `

`user `[`$`]`git checkout -b 2.0.3-gentoo 2.0.3 `

At this point it\'s possible to either use **git cherry-pick** to bring in the patches committed upstream, or commit new changes to send upstream so that they can be merged by the developers.

Once the patches are in the branch you can then use the **git** commands to create a patchset tarball and upload it to the **dev.gentoo.org** space. As of July 2012, Diego (Flameeyes) is providing access to his webspace at [\[1\]](http://dev.gentoo.org/~flameeyes/munin/) for patchset storage.

`user `[`$`]`cd munin `

`user `[`$`]`rm -rf patches `

`user `[`$`]`mkdir patches && cd patches `

`user `[`$`]`git format-patch 2.0.3.. # use the tag the current branch refers to `

`user `[`$`]`cd .. `

`user `[`$`]`tar Jcf munin-2.0.3-patches-1.tar.xz patches/*.patch # make sure to update the patchset number `

`user `[`$`]`scp munin-2.0.3-patches-1.tar.xz dev.gentoo.org:~flameeyes/public_html/munin/ `

`user `[`$`]`git tag 2.0.3-gentoo-1 `

`user `[`$`]`git push gentoo --tags && git push gentoo 2.0.3-gentoo `

Using this method is actually possible to keep [files/] pretty empty (with only the extra configuration files), which is good as users don\'t have to put up with a long sync time for packages they don\'t use.

## [New features]

While upstream is very friendly, sometimes things need to be prodded along to work correctly. This has been the case with the libwww-perl version support as well as recently the FreeIPMI-based plugin. Don\'t be surprised of what you can find into our patchset tarballs.

### [IPMI]

The official IPMI monitoring plugins coming with Munin 2.0 (**ipmi\_** and **ipmi_sensor\_**) are based off [[[sys-apps/ipmitool]](https://packages.gentoo.org/packages/sys-apps/ipmitool)[]] --- but by default this tool does not cache the sensor description data which makes it useless for most modern systems as the node will time out the plugin way before it completes.

For this reason our IPMI plugin is instead the new one Flameeyes contributed to upstream, which is based off [[[sys-libs/freeipmi]](https://packages.gentoo.org/packages/sys-libs/freeipmi)[]] and supports all the same features (as long as a patched, or new enough FreeIPMI version is used), and is interface compatible with both the original plugins.

## [TODO]

Starting from version 2 Munin [supports natively rrdcached](http://munin-monitoring.org/wiki/rrdcached) (from [[[net-analyzer/rrdtool]](https://packages.gentoo.org/packages/net-analyzer/rrdtool)[]]) but we neither have an easy way to set that up nor an init script for it. It would be cool to be able to have it working out of the box, this ties in with the CGI support (as then it should be relatively lightweight to generate the graphs on the fly).

It has to be noted that upstream would prefer for new plugins not to be added to the main package, and instead rely on a [Contrib repository](https://github.com/munin-monitoring/contrib). This repository does not have releases, have possibly untested scripts but it\'s likely we\'ll need a package for it if anything because there won\'t otherwise be any new plugins. The big hurdle with this is that not all the files have a clear license, which makes it hard to package.