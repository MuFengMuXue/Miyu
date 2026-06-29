**翻译状态：**

  * 本文（或部分内容）译自 [Tmpfs](<https://wiki.archlinux.org/title/Tmpfs> "arch:Tmpfs")，最近一次同步于 2025-10-27，若英文版本有所[更改](<https://wiki.archlinux.org/title/Tmpfs?diff=0&oldid=847600>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Tmpfs_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[tmpfs](<https://en.wikipedia.org/wiki/Tmpfs> "wikipedia:Tmpfs") 是一个停留在内存与/或交换分区的临时文件系统。把目录挂载为 tmpfs 是一个加速文件访问或是确保内容重启自动清除的有效手段。 

**提示：** tmpfs 目录中的临时文件可以使用 [systemd-tmpfiles](<../zh-cn/Systemd.html#systemd-tmpfiles_-_%E4%B8%B4%E6%97%B6%E6%96%87%E4%BB%B6> "Systemd-tmpfiles") 在计算机启动时重新创建。

##  用法

tmpfs 经常会被使用在[/tmp](<https://refspecs.linuxfoundation.org/FHS_3.0/fhs/ch03s18.html>)、[/var/lock](<https://refspecs.linuxfoundation.org/FHS_3.0/fhs/ch05s09.html>) 以及 [/var/run](<https://refspecs.linuxfoundation.org/FHS_3.0/fhs/ch05s13.html>)。请**不要** 把它用在 [/var/tmp](<https://refspecs.linuxfoundation.org/FHS_3.0/fhs/ch05s15.html>) 上，这个目录是用于跨重启保存的临时文件的。 

Arch 对 `/run` 目录使用 tmpfs，同时存在的 `/var/run` 和 `/var/lock` 只是单纯为了维持兼容性的符号链接。在默认的 systemd 配置下，tmpfs 也被用于 `/tmp`，如果没有特殊需求不需要专门在 [fstab](<../zh-cn/Fstab.html> "Fstab") 里添加条目。 

[glibc](<https://archlinux.org/packages/?name=glibc>)包 2.2 及以上为了 [POSIX 共享内存](<https://en.wikipedia.org/wiki/Shared_memory#Support_on_Unix-like_systems> "wikipedia:Shared memory")会假定有 tmpfs 被挂载于`/dev/shm`。这一挂载会由 [systemd](<../zh-cn/Systemd.html> "Systemd") 自动处理，无需手动配置 [fstab](<../zh-cn/Fstab.html> "Fstab")。 

一般来说，需要经常进行读写操作的程序与任务可以从使用 tmpfs 的目录中获益。某些应用甚至可以通过将部分或是全部数据放至共享内存以获得巨大的性能提升，例如可以[把 Firefox 的用户资料放在内存中](<../zh-cn/Firefox/%E5%9C%A8_RAM_%E4%B8%AD%E5%AD%98%E5%82%A8%E9%85%8D%E7%BD%AE.html> "Firefox/在 RAM 中存储配置")来大幅提升性能。 

##  例子

**注意：** 真正的内存/交换区消耗依实际使用而定，tmpfs 分区在真正需要内存之前不会使用任何内存。

tmpfs 分区的默认最大容量是可用内存的一半，不过这是可以修改的。若需要显式地设定最大容量，使用 `size` 挂载选项（以下的例子会覆盖默认的 `/tmp` 挂载）： 
    
    /etc/fstab
    
    tmpfs   /tmp         tmpfs   rw,nodev,nosuid,size=2G          0  0

若想让挂载更安全，可以使用以下选项： 
    
    /etc/fstab
    
    tmpfs   /www/cache    tmpfs  rw,size=1G,nr_inodes=5k,noexec,nodev,nosuid,uid=_user_ ,gid=_group_ ,mode=1700 0 0

请查看 [tmpfs(5)](<https://man.archlinux.org/man/tmpfs.5>) 手册页和[安全#文件系统](<../zh-cn/%E5%AE%89%E5%85%A8.html#%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "安全")来获取更多信息。 

重启以使修改起效。注意虽然直接运行 `mount -a` 让修改立刻起效很有吸引力，但这一操作会让当前目录的所有文件都无法被访问（这对正在运行的持有锁文件的程序可能是个大问题）。不过，如果它们都是空的，使用 `mount -a` 而非重启应该是安全的（也可以通过单独挂载各个部分来绕开这个问题）。 

在应用更改之后，通过查看 `/proc/mounts` 或是使用 `findmnt` 来验证是否起效。 
    
    $ findmnt /tmp
    
    TARGET SOURCE FSTYPE OPTIONS
    /tmp   tmpfs  tmpfs  rw,nosuid,nodev,relatime

tmpfs 也可以临时改变大小而无需重启。如果有一个大型的编译任务即将运行，可以直接： 
    
    # mount -o remount,size=4G /tmp
    
或基于 RAM 重新调整大小： 
    
    # mount -o remount,size=80% /tmp
    
##  禁用自动挂载

在 [systemd](<../zh-cn/Systemd.html> "Systemd") 下，`/tmp` 会被自动挂载为 tmpfs，除非 `/tmp` 是 `/etc/fstab` 中一个已经存在的挂载点（不论这个挂载点是 tmpfs 还是储存设备）。如果想禁用自动挂载，[mask](</wzh/index.php?title=Mask&action=edit&redlink=1> "Mask（页面不存在）") 掉 `tmp.mount` 这一 systemd 单元。 

文件将不会被储存在 tmpfs 中，而是直接到块设备上。`/tmp` 中的内容现在会在每次重启间保存，这可能不是所期望的行为（虽说文件还是会在 10 天后被清理）。若想恢复之前的行为，在重启时自动清理 `/tmp` 目录的话，可以考虑使用 [tmpfiles.d(5)](<https://man.archlinux.org/man/tmpfiles.d.5>)： 
    
    /etc/tmpfiles.d/tmp.conf
    
    # see tmpfiles.d(5)
    # always enable /tmp directory cleaning
    D! /tmp 1777 root root 0
    
    # remove files in /var/tmp older than 10 days
    D /var/tmp 1777 root root 10d
    
    # namespace mountpoints (PrivateTmp=yes) are excluded from removal
    x /tmp/systemd-private-*
    x /var/tmp/systemd-private-*
    X /tmp/systemd-private-*/tmp
    X /var/tmp/systemd-private-*/tmp

##  故障排除

###  作为 root 在 tmpfs 中打开符号链接失败

假设 `/tmp` 正在使用 tmpfs，首先更改当前工作目录到 `/tmp`，然后在这个 `/tmp` 目录下创建一个文件以及指向这个文件的符号连接。root 在读取这个符号链接时会遇到“权限不够”的错误，这是因为 `/tmp` [设置了黏滞位](<https://wiki.ubuntu.com/Security/Features#Symlink_restrictions>)。 

这个行为可以通过 `/proc/sys/fs/protected_symlinks` 控制，或是直接使用 sysctl：`sysctl -w fs.protected_symlinks=0`。参阅 [Sysctl#配置](<../zh-cn/Sysctl.html#%E9%85%8D%E7%BD%AE> "Sysctl")来永久更改这个行为。 

**警告：** 更改这一行为可能会导致安全问题！

##  提示与技巧

###  为 /run/user/xxxx 分配更多内存

控制 `/run/user/` 中 tmpfs 大小的标准方法是通过修改 `/etc/systemd/logind.conf` 中的 `RuntimeDirectorySize` （详见 [logind.conf(5)](<https://man.archlinux.org/man/logind.conf.5>)）。默认大小为物理内存的 10%，但可以安全地增加此值。需要记住的是，tmpfs 仅占用已实际使用的空间，此处指定的数值只是允许的最大值。 

##  另请参阅

  * [Linux 内核文档](<https://docs.kernel.org/filesystems/tmpfs.html>)
