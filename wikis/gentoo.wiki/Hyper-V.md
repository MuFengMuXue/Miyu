[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Hyper-V&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.microsoft.com/en-us/server-cloud/solutions/virtualization.aspx)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Hyper-V "wikipedia:Hyper-V")

Hyper-V is a [hypervisor](https://en.wikipedia.org/wiki/Hypervisor "wikipedia:Hypervisor") integrated in current versions of Microsoft Windows. This article covers the specifics of *running Gentoo as a* ***guest*** *operating system* inside a Hyper-V [virtual machine](https://en.wikipedia.org/wiki/virtual_machine "wikipedia:virtual machine").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
        -   [[1.1.1] [Linux guest support]](#Linux_guest_support)
        -   [[1.1.2] [Graphics]](#Graphics)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Integration Services]](#Integration_Services)
-   [[2] [Removal]](#Removal)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Installation]

Hyper-V support for Gentoo guests requires two important steps: kernel support and user-space graphic driver support.

** Note**\
This configuration is only pertinent to a Gentoo installation (guest) running ***as*** a virtual machine.

### [Kernel]

#### [Linux guest support]

Below is a summary of the kernel features that need to be compiled into the kernel, or provided as kernel modules, to be able to correctly run Gentoo under Hyper-V. Feature names are subject to change, so be sure to search the kernel\'s menuconfig for features containing the string `HYPERV`.

[KERNEL] **Enable basic Hyper-V guest support**

    Processor type and features  --->
       [*] Linux guest support  --->
          -*-   Enable paravirtualization code
          [*]     Paravirtualization layer for spinlocks
    Power management and ACPI options  --->
       [*] ACPI (Advanced Configuration and Power Interface) Support  --->
    [*] Networking support  --->
       Networking options  --->
          <*> Virtual Socket protocol
          <*> Hyper-V transport for Virtual Sockets
    Device Drivers  --->
       [*] PCI support
          [*] Message Signaled Interrupts (MSI and MSI-X)
          <*> Hyper-V PCI Frontend
       SCSI device support  --->
          SCSI Transports  --->
             <*> FiberChannel Transport Attributes
          [*] SCSI low-level drivers  --->
             <*> Microsoft Hyper-V virtual storage driver
       [*] Network device support  --->
          <*>   Microsoft Hyper-V virtual network driver
       Input device support  --->
          Hardware I/O ports  --->
             <*> Microsoft Synthetic Keyboard driver
       Graphics support  --->
          Frame buffer Devices  --->
             <*> Support for frame buffer devices  --->
                <*> Microsoft Hyper-V Synthetic Video support
       HID support  --->
          -*- HID bus support
          Special HID drivers  --->
             <*> Microsoft Hyper-V mouse driver
       Microsoft Hyper-V guest support  --->
          <*> Microsoft Hyper-V client drivers
          <*> Microsoft Hyper-V Utilities driver
          <*> Microsoft Hyper-V Balloon driver

To have all necessary options appear, there is an initial dependency chain. \"Linux guest support\" and \"ACPI\" must be enabled first in order for \"Microsoft Hyper-V client drivers\" to appear. \"Microsoft Hyper-V client drivers\" is necessary for most, if not all, other Hyper-V options to be available.

#### [Graphics]

For X11 (graphical) support the `CONFIG_DRM_FBDEV_EMULATION` kernel option is required:

[KERNEL] **Enable graphical support via fbdev**

    Device Drivers  --->
       Graphics support  --->
          <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support)  --->
             [*]   Enable legacy fbdev support for your modesetting driver

### [Emerge]

If X server graphical support is desired through fbdev, be sure to adjust [/etc/portage/package.use]:

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* fbdev

Next (re)emerge xorg-drivers package:

`root `[`#`]`emerge --ask --update --newuse --deep x11-base/xorg-drivers`

### [Integration Services]

Sources for the integration services can be found in the kernel source tree. Unfortunatly there is no support from Gentoo for the integration services at time of writing, so manual setup is required:

`root `[`#`]`cd /usr/src/linux/tools/hv/ `

`root `[`#`]`make install`

Next adjust the helpers to fit your system. For documentation, see the comments inside the files.

`root `[`#`]`vim /usr/libexec/hypervkvpd/hv_get_dhcp_info `

`root `[`#`]`vim /usr/libexec/hypervkvpd/hv_get_dns_info `

`root `[`#`]`vim /usr/libexec/hypervkvpd/hv_set_ifconfig `

Finally, make sure the three daemons are started on boot. Again, you will have to write the services yourself. This should however be pretty straightforward, as they do not require any configuration.

## [Removal]

Removing the Hyper-V support is as simple as disabling the related kernel options (reverse the steps in the [Kernel section](#Kernel) above) and removing the files installed in the [Integration Services section](#Integration_Services).

## [See also]

-   [Virtualization](https://wiki.gentoo.org/wiki/Virtualization "Virtualization") --- the concept and technique that permits running software in an environment separate from a computer operating system.
-   [Xen](https://wiki.gentoo.org/wiki/Xen "Xen") --- a native, or bare-metal, [hypervisor](https://en.wikipedia.org/wiki/Hypervisor "wikipedia:Hypervisor") that allows multiple distinct virtual machines (referred to as domains) to share a single physical machine.

## [External resources]

-   [http://www.altaro.com/hyper-v/linux-on-hyper-v/](http://www.altaro.com/hyper-v/linux-on-hyper-v/)
-   [https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/reference/integration-services/](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/reference/integration-services/)