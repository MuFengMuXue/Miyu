**Resources**

[[]][Home](https://www.asrock.com/mb/AMD/Fatal1ty%20X370%20Professional%20Gaming/index.asp)

The ASRock Fatal1ty X370 Professional Gaming motherboard is a moderate quality gaming motherboard for first generation Ryzen systems (socket AM4). It includes 10 SATA ports, PCI3 4x M.2 socket for NVMe solid state drives, a built in Wi-Fi controller, and two onboard NICs. Because of the emphesis on gaming, it includes two onboard RGB headers and a higher quality integrated sound card.

** Important**\
This motherboard uses the X370 chipset which may experience some soft freezes due to power states. See the [following remediation in the Ryzen article](https://wiki.gentoo.org/wiki/Ryzen#Soft_freezes_on_1st_gen_Ryzen_7 "Ryzen").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Motherboard firmware]](#Motherboard_firmware)
    -   [[1.2] [Kernel]](#Kernel)
-   [[2] [See also]](#See_also)

## [Installation]

### [Motherboard firmware]

When exclusively running a Linux based operating system, the motherboard firmware can be updated by using the \"Instant Flash\" feature. [Download the ROM firmware update](https://www.asrock.com/mb/AMD/Fatal1ty%20X370%20Professional%20Gaming/index.asp#BIOS) from the manufacturer\'s website, extract onto a [FAT32](https://wiki.gentoo.org/wiki/FAT "FAT") formatted USB flash memory device, then reboot the system. Firmware can be discovered and uploaded via the USB flash device from within the motherboard\'s graphical user interface.

### [Kernel]

Sensors for Ryzen:

    Driver `nct6775':
      * ISA bus, address 0x290
        Chip `Nuvoton NCT5532D/NCT6779D Super IO Sensors' (confidence: 9)

Which means `CONFIG_SENSORS_NCT6775` should be enabled in the kernel:

[KERNEL] **Enable `CONFIG_SENSORS_NCT6775` support**

    Device Drivers  --->
       -*- Hardware Monitoring support  --->
          <*>   Nuvoton NCT6775F and compatibles

## [See also]

-   [Ryzen](https://wiki.gentoo.org/wiki/Ryzen "Ryzen") --- a multithreaded, high performance processor manufactured by AMD.