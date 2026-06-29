This page contains [[changes](https://wiki.gentoo.org/index.php?title=Firefox&diff=1434020)] which are not marked for translation.

\

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Mozilla "Project:Mozilla")][Project](https://wiki.gentoo.org/wiki/Project:Mozilla "Project:Mozilla")

[[]][Home](https://www.mozilla.org/en-US/firefox/new/)

[[]][Firefox ESR](https://www.mozilla.org/en-US/firefox/organizations/)

[[]][Package information](https://packages.gentoo.org/packages/www-client/firefox)

[[]][Binary package information](https://packages.gentoo.org/packages/www-client/firefox-bin)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Mozilla_Firefox "wikipedia:Mozilla Firefox")

[[]][GitWeb](https://hg.mozilla.org/mozilla-central/)

[[]][Upstream wiki](https://wiki.mozilla.org/Main_Page)

[[]][Bugs (upstream)](https://bugzilla.mozilla.org/)

[[]][[#firefox](ircs://irc.libera.chat/#firefox)] ([[webchat](https://web.libera.chat/#firefox)])

**Firefox** is an [open source](https://en.wikipedia.org/wiki/Open_source "wikipedia:Open source"), [multiplatform](https://en.wikipedia.org/wiki/Cross-platform_software "wikipedia:Cross-platform software"), [web browser](https://wiki.gentoo.org/wiki/Recommended_applications#Web_browsers "Recommended applications") developed by [Mozilla](https://en.wikipedia.org/wiki/Mozilla "wikipedia:Mozilla").

Firefox has decades-old roots in [Netscape](https://en.wikipedia.org/wiki/Firefox#History "wikipedia:Firefox") and serves as a [foundation for other projects](https://wiki.gentoo.org/wiki/Firefox#Firefox_forked_projects "Firefox"), such as [GNU Icecat](https://wiki.gentoo.org/wiki/GNU_Icecat "GNU Icecat") or [LibreWolf](https://wiki.gentoo.org/wiki/LibreWolf "LibreWolf").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
        -   [[1.1.1] [www-client/firefox]](#www-client.2Ffirefox)
        -   [[1.1.2] [www-client/firefox-bin]](#www-client.2Ffirefox-bin)
    -   [[1.2] [Emerge]](#Emerge)
        -   [[1.2.1] [www-client/firefox-bin (binary package)]](#www-client.2Ffirefox-bin_.28binary_package.29)
        -   [[1.2.2] [www-client/firefox (source package)]](#www-client.2Ffirefox_.28source_package.29)
        -   [[1.2.3] [Specify a slot]](#Specify_a_slot)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Fonts]](#Fonts)
        -   [[2.1.1] [Via the \"Settings\" UI]](#Via_the_.22Settings.22_UI)
        -   [[2.1.2] [Via about:config]](#Via_about:config)
    -   [[2.2] [Running under Wayland]](#Running_under_Wayland)
    -   [[2.3] [Enabling multitouch]](#Enabling_multitouch)
        -   [[2.3.1] [Xinput2 scrolling]](#Xinput2_scrolling)
        -   [[2.3.2] [Multitouch zoom]](#Multitouch_zoom)
    -   [[2.4] [Middle mouse scroll (autoscroll)]](#Middle_mouse_scroll_.28autoscroll.29)
    -   [[2.5] [Bigger scrolling regions for Up/Down]](#Bigger_scrolling_regions_for_Up.2FDown)
    -   [[2.6] [Threads]](#Threads)
    -   [[2.7] [Audio backend]](#Audio_backend)
    -   [[2.8] [Disabling percent-encoding]](#Disabling_percent-encoding)
    -   [[2.9] [Disable enforced digital signatures verification in Firefox \>=48]](#Disable_enforced_digital_signatures_verification_in_Firefox_.3E.3D48)
        -   [[2.9.1] [Method 1]](#Method_1)
        -   [[2.9.2] [Method 2]](#Method_2)
    -   [[2.10] [Special URLs]](#Special_URLs)
    -   [[2.11] [XDG integration]](#XDG_integration)
    -   [[2.12] [Running under KDE]](#Running_under_KDE)
    -   [[2.13] [Enabling color management]](#Enabling_color_management)
    -   [[2.14] [Disabling Privacy-Preserving Attribution]](#Disabling_Privacy-Preserving_Attribution)
    -   [[2.15] [Disabling AI Chatbots]](#Disabling_AI_Chatbots)
    -   [[2.16] [Hiding certain entries in the context menu]](#Hiding_certain_entries_in_the_context_menu)
-   [[3] [Security]](#Security)
    -   [[3.1] [Running in sandbox]](#Running_in_sandbox)
    -   [[3.2] [SSL/TLS security enhancements]](#SSL.2FTLS_security_enhancements)
        -   [[3.2.1] [Deprecated options]](#Deprecated_options)
    -   [[3.3] [Safer browsing with add-ons]](#Safer_browsing_with_add-ons)
        -   [[3.3.1] [uBlock Origin]](#uBlock_Origin)
        -   [[3.3.2] [AdNauseam]](#AdNauseam)
        -   [[3.3.3] [LibRedirect]](#LibRedirect)
        -   [[3.3.4] [Facebook Container]](#Facebook_Container)
        -   [[3.3.5] [NoScript]](#NoScript)
        -   [[3.3.6] [Video speed controller]](#Video_speed_controller)
        -   [[3.3.7] [Behind The Overlay]](#Behind_The_Overlay)
    -   [[3.4] [Policies]](#Policies)
    -   [[3.5] [Local certificates]](#Local_certificates)
-   [[4] [Hardware acceleration]](#Hardware_acceleration)
    -   [[4.1] [Troubleshooting]](#Troubleshooting)
        -   [[4.1.1] [Disable hardware acceleration]](#Disable_hardware_acceleration)
        -   [[4.1.2] [Green artifacts on a video only with hardware acceleration]](#Green_artifacts_on_a_video_only_with_hardware_acceleration)
        -   [[4.1.3] [Hardware acceleration not working]](#Hardware_acceleration_not_working)
        -   [[4.1.4] [Hardware acceleration not working within a sandbox]](#Hardware_acceleration_not_working_within_a_sandbox)
-   [[5] [Troubleshooting]](#Troubleshooting_2)
    -   [[5.1] [No video with supported format and MIME type found]](#No_video_with_supported_format_and_MIME_type_found)
    -   [[5.2] [Audio]](#Audio)
        -   [[5.2.1] [Lack of sound (www-client/firefox-bin)]](#Lack_of_sound_.28www-client.2Ffirefox-bin.29)
        -   [[5.2.2] [Lack of sound when using PipeWire (www-client/firefox)]](#Lack_of_sound_when_using_PipeWire_.28www-client.2Ffirefox.29)
        -   [[5.2.3] [Sound crackling when using Pipewire or JACK (www-client/firefox)]](#Sound_crackling_when_using_Pipewire_or_JACK_.28www-client.2Ffirefox.29)
    -   [[5.3] [Crashes]](#Crashes)
    -   [[5.4] [Graphics/video]](#Graphics.2Fvideo)
        -   [[5.4.1] [Green video screen (YouTube)]](#Green_video_screen_.28YouTube.29)
        -   [[5.4.2] [Screen tearing / stuttering smooth scrolling]](#Screen_tearing_.2F_stuttering_smooth_scrolling)
    -   [[5.5] [gtk+:3 pulls in D-Bus]](#gtk.2B:3_pulls_in_D-Bus)
    -   [[5.6] [KDE Plasma Integration: failed to connect to the native host]](#KDE_Plasma_Integration:_failed_to_connect_to_the_native_host)
    -   [[5.7] [Speech dispatcher library missing]](#Speech_dispatcher_library_missing)
    -   [[5.8] [Wayland]](#Wayland)
        -   [[5.8.1] [Determine if Firefox is running the Wayland protocol backend]](#Determine_if_Firefox_is_running_the_Wayland_protocol_backend)
        -   [[5.8.2] [\"Failed to load cursor theme Adwaita\" in Wayland]](#.22Failed_to_load_cursor_theme_Adwaita.22_in_Wayland)
        -   [[5.8.3] [Touchpad scrolling feels too fast on Wayland]](#Touchpad_scrolling_feels_too_fast_on_Wayland)
    -   [[5.9] [Windows decorations missing in Fluxbox since FF-91.3.0]](#Windows_decorations_missing_in_Fluxbox_since_FF-91.3.0)
-   [[6] [Troubleshooting tips]](#Troubleshooting_tips)
    -   [[6.1] [Safe mode]](#Safe_mode)
    -   [[6.2] [Startup cache]](#Startup_cache)
    -   [[6.3] [Reset profile]](#Reset_profile)
-   [[7] [Firefox forked projects]](#Firefox_forked_projects)
-   [[8] [See also]](#See_also)
-   [[9] [External resources]](#External_resources)
-   [[10] [References]](#References)

## [Installation]

### [USE flags]

#### [][www-client/firefox]

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

The above list of USE flags is not comprehensive. [equery](https://wiki.gentoo.org/wiki/Equery "Equery") can be used if a full list is required:

`user `[`$`]`equery uses www-client/firefox`

Firefox is one package that is often compiled with [LLVM](https://wiki.gentoo.org/wiki/LLVM "LLVM"), notably by Mozilla itself, which ensures this as a well-tested path. Using [Clang](https://wiki.gentoo.org/wiki/LLVM/Clang "LLVM/Clang") to compile Firefox (by keeping the [[[clang]](https://packages.gentoo.org/useflags/clang)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag) could allow cross language optimizaton^[\[1\]](#cite_note-1)^ because Firefox mixes [C](https://wiki.gentoo.org/wiki/C "C") and [C++](https://wiki.gentoo.org/wiki/C%2B%2B "C++") code with [Rust](https://wiki.gentoo.org/wiki/Rust "Rust") code^[\[2\]](#cite_note-2)^. Compiling with [GCC](https://wiki.gentoo.org/wiki/GCC "GCC") ([[[-clang]](https://packages.gentoo.org/useflags/clang)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")]) is also supported, and there is some [analysis](https://wiki.gentoo.org/wiki/Project:Mozilla/Firefox_Benchmarks_2025_Q1 "Project:Mozilla/Firefox Benchmarks 2025 Q1") of potential small differences between each choice.

Note that `USE="-pulseaudio"` will select the ALSA audio back-end.

#### [][www-client/firefox-bin]

### [USE flags for] [www-client/firefox-bin](https://packages.gentoo.org/packages/www-client/firefox-bin) [[]] [Firefox Web Browser]

  --------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`+gmp-autoupdate`](https://packages.gentoo.org/useflags/+gmp-autoupdate)   Allow Gecko Media Plugins (binary blobs) to be automatically downloaded and kept up-to-date in user profiles
  [`selinux`](https://packages.gentoo.org/useflags/selinux)                   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`wayland`](https://packages.gentoo.org/useflags/wayland)                   Enable dev-libs/wayland backend
  --------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-22 08:04] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

** Tip**\
Firefox takes a relatively long time to compile. Unless there is a specific reason not to (such as the need for non-default [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag")), [using firefox-bin](https://wiki.gentoo.org/wiki/Firefox#www-client.2Ffirefox-bin_.28binary_package.29 "Firefox") can save a lot of installation time ([details](https://wiki.gentoo.org/wiki/Minimizing_compilation_and_installation_time#Alternative_binary_packages_.28.22-bin.22_packages.29 "Minimizing compilation and installation time")). There are also binary packages for Firefox available on the official [Gentoo binary host](https://wiki.gentoo.org/wiki/Gentoo_Binary_Host_Quickstart "Gentoo Binary Host Quickstart").

Gentoo Firefox packages are available both for the *Rapid Release* and *Extended Support Release (ESR)* Firefox update channels. To choose a specific Firefox update channel, see the [specify a slot section](https://wiki.gentoo.org/wiki/Firefox#Specify_a_slot "Firefox"). For information about Firefox releases, see [choosing a Firefox update channel](https://support.mozilla.org/en-US/kb/choosing-firefox-update-channel).

#### [][[] www-client/firefox-bin (binary package)]

[[[www-client/firefox-bin]](https://packages.gentoo.org/packages/www-client/firefox-bin)[]] provides an optimized binary build of Firefox, by Mozilla. This will install much quicker than [[[www-client/firefox]](https://packages.gentoo.org/packages/www-client/firefox)[]] but offers less compile-time configuration options.

To emerge [[[www-client/firefox-bin]](https://packages.gentoo.org/packages/www-client/firefox-bin)[]]:

`root `[`#`]`emerge --ask www-client/firefox-bin`

#### [][www-client/firefox (source package)]

** Tip**\
Enabling LTO (Link Time Optimization) can provide a measurable performance increase for Firefox specifically^[\[3\]](#cite_note-3)^, at the expense of longer compile times (note that whether these differences are perceptible to the user or not is debatable^[\[4\]](#cite_note-4)^). The LTO article has instructions on [how to enable LTO for a specific package](https://wiki.gentoo.org/wiki/LTO#Enabling_LTO_per_package "LTO").

To install Firefox from source:

`root `[`#`]`emerge --ask www-client/firefox`

This will install Firefox Extended Support Release (ESR) on a stable branch Gentoo system (or Firefox \"Rapid release\" if \~amd64 keyword is selected).

#### [[] Specify a slot]

This will explain how to select a Firefox package from a specific slot.

To select a release irrespective of keywords, subscribe to a slot:

`root `[`#`]`emerge --ask www-client/firefox:esr`

Or:

`root `[`#`]`emerge --ask www-client/firefox:rapid`

This will add the package from a specific slot to the [selected set](https://wiki.gentoo.org/wiki/Selected-packages_set_(Portage) "Selected-packages set (Portage)") ([/var/lib/portage/world]). [Read more about the motivation of slotting](https://wiki.gentoo.org/wiki/Project:Mozilla#Benefits_and_disadvantages_of_the_slotting_system "Project:Mozilla").

** Note**\
If a slot for Firefox has been previously selected, start by using `--deselect` to remove the entry from the [world] file:

`root `[`#`]`emerge --deselect www-client/firefox:esr `

`root `[`#`]`emerge -av www-client/firefox:rapid`

## [Configuration]

### [Fonts]

The fonts used by Firefox to display Web pages can be specified via the \"Settings\" UI, or via [about:config].

#### [][Via the \"Settings\" UI]

From the menu bar, select \"Edit\" -\> \"Settings\", or visit [about:preferences#general], and scroll down for the \"Fonts\" section.

There, specify the default font and the default size for that font, or select \"Advanced\" for a more fine-grained approach.

The \"Advanced\" dialog allows one to select a writing system (e.g. Latin, Simplified Chinese, Devanagari, etc.) and the fonts to be used for that writing system when a Web page needs to use a certain class of typeface: proportional, serif, sans-serif, or monospace. The minimum font size can be specified, as well as the default size for proportional and monospace fonts.

#### [Via [about:config]]

Search for `font.name`; this will list all settings available in the `font.name` and `font.name-list` namespaces.

### [Running under Wayland]

** Note**\
In [[[www-client/firefox]](https://packages.gentoo.org/packages/www-client/firefox)[]] and [[[www-client/firefox-bin]](https://packages.gentoo.org/packages/www-client/firefox-bin)[]], Wayland will be enabled by default if the `wayland` `USE` flag is set. These instructions are kept in case that still fails.

Since Firefox 65, it is possible to run Firefox natively under [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland") by launching it with the `GDK_BACKEND=wayland` environment variable set after having emerged Firefox with the *USE* flag `wayland` enabled. From a terminal:

`user `[`$`]`GDK_BACKEND="wayland" firefox`

Also, make sure that the generic Wayland environment variables `XDG_RUNTIME_DIR`, `WAYLAND_DISPLAY`, and `XDG_SESSION_TYPE` are exported correctly to ensure that GDK can communicate with the compositor.

To set Firefox to always open using the Wayland backend, set the following environment variable in the user\'s shell. Bash is the default user shell on Gentoo systems:

[FILE] **`~/.bash_profile`**

    # Enable Wayland support for Mozilla Firefox
    export MOZ_ENABLE_WAYLAND=1

### [Enabling multitouch]

#### [Xinput2 scrolling]

This brings touch scrolling and multitouch support for Firefox:

`MOZ_USE_XINPUT2` [environment variable](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/EnvVar "Handbook:AMD64/Working/EnvVar") has to be set to a value of `1` in [/etc/env.d/80firefox], or just before launching [firefox] in a shell. for example:

`user `[`$`]`MOZ_USE_XINPUT2="1" firefox`

This also *eliminates* the predefined *scroll step size* for touchpad scrolling! All scrolling will be *really* smooth.

Wacom tablets/touchscreens may need [extra configuration](https://wiki.gentoo.org/wiki/Wacom#Xinput2_multitouch "Wacom") so they emit true touch events for [Xorg](https://wiki.gentoo.org/wiki/Xorg "Xorg").

#### [Multitouch zoom]

This only works when the multitouch events reach Firefox, therefore the `Xinput2` activation above has to be done first.

  ----------------------- --------------------------------------- -----------------------
  Description             about:config option                     Value
  Multitouch activation   `gestures.enable_single_finger_input`   `False`
  Zoom in                 `browser.gesture.pinch.in`              `cmd_fullZoomReduce`
  Zoom out                `browser.gesture.pinch.out`             `cmd_fullZoomEnlarge`
  ----------------------- --------------------------------------- -----------------------

### [][Middle mouse scroll (autoscroll)]

Traditionally in Linux, the middle mouse button is used to paste the currently selected (highlighted) text into a text field. On Windows systems, the middle mouse button in Firefox is used for click-and-drag scrolling up and down the page. This functionality can be enabled in Firefox by opening `about:config` and setting `general.autoScroll = true` value^[\[5\]](#cite_note-5)^:

Middle click-and-drag scrolling should now be enabled.

Although not necessary, sometimes it is desirable to disable all other middle-click functionality within Firefox when using click-and-drag scrolling. Open `about:config` and set the following values to disable middle-click functionality:

-   `middlemouse.contentLoadURL = false`
-   `middlemouse.openNewWindow = false`
-   `middlemouse.paste = false`

### [][Bigger scrolling regions for Up/Down]

PageUp/PageDown scroll for a page, Up/Down scroll for a line, many will benefit if Up/Down would scroll for a few lines:

  -------------------------------------------------------- -------------------------------------------- -------
  Description                                              about:config option                          Value
  Vertical scroll distance, not for mouse (default is 3)   `toolkit.scrollbox.verticalScrollDistance`   `30`
  -------------------------------------------------------- -------------------------------------------- -------

To increase scrolling size for a mouse also:

  ----------------------------------------------------------------- ------------------------------------- -------
  Description                                                       about:config option                   Value
  Vertical scroll distance, for mouse and keyboard (default is 1)   `mousewheel.min_line_scroll_amount`   `N`
  ----------------------------------------------------------------- ------------------------------------- -------

### [Threads]

Firefox \>= 54 \< 66 has 4 threads enabled by default^[\[6\]](#cite_note-6)^. Firefox \>= 97 also has fission site isolation enabled by default^[\[7\]](#cite_note-7)^. Adjusting threads now does nothing with fission enabled and the UI option for changing the number of threads is also gone when fission is enabled^[\[8\]](#cite_note-8)^, Number of process per-site^[\[9\]](#cite_note-9)^ can be adjusted by modifying the corresponding option in the `about:config` interface:

  ----------------------------------------- ------------------------------------ -------
  Description                               about:config option                  Value
  Increase the threads                      `dom.ipc.processCount`               `N`
  Increase the Number of process per-site   `dom.ipc.processCount.webisolated`   `N`
  ----------------------------------------- ------------------------------------ -------

Where `N` is an integer number.

### [Audio backend]

Firefox\'s cubeb audio library supports a number of different backends.^[\[10\]](#cite_note-10)[\[11\]](#cite_note-11)^ A backend can be specified by creating and setting `media.cubeb.backend` in about:config. A selection of available backends is listed below; the \'Value\' column indicates the appropriate value for `media.cubeb.backend`, and the \'Status\' column indicates the current level of support for that backend:

-   Tier-1: Actively maintained. Should have CI coverage. Critical for Firefox.
-   Tier-2: Actively maintained by contributors. CI coverage appreciated.
-   Tier-3: Maintainers/patches accepted. Status unclear.
-   Tier-4: Deprecated, obsolete. Scheduled to be removed.

  ------------------- -------- --------------
  Description         Status   Value
  ALSA                Tier-3   `alsa`
  JACK                Tier-3   `jack`
  OSS                 Tier-2   `oss`
  PulseAudio (C)      Tier-4   `pulse`
  PulseAudio (Rust)   Tier-1   `pulse-rust`
  sndio               Tier-2   `sndio`
  ------------------- -------- --------------

Obviously, to use Firefox with JACK, [[[www-client/firefox]](https://packages.gentoo.org/packages/www-client/firefox)[]] should be installed with the USE flag [[[jack]](https://packages.gentoo.org/useflags/jack)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] enabled.

### [Disabling percent-encoding]

Normally, URLs that are copied from the address bar get [percent-encoded](https://en.wikipedia.org/wiki/Percent-encoding "wikipedia:Percent-encoding"). This may cause an annoyance when certain non-Latin symbols (such as Cyrillic) get encoded, as they become unreadable to humans.

To disable percent-encoding when copying from the address bar, set the `about:config` option `network.standard-url.escape-utf8` to `false`.

** Note**\
Unfortunately Firefox does not support non-Latin symbols in anchors, those remain encoded (not percent-encoded, though).

### [][Disable enforced digital signatures verification in Firefox \>=48]

This concerns mandatory [add-ons signature](https://wiki.mozilla.org/Add-ons/Extension_Signing) in Firefox and can lead to security issues.

#### [Method 1]

Create this file:

[FILE] **`/usr/lib/firefox/config.js`**

    //
    try )
        .eval("SIGNED_TYPES.clear()");
    }
    catch(ex)
    END

Then insert this:

[FILE] **`/usr/lib/firefox/defaults/pref/channel-prefs.js`**

    pref("general.config.obscure_value", 0);
    pref("general.config.filename", "config.js");

#### [Method 2]

[https://gist.github.com/anonymous/a661949550a26b9522f79095f8ae2d94](https://gist.github.com/anonymous/a661949550a26b9522f79095f8ae2d94)

### [Special URLs]

Firefox includes a few dozen special URLs that can be helpful in determining more information about various Firefox settings. These URLs can be entered into the Super Bar (via copy and paste) to view the special pages. A few of the more significant ones include:

-   `about:addons` - Page for managing extensions.
-   `about:buildconfig` - Page containing build information about the currently running version of Firefox. Use this page to check what compiler flags were set during Firefox\'s build.
-   `about:cache` - Information about the Network Cache Storage Service.
-   `about:config` - Modify internal browser settings and preferences.
-   `about:memory` - Measure and show memory reports, free memory, etc.
-   `about:networking` - Analyze current network information such as HTTP, socket, and DNS connections.
-   `about:plugins` - List installed plugins such as Widevine Content Decryption Module (DRM software).
-   `about:support` - A page containing technical information that might be useful when trying to solve a problem. Includes information on WebGL, Window Protocol (X11 or Wayland), and compositing graphics backends.
-   `about:telemetry`

Finally, `about:about` will display the whole list of Firefox\' "about" pages. A description for each page is available at [Firefox and the \"about\" protocol](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/The_about_protocol).

See also [Firefox chrome:// document URLs](https://superuser.com/questions/392471/firefox-chrome-document-urls).

### [XDG integration]

In order to make Firefox use [XDG file associations](https://wiki.gentoo.org/wiki/Default_applications#Setting_the_default_application_via_mimeapps.list_files "Default applications") set Content Type\'s Action to [/usr/bin/xdg-open].

To ensure Firefox is being used by other applications for handling HTTP and HTTPS links, run the following command:

`user `[`$`]`xdg-mime default firefox.desktop x-scheme-handler/http x-scheme-handler/https text/html`

### [Running under KDE]

Firefox is built with GTK, and by default will use the GTK file picker. To enable the KDE file picker, install [[[kde-plasma/xdg-desktop-portal-kde]](https://packages.gentoo.org/packages/kde-plasma/xdg-desktop-portal-kde)[]], which is installed by default if [[[kde-plasma/plasma-meta]](https://packages.gentoo.org/packages/kde-plasma/plasma-meta)[]] is installed. After that set `widget.use-xdg-desktop-portal` to `true` and `widget.use-xdg-desktop-portal.file-picker` to `1` in `about:config`.

### [Enabling color management]

See the dedicated [Color management section](https://wiki.gentoo.org/wiki/Color_management#Firefox "Color management").

### [Disabling Privacy-Preserving Attribution]

To disable the Privacy-Preserving Attribution API added in version 128,^[\[12\]](#cite_note-12)[\[13\]](#cite_note-13)[\[14\]](#cite_note-14)^ set `dom.private-attribution.submission.enabled` to false.^[\[15\]](#cite_note-15)^ Or compile Firefox with `-telemetry` use flag.

### [Disabling AI Chatbots]

To disable the AI Chatbot sidebar feature added since version 130,^[\[16\]](#cite_note-16)[\[17\]](#cite_note-17)^ set `browser.ml.chat.enabled` to false.^[\[18\]](#cite_note-18)^

### [Hiding certain entries in the context menu]

Although the Firefox UI doesn\'t directly allow users to hide certain entries in the context menu / \'right-click\' menu, it\'s possible to do so via the [userChrome.css] stylesheet. Refer to [this Reddit post](https://www.reddit.com/r/firefox/comments/1eoo6k7/firefox_context_menu/) for details.

## [Security]

### [Running in sandbox]

It is highly recommended to run your browser inside a sandbox, to limit its access to e.g. your home directory. There are many alternative sandboxing applications with this functionality to choose from.

-   [[[sys-apps/apparmor]](https://packages.gentoo.org/packages/sys-apps/apparmor)[]]
-   [[[sec-policy/selinux-mozilla]](https://packages.gentoo.org/packages/sec-policy/selinux-mozilla)[]] (SELinux)
-   [[[sys-apps/bubblewrap]](https://packages.gentoo.org/packages/sys-apps/bubblewrap)[]]
-   [[[sys-apps/firejail]](https://packages.gentoo.org/packages/sys-apps/firejail)[]]

Please see [Simple sandbox](https://wiki.gentoo.org/wiki/Simple_sandbox "Simple sandbox") for suggestions on sandboxing Firefox.

### [][SSL/TLS security enhancements]

Some `about:config` SSL/TLS security options (as of Firefox 149) which increase the security of HTTPS connections are listed below.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------- ---------
  Description                                                                                                                                                                                         about:config option                                 Value
  Minimum TLS version set to [1.2](https://en.wikipedia.org/wiki/Transport_Layer_Security#TLS_1.2 "wikipedia:Transport Layer Security"). *Changing to 4 may break access to some websites.*   `security.tls.version.min`                          `3`
  Avoiding old SSL/TLS version. *May break access to some badly configured websites.*                                                                                                                 `security.ssl.require_safe_negotiation`             `true`
  Inform user about insecure SSL/TLS negotiation (broken padlock).                                                                                                                                    `security.ssl.treat_unsafe_negotiation_as_broken`   `true`
  Require [Online Certificate Status Protocol](https://en.wikipedia.org/wiki/Online_Certificate_Status_Protocol "wikipedia:Online Certificate Status Protocol"). Introduces some latency.     `security.OCSP.require`                             `true`
  Strict [Certificate Pinning](https://en.wikipedia.org/wiki/HTTP_Public_Key_Pinning "wikipedia:HTTP Public Key Pinning").                                                                    `security.cert_pinning.enforcement_level`           `2`
  No Google [SSL False Start](https://en.wikipedia.org/wiki/TLS_False_Start#Downgrade_attacks:_FREAK_attack_and_Logjam_attack "wikipedia:TLS False Start").                                   `security.ssl.enable_false_start`                   `false`
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------- ---------

#### [Deprecated options]

These were present in older versions of Firefox.

  ------------------------------------------------------------------------------------------------------------------------ ---------------------------------- ---------
  Description                                                                                                              about:config option                Value
  Don\'t use [DES](https://en.wikipedia.org/wiki/Data_Encryption_Standard "wikipedia:Data Encryption Standard").   `security.ssl3.rsa_des_ede3_sha`   `false`
  Don\'t use [RC4](https://en.wikipedia.org/wiki/RC4 "wikipedia:RC4").                                             `security.ssl3.rsa_rc4_128_md5`    `false`
  Don\'t use RC4.                                                                                                          `security.ssl3.rsa_rc4_128_sha`    `false`
  ------------------------------------------------------------------------------------------------------------------------ ---------------------------------- ---------

### [Safer browsing with add-ons]

Many users are concerned about their privacy (tracking, bubbling, targeting, etc) while web browsing. Installing Add-ons can aid in adding an extra level of privacy to their browsing.

The add-on menu can be accessed by navigating the following menus: [Hamburger button (top right under the X) → Add-ons]

** Note**\
Occasionally certain add-ons will use key press event listeners for input from the user. FireFox\'s \"Search for text when I start typing\" feature can conflict with key press event listeners used by add-ons. This feature can be disabled by navigating to [Hamburger button (top right under the X) → Preferences → Browsing] and unchecking the \"Search for text when I start typing\" option.

#### [uBlock Origin]

uBlock Origin is \"a wide-spectrum content blocker with CPU and memory efficiency as a primary feature\".^[\[19\]](#cite_note-19)^ It enables 5 filter lists by default and others are available.

-   Mozilla Add-ons page: [https://addons.mozilla.org/en/firefox/addon/ublock-origin/](https://addons.mozilla.org/en/firefox/addon/ublock-origin/)
-   GitHub: [https://github.com/gorhill/uBlock](https://github.com/gorhill/uBlock)
-   Wikipedia: [https://en.wikipedia.org/wiki/uBlock_Origin](https://en.wikipedia.org/wiki/uBlock_Origin)

#### [AdNauseam]

AdNauseam provides the same functionality as uBlock Origin but also \"quietly clicks on every blocked ad\"^[\[20\]](#cite_note-20)^ with the goal of resisting ad network tracking efforts through obfuscation. Some research in 2021 showed it to be effective for individual users.^[\[21\]](#cite_note-21)^

-   Mozilla Add-ons page: [https://addons.mozilla.org/en-GB/firefox/addon/adnauseam/](https://addons.mozilla.org/en-GB/firefox/addon/adnauseam/)
-   Homepage: [https://adnauseam.io/](https://adnauseam.io/)
-   GitHub: [https://github.com/dhowe/AdNauseam](https://github.com/dhowe/AdNauseam)

#### [LibRedirect]

A web extension that redirects YouTube, Twitter, TikTok, and other websites to alternative privacy friendly frontends. The extension is very customizable, including the possibility of enabling/disabling redirection per service category.

-   Mozilla Add-ons page: [https://addons.mozilla.org/en-US/firefox/addon/libredirect/](https://addons.mozilla.org/en-US/firefox/addon/libredirect/)
-   Homepage: [https://libredirect.github.io/](https://libredirect.github.io/)

#### [Facebook Container]

Facebook is able to track the activity of both loged-in and logged-out users through the presence of widgets such as a \"like\"/\"share\" button on a website. This add-on, created by Mozilla themselves, utilizes Firefox container tabs to isolate Facebook (and related sites such as Instagram) from the rest of your web sessions. When installed, accessing any Facebook sites will automatically open the page in a Facebook container tab. Accessing a non-Facebook site from within the container will automatically open the page in a tab outside of the container. Additionally, it disables the Facebook widgets outside of the Facebook container.

-   Mozilla Add-ons page: [https://addons.mozilla.org/en-US/firefox/addon/facebook-container/](https://addons.mozilla.org/en-US/firefox/addon/facebook-container/)
-   GitHub: [https://github.com/mozilla/contain-facebook](https://github.com/mozilla/contain-facebook)

** Note**\
Installing the Facebook Container add-on will automatically log the user out of Facebook, close any open Facebook tabs, and delete all Facebook cookies. It also enables the \"container tabs\" feature in Firefox. This add-on is disabled during private browsing.

#### [NoScript]

NoScript blocks JavaScript that is normally enabled by default. It can keep users safe and speed up web browsing.

-   Mozilla Add-ons page: [https://addons.mozilla.org/en-US/firefox/addon/noscript/](https://addons.mozilla.org/en-US/firefox/addon/noscript/)
-   Homepage: [https://noscript.net/](https://noscript.net/)

#### [Video speed controller]

Using an HTML5 video speed controller can be helpful in accelerating the playback rate of HTML 5 video. This is useful when binging video content on sites that do not offer increases in video playback speed (such as Amazon Prime Video or Netflix).

-   Mozilla Add-ons page: [https://addons.mozilla.org/en-US/firefox/addon/videospeed/](https://addons.mozilla.org/en-US/firefox/addon/videospeed/)
-   GitHub: [https://github.com/codebicycle/videospeed](https://github.com/codebicycle/videospeed)

#### [Behind The Overlay]

Some websites use modal overlays to display pop-ups, such that manually blocking the overlay with an add-on like uBlock Origin causes the page to become unscrollable. This add-on provides a one-click solution for bypassing such cases without the need to tinker with custom filtering rules.

-   Mozilla Add-ons page: [https://addons.mozilla.org/en-US/firefox/addon/behind_the_overlay/](https://addons.mozilla.org/en-US/firefox/addon/behind_the_overlay/)
-   GitHub: [https://github.com/NicolaeNMV/BehindTheOverlay](https://github.com/NicolaeNMV/BehindTheOverlay)

### [Policies]

Custom policies can be configured in Firefox, which is particularly useful in cases where Firefox is set up for an organization or end users. However, it can also be beneficial to block specific content for personal use. ^[\[22\]](#cite_note-22)^

The procedure may vary if the binary has been utilized. For this particular procedure, it is assumed that Firefox has been compiled on the system. To configure custom policies in this scenario, it is necessary to create a JSON file in the following directory:

[/etc/firefox/policies/policies.json]

The JSON file must meet the following structure:

[FILE] **`/etc/firefox/policies/policies.json`**


    }

As an example, creating a policy that blocks `about:config` and all URLs except for the Gentoo page and its subpages would require the following contents in the corresponding JSON file:

[FILE] **`/etc/firefox/policies/policies.json`**


      }
    }

** Note**\
It is important to ensure, that the `policies.json` is not writable by non-admin users, to prevent overwriting of the policies by users, which would defeat the purpose of policies! The [chown](https://linux.die.net/man/1/chown) and [chmod](https://linux.die.net/man/1/chmod) commands can be used to change ownership and rights if for any reason the file should be writable by non-admin users.

The success of the configuration can and should always be verified by checking the special page `about:policies`. This page also contains documentation and examples for other policy options. A complete list of policies can also be found in the [policy templates provided by Mozilla on GitHub](https://github.com/mozilla/policy-templates/blob/master/README.md).

It is recommended to carefully study the list, especially when the configuration is for other users. An approach of first blocking everything and then allowing specific desired pages is always preferable, as it reduces the likelihood of overlooking pages. Special pages and protocols (such as the `file://` protocol) that are not desired to be used, should also be considered to be blocked to prevent abuse of the security policies.

### [Local certificates]

Although Firefox uses the NSS library for handling the secure communications, it doesn\'t use the [\~/.pki/nssdb/] location, nor the system-wide CA certificate list in [/etc/ssl/certs/]. Instead, it uses its own list, stored in the file [cert9.db] in each Firefox profile directory (e.g. [\~/.mozilla/firefox/xxxxxxxx.default/]. The [cert9.db] file is an SQLite database; previously, a BerkeleyDB database was used, and the relevant file was [cert8.db].

To list Firefox\'s intermediate CA certificates, use [[[certutil(1)]](https://man.archlinux.org/man/certutil.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] (provided by [[[dev-libs/nss]](https://packages.gentoo.org/packages/dev-libs/nss)[]]) and installed as a dependency of Firefox and other packages):

`user `[`$`]`certutil -L -d ~/.mozilla/firefox/*.default/`

    Certificate Nickname                                         Trust Attributes
                                                                 SSL,S/MIME,JAR/XPI

    DigiCert High Assurance CA-3                                 ,,
    DigiCert Secure Server CA                                    ,,
    InCommon Server CA                                           ,,
    ...

Local certificates should be installed in [/usr/local/share/ca-certificates], and have the extension [.crt] (instead of e.g. [.pem]), as the extension checked by the [update-ca-certificates] script.

To add the certificate to the certificate list for a particular profile:

-   In Firefox, select Edit \> Settings \> Privacy & Security. Scroll to the \"Certificates\" section, then select the \"View certificates\" button; this will open the \"Certificate Manager\" dialog. Select the \"Import\" button.

<!-- -->

-   On the command line, use the [[[certutil(1)]](https://man.archlinux.org/man/certutil.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] utility:

`user `[`$`]`certutil -d ~/.mozilla/firefox/xxxxxxxx.default/ -A -n cert-nickname -i /usr/local/share/ca-certificates/my-cert.crt -t "CT,,"`

To add a certificate to the certificate list for all profiles, add the following to the [/etc/firefox/policies/policies.json] file (as described in the [Firefox](https://wiki.gentoo.org/wiki/Firefox#Policies "Firefox") section), creating it if necessary:

[FILE] **`/etc/firefox/policies/policies.json`FireFox certificates**


      }
    }

## [Hardware acceleration]

Enable the `hwaccel` USE flag for Firefox to get correct `about:config` options. Firefox \>116 will also install helper binaries, like [vaapitest]. This flag may cause Firefox to crash and is not necessary for hardware acceleration. If so, try the options below.

Verify that *web render* hardware acceleration is working by going to `about:support#graphics` and searching for **Compositing**. A value of `WebRender` means hardware acceleration is enabled, while `WebRender (software)` means it\'s not. If you have installed the correct video card drivers but WebRender is still using software rendering, try setting **gfx.webrender.all** to **true** in `about:config`.

Hardware accelerated *video* decoding status can also be checked on the `about:support#graphics` page. Search for `HARDWARE_VIDEO_DECODING`. `Available` means it\'s working. If video decoding is disabled, you may need to setup VA-API or VDPAU drivers.

Since 116, the `wayland` USE flag isn\'t needed to get hardware acceleration on supported cards for Rapid. For ESR, 115 needs the `hwaccel wayland` USE flags enabled to get hardware acceleration. `X` and `wayland` can be enabled simultaneously. \> 116 was fixed to have hardware acceleration without `wayland` support.

  ------- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ------------------------------------------------------------------------------------------------ ---------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                                 AMD                                                                       Intel                                                                                                                                                                                                                                                                                                                                  Nvidia
  ESR                                                               Should \'just work\' if the card is supported. \> 116 will have more cards supported than 115.   Should work if the card is supported (\> Haswell).   Install [[[media-libs/nvidia-vaapi-driver]](https://packages.gentoo.org/packages/media-libs/nvidia-vaapi-driver)[]] and check [its upstream documentation](https://github.com/elFarto/nvidia-vaapi-driver). Currently, nouveau does not support hardware acceleration in Firefox.
  Rapid                                                                                         Should work if the card is supported.                                Should work if the card is supported (\> Haswell).   Install [[[media-libs/nvidia-vaapi-driver]](https://packages.gentoo.org/packages/media-libs/nvidia-vaapi-driver)[]] and check [its upstream documentation](https://github.com/elFarto/nvidia-vaapi-driver). Currently, nouveau does not support hardware acceleration in Firefox.
  ------- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ------------------------------------------------------------------------------------------------ ---------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Troubleshooting]

#### [Disable hardware acceleration]

While disabling the `hwaccel` USE flag will get rid of the required `about:config` options, these can be enabled manually regardless of the USE flag status. To disable hardware acceleration, edit `about:config` with `media.hardware-video-decoding.enabled` set to false.

#### [Green artifacts on a video only with hardware acceleration]

Try setting **media.navigator.mediadatadecoder_vpx_enabled** to false in `about:config`.

#### [Hardware acceleration not working]

Make sure [[[media-video/libva-utils]](https://packages.gentoo.org/packages/media-video/libva-utils)[]] and [[[sys-apps/pciutils]](https://packages.gentoo.org/packages/sys-apps/pciutils)[]] are installed. Make sure vaapi works outside Firefox first with **vainfo** program. Try a different program to confirm vaapi works there, e.g. **mpv \--hwdec=vaapi**.

Debug the issue with **MOZ_LOG=\"PlatformDecoderModule:5\" firefox**. On startup this will show a handshake between Firefox and the vaapi system - the browser inquires which codecs are supported by hardware. You\'ll see a list of the codecs followed by SW or HW.

You may attempt to force Firefox to use hardware acceleration by setting the about:config flag **media.hardware-video-decoding.force-enabled** to true.

#### [Hardware acceleration not working within a sandbox]

When using an external sandbox application, such as [[[sys-apps/bubblewrap]](https://packages.gentoo.org/packages/sys-apps/bubblewrap)[]] or [[[sys-apps/firejail]](https://packages.gentoo.org/packages/sys-apps/firejail)[]], make sure that hardware acceleration works **outside** the sandboxing. Hardware acceleration will require more `ro` access permissions from [/dev] and [/sys].

## [Troubleshooting]

### [No video with supported format and MIME type found]

In **about:config** try to toggle **media.rdd-process.enabled** (default is true).

### [Audio]

#### [][Lack of sound (www-client/firefox-bin)]

[[[www-client/firefox-bin]](https://packages.gentoo.org/packages/www-client/firefox-bin)[]] expects [PulseAudio](https://wiki.gentoo.org/wiki/PulseAudio "PulseAudio"). [ALSA](https://wiki.gentoo.org/wiki/ALSA "ALSA")-only systems might work around this limitation by using [[[media-sound/apulse]](https://packages.gentoo.org/packages/media-sound/apulse)[]]. For this to work, modify Firefox sandbox settings by going to `about:config` and adding [/dev/snd/] (note the trailing slash) to the `security.sandbox.content.write_path_whitelist` option.

If storing ALSA settings in [\$HOME], also, be sure to add [\$HOME/.asoundrc] to the `security.sandbox.content.write_path_whitelist` option. Whitelist path could be separated by comma.

Since around Firefox 58 there is additional modification needed to work around seccomp sandbox: `security.sandbox.content.syscall_whitelist = 16` It is now possible to go ahead and create alias for running Firefox through [apulse]:

`user `[`$`]`alias firefox='apulse firefox-bin'`

#### [][Lack of sound when using PipeWire (www-client/firefox)]

**Problem:** System sound is working properly, but Firefox itself is unable to provide sound playback.

**Cause:** The [[[www-client/firefox]](https://packages.gentoo.org/packages/www-client/firefox)[]] package has support for three audio backends: ALSA, JACK and PulseAudio. With [PipeWire](https://wiki.gentoo.org/wiki/PipeWire "PipeWire") becoming the standard audio backend on Linux, support for ALSA (via the `alsa` USE flag) or PulseAudio (via the `pulseaudio` USE flag) may not be enabled by the target [desktop profile](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)"). The default audio backend for Firefox can be checked under `about:support#media` under **Audio Backend**:

[![](/images/thumb/9/9d/Firefox_audio_backend_screenshot.png/300px-Firefox_audio_backend_screenshot.png)](https://wiki.gentoo.org/wiki/File:Firefox_audio_backend_screenshot.png)

[](https://wiki.gentoo.org/wiki/File:Firefox_audio_backend_screenshot.png "Enlarge")

Firefox audio backend screenshot

**Solution:** Enable the `pulseaudio` USE flag for Firefox and then recompile Firefox. Be sure to follow the steps detailed in the [PipeWire article](https://wiki.gentoo.org/wiki/PipeWire#USE_flags "PipeWire") to setup pipewire-alsa.

#### [][Sound crackling when using Pipewire or JACK (www-client/firefox)]

**Problem:** System sound is crackling.

**Cause:** The [[[www-client/firefox]](https://packages.gentoo.org/packages/www-client/firefox)[]] package has support for two audio backends: JACK and PulseAudio. When using Pipewire, see [Arch Linux forum post on the issue](https://bbs.archlinux.org/viewtopic.php?id=280654). When using JACK, in the Configure dialog of [[[media-sound/qjackctl]](https://packages.gentoo.org/packages/media-sound/qjackctl)[]] or [[[media-sound/cadence]](https://packages.gentoo.org/packages/media-sound/cadence)[]], to set **Buffer Size: 1024** and **Periods/Buffer: 8** works fine for me.

### [Crashes]

If Firefox crashes for no apparent reason every few minutes with an error message like `ABORT: X_GLXDestroyContext: GLXBadContext; 15 requests ago` it might help to add the Firefox user(s) to the video group:

`root `[`#`]`gpasswd -a <username> video`

### [][Graphics/video]

#### [][Green video screen (YouTube)]

If disabling (graphics) acceleration in settings does not work, disabling the equivalent options under `about:config` like `layers.acceleration.force-enabled` (85.0) might.

#### [][Screen tearing / stuttering smooth scrolling]

Build [[[www-client/firefox]](https://packages.gentoo.org/packages/www-client/firefox)[]] with the `hwaccel` *USE* flag , then check the **Compositing** value of the `about:support#graphics` table for WebRender.

[![](/images/thumb/4/43/Firefox_Compositing_is_WebRender.png/300px-Firefox_Compositing_is_WebRender.png)](https://wiki.gentoo.org/wiki/File:Firefox_Compositing_is_WebRender.png)

[](https://wiki.gentoo.org/wiki/File:Firefox_Compositing_is_WebRender.png "Enlarge")

Screenshot of Compositing being set to WebRender

** Note**\
This solution does **not** work with [[[www-client/firefox-bin]](https://packages.gentoo.org/packages/www-client/firefox-bin)[]] because the *USE* flag is not available.

Systems with [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland") support should not have issues with screen tearing.

If WebRender is enabled, then the problem could be with the video drivers. For example about [Intel](https://wiki.gentoo.org/wiki/Intel#Screen_tearing "Intel").

### [][gtk+:3 pulls in D-Bus]

Since version ≥53.0, Firefox has dropped [gtk+](https://wiki.gentoo.org/wiki/GTK "GTK"):2 support urging [Larry](https://wiki.gentoo.org/wiki/Larry_the_cow "Larry the cow") to use gtk+:3. This, however, by default, pulls-in dependencies like [D-Bus](https://wiki.gentoo.org/wiki/D-Bus "D-Bus") unconditionally. This can be avoided by using a [patch from BSD](https://forums.gentoo.org/viewtopic-t-1060964-start-38-highlight-BSD%20maintain%20a%20patch.html) available in [[[bug #669234]](https://bugs.gentoo.org/show_bug.cgi?id=669234)[]] or the [mv overlay](https://github.com/gentoo-mirror/mv/tree/master/x11-libs/gtk%2B).

Please note that, when running Firefox under native Wayland (i.e. not using XWayland), [Firefox will implicitly try to use D-Bus to enable its remote control feature](https://utcc.utoronto.ca/~cks/space/blog/unix/FirefoxDBusRemoteControl) and crash, likely with a segfault, due to the lack of D-Bus. Thus, it is necessary to invoke Firefox with the `--no-remote` command-line argument or `MOZ_NO_REMOTE` environment variable set (to anything).

### [KDE Plasma Integration: failed to connect to the native host]

If using [[[www-client/firefox-bin]](https://packages.gentoo.org/packages/www-client/firefox-bin)[]], plasma integration might not work with default install due to `org.kde.plasma.browser_integration.json` installed in an unexpected directory ([/usr/lib64/mozilla] instead of [/usr/lib/mozilla]). See bug [[[bug #687736]](https://bugs.gentoo.org/show_bug.cgi?id=687736)[]] for details.

As a work around, creating a symlink will work:

`root `[`#`]`ln -s /usr/lib64/mozilla /usr/lib/mozilla`

### [Speech dispatcher library missing]

Some webpages may result in Firefox giving a notice that \"You can't use speech synthesis because the Speech Dispatcher library is missing."^[\[23\]](#cite_note-23)^ To fix this,

`root `[`#`]`emerge --ask app-accessibility/speech-dispatcher`

### [Wayland]

#### [Determine if Firefox is running the Wayland protocol backend]

To determine if Firefox is running with the Wayland protocol as a backend, check `about:support#graphics` table for the **Window Protocol** value. \"wayland\" will be displayed when running on the Wayland protocol. Other possible values include Xwayland and x11.

#### [][\"Failed to load cursor theme Adwaita\" in Wayland]

This happens because Firefox attempts to use [/usr/local/share/icons]. ^[\[24\]](#cite_note-24)^

See the reference above for the fix.

#### [Touchpad scrolling feels too fast on Wayland]

Change the option `apz.gtk.pangesture.delta_mode` from 0 to 2. Further tweaks are discussed in [this Mozilla bugtracker thread](https://bugzilla.mozilla.org/show_bug.cgi?id=1752862).

### [Windows decorations missing in Fluxbox since FF-91.3.0]

-   [https://forums.gentoo.org/viewtopic-t-1141870.html](https://forums.gentoo.org/viewtopic-t-1141870.html) Solved in 91.9.0esr and back with 102.3.0esr (64-bit)

Once in a while this happens. What might then help is to [restart fluxbox with the menu](https://sourceforge.net/p/fluxbox/bugs/1111/#3efa).

## [Troubleshooting tips]

If the problem cannot be clearly identified and the search engine search also does not provide a helpful solution, one good starting point for further investigation could be the special page `about:support`. This page contains, like mentioned in the special pages section, further technical information, along with more special pages like `about:memory` and others. This pages can be used for a more detailed investigation of the problem. The page can also be used to copy the raw technical data to obtain support. In this case, it is important to ensure that the copied content do not contain information which should not be published - if asking in a forum for assistance for example.

In the following steps it is assumed that Firefox was compiled on the system. If the binary was utilized, it is necessary to replace `firefox` with `firefox-bin` in the commands mentioned bellow. Whether the same applies to directories should be verified. Additionally, some of the following steps require a running graphical environment.\
If Firefox is used only in headless mode on a system without any graphical environment, the following procedure might not work or not work as expected.

### [Safe mode]

Starting Firefox in safe mode temporarily disables add-ons, hardware acceleration and [WebGL](https://en.wikipedia.org/wiki/WebGL "wikipedia:WebGL"), window and sidebar size along with other position settings, userChrome and userContent customizations, and the JavaScript JIT compiler.^[\[25\]](#cite_note-25)^ This can help to determine if a problem is related to any of the aforementioned components and whether it can be resolved by removing custom settings in those sections.

To start Firefox in safe mode, the Troubleshooting Mode on the special page `about:support` can be used.^[\[26\]](#cite_note-26)^ This can also be achieved by using the CLI. This is particularly useful when the `about:support` page is not accessible, such as when Firefox does not even start:

`user `[`$`]`firefox --safe-mode`

If prompted to choose between a refresh or proceeding with the troubleshooting mode, it is recommended to test first whether the troubleshooting mode solves the problem. This can be done by conforming with the \"Open\" option.

If the problem does not persist in safe mode, than it is probably related to hardware acceleration, custom themes, or to custom extensions. To deactivate these elements step-by-step and further narrow down the problem, [this guide by Mozilla can be followed](https://support.mozilla.org/en-US/kb/troubleshoot-extensions-themes-to-fix-problems#w_the-problem-does-not-occur-in-troubleshoot-mode).

If the problem was not caused by themes or extensions, but rather by hardware acceleration, it is recommended to review the [Gentoo Hardware Acceleration Guide](https://wiki.gentoo.org/wiki/Xorg/Hardware_3D_acceleration_guide "Xorg/Hardware 3D acceleration guide"), and to see if the issue can be resolved using the suggested steps there. This ensures that hardware acceleration was configured properly.

If the problem was caused by custom themes, extensions, or other custom settings within the following removal scope, a simple refresh may solve the problem. Refreshing Firefox will remove these settings and reset them to their default values:

-   Extensions and themes
-   website permissions
-   Modified preferences
-   Added search engines
-   DOM storage
-   Security certificates and device settings
-   Download actions
-   Toolbar customization and user styles (This also removes userChrome and/or userContent CSS files if they were created. If this custom files were created, a backup of these will be required before proceeding to prevent data loss)^[\[27\]](#cite_note-27)^.

A refresh can be performed either via the special page `about:support` and by searching the \"Refresh Firefox\" option or via the command line interface. To refresh via CLI:

`user `[`$`]`firefox --safe-mode`

If prompted, select \"Refresh Firefox\". This will not reset bookmarks, history, passwords, cookies, auto fill, and the personal directory^[\[28\]](#cite_note-28)^.

[![](/images/thumb/4/4b/Firefox_safe_mode.png/300px-Firefox_safe_mode.png)](https://wiki.gentoo.org/wiki/File:Firefox_safe_mode.png)

[](https://wiki.gentoo.org/wiki/File:Firefox_safe_mode.png "Enlarge")

Refresh prompt by running firefox \--safe-mode

### [Startup cache]

If the problems are related to startup issues, like slow loading times of the Firefox application after launch or immediate crashes after startup, a broken startup cache could be one of the possible problems. To test if the startup cache causes the undesired behavior it is possible to simply clear the startup cache. One way of doing so, is to search the associated option in the `about:support` page. Please note that clearing the cache via `about:support` do not provide a possibility to revert the cleared cache. However, the startup cache can also be cleared manually with a backup option.

The Firefox startup cache is typically located in the directory: [\~/.cache/mozilla]/firefox

Please be aware that the mozilla folder may also contain the caches from other Mozilla applications, like [Thunderbird](https://wiki.gentoo.org/wiki/Thunderbird "Thunderbird"). To reset the Firefox startup cache, it is required to rename the folder, so Firefox can create a new clean startup cache on the next startup:

`user `[`$`]`cd ~/.cache/mozilla`

`user `[`$`]`mv firefox firefox_old`

If this solves the problem and the old cache is not needed anymore, it can be deleted. If the problem was not caused by the startup cache, the changes can be easily reverted:

`user `[`$`]`cd ~/.cache/mozilla `

`user `[`$`]`rm -r firefox `

`user `[`$`]`mv firefox_old firefox `

### [Reset profile]

** Note**\
This solution works with important user related profile settings. Special attention is required to avoid data loss!

Firefox stores personal information such as bookmarks, passwords and user preferences on a separate location. To quick check if the problems are caused through profile misconfiguration, it is possible to use the same approach as in clearing the startup cache. Attention is required while performing this tasks, because they usually contain user related data, like password and alike.

To find the path of the profile location the `about:support` page can be used.\
For instance, a path example could be: [/home/username/.mozilla/firefox/ntgqave6.default-esr-1679659083216]

If the support page is not accessible, the usual storage location is: [\~/.mozilla/firefox]

To quick check profile related issues:

`user `[`$`]`cd ~/.mozilla `

`user `[`$`]`mv firefox firefox_bak `

This removes all existing profiles and Firefox will create a new, clean profile on the next startup. If this does not solve the problem the changes can be easily reverted. It is necessary to close all instances of Firefox before proceeding:

`user `[`$`]`cd ~/.mozilla `

`user `[`$`]`rm -r firefox `

`user `[`$`]`mv firefox_bak firefox `

If this solves the issue and profile related settings are required, a breakdown of the related files with their purpose can be found in [this Mozilla guide](https://support.mozilla.org/en-US/kb/profiles-where-firefox-stores-user-data#w_what-information-is-stored-in-my-profile).

In this case make sure, to backup the whole profile folder first, before merging the old files with the new once.

## [Firefox forked projects]

-   [GNU Icecat](https://wiki.gentoo.org/wiki/GNU_Icecat "GNU Icecat")
-   [LibreWolf](https://wiki.gentoo.org/wiki/LibreWolf "LibreWolf")
-   [Pale Moon](https://www.palemoon.org) --- Pale Moon Web Browser.

Wikipedia maintains a list of [projects based on Firefox](https://en.wikipedia.org/wiki/List_of_web_browsers#Gecko-based "wikipedia:List of web browsers") (may not be complete).

## [See also]

-   [Thunderbird](https://wiki.gentoo.org/wiki/Thunderbird "Thunderbird") --- Mozilla\'s solution to the e-mail client.

## [External resources]

-   [The official Firefox wiki (out-of-date)](https://wiki.mozilla.org/Firefox)
-   [Firefox on Mozilla\'s Forums](http://forums.mozillazine.org/viewforum.php?f=49)
-   [Firefox on Mozilla\'s Buglist](https://bugzilla.mozilla.org/buglist.cgi?quicksearch=Firefox)
-   [Change the interface language (L10N)](https://support.mozilla.org/en-US/questions/1018686)
-   [Creating a new profile](http://kb.mozillazine.org/Profile_Manager#Creating_a_new_profile)
-   [Firefox about:config privacy enhancements](https://gist.github.com/0XDE57/fbd302cef7693e62c769)

## [References]

1.  [[[↑](#cite_ref-1)] [[https://blog.llvm.org/2019/09/closing-gap-cross-language-lto-between.html](https://blog.llvm.org/2019/09/closing-gap-cross-language-lto-between.html)]]
2.  [[[↑](#cite_ref-2)] [this is subject to change with the [GCC Rust](https://github.com/Rust-GCC/gccrs)]]
3.  [[[↑](#cite_ref-3)] [Comparative evaluations of different build options for Firefox: ]]
    -   [Project:Mozilla/Firefox_Benchmarks_2025_Q1](https://wiki.gentoo.org/wiki/Project:Mozilla/Firefox_Benchmarks_2025_Q1#Benchmarks "Project:Mozilla/Firefox Benchmarks 2025 Q1")
    -   [https://documentation.suse.com/sbp/devel-tools/html/SBP-GCC-11/index.html#sec-gcc11-firefox](https://documentation.suse.com/sbp/devel-tools/html/SBP-GCC-11/index.html#sec-gcc11-firefox)
    -   [https://documentation.suse.com/sbp/devel-tools/html/SBP-GCC-10/index.html#sec-gcc10-firefox](https://documentation.suse.com/sbp/devel-tools/html/SBP-GCC-10/index.html#sec-gcc10-firefox)
4.  [[[↑](#cite_ref-4)] [[Project:Mozilla/Firefox_Benchmarks_2025_Q1](https://wiki.gentoo.org/wiki/Project:Mozilla/Firefox_Benchmarks_2025_Q1#Conclusions.2C_insights_and_summary "Project:Mozilla/Firefox Benchmarks 2025 Q1")]]
5.  [[[↑](#cite_ref-5)] [[https://askubuntu.com/a/95333](https://askubuntu.com/a/95333)]]
6.  [[[↑](#cite_ref-6)] [[https://www.mozilla.org/en-US/firefox/66.0/releasenotes](https://www.mozilla.org/en-US/firefox/66.0/releasenotes)]]
7.  [[[↑](#cite_ref-7)] [[https://bugzilla.mozilla.org/show_bug.cgi?id=1732358](https://bugzilla.mozilla.org/show_bug.cgi?id=1732358)]]
8.  [[[↑](#cite_ref-8)] [[https://bugzilla.mozilla.org/show_bug.cgi?id=1742892#c0](https://bugzilla.mozilla.org/show_bug.cgi?id=1742892#c0)]]
9.  [[[↑](#cite_ref-9)] [[https://firefox-source-docs.mozilla.org/dom/ipc/process_model.html#isolated-web-content](https://firefox-source-docs.mozilla.org/dom/ipc/process_model.html#isolated-web-content)]]
10. [[[↑](#cite_ref-10)] [[https://github.com/mozilla/cubeb/wiki/Backend-Support](https://github.com/mozilla/cubeb/wiki/Backend-Support)]]
11. [[[↑](#cite_ref-11)] [[https://github.com/mozilla/cubeb/blob/master/src/cubeb.c#L150](https://github.com/mozilla/cubeb/blob/master/src/cubeb.c#L150)]]
12. [[[↑](#cite_ref-12)] [[https://support.mozilla.org/en-US/kb/privacy-preserving-attribution](https://support.mozilla.org/en-US/kb/privacy-preserving-attribution)]]
13. [[[↑](#cite_ref-13)] [[https://blog.mozilla.org/netpolicy/2024/08/22/ppa-update/](https://blog.mozilla.org/netpolicy/2024/08/22/ppa-update/)]]
14. [[[↑](#cite_ref-14)] [[https://lunduke.locals.com/post/5871895/mozilla-firefox-goes-anti-privacy-pro-advertising](https://lunduke.locals.com/post/5871895/mozilla-firefox-goes-anti-privacy-pro-advertising)]]
15. [[[↑](#cite_ref-15)] [[https://news.ycombinator.com/item?id=40974112](https://news.ycombinator.com/item?id=40974112)]]
16. [[[↑](#cite_ref-16)] [[https://www.mozilla.org/en-US/firefox/130.0/releasenotes/](https://www.mozilla.org/en-US/firefox/130.0/releasenotes/)]]
17. [[[↑](#cite_ref-17)] [[https://support.mozilla.org/en-US/kb/ai-chatbot](https://support.mozilla.org/en-US/kb/ai-chatbot)]]
18. [[[↑](#cite_ref-18)] [[https://connect.mozilla.org/t5/discussions/ai-chatbot-at-your-service/td-p/84919](https://connect.mozilla.org/t5/discussions/ai-chatbot-at-your-service/td-p/84919)]]
19. [[[↑](#cite_ref-19)] [[https://addons.mozilla.org/en-GB/firefox/addon/ublock-origin/](https://addons.mozilla.org/en-GB/firefox/addon/ublock-origin/)]]
20. [[[↑](#cite_ref-20)] [[https://adnauseam.io/](https://adnauseam.io/)]]
21. [[[↑](#cite_ref-21)] [[https://www.technologyreview.com/2021/01/06/1015784/adsense-google-surveillance-adnauseam-obfuscation/](https://www.technologyreview.com/2021/01/06/1015784/adsense-google-surveillance-adnauseam-obfuscation/)]]
22. [[[↑](#cite_ref-22)] [[https://support.mozilla.org/en-US/kb/customizing-firefox-using-policiesjson](https://support.mozilla.org/en-US/kb/customizing-firefox-using-policiesjson)]]
23. [[[↑](#cite_ref-23)] [[https://support.mozilla.org/en-US/kb/speechd-setup](https://support.mozilla.org/en-US/kb/speechd-setup)]]
24. [[[↑](#cite_ref-24)] [[https://forums.gentoo.org/viewtopic-t-1160601-highlight-gdkwarning.html](https://forums.gentoo.org/viewtopic-t-1160601-highlight-gdkwarning.html)]]
25. [[[↑](#cite_ref-25)] [[https://support.mozilla.org/en-US/kb/diagnose-firefox-issues-using-troubleshoot-mode#w_what-does-troubleshoot-mode-disable](https://support.mozilla.org/en-US/kb/diagnose-firefox-issues-using-troubleshoot-mode#w_what-does-troubleshoot-mode-disable)]]
26. [[[↑](#cite_ref-26)] [[https://support.mozilla.org/en-US/kb/diagnose-firefox-issues-using-troubleshoot-mode#w_how-to-start-firefox-in-troubleshoot-mode](https://support.mozilla.org/en-US/kb/diagnose-firefox-issues-using-troubleshoot-mode#w_how-to-start-firefox-in-troubleshoot-mode)]]
27. [[[↑](#cite_ref-27)] [[https://support.mozilla.org/en-US/kb/refresh-firefox-reset-add-ons-and-settings?redirectslug=reset-firefox-easily-fix-most-problems&redirectlocale=en-US#w_these-items-and-settings-will-be-removed](https://support.mozilla.org/en-US/kb/refresh-firefox-reset-add-ons-and-settings?redirectslug=reset-firefox-easily-fix-most-problems&redirectlocale=en-US#w_these-items-and-settings-will-be-removed)]]
28. [[[↑](#cite_ref-28)] [[https://support.mozilla.org/en-US/kb/refresh-firefox-reset-add-ons-and-settings?redirectslug=reset-firefox-easily-fix-most-problems&redirectlocale=en-US#w_firefox-will-save-these-items](https://support.mozilla.org/en-US/kb/refresh-firefox-reset-add-ons-and-settings?redirectslug=reset-firefox-easily-fix-most-problems&redirectlocale=en-US#w_firefox-will-save-these-items)]]