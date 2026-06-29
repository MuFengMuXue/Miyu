**Resources**

[[]][Official Support Page](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-twist-series-laptops/thinkpad-twist-s230u)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/withdrawnbook/ThinkPad_Twist_S230u.pdf)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/ibmdl/pub/pc/pccbbs/mobiles_pdf/s230u_hmm_en_0b48943_02.pdf)

[[]][User Guide](https://download.lenovo.com/ibmdl/pub/pc/pccbbs/mobiles_pdf/s230u_twist_ug_en.pdf)

[[]][BIOS Setup](https://download.lenovo.com/pccbbs/mobiles_pdf/lenovo_bios_setup_linux_wmi_sysfs_1.2.pdf)

[[]][ThinkPad Twist](https://en.wikipedia.org/wiki/ThinkPad_Twist "wikipedia:ThinkPad Twist")

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Firmware]](#Firmware)
    -   [[2.2] [Kernel]](#Kernel)
    -   [[2.3] [Emerge]](#Emerge)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Keyboard/Trackpoint/Touchpad does not work]](#Keyboard.2FTrackpoint.2FTouchpad_does_not_work)

## [Hardware]

### [Standard]

  ------------- -------------------------------------------- -------- ------------------------ ------------------ ---------------- -------
  Device        Make/model                                   Status   Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  Keyboard      N/A                                          Works    N/A                      N/A                4.2
  Wi-Fi         Intel Corporation Centrino Wireless-N 2230   Works    N/A                      iwlwifi            4.2
  Sound         N/A                                          Works    N/A                      N/A                4.2
  Webcam        N/A                                          Works    N/A                      N/A                4.2
  Card Reader   RTS5229 PCI Express Card Reader              Works    N/A                      N/A                4.2
  ------------- -------------------------------------------- -------- ------------------------ ------------------ ---------------- -------

## [Installation]

Using a standard [stage3](https://gentoo.org/downloads/) installation everything should pretty much work out of the box.

### [Firmware]

The wireless card requires external firmware (**iwlwifi-2030-6.ucode**):

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

### [Kernel]

[KERNEL] **External firmware (optional, can be loaded as a module)**

    Device Drivers  --->
      Generic Driver Options  --->
        -*- Userspace firmware loading support
        [*]   Include in-kernel firmware blobs in kernel binary
        (iwlwifi-2030-6.ucode) External firmware blobs to build into the kernel binary
        (/lib/firmware) Firmware blobs root directory
        [ ] Fallback user-helper invocation for firmware

[KERNEL] **Wi-Fi**

    Device Drivers  --->
      [*] Network device support  --->
        [*]   Wireless LAN  --->
          [ ]   ADMtek devices
          [ ]   Atheros/Qualcomm devices
          [ ]   Atmel devices
          [ ]   Broadcom devices
          [ ]   Cisco devices
          [*]   Intel devices
          < >     Intel PRO/Wireless 2100 Network Connection
          < >     Intel PRO/Wireless 2200BG and 2915ABG Network Connection
          < >     Intel Wireless WiFi 4965AGN (iwl4965)
          < >     Intel PRO/Wireless 3945ABG/BG Network Connection (iwl3945)
          <M/*>   Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)
          <M/*>   Intel Wireless WiFi DVM Firmware support
          < >     Intel Wireless WiFi MVM Firmware support

[KERNEL] **Sound**

    Device Drivers  --->
          <*> Sound card support  --->
              <*>   Advanced Linux Sound Architecture  --->
                  [*]   USB sound devices  --->
                      <M>   USB Audio/MIDI driver

[KERNEL] **Webcam**

    Device Drivers --->
        <M> Multimedia support --->
          [*] Media USB Adapters --->
            [M] USB Video Class (UVC)

[KERNEL] **Card Reader**

    Device Drivers --->
        Misc devices--->
          < > Realtek PCI-E card reader

### [Emerge]

** Note**\
It was mentioned in the discussions that the driver package may not be necessary if both \"Realtek PCI-E card reader\" (CONFIG_MISC_RTSX_PCI) and \"Realtek PCI-E SD/MMC Card Interface Driver\" (CONFIG_MMC_REALTEK_PCI) are enabled in the kernel.

Driver for card reader:

`root `[`#`]`emerge --ask sys-block/rts5229`

## [Troubleshooting]

### [][Keyboard/Trackpoint/Touchpad does not work]

For some reason on kernels \>= 4.2 the keyboard, trackpoint and touchpad do not work on the first boot. To work around this problem, add **i8042.nomux=1 i8042.reset** to your kernel parameters:

[FILE] **`/etc/default.grub`add to kernel command line**

    GRUB_CMDLINE_LINUX_DEFAULT="i8042.nomux=1 i8042.reset"