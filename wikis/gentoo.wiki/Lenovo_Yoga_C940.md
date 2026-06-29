[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Lenovo_Yoga#Yoga_900 "wikipedia:Lenovo Yoga")

Still working on installation, wiki will come soon.

## Contents

-   [[1] [Hardware Lenovo Yoga C940]](#Hardware_Lenovo_Yoga_C940)
    -   [[1.1] [Laptop Specifications]](#Laptop_Specifications)
-   [[2] [Configuration details]](#Configuration_details)
    -   [[2.1] [Host bridge]](#Host_bridge)
    -   [[2.2] [Graphics]](#Graphics)
    -   [[2.3] [PCIe bus]](#PCIe_bus)
    -   [[2.4] [USB Bus]](#USB_Bus)
    -   [[2.5] [Thunderbolt]](#Thunderbolt)
    -   [[2.6] [NVMe SSD]](#NVMe_SSD)
    -   [[2.7] [Display]](#Display)
    -   [[2.8] [Wireless]](#Wireless)
    -   [[2.9] [Audio]](#Audio)
    -   [[2.10] [bluetooth]](#bluetooth)
    -   [[2.11] [misc]](#misc)
    -   [[2.12] [Touchpad and TouchScreen]](#Touchpad_and_TouchScreen)
    -   [[2.13] [webcam]](#webcam)
    -   [[2.14] [driver summary]](#driver_summary)
-   [[3] [Problems & Workarounds]](#Problems_.26_Workarounds)
    -   [[3.1] [Thermal shutdowns]](#Thermal_shutdowns)
    -   [[3.2] [HiDPI]](#HiDPI)
    -   [[3.3] [Screen rotation]](#Screen_rotation)
    -   [[3.4] [Sounds]](#Sounds)
    -   [[3.5] [Automatic screen rotation]](#Automatic_screen_rotation)
-   [[4] [External resources]](#External_resources)

## [Hardware Lenovo Yoga C940]

on linux-5.7.5 kernel

### [Laptop Specifications]

  ----------------- ----------------------------------------------------------------------------------- ------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
       Device                                              Model                                         Works                                                                                        Notes
   Intel® Core™ i7                          Intel Core i7-1065G7 CPU @ 1.30GHz                            Yes
      Graphics                                    Intel® HD Iris Plus G7                                  Yes
       Screen                              13.3\", 3840×2160, 16:9 aspect ratio                           Yes
      WiFi card      Intel Corporation Killer Wi-Fi 6 AX1650i 160MHz Wireless Network Adapter (201NGW)    Yes
      Bluetooth                                                                                           Yes
        Audio                         Lenovo Smart Sound Technology Audio Controller                      Yes    Needs a BIOS update as documented in [linux#205755](https://bugzilla.kernel.org/show_bug.cgi?id=205755#c59), and possibly gentoo-sources≥5.10.10
       Camera                                                                                             Yes
     Touchscreen                                  Wacom tablet with a Pen                                 Yes                                                                                     multitouch ok
      Touchpad                                                                                            Yes                                            multitouch support: two finger scrolling: ok, tap click & tap drag: ok, left and right click: ok
  ----------------- ----------------------------------------------------------------------------------- ------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [Configuration details]

### [Host bridge]

`root `[`#`]`lspci -nn -k`

    00:00.0 Host bridge [0600]: Intel Corporation Device [8086:8a12] (rev 03)
            Subsystem: Lenovo Device [17aa:3801]
            Kernel driver in use: icl_uncore

[KERNEL]

    .config - Linux/x86 4.9.95-gentoo Kernel Configuration
     →

### [Graphics]

Works using x11-drivers/xf86-video-intel with VIDEO_CARDS=\"intel i965 iris\".

See [Intel](https://wiki.gentoo.org/wiki/Intel "Intel").

### [PCIe bus]

`root `[`#`]`lspci -nn -k`

    00:07.0 PCI bridge [0604]: Intel Corporation Ice Lake Thunderbolt 3 PCI Express Root Port #0 [8086:8a1d] (rev 03)
            Kernel driver in use: pcieport
    00:07.1 PCI bridge [0604]: Intel Corporation Ice Lake Thunderbolt 3 PCI Express Root Port #1 [8086:8a1f] (rev 03)
            Kernel driver in use: pcieport

### [USB Bus]

`root `[`#`]`lspci -nn -k`

00:0d.0 USB controller \[0c03\]: Intel Corporation Ice Lake Thunderbolt 3 USB Controller \[8086:8a13\] (rev 03)

           Subsystem: Lenovo Ice Lake Thunderbolt 3 USB Controller [17aa:380a]

Kernel driver in use: xhci_hcd

### [Thunderbolt]

`root `[`#`]`lspci -nn -k`

00:0d.2 System peripheral \[0880\]: Intel Corporation Ice Lake Thunderbolt 3 NHI #0 \[8086:8a17\] (rev 03)

           Kernel driver in use: thunderbolt

Kernel modules: thunderbolt

### [NVMe SSD]

`root `[`#`]`lspci -nn -k`

55:00.0 Non-Volatile memory controller \[0108\]: Samsung Electronics Co Ltd NVMe SSD Controller SM981/PM981/PM983 \[144d:a808\]

           Subsystem: Samsung Electronics Co Ltd NVMe SSD Controller SM981/PM981/PM983 [144d:a801]

Kernel driver in use: nvme

### [Display]

Worked out-of-the box in X.

### [Wireless]

`root `[`#`]`lspci -nn -k`

00:14.3 Network controller \[0280\]: Intel Corporation Killer Wi-Fi 6 AX1650i 160MHz Wireless Network Adapter (201NGW) \[8086:34f0\] (rev 30)

           Subsystem: Intel Corporation Killer Wi-Fi 6 AX1650i 160MHz Wireless Network Adapter (201NGW) [8086:0074]

Kernel driver in use: iwlwifi

### [Audio]

`root `[`#`]`lspci -nn -k`

00:1f.3 Multimedia audio controller \[0401\]: Intel Corporation Smart Sound Technology Audio Controller \[8086:34c8\] (rev 30)

           Subsystem: Lenovo Smart Sound Technology Audio Controller [17aa:382e]
           Kernel driver in use: sof-audio-pci

Kernel modules: snd_hda_intel, snd_sof_pci

### [bluetooth]

`root `[`#`]`lsusb -t`

    /:  Bus 03.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/12p, 480M
        |__ Port 10: Dev 7, If 0, Class=Wireless, Driver=btusb, 12M
        |__ Port 10: Dev 7, If 1, Class=Wireless, Driver=btusb, 12M

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

Could pair with a bluetooth headset

[Bluetooth](https://wiki.gentoo.org/wiki/Bluetooth "Bluetooth") --- describes the configuration and usage of Bluetooth controllers and devices.

### [misc]

`root `[`#`]`lspci -nn -k`

    00:04.0 Signal processing controller [1180]: Intel Corporation Device [8086:8a03] (rev 03)
            Subsystem: Lenovo Device [17aa:3802]
            Kernel driver in use: proc_thermal
            Kernel modules: processor_thermal_device
    00:12.0 Serial controller [0700]: Intel Corporation Device [8086:34fc] (rev 30)
            Subsystem: Lenovo Device [17aa:384d]
            Kernel driver in use: intel_ish_ipc
            Kernel modules: intel_ish_ipc
    00:14.2 RAM memory [0500]: Intel Corporation Device [8086:34ef] (rev 30)
            Subsystem: Lenovo Device [17aa:3846]
    00:16.0 Communication controller [0780]: Intel Corporation Management Engine Interface [8086:34e0] (rev 30)
            Subsystem: Lenovo Management Engine Interface [17aa:383a]
            Kernel driver in use: mei_me
    00:1f.0 ISA bridge [0601]: Intel Corporation Ice Lake-LP LPC Controller [8086:3482] (rev 30)
            Subsystem: Lenovo Ice Lake-LP LPC Controller [17aa:380e]
    00:1f.4 SMBus [0c05]: Intel Corporation Ice Lake-LP SMBus Controller [8086:34a3] (rev 30)
            Subsystem: Lenovo Ice Lake-LP SMBus Controller [17aa:3811]
            Kernel driver in use: i801_smbus
            Kernel modules: i2c_i801
    00:1f.5 Serial bus controller [0c80]: Intel Corporation Ice Lake-LP SPI Controller [8086:34a4] (rev 30)
            Subsystem: Lenovo Ice Lake-LP SPI Controller [17aa:3812]

** Note**\
[https://www.kernel.org/doc/Documentation/misc-devices/mei/mei.txt](https://www.kernel.org/doc/Documentation/misc-devices/mei/mei.txt) Intel Management Engine (Intel ME) is an isolated and protected computing resource (Co-processor) residing inside certain Intel chipsets.

### [Touchpad and TouchScreen]

`root `[`#`]`lspci -nn -k`

    00:15.0 Serial bus controller [0c80]: Intel Corporation Ice Lake-LP Serial IO I2C Controller #0 [8086:34e8] (rev 30)
            Subsystem: Lenovo Ice Lake-LP Serial IO I2C Controller [17aa:3840]
            Kernel driver in use: intel-lpss
            Kernel modules: intel_lpss_pci
    00:15.1 Serial bus controller [0c80]: Intel Corporation Ice Lake-LP Serial IO I2C Controller #1 [8086:34e9] (rev 30)
            Subsystem: Lenovo Ice Lake-LP Serial IO I2C Controller [17aa:3841]
            Kernel driver in use: intel-lpss
            Kernel modules: intel_lpss_pci
    00:15.2 Serial bus controller [0c80]: Intel Corporation Ice Lake-LP Serial IO I2C Controller #2 [8086:34ea] (rev 30)
            Subsystem: Lenovo Ice Lake-LP Serial IO I2C Controller [17aa:3842]
            Kernel driver in use: intel-lpss
            Kernel modules: intel_lpss_pci

### [webcam]

** Note**\
todo

### [driver summary]

** Note**\
todo

## [][Problems & Workarounds]

### [Thermal shutdowns]

It seems that one temperature sensor is not taken into account properly when throttling the CPU. This leads to frequent thermal shutdowns when under high load, especially when the battery is being charged.

Solution for now:

1.  Install [[[sys-power/thermald]](https://packages.gentoo.org/packages/sys-power/thermald)[]] and add it to the default runlevel
2.  Put the following custom configuration into [/etc/thermald/thermald-conf.xml]

[FILE] **`/etc/thermald/thermald-conf.xml`**

    <?xml version="1.0"?>
    <ThermalConfiguration>
    <Platform>
            <Name> Auto generated </Name>
            <ProductName>81Q9</ProductName>
            <Preference>QUIET</Preference>
            <PPCC>
                    <PowerLimitIndex>0</PowerLimitIndex>
                    <PowerLimitMinimum>12000</PowerLimitMinimum>
                    <PowerLimitMaximum>23000</PowerLimitMaximum>
                    <TimeWindowMinimum>28000</TimeWindowMinimum>
                    <TimeWindowMaximum>32000</TimeWindowMaximum>
                    <StepSize>500</StepSize>
            </PPCC>
            <ThermalZones>
                    <ThermalZone>
                            <Type>auto_zone_0</Type>
                            <TripPoints>
                                    <TripPoint>
                                            <SensorType>SEN2</SensorType>
                                            <Temperature>63000</Temperature>
                                            <Type>Passive</Type>
                                            <CoolingDevice>
                                                    <Type>B0D4</Type>
                                                    <SamplingPeriod>8</SamplingPeriod>
                                                    <TargetState>2147483647</TargetState>
                                            </CoolingDevice>
                                    </TripPoint>
                                    <TripPoint>
                                            <SensorType>SEN2</SensorType>
                                            <Temperature>64000</Temperature>
                                            <Type>Passive</Type>
                                            <CoolingDevice>
                                                    <Type>B0D4</Type>
                                                    <SamplingPeriod>8</SamplingPeriod>
                                            </CoolingDevice>
                                    </TripPoint>
                                    <TripPoint>
                                            <SensorType>SEN4</SensorType>
                                            <Temperature>74000</Temperature>
                                            <Type>Passive</Type>
                                            <CoolingDevice>
                                                    <Type>B0D4</Type>
                                                    <SamplingPeriod>8</SamplingPeriod>
                                            </CoolingDevice>
                                    </TripPoint>
                            </TripPoints>
                    </ThermalZone>
            </ThermalZones>
    </Platform>
    </ThermalConfiguration>

This is the configuration provided by the firmware plus an entry for SEN4 which is responsible for most of the shutdowns on my system.

### [HiDPI]

Set global scaling in your desktop configuration. For KDE this can be found right below the display configuration.

With X it was impossible to have different scaling factors per monitor, which makes external monitors hard to use unless they have similar resolution.

I have a somewhat working setup now with Plasma 5.19 / KDE 20.04 and wayland.

\

### [Screen rotation]

Seems to be unstable with Plasma 5.19.

\

### [Sounds]

Out of the box only the sound bar works (fixed by the BIOS update below). Some users have reported additional issues:

-   Sound doesn't work entirely. → This is usually an issue with the kernel configuration and missing modules.
-   The headphone jack doesn't deliver bass (as [reported in the sof-project](https://github.com/thesofproject/linux/issues/2375)). This is also fixed by the BIOS update below.

As of February 2021 there is a patched BIOS image (customized version 57 provided by Lenovo staff) that fixes the issue with the speakers. Check out [kernel bug comments](https://bugzilla.kernel.org/show_bug.cgi?id=205755#c59) and [Lenovo forum thread](https://forums.lenovo.com/t5/Other-Linux-Discussions/Yoga-C930-audio-on-Linux/m-p/5042057) for details and instructions.

After the BIOS upgrade audio has been confirmed to work on recent Gentoo using 5.10.10+ kernel version (this author used 5.10.10 and no special settings).

### [Automatic screen rotation]

Didn't look into it yet.

## [External resources]

-   [https://wiki.archlinux.org/title/Lenovo_Yoga_C940](https://wiki.archlinux.org/title/Lenovo_Yoga_C940)