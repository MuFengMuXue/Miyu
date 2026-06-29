**翻译状态：**

  * 本文（或部分内容）译自 [PPTP Server](<https://wiki.archlinux.org/title/PPTP_Server> "arch:PPTP Server")，最近一次同步于 2012-10-19，若英文版本有所[更改](<https://wiki.archlinux.org/title/PPTP_Server?diff=0&oldid=229578>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/PPTP_Server_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-preferences-desktop-locale-modified.png)](<../File:Tango-preferences-desktop-locale-modified.png>)**这篇文章或章节的[翻译](<../Project:%E8%B4%A1%E7%8C%AE.html#Translating> "Project:Contributing")质量不佳。**

**原因：** Still references `rc.d`.（在 [Talk:PPTP server#](<../zh-cn/Talk:PPTP_server.html>) 中讨论）

点对点隧道协议(PPTP)是一种实现虚拟专用网(VPN)的方法。PPTP 在TCP之上使用一个控制通道和 GRE 隧道操作加密 PPP 数据包。 

本条目说明如何在 Arch 中创建 PPTP 服务器。 

##  安装

[安装](<../zh-cn/Pacman.html> "Pacman")位于[官方软件仓库](<../zh-cn/Official_repositories.html> "Official repositories")的软件包[pptpd](<https://archlinux.org/packages/?name=pptpd>)包。 

##  配置

然后编辑文件`/etc/pptpd.conf`
    
    /etc/pptpd.conf
    
    option /etc/ppp/pptpd-options
    localip 172.16.36.1
    remoteip 172.16.36.2-254
    
接着编辑文件`/etc/ppp/pptpd-options`
    
    /etc/ppp/pptpd-options
    
    name pptpd
    refuse-pap
    refuse-chap
    refuse-mschap
    require-mschap-v2
    require-mppe-128
    proxyarp
    lock
    nobsdcomp
    novj
    novjccomp
    nologfd
    ms-dns 8.8.8.8
    ms-dns 8.8.4.4
    
在 `/etc/ppp/chap-secrets`中添加用户名和密码： 
    
    /etc/ppp/chap-secrets
    
    <username>     pptpd     <password>   *
    
在 `/etc/sysctl.d/99-sysctl.conf`中启用IP转发： 
    
    /etc/sysctl.d/99-sysctl.conf
    
    net.ipv4.ip_forward=1

应用 sysctl.conf 修改： 
    
    # sysctl --system
    
###  iptables 防火墙配置

配置 iptables 设置，允许 PPTP 客户端访问： 
    
    iptables -A INPUT -i ppp+ -j ACCEPT
    iptables -A OUTPUT -o ppp+ -j ACCEPT
    
    iptables -A INPUT -p tcp --dport 1723 -j ACCEPT
    iptables -A INPUT -p 47 -j ACCEPT
    iptables -A OUTPUT -p 47 -j ACCEPT
    
    iptables -F FORWARD
    iptables -A FORWARD -j ACCEPT
    
    iptables -A POSTROUTING -t nat -o eth0 -j MASQUERADE
    iptables -A POSTROUTING -t nat -o ppp+ -j MASQUERADE
    
使用下面命令保存新的 iptables 规则： 
    
    # rc.d save iptables
    
systemd 用户需要使用： 
    
    # iptables-save > /etc/iptables/iptables.rules
    
阅读 [Iptables](<../zh-cn/Iptables.html> "Iptables") 条目获得更多信息。 

###  ufw 防火墙配置

在 `/etc/default/ufw`中，修改默认的转发规则 
    
    /etc/default/ufw
    
    DEFAULT_FORWARD_POLICY=”ACCEPT”

修改`/etc/ufw/before.rules`，添加如下配置到 *filter 之前 
    
    /etc/ufw/before.rules
    
    # nat Table rules
    *nat
    :POSTROUTING ACCEPT [0:0]
    
    # Allow traffic from clients to eth0
    -A POSTROUTING -s 172.16.36.0/24 -o eth0 -j MASQUERADE
    
    # don.t delete the .COMMIT. line or these nat table rules won.t be processed
    COMMIT
    
代开端口 1723： 
    
    ufw allow 1723
    
重启ufw 
    
    ufw disable
    ufw enable
    
##  启动

pptpd 软件包已经提供了 service 文件. 

启动服务： 
    
    # systemctl start pptpd.service
    
开机自动启动： 
    
    # systemctl enable pptpd.service
    