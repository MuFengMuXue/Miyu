[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Tensile&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Tensile**, as a part of [ROCm](https://wiki.gentoo.org/wiki/ROCm "ROCm") stack, is a development toolkit for tuning GEMM operation on GPUs via benchmarks, and then create backend libraries for GEMM applications (rocBLAS).

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
    -   [[1.2] [Usage]](#Usage)
        -   [[1.2.1] [Running benchmarks to stretch GPU GEMM performance]](#Running_benchmarks_to_stretch_GPU_GEMM_performance)

## [Installation]

[[[dev-util/Tensile]](https://packages.gentoo.org/packages/dev-util/Tensile)[]] installs the python scripts for running benchmarks, analyzing data, and building backend libraries. It also ships various common benchmark configurations and shell scripts, as well as C++ source code for building tensile_client.

### [Emerge]

Install [[[dev-util/Tensile]](https://packages.gentoo.org/packages/dev-util/Tensile)[]]:

`root `[`#`]`emerge --ask dev-util/Tensile`

### [Usage]

#### [Running benchmarks to stretch GPU GEMM performance]

Please refer to the [official Tensile wiki](https://github.com/ROCmSoftwarePlatform/Tensile/wiki) about how to write benchmark configurations and run benchmarks. Since Gentoo already installs the command `Tensile`, so extra installation is not needed, just execute

`user `[`$`]`Tensile [-v] --global-parameters=Architecture=<your GPU arch> <benchmark_config.ymal> <benchmark_directory>`