**翻译状态：**

  * 本文（或部分内容）译自 [Emby](<https://wiki.archlinux.org/title/Emby> "arch:Emby")，最近一次同步于 2020-07-25，若英文版本有所[更改](<https://wiki.archlinux.org/title/Emby?diff=0&oldid=626777>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Emby_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Emby](<https://emby.media/>) 是一个个人媒体服务器，它具有许多平台的客户端。它用于组织个人家庭媒体，以及在其他设备上播放。社区支持大量的频道，甚至可以与PVR和Tuner卡一起使用以远程提供电视流。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [emby-server](<https://archlinux.org/packages/?name=emby-server>)包 软件包。 

##  用法

[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")并[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `emby-server.service`。 

导航到 <http://localhost:8096/> ，通过浏览器访问 Emby。 

##  写入权限

Emby 使用 systemd 的 DynamicUser 功能在[用户](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html> "用户")和[用户组](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E7%94%A8%E6%88%B7%E7%BB%84%E7%AE%A1%E7%90%86> "用户组") `emby` 下运行。默认情况下，由于 systemd 的文件系统抽象，Emby 最多具有对媒体文件的读取权限。 

（可选）您可能要授予 emby 写入权限并启用媒体删除或本地元数据保存。 为此，您可以扩展 systemd 服务： 
    
    /etc/systemd/system/emby-server.service.d/write-permissions.conf
    
    [Service]
    SupplementaryGroups=share
    ReadWritePaths=/mnt/share

这会将 `emby` 用户添加到 `share` 组，并通过 systemd 启用对 `/mnt/share` 目录的写权限。请注意，您仍然需要确保 `share` 组对实际目录具有写权限。 
