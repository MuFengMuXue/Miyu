**翻译状态：**

  * 本文（或部分内容）译自 [qBittorrent](<https://wiki.archlinux.org/title/qBittorrent> "arch:qBittorrent")，最近一次同步于 2024-01-16，若英文版本有所[更改](<https://wiki.archlinux.org/title/qBittorrent?diff=0&oldid=797201>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/qBittorrent_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[qBittorrent](<https://www.qbittorrent.org/>)是一个用[C++](<../zh-cn/C.html> "C++")、[Qt](<../zh-cn/Qt.html> "Qt")和[Python](<../zh-cn/Python.html> "Python")（可选搜索引擎）编写的开源跨平台[BitTorrent](<../zh-cn/Category:BitTorrent.html> "BitTorrent") 客户端，使用[libtorrent-rasterbar](<https://archlinux.org/packages/?name=libtorrent-rasterbar>)包库。 

它速度快，稳定性高，体积轻，支持unicode并提供集成搜索引擎。它支持UPnP端口转发 / NAT-PMP，加密（与[Vuze](</wzh/index.php?title=Vuze&action=edit&redlink=1> "Vuze（页面不存在）")兼容），FAST扩展（主线）和PeX支持（与[uTorrent](</wzh/index.php?title=UTorrent&action=edit&redlink=1> "UTorrent（页面不存在）")兼容）。 

##  安装

在官方仓库中有两个软件包可以用于[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")qBittorrent： 

  * **qBittorrent** — 具有[Qt](<../zh-cn/Qt.html> "Qt")图形界面和[#Web 界面](<#Web_%E7%95%8C%E9%9D%A2>)。

     <https://github.com/qbittorrent/qBittorrent> || [qbittorrent](<https://archlinux.org/packages/?name=qbittorrent>)包

  * **qBittorrent-nox** — 无图形界面的版本(nox -> no X server)。

     <https://github.com/qbittorrent/qBittorrent> || [qbittorrent-nox](<https://archlinux.org/packages/?name=qbittorrent-nox>)包

##  配置

在第一次运行程序时，配置文件会保存在`~/.config/qBittorrent/qBittorrent.conf`中。 

###  自启动

如果你安装了[qbittorrent-nox](<https://archlinux.org/packages/?name=qbittorrent-nox>)包，你将会得到一个systemd单元模板：`qbittorrent-nox@.service`。 

如果你[启用、启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Help:阅读")`qbittorrent-nox@username.service`，QBittorrent 将以用户 `_username_`运行。参见[[1]](<https://github.com/qbittorrent/qBittorrent/wiki/Running-qBittorrent-without-X-server-\(WebUI-only,-systemd-service-set-up,-Ubuntu-15.04-or-newer\)>)。 

默认的下载文件夹会是该用户的`Downloads`目录。 

**提示：**

  * 如果你把它作为一个可以访问的服务运行，可以[添加一个叫做qbittorrent的用户](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E6%B7%BB%E5%8A%A0%E7%99%BB%E5%BD%95%E7%94%A8%E6%88%B7> "用户和用户组")并让它在那个用户下运行，使得该服务可以在程序退出后重新启动。
  * 要修改设置（例如端口），你可以为它的systemd单元添加一个环境变量（例如端口的变量就是QBT_WEBUI_PORT）。执行`qbittorrent-nox --help`可以查看更多其他的环境变量（此信息在手册中并未给出）。

##  搜索引擎

你可以通过菜单 _视图 > 搜索引擎_启用可选搜索引擎，这将启用 _搜索_ 标签页。 

###  搜索插件

默认的搜索插件可通过下面的操作添加/启用：转到 _搜索_ 标签页，中打开追踪器窗口后通过 _搜索插件..._ （右下角按钮），并点击 _查找更新_ 。 

更多非官方的搜索插件可以在[这里](<https://github.com/qbittorrent/search-plugins/wiki/Unofficial-search-plugins>)找到。 

##  Web 界面

###  默认端口

qBittorrent默认会在所有[接口](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#%E7%BD%91%E7%BB%9C%E6%8E%A5%E5%8F%A3> "网络配置")上的8080端口监听传入连接。因此，你可以通过`<http://HOST_IP:8080>`访问。 

**注意：** HTTPS默认不启用，所以，`<https://HOST_IP:8080>`将无法访问。

###  默认用户名 & 密码

默认用户名为`admin`，在5.0.0版本之前的默认密码为`adminadmin`。版本5.0.0及以上会生成一个只在控制台可见的随机密码，直到手动保存以防止未经授权的访问。有关此更改的更多信息，请查看[这里](<https://github.com/qbittorrent/qBittorrent/pull/19777>)。 

###  允许无用户名&密码访问

在家庭环境下，通常希望能够无需输入用户名和密码就能访问Web UI。这可以在使用默认用户名和密码登录后在Web UI本身中配置。 

或者，为了避免首次登录，可以将以下部分添加到`~/.config/qBittorrent/qBittorrent.conf`中： 
    
    [Preferences]
    WebUI\AuthSubnetWhitelist=192.168.1.0/24
    WebUI\AuthSubnetWhitelistEnabled=true
    WebUI\UseUPnP=false
    
上述配置项将： 

  * 允许从192.168.1.x登录的客户端无需输入用户名和密码即可以访问Web UI。
  * 为Web UI禁用UPnP，这样Web UI将无法从网络外部访问。

然后，[重载](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Help:阅读") `qbittorrent-nox@_用户名_.service`。 

###  反向代理配置

#### nginx

请参考[qbittorrent wiki](<https://github.com/qbittorrent/qBittorrent/wiki/NGINX-Reverse-Proxy-for-Web-UI>)

##  主题

###  非官方主题

  * [如何使用自定义UI主题](<https://github.com/qbittorrent/qBittorrent/wiki/How-to-use-custom-UI-themes>)
  * [已知的qBittorrent主题列表](<https://github.com/qbittorrent/qBittorrent/wiki/List-of-known-qBittorrent-themes>)

##  故障排查

##  另见

  * [qBittorrent官方网站](<https://www.qbittorrent.org/>)
  * [qBittorrent在GitHub的wiki](<https://github.com/qbittorrent/qBittorrent/wiki>)
  * [Wikipedia:qBittorrent](<https://en.wikipedia.org/wiki/qBittorrent> "wikipedia:qBittorrent")
