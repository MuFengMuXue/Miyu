\

## Contents

-   [[1] [Hardware Support]](#Hardware_Support)
    -   [[1.1] [Summary]](#Summary)
    -   [[1.2] [Extra Hardware Information]](#Extra_Hardware_Information)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Touchpad]](#Touchpad)
    -   [[2.2] [Disk Drives]](#Disk_Drives)
    -   [[2.3] [Graphics]](#Graphics)
    -   [[2.4] [Network Devices]](#Network_Devices)
    -   [[2.5] [Sound]](#Sound)
    -   [[2.6] [Webcam]](#Webcam)
    -   [[2.7] [Backlight]](#Backlight)
    -   [[2.8] [CPU Frequency scaling]](#CPU_Frequency_scaling)
    -   [[2.9] [SD Card Reader]](#SD_Card_Reader)

## [Hardware Support]

### [Summary]

  ---------------------- -------- ----------------------------------------------------
  Device                 Works?   Description
  Processor              Yes      4th Gen Intel Core i5-4200U 1.6Ghz
  Screen                 Yes      14.1\" 1366x768 LED Wide Screen
  Wireless               Yes      802.11N Atheros Wifi (freedom compatible chipset)
  Webcam                 Yes      Built-in 1.3 Mega Pixel Camera
  Card Reader            Yes      SD/MMC Card Reader
  Optical Drive          Yes      Super-Multi Drive (DVD-RAM/R/RW/+/-/CD-R/RW)
  Graphics               Yes      Intel® HD Graphics 4400
  Built-in Audio & Mic   Yes      Intel HD
  LAN                    Yes      10/100/1000 Mbps Gigabit Ethernet
  VGA                    Yes
  USB 2.0 x 3            Yes
  Microphone-in          Yes      TRRS jack (i.e. uses same socket as Headphone-out)
  Headphone-out          Yes
  ---------------------- -------- ----------------------------------------------------

### [Extra Hardware Information]

`root `[`#`]`lspci`

    00:00.0 Host bridge: Intel Corporation Haswell-ULT DRAM Controller (rev 09)
    00:02.0 VGA compatible controller: Intel Corporation Haswell-ULT Integrated Graphics Controller (rev 09)
    00:03.0 Audio device: Intel Corporation Device 0a0c (rev 09)
    00:14.0 USB controller: Intel Corporation Lynx Point-LP USB xHCI HC (rev 04)
    00:16.0 Communication controller: Intel Corporation Lynx Point-LP HECI #0 (rev 04)
    00:1b.0 Audio device: Intel Corporation Lynx Point-LP HD Audio Controller (rev 04)
    00:1c.0 PCI bridge: Intel Corporation Lynx Point-LP PCI Express Root Port 3 (rev e4)
    00:1c.3 PCI bridge: Intel Corporation Lynx Point-LP PCI Express Root Port 4 (rev e4)
    00:1d.0 USB controller: Intel Corporation Lynx Point-LP USB EHCI #1 (rev 04)
    00:1f.0 ISA bridge: Intel Corporation Lynx Point-LP LPC Controller (rev 04)
    00:1f.2 SATA controller: Intel Corporation Lynx Point-LP SATA Controller 1 [AHCI mode] (rev 04)
    00:1f.3 SMBus: Intel Corporation Lynx Point-LP SMBus Controller (rev 04)
    01:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. Device 5289 (rev 01)
    01:00.2 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 0a)
    02:00.0 Network controller: Qualcomm Atheros AR9285 Wireless Network Adapter (PCI-Express) (rev 01)

`root `[`#`]`lsusb`

    Bus 001 Device 004: ID 174f:14a1 Syntek
    Bus 001 Device 002: ID 8087:8000 Intel Corp.
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

## [Configuration]

### [Touchpad]

[KERNEL]

    Device Drivers  --->
        Input device support  --->
            -*- Generic input layer (needed for keyboard, mouse, ...)
            <*>   Mouse interface
            [*]   Mice  --->
                <*>   PS/2 mouse
                [*]      Elantech PS/2 mouse protocol extension

The Touchpad takes a lot of physical physical space under the keyboard, and it\'s easy to accidentally move the mouse cursor while typing. One can address this by enabling the Synaptics palm detection:

`user `[`$`]`synclient PalmDetect=1`

`user `[`$`]`synclient PalmMinWidth=5`

`synclient` is installed by the [[[x11-drivers/xf86-input-synaptics]](https://packages.gentoo.org/packages/x11-drivers/xf86-input-synaptics)[]]; see [synaptics driver installation instructions](https://wiki.gentoo.org/wiki/Synaptics#Driver "Synaptics").

### [Disk Drives]

[KERNEL]

    Device Drivers  --->
        SCSI device support  --->
            -*- SCSI device support
            [*] legacy /proc/scsi/ support
            <*> SCSI disk support
            <*> SCSI CDROM support
        <*> Serial ATA and Parallel ATA drivers  --->
            <*>   AHCI SATA support

### [Graphics]

[KERNEL]

    Device Drivers  --->
        Graphics support  --->
            <*> /dev/agpgart (AGP Support)  --->
                <*>   Intel 440LX/BX/GX, I8xx and E7x05 chipset support
            <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support)  --->
            <*> Intel 8xx/9xx/G3x/G4x/HD Graphics
            [*]   Enable modesetting on intel by default

### [Network Devices]

[KERNEL]

    Device Drivers  --->
        [*] Network device support  --->
            [*]   Ethernet driver support  --->
                  [*]   Realtek devices
                  <*>     RealTek 8169 gigabit ethernet support
            [*]   Wireless LAN  --->
                  <*>   Atheros Wireless Cards  --->
                        <*>   Atheros 802.11n wireless cards support
                        [*]     Atheros ath9k PCI/PCIe bus support

### [Sound]

[KERNEL]

    Device Drivers  --->
        <*> Sound card support  --->
            [*] Preclaim OSS device numbers
            <*> Advanced Linux Sound Architecture  --->
                [*]   PCI sound devices  --->
                      <*>   Intel HD Audio  --->
                            [*]   Support jack plugging notification via input layer
                            [*]   Build Realtek HD-audio codec support
                            [*]   Build HDMI/DisplayPort HD-audio codec support
                            -*-   Enable generic HD-audio codec parser

### [Webcam]

[KERNEL]

    Device Drivers  --->
        <*> Multimedia support  --->
                  *** Multimedia core support ***
            [*]   Cameras/video grabbers support
                  *** Media drivers ***
            [*]   Media USB Drivers  --->
                  <*>   USB Video Class (UVC)
                  <*>   GSPCA based webcams  --->
                        <*>   Syntek STK1135 USB Camera Driver

### [Backlight]

[KERNEL]

    Device Drivers  --->
        Graphics support  --->
            -*- Backlight & LCD device support  --->
                -*-   Lowlevel Backlight controls

The kernel parameter `acpi_backlight=vendor` must be added to make the backlight adjustable.

The backlight setting is not persistent between reboots, but it is persistent between suspend. Create a local service to save and apply the backlight setting:

[FILE] **`/etc/local.d/backlight.stop`Save backlight setting**

    #!/bin/sh
    einfo "Saving backlight brightness"
    cat /sys/class/backlight/intel_backlight/brightness > /var/tmp/backlight_brightness

[FILE] **`/etc/local.d/backlight.start`Restore backlight setting**

    #!/bin/sh
    brightness=`cat /var/tmp/backlight_brightness`
    max_brightness=`cat /sys/class/backlight/intel_backlight/max_brightness`
    percent() %"
    }
    # The COMPAL display brightness allows very low intensity values which
    # black out the screen!  We don't want this to happen, so ignore low
    # brightness values.
    if [ $brightness > 4 ]; then
        einfo "Restoring backlight brightness to $(percent brightness max_brightness)"
        echo $brightness > /sys/class/backlight/intel_backlight/brightness
    fi

[FILE] **`/etc/pm/sleep.d/xscreensaver`Unblank screen on resume**

    !/bin/bash
    case "$1" in
         suspend|hibernate)
            # No need to lock screen as XFCE does that for you.
            ;;
        resume|thaw)
            # Restore brightness.
            brightness=`cat /var/tmp/backlight_brightness`
            echo $brightness > /sys/class/backlight/intel_backlight/brightness
            xscreensaver-command -deactivate
            ;;
        *)
            exit 1
            ;;
    esac
    exit 0

### [CPU Frequency scaling]

[KERNEL]

    Power management and ACPI options  --->
        CPU Frequency scaling  --->
            [*] CPU Frequency scaling
                  x86 CPU frequency scaling drivers  --->
                  [*] Intel P state control
                  <*> ACPI Processor P-States driver

### [SD Card Reader]

[KERNEL]

    Device Drivers  --->
        <*> MMC/SD/SDIO card support  --->
            <*>   Realtek PCI-E SD/MMC Card Interface Driver