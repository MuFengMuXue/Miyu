**Resources**

[[]][Home](https://www.asus.com/Notebooks/Eee_PC_1225B/)

## Contents

-   [[1] [Backlight support]](#Backlight_support)
-   [[2] [USB 3.0 support]](#USB_3.0_support)
-   [[3] [802.11 WiFi]](#802.11_WiFi)
-   [[4] [Bluetooth]](#Bluetooth)
-   [[5] [Ethernet]](#Ethernet)
-   [[6] [Graphics with open-source radeon drivers]](#Graphics_with_open-source_radeon_drivers)
    -   [[6.1] [Hardware acceleration video]](#Hardware_acceleration_video)
        -   [[6.1.1] [VLC player]](#VLC_player)
-   [[7] [Audio]](#Audio)
    -   [[7.1] [ALSA configuration]](#ALSA_configuration)
-   [[8] [Memory Card Reader]](#Memory_Card_Reader)
-   [[9] [Webcam]](#Webcam)
-   [[10] [Tips and tricks]](#Tips_and_tricks)
-   [[11] [See aslo]](#See_aslo)
-   [[12] [References]](#References)

## [Backlight support]

Brightness LCD may changed by Fn+F5/Fn+F6. To support it you must config kernel

[KERNEL] **Backlight**

    Power management and ACPI options --->
      [*] ACPI (Advanced Configuration and Power Interface) Support --->
        <*> AC Adapter
        <*> Battery
        -*- Button
        -*- Video
        <*> Fan
        <*> Processor
        <*> Thermal Zone
        [*] Power Management Timer Support

This options also add other functional of your laptop.

## [USB 3.0 support]

USB 3.0 provides by ASMedia ASM1042 SuperSpeed Controller. Gentoo sources have drivers for it

[KERNEL] **USB Support**

    Device Drivers  --->
        [*] USB support  --->
            <*> Support for Host-side USB
            <M> xHCI HCD (USB 3.0) support
            <*> EHCI HCD (USB 2.0) support
            <*> UHCI HCD support (most Intel and VIA) support

** Note**\
It nessecery, that xHCI HCD support will be as module. Else USB3 ports will doesn\'t work!

## [802.11 WiFi]

WiFi is provided by Broadcom BCM4313 802.11bgn Wireless Network Adapter

[KERNEL] **WiFi Support**

    [*] Networking support  --->
        [*] Wireless  --->
            <*>   cfg80211 - wireless configuration API
            [*]     enable powersave by default
            <*>   Generic IEEE 802.11 Networking Stack (mac80211)
            [*]   Minstrel
            [*]     Minstrel 802.11n support
                  Default rate control algorithm (Minstrel)  --->
            [*]   Enable LED triggers
    Device Drivers  --->
         [*] Network device support  --->
             [*] Wireless LAN  --->
                 <M> Broadcom 43xx wireless support (mac80211 stack)
                 [*]    Support for G-PHY (802.11g) devices
                 [*]    Support for N-PHY (the main 802.11n series) devices
                 [*]    Support for LP-PHY (low-power 802.11g) devices
                 [*]    Support for HT-PHY (high throughput 802.11n) devices
                 [M]    Broadcom IEEE802.11n PCIe SoftMAC WLAN driver
            Broadcom specific AMBA --->
              BCMA support
             [*] Support for BCMA on PCI-host bus
             -*- BCMA Broadcom PCI core driver
        [*] LED Support  --->
            <*>   LED Class Support
    -*- Cryptographic API --->
        -*- AES cipher algorithms
        -*- AES cipher algorithms (x86_64)

Minstrel and its 802.11n support is a rate control algorithm^[\[1\]](#cite_note-1)^ should always be activated.^[\[2\]](#cite_note-2)^

## [Bluetooth]

Bluetooth is provided by Broadcom(?) chip.

[KERNEL] **Bluetooth support**

    [*] Networking support --->
        <*> Bluetooth subsystem support --->
            [*] Bluetooth Classic (BR/EDR) features
            <*> RFCOMM protocol support
            <*> HIDP protocol support
        [*] Bluetooth Low Energy (LE) features
            Bluetooth device drivers --->
                <*> HCI USB driver
                [*] Broadcom protocol support
                <*> HCI UART driver
                    [*] Broadcom protocol support
                <*> HCI BCM203x USB driver

## [Ethernet]

Ethernet is provided by a Realtek RTL8101E Fast Ethernet device.

[KERNEL] **Ethernet Support**

    Device Drivers  --->
        Network device support --->
          Ethernet driver support --->
            [*] Realtek devices
              <*>/<M> Realtek 8169 gigabit ethernet support

You can compile ethernet driver as module, then you must check loading this module.

## [Graphics with open-source radeon drivers]

All the necessary firmware is provided with [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] package (it is easy to emerge within a chrooted environment):

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

Kernel parameters are well described in [the article about Radeon](https://wiki.gentoo.org/wiki/Radeon#Installation "Radeon"). However the choice of firmware isn\'t that obvious. As it is supposed [here](https://forums.gentoo.org/viewtopic-t-907980.html), APU is usually detected as PALM, while in fact it is closer to SUMO. The only way out is to make the driver a module and load after the root file system is mounted:

[KERNEL] **Radeon drivers**

    Device Drivers  --->
        Graphics Support --->
            <M> ATI Radeon

This lets kernel modesetting work properly.

### [Hardware acceleration video]

[]  As of **2026-05-09**, the information in this section is probably **outdated**. You can help the Gentoo community by verifying and [updating this section](https://wiki.gentoo.org/index.php?title=ASUS_Eee_PC_1225B&action=edit).

Laptop has GPU Radeon HD6320. This card support some codecs for hardware acceleration:

-   MPEG1
-   MPEG2
-   H264
-   VC1
-   MPEG4

The GPU can decode several videos without 100% load CPU.

For support hardware acceleration you must edit your install libs and player which support VDPAU technology. Enabling USE flag `vdpau` and update world.

[FILE] **`/etc/portage/make.conf`**

    USE="... vdpau ..."

Now you can manually setup the name of back-end driver with help of VDPAU_DRIVER environment variable. To do that you need to add the following line to \~/.bashrc file (provided that Bash is the default shell of a user who is going to run graphical environment).

[FILE] **`~/.bashrc`Loged as a user who run graphical interface**

    export VDPAU_DRIVER=r600

After installation, check vdpauinfo for get info

`user `[`$`]`vdpauinfo`

    display: :0   screen: 0
    API version: 1
    Information string: G3DVL VDPAU Driver Shared Library version 1.0

    Video surface:

    name   width height types
    -------------------------------------------
    420    16384 16384  NV12 YV12
    422    16384 16384  UYVY YUYV
    444    16384 16384  Y8U8V8A8 V8U8Y8A8

    Decoder capabilities:

    name                        level macbs width height
    ----------------------------------------------------
    MPEG1                           0  9216  2048  1152
    MPEG2_SIMPLE                    3  9216  2048  1152
    MPEG2_MAIN                      3  9216  2048  1152
    H264_BASELINE                  41  9216  2048  1152
    H264_MAIN                      41  9216  2048  1152
    H264_HIGH                      41  9216  2048  1152
    VC1_SIMPLE                     --- not supported ---
    VC1_MAIN                       --- not supported ---
    VC1_ADVANCED                    4  9216  2048  1152
    MPEG4_PART2_SP                  3  9216  2048  1152
    MPEG4_PART2_ASP                 5  9216  2048  1152
    DIVX4_QMOBILE                  --- not supported ---
    DIVX4_MOBILE                   --- not supported ---
    DIVX4_HOME_THEATER             --- not supported ---
    DIVX4_HD_1080P                 --- not supported ---
    DIVX5_QMOBILE                  --- not supported ---
    DIVX5_MOBILE                   --- not supported ---
    DIVX5_HOME_THEATER             --- not supported ---
    DIVX5_HD_1080P                 --- not supported ---
    H264_CONSTRAINED_BASELINE      --- not supported ---
    H264_EXTENDED                  --- not supported ---
    H264_PROGRESSIVE_HIGH          --- not supported ---
    H264_CONSTRAINED_HIGH          --- not supported ---
    H264_HIGH_444_PREDICTIVE       --- not supported ---
    HEVC_MAIN                      --- not supported ---
    HEVC_MAIN_10                   --- not supported ---
    HEVC_MAIN_STILL                --- not supported ---
    HEVC_MAIN_12                   --- not supported ---
    HEVC_MAIN_444                  --- not supported ---

    Output surface:

    name              width height nat types
    ----------------------------------------------------
    B8G8R8A8         16384 16384    y  NV12 YV12 UYVY YUYV Y8U8V8A8 V8U8Y8A8 A4I4 I4A4 A8I8 I8A8
    R8G8B8A8         16384 16384    y  NV12 YV12 UYVY YUYV Y8U8V8A8 V8U8Y8A8 A4I4 I4A4 A8I8 I8A8
    R10G10B10A2      16384 16384    y  NV12 YV12 UYVY YUYV Y8U8V8A8 V8U8Y8A8 A4I4 I4A4 A8I8 I8A8
    B10G10R10A2      16384 16384    y  NV12 YV12 UYVY YUYV Y8U8V8A8 V8U8Y8A8 A4I4 I4A4 A8I8 I8A8

    Bitmap surface:

    name              width height
    ------------------------------
    B8G8R8A8         16384 16384
    R8G8B8A8         16384 16384
    R10G10B10A2      16384 16384
    B10G10R10A2      16384 16384
    A8               16384 16384

    Video mixer:

    feature name                    sup
    ------------------------------------
    DEINTERLACE_TEMPORAL             y
    DEINTERLACE_TEMPORAL_SPATIAL     -
    INVERSE_TELECINE                 -
    NOISE_REDUCTION                  y
    SHARPNESS                        y
    LUMA_KEY                         -
    HIGH QUALITY SCALING - L1        -
    HIGH QUALITY SCALING - L2        -
    HIGH QUALITY SCALING - L3        -
    HIGH QUALITY SCALING - L4        -
    HIGH QUALITY SCALING - L5        -
    HIGH QUALITY SCALING - L6        -
    HIGH QUALITY SCALING - L7        -
    HIGH QUALITY SCALING - L8        -
    HIGH QUALITY SCALING - L9        -

    parameter name                  sup      min      max
    -----------------------------------------------------
    VIDEO_SURFACE_WIDTH              y        48     2048
    VIDEO_SURFACE_HEIGHT             y        48     1152
    CHROMA_TYPE                      y
    LAYERS                           y         0        4

    attribute name                  sup      min      max
    -----------------------------------------------------
    BACKGROUND_COLOR                 y
    CSC_MATRIX                       y
    NOISE_REDUCTION_LEVEL            y      0.00     1.00
    SHARPNESS_LEVEL                  y     -1.00     1.00
    LUMA_KEY_MIN_LUMA                y
    LUMA_KEY_MAX_LUMA                y

VDPAU support:

-   [Mpv](https://wiki.gentoo.org/wiki/Mpv "Mpv")
-   SMplayer
-   Gnome-mplayer
-   [VLC](https://wiki.gentoo.org/wiki/VLC "VLC")

#### [VLC player]

VLC have support vdpau. To use it you must enable USE flag `vdpau`. If you enable it to `/etc/portage/make.conf`, it not necessary.

In VLC go to settings `(Ctrl+P) --> Input / Codecs --> Hardware-accelerated decoding` choose `VDPAU video decoder`

When VLC play movie with hardware acceleration load CPU is 30-40%.

## [Audio]

### [ALSA configuration]

[KERNEL] **Alsa configuration**

    Device Drivers  --->
      Sound card support  --->
        <*> Advanced Linux Sound Architecture  --->
          [*] PCI sound devices --->
            <*> Intel HD Audio --->
              [*] Build Realtek HD-audio codec support
              [*] Build HDMI/DisplayPort HD-audio codec support

A good way to manage ALSA is to emerge alsa-utils:

`root `[`#`]`emerge --ask alsa-utils`

To start alsa at boot time type:

`root `[`#`]`rc-update add alsasound boot `

There is a problem that actually ALSA often sees two sound cards: HD-Audio Generic (that is a kind of a virtual device, i.e. it doesn\'t actually play music) and the required HDA ATI SB. The simplest way to check it is to launch

`user `[`$`]`aplay -l`

    **** List of PLAYBACK Hardware Devices ****
    card 0: Generic [HD-Audio Generic], device 3: HDMI 0 [HDMI 0]
      Subdevices: 1/1
      Subdevice #0: subdevice #0
    card 1: SB [HDA ATI SB], device 0: ALC269VB Analog [ALC269VB Analog]
      Suvdevices: 1/1
      Subdevice #0: subdevice #0

If HD-Audio Generic is the first number, it might be the default card. If it is the case, than you\'re likely to have no sound unless the default card is switched from 0 to 1.

[FILE] **`/etc/asound.conf`**

    defaults.ctl.card 1
    defaults.pcm.card 1
    defaults.timer.card 1

## [Memory Card Reader]

Card reader is provided by Alcor Micro.

[KERNEL]

    Device Drivers  --->
        <*> MMC/SD/SDIO card support  --->
            <*>   MMC block device driver
            [*]     Use bounce buffer for simple hosts

## [Webcam]

Webcam is supported with standart UVC

[KERNEL] **Webcam Support**

    Device Drivers  --->
        <*> Multimedia support  --->
            [*] Media USB Adapters  --->
                <*> USB Video Class (UVC)

## [Tips and tricks]

If the laptop stops responding to keyboard and touchpad, add some parameters to kernel

[FILE] **`/etc/default/grub`**

    GRUB_CMDLINE_LINUX_DEFAULT="i8042.nomux i8042.reset"

Then, rebuild grub config

`root `[`#`]`grub-mkconfig -o /boot/grub/grub.cfg`

Finally, reboot

## [See aslo]

-   [Power_management/Guide](https://wiki.gentoo.org/wiki/Power_management/Guide "Power management/Guide")
-   [Bluetooth](https://wiki.gentoo.org/wiki/Bluetooth "Bluetooth")
-   [WiFi](https://wiki.gentoo.org/wiki/Wifi "Wifi")
-   [Radeon](https://wiki.gentoo.org/wiki/Radeon "Radeon")
-   [VDPAU](https://wiki.gentoo.org/wiki/VDPAU "VDPAU")

\

## [References]

1.  [[[↑](#cite_ref-1)] [[https://wireless.wiki.kernel.org/en/developers/Documentation/mac80211/RateControl/minstrel](https://wireless.wiki.kernel.org/en/developers/Documentation/mac80211/RateControl/minstrel)]]
2.  [[[↑](#cite_ref-2)] [[Forums thread: Kernel change : 3.16.3 -\> 3.17.8 : no wlan device anymore](https://forums.gentoo.org/viewtopic-p-7702944.html#7702944)]]