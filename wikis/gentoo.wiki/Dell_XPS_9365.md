\
The *Dell XPS 13 (9365)* is a 2-in-1 convertible ultrabook released by Dell in early 2017 and has excellent Linux compatability with only minor outstanding issues: the fingerprint sensor is not supported. There is an [open issue](https://gitlab.freedesktop.org/libfprint/libfprint/issues/52) tracking progress.

## Contents

-   [[1] [Hardware]](#Hardware)
-   [[2] [Updating the BIOS]](#Updating_the_BIOS)
-   [[3] [UEFI Configuration]](#UEFI_Configuration)
-   [[4] [Portage Settings]](#Portage_Settings)
    -   [[4.1] [make.conf]](#make.conf)
-   [[5] [Kernel Configuration]](#Kernel_Configuration)

## [Hardware]

The following is a list of all PCI devices connected to the machine.

`root `[`#`]`lspci -k`

    00:00.0 Host bridge: Intel Corporation Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers (rev 02)
            Subsystem: Dell Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers
            Kernel driver in use: skl_uncore
    00:02.0 VGA compatible controller: Intel Corporation HD Graphics 615 (rev 02)
            DeviceName: Onboard IGD
            Subsystem: Dell HD Graphics 615
            Kernel driver in use: i915
            Kernel modules: i915
    00:04.0 Signal processing controller: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem (rev 02)
            Subsystem: Dell Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem
            Kernel driver in use: proc_thermal
            Kernel modules: processor_thermal_device
    00:13.0 Non-VGA unclassified device: Intel Corporation Sunrise Point-LP Integrated Sensor Hub (rev 21)
            Subsystem: Dell Sunrise Point-LP Integrated Sensor Hub
            Kernel driver in use: intel_ish_ipc
            Kernel modules: intel_ish_ipc
    00:14.0 USB controller: Intel Corporation Sunrise Point-LP USB 3.0 xHCI Controller (rev 21)
            Subsystem: Dell Sunrise Point-LP USB 3.0 xHCI Controller
            Kernel driver in use: xhci_hcd
            Kernel modules: xhci_pci
    00:14.2 Signal processing controller: Intel Corporation Sunrise Point-LP Thermal subsystem (rev 21)
            Subsystem: Dell Sunrise Point-LP Thermal subsystem
            Kernel driver in use: intel_pch_thermal
            Kernel modules: intel_pch_thermal
    00:15.0 Signal processing controller: Intel Corporation Sunrise Point-LP Serial IO I2C Controller #0 (rev 21)
            Subsystem: Dell Sunrise Point-LP Serial IO I2C Controller
            Kernel driver in use: intel-lpss
            Kernel modules: intel_lpss_pci
    00:15.1 Signal processing controller: Intel Corporation Sunrise Point-LP Serial IO I2C Controller #1 (rev 21)
            Subsystem: Dell Sunrise Point-LP Serial IO I2C Controller
            Kernel driver in use: intel-lpss
            Kernel modules: intel_lpss_pci
    00:16.0 Communication controller: Intel Corporation Sunrise Point-LP CSME HECI #1 (rev 21)
            Subsystem: Dell Sunrise Point-LP CSME HECI
            Kernel driver in use: mei_me
            Kernel modules: mei_me
    00:1c.0 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #1 (rev f1)
            Kernel driver in use: pcieport
    00:1c.4 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #5 (rev f1)
            Kernel driver in use: pcieport
    00:1d.0 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #9 (rev f1)
            Kernel driver in use: pcieport
    00:1d.1 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #10 (rev f1)
            Kernel driver in use: pcieport
    00:1f.0 ISA bridge: Intel Corporation Device 9d4b (rev 21)
            Subsystem: Dell Device 077a
    00:1f.2 Memory controller: Intel Corporation Sunrise Point-LP PMC (rev 21)
            Subsystem: Dell Sunrise Point-LP PMC
    00:1f.3 Audio device: Intel Corporation Sunrise Point-LP HD Audio (rev 21)
            Subsystem: Dell Sunrise Point-LP HD Audio
            Kernel driver in use: snd_hda_intel
            Kernel modules: snd_hda_intel, snd_soc_skl
    00:1f.4 SMBus: Intel Corporation Sunrise Point-LP SMBus (rev 21)
            Subsystem: Dell Sunrise Point-LP SMBus
            Kernel driver in use: i801_smbus
            Kernel modules: i2c_i801
    01:00.0 PCI bridge: Intel Corporation JHL6340 Thunderbolt 3 Bridge (C step) [Alpine Ridge 2C 2016] (rev 02)
            Kernel driver in use: pcieport
    02:00.0 PCI bridge: Intel Corporation JHL6340 Thunderbolt 3 Bridge (C step) [Alpine Ridge 2C 2016] (rev 02)
            Kernel driver in use: pcieport
    02:01.0 PCI bridge: Intel Corporation JHL6340 Thunderbolt 3 Bridge (C step) [Alpine Ridge 2C 2016] (rev 02)
            Kernel driver in use: pcieport
    02:02.0 PCI bridge: Intel Corporation JHL6340 Thunderbolt 3 Bridge (C step) [Alpine Ridge 2C 2016] (rev 02)
            Kernel driver in use: pcieport
    39:00.0 USB controller: Intel Corporation JHL6340 Thunderbolt 3 USB 3.1 Controller (C step) [Alpine Ridge 2C 2016] (rev 02)
            Subsystem: Dell JHL6340 Thunderbolt 3 USB 3.1 Controller (C step) [Alpine Ridge 2C 2016]
            Kernel driver in use: xhci_hcd
            Kernel modules: xhci_pci
    3a:00.0 Non-Volatile memory controller: Toshiba Corporation Device 0116
            Subsystem: Toshiba Corporation Device 0001
            Kernel driver in use: nvme
    3b:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS525A PCI Express Card Reader (rev 01)
            Subsystem: Dell RTS525A PCI Express Card Reader
            Kernel driver in use: rtsx_pci
            Kernel modules: rtsx_pci
    3c:00.0 Network controller: Intel Corporation Wireless 8265 / 8275 (rev 78)
            Subsystem: Intel Corporation Wireless 8265 / 8275
            Kernel driver in use: iwlwifi
            Kernel modules: iwlwifi

## [Updating the BIOS]

As of April 2020, the current version of the BIOS is 2.10.0. Instructions to update the system BIOS are as follows:

** Note**\
In this example, we will assume the EFI partition is at `/dev/nvme0n1p2` and that this partition is mounted to `/boot`. This may change based on the chosen partition layout chosen at the time of installation.

`user `[`$`]`lsblk --paths`

    NAME             MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
    /dev/nvme0n1     259:0    0 238.5G  0 disk
    ├─/dev/nvme0n1p1 259:1    0     8G  0 part [SWAP]
    ├─/dev/nvme0n1p2 259:2    0   500M  0 part /boot
    ├─/dev/nvme0n1p3 259:3    0    40G  0 part /
    └─/dev/nvme0n1p4 259:4    0    40G  0 part /home

1.  Download the latest version of the BIOS from the Dell support website [\[1\]](https://www.dell.com/support/home/ca/en/cabsdt1/drivers/).
2.  Copy the downloaded file to the **root** of the EFI System Partition.

    :::: cmd-box


    `root `[`#`]`cp XPS_9365_1_5_0.exe /boot/`


    ::::
3.  Reboot the system, pressing the F12 button when the *Dell* logo appears to enter the BIOS configuration menu.
4.  On the main menu of the UEFI screen, select the red **BIOS Update** button.
5.  You will be presented with the *Flash BIOS* menu. Select **Flash from file**.
6.  You will be prompted to select a file using a file browser. Select the EFI system partition that you copied the update file to, and select the update file.
7.  Once you have selected the correct BIOS update file, select the blue **Submit** option. You will be taken back to the previous *Flash BIOS* menu.
8.  After verifying that the correct BIOS update file has been selected, select **Update BIOS!**. You will be prompted with one last confirmation. Select **Confirm Update BIOS!**
9.  This step will take several minutes to flash the new BIOS. The system will reboot automatically when the process has completed. Once the system has finished rebooting, you may remove the BIOS update file from the EFI partition.

    :::: cmd-box


    `root `[`#`]`rm /boot/XPS_9365_1_5_0.exe`


    ::::
10. You can verify that the system is running the new BIOS by rebooting once again into the BIOS configuration menu (see step 3) and the version will be displayed in the top left corner, underneath the *Dell* logo and model. The version will read **BIOS Version 1.5.0**.

## [UEFI Configuration]

Some settings must be changed from the default UEFI settings in order for the system to function correctly.

## [Portage Settings]

### [make.conf]

The following are required or recommended settings for portage.

[FILE] **[`/etc/portage/make.conf`](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf")**

    #
    # make.conf
    #

    # compiler flags
    CHOST="x86_64-pc-linux-gnu"
    COMMON_FLAGS="-march=skylake -mtune=skylake -O2 -pipe"
    CFLAGS="$"
    CXXFLAGS="$"
    FCFLAGS="$"
    FFLAGS="$"
    CPU_FLAGS_X86="aes avx avx2 f16c fma3 mmx mmxext pclmul \
                   popcnt sse sse2 sse3 sse4_1 sse4_2 ssse3"

    # portage directories
    PORTDIR="/var/db/repos/gentoo"
    DISTDIR="/var/cache/distfiles"
    PKGDIR="/var/cache/binpkgs"

    # build output language
    LC_MESSAGES=C

    # emerge options
    MAKEOPTS="-j4"

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* intel i965

[FILE] **`/etc/portage/package.use/00input`**

    */* INPUT_DEVICES: libinput wacom

## [Kernel Configuration]

The following kernel configuration is based on the 4.17.10 Linux kernel, available from [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]]. This configuration is based on the default set of options, meaning any options not specified are assumed to be left as default.

** Note**\
A ready-to-go configuration file with based on the configuration below has been made available [here](https://gitlab.com/snippets/1738318).

[KERNEL]

    [*] Enable the block layer --->
        Partition Types --->
            [*] Advanced partition selection
                [*] PC BIOS (MSDOS partition tables) support
                [*] EFI GUID Partition support

    Processor type and features --->
        [*] Intel Low Power Subsystem Support
        [*] CPU microcode loading support
            [*] Intel microcode loading support
        [*] EFI runtime service support
            [*] EFI stub support ***TODO: IF STUB-LOADING NEEDED***
                [ ] EFI mixed-mode support

    Power management and ACPI options --->
        [*] Suspend to RAM and standby
        [*] Hibernation (aka 'suspend to disk')
        [*] ACPI (Advanced Configuration and Power Interface) Support --->
            <*> AC Adapter
            <*> Battery
            -*- Button
            -*- Video
            <*> Fan
            [*] Dock
            -*- Processor
            <*> Thermal Zone
        -*- CPU Frequency scaling --->
            Default CPUFreq governor (performance) --->
            -*- 'performance' governor
            <*> 'powersave' governor
            < > 'userspace' governor for userspace frequency scaling
            < > 'ondemand' cpufreq governor
            < > 'conservative' cpufreq governor
            [ ] 'schedutil' cpufreq governor
            -*- Intel P state control
            < > ACPI Processor P-States driver
        [*] Cpuidle Driver for Intel Processors

    Bus options (PCI etc.) --->
        [*] PCI support
        [*] PCI Express Port Bus support
        [*]     PCI Express Hotplug driver
        [*] Support for PCI Hotplug --->
            [*] ACPI PCI Hotplug driver
            [*] SHPC PCI Hotplug driver

    -*- Networking support --->
        -*- Wireless --->
        <*> Bluetooth subsystem support --->
            [*] Bluetooth Classic (BR/EDR) features
            <M>     RFCOMM protocol support
            <*>     HIDP protocol support
            [*]     Bluetooth High Speed (HS) features
            [*] Bluetooth Low Energy (LE) features
            Bluetooth device drivers --->
                <*> HCI USB driver

    Device Drivers --->
        NVME Support --->
            <*> NVM Express block device
        Misc devices --->
            <*> Realtek PCI-E card reader
        I2C support --->
            I2C Hardware Bus support --->
                <*> Intel 82801 (ISH/PCH)
        Network device support --->
            [*] Wireless LAN --->
                [*] Intel devices
                <M>     Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)
                < >         Intel Wireless WiFi DVM Firmware support
                <M>         Intel Wireless WiFi MVM Firmware support
        -*- Generic Thermal sysfs driver --->
            (0) Emergency poweroff delay in milli-seconds
            [*] Expose thermal sensors as hwmon device
            -*- Enable writable trip points
            Default Thermal governor (step_wise) --->
            [*] Fair-share thermal governor
            -*- Step_wise thermal governor
            [*] Bang Bang thermal governor
            -*- User_space thermal governor
            [ ] Thermal emulation mode support
            <M> Intel PowerClamp idle injection driver
            <M> X86 package temperature thermal driver
            < > Intel SoCs DTS thermal driver
            ACPI INT340X thermal drivers --->
                <*> ACPI INT340X thermal drivers
            <*> Intel PCH Thermal Reporting Driver
        Multifunction device drivers --->
            <*> Intel Low Power Subsystem support in PCI mode
        <*> Multimedia support --->
            [*] Cameras/video grabbers support
            [*] Media USB Adapters --->
                [*] USB Video Class (UVC)
            [*] Autoselect ancillary drivers (tuners, sensors, i2c, spi, frontends)
        Graphics support --->
            <*> /dev/agpart (AGP Support) --->
                < > AMD Opteron/Athlon64 on-CPU GART support
                <*> Intel 440LX/BX/GX, I8xx and E7x05 chipset support
                < > SiS chipset support
                < > VIA chipset support
            [ ] Laptop Hybrid Graphics - GPU switching support
            <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support) --->
                [*] Enable legacy fbdev support for your modesetting driver
                [ ] Allow to specify an EDID data set instead of probing for it
                < > ATI Radeon
                < > AMD GPU
                < > Nouveau (NVIDIA) cards
                <*> Intel 8xx/9xx/G3x/G4x/HD Graphics
                -*- Backlight & LCD device support --->
                [ ] Bootup logo ---
        <*> Sound card support --->
            <*> Advanced Linux Sound Architecture --->
                [*] PCI sound devices --->
                HD-Audio --->
                    <*> HD Audio PCI
                    <*> Build Realtek HD-audio codec support
                    -*- Enable generic HD-audio codec parser
                    (0) Default time-out for HD-audio power-save mode
        HID support --->
            -*- HID bus support
            [*]     Battery level reporting for HID devices
                    Special HID drivers --->
                        < > DISABLE ALL UNNEEDED DEVICES
                        <*> HID Multitouch panels
                (2048) Pre-allocated buffer size for HD-audio driver
        [*] USB support --->
            <*> xHCI HCD (USB 3.0) support
            <M> EHCI HCD (USB 2.0) support
            <M> OHCI HCD (USB 1.1) support
        <*> MMC/SD/SDIO card support --->
            <*> Realtek PCI-E SD/MMC Card Interface Driver
        [*] Generic powercap sysfs driver --->
            <*> Intel RAPL Support

    Firmware Drivers --->
        EFI (Extensible Firmware Interface) Support --->
            <*> EFI Variable Support via sysfs