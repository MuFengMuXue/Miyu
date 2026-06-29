Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/CPU_FLAGS_*/de "CPU_FLAGS_* (85% translated)")
-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/CPU_FLAGS_*/hu "CPU_FLAGS_* (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/CPU_FLAGS_*/ru "CPU_FLAGS_* (100% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/CPU_FLAGS_*/zh-cn "CPU FLAGS * (62% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/CPU_FLAGS_*/ja "CPU_FLAGS_* (100% translated)")

*Not to be confused with [CFLAGS](https://wiki.gentoo.org/wiki/GCC_optimization "GCC optimization").*

\

**Resources**

[[]][Package information](https://packages.gentoo.org/packages/app-portage/cpuid2cpuflags)

[[]][CPU_FLAGS_ARM](https://gitweb.gentoo.org/repo/gentoo.git/plain/profiles/desc/cpu_flags_arm.desc)

[[]][CPU_FLAGS_PPC](https://gitweb.gentoo.org/repo/gentoo.git/plain/profiles/desc/cpu_flags_ppc.desc)

[[]][CPU_FLAGS_X86](https://gitweb.gentoo.org/repo/gentoo.git/plain/profiles/desc/cpu_flags_x86.desc)

**`CPU_FLAGS_*`** is a [`USE_EXPAND`](https://wiki.gentoo.org/wiki//etc/portage/make.conf#USE_EXPAND "/etc/portage/make.conf") variable containing instruction set and other CPU-specific features. Currently Gentoo supports `CPU_FLAGS_X86` (for **[amd64]** and **[x86]** architectures), `CPU_FLAGS_ARM` (for **[arm]** and **[arm64]** architectures), and `CPU_FLAGS_PPC` (for **[ppc]** and **[ppc64]** architectures).

** See also**\
For more information see the [CPU_FLAGS\_\*](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#CPU_FLAGS_.2A "Handbook:AMD64/Installation/Base") section in the Gentoo Handbook.

## Contents

-   [[1] [Difference between CFLAGS and CPU_FLAGS\_\*]](#Difference_between_CFLAGS_and_CPU_FLAGS_.2A)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Using cpuid2cpuflags]](#Using_cpuid2cpuflags)
    -   [[3.1] [Emerge]](#Emerge)
    -   [[3.2] [Invocation]](#Invocation)
-   [[4] [External resources]](#External_resources)

## [][[] Difference between CFLAGS and CPU_FLAGS\_\*]

A common question is \"what\'s the difference between `CFLAGS` and e.g. `CPU_FLAGS_X86`?\"

`CPU_FLAGS_*` is an example of a [USE_EXPAND](https://wiki.gentoo.org/wiki/USE_EXPAND "USE EXPAND"). It enables specific options in ebuilds which are passed onto the build system. For example, `CPU_FLAGS_X86_SSE2`, if defined for a package, will enable handwritten ASM. These options **enable specific code** which already exists within the package.

`CFLAGS`, on the other hand, are simply used to tell the compiler it is *allowed* to try to *generate* code using such instructions if it is able. It does not mean it will be successful in doing so. e.g. `-msse2` in `CFLAGS` does not mean the compiler will be clever enough to generate SSE2 for a certain function. These options **just permit the compiler to generate certain code with certain instructions**.

It is therefore important to configure `CPU_FLAGS_*` appropriately to get the best performance out of packages.

## [[] Configuration]

These variables need to be set as `CPU_FLAGS_X86` (`CPU_FLAGS_ARM`, `CPU_FLAGS_PPC`) variable in a file in [[/etc/portage/package.use/](https://wiki.gentoo.org/wiki//etc/portage/package.use "/etc/portage/package.use")]:

[FILE] **`/etc/portage/package.use/my-cpu-flags`Setting CPU_FLAGS_X86**

    # This is just an example, please run the 'cpuid2cpuflags' tool to get an appropriate value for each system!
    */* cpu_flags_x86: aes avx avx2 f16c fma3 mmx mmxext pclmul popcnt rdrand sse sse2 sse3 sse4_1 sse4_2 ssse3

When in doubt, consult the flag descriptions using one of the commonly available tools, e.g. [equery uses] from [[[app-portage/gentoolkit]](https://packages.gentoo.org/packages/app-portage/gentoolkit)[]]:

`user `[`$`]`equery uses media-video/ffmpeg`

Most of the flag names match [/proc/cpuinfo] names, with the notable exception of `sse3` which is called `pni` in [/proc/cpuinfo] (please also do not confuse it with distinct `ssse3`).

## [[] Using cpuid2cpuflags]

[[[app-portage/cpuid2cpuflags]](https://packages.gentoo.org/packages/app-portage/cpuid2cpuflags)[]] helps users determine the correct [`CPU_FLAGS_`](https://packages.gentoo.org/useflags/search?q=cpu_flags_) `USE_EXPAND` variables for their CPU architecture.

### [[] Emerge]

`root `[`#`]`emerge --ask app-portage/cpuid2cpuflags`

### [[] Invocation]

`user `[`$`]`cpuid2cpuflags`

    CPU_FLAGS_X86: mmx mmxext sse sse2 sse3

Example to apply globally:

`root `[`#`]`echo "*/* $(cpuid2cpuflags)" > /etc/portage/package.use/00cpu-flags`

## [[] External resources]

-   News item: [new CPU_FLAGS_PPC USE_EXPAND](https://gentoo.org/support/news-items/2019-09-11-cpu_flags_ppc-introduction.html)