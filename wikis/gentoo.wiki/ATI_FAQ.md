Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/ATI_FAQ/de "ATI FAQ (33% translated)")
-   [English]
-   [italiano](https://wiki.gentoo.org/wiki/ATI_FAQ/it "ATI FAQ (14% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/ATI_FAQ/hu "ATI GYIK (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/ATI_FAQ/ru "ATI FAQ (100% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/ATI_FAQ/zh-cn "ATI FAQ (14% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/ATI_FAQ/ja "ATI FAQ (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/ATI_FAQ/ko "ATI FAQ (14% translated)")

\
This article contains Frequently Asked Questions (FAQ) to help users avoid some common installation and configuration issues related to DRI and X11 for AMD/ATI boards.

## Contents

-   [[1] [Hardware support]](#Hardware_support)
    -   [[1.1] [Are AMD/ATI boards supported?]](#Are_AMD.2FATI_boards_supported.3F)
    -   [[1.2] [I have an All-In-Wonder/Vivo board. Are the multimedia features supported?]](#I_have_an_All-In-Wonder.2FVivo_board._Are_the_multimedia_features_supported.3F)
    -   [[1.3] [I\'m not using an x86-based architecture. What are my options?]](#I.27m_not_using_an_x86-based_architecture._What_are_my_options.3F)
    -   [[1.4] [Are ATI Mobility models supported?]](#Are_ATI_Mobility_models_supported.3F)
-   [[2] [See also]](#See_also)
-   [[3] [External resources]](#External_resources)

## [Hardware support]

### [][Are AMD/ATI boards supported?]

Many AMD/ATI boards (but not all) are supported by Xorg, including 2D/3D accelerated features. For newer GPUs since GCN (Graphics Core Next) Generation 1.1 (Southern Islands and newer) drivers are provided as open source [AMDGPU](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU") and closed source [AMDGPU-PRO](https://wiki.gentoo.org/wiki/AMDGPU-PRO "AMDGPU-PRO"). Both have excellent 2D and 3D accelerated performance.

** Note**\
The [Radeon Feature Matrix](https://www.x.org/wiki/RadeonFeature) at X.org lists the open source driver support level for each part of the graphics card hardware.

  ------------------ ------------------------------------------------------------------------------------------- ------------- ------------------------------------------------------------------------------------ -------------------
  GPU                Common Name                                                                                 Mesa driver   Kernel module                                                                        Xorg driver
  Rage128            Rage128                                                                                     rage128       rage128
  R100               Radeon 7xxx, Radeon 64                                                                      radeon        [radeon](https://wiki.gentoo.org/wiki/Radeon "Radeon")                               radeon
  R200, R250, R280   Radeon 8500, Radeon 9000, Radeon 9200                                                       r200          radeon                                                                               radeon
  R300, R400         Radeon 9500-X850                                                                            r300          radeon                                                                               radeon
  R500               Radeon X1300-X1950                                                                          r300          radeon                                                                               radeon
  R600               Radeon HD2000 series                                                                        r600          radeon                                                                               radeon
  RV670              Radeon HD3000 series                                                                        r600          radeon                                                                               radeon
  RV770 (R700)       Radeon HD4000 series                                                                        r600          radeon                                                                               radeon
  Evergreen          Radeon HD5000 series                                                                        r600          radeon                                                                               radeon
  Northern Islands   Radeon HD6000 series                                                                        r600          radeon                                                                               radeon
  Southern Islands   Radeon HD7000 series (except HD7790), early Radeon R7/R9 series                             radeonsi      radeon, [AMDGPU](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU")^1^                    radeon, amdgpu^1^
  Sea Islands        Radeon HD7790, Radeon R7/R9 series                                                          radeonsi      radeon, AMDGPU, [AMDGPU-PRO](https://wiki.gentoo.org/wiki/AMDGPU-PRO "AMDGPU-PRO")   radeon, amdgpu
  Volcanic Islands   late Radeon R9 series, Radeon R9 Fury, R9 Nano, R9 Fury X, Pro Duo                          radeonsi      radeon, AMDGPU, AMDGPU-PRO                                                           amdgpu
  Arctic Islands     Radeon RX 400/500 series                                                                    radeonsi      AMDGPU, AMDGPU-PRO                                                                   amdgpu
  Vega               Radeon RX Vega                                                                              radeonsi      AMDGPU, AMDGPU-PRO                                                                   amdgpu
  Navi               Radeon RX 5500/5600/5700 (XT)                                                               radeonsi      AMDGPU, AMDGPU-PRO                                                                   amdgpu
  Raven Ridge        all AMD [Ryzen](https://wiki.gentoo.org/wiki/Ryzen "Ryzen") APUs \"with Radeon Graphics\"   radeonsi      AMDGPU, AMDGPU-PRO                                                                   amdgpu
  ------------------ ------------------------------------------------------------------------------------------- ------------- ------------------------------------------------------------------------------------ -------------------

^1^ Experimental, optional support since kernel 4.9-rc1

### [][I have an All-In-Wonder/Vivo board. Are the multimedia features supported?]

Nothing special is necessary for the board\'s multimedia features; [[[x11-drivers/xf86-video-ati]](https://packages.gentoo.org/packages/x11-drivers/xf86-video-ati)[]] should work.

### [][I\'m not using an x86-based architecture. What are my options?]

Xorg support on the **[ppc]** or **[alpha]** platforms is quite similar to **[amd64]** and **[x86]**. The open source Xorg drivers should work well on all architectures.

### [][Are ATI Mobility models supported?]

They should be, but there may be a configuration issue due to the OEM PCI ID on certain chips. In such cases the configuration file may need to be manually written.

## [See also]

-   [Xorg/Hardware 3D acceleration guide](https://wiki.gentoo.org/wiki/Xorg/Hardware_3D_acceleration_guide "Xorg/Hardware 3D acceleration guide") --- a guide to getting 3D acceleration working using the DRM with Xorg in Gentoo.

## [External resources]

-   [Unofficial AMD Linux Driver Wiki](https://wiki.cchtml.com/index.php/Main_Page)

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Luca Barbato, Jorge Paulo, Tiemo Kieft, Joshua Saddler**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*