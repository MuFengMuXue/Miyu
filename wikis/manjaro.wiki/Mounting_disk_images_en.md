[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Mounting+disk+images&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Mounting_disk_images "Mounting disk images (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Mounting_disk_images/ru "Монтирование образов дисков (100% translated)")

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Open Fuse ISO]](#Open_Fuse_ISO)
    -   [[2.1] [Fuseiso backend]](#Fuseiso_backend)

# [Overview]

Disk images come in various formats, ISO, NRG, BIN, CUE, MDF, etc. Most of these are going to be ISO images, which is also the standard image format to distribute Linux distributions and other open-source Operating systems. In order to access the disk image it has to be mounted, making it it readable. Manjaro is set up to take care of this quickly and easily.

\

# [Open Fuse ISO]

The Open Fuse ISO utility is provided by default in the Manjaro repositories. There are 2 packages available: **open-fuse-iso** and **open-fuse-iso-term**. The latter prints the output to the terminal, and the former prints the output to the notification system. The open-fuse-iso package includes the terminal only command as well.

**The utility provides a desktop entry, as such you can open an image file with \"Mount/Unmount image\" - it is set as the default action for ISO images, thus double-clicking will mount or unmount an ISO image.**

Open Fuse ISO terminal is installed by default in the NET Edition of Manjaro, and the regular variation is installed in all other official varieties as well as most community editions (depending on the maintainers software choice).

The utility is a script that calls fuseiso to mount and unmount image files in userspace. It will mount an image file in a newly created folder named \<image file\>.mount - **No root access is required**.

To use the terminal exclusive variety:

    ofit <image name>

To use the regular variety in a terminal:

    ofi <image name>

or

    open-fuse-iso <image name>

\

**Note**

------------------------------------------------------------------------

Other image formats besides .iso may also work, and the open-fuse-iso will attempt to mount them if asked

\

## [Fuseiso backend]

Since this utilty is a script that uses fuseiso\'s features, you can also use the backend directly. To mount:

    fuseiso -p <isofs_image_file> <mount_point>

To unmount:

    fusermount -u <mount_point>