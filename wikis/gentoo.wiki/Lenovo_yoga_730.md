[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Lenovo_yoga_730&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

## [Hardware]

intel gen8 i7 16gb ram nvidia gforce 1050 512GB nvm-e

i was not able to get the drives to be recognized when sata mode was set to RST in the bios. it would be nice that one didn\'t have to switch RST - AHCI in bios to get the stock windows installation to boot back and forth.

the touchpad is a i2c_designware_platform device. the following modules are necessary: intel_lpss_pci, i2c_designware, pinctrl_sunrisepoint, i2c_hid. To configure the touchpad as an *actual* touchpad with two-finger scrolling etc, then it is also necessary to enable the HID_MULTITOUCH option in the kernel. Without this, the touchpad may only be recognized as a pointer/mouse. More information [at this forum post](https://forums.gentoo.org/viewtopic-t-1098936.html).

wifi driver for 4.14.83 is in Device Drivers \--\> Staging Drivers \--\> Realtek RTL8822BE Wireless Network Adapter

wifi driver for 5.4.38 is in Device Drivers \--\> Network device Support \--\> WIreless LAN \--\> Realtek 802.11ac wireless chip support \--\> Realtek 8822BE PCI wireless network adapter

todo:

      sound
      touch screen and pen
      better tablet mode behavior

output of lspci

`root `[`#`]`lspci`

    00:00.0 Host bridge: Intel Corporation Device 5914 (rev 08)
    00:02.0 VGA compatible controller: Intel Corporation Device 5917 (rev 07)
    00:04.0 Signal processing controller: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem (rev 08)
    00:14.0 USB controller: Intel Corporation Sunrise Point-LP USB 3.0 xHCI Controller (rev 21)
    00:14.2 Signal processing controller: Intel Corporation Sunrise Point-LP Thermal subsystem (rev 21)
    00:15.0 Signal processing controller: Intel Corporation Sunrise Point-LP Serial IO I2C Controller #0 (rev 21)
    00:15.1 Signal processing controller: Intel Corporation Sunrise Point-LP Serial IO I2C Controller #1 (rev 21)
    00:15.2 Signal processing controller: Intel Corporation Sunrise Point-LP Serial IO I2C Controller #2 (rev 21)
    00:16.0 Communication controller: Intel Corporation Sunrise Point-LP CSME HECI #1 (rev 21)
    00:1c.0 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #1 (rev f1)
    00:1c.3 PCI bridge: Intel Corporation Device 9d13 (rev f1)
    00:1c.4 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #5 (rev f1)
    00:1d.0 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #9 (rev f1)
    00:1e.0 Signal processing controller: Intel Corporation Sunrise Point-LP Serial IO UART Controller #0 (rev 21)
    00:1f.0 ISA bridge: Intel Corporation Device 9d4e (rev 21)
    00:1f.2 Memory controller: Intel Corporation Sunrise Point-LP PMC (rev 21)
    00:1f.3 Audio device: Intel Corporation Sunrise Point-LP HD Audio (rev 21)
    00:1f.4 SMBus: Intel Corporation Sunrise Point-LP SMBus (rev 21)
    3a:00.0 Network controller: Realtek Semiconductor Co., Ltd. Device b822
    3b:00.0 3D controller: NVIDIA Corporation GP107M [GeForce GTX 1050 Mobile] (rev a1)
    3c:00.0 Non-Volatile memory controller: Samsung Electronics Co Ltd Device a808

`root `[`#`]`lsusb`

    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 006: ID 0bda:b023 Realtek Semiconductor Corp.
    Bus 001 Device 005: ID 06cb:0081 Synaptics, Inc.
    Bus 001 Device 004: ID 13d3:56b2 IMC Networks
    Bus 001 Device 002: ID abcd:1234 Unknown
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

output of lsmod on a fairly lean and working system:

`root `[`#`]`lsmod`

    Module                  Size  Used by
    rfcomm                 36864  12
    bnep                   20480  2
    uvcvideo              106496  0
    videobuf2_vmalloc      16384  1 uvcvideo
    videobuf2_memops       16384  1 videobuf2_vmalloc
    videobuf2_v4l2         24576  1 uvcvideo
    btusb                  49152  0
    btrtl                  16384  1 btusb
    videodev              200704  2 videobuf2_v4l2,uvcvideo
    btbcm                  16384  1 btusb
    btintel                20480  1 btusb
    videobuf2_common       49152  2 videobuf2_v4l2,uvcvideo
    bluetooth             425984  43 btrtl,btintel,btbcm,bnep,btusb,rfcomm
    ecdh_generic           16384  1 bluetooth
    ecc                    28672  1 ecdh_generic
    nvidia_drm             45056  0
    mousedev               24576  0
    bbswitch               16384  0
    hid_sensor_custom      24576  0
    wacom                 106496  0
    hid_sensor_hub         20480  1 hid_sensor_custom
    hid_multitouch         28672  0
    snd_hda_codec_hdmi     57344  1
    i2c_designware_platform    16384  0
    i2c_designware_core    20480  1 i2c_designware_platform
    intel_rapl_msr         20480  0
    snd_hda_codec_realtek   106496  1
    wmi_bmof               16384  0
    snd_hda_codec_generic    77824  1 snd_hda_codec_realtek
    nvidia_modeset       1077248  1 nvidia_drm
    x86_pkg_temp_thermal    20480  0
    intel_powerclamp       20480  0
    snd_hda_intel          40960  6
    snd_intel_nhlt         16384  1 snd_hda_intel
    snd_hda_codec         122880  4 snd_hda_codec_generic,snd_hda_codec_hdmi,snd_hda_intel,snd_hda_codec_realtek
    snd_hwdep              16384  1 snd_hda_codec
    snd_hda_core           77824  5 snd_hda_codec_generic,snd_hda_codec_hdmi,snd_hda_intel,snd_hda_codec,snd_hda_codec_realtek
    snd_pcm                98304  4 snd_hda_codec_hdmi,snd_hda_intel,snd_hda_codec,snd_hda_core
    rtwpci                 24576  0
    i2c_i801               28672  0
    rtw88                 487424  1 rtwpci
    processor_thermal_device    20480  0
    intel_rapl_common      28672  2 intel_rapl_msr,processor_thermal_device
    mei_me                 40960  0
    intel_soc_dts_iosf     20480  1 processor_thermal_device
    intel_lpss_pci         20480  0
    mei                    77824  1 mei_me
    intel_lpss             16384  1 intel_lpss_pci
    mfd_core               16384  2 hid_sensor_hub,intel_lpss
    intel_pch_thermal      16384  0
    i2c_hid                28672  0
    ideapad_laptop         24576  0
    int3403_thermal        16384  0
    int340x_thermal_zone    16384  2 int3403_thermal,processor_thermal_device
    wmi                    24576  2 wmi_bmof,ideapad_laptop
    acpi_pad               20480  0
    pinctrl_sunrisepoint    28672  1
    pinctrl_intel          24576  1 pinctrl_sunrisepoint
    int3400_thermal        16384  0
    acpi_thermal_rel       16384  1 int3400_thermal
    nvidia              20185088  7 nvidia_modeset
    efivarfs               16384  1
    configfs               36864  1
    fuse                  118784  1
    nfs                   266240  0
    lockd                  90112  1 nfs
    grace                  16384  1 lockd
    sunrpc                344064  2 lockd,nfs

more to come