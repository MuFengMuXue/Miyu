[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Ventoy&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.ventoy.net/en/)

[[]][Official documentation](https://www.ventoy.net/en/doc_news.html)

**Ventoy** is is an open source tool to create bootable USB drives for ISO/WIM/IMG/VHD(x)/EFI files. It allows the user to store multiple images, amongst other files, inside a single bootable medium.

Ventoy will create two partitions (EFI and exFAT) on the selected device. The exFAT one will work as regular storage, and will be scanned when booting Ventoy in search of bootable images.

## Contents

-   [[1] [Prerequisites]](#Prerequisites)
    -   [[1.1] [Overlay]](#Overlay)
        -   [[1.1.1] [eselect]](#eselect)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Emerge]](#Emerge)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Command line]](#Command_line)
        -   [[3.1.1] [Installing Ventoy on a device]](#Installing_Ventoy_on_a_device)
        -   [[3.1.2] [Updating a Ventoy device]](#Updating_a_Ventoy_device)
    -   [[3.2] [GUI]](#GUI)
-   [[4] [See also]](#See_also)

## [Prerequisites]

### [Overlay]

Ventoy is not on Gentoo\'s main repository, but a binary package is hosted on the [GURU](https://wiki.gentoo.org/wiki/GURU "GURU") overlay.

#### [eselect]

Using [eselect repository](https://wiki.gentoo.org/wiki/Eselect/Repository "Eselect/Repository"), run this command to add the overlay:

`root `[`#`]`eselect repository enable guru`

And then synchronize the repository:

`root `[`#`]`emaint -r guru sync`

## [Installation]

### [Emerge]

Once the [GURU](https://wiki.gentoo.org/wiki/GURU "GURU") overlay is enabled, sys-boot/ventoy-bin can be emerged:

`root `[`#`]`emerge --ask sys-boot/ventoy-bin`

## [Usage]

### [Command line]

Ventoy can be used on the command line. [ventoy] should be invoked along with the device in which the user wants to install or update Ventoy on.

** Note**\
[/dev/sdX] is an example. Replace it with the appropiate device entry.

`user `[`$`]`ventoy `

         Ventoy: 1.0.98  x86_64
         longpanda admin@ventoy.net
         https://www.ventoy.net

Usage: Ventoy2Disk.sh CMD \[ OPTION \] /dev/sdX

     CMD:
      -i  install Ventoy to sdX (fails if disk already installed with Ventoy)
      -I  force install Ventoy to sdX (no matter if installed or not)
      -u  update Ventoy in sdX
      -l  list Ventoy information in sdX

     OPTION: (optional)
      -r SIZE_MB  preserve some space at the bottom of the disk (only for install)
      -s/-S       enable/disable secure boot support (default is enabled)
      -g          use GPT partition style, default is MBR (only for install)
      -L          Label of the 1st exfat partition (default is Ventoy)

-n try non-destructive installation (only for install)

#### [Installing Ventoy on a device]

The [-i] flag can be used to install Ventoy on a device:

`root `[`#`]`ventoy -g -i /dev/sdX`

** Note**\
[-g] will make the device use the GPT format.

#### [Updating a Ventoy device]

A Ventoy device can be updated with the [-u] flag:

`root `[`#`]`ventoy -u /dev/sdX`

### [GUI]

Ventoy comes with a graphical tool as well. You can launch it via:

`root `[`#`]`ventoygui`

## [See also]

-   [LiveUSB](https://wiki.gentoo.org/wiki/LiveUSB "LiveUSB") --- explains how to create a *Gentoo LiveUSB* or, in other words, how to emulate a **[x86]** or **[amd64]** Gentoo LiveCD using a USB drive.