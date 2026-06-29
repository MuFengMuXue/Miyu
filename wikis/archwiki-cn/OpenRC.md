相关文章

  * [init](<../zh-cn/Init.html> "Init")

**翻译状态：**

  * 本文（或部分内容）译自 [OpenRC](<https://wiki.archlinux.org/title/OpenRC> "arch:OpenRC")，最近一次同步于 2026-02-26，若英文版本有所[更改](<https://wiki.archlinux.org/title/OpenRC?diff=0&oldid=802080>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/OpenRC_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

**警告：** Arch Linux只为[systemd](<../zh-cn/Systemd.html> "Systemd")提供官方支持。[[1]](<https://archlinux.org/news/end-of-initscripts-support/>)求助时请在帮助请求中提及使用OpenRC。

[OpenRC](<https://wiki.gentoo.org/wiki/OpenRC> "gentoo:OpenRC")是一个由Gentoo开发者维护的服务管理器。OpenRC是基于依赖关系的，通常使用系统提供的init程序[SysVinit](<../zh-cn/SysVinit.html> "SysVinit")。 

##  安装

关于init组件的细节，请查阅[Init](<../zh-cn/Init.html> "Init")。 

安装[openrc](<https://aur.archlinux.org/packages/openrc/>)AUR包。在0.25版本之后，OpenRC在`/usr/bin/openrc-init`提供它自己的init。 

可选地，您可以使用其他init,例如[busybox](<https://archlinux.org/packages/?name=busybox>)包。请注意，当使用`openrc-init`时，它必须和`openrc-shutdown`成对使用。并且不要使用来自其他包的`shutdown`和`reboot`命令，否则您将会遇到错误。 

一组基本的服务文件可以从[openrc-arch-services-git](<https://aur.archlinux.org/packages/openrc-arch-services-git/>)AUR包获得。其他包可能有在此包之外提供的服务文件，建议在AUR上搜索。 

为了保持和以前的初始化脚本的兼容性，配置文件已经在`/etc/openrc/`中安装。 

###  启动

在[kernel parameters](<../zh-cn/Kernel_parameters.html> "Kernel parameters")中设置`init`选项来使用OpenRC启动。 

要使用OpenRC内建的init，设置`init=/usr/bin/openrc-init`。 

请注意，当使用`openrc-init`时，`/etc/inittab`文件将不会被使用。 

##  配置

`/etc/openrc/conf.d`目录和`/etc/openrc/rc.d`文件被用于配置。 

关于配置OpenRC的一般信息，请查看： 

  * [OpenRC manuals](<https://www.calculate-linux.org/main/en/openrc_manuals>)
  * [Gentoo:OpenRC](<https://wiki.gentoo.org/wiki/OpenRC> "gentoo:OpenRC")

关于从[systemd](<../zh-cn/Systemd.html> "Systemd")迁移的说明，请查看[Init#Configuration](<../zh-cn/Init.html#Configuration> "Init")。 

###  服务

通过root身份运行`rc-update add _service_name_ _runlevel_`来启动OpenRC服务。建议启动以下服务： 

服务名  |  [Runlevel](<https://wiki.gentoo.org/wiki/OpenRC#Named_runlevels> "gentoo:OpenRC") | 描述   
---|---|---  
udev  | sysinit  | 设备热插拔   
alsa  | default  |  [ALSA](<../zh-cn/ALSA.html> "ALSA") state   
acpid  | default  | ACPI事件   
dbus  | default  | 消息总线   
dcron  | default  | 定时任务   
syslog-ng  | default  | 系统日志   
  
**警告：** 如果在您的kernel parameters中使用`init=/usr/bin/openrc-init`，您将需要手动启用[getty](<../zh-cn/Getty.html> "Getty")服务，否则您将无法使用如[该文档](<https://github.com/OpenRC/openrc/blob/master/agetty-guide.md>)中所述的交互式TTY

如果有需要，通过创建到`/etc/openrc/init.d/getty`的符号链接来为每个[getty](<../zh-cn/Getty.html> "Getty")创建服务。例如为`/dev/tty1`： 
    
    # ln -s /etc/openrc/init.d/agetty{,.tty1}
    # rc-update add agetty.tty1 default
    
为了防止PAM在登录后尝试向systemd注册（这可能会引发[问题](<https://bbs.archlinux.org/viewtopic.php?id=285505>), 可以安全地删除或注释`/etc/pam.d/system-auth`中提到systemd的行。 

另请参阅[Gentoo:Systemd#Native services](<https://wiki.gentoo.org/wiki/Systemd#Native_services> "gentoo:Systemd")。 

###  网络

网络通过`newnet` [[2]](<https://github.com/OpenRC/openrc/blob/master/NEWNET.md>)配置。 

编辑`/etc/openrc/conf.d/network`;`ip`、([iproute2](<https://archlinux.org/packages/?name=iproute2>)包)和`ifconfig`、([net-tools](<https://archlinux.org/packages/?name=net-tools>)包)命令都被支持。下面是一个使用`ip`的例子： 
    
    ip_eth0="192.168.1.2/24"
    defaultiproute="via 192.168.1.1"
    ifup_eth0="ip link set \$int mtu 1500"

网络服务被默认添加到引导运行级别(boot runlevel)，所以不需要采取进一步操作。关于一般网络信息，请参阅[Network configuration](<../zh-cn/Network_configuration.html> "Network configuration")。 

<nowiki>

**注意：** 您也可以通过启用相应的服务来使用 [NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager") 或者 [dhcpcd](<../zh-cn/Dhcpcd.html> "Dhcpcd") 。

###  启动日志

要启用启动日志记录，将`/etc/openrc/rc.conf`中`rc_logger="YES"`一行去注释。在启用时，启动日志存储在`/var/log/rc.log`。 

###  主机名

OpenRC通过`/etc/openrc/conf.d/hostname`来修改主机名。它看起来像这样： 
    
    #设置这台电脑的主机名
    hostname="myhostname"

###  内核模块

OpenRC使用`/etc/openrc/conf.d/modules`而不是`/etc/modules-load.d`。例如： 
    
    /etc/openrc/conf.d/modules
    
    #您应该查阅内核文档和配置获取模块及其选项的列表
    
    modules="vboxdrv acpi_cpufreq"

###  本地化

键盘布局可以通过`/etc/openrc/conf.d/keymaps`和`/etc/openrc/conf.d/consolefont`来配置。您也可以通过`/etc/locale.conf`文件，其来源于`/etc/profile.d/locale.sh`。 

##  使用

本节对[systemd](<../zh-cn/Systemd.html> "Systemd")以及其他[init](<../zh-cn/Init.html> "Init")进行比较。 

您可以忽略`.service`和`.target`扩展，尤其是在编辑[kernel parameters](<../zh-cn/Kernel_parameters.html> "Kernel parameters")时。 

systemd | SysVinit | OpenRC | 描述   
---|---|---|---  
`systemctl list-units` | `rc.d list` | `rc-status` | 列出所有正在运行的服务的状态   
`systemctl --failed` |  | `rc-status --crashed` | 检查所有失败的服务   
`systemctl --all` |  | `rc-update -v show` | 显示所有可用服务   
`systemctl (start, stop, restart, status) daemon.service` | `rc.d (start, stop, restart) daemon` | `rc-service daemon (start, stop, restart, status)` | 改变服务状态   
`systemctl (enable, disable) daemon.service` | `chkconfig daemon (on, off)` | `rc-update (add, del) daemon` | 启用或停用服务   
`systemctl daemon-reload` | `chkconfig daemon --add` |  | 创建或修改配置   
  
##  提示和技巧

###  静默启动

要隐藏OpenRC的启动信息，您可以编辑`/etc/inittab`，将`--quiet`添加到每个OpenRC命令。有关更多信息，请查看`$ openrc -h`。 

##  故障排除

###  卸载/tmp时出错

当关机时，您可能会得到这样的信息： 
    
    * Unmounting /tmp ... 
    * in use but fuser finds nothing [ !! ]

可以通过向`/etc/openrc/conf.d/localmount`添加如下内容解决： 
    
    no_umounts="/tmp"
    
**注意：** 只有将/tmp安装为tmpfs时才会出现此问题。

###  禁用IPv6无效

一种选择是向`/etc/openrc/sysctl.d`下一个以`.conf`结尾的文件添加： 
    
    # 禁用IPv6
    net.ipv6.conf.all.disable_ipv6 = 1
    
###  在关机期间以只读模式重新挂载根目录失败

如果发生上述情况，请编辑`/etc/openrc/init.d/mount-ro`，找到下面一行： 
    
    # Flush all pending disk writes now
    sync; sync
    
在其之后放入： 
    
    telinit u
    
###  找不到/etc/sysctl.conf

默认情况下，调用`sysctl --system`来加载sysctl配置。[[3]](<https://github.com/OpenRC/openrc/blob/master/init.d/sysctl.in#L40>)这包括从Arch中删除的`/etc/sysctl.conf`。[[4]](<https://archlinux.org/news/deprecation-of-etcsysctlconf/>)

要放置丢失文件的错误，请创建文件： 
    
    # touch /etc/sysctl.conf
    
###  opentmpfiles-setup无法启动

在启动OpenRC时，您可能会看到如下行： 
    
    * Setting up tmpfiles.d entries ...
    chattr: Operation not supported while setting flags on /var/log/journal
    chattr: No such file or directory while trying to stat /var/log/journal/%m
    chattr: Operation not supported while setting flags on /var/log/journal/remote
    [ !! ]
    ERROR: opentmpfiles-setup failed to start
    
这是由于`/usr/lib/tmpfiles.d/journal-nocow.conf`使用的选项，只有当journal位于btrfs上时才有效。 

请查阅https://github.com/OpenRC/opentmpfiles/issues/2来获取详细信息。 

一种解决方法是创建一个空的`/etc/tmpfiles.d/journal-nocow.conf`来覆盖这些设置。 

##  恢复到systemd

在大多数情况下，恢复到systemd应该很简单。它本质上是迁移到OpenRC的逆向，注意以下几点： 

  * 删除或以其他方式编辑内核命令行上的`init=`参数。
  * 用等价的包替换OpenRC定制的或no-systemd的包。

##  另请参阅

  * [Wikipedia:OpenRC](<https://en.wikipedia.org/wiki/OpenRC> "wikipedia:OpenRC")
  * [Gentoo:OpenRC](<https://wiki.gentoo.org/wiki/OpenRC> "gentoo:OpenRC")
  * [Forum thread about OpenRC in Arch](<https://bbs.archlinux.org/viewtopic.php?id=152606>)
  * [Manjaro wiki](<https://wiki.manjaro.org/index.php?title=OpenRC,_an_alternative_to_systemd>)
