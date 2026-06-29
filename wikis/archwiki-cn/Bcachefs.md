**翻译状态：**

  * 本文（或部分内容）译自 [Bcachefs](<https://wiki.archlinux.org/title/Bcachefs> "arch:Bcachefs")，最近一次同步于 2026-01-18，若英文版本有所[更改](<https://wiki.archlinux.org/title/Bcachefs?diff=0&oldid=859306>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Bcachefs_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [文件系统](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html> "文件系统")

[Bcachefs](<https://bcachefs.org/>) 是一种写时复制（CoW）文件系统，支持多设备、RAID、压缩、校验和加密。它旨在提供类似于 [Btrfs](<../zh-cn/Btrfs.html> "Btrfs") 和 [ZFS](<../zh-cn/ZFS.html> "ZFS") 的现代功能。 

Bcachefs 基于 [Bcache](<../zh-cn/Bcache.html> "Bcache")，两者都主要由 Kent Overstreet 开发。 

**警告：** Bcachefs 是一个实验性文件系统。请务必备份所有你无法承受丢失后果的数据。

##  安装

**注意：** Bcachefs 树内内核模块已于 Linux 6.18 被移除。

安装 [bcachefs-tools](<https://archlinux.org/packages/?name=bcachefs-tools>)包 以及[bcachefs-dkms](<https://archlinux.org/packages/?name=bcachefs-dkms>)包，后者使用 [DKMS](<../zh-cn/DKMS.html> "DKMS") (动态内核模块支持)为已安装的 Linux 内核提供模块。 

若需（重新）生成基于 DKMS 提供内核模块的 initramfs，还需为已安装的内核安装对应的头文件软件包（如为 [linux](<https://archlinux.org/packages/?name=linux>)包安装[linux-headers](<https://archlinux.org/packages/?name=linux-headers>)包，为 [linux-lts](<https://archlinux.org/packages/?name=linux-lts>)包安装[linux-lts-headers](<https://archlinux.org/packages/?name=linux-lts-headers>)包，诸如此类）。 

##  初次设置

###  单盘
    
    # bcachefs format /dev/sd _X_
    # mount -t bcachefs /dev/sd _X_ /mnt
    
###  多盘

与 RAID0 类似，Bcachefs 默认会将数据条带化存储 (stripe)。数据冗余由 **replicas** 选项进行处理。 对 2 个存储设备使用 `--replicas=2` 相当于 RAID1，对 4 个存储设备使用 `--replicas=2` 相当于 RAID10，以此类推。 
    
    # bcachefs format /dev/sd _X_ /dev/sd _Y_ --replicas=_n_
    # mount -t bcachefs /dev/sd _X_ :/dev/sd _Y_ /mnt
    
Bcachefs 支持混合使用不同的储存设备。如果储存设备的大小不同，为了让每个储存设备以相同的速率填满数据，文件系统在某些储存设备上会使用更大的条带。如果储存设备的速度不同，对冗余数据的读取请求会被发往 IO 延迟最低的设备。如果有些储存设备比其他更可靠（例如硬件 RAID），可以通过 `--durability=2 _device_` 来把上面的每份数据副本算成两份。 

###  加密根文件系统

Bcachefs 使用 [自行实现](<https://bcachefs.org/Encryption/#Algorithms>) 的全文件系统加密，采用 ChaCha20-Poly1305。要格式化加密的文件系统： 
    
    # bcachefs format --encrypted /dev/sd _X_
    
如果用于根文件系统，请在 `/etc/mkinitcpio.conf` 的 [HOOKS](<../zh-cn/Mkinitcpio.html#HOOKS> "Mkinitcpio") 中添加 `bcachefs`，以便在启动或从休眠恢复时提示文件系统解锁。 

**注意：** 当前只有基于 BusyBox 的初始内存盘（initramfs）支持`bcachefs` hook。

###  SSD 缓存

Bcachefs 有四个储存目标（storage targets）: metadata、background、foreground 和 promote。对文件系统进行的写入优先使用 foreground，然后随着时间推移移动至 background。对文件系统的读取会缓存在 promote 上。metadata 目标通常与超低读取延迟的 NVMe 驱动器一起使用，例如 [Intel Optane](<https://www.phoronix.com/review/bcachefs-linux-2019>)。 

**注意：** 这只是对一个单一储存池而言的优先级。如果 foreground 满了，则系统会直接向 background 写入，或者如果两个都满了则会试着写入 promote。文件系统的元数据会优先写入 foreground，但也有可能会写入储存目标中的任意一个。在移除缓存设备时请小心，因为它们可能仍旧储存了数据。请参见 [#移除设备](<#%E7%A7%BB%E9%99%A4%E8%AE%BE%E5%A4%87>)

推荐的一种配置是使用一组 SSD 作为 foreground 和 promote，使用一组 HDD 作为 background（也就是回写缓存）。 
    
    # bcachefs format \
        --label=ssd.ssd1 /dev/sd _A_ \
        --label=ssd.ssd2 /dev/sd _B_ \
        --label=hdd.hdd1 /dev/sd _C_ \
        --label=hdd.hdd2 /dev/sd _D_ \
        --label=hdd.hdd3 /dev/sd _E_ \
        --label=hdd.hdd4 /dev/sd _F_ \
        --replicas=2 \
        --foreground_target=ssd \
        --promote_target=ssd \
        --background_target=hdd
    # mount -t bcachefs /dev/sd _A_ :/dev/sd _B_ :/dev/sd _C_ :/dev/sd _D_ :/dev/sd _E_ :/dev/sd _F_ /mnt
    
如果想配置直写缓存，和上面操作基本一致，不过要对每个 SSD 设备设置 `--durability=0 _device_`。 如果想配置绕写缓存，只需把 HDD 设为 foreground，把 SSD 设为 promote。 

###  挂载

默认的挂载方式是在 mount 指令中指定每个设备。 
    
    # mount -t bcachefs /dev/sd _A_ :/dev/sd _B_ :/dev/sd _C_ :/dev/sd _D_ :/
    
`mount.bcachefs` 支持通过 UUID 挂载文件系统，UUID 会在使用 `bcachefs format` 创建文件系统时显示。 
    
    # mount.bcachefs UUID=f66d108f-83d2-4679-b50b-7d5e710f6
    
若需在启动时挂载单个或多个设备，将 `bcachefs` 加入到 `/etc/mkinitcpio.conf` 的`HOOKS` 中，并[重新生成 initramfs](<../zh-cn/%E9%87%8D%E6%96%B0%E7%94%9F%E6%88%90_initramfs.html> "重新生成 initramfs")。 

##  配置

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 缺少应该使用什么选项的细节。 (在 [Talk:Bcachefs](<../zh-cn/Talk:Bcachefs.html>) 中讨论)

大多数选项可以通过以下方式设置： 

  * 在 `bcachefs format` 期间
  * 在格式化后使用 `bcachefs set-fs-option`
  * 在挂载时通过 `mount -o _option=value_`
  * 或通过 sysfs，例如 `echo _X_ > /sys/fs/bcachefs/_UUID_ /options/_option_`

挂载选项会覆盖其他方法设置的选项，后者会将选项保存到文件系统的超级块中。 

**注意：** 要使用 sysfs 必须先挂载文件系统。除了 fsck 以外，所有的操作都可以在文件系统挂载状态下进行。

一些可用选项举例如下： 

Bcachefs 选项  选项 | 描述   
---|---  
metadata_checksum | 指定用于元数据写入的校验和 (checksum)算法。默认情况下，算法为 crc32c。可以从`none`、`crc32c`、`crc64`、`xxhash`中选择其一。   
data_checksum | 指定用于数据写入的校验和 (checksum)算法，与`metadata_checksum`具有相同的默认值和选项。   
compression | 指定用于（前台）压缩的算法。默认情况下此选项为`none`。可以从`none`、`lz4`、`gzip`、`zstd`中选择其一。   
background_compression | 指定用于后台压缩的算法，与`compression`具有相同的默认值和选项。   
str_hash | 指定用于directory entries和 xattrs 的哈希函数。可以从`crc32c`、`crc64`和`siphash`中选择其一。   
nocow | 在可能的情况下，所有写入都将就地完成。快照 (snapshot) 和 reflink 仍会导致 COW 写入。该选项会隐式禁用数据校验、压缩和加密。   
encrypted | 启用文件系统[加密](<https://bcachefs.org/Encryption/>)（chacha20/poly1305）；将提示输入密码。   
  
更多选项可以在 [bcachefs 文档](<https://bcachefs-docs.readthedocs.io/en/latest/options.html>)中找到。 

以下内容可以通过 `bcachefs setattr _file_ --option=value` 按每个文件或目录进行设置。如果在一个目录中设置，它会进行递归传递。 

**注意：** 重新平衡线程目前为止不会在后台调整副本。也就是说，如果更改文件的副本选项，则必须手动运行 rereplicate 命令以确保旧文件遵循新规则。

  * 数据冗余数 (data_replicas)
  * 数据校验和 (data_checksum)
  * 前台压缩 (compression)、后台压缩 (background_compression)
  * 存储组配置：foreground_target、background_target、promote_target

要检查哪些选项处于活动状态，可以执行 `getfattr -d -m 'bcachefs_effective\.' _directory/file_`

**注意：** 目前储存设备用量显示的是未压缩时的大小。除此之外，压缩功能一切正常。

###  更改设备所属储存组

可以通过 sysfs 更改所属储存组： 
    
    # echo _group.drive_name_ > /sys/fs/bcachefs/_filesystem_uuid_ /dev-_X_ /label
    
**注意：** 需要重新挂载才能生效。

###  添加设备
    
    # bcachefs device add --label=_group.drive_name_ /mnt /dev/_device_
    
若这是某储存组中的第一个设备，则需要修改储存目标的设置才能使用。以下例子添加了一个缓存设备。 
    
    # echo _new_group_ > /sys/fs/bcachefs/_filesystem_uuid_ /options/promote_target
    # echo _new_group_ > /sys/fs/bcachefs/_filesystem_uuid_ /options/foreground_target
    # echo _old_group_ > /sys/fs/bcachefs/_filesystem_uuid_ /options/background_target
    
**注意：** 只有新的写入会被分散到新添加的设备中去。已经写入的内容不会改变，除非储存设备的占用达到一个阈值，从而触发重新平衡（rebalance/restripe）。目前无法手动触发重新平衡。

###  移除设备

首先请确保至少设备上有两份元数据（设备移除（evacuate）功能似乎对元数据不奏效）。如果数据和元数据都已经有冗余了，可以跳过这一步。 
    
    # echo 2 > /sys/fs/bcachefs/_UUID_ /options/metadata_replicas
    # bcachefs data rereplicate /mnt
    # bcachefs device set-state ro _device_
    # bcachefs device evacuate _device_
    
将状态设置为 ro，表示只读。 

若想移除设备： 
    
    # bcachefs device remove _device_
    # bcachefs data rereplicate /mnt
    
###  冗余

Bcachefs 中的元数据和数据的冗余级别可以独立配置，以控制数据冗余和持久性（durability）。 以下选项既定义了同步（即时）冗余，它会在写入时原子执行以确保数据完整；同时也定义了最终冗余目标（eventual replication target），其会在在后台异步完成以提高冗余和故障容忍度。 

  * `--replicas=X` 设置元数据和数据副本的**目标** 数量。
  * `--metadata_replicas=X` 设置在正常运行和重新平衡期间后台维护的元数据副本的**目标** 数量。
  * `--data_replicas=X` 设置**最终** 要维持的数据副本的**目标** 数量。
  * `--metadata_replicas_required=X` 设置在元数据被视为已提交之前，必须**同步** 写入的元数据副本的**最小** 数量。
  * `--data_replicas_required=X` 设置在数据被视为已提交之前，必须**同步** 写入的数据副本的**最小** 数量。

**注意：** 区分 `--[meta]data_replicas_required` 与 `--[meta]data_replicas` 非常重要，因为 `_replicas_required` 值设定了将被立即写入的副本数量的下限，而 `_replicas` 值设定了最终会写入的副本数量。可以将 `_replicas_required` 解释为 _如果我们只能完成这么多写入，文件系统依然能以降级模式（degraded）运行_ [[1]](<https://github.com/koverstreet/bcachefs-tools/issues/225#issuecomment-2050593447>)。

###  压缩

压缩通过 `--compression=` 选项设置，支持设置压缩级别。比如要设置 zstd 压缩并使用级别 5，可以使用 `--compression=zstd:5`。 

**注意：** 目前尚未实现多线程压缩。 [[2]](<https://github.com/koverstreet/bcachefs/issues/771>)

###  子卷

Bcachefs 支持使用与 [Btrfs](<../zh-cn/Btrfs.html#Subvolumes> "Btrfs") 类似的用户空间接口来管理子卷和快照。新子卷可以创建为空子卷，也可以是另一个子卷的快照。快照是可写的，并且可以多次快照，从而形成快照树。 

创建快照的成本非常低：它们不像 [Btrfs](<../zh-cn/Btrfs.html#Subvolumes> "Btrfs") 那样基于 COW btree 的克隆，而是基于 btree 中单个键的版本控制。你可以创建成千上万个快照，唯一的限制是磁盘空间。 

####  创建子卷

创建一个新的空子卷： 
    
    # bcachefs subvolume create _/path/to/subvolume_
    
####  删除子卷

删除已有的子卷或快照： 
    
    # bcachefs subvolume delete _/path/to/subvolume_
    
####  为现有子卷创建快照

为现有子卷创建快照： 
    
    # bcachefs subvolume snapshot _/path/to/source_ _/path/to/dest_
    
子卷在删除其中所有内容后也可以使用常规的 rmdir 删除，比如使用 `rm -rf`。 

递归快照创建和递归列出子卷等功能仍待实现。 

##  提示和技巧

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 关于自动挂载的内容可能会有些用处。 (在 [Talk:Bcachefs](<../zh-cn/Talk:Bcachefs.html>) 中讨论)

请查看 [Systemd/Journal](<../zh-cn/Systemd/Journal.html> "Systemd/Journal") 以获取更多有用的错误信息。 

###  标志顺序

一些 `bcachefs format` 标志是根据其参数顺序设置的，并且仅影响切换标志后出现的驱动器。例如，如果希望 SSD 具有 `--durability=0` 并启用 `--discard` 而 HDD 使用默认值，请确保按以下顺序传递参数： 
    
    # bcachefs format \
        --label=hdd.hdd1 /dev/sd _C_ \
        --label=hdd.hdd2 /dev/sd _D_ \
        --label=hdd.hdd3 /dev/sd _E_ \
        --label=hdd.hdd4 /dev/sd _F_ \
        --durability=0 --discard \
        --label=ssd.ssd1 /dev/sd _A_ \
        --label=ssd.ssd2 /dev/sd _B_ \
        --replicas=2 \
        --foreground_target=ssd \
        --promote_target=ssd \
        --background_target=hdd
    
###  格式化后设置冗余

可以使用 `set-fs-option` 在格式化后设置副本（冗余）数量。 
    
    # bcachefs set-fs-option --metadata_replicas=_2_ --data_replicas=_2_ /dev/sd _X_
    
之后需要让 bcachefs 确保所有文件都拥有副本，命令为： 
    
    # bcachefs data rereplicate /mnt
    
##  故障排除

###  32 位程序无法查看目录内容

部分 32 位程序可能无法获取 Bcachefs 目录中的内容，这是由于执行 [readdir(3)](<https://man.archlinux.org/man/readdir.3>) syscall 时文件系统返回的数据不兼容所导致。[[3]](<https://github.com/koverstreet/bcachefs/issues/650>)

要解决这个问题，可以暂时使用不同的文件系统供程序读写，比如 [tmpfs](<../zh-cn/Tmpfs.html> "Tmpfs")。 

###  swapfile 包含空洞或其他不支持的扩展

Bcachefs 目前不支持[交换文件](<https://github.com/koverstreet/bcachefs/issues/368>)。 

###  多设备 fstab

目前 systemd 存在一个 [bug](<https://github.com/systemd/systemd/issues/8234>)，导致无法在启动时通过在 [fstab](<../zh-cn/Fstab.html> "Fstab") 中使用以冒号分隔的设备来挂载多设备 bcachefs 文件系统。使用 `mount -a` 时可以正常挂载，但在开机启动时不会挂载。不过自从 [bcachefs-tools](<https://archlinux.org/packages/?name=bcachefs-tools>)包 版本 1.7.0 起，可以通过单个设备节点来挂载多设备阵列，从而允许使用正常的 [UUID](<../zh-cn/%E5%9D%97%E8%AE%BE%E5%A4%87%E6%8C%81%E4%B9%85%E5%8C%96%E5%91%BD%E5%90%8D.html#%E9%80%9A%E8%BF%87_uuid> "UUID") 指定方法。 
    
    # UUID=10176fc9-c4fa-4a30-9fd0-a756d861c4cd     /mnt   bcachefs defaults,nofail 0 0
    
可以通过以下任一命令找到文件系统 UUID / 外部 UUID： 
    
    # bcachefs fs usage /mnt
    # bcachefs show-super /dev/sdXY
    
###  挂载加密设备错误

对于使用 `--encrypted` 选项创建的设备，当 `bcachefs unlock /dev/sd _XY_` 后挂载失败时，出现 
    
    ERROR - bcachefs::commands::cmd_mount: Fatal error: Required key not available
    
可以通过手动将密钥链接到会话来解决这个问题[[4]](<https://lore.kernel.org/all/6018852.lOV4Wx5bFT@lichtvoll.de/>)： 
    
    # keyctl link @u @s
    # mount /dev/sd _XY_ /mnt
    Enter passphrase:
    
不需要输入 _mount_ 要求的密码（按`回车键`即可）。 

##  另请参阅

  * [官方手册](<https://bcachefs.org/bcachefs-principles-of-operation.pdf>)
  * [Kent Overstreet 的 Patreon 页面](<https://www.patreon.com/bcachefs>)
  * [Wikipedia:Bcachefs](<https://en.wikipedia.org/wiki/Bcachefs> "wikipedia:Bcachefs")
  * [bcachefs on ReadTheDocs](<https://bcachefs-docs.readthedocs.io/en/latest/introduction.html>)
