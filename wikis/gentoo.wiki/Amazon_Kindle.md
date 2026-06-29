**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Amazon_Kindle "wikipedia:Amazon Kindle")

A quick document explaining how to use the **Amazon Kindle** with Gentoo.

## Contents

-   [[1] [Kernel]](#Kernel)
-   [[2] [Kindle DX / DX Graphite]](#Kindle_DX_.2F_DX_Graphite)
    -   [[2.1] [Mounting the Removable Storage Media]](#Mounting_the_Removable_Storage_Media)
        -   [[2.1.1] [Mounting using AutoFS]](#Mounting_using_AutoFS)
        -   [[2.1.2] [Mounting using udev]](#Mounting_using_udev)
-   [[3] [File Format Conversions]](#File_Format_Conversions)
    -   [[3.1] [PDF File Format]](#PDF_File_Format)
    -   [[3.2] [MOBI File Format]](#MOBI_File_Format)
-   [[4] [Tips]](#Tips)
-   [[5] [Free Books]](#Free_Books)
-   [[6] [Mobile Linux Websites]](#Mobile_Linux_Websites)
-   [[7] [See also]](#See_also)
-   [[8] [External resources]](#External_resources)

## [Kernel]

To be able to mount your Kindle as an [external storage device](https://wiki.gentoo.org/wiki/Removable_media "Removable media"), you require the **VFAT** file system as well as support for DOS partition tables in your kernel.

[KERNEL] **Enabling File System Options**

    File Systems  --->
       DOS/FAT/NT Filesystems  --->
           [*] VFAT (Windows-95) fs support
    Enable the block layer  --->
       Partition Types  --->
           [*] PC BIOS (MSDOS partition tables) support

## [][Kindle DX / DX Graphite]

### [Mounting the Removable Storage Media]

#### [Mounting using AutoFS]

Execute blkid ([[[sys-apps/util-linux]](https://packages.gentoo.org/packages/sys-apps/util-linux)[]]) with the Kindle device attached.

`root `[`#`]`blkid`

Find the [UUID](https://wiki.gentoo.org/wiki/Removable_media#UUIDs_and_labels "Removable media") from the blkid output and insert the following line into your [/etc/autofs/auto.misc] file, substituting *UUID* with your UUID:

[FILE] **`/etc/autofs/auto.misc`**

    kindle    -fstype=vfat,gid=100,noatime,rw,umask=002,user,utf8    UUID="Your_UUID_from_blkid_Output"

Edit the [/etc/conf.d/autofs] file to your liking. Make sure you uncomment the *MASTER_MAP_NAME=\"auto.master\"* line if you use the [/etc/autofs/auto.master] file!

The following addition to the [auto.master] file can be used. The *\--ghost* option auto-unmounts after five seconds:

[FILE] **`1/etc/autofs/auto.master`**

    /mnt/auto   /etc/autofs/auto.misc   --timeout=5 --ghost

#### [Mounting using udev]

The following [udev](https://wiki.gentoo.org/wiki/Udev "Udev") rule will mount your Kindle using the Volume Name (ie. \"Kindle\") to ([/media/Kindle]). You then will need to execute the user scripts [add.sh] and [remove.sh] to tell the udev to add (mount) and remove (unmount) the device. In turn, the [/media/Kindle] folder is automagically created and destroyed on mount and unmount.

[FILE] **`/etc/udev/rules.d/11-media-by-label-auto-mount.rules`**

    SUBSYSTEM!="usb", KERNEL!="sd[c-z][0-9]", GOTO="media_by_label_auto_mount_end"

    # Import FS infos
    IMPORT="/sbin/blkid -o udev -p %N"

    # Get a label if present, otherwise specify one
    ENV!="", ENV="%E"
    ENV=="", ENV="usbhd-%k"

    # Global mount options
    #ACTION=="add", ENV="relatime"
    ACTION=="add", ENV="noatime"
    # Filesystem-specific mount options
    ACTION=="add", ENV=="vfat|ntfs", ENV="$env,utf8,gid=100,umask=002"

    # Mount the device
    ACTION=="add", RUN+="/bin/mkdir -p /media/%E", RUN+="/bin/mount -o $env /dev/%k /media/%E"

    # Clean up after removal
    ACTION=="remove", ENV!="", RUN+="/bin/umount -l /media/%E", RUN+="/bin/rmdir /media/%E"

    # Exit
    LABEL="media_by_label_auto_mount_end"

[FILE] **`/home/user/bin/udev-add-all.sh`**

    #!/bin/bash -
    #===============================================================================
    #
    #          FILE:  udev-add.sh
    #
    #         USAGE:  ./udev-add.sh
    #
    #   DESCRIPTION: udev add removable media device
    #
    #        AUTHOR: Roger Zauner (rdz), rogerx (dot) oss (at) gmail (dot) com
    #       CREATED: 04/10/2010 12:18:57 AM AKDT
    #===============================================================================

    set -o nounset                              # Treat unset variables as an error
    #set -o xtrace                              # Enable trace debugging

    # sd[b-z][0-9]
    #udevadm trigger --action="add" --sysname-match="sdb1" --verbose

    if [ $HOSTNAME = "localhost1.local" ]; then
        sudo /sbin/udevadm trigger --action="add" \
          --sysname-match="sd[c-z][0-9]" --verbose
    #    sudo /sbin/udevadm trigger --action="add" \
    #      --sysname-match="sr[0-9]" --verbose

      elif [ $HOSTNAME = "localhost2.local" ]; then
        sudo /sbin/udevadm trigger --action="add" \
          --sysname-match="sd[c-z][0-9]" --verbose
    #    sudo /sbin/udevadm trigger --action="add" \
    #      --sysname-match="sr[0-9]" --verbose

      elif [ $HOSTNAME = "localhost3.local" ]; then
        sudo /sbin/udevadm trigger --action="add" \
          --sysname-match="sd[b-z][0-9]" --verbose
    #    sudo /sbin/udevadm trigger --action="add" \
    #      --sysname-match="sr[0-9]" --verbose
    fi

[FILE] **`/home/user/bin/udev-remove.sh`**

    #!/bin/bash -
    #===============================================================================
    #
    #          FILE:  udev-remove.sh
    #
    #         USAGE:  ./udev-remove.sh
    #
    #   DESCRIPTION: udev remove removable media device
    #
    #        AUTHOR: Roger Zauner (rdz), rogerx (dot) oss (at) gmail (dot) com
    #       CREATED: 04/10/2010 12:22:17 AM AKDT
    #===============================================================================

    set -o nounset                              # Treat unset variables as an error
    #set -o xtrace                              # Enable trace debugging

    # sd[b-z][0-9]
    #udevadm trigger --action="remove" --sysname-match="sdb1" --verbose

    if [ $HOSTNAME = "localhost1.local" ]; then
        sudo /sbin/udevadm trigger --action="remove" \
          --sysname-match="sd[c-z][0-9]" --verbose
    #    sudo /sbin/udevadm trigger --action="remove" \
    #      --sysname-match="sr[0-9]" --verbose

      elif [ $HOSTNAME = "localhost2.local" ]; then
        sudo /sbin/udevadm trigger --action="remove" \
          --sysname-match="sd[c-z][0-9]" --verbose
    #    sudo /sbin/udevadm trigger --action="remove" \
    #      --sysname-match="sr[0-9]" --verbose

      elif [ $HOSTNAME = "localhost3.local" ]; then
        sudo /sbin/udevadm trigger --action="remove" \
          --sysname-match="sd[b-z][0-9]" --verbose
    #    sudo /sbin/udevadm trigger --action="remove" \
    #      --sysname-match="sr[0-9]" --verbose
    fi

The AutoFS method may be preferred, as it is cleaner and doesn\'t need running the above user scripts. The main problem with the Kindle DX seems to be the DX\'s display stating the device is plugged in. Even though this is true, you can still unplug the device without using the **eject** command and the device is not mounted! And, using the **eject** command at times would confuse the device and the Linux sub-system at times. So, just unplug the device after checking the device is no longer mounted via the **mount** command. As such, much easier to just use AutoFS, as it can be configured to auto unmount it for you using the *\--ghost* option.

## [File Format Conversions]

Simple utilities for converting documents can be used, as shown below.

### [PDF File Format]

Best format to read technical documents is PDF.

-   You can create PDF\'s easily from printing them from Seamonkey or Firefox using the print to file method.
-   Use ps2pdf utilities ([[[app-text/ghostscript-gpl]](https://packages.gentoo.org/packages/app-text/ghostscript-gpl)[]])

### [MOBI File Format]

The basis of this file format is HTML, but with the feature of DRM when required by publishers. Keep it simple, avoiding TABLE tag usage. (See Amazon\'s AmazonKindlePublishingGuidelines.pdf.)

Use [Vim](https://wiki.gentoo.org/wiki/Vim "Vim") to convert a ASCII/UTF8 text file to HTML. Execute Vim\'s \":ToHtml\" command and save, then use Amazon\'s kindlegen binary on the saved file. (KindleGen is Amazon\'s version of MobiGen.)

## [Tips]

-   When possible, copy both the MOBI and PDF file formats to the device as both currently have separate pros and cons (e.g. O\'Reilly publishes books into a multitude of formats).
-   Because there are so many files freely available, create subfolders within the [/mnt/kindle/documents] folder even though the Kindle DX Graphite firmware doesn\'t display the folders, but will see the files within the folders. Then use the Kindle firmware to create a \"Collection\" with a similar name to the folders (e.g. Filesystem folder name [/mnt/kindle/documents/programming-c], Collection Name \"Programming - C\").

## [Free Books]

-   Gentoo Wiki articles can be printed to either PDF or HTML using the \"Printable version\" link, located to the bottom left within the \"toolbox\" of the viewable version of pages.
-   Many C Programming books, specifications and manuals are already freely available in PDF format (e.g. [C on Freenode](https://www.iso-9899.info/wiki/Main_Page) lists many freely available recommended books).
-   Many [FSF GNU Manuals](https://www.gnu.org/manual/) are also already available in HTML and PDF formats.
-   Manual Pages (AKA manpages) can be easily converted to HTML, then MOBI using KindleGen (see references below).
-   [TLDP](https://tldp.org/) hosts many HowTo\'s and documents in PDF and HTML formats.
-   [Python](https://www.python.org/doc/) hosts its documentation in PDF, HTML and EPUB formats.

## [Mobile Linux Websites]

-   [Lxer News (Mobile Version)](http://lxer.com/module/newswire/mobile.php)

## [See also]

-   [AutoFS](https://wiki.gentoo.org/wiki/AutoFS "AutoFS") --- a program that uses the Linux [kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") automounter to automatically [mount](https://wiki.gentoo.org/wiki/Mount "Mount") [filesystems](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") on demand.

## [External resources]

-   [Amazon Publishing Programs](https://www.amazon.com/gp/feature.html?ie=UTF8&docId=1000234621) KindleGen Program and AmazonKindlePublishingGuidelines.pdf
-   [Amazon Kindle DXG and Linux](http://rogerx.freeshell.org/programming/kindledxg_and_linux.html)
-   [Amazon Kindle - Converting .txt to .html to .mobi](http://rogerx.freeshell.org/programming/kindle-convert_txttomobi.html)
-   [Amazon Kindle - Convert Linux Manual Pages to .mobi](http://rogerx.freeshell.org/programming/kindle-convert_linuxmantomobi.html)
-   [Amazon Kindle - Strip](http://rogerx.freeshell.org/programming/kindle-strip.html)