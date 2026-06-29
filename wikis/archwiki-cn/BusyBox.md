**翻译状态：**

  * 本文（或部分内容）译自 [BusyBox](<https://wiki.archlinux.org/title/BusyBox> "arch:BusyBox")，最近一次同步于 2023-05-23，若英文版本有所[更改](<https://wiki.archlinux.org/title/BusyBox?diff=0&oldid=778735>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/BusyBox_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [mkinitcpio](<../zh-cn/Mkinitcpio.html> "Mkinitcpio")
  * [init](<../zh-cn/Init.html> "Init")

[BusyBox](<https://en.wikipedia.org/wiki/BusyBox> "wikipedia:BusyBox") 在单个小型可执行文件中为嵌入式系统提供了许多常见的 UNIX 实用程序。软件包还包含 runit; 详情请参考 [runit](</wzh/index.php?title=Runit&action=edit&redlink=1> "Runit（页面不存在）")。 

**注意：** 不要期望完全的即插即用替换和兼容性。某些实用程序可能不存在，而对于某些实用程序，则可能缺少选项。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [busybox](<https://archlinux.org/packages/?name=busybox>)包 包。 

Busybox 命令是指向 `/usr/bin/busybox` 的符号链接，因此仅占用很少的空间。这对于低占用空间的系统特别有用。 

##  用法

### init

Init 脚本可以与 busybox-init 一起使用，例如 [minirc-git](<https://aur.archlinux.org/packages/minirc-git/>)AUR。有关详细信息，请参见 [init](<../zh-cn/Init.html> "Init")。 

### getty

这些 getty 在文件 `/etc/inittab` 中定义。默认情况下，getty 在 tty 1 到 4 上启动。 

为了启用/禁用 getty，您只需将这一行放在 `/etc/inittab` 中 
    
    tty2::respawn:/sbin/agetty -8 -s 38400 tty2 linux
    
只需将 tty2 替换为 tty，就可以开始使用 getty。 如果您想让 init 在启动 gettty 之前询问您，则将 `respawn` 替换为 `askfirst`。 

### mdev

请参阅 [Gentoo wiki](<https://wiki.gentoo.org/wiki/Mdev>)。 

### runit

请参考 [runit](</wzh/index.php?title=Runit&action=edit&redlink=1> "Runit（页面不存在）")。 

##  参见

  * [w:ToyBox](<https://en.wikipedia.org/wiki/ToyBox> "w:ToyBox")
