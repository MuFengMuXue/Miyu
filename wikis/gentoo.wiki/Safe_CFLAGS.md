Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Safe_CFLAGS/hu "Biztonságok CFLAGS (94% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Safe_CFLAGS/ja "安全な CFLAGS (92% translated)")

[   Note to translators] []

This page was improperly translated to Italian. It would be helpful if someone who can do Italian translations could use the content from [this page](https://wiki.gentoo.org/wiki/User:Suricata/Safe_CFLAGS-improper_translation-it "User:Suricata/Safe CFLAGS-improper translation-it") to recreate an Italian translation using the standard wiki translation framework (click translation link at top of this page), then we can delete that imporperly translated page. See [Help:Translating](https://wiki.gentoo.org/wiki/Help:Translating "Help:Translating").

*Not to be confused with [CPU_FLAGS\_\*](https://wiki.gentoo.org/wiki/CPU_FLAGS_* "CPU FLAGS *").*

This article provides a summary of \"safe\" settings for [CFLAGS](https://en.wikipedia.org/wiki/CFLAGS "wikipedia:CFLAGS") on Gentoo Linux.

Default CFLAGS can be [set in make.conf](https://wiki.gentoo.org/wiki/Make.conf#CFLAGS_and_CXXFLAGS "Make.conf") for Gentoo systems. CFLAGS can also be [specified per-package](https://wiki.gentoo.org/wiki/Knowledge_Base:Overriding_environment_variables_per_package "Knowledge Base:Overriding environment variables per package").

** See also**\
For more information see [CFLAGS and CXXFLAGS](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Stage#CFLAGS_and_CXXFLAGS "Handbook:AMD64/Installation/Stage") in the Gentoo Handbook, and the [GCC optimization](https://wiki.gentoo.org/wiki/GCC_optimization "GCC optimization") article. See also the [FAQ](https://wiki.gentoo.org/wiki/FAQ#Things_are_really_unstable_when_using_.27-O9_-ffast-math_-fomit-frame-pointer.27_optimizations._What_gives.3F "FAQ").

## Contents

-   [[1] [Automatic CPU detection by the compiler]](#Automatic_CPU_detection_by_the_compiler)
-   [[2] [Determining CPU type in order to set CFLAGS manually]](#Determining_CPU_type_in_order_to_set_CFLAGS_manually)
    -   [[2.1] [CPU detection with resolve-march-native]](#CPU_detection_with_resolve-march-native)
    -   [[2.2] [Reporting the CPU type with /proc/cpuinfo]](#Reporting_the_CPU_type_with_.2Fproc.2Fcpuinfo)
-   [[3] [Safe CFLAGS list]](#Safe_CFLAGS_list)
    -   [[3.1] [x86/amd64]](#x86.2Famd64)
        -   [[3.1.1] [Generic psABI levels]](#Generic_psABI_levels)
        -   [[3.1.2] [Intel]](#Intel)
            -   [[3.1.2.1] [Alder Lake]](#Alder_Lake)
            -   [[3.1.2.2] [Skylake, Kaby Lake, Kaby Lake R, Coffee Lake, Comet Lake]](#Skylake.2C_Kaby_Lake.2C_Kaby_Lake_R.2C_Coffee_Lake.2C_Comet_Lake)
            -   [[3.1.2.3] [Broadwell]](#Broadwell)
            -   [[3.1.2.4] [Haswell]](#Haswell)
            -   [[3.1.2.5] [Ivy Bridge]](#Ivy_Bridge)
            -   [[3.1.2.6] [Sandy Bridge]](#Sandy_Bridge)
            -   [[3.1.2.7] [Nehalem]](#Nehalem)
            -   [[3.1.2.8] [Westmere]](#Westmere)
            -   [[3.1.2.9] [Intel Core]](#Intel_Core)
            -   [[3.1.2.10] [Older microarchitecture]](#Older_microarchitecture)
        -   [[3.1.3] [AMD]](#AMD)
            -   [[3.1.3.1] [Ryzen (Zen family)]](#Ryzen_.28Zen_family.29)
            -   [[3.1.3.2] [A6/A8/A9/A10/A12-8XXX/9XXX (Excavator)]](#A6.2FA8.2FA9.2FA10.2FA12-8XXX.2F9XXX_.28Excavator.29)
            -   [[3.1.3.3] [A4/A6/A8/A10-7XXX/8XXX (Steamroller)]](#A4.2FA6.2FA8.2FA10-7XXX.2F8XXX_.28Steamroller.29)
            -   [[3.1.3.4] [E1/E2-XXXX, A4/A6/A8/A10-XXXX (Jaguar, Puma)]](#E1.2FE2-XXXX.2C_A4.2FA6.2FA8.2FA10-XXXX_.28Jaguar.2C_Puma.29)
            -   [[3.1.3.5] [A4/A6/A8/A10-4XXX/5XXX/6XXX (Piledriver)]](#A4.2FA6.2FA8.2FA10-4XXX.2F5XXX.2F6XXX_.28Piledriver.29)
            -   [[3.1.3.6] [FX-XXXX]](#FX-XXXX)
            -   [[3.1.3.7] [Z-XX, C-X0, E-XX0, E1/E2-1X00, E2-2000 (Bobcat)]](#Z-XX.2C_C-X0.2C_E-XX0.2C_E1.2FE2-1X00.2C_E2-2000_.28Bobcat.29)
            -   [[3.1.3.8] [A4/A6/A8-3XXX/3XXXM (12h)]](#A4.2FA6.2FA8-3XXX.2F3XXXM_.2812h.29)
            -   [[3.1.3.9] [Phenom/Phenom II, Athlon II, Sempron (10h)]](#Phenom.2FPhenom_II.2C_Athlon_II.2C_Sempron_.2810h.29)
            -   [[3.1.3.10] [Older microarchitectures]](#Older_microarchitectures)
    -   [[3.2] [ARM]](#ARM)
        -   [[3.2.1] [Cortex-A]](#Cortex-A)
            -   [[3.2.1.1] [ARMv7-A/Cortex-A9 MPCore]](#ARMv7-A.2FCortex-A9_MPCore)
            -   [[3.2.1.2] [ARMv8-A/BCM2837]](#ARMv8-A.2FBCM2837)
        -   [[3.2.2] [ARM11]](#ARM11)
            -   [[3.2.2.1] [ARMv6/ARM1176JZF-S]](#ARMv6.2FARM1176JZF-S)
            -   [[3.2.2.2] [ARMv6/ARM1136JF-S]](#ARMv6.2FARM1136JF-S)
    -   [[3.3] [PowerPC / PowerPC 64]](#PowerPC_.2F_PowerPC_64)
        -   [[3.3.1] [POWER8]](#POWER8)
        -   [[3.3.2] [Cell]](#Cell)
        -   [[3.3.3] [PPC 970 (G5)]](#PPC_970_.28G5.29)
        -   [[3.3.4] [G4 (PPC 74xx)]](#G4_.28PPC_74xx.29)
            -   [[3.3.4.1] [PPC 7450 family]](#PPC_7450_family)
            -   [[3.3.4.2] [PPC 7400 family]](#PPC_7400_family)
        -   [[3.3.5] [G3 (PPC 7XX)]](#G3_.28PPC_7XX.29)
    -   [[3.4] [RISC-V]](#RISC-V)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Automatic CPU detection by the compiler]

A recommended default choice for `CFLAGS` or `CXXFLAGS` is to use `-march=native`. This enables auto-detection of the CPU\'s architecture. A possible entry might look like:

[FILE] **`/etc/portage/make.conf`**

    COMMON_FLAGS="-O2 -pipe -march=native"
    CFLAGS="$"
    CXXFLAGS="$"

** Warning**\
Do **not** use `-march=native` or `-mtune=native` in the `CFLAGS` or `CXXFLAGS` variables of [make.conf] when compiling with [[distcc](https://wiki.gentoo.org/wiki/Distcc#-march.3Dnative "Distcc")]. Consult the [distcc](https://wiki.gentoo.org/wiki/Distcc "Distcc") page about how to set up `CFLAGS`/`CXXFLAGS` correctly.

To see what GCC detects \"native\" to be for certain system in particular, the following command can be run:

`user `[`$`]`gcc -v -E -x c /dev/null -o /dev/null -march=native 2>&1 | grep /cc1 | grep mtune`

The internal translation of `-march=native` will be visible in the output. In some cases, if the CPU is unknown to GCC\'s detection model, a suboptimal `-mtune=generic` (or even no `-mtune`) will be visible. In this case, select relevant `-mtune=` from manual. In some other cases there are same to detected `-march=` or common `-mtune=intel` for (too) modern Intel CPUs.

[The cpu-type may also be detected with glibc.](https://wiki.gentoo.org/wiki/GCC_optimization#cpu-type "GCC optimization")

Also possible suboptimal `-march=native` detection - full `l2-cache-size` to single CPU thread on multi-core CPUs. Currently it used only for prefetching, but sometimes good choice to fallback to default `--param=l2-cache-size=512` or own calculated value - to reduce cache concurrency on high SMP load. But this is in theory and not for all tasks - do nothing if unsure.

Additional information can be found at the [GCC optimization](https://wiki.gentoo.org/wiki/GCC_optimization "GCC optimization") page.

## [Determining CPU type in order to set CFLAGS manually]

These tools can report system CPU information that can then be matched a CPU from the list further down this page, to get some suggested `CFLAGS` that are \"safe\" for that system.

These settings should be used, especially when unsure which `CFLAGS` the processor needs.

### [CPU detection with resolve-march-native]

A tool exists to *automagically* determine `-march=native` resolution values: [[[app-misc/resolve-march-native]](https://packages.gentoo.org/packages/app-misc/resolve-march-native)[]]. After installing it, issue:

`user `[`$`]`resolve-march-native`

### [][Reporting the CPU type with /proc/cpuinfo]

To identify the model of the CPU, take a look inside [/proc/cpuinfo] for the \"cpu family\" and \"model\" numbers like so:

`user `[`$`]`grep -m1 -A3 "vendor_id" /proc/cpuinfo`

## [Safe CFLAGS list]

** Warning**\
Since virtual machine hypervisors (*WSL*, *VirtualBox*, etc.) disable certain instruction sets (`sgx`, `xsaves`, `xsaveopt`, etc.) on the CPU from being used within the virtual machine, the values for `CFLAGS` listed here **will very likely not work and lead to a broken system** on said virtual machine. You should only really use these values for `CFLAGS` on **real hardware** instead of virtual machines.

### [][x86/amd64]

#### [Generic psABI levels]

If using a [distcc](https://wiki.gentoo.org/wiki/Distcc "Distcc") farm with slightly different CPUs, it might make more sense to generate code that is just old enough to work for all of them, without bogging down to the *really* generic code. The psABI microarchitecture levels aims to provide just that for common eras of amd64 CPUs. See [Wikipedia:x86-64#Microarchitecture_levels](https://en.wikipedia.org/wiki/x86-64#Microarchitecture_levels "wikipedia:x86-64") for a description of the levels.

#### [Intel]

##### [Alder Lake]

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| **Core i3/i5/i7 12th Gen**                                            |                                                                                                                                                                                |
| :::                                                                   | ::: box-caption                                                                                                                                                                |
|                                                                       | [FILE] **`/etc/portage/make.conf`** |
| :::  | :::                                                                                                                                                                            |
|     vendor_id       : GenuineIntel                                    |                                                                                                                                                                                |
|     cpu family      : 6                                               | :::                                                                                                           |
|     model           : 154                                             |     COMMON_FLAGS="-march=alderlake -O2 -pipe"                                                                                                                                  |
|     model name      : 12th Gen Intel(R) Core(TM) i7-1260P             |     CFLAGS="$"                                                                                                                                                   |
| :::                                                                   |     CXXFLAGS="$"                                                                                                                                                 |
|                                                                       | :::                                                                                                                                                                            |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

##### [][Skylake, Kaby Lake, Kaby Lake R, Coffee Lake, Comet Lake]

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| **Core i3/i5/i7 and Xeon E3/E5 \*V5**                                 |                                                                                                                                                                                |
| :::                                                                   | ::: box-caption                                                                                                                                                                |
|                                                                       | [FILE] **`/etc/portage/make.conf`** |
| :::  | :::                                                                                                                                                                            |
|     vendor_id       : GenuineIntel                                    |                                                                                                                                                                                |
|     cpu family      : 6                                               | :::                                                                                                           |
|     model           : 94                                              |     COMMON_FLAGS="-march=skylake -O2 -pipe"                                                                                                                                    |
|     model name      : Intel(R) Core(TM) i7-6700K CPU @ 4.00GHz        |     CFLAGS="$"                                                                                                                                                   |
|     ...                                                               |     CXXFLAGS="$"                                                                                                                                                 |
|     model           : 165                                             | :::                                                                                                                                                                            |
|     model name      : Intel(R) Core(TM) i5-10400F CPU @ 2.90GHz       |                                                                                                                                                                                |
| :::                                                                   |                                                                                                                                                                                |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

** Warning**\
Even though they fit the family and model, this set of `CFLAGS` does *NOT* work for *Skylake Pentium CPUs* (e. g. G4400, or J5005) producing invalid code, which may break the system. Use `-march=native` for these systems instead.

##### [Broadwell]

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| **Core i3/i5/i7 and Xeon E3/E5 \*V4**                                 |                                                                                                                                                                                |
| :::                                                                   | ::: box-caption                                                                                                                                                                |
|                                                                       | [FILE] **`/etc/portage/make.conf`** |
| :::  | :::                                                                                                                                                                            |
|     vendor_id       : GenuineIntel                                    |                                                                                                                                                                                |
|     cpu family      : 6                                               | :::                                                                                                           |
|     model           : 79                                              |     COMMON_FLAGS="-march=broadwell -O2 -pipe"                                                                                                                                  |
|     model name      : Intel(R) Xeon(R) CPU E5-2683 v4 @ 2.10GHz       |     CFLAGS="$"                                                                                                                                                   |
|     …                                                                 |     CXXFLAGS="$"                                                                                                                                                 |
|     model           : 79                                              | :::                                                                                                                                                                            |
|     model name      : Intel(R) Core(TM) i7-5650U CPU @ 2.20GHz        |                                                                                                                                                                                |
| :::                                                                   |                                                                                                                                                                                |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

##### [Haswell]

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| **Core i3/i5/i7 and Xeon E3/E5/E7 \*V3**                              |                                                                                                                                                                                |
| :::                                                                   | ::: box-caption                                                                                                                                                                |
|                                                                       | [FILE] **`/etc/portage/make.conf`** |
| :::  | :::                                                                                                                                                                            |
|     vendor_id      : GenuineIntel                                     |                                                                                                                                                                                |
|     cpu family     : 6                                                | :::                                                                                                           |
|     model          : 60                                               |     COMMON_FLAGS="-march=haswell -O2 -pipe"                                                                                                                                    |
|     model name     : Intel(R) Xeon(R) CPU E3-1271 v3 @ 3.60GHz        |     CFLAGS="$"                                                                                                                                                   |
|     …                                                                 |     CXXFLAGS="$"                                                                                                                                                 |
|     model          : 60                                               | :::                                                                                                                                                                            |
|     model name     : Intel(R) Core(TM) i7-4770 CPU @ 3.40GHz          |                                                                                                                                                                                |
| :::                                                                   |                                                                                                                                                                                |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

##### [Ivy Bridge]

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| **Core i3/i5/i7 and Xeon E3/E5/E7 \*V2**                              |                                                                                                                                                                                |
| :::                                                                   | ::: box-caption                                                                                                                                                                |
|                                                                       | [FILE] **`/etc/portage/make.conf`** |
| :::  | :::                                                                                                                                                                            |
|     vendor_id       : GenuineIntel                                    |                                                                                                                                                                                |
|     cpu family      : 6                                               | :::                                                                                                           |
|     model           : 58                                              |     COMMON_FLAGS="-march=ivybridge -O2 -pipe"                                                                                                                                  |
|     model name      : Intel(R) Core(TM) i7-3610QM CPU @ 2.30GHz       |     CFLAGS="$"                                                                                                                                                   |
| :::                                                                   |     CXXFLAGS="$"                                                                                                                                                 |
|                                                                       | :::                                                                                                                                                                            |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| **Pentium**                                                           |                                                                                                                                                                                |
| :::                                                                   | ::: box-caption                                                                                                                                                                |
|                                                                       | [FILE] **`/etc/portage/make.conf`** |
| :::  | :::                                                                                                                                                                            |
|     vendor_id    : GenuineIntel                                       |                                                                                                                                                                                |
|     cpu family  : 6                                                   | :::                                                                                                           |
|     model       : 58                                                  |     COMMON_FLAGS="-march=ivybridge -mno-avx -mno-aes -mno-rdrnd -O2 -pipe"                                                                                                     |
|     model name  : Intel(R) Pentium(R) CPU G2020 @ 2.90GHz             |     CFLAGS="$"                                                                                                                                                   |
| :::                                                                   |     CXXFLAGS="$"                                                                                                                                                 |
|                                                                       | :::                                                                                                                                                                            |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

##### [Sandy Bridge]

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| **Core i3/i5/i7 and Xeon E3/E5/E7**                                   |                                                                                                                                                                                |
| :::                                                                   | ::: box-caption                                                                                                                                                                |
|                                                                       | [FILE] **`/etc/portage/make.conf`** |
| :::  | :::                                                                                                                                                                            |
|     vendor_id    : GenuineIntel                                       |                                                                                                                                                                                |
|     cpu family  : 6                                                   | :::                                                                                                           |
|     …                                                                 |     COMMON_FLAGS="-march=sandybridge -O2 -pipe"                                                                                                                                |
|     model       : 42                                                  |     CFLAGS="$"                                                                                                                                                   |
|     model name  : Intel(R) Core(TM) i5-2400 CPU @ 3.10GHz             |     CXXFLAGS="$"                                                                                                                                                 |
|     …                                                                 | :::                                                                                                                                                                            |
|     model       : 45                                                  |                                                                                                                                                                                |
|     model name  : Intel(R) Core(TM) i7-3930K CPU @ 3.20GHz            |                                                                                                                                                                                |
|     …                                                                 |                                                                                                                                                                                |
|     model       : 42                                                  |                                                                                                                                                                                |
|     model name  : Intel(R) Xeon(R) CPU E31245 @ 3.30GHz               |                                                                                                                                                                                |
|     …                                                                 |                                                                                                                                                                                |
|     model           : 45                                              |                                                                                                                                                                                |
|     model name      : Intel(R) Xeon(R) CPU E5-2407 0 @ 2.20GHz        |                                                                                                                                                                                |
| :::                                                                   |                                                                                                                                                                                |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| **Pentium**                                                           |                                                                                                                                                                                |
| :::                                                                   | ::: box-caption                                                                                                                                                                |
|                                                                       | [FILE] **`/etc/portage/make.conf`** |
| :::  | :::                                                                                                                                                                            |
|     vendor_id    : GenuineIntel                                       |                                                                                                                                                                                |
|     cpu family  : 6                                                   | :::                                                                                                           |
|     model       : 42                                                  |     COMMON_FLAGS="-march=sandybridge -mno-avx -mno-aes -mno-rdrnd -O2 -pipe"                                                                                                   |
|     model name  : Intel(R) Pentium(R) CPU B960 @ 2.20GHz              |     CFLAGS="$"                                                                                                                                                   |
| :::                                                                   |     CXXFLAGS="$"                                                                                                                                                 |
|                                                                       | :::                                                                                                                                                                            |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

##### [Nehalem]

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| **Core i3/i5/i7**                                                     |                                                                                                                                                                                |
| :::                                                                   | ::: box-caption                                                                                                                                                                |
|                                                                       | [FILE] **`/etc/portage/make.conf`** |
| :::  | :::                                                                                                                                                                            |
|     vendor_id  : GenuineIntel                                         |                                                                                                                                                                                |
|     cpu family  : 6                                                   | :::                                                                                                           |
|     model       : 30                                                  |     COMMON_FLAGS="-march=nehalem -O2 -pipe"                                                                                                                                    |
|     model name  : Intel(R) Core(TM) i5-750 CPU @ 2.66GHz              |     CFLAGS="$"                                                                                                                                                   |
| :::                                                                   |     CXXFLAGS="$"                                                                                                                                                 |
|                                                                       | :::                                                                                                                                                                            |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

##### [Westmere]

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| **Core i3/i5/i7**                                                     |                                                                                                                                                                                |
| :::                                                                   | ::: box-caption                                                                                                                                                                |
|                                                                       | [FILE] **`/etc/portage/make.conf`** |
| :::  | :::                                                                                                                                                                            |
|     vendor_id  : GenuineIntel                                         |                                                                                                                                                                                |
|     cpu family  : 6                                                   | :::                                                                                                           |
|     model       : 37                                                  |     COMMON_FLAGS="-march=westmere -O2 -pipe"                                                                                                                                   |
|     model name  : Intel(R) Core(TM) i5-650 CPU @ 3.20GHz              |     CFLAGS="$"                                                                                                                                                   |
| :::                                                                   |     CXXFLAGS="$"                                                                                                                                                 |
|                                                                       | :::                                                                                                                                                                            |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

** Note**\
It may be required to add *-mno-aes -mno-pclmul*, especially for i3 (enabled by default). No output means not supported:

`user `[`$`]`grep -m1 -e aes -e pclmulqdq /proc/cpuinfo`

##### [Intel Core]

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| **Intel Core**                                                        |                                                                                                                                                                                |
| :::                                                                   | ::: box-caption                                                                                                                                                                |
|                                                                       | [FILE] **`/etc/portage/make.conf`** |
| :::  | :::                                                                                                                                                                            |
|     vendor_id       : GenuineIntel                                    |                                                                                                                                                                                |
|     cpu family      : 6                                               | :::                                                                                                           |
|     …                                                                 |     COMMON_FLAGS="-march=core2 -O2 -pipe"                                                                                                                                      |
|     model       : 15                                                  |     CFLAGS="$"                                                                                                                                                   |
|     model name  : Intel(R) Core(TM)2 Duo CPU     T7500  @ 2.20GHz     |     CXXFLAGS="$"                                                                                                                                                 |
|     …                                                                 | :::                                                                                                                                                                            |
|     model           : 15                                              |                                                                                                                                                                                |
|     model name      : Intel(R) Xeon(R) CPU            3040  @ 1.86GHz |                                                                                                                                                                                |
| :::                                                                   |                                                                                                                                                                                |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

##### [Older microarchitecture]

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| **Pentium M (Dothan)**                                                |                                                                                                                                                                                |
| :::                                                                   | ::: box-caption                                                                                                                                                                |
|                                                                       | [FILE] **`/etc/portage/make.conf`** |
| :::  | :::                                                                                                                                                                            |
|     vendor_id : GenuineIntel                                          |                                                                                                                                                                                |
|     cpu family  : 6                                                   | :::                                                                                                           |
|     model       : 13                                                  |     COMMON_FLAGS="-O2 -march=pentium-m -pipe"                                                                                                                                  |
|     model name  : Intel(R) Pentium(R) M processor 2.13GHz             |     CFLAGS="$"                                                                                                                                                   |
| :::                                                                   |     CXXFLAGS="$"                                                                                                                                                 |
|                                                                       | :::                                                                                                                                                                            |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| **Pentium 4 (Prescott)**                                              |                                                                                                                                                                                |
| :::                                                                   | ::: box-caption                                                                                                                                                                |
|                                                                       | [FILE] **`/etc/portage/make.conf`** |
| :::  | :::                                                                                                                                                                            |
|     vendor_id   : GenuineIntel                                        |                                                                                                                                                                                |
|     cpu family  : 15                                                  | :::                                                                                                           |
|     model       : 4                                                   |     COMMON_FLAGS="-O2 -march=nocona -pipe"                                                                                                                                     |
|     model name  : Intel(R) Pentium(R) 4 CPU XXXGHz                    |     CFLAGS="$"                                                                                                                                                   |
| :::                                                                   |     CXXFLAGS="$"                                                                                                                                                 |
|                                                                       | :::                                                                                                                                                                            |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

64-bit capable models: 505, 505J, 506, 511, 516, 517, 519K, 521, 524, 531, 541, 551, 561, 571, 6xx and the 3.73(3)GHz Pentium 4 Extreme Edition.

** Note**\
Check the /proc/cpuinfo for the lm flag to detect 64-bit CPUs:

`user `[`$`]`grep lm /proc/cpuinfo`

The cpuid model (4 vs 3) is **not** an indicator of 64-bit compatibility; there are 32-bit family15/model4 CPUs!

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| **All other Prescotts**                                               |                                                                                                                                                                                |
| :::                                                                   | ::: box-caption                                                                                                                                                                |
|                                                                       | [FILE] **`/etc/portage/make.conf`** |
| :::  | :::                                                                                                                                                                            |
|     vendor_id    : GenuineIntel                                       |                                                                                                                                                                                |
|     cpu family  : 15                                                  | :::                                                                                                           |
|     model       : 3                                                   |     COMMON_FLAGS="-O2 -march=prescott -pipe"                                                                                                                                   |
|     model name  : Intel(R) Pentium(R) 4 CPU XXXGHz                    |     CFLAGS="$"                                                                                                                                                   |
| :::                                                                   |     CXXFLAGS="$"                                                                                                                                                 |
|                                                                       | :::                                                                                                                                                                            |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#### [AMD]

##### [][Ryzen (Zen family)]

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                    | []                                                                                                                                                |
|                                                                       |                                                                                                                                                                                |
| ::: box-caption                                                       | ::: box-caption                                                                                                                                                                |
| **1000 and 2000 series**                                              | [FILE] **`/etc/portage/make.conf`** |
| :::                                                                   | :::                                                                                                                                                                            |
|                                                                       |                                                                                                                                                                                |
| :::  | :::                                                                                                           |
|     vendor_id   : AuthenticAMD                                        |     COMMON_FLAGS="-O2 -march=znver1 -pipe"                                                                                                                                     |
|     cpu family  : 23                                                  |     CFLAGS="$"                                                                                                                                                   |
|     model       : 1                                                   |     CXXFLAGS="$"                                                                                                                                                 |
|     model name  : AMD Ryzen 7 1800X Eight-Core Processor              | :::                                                                                                                                                                            |
|     …                                                                 |                                                                                                                                                                                |
|     cpu family  : 23                                                  |                                                                                                                                                                                |
|     model       : 8                                                   |                                                                                                                                                                                |
|     model name  : AMD Ryzen 7 2700X Eight-Core Processor              |                                                                                                                                                                                |
| :::                                                                   |                                                                                                                                                                                |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| **3000, 4000, 5000, and EPYC 7xx2 series**                            |                                                                                                                                                                                |
| :::                                                                   | ::: box-caption                                                                                                                                                                |
|                                                                       | [FILE] **`/etc/portage/make.conf`** |
| :::  | :::                                                                                                                                                                            |
|     vendor_id : AuthenticAMD                                          |                                                                                                                                                                                |
|     cpu family  : 23                                                  | :::                                                                                                           |
|     model       : 113                                                 |     COMMON_FLAGS="-O2 -march=znver2 -pipe"                                                                                                                                     |
|     model name  : AMD Ryzen 9 3900X 12-Core Processor                 |     CFLAGS="$"                                                                                                                                                   |
|     ...                                                               |     CXXFLAGS="$"                                                                                                                                                 |
|     cpu family      : 23                                              | :::                                                                                                                                                                            |
|     model           : 49                                              |                                                                                                                                                                                |
|     model name      : AMD EPYC 7542 32-Core Processor                 |                                                                                                                                                                                |
| :::                                                                   |                                                                                                                                                                                |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| **5000 and EPYC 7xx3 series**                                         |                                                                                                                                                                                |
| :::                                                                   | ::: box-caption                                                                                                                                                                |
|                                                                       | [FILE] **`/etc/portage/make.conf`** |
| :::  | :::                                                                                                                                                                            |
|     vendor_id  : AuthenticAMD                                         |                                                                                                                                                                                |
|     cpu family  : 25                                                  | :::                                                                                                           |
|     model       : 80                                                  |     COMMON_FLAGS="-O2 -march=znver3 -pipe"                                                                                                                                     |
|     model name  : AMD Ryzen 7 PRO 5850U with Radeon Graphics          |     CFLAGS="$"                                                                                                                                                   |
| :::                                                                   |     CXXFLAGS="$"                                                                                                                                                 |
|                                                                       | :::                                                                                                                                                                            |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| **7xx0 series**                                                       |                                                                                                                                                                                |
| :::                                                                   | ::: box-caption                                                                                                                                                                |
|                                                                       | [FILE] **`/etc/portage/make.conf`** |
| :::  | :::                                                                                                                                                                            |
|     vendor_id    : AuthenticAMD                                       |                                                                                                                                                                                |
|     cpu family  : 25                                                  | :::                                                                                                           |
|     model       : 97                                                  |     COMMON_FLAGS="-O2 -march=znver4 -pipe"                                                                                                                                     |
|     model name  : AMD Ryzen 7 7800X3D 8-Core Processor                |     CFLAGS="$"                                                                                                                                                   |
| :::                                                                   |     CXXFLAGS="$"                                                                                                                                                 |
|                                                                       | :::                                                                                                                                                                            |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| **AI 300, 9000 and EPYC 9xx5 series**                                 |                                                                                                                                                                                |
| :::                                                                   | ::: box-caption                                                                                                                                                                |
|                                                                       | [FILE] **`/etc/portage/make.conf`** |
| :::  | :::                                                                                                                                                                            |
|     vendor_id  : AuthenticAMD                                         |                                                                                                                                                                                |
|     cpu family  : 26                                                  | :::                                                                                                           |
|     model       : 36                                                  |     COMMON_FLAGS="-O2 -march=znver5 -pipe"                                                                                                                                     |
|     model name  : AMD Ryzen AI 9 365 w/ Radeon 880M                   |     CFLAGS="$"                                                                                                                                                   |
| :::                                                                   |     CXXFLAGS="$"                                                                                                                                                 |
|                                                                       | :::                                                                                                                                                                            |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

##### [][A6/A8/A9/A10/A12-8XXX/9XXX (Excavator)]

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| **Carrizo, Bristol Ridge, and Stoney Ridge**                          |                                                                                                                                                                                |
| :::                                                                   | ::: box-caption                                                                                                                                                                |
|                                                                       | [FILE] **`/etc/portage/make.conf`** |
| :::  | :::                                                                                                                                                                            |
|     vendor_id   : AuthenticAMD                                        |                                                                                                                                                                                |
|     cpu family  : 21                                                  | :::                                                                                                           |
|     model       : 96 or 101 or 112                                    |     COMMON_FLAGS="-O2 -march=bdver4 -pipe"                                                                                                                                     |
|     model name  : AMD A12-9800 RADEON R7, 12 COMPUTE CORES 4C+8G      |     CFLAGS="$"                                                                                                                                                   |
| :::                                                                   |     CXXFLAGS="$"                                                                                                                                                 |
|                                                                       | :::                                                                                                                                                                            |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

##### [][A4/A6/A8/A10-7XXX/8XXX (Steamroller)]

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| **Kaveri and Godavari**                                               |                                                                                                                                                                                |
| :::                                                                   | ::: box-caption                                                                                                                                                                |
|                                                                       | [FILE] **`/etc/portage/make.conf`** |
| :::  | :::                                                                                                                                                                            |
|     vendor_id    : AuthenticAMD                                       |                                                                                                                                                                                |
|     cpu family  : 21                                                  | :::                                                                                                           |
|     model       : 48 or 56                                            |     COMMON_FLAGS="-O2 -march=bdver3 -pipe"                                                                                                                                     |
|     model name  : AMD A10-7850K Radeon R7, 12 Compute Cores 4C+8G     |     CFLAGS="$"                                                                                                                                                   |
| :::                                                                   |     CXXFLAGS="$"                                                                                                                                                 |
|                                                                       | :::                                                                                                                                                                            |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

** Important**\
Various lowpower AMD APUs branded as AX-7XXX (eg. A4-7210) don\'t belong to *cpu family 21*!

##### [][E1/E2-XXXX, A4/A6/A8/A10-XXXX (Jaguar, Puma)]

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| **Kabini, Temash, Beema, Mullins, and Carrizo-L**                     |                                                                                                                                                                                |
| :::                                                                   | ::: box-caption                                                                                                                                                                |
|                                                                       | [FILE] **`/etc/portage/make.conf`** |
| :::  | :::                                                                                                                                                                            |
|     vendor_id  : AuthenticAMD                                         |                                                                                                                                                                                |
|     cpu family  : 22                                                  | :::                                                                                                           |
|     model       : 0 or 48                                             |     COMMON_FLAGS="-O2 -march=btver2 -pipe"                                                                                                                                     |
|     model name  : AMD A4-5000 APU with Radeon(TM) HD Graphics         |     CFLAGS="$"                                                                                                                                                   |
| :::                                                                   |     CXXFLAGS="$"                                                                                                                                                 |
|                                                                       | :::                                                                                                                                                                            |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

** Important**\
Majority of AMD APUs branded as A4/A6/A8-XXXX (eg. A4-5300, A4-4000 or A6-5345M) don\'t belong to *cpu family 22*! They should use settings listed for AMD APU model given by the `cpu family` and `model`.

##### [][A4/A6/A8/A10-4XXX/5XXX/6XXX (Piledriver)]

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| **Trinity and Richland**                                              |                                                                                                                                                                                |
| :::                                                                   | ::: box-caption                                                                                                                                                                |
|                                                                       | [FILE] **`/etc/portage/make.conf`** |
| :::  | :::                                                                                                                                                                            |
|     vendor_id   : AuthenticAMD                                        |                                                                                                                                                                                |
|     cpu family  : 21                                                  | :::                                                                                                           |
|     model       : 16 or 19                                            |     COMMON_FLAGS="-O2 -march=bdver2 -pipe"                                                                                                                                     |
|     model name  : AMD A8-4500M APU with Radeon(tm) HD Graphics        |     CFLAGS="$"                                                                                                                                                   |
| :::                                                                   |     CXXFLAGS="$"                                                                                                                                                 |
|                                                                       | :::                                                                                                                                                                            |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

** Important**\
Various low power AMD APUs branded as AX-5XXX/6XXX (eg. A4-5000, A4-5100 or A6-6310) don\'t belong to *CPU family 21*!

##### [FX-XXXX]

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| **Bulldozer and Piledriver**                                          |                                                                                                                                                                                |
| :::                                                                   | ::: box-caption                                                                                                                                                                |
|                                                                       | [FILE] **`/etc/portage/make.conf`** |
| :::  | :::                                                                                                                                                                            |
|     vendor_id   : AuthenticAMD                                        |                                                                                                                                                                                |
|     cpu family  : 21                                                  | :::                                                                                                           |
|     model       : 1 or 2                                              |     COMMON_FLAGS="-O2 -march=bdver1 -pipe"                                                                                                                                     |
|     model name  : AMD FX(tm)-8150 Eight-Core Processor                |     CFLAGS="$"                                                                                                                                                   |
| :::                                                                   |     CXXFLAGS="$"                                                                                                                                                 |
|                                                                       | :::                                                                                                                                                                            |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

** Important**\
Make sure and check the number listed by `model` on the system, the `-march` flag should be *bdverX* where *X* is the model number.

** Important**\
Various AMD APUs branded as FX don\'t match `model` 1 or 2! They should use settings listed for AMD APU model given by the `cpu family` and `model`.

##### [][Z-XX, C-X0, E-XX0, E1/E2-1X00, E2-2000 (Bobcat)]

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| **Ontario, Hondo, Desna, and Zacate**                                 |                                                                                                                                                                                |
| :::                                                                   | ::: box-caption                                                                                                                                                                |
|                                                                       | [FILE] **`/etc/portage/make.conf`** |
| :::  | :::                                                                                                                                                                            |
|     vendor_id  : AuthenticAMD                                         |                                                                                                                                                                                |
|     cpu family  : 20                                                  | :::                                                                                                           |
|     model       : 1 or 2                                              |     COMMON_FLAGS="-O2 -march=btver1 -pipe"                                                                                                                                     |
|     model name  : AMD E-350 Processor                                 |     CFLAGS="$"                                                                                                                                                   |
| :::                                                                   |     CXXFLAGS="$"                                                                                                                                                 |
|                                                                       | :::                                                                                                                                                                            |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

##### [][A4/A6/A8-3XXX/3XXXM (12h)]

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| **Llano**                                                             |                                                                                                                                                                                |
| :::                                                                   | ::: box-caption                                                                                                                                                                |
|                                                                       | [FILE] **`/etc/portage/make.conf`** |
| :::  | :::                                                                                                                                                                            |
|     vendor_id  : AuthenticAMD                                         |                                                                                                                                                                                |
|     cpu family  : 18                                                  | :::                                                                                                           |
|     model       : 1                                                   |     COMMON_FLAGS="-O2 -march=amdfam10 -mcx16 -mpopcnt -pipe"                                                                                                                   |
|     model name  : AMD A8-3500M APU with Radeon(tm) HD Graphics        |     CFLAGS="$"                                                                                                                                                   |
| :::                                                                   |     CXXFLAGS="$"                                                                                                                                                 |
|                                                                       | :::                                                                                                                                                                            |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

##### [][Phenom/Phenom II, Athlon II, Sempron (10h)]

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| **Agena, Deneb, Thuban, and derivatives**                             |                                                                                                                                                                                |
| :::                                                                   | ::: box-caption                                                                                                                                                                |
|                                                                       | [FILE] **`/etc/portage/make.conf`** |
| :::  | :::                                                                                                                                                                            |
|     vendor_id  : AuthenticAMD                                         |                                                                                                                                                                                |
|     cpu family  : 16                                                  | :::                                                                                                           |
|     model       : X                                                   |     COMMON_FLAGS="-O2 -march=amdfam10 -pipe"                                                                                                                                   |
|     model name  : AMD Phenom(tm) II X6 1090T Processor                |     CFLAGS="$"                                                                                                                                                   |
| :::                                                                   |     CXXFLAGS="$"                                                                                                                                                 |
|                                                                       | :::                                                                                                                                                                            |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

##### [Older microarchitectures]

** Important**\
Various AMD CPUs branded as Sempron (eg. Sempron 2200+ or Sempron 3000+) don\'t belong to *cpu family 15*!

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| **E+ revisions - Athlon 64, Athlon 64 X2/FX, Sempron (0Fh)**          |                                                                                                                                                                                |
| :::                                                                   | ::: box-caption                                                                                                                                                                |
|                                                                       | [FILE] **`/etc/portage/make.conf`** |
| :::  | :::                                                                                                                                                                            |
|     vendor_id   : AuthenticAMD                                        |                                                                                                                                                                                |
|     cpu family  : 15                                                  | :::                                                                                                           |
|     model       : >= 39                                               |     COMMON_FLAGS="-O2 -march=opteron-sse3 -pipe"                                                                                                                               |
|     model name  : AMD Athlon(tm) 64 X2 Dual Core Processor 4200+      |     CFLAGS="$"                                                                                                                                                   |
| :::                                                                   |     CXXFLAGS="$"                                                                                                                                                 |
|                                                                       | :::                                                                                                                                                                            |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| **Geode LX**                                                          |                                                                                                                                                                                |
| :::                                                                   | ::: box-caption                                                                                                                                                                |
|                                                                       | [FILE] **`/etc/portage/make.conf`** |
| :::  | :::                                                                                                                                                                            |
|     vendor_id   : AuthenticAMD                                        |                                                                                                                                                                                |
|     cpu family  : 5                                                   | :::                                                                                                           |
|     model       : 10                                                  |     CHOST="i486-pc-linux-gnu"                                                                                                                                                  |
|     model name  : Geode(TM) Integrated Processor by AMD PCS           |     COMMON_FLAGS="-Os -pipe -march=geode -mmmx -m3dnow -fomit-frame-pointer"                                                                                                   |
| :::                                                                   |     CFLAGS="$"                                                                                                                                                   |
|                                                                       |     CXXFLAGS="$"                                                                                                                                                 |
|                                                                       | :::                                                                                                                                                                            |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| **Pre-E revisions - Athlon 64, Athlon 64 FX, Sempron (0Fh)**          |                                                                                                                                                                                |
| :::                                                                   | ::: box-caption                                                                                                                                                                |
|                                                                       | [FILE] **`/etc/portage/make.conf`** |
| :::  | :::                                                                                                                                                                            |
|     vendor_id   : AuthenticAMD                                        |                                                                                                                                                                                |
|     cpu family  : 15                                                  | :::                                                                                                           |
|     model       : < 39                                                |     COMMON_FLAGS="-O2 -march=opteron -pipe"                                                                                                                                    |
|     model name  : AMD Athlon(tm) 64 Processor 3200+                   |     CFLAGS="$"                                                                                                                                                   |
| :::                                                                   |     CXXFLAGS="$"                                                                                                                                                 |
|                                                                       | :::                                                                                                                                                                            |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

### [ARM]

** Note**\
To identify the respective ARM core of the SoC, [List of ARM microarchitectures](https://en.wikipedia.org/wiki/List_of_ARM_microarchitectures "wikipedia:List of ARM microarchitectures") and [List of applications of ARM cores](https://en.wikipedia.org/wiki/List_of_applications_of_ARM_cores "wikipedia:List of applications of ARM cores") on Wikipedia may help.

#### [Cortex-A]

##### [][ARMv7-A/Cortex-A9 MPCore]

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                        | []                                                                                                                                                |
| with optional VFPv3 FPU                                                |                                                                                                                                                                                |
| :::                                                                    | ::: box-caption                                                                                                                                                                |
|                                                                        | [FILE] **`/etc/portage/make.conf`** |
| :::   | :::                                                                                                                                                                            |
|     processor       : 0                                                |                                                                                                                                                                                |
|     model name      : ARMv7 Processor rev 0 (v7l)                      | :::                                                                                                           |
|     BogoMIPS        : 2.00                                             |     CHOST="armv7a-hardfloat-linux-gnueabi"                                                                                                                                     |
|     Features        : half thumb fastmult vfp edsp vfpv3 vfpv3d16 tls  |     COMMON_FLAGS="-O2 -march=cortex-a9 -mfpu=vfpv3-d16 -mfloat-abi=hard -pipe -fomit-frame-pointer"                                                                            |
|     CPU implementer : 0x41                                             |     CFLAGS="$"                                                                                                                                                   |
|     CPU architecture: 7                                                |     CXXFLAGS="$"                                                                                                                                                 |
|     CPU variant     : 0x1                                              | :::                                                                                                                                                                            |
|     CPU part        : 0xc09                                            |                                                                                                                                                                                |
|     CPU revision    : 0                                                |                                                                                                                                                                                |
|                                                                        |                                                                                                                                                                                |
|     processor       : 1                                                |                                                                                                                                                                                |
|     model name      : ARMv7 Processor rev 0 (v7l)                      |                                                                                                                                                                                |
|     BogoMIPS        : 2.00                                             |                                                                                                                                                                                |
|     Features        : half thumb fastmult vfp edsp vfpv3 vfpv3d16 tls  |                                                                                                                                                                                |
|     CPU implementer : 0x41                                             |                                                                                                                                                                                |
|     CPU architecture: 7                                                |                                                                                                                                                                                |
|     CPU variant     : 0x1                                              |                                                                                                                                                                                |
|     CPU part        : 0xc09                                            |                                                                                                                                                                                |
|     CPU revision    : 0                                                |                                                                                                                                                                                |
|                                                                        |                                                                                                                                                                                |
|     Hardware        : NVIDIA Tegra SoC (Flattened Device Tree)         |                                                                                                                                                                                |
|     Revision        : 0000                                             |                                                                                                                                                                                |
|     Serial          : 0000000000000000                                 |                                                                                                                                                                                |
| :::                                                                    |                                                                                                                                                                                |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

** Note**\
This ARM core (equipped with the optional vfpv3d16 FPU but missing the NEON extension) is used in the Toshiba AC100/Dynabook AZ/Compal Paz00 Board.

##### [][ARMv8-A/BCM2837]

** Note**\
This is the Broadcom chip used in the Raspberry Pi 3 Model B.

+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                                                            | []                                                                                                                                                |
| **AArch32 with neon FPU**                                                                                  |                                                                                                                                                                                |
| :::                                                                                                        | ::: box-caption                                                                                                                                                                |
|                                                                                                            | [FILE] **`/etc/portage/make.conf`** |
| :::                                       | :::                                                                                                                                                                            |
|     processor  : 0-3                                                                                       |                                                                                                                                                                                |
|     model name  : ARMv7 Processor rev 4 (v7l)                                                              | :::                                                                                                           |
|     BogoMIPS    : 38.40                                                                                    |     CHOST="armv7a-hardfloat-linux-gnueabi"                                                                                                                                     |
|     Features    : half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt vfpd32 lpae evtstrm crc32  |     COMMON_FLAGS="-O2 -pipe -march=armv7-a -mfpu=neon-vfpv4 -mfloat-abi=hard"                                                                                                  |
|     CPU implementer : 0x41                                                                                 |     CFLAGS="$"                                                                                                                                                   |
|     CPU architecture: 7                                                                                    |     CXXFLAGS="$"                                                                                                                                                 |
|     CPU variant : 0x0                                                                                      | :::                                                                                                                                                                            |
|     CPU part    : 0xd03                                                                                    |                                                                                                                                                                                |
|     CPU revision    : 4                                                                                    |                                                                                                                                                                                |
|                                                                                                            |                                                                                                                                                                                |
|     Hardware    : BCM2709                                                                                  |                                                                                                                                                                                |
|     Revision        : 0000                                                                                 |                                                                                                                                                                                |
|     Serial          : 0000000000000000                                                                     |                                                                                                                                                                                |
| :::                                                                                                        |                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| **AArch64**                                                           |                                                                                                                                                                                |
| :::                                                                   | ::: box-caption                                                                                                                                                                |
|                                                                       | [FILE] **`/etc/portage/make.conf`** |
| :::  | :::                                                                                                                                                                            |
|     processor    : 0-3                                                |                                                                                                                                                                                |
|     BogoMIPS    : 38.40                                               | :::                                                                                                           |
|     Features    : fp asimd evtstrm crc32                              |     COMMON_FLAGS="-march=armv8-a+crc -mtune=cortex-a53 -O2 -pipe"                                                                                                              |
|     CPU implementer : 0x41                                            |     CFLAGS="$"                                                                                                                                                   |
|     CPU architecture: 8                                               |     CXXFLAGS="$"                                                                                                                                                 |
|     CPU variant : 0x0                                                 | :::                                                                                                                                                                            |
|     CPU part    : 0xd03                                               |                                                                                                                                                                                |
|     CPU revision    : 4                                               |                                                                                                                                                                                |
| :::                                                                   |                                                                                                                                                                                |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#### [ARM11]

##### [][ARMv6/ARM1176JZF-S]

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| :::                                                                   |                                                                                                                                                                                |
|                                                                       | ::: box-caption                                                                                                                                                                |
| :::  | [FILE] **`/etc/portage/make.conf`** |
|     processor  : 0                                                    | :::                                                                                                                                                                            |
|     model name  : ARMv6-compatible processor rev 7 (v6l)              |                                                                                                                                                                                |
|     BogoMIPS    : 697.95                                              | :::                                                                                                           |
|     Features    : half thumb fastmult vfp edsp java tls               |     CHOST="armv6j-hardfloat-linux-gnueabi"                                                                                                                                     |
|     CPU implementer : 0x41                                            |     COMMON_FLAGS="-O2 -pipe -mcpu=arm1176jzf-s -mfpu=vfp -mfloat-abi=hard"                                                                                                     |
|     CPU architecture: 7                                               |     CFLAGS="$"                                                                                                                                                   |
|     CPU variant : 0x0                                                 |     CXXFLAGS="$"                                                                                                                                                 |
|     CPU part    : 0xb76                                               | :::                                                                                                                                                                            |
|     CPU revision    : 7                                               |                                                                                                                                                                                |
|                                                                       |                                                                                                                                                                                |
|     Hardware    : BCM2835                                             |                                                                                                                                                                                |
|     Revision    : 0000                                                |                                                                                                                                                                                |
|     Serial      : 000000000XXXXXXX                                    |                                                                                                                                                                                |
| :::                                                                   |                                                                                                                                                                                |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

** Note**\
This ARM core is used in the first generation of the Raspberry Pi.

##### [][ARMv6/ARM1136JF-S]

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| :::                                                                   |                                                                                                                                                                                |
|                                                                       | ::: box-caption                                                                                                                                                                |
| :::  | [FILE] **`/etc/portage/make.conf`** |
|     Processor       : ARMv6-compatible processor rev 5 (v6l)          | :::                                                                                                                                                                            |
|     BogoMIPS        : 791.34                                          |                                                                                                                                                                                |
|     Features        : swp half thumb fastmult vfp edsp java           | :::                                                                                                           |
|     CPU implementer : 0x41                                            |     CHOST="armv6j-hardfloat-linux-gnueabi"                                                                                                                                     |
|     CPU architecture: 6TEJ                                            |     COMMON_FLAGS="-Os -mcpu=arm1136jf-s -mfpu=vfp -mfloat-abi=hard -pipe -fomit-frame-pointer"                                                                                 |
|     CPU variant     : 0x1                                             |     CFLAGS="$"                                                                                                                                                   |
|     CPU part        : 0xb36                                           |     CXXFLAGS="$"                                                                                                                                                 |
|     CPU revision    : 5                                               | :::                                                                                                                                                                            |
|                                                                       |                                                                                                                                                                                |
|     Hardware        : IMAPX200                                        |                                                                                                                                                                                |
|     Revision        : 0000                                            |                                                                                                                                                                                |
|     Serial          : 0000000000000000                                |                                                                                                                                                                                |
| :::                                                                   |                                                                                                                                                                                |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

### [][PowerPC / PowerPC 64]

** Important**\
`-march=` is not supported on the PowerPC (and RS/6000) instruction set architecture (ISA). Use `-mcpu=` and `-mtune=` instead.

** Note**\
Using `-mcpu=native` (and/or `-mtune=native`) should work on PowerPC but is not recommended due to distcc.

#### [POWER8]

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | ::: box-caption                                                                                                                                                                |
| :::                                                                   | [FILE] **`/etc/portage/make.conf`** |
|                                                                       | :::                                                                                                                                                                            |
| :::  |                                                                                                                                                                                |
|     processor       : 0                                               | :::                                                                                                           |
|     cpu             : POWER8E (raw), altivec supported                |     COMMON_FLAGS="-mcpu=power8 -O2 -pipe"                                                                                                                                      |
|     clock           : 3026.000000MHz                                  |     CFLAGS="$"                                                                                                                                                   |
|     revision        : 2.1 (pvr 004b 0201)                             |     CXXFLAGS="$"                                                                                                                                                 |
|                                                                       | :::                                                                                                                                                                            |
|     timebase        : 512000000                                       |                                                                                                                                                                                |
|     platform        : pSeries                                         |                                                                                                                                                                                |
|     model           : IBM pSeries (emulated by qemu)                  |                                                                                                                                                                                |
|     machine         : CHRP IBM pSeries (emulated by qemu)             |                                                                                                                                                                                |
| :::                                                                   |                                                                                                                                                                                |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#### [Cell]

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| :::                                                                   |                                                                                                                                                                                |
|                                                                       | ::: box-caption                                                                                                                                                                |
| :::  | [FILE] **`/etc/portage/make.conf`** |
|     processor  : 0                                                    | :::                                                                                                                                                                            |
|     cpu     : Cell Broadband Engine, altivec supported                |                                                                                                                                                                                |
|     clock       : 3192.000000MHz                                      | :::                                                                                                           |
|     revision    : 5.1 (pvr 0070 0501)                                 |     COMMON_FLAGS="-mcpu=cell -O2 -pipe -mabi=altivec -maltivec -mno-string -mno-multiple"                                                                                      |
|                                                                       |     CFLAGS="$"                                                                                                                                                   |
|     processor   : 1                                                   |     CXXFLAGS="$"                                                                                                                                                 |
|     cpu     : Cell Broadband Engine, altivec supported                | :::                                                                                                                                                                            |
|     clock       : 3192.000000MHz                                      |                                                                                                                                                                                |
|     revision    : 5.1 (pvr 0070 0501)                                 |                                                                                                                                                                                |
|                                                                       |                                                                                                                                                                                |
|     timebase    : 79800000                                            |                                                                                                                                                                                |
|     platform    : PS3                                                 |                                                                                                                                                                                |
|     model       : SonyPS3                                             |                                                                                                                                                                                |
| :::                                                                   |                                                                                                                                                                                |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

** Note**\
GCC\'s -mspe and -mabi=spe options are not targetting PS3 systems and IBM Cell. Instead, those options are dedicated to IBM e500. More info:

-   [https://lists.debian.org/debian-devel/2011/06/msg00592.html](https://lists.debian.org/debian-devel/2011/06/msg00592.html)
-   [https://wiki.debian.org/PowerPCSPEPort](https://wiki.debian.org/PowerPCSPEPort)

#### [][PPC 970 (G5)]

Compatible processors are IBM PPC970, PPC970FX, PPC970MP and PPC970GX.

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| :::                                                                   |                                                                                                                                                                                |
|                                                                       | ::: box-caption                                                                                                                                                                |
| :::  | [FILE] **`/etc/portage/make.conf`** |
|     cpu             : PPC970, altivec supported                       | :::                                                                                                                                                                            |
|     clock           : 1800MHz                                         |                                                                                                                                                                                |
|     revision        : 2.2 (pvr 0039 0202)                             | :::                                                                                                           |
|     bogomips        : 1127.21                                         |     COMMON_FLAGS="-mcpu=970 -O2 -maltivec -mabi=altivec -pipe"                                                                                                                 |
|     machine         : PowerMac7,2                                     |     CFLAGS="$"                                                                                                                                                   |
|     motherboard     : PowerMac7,2 MacRISC4 Power Macintosh            |     CXXFLAGS="$"                                                                                                                                                 |
|     board revision  : 00000001                                        | :::                                                                                                                                                                            |
|     detected as     : 336 (PowerMac G5)                               |                                                                                                                                                                                |
|     pmac flags      : 00000000                                        |                                                                                                                                                                                |
|     L2 cache        : 512K unified                                    |                                                                                                                                                                                |
|     pmac-generation : NewWorld                                        |                                                                                                                                                                                |
| :::                                                                   |                                                                                                                                                                                |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#### [][G4 (PPC 74xx)]

##### [PPC 7450 family]

Compatible processors are Motorola/Freescale MPC7450, MPC7440, MPC7451, MPC7441, MPC7455, MPC7445, MPC7457, MPC7447, MPC7447/A, and MPC7448.

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| :::                                                                   |                                                                                                                                                                                |
|                                                                       | ::: box-caption                                                                                                                                                                |
| :::  | [FILE] **`/etc/portage/make.conf`** |
|     processor       : 0                                               | :::                                                                                                                                                                            |
|     cpu             : 7447A, altivec supported                        |                                                                                                                                                                                |
|     clock           : 1666.666000MHz                                  | :::                                                                                                           |
|     revision        : 1.5 (pvr 8003 0105)                             |     COMMON_FLAGS="-mcpu=7450 -O2 -maltivec -mabi=altivec -pipe"                                                                                                                |
|     bogomips        : 33.28                                           |     CFLAGS="$"                                                                                                                                                   |
|     timebase        : 8320000                                         |     CXXFLAGS="$"                                                                                                                                                 |
|     platform        : PowerMac                                        | :::                                                                                                                                                                            |
|     model           : PowerBook5,9                                    |                                                                                                                                                                                |
|     machine         : PowerBook5,9                                    |                                                                                                                                                                                |
|     motherboard     : PowerBook5,9 MacRISC3 Power Macintosh           |                                                                                                                                                                                |
|     detected as     : 287 (PowerBook G4 17")                          |                                                                                                                                                                                |
|     pmac flags      : 00000018                                        |                                                                                                                                                                                |
|     L2 cache        : 512K unified                                    |                                                                                                                                                                                |
|     pmac-generation : NewWorld                                        |                                                                                                                                                                                |
| :::                                                                   |                                                                                                                                                                                |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

##### [PPC 7400 family]

Compatible processors are Motorola MPC7400 and MPC7410. Note: IBM manufactured the MPC7400 as 06K5319 and 10K8298 when Motorola was not able to fulfill Apple\'s demands.

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| :::                                                                   |                                                                                                                                                                                |
|                                                                       | ::: box-caption                                                                                                                                                                |
| :::  | [FILE] **`/etc/portage/make.conf`** |
|     processor       : 0                                               | :::                                                                                                                                                                            |
|     cpu             : 7400, altivec supported                         |                                                                                                                                                                                |
|     clock           : 400.000000MHz                                   | :::                                                                                                           |
|     revision        : 2.9 (pvr 000c 0209)                             |     COMMON_FLAGS="-mcpu=7400 -O2 -maltivec -mabi=altivec -pipe"                                                                                                                |
|     bogomips        : 49.66                                           |     CFLAGS="$"                                                                                                                                                   |
|     timebase        : 24908583                                        |     CXXFLAGS="$"                                                                                                                                                 |
|     platform        : PowerMac                                        | :::                                                                                                                                                                            |
|     machine         : PowerMac3,1                                     |                                                                                                                                                                                |
|     motherboard     : PowerMac3,1 MacRISC Power Macintosh             |                                                                                                                                                                                |
|     detected as     : 65 (PowerMac G4 AGP Graphics)                   |                                                                                                                                                                                |
|     pmac flags      : 00000004                                        |                                                                                                                                                                                |
|     L2 cache        : 1024K unified                                   |                                                                                                                                                                                |
|     pmac-generation : NewWorld                                        |                                                                                                                                                                                |
| :::                                                                   |                                                                                                                                                                                |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#### [][G3 (PPC 7XX)]

Compatible processors are Motorola/Freescale MPC750, MPC740, MPC755 and MPC745 as well as IBM PPC750, PPC740, PPC750L, PPC740L, PPC750CX, PPC750CXe, PPCDBK (\"Gekko\"), PPC750FX, PPC750GX, PPC750CXr, PPC750CL (\"Broadway\"), PPC750GL and PPC750FL. The BAE Systems RAD750 is a radiation hardened variant of the PPC750. The \"Espresso\" (following the \"Gekko\" and \"Broadway\") is also based on the PPC750.

For CPUs for embedded systems such as the Gekko (PPCDBK, used in the Nintendo GameCube) additional CFLAGS (like `-meabi`) will be required.

+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ::: box-caption                                                       | []                                                                                                                                                |
| :::                                                                   |                                                                                                                                                                                |
|                                                                       | ::: box-caption                                                                                                                                                                |
| :::  | [FILE] **`/etc/portage/make.conf`** |
|     processor       : 0                                               | :::                                                                                                                                                                            |
|     cpu             : 740/750                                         |                                                                                                                                                                                |
|     clock           : 400.000000MHz                                   | :::                                                                                                           |
|     revision        : 131.0 (pvr 0008 8300)                           |     COMMON_FLAGS="-mcpu=750 -Os -pipe"                                                                                                                                         |
|     bogomips        : 49.93                                           |     CFLAGS="$"                                                                                                                                                   |
|     timebase        : 24966218                                        |     CXXFLAGS="$"                                                                                                                                                 |
|     platform        : PowerMac                                        | :::                                                                                                                                                                            |
|     model           : PowerBook3,1                                    |                                                                                                                                                                                |
|     machine         : PowerBook3,1                                    |                                                                                                                                                                                |
|     motherboard     : PowerBook3,1 MacRISC2 MacRISC Power Macintosh   |                                                                                                                                                                                |
|     detected as     : 70 (PowerBook Pismo)                            |                                                                                                                                                                                |
|     pmac flags      : 0000001f                                        |                                                                                                                                                                                |
|     L2 cache        : 1024K unified                                   |                                                                                                                                                                                |
|     pmac-generation : NewWorld                                        |                                                                                                                                                                                |
| :::                                                                   |                                                                                                                                                                                |
+-----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

### [RISC-V]

+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|     processor       : 0             | ::: box-caption                                                                                                                                                                |
|     hart            : 1             | [FILE] **`/etc/portage/make.conf`** |
|     isa             : rv64imafdc    | :::                                                                                                                                                                            |
|     mmu             : sv39          |                                                                                                                                                                                |
|     uarch           : sifive,u74-mc | :::                                                                                                           |
|                                     |     COMMON_FLAGS="-march=rv64imafdc_zicsr_zba_zbb -mcpu=sifive-u74 -mtune=sifive-7-series -O2 -pipe"                                                                           |
|                                     |     CFLAGS="$"                                                                                                                                                   |
|                                     |     CXXFLAGS="$"                                                                                                                                                 |
|                                     | :::                                                                                                                                                                            |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

## [See also]

-   [CFLAGS and CXXFLAGS (AMD64 Handbook)](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Stage#CFLAGS_and_CXXFLAGS "Handbook:AMD64/Installation/Stage")
-   [CPU_FLAGS\_\*](https://wiki.gentoo.org/wiki/CPU_FLAGS_* "CPU FLAGS *") --- a [`USE_EXPAND`](https://wiki.gentoo.org/wiki//etc/portage/make.conf#USE_EXPAND "/etc/portage/make.conf") variable containing instruction set and other CPU-specific features.
-   [GCC optimization](https://wiki.gentoo.org/wiki/GCC_optimization "GCC optimization") --- an introduction to optimizing compiled code using safe, sane [`CFLAGS` and `CXXFLAGS`](https://en.wikipedia.org/wiki/CFLAGS "wikipedia:CFLAGS").
-   [Gentoo documentation page on backtraces](https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces "Project:Quality Assurance/Backtraces")
-   [RUSTFLAGS](https://wiki.gentoo.org/wiki/Rust#Environment_variables "Rust")

## [External resources]

-   [GCC Online Documentation](https://gcc.gnu.org/onlinedocs/) on GNU.org
-   [GCC x86 performance hints from Intel](https://software.intel.com/content/www/us/en/develop/blogs/gcc-x86-performance-hints.html)
-   [List of AMD Microarchitectures with extended info](https://en.wikichip.org/wiki/amd#Microarchitectures)
-   [List of Intel Microarchitectures with extended info](https://en.wikichip.org/wiki/intel#List_of_microarchitectures)
-   [SGX-Driver builds with errors in WSL](https://community.intel.com/t5/Intel-Software-Guard-Extensions/SGX-Driver-builds-with-errors-in-WSL/m-p/1461909) on community.intel.com