**翻译状态：**

  * 本文（或部分内容）译自 [Netatalk](<https://wiki.archlinux.org/title/Netatalk> "arch:Netatalk")，最近一次同步于 2020-04-23，若英文版本有所[更改](<https://wiki.archlinux.org/title/Netatalk?diff=0&oldid=599908>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Netatalk_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Netatalk](<http://netatalk.sourceforge.net/>) 是一个 Apple Filing Protocol (AFP) 的开源实现。它为 Unix 风格系统提供了与 Macintosh 文件共享的功能。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [netatalk](<https://aur.archlinux.org/packages/netatalk/>)AUR 包。 

##  配置

[使用 systemd](<../zh-cn/Systemd.html#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83> "Systemd") 来启用或启动 `netatalk.service`

除了一并安装的配置文件（升级的时候会检查这些文件），另外 Netatalk 可能会生成 `/etc/netatalk/afp_signature.conf` 或 `/var/state/netatalk/afp_signature.conf`，来保存系统的 UUID；`/etc/netatalk/afp_voluuid.conf` 或 `/var/state/netatalk/afp_voluuid.conf` 来保存 Time Machine 的 UUID。为了消除本地网络的服务广播的歧义，移除包的时候可能并不会删除这些文件。 

Netatalk 3.x 只使用一个配置文件 `/etc/afp.conf`。 查看 `man afp.conf` 来配置该文件（需要进程拥有 `afpd.log` 的写权限）： 
    
    /etc/afp.conf
    
    [Global]
     mimic model = TimeCapsule6,106
     log level = default:warn
     log file = /var/log/afpd.log
     hosts allow = 192.168.1.0/16
    
    [Homes]
     basedir regex = /home
    
    [TimeMachine]
     path = /mnt/timemachine
     valid users = tmuser
     time machine = yes
    
    [Shared Media]
     path = /srv/share/media
     valid users = joe sam
    
**警告：** 不要在 `afp.conf` 里面使用符号链接（symbolic link）

###  来客访问

如果要让来客**只读** 地访问你的共享文件夹，在 `[Global]` 这一行的下面加入以下片段： 
    
    /etc/afp.conf
    
    [Global]
    uam list = uams_guest.so
    
要让来客拥有**读/写** 权限，首先要像上面一样建立只读权限，再添加下面这一行到指定的分享片段： 
    
    /etc/afp.conf
    
    [Your Share]
    path = /mnt/public/share
    rwlist = nobody
    
## IP Tables

如果你使用 [iptables](<../zh-cn/Iptables.html> "Iptables") 包来做防火墙，可能需要加入下面几行：(如果需要的话，可以用用 `-A` 来 替换掉 `-I`) 
    
    Bonjour/Zeroconf
    
    iptables -I INPUT -p udp --dport mdns -d 224.0.0.251 -j ACCEPT
    iptables -I OUTPUT -p udp --dport mdns -d 224.0.0.251 -j ACCEPT
    
    AFP
    
    iptables -I INPUT -p tcp --dport afpovertcp -j ACCEPT
    
    SLP
    
    iptables -I INPUT -p tcp --dport slp -j ACCEPT
    iptables -I OUTPUT -p tcp --dport slp -j ACCEPT
    iptables -I INPUT -p udp --dport slp -j ACCEPT
    iptables -I OUTPUT -p udp --dport slp -j ACCEPT
    
    AppleTalk
    
    iptables -I INPUT -p tcp -m multiport --dport at-rtmp,at-nbp,at-echo,at-zis -j ACCEPT
    iptables -I OUTPUT -p tcp -m multiport --dport at-rtmp,at-nbp,at-echo,at-zis -j ACCEPT

##  开启 Bonjour/Zeroconf

Bonjour/Zeroconf 是 Netatalk 的必要组件，在默认状况下是编译好了的。不需要额外的配置，Netatalk 就可以使用 dbus 链接来注册服务。 你要确认设置 `-mimicmodel` 为你想要的字符串（查看 Mac 上的 `/System/Library/CoreServices/CoreTypes.bundle/Contents/Info.plist` 来获得一个完整的列表）。 

如果 `avahi-daemon.service` 没有运行的话，可能需要[使用 systemd](<../zh-cn/Systemd.html#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83> "Systemd") 启用或启动该服务。 
