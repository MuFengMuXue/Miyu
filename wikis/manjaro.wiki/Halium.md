## Contents

-   [[1] [Halium 9]](#Halium_9)
    -   [[1.1] [Volla Phone]](#Volla_Phone)
    -   [[1.2] [Other phones]](#Other_phones)
    -   [[1.3] [Installation]](#Installation)
    -   [[1.4] [Features]](#Features)
-   [[2] [See Also]](#See_Also)

## [Halium 9]

It is possible to install Manjaro on some Android phone using Project Halium and libhybris. Currently, only Halium 9 is supported but the plan is to add support for newer Halium versions as well. In order to use Halium 9, you will need to upgrade or downgrade to Android 9 first and install TWRP. Also, unlocking bootloader is necessary.

### [Volla Phone]

There is a premade image for Volla Phone (volla-yggdrasil). This image contains a prebuilt boot image, kernel modules and device specific configuration files.

### [Other phones]

There are also a generic Halium 9 images. You will need to flash a Halium compatible kernel (boot.img) manually and it may be necessary to add some configuration files to get more features working. You can use ssh via USB connection to debug the installation.

    ssh manjaro@10.15.19.82

You can also ask for help at our Telegram group: [https://t.me/manjaroonhalium](https://t.me/manjaroonhalium)

### [Installation]

You can find downloads [here](https://github.com/manjaro-libhybris/image-ci/releases).

To install them you can use adb changing the filename to match your download:

    adb sideload Manjaro-ARM-phosh-volla-yggdrasil-20211213.zip

### [Features]

  -------------------- ------- ------------ ---------------
                       phosh   NemoMobile   Plasma Mobile
  Screen and UI        Y       Y            N
  Carrier Info         Y       Y            N
  Mobile data          Y       ?            N
  Calls                Y       N            N
  SMS                  Y       N            N
  Loudspeaker          Y       Y            N
  Headset              Y       Y            N
  Earpiece             Y       Y            N
  WiFi                 Y       Y            N
  Bluetooth            N       N            N
  Orientation sensor   N       N            N
  Auto-brightness      N       N            N
  Proximity sensor     N       N            N
  Fingerprint          N       N            N
  GPS                  N       N            N
  NFC                  N       N            N
  Battery info         Y       Y            N
  -------------------- ------- ------------ ---------------

# [See Also]

Official website of [TWRP](http://twrp.me)

[Manjaro ARM on Halium image downloads](https://github.com/manjaro-libhybris/image-ci/releases)

[Telegram Group](https://t.me/manjaroonhalium)