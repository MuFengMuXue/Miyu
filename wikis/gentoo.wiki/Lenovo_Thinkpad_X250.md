**Resources**

[[]][Official Support Page](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-x-series-laptops/thinkpad-x250)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_X250/ThinkPad_X250_Spec.PDF)

[[]][Specifications (by region)](https://psref.lenovo.com/Product/ThinkPad/ThinkPad_X250)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/pccbbs/mobiles_pdf/x250_hmm_en_sp40f30022_01.pdf)

[[]][User Guide](https://download.lenovo.com/pccbbs/mobiles_pdf/x250_ug_en.pdf)

[[]][BIOS Setup](https://download.lenovo.com/pccbbs/mobiles_pdf/lenovo_bios_setup_linux_wmi_sysfs_1.2.pdf)

[[]][ThinkPad X Series](https://en.wikipedia.org/wiki/ThinkPad_X_Series#X250 "wikipedia:ThinkPad X Series")

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [Accessories]](#Accessories)
    -   [[1.3] [ACPI / Power Management]](#ACPI_.2F_Power_Management)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Firmware]](#Firmware)
        -   [[2.1.1] [Intel Wireless 7265]](#Intel_Wireless_7265)
    -   [[2.2] [Emerge]](#Emerge)
        -   [[2.2.1] [Battery thresholds]](#Battery_thresholds)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Portage]](#Portage)
    -   [[3.2] [X.org]](#X.org)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Suspend/resume]](#Suspend.2Fresume)
    -   [[4.2] [Total Freeze Using Graphical Acceleration]](#Total_Freeze_Using_Graphical_Acceleration)
-   [[5] [External resources]](#External_resources)

## [Hardware]

### [Standard]

  ---------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------- ------------- ------------- ----------------------------------------------------------- ---------------- ----------------------------------------------------------------------------------------------------------------------------
  Device                                                                                                                             Make/model                                                                                                                                   Status        Bus ID        Kernel driver(s)                                            Kernel version   Notes
  CPU                                                                                                                                [Core i3-5010U](http://ark.intel.com/products/84697/Intel-Core-i3-5010U-Processor-3M-Cache-2_10-GHz)         Works         N/A           N/A                                                         4.3              [Broadwell](https://en.wikipedia.org/wiki/Broadwell_(microarchitecture) "wikipedia:Broadwell (microarchitecture)")
                                                                                                                                     [Core i5-5200U](http://ark.intel.com/products/85212/Intel-Core-i5-5200U-Processor-3M-Cache-up-to-2_70-GHz)   Not tested    N/A           N/A                                                                          [Broadwell](https://en.wikipedia.org/wiki/Broadwell_(microarchitecture) "wikipedia:Broadwell (microarchitecture)")
                                                                                                                                     [Core i5-5300U](http://ark.intel.com/products/85213/Intel-Core-i5-5300U-Processor-3M-Cache-up-to-2_90-GHz)   Works         N/A           N/A                                                                          [Broadwell](https://en.wikipedia.org/wiki/Broadwell_(microarchitecture) "wikipedia:Broadwell (microarchitecture)")
                                                                                                                                     [Core i7-5600U](http://ark.intel.com/products/85215/Intel-Core-i7-5600U-Processor-4M-Cache-up-to-3_20-GHz)   Works         N/A           N/A                                                         5.4              [Broadwell](https://en.wikipedia.org/wiki/Broadwell_(microarchitecture) "wikipedia:Broadwell (microarchitecture)")
  Integrated Graphics                                                                                                                [HD Graphics 5500](https://wiki.gentoo.org/wiki/Intel "Intel")                                                                               Works         0000:0002     i915                                                        4.3              VIDEO_CARDS i965
  Audio                                                                                                                                                                                                                                                                           Works         0000:0003     snd_hda_intel                                               4.3
  USB 3.0                                                                                                                                                                                                                                                                         Works         0000:0014     xhci_hcd                                                    4.3
  [Management Engine Interface](https://www.kernel.org/doc/Documentation/misc-devices/mei/mei.txt)                                                                                                                                                Not tested    0000:0016     mei_me                                                      4.3
  Ethernet                                                                                                                                                                                                                                                                        Works         0000:0019     e1000e                                                      4.3
  PCI                                                                                                                                                                                                                                                                             Works         0000:001c     pcieport                                                    4.3
  USB 2.0                                                                                                                                                                                                                                                                         Works         0000:001d     ehci-pci                                                    4.3
  ISA                                                                                                                                                                                                                                                                             Works         0000:001f     lpc_ich                                                     4.3
  SATA                                                                                                                                                                                                                                                                            Works         0000:001f.2   ahci                                                        4.3
  SMBus                                                                                                                                                                                                                                                                           Works         0000:001f.3   i801_smbus                                                  4.3
  WiFi                                                                                                                               Intel 7265                                                                                                                                   Works         0003:0000     [iwlwifi](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi")   4.3              MVM firmware
  Bluetooth                                                                                                                          Intel 7265                                                                                                                                   Works         0003:0000                                                                 4.3              Bluetooth 4.0
  TPM                                                                                                                                STM                                                                                                                                          Works         N/A           tpm_tis                                                     4.3              TPM 1.2
  ---------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------- ------------- ------------- ----------------------------------------------------------- ---------------- ----------------------------------------------------------------------------------------------------------------------------

### [Accessories]

  ------------------------------------------------------------------------- --------------------- ------------- ----------- ------------------ ---------------- --------------------------------------------------------------------------------------------------
  Device                                                                    Make/model            Status        Bus ID      Kernel driver(s)   Kernel version   Notes
  Fingerprint Scanner                                                                             Works         N/A         N/A                                 Supported by fprint
  Multi-touch screen                                                                              Not tested    N/A         N/A
  Memory card reader                                                                              Works         0002:0000   rtsx_pci           4.3              SD, MMC, SDHC, SDXC
  [Smart card reader](https://wiki.gentoo.org/wiki/PCSC-Lite "PCSC-Lite")   Alcor Micro AU9540    Works         N/A         ehci-pci           4.3
  Webcam                                                                                          Works         N/A         uvcvideo           4.4              720p; usb 04ca:703c
  Dock                                                                      ThinkPad Ultra Dock   Not tested    N/A         N/A
  Dock                                                                      ThinkPad Pro Dock     Works         N/A         N/A                                 Tested: all ports (but not with more than one external display), (Un)Dock, Suspend-then-(un)dock
  Dock                                                                      ThinkPad Basic Dock   Not tested    N/A         N/A
  ------------------------------------------------------------------------- --------------------- ------------- ----------- ------------------ ---------------- --------------------------------------------------------------------------------------------------

### [][ACPI / Power Management]

  ------------------------------ ---------- ------------------------------------------------------------------------
             Function              Works                                     Notes
      CPU frequency scaling         Yes                              Driven by intel_pstate
      GPU Powersaving (RC6)         Yes               Support PC8+ with i915.allow_pc8=1 kernel parameter
   SATA Power Management (ALPM)     Yes
          Suspend to RAM            Yes
   Suspend to disk (hibernate)    Partial    At first seems frozen, but start to react normally after a few seconds
        Backlight control           Yes                              Driven by acpi_video.
    Keyboard backlight control      Yes
  ------------------------------ ---------- ------------------------------------------------------------------------

## [Installation]

### [Firmware]

#### [Intel Wireless 7265]

See [Detailled article](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi").

### [Emerge]

-   [Special buttons](https://wiki.gentoo.org/wiki/ACPI/ThinkPad-special-buttons "ACPI/ThinkPad-special-buttons")

#### [Battery thresholds]

`root `[`#`]`emerge --ask app-laptop/tpacpi-bat`

Modify the init file in order to change the two batteries, else only one battery will be changed:

[FILE] **`/etc/init.d/tpacpi-bat`**

    [...]
    BATS="1 2"
    [...]

See also: [https://github.com/dywisor/tlp-portage](https://github.com/dywisor/tlp-portage)

## [Configuration]

### [Portage]

[FILE] **`/etc/portage/make.conf`**

    CFLAGS="-O2 -pipe -march=native"
    CPU_FLAGS_X86="aes avx avx2 fma3 mmx mmxext popcnt sse sse2 sse3 sse4_1 sse4_2 ssse3"
    MAKEOPTS="-j5 -l5"
    INPUT_DEVICES="evdev synaptics"
    VIDEO_CARDS="intel i965"

### [X.org]

In order to have more readable screen and texts (particularly if you own a 1080p display), indicate to X.org physical size of the display:

[FILE] **`/etc/X11/xorg.conf.d/90-monitor.conf`**

    Section "Monitor"
        Identifier             "<default monitor>"
        DisplaySize             276 156    # Physical display dimensions in millimeters
    EndSection

On 1080p displays, you\'ll get a DPI resolution of 177x176 dots per inch (default is 96x96).

## [Troubleshooting]

### [][Suspend/resume]

In order to resume properly, your need to have a working TPM:

[KERNEL] **Enable TPM support**

    Device Drivers ->
      Character devices ->
        <*> TPM Hardware Support ->
          <*> TPM Interface Specification 1.2 Interface / TPM 2.0 FIFO Interface

### [Total Freeze Using Graphical Acceleration]

If you except entire system freeze when using graphical acceleration, you should disable execlists in the kernel cmdline:

    i915.enable_execlists=0

Or just disable VT-d processor feature in BIOS.

When booting directly from UEFI (eg. without Grub), set the following kernel variables:

[KERNEL] **Disabling execlists**

    Processor type and features ->
      [*] Built-in kernel command line
      (root=/dev/sdaX i915.enable_execlists=0) Built-in kernel command string

## [External resources]

-   [http://www.thinkwiki.org/wiki/Category:X250](http://www.thinkwiki.org/wiki/Category:X250)
-   [https://wiki.archlinux.org/title/Lenovo_ThinkPad_X250](https://wiki.archlinux.org/title/Lenovo_ThinkPad_X250)