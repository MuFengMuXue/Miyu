**翻译状态：**

  * 本文（或部分内容）译自 [Btrfs](<https://wiki.archlinux.org/title/Btrfs> "arch:Btrfs")，最近一次同步于 2025-09-20，若英文版本有所[更改](<https://wiki.archlinux.org/title/Btrfs?diff=0&oldid=847104>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Btrfs_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [文件系统](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html> "文件系统")
  * [Snapper](<../zh-cn/Snapper.html> "Snapper")
  * [Timeshift](<../zh-cn/Timeshift.html> "Timeshift")
  * [Yabsnap](<../zh-cn/Yabsnap.html> "Yabsnap")

译自 [Introduction — BTRFS Documentation](<https://btrfs.readthedocs.io/en/latest/Introduction.html>)： 

    Btrfs 是为 Linux 开发的现代写时复制（CoW, Copy-on-Write）文件系统，旨在提供高级功能，同时也注重容错、修复及便于管理。

**注意：** 与其它一些文件系统类似，Btrfs 仍在持续开发中，因此某些特定的功能可能尚未成熟到可以满足日常使用。要检查特定使用场景是否会受到影响，可查阅 Btrfs 官方文档的[状态](<https://btrfs.readthedocs.io/en/latest/Status.html>)页面（英文）及本文的[#已知问题](<#%E5%B7%B2%E7%9F%A5%E9%97%AE%E9%A2%98>)部分。 

##  准备

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")用户空间工具 [btrfs-progs](<https://archlinux.org/packages/?name=btrfs-progs>)包，这是执行基本操作所必需的。 

若需要从 Btrfs 文件系统启动（即内核和 [initramfs](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#initramfs> "Initramfs") 位于 Btrfs 文件系统），请检查[引导加载程序](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F> "引导加载程序")是否支持 Btrfs。 

##  创建文件系统

下文展示如何创建一个新的 Btrfs [文件系统](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html> "文件系统")。若要将一个 ext3/4 文件系统转换为 Btrfs，请参考 [#从 ext3/4 转换](<#%E4%BB%8E_Ext3/4_%E8%BD%AC%E6%8D%A2>)。若要使用无分区的配置，请参考 [#无分区 Btrfs 磁盘](<#%E6%97%A0%E5%88%86%E5%8C%BA_Btrfs_%E7%A3%81%E7%9B%98>)。 

查阅 [mkfs.btrfs(8)](<https://man.archlinux.org/man/mkfs.btrfs.8>) 以获取更多信息。 

Btrfs 文件系统可建立在一个或多个设备上。此处“[设备](<https://btrfs.readthedocs.io/en/latest/Glossary.html#:~:text=device,-A>)”是指 Linux 块设备，例如整个磁盘、分区、LVM 逻辑卷、回环设备、网络块设备等。 

###  单设备文件系统

要在分区 `/dev/_分区名_` 上创建一个 Btrfs 文件系统，执行： 
    
    # mkfs.btrfs -L _自定义卷标_ /dev/_分区名_
    
Btrfs 文件系统中，元数据的默认节点大小（nodesize）为 16 KiB 和系统页大小之中较大者，而数据的默认扇区大小等于系统页大小（自动检测）。如需为元数据指定更大的节点大小（必须是扇区大小的整数倍，最大允许 64 KiB），可通过 `-n` 选项来设置，如下例使用 32 KiB 的节点大小： 
    
    # mkfs.btrfs -L _自定义卷标_ -n 32k /dev/_分区名_
    
**注意：** 根据 [mkfs.btrfs(8) § OPTIONS](<https://man.archlinux.org/man/mkfs.btrfs.8#OPTIONS>) 手册页内容：“较小的节点大小会增加碎片化，但B树变得更高，从而能够减少锁竞争。较大的节点大小则能使数据更加紧凑并降低碎片化程度，但在更新元数据块时需要更多昂贵的内存操作。”

###  多设备文件系统

**警告：**

  * Btrfs 的 RAID 5 和 RAID 6 模式存在致命缺陷，除非用来做丢失数据无所谓的测试，否则不应当用于任何场景。这里有[已知问题和部分绕过方案的列表](<https://lore.kernel.org/linux-btrfs/20200627032414.GX10769@hungrycats.org/>)。 查阅 [btrfs(5) § RAID56 STATUS AND RECOMMENDED PRACTICES](<https://man.archlinux.org/man/btrfs.5#RAID56_STATUS_AND_RECOMMENDED_PRACTICES>) 以获取最新动态。
  * 默认情况下，[systemd](<../zh-cn/Systemd.html> "Systemd") 会为 `/var/log/journal` 目录禁用[写时复制（CoW）](<#%E5%86%99%E6%97%B6%E5%A4%8D%E5%88%B6%EF%BC%88CoW%EF%BC%89>)，这在 RAID 1 上会导致数据损坏（参见 [#禁用写时复制](<#%E7%A6%81%E7%94%A8%E5%86%99%E6%97%B6%E5%A4%8D%E5%88%B6>)）。要避免这种情况，请创建一个空文件 `/etc/tmpfiles.d/journal-nocow.conf`，用来覆盖 `/usr/lib/tmpfiles.d/journal-nocow.conf`（参阅 [tmpfiles.d(5) § CONFIGURATION DIRECTORIES AND PRECEDENCE](<https://man.archlinux.org/man/tmpfiles.d.5#CONFIGURATION_DIRECTORIES_AND_PRECEDENCE>)）。

Btrfs 可以在多个设备上创建 RAID。Btrfs 支持的 [RAID](<../zh-cn/RAID.html> "RAID") 级别包括 RAID 0、RAID 1、RAID 10、RAID 5 和 RAID 6（详情参阅下文 [#profile](<#profile>)）。Btrfs 的 RAID1 profile 仅保存两个副本，内核 5.5 版本引入了 RAID1c3 和 RAID1c4，分别对应带有3和4个副本的 RAID 1 级别。可以使用 `-d` 和 `-m` 参数分别为数据和元数据配置 RAID 级别。默认情况下，数据只有一份（ `single`），元数据则镜像存储（`raid1`）。这相当于 [JBOD](<https://en.wikipedia.org/wiki/JBOD> "w:JBOD") 配置——多个磁盘会被看做成一个文件系统，但文件不冗余。更多有关如何创建一个 Btrfs RAID 卷的信息请参阅 [Btrfs Wiki: 在多个设备上使用 Btrfs](<https://archive.kernel.org/oldwiki/btrfs.wiki.kernel.org/index.php/Using_Btrfs_with_Multiple_Devices.html>)。 
    
    # mkfs.btrfs -d single -m raid1 /dev/_分区1_ /dev/_分区2_ ...
    
必须在 `/etc/mkinitcpio.conf` 中加入 `udev`、`systemd` 或 `btrfs` 钩子之一才能使用多设备 Btrfs 文件系统。查阅 [mkinitcpio#常用钩子](<../zh-cn/Mkinitcpio.html#%E5%B8%B8%E7%94%A8%E9%92%A9%E5%AD%90> "Mkinitcpio")以获取更多信息。 

创建好文件系统之后，建议使用下面的命令扫描并注册多设备 Btrfs 文件系统，这样在挂载多设备文件系统时就仅需指定其中的一个设备： 
    
    # btrfs device scan
    
**注意：**

  * 可以之后再将设备添加到多设备文件系统中，详情请参见 Btrfs Wiki 上的[这篇文章](<https://archive.kernel.org/oldwiki/btrfs.wiki.kernel.org/index.php/Using_Btrfs_with_Multiple_Devices.html>)。
  * 多个设备可以大小各异。但如果使用 RAID 配置存储数据，当一个磁盘的大小比其他的加起来都大时，多出的空间并不会被使用。要确定多设备 Btrfs 的可用空间，可以使用 [Btrfs 磁盘使用计算器](<https://carfax.org.uk/btrfs-usage/>)确定。
  * 有些[引导加载程序](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F> "引导加载程序")不支持多设备文件系统，比如 [Syslinux](<../zh-cn/Syslinux.html> "Syslinux")。
  * Btrfs 不会自动从速度最快的设备读取，因此混合使用不同类型的磁盘会导致性能表现不稳定。详情请参阅 [Stack Overflow 上的这个回答](<https://stackoverflow.com/a/55408367>)。

[#RAID](<#RAID>) 小节中有关于维护多设备上的 Btrfs 文件系统的建议。 

#### profile

Btrfs 使用 [profile](<https://btrfs.readthedocs.io/en/latest/mkfs.btrfs.html#profiles>) 这个概念来表示镜像、奇偶校验和分条，对应 [RAID](<https://zh.wikipedia.org/wiki/RAID> "zhwp:RAID") 术语中的“RAID 级别”（若适用）。在同一个 Btrfs 文件系统中，元数据的 profile（[mkfs.btrfs(8)](<https://man.archlinux.org/man/mkfs.btrfs.8>) 的 `-m` 选项）和数据的 profile（[mkfs.btrfs(8)](<https://man.archlinux.org/man/mkfs.btrfs.8>) 的 `-d` 选项）可以不一样。 

一些重要的 profile： 

single
    没有镜像、分条和奇偶校验，让多个设备映射到单个文件系统中。在 [mdadm](<../zh-cn/RAID.html> "Mdadm") 术语中被叫做 `LINEAR`。
RAID0
    没有镜像、分条和奇偶校验，但允许并行访问设备。不像传统的 [mdadm](<../zh-cn/RAID.html> "Mdadm") RAID 那样要求设备大小相同。
RAID1
    镜像，没有分条和奇偶校验，允许在一个设备失效的情况下恢复数据。

更多 profile 请参阅手册 [mkfs.btrfs(8) § PROFILES](<https://btrfs.readthedocs.io/en/latest/mkfs.btrfs.html#profiles>)。 

##  配置文件系统

###  写时复制（CoW）

默认情况下 Btrfs 总是对所有文件使用[写时复制（CoW）](<https://zh.wikipedia.org/wiki/%E5%86%99%E5%85%A5%E6%97%B6%E5%A4%8D%E5%88%B6> "zhwp:写入时复制")。写入操作不会原地覆盖数据，而是将修改后的数据块写入新位置，同时更新元数据指向新位置。请参阅 [Btrfs Sysadmin 相关章节](<https://archive.kernel.org/oldwiki/btrfs.wiki.kernel.org/index.php/SysadminGuide.html#Copy_on_Write_.28CoW.29>)了解实现细节以及其优缺点。 

####  禁用写时复制

**警告：** 在 Btrfs 中禁用写时复制会禁用数据校验和 [[1]](<https://btrfs.readthedocs.io/en/latest/btrfs-man5.html#btrfs-specific-mount-options>) [[2]](<https://man7.org/linux/man-pages/man1/chattr.1.html>)，禁用数据校验和会使 Btrfs 无法得知这些文件是否损坏。与 RAID 1（包括 profile 中的 `RAID1`、`RAID1c3` 与 `RAID1c4`）结合使用时，断电或其他原因导致的数据损坏可能会造成副本间的数据不同步。

使用 `nodatacow` 选项挂载文件系统可禁用其上新文件的写时复制特性。注意这只会影响新建的文件，而不会影响已有的文件。`nodatacow` 参数会禁用压缩与数据校验和，参阅 [btrfs(5)](<https://man.archlinux.org/man/btrfs.5>) 以了解细节。 

**注意：**

  * 根据 [btrfs(5) § MOUNT OPTIONS](<https://man.archlinux.org/man/btrfs.5#MOUNT_OPTIONS>)：“在单个文件系统中，无法让一些子卷使用 `nodatacow` 参数挂载，而其他的使用 `datacow` 参数挂载。第一个被挂载子卷的挂载参数将会应用于其他所有子卷。”
  * 即使已禁用写时复制，在特定情况下写时复制仍然会被使用，详见下文[#仍然会触发写时复制的情况](<#%E4%BB%8D%E7%84%B6%E4%BC%9A%E8%A7%A6%E5%8F%91%E5%86%99%E6%97%B6%E5%A4%8D%E5%88%B6%E7%9A%84%E6%83%85%E5%86%B5>)。

要禁用空文件或目录中新文件（同上，不会影响其中已有文件）的写时复制特性，请使用下面的命令： 
    
    $ chattr +C _目录或文件路径_
    
**注意：** 译自 [BTRFS documentation: Attributes](<https://btrfs.readthedocs.io/en/latest/Common-features.html#attributes>)：“在目录上设置此属性时，所有新建的文件将继承该属性。由于实现限制，此标志只能在空文件上设置或取消。”

**提示：** 为目录中已存在的所有文件禁用写时复制可以使用下面的方法： 
    
    $ mv _/path/to/dir_ _/path/to/dir_ _old
    $ mkdir _/path/to/dir_
    $ chattr +C _/path/to/dir_
    $ cp -a --reflink=never _/path/to/dir_ _old/_. /path/to/dir_
    $ rm -rf _/path/to/dir_ _old
    
需要保证这个过程中未使用涉及到的数据。关于此处 `--reflink=never` 参数的使用，详见下文 [#对复制的影响](<#%E5%AF%B9%E5%A4%8D%E5%88%B6%E7%9A%84%E5%BD%B1%E5%93%8D>)。

#####  仍然会触发写时复制的情况

具有 +C 属性的文件仍然允许有超过一个引用（例如使用 `cp` [reflink](<https://btrfs.readthedocs.io/en/latest/Reflink.html#reflink>) 的副本与 Btrfs 中的快照），此时写时复制**依然会生效** 。 

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** 子章节嵌套过多。（在[en:Talk:Btrfs](<https://wiki.archlinux.org/title/Talk:Btrfs> "en:Talk:Btrfs")讨论）

######  对复制的影响

使用 `cp` 复制文件时，+C 属性**并非** 由源文件决定，而取决于目标路径——要么从上级目录继承，要么由文件系统是否使用 `nodatacow` 参数挂载决定。当源文件与目标文件都具有/不具有 +C 属性时，能够通过 reflink 进行复制，否则不能。实际行为依赖于 `--reflink` 参数，有以下三种结果： 

  * 使用 `--reflink=auto` 参数（默认情况）：若 +C 属性相同，则使用 reflink；否则进行深拷贝。
  * 使用 `--reflink`（或 `--reflink=always`）参数：若 +C 属性相同，则使用 reflink；否则操作失败。
  * 使用 `--reflink=never` 参数：总是进行深拷贝。

总的来说，如果确实要避免写时复制，必须显式地使用 `--reflink=never` 参数（若目标路径没有 +C 属性，先创建一个有 +C 属性的目录/空文件再覆盖它）。有关 `--reflink` 参数的更多信息请参阅 [cp(1)](<https://man.archlinux.org/man/cp.1>)。 

######  对快照的影响

如果为禁用了写时复制的文件创建快照，快照会锁定当前文件的数据块，因此首次写入该文件的块时[会触发写时复制](<https://www.spinics.net/lists/linux-btrfs/msg33090.html>)。但文件仍保留 +C 属性，故后续对同一文件块的写入仍为原地操作，直至下次创建快照。 

频繁快照会减弱 +C 属性的效果，因为在每次快照后的第一次写入都会触发写时复制。要避免这种情况，可以把所有禁用写时复制的文件放在一个单独的子卷中并避免为该子卷创建快照。 

###  压缩

Btrfs 支持[自动的透明压缩](<https://btrfs.readthedocs.io/en/latest/Compression.html>)，这不仅能缩减文件体积，还能通过减少写入放大来显著延长[闪存](<https://zh.wikipedia.org/wiki/%E9%97%AA%E5%AD%98> "zhwp:闪存")介质的使用寿命，详见 [Fedora:Changes/BtrfsByDefault#Compression](<https://fedoraproject.org/wiki/Changes/BtrfsByDefault#Compression> "fedora:Changes/BtrfsByDefault")、[[3]](<https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/NTV77NFF6NDZM3QTPUM2TQZ5PCM6GOO2/>) 与 [[4]](<https://pagure.io/fedora-btrfs/project/issue/36#comment-701551>)。在某些情况下（例如单线程、重文件 I/O 时），压缩可以[提升性能](<https://www.phoronix.com/scan.php?page=article&item=btrfs_compress_2635&num=1>)，而在其他场景中（如多线程和/或大文件I/O的CPU密集型任务），性能则会明显受影响。采用快速的压缩算法（`zstd` 和 `lzo`）通常性能也就越好。一些[基准测试](<https://www.phoronix.com/scan.php?page=article&item=btrfs-zstd-compress>)提供了详细的对比数据。 

####  压缩类型

Btrfs 支持的压缩算法有 `zlib`（即 [zlib](<https://zh.wikipedia.org/wiki/zlib> "zhwp:zlib") 库提供的 [DEFLATE](<https://zh.wikipedia.org/wiki/Deflate> "zhwp:Deflate") 压缩算法）、`lzo`（即 [LZO](<https://zh.wikipedia.org/wiki/LZO> "zhwp:LZO")）和 `zstd`（即 [zstd](<https://github.com/torvalds/linux/tree/master/lib/zstd>) 实现的 [Zstandard](<https://zh.wikipedia.org/wiki/Zstandard> "zhwp:Zstandard") 压缩算法）。其中 `lzo` 无压缩级别，而 `zlib` 和 `zstd` 可调整压缩级别（`zlib`：1～9；`zstd`：-15～-1、1～15，需为整数），级别越高压缩效果越好而所需时间越长。改变压缩级别对 CPU 和 I/O 吞吐的影响不一样，因此在变更前后最好进行检查和性能测试。关于压缩类型的更多信息，可参阅 [btrfs(5) § COMPRESSION](<https://man.archlinux.org/man/btrfs.5#COMPRESSION>)。 

**警告：** 如果使用 `zstd` 算法（尤其是 -15～-1 级别），使用较旧的内核或 [btrfs-progs](<https://archlinux.org/packages/?name=btrfs-progs>)包 的系统可能不能读取或修复该文件系统。

####  启用压缩

#####  为文件系统启用

挂载时指定 `compress=_算法[:级别]_` 挂载选项，对于文件系统中每次写入，Btrfs 将自动考虑是否启用压缩。其中的 `_算法_` 处可以填写 `zlib`、`lzo`、`zstd` 或 `no`（即不压缩），可选的 `_级别_` 处填写压缩级别，不填写或填写 0 时取默认值 3（`lzo` 不适用）。使用该选项时，Btrfs 会检测文件写入的数据的**首个数据块** 经压缩后体积是否缩小。如果缩小，则压缩本次写入的全部内容，否则文件会被标记为 `NOCOMPRESS`，整个写入过程**及该文件后续的所有写入过程** 都不会触发压缩 [[5]](<https://btrfs.readthedocs.io/en/latest/Compression.html#incompressible-data>)。这是为了防止等待所有待写入数据完全交付给 Btrfs 并进行尝试压缩后，磁盘才开始执行写入操作。 

**注意：**

  * 压缩挂载选项会在同一文件系统的所有挂载点（包括不同子卷与 bind 挂载）之间共享 [[6]](<https://btrfs.readthedocs.io/en/latest/Compression.html#incompressible-data>)。
  * 若文件的一次写入无法压缩，此后写入均不会进行压缩。

或者，您可以在 Btrfs 子卷上设置压缩属性，并且无论它如何挂载，它都会持久化并应用，使用 `btrfs property set / compression _alg_`，其中 `_alg_` 可以是 `zstd` 或 `zstd:_n_`，其中 `_n_` 是压缩级别。 

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 下文陈述的有关试验测试的结果缺少引用来源，且此处关于百分比的原文表述并不准确（故译文不一定正确）。 (在 [Talk:Btrfs](<../zh-cn/Talk:Btrfs.html>) 中讨论)

若改用 `compress-force=_算法[:级别]_` 挂载选项，Btrfs 会检查**每次写入** 的**每个数据块** 并分别决定是否压缩。在多个混合用途系统上进行的经验测试表明，使用 `compress-force=zstd` 相比使用 `compress=zstd` 能显著提高空间节省率（从 10% 提升到 20%），但这会导致 CPU 占用率无端（略微）升高且拖长写入所需时间。[官方 Btrfs 指导手册](<https://btrfs.readthedocs.io/en/latest/Compression.html#incompressible-data>)不推荐使用该选项。 

使用 `compress-force` 也会限制 extent 的最大大小，从而增加碎片化。[[1]](<#cite_note-1>)

只有在添加以上两个挂载选项之一后新建或修改的文件才会被自动压缩。 

**提示：** 在新的 Btrfs 上安装 Arch Linux 时，如果需要将其压缩后存储，需要在系统安装前就使用 `compress` 选项挂载，例如：`mount -o compress=zstd /dev/sd _xY_ /mnt/`，并注意在其 [fstab](<../zh-cn/Fstab.html> "Fstab") 中为根目录文件系统指定相同的 `compress` 挂载选项。

#####  为现有文件启用

要为现有文件启用压缩，可使用 `btrfs filesystem defragment -c _算法_` 命令，` _算法_` 处可选填为 `zlib`、`lzo` 或 `zstd`，使用 `-L` 选项指定压缩级别，否则使用默认值 3（`lzo` 不适用）。例如，执行以下命令可用 `zstd` 的 1 压缩级别重新压缩所有文件： 
    
    # btrfs -v filesystem defragment -r -czstd -L1 /
    
**警告：** defragment 操作会断开 [#写时复制（CoW）](<#%E5%86%99%E6%97%B6%E5%A4%8D%E5%88%B6%EF%BC%88CoW%EF%BC%89>)数据（包括通过 `cp` 复制的文件、[#快照](<#%E5%BF%AB%E7%85%A7>)和[#去重](<#%E5%8E%BB%E9%87%8D>)数据等）之间的 reflink，产生独立的文件，可能显著增加空间使用量 [[7]](<https://btrfs.readthedocs.io/en/latest/btrfs-filesystem.html#subcommand>)。

使用上面的方式压缩文件不会被持久化，其他写入操作将应用原有压缩设置。 

以下两种方式可以持久性启用对单个文件的压缩： 
    
    $ chattr +c _文件_
    
    $ btrfs property set _文件_ compression zstd
    
前一条命令使用的是从 ext2 文件系统继承的文件属性旧接口，灵活性不足，只能够使用默认的 `zlib` 压缩算法。后一条命令则可以指定压缩算法，但指定压缩级别尚未实现，因此采用默认值 3（`lzo` 不适用）。 

####  查看压缩类型和压缩率

[compsize](<https://archlinux.org/packages/?name=compsize>)包 接收一个包含文件或目录（可为整个 Btrfs 文件系统）的列表，输出其使用的压缩类型以及实际压缩率（压缩后大小/压缩前大小）。压缩前大小可能与其他程序（如 [du(1)](<https://man.archlinux.org/man/du.1>)）显示的数值不一致，因为每个 extent 都会被统计且只统计一次⸺即使有多个 [reflink](<https://btrfs.readthedocs.io/en/latest/Reflink.html#reflink>)，或其部分内容已不再使用但尚未被垃圾回收。 

`-x` 选项可限制在单一文件系统内执行，这在类似于 `compsize -x /` 的场景中非常有用，可以避免程序因尝试访问非 Btrfs 的子目录而导致整个运行的失败。 

###  子卷

“Btrfs 子卷是可独立挂载的 POSIX 文件树，而**不是** 也不能看作是**块设备** 。大多数其他 POSIX 文件系统只有一个可挂载根，而 Btrfs 不仅整个卷（称作‘顶层子卷’）可以挂载，每个子卷也可独立挂载；一个 Btrfs 卷可以包含不止一个文件树⸺包含一个‘文件森林’。Btrfs 子卷可以理解为一个 POSIX 文件命名空间。”[[8]](<https://archive.kernel.org/oldwiki/btrfs.wiki.kernel.org/index.php/SysadminGuide.html#Subvolumes>)

每个 Btrfs 文件系统都有一个 ID 为 5 的顶层子卷。这个子卷不能被移除或被其他子卷替代。顶层子卷在文件系统中的路径为 `/`，其他子卷则**嵌套** 在顶层子卷之下。子卷（不包括顶层子卷）可以在文件系统中移动，其路径可以发生变化，但子卷 ID 不可更改。 

默认情况下，挂载文件系统时会挂载顶层子卷。可以通过选项来[挂载指定子卷](<#%E6%8C%82%E8%BD%BD%E5%AD%90%E5%8D%B7>)。 

子卷的主要用途之一是[#快照](<#%E5%BF%AB%E7%85%A7>)。 

更多详细信息请参阅以下链接（英文）： 

  * [Btrfs 文档](<https://btrfs.readthedocs.io/en/latest/Subvolumes.html>)
  * [Btrfs Wiki SysadminGuide#Subvolumes](<https://archive.kernel.org/oldwiki/btrfs.wiki.kernel.org/index.php/SysadminGuide.html#Subvolumes>)
  * [Btrfs Wiki Trees](<https://archive.kernel.org/oldwiki/btrfs.wiki.kernel.org/index.php/Trees.html>)

####  创建子卷

要创建子卷，必须先挂载该 Btrfs 文件系统以使其要创建的路径可以访问（挂载根子卷或者上级子卷）。 
    
    # btrfs subvolume create _路径/子卷名_
    
例如，在 `/mnt` 所在子卷下创建子卷 `@sub`（路径为 `/mnt/@sub`）： 
    
    # btrfs subvolume create /mnt/@sub
    
**注意：**

  * 使用 `-p`（`--parents`）选项可以自动创建不存在的父目录。
  * Btrfs 中子卷名可以是任何有效的目录名，以 `@` 符号开头只是[timeshift](<https://archlinux.org/packages/?name=timeshift>)包的命名约定。
  * 如果顶层子卷没有挂载，而你想在其内部创建子卷，可以通过指定 `subvolid=5` 来临时挂载它。参见 [#挂载子卷](<#%E6%8C%82%E8%BD%BD%E5%AD%90%E5%8D%B7>)。

####  列出子卷

查看` _路径_`所属文件系统的所有子卷列表： 
    
    # btrfs subvolume list -t _路径_
    
使用 `-t` 选项会显示更易读的表格视图。 

####  删除子卷

删除子卷： 
    
    # btrfs subvolume delete _子卷路径_
    
如果子卷包含其他子卷，需要添加 `-R`（`--recursive`）选项来递归删除包含的所有子卷。子卷也可以当作常规目录删除（使用 `rm -r`、`rmdir`；但这样会比较慢）。 

####  挂载子卷

使用`subvol=_子卷路径（相对于顶层子卷）_`或`subvolid=_子卷ID_`选项来挂载子卷。通过在文件系统的顶层创建各种子卷，然后将其挂载到适当的挂载点，可以模拟传统的文件系统分区。 

例如，以下将顶层子卷挂载到 `/mnt/` 并创建两个名为 `subvol_root` 和 `subvol_home` 的子卷。当顶层子卷被卸载时，新的子卷将被挂载到 `/mnt/` 和 `/mnt/home/`： 
    
    # mount _device_ /mnt/ -o subvolid=5
    # btrfs subvolume create /mnt/subvol_root/
    # btrfs subvolume create /mnt/subvol_home/
    # umount /mnt/
    # mount -o subvol=/subvol_root _device_ /mnt/
    # mount -o subvol=/subvol_home --mkdir _device_ /mnt/home/
    
使用 `subvol` 挂载选项引用子卷时，需要使用相对于“顶层子卷”的路径。 

**提示：**

  * 子卷 ID 可通过[#列出子卷](<#%E5%88%97%E5%87%BA%E5%AD%90%E5%8D%B7>)显示。
  * 不将顶层子卷作为 `/` 挂载会使更改子卷布局的更加简单。因此，考虑创建一个子卷来作为 `/` 挂载（用以存放你的系统文件）。

**注意：** 译自 [btrfs(5) § MOUNT OPTIONS](<https://man.archlinux.org/man/btrfs.5#MOUNT_OPTIONS>)：“大多数挂载选项适用于**整个文件系统** ，因而只有第一个挂载的子卷的选项才会生效。这是由于尚未实现分子卷的选项处理，将来情况可能会改变。这意味着（例如）你无法使用挂载选项为每个子卷单独设置 `nodatacow`、`nodatasum` 或 `compress`。这最终应该会被修复，但事实证明在 Linux VFS 框架内正确实现是困难的。” 

有关目前及计划可以为每个子卷单独应用的挂载选项，请参阅 [Btrfs Wiki FAQ](<https://archive.kernel.org/oldwiki/btrfs.wiki.kernel.org/index.php/FAQ.html#Can_I_mount_subvolumes_with_different_mount_options.3F>)。 

**提示：** 最好使用 `subvol=_/path/to/subvolume_` 来挂载，而不是使用 subvolid，因为在恢复 [#快照](<#%E5%BF%AB%E7%85%A7>) 时，subvolid 可能会发生变化，从而需要更改挂载配置。

请参阅 [Snapper#建议的文件系统布局](<../zh-cn/Snapper.html#%E5%BB%BA%E8%AE%AE%E7%9A%84%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F%E5%B8%83%E5%B1%80> "Snapper")、[Btrfs SysadminGuide#Managing Snapshots](<https://archive.kernel.org/oldwiki/btrfs.wiki.kernel.org/index.php/SysadminGuide.html#Managing_Snapshots>) 和 [SysadminGuide#Layout](<https://archive.kernel.org/oldwiki/btrfs.wiki.kernel.org/index.php/SysadminGuide.html#Layout>)，了解使用子卷的文件系统布局的例子。 

有关 Btrfs 特有的挂载选项的完整列表，请参阅 [btrfs(5) § BTRFS SPECIFIC MOUNT OPTIONS](<https://man.archlinux.org/man/btrfs.5#BTRFS_SPECIFIC_MOUNT_OPTIONS>)。 

####  将子卷挂载为 /

如果要将子卷挂载为 `/`，要么[#更改默认子卷](<#%E6%9B%B4%E6%94%B9%E9%BB%98%E8%AE%A4%E5%AD%90%E5%8D%B7>)，要么在 `rootflags` [内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")中指定挂载子卷的选项（一些[引导加载程序](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F> "引导加载程序")可以自动添加，例如 [GRUB](<../zh-cn/GRUB.html> "GRUB") 的 `grub-mkconfig` 命令），并编辑 `/etc/fstab`。建议使用 `subvol=_子卷路径_` 而不是 `subvolid` 来挂载，因为后者可能在恢复[#快照](<#%E5%BF%AB%E7%85%A7>)之后发生变化，如果不同时更改挂载选项，系统将不能启动。 

如果你计划使用其中一种[同步和备份程序](<../zh-cn/%E5%90%8C%E6%AD%A5%E5%92%8C%E5%A4%87%E4%BB%BD%E7%A8%8B%E5%BA%8F.html> "同步和备份程序")，建议不要更改默认子卷，因为它会在恢复除默认子卷之外的其他子卷的快照时导致问题。例如，[Timeshift](<../zh-cn/Timeshift.html> "Timeshift")会相对于文件系统的默认子卷创建一个路径`timeshift-btrfs`来存储快照，并且建议为根和家目录使用一个单独的非默认子卷。 

####  更改默认子卷

如果没有提供 `subvol` 与 `subvolid` 选项，将挂载默认子卷。要将指定子卷设置为所在文件系统的默认子卷，执行： 
    
    # btrfs subvolume set-default _子卷路径_
    
或者使用： 
    
    # btrfs subvolume set-default _子卷ID_ _路径_
    
将` _路径_`所在文件系统的默认子卷设置为 ID 为` _子卷ID_` 的子卷。 

**提示：** 子卷ID可通过[#列出子卷](<#%E5%88%97%E5%87%BA%E5%AD%90%E5%8D%B7>)显示。

使用 `btrfs subvolume set-default` 更改默认子卷后，顶层子卷需要使用 `subvol=/` 或 `subvolid=5` 挂载选项挂载 [[9]](<https://btrfs.readthedocs.io/en/latest/Administration.html>)。 

**注意：**

  * [GRUB](<../zh-cn/GRUB.html> "GRUB") 的 `grub-mkconfig` 脚本**不** 遵守 Btrfs 的默认子卷设置⸺如果 `/` 是顶层子卷，始终不会指定 `subvol=/` 或 `subvolid=5` 挂载选项，可能导致无法启动；如果 `/` 非顶层子卷，始终会指定相应的 `subvol` 选项，导致无法仅通过设置默认子卷回退（[bug 报告](<https://savannah.gnu.org/bugs/?func=detailitem&item_id=66509>)）。目前可以通过手动修改 `grub.cfg` 中 `rootflags` [内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")解决（参见 [#挂载子卷](<#%E6%8C%82%E8%BD%BD%E5%AD%90%E5%8D%B7>)），或者使用工具自动在 [GRUB](<../zh-cn/GRUB.html> "GRUB") 中为快照创建启动项（参见 [#引导进入快照](<#%E5%BC%95%E5%AF%BC%E8%BF%9B%E5%85%A5%E5%BF%AB%E7%85%A7>)）。另外，如果 `grub.cfg` 的实际位置发生改变，例如包含 `/boot` 的子卷改变，需要再次运行 `grub-install`。详见[这个论坛帖子](<https://bbs.archlinux.org/viewtopic.php?pid=1615373>)。
  * 如果你打算使用某个[同步和备份程序](<../zh-cn/%E5%90%8C%E6%AD%A5%E5%92%8C%E5%A4%87%E4%BB%BD%E7%A8%8B%E5%BA%8F.html> "同步和备份程序")，不推荐更改默认子卷，以免在恢复非默认子卷的快照时出现问题。例如[Timeshift](<../zh-cn/Timeshift.html> "Timeshift")会在默认子卷下创建路径`timeshift-btrfs`来储存快照，为/和/home使用单独的非默认子卷比较好。

###  配额

[磁盘配额](<https://en.wikipedia.org/wiki/Disk_quota> "wikipedia:Disk quota")的概念在Unix世界有着悠久的传统。传统配额基于文件所有权，通过限制用户拥有的所有文件的总大小来控制空间使用。Btrfs采用了与传统Unix系统不同的配额设计理念，不支持传统的基于[用户或用户组](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html> "用户和用户组")的配额功能，这是因为其现代存储特性（如[#快照](<#%E5%BF%AB%E7%85%A7>)、[#写时复制（CoW）](<#%E5%86%99%E6%97%B6%E5%A4%8D%E5%88%B6%EF%BC%88CoW%EF%BC%89>)、[#去重](<#%E5%8E%BB%E9%87%8D>)和[#压缩](<#%E5%8E%8B%E7%BC%A9>)）使得传统配额的空间计算变得极其复杂且不准确 [[10]](<https://btrfs.readthedocs.io/en/latest/Qgroups.html>)。作为替代，Btrfs 采用基于子卷的配额机制，现提供两种实现机制⸺传统的[#配额组](<#%E9%85%8D%E9%A2%9D%E7%BB%84>)和较新的[#简单配额](<#%E7%AE%80%E5%8D%95%E9%85%8D%E9%A2%9D>)（在2023年底发布的6.7版本内核中引入）来实现类似的空间管理效果。虽然增加了管理复杂性，但提供了更灵活和精确的存储控制能力，且不用分区即可限制目录大小，支持动态调整配额。 

**注意：** 挂载Btrfs文件系统（或其中任一子卷）后才可以管理配额。

####  配额组

**警告：**

尽管[Btrfs 配额组](<https://btrfs.readthedocs.io/en/latest/Qgroups.html>)（quota group，简称 qgroup）在常规使用中被认为是稳定的，但启用配额组功能，尤其是在频繁创建大量快照的环境中，仍可能导致性能下降，特别是在删除快照时。配额组统计会引入额外的元数据开销，并可能在高强度快照工作负载下影响系统响应速度。 

近期的内核改进（5.15及后续版本）已修复诸多[历史问题](<https://archive.kernel.org/oldwiki/btrfs.wiki.kernel.org/index.php/Quota_support.html#Known_issues>)，但[某些限制依然存在](<https://lwn.net/Articles/944371/>)，特别是在深度嵌套的子卷或复杂的配额组层级结构等高级应用场景中。2016年就写在这里的建议⸺启用配额组前需审慎评估具体使用场景，至今仍然适用。请务必查阅最新的 [Btrfs 文档](<https://btrfs.readthedocs.io/en/latest/Qgroups.html>)获取当前详细信息。值得注意的是，为了解决配额组的性能问题，Btrfs引入了[#简单配额](<#%E7%AE%80%E5%8D%95%E9%85%8D%E9%A2%9D>)功能，提供了灵活性略差但性能更优的替代方案。

Btrfs精确的配额支持是通过子卷之上的配额组实现的。配额组使用配额组ID（qgroupid）表示，格式为` _层级_ /_ID_`。子卷的层级是0，`0/` 可以省略，而子卷对应的 `_ID_` 就是子卷的 ID，例如 `0/5` 表示顶层子卷的配额组，也可以用子卷路径代替 `0/_ID_` 的表示方式。配额组形成“树”状层级结构，但一个配额组可以有多个父配额组 [[11]](<https://btrfs.readthedocs.io/en/latest/Qgroups.html>)。叶子配额组层级为0，即子卷直接对应的配额组。所有更高层级配额组的 `_ID_` 可以自由指定。高层级配额组包含低层级配额组，相同层级之间不可嵌套，但层级不表示嵌套深度。例如，可以为 `5/100` 配额组分配子配额组 `0/5`。 

#####  总引用空间和独占引用空间

每个配额组主要追踪两个数值：**总引用空间** （total referenced space）和**独占引用空间** （exclusively referenced space）。其中**总引用空间** 是指所有能够从配额组内访问到的数据占用的存储空间，**独占引用空间** 是指只被配额组所属的**子卷** 引用（而不被该配额组以外的**子卷** 引用）的数据所占用的存储空间。 

#####  启用/禁用配额组

使用以下命令为` _路径_`所在文件系统启用配额组： 
    
    # btrfs quota enable _路径_
    
将 `enable` 改为 `disable` 以禁用配额组。 

**警告：** 禁用配额组会销毁当前所有配额组并解除其关系。

#####  创建/销毁配额组

子卷对应的0层级配额组始终会自动创建。即便子卷在启用配额前创建，启用配额时也会自动创建相应配额组。同样，[#删除子卷](<#%E5%88%A0%E9%99%A4%E5%AD%90%E5%8D%B7>)时子卷对应的配额组也会被删除，并自动解除与原包含有这一配额组的高层级配额组的关系。 

使用以下命令在` _路径_`所在文件系统创建配额组` _层级_ /_ID_`： 
    
    # btrfs qgroup create _层级_ /_ID_ _路径_
    
将 `create` 改为 `destroy` 以销毁配额组。销毁配额组类似于使用 `rm -d` 删除目录⸺如果配额组存在子配额组，必须先解除关系；如果仅存在父配额组，关系会自动解除。 

**注意：** 子卷对应的配额组不能直接删除，而应该通过直接删除子卷来自动删除。

#####  分配/删除子配额组

使用以下命令将` _路径_`所在文件系统的` _子配额组_`分配到` _父配额组_`，注意` _父配额组_`必须比` _子配额组_`层级更高： 
    
    # btrfs qgroup assign _子配额组_ _父配额组_ _路径_
    
将 `assign` 改为 `remove` 以解除这一关系。 

**注意：** 分配/解除分配子配额组后可能需要 [#配额重扫描](<#%E9%85%8D%E9%A2%9D%E9%87%8D%E6%89%AB%E6%8F%8F>)，这在当前版本中会自动触发，但可能造成性能消耗，详见[#配额重扫描](<#%E9%85%8D%E9%A2%9D%E9%87%8D%E6%89%AB%E6%8F%8F>)章节。

#####  限制/取消限制配额组

可以限制配额组的总引用空间或独占引用空间，或同时限制两者。例如，使用以下命令在` _路径_`所在文件系统中限制` _配额组_`的**总引用空间** 不超过 1 G**i** B： 
    
    # btrfs qgroup limit 1G _配额组_ _路径_
    
**注意：** 如果已[#启用压缩](<#%E5%90%AF%E7%94%A8%E5%8E%8B%E7%BC%A9>)，Btrfs目前仅支持限制压缩后的数据占据的空间。

其中` _配额组_`若省略，则会尝试将` _路径_`解释为子卷路径。添加选项 `-e`（到 `limit` 之后）改为限制**独占引用空间** 。将` _大小限制_`改为`none` 以取消限制。 

#####  列出配额组

使用以下命令列出` _路径_`所在文件系统的所有配额组： 
    
    # btrfs qgroup show _路径_
    
**注意：** 由于 `btrfs qgroup show` 使用的是磁盘中的数据，可能需要 `sync` 后才能显示准确的统计数据。为此可以添加 `--sync` 选项（到 `show` 之后），先对` _路径_`所在文件系统执行强制同步操作。

输出的“Path”列可能显示一些特殊值，含义如下： 

  * `<toplevel>`：顶层子卷对应的配额组。
  * `<under deletion>`：该配额组对应子卷已被删除（其目录已移除），但子卷元数据尚未完全清理。

**提示：** 可以使用 `btrfs subvolume sync _路径_ _子卷ID_` 等待` _路径_`所在文件系统中子卷完全删除（可以指定多个子卷 ID；若一个也没有指定则等待当前文件系统中所有待删除子卷删除完毕）。但请注意先卸载该子卷。

  * `<squota space holder>`：（仅适用于 [#简单配额](<#%E7%AE%80%E5%8D%95%E9%85%8D%E9%A2%9D>)）该配额组对应子卷已完全删除但相关统计信息仍保留。这是由于简单配额只将extent归属于首次分配它的子卷，而该子卷已完全删除但extent仍被其他子卷引用。

根据需求，可以添加一些显示选项（到 `show` 之后）。常用的选项有： 

  * `-p`：显示父配额组。
  * `-c`：显示子配额组。
  * `-r`：显示总引用空间限制。
  * `-e`：显示独占引用空间限制。
  * `-f`：仅列出` _路径_`所在子卷对应的配额组。
  * `-F`：仅列出` _路径_`所在子卷对应的配额组及包含这些配额组的高层级配额组。

更多选项请参阅 [btrfs-qgroup(8) § show](<https://man.archlinux.org/man/btrfs-qgroup.8#show>)。 

#####  配额重扫描

[配额重扫描](<https://btrfs.readthedocs.io/en/latest/btrfs-qgroup.html#quota-rescan>)（quota rescan）会读取文件系统中所有extent的元数据，据其更新各配额组的统计值。 

Btrfs的配额组可以处理许多复杂的extent共享和不再共享场景（包括子卷、子配额组的删除），同时保持总引用空间与独占引用空间的准确计数。但当配额组关系发生变化（手动 [#分配/解除分配子配额组](<#%E5%88%86%E9%85%8D/%E8%A7%A3%E9%99%A4%E5%88%86%E9%85%8D%E5%AD%90%E9%85%8D%E9%A2%9D%E7%BB%84>)）时，由于记录的数据不足（仅记录总引用空间与独占引用空间，而未明确记录哪些extent属于共享或独占），通常需要在整个文件系统内配额重扫描，此时配额组会被标记为“inconsistent”（不一致），即需要配额重扫描的状态。 

目前实现中唯一的例外是配额组的**总引用空间** 等于**独占引用空间** （即所有数据都为独占）时，仅需要在父配额组的总引用空间与独占引用空间上同时加上/减去该配额组的引用空间，不需要重新扫描配额。 

自4.19版本内核起，手动[#分配/解除分配子配额组](<#%E5%88%86%E9%85%8D/%E8%A7%A3%E9%99%A4%E5%88%86%E9%85%8D%E5%AD%90%E9%85%8D%E9%A2%9D%E7%BB%84>)时会自动触发配额重扫描（除了以上例外情况）。但考虑到其开销较大、同时只能进行一个操作、无法等待重扫描结束后再返回，可以在 `assign`/`remove` 之后添加 `--no-rescan` 选项以避免自动触发重扫描，转而在之后再手动触发。 

**提示：** 使用 `--no-rescan` 选项[#分配/解除分配子配额组](<#%E5%88%86%E9%85%8D/%E8%A7%A3%E9%99%A4%E5%88%86%E9%85%8D%E5%AD%90%E9%85%8D%E9%A2%9D%E7%BB%84>)后，若需要配额重扫描，会显示相应警告。也可以通过[#列出配额组](<#%E5%88%97%E5%87%BA%E9%85%8D%E9%A2%9D%E7%BB%84>)显示警告。

使用以下命令手动触发重新扫描` _路径_`所在文件系统的配额： 
    
    # btrfs quota rescan _路径_
    
命令运行后立即返回，添加 `-w`（`--wait`）选项（到 `rescan` 之后）以等待重新扫描结束（即使已开始）再返回。使用 `-W`（`--wait-norescan`）选项仅等待当前正在运行的重新扫描结束。使用 `-s`（`--status`）选项返回当前进度。 

####  简单配额

[#配额组](<#%E9%85%8D%E9%A2%9D%E7%BB%84>)可以处理许多复杂的extent共享和不再共享场景（包括子卷、子配额组的删除），同时维护总引用空间与独占引用空间的准确计数，但这种灵活性是有代价的：许多计算操作具有全局性，即当extent引用关系变更后，会影响到引用该extent的所有配额组的统计值。这可能导致事务提交速度下降并引发不可接受的延迟，尤其在快照数量激增的情况下更为明显。 

为解决配额组的这一局限，Btrfs还支持另一套配额规则体系：[简单配额](<https://btrfs.readthedocs.io/en/latest/Qgroups.html#simple-quotas-squota>)（simple quota，简称squota）。简单配额复用了配额组的API和层次结构模型，但不追踪共享与独占使用情况。相反，简单配额将所有extent归属于首次分配它的子卷。通过引入少量新的元数据记录，这样所有核算决策都能在涉及数据块本身的分配或释放操作的局部完成，完全避免了复杂且耗时的反向引用解析过程。 

简单配额需要在文件系统级别启用，在[启用配额组](<#%E5%90%AF%E7%94%A8/%E7%A6%81%E7%94%A8%E9%85%8D%E9%A2%9D%E7%BB%84>)的命令中添加 `-s`（`--simple`）选项（到 `enable` 之后）即可。注意若配额组已经开启，需要先[禁用配额组](<#%E5%90%AF%E7%94%A8/%E7%A6%81%E7%94%A8%E9%85%8D%E9%A2%9D%E7%BB%84>)再启用简单配额，否则不会生效 [[12]](<https://elixir.bootlin.com/linux/v6.16/source/fs/btrfs/qgroup.c#L1021-L1022>)。由于其简单的计算方法，简单配额模式下不需要（也不能）进行[#配额重扫描](<#%E9%85%8D%E9%A2%9D%E9%87%8D%E6%89%AB%E6%8F%8F>)。除了这两点外，简单配额的操作方式与配额组完全相同，但显示与限制使用的所谓“总引用空间”和“独占引用空间”都是通过上文所述方法（将所有extent归属于首次分配它的子卷）计算得到的值。由于简单配额需要记录首次分配extent的子卷，因此仅对启用后写入的extent生效，若在非空文件系统中启用简单配额，刚启用时统计值会是0，因此只有在空子卷启用简单配额限制后再写入数据，才能确保统计准确。 

###  提交间隔

Btrfs 默认设置 30 秒的事务提交（commit）间隔，即每 30 秒将新数据从内存同步到永久存储。可通过 `commit` 挂载参数（单位为秒）更改，例如修改 [fstab](<../zh-cn/Fstab.html> "Fstab")： 
    
    LABEL=arch64 / btrfs defaults,noatime,compress=lzo,commit=120 0 0
    
Btrfs 层面的周期性提交并非事务提交的唯一机制，该操作也可通过 `sync` 命令显式触发，或通过影响全局文件系统状态的其他命令间接触发，事务提交的机制还包括基于各类阈值或策略（如[控制组](<../zh-cn/%E6%8E%A7%E5%88%B6%E7%BB%84.html> "控制组")）进行刷新的内核机制，这超出了本文的范围，因此不再赘述。 

###  固态硬盘数据块异步丢弃

[TRIM 或丢弃（discard）](<https://btrfs.readthedocs.io/en/latest/Trim.html>)数据块是指文件系统通知固态硬盘哪些数据块不再使用的操作，从而固态硬盘能够在空闲时擦除（回收）这些数据块，避免等到需覆盖时再进行。内核 6.2 版本起默认启用异步丢弃功能：extent在释放事务提交后不会立即触发丢弃其包含的数据块，而是由独立的工作线程分组后统一进行，从而改善提交延迟。 

异步丢弃可以与[定期 TRIM](<../zh-cn/%E5%9B%BA%E6%80%81%E7%A1%AC%E7%9B%98.html#TRIM> "固态硬盘") 一同使用 [[13]](<https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/MLZIPQUXMJFRVSFJS6B2ACDKTYNSX3AX/>)。 

有关 TRIM 的更多信息，请参阅[固态硬盘#TRIM](<../zh-cn/%E5%9B%BA%E6%80%81%E7%A1%AC%E7%9B%98.html#TRIM> "固态硬盘")。 

##  使用

###  查看空间使用情况

因为不能同时考虑文件和元数据的使用情况，[df(1)](<https://man.archlinux.org/man/df.1>) 之类的通用用户空间工具在 Btrfs 上并不能准确地报告剩余空间大小。推荐使用 `btrfs filesystem usage` 来查看空间使用情况，例如： 
    
    # btrfs filesystem usage /
    
或者使用 `btrfs filesystem df` 快速检查已分配空间及其使用情况，无需 root 权限： 
    
    $ btrfs filesystem df /
    
**注意：** 对于 [#多设备文件系统](<#%E5%A4%9A%E8%AE%BE%E5%A4%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F>)，在 `RAID5` 或 `RAID6` [#profile](<#profile>) 与其它 profile 共存于同一文件系统时（例如，元数据使用 `DUP` 而数据使用 `RAID5`），`btrfs filesystem usage` 和 `btrfs filesystem df` 显示出的空间使用情况不准确 [[14]](<https://btrfs.readthedocs.io/en/latest/btrfs-man5.html#missing-incomplete-support>)。

更多信息可参阅 [[15]](<https://archive.kernel.org/oldwiki/btrfs.wiki.kernel.org/index.php/FAQ.html#How_much_free_space_do_I_have.3F>)。 

因为不考虑 [#写时复制（CoW）](<#%E5%86%99%E6%97%B6%E5%A4%8D%E5%88%B6%EF%BC%88CoW%EF%BC%89>)和透明 [#压缩](<#%E5%8E%8B%E7%BC%A9>)，[du(1)](<https://man.archlinux.org/man/du.1>) 和 [ncdu(1)](<https://man.archlinux.org/man/ncdu.1>) 之类的文件空间使用情况分析工具的数据也不准确。可考虑改用 [btdu](<https://aur.archlinux.org/packages/btdu/>)AUR 或 [compsize](<#%E6%9F%A5%E7%9C%8B%E5%8E%8B%E7%BC%A9%E7%B1%BB%E5%9E%8B%E5%92%8C%E5%8E%8B%E7%BC%A9%E7%8E%87>) 等支持 Btrfs 特性的工具。 

###  碎片整理

文件[碎片整理](<https://btrfs.readthedocs.io/en/latest/Defragmentation.html#>)是指尝试通过让文件包含的extent分布更加连续，合并小的extent，从而更有效地存储文件的过程。 

由于 Btrfs 的 [#写时复制（CoW）](<#%E5%86%99%E6%97%B6%E5%A4%8D%E5%88%B6%EF%BC%88CoW%EF%BC%89>)设计，修改文件时使用的新数据块在物理设备上可能与原数据块相距很远，造成文件的碎片化。碎片化在机械硬盘上是严重的问题，因为移动磁头到较远位置会导致延迟。对于现代没有这种延迟的设备（如固态硬盘）来说，这不再是问题，但进行碎片整理仍有意义，可以减少追踪分散extent所需的元数据大小。 

可以安全地碎片整理使用中的文件数据，但更难达到最优分布。 

**警告：** 碎片整理会断开[#写时复制（CoW）](<#%E5%86%99%E6%97%B6%E5%A4%8D%E5%88%B6%EF%BC%88CoW%EF%BC%89>)数据（包括通过 `cp` 复制的文件、[#快照](<#%E5%BF%AB%E7%85%A7>)和[#去重](<#%E5%8E%BB%E9%87%8D>)数据等）之间的 reflink，产生多份独立的数据，可能显著增加空间使用量 [[16]](<https://btrfs.readthedocs.io/en/latest/btrfs-filesystem.html#subcommand>)。

####  手动

使用 `btrfs filesystem defragment` 命令手动进行碎片整理，例如碎片整理根目录下的文件（不进入子卷、挂载点及到目录的软链接）： 
    
    # btrfs filesystem defragment -r /
    
**注意：** 不使用 `-r` 参数则碎片整理不会递归进行，但会对某些内部树⸺区段树（extent tree）和子卷树⸺进行碎片整理。这种设计容易引发混淆，未来版本可能会取消。

**提示：** 可以使用 `-c`、`-L` 参数指定压缩方式，参见压缩章节中 [#为现有文件启用](<#%E4%B8%BA%E7%8E%B0%E6%9C%89%E6%96%87%E4%BB%B6%E5%90%AF%E7%94%A8>)部分。

####  自动

使用挂载参数 `autodefrag` 启用自动碎片整理，参见 [btrfs(5) § MOUNT OPTIONS](<https://man.archlinux.org/man/btrfs.5#MOUNT_OPTIONS>)。 

### scrub

[scrub](<https://btrfs.readthedocs.io/en/latest/Scrub.html>)文件系统或设备是指验证其中所有数据和元数据的过程，能够检测数据校验和错误、基本超级块错误、基本元数据块头错误以及磁盘读取错误。 

**注意：** 运行中的检修任务会阻止系统挂起，详见[该讨论](<https://lore.kernel.org/linux-btrfs/20140227190656.GA28338@merlins.org/>)。

####  手动启动

使用以下命令在后台启动 scrub 任务（此处“设备”指 Linux 块设备）： 
    
    # btrfs scrub start _路径_ 或 _设备_
    
如果指定路径，则 scrub 路径所在的文件系统；如果指定设备，则 scrub 该设备。 

**注意：** 在使用镜像块组 [#profile](<#profile>)（如 RAID1）的 [#多设备文件系统](<#%E5%A4%9A%E8%AE%BE%E5%A4%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F>)上，scrub 操作还会通过从其他副本复制已验证完好的数据来自动修复任何损坏。

检查该任务的运行状态： 
    
    # btrfs scrub status /
    
也可以通过[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Help:阅读") `btrfs-scrub@.service` 来手动运行 scrub (使用同样的转移后路径)，相较 (以 root 用户身份运行) `btrfs scrub`，这么做的优点是输出内容会记录在 [Systemd 日志](<../zh-cn/Systemd/Journal.html> "Systemd/Journal")中。 

####  自动

[btrfs-progs](<https://archlinux.org/packages/?name=btrfs-progs>)包 软件包带有 `btrfs-scrub@.timer` 系统单元，用来每月运行 scrub 命令。通过添加挂载点的参数来[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Help:阅读")它，例如`btrfs-scrub@-.timer` (`/`) 或者 `btrfs-scrub@home.timer` (`/home`)。你可以使用`systemd-escape -p _/path/to/mountpoint_`来转义路径，参见[systemd-escape(1)](<https://man.archlinux.org/man/systemd-escape.1>)。 

### balance

‘balance 将会通过分配器再次传递文件系统中的所有数据。它主要用于在添加或删除设备时跨设备重新平衡文件系统中的数据。如果有设备出现故障，balance 将为指定的冗余 RAID 级别重新生成缺失的副本’[[17]](<https://btrfs.readthedocs.io/en/latest/Glossary.html>)。参阅[上游的 FAQ](<https://archive.kernel.org/oldwiki/btrfs.wiki.kernel.org/index.php/FAQ.html#What_does_.22balance.22_do.3F>)。 

在单设备文件系统上，balance 对于（临时）减少分配但未使用（元）数据块的数量也是有用的。有时候这对于解决 ["filesystem full" 故障](<https://archive.kernel.org/oldwiki/btrfs.wiki.kernel.org/index.php/FAQ.html#Help.21_Btrfs_claims_I.27m_out_of_space.2C_but_it_looks_like_I_should_have_lots_left.21>)来说也是必须的。为减少无法分配出元数据块组的可能，不建议对元数据进行 balance 操作，可指定如 `-dusage=30`只对数据块组操作。 
    
    # btrfs balance start --bg /
    # btrfs balance status /
    
###  交换文件

**注意：**

Btrfs 与 Linux 交换子系统的实现导致一些限制 [[18]](<https://btrfs.readthedocs.io/en/latest/btrfs-man5.html#swapfile-support>)： 

  * 不支持在跨设备的文件系统上使用交换文件
  * 数据 [#profile](<#profile>) 需为 `single`
  * 不能为含有正在使用中的交换文件的子卷创建快照
  * 交换文件必须预分配（即无空洞）
  * 必须单独为交换文件 [#禁用写时复制](<#%E7%A6%81%E7%94%A8%E5%86%99%E6%97%B6%E5%A4%8D%E5%88%B6>)（即交换文件必须有 `+C` 属性）

其中后两个对交换文件的限制 `btrfs filesystem mkswapfile` 命令会自动处理。 

交换文件的介绍参见 [Swap#交换文件](<../zh-cn/Swap.html#%E4%BA%A4%E6%8D%A2%E6%96%87%E4%BB%B6> "Swap")。 

在 Btrfs 中创建交换文件的正确方法是首先[创建一个子卷](<#%E5%88%9B%E5%BB%BA%E5%AD%90%E5%8D%B7>)存储交换文件，因为随后无法为该子卷创建快照。例如创建 `/swap` 子卷： 
    
    # btrfs subvolume create /swap 
    
**提示：** 考虑直接在顶层子卷下 [#创建子卷](<#%E5%88%9B%E5%BB%BA%E5%AD%90%E5%8D%B7>)，然后 [#挂载子卷](<#%E6%8C%82%E8%BD%BD%E5%AD%90%E5%8D%B7>)到 `/swap`（或其他可访问路径）。

在 `/swap/` 中创建一个 4 G**i** B 的交换文件 `swapfile`： 
    
    # btrfs filesystem mkswapfile --size 4g --uuid clear /swap/swapfile
    
`--size` 选项指定交换文件大小，默认为 2 GiB，最小 40 KiB。 

启用交换文件： 
    
    # swapon /swap/swapfile
    
最后编辑 [fstab](<../zh-cn/Fstab.html> "Fstab")，添加交换文件的配置： 
    
    /etc/fstab
    
    /swap/swapfile none swap defaults 0 0
    
更多信息参见 [fstab#用法](<../zh-cn/Fstab.html#%E7%94%A8%E6%B3%95> "Fstab")。 

有关删除交换文件等更多信息请参阅 [Swap#交换文件](<../zh-cn/Swap.html#%E4%BA%A4%E6%8D%A2%E6%96%87%E4%BB%B6> "Swap")。 

**提示：** 若要使用休眠功能，除了配置交换文件外，还需要完成[电源管理/挂起与休眠](<../zh-cn/%E7%94%B5%E6%BA%90%E7%AE%A1%E7%90%86/%E6%8C%82%E8%B5%B7%E4%B8%8E%E4%BC%91%E7%9C%A0.html> "电源管理/挂起与休眠")中描述的额外步骤。

### RAID

Btrfs 提供对 RAID [#多设备文件系统](<#%E5%A4%9A%E8%AE%BE%E5%A4%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F>)的原生支持。相较于使用 [mdadm](<../zh-cn/RAID.html> "Mdadm")，其显著优势包括自修复冗余阵列和在线数据平衡。更多信息请参见[该 Btrfs Wiki 页面](<https://archive.kernel.org/oldwiki/btrfs.wiki.kernel.org/index.php/Using_Btrfs_with_Multiple_Devices.html>)。[Btrfs SysadminGuide](<https://archive.kernel.org/oldwiki/btrfs.wiki.kernel.org/index.php/SysadminGuide.html#RAID_and_data_replication>) 提供了一些更具技术性的背景信息。 

**警告：** 奇偶校验 RAID（RAID 5/6）代码中存在多个严重的数据丢失漏洞。更多信息请参阅 Btrfs 文档的 [RAID 5/6 页面（英文）](<https://btrfs.readthedocs.io/en/latest/btrfs-man5.html#raid56-status-and-recommended-practices>)以及 linux-btrfs 邮件列表中[关于此问题的错误报告](<https://lore.kernel.org/linux-btrfs/8695beeb-f991-28c4-cf6b-8c92339e468f@inwind.it/>)。2020 年 6 月，有用户在上述邮件列表中整理发布了[当前问题的完整清单](<https://lore.kernel.org/linux-btrfs/20200627030614.GW10769@hungrycats.org/>)及[实用的恢复指南](<https://lore.kernel.org/linux-btrfs/20200627032414.GX10769@hungrycats.org/>)。

###  快照

"快照是和其它子卷共享数据和元数据的简单子卷, 利用了 btrfs 的写时复制特性。" 详见 [Btrfs Wiki SysadminGuide#Snapshots](<https://archive.kernel.org/oldwiki/btrfs.wiki.kernel.org/index.php/SysadminGuide.html#Snapshots>) 和 [the Btrfs documentation](<https://btrfs.readthedocs.io/en/latest/Subvolumes.html>)。 

要创建一个快照: 
    
    # btrfs subvolume snapshot _source_ [_dest_ /]_name_
    
`_source_`为要创建快照的对象，`[_dest_ /]_name_`为快照安放路径。 

加入 `-r` 参数可以创建一个只读快照. 为只读快照创建一个快照可以获得一个只读快照的可写入版本. 

**注意：**

  * 将一个只读快照通过`btrfs property set -f -ts '/path/to/snapshot' ro false`原位转换为可写快照是可能的。但并不推荐这样做，因为之后任何增量发送/接受（send/receive）操作会[造成问题](<https://lore.kernel.org/linux-btrfs/06e92a0b-e71b-eb21-edb5-9d2a5513b718@gmail.com/>)。创建一个新的可写快照可以预防这类问题。
  * 快照不是递归包含的，这意味着子卷内的子卷在快照里是空目录。

###  发送和接收

可以通过 `send` 命令发送一个快照,通常会与 btrfs 中的 `receive` 组成管道.例如将快照 `/root_backup` (也许是`/`的备份) 发送到 `/backup`: 
    
     # btrfs send /root_backup | btrfs receive /backup
    
_只能_ 发送只读快照,上面的命令在将子卷复制到外部设备 (例如备份驱动器) 时会很有用。 

接受结束后将创建对应子卷，无需手动再创建。 

还有一个例子创建了`/mnt/arch-v2/subvolumes/@var`子卷： 
    
    # btrfs send --proto 2 --compressed-data '/mnt/arch/snapshots/@var' | btrfs receive '/mnt/arch-v2/subvolumes/'
    
参数`--proto 2`和`--compressed-data`在本例中能够更有效地发送快照（假设数据可压缩）。 

也可以只发送两个快照间发生变化的部分,例如如果你已经发送了快照 `root_backup` ,然后又建立了一个新的只读快照 `root_backup_new` ,可以这样完成增量发送: 
    
     # btrfs send -p /root_backup /root_backup_new | btrfs receive /backup
    
现在你 `/backup` 的快照会是 `root_backup_new`。 

参阅 [Btrfs Wiki 上关于增量备份的页面 (英文)](<https://archive.kernel.org/oldwiki/btrfs.wiki.kernel.org/index.php/Incremental_Backup.html>) 获得更多信息 (例如使用工具自动化这一过程)。 

###  去重

使用写时复制，Btrfs 能够复制文件或整个子卷而无需实际复制数据。但是，无论何时更改文件，都会创建一个新的“真正的”副本。重复数据删除更进一步，通过主动识别含有相同内容的数据块并将它们通过 CoW 合并到同一个extent内。 

专用于 Btrfs 分区去重的工具包括 [duperemove](<https://archlinux.org/packages/?name=duperemove>)包和[bees](<https://archlinux.org/packages/?name=bees>)包。也许你还希望基于文件的级别对数据进行重复数据删除，比如 [rmlint-git](<https://archlinux.org/packages/?name=rmlint-git>)包、[rdfind](<https://archlinux.org/packages/?name=rdfind>)包、[jdupes](<https://aur.archlinux.org/packages/jdupes/>)AUR 或者 [dduper-git](<https://aur.archlinux.org/packages/dduper-git/>)AUR。有关这些程序的可用功能的概述和其他信息，请参阅[上游 Wiki 条目 (英文)](<https://btrfs.readthedocs.io/en/latest/Deduplication.html>)。 

###  调整大小

**警告：** 为避免数据丢失，确保在调整大小前备份好你的数据。

你可以增加文件系统的大小到设备的最大可用空间，或到一个指定大小。确保你在尝试增加文件系统大小前设备或逻辑卷有足够空间。 当指定一个设备上的文件系统到指定大小时，不论增加或减少，确保新的大小满足下面的条件： 

  * 新的大小必须大于已有数据的大小，否则会导致数据损失。
  * 新的大小必须等于或小于当前设备的可用空间。

**注意：** 如果你还计划减小文件系统所在的逻辑卷大小，请先减小文件系统大小后再尝试减小逻辑卷的大小。

将文件系统扩展到设备的最大可用大小： 
    
    # btrfs filesystem resize max /
    
将文件系统扩展到特定大小： 
    
    # btrfs filesystem resize _size_ /
    
将 `_size_` 替换为你需要的大小（按字节计算）。也可以为大小指定单位，如K（千字节），M（兆字节）或G（吉字节）。 或者也可以通过在大小前添加前缀指定增加（+）或减少（-）的变化量： 
    
    # btrfs filesystem resize +_size_ /
    # btrfs filesystem resize -_size_ /
    
##  已知问题

一些在尝试之前应该知道的限制。 

###  加密

Btrfs 暂未内置加密支持，但当前正进行一项基于 [Fscrypt](</wzh/index.php?title=Fscrypt&action=edit&redlink=1> "Fscrypt（页面不存在）")（英语：[Fscrypt](<https://wiki.archlinux.org/title/Fscrypt> "en:Fscrypt")） 的加密集成工作 [[19]](<https://lore.kernel.org/linux-btrfs/20240124195831.GA1212739@perftesting/T/>)。 

不过用户仍可在运行 `mkfs.btrfs` 前加密**分区** ，具体参见 [dm-crypt/加密整个系统](<../zh-cn/Dm-crypt/%E5%8A%A0%E5%AF%86%E6%95%B4%E4%B8%AA%E7%B3%BB%E7%BB%9F.html> "Dm-crypt/加密整个系统")。另一种方案是采用[栈式文件系统加密](<../zh-cn/%E9%9D%99%E6%80%81%E6%95%B0%E6%8D%AE%E5%8A%A0%E5%AF%86.html#%E6%A0%88%E5%BC%8F%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F%E5%8A%A0%E5%AF%86> "静态数据加密")。 

###  检查 btrfs 文件系统问题

`btrfs check` 工具目前有一些已知问题，在继续深入阅读了解之前，您不应该直接运行它, 参见 [#检查 Btrfs 文件系统](<#%E6%A3%80%E6%9F%A5_Btrfs_%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F>)小节。 

##  提示和技巧

###  无分区 Btrfs 磁盘

**警告：** 这种配置不建议用于启动设备，推荐设置一个单独的[EFI 系统分区](<../zh-cn/EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA.html> "EFI 系统分区")和Btrfs分区。 此外，GRUB 强烈反对安装GRUB到无分区磁盘。

Btrfs 能占用整个存储设备，使用[子卷](<#%E5%AD%90%E5%8D%B7>)模拟分区表来替代 [MBR](<../zh-cn/%E5%88%86%E5%8C%BA.html#%E4%B8%BB%E5%BC%95%E5%AF%BC%E8%AE%B0%E5%BD%95> "MBR") 或 [GPT](<../zh-cn/%E5%88%86%E5%8C%BA.html#GUID_%E5%88%86%E5%8C%BA%E8%A1%A8> "GPT") 分区表。虽然无分区磁盘不需要使用其它方法创建分区，然后在一个分区上[创建 Btrfs 文件系统](<#%E5%88%9B%E5%BB%BA%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F>)，但在单个磁盘上使用无分区配置存在一些限制： 

  * 不能在同一磁盘上的不同分区上创建其它的[文件系统](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html> "文件系统")。
  * 受上一条影响，无法在该磁盘上创建[EFI 系统分区](<../zh-cn/EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA.html> "EFI 系统分区")。需要额外的储存设备用于 [UEFI](<../zh-cn/UEFI.html> "UEFI") 启动。

运行下面的命令把整个设备的分区表替换成 Btrfs: 
    
    # mkfs.btrfs /dev/sd _X_
    
如果设备上存在分区表，则需要使用： 
    
    # mkfs.btrfs -f /dev/sd _X_
    
例如， 指定`/dev/sda` 而不是 `/dev/sda1`。后一种形式会格式化现有的分区而不是替换掉原有的分区表。由于根分区是 Btrfs 文件系统，请确保已将 `btrfs` 编译进内核, 或者将 `btrfs` 放入 [Mkinitcpio#模块（MODULES）](<../zh-cn/Mkinitcpio.html#%E6%A8%A1%E5%9D%97%EF%BC%88MODULES%EF%BC%89> "Mkinitcpio")中并且[重新生成 initramfs](<../zh-cn/Mkinitcpio.html#%E5%88%9B%E5%BB%BA%E5%92%8C%E5%90%AF%E7%94%A8%E9%95%9C%E5%83%8F> "Mkinitcpio")。 

像使用普通的 MBR 分区表存储设备一样安装[引导加载程序](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F> "引导加载程序"), 参考 [Syslinux#手动安装](<../zh-cn/Syslinux.html#%E6%89%8B%E5%8A%A8%E5%AE%89%E8%A3%85> "Syslinux")或 [GRUB/技巧和窍门#安装到分区上或者无分区磁盘上](<../zh-cn/GRUB/%E6%8A%80%E5%B7%A7%E5%92%8C%E7%AA%8D%E9%97%A8.html#%E5%AE%89%E8%A3%85%E5%88%B0%E5%88%86%E5%8C%BA%E4%B8%8A%E6%88%96%E8%80%85%E6%97%A0%E5%88%86%E5%8C%BA%E7%A3%81%E7%9B%98%E4%B8%8A> "GRUB/技巧和窍门")。 如果你的内核因为 `Failed to mount /sysroot.` 错误无法启动, 请在 `/etc/default/grub` 里添加 `GRUB_PRELOAD_MODULES="btrfs"` 并重新[生成](<../zh-cn/GRUB.html#%E7%94%9F%E6%88%90%E4%B8%BB%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6> "GRUB") GRUB 配置文件 。 

###  从 Ext3/4 转换

**警告：** Btrfs 的邮件列表中报告了多起转换不完整/损坏/失败的案例。在开始之前请确定您有 _可用的_ 备份并且愿意承担丢失数据的风险。 参见Btrfs维基的[Convert](<https://btrfs.readthedocs.io/en/latest/Convert.html>)页。

从安装 CD 启动，然后转化分区： 
    
    # btrfs-convert /dev/_partition_
    
挂载转换后的分区并修改 `/etc/fstab` 文件，指定分区类型 (**type** 为 btrfs，并且 **fs_passno**[最后一列] 要修改为0，因为 Btrfs 在启动时并不进行磁盘检查)。 还要注意的是分区的 UUID 将有改变，所以使用 UUID (指定分区) 时，请更新 fstab 中相应的条目。 `chroot` 到系统并重建你的[引导加载程序](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F> "引导加载程序")（如果对此过程不熟悉，参考[从现有 Linux 发行版安装 Arch Linux](<../zh-cn/%E4%BB%8E%E7%8E%B0%E6%9C%89_Linux_%E5%8F%91%E8%A1%8C%E7%89%88%E5%AE%89%E8%A3%85_Arch_Linux.html> "从现有 Linux 发行版安装 Arch Linux") )。 如果转换了根文件系统，还需要在 chroot 环境中[重建初始化内存盘](<../zh-cn/Mkinitcpio.html#%E5%88%9B%E5%BB%BA%E5%92%8C%E5%90%AF%E7%94%A8%E9%95%9C%E5%83%8F> "Mkinitcpio")以确保系统正确启动。 

**注意：**

  * 如果转换过程中有任何异样，不管是无法挂载新转换的 Btrfs 文件系统或是无法往其中写入数据，只要备份子卷 `/ext2_saved` 还在，就可以进行回滚。请使用 `btrfs-convert -r /dev/_partition_` 命令进行回滚，这将会丢弃任何对新转换 Btrfs 文件系统的更改。
  * 如果挂载已转换的 ext 分区时出现如下错误：`ERROR: dev extent devid 1 physical offset XXX len XXX is beyond device boundary XXX`，那么在分区末尾预留一些空闲空间后，转换可能会成功。请先回滚转换，然后使用 `resize2fs` 将分区缩小 50000 个块，再扩大 5000 个块（从而创建出 45000 个空闲块）。然后再次尝试转换。参见 [上游 bug 报告](<https://bugzilla.kernel.org/show_bug.cgi?id=206995>)。

确认没有问题后，通过删除 `ext2_saved` 备份子卷完成转换的最后一步。请注意，如果没了它 (备份子卷)，你将没办法还原回 ext3/4 文件系统。 
    
    # btrfs subvolume delete /ext2_saved
    
最后通过[数据平衡](<#%E6%95%B0%E6%8D%AE%E5%B9%B3%E8%A1%A1_\(Balance\)>)回收空间。 

别忘了先前安装的一些应用需要额外设置来适配Btrfs。 

**注意：** Ext3/4 转换到 Btrfs 的过程很耗时。一个普通机械硬盘上的4TB文件系统转换耗时可高达10小时。

###  从 NTFS 转换

使用 [ntfs2btrfs](<https://aur.archlinux.org/packages/ntfs2btrfs/>)AUR 或 [ntfs2btrfs-git](<https://aur.archlinux.org/packages/ntfs2btrfs-git/>)AUR 转换NTFS分区。 卸载目标文件系统并运行转换，并指定确切的压缩和校验和类型： 
    
    # ntfs2btrfs -c zstd -h crc32c /dev/partition
    
如果转换后一切正常，你可以删除原本用于恢复原始文件系统的 `image/ntfs.img` 。 

####  转换后

**警告：** 只有在确认不会恢复到原始文件系统后，才执行这些步骤，因为它们会使得恢复变得不可能，即使你保留了恢复文件。

可以在将现有文件系统转换为 Btrfs 后采取一些步骤使文件数据更连续。 
    
    # btrfs filesystem defrag -v -r -f -t 32M /mnt/filesystem
    
[#Balance](<#Balance>) 使 Btrfs 元数据更加紧凑 

###  损坏恢复

**警告：**`btrfs check` 工具有一些已知问题，参见 [#检查 Btrfs 文件系统](<#%E6%A3%80%E6%9F%A5_Btrfs_%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F>) 小节。

_btrfs-check_ 不能在一个已挂载的文件系统上工作。为了能够在不从 Live USB 启动的情况下使用 _btrfs-check_ ，需要将其添加到初始内存盘： 
    
    /etc/mkinitcpio.conf
    
    BINARIES=(btrfs)

然后[重新生成 initramfs](<../zh-cn/Mkinitcpio.html#%E5%88%9B%E5%BB%BA%E5%92%8C%E5%90%AF%E7%94%A8%E9%95%9C%E5%83%8F> "Mkinitcpio")。 

之后如果启动时出现问题，则可以使用该实用程序进行修复。 

**注意：** 如果 fsck 进程必须使空间缓存 (和/或其他缓存？) 无效 (invalidate cache)，那么随后的引导会挂起一段时间，这是正常的（进程可能会给出关于 btrfs-transaction 挂起的控制台消息）。系统应该在一段时间后从中恢复正常。

查阅 [btrfs-check(8)](<https://man.archlinux.org/man/btrfs-check.8>) 以获取更多信息。 

###  引导进入快照

要引导进入快照，因为快照可以像子卷那样被挂载，所以请像挂载子卷为根分区那样进行同样的流程 (已交代于[#挂载子卷为根挂载点](<#%E6%8C%82%E8%BD%BD%E5%AD%90%E5%8D%B7%E4%B8%BA%E6%A0%B9%E6%8C%82%E8%BD%BD%E7%82%B9>)的一段中)。 

  * 如果使用 [GRUB](<../zh-cn/GRUB.html> "GRUB")，则可以在 [grub-btrfs](<https://archlinux.org/packages/?name=grub-btrfs>)包 或 [grub-btrfs-git](<https://aur.archlinux.org/packages/grub-btrfs-git/>)AUR 的帮助下，在重新生成配置文件时使用 Btrfs 快照自动填充启动菜单。

  * 如果使用 [rEFInd](<../zh-cn/REFInd.html> "REFInd")，则可以在 [refind-btrfs](<https://aur.archlinux.org/packages/refind-btrfs/>)AUR 的帮助下，[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `refind-btrfs.service`后，在重新生成配置文件时使用 Btrfs 快照自动填充启动菜单。

  * 如果使用 [Limine](</wzh/index.php?title=Limine&action=edit&redlink=1> "Limine（页面不存在）")（英语：[Limine](<https://wiki.archlinux.org/title/Limine> "en:Limine")），可安装 [limine-snapper-sync](<https://aur.archlinux.org/packages/limine-snapper-sync/>)AUR。该工具在启用 `limine-snapper-sync.service` 后，每当 [Snapper](<../zh-cn/Snapper.html> "Snapper") 列表变更时，将自动在启动菜单中生成快照条目。详情参见 [Lamine#Btrfs 的 Snapper 快照集成](</wzh/index.php?title=Lamine&action=edit&redlink=1> "Lamine（页面不存在）")（英语：[Limine#Snapper snapshot integration for Btrfs](<https://wiki.archlinux.org/title/Limine#Snapper_snapshot_integration_for_Btrfs> "en:Limine")）。

###  搭配 systemd-nspawn 使用 Btrfs 子卷

可查阅 [systemd-nspawn#使用Btrfs子卷作为容器的根](<../zh-cn/Systemd-nspawn.html#%E4%BD%BF%E7%94%A8Btrfs%E5%AD%90%E5%8D%B7%E4%BD%9C%E4%B8%BA%E5%AE%B9%E5%99%A8%E7%9A%84%E6%A0%B9> "Systemd-nspawn")和 [systemd-nspawn#在 systemd-nspawn 中运行 docker](<../zh-cn/Systemd-nspawn.html#%E5%9C%A8_systemd-nspawn_%E4%B8%AD%E8%BF%90%E8%A1%8C_docker> "Systemd-nspawn") 等文章。 

###  减少访问时间元数据的更新

由于Btrfs的写时复制性质，访问文件就能够触发元数据的写时复制。减少访问时间的更新频率可能会消除这种不希望的硬盘使用并提高性能。参见[Fstab#atime 参数](<../zh-cn/Fstab.html#atime_%E5%8F%82%E6%95%B0> "Fstab")

###  增量备份到外置设备

下列包利用 `btrfs send` 和 `btrfs receive` 将备份增量发送到外置设备上。 参考它们的文档来查看实现，功能和需求的不同。 

  * **btrbk** — Btrfs子卷的快照和远程备份工具

     <https://github.com/digint/btrbk> || [btrbk](<https://archlinux.org/packages/?name=btrbk>)包

  * **snap-sync** — 使用[Snapper](<../zh-cn/Snapper.html> "Snapper")快照并备份到外置设备或远程机器

     <https://github.com/wesbarnett/snap-sync> || [snap-sync](<https://archlinux.org/packages/?name=snap-sync>)包

下列工具运行备份snapper快照到非Btrfs文件系统。 

  * **snapborg** — 一个类似borgmatic的工具，将snapper快照与[borg](<https://archlinux.org/packages/?name=borg>)包整合起来

     <https://github.com/enzingerm/snapborg> || [snapborg](<https://aur.archlinux.org/packages/snapborg/>)AUR

###  自动快照

要管理并自动创建快照，你可以使用像[Snapper](<../zh-cn/Snapper.html> "Snapper")，[Timeshift](<../zh-cn/Timeshift.html> "Timeshift")或[Yabsnap](<../zh-cn/Yabsnap.html> "Yabsnap")这样的快照管理器。 

###  自动通知

桌面通知能帮助您及时察觉严重的 Btrfs 问题，相较于完全不提供通知，能提供更好的问题感知。 

[btrfs-desktop-notification](<https://aur.archlinux.org/packages/btrfs-desktop-notification/>)AUR 为以下事件提供桌面通知： 

  * 启动进入任何只读快照或系统时
  * dmesg 日志中出现 Btrfs 警告、错误或致命消息

更多信息及配置方法，请参见 <https://gitlab.com/Zesko/btrfs-desktop-notification> . 

###  空间缓存v1正在被弃用

如果你的 Btrfs 文件系统是用旧的默认设置创建的，你可能会在你的系统日志中看到类似的警告: 
    
    BTRFS warning (device sdb4): space cache v1 is being deprecated and will be removed in a future release, please use -o space_cache=v2

将 Btrfs 空间缓存从旧版 v1 格式转换为新版 v2 格式并解决此警告. 你可以修改分区挂载选项，在 [fstab](<../zh-cn/Fstab.html> "Fstab") 中包含 `space_cache=v2` 或者手动进行转换： 
    
    # umount /dev/_partition_
    # mount /dev/_partition_ -o rw,space_cache=v2 /mnt
    # umount /mnt
    
**注意：** 在此转换后，Btrfs会在文件系统上设置一个compat-ro功能标志。因此，该文件系统可能无法再被非常旧的Btrfs内核实现挂载。

##  疑难解答

请查阅 [Btrfs 疑难解答](<https://btrfs.readthedocs.io/en/latest/trouble-index.html>)和[Btrfs 常见问答集（英文）](<https://archive.kernel.org/oldwiki/btrfs.wiki.kernel.org/index.php/Problem_FAQ.html>)以获得排除一般问题的信息。 

###  启动缓慢

有时，大于4TB的Btrfs卷需要较长时间才能挂载，从而导致系统启动变慢。 将群组树更改为块组树有助于解决该问题： 
    
    # btrfstune --convert-to-block-group-tree /dev/device
    
### GRUB

####  分区偏移

**注意：** 当您试图将 `core.img` 嵌入到已分区磁盘上时，可能会发生偏移问题。这意味着[可以](<../Special:Diff/319474.html> "Special:Diff/319474")将 GRUB 的 `corg.img` 直接嵌入到无分区磁盘 (例如 `/dev/sd _X_`) 上的 Btrfs 存储池中。

[GRUB](<../zh-cn/GRUB.html> "GRUB") 可以引导启动 Btrfs 分区，但是因为模块可能会比其它[文件系统](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html> "文件系统")大，`grub-install` 生成的 `core.img` 文件超过了 MBR 与第一个分区之间的空间大小 (63 扇区/31.5KiB)。最新版的 `fdisk` 和 `gdisk` 等磁盘工具会通过第一个分区前空出 1-2MiB 的空间来避免此问题。 

####  根丢失

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** Suggests editing a non-configuration file manually.（在 [Talk:Btrfs#Should not suggest to edit files in /usr/share](<../zh-cn/Talk:Btrfs.html#Should_not_suggest_to_edit_files_in_/usr/share> "Talk:Btrfs") 中讨论）

当从一个RAID配置的系统中启动用户可能会遇到错误：`error no such device: root`。编辑`/usr/share/grub/grub-mkconfig_lib`，移除行`echo " search --no-floppy --fs-uuid --set=root ${hints} ${fs_uuid}"`中的两个引号。重新生成grub的配置文件，后系统应该能够正常启动。 

**警告：** 不建议覆盖软件包提供的文件，因其会在下次更新时被覆盖。

###  挂载超时

有时（尤其在大型 RAID1 阵列上）系统启动时会出现挂载超时的现象，并带有如下日志信息： 
    
    Jan 25 18:05:12 host systemd[1]: storage.mount: Mounting timed out. Terminating.
    Jan 25 18:05:46 host systemd[1]: storage.mount: Mount process exited, code=killed, status=15/TERM
    Jan 25 18:05:46 host systemd[1]: storage.mount: Failed with result 'timeout'.
    Jan 25 18:05:46 host systemd[1]: Failed to mount /data.
    Jan 25 18:05:46 host systemd[1]: Startup finished in 32.943s (firmware) + 3.097s (loader) + 7.247s (kernel)>
    Jan 25 18:05:46 host kernel: BTRFS error (device sda): open_ctree failed

这可以通过 [fstab](<../zh-cn/Fstab.html> "Fstab") 中特定的 systemd 挂载选项 `x-systemd.mount-timeout` 提供系统以更长的超时时间来轻松解决。例如： 
    
     UUID=_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx_  /data  btrfs  rw,relatime,x-systemd.mount-timeout=5min  0 0
    
###  出现 BTRFS: open_ctree failed 错误

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 内容过时。自从systemd和udev都使用systemd-udevd后，用systemd替换udev钩子没有任何意义。（在 [Talk:Btrfs](<../zh-cn/Talk:Btrfs.html>) 中讨论）

截至 2014 年 11 月，一个似乎存在于 [systemd](<../zh-cn/Systemd.html> "Systemd") 或 [mkinitcpio](<../zh-cn/Mkinitcpio.html> "Mkinitcpio") 中的 Bug 可能会导致在 `mkinitcpio.conf` 中使用 `btrfs` 钩子（hook）的用户在启动多设备文件系统的 Btrfs 卷时遇到以下错误： 
    
    BTRFS: open_ctree failed
    mount: wrong fs type, bad option, bad superblock on /dev/sdb2, missing codepage or helper program, or other error
    
    In some cases useful info is found in syslog - try dmesg|tail or so.
    
    You are now being dropped into an emergency shell.
    
一种解决办法是，在`/etc/mkinitcpio.conf`中，将 `HOOKS` 中的 `btrfs` 移入 `MODULES` 中，然后[重新生成 initramfs](<../zh-cn/Mkinitcpio.html#%E5%88%9B%E5%BB%BA%E5%92%8C%E5%90%AF%E7%94%A8%E9%95%9C%E5%83%8F> "Mkinitcpio") 并重新启动。 

另外，如果在挂载 RAID 卷组缺少某个卷时，也有可能会发生这个错误。这种情况下，需要把 `degraded` 加入到 `/etc/fstab` 中；如果根目录在卷组上，需要同时加入[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数") `rootflags=degraded`。 

接上文，截至 2016 年 8 月，针对这一问题，一个可能的解决方案是在 `/etc/fstab` 中仅靠单个硬盘来挂载阵列，然后让 Btrfs 自动发现并追加其它硬盘。UUID 和 LABEL 等基于组的标识符似乎是导致出现错误的原因。比如说，由“disk1”（磁盘 1） 和“disk2”（磁盘 2）组成的双设备 RAID1 阵列会被分配到一个 UUID。但是请在 `/etc/fstab` 中只使用 `/dev/mapper/disk1` 来指定磁盘阵列，而不要使用 UUID。更多解释，参见这个[博客文章](<https://web.archive.org/web/20161108175034/http://blog.samcater.com/fix-for-btrfs-open_ctree-failed-when-running-root-fs-on-raid-1-or-raid10-arch-linux/>)。 

另一个可能的解决方法是在 [mkinitcpio.conf](<../zh-cn/Mkinitcpio.html> "Mkinitcpio") 中移除 `udev` 钩子并替换为 `systemd` 钩子。此时 `btrfs` _不应_ 出现在 `HOOKS` 或 `MODULES` 列表中。 

请查阅[原论坛讨论](<https://bbs.archlinux.org/viewtopic.php?id=189845>)和 [FS#42884](<https://bugs.archlinux.org/task/42884>) 获得更多的讨论内容和信息。 

###  检查 Btrfs 文件系统

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** "大开发阶段"状态已经过时。 (在[Talk:Btrfs](<../zh-cn/Talk:Btrfs.html>)讨论)

**警告：** Btrfs（特别是 `btrfs check` 命令工具）仍处在大开发阶段，强烈建议在加上 `--repair` 参数运行 `btrfs check` 前先做一个[备份](<../zh-cn/%E7%B3%BB%E7%BB%9F%E7%BB%B4%E6%8A%A4.html#%E5%A4%87%E4%BB%BD> "备份")，并提前查阅 [btrfs-check(8)](<https://man.archlinux.org/man/btrfs-check.8>)。

[btrfs-check(8)](<https://man.archlinux.org/man/btrfs-check.8>) 可以检查并修复一个未挂载的 Btrfs 文件系统。但是由于它尚未开发完成，它并不能修复某些错误（即使这些错误没有导致文件系统无法挂载）。 

###  持续的硬盘活动

自[内核](<../zh-cn/%E5%86%85%E6%A0%B8.html> "内核")版本6.2开始， [mount(8)](<https://man.archlinux.org/man/mount.8>) 默认启用 `discard=async` 选项。 这个设置[被报告](<https://lore.kernel.org/linux-btrfs/Y%2F%2Bn1wS%2F4XAH7X1p@nz/#r>)会造成硬盘的持续活动（甚至是待机状态下），因为丢弃队列填充的速度快于其处理速度。这会造成电源使用增加，特别是NVMe设备。 

到了内核版本6.3后，问题的解决办法是将`iops_limit`默认值从100改为1000。在旧版内核上，你可以手动设置到一个需要的值，例如： 
    
    # echo 1000 > /sys/fs/btrfs/_uuid_ /discard/iops_limit
    
其中` _uuid_`是btrfs文件系统的UUID。限制值`1000`需要通过实验进行调整。 

要在启动时设置该参数，可能要用到[Systemd#systemd-tmpfiles - 临时文件](<../zh-cn/Systemd.html#systemd-tmpfiles_-_%E4%B8%B4%E6%97%B6%E6%96%87%E4%BB%B6> "Systemd")，例如创建下列文件： 
    
    /etc/tmpfiles.d/btrfs-discard.conf
    
    w /sys/fs/btrfs/_uuid_ /discard/iops_limit - - - - 1000
    
或者在[fstab](<../zh-cn/Fstab.html> "Fstab")中使用`nodiscard`挂载选项禁用异步丢弃功能，使用[定期TRIM](<../zh-cn/%E5%9B%BA%E6%80%81%E7%A1%AC%E7%9B%98.html#Periodic_TRIM> "固态硬盘")来替代。 

### Device total_bytes should be at most X but found Y

若驱动器从其他计算机迁移或设备顺序变更，且报告的大小差异极小（至多几MB），可能是启用了 [HPA（主机保护区域）](<https://zh.wikipedia.org/wiki/%E4%B8%BB%E6%9C%BA%E4%BF%9D%E6%8A%A4%E5%8C%BA%E5%9F%9F> "zhwp:主机保护区域")。 

可使用 [hdparm](<https://archlinux.org/packages/?name=hdparm>)包 验证 HPA 是否启用： 
    
    # hdparm -N 设备
    
输出将显示两个数值：可见扇区数与实际扇区数。若两者不同则表明HPA已启用。 

若主板强制设置此功能且固件未提供关闭选项，唯一解决方案是收缩受影响文件系统。此操作最易在原始计算机或未应用HPA的机器上执行。 

###  设备空间不足

博客文章《[解决Btrfs文件系统空间不足问题](<https://marc.merlins.org/perso/btrfs/post_2014-05-04_Fixing-Btrfs-Filesystem-Full-Problems.html>)》建议并解释了以下检查步骤： 

  1. 立即清理空间（删除历史快照）
  2. 文件系统是否真满？元数据和/或数据块分布不均（运行 `btrfs balance`）
  3. 文件系统是否真满？数据块分布不均
  4. 文件系统是否真满？元数据分布不均
  5. 因空间不足无法执行平衡操作（运行 `btrfs balance` 前，先用 `btrfs device add` 临时添加设备如U盘或环回设备）

另可参阅 [btrfs 元数据满了怎么办 - 依云's Blog](<https://blog.lilydjwg.me/2023/7/25/btrfs-metadata-full.216670.html>)。 

有关 ENOSPC（“磁盘空间不足”）的最新处理指南，请参阅 [ENOSPC - No available disk space | Forza's Ramblings](<https://wiki.tnonline.net/w/Btrfs/ENOSPC>)。 

##  另请参阅

  * **官方网站**
    * [Btrfs 文档](<https://btrfs.readthedocs.io>)
    * [已归档的 Btrfs 百科](<https://archive.kernel.org/oldwiki/btrfs.wiki.kernel.org/>)
  * **性能相关**
    * [Btrfs on raw disks?](<https://superuser.com/questions/432188/should-i-put-my-multi-device-btrfs-filesystem-on-disk-partitions-or-raw-devices>)
    * [Varying leafsize and nodesize in Btrfs](<https://lore.kernel.org/linux-btrfs/CAKcLGm_MKEdTiHFBd-b-v2sN5gJmgFRqsykzWRXTVqUw4O6Acw@mail.gmail.com/>)
    * [Btrfs support for efficient SSD operation (data blocks alignment)](<https://lore.kernel.org/linux-btrfs/jgui4j$th5$1@dough.gmane.org/>)
    * [Is Btrfs optimized for SSDs?](<https://archive.kernel.org/oldwiki/btrfs.wiki.kernel.org/index.php/FAQ.html#Is_Btrfs_optimized_for_SSD.3F>)
    * [Lzo vs. zLib](<https://blog.erdemagaoglu.com/post/4605524309/lzo-vs-snappy-vs-lzf-vs-zlib-a-comparison-of>)
  * **杂项**
    * [Funtoo:BTRFS Fun](<https://www.funtoo.org/BTRFS_Fun>)
    * [Avi Miller presenting Btrfs](<https://www.phoronix.com/scan.php?page=news_item&px=MTA0ODU>) at SCALE 10x, January 2012.
    * [Summary of Chris Mason's talk](<https://www.phoronix.com/scan.php?page=news_item&px=MTA4Mzc>) from LFCS 2012
    * [Btrfs: stop providing a bmap operation to avoid swapfile corruptions](<https://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=35054394c4b3cecd52577c2662c84da1f3e73525>) 2009-01-21
    * [Doing Fast Incremental Backups With Btrfs Send and Receive](<https://marc.merlins.org/perso/btrfs/post_2014-03-22_Btrfs-Tips_-Doing-Fast-Incremental-Backups-With-Btrfs-Send-and-Receive.html>)

  1. [↑](<#cite_ref-1>) bees 的 issue 中有讨论过，具体链接以后再补。
