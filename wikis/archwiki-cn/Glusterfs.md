相关文章

  * [Ceph](<../zh-cn/Ceph.html> "Ceph")

**翻译状态：**

  * 本文（或部分内容）译自 [Glusterfs](<https://wiki.archlinux.org/title/Glusterfs> "arch:Glusterfs")，最近一次同步于 2023-10-10，若英文版本有所[更改](<https://wiki.archlinux.org/title/Glusterfs?diff=0&oldid=729652>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Glusterfs_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Glusterfs](<https://www.gluster.org/>) 是一个可扩展的网络[文件系统](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html> "文件系统")。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [glusterfs](<https://archlinux.org/packages/?name=glusterfs>)包 包。 

##  配置

根据不同需求，可按照多种不同方式配置 Glusterfs，包括分布式以及完全复制。下列示例创建了两个完全复制的服务器节点 gluster1 及 gluster2，各包含两个磁盘，其中 `sda` 用于操作系统，另一个磁盘 `sdb` 用于 Glusterfs。除非有特别说明，所有操作都在 glusterfs1 上执行： 

  * 在各台服务器上[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `glusterd.service` 服务。

  * 链接两台服务器

     # gluster peer probe gluster2
    
  * 在各服务器上分区并格式化 glusterfs 磁盘 
    * 上游建议在磁盘上创建单一的 [XFS](<../zh-cn/XFS.html> "XFS") 分区

  * 在各服务器的 `/etc/fstab` 中[添加](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Append")如下内容以自动挂载磁盘，其中 `/dev/sd _XY_` 为对应的磁盘分区（例如 `/dev/sdb1`）。

    /etc/fstab
    
    /dev/sd _XY_ /export/sd _XY_ xfs defaults 0 0

  * 在各服务器上[挂载](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html#%E6%8C%82%E8%BD%BD%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "挂载")磁盘，并创建 _brick_ 文件夹：

     # mkdir -p /export/sd _XY_ /brick
    
  * 在主服务器上启用复制

     # gluster volume create gv0 replica 2 gluster1.mydomain.net:/export/sdb1/brick gluster2.mydomain.net:/export/sdb1/brick
    
  * 确认卷是否正确创建

     # gluster volume info
    
  * 启动卷

     # gluster volume start gv0
    
  * 挂载卷

     # mkdir -p /mnt/glusterClientMount
     # mount -t glusterfs gluster1:/gv0 /mnt/glusterClientMount
    
##  启动时自动挂载 gluster 卷

要在启动时挂载 gluster 卷，systemd 需要等待网络正常及 `glusterd` 服务启动。可以在 fstab 中添加如下选项： 
    
    /etc/fstab
    
    localhost:/gv0 /mnt/glusterClientMount glusterfs defaults,_netdev,x-systemd.requires=glusterd.service,x-systemd.automount 0 0

##  参考

  * [glusterfs 官方安装手册](<https://docs.gluster.org/en/latest/Install-Guide/Overview/>)
  * [关于如何在 Arch Linux 安装 Glusterfs 的博客文章](<https://blog.bastelfreak.de/2016/05/short-tip-setup-glusterfs-share-on-arch-linux/>)
