[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**Resources**

[[]][Official Support Page (Kaby Lake)](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-x-series-laptops/thinkpad-x1-carbon-type-20hr-20hq)

[[]][Official Support Page (Skylake)](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-x-series-laptops/thinkpad-x1-carbon-type-20k4-20k3)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_X1_Carbon_5th_Gen/ThinkPad_X1_Carbon_5th_Gen_Spec.PDF)

[[]][Specifications (by region)](https://psref.lenovo.com/Product/ThinkPad/ThinkPad_X1_Carbon_5th_Gen)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/pccbbs/mobiles_pdf/x1_carbon_5th_hmm_en.pdf)

[[]][User Guide](https://download.lenovo.com/pccbbs/mobiles_pdf/x1_carbon_5th_ug_en.pdf)

[[]][BIOS Setup](https://download.lenovo.com/pccbbs/mobiles_pdf/lenovo_bios_setup_linux_wmi_sysfs_1.2.pdf)

[[]][ThinkPad X1 series](https://en.wikipedia.org/wiki/ThinkPad_X1_series "wikipedia:ThinkPad X1 series")

These are my notes on getting my Thinkpad X1 Carbon 5th gen working under Gentoo.

Overall, it\'s been pretty straight forward and worked well. Be sure to check out [The ArchLinux wiki](https://wiki.archlinux.org/index.php/Lenovo_ThinkPad_X1_Carbon_(Gen_5)) for some information as well.

If this is useful, please contribute - I didn\'t write great notes as I went.

## Contents

-   [[1] [SSD]](#SSD)
-   [[2] [Graphics]](#Graphics)
-   [[3] [Sound - Speakers, Microphone]](#Sound_-_Speakers.2C_Microphone)
-   [[4] [Wifi]](#Wifi)
-   [[5] [4G / LTE / \"Qualcomm® Snapdragon™ X7 LTE-A\" / EM7455]](#4G_.2F_LTE_.2F_.22Qualcomm.C2.AE_Snapdragon.E2.84.A2_X7_LTE-A.22_.2F_EM7455)
-   [[6] [Webcam]](#Webcam)
-   [[7] [Thunderbolt Dock - 40AC0135US]](#Thunderbolt_Dock_-_40AC0135US)
-   [[8] [External resources]](#External_resources)

### [SSD]

Worked well out of the box, but took me ten minutes to find it under [/dev/nvme0](https://wiki.gentoo.org/wiki/NVMe "NVMe"). I assume you need the \"CONFIG_BLK_DEV_NVME\", but I didn\'t test without.

### [Graphics]

Using the i915 kernel module (which X11 calls \"intel\").

make.conf has [VIDEO_CARDS](https://wiki.gentoo.org/wiki//etc/portage/make.conf#VIDEO_CARDS "/etc/portage/make.conf")=\"intel i965\"

Currently DRI disabled with: Option \"DRI\" \"false\", not sure if I need that.

### [][Sound - Speakers, Microphone]

Worked out of the box.

Alsamixer reports: Card: HDA Intel PCH Chip: Conexant CX8200

### [Wifi]

Worked out of the box, [iwlwifi](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi") module

### [][4G / LTE / \"Qualcomm® Snapdragon™ X7 LTE-A\" / EM7455]

I haven\'t got this working yet, but I\'ve emailed the mbim developers for some information [here](https://lists.freedesktop.org/archives/libmbim-devel/2017-October/000960.html).

Uses the cdc_mbim module, device shows up under /dev/cdc-wdm0, mine\'s stuck in \"sim-missing\". It may be due to me trying Project Fi as a carrier.

### [Webcam]

Works well, can\'t compare quality or anything but no setup issues. Used the \"uvcvideo\" module.

### [Thunderbolt Dock - 40AC0135US]

I\'ve tested running multiple monitors (via displayport), and usb devices, over this dock.

It works great out of the box, and for hotplugging I needed to enable CONFIG_HOTPLUG_PCI_ACPI in the kernel.

## [External resources]

-   [https://wiki.archlinux.org/title/Lenovo_ThinkPad_X1_Carbon\_(Gen_5)](https://wiki.archlinux.org/title/Lenovo_ThinkPad_X1_Carbon_(Gen_5))