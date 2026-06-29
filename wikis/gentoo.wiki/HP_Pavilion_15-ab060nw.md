**Resources**

[[]][Official Support Page](https://support.hp.com/us-en/product/details/hp-pavilion-15-ab000-notebook-pc-series/model/8875993)

[[]][Specifications](https://support.hp.com/us-en/document/c04769970)

[[]][Hardware Maintenance Manual](https://h10032.www1.hp.com/ctg/Manual/c04642845.pdf)

[[]][User Guide](https://h10032.www1.hp.com/ctg/Manual/c04631569.pdf)

[[]][HP Pavilion](https://en.wikipedia.org/wiki/HP_Pavilion "wikipedia:HP Pavilion")

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [BIOS]](#BIOS)
    -   [[1.2] [CPU]](#CPU)
    -   [[1.3] [Webcam]](#Webcam)
    -   [[1.4] [Touchpad]](#Touchpad)
    -   [[1.5] [Keyboard]](#Keyboard)
    -   [[1.6] [Accelerometer]](#Accelerometer)

## [Hardware]

`root `[`#`]`lspci -k`

    00:00.0 Host bridge: Intel Corporation Broadwell-U Host Bridge -OPI (rev 09)
        Subsystem: Hewlett-Packard Company Broadwell-U Host Bridge -OPI
        Kernel driver in use: bdw_uncore
    00:02.0 VGA compatible controller: Intel Corporation HD Graphics 5500 (rev 09)
        Subsystem: Hewlett-Packard Company HD Graphics 5500
        Kernel driver in use: i915
        Kernel modules: i915
    00:03.0 Audio device: Intel Corporation Broadwell-U Audio Controller (rev 09)
        Subsystem: Hewlett-Packard Company Broadwell-U Audio Controller
        Kernel driver in use: snd_hda_intel
        Kernel modules: snd_hda_intel
    00:04.0 Signal processing controller: Intel Corporation Broadwell-U Processor Thermal Subsystem (rev 09)
        Subsystem: Hewlett-Packard Company Broadwell-U Processor Thermal Subsystem
        Kernel driver in use: proc_thermal
        Kernel modules: processor_thermal_device
    00:14.0 USB controller: Intel Corporation Wildcat Point-LP USB xHCI Controller (rev 03)
        Subsystem: Hewlett-Packard Company Wildcat Point-LP USB xHCI Controller
        Kernel driver in use: xhci_hcd
        Kernel modules: xhci_pci
    00:16.0 Communication controller: Intel Corporation Wildcat Point-LP MEI Controller #1 (rev 03)
        Subsystem: Hewlett-Packard Company Wildcat Point-LP MEI Controller
        Kernel driver in use: mei_me
        Kernel modules: mei_me
    00:1b.0 Audio device: Intel Corporation Wildcat Point-LP High Definition Audio Controller (rev 03)
        Subsystem: Hewlett-Packard Company Wildcat Point-LP High Definition Audio Controller
        Kernel driver in use: snd_hda_intel
        Kernel modules: snd_hda_intel
    00:1c.0 PCI bridge: Intel Corporation Wildcat Point-LP PCI Express Root Port #1 (rev e3)
        Kernel driver in use: pcieport
        Kernel modules: shpchp
    00:1c.1 PCI bridge: Intel Corporation Wildcat Point-LP PCI Express Root Port #2 (rev e3)
        Kernel driver in use: pcieport
        Kernel modules: shpchp
    00:1c.2 PCI bridge: Intel Corporation Wildcat Point-LP PCI Express Root Port #3 (rev e3)
        Kernel driver in use: pcieport
        Kernel modules: shpchp
    00:1c.3 PCI bridge: Intel Corporation Wildcat Point-LP PCI Express Root Port #4 (rev e3)
        Kernel driver in use: pcieport
        Kernel modules: shpchp
    00:1c.4 PCI bridge: Intel Corporation Wildcat Point-LP PCI Express Root Port #5 (rev e3)
        Kernel driver in use: pcieport
        Kernel modules: shpchp
    00:1f.0 ISA bridge: Intel Corporation Wildcat Point-LP LPC Controller (rev 03)
        Subsystem: Hewlett-Packard Company Wildcat Point-LP LPC Controller
        Kernel driver in use: lpc_ich
        Kernel modules: lpc_ich
    00:1f.2 SATA controller: Intel Corporation Wildcat Point-LP SATA Controller [AHCI Mode] (rev 03)
        Subsystem: Hewlett-Packard Company Wildcat Point-LP SATA Controller [AHCI Mode]
        Kernel driver in use: ahci
        Kernel modules: ahci
    00:1f.3 SMBus: Intel Corporation Wildcat Point-LP SMBus Controller (rev 03)
        Subsystem: Hewlett-Packard Company Wildcat Point-LP SMBus Controller
        Kernel driver in use: i801_smbus
        Kernel modules: i2c_i801
    02:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS522A PCI Express Card Reader (rev 01)
        Subsystem: Hewlett-Packard Company RTS522A PCI Express Card Reader
        Kernel driver in use: rtsx_pci
        Kernel modules: rtsx_pci
    08:00.0 Network controller: Realtek Semiconductor Co., Ltd. RTL8723BE PCIe Wireless Network Adapter
        Subsystem: Hewlett-Packard Company RTL8723BE PCIe Wireless Network Adapter
        Kernel driver in use: rtl8723be
        Kernel modules: rtl8723be
    09:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8101/2/6E PCI Express Fast/Gigabit Ethernet controller (rev 0a)
        Subsystem: Hewlett-Packard Company RTL8101/2/6E PCI Express Fast/Gigabit Ethernet controller
        Kernel driver in use: r8169
        Kernel modules: r8169
    0a:00.0 3D controller: NVIDIA Corporation GM108M [GeForce 940M] (rev ff)
        Kernel modules: nouveau, nvidia_drm, nvidia

### [BIOS]

`user `[`$`]`dmidecode | sed -n '/BIOS Information/,/^$/p'`

    BIOS Information
        Vendor: Insyde
        Version: F.83
        Release Date: 03/29/2017
        Address: 0xE0000
        Runtime Size: 128 kB
        ROM Size: 6144 kB
        Characteristics:
            PCI is supported
            BIOS is upgradeable
            BIOS shadowing is allowed
            Boot from CD is supported
            Selectable boot is supported
            EDD is supported
            Japanese floppy for NEC 9800 1.2 MB is supported (int 13h)
            Japanese floppy for Toshiba 1.2 MB is supported (int 13h)
            5.25"/360 kB floppy services are supported (int 13h)
            5.25"/1.2 MB floppy services are supported (int 13h)
            3.5"/720 kB floppy services are supported (int 13h)
            3.5"/2.88 MB floppy services are supported (int 13h)
            8042 keyboard services are supported (int 9h)
            CGA/mono video services are supported (int 10h)
            ACPI is supported
            USB legacy is supported
            BIOS boot specification is supported
            Targeted content distribution is supported
            UEFI is supported
        BIOS Revision: 15.131
        Firmware Revision: 89.51

### [CPU]

`user `[`$`]`lscpu`

    Architecture:          x86_64
    CPU op-mode(s):        32-bit, 64-bit
    Byte Order:            Little Endian
    CPU(s):                4
    On-line CPU(s) list:   0-3
    Thread(s) per core:    2
    Core(s) per socket:    2
    Socket(s):             1
    NUMA node(s):          1
    Vendor ID:             GenuineIntel
    CPU family:            6
    Model:                 61
    Model name:            Intel(R) Core(TM) i5-5200U CPU @ 2.20GHz
    Stepping:              4
    CPU MHz:               2499.975
    CPU max MHz:           2700,0000
    CPU min MHz:           500,0000
    BogoMIPS:              4399.95
    Virtualization:        VT-x
    L1d cache:             32K
    L1i cache:             32K
    L2 cache:              256K
    L3 cache:              3072K
    NUMA node0 CPU(s):     0-3
    Flags:                 fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch epb intel_pt tpr_shadow vnmi flexpriority ept vpid fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap xsaveopt dtherm ida arat pln pts

### [Webcam]

`user `[`$`]`cat /sys/class/input/input21/name`

    HP Truevision HD

`user `[`$`]`grep DRIVER /sys/class/input/input21/device/uevent`

    DRIVER=uvcvideo

### [Touchpad]

`user `[`$`]`cat /sys/devices/platform/i8042/serio1/input/input100/name`

    SynPS/2 Synaptics TouchPad

`user `[`$`]`grep DRIVER /sys/devices/platform/i8042/serio1/input/input100/device/uevent`

    DRIVER=psmouse

### [Keyboard]

`user `[`$`]`cat /sys/devices/platform/i8042/serio0/input/input18/name`

    AT Translated Set 2 keyboard

`user `[`$`]`grep DRIVER /sys/devices/platform/i8042/serio0/input/input18/device/uevent`

    DRIVER=atkbd

### [Accelerometer]

`user `[`$`]`cat /sys/devices/platform/lis3lv02d/input/input8/name`

    ST LIS3LV02DL Accelerometer

`user `[`$`]`modinfo lis3lv02d`

    filename:       /lib/modules/4.11.3-gentoo-ARCH-200/kernel/drivers/misc/lis3lv02d/lis3lv02d.ko.gz
    license:        GPL
    author:         Yan Burman, Eric Piel, Pavel Machek
    description:    ST LIS3LV02Dx three-axis digital accelerometer driver
    depends:        input-polldev
    intree:         Y
    vermagic:       4.11.3-gentoo-ARCH-200 SMP preempt mod_unload modversions
    parm:           axes:Axis-mapping for x,y,z directions (array of axis)