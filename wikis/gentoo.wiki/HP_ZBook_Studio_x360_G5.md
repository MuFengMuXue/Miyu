**Resources**

[[]][Official Support Page](https://support.hp.com/us-en/product/details/hp-zbook-studio-x360-g5-convertible-workstation/20075826)

[[]][Specifications](https://support.hp.com/us-en/document/c07722736)

[[]][Hardware Maintenance Manual](https://h10032.www1.hp.com/ctg/Manual/c06040448.pdf)

[[]][User Guide](https://h10032.www1.hp.com/ctg/Manual/c06040453.pdf)

[[]][HP ZBook](https://en.wikipedia.org/wiki/HP_ZBook "wikipedia:HP ZBook")

## Contents

-   [[1] [Linux Installation]](#Linux_Installation)
    -   [[1.1] [Kernel Configuration - the easy way]](#Kernel_Configuration_-_the_easy_way)
    -   [[1.2] [Kernel tweaking]](#Kernel_tweaking)
        -   [[1.2.1] [Kernel Type and Processor Family]](#Kernel_Type_and_Processor_Family)
        -   [[1.2.2] [Storage]](#Storage)
        -   [[1.2.3] [Video - Nouveau Driver vs. Nvidia proprietary driver]](#Video_-_Nouveau_Driver_vs._Nvidia_proprietary_driver)
            -   [[1.2.3.1] [Usage of the Nouveau driver]](#Usage_of_the_Nouveau_driver)
            -   [[1.2.3.2] [Usage of the Nvidia proprietary driver]](#Usage_of_the_Nvidia_proprietary_driver)
            -   [[1.2.3.3] [Console Fonts on HiDPI displays (very small characters)]](#Console_Fonts_on_HiDPI_displays_.28very_small_characters.29)
        -   [[1.2.4] [Wireless]](#Wireless)
        -   [[1.2.5] [Audio]](#Audio)
        -   [[1.2.6] [Bluetooth]](#Bluetooth)
        -   [[1.2.7] [Card Reader]](#Card_Reader)
        -   [[1.2.8] [Touchpad / Trackpad]](#Touchpad_.2F_Trackpad)
        -   [[1.2.9] [Touchscreen]](#Touchscreen)
        -   [[1.2.10] [Accelerometer]](#Accelerometer)
    -   [[1.3] [Bootloader - using GRUB]](#Bootloader_-_using_GRUB)
        -   [[1.3.1] [Tweaking GRUB]](#Tweaking_GRUB)
            -   [[1.3.1.1] [media-fonts/terminus-font]](#media-fonts.2Fterminus-font)
    -   [[1.4] [\"The sound of silence\" - Thermal Subsystem and FAN control (optional)]](#.22The_sound_of_silence.22_-_Thermal_Subsystem_and_FAN_control_.28optional.29)
        -   [[1.4.1] [Thermal monitoring - lm_sensors]](#Thermal_monitoring_-_lm_sensors)
        -   [[1.4.2] [User space fan control application: nbfc-linux]](#User_space_fan_control_application:_nbfc-linux)

# [Linux Installation]

## [Kernel Configuration - the easy way]

The easiest way to get a running Linux Kernel with support of all devices of the ZBook Studio x360 G5 is to use the config-file of the newest Gentoo-Live-CD or Gentoo-Live-USB-Stick and strip it down to what you really need. Afterwards it could be tweaked to achieve best performance or/and special demands.

## [Kernel tweaking]

### [Kernel Type and Processor Family]

Intel(R) Xeon(R) E-2186M CPU @ 2.90GHz

[KERNEL]

    [*] 64-bit kernel
            Processor type and features --->
                Processor family (Core 2/newer Xeon)  --->

### [Storage]

Silicon Motion, Inc. Device 2262 (rev 03) (prog-if 02 \[NVM Express\])

[KERNEL]

    Device Drivers  --->
            NVME Support  --->
                <*> NVM Express block device

For details see [NVMe](https://wiki.gentoo.org/wiki/NVMe "NVMe")

### [Video - Nouveau Driver vs. Nvidia proprietary driver]

-   Intel Corporation UHD Graphics 630 (Mobile) (prog-if 00 \[VGA controller\])

If there is no line \"00:02.0 VGA compatible controller: Intel Corporation Coffee Lake-S GT2 \[UHD Graphics P630\]\" in the lspci-listing you have to enable \"Hybrid Graphics\" in the advanced settings of the BIOS.

-   NVIDIA Corporation GP107GLM \[Quadro P1000 Mobile\] (rev a1) (prog-if 00 \[VGA controller\])

Although there are actually some drawbacks on backlight control which are currently not fixed it\'s a good idea to use the Nvidia proprietary driver. It is more performant and causes less CPU workload. This is especially important for high-performance demanding applications.

#### [Usage of the Nouveau driver]

[KERNEL]

    Device Drivers  --->
            Graphics support  --->
                <*> /dev/agpgart (AGP Support)  --->
                    <*>   Intel 440LX/BX/GX, I8xx and E7x05 chipset support
                <M> Nouveau (NVIDIA) cards
                [*]   Nouveau legacy context support
                    (5)   Maximum debug level
                    (3)   Default debug level

For details see [Intel](https://wiki.gentoo.org/wiki/Intel "Intel") and [nouveau & nvidia-drivers switching](https://wiki.gentoo.org/wiki/Nouveau_%26_nvidia-drivers_switching "Nouveau & nvidia-drivers switching") articles. Note that with models with discrete graphics, the HDMI port can only be used with the discrete graphics enabled.

Bumblebee is no longer required to use the HDMI port with hybrid graphics. The earliest versions have not been verified with this laptop, but this will work starting with at least Linux 5.4, [[[x11-base/xorg-server]](https://packages.gentoo.org/packages/x11-base/xorg-server)[]] 1.20.8, and [[[x11-drivers/xf86-video-nouveau]](https://packages.gentoo.org/packages/x11-drivers/xf86-video-nouveau)[]] 1.0.16.

#### [Usage of the Nvidia proprietary driver]

To get more information about using the Nvidia proprietary driver please take a look at the [Gentoo NVIDIA/nvidia-drivers](https://wiki.gentoo.org/wiki/Nvidia-drivers "Nvidia-drivers") wiki page.

\

#### [][Console Fonts on HiDPI displays (very small characters)]

On modern displays with high DPI (\"HiDPI\"), e.g. UHD (3840x2160), the standard font will look very small. If you like to have a bigger (readable) font, Terminus can be used, which resembles a BIOS built-in textmode font.

To select this font in-kernel, `CONFIG_FONT_TER16x32` has to be enabled.

[KERNEL] **Kernel compiled-in fonts**

    Library routines  --->
          [*] Select compiled-in fonts
          [*] Terminus 16x32 font (not supported by all drivers)

### [Wireless]

Intel Corporation Wireless-AC 9560 \[Jefferson Peak\] (rev 10)

[KERNEL]

    Device Drivers  --->
            [*] Network device support  --->
                [*]   Wireless LAN  --->
                      <M>     Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)
                      <M>       Intel Wireless WiFi MVM Firmware support

See the [iwlwifi](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi") article for more information as this laptop does suffer from not being able to connect to some access points without disabling 802.11n and enabling software crypto.

### [Audio]

Intel Corporation Cannon Lake PCH cAVS (rev 10) (prog-if 80)

[KERNEL]

    Device Drivers  --->
            <M> Sound card support  --->
                <M>   Advanced Linux Sound Architecture  --->
                      HD-Audio  --->
                          <M> HD Audio PCI
                      (4096) Pre-allocated buffer size for HD-audio driver
                <M>   ALSA for SoC audio support  --->
                          [*]   Intel ASoC SST drivers
                          [*]   Sound Open Firmware Support
                          <M>     SOF PCI enumeration support
                          <M>     SOF ACPI enumeration support
                          [*]     SOF support for Intel audio DSPs
                          [*]     SOF support for CoffeeLake

### [Bluetooth]

Deeper information about the kernel configuration for bluetooth could be found in this [Wiki-page](https://wiki.gentoo.org/wiki/Bluetooth#Kernel "Bluetooth")

[KERNEL]

    -*- Networking support  --->
            <M>   Bluetooth subsystem support  --->
                      Bluetooth device drivers  --->
                      [*]   Intel AG6XX protocol support

For details see [Bluetooth](https://wiki.gentoo.org/wiki/Bluetooth "Bluetooth")

### [Card Reader]

Realtek Semiconductor Co., Ltd. RTS525A PCI Express Card Reader (rev 01)

[KERNEL]

    Device Drivers  --->
            <M> MMC/SD/SDIO card support --->
                  <M> Realtek PCI-E SD/MMC Card Interface Driver

### [][Touchpad / Trackpad]

[KERNEL]

    Device Drivers  --->
                Input device support  --->
                            -*-   Generic input layer (needed for keyboard, mouse, ...)
                                 Synaptics RMI4 bus support
                            <*>     RMI4 SMB Support

                            [*]   Mice  --->
                                  <*>   PS/2 mouse
                                  [*]     Synaptics PS/2 mouse protocol extension
                                  [*]     Synaptics PS/2 SMbus companion

### [Touchscreen]

[KERNEL]

    Device Drivers  --->
                HID support  --->
                        Special HID drivers  --->
                            <M> HID Multitouch panels

### [Accelerometer]

ST Microelectronics LIS3LV02DL Accelerometer

[KERNEL]

    Device Drivers  --->
            <M> Industrial I/O support  --->
                        Accelerometers  --->
                            <M> HID Accelerometers 3D

## [Bootloader - using GRUB]

Using GRUB for loading the operating system provides the same problem as mentioned above for the Linux console. The ZBook start in HiDPI resolution mode and the characters on the screen are very small and hard to read.

### [Tweaking GRUB]

To get a bigger font also for the grub-menue you can set the font to terminus-font

#### [][media-fonts/terminus-font]

Emerge [[[media-fonts/terminus-font]](https://packages.gentoo.org/packages/media-fonts/terminus-font)[]] :

`root `[`#`]`emerge --ask media-fonts/terminus-font`

Afterwards font-conversion is needed from .otb format to the .pf2 format. This format could then be used by grub. For more information about the font configuration please read this [WIKI-Page](https://wiki.gentoo.org/wiki/GRUB "GRUB")

`root `[`#`]`grub-mkfont -s 32 -o /boot/grub/fonts/terminus32b.pf2 /usr/share/fonts/terminus/ter-u32b.otb`

The font then has to be set as `GRUB_FONT` in `/etc/default/grub` in order to be used.

[FILE] **`/etc/default/grub`Framebuffer related settings**

    # Use a custom font, converted using grub-mkfont utility
    GRUB_FONT="/boot/grub/fonts/terminus32b.pf2"

Updating the GRUB configuration file `grub.cfg` will then activate the configuration with the new font.

`root `[`#`]`grub-mkconfig -o /boot/grub/grub.cfg`

## [][\"The sound of silence\" - Thermal Subsystem and FAN control (optional)]

-   The HP ZBook Studio x360 G5 provides the following thermal subsystem (e.g. for the Intel(R) Xeon(R) E-2186M CPU):

`root `[`#`]`lspci `

\.... 00:04.0 Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem (rev 07)

Without any precausions the \"ZBook Studio x360 G5\" causes some annoying fan noise although the CPU temperature is wide under an acceptabe thermal threshold. A solution for this problem is the usage of a combination of thermal monitoring and fan control on the operating system side.

[KERNEL]

    Device Drivers  --->
            -X- Thermal Drivers  --->
                        Intel thermal drivers  --->
                                ACPI INT340X thermal drivers  --->
                                    <X> ACPI INT340X thermal drivers

### [Thermal monitoring - lm_sensors]

The most widely used package for thermal monitoring ist lm-sensors. An extensive description of this package could be found on the [Gentoo lm_sensors WIKI page](https://wiki.gentoo.org/wiki/Lm_sensors "Lm sensors")

### [User space fan control application: nbfc-linux]

A good tool for fan control is the user-space tool nbfc-linux which is a C-port of the \"Hirschmann\" application nbfc implemented under the usage of Mono. The nbfc-linux tool can be found [here](https://github.com/nbfc-linux/nbfc-linux) at github.

[KERNEL]

    Power management and ACPI options  --->
            [*] ACPI (Advanced Configuration and Power Interface) Support  --->
                <*>  EC read/write access through /sys/kernel/debug/ec