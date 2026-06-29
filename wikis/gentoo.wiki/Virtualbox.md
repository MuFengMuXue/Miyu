This page contains [[changes](https://wiki.gentoo.org/index.php?title=VirtualBox&oldid=1377031&diff=1415235)] which are not marked for translation.

Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/VirtualBox/es "VirtualBox (2% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/VirtualBox/hu "VirtualBox (100% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/VirtualBox/ja "VirtualBox (78% translated)")

**Resources**

[[]][Home](https://www.virtualbox.org)

[[]][Package information](https://packages.gentoo.org/packages/app-emulation/virtualbox)

[[]][Wikipedia](https://en.wikipedia.org/wiki/VirtualBox "wikipedia:VirtualBox")

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/virtualbox)

**VirtualBox** is a cross-platform virtualization software that allows users to run guest operating systems inside a host operating system without having to reboot. Since 2010 VirtualBox software has been written and maintained by the Oracle Corporation.

## Contents

-   [[1] [Terminology]](#Terminology)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Kernel]](#Kernel)
    -   [[2.2] [USE flags]](#USE_flags)
    -   [[2.3] [Emerge]](#Emerge)
    -   [[2.4] [Microsoft Windows guests]](#Microsoft_Windows_guests)
    -   [[2.5] [Gentoo guests]](#Gentoo_guests)
        -   [[2.5.1] [Kernel configuration]](#Kernel_configuration)
        -   [[2.5.2] [Guest Additions]](#Guest_Additions)
            -   [[2.5.2.1] [Resizing doesn\'t work]](#Resizing_doesn.27t_work)
        -   [[2.5.3] [GPU acceleration]](#GPU_acceleration)
    -   [[2.6] [VirtualBox shared folders in a Gentoo guest]](#VirtualBox_shared_folders_in_a_Gentoo_guest)
    -   [[2.7] [Advanced networking-related]](#Advanced_networking-related)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Kernel modules]](#Kernel_modules)
        -   [[3.1.1] [systemd]](#systemd)
    -   [[3.2] [Enable port forwarding to guest machines]](#Enable_port_forwarding_to_guest_machines)
-   [[4] [Usage]](#Usage)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [virtualbox fails to build]](#virtualbox_fails_to_build)
    -   [[5.2] [virtualbox-modules fails to build]](#virtualbox-modules_fails_to_build)
    -   [[5.3] [virtualbox-modules permission denied errors]](#virtualbox-modules_permission_denied_errors)
    -   [[5.4] [Host key failing to operate in the virtual machine]](#Host_key_failing_to_operate_in_the_virtual_machine)
    -   [[5.5] [No audio after upgrade]](#No_audio_after_upgrade)
    -   [[5.6] [Performance problems]](#Performance_problems)
        -   [[5.6.1] [Microsoft Windows guests]](#Microsoft_Windows_guests_2)
        -   [[5.6.2] [Linux guests]](#Linux_guests)
    -   [[5.7] [Kernel driver not installed]](#Kernel_driver_not_installed)
    -   [[5.8] [Nonexistent host networking interface, named \'vboxnet0\']](#Nonexistent_host_networking_interface.2C_named_.27vboxnet0.27)
    -   [[5.9] [Kernel Panic when suspending the HOST while Virtualbox is running]](#Kernel_Panic_when_suspending_the_HOST_while_Virtualbox_is_running)
    -   [[5.10] [Instability with kernel 6.6.x]](#Instability_with_kernel_6.6.x)
    -   [[5.11] [Vagrant doesn\'t save virtual machines states]](#Vagrant_doesn.27t_save_virtual_machines_states)
    -   [[5.12] [Virtualbox does not start with kernel 6.12+]](#Virtualbox_does_not_start_with_kernel_6.12.2B)
    -   [[5.13] [Crash when playing sound]](#Crash_when_playing_sound)
    -   [[5.14] [Virtual machine does not start with kernel 6.15.x]](#Virtual_machine_does_not_start_with_kernel_6.15.x)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)
-   [[8] [References]](#References)

## [Terminology]

  ---------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Term                         Explanation
  Host operating system        The host computer. Most likely the physical hardware present in the room. For Gentoo users the host operating system would be Gentoo Linux
  Guest operating system       The operating system *to be* installed or *currently* installed inside the VirtualBox emulation environment. Possible alternative operating systems include Microsoft Windows, Solaris, BSD, Debian, Ubuntu, etc.
  VirtualBox Guest Additions   Drivers for the guest operating system. These drivers provide smoother operation with the Host operating system compared to the standard drivers installed by the Guest operating system.
  ---------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [Installation]

### [Kernel]

VirtualBox host requires following [kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") configuration options:

[KERNEL]

    [*] Enable loadable module support  --->
      [ ]   Trim unused exported kernel symbols
    [*] Virtualization  --->

### [USE flags]

### [USE flags for] [app-emulation/virtualbox](https://packages.gentoo.org/packages/app-emulation/virtualbox) [[]] [Family of powerful x86 virtualization products for enterprise and home use]

  ----------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+gui`](https://packages.gentoo.org/useflags/+gui)                           Enable support for a graphical user interface
  [`+opengl`](https://packages.gentoo.org/useflags/+opengl)                     Add support for OpenGL (3D graphics)
  [`+sdk`](https://packages.gentoo.org/useflags/+sdk)                           Enable building of SDK.
  [`+sdl`](https://packages.gentoo.org/useflags/+sdl)                           Add support for Simple Direct Layer (media library)
  [`+strip`](https://packages.gentoo.org/useflags/+strip)                       Allow symbol stripping to be performed by the ebuild for special files
  [`+udev`](https://packages.gentoo.org/useflags/+udev)                         Controls installation of special USB udev rules.
  [`+vmmraw`](https://packages.gentoo.org/useflags/+vmmraw)                     Enable 32-bit support on a 64-bit kernel.
  [`alsa`](https://packages.gentoo.org/useflags/alsa)                           Add support for media-libs/alsa-lib (Advanced Linux Sound Architecture)
  [`dbus`](https://packages.gentoo.org/useflags/dbus)                           Enable dbus support for anything that needs it (gpsd, gnomemeeting, etc)
  [`debug`](https://packages.gentoo.org/useflags/debug)                         Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`dist-kernel`](https://packages.gentoo.org/useflags/dist-kernel)             Enable subslot rebuilds on Distribution Kernel upgrades
  [`doc`](https://packages.gentoo.org/useflags/doc)                             Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`dtrace`](https://packages.gentoo.org/useflags/dtrace)                       Install dtrace Extension Pack.
  [`java`](https://packages.gentoo.org/useflags/java)                           Add support for Java
  [`lvm`](https://packages.gentoo.org/useflags/lvm)                             Build VBoxVolInfo that needs devicemapper from sys-fs/lvm2.
  [`modules-compress`](https://packages.gentoo.org/useflags/modules-compress)   Install compressed kernel modules (if kernel config enables module compression)
  [`modules-sign`](https://packages.gentoo.org/useflags/modules-sign)           Cryptographically sign installed kernel modules (requires CONFIG_MODULE_SIG=y in the kernel)
  [`nls`](https://packages.gentoo.org/useflags/nls)                             Add Native Language Support (using gettext - GNU locale utilities)
  [`pam`](https://packages.gentoo.org/useflags/pam)                             Add support for PAM (Pluggable Authentication Modules) - DANGEROUS to arbitrarily flip
  [`pch`](https://packages.gentoo.org/useflags/pch)                             Enable precompiled header support for faster compilation at the expense of disk space and memory
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)               Add sound server support via media-libs/libpulse (may be PulseAudio or PipeWire)
  [`python`](https://packages.gentoo.org/useflags/python)                       Add optional support/bindings for the Python language
  [`test`](https://packages.gentoo.org/useflags/test)                           Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`vboxwebsrv`](https://packages.gentoo.org/useflags/vboxwebsrv)               Build and install the VirtualBox webservice.
  [`vde`](https://packages.gentoo.org/useflags/vde)                             Support for VDE networking via net-misc/vde.
  [`vnc`](https://packages.gentoo.org/useflags/vnc)                             Enable VNC (remote desktop viewer) support
  ----------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-01 12:21] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

** Note**\
Starting with virtualbox **7.0.4** ([testing branch](https://wiki.gentoo.org/wiki/Handbook:X86/Portage/Branches#Testing "Handbook:X86/Portage/Branches") as of 2022-11), the `gui` [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") controls installation of the graphical user interface (GUI), which is enabled by default. Up to virtualbox **7.0.2**, the `qt5` USE flag controls installation of GUI, also enabled by default.

** Note**\
Starting with virtualbox **7.0.4**, the `headless` USE flag has been dropped. The same effect can be obtained by disabling the `gui`, `opengl`, and `sdl` USE flags.

### [Emerge]

`root `[`#`]`emerge --ask app-emulation/virtualbox`

### [Microsoft Windows guests]

Emerge the [[[app-emulation/virtualbox-additions]](https://packages.gentoo.org/packages/app-emulation/virtualbox-additions)[]] package on the host system to get the Guest Additions ISO image that contains all necessary Microsoft Windows guest drivers:

`root `[`#`]`emerge --ask app-emulation/virtualbox-additions`

### [Gentoo guests]

#### [Kernel configuration]

When running Gentoo as a guest system, enable the following kernel options on the guest system (either built-in or as modules) to get proper support for the hardware emulated by VirtualBox:

[KERNEL] **Generic Framebuffer prior to kernel 5.15**

    Bus options (PCI etc.)  --->
        [*] Mark VGA/VBE/EFI FB as generic system framebuffer

[KERNEL] **Generic Framebuffer kernel 5.15 and later**

    Device Drivers  --->
      Firmware Drivers  --->
        [*] Mark VGA/VBE/EFI FB as generic system framebuffer

[KERNEL] **Support for VirtualBox hardware**

    Device Drivers  --->
        <*> Serial ATA and Parallel ATA drivers (libata)  --->
            [*] AHCI SATA support
            [*] ATA SFF support (for legacy IDE and PATA)
            [*]   ATA BMDMA support
            [*]     Intel ESB, ICH, PIIX3, PIIX4 PATA/SATA support
        <*> Network device support  --->
            <*> Ethernet driver support  --->
                [*] Intel devices
                [*]   Intel(R) PRO/1000 Gigabit Ethernet support
        Input device support  --->
            <*> Keyboards  --->
                [*] AT keyboard
            <*> Mice  --->
                [*] PS/2 mouse
        <*> Virtio drivers  --->
            <*> PCI driver for virtio devices
        Graphics support  --->
            <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support)  --->
                [*] Enable legacy fbdev support for your modesetting driver
            <*> DRM driver for VMware Virtual GPU
                <*> Enable framebuffer console under vmwgfx by default
            Frame buffer Devices  --->
                <*> Support for frame buffer devices  --->
                    [*] Enable Firmware EDID
                    [*] Simple framebuffer support
            <*> Console display driver support  --->
                [*] Framebuffer Console support
                [*]   Map the console to the primary display device
        <*> Sound card support  --->
            <*> Advanced Linux Sound Architecture  --->
                <*> PCI sound devices  --->
                    [*] Intel/SiS/nVidia/AMD/ALi AC97 Controller
        <*> USB support  --->
            [*] xHCI HCD (USB 3.0) support
            [*] EHCI HCD (USB 2.0) support

#### [Guest Additions]

To install the Guest Additions, invoke the following command on the Gentoo guest system:

`root `[`#`]`emerge --ask app-emulation/virtualbox-guest-additions`

When using [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC"), make guest additions and [D-Bus](https://wiki.gentoo.org/wiki/D-Bus "D-Bus") start across reboots:

`root `[`#`]`rc-update add virtualbox-guest-additions default `

`root `[`#`]`rc-update add dbus default `

Otherwise when using [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd"), make guest additions start across reboots:

`root `[`#`]`systemctl enable --now virtualbox-guest-additions`

To enable the shared clipboard, display resizing, seamless mode, and drag and drop make sure the user running the [X](https://wiki.gentoo.org/wiki/X "X") session (on the Gentoo guest system) belongs to the [vboxguest] group:

`root `[`#`]`gpasswd -a <user> vboxguest`

Changes will not take effect until the user signs out and then signs in again (re-logins).

** Note**\
To install other Linux distributions as guest operating systems please refer to the distribution\'s documentation on how to install the drivers needed by VirtualBox or consult the official [VirtualBox documentation](https://www.virtualbox.org/manual/ch04.html#idp11274368).

##### [][Resizing doesn\'t work]

Due to the limitations of the VMSVGA described below, a daemon needs to be started in your X11 session for Guest resizing to work.

    Usage: VBoxClient --clipboard|--draganddrop|--checkhostversion|--seamless|--vmsvga[-d|--nodaemon]
    Starts the VirtualBox DRM/X Window System guest services.

    Options:
      --clipboard        starts the shared clipboard service
      --draganddrop      starts the drag and drop service
      --checkhostversion starts the host version notifier service
      --seamless         starts the seamless windows service
      --vmsvga           starts VMSVGA dynamic resizing for x11/Wayland guests
      -f, --foreground   run in the foreground (no daemonizing)
      -d, --nodaemon     continues running as a system service
      -h, --help         shows this help text
      -v, --verbose      increases logging verbosity level
      -V, --version      shows version information

If the Guest Additions are installed correctly, the shared clipboard is working, etc., but the display can\'t be resized, open the VM\'s settings in the host-side VirtualBox Manager and look at Display → Graphics Controller. If it\'s set to VMSVGA, try changing it to VBoxSVGA while the guest is powered off. According to the VirtualBox docs, this works because auto-resizing in Linux guests is induced in part by changing the serial number of the simulated monitor, which can\'t be done under VMSVGA.^[\[1\]](#cite_note-1)^

#### [GPU acceleration]

Though VirtualBox previously emulated VMWare\'s SVGA by default, this is no longer a feasible option as mesa has dropped the required \'xa\' USE flag after version 25.1 (see [bug 957955](https://bugs.gentoo.org/957955)). Now, the recommended method is to use the kernel modesetting driver. To do so, set the \'VIDEO_CARDS\' variable in [/etc/portage/make.conf] to an empty string:

    VIDEO_CARDS=""

and remove [[[x11-drivers/xf86-video-vmware]](https://packages.gentoo.org/packages/x11-drivers/xf86-video-vmware)[]].

** Important**\
When making changes to the `VIDEO_CARDS` setting, it is a good idea to perform a full deep upgrade to apply the change.

`root `[`#`]`emerge --changed-use --deep @world`

### [VirtualBox shared folders in a Gentoo guest]

VirtualBox shared folders can only be mounted after the virtualbox-guest-additions service has been started. Since this happens towards the end of the bootup sequence (OpenRC), a shared folder mount in [/etc/fstab] will fail. Either:

-   Make the `noauto` [mount](https://wiki.gentoo.org/wiki/Mount "Mount") option and add a mount/unmount pair of scripts in [/etc/local.d].
-   View [/etc/rc.conf] for information about adding extra dependencies for services.

If it is desired to let a user manually mount a shared folder, that user must be added to the [vboxsf] group:

`root `[`#`]`gpasswd -a larry vboxsf`

### [Advanced networking-related]

According to the [ebuild\'s](https://wiki.gentoo.org/wiki/Ebuild "Ebuild") message after VirtualBox is installed [[[sys-apps/usermode-utilities]](https://packages.gentoo.org/packages/sys-apps/usermode-utilities)[]] and [[[net-misc/bridge-utils]](https://packages.gentoo.org/packages/net-misc/bridge-utils)[]] can be installed for advanced network configuration. Install them only if advanced networking is required:

`root `[`#`]`emerge --ask sys-apps/usermode-utilities`

`root `[`#`]`emerge --ask net-misc/bridge-utils`

## [Configuration]

### [Kernel modules]

Users will not be able to run and use VirtualBox if they are not a member of the [vboxusers] group:

`root `[`#`]`gpasswd -a <user> vboxusers`

Changes will not take effect until the user re-login.

Load the required driver module into the kernel. This module is made available when [[[app-emulation/virtualbox-modules]](https://packages.gentoo.org/packages/app-emulation/virtualbox-modules)[]] has been emerged:

`root `[`#`]`modprobe vboxdrv`

Optional modules:

`root `[`#`]`modprobe vboxnetadp `

`root `[`#`]`modprobe vboxnetflt `

It is possible to automatically load the modules each time the system boots. Create a new file under the [/etc/modules-load.d] directory and list, separated by newlines, the kernel modules to load:

[FILE] **`/etc/modules-load.d/virtualbox.conf`**

    vboxdrv
    vboxnetadp
    vboxnetflt

#### [systemd]

Modules can be loaded immediately on systemd systems by running:

`root `[`#`]`systemctl start systemd-modules-load`

### [Enable port forwarding to guest machines]

When booting LiveCDs or other live media, it can be handy to enable port forwarding from the host machine to the guest machine. None of the additional network configuration modes are necessary for a simple port forwarding setup, so do not dig too deep into upstream docs. Port forwarding can be handy when running a web server, an SSH daemon, or any other service that runs on a specific port.

First, be sure the guest VM is shutdown, then from the command line issue:

`user `[`$`]`VBoxManage modifyvm "VM name" --natpf1 "guestssh,tcp,,2222,,22"`

Be sure to replace `"VM name"` with the proper name of the guest virtual machine. The first number (`2222`) will be the port on the host machine. The second number (`22`) will be the port on the guest machine. Adjust accordingly, then reboot the virtual machine. This can also be performed via the GUI by clicking [Settings] -\> [Network] -\> [Advanced] (drop down) -\> [Port Forwarding].

More details can be found in the [upstream documentation](https://www.virtualbox.org/manual/ch06.html#natforward).

## [Usage]

There are many options which can influence behavior and performance of the virtual machines. If you don\'t know what these options are doing, leave them to their defaults. Virtual machines may become unbootable if the wrong options are set.

Here is a list of options that are safe to use:

-   Host I/O cache can safely be enabled for all virtual storage controllers.
-   If the host system\'s CPU supports hardware virtualization, enable the \'VT-x/AMD-V\' option. It can drastically increase the performance of the virtual machines.

## [Troubleshooting]

### [virtualbox fails to build]

When the [[[app-emulation/virtualbox]](https://packages.gentoo.org/packages/app-emulation/virtualbox)[]] package fails to build because the [javac] command cannot be found (even with a Java JDK (Java Development Kit) and a Java JRE (Java Runtime Environment) installed), it is likely the JRE has been set as the default system-vm. JRE packages do not contain [javac]. Make sure the correct system-vm (JDK) has been selected using the [java-config] command and then try rebuilding virtualbox. More information can be found in the [Installing a virtual machine](https://wiki.gentoo.org/wiki/Java#Installing_a_virtual_machine "Java") section of the Java User Guide.

### [virtualbox-modules fails to build]

Some users have issues with the [[[app-emulation/virtualbox-modules]](https://packages.gentoo.org/packages/app-emulation/virtualbox-modules)[]] package failing to build. This can be caused by an improper kernel/profile configuration. Verify the chosen kernel and the selected profile *match* each other. For example, if a hardened profile is set, a hardened kernel should be used. If a default AMD64 profile is set, then the default gentoo-sources should be used. Run the [eselect] command to view the list of profile options:

`user `[`$`]`eselect profile list`

    Available profile symlink targets:
      [1]  default/linux/amd64/23.0/systemd (stable)
      [2]  default/linux/amd64/23.0/desktop (stable)
      [3]  default/linux/amd64/23.0/desktop/systemd (stable)
      [4]  default/linux/amd64/23.0/desktop/gnome (stable)
      [5]  default/linux/amd64/23.0/desktop/gnome/systemd (stable)
      [6]  default/linux/amd64/23.0/desktop/plasma (stable)
      [7]  default/linux/amd64/23.0/desktop/plasma/systemd (stable)
      [8]  default/linux/amd64/23.0/no-multilib (stable)
      [9]  default/linux/amd64/23.0/no-multilib/systemd (stable)
      [10]  default/linux/amd64/23.0/no-multilib/hardened (stable)
      [11]  default/linux/amd64/23.0/no-multilib/hardened/systemd (stable)
      [12]  default/linux/amd64/23.0/no-multilib/hardened/selinux (stable)
      [13]  default/linux/amd64/23.0/no-multilib/hardened/selinux/systemd (stable)
      [14]  default/linux/amd64/23.0/no-multilib/prefix (exp)
      [15]  default/linux/amd64/23.0/no-multilib/prefix/kernel-2.6.32+ (exp)
      [16]  default/linux/amd64/23.0/no-multilib/prefix/kernel-2.6.16+ (exp)
      [17]  default/linux/amd64/23.0/no-multilib/prefix/kernel-3.2+ (exp)
      [18]  default/linux/amd64/23.0/llvm (stable)
      [19]  default/linux/amd64/23.0/llvm/systemd (stable)
      [20]  default/linux/amd64/23.0/hardened (stable)
      [21]  default/linux/amd64/23.0/hardened/systemd (stable)
      [22]  default/linux/amd64/23.0/hardened/selinux (stable)
      [23]  default/linux/amd64/23.0/hardened/selinux/systemd (stable)
      [24]  default/linux/amd64/23.0/split-usr (stable)
      [25]  default/linux/amd64/23.0/split-usr/desktop (stable)
      [26]  default/linux/amd64/23.0/split-usr/desktop/gnome (stable)
      [27]  default/linux/amd64/23.0/split-usr/desktop/plasma (stable)
      [28]  default/linux/amd64/23.0/split-usr/no-multilib (stable)
      [29]  default/linux/amd64/23.0/split-usr/no-multilib/selinux (stable)
      [30]  default/linux/amd64/23.0/split-usr/no-multilib/hardened (stable)
      [31]  default/linux/amd64/23.0/split-usr/no-multilib/hardened/selinux (stable)
      [32]  default/linux/amd64/23.0/split-usr/no-multilib/prefix (exp)
      [33]  default/linux/amd64/23.0/split-usr/no-multilib/prefix/kernel-2.6.32+ (exp)
      [34]  default/linux/amd64/23.0/split-usr/no-multilib/prefix/kernel-2.6.16+ (exp)
      [35]  default/linux/amd64/23.0/split-usr/no-multilib/prefix/kernel-3.2+ (exp)
      [36]  default/linux/amd64/23.0/split-usr/llvm (stable)
      [37]  default/linux/amd64/23.0/split-usr/hardened (stable)
      [38]  default/linux/amd64/23.0/split-usr/hardened/selinux (stable)
      [39]  default/linux/amd64/23.0/x32 (dev)
      [40]  default/linux/amd64/23.0/x32/systemd (exp)
      [41]  default/linux/amd64/23.0/split-usr/x32 (exp)
      [42]  default/linux/amd64/23.0/musl (dev)
      [43]  default/linux/amd64/23.0/musl/llvm (exp)
      [44]  default/linux/amd64/23.0/musl/hardened (exp)
      [45]  default/linux/amd64/23.0/musl/hardened/selinux (exp)
      [46]  default/linux/amd64/23.0/split-usr/musl (dev)
      [47]  default/linux/amd64/23.0/split-usr/musl/llvm (exp)
      [48]  default/linux/amd64/23.0/split-usr/musl/hardened (exp)
      [49]  default/linux/amd64/23.0/split-usr/musl/hardened/selinux (exp)

Then use the [eselect] command again to display which kernel is selected:

`user `[`$`]`eselect kernel list`

    Available kernel symlink targets:
      [1]   linux-6.7.10-gentoo-dist
      [2]   linux-6.8.1-gentoo
      [3]   linux-6.8.2-gentoo
      [4]   linux-6.8.2-gentoo-dist *

Looking at the output of these two commands, a user can determine if the system is setup properly (the profile matches the kernel) and should have no issues installing [[[app-emulation/virtualbox-modules]](https://packages.gentoo.org/packages/app-emulation/virtualbox-modules)[]]. Remember: Make sure the system profile and the selected kernel match!

### [virtualbox-modules permission denied errors]

The following \"Permission denied\" errors can be caused by a strict file mode creation mask (e.g. `umask 077`):

    cc1: error: ./arch/x86/include/generated/uapi: Permission denied
    cc1: error: ./arch/x86/include/generated/uapi: Permission denied
    cc1: error: ./include/generated/uapi: Permission denied
    cc1: error: ./include/generated/uapi: Permission denied
    cc1: error: ./arch/x86/include/generated/uapi: Permission denied
    cc1: error: ./include/generated/uapi: Permission denied
    cc1: error: ./arch/x86/include/generated/uapi: Permission denied
    cc1: error: ./include/generated/uapi: Permission denied

The easiest solution would be to backup `.config`, run `make distclean` and use the default `umask 022`.

### [Host key failing to operate in the virtual machine]

If the host key (typically the right [Ctrl] key) is failing to operate within the virtual (guest) machine, be sure any desktop environment or window manager hooks to host key have been *disabled* from the host machine\'s desktop environment or window manager.

[   Important note to editors]

The following paragraph appears obsolete, as *gnome-extra/gnome-tweak-tool* is no longer in the gentoo repository. If anyone knows how to [update this section, please do](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide"). (Note: [[[gnome-extra/gnome-tweaks]](https://packages.gentoo.org/packages/gnome-extra/gnome-tweaks)[]] and [[[gnome-extra/mousetweaks]](https://packages.gentoo.org/packages/gnome-extra/mousetweaks)[]] seem like possible successors to *gnome-extra/gnome-tweak-tool*, but if one of those packages were an equivalent, these instructions still need validating.)

For example, the [GNOME](https://wiki.gentoo.org/wiki/GNOME "GNOME") 3 desktop environment includes a \"Show location of the \[mouse\] pointer\" option in the [Keyboard and Mouse] section of the Tweak Tool ([[[gnome-extra/gnome-tweak-tool]](https://packages.gentoo.org/packages/gnome-extra/gnome-tweak-tool)[]]). This option will enable a ripple effect to be displayed around the mouse when either the right or left [Ctrl] key is pressed. This mouse locator handle conflicts with the virtual machine\'s handle on the right [Ctrl] key. Disabling this setting (via switching the rocker switch to Off in the Tweak Tool interface) should fix the problem by re-assigning the right [Ctrl] key as the handle for the host key within the virtual machine.

### [No audio after upgrade]

If there is no sound after upgrading VirtualBox, increasing the VirtualBox ALSA buffer size may fix the issue^[\[2\]](#cite_note-2)^.

`user `[`$`]`VBoxManage setextradata global VBoxInternal2/Audio/ALSAAudio/BufferSizeMs "100"`

### [Performance problems]

#### [Microsoft Windows guests]

-   According to the [documentation](https://www.virtualbox.org/manual/ch03.html#settings-motherboard), the **I/O APIC** feature (*VM -\> Settings -\> System -\> Motherboard -\> Enable I/O APIC*), which is enabled by default, \'slightly increases the overhead of virtualization and therefore slows down the guest OS a little\'. However, there have been reports that the performance impact may actually be quite severe on some host/guest system combinations (e.g. [forum post](https://forums.virtualbox.org/viewtopic.php?f=1&t=75229)). Be aware that disabling this feature might require additional steps on the guest system as described by this [forum post](https://forums.virtualbox.org/viewtopic.php?f=2&t=21480).
-   Using a SATA controller, it is necessary to choose the right driver version from Intel\'s SATA drivers. Using a wrong version will cause performance problems along with blue screen errors! Refer to [this post](https://forums.virtualbox.org/viewtopic.php?f=28&t=42829) for a list of working SATA drivers.
-   Slow performance using SATA driver? Only use the SATA controller interface for the hard disk. Remove any CDROMs from the SATA controller and place them onto a IDE Controller.

    :::
    ** Note**\
    This can also be a problem of using the wrong SATA-driver version.
    :::
-   When installing the VirtualBox Guest Additions into your Windows operating system, do not select to enable Direct3D (experimental) option as this will cause resizing problems and other anomalies. Also, you need to install the Guest Additions from Safe Mode.
-   Do not use the ICH9 chipset with Windows. It is still considered experimental. Using it can cause temporary freezes of the whole VM when used with Windows 7. See [this post](https://forums.virtualbox.org/viewtopic.php?f=2&t=44106) for more informations.
-   Slow read/write speed to the virtual disk? If the host system has sufficient RAM, try checking (enabling) the [[Use Host I/O Cache](https://www.virtualbox.org/manual/ch05.html#iocaching)] check box in the virtual machine\'s [Storage] frame. This will cache much of the guest machine\'s page file into the host\'s memory effectively limiting the amount of I/O guest machine will use the virtual disk image file. This is particularly helpful when running Windows guests because of the amount of paging Windows based operating systems regularly perform.

#### [Linux guests]

-   When running Gentoo as a guest system make sure you start the virtualbox-guest-additions init script during bootup.
-   Having the guest VDI images on a btrfs filesystem might slow down Linux guests up to the point where the guest kernel remounts its filesystems readonly and no longer performs any I/O. This can be fixed by disabling btrfs\' copy on write for the VDI image files on the host.

### [Kernel driver not installed]

[![VirtualBox-Error: Kernel driver not installed](/images/4/40/VirtualBox-Error_In_suplibOsInit.png)](https://wiki.gentoo.org/wiki/File:VirtualBox-Error_In_suplibOsInit.png "VirtualBox-Error: Kernel driver not installed")

This may occur after building a new kernel and causes an error message:

`user `[`$`]`VirtualBox`

    WARNING: The vboxdrv kernel module is not loaded. Either there is no module available for the current kernel (4.9.0-gentoo) or it failed to load. Please recompile the kernel module and install it by

    for m in vbox; do modprobe $m; done

    You will not be able to start VMs until this problem is fixed.

**Solution:** Rebuild the VirtualBox kernel modules via:

`root `[`#`]`emerge --ask --oneshot @module-rebuild`

The system may need rebooted for changes to take effect.

### [][Nonexistent host networking interface, named \'vboxnet0\']

`root `[`#`]`VBoxManage hostonlyif create`

Newly created interface will now be shown as available, but not activated (down):

`user `[`$`]`ip link`

An IP will need to be assigned to it:

`root `[`#`]`VBoxManage hostonlyif ipconfig vboxnet0 --ip 192.168.56.101`

### [Kernel Panic when suspending the HOST while Virtualbox is running]

Try removing the vbox family of modules before suspending. If this solves the kernel panic, the vbox modules can be added to the list of permanently removed modules before suspend so that these modules are loaded automatically after suspend:

`root `[`#`]`echo 'SUSPEND_MODULES="vboxpci vboxnetflt vboxnetadp vboxdrv"' >> /etc/pm/config.d/gentoo`

### [Instability with kernel 6.6.x]

There have been reports of system instability with kernel 6.6.x (like video drivers crashing on closing a virtual box).

The only known workaround at this time is downgrading to kernel 6.1.x.

### [][Vagrant doesn\'t save virtual machines states]

If no VirtualBox instance is running, Vagrant may fail to save the states of virtual machines. This can be solved in one of two ways:

1.  Let VirtualBox open on a **graphic server**.
2.  Enable the VirtualBox web service and run the service on a **headless server**.

For method #2, VirtualBox should first be merged with the `vboxwebsrv` USE flag enabled:

`root `[`#`]`echo "app-emulation/virtualbox vboxwebsrv" >> /etc/portage/package.use/virtualbox`

`root `[`#`]`emerge --ask --oneshot app-emulation/virtualbox`

The web service should then be added to the default runlevel:

`root `[`#`]`rc-update add vboxwebsrv default`

### [][Virtualbox does not start with kernel 6.12+]

If starting virtualbox results in a message similar to \"Virtualbox can\'t enable the AMD-V extension. Please disable the KVM kernel extension, recompile your kernel and reboot\" or \"VirtualBox can\'t operate in VMX root mode. Please disable the KVM kernel extension, recompile your kernel and reboot (VERR_VMX_IN_VMX_ROOT_MODE)\" on a kernel 6.12+, the solution is to append `kvm.enable_virt_at_load=0` to kernel command line and reboot. This happens if KVM is built-in. [See also](https://bugs.gentoo.org/945135#c1)

### [Crash when playing sound]

If VirtualBox crashes when first playing a sound, a solution might be to change the sound settings (from Default to [PulseAudio](https://wiki.gentoo.org/wiki/PulseAudio "PulseAudio"), for example).

### [Virtual machine does not start with kernel 6.15.x]

Starting with kernel 6.15.0, virtualbox-drivers need to be compiled against a kernel that already has CONFIG_KVM enabled, or else virtual machines fail to start with an error similar to this:

\"ERROR \[COM\]: aRC=VBOX_E_VM_ERROR (0x80bb0003) aIID= aComponent= aText=, preserve=false aResultDetail=0\"

## [See also]

-   [PhpVirtualBox](https://wiki.gentoo.org/wiki/PhpVirtualBox "PhpVirtualBox") --- a web-based administration utility for [VirtualBox].
-   [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU") --- a generic, open-source hardware emulator and virtualization suite.
-   [Virtualization](https://wiki.gentoo.org/wiki/Virtualization "Virtualization") --- the concept and technique that permits running software in an environment separate from a computer operating system.
-   [VMware](https://wiki.gentoo.org/wiki/VMware "VMware")

## [External resources]

-   [vboxweb_rb](https://github.com/KieranP/vboxweb_rb) - Web-based administration utility ([Ruby](https://wiki.gentoo.org/wiki/Ruby "Ruby"))
-   [VirtualBox Manual](http://www.virtualbox.org/manual/)

## [References]

1.  [[[↑](#cite_ref-1)] [[https://www.virtualbox.org/wiki/Guest_resizing](https://www.virtualbox.org/wiki/Guest_resizing)]]
2.  [[[↑](#cite_ref-2)] [Section_8. [VirtualBox - No sound after update](https://forums.gentoo.org/viewtopic-t-1104042.html), [Gentoo Forums](https://forums.gentoo.org/), November 12th, 2019. Retrieved on September 14th, 2020.]]