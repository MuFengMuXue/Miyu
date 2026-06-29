**翻译状态：**

  * 本文（或部分内容）译自 [PRoot](<https://wiki.archlinux.org/title/PRoot> "arch:PRoot")，最近一次同步于 2019-01-31，若英文版本有所[更改](<https://wiki.archlinux.org/title/PRoot?diff=0&oldid=560586>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/PRoot_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[PRoot](<https://proot-me.github.io>)是一个能在用户空间内运行的程序, 功能类似于[chroot](<../zh-cn/Chroot.html> "Chroot"), `mount --bind`和 binfmt_misc , 能让root用户使用备用根目录运行程序, 就像chroot "jail"一样。 PRoot在由于缺少root权限而无法使用chroot的情况下尤其有用。 

##  安装

PRoot可以从[proot](<https://aur.archlinux.org/packages/proot/>)AUR包安装。 _pacstrap_ 可以在运行 _proot_ 之前用Arch环境初始化目录。 

##  用法

安装完成之后, PRoot不需要root权限。 和chroot一样, 你必须为PRoot提供一个新目录作为新的根目录。 如果没有指定shell程序，PRoot默认将启动`/bin/sh`。 虚拟文件系统无需手动挂载，PRoot会自动处理这个问题。 
    
    proot -r ~/mychroot/
    
此时，将启动一个shell， `/` 对应于主机上的 `~/mychroot/` 文件夹。 

可以使用 `-b` 选项明确地绑定变量： 
    
    proot -b /bin/bash:/bin/sh
    
这使得主机的/bin/bash在来宾的/bin/sh处可用 

PRoot在内部使用qemu用户模式模拟器来允许程序在PRoot内运行，即使程序是为主机系统以外的体系结构编译的。 

##  安全性

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** Compare security of chroot and PRoot: Are /proc, /sys, and /dev accessible inside a PRoot? Is privilege escalation possible? (在 [Talk:PRoot](<../zh-cn/Talk:PRoot.html>) 中讨论)

与chroot一样，PRoot仅提供文件系统级隔离。 PRoot "jail" 中的程序共享相同的内核，硬件，进程空间和网络子系统。 chroot和PRoot并不是如同虚拟机管理程序或半虚拟化程序的，真正的虚拟化程序替代品。 
