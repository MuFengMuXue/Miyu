**翻译状态：**

  * 本文（或部分内容）译自 [RAID](<https://wiki.archlinux.org/title/RAID> "arch:RAID")，最近一次同步于 2025-07-15，若英文版本有所[更改](<https://wiki.archlinux.org/title/RAID?diff=0&oldid=840187>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/RAID_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [LVM on software RAID](</wzh/index.php?title=LVM_on_software_RAID&action=edit&redlink=1> "LVM on software RAID（页面不存在）")
  * [LVM#RAID](<../zh-cn/LVM.html#RAID> "LVM")
  * [Install Arch Linux with Fake RAID](<../zh-cn/Install_Arch_Linux_with_Fake_RAID.html> "Install Arch Linux with Fake RAID")
  * [Convert a single drive system to RAID](</wzh/index.php?title=Convert_a_single_drive_system_to_RAID&action=edit&redlink=1> "Convert a single drive system to RAID（页面不存在）")
  * [ZFS](<../zh-cn/ZFS.html> "ZFS")
  * [ZFS/虚拟磁盘](<../zh-cn/ZFS/%E8%99%9A%E6%8B%9F%E7%A3%81%E7%9B%98.html> "ZFS/虚拟磁盘")
  * [Swap#分片](<../zh-cn/Swap.html#%E5%88%86%E7%89%87> "Swap")
  * [Btrfs#RAID](<../zh-cn/Btrfs.html#RAID> "Btrfs")

独立磁盘冗余阵列 (**R** edundant **A** rray of **I** ndependent **D** isks，[RAID](<https://en.wikipedia.org/wiki/RAID> "wikipedia:RAID")) 是一种将多个磁盘驱动器组件（通常是多块硬盘或多个分区）组合为一个逻辑单元的存储技术。根据 RAID 的部署情况，这个逻辑单元可以是单个的文件系统，也可以是一个能在其上建立多个分区的透明中间层。 

根据所需的冗余量和性能要求，数据按照 [#RAID 级别](<#RAID_%E7%BA%A7%E5%88%AB>)中的某一种方式分布在驱动器中。所选的 RAID 级别决定了是否可以防止数据丢失（硬盘故障时）、是否提高性能或结合两者优势。 

本文介绍如何使用 [mdadm(8)](<https://man.archlinux.org/man/mdadm.8>) 创建并管理一个软件磁盘阵列。 

**警告：** 确保在操作前[备份](<../zh-cn/%E5%90%8C%E6%AD%A5%E5%92%8C%E5%A4%87%E4%BB%BD%E7%A8%8B%E5%BA%8F.html> "同步和备份程序")所有数据。

##  RAID 级别

尽管大部分 RAID 级别都或多或少地包含了数据冗余，RAID 并不能完全保证数据安全。如果遇到火灾、计算机被盗或者多块硬盘同时损坏，RAID 将无法保护数据。此外，配置一个带有 RAID 的系统是一个复杂的过程，可能会破坏现有数据。 

###  基本 RAID 级别

有多种不同的[基本 RAID 级别](<https://en.wikipedia.org/wiki/Standard_RAID_levels> "wikipedia:Standard RAID levels")，下面列出了最常用的几种。 

[RAID 0](<https://en.wikipedia.org/wiki/Standard_RAID_levels#RAID_0> "wikipedia:Standard RAID levels")
    将多块硬盘组合为一个条带卷'并不提供数据冗余 _（实际上会降低可靠性），但它仍可以被当做是 RAID，而且它确实提供了_ 巨幅的速度提升 _。如果提高速度比数据安全更重要（比如作为[swap](<../zh-cn/Swap.html> "Swap") 分区），可以选择这种 RAID 级别。在服务器上，RAID 1 和 RAID 5 阵列更加合适。在 RAID 0 阵列中，块设备的大小是最小组成分区的大小乘以组成分区的数量。_

[RAID 1](<https://en.wikipedia.org/wiki/Standard_RAID_levels#RAID_1> "wikipedia:Standard RAID levels")
    这是最直接的 RAID 级别：完全镜像。与其他 RAID 级别一样，它只在分区位于不同物理硬盘上才有效。如果某一块硬盘损坏，由 RAID 阵列提供的块设备将不受影响。可以使用 RAID 1 的情境包括了除 [swap](<../zh-cn/Swap.html> "Swap") 和临时文件外的其他所有情境。请注意，如果使用由软件实现的 RAID，引导分区只能选择 RAID 1，因为读取引导分区的引导器通常无法辨识 RAID，但一个 RAID 1 的组成分区可以像常规分区一样读取。RAID 1 阵列块设备的大小是最小组成分区的大小。

[RAID 5](<https://en.wikipedia.org/wiki/Standard_RAID_levels#RAID_5> "wikipedia:Standard RAID levels")
    需要至少 3 块物理硬盘，并结合了 RAID 1 的数据冗余和 RAID 0 的速度与可用空间上的优势。RAID 5 使用了类似 RAID 0 的条带化技术，同时也将奇偶校验块 _分布式地存储在每一块磁盘上_ 。如果遭遇硬盘损坏，这些奇偶校验块就可以用来在替代的新磁盘上重建损坏的数据。RAID 5 仅可弥补一个组成磁盘损坏带来的损失。
    
**注意：** RAID 5 是结合了速度与数据冗余优势的常用选择。但值得注意的是，当一块硬盘损坏而没有及时更换，此时若再有硬盘损坏，则所有数据都将丢失。此外，考虑到现代磁盘的超大容量和消费级硬盘无法恢复的读取错误率 (Unrecoverable read error, URE)，超过 4TiB 的阵列在重建数据时出现至少一处读取错误 (URE) 的概率几乎在**预料之中** （概率大于 50%）。因此，存储行业不再推荐使用 RAID 5。

[RAID 6](<https://en.wikipedia.org/wiki/Standard_RAID_levels#RAID_6> "wikipedia:Standard RAID levels")
    需要至少 4 块物理硬盘，提供了和 RAID 5 一样的优势并且在两块硬盘损坏时仍能保证数据安全。RAID 6 使用了和 RAID 5 类似的条带化技术，但是把两个不同的奇偶校验块 _分布式地存储在每一块磁盘上_ 。如果磁盘发生故障，这些奇偶校验块将用于重建替换磁盘上的数据。RAID 6 可以承担两个组成磁盘的损失。在抵御无法恢复的读取错误 (Unrecoverable read error, URE) 时也某种程度上更加可靠，因为磁盘阵列在重建某一块损坏硬盘的数据时仍然有奇偶校验块可以校验数据。但是，总体而言，RAID 6 开销较大，大多数时候 far2 布局的 RAID 10（参见下文）提供了更快的速度和更强的可靠性，因此更倾向于采用 RAID 10。

###  嵌套 RAID 级别

[RAID 1+0](<https://en.wikipedia.org/wiki/Nested_RAID_levels#RAID_10_.28RAID_1.2B0.29> "wikipedia:Nested RAID levels")
    RAID1+0 是一种结合了两种基本 RAID 级别的嵌套级别，它相对基本级别提高了性能且增加了冗余量。它通常被称为 _RAID10_ ，但是，Linux MD（内核自带的 RAID 实现）支持的 RAID10 不是简单的两层 RAID 重叠，请看下文。

[RAID 10](<https://en.wikipedia.org/wiki/Non-standard_RAID_levels#Linux_MD_RAID_10> "wikipedia:Non-standard RAID levels")
    Linux 下的 RAID10 建立在 RAID1+0 的概念上，但它将其实现为单一的一层，这一层可以有多种不同的布局。可参考[创建复杂 RAID 10](<https://www.suse.com/zh-cn/documentation/sles11/stor_admin/data/raidmdadmr10cpx.html>)。
    在 Y 块硬盘上的 _近 X 布局_ 在不同硬盘上重复储存每个数据块 X 次，但不需要 Y 可以被 X 整除。数据块放在所镜像的磁盘上几乎相同的位置，这就是 _近布局_ 名字的来源。它可以工作在任意数量的磁盘上，最少是 2 块。在 2 块硬盘上的近 2 布局相当于 RAID1，4 块硬盘上的近 2 布局相当于 RAID1+0。
    在 Y 块硬盘上的 _远 X 布局_ 设计用于在镜像阵列中提供与条带化技术一样快的读取速度。它通过把每块硬盘分成前后两部分来实现这一点，写入第一块硬盘前半部分数据也会写入第二块硬盘的后半部分，反之亦然。这样可以达到一个效果，那就是把对连续数据的读取条带化，而这正是 RAID0 和 RAID5 读取性能高的原因。它的缺点在于写入连续数据时有轻微性能损失，因为硬盘磁头要运动到另一片区域来写入镜像。当数据读取性能和可用性/冗余性一样重要时，比起 RAID1+0 **和** RAID5，更应该优先考虑远 2 布局的 RAID10。需注意这种方式仍无法代替备份。详情请阅读维基百科相关页面。

**警告：** mdadm cannot reshape arrays in _far X_ layouts which means once the array is created, you will not be able to `mdadm --grow` it. For example, if you have a 4x1TB RAID10 array and you want to switch to 2TB disks, your usable capacity will remain 2TB. For such use cases, stick to _near X_ layouts.

###  RAID 级别对比

RAID 级别 | 数据冗余 | 物理设备利用率 | 读取性能 | 写入性能 | 最少磁盘数量   
---|---|---|---|---|---  
**0** | 否 | 100% | n 倍 **最优** | n 倍 **最优** | 2   
**1** | 是 | 50% | 如果有多个进程同时读取，最多 n 倍，否则 1 倍  | 1 倍 | 2   
**5** | 是 | 67% - 94% | (n−1) 倍 **较优** | (n−1) 倍 **较优** | 3   
**6** | 是 | 50% - 88% | (n−2) 倍 | (n−2) 倍 | 4   
**10,far2** | 是 | 50% | n 倍 **最优;** 与 RAID0 相当但加入了数据冗余  | (n/2) 倍 | 2   
**10,near2** | 是 | 50% | 如果有多个进程同时读取，最多 n 倍，否则 1 倍 | (n/2) 倍 | 2   
  
* 其中 _n_ 表示用于组成阵列的磁盘数量。 

### LINEAR

**LINEAR** allows to map two or more devices into a single device, without parallel accesses like **RAID0** but allowing to fully use disks from different sizes. To create a pseudo RAID using this mode without _mdadm_ , one can either use the low-level [dmsetup(8)](<https://man.archlinux.org/man/dmsetup.8>) utility, the high-level [LVM](<../zh-cn/LVM.html> "LVM") framework or the [Btrfs](<../zh-cn/Btrfs.html> "Btrfs") filesystem. 

##  实现方式

RAID 设备可以用不同方式来管理： 

软件 RAID
    这是最简单的实现方式，因为它不依赖于专用固件或专有软件。这种阵列由操作系统通过以下方式进行管理： 

  * 通过抽象层管理（比如 [mdadm](<#%E5%AE%89%E8%A3%85>)）；

**注意：** 这是在本指南下文将要使用的方法。

  * 通过逻辑卷管理器来管理（比如 [LVM](<../zh-cn/LVM.html#RAID> "LVM")）；
  * 通过文件系统的某个组件来管理（比如 [ZFS](<../zh-cn/ZFS.html> "ZFS")，[Btrfs](<../zh-cn/Btrfs.html#RAID> "Btrfs")）。

硬件 RAID
    这种阵列由安装在计算机上的专用硬件卡直接管理，硬盘直接连接在该计算机上。RAID 的处理逻辑由板载的处理器完成，它独立于[主处理器 (CPU)](<https://en.wikipedia.org/wiki/Central_processing_unit> "wikipedia:Central processing unit")。尽管这种方案独立于任何操作系统，但却需要驱动程序来使硬件 RAID 控制器正常工作。取决于不同的制造商，硬件 RAID 阵列可以在 option ROM 里设置或者操作系统安装完成后另行安装配套软件来设置。这种设置是独立于 Linux 内核的：内核并不能看到单独的每块硬盘。

[FakeRAID](</wzh/index.php?title=Fakeraid&action=edit&redlink=1> "Fakeraid（页面不存在）")
    这种类型的 RAID 应当称为 BIOS 或板载 RAID，却常被错误地当做硬件 RAID 来宣传。这种阵列由伪 RAID 控制器来管理，RAID 逻辑由 option ROM 或在 [UEFI](<../zh-cn/UEFI.html> "UEFI") 情况下由[安装了 EFI Sata 驱动程序](<https://web.archive.org/web/20220505135824/https://www.win-raid.com/t19f13-Intel-EFI-quot-RaidDriver-quot-BIOS-Modules.html>)的固件本身来完成，但并不是实现了 _所有_ RAID 功能的完整硬件 RAID 控制器。因此，这种 RAID 有时被称为 FakeRAID。[dmraid](<https://archlinux.org/packages/?name=dmraid>)包 会被用于处理这种控制器。这里列出一些 FakeRAID 控制器：[Intel Rapid Storage](<https://en.wikipedia.org/wiki/Intel_Rapid_Storage_Technology> "wikipedia:Intel Rapid Storage Technology")，JMicron JMB36x RAID ROM，AMD RAID，ASMedia 106x 和 NVIDIA MediaShield。

###  我正在使用哪一种 RAID？

由于软件 RAID 是由用户部署的，因此用户很容易就知道 RAID 的类型。 

但是，辨别 FakeRAID 和真正的硬件 RAID 是很困难的。如上所述，制造商经常错误地混淆这两种类型的 RAID，还可能进行虚假宣传。这种情况下应该采取的最好方式是运行 `lspci` 命令并在输出信息中找到你的 RAID 控制器，然后根据这些信息进行更进一步的搜索。硬件 RAID 控制器会在这一列表中出现，但 FakeRAID 不会。同时，真正的硬件 RAID 控制器通常价格很高，如果这个系统是自行组装的，那么很可能安装一个硬件 RAID 会使电脑的价格显著提高。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [mdadm](<https://archlinux.org/packages/?name=mdadm>)包。 _mdadm_ 用于管理在纯块设备上建立起来的纯软件 RAID：底层硬件不提供任何 RAID 逻辑，只是一些磁盘而已。 _mdadm_ 可以在任何块设备集合上工作，甚至是那些非常规的设备。比如，你可以用一堆 U 盘来建立 RAID 阵列。 

###  准备设备

**警告：** 这些步骤会擦除指定设备上的所有数据，输入命令请小心！

如果设备是旧设备重用或刚从一个现有的阵列上拆下来，请擦除所有旧的 RAID 配置信息： 
    
     # mdadm --misc --zero-superblock /dev/_drive_
    
或者是删除设备上的某个特定的分区： 
    
     # mdadm --misc --zero-superblock /dev/_partition_
    
**注意：**

  * 清除一个分区的 superblock 不会影响到磁盘上的其他分区。
  * 考虑到 RAID 本身的功能特点，在运行中的磁盘阵列中完全地 [安全擦除磁盘](<../zh-cn/%E5%AE%89%E5%85%A8%E5%9C%B0%E6%93%A6%E9%99%A4%E7%A3%81%E7%9B%98.html> "安全地擦除磁盘") 是很困难的。请在创建阵列前考虑要不要安全擦除磁盘。
  * You can do the whole disk preparation procedure from a GUI with [blivet-gui](<https://aur.archlinux.org/packages/blivet-gui/>)AUR.

###  对磁盘进行分区

强烈推荐对用于阵列的硬盘进行分区。考虑到大多数 RAID 用户会用到超过 2 TiB 的硬盘，因此推荐并要求使用 GPT。参阅[分区](<../zh-cn/%E5%88%86%E5%8C%BA.html> "分区")获取关于磁盘分区的更多信息以及可供使用的[分区工具](<#%E5%88%86%E5%8C%BA%E5%B7%A5%E5%85%B7>)。 

**注意：** 也可以在裸磁盘（没有分区的磁盘）上直接创建 RAID，但不推荐这么做，因为这样可能会导致更换损坏硬盘时出现问题

**注意：** 当更换 RAID 中的某块损坏的硬盘时，新硬盘的大小必须恰好等于或大于损坏的硬盘，否则无法完成阵列重建过程。即使是同一厂商相同型号的硬盘也可能有容量上的细微差别。通过在磁盘末尾保留一些未分配的空间可以消除磁盘容量上的细微差异，这样可以使替代磁盘的型号选择更加容易。因此，最好在磁盘末尾留出大约 100 MiB 的未分配空间。

####  GUID 分区表

  * 创建分区以后，这些分区的[类型标识符 (GUID)](<https://en.wikipedia.org/wiki/GUID_Partition_Table#Partition_type_GUIDs> "wikipedia:GUID Partition Table") 应该是 `A19D880F-05FC-4D3B-A006-743F0F84911E`（在 _fdisk_ 里将分区类型改为 `Linux RAID` 或在 _gdisk_ 里改为 `FD00` 可以给所选分区分配这个标识符）。
  * 如果使用了一个更大的磁盘阵列，可以考虑分配[文件系统标签](<../zh-cn/Persistent_block_device_naming.html#by-label> "Persistent block device naming")[[损坏的链接](<../Project:%E7%A4%BE%E7%BE%A4%E9%A6%96%E9%A1%B5.html#%E6%8D%9F%E5%9D%8F%E7%9A%84%E9%93%BE%E6%8E%A5> "Project:社群首页")：无效的章节] 或[分区标签](<../zh-cn/Persistent_block_device_naming.html#by-partlabel> "Persistent block device naming")[[损坏的链接](<../Project:%E7%A4%BE%E7%BE%A4%E9%A6%96%E9%A1%B5.html#%E6%8D%9F%E5%9D%8F%E7%9A%84%E9%93%BE%E6%8E%A5> "Project:社群首页")：无效的章节] 用于以后区分每块单独的硬盘。
  * 建议在每个设备上创建大小相同的分区。

####  主引导记录 (MBR)

对于在使用 MBR 的硬盘上创建分区的用户，可用的[分区类型 ID](<https://en.wikipedia.org/wiki/Partition_type> "wikipedia:Partition type") 包括： 

  * `0xDA`：无文件系统（ _fdisk_ 中称为 `Non-FS data`）。这是**推荐** 用于 Arch Linux 上 RAID 阵列的 mdadm 分区类型。
  * `0xFD`：自动检测的 RAID（ _fdisk_ 中称为 `Linux RAID autodetect`）。This partition type should only be used if RAID autodetection is desireable (non-[initramfs](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#initramfs> "Initramfs") system, old mdadm metadata format).

更多信息请参阅 [Linux Raid Wiki:Partition Types](<https://raid.wiki.kernel.org/index.php/Partition_Types>)。 

###  创建阵列

使用 `mdadm` 来创建阵列。参阅 [mdadm(8)](<https://man.archlinux.org/man/mdadm.8>) 获取支持的选项。下面列出部分使用范例。 

**警告：** 不要简单地复制/粘贴下面的示例，确保你已经使用正确的选项和设备名称替代了示例中相应的内容。

**注意：**

  * 如果有一个从 [Syslinux](<../zh-cn/Syslinux.html> "Syslinux") 启动的 RAID1 阵列，在 syslinux v4.07 中要求元数据值为 1.0，而不是默认的 1.2。
  * 当用 [Arch 安装镜像](<../zh-cn/Archiso.html> "Archiso") 创建磁盘阵列时，请使用 `--homehost=_yourhostname_` 选项设置 [主机名](</wzh/index.php?title=Hostname&action=edit&redlink=1> "Hostname（页面不存在）")（或者 `--homehost=any` 选项无论在什么主机上都用相同的主机名），否则主机名称 `archiso` 会被写入阵列的元数据中。

**提示：** 要为 RAID 设备指定一个自定义的名称，可以使用 `--name=_MyRAIDName_` 选项或将 RAID 设备路径改为 `/dev/md/_MyRAIDName_`。Udev 会使用该名称创建指向 `/dev/md/` 内 RAID 阵列的符号链接。如果 `homehost` 与当前 [主机名](</wzh/index.php?title=Hostname&action=edit&redlink=1> "Hostname（页面不存在）") 匹配（或者 homehost 设为了 `any`）则链接将会是 `/dev/md/_name_`，如果 homehost 不匹配那么链接将会是 `/dev/md/_homehost_ :_name_`。

下面这个例子展示了在 2 个设备上建立 RAID1 阵列： 
    
     # mdadm --create --verbose --level=1 --raid-devices=2 /dev/md/MyRAID1Array /dev/sdb1 /dev/sdc1
    
下面这个例子展示了使用 4 块磁盘作为工作 (active) 磁盘，1 块作为备用 (spare) 磁盘建立 RAID5 阵列： 
    
     # mdadm --create --verbose --level=5 --raid-devices=4 /dev/md/MyRAID5Array /dev/sdb1 /dev/sdc1 /dev/sdd1 /dev/sde1 --spare-devices=1 /dev/sdf1
    
**提示：**`--chunk` 可用于修改默认的区块大小。更多关于优化区块大小的内容请参阅 [Chunks: the hidden key to RAID performance](<https://www.zdnet.com/article/chunks-the-hidden-key-to-raid-performance/>)。

下面这个例子展示了在 2 个设备上建立远 2 布局的 RAID10 阵列 (RAID10, far2)： 
    
     # mdadm --create --verbose --level=10 --raid-devices=2 --layout=f2 /dev/md/MyRAID10Array /dev/sdb1 /dev/sdc1
    
这样，阵列就会在虚拟设备 `/dev/mdX` 下建立起来，容量已经合并且可以使用（但处于降级模式）。mdadm 在后台同步数据时你已经可以直接开始使用这个阵列了。储存奇偶校验位可能要花很长时间，可以用这个命令查看进度： 
    
    $ cat /proc/mdstat
    
###  更新配置文件

默认情况下，`mdadm.conf` 中的大部分内容都被注释掉了，它应该只包含如下内容： 
    
    /etc/mdadm.conf
    
    ...
    DEVICE partitions
    ...
    
这一指令告诉 mdadm 检查由 `/proc/partitions` 引用的所有设备并尽可能将其中的阵列组合起来。如果你确实想启动所有可用的阵列并且确信不存在意料之外的超级块（比如安装了新的存储设备），那么这样的配置就很好。当然有一种更精准的控制方法，就是显式地将阵列添加到 `/etc/mdadm.conf`： 
    
    # mdadm --detail --scan >> /etc/mdadm.conf
    
这将会在配置中添加类似这样的内容： 
    
    /etc/mdadm.conf
    
    ...
    DEVICE partitions
    ...
    ARRAY /dev/md/MyRAID1Array metadata=1.2 name=pine:MyRAID1Array UUID=27664f0d:111e493d:4d810213:9f291abe

这也会使 mdadm 检查由 `/proc/partitions` 引用的设备。但是，只有超级块的 UUID 是 `27664…` 的设备才会被组合成激活的阵列。 

更多信息请参阅 [mdadm.conf(5)](<https://man.archlinux.org/man/mdadm.conf.5>)。 

###  组合成磁盘阵列

更新配置文件后即可用 mdadm 组合磁盘阵列： 
    
    # mdadm --assemble --scan
    
###  格式化 RAID 上的文件系统

**提示：** To create multiple volumes inside a RAID array, follow the [LVM on software RAID](</wzh/index.php?title=LVM_on_software_RAID&action=edit&redlink=1> "LVM on software RAID（页面不存在）") article.

现在磁盘阵列已经可以像普通分区一样被格式化成某个[文件系统](<../zh-cn/File_systems.html> "File systems")，但要记住： 

  * 不是所有文件系统都支持超大分区（参阅 [Wikipedia:Comparison of file systems#Limits](<https://en.wikipedia.org/wiki/Comparison_of_file_systems#Limits> "wikipedia:Comparison of file systems")）。
  * 文件系统需要支持在线增大和收缩（参阅 [Wikipedia:Comparison of file systems#Features](<https://en.wikipedia.org/wiki/Comparison_of_file_systems#Features> "wikipedia:Comparison of file systems")）。
  * 应合理计算跨度大小和带区宽度来获得最佳性能。

####  计算 stride（跨度大小）和 stripe width（带区宽度）

优化文件系统结构以适应底层 RAID 结构需要 2 个参数： _stride_ 和 _stripe width_ 。它们对应于 RAID 的 _chunk size（区块大小）_ 、文件系统的 _block size（块大小）_ 以及 _"data disks"（数据盘）的数量_ 。 

Chunk size（RAID 区块大小）是 RAID 阵列的一个属性，在阵列创建时就已经定好了。目前 `mdadm` 默认该值为 512 KiB。这个参数可以用 `mdadm` 读取： 
    
    # mdadm --detail /dev/mdX | grep 'Chunk Size'
    
Block size（块大小）是文件系统的一个属性，在文件系统创建时就已经定好了。在大部分文件系统上（包括 ext4）默认是 4 KiB。更多关于当前系统 ext4 的信息可以查看 `/etc/mke2fs.conf` 文件。 

"Data disks"（数据盘）的数量指的是阵列能够完全重建数据所要求的最少可用设备。例如，对于 N 个设备的 raid0 来说这个数量是 N，对于 raid5 来说是 N-1。 

当你获得了这三个参数时，stride 和 stripe width 可以用下列公式来计算： 
    
    stride = chunk size / block size
    stripe width = number of data disks * stride
    
#####  范例 1. RAID0

本范例使用了正确的 stride 和 stripe width 将合并后的分区格式化成了 ext4： 

  * 假设这一 RAID0 阵列是由 2 块物理硬盘组成的。
  * Chunk size（RAID 区块大小）是 512 KiB。
  * Block size（文件系统块大小）是 4 KiB。

因为 stride = chunk size / block size。在这个例子中，stride 大小是 512/4 = 128。 

因为 stripe width = # of physical **data** disks * stride。在这个例子中，stripe width 的大小是 2*128 = 256。 
    
     # mkfs.ext4 -v -L myarray -b 4096 -E stride=128,stripe-width=256 /dev/md0
    
#####  范例 2. RAID5

本范例使用了正确的 stride 和 stripe width 将合并后的分区格式化成了 ext4： 

  * 假设这一 RAID5 阵列由 4 块物理硬盘组成，3 块是数据盘，1 块是奇偶校验盘。
  * Chunk size（RAID 区块大小）是 512 KiB。
  * Block size（文件系统块大小）是 4 KiB。

因为 stride = chunk size / block size。在这个例子中，stride 大小是 512/4 = 128。 

因为 stripe width = # of physical **data** disks * stride。在这个例子中，stripe width 的大小是 3*128 = 384. 
    
     # mkfs.ext4 -v -L myarray -b 4096 -E stride=128,stripe-width=384 /dev/md0
    
关于 stride 和 stripe width 的更多信息，请参阅：[RAID Math](<https://wiki.centos.org/HowTos/Disk_Optimization>)。 

#####  范例 3. RAID10,far2

本范例使用了正确的 stride 和 stripe width 将合并后的分区格式化成了 ext4： 

  * 假设这一 RAID10 阵列由 2 块物理硬盘组成。考虑到远 2 布局的 RAID10 的自身特性，两块硬盘都是数据盘。
  * Chunk size（RAID 区块大小）是 512 KiB。
  * Block size（文件系统块大小）是 4 KiB。

因为 stride = chunk size / block size。 在这个例子中，stride 大小是 512/4 = 128。 

因为 stripe width = # of physical **data** disks * stride。 在这个例子中，stripe width 的大小是 2*128 = 256。 
    
     # mkfs.ext4 -v -L myarray -b 4096 -E stride=128,stripe-width=256 /dev/md0
    
##  在 Live CD 中挂载 RAID

如果你需要在 Live CD 中挂载 RAID 分区，用这个命令： 
    
     # mdadm --assemble /dev/md _number_ /dev/_disk1_ /dev/_disk2_ /dev/_disk3_ /dev/_disk4_
    
如果缺一块盘的 RAID 1 被错误地识别为了 RAID 1（参照 `mdadm --detail /dev/md _number_`）并报告为非活动状态（参照 `cat /proc/mdstat`），需要先停止磁盘阵列： 
    
     # mdadm --stop /dev/md _number_
    
##  在 RAID 上安装 Arch Linux

**注意：** 本节仅适用于根文件系统在磁盘阵列上的情况。如果你的磁盘阵列上只是一个数据分区，那么可以跳过本节。

你应该在安装过程中的[分区](<../zh-cn/%E5%88%86%E5%8C%BA.html> "分区")和[格式化](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html#%E5%88%9B%E5%BB%BA%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "文件系统")步骤之间创建 RAID 阵列。这将会把一个位于 RAID 阵列上的分区格式化成根文件系统，而不是直接格式化一个分区。 按照 [#安装](<#%E5%AE%89%E8%A3%85>)一节的步骤创建 RAID 阵列。，然后继续安装过程，直到 pacstrap 步骤完成。 当使用 [UEFI 启动](<../zh-cn/UEFI.html> "UEFI")时，还需要阅读 [EFI 系统分区#ESP在软RAID1上](<../zh-cn/EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA.html#ESP%E5%9C%A8%E8%BD%AFRAID1%E4%B8%8A> "EFI 系统分区")。 

###  更新配置文件

**注意：** 这些操作应该在 chroot 以外完成，因此要在文件路径前加上 `/mnt`。

在基本系统安装完成以后，RAID 的默认配置文件 `mdadm.conf` 需要这样来更新： 
    
    # mdadm --detail --scan >> /mnt/etc/mdadm.conf
    
在运行这个命令以后一定要用文本编辑器检查 `mdadm.conf` 配置文件来确保它的内容看起来是合理的。 

**注意：** 为防止系统启动时 `mdmonitor.service` 启动失败（由 udev 启动），你需要取消 `MAILADDR` 的注释，并且在 `mdadm.conf` 结尾留下可处理磁盘阵列出错通知的邮件地址和/或应用程序。参阅 [#启用事件邮件通知](<#%E5%90%AF%E7%94%A8%E4%BA%8B%E4%BB%B6%E9%82%AE%E4%BB%B6%E9%80%9A%E7%9F%A5>)。

现在继续安装过程直到 [安装指南#关于 initramfs](<../zh-cn/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97.html#%E5%85%B3%E4%BA%8E_initramfs> "安装指南") 步骤之前为止，然后按照下一节的步骤做。 

###  配置 mkinitcpio

**注意：** 这些操作应该在 chroot 时完成。

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [mdadm](<https://archlinux.org/packages/?name=mdadm>)包，并向 `mkinitcpio.conf` 中的[钩子](<../zh-cn/Mkinitcpio.html#%E9%92%A9%E5%AD%90\(HOOKS\)> "Mkinitcpio")数组添加 `mdadm_udev` 来为初始化内存盘添加 mdadm 支持： 
    
    /etc/mkinitcpio.conf
    
    ...
    HOOKS=(base udev autodetect microcode modconf kms keyboard keymap consolefont block **mdadm_udev** filesystems fsck)
    ...

然后[重新生成初始化内存盘](<../zh-cn/Mkinitcpio.html#%E5%88%9B%E5%BB%BA%E5%92%8C%E5%90%AF%E7%94%A8%E9%95%9C%E5%83%8F> "Mkinitcpio")。 

**注意：** 每次修改 `/etc/mdadm.conf` 都需要重新生成 initramfs。

###  配置引导加载器

####  根设备

将 `root` 参数指向映射的磁盘，例如： 
    
    root=/dev/md/_MyRAIDArray_
    
如果按上述用内核设备节点来指定映射磁盘的方法之后，从软件 RAID 分区启动失败了，那就用[块设备持久化命名](<../zh-cn/%E5%9D%97%E8%AE%BE%E5%A4%87%E6%8C%81%E4%B9%85%E5%8C%96%E5%91%BD%E5%90%8D.html> "块设备持久化命名")中的某种方法来指定映射的磁盘，例如： 
    
    root=LABEL=Root_Label
    
参考 [GRUB#RAID](<../zh-cn/GRUB.html#RAID> "GRUB")。 

#### RAID0 layout

**注意：** This also affects existing mdraid RAID0 users that upgrade from an older version of the Linux kernel to 5.3.4 or newer.

Since version 5.3.4 of the Linux kernel, you need to explicitly tell the kernel which RAID0 layout should be used: RAID0_ORIG_LAYOUT (`1`) or RAID0_ALT_MULTIZONE_LAYOUT (`2`).[[1]](<https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=c84a1372df929033cb1a0441fb57bd3932f39ac9>) You can do this by providing the [kernel parameter](<../zh-cn/Kernel_parameter.html> "Kernel parameter") as follows: 
    
    raid0.default_layout=2
    
The correct value depends upon the kernel version that was used to create the raid array: use `1` if created using kernel 3.14 or earlier, use `2` if using a more recent version of the kernel. One way to check this is to look at the creation time of the raid array: 
    
    mdadm --detail /dev/md1
    
    /dev/md1:
               Version : 1.2
         Creation Time : Thu Sep 24 10:17:41 2015
            Raid Level : raid0
            Array Size : 975859712 (930.65 GiB 999.28 GB)
          Raid Devices : 3
         Total Devices : 3
           Persistence : Superblock is persistent
    
           Update Time : Thu Sep 24 10:17:41 2015
                 State : clean
        Active Devices : 3
       Working Devices : 3
        Failed Devices : 0
         Spare Devices : 0
    
            Chunk Size : 512K
    
    Consistency Policy : none
    
                  Name : archiso:root
                  UUID : 028de718:20a81234:4db79a2c:e94fd560
                Events : 0
    
        Number   Major   Minor   RaidDevice State
           0     259        2        0      active sync   /dev/nvme0n1p1
           1     259        6        1      active sync   /dev/nvme2n1p1
           2     259        5        2      active sync   /dev/nvme1n1p2
    
Here we can see that this raid array was created on September 24, 2015. The release date of Linux Kernel 3.14 was March 30, 2014, and as such this raid array is most likely created using a multizone layout (`2`). 

##  维护 RAID

###  数据清扫 (Scrubbing)

定期运行数据[清扫 (Scrubbing)](<https://en.wikipedia.org/wiki/Data_scrubbing> "wikipedia:Data scrubbing") 来检查并修复错误是一种很好的做法。一次完整数据清扫可能会花费数个小时，具体取决于磁盘阵列的大小和配置。 

启动数据清扫： 
    
    # echo check > /sys/block/mdX/md/sync_action
    
数据检查操作会扫描驱动器来检查坏扇区并自动修复它们。如果找到了包含损坏数据的好扇区（本扇区中的数据与另一块硬盘中记录本扇区应有的数据不符，例如奇偶校验块和另一块数据块相结合可以证明本数据块是错误的），那就不动作，但记录下这一事件（见下文）。这种“不动作”允许管理员自行检查坏扇区中原本的数据和从冗余数据中重建的数据，然后决定保留哪个。 

与许多 mdadm 相关的任务/事项一样，数据清扫的进度也可以通过查看 `/proc/mdstat` 文件来查询。 

例如： 
    
    $ cat /proc/mdstat
    
    Personalities : [raid6] [raid5] [raid4] [raid1]
    md0 : active raid1 sdb1[0] sdc1[1]
          3906778112 blocks super 1.2 [2/2] [UU]
          [>....................]  check =  4.0% (158288320/3906778112) finish=386.5min speed=161604K/sec
          bitmap: 0/30 pages [0KB], 65536KB chunk

安全地停止当前的数据清扫操作： 
    
    # echo idle > /sys/block/md0/md/sync_action
    
**注意：** 如果在数据清扫暂停时重启了系统，将继续进行清扫。

数据清扫完成后，管理员可以检查有多少数据块（如果有的话）被标记为坏块： 
    
    # cat /sys/block/md0/md/mismatch_cnt
    
####  关于数据清扫的一般说明

**注意：** 用户也可以 echo **repair** 到 `/sys/block/md0/md/sync_action` 里面，但是这是不明智的，因为一旦遇到数据不一致就被自动改写为一致。危险之处在于我们实际并不知道奇偶校验块和数据块哪个是对的（在 RAID1 中是不知道哪个数据块是对的）。因此自动清扫操作能不能用正确数据替换错误数据取决于运气。

以 root 身份设定一个 cron 任务来定期执行清扫是很好的。[raid-check](<https://aur.archlinux.org/packages/raid-check/>)AUR 会对此有所帮助。如果要用 systemd 定时器而不是 cron 来执行定期清扫，[raid-check-systemd](<https://aur.archlinux.org/packages/raid-check-systemd/>)AUR 中包含了相同的脚本和配套的 systemd 定时器单元文件。 

**注意：** 对于常规的大容量驱动器，清扫工作耗时大约 **6 秒每 GB** （即每 TB 大约需要 1 小时 45 分钟），因此应合理确定 cron 任务或定时器的开始时间。

####  对清扫 RAID1 和 RAID10 的说明

由于 RAID1 和 RAID10 本质上就是没有数据缓冲的，所以即使阵列工作正常，它的不匹配计数仍然可能是个非零值。这些不匹配计数只存在于正在写入数据的区域，且它们不反映任何问题。但是，我们无法区分非零的不匹配计数到底代表正在写入数据还是确实存在问题。这是造成 RAID1 和 RAID10 阵列误报错误的根源。即使如此，仍然建议定期清扫以发现并纠正驱动器上可能出现的坏扇区。 

###  从阵列中移除设备

要从阵列中移除一个[块设备](<../zh-cn/%E8%AE%BE%E5%A4%87%E6%96%87%E4%BB%B6.html#%E5%9D%97%E8%AE%BE%E5%A4%87> "设备文件")，先将这个设备标记为 faulty（故障）： 
    
     # mdadm --fail /dev/md0 /dev/_failing_array_member_
    
现在从阵列中移除这个设备： 
    
     # mdadm --remove /dev/md0 /dev/_failing_array_member_
    
If the device has not failed entirely, but you would like to replace it, e.g. because it looks like it is dying, you can actually handle replacement more gracefully by first adding a new drive and then telling mdadm to replace it. 

For example, with `/dev/sdc1` as the new one and `/dev/sdb1` as the failing one: 
    
    # mdadm /dev/md0 --add /dev/sdc1
    # mdadm /dev/md0 --replace /dev/sdb1 --with /dev/sdc1
    
The `--with /dev/sdc1` part is optional, but more explicit. See [[2]](<https://unix.stackexchange.com/questions/74924/how-to-safely-replace-a-not-yet-failed-disk-in-a-linux-raid5-array/104052#104052>) for more details. 

永久移除设备（比如想把一个设备拿出来单独使用）： 先使用上述两个命令，然后： 
    
    # mdadm --zero-superblock /dev/_failing_array_member_
    
**警告：**

  * 不要在 RAID0 阵列或者其他线性存放数据的阵列中进行这个操作！否则数据会丢失！
  * 重新使用已经移除的硬盘却不清除它的超级块将会导致下次启动时丢失所有数据。（因为 mdadm 将会把它当做磁盘阵列的一部分来使用）。

停止使用某个阵列： 

  1. 卸载 (umount) 目标阵列
  2. 用这个命令停止磁盘阵列运行：`mdadm --stop /dev/md0`
  3. 将本节开头的三个命令在每块硬盘上都运行一遍。
  4. 将 `/etc/mdadm.conf` 中的相关行移除。

###  向阵列中添加设备

可以在系统正在运行且设备已经挂载的情况下使用 mdadm 添加新设备。 按照前文所述的方法，使用现有阵列中相同的布局对新设备进行分区。 

如果 RAID 阵列尚未组合，先组合它们： 
    
    # mdadm --assemble /dev/md0 /dev/sda1 /dev/sdb1
    
向阵列中添加新设备： 
    
    # mdadm --add /dev/md0 /dev/sdc1
    
这一步 mdadm 不会花费很长时间。 

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** A `--backup-file` should be created prior to `grow` (在 [Talk:RAID#Add a drive (RAID5, RAID6)](</wzh/index.php?title=Talk:RAID&action=edit&redlink=1> "Talk:RAID（页面不存在）") 中讨论)

根据不同的 RAID 类型（比如 RAID1），mdadm 可能会把部分设备添加为备用设备，而不在这些设备上存放数据。可以使用 `--grow` 加上 `--raid-devices` 选项来增加 RAID 利用的磁盘数量。例如，将一个阵列增加至四块硬盘： 
    
    # mdadm --grow /dev/md0 --raid-devices=4
    
可以这样检查进度： 
    
    # cat /proc/mdstat
    
用这个命令检查已经添加的设备： 
    
    # mdadm --misc --detail /dev/md0
    
**注意：** 对于 RAID0 设备可能会收到以下错误信息： 
    
    mdadm: add new device failed for /dev/sdc1 as 2: Invalid argument
    
这是由于上述命令会将新磁盘添加为 "spare"（备用）盘，但是 RAID0 中不存在备用盘。如果想往 RAID0 阵列中添加磁盘，你需要同时使用 "grow" 和 "add" 参数。如下所示： 
    
    # mdadm --grow /dev/md0 --raid-devices=3 --add /dev/sdc1

###  增大 RAID 卷的大小

如果给阵列安装了更大的磁盘，或者增大了分区大小，可能就需要增大 RAID 卷的大小以适应更大的可用空间。这一过程可用首先按照上文中关于更换磁盘的步骤来做。当 RAID 卷在更大的磁盘上重建完成后，这个卷需要 "grow" 来填充多出来的空间。 
    
    # mdadm --grow /dev/md0 --size=max
    
接着，在 RAID 卷 `/dev/md0` 上的现有分区可能需要调整大小。参阅[分区](<../zh-cn/%E5%88%86%E5%8C%BA.html> "分区")获取更多信息。最后，上述分区上的文件系统也需要重新调整大小。如果用 `gparted` 来完成分区操作，这些都会自动完成。如果用的是其他工具，请手动卸载 (unmount) 文件系统并调整其大小。 
    
    # umount /storage
    # fsck.ext4 -f /dev/md0p1
    # resize2fs /dev/md0p1
    
###  修改同步速度限制

同步工作需要一定的时间。如果本机不需要完成其他任务，可以提高速度限制值。 
    
    # cat /proc/mdstat
    
     Personalities : [raid10]
     md127 : active raid10 sdd1[3] sdc1[2] sdb1[1] sda1[0]
         31251490816 blocks super 1.2 512K chunks 2 far-copies [4/4] [UUUU]
         [=>...................]  resync =  5.2% (1629533760/31251490816) finish=2071.7min speed=238293K/sec
         bitmap: 221/233 pages [884KB], 65536KB chunk

In the above example, it would seem the max speed is limited to approximately 238 M/sec. 

查看当前速度限制（单位为 KiB/s）： 
    
    # sysctl dev.raid.speed_limit_min
    
    dev.raid.speed_limit_min = 1000
    
    # sysctl dev.raid.speed_limit_max
    
    dev.raid.speed_limit_max = 200000

Set a new maximum speed of raid resyncing operations using [sysctl](<../zh-cn/Sysctl.html> "Sysctl"): 
    
    # sysctl -w dev.raid.speed_limit_min=600000
    # sysctl -w dev.raid.speed_limit_max=600000
    
然后查看同步速度和预计完成时间： 
    
    # cat /proc/mdstat
    
      Personalities : [raid10]
     md127 : active raid10 sdd1[3] sdc1[2] sdb1[1] sda1[0]
         31251490816 blocks super 1.2 512K chunks 2 far-copies [4/4] [UUUU]
         [=>...................]  resync =  5.3% (1657016448/31251490816) finish=1234.9min speed=399407K/sec
         bitmap: 221/233 pages [884KB], 65536KB chunk

### RAID5 performance

To improve RAID5 performance for fast storage (e.g. [NVMe](</wzh/index.php?title=NVMe&action=edit&redlink=1> "NVMe（页面不存在）")), increase `/sys/block/mdx/md/group_thread_cnt` to more threads. For example, to use 8 threads to operate on a RAID5 device: 
    
    # echo 8 > /sys/block/md0/md/group_thread_cnt
    
See [git kernel commit 851c30c9badf](<https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=851c30c9badfc6b294c98e887624bff53644ad21>). 

### Update RAID superblock

To update the RAID superblock, you need to first unmount the array and then stop the array with the following command: 
    
    # mdadm --stop /dev/md0
    
Then you can update certain parameters by reassembling the array. For example, to update the `homehost`: 
    
    # mdadm --assemble --update=homehost --homehost=NAS /dev/md0 /dev/sda1 /dev/sdb1
    
See the arguments of `--update` for details. 

##  监视运行情况

可以显示当前 RAID 设备状态的一行简单命令： 
    
    # awk '/^md/ {printf "%s: ", $1}; /blocks/ {print $NF}' </proc/mdstat
    
    md1: [UU]
    md0: [UU]
    
###  用 watch 监视 mdstat
    
    # watch -t 'cat /proc/mdstat'
    
或者最好用 [tmux](<https://archlinux.org/packages/?name=tmux>)包
    
    # tmux split-window -l 12 "watch -t 'cat /proc/mdstat'"
    
###  用 iotop 追踪 IO

[iotop](<https://archlinux.org/packages/?name=iotop>)包 可以显示各个进程的输入输出状态。请用这个命令来查看 RAID 线程的输入输出。 
    
     # iotop -a $(sed 's/^/-p /g' <<<`pgrep "_raid|_resync|jbd2"`)
    
###  用 iostat 追踪 IO

[sysstat](<https://archlinux.org/packages/?name=sysstat>)包 包中的 _iostat_ 实用程序可以显示各个设备和分区的输入输出统计。 
    
    # iostat -dmy 1 /dev/md0
    # iostat -dmy 1 # all
    
### mdadm via systemd

_mdadm_ provides the [systemd](<../zh-cn/Systemd.html> "Systemd") service `mdmonitor.service` which can be useful for monitoring the health of your raid arrays and notifying you if anything goes wrong. 

This service is special in that it cannot be manually activated like a regular service; _mdadm_ will take care of activating it via udev upon assembling your arrays on system startup, but it will **only** do so if an email address and/or program has been configured for its notifications (see below). 

###  启用事件邮件通知

_mdadm_ 提供了名为 `mdmonitor.service` 的 [systemd](<../zh-cn/Systemd.html> "Systemd") 服务，可帮助监控 RAID 阵列的健康度，并在出现问题时通过邮件通知你。 

这个服务较为特殊，它无法用通常的方法来激活；**仅** 在 _mdadm_ 按下面的步骤为通知配置邮件地址后，它才会在系统启动阶段组装阵列时，通过 udev 激活该服务。 

**警告：** 邮件地址配置错误会导致监控服务启动静默失败。

**注意：** 在发送邮件前，需要有一个配置好的[邮件传输代理](</wzh/index.php?title=Mail_transfer_agent&action=edit&redlink=1> "Mail transfer agent（页面不存在）")。

通过编辑 `/etc/mdadm.conf` 并配置邮件地址来启用该功能：MAILADDR _user@domain_

接下来，通过如下命令来验证功能是否正常： 
    
    # mdadm --monitor --scan --oneshot --test
    
如果测试成功并邮件正常送达，则配置完成；在下次阵列完成组装时，`mdmonitor.service` 将开始监控阵列错误。 

#### Program notifications

Like Email notification above, edit `/etc/mdadm.conf` and edit the line: 
    
    PROGRAM /usr/sbin/handle-mdadm-events
    
The argument for PROGRAM is the script you want to run for any event. Which then interact with proper network monitoring agents. Or even IM clients or push notification services like ntfy.sh for home users. 

Test in the same way as for email notification above. 

##  故障排除

如果你在重启计算机时遇到类似 "invalid raid superblock magic" 的错误，并且除了已经配置好的硬盘外又接了其他硬盘，请检查硬盘顺序是不是正确的。在安装 RAID 时，硬盘编号可能是 hdd、hde 和 hdf，但是重启后它们的编号可能变成了 hda、hdb 和 hdc。请相应地调整你的内核参数。这种情况经常发生。 

###  Error: "kernel: ataX.00: revalidation failed"

如果你突然（在重启、修改 BIOS 设置后）遇到类似错误信息： 
    
    Feb  9 08:15:46 hostserver kernel: ata8.00: revalidation failed (errno=-5)
    
这并不意味着设备已经损坏。尽管你可能会在网上看到一些讲内核崩溃的链接指向最坏的结果，但总而言之，并不是内核崩溃。可能你不知怎么的在 BIOS 里或内核参数里修改了 APIC 或 ACPI 设置。把它改回来就好了。通常关闭 APIC 和/或 ACPI 就好了。 

###  磁盘阵列以只读模式启动

当由 md 启动磁盘阵列时，超级块将被改写，数据同步可能已经开始了。要以只读模式启动，可以向内核模块 `md_mod` 传递参数 `start_ro`。设置了这个参数以后，新的磁盘阵列进入 'auto-ro' 模式，该模式停止了所有内部读写操作（更新超级块、再同步、数据恢复），并且会在第一个写入请求到来时自动切换至 'rw' （读写）模式。 

**注意：** 在第一个写入请求到来前使用 `mdadm --readonly` 命令可以将阵列设置为真正的 'ro' （只读）模式，还可以用 `mdadm --readwrite` 命令直接开始再同步而不用等待写入请求。

要在启动时设置该参数，在内核启动参数中添加 `md_mod.start_ro=1`。 

或者通过[内核模块#使用 /etc/modprobe.d/中的文件](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html#%E4%BD%BF%E7%94%A8_/etc/modprobe.d/%E4%B8%AD%E7%9A%84%E6%96%87%E4%BB%B6> "内核模块")在模块加载时传递该参数，也可以直接从 `/sys/` 传递： 
    
    # echo 1 > /sys/module/md_mod/parameters/start_ro
    
###  在损坏或缺失磁盘的情况下恢复 RAID

当磁盘阵列中的一个驱动器由于任何原因损坏时，也可能会发生上述错误。如果在缺失一块硬盘的情况下你仍需要强制启动磁盘阵列，输入以下命令（根据实际修改）： 
    
    # mdadm --manage /dev/md0 --run
    
现在你应该可以用类似下面的命令来挂载它（如果在 fstab 里有它的话）： 
    
    # mount /dev/md0
    
现在磁盘阵列应该已经工作并且可以使用，但仍旧是缺一块盘的状态。因此需要按照上文 [#准备设备](<#%E5%87%86%E5%A4%87%E8%AE%BE%E5%A4%87>)所述再添加一个磁盘分区，然后就可以将新磁盘分区加入到磁盘阵列中： 
    
    # mdadm --manage --add /dev/md0 /dev/sdd1
    
如果输入： 
    
    # cat /proc/mdstat
    
你就能看到磁盘阵列已经激活并正在重建。 

你可能还需要更新你的配置文件（参阅：[#更新配置文件](<#%E6%9B%B4%E6%96%B0%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6>)）。 

##  基准测试

用于 RAID 基准测试的工具有很多种。不同 RAID 最显著的不同是多个线程在读取 RAID 卷时的速度提升程度。 

[bonnie++](<https://archlinux.org/packages/?name=bonnie%2B%2B>)包 测试对一个或多个数据库类型文件的读写，以及对小文件的创建、读取、删除，这样可以模拟 Squid、INN 和 Maildir format e-mail 等程序的文件读写。其附带的 [ZCAV](<https://www.coker.com.au/bonnie++/zcav/>) 程序可以测试硬盘不同区域的性能，且不用向硬盘写入任何数据。 

**不应该** 使用 [hdparm](<../zh-cn/Hdparm.html> "Hdparm") 来对 RAID 进行基准测试，因为它多次返回的结果会非常不一致。 

##  参考资料

  * [Linux kernel RAID documentation](<https://docs.kernel.org/admin-guide/md.html>)
  * [Linux Software RAID](<https://www.thomas-krenn.com/en/wiki/Linux_Software_RAID>) (thomas-krenn.com)
  * [Linux RAID wiki entry](<https://archive.kernel.org/oldwiki/raid.wiki.kernel.org/>) in The Linux kernel archives
  * [How Bitmaps Work](<https://raid.wiki.kernel.org/index.php/Write-intent_bitmap>)
  * [Chapter 19. Managing RAID](<https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/managing_storage_devices/managing-raid_managing-storage-devices#overview-of-raid_managing-raid>) of Red Hat Enterprise Linux 9 documentation
  * [Linux-RAID FAQ](<https://tldp.org/FAQ/Linux-RAID-FAQ/x37.html>) on the Linux documentation project
  * [BAARF](<https://web.archive.org/web/20160114023340/http://www.miracleas.com/BAARF/>)(Archive.org) including _[Why should I not use RAID 5?](<https://web.archive.org/web/20160112115539/http://www.miracleas.com/BAARF/RAID5_versus_RAID10.txt>)_(Archive.org) by Art S. Kagel
  * [Introduction to RAID](<https://web.archive.org/web/20190425050953/http://www.linux-mag.com/id/7924/>), [Nested-RAID: RAID-5 and RAID-6 Based Configurations](<https://web.archive.org/web/20190224110216/http://www.linux-mag.com/id/7931/>), [Intro to Nested-RAID: RAID-01 and RAID-10](<https://web.archive.org/web/20190501235404/http://www.linux-mag.com/id/7928>), and [Nested-RAID: The Triple Lindy](<https://web.archive.org/web/20190501212610/http://www.linux-mag.com/id/7932/>) in Linux Magazine
  * [HowTo: Speed Up Linux Software Raid Building And Re-syncing](<https://www.cyberciti.biz/tips/linux-raid-increase-resync-rebuild-speed.html>)
  * [Wikipedia:Non-RAID drive architectures](<https://en.wikipedia.org/wiki/Non-RAID_drive_architectures> "wikipedia:Non-RAID drive architectures")

**邮件列表**

  * [Kernel Linux-Raid mailing list](<mailto:linux-raid@vger.kernel.org>)

**mdadm**

  * [mdadm source code](<https://www.kernel.org/pub/linux/utils/raid/mdadm/>)
  * [Software RAID on Linux with mdadm](<https://web.archive.org/web/20180624104254/http://www.linux-mag.com/id/7939/>) in Linux Magazine
  * [Wikipedia - mdadm](<https://en.wikipedia.org/wiki/mdadm> "wikipedia:mdadm")

**论坛帖子**

  * [Raid Performance Improvements with bitmaps](<https://forums.overclockers.com.au/threads/mdadm-bitmap.865333/>)
  * [GRUB and GRUB2](<https://bbs.archlinux.org/viewtopic.php?id=125445>)
  * [Can't install grub2 on software RAID](<https://bbs.archlinux.org/viewtopic.php?id=123698>)
  * [Use RAID metadata 1.2 in boot and root partition](<https://forums.gentoo.org/viewtopic-t-888624-start-0.html>)
