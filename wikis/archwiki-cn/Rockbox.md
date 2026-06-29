**翻译状态：**

  * 本文（或部分内容）译自 [Rockbox](<https://wiki.archlinux.org/title/Rockbox> "arch:Rockbox")，最近一次同步于 2020-07-19，若英文版本有所[更改](<https://wiki.archlinux.org/title/Rockbox?diff=0&oldid=625965>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Rockbox_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Codecs](<../zh-cn/%E7%BC%96%E8%A7%A3%E7%A0%81%E5%99%A8%E4%B8%8E%E5%AE%B9%E5%99%A8.html> "Codecs")
  * [FAT](<../zh-cn/FAT.html> "FAT")

[Rockbox](<https://www.rockbox.org>) 是数字音频播放器（MP3 播放器）的免费替代固件。它的增强功能包括对几乎所有编解码器，高级声音设置，应用程序，实用程序和游戏的支持。 

**提示：** Rockbox 通常可以与原始固件一起安装。

##  支持的设备

检查您的设备是否具有可用的 Rockbox 端口：<https://www.rockbox.org/>. 

##  安装

### Rockbox Utility

可以使用 [rbutil](<https://archlinux.org/packages/?name=rbutil>)包 软件包[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")管理 Rockbox 的官方工具。[Rockbox Utility](<https://www.rockbox.org/wiki/RockboxUtility>) 可以安装替换引导加载程序，主固件以及字体，主题和应用程序等任何其他功能。 

###  在设备上安装 Rockbox

Rockbox 项目具有出色的安装说明。您可以在 <https://www.rockbox.org/manual.shtml> 上找到它们。 

####  引导加载程序

建议使用 [#Rockbox Utility](<#Rockbox_Utility>) 安装引导加载程序。为了让 Rockbox Utility 检测您的播放器，它必须具有对播放器内部磁盘的写访问权。 

**提示：** 由于您需要对播放器磁盘进行写访问，因此可以在挂载时赋予它。例如（作为 root 用户运行）：`mount -o uid=1000,gid=1000 /dev/sdb /mnt`.

##  备份

[#Rockbox Utility](<#Rockbox_Utility>) 可以备份您的设备。 
