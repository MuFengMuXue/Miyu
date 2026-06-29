相关文章

  * [Ext4](<../zh-cn/Ext4.html> "Ext4")
  * [Btrfs](<../zh-cn/Btrfs.html> "Btrfs")
  * [fstab](<../zh-cn/Fstab.html> "Fstab")

**翻译状态：**

  * 本文（或部分内容）译自 [Fsck](<https://wiki.archlinux.org/title/Fsck> "arch:Fsck")，最近一次同步于 2026-03-25，若英文版本有所[更改](<https://wiki.archlinux.org/title/Fsck?diff=0&oldid=838817>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Fsck_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[fsck](<https://en.wikipedia.org/wiki/Fsck> "wikipedia:Fsck") 是 _“file system check”_ 的缩写，意为“文件系统检查”，用于检查 Linux 上的文件系统并尝试修复发现的错误。通常，fsck 会并行检查不同物理磁盘上的文件系统来节省时间（请参阅 [fsck(8)](<https://man.archlinux.org/man/fsck.8>)）。 

在 [Arch 的启动流程](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html> "Arch 的启动流程")中， _fsck_ 会在您每次开机时自动检查相关的驱动器，因此您无需使用命令行。 

##  启动时检查

###  方式

**提示：** 本小节中所有的“检查”（共两处）在英文原文中均为动词 “fsck”，而 fsck 本身则包含“检查并尝试修复”之意，为保证语句通顺译为“检查”，请知悉。

有两种方式： 

  1. mkinitcpio 为您提供了一个选择，即在挂载您的根文件系统前使用 `fsck` 钩子检查它。若如此做，您应当用 `rw` 内核参数将根文件系统挂载为可读写[[1]](<https://gitlab.archlinux.org/archlinux/mkinitcpio/mkinitcpio/commit/449b3e543c>)。
  2. systemd 会检查所有 fsck 选项大于 0 的文件系统（使用 [fstab 选项](<#fstab_%E9%80%89%E9%A1%B9>)或[用户提供的单元文件](<../zh-cn/Systemd.html#systemd.mount_-_%E6%8C%82%E8%BD%BD> "Systemd"))。对于根文件系统，其必须在开始时被使用 `ro` 内核参数被挂载为只读，然后再通过 [fstab](<../zh-cn/Fstab.html> "Fstab") 被重新挂载为可读写（请注意 `defaults` 挂载选项包含 `rw`）。

推荐第一种方式，若您遵循了[安装指南](<../zh-cn/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97.html> "安装指南")，则会默认这样。若您想使用第二种方式，您应当从 `mkinitcpio.conf` 中移除 `fsck` 钩子并在内核命令行中使用 `ro`。使用 `fsck.mode=skip` 内核参数可在两种做法中完全禁用 _fsck_ 。 

###  强制检查

如果您使用 `base` 的 [mkinitcpio](<../zh-cn/Mkinitcpio.html> "Mkinitcpio") 钩子，您可以向内核传递 `fsck.mode=force` [内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")以在启动时强制执行 _fsck_ ，这会检查您的设备上的每一个文件系统。 

此外，systemd 提供了 [systemd-fsck@.service(8)](<https://man.archlinux.org/man/systemd-fsck%40.service.8>)，用于检查已配置的文件系统，且不在 [initramfs](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#initramfs> "Initramfs") 中执行。然而，用这种方法检测根文件系统会推迟启动流程，因为要重新挂载根文件系统。 

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 有可能使用 systemd 钩子在 initramfs 中运行 _fsck_ 吗？ (在 [Talk:Fsck](<../zh-cn/Talk:Fsck.html>) 中讨论)

**注意：** 习惯使用其他 GNU/Linux 发行版的用户可能会习惯向每个文件系统写入 `forcefsck` 文件或使用 `shutdown -F` 关机命令等旧方法，但它们仅适用于 [SysVinit](<../zh-cn/SysVinit.html> "SysVinit") 和早期版本的 [Upstart](<https://en.wikipedia.org/wiki/Upstart> "wikipedia:Upstart")，但不适用于 [systemd](<../zh-cn/Systemd.html> "Systemd")。因此上述方法是 Arch Linux 上唯一的解决方法。

###  在修复询问中自动回答 yes

启动时的 _fsck_ 检查可能会停止并返回 `"UNEXPECTED INCONSISTENCY; RUN fsck MANUALLY."`。 

当您需要允许某些更改以修复系统，而这些更改并不被认为是完全安全的时候，它就会发生。因此需要手动执行 _fsck_ 。 

您可以通过将 `fsck.repair` 内核命令行选项设为 `yes` 来让 `fsck` 自动接受所有建议的更改（即对所有问题回答 yes）。 

**提示：** 其他可能的值为 `no` 和 `preen`，参阅 [systemd-fsck@.service(8)](<https://man.archlinux.org/man/systemd-fsck%40.service.8>) 以获取这些选项的意义。

##  提示和技巧

###  尝试修复坏块

欲自动修复 ext2/ext3/ext4 或 FAT [文件系统](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html> "文件系统")上损坏的部分，请执行： 

**警告：** 这条命令不会询问您是否修复，当您运行它时，回答就已经是 yes。
    
    # fsck -a
    
###  交互式地修复坏块

这在 boot 分区上的文件被改动而日志未能正确更新时会很有用。在这种情况下，请取消挂载 boot 分区，然后执行以下命令以修复损坏的部分： 
    
    # fsck -r _设备_
    
###  更改检查频率

**注意：** 本小节的 _tune2fs_ 命令和 _dumpe2fs_ 命令仅在 ext2/ext3/ext4 文件系统上工作。

默认情况下， _fsck_ 每 30 次启动检查一次文件系统（不同分区独立计数）。要更改检查频率，请执行： 
    
    # tune2fs -c 20 /dev/sda1
    
在本例中，`20` 是相邻两次检查之间的启动次数。 

请注意 `1` 会在每次启动时都执行检查，而 `0` 会完全停止检查。 

欲查看某分区的检查频率和挂载次数，请执行： 
    
    # dumpe2fs -h /dev/sda1 | grep -i 'mount count'
    
###  fstab 选项

[fstab](<../zh-cn/Fstab.html> "Fstab") 是一个系统配置文件，用于告诉 Linux 内核将哪些分区（文件系统）挂载到文件系统树的哪里。 

一个典型的 `/etc/fstab` 条目可能看起来像这样： 
    
    /dev/sda1   /         ext4      defaults       0  **1**
    /dev/sda2   /other    ext4      defaults       0  **2**
    /dev/sda3   /win      ntfs-3g   defaults       0  **0**
    
第 6 列（粗体文字）是 fsck 选项。 

  * `0`——不检查
  * `1`——要检查的第一个文件系统（分区），`/`（根分区）应当被设为 `1`。
  * `2`——所有要检查的其他文件系统。

##  疑难解答

###  无法在独立的 /usr 分区上运行 fsck

  1. 确保您的 `/etc/mkinitcpio.conf` 文件中配置了需要的[钩子](<../zh-cn/Mkinitcpio.html#/usr_%E6%94%BE%E5%88%B0%E5%8D%95%E7%8B%AC%E5%88%86%E5%8C%BA> "Mkinitcpio")，并在编辑该文件后重新生成了 initramfs。
  2. 检查您的 [fstab](<../zh-cn/Fstab.html> "Fstab")！只有根分区的最后一项需要是 `1`，其他的都是 `2` 或 `0`。检查是否存在其他拼写错误。

###  “ext2fs: no external journal” 报错

有时候 ext3/ext4 文件系统可能会损坏（由于电源故障）。通常，fsck 会提示 `no external journal`（无外部日志），在这种情况下，请运行以下命令： 

将该分区从其挂载点取消挂载： 
    
    # umount _directory_
    
向该分区写入新日志： 
    
    # tune2fs -j /dev/_partition_
    
运行 fsck 以修复该分区： 
    
    # fsck -p /dev/_partition_
    