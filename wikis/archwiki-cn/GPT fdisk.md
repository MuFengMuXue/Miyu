**翻译状态：**

  * 本文（或部分内容）译自 [GPT fdisk](<https://wiki.archlinux.org/title/GPT_fdisk> "arch:GPT fdisk")，最近一次同步于 2023-11-11，若英文版本有所[更改](<https://wiki.archlinux.org/title/GPT_fdisk?diff=0&oldid=790593>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/GPT_fdisk_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [分区](<../zh-cn/%E5%88%86%E5%8C%BA.html> "分区")
  * [fdisk](<../zh-cn/Fdisk.html> "Fdisk")
  * [GNU Parted](<../zh-cn/GNU_Parted.html> "GNU Parted")
  * [dd](<../zh-cn/Dd.html> "Dd")

[GPT fdisk](<https://www.rodsbooks.com/gdisk/>) 是由 Rod Smith 编写的一套用于硬盘分区的文本模式工具集，由 _gdisk_ ， _cgdisk_ ， _sgdisk_ 和 _fixparts_ 组成。它适用于 GUID（Globally Unique Identifier）分区表（GPT）硬盘，而不是过去常用的 MBR（Master Boot Record）分区表。 

_gdisk_ ， _cgdisk_ 和 _sgdisk_ 在功能上一致，但提供了不同类型的用户界面。 _gdisk_ 提供文本交互模式， _sgdisk_ 提供命令行模式，而 _cgdisk_ 有基于 [curses](<https://en.wikipedia.org/wiki/curses_\(programming_library\)> "wikipedia:curses \(programming library\)") 的用户界面。该篇文章涵盖了 [gdisk(8)](<https://man.archlinux.org/man/gdisk.8>) 和 [sgdisk(8)](<https://man.archlinux.org/man/sgdisk.8>) 工具的使用。 

**提示：**

  * [cgdisk(8)](<https://man.archlinux.org/man/cgdisk.8>) 提供了基本的功能和命令行用户界面。
  * GPT fdisk 网站包含 [gdisk](<https://www.rodsbooks.com/gdisk/walkthrough.html>)，[cgdisk](<https://www.rodsbooks.com/gdisk/cgdisk-walkthrough.html>)，[sgdisk](<https://www.rodsbooks.com/gdisk/sgdisk-walkthrough.html>) 和 [FixParts](<https://www.rodsbooks.com/fixparts/>) 的详细使用步骤。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [gptfdisk](<https://archlinux.org/packages/?name=gptfdisk>)包。 

##  列出分区

要显示[块设备](<../zh-cn/Block_device.html> "Block device")上的分区表和分区信息，可以使用如下命令，其中设备名类似于 `/dev/sda`，`/dev/nvme0n1`，`/dev/mmcblk0` 等： 
    
    # gdisk -l /dev/sda
    
或者使用 _sgdisk_ 命令: 
    
    # sgdisk -p /dev/sda
    
##  备份和恢复分区表

修改磁盘前，请先备份磁盘的分区表，可以使用备份将相同的分区布局复制到多个设备上。 

_sgdisk_ 可以创建一个二进制备份，包含 MBR, GPT 主表头，GPT 备份表头和分区表副本。下面示例将 `/dev/sda` 的分区表信息备份到 `sgdisk-sda.bin`: 
    
    # sgdisk -b=sgdisk-sda.bin /dev/sda
    
通过下面命令恢复备份: 
    
    # sgdisk -l=sgdisk-sda.bin /dev/sda
    
如果要复制分区到其它磁盘，例如从 `/dev/sda` 复制到 `/dev/sdc`: 
    
    # sgdisk -R=/dev/sdc /dev/sda
    
如果两个磁盘位于同一个计算机，使用下面命令设置随机的分区 GUID: 
    
    # sgdisk -G /dev/sdc
    
##  创建分区表和分区

[分区](<../zh-cn/%E5%88%86%E5%8C%BA.html> "分区")操作的第一步是创建一个分区表。创建分区表后，就可以根据目标[分区方案](<../zh-cn/%E5%88%86%E5%8C%BA.html#%E5%88%86%E5%8C%BA%E6%96%B9%E6%A1%88> "分区")来创建分区了。 

在开始之前，建议先[备份](<#%E5%A4%87%E4%BB%BD%E5%92%8C%E6%81%A2%E5%A4%8D%E5%88%86%E5%8C%BA%E8%A1%A8>)当前的分区表和分区布局。 

下面的步骤演示了如何使用 _gdisk_ 来创建分区表和分区。另外，你也可以使用基于 curses 的 _cgdisk_ ，但下面的操作步骤就不再适用于你了。对应的用法可参考 [cgdisk(8)](<https://man.archlinux.org/man/cgdisk.8>)。 

_gdisk_ 自动将分区按 2048 个 512 字节扇区（1 MiB）对齐，这一设置兼容所有[先进格式化](<../zh-cn/%E5%85%88%E8%BF%9B%E6%A0%BC%E5%BC%8F%E5%8C%96.html> "先进格式化") HDD 和大部分的 [SSD](<../zh-cn/%E5%9B%BA%E6%80%81%E7%A1%AC%E7%9B%98.html> "SSD")。 

使用 _gdisk_ 时, 将要编辑的[块设备](<../zh-cn/Block_device.html> "Block device")作为命令参数。以 `/dev/sda` 为例： 
    
    # gdisk /dev/sda
    
###  创建新分区表

**警告：** 在已经保存数据的磁盘上创建新分区，会删除磁盘上的所有数据。

**提示：** 在分区前，先确认你的 NVMe 硬盘和先进格式化硬盘是否使用了[最佳逻辑扇区大小](<../zh-cn/%E5%85%88%E8%BF%9B%E6%A0%BC%E5%BC%8F%E5%8C%96.html> "先进格式化")。

在提示中输入 `o` 来创建新的 [GPT 分区表](<../zh-cn/%E5%88%86%E5%8C%BA.html#GUID_%E5%88%86%E5%8C%BA%E8%A1%A8> "分区")并清除当前所有的分区数据。如果分区已经创建了你需要的分区表，请跳过此步骤。 

###  创建分区

在提示中输入 `n` 命令来创建新分区。你需要提供分区编号，起始扇区位置，末端扇区位置及分区类型。 

**注意：** 对于分区大小和位置的相关问题可参考[分区#分区方案](<../zh-cn/%E5%88%86%E5%8C%BA.html#%E5%88%86%E5%8C%BA%E6%96%B9%E6%A1%88> "分区")。

####  分区编号

分区编号是分配给分区的一个数字，例如：磁盘 `/dev/sda` 上编号为 `1` 的分区是 `/dev/sda1`，类似的有 `/dev/nvme0n1` 上的 `/dev/nvme0n1p1` 和 `/dev/mmcblk0` 上的 `/dev/mmcblk0p1`。命名方案的细节可参考 [Device file#Partition](<../zh-cn/Device_file.html#Partition> "Device file")。分区编号不一定与分区在硬盘上的顺序匹配，在这种情况下你可以对它们进行[排序](<#Sort_partitions>)。 

建议使用 _gdisk_ 提出的默认编号。 

####  起始和末端扇区

分区的起始和末端扇区可以用扇区数或是以千字节（`K`），兆字节（`M`），吉字节（`G`），太字节（`T`）或是皮字节（`P`）为单位的位置进行指定。 

位置可以以用下方式进行指定： 

  * 从硬盘起始端开始计算的绝对值，例如：`40M` 起始端意味着扇区从硬盘的第 40 MiB 开始。
  * 以 `**+**_size_` 或 `**-**_size_` 为格式的相对位置，例如：`+2G` 代指默认起始扇区后 2 GiB 的位置，而 `-200M` 代指最后一个可用扇区往前 200 MiB 的位置。

Pressing the `Enter` key with no input specifies the default value, which is the start of the largest available block for the first sector and the end of the same block for the last sector. 

**注意：** 确保使用 `+_size{M,G,T,P}_` 格式的相对值指定分区大小，且不使用小于 1 MiB 的值，这样分区就能始终和设备属性对齐。

**提示：** 为了防备需要创建 [BIOS 启动分区](<../zh-cn/GRUB.html#GUID_%E5%88%86%E5%8C%BA%E8%A1%A8_\(GPT\)_%E7%89%B9%E6%AE%8A%E6%93%8D%E4%BD%9C> "GRUB")的情况发生，建议在硬盘前 2 TiB 的任意位置保留一个 1 MiB 大小的空余空间（例如使用 `+1M` 参数创建首个分区）。

####  分区类型

可以通过输入 gdisk 内置类型编码或手动指定[分区类型 GUID](<https://en.wikipedia.org/wiki/GUID_Partition_Table#Partition_type_GUIDs> "wikipedia:GUID Partition Table") 来选择分区类型。默认的 `Linux filesystem`（GUID `0FC63DAF-8483-4772-8E79-3D69D8477DE4`，gdisk 内置编码 `8300`）类型适用于大多数用例。 

**提示：**

  * 输入 `L` 可显示 gdisk 内置编码列表。
  * 建议遵循[分区发现规范](<https://uapi-group.org/specifications/specs/discoverable_partitions_specification/>)以让 [systemd-gpt-auto-generator(8)](<https://man.archlinux.org/man/systemd-gpt-auto-generator.8>) 进行自动挂载。如果你想禁用自动挂载，可参考[#Prevent GPT partition automounting](<#Prevent_GPT_partition_automounting>)。

常见分区类型  分区类型  | 挂载点  | gdisk 编码  |  [分区类型 GUID](<https://en.wikipedia.org/wiki/GUID_Partition_Table#Partition_type_GUIDs> "wikipedia:GUID Partition Table")  
---|---|---|---  
Linux 文件系统  | Any  |  `8300` |  `0FC63DAF-8483-4772-8E79-3D69D8477DE4`  
[EFI 系统分区](<../zh-cn/EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA.html> "EFI 系统分区") | Any1 |  `ef00` |  `C12A7328-F81F-11D2-BA4B-00A0C93EC93B`  
[BIOS 启动分区](<../zh-cn/GRUB.html> "GRUB") | None  |  `ef02` |  `21686148-6449-6E6F-744E-656564454649`  
[Linux x86-64 根分区 (/)](<../zh-cn/%E5%88%86%E5%8C%BA.html#%E6%A0%B9%E5%88%86%E5%8C%BA> "分区") |  `/` |  `8304` |  `4F68BCE3-E8CD-4DB1-96E7-FBCAF984B709`  
[Linux swap](<../zh-cn/%E5%88%86%E5%8C%BA.html#Swap> "分区") |  `[SWAP]` |  `8200` |  `0657FD6D-A4AB-43C4-84E5-0933C84B4F4F`  
[Linux /home](<../zh-cn/%E5%88%86%E5%8C%BA.html#/home> "分区") |  `/home` |  `8302` |  `933AC7E1-2EB4-4F13-B844-0E14E2AEF915`  
[Linux /srv](<../zh-cn/%E5%88%86%E5%8C%BA.html#%E5%A4%9A%E5%88%86%E5%8C%BA> "分区") |  `/srv` |  `8306` |  `3B8F8425-20E0-4F3B-907F-1A25A76F98E8`  
[Linux /var](<../zh-cn/%E5%88%86%E5%8C%BA.html#/var> "分区") |  `/var`1 |  `8310` |  `4D21B016-B534-45C2-A9FB-5C16E091FD2D`  
[Linux /var/tmp](<../zh-cn/%E5%88%86%E5%8C%BA.html#%E5%A4%9A%E5%88%86%E5%8C%BA> "分区") |  `/var/tmp`1 |  `8311` |  `7EC6F557-3BC5-4ACA-B293-16EF5DF639D1`  
[Linux LVM](</wzh/index.php?title=Install_Arch_Linux_on_LVM&action=edit&redlink=1> "Install Arch Linux on LVM（页面不存在）") | Any  |  `8e00` |  `E6D6D379-F507-44C2-A23C-238F2A3DF928`  
[Linux RAID](<../zh-cn/RAID.html#GUID_%E5%88%86%E5%8C%BA%E8%A1%A8> "RAID") | Any  |  `fd00` |  `A19D880F-05FC-4D3B-A006-743F0F84911E`  
[Linux LUKS](<../zh-cn/Dm-crypt/%E5%87%86%E5%A4%87%E7%A3%81%E7%9B%98.html#%E7%89%A9%E7%90%86%E5%88%86%E5%8C%BA> "Dm-crypt/准备磁盘") | Any  |  `8309` |  `CA7D7CCB-63ED-4C53-861C-1742536059CC`  
[Linux dm-crypt](<../zh-cn/Dm-crypt/%E5%87%86%E5%A4%87%E7%A3%81%E7%9B%98.html#%E7%89%A9%E7%90%86%E5%88%86%E5%8C%BA> "Dm-crypt/准备磁盘") | Any  |  `8308` |  `7FFEC5C9-2D00-49B7-8941-3EA10A5586B7`  
  
  1. [systemd-gpt-auto-generator(8)](<https://man.archlinux.org/man/systemd-gpt-auto-generator.8>) 只会在满足特定条件的情况下自动挂载分区，详细信息可参考 [systemd#GPT分区自动挂载](<../zh-cn/Systemd.html#GPT%E5%88%86%E5%8C%BA%E8%87%AA%E5%8A%A8%E6%8C%82%E8%BD%BD> "Systemd")。

重复这一步骤，直到创建完所有需要的分区。 

###  写入更改到硬盘

**提示：** 为了方便区分，可以使用 `c` 命令修改分区名称（[分区标签](<../zh-cn/%E5%9D%97%E8%AE%BE%E5%A4%87%E6%8C%81%E4%B9%85%E5%8C%96%E5%91%BD%E5%90%8D.html#%E9%80%9A%E8%BF%87%E5%88%86%E5%8C%BA%E6%A0%87%E7%AD%BE> "块设备持久化命名")）。

使用 `w` 命令来向硬盘写入分区表并退出。 

##  提示和技巧

###  在 MBR 和 GPT 之间转换

**提示：** 更多信息请阅读 Rod Smith 的 [MBR 与 GPT 互转换说明](<https://www.rodsbooks.com/gdisk/mbr2gpt.html>)。

_gdisk_ ， _sgdisk_ 和 _cgdisk_ 能将 MBR 和 [BSD 盘符](<https://en.wikipedia.org/wiki/BSD_disklabel> "wikipedia:BSD disklabel")无损转换为 GPT。转换时，所有 MBR 主分区和逻辑分区都会变成 GPT 分区，并为每个分区生成正确的分区类型 GUID 和唯一分区 GUID。 

转换之后，需要重新安装并配置[引导加载程序](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F> "引导加载程序")才能正常从 GPT 启动。 

**警告：**

  * GPT 在硬盘末端存放了第二分区表。该数据结构默认消耗 33 个 512 字节（16.5 KiB）扇区大小。MBR 在硬盘末端没有类似的数据结构，也意味着如果 MBR 硬盘上的最后一个分区占用了硬盘的最末端，会导致转换无法完成。如果你遇到了这种情况，需要放弃转换，并调整最后一个分区的大小。

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 提供该问题的相关引用。 (在 [Talk:GPT fdisk](<../zh-cn/Talk:GPT_fdisk.html>) 中讨论)

  * 已知基于 Intel 芯片组并在 RAID 模式下运行的笔记本存在备份 GPT 表损坏问题，解决方法是尽可能使用 AHCI 替代 RAID。

要用 _sgdisk_ 将 MBR 分区表转换为 GPT，使用 `-g`/`--mbrtogpt` 选项: 
    
    # sgdisk -g /dev/sda
    
要将 GPT 转换为 MBR，使用 `-m`/`--gpttombr` 选项，注意最多只能转换四个分区。 
    
    # sgdisk -m /dev/sda
    
### Sort partitions

This applies for when a new partition is created in the space between two partitions or a partition is deleted. `/dev/sda` is used in this example. 
    
    # sgdisk -s /dev/sda
    
After sorting the partitions if you are not using [Persistent block device naming](<../zh-cn/Persistent_block_device_naming.html> "Persistent block device naming"), it might be required to adjust the `/etc/fstab` and/or the `/etc/crypttab` configuration files. 

**注意：** The kernel must read the new partition table for the partitions (e.g. `/dev/sda1`) to be usable. Reboot the system or tell the kernel to [reread the partition table](<https://serverfault.com/questions/36038/reread-partition-table-without-rebooting>).

### Recover GPT header

In case main GPT header or backup GPT header gets damaged, you can recover one from the other with _gdisk_. `/dev/sda` is used in this example. 
    
    # gdisk /dev/sda
    
choose `r` for recovery and transformation options (experts only). From there choose either 

  * `b`: use backup GPT header (rebuilding main)
  * `d`: use main GPT header (rebuilding backup)

When done write the table to disk and exit via the `w` command. 

### Expand a GPT disk

After enlarging a disk (e.g. in hardware [RAID](<../zh-cn/RAID.html> "RAID") or a [virtual machine](</wzh/index.php?title=Virtual_machine&action=edit&redlink=1> "Virtual machine（页面不存在）") disk) the newly added free space will not be immediately usable since GPT keeps data at the end of the disk. You must relocate the backup GPT header to the new end of the disk. 

Run _sgdisk_ with the option `-e`/`--move-second-header`, e.g.: 
    
    # sgdisk -e /dev/sda
    
Afterwards [print the partition table](<#List_partitions>); the total free space should now be increased. 

### Prevent GPT partition automounting

[systemd-gpt-auto-generator(8)](<https://man.archlinux.org/man/systemd-gpt-auto-generator.8>) will automount partitions following the [Discoverable Partitions Specification](<https://uapi-group.org/specifications/specs/discoverable_partitions_specification/>). Sometimes that may not be desirable. 

The automounting can be disabled by setting the [partition attribute](<https://en.wikipedia.org/wiki/GUID_Partition_Table#Partition_entries_.28LBA_2-33.29> "wikipedia:GUID Partition Table") `63` "do not automount" on the partition. 

Start _gdisk_ , e.g.: 
    
    # gdisk /dev/sda
    
Press `p` to print the partition table and take note of the partition number(s) of the for which you want to disable automounting. 

Press `x` _extra functionality (experts only)_. 

Press `a` _set attributes_. Input the partition number and set the attribute `63`. Under `Set fields are:` it should now show `63 (do not automount)`. Press `Enter` to end attribute changing. Repeat this for all partitions you want to prevent from automounting. 

When done write the table to disk and exit via the `w` command. 

Alternatively using _sgdisk_ , the attribute can be set using the `-A`/`--attributes=` option; see [sgdisk(8)](<https://man.archlinux.org/man/sgdisk.8>) for usage. For example, to set partition attribute `63` "do not automount" on `/dev/sda2` run: 
    
    # sgdisk -A 2:set:63 /dev/sda
    
### gdisk EFI application

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** _gdisk_x64.efi_ [does not seem to work anymore](<https://sourceforge.net/p/refind/discussion/general/thread/549be07acc/>) and is apparently unmaintained. (在[Talk:GPT fdisk](<../zh-cn/Talk:GPT_fdisk.html>)讨论)

There is no package for the EFI version of gdisk, but Rod Smith provides a prebuilt gdisk-1.04 EFI binary on [SourceForge](<https://sourceforge.net/projects/gptfdisk/files/gptfdisk/1.0.4/gdisk-binaries/>). Download `gdisk-efi-*.zip` and extract the archive. To use it, copy `gdisk_x64.efi` to the [EFI system partition](<../zh-cn/EFI_system_partition.html> "EFI system partition") and launch it from your [boot loader](<../zh-cn/Boot_loader.html> "Boot loader") or [UEFI Shell](<../zh-cn/Unified_Extensible_Firmware_Interface.html#UEFI_Shell> "Unified Extensible Firmware Interface"). 

_gdisk_x64.efi_ allows you to edit the partition table before the operating system is even booted. It is used the same way as the _gdisk_ binary on Linux. 

**注意：** _gdisk_x64.efi_ cannot access the file system, thus it cannot backup the partition table to a file or restore it from a backup file.

See [README-efi.txt](<https://sourceforge.net/p/gptfdisk/code/ci/master/tree/README-efi.txt>) for more information. 

##  参阅

  * [GPT fdisk 教程](<https://www.rodsbooks.com/gdisk/index.html>) \- 带有详细演示步骤的 GPT fdisk 官方页面
  * [GPT fdisk SourceForge 页面](<https://sourceforge.net/projects/gptfdisk/>)
