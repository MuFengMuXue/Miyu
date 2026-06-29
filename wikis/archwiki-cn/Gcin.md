**翻译状态：**

  * 本文（或部分内容）译自 [Gcin](<https://wiki.archlinux.org/title/Gcin> "arch:Gcin")，最近一次同步于 2020-07-14，若英文版本有所[更改](<https://wiki.archlinux.org/title/Gcin?diff=0&oldid=625190>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Gcin_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Gcin](<https://hyperrate.com/dir.php?eid=67>) 是 Edward Liu 开发的新一代中文[输入法](<../zh-cn/Input_method.html> "Input method")服务器。 Gcin 支持各种输入方法，并且可以在大多数类 Unix 操作系统下运行。 它是台湾最受欢迎的中文输入引擎之一。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [gcin](<https://archlinux.org/packages/?name=gcin>)包 软件包。 

###  安装其他输入法表格

##  配置

###  自动启动

使用 [xprofile](<../zh-cn/Xprofile.html> "Xprofile") 以自动执行以下命令： 
    
    export XMODIFIERS=@im=gcin
    export LC_CTYPE=zh_TW.UTF-8
    gcin &
    
##  用法

###  对于 GNOME/GTK 2 应用程序

gcin 提供了一个 gtk 输入模块，因此直接支持所有基于 gtk2 的应用程序，安装后无需进行任何配置（它不是 XIM，gcin 会在需要时自动启动）。 

###  对于其他应用程序

1\. 将环境语言环境设置为使用 UTF-8，例如： 
    
    export LC_CTYPE=en_US.UTF-8
    
**注意：** 必须设置 LC_CTYPE 语言环境，即使 LC_CTYPE 与 LANG 相同，也，否则gcin可能不会在使用x输入的非gtk2程序中激活。

2\. 设置 XMODIFIERS： 
    
    export XMODIFIERS=@im=gcin
    
gcin 默认使用名称“gcin”，您可以使用环境变量 GCIN_XIM 进行更改，以便运行多个 gcin 程序，例如： 
    
    export GCIN_XIM=gcin_zh
    export XMODIFIERS=@im=gcin_zh
    
请记住，如果 gtk2 应用程序不存在，它将自动启动 gcin 的一个程序。 

3\. 启动 gcin： 
    
    gcin &
    
4\. 运行您的应用程序！如果在您的应用程序运行时 gcin 被杀死，则很可能导致崩溃或其他问题。 

###  Wine/Crossover Office 的其他说明

  1. 如果运行 wine 或 Crossover Office，最好使用 Windows 2000 模拟而不是 Windows 98，并且必须至少使用 LC_CTYPE=zh_TW.utf8 启动 gcin 和 wine/cxoffice，否则 wine 将无法正确显示中文。
  2. 在具有 Windows 98 仿真的 wine+IE6 中，如果您想在网页上输入中文，LC_CTYPE 是不够的 - 您必须将 LANG 或 LC_ALL 设置为 zh_TW.utf8，这会大大降低 Wine 的速度。但是，您始终可以在位置栏中或其他位置键入中文，然后将其粘贴。
