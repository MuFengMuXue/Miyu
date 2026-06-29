**翻译状态：**

  * 本文（或部分内容）译自 [XFS](<https://wiki.archlinux.org/title/XFS> "arch:XFS")，最近一次同步于 2025-08-03，若英文版本有所[更改](<https://wiki.archlinux.org/title/XFS?diff=0&oldid=834108>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/XFS_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [文件系统](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html> "文件系统")

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 未完成（在 [Talk:XFS#](<../zh-cn/Talk:XFS.html>) 中讨论）

[XFS](<https://xfs.wiki.kernel.org/#documentation>) 是由硅谷图形公司（Silicon Graphics, Inc.）开发的高性能日志式文件系统。XFS 因其基于分配组 （allocation group）的设计而特别擅长并行 IO。当该文件系统跨越多个存储设备时，这种设计使得 IO 线程数、文件系统带宽、文件和文件系统大小都具有极大的可伸缩性。 

##  预备

为了使用 XFS 用户空间实用程序，请[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [xfsprogs](<https://archlinux.org/packages/?name=xfsprogs>)包 软件包。它包含了管理 XFS 文件系统所需的必要工具。 

##  创建

可以使用如下命令在 _device_ 上创建新文件系统： 
    
    # mkfs.xfs _device_
    
一般来说，默认选项是最适合正常使用的。[[1]](<https://web.archive.org/web/20240113230117/https://xfs.org/index.php/XFS_FAQ#Q:_I_want_to_tune_my_XFS_filesystems_for_.3Csomething.3E>)[[2]](<https://access.redhat.com/documentation/en_us/red_hat_enterprise_linux/7/html/storage_administration_guide/ch-xfs#xfscreating>)

输出示例： 
    
    meta-data=/dev/device            isize=256    agcount=4, agsize=3277258 blks
             =                       sectsz=512   attr=2
    data     =                       bsize=4096   blocks=13109032, imaxpct=25
             =                       sunit=0      swidth=0 blks
    naming   =version 2              bsize=4096   ascii-ci=0
    log      =internal log           bsize=4096   blocks=6400, version=2
             =                       sectsz=512   sunit=0 blks, lazy-count=1
    realtime =none                   extsz=4096   blocks=0, rtextents=0

**提示：**

  * 可以使用 `-L _label_` 选项来为文件系统分配标签。
  * 在对已包含文件系统的块设备使用 _mkfs.xfs_ 时，需使用 `-f` 选项来覆盖掉原有的文件系统。[[3]](<https://access.redhat.com/documentation/en_us/red_hat_enterprise_linux/7/html/storage_administration_guide/ch-xfs#xfscreating>)_**这会完全清除旧文件系统中的所有数据！**_

**注意：** “创建 XFS 文件系统后就无法缩容，但可以通过 xfs_growfs 进行扩容。”[[4]](<https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/storage_administration_guide/ch-xfs#xfscreating>)具体请参考[#调整大小](<#%E8%B0%83%E6%95%B4%E5%A4%A7%E5%B0%8F>)。

###  数据完整性

[xfsprogs](<https://archlinux.org/packages/?name=xfsprogs>)包 3.2.0 引入了一种新型磁盘格式（v5），其包含了称为[自描述元数据（Self-Describing Metadata）](<https://docs.kernel.org/filesystems/xfs/xfs-self-describing-metadata.html>)的元数据校验方案。 基于 CRC32，它提供的额外保护措施可以防止元数据损坏（例如在意外断电时）。当使用 [xfsprogs](<https://archlinux.org/packages/?name=xfsprogs>)包 3.2.3 或更高版本时，这种校验默认是打开的。如果需要在旧版内核中挂载 XFS 为可读写，可以在调用 [mkfs.xfs(8)](<https://man.archlinux.org/man/mkfs.xfs.8>) 时加上 `-m crc=0` 来关闭校验特性： 
    
    # mkfs.xfs -m crc=0 /dev/_target_partition_
    
**注意：** 禁用元数据校验同时会禁用下面提到的 [#Free inode btree](<#Free_inode_btree>)、[#Reverse mapping btree](<#Reverse_mapping_btree>) 和 [#大时间戳（Big timestamps）](<#%E5%A4%A7%E6%97%B6%E9%97%B4%E6%88%B3%EF%BC%88Big_timestamps%EF%BC%89>)功能，以及“reference count btrees”（具体信息请参考 [mkfs.xfs(8) § OPTIONS](<https://man.archlinux.org/man/mkfs.xfs.8#OPTIONS>)）。

自 Linux 内核版本 3.15 起，XFS v5 磁盘格式被视作稳定特性，可用于生产环境。 

**注意：** 与 [Btrfs](<../zh-cn/Btrfs.html> "Btrfs") 和 [ZFS](<../zh-cn/ZFS.html> "ZFS") 不同，XFS 中的 CRC32 校验仅用于元数据而非实际数据。

###  空闲 inode B+ 树

自 Linux 3.16 起，XFS 增加了一个 B+ 树用于索引未被使用的 inode。它等同于现有的索引已使用 inode 的 B+ 树，不同之处在于索引未用 inode 的 B+ 树会跟踪至少包含一个未用 inode 的 inode 块。这一设计的目的是改进分配 inode 时寻找未用 inode 簇的性能。它可以提高长期使用后的文件系统性能，比如你在数月或数年之间已经向文件系统写入或删除了数百万的文件。使用这个功能不会影响整个文件系统的可靠性程度或恢复能力。 

这个功能依赖于新的 v5 磁盘格式，自 Linux 内核 3.15 版本起它被视作为可用于生产环境的稳定特性。它没有改变磁盘上原本的数据结构，但会添加了一个与分配 inode 的 B+ 树保持一致的结构；因此，旧版本的内核只能将带有 B+ 树功能的文件系统挂载为只读模式。 

当使用 xfsprogs 3.2.3 或更高版本时这个功能默认是开启的。如果你需要一个旧版本内核可写入的文件系统，这个功能可以在格式化 XFS 分区时用 `finobt=0` 开关来关闭。你还需要把它和 `crc=0` 一起使用： 
    
    # mkfs.xfs -m crc=0,finobt=0 /dev/_target_partition_
    
也可以简写为（`finobt` 依赖于 `crc`）： 
    
    # mkfs.xfs -m crc=0 /dev/_target_partition_
    
### Reverse mapping btree

The reverse mapping btree is [at its core](<https://blogs.oracle.com/linux/xfs-online-filesystem-checking>): 

    a secondary index of storage space usage that effectively provides a redundant copy of primary space usage metadata. This adds some overhead to filesystem operations, but its inclusion in a filesystem makes cross-referencing very fast. It is an essential feature for repairing filesystems online because we can rebuild damaged primary metadata from the secondary copy.
    The feature graduated from EXPERIMENTAL status in Linux 4.16 and is production ready. However, online filesystem checking and repair is (so far) the only use case for this feature, so it will remain opt-in at least until online checking graduates to production readiness.

From [mkfs.xfs(8) § OPTIONS](<https://man.archlinux.org/man/mkfs.xfs.8#OPTIONS>): 

    The reverse mapping btree maps filesystem blocks to the owner of the filesystem block. Most of the mappings will be to an inode number and an offset, though there will also be mappings to filesystem metadata. This secondary metadata can be used to validate the primary metadata or to pinpoint exactly which data has been lost when a disk error occurs.

See also [[5]](<https://kernelnewbies.org/Linux_4.16#XFS_reverse_mapping_and_reflink_features_are_now_stable>) and [[6]](<https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=35a891be96f1f8e1227e6ad3ca827b8a08ce47ea>) for more information. 

This feature is enabled by default for new filesystems as of xfsprogs 6.5.0. 

###  大时间戳（Big timestamps）

Starting in Linux 5.10, XFS supports using refactored "timestamp and inode encoding functions to handle timestamps as a 64-bit nanosecond counter and bit shifting to increase the effective size. This now allows XFS to run well past the [Year 2038 problem](<https://zh.wikipedia.org/wiki/2038%E5%B9%B4%E9%97%AE%E9%A2%98> "zhwp:2038年问题") to now the Year 2486. Making a new XFS file-system with _bigtime_ enabled allows a timestamp range from December 1901 to July 2486 rather than December 1901 to January 2038." The feature will also allow quota timer expirations from January 1970 to July 2486 rather than January 1970 to February 2106. 

Big timestamps are enabled by default for new filesystems as of xfsprogs 5.15. 

####  升级

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** Make this a top-level section and describe which of the new defaults can be enabled on existing file systems. (在 [Talk:XFS](<../zh-cn/Talk:XFS.html>) 中讨论)

可以通过 [xfs_info(8)](<https://man.archlinux.org/man/xfs_info.8>) 检查现有文件系统是否已启用大时间戳： 
    
    # xfs_info / | grep bigtime
    ... bigtime=0 ...
    
在 [xfsprogs](<https://archlinux.org/packages/?name=xfsprogs>)包 5.11 及更新版本上，可以使用 [xfs_admin(8)](<https://man.archlinux.org/man/xfs_admin.8>) 来升级未挂载的现有文件系统： 
    
    # xfs_admin -O bigtime=1 _device_
    
也可以使用 [xfs_repair(8)](<https://man.archlinux.org/man/xfs_repair.8>)： 
    
    # xfs_repair -c bigtime=1 _device_
    
另外可以考虑顺便启用 `inobtcount`（这是另一个新的默认配置项）。 

##  性能

摘自 [XFS FAQ](<https://web.archive.org/web/20240113230117/https://xfs.org/index.php/XFS_FAQ#Q:_I_want_to_tune_my_XFS_filesystems_for_.3Csomething.3E>)： 

    默认参数已针对性能进行过优化。mkfs.xfs 可以检测到单盘与 MD/DM RAID 配置环境间的区别，并根据环境自动修改文件系统的默认参数。
    基本上你只需在使用对硬件 RAID 时为 `mkfs.xfs` 指定条带单元和宽度。

（详细内容请参考 [#带区大小和宽度](<#%E5%B8%A6%E5%8C%BA%E5%A4%A7%E5%B0%8F%E5%92%8C%E5%AE%BD%E5%BA%A6>)） 

**提示：** 当在 [RAID](<../zh-cn/RAID.html> "RAID") 设备上使用 XFS 文件系统时，可通过使用 `largeio` 和 `swalloc` 值，以及比默认情况更大的 `logbsize` 和 `allocsize` 值等来提高性能。下列文章能提供更多有关详情： 

  * <https://www.beegfs.io/wiki/StorageServerTuning>
  * <https://help.marklogic.com/Knowledgebase/Article/View/505/0/recommended-xfs-settings-for-marklogic-server>

    对于挂载选项，只有 `logbsize` 会对元数据性能产生可观影响。增加 `logbsize` 可以降低特定工作负载下日志 IO 的数量，但如果系统在进行大量修改时崩溃，那么恢复后可能会丢失更多的修改操作。

**提示：** 所有可用挂载选项请参考 [xfs(5)](<https://man.archlinux.org/man/xfs.5>)。

    从内核 3.2.12 版本开始，默认的 I/O 调度器 CFQ 将使 XFS 的并行化大打折扣。

**注意：** 在检测到 SATA 或 [NVMe](</wzh/index.php?title=NVMe&action=edit&redlink=1> "NVMe（页面不存在）") [SSD](<../zh-cn/%E5%9B%BA%E6%80%81%E7%A1%AC%E7%9B%98.html> "SSD") 时，Arch 会自动配置为不使用 I/O 调度器，该行为可通过读取 `/sys/block/nvme*n*/queue/scheduler` 中的内容进行验证。

因此基本上参照[#创建](<#%E5%88%9B%E5%BB%BA>)即可获得最佳性能。 

###  带区大小和宽度

如果这个文件系统位于条带化的 RAID 上，可以在 [mkfs.xfs(8)](<https://man.archlinux.org/man/mkfs.xfs.8>) 命令中指定带区大小来获得显著的性能提升。 

XFS 有时可以检测到软 RAID 下的几何形 (geometry), 但万一您要重塑其或正在使用硬 RAID, 请参阅[如何计算出正确的 sunit 和 swidth 值以获得最佳性能](<https://web.archive.org/web/20240113230117/https://xfs.org/index.php/XFS_FAQ#Q:_How_to_calculate_the_correct_sunit.2Cswidth_values_for_optimal_performance>)

###  访问时间记录

某些文件系统可以通过在 `/etc/fstab` 文件中添加 `noatime` 挂载选项来增强性能。对于 XFS 文件系统来说，默认的访问时间记录行为是 `relatime`，与 noatime 相比这几乎没有额外开销，且仍然可以记录正确的访问时间。所有 Linux 文件系统现在都以这个选项为默认值（从大约 2.6.30 版本开始），但是 XFS 从 2006 年开始就采用了类似 relatime 的特性，因此不需要出于性能考虑而在 XFS 上使用 noatime。[[7]](<https://web.archive.org/web/20240113230117/https://xfs.org/index.php/XFS_FAQ#Q:_Is_using_noatime_or.2Fand_nodiratime_at_mount_time_giving_any_performance_benefits_in_xfs_.28or_not_using_them_performance_decrease.29.3F>)

更多信息请参考 [Fstab#atime 参数](<../zh-cn/Fstab.html#atime_%E5%8F%82%E6%95%B0> "Fstab")。 

### Discard

Despite XFS supporting async discard[[8]](<https://lwn.net/Articles/787272/>) since kernel 4.7[[9]](<https://www.phoronix.com/scan.php?page=news_item&px=Async-Discard-Linux-4.7>)[[10]](<https://events.static.linuxfound.org/sites/events/files/slides/discard_0.pdf>), [xfs(5)](<https://man.archlinux.org/man/xfs.5>) still recommends "that you use the [fstrim](</wzh/index.php?title=Fstrim&action=edit&redlink=1> "Fstrim（页面不存在）") application to discard unused blocks rather than the discard mount option because the performance impact of this option is quite severe." 

See [固态硬盘#定期 TRIM](<../zh-cn/%E5%9B%BA%E6%80%81%E7%A1%AC%E7%9B%98.html#%E5%AE%9A%E6%9C%9F_TRIM> "固态硬盘"). 

###  磁盘碎片整理

尽管 XFS 本质上基于区段 (Extent) 并且延迟分配策略很大程度上增强了它对磁盘碎片的抗性，XFS 仍然提供了磁盘碎片整理程序（ _xfs_fsr_ ，XFS filesystem reorganizer 的缩写），它可以在已挂载且活动的 XFS 文件系统上整理碎片。定期查看 XFS 碎片也很有用。 

[xfs_fsr(8)](<https://man.archlinux.org/man/xfs_fsr.8>) 可以改进已挂载文件系统的文件组织。该重组织算法一次操作一份文件，对文件进行压实或改进文件区段布局（改成连续数据块）。 

####  检查碎片程度

查看当前文件系统中有多少磁盘碎片： 
    
    # xfs_db -c frag -r /dev/_partition_
    
####  进行碎片整理

要启动碎片整理，使用 [xfs_fsr(8)](<https://man.archlinux.org/man/xfs_fsr.8>) 命令： 
    
    # xfs_fsr /dev/_partition_
    
###  去重

The _reflink_ feature, available since kernel version 4.9 and enabled by default since `mkfs.xfs` version 5.1.0, allows creating fast reflink'ed copies of files as well as deduplication after the fact, in the same way as [btrfs](<../zh-cn/Btrfs.html> "Btrfs"): 

#### Reflink copies

Reflink copies initially use no additional space: 
    
    $ cp --reflink bigfile1 bigfile2
    
Until either file is edited, and a copy-on-write takes place. This can be very useful to create snapshots of (large) files. 

####  去重

现有文件系统可使用 [duperemove](<https://archlinux.org/packages/?name=duperemove>)包 或 [util-linux](<https://archlinux.org/packages/?name=util-linux>)包 的 [hardlink(1)](<https://man.archlinux.org/man/hardlink.1>) 工具进行去重。 

###  外部 XFS 日志

使用外部日志（元数据日志）可能对提高性能很有帮助 (例如在 [SSD](<../zh-cn/%E5%9B%BA%E6%80%81%E7%A1%AC%E7%9B%98.html> "SSD") 上)[[11]](<https://docs.oracle.com/en/operating-systems/oracle-linux/9/fsadmin/fsadmin-ManagingtheXFSFileSystem.html#extjnl-xfs>)。请参阅 [mkfs.xfs(8)](<https://man.archlinux.org/man/mkfs.xfs.8>) 获取有关 `logdev` 参数的更多详情. 

**警告：** 当心：使用闪存的情况下可能会减损硬盘寿命。请参阅[性能优化#减少磁盘读写](<../zh-cn/%E6%80%A7%E8%83%BD%E4%BC%98%E5%8C%96.html#%E5%87%8F%E5%B0%91%E7%A3%81%E7%9B%98%E8%AF%BB%E5%86%99> "性能优化")获取有关 SSD 寿命减损的详情。

要在创建 XFS 文件系统时保留指定大小的外部日志，请为 `mkfs.xfs` 命令指定 `-l logdev=_device_ ,size=_size_` 选项。如果省略 `size` 参数, 则会使用基于文件系统大小的日志大小。要在挂载 XFS 文件系统时让其使用外部日志，请为 [mount](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html#%E6%8C%82%E8%BD%BD%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "Mount") 命令指定 `-o logdev=_device_` 选项。 

###  同步间隔

XFS 有其专有的 [sysctl](<../zh-cn/Sysctl.html> "Sysctl") 变量来设置“[回写间隔](<../zh-cn/%E6%80%A7%E8%83%BD%E4%BC%98%E5%8C%96.html#%E5%9B%9E%E5%86%99%E9%97%B4%E9%9A%94%E5%92%8C%E7%BC%93%E5%86%B2%E5%8C%BA%E5%A4%A7%E5%B0%8F> "性能优化")”,默认为 3000. 

**警告：** 提高该值可能会提高性能，但同时会提高断电时数据丢失的严重程度。
    
    /etc/sysctl.d/20-xfs-sync-interval.conf
    
    fs.xfs.xfssyncd_centisecs = 10000

##  管理

###  调整大小

XFS 支持通过 [xfs_growfs(8)](<https://man.archlinux.org/man/xfs_growfs.8>) 在线调整大小： 
    
    # xfs_growfs -D _size_ _/path/to/mnt/point_
    
如果缺省 `-D size` 参数，那文件系统会自动扩大到可能的最大大小（即分区大小）。 

**注意：** 根据 [xfs_growfs(8)](<https://man.archlinux.org/man/xfs_growfs.8>)，xfs 尚未完全支持缩容： 

“只有 1 AG 大小的文件系统无法缩容，且无法将文件系统缩到 1 AG 大小，其中 _AG_ 指的是 _分配组_ 。” 

###  在线元数据检查（scrub）

**警告：** 该程序目前是**实验性** 的，这意味着它的行为和接口可能随时发生变化。详情请见 [xfs_scrub(8)](<https://man.archlinux.org/man/xfs_scrub.8>)。

`xfs_scrub` 请求内核检查 XFS 文件系统中的所有元数据对象。内核会扫描元数据记录以查找明显错误的值，然后与其它元数据进行交叉引用。其目的是通过检查单个元数据记录与文件系统中其它元数据的一致性，建立对整个文件系统一致性的合理置信度。如果存在完整的冗余数据结构，则可以根据其它元数据重建损坏的元数据。 

[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")/[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `xfs_scrub_all.timer` 以定期在线检查所有 XFS 文件系统的元数据。 

**注意：** 有时可能需要[编辑](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "编辑") `xfs_scrub_all.timer`，且如果错过了上一次执行时间（例如因为系统关机/断电），计时器将会[立即激发](<../zh-cn/Systemd/%E5%AE%9A%E6%97%B6%E5%99%A8.html#%E5%AE%9E%E6%97%B6%E5%AE%9A%E6%97%B6%E5%99%A8> "Systemd/定时器")。

###  修复

**注意：** "Unlike other Linux file systems, _xfs_repair_ does not run at boot time, even when an XFS file system was not cleanly unmounted. In the event of an unclean unmount, _xfs_repair_ simply replays the log at mount time, ensuring a consistent file system."[[12]](<https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/storage_administration_guide/xfsrepair>)

From [Checking and Repairing an XFS File System](<https://docs.oracle.com/en/operating-systems/oracle-linux/9/fsadmin/fsadmin-CheckingandRepairinganXFSFileSystem.html>) (emphasis ours): 

    If you can't mount an XFS file system, you can use the `xfs_repair -n` command to check its consistency. Typically, you would **only run this command on the device file of an[unmount](</wzh/index.php?title=Unmount&action=edit&redlink=1> "Unmount（页面不存在）")ed file system** that you believe has a problem. The `xfs_repair -n` command displays output to indicates changes that would be made to the file system in the case where it would need to complete a repair operation, but doesn't modify the file system directly.
    If you can mount the file system and you don't have a suitable backup, you can use the _xfsdump_ command to back up the existing file system data. However, note that the command might fail if the file system's metadata has become corrupted.
    You can use the _xfs_repair_ command to attempt to repair an XFS file system specified by its device file. The command replays the journal log to fix any inconsistencies that might have resulted from the file system not being cleanly unmounted. Unless the file system has an inconsistency, you typically don't need to use the follwoing command, as the journal is replayed every time that you mount an XFS file system.

    # xfs_repair _device_

    If the journal log has become corrupted, you can reset the log by specifying the `-L` option to _xfs_repair_.

**警告：**

  * The _xfs_repair_ utility cannot repair an XFS file system with a dirty log. To clear the log, mount and unmount the XFS file system. If the log is corrupt and cannot be replayed, use the `-L` option ("force log zeroing") to clear the log, that is, `xfs_repair -L /dev/_device_`. Be aware that this may result in further corruption or data loss.[[13]](<https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/storage_administration_guide/xfsrepair>)
  * Resetting the log can leave the file system in an inconsistent state, resulting in data loss and data corruption. Unless you're experienced with debugging and repairing XFS file systems by using the _xfs_db_ , it is recommended that you instead recreate the file system and restore its contents from a backup.[[14]](<https://docs.oracle.com/en/operating-systems/oracle-linux/9/fsadmin/fsadmin-CheckingandRepairinganXFSFileSystem.html>)

    If you can't mount the file system or you don't have a suitable backup, running _xfs_repair_ is the only viable option, unless you're experienced in using the _xfs_db_ command.
     _xfs_db_ provides an internal command set that allows you to debug and repair an XFS file system manually. The commands enable you to perform scans on the file system, and navigate and display its data structures. If you specify the `-x` option to enable expert mode, you can modify the data structures.

    # xfs_db [-x] _device_

    For more information, see the [xfs_db(8)](<https://man.archlinux.org/man/xfs_db.8>) and [xfs_repair(8)](<https://man.archlinux.org/man/xfs_repair.8>), and the _help_ command within _xfs_db_.

See also [Which factors influence the memory usage of xfs_repair?](<https://web.archive.org/web/20240113230117/https://xfs.org/index.php/XFS_FAQ#Q:_Which_factors_influence_the_memory_usage_of_xfs_repair.3F>) and [XFS Repair](<https://web.archive.org/web/20210416081619/https://xfs.org/docs/xfsdocs-xml-dev/XFS_User_Guide/tmp/en-US/html/xfs-repair.html>). 

###  数据恢复

Even when being mounted read-only with `mount -o ro` an XFS file system's log will be replayed if it has not been unmounted cleanly. 

There may be situations where a compromised XFS file system on a damaged storage device should be mounted read-only, so that files may be copied off it hopefully without causing further damage, yet it cannot be mounted because it has not been unmounted cleanly and is damaged to such an extent that the log cannot be replayed. Also, consider that replaying the log means writing to the compromised file system, which might be a bad idea in itself. 

To mount an XFS file system without writing to it in any way and without replaying the log, use `mount -o ro,norecovery`. 

###  撤销删除

[xfs_undelete-git](<https://aur.archlinux.org/packages/xfs_undelete-git/>)AUR 可以从未挂载或只读挂载的 XFS 文件系统中恢复被删除的文件，但存在一定限制。更多信息请参考 <https://github.com/ianka/xfs_undelete> 。 

##  故障排除

###  根文件系统配额

XFS 配额挂载选项（`uquota`、`gquota`、`prjquota` 等）会在重新挂载文件系统时失效。要对根文件系统启用配额功能，这个挂载选项需要作为[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数") `rootflags=` 传递给初始化内存盘（initramfs）。在随后的启动过程中，这个选项不需要在 `/etc/fstab` 中挂载根（`/`）文件系统的挂载选项里再次列出。 

**注意：** XFS 配额相较于标准 Linux [磁盘配额](</wzh/index.php?title=Disk_quota&action=edit&redlink=1> "Disk quota（页面不存在）")有一些区别，可以参考下 <https://inai.de/linux/adm_quota> 这篇文章。

###  如果用户“nobody”无法访问挂载点，xfs_scrub_all 会执行失败

当执行 `xfs_scrub_all` 时，它将为每个已挂载的 XFS 文件系统启动 `xfs_scrub@.service` 服务。这项服务以用户 `nobody` 身份运行，所以如果 `nobody` 无法进入目录时，命令执行将会失败，并随附以下错误： 
    
    xfs_scrub@_mountpoint_.service: Changing to the requested working directory failed: Permission denied
    xfs_scrub@_mountpoint_.service: Failed at step CHDIR spawning /usr/bin/xfs_scrub: Permission denied
    xfs_scrub@_mountpoint_.service: Main process exited, code=exited, status=200/CHDIR
    
为了能让对应服务运行，请更改挂载点的[权限](<../zh-cn/%E6%96%87%E4%BB%B6%E6%9D%83%E9%99%90%E4%B8%8E%E5%B1%9E%E6%80%A7.html> "权限")以使用户 `nobody` 拥有执行权限。 

### fsck.xfs fails in systemd-based initramfs

When using a [mkinitcpio](<../zh-cn/Mkinitcpio.html> "Mkinitcpio")-generated systemd based initramfs without the `base` hook, you will see the following messages in the [journal](<../zh-cn/Systemd/Journal.html> "Journal"): 
    
    systemd-fsck[288]: fsck: /usr/bin/fsck.xfs: execute failed: No such file or directory
    systemd-fsck[286]: fsck failed with exit status 8.
    systemd-fsck[286]: Ignoring error.
    
This is because [fsck.xfs(8)](<https://man.archlinux.org/man/fsck.xfs.8>) is a shell script and requires `/bin/sh` to execute. `/usr/bin/sh` is provided by the `base` hook, so the solution is to prepend it to the HOOKS array in `/etc/mkinitcpio.conf`. E.g.: 
    
    HOOKS=(**base** systemd ... )
    
##  参考资料

  * [XFS wiki (archive)](<https://web.archive.org/web/20240113230117/https://xfs.wiki.kernel.org/>)
  * [XFS FAQ](<https://web.archive.org/web/20240113230117/https://xfs.org/index.php/XFS_FAQ>)
  * [Improving Metadata Performance By Reducing Journal Overhead](<https://web.archive.org/web/20240113230117/https://xfs.org/index.php/Improving_Metadata_Performance_By_Reducing_Journal_Overhead>)
  * [XFS Wikipedia Entry](<https://en.wikipedia.org/wiki/XFS> "wikipedia:XFS")
  * [XFS User Guide](<https://web.archive.org/web/20210416081619/https://xfs.org/index.php/XFS_Papers_and_Documentation>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2024-03-03 ⓘ] XFS User Guide no longer exists but has a link to the git repository
