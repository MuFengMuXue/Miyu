[] Some of the information in this article may have drifted out of sync with current practices. Please help out by [checking over the content](https://wiki.gentoo.org/index.php?title=Blender&action=edit) ([how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide")).

**Resources**

[[]][Home](https://www.blender.org/)

[[]][Package information](https://packages.gentoo.org/packages/media-gfx/blender)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Blender_(software) "wikipedia:Blender (software)")

**Blender** is a free and open-source 3D creation suite. It can perform a variety of tasks, including modeling, rigging, animation, simulation, rendering, compositing and motion tracking, video editing, game creation and even 2D animation^[\[1\]](#cite_note-1)^. Blender\'s functionality can also be extended using add-ons written in [Python](https://wiki.gentoo.org/wiki/Python "Python"). Blender is a community-driven project, but is supported by the Blender Foundation which funds core development^[\[2\]](#cite_note-2)^.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Audio device support]](#Audio_device_support)
    -   [[2.2] [CUDA support]](#CUDA_support)
    -   [[2.3] [oneAPI support]](#oneAPI_support)
    -   [[2.4] [File format support]](#File_format_support)
    -   [[2.5] [Headless (server only)]](#Headless_.28server_only.29)
    -   [[2.6] [Memory allocator]](#Memory_allocator)
    -   [[2.7] [Memory profiling]](#Memory_profiling)
    -   [[2.8] [OpenColorio]](#OpenColorio)
    -   [[2.9] [OpenSubdiv]](#OpenSubdiv)
    -   [[2.10] [OpenVDB]](#OpenVDB)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)
-   [[5] [References]](#References)

## [Installation]

### [USE flags]

Blender has a lot of optional features that can be enabled for specific hardware or workflows. See [Configuration](https://wiki.gentoo.org/wiki/Blender#Configuration "Blender") for more information.

### [USE flags for] [media-gfx/blender](https://packages.gentoo.org/packages/media-gfx/blender) [[]] [3D Creation/Animation/Publishing System]

  ----------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+bullet`](https://packages.gentoo.org/useflags/+bullet)                           Enable Bullet (Physics Engine).
  [`+color-management`](https://packages.gentoo.org/useflags/+color-management)       Enable color management via media-libs/opencolorio.
  [`+cycles`](https://packages.gentoo.org/useflags/+cycles)                           Enable the Cycles raytracing render engine.
  [`+cycles-bin-kernels`](https://packages.gentoo.org/useflags/+cycles-bin-kernels)   Precompile the cycles render kernels for the CUDA/HIP/OneAPI backends, if they are enabled, at compile time. This makes it so that the user doesn\'t have to wait for the kernels to compile when they are used for the first time in Blender. If this option is not on, they will be built as needed at runtime.
  [`+embree`](https://packages.gentoo.org/useflags/+embree)                           Use embree to accelerate certain areas of the Cycles render engine.
  [`+ffmpeg`](https://packages.gentoo.org/useflags/+ffmpeg)                           Enable ffmpeg/libav-based audio/video codec support
  [`+fftw`](https://packages.gentoo.org/useflags/+fftw)                               Use FFTW library for computing Fourier transforms
  [`+fluid`](https://packages.gentoo.org/useflags/+fluid)                             Adds fluid simulation support via the built-in Mantaflow library.
  [`+gmp`](https://packages.gentoo.org/useflags/+gmp)                                 Add support for dev-libs/gmp (GNU MP library)
  [`+manifold`](https://packages.gentoo.org/useflags/+manifold)                       Enable Manifold render backend via sci-mathematics/manifold
  [`+nanovdb`](https://packages.gentoo.org/useflags/+nanovdb)                         Enable nanoVDB support in Cycles. Uses less memory than regular openVDB when rendering.
  [`+oidn`](https://packages.gentoo.org/useflags/+oidn)                               Enable OpenImageDenoiser Support
  [`+openexr`](https://packages.gentoo.org/useflags/+openexr)                         Support for the OpenEXR graphics file format
  [`+opengl`](https://packages.gentoo.org/useflags/+opengl)                           Add support for OpenGL (3D graphics)
  [`+openmp`](https://packages.gentoo.org/useflags/+openmp)                           Build support for the OpenMP (support parallel computing), requires \>=sys-devel/gcc-4.2 built with USE=\"openmp\"
  [`+openpgl`](https://packages.gentoo.org/useflags/+openpgl)                         Enable path guiding support in Cycles
  [`+opensubdiv`](https://packages.gentoo.org/useflags/+opensubdiv)                   Add rendering support form OpenSubdiv from Dreamworks Animation through media-libs/opensubdiv.
  [`+openvdb`](https://packages.gentoo.org/useflags/+openvdb)                         Enable openvdb for volumetric processing, like the voxel remesher. Also enables volumetric GPU preview rendering for Nvidia cards.
  [`+pdf`](https://packages.gentoo.org/useflags/+pdf)                                 Add general support for PDF (Portable Document Format), this replaces the pdflib and cpdflib flags
  [`+potrace`](https://packages.gentoo.org/useflags/+potrace)                         Add support for converting bitmaps into Grease pencil line using the potrace library.
  [`+pugixml`](https://packages.gentoo.org/useflags/+pugixml)                         Enable PugiXML support (Used for OpenImageIO, Grease Pencil SVG export)
  [`+rubberband`](https://packages.gentoo.org/useflags/+rubberband)                   Build with Rubber Band for audio time-stretching and pitch-scaling (used by Audaspace) via media-libs/rubberband
  [`+sndfile`](https://packages.gentoo.org/useflags/+sndfile)                         Add support for libsndfile
  [`+tbb`](https://packages.gentoo.org/useflags/+tbb)                                 Use threading building blocks library from dev-cpp/tbb.
  [`+tiff`](https://packages.gentoo.org/useflags/+tiff)                               Add support for the TIFF image format
  [`+truetype`](https://packages.gentoo.org/useflags/+truetype)                       Add support for FreeType and/or FreeType2 fonts
  [`+webp`](https://packages.gentoo.org/useflags/+webp)                               Add support for the WebP image format
  [`X`](https://packages.gentoo.org/useflags/X)                                       Add support for X11
  [`alembic`](https://packages.gentoo.org/useflags/alembic)                           Add support for Alembic through media-gfx/alembic.
  [`collada`](https://packages.gentoo.org/useflags/collada)                           Add support for Collada interchange format through media-libs/opencollada.
  [`cuda`](https://packages.gentoo.org/useflags/cuda)                                 Build cycles renderer with nVidia CUDA support.
  [`debug`](https://packages.gentoo.org/useflags/debug)                               Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`doc`](https://packages.gentoo.org/useflags/doc)                                   Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`experimental`](https://packages.gentoo.org/useflags/experimental)                 Enable experimental features
  [`gnome`](https://packages.gentoo.org/useflags/gnome)                               Add GNOME support
  [`hip`](https://packages.gentoo.org/useflags/hip)                                   Build cycles renderer with AMD HIP support.
  [`hiprt`](https://packages.gentoo.org/useflags/hiprt)                               Enable AMD HIP GPU ray tracing acceleration via dev-libs/hiprt.
  [`jack`](https://packages.gentoo.org/useflags/jack)                                 Add support for the JACK Audio Connection Kit
  [`jemalloc`](https://packages.gentoo.org/useflags/jemalloc)                         Use dev-libs/jemalloc for memory management
  [`jpeg2k`](https://packages.gentoo.org/useflags/jpeg2k)                             Support for JPEG 2000, a wavelet-based image compression format
  [`man`](https://packages.gentoo.org/useflags/man)                                   Build and install man pages
  [`ndof`](https://packages.gentoo.org/useflags/ndof)                                 Enable NDOF input devices (SpaceNavigator and friends).
  [`nls`](https://packages.gentoo.org/useflags/nls)                                   Add Native Language Support (using gettext - GNU locale utilities)
  [`openal`](https://packages.gentoo.org/useflags/openal)                             Add support for the Open Audio Library
  [`optix`](https://packages.gentoo.org/useflags/optix)                               Add support for NVIDIA\'s OptiX Raytracing Engine.
  [`osl`](https://packages.gentoo.org/useflags/osl)                                   Add support for OpenShadingLanguage scripting.
  [`pipewire`](https://packages.gentoo.org/useflags/pipewire)                         Enable Pipewire for audio support on Linux
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)                     Add sound server support via media-libs/libpulse (may be PulseAudio or PipeWire)
  [`renderdoc`](https://packages.gentoo.org/useflags/renderdoc)                       Build Blender with renderdoc support
  [`sdl`](https://packages.gentoo.org/useflags/sdl)                                   Add support for Simple Direct Layer (media library)
  [`test`](https://packages.gentoo.org/useflags/test)                                 Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`valgrind`](https://packages.gentoo.org/useflags/valgrind)                         Enable annotations for accuracy. May slow down runtime slightly. Safe to use even if not currently using dev-debug/valgrind
  [`vulkan`](https://packages.gentoo.org/useflags/vulkan)                             Add support for the Vulkan viewport backend
  [`wayland`](https://packages.gentoo.org/useflags/wayland)                           Enable dev-libs/wayland backend
  ----------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-13 15:28] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask media-gfx/blender`

** Note**\
To test what unstable packages an unstable version might need, making use of the [`--autounmask=y --autounmask-write`](https://wiki.gentoo.org/wiki/Knowledge_Base:Accepting_a_keyword_for_a_single_package#Using_--autounmask-write "Knowledge Base:Accepting a keyword for a single package") emerge options can be helpful in populating a list for further review.

## [Configuration]

Since Blender supports so many different hardware configurations, platforms, and use cases there are a lot of optional `USE` flags that can be enabled.

### [Audio device support]

Support for [PulseAudio](https://wiki.gentoo.org/wiki/PulseAudio "PulseAudio"), [JACK](https://wiki.gentoo.org/wiki/JACK "JACK"), [OpenAL](https://wiki.gentoo.org/index.php?title=OpenAL&action=edit&redlink=1 "OpenAL (page does not exist)"), and [SDL](https://wiki.gentoo.org/index.php?title=SDL&action=edit&redlink=1 "SDL (page does not exist)") audio can optionally be enabled through their respective `USE` flags.

To choose the preferred audio backend, go to the Edit-\>Preferences-\>System tab and set the Audio Dev to the desired setting.

### [CUDA support]

Cycles renderer can work on GPUs, for example Nvidia GTX 970 is about twice as fast as an i5 4690k on traditional BMW benchmark.

To enable graphics card rendering with Nvidia graphics cards, install Cuda:

`root `[`#`]`emerge --ask --verbose dev-util/nvidia-cuda-toolkit`

Inside Blender, go to the Edit-\>Preferences-\>System tab and set Compute Device to CUDA and select the graphics card in the box below. If the graphics card is not supported these options will not be visible.

Now set the renderer to Cycles Renderer and in the renderer panel under the Render options set the Device to GPU Compute.

The first time a render is created with a new version of blender, the CUDA kernels will need to be compiled. This may take over 15 minutes.

[oneAPI section of oneAPI](https://wiki.gentoo.org/wiki/OneAPI#oneAPI "OneAPI")

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

`root `[`#`]`echo 'dev-util/intel-graphics-compiler vc' > /etc/portage/package.use/intel`

`root `[`#`]`emerge --ask --verbose dev-util/intel-graphics-compiler`

** Note**\
At yet, oneAPI use flag is not implemented on the Gentoo compiled version of blender media-gfx/blender.

But with the binary ebuild media-gfx/blender-bin-5.1.1, OneAPI is working. If you use a binary package of blender obtained from \[[blender.org](https://www.blender.org/download/)\])

Actually Blender **5.0.1** is a minimal version to have oneAPI support.

------------------------------------------------------------------------

If you have some issues, perhaps you need this package **intel-level-zero-gpu-raytracing**

Install this ebuild at the version 1.1.0 of **dev-libs/level-zero-gpu-raytracing** from this Gentoo \[[repos](https://codeberg.org/lastrodamo/gentoo-overlay/src/branch/main/dev-libs/level-zero-gpu-raytracing)\]. How to install a [custom repository](https://wiki.gentoo.org/wiki/Handbook:AMD64/Portage/CustomTree#Creating_a_custom_ebuild_repository "Handbook:AMD64/Portage/CustomTree")

`root `[`#`]`emerge --ask --verbose dev-libs/level-zero-gpu-raytracing`

### [File format support]

Support OpenCOLLADA (.dae), jpeg2k, sndfile, and tiff image file formats can optionally be enabled through USE flags.

The `collada` USE flag adds entries to File-\>Import/Export for Collada (Default) (.dae) files. The others can be used with background images in the properties panel of the 3D View or as output formats in the render panel.

Blender should work with either ffmpeg or libav libraries, although only ffmpeg is officially recommended by the Blender developers.

### [][Headless (server only)]

For render farms it is possible to compile blender with the `headless` USE flag. This is *not recommended* for most users.

This feature reduces the Blender file size by around 5 MB, but it **will not be possible to run blender normally** as the GUI is not available.

In headless mode, Blender can still be used to run python scripts from the commmand line:

`user `[`$`]`blender -b -P script.py [-- [--optionsforscript .. ] ]`

** Note**\
This functionality is also available with regular versions of Blender, it is not necessary to enable the `headless` USE flag to run scripts from the command line.

### [Memory allocator]

It is recommended to enable `jemalloc` to use a more efficient memory allocator. This reduces wasted memory during rendering and allows for larger scenes to be rendered.

### [Memory profiling]

Support for memory profiling can be enabled using the `valgrind` USE flag. See [Debugging](https://wiki.gentoo.org/wiki/Debugging "Debugging") for instructions on setting up Valgrind.

### [OpenColorio]

Open Colorio provides additional options under the Color Management section of the Scene panel.

Inside Blender, select the Render View and Look options, and adjust the exposure, gamma, and curves to obtain the desired look.

### [OpenSubdiv]

*OpenSubdiv* is a set of libraries that provide high-performance subdivision surface modifier evaluation^[\[3\]](#cite_note-3)^. This can dramatically improve the frame rate of viewing animations in the viewport when using high levels of subdivision. Enable the `opensubdiv` `USE` flag to enable support in Blender.

** Note**\
Not all cards are suitable. The current code checks for geometry shader, GL_ARB_gpu_shader5, glProgramParameteri, glProgramParameteriEXT, and glProgramParameteriARB. These are available as part of OpenGL 3.2, 4.0, and 4.1, or as extensions.

### [OpenVDB]

OpenVDB provides a data structure for storing and manipulating volumetric information efficiently. It can be compiled into blender using the `openvdb` USE flag, and `openvdb-compression` is also recommended as the data can require upwards of 20MB.

In Blender, set the renderer to Cycles Renderer. Go to the physics panel and enable physics for Smoke. In the smoke section select Domain. Save the file to enable editing of the smoke cache. Change File Format to Openvdb and select Blosc compression if desired. Now create and bake the simulation.

## [See also]

-   [Debugging](https://wiki.gentoo.org/wiki/Debugging "Debugging")
-   [SpaceNavigator](https://wiki.gentoo.org/wiki/SpaceNavigator "SpaceNavigator")
-   [OpenCL](https://wiki.gentoo.org/wiki/OpenCL "OpenCL") --- a framework for writing programs that execute across heterogeneous computing platforms (CPUs, GPUs, DSPs, FPGAs, ASICs, etc.).
-   [Project:Artwork/Artwork](https://wiki.gentoo.org/wiki/Project:Artwork/Artwork "Project:Artwork/Artwork"): Gentoo artwork, including a .blend file used to create some of it.

## [External resources]

-   [Gentoo specific build instructions for Blender from Blender Wiki](https://wiki.blender.org/wiki/Building_Blender/Linux/Gentoo)

## [References]

1.  [[[↑](#cite_ref-1)] [[https://www.blender.org/about/](https://www.blender.org/about/)]]
2.  [[[↑](#cite_ref-2)] [[https://fund.blender.org/about/](https://fund.blender.org/about/)]]
3.  [[[↑](#cite_ref-3)] [[https://graphics.pixar.com/opensubdiv/overview.html](https://graphics.pixar.com/opensubdiv/overview.html)]]