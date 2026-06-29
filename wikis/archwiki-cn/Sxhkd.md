相关文章

  * [Xbindkeys](</wzh/index.php?title=Xbindkeys&action=edit&redlink=1> "Xbindkeys（页面不存在）")
  * [Xmodmap](<../zh-cn/Xmodmap.html> "Xmodmap")

**翻译状态：**

  * 本文（或部分内容）译自 [Sxhkd](<https://wiki.archlinux.org/title/Sxhkd> "arch:Sxhkd")，最近一次同步于 2024-7-3，若英文版本有所[更改](<https://wiki.archlinux.org/title/Sxhkd?diff=0&oldid=811837>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Sxhkd_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[sxhkd](<https://github.com/baskerville/sxhkd>)是一个简单的 [X](<../zh-cn/Xorg.html> "X") 热键守护进程，由 [bspwm](<../zh-cn/Bspwm.html> "Bspwm") 的开发者设计，能通过执行命令对输入事件做出反应。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [sxhkd](<https://archlinux.org/packages/?name=sxhkd>)包 或 [sxhkd-git](<https://aur.archlinux.org/packages/sxhkd-git/>)AUR。 

##  配置

sxhkd 默认使用 `$XDG_CONFIG_HOME/sxhkd/sxhkdrc` 作为配置文件。可以使用 `-c` 选项指定其他配置文件。 

配置文件中的每一行都是这样解释的： 

  * 如果以 `#` 开头，则会被忽略。
  * 如果以一个或多个空白命令开头，则作为命令读取。
  * 否则，将作为热键进行解析：每个键名之间用空格和/或 `+` 字符分隔。

通用语法： 
    
    [MODIFIER + ]*[@]KEYSYM
        COMMAND
    
其中 `MODIFIER` 是以下名称之一： `super`、`hyper`、`meta`、`alt`、`control`、`ctrl`、`shift`、`mode_switch`、`lock`、`mod1`、`mod2`、`mod3`、`mod4`、`mod5`。如果在 keysym 的开头添加了 `@`，命令将在按键释放事件中运行，否则将在按键按下事件中运行。`KEYSYM`名称是从`xev`中获取的。 

鼠标热键可通过使用以下特殊 keysym 名称之一来定义： `button1`、`button2`、`button3`、...、`button24`。热键可以包含`STRING_1`, ...,`STRING_N`} 形式的序列，在这种情况下，命令还必须包含一个包含 _N_ 元素的序列：两个序列配对生成 _N_ 热键。如果命令中包含大括号（`{`, `}`），例如：`awk '{print $1}'` ，请使用反斜线 `\` 来转义，例如：`awk '\{print$1/}'`。此外，序列可以包含 `A-Z` 形式的范围，其中 _A_ 和 _Z_ 是字母数字字符。 

实际执行的是 `SHELL -c COMMAND`，这意味着可以在 `COMMAND` 中使用环境变量。`SHELL`将是以下列表中第一个定义的环境变量的内容： `SXHKD_SHELL`、`SHELL`。如果 sxhkd 收到 `SIGUSR1` 信号，它将重新加载配置文件。 

###  例子
    
    $XDG_CONFIG_HOME/sxhkd/sxhkdrc
    
    # On mouse button 1 press Alt_R+F1
    button1
        xte "keydown Alt_R" "keydown F1" "keyup Alt_R" "keyup F1"
    
    # 按下鼠标 button 2，暂停 3 秒，然后按 Alt_R+F2 button2
        xte "sleep 3" "keydown Alt_R" "keydown F2" "keyup Alt_R" "keyup F2"
    
####  将命令绑定到一个按键上

[![](../File:Tango-preferences-desktop-locale-modified.png)](<../File:Tango-preferences-desktop-locale-modified.png>)**这篇文章或章节的[翻译](<../Project:%E8%B4%A1%E7%8C%AE.html#Translating> "Project:Contributing")质量不佳。**

**原因：** 表述与翻译存在问题。（在 [Talk:Sxhkd#](<../zh-cn/Talk:Sxhkd.html>) 中讨论）

有些用户可能希望将命令绑定到单个按键上，就像在 Windows 中使用 `Super` 键打开"开始"菜单一样。在 sxhkd 中，这可以通过绑定到由单个 keysym 的按键按下和按键释放事件组成的 chord chain 来实现，如下所示： 
    
    $XDG_CONFIG_HOME/sxhkd/sxhkdrc
    
    # Program launcher
    Super_L; @Super_L
        rofi -show drun
    
这种复杂的模式是必要的，因为如果没有明确的 chord chain（即单一的 `@Super_L`），sxhkd 将在 "任何 "释放按键时触发绑定，即使该按键被用于另一个 chord chain。此外，由于 sxhkd 不支持在修饰符中使用 `@` 符号（表示按键释放），因此必须使用按键符号来代替修饰符（`Super_L` 而不是 `super`）。 

##  用法

配置完成后，您可能希望将 sxhkd 设置为[自动启动](<../zh-cn/%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8.html> "自动启动")；有关详情，请参阅桌面环境或窗口管理器的相应文章。 

如果您的桌面环境支持[Desktop Application Autostart Specification](<https://specifications.freedesktop.org/autostart-spec/autostart-spec-latest.html>)，则可以通过在恰当目录下创建 `sxhkd.desktop` 文件以启动 sxhkd： 
    
    ~/.config/autostart/sxhkd.desktop
    
    [Desktop Entry]
    Name=sxhkd
    Comment=Simple X hotkey daemon
    Exec=/usr/bin/sxhkd
    Terminal=false
    Type=Application

##  参见

  * [官方网站](<https://github.com/baskerville/sxhkd>) \- 包括配置选项、绑定示例和源代码。
  * [Arch Linux forum thread](<https://bbs.archlinux.org/viewtopic.php?id=155613>)
