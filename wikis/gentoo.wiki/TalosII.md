**Resources**

[[]][Home](https://www.raptorcs.com/TALOSII/)

The Talos II is a dual socket Power 9 motherboard from Raptor Computing Systems. It features opensource firmware and [openBMC](https://www.openbmc.org/).

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [OpenBMC]](#OpenBMC)
    -   [[2.2] [Kernel]](#Kernel)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Bootloader]](#Bootloader)

## [Hardware]

### [Standard]

  ------------ ----------------- -------- ------------------------ ------------------ ---------------- -----------------------------------------------------------------------------------------------------------------------------
  Device       Make/model        Status   Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  CPU          IBM Power 9       Works    N/A                      N/A                4.17.12          Requires kernel version 4.16+, ideally 4.17+. Also benefits from very recent gcc releases.
  Video card   ASpeed Graphics   Works    1a03:2000                ast                4.17.12          Kernel driver works without issue. xf86-video-ast has build issues, xf86-video-modesetting works fine with glamor disabled.
  ------------ ----------------- -------- ------------------------ ------------------ ---------------- -----------------------------------------------------------------------------------------------------------------------------

## [Installation]

The system uses [petitboot](https://github.com/open-power/petitboot) as main bootloader. The grub based ppc64le install media iso contents can be copied to a partition of an usb storage and used.

Make sure to pass **console=hvc0** as boot argument if you are using the OpenBMC console.

### [OpenBMC]

The [openbmc](https://www.openbmc.org/) will ask for an address if the first Ethernet port is connected. It would listen to port 22 and port 2200. Petitboot will be directly reachable from port 2200.

### [Kernel]

Use powernv_defconfig.

To enable hardware accelerated virtualization:

[KERNEL] **Enable hardware virtualization, kvm_hv**

    --- Virtualization
    <M>   KVM support for PowerPC book3s_64 processors
    <M>     KVM for POWER7 and later using hypervisor mode in host
    < >     KVM support without using hypervisor mode in host

## [Configuration]

### [Bootloader]

The Talos uses petitboot as part of its firmware and bootloader. This means there is no need to install grub/yaboot/etc, as all petitboot needs is the config file. kboot has a delightfully simple config format, which is easily written.