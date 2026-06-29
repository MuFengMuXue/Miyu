\

**Resources**

[[]][Home](http://www.coreboot.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/coreboot "wikipedia:coreboot")

[[]][GitWeb](http://review.coreboot.org/#/q/status:open)

[[]][r/coreboot](https://reddit.com/r/coreboot)

[[]][[#coreboot](ircs://irc.libera.chat/#coreboot)] ([[webchat](https://web.libera.chat/#coreboot)])

**coreboot** is a free and opensource hardware initializing firmware which supports multiple boot ROM payloads. Supported boot ROM payloads range from [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI"), [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS") (via the open source [SeaBIOS](https://wiki.gentoo.org/index.php?title=SeaBIOS&action=edit&redlink=1 "SeaBIOS (page does not exist)")^[\[1\]](#cite_note-1)^), [Open Firmware](https://wiki.gentoo.org/wiki/Open_Firmware "Open Firmware"), to [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB") for running a Linux kernel at boot-time. This guide will show how to install coreboot with a SeaBIOS payload on supported devices, handling of userspace tools and the use of flashrom.

## Contents

-   [[1] [Supported hardware]](#Supported_hardware)
-   [[2] [The basics]](#The_basics)
    -   [[2.1] [Flasher]](#Flasher)
    -   [[2.2] [SPI flash]](#SPI_flash)
    -   [[2.3] [flashrom]](#flashrom)
-   [[3] [Dumping and compiling tools]](#Dumping_and_compiling_tools)
    -   [[3.1] [Intel ME and Gigabit Ethernet configuration data]](#Intel_ME_and_Gigabit_Ethernet_configuration_data)
-   [[4] [Configuring and compiling coreboot]](#Configuring_and_compiling_coreboot)
    -   [[4.1] [General setup]](#General_setup)
    -   [[4.2] [Mainboard]](#Mainboard)
    -   [[4.3] [Chipset]](#Chipset)
    -   [[4.4] [Devices]](#Devices)
    -   [[4.5] [Generic drivers]](#Generic_drivers)
    -   [[4.6] [Security]](#Security)
    -   [[4.7] [Console]](#Console)
    -   [[4.8] [System tables]](#System_tables)
    -   [[4.9] [Payloads]](#Payloads)
    -   [[4.10] [Debugging]](#Debugging)
    -   [[4.11] [Compiling]](#Compiling)
-   [[5] [Flashing coreboot.rom]](#Flashing_coreboot.rom)
    -   [[5.1] [Flashing via internal]](#Flashing_via_internal)
-   [[6] [Troubleshooting]](#Troubleshooting)
    -   [[6.1] [coreboot isn\'t booting (Broken build)]](#coreboot_isn.27t_booting_.28Broken_build.29)
    -   [[6.2] [Nothing is booting anymore (aka SPI chip bricked)]](#Nothing_is_booting_anymore_.28aka_SPI_chip_bricked.29)
-   [[7] [Porting a new board]](#Porting_a_new_board)
-   [[8] [Platform lockdown and device ownership]](#Platform_lockdown_and_device_ownership)
    -   [[8.1] [Intel Boot Guard]](#Intel_Boot_Guard)
    -   [[8.2] [Understanding the impact of UEFI, SecureBoot and BootGuard]](#Understanding_the_impact_of_UEFI.2C_SecureBoot_and_BootGuard)
-   [[9] [See Also]](#See_Also)
-   [[10] [External Resources]](#External_Resources)
    -   [[10.1] [coreboot Distributions]](#coreboot_Distributions)
        -   [[10.1.1] [Libreboot]](#Libreboot)
-   [[11] [References]](#References)

## [Supported hardware]

There are different types of architectures and supported hardware. The fully up-to-date table is available at the following [link](http://www.coreboot.org/Supported_Motherboards). In the table below are some well supported devices which are more or less recently released. If an older device is being used, it may be possible to remove all proprietary binary blobs. For this, use the [libreboot](https://libreboot.org/) guide.

  ----------------------- ------------------- ----------- ----------------- ---------------------- ------------------------ ------------------------ --------------------
  Hardware                Supported           Blob Free   Native RAM Init   Native Graphics Init   Flashable via Hardware   Flashable via Software   Desoldering needed
  Lenovo Thinkpad T530    Currently broken    No          Yes               Partial                Yes                      not with OEM BIOS        Yes
  Lenovo Thinkpad T480    WIP(?)              No          Yes               Partial                Yes                      not with OEM BIOS        No
  Lenovo Thinkpad T430s   Currently broken    No          Yes               Partial                Yes                      not with OEM BIOS        Yes
  Lenovo Thinkpad X230    Yes                 No          Yes               Partial                Yes                      not with OEM BIOS        No
  Lenovo Thinkpad T420s   Yes                 No          Yes               Partial                Yes                      not with OEM BIOS        No
  Lenovo Thinkpad T420    WIP                 No          Yes               Partial                Yes                      not with OEM BIOS        No
  Lenovo Thinkpad T520    Yes                 No          Yes               Partial                Yes                      not with OEM BIOS        No
  Lenovo Thinkpad X220    Yes                 No          Yes               Partial                Yes                      not with OEM BIOS        No
  Lenovo Thinkpad X220    Yes                 No          Yes               Partial                Yes                      not with OEM BIOS        No
  Lenovo Thinkpad T410    WIP                 No          Yes               Partial                Yes                      not with OEM BIOS        No
  Lenovo Thinkpad T510    WIP                 No          Yes               Partial                Yes                      not with OEM BIOS        No
  Lenovo Thinkpad X201    Currently broken    No          Yes               Partial                Yes                      not with OEM BIOS        No
  Apple Macbook Air 4,2   Yes                 No          Yes               No                     Yes                      not with OEM BIOS        No
  ----------------------- ------------------- ----------- ----------------- ---------------------- ------------------------ ------------------------ --------------------

## [The basics]

In general, the flash chip must be found on the board of the selected hardware. This is important, as the vendor usually locks the flash chip via soft lockdown. Guides for locating the chip will generally be on the coreboot wiki. This guide assumes the device contains an SPI flash chip, which requires a clip to connect up to the flasher.

### [Flasher]

As a flasher, a Raspberry Pi can easily be used. Any model and revision will do, but be warned that the earlier ones do not have enough RAM to compile coreboot by themselves. If using one of these, make sure to copy the dump of the flash chip onto a more powerful computer. If the flash chip is SPI based, make sure to get a [Pomona SOIC-8 testclip](http://www.mouser.de/ProductDetail/Pomona-Electronics/5250/?qs=q2OAyjihNMzqkARxZuX5AQ%3D%3D) for £15. But there also many other [programmers](http://flashrom.org/Supported_programmers). Make sure to get some debug wires, too.

### [SPI flash]

There are different types of SPI chips ([list](http://flashrom.org/Supported_hardware)). The most common package for these chips is SOIC-8 which can be flashed via testclip. Sometimes these chips are in a WSON-8 package; in which case the WSON-8 chip needs to be desoldered, and resoldered with a new SOIC-8. If you need help with soldering ask [hackerspaces](https://wiki.hackerspaces.org/List_of_Hacker_Spaces) near your location. SPI chips are common in sizes from 2MB - 16MB. Often vendors solder two chips to save money.

### [flashrom]

### [USE flags for] [sys-apps/flashrom](https://packages.gentoo.org/packages/sys-apps/flashrom) [[]] [Utility for reading, writing, erasing and verifying flash ROM chips]

  ----------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+asm106x`](https://packages.gentoo.org/useflags/+asm106x)                         Enable programmer for ASMedia SATA controllers
  [`+atavia`](https://packages.gentoo.org/useflags/+atavia)                           Support for VIA VT6421A SATA controllers
  [`+buspirate-spi`](https://packages.gentoo.org/useflags/+buspirate-spi)             Enable Bus Pirate SPI programmer
  [`+ch341a-spi`](https://packages.gentoo.org/useflags/+ch341a-spi)                   Enable WCH CH341A SPI programmer
  [`+ch347-spi`](https://packages.gentoo.org/useflags/+ch347-spi)                     Enable WCH CH347 SPI programmer
  [`+dediprog`](https://packages.gentoo.org/useflags/+dediprog)                       Dediprog SF100 support
  [`+developerbox-spi`](https://packages.gentoo.org/useflags/+developerbox-spi)       Enable Devloperbox SPI recovery support
  [`+digilent-spi`](https://packages.gentoo.org/useflags/+digilent-spi)               Enable support for Digilent iCEblink40 development board
  [`+dirtyjtag-spi`](https://packages.gentoo.org/useflags/+dirtyjtag-spi)             Support for DirtyJTAG (a USB-JTAG firmware for STM32 MCUs)
  [`+drkaiser`](https://packages.gentoo.org/useflags/+drkaiser)                       Enable Dr. Kaiser programmer
  [`+dummy`](https://packages.gentoo.org/useflags/+dummy)                             Enable dummy tracing
  [`+ft2232-spi`](https://packages.gentoo.org/useflags/+ft2232-spi)                   Enable ftdi programmer, flashing through FTDI/SPI USB interface
  [`+gfxnvidia`](https://packages.gentoo.org/useflags/+gfxnvidia)                     Enable NVIDIA programmer
  [`+internal`](https://packages.gentoo.org/useflags/+internal)                       Enable internal/onboard support
  [`+internal-dmi`](https://packages.gentoo.org/useflags/+internal-dmi)               Enable internal DMI decoding rather than use sys-apps/dmidecode
  [`+it8212`](https://packages.gentoo.org/useflags/+it8212)                           Support for ITE IT8212F ATA/RAID controllers
  [`+jlink-spi`](https://packages.gentoo.org/useflags/+jlink-spi)                     Support for SEGGER J-Link and compatible devices
  [`+linux-mtd`](https://packages.gentoo.org/useflags/+linux-mtd)                     Enable support for Linux mtd SPI flash devices
  [`+linux-spi`](https://packages.gentoo.org/useflags/+linux-spi)                     Enable support for Linux userspace spidev interface
  [`+nic3com`](https://packages.gentoo.org/useflags/+nic3com)                         Enable 3Com NIC programmer
  [`+nicintel`](https://packages.gentoo.org/useflags/+nicintel)                       Support for Intel NICs
  [`+nicintel-eeprom`](https://packages.gentoo.org/useflags/+nicintel-eeprom)         Support for EEPROMs on Intel Gigabit network cards
  [`+nicintel-spi`](https://packages.gentoo.org/useflags/+nicintel-spi)               Support for SPI on Intel NICs
  [`+nicrealtek`](https://packages.gentoo.org/useflags/+nicrealtek)                   Support for Realtek NICs
  [`+nv-sma-spi`](https://packages.gentoo.org/useflags/+nv-sma-spi)                   Support for NVIDIA System Management Agent
  [`+ogp-spi`](https://packages.gentoo.org/useflags/+ogp-spi)                         Enable support for OGP (Open Graphics Project) SPI flashing
  [`+pickit2-spi`](https://packages.gentoo.org/useflags/+pickit2-spi)                 Support for SPI flash ROMs accessible via Microchip PICkit2
  [`+pony-spi`](https://packages.gentoo.org/useflags/+pony-spi)                       Enable support for SI-Prog like hardware by Lancos
  [`+raiden-debug-spi`](https://packages.gentoo.org/useflags/+raiden-debug-spi)       Support for Chrome EC based debug tools - SuzyQable, Servo V4, C2D2 & uServo
  [`+rayer-spi`](https://packages.gentoo.org/useflags/+rayer-spi)                     RayeR SPIPGM hardware support
  [`+satamv`](https://packages.gentoo.org/useflags/+satamv)                           Enable programmer for Marvell SATA controllers
  [`+satasii`](https://packages.gentoo.org/useflags/+satasii)                         Enable programmer for SiI SATA controllers
  [`+serprog`](https://packages.gentoo.org/useflags/+serprog)                         Enable Serial Flasher programmer
  [`+spidriver`](https://packages.gentoo.org/useflags/+spidriver)                     Enable programmer for Excamera Labs SPIDriver
  [`+stlinkv3-spi`](https://packages.gentoo.org/useflags/+stlinkv3-spi)               Enable SPI programmer using STLINK-V3
  [`+usbblaster-spi`](https://packages.gentoo.org/useflags/+usbblaster-spi)           Enable support for Altera USB-Blaster dongles
  [`atahpt`](https://packages.gentoo.org/useflags/atahpt)                             Highpoint (HPT) ATA/RAID controller support
  [`atapromise`](https://packages.gentoo.org/useflags/atapromise)                     Support for Promise PDC2026x (FastTrak/Ultra)
  [`mediatek-i2c-spi`](https://packages.gentoo.org/useflags/mediatek-i2c-spi)         Support for Mediatek LCD controllers
  [`mstarddc-spi`](https://packages.gentoo.org/useflags/mstarddc-spi)                 Support for SPI flash ROMs accessible through DDC in MSTAR-equipped displays
  [`nicnatsemi`](https://packages.gentoo.org/useflags/nicnatsemi)                     Support for National Semiconductor NICs
  [`parade-lspcon`](https://packages.gentoo.org/useflags/parade-lspcon)               Enable support for Parade lspcon USB-C to HDMI protocol translator
  [`realtek-mst-i2c-spi`](https://packages.gentoo.org/useflags/realtek-mst-i2c-spi)   Enable support for Realtek RTD2142 MST
  [`test`](https://packages.gentoo.org/useflags/test)                                 Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`tools`](https://packages.gentoo.org/useflags/tools)                               Install ich_descriptor_tool, a tool for reading descriptor-mode SPI-flash images for Intel chipsets
  ----------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-23 18:15] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

[flashrom](https://flashrom.org) is most commonly used to dump and write to flash chips. This must be installed on the flasher, or on the machine that the flasher is connected to.

It is useful to install flashrom on the system that will be flashed to, as once coreboot is flashed initially, it can be reflashed internally, without disassembly or use of a flasher.

`root `[`#`]`emerge --ask sys-apps/flashrom`

Now, the machine needs to be disassembled. Follow the manual, or an online guide until the flash chip is accessible, and then attach the clip and wire it to the flasher.

** Warning**\
Make sure ALL power sources are disconnected from the machine, apart from the CMOS battery. It\'s possible to fry motherboards if they are connected while being flashed to.

Once the flash chip is connected to a flasher, use flashrom to dump the flash chip\'s contents.

`root `[`#`]`flashrom -p linux_spi:dev=/dev/spidev0.0 -r flash.bin`

`root `[`#`]`flashrom -p linux_spi:dev=/dev/spidev0.0 -r flash2.bin`

`root `[`#`]`diff flash.bin flash2.bin`

It\'s important to take multiple dumps, in case there is a connection error. Once a proper dump is obtained, it is safe to disconnect the flasher for now if so desired. Remember, if running on a Raspberry Pi v1, it will not have enough RAM to compile, so at this point the dump should be transferred to a different machine. It\'s possible to use the computer that the flash chip was dumped from, although this will require reassembly and another disassembly later.

## [Dumping and compiling tools]

Now, the coreboot git repository needs to be cloned to a working directory, as it contains tools required to carry on. Directories must also be created for the specific manufacturer and model.

`user `[`$`]`git clone --recursive `[`https://review.coreboot.org/coreboot.git`](https://review.coreboot.org/coreboot.git)

`user `[`$`]`cd coreboot`

`user `[`$`]`mkdir -p 3rdparty/blobs/mainboard/<manufacturer>/<model>`

Replace \<manufacturer\> and \<model\> with your manufacturer and model respectively (e.g. lenovo/x220).

The next step is to extract regions of the flash dump. Regions are similar to partitions, and are a flash chip contains a flash descriptor that can be seen as a partition table for the SPI flash with some additional properties. This descriptor is read by a program called ifdtool, which will be used to gain the individual partitions.

First, ifdtool must be compiled. Its source is contained under coreboot\'s, so cd into the directory where coreboot was cloned to.

`user `[`$`]`cd util/ifdtool`

`user `[`$`]`make`

It\'s a good idea to install globally, but not necessary.

`root `[`#`]`make install`

Then, cd back to wherever flash.bin is.

`user `[`$`]`ifdtool -x flash.bin`

This will print a partition table, and extract some blobs. A standard partition table may look like this:

  -------- ------------------ -------------- ------------
  Region   Description        Start region   End region
  0        Flash descriptor   0x00000000     0x00000fff
  1        BIOS (Firmware)    0x00500000     0x00bfffff
  2        ME                 0x00003000     0x004fffff
  3        GbE                0x00001000     0x00002fff
  4        Platform Data      unused         unused
  -------- ------------------ -------------- ------------

#### [Intel ME and Gigabit Ethernet configuration data]

Notice how the above table contains ME and GbE. These are binary blobs that initialize parts of the computer (In this case, Intel Management Engine and Gigabit Ethernet). On older devices, these can be safely removed with [libreboot](https://libreboot.org), but on Sandy Bridge and newer, they are required for the computer to run properly. Since Intel ME is required on these boards, it must be extracted. However, coreboot can drastically reduce the size of it, removing its network and system resource access. This is recommended, as not only does it improve security, it also leaves more space on the flash chip for other payloads. The Gigabit Ethernet configuration data is specific to each machine, and as such, must also be extracted from the flash chip.

At this point, the working directory should contain four new files, which follow the format flashregion\_\*.bin. These should map to the table that was printed. As previously mentioned, the descriptor, Intel ME and the GbE blobs are needed. Rename these to descriptor.bin, me.bin and gbe.bin respectively, and copy them to coreboot/3rdparty/blobs/mainboard/\<manufacturer\>/\<model\>/; the directory that was created earlier.

## [Configuring and compiling coreboot]

Now, coreboot must be configured for the specific machine. It\'s best to check the coreboot wiki page for the given device, in case there are any certain requirements. As such, this page will attempt to only detail the settings which must be set across the majority of installs. This cannot be guaranteed, and some settings may cause conflicts with the machine.

First, the configuration must be entered. This is performed in a similar manner to configuring a kernel:

`user `[`$`]`make nconfig`

Alternatively, one could use menuconfig, or even edit the config file manually (once it has been generated by nconfig/menuconfig).

#### [General setup]

Following values are recommended:

-   Use CMOS for configuration values.
-   Compress ramstage with LZMA
-   Include the coreboot .config file into the ROM image
-   Create a table of timestamps collected during boot
-   Build the ramstage to be relocatable in 32-bit address space.

For a Sandy Bridge or later device:

-   Allow use of binary-only repository

And if you\'ve previously compiled coreboot, you can reduce further compile times by enabling:

-   Update existing coreboot.rom image

#### [Mainboard]

Here, the vendor and model must be selected. Make sure the exact model is entered, if derivatives are available (e.g X220/X220t). The ROM chip size should also be selected. This should have been outputted by flashrom, but if not can be determined by checking the filesize of flash.bin.

#### [Chipset]

This menu contains chipset specific options, and also the locations for the binary blobs extracted earlier. since this is largely machine specific, there are only certain options that should be enabled across the board. I recommend enabling:

-   Enable VMX for virtualization
-   Set lock bit after configuring VMX
-   Beep on fatal error
-   Flash LEDs on fatal error

These will allow easier debugging if you have a bad flash. They can be disabled once a known working configuration is created.

Next, paths must be provided under Intel Firmware. Enable these options:

-   Add Intel descriptor.bin file
-   Add Intel ME/TXE firmware
-   Strip down the Intel ME/TXE firmware
-   Add gigabit ethernet firmware

Options for paths should now appear. They should match to the names used previously, but if not, correct them so that they do.

#### [Devices]

This area largely concerns graphics, especially in the context of laptops. Personally, I have Graphics Initialisation set to \'Use native graphics init\', and Display/Framebuffer Mode set to \'Linear \"high-resolution\" framebuffer\'. The rest of these options should be set already for the machine. If the specific device requires a VGA BIOS image, follow the coreboot wiki.

#### [Generic drivers]

I often enable:

-   PS/2 keyboard init

If the device has an Intel PCIe WiFi card, enable the option

-   Support Intel PCI-e WiFi adapters

#### [Security]

I often leave this alone, as it currently only contains Verified Boot options, but if support for this is required, enable it.

#### [Console]

This section contains options about debugging consoles. It may be useful to enable certain options, especially if issues are occuring. I have enabled:

-   Squelch AP CPUs from early console.
-   Send console output to a CBMEM buffer
-   Show POST codes on the debug console

#### [System tables]

Enable Generate SMBIOS tables, the only option here.

#### [Payloads]

In this section, the payload can be chosen. This page will detail how to set up SeaBIOS, as it has the largest compatibility with operating systems, but it is also possible to use [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB") for faster booting, or even place a kernel on the flash chip (if there is enough space).

Select the following for a proper SeaBIOS setup:

-   Add a payload \> SeaBIOS
-   SeaBIOS version \> master
-   Hardware init during option ROM execution
-   Use LZMA compression for payloads

One may also wish to enable some secondary payloads. These can be used for debugging, and changing options. A recommended option is nvramcui, which acts in a similar way to a standard BIOS options menu.

#### [Debugging]

These options are largely for development. Regular users need not enable anything in this submenu.

### [Compiling]

Now that the config is done, coreboot must be compiled. First, the cross-compiler must be built:

`user `[`$`]`make crossgcc-i386 CPUS=$(nproc)`

This requires [[[dev-lang/gnat-gpl]](https://packages.gentoo.org/packages/dev-lang/gnat-gpl)[]] to be installed, otherwise many functions will not work properly.

Once this is done, compile IASL:

`user `[`$`]`make iasl`

And finally, compile coreboot:

`user `[`$`]`make`

## [Flashing coreboot.rom]

This should produce a file in the build/ directory called coreboot.rom. This is the final image which needs to be flashed. Copy this to the flasher, if not already on it, disassemble the target device and attach the flasher to the flash chip.

On the flasher, use flashrom to flash:

`root `[`#`]`flashrom -p linux_spi:dev=/dev/spidev0.0 -w coreboot.rom`

`root `[`#`]`flashrom -p linux_spi:dev=/dev/spidev0.0 -v coreboot.rom`

The second command should return VERIFIED. If so, coreboot has been successfully flashed to the device.

### [Flashing via internal]

Once coreboot has been flashed initially, it can later be flashed internally, without need of an external flashing device. To do this, once a new coreboot.rom has been compiled, simply do the following:

`root `[`#`]`flashrom -p internal:laptop=force_I_want_a_brick -w coreboot.rom`

** Warning**\
While this has been tested on several laptops, it may not work on the device being used. Make sure to check if others have had success or failures with the internal flasher for the specific model.

## [Troubleshooting]

### [][coreboot isn\'t booting (Broken build)]

If coreboot is not booting, then it usually means that it either isn\'t configured properly, or is missing a payload. Ensure that a proper payload was selected that is compiled correctly, and properly configured itself.

It\'s also possible that coreboot is working correctly, but the graphical component isn\'t. This may be caused by using native gfx init. Try dumping a VGA BIOS and using that instead. It could also be the other way around; try switching from a VGA BIOS to native gfx init. As a final resort, try using the Legacy VGA text mode for the framebuffer mode under Devices/Display.

### [][Nothing is booting anymore (aka SPI chip bricked)]

This is usually caused by leaving the machine powered on while dumping or flashing with an external flasher. If the machine does not turn on at all (No lights, fans, or display turn on at boot), this may mean that the machine is bricked. It may be possible to repair by purchasing a new flash chip (Make sure it\'s compatible - try to use the same manufacturer and model for best results) and flashing this with either the original BIOS or the coreboot ROM. This often requires very delicate soldering, and is not for the feint of heart. It may mean that a new machine must be purchased, or at least a new motherboard.

** Note**\
Always be sure to check that the cause isn\'t a misconfigured coreboot!

## [Porting a new board]

## [Platform lockdown and device ownership]

### [Intel Boot Guard]

### [][Understanding the impact of UEFI, SecureBoot and BootGuard]

## [See Also]

-   [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS") --- the standard firmware of IBM-PC-compatible computers until it was phased out in 2020.
-   [Open Firmware](https://wiki.gentoo.org/wiki/Open_Firmware "Open Firmware") --- an [IEEE 1275-1994](https://ieeexplore.ieee.org/document/763383) standard for hardware independent firmware built on top of a [Forth](https://wiki.gentoo.org/wiki/Forth "Forth") machine.
-   [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") --- a firmware standard for boot ROM designed to provide a stable API for interacting with system hardware. On [x86](https://en.wikipedia.org/wiki/x86 "wikipedia:x86") it replaced the legacy [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS").
-   [MrChromebox\'s coreboot](https://wiki.gentoo.org/wiki/MrChromebox%27s_coreboot "MrChromebox's coreboot") --- a [coreboot] fork maintained by one of the coreboot leaders

## [External Resources]

### [coreboot Distributions]

-   [coreboot](https://www.coreboot.org/) --- the principle coreboot project upstream of all forks and derivatives.
-   [Heads](https://osresearch.net/) --- a hardened coreboot distribution with reproducible firmware images.
-   [Skulls](https://github.com/merge/skulls) --- a pre-built coreboot distribution for Lenovo Thinkpad laptops.
-   [Oreboot](https://github.com/oreboot/oreboot) --- a fork of coreboot rewritten in [Rust](https://wiki.gentoo.org/wiki/Rust "Rust").
-   [MrChromebox\'s coreboot](https://mrchromebox.tech) --- targets x86-based Chrome OS devices.

#### [Libreboot]

-   [Libreboot](https://libreboot.org/) --- a coreboot distribution with as few non-free binary blobs as possible with an automated build system and a reputation for stability.
-   [GNU Boot](https://savannah.gnu.org/projects/gnuboot) --- GNU\'s coreboot distribution downstream of Libreboot.
-   [Canoeboot](https://canoeboot.org/) --- a coreboot distribution downstream of Libreboot with a revamped build system.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://www.seabios.org/SeaBIOS](https://www.seabios.org/SeaBIOS)]]