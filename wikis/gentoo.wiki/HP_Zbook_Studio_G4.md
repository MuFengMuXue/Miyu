[] The information in this article is probably **outdated**. You can help the Gentoo community by verifying and [updating this article](https://wiki.gentoo.org/index.php?title=HP_Zbook_Studio_G4&action=edit).

**Resources**

[[]][Official Support Page](https://support.hp.com/us-en/product/details/hp-zbook-studio-g4-mobile-workstation/14840026)

[[]][Specifications](https://support.hp.com/us-en/document/c05490369)

[[]][Hardware Maintenance Manual](https://h10032.www1.hp.com/ctg/Manual/c05481588.pdf)

[[]][User Guide](https://h10032.www1.hp.com/ctg/Manual/c05478227.pdf)

[[]][Wikipedia](https://en.wikipedia.org/wiki/HP_ZBook "wikipedia:HP ZBook")

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Sound card]](#Sound_card)
    -   [[1.2] [Thunderbolt 3]](#Thunderbolt_3)
    -   [[1.3] [USB]](#USB)
    -   [[1.4] [WiFi]](#WiFi)
        -   [[1.4.1] [Hardware WiFi button]](#Hardware_WiFi_button)
    -   [[1.5] [SD card slot]](#SD_card_slot)
    -   [[1.6] [Webcam]](#Webcam)
    -   [[1.7] [Video]](#Video)
        -   [[1.7.1] [NVIDIA Optimus]](#NVIDIA_Optimus)
        -   [[1.7.2] [Intel]](#Intel)
        -   [[1.7.3] [NVIDIA]](#NVIDIA)
    -   [[1.8] [Bluetooth]](#Bluetooth)
    -   [[1.9] [HP 3D Driveguard]](#HP_3D_Driveguard)
-   [[2] [Troubleshooting]](#Troubleshooting)
    -   [[2.1] [External DisplayPort monitor does not work on PCIe(Thunderbolt 3) port]](#External_DisplayPort_monitor_does_not_work_on_PCIe.28Thunderbolt_3.29_port)
    -   [[2.2] [NVIDIA brightness control]](#NVIDIA_brightness_control)
    -   [[2.3] [Screen tearing]](#Screen_tearing)
    -   [[2.4] [Keyboard layout]](#Keyboard_layout)
        -   [[2.4.1] [tty]](#tty)
        -   [[2.4.2] [Graphical]](#Graphical)
    -   [[2.5] [Unable to suspend with Nvidia driver]](#Unable_to_suspend_with_Nvidia_driver)
-   [[3] [References]](#References)

## [Hardware]

`root `[`#`]`lspci -k`

    00:00.0 Host bridge: Intel Corporation Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers (rev 05)
        Subsystem: Hewlett-Packard Company Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers
        Kernel driver in use: skl_uncore
    00:02.0 VGA compatible controller: Intel Corporation HD Graphics 630 (rev 04)
        DeviceName: Onboard IGD
        Subsystem: Hewlett-Packard Company HD Graphics 630
        Kernel driver in use: i915
    00:04.0 Signal processing controller: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem (rev 05)
        Subsystem: Hewlett-Packard Company Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem
    00:14.0 USB controller: Intel Corporation 100 Series/C230 Series Chipset Family USB 3.0 xHCI Controller (rev 31)
        Subsystem: Hewlett-Packard Company 100 Series/C230 Series Chipset Family USB 3.0 xHCI Controller
        Kernel driver in use: xhci_hcd
    00:14.2 Signal processing controller: Intel Corporation 100 Series/C230 Series Chipset Family Thermal Subsystem (rev 31)
        Subsystem: Hewlett-Packard Company 100 Series/C230 Series Chipset Family Thermal Subsystem
        Kernel driver in use: intel_pch_thermal
        Kernel modules: intel_pch_thermal
    00:15.0 Signal processing controller: Intel Corporation 100 Series/C230 Series Chipset Family Serial IO I2C Controller #0 (rev 31)
        Subsystem: Hewlett-Packard Company 100 Series/C230 Series Chipset Family Serial IO I2C Controller
    00:16.0 Communication controller: Intel Corporation 100 Series/C230 Series Chipset Family MEI Controller #1 (rev 31)
        Subsystem: Hewlett-Packard Company 100 Series/C230 Series Chipset Family MEI Controller
    00:17.0 SATA controller: Intel Corporation Q170/Q150/B150/H170/H110/Z170/CM236 Chipset SATA Controller [AHCI Mode] (rev 31)
        Subsystem: Hewlett-Packard Company Q170/Q150/B150/H170/H110/Z170/CM236 Chipset SATA Controller [AHCI Mode]
        Kernel driver in use: ahci
    00:1b.0 PCI bridge: Intel Corporation 100 Series/C230 Series Chipset Family PCI Express Root Port #17 (rev f1)
        Kernel driver in use: pcieport
    00:1c.0 PCI bridge: Intel Corporation 100 Series/C230 Series Chipset Family PCI Express Root Port #1 (rev f1)
        Kernel driver in use: pcieport
    00:1c.1 PCI bridge: Intel Corporation 100 Series/C230 Series Chipset Family PCI Express Root Port #2 (rev f1)
        Kernel driver in use: pcieport
    00:1c.4 PCI bridge: Intel Corporation 100 Series/C230 Series Chipset Family PCI Express Root Port #5 (rev f1)
        Kernel driver in use: pcieport
    00:1d.0 PCI bridge: Intel Corporation 100 Series/C230 Series Chipset Family PCI Express Root Port #9 (rev f1)
        Kernel driver in use: pcieport
    00:1f.0 ISA bridge: Intel Corporation CM238 Chipset LPC/eSPI Controller (rev 31)
        Subsystem: Hewlett-Packard Company CM238 Chipset LPC/eSPI Controller
    00:1f.2 Memory controller: Intel Corporation 100 Series/C230 Series Chipset Family Power Management Controller (rev 31)
        Subsystem: Hewlett-Packard Company 100 Series/C230 Series Chipset Family Power Management Controller
    00:1f.3 Audio device: Intel Corporation CM238 HD Audio Controller (rev 31)
        Subsystem: Hewlett-Packard Company CM238 HD Audio Controller
        Kernel driver in use: snd_hda_intel
    00:1f.4 SMBus: Intel Corporation 100 Series/C230 Series Chipset Family SMBus (rev 31)
        Subsystem: Hewlett-Packard Company 100 Series/C230 Series Chipset Family SMBus
        Kernel driver in use: i801_smbus
    00:1f.6 Ethernet controller: Intel Corporation Ethernet Connection (2) I219-LM (rev 31)
        Subsystem: Hewlett-Packard Company Ethernet Connection (2) I219-LM
        Kernel driver in use: e1000e
    01:00.0 VGA compatible controller: NVIDIA Corporation GM107GLM [Quadro M1200 Mobile] (rev a2)
            Subsystem: Hewlett-Packard Company GM107GLM [Quadro M1200 Mobile]
            Kernel driver in use: nvidia
            Kernel modules: nvidia_drm, nvidia
    02:00.0 Network controller: Intel Corporation Wireless 8265 / 8275 (rev 78)
        Subsystem: Intel Corporation Dual Band Wireless-AC 8265
        Kernel driver in use: iwlwifi
    03:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS525A PCI Express Card Reader (rev 01)
        Subsystem: Hewlett-Packard Company RTS525A PCI Express Card Reader
        Kernel driver in use: rtsx_pci
    6f:00.0 Non-Volatile memory controller: Samsung Electronics Co Ltd NVMe SSD Controller SM961/PM961
        Subsystem: Samsung Electronics Co Ltd NVMe SSD Controller SM961/PM961
        Kernel driver in use: nvme

  --------------- ------------------------------------------------------------ ---------------------- ------------------
  Device          Make/model                                                   Status                 Kernel driver(s)
  CPU             Intel Core i7-7700HQ                                         Works                  N/A
  Ethernet        Intel Corporation Ethernet Connection I219-LM                Works                  e1000e
  USB             Intel Corporation Sunrise Point-H USB 3.0 xHCI Controller    Works                  xhci_hcd
  Video card      Intel Corporation HD Graphics 630                            Works                  i915
  Video card      NVIDIA Quadro M1200                                          Works                  nvidia
  WiFi            Intel Corporation Wireless 8265 / 8275                       Works                  iwlwifi
  Sound card      Intel Corporation Device a171                                Works                  snd_hda_intel
  Hard drive      Samsung Electronics Co Ltd NVMe SSD Controller SM961/PM961   Works                  nvme
  Bluetooth       Intel Corporation 0a2b                                       Works                  N/A
  Thunderbolt 3   Intel Corporation Sunrise Point-H PCI Express                See troubleshooting    pcieport
  SD card slot    Realtek RTS525A                                              Works                  rtsx_pci
  Webcam          HD HP Camera                                                 Works                  uvcvideo
  --------------- ------------------------------------------------------------ ---------------------- ------------------

### [Sound card]

`root `[`#`]`lspci | grep Audio `

    00:1f.3 Audio device: Intel Corporation Device a171 (rev 31)

Be sure to enable [HD Audio PCI] (snd-hda-intel) and enable the codecs.

[KERNEL]

    Device Drivers --->
        <*> Sound card support
            <*> Advanced Linux Sound Architecture --->
                HD-Audio  --->
                    <*> HD Audio PCI
                    [*] Build Realtek HD-audio codec support
                    [*] ...
                    [*] Build Silicon Labs 3054 HD-modem codec support
                    [*] Enable generic HD-audio codec parser
    General setup --->
        [*] System V IPC

### [Thunderbolt 3]

Thunderbolt 3 is a hot pluggable PCIe port, with USB 3.1 support.

[KERNEL] **Thunderbolt 3 Support**

    Bus options (PCI etc.)  --->
        [*] PCI support
        [*]   PCI Express Port Bus support
        [*]     PCI Express Hotplug driver
        [*] Support for PCI Hotplug  --->
        [*]   ACPI PCI Hotplug driver

### [USB]

Easy, just enable xHCI.

[KERNEL]

    Device Drivers  --->
        [*] USB support  --->
            <*>     xHCI HCD (USB 3.0) support

No need to enable EHCI or OHCI. xHCI is backwards compatible already.

### [WiFi]

`root `[`#`]`lspci | grep Network`

    02:00.0 Network controller: Intel Corporation Wireless 8265 / 8275 (rev 78)

Intel Corporation Wireless 8265 / 8275 does not work out of the box.\
Look for the iwlwifi firmware in the [/lib/firmware] directory.

`user `[`$`]`ls /lib/firmware | grep iwlwifi-8265`

    iwlwifi-8265-21.ucode
    iwlwifi-8265-22.ucode
    iwlwifi-8265-27.ucode
    ...

** Note**\
If the output is empty, install [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] or download the driver from [here](https://wireless.wiki.kernel.org/en/users/drivers/iwlwifi)

** Warning**\
Some had problems connecting to a 5GHz network with [iwlwifi-8265-27.ucode] firmware.^[\[1\]](#cite_note-1)^

For more information on iwlwifi configuration, see [the iwlwifi wiki](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi").

[KERNEL] **Enable iwlwifi in kernel 5.4.80-gentoo-r1**

    [*] Networking support  --->
        -*- Wireless  --->
            <*>   cfg80211 - wireless configuration API
            [*]     enable powersave by default
            <*>   Generic IEEE 802.11 Networking Stack (mac80211)
    Device Drivers  --->
        Generic Driver Options  --->
            Firmware loader --->
                (iwlwifi-8265-36.ucode) External blobs to build into the kernel binary
                (/lib/firmware) Firmware blobs root directory
        [*] Network device support  --->
            [*]   Wireless LAN  --->
                [*]   Intel devices
                <*>     Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)
                <*>       Intel Wireless WiFi MVM Firmware support

No need to enable DVM, 8265 uses [iwlmvm](https://wireless.wiki.kernel.org/en/users/drivers/iwlwifi#firmware):

[KERNEL]

    < >       Intel Wireless WiFi DVM Firmware support

#### [Hardware WiFi button]

To enable the Hardware WiFi button:

[KERNEL]

    Device Drivers --->
        [*] X86 Platform Specific Device Drivers --->
            <M> HP wireless button

If the wireless button does not work, check the iwlwifi ucode version.

### [SD card slot]

To enable the PCIe Card Reader:

[KERNEL] **Kernel version \<4.16**

    Device Drivers --->
        Multifunction device drivers --->
            <*> Realtek PCI-E card reader
        <*> MMC/SD/SDIO card support --->
            <*> Realtek PCI-E SD/MMC Card Interface Driver

[KERNEL] **Kernel version \>4.16**

    Device Drivers --->
        Misc devices --->
            <*> Realtek PCI-E card reader

### [Webcam]

Setting the following kernel parameters should be enough to be able to use the built-in webcam.

[KERNEL] **Kernel version 4.19.97**

    Device Drivers --->
        [M] Multimedia support --->
            [*] Media USB Adapters --->
                [M] USB Video Class (UVC)

### [Video]

#### [NVIDIA Optimus]

Configure according to [NVIDIA/Optimus](https://wiki.gentoo.org/wiki/NVIDIA/Optimus "NVIDIA/Optimus") & the [NVIDIA/nvidia-drivers](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers "NVIDIA/nvidia-drivers") articles.\

** Note**\
There is no need to add [nvidia] to the [VIDEO_CARDS] variable in [/etc/portage/package.use]

This is the necessary Xorg configuration:

[FILE] **`/etc/X11/xorg.conf.d/20-nvidia.conf`**

    Section "Module"
        Load "modesetting"
    EndSection

    Section "Device"
        Identifier "nvidia"
        Driver "nvidia"
        BusID "01:00:0"
        Option "AllowEmptyInitialConfiguration"
    EndSection

Be sure to switch the OpenGL drivers before starting X:

`root `[`#`]`eselect opengl set nvidia`

#### [Intel]

See the [intel](https://wiki.gentoo.org/wiki/Intel "Intel") page for up-to-date kernel parameter instructions.\
Configure Xorg to use `intel` driver.

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* intel i915

Rebuild changed packages.

`root `[`#`]`emerge -DaquN @world`

Emerge the dated Intel HD Graphics driver.

`root `[`#`]`emerge -qan x11-drivers/xf86-video-intel`

Configure Xorg file.

[FILE] **`/etc/X11/xorg.conf.d/10-intel.conf`**

    Section "Device"
        Identifier "intel"
        Driver "intel"
    EndSection

** Warning**\
Be sure to keep the [/etc/X11/xorg.conf.d/] directory clean! Do not have a configuration file for NVIDIA optimus & Intel HD Graphics

#### [NVIDIA]

First off, add `nvidia` to `VIDEO_CARDS` in [/etc/portage/package.use]

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* intel i915 nvidia

Update influenced packages

`root `[`#`]`emerge -DaquN @world`

Follow the [NVIDIA guide](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers "NVIDIA/nvidia-drivers") for a (mostly) complete configuration.

** Important**\
Disable all Framebuffer devices except the EFI framebuffer. Others may interfere with the boot process, in which you\'ll may experience a boot freeze.^[\[2\]](#cite_note-2)^.

** Note**\
If you experience a GRUB freeze on boot, try rebooting using [ctrl]+[alt]+[del] and select `UMA Graphics` or `Hybrid Graphics` in the BIOS

Set the following kernel parameters to be able to use `Discrete Graphics`

[KERNEL] **Linux 4.9.76-gentoo-r1**

    Device Drivers --->
        Graphics support --->
            Frame buffer Devices --->
                -*- Support for frame buffer devices --->
                [*] EFI-based Framebuffer Support

The following configuration enables brightness control, forces full composition pipeline to decrease screen tearing and forces a dpi of 96, which could otherwise give problems in your [wm](https://wiki.gentoo.org/wiki/Window_manager "Window manager") with varying glyph sizes.

[FILE] **`/etc/X11/xorg.conf.d/10-nvidia.conf`**

    Section "Device"
        Identifier "nvidia"
        Driver "nvidia"
        Option "RegistryDwords" "EnableBrightnessControls=1"
    EndSection

    Section "Screen"
        Identifier "Screen0"
        Device "nvidia card"
        Monitor "Monitor0"
        Option "metamodes" "nvidia-auto-select +0+0 "
    EndSection

    Section "Monitor"
        Identifier "Monitor0"
        Option "DPI" "96 x 96"
    EndSection

### [Bluetooth]

Follow the [Bluetooth article](https://wiki.gentoo.org/wiki/Bluetooth "Bluetooth") on configuring and using Bluetooth.

### [HP 3D Driveguard]

HP 3D Driveguard is a feature of HP laptops that turn off the hard drive when the laptop is falling. To enable HP 3D Driveguard, follow the instructions of the [HPfall](https://wiki.gentoo.org/wiki/HPfall "HPfall") article.

## [Troubleshooting]

### [][External DisplayPort monitor does not work on PCIe(Thunderbolt 3) port]

When using an adapter to connect a DisplayPort monitor to the PCIe port and the monitor does not get recognized, try:

1.  Make sure the adapter is not plugged into the PCIe port;
2.  Disconnect the DisplayPort cable from the adapter;
3.  Plug the adapter into the PCIe port;
4.  Connect the DisplayPort cable.

Now it should work!

### [NVIDIA brightness control]

To enable brightness control, add this line to the conf file

[FILE] **`/etc/X11/xorg.conf.d/10-nvidia.conf`**

    Section "Device"
        ...
        Option "RegistryDwords" "EnableBrightnessControl=1"
    EndSection

### [Screen tearing]

As the browser is most frequently used: emerge [[[www-client/firefox]](https://packages.gentoo.org/packages/www-client/firefox)[]] with *USE* variable `hwaccel`. It fixes 99% of smooth scrolling screen tearing. Really a game changer!

For other screen tearing problems, check out [[[x11-misc/compton]](https://packages.gentoo.org/packages/x11-misc/compton)[]].

### [Keyboard layout]

To set the keyboard layout to Dvorak Programmer

#### [tty]

For terminal:

[FILE] **`/etc/conf.d/keymaps`**

    keymap="dvorak programmer"
    ...

#### [Graphical]

For X:

[FILE] **`/etc/X11/xorg.conf.d/40-keyboard.conf`**

    Section "InputClass"
        Identifier "keyboard-all"
        Driver "evdev"
        Option "XkbLayout" "us"
        Option "XkbVariant" "dvp"
        MatchIsKeyboard "on"
    EndSection

### [Unable to suspend with Nvidia driver]

If you have trouble suspending while on `Discrete Graphics`, switch to [[[sys-auth/consolekit]](https://packages.gentoo.org/packages/sys-auth/consolekit)[]] instead of [[[sys-auth/elogind]](https://packages.gentoo.org/packages/sys-auth/elogind)[]]. This replaces **suspend** for **pm-suspend** and should fix the suspend issue. More instructions on switching at [Suspend and hibernate](https://wiki.gentoo.org/wiki/Suspend_and_hibernate "Suspend and hibernate").

## [References]

1.  [[[↑](#cite_ref-1)] [[\[1\]](https://bbs.archlinux.org/viewtopic.php?id=228653), Arch Linux forum thread about the 5GHz problem.]]
2.  [[[↑](#cite_ref-2)] [[\[2\]](https://forums.gentoo.org/viewtopic-t-989210.html), The thread explaining the boot hang using an NVIDIA GPU & the wrong kernel framebuffer configuration]]