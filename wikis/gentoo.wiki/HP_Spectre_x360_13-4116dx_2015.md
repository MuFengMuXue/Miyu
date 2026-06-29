**Resources**

[[]][Official Support Page](https://support.hp.com/us-en/product/details/hp-spectre-13-4100-x360-convertible-pc/model/11715522)

[[]][Specifications](https://support.hp.com/us-en/document/c05187562)

[[]][Hardware Maintenance Manual](https://h10032.www1.hp.com/ctg/Manual/c04807803.pdf)

[[]][User Guide](https://h10032.www1.hp.com/ctg/Manual/c04817882.pdf)

[[]][HP Spectre](https://en.wikipedia.org/wiki/HP_Spectre "wikipedia:HP Spectre")

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Firmware]](#Firmware)
    -   [[2.2] [Kernel]](#Kernel)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Unknown keys]](#Unknown_keys)
        -   [[3.1.1] [Brightness keys]](#Brightness_keys)
        -   [[3.1.2] [Tablet vs Laptop mode]](#Tablet_vs_Laptop_mode)

## [Hardware]

### [Standard]

  --------------- -------------------------------------------------------------------------- -------- ------------------------ ------------------ ---------------- -------
  Device          Make/model                                                                 Status   Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  CPU             Intel® Core™ i7-6500U                                                      Works    N/A                      N/A                4.9.10
  GPU             Intel® HD Graphics 520                                                     Works    N/A                      N/A                4.9.10
  SSD             Samsung Electronics Co Ltd Device a802 (rev 01)                            Works    N/A                      N/A                4.9.10
  Wi-Fi           Intel Corporation Wireless 7265 (rev 61)                                   Works    N/A                      N/A                4.9.10
  Bluetooth       N/A                                                                        Works    N/A                      N/A                4.9.10
  Sound           Intel Corporation Device 9d70 (rev 21)                                     Works    N/A                      N/A                4.9.10
  Card reader     Realtek Semiconductor Co., Ltd. RTS5227 PCI Express Card Reader (rev 01)   Works    N/A                      N/A                4.9.10
  Touchscreen     N/A                                                                        Works    N/A                      N/A                4.9.10
  Accelerometer   N/A                                                                        Works    N/A                      N/A                4.9.10
  --------------- -------------------------------------------------------------------------- -------- ------------------------ ------------------ ---------------- -------

## [Installation]

### [Firmware]

The wireless card requires [the external firmware](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi") ([[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]]):

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

### [Kernel]

** Tip**\
Third-party-provided [.config](https://raw.githubusercontent.com/markwkm/dotfiles/master/misc/spctrx360/linux/kernel-config-x86_64-4.9.10-gentoo-spctrx360) can be used as a template.

[KERNEL] **SSD**

    Device Drivers  --->
            <*> NVM Express block device

** Note**\
For details see [NVMe](https://wiki.gentoo.org/wiki/NVMe "NVMe").

[KERNEL] **GPU**

    Device Drivers  --->
            Graphics support  --->
                <*> /dev/agpgart (AGP Support)  --->
                    <*>   Intel 440LX/BX/GX, I8xx and E7x05 chipset support
                <*> Intel 8xx/9xx/G3x/G4x/HD Graphic

** Note**\
For details see [Intel](https://wiki.gentoo.org/wiki/Intel "Intel").

[KERNEL] **Wi-Fi**

    Device Drivers  --->
            [*] Network device support  --->
                [*]   Wireless LAN  --->
                      <M>     Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)
                      <M>       Intel Wireless WiFi MVM Firmware support

** Note**\
See the [iwlwifi](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi") article for more information as this laptop does suffer from not being able to connect to some access points without disabling 802.11n and enabling software crypto.

[KERNEL] **Sound**

    Device Drivers  --->
            <*> Sound card support  --->
                <*>   Advanced Linux Sound Architecture  --->
                      HD-Audio  --->
                          <*> HD Audio PCI
                      (2048) Pre-allocated buffer size for HD-audio driver

[KERNEL] **Bluetooth**

    -*- Networking support  --->
            <*>   Bluetooth subsystem support  --->
                      Bluetooth device drivers  --->
                      [*]   Intel AG6XX protocol support

[KERNEL] **Card reader**

    Device Drivers  --->
                Multifunction device drivers  --->
                    <*> Realtek PCI-E card reader

[KERNEL] **Touchscreen**

    Device Drivers  --->
                HID support  --->
                        Special HID drivers  --->
                            <M> HID Multitouch panels

[KERNEL] **Accelerometer**

    Device Drivers  --->
            <*> Industrial I/O support  --->
                        Accelerometers  --->
                            <*> HID Accelerometers 3D

## [Troubleshooting]

### [Unknown keys]

#### [Brightness keys]

Depending on the bios revision, the screen brightness keys may or may not be assigned to the XF86MonBrightnessUp or XF86MonBrightnessDown key symbols. Correct ACPI events can still be thrown even if the key symbols are not assigned.

The [[[x11-apps/xbacklight]](https://packages.gentoo.org/packages/x11-apps/xbacklight)[]] or [[[dev-libs/light]](https://packages.gentoo.org/packages/dev-libs/light)[]] packages provides tools for helping adjust the screen brightness.

The following messages are captured by xev ([[[x11-apps/xev]](https://packages.gentoo.org/packages/x11-apps/xev)[]]) indicating that the brightness keys are throwing key codes, if not key symbols.

This the is F2 key to decrease screen brightness:

     kernel: atkbd serio0: Unknown key pressed (translated set 2, code 0xab on isa0060/serio0).
     kernel: atkbd serio0: Use 'setkeycodes e02b <keycode>' to make it known.

\
This is from the F3 key to increase screen brightness:

     atkbd serio0: Unknown key pressed (translated set 2, code 0xab on isa0060/serio0).
     atkbd serio0: Use 'setkeycodes e02b <keycode>' to make it known.

Custom ACPI ([[[sys-power/acpid]](https://packages.gentoo.org/packages/sys-power/acpid)[]]) rules can be written to capture BRTDN and BRTUP actions. An [example](https://unix.stackexchange.com/a/427572) is given on Unix & Linux Stack Exchange.

#### [Tablet vs Laptop mode]

When opening the lid for tablet mode, the following key code is emitted:

     intel-vbtn INT33D6:00: unknown event index 0xcc
     atkbd serio0: Unknown key pressed (translated set 2, code 0xd8 on isa0060/serio0).
     atkbd serio0: Use 'setkeycodes e058 <keycode>' to make it known.

When returning to laptop mode from tablet mode, the following key code is emitted:

     intel-vbtn INT33D6:00: unknown event index 0xcd
     atkbd serio0: Unknown key pressed (translated set 2, code 0xd7 on isa0060/serio0).
     atkbd serio0: Use 'setkeycodes e057 <keycode>' to make it known.

ACPI events are also thrown in addition to the above key codes when the lid is opened far enough and closed back far enough, resp:

     video/tabletmode TBLT 0000008A 00000001
     video/tabletmode TBLT 0000008A 00000000