**翻译状态：**

  * 本文（或部分内容）译自 [Zram](<https://wiki.archlinux.org/title/Zram> "arch:Zram")，最近一次同步于 2025-04-10，若英文版本有所[更改](<https://wiki.archlinux.org/title/Zram?diff=0&oldid=830794>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Zram_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Swap](<../zh-cn/Swap.html> "Swap")
  * [zswap](<../zh-cn/Zswap.html> "Zswap")

zram（原名 compcache）是 Linux 内核模块，在内存中创建压缩块设备，实现实时压缩的 [ramdisk](<https://en.wikipedia.org/wiki/RAM_drive> "w:RAM drive")。其主要用途为： 

  * 作 swap（最常见）
  * 作 /tmp 等临时文件存储

早期仅用于压缩 swap，故名 compcache。 

##  作为 swap 的使用

在最开始，创建出的 zram 块设备并不会预留或使用任何内存。仅当有文件需要被或者想要被交换出内存时，它们才会被压缩并移入 zram 块设备。因此，zram 块设备将会根据需要动态地增长或收缩。 

即使保守估计 zstd 只能达到 1:2 压缩比（实际中压缩比通常为 1:3），zram 也能提供在内存中存储比不进行内存压缩更多内容的优势。 

**注意：**

  * 在配置 zram 时设置的 zram 大小指代可存储的最大未压缩数据量， _不是_ 指压缩后的数据大小。只要内存中的压缩后数据量小于系统物理内存容量，你甚至可以将 zram 大小配置为等于或大于系统物理内存容量。
  * 假如相关的 [zswap](<../zh-cn/Zswap.html> "Zswap") 内核功能为启用状态，它将阻碍 zram 的有效使用。这是因为 zswap 会在 zram 之前被用作 swap 缓存，并在换出的内存分页到达 zram 前对其进行拦截和压缩。在这种情况下，尽管 [zramctl(8)](<https://man.archlinux.org/man/zramctl.8>) 的输出可能并非如此，实际上大部分 zram 并未被使用。因此，建议在开始前通过内核参数或者 sysfs 设置永久[禁用 zswap](<../zh-cn/Zswap.html#%E5%BC%80%E5%85%B3_zswap> "Zswap")。
  * 不支持在休眠时将内存换出至 zram，即便 zram 被配置在位于永久性存储的设备上。 _logind_ 会阻止休眠到配置在 zram 上的交换空间的尝试。

**提示：** 你可以通过 `mem_limit` 参数指定 ZRAM 可存储的最大压缩后数据量。

一开始可以先尝试配置大小为物理内存的一半。 

###  临时应用

参考如下配置一个采用 zstd 压缩、容量为系统内存大小一半，优先度较高且非持久的 zram 设备 (重启后失效)： 
    
    # modprobe zram
    # zramctl /dev/zram0 --algorithm zstd --size "$(($(grep -Po 'MemTotal:\s*\K\d+' /proc/meminfo)/2))KiB"
    # mkswap -U clear /dev/zram0
    # swapon --discard --priority 100 /dev/zram0
    
如需禁用，可以重启或执行以下命令： 
    
    # swapoff /dev/zram0
    # modprobe -r zram
    
关于每一步操作、配置选项及潜在问题的详细信息可以参考 [zram 模组的官方文档](<https://docs.kernel.org/admin-guide/blockdev/zram.html>)。 

若需一个持久化的解决方案，请在下述章节所述的方法中任选其一。 

###  使用 udev 规则

以下的案例描述了如何通过单个 udev 规则自动在启动时配置 zram 内 swap。该案例无需额外的软件包。 

显式地[在启动时加载模组](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html#%E8%87%AA%E5%8A%A8%E5%8A%A0%E8%BD%BD%E6%A8%A1%E5%9D%97> "内核模块")： 
    
    /etc/modules-load.d/zram.conf
    
    zram
    
创建如下的 [udev 规则](<../zh-cn/Udev.html#udev_%E8%A7%84%E5%88%99> "Udev")（请按需调整 `disksize` 属性）： 
    
    /etc/udev/rules.d/99-zram.rules
    
    ACTION=="add", KERNEL=="zram0", ATTR{initstate}=="0", ATTR{comp_algorithm}="zstd", ATTR{disksize}="4G", RUN="/usr/bin/mkswap -U clear %N", TAG+="systemd"

将 `/dev/zram` 以一个高于默认值的优先度添加到您的 [fstab](<../zh-cn/Fstab.html> "Fstab")： 
    
    /etc/fstab
    
    /dev/zram0 none swap defaults,discard,pri=100 0 0

###  使用 zram-generator

[zram-generator](<https://archlinux.org/packages/?name=zram-generator>)包 提供了 `systemd-zram-setup@zram _N_.service` 单元，可自动初始化 zram 设备而无需用户[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用")相关模板或实例。详见 [zram-generator(8)](<https://man.archlinux.org/man/zram-generator.8>)。 

如要使用，只需[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [zram-generator](<https://archlinux.org/packages/?name=zram-generator>)包，并创建包含如下内容的 `/etc/systemd/zram-generator.conf` 配置文件： 
    
    /etc/systemd/zram-generator.conf
    
    [zram0]
    zram-size = min(ram / 2, 4096)
    compression-algorithm = zstd

`zram-size` 是 zram 设备的大小，单位为 `MiB`，你可以使用 `ram` 指代总内存容量。 

`compression-algorithm` 指定了 zram 设备使用的压缩算法。执行 `cat /sys/block/zram0/comp_algorithm` 将显示所有可用的压缩算法（包括当前选用的算法）。 

详细信息请参考 [zram-generator.conf(5)](<https://man.archlinux.org/man/zram-generator.conf.5>)。 

然后执行 [daemon-reload](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Daemon-reload")，并[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")你配置的 `systemd-zram-setup@zram _N_.service` 示例（` _N_` 需要与实例编号匹配，该示例中为 `systemd-zram-setup@zram0.service`） 。 

您可使用 [zramctl(8)](<https://man.archlinux.org/man/zramctl.8>) 或 [swapon(8)](<https://man.archlinux.org/man/swapon.8>)，或是通过查阅 `systemd-zram-setup@zram _N_.service` 实例的[单元状态](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "单元状态")，来检查您所配置的 `/dev/zram _N_` 设备的 [swap 状态](<../zh-cn/Swap.html#%E4%BA%A4%E6%8D%A2%E7%A9%BA%E9%97%B4> "Swap")。 

###  使用 zramswap

[zramswap](<https://aur.archlinux.org/packages/zramswap/>)AUR 提供一个自动化脚本，可配置一个优先度较高、默认为 20% 系统内存容量的 swap。如需让其自动在启动时执行，请[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `zramswap.service`。 

##  提示与技巧

###  查看 zram 状态

使用 [zramctl(8)](<https://man.archlinux.org/man/zramctl.8>)。示例： 
    
    $ zramctl
    
    NAME       ALGORITHM DISKSIZE  DATA  COMPR  TOTAL STREAMS MOUNTPOINT
    /dev/zram0 zstd           32G  1.9G 318.6M 424.9M      16 [SWAP]
    
  * DISKSIZE = 32G: 该 zram 设备最多会存储 32 GiB 的未压缩数据
  * DATA = 1.9G: 目前, 该 zram 设备上存储着 1.9 GiB (未被压缩的) 数据
  * COMPR = 318.6M: 这 1.9 GiB 未被压缩的数据被压缩到了 318.6 MiB
  * TOTAL = 424.9M: 包含元信息在内，这 1.9 GiB 未压缩的数据使用了 424.9 MiB 的物理内存

###  多个 zram 设备

初始情况下，加载 `zram` 模块会创建一个 `/dev/zram0` 设备。 

如果您需要更多的 `/dev/zram` 设备，使用 `num_devices` [内核模块参数](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html#%E9%85%8D%E7%BD%AE%E6%A8%A1%E5%9D%97%E5%8F%82%E6%95%B0> "内核模块")指定设备的量，或[在之后按需添加它们](<https://docs.kernel.org/admin-guide/blockdev/zram.html#add-remove-zram-devices>)。 

###  优化 zram 上的 swap

介于 zram 与磁盘 swap 的行为不同，可以配置系统的 swap 以充分利用 zram 的优势： 
    
    /etc/sysctl.d/99-vm-zram-parameters.conf
    
    vm.swappiness = 180
    vm.watermark_boost_factor = 0
    vm.watermark_scale_factor = 125
    vm.page-cluster = 0

该配置的解释： 

这些值与[Pop!_OS 中使用的值](<https://github.com/pop-os/default-settings/pull/163>)相同。这条 GitHub 上 Pop!_OS 的 pull request 同时链接到了[r/Fedora 上一些用户所进行的测试](<https://old.reddit.com/r/Fedora/comments/mzun99/new_zram_tuning_benchmarks/>)，结果显示 `vm.page-cluster = 0` 是较为合适的值。此外，他们也发现建议使用较高的 swappniess，这与[内核文档](<https://docs.kernel.org/admin-guide/sysctl/vm.html>)中的建议相符。 

默认情况下该值为 60。 

    对于像 zram 或 zswap 这样在内存中的 swap，以及一些混合式的、在相较文件系统来说更为快速的设备上 swap 的配置，应当考虑 100 以上的值。例如，若 swap 设备上的随机读写平均快于文件系统上随机读写的 2 倍，则 swappiness 值应为 133 (x + 2x = 200, 2x = 133.33)。

在配备硬盘驱动器的系统上，在内存设备上的随机读写会比在文件系统上的读写快若干数量级，因此 swappiness 应为 200 左右。甚至是在配备高速固态硬盘的系统上，较高的 swappiness 值也是理想的。 

###  为 zram 块设备启用后备设备

可以配置 zram 将未压缩内存页放入指定的块设备中。 

如要手动添加后备设备： 
    
    # echo /dev/_sdX_ > /sys/block/zram0/backing_dev
    
如要通过 _zram-generator_ 为 zram 块设备添加后备设备，可在 `/etc/systemd/zram-generator.conf` 中对应的 `[zram _X_]` 设备下添加如下内容： 
    
    /etc/systemd/zram-generator.conf
    
    writeback-device=/dev/disk/by-partuuid/_XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX_

然后可以通过执行以下命令将未压缩的页面推送到块设备： 
    
    # echo huge > /sys/block/zramX/writeback
    
###  将 zram 用于非 swap 用途

zram 也可以被用作普通的内存块设备，像是占用较少物理内存，但性能略微下降的 `/dev/ram` 设备。然而，有几个问题需要注意： 

  * 无分区表支持（不会自动创建 `/dev/zram _x_ p _y_`）。
  * 块大小固定为 4 kiB。

显然，可以通过在 zram 上叠加回环设备来绕过这一问题。使用 _losetup_ ，可以使用 `-b` 参数指定块大小，使用 `-P` 参数处理分区表并自动创建分区回环设备。 
    
    # zramctl -f -s _N_ G
    
    /dev/zram _x_

将磁盘镜像复制到新创建的 `/dev/zram _x_`，然后创建回环设备。如果磁盘镜像有分区表，回环设备的块大小必须与分区表使用的块大小匹配，通常为 512 或 4096 字节。 
    
    # losetup -f -b 512 -P /dev/zram _x_
    
    # ls /dev/loop*
    
    /dev/loop0 /dev/loop0p1 /dev/loop0p2
    
    # mount /dev/loop0p1 /mnt/boot
    # mount /dev/loop0p2 /mnt/root
    
**注意：**

  * zram 设备编号取决于已有的 zram 设备，其大小应足以存放磁盘镜像。
  * `ls /dev/loop*` 的输出结果取决于磁盘镜像中的内容。

##  另请参阅

  * [Wikipedia:zram](<https://en.wikipedia.org/wiki/zram> "wikipedia:zram")
  * <https://github.com/pop-os/default-settings/pull/163>
  * <https://www.reddit.com/r/pop_os/comments/znh9n6/help_test_a_zram_optimization_for_pop_os/>
