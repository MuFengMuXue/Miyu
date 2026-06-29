[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:Dofus](<../zh-cn/Talk:Dofus.html>)讨论)

**翻译状态：**

  * 本文（或部分内容）译自 [Dofus](<https://wiki.archlinux.org/title/Dofus> "arch:Dofus")，最近一次同步于 2020-05-06，若英文版本有所[更改](<https://wiki.archlinux.org/title/Dofus?diff=0&oldid=611183>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Dofus_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Dofus](<http://www.dofus.com>) 是 [Ankama](<http://www.ankama.com>) 制作的 MMORPG。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [ankama-launcher](<https://aur.archlinux.org/packages/ankama-launcher/>)AUR 包。 

当前，游戏文件安装在具有组可写性的“games”组下。您可以将用户添加到组中（`usermod -a -G games _username_`），以利用此优势。否则，您可能需要输入密码才能更新游戏文件。 

##  故障排除

要调试问题，在运行 Dofus 时设置 `AK_LOG_CONSOLE=1` 环境变量会很有帮助。然后它将在控制台中打印详细的日志。 

一个已知的问题是某些系统需要在环境中使用 `unset SESSION_MANAGER`，以避免启动时崩溃。 

有时由于先前运行的剩余过程，更新程序无法运行。杀死 `transition` 进程可以解决此问题。 
