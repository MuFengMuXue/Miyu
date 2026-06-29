[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=System_recovery&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

Linux is very easy to break if you know what you\'re doing (or if you don\'t). This article will focus on repairing common issues or defects that may occur due to operator, system, or other error.

** Important**\
If the installation is damaged to the point it cannot start up/log in, a recovery environment such as a USB stick or CD/DVD is required. If you haven\'t found/created one yet, you must find other means of repairing the install such as placing the storage medium it is installed to into a different machine and fixing it from a stable OS.

## [Creating a recovery environment]

To start, please get a live environment ISO image that can be used to perform repairs with, often a USB stick or rewritable CD/DVD. This first chapter will cover a basic invocation of [dd] to flash or burn the image to the medium.

** Warning**\
This tool is very destructive; it will overwrite the root filesystem if instructed to without even asking. It will erase the entire device\'s contents. **Make sure to use the right device!**

This tool is almost always found in any Linux environment as most use GNU coreutils, the common utilities run from a shell like [cp], [rm], and [mv]. [dd] is one of these. Therefore, it\'s the easiest way to quickly create a recovery environment.

First, check the block device list:

`user `[`$`]`lsblk`

Please locate the target device that the image should be flashed to. Then, make sure to remember or note down the device node path, e.g. [/dev/sda].

** Note**\
Any partitions on the target device must be unmounted.

Then, change directory ([cd]) to where the image is located. Now, run the following command and be **very careful to insert the correct device node**.

`root `[`#`]`dd if=the_ISO_image.iso of=/dev/target_device bs=1M status=progress`

## [See also]

-   [Dd](https://wiki.gentoo.org/wiki/Dd "Dd") --- a utility used to copy raw data from a source into sink, where source and sink can be a block device, file, or piped input/output.
-   [Fix my Gentoo](https://wiki.gentoo.org/wiki/Fix_my_Gentoo "Fix my Gentoo") --- rescuing an installation when a chroot is not possible