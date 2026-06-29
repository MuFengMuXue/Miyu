**翻译状态：**

  * 本文（或部分内容）译自 [Powerpill](<https://wiki.archlinux.org/title/Powerpill> "arch:Powerpill")，最近一次同步于 2023-02-18，若英文版本有所[更改](<https://wiki.archlinux.org/title/Powerpill?diff=0&oldid=736120>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Powerpill_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 本页是在 pacman 原生支持并行下载之前编写的，并且应该提到，由于 pacman v6 版本，这不再是一次下载多个软件包的唯一选项。 (在[Talk:Powerpill](<../zh-cn/Talk:Powerpill.html>)讨论)

[Powerpill](<https://xyne.dev/projects/powerpill/>) 是一个 [pacman](<../zh-cn/Pacman.html> "Pacman") 包装，它使用并行和分段下载来加速 Pacman 的下载。内部使用 [Aria2](<../zh-cn/Aria2.html> "Aria2") 和 [Reflector](<../zh-cn/Reflector.html> "Reflector") 来实现这一点。Powerpill 还可以将 [rsync](<../zh-cn/Rsync.html> "Rsync") 用于支持它的官方镜像。对于从单镜像下载时已经使用全部带宽的用户来说非常有效。配置文件也支持 [Pacserve](</wzh/index.php?title=Pacserve&action=edit&redlink=1> "Pacserve（页面不存在）")，并将在从外部镜像下载之前使用。示例：有人想要更新然后运行了 `pacman -Syu`，它返回一个包含20个包的列表用于更新，总计200兆。如果用户通过 pacman 下载，它们将一次下载一个。如果用户通过 powerpill 下载，它们将同时下载，许多情况下所需时间会下降几倍（取决于一个人的连接速度、服务器上软件包的可用性以及服务器/负载的速度等。） 

在一个系统上对 pacman 和 powerpill 进行的对比测试表明，在上述场景中，pacman 的下载速度平均为 300 kB/sec，powerpill 的下载速度平均为 1.2 MB/sec，速度提高了4倍。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [powerpill](<https://aur.archlinux.org/packages/powerpill/>)AUR 软件包。 

##  配置

Powerpill 有一个单独配置文件 `/etc/powerpill/powerpill.json`，你可以按喜好进行编辑。参考 [powerpill.json(1)](<https://xyne.dev/projects/powerpill/#powerpill.json1>) 手册页获取详细信息。 

##  使用 Reflector

默认情况下，Powerpill 配置为使用 [Reflector](<../zh-cn/Reflector.html> "Reflector") 从 Arch Linux 服务器的 web API 检索当前镜像列表，并将其用于并行下载。这是为了确保列表中有足够的服务器以显著提高速度。 

##  使用 rsync

一些镜像可以支持 [Rsync](<../zh-cn/Rsync.html> "Rsync")。在启用后，因为使用单连接，数据库同步 (`pacman -Sy`) 和其它操作可能会快得多。rsync 协议本身也加速了更新检查，有时还加速了文件传输。 

要找到支持 rsync 的镜像，使用 `reflector`: 
    
    $ reflector -p rsync
    
另外，你可以使用标志 `-f _n_` 以获得 `_n_` 个最快的服务器，和使用标志 `-l _m_` 以获得 `_m_` 个最新同步的服务器： 
    
    $ reflector -p rsync -f _n_ -l _m_
    
选择你想使用的镜像。`-c` 选项可以按国家进行筛选（使用 `reflector --list-countries` 查看全部列表，在名称周围加引号并注意大小写！）。完成后，编辑 `/etc/powerpill/powerpill.json`，向下滚动到 `rsync` 部分，并向 servers 字段添加任意数量的服务器。 

之后，所有官方数据库和软件包将尽可能从 rsync 服务器下载。 

注意，需要检查数据库和包是否位于带 reflector 的官方存储库中，因此安装 [reflector](<../zh-cn/Reflector.html> "Reflector") 是 rsync 功能运行所必需的。 

##  基本使用

对于大多数操作， _powerpill_ 与 pacman 的工作方式差不多，因为它是 _pacman_ 的包装脚本。 

###  系统更新

想要使用 powerpill 更新你的系统（同步并更新所有安装的包），和 _pacman_ 一样使用菜单项 `-Syu`: 
    
    # powerpill -Syu
    
###  安装软件包

想要安装软件包和它的依赖，和 _pacman_ 一样使用菜单项 `-S`: 
    
    # powerpill -S _package_
    
安装多个软件包时也和使用 _pacman_ 一样： 
    
    # powerpill -S _package1_ _package2_ _package3_
    
##  疑难解答

如果你得到 <repo>.db.sig 文件的 [err]: 
    
       b5d7d7|ERR |       0B/s|/var/lib/pacman/sync/extra.db.sig
       899e91|ERR |       0B/s|/var/lib/pacman/sync/multilib.db.sig
       8fcc32|ERR |       0B/s|/var/lib/pacman/sync/core.db.sig
       85eb3d|ERR |       0B/s|/var/lib/pacman/sync/community.db.sig
    
这是因为该存储库缺少签名文件，而且你还没有在 `/etc/pacman.conf` 中显式设置 
    
    SigLevel = PackageRequired

，更多说明请见这个[帖子](<https://bbs.archlinux.org/viewtopic.php?pid=1254940#p1254940>)。 

##  参考

  * [Powerpill](<https://xyne.dev/projects/powerpill/>) \- 项目官方页面
  * [powerpill reborn](<https://bbs.archlinux.org/viewtopic.php?id=153818>) \- powerpill is back :)
