[] This article is a **work in progress**; treat its contents with caution - [vowstar](https://wiki.gentoo.org/wiki/User:Vowstar "User:Vowstar") ([talk](https://wiki.gentoo.org/index.php?title=User_talk:Vowstar&action=edit&redlink=1 "User talk:Vowstar (page does not exist)") \| [contribs](https://wiki.gentoo.org/wiki/Special:Contributions/vowstar "Special:Contributions/vowstar")).

**Resources**

[[]][Official Support Page](https://support.hp.com/us-en/product/details/hp-elitebook-845-14-inch-g10-notebook-pc/2101628462)

[[]][Specifications](https://support.hp.com/us-en/document/ish_8110922-8110971-16)

[[]][Hardware Maintenance Manual](https://kaas.hpcloud.hp.com/pdf-public/pdf_7964747_en-US-1.pdf)

[[]][User Guide](https://kaas.hpcloud.hp.com/pdf-public/pdf_6902679_en-US-1.pdf)

[[]][Wikipedia](https://en.wikipedia.org/wiki/HP_EliteBook "wikipedia:HP EliteBook")

## Contents

-   [[1] [Standard]](#Standard)
-   [[2] [Troubleshooting]](#Troubleshooting)
    -   [[2.1] [Screen flickering white]](#Screen_flickering_white)
    -   [[2.2] [ELAN I2C touch pad not working]](#ELAN_I2C_touch_pad_not_working)
    -   [[2.3] [PCIe Bus Error for nvme]](#PCIe_Bus_Error_for_nvme)
    -   [[2.4] [Speaker no sound]](#Speaker_no_sound)
    -   [[2.5] [Mute/micmute LEDs does not lit]](#Mute.2Fmicmute_LEDs_does_not_lit)
    -   [[2.6] [Suspend does not work]](#Suspend_does_not_work)

### [Standard]

  --------------------- -------------------------------------------------------------------------------------------- -------- ----------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------- ---------------- ---------------------------------------------------------------------------
  Device                Make/model                                                                                   Status   Vendor ID / Product ID                                                                                                  Kernel driver(s)                                                                Kernel version   Notes
  Video card            Advanced Micro Devices, Inc. \[AMD/ATI\] Phoenix1 (rev d3) Radeon™ 780M Graphics             Works    \[1002:15bf\]                                                                                                           amdgpu                                                                          6.4.11           Require amdgpu.sg_display=0 kernel parameter if kernel lower than 6.4.11.
  Audio card            Advanced Micro Devices, Inc. \[AMD/ATI\] Rembrandt Radeon High Definition Audio Controller   Works    \[1002:1640\]                                                                                                           snd_hda_intel                                                                   6.4.11           ---
  Audio card            Advanced Micro Devices, Inc. \[AMD\] Family 17h/19h HD Audio Controller                      Works    \[1022:15e3\]                                                                                                           snd_hda_intel                                                                   6.4.11           ---
  Audio Coprocessor     Advanced Micro Devices, Inc. \[AMD\] ACP/ACP3X/ACP6x Audio Coprocessor                       Works    \[1022:15e2\]                                                                                                           snd_acp_pci,snd_pci_ps                                                          6.4.11           ---
  Network controller    MEDIATEK Corp. MT7922 802.11ax PCI Express Wireless Network Adapter                          Works    \[14c3:0616\]                                                                                                           mt7921e                                                                         6.4.11           Required sys-kernel/linux-firmware
  Bluetooth             MEDIATEK Corp. MT7922 Bluetooth Adapter                                                      Works    \[0489:e0f2\]                                                                                                           btusb                                                                           6.4.11           Required sys-kernel/linux-firmware
  Web Camera            Quanta Computer, Inc. HP 5MP Camera                                                          Works    \[0408:545f\]                                                                                                           uvcvideo                                                                        6.4.11           Both infrared and normal cameras work
  Fingerprint Reader    Synaptics, Inc.                                                                              Works    [06cb:00f0](https://linux-hardware.org/?id=usb:06cb-00f0)                                                                                                               6.4.11           ---
  Touchpad              Elantech I2C HID Touchpad                                                                    Works    [04F3:31EC](https://linux-hardware.org/?view=search&vendorid=04f3&deviceid=31ec#list)   i2c_designware_platform, i2c_hid, hid_generic, hid_multitouch                   6.4.11           ---
  Speaker               Cirrus Logic CS35L41(CSC3551) audio amplifier                                                Works    \[???\]                                                                                                                 serial_multi_instantiate, i2c_designware_platform, snd_hda_scodec_cs35l41_i2c   6.4.11           Required sys-kernel/linux-firmware
  LEDs on the buttons   ???                                                                                          Works    ???                                                                                                                     ???                                                                             6.4.11           The kernel version must be greater than or equal to 6.4.6.
  --------------------- -------------------------------------------------------------------------------------------- -------- ----------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------- ---------------- ---------------------------------------------------------------------------

## [Troubleshooting]

### [Screen flickering white]

Check kernel version, should above or equal 6.4.11

See [AMDGPU#Flickering_and_white_screens](https://wiki.gentoo.org/wiki/AMDGPU#Flickering_and_white_screens "AMDGPU") for resolution.

### [ELAN I2C touch pad not working]

Make sure CONFIG_PINCTRL_AMD, CONFIG_I2C_HID, CONFIG_I2C_DESIGNWARE_PLATFORM and CONFIG_HID_MULTITOUCH is set.

AMDI0010 I2C should be in dmesg.

` [ 1.724985] input: ELAN07A8:00 04F3:31EC Mouse as /devices/platform/AMDI0010:00/i2c-0/i2c-ELAN07A8:00/0018:04F3:31EC.0001/input/input6 `

`[ 1.725046] input: ELAN07A8:00 04F3:31EC Touchpad as /devices/platform/AMDI0010:00/i2c-0/i2c-ELAN07A8:00/0018:04F3:31EC.0001/input/input8 `

[https://forums.gentoo.org/viewtopic-t-1109820-start-0.html](https://forums.gentoo.org/viewtopic-t-1109820-start-0.html) [https://patchwork.kernel.org/project/linux-acpi/patch/1457609692-25903-1-git-send-email-Xiangliang.Yu@amd.com/](https://patchwork.kernel.org/project/linux-acpi/patch/1457609692-25903-1-git-send-email-Xiangliang.Yu@amd.com/)

### [PCIe Bus Error for nvme]

PCIe Bus Error: severity=Corrected, type=Physical Layer, id=00e5(Receiver ID)

Due to PCIe Active State Power Management that is transitioning the link to a lower power state and maybe causing the device to trigger these errors. Using the pcie_aspm=off boot parameter could solve this problem but increase the power consumption as it disables the power savings.

[https://askubuntu.com/questions/863150/pcie-bus-error-severity-corrected-type-physical-layer-id-00e5receiver-id](https://askubuntu.com/questions/863150/pcie-bus-error-severity-corrected-type-physical-layer-id-00e5receiver-id)

### [Speaker no sound]

-   Check kernel version, should above 6.3.8
-   Make sure CONFIG_SERIAL_MULTI_INSTANTIATE, CONFIG_SND_SOC_CS35L41_I2C, CONFIG_SND_SOC_AMD_ACP6x, CONFIG_SND_SOC_ACPI, CONFIG_SND_HDA_CODEC_REALTEK is set.
-   Make sure `i2cdetect -r -a 1 ` shows devices on address 40 and 42.
-   Make sure ` hwinfo | grep CSC3551 ` shows ` modalias = "acpi:CSC3551:", driver = "Serial bus multi instantiate pseudo device driver" `
-   Make sure ` hwinfo | grep cs35l41-hda ` shows ` cs35l41-hda: module = snd_hda_scodec_cs35l41_i2c `

### [][Mute/micmute LEDs does not lit]

The kernel version must be greater than or equal to 6.4.6, and upgrading the kernel to 6.4.6 will work normally.

### [Suspend does not work]

This laptop lacks support for classic S3 suspend, It only supports S2 suspend mode. Regarding the suspend mode, with the help of Mario Limonciello, after enabling CONFIG_AMD_PMC (kernel 6.4.6), I tested suspend and wake up separately, and it has worked normally.