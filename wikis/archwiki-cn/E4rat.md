[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:E4rat](<../zh-cn/Talk:E4rat.html>)讨论)

相关文章

  * [Improve Boot Performance (简体中文)](</wzh/index.php?title=Improve_Boot_Performance_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "Improve Boot Performance \(简体中文\)（页面不存在）")
  * [Preload](<../zh-cn/Preload.html> "Preload")
  * [Ext4 (简体中文)](</wzh/index.php?title=Ext4_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "Ext4 \(简体中文\)（页面不存在）")

**翻译状态：**

  * 本文（或部分内容）译自 [E4rat](<https://wiki.archlinux.org/title/E4rat> "arch:E4rat")，最近一次同步于 2012-07-11，若英文版本有所[更改](<https://wiki.archlinux.org/title/E4rat?diff=0&oldid=212533>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/E4rat_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-preferences-desktop-locale-modified.png)](<../File:Tango-preferences-desktop-locale-modified.png>)**这篇文章或章节的[翻译](<../Project:%E8%B4%A1%E7%8C%AE.html#Translating> "Project:Contributing")质量不佳。**

**原因：** Last updated in 2012（在 [Talk:E4rat#](<../zh-cn/Talk:E4rat.html>) 中讨论）

[e4rat](<http://e4rat.sourceforge.net/>)，“Ext4 - Reducing Access Times”（减少ext4访问次数）之略，是一款优化[ext4](</wzh/index.php?title=Ext4_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "Ext4 \(简体中文\)（页面不存在）")文件系统、加速系统启动的工具。该项目由 Andreas Rid 和 Gundolf Kiefer 发起。[e4rat工具系列](<http://e4rat.sourceforge.net/>)包含e4rat-collect、e4rat-realloc、e4rat-preload。 

目前最新版本是0.21。 

##  机制

如果你用[bootchart](</wzh/index.php?title=Bootchart_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "Bootchart \(简体中文\)（页面不存在）")监视开机过程，会发现CPU和磁盘均未全速运转。e4rat将改变这一状况，使系统启动时CPU和磁盘全速运转，从而加速启动过程。此优化包括三步： 

  * **e4rat-collect** \- 收集文件，在特定时间（默认120s，可调整）内收集文件信息
  * **e4rat-realloc** \- 文件再分配，在磁盘上整理文件
  * **e4rat-preload** \- 预读取文件

###  对谁有效？

经证实，e4rat对一般用户——直接进入X图形界面——特别有效，但对于服务器用户——启动到命令行——效果不怎么明显。此外，此工具对SSD（固态磁盘）用户也没用，因为SSD基本没有读取延迟。[Ureadahead](</wzh/index.php?title=Ureadahead&action=edit&redlink=1> "Ureadahead（页面不存在）") 可能会有效。 

**注意：**[e4rat 官方手册](<https://web.archive.org/web/20120315185141/http://e4rat.sourceforge.net/wiki/index.php/Main_Page#Ubuntu_and_ureadahead>) 声称 ureadahead 与 e4rat 冲突，在 Ubuntu 中确实这样，但是 Arch 中并无冲突，但有 ureadahead 的情况下，速度提升效果有限。

为保险起见，请及时备份数据。 

##  安装

从 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 安装软件包 [e4rat](<https://aur.archlinux.org/packages/e4rat/>)AUR. 

##  配置

现在进入正题。 

### e4rat-collect

首先，e4rat需要收集开机时预读的文件列表。添加如下内容到`/boot/grub/menu.lst`（grub）启动项的`linux`行末尾，或`/boot/grub/grub.cfg`（grub2）启动项的`kernel` 行： 
    
    kernel /vmlinuz0linux root=/dev/disk/by-label/ARCH init=/sbin/e4rat-collect ro 5

) 

由于该过程只需进行一次，所以我建议直接在grub命令行修改即可，而不必修改启动菜单文件。 

启动后，e4rat-collect默认会监视系统120秒。所以请在两分钟内打开经常使用的程序，e4rat-collect会记录下来（译者注：我不建议预读太多东西，这样反而会拖慢开机速度）。可以在`/etc/e4rat.conf`中修改默认的120秒收集时间（`timeout 120`这一行，去掉注释）。或者手动停止e4rat-collect： 
    
    e4rat-collect -k
    
或者： 
    
    pkill e4rat-collect
    
收集完成后，应该会出现这个文件：`/var/lib/e4rat/startup.log`

最后，不要忘记从`/boot/grub/grub.cfg`或`/boot/grub/menu.lst`中移除最开始添加的内容。 

### e4rat-realloc

接着上一步进行文件再分配（通俗说就是磁盘整理）。先切换启动级别1： 
    
    sudo init 1
    
输入root密码，执行： 
    
    e4rat-realloc  /var/lib/e4rat/startup.log
    
根据`startup.log`中文件的多少，或长或短要等一段时间。 

**注意：** 使用纯 [systemd](<../zh-cn/Systemd.html> "Systemd") 的用户不需要修改 [runlevels](</wzh/index.php?title=Runlevels&action=edit&redlink=1> "Runlevels（页面不存在）")，用 root 登录后执行 _e4rat-collect_ 即可。

### e4rat-preload

永久性地，添加如下内容到`/boot/grub/grub.cfg`（grub）启动项的`linux`行末尾，或`/boot/grub/menu.lst`（grub2）启动项的`kernel`行： 
    
    init=/sbin/e4rat-preload
    
**注意：** 如果你正在使用grub2，内核参数最好添加到`/etc/default/grub` \- `GRUB_CMDLINE_LINUX="..."`

###  另一选择：e4rat-preload-lite

论坛用户[jlindgren](<https://bbs.archlinux.org/viewtopic.php?id=117776&p=1>)提供了一个优化版本的preload程序，也许能帮你节约几秒的开机时间： 

优化之处在于： 

  * 启动`/sbin/init`前，只预读前100个文件（inode和文件内容），启动`/sbin/init`后再并行地预读其他文件。

从[AUR](<../zh-cn/AUR_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "AUR \(简体中文\)")中安装该工具（译者注，不要卸载e4rat，该包只提供preload）：[e4rat-preload-lite](<https://aur.archlinux.org/packages/e4rat-preload-lite/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found]

添加（或替换）如下内容到`/boot/grub/grub.cfg`（grub）启动项的`linux`行末尾，或`/boot/grub/menu.lst`（grub2）启动项的`kernel`行： 
    
    init=/usr/sbin/e4rat-preload-lite
    
重启即可。 

##  其他 init 程序搭配 e4rat

e4rat-collect默认会使用`/sbin/init`替换自己。如果使用其他init程序（比如 `/bin/systemd`），修改`/etc/e4rat.conf`中的`init`参数，并去掉前面的分号（注释）即可。 

##  启动流程图

通过[bootchart](</wzh/index.php?title=Bootchart_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "Bootchart \(简体中文\)（页面不存在）")绘制使用e4rat前后的启动流程图，可以直观地看到巨大的优化。 

### bootchart 0.9-9

添加如下内容到`grub.cfg`或`menu.lst`的启动菜单项即可： 
    
    init=/sbin/bootchartd bootchart_init=/sbin/e4rat-preload
    
该版本bootchart会在[登录管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")启动后停止监视。 

### bootchart2

添加如下内容到`grub.cfg`或`menu.lst`的启动菜单项： 
    
    init=/sbin/bootchartd
    
然后，手动修改`/sbin/bootchartd`的`init="/sbin/init"`这一行为`init="/sbin/e4rat-preload`。（译者注：虽然程序说明上说，应该通过添加启动参数设置init，但我试了，不行。） 

`/etc/bootchartd.conf`的`EXIT_PROC`中可以设置哪些程序启动后停止监视： 
    
    EXIT_PROC="kdm_greet xterm konsole gnome-terminal metacity mutter compiz ldm icewm-session enlightenment"
    
留空的话，需要手动停止监视。 

##  疑难解答

如果出现问题，请参考以下内容。 

###  startup.log 未创建

  * 在`/etc/rc.conf`注释掉`auditd`。
  * 检查下列命令的输出：

    dmesg | grep e4rat
    
  * 在`/etc/e4rat.conf`设置`loglevel`为`31`获取详细调试信息。

###  e4rat 错误地报告文件系统为 ext2

  * 添加如下内容到`/boot/grub/grub.cfg`启动项的`linux`行末尾，或`/boot/grub/menu.lst`启动项的`kernel`行末尾：

    rootfstype=ext4
    
###  无法读取 startup.log

  * 这说明你的`/var`和根目录不在同一分区，因而开机时为挂载。可以修改`startup.log`文件位置（比如{ic|/etc/startup.log}}），方法是修改`/etc/e4rat.conf`：

    startup_log_file /etc/e4rat/startup.log
    
###  减少启动时的信息输出

在 `/etc/e4rat.conf` 中将 `loglevel` 减小到 1。 
