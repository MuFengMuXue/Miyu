This page contains [[changes](https://wiki.gentoo.org/index.php?title=FEATURES&oldid=1400404&diff=1421175)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/FEATURES/de "FEATURES (7% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/FEATURES/es "FEATURES (57% translated)")
-   [français](https://wiki.gentoo.org/wiki/FEATURES/fr "FEATURES (NdT: Fonctionnalités) (93% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/FEATURES/it "FEATURES (57% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/FEATURES/hu "FEATURES (100% translated)")
-   [polski](https://wiki.gentoo.org/wiki/FEATURES/pl "FEATURES/pl (7% translated)")
-   [русский](https://wiki.gentoo.org/wiki/FEATURES/ru "FEATURES (100% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/FEATURES/zh-cn "FEATURES (43% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/FEATURES/ja "FEATURES (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/FEATURES/ko "FEATURES (36% translated)")

The `FEATURES` variable contains a list of Portage features that the user wants enabled on the system, effectively influencing Portage\'s behavior. It is set by default via [/usr/share/portage/config/make.globals], but can be easily updated through [[/etc/portage/make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf")]. Since this is an [incremental variable](https://dev.gentoo.org/~ulm/pms/head/pms.html#section-5.3.1), `FEATURES` values can be added without directly overriding the ones implemented through the Gentoo profile.

[FILE] **`/etc/portage/make.conf`Adding keepwork to FEATURES in Portage**

    FEATURES="keepwork"

[[portageq](https://wiki.gentoo.org/wiki/Portageq "Portageq")] can be used to show the active features:

`user `[`$`]`portageq envvar FEATURES | xargs -n 1`

The descriptions of the FEATURES are available in the man page for make.conf:

`user `[`$`]`man make.conf`

\

## Contents

-   [[1] [Usage]](#Usage)
-   [[2] [Default FEATURES]](#Default_FEATURES)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Usage]

FEATURES is often prepended to the [emerge] command for e.g. keeping the build log or triggering tests:

`root `[`#`]`FEATURES="keeptemp test" emerge -1a foobar`

## [Default FEATURES]

Below is a list of the FEATURES enabled by default in Portage, for the most up-to-date version of this, see the list [here](https://github.com/gentoo/portage/blob/master/cnf/make.globals#L77). The descriptions are taken from their respective entry in [[[make.conf(5)]](https://dev.gentoo.org/~zmedico/portage/doc/man/make.conf.5.html)][[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page").

  ---------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Feature                      Description
  assume-digests               When committing work to cvs with [[[repoman(1)]](https://dev.gentoo.org/~zmedico/portage/doc/man/repoman.1.html)][[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page"), assume that all existing `SRC_URI` digests are correct. This feature also affects digest generation via [[[ebuild(1)]](https://dev.gentoo.org/~zmedico/portage/doc/man/ebuild.1.html)][[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page") and [[[emerge(1)]](https://dev.gentoo.org/~zmedico/portage/doc/man/emerge.1.html)][[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page") (emerge generates digests only when the digest feature is enabled). Existing digests for files that do not exist in `$` will be automatically assumed even when assume-digests is not enabled. If a file exists in `$` but its size does not match the existing digest, the digest will be regenerated regardless of whether or not assume-digests is enabled. The [[[ebuild(1)]](https://dev.gentoo.org/~zmedico/portage/doc/man/ebuild.1.html)][[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page") digest command has a `--force` option that can be used to force regeneration of digests.
  binpkg-docompress            Perform docompress (controllable file compression) before creating binary package. When this option is enabled (the default), documentation files are already compressed inside binary packages. When it is disabled, binary packages contain uncompressed documentation and Portage compresses it before installing.
  binpkg-dostrip               Perform file stripping before creating binary package. When this option is enabled (the default), executables are already stripped inside binary packages. When it is disabled, binary packages contain unstripped executables and Portage strips (or splits) them before installing.
  binpkg-logs                  Keep logs from successful binary package merges. This is relevant only when `PORTAGE_LOGDIR` is set.
  binpkg-multi-instance        Enable support for multiple binary package instances per ebuild. Having multiple instances is useful for a number of purposes, such as retaining builds that were built with different USE flags or linked against different versions of libraries.
  buildpkg-live                When this option is enabled (the default), buildpkg will exhibit the default behavior of building binary cache for all packages. When it is disabled, binary packages will not be created for live ebuilds.
  compress-index               If set then a compressed copy of `Packages` index file will be written. This feature is intended for Gentoo binhosts using certain webservers (such as, but not limited to, Nginx with gzip_static module) to avoid redundant on-the-fly compression. The resulting file will be called `Packages.gz` and its modification time will match that of `Packages`.
  config-protect-if-modified   This causes the `CONFIG_PROTECT` behavior to be skipped for files that have not been modified since they were installed. This feature is enabled by default.
  distlocks                    Portage uses lockfiles to ensure competing instances don't clobber each other's files. It covers saving distfiles to `$` and binpkgs to `$`.
  ebuild-locks                 Use locks to ensure that unsandboxed ebuild phases never execute concurrently. Also see parallel-install.
  fixlafiles                   Modifies .la files to not include other .la files and some other fixes (order of flags, duplicated entries, \...)
  ipc-sandbox                  Isolate the ebuild phase functions from host IPC namespace. Supported only on Linux. Requires IPC namespace support in kernel.
  merge-sync                   After a package is merged or unmerged, sync relevant files to disk in order to avoid data-loss in the event of a power failure. This feature is enabled by default.
  merge-wait                   Wait for all builds to complete before merging new packages, which only matters when using the emerge(1) \--jobs option. Unless the [[[emerge(1)]](https://dev.gentoo.org/~zmedico/portage/doc/man/emerge.1.html)][[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page") `--implicit-system-deps=n` option is used, merge-wait is always effectively enabled for packages that satisfy direct or indirect dependencies of the system set. The merge-wait feature can be disabled in order to trade the possibility of random build failures for greater parallelism. The queue can be flushed by sending the SIGUSR2 signal to [[[emerge(1)]](https://dev.gentoo.org/~zmedico/portage/doc/man/emerge.1.html)][[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page").
  multilib-strict              Many Makefiles assume that their libraries should go to [/usr/lib], or [\$(prefix)/lib]. This assumption can cause a serious mess if [/usr/lib] isn't a symlink to [/usr/lib64]. To find the bad packages, we have a portage feature called multilib-strict. It will prevent emerge from putting 64bit libraries into anything other than [(/usr)/lib64].
  network-sandbox              Isolate the ebuild phase functions from host network interfaces. Supported only on Linux. Requires network namespace support in kernel.
  news                         Enable GLEP 42 news support. See [https://www.gentoo.org/glep/glep-0042.html](https://www.gentoo.org/glep/glep-0042.html).
  parallel-fetch               Fetch in the background while compiling. Run 'tail -f /var/log/emerge-fetch.log' in a terminal to view parallel-fetch progress.
  pkgdir-index-trusted         Trust that the `PKGDIR` index file is valid, meaning that no packages have been manually added or removed since the last call to `emaint --fix binhost`. This feature eliminates overhead involved with detection of packages that have been manually added or removed, which significantly improves performance in some cases, such as when `PKGDIR` resides on a high-latency network file system.
  pid-sandbox                  Isolate the process space for the ebuild processes. This makes it possible to cleanly kill all processes spawned by the ebuild. Supported only on Linux. Requires PID and mount namespace support in kernel. [/proc] is remounted inside the mount namespace to account for new PID namespace.
  preserve-libs                Preserve libraries when the sonames change during upgrade or downgrade. Libraries are preserved only if consumers of those libraries are detected. Preserved libraries are automatically removed when there are no remaining consumers. Run `emerge @preserved-rebuild` in order to rebuild all consumers of preserved libraries.
  protect-owned                This is identical to the collision-protect feature except that files may be overwritten if they are not explicitly listed in the contents of a currently installed package. This is particularly useful on systems that have lots of orphan files that have been left behind by older versions of portage that did not support the `unmerge-orphans` feature. Like collision-protect, the `COLLISION_IGNORE` variable can be used to selectively disable this feature. It is recommended to leave either protect-owned or collision-protect enabled at all times, since otherwise file collisions between packages may result in files being overwritten or uninstalled at inappropriate times. If collision-protect is enabled then it takes precedence over protect-owned.
  qa-unresolved-soname-deps    Trigger a QA warning when a package installs files with unresolved soname dependencies.
  sandbox                      Enable sandbox-ing when running [[[emerge(1)]](https://dev.gentoo.org/~zmedico/portage/doc/man/ebuild.1.html)][[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page") and [[[ebuild(1)]](https://dev.gentoo.org/~zmedico/portage/doc/man/emerge.1.html)][[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page").
  strict                       Have portage react strongly to conditions that have the potential to be dangerous (like missing or incorrect digests for ebuilds).
  unknown-features-warn        Warn if `FEATURES` contains one or more unknown values.
  unmerge-logs                 Keep logs from successful unmerge phases. This is relevant only when `PORTAGE_LOGDIR` is set.
  unmerge-orphans              If a file is not claimed by another package in the same slot and it is not protected by `CONFIG_PROTECT`, unmerge it even if the modification time or checksum differs from the file that was originally installed.
  userfetch                    When portage is run as root, drop privileges to portage:portage during the fetching of package sources.
  userpriv                     Allow portage to drop root privileges and compile packages as portage:portage without a sandbox (unless usersandbox is also used).
  usersandbox                  Enable the sandbox in the compile phase, when running without root privs (userpriv).
  usersync                     Drop privileges to the owner of `$` for [[[emerge(1)]](https://dev.gentoo.org/~zmedico/portage/doc/man/emerge.1.html)][[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page") `--sync` operations. Note that this feature assumes that all subdirectories of `$` have the same ownership as `$` itself. It is the user's responsibility to ensure correct ownership, since otherwise Portage would have to waste time validating ownership for each and every sync operation.
  ---------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [See also]

-   [Handbook:AMD64/Working/Features](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/Features "Handbook:AMD64/Working/Features")

## [External resources]

-   [FEATURES](https://devmanual.gentoo.org/eclass-reference/make.conf/index.html) in the Gentoo developer manual