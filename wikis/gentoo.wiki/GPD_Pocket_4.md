**Resources**

[[]][Home](https://www.gpd.hk/gpdpocket4)

[] This article is a **work in progress**; treat its contents with caution - [Vadorovsky](https://wiki.gentoo.org/wiki/User:Vadorovsky "User:Vadorovsky") ([talk](https://wiki.gentoo.org/index.php?title=User_talk:Vadorovsky&action=edit&redlink=1 "User talk:Vadorovsky (page does not exist)") \| [contribs](https://wiki.gentoo.org/wiki/Special:Contributions/Vadorovsky "Special:Contributions/Vadorovsky")).

**GPD Pocket 4** is an 8\" screen laptop from GPD Corporation.

## [Hardware]

### [Standard]

  ----------------------------- ----------------------------------------------------------- -------- ------------------------ ------------------ ---------------- -------
  Device                        Make/model                                                  Status   Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  CPU                           AMD Ryzen™ AI 9 HX 370                                      Works    N/A                      N/A                6.14.9
  Video card                    AMD Radeon™ 890M                                            Works    1002:150e                amdgpu             6.14.9
  Ethernet controller           Realtek Semiconductor Co., Ltd. RTL8125 2.5GbE Controller   Works    10ec:8125                r8169              6.14.9
  Wireless network controller   Intel Corporation Wi-Fi 6E(802.11ax) AX210/AX1675           Works    8086:2725                iwlwifi            6.14.9
  ----------------------------- ----------------------------------------------------------- -------- ------------------------ ------------------ ---------------- -------

## [LTE broadband]

GPD offers Quectel EC25 LTE modem as an optional module. By default, the modem *fcc-lock* state and needs to be unlocked in order to connect to any network.

Default unlocking by ModemManager can be enabled by linking the following file:

`root `[`#`]`ln -s ../../../usr/share/ModemManager/fcc-unlock.available.d/2c7c /etc/ModemManager/fcc-unlock.d/`