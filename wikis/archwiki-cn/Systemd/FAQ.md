**翻译状态：**

  * 本文（或部分内容）译自 [Systemd/FAQ](<https://wiki.archlinux.org/title/Systemd/FAQ> "arch:Systemd/FAQ")，最近一次同步于 2023-02-28，若英文版本有所[更改](<https://wiki.archlinux.org/title/Systemd/FAQ?diff=0&oldid=766254>)，则您可以帮助同步与[翻译](<../../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Systemd_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)/FAQ_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [systemd](<../../zh-cn/Systemd.html> "Systemd")
  * [systemd/用户](<../../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "Systemd/用户")
  * [Daemons](<../../zh-cn/Systemd.html> "Daemons")

##  常见问题

最新的已知问题，参见：[TODO](<https://github.com/systemd/systemd/blob/master/TODO>)。 

###  为什么控制台上会显示日志信息？

请自行设置内核日志等级（loglevel）。以前，`/etc/rc.sysinit` 帮我们把 dmesg 的日志等级设置为 `3`，是比较合适的。[内核参数](<../../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")中加入 `loglevel=3` 或 `quiet` 即可。 

###  如何修改默认的 tty 控制台（getty）数量？

目前默认仅启动一个 getty，如果切换到其它 tty, 一改新的 getty 会通过 socket 激活方式启动。例如 [Ctl] [Alt] [F2] 会在 tty2 启动 getty。 

默认情况下，最多可以自动启动 6 个 getty。[F7] 到 [F12] 不会启动 getty。要修改最大值，在 `/etc/systemd/logind.conf` 中修改 `NAutoVTs`。如果要启用所有的 [F _x_]，可以将其设置为 12。如果要[将日志转发到tty12](<../../zh-cn/Systemd/Journal.html#%E8%BD%AC%E5%8F%91_journald_%E5%88%B0_/dev/tty12> "Systemd/日志")，可以把 NAutoVTs 设置为 11。 

修改启动时启用的 tty 个数，可以采取下面方法： 

添加新的 getty： 

在 `/etc/systemd/system/getty.target.wants/` 添加新的软链接即可： 
    
    # ln -sf /usr/lib/systemd/system/getty@.service /etc/systemd/system/getty.target.wants/getty@tty9.service
    # systemctl start getty@tty9.service
    
移除 getty： 

从 `/etc/systemd/system/getty.target.wants/` 删除对应的软链接即可： 
    
    # rm /etc/systemd/system/getty.target.wants/getty@tty5.service /etc/systemd/system/getty.target.wants/getty@tty6.service
    # systemctl stop getty@tty5.service getty@tty6.service
    
systemd 不使用 `/etc/inittab` 文件。 

###  怎样输出更详细的开机信息？

如果内核信息输出后就什么信息都不输出了，很可能是因为你在内核参数中添加了 `quiet`。删除即可，然后你就可以看到一列列绿色的 [ OK ] 和红色的 [ FAILED ]了。 

所有信息都记录在系统日志，可以通过 `$ systemctl` 查看系统状态，通过 `journalctl` 查看日志。 

###  开机后控制台信息会被清空，如何避免？

创建 `/etc/systemd/system/getty@.service.d` 目录，创建文件 `nodisallocate.conf`，将 `TTYVTDisallocate` 设置为 `no`. 
    
    /etc/systemd/system/getty@.service.d/nodisallocate.conf
    
    [Service]
    TTYVTDisallocate=no

###  Systemd 需要哪些内核模块?

systemd 不支持 3.0 版本之前的内核。 

如果是自己编译内核，需要开启一些选项。请参考`/usr/share/doc/systemd/README`. 

自己编译 Systemd，请参考[systemd git ](<https://github.com/systemd/systemd/blob/main/README>)中的版本. 

###  怎样知道一个目标需要哪些进程服务？

例如，你可能想搞明白目标单元 `multi-user.target` 究竟启用了哪些服务，那么以下命令即可： 
    
    $ systemctl show -p "Wants" multi-user.target
    
    Wants=rc-local.service avahi-daemon.service rpcbind.service NetworkManager.service acpid.service dbus.service atd.service crond.service auditd.service ntpd.service udisks.service bluetooth.service org.cups.cupsd.service wpa_supplicant.service getty.target modem-manager.service portreserve.service abrtd.service yum-updatesd.service upowerd.service test-first.service pcscd.service rsyslog.service haldaemon.service remote-fs.target plymouth-quit.service systemd-update-utmp-runlevel.service sendmail.service lvm2-monitor.service cpuspeed.service udev-post.service mdmonitor.service iscsid.service livesys.service livesys-late.service irqbalance.service iscsi.service

除了 `Wants`，还可以查看各种形式的依赖和被依赖信息：`WantedBy`、`Requires`、`RequiredBy`、`Conflicts`、`ConflictedBy`、`Before`、`After`。 

###  电脑关闭了但电源没有断。

使用`systemctl poweroff` 而不是 `systemctl halt`. 

###  如何在启动的时候，运行自定义的一个脚本？

在`/etc/systemd/system` 中新建一个文件(名称可以为 _myscript_.service) 然后在其中写入如下内容： 
    
    [Unit]
    Description=My script
    
    [Service]
    ExecStart=/usr/bin/my-script
    
    [Install]
    WantedBy=multi-user.target 
    
然后开启该守护进程 
    
    # systemctl enable _myscript_.service
    
本例是说当目标multi-usr载入的时候，会启动你这个自定义脚本。脚本需要有可执行权限。 

**注意：** 如果要启动 shell 脚本，请把 `#!/bin/sh` 加到脚本的第一行，下面的做法不会成功`ExecStart=/bin/sh /path/to/script.sh`。

###  .service 状态显示绿色的 "active (exited)" (例如 iptables)

如果单次执行的程序配置了 `RemainAfterExit=yes`，这是正常的状态。详情请参考 [systemd.service(5) § OPTIONS](<https://man.archlinux.org/man/systemd.service.5#OPTIONS>)。 `systemd-user-sessions.services`、`nftables.service`、`iptables.service` 等单次执行服务均是这样。 

###  因为软链接已经存在，无法启用服务

[启用](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable")单元时，可能出现如下错误： 
    
    Failed to enable unit: File /etc/systemd/system/_symlink_ already exists and is a symlink to _file_.
    
此错误一般发生在启用指令要创建的`/etc/systemd/system/`软链已经存在的时候。典型的例子是在切换显示管理器的时候(例如切换 [GDM](<../../zh-cn/GDM.html> "GDM") 或 [SDDM](<../../zh-cn/SDDM.html> "SDDM")需要启用 `gdm.service` 或 `sddm.service`)，这时`/etc/systemd/system/display-manager.service` 已经存在。 

要解决此问题，先禁用原来的显示管理器或者使用 `-f`/`--force` 选项强制覆盖原有链接，请参考 [systemctl(1) § OPTIONS](<https://man.archlinux.org/man/systemctl.1#OPTIONS>)。 
