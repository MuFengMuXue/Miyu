**Resources**

[[]][Official Support Page](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-x-series-laptops/thinkpad-x1-carbon-type-34xx)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/withdrawnbook/ThinkPad_X1_Carbon_1st_Gen.pdf)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/pccbbs/mobiles_pdf/x1_carbon_hmm_en_0b48811_05.pdf)

[[]][User Guide](https://download.lenovo.com/ibmdl/pub/pc/pccbbs/mobiles_pdf/x1carbon_ug_en.pdf)

[[]][BIOS Setup](https://download.lenovo.com/pccbbs/mobiles_pdf/lenovo_bios_setup_linux_wmi_sysfs_1.2.pdf)

[[]][ThinkPad X1 series](https://en.wikipedia.org/wiki/ThinkPad_X1_series "wikipedia:ThinkPad X1 series")

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [Accessories]](#Accessories)
    -   [[1.3] [ACPI / Power Management]](#ACPI_.2F_Power_Management)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Firmware]](#Firmware)
        -   [[2.1.1] [Intel Wireless 6205]](#Intel_Wireless_6205)
    -   [[2.2] [Emerge]](#Emerge)
        -   [[2.2.1] [Battery thresholds]](#Battery_thresholds)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Portage]](#Portage)
-   [[4] [External resources]](#External_resources)

## [Hardware]

### [Standard]

  ---------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------- ------------- ------------- ----------------------------------------------------------- ---------------- ----------------------------------------------------------------------------------------------------------------------
  Device                                                                                                                             Make/model                                                                                                                                     Status        Bus ID        Kernel driver(s)                                            Kernel version   Notes
  CPU                                                                                                                                [Core i5-3317U](https://ark.intel.com/products/65707/Intel-Core-i5-3317U-Processor-3M-Cache-up-to-2_60-GHz)    Not tested    N/A           N/A                                                                          [Haswell](https://en.wikipedia.org/wiki/Haswell_(microarchitecture) "wikipedia:Haswell (microarchitecture)")
                                                                                                                                     [Core i5-3337U](https://ark.intel.com/products/72055/Intel-Core-i5-3337U-Processor-3M-Cache-up-to-2_70-GHzU)   Not tested    N/A           N/A                                                                          [Haswell](https://en.wikipedia.org/wiki/Haswell_(microarchitecture) "wikipedia:Haswell (microarchitecture)")
                                                                                                                                     [Core i5-3427U](https://ark.intel.com/products/64903/Intel-Core-i5-3427U-Processor-3M-Cache-up-to-2_80-GHz)    Works         N/A           N/A                                                         4.14             [Haswell](https://en.wikipedia.org/wiki/Haswell_(microarchitecture) "wikipedia:Haswell (microarchitecture)")
                                                                                                                                     [Core i7-3667U](https://ark.intel.com/products/64898/Intel-Core-i7-3667U-Processor-4M-Cache-up-to-3_20-GHz)    Not tested    N/A           N/A                                                                          [Haswell](https://en.wikipedia.org/wiki/Haswell_(microarchitecture) "wikipedia:Haswell (microarchitecture)")
  Integrated Graphics                                                                                                                [HD Graphics 4000](https://wiki.gentoo.org/wiki/Intel "Intel")                                                                                 Works         0000:0002     i915                                                        4.14             VIDEO_CARDS i965
  Audio                                                                                                                                                                                                                                                                             Works         0000:001b     snd_hda_intel                                               4.14
  USB 3.0                                                                                                                                                                                                                                                                           Works         0000:0014     xhci_hcd                                                    4.14
  [Management Engine Interface](https://www.kernel.org/doc/Documentation/misc-devices/mei/mei.txt)                                                                                                                                                  Not tested    0000:0016     mei_me                                                      4.14
  PCI                                                                                                                                                                                                                                                                               Works         0000:001c     pcieport                                                    4.14
  USB 2.0                                                                                                                                                                                                                                                                           Works         0000:001d     ehci-pci                                                    4.14
  ISA                                                                                                                                                                                                                                                                               Works         0000:001f     lpc_ich                                                     4.14
  SATA                                                                                                                                                                                                                                                                              Works         0000:001f.2   ahci                                                        4.14
  SMBus                                                                                                                                                                                                                                                                             Works         0000:001f.3   i801_smbus                                                  4.14
  WiFi                                                                                                                               Intel 6205                                                                                                                                     Works         0003:0000     [iwlwifi](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi")   4.14             MVM firmware
  Bluetooth                                                                                                                          Intel 6205                                                                                                                                     Works         0003:0000                                                                 4.14             Bluetooth 4.0
  TPM                                                                                                                                STM                                                                                                                                            Not tested    N/A           tpm_tis                                                     4.14             TPM 1.2
  ---------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------- ------------- ------------- ----------------------------------------------------------- ---------------- ----------------------------------------------------------------------------------------------------------------------

### [Accessories]

  --------------------- ------------ ------------- ----------- ------------------ ---------------- --------------------- --
  Device                Make/model   Status        Bus ID      Kernel driver(s)   Kernel version   Notes
  Fingerprint Scanner                Works         N/A         N/A                                 Supported by fprint
  Multi-touch screen                 Not tested    N/A         N/A
  Memory card reader                 Works         0002:0000   rtsx_pci           4.14             SD, MMC, SDHC, SDXC
  Webcam                             Works         N/A         uvcvideo           4.14             720p; usb 5986:0266
  --------------------- ------------ ------------- ----------- ------------------ ---------------- --------------------- --

### [][ACPI / Power Management]

  ------------------------------ ------------- ------------------------
             Function                Works              Notes
      CPU frequency scaling           Yes       Driven by intel_pstate
      GPU Powersaving (RC6)       Not tested
   SATA Power Management (ALPM)       Yes
          Suspend to RAM              Yes
   Suspend to disk (hibernate)    Not tested
        Backlight control             Yes       Driven by acpi_video.
    Keyboard backlight control        Yes
  ------------------------------ ------------- ------------------------

## [Installation]

### [Firmware]

#### [Intel Wireless 6205]

See [Detailed article](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi").

### [Emerge]

-   [Special buttons](https://wiki.gentoo.org/wiki/ACPI/ThinkPad-special-buttons "ACPI/ThinkPad-special-buttons")

#### [Battery thresholds]

`root `[`#`]`emerge --ask app-laptop/tpacpi-bat`

## [Configuration]

### [Portage]

[FILE] **`/etc/portage/make.conf`**

    CFLAGS="-O2 -pipe -march=native"
    CPU_FLAGS_X86="aes avx mmx popcnt sse sse2 sse4_1 sse4_2 ssse3"
    MAKEOPTS="-j5 -l5"
    INPUT_DEVICES="evdev synaptics"
    VIDEO_CARDS="intel i965"

## [External resources]

-   [http://www.thinkwiki.org/wiki/Category:X1_Carbon](http://www.thinkwiki.org/wiki/Category:X1_Carbon)