This article is used to list deprecated (or simply no longer existent) locations for upstream package repositories. At one time Gentoo ebuild maintainers were able to download source tarballs for packages from these sites. Now that they are no longer usable, ebuild maintainers have the difficult job up tracking down where the upstream projects have decided to move their project repositories.

The broken `SRC_URI` values in the official Gentoo tree generate a lot of maintenance work.

## Contents

-   [[1] [Security]](#Security)
-   [[2] [Mirrors]](#Mirrors)
-   [[3] [Fixing a package]](#Fixing_a_package)
-   [[4] [Notable repositories that were shut down]](#Notable_repositories_that_were_shut_down)

## [Security]

Many projects got forked several times during the shut down procedure and it is not always easy to **find out which fork is the right one** for the Gentoo ebuild.

While many packages need an update to a new URL it is easy to plant silently a link to malicious source code instead of the original source code. It is also possible that a developer uses a wrong fork by accident.

Developers should read also the **[How to deal with package forks?](https://archives.gentoo.org/gentoo-dev/message/18d271b991a4088675444939ce1ee1a1)** discussion as started on 2017-03-09 on the developer mailing list.

## [Mirrors]

Find out, if there sources on **example.com** which we **must not mirror**

`user `[`$`]`cd /var/db/repos/gentoo/metadata/md5-cache; grep "URI=.*example\.com" -R -l | xargs grep "RESTRICT"`

Returns all **RESTRICT** variables of the affected ebuilds. Are they using restrictions which would forbid mirroring in general?

[Note about mirror://gentoo from devmanual](https://devmanual.gentoo.org/general-concepts/mirrors/) \"Previous policy was to use **mirror://gentoo directly, but this is now deprecated**, as that wouldn\'t allow to have long-term availability and traceability of the source files, which might be a requirement of the license. \"

## [Fixing a package]

-   If there is **no** suitable upstream homepage use `HOMEPAGE="https://wiki.gentoo.org/wiki/No_homepage"` as a substitute.

## [Notable repositories that were shut down]

-   2014-04-30: [BerliOS shut down](https://en.wikipedia.org/wiki/BerliOS#SourceForge_mirror_projects "wikipedia:BerliOS") ([[[bug #494678]](https://bugs.gentoo.org/show_bug.cgi?id=494678)[]]) (70 ebuilds affected)
-   2014-06-18: **[Freecode.com (formerly Freshmeat)](https://wiki.gentoo.org/wiki/Upstream_repository_shutdowns/Freecode.com "Upstream repository shutdowns/Freecode.com")** is not updated anymore and was never a primary SRC_URI or HOMEPAGE
-   2015-05-31: gitorious.org shut down ([[[bug #544808]](https://bugs.gentoo.org/show_bug.cgi?id=544808)[]]) (26 ebuilds affected)
-   2015-05-31: **[codehaus.org shut down](https://wiki.gentoo.org/wiki/Upstream_repository_shutdowns/codehaus.org "Upstream repository shutdowns/codehaus.org")** ([[[bug #550054]](https://bugs.gentoo.org/show_bug.cgi?id=550054)[]]) (40 ebuilds affected, all fixed.)
-   2016-03-31: **JavaForge shut down** ([[[bug #636472]](https://bugs.gentoo.org/show_bug.cgi?id=636472)[]]) (2 ebuilds affected)
-   2016-12-31: **[Google Code shut down](https://wiki.gentoo.org/wiki/Upstream_repository_shutdowns/Google_code "Upstream repository shutdowns/Google code")** ([[[bug #544092]](https://bugs.gentoo.org/show_bug.cgi?id=544092)[]]) (500+ ebuilds affected)
-   2017-03-01: **[Fedorahosted.org shut down](https://wiki.gentoo.org/wiki/Upstream_repository_shutdowns/Fedorahosted.org "Upstream repository shutdowns/Fedorahosted.org")** ([[[bug #618046]](https://bugs.gentoo.org/show_bug.cgi?id=618046)[]]) (107 ebuilds affected)
-   2017-03-01: **ftp.kernel.org shut down** ([[[bug #611402]](https://bugs.gentoo.org/show_bug.cgi?id=611402)[]]) (9 ebuilds affected, all fixed by now)
-   2017-05-16: **[gna.org shut down](https://wiki.gentoo.org/wiki/Upstream_repository_shutdowns/gna.org "Upstream repository shutdowns/gna.org")** ([[[bug #612500]](https://bugs.gentoo.org/show_bug.cgi?id=612500)[]]) (88 ebuilds affected)
-   2018-06-05: **[alioth.debian.org shut down](https://wiki.gentoo.org/wiki/Upstream_repository_shutdowns/alioth.debian.org "Upstream repository shutdowns/alioth.debian.org")** ([[[bug #683184]](https://bugs.gentoo.org/show_bug.cgi?id=683184)[]] (60 ebuilds affected)
-   2020-08-20: **[BitBucket retires support for mercurial repositories](https://wiki.gentoo.org/wiki/Upstream_repository_shutdowns/bitbucket.org "Upstream repository shutdowns/bitbucket.org")** [[[bug #737896]](https://bugs.gentoo.org/show_bug.cgi?id=737896)[]] (63 ebuilds affected)