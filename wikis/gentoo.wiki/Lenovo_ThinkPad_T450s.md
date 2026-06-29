**Resources**

[[]][Home](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-t-series-laptops/thinkpad-t450s)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_T450s/ThinkPad_T450s_Spec.PDF)

[[]][Specifications (by region)](https://psref.lenovo.com/Product/ThinkPad/ThinkPad_T450s)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/pccbbs/mobiles_pdf/t450s_hmm_en_sp40g54937_01.pdf)

[[]][User Guide](https://download.lenovo.com/pccbbs/mobiles_pdf/t450s_ug_en.pdf)

[[]][ThinkPad T series](https://en.wikipedia.org/wiki/ThinkPad_T_series "wikipedia:ThinkPad T series")

This article describes hardware specific setup steps for the Lenovo ThinkPad T450s on Gentoo.

## Contents

-   [[1] [Hardware]](#Hardware)
-   [[2] [Installation]](#Installation)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [CPU]](#CPU)
    -   [[3.2] [Kernel modules]](#Kernel_modules)
        -   [[3.2.1] [ACPI]](#ACPI)
        -   [[3.2.2] [Hardware monitoring]](#Hardware_monitoring)
        -   [[3.2.3] [Video card]](#Video_card)
        -   [[3.2.4] [Ethernet controller]](#Ethernet_controller)
        -   [[3.2.5] [Wireless controller]](#Wireless_controller)
        -   [[3.2.6] [Integrated camera]](#Integrated_camera)
        -   [[3.2.7] [Audio device]](#Audio_device)
        -   [[3.2.8] [EHCI controller]](#EHCI_controller)
        -   [[3.2.9] [xHCI controller]](#xHCI_controller)
        -   [[3.2.10] [MEI controller]](#MEI_controller)
        -   [[3.2.11] [PCI Express controller]](#PCI_Express_controller)
        -   [[3.2.12] [SATA controller]](#SATA_controller)
        -   [[3.2.13] [LPC controller]](#LPC_controller)
        -   [[3.2.14] [SMBus controller]](#SMBus_controller)
        -   [[3.2.15] [Host bridge]](#Host_bridge)
    -   [[3.3] [Hotkeys]](#Hotkeys)
-   [[4] [External resources]](#External_resources)

## [Hardware]

  ------------------------ ------------------------------------------------------------------------------ ------------- ------------------ ---------------- ------------------------------
  Device                   Make/model                                                                     Status        Kernel driver(s)   Kernel version   Notes
  CPU                      Intel(R) i7-5600U Processor (4M Cache, 2.6GHz)                                 Works         N/A                4.19.97,5.4.28   Microcode update recommended
  Video card               Intel Corporation HD Graphics 5500 (rev 09)                                    Works         i915               4.19.97,5.4.28   N/A
  Ethernet controller      Intel Corporation Ethernet Connection (3) I218-LM (rev 03)                     Works         e1000e             4.19.97,5.4.28   N/A
  Audio device             Intel Corporation Wildcat Point-LP High Definition Audio Controller (rev 03)   Works         snd_hda_intel      4.19.97,5.4.28   N/A
  Wireless controller      Intel Corporation Wireless 7265 (rev 99)                                       Works         iwlwifi            4.19.97,5.4.28   N/A
  SD card reader           Realtek Semiconductor Co., Ltd. RTS5227 PCI Express Card Reader (rev 01)       Not tested    rtsx_pci           4.19.97,5.4.28   N/A
  Integrated camera        Chicony Electronics                                                            Works         uvcvideo           4.19.97,5.4.28   N/A
  Fingerprint sensor       Validity Sensors, Inc. VFS 5011                                                Not tested    N/A                4.19.97,5.4.28   N/A
  EHCI controller          Intel Corporation Wildcat Point-LP USB EHCI Controller (rev 03)                Works         ehci_pci           4.19.97,5.4.28   N/A
  xHCI controller          Intel Corporation Wildcat Point-LP USB xHCI Controller (rev 03)                Works         xhci_pci           4.19.97,5.4.28   N/A
  MEI controller           Intel Corporation Wildcat Point-LP MEI Controller #1 (rev 03)                  Works         mei_me             4.19.97,5.4.28   N/A
  PCI Express controller   Intel Corporation Wildcat Point-LP PCI Express Root Port #3 (rev e3)           Works         pcieport           4.19.97,5.4.28   N/A
  SATA controller          Intel Corporation Wildcat Point-LP SATA Controller \[AHCI Mode\] (rev 03)      Works         ahci               4.19.97,5.4.28   N/A
  LPC controller           Intel Corporation Wildcat Point-LP LPC Controller (rev 03)                     Works         lpc_ich            4.19.97,5.4.28   N/A
  SMBus controller         Intel Corporation Wildcat Point-LP SMBus Controller (rev 03)                   Works         ic2_i801           4.19.97,5.4.28   N/A
  Host bridge              Intel Corporation Broadwell-U Host Bridge -OPI (rev 09)                        Works         bdw_uncore         4.19.97,5.4.28   N/A
  ------------------------ ------------------------------------------------------------------------------ ------------- ------------------ ---------------- ------------------------------

## [Installation]

It is a good idea to update to the latest BIOS available, check [the official page](https://support.lenovo.com/au/en/downloads/ds102109).

The installation procedure from a Gentoo installation media works perfectly as described [in the Handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Installation "Handbook:AMD64/Full/Installation").

Make sure to boot in **UEFI** mode (*BIOS, Startup, UEFI/Legacy Boot must be set to \[UEFI Only\]*) and follow the UEFI variants in the guide. [Genkernel](https://wiki.gentoo.org/wiki/Genkernel "Genkernel") should generate a working kernel with pretty much everything working out of the box.

To customize the kernel, the section below describes the needed modules.

** Important**\
If Grub doesn\'t pick up the configuration and it is stuck at boot, double check that the EFI file has been created and installed in the right place, i.e. [/boot/EFI/gentoo/grubx64.efi].

## [Configuration]

### [CPU]

It is recommended to enable the microcode update support as explained in [Intel microcode](https://wiki.gentoo.org/wiki/Intel_microcode "Intel microcode").

### [Kernel modules]

These sections contain only the specific portion needed to enable the device. Most of the drivers can be compiled as modules or built directly into the kernel, it is up to the reader to choose the preferred way of compilation.

#### [ACPI]

[KERNEL] **ACPI**

    Power management and ACPI options  --->
        [*] Suspend to RAM and stanby
        [*] Hibernation (aka 'suspend to disk')
        [*] ACPI (Advanced Configuration and Power Interface) Support  --->
            <*> AC Adapter
            <*> Battery
            <*> Button
             Video
            <*> Thermal Zone
            [*] Allow upgrading ACPI tables via initrd
            CPU Frequency scaling  --->
                [*] CPU Frequency scaling
                [*] Intel P state control
                (choose additional governor)
            [*] Cpuidle Driver for Intel Processors
    Device Drivers  --->
        [*] X86 Platform Specific Device Drivers  --->
            <M> ThinkPad ACPI Laptop Extras
            [*]   Console audio control ALSA interface
    [*] Networking support  --->
        <M> RF Switch subsystem support

#### [Hardware monitoring]

[KERNEL] **Hardware monitoring**

    Device Drivers  --->
        [*] X86 Platform Specific Device Drivers  --->
            <M> ThinkPad ACPI Laptop Extras
         Hardware Monitoring Support  --->
            <M> Intel Core/Core2/Atom temperature sensor

#### [Video card]

[KERNEL] **Video card**

    Device Drivers  --->
        Graphics support  --->
            <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support)
            <M> Intel 8xx/9xx/G3x/G4x/HD Graphics

#### [Ethernet controller]

[KERNEL] **Ethernet controller**

    Device Drivers  --->
        [*] Network device support  --->
            [*] Ethernet driver support  --->
                [*] Intel devices  --->
                [M] Intel(R) PRO/1000 PCI-Express Gigabit Ethernet support

#### [Wireless controller]

[KERNEL] **Wireless controller**

    -*- Wireless  --->
        [M] cfg80211 - wireless configuration API
        [M] Generic IEEE 802.11 Networking Stack (mac80211)
    Device Drivers  --->
        [*] Network device support  --->
            [*] Wireless LAN  --->
                [*] Intel devices
                [M] Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)
                [M] Intel Wireless WiFi MVM Firmware support

#### [Integrated camera]

[KERNEL] **Integrated camera**

    Device Drivers  --->
        [M] Multimedia support  --->
            [*] Media USB Adapters  --->
                [M] USB Video Class (UVC)

#### [Audio device]

[KERNEL] **Audio device**

    Device Drivers  --->
        [M] Source card support  --->
            [M] Advanced Linux Source Architecture  --->
                HD Audio  --->
                    [M] HD Audio PCI
                    [M] Build Realtek HD-audio codec support

#### [EHCI controller]

[KERNEL] **EHCI controller**

    [*] Networking support  --->
        <M> Bluetooth subsystem support  --->
            Bluetooth device drivers  --->
                <M> HCI USB driver
    Device Drivers  --->
        [*] USB support  --->
            [M] EHCI HCD (USB 2.0) support
            [*]     Root Hub Transaction Translators
            [*]     Improved Transaction Translator scheduling

#### [xHCI controller]

[KERNEL] **xHCI controller**

    Device Drivers  --->
        [*] USB support  --->
            [M] xHCI HCD (USB 3.0) support

#### [MEI controller]

[KERNEL] **MEI controller**

    Device Drivers  --->
        Misc devices  --->
             Intel Management Engine Interface
            [M] ME Enabled Intel Chipsets

#### [PCI Express controller]

[KERNEL] **PCI Express controller**

    Bus options (PCI etc.)  --->
        [*] PCI support
        [*] PCI Express Port Bus support

#### [SATA controller]

[KERNEL] **SATA controller**

    Device Drivers  --->
        <*> Serial ATA and Parallel ATA drivers (libata) --->
            [*] ATA ACPI Support
            [*] AHCI SATA support

#### [LPC controller]

[KERNEL] **LPC controller**

    Device Drivers  --->
        Multifunction device drivers --->
            <*> Intel ICH LPC

#### [SMBus controller]

[KERNEL] **SMBus controller**

    Device Drivers  --->
        I2C support --->
            I2C Hardware Bus support --->
                <*> Intel 82801 (ICH/PCH)

#### [Host bridge]

[KERNEL] **Host bridge**

    Processor type and features  --->
        Performance monitoring --->
            <*> Intel uncore performance events

### [Hotkeys]

If you have a recent BIOS installed all the Fn keys should work out of the box.

Bear in mind there\'s a BIOS option to alternate between standard F1-F12 functions and media functions: *BIOS, Config, Keyboard/Mouse, F1-F12 as Primary Function*.

## [External resources]

-   [https://wiki.archlinux.org/title/Lenovo_ThinkPad_T450(s)](https://wiki.archlinux.org/title/Lenovo_ThinkPad_T450(s))