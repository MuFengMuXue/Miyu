**翻译状态：**

  * 本文（或部分内容）译自 [Webmin](<https://wiki.archlinux.org/title/Webmin> "arch:Webmin")，最近一次同步于 2020-07-21，若英文版本有所[更改](<https://wiki.archlinux.org/title/Webmin?diff=0&oldid=626225>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Webmin_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

来自项目[主页](<https://www.webmin.com/>)： 

    Webmin 是用于 Unix 的系统管理的基于 Web 的界面。使用任何现代的 Web 浏览器，您都可以设置用户帐户，Apache，DNS，文件共享等等。Webmin 消除了手动编辑 Unix 配置文件（如 `/etc/passwd`）的需要，并允许您从控制台或远程管理系统。请参阅[标准模块](<https://www.webmin.com/standard.html>)页面以获取 Webmin 内置的所有功能的列表，或查看[屏幕截图](<https://www.webmin.com/demo.html>)。

##  安装

从 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [webmin](<https://aur.archlinux.org/packages/webmin/>)AUR 软件包。 

##  配置

要允许从远程计算机访问 Webmin，请将防火墙配置为允许访问 TCP 端口 10000。您可能希望将防火墙配置为仅限制对某些 IP 地址的访问。 

###  更改端口

要更改端口，请在 `/etc/webmin/miniserv.conf` 文件中编辑 `port` 变量。 
    
    /etc/webmin/miniserv.conf
    
    [...]
    port=10000
    [...]

###  （仅）绑定到 localhost

要（仅）将 Webmin 绑定到 `localhost`，请将以下行添加到 `/etc/webmin/miniserv.conf` 文件中。 
    
    /etc/webmin/miniserv.conf
    
    bind=127.0.0.1

##  用法

[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `webmin.service` 或[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")它（如果您希望在引导时加载 webmin）。 

在 Web 浏览器中，输入端口号为 10000 的服务器的 https 地址以访问 Webmin： 
    
    https://_host_ :10000
    
您将需要输入运行 Webmin 的服务器的 root 密码才能使用 Webmin 界面并管理服务器。 
