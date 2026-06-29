**Resources**

[[]][Home](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-edge-laptops/thinkpad-edge-e540)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_E540/ThinkPad_E540_Spec.PDF)

[[]][Specifications (by region)](https://psref.lenovo.com/Product/ThinkPad/ThinkPad_E540)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/ibmdl/pub/pc/pccbbs/mobiles_pdf/e540_hmm_en_sp40a26433.pdf)

[[]][User Guide](https://download.lenovo.com/ibmdl/pub/pc/pccbbs/mobiles_pdf/e440_e540_ug_en.pdf)

[[]][BIOS Setup](https://download.lenovo.com/pccbbs/mobiles_pdf/lenovo_bios_setup_linux_wmi_sysfs_1.2.pdf)

[[]][ThinkPad E series](https://en.wikipedia.org/wiki/ThinkPad_E_series "wikipedia:ThinkPad E series")

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Firmware]](#Firmware)
    -   [[2.2] [Kernel]](#Kernel)
    -   [[2.3] [Emerge]](#Emerge)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [No resume possible (UEFI problem)]](#No_resume_possible_.28UEFI_problem.29)
    -   [[3.2] [No Wi-Fi after resume]](#No_Wi-Fi_after_resume)
    -   [[3.3] [Blinking power LED after resume]](#Blinking_power_LED_after_resume)
    -   [[3.4] [Hotkeys do not work after resume]](#Hotkeys_do_not_work_after_resume)

## [Hardware]

### [Standard]

  ----------------------- ------------------------------------------------------------------------- -------- ------------------------ ------------------ ---------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Device                  Make/model                                                                Status   Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  CPU                     N/A                                                                       Works    N/A                      N/A                N/A
  GPU                     Intel Corporation 4th Gen Core Processor Integrated Graphics Controller   Works    N/A                      N/A                N/A
  Wi-Fi                   Intel Corporation Wireless 7260                                           Works    N/A                      N/A                N/A
  Bluetooth               Intel Corporation Wireless 7260                                           Works    N/A                      N/A                N/A
  Trackpoint              N/A                                                                       Works    N/A                      N/A                N/A              Since the mouse buttons got integrated into the touchpad, it is awkward to use. To enable middle button scrolling use x11-drivers/xf86-input-[libinput](https://wiki.gentoo.org/wiki/Libinput "Libinput") (\>=0.8.0)
  LCD Backlight control   N/A                                                                       Works    N/A                      N/A                N/A
  Hotkeys                 N/A                                                                       Works    N/A                      N/A                N/A
  Webcam                  N/A                                                                       Works    N/A                      N/A                N/A
  ----------------------- ------------------------------------------------------------------------- -------- ------------------------ ------------------ ---------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`root `[`#`]`lspci`

    00:00.0 Host bridge: Intel Corporation Xeon E3-1200 v3/4th Gen Core Processor DRAM Controller (rev 06)
    00:02.0 VGA compatible controller: Intel Corporation 4th Gen Core Processor Integrated Graphics Controller (rev 06)
    00:03.0 Audio device: Intel Corporation Xeon E3-1200 v3/4th Gen Core Processor HD Audio Controller (rev 06)
    00:14.0 USB controller: Intel Corporation 8 Series/C220 Series Chipset Family USB xHCI (rev 04)
    00:16.0 Communication controller: Intel Corporation 8 Series/C220 Series Chipset Family MEI Controller #1 (rev 04)
    00:1a.0 USB controller: Intel Corporation 8 Series/C220 Series Chipset Family USB EHCI #2 (rev 04)
    00:1b.0 Audio device: Intel Corporation 8 Series/C220 Series Chipset High Definition Audio Controller (rev 04)
    00:1c.0 PCI bridge: Intel Corporation 8 Series/C220 Series Chipset Family PCI Express Root Port #1 (rev d4)
    00:1c.2 PCI bridge: Intel Corporation 8 Series/C220 Series Chipset Family PCI Express Root Port #3 (rev d4)
    00:1c.3 PCI bridge: Intel Corporation 8 Series/C220 Series Chipset Family PCI Express Root Port #4 (rev d4)
    00:1c.4 PCI bridge: Intel Corporation 8 Series/C220 Series Chipset Family PCI Express Root Port #5 (rev d4)
    00:1d.0 USB controller: Intel Corporation 8 Series/C220 Series Chipset Family USB EHCI #1 (rev 04)
    00:1f.0 ISA bridge: Intel Corporation HM87 Express LPC Controller (rev 04)
    00:1f.2 SATA controller: Intel Corporation 8 Series/C220 Series Chipset Family 6-port SATA Controller 1 [AHCI mode] (rev 04)
    00:1f.3 SMBus: Intel Corporation 8 Series/C220 Series Chipset Family SMBus Controller (rev 04)
    02:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS5227 PCI Express Card Reader (rev 01)
    03:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 10)
    04:00.0 Network controller: Intel Corporation Wireless 7260 (rev 73)

`root `[`#`]`lsusb`

    Bus 002 Device 002: ID 8087:8000 Intel Corp.
    Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 001 Device 002: ID 8087:8008 Intel Corp.
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 003 Device 003: ID 04f2:b398 Chicony Electronics Co., Ltd
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

## [Installation]

### [Firmware]

** Note**\
Make sure to activate the redistributable USE-flag and accept the appropriate licenses on the [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] package, otherwise it won\'t install the firmware files needed for this machine.

Wi-fi and Bluetooth firmware:

`root `[`#`]`emerge --ask sys-firmware/linux-firmware`

### [Kernel]

[KERNEL]

    Device drivers -->
      Graphics support -->
        Direct Rendering Manager -->
          <M> Intel 8xx/9xx/G3x/G4x/HD Graphics
            [*] Enable modesetting on intel by default
    Device drivers -->
      Misc devices -->
        <M> Realtek PCI-E card reader
      MMC/SD/SDIO card support -->
        <M> Realtek PCI-E SD/MMC Card Interface Driver
      <M> Multimedia support -->
        [*] Cameras/video grabbers support
        [*] Media USB Adapters -->
          <M> USB Video Class (UVC)
      Sound card support -->
        [*] Advanced Linux Sound Architecture -->
          PCI sound devices -->
            [*] Intel/SiS/nVidia/AMD/ALi AC97 Controller
          HD-Audio -->
            [*] HD Audio PCI
            [*] Build Realtek HD-audio codec support
            [*] Build Conexant HD-audio codec support
            [*] Build HDMI/DisplayPort HD-audio codec support
      [*] Watchdog Timer Support  -->
        <M>   Intel TCO Timer/Watchdog
          [*]     Intel TCO Timer/Watchdog Specific Vendor Support
      Character devices  -->
        [*]   Intel HW Random Number Generator support
      [*] X86 Platform Specific Device Drivers  --->
        <M>   ThinkPad ACPI Laptop Extras
          [*]     Console audio control ALSA interface
      -*- Hardware Monitoring support  --->
        <M>   Intel Core/Core2/Atom temperature sensor

### [Emerge]

If you are using [Xfce](https://wiki.gentoo.org/wiki/Xfce "Xfce"), you can install [[[xfce-extra/xfce4-kbdleds-plugin]](https://packages.gentoo.org/packages/xfce-extra/xfce4-kbdleds-plugin)[]] to see the status of your modifier keys (Caps-Lock, Num-Lock):

`root `[`#`]`emerge --ask xfce-extra/xfce4-kbdleds-plugin`

For [GNOME](https://wiki.gentoo.org/wiki/GNOME "GNOME") there is the \"Lock keys\" extension, which you can find on [https://extensions.gnome.org](https://extensions.gnome.org)

## [Troubleshooting]

### [][No resume possible (UEFI problem)]

** Note**\
New BIOS and software versions should fix this problem, so that the workaround below is no longer required. Update your Gentoo system and BIOS to the latest versions available.

When you open the lid or press a button to resume, the device will not resume. The fan seems to come on, but thats it. You have to hard reset (push the power button for about 5 seconds) to make it work again. To make resume work, you have to turn off \"USB 3 Mode\" in the UEFI settings (pushing Enter when the laptop starts). The drawback of this method is, of course, that your USB ports will only work in USB 2 mode, which means much slower data transfers.

See [this link](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1331077) for more information.

### [No Wi-Fi after resume]

** Note**\
New BIOS and software versions should fix this problem, so that the workaround below is no longer required. Update your Gentoo system and BIOS to the latest versions available.

When the device resumes from suspend, the Wifi will no longer work. This seems to be a problem with wpa_supplicant, because restarting it fixes it. On Ubuntu distributions, this problem does not occur, so they probably have a patch for it.

See [this link](https://bugs.launchpad.net/ubuntu/+source/gnome-nettool/+bug/1311257) for more information.

With this script in your \"/etc/pm/sleep.d\" folder, you can restart wpa_supplicant after suspend:

[CODE]

    #!/bin/sh

    if [ "$1" = "resume" ]
    then
        # If you're using NetworkManager, it will restart this service automatically.
        killall wpa_supplicant
        # Otherwise use this code (not tested):
        #rc-service wpa_supplicant restart
    fi

After saving the script file, you have to make it executable:

`root `[`#`]`chmod +x fix_wpa_supplicant.sh`

### [Blinking power LED after resume]

Sometimes, when the device resumes, the power LED will blink instead of stay lit. This can be fixed by resetting the power LED after suspend. To do this, you have to issue the following command as root:

`root `[`#`]`echo '0 on' > /proc/acpi/ibm/led`

See \"Documentation/laptops/thinkpad-acpi.txt\" in your kernel source directory for more information.

### [Hotkeys do not work after resume]

Update BIOS to the latest version.