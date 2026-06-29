[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Lenovo_Thinkpad_x140e&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Official Support Page](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-x-series-laptops/thinkpad-x140e)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/withdrawnbook/ThinkPad_X140e.pdf)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/ibmdl/pub/pc/pccbbs/mobiles_pdf/x140e_hmm_sp40a26006_01.pdf)

[[]][User Guide](https://download.lenovo.com/ibmdl/pub/pc/pccbbs/mobiles_pdf/x140e_ug_en.pdf)

[[]][BIOS Setup](https://download.lenovo.com/pccbbs/mobiles_pdf/lenovo_bios_setup_linux_wmi_sysfs_1.2.pdf)

[[]][ThinkPad X series](https://en.wikipedia.org/wiki/ThinkPad_X_series "wikipedia:ThinkPad X series")

The **Lenovo ThinkPad x140e** is an 11.6 inch laptop made by Lenovo. Like other members of the ThinkPad line it is semi-rugged and business needs take priority over design aesthetics. As such it is thicker than many modern laptops but has a lot of I/O connectivity options to show for it. Additionally, the laptop is quite easy to service and both the RAM and the fixed disk are user upgradable.

It makes quite a good \"grab and go\" laptop for casual and office work. It\'s chief drawbacks are its overly sensitive touchpad and buggy WiFi chipset.

## Contents

-   [[1] [Installation]](#Installation)
-   [[2] [Troubleshooting]](#Troubleshooting)
    -   [[2.1] [I installed Gentoo but my WiFi Module Isn\'t Working]](#I_installed_Gentoo_but_my_WiFi_Module_Isn.27t_Working)
    -   [[2.2] [My WiFi suffers frequent drop outs]](#My_WiFi_suffers_frequent_drop_outs)
    -   [[2.3] [I Installed a Better WiFi Card and Now my System Won\'t Boot]](#I_Installed_a_Better_WiFi_Card_and_Now_my_System_Won.27t_Boot)
-   [[3] [External References]](#External_References)

## [Installation]

Installation of Gentoo is straightforward with both [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") and [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd"). The only gotcha is the WiFi module. The WiFi module that ships with the ThinkPad x140e is part of the B43XX. In order to get the WiFi working the following package must be installed:

`root `[`#`]`emerge --ask sys-firmware/b43-firmware`

## [Troubleshooting]

### [][I installed Gentoo but my WiFi Module Isn\'t Working]

This is a common issue. Most likely the B43XX firmware needs to be installed.

`root `[`#`]`emerge --ask sys-firmware/b43-firmware`

### [My WiFi suffers frequent drop outs]

If you suffer frequent dropouts with commands such as [rsync](https://wiki.gentoo.org/wiki/Rsync "Rsync"), [scp](https://wiki.gentoo.org/wiki/Scp "Scp") and similar it\'s most likely a limitation of the WiFi chipset. The B43XX is known to be very buggy at the chipset level. In more typical usage, such as web browsing, it\'s easy not to notice these issues. With usage more typical of a Gentoo user WiFi stability issues are much harder to miss.

### [][I Installed a Better WiFi Card and Now my System Won\'t Boot]

The ThinkPad x140e has a user hostile anti-feature in its firmware: it will not boot with non-Lenovo WiFi modules installed. This would not be so bad except for the issues inherent in the WiFi chipset. A error looks like this:

         1802: Unauthorized network card is plugged in - Power off and remove the miniPCI network card.

Absent a third-party firmware patch to disable this \"feature\" there is no way around this vendor imposed limitation.

## [External References]

-   [Think Wiki Custom BIOS page](https://www.thinkwiki.org/wiki/Custom_BIOS).
-   [1802: Unauthorized network card is plugged in - Power off and remove the miniPCI network card](https://www.thinkwiki.org/wiki/Problem_with_unauthorized_MiniPCI_network_card).