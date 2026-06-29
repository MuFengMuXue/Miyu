[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=ROCm_packaging_history&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

## [Early days]

[ROCm overlay](https://github.com/justxi/rocm)

## [][Brief history of [[[dev-util/hip]](https://packages.gentoo.org/packages/dev-util/hip)[]] and [[[dev-libs/rocm-opencl-runtime]](https://packages.gentoo.org/packages/dev-libs/rocm-opencl-runtime)[]]]

At first (ROCm-4) [hip](https://github.com/ROCm/HIP/tree/rocm-4.0.x), [rocm-opencl-runtime](https://github.com/ROCm/rocm-opencl-runtime/tree/rocm-4.0.x), [rocclr](https://github.com/ROCm/rocclr/tree/rocm-4.0.x) are in separated repositories and separated ebuilds. [[[dev-libs/rocm-opencl-runtime]](https://packages.gentoo.org/packages/dev-libs/rocm-opencl-runtime)[]] and [[[dev-util/hip]](https://packages.gentoo.org/packages/dev-util/hip)[]] both depend on (link to) [[[dev-libs/rocclr]](https://packages.gentoo.org/packages/dev-libs/rocclr)[]]. CLR stands for *compute language runtime*.

From ROCm-4.5 AMD [make rocclr a static library bundled to rocm-opencl-runtime and hip runtime](https://github.com/ROCm/ROCclr/blob/rocm-4.5.x/CMakeLists.txt). So [[[dev-libs/rocclr]](https://packages.gentoo.org/packages/dev-libs/rocclr)[]] disappeared.

Also from ROCm-4.5 hip upstream is split into [HIP](https://github.com/ROCm/HIP) and [hipamd](https://github.com/ROCm/hipamd), former one mainly contains vendor independent headers, utilities (like clang wrapper hipcc), tests, samples. [hipamd](https://github.com/ROCm/hipamd) repo is for AMD GPUs, providing hip runtime library and some [Perl](https://wiki.gentoo.org/wiki/Perl "Perl") scripts roc-obj-\* to inspect AMDGPU kernel in ELF binaries. Building hip runtime requires [rocclr](https://github.com/ROCm/rocclr/tree/rocm-4.5.x) + [HIP](https://github.com/ROCm/HIP) + [hipamd](https://github.com/ROCm/hipamd). Gentoo use one [[[dev-util/hip]](https://packages.gentoo.org/packages/dev-util/hip)[]] to package them. That is the case for ROCm-5 ebuilds.

From this point HIP can also build with NVIDIA CUDA backend, but not enabled in ROCm-5 ebuilds.

During ROCm-5, HIP got further separated into [HIP](https://github.com/ROCm/HIP) (headers) [HIPCC](https://github.com/ROCm/HIPCC) (clang wrapper) and [hip-tests](https://github.com/ROCm/hip-tests) (tests, samples). And [[[dev-util/hipcc]](https://packages.gentoo.org/packages/dev-util/hipcc)[]] was separated from [[[dev-util/hip]](https://packages.gentoo.org/packages/dev-util/hip)[]] in 5.7.

Also, from ROCm-5.6 upstream merged [rocclr](https://github.com/ROCm/rocclr) + [hipamd](https://github.com/ROCm/hipamd) + [rocm-opencl-runtime](https://github.com/ROCm/rocm-opencl-runtime) into [clr](https://github.com/ROCm/clr) as the AMD GPU backend for both hip and opencl. Supporting what language depends on [Cmake](https://wiki.gentoo.org/index.php?title=Cmake&action=edit&redlink=1 "Cmake (page does not exist)") argument `CLR_BUILD_HIP` and `CLR_BUILD_OCL`. So building [[[dev-util/hip]](https://packages.gentoo.org/packages/dev-util/hip)[]] needs [clr](https://github.com/ROCm/clr) + [HIP](https://github.com/ROCm/HIP) (and testing needs [hip-tests](https://github.com/ROCm/hip-tests)) with `CLR_BUILD_HIP=On`, while building [[[dev-libs/rocm-opencl-runtime]](https://packages.gentoo.org/packages/dev-libs/rocm-opencl-runtime)[]] only needs [clr](https://github.com/ROCm/clr) with `CLR_BUILD_OCL=On`.

As of ROCm-6, upstream introduced hipother repo to provide wrapper headers of CUDA backend. And Gentoo packages [[[dev-libs/hipother]](https://packages.gentoo.org/packages/dev-libs/hipother)[]]. hip can only have one backend.