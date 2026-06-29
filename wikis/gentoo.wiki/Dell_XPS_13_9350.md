**Resources**

[[]][Official Support Page](https://www.dell.com/support/home/en-us/product-support/product/xps-13-9350-laptop/overview)

[[]][Specifications](https://dl.dell.com/manuals/all-products/esuprt_laptop/esuprt_xps_laptop/xps-13-9350-laptop_reference%20guide_en-us.pdf)

[[]][Hardware Maintenance Manual](https://dl.dell.com/topicspdf/xps-13-9350-laptop_service-manual_en-us.pdf)

This article is currently a WIP. Please add to it.

As Dell makes several differently configured laptops under the same model name, this article is based upon the P54G version. (you can look up yours under the hatch, after \"Reg Model\".

## Contents

-   [[1] [Hardware]](#Hardware)
-   [[2] [Wi-Fi]](#Wi-Fi)
    -   [[2.1] [Kernel Options]](#Kernel_Options)
    -   [[2.2] [Firmware]](#Firmware)
        -   [[2.2.1] [When using built-in configuration]](#When_using_built-in_configuration)
-   [[3] [Kernel Modules & Drivers]](#Kernel_Modules_.26_Drivers)
    -   [[3.1] [SMBus]](#SMBus)
    -   [[3.2] [PCI-E Card Reader]](#PCI-E_Card_Reader)
    -   [[3.3] [Memory Controller]](#Memory_Controller)
    -   [[3.4] [CPU]](#CPU)
    -   [[3.5] [Touchscreen]](#Touchscreen)
    -   [[3.6] [NVMe]](#NVMe)
    -   [[3.7] [Sata Controller]](#Sata_Controller)
    -   [[3.8] [Webcam]](#Webcam)
    -   [[3.9] [Bluetooth]](#Bluetooth)
    -   [[3.10] [Sound]](#Sound)
-   [[4] [Graphics]](#Graphics)
    -   [[4.1] [Kernel]](#Kernel)
    -   [[4.2] [Firmware]](#Firmware_2)
-   [[5] [Microcode]](#Microcode)
    -   [[5.1] [Installing with UEFI System]](#Installing_with_UEFI_System)
-   [[6] [Driver Summary]](#Driver_Summary)
-   [[7] [Remaining boot issues]](#Remaining_boot_issues)

## [Hardware]

  ----------- --------------------------
  Class       Product
  Processor   Intel® Core I5-6200U CPU
  Wi-Fi       Intel Wifi 8260
  Bluetooth   Intel Bluetooth
  Audio       Intel HD Audio
  Graphics    Intel HD Graphics 520
  ----------- --------------------------

`root `[`#`]`lspci -nn`

    00:00.0 Host bridge [0600]: Intel Corporation Sky Lake Host Bridge/DRAM Registers [8086:1904] (rev 08)
    00:02.0 VGA compatible controller [0300]: Intel Corporation Sky Lake Integrated Graphics [8086:1916] (rev 07)
    00:04.0 Signal processing controller [1180]: Intel Corporation Device [8086:1903] (rev 08)
    00:14.0 USB controller [0c03]: Intel Corporation Device [8086:9d2f] (rev 21)
    00:14.2 Signal processing controller [1180]: Intel Corporation Device [8086:9d31] (rev 21)
    00:15.0 Signal processing controller [1180]: Intel Corporation Device [8086:9d60] (rev 21)
    00:15.1 Signal processing controller [1180]: Intel Corporation Device [8086:9d61] (rev 21)
    00:16.0 Communication controller [0780]: Intel Corporation Device [8086:9d3a] (rev 21)
    00:17.0 SATA controller [0106]: Intel Corporation Device [8086:9d03] (rev 21)
    00:1c.0 PCI bridge [0604]: Intel Corporation Device [8086:9d10] (rev f1)
    00:1c.4 PCI bridge [0604]: Intel Corporation Device [8086:9d14] (rev f1)
    00:1c.5 PCI bridge [0604]: Intel Corporation Device [8086:9d15] (rev f1)
    00:1f.0 ISA bridge [0601]: Intel Corporation Device [8086:9d48] (rev 21)
    00:1f.2 Memory controller [0580]: Intel Corporation Device [8086:9d21] (rev 21)
    00:1f.3 Audio device [0403]: Intel Corporation Device [8086:9d70] (rev 21)
    00:1f.4 SMBus [0c05]: Intel Corporation Device [8086:9d23] (rev 21)
    3a:00.0 Network controller [0280]: Intel Corporation Wireless 8260 [8086:24f3] (rev 3a)
    3b:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. Device [10ec:525a] (rev 01)

`root `[`#`]`lsusb`

    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 002: ID 8087:0a2b Intel Corp.
    Bus 001 Device 003: ID 0c45:670c Microdia
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

# [Wi-Fi]

## [Kernel Options]

We\'re trying to make [iwlwifi](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi") work, for more information go to the specific [iwlwifi](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi") article. After enabling the basic 802.11 support kernel options, let\'s enable the driver !

[KERNEL]

            Device Drivers  --->
            [*] Network device support  --->
            --- Network device support
            [*]   Wireless LAN  --->
                --- Wireless LAN
                [*]   Intel devices
                < >     Intel PRO/Wireless 2100 Network Connection
                < >     Intel PRO/Wireless 2200BG and 2915ABG Network Connection
                < >     Intel Wireless WiFi 4965AGN (iwl4965)
                < >     Intel PRO/Wireless 3945ABG/BG Network Connection (iwl3945)
                <M>     Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)
                <M>       Intel Wireless WiFi DVM Firmware support
                <M>       Intel Wireless WiFi MVM Firmware support

## [Firmware]

Firmware for the 8260 chip is needed. It is available in [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]]:

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

### [When using built-in configuration]

In case the driver is built into the kernel (`<*>`) instead as a module (`<M>`), also the firmware needs to be built [into the kernel](https://wiki.gentoo.org/wiki/Kernel_Modules#Compile-in-kernel_modules_vs_Loadable_kernel_modules_.28LKMs.29 "Kernel Modules").

[KERNEL]

            Device Drivers  --->
                Generic Driver Options  --->
                -*- Userspace firmware loading support
                [ ]   Include in-kernel firmware blobs in kernel binary
                (iwlwifi-8000C-XX.ucode) External firmware blobs to build into the kernel binary
                (/lib/firmware) Firmware blobs root directory
                [ ] Fallback user-helper invocation for firmware loading

(Replace the XX with the latest version)

# [][Kernel Modules & Drivers]

## [SMBus]

`root `[`#`]`lspci -nn -k`

    00:1f.4 SMBus [0c05]: Intel Corporation Sunrise Point-LP SMBus [8086:9d23] (rev 21)
        Subsystem: Dell Sunrise Point-LP SMBus [1028:0704]
        Kernel driver in use: i801_smbus

## [PCI-E Card Reader]

`root `[`#`]`lspci -nn -k`

    3b:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS525A PCI Express Card Reader [10ec:525a] (rev 01)
        Subsystem: Dell RTS525A PCI Express Card Reader [1028:0704]
        Kernel driver in use: rtsx_pci
        Kernel modules: rtsx_pci

## [Memory Controller]

`root `[`#`]`lspci -nn -k`

    00:1f.2 Memory controller [0580]: Intel Corporation Sunrise Point-LP PMC [8086:9d21] (rev 21)
        Subsystem: Dell Sunrise Point-LP PMC [1028:0704]
        Kernel driver in use: intel_pmc_core

## [CPU]

`root `[`#`]`lspci -nn -k`

    00:04.0 Signal processing controller [1180]: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem [8086:1903] (rev 08)
        Subsystem: Dell Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem [1028:0704]
        Kernel driver in use: proc_thermal
        Kernel modules: processor_thermal_device
    00:14.2 Signal processing controller [1180]: Intel Corporation Sunrise Point-LP Thermal subsystem [8086:9d31] (rev 21)
        Subsystem: Dell Sunrise Point-LP Thermal subsystem [1028:0704]
        Kernel driver in use: intel_pch_thermal
        Kernel modules: intel_pch_thermal
    00:16.0 Communication controller [0780]: Intel Corporation Sunrise Point-LP CSME HECI #1 [8086:9d3a] (rev 21)
        Subsystem: Dell Sunrise Point-LP CSME HECI [1028:0704]
        Kernel driver in use: mei_me

## [Touchscreen]

`root `[`#`]`lspci -nn -k`

    00:15.0 Signal processing controller [1180]: Intel Corporation Sunrise Point-LP Serial IO I2C Controller #0 [8086:9d60] (rev 21)
        Subsystem: Dell Sunrise Point-LP Serial IO I2C Controller [1028:0704]
        Kernel driver in use: intel-lpss
        Kernel modules: intel_lpss_pci
    00:15.1 Signal processing controller [1180]: Intel Corporation Sunrise Point-LP Serial IO I2C Controller #1 [8086:9d61] (rev 21)
        Subsystem: Dell Sunrise Point-LP Serial IO I2C Controller [1028:0704]
        Kernel driver in use: intel-lpss
        Kernel modules: intel_lpss_pci

## [NVMe]

`root `[`#`]`lspci -nn -k`

    3c:00.0 Non-Volatile memory controller [0108]: Toshiba America Info Systems Device [1179:0115] (rev 01)
        Subsystem: Toshiba America Info Systems Device [1179:0001]
        Kernel driver in use: nvme

## [Sata Controller]

`root `[`#`]`lspci -nn -k`

    00:17.0 SATA controller [0106]: Intel Corporation Sunrise Point-LP SATA Controller [AHCI mode] [8086:9d03] (rev 21)
        Subsystem: Dell Sunrise Point-LP SATA Controller [AHCI mode] [1028:0704]
        Kernel driver in use: ahci

## [Webcam]

`root `[`#`]`lsusb -t`

    /:  Bus 02.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/6p, 5000M
    /:  Bus 01.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/12p, 480M
        |__ Port 5: Dev 4, If 0, Class=Video, Driver=uvcvideo, 480M
        |__ Port 5: Dev 4, If 1, Class=Video, Driver=uvcvideo, 480M

[KERNEL]

    .config - Linux/x86 4.14.65-gentoo Kernel Configuration
     → Device Drivers → Multimedia support →
    [*]   Cameras/video grabbers support
    [*]   Media USB Adapters  --->
           <M>   USB Video Class (UVC)
           [*]     UVC input events device support

## [Bluetooth]

`root `[`#`]`lsusb -t`

    /:  Bus 02.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/6p, 5000M
    /:  Bus 01.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/12p, 480M
        |__ Port 3: Dev 2, If 0, Class=Wireless, Driver=btusb, 12M
        |__ Port 3: Dev 2, If 1, Class=Wireless, Driver=btusb, 12M

[KERNEL]

    .config - Linux/x86 4.9.95-gentoo Kernel Configuration
     → Search (CONFIG_BT_HCIBTUSB)

     Symbol: BT_HCIBTUSB [=m]
     Type  : tristate
     Prompt: HCI USB driver
     Location:
      │     -> Networking support (NET [=y])
      │       -> Bluetooth subsystem support (BT [=m])│
      │ (1)     -> Bluetooth device drivers│
      │   Defined at drivers/bluetooth/Kconfig:21│
      │   Depends on: NET [=y] && BT [=m] && USB [=y]│
      │   Selects: BT_INTEL [=m]

## [Sound]

`root `[`#`]`lspci -nn -k`

    00:1f.3 Audio device [0403]: Intel Corporation Sunrise Point-LP HD Audio [8086:9d70] (rev 21)
        Subsystem: Dell Sunrise Point-LP HD Audio [1028:0704]
        Kernel driver in use: snd_hda_intel

# [Graphics]

Use intel HD graphics: [intel](https://wiki.gentoo.org/wiki/Intel "Intel").

## [Kernel]

[KERNEL]

    Processor type and features  --->
        [*] MTRR (Memory Type Range Register) support
            Device Drivers  --->
                Graphics support  --->
                    <*> /dev/agpgart (AGP Support)  --->
                        --- /dev/agpgart (AGP Support)
                        < >   AMD Opteron/Athlon64 on-CPU GART support
                        -*-   Intel 440LX/BX/GX, I8xx and E7x05 chipset support
                        < >   SiS chipset support
                        < >   VIA chipset support
                    [ ] VGA Arbitration
                    [ ] Laptop Hybrid Graphics - GPU switching support
                    <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support)  --->
                        --- Direct Rendering Manager (XFree86 4.1.0 and higher DRI support)
                        [*]   Enable legacy fbdev support for your modesetting driver
                    [ ] Allow to specify an EDID data set instead of probing for it
                        I2C encoder or helper chips  --->
                    < > 3dfx Banshee/Voodoo3+
                    < > ATI Rage 128
                    < > ATI Radeon
                    < > AMD GPU
                    < > Nouveau (NVIDIA) cards
                    < > Intel I810
                    <*> Intel 8xx/9xx/G3x/G4x/HD Graphics
                    [ ]   Enable preliminary support for prerelease Intel hardware by default
                    < > Matrox g200/g400
                    < > SiS video cards
                    < > Via unichrome video cards
                    < > Savage video cards
                    < > Virtual GEM provider
                    < > DRM driver for VMware Virtual GPU
                    < > Intel GMA5/600 KMS Framebuffer
                    < > DisplayLink
                    < > AST server chips
                    < > Kernel modesetting driver for MGA G200 server engines
                    < > Cirrus driver for QEMU emulated device
                    < > QXL virtual GPU
                    < > DRM Support for bochs dispi vga interface (qemu stdvga)
                        Display Panels  ----
                        Display Interface Bridges  ----
                        Frame buffer Devices  --->
                    -*- Backlight & LCD device support  --->
                        Console display driver support  --->
                    [*] Bootup logo  --->

## [Firmware]

We need firmware for this Skylake chip, for runtime power management, if it wasn\'t installed before, install [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]]:

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

This time we\'ll include the firmware in the kernel.

[KERNEL]

    Device Drivers  --->
        Generic Driver Options  --->
            -*- Userspace firmware loading support
            [*] Include in-kernel firmware blobs in kernel binary
                (i915/skl_dmc_ver1_27.bin)
                (/lib/firmware) Firmware blobs root directory

If you receive the following error

`root `[`#`]`dmesg`

    i915 0000:00:02.0: Direct firmware load for i915/skl_dmc_ver1_26.bin failed with error -2

We need to patch the firmware to load the 1.27 firmware with this file [Firmware Patch](https://patchwork.freedesktop.org/patch/187559/)

I used this cmd to implement the patch

`root `[`#`]`patch /usr/src/linux/drivers/gpu/drm/i915/intel_csr.c drm-i915-skl-DMC-firmware-for-skylake-v1.27.patch`

# [Microcode]

If you are seeing this message during boot time

`root `[`#`]`dmesg`

    [    0.000000] Using ACPI (MADT) for SMP configuration information
    [    0.000000] ACPI: HPET id: 0x8086a701 base: 0xfed00000
    [    0.000000] [Firmware Bug]: TSC_DEADLINE disabled due to Errata; please update microcode to version: 0xb2 (or later)
    [    0.000000] smpboot: Allowing 4 CPUs, 0 hotplug CPUs
    [    0.000000] PM: Registered nosave memory: [mem 0x00000000-0x00000fff]
    [    0.000000] PM: Registered nosave memory: [mem 0x00058000-0x00058fff]

Installing the Intel Microcode may help.

## [Installing with UEFI System]

Add initramfs to your use flag to allow emerge to copy the microcode file to your /boot partition.

[FILE] **`/etc/portage/make.conf`**

    USE="initramfs"

`root `[`#`]`emerge --ask emerge --ask sys-firmware/intel-microcode`

Now grub should be able to find the /boot/intel_uc.img file

`root `[`#`]`grub-mkconfig -o /boot/grub/grub.cfg`

# [Driver Summary]

`root `[`#`]`lsmod`

    Module                  Size  Used by
    rtsx_pci_sdmmc         20480  0
    mmc_core              126976  1 rtsx_pci_sdmmc
    wmi_bmof               16384  0
    dell_wmi               16384  0
    dell_laptop            24576  0
    dell_smbios            16384  2 dell_wmi,dell_laptop
    dcdbas                 16384  1 dell_smbios
    iwlmvm                311296  0
    x86_pkg_temp_thermal    16384  0
    btusb                  49152  0
    iwlwifi               270336  1 iwlmvm
    btrtl                  16384  1 btusb
    btbcm                  16384  1 btusb
    rtsx_pci               45056  1 rtsx_pci_sdmmc
    btintel                16384  1 btusb
    uvcvideo               90112  0
    videobuf2_vmalloc      16384  1 uvcvideo
    hid_multitouch         24576  0
    videobuf2_memops       16384  1 videobuf2_vmalloc
    bluetooth             393216  5 btrtl,btintel,btbcm,btusb
    videobuf2_v4l2         24576  1 uvcvideo
    processor_thermal_device    16384  0
    videobuf2_core         36864  2 videobuf2_v4l2,uvcvideo
    ecdh_generic           24576  1 bluetooth
    intel_soc_dts_iosf     16384  1 processor_thermal_device
    intel_lpss_pci         20480  0
    intel_pch_thermal      16384  0
    intel_lpss             16384  1 intel_lpss_pci
    mfd_core               16384  2 rtsx_pci,intel_lpss
    wmi                    24576  2 dell_wmi,wmi_bmof
    int3403_thermal        16384  0
    int3400_thermal        16384  0
    intel_hid              16384  0
    acpi_thermal_rel       16384  1 int3400_thermal
    int340x_thermal_zone    16384  2 int3403_thermal,processor_thermal_device
    efivarfs               16384  1
    ecb                    16384  0
    ixgbe                 270336  0
    mdio                   16384  1 ixgbe
    xfs                  1134592  0
    xhci_plat_hcd          16384  0

`root `[`#`]`lsusb -t`

    /:  Bus 02.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/6p, 5000M
    /:  Bus 01.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/12p, 480M
        |__ Port 3: Dev 2, If 0, Class=Wireless, Driver=btusb, 12M
        |__ Port 3: Dev 2, If 1, Class=Wireless, Driver=btusb, 12M
        |__ Port 4: Dev 3, If 0, Class=Human Interface Device, Driver=usbhid, 12M
        |__ Port 5: Dev 4, If 0, Class=Video, Driver=uvcvideo, 480M
        |__ Port 5: Dev 4, If 1, Class=Video, Driver=uvcvideo, 480M

`root `[`#`]`lspci -nn -k`

    00:00.0 Host bridge [0600]: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Host Bridge/DRAM Registers [8086:1904] (rev 08)
        Subsystem: Dell Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Host Bridge/DRAM Registers [1028:0704]
        Kernel driver in use: skl_uncore
    00:02.0 VGA compatible controller [0300]: Intel Corporation HD Graphics 520 [8086:1916] (rev 07)
        Subsystem: Dell HD Graphics 520 [1028:0704]
        Kernel driver in use: i915
    00:04.0 Signal processing controller [1180]: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem [8086:1903] (rev 08)
        Subsystem: Dell Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem [1028:0704]
        Kernel driver in use: proc_thermal
        Kernel modules: processor_thermal_device
    00:14.0 USB controller [0c03]: Intel Corporation Sunrise Point-LP USB 3.0 xHCI Controller [8086:9d2f] (rev 21)
        Subsystem: Dell Sunrise Point-LP USB 3.0 xHCI Controller [1028:0704]
        Kernel driver in use: xhci_hcd
    00:14.2 Signal processing controller [1180]: Intel Corporation Sunrise Point-LP Thermal subsystem [8086:9d31] (rev 21)
        Subsystem: Dell Sunrise Point-LP Thermal subsystem [1028:0704]
        Kernel driver in use: intel_pch_thermal
        Kernel modules: intel_pch_thermal
    00:15.0 Signal processing controller [1180]: Intel Corporation Sunrise Point-LP Serial IO I2C Controller #0 [8086:9d60] (rev 21)
        Subsystem: Dell Sunrise Point-LP Serial IO I2C Controller [1028:0704]
        Kernel driver in use: intel-lpss
        Kernel modules: intel_lpss_pci
    00:15.1 Signal processing controller [1180]: Intel Corporation Sunrise Point-LP Serial IO I2C Controller #1 [8086:9d61] (rev 21)
        Subsystem: Dell Sunrise Point-LP Serial IO I2C Controller [1028:0704]
        Kernel driver in use: intel-lpss
        Kernel modules: intel_lpss_pci
    00:16.0 Communication controller [0780]: Intel Corporation Sunrise Point-LP CSME HECI #1 [8086:9d3a] (rev 21)
        Subsystem: Dell Sunrise Point-LP CSME HECI [1028:0704]
        Kernel driver in use: mei_me
    00:16.3 Serial controller [0700]: Intel Corporation Device [8086:9d3d] (rev 21)
        Subsystem: Dell Device [1028:0704]
        Kernel driver in use: serial
    00:17.0 SATA controller [0106]: Intel Corporation Sunrise Point-LP SATA Controller [AHCI mode] [8086:9d03] (rev 21)
        Subsystem: Dell Sunrise Point-LP SATA Controller [AHCI mode] [1028:0704]
        Kernel driver in use: ahci
    00:1c.0 PCI bridge [0604]: Intel Corporation Sunrise Point-LP PCI Express Root Port #1 [8086:9d10] (rev f1)
        Kernel driver in use: pcieport
    00:1c.4 PCI bridge [0604]: Intel Corporation Sunrise Point-LP PCI Express Root Port #5 [8086:9d14] (rev f1)
        Kernel driver in use: pcieport
    00:1c.5 PCI bridge [0604]: Intel Corporation Sunrise Point-LP PCI Express Root Port #6 [8086:9d15] (rev f1)
        Kernel driver in use: pcieport
    00:1d.0 PCI bridge [0604]: Intel Corporation Sunrise Point-LP PCI Express Root Port #9 [8086:9d18] (rev f1)
        Kernel driver in use: pcieport
    00:1f.0 ISA bridge [0601]: Intel Corporation Sunrise Point-LP LPC Controller [8086:9d48] (rev 21)
        Subsystem: Dell Sunrise Point-LP LPC Controller [1028:0704]
    00:1f.2 Memory controller [0580]: Intel Corporation Sunrise Point-LP PMC [8086:9d21] (rev 21)
        Subsystem: Dell Sunrise Point-LP PMC [1028:0704]
        Kernel driver in use: intel_pmc_core
    00:1f.3 Audio device [0403]: Intel Corporation Sunrise Point-LP HD Audio [8086:9d70] (rev 21)
        Subsystem: Dell Sunrise Point-LP HD Audio [1028:0704]
        Kernel driver in use: snd_hda_intel
    00:1f.4 SMBus [0c05]: Intel Corporation Sunrise Point-LP SMBus [8086:9d23] (rev 21)
        Subsystem: Dell Sunrise Point-LP SMBus [1028:0704]
        Kernel driver in use: i801_smbus
    3a:00.0 Network controller [0280]: Intel Corporation Wireless 8260 [8086:24f3] (rev 3a)
        Subsystem: Intel Corporation Wireless 8260 [8086:0050]
        Kernel driver in use: iwlwifi
        Kernel modules: iwlwifi
    3b:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS525A PCI Express Card Reader [10ec:525a] (rev 01)
        Subsystem: Dell RTS525A PCI Express Card Reader [1028:0704]
        Kernel driver in use: rtsx_pci
        Kernel modules: rtsx_pci
    3c:00.0 Non-Volatile memory controller [0108]: Toshiba America Info Systems Device [1179:0115] (rev 01)
        Subsystem: Toshiba America Info Systems Device [1179:0001]
        Kernel driver in use: nvme

# [Remaining boot issues]

Here are the remaining issues with my current build: Profile: Gentoo systemd 17.0 boot: uefi disk: LVM 9350 ver: P54G BIOS: 1.7.0

`root `[`#`]`dmesg`

    (NULL device *): hwmon_device_register() is deprecated. Please convert the driver to use hwmon_device_register_with_info().
    usb: port power management may be unreliable
    ...
    i8042: Warning: Keylock active
    ...
    NOHZ: local_softirq_pending 282 <---Lots of these with different numbers
    ...
    snd_hda_codec_realtek hdaudioC0D0: Failed to find dell wmi symbol dell_micmute_led_set
    ...
    systemd[1]: File /lib/systemd/system/systemd-journald.service:35 configures an IP firewall (IPAddressDeny=any), but the local system does not support BPF/cgroup based firewalling.
    systemd[1]: Proceeding WITHOUT firewalling in effect! (This warning is only shown for the first loaded unit using IP firewalling.)
    ...
    ACPI Warning: \_SB.IETM._ART: Return Package type mismatch at index 0 - found Integer, expected Reference (20170728/nspredef-297)
    ACPI: Invalid package element [0]: got number, expecting [R]
    _ART package 0 is invalid, ignored
    ...
    wmi_bus wmi_bus-PNP0C14:01: WQBC data block query control method not found
    ...
    thermal thermal_zone11: failed to read out thermal zone (-61)