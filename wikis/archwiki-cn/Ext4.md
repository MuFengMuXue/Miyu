**翻译状态：**

  * 本文（或部分内容）译自 [Ext4](<https://wiki.archlinux.org/title/Ext4> "arch:Ext4")，最近一次同步于 2024-06-10，若英文版本有所[更改](<https://wiki.archlinux.org/title/Ext4?diff=0&oldid=736163>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Ext4_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [文件系统](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html> "文件系统")
  * [Ext3](</wzh/index.php?title=Ext3&action=edit&redlink=1> "Ext3（页面不存在）")

来自 [Ext4 - Linux Kernel Newbies](<https://kernelnewbies.org/Ext4>)： 

    Ext4 是最常用的 Linux 文件系统 Ext3 的进化。在许多方面，Ext4对于 Ext3 有着比 Ext3 对于 Ext2 更多更深的改变。Ext3 主要是向 Ext2 添加了日志系统，而 Ext4 修改了重要的文件系统的数据结构，比如用来存储文件数据的那部分。当然结果就是文件系统有更好的设计，更好的性能，稳定性还有更多的功能。

##  创建 ext4 文件系统

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [e2fsprogs](<https://archlinux.org/packages/?name=e2fsprogs>)包。 

要格式化分区，使用： 
    
    # mkfs.ext4 /dev/_分区_
    
**提示：**

  * 更多选项参见 [mke2fs(8)](<https://man.archlinux.org/man/mke2fs.8>)；编辑 `/etc/mke2fs.conf` 可以查看/修改默认配置。
  * 如果支持，可以启用[元数据校验和](<#%E5%9C%A8%E7%8E%B0%E6%9C%89%E7%9A%84%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F%E4%B8%AD%E5%90%AF%E7%94%A8%E5%85%83%E6%95%B0%E6%8D%AE%E6%A0%A1%E9%AA%8C%E5%92%8C>)。

###  Bytes-per-inode 比例

来自 [mke2fs(8)](<https://man.archlinux.org/man/mke2fs.8>): 

     _**mke2fs** 在硬盘上为每个bytes-per-inode大小的空间创建一个 inode. B_ytes-per-inode _的比例越大, 创建的 inode 就越少._

创建新文件、目录、符号链接等都需要至少一个空闲的 [inode](<https://en.wikipedia.org/wiki/Inode> "wikipedia:Inode")。如果 inode 数过低，即使文件系统中仍有空间也无法创建文件。 

由于无法在创建文件系统后修改 bytes-per-inode 比例以及 inode 数量, `mkfs.ext4` 默认使用更低的 inode 比例，即每 16384 bytes (16 KiB) 一个 inode 以避免这个问题. 

然而，对于一个具有对于大小为数百或数千GB、平均文件大小为兆字节的分区，这通常会导致 inode 过大，因为创建的文件数永远不会达到 inode 数。 

这样的结果是浪费硬盘空间, 因为这些未使用的 inode 每个都会占用文件系统 256 bytes 的空间 (这是在 `/etc/mke2fs.conf` 中设置的，但是不应该改变). 256 * 数百万 = 许多GB在未使用的节点中被浪费了. 

这种情况可以通过比较以下几点进行评价， `Use%` 以及 `IUse%` 由 `df` 和 `df -i` 提供: 
    
    $ df -h /home
    
    Filesystem              Size    Used   Avail  **Use%**   Mounted on
    /dev/mapper/lvm-home    115G    56G    59G    **49%**    /home
    
    $ df -hi /home
    
    Filesystem              Inodes  IUsed  IFree  **IUse%**  Mounted on
    /dev/mapper/lvm-home    1.8M    1.1K   1.8M   **1%**     /home
    
要指定一个不同的 Bytes-per-inode 比率，你可以使用 `-T _usage-type_` 选项，将会使用`/etc/mke2fs.conf`中定义的类型，表示文件系统预期的用法。 在这些类型中较大的 `largefile` 和 `largefile4` 将提供更相关联的比例，即每 1 MiB 或 4 MiB 一个 inode。 
    
    # mkfs.ext4 -T largefile /dev/_device_
    
Bytes-per-inode 比例可以直接通过 `-i` 选项设定: _e.g._ 使用 `-i 2097152` 对应 2 MiB 的比例以及 `-i 6291456` 对应 6 MiB 的比例. 

**提示：** 相反地，如果你需要建立一个分区用于存放数百万计的小文件（例如邮件或新闻组项目）你可以使用更小的 _usage-type_ 值，例如 `news` (每 4096 bytes 一个 节点) 或者 `small` (相同但更小的 inode 和 block 大小).

**警告：** 如果你大量使用符号链接，请确保保持足够高的 inode 数和较低的 bytes-per-inode，因为符号链接虽然不会占用更多的空间，但每一个新的符号链接都会消耗一个新的 inode，因此文件系统中的 inode 可能会被很快用完。

###  保留块

默认情况下，5% 的文件系统块会被预留给超级用户，以避免碎片化并“ _允许由 root 拥有的守护程序在非特权进程被阻止向文件系统写入后继续正常运行_ ”（来自 [mke2fs(8)](<https://man.archlinux.org/man/mke2fs.8>)）。 

对于现在的大容量磁盘，如果分区被用于长期存储或对系统运作并非至关重要（例如 `/home`），这将比必要的大小更大。查看[这封邮件](<https://www.redhat.com/archives/ext3-users/2009-January/msg00026.html>)，可以了解ext4 的开发者 Ted Ts'o 对保留块的看法 ，以及[这个 superuser 的回答](<https://superuser.com/questions/1256074/how-much-space-to-leave-free-on-hdd-or-ssd/1257550#1257550>)，为这个话题提供了一般的背景信息。 

如果分区满足以下条件之一，则通常可以放心缩小保留块的比例： 

  * 非常大（例如 > 50G）
  * 用于长期存储，即文件不会被非常频繁地创建和删除

在 ext4 相关的实用程序中可以使用 `-m` 选项指定保留块的比例。 

要在创建文件系统时不创建保留块，使用： 
    
    # mkfs.ext4 -m 0 /dev/_设备_
    
要在之后将比例改为 1%，使用： 
    
    # tune2fs -m 1 /dev/_设备_
    
要将保留块空间设置为以千兆字节为单位的绝对大小，使用 `-r`: 
    
    # tune2fs -r $((_ngigs_ * 1024**3 / _blocksize_)) /dev/_设备_
    
`_blocksize_` 是文件系统中的块大小，以字节为单位。它几乎总是4096，但你可以检查以确保无误： 
    
    # tune2fs -l /dev/_设备_ | grep 'Block size:'
    
    Block size:               4096
    
$(()) 语法用于数学扩展。这个语法在 [bash](<https://archlinux.org/packages/?name=bash>)包 和 [zsh](<https://archlinux.org/packages/?name=zsh>)包中有效，但在 [fish](<https://archlinux.org/packages/?name=fish>)包中不适用。 对于 fish，应使用以下语法： 
    
    # tune2fs -r (math 'ngigs * 1024^3 / blocksize') /dev/_设备_
    
这些命令可以应用于已挂载的文件系统，改变将立即生效。可以使用 [findmnt(8)](<https://man.archlinux.org/man/findmnt.8>) 查找设备名： 
    
    # tune2fs -m 1 "$(findmnt -no SOURCE _挂载点路径_)"
    
查询当前保留块的数量： 
    
    # tune2fs -l /dev/mapper/proxima-root | grep 'Reserved block count:'
    
    Reserved block count:     2975334
    
这是块的数量，所以需要乘上文件系统的块大小才能得到字节数：`2975334 * 4096 / 1024**3 = 11.34 GiB`。 

##  从 ext2/ext3 迁移到 ext4

###  不转换直接把 ext2/ext3 分区挂载成 ext4 分区格式

####  基本原理

转换到ext4和继续使用 ext2/ext3 格式的折中的办法就是把分区当作 ext4 分区来挂载。 

**优点:**

  * 兼容性（分区的文件系统可以继续挂载为 ext3） – 这允许用户继续在不支持 ext4 文件格式的操作系统中读取分区。（例如：带 ext2/ext3 驱动的 Windows 系统）
  * 提高性能（不过没有完全转换成 ext4 分区后好）。[[1]](<https://kernelnewbies.org/Ext4>) [[2]](<https://events.static.linuxfound.org/slides/2010/linuxcon_japan/linuxcon_jp2010_fujita.pdf>)

**缺点:**

  * 仅能使用少部分 ext4 特性。（只有那些不改变分区格式的功能能被使用，例如 multiblock allocation 和 delayed allocation）

**注意：** 除了由 ext4 格式带来的相对新的不一样的特性（可以看作一种潜在风险）之外，**这种技术没有大的缺点**

####  步骤

  1. 修改 `/etc/fstab`，把你想要挂载成 ext4 的分区的“type”栏的内容从 ext2/ext3 改为 ext4。
  2. 重新挂载分区。

###  将 ext2/ext3 分区转换为 ext4 格式

####  基本原理

为了能够使用 ext4 的全部特性，必须完成一个不可逆的转换过程。 

**优点：**

  * 更好的性能以及新功能。[[3]](<https://kernelnewbies.org/Ext4>) [[4]](<https://events.static.linuxfound.org/slides/2010/linuxcon_japan/linuxcon_jp2010_fujita.pdf>)

**缺点：**

  * 对于主要包含静态文件的分区，例如 /boot 分区，新功能可能并没有什么好处。此外，添加日志功能（将ext2分区转换为ext3/ext4分区会自动进行）总是会带来额外的性能开销。
  * 不可逆（ext4 分区不能“降级”到 ext2/ext3。不过，在启用 [extent](<https://zh.wikipedia.org/wiki/Extent_\(%E6%AA%94%E6%A1%88%E7%B3%BB%E7%B5%B1\)> "wiki-zh:Extent \(档案系统\)")和其他特有功能前，是可以向下兼容的)

####  步骤

这些指令改编自[内核文档](<https://ext4.wiki.kernel.org/index.php/Ext4_Howto>)和 [BBS thread](<https://bbs.archlinux.org/viewtopic.php?id=61602>)。 

**警告：**

  * 如果你要转换系统的根文件系统，请确保在重启时可以使用'fallback' initramfs。或者，根据[Mkinitcpio#模块（MODULES）](<../zh-cn/Mkinitcpio.html#%E6%A8%A1%E5%9D%97%EF%BC%88MODULES%EF%BC%89> "Mkinitcpio") 添加ext4，并在启动前[重新创建initramfs](<../zh-cn/Mkinitcpio.html#%E5%88%9B%E5%BB%BA%E5%92%8C%E5%90%AF%E7%94%A8%E9%95%9C%E5%83%8F> "Mkinitcpio") 。
  * 如果你决定转换一个 `/boot` 分区, 请确保 [引导加载程序](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F> "引导加载程序") 支持从ext4启动.

在下面的步骤中，`/dev/sdxX` 代表要转换的分区的路径，例如 `/dev/sda1`。 

  1. 在将任何ext3分区转换为ext4之前，[备份](<../zh-cn/%E5%90%8C%E6%AD%A5%E5%92%8C%E5%A4%87%E4%BB%BD%E7%A8%8B%E5%BA%8F.html> "同步和备份程序")所有数据。[clonezilla](<https://archlinux.org/packages/?name=clonezilla>)包是一个有用的工具，尤其对于根分区来说。
  2. 编辑 `/etc/fstab` ，将要转换为ext4分区的'type'栏的内容从ext3改为ext4。
  3. 启用实时介质（如果需要）。使用 [e2fsprogs](<https://archlinux.org/packages/?name=e2fsprogs>)包 进行转换时分区必须未挂载。如果要转换根分区，最简单的方法就是从其他实时介质启动。
  4. 确保分区未被挂载
  5. 如果你想转换一个ext2分区，第一步就是以root身份运行 `tune2fs -j /dev/sdxX` 来添加[日志](<../zh-cn/File_systems.html#Journaling> "File systems")，使其成为ext3分区。
  6. 以root身份运行`tune2fs -O extent,uninit_bg,dir_index /dev/sdxX` 。这个命令将ext3分区转换为ext4（不可逆）。
  7. 以 root 身份运行 `fsck -f /dev/sdxX`。 
     * 这一步是必须的，否则文件系统**将无法读取** 。这次运行 _fsck_ 是为了将文件系统恢复到一致状态。它将发现组描述中的校验和错误。`-f` 选项要求 _fsck_ 强制检查，即使文件系统看起来是干净的。可以在上面使用 `-p` 选项来“自动修复”（否则，每个错误都要求用户输入）。
  8. 推荐操作：挂载分区并以root身份运行 `e4defrag -c -v /dev/sdxX` 。 
     * 即使现在文件系统已经转换为ext4了，但以前写入的文件还没有利用ext4的[extent](<https://zh.wikipedia.org/wiki/Extent_\(%E6%AA%94%E6%A1%88%E7%B3%BB%E7%B5%B1\)> "wiki-zh:Extent \(档案系统\)")的优势，该操作将提高大文件性能并减少碎片和文件系统检查时间。为了充分利用ext4的优势，所有文件都需要在磁盘上重写。使用 `e4defrag`来解决这个问题。
  9. 重新启动

##  提升性能

### E4rat

[E4rat](<../zh-cn/E4rat.html> "E4rat") 是为 ext4 文件系统设计的预加载应用程序。它监视启动时打开的文件，并通过优化它们在分区上所处的位置来提升访问效率，并在启动过程之初就预加载它们。与机械硬盘不同的是 _E4rat_ 不会提升[固态硬盘](<../zh-cn/%E5%9B%BA%E6%80%81%E7%A1%AC%E7%9B%98.html> "固态硬盘")的性能，因为后者的访问时间与前者相比可以忽略不计。 

###  禁用访问时间更新

_ext4_ 文件系统会记录于文件上次被访问的时间相关的信息，而记录这些信息会导致开销。使用 `noatime` 选项可防止更新访问时间戳。 
    
    /etc/fstab
    
    /dev/sda5    /    ext4    defaults,**noatime**    0    1
    
这样做会破坏访问依赖时间的应用程序，请查看 [fstab#atime 参数](<../zh-cn/Fstab.html#atime_%E5%8F%82%E6%95%B0> "Fstab")获取可能的解决方案。 

###  增加提交时间间隔

通过为 `提交` 选项提供更长的延迟时间，可以增加数据和元数据的同步间隔。 

默认的5秒意味着如果断电，最多只会丢失5秒的工作。它每5秒强制对所有数据/日志进行一次完整的同步到物理介质。由于有了日志功能，文件系统不会受损。以下的 [fstab](<../zh-cn/Fstab.html> "Fstab") 示例展示了`commit`选项的使用： 
    
    /etc/fstab
    
    /dev/sda5    /    ext4    defaults,noatime,**commit=60**    0    1

###  关闭屏障

**警告：** 如果磁盘无法保证在电源掉电时缓存正确写入，禁用屏障可能会导致严重的文件系统损坏和数据丢失。

_Ext4_ 默认启用写屏障。它确保文件系统元数据磁盘上被正确地写入和排序，即使在写缓存掉电时也是如此。这会带来性能成本，特别是对于大量使用 _fsync_ 或创建和删除许多小文件的应用程序。对于写缓存由电池供电的磁盘，禁用障碍可以会安全地提高性能。 

要关闭屏障，将 `barrier=0` 选项添加到文件系统中。例如： 
    
    /etc/fstab
    
    /dev/sda5    /    ext4    noatime,**barrier=0**    0    1

###  禁用日志

**警告：** 使用没有日志的文件系统，在突发卸载的情况下，例如断电或者内核锁定，将导致数据丢失。

_ext4_ 中禁用日志，可以对已卸载的硬盘使用下列指令完成操作: 
    
    # tune2fs -O "^has_journal" /dev/sdXN
    
##  技巧与窍门

###  使用基于文件的加密

自从Linux 4.1以来，ext4原生支持文件加密，请参阅 [fscrypt](</wzh/index.php?title=Fscrypt&action=edit&redlink=1> "Fscrypt（页面不存在）")（英语：[fscrypt](<https://wiki.archlinux.org/title/fscrypt> "en:fscrypt")） 文章。加密是在目录级别应用的，在不同的目录中可以使用不同的加密密钥。这与 [dm-crypt](<../zh-cn/Dm-crypt.html> "Dm-crypt")（块级别的加密）和 [eCryptfs](</wzh/index.php?title=ECryptfs&action=edit&redlink=1> "ECryptfs（页面不存在）")（英语：[eCryptfs](<https://wiki.archlinux.org/title/eCryptfs> "en:eCryptfs")）（堆叠加密文件系统）都不同 

###  在现有的文件系统中启用元数据校验和

当一个文件系统是使用 [e2fsprogs](<https://archlinux.org/packages/?name=e2fsprogs>)包 1.43 (2016) 或更高的版本创建时，默认情况下会启用元数据校验和。可以转换现有文件系统以启用元数据校验和支持。 

如果CPU支持 SSE 4.2，请确保加载 `crc32c_intel` [内核模块](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html> "内核模块")以启用硬件加速的 CRC32C 算法[[5]](<https://ext4.wiki.kernel.org/index.php/Ext4_Metadata_Checksums#Benchmarking>)。如果不支持，则改为加载 `crc32c_generic` 模块。。 

要了解有关元数据校验和的更多信息，请参阅 [ext4 wiki](<https://ext4.wiki.kernel.org/index.php/Ext4_Metadata_Checksums>)。 

**提示：** 使用`dumpe2fs`检查文件系统上启用的功能： 
    
    # dumpe2fs -h _/dev/path/to/disk_
    
**注意：** 必须卸载文件系统。

首先需要使用 `e2fsck`来检查和优化分区： 
    
    # e2fsck -Df _/dev/path/to/disk_  
    
将文件系统转换为 64 位： 
    
    # resize2fs -b _/dev/path/to/disk_ 
    
最后启用校验和支持： 
    
    # tune2fs -O metadata_csum _/dev/path/to/disk_
    
验证： 
    
    # dumpe2fs -h _/dev/path/to/disk_ | grep features:
    
    Filesystem features:      has_journal ext_attr resize_inode dir_index filetype extent **64bit** flex_bg sparse_super large_file huge_file dir_nlink extra_isize **metadata_csum**

###  在现有的文件系统中启用 fast_commit

从 5.10 内核开始，可以启用`fast_commit` 选项来提高ext4的性能： 
    
    # tune2fs -O fast_commit /dev/_drivepartition_
    
阐述当前配置或更改： 
    
    # tune2fs -l /dev/_drivepartition_ | grep features
    
###  启用不区分大小写模式

**警告：** GRUB目前不支持Ext4的 `casefold`功能；请参见[GRUB bug #56897](<https://savannah.gnu.org/bugs/?56897/>)。为GRUB需要读取的文件系统启用该功能将会导致系统无法启动，并出现`未知文件系统` 错误，即使没有目录实际使用该功能。 

ext4 可以在不区分大小写的模式下使用，这可以提高在 [Wine](<../zh-cn/Wine.html> "Wine") 中运行应用程序和游戏的性能。此功能不影响整个文件系统，只影响了启用不区分大小写属性的目录。 

首先，在文件系统中启用该功能： 
    
    # tune2fs -O casefold /dev/path/to/disk
    
现在，你可以在任何目录中启用不区分大小写： 
    
    $ chattr +F /mnt/partition/case-insensitive-directory
    
请注意，目录必须为空，且从其他地方移动子目录不会继承他们的属性，因此，请相应地提前规划。 

##  参见

  * [Ext4 官方 wiki](<https://ext4.wiki.kernel.org/>)
  * [Ext4 Disk Layout](<https://ext4.wiki.kernel.org/index.php/Ext4_Disk_Layout>) described in its wiki
  * [Ext4 加密](<https://lwn.net/Articles/639427/>) LWN 文章
  * Kernel commits for ext4 encryption [[6]](<https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/commit/?id=6162e4b0bedeb3dac2ba0a5e1b1f56db107d97ec>) [[7]](<https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/commit/?id=8663da2c0919896788321cd8a0016af08588c656>)
  * [e2fsprogs Changelog](<https://e2fsprogs.sourceforge.net/e2fsprogs-release.html>)
  * [Ext4 元数据校验和](<https://ext4.wiki.kernel.org/index.php/Ext4_Metadata_Checksums>)
  * [Ext4 fast commits](<https://lwn.net/Articles/842385/>)
