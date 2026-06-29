[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=QtWebEngine&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://wiki.qt.io/QtWebEngine)

[[]][Package information](https://packages.gentoo.org/packages/dev-qt/qtwebengine)

[[]][GitHub](https://github.com/qt/qtwebengine)

**QtWebEngine** is a web browser library that integrates [Chromium](https://wiki.gentoo.org/wiki/Chromium "Chromium") into [Qt](https://wiki.gentoo.org/wiki/Qt "Qt"). It is usually pulled in as a dependency rather than installed directly.

This package may take particularly long to compile, the [[[jumbo-build]](https://packages.gentoo.org/useflags/jumbo-build)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] use flag may help.

** Tip**\
[Gentoo\'s public binhost](https://wiki.gentoo.org/wiki/Gentoo_Binary_Host_Quickstart "Gentoo Binary Host Quickstart") contains qtwebengine, for much faster installation.

** See also**\
[Minimizing compilation and installation time](https://wiki.gentoo.org/wiki/Minimizing_compilation_and_installation_time#QtWebEngine "Minimizing compilation and installation time") for tips on avoiding installing QtWebEngine, if it is not desired.

## [Use flags]

### [USE flags for] [dev-qt/qtwebengine](https://packages.gentoo.org/packages/dev-qt/qtwebengine) [[]] [Library for rendering dynamic web content in Qt6 C++ and QML applications]

  ----------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+alsa`](https://packages.gentoo.org/useflags/+alsa)                   Add support for media-libs/alsa-lib (Advanced Linux Sound Architecture)
  [`+jumbo-build`](https://packages.gentoo.org/useflags/+jumbo-build)     Combine source files to speed up build process.
  [`+pdfium`](https://packages.gentoo.org/useflags/+pdfium)               Build the QtPdf module based on chromium\'s PDFium library
  [`+system-icu`](https://packages.gentoo.org/useflags/+system-icu)       Use the system-wide dev-libs/icu instead of bundled.
  [`+widgets`](https://packages.gentoo.org/useflags/+widgets)             Enable QtWidgets support
  [`accessibility`](https://packages.gentoo.org/useflags/accessibility)   Add support for accessibility (eg \'at-spi\' library)
  [`bindist`](https://packages.gentoo.org/useflags/bindist)               Flag to enable or disable options for prebuilt (GRP) packages (eg. due to licensing issues)
  [`custom-cflags`](https://packages.gentoo.org/useflags/custom-cflags)   Build with user-specified CFLAGS (unsupported)
  [`designer`](https://packages.gentoo.org/useflags/designer)             Install the QWebEngineView plugin used to add widgets in dev-qt/qttools\[designer\] forms that display web pages.
  [`geolocation`](https://packages.gentoo.org/useflags/geolocation)       Enable physical position determination
  [`kerberos`](https://packages.gentoo.org/useflags/kerberos)             Add kerberos support
  [`opengl`](https://packages.gentoo.org/useflags/opengl)                 Add support for OpenGL (3D graphics)
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)         Add sound server support via media-libs/libpulse (may be PulseAudio or PipeWire)
  [`qml`](https://packages.gentoo.org/useflags/qml)                       Build QML/QtQuick bindings and imports
  [`screencast`](https://packages.gentoo.org/useflags/screencast)         Enable support for remote desktop and screen cast using PipeWire
  [`test`](https://packages.gentoo.org/useflags/test)                     Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`vaapi`](https://packages.gentoo.org/useflags/vaapi)                   Enable Video Acceleration API for hardware decoding
  [`vulkan`](https://packages.gentoo.org/useflags/vulkan)                 Add support for 3D graphics and computing via the Vulkan cross-platform API
  [`webdriver`](https://packages.gentoo.org/useflags/webdriver)           Build tool for automated testing (ChromeDriver equivalent)
  ----------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-18 03:23] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]