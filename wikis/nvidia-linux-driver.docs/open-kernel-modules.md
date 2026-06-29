## Chapter 45. Open Linux Kernel Modules

### Introduction

The NVIDIA Linux GPU Driver contains several kernel modules: nvidia.ko, nvidia-modeset.ko, nvidia-uvm.ko, nvidia-drm.ko, and nvidia-peermem.ko.

Two "flavors" of these kernel modules are provided:

- Open, i.e. source-published, kernel modules that are dual licensed MIT/GPLv2. With every driver release, the source code to the open kernel modules is published on https://github.com/NVIDIA/open-gpu-kernel-modules and a tarball is provided on https://download.nvidia.com/XFree86/.

- Proprietary. This is the flavor that NVIDIA has historically shipped.

We recommend the use of open kernel modules on all GPUs that support it.

Though the kernel modules in the two flavors are different, they are based on the same underlying source code. The two flavors are mutually exclusive: they cannot be used within the kernel at the same time, and they should not be installed on the filesystem at the same time.

The user space components of the NVIDIA Linux GPU driver are identical and behave in the same way, regardless of which flavor of kernel module is used.

### Supported Features

The proprietary flavor supports the GPU architectures Maxwell, Pascal, Volta, Turing, and later GPUs until Blackwell. Blackwell and later are only supported by the open kernel modules.

The open flavor of kernel modules supports Turing and later GPUs. The open kernel modules cannot support GPUs before Turing, because the open kernel modules depend on the GPU System Processor (GSP) first introduced in Turing.

The following features will only work with the open kernel modules flavor of the driver:

- NVIDIA Confidential Computing

- Magnum IO GPUDirect Storage (GDS)

- Heterogeneous Memory Management (HMM)

- CPU affinity for GPU fault handlers

- DMABUF support for CUDA allocations

### Known Issues

The following are some known limitations of the open kernel modules versus the proprietary kernel modules with GSP firmware mode disabled:

- GPU initialization is slower. One possible mitigation is to use nvidia-persistenced to initialize the GPU(s) in advance, before running applications that use the GPU.

- Enter and exit latencies for power-saving modes like S3, S4 and Run Time D3 (RTD3) can be longer due to additional GSP state being restored.

- GPU power consumption can be marginally impacted in some scenarios.

- Run Time D3 (RTD3) is only supported on Ampere and above GPUs.

### Installation

Because the two flavors of kernel modules are mutually exclusive, one or the other must be chosen at install time. By default, installation will choose which flavor of kernel modules to install, based on the GPUs detected in the system. If a pre-Turing GPU is detected, installation will default to the proprietary flavor of kernel modules. Otherwise, installation will default to the open flavor of kernel modules.

This default can be overridden with the "--kernel-module-type" .run file option, or its short form "-M". Use "-M=proprietary" to force installation of the proprietary flavor of kernel modules, or "-M=open" to force installation of the open flavor of kernel modules.

E.g.,

``` screen
    sh ./NVIDIA-Linux-[...].run -m=kernel-open
```

As a convenience, the open kernel modules distributed in the .run file are pre-compiled.

Advanced users, who want to instead build the open kernel modules from source, should do the following:

- Uninstall any existing driver with \`nvidia-uninstall\`.

- Install from the .run file with "--no-kernel-modules" option, to install everything except the kernel modules.

- Fetch, build, and install the open kernel module source from https://github.com/NVIDIA/open-gpu-kernel-modules. See https://github.com/NVIDIA/open-gpu-kernel-modules/blob/main/README.md for details on building.

Note that you must use the same version of the .run file and the open kernel module source from https://github.com/NVIDIA/open-gpu-kernel-modules

You can determine which flavor of kernel modules is installed using either \`modinfo\` or looking at /proc/driver/nvidia/version.

E.g., the proprietary flavor will report:

``` screen
    # modinfo nvidia | grep license
    license:        NVIDIA

    # cat /proc/driver/nvidia/version
    NVRM version: NVIDIA UNIX x86_64 Kernel Module  [...]
```

The open flavor will report:

``` screen
    # modinfo nvidia | grep license
    license:        Dual MIT/GPL

    # cat /proc/driver/nvidia/version
    NVRM version: NVIDIA UNIX Open Kernel Module for x86_64  [...]
```
