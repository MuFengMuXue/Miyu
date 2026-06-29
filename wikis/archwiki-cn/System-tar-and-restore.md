**翻译状态：**

  * 本文（或部分内容）译自 [System-tar-and-restore](<https://wiki.archlinux.org/title/System-tar-and-restore> "arch:System-tar-and-restore")，最近一次同步于 2020-05-14，若英文版本有所[更改](<https://wiki.archlinux.org/title/System-tar-and-restore?diff=0&oldid=612763>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/System-tar-and-restore_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

**System-tar-and-restore** 包含两个 bash 脚本，即主程序 **star.sh** 和 gui 包装器 **star-gui.sh** 。三种模式可用： 

  * **Backup** ：使用此模式，您可以为系统创建 tar 备份档案。

  * **Restore/Transfer** ：还原模式使用以上创建的存档将其提取到所需分区中。传输模式使用 [rsync](<https://archlinux.org/packages/?name=rsync>)包 在所需分区中传输系统。然后，在两种情况下，脚本都会生成目标系统的 fstab，为每个可用内核重建 initramfs，生成语言环境，最后安装并配置选定的引导加载程序。

如果您打算使用 gui，请安装 [gtkdialog](<https://aur.archlinux.org/packages/gtkdialog/>)AUR。 

##  安装

安装 [system-tar-and-restore](<https://aur.archlinux.org/packages/system-tar-and-restore/>)AUR。 

##  使用

请参阅[自述文件](<https://github.com/tritonas00/system-tar-and-restore/blob/master/README.md>)。 
