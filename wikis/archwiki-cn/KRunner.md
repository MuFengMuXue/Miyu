**翻译状态：**

  * 本文（或部分内容）译自 [KRunner](<https://wiki.archlinux.org/title/KRunner> "arch:KRunner")，最近一次同步于 2021-07-31，若英文版本有所[更改](<https://wiki.archlinux.org/title/KRunner?diff=0&oldid=690014>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/KRunner_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [KDE](<../zh-cn/KDE.html> "KDE")

[KRunner](<https://userbase.kde.org/Plasma/Krunner>) 是 [Plasma](<../zh-cn/KDE.html> "Plasma") 5 中内置的搜索应用, 能够快速的启动应用程序以及运行命令, 并且具有一个"runner"系统, 用户可以自定义可用的功能. 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [krunner](<https://archlinux.org/packages/?name=krunner>)包 软件包. 

##  使用方法

需要在Plasma桌面中运行KRunner, 你可以右键单击桌面然后从菜单中选择"run command"(中文环境下为"显示KRunner"), 也可以使用键盘快捷键 `Alt+Space` 或者 `Alt+F2` 来启动KRunner. 在某些工作区状态下(例如一个空白的桌面), 直接在键盘上输入就会自动唤醒KRunner. 

##  使用Meta键唤醒KRunner

为了使用Meta键作为启动KRunner的快捷键, 请运行命令 
    
    kwriteconfig5 --file kwinrc --group ModifierOnlyShortcuts --key Meta "org.kde.krunner,/App,,display"
    
要将更改应用于当前会话，使用qdbus向KWin发送特定的DBus信号： 
    
    qdbus org.kde.KWin /KWin reconfigure

如果不使用DBus那么需要重启KWin才能够生效： 
    
    kwin_x11 --replace # For X11
    kwin_wayland --replace # For wayland

##  更改被激活的窗口

Plasma 5 桌面不包含默认的方式来指定krunner仅由活动窗口标题来进行搜索. 以下方法可用于解决此问题. 

###  使用生成的完整窗口列表来搜索窗口标题

此方法要求系统中安装了 [xdotool](<https://archlinux.org/packages/?name=xdotool>)包 软件包. 

  1. 打开 _系统设置 > 工作区 > 快捷键 > 自定义快捷键_.
  2. 右键列表新建一个全局快捷键, 并选择 命令/URL: 项
  3. 勾选名称右边的复选框.
  4. 在触发器选项卡中点击按钮来设置所需的快捷键组合.
  5. 在动作选项卡中输入 `/usr/local/bin/krunner-search-by-windows.sh`
  6. 创建文件 `/usr/local/bin/krunner-search-by-windows.sh` 并输入以下内容: 
         
         #!/bin/bash
         qdbus org.kde.krunner /App querySingleRunner windows "" 
         sleep 0.2
         xdotool type 'window '
         xdotool key "shift+BackSpace"

  7. 给文件赋予运行权限: 
         
         chmod a+x /usr/local/bin/krunner-search-by-windows.sh

输入上面的内容时要注意 `window` 后面的空格. 

现在你可以通过你指定的快捷键来获得已打开窗口的列表, 并在键入时根据该列表进行搜索; 

###  在没有完整窗口列表的情况下搜索窗口标题

这种方法局限性会大一些, 但没有上面那种方法那么丑. 

  1. 打开 _系统设置 > 工作区 > 快捷键 > 自定义快捷键_.
  2. 右键新建一个全局快捷键, 并选择 D-bus 命令
  3. 勾选名称右边的复选框.
  4. 在触发器选项卡中点击按钮来设置所需的快捷键组合.
  5. 在 动作 选项卡中填写下面这些信息:

      - 远程应用程序         : org.kde.krunner
      - 远程对象            : /App
      - 函数                : querySingleRunner
      - 参数                : windows ""
    
##  参见

  * [KRunner on KDE UserBase Wiki](<https://userbase.kde.org/Plasma/Krunner>)
