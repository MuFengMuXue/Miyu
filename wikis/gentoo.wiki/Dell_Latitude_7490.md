[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Dell_Latitude_7490&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Official Support Page](https://www.dell.com/support/home/en-au/product-support/product/latitude-14-7490-laptop/overview)

[[]][Specifications](https://dl.dell.com/topicspdf/latitude-14-7490-laptop_owners-manual2_en-us.pdf#_OPENTOPIC_TOC_PROCESSING_d112e12395)

[[]][Hardware Maintenance Manual](https://dl.dell.com/topicspdf/latitude-14-7490-laptop_owners-manual2_en-us.pdf)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Dell_Latitude#xx90_Models_.282018.29 "wikipedia:Dell Latitude")

## [Hardware]

  --------------------- -------------------------------------------------------------------------- ------------- --------------------------------------------------------------------------------------------- ------------------------------------------------------------ ---------------- -------
  Device                Make/model                                                                 Status        Vendor ID / Product ID                                                                        Kernel driver(s)                                             Kernel version   Notes
  CPU                   Intel(R) Core(TM) i7-8650U CPU (8th gen, KabyLake) @ 1.90GHz               Works         N/A                                                                                           N/A                                                          6.9.10
  GPU                   Intel UHD Graphics 620 (rev 07) with 64M memory                            Works         8086:5917                                                                                     i915                                                         6.9.10
  Ethernet              Intel Corporation Ethernet Connection (4) I219-LM (rev 21)                 Works         8086:15d7                                                                                     [e1000e](https://wiki.gentoo.org/wiki/Ethernet "Ethernet")   6.9.10
  WiFi                  Intel Corporation Wireless 8265 / 8275 (rev 78)                            Works         8086:24fd                                                                                     [iwlwifi](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi")    6.9.10
  Bluetooth             Intel Corp. Bluetooth wireless interface                                   Works         8087:0a2b                                                                                     btintel, btusb                                               6.9.10
  Keyboard              AT Translated Set 2 keyboard                                               Works         N/A                                                                                           i8042, atkbd                                                 6.9.10
  Display/touchscreen   LG Display LCD Monitor LGD05A2 1920x1080 309x174mm 14.0-inch               Works         MELF0410:00 1FD2:7007                                                                         hid-multitouch
  Touchpad              N/A                                                                        Works         [DELL081C](https://wiki.gentoo.org/wiki/DELL081C_Touchpad "DELL081C Touchpad"):00 044E:121F   hid-multitouch                                               6.9.10
  Pointstick            N/A                                                                        Works         [DELL081C](https://wiki.gentoo.org/wiki/DELL081C_Touchpad "DELL081C Touchpad"):00 044E:121F   N/A                                                          6.9.10
  Sound                 Intel Corporation Sunrise Point-LP HD Audio (rev 21)                       Works         8086:9d71                                                                                     snd_hda_intel, snd_soc_avs, snd_hda_codec_hdmi               6.9.10
  Webcam                Realtek Semiconductor Corp. Integrated Webcam HD                           Works         0bda:58ca                                                                                     N/A                                                          6.9.10
  Card reader           Realtek Semiconductor Co., Ltd. RTS525A PCI Express Card Reader (rev 01)   Not tested    10ec:525a                                                                                     rtsx_pci                                                     6.9.10
  --------------------- -------------------------------------------------------------------------- ------------- --------------------------------------------------------------------------------------------- ------------------------------------------------------------ ---------------- -------