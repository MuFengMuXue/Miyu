**翻译状态：**

  * 本文（或部分内容）译自 [rxvt-unicode](<https://wiki.archlinux.org/title/rxvt-unicode> "arch:rxvt-unicode")，最近一次同步于 2022-07-19，若英文版本有所[更改](<https://wiki.archlinux.org/title/rxvt-unicode?diff=0&oldid=737136>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/rxvt-unicode_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [rxvt-unicode/Tips and tricks](</wzh/index.php?title=Rxvt-unicode/Tips_and_tricks&action=edit&redlink=1> "Rxvt-unicode/Tips and tricks（页面不存在）")

[rxvt-unicode](<http://software.schmorp.de/pkg/rxvt-unicode.html>) 是一个从 [rxvt](<https://en.wikipedia.org/wiki/Rxvt> "wikipedia:Rxvt") 分支出的可定制终端。rxvt-unicode 的特性包括：通过 [Unicode](<https://en.wikipedia.org/wiki/Unicode> "wikipedia:Unicode") 实现的多语言支持、透明度支持、多字体显示和 [Perl](</wzh/index.php?title=Perl&action=edit&redlink=1> "Perl（页面不存在）") 插件支持。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [rxvt-unicode](<https://archlinux.org/packages/?name=rxvt-unicode>)包 包，或 [rxvt-unicode-truecolor](<https://aur.archlinux.org/packages/rxvt-unicode-truecolor/>)AUR 以获得 24 位真彩色支持。 

##  配置

浏览 [urxvt(1)](<https://man.archlinux.org/man/urxvt.1>) 和 [urxvt(7)](<https://man.archlinux.org/man/urxvt.7>) 以获得可用的设置。 

### Xresources

Rxvt-unicode 用命令行参数或者[Xresources](</wzh/index.php?title=Xresources&action=edit&redlink=1> "Xresources（页面不存在）")来控制。命令行参数会覆盖Xresource设置，详情参见[X resources](<../zh-cn/X_resources.html> "X resources")。 

`urxvt --help` 在标准错误输出 输出所有的 _rxvt_ 设置. 帮助页(man page)有每一个设置的完整描述。 

###  回滚位置

当终端内容过多而无法显示时，旧内容会存放到缓冲区。 默认情况下，当shell有新的输出时，会自动跳到最底部。如果你想看以往的输出内容(而不跳到最底部)，设置如下 `~/.Xresources`: 
    
    ! 输出时不滚动
    URxvt*scrollTtyOutput: false
    
    ! scroll in relation to buffer (with mouse scroll or Shift+Page Up)
    URxvt*scrollWithBuffer: true
    
    ! 按键按下时回到最底部
    URxvt*scrollTtyKeypress: true
    
###  回滚 _辅助屏幕_

当你滚动一个有 _辅助屏幕_ 的页面(例如： 不带`**-X**`参数的`less`，禁用滚动条而让这个页面 _自己_ 处理滚动会更好:这在konsole终端和基于vte的终端都是默认且不可更改的。 

在 urxvt 中, 关闭回滚,启用 _第二屏幕_ : 
    
    URxvt.secondaryScreen: 1
    URxvt.secondaryScroll: 0
    
除了使用鼠标滚轮滚动之外，上述配置正常生效。当您使用鼠标滚轮在“辅助屏幕”中滚动页面，同时在回滚缓冲区中有一些内容。这时，回滚缓冲区会滚动，而不是页面。为了解决这个问题，有必要在rxvt-unicode中引入一个新选项[[1]](<https://bbs.archlinux.org/viewtopic.php?id=132150>)。在AUR中有一个修补过的rxvt-unicode，名为 [rxvt-unicode-better-wheel-scrolling](<https://aur.archlinux.org/packages/rxvt-unicode-better-wheel-scrolling/>)AUR。安装后，将以下内容添加到配置文件: 
    
    URxvt.secondaryWheel: 1
    
**注意：** 避免在使用这个参数时使用[urxvt-vtwheel](<https://aur.archlinux.org/packages/urxvt-vtwheel/>)AUR perl插件, 二者冲突。

###  字体设置方法
    
    URxvt.font: 9x15
    
等同于: 
    
    URxvt.font: -misc-fixed-medium-r-normal--15-140-75-75-c-90-iso8859-1
    
设置粗体 
    
    URxvt.font: 9x15bold
    
等同于: 
    
    URxvt.font: -misc-fixed-bold-r-normal--15-140-75-75-c-90-iso8859-1
    
在 `/usr/share/fonts/misc/fonts.alias` 可以找到完整的字体(X core font)简称列表(在`/usr/share/fonts/`的某些子目录下也有其他的fonts.alias文件,但因为他们分别来自其他字体包，所以可能包含你实际上未安装的字体)。值得注意的是，这些别名选择的是ISO-8859-1版本的字体，而不是ISO-10646-1 (Unicode)版本、是75 DPI而不是100 DPI版本，因此您最好避免使用它们，而是使用完整的长名称来选择字体。 

**注意：** 上面的方法只适用于位图字体。其他字体可以用下面的方法通过 [Xft](<https://en.wikipedia.org/wiki/Xft> "w:Xft") 设置:
    
    URxvt.font: xft:monaco:size=10
    
或者 
    
    URxvt.font: xft:monaco:bold:size=10
    
**注意：** 如果Xft字体名称中包含连词符(-), 则必须用反斜杠(\\)转义两次。这与使用 urxvt 的 -fn参数和fc-list返回的结果不同，其中的反斜杠只出现于一次。

在提交配置之前，在实时终端中测试字体的一个好方法是在终端中打印转义代码，例如: 
    
    $ printf '\e]710;%s\007' "xft:Terminus:pixelsize=12"
    
###  字体间距

默认情况下，字符之间的距离可能会感觉太宽。间距可以减少一个像素，如: 
    
    ~/.Xresources
    
    URxvt.letterSpace: -1
    
这是一些关于 _urxvt_ 如何计算字体宽度的讨论 [[2]](<http://lists.schmorp.de/pipermail/rxvt-unicode/2007q4/000511.html>)[[3]](<http://lists.schmorp.de/pipermail/rxvt-unicode/2007q4/000512.html>)。 [rxvt-unicode-patched](<https://aur.archlinux.org/packages/rxvt-unicode-patched/>)AUR 改变了计算方法, 使字体更紧凑 (通常情况下)。 

###  颜色

rxvt-unicode在编译时就加入了颜色支持。除了默认的前景色和背景色外，rxvt最多可以显示256种颜色(加上高辨识度的粗体/闪烁/下划线和任何组合)。 

还可以将前景(foreground)、背景(background)、游标颜色(cursorColor)、cursorColor2、colorBD、colorUL的颜色值指定为数字0-15，作为引用color0-color15的颜色名称的方便快捷方式。详情参见 [#Xresources](<#Xresources>). 

**注意：** 默认情况下 `urxvt` 使用与[Xterm](</wzh/index.php?title=Xterm&action=edit&redlink=1> "Xterm（页面不存在）")相同的颜色,除了一个. 添加 `URxvt.color12: rgb:5c/5c/ff` 到 Xresources 来改变它.

###  打印

默认情况下，当按下`PrintScreen`时，rxvt-unicode将通过lpr打印出一个屏幕转储。使用`Ctrl+PrintScreen`或`Shift-PrintScreen`也会在打印输出中包含终端的回滚。根据个人喜好和需要，可以更改或完全禁用此行为。 
    
    ~/.Xresources
    
    ! 当按下PrintScreen时，禁用打印终端内容。
    URxvt.print-pipe: "cat > /dev/null"
    
##  复制和粘贴

Rxvt-unicode默认使用`PRIMARY`作为剪切缓冲区。详情参见 [Selecting and pasting text](<http://pod.tst.eu/http://cvs.schmorp.de/rxvt-unicode/doc/rxvt.1.pod#THE_SELECTION_SELECTING_AND_PASTING_>)。 

可以通过绑定{{ic|ALT-CTRL-c}和`ALT-CTRL-v`到复制和粘贴来访问`CLIPBOARD`。 

**注意：** 选中文本会自动复制到 `PRIMARY`。 `selection-to-clipboard` 从[rxvt-unicode](<https://archlinux.org/packages/?name=rxvt-unicode>)包 9.20开始的[Perl插件](<#Perl%E6%8F%92%E4%BB%B6>)也会拷贝到 `CLIPBOARD`。

如果你想复制到`PRIMARY`选区，并确保你的` CLIPBOARD`选区更新了相同的内容，你可以添加以下内容: 
    
    URxvt.perl-ext-common:  ...,clipboard,...
    
以及 
    
    URxvt.clipboard.autocopy: true
    URxvt.keysym.M-c: perl:clipboard:copy
    URxvt.keysym.M-v: perl:clipboard:paste
    
参见 [Clipboard#Managers](<../zh-cn/%E5%89%AA%E8%B4%B4%E6%9D%BF.html#Managers> "Clipboard"). 

##  Perl插件

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** 侧重于介绍url-select,因为matcher和url-select基本上是等价的而且手册页存在重复（在[Talk:Rxvt-unicode](<../zh-cn/Talk:Rxvt-unicode.html>)讨论）

我们可以通过包含以下行来启用URxvt perl扩展: 
    
     URxvt.perl-ext-common: extension_name_1,extension_name_2,...
    
请注意：在多个插件名之间**不应该** 有任何的间隔 

### Clickable URLs

您可以使用matcher扩展使终端中的url可单击。例如，要使用鼠标左键在默认的web浏览器中打开链接，请将以下内容添加到`.Xresources`中: 
    
    URxvt.perl-ext-common: default,matcher
    URxvt.url-launcher: /usr/bin/xdg-open
    URxvt.matcher.button: 1
    
rxvt-unicode 9.14 可以使用matcher通过键盘打开和列出最近(目前限制为10个)的url: 
    
    URxvt.keysym.C-Delete: perl:matcher:last
    URxvt.keysym.M-Delete: perl:matcher:list
    
匹配的链接可以指定[前景或背景色](<#%E9%A2%9C%E8%89%B2>)，例如蓝色: 
    
    URxvt.matcher.rend.0: Uline Bold fg5
    
或者使用`colorUL`设置#RRGGBB颜色。然而，这会将颜色应用到所有下划线的文本，而不是只有URL链接: 
    
    URxvt.colorUL: #4682B4
    
###  Yankable URLs (no mouse)

此外，你可以在web浏览器中选择和打开url，而无需使用鼠标。 从 [official repositories](<../zh-cn/Official_repositories.html> "Official repositories") 安装[urxvt-perls](<https://archlinux.org/packages/?name=urxvt-perls>)包 包，修改你的 `.Xresources` 。 下面是一个例子： 
    
    URxvt.perl-ext: default,url-select
    URxvt.keysym.M-u: perl:url-select:select_next
    URxvt.url-select.launcher: /usr/bin/xdg-open
    URxvt.url-select.underline: true
    
**注意：** 这个扩展代替了上面提到的可点击url扩展，因此`matcher`可以从`URxvt中删除。perl-ext`

**key commands:**

Key | 描述   
---|---  
Alt+u | 进入选择模式。您屏幕上的最后一个URL将被选中。您可以重复`Alt+u`来向上选择下一个的URL。   
k | 向上选择下一个URL。   
j | 向下选择下一个的URL   
Return | 在浏览器中打开选定的URL并退出选择模式   
o | 在浏览器中打开选定的URL，不退出选择模式   
y | 复制选定的URL并退出选择模式   
Esc | 退出选择模式   
  
### Simple tabs

要将选项卡(tabs)添加到urxvt，请将以下内容添加到您的`~/.Xresources`: 
    
    URxvt.perl-ext-common: ...,tabbed,...
    
使用如下命令控制选项卡(tabs): 

Key | 描述   
---|---  
Shift+Down | 新建选项卡   
Shift+Left | 转到左边的选项卡   
Shift+Right | 转到右边的选项卡   
Ctrl+Left | 向左移动当前选项卡   
Ctrl+Right | 向右移动当前选项卡   
Ctrl+d | 关闭选项卡   
  
你可以通过如下方式改变标签的颜色: 
    
    URxvt.tabbed.tabbar-fg: 2
    URxvt.tabbed.tabbar-bg: 0
    URxvt.tabbed.tab-fg: 3
    URxvt.tabbed.tab-bg: 0
    
###  全屏

您可以安装[AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR")包[urxvt-fullscreen](<https://aur.archlinux.org/packages/urxvt-fullscreen/>)AUR，然后绑定一个键来启用和关闭urxvt全屏。 
    
    ~/.Xresources
    
    ...
    URxvt.perl-ext-common: ...,fullscreen,...
    URxvt.keysym.F11: perl:fullscreen:switch
    ...
    
###  动态更改字体大小

从[AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR")安装[urxvt-resize-font-git](<https://aur.archlinux.org/packages/urxvt-resize-font-git/>)AUR，将它添加到您的Perl扩展`~/.Xresources`中 
    
     URxvt.perl-ext-common:  ...,resize-font,...
    
默认快捷键是： 

  * `Ctrl++` (or `Ctrl+Shift+=`) 增大字体
  * `Ctrl+-` 减小字体
  * `Ctrl+=` 恢复(reset)字体大小
  * `Ctrl+?` 查看当前字体大小

你也可以改变快捷键, 像这样: 
    
     URxvt.keysym.C-Down:  resize-font:smaller
     URxvt.keysym.C-Up:    resize-font:bigger
    
要使Ctrl+Shift绑定生效，需要禁用默认绑定(参见讨论[[4]](<https://wilmer.gaa.st/blog/archives/36-rxvt-unicode-and-ISO-14755-mode.html>)): 
    
     URxvt.iso14755: false
     URxvt.iso14755_52: false
    
###  禁用Perl插件

如果不使用Perl扩展特性，可以通过完全禁用Perl扩展来提高安全性和速度。 
    
    URxvt.perl-ext:
    URxvt.perl-ext-common:
    
**注意：** 如果您使用多个Perl扩展特性，您可以依次列出它们，用逗号分隔:` urxwt.Perl -ext-common:default,matcher,tabbed`

##  故障排除

###  升级到v9.09后，透明度不生效

rxvt-unicode开发人员删除了很多非标准壁纸设置程序(wallpaper setter)的兼容性代码。使用不兼容的壁纸设置程序会破坏对透明度的支持。建议壁纸设置程序: 

  * [feh](<../zh-cn/Feh.html> "Feh")
  * hsetroot
  * esetroot

要使透明真正的起效，请确保注释掉 URxvt.tintColor 和URxvt.inheritPixmap。 

###  远程主机

如果您正在登录到远程主机，在rxvt-unicode下运行文本模式程序时可能会遇到问题。可以通过在远程主机上安装[rxvt-unicode](<https://archlinux.org/packages/?name=rxvt-unicode>)包或将`/usr/share/terminfo/r/rxvt-unicode`从您的本地机器复制到您的主机`~/.terminfo/r/rxvt-unicode`来解决这个问题;rxvt-unicode-256color 也使用相同的方法。 

有些远程系统不会自动更改标题，除非您指定TERM=xterm。要修复此问题，请在远程机器上的.bashrc中添加以下代码: 
    
    PROMPT_COMMAND='echo -ne "\033]0;${USER}@${HOSTNAME}:${PWD}\007"'
    
###  使用 rxvt-unicode 作为 gmrun 终端

与其他一些终端不同，urxvt希望`-e`的参数是单独给出的，而不是与引号组合在一起。这将导致gmrun出现问题，因为它规定了相反的行为。这可以通过在`.gmrunrc`中gmrun的“Terminal”变量前加上一个“eval”来解决: 
    
    Terminal = eval urxvt
    TermExec = ${Terminal} -e
    
(gmrun使用`/bin/sh`执行命令，因此这里可以理解 _eval_ 。)_eval_ 的副作用是将参数 _分解_ 为`-e`，就像`$@`在[Bash](<../zh-cn/Bash.html> "Bash")中所做的那样，使urxvt能够理解命令。 

###  我的数字键盘行为怪异，产生不同的输出? (e.g. 在vim中)

一些Debian GNU/Linux用户似乎有这个问题，尽管到目前为止还没有具体的细节报告。这可能是由于错误的TERM环境变量设置造成的，尽管关于是否会发生这种情况以及如何发生的细节还不清楚，但TERM=rxvt应该会提供一个兼容的键映射。 

然而，使用 _xmodmap_ 程序([xorg-xmodmap](<https://archlinux.org/packages/?name=xorg-xmodmap>)包)，你可以将你的数字键盘重新映射回来。 

1\. 使用`xev`程序检查数字键盘(numpad)生成的keycode。 

  * 启动`xev` 程序
  * 按下数字键盘的按键 并且 在 `xev`的输出中寻找 _... keycode xxx ..._ 。 例如, numpad 1 在某些键盘中是 "End" 键,所以你得到的keycode是'**keycode 87'**.

2\. 创建或修改你的xmodmap文件，通常是`~/.Xmodmap`，其中的内容表示你的键码。 

带有数字键盘键码的xmodmap文件示例: 
    
    keycode 63 = KP_Multiply
    keycode 79 = Home KP_7
    keycode 80 = Up KP_8
    keycode 81 = Prior KP_9
    keycode 82 = KP_Subtract
    keycode 83 = Left KP_4
    keycode 84 = KP_5
    keycode 85 = Right KP_6
    keycode 86 = KP_Add
    keycode 87 = End KP_1
    keycode 88 = Down KP_2
    keycode 89 = Next KP_3
    keycode 90 = Insert KP_0
    keycode 91 = Delete KP_Decimal
    keycode 112 = Prior
    keycode 117 = Next

3\. 在 X 会话启动时载入你的xmodmap文件。 

例如, 在 `~/.xinitrc`文件中添加: 
    
    ...
    xmodmap ~/.Xmodmap
    ...
    
###  组合键不工作

参见[在终端中启用Alt键](<https://vim.wikia.com/wiki/Get_Alt_key_to_work_in_terminal?useskin=monobook>). 

###  绘制符号时性能低下

有些程序，如alsamixer和xprop，在某些图形驱动程序上表现不佳，因此重绘非常缓慢。选项“skipBuiltinGlyphs”为`~/。Xresources`或命令行选项`-sbg`可以修复此错误。一种可能的解决方案是在`~/.Xresources`中添加以下内容: 
    
    URxvt*skipBuiltinGlyphs:    true
    
###  非常多的行会导致速度减慢

`matcher`插件可能是这里的罪魁祸首。它必须在每次行更新时对行匹配regex，如果您有一个很大的`saveLines`值，那么允许非常大的最多行可能会加剧这个问题。 

这里有一些简单的解决方法: 

  * 减少 `saveLines`
  * 关闭 `matcher` 插件

如果这两个选项都不合适，你可以设置超过某个截止点之后禁用URL匹配: 

  1. 复制 `/usr/lib/urxvt/perl/matcher` 到 `~/.urxvt/ext/` (如果目录不存在则创建)
  2. 修改 `~/.urxvt/ext/matcher`, 找到 `my ($self, $row) = @_;` 行的 `on_line_update` 部分。它应该在270行。
  3. 那行之后, 插入新行： `return () if $row < -100;`. 这将在终端顶部后面超过100行的任何行上禁用URL匹配。

##  参见

  * [rxvt-unicode](<http://software.schmorp.de/pkg/rxvt-unicode.html>) \- 官方网站
  * [Source Code](<http://cvs.schmorp.de/rxvt-unicode/>) \- 可浏览的 CVS
  * [rxvt-unicode FAQ](<http://pod.tst.eu/http://cvs.schmorp.de/rxvt-unicode/doc/rxvt.7.pod>) \- 官方 FAQ
  * [rxvt-unicode Reference](<http://pod.tst.eu/http://cvs.schmorp.de/rxvt-unicode/doc/rxvt.1.pod>) \- 官方手册页
  * [urxvtperl](<http://pod.tst.eu/http://cvs.schmorp.de/rxvt-unicode/src/urxvt.pm>) \- 官方 Perl 扩展参考
