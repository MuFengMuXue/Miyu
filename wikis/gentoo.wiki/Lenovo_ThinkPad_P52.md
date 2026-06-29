[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**Resources**

[[]][Home](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-p-series-laptops/thinkpad-p52-type-20m9-20ma)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_P52/ThinkPad_P52_Spec.PDF)

[[]][Specifications (by region)](https://psref.lenovo.com/Product/ThinkPad/ThinkPad_P52)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/pccbbs/mobiles_pdf/tp_p52_hmm_v2_en.pdf)

[[]][User Guide](https://download.lenovo.com/pccbbs/mobiles_pdf/p52_ug_en.pdf)

[[]][BIOS Setup](https://download.lenovo.com/pccbbs/mobiles_pdf/lenovo_bios_setup_linux_wmi_sysfs_1.2.pdf)

[[]][ThinkPad P series](https://en.wikipedia.org/wiki/ThinkPad_P_series "wikipedia:ThinkPad P series")

As of 2018-09-30 this is a WIP page inspired by [Lenovo ThinkPad P50](https://wiki.gentoo.org/wiki/Lenovo_ThinkPad_P50 "Lenovo ThinkPad P50"). Feel free to chat with me (zougloub on freenode) if you\'re figuring stuff out or have questions.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Overview]](#Overview)
    -   [[1.2] [Peculiarities]](#Peculiarities)
    -   [[1.3] [Power management]](#Power_management)
    -   [[1.4] [Kernel]](#Kernel)
    -   [[1.5] [Graphics]](#Graphics)
        -   [[1.5.1] [Setup for Hybrid Graphics mode with external displays on the dGPU]](#Setup_for_Hybrid_Graphics_mode_with_external_displays_on_the_dGPU)
        -   [[1.5.2] [Setup for Hybrid Graphics mode without external displays on the dGPU and only using the dGPU for your eDP display]](#Setup_for_Hybrid_Graphics_mode_without_external_displays_on_the_dGPU_and_only_using_the_dGPU_for_your_eDP_display)
        -   [[1.5.3] [Usage]](#Usage)
    -   [[1.6] [FN keys]](#FN_keys)
    -   [[1.7] [Thunderbolt]](#Thunderbolt)
    -   [[1.8] [SD card reader]](#SD_card_reader)
    -   [[1.9] [Smart Card Reader]](#Smart_Card_Reader)
    -   [[1.10] [Input (Trackpoint, Touchpad, Touchscreen)]](#Input_.28Trackpoint.2C_Touchpad.2C_Touchscreen.29)
        -   [[1.10.1] [Touchpad]](#Touchpad)
        -   [[1.10.2] [Touchscreen]](#Touchscreen)
-   [[2] [External resources]](#External_resources)

## [Hardware]

### [Overview]

`root `[`#`]`lscpu`

    Architecture:        x86_64
    CPU op-mode(s):      32-bit, 64-bit
    Byte Order:          Little Endian
    CPU(s):              12
    On-line CPU(s) list: 0-11
    Thread(s) per core:  2
    Core(s) per socket:  6
    Socket(s):           1
    NUMA node(s):        1
    Vendor ID:           GenuineIntel
    CPU family:          6
    Model:               158
    Model name:          Intel(R) Xeon(R) E-2176M  CPU @ 2.70GHz
    Stepping:            10
    CPU MHz:             800.023
    CPU max MHz:         4400.0000
    CPU min MHz:         800.0000
    BogoMIPS:            5424.00
    Virtualization:      VT-x
    L1d cache:           32K
    L1i cache:           32K
    L2 cache:            256K
    L3 cache:            12288K
    NUMA node0 CPU(s):   0-11
    Flags:               fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb invpcid_single pti ssbd ibrs ibpb stibp tpr_shadow vnmi flexpriority ept vpid fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm mpx rdseed adx smap clflushopt intel_pt xsaveopt xsavec xgetbv1 xsaves dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp flush_l1d

`root `[`#`]`lspci -nnk`

    00:00.0 Host bridge [0600]: Intel Corporation Device [8086:3ec4] (rev 07)
            Subsystem: Lenovo Device [17aa:225f]
    00:01.0 PCI bridge [0604]: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor PCIe Controller (x16) [8086:1901] (rev 07)
            Kernel driver in use: pcieport
    00:02.0 VGA compatible controller [0300]: Intel Corporation Device [8086:3e94]
            Subsystem: Lenovo Device [17aa:225f]
            Kernel driver in use: i915
    00:04.0 Signal processing controller [1180]: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem [8086:1903] (rev 07)
            Subsystem: Lenovo Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem [17aa:225f]
    00:08.0 System peripheral [0880]: Intel Corporation Xeon E3-1200 v5/v6 / E3-1500 v5 / 6th/7th Gen Core Processor Gaussian Mixture Model [8086:1911]
            Subsystem: Lenovo Xeon E3-1200 v5/v6 / E3-1500 v5 / 6th/7th Gen Core Processor Gaussian Mixture Model [17aa:225f]
    00:12.0 Signal processing controller [1180]: Intel Corporation Device [8086:a379] (rev 10)
            Subsystem: Lenovo Device [17aa:225f]
    00:14.0 USB controller [0c03]: Intel Corporation Device [8086:a36d] (rev 10)
            Subsystem: Lenovo Device [17aa:225f]
            Kernel driver in use: xhci_hcd
            Kernel modules: xhci_pci
    00:14.2 RAM memory [0500]: Intel Corporation Device [8086:a36f] (rev 10)
            Subsystem: Lenovo Device [17aa:225f]
    00:14.3 Network controller [0280]: Intel Corporation Device [8086:a370] (rev 10)
            Subsystem: Intel Corporation Device [8086:0030]
            Kernel driver in use: iwlwifi
            Kernel modules: iwlwifi
    00:15.0 Serial bus controller [0c80]: Intel Corporation Device [8086:a368] (rev 10)
            Subsystem: Lenovo Device [17aa:225f]
    00:16.0 Communication controller [0780]: Intel Corporation Device [8086:a360] (rev 10)
            Subsystem: Lenovo Device [17aa:225f]
    00:16.3 Serial controller [0700]: Intel Corporation Device [8086:a363] (rev 10)
            Subsystem: Lenovo Device [17aa:225f]
            Kernel driver in use: serial
    00:17.0 SATA controller [0106]: Intel Corporation Device [8086:a353] (rev 10)
            Subsystem: Lenovo Device [17aa:225f]
            Kernel driver in use: ahci
    00:1c.0 PCI bridge [0604]: Intel Corporation Device [8086:a338] (rev f0)
            Kernel driver in use: pcieport
    00:1c.7 PCI bridge [0604]: Intel Corporation Device [8086:a33f] (rev f0)
            Kernel driver in use: pcieport
    00:1d.0 PCI bridge [0604]: Intel Corporation Device [8086:a330] (rev f0)
            Kernel driver in use: pcieport
    00:1e.0 Communication controller [0780]: Intel Corporation Device [8086:a328] (rev 10)
            Subsystem: Lenovo Device [17aa:225f]
    00:1f.0 ISA bridge [0601]: Intel Corporation Device [8086:a30e] (rev 10)
            Subsystem: Lenovo Device [17aa:225f]
    00:1f.3 Audio device [0403]: Intel Corporation Device [8086:a348] (rev 10)
            Subsystem: Lenovo Device [17aa:225f]
            Kernel driver in use: snd_hda_intel
            Kernel modules: snd_hda_intel
    00:1f.4 SMBus [0c05]: Intel Corporation Device [8086:a323] (rev 10)
            Subsystem: Lenovo Device [17aa:225f]
            Kernel driver in use: i801_smbus
    00:1f.5 Serial bus controller [0c80]: Intel Corporation Device [8086:a324] (rev 10)
            Subsystem: Lenovo Device [17aa:225f]
    00:1f.6 Ethernet controller [0200]: Intel Corporation Ethernet Connection (7) I219-LM [8086:15bb] (rev 10)
            Subsystem: Lenovo Ethernet Connection (7) I219-LM [17aa:225f]
            Kernel driver in use: e1000e
    01:00.0 VGA compatible controller [0300]: NVIDIA Corporation Device [10de:1cba] (rev ff)
            Kernel modules: nvidiafb, nouveau, nvidia_drm, nvidia
    01:00.1 Audio device [0403]: NVIDIA Corporation GP107GL High Definition Audio Controller [10de:0fb9] (rev ff)
            Kernel driver in use: snd_hda_intel
            Kernel modules: snd_hda_intel
    70:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS525A PCI Express Card Reader [10ec:525a] (rev 01)
            Subsystem: Lenovo RTS525A PCI Express Card Reader [17aa:225f]
            Kernel driver in use: rtsx_pci
            Kernel modules: rtsx_pci
    71:00.0 Non-Volatile memory controller [0108]: Samsung Electronics Co Ltd NVMe SSD Controller SM951/PM951 [144d:a802] (rev 01)
            Subsystem: Samsung Electronics Co Ltd NVMe SSD Controller SM951/PM951 [144d:a801]
            Kernel driver in use: nvme

`root `[`#`]`lsusb -t`

    /:  Bus 02.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/10p, 10000M
    /:  Bus 01.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/16p, 480M
        |__ Port 8: Dev 2, If 1, Class=Video, Driver=uvcvideo, 480M
        |__ Port 8: Dev 2, If 0, Class=Video, Driver=uvcvideo, 480M
        |__ Port 9: Dev 3, If 0, Class=Vendor Specific Class, Driver=, 12M
        |__ Port 10: Dev 4, If 0, Class=Human Interface Device, Driver=usbhid, 12M
        |__ Port 10: Dev 4, If 1, Class=Human Interface Device, Driver=usbhid, 12M
        |__ Port 12: Dev 5, If 1, Class=Video, Driver=uvcvideo, 480M
        |__ Port 12: Dev 5, If 0, Class=Video, Driver=uvcvideo, 480M
        |__ Port 14: Dev 6, If 0, Class=Wireless, Driver=btusb, 12M
        |__ Port 14: Dev 6, If 1, Class=Wireless, Driver=btusb, 12M

`root `[`#`]`lsusb`

    Bus 001 Device 002: ID 04f2:b614 Chicony Electronics Co., Ltd
    Bus 001 Device 004: ID 056a:5191 Wacom Co., Ltd
    Bus 001 Device 005: ID 04f2:b615 Chicony Electronics Co., Ltd
    Bus 001 Device 006: ID 8087:0aaa Intel Corp.
    Bus 001 Device 003: ID 06cb:009a Synaptics, Inc.
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

### [Peculiarities]

-   (EDIT): The system doesn\'t boot from the Gentoo Install or Gentoo Admin USB Key (converted from ISO as there\'s not optical drive included). In order to get this working you need to boot from another distribution
-   The system boots with Hybrid Graphics Mode, but doesn\'t work correctly. You can\'t run startx or run lspci. it will cause the system to hang when using SystemRescueCD (tested version 6.0.2). To solve this you need to edit the grub configuration before booting and append the following 2 items: acpi_osi=! acpi_osi=\"Windows 2009\" and press F10 to boot. After Hybrid Graphics mode boots fine. The same happens with Ubuntu 18.10. The USB Key boots, it shows the graphical desktop. You can move the mouse around, but you can\'t click anything and nothing else responds. It\'s solved with the acpi_osi kernel parameters.
-   After installing Gentoo with a recent kernel it\'s safe to use acpi_osi=! acpi_osi=\"Linux\". This works without a problem.
-   (EDIT): startx doesnt\'t work when booting as described below. As a temporary solution is to run rmmod nouveau and create an /etc/X11/xorg.conf on the USB key and specify the Intel lines described in the corresponding section below. After xorg will start just fine.
-   (EDIT): Touchpad works fine with the 4.19.\* gentoo-sources kernel after compiling in ELAN support as PS/2 and I2C driver and the IBM TrackPoint driver. It\'s registered as a serio device and after installing and activating gpm I can report that the mouse is working and even scroll functionality of the middle mouse button works
-   Hybrid graphics are not a breeze to use
-   (EDIT): Make sure to run at least UEFI / BIOS version 1.18 due to a corruption bug when switching from Dedicated to Hybrid Graphics mode

### [Power management]

This section deals with:

-   Tips for reducing power consumption
-   Suspend/resume

TODO see Lenovo_ThinkPad_P50

### [Kernel]

To get everything working properly including power management and Low Power Subsystems support, make sure the following items are included in the .config file

It will be useful to manual apply the [patch](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/patch/?id=14232c6e788cb1f7b96dbd08b077f90923324b24) from kernel 5.8 for dual fan control

** Note**\
Tested on kernel version 5.3.12 and 5.7.10

`root `[`#`]`cd /usr/src/linux `

`root `[`#`]`curl "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/patch/?id=14232c6e788cb1f7b96dbd08b077f90923324b24" > dualfan.patch `

`root `[`#`]`patch -p1 < dualfan.patch `

TODO

### [Graphics]

The laptop has an integrated Intel GPU (iGPU) and a second NVIDIA GPU (dGPU). External displays are routed through the dGPU, and the laptop screen is connected to the iGPU.

There\'s several ways to configure the display(s).

-   The BIOS: It can either enable hybrid graphics or only the dGPU.
-   The bbswitch module (part of Bumblebee) can enable/disable the dGPU in a hybrid graphics configuration.
-   Bumblebee can route OpenGL / OpenCL calls to the dGPU.
-   The PRIME \"thing\" handles display routing through one or the other GPU.
-   Using the nouveau or NVIDIA proprietary drivers.

Obviously:

-   If external displays are to be used, the dGPU must be on.
-   The iGPU uses less power (see Power Management).
-   The ideal configuration is Hybrid Graphics, with all display connectors available, and rendering mainly done using the iGPU, with the dGPU helping out for graphics-intensive loads and when external displays are to be used.

Notable configurations that work:

1.  BIOS in discrete graphics with NVIDIA-only display (that\'s the easiest way)
2.  BIOS in hybrid graphics with Intel-only display and Bumblebee, no external displays (everything is good except for no external displays)
3.  BIOS in hybrid graphics with laptop panel on iGPU and xf86-video-intel (not modesetting) and external displays using eGPU and NVIDIA proprietary drivers, which will be detailed hereafter.

The configuration of bumblebee needs to be adjusted according to usage.

\

#### [Setup for Hybrid Graphics mode with external displays on the dGPU]

1.  Install NVIDIA proprietary drivers
2.  Install [[[x11-misc/bumblebee]](https://packages.gentoo.org/packages/x11-misc/bumblebee)[]] and [[[sys-power/bbswitch]](https://packages.gentoo.org/packages/sys-power/bbswitch)[]]
3.  Edit Bumblebee\'s [xorg.conf.nvidia] as follows (important bits are `UseEDID` and `AllowEmptyInitialConfiguration`):

    ::: box-caption
    [FILE] **`/etc/bumblebee/xorg.conf.nvidia`**
    :::

    :::
        Section "ServerLayout"
            Identifier  "Layout0"
            Option      "AutoAddDevices" "false" # prevent plugging udev devices to this server
            Option      "AutoAddGPU" "false" # only nvidia
        EndSection

        Section "Device"
            Identifier  "DiscreteNvidia"
            Driver      "nvidia"
            VendorName  "NVIDIA Corporation"
            BusID "PCI:01:00:0"
            Option "ProbeAllGpus" "false"
            Option "NoLogo" "true"
            Option "UseEDID" "true" # detect external monitors resolutions
            Option "AllowEmptyInitialConfiguration" # work even if no display
        EndSection
    :::
4.  Edit Bumblebee\'s configuration file

    ::: box-caption
    [FILE] **`/etc/bumblebee/bumblebee.conf`**
    :::

    :::
        KeepUnusedXServer=false
        TurnOffCardAtExit=true
    :::
5.  Restart the bumblebeed daemon
    1.  For systemd users: systemctl enable bumblebeed && systemctl start bumblebeed
    2.  For openRC users: rc-update add bumblebeed default && service bumblebeed start

Note: Failure to change the settings above, will cause the keyboard to stop responding when exiting X or restarting the bumblebeed daemon.

1.  Add an [xorg.conf.d] snippet as follows (to use the `intel` driver, which offers [intel-virtual-output]):

    ::: box-caption
    [FILE] **`/etc/X11/xorg.conf.d/intel.conf`**
    :::

    :::
        Section "Device"
            Identifier     "intel"
            Driver         "intel"
            Option         "TearFree"    "true" # not relevant here but useful
        EndSection
    :::

#### [Setup for Hybrid Graphics mode without external displays on the dGPU and only using the dGPU for your eDP display]

1.  Set [/etc/bumblebee/bumblebee.conf] to have `PMMethod=none` and `KeepUnusedXServer=true`, which allows to keep the display active after running a dummy [optirun true]

#### [Usage]

1.  Run [optirun true] to start the Bumblebee X server if you want to start display output on your local screen
2.  Run [intel-virtual-output] to plug the NVIDIA hardware outputs as virtual outputs on the current X screen
3.  At this point the plugged external monitors will become available in XRandR, as virtual devices, e.g.

`user `[`$`]`xrandr`

    [...]
    VIRTUAL1 disconnected (normal left inverted right x axis y axis)
    VIRTUAL2 disconnected (normal left inverted right x axis y axis)
    VIRTUAL3 disconnected (normal left inverted right x axis y axis)
    VIRTUAL4 disconnected (normal left inverted right x axis y axis)
    VIRTUAL5 connected 2560x1440+1920+0 (normal left inverted right x axis y axis) 0mm x 0mm
       2560x1440     59.95*
    [...]

### [FN keys]

### [Thunderbolt]

Use [tbtadm] ([[[sys-apps/thunderbolt-software-user-space]](https://packages.gentoo.org/packages/sys-apps/thunderbolt-software-user-space)[]]) or [boltctl] ([[[sys-apps/bolt]](https://packages.gentoo.org/packages/sys-apps/bolt)[]]).

DisplayPort outputs are simply routed graphics, i.e. their working depends on the GPU configuration\...

### [SD card reader]

Handled by the `rtsx_pci_sdmmc` kernel module.

### [Smart Card Reader]

Some versions of the Lenovo ThinkPad P52 contain a Alcor AU based series USB Smart Card reader. Follow the [PCSC Lite guide](https://wiki.gentoo.org/wiki/PCSC-Lite "PCSC-Lite") to get this working. The driver needed is: [[[app-crypt/ccid]](https://packages.gentoo.org/packages/app-crypt/ccid)[]].

### [][Input (Trackpoint, Touchpad, Touchscreen)]

`root `[`#`]`lsinput`

        0: 0000:0003 HOST   PNP0C0E/button/i Sleep Button             KEY
        1: 0000:0005 HOST   PNP0C0D/button/i Lid Switch               SW
        2: 0000:0001 HOST   LNXPWRBN/button/ Power Button             KEY
        3: 0000:0006 HOST   LNXVIDEO/video/i Video Bus                KEY
        4: 0000:0006 HOST   LNXVIDEO/video/i Video Bus                KEY
        5: 0001:0002 I8042  isa0060/serio0/i AT Raw Set 2 keyboard    KEY MSC LED
        6: 001f:0001 ISA    isa0061/input0   PC Speaker               SND
        7: 17aa:5054 HOST   thinkpad_acpi/in ThinkPad Extra Buttons   KEY MSC SW
        8: 10ec:0285 PCI    card0/codec#0/be HDA Digital PCBeep       SND
        9: 0000:0000 (null) ALSA             HDA Intel PCH Mic        SW
       10: 0000:0000 (null) ALSA             HDA Intel PCH Headphone  SW
       11: 0000:0000 (null) ALSA             HDA Intel PCH HDMI/DP,pc SW
       12: 0000:0000 (null) ALSA             HDA Intel PCH HDMI/DP,pc SW
       13: 0000:0000 (null) ALSA             HDA Intel PCH HDMI/DP,pc SW
       14: 0000:0000 (null) ALSA             HDA Intel PCH HDMI/DP,pc SW
       15: 0000:0000 (null) ALSA             HDA Intel PCH HDMI/DP,pc SW
       16: 0000:0000 (null) ALSA             HDA NVidia HDMI/DP,pcm=3 SW
       17: 0000:0000 (null) ALSA             HDA NVidia HDMI/DP,pcm=7 SW
       18: 0000:0000 (null) ALSA             HDA NVidia HDMI/DP,pcm=8 SW
       19: 0000:0000 (null) ALSA             HDA NVidia HDMI/DP,pcm=9 SW
       20: 0002:000e I8042  isa0060/serio1/i ETPS/2 Elantech TrackPoi KEY REL
       21: 0002:000e I8042  isa0060/serio1/i ETPS/2 Elantech Touchpad KEY ABS
       22: 056a:5191 USB    usb-0000:00:14.0 Wacom Co.,Ltd. Pen and m KEY ABS MSC
       23: 056a:5191 USB    usb-0000:00:14.0 Wacom Co.,Ltd. Pen and m ABS
       24: 056a:5191 USB    usb-0000:00:14.0 Wacom Co.,Ltd. Pen and m KEY ABS MSC
       25: 056a:5191 USB    usb-0000:00:14.0 Wacom Co.,Ltd. Pen and m KEY ABS MSC
       26: 056a:5191 USB    usb-0000:00:14.0 Wacom Co.,Ltd. Pen and m KEY ABS MSC
       27: 04f2:b614 USB    usb-0000:00:14.0 Integrated Camera: Integ KEY
       28: 04f2:b615 USB    usb-0000:00:14.0 Integrated IR Camera: In KEY

#### [Touchpad]

In order to have the trackpoint/touchpad work:

-   Ensure the `psmouse` module has been built with elantech options
-   Pass `elantech_smbus=0` to the `psmouse` kernel module (either by kernel command-line or modprobe.d configuration file)

#### [Touchscreen]

In order to have the touchscreen work:

-   Multi-touch is handled by the `wacom` kernel module
-   Multi-touch at the X/Wayland level is handled by the `libinput` X module (*not* `wacom`!).

Notes:

-   [mtdev-test] will show a non-empty list of event if the touchscreen is configured properly:

`root `[`#`]`mtdev-test /dev/input/event22`

    supported mt events:
       ABS_MT_SLOT
       ABS_MT_POSITION_X
       ABS_MT_POSITION_Y
       ABS_MT_TRACKING_ID

-   [libinput debug-events] will show finger ids when configured properly:

`root `[`#`]`libinput debug-events`

    ...
          event22  TOUCH_DOWN       +18.97s      0 (0) 75.90/58.04 (261.25/112.38mm)
          event22  TOUCH_FRAME      +18.97s
          event22  TOUCH_UP         +19.27s
          event22  TOUCH_FRAME      +19.27s
          event22  TOUCH_DOWN       +19.61s      1 (1) 88.99/48.35 (306.32/93.62mm)
          event22  TOUCH_FRAME      +19.61s
          event22  TOUCH_DOWN       +20.05s      2 (2) 95.49/55.60 (328.70/107.65mm)
          event22  TOUCH_FRAME      +20.05s
    ...

-   [[[x11-libs/gtk+]](https://packages.gentoo.org/packages/x11-libs/gtk+)[]]:3\[examples\]\'s gtk3-demo has a multi-touch test window that can be useful to visually check that everything is OK within GTK (there aren\'t so many multi-touch enabled apps out there).

## [External resources]

-   [https://wiki.archlinux.org/title/Lenovo_ThinkPad_P52](https://wiki.archlinux.org/title/Lenovo_ThinkPad_P52)