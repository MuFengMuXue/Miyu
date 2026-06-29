[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

[] The information in this article is probably **outdated**. You can help the Gentoo community by verifying and [updating this article](https://wiki.gentoo.org/index.php?title=Lenovo_ThinkPad_X1_Tablet_(Gen_2)&action=edit).

**Resources**

[[]][Official Support Page](https://pcsupport.lenovo.com/us/en/products/tablets/thinkpad-tablet-series/thinkpad-x1-tablet-type-20jb-20jc)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/Think_Tablets/ThinkPad_X1_Tablet_2nd_Gen/ThinkPad_X1_Tablet_2nd_Gen_Spec.PDF)

[[]][Specifications (by region)](https://psref.lenovo.com/Product/Think_Tablets/ThinkPad_X1_Tablet_2nd_Gen)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/pccbbs/mobiles_pdf/x1_tablet_gen_2_hmm_en_sp40j65548_03.pdf)

[[]][User Guide](https://download.lenovo.com/pccbbs/mobiles_pdf/x1_tablet_gen_2_ug_en.pdf)

[[]][ThinkPad X1 series](https://en.wikipedia.org/wiki/ThinkPad_X1_series#X1_Tablet "wikipedia:ThinkPad X1 series")

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [Accessories]](#Accessories)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Kernel]](#Kernel)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Keyboard, trackpoint and touchpad do not work]](#Keyboard.2C_trackpoint_and_touchpad_do_not_work)

## [Hardware]

### [Standard]

  --------------------- ------------- --------- ------------------------ ------------------ ---------------- ----------------------------------
  Device                Make/model    Status    Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  CPU                   i7-7Y75       Works     N/A                      N/A                5.10
  Wi-Fi                 N/A           Works     N/A                      iwlwifi            5.10
  microSD card reader   N/A           Works     N/A                      N/A                5.10
  Touchscreen           WCOM5115:00   Borked    056A:5115                N/A                5.10             Requires Kernel \< 5.10 to work.
  --------------------- ------------- --------- ------------------------ ------------------ ---------------- ----------------------------------

### [Accessories]

  -------- ------------------------ -------- ------------------------ ------------------ ---------------- -------
  Device   Make/model               Status   Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  Dock     ThinkPad OneLink+ Dock   Works    N/A                      N/A                5.10
  -------- ------------------------ -------- ------------------------ ------------------ ---------------- -------

## [Installation]

### [Kernel]

[KERNEL] **Wi-Fi (kernel 5.10)**

    Device Drivers  --->
      [*] Network device support  --->
        [*]   Wireless LAN  --->
          [ ]   ADMtek devices
          [ ]   Atheros/Qualcomm devices
          [ ]   Atmel devices
          [ ]   Broadcom devices
          [ ]   Cisco devices
          [*]   Intel devices
          < >     Intel PRO/Wireless 2100 Network Connection
          < >     Intel PRO/Wireless 2200BG and 2915ABG Network Connection
          < >     Intel Wireless WiFi 4965AGN (iwl4965)
          < >     Intel PRO/Wireless 3945ABG/BG Network Connection (iwl3945)
          <M/*>   Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)
          <M/*>   Intel Wireless WiFi DVM Firmware support
          < >     Intel Wireless WiFi MVM Firmware support
    -> Device Drivers
         -> Network device support
           -> USB Network Adapters
             -> Multi-purpose USB Networking Framework
               -M-   CDC NCM support
               <M>   CDC MBIM support

[KERNEL] **Ethernet (ThinkPad OneLink+ Dock)**

    -> Device Drivers
         -> Network device support
           -> USB Network Adapters
             -> Multi-purpose USB Networking Framework
               <M>   CDC Ethernet support (smart devices such as cable modems)

[KERNEL] **microSD Card Reader**

    -> Device Drivers
      -> <M> MMC/SD/SDIO card support
          <M> Realtek PCI-E SD/MMC Card Interface Driver

      -> Misc devices
          <M> Realtek PCI-E card reader

      -> [*] USB support
        -> [*] USB Mass Storage support
          <M> Realtek Card Reader support

[KERNEL] **DisplayLink (USB-C)**

    Device Drivers --->
        Graphics support --->
            <*> DisplayLink
            <*> Frame buffer Devices --->
                <*> Displaylink USB Framebuffer support

[KERNEL] **Touchscreen**

    Device Drivers --->
        Input device support --->
            <*> Touchscreens --->
                <*> Wacom Tablet support (I2C)

## [Troubleshooting]

### [][Keyboard, trackpoint and touchpad do not work]

For some reason on kernels \>= 4.2 the keyboard, trackpoint and touchpad do not work on first boot. To get around this problem add **i8042.nomux=1 i8042.reset** to the kernel parameters:

[FILE] **`/etc/default.grub`**

    GRUB_CMDLINE_LINUX_DEFAULT="i8042.nomux=1 i8042.reset"