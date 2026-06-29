This page contains [[changes](https://wiki.gentoo.org/index.php?title=Kernel&oldid=1418811&diff=1441447)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Kernel/de "Kernel (42% translated)")
-   [English]
-   [Türkçe](https://wiki.gentoo.org/wiki/Kernel/tr "Çekirdek (4% translated)")
-   [español](https://wiki.gentoo.org/wiki/Kernel/es "El Núcleo (Kernel) (65% translated)")
-   [français](https://wiki.gentoo.org/wiki/Kernel/fr "Noyau (84% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/Kernel/it "Kernel (7% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Kernel/hu "Kernel (85% translated)")
-   [polski](https://wiki.gentoo.org/wiki/Kernel/pl "Kernel/pl (0% translated)")
-   [português do Brasil](https://wiki.gentoo.org/wiki/Kernel/pt-br "Kernel (7% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Kernel/ru "Ядро (62% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Kernel/zh-cn "内核 (42% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Kernel/ja "カーネル (98% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Kernel/ko "Kernel (7% translated)")

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Kernel "Project:Kernel")][Project](https://wiki.gentoo.org/wiki/Project:Kernel "Project:Kernel")

[[]][Home](https://www.kernel.org)

[[]][Official documentation](https://www.kernel.org/doc/html/latest/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Linux_kernel "wikipedia:Linux kernel")

[[]][GitHub](https://github.com/torvalds/linux)

[[]][GitWeb](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git)

[[]][Bugs (upstream)](https://bugzilla.kernel.org/)

[![](/images/thumb/a/af/Tux.png/250px-Tux.png)](https://wiki.gentoo.org/wiki/File:Tux.png)

[](https://wiki.gentoo.org/wiki/File:Tux.png "Enlarge")

Tux, the Linux mascot.

The **[Linux](https://en.wikipedia.org/wiki/Linux_kernel "wikipedia:Linux kernel") kernel** is a central part of the Gentoo [operating system (OS)](https://en.wikipedia.org/wiki/operating_system "wikipedia:operating system"). It provides essential OS facilities such as [device drivers](https://en.wikipedia.org/wiki/Device_driver "wikipedia:Device driver"), [virtual consoles](https://wiki.gentoo.org/wiki/Terminal_emulator#Virtual_consoles_and_switching "Terminal emulator"), [memory management](https://en.wikipedia.org/wiki/memory_management "wikipedia:memory management"), [task scheduling](https://en.wikipedia.org/wiki/Scheduling_(computing) "wikipedia:Scheduling (computing)"), [inter-process communication](https://en.wikipedia.org/wiki/inter-process_communication "wikipedia:inter-process communication"), [virtual filesystems](https://en.wikipedia.org/wiki/Virtual_file_system "wikipedia:Virtual file system"), etc.

Though Linux is a [monolithic kernel](https://en.wikipedia.org/wiki/monolithic_kernel "wikipedia:monolithic kernel"), its [modular design](https://en.wikipedia.org/wiki/Loadable_kernel_module "wikipedia:Loadable kernel module") means that code will only ever be loaded if required, allowing modules to be available without affecting performance or memory usage. Linux kernel deployments can therefore provide many device drivers and services, with little to no penalty on performance: unneeded modules will simply be ignored.

The kernel is predominantly written in [C](https://wiki.gentoo.org/wiki/C "C") and also uses [assembly](https://wiki.gentoo.org/wiki/Assembly_Language "Assembly Language") and [Rust](https://wiki.gentoo.org/wiki/Rust "Rust") code, for example.

** See also**\
See also the [handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Kernel "Handbook:AMD64/Installation/Kernel") on installing and setting up a kernel.

## Contents

-   [[1] [Which kernel to install?]](#Which_kernel_to_install.3F)
    -   [[1.1] [Distribution kernels]](#Distribution_kernels)
        -   [[1.1.1] [gentoo-kernel-bin]](#gentoo-kernel-bin)
        -   [[1.1.2] [gentoo-kernel]](#gentoo-kernel)
            -   [[1.1.2.1] [Code snippet]](#Code_snippet)
            -   [[1.1.2.2] [savedconfig]](#savedconfig)
    -   [[1.2] [gentoo-sources]](#gentoo-sources)
-   [[2] [Installing kernel source code]](#Installing_kernel_source_code)
    -   [[2.1] [USE flags]](#USE_flags)
    -   [[2.2] [Emerge]](#Emerge)
        -   [[2.2.1] [Alternative kernels]](#Alternative_kernels)
        -   [[2.2.2] [Searching all kernel packages]](#Searching_all_kernel_packages)
-   [[3] [Managing the kernel]](#Managing_the_kernel)
    -   [[3.1] [Configuration]](#Configuration)
    -   [[3.2] [Upgrade]](#Upgrade)
    -   [[3.3] [Removal]](#Removal)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Kernel configuration support]](#Kernel_configuration_support)
    -   [[4.2] [Kernel command-line parameters]](#Kernel_command-line_parameters)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

### [][[] Which kernel to install?]

Gentoo provides a choice of methods to get a kernel up and running, from a standard binary kernel as would be supplied by most distributions to a custom configured and compiled kernel.

** Tip**\
When starting out, the [gentoo-kernel-bin](https://wiki.gentoo.org/wiki/Project:Distribution_Kernel "Project:Distribution Kernel") provides a quick and easy way to get a kernel up and running, while still providing a light, high performance kernel (just like any modern distribution would). Once a system is installed and functioning correctly, a different kernel may be selected if needed. The [[[sys-kernel/gentoo-kernel-bin]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel-bin)[]] can be kept around in case of issues booting a custom kernel.

#### [[] Distribution kernels]

The [distribution kernel project](https://wiki.gentoo.org/wiki/Project:Distribution_Kernel "Project:Distribution Kernel") provides packages to install and manage kernels through [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"). These kernels are compiled (if needed) and installed with just an [emerge] command like any other package, which can lessen the administrative burden. Kernel updates are performed when [updating the system](https://wiki.gentoo.org/wiki/Upgrading_Gentoo "Upgrading Gentoo") (e.g. [emerge -avuDN \@world]).

These kernels come with a default configuration that should \"just work\" for most systems. For users not interested in configuring their own kernel from scratch, these kernels can get things up and running quicker:

##### [[] gentoo-kernel-bin]

The [[[sys-kernel/gentoo-kernel-bin]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel-bin)[]] is a binary package containing a precompiled kernel, allowing for faster installation. This package is a precompiled version of the gentoo-kernel package with a default configuration.

##### [[] gentoo-kernel]

The [[[sys-kernel/gentoo-kernel]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel)[]] package provides a kernel that will be compiled and installed when the package is emerged. This comes with a default configuration that should work out of the box on most systems.

[[[sys-kernel/gentoo-kernel]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel)[]] can also be configured to use a custom kernel config which make automation a lot more simpler when compared to [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]].

Below are some examples of this:

###### [Code snippet]

When only one or two features of a kernel config needs changing it is possible to apply the change using [/etc/kernel/config.d].

This could be something like applying CONFIG_X86_NATIVE_CPU=y to tune the distribution kernel it is being built on.

This process is described in more detail in the [Distribution kernel config.d](https://wiki.gentoo.org/wiki/Distribution_Kernel#Using_.2Fetc.2Fkernel.2Fconfig.d "Distribution Kernel") section

###### [savedconfig]

When a completely custom kernel config is required then it is usally better to use the savedconfig option.

This allows a kernel config made with [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]] to be transferred to the distribution and kernel allows that config to applied to future updates.

This is viewed as a better way to manage the kernel in Gentoo by some users, as it gives users access to the feature in Portage to rebuild out of tree modules such as [[[x11-drivers/nvidia-driver]](https://packages.gentoo.org/packages/x11-drivers/nvidia-driver)[]] on every kernel update without being manually called for.

This process is described in more detail in the [Distribution kernel savedconfig](https://wiki.gentoo.org/wiki/Distribution_Kernel#Using_savedconfig "Distribution Kernel") section

** Important**\
The rest of this article concerns installation using the [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]] package. See the [distribution kernel](https://wiki.gentoo.org/wiki/Distribution_Kernel "Distribution Kernel") for further information on distribution kernels.

#### [[] gentoo-sources]

When manually compiling kernel sources, Gentoo recommends the [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]] package for most users. Its stable versions follow the long term stable (LTS) kernels from upstream kernel.org.

## [[] Installing kernel source code]

To obtain a kernel, it is necessary to install the kernel source code. The recommended kernel sources for a Gentoo desktop system are [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]]. These are maintained by the Gentoo developers, and patched when necessary to fix security vulnerabilities and functional problems, as well as to improve compatibility with rare system architectures.

### [[] USE flags]

### [USE flags for] [sys-kernel/gentoo-sources](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources) [[]] [Full sources including the Gentoo patchset for the 7.0 kernel tree]

  --------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------
  [`build`](https://packages.gentoo.org/useflags/build)                 !!internal use only!! DO NOT SET THIS FLAG YOURSELF!, used for creating build images and the first half of bootstrapping \[make stage1\]
  [`experimental`](https://packages.gentoo.org/useflags/experimental)   Apply experimental patches; for more information, see \"https://wiki.gentoo.org/wiki/Project:Kernel/Experimental\".
  [`symlink`](https://packages.gentoo.org/useflags/symlink)             Force kernel ebuilds to automatically update the /usr/src/linux symlink
  --------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-25 21:38] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [[] Emerge]

To install [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]]:

`root `[`#`]`emerge --ask sys-kernel/gentoo-sources`

#### [[] Alternative kernels]

There are many other kernel packages in the Portage tree. For details on many of these, see the [kernel packages](https://wiki.gentoo.org/wiki/Kernel/Packages "Kernel/Packages") article. Further help on choosing a kernel can be found in developer Greg Kroah-Hartman\'s article [What Stable Kernel Should I Use?](http://kroah.com/log/blog/2018/08/24/what-stable-kernel-should-i-use/).

#### [[] Searching all kernel packages]

A full list of kernel sources with short descriptions can be found by searching with [emerge]:

`root `[`#`]`emerge --search sources`

## [[] Managing the kernel]

### [[] Configuration]

[Understanding manual configuration](https://wiki.gentoo.org/wiki/Kernel/Configuration "Kernel/Configuration")

<!-- -->

[Applying manual configuration](https://wiki.gentoo.org/wiki/Kernel/Gentoo_Kernel_Configuration_Guide "Kernel/Gentoo Kernel Configuration Guide")

<!-- -->

[Deblobbing](https://wiki.gentoo.org/wiki/Kernel/Deblobbing "Kernel/Deblobbing")

<!-- -->

[Security](https://wiki.gentoo.org/wiki/Security_Handbook/Kernel_security "Security Handbook/Kernel security")

<!-- -->

[Modules](https://wiki.gentoo.org/wiki/Kernel_Modules "Kernel Modules")

<!-- -->

[Optimization](https://wiki.gentoo.org/wiki/Kernel/Optimization "Kernel/Optimization")

<!-- -->

[Command-line parameters](https://wiki.gentoo.org/wiki/Kernel/Command-line_parameters "Kernel/Command-line parameters")

### [[] Upgrade]

[Kernel upgrade](https://wiki.gentoo.org/wiki/Kernel/Upgrade "Kernel/Upgrade")

### [[] Removal]

[Kernel removal](https://wiki.gentoo.org/wiki/Kernel/Removal "Kernel/Removal")

## [[] Troubleshooting]

### [[] Kernel configuration support]

See the [IKCONFIG support](https://wiki.gentoo.org/wiki/Kernel/IKCONFIG_support "Kernel/IKCONFIG support") sub-article.

### [[] Kernel command-line parameters]

When booting from a bootloader, the Linux kernel can accept command-line parameters to change its behavior. This can help, for example, in troubleshooting the kernel at boot time, or to blacklist a certain module that should not be loading. See Gentoo\'s [Kernel/Command-line parameters](https://wiki.gentoo.org/wiki/Kernel/Command-line_parameters "Kernel/Command-line parameters") article for more details.

Kernel.org has a nicely formatted list of available [kernel command-line parameters](https://www.kernel.org/doc/html/latest/admin-guide/kernel-parameters.html) in their admin guide.

## [[] See also]

-   [fwupd](https://wiki.gentoo.org/wiki/Fwupd "Fwupd") --- a daemon that provides a safe, reliable way of applying firmware updates on Linux.
-   [Handbook:AMD64/Installation/Kernel](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Kernel "Handbook:AMD64/Installation/Kernel") --- handbook page about installing and setting up a kernel
-   [Linux firmware](https://wiki.gentoo.org/wiki/Linux_firmware "Linux firmware") --- is a package distributed alongside the Linux kernel that contains firmware [binary blobs](https://en.wikipedia.org/wiki/binary_blob "wikipedia:binary blob") necessary for partial or full functionality of certain hardware devices.
-   [The kernel category](https://wiki.gentoo.org/wiki/Category:Kernel "Category:Kernel") --- all the kernel related articles on the wiki.
-   [The hardware category](https://wiki.gentoo.org/wiki/Category:Hardware "Category:Hardware") --- lists of hardware stacks with associated kernel configurations.

## [[] External resources]

-   [planet.kernel.org](http://planet.kernel.org/) - Blogs related to the Linux kernel.
-   [kernelnewbies.org](https://kernelnewbies.org/) - A \"community of aspiring Linux kernel developers who work to improve their kernels, as well as more experienced developers willing to share their knowledge\".
-   [kernel.org/doc/](https://www.kernel.org/doc/) - Official comprehensive documentation for the Linux kernel.
-   [What Stable Kernel Should I Use?](http://kroah.com/log/blog/2018/08/24/what-stable-kernel-should-i-use/) - An article by kernel developer Greg Kroah-Hartman.
-   [Building the kernel as root can be harmful](https://forums.gentoo.org/viewtopic-t-1064076.html)
-   [The Linux Kernel Module Programming Guide](https://github.com/sysprog21/lkmpg/)