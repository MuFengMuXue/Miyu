[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Lenovo_IdeaPad_Flex_5_13IML05_Chromebook&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Official Support Page](https://pcsupport.lenovo.com/us/en/products/chromebook-laptops/lenovo-chromebooks-series/flex-5-cb-13iml05)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/IdeaPad/IdeaPad_Flex_5_CB_13IML05/IdeaPad_Flex_5_CB_13IML05_Spec.pdf)

[[]][Specifications (by region)](https://psref.lenovo.com/Product/IdeaPad/IdeaPad_Flex_5_CB_13IML05?tab=model)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/consumer/mobiles_pub/flex5cb_13iml05.pdf)

[[]][User Guide](https://download.lenovo.com/consumer/mobiles_pub/flex_5_13iml_ug_en_202005.pdf)

[![](/images/thumb/b/b1/Lenovo_IdeaPad_Flex_5_13IML05_Chromebook.jpg/300px-Lenovo_IdeaPad_Flex_5_13IML05_Chromebook.jpg)](https://wiki.gentoo.org/wiki/File:Lenovo_IdeaPad_Flex_5_13IML05_Chromebook.jpg)

[](https://wiki.gentoo.org/wiki/File:Lenovo_IdeaPad_Flex_5_13IML05_Chromebook.jpg "Enlarge")

Lenovo IdeaPad Flex 5 13IML05 Chromebook

The **Lenovo IdeaPad Flex 5 13IML05 Chromebook** is a Chromebook released in 2020. ^[\[1\]](#cite_note-1)^ The code name of this Chromebook is **Akemi**.

This Chromebook **should not** be confused with the [Lenovo IdeaPad Flex 5 13ITL6 Chromebook](https://psref.lenovo.com/Product/IdeaPad/IP_Flex_5_Chrome_13ITL6) released in 2021. ^[\[2\]](#cite_note-2)^

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [Accessories]](#Accessories)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Gentoo LiveGUI USB Image]](#Gentoo_LiveGUI_USB_Image)
        -   [[2.1.1] [Sound]](#Sound)
    -   [[2.2] [Firmware]](#Firmware)
    -   [[2.3] [Kernel]](#Kernel)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Sound]](#Sound_2)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)
-   [[6] [References]](#References)

## [Hardware]

### [Standard]

  --------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------- -------- ------------------------ ----------------------------------------------------------- ---------------- -------------------------------------------------------------------------------------------------------------------
  Device                Make/model                                                                                                                                                       Status   Vendor ID / Product ID   Kernel driver(s)                                            Kernel version   Notes
  CPU                   Intel® Core™ i3-10110U                                                                                                                                           Works    N/A                      N/A                                                         6.6.13
  GPU                   Intel Corporation CometLake-U GT2 \[UHD Graphics\]                                                                                                               Works    8086:9b41                i915                                                        6.6.13
  SSD                   Samsung Electronics Co Ltd NVMe SSD Controller 980                                                                                                               Works    144d:a809                nvme                                                        6.6.13
  MicroSD card reader   Intel Corporation Comet Lake PCH-LP SCS3                                                                                                                         Works    8086:02f5                sdhci-pci                                                   6.6.13
  USB Ports             Intel Corporation Comet Lake PCH-LP USB 3.1 xHCI Host Controller                                                                                                 Works    N/A                      xhci_hcd                                                    6.6.13
  Wi-Fi                 [Intel® Wi-Fi 6 AX201](https://www.intel.com/content/www/us/en/products/sku/130293/intel-wifi-6-ax201-gig/specifications.html)   Works    8086:02f0                [iwlwifi](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi")   6.6.13           The card is affected by [a bug](https://wiki.gentoo.org/wiki/Iwlwifi#Network_crashes_under_heavy_load "Iwlwifi").
  Bluetooth             [Intel® Wi-Fi 6 AX201](https://www.intel.com/content/www/us/en/products/sku/130293/intel-wifi-6-ax201-gig/specifications.html)   Works    8087:0026                btusb                                                       6.6.13
  Speakers              Intel Corporation Comet Lake PCH-LP cAVS                                                                                                                         Works    8086:02c8                sof-audio-pci-intel-cnl                                     6.6.13
  Microphone            Intel Corporation Comet Lake PCH-LP cAVS                                                                                                                         Works    N/A                      sof-audio-pci-intel-cnl                                     6.6.13
  3.5mm jack            Intel Corporation Comet Lake PCH-LP cAVS                                                                                                                         Works    N/A                      sof-audio-pci-intel-cnl                                     6.6.13
  Touchpad              N/A                                                                                                                                                              Works    06cb:cde1                N/A                                                         6.6.13
  Touchscreen           N/A                                                                                                                                                              Works    27c6:0e32                N/A                                                         6.6.13
  Webcam                Syntek Integrated Camera                                                                                                                                         Works    174f:244f                uvcvideo                                                    6.6.13
  Accelerometer         N/A                                                                                                                                                              Works    N/A                      N/A                                                         6.6.38
  --------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------- -------- ------------------------ ----------------------------------------------------------- ---------------- -------------------------------------------------------------------------------------------------------------------

### [Accessories]

  -------- ------------ ------------- -------- ------------------ ---------------- -------
  Device   Make/model   Status        Bus ID   Kernel driver(s)   Kernel version   Notes
  Stylus   N/A          Not tested    N/A      N/A                N/A
  -------- ------------ ------------- -------- ------------------ ---------------- -------

## [Installation]

** Warning**\
Installing the operating system on this Chromebook requires [flashing the UEFI firmware](https://wiki.archlinux.org/title/Lenovo_IdeaPad_Flex_5_13IML05_Chromebook#UEFI%20Firmware%20Flashing).

### [Gentoo LiveGUI USB Image]

#### [Sound]

** Warning**\
The following script automatically re-logins the user, causing running applications to stop working. Save any changes before running the script to prevent data loss.

** Important**\
The script requires root privileges.

By default, the sound card is disabled and there is no output to the speakers. The image does not contain required firmware blobs, so it is necessary to install them. The following script installs the blobs and configures PipeWire to use the sound card.

[FILE] **`sound.sh`**

    #!/bin/bash
    emerge --sync
    emerge sof-firmware
    rmmod snd_sof_pci_intel_cnl
    modprobe snd_sof_pci_intel_cnl
    echo "media-video/pipewire pipewire-alsa" > /etc/portage/package.use/pipewire
    emerge pipewire
    usermod -aG pipewire gentoo
    mkdir -p /etc/pipewire/pipewire.conf.d
    cat <<EOF > /etc/pipewire/pipewire.conf.d/alsa.conf
    context.objects = [

      }


      }
    ]
    EOF
    loginctl terminate-user gentoo

### [Firmware]

WiFi, Bluetooth, GPU blobs:

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

-   iwlwifi-QuZ-a0-hr-b0-77.ucode
-   intel/ibt-19-0-4.sfi
-   intel/ibt-19-0-4.ddc
-   i915/kbl_dmc_ver1_04.bin

\
Sound blobs:

`root `[`#`]`emerge --ask sys-firmware/sof-firmware`

-   intel/sof/community/sof-cml.ri
-   intel/sof-tplg/sof-cml-rt5682-max98357a.tplg

\
CPU blobs:

`root `[`#`]`emerge --ask sys-firmware/intel-microcode`

-   intel-ucode/06-8e-0c

### [Kernel]

[KERNEL] **All required external firmware (kernel version 6.6.13)**

    Device Drivers  --->
        Generic Driver Options  --->
            Firmware loader --->
                -*- Firmware loading facility
                (intel-ucode/06-8e-0c iwlwifi-QuZ-a0-hr-b0-77.ucode intel/ibt-19-0-4.sfi intel/ibt-19-0-4.ddc intel/sof/community/sof-cml.ri intel/sof-tplg/sof-cml-rt5682-max98357a.tplg i915/kbl_dmc_ver1_04.bin) External firmware blobs to build into the kernel binary Search for <code>CONFIG_EXTRA_FIRMWARE</code> to find this item.
                (/lib/firmware) Firmware blobs root directory Search for <code>CONFIG_EXTRA_FIRMWARE_DIR</code> to find this item.

[KERNEL] **Graphics**

    Device Drivers  --->
        Graphics support  --->
            Frame buffer Devices  --->
                [*] Support for frame buffer devices Search for <code>CONFIG_FB</code> to find this item.
            [*] Direct Rendering Manager (XFree86 4.1.0 and higher DRI support) Search for <code>CONFIG_DRM</code> to find this item.
            [*] Intel 8xx/9xx/G3x/G4x/HD Graphics Search for <code>CONFIG_DRM_I915</code> to find this item.
            [*] Enable legacy fbdev support for your modesetting driver Search for <code>CONFIG_DRM_FBDEV_EMULATION</code> to find this item.

[KERNEL] **SSD**

    Device Drivers  --->
        NVME Support  --->
            [*] NVM Express block device Search for <code>CONFIG_BLK_DEV_NVME</code> to find this item.

[KERNEL] **WiFi**

    Device Drivers  --->
       [*] Network device support  --->
           [*] Wireless LAN  --->
               [*] Intel devices Search for <code>CONFIG_WLAN_VENDOR_INTEL</code> to find this item.
               [*]   Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi) Search for <code>CONFIG_IWLWIFI</code> to find this item.
               [*]     Intel Wireless WiFi MVM Firmware support Search for <code>CONFIG_IWLMVM</code> to find this item.

[KERNEL] **I2C Bus**

    Device Drivers  --->
        I2C support  --->
            -*- I2C support
                  I2C Hardware Bus support  --->
                      [*] Intel 82801 (ICH/PCH) Search for <code>CONFIG_I2C_I801</code> to find this item.
                      [*] Synopsys DesignWare Platform Search for <code>CONFIG_I2C_DESIGNWARE_PLATFORM</code> to find this item.
                      [*] Synopsys DesignWare PCI Search for <code>CONFIG_I2C_DESIGNWARE_PCI</code> to find this item.
        HID bus support  --->
            --- HID bus support
            [*]   I2C HID support  --->
                    [*] HID over I2C transport layer ACPI driver Search for <code>CONFIG_I2C_HID_ACPI</code> to find this item.

[KERNEL] **Touchscreen (relies on the I2C bus)**

    Device Drivers  --->
        HID bus support  --->
            --- HID bus support
            [*]   Generic HID driver Search for <code>CONFIG_HID_GENERIC</code> to find this item.

[KERNEL] **Touchpad (relies on the I2C bus)**

    Device Drivers  --->
        HID bus support  --->
            --- HID bus support
                  Special HID drivers  --->
                      [*] Synaptics RMI4 device support Search for <code>CONFIG_HID_RMI</code> to find this item.

[KERNEL] **External USB mouses (optional)**

    Device Drivers  --->
        HID bus support  --->
            --- HID bus support
                  USB HID support  --->
                    [*] USB HID transport layer Search for <code>CONFIG_USB_HID</code> to find this item.

[KERNEL] **Sound**

    Device Drivers  --->
        -*- Pin controllers  --->
            Intel pinctrl drivers  --->
                [*] Intel Cannon Lake PCH pinctrl and GPIO driver Search for <code>CONFIG_PINCTRL_CANNONLAKE</code> to find this item.
        [*] Sound card support  --->
            [*] Advanced Linux Sound Architecture  --->
                HD-Audio  --->
                    [*] Build HDMI/DisplayPort HD-audio codec support Search for <code>CONFIG_SND_HDA_CODEC_HDMI</code> to find this item.
                [*] ALSA for SoC audio support  --->
                    [*] Sound Open Firmware Support  --->
                        [*] SOF PCI enumeration support Search for <code>CONFIG_SND_SOC_SOF_PCI</code> to find this item.
                        [*] SOF support for Intel audio DSPs Search for <code>CONFIG_SND_SOC_SOF_INTEL_TOPLEVEL</code> to find this item.
                        [*] SOF support for CometLake Search for <code>CONFIG_SND_SOC_SOF_COMETLAKE</code> to find this item.
                        [*] SOF support for HDA Links(HDA/HDMI) Search for <code>CONFIG_SND_SOC_SOF_HDA_LINK</code> to find this item.
                        [*]   SOF support for HDAudio codecs Search for <code>CONFIG_SND_SOC_SOF_HDA_AUDIO_CODEC</code> to find this item.
                    -*- Intel Machine drivers  --->
                        [*] SOF with rt5682 codec in I2S Mode Search for <code>CONFIG_SND_SOC_INTEL_SOF_RT5682_MACH</code> to find this item.

[KERNEL] **Webcam**

    Device Drivers  --->
        Multimedia support  --->
            --- Multimedia support
                  Media core support  --->
                    [*] Video4Linux core Search for <code>CONFIG_VIDEO_DEV</code> to find this item.
                  Media drivers  --->
                    [*] Media USB Adapters  --->
                          --- Media USB Adapters
                          [*]   USB Video Class (UVC) Search for <code>CONFIG_USB_VIDEO_CLASS</code> to find this item.

[KERNEL] **Accelerometer**

    Device Drivers  --->
        [*] Platform support for Chrome hardware  --->
            [*]   ChromeOS Embedded Controller Search for <code>CONFIG_CROS_EC</code> to find this item.
            [*]     ChromeOS Embedded Controller (LPC) Search for <code>CONFIG_CROS_EC_LPC</code> to find this item.
            [*]   ChromeOS EC MEMS Sensor Hub Search for <code>CONFIG_CROS_EC_SENSORHUB</code> to find this item.
        [*] Industrial I/O support  --->
            [*]   ChromeOS EC Sensors Core Search for <code>CONFIG_IIO_CROS_EC_SENSORS_CORE</code> to find this item.
            [*]     ChromeOS EC Contiguous Sensor Search for <code>CONFIG_IIO_CROS_EC_SENSORS</code> to find this item.

** Note**\
The accelerometer can be tested by running the following command:

`user `[`$`]`cat /sys/bus/iio/devices/iio\:device0/in_accel_x_raw`

## [Configuration]

### [Sound]

** Important**\
The user must belong to the **audio** and **pipewire** groups, otherwise the daemon will not connect to the sink.

Install [[[media-video/pipewire]](https://packages.gentoo.org/packages/media-video/pipewire)[]] with the following USE flags: **sound-server**, **pipewire-alsa**, **bluetooth** (optional).

The sound doesn\'t work out of the box, so you have to manually specify the sink and source. In the case of Bluetooth or 3.5mm jack, no additional configuration is required.

[FILE] **`/etc/pipewire/pipewire.conf.d/alsa.conf`**

    context.objects = [

      }


      }
    ]

## [See also]

-   [Chromebook](https://wiki.gentoo.org/wiki/Chromebook "Chromebook")
-   [Chromebook/Sound configuration](https://wiki.gentoo.org/wiki/Chromebook/Sound_configuration "Chromebook/Sound configuration")

## [External resources]

-   [ArchLinux » Lenovo IdeaPad Flex 5 13IML05 Chromebook](https://wiki.archlinux.org/title/Lenovo_IdeaPad_Flex_5_13IML05_Chromebook)

## [References]

1.  [[[↑](#cite_ref-1)] [[https://news.lenovo.com/pressroom/press-releases/lenovo-breaks-barriers-with-new-consumer-technology-unveiled-at-ces-2020-2/](https://news.lenovo.com/pressroom/press-releases/lenovo-breaks-barriers-with-new-consumer-technology-unveiled-at-ces-2020-2/)]]
2.  [[[↑](#cite_ref-2)] [[https://news.lenovo.com/pressroom/press-releases/consumer-devices-for-living-a-hybrid-life-simply-mwc/](https://news.lenovo.com/pressroom/press-releases/consumer-devices-for-living-a-hybrid-life-simply-mwc/)]]