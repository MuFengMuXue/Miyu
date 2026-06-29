[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Wlroots&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://gitlab.freedesktop.org/wlroots/wlroots)

[[]][Official documentation](https://gitlab.freedesktop.org/wlroots/wlroots/-/wikis/home)

[[]][Package information](https://packages.gentoo.org/packages/gui-libs/wlroots)

**wlroots** is a library providing pluggable, composable, unopinionated modules for building a Wayland compositor. As described by the project README:

> -   wlroots provides backends that abstract the underlying display and input hardware, including KMS/DRM, libinput, Wayland, X11, and headless backends, plus any custom backends you choose to write, which can all be created or destroyed at runtime and used in concert with each other.
> -   wlroots provides unopinionated, mostly standalone implementations of many Wayland interfaces, both from wayland.xml and various protocol extensions. We also promote the standardization of portable extensions across many compositors.
> -   wlroots provides several powerful, standalone, and optional tools that implement components common to many compositors, such as the arrangement of outputs in physical space.
> -   wlroots provides an Xwayland abstraction that allows you to have excellent Xwayland support without worrying about writing your own X11 window manager on top of writing your compositor.
> -   wlroots provides a renderer abstraction that simple compositors can use to avoid writing GL code directly, but which steps out of the way when your needs demand custom rendering code.

The [Wayland protocols](https://wayland.app/protocols/) currently supported by wlroots can be found in [the [types] directory of the wlroots repository](https://gitlab.freedesktop.org/wlroots/wlroots/-/tree/master/types?ref_type=heads).

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Usage]](#Usage)
-   [[2] [See also]](#See_also)
-   [[3] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [gui-libs/wlroots](https://packages.gentoo.org/packages/gui-libs/wlroots) [[]] [Pluggable, composable, unopinionated modules for building a Wayland compositor]

  ------------------------------------------------------------------- -----------------------------------------------------------------------------
  [`+drm`](https://packages.gentoo.org/useflags/+drm)                 Enable Direct Rendering Management
  [`+libinput`](https://packages.gentoo.org/useflags/+libinput)       Enable support for input devices via dev-libs/libinput
  [`+session`](https://packages.gentoo.org/useflags/+session)         Enable session support (is required for DRM and libinput)
  [`X`](https://packages.gentoo.org/useflags/X)                       Enable support for X11 applications (XWayland)
  [`lcms`](https://packages.gentoo.org/useflags/lcms)                 Add lcms support (color management engine)
  [`liftoff`](https://packages.gentoo.org/useflags/liftoff)           Enable support for libliftoff KMS plane backend
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)     Verify upstream signatures on distfiles
  [`vulkan`](https://packages.gentoo.org/useflags/vulkan)             Add support for 3D graphics and computing via the Vulkan cross-platform API
  [`x11-backend`](https://packages.gentoo.org/useflags/x11-backend)   Enable support for handling input/output devices through x11-libs/libxcb
  [`xcb-errors`](https://packages.gentoo.org/useflags/xcb-errors)     Better error reporting when using xwayland
  ------------------------------------------------------------------- -----------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-05 03:35] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Normally wlroots does not need to be installed manually; it should be pulled in as a dependency when installing a wlroots-based compositor.

### [Usage]

Wayland compositors currently based on wlroots include:

  ---------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Name                                                                                     Package                                                                                                                                                                                                                                                                                                                                                                                                                                     Type       Description
  [Cage](https://github.com/cage-kiosk/cage)               [[[gui-wm/cage::guru]](https://gpo.zugaina.org/Overlays/guru/gui-wm/cage)[]]                                        Kiosk      \[Beta\] Kiosk based compositor for displaying a single fullscreen application (in GURU overlay)
  [Cagebreak](https://github.com/project-repo/cagebreak)   [[[gui-wm/cagebreak::wayland-desktop]](https://gpo.zugaina.org/Overlays/wayland-desktop/gui-wm/cagebreak)[]]   Tiling     \[Beta\] Tiling compositor inspired by RatPoison (in wayland-desktop overlay)
  [DWL](https://codeberg.org/dwl/dwl)                      [[[gui-wm/dwl]](https://packages.gentoo.org/packages/gui-wm/dwl)[]]                                                                                        Tiling     \[Unstable\] DWM clone
  [Kiwmi](https://github.com/buffet/kiwmi)                 [[[gui-wm/kiwmi::wayland-desktop]](https://gpo.zugaina.org/Overlays/wayland-desktop/gui-wm/kiwmi)[]]               Stacking   \[Unstable\] Fully programmable compositor configurable with Lua (in wayland-desktop overlay)
  [Labwc](https://wiki.gentoo.org/wiki/Labwc "Labwc")                                      [[[gui-wm/labwc::wayland-desktop]](https://gpo.zugaina.org/Overlays/wayland-desktop/gui-wm/labwc)[]]               Stacking   \[Unstable\] OpenBox clone (in wayland-desktop overlay)
  [River](https://wiki.gentoo.org/wiki/River "River")                                      [[[gui-wm/river::wayland-desktop]](https://gpo.zugaina.org/Overlays/wayland-desktop/gui-wm/river)[]]               Tiling     \[Unstable\] Dynamic tiling compositor, inspired by DWM and bspwm (in wayland-desktop overlay)
  [Sway](https://wiki.gentoo.org/wiki/Sway "Sway")                                         [[[gui-wm/sway]](https://packages.gentoo.org/packages/gui-wm/sway)[]]                                                                                     Tiling     [[[x11-wm/i3]](https://packages.gentoo.org/packages/x11-wm/i3)[]] clone
  [Waybox](https://github.com/wizbright/waybox)            [[[gui-wm/waybox::wayland-desktop]](https://gpo.zugaina.org/Overlays/wayland-desktop/gui-wm/waybox)[]]            Stacking   \[Unstable\] OpenBox clone (in wayland-desktop overlay)
  [Wayfire](https://wiki.gentoo.org/wiki/Wayfire "Wayfire")                                [[[gui-wm/wayfire]](https://packages.gentoo.org/packages/gui-wm/wayfire)[]]                                                                            Stacking   Beautiful, eye candy compositor inspired by [Compiz](https://wiki.gentoo.org/wiki/Compiz "Compiz")
  [Woodland](https://github.com/DiogenesN/woodland)        [[[gui-wm/woodland]](https://packages.gentoo.org/packages/gui-wm/woodland)[]]                                                                         Stacking   A Wayland window-stacking compositor.
  ---------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For information about environment variables read by wlroots, refer to [this file in the wlroots documentation](https://gitlab.freedesktop.org/wlroots/wlroots/-/blob/master/docs/env_vars.md).

## [See also]

-   [Labwc](https://wiki.gentoo.org/wiki/Labwc "Labwc") --- a stacking [wlroots]-based [Wayland compositor](https://wiki.gentoo.org/wiki/Wayland_compositor "Wayland compositor"), inspired by [Openbox](https://wiki.gentoo.org/wiki/Openbox "Openbox")
-   [River](https://wiki.gentoo.org/wiki/River "River") --- a non-monolithic [wlroots]-based [Wayland compositor](https://wiki.gentoo.org/wiki/Wayland_compositor "Wayland compositor") written in [Zig](https://wiki.gentoo.org/wiki/Zig "Zig"). River allows for the use of a seperate compatible window manager to define window arrangement, window decorations, keybindings and other behavior
-   [Sway](https://wiki.gentoo.org/wiki/Sway "Sway") --- an open-source [wlroots]-based [Wayland compositor](https://wiki.gentoo.org/wiki/Wayland_compositor "Wayland compositor") that is designed to be compatible with the [i3](https://wiki.gentoo.org/wiki/I3 "I3") window manager.
-   [Wayfire](https://wiki.gentoo.org/wiki/Wayfire "Wayfire") --- Wayland compositor inspired by Compiz and based on [wlroots]

## [External resources]

-   [Architecture](https://gitlab.freedesktop.org/wlroots/wlroots/-/blob/master/docs/architecture.md) - A high-level overview of the wlroots design
-   [Introduction to wlroots](https://way-cooler.org/book/wlroots_introduction.html) - An introductory tutorial about using the wlroots library
-   [tinywl](https://gitlab.freedesktop.org/wlroots/wlroots/-/tree/master/tinywl) - A \"minimum viable product\" Wayland compositor based on wlroots
-   [Awesome wlroots](https://github.com/solarkraft/awesome-wlroots) - A list of tools and compositors around wlroots