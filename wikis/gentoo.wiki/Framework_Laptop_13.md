**Resources**

[[]][Product Information](https://frame.work)

[[]][Specifications](https://frame.work/products/laptop-diy-13-gen-intel)

[[]][Framework Computer](https://en.wikipedia.org/wiki/https://en.wikipedia.org/wiki/Framework_Computer "wikipedia:https://en.wikipedia.org/wiki/Framework Computer")

[[]][Expansion Cards](https://wiki.gentoo.org/wiki/Framework_Expansion_Cards#.2FGuide "Framework Expansion Cards")

The Framework Laptop 13, released in 2021, is a highly modular and repairable 13 inch laptop. The DIY edition in particular comes without an OS and the developers and community are currently focused on supporting Arch Linux as an alternative to Windows.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Intel Tiger Lake (11th-gen)]](#Intel_Tiger_Lake_.2811th-gen.29)
    -   [[1.2] [Intel Alder Lake (12th-gen)]](#Intel_Alder_Lake_.2812th-gen.29)
    -   [[1.3] [Intel Raptor Lake (13th-gen)]](#Intel_Raptor_Lake_.2813th-gen.29)
    -   [[1.4] [AMD 7040 Series]](#AMD_7040_Series)
    -   [[1.5] [Expansion cards]](#Expansion_cards)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Firmware]](#Firmware)
    -   [[2.2] [Kernel]](#Kernel)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [BIOS updates]](#BIOS_updates)
    -   [[3.2] [Motherboard and/or CPU upgrades]](#Motherboard_and.2For_CPU_upgrades)
    -   [[3.3] [No Lid Switch and Power Button ACPI events]](#No_Lid_Switch_and_Power_Button_ACPI_events)
    -   [[3.4] [Touchpad not working]](#Touchpad_not_working)
        -   [[3.4.1] [Without \"HID over I2C transport layer ACPI\"]](#Without_.22HID_over_I2C_transport_layer_ACPI.22)
        -   [[3.4.2] [With \"HID over I2C transport layer ACPI\"]](#With_.22HID_over_I2C_transport_layer_ACPI.22)
    -   [[3.5] [Built-in Keyboard not working on boot to unlock encrypted device]](#Built-in_Keyboard_not_working_on_boot_to_unlock_encrypted_device)
    -   [[3.6] [EFI Stub Kernel Boot Failed]](#EFI_Stub_Kernel_Boot_Failed)
    -   [[3.7] [Fingerprint reader]](#Fingerprint_reader)
    -   [[3.8] [Brightness Keys Not Working]](#Brightness_Keys_Not_Working)
    -   [[3.9] [Freezing with 6.4 series kernels]](#Freezing_with_6.4_series_kernels)
-   [[4] [See also]](#See_also)
-   [[5] [References]](#References)

## [Hardware]

### [][Intel Tiger Lake (11th-gen)]

+-----------------------+---------------------------------+---------+------------------------+--------------------------------------+--------------------+-------------------------------------------------------------------------------------------------------+
| Device                | Make/model                      | Status  | Vendor ID / Product ID | Kernel driver(s)                     | Kernel version     | Notes                                                                                                 |
+-----------------------+---------------------------------+---------+------------------------+--------------------------------------+--------------------+-------------------------------------------------------------------------------------------------------+
| Chipset               | Intel Tiger Lake                | Works   | \[multiple\]           | i801_smbus                           | 5.14.15            |                                                                                                       |
|                       |                                 |         |                        |                                      |                    |                                                                                                       |
|                       |                                 |         |                        | intel_ish_ipc                        |                    |                                                                                                       |
|                       |                                 |         |                        |                                      |                    |                                                                                                       |
|                       |                                 |         |                        | intel_lpss_pci                       |                    |                                                                                                       |
|                       |                                 |         |                        |                                      |                    |                                                                                                       |
|                       |                                 |         |                        | intel_pmt                            |                    |                                                                                                       |
+-----------------------+---------------------------------+---------+------------------------+--------------------------------------+--------------------+-------------------------------------------------------------------------------------------------------+
| Video card            | Intel Tiger Lake-LP GT2         | Works   | f111:0001              | i915                                 | 5.14.15            | i915 and intel VIDEO_CARDS flags                                                                      |
+-----------------------+---------------------------------+---------+------------------------+--------------------------------------+--------------------+-------------------------------------------------------------------------------------------------------+
| Sound card            | Intel Tiger Lake-LP Smart Sound | Works   | 8086:a0c8:f111:0001    | snd_hda_intel, snd_soc_sof_tigerlake | 5.14.15            | Also requires either Realtek or IDT HD codec, depending on date of manufacture^[\[1\]](#cite_note-1)^ |
+-----------------------+---------------------------------+---------+------------------------+--------------------------------------+--------------------+-------------------------------------------------------------------------------------------------------+
| Wireless network card | Intel AX210                     | Works   | 8086:2725:8086:0024    | iwlwifi                              | 5.14.15            | Needs firmware from sys-kernel/linux-firmware                                                         |
+-----------------------+---------------------------------+---------+------------------------+--------------------------------------+--------------------+-------------------------------------------------------------------------------------------------------+
| Bluetooth             | Intel AX210                     | Works   |                        | bluetooth                            | 5.14.15            |                                                                                                       |
+-----------------------+---------------------------------+---------+------------------------+--------------------------------------+--------------------+-------------------------------------------------------------------------------------------------------+
| Touchpad              | PixArt PIXA3854                 | Works   | 093A:0274              | hid_multitouch                       | 5.14.15            | Also depends on i2c_designware_core, intel_ishtp_hid                                                  |
+-----------------------+---------------------------------+---------+------------------------+--------------------------------------+--------------------+-------------------------------------------------------------------------------------------------------+
| Fingerprint Reader    | Goodix USB2.0 MISC              | Works   | 27c6:609c              |                                      |                    | Requires sys-auth/fprintd-1.94.0                                                                      |
+-----------------------+---------------------------------+---------+------------------------+--------------------------------------+--------------------+-------------------------------------------------------------------------------------------------------+
| Webcam                | Realtek Laptop Camera           | Works   | 0bda:5634              | uvc                                  | 5.15.8 (as tested) |                                                                                                       |
+-----------------------+---------------------------------+---------+------------------------+--------------------------------------+--------------------+-------------------------------------------------------------------------------------------------------+

### [][Intel Alder Lake (12th-gen)]

  ----------------------- --------------------------------- -------- ------------------------ ------------------ ---------------- --------------------------------------------------------
  Device                  Make/model                        Status   Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  Chipset                 Intel Alder Lake                  Works
  Video card              Intel Alder Lake-LP GT2           Works
  Sound card              Intel Alder Lake-LP Smart Sound   Works
  Wireless network card   Intel AX210                       Works
  Bluetooth               Intel AX210                       Works
  Touchpad                PixArt PIXA3854                   Works                                                                 Depends on pinctrl_tigerlake and not pinctrl_alderlake
  Fingerprint Reader      Goodix USB2.0 MISC                Works
  Webcam                  Realtek Laptop Camera             Works
  Ambient light sensor                                      Works
  ----------------------- --------------------------------- -------- ------------------------ ------------------ ---------------- --------------------------------------------------------

\

### [][Intel Raptor Lake (13th-gen)]

  ----------------------- --------------------------------- -------- ------------------------ ------------------ ---------------- --------------------------------------------------------
  Device                  Make/model                        Status   Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  Chipset                 Intel Alder Lake                  Works
  Video card              Intel Alder Lake-LP GT2           Works
  Sound card              Intel Alder Lake-LP Smart Sound   Works
  Wireless network card   Intel AX210                       Works
  Bluetooth               Intel AX210                       Works
  Touchpad                PixArt PIXA3854                   Works                                                                 Depends on pinctrl_tigerlake and not pinctrl_alderlake
  ----------------------- --------------------------------- -------- ------------------------ ------------------ ---------------- --------------------------------------------------------

### [AMD 7040 Series]

  -------------------------------------------------- --------------------------- ---------- ------------------------ ----------------------------------------------------------------- ---------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Device                                             Make/model                  Status     Vendor ID / Product ID   Kernel driver(s)                                                  Kernel version   Notes
  Chipset                                            AMD Pink Sardine            Works
  Video card                                         AMD Radeon 780M             Works                               amdgpu
  Sound card                                         Ryzen HD Audio Controller   Works                               snd_hda_intel snd_hda_codec_generic
  Sound card via external Displayport USB-C screen   Ryzen HD Audio Controller   Works                               snd_hda_codec_hdmi snd_hda_codec_generic snd_hda_codec_atihdmi
  Wireless network card                              MediaTek MT7922             Works                               mt7921e
  Bluetooth                                          MediaTek MT7922             Works                               bluetooth btmtk btusb (You must enable CONFIG_BT_HCIBTUSB_MTK)
  Touchpad                                           PixArt PIXA3854             Works                               hid_multitouch i2c_designware_platform i2c_hid_acpi pinctrl_amd
  Fingerprint Reader                                 Goodix USB2.0 MISC          Works\*    27c6:609c                                                                                                   \*Requires firmware update: see [\[1\]](https://knowledgebase.frame.work/en_us/updating-fingerprint-reader-firmware-on-linux-for-13th-gen-and-amd-ryzen-7040-series-laptops-HJrvxv_za)
  Webcam                                             Generic Laptop Camera (?)   Works                               uvcvideo
  Ambient light sensor
  -------------------------------------------------- --------------------------- ---------- ------------------------ ----------------------------------------------------------------- ---------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Backlight:

The backlight brightness keys (on the 7840U at least) show up as ACPI events rather than keyboard keys, and require the CONFIG_I2C_DESIGNWARE_PLATFORM kernel option to be set to work. The backlight itself can still be adjusted without that config option, via the usual echoing to the appropriate brightness file: /sys/class/backlight/amdgpu_bl0/brightness

The backlight keys will also need [[[sys-power/acpilight]](https://packages.gentoo.org/packages/sys-power/acpilight)[]] installed, replacing [[[x11-apps/xbacklight]](https://packages.gentoo.org/packages/x11-apps/xbacklight)[]] if it was previously installed.

### [Expansion cards]

**See [Framework Expansion Cards](https://wiki.gentoo.org/wiki/Framework_Expansion_Cards "Framework Expansion Cards").** The Framework Laptop 13 features four modular expansion card slots allowing for custom port configurations.

## [Installation]

Because of some boot menu and device selection issues, it may be necessary to update to BIOS version 3.06 before installing. See: [https://community.frame.work/t/public-beta-test-bios-v3-06-driver-bundle-2021-10-29/10167](https://community.frame.work/t/public-beta-test-bios-v3-06-driver-bundle-2021-10-29/10167) This update is also necessary to support the Tempo audio codec in the post-Oct 2021 Framework laptops.

The Framework Laptop 13 supports [fwupd](https://wiki.gentoo.org/wiki/Fwupd "Fwupd") to update the BIOS.

### [Firmware]

Firmware from [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] is needed for the GPU, wireless, and bluetooth interfaces. The TigerLake GPU firmware in particular needs to be loaded immediately at boot, so it must be included as a kernel blob or on an init ramdisk. See: [Intel#Firmware](https://wiki.gentoo.org/wiki/Intel#Firmware "Intel")

### [Kernel]

There have been significant stability issues with Wifi and Bluetooth in kernels prior to 5.14.15, so we\'re starting there.

[KERNEL] **Intel Power Management**

    Processor type and features  --->
      [*] Intel Low Power Subsystem support Search for <code>CONFIG_X86_INTEL_LPSS</code> to find this item.
    Power management and ACPI options  --->
      [*] ACPI (Advanced Configuration and Power Interface) Support  ---> Search for <code>CONFIG_ACPI</code> to find this item.
      ~~ Your choice of AC, Battery, Fan, Thermal, etc ~~
         [*] Intel DPTF (Dynamic Platform and Thermal Framework) Support Search for <code>CONFIG_ACPI_DPTF</code> to find this item.
      [*] Cpuidle Driver for Intel Processors Search for <code>CONFIG_CONFIG_INTEL_IDLE</code> to find this item.
    Firmware Drivers  --->
      [*] Load custom ACPI SSDT overlay from an EFI variable Search for <code>CONFIG_EFI_CUSTOM_SSDT_OVERLAYS</code> to find this item.
    Device Drivers   --->
      <*> Thermal Drivers  ---> Search for <code>CONFIG_CONFIG_THERMAL</code> to find this item.
         Intel thermal drivers  --->
            <*> X86 package temperature thermal driver Search for <code>CONFIG_X86_PKG_TEMP_THERMAL</code> to find this item.
            <*> Intel SoCs DTS thermal driver Search for <code>CONFIG_INTEL_SOC_DTS_THERMAL</code> to find this item.
            ACPI INT340X thermal drivers  --->
               <*> ACPI INT340X thermal driver Search for <code>CONFIG_INT340X_THERMAL</code> to find this item.
            <*> Intel TCC offset cooling Driver Search for <code>CONFIG_INTEL_TCC_COOLING</code> to find this item.
      Multifunction device drivers  --->
         <*> Intel Low Power Subsystem support in PCI mode Search for <code>CONFIG_MFD_INTEL_LPSS_PCI</code> to find this item.
         <*> Intel PMC Driver for Broxton Search for <code>CONFIG_MFD_INTEL_PMC_BXT</code> to find this item.
         <*> Intel Platform Monitoring Technology (PMT) support Search for <code>CONFIG_INTEL_PMT_TELEMETRY</code> to find this item.
      [*] X86 Platform Specific Device Drivers Search for <code>CONFIG_X86_PLATFORM_DEVICES</code> to find this item.
         <*> Intel PMC Core driver Search for <code>CONFIG_INTEL_PMC_CORE</code> to find this item.

[KERNEL] **AMD Power Management**

    Processor type and features  --->
      [*] AMD ACPI2Platform devices support Search for <code>CONFIG_X86_AMD_PLATFORM_DEVICE</code> to find this item.
      [*] Supported processor vendors  --->
          [*]   Support AMD processors Search for <code>CONFIG_CPU_SUP_AMD</code> to find this item.
    Power management and ACPI options  --->
      [*] ACPI (Advanced Configuration and Power Interface) Support  ---> Search for <code>CONFIG_ACPI</code> to find this item.
          CPU Frequency scaling  --->
             [*]   AMD Processor P-State driver Search for <code>CONFIG_X86_AMD_PSTATE</code> to find this item.
             (3)     AMD Processor P-State default mode
    Firmware Drivers  --->
      [*] Load custom ACPI SSDT overlay from an EFI variable Search for <code>CONFIG_EFI_CUSTOM_SSDT_OVERLAYS</code> to find this item.
    Device Drivers   --->
       [*] }
            <*>   ChromeOS specific ACPI extensions
            <M>   Chrome OS Laptop
            <M>   Chrome OS pstore support
            <M>   ChromeOS Tablet Switch Controller
            <M>   ChromeOS Embedded Controller
            <M>   ChromeOS Embedded Controller (I2C)
            <M>   ChromeOS Embedded Controller (SPI)
            <M>   ChromeOS Embedded Controller (LPC)
            <M>   Backlight LED support for Chrome OS keyboards
            <M>   ChromeOS EC miscdevice
            <M>   Chromebook Pixel's lightbar support
            <M>   ChromeOS EC MEMS Sensor Hub
            <M>   ChromeOS EC control and information through sysfs
            <M>   ChromeOS EC Type-C Connector Control
            <M>   ChromeOS HPS device
            <M>   Logging driver for USB PD charger
            <M>   ChromeOS Type-C power delivery event notifier
            <M>   ChromeOS Privacy Screen support
            <M>   ChromeOS EC Type-C Switch Control
            <M>   ChromeOS Wilco Embedded Controller
       <*> Thermal Drivers  ---> Search for <code>CONFIG_CONFIG_THERMAL</code> to find this item.

[KERNEL] **I2C Bus (needed for Touchpad, Camera, and probably other stuff)**

    Device Drivers  --->
      <*> I2C Support  ---> Search for <code>CONFIG_I2C</code> to find this item.
         <*>   I2C device interface Search for <code>CONFIG_I2C_CHARDEV</code> to find this item.
         I2C Hardware Bus Support  --->
            <*> Intel 82801 (ICH/PCH) Search for <code>CONFIG_I2C_I801</code> to find this item.
            <*> Synopsys Designware Platform Search for <code>CONFIG_I2C_DESIGNWARE_PLATFORM</code> to find this item.

[KERNEL] **I2C Bus on AMD**

    Device Drivers  --->
      <*> Pin controllers  ---> Search for <code>CONFIG_PINCTRL</code> to find this item.
        <*> AMD GPIO pin control Search for <code>CONFIG_PINCTRL_AMD</code> to find this item.

[KERNEL] **Touchpad**

    Device Drivers  --->
      Input device support  --->
      HID support  --->
         <*> Generic HID driver Search for <code>CONFIG_HID_GENERIC</code> to find this item.
         Special HID driver  --->
            <*> HID Multitouch panels Search for <code>CONFIG_HID_MULTITOUCH</code> to find this item.
            <*> HID Sensors framework support Search for <code>CONFIG_HID_SENSOR_HUB</code> to find this item.
         <*> I2C HID support ---> Search for <code>CONFIG_I2C_HID</code> to find this item.
           <*> HID over I2C transport layer ACPI driver Search for <code>CONFIG_I2C_HID_ACPI</code> to find this item.
         Intel ISH HID support  --->
            <*> Intel Integrated Sensor Hub Search for <code>CONFIG_INTEL_ISH_HID</code> to find this item.

[KERNEL] **Intel Wireless LAN**

    [*] Networking support  ---> Search for <code>CONFIG_NET</code> to find this item.
      [*] Wireless  ---> Search for <code>CONFIG_WIRELESS</code> to find this item.
         <*> cfg80211 - wireless configuration API Search for <code>CONFIG_CFG80211</code> to find this item.
         <*> Generic IEEE 802.11 Networking Stack (mac80211) Search for <code>CONFIG_MAC80211</code> to find this item.

[KERNEL] **AMD Wireless LAN**

    [*] Networking support  ---> Search for <code>CONFIG_NET</code> to find this item.
      [*] Wireless  ---> Search for <code>CONFIG_WIRELESS</code> to find this item.
         <*> cfg80211 - wireless configuration API Search for <code>CONFIG_CFG80211</code> to find this item.
         <*> Generic IEEE 802.11 Networking Stack (mac80211) Search for <code>CONFIG_MAC80211</code> to find this item.
    Device Drivers  --->
      [*] Network device support  ---> Search for <code>CONFIG_NETDEVICES</code> to find this item.
         [*] Wireless LAN  ---> Search for <code>CONFIG_WLAN</code> to find this item.
            [*] MediaTek devices Search for <code>CONFIG_WLAN_VENDOR_MEDIATEK</code> to find this item.
            <*>   MediaTek MT7921E (PCIe) support  Search for <code>CONFIG_MT7921E</code> to find this item.

[KERNEL] **Intel Graphics card**

    Device Drivers  --->
     Graphics support  --->
      <*> /dev/agpgart (AGP Support)  ---> Search for <code>CONFIG_AGP</code> to find this item.
      <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support)  ---> Search for <code>CONFIG_DRM</code> to find this item.
      <*> Intel 8xx/9xx/G3x/G4x/HD Graphics Search for <code>CONFIG_DRM_I915</code> to find this item.

[KERNEL] **AMD Graphics card**

    Device Drivers  --->
     Graphics support  --->
      <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support)  ---> Search for <code>CONFIG_DRM</code> to find this item.
         <*> AMDGPU Search for <code>CONFIG_DRM_AMDGPU</code> to find this item.

Note: you have to include firmware blobs in the kernel if you don\'t compile amdgpu as a module. The required configuration string on 7040 is: *CONFIG_EXTRA_FIRMWARE=\"amdgpu/psp_13_0_4_toc.bin amdgpu/dcn_3_1_4_dmcub.bin amdgpu/gc_11_0_1_pfp.bin amdgpu/sdma_6_0_1.bin amdgpu/vcn_4_0_2.bin amdgpu/gc_11_0_1_imu.bin amdgpu/gc_11_0_1_mec.bin amdgpu/gc_11_0_1_mes.bin amdgpu/gc_11_0_1_mes_2.bin amdgpu/psp_13_0_4_ta.bin amdgpu/gc_11_0_1_me.bin amdgpu/gc_11_0_1_mes1.bin amdgpu/gc_11_0_1_rlc.bin\"*

[KERNEL] **Sound**

    Device Drivers  --->
      <*> Sound card support  ---> Search for <code>CONFIG_SOUND</code> to find this item.
         <*> Advanced Linux Sound Architecture  ---> Search for <code>CONFIG_SND</code> to find this item.
            HD Audio  --->
               <*> HD Audio PCI Search for <code>CONFIG_SND_HDA_INTEL</code> to find this item.
               <*> Build Realtek HD-audio codec support Search for <code>CONFIG_SND_HDA_CODEC_REALTEK</code> to find this item.
               <*> Build IDT/Sigmatel HD-audio codec support Search for <code>CONFIG_SND_HDA_CODEC_SIGMATEL</code> to find this item.
               <*> Build HDMI/DisplayPort HD-audio codec support Search for <code>CONFIG_SND_HDA_CODEC_HDMI</code> to find this item.
            <*> ALSA for SoC audio support  ---> Search for <code>CONFIG_SND_SOC</code> to find this item.
               [*] Sound Open Firmware Support Search for <code>CONFIG_SND_SOC_SOF_TOPLEVEL</code> to find this item.
               <*>   SOF PCI enumeration support Search for <code>CONFIG_SND_SOC_SOF_PCI</code> to find this item.
               [*]   SOF support for Intel audio DSPs Search for <code>CONFIG_SND_SOC_SOF_INTEL_TOPLEVEL</code> to find this item.
               <*>      SOF support for Tigerlake Search for <code>CONFIG_SND_SOC_SOF_TIGERLAKE</code> to find this item.

[KERNEL] **Storage (NVMe)**

    Device Drivers  --->
      NVME Support  --->
          <*> NVM Express block device Search for <code>CONFIG_BLK_DEV_NVME</code> to find this item.
               [*] NVMe multipath support Search for <code>CONFIG_NVME_MULTIPATH</code> to find this item.

[KERNEL] **Ambient light sensor**

    Device Drivers  --->
      <M> Industrial I/O support   --->  Search for <code>CONFIG_IIO</code> to find this item.
          Light sensors --->
               <M> HID ALS (CONFIG_HID_SENSOR_ALS) Search for <code>CONFIG_HID_SENSOR_ALS</code> to find this item.

The ambient light sensors values can be read using the command:

`root `[`#`]`cat /sys/bus/iio/devices/iio\:device0/in_illuminance_raw`

** Note**\
Post-October \'21 Frameworks use a Tempo (also known as IDT/Sigmatel) audio codec instead of Realtek

For more features on battery charge limit and LED configuration an out-of-tree kernel module can be installed via

`root `[`#`]`emerge --ask app-laptop/framework-laptop-kmod`

## [Troubleshooting]

### [BIOS updates]

Upgrading the Framework Laptop\'s BIOS will erase the EFI boot entries, leaving a Gentoo system unbootable afterwards. This can be fixed by booting from Gentoo install media, mounting and chrooting into the local install root and re-running grub-install.

Follow the *Mounting the necessary filesystems, Entering the new environment, and Mounting the boot partition* steps from the Handbook, substituting device names as necessary ([Handbook:AMD64/Parts/Installation/Base](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Mounting_the_necessary_filesystems "Handbook:AMD64/Installation/Base"))

Then recreate the necessary EFI entry

`root `[`#`]`grub-install --target=x86_64-efi --efi-directory=/boot`

### [][Motherboard and/or CPU upgrades]

Intel 12th Gen Alder Lake CPUs have a subset of the features of the 11th gen CPUs. Recompile the system to something more generic if attempting to use a Gentoo installation from an 11th gen Framework laptop after upgrading it to 12th gen. See the [GCC optimization](https://wiki.gentoo.org/wiki/GCC_optimization "GCC optimization") article for more details on adjusting the `-march` and `-mtune` compiler flags.

### [No Lid Switch and Power Button ACPI events]

If closing the lid or pressing the power button does nothing, check if ACPI events are working:

`user `[`$`]`evtest`

    No device specified, trying to scan all of /dev/input/event*
    Available devices:
    /dev/input/event0:9Lid Switch
    /dev/input/event1:9Power Button
    Select the device event number [0-14]:

Choose the Lid Switch device and close/open the lid. If there is no output, make sure kernel option `CONFIG_ACPI_EC` is enabled.

[KERNEL] **CONFIG_ACPI_EC**

    Power management and ACPI options  --->
      [*] ACPI (Advanced Configuration and Power Interface) Support  ---> Search for <code>CONFIG_ACPI</code> to find this item.
         [*] Embedded Controller  Search for <code>CONFIG_ACPI_EC</code> to find this item.

\

### [Touchpad not working]

If the touchpad is not working (no movement, no clicks, no gestures), verify the \"HID over I2C transport layer ACPI\" driver (see Kernel section / Touchpad) is available as a module or built-in driver.

If \"PIXA3854\" cannot be found in the [dmesg] log, then the kernel is likely missing driver support.

#### [][Without \"HID over I2C transport layer ACPI\"]

`user `[`$`]`dmesg |grep -i hid`

    [    2.499342] hid: raw HID events driver (C) Jiri Kosina
    [    2.499362] usbcore: registered new interface driver usbhid
    [    2.499363] usbhid: USB HID core driver
    [    3.376794] hid-generic 0003:32AC:0002.0001: hiddev96,hidraw0: USB HID v1.11 Device [Framework HDMI Expansion Card] on usb-0000:00:14.0-4/input1

#### [][With \"HID over I2C transport layer ACPI\"]

`user `[`$`]`dmesg |grep -i hid`

    [    2.494448] hid: raw HID events driver (C) Jiri Kosina
    [    2.494474] usbcore: registered new interface driver usbhid
    [    2.494475] usbhid: USB HID core driver
    [    3.371391] hid-generic 0003:32AC:0002.0001: hiddev96,hidraw0: USB HID v1.11 Device [Framework HDMI Expansion Card] on usb-0000:00:14.0-4/input1
    [   19.053758] hid-generic 0018:32AC:0006.0002: input,hidraw1: I2C HID v1.00 Device [FRMW0001:00 32AC:0006] on i2c-FRMW0001:00
    [   19.079450] hid-generic 0018:093A:0274.0003: input,hidraw2: I2C HID v1.00 Mouse [PIXA3854:00 093A:0274] on i2c-PIXA3854:00
    [   19.280641] Module hid_sensor_hub is blacklisted
    [   19.430450] hid-multitouch 0018:093A:0274.0003: input,hidraw2: I2C HID v1.00 Mouse [PIXA3854:00 093A:0274] on i2c-PIXA3854:00

[https://forums.gentoo.org/viewtopic-p-8692426.html#8692426](https://forums.gentoo.org/viewtopic-p-8692426.html#8692426)

[https://forums.gentoo.org/viewtopic-t-1148336-highlight-framework+laptop.html](https://forums.gentoo.org/viewtopic-t-1148336-highlight-framework+laptop.html)

[https://community.frame.work/t/quick-note-on-the-touchpad-linux-kernel-config-for-the-12th-gen-based-laptop/22267/4?u=malachay](https://community.frame.work/t/quick-note-on-the-touchpad-linux-kernel-config-for-the-12th-gen-based-laptop/22267/4?u=malachay)

### [Built-in Keyboard not working on boot to unlock encrypted device]

Set `CONFIG_KEYBOARD_ATKBD` to `y` to enable built-in keyboard to unlock encrypted luks devices

[KERNEL]

    Device Drivers  --->
      Input device support  --->
         [*] Keyboards  ---> Search for <code>CONFIG_INPUT_KEYBOARD</code> to find this item.
            <*> AT keyboard Search for <code>CONFIG_KEYBOARD_ATKBD</code> to find this item.

### [EFI Stub Kernel Boot Failed]

If `CONFIG_EFI_DISABLE_PCI_DMA`is set to `y`, manually selecting the EFI stub kernel on boot will fail with errors:\
\
`EFI stub: ERROR exit_boot() failed!`\
`EFI stub: ERROR efi_main() failed!`\

These errors flash by quickly and one may only see a blue box stating boot failed.

Disable `CONFIG_EFI_DISABLE_PCI_DMA` and recompile to boot the efi stub kernel.

[KERNEL]

    Device Drivers  --->
      Firmware Drivers --->
         EFI (Extensible Firmware Interface) Support  --->
            [ ] Clear Busmaster bit on PCI bridges during ExitBootServices() Search for <code>CONFIG_EFI_DISABLE_PCI_DMA</code> to find this item.

### [Fingerprint reader]

** Note**\
For the last generation of keyboard (generation 13 and recent replacement keyboard), the fingerprint sensor is not working properly with the default firmware. You can wait for framework to push the new firmware to fwupd, but if you know what you are doing and you want an immediate fix, you can follow the instructions here: [\[2\]](https://knowledgebase.frame.work/en_us/updating-fingerprint-reader-firmware-on-linux-for-13th-gen-and-amd-ryzen-7040-series-laptops-HJrvxv_za).

Fingerprints are read via the [fprintd](https://wiki.gentoo.org/wiki/Fingerprint_Reader "Fingerprint Reader") package installed by

`root `[`#`]`emerge --ask sys-auth/fprintd`

Fingerprints are stored on the fingerprint reader itself, so if you register a fingerprint and then switch operating systems, you won\'t be able to register it on the second OS as fprintd gives you \"Enroll result: enroll-duplicate\". This is a problem if you dual-boot or have to re-install linux.

To wipe these fingerprints, install fprintd and use the following python script^[\[2\]](#cite_note-2)^:

[FILE] **`wipe_fingerprints.py`Wipe Fingerprint Script**

    #! /usr/bin/python3

    import gi
    gi.require_version('FPrint', '2.0')
    from gi.repository import FPrint

    ctx = FPrint.Context()

    for dev in ctx.get_devices():
        print(dev)
        print(dev.get_driver())
        print(dev.props.device_id);

        dev.open_sync()

        dev.clear_storage_sync()
        print("All prints deleted.")

        dev.close_sync()

Then run the script with python3 as root:

`root `[`#`]`python3 ./wipe_fingerprints.py`

### [Brightness Keys Not Working]

Due to a quirk^[\[3\]](#cite_note-3)^ with Linux drivers and how the Framework laptop is setup, one cannot have both the ambient light sensor and the brightness keys work. For the brightness keys to function and send XF86MonBrightnessUp / Down events the ambient light sensor driver must be disabled.

To do this ensure that the `hid_sensor_hub` Kernel module is not being loaded. If the `CONFIG_HID_SENSOR_HUB` kernel build option is set to `m` then either unset it and rebuild the kernel, or add a modprobe blacklist rule:

    # /etc/modprobe.d/framework.conf
    blacklist hid_sensor_hub

If `CONFIG_HID_SENSOR_HUB` is set to `y` then unset it and rebuild the kernel^[\[4\]](#cite_note-4)^.

### [Freezing with 6.4 series kernels]

It is necessary to boot with tpm_tis.interrupts=0 in order to avoid a hang at boot as of 6.4.3.^[\[5\]](#cite_note-5)^

## [See also]

-   [Framework Expansion Cards](https://wiki.gentoo.org/wiki/Framework_Expansion_Cards "Framework Expansion Cards")
-   [Framework Laptop 16](https://wiki.gentoo.org/wiki/Framework_Laptop_16 "Framework Laptop 16") --- a highly modular and repairable 16 inch laptop
-   [Framework Laptop 12](https://wiki.gentoo.org/index.php?title=Framework_Laptop_12&action=edit&redlink=1 "Framework Laptop 12 (page does not exist)")
-   [Framework Desktop](https://wiki.gentoo.org/index.php?title=Framework_Desktop&action=edit&redlink=1 "Framework Desktop (page does not exist)")

## [References]

1.  [[[↑](#cite_ref-1)] [[https://frame.work/blog/solving-for-silicon-shortages](https://frame.work/blog/solving-for-silicon-shortages)]]
2.  [[[↑](#cite_ref-2)] [[https://community.frame.work/t/fingerprint-scanner-compatibility-with-linux-ubuntu-fedora-etc/1501/206](https://community.frame.work/t/fingerprint-scanner-compatibility-with-linux-ubuntu-fedora-etc/1501/206)]]
3.  [[[↑](#cite_ref-3)] [[https://community.frame.work/t/responded-12th-gen-not-sending-xf86monbrightnessup-down/20605/11](https://community.frame.work/t/responded-12th-gen-not-sending-xf86monbrightnessup-down/20605/11)]]
4.  [[[↑](#cite_ref-4)] [[https://community.frame.work/t/some-issues-running-gentoo-linux/12017/20](https://community.frame.work/t/some-issues-running-gentoo-linux/12017/20)]]
5.  [[[↑](#cite_ref-5)] [[https://community.frame.work/t/tracking-kernel-6-4-hangs-at-ima-allocated-hash-algorithm-sha1/32956/41?page=3](https://community.frame.work/t/tracking-kernel-6-4-hangs-at-ima-allocated-hash-algorithm-sha1/32956/41?page=3)]]