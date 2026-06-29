**Resources**

[[]][Official Support Page](https://www.dell.com/support/home/en-us/product-support/product/inspiron-15-5515-laptop/overview)

[[]][Specifications](https://dl.dell.com/content/manual31633392-inspiron-15-5515-setup-and-specifications.pdf)

[[]][Hardware Maintenance Manual](https://dl.dell.com/content/manual45760195-inspiron-15-5515-service-manual.pdf)

[[]][Dell Inspiron](https://en.wikipedia.org/wiki/Dell_Inspiron "wikipedia:Dell Inspiron")

The **Dell Inspiron 15 5515** is a laptop manufactured by Dell Technologies.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [Accessories]](#Accessories)
    -   [[1.3] [Detailed information]](#Detailed_information)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Firmware]](#Firmware)
    -   [[2.2] [Kernel]](#Kernel)
        -   [[2.2.1] [Touchpad & touch screen]](#Touchpad_.26_touch_screen)
        -   [[2.2.2] [Webcam]](#Webcam)
        -   [[2.2.3] [Sound & Microphone]](#Sound_.26_Microphone)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [F keys]](#F_keys)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Touch pad gestures don\'t work, touch screen doesn\'t work]](#Touch_pad_gestures_don.27t_work.2C_touch_screen_doesn.27t_work)
-   [[5] [External resources]](#External_resources)

## [Hardware]

### [Standard]

  -------------------- -------------------------------------------------------------------------------------------------------------- -------- ------------------------ ------------------ ---------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Device               Make/model                                                                                                     Status   Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  CPU                  AMD Ryzen 5 5500U/5700U                                                                                        Works    N/A                      N/A                5.15.26
  Video card           AMD Lucienne \[Radeon Vega 7/8\]                                                                               Works    1002:1637                amdgpu             5.15.26
  Touchpad             Dell                                                                                                           Works    27C6:0D42                i2c-hid            5.15.26          Requires specific configuration, see below
  Touch screen         Dell                                                                                                           Works    04F3:2C6B                i2c-hid            5.15.26          Requires specific configuration, see below
  Fingerprint Reader   Goodix MOC Fingerprint sensor                                                                                  Works    27C6:639C                N/A                5.15.26          Works with [[[sys-auth/fprintd]](https://packages.gentoo.org/packages/sys-auth/fprintd)[]]
  Webcam               Microdia                                                                                                       Works    0C45:6725                uvcvideo           5.15.26
  Microphone           Dell                                                                                                           Works    N/A                      N/A                5.15.26
  Wi-Fi                [Qualcomm Atheros QCA6174](https://wiki.gentoo.org/wiki/Qualcomm_Atheros_QCA6174 "Qualcomm Atheros QCA6174")   Works    168C:003E                ath10k_pci         5.15.26
  USB                  AMD Renoir/Cezanne USB 3.1                                                                                     Works    1022:1639                xhci_hcd           5.15.26
  TPM                  fTPM 2.0                                                                                                       Works    N/A                      tpm_crb, tpm_tis   5.15.26
  -------------------- -------------------------------------------------------------------------------------------------------------- -------- ------------------------ ------------------ ---------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Accessories]

  -------- ------------ -------- ------------------------ ------------------ ---------------- --------------------------------------------------------------
  Device   Make/model   Status   Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  Dock     Dell WD19S   Works    N/A                      N/A                5.15.26          The power button on the dock does not work (it does nothing)
  -------- ------------ -------- ------------------------ ------------------ ---------------- --------------------------------------------------------------

### [Detailed information]

`root `[`#`]`lspci`

    00:00.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne Root Complex
    00:00.2 IOMMU: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne IOMMU
    00:01.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir PCIe Dummy Host Bridge
    00:01.2 PCI bridge: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne PCIe GPP Bridge
    00:02.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir PCIe Dummy Host Bridge
    00:02.2 PCI bridge: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne PCIe GPP Bridge
    00:08.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir PCIe Dummy Host Bridge
    00:08.1 PCI bridge: Advanced Micro Devices, Inc. [AMD] Renoir Internal PCIe GPP Bridge to Bus
    00:08.2 PCI bridge: Advanced Micro Devices, Inc. [AMD] Renoir Internal PCIe GPP Bridge to Bus
    00:14.0 SMBus: Advanced Micro Devices, Inc. [AMD] FCH SMBus Controller (rev 51)
    00:14.3 ISA bridge: Advanced Micro Devices, Inc. [AMD] FCH LPC Bridge (rev 51)
    00:18.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 0
    00:18.1 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 1
    00:18.2 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 2
    00:18.3 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 3
    00:18.4 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 4
    00:18.5 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 5
    00:18.6 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 6
    00:18.7 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 7
    01:00.0 Non-Volatile memory controller: KIOXIA Corporation Device 0001
    02:00.0 Network controller: Qualcomm Atheros QCA6174 802.11ac Wireless Network Adapter (rev 32)
    03:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Lucienne (rev c2)
    03:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Renoir Radeon High Definition Audio Controller
    03:00.2 Encryption controller: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 10h-1fh) Platform Security Processor
    03:00.3 USB controller: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne USB 3.1
    03:00.4 USB controller: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne USB 3.1
    03:00.5 Multimedia controller: Advanced Micro Devices, Inc. [AMD] Raven/Raven2/FireFlight/Renoir Audio Processor (rev 01)
    03:00.6 Audio device: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 10h-1fh) HD Audio Controller
    04:00.0 SATA controller: Advanced Micro Devices, Inc. [AMD] FCH SATA Controller [AHCI mode] (rev 81)
    04:00.1 SATA controller: Advanced Micro Devices, Inc. [AMD] FCH SATA Controller [AHCI mode] (rev 81)

`user `[`$`]`cat /proc/cpuinfo`

    processor   : 0
    vendor_id   : AuthenticAMD
    cpu family  : 23
    model       : 104
    model name  : AMD Ryzen 5 5500U with Radeon Graphics
    stepping    : 1
    microcode   : 0x8608103
    cpu MHz     : 2100.000
    cache size  : 512 KB
    physical id : 0
    siblings    : 12
    core id     : 0
    cpu cores   : 6
    apicid      : 0
    initial apicid  : 0
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 16
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 hw_pstate ssbd mba ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 cqm rdt_a rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local clzero irperf xsaveerptr rdpru wbnoinvd arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip rdpid overflow_recov succor smca
    bugs        : sysret_ss_attrs spectre_v1 spectre_v2 spec_store_bypass
    bogomips    : 4192.33
    TLB size    : 3072 4K pages
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 48 bits physical, 48 bits virtual
    power management: ts ttp tm hwpstate cpb eff_freq_ro [13] [14]

## [Installation]

### [Firmware]

The [AMDGPU](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU") driver requires the following [firmware](https://wiki.gentoo.org/wiki/Linux_firmware "Linux firmware"):

-   amdgpu/renoir_sdma.bin
-   amdgpu/renoir_asd.bin
-   amdgpu/renoir_ta.bin
-   amdgpu/renoir_pfp.bin
-   amdgpu/renoir_me.bin
-   amdgpu/renoir_ce.bin
-   amdgpu/renoir_rlc.bin
-   amdgpu/renoir_mec.bin
-   amdgpu/renoir_dmcub.bin
-   amdgpu/renoir_vcn.bin

\
The Atheros driver requires the following firmware:

-   ath10k/QCA6174/hw3.0/firmware-6.bin
-   ath10k/QCA6174/hw3.0/board-2.bin

### [Kernel]

#### [][Touchpad & touch screen]

For the touchpad and touch screen to work correctly, the following drivers are needed:

[KERNEL] **Enable support for touchpad and touch screen**

    Processor type and features  --->
        [*] AMD ACPI2Platform devices support
    Device Drivers  --->
        -*- Pin controllers  --->
            <*> AMD GPIO pin control
        HID support  --->
            Special HID drivers  --->
                <*> HID Multitouch panels
            I2C HID support  --->
                <*> HID over I2C transport layer
        I2C support  --->
            I2C Hardware Bus support  --->
                <*> AMD MP2 PCIe
                <*> Synopsys DesignWare Platform
                <*> Synopsys DesignWare PCI
        Input device support  --->
            Mice  --->
                <*> ELAN I2C Touchpad support
                [*] Enable I2C support
                [*] Enable SMbus support

#### [Webcam]

For the webcam, the following drivers are required:

[KERNEL] **Enable support for the webcam**

    Device Drivers  --->
        [*] Multimedia support  --->
            [*] Filter media drivers
                Media Device Types  --->
                    [*] Cameras and video grabbers
                Video4Linux options  --->
                    [*] V4L2 sub-device userspace API
                Media Drivers  --->
                    [*] USB Video Class (UVC)
                    [*]   UVC input events device support

#### [][Sound & Microphone]

For sound and the microphone to work, you need to enable the AMD Renoir audio drivers:

[KERNEL] **Enable audio support**

    Device Drivers  --->
         <*> Sound card support  --->
            <*>   Advanced Linux Sound Architecture  --->
                [*]   PCI sound devices  --->
                HD-Audio  --->
                    <*> HD Audio PCI
                    <*> Build Realtek HD-audio codec support
                    <*> Build HDMI/DisplayPort HD-audio codec support
                <*> ALSA for SoC audio support  --->
                    <*> AMD Audio Coprocessor-v3.x support
                    <*> AMD Audio Coprocessor - Renoir support
                    <*>   AMD Renoir support for DMIC

** Note**\
None of the items under \"PCI sound devices\" need to be selected. SND_PCI is just needed to enable HD-Audio.

## [Configuration]

### [F keys]

By default, the F keypresses default to their media/Fn function, rather than the F key itself. This can be changed in the BIOS.

## [Troubleshooting]

### [][Touch pad gestures don\'t work, touch screen doesn\'t work]

Makes sure the drivers from the above Kernel section are installed.

## [External resources]

-   [Gentoo forum thread about the touch pad on this laptop](https://forums.gentoo.org/viewtopic-t-1147207-postdays-0-postorder-asc-start-0.html?sid=360d1da3f480aa6b1334fa8485ea8e4c)