# Hurd

What happens when you give Wine to a [GNU
Hurd](https://www.gnu.org/software/hurd/hurd.html)?

The Hurd actually isn't a complete environment but a distinct kernel
(like the Linux, System V, and BSD kernels). The Hurd has been in
development on-and-off for over 30 years, and is based on the [CMU Mach
microkernel](https://en.wikipedia.org/wiki/Mach_%28kernel%29). It
consists of only a
[microkernel](https://en.wikipedia.org/wiki/Microkernel) and userspace
components (that handle functions otherwise included in a monolithic
kernel). As a result, unless you're actually developing patches for Wine
to run on the Hurd, you probably need to worry more about the
environment you're using.

Currently, the [Debian Hurd](https://www.debian.org/ports/hurd/) port
is the most stable and popular so you might want to see the
[Debian/Ubuntu](Debian-Ubuntu) page for info on installing and
building wine.

# Status

[Wine 1.7.28 should run well on Debian GNU/Hurd
2013](https://www.gnu.org/software/hurd/open_issues/wine.html). Debian
GNU/Hurd 2015 is out too now so that should makes two releases of Debian
Hurd that play well with a Wine development release!

There was previously an [issue with old versions of
eglibc](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=724681) (prior
to 2.17-94), but with the [merge of eglibc into
glibc](https://www.eglibc.org/home) and the 2015 release of Debian
GNU/Hurd, you probably don't need to worry about it.

**Hurd-related Wine patches:**

- [commit 1](02e6f7d146a35b5a86655c1c1e562f458bfbb74c)
- [commit 2](5865fe78de685e2a5c7e05fa22449382884758dc)
- [commit 3](6d50cfcac28f84e07777fc10874887356832102e)

# See also

- [Compatibility](Compatibility)
