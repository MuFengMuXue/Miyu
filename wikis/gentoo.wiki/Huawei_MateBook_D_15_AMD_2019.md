**Resources**

[[]][Official Support Page](https://consumer.huawei.com/en/support/laptops/matebook-d-15-amd/)

[[]][Huawei MateBook series](https://en.wikipedia.org/wiki/Huawei_MateBook_series "wikipedia:Huawei MateBook series")

There are different Huawei laptops models for MateBook series. In this page, the model will be AMD version of Huawei Laptop D 15 released on 2019.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [CPU]](#CPU)
    -   [[1.2] [GPU]](#GPU)
    -   [[1.3] [RAM]](#RAM)
    -   [[1.4] [SSD]](#SSD)
    -   [[1.5] [Wireless]](#Wireless)
    -   [[1.6] [Sound]](#Sound)
    -   [[1.7] [lspci]](#lspci)
    -   [[1.8] [lsusb]](#lsusb)
-   [[2] [Blobs]](#Blobs)
    -   [[2.1] [AMDGPU]](#AMDGPU)
-   [[3] [Kernel]](#Kernel)
    -   [[3.1] [Graphics]](#Graphics)
    -   [[3.2] [Sound]](#Sound_2)
    -   [[3.3] [Wireless]](#Wireless_2)
    -   [[3.4] [Keyboard]](#Keyboard)
    -   [[3.5] [Touchpad]](#Touchpad)

## [Hardware]

### [CPU]

There are 2 versions available: AMD Ryzen 5 3500U (used here) and AMD Ryzen 7 3700U.

`user `[`$`]`lscpu`

    Architecture:                       x86_64
    CPU op-mode(s):                     32-bit, 64-bit
    Address sizes:                      43 bits physical, 48 bits virtual
    Byte Order:                         Little Endian
    CPU(s):                             8
    On-line CPU(s) list:                0-7
    Vendor ID:                          AuthenticAMD
    BIOS Vendor ID:                     Advanced Micro Devices, Inc.
    Model name:                         AMD Ryzen 5 3500U with Radeon Vega Mobile Gfx
    BIOS Model name:                    AMD Ryzen 5 3500U with Radeon Vega Mobile Gfx   NULL CPU @ 2.1GHz
    BIOS CPU family:                    107
    CPU family:                         23
    Model:                              24
    Thread(s) per core:                 2
    Core(s) per socket:                 4
    Socket(s):                          1
    Stepping:                           1
    Frequency boost:                    enabled
    CPU(s) scaling MHz:                 65%
    CPU max MHz:                        2100.0000
    CPU min MHz:                        1400.0000
    BogoMIPS:                           4193.78
    Flags:                              fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb hw_pstate ssbd ibpb vmmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap clflushopt sha_ni xsaveopt xsavec xgetbv1 clzero irperf xsaveerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif overflow_recov succor smca sev sev_es

### [GPU]

There are 2 versions available: Radeon Vega 8 Graphics (used here) and Radeon Vega 10 Graphics.

`root `[`#`]`lscpi -k -s 03:00.0`

    03:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Picasso/Raven 2 [Radeon Vega Series / Radeon Vega Mobile Series] [1002:15d8] (rev c2)
        Subsystem: Huawei Technologies Co., Ltd. Picasso/Raven 2 [Radeon Vega Series / Radeon Vega Mobile Series] [19e5:3e18]
        Kernel driver in use: amdgpu
        Kernel modules: amdgpu

### [RAM]

RAM is DDR4 and the RAM modules are not upgradable.

The capacity of RAM modules:

`root `[`#`]`dmidecode -t memory | grep -i size`

     Size: 4 GB
        Size: 4 GB

The frequency of RAM modulesː

`root `[`#`]`dmidecode -t memory | grep 'Memory Speed'`

      Configured Memory Speed: 2400 MT/s
        Configured Memory Speed: 2400 MT/s

### [SSD]

The storage slot is PCIe 3.0 NVMe SSD.

The original storage was changed.

`root `[`#`]`lscpi -k -s 01:00.0`

    01:00.0 Non-Volatile memory controller [0108]: Samsung Electronics Co Ltd NVMe SSD Controller SM981/PM981/PM983 [144d:a808]
        Subsystem: Samsung Electronics Co Ltd NVMe SSD Controller SM981/PM981/PM983 (SSD 970 EVO) [144d:a801]
        Kernel driver in use: nvme
        Kernel modules: nvme

### [Wireless]

The original Mini PCIe card was changed.

`root `[`#`]`lscpi -k -s 02:00.0`

    02:00.0 Network controller [0280]: Qualcomm Atheros AR9462 Wireless Network Adapter [168c:0034] (rev 01)
        Subsystem: AzureWave AR9462 Wireless Network Adapter [1a3b:2234]
        Kernel driver in use: ath9k
        Kernel modules: ath9k

### [Sound]

For laptop speakers and HDMI/DP is used Realtek HD Audio Controller.

`root `[`#`]`lscpi -k -s 03:00.6`

    03:00.6 Audio device [0403]: Advanced Micro Devices, Inc. [AMD] Family 17h/19h HD Audio Controller [1022:15e3]
        Subsystem: Huawei Technologies Co., Ltd. Family 17h/19h HD Audio Controller [19e5:3e18]
        Kernel driver in use: snd_hda_intel
        Kernel modules: snd_hda_intel

`root `[`#`]`lscpi -k -s 03:00.1`

    03:00.1 Audio device [0403]: Advanced Micro Devices, Inc. [AMD/ATI] Raven/Raven2/Fenghuang HDMI/DP Audio Controller [1002:15de]
        Subsystem: Huawei Technologies Co., Ltd. Raven/Raven2/Fenghuang HDMI/DP Audio Controller [19e5:3e18]
        Kernel driver in use: snd_hda_intel
        Kernel modules: snd_hda_intel

### [lspci]

`root `[`#`]`lspci -nnk`

    00:00.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Root Complex [1022:15d0]
        Subsystem: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Root Complex [1022:15d0]
    00:00.2 IOMMU [0806]: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 IOMMU [1022:15d1]
        Subsystem: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 IOMMU [1022:15d1]
    00:01.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-1fh) PCIe Dummy Host Bridge [1022:1452]
    00:01.3 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 PCIe GPP Bridge [6:0] [1022:15d3]
        Subsystem: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 PCIe GPP Bridge [6:0] [1022:1453]
        Kernel driver in use: pcieport
    00:01.7 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 PCIe GPP Bridge [6:0] [1022:15d3]
        Subsystem: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 PCIe GPP Bridge [6:0] [1022:1453]
        Kernel driver in use: pcieport
    00:08.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-1fh) PCIe Dummy Host Bridge [1022:1452]
    00:08.1 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Internal PCIe GPP Bridge 0 to Bus A [1022:15db]
        Subsystem: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Internal PCIe GPP Bridge 0 to Bus A [1022:0000]
        Kernel driver in use: pcieport
    00:14.0 SMBus [0c05]: Advanced Micro Devices, Inc. [AMD] FCH SMBus Controller [1022:790b] (rev 61)
        Subsystem: Huawei Technologies Co., Ltd. FCH SMBus Controller [19e5:3e18]
        Kernel driver in use: piix4_smbus
        Kernel modules: i2c_piix4, sp5100_tco
    00:14.3 ISA bridge [0601]: Advanced Micro Devices, Inc. [AMD] FCH LPC Bridge [1022:790e] (rev 51)
        Subsystem: Huawei Technologies Co., Ltd. FCH LPC Bridge [19e5:3e18]
    00:18.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 0 [1022:15e8]
    00:18.1 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 1 [1022:15e9]
    00:18.2 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 2 [1022:15ea]
    00:18.3 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 3 [1022:15eb]
        Kernel driver in use: k10temp
        Kernel modules: k10temp
    00:18.4 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 4 [1022:15ec]
    00:18.5 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 5 [1022:15ed]
    00:18.6 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 6 [1022:15ee]
    00:18.7 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 7 [1022:15ef]
    01:00.0 Non-Volatile memory controller [0108]: Samsung Electronics Co Ltd NVMe SSD Controller SM981/PM981/PM983 [144d:a808]
        Subsystem: Samsung Electronics Co Ltd NVMe SSD Controller SM981/PM981/PM983 (SSD 970 EVO) [144d:a801]
        Kernel driver in use: nvme
        Kernel modules: nvme
    02:00.0 Network controller [0280]: Qualcomm Atheros AR9462 Wireless Network Adapter [168c:0034] (rev 01)
        Subsystem: AzureWave AR9462 Wireless Network Adapter [1a3b:2234]
        Kernel driver in use: ath9k
        Kernel modules: ath9k
    03:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Picasso/Raven 2 [Radeon Vega Series / Radeon Vega Mobile Series] [1002:15d8] (rev c2)
        Subsystem: Huawei Technologies Co., Ltd. Picasso/Raven 2 [Radeon Vega Series / Radeon Vega Mobile Series] [19e5:3e18]
        Kernel driver in use: amdgpu
        Kernel modules: amdgpu
    03:00.1 Audio device [0403]: Advanced Micro Devices, Inc. [AMD/ATI] Raven/Raven2/Fenghuang HDMI/DP Audio Controller [1002:15de]
        Subsystem: Huawei Technologies Co., Ltd. Raven/Raven2/Fenghuang HDMI/DP Audio Controller [19e5:3e18]
        Kernel driver in use: snd_hda_intel
        Kernel modules: snd_hda_intel
    03:00.2 Encryption controller [1080]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 10h-1fh) Platform Security Processor [1022:15df]
        Subsystem: Huawei Technologies Co., Ltd. Family 17h (Models 10h-1fh) Platform Security Processor [19e5:3e18]
        Kernel driver in use: ccp
        Kernel modules: ccp
    03:00.3 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Raven USB 3.1 [1022:15e0]
        Subsystem: Huawei Technologies Co., Ltd. Raven USB 3.1 [19e5:3e18]
        Kernel driver in use: xhci_hcd
        Kernel modules: xhci_pci
    03:00.4 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Raven USB 3.1 [1022:15e1]
        Subsystem: Huawei Technologies Co., Ltd. Raven USB 3.1 [19e5:3e18]
        Kernel driver in use: xhci_hcd
        Kernel modules: xhci_pci
    03:00.5 Multimedia controller [0480]: Advanced Micro Devices, Inc. [AMD] ACP/ACP3X/ACP6x Audio Coprocessor [1022:15e2]
        Subsystem: Huawei Technologies Co., Ltd. ACP/ACP3X/ACP6x Audio Coprocessor [19e5:3e18]
        Kernel driver in use: snd_pci_acp3x
        Kernel modules: snd_pci_acp3x, snd_rn_pci_acp3x
    03:00.6 Audio device [0403]: Advanced Micro Devices, Inc. [AMD] Family 17h/19h HD Audio Controller [1022:15e3]
        Subsystem: Huawei Technologies Co., Ltd. Family 17h/19h HD Audio Controller [19e5:3e18]
        Kernel driver in use: snd_hda_intel
        Kernel modules: snd_hda_intel

### [lsusb]

`user `[`$`]`lsusb`

    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 001 Device 002: ID 05e3:0610 Genesys Logic, Inc. Hub
    Bus 001 Device 003: ID 27c6:5110 Shenzhen Goodix Technology Co.,Ltd. Goodix Fingerprint Device
    Bus 001 Device 004: ID 13d3:56f9 IMC Networks ov9734_azurewave_camera
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub

## [Blobs]

### [AMDGPU]

Firmware blobs required for GPU are:

`user `[`$`]`echo amdgpu/*`

    amdgpu/picasso_asd.bin amdgpu/picasso_ce.bin amdgpu/picasso_gpu_info.bin amdgpu/picasso_me.bin amdgpu/picasso_mec2.bin amdgpu/picasso_mec.bin amdgpu/picasso_pfp.bin amdgpu/picasso_rlc.bin amdgpu/picasso_sdma.bin amdgpu/picasso_ta.bin amdgpu/picasso_vcn.bin amdgpu/raven_dmcu.bin

## [Kernel]

### [Graphics]

For Radeon Vega 8 Graphics or Radeon Vega 10 Graphics:

[KERNEL]

        Processor type and features  --->
            [*] MTRR (Memory Type Range Register) support
        Device Drivers  --->
                Graphics support  --->
                    <M> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support) --->
                    [*] Enable legacy fbdev support for your modesetting driver
                    <M> AMD GPU
                          Display Engine Configuration  --->
                              [*] AMD DC - Enable new display engine

### [Sound]

The motherboard uses Realtek HD Audio.

[KERNEL]

        Device Drivers  --->
            <M> Sound card support  --->
                    --- Sound card support
                    <M>   Advanced Linux Sound Architecture  --->
                            --- Advanced Linux Sound Architecture
                            [*]   PCI sound devices  --->
                                  HD-Audio  --->
                                    <M> HD Audio PCI
                                    <M> Build Realtek HD-audio codec support
                                    <M> Build HDMI/DisplayPort HD-audio codec support
                                    -M- Enable generic HD-audio codec parser
                            <M>   ALSA for SoC audio support  --->
                                    --- ALSA for SoC audio support
                                    <M>   AMD Audio Coprocessor-v3.x support

### [Wireless]

The motheboard does not have whitelist for Mini PCIe wireless card.

For Qualcomm Atheros AR9462 (the original Mini PCIe wireless card was replaced by a blobless wireless card):

[KERNEL]

    [*] Networking support  --->
            --- Networking support
            [*]   Wireless  --->
                    --- Wireless
                    <M>   cfg80211 - wireless configuration API
                    <M>   Generic IEEE 802.11 Networking Stack (mac80211)
                    [*]   Minstrel
        Device Drivers  --->
                Network device support  --->
                    --- Network device support
                    [*]   Wireless LAN  --->
                            [*] Atheros/Qualcomm devices
                            <M>   Atheros 802.11n wireless cards support
                            [*]     Atheros ath9k PCI/PCIe bus support
                            [*]     Atheros ath9k support for PC OEM cards
    -*- Cryptographic API --->
            --- Cryptographic API
                  Accelerated Cryptographic Algorithms for CPU (x86)  --->
                      <*> Ciphers: AES, modes: ECB, CBC, CTS, CTR, XTR, XTS, GCM (AES-NI)

### [Keyboard]

The keyboard is connected as AT keyboard.

[KERNEL]

        Device Drivers  --->
                Input device support  --->
                    -*- Generic input layer (needed for keyboard, mouse, ...)
                    [*]   Keyboards  --->
                            --- Keyboards
                            <*>   AT keyboard
                        Hardware I/O ports --->
                            -*- Serial I/O support
                            -*- i8042 PC Keyboard controller
                            -*- PS/2 driver library

### [Touchpad]

The touchpad is an ELAN 2204 model, it is connected by i2c protocol.

[KERNEL]

        Processor type and features  --->
            [*] AMD ACPI2Platform devices support
        Device Drivers  --->
                Input device support  --->
                        Mice  --->
                            <*> ELAN I2C Touchpad support
                            [*]   Enable I2C support
                            [*]   Enable SMbus support
                I2C support  --->
                        I2C Hardware Bus support  --->
                            <*> AMD MP2 PCIe
                            <*> Synopsys DesignWare Platform
                            <*> Synopsys DesignWare PCI
            -*- Pin controllers  --->
                    [*] AMD GPIO pin control
            [*] HID bus support  --->
                    --- HID bus support
                    <M>   Generic HID driver
                          Special HID drivers --->
                              <M> HID Multitouch panels
                    <M> I2C HID support  --->
                            --- I2C HID support
                            <M>   HID over I2C transport layer ACPI driver