相关文章

  * [Profile-sync-daemon](<../zh-cn/Profile-sync-daemon.html> "Profile-sync-daemon")

**翻译状态：**

  * 本文（或部分内容）译自 [Anything-sync-daemon](<https://wiki.archlinux.org/title/Anything-sync-daemon> "arch:Anything-sync-daemon")，最近一次同步于 2023-06-04，若英文版本有所[更改](<https://wiki.archlinux.org/title/Anything-sync-daemon?diff=0&oldid=756838>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Anything-sync-daemon_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[anything-sync-daemon](<https://archlinux.org/packages/?name=anything-sync-daemon>)包 (asd) 是一个小型的、用以将用户指定的目录（同步的目标）移至 tmpfs 并定期同步回硬盘（HDD/SSD）的伪守护进程。其原理为通过 bind 挂载以及创造性地使用 rsync 来同步两处的文件。此外，ASD 有着多种用于崩溃恢复的特性。 

ASD 的设计目标以及优点有： 

  1. 透明的用户体验
  2. 减少对硬盘的损耗
  3. 速度

当目标目录被移至 tmpfs 之后，相应的读写操作也将从硬盘转移到内存，因而可以减少硬盘损耗，同时提升运行速度与响应速度。内存的访问时间以纳秒计，而硬盘则是以毫秒计，这中间差了六个数量级，或者说，内存比硬盘快出一百万倍。 

**警告：** 如果你只想同步浏览器的 profile，我们建议不要使用 ASD，而是使用专门为此设计的、可以检查浏览器运行状况的 [PSD](<../zh-cn/Profile-sync-daemon.html> "Profile-sync-daemon")。ASD 并不会做这些检查，在某些情况下，浏览器 profile 的数据可能丢失。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [anything-sync-daemon](<https://archlinux.org/packages/?name=anything-sync-daemon>)包 包。 

##  配置

配置文件在随软件包安装的 `/etc/asd.conf`。 

  * 至少需要在 `WHATTOSYNC` 数组里定义由 ASD 管理的同步目标。语法见下方。
  * 选做：取消 `VOLATILE` 变量的注释并定义 tmpfs 的位置。
  * 选做：启用 overlayfs 来进一步提升同步的速度并降低内存的使用。注意该选项需要你的内核进行任一 overlay 内核模块的使用的配置。阅读 [#Overlayfs 模式](<#Overlayfs_%E6%A8%A1%E5%BC%8F>)以了解更多信息。

**注意：** 对于 VOLATILE 设定来说，默认值 `/tmp` 就应该很好了。如果你正在使用 [bleachbit](<https://archlinux.org/packages/?name=bleachbit>)包，请不要用 `--clean system.tmp` 选项调用它，否则你会把一个 ASD 用来记录同步状态的关键的文件（.foo）给移除掉。另外，请注意使用设置成 `/dev/shm` 可能会带来问题，此时 systemd 的 NAMESPACE 可能只会在用户开启 overlayfs 选项时出现。

例如： 
    
    WHATTOSYNC=('/var/lib/monitorix' '/srv/http' '/foo/bar')
    
或者 
    
    WHATTOSYNC=(
    '/var/lib/monitorix'
    '/srv/http'
    '/foo/bar'
    )
    
##  使用

[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `asd.service`。此外，程序提供的同步定时器会每小时运行一次，将文件从 tmpfs 同步回硬盘。同步定时器在 `asd.service` 启动后会自动启动，所以不必手动启动。 

###  预览（parse）模式

运行 `asd parse` 来查看在 `/etc/asd.conf` 的设定下 ASD 将会进行或是正在进行什么操作。它同时也会提供目录大小、路径、以及是否存在恢复快照等有用信息。 

##  提示以及技巧

###  更频繁地进行同步

软件提供了同步的计时器（timer），每小时运行一次。用户可以通过[扩展对应的 systemd unit](<../zh-cn/Systemd.html#Editing_provided_units> "Systemd")对其重新设定。下面的例子将定时器设定为每十分钟同步一次（注意要先清除 `OnUnitActiveSec` 再设定新的值 [[1]](<https://bugzilla.redhat.com/show_bug.cgi?id=756787#c9>)）： 
    
    /etc/systemd/system/asd-resync.timer.d/frequency.conf
    
    [Unit]
    Description=Timer for Anything-sync-daemon - 10min
    
    [Timer]
    OnUnitActiveSec=
    OnUnitActiveSec=10min

查看 [systemd.timer(5)](<https://man.archlinux.org/man/systemd.timer.5>) 以获取更多选项。 

###  Overlayfs 模式

**注意：** 生产环境下的不同发行版的 Linux 内核有好几个版本的 overlayfs。版本 22 以及更低的版本的模块是“overlayfs”，而新版本（23 以及更高）是“overlay”——注意新版本里没有了“fs”的后缀。如果被设定使用其中一种 overlayfs 的话，ASD 会自动检测你的内核里可用的版本。

Overlayfs 是 Linux 内核版本 3.18.0 里正式引入的简单的联合文件系统。从 ASD 版本 5.54 开始，overlayfs 就可以被用于减低 ASD 的 tmpfs 内存使用并加速同步操作（以及取消同步的操作）。关键在于 overlay 的挂载只会写入更改了的数据写入而不会写入写入整个同步目录。在使用 overlayfs 模式时，ASD 默认启用的崩溃恢复特性也生效。Overlayfs 模式可以通过取消 `/etc/asd.conf` 里的 `USE_OVERLAYFS="yes"` 一行的注释并[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启")守护进程来开启。 

###  快照

有时候你的同步目录的最新的完好的备份还会在你的文件系统里保存着。在重启时，ASD 会检查上次退出时是否处在某种损坏的状态。如果检测到是的话，ASD 会先将最新的完好备份快照下来，之后再用这份备份恢复。注意，ASD 为了试图减少硬盘占用，它不会把整个目录都复制下来。它实际上使用了硬链接，在同步的时候才创建新的文件并保留原有的硬链接。所以在 ASD 正在备份的时候尝试更改目录可能会导致目录变为某种损坏的状态。 

**注意：** 如果真的想的话，用户可以通过在 `/etc/asd.conf` 里取消 `USE_BACKUPS` 变量的注释并设成 `"no"` 来将快照/备份特性直接关闭

快照会和同步目标在一个目录里，并且它的文件名会带有对应了恢复时间的时间戳。例如，`/foo/bar` 的快照会是 `/foo/.bar-backup_asd-crashrecovery-20141221_070112.tar.zstd`——当然你对应的时间戳后缀会不同。 

要恢复快照的话： 

  * [停止](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "停止") `asd.service`.
  * 确认不存在 ASD 创建的目录。如果存在的话，那么 ASD 上次因为某些其它的原因没有正确退出。
  * 将损坏的同步目录转移至备份位置（不要盲目地删除任何东西）。
  * 将快照存档的 tar 压缩包解压到同步目录。

以 `/foo/bar` 为例： 
    
    $ cd /foo
    $ mv bar bar-bad
    $ tar -xvf .bar-backup_asd-crashrecovery-20141221_070112.tar.zstd
    
####  使用清除（clean）模式清除所有快照

运行 `asd clean` 会删除所有的恢复快照。请只在确定你想要删除的时候再运行这个命令。 

**注意：** 如果同步目录的权限在 root 或者另一用户手中而 ASD 被调用来清除快照，那么它会因为同步目标的权限而出错。用户可以通过 sudo 或者以 root 身份调用这个功能来避免此类错误。

##  支持

请至[讨论贴](<https://bbs.archlinux.org/viewtopic.php?id=139141>)发表评论或提问。 
