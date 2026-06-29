This page contains [[changes](https://wiki.gentoo.org/index.php?title=Chromium&oldid=1430116&diff=1441742)] which are not marked for translation.

Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/Chromium/es "Chromium (27% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Chromium/hu "Chromium (77% translated)")
-   [svenska](https://wiki.gentoo.org/wiki/Chromium/sv "Chromium (37% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Chromium/zh-cn "Chromium (36% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Chromium/ja "Chromium (100% translated)")

**Resources**

[[]][Home](http://www.chromium.org/)

[[]][Package information](https://packages.gentoo.org/packages/www-client/chromium)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Chromium_(web_browser) "wikipedia:Chromium (web browser)")

[[]][Blog](http://blog.chromium.org/)

[[]][GitWeb](https://chromium.googlesource.com/chromium/src.git)

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Chromium "Project:Chromium")][Project](https://wiki.gentoo.org/wiki/Project:Chromium "Project:Chromium")

**Chromium** is the open source browser that [Google Chrome](https://wiki.gentoo.org/wiki/Google_Chrome "Google Chrome") and many other browsers are based on. It features a minimal user interface, powerful web development tools, and a built in task manager. The Chromium Project is at the forefront of implementing new web standards.

A complete list of the differences can be found in the [Chromium repository](https://chromium.googlesource.com/chromium/src/+/HEAD/docs/chromium_browser_vs_google_chrome.md).

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
        -   [[1.1.1] [icu]](#icu)
        -   [[1.1.2] [L10N]](#L10N)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [HiDPI]](#HiDPI)
    -   [[2.2] [Disable animations]](#Disable_animations)
    -   [[2.3] [Profile Directories]](#Profile_Directories)
-   [[3] [Security]](#Security)
    -   [[3.1] [Policies]](#Policies)
        -   [[3.1.1] [Creating of managed policies]](#Creating_of_managed_policies)
    -   [[3.2] [Local certificates]](#Local_certificates)
-   [[4] [Usage]](#Usage)
    -   [[4.1] [Chrome URLs]](#Chrome_URLs)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Screencast support]](#Screencast_support)
    -   [[5.2] [Tabs crash]](#Tabs_crash)
    -   [[5.3] [Why doesn\'t compilation respect my CFLAGS?]](#Why_doesn.27t_compilation_respect_my_CFLAGS.3F)
-   [[6] [Chromium-based browsers (forks)]](#Chromium-based_browsers_.28forks.29)
-   [[7] [See also]](#See_also)
-   [[8] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [www-client/chromium](https://packages.gentoo.org/packages/www-client/chromium) [[]] [Open-source version of Google Chrome web browser]

  ----------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------
  [`+X`](https://packages.gentoo.org/useflags/+X)                                     Add support for X11
  [`+hangouts`](https://packages.gentoo.org/useflags/+hangouts)                       Enable support for Google Hangouts features such as screen sharing
  [`+official`](https://packages.gentoo.org/useflags/+official)                       Enable Official build instead of Developer build.
  [`+proprietary-codecs`](https://packages.gentoo.org/useflags/+proprietary-codecs)   Enable codecs for patent-encumbered audio and video formats.
  [`+rar`](https://packages.gentoo.org/useflags/+rar)                                 Enable the Safe Browsing feature to inspect RAR files.
  [`+screencast`](https://packages.gentoo.org/useflags/+screencast)                   Enable support for remote desktop and screen cast using PipeWire
  [`+system-harfbuzz`](https://packages.gentoo.org/useflags/+system-harfbuzz)         Use system media-libs/harfbuzz instead of the bundled library.
  [`+system-icu`](https://packages.gentoo.org/useflags/+system-icu)                   Use system dev-libs/icu instead of the bundled one
  [`+system-zstd`](https://packages.gentoo.org/useflags/+system-zstd)                 Use system app-arch/zstd instead of the bundled one.
  [`+vaapi`](https://packages.gentoo.org/useflags/+vaapi)                             Enable Video Acceleration API for hardware decoding
  [`+wayland`](https://packages.gentoo.org/useflags/+wayland)                         Enable dev-libs/wayland backend
  [`+widevine`](https://packages.gentoo.org/useflags/+widevine)                       Unsupported closed-source DRM capability (required by Netflix VOD)
  [`bindist`](https://packages.gentoo.org/useflags/bindist)                           Flag to enable or disable options for prebuilt (GRP) packages (eg. due to licensing issues)
  [`bundled-toolchain`](https://packages.gentoo.org/useflags/bundled-toolchain)       Download and use the upstream binary toolchain(s) to build Chromium
  [`cups`](https://packages.gentoo.org/useflags/cups)                                 Add support for CUPS (Common Unix Printing System)
  [`custom-cflags`](https://packages.gentoo.org/useflags/custom-cflags)               Build with user-specified CFLAGS (unsupported)
  [`debug`](https://packages.gentoo.org/useflags/debug)                               Enable DCHECK feature with severity configurable at runtime. Mostly intended for debugging and development, NOT RECOMMENDED for general use.
  [`ffmpeg-chromium`](https://packages.gentoo.org/useflags/ffmpeg-chromium)           (binpkg only) Use Chromium FFmpeg fork (media-video/ffmpeg-chromium) rather than mainline FFmpeg (media-video/ffmpeg)
  [`gtk4`](https://packages.gentoo.org/useflags/gtk4)                                 Build with GTK4 headers.
  [`headless`](https://packages.gentoo.org/useflags/headless)                         Build Ozone only with headless backend, NOT RECOMMENDED for general use.
  [`kerberos`](https://packages.gentoo.org/useflags/kerberos)                         Add kerberos support
  [`pax-kernel`](https://packages.gentoo.org/useflags/pax-kernel)                     Allow building on a PaX-enabled kernel
  [`pgo`](https://packages.gentoo.org/useflags/pgo)                                   Build with Profile Guided Optimizations (2-stage compilation)
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)                     Add sound server support via media-libs/libpulse (may be PulseAudio or PipeWire)
  [`qt6`](https://packages.gentoo.org/useflags/qt6)                                   Add support for the Qt 6 application and UI framework
  [`selinux`](https://packages.gentoo.org/useflags/selinux)                           !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`test`](https://packages.gentoo.org/useflags/test)                                 Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-24 00:34] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

#### [icu]

** Important**\
To avoid an emerge slot conflict with [[[dev-libs/libxml2]](https://packages.gentoo.org/packages/dev-libs/libxml2)[]], which prevents Chromium from being emerged, `icu` USE flag must be set in [/etc/portage/make.conf]. If `icu` is newly set, update the system before emerging Chromium by issuing:\
\

`root `[`#`]`emerge --ask --update --deep --newuse @world`

#### [L10N]

There are many languages available via the [`L10N`](https://wiki.gentoo.org/wiki/Localization "Localization") [`USE_EXPAND`](https://wiki.gentoo.org/wiki/USE_EXPAND "USE EXPAND") variable in Chromium. So many, in fact, that the wiki cannot display all of them. For a full list of localization languages run:

`user `[`$`]`equery u www-client/chromium | grep -i l10n`

** Note**\
The [equery] tools comes as part of the [[[app-portage/gentoolkit]](https://packages.gentoo.org/packages/app-portage/gentoolkit)[]] package. It will need to be installed in order to use the above command.

For more information on localization see the [Localization](https://wiki.gentoo.org/wiki/Localization "Localization") article.

### [Emerge]

** Tip**\
Be aware that compiling Chromium can take a significant amount of real time, CPU time, and system memory. Allow 2Gb of RAM per each make thread (as defined by [MAKEOPTS](https://wiki.gentoo.org/wiki/MAKEOPTS "MAKEOPTS"), see [this post](https://forums.gentoo.org/viewtopic-t-1118442.html)). It is probably not a good idea to build Chromium when the system is under heavy load.

Gentoo\'s Chromium package enables the various channels to be installed simultaneously, using SLOTs to select the enabled versions.

Typically users on `arch` will receive the stable channel, while users on `~arch` will end up with the beta channel, however testing users consider explicitly selecting the either the stable or beta slot as during channel promotions, stable is often released the day before beta and with a higher patch version; portage will prefer stable as the highest `~arch`-keyworded package in this case.

The dev (unstable) channel is also provided, but is not keyworded. Users should feel free to unmask this package and enable as many channels as they would like, noting the compile time for each channel (ccache may help, though the cache would need to be reasonably sized \[100+GB\]).

After setting USE flags as desired, [emerge] Chromium with the following command:

`root `[`#`]`emerge --ask www-client/chromium`

or, to select a specific slot (or slots):

`root `[`#`]`emerge --ask www-client/chromium:stable www-client/chromium:beta`

## [Configuration]

### [HiDPI]

Chromium\'s visual output is generally disconnected from a [Desktop environment](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment")\'s DPI scaling. It can be instructed to start in a scaled mode by using the `--force-device-scale-factor` command-line option. This option can be passed a integer or decimal value. Standard scaling begins at 1.0. For example, to make Chromium\'s UI 1.5x larger:

`user `[`$`]`chromium --force-device-scale-factor=1.5`

A full list of command-line switches can be found [here](https://peter.sh/experiments/chromium-command-line-switches/).

### [Disable animations]

To turn off animations, set the following parameters:

[FILE] **`/etc/chromium/default`**

    CHROMIUM_FLAGS="--wm-window-animations-disabled --animation-duration-scale=0"

### [Profile Directories]

Gentoo enables simultaneous installation of the various Chromium channels (stable, beta, dev \[unstable\]). As a result of this, each channel has an independent profile directory in the same way that Google Chrome or any other properly-channeled Chromium-based browser. This is a requirement as Chromium semi-regularly performs incompatible profile format upgrades that will cause older versions / channels to crash on startup without an error message.

It is possible to copy / move the profile directory for a particular user in the event that they switch to a later channel, however it is \*not\* advisable to attempt sharing a profile directory between channels by symlinking.

The various channel profile directories are:

-   Stable: [\~/.config/chromium]
-   Beta: [\~/.config/chromium-beta]
-   Dev: [\~/.config/chromium-unstable]

## [Security]

### [Policies]

It is possible to set specific policies for chromium. This can be useful especially if the browser should be accessible by users, but the content should be restricted to trusted sites. It can also be configured to restrict the access to specified URIs, like the `file://` protocol, to prevent users from surfing the file system.

Chromium looks in [/etc/chromium/policies] for existing policies. There are two types of policies which can be defined:

-   managed
-   recommended

Generally managed policies are maintained by an administrator and recommended policies are recommended for users but not required.\
For further information about the two policy types the documentation should be referred on the [Google Chrome support page](https://support.google.com/chrome/a/answer/9037717?hl=en).

The following example assumes managed policies. However, the procedure for recommended policies is very similar and can be found in the [Chromium documentation](https://www.chromium.org/administrators/linux-quick-start/).

#### [Creating of managed policies]

To set custom managed policies, a JSON file must be created in [/etc/chromium/policies/managed/\<filename\>.json]

** Note**\
It is important to ensure, that the `<filename>.json` is not writable by non-admin users, to prevent overwriting of the policies by users, which would defeat the purpose of policies! The [[[chown(1)]](https://man.archlinux.org/man/chown.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] and [[[chmod(1)]](https://man.archlinux.org/man/chmod.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] commands can be used to change ownership and rights if for any reason the file should be writable by non-admin users.

The structure of the JSON file is the same for all chromium based browsers (Chrome, Chromium, Brave etc). An example JSON file could look like this:

[CODE]



This prevents the user from surfing on the file system using the file protocol, incognito mode, blocks the listed URIs and URLs, and the location and notifications. More settings, can be found in the policy list: [https://www.chromium.org/administrators/policy-list-3/](https://www.chromium.org/administrators/policy-list-3/). If configured for other users as a service, it is recommended to block all sites at first and then define the allowed sites, to avoid abuse of the service. Please note that this only blocks the user from visiting specified locations. It does not disable the protocols on the system, so other applications must be configured separately.

If the policy was configured properly can be proofed on the special page: `chrome://policy`.

For a better structure, it is also possible to spread the policies over multiple JSON files. In this case it is indispensable to ensure that the same policy occurs only once per all files! If a policy is defined multiple times across the JSON files than the state of the policy will be undefined and it would be unclear which rule would be used!

Meaningful filenames and a simple grep across the files in case of doubt can help to prevent such misconfigurations.

### [Local certificates]

Chromium (like many other web browsers, such as Firefox) does not use the system-wide CA certificate list.

To use a custom certificate when using Chromium-based Web browsers like Chrome, open [chrome://settings/certificates], choose the \"Authorities\" tab, and import the certificate.

## [Usage]

### [Chrome URLs]

Much like Firefox, Chromium has many internal Chrome URLs (special pages) that are used for additional configuration, troubleshooting, task management, etc. An exhaustive list of special pages can be accessed by navigating to: `chrome://chrome-urls/`

Prominent special pages include:

-   `chrome://components` - Shows enabled components and provides a button to check for updates for each of them.
-   `chrome://extensions` - A page to manage extensions.
-   `chrome://flags` - Enable/disable experimental features.
-   `chrome://gpu` - Displays information about use of graphics acceleration.
-   `chrome://history` - Displays web history. Also accessible through the sandwich menu or by pressing [Ctrl]+[h].
-   `chrome://net-internals/` - Lots of information on network connections.
-   `chrome://version/` - Displays more version information than the `chrome` page.

## [Troubleshooting]

### [Screencast support]

Screencast is disabled by default at runtime. Either enable it by navigating to `chrome://flags/#enable-webrtc-pipewire-capturer` inside Chromium or add `--enable-features=WebRTCPipeWireCapturer` as a value to the `CHROMIUM_FLAGS` variable in the [/etc/chromium/default] file.

### [Tabs crash]

Occasionally tabs in Chromium crash. This can be caused by quite a few things, however one of the most common reason for occurrence is that the system is running low on memory. On Gentoo, this can especially happen if the system is compiling a [[[www-client/chromium]](https://packages.gentoo.org/packages/www-client/chromium)[]] package update *while running* Chromium.

The [free] command can be used to see how much memory is available on the system:

`user `[`$`]`free -h`

                  total        used        free      shared  buff/cache   available
    Mem:            15G         11G        735M        789M        3.4G        3.1G

The solution to is to free up memory until the large package compiles have finished. Open a resource monitor of choice and kill applications using large amounts of memory.

### [][Why doesn\'t compilation respect my CFLAGS?]

For the most part, there is limited benefit to passing microarchitecture flags like `-march`, `-mtune`, or `-mcpu` into a Chromium build. In fact, when these flags aren\'t explicitly filtered by the ebuild, they are known to cause compilation failures.

The reasons for this are straightforward:

1.  We use Chromium\'s upstream `//build/toolchain/linux/unbundle` toolchain configuration, which allows downstream distributions to inject system compilers and environment variables into the build system.
2.  The unbundle toolchain implementation appends system `CFLAGS` *after* Chromium\'s internal configuration files have established their own highly targeted optimisation flags.
3.  Certain critical multimedia or maths components require specific vector instruction sets (e.g., `AVX2`/`AVX-512` on `amd64`, or `SVE`/`SME` on `arm64`) to build hardware-accelerated code blocks. Chromium compiles multiple variants and selects the best variant at runtime based on the host CPU. Because system flags are appended last by the `unbundle` toolchain, a restrictive global `-march` can completely override these localised targets, causing the compiler to reject code sections written for advanced extensions.

** Tip**\
The processor building a given package doesn\'t need to support specific instructions to produce output that includes them. The compiler emits the requested machine code, and Chromium relies on runtime feature detection to safely execute those code paths only on capable hardware.

Users who wish to ignore this may enable [[[custom-cflags]](https://packages.gentoo.org/useflags/custom-cflags)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")], however bugs related to the issues described above will not receive support.

## [][Chromium-based browsers (forks)]

-   [Brave](https://wiki.gentoo.org/wiki/Brave "Brave") --- a web browser focused on privacy, blocking trackers, and advertisements.
-   [Opera](https://wiki.gentoo.org/wiki/Opera "Opera") --- a multi-platform web browser.
-   Microsoft Edge
-   [Vivaldi](https://wiki.gentoo.org/wiki/Vivaldi "Vivaldi") --- a browser for our friends.

## [See also]

-   [Firefox](https://wiki.gentoo.org/wiki/Firefox "Firefox") --- [open source](https://en.wikipedia.org/wiki/Open_source "wikipedia:Open source"), [multiplatform](https://en.wikipedia.org/wiki/Cross-platform_software "wikipedia:Cross-platform software"), [web browser](https://wiki.gentoo.org/wiki/Recommended_applications#Web_browsers "Recommended applications") developed by [Mozilla](https://en.wikipedia.org/wiki/Mozilla "wikipedia:Mozilla").
-   [Chrome](https://wiki.gentoo.org/wiki/Chrome "Chrome") --- Google\'s proprietary (closed source) web browser.

## [References]