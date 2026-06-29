**Resources**

[[]][Home](https://www.asrock.com/mb/Intel/J5005-ITX/index.asp)

\

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [Hardware]](#Hardware)
-   [[3] [Installation]](#Installation)
-   [[4] [Kernel configuration]](#Kernel_configuration)
    -   [[4.1] [CPU]](#CPU)
    -   [[4.2] [PCI Express]](#PCI_Express)
    -   [[4.3] [Storage controllers]](#Storage_controllers)
    -   [[4.4] [Video]](#Video)
    -   [[4.5] [Sound]](#Sound)
    -   [[4.6] [USB]](#USB)
    -   [[4.7] [Network]](#Network)
    -   [[4.8] [Intel MEI]](#Intel_MEI)
    -   [[4.9] [Sensors]](#Sensors)
    -   [[4.10] [SMBus]](#SMBus)
-   [[5] [Portage make.conf]](#Portage_make.conf)

## [Introduction]

The board is well named: it is a [mini-ITX](https://en.wikipedia.org/wiki/Mini-ITX) board, with an on-board [Intel J5005](//ark.intel.com/content/www/us/en/ark/products/128984/intel-pentium-silver-j5005-processor-4m-cache-up-to-2-80-ghz.html) CPU. The CPU has a passive cooler mounted on top. The J5005 has integrated graphics, capable of running 4k at 60 Hz over HDMI 2.0. There are two SO-DIMM memory slots allowing for dual lane memory access. The board has 4 SATA-3 6 GB/s ports to connect HDDs or SSDs. More specifications can be found at [ASRock\'s website](//www.asrock.com/mb/Intel/J5005-ITX/index.asp#Specification).

Reasons to build a rig using this board could be the combination of:

-   Low power CPU with 10 W TDP: if placed in a spacious enough case then it can be run fanless
-   A CPU with [SSSE3](https://en.wikipedia.org/wiki/SSSE3), and [AES](https://en.wikipedia.org/wiki/AES_instruction_set) instructions, perfect for fast disk encryption, vpn connections, and encrypted wireless
-   An optical [S/PDIF port](https://en.wikipedia.org/wiki/S/PDIF) allows for digital connection to an external audio amplifier
-   4 SATA-3 ports provide plenty of storage opportunity
-   Capable of 4k graphics: good for [HTPCs](https://en.wikipedia.org/wiki/Home_theater_PC)
-   Small ITX form factor

## [Hardware]

  ----------------- ----------------------- ------------- --------- ---------------------- ---------------- --------------------------------
  Device            Make/model              Status        Bus ID    Kernel driver(s)       Kernel version   Notes
  CPU               Intel J5005             Works         N/A       N/A                    5.4.18           Goldmont Plus microarchitecure
  Video             Intel HD Graphics 605   Works         00:02.0   i915                   5.4.18           Integrated graphics
  Audio             Intel Device 3198       Works         00:0e.0   snd_hda_intel          5.4.18           Realtek ALC892 Audio Codec
  SATA controller   Intel Device 31e3       Works         00:12.0   ahci                   5.4.18           2 x SATA3 6.0 Gb/s
  SATA controller   ASMedia ASM1062         Works         04:00.0   ahci                   5.4.18           2 x SATA3 6.0 Gb/s
  Ethernet          Realtek RTL 8111H       Works         03:00.0   r8169                  5.4.18           Gigabit LAN 10/100/1000 Mb/s
  SMBus             ASMedia ASM1062         Not tested    00:1f.1   i801_smbus, i2c_i801   5.4.18
  ----------------- ----------------------- ------------- --------- ---------------------- ---------------- --------------------------------

The board also sports

-   1 M.2 Key E interface, meant for a wireless card
-   1 x PCI Express 2.0 x1 Slot

\

## [Installation]

The installation is per the [Gentoo AMD64 handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64 "Handbook:AMD64").

Some specific configuration options are:

-   If [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]] is emerged with the \"experimental\" USE flag, then it is possible to set the processor family to \"Intel Goldmont Plus\"
-   Enable the kernel modules for encryption using SSE3 and AES instructions, see [Iwd](https://wiki.gentoo.org/wiki/Iwd "Iwd") for an example of the options to enable
-   [Intel graphics](https://wiki.gentoo.org/wiki/Intel "Intel"), configuring the drivers for generation 9
-   [USB](https://wiki.gentoo.org/wiki/USB/Guide "USB/Guide") support, configuring xHCI, EHCI, and UHCI
-   Audio according to [ALSA](https://wiki.gentoo.org/wiki/ALSA "ALSA") and optionally [PulseAudio](https://wiki.gentoo.org/wiki/PulseAudio "PulseAudio"). Make sure to enable build Realtek HD-audio codec support

## [Kernel configuration]

### [CPU]

Intel J5005:

-   marketing name: Intel® Pentium® Silver J5005 Processor
-   code name: Gemini Lake
-   architecture: Goldmont plus

\

[KERNEL] **CPU**

    [*] 64-bit kernel
        Processor type and features  --->
            [*] Intel Low Power Subsystem Support
            -*- Intel SoC IOSF Sideband support for SoC platforms
                Processor family (Intel Goldmont Plus)  --->
            (4) Maximum number of CPUs
            [*] Multi-core scheduler support
            [*] Machine Check / overheating reporting
            [*] CPU microcode loading support
            [*]   Intel microcode loading support
            <*> /dev/cpu/*/msr - Model-specific register support
            <*> /dev/cpu/*/cpuid - CPU information support
        Power management and ACPI options  --->
            CPU Frequency scaling  --->
                Default CPUFreq governor (performance)  --->
                -*-   'performance' governor
            [*] Intel P state control
        [*] Cpuidle Driver for Intel Processors
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

\

### [Storage controllers]

Select \"AHCI SATA support\" module.

[KERNEL] **Storage controllers**

    Device Drivers --->
        <*> Serial ATA and Parallel ATA drivers (libata)  --->
            [*] ATA ACPI Support
            <*> AHCI SATA support

\

### [Video]

The integrated video is Intel Gen 9.

[KERNEL] **Video**

    Device Drivers --->
        Graphics support  --->
        <M> /dev/agpgart (AGP Support)  --->
            <M> Intel 440LX/BX/GX, I8xx and E7x05 chipset support
        <M> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support)  --->
            [*] Enable legacy fbdev support for your modesetting driver
        <M> Intel 8xx/9xx/G3x/G4x/HD Graphics
            [*] Always enable userptr support

The required firmware is loaded automatically when the i915 driver is built as a module.

Provide configuration options for the i915 driver to enable functions of the Graphics micro (µ) Controller (GuC), the HEVC/H.265 micro (µ) Controller (HuC), as well as framebuffer compression (see [here](https://01.org/linuxgraphics/downloads/firmware), and [here](https://gist.github.com/Brainiarc7/aa43570f512906e882ad6cdd835efe57) for details):

[FILE] **`/etc/modprobe.d/i915.conf`**

    options i915 enable_fbc=1 enable_guc=2

Note that enable_guc shows the kernel as tainted:

`root `[`#`]`dmesg | grep -iE "huc|guc|dmc|i915|drm"`

    [    3.770822] Setting dangerous option enable_guc - tainting kernel
    [    3.771670] i915 0000:00:02.0: vgaarb: deactivate vga console
    [    3.771758] [drm] couldn't get memory information
    [    3.771760] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
    [    3.771760] [drm] Driver supports precise vblank timestamp query.
    [    3.771831] i915 0000:00:02.0: vgaarb: changed VGA decodes: olddecodes=io+mem,decodes=io+mem:owns=io+mem
    [    3.772438] [drm] Applying Increase DDI Disabled quirk
    [    3.772617] mei_hdcp 0000:00:0f.0-b638ab7e-94e2-4ea2-a552-d1c54b627f04: bound 0000:00:02.0 (ops i915_hdcp_component_ops [i915])
    [    3.775721] [drm] Finished loading DMC firmware i915/glk_dmc_ver1_04.bin (v1.4)
    [    4.910767] [drm] failed to retrieve link info, disabling eDP
    [    4.925196] [drm] GuC communication enabled
    [    4.930132] i915 0000:00:02.0: GuC firmware i915/glk_guc_33.0.0.bin version 33.0 submission:disabled
    [    4.930134] i915 0000:00:02.0: HuC firmware i915/glk_huc_ver03_01_2893.bin version 3.1 authenticated:yes
    [    4.931417] [drm] Initialized i915 1.6.0 20190822 for 0000:00:02.0 on minor 0
    [    4.933150] snd_hda_intel 0000:00:0e.0: bound 0000:00:02.0 (ops i915_audio_component_bind_ops [i915])
    [    4.969752] fbcon: i915drmfb (fb0) is primary device
    [    5.151377] i915 0000:00:02.0: fb0: i915drmfb frame buffer device

### [Sound]

[KERNEL] **Sound**

    Device Drivers --->
        <M> Sound card support  --->
            <M> Advanced Linux Sound Architecture --->
                <*> PCI sound devices --->
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
            <M> UHCI HCD (most Intel and VIA) support

\

### [Network]

[KERNEL] **Ethernet**

    Device Drivers --->
        [*] Network device support --->
            [*] Ethernet driver support  --->
            [*] Realtek devices
                <M> Realtek 8169/8168/8101/8125 ethernet support

\

### [Intel MEI]

[KERNEL] **MEI**

    Device Drivers --->
        Misc devices  --->
             Intel Management Engine Interface
             ME Enabled Intel Chipsets
            <M> Intel HDCP2.2 services of ME Interface

\

### [Sensors]

Next to the standard Intel core temperature sensor, the board also contains a a Nuvoton NCT6796D Super I/O chip, which can be used for monitoring and fan control.

[KERNEL] **Sensors**

    Device Drivers --->
        <*> Hardware Monitoring support  --->
            <M> Intel Core/Core2/Atom temperature sensor
            <M> Nuvoton NCT6775F and compatibles

\

### [SMBus]

[KERNEL] **SMBus**

    Device Drivers --->
        I2C support  --->
             I2C support
            [*]   ACPI I2C Operation region support
            <M>   I2C device interface
            [*]   Autoselect pertinent helper modules
                  I2C Hardware Bus support  --->
                  <M> Intel 82801 (ICH/PCH)

## [Portage make.conf]

Many options of Gentoo are set in [/etc/portage/make.conf]. Some of the key aspects are:

[FILE] **`/etc/portage/make.conf`**

    CFLAGS="-march=goldmont-plus -O2 -pipe"
    CXXFLAGS="$

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* intel i965

[FILE] **`/etc/portage/package.use/00cpu-flags`**

    */* CPU_FLAGS_X86: aes mmx mmxext pclmul popcnt sha sse sse2 sse3 sse4_1 sse4_2 ssse3