**Resources**

[[]][Home](https://www.amd.com/en/technologies/radeon-prorender)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Radeon_Pro#ProRender "wikipedia:Radeon Pro")

[[]][GitHub](https://github.com/GPUOpen-LibrariesAndSDKs/RadeonProRenderSDK)

[[]][Bugs (upstream)](https://github.com/GPUOpen-LibrariesAndSDKs/RadeonProRenderSDK/issues)

AMD [Radeon ProRender](https://github.com/GPUOpen-LibrariesAndSDKs/RadeonProRenderSDK) is a powerful physically-based rendering engine that enables creative professionals to produce stunningly photorealistic images. [https://www.amd.com/en/technologies/radeon-prorender](https://www.amd.com/en/technologies/radeon-prorender)

## Contents

-   [[1] [ProRender SDK]](#ProRender_SDK)
    -   [[1.1] [Repository preparation]](#Repository_preparation)
        -   [[1.1.1] [eselect repository]](#eselect_repository)
    -   [[1.2] [SDK installation]](#SDK_installation)
    -   [[1.3] [Tutorials]](#Tutorials)
        -   [[1.3.1] [Build]](#Build)
        -   [[1.3.2] [Run]](#Run)
-   [[2] [Image Processing Library]](#Image_Processing_Library)
    -   [[2.1] [Tutorials]](#Tutorials_2)
        -   [[2.1.1] [Build]](#Build_2)
        -   [[2.1.2] [Run]](#Run_2)
-   [[3] [Resources]](#Resources)

## [ProRender SDK]

### [Repository preparation]

Ebuild for SDK installation not in official gentoo repository, but can be found in [feniksa](https://github.com/feniksa/gentoo-overlay/tree/master/dev-util/radeon-pro-render-sdk) overlay. Use [eselect repository] to configure the additional repository.

#### [eselect repository]

Install [[[app-eselect/eselect-repository]](https://packages.gentoo.org/packages/app-eselect/eselect-repository)[]]:

`root `[`#`]`emerge --ask --noreplace app-eselect/eselect-repository`

Enable and sync the feniksa repository:

`root `[`#`]`eselect repository enable feniksa`

`root `[`#`]`emerge --sync feniksa`

### [SDK installation]

To install Radeon Pro Render SDK:

`root `[`#`]`emerge --ask dev-libs/radeon-pro-render-sdk`

### [Tutorials]

#### [Build]

Install the package with the examples USE flag:

`root `[`#`]`emerge --ask dev-libs/radeon-pro-render-sdk[examples]`

#### [Run]

All tutorial binaries may be found at [/usr/share/RadeonProRender/tutorials/Bin] directory. First, let\'s check ProRender initialize

`root `[`#`]`cd /usr/share/RadeonProRender/tutorials/Bin `

`root `[`#`]`./00_context_creation64D`

    Radeon ProRender SDK simple context creation tutorial.
    RPR Context creation succeeded.
    GPU0 name : NVIDIA GeForce GTX 1080

If everything is fine, last line should show GPU name. It means, that RadeonProRender correctly initialize OpenCL, found available GPU and initialized resources for PBR rendering . Source code of this tutorial may be found at [/usr/share/RadeonProRender/tutorials/00_context_creation/main.cpp]

** Note**\
First run may take up to 2 minutes for RadeonProRender kernel compilation

Let\'s run some PBR

`root `[`#`]`cd /usr/share/RadeonProRender/tutorials/Bin `

`root `[`#`]`./22_material_uber64D`

    RPR Context creation succeeded.
    Rendering 22_material_uber_00.png ...
    Rendering 22_material_uber_01.png ...
    Rendering 22_material_uber_02.png ...
    Rendering 22_material_uber_03.png ...
    Rendering 22_material_uber_04.png ...
    Rendering 22_material_uber_05.png ...
    Rendering 22_material_uber_06.png ...
    Rendering 22_material_uber_07.png ...
    Rendering 22_material_uber_08.png ...
    Rendering 22_material_uber_final.png ...

In folder [/usr/share/RadeonProRender/tutorials/Bin] should be png files with result of rendering. Source code of material creation may be found at [/usr/share/RadeonProRender/tutorials/22_material_uber/main.cpp]

## [Image Processing Library]

To install Radeon Pro Render [Image Filtering library](https://github.com/GPUOpen-LibrariesAndSDKs/RadeonImageFilter)

`root `[`#`]`emerge --ask dev-libs/radeon-pro-image-filter`

### [Tutorials]

#### [Build]

Install the package with the examples USE flag:

`root `[`#`]`emerge --ask dev-libs/radeon-pro-image-filter[examples]`

#### [Run]

All tutorial binaries may be found at [/usr/share/RadeonImageFilter/samples/Bin] directory. First, let\'s check ProRender initialize

`root `[`#`]`cd /usr/share/RadeonImageFilter `

`root `[`#`]` mkdir images `

`root `[`#`]`./samples/Bin/AIDenoiser/AIDenoiser`

    [MSG  @RIF]: Loaded RIF API version: 1.7.3.0x1c7b817e
    INFO: MIOpen version: 2.0.5
    [MSG  @RIF]: Loading model: ./models/denoise_c9_ldr.pb
    INFO: Memory: required: 0, single node max: 0, requested sum: 0
    RIF inference time: 57133 us. Resolution is : 600x800
    outputPath=./images/output_0.hdr

\
In folder [/usr/share/RadeonImageFilter/images] should be png/hdr files with sample run results

\

## [Resources]

-   [RadeonProRenderSDK github repository](https://github.com/GPUOpen-LibrariesAndSDKs/RadeonProRenderSDK)
-   [RadeonProRenderSDK documentation](https://radeon-pro.github.io/RadeonProRenderDocs/en/index.html)
-   [Image Filtering library for RadeonProRenderSDK (postprocessing)](https://gpuopen.com/radeon-image-filtering-library/)
-   [Image Filtering library on Github](https://github.com/GPUOpen-LibrariesAndSDKs/RadeonImageFilter)
-   [Radeon Pro Render technology suite](https://gpuopen.com/radeon-prorender-suite)
-   [RadeonProRender SDK news](https://community.amd.com/t5/radeon-pro-graphics/amd-radeon-prorender-developer-updates-and-new-beta-plug-ins/ba-p/414280)