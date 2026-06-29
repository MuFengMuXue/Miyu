[] The information in this article is probably **outdated**. You can help the Gentoo community by verifying and [updating this article](https://wiki.gentoo.org/index.php?title=Lenovo_Thinkpad_E531&action=edit).

**Resources**

[[]][Home](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-edge-laptops/thinkpad-edge-e531)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_E531/ThinkPad_E531_Spec.PDF)

[[]][Specifications (by region)](https://psref.lenovo.com/Product/ThinkPad/ThinkPad_E531)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/ibmdl/pub/pc/pccbbs/mobiles_pdf/edge_e531_hmm_en_0c10929_01.pdf)

[[]][User Guide](https://download.lenovo.com/ibmdl/pub/pc/pccbbs/mobiles_pdf/e431_e531_ug_en.pdf)

[[]][BIOS Setup](https://download.lenovo.com/pccbbs/mobiles_pdf/lenovo_bios_setup_linux_wmi_sysfs_1.2.pdf)

[[]][ThinkPad E series](https://en.wikipedia.org/wiki/ThinkPad_E_series "wikipedia:ThinkPad E series")

## Contents

-   [[1] [Hardware]](#Hardware)
-   [[2] [UEFI update]](#UEFI_update)
-   [[3] [Installation]](#Installation)
    -   [[3.1] [Firmware]](#Firmware)
    -   [[3.2] [Kernel]](#Kernel)
    -   [[3.3] [Emerge]](#Emerge)
-   [[4] [Configuration]](#Configuration)
    -   [[4.1] [Screen backlight controls]](#Screen_backlight_controls)

## [Hardware]

`root `[`#`]`lspci`

    00:00.0 Host bridge [0600]: Intel Corporation 3rd Gen Core processor DRAM Controller [8086:0154] (rev 09)
        Subsystem: Lenovo Device [17aa:5018]
    00:02.0 VGA compatible controller [0300]: Intel Corporation 3rd Gen Core processor Graphics Controller [8086:0166] (rev 09)
        Subsystem: Lenovo Device [17aa:5018]
        Kernel driver in use: i915
    00:14.0 USB controller [0c03]: Intel Corporation 7 Series/C210 Series Chipset Family USB xHCI Host Controller [8086:1e31] (rev 04)
        Subsystem: Lenovo Device [17aa:5018]
        Kernel driver in use: xhci_hcd
    00:16.0 Communication controller [0780]: Intel Corporation 7 Series/C210 Series Chipset Family MEI Controller #1 [8086:1e3a] (rev 04)
        Subsystem: Lenovo Device [17aa:5018]
        Kernel driver in use: mei_me
        Kernel modules: mei_me
    00:1a.0 USB controller [0c03]: Intel Corporation 7 Series/C210 Series Chipset Family USB Enhanced Host Controller #2 [8086:1e2d] (rev 04)
        Subsystem: Lenovo Device [17aa:5018]
        Kernel driver in use: ehci-pci
    00:1b.0 Audio device [0403]: Intel Corporation 7 Series/C210 Series Chipset Family High Definition Audio Controller [8086:1e20] (rev 04)
        Subsystem: Lenovo Device [17aa:5018]
        Kernel driver in use: snd_hda_intel
    00:1c.0 PCI bridge [0604]: Intel Corporation 7 Series/C210 Series Chipset Family PCI Express Root Port 1 [8086:1e10] (rev c4)
        Kernel driver in use: pcieport
    00:1c.1 PCI bridge [0604]: Intel Corporation 7 Series/C210 Series Chipset Family PCI Express Root Port 2 [8086:1e12] (rev c4)
        Kernel driver in use: pcieport
    00:1c.3 PCI bridge [0604]: Intel Corporation 7 Series/C210 Series Chipset Family PCI Express Root Port 4 [8086:1e16] (rev c4)
        Kernel driver in use: pcieport
    00:1d.0 USB controller [0c03]: Intel Corporation 7 Series/C210 Series Chipset Family USB Enhanced Host Controller #1 [8086:1e26] (rev 04)
        Subsystem: Lenovo Device [17aa:5018]
        Kernel driver in use: ehci-pci
    00:1f.0 ISA bridge [0601]: Intel Corporation HM77 Express Chipset LPC Controller [8086:1e57] (rev 04)
        Subsystem: Lenovo Device [17aa:5018]
        Kernel driver in use: lpc_ich
        Kernel modules: lpc_ich
    00:1f.2 SATA controller [0106]: Intel Corporation 7 Series Chipset Family 6-port SATA Controller [AHCI mode] [8086:1e03] (rev 04)
        Subsystem: Lenovo Device [17aa:5018]
        Kernel driver in use: ahci
    00:1f.3 SMBus [0c05]: Intel Corporation 7 Series/C210 Series Chipset Family SMBus Controller [8086:1e22] (rev 04)
        Subsystem: Lenovo Device [17aa:5018]
    03:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS5229 PCI Express Card Reader [10ec:5229] (rev 01)
        Subsystem: Lenovo Device [17aa:5018]
        Kernel driver in use: rtsx_pci
        Kernel modules: rtsx_pci
    04:00.0 Network controller [0280]: Intel Corporation Centrino Wireless-N 2230 [8086:0888] (rev c4)
        Subsystem: Intel Corporation Centrino Wireless-N 2230 BGN [8086:4262]
        Kernel driver in use: iwlwifi
        Kernel modules: iwlwifi
    05:00.0 Ethernet controller [0200]: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller [10ec:8168] (rev 07)
        Subsystem: Lenovo Device [17aa:5018]
        Kernel driver in use: r8169
        Kernel modules: r8169

## [UEFI update]

`user `[`$`]`wget `[`http://download.gna.org/grub4dos/grub4dos-0.4.4.zip`](http://download.gna.org/grub4dos/grub4dos-0.4.4.zip)` `

`user `[`$`]`unzip grub4dos-0.4.4.zip `

`user `[`$`]`cd grub4dos-0.4.4 `

Insert usb drive and format it to fat32.

`root `[`#`]`./bootlace.com /dev/sdX`

[/dev/sdX] is the device name assigned to your pendrive. Copy the files [grldr] and [menu.lst] to the root directory of your pendrive. Copy the bios update CD ISO image to the root directory of your pendrive. Edit [menu.lst] on your usb drive:

[FILE] **`menu.lst`**

    title thinkpad-bios
    map (hd0,0)/1yuj18us.iso (hd32)
    map --hook
    chainloader (hd32)
    boot

Reboot and press [F12] to select booting from USB. Now you should be able to boot the Thinkpad\'s ISO image and flash the BIOS.

## [Installation]

### [Firmware]

The wireless card requires external firmware:

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

### [Kernel]

[KERNEL] **Ethernet and Wi-Fi**

    Device Drivers  --->
    [*] Network device support  --->
    [*]   Ethernet driver support  --->
    [*]   Realtek devices
    <M>     Realtek 8169 gigabit ethernet support

    [*]   Wireless LAN  --->
    <M>   Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)
    <M>     Intel Wireless WiFi DVM Firmware support

[KERNEL] **Sensors**

    Device Drivers  --->
    -*- I2C support  --->
    I2C Hardware Bus support  --->
    <*> Intel 82801 (ICH/PCH)

    -*- Hardware Monitoring support  --->
    <M>   Intel Core/Core2/Atom temperature sensor

    [*] X86 Platform Specific Device Drivers  --->
    <M>   ThinkPad ACPI Laptop Extras
    [*]     Console audio control ALSA interface

[KERNEL] **Watchdog**

    Device Drivers  --->
    [*] Watchdog Timer Support  --->
    <M>   Intel TCO Timer/Watchdog
    [*]     Intel TCO Timer/Watchdog Specific Vendor Support

[KERNEL] **Random number generator**

    Device Drivers  --->
    Character devices  --->
    [*]   Intel HW Random Number Generator support

[KERNEL] **Sound**

    Device Drivers  --->
    <*> Sound card support  --->
    <*>   Advanced Linux Sound Architecture  --->
    [*]   PCI sound devices  --->
    <*>   Intel HD Audio  --->
    <*>   Build HDMI/DisplayPort HD-audio codec support
    <*>   Build Conexant HD-audio codec support

### [Emerge]

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* intel i965

Sensor monitoring program:

`root `[`#`]`emerge --ask sys-apps/lm-sensors`

## [Configuration]

### [Screen backlight controls]

Add `acpi_osi='!Windows 2012'` to kernel cmdline ([grub.cfg]).