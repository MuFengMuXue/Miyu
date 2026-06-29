**翻译状态：**

  * 本文（或部分内容）译自 [Yabsnap](<https://wiki.archlinux.org/title/Yabsnap> "arch:Yabsnap")，最近一次同步于 2024-08-16，若英文版本有所[更改](<https://wiki.archlinux.org/title/Yabsnap?diff=0&oldid=814606>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Yabsnap_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Btrfs](<../zh-cn/Btrfs.html> "Btrfs")
  * [Snapper](<../zh-cn/Snapper.html> "Snapper")

[Yabsnap](<https://github.com/hirak99/yabsnap>) 是一个为 Arch 编写的、用于 [Btrfs](<../zh-cn/Btrfs.html> "Btrfs") 分区的定时快照管理器。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [yabsnap](<https://aur.archlinux.org/packages/yabsnap/>)AUR 软件包，开发版本可以通过 [yabsnap-git](<https://aur.archlinux.org/packages/yabsnap-git/>)AUR 安装。 

##  配置

运行以下命令将会创建一个配置文件： 
    
    # yabsnap create-config _configname_
    
此命令会在 `/etc/yabsnap/configs/_configname_.conf` 生成配置文件。编辑该文件，修改以下内容： 

  * `source` \- 子卷挂载点。例如 `/home`。
  * `dest_prefix` \- 快照名称的完整路径及前缀。例如，`/.snapshot/@home-` 会创建如下格式的备份快照：`/.snapshot/@home-20230525120000`。

您还可以编辑其他参数，以指定何时触发或清理备份。 

##  主要命令

###  查看快照

要查看现有的快照，执行： 
    
    $ yabsnap list
    
###  创建快照

要为所有已有配置创建快照，执行: 
    
    # yabsnap create --comment 'COMMENT'
    
您也可以单独地为已挂载子卷创建快照， Yabsnap 会自动地找到相应的配置。执行： 
    
    # yabsnap --source '/home' create --comment 'COMMENT'
    
##  清理或删除快照

###  自动清理

根据 `/etc/yabsnap/configs/*.conf` 中的配置，Yabsnap 会自动删除超出上限的旧快照。 

###  删除快照

也可以手动删除快照。 

指定完整路径以删除特定的快照： 
    
    # yabsnap delete /.snapshots/@home-20230525120000
    
指定时间戳可删除所有匹配的同时拍摄的快照： 
    
    # yabsnap delete 20230525120000
    
##  回滚

###  回滚注意事项：使用 subvol 而不是 subvolid 挂载

建议使用 subvol 而不是 subvolid 来挂载所有的 btrfs 子卷。 

例如使用下列 [fstab](<../zh-cn/Fstab.html> "Fstab") 条目： 
    
    UUID=[YOUR_UUID] / btrfs rw,noatime,ssd,space_cache=v2,compress=zstd,subvol=/@ 0 0
    
**注意：** 使用的挂载选项是 `subvol=/@`。**不要** 使用 `subvolid=`。

这样做的原因是该回滚机制不会修改您的 fstab 文件，它只会确保正确的快照挂载在相应的位置。（如果使用`subvolid`，那么会挂载原来的子卷） 

###  回滚操作

回滚命令是安全的（因为并未执行任何修改操作），直到执行其生成的脚本。 

此命令将生成一个回滚脚本，请将时间戳更改为现有的某个快照： 
    
    $ yabsnap rollback-gen 20230525081049 | tee ~/rollback.sh
    
只有运行该脚本才会执行真正的回滚操作。因此建议在回滚之前先检查生成的命令。 

检查完生成的回滚脚本后，将其设为[可执行](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "可执行")，然后运行： 
    
    # ~/rollback.sh
    
此操作将回滚前述指定时间戳的所有快照。 

##  与 Snapper 的比较

Yabsnap 是为了克服 [Snapper](<../zh-cn/Snapper.html> "Snapper") 的某些不足而创立。具体而言，它可以做一些 Snapper 难以或无法完成的任务（截至撰写本文时）： 

  * 自定义备份目的路径 [(issue)](<https://github.com/openSUSE/snapper/issues/54>)，
  * 对所有已配置的快照进行回滚（而不仅仅是默认子卷）
  * 集成了 [pacman hook](<../zh-cn/Pacman_hook.html> "Pacman hook") 支持。

##  参见

  * [Yabsnap github 页面](<https://github.com/hirak99/yabsnap>)
