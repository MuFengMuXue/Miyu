+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [![Tango-dialog-warning.png](/images/d/d8/Tango-dialog-warning.png)](//wiki.manjaro.org/index.php?title=File:Tango-dialog-warning.png) | **This article or section is out of date.**                                                                                                                                                                    | [![Tango-dialog-warning.png](/images/d/d8/Tango-dialog-warning.png)](//wiki.manjaro.org/index.php?title=File:Tango-dialog-warning.png) |
|                                                                                                                                                                                                                          |                                                                                                                                                                                                                |                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                          | :::                                                                                                                                                                                    |                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                          | **Reason:** Some statements needs revision - ventoy is missing ([Discuss](//wiki.manjaro.org/index.php?title=Talk:Burn_an_ISO_File&action=edit&redlink=1 "Talk:Burn an ISO File (page does not exist)")) |                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                          | :::                                                                                                                                                                                                            |                                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Other languages:

[English] • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Burn_an_ISO_File/tr "ISO Dosyası Yazma (90% translated)") • ‎[español](//wiki.manjaro.org/index.php?title=Burn_an_ISO_File/es "Grabar un archivo ISO (90% translated)") • ‎[français](//wiki.manjaro.org/index.php?title=Burn_an_ISO_File/fr "Graver une image disque ISO (67% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Burn_an_ISO_File/ru "Запись ISO-файла (100% translated)") • ‎[فارسی](//wiki.manjaro.org/index.php?title=Burn_an_ISO_File/fa "یک پرونده ISO بنویسید (75% translated)")

## Contents

-   [[1] [Overview]](#Overview)
    -   [[1.1] [Burning to CD/DVD in Linux]](#Burning_to_CD.2FDVD_in_Linux)
    -   [[1.2] [Burning to a CD/DVD in Windows]](#Burning_to_a_CD.2FDVD_in_Windows)
    -   [[1.3] [Writing to a USB Stick in Linux]](#Writing_to_a_USB_Stick_in_Linux)
    -   [[1.4] [Using the Terminal]](#Using_the_Terminal)
    -   [[1.5] [How you can check ISO]](#How_you_can_check_ISO)
    -   [[1.6] [How create isohybrid]](#How_create_isohybrid)
    -   [[1.7] [Using a Burning Application]](#Using_a_Burning_Application)
        -   [[1.7.1] [ImageWriter]](#ImageWriter)
    -   [[1.8] [Writing to a USB Stick in Windows]](#Writing_to_a_USB_Stick_in_Windows)
        -   [[1.8.1] [Using Rufus]](#Using_Rufus)
    -   [[1.9] [Writing to a USB Stick on a Macintosh]](#Writing_to_a_USB_Stick_on_a_Macintosh)
-   [[2] [See Also]](#See_Also)

## [Overview]

As outlined in the **[Download Manjaro page](//wiki.manjaro.org/index.php?title=Special:MyLanguage/Download_Manjaro "Special:MyLanguage/Download Manjaro")**, an ISO is not simply a \'drag and drop\' or \'copy and paste\' duplication of Manjaro\'s installation files. It is in fact a copy of the raw computer code that makes up the files themselves. This is why it is necessary to use a **software burning application** to \'burn\' an ISO file, that is, convert its raw code into the files onto a physical medium such as a DVD or USB flashdrive / datastick in order to use it. Once burned / converted, the files on that medium can then be used to run Manjaro directly without having to install it to your system (referred to as *Live-CD or Live-USB* mode), and/or install Manjaro on your system. Again however, it will not be necessary to to burn an ISO if you intend on running Manjaro in a virtual machine environment using Oracle\'s Virtualbox. This is because Virtualbox is able to read ISO files directly as *virtual disks*.

**note**

------------------------------------------------------------------------

Manjaro will not have full functionality when run in Live-CD mode. For example, you will not be able to save any changes to the system, or install updates or new applications.

### [][Burning to CD/DVD in Linux]

**tip**

------------------------------------------------------------------------

It is strongly recommended to select the slowest speed available when burning to disc in order minimise the possibility of corruption during the burning process.

Several different software burning applications - if not already installed - should be available for installation from your distribution\'s Software Center / Software Manager / Package Manager / repositories. Popular burners include *XFBurn*, *K3b*, and *Brasero*. Which one you may choose is entirely down to personal choice. However, a guide to burning your downloaded Manjaro ISO using Brasero has been provided below:

[![Brasero.png](/images/thumb/5/56/Brasero.png/375px-Brasero.png)](//wiki.manjaro.org/index.php?title=File:Brasero.png)

[](//wiki.manjaro.org/index.php?title=File:Brasero.png "Enlarge")

**1.** Insert a Blank CD/DVD (use a DVD if burning an ISO for anything other than the NET Edition)

**2.** Start the Brasero software burner

**3.** Click the **Burn Image - Burn an existing CD/DVD image to disc** button to open the *Image Burning Setup* window.

**4.** Click the button beneath the title **Select a disc image to write** to open up your file manager. Locate and double-click the downloaded ISO file to load it. Upon automatically returning to the *Image Burning Setup* window, note that the ISO file is now listed as the disc image to write.

**5.** Underneath the title **Select a disc to write to** the blank CD/DVD inserted should already have been automatically listed. Otherwise, click the button to select it manually.

**6.** Click the **properties** button to open the *properties window*, and then click the button beneath the title **Burning Speed**. Again, it is strongly recommended to select the slowest speed available. Once selected, click the **Close** button.

**7.** Click the **Burn** button to start the burning process. If necessary, follow any on-screen instructions provided.

**8.** In case that Brasero complains about the iso-image not being recognized as iso: switch to XFBurn. This will burn without complaints.

### [][Burning to a CD/DVD in Windows]

In Windows 7 and later, support for burning an ISO to DVD is built-in. Simply right click on the on .iso file and select \"Burn disk image\". This will bring up a series of dialogues to walk you through the process.

For Windows Vista or older versions of Windows you will need to download 3rd party software. Several free software burner applications are available for Windows. One such tool is DeepBurner. The portable version can be downloaded from [here](https://pendriveapps.com/deepburner-portable/).

### [Writing to a USB Stick in Linux]

This section describes how to write a Linux ISO file to USB.

Windows ISO files are notoriously difficult and requires special attention.

### [Using the Terminal]

To burn the iso on an usb stick, enter the following command in a terminal :

[user \$ ][ sudo dd bs=4M if=/path/to/manjaro.iso of=/dev/sd\[drive letter\] status=progress oflag=sync [COPY TO CLIPBOARD]]

\

Where \[drive letter\] is the letter of your removable device. Please note that it is the **device** (e.g. /dev/sdb), and **not** the partition number (e.g. /dev/sdb1).

To find which drive letter it might be write:

[user \$ ][ sudo fdisk -l [COPY TO CLIPBOARD]]

\

\

**Warning**

------------------------------------------------------------------------

Not all ISO are isohybrid ! However you can create isohybrid ISO. If you use very old hardware and rare, may not support isohybrid. Isohybrid created for UEFI should work with \"Legacy mode\", without support UEFI not will work on UEFI. Before use USB stick check Bios/UEFI settings, USB should start first. If isohybrid not working for you with uefi, try create isohybrid for own use without this option.

\

### [How you can check ISO]

[user \$ ][ fdisk -l [COPY TO CLIPBOARD]]

\

Example:

[user \$ ][ fdisk -l manjaro-mate-15.12-x86_64.iso ]

Disk manjaro-mate-15.12-x86_64.iso: 7,5 GiB, 8006074368 bytes, 15636864 sectors Units: sectors of 1 \* 512 = 512 bytes Sector size (logical/physical): 512 bytes / 512 bytes I/O size (minimum/optimal): 512 bytes / 512 bytes Disklabel type: dos

Disk identifier: 0x00000000 [COPY TO CLIPBOARD]

\

[user \$ ][ fdisk -l manjaro-xfce-16.08-x86_64.iso ]

Disk manjaro-xfce-16.08-x86_64.iso: 1,5 GiB, 1561657344 bytes, 3050112 sectors Units: sectors of 1 \* 512 = 512 bytes Sector size (logical/physical): 512 bytes / 512 bytes I/O size (minimum/optimal): 512 bytes / 512 bytes Disklabel type: dos Disk identifier: 0x06c2dccb . Device Boot Start End Sectors Size Id Type manjaro-xfce-16.08-x86_64.iso1 \* 0 3050111 3050112 1,5G 0 Empty

manjaro-xfce-16.08-x86_64.iso2 224 63711 63488 31M ef EFI (FAT-12/16/32) [COPY TO CLIPBOARD]

\

Isohybrid have 2 partitions, you can check also with gparted after burn the iso on an usb stick.

### [How create isohybrid]

[user \$ ][ isohybrid -v /path/to/name.iso [COPY TO CLIPBOARD]]

\

or for UEFI

[user \$ ][ isohybrid \--uefi -v output.iso [COPY TO CLIPBOARD]]

\

More in [https://wiki.syslinux.org/wiki/index.php?title=Isohybrid](https://wiki.syslinux.org/wiki/index.php?title=Isohybrid)

### [Using a Burning Application]

#### [ImageWriter]

ImageWriter should be available for installation from your distribution\'s Software Center / Software Manager / Package Manager / repositories. Once Imagewriter has been downloaded and installed, ensure that your USB stick is plugged in before starting it.

A brief guide to writing the Manjaro .ISO image has been provided:

**1.** Click on the centre icon

**2.** Navigate to where the ISO image has been saved and select it

**3.** Ensure that your USB device has been selected from the drop-down menu

**4.** Click on the **Write** button

**5.** After the **Write** process has finished, reboot your system

### [Writing to a USB Stick in Windows]

#### [Using Rufus]

[Rufus](https://rufus.ie/en/) is a utility that helps format and create bootable USB flash drives, such as USB keys/pendrives, memory sticks, etc.

When you use Rufus to write a Manjaro Live ISO to USB you must select DD mode when prompted to use standard or DD mode.

See its website for more details: [https://rufus.ie/en/](https://rufus.ie/en/)

### [Writing to a USB Stick on a Macintosh]

As a Unix variant, macOS uses a similar approach to Linux. All commands below should be run in the **Terminal** application. Commands using **sudo** may prompt for your password; this is expected.

After you\'ve inserted your USB drive, identify it using **diskutil**:

[user \$ ][ diskutil list [COPY TO CLIPBOARD]]

\

      /dev/disk0 (internal, physical):
         #:                       TYPE NAME                    SIZE       IDENTIFIER
         0:      GUID_partition_scheme                        *1.0 TB     disk0
         1:                        EFI EFI                     209.7 MB   disk0s1
         2:                 Apple_APFS Container disk1         1000.0 GB  disk0s2
      /dev/disk3 (external, physical):
         #:                       TYPE NAME                    SIZE       IDENTIFIER
         0:     FDisk_partition_scheme                        *7.8 GB     disk3
         1:               Windows_NTFS MYUSBDRIVE              7.8 GB     disk3s1

Note the identifier **disk3s1** in this example.

Unmount the drive with the command:

[user \$ ][ sudo diskutil unmount /dev/disk3s1 [COPY TO CLIPBOARD]]

\

      Volume MYUSBDRIVE on disk3s1 unmounted

Now you can use **dd** to write to the raw device:

[user \$ ][ sudo dd bs=4M if=Desktop/manjaro-i3-21.2.3-220205-linux515.iso of=/dev/disk3 [COPY TO CLIPBOARD]]

\

      787+1 records in
      787+1 records out
      3303161856 bytes transferred in 2470.782563 secs (1336889 bytes/sec)

The USB drive can now be removed from the computer and used to boot Manjaro.

## [See Also]

-   **[Download Manjaro](//wiki.manjaro.org/index.php?title=Special:MyLanguage/Download_Manjaro "Special:MyLanguage/Download Manjaro")**
-   **[Check a Downloaded ISO Image For Errors](//wiki.manjaro.org/index.php?title=Special:MyLanguage/Check_a_Downloaded_ISO_Image_For_Errors "Special:MyLanguage/Check a Downloaded ISO Image For Errors")**
-   **[Installation Guide](//wiki.manjaro.org/index.php?title=Special:MyLanguage/Installation_Guides "Special:MyLanguage/Installation Guides")**