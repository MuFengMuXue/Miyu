This page contains [[changes](https://wiki.gentoo.org/index.php?title=VMware&diff=1430456)] which are not marked for translation.

\

[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=VMware&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.vmware.com/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/VMware "wikipedia:VMware")

VMware, Inc. sells a variety of closed-source hypervisors. \"VMware\" can refer to both the company or its products.

** Important**\
VMware works best on a systemd system and although it can be forced to work on an OpenRC system, it is suboptimal and not recommended.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Required kernel options]](#Required_kernel_options)
    -   [[1.2] [Kernel modules]](#Kernel_modules)
    -   [[1.3] [systemd services]](#systemd_services)
    -   [[1.4] [Uninstallation]](#Uninstallation)
-   [[2] [Gentoo guests]](#Gentoo_guests)
    -   [[2.1] [Kernel Configuration]](#Kernel_Configuration)
    -   [[2.2] [Emerge]](#Emerge)
    -   [[2.3] [vmware-tools service]](#vmware-tools_service)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [VMware\'s GUI window closes when the cursor is moved out of the window]](#VMware.27s_GUI_window_closes_when_the_cursor_is_moved_out_of_the_window)
-   [[4] [See also]](#See_also)

## [Installation]

When installing VMware Workstation on Gentoo you need to download the bundle from [VMware\'s website](https://blogs.vmware.com/workstation/2024/05/vmware-workstation-pro-now-available-free-for-personal-use.html).

`root `[`#`]`bash VMware-Workstation-Full-16.1.2-17966106.x86_64.bundle`

** Note**\
Both `VMware-Workstation-Full-25H2-24995812.x86_64.bundle` and `VMware-Workstation-Full-17.5.2-23775571.x86_64.bundle` have been tested and can be easily installed following the steps above.

### [Required kernel options]

To install and run VMware Workstation on Gentoo you need to enable next kernel options:

[KERNEL] **Kernel configuration for VMware Workstation/Player hosts**

    Processor type and features  --->
        [*] IOPERM and IOPL Emulation Search for <code>CONFIG_X86_IOPL_IOPERM</code> to find this item.
    [*] Enable loadable module support ---> Search for <code>CONFIG_MODULES</code> to find this item.
    File systems  --->
        <*/M> FUSE (Filesystem in Userspace) support Search for <code>CONFIG_FUSE_FS</code> to find this item.
    Device Drivers  --->
       Misc devices  --->
           <*/M> VMware VMCI Driver Search for <code>CONFIG_VMWARE_VMCI</code> to find this item.

If you require VMware VMCI Sockets for host-guest/guest-guest communication, you need to also enable CONFIG_VMWARE_VMCI_VSOCKETS. This is an optional feature and isn\'t required to run VMware guests.

[KERNEL] **Optional configuration for VMware Workstation/Player hosts**

    [*] Networking support  --->
        Networking options  --->
            <*/M> Virtual Socket protocol Search for <code>CONFIG_VSOCKETS</code> to find this item.
            <*/M>   VMware VMCI transport for Virtual Sockets Search for <code>CONFIG_VMWARE_VMCI_VSOCKETS</code> to find this item.

### [Kernel modules]

VMware Workstation 16.0 is known to support up to linux 5.8, and 16.1 works on 5.10 from my testing. If you use an older version of Workstation it will require an older kernel, 15.5 supports up to 5.4, 14.1.7 suppots up to 4.18, and 12.5.9 supports up to 4.12. After a kernel upgrade you will have to rebuild the VMware modules. You can do this by running the following command.

`root `[`#`]`vmware-modconfig --console --install-all`

\
For kernels greater than 6.9 the following workaround enables VMWare Workstation 17.5:

`root `[`#`]`git clone -b tmp/workstation-17.5.2-k6.9.1 `[`https://github.com/nan0desu/vmware-host-modules.git`](https://github.com/nan0desu/vmware-host-modules.git)

`root `[`#`]`cd vmware-host-modules/`

`root `[`#`]`make`

`root `[`#`]`make install`

To get modules working for VMware Workstation 17.6.3 you need to go deeper in the git and get some unmerged code (as of this writing). I tested this on a 6.12.25 kernel.

`user `[`$`]`git clone `[`https://github.com/mkubecek/vmware-host-modules.git`](https://github.com/mkubecek/vmware-host-modules.git)

`user `[`$`]`cd vmware-host/modules/`

`user `[`$`]`git fetch origin pull/303/head:pr-303`

`user `[`$`]`git checkout pr-303`

`user `[`$`]`make`

`root `[`#`]`make install`

### [systemd services]

If you are using systemd you might want to create some systemd service files to start VMware services on startup using systemd.

[FILE] **`/etc/systemd/system/vmware.service`**

    [Unit]
    Description=VMware daemon
    Requires=vmware-usbarbitrator.service
    Before=vmware-usbarbitrator.service
    After=network.target

    [Service]
    ExecStart=/etc/init.d/vmware start
    ExecStop=/etc/init.d/vmware stop
    PIDFile=/var/lock/subsys/vmware
    RemainAfterExit=yes

    [Install]
    WantedBy=multi-user.target

[FILE] **`/etc/systemd/system/vmware-usbarbitrator.service`**

    [Unit]
    Description=VMware USB Arbitrator
    Requires=vmware.service
    After=vmware.service

    [Service]
    ExecStart=/usr/bin/vmware-usbarbitrator
    ExecStop=/usr/bin/vmware-usbarbitrator --kill
    RemainAfterExit=yes

    [Install]
    WantedBy=multi-user.target

If you want to enable networking, add this service:

[FILE] **`/etc/systemd/system/vmware-networks-server.service`**

    [Unit]
    Description=VMware Networks
    Wants=vmware-networks-configuration.service
    After=vmware-networks-configuration.service

    [Service]
    Type=forking
    ExecStartPre=-/sbin/modprobe vmnet
    ExecStart=/usr/bin/vmware-networks --start
    ExecStop=/usr/bin/vmware-networks --stop

    [Install]
    WantedBy=multi-user.target

If you want to connect to your VMware Workstation from another server:

[FILE] **`/etc/systemd/system/vmware-workstation-server.service`**

    [Unit]
    Description=VMware Workstation Server
    Requires=vmware.service
    After=vmware.service

    [Service]
    ExecStart=/etc/init.d/vmware-workstation-server start
    ExecStop=/etc/init.d/vmware-workstation-server stop
    PIDFile=/var/lock/subsys/vmware-workstation-server
    RemainAfterExit=yes

    [Install]
    WantedBy=multi-user.target

### [Uninstallation]

If you use systemd and created systemd service files, you should delete them first:

`root `[`#`]`systemctl disable --now vmware.service vmware-networks-server.service vmware-workstation-server.service`

`root `[`#`]`rm /etc/systemd/system/vmware.service /etc/systemd/system/vmware.service /etc/systemd/system/vmware-networks-server.service /etc/systemd/system/vmware-workstation-server.service`

VMware Workstation has an uninstaller, and can be uninstalled.

`root `[`#`]`vmware-installer -u vmware-workstation`

## [Gentoo guests]

Running Gentoo Linux as a guest inside of VMware Workstation requires enabling some kernel modules and installing [[[app-emulation/open-vm-tools]](https://packages.gentoo.org/packages/app-emulation/open-vm-tools)[]].

### [Kernel Configuration]

When working with VMware ESXi, despite the Ethernet emulator stating it would be an Intel e1000e, the guest OS was presented with an AMD Ethernet adapter. Both are included for completeness as well as the e1000.

[KERNEL]

    Device Drivers  --->
            [*] Fusion MPT device support  --->
                    <*>   Fusion MPT ScsiHost drivers for SPI
                Misc devices  --->
                    <*> VMware Balloon Driver
                    <*> VMware VMCI Driver
                SCSI device support  --->
                    [*] SCSI low-level drivers  --->
                       <*>   VMware PVSCSI driver support
            [*] Network device support  --->
                    [*]   Ethernet driver support  --->
                        [*]   AMD devices
                        <*>     AMD 8111 (new PCI LANCE) support
                        <*>     AMD PCnet32 PCI support
                        [*]   Intel devices
                        <*>     Intel(R) PRO/1000 Gigabit Ethernet support
                        <*>     Intel(R) PRO/1000 PCI-Express Gigabit Ethernet support
                    <*>   VMware VMXNET3 ethernet driver
                Input device support  --->
                    [*]   Keyboards  --->
                        <*>   AT keyboard
                    [*]   Mice  --->
                        [*]   PS/2 mouse
                        [*]     Virtual mouse (vmmouse)
                Graphics support  --->
                    <*> DRM driver for VMware Virtual GPU
                    [*]   Enable mksGuestStats instrumentation of vmwgfx by default
                        Frame buffer Devices  --->
                        <*> Support for frame buffer devices  --->
        File systems  --->
            <*> FUSE (Filesystem in Userspace) support

** Note**\
The `VMware Balloon Driver` option is visible only once the `VMware VMCI Driver` option is enabled, and the `Enable framebuffer console under vmwgfx by default` option is visible only once the `Support for frame buffer devices` option is enabled.

The keywords for the above options are:

-   CONFIG_FUSION
-   CONFIG_FUSION_SPI
-   CONFIG_NET_VENDOR_AMD
-   CONFIG_AMD8111_ETH
-   CONFIG_PCNET32
-   CONFIG_NET_VENDOR_INTEL
-   CONFIG_E1000
-   CONFIG_E1000E
-   CONFIG_KEYBOARD_ATKBD
-   CONFIG_VMWARE_BALLOON
-   CONFIG_VMWARE_VMCI
-   CONFIG_VMWARE_PVSCSI
-   CONFIG_VMXNET3
-   CONFIG_MOUSE_PS2_VMMOUSE
-   CONFIG_DRM_VMWGFX
-   CONFIG_DRM_VMWGFX_MKSSTATS
-   CONFIG_FB
-   CONFIG_FUSE_FS

If you require VMware VMCI Sockets for host-guest/guest-guest communication, you need to also enable CONFIG_VMWARE_VMCI_VSOCKETS. This is an optional feature and isn\'t required to run VMware guests.

[KERNEL]

    [*] Networking support  --->
            Networking options  --->
                <*> Virtual Socket protocol
                <*>   VMware VMCI transport for Virtual Sockets

### [Emerge]

Install [[[app-emulation/open-vm-tools]](https://packages.gentoo.org/packages/app-emulation/open-vm-tools)[]]:

`root `[`#`]`emerge --ask app-emulation/open-vm-tools`

### [vmware-tools service]

Start the service:

`root `[`#`]`rc-service vmware-tools start`

And, add the vmware-tools service to the default run level.

`root `[`#`]`rc-update add vmware-tools`

## [Troubleshooting]

### [][VMware\'s GUI window closes when the cursor is moved out of the window]

This is due to a [[[x11-libs/libX11]](https://packages.gentoo.org/packages/x11-libs/libX11)[]] bug when running VMware under a Wayland session. As of December 6th, 2025, the patch that solves this has yet to be merged, but a temporary fix can be applied via [user patches](https://wiki.gentoo.org/wiki//etc/portage/patches#Adding_user_patches "/etc/portage/patches"). The specific patch to be added to [/etc/portage/patches/x11-libs/libX11-1.8.12] is from this merge request: [https://gitlab.freedesktop.org/xorg/lib/libx11/-/merge_requests/293](https://gitlab.freedesktop.org/xorg/lib/libx11/-/merge_requests/293).

## [See also]

-   [Virtualization](https://wiki.gentoo.org/wiki/Virtualization "Virtualization") --- the concept and technique that permits running software in an environment separate from a computer operating system.