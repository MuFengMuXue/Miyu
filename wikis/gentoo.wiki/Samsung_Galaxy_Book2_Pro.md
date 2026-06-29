**Resources**

[[]][Home](https://www.samsung.com/us/computing/galaxy-book2/buy/?modelCode=NP930XED-KA1US)

The Samsung Galaxy Book2 Pro is a productivity laptop released in 2022. It comes in a few varieties, with 2 choices of CPU and screen size, which also affect the RAM and SSD size:

  --------- --------------------- ---------------------
            Intel Core i5-1240P   Intel Core i7-1260P
  13.3 in   8 GB RAM              8 GB RAM
            256 GB SSD            512 GB SSD
  15.6 in   8 GB RAM              16 GB RAM
            512 GB SSD            512 GB SSD
  --------- --------------------- ---------------------

This laptop is extremely light at 0.87 kg (13.3 in model) / 1.16 kg (15.6 in model), yet quite powerful. It features a 12th generation Intel CPU, 8 GB / 16 GB of RAM, a 256 GB / 512 GB SSD, a 1920x1080 AMOLED screen, and a good selection of ports. Hardware is largely supported and the system can be made very usable, though doing so requires proprietary firmware blobs. The lack of a dedicated GPU makes it unsuited for heavy graphics or gaming workloads.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [BIOS]](#BIOS)
    -   [[1.2] [Standard]](#Standard)
    -   [[1.3] [Ports]](#Ports)
    -   [[1.4] [Firmware]](#Firmware)
    -   [[1.5] [Kernel]](#Kernel)
-   [[2] [make.conf]](#make.conf)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Brightness keys]](#Brightness_keys)
    -   [[3.2] [Volume keys]](#Volume_keys)
-   [[4] [External resources]](#External_resources)
-   [[5] [References]](#References)

## [Hardware]

### [BIOS]

Hold [F2] to enter the BIOS upon boot. Hold the power button to forcefully shut down the computer.

### [Standard]

  --------------------- -------------------------------------------- ------------------- ------------------------ ------------------ --------------------------
  Device                Make/model                                   Status              Vendor ID / Product ID   Kernel driver(s)   Notes
  CPU                   Intel Core i5-1240P / Intel Core i7-1260P    Works                                        i915               Alder Lake architecture.
  RAM                   8 GB / 16 GB LPDDR5                          Works
  Disk                  256 GB / 512 GB NVMe SSD                     Works                                        nvme
  Ethernet              ASIX AX88179A Gigabit Ethernet               Works               0b95:1790                cdc_ncm
  Display               13.3 in / 15.6 in 1920x1080 AMOLED           Only in software
  Camera                SunplusIT 1080p                              Works               2b7e:c556                uvcvideo
  Fingerprint scanner   LighTuning ETU905x                           Untested            1c7a:0582
  Network card          Intel Wi-Fi 6E AX211 160 MHz                 Works               8086:0094                iwlwifi
  Sound card            Intel Alder Lake PCH-P HD Audio Controller   Works               8086:51c8                snd_hda_intel
  --------------------- -------------------------------------------- ------------------- ------------------------ ------------------ --------------------------

### [Ports]

-   1 USB-A
-   1 USB-C
-   1 Thunderbolt
-   1 HDMI
-   1 MicroSD card
-   1 3.5 mm audio jack

### [Firmware]

Install DMC, GuC, and HuC firmware as detailed in [Intel firmware](https://wiki.gentoo.org/wiki/Intel#Firmware "Intel"). Update microcode as detailed in [Intel microcode](https://wiki.gentoo.org/wiki/Intel_microcode "Intel microcode").

### [Kernel]

Enable [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") support:

[KERNEL]

    Processor type and features --->
        [*] EFI runtime service support (EFI=y)

To boot using [EFI stub](https://wiki.gentoo.org/wiki/EFI_stub "EFI stub"):

[KERNEL]

    Processor type and features --->
        [*] EFI runtime service support (EFI=y)
            [*] EFI stub support (EFI_STUB=y)
                [ ] EFI mixed-mode support (EFI_MIXED=n)

Enable NVMe support:

[KERNEL]

    Device Drivers --->
        NVME Support --->
            <*> NVM Express block device

Enable sound support:

** Note**\
Although this is an Alder Lake system, the Tiger Lake SOF driver is the correct one here. *The Alder Lake SOF driver will not work!*

[KERNEL]

    Device Drivers --->
        <*> Sound card support --->
            <*> Advanced Linux Sound Architecture --->
                [*] PCI sound devices
                HD-Audio --->
                    <*> HD Audio PCI
                    <*> Build Realtek HD-audio codec support
                    <*> Build HDMI/DisplayPort HD-audio codec support
                <*> ALSA for SoC audio support --->
                    [*] Intel ASoC SST drivers
                    <*>   Skylake Platforms
                    [*]   HDAudio codec support
                    <*> Intel Machine drivers --->
                        <*> Skylake+ with HDA Codecs
                    [*] Sound Open Firmware Support --->
                        <*> SOF PCI enumeration support
                        [*] SOF support for Intel audio DSPs
                        <*> SOF support for Tigerlake

Enable the ports:

[KERNEL]

    Device Drivers --->
        [*] USB support --->
            <*> Support for Host-side USB
            <*> xHCI HCD (USB 3.0) support
        <*> Unified support for USB4 and Thunderbolt --->

Enable Ethernet support:

[KERNEL]

    Device Drivers --->
        [*] Network device support --->
            <*> USB Network Adapters --->
                <*> Multi-purpose USB Networking Framework
                <*>   ASIX AX88179/178A USB 3.0/2.0 to Gigabit Ethernet
                <*>   CDC NCM support

## [make.conf]

[FILE] **`/etc/portage/make.conf`**

    COMMON_FLAGS="-march=native -O2 -pipe"
    RUSTFLAGS="-C target-cpu=native -C opt-level=2"

    CPU_FLAGS_X86="aes avx avx2 f16c fma3 mmx mmxext pclmul popcnt rdrand sha sse sse2 sse3 sse4_1 sse4_2 ssse3"

    VIDEO_CARDS="intel"

    # Tell sys-firmware/intel-microcode to only install microcode for this computer's CPU.
    MICROCODE_SIGNATURES="-S"

## [Configuration]

### [Brightness keys]

The laptop\'s AMOLED screen is currently unsupported by the kernel. Instead, the brightness must be adjusted in software, using color correction. On X, emerge [[[x11-apps/xrandr]](https://packages.gentoo.org/packages/x11-apps/xrandr)[]]:

`root `[`#`]`emerge --ask x11-apps/xrandr`

Determine the output\'s name by running:

`user `[`$`]`xrandr --listmonitors`

    Monitors: 1
     0: +*eDP-1 1920/294x1080/165+0+0  eDP-1

Here the output is named **eDP-1**. Then try setting the brightness to 50%:

`user `[`$`]`xrandr --output eDP-1 --brightness .5`

This process can be automated with a script such as this:

[FILE] **`/usr/bin/brightness`**

    #!/bin/sh

    BRIGHTNESS_FILE="$/.local/brightness"
    OUTPUT="eDP-1"
    INCREMENT=5

    if [ -f "$" ]; then
        BRIGHTNESS=$(cat "$")
    else
        touch "$"
        BRIGHTNESS=100
    fi

    case "$" in
        up)   [ $ -lt 100 ] && BRIGHTNESS=$(($ + $)) ;;
        down) [ $ -gt 0   ] && BRIGHTNESS=$(($ - $)) ;;
    esac

    xrandr --output $ --brightness $(echo "scale=2; $/100" | bc)
    echo $ > "$"

This script allows a user to run [brightness up] and [brightness down] to change the brightness in increments of 5%. It stores the current brightness in [\~/.local/brightness], allowing it to be preserved across shells and reboots. [brightness] (without any arguments) can be run to restore the brightness from this file in case something else messes the brightness up (for example, if X resets the color correction on startup).

The brightness keys can then be bound to call this script when pressed.

### [Volume keys]

Install [[[media-sound/alsa-utils]](https://packages.gentoo.org/packages/media-sound/alsa-utils)[]]:

`root `[`#`]`emerge --ask media-sound/alsa-utils`

Then bind the volume keys to the following commands:

Raise volume by 5%:

`user `[`$`]`amixer -q set Master 5%+`

Lower volume by 5%:

`user `[`$`]`amixer -q set Master 5%-`

Toggle mute/unmute:

`user `[`$`]`amixer -q set Master toggle`

## [External resources]

-   [https://www.techradar.com/reviews/samsung-galaxy-book2-pro](https://www.techradar.com/reviews/samsung-galaxy-book2-pro)
-   [https://wiki.archlinux.org/title/Laptop/Samsung](https://wiki.archlinux.org/title/Laptop/Samsung)
-   [https://github.com/joshuagrisham/galaxy-book2-pro-linux](https://github.com/joshuagrisham/galaxy-book2-pro-linux)

## [References]