[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**Resources**

[[]][Official Support Page](https://www.dell.com/support/home/en-au/product-support/product/xps-15-9560-laptop/overview)

[[]][Specifications](https://dl.dell.com/topicspdf/xps-15-9560-laptop_specifications_en-us.pdf)

[[]][Hardware Maintenance Manual](https://dl.dell.com/topicspdf/xps-15-9560-laptop_setup-guide_en-us.pdf)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Dell_XPS#XPS_15_.289560.29 "wikipedia:Dell XPS")

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [Accessories]](#Accessories)
    -   [[1.3] [Firmware]](#Firmware)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [package.use]](#package.use)
    -   [[2.2] [Kernel]](#Kernel)
    -   [[2.3] [Touchpad]](#Touchpad)
    -   [[2.4] [Bumblebee / Primus]](#Bumblebee_.2F_Primus)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Slow 2D graphics]](#Slow_2D_graphics)
    -   [[3.2] [X11 fails to start with \"No Screens Found\"]](#X11_fails_to_start_with_.22No_Screens_Found.22)
    -   [[3.3] [Crash on X11 startup]](#Crash_on_X11_startup)
    -   [[3.4] [Excessive CPU Throttling]](#Excessive_CPU_Throttling)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Hardware]

### [Standard]

  -------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------- ---------------------------------------------------------------- ----------------
  Device               Make/model                                                                                                                                                                                 Status   Kernel driver(s)                                                 Kernel version
  CPU                  Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz                                                                                                                                                  Works                                                                     4.12.5
  Memory               16GB DDR4-2400MHz                                                                                                                                                                          Works
  Hard disk            512GB PCIe Solid State Drive                                                                                                                                                               Works    nvme
  Video card           NVIDIA Corporation GP107M GeForce GTX 1050 Mobile (4GB GDDR5)                                                                                                                              Works    nvidia, fbsimple                                                 4.14.8
  Video card           Intel Corporation Device 591b (rev 04)                                                                                                                                                     Works    i915                                                             4.13
  Wireless             Killer 1535 802.11ac 2x2 WiFi ([Qualcomm Atheros QCA6174](https://wiki.gentoo.org/wiki/Qualcomm_Atheros_QCA6174 "Qualcomm Atheros QCA6174"))                                               Works    ath10k_core ath10k_pci linux-firmware
  Touchscreen          ELAN Touchscreen                                                                                                                                                                           Works    usbhid hid_multitouch                                            4.15.4
  Touchpad             [Synaptics](https://wiki.gentoo.org/wiki/Synaptics "Synaptics") TouchPad                                                                                                                   Works    mouse_ps2_synaptics_smbus                                        4.13.0
  Bluetooth            Killer 1535 Bluetooth                                                                                                                                                                      Works    bluetooth btrtl btintel bnep btbcm rfcomm btusb linux-firmware   4.15.4
  USB 3.0                                                                                                                                                                                                         Works    xhci_hcd
  Thunderbolt 3        2 lanes of PCI Express Gen 3. Supports: Power In / Charging, PowerShare, 40Gbps Bi-Directional, 3.1 USB Gen 2 (10Gbps), VGA, HDMI, Ethernet and USB-A via Dell Adapter (Sold Separately)   Works    ?
  SD Card Reader       SD, SDHC, SDXC                                                                                                                                                                             Works    ?
  Webcam               Widescreen HD (720p)                                                                                                                                                                       Works    uvc                                                              4.14.8
  Microphone           Dual array digital microphones                                                                                                                                                             Works    ?
  Fingerprint reader   138a:0091 Validity Sensors, Inc.                                                                                                                                                           No       None (see below)
  -------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------- ---------------------------------------------------------------- ----------------

Regarding the unsupported fingerprint reader, according to arch wiki, \"The fingerprint reader is a Validity/Synaptics model with USB id 138a:0090. There currently is no Linux driver but an open source Linux driver is being developed by reverse engineering the Windows driver.\". This implies some or earlier versions have the 138a:0090 version, which a driver is now functional for, however mine has the 138a:0091 version, which is unsupported. See [driver development github repository](https://github.com/nmikhailov/Validity90) for further information.

### [Accessories]

Some models have touch screens. Some models are 2-in-1 (break apart). I tested on a conventional (non break apart) model with touch screen, however the touch screen has not been tested. A dock exists however I have never seen it and wouldn\'t personally make use of it. Other reports have described docks in this series as functional, however.

### [Firmware]

BIOS version on receipt was `1.3.4` with `ePSA Build 4304.17 UEFI ROM`.

We need the [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] package to operate the wireless chipset and to provide firmware to upload to the Intel graphics controller to enable things like proper power management.

`root `[`#`]`emerge linux-firmware`

## [Configuration]

### [package.use]

We want to enable a few things in  \...

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* nvidia

[FILE] **`/etc/portage/package.use/00input`**

    */* INPUT_DEVICES: evdev wacom libinput synaptics

### [Kernel]

[KERNEL] **Input support**

    CONFIG_INPUT_EVDEV=y

[KERNEL] **NVMe support**

    CONFIG_NVME_CORE=y
    CONFIG_NVME_=y

[KERNEL] **Wireless support**

    CONFIG_ATH10K=m=y
    CONFIG_ATH10K_PCI=m
    CONFIG_ATH10K_AHB=y
    CONFIG_ATH10K_USB=m

[KERNEL] **Real Time Clock support**

    CONFIG_RTC_CLASS=y
    CONFIG_RTC_HCTOSYS=y
    CONFIG_RTC_SYSTOHC=y
    CONFIG_RTC_NVMEM=y
    CONFIG_RTC_INTF_SYSFS=y
    CONFIG_RTC_INTF_PROC=y
    CONFIG_RTC_INTF_DEV=y
    CONFIG_RTC_DRV_CMOS=y

[KERNEL] **ACPI button support**

    CONFIG_DELL_SMBIOS=y
    CONFIG_DELL_WMI=y
    CONFIG_DELL_WMI_AIO=y
    CONFIG_DELL_WMI_LED=y
    CONFIG_DELL_SMO8800=y
    CONFIG_DELL_RBTN=y

** Note**\
Probably not all of these are needed, but I am too lazy to isolate the correct option. To test this is working, [emerge acpid] then run [acpid && acpi_listen] on the command-line. Pressing the various function keys such as [F11]/[F12] for brightness up and down should show events like `BRTUP` and `BRTDN`. If you don\'t have the correct kernel flags, these will simply shown zeroes and no named/registered ACPI events.

** Important**\
For x86 and AMD64 processors, the in-kernel [framebuffer](https://wiki.gentoo.org/wiki/Framebuffer "Framebuffer") driver conflicts with the binary driver provided by NVIDIA. When compiling the kernel for these CPUs, completely remove support for the in-kernel driver as shown:

[KERNEL] **Disable support for the in-kernel driver**

    Device Drivers --->
        Graphics support --->
            Frame buffer Devices --->
                <*> Support for frame buffer devices --->
                < >   nVidia Framebuffer Support
                < >   nVidia Riva support
                < >   Userspace VESA VGA graphics support
                < >   VESA VGA graphics support
                <*>   Simple framebuffer support
                < >   EFI-based Framebuffer Support

Now make sure the `nouveau` driver is disabled:

[KERNEL]

    Device Drivers  --->
        Graphics support  --->
            < > Nouveau (NVIDIA) cards

Ensure MTRR and kernel module support are enabled.

[KERNEL]

    [*] Enable loadable module support --->
    Processor type and features --->
       [*] MTRR (Memory Type Range Register) support

[KERNEL] **Graphics support**

    CONFIG_FB=y
    CONFIG_FB_BACKLIGHT=y
    CONFIG_FB_NVIDIA=n
    CONFIG_FB_RIVA=n
    CONFIG_DRM_NOUVEAU=n
    CONFIG_FB_EFI=n
    CONFIG_FB_VGA16=n
    CONFIG_FB_UVESA=n
    CONFIG_FB_SIMPLE=y

** Note**\
Unsure whether in-kernel AGP or builtin nvAGP is better on this device. Apparently this varies by device. The switch is this option.

[KERNEL]

    Device Drivers --->
       Graphics support --->
          -*- /dev/agpgart (AGP Support) --->

### [Touchpad]

[Synaptics](https://wiki.gentoo.org/wiki/Synaptics "Synaptics") touch pad.

`root `[`#`]`emerge --ask xf86-input-synaptics`

You can tune this with a tool, see [the arch linux page on synaptics touchpad](https://wiki.archlinux.org/index.php/Touchpad_Synaptics) for more details.

### [][Bumblebee / Primus]

Hybrid Graphics (GPU Switching) is available on the XPS 15 9560. Follow the [Gentoo Bumblebee Wiki](https://wiki.gentoo.org/wiki/NVIDIA/Bumblebee "NVIDIA/Bumblebee") guide to installing it.

** Important**\
There is a known bug with [Bumblebee] whereupon the user cannot start an x server or make any PCI but calls while the GPU is switched off. Symptoms will be a complete system hang when running `nvidia-smi` or `lspci` or similar while [Bumblebee] is ON, [bbswitch] is enabled, and the discrete GPU is off. The answer lies in \[[this Reddit thread](https://www.reddit.com/r/Dell/comments/84bq98/dell_xps_9560_archlinux_and_nvidiabumblebee/%7C)\] and \[[this Arch forums post](https://bbs.archlinux.org/viewtopic.php?id=223056%7C)\]. Add `GRUB_CMDLINE_LINUX_DEFAULT='acpi_rev_override=5 modprobe.blacklist=nvidia nvidia.modeset=0 pcie_port_pm=off acpi_osi="Windows 2009"'` to a grub config file then rebuild grub.

** Note**\
It was necessary on my system to configure Xorg to use the Intel iGPU by default and to have the `nvidia` module loaded in order to start an X server without the system hanging. See the [Troubleshooting Section](https://wiki.gentoo.org/wiki/NVIDIA/Bumblebee#Troubleshooting "NVIDIA/Bumblebee") of the wiki.

## [Troubleshooting]

### [Slow 2D graphics]

According to [this page](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers#Getting_2D_acceleration_to_work_on_machines_with_4GB_memory_or_more "NVIDIA/nvidia-drivers") slow 2D performance attributed to a BIOS setting can be identified via:

`root `[`#`]`cat /proc/mtrr`

    reg00: base=0x00000000 ( 2048MB), size= 2048MB, count=1, uncachable
    ...

If any line contains the word \"uncachable\" apparently you need to reboot, enter BIOS, and change an MTRR setting from \'continuous\' to \'discrete\'. However, on my machine while this is certainly the case, I cannot find such an option in the BIOS.

### [][X11 fails to start with \"No Screens Found\"]

This can be because you have enabled the `efifb` EFI Framebuffer Driver in the kernel. Disable it. Only `CONFIG_FB_SIMPLE=y` (Simple Framebuffer) is OK to leave enabled!

### [Crash on X11 startup]

This can occur you have the `nouveau` driver enabled. You can work around it by adding [nomodeset] to the kernel command line.

### [Excessive CPU Throttling]

When the CPU runs continuously at 100% (say, for instance when emerging larger packages), it can become quite hot. When it crosses certain temperature thresholds, it throttles down the CPU frequency, which in turn makes it run cooler for a while, but at a vastly lower clock frequency. Dell XPS 15:s (and other XPS models) have historically have not had enough airflow to cool the CPU in its default configuration (or the discrete GPU for that matter).

Several workarounds have been attempted with modding the case with cooling pads, tape, better thermal paste, etc. One easy thing to try first is to adjust the voltage of the CPU (and/or the GPU) with the \'sys-power/intel-undervolt\' package.

In the settings in `/etc/intel-undervolt.conf`, try something like this:

       undervolt 0 'CPU' -125
       undervolt 1 'GPU' -75
       undervolt 2 'CPU Cache' -125
       undervolt 3 'System Agent' -75
       undervolt 4 'Analog I/O' 0

Due to a lot of factors depending on your particular machine, you might still be able to get a stable system with even lower figures, or you might have to raise them a bit. It did make a huge difference in temperature, and the CPU did not throttle anymore after these settings.

## [See also]

-   Closed source [NVIDIA drivers](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers "NVIDIA/nvidia-drivers") and open source [Nouveau](https://wiki.gentoo.org/wiki/Nouveau "Nouveau") drivers and [how to switch between them](https://wiki.gentoo.org/wiki/Nouveau_%26_nvidia-drivers_switching "Nouveau & nvidia-drivers switching").
-   [Qualcomm Atheros QCA6174](https://wiki.gentoo.org/wiki/Qualcomm_Atheros_QCA6174 "Qualcomm Atheros QCA6174") and [Gentoo AMD64 Handbook Wireless Networking](https://wiki.gentoo.org/wiki/Handbook:AMD64/Networking/Wireless "Handbook:AMD64/Networking/Wireless")

## [External resources]

-   [https://www.anandtech.com/print/11670/the-dell-xps-15-9560-review-infinity-edge-part-two](https://www.anandtech.com/print/11670/the-dell-xps-15-9560-review-infinity-edge-part-two)
-   [https://wiki.archlinux.org/index.php/Dell_XPS_15_9560](https://wiki.archlinux.org/index.php/Dell_XPS_15_9560)
-   [https://github.com/strelec/dell-xps-15-kernel-config](https://github.com/strelec/dell-xps-15-kernel-config)
-   [https://browser.geekbench.com/geekbench3/8250863](https://browser.geekbench.com/geekbench3/8250863)
-   [https://forums.gentoo.org/viewtopic-p-8114160.html](https://forums.gentoo.org/viewtopic-p-8114160.html)
-   [https://grahamc.com/blog/nixos-on-dell-9560](https://grahamc.com/blog/nixos-on-dell-9560)
-   [https://www.ultrabookreview.com/14875-fix-throttling-xps-15/](https://www.ultrabookreview.com/14875-fix-throttling-xps-15/)