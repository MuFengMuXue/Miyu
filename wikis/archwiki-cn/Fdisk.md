**翻译状态：**

  * 本文（或部分内容）译自 [fdisk](<https://wiki.archlinux.org/title/fdisk> "arch:fdisk")，最近一次同步于 2026-04-08，若英文版本有所[更改](<https://wiki.archlinux.org/title/fdisk?diff=0&oldid=869036>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/fdisk_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [文件系统](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html> "文件系统")
  * [GPT fdisk](<../zh-cn/GPT_fdisk.html> "GPT fdisk")
  * [Parted](<../zh-cn/Parted.html> "Parted")
  * [分区](<../zh-cn/%E5%88%86%E5%8C%BA.html> "分区")
  * [dd](<../zh-cn/Dd.html> "Dd")

[util-linux fdisk](<https://git.kernel.org/cgit/utils/util-linux/util-linux.git/>) 是基于命令行界面的分区表创建和编辑工具。一个硬盘需要分为一个或多个分区，这个信息被记录在分区表里面。 

本文介绍 3 种有着不同交互界面的分区工具： 

  * [fdisk(8)](<https://man.archlinux.org/man/fdisk.8>)——常用的命令行分区工具（对话式交互）。
  * [sfdisk(8)](<https://man.archlinux.org/man/sfdisk.8>)——支持脚本的分区工具，可用于自动配置和备份、恢复分区。
  * [cfdisk(8)](<https://man.archlinux.org/man/cfdisk.8>)——操作简单方便的 TUI 分区工具。

##  安装

要使用 _fdisk_ 及相关工具，请使用 [util-linux](<https://archlinux.org/packages/?name=util-linux>)包 软件包，这个软件包是 [base](<https://archlinux.org/packages/?name=base>)包 [元软件包](<../zh-cn/%E5%85%83%E8%BD%AF%E4%BB%B6%E5%8C%85%E5%92%8C%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%BB%84.html> "元软件包")的依赖。 

##  显示分区

要列出[块设备](<../zh-cn/%E8%AE%BE%E5%A4%87%E6%96%87%E4%BB%B6.html#%E5%9D%97%E8%AE%BE%E5%A4%87> "块设备")上的分区表和分区，可以运行以下命令，其中设备的名称类似于 `/dev/sda`、`/dev/nvme0n1`、`/dev/mmcblk0` 等： 
    
    # fdisk -l /dev/sda
    
**注意：** 如果未指定设备， _fdisk_ 将列出 `/proc/partitions` 中的所有分区。

##  备份和恢复分区表

在对硬盘做出更改之前，您可能需要备份硬盘的分区表和分区方案。您还可以使用备份将同一分区布局复制到多个硬盘上。 

对于GPT和MBR，您可以使用“sfdisk”将设备的分区布局保存到具有`-d`/`--dump` 选项的文件中. 对设备 `/dev/sda`运行以下命令: 
    
    # sfdisk -d /dev/sda > sda.dump
    
对于大小为 1 GiB 的单个 ext4 分区，该文件应如下所示： 
    
    sda.dump
    
    label: gpt
    label-id: AAAAAAAA-BBBB-CCCC-DDDD-EEEEEEEEEEEE
    device: /dev/sda
    unit: sectors
    first-lba: 34
    last-lba: 1048576
    sector-size: 512
    
    /dev/sda1 : start=2048, size=1048576, type=0FC63DAF-8483-4772-8E79-3D69D8477DE4, uuid=BBF1CD36-9262-463E-A4FB-81E32C12BDE7

要稍后恢复此布局，可以运行： 
    
    # sfdisk /dev/sda < sda.dump
    
##  创建分区表和分区

硬盘[分区](<../zh-cn/%E5%88%86%E5%8C%BA.html> "分区")的第一步是创建分区表。然后，根据所需的[分区方案](<../zh-cn/%E5%88%86%E5%8C%BA.html#%E5%88%86%E5%8C%BA%E6%96%B9%E6%A1%88> "分区")创建实际分区。参见[分区表](<../zh-cn/%E5%88%86%E5%8C%BA.html#%E5%88%86%E5%8C%BA%E8%A1%A8> "分区表")一文来帮助你选择使用 [MBR](<../zh-cn/%E5%88%86%E5%8C%BA.html#%E4%B8%BB%E5%BC%95%E5%AF%BC%E8%AE%B0%E5%BD%95> "MBR") 或是 [GPT](<../zh-cn/%E5%88%86%E5%8C%BA.html#GUID_%E5%88%86%E5%8C%BA%E8%A1%A8> "GPT")。 

在开始之前，您可能希望[备份](<#%E5%A4%87%E4%BB%BD%E5%92%8C%E6%81%A2%E5%A4%8D%E5%88%86%E5%8C%BA%E8%A1%A8>)您当前的分区表和方案。 

_fdisk_ 会自动在 2048 个 512 字节扇区（1 MiB）块大小基础上自动进行分区对齐，这应该与所有使用[先进格式化](<../zh-cn/%E5%85%88%E8%BF%9B%E6%A0%BC%E5%BC%8F%E5%8C%96.html> "先进格式化")的 HDD 和绝大多数 [SSD](<../zh-cn/%E5%9B%BA%E6%80%81%E7%A1%AC%E7%9B%98.html> "SSD") 兼容。这意味着默认设置会自动使用正确的对齐方式。 

To use _fdisk_ , run the program with the name of the [block device](<../zh-cn/Block_device.html> "Block device") you want to change/edit. This example uses `/dev/sda`: 

要使用 _fdisk_ ，需带上你想要更改/编辑的[块设备](<../zh-cn/%E8%AE%BE%E5%A4%87%E6%96%87%E4%BB%B6.html#%E5%9D%97%E8%AE%BE%E5%A4%87> "块设备")的名字来运行程序。在本例中我们使用 `/dev/sda`： 
    
    # fdisk /dev/sda
    
这将启动 _fdisk_ 程序，您可以在其中键入命令。 

###  创建新的分区表

**警告：** 如果在存有数据的硬盘上创建新分区表，它将擦除硬盘上的所有数据。请务必确保这是你想要做的

**提示：**

  * 分区前，请检查 NVMe 硬盘和高级格式硬盘是否使用了[最佳逻辑扇区大小](<../zh-cn/%E5%85%88%E8%BF%9B%E6%A0%BC%E5%BC%8F%E5%8C%96.html> "先进格式化")。
  * 在固态硬盘（SSD）上分区前应考虑[清空 SSD 存储单元](</wzh/index.php?title=SSD_memory_cell_clearing&action=edit&redlink=1> "SSD memory cell clearing（页面不存在）")。

要创建一个新的分区表并清除当前所有的分区信息，请在提示符下输入 `g` 以新建一个 GUID 分区表（[GPT](<../zh-cn/%E5%88%86%E5%8C%BA.html#GUID_%E5%88%86%E5%8C%BA%E8%A1%A8> "GPT")）或输入 `o` 新建一个 [MBR](<../zh-cn/%E5%88%86%E5%8C%BA.html#%E4%B8%BB%E5%BC%95%E5%AF%BC%E8%AE%B0%E5%BD%95> "MBR") 分区表。若已创建所需的分区表，请跳过此步骤。 

###  创建分区

使用 `n` 命令创建分区。需要输入分区编号，起始扇区和结束扇区。对于 MBR 类型分区，还可能需要输入分区类型。 

**注意：** 分区大小和位置的选择请参考 [分区#分区方案](<../zh-cn/%E5%88%86%E5%8C%BA.html#%E5%88%86%E5%8C%BA%E6%96%B9%E6%A1%88> "分区")。

####  分区类型

使用 MBR 时， _fdisk_ 会询问 MBR 分区的类型。输入 `p` 创建主分区，输入 `e` 创建扩展分区，最多可以创建四个主分区。 

_fdisk_ 默认不询问分区类型 ID，而是直接使用 'Linux filesystem'，稍后可[修改](<#%E4%BF%AE%E6%94%B9%E5%88%86%E5%8C%BA%E7%B1%BB%E5%9E%8B>)该 ID。 

####  分区编号

分区编号是分区在硬盘中的编号，例如硬盘 `/dev/sda` 的 `1` 号分区为 `/dev/sda1`，对于 `/dev/nvme0n1` 是 `/dev/nvme0n1p1`，而 `/dev/mmcblk0` 则是 `/dev/mmcblk0p1`。有关命名方案的详细信息请参阅[设备分区名](<../zh-cn/%E8%AE%BE%E5%A4%87%E6%96%87%E4%BB%B6.html#%E5%88%86%E5%8C%BA> "设备文件")。分区的编号可能不与硬盘上的分区顺序一致，请参考[分区排序](<#%E5%88%86%E5%8C%BA%E6%8E%92%E5%BA%8F>)。 

建议使用 _fdisk_ 推荐的默认编号。 

####  起始和结束扇区

起始扇区必须使用绝对扇区号。结束扇区可使用绝对扇区号或以这些单位指定：`K`、`M`、`G`、`T` 或 `P`。 

结束扇区的位置可以是： 

  * 从硬盘起始位置开始的绝对位置。例如，`40M` 作为起始扇区，指定了距硬盘开头 40 MiB 的位置。
  * 在 `**+**_size_` 或 `**-**_size_` 后接大小的相对位置。例如，使用 `+2G` 以指定位于起始扇区之后 2 GiB 的位置，或使用 `-200M` 以指定位于最后一个可用扇区之前 200 MiB 的位置。

未输入扇区位置的指定值而直接按 `Enter` 键将使用默认值，对于起始扇区是最大可用块的开始位置，对于结束扇区则是最大可用块的结束位置。 

**注意：**

  * 分区时，使用起始分区的默认值总是个不错的选择。此外，确保指定分区大小时使用 `+_size{M,G,T,P}_` ，不要使用小于 1 MiB 的大小。此类分区始终根据设备属性对齐。
  * [EFI 系统分区](<../zh-cn/EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA.html> "EFI 系统分区")需要 `EFI System` 类型的分区。
  * 将 GRUB 安装到基于 BIOS 系统的 GPT 分区的设备上时，[GRUB](<../zh-cn/GRUB.html> "GRUB") 需要一个 `BIOS boot` 类型的 [BIOS 启动分区](<../zh-cn/GRUB.html#GUID_%E5%88%86%E5%8C%BA%E8%A1%A8_\(GPT\)_%E7%89%B9%E6%AE%8A%E6%93%8D%E4%BD%9C> "GRUB")。

**提示：** 在使用 MBR 分区表的硬盘上，需在硬盘末尾保留至少 33 个 512 字节扇区大小（16.5 KiB）的未分区空间以便[在 MBR 与 GPT 分区表之间转换](<../zh-cn/GPT_fdisk.html#%E5%9C%A8_MBR_%E5%92%8C_GPT_%E4%B9%8B%E9%97%B4%E8%BD%AC%E6%8D%A2> "Gdisk")。

重复此过程，直到获得所需的分区。 

###  修改分区类型

每个分区都有类型，MBR 使用[分区 ID](<https://en.wikipedia.org/wiki/Partition_type> "wikipedia:Partition type") 进行定义; GPT 使用[分区类型 GUID](<https://en.wikipedia.org/wiki/GUID_Partition_Table#Partition_type_GUIDs> "wikipedia:GUID Partition Table") 进行定义。 

按下 `t` 修改分区类型，可以使用以下别名指定常用分区类型： 

  * `uefi`： [ESP](<../zh-cn/EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA.html> "ESP")
  * `xbootldr`： XBOOTLDR 分区
  * `home`：[home](<../zh-cn/%E5%88%86%E5%8C%BA.html#/home> "分区") 分区
  * `swap`： [swap](<../zh-cn/Swap.html> "Swap") 交换分区
  * `linux`：用于其它分区

**提示：**

  * 按下 `L` 可以显示 fdisk 的内部码表。
  * 在使用 GPT 时，建议遵循 [可侦测分区标准](<https://uapi-group.org/specifications/specs/discoverable_partitions_specification/>)，以使用 [GPT 自动挂载](<../zh-cn/Systemd.html#GPT%E5%88%86%E5%8C%BA%E8%87%AA%E5%8A%A8%E6%8C%82%E8%BD%BD> "Systemd")功能。

###  将 MBR 分区设为可启动

输入 `a` 可以将一个 MBR 分区设置为[可启动（即活动）](<https://en.wikipedia.org/wiki/Boot_flag> "wikipedia:Boot flag")分区。 

###  检查并写入分区表更改

  * 使用 `p` 显示更改内容。
  * 使用 `q` 放弃更改。
  * 使用 `w` 将更改写入硬盘并退出程序。

##  移动分区

**警告：** 因为移动分区时需要重写全部的分区数据，所以要移动的分区必须先下线。移动分区的动作很慢且存在风险，强烈建议操作前进行备份。[sfdisk(8) § OPTIONS](<https://man.archlinux.org/man/sfdisk.8#OPTIONS>) 手册中有说明：“这个操作存在风险而且是非原子操作。”

要移动分区，先要准备足够的空余硬盘空间。如果需要，可以缩小分区及文件系统，请参考 [Parted#缩小分区](<../zh-cn/Parted.html#%E7%BC%A9%E5%B0%8F%E5%88%86%E5%8C%BA> "Parted")。要移动分区： 
    
    # echo '+_sectors_ ,' | sfdisk --move-data _device_ -N _number_
    
其中 `_sectors_` 是要偏移的扇区数，` _+_` 表示增加，` _device_` 是分区所在设备，` _number_` 是分区编号。如果在硬盘的开始或中间增加了分区，想重新编号，可以参考 [#分区排序](<#%E5%88%86%E5%8C%BA%E6%8E%92%E5%BA%8F>)或 _fdisk_ 的“额外功能”模式。 

##  提示和技巧

###  分区排序

这适用于在两个分区之间的空间中创建或删除了分区的情况。本例中使用了 `/dev/sda`。 
    
    # sfdisk -r /dev/sda
    
在调整分区顺序后，如果没有使用[块设备持久化命名](<../zh-cn/%E5%9D%97%E8%AE%BE%E5%A4%87%E6%8C%81%E4%B9%85%E5%8C%96%E5%91%BD%E5%90%8D.html> "块设备持久化命名")，则需要调整 `/etc/fstab`、`/etc/crypttab` 等使用分区编号的配置文件。 

**注意：** 内核必须读取新分区表才能让分区（例如 `/dev/sda1`）处于可访问状态，可以重启系统或让内核 [重新读取分区表](<https://serverfault.com/questions/36038/reread-partition-table-without-rebooting>)（即执行 `partprobe /dev/sda`）。

## cfdisk

[cfdisk(8)](<https://man.archlinux.org/man/cfdisk.8>) 提供了基于 [curses](<https://en.wikipedia.org/wiki/curses_\(programming_library\)> "w:curses \(programming library\)") 的 TUI，相比 fdisk 操作更简单方便，但也不支持 fdisk 在 extra/expert 下的大多数特性和功能。 cfdisk 的使用方式如下： 
    
    # cfdisk /dev/sda
    
  * 按下 `?` 显示帮助页面。
  * cfdisk 启动后，界面顶部会显示目前的分区情况。有着 `>>` 游标和反色背景的分区是被选中的分区。用户可以使用上下方向键来选择不同的分区。
  * 界面底部显示已被选中的分区的详细信息以及可用的命令列表。命令的帮助说明显示在命令的下方。使用左右方向键选择某个命令，按下 `Enter` 键执行。
  * 类似 fdisk，所有的操作都会按顺序列队并等待用户运行 `Write` 命令后才会真正执行并写入硬盘。用户可以随时丢弃任何修改并安全地退出程序。
  * 如果磁盘上还没有分区，cfdisk 会询问是否需要创建一个分区。如需要修改已有的分区表格式，则必须擦除硬盘内容或改用 fdisk [重建分区表](<#%E5%88%9B%E5%BB%BA%E6%96%B0%E7%9A%84%E5%88%86%E5%8C%BA%E8%A1%A8>)。

##  另见

  * [Managing partitions in Linux with fdisk](<https://www.redhat.com/sysadmin/partitions-fdisk>)
