相关文章

  * [安全地擦除磁盘#hdparm](<../zh-cn/%E5%AE%89%E5%85%A8%E5%9C%B0%E6%93%A6%E9%99%A4%E7%A3%81%E7%9B%98.html#hdparm> "安全地擦除磁盘")

**翻译状态：**

  * 本文（或部分内容）译自 [︁Hdparm](<https://wiki.archlinux.org/title/%EF%B8%81Hdparm> "arch:︁Hdparm")，最近一次同步于 2025-02-04，若英文版本有所[更改](<https://wiki.archlinux.org/title/%EF%B8%81Hdparm?diff=0&oldid=802353>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/%EF%B8%81Hdparm_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

_hdparm_ 和 _sdparm_ 是用于设置和查看[硬盘](<https://zh.wikipedia.org/wiki/%E7%A1%AC%E7%9B%98> "zhwp:硬盘")参数的命令行实用程序。 _hdparm_ 也可以用作简单的[基准测试](<../zh-cn/%E5%9F%BA%E5%87%86%E6%B5%8B%E8%AF%95.html> "基准测试")工具。 

最初 _hdparm_ 被设计用于 [IDE](<https://en.wikipedia.org/wiki/Parallel_ATA#IDE_and_ATA-1> "wikipedia:Parallel ATA") 硬盘，而 _sdparm_ 对应的是 [SCSI](<https://zh.wikipedia.org/wiki/%E5%B0%8F%E5%9E%8B%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%B3%BB%E7%BB%9F%E6%8E%A5%E5%8F%A3> "zhwp:小型计算机系统接口") 硬盘。大约从 2010 年开始，存储设备接口变成了 IDE 和 SCSI 的增强组合， _hdparm_ 和 _sdparm_ 在功能上也形成互补。 

**警告：** 更改磁盘的默认参数可能会导致系统冻结甚至对磁盘造成不可逆转的损坏。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [hdparm](<https://archlinux.org/packages/?name=hdparm>)包 软件包。对于 SCSI 设备，安装 [sdparm](<https://archlinux.org/packages/?name=sdparm>)包 软件包。 

##  使用

###  磁盘信息

运行下面命令获取磁盘信息： 
    
    # hdparm -I /dev/sda
    
###  基准测试

hdparm 可以被用于进行[基准测试](<../zh-cn/%E5%9F%BA%E5%87%86%E6%B5%8B%E8%AF%95.html#hdparm> "基准测试")。 

###  电源管理配置

现代硬盘驱动器支持许多电源管理功能，下表总结了最常见的功能。完整列表见 [hdparm(8)](<https://man.archlinux.org/man/hdparm.8>)。 

**警告：** 过于激进的电源管理会因频繁停车和降速而缩短硬盘驱动器的使用寿命。

参数 | 描述   
---|---  
`-B` | 设置 [Advanced Power Management](<https://zh.wikipedia.org/wiki/%E9%AB%98%E7%BA%A7%E7%94%B5%E6%BA%90%E7%AE%A1%E7%90%86> "zhwp:高级电源管理")（APM 高级电源管理）功能。可设定的值介于 1 和 255 之间，值越低意味着更积极的电源管理，值越高意味着更好的性能。从 1 到 127 的值允许降速，从 128 到 254 的值不允许。值 255 完全禁用该功能。   
`-S` | 设置驱动器待机（减速）前的超时时间。指定空闲状态（没有磁盘活动）的磁盘等待多长时间后关闭电机以节省电力。值设定为 0 禁用降速，从 1 到 240 的值指定 5 秒的倍数，从 241 到 251 的值指定 30 分钟的倍数。   
`-M` | 设置 [Automatic Acoustic Management](<https://en.wikipedia.org/wiki/Automatic_Acoustic_Management> "wikipedia:Automatic Acoustic Management")（自动声学管理）功能。大多数现代硬盘驱动器都能够降低磁头移动速度以减少其噪音输出。可设定的值取决于磁盘，某些磁盘可能不支持此功能。   
  
**注意：**

  * 当同时设置 `-B` 和 `-S` 参数时，APM 的值小于 128 可能会导致驱动器在 `-S` 超时值之前减速。详见 [[1]](<https://bbs.archlinux.org/viewtopic.php?id=216832>)。
  * 现在还无法读取 `-S` 的值。

要查询当前值，请传递不带值的参数。以 `-B` 为例： 
    
    # hdparm -B /dev/sda
    
要应用不同的值，例如将 APM 设置为 127： 
    
    # hdparm -B 127 /dev/sda
    
###  写入缓存

写入缓存是指在将数据写入硬盘前暂时将文件缓存到[硬盘板载内存](<https://zh.wikipedia.org/wiki/%E7%A3%81%E7%9B%98%E7%BC%93%E5%AD%98> "zhwp:磁盘缓存")的行为，同时可以提升性能。大多数硬盘都提供了写入缓存并默认启用。使用以下命令可以进行检查： 
    
    $ hdparm -W /dev/_sdX_
    
**警告：** 写入缓存可以提升性能，但也提升了突然断电时丢失数据的风险。

如果显示被禁用，可以使用如下命令进行启用： 
    
    $ hdparm -W 1 /dev/_sdX_
    
另外也可以将其禁用： 
    
    $ hdparm -W 0 /dev/_sdX_
    
###  关闭硬盘驱动器

这个功能的一个典型使用场景是，磁盘使用的是廉价外接 USB/SATA/火线硬盘盒或者桥接设备进行连接。如果在关闭电源开关时没有正确向驱动器发出停止命令，驱动器将被强制执行紧急磁头缩回。经常这样做迟早会破坏驱动器。一种解决方案是，在确定数据已写入介质后，运行命令关闭驱动器电源： 
    
    # hdparm -Y /dev/sd _X_
    
**警告：** 绝对要确保 

  1. 数据已实际完成写入。还建议等待一段时间，以待驱动器空闲。
  2. 你要关闭电源的目标驱动器正确（案例中为 `/dev/sd _X_`）

##  提示与技巧

###  在不唤醒磁盘的情况下查询磁盘状态

已知调用 hdparm 的查询选项会唤醒某些驱动器。在这种情况下，用 [smartmontools](</wzh/index.php?title=Smartmontools&action=edit&redlink=1> "Smartmontools（页面不存在）") 提供的 `smartctl` 来查询将不会唤醒睡眠的磁盘。例如： 
    
    # smartctl -i -n standby /dev/sda
    
    smartctl 6.5 2016-05-07 r4318 [x86_64-linux-4.10.13-1-ARCH] (local build)
    Copyright (C) 2002-16, Bruce Allen, Christian Franke, www.smartmontools.org
    
    Device is in STANDBY mode, exit(2)
    
###  使用 udev 规则使配置持久化

要使设置在重新启动后保持不变，可以使用 [udev](<../zh-cn/Udev.html> "Udev") 规则： 
    
    /etc/udev/rules.d/69-hdparm.rules
    
    ACTION=="add", SUBSYSTEM=="block", KERNEL=="sda", RUN+="/usr/bin/hdparm -B 254 -S 0 /dev/sda"

由于硬盘可能会被随机分配新的 `/dev/sd _X_`，可以参考 [Udev#Identifying a disk by its serial](<../zh-cn/Udev.html#Identifying_a_disk_by_its_serial> "Udev") 通过其序列号进行识别。 

具有多个硬盘驱动器的系统可以根据某些条件灵活应用该规则。例如，要将省电设置应用于所有旋转驱动器（带旋转磁头的硬盘，尤其不包括[固态硬盘](<../zh-cn/%E5%9B%BA%E6%80%81%E7%A1%AC%E7%9B%98.html> "固态硬盘")），请使用以下规则： 
    
    /etc/udev/rules.d/69-hdparm.rules
    
    ACTION=="add|change", KERNEL=="sd[a-z]", ATTRS{queue/rotational}=="1", RUN+="/usr/bin/hdparm -B 127 /dev/%k"

###  唤醒后重新应用配置

如果系统挂起/休眠后配置丢失，可以使用 [systemd-sleep](<../zh-cn/%E7%94%B5%E6%BA%90%E7%AE%A1%E7%90%86/%E6%8C%82%E8%B5%B7%E4%B8%8E%E4%BC%91%E7%9C%A0.html#Hooks_in_/usr/lib/systemd/system-sleep> "电源管理/挂起与休眠") 重新应用。 

将脚本放入 `/usr/lib/systemd/system-sleep/` 并设置为[可执行](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "可执行")： 
    
    /usr/lib/systemd/system-sleep/hdparm
    
    #!/bin/sh
    
    case $1 in post)
            /usr/bin/hdparm -B 254 -S 0 /dev/sda
            ;;
    esac

###  启动后直接使驱动器进入睡眠状态

很少使用的设备可以在引导过程结束时直接进入睡眠状态。这不适用于上述 udev 规则，因为它发生得太早了。为了在启动完成时发出命令，只需创建一个 [systemd](<../zh-cn/Systemd.html> "Systemd") 服务并[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")它： 
    
    /etc/systemd/system/hdparm.service
    
    [Unit]
    Description=hdparm sleep
    
    [Service]
    Type=oneshot
    ExecStart=/usr/bin/hdparm -q -S 120 -y /dev/sdb
    
    [Install]
    WantedBy=multi-user.target

###  使用不受支持的硬件

某些驱动器不支持通过 hdparm 降速。类似以下诊断错误消息很好地表明了这种情况： 
    
    # hdparm -S 240 /dev/sda
    
    /dev/sda:
    setting standby to 240 (20 minutes)
    HDIO_DRIVE_CMD(setidle) failed: Invalid argument
    
其他一些驱动器会确认 hdparm 命令，但不遵守参数（APM 或降速计时器）。使用 Toshiba P300（型号 HDWD120）HDD 时会观察到这一点。 

此类驱动器可以使用 [hd-idle](<https://aur.archlinux.org/packages/hd-idle/>)AUR 附带的 [systemd](<../zh-cn/Systemd.html> "Systemd") 服务进行降速。需要编辑 `/etc/conf.d/hd-idle` 和 `HD_IDLE_OPTS` 值，然后[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")和[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `hd-idle.service`。 

例如为 `/dev/sda` 设置 10 分钟空闲时间和为 `/dev/disk/by-uuid/01CF0AC9AA5EAF70` 设置 1 分钟空闲时间： 
    
    HD_IDLE_OPTS="-i 0 -a /dev/sda -i 600 -a /dev/disk/by-uuid/01CF0AC9AA5EAF70 -i 60"
    
开头的 `-i 0` 参数表示在其他驱动器上禁用 hd-idle。 

###  西部数据绿盘的电源管理

_Western Digital Green_ 硬盘有一个特殊的 _idle3_ 计时器，控制驱动器在将磁头移动到停放位置并进入低功耗状态之前等待多长时间。出厂默认设置为 8 秒，这可能会在短时间内发生数千个磁头加载/卸载周期并最终导致过早发生故障，更不用说在执行例行 I/O 之前经常需要唤醒驱动器对性能的影响。西部数据发布过[声明](<https://web.archive.org/web/20190129000226/http://wdc.custhelp.com/app/answers/detail/a_id/5357>)，声称 Linux 没有针对低功耗存储设备进行优化，并建议降低日志记录频率。这里有几种方法可以修改 _idle3_ 状态： 

  1. 西部数据提供了一个 DOS 实用程序 _wdidle3.exe_ ，可以[下载](<https://support.wdc.com/downloads.aspx?p=113>)用于调整此设置。此实用程序旨在仅升级以下硬盘的固件： WD1000FYPS，WD7500AYPS 和 WD7501AYPS，但众所周知它也能够更改其他绿盘的 _idle3_ 计时器。
  2. hdparm 在 `-J` 标志后面具有逆向工程实现，似乎至少能在几个驱动器上工作，但它不像原始官方程序那样完整。对于 Linux 使用，建议设置为 30 秒。值设定为 0 以完全禁用 WD idle3 计时器（**不推荐** ）：
         
         # hdparm -J 30 --please-destroy-my-drive /dev/sda

。请参阅[#使用 udev 规则使配置持久化](<#%E4%BD%BF%E7%94%A8_udev_%E8%A7%84%E5%88%99%E4%BD%BF%E9%85%8D%E7%BD%AE%E6%8C%81%E4%B9%85%E5%8C%96>)在支持的硬盘驱动器上自动使用此参数。
  3. [idle3-tools](<https://archlinux.org/packages/?name=idle3-tools>)包 软件包提供了另一个非官方实用程序。原始 `_idle3_` 值作为 _idle3ctl_ 命令的参数传递。[idle3ctl(8)](<https://man.archlinux.org/man/idle3ctl.8>) 内的底部表格中提供了此值与超时（以秒为单位）之间的对应关系。以下命令会将计时器设置为 30 秒：
         
         # idle3ctl -s 129 /dev/sdc

。以下命令完全禁用计时器（**不推荐** ）：
         
         # idle3ctl -d /dev/sdc

**注意：**

  * 无论使用上述哪个程序，任何更改都需要一个完整的电源循环才能生效。这意味着驱动器需要关闭然后再打开，简单的重启是不够的。
  * 众所周知，一些西数绿盘对 hparm 的待机超时参数有不同的解释，导致 `-S 1` 会配置计时器为 10 分钟而不是 5 秒。
  * 西数绿盘在读/写期间的功耗通常约为 5.3W，空闲模式下为 4.7W，待机模式下为 0.7W。

##  疑难解答

###  APM 级别在挂起后被重置

APM 级别可能会在挂起后重置，需要在每次恢复后重新执行。这可以通过以下 [systemd](<../zh-cn/Systemd.html> "Systemd") 单元（改编自[论坛主题](<https://bbs.archlinux.org/viewtopic.php?id=151640>)）自动完成： 
    
    /etc/systemd/system/apm.service
    
    [Unit]
    Description=Local system resume actions
    After=suspend.target hybrid-sleep.target hibernate.target
    
    [Service]
    Type=simple
    ExecStart=/usr/bin/hdparm -B 254 /dev/sda
    
    [Install]
    WantedBy=sleep.target

**注意：**`sleep.target` 被所有 `suspend`、`hybrid-sleep` 和 `hibernate` 目标拉取，但它在系统挂起**之前** 就会完成启动，因此必须明确指定三个目标。详见[[2]](<https://wiki.archlinux.org/index.php?title=Talk:Hdparm&oldid=440457#Troubleshooting_APM_settings_after_suspend.2C_hibernate_or_hybrid-sleep>)。

也可以[在 /usr/lib/systemd/system-sleep 中创建一个钩子](<../zh-cn/%E7%94%B5%E6%BA%90%E7%AE%A1%E7%90%86.html#/usr/lib/systemd/system-sleep_%E4%B8%AD%E7%9A%84%E9%92%A9%E5%AD%90> "电源管理")。 

##  另请参见

  * <https://sourceforge.net/projects/hdparm/> \- SourceForge 上的 hdparm 页面
