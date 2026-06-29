**Resources**

[[]][Home](https://www.freedesktop.org/wiki/Software/dbus/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/D-Bus "wikipedia:D-Bus")

[[]][Official documentation](https://dbus.freedesktop.org/doc/dbus-specification.html)

[[]][GitWeb](https://cgit.freedesktop.org/dbus/dbus/)

**D-Bus** is an interprocess communication (IPC) system for software applications. Software makes use of D-Bus to communicate information between services.

** Important**\
There are two distinct D-Bus buses: the *system bus* and the *session bus*. The *system* bus is for messages related to the system as a whole, e.g. hardware connects and disconnects. The *session* bus, on the other hand, is for messages related to a specific user session, e.g. an X or Wayland session. The [dbus] service provided by OpenRC and systemd only provides the *system* bus, not a *session* bus.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [The system bus: the dbus service]](#The_system_bus:_the_dbus_service)
        -   [[2.2.1] [OpenRC]](#OpenRC)
    -   [[2.3] [The session bus]](#The_session_bus)
-   [[3] [Usage]](#Usage)
-   [[4] [Troubleshooting]](#Troubleshooting)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation]

### [USE flags]

Portage knows the global `dbus` USE flag for enabling support for D-Bus in other packages. Enabling this flag will pull in [[[sys-apps/dbus]](https://packages.gentoo.org/packages/sys-apps/dbus)[]] automatically. This is the default for *desktop* [profiles](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)"):

[FILE] **`/etc/portage/make.conf`Enabling D-Bus globally**

    USE="dbus"

### [USE flags for] [sys-apps/dbus](https://packages.gentoo.org/packages/sys-apps/dbus) [[]] [A message bus system, a simple way for applications to talk to each other]

  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`X`](https://packages.gentoo.org/useflags/X)                       Add support for X11
  [`apparmor`](https://packages.gentoo.org/useflags/apparmor)         Enable support for the AppArmor application security system
  [`audit`](https://packages.gentoo.org/useflags/audit)               Enable support for Linux audit subsystem using sys-process/audit
  [`debug`](https://packages.gentoo.org/useflags/debug)               Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`doc`](https://packages.gentoo.org/useflags/doc)                   Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`elogind`](https://packages.gentoo.org/useflags/elogind)           Enable session tracking via sys-auth/elogind
  [`selinux`](https://packages.gentoo.org/useflags/selinux)           !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`static-libs`](https://packages.gentoo.org/useflags/static-libs)   Build static versions of dynamic libraries as well
  [`systemd`](https://packages.gentoo.org/useflags/systemd)           Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`test`](https://packages.gentoo.org/useflags/test)                 Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`valgrind`](https://packages.gentoo.org/useflags/valgrind)         Enable annotations for accuracy. May slow down runtime slightly. Safe to use even if not currently using dev-debug/valgrind
  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-19 03:51] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

After setting the `dbus` global USE flag be sure to update the system using the `--changed-use` option:

`root `[`#`]`emerge --ask --changed-use --deep @world`

## [Configuration]

### [Files]

The main configuration files include:

-   [/usr/share/dbus-1/system.conf] for the system bus
-   [/usr/share/dbus-1/session.conf] for the session bus

### [The system bus: the `dbus` service]

A D-Bus service, such as the OpenRC service described below, typically provides the *system* bus, but **not** a *session* bus. Depending on system configuration, a *session bus* may need to be manually started in order for certain \'desktop\' functionality to be available. For further details, refer to [the session bus](#The_session_bus), below.

#### [OpenRC]

After configuration step, start the D-Bus *system bus* with:

`root `[`#`]`/etc/init.d/dbus start`

To start the D-Bus system bus at boot time, add it the default run level:

`root `[`#`]`rc-update add dbus default`

** Tip**\
Even without adding D-Bus to the default runlevel it often will get started by D-Bus dependent services. This should explain why D-Bus mysteriously gets started even though it has not been formally added to a system runlevel.

### [The session bus]

If using a desktop environment such as KDE or GNOME, a session bus should be created automatically. More generally, however, a session bus might not get created automatically. In particular, this is the case when using [startx] / [.xinitrc].

To check whether a session bus is available within the X or Wayland session, open a terminal in that session and do:

`user `[`$`]`echo $DBUS_SESSION_BUS_ADDRESS`

This should output a string beginning with `unix:path=`, e.g. `unix:path=/tmp/dbus-a77380e2b9,guid=90c8f55c7e7745be8f35a31b977085fc`. If no such string is displayed, there is no D-Bus session bus visible to the session.

Executing a window manager, like i3 or bspwm, via [dbus-run-session] or [dbus-launch] grants a D-Bus session to the X or Wayland session.

** Warning**\
When *not using a login manager*, **security issues arise when relying on a screen lock program**. Lock programs only prevent access to the running X session and the tty where X was launched may still be accessible. This makes it possible to kill X and gain access to logged-in user\'s shell. **Make sure the X session is launched with the [exec] command** to ensure a user is logged out if X is terminated for any reason.

[FILE] **`~/.xinitrc`**

    exec dbus-launch --exit-with-session i3

Important things to note:

1.  The session bus thus created *will only be visible to programs created as child processes of the program launched by [dbus-launch]*. Thus, any programs needing access to the session bus will need to be started via the startup procedure of that program (e.g. for i3, via [\~/.config/i3/config]).
2.  The use of [exec] here means that *no subsequent lines of the [.xinitrc] file will be executed*. [exec] is typically a shell builtin; for details, refer to the documentation for the shell being used to run the [.xinitrc] script. This is not the same behavior as some might expect from e.g. Sway, where the rest of the file/script continues after *exec*.

## [Usage]

Some useful commands include:

-   [dbus-monitor \--system] - To monitor the activities in the system bus.
-   [dbus-monitor \--session] - To monitor the activities in the session bus.
-   [dbus-send \<PARAMETER\>] - To send a message. See the dbus-send [man page](https://wiki.gentoo.org/wiki/Man_page "Man page") ([man dbus-send]) for more information.

To view dbus services:

`user `[`$`]`dbus-send --print-reply --dest=org.freedesktop.DBus /org/freedesktop/DBus org.freedesktop.DBus.ListNames`

Users of systemd or elogind can use [[[busctl(1)]](https://man.archlinux.org/man/busctl.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] to list objects on a given bus, e.g.:

`user `[`$`]`busctl --user tree `

    Service org.freedesktop.DBus:
    └─/org/freedesktop/DBus

    Service org.freedesktop.Notifications:
    └─/org
      └─/org/freedesktop
        └─/org/freedesktop/Notifications
    ...

To shutdown and reboot as a regular user when using elogind:

`user `[`$`]`dbus-send --system --print-reply --dest=org.freedesktop.login1 /org/freedesktop/login1 org.freedesktop.login1.Manager.PowerOff boolean:false`

`user `[`$`]`dbus-send --system --print-reply --dest=org.freedesktop.login1 /org/freedesktop/login1 org.freedesktop.login1.Manager.Reboot boolean:false`

Changing the last argument to `boolean:true` should make polkit interactively ask the user for authentication credentials if it needs to.

The [[[dev-debug/d-spy]](https://packages.gentoo.org/packages/dev-debug/d-spy)[]] package provides a GUI to explore available D-Bus services and objects on the system and session buses, and to call methods of D-Bus interfaces.

## [Troubleshooting]

Use the [dbus-monitor] command to monitor the buses. Errors are also redirected to the syslog ([/var/log/messages]).

## [See also]

-   [Eudev](https://wiki.gentoo.org/wiki/Eudev "Eudev") --- a fork of [udev](https://wiki.gentoo.org/wiki/Udev "Udev"), [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd")\'s [device file](https://wiki.gentoo.org/wiki/Device_file "Device file") manager for the Linux kernel.
-   [Udev](https://wiki.gentoo.org/wiki/Udev "Udev") --- [systemd\'s](https://wiki.gentoo.org/wiki/Systemd "Systemd") device manager for the Linux kernel.

## [External resources]

-   [Introduction to D-Bus](https://www.freedesktop.org/wiki/IntroductionToDBus/) (freedesktop.org)
-   [D-Bus tutorial](https://dbus.freedesktop.org/doc/dbus-tutorial.html) (freedesktop.org)
-   [D-Bus](https://wiki.archlinux.org/index.php/D-Bus) (Arch Wiki)