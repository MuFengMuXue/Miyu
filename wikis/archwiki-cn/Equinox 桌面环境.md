**翻译状态：**

  * 本文（或部分内容）译自 [Equinox Desktop Environment](<https://wiki.archlinux.org/title/Equinox_Desktop_Environment> "arch:Equinox Desktop Environment")，最近一次同步于 2021-06-03，若英文版本有所[更改](<https://wiki.archlinux.org/title/Equinox_Desktop_Environment?diff=0&oldid=675326>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Equinox_Desktop_Environment_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")

[Equinox Desktop Environment](<https://edeproject.org/>)（EDE）是一种桌面环境，旨在简单，轻巧和快速。 

它主要提供最基本的功能：窗口管理器（默认情况下使用 [PekWM](</wzh/index.php?title=PekWM&action=edit&redlink=1> "PekWM（页面不存在）")），包含面板的简单 GUI，监视可移动媒体的守护程序和通知守护程序。除此之外，只剩下一些配置程序，计算器等。从 2.0 版开始，EDE 遵循 FreeDesktop.org 准则。 

与其他桌面环境不同，EDE 基于 [FLTK 工具包](<https://fltk.org>)。它特别适合于 RAM 很少的系统，或者想要完全自定义系统并需要功能和应用程序尚未膨胀的 GUI 的用户。 

##  安装

可以使用 [ede](<https://aur.archlinux.org/packages/ede/>)AUR 包从 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") EDE。 

或者，您可以从[#自定义存储库](<#%E8%87%AA%E5%AE%9A%E4%B9%89%E5%AD%98%E5%82%A8%E5%BA%93>)中获取它。 

###  自定义存储库

要启用 EDE 的[非官方用户存储库](</wzh/index.php?title=%E9%9D%9E%E5%AE%98%E6%96%B9%E7%94%A8%E6%88%B7%E5%AD%98%E5%82%A8%E5%BA%93&action=edit&redlink=1> "非官方用户存储库（页面不存在）")，请将以下行添加到 `/etc/pacman.conf` 中： 
    
    [ede]
    SigLevel = Optional
    Server = http://ede.elderlinux.org/repos/archlinux/$arch
    
接下来[刷新软件包列表](<../zh-cn/%E9%95%9C%E5%83%8F%E6%BA%90.html#Force_pacman_to_refresh_the_package_lists> "Mirrors")，并通过 [pacman](<../zh-cn/Pacman.html> "Pacman") [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") EDE 软件包： 

  * _edelib_
  * _ede-common_
  * _ede_
  * _ede-wallpapers_ (optional)

##  启动桌面环境

要启动 EDE，可以使用[显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")或使用 startx。如果选择后者，只需将以下内容写入用户的 `.xinitrc`： 
    
     exec startede
    
##  应用

由于 EDE 是基本的桌面环境，因此您甚至必须自己添加最常见的应用程序，例如文件管理器或编辑器。您有选择的自由。 

由于这个桌面环境的性质，安装轻量级软件显然很有意义。但是，没有太多的 [FLTK](<https://fltk.org>) 应用程序可用，因此您可能不得不依靠第二个工具包，例如 [GTK](<../zh-cn/GTK.html> "GTK")。 

###  一些建议

  * 文件管理器：[PCManFM](<../zh-cn/PCManFM.html> "PCManFM")
  * 浏览器：[Dillo](<../zh-cn/Dillo.html> "Dillo") 或 [Midori](</wzh/index.php?title=Midori&action=edit&redlink=1> "Midori（页面不存在）")
  * 编辑器：[Leafpad](<http://tarot.freeshell.org/leafpad/>)
  * 终端模拟器：[Xterm](</wzh/index.php?title=Xterm&action=edit&redlink=1> "Xterm（页面不存在）")
