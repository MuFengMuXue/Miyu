**翻译状态：**

  * 本文（或部分内容）译自 [Back In Time](<https://wiki.archlinux.org/title/Back_In_Time> "arch:Back In Time")，最近一次同步于 2024-6-23，若英文版本有所[更改](<https://wiki.archlinux.org/title/Back_In_Time?diff=0&oldid=811141>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Back_In_Time_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

摘自[上游](<https://github.com/bit-team/backintime?tab=readme-ov-file#back-in-time>): 

    Back In Time 是一款易于使用的文件和文件夹备份工具。它可在 GNU Linux 上运行（不能在 Windows 或 OS X/macOS 上运行），并提供一个命令行工具 _backintime_ 和一个图形用户界面 _backintime-qt_ ，这两个工具都是用 Python3 编写的。它使用 [rsync](<../zh-cn/Rsync.html> "Rsync") 手动或计划快照，并通过 SSH 在本地或远程存储。每个快照都在自己的文件夹中，并带有原始文件的副本，但为了节省存储空间，快照之间会硬链接不变的文件。它的灵感来自 FlyBack。

##  安装

可以[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") GUI 版本 [backintime](<https://aur.archlinux.org/packages/backintime/>)AUR 或者 CLI-only 版本 [backintime-cli](<https://aur.archlinux.org/packages/backintime-cli/>)AUR 。 

##  用法

对于图形界面 (GUI) ，运行 _backintime-qt_ 。对于命令行界面（CLI），运行 _backintime_ 。 

对于图形用户界面版本，桌面环境中安装了两个启动程序： _Back In Time_ 和 _Back In Time (root)_ 。后者将[以根用户权限启动图形用户界面](</wzh/index.php?title=%E4%BB%A5%E6%A0%B9%E7%94%A8%E6%88%B7%E8%BA%AB%E4%BB%BD%E8%BF%90%E8%A1%8C_GUI_%E5%BA%94%E7%94%A8&action=edit&redlink=1> "以根用户身份运行 GUI 应用（页面不存在）")（英语：[Running GUI applications as root](<https://wiki.archlinux.org/title/Running_GUI_applications_as_root> "en:Running GUI applications as root")）（使用 [pkexec(1)](<https://man.archlinux.org/man/pkexec.1>)），可用于备份当前用户在 `/home` 中的文件以外的文件。 

##  启用计划任务

备份工作的计划任务是通过 [cron](<../zh-cn/Cron.html> "Cron") 实现的。 

默认情况下，没有[自动启用](<../zh-cn/Systemd.html#%E9%BB%98%E8%AE%A4%E5%90%AF%E7%94%A8%E6%96%B0%E5%AE%89%E8%A3%85%E7%9A%84%E5%8D%95%E5%85%83> "Systemd")服务：您需要[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")与您安装的 cron 提供程序相关的[cron 服务](<../zh-cn/Cron.html#%E6%BF%80%E6%B4%BB%E5%8F%8A%E5%BC%80%E6%9C%BA%E5%90%AF%E5%8A%A8> "Cron")。 

##  参见

  * 在 Microsoft GitHub 上的[上游项目](<https://github.com/bit-team/backintime>)
  * [已知问题与解决方案](<https://github.com/bit-team/backintime?tab=readme-ov-file#known-problems-and-workarounds>) (README.md)
  * [FAQ](<https://github.com/bit-team/backintime/blob/dev/FAQ.md>)
    * [错误与处理办法](<https://github.com/bit-team/backintime/blob/dev/FAQ.md#problems-errors--solutions>)
  * [邮件列表 _bit-dev_](<https://mail.python.org/mailman3/lists/bit-dev.python.org/>)
  * [用户手册](<https://backintime.readthedocs.io/en/latest/>)
