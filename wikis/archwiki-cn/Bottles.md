**翻译状态：**

  * 本文（或部分内容）译自 [Bottles](<https://wiki.archlinux.org/title/Bottles> "arch:Bottles")，最近一次同步于 2024-08-31，若英文版本有所[更改](<https://wiki.archlinux.org/title/Bottles?diff=0&oldid=815651>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Bottles_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

Bottles 是一款使用 [GTK](<../zh-cn/GTK.html> "GTK") 框架、用 [Python](<../zh-cn/Python.html> "Python") 编写的 [Wine](<../zh-cn/Wine.html> "Wine") prefix 管理器。它可用于创建和管理 Wine prefix，以及自动处理各种 Wine runner 的安装、Windows 依赖项和某些 Windows 应用程序的安装。它还可用于在 prefix 中覆盖 Windows DLL 文件，并管理 Wine 会话的环境变量。 

它可用于运行本地 Windows 应用程序和游戏，在大多数情况下性能接近本地，在官方支持的模式下还支持应用程序沙盒。 

##  安装

**注意：** Bottles 开发人员强烈建议用户通过 [Flatpak](<../zh-cn/Flatpak.html> "Flatpak") 安装 Bottles，因为它用于沙箱。

使用以下命令从 Flatpak 安装 Bottles。 
    
    $ flatpak install bottles
    
此外，还可以通过安装 [bottles](<https://aur.archlinux.org/packages/bottles/>)AUR 和 [bottles-git](<https://aur.archlinux.org/packages/bottles-git/>)AUR 来安装 Bottles。 

##  用法

Bottles 的使用指南详见 [Bottles User Documentation](<https://docs.usebottles.com/>)。 

##  参见

  * [项目主页](<https://usebottles.com/>)
  * [项目文档](<https://docs.usebottles.com/>)
  * [项目 Github 页面](<https://github.com/bottlesdevs/Bottles>)
