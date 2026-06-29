The `CHOST` variable tells the compiler which platform code should be built for. Unlike the [`CFLAGS`](https://wiki.gentoo.org/wiki/GCC_optimization "GCC optimization") variable, which is used for the optimizations, the `CHOST` variable is fixed and cannot be changed easily.

The [profile](https://wiki.gentoo.org/wiki/Portage/Profiles "Portage/Profiles") provides the default `CHOST` values, but it can be changed in the [/etc/portage/make.conf] file.

The variable is a dash-separated tuple in the form of *ARCH*-*VENDOR*-*OS*-*LIBC*:

  ---------- --------------------------------------------
  Values     Descriptions
  *ARCH*     Specifies the CPU architecture.
  *VENDOR*   Specifies the hardware platform or vendor.
  *OS*       Specifies the operating system.
  *LIBC*     Specifies the C library to use.
  ---------- --------------------------------------------

Only *ARCH* is strictly required in all cases, but it is good practice to specify all four fields (for Linux machines at least). For operating systems suffixed by a \'\*\', a kernel version should go in its place. Additionally, the *LIBC* field should usually be ommitted for said operating systems.

The following non-comprehensive table lists some field values known to work:

+---------------------------------------------------------------------------------+---------------------+-------------------+-------------------+
| Architecture                                                                    | Vendor              | Operating System  | C Library         |
+---------------------------------------------------------------------------------+---------------------+-------------------+-------------------+
| required                                                                        | optional            | optional          | optional          |
+---------------------------------------------------------------------------------+---------------------+-------------------+-------------------+
| aarch64 / aarch64_be\                                                           | apple\              | darwin\*\         | eabi (arm)\       |
|                                                                                 |                     |                   |                   |
| arm64 (only use this for arm64-apple-)\                            | gentoo\             | elf\              | gnu\              |
| alpha\                                                                          | ibm (s390 only)\ | freebsd\*\        | gnuabi64 (mips)\  |
| arm / armv4 / armv4l / armv4t / armv4tl / armv5te / armv5tel / armv6j / armv7a\ | pc\                 | gentoo-freebsd\*\ | gnuabin32 (mips)\ |
| hppa / hppa1.1 / hppa2.0 / hppa64\                                              | pc_t64\             | ios\*\            | gnueabi (arm)\    |
| i386 / i486 / i586 / i686\                                                      | softfloat\          | linux\            | gnueabihf (arm)\  |
| ia64\                                                                           | softfp\             | solaris\*\        | gnux32 (x86_64)\  |
| loongarch64\                                                                    | hardfloat\          | uclinux           | musl\             |
| m68k\                                                                           | unknown             |                   | musleabi (arm)\   |
| mips / mipsel\                                                                  |                     |                   | musleabihf (arm)\ |
| mips64 / mips64el\                                                              |                     |                   | uclibc            |
| powerpc / powerpcle\                                                            |                     |                   |                   |
| powerpc64 / powerpc64le\                                                        |                     |                   |                   |
| riscv32 / riscv64\                                                              |                     |                   |                   |
| s390 / s390x\                                                                   |                     |                   |                   |
| sh / sh4 / sh64\                                                                |                     |                   |                   |
| sparc / sparc64\                                                                |                     |                   |                   |
| x86_64                                                                          |                     |                   |                   |
+---------------------------------------------------------------------------------+---------------------+-------------------+-------------------+

## [Examples]

-   aarch64-unknown-linux-gnu
-   arm64-apple-darwin21
-   armv5tel-softfloat-linux-gnueabi
-   powerpc-apple-darwin9
-   powerpc64le-unknown-linux-musl
-   x86_64-pc-linux-gnu
-   x86_64-pc-solaris2.11

## [See also]

-   [Changing the CHOST variable](https://wiki.gentoo.org/wiki/Changing_the_CHOST_variable "Changing the CHOST variable") --- explains how to change the [`CHOST`] variable of an existing system.