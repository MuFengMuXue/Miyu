[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Lenovo_ThinkPad_T400&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Hardware Maintenance Manual](https://download.lenovo.com/pccbbs/mobiles_pdf/43y6629_05.pdf)

[[]][ThinkPad T series](https://en.wikipedia.org/wiki/ThinkPad_T_series "wikipedia:ThinkPad T series")

A ThinkPad with [libreboot support](https://libreboot.org/docs/install/t400_external.html).

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [Accessories]](#Accessories)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Emerge]](#Emerge)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [package.use]](#package.use)
    -   [[3.2] [Synaptics Touchpad]](#Synaptics_Touchpad)
    -   [[3.3] [Video]](#Video)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)
-   [[6] [References]](#References)

## [Hardware]

### [Standard]

  --------------------- ----------------------------------------------------------------------------------- -------- --------- ------------------ ---------------- -------
  Device                Make/model                                                                          Status   Bus ID    Kernel driver(s)   Kernel version   Notes
  CPU                   Intel(R) Core(TM)2 Duo CPU P8400 @ 2.26GHz                                          Works    N/A       N/A                4.0.5            N/A
  Video Card            Intel Corporation Mobile 4 Series Chipset Integrated Graphics Controller (rev 07)   Works    00:02.1   i915               4.0.5            N/A
  Ethernet controller   Intel Corporation 82567LM Gigabit Network Connection (rev 03)                       Works    00:19.0   e1000e             4.0.5            N/A
  Audio device          Intel Corporation 82801I (ICH9 Family) HD Audio Controller (rev 03)                 Works    00:1b.0   snd_hda_intel      4.0.5            N/A
  Network controller    Intel Corporation PRO/Wireless 5100 AGN \[Shiloh\] Network Connection               Works    03:00.0   iwlwifi            4.0.5            N/A
  --------------------- ----------------------------------------------------------------------------------- -------- --------- ------------------ ---------------- -------

### [Accessories]

  -------- ------------------- ------------- -------- ------------------ ---------------- -------
  Device   Make/model          Status        Bus ID   Kernel driver(s)   Kernel version   Notes
  Dock     ThinkPad Pro Dock   Not tested    N/A      N/A                N/A              N/A
  -------- ------------------- ------------- -------- ------------------ ---------------- -------

## [Installation]

### [Emerge]

Install the ThinkPad SMAPI BIOS driver

`root `[`#`]`emerge --ask app-laptop/tp_smapi`

## [Configuration]

### [package.use]

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* intel i965

[FILE] **`/etc/portage/package.use/00input`**

    */* INPUT_DEVICES: libinput

[FILE] **`/etc/portage/package.use/00cpu-flags`**

    */* CPU_FLAGS_X86: mmx mmxext sse sse2 sse3 sse4_1 ssse3

### [Synaptics Touchpad]

[FILE] **`/etc/X11/xorg.conf.d/20-touchpad.conf`Synaptics enhanced configuration**

    Section "InputDevice"
            identifier      "touchpad0"
            driver          "synaptics"
            option          "AutoServerLayout" "on"

            # Some extra options for touchpad.
            Option  "LeftEdge"      "1700"
            Option  "RightEdge"     "5300"
            Option  "TopEdge"       "1700"
            Option  "BottomEdge"    "4200"
            Option  "FingerLow"     "25"
            Option  "FingerHigh"    "30"
            Option  "MaxTapTime"    "180"
            Option  "MaxTapMove"    "220"
            Option  "MinSpeed"      "0.7"
            Option  "MaxSpeed"      "0.8"
            Option  "AccelFactor"   "0.0010"
            Option  "SHMConfig"     "on"
            Option  "TapButton1"    "1"
            Option  "VertTwoFingerScroll"   "1"
            Option  "HorizTwoFingerScroll"  "1"
            Option  "VertScrollDelta"       "100"
    EndSection

### [Video]

For detailed graphics card configuration follow the [Intel](https://wiki.gentoo.org/wiki/Intel "Intel") wiki article. The video card can be found out following way:

`root `[`#`]`lspci -nn |grep -i vga `

    00:02.0 VGA compatible controller [0300]: Intel Corporation Mobile 4 Series Chipset Integrated Graphics Controller [8086:2a42] (rev 07)

    VendorId: 8086
    DeviceId: 2a42

The VendorID: 8086 says it is a Intel Chipset, and DeviceID 2a42 defines the VGA Controller as a GMA 4500MHD graphics, and a GM45 chipset.

-   [https://en.wikipedia.org/wiki/List_of_Intel_graphics_processing_units#Fourth_generation](https://en.wikipedia.org/wiki/List_of_Intel_graphics_processing_units#Fourth_generation)

Showing video card using [[[x11-apps/igt-gpu-tools]](https://packages.gentoo.org/packages/x11-apps/igt-gpu-tools)[]]

`root `[`#`]`intel_gpu_top`

    intel-gpu-top: Intel Cantiga (Gen4) @ /dev/dri/card0 - ----/---- MHz; ---% RC6
              0 irqs/s

             ENGINES     BUSY                                     MI_SEMA MI_WAIT
           Render/3D   30.51% |██████████▏                      |    ---%      0%
               Video    0.00% |                                 |    ---%      0%

## [See also]

-   [Installation on libreboot](https://wiki.gentoo.org/wiki/Installation_on_libreboot "Installation on libreboot")
-   [Intel](https://wiki.gentoo.org/wiki/Intel "Intel")

## [External resources]

-   [https://wiki.archlinux.org/index.php/Lenovo_ThinkPad_T400](https://wiki.archlinux.org/index.php/Lenovo_ThinkPad_T400)
-   [http://www.thinkwiki.org/wiki/Install_Gentoo_on_a_Thinkpad_T400](http://www.thinkwiki.org/wiki/Install_Gentoo_on_a_Thinkpad_T400)
-   [http://www.thinkwiki.org/wiki/Category:Gentoo](http://www.thinkwiki.org/wiki/Category:Gentoo)

## [References]

-   [https://libreboot.org/docs/install/t400_external.html](https://libreboot.org/docs/install/t400_external.html)
-   [http://www.thinkwiki.org/wiki/Category:T400](http://www.thinkwiki.org/wiki/Category:T400)