**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Intel_Core_2 "wikipedia:Intel Core 2")

This article describes the setup of an Intel Core 2 Solo/Duo/Quad processor.

The Intel Core 2 line of processors supports both the 32-bit and 64-bit mode. The general pros and cons can be read about in the [Wikipedia article](https://en.wikipedia.org/wiki/64-bit_computing#32-bit_vs_64-bit "wikipedia:64-bit computing"). By now only very few applications do not support 64-bit mode or work in a 32-bit compatibility mode.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [BIOS]](#BIOS)
    -   [[1.2] [Kernel]](#Kernel)
    -   [[1.3] [Software]](#Software)
    -   [[1.4] [Temperature sensor]](#Temperature_sensor)
    -   [[1.5] [Virtualization]](#Virtualization)
-   [[2] [See also]](#See_also)

## [Installation]

### [BIOS]

If you have a dual-core or a quad-core Intel Core 2 CPU, you should first check if all cores are enabled:

`user `[`$`]`cat /proc/cpuinfo`

If not, enable options like *APIC*, *MultiCore*, etc. in the [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS").

### [Kernel]

Activate the following kernel options.

For a single-core processor:

[KERNEL]

    Processor type and features  --->
        [ ] Symmetric multi-processing support
        Subarchitecture Type ()  --->
            (X) PC-compatible
        Processor family ()  --->
            (X) Core 2/newer Xeon

For a dual-core or a quad-core processor:

[KERNEL]

    Processor type and features  --->
        [*] Symmetric multi-processing support
        Subarchitecture Type ()  --->
            (X) PC-compatible
        Processor family ()  --->
            (X) Core 2/newer Xeon

        dual-core
        (2) Maximum number of CPUs (2-256)

        quad-core
        (4) Maximum number of CPUs (2-256)

### [Software]

[FILE] **`/etc/portage/package.use/00cpu-flags`**

    CPU_FLAGS_X86="mmx sse sse2 sse3 ssse3"

[FILE] **`/etc/portage/package.use/00cpu-flags`Penryn and newer**

    CPU_FLAGS_X86="mmx sse sse2 sse3 ssse3 sse4 sse4a sse4_1"

[FILE] **[`/etc/portage/make.conf`](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf")CFLAGS**

    # Note: -fomit-frame-pointer only makes a difference on x86 since it is included in -O2 on amd64
    CFLAGS="-march=native -O2 -pipe -fomit-frame-pointer"
    CXXFLAGS="$"

[FILE] **[`/etc/portage/make.conf`](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf")MAKEOPTS (Intel Core 2 Solo)**

    MAKEOPTS="-j1"

[FILE] **[`/etc/portage/make.conf`](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf")MAKEOPTS (Intel Core 2 Duo)**

    MAKEOPTS="-j2"

[FILE] **[`/etc/portage/make.conf`](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf")MAKEOPTS (Intel Core 2 Quad)**

    MAKEOPTS="-j3"

### [Temperature sensor]

See the [lm_sensors](https://wiki.gentoo.org/wiki/Lm_sensors "Lm sensors") article and activate the kernel driver **coretemp**.

### [Virtualization]

Most of these processors support Intel VT. Exceptions include:

-   Merom \<T5600
-   Allendale E4xxx

See the [Virtualization category](https://wiki.gentoo.org/wiki/Category:Virtualization "Category:Virtualization").

## [See also]

-   [Intel microcode](https://wiki.gentoo.org/wiki/Intel_microcode "Intel microcode") --- describes the process of updating the [microcode](https://wiki.gentoo.org/wiki/Microcode "Microcode") on Intel processors.
-   [Power management/Processor](https://wiki.gentoo.org/wiki/Power_management/Processor "Power management/Processor") --- describes the setup of [power management](https://wiki.gentoo.org/wiki/Power_management "Power management") for [processors](https://wiki.gentoo.org/wiki/Category:Processors "Category:Processors").
-   [CPU_FLAGS\_\*](https://wiki.gentoo.org/wiki/CPU_FLAGS_* "CPU FLAGS *") --- a [`USE_EXPAND`](https://wiki.gentoo.org/wiki//etc/portage/make.conf#USE_EXPAND "/etc/portage/make.conf") variable containing instruction set and other CPU-specific features.