**Resources**

[[]][Home](https://www.lenovo.com/us/en/laptops/thinkpad/thinkpad-e-series/ThinkPad-E485/p/22TP2TEE485)

[[]][Official Support Page](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-edge-laptops/thinkpad-e485-type-20ku)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_E485/ThinkPad_E485_Spec.PDF)

[[]][Specifications (by region)](https://psref.lenovo.com/Product/ThinkPad/ThinkPad_E485)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/pccbbs/mobiles_pdf/tp-e480-e485-r480-hmm-en.pdf)

[[]][User Guide](https://download.lenovo.com/pccbbs/mobiles_pdf/e485_ug_en.pdf)

[[]][BIOS Setup](https://download.lenovo.com/pccbbs/mobiles_pdf/lenovo_bios_setup_linux_wmi_sysfs_1.2.pdf)

The Lenovo ThinkPad E485 is a business laptop aimed at SMB. It is one of the early laptops with an AMD Ryzen CPU with integrated graphics. The laptop has a solid build, a good keyboard, and a nice 14\" 1920x1080 display. It is possible to have both NMVe and an SSD or spinning hard disk. It is cheaper than most other ThinkPads, but lacks some features like a fingerprint scanner or a backlit keyboard.

## Contents

-   [[1] [Hardware]](#Hardware)
-   [[2] [Installation]](#Installation)
-   [[3] [Kernel configuration]](#Kernel_configuration)
    -   [[3.1] [CPU]](#CPU)
    -   [[3.2] [PCI Express]](#PCI_Express)
    -   [[3.3] [Storage controllers]](#Storage_controllers)
    -   [[3.4] [Video]](#Video)
    -   [[3.5] [Sound]](#Sound)
    -   [[3.6] [USB]](#USB)
    -   [[3.7] [Network]](#Network)
    -   [[3.8] [Camera]](#Camera)
    -   [[3.9] [Sensors]](#Sensors)
-   [[4] [Portage make.conf]](#Portage_make.conf)

## [Hardware]

  -------------------- ------------------------------------------------------------------------------------------------------ -------- ------------------------ ------------------------------------ ---------------- ------------------------------
  Device               Make/model                                                                                             Status   Vendor ID / Product ID   Kernel driver(s)                     Kernel version   Notes
  CPU                  [AMD Ryzen 5 2500U](//www.amd.com/en/products/apu/amd-ryzen-5-2500u)   Works    N/A                      N/A                                  5.4.30
  Video                AMD Radeon Vega 8                                                                                      Works    05:00.0                  amdgpu                               5.4.30           Integrated graphics
  Audio                AMD Raven/Raven2/Fenghuang HDMI/DP Audio Controller                                                    Works    05:00.1                  snd_hda_intel                        5.4.40
  Audio                AMD Family 17h (Models 10h-1fh) HD Audio Controller                                                    Works    05:00.1                  snd_hda_intel                        5.4.40
  NVME controller      Samsung SM961/PM961                                                                                    Works    01:00.0                  nvme                                 5.4.30
  SATA controller      AMD FCH SATA Controller                                                                                Works    06:00.0                  ahci                                 5.4.30
  SD/MMC Card Reader   O2 Micro                                                                                               Works    03:00.0                  sdhci_pci                            5.4.30
  USB                  AMD Raven USB 3.1                                                                                      Works    05:00.3/4                xhci_hcd                             5.4.30
  Ethernet             Realtek RTL8111GUS                                                                                     Works    02:00.0                  r8169                                5.4.30           Gigabit LAN 10/100/1000 Mb/s
  Wireless LAN         Qualcomm Atheros QCA9377                                                                               Works    04.00.0                  ath10k_pci                           5.4.30           802.11ac
  SMBus                AMD FCH SMBus Controller (rev 61)                                                                      Works    00:14.0                  piix4_smbus, i2c_piix4, sp5100_tco   5.4.30
  Camera               Chicony, ID 04f2:b604                                                                                  Works    USB Bus 003 Device 003   uvcvideo                             5.4.30           720p
  Bluetooth            Qualcomm Atheros Bluetooth Device ID 0cf3:e500                                                         Works    USB Bus 003 Device 002   btusb                                5.4.30
  -------------------- ------------------------------------------------------------------------------------------------------ -------- ------------------------ ------------------------------------ ---------------- ------------------------------

## [Installation]

The installation is per the [Gentoo AMD64 handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64 "Handbook:AMD64").

Some specific configuration options are:

-   If [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]] is emerged with the \"experimental\" USE flag, then it is possible to set the processor family to \"AMD Zen\"
-   Enable the kernel modules for encryption using SSE3 and AES instructions, see [Iwd](https://wiki.gentoo.org/wiki/Iwd "Iwd") for an example of the options to enable
-   [AMDGPU graphics](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU"), configuring the drivers for the Vega family
-   [USB](https://wiki.gentoo.org/wiki/USB/Guide "USB/Guide") support, configuring xHCI, EHCI
-   Audio according to [ALSA](https://wiki.gentoo.org/wiki/ALSA "ALSA") and optionally [PulseAudio](https://wiki.gentoo.org/wiki/PulseAudio "PulseAudio"). Make sure to enable build Realtek HD-audio codec support.

## [Kernel configuration]

### [CPU]

-   Microarchitecture: Zen
-   Processor core: Raven Ridge

Enable AMD specific kernel options, load the required microcode, and enable the crypto instructions.

\

[KERNEL] **CPU**

    [*] 64-bit kernel
        Processor type and features  --->
            -*- Intel SoC IOSF Sideband support for SoC platforms
                Processor family (AMD Zen)  --->
            (8) Maximum number of CPUs
            [*] Multi-core scheduler support
            [*] Machine Check / overheating reporting
            [*]   AMD MCE features
            [*] CPU microcode loading support
            [*]   AMD microcode loading support
            <*> /dev/cpu/*/msr - Model-specific register support
            <*> /dev/cpu/*/cpuid - CPU information support
            [*] AMD Secure Memory Encryption (SME) support
        Power management and ACPI options  --->
            CPU Frequency scaling  --->
                Default CPUFreq governor (performance)  --->
                -*-   'performance' governor
                <M>   Processor Clocking Control interface driver
                <*>   ACPI Processor P-States driver
                <*>   AMD Opteron/Athlon64 PowerNow
                <*>   AMD frequency sensitivity feedback powersave bias
        Device Drivers  --->
            Generic Driver Options  --->
                Firmware loader  --->
                    -*- Firmware loading facility
                    (amd-ucode/microcode_amd_fam17h.bin amd/amd_sev_fam17h_model0xh.sbin) Build named firmware blobs into the kernel binary
                    (/lib/firmware) Firmware blobs root directory
    -*- Cryptographic API  --->
        <M> Parallel crypto engine
        <*> CRC32c INTEL hardware acceleration
        <M> SHA1 digest algorithm (SSSE3/AVX/AVX2/SHA-NI)
        <M> SHA256 digest algorithm (SSSE3/AVX/AVX2/SHA-NI)
        <M> SHA512 digest algorithm (SSSE3/AVX/AVX)
        <*> AES cipher algorithms (AES-NI)
        <M> Triple DES EDE cipher algorithm (x86-64)

### [PCI Express]

[KERNEL] **PCI Express**

    Device Drivers --->
        [*] PCI support  --->
            [*] PCI Express Port Bus support
            [*]   PCI Express Advanced Error Reporting support
    Bus options (PCI etc.)  --->
        [*] Support mmconfig PCI config space access
        [*] Mark VGA/VBE/EFI FB as generic system framebuffer

\

### [Storage controllers]

Configure SATA and NMVe drivers as built-in. The memory card driver can be built in as module.

\

[KERNEL] **Storage controllers**

    Device Drivers --->
            NVME Support  --->
            <*> NVM Express block device
        <*> Serial ATA and Parallel ATA drivers (libata)  --->
            [*] ATA ACPI Support
            <*> AHCI SATA support
        <M> MMC/SD/SDIO card support  --->
            <M> MMC block device driver
            <M> Secure Digital Host Controller Interface support
            <M>   SDHCI support on PCI bus
            -M- Command Queue Host Controller Interface support

### [Video]

[KERNEL] **Video**

    Device Drivers --->
        Graphics support  --->
        <M> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support)  --->
        <M> AMD GPU
        [*] HSA kernel driver for AMD GPU device
        <M> Virtual GEM provider
        <M> DisplayLink

Note that the AMD GPU also needs firmware, which will be loaded automatically if the driver is built as a module.

`root `[`#`]`dmesg | grep firmware | grep drm`

    [    4.046891] [drm] Found VCN firmware Version ENC: 1.9 DEC: 1 VEP: 0 Revision: 28
    [    4.046906] [drm] PSP loading VCN firmware

### [Sound]

[KERNEL] **Sound**

    Device Drivers --->
        <*> Sound card support  --->
            <M> Advanced Linux Sound Architecture --->
                <M> HR-timer backend support
                <*> PCI sound devices --->
                    <M> Intel/SiS/nVidia/AMD/ALi AC97 Controller
                    <M> Intel/SiS/nVidia/AMD MC97 Modem
                 HD-Audio  --->
                    <M> Build Realtek HD-audio codec support
                    <M> Build HDMI/DisplayPort HD-audio codec support

\

### [USB]

[KERNEL] **USB**

    Device Drivers --->
        [*] USB support --->
            <*> Support for Host-side USB
            <M> xHCI HCD (USB 3.0) support
            <M> EHCI HCD (USB 2.0) support

\

### [Network]

Configure support for both ethernet and wifi

\

[KERNEL] **Network**

    Device Drivers --->
        [*] Network device support --->
            [*] Ethernet driver support  --->
            [*] Realtek devices
                <M> Realtek 8169/8168/8101/8125 ethernet support
         PHY Device support and infrastructure  --->
            -M- Realtek PHYs
        [*] Wireless LAN  --->
            [*] Atheros/Qualcomm devices
            <M>   Atheros 802.11ac wireless cards support
            <M>   Atheros ath10k PCI support

### [Camera]

[KERNEL] **Camera**

    Device Drivers --->
    <M> Multimedia support  --->
        [*] Media Controller API
        [*] V4L2 sub-device userspace API
        [*] Media USB Adapters  --->
            <M> USB Video Class (UVC)
            [*]   UVC input events device support
            <M> GSPCA based webcams  --->
            [*] V4L platform devices  --->
            [*] Autoselect ancillary drivers (tuners, sensors, i2c, spi, frontends)
    [*] USB support  --->
        <M> USB Gadget Support  --->
            <M> USB Gadget functions configurable through configfs
            <M> USB Webcam Gadget

\

### [Sensors]

Sensors are provided through:

-   CPU
-   GPU
-   Thinkpad

\

[KERNEL] **Sensors**

    Device Drivers --->
        <*> Hardware Monitoring support  --->
            <M> AMD Family 10h+ temperature sensor
        [*] X86 Platform Specific Device Drivers  --->
            <M> ThinkPad ACPI Laptop Extras

## [Portage make.conf]

Many options of Gentoo are set in [/etc/portage/make.conf]. Some of the key aspects are:

[FILE] **`/etc/portage/make.conf`**

    CFLAGS="-march=znver1 -O2 -pipe
    CXXFLAGS="$"

[FILE] **`/etc/portage/package.use/00cpu-flags`**

    */* CPU_FLAGS_X86: aes avx avx2 f16c fma3 mmx mmxext pclmul popcnt sha sse sse2 sse3 sse4_1 sse4_2 sse4a ssse3

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* amdgpu radeonsi