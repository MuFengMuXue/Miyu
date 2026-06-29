# General-purpose computing on graphics processing units

General-purpose computing on graphics processing units (GPGPU) API definitions include the vendor-independent OpenCL, SYCL, HIP, OpenMP, and Vulkan compute shader; and Nvidia's CUDA. Each API can have multiple implementations on multiple types of hardware or software: GPUs, CPUs, NPUs, FPGAs, or just a different GPGPU API (shim/transpiler).

## OpenCL
OpenCL (Open Computing Language) is an open, royalty-free parallel programming specification developed by the Khronos Group, a non-profit consortium.

The OpenCL specifications describe a C-based programming language, a general environment that is required to be present, and a C API to enable programmers to call into this environment. There are also bindings that let other languages to call into this environment as well as alternative languages for writing the OpenCL computation kernel.

An OpenCL environment includes at least one of the following:

* A copy of the libOpenCL.so, the ICD loader presenting a full OpenCL API interface.
* Platform-dependent drivers that are loaded by the ICD loader.

## ICD loader (libOpenCL.so)
It is very common for a system to have multiple OpenCL-capable hardware and hence multiple OpenCL runtime implementations. A component called the "OpenCL ICD loader" is supposed to be a platform-agnostic library that provides the means to load device-specific drivers through the OpenCL API.
Most OpenCL vendors provide their own implementation of an OpenCL ICD loader, and these should all work with the other vendors' OpenCL implementations. Unfortunately, most vendors do not provide completely up-to-date ICD loaders, and therefore Arch Linux has decided to provide this library from a separate project () which provides a functioning implementation of the current OpenCL API. As of 2025, the current OpenCL version is 3.0.

The other ICD loader libraries are installed as part of each vendor's SDK. If you want to ensure the ICD loader from the  package is used, you can create a file in  which adds  to the dynamic program loader's search directories:

This is necessary because all the SDKs add their runtime's lib directories to the search path through  files.

The available packages containing various OpenCL ICDs are:

* : recommended, most up-to-date
*  by Intel. Provides OpenCL 2.0, deprecated in favour of .

## Managing implementations
To see which OpenCL implementations are currently active on your system, use the following command:

 $ ls /etc/OpenCL/vendors

To find out all possible (known) properties of the OpenCL platform and devices available on the system, install .

You can specify which implementations should your application see using . For example:

 $ ocl-icd-choose amdocl64.icd:mesa.icd davinci-resolve-checker

 is a simple wrapper script that sets the  environment variable. It would not be needed if  could handle single icd files like the manual suggests; this is a known bug being tracked as OCL-dev/ocl-icd#7.

## Runtime
To execute programs that use OpenCL, a runtime that can be loaded by libOpenCL.so needs to be installed.

## OpenCL on generic GPU
For any GPU supported by Mesa, you can use rusticl by installing . It can be enabled by using the environment variable , where  is a Gallium driver, such as  or . It works on the broadest set of hardware but does not necessarily provide the best performance. If you have trouble setting up other drivers, try using it: it takes a very small amount of configuration to enable.

## OpenCL on AMD/ATI GPU
* : Part of AMD's ROCm GPU compute stack, officially supporting a small range of GPU models (other cards may work with unofficial or partial support). To support cards older than Vega, you need to set the runtime variable . This is similar, but not quite equivalent to specifying  in ubuntu's amdgpu-install, because this package's rocm version differs from ubuntu's installer version.
* : Legacy Orca OpenCL repackaged from AMD's ubuntu releases. Equivalent to specifying  in ubuntu's amdgpu-install.
* , : ROCm components repackaged from AMD's Ubuntu releases. Equivalent to specifying  in ubuntu's amdgpu-install.

## OpenCL image support
The latest ROCm versions now includes OpenCL Image Support used by GPGPU accelerated software such as Darktable. ROCm with the AMDGPU open source graphics driver are all that is required. AMDGPU PRO is not required.

## OpenCL on NVIDIA GPU
* : official NVIDIA runtime

