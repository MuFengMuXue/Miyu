[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**Resources**

[[]][Official Support Page](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/yoga-series/yoga-3-pro-1370-laptop-lenovo)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/Lenovo_Laptops/Lenovo_Yoga_3_Pro/Lenovo_Yoga_3_Pro_Spec.PDF)

[[]][Specifications (by region)](https://psref.lenovo.com/Product/Yoga/Lenovo_Yoga_3_Pro)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/consumer/mobiles_pub/lenovo_yoga_3_pro_1370_hmm_201512.pdf)

[[]][User Guide](https://download.lenovo.com/consumer/mobiles_pub/lenovo_yoga_3_pro_1370_series_ug_english.pdf)

[[]][Lenovo Yoga](https://en.wikipedia.org/wiki/Lenovo_Yoga#Lenovo_Yoga_3_Pro "wikipedia:Lenovo Yoga")

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Laptop Specifications]](#Laptop_Specifications)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Booting]](#Booting)
    -   [[2.2] [HiDPI]](#HiDPI)
    -   [[2.3] [Wireless]](#Wireless)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Kernel]](#Kernel)

# [Hardware]

## [Laptop Specifications]

  --------------- ----------------------------- ------------------------------ ----------- ------------ ------------------------------------------------------------------------------------------------
  **Type**        **Device**                    **Model**                      **ID**      **Works?**   **Note**
  **Processor**   Intel® Core™ M                5Y70, 5Y71, (Broadwell)        n/a         Yes
  **Graphics**    Intel® HD Graphics            5300                           8086:161e   Yes
  **Display**     13.3\" QHD+ LED (3200x1800)   LTN133YL03-L01                 n/a         Yes
  **Audio**       Intel HDA                     Broadwell-U Audio Controller   8086:160c   Yes          Needs snd_hda_intel
  **Network**     Wireless                      Broadcom BCM4352               14e4:43b1   Yes          Supported by the wl driver only
  **Network**     Bluetooth                     Lenovo NGFF (4352 / 20702)     0489:e07a   Yes          See [Broadcom Bluetooth](https://wiki.gentoo.org/wiki/Broadcom_Bluetooth "Broadcom Bluetooth")
  **Input**       Camera                        Lenovo EasyCamera              5986:0535   ?            Not yet tested
  **Input**       Card Reader                                                              ?            Not yet tested
  **Input**       Touchscreen                                                              Yes
  **Input**       Touchpad                                                                 Yes
  --------------- ----------------------------- ------------------------------ ----------- ------------ ------------------------------------------------------------------------------------------------

\

# [Installation]

** Note**\
I am using SystemRescueCd-x86-4.5.2 as an installation medium, with the \'alternative\' (newer) kernel option, installing an EFI stub kernel instead of a boot loader, and using systemd. YMMV with other choices.

## [Booting]

To get to the boot/BIOS menu, there is no key combination. Press the recessed button next to the power button instead; unintuitively called the \"novo\" button by the documentation. You also might have to disable FastStartup and Secure Boot temporarily in the bios menu to get it to boot from your USB device.

## [HiDPI]

The high DPI means that you have to tweak some settings or suffer through tiny nigh-unreadable text while installing. There are larger fonts available at */usr/share/consolefonts/*, which can be used by running e.g:

`user `[`$`]`setfont ter-128b`

Later on when you get X11 running, it might think your screen is a lot larger then it really is, defaulting to 96 DPI. Setting the window size manually fixes this.

You generally want a DPI double or 50% larger than 96, as it makes bitmap GUI elements scale better. Still, you need software which takes the DPI into account - the default xterm XLFD font, for example, will still look tiny until you replace it with a non-bitmap font.

[FILE] **`/etc/X11/xorg.conf.d/30-monitor.conf`**

    Section "Monitor"
        Identifier "<default monitor>"
        # We want a DPI of 192, i.e. half the size of what x11 thinks our screen is (846mm x 476mm).
        DisplaySize 423 238
    EndSection

## [Wireless]

The only driver available that supports the card is the proprietary **wl** driver, available by installing **net-wireless/broadcom-sta**. If you don\'t have this on your installation drive, you might need to use an external USB NIC.

# [Configuration]

[FILE] **`/etc/portage/make.conf`**

    CFLAGS="-O2 -pipe -march=native"

[FILE] **`/etc/portage/package.use/00input`**

    */* INPUT_DEVICES: evdev synaptics

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* intel i965

[FILE] **`/etc/portage/package.use/00cpu-flags`**

    */*  CPU_FLAGS_X86: aes avx avx2 fma3 mmx mmxext popcnt sse sse2 sse3 sse4_1 sse4_2 ssse3

## [Kernel]

[KERNEL] **Audio**

    Device Drivers  --->
       Sound card support  --->
          Advanced Linux Sound Architecture  --->
             [*] PCI sound devices  --->
             HD-Audio  --->
                 <*> HD Audio PCI
                 [*] Enable generic HD-audio codec parser

[KERNEL] **Wifi**

    Processor type and features  --->
       Preemption Model (Voluntary kernel Preemption (Desktop))  --->
    Networking support  --->
       Wireless  --->
          <*> cfg80211 - wireless configuration API
          <*>   cfg80211 wireless extensions compatibility
          < > Generic IEEE 802.11 netowkring Stack (mac80211)
       <*> RF switch subsystem support

[KERNEL] **Inputs**

    Processor type and features  --->
       [*] Intel Low Power Subsystem Support
    Device Drivers  --->
       Input device support  --->
          <*> Mouse interface
          <*> Event interface
          [*] Keyboards  --->
              <*> AT keyboard
       I2C support  --->
          [*] Autoselect pertinent helper modules
          I2C Hardware Bus support  --->
              <*> Synopsys DesignWare Platform
       HID support  --->
          [*] /dev/hidraw raw HID device support
          [*] Generic HID driver
          Special HID drivers  --->
              <*> HID multitouch panels
              <*> Synaptics RMI4 device support
          I2C HID support  --->
              <*> HID over I2C transport layer