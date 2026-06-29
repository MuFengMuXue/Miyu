  
**翻译状态：**

  * 本文（或部分内容）译自 [CrossOver](<https://wiki.archlinux.org/title/CrossOver> "arch:CrossOver")，最近一次同步于 2025-07-28，若英文版本有所[更改](<https://wiki.archlinux.org/title/CrossOver?diff=0&oldid=840822>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/CrossOver_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[CrossOver](<https://www.codeweavers.com/crossover>) is the paid, commercialized version of [Wine](<../zh-cn/Wine.html> "Wine") which provides more comprehensive end-user support. It includes scripts, patches, a [GUI](<https://en.wikipedia.org/wiki/Graphical_user_interface> "wikipedia:Graphical user interface"), and third-party software which may never be accepted in the Wine Project. This combination makes running Windows programs considerably easier for those less tech-savvy. [CrossOver](<https://www.codeweavers.com/crossover>) 是 [Wine](<../zh-cn/Wine.html> "Wine") 的一个付费的，产业化的版本，为最终使用产品的人提供技术的帮助与支持。它包括脚本，补丁，[GUI](<https://en.wikipedia.org/wiki/Graphical_user_interface> "wikipedia:Graphical user interface") 界面和一些没有被 Wine 项目接受的第三方软件。这些特点的结合使 Windows 程序的运行更加简单和方便。 

##  安装

本文建议你安装 crossover 试用版本。[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [crossover](<https://aur.archlinux.org/packages/crossover/>)AUR 包。 

##  用法

如果由用户安装了 _单用户模式_ ，Crossover 二进制库会在 `~/cxoffice` 中。Windows 应用程序和配置文件将被放在 `~/.cxoffice` 中。 

如果由 root 权限安装了 _多用户模式_ ，Crossover 二进制库会在 `/opt/cxoffice` 中。每个用户的运行环境在 `~/.cxoffice` 中。 

像 [KDE](<../zh-cn/KDE.html> "KDE") 这样的一些桌面环境可能会自动地把菜单项目当作安装过程。 

安装的程序应该位于 _Window Applications_ 的菜单项目下。 

**提示：** 如果你注册失败，请尝试用 root 权限执行 `/opt/cxoffice/bin/cxregister`。之后注册应该对系统上的所有用户是有效完成的。

##  疑难解答

There is also a way to generate a log file to assist you in tracking down errors that may be preventing you from running your desired Windows application(s). Follow the menu path _CrossOver > Run a Windows Command > Debug Options_ and click the "+" sign to expand the options. Click the "Create log file" checkbox. Enter the command you would use to run your Windows application in the "Command" text box. You can use the browse button, if you are not sure what to enter, to navigate to your Windows application. CrossOver will prompt you for a location to save the log file. Choose your location and press enter to have Crossover generate the log file in it. 

Although the `libSM.so` library was not shown in the cxdiag list of missing libraries - it did appear in the log file. The library belongs to the [libsm](<https://archlinux.org/packages/?name=libsm>)包 package. If you are having problems getting your application to run, check its installation status. 
