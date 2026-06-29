**翻译状态：**

  * 本文（或部分内容）译自 [Swap](<https://wiki.archlinux.org/title/Swap> "arch:Swap")，最近一次同步于 2025-04-10，若英文版本有所[更改](<https://wiki.archlinux.org/title/Swap?diff=0&oldid=826122>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Swap_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [fstab](<../zh-cn/Fstab.html> "Fstab")
  * [Hibernation](<../zh-cn/%E7%94%B5%E6%BA%90%E7%AE%A1%E7%90%86/%E6%8C%82%E8%B5%B7%E4%B8%8E%E4%BC%91%E7%9C%A0.html> "Hibernation")
  * [Zswap](<../zh-cn/Zswap.html> "Zswap")
  * [zram](<../zh-cn/Zram.html> "Zram")
  * [Swap on video ram](</wzh/index.php?title=Swap_on_video_ram&action=edit&redlink=1> "Swap on video ram（页面不存在）")
  * [ZFS#Swap volume](<../zh-cn/ZFS.html#Swap_volume> "ZFS")
  * [dm-crypt/交换分区加密](<../zh-cn/Dm-crypt/%E4%BA%A4%E6%8D%A2%E5%88%86%E5%8C%BA%E5%8A%A0%E5%AF%86.html> "Dm-crypt/交换分区加密")

swap也叫交换空间，是用于暂存暂时用不到内存页面的地方，以为更加常用的数据腾出更多空间。本文介绍了GNU/Linux上的[swap和分页](<https://en.wikipedia.org/wiki/Paging> "wikipedia:Paging")，教您如何创建和启用交换分区或交换文件。 

swap支持由Linux内核和来自 [util-linux](<https://archlinux.org/packages/?name=util-linux>)包 软件包的用户空间实用程序提供。 

## swap

swap可以是磁盘的一个分区，也可以是一个文件。用户可以在安装时或安装后的任何时候创建swap。swap有两种用途：第一，是暂存暂时用不到内存页面，将内存空间腾出给更常用的数据；第二，是用于 [suspend-to-disk](<../zh-cn/Power_management/Suspend_and_hibernate.html> "Power management/Suspend and hibernate") 支持。 

使用swap来暂时内存数据是否有好处取决于您的物理内存大小。如果物理内存非常充裕，通常有大量未使用空间的话，则根本用不到swap。如果物理内存非常不足，无法存下您当前正在使用的软件的活跃数据（“工作集”）的话，使用swap将导致频繁交换以至于系统运行缓存。而在以上两种极端情况之间，使用swap通常能够交换出不活跃的内存数据、将释放出来的空间用于I/O缓存或者活跃数据，将提升使用体验，或者让更多的软件可以放在后台驻留而不是为了腾出内存空间给当前程序使用而关闭。这对于某些占用内存很多、但又经常有大量不活跃数据的软件很有效，比如[网页浏览器](<../zh-cn/Category:%E7%BD%91%E9%A1%B5%E6%B5%8F%E8%A7%88%E5%99%A8.html> "Category:网页浏览器")和[Telegram](<../zh-cn/Telegram.html> "Telegram")。 

参见[《替swap辩护：常见的误解》](<https://farseerfc.me/in-defence-of-swap.html>)和[《关于swap的一些补充》](<https://farseerfc.me/followup-about-swap.html>)。 

**注意：** 连续的交换文件和交换分区之间没有性能之别，两者的处理方式是一样的。

要检查swap的状态，使用： 
    
    $ swapon --show
    
或者显示物理内存以及交换使用情况： 
    
    $ free -h
    
##  交换分区

[交换分区](<../zh-cn/%E5%88%86%E5%8C%BA.html#Swap> "Partitioning")可以用大多数 GNU/Linux [分区工具](<../zh-cn/%E5%88%86%E5%8C%BA.html> "Partitioning")创建。交换分区在 GPT 上的分区类型 GUID 为 `0657FD6D-A4AB-43C4-84E5-0933C84B4F4F`（[gdisk](<../zh-cn/GPT_fdisk.html> "Gdisk") 的 `8200` 类型，[fdisk](<../zh-cn/Fdisk.html> "Fdisk") 的 `swap` 类型），在 MBR 上的类型 ID 为 `82`。 

要将分区设置为 Linux 交换分区，请使用 [mkswap(8)](<https://man.archlinux.org/man/mkswap.8>) 命令。例如： 
    
    # mkswap /dev/sd _xy_
    
**警告：** 指定分区上的所有数据会丢失。

想要启用一个设备作为交换分区： 
    
    # swapon /dev/sd _xy_
    
参见 [swapon(8)](<https://man.archlinux.org/man/swapon.8>) 了解选项语法。 

###  启动时启用

要在启动时启用交换分区，可以： 

  * 使用 [systemd#GPT分区自动挂载](<../zh-cn/Systemd.html#GPT%E5%88%86%E5%8C%BA%E8%87%AA%E5%8A%A8%E6%8C%82%E8%BD%BD> "Systemd")
  * 或者添加一个条目到 `/etc/fstab`。例如：
        
        UUID=_device_UUID_ none swap defaults 0 0

    其中 `_device_UUID_` 是交换分区的 [UUID](<../zh-cn/%E5%9D%97%E8%AE%BE%E5%A4%87%E6%8C%81%E4%B9%85%E5%8C%96%E5%91%BD%E5%90%8D.html#%E9%80%9A%E8%BF%87_uuid> "UUID")。

参见 [fstab](<../zh-cn/Fstab.html> "Fstab") 了解文件语法，以及 [systemd#systemd.mount - mounting](<../zh-cn/Systemd.html#systemd.mount_-_mounting> "Systemd")。 

###  关闭交换分区

使用下面的命令关闭交换分区： 
    
    # swapoff /dev/sd _xy_
    
也可以使用 `-a` 参数来关闭所有的交换分区。 

因为 swap 通过 systemd 管理，因此会在下一次系统启动时再次激活。要永久禁用该特性，运行 `systemctl --type swap` 来查找 _.swap_ 单元，然后 [mask](</wzh/index.php?title=Mask&action=edit&redlink=1> "Mask（页面不存在）") 它。 

##  交换文件

相比于使用一个磁盘分区作为swap，使用交换文件可以更方便地随时调整大小或者移除。当磁盘空间有限（例如常规大小的SSD）时，使用交换文件更加理想。 

文件系统  | 是否支持交换文件   
---|---  
[Bcachefs](<../zh-cn/Bcachefs.html> "Bcachefs") |  [否](<https://github.com/koverstreet/bcachefs/issues/368>)  
[Btrfs](<../zh-cn/Btrfs.html> "Btrfs") |  [是](<../zh-cn/Btrfs.html#%E4%BA%A4%E6%8D%A2%E6%96%87%E4%BB%B6> "Btrfs")  
[F2FS](<../zh-cn/F2FS.html> "F2FS") | 是   
[ext4](<../zh-cn/Ext4.html> "Ext4") | 是   
[JFS](</wzh/index.php?title=JFS&action=edit&redlink=1> "JFS（页面不存在）") | 是   
[NILFS2](<https://en.wikipedia.org/wiki/NILFS> "wikipedia:NILFS") | 否   
[NTFS3](</wzh/index.php?title=NTFS3&action=edit&redlink=1> "NTFS3（页面不存在）") | 是   
[ReiserFS](<https://en.wikipedia.org/wiki/ReiserFS> "wikipedia:ReiserFS") | 是   
[XFS](<../zh-cn/XFS.html> "XFS") | 是   
[ZFS](<../zh-cn/ZFS.html> "ZFS") | 否   
  
###  建立交换文件

**注意：** 如果您使用[Btrfs](<../zh-cn/Btrfs.html> "Btrfs")，请先参阅 [Btrfs#交换文件](<../zh-cn/Btrfs.html#%E4%BA%A4%E6%8D%A2%E6%96%87%E4%BB%B6> "Btrfs")。

使用 [mkswap(8)](<https://man.archlinux.org/man/mkswap.8>) 创建一个由你自己指定大小的交换文件（参见 [Partitioning#Swap](<../zh-cn/%E5%88%86%E5%8C%BA.html#Swap> "Partitioning") 获取建议）。例如，创建一个 4 GiB 的交换文件： 
    
    # mkswap -U clear --size 4G --file /swapfile
    
启用交换文件： 
    
    # swapon /swapfile
    
最后，编辑 `/etc/fstab`，在为交换文件添加一个条目： 
    
    /etc/fstab
    
    /swapfile none swap defaults 0 0

有关更多信息，请参见 [fstab#Usage](<../zh-cn/Fstab.html#Usage> "Fstab"). 

**注意：** 交换文件必须由文件系统上的位置指定，而不是由UUID或标签指定。

###  删除交换文件

如果要删除一个交换文件，必须先停用它。 

作为root运行： 
    
    # swapoff /swapfile
    
然后即可删除它： 
    
    # rm -f /swapfile
    
最后从 `/etc/fstab` 中删除相关条目 

##  交换加密

查看 [dm-crypt/交换分区加密](<../zh-cn/Dm-crypt/%E4%BA%A4%E6%8D%A2%E5%88%86%E5%8C%BA%E5%8A%A0%E5%AF%86.html> "Dm-crypt/交换分区加密")。 

##  性能优化

交换操作通常比直接访问RAM中的数据慢得多。然而，完全禁用交换以提高性能有时会导致性能下降。如果没有足够的物理内存来容纳所有内容，完全不进行交换会减少文件系统缓存的可用内存，从而导致更频繁且代价高昂的磁盘使用。 

可以调整交换值以提高性能： 

### swappiness

当内存使用达到某个阈值时，内核会开始查看活动内存并尝试释放一些内容。文件数据可以写入文件系统（如果已更改），卸载并在稍后重新加载；其他数据必须先写入swap才能卸载。 

_swappiness_ [sysctl](<../zh-cn/Sysctl.html> "Sysctl") 参数代表了内核对于写入swap而不是文件的偏好。它的值可以是0到200之间（在Linux内核版本低于5.8时最大值为100），默认值为60。较低的值会导致内核更倾向于释放打开的文件，较高的值会导致内核尝试使用swap，而值100意味着IO成本被假定为相等。 

**注意：** 有一个常见的误解是swappiness会影响内存阈值或阻止使用交换空间，但它只影响释放文件页面而不是交换的偏好。有关更详细的解释，请参阅：[这篇文章](<https://www.howtogeek.com/449691/what-is-swapiness-on-linux-and-how-to-change-it/>) 或 [内核源代码](<https://github.com/torvalds/linux/blob/v6.2/mm/vmscan.c#L3000-L3014>) 中它的使用。

要查看当前交换值(Swappiness)，请执行以下操作： 
    
    $ sysctl vm.swappiness
    
此外，可以读取文件 `/proc/sys/vm/swappiness` 以获得原始整数值。 

要临时设置交换值(Swappiness)，请执行以下操作： 
    
    # sysctl -w vm.swappiness=35
    
要永久设置交换值，请创建[sysctl.d(5)](<https://man.archlinux.org/man/sysctl.d.5>)配置文件。例如： 
    
    /etc/sysctl.d/99-swappiness.conf
    
    vm.swappiness=35

为了让 [boot loader](<../zh-cn/Boot_loader.html> "Boot loader") 在加载内核时设置交换值，添加一个 [kernel parameter](<../zh-cn/Kernel_parameter.html> "Kernel parameter")，例如 `sysctl.vm.swappiness=35`. 

要测试和了解这可能起作用的原因，请查看[此文章](<https://rudd-o.com/en/linux-and-free-software/tales-from-responsivenessland-why-linux-feels-slow-and-how-to-fix-that>)。有关最近的反对意见，请参阅[这篇文章](<https://chrisdown.name/2018/01/02/in-defence-of-swap.html>)。 

###  VFS 缓存压力

`vm.vfs_cache_pressure` 是另外一个影响交换性能的 _sysctl_ 参数，这个参数控制内核回收 VFS 缓存的程度，增大数值会增加回收 VFS 缓存的频率[[1]](<https://web.archive.org/web/20171004100853/http://doc.opensuse.org/documentation/leap/tuning/html/book.sle.tuning/cha.tuning.memory.html#cha.tuning.memory.vm.reclaim>)。更多信息请阅读 [Linux kernel documentation](<https://docs.kernel.org/admin-guide/sysctl/vm.html>)。 

###  优先级

如果你有多个交换文件或交换分区，你应该考虑给它们各自分配一个优先级值(0 到 32767)。系统会优先使用较高优先级的交换区域，然后再使用较低优先级的交换区域。例如，如果你有一个较快的磁盘和一个较慢的磁盘，给较快的设备分配一个更高的优先级。优先级可以在 fstab 中通过 `pri` 参数指定： 
    
    UUID=f9fe0b69-a280-415d-a03a-a32752370dee none swap defaults,pri=100 0 0
    UUID=d7eb6062-01c8-4367-ac1d-3bf1167de8bb none swap defaults,pri=10  0 0
    
或者通过 swapon 的 `--priority` 参数： 
    
    # swapon --priority 100 /dev/sda1
    
如果两个或更多的区域有同样的优先级，并且它们都是可用的最高优先级，页面会按照循环的方式在它们之间分配。 

###  分片

不需要使用 [RAID](<../zh-cn/RAID.html> "RAID") 提高交换的性能，只要在 `/etc/fstab` 中给交换设备设置相同的优先级，内核会将交换分片到多个设备。详情请参考 [Software-RAID 指南](<https://unthought.net/Software-RAID.HOWTO/Software-RAID.HOWTO-2.html#ss2.3>)。 

###  丢弃（即 trim）

参见 [Solid state drive#swap](<../zh-cn/Solid_state_drive.html#swap> "Solid state drive")。 

###  在RAM中使用压缩块设备

参见 [Improving performance#zram or zswap](<../zh-cn/Improving_performance.html#zram_or_zswap> "Improving performance")。 

###  仅将swap用于休眠

如果你只需要swap作为休眠映像存储空间，那么你可以使用 [zswap](<../zh-cn/Zswap.html> "Zswap") 并禁用其回写，以便在常规交换使用中没有磁盘写入。参见 [Power management/Suspend and hibernate#Disable zswap writeback to use the swap space only for hibernation](<../zh-cn/Power_management/Suspend_and_hibernate.html#Disable_zswap_writeback_to_use_the_swap_space_only_for_hibernation> "Power management/Suspend and hibernate")。 

##  参见

  * [替swap辩护：常见的误解](<https://farseerfc.me/in-defence-of-swap.html>)
  * [关于swap的一些补充](<https://farseerfc.me/followup-about-swap.html>)
