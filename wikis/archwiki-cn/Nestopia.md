**翻译状态：**

  * 本文（或部分内容）译自 [Nestopia](<https://wiki.archlinux.org/title/Nestopia> "arch:Nestopia")，最近一次同步于 2020-05-03，若英文版本有所[更改](<https://wiki.archlinux.org/title/Nestopia?diff=0&oldid=610289>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Nestopia_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Nestopia](<https://github.com/0ldsk00l/nestopia>) 是一个开源的 NES 模拟器，它试图尽可能准确地模拟 NES 硬件。它适用于 Windows、macOS、Linux 和 BSD。也有一个 libretro 端口，有关更多信息，请参见 [RetroArch](</wzh/index.php?title=RetroArch&action=edit&redlink=1> "RetroArch（页面不存在）")。 

##  安装

从 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 安装 [nestopia](<https://aur.archlinux.org/packages/nestopia/>)AUR 包。或者，安装 [nestopia-git](<https://aur.archlinux.org/packages/nestopia-git/>)AUR 开发版本。 

##  问题解决

###  libao 后端无音频

目前，libao 后端已损坏。建议在 _Emulator - > Configuration -> Audio_ 中将音频 API 更改为 _SDL_ 。 

##  参见

  * [官方网站](<http://0ldsk00l.ca/nestopia/>)
  * [GitHub 页面](<https://github.com/0ldsk00l/nestopia>)
  * [NES 游戏列表](<https://nesdir.github.io/>)
