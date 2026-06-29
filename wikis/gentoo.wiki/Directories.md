This article contains a non-exhaustive list of some directories typically found on Gentoo installations that are outside the Linux [Filesystem Hierarchy Standard](https://wiki.gentoo.org/wiki/Filesystem_Hierarchy_Standard "Filesystem Hierarchy Standard"). A few of these special directories are mentioned in the [handbook](https://wiki.gentoo.org/wiki/Handbook:Main_Page "Handbook:Main Page").

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Directory                                                                                                                                                                               Description
  [/]                                                                                                  By default Portage installs all files on the current filesystem to [/].
  [[/etc/conf.d](https://wiki.gentoo.org/wiki//etc/conf.d "/etc/conf.d")]                              Every init script that can be configured has a file in this directory.
  [/etc/env.d]                                                                                         Files which contain the variables.
  [/etc/init.d]                                                                                        Init scripts directory. Most services that can be controlled should install a script here.
  [[/etc/portage](https://wiki.gentoo.org/wiki//etc/portage "/etc/portage")]                           The Portage configuration directory.
  [/etc/runlevels/boot]                                                                                The [boot] runlevel.
  [/etc/runlevels/default]                                                                             The [default] runlevel.
  [/etc/runlevels/nonetwork]                                                                           The [nonetwork] runlevel.
  [/etc/runlevels/reboot]                                                                              The [reboot] runlevel.
  [/etc/runlevels/shutdown]                                                                            The [shutdown] runlevel
  [/etc/runlevels/single]                                                                              The [single] runlevel
  [/etc/runlevels/sysinit]                                                                             The [sysinit] runlevel.
  [/opt/ebuilds]                                                                                       Overlay tree.
  [/usr/lib/ccache/bin]                                                                                The ccache binary directory.
  [[/usr/share/doc/](https://wiki.gentoo.org/wiki//usr/share/doc/ "/usr/share/doc/")\]       Documentation is generally found at this location.
  [/usr/src/linux]                                                                                     Linux sources directory.
  [[/var/cache/binpkgs](https://wiki.gentoo.org/wiki//var/cache/binpkgs "/var/cache/binpkgs")]         Prebuilt binary packages.
  [[/var/cache/distfiles](https://wiki.gentoo.org/wiki//var/cache/distfiles "/var/cache/distfiles")]   Downloaded source code archives.
  [/var/cache/edb]                                                                                     Portage cache.
  [/var/db/pkg]                                                                                        Portage stores the state of the system.
  [[/var/db/repos/gentoo](https://wiki.gentoo.org/wiki//var/db/repos/gentoo "/var/db/repos/gentoo")]   Gentoo repositories\' default location.
  [[/var/lib/portage](https://wiki.gentoo.org/wiki//var/lib/portage "/var/lib/portage")]               The versions for the applications have been explicitly installed.
  [/var/log/portage/elog]                                                                              One log per package.
  [/var/tmp]                                                                                           Portage temporary file directory.
  [/var/tmp/ccache]                                                                                    Portage default ccache home directory.
  [/var/tmp/portage]                                                                                   Portage specific build directories for each package it emerges.
  [emerge \--info \| grep CONFIG_PROTECT=]                                                     Directories which should be protected by Portage during updates, see [`CONFIG_PROTECT`](https://wiki.gentoo.org/wiki/CONFIG_PROTECT "CONFIG PROTECT") article for more information.
  [emerge \--info \| grep CONFIG_PROTECT_MASK=]                                                Directories which should not be protected by Portage during updates, see [`CONFIG_PROTECT`](https://wiki.gentoo.org/wiki/CONFIG_PROTECT "CONFIG PROTECT") article for more information.
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [External resources]

-   [https://devmanual.gentoo.org/general-concepts/filesystem/index.html](https://devmanual.gentoo.org/general-concepts/filesystem/index.html) - General concepts from the Dev Handbook for Gentoo developers on filesystem hierarchy.
-   [https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard) - Wikipedia\'s article on the Linux Filesystem Hierarchy Standard (FHS).