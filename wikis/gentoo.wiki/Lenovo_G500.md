[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Lenovo_G500&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Lenovo G500](https://pcsupport.lenovo.com/ru/en/products/laptops-and-netbooks/lenovo-g-series-laptops/lenovo-g500-notebook)

[[]][Specifications](https://download.lenovo.com/consumer/mobiles_pub/lenovo_g400g500g405g505g410g510_hmm.pdf#G4.1006019)

[[]][Specifications (parts)](https://download.lenovo.com/consumer/mobiles_pub/lenovo_g400g500g405g505g410g510_hmm.pdf#G4.1013683)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/consumer/mobiles_pub/lenovo_g400g500g405g505g410g510_hmm.pdf)

[[]][User Guide](https://download.lenovo.com/consumer/mobiles_pub/lenovo_g400g500g405g505g410g510_ug_english.pdf)

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [Detailed information]](#Detailed_information)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Kernel]](#Kernel)
        -   [[2.1.1] [Webcam]](#Webcam)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [CPU governor]](#CPU_governor)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Fn-keys]](#Fn-keys)

## [Hardware]

### [Standard]

  -------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------- ------------------------ ------------------ ---------------- --------------------------------------------------------------
  Device               Make/model                                                                                                                                                                               Status        Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  BIOS                 Winbond 25Q64CVSIG                                                                                                                                                                       Partial       N/A                      N/A                N/A              In-circuit programming is not working. Requires desoldering.
  CPU                  [Intel® Core™ i3-3110M](https://www.intel.com/content/www/us/en/products/sku/65700/intel-core-i33110m-processor-3m-cache-2-40-ghz/specifications.html)   Works         N/A                      N/A                5.15.26
  iGPU                 Intel Corporation 3rd Gen Core processor Graphics Controller                                                                                                                             Works         N/A                      i915               5.15.26
  dGPU                 Radeon HD 8570A/8570M                                                                                                                                                                    Not tested    N/A                      N/A                N/A              Requires firmware blobs.
  Sound                N/A                                                                                                                                                                                      Works         N/A                      N/A                5.15.26
  HDMI port            N/A                                                                                                                                                                                      Works         N/A                      N/A                5.15.26
  Ethernet             N/A                                                                                                                                                                                      Works         N/A                      alx                5.15.26
  Wi-Fi                N/A                                                                                                                                                                                      Not tested    N/A                      N/A                N/A              Requires firmware blobs.
  Bluetooth            N/A                                                                                                                                                                                      Not tested    N/A                      N/A                N/A              Requires firmware blobs.
  SD/MMC card reader   N/A                                                                                                                                                                                      Not tested    N/A                      N/A                N/A
  ODD                  N/A                                                                                                                                                                                      Not tested    N/A                      N/A                N/A
  Webcam               N/A                                                                                                                                                                                      Works         N/A                      uvcvideo           5.15.26
  -------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------- ------------------------ ------------------ ---------------- --------------------------------------------------------------

### [Detailed information]

`root `[`#`]`lscpu`

    Architecture:                    x86_64
    CPU op-mode(s):                  32-bit, 64-bit
    Address sizes:                   36 bits physical, 48 bits virtual
    Byte Order:                      Little Endian
    CPU(s):                          4
    On-line CPU(s) list:             0-3
    Vendor ID:                       GenuineIntel
    Model name:                      Intel(R) Core(TM) i3-3110M CPU @ 2.40GHz
    CPU family:                      6
    Model:                           58
    Thread(s) per core:              2
    Core(s) per socket:              2
    Socket(s):                       1
    Stepping:                        9
    CPU max MHz:                     2400.0000
    CPU min MHz:                     1200.0000
    BogoMIPS:                        4790.50
    Flags:                           fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic popcnt tsc_deadline_timer xsave avx f16c lahf_lm cpuid_fault epb pti tpr_shadow vnmi flexpriority ept vpid fsgsbase smep erms xsaveopt dtherm arat pln pts
    Virtualization:                  VT-x
    L1d cache:                       64 KiB (2 instances)
    L1i cache:                       64 KiB (2 instances)
    L2 cache:                        512 KiB (2 instances)
    L3 cache:                        3 MiB (1 instance)
    NUMA node(s):                    1
    NUMA node0 CPU(s):               0-3
    Vulnerability Itlb multihit:     KVM: Mitigation: VMX disabled
    Vulnerability L1tf:              Mitigation; PTE Inversion; VMX conditional cache flushes, SMT vulnerable
    Vulnerability Mds:               Vulnerable: Clear CPU buffers attempted, no microcode; SMT vulnerable
    Vulnerability Meltdown:          Mitigation; PTI
    Vulnerability Spec store bypass: Vulnerable
    Vulnerability Spectre v1:        Mitigation; usercopy/swapgs barriers and __user pointer sanitization
    Vulnerability Spectre v2:        Mitigation; Full generic retpoline, STIBP disabled, RSB filling
    Vulnerability Srbds:             Not affected
    Vulnerability Tsx async abort:   Not affected

`root `[`#`]`lspci`

    00:00.0 Host bridge: Intel Corporation 3rd Gen Core processor DRAM Controller (rev 09)
        Subsystem: Lenovo 3rd Gen Core processor DRAM Controller
    00:01.0 PCI bridge: Intel Corporation Xeon E3-1200 v2/3rd Gen Core processor PCI Express Root Port (rev 09)
        Kernel driver in use: pcieport
    00:02.0 VGA compatible controller: Intel Corporation 3rd Gen Core processor Graphics Controller (rev 09)
        Subsystem: Lenovo 3rd Gen Core processor Graphics Controller
        Kernel driver in use: i915
    00:14.0 USB controller: Intel Corporation 7 Series/C210 Series Chipset Family USB xHCI Host Controller (rev 04)
        Subsystem: Lenovo 7 Series/C210 Series Chipset Family USB xHCI Host Controller
        Kernel driver in use: xhci_hcd
    00:1a.0 USB controller: Intel Corporation 7 Series/C216 Chipset Family USB Enhanced Host Controller #2 (rev 04)
        Subsystem: Lenovo 7 Series/C216 Chipset Family USB Enhanced Host Controller
        Kernel driver in use: ehci-pci
    00:1b.0 Audio device: Intel Corporation 7 Series/C216 Chipset Family High Definition Audio Controller (rev 04)
        Subsystem: Lenovo 7 Series/C216 Chipset Family High Definition Audio Controller
        Kernel driver in use: snd_hda_intel
    00:1c.0 PCI bridge: Intel Corporation 7 Series/C216 Chipset Family PCI Express Root Port 1 (rev c4)
        Kernel driver in use: pcieport
    00:1d.0 USB controller: Intel Corporation 7 Series/C216 Chipset Family USB Enhanced Host Controller #1 (rev 04)
        Subsystem: Lenovo 7 Series/C216 Chipset Family USB Enhanced Host Controller
        Kernel driver in use: ehci-pci
    00:1f.0 ISA bridge: Intel Corporation HM76 Express Chipset LPC Controller (rev 04)
        Subsystem: Lenovo HM76 Express Chipset LPC Controller
        Kernel driver in use: lpc_ich
    00:1f.2 SATA controller: Intel Corporation 7 Series Chipset Family 6-port SATA Controller [AHCI mode] (rev 04)
        Subsystem: Lenovo 7 Series Chipset Family 6-port SATA Controller [AHCI mode]
        Kernel driver in use: ahci
    00:1f.3 SMBus: Intel Corporation 7 Series/C216 Chipset Family SMBus Controller (rev 04)
        Subsystem: Lenovo 7 Series/C216 Chipset Family SMBus Controller
        Kernel driver in use: i801_smbus
    01:00.0 Display controller: Advanced Micro Devices, Inc. [AMD/ATI] Sun PRO [Radeon HD 8570A/8570M]
        Subsystem: Lenovo Sun PRO [Radeon HD 8570A/8570M]
    02:00.0 Ethernet controller: Qualcomm Atheros QCA8172 Fast Ethernet (rev 10)
        Subsystem: Lenovo QCA8172 Fast Ethernet
        Kernel driver in use: alx

`root `[`#`]`lsusb`

    /:  Bus 04.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/4p, 5000M
        |__ Port 2: Dev 2, If 0, Class=Mass Storage, Driver=usb-storage, 5000M
    /:  Bus 03.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/4p, 480M
        |__ Port 1: Dev 2, If 0, Class=Human Interface Device, Driver=usbhid, 1.5M
        |__ Port 1: Dev 2, If 1, Class=Human Interface Device, Driver=usbhid, 1.5M
        |__ Port 4: Dev 4, If 0, Class=Video, Driver=uvcvideo, 480M
        |__ Port 4: Dev 4, If 1, Class=Video, Driver=uvcvideo, 480M
    /:  Bus 02.Port 1: Dev 1, Class=root_hub, Driver=ehci-pci/2p, 480M
        |__ Port 1: Dev 2, If 0, Class=Hub, Driver=hub/6p, 480M
    /:  Bus 01.Port 1: Dev 1, Class=root_hub, Driver=ehci-pci/2p, 480M
        |__ Port 1: Dev 2, If 0, Class=Hub, Driver=hub/6p, 480M
            |__ Port 4: Dev 3, If 0, Class=Vendor Specific Class, Driver=rtsx_usb, 480M

## [Installation]

### [Kernel]

[KERNEL] **Kernel 5.15.26 (gentoo-sources)**

    Processor type and features ->
      Processor family - Core 2/newer Xeon
      [ ] Enable 5-level page tables support
      [ ] Software Guard eXtensions (SGX)
    Power management and ACPI options ->
      CPU Frequency scaling ->
        -*-   'performance' governor
        -*-   'powersave' governor
        [*] ACPI Processor P-States driver
    Device Drivers ->
      Misc devices ->
        Realtek USB card reader
      Serial ATA and Parallel ATA drivers (libata)  --->
        [*] Intel ESB, ICH, PIIX3, PIIX4 PATA/SATA support
        [*] Intel SCH PATA support
      Network device support --->
      Network device support --->
        Ethernet driver support  --->
          [*]   Atheros devices
          [*]     Qualcomm Atheros AR816x/AR817x support
      Input device support --->
        Mice --->
          [*] PS/ mouse
      I2C support --->
        I2C Hardware Bus support  --->
          [*] Intel 82801 (ICH/PCH)
      Multifunction device drivers  --->
        [*] Intel ICH LPC
      Graphics support --->
        [*] Intel 8xx/9xx/G3x/G4x/HD Graphics
        [*/ ] ATI Radeon
        [*/ ] AMD GPU
      [*] Sound card support  --->
        [*]   Advanced Linux Sound Architecture  --->
          HD-Audio  --->
            [*] HD Audio PCI
            [*] Enable generic HD-audio codec parser
      HID support -->
        [*]   Generic HID driver
        USB HID support  --->
          [*] USB HID transport layer
      [*] X86 Platform Specific Device Drivers  --->
        [*]   Lenovo IdeaPad Laptop Extras
        [*]   ThinkPad ACPI Laptop Extras
        [*]     Console audio control ALSA interface
        [*]     Allow control of important LEDs (unsafe)
        [*]     Video output control support
        [*]     Support NVRAM polling for hot keys

#### [Webcam]

[KERNEL]

    Device Drivers  --->
    [*] Multimedia support  --->
      Media device types --->
        [*]   Cameras/video grabbers support
      Media drivers  --->
        [*]   Media USB Adapters  --->
          [*]   USB Video Class (UVC)

## [Configuration]

### [CPU governor]

[[[xfce-extra/xfce4-cpufreq-plugin]](https://packages.gentoo.org/packages/xfce-extra/xfce4-cpufreq-plugin)[]] allows viewing of CPU\'s governor status.

[FILE] **`/root/.bash_aliases`**

    alias perf="echo performance | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor"
    alias pow="echo powersave | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor"

## [Troubleshooting]

### [Fn-keys]

Function key is inderted like it is pressed, but every key works.

`root `[`#`]`dmesg > grep -ie error -e warn -e conflict`

    [    0.537040] acpi PNP0A08:00: _OSC: platform retains control of PCIe features (AE_ERROR)
    [    4.224064] amdgpu 0000:01:00.0: Direct firmware load for amdgpu/hainan_mc.bin failed with error -2
    [    4.225539] [drm:amdgpu_device_init.cold] *ERROR* sw_init of IP block <gmc_v6_0> failed -2
    [    4.225687] amdgpu 0000:01:00.0: amdgpu: Fatal error during GPU init
    [    4.225985] amdgpu: probe of 0000:01:00.0 failed with error -2
    [    4.264890] ACPI Warning: SystemIO range 0x0000000000000428-0x000000000000042F conflicts with OpRegion 0x0000000000000400-0x000000000000047F (\PMIO) (20210730/utaddress-204)
    [    4.264899] ACPI: OSL: Resource conflict; ACPI support missing from driver?
    [    4.264907] ACPI Warning: SystemIO range 0x0000000000000540-0x000000000000054F conflicts with OpRegion 0x0000000000000500-0x000000000000055F (\_SB.PCI0.PEG0.PEGP.GPIO) (20210730/utaddress-204)
    [    4.264913] ACPI Warning: SystemIO range 0x0000000000000540-0x000000000000054F conflicts with OpRegion 0x0000000000000500-0x0000000000000563 (\GPIO) (20210730/utaddress-204)
    [    4.264919] ACPI: OSL: Resource conflict; ACPI support missing from driver?
    [    4.264921] ACPI Warning: SystemIO range 0x0000000000000530-0x000000000000053F conflicts with OpRegion 0x0000000000000500-0x000000000000055F (\_SB.PCI0.PEG0.PEGP.GPIO) (20210730/utaddress-204)
    [    4.264927] ACPI Warning: SystemIO range 0x0000000000000530-0x000000000000053F conflicts with OpRegion 0x0000000000000500-0x0000000000000563 (\GPIO) (20210730/utaddress-204)
    [    4.264932] ACPI: OSL: Resource conflict; ACPI support missing from driver?
    [    4.264935] ACPI Warning: SystemIO range 0x0000000000000500-0x000000000000052F conflicts with OpRegion 0x0000000000000500-0x000000000000055F (\_SB.PCI0.PEG0.PEGP.GPIO) (20210730/utaddress-204)
    [    4.264942] ACPI Warning: SystemIO range 0x0000000000000500-0x000000000000052F conflicts with OpRegion 0x0000000000000500-0x0000000000000563 (\GPIO) (20210730/utaddress-204)
    [    4.264948] ACPI: OSL: Resource conflict; ACPI support missing from driver?
    [    4.264951] lpc_ich: Resource conflict(s) found affecting gpio_ich
    [    5.458230] platform regulatory.0: Direct firmware load for regulatory.db failed with error -2