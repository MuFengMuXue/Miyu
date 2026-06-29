**翻译状态：**

  * 本文（或部分内容）译自 [Jabberd2](<https://wiki.archlinux.org/title/Jabberd2> "arch:Jabberd2")，最近一次同步于 2020-05-21，若英文版本有所[更改](<https://wiki.archlinux.org/title/Jabberd2?diff=0&oldid=614678>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Jabberd2_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[jabberd2](<https://jabberd2.org/>) 是一个 [XMPP](<https://en.wikipedia.org/wiki/XMPP> "wikipedia:XMPP") 服务器，用 C 语言编写，并根据 GNU 通用公共许可作为自由软件许可。它的灵感来自 jabberd14。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [jabberd2](<https://aur.archlinux.org/packages/jabberd2/>)AUR 包。 

##  配置

编辑 `/etc/jabberd/c2s.xml` 并将标记 `<id register-enable='mu'>` 的内容更改为您的域。 

这行将添加您的用户 ID。（如果您将 `example.com` 放在此处，则您的用户 ID 将类似于 `user@example.com`）如果将通过开放的 Internet（而不是 VPN 或 LAN）访问 jabber 服务，则该名称**应由** DNS 解析为您的服务器。 

`register-enable='mu'` 部分允许使用标准的 jabber 客户端注册帐户。 

还要在 `sm.xml` 上设置服务器： 
    
    /etc/jabberd/sm.xml
    
    <id>mymachine.com</id>
    
###  守护进程

配置 `jabberd.service` 以在开机时启动。 

阅读[守护程序](<../zh-cn/Systemd.html> "守护程序")以获取更多信息。 

##  参见

  * [Jabberd2 主页](<https://jabberd2.org/>)
