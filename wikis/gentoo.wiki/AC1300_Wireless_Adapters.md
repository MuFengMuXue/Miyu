## Contents

-   [[1] [Drivers for Realtek\'s chipsets]](#Drivers_for_Realtek.27s_chipsets)
-   [[2] [Kernel configuration]](#Kernel_configuration)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [\"wlan0: Failed to initialize driver interface\"]](#.22wlan0:_Failed_to_initialize_driver_interface.22)
-   [[4] [See also]](#See_also)

## [][Drivers for Realtek\'s chipsets]

-   \"RTW88\" built-in kernel (require firmware) [https://github.com/lwfinger/rtw88](https://github.com/lwfinger/rtw88)
-   \"88x2bu-20210702\" for RTL8822BU (USB) [https://github.com/morrownr/88x2bu-20210702](https://github.com/morrownr/88x2bu-20210702)
-   \"rtl88x2ce-dkms\" for RTL8822CE (PCIE) [https://github.com/juanro49/rtl88x2ce-dkms](https://github.com/juanro49/rtl88x2ce-dkms)

## [Kernel configuration]

[KERNEL]

    Device Drivers --->
      - Generic Driver Options
        - Firmware loader
          - Build named firmware blobs into the kernel binary. Add those two files:
            - regulatory.db regulatory.db.p7s
    [*] Networking support  --->
      - Networking options
        - [*] Packet socket
      - [*] Wireless  --->
        - <*>   cfg80211 - wireless configurtion API
        - <*>   Generic IEEE 802.11 Networking Stack (mac80211)
      - <*>   RF switch subsystem support --->
    Cryptographic API --->
       - Accelerated Cryptographic Algorithms for CPU (x86)  --->
         - <*> Ciphers: AES, modes: ECB, CBC, CTS, CTR, XTR, XTS, GCM (AES-NI)

## [Troubleshooting]

### [][\"wlan0: Failed to initialize driver interface\"]

Make sure that these options are enabled:

[KERNEL]

    - [*] Networking support  --->
      - Networking options
        - [*] Packet socket

## [See also]

-   [AC1200 Wireless Adapters](https://wiki.gentoo.org/wiki/AC1200_Wireless_Adapters "AC1200 Wireless Adapters")
-   [Handbook:AMD64/Networking/Wireless](https://wiki.gentoo.org/wiki/Handbook:AMD64/Networking/Wireless "Handbook:AMD64/Networking/Wireless")