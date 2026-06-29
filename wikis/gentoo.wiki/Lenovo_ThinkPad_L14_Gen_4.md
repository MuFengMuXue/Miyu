**Resources**

[[]][Home](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-l-series-laptops/thinkpad-l14-gen-4-type-21h5-21h6)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_L14_Gen_4_AMD/ThinkPad_L14_Gen_4_AMD_Spec.pdf)

[[]][Specifications (by region)](https://psref.lenovo.com/product/thinkpad_l14_gen_4_amd?tab=model)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/pccbbs/mobiles_pdf/l14_l15_gen4_hmm_en.pdf)

[[]][User Guide](https://download.lenovo.com/pccbbs/mobiles_pdf/l14_l15_gen4_linux_ug.pdf)

[[]][BIOS Setup](https://download.lenovo.com/pccbbs/mobiles_pdf/lenovo_bios_setup_linux_wmi_sysfs_1.2.pdf)

The **Lenovo ThinkPad L14 (Gen 4)** is a 14-inch laptop manufactured by Lenovo for business needs. As such, it is thicker than many modern laptops and has plenty of ports. The laptop is also quite easy to maintain and has the option of installing an LTE modem.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [Accessories]](#Accessories)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Firmware]](#Firmware)
    -   [[2.2] [Kernel]](#Kernel)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Disable Secure Boot]](#Disable_Secure_Boot)
    -   [[3.2] [LTE modem]](#LTE_modem)
        -   [[3.2.1] [Queltec]](#Queltec)
        -   [[3.2.2] [Fibocom]](#Fibocom)

## [Hardware]

### [Standard]

  ------------------- ------------------------------------------------------------------------- -------- ------------------------ ------------------ ---------------- -------
  Device              Make/model                                                                Status   Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  CPU                 AMD Ryzen 5 PRO 7530U with Radeon Graphics                                Works    N/A                      N/A                6.4.11
  Wi-Fi               MEDIATEK Corp. MT7922 802.11ax PCI Express Wireless Network Adapter       Works    N/A                      mt7921e            6.4.11
  Ethernet            Realtek Semiconductor Co., Ltd. RTL8111/8168/8411                         Works    N/A                      r8169              6.4.11
  Bluetooth           Foxconn / Hon Hai Wireless_Device                                         Works    0489:e0d8                btusb              6.4.11
  Audio               Advanced Micro Devices, Inc. \[AMD\] Family 17h/19h HD Audio Controller   Works    N/A                      snd_hda_intel      6.4.11
  GPU                 Advanced Micro Devices, Inc. \[AMD/ATI\] Barcelo (rev d5)                 Works    N/A                      amdgpu             6.4.11
  MMC card reader     O2 Micro, Inc. SD/MMC Card Reader Controller (rev 01)                     Works    N/A                      N/A                6.4.11
  Smart card reader   EMV Smartcard Reader                                                      Works    N/A                      usbfs              6.4.11
  Finger Print        Cypress Semiconductor                                                     Works    N/A                      usbhid             6.4.11
  RGB Camera          Integrated RGB Camera                                                     Works    N/A                      uvcvideo           6.4.11
  Touchpad            ELAN067F:00                                                               Works    N/A                      i2c_designware     6.4.11
  Trackpad            TPPS/2 Elan TrackPoint                                                    Works    N/A                      mousedev           6.4.11
  ------------------- ------------------------------------------------------------------------- -------- ------------------------ ------------------ ---------------- -------

### [Accessories]

** Note**\
Be aware of the WWAN BIOS whitelisting in all new ThinkPad models.

  ----------- -------------------------------------------------------------------------------- -------- ------------------------ ------------------ ---------------- ------- --
  Device      Make/model                                                                       Status   Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  LTE modem   Quectel Wireless Solutions Co., Ltd. EM05-G                                      Works    2c7c:030a                cdc_mbim           6.6.13
  LTE modem   Fibocom L860-GL-16 (Intel Corporation XMM7560 LTE Advanced Pro Modem (rev 01))   Works    8086:7560                iosm               6.6.21
  ----------- -------------------------------------------------------------------------------- -------- ------------------------ ------------------ ---------------- ------- --

`root `[`#`]`lspci -nn`

    00:00.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne Root Complex [1022:1630]
    00:00.2 IOMMU [0806]: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne IOMMU [1022:1631]
    00:01.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Renoir PCIe Dummy Host Bridge [1022:1632]
    00:02.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Renoir PCIe Dummy Host Bridge [1022:1632]
    00:02.1 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne PCIe GPP Bridge [1022:1634]
    00:02.3 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne PCIe GPP Bridge [1022:1634]
    00:02.4 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne PCIe GPP Bridge [1022:1634]
    00:02.6 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne PCIe GPP Bridge [1022:1634]
    00:08.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Renoir PCIe Dummy Host Bridge [1022:1632]
    00:08.1 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Renoir Internal PCIe GPP Bridge to Bus [1022:1635]
    00:14.0 SMBus [0c05]: Advanced Micro Devices, Inc. [AMD] FCH SMBus Controller [1022:790b] (rev 51)
    00:14.3 ISA bridge [0601]: Advanced Micro Devices, Inc. [AMD] FCH LPC Bridge [1022:790e] (rev 51)
    00:18.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 0 [1022:166a]
    00:18.1 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 1 [1022:166b]
    00:18.2 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 2 [1022:166c]
    00:18.3 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 3 [1022:166d]
    00:18.4 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 4 [1022:166e]
    00:18.5 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 5 [1022:166f]
    00:18.6 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 6 [1022:1670]
    00:18.7 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 7 [1022:1671]
    01:00.0 Non-Volatile memory controller [0108]: Transcend Information, Inc. Device [1d79:2263] (rev 03)
    03:00.0 Ethernet controller [0200]: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller [10ec:8168] (rev 0e)
    04:00.0 SD Host controller [0805]: O2 Micro, Inc. SD/MMC Card Reader Controller [1217:8621] (rev 01)
    06:00.0 Network controller [0280]: MEDIATEK Corp. MT7922 802.11ax PCI Express Wireless Network Adapter [14c3:0616]
    07:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Barcelo [1002:15e7] (rev d5)
    07:00.1 Audio device [0403]: Advanced Micro Devices, Inc. [AMD/ATI] Renoir Radeon High Definition Audio Controller [1002:1637]
    07:00.2 Encryption controller [1080]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 10h-1fh) Platform Security Processor [1022:15df]
    07:00.3 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne USB 3.1 [1022:1639]
    07:00.4 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne USB 3.1 [1022:1639]
    07:00.5 Multimedia controller [0480]: Advanced Micro Devices, Inc. [AMD] ACP/ACP3X/ACP6x Audio Coprocessor [1022:15e2] (rev 01)
    07:00.6 Audio device [0403]: Advanced Micro Devices, Inc. [AMD] Family 17h/19h HD Audio Controller [1022:15e3]

`root `[`#`]`lsusb`

    Bus 004 Device 004: ID 17ef:1020 Lenovo ThinkPad Dock Hub
    Bus 004 Device 003: ID 17ef:3062 Lenovo ThinkPad Dock Ethernet [Realtek RTL8153B]
    Bus 004 Device 002: ID 17ef:101f Lenovo
    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 003 Device 011: ID 30c9:0050 Luxvisions Innotech Limited Integrated RGB Camera
    Bus 003 Device 009: ID 058f:9540 Alcor Micro Corp. AU9540 Smartcard Reader
    Bus 003 Device 005: ID 05e3:0610 Genesys Logic, Inc. Hub
    Bus 003 Device 003: ID 046d:c52b Logitech, Inc. Unifying Receiver
    Bus 003 Device 008: ID 1235:8200 Focusrite-Novation Scarlett 2i4 USB
    Bus 003 Device 012: ID 17ef:3063 Lenovo ThinkPad Dock Audio
    Bus 003 Device 010: ID 04d9:0125 Holtek Semiconductor, Inc. USB Keyboard
    Bus 003 Device 007: ID 17ef:1021 Lenovo ThinkPad Dock Hub [Cypress HX2VL]
    Bus 003 Device 006: ID 17ef:1026 Lenovo
    Bus 003 Device 004: ID 17ef:3060 Lenovo ThinkPad Dock
    Bus 003 Device 002: ID 17ef:1025 Lenovo
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 003: ID 06cb:00f9 Synaptics, Inc.
    Bus 001 Device 002: ID 0489:e0d8 Foxconn / Hon Hai Wireless_Device
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

`root `[`#`]`i2cdetect -l`

    i2c-0   i2c             Synopsys DesignWare I2C adapter         I2C adapter
    i2c-1   i2c             Synopsys DesignWare I2C adapter         I2C adapter
    i2c-2   i2c             AMDGPU DM i2c hw bus 0                  I2C adapter
    i2c-3   i2c             AMDGPU DM i2c hw bus 1                  I2C adapter
    i2c-4   i2c             AMDGPU DM i2c hw bus 2                  I2C adapter
    i2c-5   i2c             AMDGPU DM i2c hw bus 3                  I2C adapter
    i2c-6   i2c             AMDGPU DM aux hw bus 0                  I2C adapter
    i2c-7   i2c             AMDGPU DM aux hw bus 2                  I2C adapter
    i2c-8   i2c             AMDGPU DM aux hw bus 3                  I2C adapter
    i2c-9   i2c             DPMST                                   I2C adapter
    i2c-10  i2c             DPMST                                   I2C adapter

`root `[`#`]`lsmod`

    Module                  Size  Used by
    dm_crypt               49152  1
    onboard_usb_hub        20480  0
    xhci_pci               24576  0
    xhci_pci_renesas       12288  1 xhci_pci
    sp5100_tco             12288  0
    mt7921e                32768  0
    watchdog               40960  1 sp5100_tco
    ucsi_acpi              12288  0
    k10temp                12288  0
    xhci_hcd              290816  1 xhci_pci
    typec_ucsi             49152  1 ucsi_acpi
    typec                  98304  1 typec_ucsi
    roles                  16384  1 typec_ucsi
    dm_mod                167936  3 dm_crypt
    dax                    49152  1 dm_mod

`root `[`#`]`sensors`

    thinkpad-isa-0000
    Adapter: ISA adapter
    fan1:        1765 RPM
    CPU:          +42.0°C
    GPU:              N/A
    temp3:        +42.0°C
    temp4:         +0.0°C
    temp5:        +42.0°C
    temp6:        +42.0°C
    temp7:        +42.0°C
    temp8:       -108.0°C

    BAT0-acpi-0
    Adapter: ACPI interface
    in0:          13.00 V

    k10temp-pci-00c3
    Adapter: PCI adapter
    Tctl:         +43.4°C

    amdgpu-pci-0700
    Adapter: PCI adapter
    vddgfx:        1.45 V
    vddnb:       799.00 mV
    edge:         +40.0°C
    PPT:          10.00 W

    acpitz-acpi-0
    Adapter: ACPI interface
    temp1:        +42.0°C  (crit = +128.0°C)

## [Installation]

** Note**\
If there are plans to use [EFI stub](https://wiki.gentoo.org/wiki/EFI_stub "EFI stub"), disable Secure Boot as explained [here](#Disable_Secure_Boot).

### [Firmware]

External firmware is required for the Wi-Fi module and AMD GPU:

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

### [Kernel]

** Tip**\
A third-party provided [configuration file](//ow1.in/Lenovo_L14_Gen4_6.4.11.config.gz) (kernel version 6.4.11) can be used as a template.

[KERNEL] **All required external firmware (kernel version 6.4.11)**

    Device Drivers  --->
      Generic Driver Options  --->
        Firmware loader  --->
    -*-   Firmware loading facility
            amdgpu/green_sardine_asd.bin amdgpu/green_sardine_ta.bin amdgpu/green_sardine_dmcub.bin amdgpu/green_sardine_pfp.bin amdgpu/green_sardine_me.bin amdgpu/green_sardine_ce.bin amdgpu/green_sardine_rlc.bin amdgpu/green_sardine_mec.bin amdgpu/green_sardine_sdma.bin amdgpu/green_sardine_vcn.bin mediatek/BT_RAM_CODE_MT7922_1_1_hdr.bin mediatek/WIFI_RAM_CODE_MT7922_1.bin mediatek/WIFI_MT7922_patch_mcu_1_1_hdr.bin regulatory.db regulatory.db.p7s

[KERNEL] **Wi-Fi (MEDIATEK Corp. MT7922 802.11ax)**

    Device Drivers  --->
    [*] Network Device support --->
    [*]   Wireless Lan --->
    [*]     MediaTek devices
    <*>       MediaTek MT7921E (PCIe) support

[KERNEL] **Bluetooth (MediaTek Inc. Wireless Device 0489:e0d8)**

    Networking Support  --->
    <*> Bluetooth subsystem support  --->
          Bluetooth device drivers  --->
    <*>     HCI USB driver
    [*]       MediaTek protocol support

[KERNEL] **Touchpad/Trackpad (ELAN067F:00)**

    Device Drivers  --->
    [*] Input device support --->
    [*]   Mice --->
    <*>     PS/2 mouse
    [*]       Elantech PS/2 protocol extension
    < >     ELAN I2C Touchpad support
    [ ]   Touchscreens  ---
    [*]   HID bus support
    <*>     I2C HID support
    < >       Driver for Elan hid-i2c based devices on OF systems
    -*- Pin controllers
    [*]   AMD GPIO pin control
        I2C suppoer
          I2C Hardware Bus support  --->
    [*]     Synopsys DesignWare Slave
    <*>     Synopsys DesignWare Platform

## [Configuration]

### [Disable Secure Boot]

To disable Secure Boot, the following steps must be performed:

-   Enable UEFI-only loading (no legacy support)
-   Set an administrator password
-   Disable secure boot

### [LTE modem]

The modem is [FCC locked](https://modemmanager.org/docs/modemmanager/fcc-unlock/).

#### [Queltec]

A script to enable the radio is installed by [[[net-misc/modemmanager]](https://packages.gentoo.org/packages/net-misc/modemmanager)[]], but a link to it must be manually created:

`root `[`#`]`mkdir -p /etc/ModemManager/fcc-unlock.d`

`root `[`#`]`ln -s ../../../usr/share/ModemManager/fcc-unlock.available.d/2c7c:030a /etc/ModemManager/fcc-unlock.d/`

#### [Fibocom]

Some useful information can be obtained at the [Fibocom L860-GL-16](https://wiki.gentoo.org/wiki/Fibocom_L860-GL-16 "Fibocom L860-GL-16") page.