## OpenCL on Intel GPU
* : a.k.a. the "NEO" runtime, the open-source OpenCL (and oneAPI Level Zero) implementation for Intel Gen12 (Rocket/Tiger Lake) Integrated Graphics and above (includes all discrete Intel GPUs).
* : same as above (with partial oneAPI Level Zero support), only for Intel Gen8 (Broadwell), Gen9 (Skylake and variants), and Gen11 (Ice/Elkhart Lake) Graphics. The OpenCL ICD provided for legacy platforms has the suffix "legacy1".
* : the open-source OpenCL implementation for Intel Gen7 (Ivy Bridge) Graphics and above, deprecated by Intel in favour of the NEO OpenCL runtime, remains recommended solution for legacy hardware platforms (e.g. Ivy Bridge, Haswell).
* : the proprietary OpenCL implementation for Intel Gen7 (Ivy Bridge) Graphics and above, deprecated by Intel in favour of the NEO OpenCL runtime, remains recommended solution for legacy hardware platforms (e.g. Ivy Bridge, Haswell).

## OpenCL on CPU
The following allow OpenCL to be run on a CPU:

* : Intel's LLVM and oneAPI-based implementation for x86_64 processors. Officially intended for Intel Core and Xeon processors, it actually works on all x86_64 processors with SSE4.1. Even on AMD Zen processors it outperforms pocl.
* : LLVM-based OpenCL implementation, works for all CPU architectures supported by LLVM and some GPUs (Nvidia through libCUDA, Intel through Level Zero) as well as OpenASIP. Despite this broad coverage, its performance leaves a lot to be desired.
* : AMD CPU runtime, abandoned

## OpenCL on Vulkan
The following allow OpenCL to be run on top of a Vulkan runtime:

* : Clspv is a prototype compiler for a subset of OpenCL C to Vulkan compute shaders.
* : clvk is a prototype implementation of OpenCL 3.0 on top of Vulkan using clspv as the compiler.

## OpenCL on FPGA
* pocl for OpenASIP, see above.
* : Xilinx Run Time for FPGA xrt
* fpga-runtime-for-opencl: Intel FPGA Runtime

## 32-bit runtime
To execute 32-bit programs that use OpenCL, a compatible hardware 32-bit runtime needs to be installed.

## OpenCL on generic GPU (32-bit)
* : OpenCL support for Mesa drivers (32-bit)

## OpenCL on NVIDIA GPU (32-bit)
* : OpenCL implemention for NVIDIA (32-bit)

## Development
For OpenCL development, the bare minimum additional packages required, are:

* : OpenCL ICD loader implementation, up to date with the latest OpenCL specification.
* : OpenCL C/C++ API headers.

The vendors' SDKs provide a multitude of tools and support libraries:

* : Intel OpenCL SDK (old version, new OpenCL SDKs are included in the INDE and Intel Media Server Studio)
* : This package is installed as  and apart from SDK files it also contains a number of code samples (). It also provides the  utility which lists OpenCL platforms and devices present in the system and displays detailed information about them. As the SDK itself contains a CPU OpenCL driver, no extra driver is needed to execute OpenCL on CPU devices (regardless of its vendor).
* : Develop OpenCL-based applications for AMD platforms.
* : Nvidia's GPU SDK which includes support for OpenCL 3.0.

## Language bindings
These bindings allow other languages to call into the OpenCL environment. They generally do not alter the requirement to write the kernel in OpenCL C.

* JavaScript/HTML5: WebCL
* Python:
* D: cl4d or DCompute
* Java: Aparapi or JOCL (a part of JogAmp)
* Mono/.NET: Open Toolkit
* Go: OpenCL bindings for Go
* Racket: Racket has a native interface on PLaneT that can be installed via raco.
* Rust: ocl
* Julia: OpenCL.jl

## SYCL
According to Wikipedia:SYCL:

SYCL is a higher-level programming model to improve programming productivity on various hardware accelerators. It is a single-source embedded domain-specific language (eDSL) based on pure C++17.

SYCL is inspired by OpenCL that enables code for heterogeneous processors to be written in a “single-source” style using completely standard C++. SYCL enables single-source development where C++ template functions can contain both host and device code to construct complex algorithms that use hardware accelerators, and then re-use them throughout their source code on different types of data.

