**Resources**

[[]][Product Information](https://www.lenovo.com/us/en/laptops/thinkpad/thinkpad-x1/X1-Carbon-Gen-8-/p/22TP2X1X1C8)

[[]][Official Support Page](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-x-series-laptops/thinkpad-x1-carbon-8th-gen-type-20u9-20ua)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_X1_Carbon_Gen_8/ThinkPad_X1_Carbon_Gen_8_Spec.pdf)

[[]][Specifications (by region)](https://psref.lenovo.com/Product/ThinkPad/ThinkPad_X1_Carbon_Gen_8?tab=model)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/pccbbs/mobiles_pdf/x1_yoga_gen5_x1_carbon_gen8_hmm_en.pdf)

[[]][User Guide](https://download.lenovo.com/pccbbs/mobiles_pdf/x1_yoga_gen5_x1_carbon_gen8_user_guide_linux_fedora.pdf)

[[]][BIOS Setup](https://download.lenovo.com/pccbbs/mobiles_pdf/lenovo_bios_setup_linux_wmi_sysfs_1.2.pdf)

[[]][ThinkPad X1 series](https://en.wikipedia.org/wiki/ThinkPad_X1_series "wikipedia:ThinkPad X1 series")

Lenovo has announced Linux support for numerous of its systems.^[\[1\]](#cite_note-1)^

Amongst them the Lenovo \"ThinkPad X1 Carbon Gen 8\".

Quoting Igor Bergman, Vice President of PCSD Software & Cloud at Lenovo, \"\[\...\] Our goal is to remove the complexity and provide the Linux community with the premium experience that our customers know us for. This is why we have taken this next step to offer Linux-ready devices right out of the box \[\...\]\".

These are steps on getting Gentoo fully functional on the Lenovo X1 Carbon, 8th generation.

The Arch Linux wiki pages for the 7th^[\[2\]](#cite_note-2)^ and 8th^[\[3\]](#cite_note-3)^ generation of this laptop had been a great source of information.

As well as ThinkWiki^[\[4\]](#cite_note-4)^.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [System Model Verfication]](#System_Model_Verfication)
    -   [[1.2] [Standard]](#Standard)
    -   [[1.3] [Accessories]](#Accessories)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [BIOS]](#BIOS)
    -   [[2.2] [USEflags]](#USEflags)
    -   [[2.3] [Firmware]](#Firmware)
    -   [[2.4] [Audio]](#Audio)
        -   [[2.4.1] [Alsa]](#Alsa)
        -   [[2.4.2] [Pulseaudio]](#Pulseaudio)
-   [[3] [See also]](#See_also)
-   [[4] [References]](#References)

## [Hardware]

### [System Model Verfication]

`root `[`#`]`dmidecode -s system-version`

    ThinkPad X1 Carbon Gen 8

\

### [Standard]

  -------------------- ------------------------------------ --------------------------------------- ------------------------ ------------------------------------ ---------------- -----------------------------------------------
  Device               Make/model                           Status                                  Vendor ID / Product ID   Kernel driver(s)                     Kernel version   Notes
  CPU                  Intel(R) Core(TM) i7-10510U CPU      Works                                   N/A                      N/A                                  5.8.13
  Video card           Intel Corporation UHD Graphics       Works                                   8086:9b41                i915                                 5.8.13
  Wireless             Intel Corporation Wireless-AC 9462   Works                                   8086:02f0                iwlmvm                               5.8.13
  Speakers             Skylake+                             Works                                   8086:02c8                snd_soc_skl_hda_dsp, snd_hda_intel   5.8.13
  Microphone           Skylake+                             Needs firmware and configuration        8086:02c8                snd_soc_skl_hda_dsp, snd_hda_intel   5.8.13           DSP Digital mic, Skylake+ platform
  Touchpad             Synaptics                            Needs firmware update                   06cb:00bd                hid-generic,hid-multitouch           5.8.13           USB
  Trackpoint           Elan                                 Works                                   N/A                      psmouse                              5.8.13
  Cameras (internal)   Chicony Electronics                  Works                                   04f2:b6cb                uvcvideo                             5.8.13           USB, Two cameras, C & I
  Fingerprint reader   Synaptics                            Firmware update needed                  06cb:00bd                N/A                                  5.8.13           This device is reported to work by Arch Linux
  Power Management     Lenovo                               BIOS settings needed, S3 sleep state    N/A                      thinkpad_acpi                        5.8.13           Including keyboard backlight and Fn keys
  Bluetooth            Intel                                Works                                   8087:0026                btusb                                5.8.13           USB
  Disk                 Samsung                              Works                                   144d:a808                nvme                                 5.8.13           This might vary on your system
  -------------------- ------------------------------------ --------------------------------------- ------------------------ ------------------------------------ ---------------- -----------------------------------------------

\

### [Accessories]

  ----------------- ------------------- ------------- -------- ------------------ ---------------- --------------
  Device            Make/model          Status        Bus ID   Kernel driver(s)   Kernel version   Notes
  Docking Station   ThinkPad Pro Dock   Not tested    N/A      N/A                N/A              To be tested
  ----------------- ------------------- ------------- -------- ------------------ ---------------- --------------

\

## [Installation]

** Note**\
The only senseful way of running Gentoo on this laptop is in UEFI mode. If you choose legacy BIOS, you will not be able to update firmware and some hardware will not work.

\

### [BIOS]

The following settings are recommended^[\[5\]](#cite_note-5)^.

[CODE]

    Security -> Secure Boot -> Disabled
    Config -> Power -> Sleep State -> Linux
    Security -> Virtualization -> Kernel DMA Protection -> Disabled
    Config -> Thunderbolt BIOS Assist Mode -> Enabled

\

### [USEflags]

  --------------- -----------------------------------------------------------------------
  USEflag         Purpose
  `alsa`          The ALSA Linux sound system
  `alsa-plugin`   Plugins for ALSA
  `bluetooth`     Bluetooth for Linux
  `nvme`          nvme disk support and firmware update
  `synaptics`     Synaptics touchpad and fingerprint reader support und firmware update
  `thunderbolt`   Thunderbolt support and firwmare update
  `tpm`           Trusted Platform support and firmware update
  `uefi`          UEFI support and firmware update
  --------------- -----------------------------------------------------------------------

\

### [Firmware]

Use fwupdmgr to update your systems firmware. Note to USEflags section. System must be started in efi mode and `efivarfs` mounted.

`root `[`#`]`emerge --ask sys-apps/fwupd`

Fetch information from upstream.

`root `[`#`]`fwupdmgr refresh`

Update the system firmware. This will involve reboots. Repeat until no more updates applicable.

`root `[`#`]`fwupdmgr update`

** Note**\
Some hardware is known to only function properly under Linux, after firmware updates, including the touchpad and the fingerprint reader.

** Warning**\
If you forget to include the `uefi` `thunderbolt` `nvme` and co. USEflags, you will not be able to update the firmware of those devices and they might not function properly.

### [Audio]

** Note**\
At the time of the writing of this article, the microphone did not work out of the box.

\

#### [Alsa]

Add `hdsp` and `hdspm` alsa cards to the standard alsa cards.

[FILE] **`/etc/portage/package.use/00audio`**

    */* ALSA_CARDS: hdsp hdspm

The following packaes needed to be installed.

`root `[`#`]`emerge --ask sys-firmware/alsa-firmware media-sound/alsa-utils media-libs/alsa-topology-conf media-libs/alsa-ucm-conf sys-firmware/sof-firmware`

Run `alsamixer`, tune up the volume master and all microphones to maximum and store the settings.

`root `[`#`]`alsamixer`

`root `[`#`]`alsactl store`

#### [Pulseaudio]

The DMIC (Digital Microphone) consists of 4 channels and that topology must be specifically set for pulseaudio.

** Note**\
Some more settings might be needed to prioritize freshly connected HDMI or Headsets over the internal speakers

[FILE] **`/etc/pulse/default.pa`**

    load-module module-alsa-sink device=hw:0,0 channels=4
    load-module module-alsa-source device=hw:0,6 channels=4

** Warning**\
Place `module-alsa-sink` and `module-alsa-source` before `module-udev-detect` and `module-detect`.

Finally restart the system.

\

## [See also]

-   [Lenovo_ThinkPad_X1_Carbon_7th_generation](https://wiki.gentoo.org/wiki/Lenovo_ThinkPad_X1_Carbon_7th_generation "Lenovo ThinkPad X1 Carbon 7th generation")

\

## [References]

1.  [[[↑](#cite_ref-1)] [[Lenovo Launches Linux-Ready ThinkPad and ThinkStation PCs Preinstalled with Ubuntu](https://news.lenovo.com/pressroom/press-releases/lenovo-launches-linux-ready-thinkpad-and-thinkstation-pcs-preinstalled-with-ubuntu/), accessed 9th Oct 2020]]
2.  [[[↑](#cite_ref-2)] [[https://wiki.archlinux.org/index.php/Lenovo_ThinkPad_X1_Carbon\_(Gen_7)](https://wiki.archlinux.org/index.php/Lenovo_ThinkPad_X1_Carbon_(Gen_7)), accessed 9th Oct 2020]]
3.  [[[↑](#cite_ref-3)] [[https://wiki.archlinux.org/index.php/Lenovo_ThinkPad_X1_Carbon\_(Gen_8)](https://wiki.archlinux.org/index.php/Lenovo_ThinkPad_X1_Carbon_(Gen_8)), accessed 9th Oct 2020]]
4.  [[[↑](#cite_ref-4)] [[https://www.thinkwiki.org/wiki/ThinkWiki](https://www.thinkwiki.org/wiki/ThinkWiki), accessed 9th Oct 2020]]
5.  [[[↑](#cite_ref-5)] [[Arch Linux Recommendation](https://wiki.archlinux.org/index.php/Lenovo_ThinkPad_X1_Carbon_(Gen_7)#BIOS_configurations), accessed 9th Oct 2020]]