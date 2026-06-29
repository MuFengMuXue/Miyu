**Resources**

[[]][Home](https://www.tuxedocomputers.com/en/TUXEDO-InfinityBook-Pro-15-Gen10-AMD.tuxedo)

\
The TUXEDO InfinityBook Pro 15 (Gen10) a configurable Linux notebook from 2025.

## Contents

-   [[1] [Hardware]](#Hardware)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [make.conf]](#make.conf)
-   [[3] [Kernel]](#Kernel)
    -   [[3.1] [Processor]](#Processor)
    -   [[3.2] [TUXEDO\'s driver modules]](#TUXEDO.27s_driver_modules)
    -   [[3.3] [Alternative fan control]](#Alternative_fan_control)
-   [[4] [Keyboard]](#Keyboard)
-   [[5] [NPU]](#NPU)
-   [[6] [YT6801]](#YT6801)
-   [[7] [References]](#References)

## [Hardware]

  ---------- ---------------------------------- -------- ---------------- -------------------------------------
  Device     Make/model                         Status   Kernel version   Note
  APU        AMD Ryzen AI 9 HX 370              Works    6.18.7           Depends on chosen configuration.
  Video      Radeon 890M                        Works    6.18.7           Depends on chosen configuration.
  NPU        XDNA 2 NPU                         Works    7.0              Depends on chosen configuration.
  Keyboard   QWERTZ                             Works    6.18.7           should work with every other layout
  WiFi       AMD RZ616 / Mediatek MT7922A22M:   Works    6.18.7           Intel Wi-Fi 6 AX210 available too.
  Ethernet   Motorcomm YT6801                   Works    7.0              Basic functionality
  ---------- ---------------------------------- -------- ---------------- -------------------------------------

## [Installation]

### [make.conf]

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* amdgpu radeonsi

## [Kernel]

Running kernels below 6.17 is not recommended by the vendor, who also reports other issues when not running its kernel and OS. ^[\[1\]](#cite_note-tuxedo_linux_faq-1)^

#### [Processor]

Read [this](https://wiki.gentoo.org/wiki/Ryzen#Kernel "Ryzen") article for the processor.

#### [][TUXEDO\'s driver modules]

Read the [TUXEDO Software](https://wiki.gentoo.org/wiki/TUXEDO_Software "TUXEDO Software") article for further instructions. In general, install **tuxedo-drivers** and **tuxedo-control-center-bin**.

#### [Alternative fan control]

See [https://github.com/timohubois/tuxedo-infinitybook-gen10-fan](https://github.com/timohubois/tuxedo-infinitybook-gen10-fan) for an alternative approach towards fan-control avoiding tuxedo-control-center.

## [Keyboard]

Install the tuxedo-drivers. Backlight can be controlled in **/sys/devices/platform/tuxedo_keyboard/leds/white:kbd_backlight** or tuxedo-control-center.

## [NPU]

The NPU was succesfully tested using the upstream kernel drivers and Lemonade server and FastFlowLM. [User:Lockal/AMDXDNA](https://wiki.gentoo.org/wiki/User:Lockal/AMDXDNA "User:Lockal/AMDXDNA") was a helfpul resource.

## [YT6801]

Starting with kernel 7.0, there is a dwmac_motorcomm module, so Ethernet works out of the box now. Features like WoL, RSS and LED control do not appear part of this ^[\[2\]](#cite_note-yt6801_upstream-2)^. Previously, the official driver could be built from ^[\[3\]](#cite_note-yt6801_vendor-3)^ or TUXEDO\'s fork [https://gitlab.com/tuxedocomputers/development/packages/tuxedo-yt6801](https://gitlab.com/tuxedocomputers/development/packages/tuxedo-yt6801).

## [References]

1.  [[[↑](#cite_ref-tuxedo_linux_faq_1-0)] [[https://www.tuxedocomputers.com/en/FAQ-TUXEDO-InfinityBook-Pro-15-Gen10-AMD.tuxedo](https://www.tuxedocomputers.com/en/FAQ-TUXEDO-InfinityBook-Pro-15-Gen10-AMD.tuxedo)]]
2.  [[[↑](#cite_ref-yt6801_upstream_2-0)] [[https://lore.kernel.org/netdev/20260109093445.46791-2-me@ziyao.cc/](https://lore.kernel.org/netdev/20260109093445.46791-2-me@ziyao.cc/)]]
3.  [[[↑](#cite_ref-yt6801_vendor_3-0)] [[https://www.motor-comm.com/Cn/Skippower/downloadFile.html?id=1817](https://www.motor-comm.com/Cn/Skippower/downloadFile.html?id=1817)]]