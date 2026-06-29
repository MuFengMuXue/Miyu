**Resources**

[[]][Home](https://www.yubico.com/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/YubiKey "wikipedia:YubiKey")

The YubiKey is a hardware security device that can be used to safely store cryptographic keys, OTP tokens, and challenge response seeds which can be used for authentication or encryption.

Modern YubiKeys have an [OpenPGP module](https://support.yubico.com/hc/en-us/articles/360013790259-Using-Your-YubiKey-with-OpenPGP) which can be used to store GPG keys, they also include U2F modules which can be used for authentication.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [YubiKey 5 FIPS series]](#YubiKey_5_FIPS_series)
    -   [[1.2] [YubiKey 5 BIO series]](#YubiKey_5_BIO_series)
    -   [[1.3] [Security Key Series]](#Security_Key_Series)
    -   [[1.4] [YubiKey 5 Series]](#YubiKey_5_Series)
    -   [[1.5] [YubiKey FIPS (4 Series)]](#YubiKey_FIPS_.284_Series.29)
    -   [[1.6] [YubiHSM Series]](#YubiHSM_Series)
    -   [[1.7] [Legacy Devices]](#Legacy_Devices)
    -   [[1.8] [YubiKey 4 Series]](#YubiKey_4_Series)
    -   [[1.9] [Kernel]](#Kernel)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [U2F & FIDO]](#U2F_.26_FIDO)
    -   [[2.2] [Yubico OTP & Oath TOTP/HOTP]](#Yubico_OTP_.26_Oath_TOTP.2FHOTP)
    -   [[2.3] [PIV Smart Card]](#PIV_Smart_Card)
    -   [[2.4] [GPG]](#GPG)
-   [[3] [Configuration]](#Configuration)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)
-   [[6] [References]](#References)

## [Hardware]

The following tables list all current (2023-04-28) YubiKey devices and their module support as stated on the Yubico website^[\[1\]](#cite_note-1)[\[2\]](#cite_note-2)^.

An in-depth table showing the features of current YubiKeys is located on their [store](https://www.yubico.com/us/store/compare/)

### [YubiKey 5 FIPS series]

  ---------------------------------------------- ------- ------ ------ ------ ------------- ---------
  Device                                         FIDO2   U2F    OTP    OATH   PIV (PC/SC)   OpenPGP
  YubiKey 5C NFC FIPS ^[\[3\]](#cite_note-3)^    Yes     Yes    Yes    Yes    Yes           Yes
  YubiKey 5 NFC FIPS ^[\[4\]](#cite_note-4)^     Yes     Yes    Yes    Yes    Yes           Yes
  YubiKey 5Ci FIPS ^[\[5\]](#cite_note-5)^       Yes     Yes    Yes    Yes    Yes           Yes
  YubiKey 5C FIPS ^[\[6\]](#cite_note-6)^        Yes     Yes    Yes    Yes    Yes           Yes
  YubiKey 5 Nano FIPS ^[\[7\]](#cite_note-7)^    Yes     Yes    Yes    Yes    Yes           Yes
  YubiKey 5C Nano FIPS ^[\[8\]](#cite_note-8)^   Yes     Yes    Yes    Yes    Yes           Yes
  ---------------------------------------------- ------- ------ ------ ------ ------------- ---------

### [YubiKey 5 BIO series]

  -------------------------------------------------------- ------- ------ ----- ------ ------------- ---------
  Device                                                   FIDO2   U2F    OTP   OATH   PIV (PC/SC)   OpenPGP
  YubiKey Bio - FIDO Edition ^[\[9\]](#cite_note-9)^       Yes     Yes    No    No     No            No
  YubiKey C Bio - FIDO Edition ^[\[10\]](#cite_note-10)^   Yes     Yes    No    No     No            No
  -------------------------------------------------------- ------- ------ ----- ------ ------------- ---------

### [Security Key Series]

  ------------------------------------------------------------------- ------- ------ ----- ------ ------------- ---------
  Device                                                              FIDO2   U2F    OTP   OATH   PIV (PC/SC)   OpenPGP
  Security Key NFC - Enterprise Edition ^[\[11\]](#cite_note-11)^     Yes     Yes    No    No     No            No
  Security Key C NFC - Enterprise Edition ^[\[12\]](#cite_note-12)^   Yes     Yes    No    No     No            No
  Security Key C NFC ^[\[13\]](#cite_note-13)^                        Yes     Yes    No    No     No            No
  Security Key by Yubico ^[\[14\]](#cite_note-14)^                    Yes     Yes    No    No     No            No
  FIDO U2F Security Key ^[\[15\]](#cite_note-15)^                     Yes     Yes    No    No     No            No
  Security Key NFC ^[\[16\]](#cite_note-16)^                          Yes     Yes    No    No     No            No
  ------------------------------------------------------------------- ------- ------ ----- ------ ------------- ---------

### [YubiKey 5 Series]

  ------------------------------------------- ------- ------ ------ ------ ------------- ---------
  Device                                      FIDO2   U2F    OTP    OATH   PIV (PC/SC)   OpenPGP
  YubiKey 5C NFC ^[\[17\]](#cite_note-17)^    Yes     Yes    Yes    Yes    Yes           Yes
  YubiKey 5 Nano ^[\[18\]](#cite_note-18)^    Yes     Yes    Yes    Yes    Yes           Yes
  YubiKey 5C Nano ^[\[19\]](#cite_note-19)^   Yes     Yes    Yes    Yes    Yes           Yes
  YubiKey 5 NFC ^[\[20\]](#cite_note-20)^     Yes     Yes    Yes    Yes    Yes           Yes
  YubiKey 5Ci ^[\[21\]](#cite_note-21)^       Yes     Yes    Yes    Yes    Yes           Yes
  YubiKey 5C ^[\[22\]](#cite_note-22)^        Yes     Yes    Yes    Yes    Yes           Yes
  ------------------------------------------- ------- ------ ------ ------ ------------- ---------

### [][YubiKey FIPS (4 Series)]

  ---------------------------------------------------------- ------- ------ ------ ------ ------------- ---------
  Device                                                     FIDO2   U2F    OTP    OATH   PIV (PC/SC)   OpenPGP
  YubiKey C Nano FIPS (4 Series) ^[\[23\]](#cite_note-23)^   No      Yes    Yes    Yes    Yes           Yes
  YubiKey FIPS (4 series) ^[\[24\]](#cite_note-24)^          No      Yes    Yes    Yes    Yes           Yes
  YubiKey Nano FIPS (4 series) ^[\[25\]](#cite_note-25)^     No      Yes    Yes    Yes    Yes           Yes
  YubiKey C FIPS (4 series) ^[\[26\]](#cite_note-26)^        No      Yes    Yes    Yes    Yes           Yes
  ---------------------------------------------------------- ------- ------ ------ ------ ------------- ---------

### [YubiHSM Series]

  ------------------------------------- ------- ----- ----- ------ ------------- ---------
  Device                                FIDO2   U2F   OTP   OATH   PIV (PC/SC)   OpenPGP
  YubiHSM 1 ^[\[27\]](#cite_note-27)^   No      No    No    No     No            No
  YubiHSM2 ^[\[28\]](#cite_note-28)^    No      No    No    No     No            No
  ------------------------------------- ------- ----- ----- ------ ------------- ---------

### [Legacy Devices]

  -------------------------------------------- ------- ------ ------ ------ ------------- ---------
  Device                                       FIDO2   U2F    OTP    OATH   PIV (PC/SC)   OpenPGP
  YubiKey Edge-n ^[\[29\]](#cite_note-29)^     No      Yes    Yes    No     No            No
  YubiKey Edge ^[\[30\]](#cite_note-30)^       No      Yes    Yes    No     No            No
  YubiKey NEO ^[\[31\]](#cite_note-31)^        No      Yes    Yes    Yes    Yes           Yes
  YubiKey NEO-n ^[\[32\]](#cite_note-32)^      No      Yes    Yes    Yes    Yes           Yes
  YubiKey Nano ^[\[33\]](#cite_note-33)^       No      No     Yes    No     No            No
  YubiKey Standard ^[\[34\]](#cite_note-34)^   No      No     Yes    No     No            No
  -------------------------------------------- ------- ------ ------ ------ ------------- ---------

### [YubiKey 4 Series]

  ------------------------------------------- ------- ------ ------ ------ ------------- ---------
  Device                                      FIDO2   U2F    OTP    OATH   PIV (PC/SC)   OpenPGP
  YubiKey 4 ^[\[35\]](#cite_note-35)^         No      Yes    Yes    Yes    Yes           Yes
  YubiKey 4C Nano ^[\[36\]](#cite_note-36)^   No      Yes    Yes    Yes    Yes           Yes
  YubiKey 4 Nano ^[\[37\]](#cite_note-37)^    No      Yes    Yes    Yes    Yes           Yes
  YubiKey 4C ^[\[38\]](#cite_note-38)^        No      Yes    Yes    Yes    Yes           Yes
  ------------------------------------------- ------- ------ ------ ------ ------------- ---------

### [Kernel]

[KERNEL] **Enable support for raw HID devices**

    Device Drivers  --->
      HID support  --->
        -*- HID bus support
        [*]   /dev/hidraw raw HID device support
        USB HID support  --->
          [*] /dev/hiddev raw HID device support

## [Usage]

The different modes of operation of YubiKeys also require different ways for software to interact with them:

-   U2F (through generic HID devices)
-   FIDO (through generic HID devices)
-   Yubico OTP (through libusb)
-   Oath TOTP/HOTP (through libusb)
-   PIV Smart Card (through PC/SC)
-   PGP Smart Card (through a GnuPG-specific PC/SC interface)

** Note**\
[[[dev-libs/libfido2]](https://packages.gentoo.org/packages/dev-libs/libfido2)[]] provide udev rules to allow the plugdev group can access them, and regular users need to be part of \'plugdev\' group to access the key. ^[\[39\]](#cite_note-39)^

### [][U2F & FIDO]

To use Yubikey as U2F/FIDO device, generic HID (*hidraw*) devices may be used.

[[[sys-auth/pam_u2f]](https://packages.gentoo.org/packages/sys-auth/pam_u2f)[]] and [[[net-misc/openssh]](https://packages.gentoo.org/packages/net-misc/openssh)[]] with the *security-key* *USE* flag depend on [[[dev-libs/libfido2]](https://packages.gentoo.org/packages/dev-libs/libfido2)[]], which is required to make use of the FIDO2 functions of YubiKeys.

This mode of interacting with YubiKeys is used by:

-   [YubiKey/PAM](https://wiki.gentoo.org/wiki/YubiKey/PAM "YubiKey/PAM")
-   [YubiKey/SSH](https://wiki.gentoo.org/wiki/YubiKey/SSH "YubiKey/SSH")

### [][Yubico OTP & Oath TOTP/HOTP]

To use Yubikey in some modes, such as OTP challenge-response, raw USB access may be used. This can be either directly or through a library such as [[[sys-auth/libyubikey]](https://packages.gentoo.org/packages/sys-auth/libyubikey)[]].

This mode of interacting with Yubikeys is used by:

-   [[[sys-auth/libyubikey]](https://packages.gentoo.org/packages/sys-auth/libyubikey)[]]
-   [[[sys-auth/yubikey-personalization-gui]](https://packages.gentoo.org/packages/sys-auth/yubikey-personalization-gui)[]] aka `ykinfo`
-   [[[app-admin/keepassxc]](https://packages.gentoo.org/packages/app-admin/keepassxc)[]]

** Note**\
Regular users need to be part of \'usb\' group to access USB or will be confronted with unspecific \'access denied\' messages.

### [PIV Smart Card]

To use Yubikey as a PIV Smart Card, it can be accessed according to the PC/SC specification (short for \"Personal Computer/Smart Card\"). [[[sys-apps/pcsc-lite]](https://packages.gentoo.org/packages/sys-apps/pcsc-lite)[]] provides the daemon [pcscd-service] to interact with smart cards. Instructions for setting up PC/SC can be found at [PCSC-Lite](https://wiki.gentoo.org/wiki/PCSC-Lite "PCSC-Lite").

This mode of interacting with Yubikeys is used by:

-   [[[sys-auth/yubico-piv-tool]](https://packages.gentoo.org/packages/sys-auth/yubico-piv-tool)[]]
-   [[[app-crypt/yubikey-manager]](https://packages.gentoo.org/packages/app-crypt/yubikey-manager)[]] aka `ykman`
-   [[[app-crypt/yubikey-manager-qt]](https://packages.gentoo.org/packages/app-crypt/yubikey-manager-qt)[]]

** Note**\
udev/plugdev need to be configured correctly for the PC/SC daemon to pick-up yubikey plug events.

### [GPG]

Some Yubikeys also run a OpenPGP Smart Card applet. Although it\'s technically PC/SC, GnuGPG is used directly to interact with the Yubikey. This mode of interacting with Yubikeys is used by:

-   [YubiKey/GPG](https://wiki.gentoo.org/wiki/YubiKey/GPG "YubiKey/GPG")
-   [YubiKey/SSH](https://wiki.gentoo.org/wiki/YubiKey/SSH "YubiKey/SSH") through GPG

** Note**\
Generally using any PIV or other PC/SC tools conflicts with GPG working properly.

## [Configuration]

There are various utilities for the configuration of Yubikeys:

-   [[[app-crypt/yubioath-flutter-bin]](https://packages.gentoo.org/packages/app-crypt/yubioath-flutter-bin)[]] allows interface-configuration and generating TOTP-Codes, it is officially called [Yubico-Authenticator](https://www.yubico.com/products/yubico-authenticator/). It requires the pcscd-service, which is described below.
-   [[[app-crypt/yubikey-manager]](https://packages.gentoo.org/packages/app-crypt/yubikey-manager)[]] aka `ykman` allows configuration of OTP, FIDO2, PIV, and enabling/disabling different interfaces (e.g. NFC)
-   [[[app-crypt/yubikey-manager-qt]](https://packages.gentoo.org/packages/app-crypt/yubikey-manager-qt)[]]([deprecated](https://github.com/Yubico/yubikey-manager-qt/issues/361#issuecomment-2277590483), switch over to the [Yubico Authenticator](https://developers.yubico.com/yubioath-flutter/)) a GUI for [[[app-crypt/yubikey-manager]](https://packages.gentoo.org/packages/app-crypt/yubikey-manager)[]]
-   [[[sys-auth/yubico-piv-tool]](https://packages.gentoo.org/packages/sys-auth/yubico-piv-tool)[]] CLI-tool for PIV configuration
-   [[[sys-auth/yubikey-personalization-gui]](https://packages.gentoo.org/packages/sys-auth/yubikey-personalization-gui)[]] aka `ykinfo` allows very low-level and batch configuration of Yubikeys

## [See also]

-   [PAM](https://wiki.gentoo.org/wiki/PAM "PAM") --- allows (third party) services to provide an authentication module for their service which can then be used on PAM enabled systems.
-   [GnuPG](https://wiki.gentoo.org/wiki/GnuPG "GnuPG") --- a free implementation of the OpenPGP standard (RFC 4880).
-   [Google Authenticator](https://wiki.gentoo.org/wiki/Google_Authenticator "Google Authenticator") --- describes an easy way to setup two-factor authentication on Gentoo.
-   [OATH-Toolkit](https://wiki.gentoo.org/wiki/OATH-Toolkit "OATH-Toolkit") --- toolkit for (OTP) One-Time Password authentication using HOTP/TOTP algorithms.

## [External resources]

-   [Yubico Support](https://support.yubico.com/hc/en-us/), Contains many articles on YubiKey configuration

## [References]

1.  [[[↑](#cite_ref-1)] [[https://support.yubico.com/hc/en-us/articles/360013708900-Using-Your-U2F-YubiKey-with-Linux](https://support.yubico.com/hc/en-us/articles/360013708900-Using-Your-U2F-YubiKey-with-Linux)]]
2.  [[[↑](#cite_ref-2)] [[https://support.yubico.com/hc/en-us/articles/360013790259-Using-Your-YubiKey-with-OpenPGP](https://support.yubico.com/hc/en-us/articles/360013790259-Using-Your-YubiKey-with-OpenPGP)]]
3.  [[[↑](#cite_ref-3)] [[https://support.yubico.com/hc/en-us/articles/360021467299-YubiKey-5C-NFC-FIPS](https://support.yubico.com/hc/en-us/articles/360021467299-YubiKey-5C-NFC-FIPS)]]
4.  [[[↑](#cite_ref-4)] [[https://support.yubico.com/hc/en-us/articles/360021443340-YubiKey-5-NFC-FIPS](https://support.yubico.com/hc/en-us/articles/360021443340-YubiKey-5-NFC-FIPS)]]
5.  [[[↑](#cite_ref-5)] [[https://support.yubico.com/hc/en-us/articles/360021443360-YubiKey-5Ci-FIPS](https://support.yubico.com/hc/en-us/articles/360021443360-YubiKey-5Ci-FIPS)]]
6.  [[[↑](#cite_ref-6)] [[https://support.yubico.com/hc/en-us/articles/360021467359-YubiKey-5C-FIPS](https://support.yubico.com/hc/en-us/articles/360021467359-YubiKey-5C-FIPS)]]
7.  [[[↑](#cite_ref-7)] [[https://support.yubico.com/hc/en-us/articles/360021443380-YubiKey-5C-Nano-FIPS](https://support.yubico.com/hc/en-us/articles/360021443380-YubiKey-5C-Nano-FIPS)]]
8.  [[[↑](#cite_ref-8)] [[https://support.yubico.com/hc/en-us/articles/360021443380-YubiKey-5C-Nano-FIPS](https://support.yubico.com/hc/en-us/articles/360021443380-YubiKey-5C-Nano-FIPS)]]
9.  [[[↑](#cite_ref-9)] [[https://support.yubico.com/hc/en-us/articles/360021467299-YubiKey-5C-NFC-FIPS](https://support.yubico.com/hc/en-us/articles/360021467299-YubiKey-5C-NFC-FIPS)]]
10. [[[↑](#cite_ref-10)] [[https://support.yubico.com/hc/en-us/articles/4407752687378-YubiKey-C-Bio-FIDO-Edition](https://support.yubico.com/hc/en-us/articles/4407752687378-YubiKey-C-Bio-FIDO-Edition)]]
11. [[[↑](#cite_ref-11)] [[https://support.yubico.com/hc/en-us/articles/7450466556700-Security-Key-NFC-Enterprise-Edition](https://support.yubico.com/hc/en-us/articles/7450466556700-Security-Key-NFC-Enterprise-Edition)]]
12. [[[↑](#cite_ref-12)] [[https://support.yubico.com/hc/en-us/articles/7450467794076-Security-Key-C-NFC-Enterprise-Edition](https://support.yubico.com/hc/en-us/articles/7450467794076-Security-Key-C-NFC-Enterprise-Edition)]]
13. [[[↑](#cite_ref-13)] [[https://support.yubico.com/hc/en-us/articles/4408701728914-Security-Key-C-NFC](https://support.yubico.com/hc/en-us/articles/4408701728914-Security-Key-C-NFC)]]
14. [[[↑](#cite_ref-14)] [[https://support.yubico.com/hc/en-us/articles/360013647720-Security-Key-by-Yubico](https://support.yubico.com/hc/en-us/articles/360013647720-Security-Key-by-Yubico)]]
15. [[[↑](#cite_ref-15)] [[https://support.yubico.com/hc/en-us/articles/360013656800-FIDO-U2F-Security-Key](https://support.yubico.com/hc/en-us/articles/360013656800-FIDO-U2F-Security-Key)]]
16. [[[↑](#cite_ref-16)] [[https://support.yubico.com/hc/en-us/articles/360013779399-Security-Key-NFC](https://support.yubico.com/hc/en-us/articles/360013779399-Security-Key-NFC)]]
17. [[[↑](#cite_ref-17)] [[https://support.yubico.com/hc/en-us/articles/360013656980-YubiKey-5-NFC](https://support.yubico.com/hc/en-us/articles/360013656980-YubiKey-5-NFC)]]
18. [[[↑](#cite_ref-18)] [[https://support.yubico.com/hc/en-us/articles/360013708340-YubiKey-5-Nano](https://support.yubico.com/hc/en-us/articles/360013708340-YubiKey-5-Nano)]]
19. [[[↑](#cite_ref-19)] [[https://support.yubico.com/hc/en-us/articles/360013724699-YubiKey-5C-Nano](https://support.yubico.com/hc/en-us/articles/360013724699-YubiKey-5C-Nano)]]
20. [[[↑](#cite_ref-20)] [[https://support.yubico.com/hc/en-us/articles/360016649339-YubiKey-5C-NFC](https://support.yubico.com/hc/en-us/articles/360016649339-YubiKey-5C-NFC)]]
21. [[[↑](#cite_ref-21)] [[https://support.yubico.com/hc/en-us/articles/360013708440-YubiKey-5Ci](https://support.yubico.com/hc/en-us/articles/360013708440-YubiKey-5Ci)]]
22. [[[↑](#cite_ref-22)] [[https://support.yubico.com/hc/en-us/articles/360013724359-YubiKey-5C](https://support.yubico.com/hc/en-us/articles/360013724359-YubiKey-5C)]]
23. [[[↑](#cite_ref-23)] [[https://support.yubico.com/hc/en-us/articles/360013761279-YubiKey-C-Nano-FIPS-4-Series-](https://support.yubico.com/hc/en-us/articles/360013761279-YubiKey-C-Nano-FIPS-4-Series-)]]
24. [[[↑](#cite_ref-24)] [[https://support.yubico.com/hc/en-us/articles/360013761699-YubiKey-FIPS-4-Series-](https://support.yubico.com/hc/en-us/articles/360013761699-YubiKey-FIPS-4-Series-)]]
25. [[[↑](#cite_ref-25)] [[https://support.yubico.com/hc/en-us/articles/360013778259-YubiKey-Nano-FIPS-4-Series-](https://support.yubico.com/hc/en-us/articles/360013778259-YubiKey-Nano-FIPS-4-Series-)]]
26. [[[↑](#cite_ref-26)] [[https://support.yubico.com/hc/en-us/articles/360013729079\--YubiKey-C-FIPS-4-Series-](https://support.yubico.com/hc/en-us/articles/360013729079--YubiKey-C-FIPS-4-Series-)]]
27. [[[↑](#cite_ref-27)] [[https://support.yubico.com/hc/en-us/articles/360013662860\--YubiHSM-1](https://support.yubico.com/hc/en-us/articles/360013662860--YubiHSM-1)]]
28. [[[↑](#cite_ref-28)] [[https://support.yubico.com/hc/en-us/articles/360013643200-YubiHSM-2](https://support.yubico.com/hc/en-us/articles/360013643200-YubiHSM-2)]]
29. [[[↑](#cite_ref-29)] [[https://support.yubico.com/hc/en-us/articles/360013714659-YubiKey-Edge-n](https://support.yubico.com/hc/en-us/articles/360013714659-YubiKey-Edge-n)]]
30. [[[↑](#cite_ref-30)] [[https://support.yubico.com/hc/en-us/articles/360013714619-YubiKey-Edge](https://support.yubico.com/hc/en-us/articles/360013714619-YubiKey-Edge)]]
31. [[[↑](#cite_ref-31)] [[https://support.yubico.com/hc/en-us/articles/360013714579-YubiKey-NEO](https://support.yubico.com/hc/en-us/articles/360013714579-YubiKey-NEO)]]
32. [[[↑](#cite_ref-32)] [[https://support.yubico.com/hc/en-us/articles/360013714639-YubiKey-NEO-n](https://support.yubico.com/hc/en-us/articles/360013714639-YubiKey-NEO-n)]]
33. [[[↑](#cite_ref-33)] [[https://support.yubico.com/hc/en-us/articles/360013656840-YubiKey-Nano](https://support.yubico.com/hc/en-us/articles/360013656840-YubiKey-Nano)]]
34. [[[↑](#cite_ref-34)] [[https://support.yubico.com/hc/en-us/articles/360013656120-YubiKey-Standard](https://support.yubico.com/hc/en-us/articles/360013656120-YubiKey-Standard)]]
35. [[[↑](#cite_ref-35)] [[https://support.yubico.com/hc/en-us/articles/360013714599-YubiKey-4](https://support.yubico.com/hc/en-us/articles/360013714599-YubiKey-4)]]
36. [[[↑](#cite_ref-36)] [[https://support.yubico.com/hc/en-us/articles/360013647840-YubiKey-4C-Nano](https://support.yubico.com/hc/en-us/articles/360013647840-YubiKey-4C-Nano)]]
37. [[[↑](#cite_ref-37)] [[https://support.yubico.com/hc/en-us/articles/360013647780-YubiKey-4-Nano](https://support.yubico.com/hc/en-us/articles/360013647780-YubiKey-4-Nano)]]
38. [[[↑](#cite_ref-38)] [[https://support.yubico.com/hc/en-us/articles/360013647820-YubiKey-4C](https://support.yubico.com/hc/en-us/articles/360013647820-YubiKey-4C)]]
39. [[[↑](#cite_ref-39)] [[https://forums.gentoo.org/viewtopic-t-1119574-start-0.html](https://forums.gentoo.org/viewtopic-t-1119574-start-0.html)]]