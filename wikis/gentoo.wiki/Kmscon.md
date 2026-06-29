This page contains [[changes](https://wiki.gentoo.org/index.php?title=Kmscon&diff=1437303)] which are not marked for translation.

\

[] This article is a **work in progress**; treat its contents with caution - [Afstelnoj](https://wiki.gentoo.org/index.php?title=User:Afstelnoj&action=edit&redlink=1 "User:Afstelnoj (page does not exist)") ([talk](https://wiki.gentoo.org/index.php?title=User_talk:Afstelnoj&action=edit&redlink=1 "User talk:Afstelnoj (page does not exist)") \| [contribs](https://wiki.gentoo.org/wiki/Special:Contributions/Afstelnoj "Special:Contributions/Afstelnoj")).

**Resources**

[[]][Home](https://github.com/kmscon/kmscon)

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/kmscon)

**Kmscon** is a simple terminal emulator based on Linux kernel mode setting (KMS). It is an attempt to replace the in-kernel VT implementation with a userspace console. Kmscon addresses the limitations of the built-in virtual console by better support for non-Latin characters, better font rendering with anti-aliasing, more fluent DRM backed presentation and better compatibility with HiDPI.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [OpenRC]](#OpenRC)
    -   [[2.2] [systemd]](#systemd)
-   [[3] [Usage]](#Usage)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [OpenRC]](#OpenRC_2)
        -   [[4.1.1] [openrc-init]](#openrc-init)
        -   [[4.1.2] [sysvinit]](#sysvinit)
    -   [[4.2] [systemd]](#systemd_2)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Can\'t start X / Wayland session on kmscon]](#Can.27t_start_X_.2F_Wayland_session_on_kmscon)
    -   [[5.2] [Unable to switch between different TTYs]](#Unable_to_switch_between_different_TTYs)
-   [[6] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [sys-apps/kmscon](https://packages.gentoo.org/packages/sys-apps/kmscon) [[]] [KMS/DRM based virtual Console Emulator]

  ------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+drm`](https://packages.gentoo.org/useflags/+drm)           Enable Linux DRM for backend
  [`+fbdev`](https://packages.gentoo.org/useflags/+fbdev)       Enable Linux FBDev for backend
  [`+gles2`](https://packages.gentoo.org/useflags/+gles2)       Enable GLES 2.0 (OpenGL for Embedded Systems) support (independently of full OpenGL, see also: gles2-only)
  [`+pango`](https://packages.gentoo.org/useflags/+pango)       Enable pango font rendering
  [`debug`](https://packages.gentoo.org/useflags/debug)         Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`doc`](https://packages.gentoo.org/useflags/doc)             Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`elogind`](https://packages.gentoo.org/useflags/elogind)     Enable session tracking via sys-auth/elogind
  [`freetype`](https://packages.gentoo.org/useflags/freetype)   Enable freetype2 renderer
  [`systemd`](https://packages.gentoo.org/useflags/systemd)     Enable multiseat support via systemd
  [`test`](https://packages.gentoo.org/useflags/test)           Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-24 15:46] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask sys-apps/kmscon`

## [Configuration]

It is recommended that the `ERASECHAR` line in [/etc/login.defs] be commented out for proper backspace functionality at the kmscon login prompt. Refer to [this Github issue](https://github.com/dvdhrm/kmscon/issues/69#issuecomment-13827797) for details.

### [OpenRC]

The usage of kmscon on OpenRC is similar to agetty; the following script is based on [/etc/init.d/agetty].

[FILE] **`/etc/init.d/kmsconvt`**

    #!/sbin/openrc-run

    description="KMS System Console"
    supervisor="supervise-daemon"
    port="$"
    command=/usr/bin/kmscon
    command_args_foreground="--vt=$ --seats=seat0 --no-switchvt"
    pidfile="/run/$.pid"

    depend()

    start_pre()  cannot be started directly. You must create"
                    eerror "symbolic links to it for the ports you want to start"
                    eerror "kmscon on and add those to the appropriate runlevels."
                    return 1
            else
                    export EINFO_QUIET="$"
            fi
    }

    stop_pre() "
    }

`root `[`#`]`cd /etc/init.d `

`root `[`#`]`chmod +x ./kmsconvt `

`root `[`#`]`for n in $(seq 1 6); do ln -s kmsconvt kmsconvt.tty$n; rc-update add kmsconvt.tty$n default; done `

### [systemd]

`root `[`#`]`ln -s '/usr/lib/systemd/system/kmsconvt@.service' '/etc/systemd/system/autovt@.service'`

## [Usage]

** Note**\
Currently, the kmscon(1) and kmscon-launch-gui(1) man pages will not be installed unless the package\'s `doc` USE flag is enabled; refer to [[[bug #917051]](https://bugs.gentoo.org/show_bug.cgi?id=917051)[]] for details.

Refer to the [[[kmscon(1)]](https://man.archlinux.org/man/kmscon.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page for general information about usage.

GUI environments must be started via the [kmscon-launch-gui] script, e.g.:

`user `[`$`]`kmscon-launch-gui startx`

## [Removal]

Prior to removing kmscon, the system must be reconfigured to return to using agetty; a LiveCD may need to be used for this. Kmscon can then safely be removed.

** Warning**\
A VT implementation must always be set, otherwise softlock can occur after reboot. Ensure either agetty (the default) or kmscon is enabled before reboot.

### [OpenRC]

#### [openrc-init]

If you are using [openrc-init](https://wiki.gentoo.org/wiki/OpenRC/openrc-init "OpenRC/openrc-init"), you need：

`root `[`#`]`cd /etc/init.d `

`root `[`#`]`for n in $(seq 1 6); do rc-update del kmsconvt.tty$ default; cp agetty agetty.tty$ ; rc-update add agetty.tty$ default ; done `

#### [sysvinit]

TODO

### [systemd]

`root `[`#`]`systemctl disable autovt@ `

`root `[`#`]`ln -s '/usr/lib/systemd/system/getty@.service' '/etc/systemd/system/autovt@.service' `

## [Troubleshooting]

### [][Can\'t start X / Wayland session on kmscon]

An X / Wayland session can\'t be started directly on kmscon; a [Display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager") or [kmscon-launch-gui] must be used instead, e.g.:

`user `[`$`]`kmscon-launch-gui sway`

### [Unable to switch between different TTYs]

Check [/etc/kmscon/kmscon.conf] and verify that it includes:

[FILE] **`/etc/kmscon/kmscon.conf`**

    switchvt

## [See also]

-   [Terminal emulator](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator") --- emulates a video terminal within another display architecture (e.g. in [X](https://wiki.gentoo.org/wiki/X_server "X server")).