**[] Deprecated article**\
\

This article is **deprecated (obsolete)**. Contents are [no longer relevant], and are intended for historical reference only!

\
TLDR: **Do not use this article!**

The `SYNC` variable located in [[/etc/portage/make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf")] was used to set the rsync server URL in order to update the main Gentoo repository. `SYNC` has been *deprecated* in favor of using new the plug-in sync system (defined in [[/etc/portage/repos.conf/gentoo.conf]](https://wiki.gentoo.org/wiki/Project:Portage/Sync#Portage_configuration "Project:Portage/Sync") file).

** Tip**\
Although `SYNC` can still be used in most cases it is recommended all users upgrade repository syncing on their systems to use the new [[/etc/portage/repos.conf](https://wiki.gentoo.org/wiki//etc/portage/repos.conf "/etc/portage/repos.conf")] configuration.

## [External resources]

-   [https://www.gentoo.org/support/news-items/2015-02-04-portage-sync-changes.html](https://www.gentoo.org/support/news-items/2015-02-04-portage-sync-changes.html) - Main site news item announcing the plug-in sync system.