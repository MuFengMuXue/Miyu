**翻译状态：**

  * 本文（或部分内容）译自 [Hddtemp](<https://wiki.archlinux.org/title/Hddtemp> "arch:Hddtemp")，最近一次同步于 2022-11-20，若英文版本有所[更改](<https://wiki.archlinux.org/title/Hddtemp?diff=0&oldid=757494>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Hddtemp_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [lm_sensors](<../zh-cn/Lm_sensors.html> "Lm sensors")
  * [Conky](<../zh-cn/Conky.html> "Conky")

[Hddtemp](<https://savannah.nongnu.org/projects/hddtemp/>) 是一个小工具（有守护进程），通过 [S.M.A.R.T.](</wzh/index.php?title=S.M.A.R.T.&action=edit&redlink=1> "S.M.A.R.T.（页面不存在）")（对于支持该功能的驱动器）提供硬盘温度。 

**提示：** 访问驱动器温度的一个更通用的选项是 [Linux 监测传感器](<../zh-cn/Lm_sensors.html> "Lm sensors")，因为它也处理其他数据。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [hddtemp](<https://archlinux.org/packages/?name=hddtemp>)包。 

##  使用

Hddtemp 需要[根用户](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E6%A6%82%E8%A7%88> "根用户")权限。命令 `hddtemp` 后面必须至少有一个驱动器的位置。你可以列出几个用空格分隔的驱动器。 
    
    # hddtemp /dev/disk/by-id/wwn-0x60015ee0000b237f /dev/sd _X2_ ... /dev/sd _Xn_
    
**注意：**`/dev/`下的块设备命名，如`/dev/sdX`，是不一致的。更多信息请参见[持久化块设备命名](<../zh-cn/%E5%9D%97%E8%AE%BE%E5%A4%87%E6%8C%81%E4%B9%85%E5%8C%96%E5%91%BD%E5%90%8D.html> "持久化块设备命名")。 

更多使用信息见 [hddtemp(8)](<https://man.archlinux.org/man/hddtemp.8>)。 

##  守护进程

运行守护进程允许普通用户通过 TCP/IP 访问温度信息。这对脚本和系统监控很有帮助。 

该守护进程由 `hddtemp.service` [控制](<../zh-cn/Systemd.html#Using_units> "Systemd")。 

要获取温度，请连接该守护进程，其监听端口为7634。 

使用 [inetutils](<https://archlinux.org/packages/?name=inetutils>)包： 
    
    $ telnet localhost 7634
    
使用 [gnu-netcat](<https://archlinux.org/packages/?name=gnu-netcat>)包: 
    
    $ nc localhost 7634
    
两种输出都类似于： 
    
    |/dev/sda|ST3500413AS|32|C||/dev/sdb|ST2000DM001-1CH164|36|C|
    
为了数据更直观： 
    
    $ nc localhost 7634 |sed 's/|//m' | sed 's/||/ \n/g' | awk -F'|' '{print $1 " " $3 " " $4}'
    
    /dev/sda 32 C 
    /dev/sdb 36 C

###  覆盖默认磁盘

默认的 Hddtemp 守护进程只监控 `/dev/sda`。如果有多个磁盘，需要[覆盖](<../zh-cn/Systemd.html#Editing_provided_units> "Systemd")默认配置来监控。 

如果需要查看哪些硬盘支持监控，可以用 [smartmontools](<https://archlinux.org/packages/?name=smartmontools>)包 检查。[编辑](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "编辑") `hddtemp.service`： 
    
    [Service]
    ExecStart=
    ExecStart=/usr/bin/hddtemp --daemon --foreground /dev/disk/by-id/wwn-0x60015ee0000b237f /dev/sdb --listen=127.0.0.1
    
将设备名称更改为需要监控的设备。 

编辑完毕后，保存文件并退出编辑器。[Systemd](<../zh-cn/Systemd.html> "Systemd") 会应用更改并自动重新加载 `hddtemp` 服务。 

你也可以使用 [auto-generate](<https://github.com/AndyCrowd/auto-generate-configuration-files/blob/master/gen-customexec.conf-hddtemp.sh>) 脚本，它会使用 {{pkg|smartmontools} 检测支持的硬盘，并打印到标准输出文件。 

##  监控器

Hddtemp 可以与[系统监视器](<../zh-cn/List_of_applications.html#System_monitors> "List of applications")集成。[Conky](<../zh-cn/Conky.html> "Conky") 在守护进程模式中已内置对 Hddtemp 的支持。只需[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `hddtemp.service` 并将`$hddtemp ℃` 添加到 Conky 配置文件。 

##  固态硬盘

Hddtemp 通常从驱动器的智能数据中读取字段`194`。在固态硬盘中，温度信息通常存储在`190`字段。要获取这些信息，可以运行： 
    
    # smartctl --all /dev/sd _x_
    
或 
    
    # hddtemp --debug /dev/sd _x_
    
其中 `/dev/sd _x_` 是驱动器（使用 [lsblk](<../zh-cn/%E8%AE%BE%E5%A4%87%E6%96%87%E4%BB%B6.html#lsblk> "Lsblk") 来检查）。 

或者在 `/etc/hddtemp.db` 中添加新条目。例如： 
    
    # echo '"Samsung SSD 840 EVO 250GB" 190 C "Samsung SSD 840 EVO 250GB"' >> /etc/hddtemp.db
    