While the SYCL standard started as the higher-level programming model sub-group of the OpenCL working group and was originally developed for use with OpenCL and SPIR, SYCL is a Khronos Group workgroup independent from the OpenCL working group [... starting with SYCL 2020, SYCL has been generalized as a more general heterogeneous framework able to target other systems. This is now possible with the concept of a generic backend to target any acceleration API while enabling full interoperability with the target API, like using existing native libraries to reach the maximum performance along with simplifying the programming effort. For example, the OpenSYCL implementation targets ROCm and CUDA via AMD's cross-vendor HIP.

In other words, the SYCL defines a programming environment based on C++17. This environment is intended to be combined with compilers that produce code for both CPUs and GPGPUs. The language intended for the GPGPU side used to be SPIR, but compilers that target other intermediate representations also exist.

## Implementations
* : Open source implementation mainly driven by Xilinx.
* : Compiler for multiple programming models (SYCL, C++ standard parallelism, HIP/CUDA) for CPUs and GPUs from all vendors.
* : Intel's Data Parallel C++: the LLVM/oneAPI Implementation of SYCL.
*  Codeplay's proprietary implementation of SYCL 1.2.1. Can target SPIR, SPIR-V and experimentally PTX (NVIDIA) as device targets (ends of support on 1st september 2023, will get merged into intel llvm implementation Source).

## oneAPI
oneAPI is a marketing name used by many of Intel's high-performance computing libraries. The package  provides  that can be used to set up the environment for compilation and linking of SYCL programs. Some parts of the components like the compiler are open-sourced by Intel on GitHub while others are not.

Some packages can be installed for additional functionality. For example,  enables GPU offloading of the Math Kernel Library (MKL) to be supported.

## Checking for SPIR support
SYCL was originally intended to be compiled to SPIR or SPIR-V. Both are intermediate languages designed by Khronos that can be consumed by an OpenCL driver. SPIR is included as a OpenCL 1.0 or 2.0 extension while SPIR-V is included in OpenCL core from version 2.1 onwards (). To check whether SPIR or SPIR-V are supported  can be used:

ComputeCpp additionally ships with a tool that summarizes the relevant system information:

Drivers known to at least partially support SPIR or SPIR-V include , , and .

## Other uses of SPIR/SPIR-V
SPIR-V covers not only compute kernels, but also graphics shaders. It is able to serve as a shader intermediate language for OpenGL and Vulkan as well as a compute intermediate language for OpenCL, Vulkan, and SYCL. It can also be decompiled as a way to convert a kernel or shader from one language to another.

The C++ for OpenCL language (not to be confused with the short-lived "OpenCL C++") combines C++17 with OpenCL C. A handful of OpenCL drivers support loading it directly with  like one would do with OpenCL C, but the main expected usage is through  converting it to SPIR-V first. It can be an option for programmers who want to use C++17 in writing OpenCL kernels but do not want to embrace the whole model of SYCL.

## Development
SYCL requires a working C++11 environment to be set up.

There are a few open source libraries available for making use of the parallel capabilities in SYCL from its C++17 language:

* ComputeCpp SDK: Collection of code examples,  integration for ComputeCpp
* SYCL-DNN: Neural network performance primitives
* SYCL-BLAS: Linear algebra performance primitives
* VisionCpp: Computer Vision library
* SYCL Parallel STL: GPU implementation of the C++17 parallel algorithms

## CUDA
CUDA (Compute Unified Device Architecture) is NVIDIA's proprietary, closed-source parallel computing architecture and framework. It requires an NVIDIA GPU, and consists of several components:

* Required:
** NVIDIA kernel module
** CUDA "driver" and "runtime" libraries
* Optional:
** Additional libraries: CUBLAS, CUFFT, CUSPARSE, etc.
** CUDA toolkit, including the  compiler
** CUDA SDK, which contains many code samples and examples of CUDA and OpenCL programs

The kernel module and CUDA "driver" library are shipped in  and . The "runtime" library and the rest of the CUDA toolkit are available in .  needs  to be installed, see .

## Development
The  package installs all components in the directory . The script in  sets the relevant environment variables so all build systems that support CUDA can find it.

To find whether the installation was successful and whether CUDA is up and running, you can compile the CUDA samples. One way to check the installation is to run the  sample.

## Language bindings
* Fortran: PGI CUDA Fortran Compiler
* Haskell: The accelerate package lists available CUDA backends
* Java: JCuda
* Mathematica: CUDAlink
* Mono/.NET: CUDAfy.NET, managedCuda
* Perl: KappaCUDA, CUDA-Minimal
* Python:
* Ruby: rbcuda
* Rust: Rust-CUDA. Unmaintained: cuda-sys (bindings), RustaCUDA (high-level wrapper).

## ROCm
ROCm ROCm (Radeon Open Compute Platform) is AMD's answer to CUDA. It includes many pieces of software from driver (AMDGPU) to compiler and runtime library, much like CUDA. Some parts are specific to select AMD GPUs, other parts completely hardware-agnostic. See the ROCm for Arch Linux repository for more information.

ROCm includes a singular software stack for implementing compute capabilities on the AMDGPU driver. On top of this stack, it implements HIP, OpenMP, and OpenCL. It also includes some parts built on top of HIP as well as an implementation of HIP using NVIDIA's CUDA stack.

## ROCm-enabled models
ROCm should support AMD GPUs from the Polaris architecture (RX 500 series) and above. The official list of GPU models is very short, consisting of mostly profession models. However, consumer GPUs and APUs of the equivalent generations are known to work. Other generations may work with unofficial or partial support. To support Polaris, you need to set the runtime variable .

It takes some time for newer AMD GPU architectures to be added to ROCm; see Wikipedia:ROCm#Consumer-grade GPUs for an up-to-date support matrix. Also see #OpenCL on AMD/ATI GPU from before.

## HIP
The Heterogeneous Interface for Portability (HIP) is AMD's dedicated GPU programming environment for designing high performance kernels on GPU hardware. HIP is a C++ runtime API and programming language that allows developers to create portable applications on different platforms.

HIP's specification is managed in the rocm-systems repository, but HIP itself is  hardware-agnostic.

HIP runtime library packages:

* : The high-level runtime library, analogous to the OpenCL ICD loader.
* : Implementation of HIP for AMD GPUs.
* : The Heterogeneous Interface for NVIDIA GPUs in ROCm. This is really just a bunch of header files for the CUDA C++ compiler mostly consisting of  renames.

The  package includes the HIP SDK. All components are installed in the directory . The script that sets the relevant environment variables is provided in . Some software might also check for , which can be manually set to the same value as .

 is the HIP backend for AMD's open source deep learning library.

## ROCm troubleshooting
First check if your GPU shows up in . If it does not, it might mean that ROCm does not support your GPU or it is built without support for your GPU.

Also check the ROCm HIP environment variables for debugging, GPU isolation, etc.

## OpenMP and OpenACC
OpenMP is better-known for its use in CPU multiprocessing, but it also supports some offloading for moving some work to GPGPUs. OpenACC is in a similar position: both are based on inserting pragmas into ordinary C/C++/Fortran code and having the compiler split out the marked part for offloading or multiprocessing.

* AMD provides an implementation of OpenMP for ROCm-capable AMD GPUs. The  package provides AOMP - an open source Clang/LLVM based compiler with added support for the OpenMP API on AMD GPUs.
* Nvidia's  provides OpenMP implementation with GPU offloading on their GPUs. * GCC can generate Nvidia (nvptx) and AMD (gfx9, gfx10, gfx11) code for offloading OpenMP and OpenACC [https://gcc.gnu.org/wiki/Offloading.
* Clang/LLVM can generate Nvidia (nvptx) and AMD (amdgpu) code for offloading OpenMP and OpenACC [https://clang.llvm.org/docs/ClangOffloadBundler.html.

## List of GPGPU accelerated software
* Bitcoin
* Blender – CUDA support for Nvidia GPUs and HIP support for AMD GPUs. More information in * BOINC – some projects provide OpenCL and/or CUDA programs
*  – a GPU memtest. Despite its name, is supports both CUDA and OpenCL.
*  – OpenCL feature requires at least 1 GB RAM on GPU and Image support (check output of clinfo command).
* DaVinci Resolve - a non-linear video editor. Can use both OpenCL and CUDA.
* FFmpeg – more information in [https://trac.ffmpeg.org/wiki/HWAccelIntro#OpenCL.
** HandBrake
* Folding@home – uses OpenCL and CUDA versions of the molecular simulation software GROMACS
* GIMP – experimental – more information in * Hashcat
*
* LibreOffice Calc – more information in [https://help.libreoffice.org/Calc/OpenCL_Options.
* mpv - See mpv#Hardware video acceleration.
*  - Used for searching the neural network (supports tensorflow, OpenCL, CUDA, and openblas)
* opencl-benchmark - simple FP64/FP32/FP16/INT64/INT32/INT16/INT8 and memory/PCIe bandwidth benchmarking tool for OpenCL
*
* Ollama - LLM inference software
* llama.cpp - LLM inference in C/C++
*
* ,
* ,
*  - High Perf CryptoNote CPU and GPU (OpenCL, CUDA) miner

## PyTorch on ROCm
To use PyTorch with ROCm install .

ROCm pretends to be CUDA so this should return . If it does not, either it is not compiled with your GPU support or you might have conflicting dependencies. You can verify those by looking at  - there should not be any missing  files nor multiple versions of same .
