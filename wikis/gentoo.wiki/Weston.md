**Resources**

[[]][Home](https://wayland.freedesktop.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Wayland_(display_server_protocol)#WESTON "wikipedia:Wayland (display server protocol)")

[[]][GitWeb](https://cgit.freedesktop.org/wayland/weston)

**Weston** is a reference implementation of a [Wayland compositor](https://wiki.gentoo.org/wiki/Wayland_compositor "Wayland compositor"). It is part of the Wayland project and can run as an [X](https://wiki.gentoo.org/wiki/X "X") client or under Linux Kernel Mode Setting (KMS).

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [weston without systemd (weston-9.0.0-r1)]](#weston_without_systemd_.28weston-9.0.0-r1.29)
    -   [[2.2] [weston without systemd (weston-10.0.0)]](#weston_without_systemd_.28weston-10.0.0.29)
-   [[3] [See also]](#See_also)
-   [[4] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [dev-libs/weston](https://packages.gentoo.org/packages/dev-libs/weston) [[]] [Wayland reference compositor]

  ------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+X`](https://packages.gentoo.org/useflags/+X)                                       Add support for X11
  [`+desktop`](https://packages.gentoo.org/useflags/+desktop)                           Enable the desktop shell
  [`+drm`](https://packages.gentoo.org/useflags/+drm)                                   Enable drm compositor support
  [`+gles2`](https://packages.gentoo.org/useflags/+gles2)                               Enable the GLESv2 renderer, not just the x11-libs/pixman-based software fallback
  [`+resize-optimization`](https://packages.gentoo.org/useflags/+resize-optimization)   Increase performance, allocate more RAM. Recommended to disable on Raspberry Pi
  [`+suid`](https://packages.gentoo.org/useflags/+suid)                                 Enable setuid root program(s)
  [`editor`](https://packages.gentoo.org/useflags/editor)                               Install wayland-editor example application
  [`examples`](https://packages.gentoo.org/useflags/examples)                           Install examples, usually source code
  [`fullscreen`](https://packages.gentoo.org/useflags/fullscreen)                       Enable fullscreen shell
  [`headless`](https://packages.gentoo.org/useflags/headless)                           Headless backend and a noop renderer, mainly for testing purposes
  [`ivi`](https://packages.gentoo.org/useflags/ivi)                                     Enable the IVI shell
  [`jpeg`](https://packages.gentoo.org/useflags/jpeg)                                   Add JPEG image support
  [`kiosk`](https://packages.gentoo.org/useflags/kiosk)                                 Enable the kiosk shell
  [`lcms`](https://packages.gentoo.org/useflags/lcms)                                   Add lcms support (color management engine)
  [`lua`](https://packages.gentoo.org/useflags/lua)                                     Enable Lua scripting support
  [`pipewire`](https://packages.gentoo.org/useflags/pipewire)                           Enable virtual remote output with Pipewire on DRM backend
  [`rdp`](https://packages.gentoo.org/useflags/rdp)                                     Enable Remote Desktop Protocol compositor support
  [`remoting`](https://packages.gentoo.org/useflags/remoting)                           Enable plugin to stream output to remote hosts using media-libs/gstreamer
  [`screen-sharing`](https://packages.gentoo.org/useflags/screen-sharing)               Enable screen-sharing through RDP
  [`systemd`](https://packages.gentoo.org/useflags/systemd)                             Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`test`](https://packages.gentoo.org/useflags/test)                                   Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`vnc`](https://packages.gentoo.org/useflags/vnc)                                     Enable VNC (remote desktop viewer) support
  [`vulkan`](https://packages.gentoo.org/useflags/vulkan)                               Add support for 3D graphics and computing via the Vulkan cross-platform API
  [`wayland-compositor`](https://packages.gentoo.org/useflags/wayland-compositor)       Enable Wayland compositor support
  [`webp`](https://packages.gentoo.org/useflags/webp)                                   Add support for the WebP image format
  [`xwayland`](https://packages.gentoo.org/useflags/xwayland)                           Enable ability support native X11 applications
  ------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-16 14:40] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask dev-libs/weston`

## [Usage]

The Weston compositor is a minimal and fast compositor and is suitable for many embedded and mobile use cases.

Enable the `examples` USE flag for building example applications like [weston-image] or [weston-view].

Weston is configured on a local level with the [\~/.config/weston.ini] file (cf. [[man 5 weston.ini]]).

** Note**\
Follow the instructions below if your environment does not define `XDG_RUNTIME_DIR`. Weston creates its unix socket file in the directory specified by this environment variable and clients use the same variable to find that socket. ^[\[1\]](#cite_note-1)^

The *environment variable* can be defined in the usual configuration files. For example, if [Larry the cow (Larry) ](https://wiki.gentoo.org/wiki/User:Larry "User:Larry") sets `XDG_RUNTIME_DIR` variable in his [Bash](https://wiki.gentoo.org/wiki/Bash "Bash") shell\'s configuration file and he has chosen that the directory will be in [/tmp].

[FILE] **`/home/larry/.bash_profile`Set `XDG_RUNTIME_DIR`**

    #!/bin/bash
    if test -z "$"; then
        export XDG_RUNTIME_DIR=/tmp/$-runtime-dir
        if ! test -d "$"; then
            mkdir "$"
            chmod 0700 "$"
        fi
    fi

To launch the compositor as a standalone display server (i) enable systemd session support for weston-launch (by USE=systemd), (ii) or users without systemd are referred to the section [#weston-launch without systemd](#weston-launch_without_systemd) below.

On a VT (outside of X), launch Weston with the DRM backend:

** Note**\
The weston-launch command has been deprecated in version 10.0.0 and is no longer available unless weston is build with the -Ddeprecated-weston-launch=true. Instead use *weston*

`user `[`$`]`weston-launch`

Ditto, with XWayland support:

`user `[`$`]`weston-launch -- --xwayland`

Nest a weston instance \"wayland-1\" in another Weston \"wayland-0\":

`user `[`$`]`WAYLAND_DISPLAY=wayland-0 weston -Swayland-1 `

From an X terminal, launch Weston with the x11 backend:

`user `[`$`]`weston`

### [][weston without systemd (weston-9.0.0-r1)]

As of Nov 2021 (weston-9.0.0-r1), users without systemd need the workaround below. As solved in [[[bug #479468]](https://bugs.gentoo.org/show_bug.cgi?id=479468)[]], weston-9999 introduced the USE flag \"seatd\", enabling elogind as a substitute of systemd.

You have to create the group named \"weston-launch\", and add the user to that group:

`root `[`#`]`groupadd weston-launch `

`root `[`#`]`usermod -a -G weston-launch `*`user-name`*` `

Notice: This might be unbelievable, but true: The group name \"weston-launch\" is hardcoded, and the command weston-launch checks if the user belongs to it. It is *not* relevant e.g. a device file is writable to a user.

### [][weston without systemd (weston-10.0.0)]

Users without systemd can use either [seatd](https://wiki.gentoo.org/wiki/Seatd "Seatd") or [elogind](https://wiki.gentoo.org/wiki/Elogind "Elogind"). Either service must be running before starting weston.

For [seatd](https://wiki.gentoo.org/wiki/Seatd "Seatd") the user running weston must be a member of the video group, otherwise the unix-socket */run/seatd.sock* for seatd access is not available

## [See also]

-   [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland") --- a [communication protocol](https://en.wikipedia.org/wiki/communication_protocol "wikipedia:communication protocol") between a [display server](https://en.wikipedia.org/wiki/display_server "wikipedia:display server") and its clients
-   [Xorg](https://wiki.gentoo.org/wiki/Xorg "Xorg") --- an open source implementation of the [X server](https://wiki.gentoo.org/wiki/X_server "X server").

## [References]

1.  [[[↑](#cite_ref-1)] [[https://wayland.freedesktop.org/building.html](https://wayland.freedesktop.org/building.html)]]