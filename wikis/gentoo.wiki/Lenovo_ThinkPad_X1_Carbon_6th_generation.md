**Resources**

[[]][Official Support Page](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-x-series-laptops/thinkpad-x1-carbon-6th-gen-type-20kh-20kg)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_X1_Carbon_6th_Gen/ThinkPad_X1_Carbon_6th_Gen_Spec.PDF)

[[]][Specifications (by region)](https://psref.lenovo.com/Product/ThinkPad/ThinkPad_X1_Carbon_6th_Gen)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/pccbbs/mobiles_pdf/x1_carbon_6thgen_hmm_en.pdf)

[[]][User Guide](https://download.lenovo.com/pccbbs/mobiles_pdf/x1carbon_6thgen_ug_en.pdf)

[[]][BIOS Setup](https://download.lenovo.com/pccbbs/mobiles_pdf/lenovo_bios_setup_linux_wmi_sysfs_1.2.pdf)

[[]][ThinkPad X1 series](https://en.wikipedia.org/wiki/ThinkPad_X1_series "wikipedia:ThinkPad X1 series")

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Firmware]](#Firmware)
    -   [[1.2] [Kernel]](#Kernel)
-   [[2] [External resources]](#External_resources)

## [Installation]

Overall, follow everything in the [installation guide](https://wiki.gentoo.org/wiki/Handbook:AMD64 "Handbook:AMD64") with minor changes.

### [Firmware]

Wireless requires [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] to be merged. See [Linux firmware](https://wiki.gentoo.org/wiki/Linux_firmware "Linux firmware") for more details.

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

### [Kernel]

[KERNEL] **NVMe drive (kernel version 4.13)**

    CONFIG_NVME_CORE=y
    CONFIG_BLK_DEV_NVME=y

## [External resources]

-   [https://wiki.archlinux.org/title/Lenovo_ThinkPad_X1_Carbon\_(Gen_6)](https://wiki.archlinux.org/title/Lenovo_ThinkPad_X1_Carbon_(Gen_6))