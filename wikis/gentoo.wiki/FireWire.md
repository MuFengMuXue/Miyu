**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/IEEE_1394 "wikipedia:IEEE 1394")

This article describes the setup of FireWire (IEEE 1394, i.Link) controllers.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel configuration]](#Kernel_configuration)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [External resources]](#External_resources)

## [Installation]

### [Kernel configuration]

For FireWire support, the following kernel options need to be activated:

[KERNEL] **Add FireWire driver support**

    Device Drivers --->
        IEEE 1394 (FireWire) support  --->
            <*> FireWire driver stack
            <*>   OHCI-1394 controllers

Select additional drivers as needed. For example, a FireWire hard drive may need the following options enabled:

[KERNEL] **Add additional driver support**

    Device Drivers --->
        SCSI device support --->
            <*> SCSI device support
            <*> SCSI disk support
        IEEE 1394 (FireWire) support  --->
            <*>   Storage devices (SBP-2 protocol)

### [USE flags]

Portage knows the global USE flag `ieee1394` for enabling support for FireWire in other packages. Enabling this USE flag will pull in [[[sys-libs/libraw1394]](https://packages.gentoo.org/packages/sys-libs/libraw1394)[]] automatically:

[FILE] **`/etc/portage/make.conf`**

    USE="... ieee1394 ..."

### [USE flags for] [sys-libs/libraw1394](https://packages.gentoo.org/packages/sys-libs/libraw1394) [[]] [Library that provides direct access to the IEEE 1394 bus]

  ------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------
  [`valgrind`](https://packages.gentoo.org/useflags/valgrind)   Enable annotations for accuracy. May slow down runtime slightly. Safe to use even if not currently using dev-debug/valgrind
  ------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-09-02 17:00] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

After setting the USE flag above update the system so the changes take effect:

`root `[`#`]`emerge --ask --changed-use --deep @world`

## [External resources]

-   [FireWire kernel wiki](https://ieee1394.wiki.kernel.org/)