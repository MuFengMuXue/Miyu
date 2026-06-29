[] The information in this article is probably **outdated**. You can help the Gentoo community by verifying and [updating this article](https://wiki.gentoo.org/index.php?title=Lenovo_ThinkPad_T420s&action=edit).

**Resources**

[[]][Home](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-t-series-laptops/thinkpad-t420s)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/ibmdl/pub/pc/pccbbs/mobiles_pdf/t420s_t420si_hmm_en_0a60241_07.pdf)

[[]][User Guide](https://download.lenovo.com/ibmdl/pub/pc/pccbbs/mobiles_pdf/t420s_t420si_ug_en.pdf)

[[]][ThinkPad T series](https://en.wikipedia.org/wiki/ThinkPad_T_series "wikipedia:ThinkPad T series")

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Kernel]](#Kernel)
    -   [[2.2] [Emerge]](#Emerge)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Fan control]](#Fan_control)

## [Hardware]

### [Standard]

  ------------- --------------------------------------------------------------------------------------- -------- ------------------------ ------------------ ---------------- -------
  Device        Make/model                                                                              Status   Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  CPU           N/A                                                                                     Works    N/A                      N/A                N/A
  GPU           Intel Corporation 2nd Generation Core Processor Family Integrated Graphics Controller   Works    N/A                      i915               N/A
  Ethernet      Intel Corporation 82579LM Gigabit Network Connection                                    Works    N/A                      N/A                N/A
  Wi-Fi         Intel Corporation Centrino Ultimate-N 6300                                              Works    N/A                      iwlwifi            N/A
  Card Reader   Ricoh Co Ltd MMC/SD Host Controller                                                     Works    N/A                      N/A                N/A
  ------------- --------------------------------------------------------------------------------------- -------- ------------------------ ------------------ ---------------- -------

`root `[`#`]`lspci (partial output, recovered from the history)`

    00:00.0 Host bridge: Intel Corporation 2nd Generation Core Processor Family DRAM Controller (rev 09)
    00:02.0 VGA compatible controller: Intel Corporation 2nd Generation Core Processor Family Integrated Graphics Controller (rev 09)
    00:16.0 Communication controller: Intel Corporation 6 Series/C200 Series Chipset Family MEI Controller #1 (rev 04)
    00:16.3 Serial controller: Intel Corporation 6 Series/C200 Series Chipset Family KT Controller (rev 04)
    00:19.0 Ethernet controller: Intel Corporation 82579LM Gigabit Network Connection (rev 04)
    00:1a.0 USB controller: Intel Corporation 6 Series/C200 Series Chipset Family USB Enhanced Host Controller #2 (rev 04)
    00:1b.0 Audio device: Intel Corporation 6 Series/C200 Series Chipset Family High Definition Audio Controller (rev 04)
    00:1c.0 PCI bridge: Intel Corporation 6 Series/C200 Series Chipset Family PCI Express Root Port 1 (rev b4)
    00:1c.1 PCI bridge: Intel Corporation 6 Series/C200 Series Chipset Family PCI Express Root Port 2 (rev b4)
    00:1c.3 PCI bridge: Intel Corporation 6 Series/C200 Series Chipset Family PCI Express Root Port 4 (rev b4)
    00:1c.4 PCI bridge: Intel Corporation 6 Series/C200 Series Chipset Family PCI Express Root Port 5 (rev b4)
    00:1d.0 USB controller: Intel Corporation 6 Series/C200 Series Chipset Family USB Enhanced Host Controller #1 (rev 04)
    00:1f.0 ISA bridge: Intel Corporation QM67 Express Chipset Family LPC Controller (rev 04)
    00:1f.2 SATA controller: Intel Corporation 6 Series/C200 Series Chipset Family 6 port SATA AHCI Controller (rev 04)
    00:1f.3 SMBus: Intel Corporation 6 Series/C200 Series Chipset Family SMBus Controller (rev 04)
    03:00.0 Network controller: Intel Corporation Centrino Ultimate-N 6300 (rev 3e)
    05:00.0 System peripheral: Ricoh Co Ltd MMC/SD Host Controller (rev 07)
    0d:00.0 USB controller: NEC Corporation uPD720200 USB 3.0 Host Controller (rev 04)

## [Installation]

### [Kernel]

[FILE] **`.config`**

    CONFIG_DRM_I915
    CONFIG_DRM_I915_KMS
    CONFIG_SERIAL_CORE
    CONFIG_E1000E
    CONFIG_USB_EHCI_PCI
    CONFIG_SND_HDA_INTEL
    CONFIG_USB_EHCI_PCI
    CONFIG_SATA_AHCI
    CONFIG_I2C_I801
    CONFIG_IWLWIFI
    CONFIG_MMC_SDHCI
    CONFIG_MMC_SDHCI_PCI

### [Emerge]

[FILE] **`/etc/portage/package.use/00input`**

    */* INPUT_DEVICES: evdev synaptics

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* intel i965

[FILE] **`/etc/portage/package.use/00cpu-flags`**

    */*  CPU_FLAGS_X86: aes avx mmx mmxext popcnt sse sse2 sse3 sse4_1 sse4_2 ssse3

## [Configuration]

### [Fan control]

Fan control needs to be explicitly allowed:

[FILE] **`/etc/modprobe.d/thinkpad_acpi.conf`**

    options thinkpad_acpi fan_control=1

Turn off:

`root `[`#`]`echo level 0 > /proc/acpi/ibm/fan`

Maximum measured speed:

`root `[`#`]`echo level 7 > /proc/acpi/ibm/fan`

Automatic speed (default):

`root `[`#`]`echo level auto > /proc/acpi/ibm/fan`

Maximum speed:

`root `[`#`]`echo level disengaged > /proc/acpi/ibm/fan`