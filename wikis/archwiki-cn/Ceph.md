相关文章

  * [Glusterfs](<../zh-cn/Glusterfs.html> "Glusterfs")

**翻译状态：**

  * 本文（或部分内容）译自 [Ceph](<https://wiki.archlinux.org/title/Ceph> "arch:Ceph")，最近一次同步于 2023-10-10，若英文版本有所[更改](<https://wiki.archlinux.org/title/Ceph?diff=0&oldid=765374>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Ceph_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

Ceph 是一个专注于分布式的、弹性可扩展的、高可靠的、性能优异的存储系统平台，可用于为[虚拟机](<https://en.wikipedia.org/wiki/Virtual_Machine> "wikipedia:Virtual Machine")提供块存储方案或通过 [FUSE](<../zh-cn/FUSE.html> "FUSE") 提供常规的文件系统。Ceph 是个高度可配置的系统，管理者可以控制系统的各个方面。它提供了一个命令行界面用于监视和控制其存储集群。Ceph 也包含鉴证和授权功能，可兼容多种存储网关接口，如 [OpenStack Swift](<https://en.wikipedia.org/wiki/OpenStack#Swift> "wikipedia:OpenStack") 和 [Amazon S3](<https://en.wikipedia.org/wiki/Amazon_S3> "wikipedia:Amazon S3")。 

引自 [Wikipedia: Ceph (software)](<https://en.wikipedia.org/wiki/Ceph_\(software\)> "wikipedia:Ceph \(software\)"): 

    Ceph 是一个自由的存储平台软件，设计用于使用单个分布式计算机集群提供对象/块及文件存储服务。Ceph 的主要目标为：无单点故障的完全分布式结构，艾子节级的可扩展性以及获取自由。The data is replicated, making it fault tolerant.

引自 [Ceph.com](<https://ceph.com/>): 

    Ceph 是一个针对高性能、高可靠性及可扩展性设计的分布式对象存储及文件存储系统。

**警告：**

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 根据 <https://docs.ceph.com/en/pacific/install/> ，ceph-deploy 已不再被继续维护，目前推荐使用 Cephadm 和 Rook 进行安装 (在[Talk:Ceph](<../zh-cn/Talk:Ceph.html>)讨论)

推荐使用[官方部署工具](<https://github.com/ceph/ceph-deploy>)安装 Ceph 。该工具通过 [SSH](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH") 连接到目标机器并自动完成安装、配置和系统管理。官方部署工具(ceph-deploy)目前尚不支持 [Arch Linux](<../zh-cn/Arch_Linux.html> "Arch Linux") ，不能使用[快速安装方式](<https://docs.ceph.com/docs/master/start/>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2020-12-20 ⓘ] 部署，只能按官方文档[手工部署](<https://docs.ceph.com/docs/master/install/manual-deployment/>)。因此本文目前仅介绍手工部署方法。 

The official documentation [states](<https://docs.ceph.com/docs/master/install/#deploy-a-cluster-manually>) "the manual procedure is primarily for exemplary purposes for those developing deployment scripts with Chef, Juju, Puppet, etc.". 

##  术语

**提示：**[官方文档](<https://docs.ceph.com/docs/master/glossary/>)提供了完整的术语表

  * **Client** : 连接到 Ceph 集群获取数据，但不属于 Ceph 集群中一部分的模块。
  * **MONs** : 即监视器，存放了集群状态及例如服务和数据位置等集群信息。
  * **MDSs** : 即元数据服务器，为 Ceph 文件系统存储元数据，以减轻存储集群的负载（例如`ls` 等命令所需的信息）。
  * **Node** : 运行如 OSDs 及 MONs 等 Ceph 服务的单台设备。
  * **OSDs** : 即 OSD daemons，负责集群的数据存储工作，也同时负责多项其它任务，例如数据复制，恢复及重平衡。
  * **Storage cluster** : 负载数据存储的核心软件（OSDs+MONs）。

##  安装

###  软件包

可以安装 [ceph](<https://aur.archlinux.org/packages/ceph/>)AUR。如果愿意冒险，也可以安装开发版的 [ceph-git](<https://aur.archlinux.org/packages/ceph-git/>)AUR。 

存储集群的所有节点都要安装 [ceph](<https://aur.archlinux.org/packages/ceph/>)AUR。 

###  NTP 客户端

**警告：** 应当同步监视器节点的时钟以避免[时钟偏移](<../zh-cn/%E7%B3%BB%E7%BB%9F%E6%97%B6%E9%97%B4.html#%E6%97%B6%E9%92%9F%E5%81%8F%E7%A7%BB> "系统时间")，否则将导致集群性能下降甚至停止工作。[官方文档](<https://docs.ceph.com/docs/master/rados/configuration/mon-config-ref/#clock:>)建议所有节点都应采取某种方式同步时钟。

在节点上安装并运行时钟同步客户端，可参阅[时钟同步](<../zh-cn/%E7%B3%BB%E7%BB%9F%E6%97%B6%E9%97%B4.html#%E6%97%B6%E9%92%9F%E5%90%8C%E6%AD%A5> "系统时间")。 

##  启动一个存储集群

在使用存储集群前，需要先使用标识符和密钥初始化集群的监视器。 

Ceph 的上游文档非常完善，且适用于最新版本。 

要初始化存储集群，请参考[官方手动部署指南](<https://docs.ceph.com/docs/master/install/manual-deployment/#monitor-bootstrapping>)中的步骤。 

###  启动一个监视器

鉴于你所用的系统很可能使用了 [systemd](<../zh-cn/Systemd.html> "Systemd")，你可以通过 systemd 单元启用监视器。 

举个例子，对于名称为 `node1` 的监视器，可以按[Systemd#使用单元](<../zh-cn/Systemd.html#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83> "Systemd")中的描述启动并启用 `ceph-mon@node1.service`。 

##  参阅

  * 官方网站 
    * [主页](<https://ceph.com>)
    * [文档](<https://docs.ceph.com/docs/master/>)
  * 官方源码下载 
    * [GitHub organization](<https://github.com/ceph>)
    * [Ceph](<https://github.com/ceph/ceph>)

  * [Ceph中国社区](<http://ceph.org.cn/>)
