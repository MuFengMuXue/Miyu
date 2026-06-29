## What is Multiarch?

In order to ease cross-compiling and distribution, the Debian-based
distros have undertaken a project known as "multi-arch". The idea is to
update the packaged software itself, and occasionally change how it's
built, so that every package can satisfy multiple architectures. Either
one version of the package will work for all architectures, or the
different architectures' versions can be installed alongside each other.

To be fully compliant, a package not only needs to play well with
different architectures, but explicitly state how it operates in a
multi-arch environment. This is implemented through values in the
control file of each source package, which are then enforced by the
distro's package management.

While there are general guidelines, each package has its own dynamic so
making it multi-arch compatible is largely up to that package's
maintainer. As a result, multi-arch is still a work in progress, and the
distros prioritize which packages they focus on.

According to documents from ca. 2013, multi-arch behavior for
header-files (common in -dev packages) was undefined. Since then, the
Debian-family distros have settled on using subdirectories for
multi-arch triplets within */usr/include/*. Note that this extension is
not yet part of the [Filesystem Hierarchy
Standard](https://refspecs.linuxfoundation.org/fhs.shtml).

## Status of Wine Build Dependencies

Perhaps the main (but not only) way this matters to Wine is in regards
to building and porting. Once all of Wine's build dependencies are
multi-arch compatible, cross-compiling and packaging Wine for different
architectures becomes much simpler.

As of November 2020, building Wine 5.5 on Debian Buster shows the
following build dependencies still conflicting across architectures
(version info may be different for Ubuntu, Mint, etc.)

| Debian Package     | Stable Version | Unstable Version | Apt-get Result                 | Debian Bug Report | Fixed in Buster? | Fixed in Bullseye? | Notes                                                                    |
|--------------------|----------------|------------------|--------------------------------|-------------------|------------------|--------------------|--------------------------------------------------------------------------|
| libsdl2-dev        | 2.0.9+dfsg1-1  | 2.0.12+dfsg1-4   | Conflicts across architectures | \#909740          | no               | yes                |                                                                          |
| libxml-parser-perl | 2.44-4         | 2.46-2           | Requires dependencies          | \#717882          | no               | no                 | Requires **perl** and **perl-base** to resolve. Unlikely to be resolved. |

## See Also

Some of these pages might be out of date, but they're still good places
to start:

- The [MultiarchSpec](https://wiki.ubuntu.com/MultiarchSpec) on the
  Ubuntu Wiki
- [Multiarch](https://wiki.debian.org/Multiarch) on the Debian Wiki
- [MultiarchCross](https://wiki.ubuntu.com/MultiarchCross) on the Ubuntu
  Wiki has details about how multi-arch works with -dev packages.
