**Resources**

[[]][Product Information](https://www.lenovo.com/us/en/p/laptops/thinkpad/thinkpadt/thinkpad-t480/22tp2tt4800)

[[]][Official Support Page](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-t-series-laptops/thinkpad-t480-type-20l5-20l6)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_T480/ThinkPad_T480_Spec.PDF)

[[]][Specifications (by region)](https://psref.lenovo.com/Product/ThinkPad/ThinkPad_T480)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/pccbbs/mobiles_pdf/t480_hmm_en.pdf)

[[]][User Guide](https://download.lenovo.com/pccbbs/mobiles_pdf/t480_ug_en.pdf)

[[]][ThinkPad T Series](https://en.wikipedia.org/wiki/ThinkPad_T_Series "wikipedia:ThinkPad T Series")

Lenovo Thinkpad T480 is a business notebook based on 7th/8th generation Intel® Core™ processor.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Firmware]](#Firmware)
    -   [[2.2] [Kernel]](#Kernel)
        -   [[2.2.1] [Processor]](#Processor)
        -   [[2.2.2] [Drivers]](#Drivers)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Portage]](#Portage)
    -   [[3.2] [libinput]](#libinput)
    -   [[3.3] [Display backlight]](#Display_backlight)
    -   [[3.4] [Keyboard backlight]](#Keyboard_backlight)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Processor throttles under load]](#Processor_throttles_under_load)
-   [[5] [External resources]](#External_resources)
-   [[6] [References]](#References)

## [Hardware]

### [Standard]

  ------------------------- ----------------------------------------------------------------------------------------------------- ------------- ------------------------ -------------------------------------------------------------- ---------------- -----------------------------------------------------------------
  Device                    Make/model                                                                                            Status        Vendor ID / Product ID   Kernel driver(s)                                               Kernel version   Notes
  CPU                       Intel i5-7200U, i5-7300U, i3-8130U, i5-8250U, i5-8350U, i7-8550U, or i7-8650U                         Works         N/A                      N/A                                                            6.12.58
  RAM                       max 64GiB DDR4 2400MHz (2 SO-DIMM)                                                                    Works         N/A                      N/A                                                            6.12.58
  GPU                       integrated Intel HD/UHD Graphics 620                                                                  Works         N/A                      [intel](https://wiki.gentoo.org/wiki/Intel "Intel")            6.12.58
  Discrete GPU (optional)   NVIDIA GeForce MX150, 2GB GDDR5 memory                                                                Works         N/A                      N/A                                                            6.12.58          x11-drivers/nvidia-drivers 580.95.05
  Display                   14.0\"; 16:9; HD 1366x768 TN 220 nits, FHD 1920 x 1080 IPS 250 nits, or WQHD 2560x1440 IPS 300 nits   Works         N/A                      N/A                                                            6.12.58          multitouch option for FHD
  Storage                   M.2 PCIe-NVMe, 512GB/1TB                                                                              Works         N/A                      [nvme](https://wiki.gentoo.org/wiki/NVMe "NVMe")               6.6.6            Sandisk Corp WD Black 2018/SN750 / PC SN720 NVMe SSD
  Ethernet                  Intel Ethernet Connection I219-V                                                                      Works         N/A                      e1000e                                                         6.12.58          Intel Corporation Ethernet Connection (4) I219-V (rev 21)
  Wi-Fi                     Intel Dual Band Wireless-AC 8265, Wi-Fi 2x2 802.11ac                                                  Works         N/A                      [iwlwifi](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi")      6.12.58          Intel Corporation Dual Band Wireless-AC 8265 \[Windstorm Peak\]
  Bluetooth                 Intel Bluetooth 4.1                                                                                   Not tested    8087:0a2b                [btusb](https://wiki.gentoo.org/wiki/Bluetooth "Bluetooth")    6.12.58
  Mobile Broadband          Intel XMM 7262 (Fibocom L830-EB) or Intel XMM 7360 (Fibocom L850-GL)                                  Not tested    N/A                      N/A                                                            N/A
  Sound                     HD Audio, Realtek ALC3287 codec                                                                       Works         N/A                      snd_hda_intel                                                  6.12.58
  Webcam                    IMC Networks Integrated Camera                                                                        Works         13d3:56a6                uvcvideo                                                       6.12.58          HD720p
  Keyboard                  Backlit                                                                                               Works         N/A                      N/A                                                            6.12.58
  Touchpad                  Synaptics TM3276-022                                                                                  Works         N/A                      [libinput](https://wiki.gentoo.org/wiki/Libinput "Libinput")   6.12.58
  Fingerprint Reader        Synaptics, Inc. Metallica MIS Touch Fingerprint Reader                                                Not tested    06cb:009a                N/A                                                            N/A
  Smartcard Reader          Alcor Micro Corp. AU9540 Smartcard Reader                                                             Not tested    058f:9540                sdhci-pci                                                      6.6.6
  SD Card Reader            Realtek Semiconductor Corp. Card Reader                                                               Works         0bda:0316                usb-storage                                                    6.12.58
  ------------------------- ----------------------------------------------------------------------------------------------------- ------------- ------------------------ -------------------------------------------------------------- ---------------- -----------------------------------------------------------------

CPU and its features:

`root `[`#`]`lscpu`

    Architecture:                       x86_64
    CPU op-mode(s):                     32-bit, 64-bit
    Address sizes:                      39 bits physical, 48 bits virtual
    Byte Order:                         Little Endian
    CPU(s):                             8
    On-line CPU(s) list:                0-7
    Vendor ID:                          GenuineIntel
    Model name:                         Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz
    CPU family:                         6
    Model:                              142
    Thread(s) per core:                 2
    Core(s) per socket:                 4
    Socket(s):                          1
    Stepping:                           10
    CPU(s) scaling MHz:                 20%
    CPU max MHz:                        4000.0000
    CPU min MHz:                        400.0000
    BogoMIPS:                           3999.93
    Flags:                              fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb pti ssbd ibrs ibpb stibp tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid mpx rdseed adx smap clflushopt intel_pt xsaveopt xsavec xgetbv1 xsaves dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp vnmi md_clear flush_l1d arch_capabilities

List of PCI devices:

`root `[`#`]`lspci -k`

    00:00.0 Host bridge: Intel Corporation Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers (rev 08)
        Subsystem: Lenovo ThinkPad T480
        Kernel driver in use: skl_uncore
    00:02.0 VGA compatible controller: Intel Corporation UHD Graphics 620 (rev 07)
        Subsystem: Lenovo UHD Graphics 620
        Kernel driver in use: i915
    00:04.0 Signal processing controller: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem (rev 08)
        Subsystem: Lenovo ThinkPad T480
        Kernel driver in use: proc_thermal
        Kernel modules: processor_thermal_device_pci_legacy
    00:08.0 System peripheral: Intel Corporation Xeon E3-1200 v5/v6 / E3-1500 v5 / 6th/7th/8th Gen Core Processor Gaussian Mixture Model
        Subsystem: Lenovo ThinkPad T480
    00:14.0 USB controller: Intel Corporation Sunrise Point-LP USB 3.0 xHCI Controller (rev 21)
        Subsystem: Lenovo ThinkPad T480
        Kernel driver in use: xhci_hcd
        Kernel modules: xhci_pci
    00:14.2 Signal processing controller: Intel Corporation Sunrise Point-LP Thermal subsystem (rev 21)
        Subsystem: Lenovo ThinkPad T480
        Kernel driver in use: intel_pch_thermal
        Kernel modules: intel_pch_thermal
    00:15.0 Signal processing controller: Intel Corporation Sunrise Point-LP Serial IO I2C Controller #0 (rev 21)
        Subsystem: Lenovo ThinkPad T480
    00:16.0 Communication controller: Intel Corporation Sunrise Point-LP CSME HECI #1 (rev 21)
        Subsystem: Lenovo ThinkPad T480
    00:1c.0 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #1 (rev f1)
        Subsystem: Lenovo Sunrise Point-LP PCI Express Root Port
        Kernel driver in use: pcieport
    00:1c.6 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #7 (rev f1)
        Subsystem: Lenovo Sunrise Point-LP PCI Express Root Port
        Kernel driver in use: pcieport
    00:1d.0 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #9 (rev f1)
        Subsystem: Lenovo Sunrise Point-LP PCI Express Root Port
        Kernel driver in use: pcieport
    00:1d.2 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #11 (rev f1)
        Subsystem: Lenovo Sunrise Point-LP PCI Express Root Port
        Kernel driver in use: pcieport
    00:1f.0 ISA bridge: Intel Corporation Sunrise Point LPC/eSPI Controller (rev 21)
        Subsystem: Lenovo ThinkPad T480
    00:1f.2 Memory controller: Intel Corporation Sunrise Point-LP PMC (rev 21)
        Subsystem: Lenovo ThinkPad T480
    00:1f.3 Audio device: Intel Corporation Sunrise Point-LP HD Audio (rev 21)
        Subsystem: Lenovo ThinkPad T480
        Kernel driver in use: snd_hda_intel
    00:1f.4 SMBus: Intel Corporation Sunrise Point-LP SMBus (rev 21)
        Subsystem: Lenovo ThinkPad T480
        Kernel driver in use: i801_smbus
    00:1f.6 Ethernet controller: Intel Corporation Ethernet Connection (4) I219-V (rev 21)
        Subsystem: Lenovo ThinkPad T480
        Kernel driver in use: e1000e
    03:00.0 Network controller: Intel Corporation Wireless 8265 / 8275 (rev 78)
        Subsystem: Intel Corporation Dual Band Wireless-AC 8265 [Windstorm Peak]
        Kernel driver in use: iwlwifi
        Kernel modules: iwlwifi
    04:00.0 PCI bridge: Intel Corporation JHL6240 Thunderbolt 3 Bridge (Low Power) [Alpine Ridge LP 2016] (rev 01)
        Subsystem: Device 2222:1111
        Kernel driver in use: pcieport
    05:00.0 PCI bridge: Intel Corporation JHL6240 Thunderbolt 3 Bridge (Low Power) [Alpine Ridge LP 2016] (rev 01)
        Subsystem: Device 2222:1111
        Kernel driver in use: pcieport
    05:01.0 PCI bridge: Intel Corporation JHL6240 Thunderbolt 3 Bridge (Low Power) [Alpine Ridge LP 2016] (rev 01)
        Subsystem: Device 2222:1111
        Kernel driver in use: pcieport
    05:02.0 PCI bridge: Intel Corporation JHL6240 Thunderbolt 3 Bridge (Low Power) [Alpine Ridge LP 2016] (rev 01)
        Subsystem: Device 2222:1111
        Kernel driver in use: pcieport
    06:00.0 System peripheral: Intel Corporation JHL6240 Thunderbolt 3 NHI (Low Power) [Alpine Ridge LP 2016] (rev 01)
        Subsystem: Device 2222:1111
    3c:00.0 USB controller: Intel Corporation JHL6240 Thunderbolt 3 USB 3.1 Controller (Low Power) [Alpine Ridge LP 2016] (rev 01)
        Subsystem: Device 2222:1111
        Kernel driver in use: xhci_hcd
        Kernel modules: xhci_pci
    3d:00.0 Non-Volatile memory controller: Sandisk Corp SanDisk Extreme Pro / WD Black 2018/SN750/PC SN720 NVMe SSD
        Subsystem: Sandisk Corp WD Black 2018/SN750 / PC SN720 NVMe SSD
        Kernel driver in use: nvme

List of USB devices:

`root `[`#`]`lsusb`

    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 002 Device 002: ID 0bda:0316 Realtek Semiconductor Corp. Card Reader
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 005: ID 06cb:009a Synaptics, Inc. Metallica MIS Touch Fingerprint Reader
    Bus 001 Device 004: ID 13d3:56a6 IMC Networks Integrated Camera
    Bus 001 Device 003: ID 8087:0a2b Intel Corp. Bluetooth wireless interface
    Bus 001 Device 002: ID 058f:9540 Alcor Micro Corp. AU9540 Smartcard Reader
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

List the state of both batteries:

`root `[`#`]`upower -i /org/freedesktop/UPower/devices/battery_BAT0`

`root `[`#`]`upower -i /org/freedesktop/UPower/devices/battery_BAT1`

## [Installation]

### [Firmware]

[Intel microcode](https://wiki.gentoo.org/wiki/Intel_microcode "Intel microcode"):

`root `[`#`]`emerge --ask sys-firmware/intel-microcode`

In order for the SoC and wireless to work properly, it is necessary to install the proper firmware files:

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

** Tip**\
See [intel](https://wiki.gentoo.org/wiki/Intel#DMC_firmware "Intel") and [iwlwifi](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi") articles for more information.

### [Kernel]

#### [Processor]

[KERNEL] **Kernel 6.6.6 (gentoo-sources)**

    Processor type and features  --->
          Processor family (Core 2/newer Xeon)
          Supported processsor vendors  --->
            [*] Support Intel processors

    Power management and ACPI options  --->
          CPU Frequency scaling  --->
                 Default CPUFreq governor (performance)
            <*>  'performance' governor
            *** CPU frequency scaling drivers ***
            -*- Intel P state control

    Device Drivers  --->
      [*] IOMMU Hardware Support  --->
           [*] Support for Intel IOMMU using DMA Remapping Devices
              [*]     Enable Intel DMA Remapping Devices by default
              [*]     Intel IOMMU performance events
           [*] Support for Interrupt Remapping

Using [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]] with the [[[experimental]](https://packages.gentoo.org/useflags/experimental)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag will have additional Processor family options made available:

[KERNEL] **Kernel 6.6.6 (gentoo-sources)**

    Processor type and features  --->
      Processor family  --->
        ...

or simply autodetecting the processor options by the compiler:

[KERNEL] **Kernel 6.6.6 (gentoo-sources)**

    Processor type and features  --->
      Processor family  --->
        (X) Native optimizations autodetected by GCC

#### [Drivers]

[KERNEL] **Kernel 6.6.6 (gentoo-sources)**

    Power management and ACPI options  --->
      [*] ACPI (Advanced Configuration and Power Interface) Support  --->
            <*>  Battery
            <*>  Video
              Fan

    Networking support  --->
      <M> Bluetooth subsystem support  --->
          Bluetooth device drivers  --->
            <M> HCI USB driver

      <*> Wireless  --->
        <M>  cfg80211 - wireless configuration API
        [*]  enable powersave by default
        <M>  Generic IEEE 802.11 Networking Stack (mac80211)

    Device Drivers  --->
      [*] PCI support  --->
            [*] PCI Express Port Bus support
          NVME Support  --->
            <*> NVM Express block device
          SCSI device support  --->
            <*> SCSI disk support

      <*> Serial ATA and Parallel ATA drivers (libata)  --->
            <*> AHCI SATA support

          Character devices  --->
            <M> TPM Hardware Support  --->
                [*] TPM HW Random Number Generator support
                <M> TPM Interface Specification 1.2 Interface / TPM 2.0 FIFO Interface
                <M> TPM 2.0 CRB Interface

      [*] Network device support  --->
            [*] Ethernet driver support  --->
                [*] Intel devices
                <*>     Intel(R) PRO/1000 PCI-Express Gigabit Ethernet support
            [*] Wireless LAN  --->
                [*] Intel devices
                <M>   Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)
                < >   Intel Wireless WiFi DVM Firmware support
                <M>   Intel Wireless WiFi MVM Firmware support

          I2C support  --->
            I2C Hardware Bus support  --->
                <M> Intel 82801 (ICH/PCH)

      -*- Power supply class support  --->
            [*] Expose power supply sensors as hwmon device

      [*] Watchdog Timer Support  --->
            <*> Intel TCO Timer/Watchdog

      <*> Multimedia support  --->
            [*] Media USB Adapters  --->
                  <*> USB Video Class (UVC)

          Graphics support  --->
             <*> /dev/agpgart (AGP Support)  --->
                  --- /dev/agpgart (AGP Support)
                  -*-   Intel 440LX/BX/GX, I8xx and E7x05 chipset support
             <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support)  --->
             [*] Enable legacy fbdev support for your modesetting driver
             <*> Intel 8xx/9xx/G3x/G4x/HD Graphics
                    [*]   Enable capturing GPU state following a hang
                    [*]     Compress GPU error state
                    [*]   Always enable userptr support

      <*> Sound card support  --->
            <*> Advanced Linux Sound Architecture  --->
              [*] PCI sound devices  --->
              <*> HD-Audio  --->
                  <*> HD Audio PCI
                  <*> Build Realtek HD-audio codec support
                  <*> Build HDMI/DisplayPort HD-audio codec support

      [*] USB support  --->
        <*> xHCI HCD (USB 3.0) support
        <*> EHCI HCD (USB 2.0) support

      <M> MMC/SD/SDIO card support  --->
            <M> Secure Digital Host Controller Interface support
            <M>   SDHCI support on PCI bus

      [*] X86 Platform Specific Device Drivers  --->
            <*> ThinkPad ACPI Laptop Extras
            [*]   Console audio control ALSA interface
            [*]   Video output control support
            [*]   Support NVRAM polling for hot keys

## [Configuration]

### [Portage]

[FILE] **`/etc/portage/make.conf`**

    # Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz
    MAKEOPTS="-j8"
    CPU_FLAGS_X86="aes avx avx2 f16c fma3 mmx mmxext pclmul popcnt sse sse2 sse3 sse4_1 sse4_2 sse4a ssse3"

    # drivers
    #
    INPUT_DEVICES="libinput"
    VIDEO_CARDS="intel"

### [libinput]

[FILE] **`/etc/X11/xorg.conf.d/40-libinput.conf`Configure touchpad**

    Section "InputClass"
         Identifier "libinput touchpad catchall"
         MatchIsTouchpad "on"
         MatchDevicePath "/dev/input/event*"
         Option "Tapping" "True" # Touchpad tapping enabled
         Option "TappingDrag" "False" # Never drag
         Option "TransformationMatrix" "0.96 0 0 0 0.96 0 0 0 1" # Slight accel
         Driver "libinput"
    EndSection

### [Display backlight]

To control the display backlight install [[[sys-power/acpilight]](https://packages.gentoo.org/packages/sys-power/acpilight)[]]:

`root `[`#`]`emerge --ask sys-power/acpilight`

Make the desired users a part of the `video` group to set the display brightness.

** Tip**\

`user `[`$`]`udevadm monitor`

can be used to analyze whether a backlight key press actually triggers a value change.

### [Keyboard backlight]

The keyboard backlight is working out of the box (with a keyboard actually supporting the backlight), and can be controlled by using the [Fn]+[Space] keys without any further adjustments. There are 3 predefined steps of the keyboard backlight. `0`, `50` and `100`.

To display the current setting of keyboard backlight use the `-ctrl tpacpi::kbd_backlight` command line option for [xbacklight].

To show the available adjustment steps use following command, it will show `3` steps:

`user `[`$`]`xbacklight -ctrl tpacpi::kbd_backlight -get-steps`

To display the current setting use following command:

`user `[`$`]`xbacklight -ctrl tpacpi::kbd_backlight -getf`

## [Troubleshooting]

### [Processor throttles under load]

Lenovo Thinkpad T480 is one of the devices hit by CPU package power limit bug. The bug causes the affected processors to throttle its frequency down to the base line (\~1.8GHz) during a multi-core load (e.g. kernel compilation).^[\[1\]](#cite_note-1)^

There is a simple utility correcting the power limit configuration - [[[sys-power/throttled]](https://packages.gentoo.org/packages/sys-power/throttled)[]]:

`root `[`#`]`emerge --ask sys-power/throttled`

## [External resources]

-   [https://wiki.archlinux.org/title/Lenovo_ThinkPad_T480](https://wiki.archlinux.org/title/Lenovo_ThinkPad_T480)

## [References]

1.  [[[↑](#cite_ref-1)] [[T480s Linux throttling bug](https://www.reddit.com/r/thinkpad/comments/870u0a/t480s_linux_throttling_bug/), Reddit.com]]