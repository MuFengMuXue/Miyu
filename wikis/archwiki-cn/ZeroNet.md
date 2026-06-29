**翻译状态：**

  * 本文（或部分内容）译自 [ZeroNet](<https://wiki.archlinux.org/title/ZeroNet> "arch:ZeroNet")，最近一次同步于 2017-08-01，若英文版本有所[更改](<https://wiki.archlinux.org/title/ZeroNet?diff=0&oldid=483448>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/ZeroNet_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** Not updated for a while, still references python2.（在 [Talk:ZeroNet#](<../zh-cn/Talk:ZeroNet.html>) 中讨论）

[ZeroNet](<https://zeronet.io/>) 可以“利用比特币加密和 BitTorrent 网络创建公开、自由和不受审查的网站”。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [zeronet](<https://aur.archlinux.org/packages/zeronet/>)AUR 软件包。 

最新的开发版是 [zeronet-git](<https://aur.archlinux.org/packages/zeronet-git/>)AUR 包。 

##  配置

###  启动

启动 ZeroNet ：[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start/enable") `zeronet.service`。 

### Tor

默认情况下，ZeroNet 使用 clearnet 和 Tor（如果可用）。要启用对 Tor 的支持需要安装 [Tor](<../zh-cn/Tor.html> "Tor")（[tor](<https://archlinux.org/packages/?name=tor>)包）。然后执行下列命令让 ZeroNet 使用 Tor ： 
    
    # usermod -a -G tor zeronet
    # mkdir -m 750 /var/lib/tor-auth
    # chown tor:tor /var/lib/tor-auth
    
在 `/etc/tor/torrc` 中[添加](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Append")下列行： 
    
    ControlPort 9051
    CookieAuthentication 1
    CookieAuthFileGroupReadable 1
    CookieAuthFile /var/lib/tor-auth/control_auth_cookie
    
##  创建 ZeroNet 站点

所有操作，包括 ZeroNet 站点文件的编辑，都应该以 `zeronet` 用户执行。使用 `--config_file` 选项可以指定要使用的配置文件。`/var/lib/zeronet` 中默认的数据文件目录是`/var/lib/zeronet`。示例: 
    
    $ sudo -u zeronet python2 zeronet.py --config_file /etc/zeronet.conf
    
或 
    
    $ sudo su - zeronet
    $ cd /opt/zeronet
    $ python2 zeronet.py --config_file /etc/zeronet.conf
    
创建的站点的初始数据位于 `/var/lib/zeronet/[address]` 中，关于创建 Zeronet 站点的更多信息，请阅读 [Zeronet FAQ](<https://zeronet.readthedocs.io/en/latest/using_zeronet/create_new_site/>). 

##  参阅

  * [ZeroNet 文档](<https://zeronet.readthedocs.io/en/latest/>)
