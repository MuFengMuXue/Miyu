[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**Resources**

[[]][Home](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/yoga-series/yoga-13-notebook-ideapad)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/consumer/mobiles_pub/ideapad_yoga_13_hmm.pdf)

[[]][User Guide](https://download.lenovo.com/consumer/mobiles_pub/ideapad_yoga13_ug_v2.0_jul_2012_english.pdf)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Lenovo_IdeaPad_Yoga_13 "wikipedia:Lenovo IdeaPad Yoga 13")

Still working on installation, wiki will come soon.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Laptop Specifications]](#Laptop_Specifications)
        -   [[1.1.1] [Hardware]](#Hardware_2)
-   [[2] [Configuration details]](#Configuration_details)
    -   [[2.1] [Graphics]](#Graphics)
        -   [[2.1.1] [Feature support]](#Feature_support)
    -   [[2.2] [Display]](#Display)
    -   [[2.3] [Wireless]](#Wireless)
        -   [[2.3.1] [Method 1: Using the kernel driver]](#Method_1:_Using_the_kernel_driver)
        -   [[2.3.2] [Method 2: Using the lwfinger driver]](#Method_2:_Using_the_lwfinger_driver)

## [Hardware]

### [Laptop Specifications]

  -------------------- --------------------------------------- ------------- -----------------------------------------------------------
         Device                         Model                      Works                                Notes
    Intel® Core™ i5     3317U, 1.7G/2.6G, 4T, 3M (Ivy Bridge)       Yes
   Intel® HD Graphics                   4000                        Yes                          i915 kernel driver
   LG 13.3\"1600×900           LP133WD2 (SL)(B1) (IPS)              Yes                            intel_backlight
        Wireless                  Realtek RTL8723AU                 Yes       Support Added To Linux 3.15 through r8723au kernel driver
       Bluetooth                     Realtek usb                    Yes
         Camera                        Lenovo                       Yes
      Card Reader                                               Not tested
      Touchscreen                                                 Partial                        Singletouch working
  -------------------- --------------------------------------- ------------- -----------------------------------------------------------

#### [Hardware]

`root `[`#`]`lspci`

    00:00.0 Host bridge: Intel Corporation 3rd Gen Core processor DRAM Controller (rev 09)
    00:02.0 VGA compatible controller: Intel Corporation 3rd Gen Core processor Graphics Controller (rev 09)
    00:04.0 Signal processing controller: Intel Corporation 3rd Gen Core Processor Thermal Subsystem (rev 09)
    00:14.0 USB controller: Intel Corporation 7 Series/C210 Series Chipset Family USB xHCI Host Controller (rev 04)
    00:16.0 Communication controller: Intel Corporation 7 Series/C210 Series Chipset Family MEI Controller #1 (rev 04)
    00:1a.0 USB controller: Intel Corporation 7 Series/C210 Series Chipset Family USB Enhanced Host Controller #2 (rev 04)
    00:1b.0 Audio device: Intel Corporation 7 Series/C210 Series Chipset Family High Definition Audio Controller (rev 04)
    00:1d.0 USB controller: Intel Corporation 7 Series/C210 Series Chipset Family USB Enhanced Host Controller #1 (rev 04)
    00:1f.0 ISA bridge: Intel Corporation QS77 Express Chipset LPC Controller (rev 04)
    00:1f.2 SATA controller: Intel Corporation 7 Series Chipset Family 6-port SATA Controller [AHCI mode] (rev 04)
    00:1f.3 SMBus: Intel Corporation 7 Series/C210 Series Chipset Family SMBus Controller (rev 04)
    00:1f.6 Signal processing controller: Intel Corporation 7 Series/C210 Series Chipset Family Thermal Management Controller (rev 04)

## [Configuration details]

### [Graphics]

See [Intel](https://wiki.gentoo.org/wiki/Intel "Intel").

#### [Feature support]

  ------------ -------- --------------- --------- ----------------------------------------------------- ----------------------------
    Chipset     OpenGL     OpenGL ES     OpenCL    [VAAPI](https://wiki.gentoo.org/wiki/VAAPI "VAAPI")              USE
   Ivy Bridge    3.1     2.0 (3.0)^1^    1.1^2^                            Yes                           VIDEO_CARDS=\"intel i965\"
  ------------ -------- --------------- --------- ----------------------------------------------------- ----------------------------

### [Display]

Backlight control through brightness buttons is enabled by adding the `acpi_backlight=vendor` into the [/etc/default/grub], i.e. `GRUB_CMDLINE_LINUX_DEFAULT="acpi_backlight=vendor"`

### [Wireless]

#### [Method 1: Using the kernel driver]

The r8723au driver provides support for the Realtek RTL8723AU WiFi chipset. The RTL8723AU is the USB version of the Realtek 8723A chipset, with ID of 0bda:1724. Since the version 3.15 of the kernel, the RTL8723AU is supported in the staging drivers.

**Step 1ː** Configure and compile kernel

[KERNEL]

    <M>   Realtek RTL8723AU Wireless LAN NIC driver
    [*]     Realtek RTL8723AU AP mode
    [*]     Realtek RTL8723AU BlueTooth Coexistence

** Note**\
The option \"Realtek RTL8723AU Wireless LAN NIC driver\" in the section \"Device Drivers-\>Staging drivers\" appears if the option \"RF switch subsystem support\" in the \"Networking options\" is enabled.

[KERNEL]

    <M>   RF switch subsystem support  --->

**Step 2:** The gentoo package [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] is required.

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

#### [Method 2: Using the lwfinger driver]

`root `[`#`]`git clone git@github.com:lwfinger/rtl8723au.git `

`root `[`#`]`cd rtl8723au/ `

`root `[`#`]`make `

`root `[`#`]`make install `

`root `[`#`]`modprobe rtl8723au `