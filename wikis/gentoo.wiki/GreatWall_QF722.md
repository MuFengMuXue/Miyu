[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=GreatWall_QF722&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Product Information](https://www.greatwall.com.cn/product/34.html)

[[]][Specifications](https://www.greatwall.com.cn/product/34.html)

[[]][User Manual](https://static2.17youhui.com.cn/uploads/sites/36/2022/09/321c152b7a0186a4b317ddcd1bddd459.pdf)

The GreatWall QF722 is an AArch64 based laptop featuring an ARMv8 based Phytium FT-2000/4-M processor.

This product is not meant for consumer market but government usage, which makes it niche and expensive to get (as brand new).

**Pros:**

-   More standardized overall hardware architecture compared to other SoC-based ARM Laptops

**Cons:**

-   Niche and expensive to get on the consumer market
-   Some hardware have no mainline support
-   Barely benefits anything from using an ARM processor (less noise and heat, longer battery life, etc. compared to x86-based laptops)

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [Detailed information]](#Detailed_information)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Firmware]](#Firmware)
    -   [[2.2] [Kernel]](#Kernel)
        -   [[2.2.1] [Very Basics]](#Very_Basics)
        -   [[2.2.2] [Power Management]](#Power_Management)
        -   [[2.2.3] [USB Support]](#USB_Support)
        -   [[2.2.4] [Keyboard & Trackpad]](#Keyboard_.26_Trackpad)
        -   [[2.2.5] [WLAN]](#WLAN)
        -   [[2.2.6] [Webcam]](#Webcam)
        -   [[2.2.7] [GPU]](#GPU)
        -   [[2.2.8] [Sound]](#Sound)
        -   [[2.2.9] [Bluetooth]](#Bluetooth)
    -   [[2.3] [Alternative: Using NeoKylin Kernel]](#Alternative:_Using_NeoKylin_Kernel)
        -   [[2.3.1] [Optional: reinstalling linux-firmware]](#Optional:_reinstalling_linux-firmware)
        -   [[2.3.2] [Optional: Suppressing Oddball Kernel Messages]](#Optional:_Suppressing_Oddball_Kernel_Messages)
    -   [[2.4] [Emerge]](#Emerge)
        -   [[2.4.1] [Keyboard & Mouse]](#Keyboard_.26_Mouse)
        -   [[2.4.2] [Embedded Controller (EC)]](#Embedded_Controller_.28EC.29)
        -   [[2.4.3] [Sound]](#Sound_2)
        -   [[2.4.4] [Linux-firmware]](#Linux-firmware)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Optional: Capping CPU Frequency]](#Optional:_Capping_CPU_Frequency)
    -   [[3.2] [Optional: Change the CPU governor]](#Optional:_Change_the_CPU_governor)
-   [[4] [External resources]](#External_resources)

## [Hardware]

### [Standard]

  -------------------------- ----------------------------------------------------------------- ----------------- --------------------------------------------- ------------------ --------------------- ----------------------------------------------------------------------------------------------------------------------
  Device                     Make/model                                                        Status            Vendor ID / Product ID                        Kernel driver(s)   Kernel version        Notes
  CPU                        Phytium FT-2000/4-M                                               Malfunction       N/A                                           N/A                6.12.21-gentoo-dist   SCMI based governor having issues, unable to scale CPU frequency; workloads are not properly distributed among cores
  GPU                        AMD RX550X                                                        Works             1002:6987:17aa:380e / 03-00                   amdgpu             6.12.21-gentoo-dist
  NVMe ssd                   WD Blue SN550 NVMe SSD 256GB                                      Works             \-                                            nvme               6.12.21-gentoo-dist
  WLAN Adapter               RTL8821CE 802.11ac PCIe Wireless Network Adapter                  Works             10ec:c821:1a3b:3043 / 02-80-00                rtw88_8821ce       6.12.21-gentoo-dist
  Bluetooth Adapter          IMC Networks Bluetooth Radio                                      Works             13d3:3533 / e0-01-01                          btusb              6.12.21-gentoo-dist   Doesn\'t work on NeoKylin 5.10 kernel due to linux-firmware issues
  USB Controller             ASMedia Technology Inc. ASM2142/ASM3142 USB 3.1 Host Controller   Works             1b21:2142:1b21:2142 / 0c-03-30                xhci_hcd           6.12.21-gentoo-dist
  USB Controller             VIA Technologies, Inc. VL805/806 xHCI USB 3.0 Controller          Works             1106:3483:1106:3483 / 0c-03-30                xhci_hcd           6.12.21-gentoo-dist
  Fingerprint Sensor         PXAT MOH                                                          Non-functional    2f0a:0f0d / ff-00-00                          \-                 6.12.21-gentoo-dist   No drivers available.
  Audio                      PhyHDA (wrapped Realtek ALC269VC)                                 Undetectable      ?                                             \-                 6.12.21-gentoo-dist   No drivers available.
  Webcam                     Shenzhen Kingcome Optoelectronic KNC-172F                         Works             2b7e:0172 / 0e-01-00                          uvcvideo           6.12.21-gentoo-dist
  Embedded Controller (EC)   \-                                                                Works             \-                                            gwnb_power         6.12.21-gentoo-dist   Requires out-of-tree kernel module; Sluggish, power status change takes \~30s to be reflected
  Keyboard                   AT Translated Set 2 keyboard                                      Limited           ps/2:0001-0001-at-translated-set-2-keyboard   ft8042             6.12.21-gentoo-dist   Requires out-of-tree kernel module; multimedia keys non-functional.
  Trackpad                   ImPS/2 Wheel Mouse                                                Works             ps/2:logitech-0005-imps-2-wheel-mouse         ft8042             6.12.21-gentoo-dist   Requires out-of-tree kernel module.
  -------------------------- ----------------------------------------------------------------- ----------------- --------------------------------------------- ------------------ --------------------- ----------------------------------------------------------------------------------------------------------------------

### [Detailed information]

`root `[`#`]`uname -r`

    6.12.21-gentoo

`root `[`#`]`lscpu`

    Architecture:             aarch64
      CPU op-mode(s):         32-bit, 64-bit
      Byte Order:             Little Endian
    CPU(s):                   4
      On-line CPU(s) list:    0-3
    Vendor ID:                Phytium
      BIOS Vendor ID:         PHYTIUM LTD
      Model name:             FTC663
        BIOS Model name:      FT-2000/4-M Greatwall CPU @ 2.2GHz
        BIOS CPU family:      257
        Model:                3
        Thread(s) per core:   1
        Core(s) per socket:   4
        Socket(s):            1
        Stepping:             0x1
        BogoMIPS:             96.00
        Flags:                fp asimd evtstrm aes pmull sha1 sha2 crc32 cpuid
    Caches (sum of all):
      L1d:                    64 KiB (3 instances)
      L1i:                    96 KiB (3 instances)
      L2:                     2 MiB (2 instances)
      L3:                     4 MiB (1 instance)
    NUMA:
      NUMA node(s):           1
      NUMA node0 CPU(s):      0-3
    Vulnerabilities:
      Gather data sampling:   Not affected
      Itlb multihit:          Not affected
      L1tf:                   Not affected
      Mds:                    Not affected
      Meltdown:               Mitigation; PTI
      Mmio stale data:        Not affected
      Reg file data sampling: Not affected
      Retbleed:               Not affected
      Spec rstack overflow:   Not affected
      Spec store bypass:      Not affected
      Spectre v1:             Mitigation; __user pointer sanitization
      Spectre v2:             Not affected
      Srbds:                  Not affected
      Tsx async abort:        Not affected

`root `[`#`]`lspci -nnk`

    00:00.0 PCI bridge [0604]: Cadence Design Systems, Inc. Device [17cd:dc16]
        Kernel driver in use: pcieport
    00:01.0 PCI bridge [0604]: Cadence Design Systems, Inc. Device [17cd:dc08]
        Kernel driver in use: pcieport
    00:02.0 PCI bridge [0604]: Cadence Design Systems, Inc. Device [17cd:dc01]
        Kernel driver in use: pcieport
    00:03.0 PCI bridge [0604]: Cadence Design Systems, Inc. Device [17cd:dc16]
        Kernel driver in use: pcieport
    00:04.0 PCI bridge [0604]: Cadence Design Systems, Inc. Device [17cd:dc08]
        Kernel driver in use: pcieport
    00:05.0 PCI bridge [0604]: Cadence Design Systems, Inc. Device [17cd:dc01]
        Kernel driver in use: pcieport
    01:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Lexa [Radeon 540X/550X/630 / RX 640 / E9171 MCM] [1002:6987] (rev c0)
        Subsystem: Lenovo Device [17aa:380e]
        Kernel driver in use: amdgpu
        Kernel modules: amdgpu
    01:00.1 Audio device [0403]: Advanced Micro Devices, Inc. [AMD/ATI] Baffin HDMI/DP Audio [Radeon RX 550 640SP / RX 560/560X] [1002:aae0]
        Subsystem: Lenovo Device [17aa:aae0]
        Kernel driver in use: snd_hda_intel
        Kernel modules: snd_hda_intel
    02:00.0 USB controller [0c03]: ASMedia Technology Inc. ASM2142/ASM3142 USB 3.1 Host Controller [1b21:2142]
        Subsystem: ASMedia Technology Inc. ASM2142/ASM3142 USB 3.1 Host Controller [1b21:2142]
        Kernel driver in use: xhci_hcd
    04:00.0 USB controller [0c03]: VIA Technologies, Inc. VL805/806 xHCI USB 3.0 Controller [1106:3483] (rev 01)
        Subsystem: VIA Technologies, Inc. VL805/806 xHCI USB 3.0 Controller [1106:3483]
        Kernel driver in use: xhci_hcd
    05:00.0 Non-Volatile memory controller [0108]: Sandisk Corp SanDisk Ultra 3D / WD PC SN530, IX SN530, Blue SN550 NVMe SSD (DRAM-less) [15b7:5009] (rev 01)
        Subsystem: Sandisk Corp WD Blue SN550 NVMe SSD [15b7:5009]
        Kernel driver in use: nvme
    06:00.0 Network controller [0280]: Realtek Semiconductor Co., Ltd. RTL8821CE 802.11ac PCIe Wireless Network Adapter [10ec:c821]
        Subsystem: AzureWave Device [1a3b:3043]
        Kernel driver in use: rtw_8821ce
        Kernel modules: rtw88_8821ce

`root `[`#`]`lsusb`

    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 003 Device 002: ID 2109:3431 VIA Labs, Inc. Hub
    Bus 003 Device 003: ID 2f0a:0f0d PXAT MOH
    Bus 003 Device 004: ID 13d3:3533 IMC Networks Bluetooth Radio
    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub

`root `[`#`]`lsusb -vt`

    /:  Bus 001.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/2p, 480M
        ID 1d6b:0002 Linux Foundation 2.0 root hub
    /:  Bus 002.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/2p, 10000M
        ID 1d6b:0003 Linux Foundation 3.0 root hub
    /:  Bus 003.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/1p, 480M
        ID 1d6b:0002 Linux Foundation 2.0 root hub
        |__ Port 001: Dev 002, If 0, Class=Hub, Driver=hub/4p, 480M
            ID 2109:3431 VIA Labs, Inc. Hub
            |__ Port 001: Dev 003, If 0, Class=Vendor Specific Class, Driver=[none], 12M
                ID 2f0a:0f0d
            |__ Port 003: Dev 004, If 0, Class=Wireless, Driver=btusb, 12M
                ID 13d3:3533 IMC Networks
            |__ Port 003: Dev 004, If 1, Class=Wireless, Driver=btusb, 12M
                ID 13d3:3533 IMC Networks
    /:  Bus 004.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/4p, 5000M
        ID 1d6b:0003 Linux Foundation 3.0 root hub

## [Installation]

Due to missing specifically tailored PS/2 controller drivers, the built-in keyboard and trackpad won\'t be functional in Gentoo Minimal Installation Disk and many other LiveCD environments. Either prepare a set of USB keyboard (& mouse for GUI), or use few distros that have this driver built in: [openKylin](https://www.openkylin.top/index-en.html), [NeoKylin](https://kylinos.cn/), or [Uniontech UOS](https://uos.uniontech.com/).

### [Firmware]

The firmware follows UEFI 2.7 standard. No DeviceTree is used.

[Handbook:AMD64/Installation/Bootloader#UEFI systems](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Bootloader#UEFI_systems "Handbook:AMD64/Installation/Bootloader") could be used as a cross reference to set up [GRUB].

### [Kernel]

** Important**\
This configuration makes the system work to the extent described in the Hardware section, but probably not the most optimized, either due to poor/misunderstanding of things by the author or for fail-safe considerations.

#### [Very Basics]

[KERNEL] **Basic Configurations**

    Platform selection  --->
        (clear all options.)
    Kernel Features  --->
        [*] Multi-core scheduler support
        [*] SMT scheduler support
            (512) Maximum number of CPUs (2-4096)
        [*] ARM Scalable Vector Extension support
        [*] Core Scheduling for SMT
        [*] Kernel support for 32-bit EL0  --->
            [*]   Enable kuser helpers page for 32-bit applications (NEW)
            [*]   Fix up misaligned multi-word loads and stores in user space
            [*]   Emulate deprecated/obsolete ARMv8 instructions  --->
                [*]   Emulate SWP/SWPB instructions
                [*]   Emulate CP15 Barrier instructions
                [*]   Emulate SETEND instruction
        ARMv8.1 architectural features --->
            [*] Atomic instructions
    Boot options  --->
        [*] Enable support for the ARM64 ACPI parking protocol
        [*] UEFI runtime support
        [*] Install compressed image by default
        [*] Enable support for SMBIOS (DMI) tables
    Device Drivers  --->
        Generic Driver Options  --->
            -*- Maintain a devtmpfs filesystem to mount at /dev
            [*]   Automount devtmpfs at /dev, after the kernel mounted the rootfs
        [*] PCI support  --->
            PCI controller drivers  --->
                <*> Generic PCI host controller
        NVME Support  --->
            <*> NVM Express block device
            [*] NVMe multipath support
        Firmware Drivers  --->
            [*] ARM Software Delegated Exception Interface (SDEI)
            [*] Export DMI identification via sysfs to userspace
            <M> DMI table support in sysfs
            <M> Arm Firmware Framework for Armv8-A
            [*] ARM PSCI checker
            EFI (Extensible Firmware Interface) Support  --->
                [*] Enable the generic EFI decompressor
                [*] Load custom ACPI SSDT overlay from an EFI variable
        [*] SPI support  --->
            <*>   Cadence SPI controller
        PHY Subsystem  --->
            -*- PHY Core
            <M> Cadence Torrent PHY driver
            <M> Cadence D-PHY Support
            <M> Cadence D-PHY Rx Support
            <M> Cadence Sierra PHY Driver
            <M> Cadence Salvo PHY Driver
    File systems  --->
        -*- The Extended 4 (ext4) filesystem
        [*]   Use ext4 for ext2 file systems
        -*-   Ext4 POSIX Access Control Lists
        -*-   Ext4 Security Labels
        <M> FUSE (Filesystem in Userspace) support
        <M>   Character device in Userspace support
        <M>   Virtio Filesystem
            [*]     Virtio Filesystem Direct Host Memory Access support (NEW)
        [*]   FUSE passthrough operations support (NEW)
        DOS/FAT/EXFAT/NT Filesystems  --->
            <*> MSDOS fs support
            <*> VFAT (Windows-95) fs support
            <*> exFAT filesystem support
             NTFS Read-Write file system support
            <M> NTFS file system support
        Pseudo filesystems  --->
        -*- /proc file system support
        -*- Tmpfs virtual memory file system support (former shm fs)
    -*- Enable the block layer  --->
        Partition Types  --->
            [*] Advanced partition selection
            [*]   EFI GUID Partition support

#### [Power Management]

** Note**\
Battery level and lid control require EC driver, which is out of tree; CPU frequency scaling and governor are provided by ARM SCMI/SCPI, but does not work for reasons currently unknown.

[KERNEL] **Power Management Options**

    Power management options  --->
        [*] Suspend to RAM and standby
        [ ]   Skip kernel's sys_sync() on suspend to RAM/standby
        [ ] Hibernation (aka 'suspend to disk')
        [ ] Opportunistic sleep
        [ ] Userspace opportunistic sleep
        [*] User space wakeup sources interface
            (100) Maximum number of user space wakeup sources (0 = no limit) (NEW)
            [*]   Garbage collector for user space wakeup sources (NEW)
        -*- Device power management core functionality
        [*] Energy Model for devices with DVFS (CPUs, GPUs, etc)
    [*] ACPI (Advanced Configuration and Power Interface) Support  --->
        [*]   ACPI Firmware Performance Data Table (FPDT) support
        <*>   EC read/write access through /sys/kernel/debug/ec
        <*>   AC Adapter
        <*>   Battery
        <*>   Button
           Video
        <*>   Fan
        <*>   ACPI Time and Alarm (TAD) Device Support
        <*>   Processor
        <*>   Thermal Zone
        [*]   Allow upgrading ACPI tables via initrd
        [*]   PCI slot detection driver
        [*]   Platform Runtime Mechanism Support
        [*]   ACPI PCC Address Space
        [*]   ACPI FFH Address Space
    CPU Power Management  --->
        CPU Idle  --->
            -*- CPU idle PM support
            ARM CPU Idle Drivers  --->
                [*] PSCI CPU idle Driver
                [*]   PSCI CPU idle Domain
        CPU Frequency scaling  --->
            [*] CPU Frequency scaling
            [*]   CPU frequency transition statistics
            Default CPUFreq governor (ondemand)  --->
            -*-   'performance' governor
            <*>   'powersave' governor
            <*>   'userspace' governor for userspace frequency scaling
            -*-   'ondemand' cpufreq policy governor
            <*>   'conservative' cpufreq governor
            [*]   'schedutil' cpufreq policy governor
            *** CPU frequency scaling drivers ***
            < >   Generic DT based cpufreq driver
            [ ]   Generic DT based cpufreq platdev driver
            <*>   SCMI based CPUfreq driver
            <*>   CPUFreq driver based on the ACPI CPPC spec
            [*]     Frequency Invariance support for CPPC cpufreq driver (NEW)
    Device Drivers  --->
        Firmware Drivers --->
            ARM System Control and Management Interface Protocol --->
                <*> ARM System Control and Management Interface (SCMI) Message Protocol
                [*] Enable support for SCMI Raw transmission mode
                [*] Allow SCMI Raw mode coexistence with normal SCMI stack
                [*] Enable SCMI communication debug metrics tracking
                SCMI Transport Drivers --->
                    <*> SCMI transport base on Mailbox
                    <*> SCMI transport base on SMC
                    [*] Enable atomic mode support for SCMI SMC transport
                    <*> SCMI transport based on OP-TEE service
                    < > SCMI transport based on VirtIO
                <*> SCMI system power control driver
            <*> ARM System Control and Power Interface (SCPI) Message Protocol
        -*- Thermal drivers  --->
        [*]   Thermal netlink management
        [*]   Thermal state transition statistics
        [ ]   Thermal subsystem debug support
            (0)   Emergency poweroff delay in milli-seconds
        [ ]   APIs to parse thermal data out of device tree
            Default Thermal governor (step_wise)  --->
        [*]   Fair-share thermal governor
        -*-   Step_wise thermal governor
        [*]   Bang Bang thermal governor
        [*]   User_space thermal governor
        [*]   Power allocator thermal governor
        [*]   Generic device cooling support
        [ ]   Thermal emulation mode support
        <*>   Generic Thermal MMIO driver
        < >   Temperature sensor driver for Maxim MAX77620 PMIC
        PM Domains --->
            <*> SCMI performance domain driver
            <*> SCMI power domain driver
            <*> SCPI power domain driver
        Generic powercap sysfs driver --->
            [*] Idle injection framework
            <*> ARM SCMI Powercap driver

#### [USB Support]

[KERNEL] **USB Support**

    Device Drivers  --->
        [*] HID bus support  --->
        -*-   HID bus core support
        [*]     Battery level reporting for HID devices
        [*]     /dev/hidraw raw HID device support
        <*>     Generic HID driver
        USB HID support  --->
            <*> USB HID transport layer
            [*] PID device support
            [*] /dev/hiddev raw HID device support

        [*] USB support  --->
            [*]   PCI based USB host interface
            <M>   USB Mass Storage support
            <M>     USB Attached SCSI
            <*>   xHCI HCD (USB 3.0) support
            <*>   EHCI HCD (USB 2.0) support
            [*]     Root Hub Transaction Translators
            <*>   OHCI HCD (USB 1.1) support
            <M>   USB Type-C Support  --->
                <M>   USB Type-C Port Controller Manager
                <M>     Type-C Port Controller Interface driver
                <M>   USB Type-C Connector System Software Interface driver
                <M>     UCSI ACPI Interface Driver

#### [][Keyboard & Trackpad]

** Note**\
Besides these options, built-in keyboard and trackpad requires out-of-tree kernel module to function.

[KERNEL] **Keyboard & Trackpad**

    Device Drivers  --->
            Input device support  --->
                -*- Generic input layer (needed for keyboard, mouse, ...)
                [*]   Keyboards  --->
                    <M>   AT keyboard
                [*]   Mice  --->
                    <*>   PS/2 mouse
                    [*]     Logitech PS/2++ mouse protocol extension
                    [*]   Miscellaneous devices  --->
                        <M>   Windows-compatible SoC Button Array

#### [WLAN]

[KERNEL] **WLAN**

    -*- Networking support  --->
        -*-   Wireless  --->
            <M>   cfg80211 - wireless configuration API
            [*]     nl80211 testmode command
            [*]     enable powersave by default
            [*]     cfg80211 DebugFS entries
            [*]     support CRDA
            [*]     cfg80211 wireless extensions compatibility
            <M>   Generic IEEE 802.11 Networking Stack (mac80211)
            [*]   Minstrel
                Default rate control algorithm (Minstrel)  --->
            [*]   Enable mac80211 mesh networking support
            [*]   Export mac80211 internals in DebugFS
        <M>   RF switch subsystem support  --->
            [*]   RF switch input support
            <M>   GPIO RFKILL driver
        Device Drivers  --->
            [*] Network device support  --->
                [*]   Network core driver support
                [*]   Wireless LAN  --->
                    [*]   Realtek devices
                    <M>     Realtek 802.11ac wireless chips support  --->
                        <M>   Realtek 8821CE PCI wireless network adapter

#### [Webcam]

** Note**\
This step could be easily forgotten by users unfamiliar with this unit, as if the kill switch of the camera is not switched on, the camera will be disconnected from the USB bus and tricking the user into thinking the kernel configuration is problematic / hardware failure.

** Tip**\
A red LED will turn on once the kill switch of the camera has been turned on, no matter if the camera has actually been accessed. This LED is not programmatically controllable.

[KERNEL] **Enable USB Video Class for Webcam**

    Device Drivers  --->
        <M> Multimedia support  --->
            [*]   Autoselect ancillary drivers (tuners, sensors, i2c, spi, frontends)
            Media device types  --->
                [*] Cameras and video grabbers
            Media drivers  --->
                [*] Media USB Adapters  --->
                    <M>   USB Video Class (UVC)
                    [*]     UVC input events device support

#### [GPU]

Reference to [AMDGPU](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU").

#### [Sound]

** Note**\
Internal speaker will not work as no driver is available for the built-in sound card.

Reference to [ALSA](https://wiki.gentoo.org/wiki/ALSA "ALSA").

#### [Bluetooth]

Reference to [Bluetooth](https://wiki.gentoo.org/wiki/Bluetooth "Bluetooth"). The Bluetooth adapter firmware requires [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]].

### [Alternative: Using NeoKylin Kernel]

Using the kernel and kernel modules from NeoKylin will easily solve CPU governor, keyboard, trackpad, EC, and audio issues, as this device has been certified to be compatible with NeoKylin.

** Tip**\
A full installation of NeoKylin will bundle kernel configuration file that used to build the kernel under `/boot`. This could be used as a startpoint to configure and compile Gentoo kernel, despite this configuration is not well optimized.

Acquire NeoKylin kernel from NeoKylin rootfs, either of a NeoKylin LiveCD or full installation, and copy it into places:

`root `[`#`]`cp $/vmlinuz-$-generic /boot/vmlinuz-$-generic`

`root `[`#`]`cp -r $/lib/modules/$-generic /lib/modules/$-generic`

Then rengenrate initramfs and grub configuration:

** Note**\
The following command use [dracut] and [grub] for example. If preferring other ways of generating initramfs and/or bootloaders, check out the corresponding articles.

`root `[`#`]`dracut --kver $-generic && grub-mkconfig -o /boot/grub/grub.cfg`

#### [Optional: reinstalling linux-firmware]

[[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] has to be reinstalled without USE flag `compress-zstd` if formerly enabled, as NeoKylin kernel didn\'t enable ZSTD-compressed firmware support (till the last edit of this article).

[FILE] **`/etc/portage/package.use/linux-firmware`Disabling compress-zstd USE flag**

    sys-kernel/linux-firmware -compress-zstd

`root `[`#`]`emerge -av linux-firmware`

#### [Optional: Suppressing Oddball Kernel Messages]

NeoKylin kernel may generate oddball kernel messages such as `Authorization binary is corrupted, please call xxx-xxx-xxxx for help` or `denied  for pid 1 comm='systemd' name='/usr/lib/systemd/systemd'...` . These are due to missing userland executables for [Kysec], a security measure in NeoKylin kernel. These executables aren\'t actually being blocked from executing, but could be annoying while reading the output of [dmesg] for debugging purposes.

The kernel parameter `security=` could be passed to the kernel on boot to disable [Kysec] to suppress these kernel messages.

** Important**\
Not recommended to add this parameter to [GRUB_CMDLINE_LINUX_DEFAULT] if multibooting with other kernels/distros as this could accidentally disable security measures in them such as [AppArmor](https://wiki.gentoo.org/wiki/AppArmor "AppArmor").

### [Emerge]

#### [][Keyboard & Mouse]

The built-in keyboard and trackpad use the PS/2 protocol and an Intel 8042-compatible interface, which is not supported by the mainline Linux kernel on ARM. A modded `i8042` kernel module called `ft8042` is required. This module could be acquired from [ATZLinux Kernel project](https://gitee.com/atzlinux/atzlinux-kernel/tree/master/drivers/input/serio/ft8042), but required patching to compile on Linux kernel 6.12 .

A patched version made by the author of this article could be found at [here](https://github.com/Randname666/ft8042).

** Important**\
Currently, this poorly patched kernel module would result in IRQ#28 being disabled on boot due to mishandling. This could result in undesired consequences. The author doesn\'t have enough understanding about kernel programming to solve this issue; your help is much appreciated.

** Note**\
Scroll wheel events generated by double-finger sliding on the touchpad are globally reverted: sliding up sends a scroll wheel down event and vice versa. Some desktop environments would have the option to revert scroll direction again but TUI programs would still be affected.

#### [][Embedded Controller (EC)]

The EC requires a platform-specific driver `gwnb_power` to function. This could be acquired from [ATZLinux Kernel project](https://gitee.com/atzlinux/atzlinux-kernel/tree/master/drivers/power/supply/gw-nb-ec).

#### [Sound]

Built-in audio is provided by PhyHDA, which is probably wrapped/rebranded/modified Realtek Audio.

The driver for this sound card is out-of-tree, way too broken, and may require extensive effort to adapt to Linux kernel 6.12+.

#### [Linux-firmware]

Bluetooth and GPU require [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]].

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

## [Configuration]

### [Optional: Capping CPU Frequency]

As the CPU frequency scaling is not functional, the CPU frequency may be capped in UEFI setup to reduce heat and battery consumption, if no demanding tasks will be performed.

Press [Delete] on boot to enter UEFI setup.

[CODE] **Capping CPU frequency**

    Device Manager ->
        CPU Configuration ->
            CPU SPEED <2200MHz>

### [Optional: Change the CPU governor]

NeoKylin kernel is compiled with [Performance] set as default governor. It could be changed to other governors in order to reduce heat and battery consumption.

Reference to [Power management/Processor#Manual governor/driver change](https://wiki.gentoo.org/wiki/Power_management/Processor#Manual_governor.2Fdriver_change "Power management/Processor") and [Power management/Guide#Using Laptop Mode Tools](https://wiki.gentoo.org/wiki/Power_management/Guide#Using_Laptop_Mode_Tools "Power management/Guide").

## [External resources]

-   [Phytium Processor](https://www.phytium.com.cn/en/index/)
-   [NeoKylin](https://kylinos.cn/)
-   [ATZLinux](https://www.atzlinux.com/)