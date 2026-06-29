[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=HIP&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**HIP** is the acronym of \"Heterogeneous-Compute Interface for Portability\". HIP is a C++ dialect to help conversion of Cuda applications to C++ in a portable manner. In other words, HIP is an abstraction layer that can either use the underlying lower-level ROCm libraries if your system has an AMD GPU or redirect the calls to CUDA if you have an nVidia GPU. As stated in the [HIP FAQ](https://github.com/ROCm-Developer-Tools/HIP/blob/develop/docs/markdown/hip_faq.md):

> HIP provides porting tools which do most of the work to convert CUDA code into portable C++ code that uses the HIP APIs. Most developers will port their code from CUDA to HIP and then maintain the HIP version. HIP code provides the same performance as native CUDA code, plus the benefits of running on AMD platforms.

**However it is not CUDA a drop-in and it only supports a CUDA functions sub-set.**

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Additional software]](#Additional_software)
-   [[2] [HIP Utilities]](#HIP_Utilities)
    -   [[2.1] [hipcc (Clang wrapper)]](#hipcc_.28Clang_wrapper.29)
    -   [[2.2] [hipconfig]](#hipconfig)
-   [[3] [Testing your HIP installation]](#Testing_your_HIP_installation)
-   [[4] [More advanced topics]](#More_advanced_topics)
-   [[5] [References]](#References)

## [Installation]

[[[dev-util/hip]](https://packages.gentoo.org/packages/dev-util/hip)[]] pulls in basic libraries, APIs and utilities that can compile and run a HIP program. Several other HIP/ROCm libaries can be found in `sci-libs`.

** Warning**\
[[[dev-util/hip]](https://packages.gentoo.org/packages/dev-util/hip)[]] uses the system LLVM/Clang (as provided by [[[sys-devel/clang]](https://packages.gentoo.org/packages/sys-devel/clang)[]] and related packages).

### [USE flags]

### [USE flags for] [dev-util/hip](https://packages.gentoo.org/packages/dev-util/hip) [[]] [C++ Heterogeneous-Compute Interface for Portability]

  --------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+hip`](https://packages.gentoo.org/useflags/+hip)                               Build HIP runtime
  [`debug`](https://packages.gentoo.org/useflags/debug)                             Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`doc`](https://packages.gentoo.org/useflags/doc)                                 Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`numa`](https://packages.gentoo.org/useflags/numa)                               Enable NUMA support using sys-process/numactl (NUMA kernel support is also required)
  [`opencl`](https://packages.gentoo.org/useflags/opencl)                           Build vendored OpenCL runtime
  [`test`](https://packages.gentoo.org/useflags/test)                               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`video_cards_amdgpu`](https://packages.gentoo.org/useflags/video_cards_amdgpu)   Build for AMD platform
  [`video_cards_nvidia`](https://packages.gentoo.org/useflags/video_cards_nvidia)   Build for Nvidia platform
  --------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-11 14:55] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[dev-util/hip]](https://packages.gentoo.org/packages/dev-util/hip)[]]:

`root `[`#`]`emerge --ask dev-util/hip`

** Note**\
hipcc is a Perl wrapper of Clang. By default, clang uses libstdc++ provided by gcc ([[[sys-devel/gcc]](https://packages.gentoo.org/packages/sys-devel/gcc)[]]), and that causes bugs sometimes (e.g. [[[bug #842405]](https://bugs.gentoo.org/show_bug.cgi?id=842405)[]] and [[[bug #857126]](https://bugs.gentoo.org/show_bug.cgi?id=857126)[]], both fixed).

### [Additional software]

Extra utilities, such as profiler for HIP program, can also be installed:

`root `[`#`]`emerge --ask dev-util/rocprofiler`

## [HIP Utilities]

#### [][hipcc (Clang wrapper)]

Using Clang/LLVM to compile a C++ HIP program requires several \"cumbersome\" command-line parameters. Fortunately, [[[dev-util/hip]](https://packages.gentoo.org/packages/dev-util/hip)[]] provides a clang wrapper called [hipcc], which handles the underlying complexity of Clang invocation.

To automatically detect GPU architecture and compile a HIP program, run:

`user `[`$`]`hipcc foo.cpp -o bar`

To specify GPU architectures and fine-tune the features to be used, use the `--offload-arch` command-line option:

`user `[`$`]`hipcc --offload-arch=gfx906:sramecc+:xnack- --offload-arch=gfx90a:sramecc+:xnack+ --offload-arch=gfx1031 foo.cpp -o bar`

For architecture argument, see [LLVM AMDGPU processors](https://llvm.org/docs/AMDGPUUsage.html#processors) for details.

To view the detailed clang command executed, set the `HIPCC_VERBOSE` environment variable to `1` on the command-line (or export it). For the above command it should give something like:

`user `[`$`]`HIPCC_VERBOSE=1 hipcc --offload-arch=gfx906:sramecc+:xnack- --offload-arch=gfx90a:sramecc+:xnack+ --offload-arch=gfx1031 foo.cpp -o bar`

    /usr/lib/llvm/15/bin/clang++  --offload-arch=gfx906:sramecc+:xnack- --offload-arch=gfx90a:sramecc+:xnack+ --offload-arch=gfx1031 -fno-stack-protector -O3 -mllvm -amdgpu-early-inline-all=true -mllvm -amdgpu-function-calls=false --rocm-path="/usr" --hip-device-lib-path="/usr/lib/amdgcn/bitcode"  -L"/usr/lib64" -O3 -lgcc_s -lgcc -lpthread -lm -lrt  -x hip foo.cpp -o "bar" -Wl,--enable-new-dtags -lamdhip64  -L/usr/lib/llvm/15/bin/../../../../lib/clang/16/lib/linux -lclang_rt.builtins-x86_64

Libraries list and path parameters put aside, notice the parameters:

-   **-x** : to tell the compiler to threat `foo.cpp` as C++ HIP file (not a \"regular\" C++ file)
-   **\--rocm-path** : the root path where the ROCm stuff resides
-   **\--hip-device-lib-path** : the path to find the GPU bitcode files
-   **-amdgpu-early-inline-all=true -amdgpu-function-calls=false** is a workaround for some use cases discussed [here](https://docs.amd.com/bundle/ROCm-Compiler-Reference-Guide-v5.3/page/Introduction_to_Compiler_Reference_Guide.html). Quoting:

> amdclang++ relies on inlining heuristics to control inlining. Users experiencing performance or compilation issues with code using file scoped or device function scoped \_\_shared\_\_ variables could try -mllvm -amdgpu-early-inline-all=true -mllvm -amdgpu-function-calls=false to work around the issue. These issues will be addressed in future compiler improvements.

-   **-fno-stack-protector** is a workaround for [hardened toolchain flags](https://wiki.gentoo.org/wiki/Hardened/Toolchain "Hardened/Toolchain"), which include `-fstack-protector-strong`. Until [fix](https://github.com/llvm/llvm-project/pull/70799) in Clang-18.1.0, Clang attempts to add stack-protector even to targets, which does not have runtime support, causing ineffective code or crashes during compilation. hipcc disables stack-protector for that reason.

#### [hipconfig]

`hipconfig` is a Perl script for displaying the configuration of HIP.

Displaying full information:

`user `[`$`]`hipconfig --full`

    HIP version  : 5.4.3

    == hipconfig
    HIP_PATH     : /usr
    ROCM_PATH    : /usr
    HIP_COMPILER : clang
    HIP_PLATFORM : amd
    HIP_RUNTIME  : rocclr
    CPP_CONFIG   :  -D__HIP_PLATFORM_HCC__= -D__HIP_PLATFORM_AMD__= -I/usr/include -I/usr/lib/llvm/15/bin/../lib/clang/15.0.7 -I/usr/include

    == hip-clang
    HSA_PATH         : /usr
    HIP_CLANG_PATH   : /usr/lib/llvm/15/bin
    clang version 15.0.7
    Target: x86_64-pc-linux-gnu
    Thread model: posix
    InstalledDir: /usr/lib/llvm/15/bin
    Configuration file: /etc/clang/clang++.cfg
    LLVM (http://llvm.org/):
      LLVM version 15.0.7
      Optimized build.
      Default target: x86_64-pc-linux-gnu
      Host CPU: znver3

      Registered Targets:
        aarch64    - AArch64 (little endian)
        aarch64_32 - AArch64 (little endian ILP32)
        aarch64_be - AArch64 (big endian)
        amdgcn     - AMD GCN GPUs
        arm        - ARM
        arm64      - ARM64 (little endian)
        arm64_32   - ARM64 (little endian ILP32)
        armeb      - ARM (big endian)
        avr        - Atmel AVR Microcontroller
        bpf        - BPF (host endian)
        bpfeb      - BPF (big endian)
        bpfel      - BPF (little endian)
        hexagon    - Hexagon
        lanai      - Lanai
        mips       - MIPS (32-bit big endian)
        mips64     - MIPS (64-bit big endian)
        mips64el   - MIPS (64-bit little endian)
        mipsel     - MIPS (32-bit little endian)
        msp430     - MSP430 [experimental]
        nvptx      - NVIDIA PTX 32-bit
        nvptx64    - NVIDIA PTX 64-bit
        ppc32      - PowerPC 32
        ppc32le    - PowerPC 32 LE
        ppc64      - PowerPC 64
        ppc64le    - PowerPC 64 LE
        r600       - AMD GPUs HD2XXX-HD6XXX
        riscv32    - 32-bit RISC-V
        riscv64    - 64-bit RISC-V
        sparc      - Sparc
        sparcel    - Sparc LE
        sparcv9    - Sparc V9
        systemz    - SystemZ
        thumb      - Thumb
        thumbeb    - Thumb (big endian)
        ve         - VE
        wasm32     - WebAssembly 32-bit
        wasm64     - WebAssembly 64-bit
        x86        - 32-bit X86: Pentium-Pro and above
        x86-64     - 64-bit X86: EM64T and AMD64
        xcore      - XCore
    hip-clang-cxxflags :  -fno-stack-protector -O3
    hip-clang-ldflags  :  -L"/usr/lib64" -O3 -lgcc_s -lgcc -lpthread -lm -lrt

    (...)
    [REDACTED]

## [Testing your HIP installation]

To test the installation, start by downloading [a simple example](https://raw.githubusercontent.com/ROCm-Developer-Tools/HIP-CPU/master/examples/vadd_hip/vadd_hip.cpp) from the ROCm GitHub repository:

`user `[`$`]`cd /tmp && wget `[`https://raw.githubusercontent.com/ROCm-Developer-Tools/HIP-CPU/master/examples/vadd_hip/vadd_hip.cpp`](https://raw.githubusercontent.com/ROCm-Developer-Tools/HIP-CPU/master/examples/vadd_hip/vadd_hip.cpp)

Then simply compile it with `hipcc`:

`user `[`$`]`hipcc vadd_hip.cpp -o vadd_hip`

and run it:

`user `[`$`]`./vadd_hip`

    PASSED!

So far so good. For those unfamiliar with GPU computing, this simple program does the following:

1.  It allocates three buffers of 1,000,000 `float` numbers each in the main (host) memory, those are named `A_h`, `B_h` and `C_h` (by coding convention \'h\' for \'host\')
2.  It does the same on the GPU device (i.e. your discrete video card or iGPU), respectively named `A_d`, `B_d` and `C_d`
3.  It initializes two of the buffers (`A_h` and `B_h`) with some numbers
4.  It copies the contents of A and B buffers from the host to their counterpart on the device so `A_h` is copied into `A_d` and `B_h` into `B_d`
5.  It then spawns the HIP kernel (i.e. the function `vadd_hip()`) on the GPU device. That kernel takes the numbers stored in `A_d` and `B_d` and sum them **in parallel** using the GPU compute units and puts the results in `C_d` (So `C_d[0] = A_d[0] + B_d[0]`, `C_d[1] = A_d[1] + B_d[1]` and so on)
6.  The results stored in `C_d` are copied back in the main memory (i.e. into `C_h`)
7.  The very same calculations are done on CPU and the results is compared to what has been computed on the GPU device
8.  If differences between the results computed on the CPU and GPU are found, an error message is shown else \"PASSED!\" is displayed.

It is also possible to have a very detailed trace of what is going on using the `AMD_LOG_LEVEL`^[\[1\]](#cite_note-1)[\[2\]](#cite_note-2)^ environment variable. Its value can be between `0`(`LOG_NONE`) to `4` (`LOG_DEBUG`) that latter value giving the maximum amount of details.

For the above example:

`user `[`$`]`AMD_LOG_LEVEL=4 ./vadd_hip`

    :3:rocdevice.cpp            :426 : 102993786016 us: 17154: [tid:0x7f0824e798c0] Initializing HSA stack.
    :3:comgrctx.cpp             :33  : 102993789633 us: 17154: [tid:0x7f0824e798c0] Loading COMGR library.
    :3:rocdevice.cpp            :205 : 102993789651 us: 17154: [tid:0x7f0824e798c0] Numa selects cpu agent[0]=0x55d4bf5bd3f0(fine=0x55d4bf5bd5e0,coarse=0x55d4bf5be150) for gpu agent=0x55d4bf5bed80
    :3:rocdevice.cpp            :1633: 102993789745 us: 17154: [tid:0x7f0824e798c0] HMM support: 1, xnack: 0, direct host access: 0

    :4:rocdevice.cpp            :1942: 102993789770 us: 17154: [tid:0x7f0824e798c0] Allocate hsa host memory 0x7f0835fb2000, size 0x28
    :4:rocdevice.cpp            :1942: 102993789958 us: 17154: [tid:0x7f0824e798c0] Allocate hsa host memory 0x7f0723000000, size 0x101000
    :4:rocdevice.cpp            :1942: 102993790163 us: 17154: [tid:0x7f0824e798c0] Allocate hsa host memory 0x7f0722e00000, size 0x101000
    :4:runtime.cpp              :83  : 102993790172 us: 17154: [tid:0x7f0824e798c0] init
    :3:hip_context.cpp          :50  : 102993790173 us: 17154: [tid:0x7f0824e798c0] Direct Dispatch: 1
    :4:rocdevice.cpp            :2069: 102993790201 us: 17154: [tid:0x7f0824e798c0] Allocate hsa device memory 0x7f0722800000, size 0x3d0900
    :3:rocdevice.cpp            :2108: 102993790203 us: 17154: [tid:0x7f0824e798c0] device=0x55d4bf60b850, freeMem_ = 0xfec2f700
    :3:hip_memory.cpp           :513 : 102993790333 us: 17154: [tid:0x7f0824e798c0] hipMalloc: Returned hipSuccess : 0x7f0722800000
    :3:hip_memory.cpp           :511 : 102993790386 us: 17154: [tid:0x7f0824e798c0]  hipMalloc ( 0x7ffd49f8a068, 4000000 )
    :4:rocdevice.cpp            :2069: 102993790400 us: 17154: [tid:0x7f0824e798c0] Allocate hsa device memory 0x7f0722200000, size 0x3d0900
    :3:rocdevice.cpp            :2108: 102993790402 us: 17154: [tid:0x7f0824e798c0] device=0x55d4bf60b850, freeMem_ = 0xfe85ee00
    :3:hip_memory.cpp           :513 : 102993790403 us: 17154: [tid:0x7f0824e798c0] hipMalloc: Returned hipSuccess : 0x7f0722200000: duration: 17 us
    :3:hip_memory.cpp           :511 : 102993790405 us: 17154: [tid:0x7f0824e798c0]  hipMalloc ( 0x7ffd49f8a060, 4000000 )
    :4:rocdevice.cpp            :2069: 102993790416 us: 17154: [tid:0x7f0824e798c0] Allocate hsa device memory 0x7f0721c00000, size 0x3d0900
    :3:rocdevice.cpp            :2108: 102993790417 us: 17154: [tid:0x7f0824e798c0] device=0x55d4bf60b850, freeMem_ = 0xfe48e500
    :3:hip_memory.cpp           :513 : 102993790418 us: 17154: [tid:0x7f0824e798c0] hipMalloc: Returned hipSuccess : 0x7f0721c00000: duration: 13 us
    :3:hip_memory.cpp           :582 : 102993792039 us: 17154: [tid:0x7f0824e798c0]  hipMemcpy ( 0x7f0722800000, 0x7f0824aa0010, 4000000, hipMemcpyHostToDevice )
    :3:rocdevice.cpp            :2703: 102993792045 us: 17154: [tid:0x7f0824e798c0] number of allocated hardware queues with low priority: 0, with normal priority: 0, with high priority: 0, maximum per priority is: 4
    :3:rocdevice.cpp            :2777: 102993795416 us: 17154: [tid:0x7f0824e798c0] created hardware queue 0x7f0835fa2000 with size 16384 with priority 1, cooperative: 0
    :4:rocdevice.cpp            :1942: 102993795582 us: 17154: [tid:0x7f0824e798c0] Allocate hsa host memory 0x7f0720a00000, size 0x100000
    :3:devprogram.cpp           :2676: 102993889143 us: 17154: [tid:0x7f0824e798c0] Using Code Object V4.
    :3:devprogram.cpp           :2979: 102993889685 us: 17154: [tid:0x7f0824e798c0] For Init/Fini: Kernel Name: __amd_rocclr_streamOpsWrite
    :3:devprogram.cpp           :2979: 102993889688 us: 17154: [tid:0x7f0824e798c0] For Init/Fini: Kernel Name: __amd_rocclr_fillImage
    :3:devprogram.cpp           :2979: 102993889689 us: 17154: [tid:0x7f0824e798c0] For Init/Fini: Kernel Name: __amd_rocclr_fillBufferAligned2D
    :3:devprogram.cpp           :2979: 102993889690 us: 17154: [tid:0x7f0824e798c0] For Init/Fini: Kernel Name: __amd_rocclr_copyImageToBuffer
    :3:devprogram.cpp           :2979: 102993889691 us: 17154: [tid:0x7f0824e798c0] For Init/Fini: Kernel Name: __amd_rocclr_copyImage1DA
    :3:devprogram.cpp           :2979: 102993889692 us: 17154: [tid:0x7f0824e798c0] For Init/Fini: Kernel Name: __amd_rocclr_fillBufferAligned
    :3:devprogram.cpp           :2979: 102993889693 us: 17154: [tid:0x7f0824e798c0] For Init/Fini: Kernel Name: __amd_rocclr_copyImage
    :3:devprogram.cpp           :2979: 102993889694 us: 17154: [tid:0x7f0824e798c0] For Init/Fini: Kernel Name: __amd_rocclr_streamOpsWait
    :3:devprogram.cpp           :2979: 102993889694 us: 17154: [tid:0x7f0824e798c0] For Init/Fini: Kernel Name: __amd_rocclr_copyBufferRectAligned
    :3:devprogram.cpp           :2979: 102993889695 us: 17154: [tid:0x7f0824e798c0] For Init/Fini: Kernel Name: __amd_rocclr_copyBufferRect
    :3:devprogram.cpp           :2979: 102993889696 us: 17154: [tid:0x7f0824e798c0] For Init/Fini: Kernel Name: __amd_rocclr_copyBufferAligned
    :3:devprogram.cpp           :2979: 102993889697 us: 17154: [tid:0x7f0824e798c0] For Init/Fini: Kernel Name: __amd_rocclr_copyBufferToImage
    :3:devprogram.cpp           :2979: 102993889698 us: 17154: [tid:0x7f0824e798c0] For Init/Fini: Kernel Name: __amd_rocclr_copyBuffer
    :4:command.cpp              :349 : 102993889736 us: 17154: [tid:0x7f0824e798c0] Command (CopyHostToDevice) enqueued: 0x55d4bfbfe270
    :4:rocmemory.cpp            :944 : 102993889938 us: 17154: [tid:0x7f0824e798c0] Locking to pool 0x55d4bf5be150, size 0x3d1000, HostPtr = 0x7f0824aa0000, DevPtr = 0x7f0720600000
    :4:rocblit.cpp              :664 : 102993889951 us: 17154: [tid:0x7f0824e798c0] HSA Asycn Copy dst=0x7f0722800000, src=0x7f0720600010, size=0, wait_event=0x7f0835fc4800, completion_signal=0x7ffd49f89870
    :4:rocvirtual.cpp           :550 : 102993890283 us: 17154: [tid:0x7f0824e798c0] Host wait on completion_signal=0x7f0835fc4800
    :3:rocvirtual.hpp           :61  : 102993890285 us: 17154: [tid:0x7f0824e798c0] Host active wait for Signal = (0x7f0835fc4800) for -1 ns
    :4:command.cpp              :289 : 102993890466 us: 17154: [tid:0x7f0824e798c0] Queue marker to command queue: 0x55d4bf5b8720
    :4:command.cpp              :349 : 102993890468 us: 17154: [tid:0x7f0824e798c0] Command (InternalMarker) enqueued: 0x55d4bfb6ebe0
    :4:command.cpp              :179 : 102993890470 us: 17154: [tid:0x7f0824e798c0] Command 0x55d4bfbfe270 complete
    :4:command.cpp              :173 : 102993890471 us: 17154: [tid:0x7f0824e798c0] Command 0x55d4bfb6ebe0 complete (Wall: 102993890470, CPU: 0, GPU: 0 us)
    :4:command.cpp              :253 : 102993890472 us: 17154: [tid:0x7f0824e798c0] Waiting for event 0x55d4bfbfe270 to complete, current status 0
    :4:command.cpp              :268 : 102993890473 us: 17154: [tid:0x7f0824e798c0] Event 0x55d4bfbfe270 wait completed
    :3:hip_memory.cpp           :583 : 102993890476 us: 17154: [tid:0x7f0824e798c0] hipMemcpy: Returned hipSuccess : : duration: 98437 us
    :3:hip_memory.cpp           :582 : 102993890480 us: 17154: [tid:0x7f0824e798c0]  hipMemcpy ( 0x7f0722200000, 0x7f08246cf010, 4000000, hipMemcpyHostToDevice )
    :4:command.cpp              :349 : 102993890483 us: 17154: [tid:0x7f0824e798c0] Command (CopyHostToDevice) enqueued: 0x55d4bfbfe270
    :4:rocmemory.cpp            :944 : 102993890634 us: 17154: [tid:0x7f0824e798c0] Locking to pool 0x55d4bf5be150, size 0x3d1000, HostPtr = 0x7f08246cf000, DevPtr = 0x7f071ae00000
    :4:rocblit.cpp              :664 : 102993890636 us: 17154: [tid:0x7f0824e798c0] HSA Asycn Copy dst=0x7f0722200000, src=0x7f071ae00010, size=0, wait_event=0x7f0835fc4780, completion_signal=0x0
    :4:rocvirtual.cpp           :550 : 102993890638 us: 17154: [tid:0x7f0824e798c0] Host wait on completion_signal=0x7f0835fc4780
    :3:rocvirtual.hpp           :61  : 102993890639 us: 17154: [tid:0x7f0824e798c0] Host active wait for Signal = (0x7f0835fc4780) for -1 ns
    :4:command.cpp              :289 : 102993890805 us: 17154: [tid:0x7f0824e798c0] Queue marker to command queue: 0x55d4bf5b8720
    :4:command.cpp              :349 : 102993890807 us: 17154: [tid:0x7f0824e798c0] Command (InternalMarker) enqueued: 0x55d4bfb6ebe0
    :4:command.cpp              :179 : 102993890808 us: 17154: [tid:0x7f0824e798c0] Command 0x55d4bfbfe270 complete
    :4:command.cpp              :173 : 102993890809 us: 17154: [tid:0x7f0824e798c0] Command 0x55d4bfb6ebe0 complete (Wall: 102993890808, CPU: 0, GPU: 0 us)
    :4:command.cpp              :253 : 102993890810 us: 17154: [tid:0x7f0824e798c0] Waiting for event 0x55d4bfbfe270 to complete, current status 0
    :4:command.cpp              :268 : 102993890811 us: 17154: [tid:0x7f0824e798c0] Event 0x55d4bfbfe270 wait completed
    :3:hip_memory.cpp           :583 : 102993890811 us: 17154: [tid:0x7f0824e798c0] hipMemcpy: Returned hipSuccess : : duration: 331 us
    :3:hip_platform.cpp         :194 : 102993890921 us: 17154: [tid:0x7f0824e798c0]  __hipPushCallConfiguration ( , , 0, stream:<null> )
    :3:hip_platform.cpp         :198 : 102993890925 us: 17154: [tid:0x7f0824e798c0] __hipPushCallConfiguration: Returned hipSuccess :
    :3:hip_platform.cpp         :203 : 102993890979 us: 17154: [tid:0x7f0824e798c0]  __hipPopCallConfiguration ( , , 0x7ffd49f8a080, 0x7ffd49f8a078 )
    :3:hip_platform.cpp         :212 : 102993890982 us: 17154: [tid:0x7f0824e798c0] __hipPopCallConfiguration: Returned hipSuccess :
    :3:hip_module.cpp           :469 : 102993890989 us: 17154: [tid:0x7f0824e798c0]  hipLaunchKernel ( 0x55d4be7d6d90, , , 0x7ffd49f8a0c0, 0, stream:<null> )
    :3:devprogram.cpp           :2676: 102993891048 us: 17154: [tid:0x7f0824e798c0] Using Code Object V4.
    :3:devprogram.cpp           :2979: 102993891243 us: 17154: [tid:0x7f0824e798c0] For Init/Fini: Kernel Name: _Z8vadd_hipPKfS0_Pfi
    :4:command.cpp              :349 : 102993891248 us: 17154: [tid:0x7f0824e798c0] Command (KernelExecution) enqueued: 0x55d4bfb63a80
    :3:rocvirtual.cpp           :703 : 102993891251 us: 17154: [tid:0x7f0824e798c0] Arg0:   = ptr:0x7f0722800000 obj:[0x7f0722800000-0x7f0722bd0900]
    :3:rocvirtual.cpp           :703 : 102993891252 us: 17154: [tid:0x7f0824e798c0] Arg1:   = ptr:0x7f0722200000 obj:[0x7f0722200000-0x7f07225d0900]
    :3:rocvirtual.cpp           :703 : 102993891254 us: 17154: [tid:0x7f0824e798c0] Arg2:   = ptr:0x7f0721c00000 obj:[0x7f0721c00000-0x7f0721fd0900]
    :3:rocvirtual.cpp           :778 : 102993891256 us: 17154: [tid:0x7f0824e798c0] Arg3:   = val:1000000
    :3:rocvirtual.cpp           :2774: 102993891257 us: 17154: [tid:0x7f0824e798c0] ShaderName : _Z8vadd_hipPKfS0_Pfi
    :4:rocvirtual.cpp           :862 : 102993891263 us: 17154: [tid:0x7f0824e798c0] HWq=0x7f0835fa2000, Dispatch Header = 0x1502 (type=2, barrier=1, acquire=2, release=2), setup=3, grid=[1000192, 1, 1], workgroup=[256, 1, 1], private_seg_size=0, group_seg_size=0, kernel_obj=0x7f0823adc680, kernarg_address=0x7f0720a00000, completion_signal=0x0
    :3:hip_module.cpp           :470 : 102993891266 us: 17154: [tid:0x7f0824e798c0] hipLaunchKernel: Returned hipSuccess :
    :3:hip_memory.cpp           :582 : 102993891269 us: 17154: [tid:0x7f0824e798c0]  hipMemcpy ( 0x7f08242fe010, 0x7f0721c00000, 4000000, hipMemcpyDeviceToHost )
    :4:command.cpp              :349 : 102993891272 us: 17154: [tid:0x7f0824e798c0] Command (CopyDeviceToHost) enqueued: 0x55d4bfbfe270
    :4:rocmemory.cpp            :944 : 102993891886 us: 17154: [tid:0x7f0824e798c0] Locking to pool 0x55d4bf5be150, size 0x3d1000, HostPtr = 0x7f08242fe000, DevPtr = 0x7f071ae00000
    :4:rocvirtual.cpp           :1005: 102993891890 us: 17154: [tid:0x7f0824e798c0] HWq=0x7f0835fa2000, BarrierAND Header = 0x1503 (type=3, barrier=1, acquire=2, release=2), dep_signal=[0x0, 0x0, 0x0, 0x0, 0x0], completion_signal=0x7f0835fc4700
    :4:rocblit.cpp              :664 : 102993891892 us: 17154: [tid:0x7f0824e798c0] HSA Asycn Copy dst=0x7f071ae00010, src=0x7f0721c00000, size=905725696, wait_event=0x7f0835fc4680, completion_signal=0x7ffd49f89b00
    :4:rocvirtual.cpp           :550 : 102993892102 us: 17154: [tid:0x7f0824e798c0] Host wait on completion_signal=0x7f0835fc4680
    :3:rocvirtual.hpp           :61  : 102993892104 us: 17154: [tid:0x7f0824e798c0] Host active wait for Signal = (0x7f0835fc4680) for -1 ns
    :4:command.cpp              :289 : 102993892293 us: 17154: [tid:0x7f0824e798c0] Queue marker to command queue: 0x55d4bf5b8720
    :4:command.cpp              :349 : 102993892295 us: 17154: [tid:0x7f0824e798c0] Command (InternalMarker) enqueued: 0x55d4bfb6ebe0
    :4:command.cpp              :179 : 102993892296 us: 17154: [tid:0x7f0824e798c0] Command 0x55d4bfb63a80 complete
    :4:command.cpp              :179 : 102993892297 us: 17154: [tid:0x7f0824e798c0] Command 0x55d4bfbfe270 complete
    :4:command.cpp              :173 : 102993892299 us: 17154: [tid:0x7f0824e798c0] Command 0x55d4bfb6ebe0 complete (Wall: 102993892298, CPU: 0, GPU: 0 us)
    :4:command.cpp              :253 : 102993892300 us: 17154: [tid:0x7f0824e798c0] Waiting for event 0x55d4bfbfe270 to complete, current status 0
    :4:command.cpp              :268 : 102993892302 us: 17154: [tid:0x7f0824e798c0] Event 0x55d4bfbfe270 wait completed
    :3:hip_memory.cpp           :583 : 102993892303 us: 17154: [tid:0x7f0824e798c0] hipMemcpy: Returned hipSuccess : : duration: 1034 us
    PASSED!
    :3:devprogram.cpp           :2979: 102993892796 us: 17154: [tid:0x7f0824e798c0] For Init/Fini: Kernel Name: _Z8vadd_hipPKfS0_Pfi

In case of a program that have a HIP kernel crash with error like \"Page not present\", this can give a first idea about what is going on.

** Tip**\
As kernels are C++ functions, it is possible to demangle them running `c++filt` and passing the mangled name as an argument=\> `c++filt _Z8vadd_hipPKfS0_Pfi` which gives the result `vadd_hip(float const*, float const*, float*, int)`.

## [More advanced topics]

## [References]

1.  [[[↑](#cite_ref-1)] [[Logging HIP activity](https://github.com/ROCm/HIP/blob/d592b826ba18e9201e910017409f7b0f0913976a/docs/how-to/logging.rst)]]
2.  [[[↑](#cite_ref-2)] [[HIP environment variable summary](https://github.com/ROCm/HIP/blob/d592b826ba18e9201e910017409f7b0f0913976a/docs/how-to/debugging.rst#hip-environment-variable-summary)]]