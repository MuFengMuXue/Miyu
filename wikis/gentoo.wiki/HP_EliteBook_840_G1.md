**Resources**

[[]][Official Support Page](https://support.hp.com/us-en/product/details/hp-elitebook-840-g1-notebook-pc/5405360)

[[]][Specifications](https://support.hp.com/us-en/document/c03961746)

[[]][Hardware Maintenance Manual](https://h10032.www1.hp.com/ctg/Manual/c04655205.pdf)

[[]][User Guide](https://h10032.www1.hp.com/ctg/Manual/c04156186.pdf)

[[]][HP EliteBook](https://en.wikipedia.org/wiki/HP_EliteBook "wikipedia:HP EliteBook")

This article written on HP EliteBook 840 G1 (D8R82AV variant).

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [Detailed information]](#Detailed_information)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Firmware]](#Firmware)
    -   [[2.2] [Kernel]](#Kernel)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [ACPI events]](#ACPI_events)
        -   [[3.1.1] [Lid]](#Lid)
        -   [[3.1.2] [AC Adapter]](#AC_Adapter)
        -   [[3.1.3] [Complete configuration]](#Complete_configuration)

## [Hardware]

### [Standard]

  ----------------------------- ------------------------------------------------------------------------------- -------- ------------------------ ------------------ ---------------- ------------------------------------------------
  Device                        Make/model                                                                      Status   Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  Video card                    Intel Corporation Haswell-ULT Integrated Graphics Controller (HD4400)(rev 0b)   Works    8086:0a16                i915               N/A
  Ethernet controller           Intel Corporation Ethernet Connection I218-LM (rev 04)                          Works    8086:155a                e1000e             N/A
  Wireless network controller   Intel Corporation Wireless 7260 (rev 73)                                        Works    8086:08b1                iwlwifi            N/A              Interface modes other than managed not tested.
  Bluetooth                     N/A                                                                             Works    8087:07dc                btusb              N/A
  Web Camera                    Chicony Electronics Co., Ltd HP HD Camera                                       Works    04f2:b3ed                uvcvideo           N/A
  ----------------------------- ------------------------------------------------------------------------------- -------- ------------------------ ------------------ ---------------- ------------------------------------------------

### [Detailed information]

`root `[`#`]`lspci -nn`

    00:00.0 Host bridge [0600]: Intel Corporation Haswell-ULT DRAM Controller [8086:0a04] (rev 0b)
    00:02.0 VGA compatible controller [0300]: Intel Corporation Haswell-ULT Integrated Graphics Controller [8086:0a16] (rev 0b)
    00:03.0 Audio device [0403]: Intel Corporation Haswell-ULT HD Audio Controller [8086:0a0c] (rev 0b)
    00:14.0 USB controller [0c03]: Intel Corporation 8 Series USB xHCI HC [8086:9c31] (rev 04)
    00:16.0 Communication controller [0780]: Intel Corporation 8 Series HECI #0 [8086:9c3a] (rev 04)
    00:16.3 Serial controller [0700]: Intel Corporation 8 Series HECI KT [8086:9c3d] (rev 04)
    00:19.0 Ethernet controller [0200]: Intel Corporation Ethernet Connection I218-LM [8086:155a] (rev 04)
    00:1b.0 Audio device [0403]: Intel Corporation 8 Series HD Audio Controller [8086:9c20] (rev 04)
    00:1c.0 PCI bridge [0604]: Intel Corporation 8 Series PCI Express Root Port 1 [8086:9c10] (rev e4)
    00:1c.3 PCI bridge [0604]: Intel Corporation 8 Series PCI Express Root Port 4 [8086:9c16] (rev e4)
    00:1c.4 PCI bridge [0604]: Intel Corporation 8 Series PCI Express Root Port 5 [8086:9c18] (rev e4)
    00:1c.5 PCI bridge [0604]: Intel Corporation 8 Series PCI Express Root Port 6 [8086:9c1a] (rev e4)
    00:1d.0 USB controller [0c03]: Intel Corporation 8 Series USB EHCI #1 [8086:9c26] (rev 04)
    00:1f.0 ISA bridge [0601]: Intel Corporation 8 Series LPC Controller [8086:9c43] (rev 04)
    00:1f.2 SATA controller [0106]: Intel Corporation 8 Series SATA Controller 1 [AHCI mode] [8086:9c03] (rev 04)
    00:1f.3 SMBus [0c05]: Intel Corporation 8 Series SMBus Controller [8086:9c22] (rev 04)
    02:00.0 Network controller [0280]: Intel Corporation Wireless 7260 [8086:08b1] (rev 73)
    03:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Mars [Radeon HD 8730M] [1002:6601]
    03:00.1 Audio device [0403]: Advanced Micro Devices, Inc. [AMD/ATI] Oland/Hainan/Cape Verde/Pitcairn HDMI Audio [Radeon HD 7000 Series] [1002:aab0]
    04:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS5227 PCI Express Card Reader [10ec:5227] (rev 01)

`root `[`#`]`lsusb`

    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 001 Device 002: ID 0424:2134 Microchip Technology, Inc. (formerly SMSC) Hub
    Bus 001 Device 003: ID 04f2:b3ed Chicony Electronics Co., Ltd HP HD Webcam
    Bus 001 Device 004: ID 8087:07dc Intel Corp. Bluetooth wireless interface
    Bus 001 Device 005: ID 058f:9540 Alcor Micro Corp. AU9540 Smartcard Reader
    Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 002 Device 002: ID 8087:8000 Intel Corp. Integrated Rate Matching Hub
    Bus 003 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 003 Device 002: ID 0424:5534 Microchip Technology, Inc. (formerly SMSC) Hub

## [Installation]

[FILE] **`/etc/portage/package.use/00input`**

    */* INPUT_DEVICES: libinput

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* i915 intel radeon radeonsi

### [Firmware]

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

### [Kernel]

[KERNEL] **NVME block device**

    Device Drivers  --->
           NVME Support  --->
          <*> NVM Express block device

[KERNEL] **Ethernet controller**

    Generic Driver Options  --->
       [*] Network device support  ---
          [*]   Ethernet driver support  --->
             [*]   Intel devices
             <M>     Intel(R) PRO/1000 PCI-Express Gigabit Ethernet support

[KERNEL] **Wireless network controller**

    Generic Driver Options  --->
       [*] Network device support  ---
          [*]   Wireless LAN  --->
             [*]   Intel devices
             <M>     Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)
             <M>       Intel Wireless WiFi MVM Firmware support

[KERNEL] **Bluetooth device**

    Networking Support  --->
       <*> Bluetooth subsystem support  --->
          <*>   Bluetooth device drivers  --->
             <M>   HCI USB driver  --->

[KERNEL] **Trackpad**

    Devices Drivers  --->
       Input device support  --->
          [*]   Mice  --->
             <M>   PS/2 mouse
          <M>   Synaptics RMI4 bus support
          <M>     RMI4 SMB Support
          [*]     RMI4 Function 03 (PS2 Guest)
          [*]     RMI4 Function 11 (2D pointing)
          [*]     RMI4 Function 12 (2D pointing)
          [*]     RMI4 Function 30 (GPIO LED)
          [*]     RMI4 Function 34 (Device reflash)
          [*]     RMI4 Function 3A (GPIO)
          [*]     RMI4 Function 54 (Analog diagnostics)

[KERNEL] **Audio device**

    Device Drivers  --->
       <*> Sound card support  --->
          <*>   Advanced Linux Sound Architecture  --->
             [*]   PCI sound devices  --->
                      <M>   Intel/SiS/nVidia/AMD/ALi AC97 Controller
                   HD-Audio  --->
                      <M> HD Audio PCI
                      <M> Build IDT/Sigmatel HD-audio codec support
                      <M> Build HDMI/DisplayPort HD-audio codec support

[KERNEL] **Webcam device**

    Device Drivers  --->
       <*> Multimedia support  --->
              Media Device Types  --->
                 [*] Cameras and video grabbers
              Media drivers  -->
                 [*] Media USB Adapters  --->
                     <M>   USB Video Class (UVC)

## [Configuration]

### [ACPI events]

Install the [ACPI](https://wiki.gentoo.org/wiki/ACPI "ACPI") daemon:

`root `[`#`]`emerge --ask sys-power/acpid`

#### [Lid]

[FILE] **`/etc/acpi/default.sh`**

    case "$group" in
      button)
        case "$action" in
          ...
          # handle lid close
          lid)
            if grep -q closed /proc/acpi/button/lid/LID/state
            then
              systemctl suspend
            fi
          ;;
          ...

#### [AC Adapter]

[FILE] **`/etc/acpi/default.sh`**

    case "$group" in
      ...
      ac_adapter)
        case "$value" in
          # Action on unplug AC power
          *0)
            cpupower frequecy-set -g powersave
            echo 300 > /sys/class/backlight/intel_backlight/brightness
            ;;

          # Action on plug AC Power
          *1)
            cpupower frequency-set -g performance
            echo 937 > /sys/class/backlight/intel_backlight/brightness
            ;;

          *) log_unhandled $* ;;
        esac
        ;;
        ...

#### [Complete configuration]

[FILE] **`/etc/acpi/default.sh`**

    #!/bin/sh
    # /etc/acpi/default.sh
    # Default acpi script that takes an entry for all actions

    set $*

    group=$
    action=$
    device=$2
    id=$3
    value=$4

    log_unhandled()

    case "$group" in
      button)
        case "$action" in
          power)
            /etc/acpi/actions/powerbtn.sh
          ;;
          # avoid mute key (fn+f8) to log unhandled
          mute);;
          f20);;
          # handle lid close
          lid)
            if grep -q closed /proc/acpi/button/lid/LID/state
            then
              systemctl suspend
            fi
          ;;
          # (fn+f6)
          volumedown);;
          # (fn+f7)
          volumeup);;
          # arrow keys
          up);;
          down);;
          left);;
          right);;
          # log unhandled actions
          *)
            log_unhandled $* ;;
        esac
        ;;

      ac_adapter)
        case "$value" in
          # Action on unplug AC power
          *0)
            cpupower frequency-set -g powersave
            echo 300 > /sys/class/backlight/intel_backlight/brightness
            ;;

          # Action on plug AC Power
          *1)
            cpupower frequency-set -g performance
            echo 937 > /sys/class/backlight/intel_backlight/brightness
            ;;

          *) log_unhandled $* ;;
        esac
        ;;
      battery) ;;
      video)
        case "$action" in
          # (fn+f4)
          switchmode) ;;
          # (fn+f8)
          brightnessdown) ;;
          # (fn+f9)
          brightnessup) ;;
          *) log_unhandled $* ;;
        esac
        ;;
      *)  log_unhandled $* ;;
    esac