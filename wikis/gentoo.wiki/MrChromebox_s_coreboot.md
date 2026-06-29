[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=MrChromebox%27s_coreboot&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://mrchromebox.tech)

[[]][MrChromebox\'s coreboot](https://github.com/MrChromebox/coreboot)

[[]][Fimware Utility Script](https://github.com/MrChromebox/scripts)

[[]][Issue tracker (script-related)](https://github.com/MrChromebox/scripts/issues)

[[]][Issue tracker (non-script-related firmware issues)](https://github.com/MrChromebox/firmware/issues)

The **MrChromebox\'s coreboot** is a [coreboot](https://wiki.gentoo.org/wiki/Coreboot "Coreboot") fork maintained by one of the coreboot leaders ^[\[1\]](#cite_note-1)^, Matt DeVillier (MrChromebox) ^[\[2\]](#cite_note-2)^. The fork targets Chrome OS devices based on x86 architecture. ARM is not supported ^[\[3\]](#cite_note-3)^.

## Contents

-   [[1] [Firmware Utility Script]](#Firmware_Utility_Script)
-   [[2] [Manual installation]](#Manual_installation)
    -   [[2.1] [Device list]](#Device_list)
    -   [[2.2] [Linux Mint environment]](#Linux_Mint_environment)
    -   [[2.3] [Compilation]](#Compilation)
    -   [[2.4] [VPD injection]](#VPD_injection)
        -   [[2.4.1] [BIOS region extraction]](#BIOS_region_extraction)
            -   [[2.4.1.1] [Intel-based device]](#Intel-based_device)
            -   [[2.4.1.2] [Non-Intel-based device]](#Non-Intel-based_device)
        -   [[2.4.2] [VPD extraction and injection]](#VPD_extraction_and_injection)
    -   [[2.5] [Flashing the firmware]](#Flashing_the_firmware)
        -   [[2.5.1] [Intel-based device]](#Intel-based_device_2)
        -   [[2.5.2] [Non-Intel-based device]](#Non-Intel-based_device_2)
    -   [[2.6] [Customization]](#Customization)
        -   [[2.6.1] [Custom BIOS name]](#Custom_BIOS_name)
        -   [[2.6.2] [Decreasing the boot timeout]](#Decreasing_the_boot_timeout)
        -   [[2.6.3] [Larry the Cow as the splash screen image]](#Larry_the_Cow_as_the_splash_screen_image)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)
-   [[5] [References]](#References)

## [Firmware Utility Script]

** Warning**\
Even though the scripts are stored on GitHub, the blob files will be downloaded from the [MrChromebox\'s website](https://mrchromebox.tech) ^[\[4\]](#cite_note-4)^. In the case of firmware blobs, only md5 and sha1 checksum verification is implemented, but the checksums are also stored on the website, which breaks all security. ^[\[5\]](#cite_note-5)^ ^[\[6\]](#cite_note-6)^ ^[\[7\]](#cite_note-7)^ In addition, the script downloads binary tools from the website without any verification and runs them as **root**. ^[\[8\]](#cite_note-8)^ ^[\[9\]](#cite_note-9)^ ^[\[10\]](#cite_note-10)^ Therefore, there is **no way to know** if the blobs or tools have been **compomised**.

MrChromebox provides a script that automatically detects the motherboard, downloads the compiled coreboot as a blob, injects the [VPD](https://en.wikipedia.org/wiki/Vital_Product_Data "wikipedia:Vital Product Data") into that blob, disables write protection, and flashes it to the device. The script can be executed as follows:

`user `[`$`]`git clone `[`https://github.com/MrChromebox/scripts`](https://github.com/MrChromebox/scripts)

`user `[`$`]`cd scripts`

`root `[`#`]`./firmware-util.sh`

The current state of the script running on various live images:

  ---------------------------------------- ------------------ ------------ --------- --------------------------------------
  Distribution                             Version            Date         Status    Notes
  Gentoo LiveGUI USB Image                 20240707T170407Z   2024-07-14   Borked    The kernel is not permissive enough.
  Linux Mint Cinnamon Edition Live Image   21.3               2024-07-14   Works     Works out of the box.
  Ubuntu Desktop Live Image                24.04 LTS          2024-07-14   Works     Requires curl to be installed.
  ---------------------------------------- ------------------ ------------ --------- --------------------------------------

## [Manual installation]

### [Device list]

This is a list of Chrome OS devices on which manual installation has been successfully performed. Feel free to add to the list!

  -------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------- ------------------ ----------------------------------------------------------------------------------------------------------------------------------------- -------- -------
  Device                                                                                                                                                         Motherboard   coreboot version   Owner(s)                                                                                                                                  Status   Notes
  [Lenovo IdeaPad Flex 5 13IML05 Chromebook](https://wiki.gentoo.org/wiki/Lenovo_IdeaPad_Flex_5_13IML05_Chromebook "Lenovo IdeaPad Flex 5 13IML05 Chromebook")   akemi         2405.0             [Lars Hint ](https://wiki.gentoo.org/index.php?title=User:Lars_Hint&action=edit&redlink=1 "User:Lars Hint (page does not exist)")   Works
  -------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------- ------------------ ----------------------------------------------------------------------------------------------------------------------------------------- -------- -------

### [Linux Mint environment]

** Warning**\
EFI users should be aware that if Linux Mint is installed on an external disk, the EFI partition type code of the internal disk must be changed from EF00 to another partition type (e.g. 8300), otherwise the installer will screw up the partition instead of creating a new one on the external disk.

** Important**\
After writing a live Linux Mint image to a USB drive, the following error will occur when booting to the drive and the process will hang:

    stdin: Invalid argument

This happens because Linux Mint checks if the GPT at the beginning of the disk matches the GPT at the end, which does not exist. After checking, Linux Mint writes GPT at the end and hangs. To fix the problem, just do a hard reset and it will work on the next boot.

To achieve a more reproducible environment, the compilation will be performed from a [Linux Mint](https://linuxmint.com) system (version 21.3).

Install crossgcc dev-dependencies:

`root `[`#`]`apt-get install git g++ zlib1g-dev gnat`

Install coreboot dev-dependencies:

`root `[`#`]`apt-get install libssl-dev uuid-dev nasm imagemagick`

Install menuconfig dev-dependencies:

`root `[`#`]`apt-get install libncurses-dev`

Install flashrom dev-dependencies:

`root `[`#`]`apt-get install meson libpci-dev`

Create a symlink to python:

`root `[`#`]`ln -s /usr/bin/python3 /usr/bin/python`

### [Compilation]

Clone the repository:

`user `[`$`]`git clone --recurse-submodules `[`https://github.com/MrChromebox/coreboot`](https://github.com/MrChromebox/coreboot)

`user `[`$`]`cd coreboot`

Select a version (all versions can be seen by executing `git branch --all`):

`user `[`$`]`git checkout remotes/origin/MrChromebox-2405`

Compile the cross-compiler:

`user `[`$`]`make crossgcc-i386 CPUS=$(nproc)`

Detect the name of the motherboard:

`root `[`#`]`dmidecode --string system-product-name`

Starting with version 4.22.0, there is a script in the repository to simplify the build ^[\[11\]](#cite_note-11)^:

`user `[`$`]`./build-uefi.sh <MOTHERBOARD_NAME_IN_LOWER_CASE>`

To see the compiled binary file, run the command:

`user `[`$`]`ls ../roms/*.rom`

** Important**\
The binary is not yet ready for flashing as it requires [VPD](https://en.wikipedia.org/wiki/Vital_Product_Data "wikipedia:Vital Product Data") to be injected.

### [VPD injection]

#### [BIOS region extraction]

Compile the flashrom:

`user `[`$`]`git clone `[`https://github.com/flashrom/flashrom`](https://github.com/flashrom/flashrom)` `

`user `[`$`]`cd flashrom `

`user `[`$`]`git switch --detach v1.5.1 `

`user `[`$`]`meson setup builddir `

`user `[`$`]`meson compile -C builddir `

`user `[`$`]`cd builddir`

Extract the BIOS region into a file:

##### [Intel-based device]

`root `[`#`]`./flashrom -p internal --ifd -i bios -r /tmp/bios.bin`

##### [Non-Intel-based device]

`root `[`#`]`./flashrom -p internal -r /tmp/bios.bin`

#### [VPD extraction and injection]

Compile the cbfstool:

`user `[`$`]`git clone `[`https://github.com/coreboot/coreboot`](https://github.com/coreboot/coreboot)` `

`user `[`$`]`cd coreboot `

`user `[`$`]`git switch --detach 24.05 `

`user `[`$`]`make -C util/cbfstool`

** Note**\
Cloning the original coreboot repository is optional, as cbfstool is also present in the MrChromebox\'s fork.

Extract the VPD from the BIOS region extracted earlier:

`user `[`$`]`./util/cbfstool/cbfstool /tmp/bios.bin read -r RO_VPD -f /tmp/vpd.bin`

Ensure that the VPD is present:

`user `[`$`]`hexdump -C /tmp/vpd.bin`

Inject the VPD into the firmware file:

`user `[`$`]`./util/cbfstool/cbfstool <FIRMWARE FILE PATH> write -r RO_VPD -f /tmp/vpd.bin`

### [Flashing the firmware]

** Warning**\
This step may result in hardware damage or data loss. Before proceeding, ensure that everything required for [unbricking](https://wiki.mrchromebox.tech/Unbricking) is in place.

** Note**\
\* flashrom can output some failure messages that can be safely ignored, so it is necessary to know the status code (the last echo command must be equal to zero).

-   After rebooting, the screen will be black for a minute.

#### [Intel-based device]

`root `[`#`]`./flashrom -p internal --ifd -i bios -N -w <FIRMWARE FILE PATH>`

`root `[`#`]`echo $?`

#### [Non-Intel-based device]

`root `[`#`]`./flashrom -p internal -N -w <FIRMWARE FILE PATH>`

`root `[`#`]`echo $?`

### [Customization]

** Note**\
It is highly recommended to perform the customization only after ensuring that everything works with the default values.

Find the location of the configuration file:

`user `[`$`]`find ./configs -name "config.<MOTHERBOARD_NAME_IN_LOWER_CASE>.uefi"`

Copy the configuration file to the root directory of the coreboot repository:

`user `[`$`]`cp <PATH_TO_CONFIGURATION_FILE> ./.config`

The configuration file has the same structure as the kernel configuration file and can be edited via menuconfig:

`user `[`$`]`make menuconfig`

After editing the configuration, the original configuration file needs to be replaced:

`user `[`$`]`make savedefconfig`

`user `[`$`]`mv ./defconfig <PATH_TO_CONFIGURATION_FILE>`

After replacement, it is necessary to (re)build the firmware by (re)running the [build-uefi.sh] script.

#### [Custom BIOS name]

The name is defined through `CONFIG_LOCALVERSION`, which can be changed in the [build-uefi.sh] file to, for example, this:

[CODE]

    echo "CONFIG_LOCALVERSION=\"coreboot-2405\"" >> .config

#### [Decreasing the boot timeout]

To decrease the menu prompt display time from two seconds to one second:

[KCONFIG]

    Payload  --->
      [ ] Don't add a payload
      (1)  Set the timeout for boot menu prompt Search for <code>CONFIG_EDK2_BOOT_TIMEOUT</code> to find this item.

#### [Larry the Cow as the splash screen image]

Download the image to the root directory of the repository:

`user `[`$`]`wget wiki.gentoo.org/images/3/3d/Larry_color.svg`

And set the path via menuconfig:

[KCONFIG]

    Payload  --->
      [ ] Don't add a payload
      (Larry_color.svg) edk2 Bootsplash path and filename Search for <code>CONFIG_EDK2_BOOTSPLASH_FILE</code> to find this item.

## [See also]

-   [Coreboot](https://wiki.gentoo.org/wiki/Coreboot "Coreboot") --- a free and opensource hardware initializing firmware which supports multiple boot ROM payloads.
-   [Chromebook](https://wiki.gentoo.org/wiki/Chromebook "Chromebook") --- installing Gentoo on a Chromebook

## [External resources]

-   [ArchLinux » Chrome OS devices/Custom firmware](https://wiki.archlinux.org/title/Chrome_OS_devices/Custom_firmware)

## [References]

1.  [[[↑](#cite_ref-1)] [[https://www.coreboot.org/leadership.html](https://www.coreboot.org/leadership.html)]]
2.  [[[↑](#cite_ref-2)] [[https://arstechnica.com/gadgets/2017/06/how-to-install-linux-on-a-chromebook/](https://arstechnica.com/gadgets/2017/06/how-to-install-linux-on-a-chromebook/)]]
3.  [[[↑](#cite_ref-3)] [[https://github.com/MrChromebox/scripts/issues/41#issuecomment-406382894](https://github.com/MrChromebox/scripts/issues/41#issuecomment-406382894)]]
4.  [[[↑](#cite_ref-4)] [[https://github.com/MrChromebox/scripts/blob/c5773cd93f6edaf0099340bcfecb40d08e3ee591/sources.sh](https://github.com/MrChromebox/scripts/blob/c5773cd93f6edaf0099340bcfecb40d08e3ee591/sources.sh)]]
5.  [[[↑](#cite_ref-5)] [[https://github.com/MrChromebox/scripts/blob/c5773cd93f6edaf0099340bcfecb40d08e3ee591/sources.sh#L12](https://github.com/MrChromebox/scripts/blob/c5773cd93f6edaf0099340bcfecb40d08e3ee591/sources.sh#L12)]]
6.  [[[↑](#cite_ref-6)] [[https://github.com/MrChromebox/scripts/blob/c5773cd93f6edaf0099340bcfecb40d08e3ee591/firmware.sh#L282](https://github.com/MrChromebox/scripts/blob/c5773cd93f6edaf0099340bcfecb40d08e3ee591/firmware.sh#L282)]]
7.  [[[↑](#cite_ref-7)] [[https://github.com/MrChromebox/scripts/blob/c5773cd93f6edaf0099340bcfecb40d08e3ee591/firmware.sh#L97](https://github.com/MrChromebox/scripts/blob/c5773cd93f6edaf0099340bcfecb40d08e3ee591/firmware.sh#L97)]]
8.  [[[↑](#cite_ref-8)] [[https://github.com/MrChromebox/scripts/blob/c5773cd93f6edaf0099340bcfecb40d08e3ee591/sources.sh#L9](https://github.com/MrChromebox/scripts/blob/c5773cd93f6edaf0099340bcfecb40d08e3ee591/sources.sh#L9)]]
9.  [[[↑](#cite_ref-9)] [[https://github.com/MrChromebox/scripts/blob/c5773cd93f6edaf0099340bcfecb40d08e3ee591/functions.sh#L256](https://github.com/MrChromebox/scripts/blob/c5773cd93f6edaf0099340bcfecb40d08e3ee591/functions.sh#L256)]]
10. [[[↑](#cite_ref-10)] [[https://github.com/MrChromebox/scripts/blob/c5773cd93f6edaf0099340bcfecb40d08e3ee591/firmware.sh#L433](https://github.com/MrChromebox/scripts/blob/c5773cd93f6edaf0099340bcfecb40d08e3ee591/firmware.sh#L433)]]
11. [[[↑](#cite_ref-11)] [[https://github.com/MrChromebox/coreboot/commit/209b167567818df791161a69228cf838624beeb5](https://github.com/MrChromebox/coreboot/commit/209b167567818df791161a69228cf838624beeb5)]]