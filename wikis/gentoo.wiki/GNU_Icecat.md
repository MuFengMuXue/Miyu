**Resources**

[[]][Home](https://www.gnu.org/software/gnuzilla/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/GNU_IceCat "wikipedia:GNU IceCat")

[[]][Bugs (upstream)](https://lists.gnu.org/mailman/listinfo/bug-gnuzilla)

[[]][[#icecat](ircs://irc.libera.chat/#icecat)] ([[webchat](https://web.libera.chat/#icecat)])

[[]][GitWeb](https://git.savannah.gnu.org/cgit/gnuzilla.git)

[![Icecat-gentoo-desktop.png](/images/thumb/8/86/Icecat-gentoo-desktop.png/300px-Icecat-gentoo-desktop.png)](https://wiki.gentoo.org/wiki/File:Icecat-gentoo-desktop.png)

[](https://wiki.gentoo.org/wiki/File:Icecat-gentoo-desktop.png "Enlarge")

GNU icecat is a web browser developed by the [GNU project](https://en.wikipedia.org/wiki/GNU "wikipedia:GNU") that is entirely [Free Software](https://en.wikipedia.org/wiki/Free_software "wikipedia:Free software"). The GNU project\'s goal is to make a web browser that doesn\'t load any proprietary software in any form, such as proprietary JavaScript, [Digital Rights Management](https://en.wikipedia.org/wiki/Digital_rights_management "wikipedia:Digital rights management") software and proprietary extensions.

Icecat is based on [Firefox](https://wiki.gentoo.org/wiki/Firefox "Firefox").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Removal]](#Removal)
-   [[3] [Features]](#Features)
    -   [[3.1] [Pre-installed addons]](#Pre-installed_addons)
        -   [[3.1.1] [GNU LibreJS]](#GNU_LibreJS)
        -   [[3.1.2] [Https-Everywhere]](#Https-Everywhere)
        -   [[3.1.3] [Other]](#Other)
-   [[4] [See also]](#See_also)

## [Installation]

### [USE flags]

** Note**\
These USE flags are for [[[www-client/firefox]](https://packages.gentoo.org/packages/www-client/firefox)[]], but they also apply for Icecat.

### [USE flags for] [www-client/firefox](https://packages.gentoo.org/packages/www-client/firefox) [[]] [Firefox Web Browser]

  ----------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+X`](https://packages.gentoo.org/useflags/+X)                               Add support for X11
  [`+clang`](https://packages.gentoo.org/useflags/+clang)                       Use Clang compiler instead of GCC
  [`+gmp-autoupdate`](https://packages.gentoo.org/useflags/+gmp-autoupdate)     Allow Gecko Media Plugins (binary blobs) to be automatically downloaded and kept up-to-date in user profiles
  [`+jumbo-build`](https://packages.gentoo.org/useflags/+jumbo-build)           Enable unified build - combines source files to speed up build process, but requires more memory
  [`+system-av1`](https://packages.gentoo.org/useflags/+system-av1)             Use the system-wide media-libs/dav1d and media-libs/libaom library instead of bundled
  [`+system-harfbuzz`](https://packages.gentoo.org/useflags/+system-harfbuzz)   Use the system-wide media-libs/harfbuzz instead of bundled and media-gfx/graphite2 in most cases
  [`+system-icu`](https://packages.gentoo.org/useflags/+system-icu)             Use the system-wide dev-libs/icu instead of bundled
  [`+system-jpeg`](https://packages.gentoo.org/useflags/+system-jpeg)           Use the system-wide media-libs/libjpeg-turbo instead of bundled
  [`+system-libevent`](https://packages.gentoo.org/useflags/+system-libevent)   Use the system-wide dev-libs/libevent instead of bundled
  [`+system-libvpx`](https://packages.gentoo.org/useflags/+system-libvpx)       Use the system-wide media-libs/libvpx instead of bundled
  [`+system-webp`](https://packages.gentoo.org/useflags/+system-webp)           Use the system-wide media-libs/libwebp instead of bundled
  [`+telemetry`](https://packages.gentoo.org/useflags/+telemetry)               Send anonymized usage information to upstream so they can better understand our users
  [`dbus`](https://packages.gentoo.org/useflags/dbus)                           Enable dbus support for anything that needs it (gpsd, gnomemeeting, etc)
  [`debug`](https://packages.gentoo.org/useflags/debug)                         Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`eme-free`](https://packages.gentoo.org/useflags/eme-free)                   Disable EME (DRM plugin) capability at build time
  [`gnome-shell`](https://packages.gentoo.org/useflags/gnome-shell)             Integrate with gnome-base/gnome-shell search
  [`hardened`](https://packages.gentoo.org/useflags/hardened)                   Activate default security enhancements for toolchain (gcc, glibc, binutils)
  [`hwaccel`](https://packages.gentoo.org/useflags/hwaccel)                     Force-enable hardware-accelerated rendering (Mozilla bug 594876)
  [`jack`](https://packages.gentoo.org/useflags/jack)                           Add support for the JACK Audio Connection Kit
  [`jpegxl`](https://packages.gentoo.org/useflags/jpegxl)                       Add JPEG XL image support (EXPERIMENTAL, no official upstream support)
  [`libproxy`](https://packages.gentoo.org/useflags/libproxy)                   Enable libproxy support
  [`openh264`](https://packages.gentoo.org/useflags/openh264)                   Use media-libs/openh264 for H264 support instead of downloading binary blob from Mozilla at runtime
  [`pgo`](https://packages.gentoo.org/useflags/pgo)                             Add support for profile-guided optimization for faster binaries - this option will double the compile time
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)               Add sound server support via media-libs/libpulse (may be PulseAudio or Pipewire, or apulse if installed)
  [`selinux`](https://packages.gentoo.org/useflags/selinux)                     !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`sndio`](https://packages.gentoo.org/useflags/sndio)                         Enable support for the media-sound/sndio backend
  [`system-pipewire`](https://packages.gentoo.org/useflags/system-pipewire)     Use system media-video/pipewire for WebRTC and screencast instead of bundled one
  [`system-png`](https://packages.gentoo.org/useflags/system-png)               Use the system-wide media-libs/libpng instead of bundled (requires APNG patches)
  [`test`](https://packages.gentoo.org/useflags/test)                           Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`valgrind`](https://packages.gentoo.org/useflags/valgrind)                   Enable annotations for accuracy. May slow down runtime slightly. Safe to use even if not currently using dev-debug/valgrind
  [`wasm-sandbox`](https://packages.gentoo.org/useflags/wasm-sandbox)           Sandbox certain third-party libraries through WebAssembly using RLBox
  [`wayland`](https://packages.gentoo.org/useflags/wayland)                     Enable dev-libs/wayland backend
  [`wifi`](https://packages.gentoo.org/useflags/wifi)                           Enable necko-wifi for NetworkManager integration, and access point MAC address scanning for better precision with opt-in geolocation services
  ----------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-24 09:10] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Icecat is available in the [parona-overlay overlay](https://gitlab.com/Parona/parona-overlay) repository.

Install [[[app-eselect/eselect-repository]](https://packages.gentoo.org/packages/app-eselect/eselect-repository)[]] and [[[dev-vcs/git]](https://packages.gentoo.org/packages/dev-vcs/git)[]]

`root `[`#`]`emerge --ask dev-vcs/git app-eselect/eselect-repository`

Enable **parona-overlay**:

`root `[`#`]`eselect repository enable parona-overlay`

Sync the repository:

`root `[`#`]`emerge --sync parona-overlay`

and finally, emerge icecat:

`root `[`#`]`emerge --ask www-client/icecat`

## [Removal]

To remove GNU Icecat:

`root `[`#`]`emerge --ask --depclean --verbose www-client/icecat`

To remove unused dependencies:

`root `[`#`]`emerge -c`

## [Features]

**privacy-preserving addons**

Many users are concerned about their privacy (tracking, bubbling, targeting, etc) while web browsing. This is a list of **Free** addons that might add extra level of privacy to their browsing.

The add-on menu can be accessed by navigating the following menus: [Hamburger button (top right under the X) → Add-ons]

### [Pre-installed addons]

#### [GNU LibreJS]

GNU LibreJS aims to address the JavaScript problem described in Richard Stallman\'s article [The JavaScript Trap](https://www.gnu.org/philosophy/javascript-trap.html). It blocks proprietary nontrivial JavaScript while allowing JavaScript that is free and/or trivial.

Mozilla Add-ons page: [https://addons.mozilla.org/en-US/firefox/addon/librejs/](https://addons.mozilla.org/en-US/firefox/addon/librejs/)

Git repository: [https://git.savannah.gnu.org/cgit/librejs.git/](https://git.savannah.gnu.org/cgit/librejs.git/)

Wikipedia: [https://en.wikipedia.org/wiki/GNU_LibreJS](https://en.wikipedia.org/wiki/GNU_LibreJS)

homepage: [https://www.gnu.org/software/librejs/](https://www.gnu.org/software/librejs/)

#### [Https-Everywhere]

This extension encrypts your communications with many major websites, making your browsing more secure. You can also enable https-only mode in the Icecat settings.

Mozilla Add-ons page: [https://addons.mozilla.org/en-US/firefox/addon/https-everywhere/](https://addons.mozilla.org/en-US/firefox/addon/https-everywhere/)

Git repository: [https://github.com/EFForg/https-everywhere](https://github.com/EFForg/https-everywhere)

Homepage: [https://eff.org/https-everywhere](https://eff.org/https-everywhere)

#### [Other]

The consequence of disabling proprietary JavaScript on most website is, that they tend to break. There are extensions that try to solve this issue with workarrounds that don\'t involve running proprietary software. These include:

-   **disable-polymer-youtube** - this extension disables the \"polymer\" framework that google introduced to youtube.com in 2017.
-   **LibreJS/USPS compatibility**
-   **LibrifyJS: libgen.me** - Libre replacement for JavaScript blocked by GNU LibreJS on libgen.me
-   **Reveal hidden HTML** - An add-on that is meant to fix CSS related bugs when blocking proprietary JavaScript.
-   **Searxes\' Third-party Request Blocker** - Prevent from connecting to a third-party resource without user consent.
-   **ViewTube** - Makes watching videos without proprietary JavaScript more convenient.
-   **Workarounds for nonfree JS**

## [See also]

-   [Firefox](https://wiki.gentoo.org/wiki/Firefox "Firefox") --- [open source](https://en.wikipedia.org/wiki/Open_source "wikipedia:Open source"), [multiplatform](https://en.wikipedia.org/wiki/Cross-platform_software "wikipedia:Cross-platform software"), [web browser](https://wiki.gentoo.org/wiki/Recommended_applications#Web_browsers "Recommended applications") developed by [Mozilla](https://en.wikipedia.org/wiki/Mozilla "wikipedia:Mozilla").