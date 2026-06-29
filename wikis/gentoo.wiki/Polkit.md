**Resources**

[[]][Home](http://www.freedesktop.org/wiki/Software/polkit)

[[]][Wikipedia](https://en.wikipedia.org/wiki/PolicyKit "wikipedia:PolicyKit")

**polkit** (formerly **PolicyKit**) is an authorization API intended to be used by privileged programs (e.g. system daemons) offering services to unprivileged programs.

## Contents

-   [[1] [Description]](#Description)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Prerequisites]](#Prerequisites)
    -   [[2.2] [USE flags]](#USE_flags)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Rules]](#Rules)
-   [[4] [Usage]](#Usage)
-   [[5] [Troubleshooting]](#Troubleshooting)

## [Description]

Privileged programs (in the following called daemons) with polkit support offload the decision as to whether a program is allowed to use some function of the daemon. The daemon keeps an incoming request on hold, asks polkit if the program is authorized, and then allows or denies the request based on polkit\'s return. The requesting program is not aware of polkit and so needs no polkit support itself. The communication is handled over [D-Bus](https://wiki.gentoo.org/wiki/D-Bus "D-Bus").

Daemons come with polkit action files, which offer some function and define who is authorized. This can be any user, either the active or inactive user. Also they can specify that the user needs to authenticate by entering a password as himself or as admin. These actions do not grant root permission to an entire process, but rather allows a finer level of control of centralized system policy.

The authorization defaults defined by the action files can be refined by rules files. Here you can define who\'s admin (root or any user in a special group) and add special handling for an action.

## [Installation]

** Note**\
When updating, refer to the polkit [upgrade subpage](https://wiki.gentoo.org/wiki/Polkit/upgrade "Polkit/upgrade").

### [Prerequisites]

Polkit uses [D-Bus](https://wiki.gentoo.org/wiki/D-Bus "D-Bus"), so set it up first.

Also, make sure you set `CONFIG_FUTEX=y` in the kernel. Without this option selected, the [polkitd] process may generate high CPU usage.

### [USE flags]

Portage knows the global `policykit` USE flag for enabling support for polkit in other packages. Enabling this USE flag will pull in [[[sys-auth/polkit]](https://packages.gentoo.org/packages/sys-auth/polkit)[]] automatically (default for *desktop* [profiles](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)")):

[FILE] **`/etc/portage/make.conf`**

    USE="policykit"

The USE flags of [[[sys-auth/polkit]](https://packages.gentoo.org/packages/sys-auth/polkit)[]] are:

### [USE flags for] [sys-auth/polkit](https://packages.gentoo.org/packages/sys-auth/polkit) [[]] [Policy framework for controlling privileges for system-wide services]

  ------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+introspection`](https://packages.gentoo.org/useflags/+introspection)   Add support for GObject based introspection
  [`elogind`](https://packages.gentoo.org/useflags/elogind)                 Enable session tracking via sys-auth/elogind
  [`examples`](https://packages.gentoo.org/useflags/examples)               Install examples, usually source code
  [`gtk`](https://packages.gentoo.org/useflags/gtk)                         Add support for x11-libs/gtk+ (The GIMP Toolkit)
  [`kde`](https://packages.gentoo.org/useflags/kde)                         Add support for software made by KDE, a free software community
  [`nls`](https://packages.gentoo.org/useflags/nls)                         Add Native Language Support (using gettext - GNU locale utilities)
  [`pam`](https://packages.gentoo.org/useflags/pam)                         Add support for PAM (Pluggable Authentication Modules) - DANGEROUS to arbitrarily flip
  [`selinux`](https://packages.gentoo.org/useflags/selinux)                 !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`systemd`](https://packages.gentoo.org/useflags/systemd)                 Use sys-apps/systemd for session tracking
  [`test`](https://packages.gentoo.org/useflags/test)                       Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-29 19:54] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

After setting this you want to update your system so the changes take effect:

`root `[`#`]`emerge --ask --changed-use --deep @world`

Depending on above USE flag settings, either [elogind](https://wiki.gentoo.org/wiki/Elogind "Elogind") or [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") need to be configured.

## [Configuration]

The actions files are in [/usr/share/polkit-1/actions], the rules files are in [/usr/share/polkit-1/rules.d] and [/etc/polkit-1/rules.d].

### [Rules]

Rules redefine who\'s authorized for an action. The rules files begin with a number and are processed in lexical order. The first file with a matching rule is used. Own files should have a low number, like *10*. The filenames have the [.rules] suffix.

For example, to let the users of the [wheel] group also perform functions as administrators, create the following file:

[FILE] **`/etc/polkit-1/rules.d/10-admin.rules`**

    polkit.addAdminRule(function(action, subject) );

To allow user [larry] to mount disks, create the following file:

[FILE] **`/etc/polkit-1/rules.d/10-udisks.rules`**

    polkit.addRule(function(action, subject)
    });

See [man polkit] for more information.

## [Usage]

Show all available actions:

`user `[`$`]`pkaction`

Show details about the given action:

`user `[`$`]`pkaction --verbose --action-id ACTION`

List all temporary authorizations for the current session:

`user `[`$`]`pkcheck --list-temp`

Runs the given program with the user rights of the given user:

`user `[`$`]`pkexec --user USER PROGRAM`

For more information see the [man pages](https://wiki.gentoo.org/wiki/Man_page "Man page"), e.g. for [pkaction]: [man pkaction]

## [Troubleshooting]

-   [[[Gentoo bugtracker: known bugs]](https://bugs.gentoo.org/buglist.cgi?quicksearch=polkit&order=bug_id%20DESC)[]]
-   Polkit communicates over D-Bus, so also see the [D-Bus \"Troubleshooting\" section](https://wiki.gentoo.org/wiki/D-Bus#Troubleshooting "D-Bus").
-   [How to switch polkit from spidermonkey to duktape](https://forums.gentoo.org/viewtopic-t-1131447.html)