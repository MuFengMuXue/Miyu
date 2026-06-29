### [oneAPI support]

Install the driver of your [[intel](https://wiki.gentoo.org/wiki/Intel "Intel")] GPU

To enable graphics card rendering with Intel graphics cards with oneAPI, we needs some libraries dependencies:

See \[[documentation](https://docs.blender.org/manual/fr/dev/render/cycles/gpu_rendering.html#oneapi-intel)\] of Blender

1\. dev-libs/intel-compute-runtime

`root `[`#`]`emerge --ask --verbose dev-libs/intel-compute-runtime`

2\. dev-libs/level-zero

`root `[`#`]`emerge --ask --verbose dev-libs/level-zero`

3\. dev-util/intel-graphics-compiler

Add **vc** use flag for **intel-graphics-compiler**:

`root `[`#`]`` echo `dev-util/intel-graphics-compiler vc` > /etc/portage/package.use/intel ``

`root `[`#`]`emerge --ask --verbose dev-util/intel-graphics-compiler`

** Note**\
At yet, oneAPI use flag is not implemented on the Gentoo compiled version of blender media-gfx/blender.

But with the binary ebuild media-gfx/blender-bin-5.1.1, OneAPI is working. If you use a binary package of blender obtained from \[[blender.org](https://www.blender.org/download/)\])

Actually Blender **5.0.1** is a minimal version to have oneAPI support.

------------------------------------------------------------------------

If you have some issues, perhaps you need this package **intel-level-zero-gpu-raytracing**

Install this ebuild at the version 1.1.0 of **dev-libs/level-zero-gpu-raytracing** from on this Gentoo \[[repos](https://codeberg.org/lastrodamo/gentoo-overlay/src/branch/main/dev-libs/level-zero-gpu-raytracing)\]. How to install a [custom repository](https://wiki.gentoo.org/wiki/Handbook:AMD64/Portage/CustomTree#Creating_a_custom_ebuild_repository "Handbook:AMD64/Portage/CustomTree")

`root `[`#`]`emerge --ask --verbose dev-libs/level-zero-gpu-raytracing`