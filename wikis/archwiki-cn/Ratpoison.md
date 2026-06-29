[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:Ratpoison](<../zh-cn/Talk:Ratpoison.html>)讨论)

**翻译状态：**

  * 本文（或部分内容）译自 [Ratpoison](<https://wiki.archlinux.org/title/Ratpoison> "arch:Ratpoison")，最近一次同步于 2016-02-01，若英文版本有所[更改](<https://wiki.archlinux.org/title/Ratpoison?diff=0&oldid=418627>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Ratpoison_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-preferences-desktop-locale-modified.png)](<../File:Tango-preferences-desktop-locale-modified.png>)**这篇文章或章节的[翻译](<../Project:%E8%B4%A1%E7%8C%AE.html#Translating> "Project:Contributing")质量不佳。**

**原因：** Last updated in 2016（在 [Talk:Ratpoison#](<../zh-cn/Talk:Ratpoison.html>) 中讨论）

[Ratpoison](<https://www.nongnu.org/ratpoison/>)是一个用C语言编写的平铺式窗口管理器，它允许用户不用鼠标就能管理应用程序。它的界面收到[GNU Screen](<../zh-cn/GNU_Screen.html> "GNU Screen")的启发。 

##  安装

Ratpoison可以通过[ratpoison](<https://archlinux.org/packages/?name=ratpoison>)包 或者是[ratpoison-git](<https://aur.archlinux.org/packages/ratpoison-git/>)AUR[[损坏的链接](<../zh-cn/Help:%E6%93%8D%E4%BD%9C%E6%B5%81%E7%A8%8B.html#%E4%BF%AE%E5%A4%8D%E6%8D%9F%E5%9D%8F%E7%9A%84%E5%8C%85%E9%93%BE%E6%8E%A5> "Help:操作流程")：package not found] （开发版本）安装。 

##  配置

为了让Ratpoison成为你的窗口管理器，你必须新建/编辑文件`~/.xinitrc`. 

.xinitrc的一个例子: 
    
    # The black/white grid as background doesn't suit my taste.
    xsetroot -solid black &
    # Ratpoison is compatible with xcompmgr! now you can have real transparency
    xcompmgr -c -f -D 5 &
    #fire up ratpoison!
    exec /usr/bin/ratpoison
    
##  使用Ratpoison

在X11启动后你会看到黑色的屏幕背景还有右上角它弹出的一个文本框"Welcome to Ratpoison"。现在按下`Ctrl+t`，再输入`?`来获取快捷键列表。如果你习惯使用GNU screen，你将马上感到它非常熟悉。 你可以自定义快捷键，你甚至可以覆盖`~/.ratpoisonrc`中已存在的快捷键 

例如: 
    
    # Overriding CTRL+t 'c' to start aterm instead of xterm
    bind c exec aterm
    
    bind f exec firefox
    
如果使用上述配置，当你按下`Ctrl+t` 然后`f`后, ratpoison将启动firefox. 

这是另一个我正在用的.ratpoisonrc配置: 
    
    exec xsetroot -cursor_name left_ptr
    startup_message off
    
    escape C-z
    
    # Make a screenshot
    alias sshot exec import -window root ~/screenshot-$(date +%F).jpg
    definekey top M-C-Print sshot
    
    #virtual desks
    gnewbg one
    gnewbg two
    
    definekey top M-l exec ratpoison -c "select -" -c "gprev" -c "next"
    definekey top M-h exec ratpoison -c "select -" -c "gnext" -c "next"
    
    #switch between windows
    definekey top M-j next
    definekey top M-k prev
    
    #apps
    unbind c
    bind c exec urxvt -tr
    #bind c exec aterm
    
    bind g exec gftp
    bind f exec firefox
    
##  小贴士

###  Java Swing应用程序

Java Swing GUI应用程序不认为ratpoison是平铺式窗口管理器, 且不正确地像ratpoison配置的那样全屏显示。不过有一种方法可以让它认为自己在平铺式管理器中并且正确的全屏。 

首先安装`wmname` package， 然后将这一行加入你的`.ratpoisonrc`中: 
    
    ~/.ratpoisonrc
    
    exec wmname LG3D
    
啊哈！Java Swing应用现在可以正确全屏了。 

###  多个虚拟桌面

默认情况下，ratpoison只有一个虚拟桌面，但是用一个叫做rpws(默认安装）的脚本，你可以有多个虚拟桌面。 

只要更改你的.ratpoisonrc，然后加入: 
    
    ~/.ratpoisonrc
    
    exec /usr/bin/rpws init 6 -k
    
这样就会创建6个虚拟桌面。默认地，你可以进入通过按下`Alt+F1` 来进入1号虚拟桌面, `Alt+F2` 来进入2号虚拟桌面，以此类推。 

你也可以这样添加快捷键: 
    
    bind C-1 exec rpws 1
    bind C-2 exec rpws 2
    ...
    
这样允许你通过`Ctrl+t` `Ctrl+1` 进入它们(假定`Ctrl+t` 是你的escape键) 

###  Urxvt和xterm

Urxvt和xter，因为它们被默认安装，发送重调大小的信号给窗口管理器。这个在大多数窗口管理器中起作用，但是在ratpoison中无效。结果就是URxvt/xterm通过更改字号调整自己的大小，而不是将自己调整成全屏，有无法填充空格的几率很高。有两种方法改变这个现状。请看下文。 

####  安装打过补丁的URxvt

如果你使用URxvt,软件包[rxvt-unicode-fontspacing-noinc-vteclear-secondarywheel](<https://aur.archlinux.org/packages/rxvt-unicode-fontspacing-noinc-vteclear-secondarywheel/>)AUR除其他改动外，还不发送重调大小的信号给窗口管理器。如果你安装这个版本的URxvt而不是默认版本，URxvt就会在ratpoison中正常调整大小。 

####  配置边缘

我们可以使用xterm/URxvt默认的边框设置工具将ratpoison的边框设置为0。 
    
    ~/.Xresources
    
    urxvt*internalBorder: 8 #change urxvt to xterm if necessary. Using the font terminus in urxvt at 14px size, 8 is the correct number here.
    
    ~/.ratpoisonrc
    
    set border 0
    
###  自启动

当ratpoison启动时自启动应用的例子。文件 `~/.ratpoisonrc`中的内容会在ratpoison启动时执行。 
    
    Launch urxvt with a tmux session
    
    exec urxvt -e bash -c "tmux -q has-session && exec tmux attach-session -d || exec tmux new-session -n$USER -s$USER@$HOSTNAME"
    
    Launch optimized chromium
    
    exec bash -c 'pidof chromium &>/dev/null || exec /usr/bin/chromium --disk-cache-dir=~/tmp/cache'
    
###  壁纸和透明度

通过[xcompmgr](<../zh-cn/Xcompmgr.html> "Xcompmgr")还有nitrogen设置透明的例子. 首先启动nitrogen然后设置你希望设置成壁纸的壁纸。然后把这个加入到你的.ratpoisonrc中去 
    
    Wallpaper and transparency
    
    exec xcompmgr -c -f -D 5 &
    exec nitrogen --restore
    
##  有用的快捷键

`Ctrl+t` `!` <_程序名称_ > 启动某个程序   
---  
`Ctrl+t` `?` 显示快捷键设置   
`Ctrl+t` `c` 启动一个x terminal   
`Ctrl+t` `n` 切换到下一个窗口   
`Ctrl+t` `p` 切换到之前的窗口   
`Ctrl+t` `1`-`9` 切换到1-9号窗口   
`Ctrl+t` `k` 关闭当前窗口   
`Ctrl+t` `Shift+k` 杀死当前窗口   
`Ctrl+t` `s`,`Shift+s` 将当前布局改为竖直布局或水平布局   
`Ctrl+t` `Tab`, `←`, `↑`, `→`, `↓` 切换到下一个，左边的，顶部的，右边的，顶部的框架.   
`Ctrl+t` `Shift+q` 将当前框架指定为唯一   
`Ctrl+t` `:` 执行一个ratpoison命令   
  
##  焦点跟随鼠标

Arch linux的ratpoison包同时在/usr/share/ratpoison中安装了编译脚本，sloppy.c。它能被用来在ratpoison中启动焦点跟随鼠标。为了启动它，你可以: 
    
    # cd /usr/share/ratpoison/
    # gcc -o sloppy sloppy.c -lX11
    # ./sloppy
    
想要自启动，你可以将下列行加入~/.ratpoisonrc 
    
    exec /usr/share/ratpoison/sloppy
    
##  Ratpoison和显示管理器

许多[display managers](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器") (例如 [LightDM](<../zh-cn/LightDM.html> "LightDM")) 在 `/usr/share/xsessions/`中确认可用的会话，并且大多数窗口管理器和桌面环境会在那建立一个.desktop文件。然而ratpoison却会在`/etc/X11/sessions/`里创建。 为了让显示管理器识别ratpoison，你需要将`/etc/X11/sessions/ratpoison.desktop` 拷贝至`/usr/share/xsessions/ratpoison.desktop`. 如果 `/usr/share/xsessions`不存在，你需要在root下建立 

##  更多链接

  * [The Ratpoison wiki](<http://ratpoison.wxcvbn.org/>)
  * [X11 Keys in Ratpoison](<http://stumpwm.svkt.org/cgi-bin/ratpoison.pl?action=browse;id=keys>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2020-08-04 ⓘ]
  * [Ratpoison config sample](<http://www.ormiret.com/?q=node/11>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2021-11-15 ⓘ]
  * [Share your Ratpoison (experience) forum thread](<https://bbs.archlinux.org/viewtopic.php?id=68622>)
  * [Collection of scripts for the Ratpoison window manager](<https://github.com/jbaber/ratpoison_scripts>)
  * [Stumpwm - a successor to Ratpoison written in Common lisp](<https://www.nongnu.org/stumpwm/>)
