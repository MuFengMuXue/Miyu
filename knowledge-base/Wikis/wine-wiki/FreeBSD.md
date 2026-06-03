[FreeBSD](https://www.freebsd.org/) is one of the classic unixes
(unices?) with a long history of great ideas but is still thoroughly
modern. Read on for more details about setting up wine on your FreeBSD
system.

Also, if you're using either [PC-BSD](https://www.pcbsd.org/) or
[ArchBSD](https://www.pacbsd.org/), these are downstream projects of
FreeBSD that specialize in providing a good desktop experience and
simple packaging. Some instructions might not be the same (e.g. ArchBSD
uses the `pacman` package manager instead of Ports), but both projects
cooperate and regularly re-sync with FreeBSD so many concepts and issues
should be very similar.

## Installation

The FreeBSD Ports repository contains up-to-date packages for Wine's
stable, development, and experimental staging releases; you can install
them on 32-bit FreeBSD easily

```
pkg install wine
pkg install wine-devel
pkg install wine-staging
```

If you're on a 64-bit version of FreeBSD, you'll need to use the special
i386 packages to get 32-bit wine. Instead of the packages listed above,
just choose from

```
pkg install i386-wine
pkg install i386-wine-devel
pkg install i386-wine-staging
```

Don't let the i386 name fool you; these packages are only meant to allow
32-bit wine on amd64 systems. If you're on 32-bit FreeBSD, the packages
may have a failsafe that redirects to the vanilla one anyway, but it's
much safer if you stick to the normal packages.

FreeBSD can actually build and run the pure 64-bit version of wine now.
The problem is that it still doesn't support WoW64, and since that's
necessary for the overwhelming majority of Windows apps,
[AMD64](AMD64) systems still need to use the 32-bit package.

## Building Wine

The instructions below lay out the most straight-forward approaches to
[Building Wine](Building-Wine) on FreeBSD (which follow the
standard instructions in spirit, but using BSD idioms).

If you're on an amd64 system, FreeBSD's packages, including the base
system and build tools, respect
[multilib](Building-Wine#multi-arch-and-multi-lib) conventions
([apparently since Jun 2013 or
earlier](https://lists.freebsd.org/pipermail/freebsd-current/2013-June/042378.html)).
However, per communication with FreeBSD devs in spring 2017, there is
no plan or intent to add multiarch-style cross-compiling to the ports
system (probably because FreeBSD's approach to cross-compiling is
already so mature and streamlined).

### Classic chroot

FreeBSD makes chroots wicked simple. All you need to do is...

- Load the necessary i386 files for a chroot into a folder

  ```sh
  $ cd /usr/src
  $ make buildworld TARGET=i386
  $ make installworld TARGET=i386 DESTDIR=/compat/i386
  $ make distribution TARGET=i386 DESTDIR=/compat/i386
  $ mkdir /compat/i386/usr/ports
  ```

- Add mount points for necessary directories to the chroot

  ```sh
  $ mount -t devfs devfs /compat/i386/dev
  $ mount -t nullfs /usr/ports /compat/i386/usr/ports
  ```

- Enter the chroot, set a few environment variables, and start
  `ldconfig` running

  ```sh
  $ chroot /compat/i386
  $ setenv MACHINE i386
  $ setenv UNAME_m i386
  $ setenv UNAME_p i386
  $ service ldconfig start
  ```

- Then move to your desired build directory and make the package

  ```sh
  $ cd /usr/ports/emulators/i386-wine-devel
  $ make package
  ```

And you're done!

If you're not sure where your built package was saved, while **still
in** the chroot, you can ask with `make -V` and the `PKGFILE`
environment variable:

```sh
$ echo /compat/i386/$(make -V PKGFILE)
```

### Poudriere

If you want to add a layer of quality control when you build wine, or
maybe you want to help "package" it (build a port) for FreeBSD, then the
previous info is good to know, but you'll also want to read up on
[poudriere](https://www.freebsd.org/doc/handbook/ports-poudriere.html).
This tool is designed to automate the extra build and quality-control
steps you want for a high-quality release. If you're familiar with
Debian's `debuild` system, it's like that (only
with the splendor and majesty of
[ZFS](https://www.freebsd.org/doc/handbook/zfs.html)).

If you're trying to cross-compile wine on FreeBSD to another platform,
you also might want to use poudriere. Per communication with FreeBSD
developers in spring 2017, while poudriere is not strictly necessary for
cross-compiling on FreeBSD, it simplifies the process and is the
**preferred method for port builders**.

## Outstanding Issues

There are still many subtle bugs in how wine runs on FreeBSD vs. other
platforms. Some of them might be due to our upstream code while others
sneak in during the packaging process. The former will ideally be
tracked here at WineHQ while the latter should wind up on the FreeBSD
bug-tracker:

- [Open FreeBSD-specific bugs here at
  WineHQ](https://bugs.winehq.org/buglist.cgi?op_sys=FreeBSD&query_format=advanced&product=Wine&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=STAGED&bug_status=REOPENED&bug_status=RESOLVED)
- [Open wine bugs at
  FreeBSD](https://bugs.freebsd.org/bugzilla/buglist.cgi?short_desc=wine&query_format=advanced&bug_status=New&bug_status=Open&bug_status=In%20Progress&bug_status=UNCONFIRMED&short_desc_type=allwordssubstr)

However, while neither of the bug-trackers seem to have an open ticket
for it, our main structural problem now is WoW64 support on FreeBSD. If
you're interested in helping fix WoW64 support on FreeBSD, your best bet
is to first try following the [shared WoW64 build
instructions](Building-Wine#shared-wow64) to compile wine
from source (preferably from the tip of our git tree).

If (when?) this fails, concentrate on the first error; if there's no
simple workaround, [submit a patch](Submitting-Patches) if
you feel up to it, or if not, at least [report the bug](Bugs)
on the proper bug-tracker. Once you can compile and link a WoW64-capable
version of wine, you can move onto runtime errors. And don't forget that
the wine [Conformance Tests](Conformance-Tests) are great for
pinpointing problems too.

## See Also

- The FreeBSD Wiki's [main page for Wine](https://wiki.freebsd.org/Wine)
- [32-bit Wine on 64-bit FreeBSD](https://wiki.freebsd.org/i386-Wine),
  also on the FreeBSD Wiki
- [Building Wine](Building-Wine)
- [Packaging](Packaging)
- [Compatibility](Compatibility)
- Psst... if a problem on FreeBSD has you bamboozled,
  [macOS](MacOS) inherits much of FreeBSD's user-space and
  even some of the kernel; maybe OS X bug reports, patches, and test
  results can give you hints
