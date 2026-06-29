相关文章

  * [桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")

**翻译状态：**

  * 本文（或部分内容）译自 [Trinity](<https://wiki.archlinux.org/title/Trinity> "arch:Trinity")，最近一次同步于 2024-6-21，若英文版本有所[更改](<https://wiki.archlinux.org/title/Trinity?diff=0&oldid=810974>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Trinity_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

来自 Trinity Desktop Environment (TDE) [项目页面](<http://trinitydesktop.org/>)： 

    TDE 是一个完整的软件桌面环境，设计用于类 Unix 操作系统，面向喜欢传统桌面模式的计算机用户，是免费/自由软件。TDE 诞生于 2010 年，是 [KDE](<../zh-cn/KDE.html> "KDE") 3.5 的一个分叉。TDE 是一个完全独立的项目，有自己的个性和开发团队，适用于各种 Linux 发行版、BSD 和 DilOS。

TDE 仍然依赖于旧版本的 Qt，由于该 Qt 版本已经过时，他们现在自己维护该版本。 

Trinity 的应用程序和小程序也可用于其他桌面环境。 

##  安装

###  二进制软件包

从 [trinity](<../zh-cn/%E9%9D%9E%E5%AE%98%E6%96%B9%E7%94%A8%E6%88%B7%E4%BB%93%E5%BA%93.html#trinity> "非官方用户仓库") 资源库中安装 _tde-tdebase_ 软件包以获得基本的 Trinity 环境，或安装 _tde-meta_ 软件包以获得更完整的 Trinity 桌面环境。 

如果在[升级](<../zh-cn/%E7%B3%BB%E7%BB%9F%E7%BB%B4%E6%8A%A4.html#%E6%9B%B4%E6%96%B0%E7%B3%BB%E7%BB%9F> "升级")过程中出现任何错误，请按照[pacman/软件包签名#导入非官方密钥](<../zh-cn/Pacman/%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%AD%BE%E5%90%8D.html#%E5%AF%BC%E5%85%A5%E9%9D%9E%E5%AE%98%E6%96%B9%E5%AF%86%E9%92%A5> "Pacman/软件包签名")的方法添加 `0x8685AD8B` 密钥。 

###  从源代码构建

[Trinity 软件包存储库](<https://mirror.git.trinitydesktop.org/gitea/TDE/tde-packaging>)包含大多数 Trinity 软件包的 PKGBUILD 文件，这些文件位于 "arch "文件夹中。 

源代码在 git 仓库中。有关克隆的更多信息，请访问 [GIT 信息](<https://wiki.trinitydesktop.org/Project_GIT_Information#Using_GIT>)页面。 

[如何构建 TDE](<https://wiki.trinitydesktop.org/How_to_Build_TDE>)页面中说明了建议的构建顺序。 

**注意：** 请参阅[DeveloperWiki:Building in a clean chroot](</wzh/index.php?title=DeveloperWiki:Building_in_a_clean_chroot&action=edit&redlink=1> "DeveloperWiki:Building in a clean chroot（页面不存在）")，在 chroot 中构建软件包。

##  启动

###  手动

从 Linux 控制台启动 Trinity 
    
    $ startx /opt/trinity/bin/starttde
    
更多信息请参阅[xinit](<../zh-cn/Xinit.html> "Xinit")。 

###  图形化

_tde-tdebase_ 自带 TDE 显示管理器。要在启动时启动它，[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `tdm.service`。 

##  锦囊妙计

###  Trinity "Kicker" 面板和其他桌面环境

要在其他桌面环境中使用 Trinity "kicker "桌面面板和小程序，请创建此脚本并使其[可执行](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "可执行")。对于 Plasma5，使用"'系统设置 > 启动和关机 > 自动启动 > 添加脚本'"。 
    
    #!/bin/bash
    /opt/trinity/bin/tdeinit
    /opt/trinity/bin/kicker
    /opt/trinity/bin/tdebuildsycoca --noincremental
    
##  问题解决

###  TDE 显示管理器

如果遇到任何问题，可能需要手动配置 `default.target`。有关解决方法，请参见[显示管理器#加载显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html#%E5%8A%A0%E8%BD%BD%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8> "显示管理器")。 

##  参见

  * [TDE Git 仓库](<https://git.trinitydesktop.org/cgit/>)
  * [TDE bug追踪](<http://bugs.trinitydesktop.org/>)
  * [邮件列表](<http://trinitydesktop.org/mailinglist.php>)
  * [Developers Web](<https://wiki.trinitydesktop.org/Category:Developers>)
  * [QT and TQT Tutorials and Documentation](<https://wiki.trinitydesktop.org/Category:Developers#Tutorials_and_Documentation_for_QT_and_TQT>)
  * [怎样构建](<https://wiki.trinitydesktop.org/Category:Developers#Building_and_Distributing_Trinity>)
