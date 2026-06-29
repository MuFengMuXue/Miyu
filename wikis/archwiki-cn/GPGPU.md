**翻译状态：**

  * 本文（或部分内容）译自 [GPGPU](<https://wiki.archlinux.org/title/GPGPU> "arch:GPGPU")，最近一次同步于 2026-02-23，若英文版本有所[更改](<https://wiki.archlinux.org/title/GPGPU?diff=0&oldid=862103>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/GPGPU_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-preferences-desktop-locale-modified.png)](<../File:Tango-preferences-desktop-locale-modified.png>)**这篇文章或章节的[翻译](<../Project:%E8%B4%A1%E7%8C%AE.html#Translating> "Project:Contributing")质量不佳。**

**原因：** 文章正在进行大规模更新，需要分阶段对其进行调整。（在 [Talk:GPGPU#](<../zh-cn/Talk:GPGPU.html>) 中讨论）

相关文章

  * [NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA")
  * [硬件视频加速](<../zh-cn/%E7%A1%AC%E4%BB%B6%E8%A7%86%E9%A2%91%E5%8A%A0%E9%80%9F.html> "硬件视频加速")

[通用图形处理单元计算](<https://en.wikipedia.org/wiki/GPGPU> "w:GPGPU")（GPGPU）API定义包括厂商无关的OpenCL、SYCL、HIP、OpenMP和Vulkan计算着色器;以及Nvidia的CUDA。每个API可以有多种硬件或软件的实现：GPU、CPU、NPU、FPGA，或者仅仅是不同的GPGPU API（shim/transpiler）。 

## OpenCL

[OpenCL](<https://en.wikipedia.org/wiki/OpenCL> "w:OpenCL")（开放计算语言）是由非营利联盟Khronos Group开发的一种开放、免版税的并行编程规范。 

OpenCL 规范描述了一种基于 C 的编程语言、一个必须存在的通用环境，以及一个 C API，使程序员能够调用该环境。还有绑定允许其他语言调用该环境，以及编写 OpenCL 计算内核的替代语言。 

**提示：** clinfo 工具可用于列出 OpenCL 平台、设备及 ICD 加载器属性。

OpenCL 环境至少包含以下一种： 

  * _libOpenCL.so_ 的副本，ICD加载器呈现完整的OpenCL API接口。
  * 由ICD加载器加载的平台相关驱动程序。

###  ICD加载器（libOpenCL.so）

系统通常拥有多个支持 OpenCL 的硬件，因此存在多个 OpenCL 运行时实现。一个名为“OpenCL ICD loader”的组件应是一个平台无关的库，通过 OpenCL API 提供加载设备特定驱动程序的手段。 大多数 OpenCL 厂商都提供自己的 OpenCL ICD 加载器实现，这些都能与其他厂商的 OpenCL 实现兼容。遗憾的是，大多数厂商并未提供完全最新的ICD加载器，因此Arch Linux决定从一个独立项目[ocl-icd](<https://archlinux.org/packages/?name=ocl-icd>)包中提供该库，该项目提供了当前OpenCL API的可运行实现。截至2025年，当前的OpenCL版本为3.0。 

其他ICD加载器库则作为各厂商SDK的一部分安装。如果你想确保使用 [ocl-icd](<https://archlinux.org/packages/?name=ocl-icd>)包 中的 ICD 加载器，可以在 `/etc/ld.so.conf.d` 创建一个文件，为动态程序加载器的搜索目录添加`/usr/lib`： 
    
    /etc/ld.so.conf.d/00-usrlib.conf
    
    /usr/lib

这是必要的，因为所有SDK都会把运行时的库目录添加到`ld.so.conf.d`文件的搜索路径中。 

包含各种 OpenCL ICD 的可用软件包有： 

  * [ocl-icd](<https://archlinux.org/packages/?name=ocl-icd>)包：推荐，最新
  * [intel-compute-runtime](<https://archlinux.org/packages/?name=intel-compute-runtime>)包：Intel提供的OpenCL实现。

**注意：** ICD 加载器的供应商在功能上无关紧要：它们应当与厂商无关，只要实现正确，就可以互换使用。供应商的作用仅用于区分它们之间的区别。

###  管理实现

要查看当前系统中哪些OpenCL实现正在运行，请使用以下命令： 

ls /etc/OpenCL/vendors 

要了解 OpenCL 平台及系统上可用设备的所有可能（已知）属性，请安装 [clinfo](<https://archlinux.org/packages/?name=clinfo>)包。 

你可以用ocl-icd-choose指定应用应接收哪些实现。例如： 

ocl-icd-choose amdocl64.icd:mesa.icd davinci-resolve-checker 

`ocl-icd-choose` 是一个简单的包装脚本，用于设置`OCL_ICD_FILENAMES`环境变量。如果`OCL_ICD_VENDORS`能像说明书建议的那样处理单个ICD文件，那就不需要它了;这是一个已知的bug，被追踪为[OCL-dev/ocl-icd#7](<https://github.com/OCL-dev/ocl-icd/issues/7#issuecomment-1522941979>)。 

###  运行时

要**执行** 使用 OpenCL 的程序，需要安装一个可由 _libOpenCL.so_ 加载的运行时。 

####  通用GPU上的OpenCL

对于[Mesa](<../zh-cn/OpenGL.html> "OpenGL")支持 _的任何_ 显卡，你可以通过安装[opencl-mesa](<https://archlinux.org/packages/?name=opencl-mesa>)包来使用rusticl。可以通过使用[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量") `RUSTICL_ENABLE=_driver_` 来启用，其中 `_driver_` 是 Gallium 驱动程序，如 `radeonsi` 或 `iris`。它能在最广泛的硬件上运行，但不一定能提供最佳性能。如果你在设置其他驱动时遇到困难，可以试试用它：启用只需要非常少的配置。 

####  OpenCL 在 AMD/ATI GPU 上

  * [rocm-opencl-runtime](<https://archlinux.org/packages/?name=rocm-opencl-runtime>)包：AMD ROCm GPU 计算栈的一部分，官方支持少量 GPU 型号（其他显卡可能支持非官方或部分支持）。要支持比Vega更早的显卡，你需要设置运行时变量`ROC_ENABLE_PRE_VEGA=1`。这与在 Ubuntu 的 amdgpu-install 中指定 `opencl=rocr` 类似，但不完全等同，因为该包的 ROCM 版本与 Ubuntu 安装程序版本不同。
  * [opencl-legacy-amdgpu-pro](<https://aur.archlinux.org/packages/opencl-legacy-amdgpu-pro/>)AUR：从AMD Ubuntu版本重新包装的Legacy Orca OpenCL。相当于在 Ubuntu 的 amdgpu-install 中指定 `opencl=legacy`。
  * [opencl-amd](<https://aur.archlinux.org/packages/opencl-amd/>)AUR、[opencl-amd-dev](<https://aur.archlinux.org/packages/opencl-amd-dev/>)AUR：ROCm组件从AMD的Ubuntu版本重新打包而来。相当于在 Ubuntu 的 amdgpu-install 中指定 `opencl=rocr,legacy`。

#####  OpenCL 图像支持

最新的ROCm版本现已包含用于GPGPU加速软件如Darktable的OpenCL图像支持。配备AMDGPU开源图形驱动的ROCm仅需完成。AMDGPU PRO不是必需的。 
    
    /opt/rocm/bin/clinfo | grep -i "image support"
    
    Image support     Yes

#### NVIDIA

  * [opencl-nvidia](<https://archlinux.org/packages/?name=opencl-nvidia>)包：官方[NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA")运行库

#### Intel

  * [intel-compute-runtime](<https://archlinux.org/packages/?name=intel-compute-runtime>)包：也被称为Neo OpenCL运行库，开源实现，支持Intel HD Graphics GPU第八代(Broadwell)及更新的硬件。
  * [opencl-clover-mesa](<https://archlinux.org/packages/?name=opencl-clover-mesa>)包或[opencl-rusticl-mesa](<https://archlinux.org/packages/?name=opencl-rusticl-mesa>)包：mesa驱动通过clover/rusticl提供的OpenCL支持
  * [beignet](<https://aur.archlinux.org/packages/beignet/>)AUR：Intel HD Graphics GPU第七代(Ivy Bridge)及更新硬件的开源支持，因被NEO OpenCL替代而被弃用，依然是传统硬件平台的推荐解决方案（如Ivy Bridge，Haswell）
  * [intel-opencl](<https://aur.archlinux.org/packages/intel-opencl/>)AUR：Intel HD Graphics GPU第七代(Ivy Bridge)及更新硬件的闭源支持，因被NEO OpenCL替代而被弃用，依然是传统硬件平台的推荐解决方案（如Ivy Bridge，Haswell）
  * [intel-opencl-runtime](<https://aur.archlinux.org/packages/intel-opencl-runtime/>)AUR：Intel酷睿及志强处理器的实现，同样支持非Intel CPU

#### Others

  * [pocl](<https://archlinux.org/packages/?name=pocl>)包：基于LLVM的OpenCL实现（与硬件无关）

还有一些编译器和翻译器能够让OpenCL应用在Vulkan上运行。 

  * [clspv-git](<https://aur.archlinux.org/packages/clspv-git/>)AUR：Clspv是一个OpenCL子集到Vulkan计算着色器的原型编译器
  * [clvk-git](<https://aur.archlinux.org/packages/clvk-git/>)AUR：clvk是一个在Vulkan上的OpenCL 3.0原型实现，使用clspy作为编译器
  * [xrt-bin](<https://aur.archlinux.org/packages/xrt-bin/>)AUR：Xilinx FPGA [xrt](<https://github.com/Xilinx/XRT>)运行库
  * [fpga-runtime-for-opencl](<https://github.com/intel/fpga-runtime-for-opencl>):FPGA运行库

###  32位运行库

要**运行** 使用OpenCL的32位程序，需要安装一个兼容硬件的32位运行库。 

**提示：**[clinfo](<https://archlinux.org/packages/?name=clinfo>)包工具只能显示64位OpenCL平台，设备和ICD加载器属性。要用于32位，你需要编译32位clinfo或使用archlinux32项目中的 [clinfo](<https://www.archlinux32.org/packages/i686/extra/clinfo/>)。

####  AMD/ATI

  * [lib32-opencl-clover-mesa](<https://archlinux.org/packages/?name=lib32-opencl-clover-mesa>)包 或 [lib32-opencl-rusticl-mesa](<https://archlinux.org/packages/?name=lib32-opencl-rusticl-mesa>)包：AMD/ATI Radeon mesa 32位驱动的OpenCL支持

#### NVIDIA

  * [lib32-opencl-nvidia](<https://archlinux.org/packages/?name=lib32-opencl-nvidia>)包：NVIDIA（32位）的OpenCL实现

###  ICD加载器 (libOpenCL.so)

OpenCL ICD加载器应该是一个平台无关的库，提供了通过OpenCL API加载设备相关驱动的方法。 大多数OpenCL供应商提供了自己的OpenCL ICD加载器实现，这些加载器也应该全部与其它供应商的实现兼容。但不幸的是，大多供应商没有提供完全最新的ICD加载器，因此Arch Linux决定提供一个来自独立项目的加载器库([ocl-icd](<https://archlinux.org/packages/?name=ocl-icd>)包)，该库目前提供了当前OpenCL API的实现。 

其它ICD加载器库文件安装在各个供应商的SDK中。如果你想确保使用[ocl-icd](<https://archlinux.org/packages/?name=ocl-icd>)包的ICD加载器，你可以在`/etc/ld.so.conf.d` 创建配置文件，添加`/usr/lib`到动态程序加载器的搜索目录中： 
    
    /etc/ld.so.conf.d/00-usrlib.conf
    
    /usr/lib
    
因为所有SKD通过`ld.so.conf.d`添加自己的运行库库目录到搜索路径。 

包含各种OpenCL ICD的包有： 

  * [ocl-icd](<https://archlinux.org/packages/?name=ocl-icd>)包：推荐，几乎是最新的
  * [intel-opencl](<https://aur.archlinux.org/packages/intel-opencl/>)AUR：由Intel提供的OpenCL 2.0，因被[intel-compute-runtime](<https://archlinux.org/packages/?name=intel-compute-runtime>)包替代而废弃

**注意：** 上文提及的ICD加载器的供应商仅用于区分各个供应商提供的加载器，除此之外没有任何关联。ICD加载器是与供应商无关的，也应该是可以相互替换的（只要这些加载器的实现是正确的）。

###  开发

要**开发** OpenCL，需要最小的额外包： 

  * [ocl-icd](<https://archlinux.org/packages/?name=ocl-icd>)包：OpenCL ICD加载器实现，符合最新OpenCL标准
  * [opencl-headers](<https://archlinux.org/packages/?name=opencl-headers>)包：OpenCL C/C++ API头文件

供应商提供了大量工具和支持库文件： 

  * [intel-opencl-sdk](<https://aur.archlinux.org/packages/intel-opencl-sdk/>)AUR：[Intel OpenCL SDK](<https://software.intel.com/en-us/articles/opencl-sdk/>)（旧版，新版OpenCL SDK包含在INDE 和Intel Media Server Studio中）
  * [amdapp-sdk](<https://aur.archlinux.org/packages/amdapp-sdk/>)AUR：安装在`/opt/AMDAPP`，除了SKD文件，还包含一一些代码示例（`/opt/AMDAPP/SDK/samples/`）。还提供了`clinfo`工具，用于显示系统中的OpenCL平台和设备及其详细信息。SDK还附带了OpenCL CPU驱动，无需其它驱动即可在CPU设备执行OpenCL（不论CPU的供应商）
  * [cuda](<https://archlinux.org/packages/?name=cuda>)包：Nvidia的GPU SDK包含了OpenCL 3.0的支持

###  实现

使用下列命令查看当前你的系统上的OpenCL实现： 
    
    $ ls /etc/OpenCL/vendors
    
要确认系统可用的OpenCL平台和设备上所有可能（已知）的特性，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")[clinfo](<https://archlinux.org/packages/?name=clinfo>)包。 

你可以指定你的程序使用特定实现，通过[ocl-icd-choose](<https://aur.archlinux.org/packages/ocl-icd-choose/>)AUR完成： 
    
    $ ocl-icd-choose amdocl64.icd:mesa.icd davinci-resolve-checker
    
#### Rusticl

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 可能不能为OCL_ICD_VENDORS指定单个icd文件，尽管手册这样说。参见 [https://github.com/OCL-dev/ocl-icd/issues/7#issuecomment-1522941979（在](<https://github.com/OCL-dev/ocl-icd/issues/7#issuecomment-1522941979%EF%BC%88%E5%9C%A8>) [Talk:GPGPU](<../zh-cn/Talk:GPGPU.html>) 中讨论）

[Rusticl](<https://docs.mesa3d.org/rusticl.html>)是[opencl-rusticl-mesa](<https://archlinux.org/packages/?name=opencl-rusticl-mesa>)包提供的一个由Rust编写的新的OpenCL实现。可以通过设置[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")`RUSTICL_ENABLE=_driver_`启用该实现，命令中的` _driver_`是Gallium驱动，如`iris`或`radeonsi`。 

另外，如果OpenCL应用无法检测到Rusticl，使用以下的环境变量： 
    
    OCL_ICD_VENDORS=/etc/OpenCL/vendors/rusticl.icd
    
####  语言绑定

  * **JavaScript/HTML5** : [WebCL](<https://www.khronos.org/webcl/>)
  * [Python](<../zh-cn/Python.html> "Python"): [python-pyopencl](<https://archlinux.org/packages/?name=python-pyopencl>)包
  * [D](</wzh/index.php?title=D&action=edit&redlink=1> "D（页面不存在）"): [cl4d](<https://github.com/Trass3r/cl4d>) or [DCompute](<https://github.com/libmir/dcompute>)
  * [Java](<../zh-cn/Java.html> "Java"): [Aparapi](<https://git.qoto.org/aparapi/aparapi>) or [JOCL](<https://jogamp.org/jocl/www/>) (a part of [JogAmp](<https://jogamp.org/>))
  * [Mono/.NET](<../zh-cn/Mono.html> "Mono"): [Open Toolkit](<https://sourceforge.net/projects/opentk/>)
  * [Go](<../zh-cn/Go.html> "Go"): [OpenCL bindings for Go](<https://github.com/samuel/go-opencl>)
  * **Racket** : Racket has a native interface [on PLaneT](<http://planet.racket-lang.org/display.ss?owner=jaymccarthy&package=opencl.plt>) that can be installed via raco.
  * [Rust](<../zh-cn/Rust.html> "Rust"): [ocl](<https://github.com/cogciprocate/ocl>)
  * [Julia](<../zh-cn/Julia.html> "Julia"): [OpenCL.jl](<https://github.com/JuliaGPU/OpenCL.jl>)

## SYCL

根据[Wikipedia:SYCL](<https://en.wikipedia.org/wiki/SYCL> "wikipedia:SYCL")： 

    SYCL 是一种用于在各种硬件加速器上提高编程生产力的高级编程语言模型。这是一种单源特定于域的嵌入式语言，基于C++17。

    SYCL 是一个免版税的跨平台抽象层，它建立在受 OpenCL 启发的底层概念、可移植性和效率之上，它使异构处理器的代码能够使用完全标准的C++以“单一来源”风格编写。SYCL 支持单源开发，其中C++模板函数可以包含主机和设备代码，以构建使用硬件加速器的复杂算法，然后在不同类型的数据上始终使用这些源代码。

    虽然 SYCL 标准最初是 OpenCL 工作组的高级编程模型子组，最初是为与 OpenCL 和 SPIR 一起使用而开发的，自2019年9月20日，SYCL从 OpenCL工作中独立，成为一个Khronos Group 工作组，从 SYCL 2020 开始，SYCL 已被推广为能够针对其他系统的更通用的异构架构。现在可以通过一个通用后端，针对任何加速 API，同时实现API 的完全互操作性，比如简化编程工作的同时，用已有的本地库来达到最大性能。例如，Open SYCL 通过 AMD 的 HIP 来利用 ROCm 和 CUDA。

###  实现

  * [computecpp](<https://aur.archlinux.org/packages/computecpp/>)AUR：Codeplay的私有SYCL 1.2.1实现。支持SPIR，SPIR-V和实验性支持PTX (NVIDIA)。（2023年9月1日结束支持，将并入intel llvm [Source](<https://codeplay.com/portal/news/2023/07/07/the-future-of-computecpp>)）。
  * [trisycl-git](<https://aur.archlinux.org/packages/trisycl-git/>)AUR：Xilinx的开源实现。
  * [hipsycl-cuda-git](<https://aur.archlinux.org/packages/hipsycl-cuda-git/>)AUR和[hipsycl-rocm-git](<https://aur.archlinux.org/packages/hipsycl-rocm-git/>)AUR：基于AMD HIP而不是OpenCL构建的开放实现，能够在AMD和NVIDIA GPU上运行。
  * [intel-oneapi-dpcpp-cpp](<https://archlinux.org/packages/?name=intel-oneapi-dpcpp-cpp>)包: Intel的数据并行C++：oneAPI的SYCL实现。

###  检查SPIR支持

大多数SYCL实现能够编译加速器代码到[SPIR](<https://en.wikipedia.org/wiki/Standard_Portable_Intermediate_Representation> "wikipedia:Standard Portable Intermediate Representation")或[SPIR-V](<https://en.wikipedia.org/wiki/Standard_Portable_Intermediate_Representation> "wikipedia:Standard Portable Intermediate Representation")。两者都是由Khronos设计的中间语言，并被OpenCL驱动使用。要检查是否支持SPIR或SPIR-V，使用[clinfo](<https://archlinux.org/packages/?name=clinfo>)包： 
    
    $ clinfo | grep -i spir
    
    Platform Extensions                             cl_khr_icd cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_byte_addressable_store cl_khr_depth_images cl_khr_3d_image_writes cl_intel_exec_by_local_thread cl_khr_spir cl_khr_fp64 cl_khr_image2d_from_buffer cl_intel_vec_len_hint 
      IL version                                    SPIR-V_1.0
      SPIR versions                                 1.2

ComputeCpp也提供了一个显示相关系统信息的工具： 
    
    $ computecpp_info
    
    Device 0:
    
      Device is supported                     : UNTESTED - Untested OS
      CL_DEVICE_NAME                          : Intel(R) Core(TM) i7-4770K CPU @ 3.50GHz
      CL_DEVICE_VENDOR                        : Intel(R) Corporation
      CL_DRIVER_VERSION                       : 18.1.0.0920
      CL_DEVICE_TYPE                          : CL_DEVICE_TYPE_CPU 
    
[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** Is the driver for AMD [opencl-legacy-amdgpu-pro](<https://aur.archlinux.org/packages/opencl-legacy-amdgpu-pro/>)AUR or [opencl-amd](<https://aur.archlinux.org/packages/opencl-amd/>)AUR? (在[Talk:GPGPU](<../zh-cn/Talk:GPGPU.html>)讨论)

已知至少部分支持SPIR或SPIR-V的驱动包括[intel-compute-runtime](<https://archlinux.org/packages/?name=intel-compute-runtime>)包，[intel-opencl-runtime](<https://aur.archlinux.org/packages/intel-opencl-runtime/>)AUR，[pocl](<https://archlinux.org/packages/?name=pocl>)包和[amdgpu-pro-opencl](<https://aur.archlinux.org/packages/amdgpu-pro-opencl/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]. 

###  开发

SYCL需要C++11环境，以下是一些开源库： 

  * [ComputeCpp SDK](<https://github.com/codeplaysoftware/computecpp-sdk/>)：包含示例代码，用于ComputeCpp的[cmake](<https://archlinux.org/packages/?name=cmake>)包集成
  * [SYCL-DNN](<https://github.com/codeplaysoftware/SYCL-DNN>)：神经网络性能基元
  * [SYCL-BLAS](<https://github.com/codeplaysoftware/SYCL-BLAS>)：线性代数性能基元
  * [VisionCpp](<https://github.com/codeplaysoftware/visioncpp>)：计算视觉库
  * [SYCL Parallel STL](<https://github.com/KhronosGroup/SyclParallelSTL>)：C++17并行算法的GPU实现

## CUDA

[CUDA](<https://en.wikipedia.org/wiki/CUDA> "wikipedia:CUDA")（Compute Unified Device Architecture，计算统一设备体系结构）是[NVIDIA](<../zh-cn/NVIDIA.html> "NVIDIA")的私有闭源并行计算架构。需要NVIDIA GPU，和一些组件： 

  * 必须： 
    * 私有NVIDIA内核模块
    * CUDA"驱动"和"运行时"库
  * 可选： 
    * 额外的库: CUBLAS，CUFFT，CUSPARSE等
    * CUDA工具包，包括`nvcc`编译器
    * CUDA SDK包含了许多示例代码，CUDA和OpenCL示例程序

内核模块和CUDA"驱动"库包含在[nvidia](<https://archlinux.org/packages/?name=nvidia>)包和[opencl-nvidia](<https://archlinux.org/packages/?name=opencl-nvidia>)包中。"运行时"库及其它CUDA工具包在[cuda](<https://archlinux.org/packages/?name=cuda>)包中。`cuda-gdb`需要安装[ncurses5-compat-libs](<https://aur.archlinux.org/packages/ncurses5-compat-libs/>)AUR，见[FS#46598](<https://bugs.archlinux.org/task/46598>)。 

###  开发

[cuda](<https://archlinux.org/packages/?name=cuda>)包中所有组件安装在`/opt/cuda`。在`/etc/profile.d/cuda.sh`里设置了相关环境变量，这样所有支持CUDA的构建系统都能找到CUDA。 

要确认CUDA是否安装成功，可以编译[CUDA示例代码](<https://github.com/nvidia/cuda-samples>)。一种检查安装的方法是运行`deviceQuery`示例。 One way to check the installation is to run the `deviceQuery` sample. 

###  语言绑定

  * **Fortran** : [PGI CUDA Fortran Compiler](<https://www.pgroup.com/resources/cudafortran.htm>)
  * [Haskell](</wzh/index.php?title=Haskell&action=edit&redlink=1> "Haskell（页面不存在）"): [accelerate package](<https://hackage.haskell.org/package/accelerate>)列出了可用的CUDA后端
  * [Java](<../zh-cn/Java.html> "Java"): [JCuda](<http://www.jcuda.org/jcuda/JCuda.html>)
  * [Mathematica](<../zh-cn/Mathematica.html> "Mathematica"): [CUDAlink](<https://reference.wolfram.com/mathematica/CUDALink/tutorial/Overview.html>)
  * [Mono/.NET](<../zh-cn/Mono.html> "Mono"): [CUDAfy.NET](<https://github.com/rapiddev/CUDAfy.NET>), [managedCuda](<https://github.com/kunzmi/managedCuda>)
  * [Perl](</wzh/index.php?title=Perl&action=edit&redlink=1> "Perl（页面不存在）"): [KappaCUDA](<https://metacpan.org/pod/KappaCUDA>), [CUDA-Minimal](<https://github.com/run4flat/perl-CUDA-Minimal>)
  * [Python](<../zh-cn/Python.html> "Python"): [python-pycuda](<https://archlinux.org/packages/?name=python-pycuda>)包
  * [Ruby](<../zh-cn/Ruby.html> "Ruby"): [rbcuda](<https://github.com/SciRuby/rbcuda>)
  * [Rust](<../zh-cn/Rust.html> "Rust"): [cuda-sys](<https://github.com/rust-cuda/cuda-sys>) (绑定) 或 [RustaCUDA](<https://github.com/bheisler/rustacuda>) (高级封装)

## ROCm

[ROCm](<https://rocm.docs.amd.com/en/latest/>) （Radeon开发计算平台）是AMD的开源并行计算架构。尽管其需要AMD GPU，一些ROCm工具却是硬件无关的。参见[ROCm for Arch Linux repository](<https://github.com/rocm-arch/rocm-arch>)。 

  * [rocm-hip-sdk](<https://archlinux.org/packages/?name=rocm-hip-sdk>)包：为AMD平台开发使用HIP的应用和库
  * [rocm-opencl-sdk](<https://archlinux.org/packages/?name=rocm-opencl-sdk>)包：为AMD平台开发基于OpenCL的应用

### HIP

[异构计算可移植接口（Heterogeneous Interface for Portability，HIP）](<https://rocmdocs.amd.com/en/latest/Programming_Guides/HIP_API_Guide.html>)是AMD的专用GPU编程环境，用于设计GPU硬件的高性能内核。HIP作为C++运行库API和编程语言，允许开发者为不同平台创建可移植应用。 

  * [rocm-hip-runtime](<https://archlinux.org/packages/?name=rocm-hip-runtime>)包：基本运行库，用于在AMD平台运行HIP应用
  * [hip-runtime-amd](<https://archlinux.org/packages/?name=hip-runtime-amd>)包：ROCm中用于AMDGPU的异构接口，支持polaris架构（RX 500系列）到RDNA 2架构（RX 6000系列）
  * [miopen-hip](<https://archlinux.org/packages/?name=miopen-hip>)包: AMD开源深度学习库，使用HIP后端
  * [hip-runtime-nvidia](<https://aur.archlinux.org/packages/hip-runtime-nvidia/>)AUR：ROCm中用于NVIDIA GPU的异构接口

**提示：** 关于Blender使用HIP的更多信息，参见[这里](<../zh-cn/Blender.html> "Blender")。

### OpenMP

[openmp-extras](<https://aur.archlinux.org/packages/openmp-extras/>)AUR提供了[AOMP](<https://github.com/ROCm-Developer-Tools/aomp>) \- 一个开源基于Clang/LLVM的编译器，提供OpenMP API在AMD GPU的支持。 

### OpenCL

[rocm-opencl-runtime](<https://archlinux.org/packages/?name=rocm-opencl-runtime>)包是ROCm框架的一部分，提供了OpenCL运行库。 

####  OpenCL图像支持

ROCm最新版本提供了OpenCL 图像支持，可用于GPGPU加速软件如Darktable。仅需[AMDGPU](<../zh-cn/AMDGPU.html> "AMDGPU")开源驱动和ROCm，不需要AMDGPU PRO。 
    
    $ /opt/rocm/bin/clinfo | grep -i "image support"
    
    Image support                                   Yes

###  疑难解答

首先确认你的GPU出现在`/opt/rocm/bin/rocminfo`的输出里。如果没有，这可能意味着ROCm不支持你的GPU或者ROCm软件在编译时未做相关配置。 

#### PyTorch

要让PyTorch支持ROCm,安装[python-pytorch-rocm](<https://archlinux.org/packages/?name=python-pytorch-rocm>)包。 
    
    $ python -c 'import torch; print(torch.cuda.is_available())'
    
    True

上面的命令如果没有返回`True`，那么python-pytorch-rocm可能在编译时没有支持你的GPU或者你的依赖存在冲突，你可以使用`ldd /usr/lib/libtorch.so`进行检查，输出结果应该不会有任何`.so`文件的丢失或多个不同版本的相同`.so`文件。 

##  支持GPGPU加速的软件

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** More application may support GPGPU. (在 [Talk:GPGPU](<../zh-cn/Talk:GPGPU.html>) 中讨论)

  * [Bitcoin](</wzh/index.php?title=Bitcoin&action=edit&redlink=1> "Bitcoin（页面不存在）")
  * [Blender](<../zh-cn/Blender.html> "Blender") – Nvidia GPU支持CUDA，AMD GPU支持HIP。详情参见[这里](<https://docs.blender.org/manual/en/latest/render/cycles/gpu_rendering.html>)
  * [BOINC](<../zh-cn/BOINC.html> "BOINC")
  * [FFmpeg](<../zh-cn/FFmpeg.html> "FFmpeg") – 详情参见[这里](<https://trac.ffmpeg.org/wiki/HWAccelIntro#OpenCL>)
  * [Folding@home](<../zh-cn/Folding@home.html> "Folding@home")
  * [GIMP](<../zh-cn/GIMP.html> "GIMP") – 实验性支持 – 更多信息参见[这里](<http://www.h-online.com/open/news/item/GIMP-2-8-RC-1-arrives-with-GPU-acceleration-1518417.html>)
  * [HandBrake](</wzh/index.php?title=HandBrake&action=edit&redlink=1> "HandBrake（页面不存在）")
  * [Hashcat](<../zh-cn/Hashcat.html> "Hashcat")
  * [LibreOffice](<../zh-cn/LibreOffice.html> "LibreOffice") Calc – 更多信息参见[这里](<https://help.libreoffice.org/Calc/OpenCL_Options>).
  * [mpv](<../zh-cn/Mpv.html> "Mpv") \- 参见 [mpv#Hardware video acceleration](<../zh-cn/Mpv.html#Hardware_video_acceleration> "Mpv").
  * [clinfo](<https://archlinux.org/packages/?name=clinfo>)包 – 确认系统可用的OpenCL平台和设备上所有可能（已知）的特性
  * [cuda_memtest](<https://aur.archlinux.org/packages/cuda_memtest/>)AUR – 一个GPU内存测试。尽管名字有cuda，它也支持OpenCL
  * [darktable](<https://archlinux.org/packages/?name=darktable>)包 – OpenCL特性需要至少1 GB现存和 _图形支持_ （使用clinfo命令检查）
  * [DaVinci Resolve](<../zh-cn/DaVinci_Resolve.html> "DaVinci Resolve") \- 非线性视频编辑器，同时支持OpenCL和CUDA
  * [imagemagick](<https://archlinux.org/packages/?name=imagemagick>)包
  * [lc0](<https://aur.archlinux.org/packages/lc0/>)AUR \- 用于搜索神经网络（支持tensorflow，OpenCL，CUDA和openblas）
  * [opencv](<https://archlinux.org/packages/?name=opencv>)包
  * [pyrit](<https://aur.archlinux.org/packages/pyrit/>)AUR
  * [python-pytorch-cuda](<https://archlinux.org/packages/?name=python-pytorch-cuda>)包 \- CUDA后端的PyTorch
  * [tensorflow-cuda](<https://archlinux.org/packages/?name=tensorflow-cuda>)包 \- TensorFlow的CUDA版本
  * [tensorflow-computecpp](<https://aur.archlinux.org/packages/tensorflow-computecpp/>)AUR \- TensorFlow的SYCL版本
  * [whisper.cpp-clblas](<https://aur.archlinux.org/packages/whisper.cpp-clblas/>)AUR 和 [whisper.cpp-cublas](<https://aur.archlinux.org/packages/whisper.cpp-cublas/>)AUR \- OpenAI Whisper 模型 的 C/C++ 移植(使用 OpenCL 和 CUDA 优化)
  * [xmrig](<https://archlinux.org/packages/?name=xmrig>)包 \- High Perf CryptoNote CPU and GPU (OpenCL, CUDA) miner

##  另见

  * [OpenCL官方主页](<https://www.khronos.org/opencl/>)
  * [SYCL官方主页](<https://www.khronos.org/sycl/>)
  * [SPIR官方主页](<https://www.khronos.org/spir/>)
  * [CUDA工具包主页](<https://developer.nvidia.com/cuda-toolkit>)
  * [Intel SDK用于OpenCL应用](<https://software.intel.com/en-us/intel-opencl>)
  * [ComputeCpp官方主页](<https://developer.codeplay.com/home/>)
  * [不同GPU的OpenCL框架支持列表](<https://gitlab.com/illwieckz/i-love-compute>)
