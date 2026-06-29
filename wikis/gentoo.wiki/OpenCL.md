Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/OpenCL/de "OpenCL/de (6% translated)")
-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/OpenCL/hu "OpenCL (100% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/OpenCL/ja "OpenCL (100% translated)")

*Not to be confused with [OpenCT](https://wiki.gentoo.org/wiki/OpenCT "OpenCT").*

**Open Computing Language** (OpenCL) is a framework for writing programs that execute across heterogeneous computing platforms (CPUs, GPUs, DSPs, FPGAs, ASICs, etc.).

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Implementations on Linux]](#Implementations_on_Linux)
    -   [[2.1] [ICD]](#ICD)
    -   [[2.2] [Mesa (rusticl)]](#Mesa_.28rusticl.29)
    -   [[2.3] [Mesa (clover)]](#Mesa_.28clover.29)
    -   [[2.4] [Intel - CPU]](#Intel_-_CPU)
    -   [[2.5] [Intel - GPU]](#Intel_-_GPU)
        -   [[2.5.1] [Intel Graphics Compute Runtime]](#Intel_Graphics_Compute_Runtime)
    -   [[2.6] [AMD]](#AMD)
    -   [[2.7] [nVidia]](#nVidia)
-   [[3] [Usage notes]](#Usage_notes)
    -   [[3.1] [Displaying info about OpenCL]](#Displaying_info_about_OpenCL)
    -   [[3.2] [Implementation validation]](#Implementation_validation)
    -   [[3.3] [Implementation tuning]](#Implementation_tuning)
    -   [[3.4] [LLVM DLL hell]](#LLVM_DLL_hell)
-   [[4] [References]](#References)

## [Overview]

The point of this article is to deal with Gentoo implementation and quirks so the overview will be short. For a better overview of the theoretical aspects, see [the OpenCL wikipedia article](https://en.wikipedia.org/wiki/OpenCL "wikipedia:OpenCL").

OpenCL presents itself as a library with a simple interface:

-   Standardized API headers (eg. `#include CL/cl.h`) for C and C++.
-   The OpenCL library (eg. [libOpenCL.so]).

The standard is made to provide many OpenCL *platforms* on one system, and each platform can see various *devices*. Each *device* has a certain compute characteristics (number of compute units, optimal vector size, memory limits, \...).

The OpenCL standard allows to load OpenCL *kernels* which are pieces of C99-like code that is JIT-compiled by the OpenCL implementations (most of them rely on [LLVM](https://wiki.gentoo.org/wiki/LLVM "LLVM") to work), and execute these kernels on the target hardware. Functions are provided to compile the kernels, load them, transfer data back and forth from the target devices, etc.

Hardware vendors can benefit from this standard by implementing the OpenCL primitives for their hardware.

Installing an OpenCL implementation means adding a library implementing the OpenCL API, and a reference to the library path in the ICD (Installable Client Driver) database, as a file in [/etc/OpenCL/vendors].

There is an ICD loader which can be provided by a generic loader or one of the implementations. For most uses of OpenCL one of these must be selected using [eselect opencl].

The OpenCL host and device API calls, the memory hierarchy are standard, but it doesn\'t mean that code which is *portable* to different implementations will be *efficient* on all of them. Often, code has to be tested on one implementation to eliminate issues. See the [implementation validation](https://wiki.gentoo.org/wiki/OpenCL#Implementation_Validation "OpenCL") and [implementation tuning](https://wiki.gentoo.org/wiki/OpenCL#Implementation_Tuning "OpenCL") sections.

## [Implementations on Linux]

Here are upstream projects that provide an implementation of OpenCL.

-   pocl is an OpenSource, LLVM-based OpenCL implementation for the CPU which is not necessarily the fastest, but is educational
-   mesa has a WIP implementation which works on some GPU devices.
-   AMD provides its AMD APP SDK [\[1\]](http://developer.amd.com/tools-and-sdks/opencl-zone/amd-accelerated-parallel-processing-app-sdk/) which contains an OpenCL library.
-   NVIDIA provides its CUDA toolkit [\[2\]](https://developer.nvidia.com/cuda-toolkit) which contains an OpenCL library.
-   Intel, on Linux, has an implementation for CPU devices, and another for GPU devices (\"Beignet\").

The implementations will be developed in further subsections.

### [ICD]

The [[[dev-libs/opencl-icd-loader]](https://packages.gentoo.org/packages/dev-libs/opencl-icd-loader)[]] package provides a layer of indirection to enable different OpenCL implementations, and also provides the *OpenCL.pc* pkg-config descriptor.

### [][Mesa (rusticl)]

As of late-2023, installing [[[media-libs/mesa]](https://packages.gentoo.org/packages/media-libs/mesa)[]] with the `opencl` USE flag provides an OpenCL 3 installation with rusticl that works with radeonsi. To use it you must export the environment variable `RUSTICL_ENABLE=radeonsi` before running an application that uses OpenCL (e.g. `RUSTICL_ENABLE=radeonsi clinfo`).

### [][Mesa (clover)]

As of mid-2023, installing [[[media-libs/mesa]](https://packages.gentoo.org/packages/media-libs/mesa)[]] with the `opencl` USE flag provides an OpenCL 1.1 installation that works on Evergreen through Sea Islands AMD GPU families (Vega and later GPU families like Navi are not supported). See the [AMD](https://wiki.gentoo.org/wiki/OpenCL#AMD "OpenCL") section below for newer GPUs. For a full list of features see the [GalliumCompute Matrix](https://dri.freedesktop.org/wiki/GalliumCompute/).

Since media-libs/mesa-20.3 [it supports OpenCL 1.2](https://www.phoronix.com/scan.php?page=news_item&px=Mesa-20.3-OpenCL-1.2-Clover).

### [Intel - CPU]

The Intel CPU SDK is provided by the [[[dev-util/intel-ocl-sdk]](https://packages.gentoo.org/packages/dev-util/intel-ocl-sdk)[]] which is in portage.

### [Intel - GPU]

#### [Intel Graphics Compute Runtime]

Beginning with the Broadwell processor series, [Intel](https://wiki.gentoo.org/wiki/Intel "Intel") Graphics Compute Runtime for OpenCL is provided by [[[dev-libs/intel-compute-runtime]](https://packages.gentoo.org/packages/dev-libs/intel-compute-runtime)[]].

Install it manually as the [[[virtual/opencl]](https://packages.gentoo.org/packages/virtual/opencl)[]] note suggests (64-bit only):

`root `[`#`]`emerge --ask dev-libs/intel-compute-runtime`

### [[] AMD]

The newest OpenCL implementation from AMD is ROCm, Radeon Open Compute, which supports GFX8 and newer GPU chips (Fiji, Polaris, Vega). The GFX7 chips are enabled, but not officially supported. For older chips, use either the Mesa clover (above), or amdgpu-pro-opencl (below) implementations. The ROCm source is available on GitHub, at [RadeonOpenCompute/ROCm](https://github.com/RadeonOpenCompute/ROCm). ROCm is in Gentoo; install [[[dev-libs/rocm-opencl-runtime]](https://packages.gentoo.org/packages/dev-libs/rocm-opencl-runtime)[]]. For an error-free operation, it may be necessary to recompile [[[media-libs/mesa]](https://packages.gentoo.org/packages/media-libs/mesa)[]] with the `-opencl` USE flag.

For ROCm to work properly with the AMDGPU drivers, the following kernel options must be set:

[KERNEL]

    Memory Management options  --->
        [*] Memory hotplug
        [*]   Allow for memory hot remove
        [*] Device memory (pmem, HMM, etc...) hotplug support

    Device Drivers  --->
        Graphics support  --->
            <M/*> AMD GPU
            [*]   Always enable userptr write support
            <M/*> HSA kernel driver for AMD GPU devices

There also exists [[[dev-libs/amdgpu-pro-opencl]](https://packages.gentoo.org/packages/dev-libs/amdgpu-pro-opencl)[]] -package which provides ***closed source*** OpenCL libraries from Ubuntu AMDGPU-PRO driver package. These libraries are *normally* used with the closed source [AMDGPU-PRO](https://wiki.gentoo.org/wiki/AMDGPU-PRO "AMDGPU-PRO") drivers, but this package helps users to try *if* they can use them with open source [AMDGPU](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU") drivers.

** Important**\
Mixing closed source OpenCL libraries with open source drivers isn\'t officially supported in any way. However there have been success at some levels^[\[1\]](#cite_note-1)[\[2\]](#cite_note-2)^. Users who encounter problems are encouraged to ask help from the forums and not report it as a bug.

### [nVidia]

The driver is provided by the [[[dev-util/nvidia-cuda-toolkit]](https://packages.gentoo.org/packages/dev-util/nvidia-cuda-toolkit)[]] package which is in the main ebuild repository.

## [Usage notes]

### [Displaying info about OpenCL]

Information about the system\'s OpenCL capabilities can be viewed using the [[[dev-util/clinfo]](https://packages.gentoo.org/packages/dev-util/clinfo)[]] package.

### [[] Implementation validation]

An implementation (especially the experimental ones) can be checked by running test suites such as:

-   [piglit](http://cgit.freedesktop.org/piglit/): Open Source OpenGL/OpenCL test suite. Check [GalliumCompute](http://dri.freedesktop.org/wiki/GalliumCompute/#index4h3) for simple piglit tests

### [[] Implementation tuning]

The main vendors will provide some form of advanced documentation to use their hardware to the maximum:

-   nVidia: For developers targeting nVidia hardware, nVidia provides a [Best Practices Guide](http://www.nvidia.com/content/cudazone/CUDABrowser/downloads/papers/NVIDIA_OpenCL_BestPracticesGuide.pdf).
-   AMD: For developers targeting AMD hardware, AMD provides an [Optimization Guide](http://developer.amd.com/tools-and-sdks/opencl-zone/opencl-tools-sdks/amd-accelerated-parallel-processing-app-sdk/opencl-optimization-guide/).

Some characteristics are not straightforward to find. Benchmarks are one mode of discovery.

### [LLVM DLL hell]

LLVM is starting to become a central library, and it is used by most of the implementations. If the user/implementer is not careful, linkage issues can occur (symbol collisions, constructors getting called multiple times and not handled, etc.). This is something that can be noticed with many implementations also.

## [References]

1.  [[[↑](#cite_ref-1)] [[AMDGPU and OpenCL](https://www.reddit.com/r/Gentoo/comments/693gvj/amdgpu_and_opencl/dh52z2m/) - Reddit]]
2.  [[[↑](#cite_ref-2)] [[Post 8087132](https://forums.gentoo.org/viewtopic-p-8087132.html#8087132) - Gentoo Forums]]