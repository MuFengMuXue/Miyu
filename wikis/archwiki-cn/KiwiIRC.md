**翻译状态：**

  * 本文（或部分内容）译自 [KiwiIRC](<https://wiki.archlinux.org/title/KiwiIRC> "arch:KiwiIRC")，最近一次同步于 2020-05-05，若英文版本有所[更改](<https://wiki.archlinux.org/title/KiwiIRC?diff=0&oldid=610912>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/KiwiIRC_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[KiwiIRC](<https://kiwiirc.com>) 是您可以享受的手工制作的IRC客户端。专为轻松自由使用而设计。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [kiwiirc](<https://aur.archlinux.org/packages/kiwiirc/>)AUR 包。 

##  运行

### Apache

创建 Apache 配置文件： 
    
    /etc/httpd/conf/extra/kiwiirc.conf
    
    Alias /kiwiirc "/usr/share/webapps/kiwiirc"
    <Directory "/usr/share/webapps/kiwiirc">
        AllowOverride All
        Options FollowSymlinks
        Require all granted
    </Directory>

并将其包含在 `/etc/httpd/conf/httpd.conf`： 
    
    # kiwiirc configuration
    Include conf/extra/kiwiirc.conf
    
更改 Apache 配置文件后，[重新启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重新启动") `httpd.service`。 

### Lighttpd

配置 [Lighttpd](<../zh-cn/Lighttpd.html> "Lighttpd")，确保 `mod_alias` 已启用 

将 kiwiirc 的以下别名添加到配置中： 
    
     alias.url = ( "/kiwiirc" => "/usr/share/webapps/kiwiirc/")
    