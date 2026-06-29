**翻译状态：**

  * 本文（或部分内容）译自 [Multiboot USB drive](<https://wiki.archlinux.org/title/Multiboot_USB_drive> "arch:Multiboot USB drive")，最近一次同步于 2022-09-30，若英文版本有所[更改](<https://wiki.archlinux.org/title/Multiboot_USB_drive?diff=0&oldid=640905>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Multiboot_USB_drive_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [GRUB](<../zh-cn/GRUB.html> "GRUB")
  * [Syslinux](<../zh-cn/Syslinux.html> "Syslinux")
  * [Archiso](<../zh-cn/Archiso.html> "Archiso")

多引导USB启动盘可以从单个设备引导多个ISO镜像文件。ISO镜像文件可以不需要解压复制到U盘上就可以启动。以下有多种可用的方案，但不一定兼容所有ISO镜像。 

##  GRUB引导器及loopback devices实现

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** multiple [style](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:Style") issues（在[Talk:多引导 USB 设备](<../zh-cn/Talk:%E5%A4%9A%E5%BC%95%E5%AF%BC_USB_%E8%AE%BE%E5%A4%87.html>)讨论）

优点: 

  * 仅需要一个分区
  * 所有ISO文件镜像可在同一个文件夹下被检测到
  * 易于添加或移除ISO镜像文件

缺点: 

  * 并非所有镜像兼容
  * ISO文件原本的启动菜单不会显示
  * 找到可用的启动项可能并不容易

###  准备

在USB设备上创建至少一个[分区](<../zh-cn/%E5%88%86%E5%8C%BA.html> "分区")和一个[GRUB](<../zh-cn/GRUB.html> "GRUB")支持的[文件系统](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html#%E5%88%9B%E5%BB%BA%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "文件系统")。分区的大小取决与要存储在其中的ISO文件大小和引导程序所计划需要的空间。 

###  安装 GRUB引导器

####  简单安装

挂载U盘: 
    
    # mount /dev/sdXY /mnt
    
U盘上创建 /boot文件夹: 
    
    # mkdir /mnt/boot
    
安装GRUB到U盘: 
    
    # grub-install --target=i386-pc --recheck --boot-directory=/mnt/boot /dev/sdX
    
如果以UEFI启动镜像, 您需要按UEFI方式安装GRUB: 
    
    # grub-install --target=x86_64-efi --removable --boot-directory=/mnt/boot --efi-directory=/mnt
    
对于UEFI, 引导分区必须是FAT32格式, 且启动分区必须是MBR分区表中的第一个分区. 

####  混合 UEFI GPT + BIOS GPT/MBR 启动

以下有用的配置可以帮助您创建一份可以在任意地方启动的通用U盘。首先，您必须在您的设备上创建一份 [GPT](<../zh-cn/%E5%88%86%E5%8C%BA.html#GUID_%E5%88%86%E5%8C%BA%E8%A1%A8> "GPT") 分区。您至少需要以下三个分区： 

  1. 一个BIOS启动分区（gdisk代号编码 `EF02`），该分区至少需要1 MiB的大小。
  2. 一个EFI系统分区（gdisk代号编码`EF00`且它使用[FAT32文件系统](<../zh-cn/EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA.html> "EFI 系统分区")），该分区至少需要50 MiB的大小。
  3. 您自己的数据分区（使用[GRUB](<../zh-cn/GRUB.html> "GRUB")支持的文件系统)，该分区的大小是由您硬盘的剩余空间容量来决定的。

接下来您必须创建一个[MBR混合](<https://www.rodsbooks.com/gdisk/hybrid.html>)分区表。如果没有它，一个仅BIOS MBR引导启动的电脑将无法启动。因为它无法寻找到硬盘里的实例以启动。 

以下是一个使用[gdisk](<../zh-cn/GPT_fdisk.html> "Gdisk")创建MBR混合分区表的例子： 
    
    # gdisk /dev/sdX
    
    Command (? for help): r
    Recovery/transformation command (? for help): h
    
    WARNING! Hybrid MBRs are flaky and dangerous! If you decide not to use one,
    just hit the Enter key at the below prompt and your MBR partition table will
    be untouched.
    
    Type from one to three GPT partition numbers, separated by spaces, to be added to the hybrid MBR, in sequence: 1 2 3
    Place EFI GPT (0xEE) partition first in MBR (good for GRUB)? (Y/N): N
    
    Creating entry for GPT partition #1 (MBR partition #1)
    Enter an MBR hex code (default EF): 
    Set the bootable flag? (Y/N): N
    
    Creating entry for GPT partition #2 (MBR partition #2)
    Enter an MBR hex code (default EF): 
    Set the bootable flag? (Y/N): N
    
    Creating entry for GPT partition #3 (MBR partition #3)
    Enter an MBR hex code (default 83): 
    Set the bootable flag? (Y/N): Y
    
    Recovery/transformation command (? for help): x
    Expert command (? for help): h
    Expert command (? for help): w
    
    Final checks complete. About to write GPT data. THIS WILL OVERWRITE EXISTING
    PARTITIONS!!
    
    Do you want to proceed? (Y/N): Y
    
注意 Hybird MBR 只可以输入三个分区。 

不要忘了格式化这些分区： 
    
    # mkfs.fat -F32 /dev/sdX2
    # mkfs.ext4 /dev/sdX3
    
您现在可以安装GRUB以同时支持EFI + GPT引导以及BIOS + GPT/MBR引导。GRUB配置(--boot-directory）将会被保持在同一个地方。 

首先，您需要挂载您USB驱动器上的EFI系统分区和数据分区。 

以下是如何挂载的例子： 
    
    # mount /dev/sdX3 /mnt
    # mkdir -p /mnt/boot/EFI
    # mount /dev/sdX2 /mnt/boot/EFI
    
然后，您就可以在UEFI上安装GRUB： 

在大多数案例中，`EFI_MOUNTPOINT`将会对应至您所挂载的U盘上的`/mnt/boot/EFI`这个子目录中。`DATA_MOUNTPOINT`是数据分区的挂载目录。在本例中就是 sdX3 的挂载目录，即`/mnt`。 
    
    # grub-install --target=x86_64-efi --recheck --removable --efi-directory=/_EFI_MOUNTPOINT_ --boot-directory=/_DATA_MOUNTPOINT_ /boot
    
在BIOS上安装GRUB： 
    
    # grub-install --target=i386-pc --recheck --boot-directory=/_DATA_MOUNTPOINT_ /boot /dev/sd _X_
    
作为后备处理，您也可以把GRUB安装进您的MBR启动分区里面。 
    
    # grub-install --target=i386-pc --recheck --boot-directory=/_DATA_MOUNTPOINT_ /boot /dev/_sdX3_
    
###  配置 GRUB

####  参考模板

有些git项目中提供了一些预先存在的GRUB配置文件，一个优秀且通用的 grub.cfg 文件可以用来按需加载其他引导项，只有在指定的ISO文件（或包含它们的文件夹）存在于驱动器上时才会显示它们。 

Multiboot USB: <https://github.com/hackerncoder/multibootusb>

GLIM (GRUB2 Live ISO Multiboot): <https://github.com/thias/glim>

####  手动配置

通过手动编辑`grub.cfg`以代替自动生成它可以更容易的达到制作多启动USB驱动盘的目的。或者，在`/etc/grub.d/40_custom`或`/mnt/boot/grub/custom.cfg`中做出如下改动并通过[grub-mkconfig](<../zh-cn/GRUB.html#Generate_the_main_configuration_file> "GRUB")生成`/mnt/boot/grub/grub.cfg`。 

As it is recommend to use a [persistent name](<../zh-cn/Persistent_block_device_naming.html> "Persistent block device naming") instead of `/dev/sd _xY_` to identify the partition on the USB drive where the image files are located, define a variable for convenience to hold the value. If the ISO images are on the same partition as GRUB, use the following to read the UUID at boot time: 
    
    /mnt/boot/grub/grub.cfg
    
    # path to the partition holding ISO images (using UUID)
    probe -u $root --set=rootuuid
    set imgdevpath="/dev/disk/by-uuid/$rootuuid"

Or specify the UUID explicitly: 
    
    /mnt/boot/grub/grub.cfg
    
    # path to the partition holding ISO images (using UUID)
    set imgdevpath="/dev/disk/by-uuid/_UUID_value_ "

Alternatively, use the device label instead of UUID: 
    
    /mnt/boot/grub/grub.cfg
    
    # path to the partition holding ISO images (using labels)
    set imgdevpath="/dev/disk/by-label/_label_value_ "

The necessary UUID or label can be found using `lsblk -f`. Do not use the same label as the Arch ISO for the USB device, otherwise the boot process will fail. 

To complete the configuration, a boot entry for each ISO image has to be added below this header, see the next section for examples. 

###  启动项

It is assumed that the ISO images are stored in the `boot/iso/` directory on the same filesystem where GRUB is installed. Otherwise it would be necessary to prefix the path to ISO file with device identification when using the `loopback` command, for example `loopback loop **(hd1,2)** $isofile`. As this identification of devices is not [persistent](<../zh-cn/Persistent_block_device_naming.html> "Persistent block device naming"), it is not used in the examples in this section. 

One can use persistent block device naming like so. Replace the UUID according to your ISO filesystem UUID. 
    
    # define globally (i.e outside any menuentry)
    insmod search_fs_uuid
    search --no-floppy --set=**isopart** --fs-uuid _123-456_
    # later use inside each menuentry instead
    loopback loop **($isopart)** $isofile

**提示：** For a list of kernel parameters, see [the kernel's command-line parameter documentation](<https://docs.kernel.org/admin-guide/kernel-parameters.html>). For more examples of boot entries, see the [GRUB upstream documentation](<https://www.gnu.org/software/grub/manual/grub.html#Multi_002dboot-manual-config>) or the documentation for the distribution you wish to boot.

#### Arch Linux monthly release

Also see [archiso](<../zh-cn/Archiso.html> "Archiso"). 
    
    menuentry '[loopback]archlinux-2020.10.01-x86_64.iso' {
    	set isofile='/boot/iso/archlinux-2020.10.01-x86_64.iso'
    	loopback loop $isofile
    	linux (loop)/arch/boot/x86_64/vmlinuz-linux img_dev=$imgdevpath img_loop=$isofile earlymodules=loop
    	initrd (loop)/arch/boot/intel-ucode.img (loop)/arch/boot/amd-ucode.img (loop)/arch/boot/x86_64/initramfs-linux.img
    }

See [README.bootparams](<https://gitlab.archlinux.org/mkinitcpio/mkinitcpio-archiso/blob/master/docs/README.bootparams>) for archiso options supported in kernel command line. 

####  Memtest86+

[Memtest86+](</wzh/index.php?title=Stress_testing&action=edit&redlink=1> "Stress testing（页面不存在）")[[损坏的链接](<../Project:%E7%A4%BE%E7%BE%A4%E9%A6%96%E9%A1%B5.html#%E6%8D%9F%E5%9D%8F%E7%9A%84%E9%93%BE%E6%8E%A5> "Project:社群首页")：无效的章节]包含在每月构建的 ISO中。 
    
    menuentry '[loopback]archlinux-2020.10.01-x86_64.iso' {
    	set isofile='/boot/iso/archlinux-2020.10.01-x86_64.iso'
    	loopback loop $isofile
    	linux16 (loop)/arch/boot/memtest
    }

#### archboot

参见 [Archboot Homepage](<https://gitlab.archlinux.org/tpowa/archboot/-/wikis/Archboot-Homepage>)。 
    
    menuentry '[loopback]archlinux-2014.11-1-archboot' {
    	set isofile='/boot/iso/archlinux-2014.11-1-archboot.iso'
    	loopback loop $isofile
    	linux (loop)/boot/vmlinuz_**x86_64** iso_loop_dev=$imgdevpath iso_loop_path=$isofile
    	initrd (loop)/boot/initramfs_**x86_64**.img
    }

##  Syslinux和memdisk实现

Using the [memdisk](<https://wiki.syslinux.org/wiki/index.php/MEMDISK>) module, the ISO image is loaded into memory, and its bootloader is loaded. Make sure that the system that will boot this USB drive has sufficient amount of memory for the image file and running operating system. 

###  准备

Make sure that the USB drive is properly [partitioned](<../zh-cn/%E5%88%86%E5%8C%BA.html> "Partitioning") and that there is a partition with [file system](<../zh-cn/File_system.html> "File system") supported by Syslinux, for example fat32 or ext4. Then install Syslinux to this partition, see [Syslinux#Installation on BIOS](<../zh-cn/Syslinux.html#Installation_on_BIOS> "Syslinux"). 

###  安装 memdisk 模块

The memdisk module was not installed during Syslinux installation, it has to be installed manually. Mount the partition where Syslinux is installed to `/mnt/` and copy the memdisk module to the same directory where Syslinux is installed: 
    
    # cp /usr/lib/syslinux/bios/memdisk /mnt/boot/syslinux/
    
###  配置

在将ISO文件复制至USB驱动盘之后，编辑[Syslinux配置文件](<../zh-cn/Syslinux.html#Configuration> "Syslinux")并为ISO镜像创立菜单条目，最基础的条目看起来像这样： 
    
    boot/syslinux/syslinux.cfg
    
    LABEL _some_label_
        LINUX memdisk
        INITRD _/path/to/image.iso_
        APPEND iso
    
参见[memdisk on Syslinux wiki](<https://wiki.syslinux.org/wiki/index.php/MEMDISK>) 以了解更多调试选项。 

##  自动制作工具实现(开源软件)

  * **GRUB2 Live ISO Multiboot (GLIM)** — A set of GRUB configuration files to turn a VFAT formatted USB memory stick with GNU/Linux distribution ISO images into a multiboot USB drive.

     <https://github.com/thias/glim> || 未被打包？[在 AUR 里搜索](<https://aur.archlinux.org/packages/>)

  * **liveusb-builder** — 一个为GNU/Linux发行版创建多启动U盘的脚本套件

     <https://github.com/mytbk/liveusb-builder> || [liveusb-builder-git](<https://aur.archlinux.org/packages/liveusb-builder-git/>)AUR

  * **MultiBootUSB** — 一个具有CLI和GUI界面的跨平台Python软件，可添加或删除多个Linux LIVE映像环境到U盘。

     <https://github.com/mbusb/multibootusb> || [multibootusb](<https://aur.archlinux.org/packages/multibootusb/>)AUR

  * **MultiSystem** — 一个图形化工具，可添加或删除多个Linux LIVE映像环境到U盘。

     <http://liveusb.info/dotclear/> || [multisystem](<https://aur.archlinux.org/packages/multisystem/>)AUR

  * **[Ventoy](<../zh-cn/Ventoy.html> "Ventoy")** — 一个开源工具，为ISO/WIM/IMG/VHD(x)/EFI文件创建可引导的USB驱动器。不需要一遍又一遍格式化磁盘，只需要复制文件到U盘即可启动。

     <https://www.ventoy.net/> || [ventoy-bin](<https://aur.archlinux.org/packages/ventoy-bin/>)AUR

##  更多参考

  * GRUB: 
    * <https://help.ubuntu.com/community/Grub2/ISOBoot/Examples>
    * <https://help.ubuntu.com/community/Grub2/ISOBoot>
    * [GRUB Live ISO Multiboot](<https://github.com/thias/glim>) \- GRUB configurations for booting ISO images
  * Syslinux: 
    * [Boot an ISO image](<https://wiki.syslinux.org/wiki/index.php?title=Boot_an_Iso_image>)
