**翻译状态：**

  * 本文（或部分内容）译自 [Profile-sync-daemon](<https://wiki.archlinux.org/title/Profile-sync-daemon> "arch:Profile-sync-daemon")，最近一次同步于 2025-01-07，若英文版本有所[更改](<https://wiki.archlinux.org/title/Profile-sync-daemon?diff=0&oldid=824630>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Profile-sync-daemon_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Anything-sync-daemon](<../zh-cn/Anything-sync-daemon.html> "Anything-sync-daemon")
  * [Firefox](<../zh-cn/Firefox.html> "Firefox")
  * [Chromium](<../zh-cn/Chromium.html> "Chromium")
  * [Pdnsd](</wzh/index.php?title=Pdnsd&action=edit&redlink=1> "Pdnsd（页面不存在）")
  * [SSD](<../zh-cn/%E5%9B%BA%E6%80%81%E7%A1%AC%E7%9B%98.html> "SSD")

[profile-sync-daemon](<https://archlinux.org/packages/?name=profile-sync-daemon>)包 (psd) 是一个小型伪守护进程，旨在于 tmpfs 中管理浏览器配置文件，并定期将其同步回磁盘中。保持 tmpfs 副本和与媒体相关的浏览器配置文件备份之间的同步的过程通过创新地使用 [rsync](<../zh-cn/Rsync.html> "Rsync") 实现。此外，psd 还具有若干崩溃恢复功能。 

psd 的设计目标和优点如下： 

  1. 自动化用户体验
  2. 减少硬盘磨损
  3. 提高速度

由于浏览器配置文件、缓存等被迁移到 [tmpfs](<../zh-cn/Tmpfs.html> "Tmpfs")（内存）中，因此与使用浏览器相关的 I/O 操作也会从磁盘重定向到内存，从而减少磁盘磨损，并大幅提升浏览器的速度和可响应性。 

**注意：**

  * 一些浏览器，如 Chrome（及 Chromium）和 Firefox（自 v21 起），将缓存目录与配置文件目录**分开** 存放。profile-sync-daemon 不能用于修改此行为，可以参考 [Chromium#临时文件系统中的缓存](<../zh-cn/Chromium.html#%E4%B8%B4%E6%97%B6%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F%E4%B8%AD%E7%9A%84%E7%BC%93%E5%AD%98> "Chromium")部分了解 Chromium 的相关内容，并参考 [Firefox/在 RAM 中存储配置](<../zh-cn/Firefox/%E5%9C%A8_RAM_%E4%B8%AD%E5%AD%98%E5%82%A8%E9%85%8D%E7%BD%AE.html> "Firefox/在 RAM 中存储配置")文章获取解决方法。
  * 默认配置文件 `/usr/share/psd/psd.conf` 可能会随软件包的更新更改。需要使用 `diff` 比较用户配置 `$XDG_CONFIG_HOME/psd/psd.conf` 与其的差异。在 Arch Linux 上，pacman 会通知执行此操作。
  * psd 可能会导致[登录变慢](<https://www.reddit.com/r/archlinux/comments/4l7gvm/very_slow_when_login/d3lrx9y/>)，因为需要在登录时将浏览器缓存复制到 RAM 中。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [profile-sync-daemon](<https://archlinux.org/packages/?name=profile-sync-daemon>)包。 

##  配置

第一次运行 psd 时，会创建包含所有设置的 `$XDG_CONFIG_HOME/psd/psd.conf` 配置文件。在使用 `psd.service` 启动同步前，可以使用 `psd` 命令来创建此文件。 

**注意：** 在 psd 活动时对配置文件做的修改只有在[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `psd.service` 服务后才能生效。

以下是可选的环境变量配置： 

  * 设置 `USE_OVERLAYFS` 变量：启用 overlayfs，可提高同步速度并减少内存占用。对 `/usr/bin/psd-overlay-helper` 拥有 sudo 权限才能使用此选项，且内核必须支持最低版本 22 的 overlayfs。有关详细信息，参阅 [#Overlayfs 模式](<#Overlayfs_%E6%A8%A1%E5%BC%8F>)。
  * 设置 `BROWSERS` 数组：需要管理的浏览器。默认管理所有检测到的浏览器。 
    * 示例（假设已安装 Chromium、Opera 和 Firefox，但用户只希望将 Chromium 和 Opera 同步到 tmpfs）：

    BROWSERS=(chromium opera)
    
  * 设置 `USE_BACKUPS` 变量：启用/禁用崩溃恢复快照。默认启用。
  * 设置 `BACKUP_LIMIT` 变量：保留的崩溃恢复快照的数量。

从 psd 的 5.54 版本开始，原生支持 [overlayfs](<#Overlayfs_mode>)，要求 Linux 内核版本至少为 3.18.0。 

###  支持的浏览器

目前，psd 自动检测并管理以下浏览器： 

  * [Chromium](<../zh-cn/Chromium.html> "Chromium")
  * [chromium-dev](<https://aur.archlinux.org/packages/chromium-dev/>)AUR
  * [conkeror-git](<https://aur.archlinux.org/packages/conkeror-git/>)AUR
  * [Epiphany](</wzh/index.php?title=Epiphany&action=edit&redlink=1> "Epiphany（页面不存在）")（英语：[Epiphany](<https://wiki.archlinux.org/title/Epiphany> "en:Epiphany")）
  * [falkon](<https://archlinux.org/packages/?name=falkon>)包
  * [Firefox](<../zh-cn/Firefox.html> "Firefox")（所有版本，包括稳定版、beta 和 nightly）
  * [google-chrome](<https://aur.archlinux.org/packages/google-chrome/>)AUR
  * [google-chrome-beta](<https://aur.archlinux.org/packages/google-chrome-beta/>)AUR
  * [google-chrome-dev](<https://aur.archlinux.org/packages/google-chrome-dev/>)AUR
  * [icecat](<https://aur.archlinux.org/packages/icecat/>)AUR
  * [Luakit](</wzh/index.php?title=Luakit&action=edit&redlink=1> "Luakit（页面不存在）")（英语：[Luakit](<https://wiki.archlinux.org/title/Luakit> "en:Luakit")）
  * [Opera](<../zh-cn/Opera.html> "Opera")
  * [Otter Browser](<../zh-cn/Otter_Browser.html> "Otter Browser")
  * [palemoon](<https://aur.archlinux.org/packages/palemoon/>)AUR
  * [Qutebrowser](</wzh/index.php?title=Qutebrowser&action=edit&redlink=1> "Qutebrowser（页面不存在）")（英语：[Qutebrowser](<https://wiki.archlinux.org/title/Qutebrowser> "en:Qutebrowser")）
  * [seamonkey](<https://aur.archlinux.org/packages/seamonkey/>)AUR
  * [surf](<https://aur.archlinux.org/packages/surf/>)AUR
  * [vivaldi](<https://archlinux.org/packages/?name=vivaldi>)包

##  用法

[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `psd.service` [用户单元](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "用户单元")。提供的 resync-timer 每小时将配置文件从 tmpfs 同步回磁盘。resync-timer 会随着 `psd.service` 自动启动，无需手动启动。 

###  预览（解析）模式

运行 `psd parse` 以查看 psd 根据 `$XDG_CONFIG_HOME/psd/psd.conf` 将执行的操作和正在执行的操作。它还会提供一些有用的信息，例如配置文件大小、路径以及是否创建了任何恢复快照。 

##  提示与技巧

###  缩短同步间隔

psd 提供的同步定时器每小时触发一次。更改同步间隔需要[修改 systemd 单元](<../zh-cn/Systemd.html#%E4%BF%AE%E6%94%B9%E7%8E%B0%E5%AD%98%E5%8D%95%E5%85%83%E6%96%87%E4%BB%B6> "Systemd")。下面的示例将定时器更改为每十分钟同步一次（请注意，`OnUnitActiveSec` 需要在重新分配之前手动清除 [[1]](<https://bugzilla.redhat.com/show_bug.cgi?id=756787#c9>)）： 
    
    ~/.config/systemd/user/psd-resync.timer.d/frequency.conf
    
    [Unit]
    Description=Timer for Profile-sync-daemon - 10min
    
    [Timer]
    OnUnitActiveSec=
    OnUnitActiveSec=10min

更多选项请参阅 [systemd.timer(5)](<https://man.archlinux.org/man/systemd.timer.5>)。 

###  Overlayfs 模式

**注意：** 在 Linux 内核中有多个版本的 overlayfs 可用于生产环境，不同发行版中的 overlayfs 版本可能不同。版本 22 及以下的模块名为“overlayfs”，而更新的版本（23 及以上）的模块名为“overlay”（删去了“fs”）。如果配置使用某一版本，psd 会自动检测内核支持的 overlayfs 版本。

Overlayfs 是一个简单的联合文件系统，自 Linux 内核 3.18.0 版本开始被主线集成。psd 从版本 5.54 开始，可用 overlayfs 减少其 tmpfs 空间占用的内存，并加速同步和取消同步操作。其原理在于 overlay 挂载只写出发生更改的数据，而不是整个配置文件。运行于 overlayfs 模式时，psd 默认模式下的恢复功能仍然有效。通过取消注释 `USE_OVERLAYFS="yes"` 行并重新启动守护进程，即可启用 overlayfs 模式（配置文件位于 `$XDG_CONFIG_HOME/psd/psd.conf`）。 

自 psd 版本 6.05 起，使用此模式必须具有对 `/usr/bin/psd-overlay-helper` 无密码提示的 [sudo](<../zh-cn/Sudo.html> "Sudo") 权限或全局 sudo 权限。以下是添加这些权限所需的 `/etc/sudoers` 行，请使用 [visudo](<../zh-cn/Sudo.html#%E4%BD%BF%E7%94%A8_visudo> "Visudo") 添加： 
    
    **< 用户名>** ALL=(ALL) NOPASSWD: /usr/bin/psd-overlay-helper
    
请参见前文 [#预览（解析）模式](<#%E9%A2%84%E8%A7%88%EF%BC%88%E8%A7%A3%E6%9E%90%EF%BC%89%E6%A8%A1%E5%BC%8F>)中的示例，可显示使用 overlayfs 的系统节省的内存。注意“overlayfs 大小”报告与每个配置文件的总“配置文件大小”报告之间的对比。请注意，这些数字会根据写入配置文件的数据量而变化，但在常见的使用情况下，overlayfs 的大小通常小于配置文件大小。 

**警告：** 在 overlayfs 模式下使用 psd（尤其是 `psd-overlay-helper`）可能导致权限提升。[[2]](<https://github.com/graysky2/profile-sync-daemon/issues/235>)[[3]](<https://github.com/graysky2/profile-sync-daemon/issues/286>)

Overlayfs 的工作方式是挂载配置文件的只读基础副本（browser-back-ovfs），并在其上管理新数据。为了避免重新同步到只读文件系统，会使用一个副本。因此，使用 overlayfs 是一种权衡：初始同步时间更快，内存使用更少，但需要占用主目录中的磁盘空间。 

###  为 /run/user/xxxx 分配更多内存以容纳配置文件

控制 `/run/user` 大小的标准方法是编辑 `/etc/systemd/logind.conf` 中的 RuntimeDirectorySize 配置（参见 [logind.conf(5)](<https://man.archlinux.org/man/logind.conf.5>)）。默认情况下，使用物理内存的 10%，但可以安全地增加此值。请记住，tmpfs 只会使用实际占用的空间，这里指定的数字仅为允许的最大值。 

###  快照

通常情况下，浏览器配置文件的“最后有效”备份可能仍然安全地保存在文件系统中。在重启 psd（例如系统重启）时，会检查指向 tmpfs 配置文件副本的符号链接是否有效。如果无效，psd 会在重新定位之前对“最后有效”备份进行快照。这主要是为了完整性检查，以确保 psd 未造成任何损害，任何数据丢失都源于其他因素。 

**注意：** 可以通过在 `$XDG_CONFIG_HOME/psd/psd.conf` 中将 `USE_BACKUPS` 变量取消注释并设置为 `"no"`，禁用快照/备份功能。

可在与浏览器存放配置文件的目录中找到快照，它将包含与恢复发生时间对应的日期时间戳。例如，Chromium 的快照路径为 `~/.config/chromium-backup-crashrecovery-20130912_153310`⸺当然，日期时间后缀会有所不同。 

恢复快照的方法： 

  * [停止](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "停止") `psd.service` [用户单元](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "用户单元")。
  * 确保没有指向 tmpfs 浏览器配置文件目录的符号链接。如果有，说明 psd 可能由于某些原因没有正确停止。
  * 将“坏掉的”配置文件副本移到备份中（不要盲目删除任何文件）。
  * 将快照目录复制到浏览器预期的目录中。

以 Chromium 为例： 
    
    $ mv ~/.config/chromium ~/.config/chromium-bad
    $ cp -a ~/.config/chromium-backup-crashrecovery-20130912_153310 ~/.config/chromium
    
重新启动 Chromium，浏览器将使用备份快照。如果一切正常，关闭浏览器并重启 psd。此时，可以安全地删除`~/.config/chromium-backup-crashrecovery-20130912_153310`。 

####  使用清理模式清除所有快照

运行 `psd clean` 将删除所有积累的恢复快照。在确定要删除这些快照后再运行此命令。 

##  支持

如有评论或疑虑，请在[讨论帖](<https://bbs.archlinux.org/viewtopic.php?pid=1026974>)中发布。 

##  另见

  * （英文）[Web Upd8⸺使用 profile-sync-daemon 将浏览器配置文件保存在 tmpfs（RAM）中，以减少磁盘写入并提高性能](<http://www.webupd8.org/2013/02/keep-your-browser-profiles-in-tmpfs-ram.html>)
  * （英文）[Nicolas Bernaerts⸺SSD 驱动器的调整](<https://web.archive.org/web/20220516124034/http://www.bernaerts-nicolas.fr/linux/74-ubuntu/250-ubuntu-tweaks-ssd>)
