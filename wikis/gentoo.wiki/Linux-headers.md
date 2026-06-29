**linux-headers** is a package providing the [Linux kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") headers. These are part of the kernel, although they are shipped separately (further reasoning is available: [\[1\]](https://web.archive.org/web/20171219160722/http://linuxmafia.com/faq/Kernel/usr-src-linux-symlink.html)). The headers act as an interface between internal kernel components and also between [userspace](https://en.wikipedia.org/wiki/User_space "wikipedia:User space") and the kernel. Packages like [[[sys-libs/glibc]](https://packages.gentoo.org/packages/sys-libs/glibc)[]] depend on the kernel headers.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [FAQ]](#FAQ)
-   [[3] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [sys-kernel/linux-headers](https://packages.gentoo.org/packages/sys-kernel/linux-headers) [[]] [Linux system headers]

  --------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------
  [`headers-only`](https://packages.gentoo.org/useflags/headers-only)   Install only C headers instead of whole package. Mainly used by sys-devel/crossdev for toolchain bootstrap.
  --------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-05 04:04] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[sys-kernel/linux-headers]](https://packages.gentoo.org/packages/sys-kernel/linux-headers)[]]:

`root `[`#`]`emerge --ask sys-kernel/linux-headers`

## [FAQ]

A common question regarding linux-headers is whether you need to keep them synced with your kernel version. The answer is no. You can have a *newer* linux-headers version than your running kernel binary.

So for example, if you have kernel 4.1 installed, you can have linux-headers 4.4. If you compile your **glibc** with this newer headers and later upgrade to kernel 4.4, you will be able to use the new features of this kernel without recompiling **glibc** again.

For more information read [glibc FAQ](https://sourceware.org/glibc/wiki/FAQ#What_version_of_the_Linux_kernel_headers_should_be_used.3F) and [\[2\]](https://sourceware.org/ml/libc-help/2014-11/msg00010.html).

## [External resources]

-   [http://kernelnewbies.org/KernelHeaders](http://kernelnewbies.org/KernelHeaders) - KernelNewbies provides a nice overview of kernel headers.