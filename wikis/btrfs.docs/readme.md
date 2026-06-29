# README

Btrfs-progs
===========


Userspace utilities to manage btrfs filesystems.
License: GPLv2.

Btrfs is a copy on write (COW) filesystem for Linux aimed at implementing
advanced features while focusing on fault tolerance, repair and easy
administration.

This repository hosts following utilities and also documentation:

* **btrfs** &mdash; the main administration tool ([manual page](https://btrfs.readthedocs.io/en/latest/btrfs.html))
* **mkfs.btrfs** &mdash; utility to create the filesystem ([manual page](https://btrfs.readthedocs.io/en/latest/mkfs.btrfs.html))
* all-in-one binary in the busybox style with mkfs.btrfs, btrfs-image and other tools built-in ([standalone tools](https://btrfs.readthedocs.io/en/latest/btrfs.html#standalone-tools))
* **libbtrfsutil** (LGPL v2.1) &mdash; C and python 3 bindings, see [libbtrfsutil/README.md](libbtrfsutil/README.md) for more
* **btrfsutil** python bindings published at https://pypi.org/project/btrfsutil
* manual pages and documentation source published at [btrfs.readthedocs.io](https://btrfs.readthedocs.io) (RTD)

See [INSTALL](INSTALL) for build instructions, [tests/README.md](tests/README.md) for
testing information and [ci/README.md](ci/README.md) for CI information.

Release cycle
-------------

The major version releases are time-based and follow the cycle of the linux
kernel releases. The cycle usually takes 2 months. A minor version release may
happen in the meantime if there are bug fixes or minor useful improvements
queued.

The release tags are signed with a GPG key ID `F2B4 1200 C54E FB30 380C  1756 C565 D5F9 D76D 583B`,
release tarballs are hosted at [kernel.org](https://www.kernel.org/pub/linux/kernel/people/kdave/btrfs-progs/).
See file [CHANGES](CHANGES) or [changelogs on RTD](https://btrfs.readthedocs.io/en/latest/CHANGES.html).

Releases with changelog are also published at [Github release page](https://github.com/kdave/btrfs-progs/releases).

### Static binaries

For each release there are static binaries of `btrfs` and `btrfs.box` provided.
These can be used in rescue environments and are built for `x86_64`
architecture (with maximum backward compatibility), inside the [Github Actions
workflow](https://github.com/kdave/btrfs-progs/actions/workflows/artifacts-static-build.yml).
The `btrfs.box` is an all-in-one tool in the [busybox](https://www.busybox.net)
style, the functionality is determined by the binary names (either symlink,
hardlink or a file copy).

### Feature compatibility

The *btrfs-progs* of version *X.Y* declare support of kernel features of the same
version. New progs on old kernel are expected to work, limited only by features
provided by the kernel.

### Build compatibility

Build is supported on the [GNU C library](https://www.gnu.org/software/libc/)
as the primary target, and on the [musl libc](https://musl.libc.org/)
and [uClibc-ng](https://www.uclibc-ng.org/).

The supported compilers are [gcc](https://gcc.gnu.org/) (minimal version 4.8)
and [clang](https://clang.llvm.org/) (minimal version 3.4).

Build tests are done on [several distributions](https://github.com/kdave/btrfs-progs/blob/master/.github/workflows/image-build-test.yml), see
[Github actions workflow](https://github.com/kdave/btrfs-progs/actions/workflows/image-build-test.yml).

Reporting bugs
--------------

There are several ways, each has its own specifics and audience that can give
feedback or work on a fix. The following list is sorted in the order of
preference:

* [Github issue tracker](https://github.com/kdave/btrfs-progs/issues)
* to the mailing list *linux-btrfs@vger.kernel.org* -- (not required to
  subscribe), beware that the mail might get overlooked in other traffic
* IRC (irc.libera.chat #btrfs) -- good for discussions eg. if a bug is already
  known, but reports could miss developers' attention
* please don't use https://bugzilla.kernel.org for btrfs-progs bugs

Third-party sources
-------------------

Build dependencies are listed in [INSTALL](INSTALL). Implementation of checksum/hash
functions is provided by copies of the respective sources to avoid adding
dependencies that would make deployments in rescue or limited environments
harder. The implementations are portable and there are optimized versions for
some architectures.  Optionally it's possible to use
[libgcrypt](https://www.gnupg.org/software/libgcrypt/index.html),
[libsodium](https://doc.libsodium.org),
[libkcapi](https://www.chronox.de/libkcapi.html),
[Botan](https://botan.randombit.net) or
[OpenSSL](https://www.openssl.org) implementations.

The builtin implementations uses the following sources:
[CRC32C](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git),
[XXHASH](https://github.com/Cyan4973/xxHash),
[SHA256](https://tools.ietf.org/html/rfc4634),
[BLAKE2](https://github.com/BLAKE2/BLAKE2).

Some other code is borrowed from kernel, eg. the raid5 tables or data structure
implementation (list, rb-tree).

References
----------

* [Documentation](https://btrfs.readthedocs.io)
* [Manual pages](https://btrfs.readthedocs.io/en/latest/man-index.html)
* [Changes -- btrfs-progs](https://btrfs.readthedocs.io/en/latest/CHANGES.html)
* [Features by kernel version](https://btrfs.readthedocs.io/en/latest/Feature-by-version.html)
