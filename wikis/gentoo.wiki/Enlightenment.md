**Resources**

[[]][Home](https://www.enlightenment.org/)

[[]][Package information](https://packages.gentoo.org/packages/x11-wm/enlightenment)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Enlightenment_(software) "wikipedia:Enlightenment (software)")

[[]][GitWeb](https://git.enlightenment.org/)

[[]][[#e](ircs://irc.libera.chat/#e)] ([[webchat](https://web.libera.chat/#e)])

[[]][[#gentoo-desktop](ircs://irc.libera.chat/#gentoo-desktop)] ([[webchat](https://web.libera.chat/#gentoo-desktop)])

**Enlightenment** is an eye-candy, compositing and stacking [window manager](https://wiki.gentoo.org/wiki/Window_manager "Window manager") that is released under the permissive BSD License. It was first released in 1997 by Carsten Haitzler (Rasterman) and this original release was dubbed Enlightenment DR16 (or E16 for short). In 2012 a new version of Enlightenment was released, which was called Enlightenment DR17 (or E17). Since then many further major releases of Enlightenment have been made, from E18 to E24.

There has been some confusion over Enlightenment versions. E16, despite being an older release of Enlightenment, has its releases numbered 1.x, while the later releases of Enlightenment (E17-E23) all have decimal release numbers. E17 is numbered 0.17.x, E18 is numbered 0.18.x, E19 is numbered 0.19.x while E20 is numbered 0.20.x and so on. Consequently, it is advised that users are careful as to which version of Enlightenment they are installing. While the version numbers reflect actual versions of the upstream tar archives, they can be confusing.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Latest Enlightenment]](#Latest_Enlightenment)
    -   [[1.3] [Stable Enlightenment]](#Stable_Enlightenment)
    -   [[1.4] [Enlightenment live ebuilds]](#Enlightenment_live_ebuilds)
    -   [[1.5] [Enlightenment e16]](#Enlightenment_e16)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Enlightenment]](#Enlightenment)
    -   [[2.2] [Launching enlightenment with startx]](#Launching_enlightenment_with_startx)
-   [[3] [Tips and tricks]](#Tips_and_tricks)
    -   [[3.1] [Adding Gadgets to desktop]](#Adding_Gadgets_to_desktop)
    -   [[3.2] [Autostarting applications on login]](#Autostarting_applications_on_login)
    -   [[3.3] [Disabling desktop application icons]](#Disabling_desktop_application_icons)
    -   [[3.4] [Using \'bryce\' instead of old-fashioned panel]](#Using_.27bryce.27_instead_of_old-fashioned_panel)
    -   [[3.5] [Wayland session]](#Wayland_session)
    -   [[3.6] [Request dark theme from applications]](#Request_dark_theme_from_applications)
    -   [[3.7] [Themes]](#Themes)
-   [[4] [EFL-based applications]](#EFL-based_applications)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Applications requiring system tray not working properly]](#Applications_requiring_system_tray_not_working_properly)
    -   [[5.2] [Black window contents]](#Black_window_contents)
    -   [[5.3] [\"No opengl engines found\" with nvidia-drivers]](#.22No_opengl_engines_found.22_with_nvidia-drivers)
    -   [[5.4] [Use systemd user session to select the window manager]](#Use_systemd_user_session_to_select_the_window_manager)
    -   [[5.5] [\"build error: conflicting types for 'GLintptr'\"]](#.22build_error:_conflicting_types_for_.E2.80.98GLintptr.E2.80.99.22)
    -   [[5.6] [\"build error: undefined symbol: \_EFL_GFX_PATH_CHANGED\"]](#.22build_error:_undefined_symbol:_EFL_GFX_PATH_CHANGED.22)
    -   [[5.7] [Xorg touchpad config ignored]](#Xorg_touchpad_config_ignored)
    -   [[5.8] [Debugging]](#Debugging)
    -   [[5.9] [Can\'t change keyboard layout]](#Can.27t_change_keyboard_layout)
-   [[6] [Screenshots]](#Screenshots)
-   [[7] [See also]](#See_also)
-   [[8] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [x11-wm/enlightenment](https://packages.gentoo.org/packages/x11-wm/enlightenment) [[]] [Enlightenment window manager]

  ------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------
  [`bluetooth`](https://packages.gentoo.org/useflags/bluetooth)       Enable Bluetooth Support
  [`connman`](https://packages.gentoo.org/useflags/connman)           Add support for net-misc/connman
  [`doc`](https://packages.gentoo.org/useflags/doc)                   Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`exif`](https://packages.gentoo.org/useflags/exif)                 Add support for reading EXIF headers from JPEG and TIFF images
  [`geolocation`](https://packages.gentoo.org/useflags/geolocation)   Enable physical position determination
  [`nls`](https://packages.gentoo.org/useflags/nls)                   Add Native Language Support (using gettext - GNU locale utilities)
  [`pam`](https://packages.gentoo.org/useflags/pam)                   Add support for PAM (Pluggable Authentication Modules) - DANGEROUS to arbitrarily flip
  [`policykit`](https://packages.gentoo.org/useflags/policykit)       Enable PolicyKit (polkit) authentication support
  [`systemd`](https://packages.gentoo.org/useflags/systemd)           Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`udisks`](https://packages.gentoo.org/useflags/udisks)             Enable storage management support (automounting, volume monitoring, etc)
  [`wayland`](https://packages.gentoo.org/useflags/wayland)           Enable dev-libs/wayland backend
  [`xwayland`](https://packages.gentoo.org/useflags/xwayland)         Enable XWayland application support
  ------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-01-09 09:58] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

All Wayland related modules should be either disabled or enabled, depending on the `wayland` USE flag status.

### [USE flags for] [dev-libs/efl](https://packages.gentoo.org/packages/dev-libs/efl) [[]] [Enlightenment Foundation Libraries all-in-one package]

  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+X`](https://packages.gentoo.org/useflags/+X)                     Add support for X11
  [`+eet`](https://packages.gentoo.org/useflags/+eet)                 Enable Eet image loader
  [`+fontconfig`](https://packages.gentoo.org/useflags/+fontconfig)   Support for configuring and customizing font access via media-libs/fontconfig
  [`+gstreamer`](https://packages.gentoo.org/useflags/+gstreamer)     Add support for media-libs/gstreamer (Streaming media)
  [`+pdf`](https://packages.gentoo.org/useflags/+pdf)                 Add general support for PDF (Portable Document Format), this replaces the pdflib and cpdflib flags
  [`+sound`](https://packages.gentoo.org/useflags/+sound)             Enable sound support
  [`+svg`](https://packages.gentoo.org/useflags/+svg)                 Add support for SVG (Scalable Vector Graphics)
  [`+system-lz4`](https://packages.gentoo.org/useflags/+system-lz4)   Use system liblz4 instead of bundled one
  [`avif`](https://packages.gentoo.org/useflags/avif)                 Add AV1 Image Format (AVIF) support
  [`bmp`](https://packages.gentoo.org/useflags/bmp)                   Enable WBMP image loader
  [`connman`](https://packages.gentoo.org/useflags/connman)           Add support for net-misc/connman
  [`dds`](https://packages.gentoo.org/useflags/dds)                   Enable DDS image loader
  [`debug`](https://packages.gentoo.org/useflags/debug)               Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`doc`](https://packages.gentoo.org/useflags/doc)                   Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`drm`](https://packages.gentoo.org/useflags/drm)                   Enable DRM engine
  [`efl-one`](https://packages.gentoo.org/useflags/efl-one)           Combine multiple core libraries into one libefl.so
  [`elogind`](https://packages.gentoo.org/useflags/elogind)           Enable session tracking via sys-auth/elogind
  [`examples`](https://packages.gentoo.org/useflags/examples)         Install examples, usually source code
  [`fbcon`](https://packages.gentoo.org/useflags/fbcon)               Add framebuffer support for the console, via the kernel
  [`fribidi`](https://packages.gentoo.org/useflags/fribidi)           Enable bidirectional text support
  [`gif`](https://packages.gentoo.org/useflags/gif)                   Add GIF image support
  [`glib`](https://packages.gentoo.org/useflags/glib)                 Enable dev-libs/glib support
  [`harfbuzz`](https://packages.gentoo.org/useflags/harfbuzz)         Enable complex text shaping and layout support
  [`heif`](https://packages.gentoo.org/useflags/heif)                 Enable support for ISO/IEC 23008-12:2017 HEIF/HEIC image format
  [`hyphen`](https://packages.gentoo.org/useflags/hyphen)             Enable text hyphenation support
  [`ibus`](https://packages.gentoo.org/useflags/ibus)                 Enable Intelligent Input Bus
  [`ico`](https://packages.gentoo.org/useflags/ico)                   Enable Ico image loader
  [`jpeg2k`](https://packages.gentoo.org/useflags/jpeg2k)             Support for JPEG 2000, a wavelet-based image compression format
  [`jpegxl`](https://packages.gentoo.org/useflags/jpegxl)             Add JPEG XL image support
  [`json`](https://packages.gentoo.org/useflags/json)                 Enable lottie animation support
  [`mono`](https://packages.gentoo.org/useflags/mono)                 Enable mono bindings
  [`nls`](https://packages.gentoo.org/useflags/nls)                   Add Native Language Support (using gettext - GNU locale utilities)
  [`opengl`](https://packages.gentoo.org/useflags/opengl)             Add support for OpenGL (3D graphics)
  [`physics`](https://packages.gentoo.org/useflags/physics)           Enable Bullet physics effects and support
  [`pmaps`](https://packages.gentoo.org/useflags/pmaps)               Enable PMAPS image loader
  [`postscript`](https://packages.gentoo.org/useflags/postscript)     Enable support for the PostScript language (often with ghostscript-gpl or libspectre)
  [`psd`](https://packages.gentoo.org/useflags/psd)                   Enable PSD image loader
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)     Add sound server support via media-libs/libpulse (may be PulseAudio or PipeWire)
  [`raw`](https://packages.gentoo.org/useflags/raw)                   Add support for raw image formats
  [`scim`](https://packages.gentoo.org/useflags/scim)                 Enable Smart Common Input Method
  [`sdl`](https://packages.gentoo.org/useflags/sdl)                   Add support for Simple Direct Layer (media library)
  [`systemd`](https://packages.gentoo.org/useflags/systemd)           Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`tga`](https://packages.gentoo.org/useflags/tga)                   Enable Tga image loader
  [`tgv`](https://packages.gentoo.org/useflags/tgv)                   Enable Tgv image loader
  [`tiff`](https://packages.gentoo.org/useflags/tiff)                 Add support for the TIFF image format
  [`tslib`](https://packages.gentoo.org/useflags/tslib)               Enable x11-libs/tslib for touchscreen events
  [`unwind`](https://packages.gentoo.org/useflags/unwind)             Enable debug support via sys-libs/libunwind
  [`v4l`](https://packages.gentoo.org/useflags/v4l)                   Enable support for video4linux (using linux-headers or userspace libv4l libraries)
  [`vnc`](https://packages.gentoo.org/useflags/vnc)                   Enable VNC (remote desktop viewer) support
  [`wayland`](https://packages.gentoo.org/useflags/wayland)           Enable dev-libs/wayland backend
  [`webp`](https://packages.gentoo.org/useflags/webp)                 Add support for the WebP image format
  [`xcf`](https://packages.gentoo.org/useflags/xcf)                   Enable XCF image loader
  [`xim`](https://packages.gentoo.org/useflags/xim)                   Enable X Input Method
  [`xpm`](https://packages.gentoo.org/useflags/xpm)                   Add support for XPM graphics format
  [`xpresent`](https://packages.gentoo.org/useflags/xpresent)         Enable x11-libs/libXpresent support
  [`zeroconf`](https://packages.gentoo.org/useflags/zeroconf)         Support for DNS Service Discovery (DNS-SD)
  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-01-09 09:58] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

EFL preview and menu entries support the `svg` USE flag. It is recommended have at least the USE flags `X drm eet fontconfig gles2 gstreamer harfbuzz ico jpeg2k pulseaudio sound svg system-lz4 systemd`.

### [Latest Enlightenment]

To install the latest Enlightenment and libraries, issue:

`root `[`#`]`emerge --ask enlightenment`

### [Stable Enlightenment]

Because upstream only provides support for the latest Enlightenment, Gentoo will try to follow upstream\'s release cycles closely. When preferring to use older releases of Enlightenment WM, setting up a [local overlay](https://wiki.gentoo.org/wiki/Custom_repository#Creating_a_local_repository "Custom repository") to store ebuilds for x11-wm/enlightenment and dev-libs/efl may be necessary. Older ebuilds can be located by utilizing [gentoo.git history](https://gitweb.gentoo.org/repo/gentoo.git/log/x11-wm/enlightenment?showmsg=1).

On stable systems, to get the latest stable version, type

`root `[`#`]`emerge --ask x11-wm/enlightenment`

Utilize [/etc/portage/package.mask] to block incoming updates.

### [Enlightenment live ebuilds]

The process is a little different because it\'s recommended to always rebuild all of the components using their current state in [Git](https://wiki.gentoo.org/wiki/Git "Git"). Verify [Eselect/Repository](https://wiki.gentoo.org/wiki/Eselect/Repository "Eselect/Repository") has been installed, then add the [enlightenment-live](http://gpo.zugaina.org/Overlays/enlightenment-live) overlay.

`root `[`#`]`eselect repository enable enlightenment-live`

Verify all core enlightenment packages using live ebuilds. This can be updated using the exact same command to ensure that all core packages are updated.

`root `[`#`]`emerge --ask --autounmask-write @enlightenment-core-9999`

The *enlightenment-core-9999* set contains the following packages:

[CODE] **enlightenment-core-9999 content**

    ''
     =dev-libs/efl-9999
     =x11-wm/enlightenment-9999
     =x11-terms/terminology-9999

When installing both stable and experimental EFL application, *enlightenment-apps-9999* may be set. It contains:

[CODE] **enlightenment-apps-9999 content**

    ''
     =app-editors/ecrire-9999
     =app-misc/equate-9999
     =dev-vcs/egitu-9999
     =media-gfx/eluminance-9999
     =media-gfx/ephoto-9999
     =media-video/rage-9999
     =net-irc/express-9999
     =net-p2p/epour-9999
     =dev-util/espionage-9999
     =sys-process/evisum-9999

** Note**\
The ebuild for EFL is now using meson. USE flags may be different.

Be aware that they are currently masked for \~amd64, so they may require unmasking:

`root `[`#`]`emerge --ask --autounmask-write efl enlightenment`

** Note**\
The ebuilds are currently tested for X and not for Wayland. Further investigation and feedback is needed for Enlightenment with Wayland

If anything goes wrong, file a ticket on GitHub or contact [User:Rafspiny](https://wiki.gentoo.org/wiki/User:Rafspiny "User:Rafspiny"). Those are live ebuilds and therefore they can occasionally need updating. I\'m also considering starting a separate overlay just for Enlightenment.

### [Enlightenment e16]

Old Enlightenment-e16 is still maintained. Install it from Gentoo\'s main tree with

`root `[`#`]`emerge --ask e16`

## [Configuration]

### [Enlightenment]

Enlightenment\'s configuration is all handled through its settings editor. \"Under-the-hood\" configuration options are accessed via:

`user `[`$`]`elementary_config`

The command line tool `vieet` is especially useful in emergencies. In many cases, moving the broken [\~/.e] and [\~/.elementary] configuration to a temporary place before re-starting Enlightenment usually helps.

### [Launching enlightenment with startx]

[FILE] **`~/.xinitrc`**

    exec dbus-launch --exit-with-session enlightenment_start

## [Tips and tricks]

### [Adding Gadgets to desktop]

Open up menu and navigate to \"Desktop -\> Add Gadgets\".

### [Autostarting applications on login]

There\'s a comprehensive setting editor for that in the Settings Panel, under \"Applications -\> Autostart applications\"

### [Disabling desktop application icons]

The option to disable application icons in desktop is a bit hidden. Open Settings Panel then go to \"Files\" tab, navigate to \"File Manager -\> Display\" and uncheck \"Icons On Desktop\".

### [][Using \'bryce\' instead of old-fashioned panel]

With recent versions, users can opt to use experimental new \"bryce\" instead of old panel. Open desktop menu and navigate to \"Desktop -\> Add Bryce\". Bryces are experimental in Enlightenment\'s versions below 0.25.

### [Wayland session]

** Important**\
At the time of writing (28 Sept 2020) Enlightenment with Wayland session is **not** considered stable for everyday use.

Easiest way to start a wayland session is to use a wayland-compliant login manager, like [GDM](https://packages.gentoo.org/packages/gnome-base/gdm) or [SDDM](https://packages.gentoo.org/packages/x11-misc/sddm). Wayland session can be started from TTY also, by calling

`user `[`$`]`enlightenment_start`

provided that wayland USE flag and dependencies are set up correctly. There are some fine-tuning options to be exported, if needed:

`user `[`$`]`ECORE_EVAS_ENGINE=wayland_egl ELM_DISPLAY=wl ELM_ACCEL=gl enlightenment_start`

where `ECORE_EVAS_ENGINE` is set to `wayland_egl` or `wayland_shm` depending on SHM based software rendering or EGL is desired.

When using software rendering, also export `ELM_ACCEL=none`.

Note that in theory Wayland should work with elogind, but only systemd is supported by upstream.

### [Request dark theme from applications]

To request applications to use their dark theme if available, checkout [GTK#System-wide_dark_theme](https://wiki.gentoo.org/wiki/GTK#System-wide_dark_theme "GTK") and [Qt#Theming](https://wiki.gentoo.org/wiki/Qt#Theming "Qt")!

### [Themes]

The **Theme** settings panel offers the possibility to either import a new theme from a file or from the online tool.

When it comes to icon themes, you are required to unpack them in *\~/.local/share/icons*. Then you can see them listed under the *Application theme* setting.

## [EFL-based applications]

[EFL](https://packages.gentoo.org/packages/dev-libs/efl) and [python-efl](https://packages.gentoo.org/packages/dev-python/python-efl) offer developers everything needed to develop eye-candy applications that integrate into Enlightenment WM. Here are few of them,

-   [ecrire](https://packages.gentoo.org/packages/app-editors/ecrire) A simple Notepad-like text editor using EFL
-   [Edi](https://packages.gentoo.org/packages/dev-util/edi) An EFL-based IDE
-   [entice](https://packages.gentoo.org/packages/media-gfx/entice) A simple image viewer based on EFL
-   [Ephoto](https://packages.gentoo.org/packages/media-gfx/ephoto) Enlightenment image viewer written with EFL
-   [rage](https://packages.gentoo.org/packages/media-video/rage) Video and audio player written using EFL
-   [Econnman](https://packages.gentoo.org/packages/net-misc/econnman) ConnMan User Interface for Enlightenment
-   [Evisum](https://packages.gentoo.org/packages/sys-process/evisum) System and process monitor written with EFL
-   [terminology](https://packages.gentoo.org/packages/x11-terms/terminology) Feature rich terminal emulator
-   [e-flat-theme](https://packages.gentoo.org/packages/x11-themes/e-flat-theme) A modern, flat theme for Enlightenment
-   [e-gtk-theme](https://packages.gentoo.org/packages/x11-themes/e-gtk-theme) A GTK theme to match Enlightenment WM\'s default theme

\

** Note**\
Anyone can add software they use via [the proxy-maint project](https://wiki.gentoo.org/wiki/Project:Proxy_Maintainers "Project:Proxy Maintainers"). Please do so. [A short list of external applications](https://phab.enlightenment.org/w/). And [some python-efl applications](https://phab.enlightenment.org/w/projects/python_bindings_for_efl/).

## [Troubleshooting]

### [Applications requiring system tray not working properly]

Older applications still using xembed systray instead of appindicator may not work properly (Dropbox for example). Solution is to install a stand-alone system tray program, such as [stalonetray](https://packages.gentoo.org/packages/x11-misc/stalonetray).

### [Black window contents]

If windows with completely black contents appear (most likely with the nvidia proprietary driver and Enlightenment 0.20.5 or 0.20.6), follow these steps:

-   Log out from Xorg.
-   Set `E_COMP_ENGINE=sw`, for example in [\~/.xinitrc]:

[FILE] **`~/.xinitrc`**

    export E_COMP_ENGINE=sw
    exec dbus-launch --exit-with-session enlightenment_start

Alternatively, set the variable in the [/etc/environment] file:

-   Start X.
-   Go to Settings-\>Composite-\>Advanced-\>Rendering and disable \"Texture from pixmap\".
-   Then remove \"export E_COMP_ENGINE=sw\" from [\~/.xinitrc] and log out/in to get accelerated rendering again.

For more information see [this bug report](https://phab.enlightenment.org/T3030).

### [][\"No opengl engines found\" with nvidia-drivers]

With latest releases of mesa and xorg-1.20, [efl](https://packages.gentoo.org/packages/dev-libs/efl) can look for [libGL.so] from a wrong place. This results in Enlightenment\'s gl-engine not using opengl backend. This can be fixed with [patchelf](https://packages.gentoo.org/packages/dev-util/patchelf) utility.

Identify where the [libGL.so] shared object is installed, usually [/usr/lib/opengl/nvidia/lib/libGL.so]. Then use patchelf to modify [efl](https://packages.gentoo.org/packages/dev-libs/efl)\'s gl engine,

`user `[`$`]`patchelf --set-rpath /usr/lib/opengl/nvidia/lib/ /usr/lib64/evas/modules/engines/gl_x11/v-1.20/module.so`

And relog. Paths depend on system architechture. This needs to be done once, or everytime [efl](https://packages.gentoo.org/packages/dev-libs/efl) is re-installed.

### [Use systemd user session to select the window manager]

When compiled with `systemd` USE flag enabled, Enlightenment installs a systemd service file to [/usr/lib/systemd/user/graphical-session.target] that can be used to spawn a graphical user session. This file however has `Requires=xorg.target` which requires [set up xorg as a systemd service](https://wiki.archlinux.org/index.php/Systemd/User#Xorg_as_a_systemd_user_service) to be set manually.

### [][\"build error: conflicting types for 'GLintptr'\"]

Most likely due to newer Mesa dropping openGL support for older graphics cards. Try building dev-libs/efl with `gles2 -opengl` to get GL working again.

### [][\"build error: undefined symbol: \_EFL_GFX_PATH_CHANGED\"]

An unfortunate build error that\'s caused by existing libraries. There is usually a more detailed error, like: \"/usr/lib64/libector.so.1: undefined symbol: \_EFL_GFX_PATH_CHANGED\". In this case, remove any existing installation of dev-libs/efl and the offending library.

** Important**\
It is wise to log out from Enlightenment before removing efl. Removing efl while using Enlightenment might cause Enlightenment to act weirdly and in the worst case lock up. If this occurs, the build failure will not be visible. Log in to TTY or some other WM/DE while re-installing efl.

`root `[`#`]`emerge -C --nodeps dev-libs/efl`

`root `[`#`]`rm /usr/lib64/libector.so.1`

`root `[`#`]`emerge --ask dev-libs/efl`

See more in [[[bug #651890]](https://bugs.gentoo.org/show_bug.cgi?id=651890)[]].

### [Xorg touchpad config ignored]

Since 0.25, any touchpad settings configured via xorg [.conf] files seem to be ignored. If tap-to-click or double-tap-to-drag does not work anymore after a recent update, this most likely is the case.

Enlightenment takes care of touchpad settings itself now, it seems.

Use the mouse settings (Everything launcher, type \"Mouse\"; or use Settings \> Input \> Mouse) and navigate to the \"touchpad\" tab to find the settings probably set in [/etc/X11/xorg.conf.d/\*.conf] before and manually configure them.

### [Debugging]

When attempting to move config files away and Enlightenment still does not work, debug the problem by typing the following and reading the log file:

`user `[`$`]`enlightenment_start 2>&1 | tee logthing.txt`

It is useful when making a bug report to [bugs.gentoo.org](https://bugs.gentoo.org/) or upstream\'s [Phabricator](https://phab.enlightenment.org/project/). If the log file does not imply clear errors, Enlightenment may need started with debugging tools such as [[[dev-debug/gdb]](https://packages.gentoo.org/packages/dev-debug/gdb)[]], [[[dev-debug/strace]](https://packages.gentoo.org/packages/dev-debug/strace)[]], or [[[dev-debug/valgrind]](https://packages.gentoo.org/packages/dev-debug/valgrind)[]].

`user `[`$`]`E_START=1 strace enlightenment_start 2>&1 | tee logthing.txt`

### [][Can\'t change keyboard layout]

When having trouble changing the keyboard layout to a different language, install the packages [[[x11-libs/libxklavier]](https://packages.gentoo.org/packages/x11-libs/libxklavier)[]] and [[[x11-apps/setxkbmap]](https://packages.gentoo.org/packages/x11-apps/setxkbmap)[]].

## [Screenshots]

-   ::::::
    ::::
    :::
    [![E 0.25.png](/images/thumb/6/6e/E_0.25.png/400px-E_0.25.png)](https://wiki.gentoo.org/wiki/File:E_0.25.png)
    :::
    ::::

    ::: gallerytext
    :::
    ::::::

<!-- -->

-   ::::::
    ::::
    :::
    [![E-23-6 m.png](/images/thumb/8/80/E-23-6_m.png/400px-E-23-6_m.png)](https://wiki.gentoo.org/wiki/File:E-23-6_m.png)
    :::
    ::::

    ::: gallerytext
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![E-5fb32e628b6b31.29748375.jpg](/images/thumb/f/f8/E-5fb32e628b6b31.29748375.jpg/400px-E-5fb32e628b6b31.29748375.jpg)](https://wiki.gentoo.org/wiki/File:E-5fb32e628b6b31.29748375.jpg)
    :::
    ::::

    ::: gallerytext
    :::
    ::::::

<!-- -->

-   ::::::
    ::::
    :::
    [![1 m.png](/images/thumb/b/b1/1_m.png/400px-1_m.png)](https://wiki.gentoo.org/wiki/File:1_m.png)
    :::
    ::::

    ::: gallerytext
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![E-23-2 m.png](/images/thumb/0/0b/E-23-2_m.png/400px-E-23-2_m.png)](https://wiki.gentoo.org/wiki/File:E-23-2_m.png)
    :::
    ::::

    ::: gallerytext
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![E23-4 m.png](/images/thumb/8/8a/E23-4_m.png/400px-E23-4_m.png)](https://wiki.gentoo.org/wiki/File:E23-4_m.png)
    :::
    ::::

    ::: gallerytext
    :::
    ::::::

<!-- -->

-   ::::::
    ::::
    :::
    [![E22-1.png](/images/thumb/f/f8/E22-1.png/400px-E22-1.png)](https://wiki.gentoo.org/wiki/File:E22-1.png)
    :::
    ::::

    ::: gallerytext
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![E22-2.png](/images/thumb/0/03/E22-2.png/400px-E22-2.png)](https://wiki.gentoo.org/wiki/File:E22-2.png)
    :::
    ::::

    ::: gallerytext
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![E22-3.png](/images/thumb/8/84/E22-3.png/400px-E22-3.png)](https://wiki.gentoo.org/wiki/File:E22-3.png)
    :::
    ::::

    ::: gallerytext
    :::
    ::::::

<!-- -->

-   ::::::
    ::::
    :::
    [![E-5.png](/images/thumb/4/4a/E-5.png/400px-E-5.png)](https://wiki.gentoo.org/wiki/File:E-5.png)
    :::
    ::::

    ::: gallerytext
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![Evisum-1.png](/images/thumb/9/92/Evisum-1.png/384px-Evisum-1.png)](https://wiki.gentoo.org/wiki/File:Evisum-1.png)
    :::
    ::::

    ::: gallerytext
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![Evisum-2.png](/images/thumb/1/1e/Evisum-2.png/384px-Evisum-2.png)](https://wiki.gentoo.org/wiki/File:Evisum-2.png)
    :::
    ::::

    ::: gallerytext
    :::
    ::::::

## [See also]

-   [Desktop environment](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") --- provides a list of desktop environments available in Gentoo.
-   [Recommended applications](https://wiki.gentoo.org/wiki/Recommended_applications "Recommended applications") --- applications recommended for use in a graphical environment ([X11](https://wiki.gentoo.org/wiki/Xorg "Xorg"), [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland"))

## [External resources]

-   [E Window Manager Faq](https://phab.enlightenment.org/w/e_window_manager_faq/)
-   [GTK Theme to match the new dark default theme](https://github.com/tokiclover/e-gtk-theme)
-   [Homepage](https://enlightenment.org)
-   [Wikipedia article](https://en.wikipedia.org/wiki/Enlightenment_(window_manager) "wikipedia:Enlightenment (window manager)")
-   [Arch linux Wiki page](https://wiki.archlinux.org/index.php/enlightenment)
-   [Sending patches upstream](https://phab.enlightenment.org/w/arcanist/)
-   [pling.com theme repository for Enlightenment](https://www.pling.com/browse/cat/145/order/latest/)