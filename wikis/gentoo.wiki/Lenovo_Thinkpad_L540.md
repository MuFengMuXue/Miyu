[] The information in this article is probably **outdated**. You can help the Gentoo community by verifying and [updating this article](https://wiki.gentoo.org/index.php?title=Lenovo_Thinkpad_L540&action=edit).

[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**Resources**

[[]][Home](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-l-series-laptops/thinkpad-l540)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_L540/ThinkPad_L540_Spec.PDF)

[[]][Specifications (by region)](https://psref.lenovo.com/Product/ThinkPad/ThinkPad_L540)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/ibmdl/pub/pc/pccbbs/mobiles_pdf/l440_l540_hmm_en_sp40a26004_04.pdf)

[[]][User Guide](https://download.lenovo.com/ibmdl/pub/pc/pccbbs/mobiles_pdf/l440_l540_ug_en.pdf)

[[]][BIOS Setup](https://download.lenovo.com/pccbbs/mobiles_pdf/lenovo_bios_setup_linux_wmi_sysfs_1.2.pdf)

[[]][ThinkPad_L_series](https://en.wikipedia.org/wiki/ThinkPad_L_series "wikipedia:ThinkPad L series")

This article contains information to assist when installing Gentoo on a Lenovo Thinkpad L540.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [lspci]](#lspci)
-   [[2] [Troubleshooting]](#Troubleshooting)
    -   [[2.1] [Unable to shutdown/reboot, irq N:nobody cared (try booting with the \"irqpoll\" option), system turns dead after resume from hibernation.]](#Unable_to_shutdown.2Freboot.2C_irq_N:nobody_cared_.28try_booting_with_the_.22irqpoll.22_option.29.2C_system_turns_dead_after_resume_from_hibernation.)
    -   [[2.2] [Brightness control does not work]](#Brightness_control_does_not_work)
    -   [[2.3] [After resuming from hibernation system either ends up with black screen or crash shortly after resuming]](#After_resuming_from_hibernation_system_either_ends_up_with_black_screen_or_crash_shortly_after_resuming)
    -   [[2.4] [Wrong order of ALSA cards (First HDMI, then PCH]](#Wrong_order_of_ALSA_cards_.28First_HDMI.2C_then_PCH)
    -   [[2.5] [Random system hangs with possible screen artifacts]](#Random_system_hangs_with_possible_screen_artifacts)

## [Hardware]

### [lspci]

`root `[`#`]`lspci`

    00:00.0 Host bridge: Intel Corporation Xeon E3-1200 v3/4th Gen Core Processor DRAM Controller (rev 06)
    00:02.0 VGA compatible controller: Intel Corporation 4th Gen Core Processor Integrated Graphics Controller (rev 06)
    00:03.0 Audio device: Intel Corporation Xeon E3-1200 v3/4th Gen Core Processor HD Audio Controller (rev 06)
    00:14.0 USB controller: Intel Corporation 8 Series/C220 Series Chipset Family USB xHCI (rev 05)
    00:16.0 Communication controller: Intel Corporation 8 Series/C220 Series Chipset Family MEI Controller #1 (rev 04)
    00:19.0 Ethernet controller: Intel Corporation Ethernet Connection I217-V (rev 05)
    00:1b.0 Audio device: Intel Corporation 8 Series/C220 Series Chipset High Definition Audio Controller (rev 05)
    00:1c.0 PCI bridge: Intel Corporation 8 Series/C220 Series Chipset Family PCI Express Root Port #1 (rev d5)
    00:1c.1 PCI bridge: Intel Corporation 8 Series/C220 Series Chipset Family PCI Express Root Port #2 (rev d5)
    00:1c.4 PCI bridge: Intel Corporation 8 Series/C220 Series Chipset Family PCI Express Root Port #5 (rev d5)
    00:1f.0 ISA bridge: Intel Corporation HM86 Express LPC Controller (rev 05)
    00:1f.2 SATA controller: Intel Corporation 8 Series/C220 Series Chipset Family 6-port SATA Controller 1 [AHCI mode] (rev 05)
    00:1f.3 SMBus: Intel Corporation 8 Series/C220 Series Chipset Family SMBus Controller (rev 05)
    02:00.0 Network controller: Intel Corporation Wireless 7260 (rev 6b)
    03:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS5227 PCI Express Card Reader (rev 01)

## [Troubleshooting]

** Note**\
Keep in mind that issues below could be limited to a specific unit of Lenovo Thinkpad L540 as well as depends on BIOS version that has been used. Findings based on \"20AUA1FFPB (LENOVO_MT_20AU_BU_Think_FM_ThinkPad L540)\"

### [][Unable to shutdown/reboot, irq N:nobody cared (try booting with the \"irqpoll\" option), system turns dead after resume from hibernation.]

It seems that with kernel **\<4.0** you may have issues halting the system, which will result in hang after message about powering off. With kernel **=4.0** you may have no longer such issue but after you resume from hibernation, USB ports may not work at all as well as you may start seeing the message about irq that nobody cared. With kernel **=4.1** systems after resume from hibernation turns dead. The apps are semi-responsible but no new process can be spawned, like storage was offline. Booting with \`**irqpoll**\` does make the system works as it should.

As of kernel 4.2.0-rc1 the issues with IRQ are no more.

### [Brightness control does not work]

Depends on kernel version, you may need to boot with either **acpi_osi=Linux** or with empty string **acpi_osi=**

### [After resuming from hibernation system either ends up with black screen or crash shortly after resuming]

Randomly, but often, after resuming from on-disk hibernation the system may hang with black screen or resume, but crash shortly after (multiple segfaults, later resulting in whole system freeze after several seconds)

Multiple sources reports that there\'s a bug in a whole range of Lenovo laptops, including but not limiting to X1 Carbon, E540, L540 and others, the bug affect USB 3.0 port and after disabling USB 3.0 in bios (system uses all ports as usb 2.0 after than) there\'s no longer issue with resume. In case of this very L540 that wasn\'t enough. Solution was to disable XHCI (usb 3.0) driver in kernel as well as disabling PREEMPT in the kernel and reducing timer frequency to 100 Hz, by changing the symbols:

`root `[`#`]`./scripts/diffconfig .config-broken .config`

    -USB_XHCI_PCI y
     HZ 250 -> 100
     HZ_100 n -> y
     HZ_250 y -> n
     PREEMPT_NONE n -> y
     PREEMPT_VOLUNTARY y -> n
     USB_XHCI_HCD y -> n

This is hardly considered as fix, but rather a workaround that does not trigger the bug.

### [][Wrong order of ALSA cards (First HDMI, then PCH]

For some reason the card0 is not the PCH card. This can be changed with index option of snd-hda-intel module.

One can create /etc/modprobe.d/alsa-reorder.conf with

    options snd_hda_intel index=1,0

To reorder the PCH as first card.

### [Random system hangs with possible screen artifacts]

Since update to BIOS version J4ET76WW (1.76) random hard-freezes have been experienced. The screen usually is torn apart. Update to BIOS version 1.78 solve the issue. All version from 1.74 to 1.76 are no longer available on the Lenovo page. 1.77 was never public and 1.78 changelog lists only changes from 1.77 to 1.78.