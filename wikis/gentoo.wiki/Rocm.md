[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=ROCm&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

According to the [ROCm official document (v5.4.3)](https://docs.amd.com/bundle/ROCm-Installation-Guide-v5.4.3/page/Introduction_to_ROCm_Installation_Guide_for_Linux.html) \"ROCm is a brand name for ROCm open software platform (for software) or the ROCm™ open platform ecosystem (includes hardware like FPGAs or other CPU architectures).\"

In the scope of Gentoo distribution, \"ROCm\" refers to ROCm open software platform, currently supporting [AMDGPU](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU") as its hardware.

** Important**\
ROCm itself aims for as an environment for heterogeneous computing, not limiting to AMDGPU. It is the current packaging strategy of Gentoo that ROCm only supports AMDGPU; if ROCm is needed for other vendors (typically the cuda backend of `sci-libs/hip-*` packages), please file a bug to [Gentoo Bugzilla](https://bugs.gentoo.org/)

ROCm is somewhat analogous to [CUDA](https://en.wikipedia.org/wiki/CUDA) in the sense of providing an API ([HIPAMD](https://wiki.gentoo.org/wiki/HIP "HIP")) whose usage is in the same spirit: simplified kernels-based GPU programming. It also provides OpenCL and OpenMP and programming models. Note that ROCm is not the only way to run compute tasks on AMD GPUs as Mesa3D ([[[media-libs/mesa]](https://packages.gentoo.org/packages/media-libs/mesa)[]]) also provides this capability over its own OpenCL and Vulkan APIs.

## Contents

-   [[1] [Components of ROCm]](#Components_of_ROCm)
-   [[2] [Installation guide]](#Installation_guide)
    -   [[2.1] [Supported AMD GPUs]](#Supported_AMD_GPUs)
    -   [[2.2] [Kernel requirements]](#Kernel_requirements)
        -   [[2.2.1] [Kernel configuration options]](#Kernel_configuration_options)
        -   [[2.2.2] [Kernel command line parameters]](#Kernel_command_line_parameters)
        -   [[2.2.3] [Checking for a functional kernel configuration]](#Checking_for_a_functional_kernel_configuration)
        -   [[2.2.4] [iommu pass-through]](#iommu_pass-through)
    -   [[2.3] [Users privileges]](#Users_privileges)
    -   [[2.4] [System monitoring tools]](#System_monitoring_tools)
-   [[3] [Programming models]](#Programming_models)
    -   [[3.1] [OpenCL]](#OpenCL)
    -   [[3.2] [HIP]](#HIP)
    -   [[3.3] [OpenMP]](#OpenMP)
        -   [[3.3.1] [Enabling OpenMP for Clang/LLVM]](#Enabling_OpenMP_for_Clang.2FLLVM)
        -   [[3.3.2] [Testing OpenMP support]](#Testing_OpenMP_support)
            -   [[3.3.2.1] [If llvm-core/clang does not contain amdgpu-arch tool or the target GPU is not on the machine]](#If_llvm-core.2Fclang_does_not_contain_amdgpu-arch_tool_or_the_target_GPU_is_not_on_the_machine)
    -   [[3.4] [Others]](#Others)
-   [[4] [ROCm libraries]](#ROCm_libraries)
    -   [[4.1] [Specifying architectures to compile]](#Specifying_architectures_to_compile)
        -   [[4.1.1] [Upgrade to 5.1.3 or above from the legacy way]](#Upgrade_to_5.1.3_or_above_from_the_legacy_way)
    -   [[4.2] [Driver and userspace compatibility matrix]](#Driver_and_userspace_compatibility_matrix)
-   [[5] [XNACK target feature]](#XNACK_target_feature)
-   [[6] [Contributing and developing guide]](#Contributing_and_developing_guide)
-   [[7] [See also]](#See_also)
-   [[8] [References]](#References)

### [Components of ROCm]

[ROCm can be classified into five categories](https://www.amd.com/en/graphics/servers-solutions-rocm):

1.  Drivers and runtimes, provided by the amdgpu kernel model and `dev-libs/roct-thunk-interface` and `dev-libs/rocr-runtime`.
2.  Programming models. See [ROCm#Programming_models](https://wiki.gentoo.org/wiki/ROCm#Programming_models "ROCm") for details.
3.  Compilers and tools. Gentoo uses to vanilla clang (`>=llvm-core/clang-14.0.6-r1`).
4.  Libraries. Gentoo has packaged most libraries prefixed by `roc` and `hip` in `sci-libs` category, with `src_test` enabled. All `sci-libs/roc*` packages are written in HIP and uses hipamd as backend, while `sci-libs/hip*` are simple wrappers.
5.  Deployment tools. As a user of Gentoo, the best choice to deploy common ROCm components is via portage.

### [Installation guide]

#### [Supported AMD GPUs]

ROCm targets discrete AMD GPUs and officially supports nearly any GFX9 and later GPU generations with a few exceptions ^[\[1\]](#cite_note-1)^. Basically this covers GCN-3 (*Fiji* chips only) to GCN-5 and all RDNA micro-architectures.

A full list of officially supported hardware can be [found on AMD\'s ROCm documentation site](https://rocm.docs.amd.com/en/latest/reference/gpu-arch-specs.html#accelerator-and-gpu-hardware-specifications).

#### [Kernel requirements]

##### [Kernel configuration options]

The following kernel configuration options have be ticked:

[KERNEL]

    Device Drivers --->
      Graphics Support --->
        <M> AMD GPU
        [ ]   Enable amdgpu support for SI parts
        [ ]   Enable amdgpu support for CIK parts
        -*-   Always enable userptr write support
        ACP (Audio CoProcessor) Configuration  --->
        Display Engine Configuration  --->
        [*]   HSA kernel driver for AMD GPU devices
        [*]     Enable HMM-based shared virtual memory manager

** Note**\
You can also choose to not build the AMD GPU support as a kernel module and so make it being built-in.

##### [Kernel command line parameters]

The defaults options values for the AMDGPU kernel module are adequate and provide a stable configuration. Under some circumstances it is possible to override various options (see [drivers/gpu/drm/amd/amdgpu/amdgpu_drv.c] in the Linux kernel source tree for a detailed description of those).

For example, setting `amdgpu.ppfeaturemask=0xffffffff` gives full features in AMDGPU power play, which maybe useful when adjusting GPU power profiles via `rocm-smi`.

##### [Checking for a functional kernel configuration]

Once your Linux kernel has been reconfigured, recompiled by a manner of your choice and the machine rebooted to use it, you can check for KFD messages in the Linux kernel log. If AMDKFD (AMD Fusion Kernel Driver) which is the HSA compute Linux kernel driver has been successfully enabled for your AMD GPU you should see something like:

`root `[`#`]`dmesg | grep kfd`

    [    9.324948] kfd kfd: amdgpu: Allocated 3969056 bytes on gart
    [    9.376206] kfd kfd: amdgpu: added device 1002:73df

##### [iommu pass-through]

[According to AMD](https://community.amd.com/t5/knowledge-base/iommu-advisory-for-amd-instinct/ta-p/484601), running peer-to-peer programs on multiple GPUs may trigger system crash. The solution is to set kernel command line parameter `iommu=pt`.

Some user reports also suggest that iommu pass-through mode decreases the possibility of amdgpu driver crashes like page faults.

#### [Users privileges]

Using ROCm requires access to the character device [/dev/kfd] which is owned by `root:video`. Thus any user wanting to use ROCm should be included in the [video] group. This is achieved via:

`user `[`$`]`usermod -a -G video larry`

** Important**\
This change will be effective at their next logon.

#### [System monitoring tools]

[[[dev-util/rocm-smi]](https://packages.gentoo.org/packages/dev-util/rocm-smi)[]] provides various information about the underlying AMD GPU devices such as the die temperature, the current clock speeds and VRAM usage. To install it:

`root `[`#`]`emerge --ask dev-util/rocm-smi`

You can simply invoke it without any options to see a short summary:

`user `[`$`]`rocm-smi`

    ======================= ROCm System Management Interface =======================
    ================================= Concise Info =================================
    GPU  Temp (DieEdge)  AvgPwr  SCLK    MCLK   Fan  Perf  PwrCap  VRAM%  GPU%
    0    45.0c           7.0W    500Mhz  96Mhz  0%   auto  220.0W   16%   1%
    ================================================================================
    ============================= End of ROCm SMI Log ==============================

** Tip**\
You can invoke `rocm-smi` with the option `-a` to view a complete report.

Another package of interest is [[[dev-util/rocminfo]](https://packages.gentoo.org/packages/dev-util/rocminfo)[]] which provides detailed information about currently registered HSA devices. To install it:

`root `[`#`]`emerge --ask dev-util/rocminfo`

Then, simply invoke it to see what is usable by ROCm:

`user `[`$`]`rocminfo`

    ROCk module is loaded
    =====================
    HSA System Attributes
    =====================
    Runtime Version:         1.1
    System Timestamp Freq.:  1000.000000MHz
    Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
    Machine Model:           LARGE
    System Endianness:       LITTLE

    ==========
    HSA Agents
    ==========
    *******
    Agent 1
    *******
      Name:                    AMD Ryzen 9 7950X 16-Core Processor
      Uuid:                    CPU-XX
      Marketing Name:          AMD Ryzen 9 7950X 16-Core Processor
      Vendor Name:             CPU
      Feature:                 None specified
      Profile:                 FULL_PROFILE
      Float Round Mode:        NEAR
      Max Queue Number:        0(0x0)
      Queue Min Size:          0(0x0)
      Queue Max Size:          0(0x0)
      Queue Type:              MULTI
      Node:                    0
      Device Type:             CPU
      Cache Info:
        L1:                      32768(0x8000) KB
      Chip ID:                 0(0x0)
      ASIC Revision:           0(0x0)
      Cacheline Size:          64(0x40)
      Max Clock Freq. (MHz):   4500
      BDFID:                   0
      Internal Node ID:        0
      Compute Unit:            32
      SIMDs per CU:            0
      Shader Engines:          0
      Shader Arrs. per Eng.:   0
      WatchPts on Addr. Ranges:1
      Features:                None
      Pool Info:
        Pool 1
          Segment:                 GLOBAL; FLAGS: FINE GRAINED
          Size:                    131631704(0x7d88a58) KB
          Allocatable:             TRUE
          Alloc Granule:           4KB
          Alloc Alignment:         4KB
          Accessible by all:       TRUE
        Pool 2
          Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
          Size:                    131631704(0x7d88a58) KB
          Allocatable:             TRUE
          Alloc Granule:           4KB
          Alloc Alignment:         4KB
          Accessible by all:       TRUE
        Pool 3
          Segment:                 GLOBAL; FLAGS: COARSE GRAINED
          Size:                    131631704(0x7d88a58) KB
          Allocatable:             TRUE
          Alloc Granule:           4KB
          Alloc Alignment:         4KB
          Accessible by all:       TRUE
      ISA Info:
    *******
    Agent 2
    *******
      Name:                    gfx1031
      Uuid:                    GPU-XX
      Marketing Name:          AMD Radeon RX 6750 XT
      Vendor Name:             AMD
      Feature:                 KERNEL_DISPATCH
      Profile:                 BASE_PROFILE
      Float Round Mode:        NEAR
      Max Queue Number:        128(0x80)
      Queue Min Size:          64(0x40)
      Queue Max Size:          131072(0x20000)
      Queue Type:              MULTI
      Node:                    1
      Device Type:             GPU
      Cache Info:
        L1:                      16(0x10) KB
        L2:                      3072(0xc00) KB
        L3:                      98304(0x18000) KB
      Chip ID:                 29663(0x73df)
      ASIC Revision:           0(0x0)
      Cacheline Size:          64(0x40)
      Max Clock Freq. (MHz):   2880
      BDFID:                   768
      Internal Node ID:        1
      Compute Unit:            40
      SIMDs per CU:            2
      Shader Engines:          4
      Shader Arrs. per Eng.:   2
      WatchPts on Addr. Ranges:4
      Features:                KERNEL_DISPATCH
      Fast F16 Operation:      TRUE
      Wavefront Size:          32(0x20)
      Workgroup Max Size:      1024(0x400)
      Workgroup Max Size per Dimension:
        x                        1024(0x400)
        y                        1024(0x400)
        z                        1024(0x400)
      Max Waves Per CU:        32(0x20)
      Max Work-item Per CU:    1024(0x400)
      Grid Max Size:           4294967295(0xffffffff)
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)
        y                        4294967295(0xffffffff)
        z                        4294967295(0xffffffff)
      Max fbarriers/Workgrp:   32
      Pool Info:
        Pool 1
          Segment:                 GLOBAL; FLAGS: COARSE GRAINED
          Size:                    12566528(0xbfc000) KB
          Allocatable:             TRUE
          Alloc Granule:           4KB
          Alloc Alignment:         4KB
          Accessible by all:       FALSE
        Pool 2
          Segment:                 GROUP
          Size:                    64(0x40) KB
          Allocatable:             FALSE
          Alloc Granule:           0KB
          Alloc Alignment:         0KB
          Accessible by all:       FALSE
      ISA Info:
        ISA 1
          Name:                    amdgcn-amd-amdhsa--gfx1031
          Machine Models:          HSA_MACHINE_MODEL_LARGE
          Profiles:                HSA_PROFILE_BASE
          Default Rounding Mode:   NEAR
          Default Rounding Mode:   NEAR
          Fast f16:                TRUE
          Workgroup Max Size:      1024(0x400)
          Workgroup Max Size per Dimension:
            x                        1024(0x400)
            y                        1024(0x400)
            z                        1024(0x400)
          Grid Max Size:           4294967295(0xffffffff)
          Grid Max Size per Dimension:
            x                        4294967295(0xffffffff)
            y                        4294967295(0xffffffff)
            z                        4294967295(0xffffffff)
          FBarrier Max Size:       32
    *** Done ***

** Note**\
In the above example, the integrated GPU had been deactivated in the BIOS, thus only the CPU itself and the dGPU are usable.

### [Programming models]

#### [OpenCL]

Detailed information can be seen in [OpenCL#AMD](https://wiki.gentoo.org/wiki/OpenCL#AMD "OpenCL").

#### [HIP]

Detailed information can be seen in [HIP](https://wiki.gentoo.org/wiki/HIP "HIP").

#### [OpenMP]

##### [][Enabling OpenMP for Clang/LLVM]

To enable OpenMP offloading on AMDGPU, ensure that :

-   [[[llvm-core/clang-runtime]](https://packages.gentoo.org/packages/llvm-core/clang-runtime)[]] has been emerged with the [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag")`openmp` set
-   [[[llvm-runtimes/openmp]](https://packages.gentoo.org/packages/llvm-runtimes/openmp)[]] (LLVM/clang specific) has been emerged with the [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag") `offload` and `llvm_targets_AMDGPU` **both** set.

This is achieved by:

-   Checking if the portage configuration has `AMDGPU` set as a target for the variable `LLVM_TARGETS`:

`root `[`#`]`emerge --info`

    (...)
    LLVM_TARGETS="AMDGPU BPF X86"
    (...)

-   Adding the required statements in [/etc/portage/package.use] either by adding a file under it (if [/etc/portage/package.use]) is a directory or an entry (if [/etc/portage/package.use] is a file) like this:

[FILE] *******Package.use for offloading OpenMP on AMDGPU***

    llvm-core/clang-runtime openmp

Then re-emerge [[[llvm-core/clang-runtime]](https://packages.gentoo.org/packages/llvm-core/clang-runtime)[]] (should kick [[[llvm-runtimes/openmp]](https://packages.gentoo.org/packages/llvm-runtimes/openmp)[]] in as a dependency):

`root `[`#`]`emerge --ask --deep --newuse llvm-core/clang-runtime`

** Tip**\
You can also set the `openmp` USE flag globally by adding it to the `USE` variable defined in [/etc/portage/make.conf]

##### [Testing OpenMP support]

`user `[`$`]`clang -fno-stack-protector -fopenmp -fopenmp-targets=amdgcn-amd-amdhsa -Xopenmp-target=amdgcn-amd-amdhsa --rocm-path=/opt/gentoo/usr --rocm-device-lib-path=/opt/gentoo/usr/lib/amdgcn/bitcode <openmp source code> -o <executable>`

** Note**\
`-fno-stack-protector` is needed because Gentoo has turned on `-fstack-protector-strong` in `/etc/clang/gentoo-hardened.cfg`, see [llvm-project/issues/62066](https://github.com/llvm/llvm-project/issues/62066) and [[[bug #890377]](https://bugs.gentoo.org/show_bug.cgi?id=890377)[]].

If clang omits `error: no library 'libomptarget-amdgpu-gfx1031.bc' found in the default clang lib directory or in LIBRARY_PATH; use '--libomptarget-amdgpu-bc-path' to specify amdgpu bitcode library` Then adding `--libomptarget-amdgpu-bc-path=/usr/lib64/` to the compile command resolve this issue.

###### [][If llvm-core/clang does not contain amdgpu-arch tool or the target GPU is not on the machine]

Clang omits `error: cannot determine AMDGPU architecture: amdgpu-arch: Execute failed: Executable "amdgpu-arch" doesn't exist!`.

In this case clang cannot detect gpu architecture automatically (or in cross compile, arch is not present on compile machine), so clang needs a GPU arch specifier script:

[FILE] **`/tmp/print_gpu_arch.sh`GPU arch specifier**

    #!/bin/bash
    echo "gfx90a"  # Change to the target to compile here, but do not append target features such as :xnack-

Make script executable:

`user `[`$`]`chmod +x /tmp/print_gpu_arch.sh`

And then add option `--amdgpu-arch-tool=/tmp/print_gpu_arch.sh` to the compilation command.

#### [Others]

The backend of ROCm is currently llvm/clang, so any programming model that can generate LLVM IR for AMDGPU can use ROCm. [Numba](https://github.com/numba/numba) is a jit compiler for python codes, and can offload to ROCm. Currently Gentoo does not packaged numba with ROCm yet.

### [ROCm libraries]

Currently, Gentoo has packages `rocBLAS`, `rocFFT`, `rocPRIM`, `rocRAND`, `rocSOLVER`, `rocSPARSE`, `rocThrust`, `composable-kernel`, `miopen`, and `pytorch[rocm]` in `sci-libs` category. Those are math and deep learning libraries written in HIP and runs on AMD GPUs.

Wrapper packages, are `hipBLAS` (wrapper of `rocBLAS`+`rocSOLVER` vs `cuBLAS`+`cuSOLVER`), `hipCUB` (wrapper of `rocPRIM` vs `CUB`), `hipFFT`(`rocFFT` vs `cuFFT`), and `hipSPARSE`(`rocSPARSE` vs `cuSPARSE`).

`hipDNN` is currently not packaged. It\'s a wrapper of `miopen` vs `cudnn`.

`dev-libs/rccl` (targeting `nccl`) is collective communication routines for AMD GPUs. It can also run tests, but tests are only meaningful on multi GPU systems.

Ebuild for `sci-libs/rocALUTION` (targeting [paralution](https://www.paralution.com/)) is currently in development.

#### [Specifying architectures to compile]

With `rocm.eclass` (ROCm version \>=5.1.3), Gentoo handles the `AMDGPU_TARGETS` `USE_EXPAND`. The map between GPU and arch name can be viewed via checking use flag for ROCm libraries:

`example $``equery uses rocBLAS`

     * Found these USE flags for sci-libs/rocBLAS-6.4.1:
     U I
     - - amdgpu_targets_gfx1010 : RDNA GPU, codename navi10, including Radeon RX 5700XT/5700/5700M/5700B/5700XTB/5600XT/5600/5600M, Radeon Pro 5700XT/5700, Radeon Pro W5700X/W5700
     - - amdgpu_targets_gfx1011 : RDNA GPU, codename navi12, including Radeon Pro 5600M/V520
     - - amdgpu_targets_gfx1012 : RDNA GPU, codename navi14, including Radeon RX 5500XT/5500/5500M/5500XTB/5300/5300M, Radeon Pro 5500XT/5500M/5300/5300M, Radeon Pro W5500X/W5500/W5500M/W5300M
     + - amdgpu_targets_gfx1030 : RDNA2 GPU, codename navi21/sienna cichlid, including Radeon RX 6950XT/6900XT/6800XT/6800, Radeon Pro W6800
     - - amdgpu_targets_gfx1031 : RDNA2 GPU, codename navi22/navy flounder, including Radeon RX 6750XT/6700XT/6800M/6700M
     + + amdgpu_targets_gfx1100 : RDNA3 GPU, codename navi31/plum bonito, including Radeon RX 7900XTX/7900XT, AMD Radeon Pro W7900/W7800
     - - amdgpu_targets_gfx1101 : RDNA3 GPU, codename navi32, including Radeon RX 7700XT/7800XT
     - - amdgpu_targets_gfx1102 : RDNA3 GPU, codename navi33, including Radeon RX 7600/7600M/7600M XT/7700S/7600S, AMD Radeon PRO W7600/W7500
     - - amdgpu_targets_gfx1200 : RDNA4 GPU, codename navi44, including Radeon RX 9060XT
     - - amdgpu_targets_gfx1201 : RDNA4 GPU, codename navi48, including Radeon RX 9070/9070XT/9070GRE and Radeon AI PRO R9700
     - - amdgpu_targets_gfx803  : Fiji GPU, codename fiji, including Radeon R9 Nano/Fury/FuryX, Radeon Pro Duo, FirePro S9300x2, Radeon Instinct MI8
     - - amdgpu_targets_gfx900  : Vega GPU, codename vega10, including Radeon Vega Frontier Edition, Radeon RX Vega 56/64, Radeon RX Vega 64 Liquid, Radeon Pro Vega 48/56/64/64X, Radeon Pro WX
                                  8200/9100, Radeon Pro V320/V340/SSG, Radeon Instinct MI25
     - - amdgpu_targets_gfx906  : Vega GPU, codename vega20, including Radeon (Pro) VII, Radeon Instinct MI50/MI60
     + - amdgpu_targets_gfx908  : CDNA Accelerator, codename arcturus, including AMD Instinct MI100 Accelerator
     + - amdgpu_targets_gfx90a  : CDNA2 Accelerator, codename aldebaran, including AMD Instinct MI200 series Accelerators
     - - amdgpu_targets_gfx940  : CDNA3 Accelerator, codename aqua_vangaram, MI300A rev 0
     - - amdgpu_targets_gfx941  : CDNA3 Accelerator, codename aqua_vangaram, MI300X rev 0
     + - amdgpu_targets_gfx942  : CDNA3 Accelerator, codename aqua_vangaram, MI300A and MI300X rev >=1
     - - benchmark              : Build and install rocblas-bench.
     - - doc                    : Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
     - + hipblaslt              : Build with hipBLASLt for some non-batched and strided batched problems on gfx12.
     + + llvm_slot_20           : Use LLVM 20.
     - - test                   : Perform rocblas-test to compare the result between rocBLAS and system BLAS.
     + + video_cards_amdgpu     : VIDEO_CARDS setting to build driver for AMDGPU video cards

By default, officially supported architectures are turned on. This list is usually different for each major ROCm release. For example, ROCm-5.7.1 supported `gfx906 gfx908 gfx90a gfx1030`, ROCm-6.0 added support of `gfx942 gfx1100`, ROCm-6.4.1 dropped support of `gfx906` (but unofficially target `gfx906` is still available). Compilation for all supported architectures may take hours. Notably, flagship AMD Instinct MI325X GPU for datacenters, architecture `gfx942`, produces gigabytes of specialized code. Therefore it is highly recommended to limit targets to specific architecture. For example, for a system with Radeon VII and RX 6700XT, specify GPU archs for all packages:

[FILE] **`/etc/portage/package.use/00-amdgpu-targets`Example for AMDGPU_TARGETS use flag**

    # disable all targets except for gfx1031 and gfx906
    */* AMDGPU_TARGETS: -* gfx1031 gfx906

Adjusting use flags for individual packages is also supported. Portage will take care of the dependencies: if `sci-libs/miopen` enables `gfx1031`, then `sci-libs/rocBLAS` should turns on `gfx1031`, or when portage will try to add it to `/etc/portage/package.use/zz-autounmask`.

##### [Upgrade to 5.1.3 or above from the legacy way]

Before introducing `rocm.eclass` (ROCm version \<5.1.3), architectures are specified via environment variable `AMDGPU_TARGETS`:

For users installing ROCm libraries using the legacy method (specifying `/etc/portage/make.conf`), upgrading to 5.1.3 takes two steps:

    1. Remove AMDGPU_TARGETS entry in /etc/portage/make.conf
    2. Add /etc/portage/package.use/00-amdgpu-targets mentioned in ROCm#Specifying_architectures_to_compile

#### [Driver and userspace compatibility matrix]

See [User and kernel-space support matrix](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/user-kernel-space-compat-matrix.html), where column \"KFD\" refers to the version of `dev-libs/roct-thunk-interface` and the ROCm version of amdkfd in amdgpu kernel module (if using upstream amdgpu module Linux kernel, there\'s no clear ROCm version for amdkfd kernel driver).

### [XNACK target feature]

NACK stands for [negative-acknowledgement](https://en.wikipedia.org/wiki/Acknowledgement_(data_networks)). It is an important feature in Heterogeneous Memory Management (HMM) ^[\[2\]](#cite_note-2)^. Simply put, in HMM GPU VRAM and CPU RAM shares the same pointer space, while xnack allows the GPU to retry memory accesses after a page fault when the desired data does not exist in GPU VRAM, making VRAM kind of a cache of CPU RAM for GPU devices. ROCm official document ^[\[3\]](#cite_note-3)^ and other documents may help better understanding the mechanism and importance of xnack, how to enable it, and the performance impact: ^[\[4\]](#cite_note-4)^ ^[\[5\]](#cite_note-5)^

For GFX9 series GPUs, it is common to append xnack feature flag behind GPU architecture, for example `gfx906:xnack-`. `xnack-` stands for xnack disabled, while `xnack+` is xnack enabled, and the compiled GPU kernel can be only executed when xnack feature is disabled. `gfx906` stands for \"xnack any\", meaning GPU kernel can be launched in both xnack on or xnack off, but **may** be less performant ^[\[6\]](#cite_note-6)^.

Whether GPU has xnack feature enabled can be checked with `rocminfo`.

### [Contributing and developing guide]

Testing [ROCm libraries](https://wiki.gentoo.org/wiki/ROCm#ROCm_libraries "ROCm") is not easy \-- it requires recent AMD discrete GPUs and days of compilation and testing. If using [ROCm libraries](https://wiki.gentoo.org/wiki/ROCm#ROCm_libraries "ROCm") and mathematical correctness is considered important, please test the hardware by enabling tests:

[FILE] **`/etc/portage/make.conf`**

    FEATURES="test"

Then emerge the desired ROCm package. If test failures occurs, usually it is caused by small inconsistencies between [ROCm libraries](https://wiki.gentoo.org/wiki/ROCm#ROCm_libraries "ROCm") and CPU reference implementations. Or it is caused by upstream bugs, or Gentoo deployment strategy. In either situation, filing a bug report to Gentoo Bugzilla is welcome, and it would be better to report to upstream for mathematical errors.

There is a page [ROCm packaging history](https://wiki.gentoo.org/wiki/ROCm_packaging_history "ROCm packaging history") working in progress.

## [See also]

-   [AMDGPU](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU") --- the open source graphics drivers for AMD Radeon and other GPUs.
-   [Nvidia](https://wiki.gentoo.org/wiki/Nvidia "Nvidia") --- a popular graphical chipset manufacturer.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html)]]
2.  [[[↑](#cite_ref-2)] [[Kernel document for HMM](https://www.kernel.org/doc/html/v5.8/vm/hmm.html)]]
3.  [[[↑](#cite_ref-3)] [[ROCm document on XNACK](https://rocm.docs.amd.com/en/latest/conceptual/gpu-memory.html#xnack)]]
4.  [[[↑](#cite_ref-4)] [[Blog by ROCm user niconiconi](https://niconiconi.neocities.org/tech-notes/xnack-on-amd-gpus/)]]
5.  [[[↑](#cite_ref-5)] [[Page migration document from Oak Ridge National Library](https://docs.olcf.ornl.gov/systems/crusher_quick_start_guide.html#enabling-gpu-page-migration)]]
6.  [[[↑](#cite_ref-6)] [[LLVM document on AMDGPU target feature](https://llvm.org/docs/AMDGPUUsage.html#target-features)]]