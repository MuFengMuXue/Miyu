**Resources**

[[]][Official Support Page](https://www.dell.com/support/home/en-us/product-support/product/xps-13-l321x/overview)

[[]][Hardware Maintenance Manual](https://dl.dell.com/manuals/all-products/esuprt_laptop/esuprt_xps_laptop/xps-13-l321x_owner's%20manual_en-us.pdf)

** Note**\
This article is for the old model of the Dell XPS 13. For the new (2015) model, see [Dell_XPS_13_9343](https://wiki.gentoo.org/wiki/Dell_XPS_13_9343 "Dell XPS 13 9343")

## Contents

-   [[1] [Laptop specifications]](#Laptop_specifications)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Kernel]](#Kernel)
        -   [[2.1.1] [Input devices]](#Input_devices)
        -   [[2.1.2] [USB 2.0 support]](#USB_2.0_support)
        -   [[2.1.3] [USB 3.0 support]](#USB_3.0_support)
        -   [[2.1.4] [Drives and storage]](#Drives_and_storage)
        -   [[2.1.5] [Graphics]](#Graphics)
        -   [[2.1.6] [Wi-Fi]](#Wi-Fi)
        -   [[2.1.7] [CPU frequency scaling]](#CPU_frequency_scaling)
        -   [[2.1.8] [Sound]](#Sound)
        -   [[2.1.9] [Touchpad]](#Touchpad)
        -   [[2.1.10] [Webcam]](#Webcam)
        -   [[2.1.11] [Bluetooth]](#Bluetooth)
        -   [[2.1.12] [OpenRC service]](#OpenRC_service)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Noisy fan]](#Noisy_fan)
    -   [[3.2] [Wireless]](#Wireless)

## [Laptop specifications]

Hardware specs may vary. These are the specs for the model XPS 13 Ultrabook:

-   Intel Core i5-2467M 1.6GHz to 2.3GHz or i7-2637M 1.7GHz to 2.9GHz, 3MB cache
-   4-8GB Dual Channel DDR3 1333MHz
-   Intel HD Graphics 3000-4000 (on-CPU)
-   High Definition Audio with Waves MaxxAudio 4
-   13.3in TFT LCD Widescreen screen (1366x768 or 1920x1080)
-   Samsung PM830 SATA 3 128GB or 256GB mSATA SSD Hard Disk
-   1x USB 2.0 ports and 1x USB 3.0 ports
-   mini-DisplayPort output
-   Intel Centrino Advanced-N 6230 802.11 a/g/n with Intel Smart Connect Technology + Bluetooth 3.0

Printout of lspci:

`root `[`#`]`lspci`

    000:00.0 Host bridge: Intel Corporation 2nd Generation Core Processor Family DRAM Controller (rev 09)
    00:02.0 VGA compatible controller: Intel Corporation 2nd Generation Core Processor Family Integrated Graphics Controller (rev 09)
    00:16.0 Communication controller: Intel Corporation 6 Series/C200 Series Chipset Family MEI Controller #1 (rev 04)
    00:1a.0 USB controller: Intel Corporation 6 Series/C200 Series Chipset Family USB Enhanced Host Controller #2 (rev 05)
    00:1b.0 Audio device: Intel Corporation 6 Series/C200 Series Chipset Family High Definition Audio Controller (rev 05)
    00:1c.0 PCI bridge: Intel Corporation 6 Series/C200 Series Chipset Family PCI Express Root Port 1 (rev b5)
    00:1c.1 PCI bridge: Intel Corporation 6 Series/C200 Series Chipset Family PCI Express Root Port 2 (rev b5)
    00:1c.3 PCI bridge: Intel Corporation 6 Series/C200 Series Chipset Family PCI Express Root Port 4 (rev b5)
    00:1d.0 USB controller: Intel Corporation 6 Series/C200 Series Chipset Family USB Enhanced Host Controller #1 (rev 05)
    00:1f.0 ISA bridge: Intel Corporation QS67 Express Chipset Family LPC Controller (rev 05)
    00:1f.2 SATA controller: Intel Corporation 6 Series/C200 Series Chipset Family 6 port SATA AHCI Controller (rev 05)
    00:1f.3 SMBus: Intel Corporation 6 Series/C200 Series Chipset Family SMBus Controller (rev 05)
    02:00.0 Network controller: Intel Corporation Centrino Advanced-N 6230 (rev 34)
    03:00.0 USB controller: Fresco Logic Device 1009 (rev 02)

Printout of lsusb (builtin devices, no external devices connected):

`root `[`#`]`lsusb`

    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 004 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 003 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
    Bus 004 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
    Bus 003 Device 003: ID 1bcf:288f Sunplus Innovation Technology Inc.
    Bus 004 Device 003: ID 8086:0189 Intel Corp.

Printout of lsmod (builtin devices, no external devices connected):

`root `[`#`]`lsmod`

    Module                  Size  Used by
    ac                      3081  0
    aes_generic            26002  1 aes_x86_64
    aes_x86_64              7340  2
    arc4                    1274  2
    battery                10739  0
    cfg80211              145914  2 iwlwifi,mac80211
    dcdbas                  4864  0
    ehci_hcd               32642  0
    i2c_i801                7262  0
    ipv6                  228393  50
    iwlwifi               166316  0
    mac80211              170414  1 iwlwifi
    pcspkr                  1715  0
    processor              24846  4
    rfkill                  8864  1 cfg80211
    sg                     21140  0
    snd                    47863  13 snd_hda_codec_hdmi,snd_hda_codec_realtek,snd_hda_intel,snd_hda_codec,snd_hwdep,snd_pcm,snd_timer
    snd_hda_codec          60868  3 snd_hda_codec_hdmi,snd_hda_codec_realtek,snd_hda_intel
    snd_hda_codec_hdmi     21505  1
    snd_hda_codec_realtek   101574  1
    snd_hda_intel          20200  4
    snd_hwdep               5078  1 snd_hda_codec
    snd_page_alloc          5977  2 snd_hda_intel,snd_pcm
    snd_pcm                56441  4 snd_hda_codec_hdmi,snd_hda_intel,snd_hda_codec
    snd_timer              15545  2 snd_pcm
    thermal                 7658  0
    usb_common               850  1 usbcore
    usbcore               121978  3 ehci_hcd,xhci_hcd
    xhci_hcd               65190  0

Information from [/proc/cpuinfo]:

`root `[`#`]`cat /proc/cpuinfo`

    processor   : 0
    vendor_id   : GenuineIntel
    cpu family  : 6
    model       : 42
    model name  : Intel(R) Core(TM) i7-2637M CPU @ 1.70GHz
    stepping    : 7
    microcode   : 0x25
    cpu MHz     : 1696.199
    cache size  : 4096 KB
    physical id : 0
    siblings    : 4
    core id     : 0
    cpu cores   : 2
    apicid      : 0
    initial apicid  : 0
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 13
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse
                      sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts nopl xtopology nonstop_tsc
                      aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2
                      x2apic popcnt tsc_deadline_timer aes xsave avx lahf_lm ida arat epb xsaveopt pln pts dts tpr_shadow vnmi
                      flexpriority ept vpid
    bogomips    : 3392.39
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 36 bits physical, 48 bits virtual
    power management:

    processor   : 1
    vendor_id   : GenuineIntel
    cpu family  : 6
    model       : 42
    model name  : Intel(R) Core(TM) i7-2637M CPU @ 1.70GHz
    stepping    : 7
    microcode   : 0x25
    cpu MHz     : 1696.199
    cache size  : 4096 KB
    physical id : 0
    siblings    : 4
    core id     : 0
    cpu cores   : 2
    apicid      : 1
    initial apicid  : 1
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 13
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse
                      sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts nopl xtopology nonstop_tsc
                      aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2
                      x2apic popcnt tsc_deadline_timer aes xsave avx lahf_lm ida arat epb xsaveopt pln pts dts tpr_shadow vnmi
                      flexpriority ept vpid
    bogomips    : 3392.39
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 36 bits physical, 48 bits virtual
    power management:

    processor   : 2
    vendor_id   : GenuineIntel
    cpu family  : 6
    model       : 42
    model name  : Intel(R) Core(TM) i7-2637M CPU @ 1.70GHz
    stepping    : 7
    microcode   : 0x25
    cpu MHz     : 1696.199
    cache size  : 4096 KB
    physical id : 0
    siblings    : 4
    core id     : 1
    cpu cores   : 2
    apicid      : 2
    initial apicid  : 2
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 13
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse
                      sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts nopl xtopology nonstop_tsc
                      aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2
                      x2apic popcnt tsc_deadline_timer aes xsave avx lahf_lm ida arat epb xsaveopt pln pts dts tpr_shadow vnmi
                      flexpriority ept vpid
    bogomips    : 3392.39
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 36 bits physical, 48 bits virtual
    power management:

    processor   : 3
    vendor_id   : GenuineIntel
    cpu family  : 6
    model       : 42
    model name  : Intel(R) Core(TM) i7-2637M CPU @ 1.70GHz
    stepping    : 7
    microcode   : 0x25
    cpu MHz     : 1696.199
    cache size  : 4096 KB
    physical id : 0
    siblings    : 4
    core id     : 1
    cpu cores   : 2
    apicid      : 3
    initial apicid  : 3
    fpu     : yes
    fpu_exception   : yes
    cpuid level : 13
    wp      : yes
    flags       : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse
                      sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts nopl xtopology nonstop_tsc
                      aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2
                      x2apic popcnt tsc_deadline_timer aes xsave avx lahf_lm ida arat epb xsaveopt pln pts dts tpr_shadow vnmi
                      flexpriority ept vpid
    bogomips    : 3392.39
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 36 bits physical, 48 bits virtual
    power management:

## [Installation]

### [Kernel]

#### [Input devices]

#### [USB 2.0 support]

-   Compile the ehci-hcd driver as module.

[KERNEL] **USB controller: Intel Corporation 7 Series/C210 Series Chipset Family USB Enhanced Host Controller #1 (rev 04)**

    Device Drivers  --->
        [*] USB support  --->
            <M>   EHCI HCD (USB 2.0) support
                [*]   Root Hub Transaction Translators
                [*]   Improved Transaction Translators scheduling

#### [USB 3.0 support]

Compile the xhci-hcd driver as module:

[KERNEL] **USB controller: *Fresco Logic Device 1009 (rev 02)* or *Intel Corporation 7 Series/C210 Series Chipset Family USB xHCI Host Controller (rev 04)*, 3.3.1-gentoo**

    Device Drivers  --->
        [*] USB support  --->
            <M>   xHCI HCD (USB 3.0) support

Kernel version 3.3 at least is required for the USB 3 support.

#### [Drives and storage]

Hard drive controller works using AHCI driver in the kernel:

[KERNEL] **Intel Corporation 6 Series/C200 Series Chipset Family 6 port SATA AHCI Controller, 3.3.1-gentoo**

    Device Drivers  --->
        <*> Serial ATA and Parallel ATA drivers  --->
            <*>   AHCI SATA support

#### [Graphics]

[KERNEL] **Intel Corporation 2nd Generation Core Processor Family Integrated Graphics Controller, 3.3.1-gentoo**

    Device Drivers  --->
        Graphics support  --->
            <*> /dev/agpgart (AGP Support)  --->
                <*>   Intel 440LX/BX/GX, I8xx and E7x05 chipset support
            <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support)  --->
                <*>   Intel 8xx/9xx/G3x/G4x/HD Graphics
                [*]     Enable modesetting on intel by default

There is an issue with screen brightness which cannot be adjustable. There are two ways to work around this problem.

The *permanent* way to fix this issue is to apply [this patch](https://bugzilla.kernel.org/attachment.cgi?id=97751) to the kernel sources. The patch is an attachment to [kernel bug #47941](https://bugzilla.kernel.org/show_bug.cgi?id=47941). To apply the patch execute the following commands (tested in kernel 3.9.2).

`root `[`#`]`cd /usr/src/linux `

`root `[`#`]`wget 'https://bugzilla.kernel.org/attachment.cgi?id=97751' -O backlight_fix.patch `

`root `[`#`]`patch -p1 --dry-run -i ./backlight_fix.patch `

`root `[`#`]`patch -p1 -i ./backlight_fix.patch # run this command only if the previous patch command gives no errors `

The *temporary* way to work around the brightness issue is to run the following command. This is only a temporary solution because the command needs to be run on every boot, on every resume from suspend, and every time the screen is blanked by DPMS. This last issue is [kernel bug #53491](https://bugzilla.kernel.org/show_bug.cgi?id=53491).

`root `[`#`]`echo 0 > /sys/class/backlight/intel_backlight/brightness`

Use a script to run it at start up:

[FILE] **`/etc/local.d/backlight.start`**

    #!/bin/bash
    echo 0 > /sys/class/backlight/intel_backlight/brightness

As well as after hibernate and suspend:

[FILE] **`/etc/pm/sleep.d/backlight`**

    #!/bin/bash
    case "$1" in
      suspend|hibernate)
        #do nothing
      ;;
      resume|thaw)
        echo 0 > /sys/class/backlight/intel_backlight/brightness
      ;;
      *)
        exit 1
      ;;
    esac
    exit 0

Both scripts need to be executable:

`root `[`#`]`chmod +x /etc/local.d/backlight.start /etc/pm/sleep.d/backlight`

#### [Wi-Fi]

[KERNEL] **Intel Corporation Centrino Advanced-N 6230, 3.3.1-gentoo**

    [*] Networking support  --->
        [*]   Wireless  --->
            <*>   Generic IEEE 802.11 Networking Stack (mac80211)

    Device Drivers  --->
        [*] Network device support  --->
            Wireless LAN  --->
                <M>   Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)

The kernel will also need the firmware before the wireless card will operate. Emerge either of the following packages.

`root `[`#`]`emerge --ask sys-firmware/iwl6030-ucode`

Alternatively, install the full Linux firmware package:

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

#### [CPU frequency scaling]

[KERNEL] **CPU frequency scaling**

    Power management and ACPI options  --->
        CPU Frequency scaling  --->
        [*] CPU Frequency scaling
        <*>   ACPI Processor P-States driver

#### [Sound]

[KERNEL] **Sound device**

    Device Drivers  --->
        --- Sound card support  --->
            <M>   Advanced Linux Sound Architecture  --->
                [*]   PCI sound devices  --->
                    <M>   Intel HD Audio  --->

#### [Touchpad]

The support for the Cypress touchpad was added in Kernel 3.9.0 thanks to the [Sputnik project](http://en.community.dell.com/techcenter/b/techcenter/archive/2012/05/07/developer-laptop-launches-project-sputnik.aspx).

[KERNEL]

    Device Drivers  --->
        Input device support --->
            -*- Generic input layer (needed for keyboard, mouse, ...)
            [*]   Mice  --->
                <M>   PS/2 mouse
                [*]      Cypress PS/2 mouse protocol extension

#### [Webcam]

The webcam will work using the v4l2 driver (tested) and sunplus driver (untested):

[KERNEL] **Bus 001 Device 003: ID 1bcf:288f Sunplus Innovation Technology Inc.**

    Device Drivers  --->
        <M> Multimedia support  --->
            <M>   Video For Linux
            [*]   Video capture adapters  --->
                    [*]   V4L USB devices  --->
                        <M>   USB Video Class (UVC)
                        [*]     UVC input events device support
                        <M>   GSPCA based webcams  --->
                            <M>   SUNPLUS USB Camera Driver

Test it out with mplayer:

`root `[`#`]`mplayer tv:// -tv driver=v4l2:width=640:height=480:device=/dev/video0 -fps 15 -vf screenshot`

#### [Bluetooth]

It is connected to the internal USB 2.0 port, so make sure to enable [USB 2.0 support](#USB_2.0_Support) and [PC-Card](https://wiki.gentoo.org/wiki/PC-Card "PC-Card") support, as they are prerequisites for Bluetooth operation. Finally, activate the following kernel options:

[KERNEL]

    [*] Networking support  --->
        <*> Bluetooth subsystem support  --->

            Select options for Bluetooth applications, see table below:
            <*>   ...

                Bluetooth device drivers  --->

                   Select a Bluetooth HCI driver, e.g.:
                   <*> HCI USB driver (btusb)

#### [OpenRC service]

Bluetooth is now ready to start:

`root `[`#`]`/etc/init.d/bluetooth start`

To start Bluetooth at boot time, add it the default runlevel:

`root `[`#`]`rc-update add bluetooth default`

## [Troubleshooting]

### [Noisy fan]

On the core i7 model, the fan is running too often and too early. A BIOS firmware upgrade resolved the issue. Download the latest release [here](https://www.dell.com/support/home/us/en/19/product-support/product/xps-13-l321x/drivers).

### [Wireless]

When the laptop is too close to a 802.11n router, the wireless hangs. This is a [known issue](http://bugzilla.intellinuxwireless.org/show_bug.cgi?id=2314) but the Bugzilla was [disabled due to security issues](http://wireless.kernel.org/en/users/Drivers/iwlwifi#Bugzilla).

This firmware issue can be worked around by disabling 11n on the iwlwifi module. First try a temporary workaround:

`root `[`#`]`modprobe -rv iwldvm`

`root `[`#`]`modprobe iwlwifi 11n_disable=1`

It works make the the change permanent:

[FILE] **`/etc/modprobe.d/iwlwifi.conf`**

    options iwlwifi 11n_disable=1