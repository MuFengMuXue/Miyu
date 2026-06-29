[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Dell_Latitude_7480&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Official Support Page](https://www.dell.com/support/home/en-us/product-support/product/latitude-14-7480-laptop/overview)

[[]][Hardware Maintenance Manual](https://dl.dell.com/content/manual27916210-dell-latitude-7480-owner-s-manual.pdf)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Dell_Latitude#xx80_Models_.282017.29 "wikipedia:Dell Latitude")

## [Hardware]

### [Standard]

  ------------- ------------------------------------------------------------------------------------------------------------------ ------------- ------------------------ ------------------------------------------------------------ ---------------- ---------------------------------------------
  Device        Make/model                                                                                                         Status        Vendor ID / Product ID   Kernel driver(s)                                             Kernel version   Notes
  CPU           Intel(R) Core(TM) i7-6600U CPU @ 2.60GHz                                                                           Works         N/A                      N/A                                                          6.3.4
  GPU                                                                                                                              Works         N/A                      [Intel](https://wiki.gentoo.org/wiki/Intel "Intel")          6.3.4
  Card reader   Realtek Semiconductor Co., Ltd. RTS525A PCI Express Card Reader                                                    Not tested    10ec:525a                rtsx_pci                                                     6.3.4
  Ethernet      Intel Corporation Ethernet Connection (4) I219-LM                                                                  Works         8086:15d7                [e1000e](https://wiki.gentoo.org/wiki/Ethernet "Ethernet")   6.3.4
  WiFi          Intel Corporation Wireless 8265 / 8275                                                                             Works         8086:24fd                [iwlwifi](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi")    6.3.4            Together with mac80211, cfg80211, iwlmvm.
  Keyboard      AT Translated Set 2 keyboard                                                                                       Works         N/A                      i8042, atkbd                                                 6.3.4
  Touchpad      [DLL07A0:01](https://linux-hardware.org/?id=ps/2:044e-120b-dll07a7-01-044e-120b)   Works         044E:120B                i2c_designware                                               6.3.4            TODO: Requires more drivers/flags/packages.
  Stick         DualPoint Stick                                                                                                    Works         N/A                      i2c_designware                                               6.3.4            TODO: As above.
  ------------- ------------------------------------------------------------------------------------------------------------------ ------------- ------------------------ ------------------------------------------------------------ ---------------- ---------------------------------------------