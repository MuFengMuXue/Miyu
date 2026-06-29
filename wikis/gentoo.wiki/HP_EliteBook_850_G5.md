**Resources**

[[]][Official Support Page](https://support.hp.com/us-en/product/details/hp-elitebook-850-g5-notebook-pc/18491276)

[[]][Specifications](https://support.hp.com/us-en/document/c05903028)

[[]][Hardware Maintenance Manual](http://h10032.www1.hp.com/ctg/Manual/c06189562.pdf)

[[]][User Guide](https://h10032.www1.hp.com/ctg/Manual/c05920079.pdf)

[[]][HP EliteBook](https://en.wikipedia.org/wiki/HP_EliteBook "wikipedia:HP EliteBook")

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [lspci]](#lspci)
    -   [[1.3] [lsusb]](#lsusb)
    -   [[1.4] [Keyboard]](#Keyboard)
    -   [[1.5] [Smart card reader]](#Smart_card_reader)

## [Hardware]

### [Standard]

  -------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------- ------------------ -------------------------------------------------------------
  Device               Make/model                                                                                                                                                           Status      Kernel driver(s)   Kernel version
  CPU                  Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz                                                                                                                             Works                          4.14.65
  Memory               1 x 16GB DDR4-2400MHz                                                                                                                                                Works
  Hard disk            [Samsung PM981 MZVLB512HAJQ](https://www.samsung.com/semiconductor/ssd/client-ssd/MZVLB512HAJQ/) 512GB PCIe NVMe Solid State Drive   Works       nvme               4.14.65
  Video card           Intel UHD Graphics 620                                                                                                                                               Works       intel i965         4.14.65
  Wireless             Intel Corporation Wireless 8265 / 8275 (rev 78)                                                                                                                      Works       iwlwifi            4.14.65
  Ethernet             Intel Corporation Ethernet Connection                                                                                                                                Works       e1000e             4.14.65
  Touchpad             Synaptics TouchPad                                                                                                                                                   Works
  Keyboard             Backlight keyboard                                                                                                                                                   Works                          4.14.65 plus some needed tweaks to make LED buttons working
  Bluetooth                                                                                                                                                                                 Works
  USB 3.0                                                                                                                                                                                   Works       xhci_hcd
  Thunderbolt                                                                                                                                                                               Untested    ?
  Smart Card Reader    SC                                                                                                                                                                   Works                          4.14.65
  Webcam               Cheng Uei Precision Industry Co., Ltd (Foxlink)                                                                                                                      Works       uvc                4.18.x plus 2 patches
  Microphone           Dual array digital microphones                                                                                                                                       Works       ?
  Fingerprint reader   138a:00ab Validity Sensors, Inc.                                                                                                                                     No
  -------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------- ------------------ -------------------------------------------------------------

### [lspci]

`root `[`#`]`lspci -k `

    00:00.0 Host bridge: Intel Corporation Device 5914 (rev 08)
            Subsystem: Hewlett-Packard Company Device 83b2
    00:02.0 VGA compatible controller: Intel Corporation Device 5917 (rev 07)
            Subsystem: Hewlett-Packard Company Device 83b2
        Kernel driver in use: i915
    00:04.0 Signal processing controller: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem (rev 08)
        Subsystem: Hewlett-Packard Company Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem
        Kernel driver in use: proc_thermal
        Kernel modules: processor_thermal_device
    00:13.0 Non-VGA unclassified device: Intel Corporation Sunrise Point-LP Integrated Sensor Hub (rev 21)
        Subsystem: Hewlett-Packard Company Sunrise Point-LP Integrated Sensor Hub
        Kernel driver in use: intel_ish_ipc
        Kernel modules: intel_ish_ipc
    00:14.0 USB controller: Intel Corporation Sunrise Point-LP USB 3.0 xHCI Controller (rev 21)
        Subsystem: Hewlett-Packard Company Sunrise Point-LP USB 3.0 xHCI Controller
        Kernel driver in use: xhci_hcd
        Kernel modules: xhci_pci
    00:14.2 Signal processing controller: Intel Corporation Sunrise Point-LP Thermal subsystem (rev 21)
        Subsystem: Hewlett-Packard Company Sunrise Point-LP Thermal subsystem
        Kernel driver in use: intel_pch_thermal
        Kernel modules: intel_pch_thermal
    00:15.0 Signal processing controller: Intel Corporation Sunrise Point-LP Serial IO I2C Controller #0 (rev 21)
        Subsystem: Hewlett-Packard Company Sunrise Point-LP Serial IO I2C Controller
        Kernel driver in use: intel-lpss
        Kernel modules: intel_lpss_pci
    00:15.1 Signal processing controller: Intel Corporation Sunrise Point-LP Serial IO I2C Controller #1 (rev 21)
        Subsystem: Hewlett-Packard Company Sunrise Point-LP Serial IO I2C Controller
        Kernel driver in use: intel-lpss
        Kernel modules: intel_lpss_pci
    00:16.0 Communication controller: Intel Corporation Sunrise Point-LP CSME HECI #1 (rev 21)
        Subsystem: Hewlett-Packard Company Sunrise Point-LP CSME HECI
        Kernel driver in use: mei_me
        Kernel modules: mei_me
    00:1c.0 PCI bridge: Intel Corporation Device 9d13 (rev f1)
        Kernel driver in use: pcieport
    00:1c.4 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #5 (rev f1)
        Kernel driver in use: pcieport
    00:1d.0 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #9 (rev f1)
        Kernel driver in use: pcieport
    00:1f.0 ISA bridge: Intel Corporation Device 9d4e (rev 21)
        Subsystem: Hewlett-Packard Company Device 83b2
    00:1f.2 Memory controller: Intel Corporation Sunrise Point-LP PMC (rev 21)
        Subsystem: Hewlett-Packard Company Sunrise Point-LP PMC
    00:1f.3 Audio device: Intel Corporation Sunrise Point-LP HD Audio (rev 21)
        Subsystem: Hewlett-Packard Company Sunrise Point-LP HD Audio
        Kernel driver in use: snd_hda_intel
        Kernel modules: snd_hda_intel, snd_soc_skl
    00:1f.4 SMBus: Intel Corporation Sunrise Point-LP SMBus (rev 21)
        Subsystem: Hewlett-Packard Company Sunrise Point-LP SMBus
        Kernel driver in use: i801_smbus
    00:1f.6 Ethernet controller: Intel Corporation Ethernet Connection (4) I219-V (rev 21)
        Subsystem: Hewlett-Packard Company Ethernet Connection (4) I219-V
        Kernel driver in use: e1000e
    01:00.0 Network controller: Intel Corporation Wireless 8265 / 8275 (rev 78)
        Subsystem: Intel Corporation Wireless 8265 / 8275
        Kernel driver in use: iwlwifi
        Kernel modules: iwlwifi
    3b:00.0 Non-Volatile memory controller: Samsung Electronics Co Ltd Device a808
        Subsystem: Samsung Electronics Co Ltd Device a801
        Kernel driver in use: nvme
        Kernel modules: nvme

### [lsusb]

`root `[`#`]`lsusb `

    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 004: ID 05c8:0808 Cheng Uei Precision Industry Co., Ltd (Foxlink)
    Bus 001 Device 003: ID 138a:00ab Validity Sensors, Inc.
    Bus 001 Device 002: ID 8087:0a2b Intel Corp.
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

### [Keyboard]

The keyboard has the following special keys:

-   [F1] triggers the display settings
-   [F2] does nothing
-   [F3] decreases the display brightness
-   [F4] increases the display brightness
-   [F5] mutes/unmutes the volume.

** Tip**\
In order to make the mute LED working, make sure to install the required kernel modules along with ALSA/PulseAudio, and to add the following to [/etc/modprobe.d/alsa.conf]

[FILE] **`/etc/modprobe.d/alsa.conf`**

    ...
    options snd-hda-intel model=mute-led-gpio

This also allows the microphone mute LED (on [F8]) to work whenever you mute/unmute the microphone. If the mute LED is still not working, run [alsamixer] and make sure that `Mute-LED mode` is set to `Follow Master`.

-   [F6] decreases the volume
-   [F7] increases the volume
-   [F8] mutes/unmutes the microphone
-   [F9] toggles the keyboard backlight and its intensity
-   [F10] does nothing
-   [F11] toggles Wi-Fi status

** Note**\
You need to build `CONFIG_IWLWIFI` **and** `CONFIG_HP_WIRELESS` as kernel modules (or built-in) in order for the button to correctly work. As of now, the wireless LED stays on regardless of its state, I will update the section if I will manage to make this work.

-   [F12] can be bound to open the calendar

To access [F1]-[F12] you need to keep pressed the [fn] key.

** Tip**\
Hold [fn] and [Shift] to block the function keys. The LED on the [fn] key should light up.

### [Smart card reader]

In order for the smart card reader to work, install [[[dev-libs/opensc]](https://packages.gentoo.org/packages/dev-libs/opensc)[]] and [[[app-crypt/ccid]](https://packages.gentoo.org/packages/app-crypt/ccid)[]].

`root `[`#`]`emerge --ask dev-libs/opensc app-crypt/ccid`

Reboot and if you insert a smart card in the smart card reader it should be detected and a notification should appear.