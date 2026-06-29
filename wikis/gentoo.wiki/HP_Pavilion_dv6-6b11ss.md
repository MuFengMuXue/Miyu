[] The information in this article is probably **outdated**. You can help the Gentoo community by verifying and [updating this article](https://wiki.gentoo.org/index.php?title=HP_Pavilion_dv6-6b11ss&action=edit).

**Resources**

[[]][Official Support Page](https://support.hp.com/us-en/product/details/hp-pavilion-dv6-6b00-entertainment-notebook-pc-series/model/5189114)

[[]][Hardware Maintenance Manual](https://h10032.www1.hp.com/ctg/Manual/c03015537.pdf)

[[]][HP Pavilion](https://en.wikipedia.org/wiki/HP_Pavilion "wikipedia:HP Pavilion")

## Contents

-   [[1] [Hardware:]](#Hardware:)
    -   [[1.1] [Wi-Fi drivers:]](#Wi-Fi_drivers:)
    -   [[1.2] [SD card reader:]](#SD_card_reader:)
    -   [[1.3] [ACPI:]](#ACPI:)
    -   [[1.4] [HP and camera drivers:]](#HP_and_camera_drivers:)
-   [[2] [Portage:]](#Portage:)
-   [[3] [Graphics and video decoding:]](#Graphics_and_video_decoding:)
-   [[4] [Touchpad and keyboard layout config:]](#Touchpad_and_keyboard_layout_config:)

#### [Hardware:]

Printout of lspci:

`root `[`#`]`lspci`

    00:00.0 Host bridge: Intel Corporation 2nd Generation Core Processor Family DRAM Controller (rev 09)
    00:01.0 PCI bridge: Intel Corporation Xeon E3-1200/2nd Generation Core Processor Family PCI Express Root Port (rev 09)
    00:02.0 VGA compatible controller: Intel Corporation 2nd Generation Core Processor Family Integrated Graphics Controller (rev 09)
    00:16.0 Communication controller: Intel Corporation 6 Series/C200 Series Chipset Family MEI Controller #1 (rev 04)
    00:1a.0 USB controller: Intel Corporation 6 Series/C200 Series Chipset Family USB Enhanced Host Controller #2 (rev 05)
    00:1b.0 Audio device: Intel Corporation 6 Series/C200 Series Chipset Family High Definition Audio Controller (rev 05)
    00:1c.0 PCI bridge: Intel Corporation 6 Series/C200 Series Chipset Family PCI Express Root Port 1 (rev b5)
    00:1c.1 PCI bridge: Intel Corporation 6 Series/C200 Series Chipset Family PCI Express Root Port 2 (rev b5)
    00:1c.2 PCI bridge: Intel Corporation 6 Series/C200 Series Chipset Family PCI Express Root Port 3 (rev b5)
    00:1c.3 PCI bridge: Intel Corporation 6 Series/C200 Series Chipset Family PCI Express Root Port 4 (rev b5)
    00:1d.0 USB controller: Intel Corporation 6 Series/C200 Series Chipset Family USB Enhanced Host Controller #1 (rev 05)
    00:1f.0 ISA bridge: Intel Corporation HM65 Express Chipset Family LPC Controller (rev 05)
    00:1f.2 SATA controller: Intel Corporation 6 Series/C200 Series Chipset Family 6 port SATA AHCI Controller (rev 05)
    00:1f.3 SMBus: Intel Corporation 6 Series/C200 Series Chipset Family SMBus Controller (rev 05)
    01:00.0 VGA compatible controller: Advanced Micro Devices [AMD] nee ATI Caicos [Radeon HD 6400M/7400M Series]
    07:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168 PCI Express Gigabit Ethernet controller (rev 06)
    0d:00.0 Network controller: Broadcom Corporation BCM4313 802.11b/g/n Wireless LAN Controller (rev 01)
    13:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS5209 PCI Express Card Reader (rev 01)
    13:00.1 SD Host controller: Realtek Semiconductor Co., Ltd. RTS5209 PCI Express Card Reader (rev 01)
    19:00.0 USB controller: NEC Corporation uPD720200 USB 3.0 Host Controller (rev 04)

Main specifications ([full specs of the laptop](http://support.hp.com/us-en/product/HP-Pavilion-dv6-6b00-Entertainment-Notebook-PC-series/5145688/model/5189114/document/c03083240/)) :

-   **CPU**: 2.4 GHz Intel Core i5-2430M
-   **Main memory**: 6 GB DDR3
-   **Video Graphics (I)**: AMD Radeon HD 6490M (1 GB DDR5 dedicated)
-   **Video Graphics (II)**: Intel Sandy Bridge GPU
-   **Hard disk**: 500 GB SATA (5400 rpm)

##### [Wi-Fi drivers:]

Compile and install [brcmsmac driver](http://linuxwireless.org/en/users/Drivers/brcm80211) from Linux kernel.

[KERNEL]

    Device Drivers --->
      [*] Network device support --->
        [*] Wireless LAN --->
          < > Broadcom 43xx wireless support (mac80211 stack)
          < > Broadcom 43xx-legacy wireless support (mac80211 stack)
          <M> Broadcom IEEE802.11n PCIe SoftMAC WLAN driver
          < > Broadcom IEEE802.11n embedded FullMAC WLAN driver
      Broadcom specific AMBA  --->
        <M> BCMA support
        [*] Support for BCMA on PCI-host bus

And install the ebuild [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] to get the required firmware.

##### [SD card reader:]

To make sure the integrated SD card reader works fine, your kernel should have:

[KERNEL]

    Device Drivers  --->
      Multifunction device drivers  --->
        <M> Realtek PCI-E card reader
      <M> MMC/SD/SDIO card support  --->
        <M>   MMC block device driver
        <M>   Realtek PCI-E SD/MMC Card Interface Driver
      <M> Sony MemoryStick card support  --->
        <M>   Realtek PCI-E Memstick Card Interface Driver

    Bus options (PCI etc.)  --->
      <*> Support for PCI Hotplug  --->
      [*]   PCI Express Port Bus support
      [*]   PCI Express Hotplug driver
      [*]   ACPI PCI Hotplug driver

##### [ACPI:]

To setup [laptop-mode-tools](https://wiki.gentoo.org/wiki/Power_management/Guide "Power management/Guide") is recommended. Edit the [/etc/default/grub] file and add this string:

[FILE] **`/etc/default/grub`**

    GRUB_CMDLINE_LINUX_DEFAULT="acpi_backlight=vendor acpi_osi=Linux"

Next, run `grub2-mkconfig` to update your configuration from that file.

##### [HP and camera drivers:]

You can enable the following kernel options (as module o built-in):

[KERNEL]

    Device drivers --->
        [*] X86 Platform Specific Device Drivers  --->
            <*> HP laptop accelerometer
            <*> HP WMI extras
        Multimedia devices --->
          [*]   Video capture adapters --->
          [*]     V4L USB device --->
          <*>       USB Video Class (UVC)
          [*]         UVC input events device support
        [*] Hardware Monitoring support -->
            <*> STMicroeletronics LIS3* three-axis digital accelerometer

Check the webcam module is loaded:

`user `[`$`]`dmesg | grep uvc`

    uvcvideo: Found UVC 1.00 device USB2.0 UVC HP TrueVision HD (064e:d281)

Check the accelerometer sensor driver for hard disk is loaded:

`user `[`$`]`dmesg | grep Accelerometer`

    input: ST LIS3LV02DL Accelerometer as /devices/platform/lis3lv02d/input/input17

You can test the sensor by moving your laptop and checking the output of this command:

    watch -n 1 'cat /sys/devices/platform/lis3lv02d/position'

See [HPfall](https://wiki.gentoo.org/wiki/HPfall "HPfall") for more information about hard disk protection.

#### [Portage:]

Some values to config portage for this laptop:

[FILE] **`/etc/portage/make.conf`**

    CFLAGS="-march=corei7-avx -O2 -pipe"

[FILE] **`/etc/portage/package.use/00grub`**

    */* GRUB_PLATFORMS: pc

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* intel i915 radeon

[FILE] **`/etc/portage/package.use/00cpu-flags`**

    */* CPU_FLAGS_X86: mmx mmxext sse sse2 sse3 ssse3 sse4 sse4a sse4_1 sse4_2

#### [Graphics and video decoding:]

The laptop includes an [Intel Sandy Bridge integrated GPU](https://wiki.gentoo.org/wiki/Intel "Intel") that supports VA API and works with intel opensource driver and AMD 6490M discrete GPU that works with [radeon](https://wiki.gentoo.org/wiki/Radeon "Radeon"). Sadly, VA API standard is not recognize for many applications, but you can install the great [libvdpau-va-gl library](https://github.com/i-rinat/libvdpau-va-gl) from [several overlays](http://gpo.zugaina.org/x11-libs/libvdpau-va-gl) to get the video decoding by hardware works for VDPAU, a standard more extended. Currently (end-2013) [Mozilla Firefox doesn\'t support](https://support.mozilla.org/en-US/questions/971722) a way to configure its gstreamer-backend to use VA API. See this blog entry: [VA API Backend for VDPAU](http://davidrosca.blogspot.com.es/2013/05/va-api-backend-for-vdpau.html)

For basic usage, intel driver works fine. Portage configuration:

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: intel i915

Useful links:

-   [Using vga_switcheroo (Ubuntu Wiki)](https://help.ubuntu.com/community/HybridGraphics#Using_vga_switcheroo)
-   [PRIME (ArchLinux Wiki)](https://wiki.archlinux.org/index.php/PRIME)
-   [ATI/AMD on Linux (ArchLinux Wiki)](https://wiki.archlinux.org/index.php/ATI)

#### [Touchpad and keyboard layout config:]

Make a [/etc/X11/xorg.conf.d/20-input.conf] to config the synaptics touchpad and keyboard layout (in my case, Spanish)

[FILE] **`/etc/X11/xorg.conf.d/20-input.conf`**

    # Xorg configuration: mouse
    Section "InputClass"
        Identifier   "MyTouchpad"
        MatchIsTouchpad   "on"
        MatchDevicePath   "/dev/input/event*"
        Driver      "synaptics"
            Option      "TapButton1" "1"
            Option      "VertEdgeScroll" "true"
            Option      "HorizEdgeScroll" "true"
            Option      "RTCornerButton" "3"
            Option      "RBCornerButton" "2"
            Option      "MaxTapMove" "131"
            Option      "EmulateTwoFingerMinZ" "24"
            option      "EmulateTwoFingerMinW" "9"
            Option      "VertTwoFingerScroll" "on"
    EndSection
    Section "InputClass"
        Identifier "mykeyboard"
        Driver "evdev"
        Option "XkbLayout" "es"
        MatchIsKeyboard "on"
    EndSection
    Section "InputClass"
      Identifier "touchpad catchall"
      MatchIsTouchpad "on"
          Option "TapButton1" "1"
          Option "TapButton2" "2"
          Option "TapButton3" "3"
    EndSection