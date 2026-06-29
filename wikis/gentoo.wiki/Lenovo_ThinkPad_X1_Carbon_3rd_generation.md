**Resources**

[[]][Official Support Page](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-x-series-laptops/thinkpad-x1-carbon-20bs-20bt)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_X1_Carbon_3rd_Gen/ThinkPad_X1_Carbon_3rd_Gen_Spec.PDF)

[[]][Specifications (by region)](https://psref.lenovo.com/Product/ThinkPad/ThinkPad_X1_Carbon_3rd_Gen)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/pccbbs/mobiles_pdf/x1_carbon3_hmm_en_sp40g55065_01.pdf)

[[]][User Guide](https://download.lenovo.com/pccbbs/mobiles_pdf/x1carbon3_ug_en.pdf)

[[]][BIOS Setup](https://download.lenovo.com/pccbbs/mobiles_pdf/lenovo_bios_setup_linux_wmi_sysfs_1.2.pdf)

[[]][ThinkPad X1 series](https://en.wikipedia.org/wiki/ThinkPad_X1_series "wikipedia:ThinkPad X1 series")

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Firmware]](#Firmware)
    -   [[2.2] [Kernel]](#Kernel)
    -   [[2.3] [Emerge]](#Emerge)
-   [[3] [External resources]](#External_resources)

## [Hardware]

### [Standard]

  ---------------------------- ---------------------------------- -------- ------------------------ ------------------ ---------------- -------------------------------------------------------------------
  Device                       Make/model                         Status   Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  CPU                          Intel i7-5600 series               Works    N/A                      N/A                4.12.12
  WQHD Touchscreen             2540x1440                          Works    N/A                      N/A                4.12.12          Does not need the Xorg mutouch driver for the touchscreen to work
  WiFi                         Intel Wireless                     Works    N/A                      iwlwifi            4.12.12
  Synaptics or Elan Touchpad   N/A                                Works    N/A                      N/A                4.12.12
  Video card                   Intel 5000-series \[Intel 5600\]   Works    N/A                      intel i965         4.12.12
  ---------------------------- ---------------------------------- -------- ------------------------ ------------------ ---------------- -------------------------------------------------------------------

## [Installation]

### [Firmware]

External firmware is required for Wi-Fi to work:

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

### [Kernel]

[KERNEL] **Enable support for hardware drivers, filesystems and features**

    -*- Enable the block layer --->
        Partition Types --->
            [*] Advanced partition selection
            [*] EFI GUID Partition support

    Processor type and features  --->
        [*] Symmetric multi-processing support
        [Y] Machine Check / overheating reporting
        [Y]   Intel MCE Features
        [*] EFI runtime service support
        [*]   EFI stub support
        [*]     EFI mixed-mode support

    Executable file formats / Emulations  --->
        [*] IA32 Emulation

    [*] Networking support  --->
        Networking options  --->
            <*> Packet socket
        [*] Wireless  --->
            <M>   cfg80211 - wireless configuration API
            [M]     cfg80211 wireless extensions compatibility

    Device Drivers --->
        Generic Driver Options --->
            [*] Maintain a devtmpfs filesystem to mount at /dev
            [ ]   Automount devtmpfs at /dev, after the kernel mounted the rootfs
            -*- Userspace firmware loading support
        [*] Network device support  --->
            [*] Wireless LAN  --->
                [*]   Intel devices   (Note: compile these as modules)
                <M>     Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)
                <M>       Intel Wireless WiFi DVM Firmware support
                <M>       Intel Wireless WiFi MVM Firmware support
        Character devices ->
            <Y> TPM Hardware Support ->  (Note: required for suspend/resume)
                <Y> TPM Interface Specification 1.2 Interface / TPM 2.0 FIFO Interface  (Note: required for suspend/resume)
        IOMMU Hardware Support ->
            Support for Intel IOMMU using DMA Remapping Devices ->
                <N> Enable Intel DMA Remapping Devices by default  (Note: can cause GPU hangs if <Y>)
        SCSI device support  --->
            <*> SCSI disk support
        HID support  --->
            -*- HID bus support
            <*>   Generic HID driver
            [*]   Battery level reporting for HID devices
                USB HID support  --->
                    <*> USB HID transport layer
        [*] USB support  --->
            <*>     xHCI HCD (USB 3.0) support
            <*>     EHCI HCD (USB 2.0) support
            <*>     OHCI HCD (USB 1.1) support
        [*] Real Time Clock --->
              [*]   Set system time from RTC on startup and resume
              (rtc0)  RTC used to set the system time
              [*]   Set the RTC time based on NTP synchronization
              (rtc0)  RTC used to synchronize NTP adjustment
              [*]   /sys/class/rtc/rtcN (sysfs)
              [*]   /proc/driver/rtc (procfs for rtc0)
              [*]   /dev/rtcN (character devices)
              <*>   PC-style 'CMOS'
        Graphics support  --->
            <*> /dev/agpgart (AGP Support)  --->
                --- /dev/agpgart (AGP Support)
                -*-   Intel 440LX/BX/GX, I8xx and E7x05 chipset support
            [ ] VGA Arbitration
            [ ] Laptop Hybrid Graphics - GPU switching support
            <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support)  --->
                --- Direct Rendering Manager (XFree86 4.1.0 and higher DRI support)
                [*]   Enable legacy fbdev support for your modesetting driver
            [ ] Allow to specify an EDID data set instead of probing for it
                I2C encoder or helper chips  --->
            <*> Intel 8xx/9xx/G3x/G4x/HD Graphics
            -*- Backlight & LCD device support  --->
            [*] Bootup logo  --->

    Firmware Drivers  --->
        EFI (Extensible Firmware Interface) Support  --->
            <*> EFI Variable Support via sysfs

    -*- Cryptographic API --->  (Note: for WiFi)
        -*- AES cipher algorithms
        -*- AES cipher algorithms (x86_64)
        <*> AES cipher algorithms (AES-NI)

### [Emerge]

[FILE] **`/etc/portage/make.conf`**

    MAKEOPTS="-j5"
    CPU_FLAGS_X86="aes avx avx2 fma3 mmx mmxext pclmul popcnt sse sse2 sse3 sse4_1 sse4_2 ssse3"

    VIDEO_CARDS="intel i965"
    INPUT_DEVICES="evdev synaptics mutouch"

## [External resources]

-   [https://wiki.archlinux.org/title/Lenovo_ThinkPad_X1_Carbon\_(Gen_3)](https://wiki.archlinux.org/title/Lenovo_ThinkPad_X1_Carbon_(Gen_3))