[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**Resources**

[[]][Home](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-s-series-laptops/thinkpad-s440)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_S440/ThinkPad_S440_Spec.PDF)

[[]][Specifications (by region)](https://psref.lenovo.com/Product/ThinkPad/ThinkPad_S440)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/ibmdl/pub/pc/pccbbs/mobiles_pdf/s440_hmm_en.pdf)

[[]][User Guide](https://download.lenovo.com/ibmdl/pub/pc/pccbbs/mobiles_pdf/s440_ug_en.pdf)

[[]][BIOS Setup](https://download.lenovo.com/pccbbs/mobiles_pdf/lenovo_bios_setup_linux_wmi_sysfs_1.2.pdf)

## Contents

-   [[1] [About ThinkPad S440]](#About_ThinkPad_S440)
-   [[2] [BIOS]](#BIOS)
-   [[3] [Leaving Microsoft Windows Installed]](#Leaving_Microsoft_Windows_Installed)
-   [[4] [Hardware Support Status]](#Hardware_Support_Status)
    -   [[4.1] [ACPI - Power Management]](#ACPI_-_Power_Management)
    -   [[4.2] [ACPI - Sound Management]](#ACPI_-_Sound_Management)
    -   [[4.3] [Hardware List]](#Hardware_List)
-   [[5] [Configuration details]](#Configuration_details)
    -   [[5.1] [Compiler flags]](#Compiler_flags)
    -   [[5.2] [Kernel Configuration]](#Kernel_Configuration)
        -   [[5.2.1] [Wireless LAN]](#Wireless_LAN)
        -   [[5.2.2] [MMC/SD Card Reader]](#MMC.2FSD_Card_Reader)
    -   [[5.3] [Required packages]](#Required_packages)
    -   [[5.4] [Sound]](#Sound)
    -   [[5.5] [External resources]](#External_resources)

# [About ThinkPad S440]

The Lenovo Thinkpad S440 was sold with optional touchscreen and optional ATI graphic card in addition to a standard intel graphic card. This entry is based on a non-touch model with the standard intel graphic card only.

Lenovo stopped selling the Lenovo ThinkPad S440 model [\[1\]](http://shop.lenovo.com/gb/en/laptops/thinkpad/s-series/s440/)

# [BIOS]

The Lenovo Thinkpad S440 has BIOS settings you probably want to adapt when deploying Linux on it. [Download the user manual (Third Edition, published Jan. 2015)](http://download.lenovo.com/ibmdl/pub/pc/pccbbs/mobiles_pdf/s440_ug_en.pdf) and have it at hand to understand the settings and their various option values. In the manual, go to *Using the ThinkPad Setup program* where a table of BIOS options can be found. BIOS settings which might be required for a successful install and can be found in the table below:

  --------------------- ------------------------------------ -------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Menu item             Submenu item                         Selection            Explainations
  Intel Smart Connect                                        Disabled             This function is not documented in the manual! [Intel Smart Connect](http://www.intel.com/content/www/us/en/architecture-and-technology/smart-connect-technology.html) periodically fetches mail, social network messages and runs cloud synchronization while the computer is in standby. There are reports that this function leads to unwanted wake-up from power-safe modes.
  USB                   USB UEFI BIOS Support                Enabled (default)    Keep on \"Enable\" if you plan to install Gentoo from USB stick.
  Virtualization        Intel(R) Virtualization Technology   Disabled (default)   Enable this if you want to run virual machines.
  Virtualization        Intel VT-d Feature                   Disabled (default)   Enable this if you want to run virual machines (and utilize I/O virtualization).
  Anti-Theft            Intel AT Module Activation           Disabled             [Intel® Anti-Theft Service will be terminated by the end of January 2015.](http://www.intel.com/content/www/us/en/architecture-and-technology/anti-theft/anti-theft-general-technology.html)
  Anti-Theft            Computrace                           Disabled             [Computrace is an optional monitoring service from Absolute Software.](https://www.absolute.com/en/products/absolute-computrace)
  Secure Boot           Secure Boot                          Disabled (default)   Required to boot \"unauthorized operating systems\" (a.k.a. Linux)
  UEFI/Legacy Boot                                           UEFI Only            Use this setting to make 100% sure UEFI is used to avoid future confusion.
  UEFI/Legacy Boot      CSM Support                          No                   [Prevents booting from MBR-partitioned disks](https://en.wikipedia.org/wiki/Unified_Extensible_Firmware_Interface#CSM_booting "wikipedia:Unified Extensible Firmware Interface") because its successor, the [GUID Partition Table (GPT)](https://en.wikipedia.org/wiki/GUID_Partition_Table "wikipedia:GUID Partition Table") should be used. If you have trouble booting the installation medium temporarily set this to **Yes**.
  Boot Mode                                                  Diagnostics          Verbose boot process.
  --------------------- ------------------------------------ -------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# [Leaving Microsoft Windows Installed]

Lenovo\'s ThinkPad S440 comes with M\$ Windows (8.1 or 7) pre-installed. I recommend to keep M\$ Windows installed because

-   firmware or BIOS updates usually require M\$ Windows (on their download site they offer Linux based tools too, so there is hope)
-   it comes in handy for troubleshooting sometimes
-   no M\$ Windows install medium comes with the laptop. Therefore, [reinstalling Windows is tiresome](http://forums.lenovo.com/t5/Lenovo-U-and-S-Series-Notebooks/Windows-8-Installation-Replace-Hard-Disk/td-p/1105875).

Lenovo\'s official download website for ThinkPad S440 is [here](http://support.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-s-series-laptops/thinkpad-s440).

If Gentoo was installed in dual-boot configuration with M\$ the partition table should look similar(!) to this. Comments (marked by #) were added manually by me.

`root `[`#`]`parted -l`

    Model: ATA SAMSUNG MZ7TE128 (scsi)
    Disk /dev/sda: 128GB
    Sector size (logical/physical): 512B/512B
    Partition Table: gpt
    Disk Flags:
    Number  Start   End     Size    File system  Name                          Flags         # Label
     1      1049kB  1050MB  1049MB  ntfs                                       hidden, diag  # WINRE_DRV
     2      1050MB  1322MB  273MB   fat32        EFI system partition          boot, esp     # SYSTEM_DRV
     3      1322MB  1456MB  134MB                Microsoft reserved partition  msftres
     4      1456MB  33.8GB  32.4GB  ntfs         Basic data partition          msftdata      # Windows8_OS
     6      33.8GB  46.9GB  13.1GB  ext4                                                     # Linux Mint
     7      46.9GB  107GB   60.3GB  ext4                                                     # Gentoo
     5      107GB   128GB   20.8GB  ntfs                                       hidden, diag  # Lenovo_Recovery

Don\'t swipe the [Microsoft reserved partition](https://en.wikipedia.org/wiki/Microsoft_Reserved_Partition "wikipedia:Microsoft Reserved Partition")!

# [Hardware Support Status]

## [ACPI - Power Management]

  ----------------------------- ------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Function**                  **Works?**   **Note**
  Suspend to RAM                Yes          see [Suspend_and_hibernate](https://wiki.gentoo.org/wiki/Suspend_and_hibernate "Suspend and hibernate")
  Suspend to disk (hibernate)   Untested
  Display backlight control     Yes          see [ACPI/ThinkPad-special-buttons#Backlight_control](https://wiki.gentoo.org/wiki/ACPI/ThinkPad-special-buttons#Backlight_control "ACPI/ThinkPad-special-buttons")
  Keyboard backlight control    Yes          Fn + Space
  ----------------------------- ------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [ACPI - Sound Management]

If the special keys are not working, the following modifications, based on [ACPI](https://wiki.gentoo.org/wiki/ACPI "ACPI") and [ACPI/ThinkPad-special-buttons](https://wiki.gentoo.org/wiki/ACPI/ThinkPad-special-buttons "ACPI/ThinkPad-special-buttons"), are suggested:

[FILE] **`/etc/acpi/events/FnF1-mute`Enabling the mute function key**

    event=button/mute
    action=/etc/acpi/actions/FnF1-mute.sh

[FILE] **`/etc/acpi/events/FnF2-volumedown`Enabling the volume down function key**

    event=button/volumedown
    action=/etc/acpi/actions/FnF2-volumedown.sh

[FILE] **`/etc/acpi/events/FnF3-volumeup`Enabling the volume up function key**

    event=button/volumeup
    action=/etc/acpi/actions/FnF3-volumeup.sh

[FILE] **`/etc/acpi/actions/FnF1-mute.sh`Enabling the mute function key**

    #!/bin/sh
    amixer -q set Master toggle

[FILE] **`/etc/acpi/actions/FnF2-volumedown.sh`Enabling the volume down function key**

    #!/bin/sh
    amixer -q set Master 3dB-

[FILE] **`/etc/acpi/actions/FnF3-volumeup.sh`Enabling the volume up function key**

    #!/bin/sh
    amixer -q set Master 3dB+

`root `[`#`]`chmod +x /etc/acpi/actions/FnF1-mute.sh /etc/acpi/actions/FnF2-volumedown.sh /etc/acpi/actions/FnF3-volumeup.sh `

`root `[`#`]`/etc/init.d/acpid restart`

## [Hardware List]

`root `[`#`]`lspci -nnk`

    00:00.0 Host bridge [0600]: Intel Corporation Haswell-ULT DRAM Controller [8086:0a04] (rev 0b)
            Subsystem: Lenovo Device [17aa:501c]
    00:02.0 VGA compatible controller [0300]: Intel Corporation Haswell-ULT Integrated Graphics Controller [8086:0a16] (rev 0b)
            Subsystem: Lenovo Device [17aa:501c]
            Kernel driver in use: i915
    00:03.0 Audio device [0403]: Intel Corporation Haswell-ULT HD Audio Controller [8086:0a0c] (rev 0b)
            Subsystem: Lenovo Device [17aa:501c]
            Kernel driver in use: snd_hda_intel
    00:14.0 USB controller [0c03]: Intel Corporation 8 Series USB xHCI HC [8086:9c31] (rev 04)
            Subsystem: Lenovo Device [17aa:501c]
            Kernel driver in use: xhci_hcd
    00:16.0 Communication controller [0780]: Intel Corporation 8 Series HECI #0 [8086:9c3a] (rev 04)
            Subsystem: Lenovo Device [17aa:501c]
    00:1b.0 Audio device [0403]: Intel Corporation 8 Series HD Audio Controller [8086:9c20] (rev 04)
            Subsystem: Lenovo Device [17aa:501c]
            Kernel driver in use: snd_hda_intel
    00:1c.0 PCI bridge [0604]: Intel Corporation 8 Series PCI Express Root Port 1 [8086:9c10] (rev e4)
            Kernel driver in use: pcieport
    00:1c.1 PCI bridge [0604]: Intel Corporation 8 Series PCI Express Root Port 2 [8086:9c12] (rev e4)
            Kernel driver in use: pcieport
    00:1c.2 PCI bridge [0604]: Intel Corporation 8 Series PCI Express Root Port 3 [8086:9c14] (rev e4)
            Kernel driver in use: pcieport
    00:1c.3 PCI bridge [0604]: Intel Corporation 8 Series PCI Express Root Port 4 [8086:9c16] (rev e4)
            Kernel driver in use: pcieport
    00:1d.0 USB controller [0c03]: Intel Corporation 8 Series USB EHCI #1 [8086:9c26] (rev 04)
            Subsystem: Lenovo Device [17aa:501c]
            Kernel driver in use: ehci-pci
    00:1f.0 ISA bridge [0601]: Intel Corporation 8 Series LPC Controller [8086:9c43] (rev 04)
            Subsystem: Lenovo Device [17aa:501c]
            Kernel driver in use: lpc_ich
            Kernel modules: lpc_ich
    00:1f.2 SATA controller [0106]: Intel Corporation 8 Series SATA Controller 1 [AHCI mode] [8086:9c03] (rev 04)
            Subsystem: Lenovo Device [17aa:501c]
            Kernel driver in use: ahci
    00:1f.3 SMBus [0c05]: Intel Corporation 8 Series SMBus Controller [8086:9c22] (rev 04)
            Subsystem: Lenovo Device [17aa:501c]
    03:00.0 Ethernet controller [0200]: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller [10ec:8168] (rev 10)
            Subsystem: Lenovo Device [17aa:501c]
            Kernel driver in use: r8169
    04:00.0 Network controller [0280]: Intel Corporation Wireless 7260 [8086:08b2] (rev 83)
            Subsystem: Intel Corporation Dual Band Wireless-AC 7260 [8086:4270]
            Kernel driver in use: iwlwifi
            Kernel modules: iwlwifi
    05:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS5227 PCI Express Card Reader [10ec:5227] (rev 01)
            Subsystem: Lenovo Device [17aa:501c]
            Kernel driver in use: rtsx_pci
            Kernel modules: rtsx_pci

`root `[`#`]`lsusb`

    Bus 003 Device 002: ID 8087:8000 Intel Corp.
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 004: ID 138a:0011 Validity Sensors, Inc. VFS5011 Fingerprint Reader
    Bus 001 Device 003: ID 0bda:5720 Realtek Semiconductor Corp.
    Bus 001 Device 002: ID 8087:07dc Intel Corp.
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

# [Configuration details]

## [Compiler flags]

*Main article: [Safe CFLAGS](https://wiki.gentoo.org/wiki/Safe_CFLAGS "Safe CFLAGS")*

[FILE] **`/etc/portage/make.conf`compuler flags**

    CFLAGS="-O2 -pipe -march=native"
    CXXFLAGS="$"

\

[FILE] **`/etc/portage/package.use/00grub`**

    */*  GRUB_PLATFORMS: efi-64

[FILE] **`/etc/portage/package.use/00input`**

    */* INPUT_DEVICES: libinput evdev synaptics

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* intel i965

[FILE] **`/etc/portage/package.use/00cpu-flags`**

    */*  CPU_FLAGS_X86: aes avx avx2 fma3 mmx mmxext popcnt sse sse2 sse3 sse4_1 sse4_2 ssse3

## [Kernel Configuration]

### [Wireless LAN]

In case you followed [Wifi](https://wiki.gentoo.org/wiki/Wifi "Wifi"), it is sufficient to enable `MVM Firmare support` only. MVM supports Intel 7260 (which is built into this model) and 3160 devices, while `DVM Firmware support` supports all other Intel devices.

[KERNEL]

        Device Drivers  --->
        [*] Network device support  --->
            [*] Wireless LAN  --->
                <M>   Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)
                    < >     Intel Wireless WiFi DVM Firmware support
                    <M>     Intel Wireless WiFi MVM Firmware support

### [][MMC/SD Card Reader]

In order to use the MMC/SD card reader (the slot is on the left hand side of the notebook) you need to enable the respective drivers in the kernel config.

[KERNEL]

        Device Drivers  --->
        <*> MMC/SD/SDIO card support  --->
            <*> MMC block device driver
            <M> Realtek PCI-E SD/MMC Card Interface Driver

## [Required packages]

-   [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]]

## [Sound]

It may be that sound does not work out of the box. This is caused by the order in which the kernel modules are loaded and the fact that there is a HDMI and PCH sound card in the laptop.

First, test if the PCH sound card is functional. Get a list of all PCM devices

`root `[`linux #`]`aplay -L`

    null
        Discard all samples (playback) or generate zero samples (capture)
    default:CARD=PCH
        HDA Intel PCH, ID 510f Analog
        Default Audio Device
    sysdefault:CARD=PCH
        HDA Intel PCH, ID 510f Analog
        Default Audio Device
    front:CARD=PCH,DEV=0
        HDA Intel PCH, ID 510f Analog
        Front speakers
    surround21:CARD=PCH,DEV=0
        HDA Intel PCH, ID 510f Analog
        2.1 Surround output to Front and Subwoofer speakers
    surround40:CARD=PCH,DEV=0
        HDA Intel PCH, ID 510f Analog
        4.0 Surround output to Front and Rear speakers
    surround41:CARD=PCH,DEV=0
        HDA Intel PCH, ID 510f Analog
        4.1 Surround output to Front, Rear and Subwoofer speakers
    surround50:CARD=PCH,DEV=0
        HDA Intel PCH, ID 510f Analog
        5.0 Surround output to Front, Center and Rear speakers
    surround51:CARD=PCH,DEV=0
        HDA Intel PCH, ID 510f Analog
        5.1 Surround output to Front, Center, Rear and Subwoofer speakers
    surround71:CARD=PCH,DEV=0
        HDA Intel PCH, ID 510f Analog
        7.1 Surround output to Front, Center, Side, Rear and Woofer speakers
    hdmi:CARD=HDMI,DEV=0
        HDA Intel HDMI, HDMI 0
        HDMI Audio Output
    hdmi:CARD=HDMI,DEV=1
        HDA Intel HDMI, HDMI 1
        HDMI Audio Output

Next, test sound output (you should hear noise):

`root `[`#`]`aplay -Ddefault:CARD=PCH /usr/share/sounds/alsa/Noise.wav`

    Playing WAVE '/usr/share/sounds/alsa/Noise.wav' : Signed 16 bit Little Endian, Rate 48000 Hz, Mono

Finally follow the advice given in [ALSA#HTML5_does_not_play_in_firefox_browser](https://wiki.gentoo.org/wiki/ALSA#HTML5_does_not_play_in_firefox_browser "ALSA") and

[FILE] **`/etc/default/grub`swapping sound card order**

    ...
    # change load order sound cards
    GRUB_CMDLINE_LINUX_DEFAULT="snd-hda-intel.index=1,0"
    ...

Reconfigure and reinstall grub and reboot to make the change effective.

## [External resources]

-   [https://wiki.archlinux.org/title/Lenovo_ThinkPad_S440](https://wiki.archlinux.org/title/Lenovo_ThinkPad_S440)