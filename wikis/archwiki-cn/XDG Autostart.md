**翻译状态：**

  * 本文（或部分内容）译自 [XDG Autostart](<https://wiki.archlinux.org/title/XDG_Autostart> "arch:XDG Autostart")，最近一次同步于 2022-07-17，若英文版本有所[更改](<https://wiki.archlinux.org/title/XDG_Autostart?diff=0&oldid=726106>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/XDG_Autostart_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[XDG Autostart 规范](<https://specifications.freedesktop.org/autostart-spec/autostart-spec-latest.html>)定义了一种通过将其放置在特定[#目录](<#%E7%9B%AE%E5%BD%95>)中来在[桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")启动和可移动介质安装中[自动启动](<../zh-cn/%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8.html> "自动启动")普通[桌面项](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%A1%B9.html> "桌面项")的方法。 

##  先决条件

您需要使用支持它的[桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")或专用实现，例如： 

  * [dex](<https://archlinux.org/packages/?name=dex>)包
  * [dapper](<https://aur.archlinux.org/packages/dapper/>)AUR
  * [fbautostart](<https://aur.archlinux.org/packages/fbautostart/>)AUR
  * [sandsmark-xdg-autostart-launcher-git](<https://aur.archlinux.org/packages/sandsmark-xdg-autostart-launcher-git/>)AUR
  * [systemd-xdg-autostart-generator](<https://systemd.io/DESKTOP_ENVIRONMENTS/#xdg-autostart-integration>)

##  目录

按优先顺序排列的自动启动目录为： 

  * 用户特定：`$XDG_CONFIG_HOME/autostart`（默认为 `~/.config/autostart`）
  * 系统范围：`$XDG_CONFIG_DIRS/autostart`（默认为 `/etc/xdg/autostart`）[[1]](<https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html#referencing>)

系统范围的[桌面配置项](</wzh/index.php?title=%E6%A1%8C%E9%9D%A2%E9%85%8D%E7%BD%AE%E9%A1%B9&action=edit&redlink=1> "桌面配置项（页面不存在）")可以由具有相同文件名的用户特定配置项覆盖。 

**提示：** 要禁用系统范围的条目，请创建一个包含 `Hidden=true` 的替代配置项。

有关更多详细信息，请阅读[规范](<https://specifications.freedesktop.org/autostart-spec/autostart-spec-latest.html>)。 
