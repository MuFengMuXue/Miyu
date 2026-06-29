Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/Elogind/es "elogind (100% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Elogind/hu "elogind (85% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Elogind/ru "elogind (54% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Elogind/ja "elogind (100% translated)")

**Resources**

[[]][GitHub](https://github.com/elogind/elogind)

[[]][Package information](https://packages.gentoo.org/packages/sys-auth/elogind)

**elogind** is the [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") project\'s [*logind*](https://en.wikipedia.org/wiki/Systemd#logind "wikipedia:Systemd"), extracted to a standalone package. It\'s designed for users who prefer a non-systemd [init system](https://wiki.gentoo.org/wiki/Init_system "Init system"), but still want to use popular software such as [KDE](https://wiki.gentoo.org/wiki/KDE "KDE") or [GNOME](https://wiki.gentoo.org/wiki/GNOME "GNOME") that otherwise hard-depends on systemd.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Service]](#Service)
    -   [[2.2] [startx D-Bus integration]](#startx_D-Bus_integration)
    -   [[2.3] [Suspend/Hibernate Resume/Thaw hook scripts]](#Suspend.2FHibernate_Resume.2FThaw_hook_scripts)
    -   [[2.4] [elogind.conf]](#elogind.conf)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [loginctl]](#loginctl)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Confirmation of full functionality]](#Confirmation_of_full_functionality)
    -   [[4.2] [Conflict when using hidepid in proc]](#Conflict_when_using_hidepid_in_proc)
    -   [[4.3] [PAM]](#PAM)
-   [[5] [External resources]](#External_resources)

## [Installation]

### [Kernel]

The following kernel options are recommended:

[KERNEL]

    General setup  --->
        [*] Control Group support  --->
    File systems  --->
        [*] Inotify support for userspace

In the unlikely (and not recommended) event that standard kernel features are enabled for manual configuration, elogind also requires `eventpoll`, `signalfd()` and `timerfd()` support. Most users can ignore this.

### [USE flags]

### [USE flags for] [sys-auth/elogind](https://packages.gentoo.org/packages/sys-auth/elogind) [[]] [The systemd project\'s logind, extracted to a standalone package]

  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+acl`](https://packages.gentoo.org/useflags/+acl)                     Add support for Access Control Lists
  [`+pam`](https://packages.gentoo.org/useflags/+pam)                     Add support for PAM (Pluggable Authentication Modules) - DANGEROUS to arbitrarily flip
  [`+policykit`](https://packages.gentoo.org/useflags/+policykit)         Enable PolicyKit (polkit) authentication support
  [`audit`](https://packages.gentoo.org/useflags/audit)                   Enable support for Linux audit subsystem using sys-process/audit
  [`cgroup-hybrid`](https://packages.gentoo.org/useflags/cgroup-hybrid)   Use hybrid cgroup hierarchy instead of unified (OpenRC\'s default).
  [`debug`](https://packages.gentoo.org/useflags/debug)                   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`doc`](https://packages.gentoo.org/useflags/doc)                       Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`selinux`](https://packages.gentoo.org/useflags/selinux)               !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`test`](https://packages.gentoo.org/useflags/test)                     Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-12 18:07] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

There is a global `elogind` USE flag for enabling elogind support in other packages. It\'s also recommended to disable support for other session trackers (`systemd`) to avoid conflicts:

[FILE] **`/etc/portage/make.conf`**

    USE="elogind -systemd"

** Warning**\
Using elogind and systemd at the same time is untested and not advised!

### [Emerge]

After updating the USE flags update the system so the changes take effect:

`root `[`#`]`emerge --ask --changed-use --deep @world`

## [Configuration]

### [Service]

elogind should be configured to start at boot time:

`root `[`#`]`rc-update add elogind boot`

When [D-Bus](https://wiki.gentoo.org/wiki/D-Bus "D-Bus") is installed with the `USE="elogind"` flag, starting elogind on boot triggers the dbus system daemon to load automatically.

Alternatively, elogind can be launched on-demand by the first program that requests it (like a compatible [display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager")), through the system dbus service.

** Warning**\
If there are problems getting poweroff/reboot/suspend etc. working from desktop environment, putting elogind into boot runlevel will make sure the elogind-daemon is started properly before any user is logged in, and so should fix the problem.

Additionally, if built with the [[[pam]](https://packages.gentoo.org/useflags/pam)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag"), elogind will be activated when the first user logs into the system.

** Warning**\
In order to trigger elogind to activate a session on first on a VT console terminal, [[[sys-apps/shadow]](https://packages.gentoo.org/packages/sys-apps/shadow)[]] has to be built with the `pam` USE flag also, since it provides /bin/login. This concept also applies to any other graphical login managers or alternative terminal login programs used. In that case, they should be built with PAM too.

### [startx D-Bus integration]

To have an elogind session created when using [startx] to start the X server (instead of a [display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager")), add the following to the user\'s [\~/.xinitrc] file:

[FILE] **`~/.xinitrc`**

    exec dbus-run-session <WINDOW_MANAGER>

`WINDOW_MANAGER` in the above example needs to be replaced by a [window manager](https://wiki.gentoo.org/wiki/Window_manager "Window manager") or a single application.

** Tip**\
This exec command launches [dbus-daemon \--session], which launches your WM. No further commands will be executed if placed after this \"exec\" line.

### [][Suspend/Hibernate Resume/Thaw hook scripts]

With elogind the situation is much handier. Any suspend/resume and hibernate/thaw hook scripts need to be in the directory [/etc/elogind/system-sleep/] and use the variables `$1` (`pre` or `post`) and `$2` (`suspend`, `hibernate`, or `hybrid-sleep`). For example, in the case of elogind a hook script could have the following format:

[FILE] **`/etc/elogind/system-sleep/example.sh`An example of elogind hook**

    #!/bin/bash
    case $1/$2 in
      pre/*)
        # Put here any commands expected to be run when suspending or hibernating.
        ;;
      post/*)
        # Put here any commands expected to be run when resuming from suspension or thawing from hibernation.
        ;;
    esac

Do not forget to make the hook scripts executable:

`root `[`#`]`chmod +x /etc/elogind/system-sleep/example.sh`

### [elogind.conf]

Other automatic actions can be configured through [/etc/elogind/logind.conf]. For example, to disable suspend on laptop lid close,

[FILE] **`/etc/elogind/logind.conf.d/lid.conf`Disable suspend on laptop lid close**

    [Login]
    HandleLidSwitch=ignore

Make sure to reload the loginctl configuration following changes.

`root `[`#`]`loginctl reload`

** Warning**\
Restarting the logind service via service manager instead of using `loginctl reload` will cause the loss of all existing login sessions.

## [Usage]

### [loginctl]

The command [loginctl] may be used to control and introspect the login manager. For example, to shut down or reboot the system:

`user `[`$`]`loginctl poweroff`

`user `[`$`]`loginctl reboot`

For example, to suspend, hibernate or hybrid-suspend the system:

`user `[`$`]`loginctl suspend`

`user `[`$`]`loginctl hibernate`

`user `[`$`]`loginctl hybrid-sleep`

To suspend the system and then hibernate after a period of inactivity while the system is suspended:

`user `[`$`]`loginctl suspend-then-hibernate`

where hibernation delay can be specified in [/etc/elogind/logind.conf].

## [Troubleshooting]

### [Confirmation of full functionality]

Running loginctl itself will indicate ALL sessions/seats/users/tty\'s for which elogind has been fully activated. For example:

`user `[`$`]`loginctl`

    SESSION  UID USER      SEAT  TTY
          1    0 root      seat0 tty1
          2 1000 larry     seat0 tty2

    2 sessions listed.

Checking for the presence of XDG environment variables should produce similar results, even before a GUI is loaded. For example:

`user `[`$`]`env | grep "XDG" `

    XDG_CONFIG_DIRS=/etc/xdg
    XDG_SEAT=seat0
    XDG_SESSION_TYPE=tty
    XDG_SESSION_CLASS=user
    XDG_VTNR=2
    XDG_SESSION_ID=2
    XDG_RUNTIME_DIR=/run/user/1000
    XDG_DATA_DIRS=/usr/local/share:/usr/share

### [Conflict when using hidepid in proc]

When [procfs is mounted](https://wiki.gentoo.org/wiki/Procfs#Restricting_access_to_PID_directories "Procfs") with `hidepid=2` and `gid=wheel`, there will be conflicts with elogind. In order to change this, the [gid] needs to be changed to `gid=polkitd`.

See also this forum post [https://forums.gentoo.org/viewtopic-t-1099870.html](https://forums.gentoo.org/viewtopic-t-1099870.html)

### [PAM]

If using [[[pam]](https://packages.gentoo.org/useflags/pam)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")], make sure there are no conflicting pending changes waiting to be written to [/etc] (run [dispatch-conf] to merge any [/etc/pam.d] conflicts).

Confirm these changes took place in these two [/etc/pam.d] files:

`user `[`$`]`grep -r "elogind" /etc/pam.d/ `

    /etc/pam.d/elogind-user: session optional pam_elogind.so
    /etc/pam.d/system-login: -session        optional        pam_elogind.so

## [External resources]

-   [[[bug #599470]](https://bugs.gentoo.org/show_bug.cgi?id=599470)[]] - [[[sys-auth/elogind]](https://packages.gentoo.org/packages/sys-auth/elogind)[]] integration into Gentoo tracker bug.
-   [News item - Desktop profile switching USE default to elogind](https://gentoo.org/support/news-items/2020-04-14-elogind-default.html)