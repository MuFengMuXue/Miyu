[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Xwayland&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://wayland.freedesktop.org/xserver.html)

[[]][Package information](https://packages.gentoo.org/packages/x11-base/xwayland)

[Xwayland] is an X server for running X clients under [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland"). It is built from a collection of patches to the X.Org server codebase, created and maintained by Wayland developers.

Not all software supports, or plans to support, running under Wayland. Wayland compositors can use Xwayland to allow use of such software within their environment.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [The DISPLAY environment variable]](#The_DISPLAY_environment_variable)
-   [[3] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [x11-base/xwayland](https://packages.gentoo.org/packages/x11-base/xwayland) [[]] [Standalone X server running under Wayland]

  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`libei`](https://packages.gentoo.org/useflags/libei)             Enable emulated input using dev-libs/libei
  [`selinux`](https://packages.gentoo.org/useflags/selinux)         !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`systemd`](https://packages.gentoo.org/useflags/systemd)         Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`unwind`](https://packages.gentoo.org/useflags/unwind)           Enable libunwind usage for backtraces
  [`xcsecurity`](https://packages.gentoo.org/useflags/xcsecurity)   Build Security extension
  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-30 20:45] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

Certain packages need to be built with certain USE flags in order to utilize Xwayland:

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------
  Package                                                                                                                                                                                                                                                                                                                                                                              USE flag
  [[[dev-libs/weston]](https://packages.gentoo.org/packages/dev-libs/weston)[]]                  `xwayland`
  [[[gui-libs/wlroots]](https://packages.gentoo.org/packages/gui-libs/wlroots)[]]               `X`
  [[[gui-wm/sway]](https://packages.gentoo.org/packages/gui-wm/sway)[]]                              `X`
  [[[x11-wm/enlightenment]](https://packages.gentoo.org/packages/x11-wm/enlightenment)[]]   `xwayland`
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------

### [Emerge]

`root `[`#`]`emerge --ask x11-base/xwayland`

## [Usage]

Normally Xwayland shouldn\'t need to be started manually; it should be started on-demand by the running Wayland compositor.

Once started, there should be an \"Xwayland\" entry in the list of running processes, e.g.:

    Xwayland :0 -rootless -core -terminate -listenfd 26 -listenfd 27 -displayfd 60 -wm 57

[[[Xwayland(1)]](https://man.archlinux.org/man/Xwayland.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] accepts the same command-line arguments as [[[Xserver(1)]](https://man.archlinux.org/man/Xserver.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")], followed by various arguments specifically handled by Xwayland. In the above example, the following arguments are [[[Xserver(1)]](https://man.archlinux.org/man/Xserver.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] arguments:

-   `:0`: Request \"0\" as the display number for the server. Refer to the discussion about the `-displayfd` argument, below, regarding situations where a different display number is required.

<!-- -->

-   `-core`: \"\[C\]auses the server to generate a core dump on fatal errors.\"

<!-- -->

-   `-displayfd 60`: \"Rather than specify a display number, the X server will attempt to listen on successively higher display numbers, and upon finding a free one, will write the display number back on this file descriptor as a newline-terminated string.\"

<!-- -->

-   `-terminate`: \"\[C\]auses the server to terminate at server reset, instead of continuing to run.\"

The remaining arguments are handled by [[[Xwayland(1)]](https://man.archlinux.org/man/Xwayland.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]:

-   `-rootless`: \"Run Xwayland rootless, so that X clients integrate seamlessly with Wayland clients in a Wayland desktop. That requires the Wayland server to be an X window manager as well.\"

<!-- -->

-   `-listenfd 26`, `-listenfd 27`: \"Add given fd as a listen socket. This option is used by the Wayland server to pass Xwayland the socket where X clients connect.\"

<!-- -->

-   `-wm 57`: \"\[U\]sed by the Wayland server to pass Xwayland the socket where the X window manager client connects\".

### [The DISPLAY environment variable]

In general, as the compositor is typically responsible for starting an Xwayland instance, it also needs to set the X `DISPLAY` environment variable appropriately - such as at the start of a session - for use by client applications. If a particular compositor does not seem to be doing so, please refer to the compositor\'s documentation and/or support communities.

## [See also]

-   [[[Xserver(1)]](https://man.archlinux.org/man/Xserver.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page
-   [[[Xwayland(1)]](https://man.archlinux.org/man/Xwayland.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page