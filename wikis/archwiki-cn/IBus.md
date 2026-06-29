[![](../File:Tango-preferences-desktop-locale-modified.png)](<../File:Tango-preferences-desktop-locale-modified.png>)**这篇文章或章节的[翻译](<../Project:%E8%B4%A1%E7%8C%AE.html#Translating> "Project:Contributing")质量不佳。**

**原因：** Looks nothing like the structure of the English page.（在 [Talk:IBus#](<../zh-cn/Talk:IBus.html>) 中讨论）

相关文章

  * [Fcitx](<../zh-cn/Fcitx.html> "Fcitx")
  * [Fcitx5](<../zh-cn/Fcitx_5.html> "Fcitx5")
  * [SCIM](</wzh/index.php?title=SCIM&action=edit&redlink=1> "SCIM（页面不存在）")
  * [UIM](</wzh/index.php?title=UIM&action=edit&redlink=1> "UIM（页面不存在）")

[IBus](<https://en.wikipedia.org/wiki/Intelligent_Input_Bus> "w:Intelligent Input Bus") ("Intelligent Input Bus") 是一个[输入法框架](<https://en.wikipedia.org/wiki/Input_method> "w:Input method")，允许用户便捷地在不同的键盘布局中切换。当IBus框架和特定的[输入法](<../zh-cn/%E8%BE%93%E5%85%A5%E6%B3%95.html> "输入法")结合使用时，你就可以使用你的键盘输入键盘本身所不支持的非拉丁字母。（译者注：即在ArchLinux——其他Linux也类似，输入法需要和一个框架搭配使用，IBus就起到这个框架的作用） 

##  安装

安装 [ibus](<https://archlinux.org/packages/?name=ibus>)包 软件包。

**注意：**[GNOME](<../zh-cn/GNOME.html> "GNOME")自从3.6版本以来，就[集成](<https://help.gnome.org/misc/release-notes/3.6/i18n-ibus.html.en>)了IBus，并默认使用。所以如果你使用3.6版本以上的GNOME作为你的[桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")，你可以跳过这一步。

###  输入法引擎

至少需要一种与所用语言相应的输入法。您可以在[输入法#输入法列表](<../zh-cn/%E8%BE%93%E5%85%A5%E6%B3%95.html#%E8%BE%93%E5%85%A5%E6%B3%95%E5%88%97%E8%A1%A8> "输入法")查看IBus支持的输入法列表。部分可用的输入法如下，如您发现无法使用，请前往[输入法#输入法列表](<../zh-cn/%E8%BE%93%E5%85%A5%E6%B3%95.html#%E8%BE%93%E5%85%A5%E6%B3%95%E5%88%97%E8%A1%A8> "输入法")查看并积极反馈以更新该内容 

####  中文引擎

  * [ibus-pinyin](<https://archlinux.org/packages/?name=ibus-pinyin>)包：一个智能中文输入法引擎，支持汉语拼音与注音符号。设计者为 Ibus 的主要作者，而且有许多的高级功能（如英文拼错修改）。
  * [ibus-libpinyin](<https://archlinux.org/packages/?name=ibus-libpinyin>)包：一个强大的智能中文输入引擎，基于 libpinyin，提供了比 ibus-pinyin 更强大的功能，支持动态调整字频、云输入，可以添加用户词典
  * [ibus-rime](<https://archlinux.org/packages/?name=ibus-rime>)包：一个强大的智能中文输入法，支持拼音、注音或者没有音调的拼音、双拼、粤拼、中州韵、仓颉和五笔 86。
  * [ibus-chewing](<https://archlinux.org/packages/?name=ibus-chewing>)包：一个智能中文输入法引擎，支持注音符号，基于 [libchewing](<https://archlinux.org/packages/?name=libchewing>)包。

####  日文引擎

  * [ibus-anthy](<https://archlinux.org/packages/?name=ibus-anthy>)包：日文输入法引擎，基于 [anthy](<https://archlinux.org/packages/?name=anthy>)包。
  * [ibus-mozc](<https://aur.archlinux.org/packages/ibus-mozc/>)AUR：谷歌日文输入法的开源版本，基于 [Mozc](</wzh/index.php?title=Mozc&action=edit&redlink=1> "Mozc（页面不存在）")。
  * [ibus-kkc](<https://archlinux.org/packages/?name=ibus-kkc>)包：日文输入法引擎，基于 [libkkc](<https://archlinux.org/packages/?name=libkkc>)包。
  * [ibus-skk](<https://archlinux.org/packages/?name=ibus-skk>)包：日文假名转汉字输入法引擎，基于 [libskk](<https://archlinux.org/packages/?name=libskk>)包。

####  越南文引擎

  * [ibus-bamboo](<https://aur.archlinux.org/packages/ibus-bamboo/>)AUR：越南文输入法引擎，基于 Bamboo 引擎。
  * [ibus-bogo](<https://aur.archlinux.org/packages/ibus-bogo/>)AUR：越南文输入法引擎，基于 Bogo。（已停止开发）
  * [ibus-unikey](<https://archlinux.org/packages/?name=ibus-unikey>)包：用于输入越南字的输入法引擎。（已停止开发）

####  其他引擎

  * [ibus-hangul](<https://archlinux.org/packages/?name=ibus-hangul>)包：一个韩文输入法，基于 [libhangul](<https://archlinux.org/packages/?name=libhangul>)包。
  * [ibus-table](<https://archlinux.org/packages/?name=ibus-table>)包：一个支持查表型输入法的输入法引擎。
  * [ibus-m17n](<https://archlinux.org/packages/?name=ibus-m17n>)包：一个 m17n 输入法引擎，可以用 m17n-db 数据库中的输入法来输入许多语言。

查看所有可用的输入法： 
    
    $ pacman -Ss ^ibus-*
    
其他软包也供给于 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR")。 

##  环境适配

请按照如下示例设置[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")
    
    /etc/environment
    
    GTK_IM_MODULE=ibus
    QT_IM_MODULE=ibus
    XMODIFIERS=@im=ibus

如果你希望当你登录时，IBus就启动，请使用以下命令创建一个[自动启动](<../zh-cn/%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8.html> "自动启动")条目： 
    
     ibus-daemon -rxRd
    
这样，下次登录时，IBus就会随着用户会话而自动启动

**提示：** * [ibus-autostart](<https://aur.archlinux.org/packages/ibus-autostart/>)AUR 软件包提供了一个[自动启动](<../zh-cn/%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8.html> "自动启动") 条目来自动启动该服务 

  * [ibus-daemon](<https://aur.archlinux.org/packages/ibus-daemon/>)AUR软件包提供了一个服务`ibus@$DISPLAY.service`，可以[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")它来达到这个目的
  * [KDE](<../zh-cn/KDE.html> "KDE")提供了一个Plasm形式的 _输入面板_ ，可以作为IBus的前端，以提供更好的输入体验 
    * 欲启动有 _输入面板_ 的IBus，请在 _ibus-daemon_ 命令中加入 `--panel=/usr/lib/kimpanel-ibus-panel`选项。（如果面板没有出现，你还可以尝试用`--desktop=kde`选项。要配置*输入面板*的宽度，请参见[KDE UserBase Wiki](<https://userbase.kde.org/Tutorials/Kimpanel>)和[KDE#Widgets](<https://wiki.archlinux.org/title/KDE#Widgets>)
    * [ibus-autostart-kimpanel](<https://aur.archlinux.org/packages/ibus-autostart-kimpanel/>)AUR软件包提供了一个可以自启动该功能的[自动启动](<../zh-cn/%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8.html> "自动启动")条目

译者注：[KDE#Widgets](<https://wiki.archlinux.org/title/KDE#Widgets>)这一章节由于[KDE](<../zh-cn/KDE.html> "KDE")翻译的过时，无法链接到最新的中文章节，遂在此链接了原文Wiki的链接。如翻译有所跟进，请随时修改。

##  配置

你可能需要先设置系统的语言环境，请： 

  1. 参见[Locale](<../zh-cn/Locale.html> "Locale")来获取关于在系统中安装非拉丁文字体的帮助
  2. 参见[字体#非拉丁文字](<../zh-cn/%E5%AD%97%E4%BD%93.html#%E9%9D%9E%E6%8B%89%E4%B8%81%E6%96%87%E5%AD%97> "字体")获取可用的非拉丁字体的不完全列表

### GNOME

[GNOME](<../zh-cn/GNOME.html> "GNOME")默认使用IBus，因此你只需简单地打开 _设置 >键盘>输入源_并添加你所使用的键盘布局即可。 

一些非拉丁语言（如简体中文）需要在[GNOME Tweaks](<https://gitlab.gnome.org/GNOME/gnome-tweaks>)中启用 _显示拓展输入源_ 选项 

###  其他桌面环境

**提示：** 对于[Wayland](<../zh-cn/Wayland.html> "Wayland")环境，请参见[WaylandDesktop](<https://github.com/ibus/ibus/wiki/WaylandDesktop>)

要启动IBus偏好设置窗口，你可以执行以下任一操作： 

  * 右键IBus的托盘图标，选择 _偏好_ ；
  * 找到并启动IBus偏好设置的图形化应用程序；
  * 在终端中运行命令`ibus-setup`

在这个窗口，主要有两个重要的功能：一是 _下一个输入法_ 的快捷键（建议你设置这个选项，来替代你的桌面环境所提供的快捷键）；二是 _输入法_ 页面，你可以在这里添加或者删除不同的键盘布局（建议你在此处操作，而不是在桌面环境所默认提供键盘布局管理器操作） 

##  使用提示和技巧

###  moji 输入

IBus支持Emoji表情符号的输入。按下快捷键`Super+.`即可看到输入模式变为一个下划线 _e_ 字符。接下来你可以输入符号或emoji的名称（例如 _:)_ 或 _face)_ ）并敲击Space键（空格键）渲染该符号。如果你对该结果表示满意，你可以按下回车来输入该符号并推出Emoji输入模式。或者你也可以再次按下空格键，来打开一个对话框，以便于你进一步选择你需要的符号。 

###  Unicode输入

IBus支持输入复杂的Unicode字符。使用快捷键`Ctrl+Shift+u`即可看到输入模式变为一个下划线 _u_ 字符。你可以输入Unicode代码并按`Space` 或 `Enter` 来渲染并输入该字符 

###  托盘图标颜色

IBus默认使用蓝色来显示当前正活跃的键盘布局（如**EN** ）这个颜色值存储在[gestting schema](<../zh-cn/GNOME.html#%E9%85%8D%E7%BD%AE> "GNOME")中，因此如果你希望修改他，请执行如下命令： 
    
    $ gsettings set org.freedesktop.ibus.panel xkb-icon-rgba 'COLOR'

其中，'COLOR'是字符串形式，遵循如下要求： 

是一个RGBA值，即： 

  1. 一个X11中的颜色名称
  2. 一个十六进制数值，如'#rrggbb'，r,g,b分别是红、绿、蓝的十六进制数
  3. 一个如下格式的RGB数值：'rgb(r,g,b)'
  4. 一个RGBA颜色，应该如下格式：'rgba(r,g,b,a)'，其中r,g,b都是[0,255]范围内的数值或[0%,100%]范围内的百分数，而a是[0,1]范围内的浮点数，以表示透明度

**提示：** 你也可以使用[dconf-editor](<https://archlinux.org/packages/?name=dconf-editor>)包来以一种更友好的方式修改设置模式（gsettings schema）

**注意：** 这不适用于 [GNOME](<../zh-cn/GNOME.html> "GNOME") 或存在KDE输入法面板的 [KDE](<../zh-cn/KDE.html> "KDE")，因为它们都为 IBus 提供了自己的图标。

##  疑难解答

### rxvt-unicode

如果有 ibus 与 [rxvt-unicode](<https://archlinux.org/packages/?name=rxvt-unicode>)包 包的问题，以下的步骤应该能够解决。 

将以下的两行代码添加到你的 `~/.Xresources` 文件（可能不需要，先尝试，如果问题出现，再添加代码）： 
    
      URxvt.inputMethod: ibus
      URxvt.preeditType: OnTheSpot,None
    
然后用以下的命令启动Ibus: 
    
      ibus-daemon --xim
    
如果 ibus-daemon 自动开启（如在 `~/.xinitrc` 或 `~/.xsession` 中)，但是以前执行 `ibus-daemon &` 没有用 `--xim` 选项，确保先结束已打开的进程，再尝试新命令。 

###  GTK 应用程序

有些用户在 GTK 应用程序下使用输入法时会因为无法找到 gtk.immodules 文件而出现问题。在 $HOME/.bashrc 中加入 
    
     (gtk2) export GTK_IM_MODULE_FILE=/etc/gtk-2.0/gtk.immodules
     (gtk3) export GTK_IM_MODULE_FILE=/usr/lib/gtk-3.0/3.0.0/immodules.cache
    
应该会解决问题。 

**注意：** 如果你设置为 gtk2，那么你无法使用 gtk3 的应用程序比如gedit, 如果你设置为 gtk3，那么你无法使用 gtk2 的应用程序比如 xfce

###  中文输入

如果你在输入中文时遇到问题，检查你的 locale 设置。比如在香港，export LANG=zh_HK.utf8。 

如需 ibus 随 gnome 启动，把这些加入 `~/.profile` 后重启 gnome。 
    
       export GTK_IM_MODULE=ibus
       export XMODIFIERS=@im=ibus
       export QT_IM_MODULE=ibus
       ibus-daemon -d -x
    
更详细的解决方案可以查看[这里](<https://forum.ubuntu.org.cn/viewtopic.php?f=155&t=346639>)。 

在 gnome桌面 wayland 环境下,可能会出现部分软件无法切换中文输入,例如 QQ 等,需要安装Input Method Panel[[1]](<https://extensions.gnome.org/extension/261/kimpanel>)这个 gnome-shell扩展解决. 

如果安装的输入法无法调整候选词方向等,可以尝试IBus Tweaker[[2]](<https://extensions.gnome.org/extension/2820/ibus-tweaker>)进行调整 

### LibreOffice

如果 IBus 确实已经启动，但是在 LibreOffice 里没有出现输入窗口，你需要在 ~/.bashrc 里加入这行： 
    
    export XMODIFIERS=@im=ibus
    
然后你需要用 "--xim -d" 参数来启动 ibus， 你可以在 ~/.xinitrc 中加入这行： 
    
    ibus-daemon --xim -d
    
但是可怕的是你必须在终端中启动 LibreOffice。 

如果你使用 KDE 而上面的方法没用，而你也不介意在 GTK2 模式下运行 LibreOffice，安装 "libreoffice-gnome" 然后在 ~/.xprofile 中添加此行： 
    
    export OOO_FORCE_DESKTOP="gnome"
    
这会使 IBus 在 LibreOffice 正常使用，你也可以在任何地方启动 LibreOffice -- 而不只是在终端。 

###  修改 Gnome-shell 中 ibus 候选框的字体和字号

####  通过扩展

Gnome 扩展中心提供了一些扩展来修改 ibus 界面，例如 [Customize iBus](<https://extensions.gnome.org/extension/4112/customize-ibus/>)，用户可以在图形界面中修改 ibus 字体、字号等等 

####  通过自定义主题

很多人对 Gnome-shell 不能独立的设置 ibus 输入法的候选词字体和字号颇有微词，下面，介绍一种修改的办法。 首先，你需要安装一个 Gnome-Shell 主题，且激活它，然后你需要修改主题的 gnome-shell.css 文件。这个文件一般在目录 /usr/share/themes/主题名/gnome-shell/ 下。使用你喜欢的编辑器打开它，搜索 .candidate-popup-content 字段（如果没有就新建一个）： 
    
    .candidate-popup-content {
    }
    
然后根据需要添加以下两行（添加后应该是下框中的样子），通过本设置可以改变输入的字母的字体和字号： 
    
    .candidate-popup-content {
           /* 设置字体 */
    	font-family: "Microsoft YaHei UI", serif,cantarell,sans-serif;
           /* 设置号 */
    	font-size: 15px;
    }
    
如果需要修改候选框的字体和字号，你需要搜索 .candidate-box 字段（如果没有就新建一个）： 
    
    .candidate-box {
    }
    
然后根据需要添加以下两行（添加后应该是下框中的样子），通过本设置可以改变输入的字母的字体和字号： 
    
    .candidate-box {
           /* 设置字体 */
    	font-family: "Microsoft YaHei UI", serif,cantarell,sans-serif;
           /* 设置号 */
    	font-size: 15px;
    }
    
###  开启单行模式

[ibus-libpinyin](<https://archlinux.org/packages/?name=ibus-libpinyin>)包 可以在其设置界面中的“外观”-“显示风格”这一项选择“紧凑”，以此来开启单行模式。 

**注：ibus-libpinyin 在输入源和系统托盘中显示为“中文（智能拼音）”。**
