**Resources**

[[]][Home](https://www.darktable.org/)

[[]][GitHub](https://github.com/darktable-org/darktable)

[[]][Official documentation](https://www.darktable.org/usermanual/en/)

[[]][Package information](https://packages.gentoo.org/packages/media-gfx/darktable)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Darktable "wikipedia:Darktable")

**darktable** is a photography workflow application and [RAW](https://en.wikipedia.org/wiki/Raw_image_format "wikipedia:Raw image format") developer. It simplifies managing large numbers of RAW photos and their post-production in a non-destructive manner.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
-   [[2] [Config]](#Config)
-   [[3] [Utilities]](#Utilities)
    -   [[3.1] [darktable-cli]](#darktable-cli)
    -   [[3.2] [darktable-cmstest]](#darktable-cmstest)
    -   [[3.3] [darktable-cltest]](#darktable-cltest)
    -   [[3.4] [dt-curve-tool]](#dt-curve-tool)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Installation]

** Note**\
Building darktable with GCC requires Graphite support. Either [[[sys-devel/gcc]](https://packages.gentoo.org/packages/sys-devel/gcc)[]] should be built with the [[[graphite]](https://packages.gentoo.org/useflags/graphite)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] `USE` flag, or a different compiler should be used.

`root `[`#`]`emerge --ask media-gfx/darktable`

### [USE flags]

### [USE flags for] [media-gfx/darktable](https://packages.gentoo.org/packages/media-gfx/darktable) [[]] [A virtual lighttable and darkroom for photographers]

  ------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`X`](https://packages.gentoo.org/useflags/X)                             Add support for X11
  [`avif`](https://packages.gentoo.org/useflags/avif)                       Add AV1 Image Format (AVIF) support
  [`colord`](https://packages.gentoo.org/useflags/colord)                   Support color management using x11-misc/colord
  [`cups`](https://packages.gentoo.org/useflags/cups)                       Add support for CUPS (Common Unix Printing System)
  [`doc`](https://packages.gentoo.org/useflags/doc)                         Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`gamepad`](https://packages.gentoo.org/useflags/gamepad)                 Support using game controllers as input devices
  [`geolocation`](https://packages.gentoo.org/useflags/geolocation)         Enable geotagging support
  [`gphoto2`](https://packages.gentoo.org/useflags/gphoto2)                 Add digital camera support
  [`graphicsmagick`](https://packages.gentoo.org/useflags/graphicsmagick)   Build and link against GraphicsMagick instead of ImageMagick (requires USE=imagemagick if optional)
  [`heif`](https://packages.gentoo.org/useflags/heif)                       Enable support for ISO/IEC 23008-12:2017 HEIF/HEIC image format
  [`jpeg2k`](https://packages.gentoo.org/useflags/jpeg2k)                   Support for JPEG 2000, a wavelet-based image compression format
  [`jpegxl`](https://packages.gentoo.org/useflags/jpegxl)                   Add JPEG XL image support
  [`keyring`](https://packages.gentoo.org/useflags/keyring)                 Enable support for freedesktop.org Secret Service API password store
  [`kwallet`](https://packages.gentoo.org/useflags/kwallet)                 Enable encrypted storage of passwords with kde-frameworks/kwallet
  [`lto`](https://packages.gentoo.org/useflags/lto)                         Enable link-time optimisations in the RawSpeed library
  [`lua`](https://packages.gentoo.org/useflags/lua)                         Enable Lua scripting support
  [`midi`](https://packages.gentoo.org/useflags/midi)                       Support using MIDI input devices such as Behringer X-Touch Mini, Arturia Beatstep or Korg nanoKONTROL2, as input devices
  [`opencl`](https://packages.gentoo.org/useflags/opencl)                   Enable OpenCL support (computation on GPU)
  [`openexr`](https://packages.gentoo.org/useflags/openexr)                 Support for the OpenEXR graphics file format
  [`openmp`](https://packages.gentoo.org/useflags/openmp)                   Build support for the OpenMP (support parallel computing), requires \>=sys-devel/gcc-4.2 built with USE=\"openmp\"
  [`test`](https://packages.gentoo.org/useflags/test)                       Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`tools`](https://packages.gentoo.org/useflags/tools)                     Install tools for generating base curves and noise profiles
  [`wayland`](https://packages.gentoo.org/useflags/wayland)                 Enable dev-libs/wayland backend
  [`webp`](https://packages.gentoo.org/useflags/webp)                       Add support for the WebP image format
  ------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-23 06:12] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

** Note**\
For [OpenCL](https://wiki.gentoo.org/wiki/OpenCL "OpenCL") compatibility consult the [darktable-cltest](https://wiki.gentoo.org/wiki/Darktable#darktable-cltest "Darktable") tool.

## [Config]

Basic settings can be altered in [\~/.config/darktable/darktablerc].

## [Utilities]

The [[[media-gfx/darktable]](https://packages.gentoo.org/packages/media-gfx/darktable)[]] package provides a few additional tools (some of them are optional - controlled by the `tools` USE flag).

### [darktable-cli]

Using [darktable-cli] it is possible to use darktable for a non-interactive batch processing and export.

### [darktable-cmstest]

[darktable-cmstest] helps debugging color management issues (eg. exported photo colors don\'t match the darktable\'s). Also it indicates whether the `colord` USE flag was enabled.

### [darktable-cltest]

Darktable with enabled `opencl` USE flag supports [OpenCL](https://wiki.gentoo.org/wiki/OpenCL "OpenCL")-based GPU acceleration. The [darktable-cltest] utility helps debugging the darktable\'s setup and OpenCL driver interactions.

### [dt-curve-tool]

In order to improve approximation of camera\'s built-in JPEG engine with the default RAW processing settings you can use the [dt-curve-tool].

## [See also]

-   [Color management](https://wiki.gentoo.org/wiki/Color_management "Color management") --- a computer technique for ensuring colors stay the same or at least as close as possible between devices.

## [External resources]

-   [dt-curve-tool](https://github.com/darktable-org/darktable/tree/master/tools/basecurve) - [dt-curve-tool] manual
-   [faq](https://www.darktable.org/about/faq/) - Official darktable FAQ
-   [camera support](https://www.darktable.org/resources/camera-support/) - List of supported cameras