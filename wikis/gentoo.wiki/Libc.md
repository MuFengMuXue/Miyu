**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/C_POSIX_library "wikipedia:C POSIX library")

For Unix-like operating systems, the **libc** is a software component that allows userspace applications to interact with operating system services.

libc implements the facilities specified by the library clause of the C programming language standard ---ISO/IEC International Standard 9899---, the POSIX (*Portable Operating System Interface*) and X/Open system interfaces as defined in IEEE Standard 1003.1, and other extensions.

On Linux distributions the libc implementation normally takes the form of one or more *Executable and Linking Format (ELF) shared object files* (\'.so files\'), with architecture-specific machine code that processes load at runtime using *dynamic linking*. Dynamic linking makes the libc a runtime dependency of pretty much every package, and thus a core component of the distribution.

## [Available software]

** Important**\
musl-based profiles are currently labeled \'experimental\', i.e. [eselect profile list] would show \"(exp)\" after the profile name. Most *stable* Linux profiles are currently GNU libc-based only.

Gentoo supports two libc implementations for Linux:

  ----------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Name                                                  Package                                                                                                                                                                                                                                                                                                                                                            Description
  [glibc](https://wiki.gentoo.org/wiki/Glibc "Glibc")   [[[sys-libs/glibc]](https://packages.gentoo.org/packages/sys-libs/glibc)[]]   from the GNU project, one of the oldest, best-known free software libc implementations. The GNU-style target triplets that represent the resulting operating system (for using e.g. as [values of `CHOST`](https://wiki.gentoo.org/wiki/CHOST "CHOST")) have the form `*-*-linux-gnu*`.
  [musl](https://wiki.gentoo.org/wiki/Musl "Musl")      [[[sys-libs/musl]](https://packages.gentoo.org/packages/sys-libs/musl)[]]      from the musl project, aimed at being simple, lightweight, fast and correct in the sense of standards-conformance and safety. The GNU-style target triplets that represent the resulting operating system have the form `*-*-linux-musl*`.
  ----------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

uclibc-ng (was package *sys-libs/uclibc-ng*) is no longer supported, please use musl.

## [][Gentoo\'s libc setup]

The choice of libc implementation for a Gentoo machine is governed by [profiles](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)").

Profiles that select the Linux kernel (`KERNEL` [USE_EXPAND variable](https://wiki.gentoo.org/wiki/USE_EXPAND "USE EXPAND") set to `linux`) have package [[[virtual/libc]](https://packages.gentoo.org/packages/virtual/libc)[]] in [the system set](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)"), i.e. it is guaranteed to be present in every Gentoo machine. This is a [virtual package](https://wiki.gentoo.org/wiki/Virtual_packages "Virtual packages"), that is, it installs no files but has an any-of dependency, `|| ( ... )`, on other packages, or a similar construct. For these profiles, virtual/libc can be satisfied by one of the aforementioned libc packages depending on the value of the `ELIBC` USE_EXPAND variable.

Musl-based profiles (those with \'musl\' in the name, like [default/linux/amd64/23.0/musl]) set `ELIBC` to `musl`, which causes virtual/libc to be satisfied by sys-libs/musl. Otherwise, `ELIBC` is set to `glibc`, which causes virtual/libc to be satisfied by sys-libs/glibc.

** Note**\
`ELIBC`, just like `KERNEL`, can only be set by profiles.

Musl stage 3 [stage files](https://wiki.gentoo.org/wiki/Stage_file "Stage file") are available in Gentoo mirrors, in \'vanilla\' and hardened variants, although some of them, depending on architecture, might be found in the [/experimental] directory instead of the standard [/releases/\*/autobuilds/current-stage3-\*] directory. Their names have the forms [stage3-\*-musl--\*.tar.. There is also an official musl [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository"), available with [eselect repository](https://wiki.gentoo.org/wiki/Eselect/Repository "Eselect/Repository") under the name \"musl\", which houses additional patches that allow several packages to build with sys-libs/musl.

For a refresher on stage 3s and profiles, please review [the Gentoo Handbook](https://wiki.gentoo.org/wiki/Handbook:Main_Page "Handbook:Main Page").

## [See also]

-   [Gentoo Toolchain Project](https://wiki.gentoo.org/wiki/Project:Toolchain "Project:Toolchain"), responsible of managing the GNU libc package
-   [Gentoo Hardened musl Project](https://wiki.gentoo.org/wiki/Project:Hardened_musl "Project:Hardened musl")
-   [Gentoo Hardened uClibc Project](https://wiki.gentoo.org/wiki/Project:Hardened_uClibc "Project:Hardened uClibc")