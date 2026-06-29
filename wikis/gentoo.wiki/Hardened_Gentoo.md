Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Hardened_Gentoo/de "Gehärtetes Gentoo (Hardened Gentoo) (64% translated)")
-   [English]
-   [Nederlands](https://wiki.gentoo.org/wiki/Hardened_Gentoo/nl "Hardened Gentoo (24% translated)")
-   [español](https://wiki.gentoo.org/wiki/Hardened_Gentoo/es "Hardened Gentoo (32% translated)")
-   [français](https://wiki.gentoo.org/wiki/Hardened_Gentoo/fr "Gentoo durci (24% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/Hardened_Gentoo/it "Gentoo Hardened (24% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Hardened_Gentoo/hu "Megerősített Gentoo (92% translated)")
-   [svenska](https://wiki.gentoo.org/wiki/Hardened_Gentoo/sv "Härdad Gentoo (12% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Hardened_Gentoo/ru "Hardened Gentoo (100% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Hardened_Gentoo/zh-cn "加固的Gentoo (Hardened Gentoo) (24% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Hardened_Gentoo/ja "Hardened Gentoo (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Hardened_Gentoo/ko "Hardened Gentoo (24% translated)")

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Hardened "Project:Hardened")][Project](https://wiki.gentoo.org/wiki/Project:Hardened "Project:Hardened")

**Gentoo Hardened** is a Gentoo project that offers multiple additional security services on top of the well-known Gentoo Linux installation.

Whether running an Internet-facing server or a flexible workstation, when dealing with multiple threats it can be advantageous to harden the system further than just automatically applying the latest security patches. *Hardening* a system means taking additional countermeasures against attacks and other risks and is usually a combined set of activities performed on the system.

The base of Gentoo Hardened is a hardened toolchain by enabling specific options in the toolchain (compiler, linker \...) such as forcing position-independent executables (PIE), stack smashing protection and compile-time buffer checks. See the [table](https://wiki.gentoo.org/wiki/Hardened/Toolchain#Changes "Hardened/Toolchain").

Within Gentoo Hardened, several *additional* projects are active that help further harden a Gentoo system through:

-   Enabling [SELinux](https://wiki.gentoo.org/wiki/Hardened_Gentoo/SELinux "Hardened Gentoo/SELinux") extensions in the Linux kernel, which offers a Mandatory Access Control system enhancing the standard Linux permission restrictions.
-   Enabling [Integrity](https://wiki.gentoo.org/wiki/Integrity "Integrity") related technologies, such as Integrity Measurement Architecture, for making systems resilient against tampering.

Of course, this includes the necessary userspace utilities to manage these extensions.

## [[] Switching to a Hardened profile]

** Important**\
Read [relevant documentation](https://wiki.gentoo.org/wiki/Portage/Profiles#Changing_profile "Portage/Profiles") before performing any profile changes.

Select a hardened [profile](https://wiki.gentoo.org/wiki/Portage/Profiles "Portage/Profiles"), so that *package management* will be done in a hardened way.

`root `[`#`]`eselect profile list`

`root `[`#`]`eselect profile set [number of hardened profile]`

`root `[`#`]`source /etc/profile`

By choosing the hardened profile, certain package management settings (masks, USE flags, etc) become default for the system. This applies to many packages, including the toolchain. The toolchain is used for building/compiling programs, and includes: the [gcc](https://wiki.gentoo.org/wiki/Gcc "Gcc") (GNU Compiler Collection), [binutils](https://wiki.gentoo.org/wiki/Binutils "Binutils") (linker, etc.), and the [glibc](https://wiki.gentoo.org/wiki/Glibc "Glibc") (GNU C library). By re-emerging the toolchain, these new default settings will apply to the toolchain, which will allow all future *package compiling* to be done in a hardened way.

`root `[`#`]`emerge --oneshot sys-devel/gcc`

`root `[`#`]`emerge --oneshot sys-devel/binutils sys-libs/glibc`

The above commands rebuilt GCC, which can now be used to compile hardened software. Make sure that the compiler selected is the version just built:

`root `[`#`]`gcc-config -l `

    [1] x86_64-pc-linux-gnu-9.3.0 *
    [2] x86_64-pc-linux-gnu-8.5.0

Finally source the new profile settings:

`root `[`#`]`source /etc/profile`

Now reinstall all packages with the new hardened toolchain:

`root `[`#`]`emerge --emptytree --verbose @world`

If not using the [distribution kernel](https://wiki.gentoo.org/wiki/Project:Distribution_Kernel "Project:Distribution Kernel"), reinstall the kernel sources:

`root `[`#`]`emerge --ask gentoo-sources`

Now configure/compile the sources and add the new kernel to the boot manager (e.g. GRUB).

## [[] See also]

For more information, check out the following resources:

-   [Gentoo Hardened SELinux Project](https://wiki.gentoo.org/wiki/Project:SELinux "Project:SELinux")