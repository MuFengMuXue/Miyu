相关文章

  * [文件系统](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html> "文件系统")
  * [ZFS/虚拟磁盘](<../zh-cn/ZFS/%E8%99%9A%E6%8B%9F%E7%A3%81%E7%9B%98.html> "ZFS/虚拟磁盘")
  * [在 ZFS 上安装 Arch Linux](<../zh-cn/%E5%9C%A8_ZFS_%E4%B8%8A%E5%AE%89%E8%A3%85_Arch_Linux.html> "在 ZFS 上安装 Arch Linux")

**翻译状态：**

  * 本文（或部分内容）译自 [ZFS](<https://wiki.archlinux.org/title/ZFS> "arch:ZFS")，最近一次同步于 2025-01-04，若英文版本有所[更改](<https://wiki.archlinux.org/title/ZFS?diff=0&oldid=824230>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/ZFS_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[ZFS](<https://zh.wikipedia.org/wiki/ZFS> "zhwp:ZFS") 最早是由[太阳计算机公司](<https://zh.wikipedia.org/wiki/%E5%A4%AA%E9%98%B3%E8%AE%A1%E7%AE%97%E6%9C%BA%E5%85%AC%E5%8F%B8> "zhwp:太阳计算机公司")为 solaris 操作系统开发并发布的一个先进文件系统，现在的 ZFS 一词通常指 [OpenZFS](<https://github.com/openzfs/zfs>) 分支，该分支将原先的实现移植到了包括 Linux 等其它操作系统上，同时继续开发 solaris ZFS。本文将把 ZFS 和 OpenZFS 视为同义词。 

ZFS 具有丰富的特性，其中包括：更好的页缓存算法：[ARC](<https://en.wikipedia.org/wiki/Adaptive_replacement_cache> "wikipedia:Adaptive replacement cache")、去重、池化存储、[快照](<https://en.wikipedia.org/wiki/Snapshot_\(computer_storage\)> "wikipedia:Snapshot \(computer storage\)")、复制、数据完整性检查及自动修复（scrubbing）、[RAID-Z](<https://en.wikipedia.org/wiki/RAID-Z> "wikipedia:RAID-Z") 等等。 

##  概念

与将数据存放在单个块设备上的常见文件系统不同，ZFS 将数据存放在存储池中。存储池由 vdev（虚拟设备）组成，而 vdev 又由块设备构成。存储池始终将数据写入到剩余空间占比最大的 vdev 中，使数据条带化分布在各个 vdev 内。另一方面，vdev 可以使用如 RAIDZ 和镜像更复杂的配置。在最简单的配置中，可以在由单个分区组成的单个 vdev 上创建一个池，其行为与常规文件系统类似。 

创建后，就可以从池中分配存储资源。这些资源被分组为称为数据集的单元。数据集有 4 种类型： 

  1. 文件系统：文件系统基本上就是一个目录树，可以像常规文件系统一样被挂载到系统名字空间中
  2. 卷（zvol）：表现为块设备的卷
  3. 快照：文件系统或卷的快照
  4. 书签：不存储任何数据的快照，用于增量复制

数据集被标识为一条唯一路径，格式如下： 
    
    pool(/segment)+((#|@)bookmark/snapshot name)?
    
其中 `#` 被用于书签，`@` 被用于快照。 

**注意：** 上述内容是 [zpoolconcepts(7)](<https://openzfs.github.io/openzfs-docs/man/master/7/zpoolconcepts.7.html>) 和 [zfsconcepts(7)](<https://openzfs.github.io/openzfs-docs/man/master/7/zfsconcepts.7.html>) 的简短摘要。强烈建议阅读这两篇文档，以熟悉其中的概念以及此处未涉及的技术术语。

##  位于内核树外导致的问题

由于复杂的法律问题，Linux 内核维护者拒绝将 ZFS 并入到 Linux 内核中，因此 ZFS 被作为树外内核模块进行开发。由此导致的一个问题是：内核升级经常会导致 ZFS 使用的内核 API 被修改。在这种情况下，ZFS 将被迫修改代码以使用新的 API，也就意味着在一段时间内 ZFS 将不兼容最新的主线内核版本。 

**提示：** 由于 [linux](<https://archlinux.org/packages/?name=linux>)包 会密切跟踪最新稳定内核版本，如果你不想将 [linux](<https://archlinux.org/packages/?name=linux>)包 包固定在特定版本，最好是使用 [linux-lts](<https://archlinux.org/packages/?name=linux-lts>)包。

##  安装

作为树外模块，有两种类型的包可供选择安装：一种是为特定内核版本构建的二进制内核模块，另一种是将其源码安装为 [DKMS](<../zh-cn/DKMS.html> "DKMS") 模块，并在内核更新时自动重新构建。 

除了内核模块外，用户还需要安装如 [zpool(8)](<https://openzfs.github.io/openzfs-docs/man/master/8/zpool.8.html>) 和 [zfs(8)](<https://openzfs.github.io/openzfs-docs/man/master/8/zfs.8.html>) 的用户空间工具。这些工具通常被打包为单个软件包，名称为 `zfs-utils*`。 

下面提到的所有内核模块都已在依赖中指定所需的 `zfs-utils*` 包，因此在安装时你只需满足其依赖即可。 

###  二进制内核模块

各软件包的比较  包名  | 软件源  | ZFS 发布类型  | 目标 kernel  | 二进制包  | 附注   
---|---|---|---|---|---  
[zfs-linux-lts](<https://aur.archlinux.org/packages/zfs-linux-lts/>)AUR | AUR  | 稳定版  |  [linux-lts](<https://archlinux.org/packages/?name=linux-lts>)包 | 否  | 强烈建议在构建新版 ZFS 包时使用 [devtools](<https://wiki.archlinux.org/title/DeveloperWiki:Building_in_a_clean_chroot#Convenience_way>)，从而无需在升级内核时卸载当前安装的 ZFS 包。   
[zfs-linux](<https://aur.archlinux.org/packages/zfs-linux/>)AUR | AUR  | 稳定版  |  [linux](<https://archlinux.org/packages/?name=linux>)包 | 否   
zfs-linux  |  [archzfs](<../zh-cn/%E9%9D%9E%E5%AE%98%E6%96%B9%E7%94%A8%E6%88%B7%E4%BB%93%E5%BA%93.html#archzfs> "非官方用户仓库") | 稳定版  | linux  | 是  |   
zfs-linux-lts  | archzfs  | 稳定版  | linux-lts  | 是  |   
  
### DKMS

  * [zfs-dkms](<https://aur.archlinux.org/packages/zfs-dkms/>)AUR：稳定版本
  * [zfs-dkms-staging-git](<https://aur.archlinux.org/packages/zfs-dkms-staging-git/>)AUR：稳定版本，包含为最新 [linux](<https://archlinux.org/packages/?name=linux>)包 内核版本提供支持的补丁

###  使用 ZFS 作为根分区

参见[在 ZFS 上安装 Arch Linux](<../zh-cn/%E5%9C%A8_ZFS_%E4%B8%8A%E5%AE%89%E8%A3%85_Arch_Linux.html> "在 ZFS 上安装 Arch Linux")。 

##  配置

###  启动时导入存储池

ZFS 提供了用于自动导入存储池的 systemd 服务，和为其它单元提供 ZFS 初始化状态的目标，其中包括： 

  * `zfs.target`：全部 ZFS 服务完成后激活
  * `zfs-import.target`：完成 ZFS 存储池导入后激活
  * `zfs-volumes.target`：所有 zvol 都出现在 `/dev` 下后激活
  * `zfs-import-scan.service`：使用 libblkid 扫描设备并导入存储池
  * `zfs-import-cache.service`：检查 `zpool.cache` 并导入存储池
  * `zfs-volume-wait.service`：等待所有 zvol 都可用

你需要在 `zfs-import-scan.service` 和 `zfs-import-cache.service` 间二选一，并启用其它全部服务和目标。 

#### zfs-import-scan

`zfs-import-scan.service` 使用了 `zpool import` 的默认逻辑：使用 blkid 扫描设备，意味着其不需要使用 `zpool.cache` 文件。鉴于 `zpool.cache` 已被[废弃](<https://github.com/openzfs/zfs/issues/1035#issuecomment-13411970>)，建议使用该方法。 

如果 `zpool.cache` 存在且不为空，那么 `zfs-import-scan.service` 就不会启动，因此需要确保你的所有存储池导入时都没有启用 `cachefile` 选项，该操作可通过启用 `zfs` 模块的 [`zfs_autoimport_diable`](<https://openzfs.github.io/openzfs-docs/Performance%20and%20Tuning/Module%20Parameters.html#zfs-autoimport-disable>) 选项实现。你还需要删除现有的 `zpool.cache`，或在启动时将所有导入的存储池的 `cachefile` 选项设为 `none`。 

#### zfs-import-cache

`zfs-import-cache.service` 在导入存储池时使用 `zpool import -c <zpool.cache>`，该操作会从 `zpool.cache` 读取设备路径。 

由于重启或出现硬件更改后设备路径可能会变化，因此在使用该方法时需注意创建 ZFS 存储池时使用的设备路径，否则会导致缓存过时并导入失败。关于如何选择持久化设备路径的信息请参考[块设备持久化命名](<../zh-cn/%E5%9D%97%E8%AE%BE%E5%A4%87%E6%8C%81%E4%B9%85%E5%8C%96%E5%91%BD%E5%90%8D.html> "块设备持久化命名")。 

###  自动挂载文件系统

`zfs-import-scan.service` 和 `zfs-import-cache.service` 服务会导入存储池，但不会挂载任何文件系统。根据你的系统是否配置了 `mountpoint=legacy`，有两种方法可以在启动时导入文件系统。如果你的文件系统混用了 legacy 与非 legacy 配置，那就需要同时使用两种方式。 

#### zfs-mount-generator

如果你的文件系统使用非 legacy 挂载，那么建议使用 [zfs-mount-generator](<https://openzfs.github.io/openzfs-docs/man/master/8/zfs-mount-generator.8.html>)，这是一个 [systemd.generator(7)](<https://man.archlinux.org/man/systemd.generator.7>)，可以为导入的 ZFS 存储池中的所有文件系统生成带有 `canmount=on` 选项的 systemd 挂载单元文件，以便在启动时挂载文件系统。由于其需要使用 `zfs list` 缓存，默认情况下运行 zfs-mount-generator 不会产生任何效果，你需要进行以下操作： 

  1. 启用并启动 `zfs-zed.service`
  2. 创建 `/etc/zfs/zfs-list.cache` 目录
  3. 在 `/etc/zfs/zfs-list.cache` 中创建以你的存储池为名的空文件，ZFS Event Daemon（ZED）只会在存储池对应文件存在并可写入时更新文件系统清单：
         
         # touch /etc/zfs/zfs-list.cache/<pool-name>

  4. 检查 `/etc/zfs/zfs-list.cache/<pool-name>` 的内容。如果其内容为空，需要执行以下命令修改任意 ZFS 文件系统的 canmount 属性，以生成 ZFS 事件来触发 ZED：
         
         zfs set canmount=off zroot/fs1

，然后执行 
         
         zfs inherit canmount zroot/fs1

#### fstab

如果你的文件系统使用 legacy 挂载，那就需要在 [fstab](<../zh-cn/Fstab.html> "Fstab") 文件中指定挂载点。设备一项需填入文件系统的完整路径名称，dump 及 fsck 项需填为 0。 

###  创建 hostid 文件

通常没有需要，但还是建议创建 `/etc/hostid` 文件： 
    
    # zgenhostid $(hostid)
    
##  存储池

###  尝试使用 ZFS

如果有用户希望在不会造成数据丢失的情况下试用 ZFS，可参考 [ZFS/Virtual disks](<../zh-cn/ZFS/Virtual_disks.html> "ZFS/Virtual disks")。 

###  创建 ZFS 池

**提示：** 你可能需要先阅读 [#ashift 属性](<#ashift_%E5%B1%9E%E6%80%A7>)，因为建议在创建池时设置 `ashift`。

要创建 ZFS 池，请使用如下命令： 
    
    # zpool create -R <root> -o <poolopts> -O <dsetprops> <pool> <vdevs>
    
其中 `vdev` 是单个设备或使用以下格式： 
    
    <vdev type> <device> ... <device>
    
  * **-R** ：在该文件夹下挂载所有文件系统，用于不影响当前系统
  * **-o** ：指定存储池属性，可多次使用。类似 `ashift` 等属性在创建后就无法修改（理论上 `ashift` 是各 vdev 独立的，但要为 vdev 单独配置该参数就需要执行 `zpool add`）。
  * **-O** ：指定存储池根数据集的属性，可多次使用。类似 `normalization` 等属性在创建后就无法更改。
  * **pool** ：存储池的名称
  * **vdev type** ：受支持的 vdev 清单请参考 [zpoolconcepts(7)](<https://openzfs.github.io/openzfs-docs/man/master/7/zpoolconcepts.7.html>)。
  * **device** ：块设备，可以是完整路径或路径的文件名部分

**注意：** 取决于挂载存储池使用的具体[方法](<#%E5%90%AF%E5%8A%A8%E6%97%B6%E5%AF%BC%E5%85%A5%E5%AD%98%E5%82%A8%E6%B1%A0>)，你可能要注意创建存储池时使用的设备路径。

以在单个分区上创建存储池为例： 
    
    # zpool create -R /mnt pool /dev/sda
    
使用单个 `raidz1` vdev 创建池： 
    
    # zpool create -R /mnt pool \
                   raidz1 \
                      ata-ST3000DM001-9YN166_S1F0KDGY \
                      ata-ST3000DM001-9YN166_S1F0JKRR \
                      ata-ST3000DM001-9YN166_S1F0KBP8 \
                      ata-ST3000DM001-9YN166_S1F0JTM1
    
使用两个镜像（`mirror`）vdev 创建池： 
    
    # zpool create -R /mnt pool \
                   mirror \
                      ata-ST3000DM001-9YN166_S1F0KDGY \
                      ata-ST3000DM001-9YN166_S1F0JKRR \
                   mirror \
                      ata-ST3000DM001-9YN166_S1F0KBP8 \
                      ata-ST3000DM001-9YN166_S1F0JTM1
    
####  ashift 属性

`ashift` 是一个不可修改的 vdev 独立属性，决定了（逻辑）扇区大小为 2^ashift 字节。为提升性能，逻辑扇区大小需要大于或等于硬盘的物理扇区大小。 

默认情况下，`zpool create` 可以自动识别设备的物理扇区大小，适用于单硬盘配置场景。 

但如果你需要（或打算）配置如 `mirror` 或 `raidzX` 的可替换故障硬盘的 vdev 环境，建议始终设定 `ashift=12`。这是因为在 512 字节硬盘上使用 4kb 逻辑扇区大小没有问题，但反过来操作就会导致性能下降（除非你的硬盘是比较少见的 8kb 扇区大小 [SSD](<https://github.com/openzfs/zfs/blob/master/cmd/zpool/os/linux/zpool_vdev_os.c#L99>)）。 

**提示：** 可以使用 
    
    $ lsblk --filter 'TYPE=="DISK"' -o NAME,PHY-SEC
    
来检查硬盘的物理扇区大小。 

另外，如果你在使用 NVMe 硬盘，有概率可以将其格式化为更高性能的 LBA 格式（具体参考 [nvme-format(1)](<https://man.archlinux.org/man/nvme-format.1>)）。 

####  创建兼容 GRUB 的存储池

默认情况下， _zpool create_ 会为存储池启用所有特性。如果使用 [GRUB](<../zh-cn/GRUB.html> "GRUB") 时将 `/boot` 放置到了 ZFS 下，就需要将 GRUB 不支持的特性全部禁用，否则 GRUB 将无法读取池中的数据。ZFS 内置了兼容性文件（参见 `/usr/share/zfs/compatibility.d`），可以帮助创建仅包含部分特性集的存储池，其中就包括了 grub2。 

可以通过如下命令创建包含部分特性集的存储池： 
    
    # zpool create -o compatibility=grub2 $POOL_NAME $VDEVS
    
###  验证存储池状态

如果命令成功执行，则不会有任何输出。使用 [mount](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html#%E6%8C%82%E8%BD%BD%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "Mount") 命令会显示存储池已被挂载。使用 `zpool status` 会显示存储池已被创建： 
    
    # zpool status
    
      pool: bigdata
     state: ONLINE
     scan: none requested
    config:
    
            NAME                                       STATE     READ WRITE CKSUM
            bigdata                                    ONLINE       0     0     0
              -0                                       ONLINE       0     0     0
                ata-ST3000DM001-9YN166_S1F0KDGY-part1  ONLINE       0     0     0
                ata-ST3000DM001-9YN166_S1F0JKRR-part1  ONLINE       0     0     0
                ata-ST3000DM001-9YN166_S1F0KBP8-part1  ONLINE       0     0     0
                ata-ST3000DM001-9YN166_S1F0JTM1-part1  ONLINE       0     0     0
    
    errors: No known data errors
    
###  删除存储池

要删除整个存储池： 
    
    # zpool destroy <pool>
    
接下来检查下存储池状态： 
    
    # zpool status
    
    no pools available
    
###  导出存储池

通过以下命令导出存储池： 
    
    # zpool export <pool>
    
###  扩展现有存储池

可以通过如下命令将一个设备（单个分区或硬盘）添加到现有 zpool： 
    
    # zpool add <pool> <device-id>
    
###  添加设备为镜像

可以将设备（分区或硬盘）作为镜像附加到现有设备上（与 RAID1 类似）： 
    
    # zpool attach <pool> <device-id|mirror> <new-device-id>
    
你可以将新设备添加到现有镜像 vdev 中（例如从 2 盘镜像变为 3 盘镜像）或[将其附加到单个设备上以构成新的镜像 vdev](<https://askubuntu.com/a/1303462>)。 

###  重命名存储池

可以用以下两步重命名已创建的存储池： 
    
    # zpool export oldname
    # zpool import oldname newname
    
###  更换挂载点

可以通过如下命令修改 zpool 的挂载点： 
    
    # zfs set mountpoint=/foo/bar poolname
    
###  升级存储池

将 ZFS 升级到新版本后，有可能会获得一些新功能。出于兼容性考虑，ZFS 不会自动为之前创建的存储池启用新功能，而需要单独为每个存储池手动启用。 

要检查是否可以升级： 
    
    $ zpool upgrade
    
    This system supports ZFS pool feature flags.
    
    All pools are formatted using feature flags.
    
    Every feature flags pool has all supported and requested features enabled.

如果有可以升级的存储池，会出现如下输出： 
    
    This system supports ZFS pool feature flags.
    
    All pools are formatted using feature flags.
    
    Some supported features are not enabled on the following pools. Once a
    feature is enabled the pool may become incompatible with software
    that does not support the feature. See zpool-features(7) for details.
    
    Note that the pool 'compatibility' feature can be used to inhibit
    feature upgrades.
    
    POOL  FEATURE
    
    * * *
    
    rpool
          redaction_list_spill
          raidz_expansion
          fast_dedup
          longname
          large_microzap
    
升级单个存储池： 
    
    # zpool upgrade <pool>
    
使用如下命令来升级所有存储池： 
    
    # zpool upgrade -a
    
##  创建数据集

相对于在存储池中创建文件夹，用户可以选择在存储池中创建数据集。除了快照外，数据集还提供了如配额控制等更强大的控制功能。在创建并挂载数据集前，需确保存储池中不存在与数据集同名的文件夹。以下命令可用于创建数据集： 
    
    # zfs create <存储池名>/<数据集名>
    
可以对数据集应用 ZFS 特定属性。例如，你可以对数据集中的文件夹设定配额限制： 
    
    # zfs set quota=20G <存储池名>/<数据集名>/<文件夹>
    
如需了解更多 ZFS 命令，可查阅 zfs(8) 或 zpool(8)。 

###  原生加密

ZFS 支持如下几种加密方式：`aes-128-ccm`, `aes-192-ccm`, `aes-256-ccm`, `aes-128-gcm`, `aes-192-gcm` 及 `aes-256-gcm`。当加密设置为 `on` 时，将使用 `aes-256-gcm` 进行加密。See [zfs-change-key(8)](<https://openzfs.github.io/openzfs-docs/man/8/zfs-change-key.8.html#Encryption>) for a description of the native encryption, including limitations. 

支持下列几种密钥格式：`passphrase`, `raw`, `hex`。 

One can also specify/increase the default iterations of PBKDF2 when using `passphrase` with `-o pbkdf2iters <n>`, although it may increase the decryption time. 

**注意：**

  * To import a pool with keys, one needs to specify the `-l` flag, without this flag encrypted datasets will be left unavailable until the keys are loaded. See [#Importing a pool created by id](<#Importing_a_pool_created_by_id>).
  * Native ZFS encryption has been made available in the stable 0.8.0 release or newer. Previously it was only available in development versions provided by packages like [zfs-linux-git](<https://aur.archlinux.org/packages/zfs-linux-git/>)AUR, [zfs-dkms-git](<https://aur.archlinux.org/packages/zfs-dkms-git/>)AUR or other development builds. Users who were only using the development versions for the native encryption, may now switch to the stable releases if they wish.
  * The default encryption suite was changed from `aes-256-ccm` to `aes-256-gcm` in the 0.8.4 release.

使用如下命令创建通过密码短语加密的数据集： 
    
    # zfs create -o encryption=on -o keyformat=passphrase <存储池名>/<数据集名>
    
使用密钥而不是密码短语进行加密： 
    
    # dd if=/dev/random of=/path/to/key bs=32 count=1 iflag=fullblock
    # zfs create -o encryption=on -o keyformat=raw -o keylocation=file:///path/to/key <存储池名>/<数据集名>
    
The easy way to make a key in human-readable form (`keyformat=hex`): 
    
    # od -Anone -x -N 32 -w64 /dev/random | tr -d [:blank:] > /path/to/hex.key
    
验证密钥位置： 
    
    # zfs get keylocation <存储池名>/<数据集名>
    
更改密钥位置： 
    
    # zfs set keylocation=file:///path/to/key <存储池名>/<数据集名>
    
你也可以下列任意一条命令手动加载密钥： 
    
    # zfs load-key <存储池名>/<数据集名> # load key for a specific dataset
    # zfs load-key -a # load all keys
    # zfs load-key -r zpool/dataset # load all keys in a dataset
    
挂载加密数据集： 
    
    # zfs mount <存储池名>/<数据集名>
    
####  启动时解锁/挂载：systemd

可以使用 [systemd](<../zh-cn/Systemd.html> "Systemd") 单元在启动时自动解锁数据集。例如，可以创建如下服务来解锁特定的数据集： 
    
    /etc/systemd/system/zfs-load-key@.service
    
    [Unit]
    Description=Load %I encryption keys
    Before=systemd-user-sessions.service zfs-mount.service
    After=zfs-import.target
    Requires=zfs-import.target
    DefaultDependencies=no
    
    [Service]
    Type=oneshot
    RemainAfterExit=yes
    ExecStart=/usr/bin/bash -c 'until (systemd-ask-password "Encrypted ZFS password for %I" --no-tty | zfs load-key %I); do echo "Try again!"; done'
    
    [Install]
    WantedBy=zfs-mount.service
    
接下来为每个加密数据集[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用")该服务 (例如 `zfs-load-key@pool0-dataset0.service`)。注意，`-` 在 systemd 单元中的定义为 `/`，详细资料可参考 `systemd-escape(1)`。 

**注意：** The `Before=systemd-user-sessions.service` ensures that systemd-ask-password is invoked before the local IO devices are handed over to the [desktop environment](<../zh-cn/Desktop_environment.html> "Desktop environment").

另一种方法是加载所有可能用到的密钥： 
    
    /etc/systemd/system/zfs-load-key.service
    
    [Unit]
    Description=Load encryption keys
    DefaultDependencies=no
    After=zfs-import.target
    Before=zfs-mount.service
    
    [Service]
    Type=oneshot
    RemainAfterExit=yes
    ExecStart=/usr/bin/zfs load-key -a
    StandardInput=tty-force
    
    [Install]
    WantedBy=zfs-mount.service

接下来[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `zfs-load-key.service`。 

####  登录时解锁：PAM

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** Missing prompts in front of commands.（在[Talk:ZFS](<../zh-cn/Talk:ZFS.html>)讨论）

If you are not encrypting the root volume, but only the home volume or a user-specific volume, another idea is to [wait until login to decrypt it](<https://blog.trifork.com/2020/05/22/linux-homedir-encryption/>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2024-11-06 ⓘ]. The advantages of this method are that the system boots uninterrupted, and that when the user logs in, the same password can be used both to authenticate and to decrypt the home volume, so that the password is only entered once. 

First set the mountpoint to legacy to avoid having it mounted by `zfs mount -a`: 
    
    zfs set mountpoint=legacy zroot/data/home

Ensure that it is in /etc/fstab so that `mount /home` will work: 
    
    /etc/fstab
    
    zroot/data/home         /home           zfs             rw,xattr,posixacl,noauto        0 0

Alternatively, you can keep using ZFS mounts if you use both: 
    
    zfs set canmount=noauto zroot/data/home
    zfs set org.openzfs.systemd:ignore=on zroot/data/home

The first will stop ZFS automatically mounting it, and the second systemd, but you will still be able to manually (or through the following scripts) mount it. If you have child datasets, `org.openzfs.systemd:ignore=on` will be inherited, but you will need to set `canmount=noauto` on each as it is not inheritable, otherwise they will try to mount without a mountpoint. 

On a single-user system, with only one `/home` volume having the same encryption password as the user's password, it can be decrypted at login as follows: first create `/usr/local/bin/mount-zfs-homedir`
    
    /usr/local/bin/mount-zfs-homedir
    
    #!/bin/bash
    set -eu
    
    # $PAM_USER will be the username of the user, you can use it for per-user home volumes.
    HOME_VOLUME="zroot/data/home" 
    
    if [ "$(zfs get keystatus "${HOME_VOLUME}" -Ho value)" != "available" ]; then
      PASSWORD=$(cat -)
      zfs load-key "${HOME_VOLUME}" <<< "$PASSWORD" || continue
    fi
    
    # This will also mount any child datasets, unless they use a different key.
    echo "$(zfs list -rHo name,keystatus,mounted "${HOME_VOLUME}")" | while IFS=$'\t' read -r NAME KEYSTATUS MOUNTED; do
      if [ "${MOUNTED}" != "yes" ] && [ "${KEYSTATUS}" == "available" ]; then
        zfs mount "${NAME}" || true
      fi
    done

do not forget to make it [executable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "Executable"); then get PAM to run it by adding the following line to /etc/pam.d/system-auth: 
    
    /etc/pam.d/system-auth
    
    auth       optional                    pam_exec.so          expose_authtok /usr/local/bin/mount-zfs-homedir
    
Now it will transparently decrypt and mount the /home volume when you log in anywhere: on the console, via ssh, etc. 

##### SSH

A caveat is that since your `~/.ssh` directory is not mounted, if you log in via ssh, you must use password authentication the first time rather than relying on `~/.ssh/authorized_keys`. 

If you do not wish to enable (insecure) password authentication, you can instead move `~/.ssh/authorized_keys` to a new location. Make `/etc/ssh/user_config/` and inside it a folder for each user, owned by that user and with `700` permissions. Then move each user's `authorized_keys` into their respective folders, and edit the system sshd configuration: 
    
    /etc/ssh/sshd_config
    
    AuthorizedKeysFile /etc/ssh/user_config/%u/authorized_keys

Then [restart](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `sshd.service`. You can also optionally make a link for each user from `~/.ssh/authorized_keys` to the new location so users can still edit it as they are used to. 

This will let you log in, but your home partition will not be mounted, and you will need to do so manually. There are multiple options to work around this: 

######  SSH Key & Password when required

It is possible to set up PAM to only prompt for a password via SSH when it is necessary to decrypt your home partition. You will need to enable both `publickey` and `keyboard-interactive` authentication methods: 
    
    /etc/ssh/sshd_config
    
    PubkeyAuthentication yes
    KbdInteractiveAuthentication yes
    AuthenticationMethods publickey,keyboard-interactive
    
    ## Example of excluding a certain user who does not have an encrypted home directory.
    #Match User nohome
    #  KbdInteractiveAuthentication no
    #  AuthenticationMethods publickey

**警告：** Note the comma in `AuthenticationMethods publickey,keyboard-interactive`, this means that you need to do _both_ authentication methods to log in with SSH. The very similar `AuthenticationMethods publickey keyboard-interactive` means you can do **either** to log in, which would let someone bypass your public key auth.

**注意：** You may ask why `keyboard-interactive` and not `password`? `password` is done client-side, so even if the auth is skipped, the user is still prompted and the password is just thrown away. With `keyboard-interactive` the user does not get prompted at all when we skip it.

This will mean it asks for the password after validating the key, but using PAM we can stop it asking for the password when not needed. We make a script that will fail when the key is not available to us: 
    
    /usr/local/bin/require-encrypted-homedir
    
    #!/bin/bash
    set -eu
    
    HOME_VOLUME="zroot/data/home" # You can use $PAM_USER to use the username in the volume for a per-user solution.
    
    if [ "$(zfs get keystatus "${HOME_VOLUME}" -Ho value)" != "available" ]; then
      exit 27 # PAM_TRY_AGAIN
    elif [[ "${SSH_AUTH_INFO_0:-""}" =~ ^"publickey " ]]; then
      exit 0
    else
      # If this happens, it implies a configuration error: either you are allowing auth without a public 
      # key, or have enabled this in a non-SSH PAM service. Both are dangerous and this should block it, 
      # but if you see it, fix your configuration.
      exit 3 # PAM_SERVICE_ERR
    fi

And make it [executable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "Executable"). 

Now we want to configure PAM to call this, and skip asking for the password if the script succeeds because we already have the key available. Add this line above the existing auth line(s) you want to skip (all of them unless you have something else set up) for the SSH service: 
    
    /etc/pam.d/sshd
    
    auth sufficient pam_exec.so /usr/local/bin/require-encrypted-homedir

**警告：** This is for `/etc/pam.d/sshd` **not** `/etc/pam.d/system-auth` as above. You do not want local users without a public key to be able to skip the password. There a safeguard in the script against this, but still best to be careful.

**注意：** When using private keys, the auth step is skipped in PAM as the private key authentication is handled entirely by `sshd`. This means that the script we are adding here will never be run for private keys and they cannot be skipped, however, we still do a check for defence-in-depth to try and ensure a key has been checked.

With this, you will be prompted for a password only when the key is not loaded. 

######  SSH Key & Password

A simpler option is to just enable both methods, meaning your key still gets checked, but then you have to type the password too, which will decrypt your home partition. 
    
    /etc/ssh/sshd_config
    
    PubkeyAuthentication yes
    PasswordAuthentication yes
    AuthenticationMethods publickey,password

**警告：** Note the comma in `AuthenticationMethods publickey,password`, this means that you need to do _both_ authentication methods to log in with SSH. The very similar `AuthenticationMethods publickey password` means you can do **either** to log in, which would let someone bypass your public key auth.

This works (and will not let anyone authenticate with _just_ a password), but has the downside of requiring your password every time. 

You can also specify something like: 
    
    AuthenticationMethods publickey password,publickey

This allows clients to either use either just a public key, or one and a password. Which the client will do will be based on the `PreferredAuthentications` option. `-o PreferredAuthentications=password,publickey` will ask for the password, while `-o PreferredAuthentications=publickey` will not. This is more manual than automated fallback, but has less moving parts, and avoids asking you every time if you prefer `publickey` by default (you can use [host-specific options](<../zh-cn/OpenSSH.html#Configuration> "OpenSSH") on clients to simplify setting these options). 

###  交换卷

**警告：**

  * 如果您的系统内存压力较大，则不管剩余多少交换空间可用，将 zvol 用作交换卷都可能会导致文件系统锁起。这个问题现在正在 [OpenZFS issue #7734](<https://github.com/openzfs/zfs/issues/7734>) 中调查。
  * zvol 上的交换空间不支持从休眠中唤醒，如果尝试从休眠中恢复将会导致存储池损坏。可能的解决方案见：<https://github.com/openzfs/zfs/issues/260#issuecomment-758782144>

ZFS 不允许使用交换文件，但您可以将一个 ZFS 卷 (ZVOL) 用作交换空间。需要注意的是必须将 ZVOL 的块大小设置为系统的 PAGESIZE，后者可以通过运行 `getconf PAGESIZE` 命令来获得（对于 x86_64 系统来说，其默认值为 4KiB）。关闭 ZVOL 上的写入缓存也可以让系统在低内存状态下更好运行。 

创建一个 8 GiB 的 ZFS 卷： 
    
    # zfs create -V 8G -b $(getconf PAGESIZE) -o compression=zle \
                  -o logbias=throughput -o sync=always\
                  -o primarycache=metadata -o secondarycache=none \
                  -o com.sun:auto-snapshot=false <pool>/swap
    
将其格式化为交换空间： 
    
    # mkswap -f /dev/zvol/<pool>/swap
    # swapon /dev/zvol/<pool>/swap
    
要将其永久自动挂载，编辑 `/etc/fstab`。ZVOLs 支持垃圾回收，这对 ZFS 的块分配器有潜在帮助，同时当交换空间仍有剩余时有助于减少其他数据集上的磁盘碎片。 

在 `/etc/fstab` 中添加如下行： 
    
    /dev/zvol/<pool>/swap none swap discard 0 0
    
###  访问控制列表（Access Control Lists，ACL）

要对数据集使用 [ACL](<../zh-cn/%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6%E5%88%97%E8%A1%A8.html> "ACL")，请使用如下命令： 
    
    # zfs set acltype=posixacl <nameofzpool>/<nameofdataset>
    # zfs set xattr=sa <nameofzpool>/<nameofdataset>
    
出于性能原因，建议配置 `xattr` [[1]](<https://github.com/openzfs/zfs/issues/170#issuecomment-27348094>)。 

鉴于数据集会继承 ACL 参数，最好是对 zpool 启用 ACL。默认模式为 `restricted`，你可能会需要修改其设置：`aclinherit=passthrough` [[2]](<https://docs.oracle.com/cd/E19120-01/open.solaris/817-2271/gbaaz/index.html>)；但要注意的是，`aclinherit` 不影响 POSIX ACL [[3]](<https://askubuntu.com/questions/342553/activate-acl-for-zfs-pool-ubuntu-13-04#comment1220577_392008>): 
    
    # zfs set aclinherit=passthrough <nameofzpool>
    # zfs set acltype=posixacl <nameofzpool>
    # zfs set xattr=sa <nameofzpool>
    
### Databases

ZFS, unlike most other file systems, has a variable record size, or what is commonly referred to as a block size. By default, the recordsize on ZFS is 128KiB, which means it will dynamically allocate blocks of any size from 512B to 128KiB depending on the size of file being written. This can often help fragmentation and file access, at the cost that ZFS would have to allocate new 128KiB blocks each time only a few bytes are written to. 

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** At least MariaDB uses a default of 16Kib pages! Check your specific DBMS before setting this value.（在 [Talk:ZFS](<../zh-cn/Talk:ZFS.html>) 中讨论）

Most RDBMSes work in 8KiB-sized blocks by default. Although the block size is tunable for [MySQL/MariaDB](<../zh-cn/MySQL.html> "MySQL"), [PostgreSQL](<../zh-cn/PostgreSQL.html> "PostgreSQL"), and Oracle database, all three of them use an 8KiB block size _by default_. For both performance concerns and keeping snapshot differences to a minimum (for backup purposes, this is helpful), it is usually desirable to tune ZFS instead to accommodate the databases, using a command such as: 
    
    # zfs set recordsize=8K <pool>/postgres
    
These RDBMSes also tend to implement their own caching algorithm, often similar to ZFS's own ARC. In the interest of saving memory, it is best to simply disable ZFS's caching of the database's file data and let the database do its own job: 

**注意：**[L2ARC](<#L2ARC>) requires `primarycache` to function, because it is fed with data evicted from `primarycache`. If you intend to use the L2ARC, do not set the option below, otherwise no actual data will be cached on L2ARC.
    
    # zfs set primarycache=metadata <pool>/postgres
    
ZFS uses the [ZIL](<#ZIL>) for crash recovery, but databases are often syncing their data files to the file system on their own transaction commits anyway. The end result of this is that ZFS will be committing data **twice** to the data disks, and it can severely impact performance. You can tell ZFS to prefer to not use the ZIL, and in which case, data is only committed to the file system once. However, doing so on non-solid state storage (e.g. HDDs) can result in decreased read performance due to fragmentation ([OpenZFS Wiki](<https://openzfs.org/wiki/ZFS_on_high_latency_devices>)) -- with mechanical hard drives, please consider using a dedicated SSD as [ZIL](<#ZIL>) rather than setting the option below. In addition, setting this for non-database file systems, or for pools with configured log devices, can also _negatively_ impact the performance, so beware: 
    
    # zfs set logbias=throughput <pool>/postgres
    
These can also be done at file system creation time, for example: 
    
    # zfs create -o recordsize=8K \
                 -o primarycache=metadata \
                 -o mountpoint=/var/lib/postgres \
                 -o logbias=throughput \
                  <pool>/postgres
    
Please note: these kinds of tuning parameters are ideal for specialized applications like RDBMSes. You can easily _hurt_ ZFS's performance by setting these on a general-purpose file system such as your /home directory. 

###  /tmp

If you would like to use ZFS to store your /tmp directory, which may be useful for storing arbitrarily-large sets of files or simply keeping your RAM free of idle data, you can generally improve performance of certain applications writing to /tmp by disabling file system sync. This causes ZFS to ignore an application's sync requests (eg, with `fsync` or `O_SYNC`) and return immediately. While this has severe application-side data consistency consequences (never disable sync for a database!), files in /tmp are less likely to be important and affected. Please note this does _not_ affect the integrity of ZFS itself, only the possibility that data an application expects on-disk may not have actually been written out following a crash. 
    
    # zfs set sync=disabled <pool>/tmp
    
Additionally, for security purposes, you may want to disable **setuid** and **devices** on the /tmp file system, which prevents some kinds of privilege-escalation attacks or the use of device nodes: 
    
    # zfs set setuid=off <pool>/tmp
    # zfs set devices=off <pool>/tmp
    
Combining all of these for a create command would be as follows: 
    
    # zfs create -o setuid=off -o devices=off -o sync=disabled -o mountpoint=/tmp <pool>/tmp
    
Please note, also, that if you want /tmp on ZFS, you will need to [mask](</wzh/index.php?title=Mask&action=edit&redlink=1> "Mask（页面不存在）") (disable) [systemd](<../zh-cn/Systemd.html> "Systemd")'s automatic tmpfs-backed /tmp (`tmp.mount`, else ZFS will be unable to mount your dataset at boot-time or import-time. 

###  使用 ZFS Send 和 ZFS Recv 传输快照

通过搭配使用 `zfs send` 和 `zfs recv`，可以将 ZFS 快照传输到任意目标。该操作通过标准输出实现，可以将数据发送到任意文件、设备或网络目标，也可以在管道中加入其它程序对数据流进行中间操作。 

以下为常见用例： 

####  ZFS Send 基本用法

首先为一个 ZFS 文件系统创建快照： 
    
    # zfs snapshot zpool0/archive/books@snap
    
然后将快照发送到另一 zpool 上的新位置： 
    
    # zfs send -v zpool0/archive/books@snap | zfs recv zpool4/library
    
现在 `zpool0/archive/books@snap` 上的内容就被发送到了 `zpool4/library`。 

**提示：** 各命令行选项的具体信息请参考 [man zfs-send](<https://openzfs.github.io/openzfs-docs/man/8/zfs-send.8.html>) 和 [man zfs-recv](<https://openzfs.github.io/openzfs-docs/man/8/zfs-recv.8.html>)。

#####  传入/传出到文件

首先为一个 ZFS 文件系统创建快照： 
    
    # zfs snapshot zpool0/archive/books@snap
    
将快照写入到 gzip 文件： 
    
    # zfs send zpool0/archive/books@snap > /tmp/mybooks.gz
    
**警告：** 如果想在发送时保留加密，需对 `zfs send` 使用 `-w` 选项。

从文件恢复快照： 
    
    # gzcat /tmp/mybooks.gz | zfs recv -F zpool0/archive/books
    
####  通过 SSH 发送

首先为一个 ZFS 文件系统创建快照： 
    
    # zfs snapshot zpool1/filestore@snap
    
下一步是通过管道将数据“发送”到运行“recv”的 ssh 会话： 
    
    # zfs send -v zpool1/filestore@snap | ssh $HOST zfs recv coldstore/backups
    
使用 `-v` 选项将会输出数据流的信息。如果你使用密码或密钥，会出现提示要求进行输入。 

####  增量备份

You may wish update a previously sent ZFS filesystem without retransmitting all of the data over again. Alternatively, it may be necessary to keep a filesystem online during a lengthy transfer and it is now time to send writes that were made since the initial snapshot. 

首先为一个 ZFS 文件系统创建快照： 
    
    # zfs snapshot zpool1/filestore@initial
    
下一步是通过管道将数据“发送”到运行“recv”的 ssh 会话： 
    
    # zfs send -v -R zpool1/filestore@initial | ssh $HOST zfs recv coldstore/backups
    
在写入更改后，再创建一个快照： 
    
    # zfs snapshot zpool1/filestore@snap2
    
接下来发送本地 zpool1/filestore@initial 和 zpool1/filestore@snap2 两个快照的区别，然后为远程文件系统 coldstore/backups 再创建一个快照： 
    
    # zfs send -v -i -R zpool1/filestore@initial | ssh $HOST zfs recv coldstore/backups
    
现在 zpool1/filestore 和 coldstore/backups 都存有 @initial 和 @snap2 两个快照。 

你可能会想在远程主机上将最新快照作为当前活动文件系统： 
    
    # rollback coldstore/backups@snap2
    
##  调校

###  通用

可以使用参数进一步调整 ZFS 池和数据集。 

**注意：** 除配额和预留外，所有可设置的属性值都会从父数据集继承。

要检索当前 ZFS 池的参数状态，请执行以下操作： 
    
    # zfs get all <pool>
    
要检索指定数据集的参数状态，请执行以下操作： 
    
    # zfs get all <pool>/<dataset>
    
要禁用默认启用的访问时间功能（atime），请执行以下操作： 
    
    # zfs set atime=off <pool>
    
要禁用特定数据集的访问时间功能（atime），请执行以下操作： 
    
    # zfs set atime=off <pool>/<dataset>
    
除了完全关闭 atime 之外，您还可以使用 `relatime`。这为ZFS带来了默认的 ext4/XFS atime 语义，只有在修改或更改时间发生变化时，或者访问时间在过去24小时内没有变化时，才更新访问时间。这是 `atime=off` 和 `atime=on` 之间的折衷。该属性 _只_ 在 `atime` 为 `on` 时生效： 
    
    # zfs set atime=on <pool>
    # zfs set relatime=on <pool>
    
压缩功能则是对数据的透明压缩。ZFS 支持数种不同的压缩算法，目前默认采用 lz4 。 _gzip_ 比较适合用于那些不频繁写入并且可压缩率较高的数据。请参考 [OpenZFS Wiki](<https://openzfs.github.io/openzfs-docs/Performance%20and%20Tuning/Workload%20Tuning.html>) 以获得更多信息。 

要启用压缩，请执行： 
    
    # zfs set compression=on <pool>
    
若要将池和/或数据集的属性重置为默认状态，请使用 `zfs inherit`： 
    
    # zfs inherit -rS atime <pool>
    # zfs inherit -rS atime <pool>/<dataset>
    
**注意：** 使用 `-r` 标志将递归重置ZPool中的所有数据集。

### Scrubbing

当 ZFS 在读取数据过程中检测到错误时，它会在可能时静默修复数据，写回到磁盘并记录日志，使得你可以获得存储池中错误的概览。ZFS 没有 fsck 一类的工具，但提供了称为 scrubbing 的特性。它会遍历存储池中的所有数据，并验证是否所有块都可被正常读取。 

要对存储池执行 scrub： 
    
    # zpool scrub <pool>
    
要中断运行中的 scrub： 
    
    # zpool scrub -s <pool>
    
####  多久需要运行一次呢？

根据 Oracle 的博客文章 [Disk Scrub - Why and When?](<https://blogs.oracle.com/wonders-of-zfs-storage/disk-scrub-why-and-when-v2>): 

    这一问题对支持人员来说有难度，因为最贴切的回答是“看情况”。所以，在我给出一个较通用的回答前，有些可以用来创建更贴合你需求的答案的提示。

  * 你最旧的备份的有效期是多久？对数据执行 scrub 操作的频率因至少与你最旧备份的有效期相当，以确保回复点可用。
  * 你通常多久会碰到一次磁盘故障？While the recruitment of a hot-spare disk invokes a "resilver" -- a targeted scrub of just the VDEV which lost a disk -- you should probably scrub at least as often as you experience disk failures on average in your specific environment.
  * 你多久会读取一次磁盘上最旧的数据？你应偶尔进行一次 scrub，以防止旧数据在你不知道的情况下出现位腐坏。

    如果针对上述任一问题的答案是“我不知道”，那最通用的回答是：你应至少每月对 zpool 执行一次 scrub 操作。这一周期对多数用例来说都较为合适，提供了足以在各种高负载环境下完成运行的时间，并快于大型 zpools（192+ 磁盘）出现磁盘故障的时间。

根据 Aaron Toponce 的 [ZFS Administration Guide](<https://pthree.org/2012/12/11/zfs-administration-part-vi-scrub-and-resilver/>)，他建议对消费级磁盘每周执行一次 scrub。 

####  根据服务或定时器运行

**注意：** 从 OpenZFS 2.1.3 开始提供了每周/月运行的 [systemd](<../zh-cn/Systemd.html> "Systemd") 定时器/服务。使用时需根据目标存储池 [启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")/[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `zfs-scrub-weekly@_pool-to-scrub_.timer` 或 `zfs-scrub-monthly@_pool-to-scrub_.timer`。

可以使用 [systemd](<../zh-cn/Systemd.html> "Systemd") 定时器/服务来自动对存储池执行 scrub。 

要对特定存储池执行每月 scrubbing： 
    
    /etc/systemd/system/zfs-scrub@.timer
    
    [Unit]
    Description=Monthly zpool scrub on %i
    
    [Timer]
    OnCalendar=monthly
    AccuracySec=1h
    Persistent=true
    
    [Install]
    WantedBy=multi-user.target
    
    /etc/systemd/system/zfs-scrub@.service
    
    [Unit]
    Description=zpool scrub on %i
    
    [Service]
    Nice=19
    IOSchedulingClass=idle
    KillSignal=SIGINT
    ExecStart=/usr/bin/zpool scrub %i
    
    [Install]
    WantedBy=multi-user.target

[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")/[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `zfs-scrub@_pool-to-scrub_.timer` 单元以为特定 zpool 启用月度 scrubbing。 

###  启用 TRIM

要检查你的 vdev 是否支持 [TRIM](<../zh-cn/%E5%9B%BA%E6%80%81%E7%A1%AC%E7%9B%98.html#TRIM> "TRIM")，你可以通过 `-t` 为 `zpool status` 输出添加 TRIM 信息： 
    
    $ zpool status -t tank
    
    pool: tank
     state: ONLINE
      scan: none requested
     config:
    
    	NAME                                     STATE     READ WRITE CKSUM
    	tank                                     ONLINE       0     0     0
    	  ata-ST31000524AS_5RP4SSNR-part1        ONLINE       0     0     0  (trim unsupported)
    	  ata-CT480BX500SSD1_2134A59B933D-part1  ONLINE       0     0     0  (untrimmed)
    
    errors: No known data errors

ZFS 可以手动或通过 `autotrim` 定时对支持的设备进行 TRIM。 

对 zpool 手动进行 TRIM： 
    
     # zpool trim <zpool>
    
为数据池中所有支持的 vdev 启用自动 TRIM： 
    
     # zpool set autotrim=on <zpool>
    
**注意：** 因为自动 TRIM 与 `zpool trim` 的操作有所不同，[你可能会想偶尔手动执行 TRIM。](<https://github.com/openzfs/zfs/commit/1b939560be5c51deecf875af9dada9d094633bf7>)

要使用 [systemd](<../zh-cn/Systemd.html> "Systemd") 定时器/服务对特定存储池每月执行一次完整的 `zpool trim`： 
    
    /etc/systemd/system/zfs-trim@.timer
    
    [Unit]
    Description=Monthly zpool trim on %i
    
    [Timer]
    OnCalendar=monthly
    AccuracySec=1h
    Persistent=true
    
    [Install]
    WantedBy=multi-user.target
    
    /etc/systemd/system/zfs-trim@.service
    
    [Unit]
    Description=zpool trim on %i
    Documentation=man:zpool-trim(8)
    Requires=zfs.target
    After=zfs.target
    ConditionACPower=true
    ConditionPathIsDirectory=/sys/module/zfs
    
    [Service]
    Nice=19
    IOSchedulingClass=idle
    KillSignal=SIGINT
    ExecStart=/bin/sh -c '\
    if /usr/bin/zpool status %i | grep "trimming"; then\
    exec /usr/bin/zpool wait -t trim %i;\
    else exec /usr/bin/zpool trim -w %i; fi'
    ExecStop=-/bin/sh -c '/usr/bin/zpool trim -s %i 2>/dev/null || true'
    
    [Install]
    WantedBy=multi-user.target

[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")/[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `zfs-trim@_pool-to-trim_.timer` 单元以对特定存储池启用 TRIM。 

### SSD Caching

If your pool has no configured log devices, ZFS reserves space on the pool's data disks for its intent log (the ZIL, also called SLOG). If your data disks are slow (e.g. HDD) it is highly recommended to configure the ZIL on solid state drives for better write performance and also to consider a layer 2 adaptive replacement cache (L2ARC). The process to add them is very similar to adding a new VDEV. 

All of the below references to device-id are the IDs from `/dev/disk/by-id/*`. 

#### ZIL

To add a mirrored ZIL: 
    
     # zpool add <pool> log mirror <device-id-1> <device-id-2>
    
Or to add a single device ZIL: 
    
     # zpool add <pool> log <device-id>
    
Because the ZIL device stores data that has not been written to the pool, it is important to use devices that can finish writes when power is lost. It is also important to use redundancy, since a device failure can cause data loss. In addition, the ZIL is only used for sync writes, so may not provide any performance improvement when your data drives are as fast as your ZIL drive(s). 

#### L2ARC

使用如下命令添加 L2ARC： 
    
    # zpool add <pool> cache <device-id>
    
L2ARC 是只读缓存，所以不需要任何冗余。从 [ZFS 2.0.0 版本](<https://github.com/openzfs/zfs/releases/tag/zfs-2.0.0>)开始，L2ARC 可以在重启后保留。[[4]](<https://github.com/openzfs/zfs/pull/9582>)

L2ARC 通常只在热数据量比系统内存更**大** ，但又小到能放入 L2ARC 的情况下有用。L2ARC 由系统内存中的 ARC 进行索引，每条记录（默认为 128KiB）消耗 70 字节内存。所以，对应的内存用量可用以下公式计算： 
    
    (L2ARC 大小) / (记录大小) * 70 字节
    
因此，由于 L2ARC 占用了 ARC 的内存空间，在某些情况下它会造成存储性能的下降。 

### ZVOLs

ZFS volumes (ZVOLs) can suffer from the same block size-related issues as RDBMSes, but it is worth noting that the default recordsize for ZVOLs is 8 KiB already. If possible, it is best to align any partitions contained in a ZVOL to your recordsize (current versions of fdisk and gdisk by default automatically align at 1MiB segments, which works), and file system block sizes to the same size. Other than this, you might tweak the **recordsize** to accommodate the data inside the ZVOL as necessary (though 8 KiB tends to be a good value for most file systems, even when using 4 KiB blocks on that level). 

#### RAIDZ and Advanced Format physical disks

Each block of a ZVOL gets its own parity disks, and if you have physical media with logical block sizes of 4096B, 8192B, or so on, the parity needs to be stored in whole physical blocks, and this can drastically increase the space requirements of a ZVOL, requiring 2× or more physical storage capacity than the ZVOL's logical capacity. Setting the **recordsize** to 16k or 32k can help reduce this footprint drastically. 

See [OpenZFS issue #1807](<https://github.com/openzfs/zfs/issues/1807>) for details. 

###  I/O Scheduler

While ZFS is expected to work well with modern schedulers including, `mq-deadline`, and `none`, experimenting with [manually setting](<../zh-cn/Improving_performance.html#Changing_I/O_scheduler> "Improving performance") the I/O scheduler on ZFS disks may yield performance gains. The ZFS recomendation is "[...] users leave the default scheduler [“unless you’re encountering a specific problem, or have clearly measured a performance improvement for your workload”](<https://github.com/openzfs/zfs/issues/9778#issuecomment-569347505>)"[[5]](<https://openzfs.github.io/openzfs-docs/Performance%20and%20Tuning/Module%20Parameters.html#zfs-vdev-scheduler>)

##  排障

### Creating a zpool fails

If the following error occurs then it can be fixed. 
    
    # the kernel failed to rescan the partition table: 16
    # cannot label 'sdc': try using parted(8) and then provide a specific slice: -1
    
One reason this can occur is because ZFS expects pool creation to take less than 1 second[[6]](<https://github.com/openzfs/zfs/issues/2582>)[[7]](<https://github.com/openzfs/zfs/issues/1646>). This is a reasonable assumption under ordinary conditions, but in many situations it may take longer. Each drive will need to be cleared again before another attempt can be made. 
    
    # parted /dev/sda rm 1
    # parted /dev/sda rm 1
    # dd if=/dev/zero of=/dev/sdb bs=512 count=1
    # zpool labelclear /dev/sda
    
A brute force creation can be attempted over and over again, and with some luck the ZPool creation will take less than 1 second. One cause for creation slowdown can be slow burst read writes on a drive. By reading from the disk in parallell to ZPool creation, it may be possible to increase burst speeds. 
    
    # dd if=/dev/sda of=/dev/null
    
This can be done with multiple drives by saving the above command for each drive to a file on separate lines and running 
    
    # cat $FILE | parallel
    
Then run ZPool creation at the same time. 

### ZFS is using too much RAM

By default, ZFS caches file operations ([ARC](<https://en.wikipedia.org/wiki/Adaptive_replacement_cache> "wikipedia:Adaptive replacement cache")) using up to half of available system memory on the host. To adjust the ARC size, add the following to the [Kernel parameters](<../zh-cn/Kernel_parameters.html> "Kernel parameters") list: 
    
    zfs.zfs_arc_max=536870912 # (for 512MiB)
    
In case that the default value of `zfs_arc_min` (1/32 of system memory) is higher than the specified `zfs_arc_max` it is needed to add also the following to the [Kernel parameters](<../zh-cn/Kernel_parameters.html> "Kernel parameters") list: 
    
    zfs.zfs_arc_min=268435456 # (for 256MiB, needs to be lower than zfs.zfs_arc_max)
    
You may also want to increase `zfs_arc_sys_free` instead (in this example to 8GiB): 
    
    # echo $((8*1024**3)) > /sys/module/zfs/parameters/zfs_arc_sys_free
    
For a more detailed description, as well as other configuration options, see [Gentoo:ZFS#ARC](<https://wiki.gentoo.org/wiki/ZFS#ARC> "gentoo:ZFS"). 

ZFS should release ARC as applications reserve more RAM, but some applications still [get confused](<https://github.com/openzfs/zfs/issues/10255>), and reported [free RAM is always wrong](<https://github.com/openzfs/zfs/issues/10251>). But in case all your applications work as intended and you have no problems, there is no need to change ARC settings. 

### No hostid found

An error that occurs at boot with the following lines appearing before initscript output: 
    
    ZFS: No hostid found on kernel command line or /etc/hostid.
    
This warning occurs because the ZFS module does not have access to the spl hosted. There are two solutions, for this. Either place the spl hostid in the [内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数") in the boot loader. For example, adding `spl.spl_hostid=0x00bab10c`. 

The other solution is to make sure that there is a hostid in `/etc/hostid`, and then [regenerate the initramfs](<../zh-cn/Regenerate_the_initramfs.html> "Regenerate the initramfs") image. Which will copy the hostid into the initramfs image. 

###  Pool cannot be found while booting from SAS/SCSI devices

In case you are booting a SAS/SCSI based, you might occassionally get boot problems where the pool you are trying to boot from cannot be found. A likely reason for this is that your devices are initialized too late into the process. That means that zfs cannot find any devices at the time when it tries to assemble your pool. 

In this case you should force the scsi driver to wait for devices to come online before continuing. You can do this by putting this into `/etc/modprobe.d/zfs.conf`: 
    
    /etc/modprobe.d/zfs.conf
    
    options scsi_mod scan=sync

Afterwards, [regenerate the initramfs](<../zh-cn/Regenerate_the_initramfs.html> "Regenerate the initramfs"). 

This works because the zfs hook will copy the file at `/etc/modprobe.d/zfs.conf` into the initcpio which will then be used at build time. 

###  On boot the zfs pool does not mount stating: "pool may be in use from other system"

#### Unexported pool

If the new installation does not boot because the zpool cannot be imported, chroot into the installation and properly export the zpool. See [#Emergency chroot repair with archzfs](<#Emergency_chroot_repair_with_archzfs>). 

Once inside the chroot environment, load the ZFS module and force import the zpool, 
    
    # zpool import -a -f
    
now export the pool: 
    
    # zpool export <pool>
    
To see the available pools, use, 
    
    # zpool status
    
It is necessary to export a pool because of the way ZFS uses the hostid to track the system the zpool was created on. The hostid is generated partly based on the network setup. During the installation in the archiso the network configuration could be different generating a different hostid than the one contained in the new installation. Once the zfs filesystem is exported and then re-imported in the new installation, the hostid is reset. See [Re: Howto zpool import/export automatically? - msg#00227](<https://web.archive.org/web/20151101094022/http://osdir.com/ml/zfs-discuss/2011-06/msg00227.html>). 

If ZFS complains about "pool may be in use" after every reboot, properly export pool as described above, and then [regenerate the initramfs](<../zh-cn/Regenerate_the_initramfs.html> "Regenerate the initramfs") in normally booted system. 

#### Incorrect hostid

Double check that the pool is properly exported. Exporting the zpool clears the hostid marking the ownership. So during the first boot the zpool should mount correctly. If it does not there is some other problem. 

Reboot again, if the zfs pool refuses to mount it means the hostid is not yet correctly set in the early boot phase and it confuses zfs. Manually tell zfs the correct number, once the hostid is coherent across the reboots the zpool will mount correctly. 

Boot using zfs_force and write down the hostid. This one is just an example. 
    
    $ hostid
    
    0a0af0f8
    
This number have to be added to the [内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数") as `spl.spl_hostid=0x0a0af0f8`. Another solution is writing the hostid inside the initram image, see the [installation guide](<../zh-cn/Install_Arch_Linux_on_ZFS.html#Configure_systemd_ZFS_mounts> "Install Arch Linux on ZFS")[[损坏的链接](<../Project:%E7%A4%BE%E7%BE%A4%E9%A6%96%E9%A1%B5.html#%E6%8D%9F%E5%9D%8F%E7%9A%84%E9%93%BE%E6%8E%A5> "Project:社群首页")：无效的章节] explanation about this. 

Users can always ignore the check adding `zfs_force=1` in the [内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数"), but it is not advisable as a permanent solution. 

### Devices have different sector alignment

Once a drive has become faulted it should be replaced A.S.A.P. with an identical drive. 
    
    # zpool replace bigdata ata-ST3000DM001-9YN166_S1F0KDGY ata-ST3000DM001-1CH166_W1F478BD -f
    
but in this instance, the following error is produced: 
    
    cannot replace ata-ST3000DM001-9YN166_S1F0KDGY with ata-ST3000DM001-1CH166_W1F478BD: devices have different sector alignment
    
ZFS uses the ashift option to adjust for physical block size. When replacing the faulted disk, ZFS is attempting to use `ashift=12`, but the faulted disk is using a different ashift (probably `ashift=9`) and this causes the resulting error. 

For Advanced Format disks with 4 KiB block size, an `ashift` of `12` is recommended for best performance. See [OpenZFS FAQ: Performance Considerations](<https://openzfs.github.io/openzfs-docs/Project%20and%20Community/FAQ.html#performance-considerations>) and [ZFS and Advanced Format disks](<https://web.archive.org/web/20170913063528/https://wiki.illumos.org/display/illumos/ZFS+and+Advanced+Format+disks>). 

Use zdb to find the ashift of the zpool: `zdb `, then use the `-o` argument to set the ashift of the replacement drive: 
    
    # zpool replace bigdata ata-ST3000DM001-9YN166_S1F0KDGY ata-ST3000DM001-1CH166_W1F478BD -o ashift=9 -f
    
Check the zpool status for confirmation: 
    
    # zpool status -v
    
    pool: bigdata
    state: DEGRADED
    status: One or more devices is currently being resilvered.  The pool will
            continue to function, possibly in a degraded state.
    action: Wait for the resilver to complete.
    scan: resilver in progress since Mon Jun 16 11:16:28 2014
        10.3G scanned out of 5.90T at 81.7M/s, 20h59m to go
        2.57G resilvered, 0.17% done
    config:
    
            NAME                                   STATE     READ WRITE CKSUM
            bigdata                                DEGRADED     0     0     0
            raidz1-0                               DEGRADED     0     0     0
                replacing-0                        OFFLINE      0     0     0
                ata-ST3000DM001-9YN166_S1F0KDGY    OFFLINE      0     0     0
                ata-ST3000DM001-1CH166_W1F478BD    ONLINE       0     0     0  (resilvering)
                ata-ST3000DM001-9YN166_S1F0JKRR    ONLINE       0     0     0
                ata-ST3000DM001-9YN166_S1F0KBP8    ONLINE       0     0     0
                ata-ST3000DM001-9YN166_S1F0JTM1    ONLINE       0     0     0
    
    errors: No known data errors
    
###  Pool resilvering stuck/restarting/slow?

According to [ZFS issue #840](<https://github.com/openzfs/zfs/issues/840>), this is a known issue since 2012 with ZFS-ZED which causes the resilvering process to constantly restart, sometimes get stuck and be generally slow for some hardware. The simplest mitigation is to stop zfs-zed.service until the resilver completes. 

### Fix slow boot caused by failed import of unavailable pools in the initramfs zpool.cache

Your boot time can be significantly impacted if you update your intitramfs (eg when doing a kernel update) when you have additional but non-permanently attached pools imported because these pools will get added to your initramfs zpool.cache and ZFS will attempt to import these extra pools on every boot, regardless of whether you have exported it and removed it from your regular zpool.cache. 

If you notice ZFS trying to import unavailable pools at boot, first run: 
    
    $ zdb -C
    
To check your zpool.cache for pools you do not want imported at boot. If this command is showing (a) additional, currently unavailable pool(s), run: 
    
    # zpool set cachefile=/etc/zfs/zpool.cache zroot
    
To clear the zpool.cache of any pools other than the pool named zroot. Sometimes there is no need to refresh your zpool.cache, but instead all you need to do is [regenerate the initramfs](<../zh-cn/Regenerate_the_initramfs.html> "Regenerate the initramfs"). 

### ZFS Command History

ZFS logs changes to a pool's structure natively as a log of executed commands in a ring buffer (which cannot be turned off). The log may be helpful when restoring a degraded or failed pool. 
    
    # zpool history zpool
    
    History for 'zpool':
    2023-02-19.16:28:44 zpool create zpool raidz1 /scratch/disk_1.img /scratch/disk_2.img /scratch/disk_3.img
    2023-02-19.16:31:29 zfs set compression=lz4 zpool
    2023-02-19.16:41:45 zpool scrub zpool
    2023-02-19.17:00:57 zpool replace zpool /scratch/disk_1.img /scratch/bigger_disk_1.img
    2023-02-19.17:01:34 zpool scrub zpool
    2023-02-19.17:01:42 zpool replace zpool /scratch/disk_2.img /scratch/bigger_disk_2.img
    2023-02-19.17:01:46 zpool replace zpool /scratch/disk_3.img /scratch/bigger_disk_3.img
    
##  小技巧

###  创建带有 ZFS 支持的 Archiso 映像

[![](../File:Tango-go-next.png)](<../File:Tango-go-next.png>)**此页面或章节适合移动到[在自定义的 archiso 安装介质中启用 ZFS 模块](</wzh/index.php?title=%E5%9C%A8%E8%87%AA%E5%AE%9A%E4%B9%89%E7%9A%84_archiso_%E5%AE%89%E8%A3%85%E4%BB%8B%E8%B4%A8%E4%B8%AD%E5%90%AF%E7%94%A8_ZFS_%E6%A8%A1%E5%9D%97&action=edit&redlink=1> "在自定义的 archiso 安装介质中启用 ZFS 模块（页面不存在）")。**

**附注：** The target links here for its Arch instructions, but is the natural context.（在 [Talk:ZFS](<../zh-cn/Talk:ZFS.html>) 讨论）

创建 Arch Linux live CD/DVD/USB 映像的具体步骤在 [Archiso](<../zh-cn/Archiso.html> "Archiso") 中已有描述。如需在映像中加入 ZFS 支持，可以选择手动构建 AUR 上的 PKGBUILDs，或是在映像中加入[非官方用户仓库](<../zh-cn/%E9%9D%9E%E5%AE%98%E6%96%B9%E7%94%A8%E6%88%B7%E4%BB%93%E5%BA%93.html> "非官方用户仓库")中的预构建包。 

####  使用 AUR 自行构建 ZFS 包

参考[正常流程](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93_\(AUR\).html#%E6%9E%84%E5%BB%BA%E8%BD%AF%E4%BB%B6%E5%8C%85> "Arch 用户软件仓库 \(AUR\)")自行构建你需要的 ZFS 包。如果你不确定需要哪个包，[zfs-dkms](<https://aur.archlinux.org/packages/zfs-dkms/>)AUR 和 [zfs-utils](<https://aur.archlinux.org/packages/zfs-utils/>)AUR 可以支持你在 Archiso 映像上做出的多数改动。下一步需要[创建一个本地仓库](<../zh-cn/Pacman/%E6%8F%90%E7%A4%BA%E5%92%8C%E6%8A%80%E5%B7%A7.html#%E8%87%AA%E5%BB%BA%E6%9C%AC%E5%9C%B0%E4%BB%93%E5%BA%93> "Pacman/提示和技巧")，并[将仓库添加到](<../zh-cn/Archiso.html#%E8%87%AA%E5%AE%9A%E4%B9%89%E6%9C%AC%E5%9C%B0%E4%BB%93%E5%BA%93> "Archiso")新配置的 Pacman 配置文件中。 

将构建出的包添加到要安装的包列表中。下面的例子假设你仅想安装 [zfs-dkms](<https://aur.archlinux.org/packages/zfs-dkms/>)AUR 和 [zfs-utils](<https://aur.archlinux.org/packages/zfs-utils/>)AUR 包： 
    
    packages.x86_64
    
    ...
    zfs-dkms
    zfs-utils
    
如果你添加了任何 [DKMS](<../zh-cn/DKMS.html> "DKMS") 包，请确保你同时添加了 ISO 所用内核对应的头文件包（默认内核对应为 [linux-headers](<https://archlinux.org/packages/?name=linux-headers>)包）。 

####  使用 archzfs 非官方用户仓库

将 [archzfs](<../zh-cn/%E9%9D%9E%E5%AE%98%E6%96%B9%E7%94%A8%E6%88%B7%E4%BB%93%E5%BA%93.html#archzfs> "非官方用户仓库") 非官方用户仓库添加到新 Archiso 配置中的 `pacman.conf` 文件中。 

将 `archzfs-linux` 软件包组添加到要安装的软件包包列表中（`archzfs` 仓库提供的包仅支持 x86_64 架构）： 
    
    packages.x86_64
    
    ...
    archzfs-linux
    
**注意：** 如果你稍后在运行 modprobe zfs 的过程中出现报错，需在 packages.x86_64 中加入 linux-headers 包。

####  收尾

无论你使用了哪种方法，最后都需要[构建 ISO 映像](<../zh-cn/Archiso.html#%E6%9E%84%E5%BB%BA_ISO_%E6%98%A0%E5%83%8F> "Archiso")。 

###  自动快照

#### zrepl

[zrepl](<https://aur.archlinux.org/packages/zrepl/>)AUR 包提供了一个 ZFS 自动复制服务，可被用作类似 [snapper](<../zh-cn/Snapper.html> "Snapper") 的快照服务。 

关于配置 zrepl 守护进程的详细方法请参考 [zrepl 文档](<https://zrepl.github.io/>)，配置文件位于 `/etc/zrepl/zrepl.yml`。完成后，先使用 `zrepl configcheck` 检查配置文件是否有语法问题，再启用 `zrepl.service` 服务。 

#### sanoid

[sanoid](<https://aur.archlinux.org/packages/sanoid/>)AUR 是一个策略驱动的快照工具，它还提供了 `syncoid`，可用于复制快照。它也附带了 systemd 服务和定时器。 

Sanoid 只会清理本地系统的快照，如果要清理远程系统的快照，需要在远程系统上使用 prune 选项运行 sanoid。可以使用 `--prune-snapshots` 命令行选项，也可以将 `--cron` 命令行选项搭配 `autoprune = yes` 和 `autosnap = no` 配置选项使用。 

#### zfs-auto-snapshot

**注意：** [zfs-auto-snapshot-git](<https://aur.archlinux.org/packages/zfs-auto-snapshot-git/>)AUR 从 2019 年开始就没有被更新过了，而且功能上比较受限。建议使用如 [zrepl](<https://aur.archlinux.org/packages/zrepl/>)AUR 等更新的工具。

The [zfs-auto-snapshot-git](<https://aur.archlinux.org/packages/zfs-auto-snapshot-git/>)AUR 包提供了一个 shell 脚本，可以自动为所有 ZFS 数据集生成并管理由日期和标签（如每小时，每日等）命名的快照。该包还会安装每十五分钟、每小时、每天、每周、每月进行快照的 cron 任务。你还可以调整 `--keep parameter` 选项来设定要保留快照的时长（每月快照的脚本默认将数据保留一年）。 

如果不想对某个数据集进行快照，可以对其设置 `com.sun:auto-snapshot=false`。如果不想进行月度快照，还可以通过标签进行更精细化的配置：`com.sun:auto-snapshot:monthly=false`。 

**注意：** 在 [scrubbing](<#Scrubbing>) 期间，zfs-auto-snapshot-git 不会创建快照。你可以[修改提供的 systemd 单元文件](<../zh-cn/Systemd.html#%E4%BF%AE%E6%94%B9%E7%8E%B0%E5%AD%98%E5%8D%95%E5%85%83%E6%96%87%E4%BB%B6> "Systemd")，移除 `ExecStart` 中的 `--skip-scrub` 选项来绕过该限制，但不清楚是否有任何后果，有知道的请协助添加相关内容。

安装该软件包后，[启用并启动你想要的定时器](<../zh-cn/Systemd/%E5%AE%9A%E6%97%B6%E5%99%A8.html> "Systemd/定时器")（`zfs-auto-snapshot-{frequent,daily,weekly,monthly}.timer`）。 

###  创建共享

ZFS 支持创建 [NFS](<../zh-cn/NFS.html> "NFS") 或 [SMB](</wzh/index.php?title=SMB&action=edit&redlink=1> "SMB（页面不存在）") 共享。 

#### NFS

首先，确保系统已经安装并配置了 [NFS](<../zh-cn/NFS.html> "NFS")。注意：无需编辑 `/etc/exports`。对于 NFS 共享，确保已经[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `nfs-server.service` 和 `zfs-share.service`。 

要将存储池共享到网络： 
    
    # zfs set sharenfs=on _存储池名_
    
要将数据集共享到网络： 
    
    # zfs set sharenfs=on _存储池名_ /_数据集名_
    
要为特定 IP 段启用读写权限： 
    
    # zfs set sharenfs="rw=@192.168.1.100/24,rw=@10.0.0.0/24" _存储池名_ /_数据集名_
    
要确认数据集是否已成功导出： 
    
    # showmount -e `hostname`
    
    Export list for hostname:
    /path/of/dataset 192.168.1.100/24
    
要确认当前导出状态的详细信息： 
    
    # exportfs -v
    
    _/path/of/dataset_
        192.168.1.100/24(sync,wdelay,hide,no_subtree_check,mountpoint,sec=sys,rw,secure,no_root_squash,no_all_squash)

要通过 ZFS 查看当前 NFS 共享列表： 
    
    # zfs get sharenfs
    
#### SMB

**注意：** SMB functionality is very limited. The usershare path must be `/var/lib/samba/usershares` and the only supported sharesmb options are `on` and `off`. Enabling guest access via `sharesmb=guest_ok=y` is not supported. 

When sharing through SMB, using `usershares` in `/etc/samba/smb.conf` will allow ZFS to setup and create the shares. See [Samba#Enable Usershares](<../zh-cn/Samba.html#Enable_Usershares> "Samba") for details. 
    
    /etc/samba/smb.conf
    
    [global]
        usershare path = /var/lib/samba/usershares
        usershare max shares = 100
        usershare allow guests = yes
        usershare owner only = no

Create and set permissions on the user directory as root 
    
    # mkdir /var/lib/samba/usershares
    # chmod +t /var/lib/samba/usershares
    
To make a pool available on the network: 
    
    # zfs set sharesmb=on _nameofzpool_
    
To make a dataset available on the network: 
    
    # zfs set sharesmb=on _nameofzpool_ /_nameofdataset_
    
To check if the dataset is exported successfully: 
    
    # smbclient -L localhost -U%
    
            Sharename       Type      Comment
            ---------       ----      -------
            IPC$            IPC       IPC Service (SMB Server Name)
            _nameofzpool_ __nameofdataset_        Disk      Comment: path/of/dataset
    SMB1 disabled -- no workgroup available
    
To view the current SMB share list by ZFS: 
    
    # zfs get sharesmb
    
### Encryption in ZFS using dm-crypt

Before [OpenZFS version 0.8.0](<https://github.com/openzfs/zfs/releases/tag/zfs-0.8.0>), ZFS did not support encryption directly (See [#Native encryption](<#Native_encryption>)). Instead, zpools can be created on [dm-crypt](<../zh-cn/Dm-crypt.html> "Dm-crypt") block devices. Since the zpool is created on the plain-text abstraction, it is possible to have the data encrypted while having all the advantages of ZFS like deduplication, compression, and data robustness. Furthermore, utilizing dm-crypt will encrypt the zpools metadata, which the native encryption can inherently not provide.[[8]](<https://openzfs.github.io/openzfs-docs/man/8/zfs-change-key.8.html#Encryption>)

dm-crypt, possibly via LUKS, creates devices in `/dev/mapper` and their name is fixed. So you just need to change `zpool create` commands to point to that names. The idea is configuring the system to create the `/dev/mapper` block devices and import the zpools from there. Since zpools can be created in multiple devices (raid, mirroring, striping, ...), it is important all the devices are encrypted otherwise the protection might be partially lost. 

For example, an encrypted zpool can be created using plain dm-crypt (without LUKS) with: 
    
    # cryptsetup open --type=plain --hash=sha256 --cipher=aes-xts-plain64 --offset=0 \
                 --key-file=/dev/sdZ --key-size=512 /dev/sdX enc
    # zpool create zroot /dev/mapper/enc
    
In the case of a root filesystem pool, the `mkinitcpio.conf` HOOKS line will enable the keyboard for the password, create the devices, and load the pools. It will contain something like: 
    
    HOOKS=(... keyboard encrypt zfs ...)
    
Since the `/dev/mapper/enc` name is fixed no import errors will occur. 

Creating encrypted zpools works fine. But if you need encrypted directories, for example to protect your users' homes, ZFS loses some functionality. 

ZFS will see the encrypted data, not the plain-text abstraction, so compression and deduplication will not work. The reason is that encrypted data has always high entropy making compression ineffective and even from the same input you get different output (thanks to salting) making deduplication impossible. To reduce the unnecessary overhead it is possible to create a sub-filesystem for each encrypted directory and use [eCryptfs](</wzh/index.php?title=ECryptfs&action=edit&redlink=1> "ECryptfs（页面不存在）") on it. 

For example to have an encrypted home: (the two passwords, encryption and login, must be the same) 
    
    # zfs create -o compression=off -o dedup=off -o mountpoint=/home/<username> <zpool>/<username>
    # useradd -m <username>
    # passwd <username>
    # ecryptfs-migrate-home -u <username>
    <log in user and complete the procedure with ecryptfs-unwrap-passphrase>
    
### Emergency chroot repair with archzfs

To get into the ZFS filesystem from live system for maintenance, there are two options: 

  1. Build custom archiso with ZFS as described in [#Create an Archiso image with ZFS support](<#Create_an_Archiso_image_with_ZFS_support>).
  2. Boot the latest official archiso and bring up the network. Then enable [archzfs](<../zh-cn/Unofficial_user_repositories.html#archzfs> "Unofficial user repositories") repository inside the live system as usual, sync the pacman package database and install the _archzfs-archiso-linux_ package.

To start the recovery, load the ZFS kernel modules: 
    
    # modprobe zfs
    
Import the pool: 
    
    # zpool import -a -R /mnt
    
Mount the boot partition and EFI system partition (if any): 
    
    # mount /dev/sda2 /mnt/boot
    # mount /dev/sda1 /mnt/efi
    
Chroot into the ZFS filesystem: 
    
    # arch-chroot /mnt /bin/bash
    
Check the kernel version: 
    
    # pacman -Qi linux
    # uname -r
    
uname will show the kernel version of the archiso. If they are different, run depmod (in the chroot) with the correct kernel version of the chroot installation: 
    
    # depmod -a 3.6.9-1-ARCH (version gathered from pacman -Qi linux but using the matching kernel modules directory name under the chroot's /lib/modules)
    
This will load the correct kernel modules for the kernel version installed in the chroot installation. 

[Regenerate the initramfs](<../zh-cn/Regenerate_the_initramfs.html> "Regenerate the initramfs"). There should be no errors. 

### Bind mount

Here a bind mount from /mnt/zfspool to /srv/nfs4/music is created. The configuration ensures that the zfs pool is ready before the bind mount is created. 

#### fstab

See [systemd.mount(5)](<https://man.archlinux.org/man/systemd.mount.5>) for more information on how systemd converts fstab into mount unit files with [systemd-fstab-generator(8)](<https://man.archlinux.org/man/systemd-fstab-generator.8>). 
    
    /etc/fstab
    
    /mnt/zfspool		/srv/nfs4/music		none	bind,defaults,nofail,x-systemd.requires=zfs-mount.service	0 0
    
###  Monitoring / Mailing on Events

See [ZED: The ZFS Event Daemon](<https://ramsdenj.com/2016/08/29/arch-linux-on-zfs-part-3-followup.html>) for more information. 

An email forwarder, such as [S-nail](</wzh/index.php?title=S-nail&action=edit&redlink=1> "S-nail（页面不存在）"), is required to accomplish this. Test it to be sure it is working correctly. 

Uncomment the following in the configuration file: 
    
    /etc/zfs/zed.d/zed.rc
    
     ZED_EMAIL_ADDR="root"
     ZED_EMAIL_PROG="mailx"
     ZED_NOTIFY_VERBOSE=0
     ZED_EMAIL_OPTS="-s '@SUBJECT@' @ADDRESS@"
    
Update 'root' in `ZED_EMAIL_ADDR="root"` to the email address you want to receive notifications at. 

If you are keeping your mailrc in your home directory, you can tell mail to get it from there by setting `MAILRC`: 
    
    /etc/zfs/zed.d/zed.rc
    
    export MAILRC=/home/<user>/.mailrc

This works because ZED sources this file, so `mailx` sees this environment variable. 

If you want to receive an email no matter the state of your pool, you will want to set `ZED_NOTIFY_VERBOSE=1`. You will need to do this temporary to test. 

[Start](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") and [enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") `zfs-zed.service`. 

With `ZED_NOTIFY_VERBOSE=1`, you can test by running a scrub as root: `zpool scrub <pool-name>`. 

###  Wrap shell commands in pre & post snapshots

Since it is so cheap to make a snapshot, we can use this as a measure of security for sensitive commands such as system and package upgrades. If we make a snapshot before, and one after, we can later diff these snapshots to find out what changed on the filesystem after the command executed. Furthermore we can also rollback in case the outcome was not desired. 

#### znp

E.g.: 
    
    # zfs snapshot -r zroot@pre
    # pacman -Syu
    # zfs snapshot -r zroot@post
    # zfs diff zroot@pre zroot@post 
    # zfs rollback zroot@pre
    
A utility that automates the creation of pre and post snapshots around a shell command is [znp](<https://gist.github.com/erikw/eeec35be33e847c211acd886ffb145d5>). 

E.g.: 
    
    # znp pacman -Syu
    # znp find / -name "something*" -delete
    
and you would get snapshots created before and after the supplied command, and also output of the commands logged to file for future reference so we know what command created the diff seen in a pair of pre/post snapshots. 

### Remote unlocking of ZFS encrypted root

As of [PR #261](<https://github.com/archzfs/archzfs/pull/261>), `archzfs` supports SSH unlocking of natively-encrypted ZFS datasets. This section describes how to use this feature, and is largely based on [dm-crypt/特殊应用#基于BusyBox的initramfs（使用mkinitcpio）构建](<../zh-cn/Dm-crypt/%E7%89%B9%E6%AE%8A%E5%BA%94%E7%94%A8.html#%E5%9F%BA%E4%BA%8EBusyBox%E7%9A%84initramfs%EF%BC%88%E4%BD%BF%E7%94%A8mkinitcpio%EF%BC%89%E6%9E%84%E5%BB%BA> "Dm-crypt/特殊应用"). 

  1. Install [mkinitcpio-netconf](<https://archlinux.org/packages/?name=mkinitcpio-netconf>)包 to provide hooks for setting up early user space networking.
  2. Choose an SSH server to use in early user space. The options are [mkinitcpio-tinyssh](<https://archlinux.org/packages/?name=mkinitcpio-tinyssh>)包 or [mkinitcpio-dropbear](<https://archlinux.org/packages/?name=mkinitcpio-dropbear>)包, and are mutually exclusive. 
     1. If using [mkinitcpio-tinyssh](<https://archlinux.org/packages/?name=mkinitcpio-tinyssh>)包, it is also recommended to install [tinyssh](<https://archlinux.org/packages/?name=tinyssh>)包 or [tinyssh-convert-git](<https://aur.archlinux.org/packages/tinyssh-convert-git/>)AUR. This tool converts an existing OpenSSH hostkey to the TinySSH key format, preserving the key fingerprint and avoiding connection warnings. The TinySSH and Dropbear mkinitcpio install scripts will automatically convert existing hostkeys when generating a new initcpio image.
  3. Decide whether to use an existing OpenSSH key or generate a new one (recommended) for the host that will be connecting to and unlocking the encrypted ZFS machine. Copy the public key into `/etc/tinyssh/root_key` or `/etc/dropbear/root_key`. When generating the initcpio image, this file will be added to `authorized_keys` for the root user and is only valid in the initrd environment.
  4. Add the `ip=` [内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数") to your boot loader configuration. The `ip` string is [highly configurable](<https://docs.kernel.org/admin-guide/nfs/nfsroot.html>). A simple DHCP example is shown below.
         
         ip=:::::eth0:dhcp

  5. Edit `/etc/mkinitcpio.conf` to include the `netconf`, `dropbear` or `tinyssh`, and `zfsencryptssh` hooks before the `zfs` hook:
         
         HOOKS=(... netconf <tinyssh>|<dropbear> zfsencryptssh zfs ...)

  6. [Regenerate the initramfs](<../zh-cn/Regenerate_the_initramfs.html> "Regenerate the initramfs").
  7. Reboot and try it out!

#### Changing the SSH server port

By default, [mkinitcpio-tinyssh](<https://archlinux.org/packages/?name=mkinitcpio-tinyssh>)包 and [mkinitcpio-dropbear](<https://archlinux.org/packages/?name=mkinitcpio-dropbear>)包 listen on port `22`. You may wish to change this. 

For **TinySSH** , copy `/usr/lib/initcpio/hooks/tinyssh` to `/etc/initcpio/hooks/tinyssh`, and find/modify the following line in the `run_hook()` function: 
    
    /etc/initcpio/hooks/tinyssh
    
    /usr/bin/tcpserver -HRDl0 0.0.0.0 <new_port> /usr/sbin/tinysshd -v /etc/tinyssh/sshkeydir &
    
For **Dropbear** , copy `/usr/lib/initcpio/hooks/dropbear` to `/etc/initcpio/hooks/dropbear`, and find/modify the following line in the `run_hook()` function: 
    
    /etc/initcpio/hooks/tinyssh
    
     /usr/sbin/dropbear -E -s -j -k -p <new_port>
    
[Regenerate the initramfs](<../zh-cn/Regenerate_the_initramfs.html> "Regenerate the initramfs"). 

####  Unlocking from a Windows machine using PuTTY/Plink

First, we need to use `puttygen.exe` to import and convert the OpenSSH key generated earlier into PuTTY's _.ppk_ private key format. We will call it `zfs_unlock.ppk` for this example. 

The mkinitcpio-netconf process above does not setup a shell (nor do we need need one). However, because there is no shell, PuTTY will immediately close after a successful connection. This can be disabled in the PuTTY SSH configuration (_Connection > SSH > [X] Do not start a shell or command at all_), but it still does not allow us to see stdout or enter the encryption passphrase. Instead, we use `plink.exe` with the following parameters: 
    
    plink.exe -ssh -l root -i c:\path\to\zfs_unlock.ppk <hostname>
    
The plink command can be put into a batch script for ease of use. 

### Enabling bclone support

To use `cp --reflink` and other commands needing bclone support, it is necessary to upgrade the _feature flags_ if coming from a version prior to 2.2.2. This will allow the pool to have support for bclone. This is done with `zpool upgrade`, if the status of the pool show this is possible. 

It is also required to enable a module parameter, otherwise userspace apps will not be able to use this feature. You can do this by putting this into `/etc/modprobe.d/zfs.conf`: 
    
    /etc/modprobe.d/zfs.conf
    
    options zfs zfs_bclone_enabled=1

Check that is working, and how much space is being saved with the command: `zpool get all POOLNAME | grep clon`

##  参考

  * [Aaron Toponce's 17-part blog on ZFS](<https://pthree.org/2012/12/04/zfs-administration-part-i-vdevs/>)
  * [OpenZFS releases](<https://zfsonlinux.org/>)
  * [OpenZFS FAQ](<https://openzfs.github.io/openzfs-docs/Project%20and%20Community/FAQ.html>)
  * [FreeBSD Handbook - The Z File System](<https://www.freebsd.org/doc/en_US.ISO8859-1/books/handbook/zfs.html>)
  * [Oracle Solaris ZFS Administration Guide](<https://docs.oracle.com/cd/E19253-01/819-5461/index.html>)
  * [ZFS Best Practices Guide](<https://web.archive.org/web/20161028084224/http://www.solarisinternals.com/wiki/index.php/ZFS_Best_Practices_Guide>)
  * [ZFS Troubleshooting Guide](<https://docs.oracle.com/cd/E23823_01/html/819-5461/gavwg.html>)
  * [How Pingdom uses ZFS to back up 5TB of MySQL data every day](<https://web.archive.org/web/20171213164254/http://royal.pingdom.com/2013/06/04/zfs-backup/>)
  * [Tutorial on adding the modules to a custom kernel](<https://www.linuxquestions.org/questions/linux-from-scratch-13/%5Bhow-to%5D-add-zfs-to-the-linux-kernel-4175514510/>)
  * [How to create cross platform ZFS disks under Linux](<https://github.com/danboid/creating-ZFS-disks-under-Linux>)
  * [How-To: Using ZFS Encryption at Rest in OpenZFS (ZFS on Linux, ZFS on FreeBSD, …)](<https://blog.heckel.xyz/2017/01/08/zfs-encryption-openzfs-zfs-on-linux/>)
  * [Archzfs iso download page: Frequently updated and downloadable archzfs linux iso with full OpenZFS support since 2016](<https://archzfs.leibelt.de/>)
