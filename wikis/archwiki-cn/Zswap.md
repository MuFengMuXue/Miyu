相关文章

  * [内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")
  * [Mkinitcpio](<../zh-cn/Mkinitcpio.html> "Mkinitcpio")

**翻译状态：**

  * 本文（或部分内容）译自 [zswap](<https://wiki.archlinux.org/title/zswap> "arch:zswap")，最近一次同步于 2023-3-24，若英文版本有所[更改](<https://wiki.archlinux.org/title/zswap?diff=0&oldid=772217>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/zswap_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[zswap](<https://en.wikipedia.org/wiki/zswap> "wikipedia:zswap") 是一个内核功能，它为交换页提供了一个压缩的内存缓存。原本会交换到磁盘的页被压缩并存储到内存中的存储池中。一旦池已满或内存耗尽，最近最少使用的（[LRU](<https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_.28LRU.29> "wikipedia:Cache replacement policies")）页就会被解压缩并写入磁盘，就好像它没有被拦截一样。将页解压缩到交换缓存后，可以释放池中的压缩版本。 

与 [zram](<../zh-cn/Zram.html> "Zram") 相比的区别在于，zswap 与 [swap](<../zh-cn/Swap.html> "Swap") 设备协同工作，而 _zram_ 是内存中的交换设备，不需要后备交换设备。 

##  开关 zswap

在稳定版（stable）的 [linux](<https://archlinux.org/packages/?name=linux>)包 官方内核中，zswap 会被默认启用。这可以通过[稳定版内核配置](<https://github.com/archlinux/svntogit-packages/blob/packages/linux/trunk/config>)中的 `CONFIG_ZSWAP_DEFAULT_ON` 标志进行验证。 

要在运行时禁用 zswap，请执行下面的命令： 
    
    # echo 0 > /sys/module/zswap/parameters/enabled
    
要永久禁用 zswap，添加 `zswap.enabled=0` 到你的[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")。 

##  定制 zswap

###  当前参数

zswap 有几个可自定义的参数。可以使用以下方式显示实时设置： 
    
    $ grep -R . /sys/module/zswap/parameters
    
    /sys/module/zswap/parameters/same_filled_pages_enabled:Y
    /sys/module/zswap/parameters/enabled:Y
    /sys/module/zswap/parameters/max_pool_percent:20
    /sys/module/zswap/parameters/compressor:lz4
    /sys/module/zswap/parameters/zpool:z3fold
    /sys/module/zswap/parameters/accept_threshold_percent:90
    
见 [zswap 文档](<https://docs.kernel.org/admin-guide/mm/zswap.html>)获取不同参数的描述。 

显示初始配置的引导时加载消息可以通过以下方式检索： 
    
    # dmesg | grep zswap:
    
    [    0.317569] zswap: loaded using pool lz4/z3fold
    
###  设定参数

####  使用 sysfs

每个设置都可以在运行时通过 [sysfs](<https://en.wikipedia.org/wiki/sysfs> "wikipedia:sysfs") 接口进行更改。作为示例，要更改 `compressor` 参数： 
    
    # echo lz4 > /sys/module/zswap/parameters/compressor
    
####  使用内核引导参数

要持久化参数更改，必须在内核引导参数中添加相应的选项，例如 `zswap.compressor=lz4`。因此，要永久设定上述所有设置，必须添加以下[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")： 
    
    zswap.enabled=1 zswap.compressor=lz4 zswap.max_pool_percent=20 zswap.zpool=z3fold
    
当通过引导参数更改压缩算法时，需要确保在引导期间尽早加载相应的压缩模块（参考 [#压缩算法](<#%E5%8E%8B%E7%BC%A9%E7%AE%97%E6%B3%95>)）。 

###  最大池大小

存储池不是预先分配的，它可以增长到可用内存总量的一定百分比，默认情况下最多占内存总量的20%。一旦达到此阈值，就会将页从池中逐出到交换设备中。压缩池的最大大小由参数 `max_pool_percent` 控制。 

###  压缩存储池分配器

_zpool_ 参数控制压缩存储池的管理。 

在 6.3 版本后的内核中，添加了 [zsmalloc](<https://docs.kernel.org/mm/zsmalloc.html>) 分配器。它在低内存条件下表现良好，并且可以节省更多内存。 

对于较旧的内核，可以使用 zbud 数据分配器，它将恰好两个压缩页面存储到一个中，这将压缩比限制为 2 或更低。 

同样， [z3fold](<https://docs.kernel.org/mm/z3fold.html>) 分配器允许每页最多 3 个压缩对象（与 zbud 的 1.7 相比，典型的压缩比平均约为 2.7）。该分配器以前被建议优于 zsmalloc，因为它具有更好的性能，但由于这一点不再成立且存在众多错误，自 6.13 起已被弃用并默认禁用（在 6.6.55 中回移植到 6.6 LTS），并计划移除。 

默认情况下会创建一个类型为 zsmalloc 的 zpool。使用内核参数 `zswap.zpool` 可以在启动时选择其他分配器。数据分配器也可以在后期通过 sysfs 接口进行更改。 

###  压缩算法

对于页的压缩，zswap 使用内核加密 API 提供的压缩器模块。默认情况下会使用 _lz4_ 压缩算法，但也可以在启动时使用 `zswap.compressor` 更改压缩算法。其他选项包括 _deflate_ , _lz4hc_ , _lzo_ , _lzo-rle_ , _842_ 和 _zstd_ 。 

使用 _sysfs_ 在运行时更改压缩不会有问题，但在本例中，zswap 从 _lz4_ 开始，并在稍后阶段切换到定义的算法。要立即使用另一种算法启动 zswap，必须通过内核引导参数进行设定，并且内核必须尽早加载相应的模块。这可以通过以下步骤来实现： 

  1. 将与所选压缩器相关的模块添加到 [mkinitcpio#模块（MODULES）](<../zh-cn/Mkinitcpio.html#%E6%A8%A1%E5%9D%97%EF%BC%88MODULES%EF%BC%89> "Mkinitcpio")数组中。
  2. 修改 mkinitcpio 配置后重新生成 ramdisk 环境：见 [mkinitcpio#创建和启用镜像](<../zh-cn/Mkinitcpio.html#%E5%88%9B%E5%BB%BA%E5%92%8C%E5%90%AF%E7%94%A8%E9%95%9C%E5%83%8F> "Mkinitcpio")。
  3. 在[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")中将 `zswap.compressor` 设定为你选择的算法。

在下次启动时，见 [#当前参数](<#%E5%BD%93%E5%89%8D%E5%8F%82%E6%95%B0>)来检查 zswap 现在是否使用了请求的压缩器。 

##  另见

  * [zswap：如何确定是否压缩交换页？](<https://lore.kernel.org/lkml/1674223.HVFdAhB7u5@merkaba/>)。
  * [IBM 支持文章“新的 Linux zswap 压缩功能”（基准图像不加载）](<https://www.ibm.com/support/pages/new-linux-zswap-compression-functionality>)。
  * [Ask Ubuntu: zram vs. zswap vs. zcache](<https://askubuntu.com/questions/471912/zram-vs-zswap-vs-zcache-ultimate-guide-when-to-use-which-one>)。
  * [Arch Linux 论坛讨论串](<https://bbs.archlinux.org/viewtopic.php?id=169585>)。
  * [由 zswap 的主要开发者撰写的 LWN.net 技术文章](<https://lwn.net/Articles/537422/>)。
