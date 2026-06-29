**翻译状态：**

  * 本文（或部分内容）译自 [Sslh](<https://wiki.archlinux.org/title/Sslh> "arch:Sslh")，最近一次同步于 2021-04-20，若英文版本有所[更改](<https://wiki.archlinux.org/title/Sslh?diff=0&oldid=663044>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Sslh_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[sslh](<https://www.rutschle.net/tech/sslh/README.html>)是一个ssl/ssh多路复用软件。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Help:Reading")[sslh](<https://archlinux.org/packages/?name=sslh>)包软件包。 

##  配置

软件的默认配置在`/etc/sslh.cfg`文件中，支持`ssh`、`openvpn`、`xmpp`、`http`、`ssl`和`anyprot`协议。 

软件包中还包括2个额外的配置文件： 

  * `/usr/share/doc/sslh/basic.cfg`, 基础配置文件，提供“标准安装”所需要的合理配置。
  * `/usr/share/doc/sslh/example.cfg`, 此配置文件被用作说明文档，其不应当被当做默认配置使用，也不应该在任何生产环境中使用。

##  运行

将`sslh-fork.service`或`sslh-select.service`[设置为开机自启动](<../zh-cn/Systemd.html#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83> "Systemd")。 

`sslh-fork`为每一个新连接创建一个新的进程。`sslh-fork`经过广泛测试，具有良好的可靠性，但会榨干许多处理器的性能。 如果在一个“小环境”下使用`sslh`（只有几个ssh连接的低流量https服务器），使用`sslh-fork`非常合适。 

`sslh-select`只使用一个线程，在同一时间监听所有连接。`sslh-select`功能较新且测试不足，但每个连接最多只使用16字节。当然，如果`sslh-select`停止工作，所有连接都会中止，因此你不能对其远程升级。 如果在一个“中型环境”下使用`sslh`（上千个ssh连接和上千个ssl连接），`sslh-select`更合适。 

如果要在非常大的环境下使用`sslh`（上万个连接），可能需要某些应用了libevent或类似技术的“概念版”软件（译者注：vapourware，又称“雾件”，指发布后从未真正发行的软件，类似于“概念车”）。 

##  参考

[Difference between sslh-fork and sslh-select](<https://github.com/yrutschle/sslh/blob/master/doc/INSTALL.md#binaries>)

[basic.cfg](<https://github.com/yrutschle/sslh/blob/master/basic.cfg>)

[example.cfg](<https://github.com/yrutschle/sslh/blob/master/example.cfg>)
