## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Laptop Specifications]](#Laptop_Specifications)
        -   [[1.1.1] [Hardware]](#Hardware_2)
-   [[2] [Configuration details]](#Configuration_details)
    -   [[2.1] [CPU]](#CPU)
    -   [[2.2] [Graphics]](#Graphics)
    -   [[2.3] [Touchpad]](#Touchpad)
    -   [[2.4] [Camera]](#Camera)
    -   [[2.5] [Bluetooth]](#Bluetooth)
    -   [[2.6] [package.use]](#package.use)
-   [[3] [External resources]](#External_resources)

## [Hardware]

### [Laptop Specifications]

  ---------------- -------------------------------------------------------------------------------------------------------------- ------------- ------------------------------------------------------------------------------------------------------------------------------------------------
       Device                                                          Model                                                          Works                                                                          Notes
     Processor                                    6th Generation Intel® Core™ i7 6820HK (Skylake)                                      Yes
    Discrete GPU                                                NVIDIA GTX 980M 8GB                                                    Yes                                              DisplayPort+HDMI+built-in display in triple-monitor setup tested
   Integrated GPU                                              Intel® HD Graphics 530                                              Not tested
   Switching GPUs                                                                                                                  Not tested
        LCD                                                        17\" IPS 1080p                                                      Yes
        WiFi        [Qualcomm Atheros QCA6174](https://wiki.gentoo.org/wiki/Qualcomm_Atheros_QCA6174 "Qualcomm Atheros QCA6174")       Yes                                                           ath10k kernel driver + linux-firmware
     Bluetooth                                                                                                                         Yes                                                                  Tested as far as pairing
       Camera                                                     BisonCam, NB Pro                                                     Yes                                           Be sure to enable with Fn+F6 (or Win+F6 if Swap keys enabled in BIOS)
    Card Reader                                                Realtek RTS5249 PCI-E                                                   Yes
      Touchpad                                                     Synaptics PS/2                                                      Yes
    Audio Device                                                   Realtek ALC898                                                      Yes
    RGB Lighting                                                    MSI EPF USB                                                    Not tested    [https://linux-hardware.org/index.php?id=usb:1770-ff00](https://linux-hardware.org/index.php?id=usb:1770-ff00)
      Ethernet                                             Qualcomm Atheros Killer E2400                                               Yes
   Optical Drive                                                                                                                       Yes
   Thunderbolt 3                                          Intel DSL6340 Thunderbolt 3 NHI                                          Not tested
  ---------------- -------------------------------------------------------------------------------------------------------------- ------------- ------------------------------------------------------------------------------------------------------------------------------------------------

#### [Hardware]

`root `[`#`]`lspci -k`

    00:00.0 Host bridge: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Host Bridge/DRAM Registers (rev 07)
        Subsystem: Micro-Star International Co., Ltd. [MSI] Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Host Bridge/DRAM Registers
    00:01.0 PCI bridge: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor PCIe Controller (x16) (rev 07)
        Kernel driver in use: pcieport
    00:08.0 System peripheral: Intel Corporation Xeon E3-1200 v5/v6 / E3-1500 v5 / 6th/7th Gen Core Processor Gaussian Mixture Model
        Subsystem: Micro-Star International Co., Ltd. [MSI] Xeon E3-1200 v5/v6 / E3-1500 v5 / 6th/7th Gen Core Processor Gaussian Mixture Model
    00:14.0 USB controller: Intel Corporation Sunrise Point-H USB 3.0 xHCI Controller (rev 31)
        Subsystem: Micro-Star International Co., Ltd. [MSI] Sunrise Point-H USB 3.0 xHCI Controller
        Kernel driver in use: xhci_hcd
    00:14.2 Signal processing controller: Intel Corporation Sunrise Point-H Thermal subsystem (rev 31)
        Subsystem: Micro-Star International Co., Ltd. [MSI] Sunrise Point-H Thermal subsystem
    00:16.0 Communication controller: Intel Corporation Sunrise Point-H CSME HECI #1 (rev 31)
        Subsystem: Micro-Star International Co., Ltd. [MSI] Sunrise Point-H CSME HECI
        Kernel driver in use: mei_me
    00:17.0 SATA controller: Intel Corporation Sunrise Point-H SATA controller [AHCI mode] (rev 31)
        Subsystem: Micro-Star International Co., Ltd. [MSI] Sunrise Point-H SATA controller [AHCI mode]
        Kernel driver in use: ahci
    00:1b.0 PCI bridge: Intel Corporation Sunrise Point-H PCI Root Port #17 (rev f1)
        Kernel driver in use: pcieport
    00:1c.0 PCI bridge: Intel Corporation Sunrise Point-H PCI Express Root Port #1 (rev f1)
        Kernel driver in use: pcieport
    00:1c.2 PCI bridge: Intel Corporation Sunrise Point-H PCI Express Root Port #3 (rev f1)
        Kernel driver in use: pcieport
    00:1c.3 PCI bridge: Intel Corporation Sunrise Point-H PCI Express Root Port #4 (rev f1)
        Kernel driver in use: pcieport
    00:1c.4 PCI bridge: Intel Corporation Sunrise Point-H PCI Express Root Port #5 (rev f1)
        Kernel driver in use: pcieport
    00:1d.0 PCI bridge: Intel Corporation Sunrise Point-H PCI Express Root Port #9 (rev f1)
        Kernel driver in use: pcieport
    00:1f.0 ISA bridge: Intel Corporation Sunrise Point-H LPC Controller (rev 31)
        Subsystem: Micro-Star International Co., Ltd. [MSI] Sunrise Point-H LPC Controller
    00:1f.2 Memory controller: Intel Corporation Sunrise Point-H PMC (rev 31)
        Subsystem: Micro-Star International Co., Ltd. [MSI] Sunrise Point-H PMC
    00:1f.3 Audio device: Intel Corporation Sunrise Point-H HD Audio (rev 31)
        Subsystem: Micro-Star International Co., Ltd. [MSI] Sunrise Point-H HD Audio
        Kernel driver in use: snd_hda_intel
    00:1f.4 SMBus: Intel Corporation Sunrise Point-H SMBus (rev 31)
        Subsystem: Micro-Star International Co., Ltd. [MSI] Sunrise Point-H SMBus
        Kernel driver in use: i801_smbus
    01:00.0 VGA compatible controller: NVIDIA Corporation GM204M [GeForce GTX 980M] (rev a1)
        Subsystem: Micro-Star International Co., Ltd. [MSI] GM204M [GeForce GTX 980M]
        Kernel driver in use: nvidia
        Kernel modules: nvidia_drm, nvidia
    01:00.1 Audio device: NVIDIA Corporation GM204 High Definition Audio Controller (rev a1)
        Subsystem: Micro-Star International Co., Ltd. [MSI] GM204 High Definition Audio Controller
        Kernel driver in use: snd_hda_intel
    02:00.0 Non-Volatile memory controller: Toshiba America Info Systems NVMe Controller (rev 01)
        Subsystem: Toshiba America Info Systems NVMe Controller
        Kernel driver in use: nvme
    03:00.0 Network controller: Qualcomm Atheros QCA6174 802.11ac Wireless Network Adapter (rev 32)
        Subsystem: Bigfoot Networks, Inc. QCA6174 802.11ac Wireless Network Adapter
        Kernel driver in use: ath10k_pci
        Kernel modules: ath10k_pci
    04:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS5249 PCI Express Card Reader (rev 01)
        Subsystem: Micro-Star International Co., Ltd. [MSI] RTS5249 PCI Express Card Reader
        Kernel driver in use: rtsx_pci
    05:00.0 Ethernet controller: Qualcomm Atheros Killer E2400 Gigabit Ethernet Controller (rev 10)
        Subsystem: Micro-Star International Co., Ltd. [MSI] Killer E2400 Gigabit Ethernet Controller
        Kernel driver in use: alx
    06:00.0 PCI bridge: Intel Corporation DSL6340 Thunderbolt 3 Bridge [Alpine Ridge 2C 2015]
        Kernel driver in use: pcieport
    07:00.0 PCI bridge: Intel Corporation DSL6340 Thunderbolt 3 Bridge [Alpine Ridge 2C 2015]
        Kernel driver in use: pcieport
    07:01.0 PCI bridge: Intel Corporation DSL6340 Thunderbolt 3 Bridge [Alpine Ridge 2C 2015]
        Kernel driver in use: pcieport
    07:02.0 PCI bridge: Intel Corporation DSL6340 Thunderbolt 3 Bridge [Alpine Ridge 2C 2015]
        Kernel driver in use: pcieport
    08:00.0 System peripheral: Intel Corporation DSL6340 Thunderbolt 3 NHI [Alpine Ridge 2C 2015]
        Subsystem: Device 2222:1111
        Kernel driver in use: thunderbolt
    3d:00.0 USB controller: Intel Corporation DSL6340 USB 3.1 Controller [Alpine Ridge]
        Subsystem: Device 2222:1111
        Kernel driver in use: xhci_hcd
    3f:00.0 Non-Volatile memory controller: Toshiba America Info Systems NVMe Controller (rev 01)
        Subsystem: Toshiba America Info Systems NVMe Controller
        Kernel driver in use: nvme

## [Configuration details]

### [CPU]

[This bug](https://lwn.net/Articles/726496/) applies to the CPU contained in this laptop. You should review [this forum post](https://forums.gentoo.org/viewtopic-t-1065464-highlight-.html) and if the solution is still relevant, apply it ASAP.

### [Graphics]

See [NVIDIA/nvidia-drivers](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers "NVIDIA/nvidia-drivers") or [nouveau](https://wiki.gentoo.org/wiki/Nouveau "Nouveau"). Also, [Xorg/Hardware_3D_acceleration_guide](https://wiki.gentoo.org/wiki/Xorg/Hardware_3D_acceleration_guide "Xorg/Hardware 3D acceleration guide").

### [Touchpad]

See [Synaptics](https://wiki.gentoo.org/wiki/Synaptics "Synaptics").

### [Camera]

The camera can be disabled via a special fn-key combo (Fn+F6). In BIOS, there is an option to swap Fn with Windows key. Keep this in mind when trying to get the camera working. You know the camera is enabled, as follows:

`root `[`#`]`lsusb -d 5986:055c`

    Bus 001 Device 012: ID 5986:055c Acer, Inc

Blank/no output means it is disabled.

### [Bluetooth]

See [bluetooth](https://wiki.gentoo.org/wiki/Bluetooth "Bluetooth")

### [package.use]

It is recommended to add or edit options in [/etc/portage/package.use] as such:

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* nvidia

[FILE] **`/etc/portage/package.use/00input`**

    */* INPUT_DEVICES: evdev synaptic

[FILE] **`/etc/portage/package.use/00cpu-flags`**

    */* CPU_FLAGS_X86: aes avx avx2 f16c fma3 mmx mmxext popcnt sse sse2 sse3 sse4_1 sse4_2 ssse3

## [External resources]

-   [Forum post](https://forums.gentoo.org/viewtopic-t-1068092.html) - get some unofficial user-to-user support + additional notes.
-   [User contributed kernel configs](https://bitbucket.org/experimentfailed/gentoo-kernel-configs) - Kernel config by ExperimentFailed aka statikregimen.