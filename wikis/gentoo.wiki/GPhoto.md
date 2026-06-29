**Resources**

[[]][Home](http://gphoto.sourceforge.net)

[[]][Wikipedia](https://en.wikipedia.org/wiki/GPhoto "wikipedia:GPhoto")

[[]][[#gphoto](ircs://irc.libera.chat/#gphoto)] ([[webchat](https://web.libera.chat/#gphoto)])

***gPhoto** is a set of software applications and libraries for use in digital photography. gPhoto supports not just retrieving of images from camera devices, but also upload and remote controlled configuration and capture, depending on whether the camera supports those features.* - Wikipedia, the free encyclopedia

## [Installation]

gPhoto support can be enabled system-wide by setting the `USE` variable to `gphoto2`.

[FILE] **`/etc/portage/make.conf`**

    USE="gphoto2"

another way of enabling it is by creating a file named [gphoto2] in [/etc/portage/package.use]:

[FILE] **`/etc/portage/package.use/gphoto2`**

    */* gphoto2

Enabling gPhoto support will pull in the [[[media-libs/libgphoto2]](https://packages.gentoo.org/packages/media-libs/libgphoto2)[]] package, which has the following USE flags:

### [USE flags for] [media-libs/libgphoto2](https://packages.gentoo.org/packages/media-libs/libgphoto2) [[]] [Library that implements support for numerous digital cameras]

  ----------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------
  [`doc`](https://packages.gentoo.org/useflags/doc)                 Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`examples`](https://packages.gentoo.org/useflags/examples)       Install examples, usually source code
  [`exif`](https://packages.gentoo.org/useflags/exif)               Add support for reading EXIF headers from JPEG and TIFF images
  [`gd`](https://packages.gentoo.org/useflags/gd)                   Add support for media-libs/gd (to generate graphics on the fly)
  [`jpeg`](https://packages.gentoo.org/useflags/jpeg)               Add JPEG image support
  [`nls`](https://packages.gentoo.org/useflags/nls)                 Add Native Language Support (using gettext - GNU locale utilities)
  [`serial`](https://packages.gentoo.org/useflags/serial)           Enable serial port support
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-20 09:28] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

The system needs to be updated if the `USE` variable was set to `gphoto2`.

`root `[`#`]`emerge --ask --changed-use --deep @world`

Install [[[media-gfx/gphoto2]](https://packages.gentoo.org/packages/media-gfx/gphoto2)[]] for a command-line interface to libgphoto2.

`root `[`#`]`emerge --ask media-gfx/gphoto2`

## [Usage]

To import images from a camera, skipping already existing files, plug it in, change to the image import directory, and run:

`user `[`$`]`gphoto2 --get-all-files --skip-existing`