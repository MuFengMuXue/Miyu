相关文章

  * [find](<../zh-cn/%E6%A0%B8%E5%BF%83%E5%B7%A5%E5%85%B7.html#%E5%9F%BA%E7%A1%80> "Find")
  * [核心工具](<../zh-cn/%E6%A0%B8%E5%BF%83%E5%B7%A5%E5%85%B7.html> "核心工具")
  * [应用程序列表/工具#文件搜索](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E5%B7%A5%E5%85%B7.html#%E6%96%87%E4%BB%B6%E6%90%9C%E7%B4%A2> "应用程序列表/工具")

**翻译状态：**

  * 本文（或部分内容）译自 [locate](<https://wiki.archlinux.org/title/locate> "arch:locate")，最近一次同步于 2025-03-02，若英文版本有所[更改](<https://wiki.archlinux.org/title/locate?diff=0&oldid=825890>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/locate_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

_locate_ （即 _定位_ ）是一种常用的 Unix 工具，用于通过文件名快速查找文件。与 [find](<../zh-cn/%E6%A0%B8%E5%BF%83%E5%B7%A5%E5%85%B7.html#%E5%9F%BA%E7%A1%80> "Find") 工具相比， _locate_ 通过搜索预先构建的数据库文件，而不是直接搜索[文件系统](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html> "文件系统")，提高了查找速度。这种方法的缺点是，`locate` 无法检测到数据库文件生成后的更改。通过按计划更新数据库，可以将这一问题降至最低。 

随着时间的推移，各种替代实现经历了迭代更替：从仅显示用户可访问文件的 slocate（secure locate，安全定位），到每次更新时合并数据库的 [mlocate](<https://pagure.io/mlocate>)（merging locate，合并定位）——这种合并机制通过跳过已检查文件实现了性能提升，再到如今基于[倒排列表](<https://en.wikipedia.org/wiki/Inverted_index> "wikipedia:Inverted index")构建的 [plocate](<https://plocate.sesse.net/>)（posting locate，列表定位），它通过预先处理数据库生成速度更快、体积更小的索引。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [plocate](<https://archlinux.org/packages/?name=plocate>)包 软件包。它提供了 `plocate`、`updatedb`、`plocate-build` 等命令以及指向 `plocate` 的符号链接 `locate`、`mlocate`。 

虽然 [GNU findutils](<https://www.gnu.org/software/findutils/>) 也包含 _locate_ 实现，但 Arch 的 [findutils](<https://archlinux.org/packages/?name=findutils>)包 软件包并不包含。 

[LS-Shandong](<../User:RivuletCedar.html> "User:LS-Shandong") 维护了一个 [plocate 分叉](<https://codeberg.org/LS-Shandong/plocate>)，这个分叉包含了 [Steinar](<https://www.sesse.net/>) 正考虑合并入官方 plocate 的 i18n 支持及软件的[简体中文](<../zh-cn/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87%E6%9C%AC%E5%9C%B0%E5%8C%96.html> "简体中文本地化")翻译和手册页翻译。安装 [plocate-enhanced-git](<https://aur.archlinux.org/packages/plocate-enhanced-git/>)AUR 软件包以获取它。 

##  用法

在使用 [plocate(1)](<https://man.archlinux.org/man/plocate.1>) 之前，需要先创建数据库，这可以通过 [updatedb(8)](<https://man.archlinux.org/man/updatedb.8>) 命令完成，顾名思义，该命令用于更新数据库。 

[plocate](<https://archlinux.org/packages/?name=plocate>)包 包含一个 `plocate-updatedb.timer` 单元，每天都会调用数据库更新，安装时已[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")。如果想在重启前使用，请手动启动[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")。您也可以随时以根用户身份手动运行 _updatedb_ 。 

为节省时间，（默认情况下）可以通过编辑 `/etc/updatedb.conf` 配置 _updatedb_ 忽略某些文件系统和路径。[updatedb.conf(5)](<https://man.archlinux.org/man/updatedb.conf.5>) 介绍了该文件的语义。值得注意的是，默认配置（`PRUNEPATHS`）中忽略的路径包括 `/media` 和 `/mnt`，因此 _locate_ 可能无法发现外部设备上的文件。 

##  问题解决

### Btrfs

默认配置会阻止结果中包含 [Btrfs](<../zh-cn/Btrfs.html> "Btrfs") 文件系统。要允许包含 btrfs 挂载点，请添加 
    
    /etc/updatedb.conf
    
    PRUNE_BIND_MOUNTS = "no"

当然，这也意味着其他绑定挂载点也会被包含在内。如果需要排除这些挂载点，可以使用同一配置文件中的 `PRUNEPATHS` 设置。 

##  参见

  * [How locate works and rewrite it in one minute](<https://jvns.ca/blog/2015/03/05/how-the-locate-command-works-and-lets-rewrite-it-in-one-minute/>)
  * [plocate 官方网站](<https://plocate.sesse.net/>)
