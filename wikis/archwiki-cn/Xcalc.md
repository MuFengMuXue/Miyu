**翻译状态：**

  * 本文（或部分内容）译自 [Xcalc](<https://wiki.archlinux.org/title/Xcalc> "arch:Xcalc")，最近一次同步于 2024-8-1，若英文版本有所[更改](<https://wiki.archlinux.org/title/Xcalc?diff=0&oldid=813649>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Xcalc_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

**xcalc** 是 [X Window System](<../zh-cn/X_Window_System.html> "X Window System") 的[科学计算器](<https://en.wikipedia.org/wiki/Scientific_calculator> "wikipedia:Scientific calculator")。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [xorg-xcalc](<https://archlinux.org/packages/?name=xorg-xcalc>)包 软件包。 

##  配置

你可以在 [X resources](<../zh-cn/X_resources.html> "X resources") 文件中设置几个选项，让 xcalc 看起来比默认的白底黑字更好看。每个按钮的位置、标签、功能和颜色都可以单独更改。更多信息，请参见 [xcalc(1) § CUSTOMIZATION](<https://man.archlinux.org/man/xcalc.1#CUSTOMIZATION>)。 

###  主题

xcalc 有一个内置主题，模仿 [Texas Instruments TI-30](<https://en.wikipedia.org/wiki/TI-30> "wikipedia:TI-30") 的外观。如何启用该主题，请参见 [xcalc(1) § COLORS](<https://man.archlinux.org/man/xcalc.1#COLORS>)。 

如果你只是想要一些更漂亮的颜色，可以试试这个主题。 
    
    ~/.Xresources
    
    XCalc.geometry:                        200x275
    XCalc.stipple:                         true
    XCalc.ti.Command.background:           #777777
    XCalc.ti.Command.foreground:           White
    XCalc.ti.bevel.background:             #111111
    XCalc.ti.bevel.screen.DEC.background:  #000000
    XCalc.ti.bevel.screen.DEC.foreground:  LightSeaGreen
    XCalc.ti.bevel.screen.DEG.background:  #000000
    XCalc.ti.bevel.screen.DEG.foreground:  LightSeaGreen
    XCalc.ti.bevel.screen.GRAD.background: #000000
    XCalc.ti.bevel.screen.GRAD.foreground: LightSeaGreen
    XCalc.ti.bevel.screen.HEX.background:  #000000
    XCalc.ti.bevel.screen.HEX.foreground:  LightSeaGreen
    XCalc.ti.bevel.screen.INV.background:  #000000
    XCalc.ti.bevel.screen.INV.foreground:  Red
    XCalc.ti.bevel.screen.LCD.background:  #000000
    XCalc.ti.bevel.screen.LCD.foreground:  LightSeaGreen
    XCalc.ti.bevel.screen.LCD.shadowWidth: 0
    XCalc.ti.bevel.screen.M.background:    #000000
    XCalc.ti.bevel.screen.M.foreground:    LightSeaGreen
    XCalc.ti.bevel.screen.OCT.background:  #000000
    XCalc.ti.bevel.screen.OCT.foreground:  LightSeaGreen
    XCalc.ti.bevel.screen.P.background:    #000000
    XCalc.ti.bevel.screen.P.foreground:    Yellow
    XCalc.ti.bevel.screen.RAD.background:  #000000
    XCalc.ti.bevel.screen.RAD.foreground:  LightSeaGreen
    XCalc.ti.bevel.screen.background:      #000000
    XCalc.ti.button4.background:           Orange3
    XCalc.ti.button5.background:           Red4
    XCalc.ti.button23.background:          #611161
    XCalc.ti.button24.background:          #611161
    XCalc.ti.button35.background:          #611111
    XCalc.ti.button37.background:          #222262
    XCalc.ti.button38.background:          #222262
    XCalc.ti.button39.background:          #222262
    XCalc.ti.button40.background:          #722222
    XCalc.ti.button42.background:          #333373
    XCalc.ti.button43.background:          #333373
    XCalc.ti.button44.background:          #333373
    XCalc.ti.button45.background:          #833333
    XCalc.ti.button47.background:          #444484
    XCalc.ti.button48.background:          #444484
    XCalc.ti.button49.background:          #444484
    XCalc.ti.button50.background:          #944444
    XCalc.ti.button52.background:          #555595
    XCalc.ti.button53.background:          #555595
    XCalc.ti.button54.background:          #555595
    XCalc.ti.button55.background:          #a55555
    
###  更改分部标签

如果您愿意，可以将分隔符改为正斜线。 
    
    XCalc.ti.button35.label: /
    
###  桌面项

xcalc 不会显示在应用程序菜单中，因为它没有[桌面项](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%A1%B9.html> "桌面项")。要让它出现在菜单中，可以添加一个桌面项。 
    
    ~/.local/share/applications/xcalc.desktop
    
    [Desktop Entry]
    Name=XCalc
    GenericName=Scientific Calculator
    Comment=Scientific calculator for X
    Exec=xcalc
    Icon=accessories-calculator
    Terminal=false
    Type=Application
    StartupNotify=true
    Keywords=calculator;scientific;
    Categories=Utility;Calculator;

在 _Utility > Calculator_应用程序列表中，菜单项将显示为 _XCalc_ 。 

##  参见

  * [更改 xcalc 上的颜色](<https://bbs.archlinux.org/viewtopic.php?id=85918>)
  * [Xcalc 主题的神奇之处](<https://forums.bunsenlabs.org/viewtopic.php?id=3007>)
  * [xcalc 打扮得花枝招展！](<https://oldforum.puppylinux.com/viewtopic.php?t=83837>)
