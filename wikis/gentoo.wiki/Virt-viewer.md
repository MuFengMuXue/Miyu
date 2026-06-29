**Resources**

[[]][Home](https://virt-manager.org/)

[[]][Package information](https://packages.gentoo.org/packages/app-emulation/virt-viewer)

[[]][GitLab](https://gitlab.com/virt-viewer/virt-viewer)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Virtual_Machine_Manager "wikipedia:Virtual Machine Manager")

[[]][Official documentation](https://virt-manager.org/)

[[]][Man page](https://manpages.ubuntu.com/manpages/latest/man1/virt-viewer.1.html)

[[]][Bugs (upstream)](https://gitlab.com/virt-viewer/virt-viewer/-/issues)

[virt-viewer] is a graphical console viewer for virtual machines managed by libvirt.

The program connects to an existing virtual machine and displays its graphical console (SPICE, VNC, etc.).

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [USE flags]](#USE_flags)
    -   [[2.2] [Emerge]](#Emerge)
    -   [[2.3] [Additional software]](#Additional_software)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Environment variables]](#Environment_variables)
    -   [[3.2] [Files]](#Files)
    -   [[3.3] [User permissions]](#User_permissions)
        -   [[3.3.1] [System user/group]](#System_user.2Fgroup)
-   [[4] [Usage]](#Usage)
    -   [[4.1] [Invocation]](#Invocation)
    -   [[4.2] [Default connection]](#Default_connection)
    -   [[4.3] [System start]](#System_start)
    -   [[4.4] [Session start]](#Session_start)
    -   [[4.5] [Full screen]](#Full_screen)
    -   [[4.6] [Reconnect automatically]](#Reconnect_automatically)
    -   [[4.7] [Waiting for VM to start]](#Waiting_for_VM_to_start)
-   [[5] [Removal]](#Removal)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

## [Overview]

[virt-viewer] is a protocol-deciphering front-end and a wrapper to the [remote-viewer] that actually displays the VM\'s desktop/console.

## [Installation]

### [USE flags]

### [USE flags for] [app-emulation/virt-viewer](https://packages.gentoo.org/packages/app-emulation/virt-viewer) [[]] [Graphical console client for connecting to virtual machines]

  ------------------------------------------------------------- --------------------------------------------------------------
  [`+libvirt`](https://packages.gentoo.org/useflags/+libvirt)   Support connecting to virtual machines managed by libvirt.
  [`+spice`](https://packages.gentoo.org/useflags/+spice)       Support connecting to SPICE-enabled virtual machines.
  [`+vnc`](https://packages.gentoo.org/useflags/+vnc)           Support connecting to VNC-enabled virtual machines.
  [`sasl`](https://packages.gentoo.org/useflags/sasl)           Add support for the Simple Authentication and Security Layer
  [`vte`](https://packages.gentoo.org/useflags/vte)             Enable terminal support (x11-libs/vte) in the GTK+ interface
  ------------------------------------------------------------- --------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-14 10:23] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

** Note**\
If [virt-viewer] is going to be used, be sure to enable the `usbredir` and `spice` USE flags on the qemu package for correct operation.

\

### [Emerge]

`root `[`#`]`emerge --ask app-emulation/virt-viewer`

** Note**\
If full graphical console support is desired, add the `usbredir` and `spice` USE flags for the [app-emulation/qemu] package.

\

### [Additional software]

The [virt-viewer] requires the [[[app-emulation/libvirt]](https://packages.gentoo.org/packages/app-emulation/libvirt)[]] package. See [Libvirt](https://wiki.gentoo.org/wiki/Libvirt "Libvirt") --- a virtualization management toolkit for installation.

## [Configuration]

### [Environment variables]

A list of optional environment variables that are read and checked by the [virt-viewer] command:

Environment variable name

Description

Type

`VIRT_VIEWER_KEEP_FILE`

controls whether the temporary connection file (.vv) for VNC/SPICE descriptors gets deleted after use.

integer

`DISPLAY`

the display X server and screen to which graphical applications should be sent. Needed for GTK/SPICE windows or graphical virt-manager sessions.

X11 address string

`WAYLAND_DISPLAY`

Wayland display socket; used when running under Wayland instead of X11.

String

`GSETTINGS_BACKEND`

which backend is used for the GSettings system, which is part of the GNOME configuration system. Valid values are **[dconf]** and **[memory]**.

Enum

`GSETTINGS_SCHEMA_DIR`

the directory where GSettings schemas are located.

Filepath

`XDG_DATA_HOME`

Custom user data path (e.g., app files, preferences). Overridden by libvirt for isolation. Default is [\~/.local/share]

Filepath

`XDG_CACHE_HOME`

Custom user cache directory containing session-local runtime data for user. Default is [\~/.cache]

Filepath

`XDG_CONFIG_HOME`

Directory for user configuration files, commonly UI themes or custom keymaps. Default is [\~/.config]

Filepath

`XDG_RUNTIME_DIR`

runtime directory for user session

Filepath

### [Files]

Files accessed by [virt-viewer]:

-   [/usr/bin/virt-viewer]
-   [/usr/bin/remote-viewer]
-   [/usr/share/virt-viewer/]
-   [/usr/share/glib-2.0/schemas/]
-   [/usr/share/icons/]
-   [/run/user/\<uid\>/libvirt/] --- session sockets
-   [/var/run/libvirt/] --- system sockets

### [User permissions]

User must have permission to access libvirt sockets:

-   [/var/run/libvirt/libvirt-sock] (system connection)
-   [/run/user/\<uid\>/libvirt/libvirt-sock] (session connection)

See [libvirt configuration](https://wiki.gentoo.org/wiki/Libvirt#Configuration "Libvirt").

\

#### [][System user/group]

For non-root usage, user must be a member of [libvirt] group:

`root `[`#`]`gpasswd -a <user> libvirt`

\

\

## [Usage]

### [Invocation]

`user `[`$`]`virt-viewer --help`

    $ virt-viewer --help
    Usage: virt-viewer [OPTIONS] DOMAIN-NAME|ID|UUID

    Connect to a virtual machine console.

    Options:
      -h, --help              Show help options
      -V, --version           Show version
      -c, --connect URI       Connect to hypervisor with libvirt URI
      -w, --wait              Wait for domain to start
      -r, --reconnect         Reconnect on disconnect
      -z, --zoom              Set initial zoom level
      -f, --full-screen       Start in full screen mode
      --display DISPLAY       Specify display backend
      --attach                Attach to running domain
      --direct                Do not use libvirt, connect directly
      --spice-debug           Enable SPICE debug output
      --hotkeys HOTKEYS       Override default hotkeys

### [Default connection]

Compiled default for Libvirt connection is [qemu:///system].

Default connection can be confirmed by executing:

`host$``virsh uri`

    qemu:///system

`root#``virsh uri`

    qemu:///system

### [System start]

Connect to a VM using system connection:

`user `[`$`]`virt-viewer -c qemu:///system win10`

### [Session start]

Connect to a VM using session connection:

`user `[`$`]`virt-viewer -c qemu:///session win10`

\

### [Full screen]

Open console in full screen:

`user `[`$`]`virt-viewer --full-screen win10`

### [Reconnect automatically]

Reconnect automatically:

`user `[`$`]`virt-viewer --reconnect win10`

### [Waiting for VM to start]

Wait for VM to start:

`user `[`$`]`virt-viewer --wait win10`

## [Removal]

`root `[`#`]`emerge --ask --depclean --verbose app-emulation/virt-viewer`

## [See also]

-   [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU") --- a generic, open-source hardware emulator and virtualization suite.
-   [Libvirt](https://wiki.gentoo.org/wiki/Libvirt "Libvirt") --- a virtualization management toolkit
-   [Virt-manager](https://wiki.gentoo.org/wiki/Virt-manager "Virt-manager") --- lightweight GUI application designed for managing virtual machines and containers via the [libvirt](https://wiki.gentoo.org/wiki/Libvirt "Libvirt") API.
-   [Virt-install](https://wiki.gentoo.org/wiki/Virt-install "Virt-install") --- a CLI-based [virtualization](https://wiki.gentoo.org/wiki/Virtualization "Virtualization") machine creator utility.

## [External resources]

-   [virt-viewer project homepage](https://virt-manager.org/)