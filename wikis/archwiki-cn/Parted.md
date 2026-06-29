**翻译状态：**

  * 本文（或部分内容）译自 [Parted](<https://wiki.archlinux.org/title/Parted> "arch:Parted")，最近一次同步于 2024-05-22，若英文版本有所[更改](<https://wiki.archlinux.org/title/Parted?diff=0&oldid=808824>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Parted_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [fdisk](<../zh-cn/Fdisk.html> "Fdisk")
  * [gdisk](<../zh-cn/GPT_fdisk.html> "Gdisk")
  * [分区](<../zh-cn/%E5%88%86%E5%8C%BA.html> "分区")

[GNU Parted](<https://www.gnu.org/software/parted/parted.html>) 是创建和处理分区表的程序。GParted 是 GUI 前端。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")下列任一软件包： 

  * [parted](<https://archlinux.org/packages/?name=parted>)包 – 仅命令行版本
  * [gparted](<https://archlinux.org/packages/?name=gparted>)包 – _parted_ 的图形化前端

**注意：** 在 [Wayland](<../zh-cn/Wayland.html> "Wayland") 下运行 GParted 同时需要安装 [xorg-xhost](<https://archlinux.org/packages/?name=xorg-xhost>)包 可选包。更多信息请参考 [[1]](<http://gparted-forum.surf4.info/viewtopic.php?id=17682>)

##  使用

Parted 有两种模式：命令行模式和交互模式，请用下面命令启动： 
    
    # parted _device_
    
其中 `_device_` 是要编辑的[块设备](<../zh-cn/%E8%AE%BE%E5%A4%87%E6%96%87%E4%BB%B6.html#%E5%9D%97%E8%AE%BE%E5%A4%87> "块设备")（例如 `/dev/sda`，`/dev/nvme0n1`，`/dev/mmcblk0` 等）。如果你缺省了 `_device_` 参数， _parted_ 将尝试猜测要使用的设备。 

###  命令行模式

在命令行模式下，可以同时执行一个或多个命令： 
    
    # parted /dev/sda mklabel gpt mkpart P1 ext3 1MiB 8MiB 
    
**注意：**`--help` 等参数只有在命令行中才能指定。

###  交互模式

交互模式简化了分区过程，并自动将所有命令应用到指定的设备上，无需反复指定目标设备。 

In order to start operating on a device, execute: 
    
    # parted /dev/sd _x_
    
命令提示符会从 (`#`) 变成 `(parted)`：这也意味着无需将新的命令提示符作为命令的一部分进行输入。 

要查看可用的命令，输入： 
    
    (parted) help
    
完成操作后，或是要对另一个设备创建分区表或格式时，用下面命令退出： 
    
    (parted) quit
    
退出后命令提示符会变回到 `#`。 

如果命令没带参数，Parted 会进行询问： 
    
    (parted) mklabel
    New disk label type? gpt
    
##  数值设定

很多分区系统有复杂的限制，Parted 可能会对输入的数值进行稍微的修改。例如设定了 10.4Mb，实际会使用 10.352Mb。如果修正后的数值差异太大，Parted 会进行提示确认。如果你有需要指定数值，或是想看看 Parted 所做的操作，可以用扇区值加上“s”后缀指定数值，并使用“unit s”命令让分区信息以扇区值为单位显示。 

从 parted-2.4 开始，当使用 “MiB”, “GiB”, “TiB” 等 IEC 单位时，parted 会使用与对应的字节值（即“B”后缀）相同的精确数值，不进行任何修正。而使用“4GB”这样的值时，可能会落到最大前后相差 500MB 的位置上。因此，在创建分区时，建议使用字节（“B”），扇区（“s”）或是像“MiB”这样的 IEC 二进制单位，而不是“MB”，“GB”等。 

##  分区

###  创建新分区表

**警告：** 如果你在存有数据的硬盘上创建新分区表，硬盘上所有数据都会被清除。因此，在进行操作前请再次进行确认。

**提示：**

  * 在分区前，检查你的 NVMe 硬盘和先进格式硬盘是否使用了[最佳逻辑扇区大小](<../zh-cn/%E5%85%88%E8%BF%9B%E6%A0%BC%E5%BC%8F%E5%8C%96.html> "先进格式化")。
  * 在对固态硬盘进行分区之前，考虑执行[存储单元清理](</wzh/index.php?title=%E5%9B%BA%E6%80%81%E7%A1%AC%E7%9B%98/%E5%AD%98%E5%82%A8%E5%8D%95%E5%85%83%E6%B8%85%E7%90%86&action=edit&redlink=1> "固态硬盘/存储单元清理（页面不存在）")（英语：[Solid state drive/Memory cell clearing](<https://wiki.archlinux.org/title/Solid_state_drive/Memory_cell_clearing> "en:Solid state drive/Memory cell clearing")）。

如果一个硬盘没有做过分区，或者是你想要修改分区表的类型，你需要为对应的设备创建/重建分区表。另外，对于分区方案要完全重建的设备来说，重建分区表也很有用。 

用下面的命令打开要创建/重建分区表的设备： 
    
    # parted /dev/sd _x_
    
使用以下命令创建 [GUID 分区表](<../zh-cn/%E5%88%86%E5%8C%BA.html#GUID_%E5%88%86%E5%8C%BA%E8%A1%A8> "分区")： 
    
    (parted) mklabel gpt
    
使用下列命令创建 [MBR](<../zh-cn/%E5%88%86%E5%8C%BA.html#%E4%B8%BB%E5%BC%95%E5%AF%BC%E8%AE%B0%E5%BD%95> "分区")/MS-DOS 分区表： 
    
    (parted) mklabel msdos
    
###  分区方案

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 将所有的百分数替换为已对齐的特定 MiB 值，以防止 [对齐问题](<../zh-cn/Advanced_Format.html#Partition_alignment> "Advanced Format")。同时也提醒这一问题。 (在 [Talk:Installation guide#Remove parted](</wzh/index.php?title=Talk:Installation_guide&action=edit&redlink=1> "Talk:Installation guide（页面不存在）") 中讨论)

你可以决定磁盘分区的数量和各自的大小，以及分区应挂载到安装的系统上哪些文件夹（一般称为 _挂载点_ ）。可以在[分区#分区方案](<../zh-cn/%E5%88%86%E5%8C%BA.html#%E5%88%86%E5%8C%BA%E6%96%B9%E6%A1%88> "分区")查看具体需要的分区。 

创建分区将用到如下命令： 
    
    (parted) mkpart _part-type-or-part-label_ _fs-type_ _start_ _end_
    
  * 根据分区表的不同，` _part-type-or-part-label_` 有不同的解释： 
    * MBR：参数被用作为` _分区类型_`，可选值为 `primary`，`extended` 或 `logical`。
    * GPT：参数被用作为 `_part-label_`，即分区的 [PARTLABEL](</wzh/index.php?title=PARTLABEL&action=edit&redlink=1> "PARTLABEL（页面不存在）") 参数。如果想不设置分区标签，可以使用引上的空字符（`""`）。

**注意：** 网上的很多教程对 GPT 也使用了 `mkpart primary` 开头的错误命令，这一命令会将分区标签设置为“primary”。

  * `_fs-type_` 是 `help mkpart` 命令显示的标识符中最接近使用的文件系统的一项。 _mkpart_ 命令并不会创建文件系统：` _fs-type_` 参数只是简单地被 _parted_ 用于为 GPT 分区设置[分区类型 GUID](<https://en.wikipedia.org/wiki/GUID_Partition_Table#Partition_type_GUIDs> "wikipedia:GUID Partition Table") 或是为 MBR 分区设置[分区类型 ID](<https://en.wikipedia.org/wiki/Partition_type> "wikipedia:Partition type")。

**提示：** _parted_ 将 Linux 原生文件系统都映射为同一“Linux 文件系统”分区类型（GUID `0FC63DAF-8483-4772-8E79-3D69D8477DE4` 或是 ID `0x83`），所以可以安全地进行例如为 _ext4_ 格式的分区使用 `ext2` 类型的操作。

  * `_start_` 是相对于设备起始位置的分区开始位置，由一个数字加上[单位](<https://www.gnu.org/software/parted/manual/parted.html#unit>)组成，例如 `1MiB` 值从 1 MiB 的位置开始。
  * `_end_` 是相对于设备起始位置的分区结束位置（ _不是_ 从 `_start_` 的值开始）。它的格式与 `_start_` 相同，例如 `100%` 表示到设备的末端（使用所有剩余空间）。

**提示：**

  * 对于使用 MBR 分区表的硬盘，建议在硬盘末端留下至少 33 个 512-byte 扇区（16.5 KiB）的未分区空间，以保证 [ MBR 与 GPT 间转换](<../zh-cn/GPT_fdisk.html#%E5%9C%A8_MBR_%E5%92%8C_GPT_%E4%B9%8B%E9%97%B4%E8%BD%AC%E6%8D%A2> "Gdisk")的兼容性。
  * 为了不留空隙，分区的开始和结束应该首尾相连。

**注意：**

  * _parted_ 不支持指定一个分区相对于前一个分区的开始和结束位置。参见 [bug #59176](<https://debbugs.gnu.org/cgi/bugreport.cgi?bug=59176>) 和 [bug #55841](<https://debbugs.gnu.org/cgi/bugreport.cgi?bug=55841>).
  * _parted_ 可能会报出以下错误：

    Warning: The resulting partition is not properly aligned for best performance.
    Ignore/Cancel?
    
在这种情况下，请参考[分区#分区对齐](<../zh-cn/%E5%88%86%E5%8C%BA.html#%E5%88%86%E5%8C%BA%E5%AF%B9%E9%BD%90> "分区")并参照[#对齐](<#%E5%AF%B9%E9%BD%90>)进行修复。

下列命令将包含 `/boot` 目录的分区标记为可启动： 
    
    (parted) set _partition_ boot on
    
  * `_partition_` 是要标记的分区编号（参考 `print` 命令的输出）。
  * `esp` 是 GPT 上 `boot` 的别名。[[2]](<https://www.gnu.org/software/parted/manual/html_node/set.html>)

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 讲解 `boot`，`legacy_boot` 和 `esp` 标记及它们在 MBR 和 GPT 上的不同用例。 (在 [Talk:Parted](<../zh-cn/Talk:Parted.html>) 中讨论)

####  UEFI/GPT 示例

在每一个实例上都需要一个特殊的 [EFI 系统分区](<../zh-cn/EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA.html> "EFI 系统分区")。 

首先需要一个 [EFI 系统分区](<../zh-cn/EFI_system_partition.html> "EFI system partition").如果是和 Windows 双系统启动，此分区已经存在，不要重新创建。 

使用如下命令创建新的 EFI 系统分区（建议至少 1 GiB）： 
    
    (parted) mkpart "EFI system partition" fat32 1MiB 1025MiB
    (parted) set 1 esp on
    
剩下的空间可以随你决定，例如完全用在根分区上： 
    
    (parted) mkpart "root partition" ext4 1025MiB 100%
    (parted) type 2 4F68BCE3-E8CD-4DB1-96E7-FBCAF984B709
    
如果要拆分为 swap （4 GiB）和 `/`（剩余所有空间）两个分区： 
    
    (parted) mkpart "swap partition" linux-swap 1025MiB 5121MiB
    (parted) mkpart "root partition" ext4 5121MiB 100%
    (parted) type 3 4F68BCE3-E8CD-4DB1-96E7-FBCAF984B709
    
如果要拆分为 swap（4 GiB），`/`（32 GiB）和 `/home`（剩余所有空间）三个分区： 
    
    (parted) mkpart "swap partition" linux-swap 1025MiB 5121MiB
    (parted) mkpart "root partition" ext4 5121MiB 37889MiB
    (parted) type 3 4F68BCE3-E8CD-4DB1-96E7-FBCAF984B709
    (parted) mkpart "home partition" ext4 37889MiB 100%
    (parted) set 4 linux-home on
    
####  BIOS/MBR 示例

最简单的方案是使用如下命令创建使用所有空间的单一主分区： 
    
    (parted) mkpart primary ext4 1MiB 100%
    (parted) set 1 boot on
    
在下面的示例中，将创建一个 4 GiB 的交换分区，然后使用所有剩余空间创建一个 `/` 分区： 
    
    (parted) mkpart primary linux-swap 1MiB 4097MiB
     parted) mkpart primary ext4 4097MiB 100%
    (parted) set 2 boot on
    
在下面的最后一个示例中，将创建独立的 `/boot` (1 GiB)、swap (4 GiB)、`/` (32 GiB) 和 `/home`（所有剩余空间）分区： 
    
    (parted) mkpart primary ext4 1MiB 1025MiB
    (parted) set 1 boot on
    (parted) set 1 bls_boot on
    (parted) mkpart primary linux-swap 1025MiB 5121MiB
    (parted) mkpart primary ext4 5121MiB 37889MiB
    (parted) mkpart primary ext4 37889MiB 100%
    
###  调整分区

**警告：** ext2/3/4 分区在调整前需要先卸载并停止使用。编辑使用中的系统的根分区会非常困难和危险，建议使用安装介质/救援系统进行操作。

**注意：**

  * `parted` 只能移动分区的末端。
  * parted v3.2 _resizepart_ 可能需要用到[#交互模式](<#%E4%BA%A4%E4%BA%92%E6%A8%A1%E5%BC%8F>)。[[3]](<https://bugs.launchpad.net/ubuntu/+source/parted/+bug/1270203>)
  * 这些说明适用于使用 ext2，ext3 或 ext4 文件系统的分区。

如果要扩展分区，必须先调整分区的大小，然后调整其上文件系统的大小；如果要缩小分区，必须先调整文件系统的大小，再调整分区，以避免数据丢失。 

####  扩展分区

在 parted 交互模式下扩展分区，使用： 
    
    (parted) resizepart _number_ _end_
    
其中 `_number_` 是您正在扩展的分区的编号，而 `_end_` 是该分区的新末端（需要大于旧的末端）。 

要扩展分区上的 ext2/3/4 文件系统，使用如下命令（如果没有指定 `_size_`，默认值为分区的大小）： 
    
    # resize2fs /dev/_sdaX_ _size_
    
要扩展 Btrfs 文件系统： 
    
    # btrfs filesystem resize _size_ _/path/to/mount/point_
    
其中 `_/path/to/mount/point_` 代表要扩展的分区的挂载点，` _size_` 是新大小（格式如 `16G`）或是修改值（格式如 `+1G`）。使用 `max` 可以填充分区中的所有剩余空间。 

####  缩小分区

缩小分区上的 ext2/3/4 文件系统： 
    
    # resize2fs /dev/_sdaX_ _size_
    
**注意：** 与 parted 不同，[resize2fs(8)](<https://man.archlinux.org/man/resize2fs.8>) 使用 K，M，G 和 T 指代 KiB，MiB，GiB 和 TiB。注意，[e2fsprogs](<https://archlinux.org/packages/?name=e2fsprogs>)包 文档错误地将 kibibytes，mebibytes，gibibytes 和 tebibytes 称为“kilobytes，megabytes，gigabytes，terabytes 的二次方"。

缩小 Btrfs 文件系统： 
    
    # btrfs filesystem resize _size_ _/path/to/mount/point_
    
其中 `_/path/to/mount/point_` 代表要缩小的分区的挂载点，而 `_size_` 是该分区的新大小。 

然后在 parted 交互模式下缩小分区： 
    
    (parted) resizepart _number_ _end_
    
其中 `_number_` 是要缩小的分区的编号，而 `_end_` 是该分区的新末端（需要小于旧末端）。 

完成后，使用 [util-linux](<https://archlinux.org/packages/?name=util-linux>)包 中的 _resizepart_ 命令告诉内核新的分区大小： 
    
    # resizepart _device_ _number_ _size_
    
其中 `_device_` 是保存分区的设备，` _number_` 是分区的编号， `_size_` 是格式为 512 字节扇区的分区新大小。 

##  已知问题

除非命令本身就具有危险性（例如 _rm_ ， _mklabel_ 和 _mkpart_ ），Parted 始终会在进行具有潜在危险性的操作前发出警告。 

###  对齐

**警告：** _parted_ 仅对齐分区起始端，不对齐大小。这一特性不符合 dm-crypt/LUKS 的需求，详细信息请参考 [Advanced Format#Partition alignment](<../zh-cn/Advanced_Format.html#Partition_alignment> "Advanced Format")。

在创建分区时， _parted_ 可能会对分区未对齐发出警告，但不会对正确对齐的分区发出提示。例如： 
    
    (parted) mkpart primary fat16 0 32M
    Warning: The resulting partition is not properly aligned for best performance.
    Ignore/Cancel?                                                     
    
这一警告意味着分区的起始端未对齐。输入“Ignore”来无视警告，以扇区为格式输出分区表来查看起始端位置，以舍入到 2 次方的值递增作为起始端移除并重建分区，直到警告停止。 举个例子，在具有 512B 扇区的闪存盘上，Parted 期望扇区的起始位置为 2048 的乘积，即 1 MiB 对齐。 

如果你希望 _parted_ 自动计算正确的对齐值，可以使用 0% 而不是特定值作为起始端。例如，如果要创建一个大 ext4 分区，可以使用如下命令： 
    
    (parted) mkpart primary ext4 0% 100%
    
##  小技巧

### Check alignment

**警告：** _parted_ 仅验证分区起始端是否对齐，而不验证大小。这一特性不符合 dm-crypt/LUKS 的需求，详细信息请参考 [Advanced Format#Partition alignment](<../zh-cn/Advanced_Format.html#Partition_alignment> "Advanced Format")。

在已分区的硬盘上，你可以用 _parted_ 验证单个分区是否对齐。例如，要验证 `/dev/sda` 上的分区 1，可以使用如下命令： 
    
    # parted /dev/sda
    (parted) align-check optimal 1
    1 aligned
    
##  参考

  * [GNU parted - Parted 用户手册](<https://www.gnu.org/software/parted/manual/>)
  * [How to align partitions for best performance using parted](<https://rainbow.chard.org/2013/01/30/how-to-align-partitions-for-best-performance-using-parted/>)
  * [调整 ext3/ext4 分区大小](<http://positon.org/resize-an-ext3-ext4-partition>)
  * [GParted 官方论坛](<http://gparted-forum.surf4.info/>)
