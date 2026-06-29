This page contains [[changes](https://wiki.gentoo.org/index.php?title=Tahoe-LAFS&diff=1244860)] which are not marked for translation.

[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Tahoe-LAFS&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://tahoe-lafs.org/trac/tahoe-lafs/wiki)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Tahoe-LAFS "wikipedia:Tahoe-LAFS")

[[]][GitWeb](https://tahoe-lafs.org/trac/tahoe-lafs/browser)

[[]][GitHub](https://github.com/tahoe-lafs/tahoe-lafs)

[[]][[#tahoe-lafs](ircs://irc.libera.chat/#tahoe-lafs)] ([[webchat](https://web.libera.chat/#tahoe-lafs)])

**Tahoe-LAFS** (**L**east **A**uthority **F**ile **S**ystem) is an encrypted, secure, distributed (fault-tolerant) file system). It does not require trust between parties in order to keep data safe and secure; the only caveat being involved parties must leave their system\'s connected to the storage network.

** Important**\
tahoe-lafs was removed from gentoo ebuild repository on 2020-01-04 with [\[1\]](https://gitweb.gentoo.org/repo/gentoo.git/commit/net-fs?id%7C08ead17b4c1ad65eeebe6bd87ed8c8b381bffa39)

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Emerge fails]](#Emerge_fails)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation]

### [Kernel]

(Optional section. Remove if not applicable.)

[KERNEL]

    Write kernel feature instructions here.

### [USE flags]

There are only a couple USE flags available for Tahoe-LAFS, neither of them incorporate additional functionality. Essentially when more documentation is desired make sure the `doc` flag is enabled in [/etc/portage/package.use].

\

### [Emerge]

Install Tahoe:

`root `[`#`]`emerge --ask net-fs/tahoe-lafs`

## [Configuration]

(Needs written\...)

## [Usage]

(Needs written\...)

### [Invocation]

Tahoe can be invoked via:

`user `[`$`]`tahoe`

## [Troubleshooting]

### [Emerge fails]

[emerge] tahoe-lafs fails with a `pkg_resources.DistributionNotFound` error similar to the following:

[CODE] **Tahoe-LAFS emerge failure**

    * python2_7: running distutils-r1_run_phase distutils-r1_python_compile
    /usr/bin/python2.7 setup.py build
    Traceback (most recent call last):
      File "setup.py", line 73, in &lt;module&gt;
        import setuptools
      File "/usr/lib64/python2.7/site-packages/setuptools/__init__.py", line 11, in &lt;module&gt;
        from setuptools.extension import Extension
      File "/usr/lib64/python2.7/site-packages/setuptools/extension.py", line 8, in &lt;module&gt;
        from .dist import _get_unpatched
      File "/usr/lib64/python2.7/site-packages/setuptools/dist.py", line 19, in &lt;module&gt;
        import pkg_resources
      File "/usr/lib64/python2.7/site-packages/pkg_resources/__init__.py", line 3018, in &lt;module&gt;
        working_set = WorkingSet._build_master()
      File "/usr/lib64/python2.7/site-packages/pkg_resources/__init__.py", line 614, in _build_master
        return cls._build_from_requirements(__requires__)
      File "/usr/lib64/python2.7/site-packages/pkg_resources/__init__.py", line 627, in _build_from_requirements
        dists = ws.resolve(reqs, Environment())
      File "/usr/lib64/python2.7/site-packages/pkg_resources/__init__.py", line 805, in resolve
        raise DistributionNotFound(req)
    pkg_resources.DistributionNotFound: pycrypto==2.1.0,==2.3,&gt;=2.4.1

The work around to this problem is to roll back the [[[dev-python/setuptools]](https://packages.gentoo.org/packages/dev-python/setuptools)[]] package to an earlier version. It appears version 12.0.1 which is currently marked as stable on **[amd64]** as an issue determining versioning for Python dependencies. Rolling back to version 7.0 should do the trick:

`root `[`#`]`emerge --ask =dev-python/setuptools-7.0`

After the new version of [[[dev-python/setuptools]](https://packages.gentoo.org/packages/dev-python/setuptools)[]] is installed proceed with [installation process](#Installation) as normal.

## [See also]

-   [Ceph](https://wiki.gentoo.org/wiki/Ceph "Ceph") --- a distributed object store and filesystem designed to provide excellent performance, reliability, and scalability.
-   [ISCSI](https://wiki.gentoo.org/wiki/ISCSI "ISCSI") --- an IP-based network standard and a [Storage Area Network](https://en.wikipedia.org/wiki/Storage_area_network "wikipedia:Storage area network") (SAN) protocol.

## [External resources]

-   [https://www.linux.com/learn/tutorials/546799:weekend-project-get-started-with-tahoe-lafs-storage-grids](https://www.linux.com/learn/tutorials/546799:weekend-project-get-started-with-tahoe-lafs-storage-grids) - An article explaining what Tahoe-LAFS is and how it works.
-   [https://www.lowendguide.com/3/networking/how-to-set-up-your-own-distributed-redundant-and-encrypted-storage-grid-in-a-few-easy-steps-tahoe-lafs/](https://www.lowendguide.com/3/networking/how-to-set-up-your-own-distributed-redundant-and-encrypted-storage-grid-in-a-few-easy-steps-tahoe-lafs/) - An independently written Tahoe-LAFS setup guide.