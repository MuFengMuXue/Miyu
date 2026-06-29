**Resources**

[[]][Product Information](https://www.lenovo.com/us/en/laptops/thinkpad/thinkpad-t-series/T495/p/22TP2TTT495)

[[]][Official Support Page](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-t-series-laptops/thinkpad-t495-type-20nj-20nk)

[[]][Official Support Data](https://download.lenovo.com/supportdata/product.html?id=LAPTOPS-AND-NETBOOKS/THINKPAD-T-SERIES-LAPTOPS/THINKPAD-T495-TYPE-20NJ-20NK)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_T495/ThinkPad_T495_Spec.pdf)

[[]][Specifications (by region)](https://psref.lenovo.com/Product/ThinkPad/ThinkPad_T495)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/pccbbs/mobiles_pdf/t495_hmm_en.pdf)

[[]][User Guide](https://download.lenovo.com/pccbbs/mobiles_pdf/t495_ug_v2_en.pdf)

[[]][BIOS Setup](https://download.lenovo.com/pccbbs/mobiles_pdf/lenovo_bios_setup_linux_wmi_sysfs_1.2.pdf)

[[]][ThinkPad T Series](https://en.wikipedia.org/wiki/ThinkPad_T_Series "wikipedia:ThinkPad T Series")

Lenovo Thinkpad T495 is a business notebook based on 2nd generation of AMD Ryzen™ processors with Radeon™ Vega graphics, supporting AMD FreeSync™, and delivering up to 14.9 hours of battery life.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [Accessories]](#Accessories)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Kernel configuration]](#Kernel_configuration)
        -   [[2.1.1] [Processor]](#Processor)
        -   [[2.1.2] [Drivers]](#Drivers)
    -   [[2.2] [Firmware]](#Firmware)
    -   [[2.3] [GRUB settings]](#GRUB_settings)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Portage]](#Portage)
    -   [[3.2] [Xorg]](#Xorg)
    -   [[3.3] [Sensors]](#Sensors)
    -   [[3.4] [Display backlight]](#Display_backlight)
    -   [[3.5] [Keyboard backlight]](#Keyboard_backlight)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Unable to write to IOMMU]](#Unable_to_write_to_IOMMU)
    -   [[4.2] [Slow/unresponsive system after direct reboot from Microsoft Window 10]](#Slow.2Funresponsive_system_after_direct_reboot_from_Microsoft_Window_10)
    -   [[4.3] [AMDGPU always on 100%]](#AMDGPU_always_on_100.25)
-   [[5] [External resources]](#External_resources)

## [Hardware]

### [Standard]

Lenovo Thinkpad T495 specification:

  -------------------- ---------------------------------------------------------------------------- ------------- -------------- -------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Device               Make/model                                                                   Status        Bus ID         Driver                                                         Notes
  CPU                  AMD Ryzen 3 PRO 3300U, AMD Ryzen 5 PRO 3500U, or AMD Ryzen 7 PRO 3700U       Works         N/A            N/A
  Memory               DDR4 2400MHz (8/16GB soldered)                                               Works         N/A            N/A                                                            1 extra slot allows for up to 48GB of total RAM
  Graphics             Integrated AMD Radeon™ Vega 6, 8, or 10 (Picasso)                            Works         PCIe 06:00.0   [amdgpu](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU")         GPU reserves 2GB of the system memory, requires kernel version \>=5.1
  Display              14.0\", HD 1366x768 TN, 220 nits, or FHD 1920 x 1080 IPS, 250/300/400 nits   Works         N/A            N/A                                                            multitouch option for FHD 300 nits
  Storage              M.2 PCIe-NVMe, Opal, 256GB/512GB/1TB                                         Works         PCIe 02:00.0   [nvme](https://wiki.gentoo.org/wiki/NVMe "NVMe")               Samsung NVMe PM981a or Western Digital PC SN720
  Ethernet             Realtek RTL8211E Gigabit Ethernet                                            Works         PCIe 03:00.0   r8169
  Wireless             Intel® 9260 Wireless AC                                                      Works         PCIe 01:00.0   [iwlwifi](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi")
  Bluetooth            Intel® Bluetooth® 5.0                                                        Works         USB 004:002    [btusb](https://wiki.gentoo.org/wiki/Bluetooth "Bluetooth")
  Mobile Broadband     Fibocom L850-GL 4G LTE CAT9                                                  Not tested    N/A            N/A
  Audio                Realtek ALC892                                                               Works         PCIe 06:00.6   snd_hda_intel, snd_hda_codec_realtek
  Camera               Chicony 720p                                                                 Works         USB 004:004    uvcvideo
  Keyboard             Backlit                                                                      Works         N/A            N/A
  Touchpad             Synaptics                                                                    Works         N/A            [libinput](https://wiki.gentoo.org/wiki/Libinput "Libinput")
  Fingerprint Reader   Synaptics UWP WBDI                                                           Works         USB 004:006    N/A                                                            Requires version 1.90 or newer of [[[sys-auth/libfprint]](https://packages.gentoo.org/packages/sys-auth/libfprint)[]] and [[[sys-auth/fprintd]](https://packages.gentoo.org/packages/sys-auth/fprintd)[]]
  Smartcard Reader     Alcor Micro AU95403                                                          Works         USB 004:005    sdhci-pci                                                      Supports microSD cards only.
  Battery              3 Cell Li-Polymer, 50Wh                                                      Works         N/A            N/A
  -------------------- ---------------------------------------------------------------------------- ------------- -------------- -------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Accessories]

  ----------------- -------------------------------------- ------------- -------- ------------------ ---------------- ---------------------------------------------
  Device            Make/model                             Status        Bus ID   Kernel driver(s)   Kernel version   Notes
  Docking station   Lenovo ThinkPad Basic Docking (40AG)   Works         N/A      USB-C/USB          5.5.13           Everything works, no special driver needed.
  Docking station   Lenovo ThinkPad Pro Docking (40AH)     Not tested    N/A      N/A
  Docking station   Lenovo ThinkPad Ultra Docking (40AJ)   Not tested    N/A      N/A
  ----------------- -------------------------------------- ------------- -------- ------------------ ---------------- ---------------------------------------------

CPU and its features:

`root `[`#`]`lscpu`

    Architecture:        x86_64
    CPU op-mode(s):      32-bit, 64-bit
    Byte Order:          Little Endian
    Address sizes:       43 bits physical, 48 bits virtual
    CPU(s):              8
    On-line CPU(s) list: 0-7
    Thread(s) per core:  2
    Core(s) per socket:  4
    Socket(s):           1
    Vendor ID:           AuthenticAMD
    CPU family:          23
    Model:               24
    Model name:          AMD Ryzen 7 PRO 3700U w/ Radeon Vega Mobile Gfx
    Stepping:            1
    CPU MHz:             1225.375
    CPU max MHz:         2300.0000
    CPU min MHz:         1400.0000
    BogoMIPS:            4591.44
    Virtualization:      AMD-V
    L1d cache:           32K
    L1i cache:           64K
    L2 cache:            512K
    L3 cache:            4096K
    Flags:               fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb hw_pstate sme ssbd sev ibpb vmmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap clflushopt sha_ni xsaveopt xsavec xgetbv1 xsaves clzero irperf xsaveerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif overflow_recov succor smca

List of PCI devices:

`root `[`#`]`lspci -k`

    00:00.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Root Complex
            Subsystem: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Root Complex
    00:00.2 IOMMU: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 IOMMU
            Subsystem: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 IOMMU
    00:01.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-1fh) PCIe Dummy Host Bridge
    00:01.2 PCI bridge: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 PCIe GPP Bridge [6:0]
            Kernel driver in use: pcieport
    00:01.3 PCI bridge: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 PCIe GPP Bridge [6:0]
            Kernel driver in use: pcieport
    00:01.4 PCI bridge: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 PCIe GPP Bridge [6:0]
            Kernel driver in use: pcieport
    00:01.6 PCI bridge: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 PCIe GPP Bridge [6:0]
            Kernel driver in use: pcieport
    00:01.7 PCI bridge: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 PCIe GPP Bridge [6:0]
            Kernel driver in use: pcieport
    00:08.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-1fh) PCIe Dummy Host Bridge
    00:08.1 PCI bridge: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Internal PCIe GPP Bridge 0 to Bus A
            Kernel driver in use: pcieport
    00:14.0 SMBus: Advanced Micro Devices, Inc. [AMD] FCH SMBus Controller (rev 61)
            Subsystem: Lenovo FCH SMBus Controller
            Kernel driver in use: piix4_smbus
            Kernel modules: i2c_piix4, sp5100_tco
    00:14.3 ISA bridge: Advanced Micro Devices, Inc. [AMD] FCH LPC Bridge (rev 51)
            Subsystem: Lenovo FCH LPC Bridge
    00:18.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 0
    00:18.1 Host bridge: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 1
    00:18.2 Host bridge: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 2
    00:18.3 Host bridge: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 3
            Kernel driver in use: k10temp
            Kernel modules: k10temp
    00:18.4 Host bridge: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 4
    00:18.5 Host bridge: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 5
    00:18.6 Host bridge: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 6
    00:18.7 Host bridge: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 7
    01:00.0 Network controller: Intel Corporation Wireless-AC 9260 (rev 29)
            Subsystem: Intel Corporation Wireless-AC 9260
            Kernel driver in use: iwlwifi
            Kernel modules: iwlwifi
    02:00.0 Non-Volatile memory controller: Samsung Electronics Co Ltd NVMe SSD Controller SM981/PM981/PM983
            Subsystem: Samsung Electronics Co Ltd NVMe SSD Controller SM981/PM981/PM983
            Kernel driver in use: nvme
    03:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 0e)
            Subsystem: Lenovo RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller
            Kernel driver in use: r8169
    03:00.1 Serial controller: Realtek Semiconductor Co., Ltd. Device 816a (rev 0e)
            Subsystem: Lenovo Device 5125
            Kernel modules: 8250_pci
    03:00.2 Serial controller: Realtek Semiconductor Co., Ltd. Device 816b (rev 0e)
            Subsystem: Lenovo Device 5125
            Kernel modules: 8250_pci
    03:00.3 IPMI Interface: Realtek Semiconductor Co., Ltd. Device 816c (rev 0e)
            Subsystem: Lenovo Device 5125
            Kernel modules: ipmi_si
    03:00.4 USB controller: Realtek Semiconductor Co., Ltd. Device 816d (rev 0e)
            Subsystem: Lenovo Device 5125
            Kernel driver in use: ehci-pci
    04:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 10)
            Subsystem: Lenovo RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller
            Kernel driver in use: r8169
    05:00.0 SD Host controller: Genesys Logic, Inc GL9750 SD Host Controller (rev 01)
            Subsystem: Lenovo GL9750 SD Host Controller
            Kernel driver in use: sdhci-pci
            Kernel modules: sdhci_pci
    06:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Picasso (rev d1)
            Subsystem: Lenovo Picasso
            Kernel driver in use: amdgpu
    06:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Raven/Raven2/Fenghuang HDMI/DP Audio Controller
            Subsystem: Lenovo Raven/Raven2/Fenghuang HDMI/DP Audio Controller
            Kernel driver in use: snd_hda_intel
            Kernel modules: snd_hda_intel
    06:00.2 Encryption controller: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 10h-1fh) Platform Security Processor
            Subsystem: Lenovo Family 17h (Models 10h-1fh) Platform Security Processor
    06:00.3 USB controller: Advanced Micro Devices, Inc. [AMD] Raven USB 3.1
            Subsystem: Lenovo Raven USB 3.1
            Kernel driver in use: xhci_hcd
    06:00.4 USB controller: Advanced Micro Devices, Inc. [AMD] Raven USB 3.1
            Subsystem: Lenovo Raven USB 3.1
            Kernel driver in use: xhci_hcd
    06:00.5 Multimedia controller: Advanced Micro Devices, Inc. [AMD] Raven/Raven2/FireFlight/Renoir Audio Processor
            Subsystem: Lenovo Raven/Raven2/FireFlight/Renoir Audio Processor
    06:00.6 Audio device: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 10h-1fh) HD Audio Controller
            Subsystem: Lenovo Family 17h (Models 10h-1fh) HD Audio Controller
            Kernel driver in use: snd_hda_intel
            Kernel modules: snd_hda_intel

List of USB devices:

`root `[`#`]`lsusb`

    Bus 005 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 004 Device 006: ID 06cb:00bd Synaptics, Inc.
    Bus 004 Device 005: ID 058f:9540 Alcor Micro Corp. AU9540 Smartcard Reader
    Bus 004 Device 004: ID 04f2:b681 Chicony Electronics Co., Ltd
    Bus 004 Device 003: ID 05e3:0610 Genesys Logic, Inc. 4-port hub
    Bus 004 Device 002: ID 8087:0025 Intel Corp.
    Bus 004 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 003 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

## [Installation]

### [Kernel configuration]

** Note**\
Full hardware support and recognition relies heavily on the 5.x branch linux kernel. Do not use 4.x linux kernels.

#### [Processor]

[KERNEL] **Kernel 5.4.1 (gentoo-sources)**

    Processor type and features  --->
          Processor family (Generic-x86-64)
      [*] CPU microcode loading support
      [*]   AMD microcode loading support

    Power management and ACPI options  --->
          CPU Frequency scaling  --->
                 Default CPUFreq governor (performance)
            <*>  'performance' governor

    Device Drivers  --->
          Generic Driver Options  --->
                Firmware loader  --->
                  -*- Firmware loading facility
                  (amd-ucode/microcode_amd_fam17h.bin)
                  (/lib/firmware) Firmware blobs root directory

      <*> Hardware Monitoring support  --->
            <M> AMD Family 10h+ temperature sensor

      [*] IOMMU Hardware Support  --->
            [*] AMD IOMMU support
            <*>   AMD IOMMU Version 2 driver
            [*] Support for Interrupt Remapping

Using [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]] with the `experimental` USE flag will have additional Processor family options made available:

[KERNEL] **Kernel 5.4.1 (gentoo-sources)**

    Processor type and features  --->
      Processor family  --->
        (X) AMD Zen 2

or simply autodetecting the processor options by the compiler:

[KERNEL] **Kernel 5.4.1 (gentoo-sources)**

    Processor type and features  --->
      Processor family  --->
        (X) Native optimizations autodetected by GCC

For more information see the wiki page on [AMD Ryzen processors](https://wiki.gentoo.org/wiki/Ryzen "Ryzen").

#### [Drivers]

[KERNEL] **Kernel 5.4.1 (gentoo-sources)**

    Power management and ACPI options  --->
      [*] ACPI (Advanced Configuration and Power Interface) Support  --->
            <*>  Battery
            <*>  Video

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

          Generic Driver Options  --->
                Firmware loader  --->
                  -*- Firmware loading facility
                  (amd-ucode/microcode_amd_fam17h.bin ... iwlwifi-9260-th-b0-jf-b0-34.ucode)
                  (/lib/firmware) Firmware blobs root directory

      <*> Serial ATA and Parallel ATA drivers (libata)  --->
            <*> AHCI SATA support

          Character devices  --->
            <M> TPM Hardware Support  --->
                [*] TPM HW Random Number Generator support
                <M> TPM Interface Specification 1.2 Interface / TPM 2.0 FIFO Interface
                <M> TPM 2.0 CRB Interface

      [*] Network device support  --->
            [*] Ethernet driver support  --->
                [*] Realtek devices
                <*>   Realtek 8169 gigabit ethernet support
            [*] Wireless LAN  --->
                [*] Intel devices
                <M>   Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)
                < >   Intel Wireless WiFi DVM Firmware support
                <M>   Intel Wireless WiFi MVM Firmware support

          I2C support  --->
            I2C Hardware Bus support  --->
              <M> Intel PIIX4 and compatible (ATI/AMD/Serverworks/Broadcom/SMSC)

      -*- Power supply class support  --->
            [*] Expose power supply sensors as hwmon device

      [*] Watchdog Timer Support  --->
            <M> AMD/ATI SP5100 TCO Timer/Watchdog

      <*> Multimedia support  --->
            [*] Media USB Adapters  --->
                  <*> USB Video Class (UVC)

          Graphics support  --->
            <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support)
            <*> AMD GPU
                Display Engine Configuration  --->
                  [*] AMD DC - Enable new display engine
                Frame buffer Devices  --->
                  -*- Support for frame buffer devices  --->
                        [*] EFI-based Framebuffer Support
                        [*] Simple framebuffer support
                Console display driver support  --->
                  <*> Framebuffer Console support

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

** Note**\
The option for the built-in firmware files below option [\"-\*- Firmware loading facility\"] is incomplete. See the next section [Firmware](#firmware) for the complete list of the firmware files.

### [Firmware]

In order for the graphics and wireless to work properly, it is necessary to install the proper firmware (or microcode) files and build them into the kernel, as shown below.

[FILE] **`/usr/src/linux/.config`**

    CONFIG_EXTRA_FIRMWARE="amd-ucode/microcode_amd_fam17h.bin amdgpu/picasso_asd.bin amdgpu/picasso_ce.bin amdgpu/picasso_gpu_info.bin amdgpu/picasso_me.bin amdgpu/picasso_mec.bin amdgpu/picasso_mec2.bin amdgpu/picasso_pfp.bin amdgpu/picasso_rlc.bin amdgpu/picasso_rlc_am4.bin amdgpu/picasso_sdma.bin amdgpu/picasso_ta.bin amdgpu/picasso_vcn.bin iwlwifi-9260-th-b0-jf-b0-34.ucode regulatory.db regulatory.db.p7s"

These files should be installed in the system before the kernel recompilation using, for example, the command

`root `[`#`]`emerge --ask sys-kernel/linux-firmware net-wireless/wireless-regdb`

See [amdgpu](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU") and [iwlwifi](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi") wiki pages for more information.

### [GRUB settings]

Edit/update the following line in the following file:

[FILE] **`/etc/default/grub`**

    GRUB_CMDLINE_LINUX_DEFAULT="acpi_backlight=vendor"

## [Configuration]

### [Portage]

[FILE] **`/etc/portage/package.use/00input`**

    */* INPUT_DEVICES: libinput

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* amdgpu radeonsi

[FILE] **`/etc/portage/package.use/00cpu-flags`**

    */*  CPU_FLAGS_X86: aes avx avx2 f16c fma3 mmx mmxext pclmul popcnt sha sse sse2 sse3 sse4_1 sse4_2 sse4a ssse3

### [Xorg]

[FILE] **`/etc/X11/xorg.conf.d/10-device.conf`Device section**

    Section "Device"
       Identifier  "device_default"
       Driver      "amdgpu"
       Option      "DRI" "3"
       Option      "TearFree" "on"
       Option      "monitor-eDP" "monitor_default"
    EndSection

[FILE] **`/etc/X11/xorg.conf.d/20-monitor.conf`Monitor section**

    Section "Monitor"
      Identifier   "monitor_default"
      DisplaySize  309 174                      # 14.0" and 1920x1080 => 157dpi
      Option       "PreferredMode"  "1920x1080"
      Option       "DPMS"           "On"
    EndSection

[FILE] **`/etc/X11/xorg.conf.d/30-monitor.conf`Screen section**

    Section "Screen"
      Identifier       "screen_default"
      Device           "device_default"
      Monitor          "monitor_default"
      DefaultDepth     24
      SubSection "Display"
        Depth          24
      EndSubSection
    EndSection

### [Sensors]

[FILE] **`/etc/sensors.d/amdgpu.conf`**

    chip "amdgpu-*"

        label temp1 "GPU temperature"
        ignore in0
        ignore in1

[FILE] **`/etc/sensors.d/battery.conf`**

    chip "BAT0-acpi-*"

        label in0 "BAT voltage"

[FILE] **`/etc/sensors.d/iwlwifi.conf`**

    chip "iwlwifi-*"

        label temp1 "WiFi temperature"

[FILE] **`/etc/sensors.d/thinkpad.conf`**

    chip "thinkpad-isa-*"

      label fan1   "Fan speed"
      label temp1  "CPU temperature"
      label temp11 "Power circuitry temperature"
      ignore temp2
      ignore temp3
      ignore temp4
      ignore temp5
      ignore temp6
      ignore temp7
      ignore temp8
      ignore temp9
      ignore temp10
      ignore temp12
      ignore temp13
      ignore temp14
      ignore temp15
      ignore temp16

### [Display backlight]

To control the display backlight install [[[sys-power/acpilight]](https://packages.gentoo.org/packages/sys-power/acpilight)[]]. This comes with a system udev rule recommended by the upstream author.

`root `[`#`]`emerge --ask sys-power/acpilight`

Regular system users are not prohibited to alter files in the `sys` filesystem. The included `udev` rule allows users in the `video` group to set the display brightness.

### [Keyboard backlight]

The keyboard backlight is working out of the box, and can be controlled by using the [Fn]+[Space] keys without any further adjustments. There are 3 predefined steps of the keyboard backlight. `0`, `50` and `100`. To display the current setting of keyboard backlight use the `-ctrl tpacpi::kbd_backlight` command line option for `xbacklight`.

To show the available adjustment steps use following command, it will show `3` steps.

`user `[`$`]`xbacklight -ctrl tpacpi::kbd_backlight -get-steps`

To display the current setting use following command:

`user `[`$`]` xbacklight -ctrl tpacpi::kbd_backlight -getf`

## [Troubleshooting]

### [Unable to write to IOMMU]

Sometimes (most of the time) I am getting the following kernel message when booting the system:

`pci 0000:00:00.2: AMD-Vi: Unable to write to IOMMU perf counter.`

`pci 0000:00:00.2: can't derive routing for PCI INT A`

`pci 0000:00:00.2: PCI INT A: not connected`

Later, in the kernel log, one can find the following line:

`pci 0000:00:00.2: AMD-Vi: Found IOMMU cap 0x40`

It seems that IOMMU works just fine and the first message is a result of a premature initialization of the IOMMU system. According to other reports found on the internet, it can be ignored. Still, it pollutes the screen during a silent boot process.

### [][Slow/unresponsive system after direct reboot from Microsoft Window 10]

In kernel versions from 5.4 to 5.6.13 some issues related to MMC/SDHCI driver for Genesys Logic GLI9750 occur after direct reboot from Microsoft Windows 10. The system becomes slow with a few kernel threads using 100% of CPU trying to access MMC/SDHCI device. The issue has been reported (kernel bug [#205871](//bugzilla.kernel.org/show_bug.cgi?id=205871)) and fixed in kernels 5.4.42 and 5.6.14.

### [][AMDGPU always on 100%]

** Note**\
The bug[1455 is closed](https://gitlab.freedesktop.org/drm/amd/-/issues/1455). Fix using [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]]-20220310

Steps to verfiy if hardware is hit by this bug:

Verify frequency GPU currently uses, it should be at 400MHz, but it is stucked permanently at 1200MHz and does not get back to the lowest frequency available. Verify using the command below:

`user `[`$`]`cat /sys/class/drm/card0/device/pp_dpm_mclk`

    0: 400Mhz
    1: 933Mhz
    2: 1067Mhz
    3: 1200Mhz *

Verify the Memory Clock using the hardware specific [[[app-misc/radeontop]](https://packages.gentoo.org/packages/app-misc/radeontop)[]] tool.

`user `[`$`]`radeontop`

    Collecting data, please wait....
                radeontop 1.4, running on RAVEN bus 06, 120 samples/sec
                                             │
                       Graphics pipe   0.00% │
    ─────────────────────────────────────────┼─────────────────────────────────────────
                        Event Engine   0.00% │
                                             │
         Vertex Grouper + Tesselator   0.00% │
                                             │
                   Texture Addresser   0.00% │
                                             │
                       Shader Export   0.00% │
         Sequencer Instruction Cache   0.00% │
                 Shader Interpolator   0.00% │
                                             │
                      Scan Converter   0.00% │
                  Primitive Assembly   0.00% │
                                             │
                         Depth Block   0.00% │
                         Color Block   0.00% │
                                             │
                    67M / 2016M VRAM   3.35% │
                     23M / 3063M GTT   0.76% │
          1.20G / 1.20G Memory Clock 100.00% │█████████████████████████████████████████
          0.20G / 1.20G Shader Clock  16.67% │██████
                                             │

Create a file dump:

`user `[`$`]`radeontop -d /tmp/test`

View dump:

`user `[`$`]`head /tmp/test`

    1642627259.573360: bus 06, gpu 0.00%, ee 0.00%, vgt 0.00%, ta 0.00%, sx 0.00%, sh 0.00%, spi 0.00%, sc 0.00%, pa 0.00%, db 0.0
    0%, cb 0.00%, vram 3.35% 67.49mb, gtt 0.76% 23.21mb, mclk 100.00% 1.200ghz, sclk 16.67% 0.200ghz

Notice **mclk** is always at 100%, making the laptop heat up more than usual and consume the battery faster.

## [External resources]

-   [Memory clock always at 100% on the thinkpad T495](https://gitlab.freedesktop.org/drm/amd/-/issues/1455)
-   [https://wiki.archlinux.org/title/Lenovo_ThinkPad_T495](https://wiki.archlinux.org/title/Lenovo_ThinkPad_T495)