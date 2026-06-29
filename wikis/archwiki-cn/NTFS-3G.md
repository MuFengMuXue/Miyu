**翻译状态：**

  * 本文（或部分内容）译自 [NTFS-3G](<https://wiki.archlinux.org/title/NTFS-3G> "arch:NTFS-3G")，最近一次同步于 2019-10-06，若英文版本有所[更改](<https://wiki.archlinux.org/title/NTFS-3G?diff=0&oldid=573885>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/NTFS-3G_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [File systems](<../zh-cn/File_systems.html> "File systems")
  * [NTFS](<../zh-cn/NTFS.html> "NTFS")

[NTFS-3G](<https://github.com/tuxera/ntfs-3g>) 是[微软 NTFS](<https://en.wikipedia.org/wiki/NTFS> "wikipedia:NTFS") 的一个开源实现，同时支持读**和** 写。NTFS-3G 开发者使用 FUSE 文件系统辅助开发并帮助实现可移植性。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [ntfs-3g](<https://archlinux.org/packages/?name=ntfs-3g>)包 软件包。 

##  手动挂载

有两种手动挂载 NTFS 分区的方法。传统方法是： 
    
    # mount /dev/_你的_NTFS_分区_ _/mount/point_
    
在 Arch 中不需要显式指定挂载类型 `ntfs-3g`。 _mount_ 命令默认会使用 `/usr/bin/mount.ntfs`（在安装了 ntfs-3g 软件包之后被符号连接到 `/usr/bin/ntfs-3g`）。 

第二种方法是直接调用 `ntfs-3g`： 
    
    # ntfs-3g /dev/_你的_NTFS_分区_ _/mount/point_
    
可用选项参见 [ntfs-3g(8)](<https://man.archlinux.org/man/ntfs-3g.8>)。 

##  格式化

**警告：** 与往常一样，仔细检查设备路径。
    
    # mkfs.ntfs -Q -L 卷标 /dev/sd _XY_
    
**注意：**`-Q` 通过不向驱动器填充零且不检查坏扇区来加速格式化。

##  配置

你的 NTFS 分区可以被配置成自动挂载，或者预先配置好来安装你想要的方式挂载。配置可以在文件系统配置文件 [fstab](<../zh-cn/Fstab.html> "Fstab") 中指定或者使用 udev 规则。 

###  默认配置

使用默认配置会在启动时挂载 NTFS 分区。使用这种方法，如果挂载位置的父文件夹有合适的用户或组[权限](<../zh-cn/Users_and_groups.html> "Users and groups")，用户或组就可以读写这个分区。 

把以下内容写入`/etc/fstab`: 
    
    # <file system>  <dir>  <type>  <options>  <dump>  <pass>
    /dev/_NTFS-part_  /mnt/windows  ntfs-3g   defaults		  0       0
    
###  Linux权限兼容

Linux系统通常将目录的权限设为755，将文件的权限设为644。如果您经常使用NTFS分区，建议保留这些权限。下面的示例将上述权限分配给普通用户： 
    
    # 安装具有 linux 兼容权限的内部 Windows 分区，即权限755用于目录（dmask=022）和权限644用于文件（fmask=133）
    /dev/_NTFS-partition_  /mnt/windows  ntfs-3g uid=_username_ ,gid=users,dmask=022,fmask=133 0 0
    
或者，如果Windows上的权限对你很重要，你可以使用 [ntfsusermap(8)](<https://man.archlinux.org/man/ntfsusermap.8>) 命令将 Windows 用户 映射到 Linux 用户上。ntfs-3g将会处理权限的翻译。 

###  允许组/用户

在`/etc/fstab`中，您还可以指定其他选项，如允许访问（读取）分区的用户。例如，您允许`users`组中的人员具有访问权限： 
    
    /dev/_NTFS-partition_  /mnt/windows  ntfs-3g   gid=users,umask=0022    0       0
    
默认情况下, 上述命令仅为root用户启用写支持。若要为其他用户启用，必须显示指定应授予写入权限的用户。使用`uid`参数加您的用户名以启用用户写支持： 
    
    /dev/_NTFS-partition_  /mnt/windows  ntfs-3g   uid=_username_ ,gid=_groupid_ ,umask=0022    0       0
    
如果您在一个单用户计算机上运行，您可能希望自己拥有该文件系统并授予所有可能的权限： 
    
    /dev/_NTFS-partition_  /mnt/windows  ntfs-3g   uid=_username_ ,gid=_groupid_    0       0
    
###  基本的 ntfs-3g 选项

对大多数人来说，上面的设置已经足够了。这是一些其他的对于不同的Linux文件系统的通用选项。完整列表参见[ntfs-3g(8) § OPTIONS](<https://man.archlinux.org/man/ntfs-3g.8#OPTIONS>)

[umask](<../zh-cn/Umask.html> "Umask")
    umask 是一个嵌入的 shell 命令，可以自动设置新创建的文件的权限。对于 Arch Linux，对于 root 和 user 默认的 umask 是 0022。设为 0022 将使新目录有目录权限755，新文件有权限644。你可以在[这里](<https://www.cyberciti.biz/tips/understanding-linux-unix-umask-value-usage.html>)查看更多关于 umask 权限的信息：。
noauto
    如果设置了 `noauto`，`/etc/fstab` 中的 NTFS 条目不会在启动时自动挂载。
uid
    用户 id 号码。这允许指定用户具有完全的访问权限。你的uid可以用 `id` 命令获得。
fmask and dmask
    与 `umask` 类似但是分别定义的是文件和目录的权限。

下面的选项只对ntfs-3g有用： 

windows_names
    阻止创建拥有不被Windows允许的名字的文件、目录以及扩展属性的。

###  允许用户挂载

默认情况下，如果 _ntfs-3g_ 在挂载一个[块设备](<../zh-cn/Block_device.html> "Block device")， _ntfs-3g_ 需要 root 权限运行, 即使在`/etc/fstab`中有`user`选项。有关详细信息，请参阅 [ntfs-3g-faq](<https://github.com/tuxera/ntfs-3g/wiki/NTFS-3G-FAQ>)。即使在fstab里面有了`user`选项，ntfs-3g仍然需要root权限。 

**注意：**

  * [ntfs-3g](<https://archlinux.org/packages/?name=ntfs-3g>)包包没有内置FUSE支持。使用[ABS](<../zh-cn/Arch_%E6%9E%84%E5%BB%BA%E7%B3%BB%E7%BB%9F.html> "ABS")重新构建包以启用FUSE支持。 
    * 完整的解释是， "user" and "users" work via a setuid `mount` not dropping its setuid privilege so that the block device can be used without root. However, ntfs-3g has a hard-coded restriction in ntfs-3g that bails on setuid if an external libfuse is used.
    * 并没有好的技术原因 for not allowing setuid for external FUSE besides a mistrust of the library. [This patch](<https://github.com/AOSC-Dev/ntfs-3g/commit/c918fb79f9f340bce1a19dacf4b720d19922450d>) removes the said restriction.
  * 卸载权限似乎存在问题，因此如果需要卸载文件系统，则仍需要 root 权限。您还可以使用`fusermount -u /mnt/_mountpoint_`来卸载文件系统并避免使用root权限。此外, 如果在`/etc/fstab`中使用` _users_`（复数）而不是`user`选项，您可以使用`mount`和`umount`命令装卸载文件系统。

对于非块设备，比如普通的镜像，命令行下的 _ntfs-3g_ 应该可以在普通用户权限下照常使用，因为当无法与内核直接交互时，the underlying FUSE calls 会重定向到 setuid-root _fusermount_ 。 

##  调整NTFS分区大小

**注意：** 对重要数据请提前做好备份！

大多数已购买的系统已经有[Windows](<https://en.wikipedia.org/wiki/Windows> "wikipedia:Windows")安装在其上，有些人希望在进行 Arch Linux 安装时不要完全擦除它。因此，在某些方面，调整现有 Windows 分区的大小以为 Linux 分区腾出空间是很有用的。这经常通过[Live CD](<https://en.wikipedia.org/wiki/Live_CD> "wikipedia:Live CD")或可引导的USB闪存驱动器完成。 

对于Live CD，典型的创建过程是下载ISO文件，刻录到CD，然后从它启动。[InfraRecorder](<http://infrarecorder.org/>)是一个免费（通过GPL3）的Windows上的CD/DVD刻录应用程序，这是很合适的方法。如果您想要使用可引导的USB驱动器，请参阅[USB flash installation media](<../zh-cn/USB_flash_installation_media.html> "USB flash installation media")中创建可引导的USB驱动器的方法。 

有许多可引导的CD/USB映像可用。此列表不是详尽无遗的, 但是是个很好的开始： 

  * **[GParted](<https://en.wikipedia.org/wiki/GParted> "wikipedia:GParted")** — 为x86计算机设计的小型GNU/Linux发行版。允许你使用最新版GParted应用的所有功能。不包括额外的软件包System Rescue CD，并且磁盘加密可能不受支持。

     <http://gparted.sourceforge.net/> || [gparted](<https://archlinux.org/packages/?name=gparted>)包

  * **[Parted Magic](<https://en.wikipedia.org/wiki/Parted_Magic> "wikipedia:Parted Magic")** — [gparted](<https://archlinux.org/packages/?name=gparted>)包。使用分区编辑器可以调整大小、复制和移动分区。您可以增长或收缩您的 C: 驱动器，为新操作系统创建空间。尝试从丢失的分区中进行数据抢救。

     <https://partedmagic.com/> ||

请注意, 调整 NTFS 分区大小的重要程序包括 ntfs-3g 和类似于 (G)parted 或 fdisk 的实用程序，由[util-linux](<https://archlinux.org/packages/?name=util-linux>)包包提供。除非您是高级用户，否则最好使用像 GParted 这样的工具来执行任何调整大小操作，以尽量减少由于用户错误而导致数据丢失的可能性。 

如果您的系统上已经安装了 Arch Linux，并且只想调整现有 NTFS 分区的大小，则可以使用 parted 和 ntfs-3g 包来完成。或者，在安装 [GParted](<../zh-cn/Parted.html> "GParted") 包后, 可以使用 GParted GUI，其本质是调用 [ntfsresize(8)](<https://man.archlinux.org/man/ntfsresize.8>) 命令 

##  疑难解答

###  已压缩的文件

若您在挂载一个Windows 10的NTFS文件系统，并且读取其中的文件和文件夹时出现以下情形： 

  1. 出现链接到“不支持的重解析点”（unsupported reparse point）的损坏的符号链接，或
  2. 出现错误信息：`cannot access _some_file_ : Input/output error` （此时`Could not load plugin /usr/lib64/ntfs-3g/ntfs-plugin-80000017.so: Success`在[日志](<../zh-cn/Systemd/Journal.html> "Journal")中)

其原因是NTFS-3G默认不支持某些类型的[重解析点](<https://en.wikipedia.org/wiki/NTFS_reparse_point> "wikipedia:NTFS reparse point")。一些插件可用于部分特性的兼容性，如： 

  * 系统压缩
  * 文件去重
  * OneDrive文件

[点击此处](<https://jp-andre.pagesperso-orange.fr/junctions.html#other>)查看更多细节。 

系统压缩可以压缩特定的文件。目前由两种可能的解决方案。 

你可以安装ntfg-3g的 ntfs-3g-system-compressionAUR 插件. 目前插件只支持读取，并不支持写入，例如创建文件便不被支持。 

或者，在Windows 10内禁用压缩： 
    
    C:\WINDOWS\system32> compact.exe /CompactOS:never
    
###  损坏的NTFS文件系统

如果NTFS文件系统有错，ntfs-3g会以只读方式挂载它。要修复NTFS系统，启动Windows并使用它的磁盘检查程序，chkdsk。考虑到 ntfsfix 只能修复一些错误，如果失败，chkdsk 可能会成功。 

想要修复 NTFS 文件系统，该设备必须已经被卸载。例如，想要修复 `/dev/sda2` 中的 NTFS 文件系统： 
    
    # umount /dev/sda2
    # ntfsfix /dev/sda2
    Mounting volume... OK
    Processing of $MFT and $MFTMirr completed successfully.
    NTFS volume version is 3.1.
    NTFS partition /dev/sda2 was processed successfully.
    # mount /dev/sda2
    
如果顺利的话，该分区已经可以写入了。 

###  WIndows分区下的中文文件乱码

见[简体中文本地化#Windows 分区下的中文文件名乱码](<../zh-cn/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87%E6%9C%AC%E5%9C%B0%E5%8C%96.html#Windows_%E5%88%86%E5%8C%BA%E4%B8%8B%E7%9A%84%E4%B8%AD%E6%96%87%E6%96%87%E4%BB%B6%E5%90%8D%E4%B9%B1%E7%A0%81> "简体中文本地化")

###  元数据保存在Windows中，拒绝挂载

当与 Windows 8 或 10双引导时,试图挂载一个可见的Windows可能会出现如下错误: 
    
    The disk contains an unclean file system (0, 0).
    Metadata kept in Windows cache, refused to mount.
    Failed to mount '/dev/sdc1': Operation not permitted
    The NTFS partition is in an unsafe state. Please resume and shutdown
    Windows fully (no hibernation or fast restarting), or mount the volume
    read-only with the 'ro' mount option.
    
问题是因为Windows 8中引入"快速启动"特性。启用快速启动后，所有分区的元数据的一部分被还原到它们在以前关闭的状态。因此，在 Linux 上所做的更改可能会丢失。这会发生在任何选择"关闭"或"休眠" NTFS 分区的Windows 8 或 10 下。然而，通过选择"重新启动"关闭 Windows 是安全的。 

要启用对其他操作系统的系统分区写入，请确保禁用快速重启。通过以管理员身份执行命令: 
    
    powercfg /h off
    
你可以在 _控制面板 >硬件与声音> 电源选项 > 系统设置 > 当电源键按下时做什么_， 去掉勾选 _启用快速启动_

###  删除Windows休眠元数据

作为一个以上干净关机方法的替代方法，有一个办法可以彻底删除休眠后保存的 NTFS 元数据。这个方法只适用于当你不能或不想启动至 Windows，并希望它完全关闭。这个办法是在使用 [ntfs-3g](<https://archlinux.org/packages/?name=ntfs-3g>)包 提供的 _ntfsfix_ 。 
    
    # ntfsfix /dev/_你的NTFS分区_
    
**警告：** 这个方法意味着已保存的 Windows 会话将彻底丢失。使用该选项后果自负。

###  挂载失败

如果你按本指南内容操作也无法挂载你的 NTFS 分区，可以尝试一下在 `fstab` 中的所有 ntfs 分区里加上 [UUID](<../zh-cn/%E5%9D%97%E8%AE%BE%E5%A4%87%E6%8C%81%E4%B9%85%E5%8C%96%E5%91%BD%E5%90%8D.html#%E9%80%9A%E8%BF%87_uuid> "UUID")。参见[示例](<../zh-cn/Fstab.html#%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F_UUID> "Fstab"). 

### Windows mount failure

Windows 不会识别一个没有相应的分区类型的NTFS分区。创建一个与 Windows 共用的NTFS分区时的常见陷阱就是忘记设置分区类型为 NTFS。 见 [fdisk](<../zh-cn/Fdisk.html> "Fdisk") 或者[分区工具](<../zh-cn/%E5%88%86%E5%8C%BA.html#%E5%88%86%E5%8C%BA%E5%B7%A5%E5%85%B7> "分区")。 

##  测试版特性 & 发布

有一个关于“高级特性”的网页，由 Jean-Pierre André ，NTFS-3G的作者之一维护。它提供了: 

  * 关于在 NTFS-3G 中处理一些 NTFS 特性的文档，包括： 
    * 符号链接，连接点，和一些其他的重解析点。
    * 扩展属性 (xattrs) as an interface for ADS streams and special NTFS attributes
    * 安全和权限，包括 POSIX 映射和 ACL 映射。
  * 用于解析特殊重解析点的插件。 文档中提供的信息也适用于 Tuxera 版本 (2017.3.23)。系统压缩插件和去重插件也适用于 Tuxera 版本，但 OneDrive 插件需要需要一些只在高级发布版可用的调整项。 当然，这个网页目前由 J.-P. André撰写。[一个旧版的网页](<https://www.tuxera.com/community/ntfs-3g-advanced/>)可在 tuxera.com被找到；它链接到 OpenIndiana 的页面， 又链接到 J.-P. André 的网。

##  参见

  * [ntfs-3g(8)](<https://man.archlinux.org/man/ntfs-3g.8>)
