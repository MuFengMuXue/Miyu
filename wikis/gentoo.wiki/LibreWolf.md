**Resources**

[[]][Home](https://librewolf.net/)

[[]][Official documentation](https://librewolf.net/docs/faq)

[![Codeberg Logo](/images/thumb/c/cc/Codeberg-logo.png/30px-Codeberg-logo.png)][Codeberg](https://codeberg.org/librewolf/gentoo)

[[]][Bugs (upstream)](https://codeberg.org/librewolf/issues/issues)

**LibreWolf** is a fork of [Firefox](https://wiki.gentoo.org/wiki/Firefox "Firefox") which focuses on privacy and security. LibreWolf aims to be a private, secure, and freedom-expanding alternative browser. All telemetry, data collection, and annoyances of Firefox are removed.^[\[1\]](#cite_note-1)^

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Prerequisites]](#Prerequisites)
        -   [[1.1.1] [Install required software]](#Install_required_software)
        -   [[1.1.2] [Overlay]](#Overlay)
            -   [[1.1.2.1] [Eselect]](#Eselect)
            -   [[1.1.2.2] [Manual]](#Manual)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
    -   [[1.4] [Flatpak]](#Flatpak)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Running under Wayland]](#Running_under_Wayland)
    -   [[2.3] [Localization]](#Localization)
-   [[3] [Security]](#Security)
-   [[4] [Troubleshooting]](#Troubleshooting)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)
-   [[7] [References]](#References)

## [Installation]

### [Prerequisites]

The following must be installed in order for the rest of this article to work properly: [[[app-eselect/eselect-repository]](https://packages.gentoo.org/packages/app-eselect/eselect-repository)[]] and [[[dev-vcs/git]](https://packages.gentoo.org/packages/dev-vcs/git)[]].

Skip this if they are already installed.

#### [Install required software]

`root `[`#`]`emerge --ask app-eselect/eselect-repository dev-vcs/git`

#### [Overlay]

LibreWolf is not packaged in the main Gentoo repository, but an [official overlay is available](https://librewolf.net/installation/gentoo/).

##### [Eselect]

Using [eselect repository](https://wiki.gentoo.org/wiki/Eselect/Repository "Eselect/Repository"), run this command to add the overlay:

`root `[`#`]`eselect repository add librewolf git `[`https://codeberg.org/librewolf/gentoo.git`](https://codeberg.org/librewolf/gentoo.git)

And then synchronize the repository:

`root `[`#`]`emaint sync -r librewolf`

##### [Manual]

Create a new repository file in [/etc/portage/repos.conf]:

[FILE] **`/etc/portage/repos.conf/librewolf.conf`**

    [librewolf]
    priority = 50
    location = /var/db/repos/librewolf
    sync-type = git
    sync-uri = https://codeberg.org/librewolf/gentoo.git
    auto-sync = Yes

And then synchronize the repository:

`root `[`#`]`emaint sync -r librewolf`

### [USE flags]

The Gentoo [[[www-client/firefox]](https://packages.gentoo.org/packages/www-client/firefox)[]] `USE` flags are listed below, but still apply to [www-client/librewolf](https://codeberg.org/librewolf/gentoo/src/branch/master/www-client/librewolf):

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

** Important**\
For localization support, review [Localization](https://wiki.gentoo.org/wiki/Librewolf#Localization "Librewolf") before emerging. Changing the localization requires a full recompilation of the package, so it\'s important to get it right the first time.

Assuming the [overlay is properly installed,](https://wiki.gentoo.org/wiki/Librewolf#Overlay "Librewolf") use [emerge] to install [www-client/librewolf](https://codeberg.org/librewolf/gentoo/src/branch/master/www-client/librewolf):

`root `[`#`]`emerge --ask www-client/librewolf`

Alternatively, user who wish to avoid compiling may install the precompiled package instead.

`root `[`#`]`emerge --ask www-client/librewolf-bin`

### [Flatpak]

LibreWolf is also available on Flathub. If you prefer to install LibreWolf as a Flatpak, follow the install instructions from the [Flatpak](https://wiki.gentoo.org/wiki/Flatpak "Flatpak") wiki article including adding the Flathub repository. Then run this command:

`user `[`$`]`flatpak install --user io.gitlab.librewolf-community`

## [Configuration]

Since LibreWolf is based on Firefox, most of the configuration options in [Firefox](https://wiki.gentoo.org/wiki/Firefox#Configuration "Firefox") apply.

### [Files]

-   [\$HOME/.librewolf] - Main configuration directory.

### [Running under Wayland]

Recent versions of LibreWolf run on [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland") by default if the `wayland` `USE` flag is set. To verify this, see the `Window Support` field under `about:support`.

In the case that this doesn\'t work, see [Firefox](https://wiki.gentoo.org/wiki/Firefox#Running_under_Wayland "Firefox") for forcing Wayland support.

### [Localization]

[www-client/librewolf](https://codeberg.org/librewolf/gentoo/src/branch/master/www-client/librewolf) respects the `L10N` variable. See the [L10N in the localization guide](https://wiki.gentoo.org/wiki/Localization/Guide#L10N "Localization/Guide").

## [Security]

LibreWolf is hardened by default and includes [uBlock Origin](https://en.wikipedia.org/wiki/UBlock_Origin)^[\[2\]](#cite_note-2)^. See the [LibreWolf Documentation](https://librewolf.net/docs/addons/) for a recommended list of add-ons and which ones to avoid.

## [Troubleshooting]

See the official [LibreWolf FAQ](https://librewolf.net/docs/faq/) for LibreWolf-specific issues.

The LibreWolf Gentoo overlay is based off of the official Firefox overlay^[\[3\]](#cite_note-3)^, and will inherit any issues that also affect [[[www-firefox]](https://packages.gentoo.org/packages/www-firefox)[]]. Check out [Firefox](https://wiki.gentoo.org/wiki/Firefox#Troubleshooting "Firefox") for details.

## [See also]

-   [Firefox](https://wiki.gentoo.org/wiki/Firefox "Firefox") --- [open source](https://en.wikipedia.org/wiki/Open_source "wikipedia:Open source"), [multiplatform](https://en.wikipedia.org/wiki/Cross-platform_software "wikipedia:Cross-platform software"), [web browser](https://wiki.gentoo.org/wiki/Recommended_applications#Web_browsers "Recommended applications") developed by [Mozilla](https://en.wikipedia.org/wiki/Mozilla "wikipedia:Mozilla").

## [External resources]

-   [LibreWolf Website](https://librewolf.net) - The LibreWolf main site.
-   [LibreWolf FAQ](https://librewolf.net/docs/faq) - Frequently Asked Questions about LibreWolf.
-   [LibreWolf Gentoo installation](https://librewolf.net/installation/gentoo/) - The LibreWolf installation for Gentoo Linux.
-   [LibreWolf Gentoo overlay](https://codeberg.org/librewolf/gentoo) - The official LibreWolf overlay for Gentoo Linux.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://web.archive.org/web/20220105084629/https://librewolf.net/#what-is-librewolf](https://web.archive.org/web/20220105084629/https://librewolf.net/#what-is-librewolf)]]
2.  [[[↑](#cite_ref-2)] [[https://librewolf.net/#main-features](https://librewolf.net/#main-features)]]
3.  [[[↑](#cite_ref-3)] [[https://codeberg.org/librewolf/gentoo#packaging-workflow](https://codeberg.org/librewolf/gentoo#packaging-workflow)]]