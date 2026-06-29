相关文章

  * [tmux](<../zh-cn/Tmux.html> "Tmux")
  * [Ratpoison](<../zh-cn/Ratpoison.html> "Ratpoison")
  * [Xpra](</wzh/index.php?title=Xpra&action=edit&redlink=1> "Xpra（页面不存在）")

**翻译状态：**

  * 本文（或部分内容）译自 [GNU Screen](<https://wiki.archlinux.org/title/GNU_Screen> "arch:GNU Screen")，最近一次同步于 2024-5-28，若英文版本有所[更改](<https://wiki.archlinux.org/title/GNU_Screen?diff=0&oldid=781279>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/GNU_Screen_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 需要翻译。（在 [Talk:GNU Screen#](<../zh-cn/Talk:GNU_Screen.html>) 中讨论）

[GNU Screen](<https://www.gnu.org/software/screen/>) 是一个全屏窗口管理器，它在多个进程（通常是交互式 shell）之间复用一个物理终端。Screen 中运行的程序在其窗口当前不可见时仍可继续运行，甚至在整个屏幕会话从用户终端分离时也是如此。 

有关功能之描述，参阅官方概述 [GNU Screen 手册](<https://www.gnu.org/software/screen/manual/screen.html#Overview>)。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [screen](<https://archlinux.org/packages/?name=screen>)包 软件包。 

##  用法

输入命令时按下 "转义键 "`Ctrl+a`，然后进行键绑定。 

有些用户认为默认的转义键 `Ctrl+a` 不方便。可以按照 [#更改转义键](<#%E6%9B%B4%E6%94%B9%E8%BD%AC%E4%B9%89%E9%94%AE>)中的说明，将转义键更改为其他键。 

###  常用命令

  * `Ctrl+a` `?` 显示命令及其默认值
  * `Ctrl+a` `:` 进入屏幕命令提示符
  * `Ctrl+a` `"` 窗口列表
  * `Ctrl+a` `0` 打开窗口 0
  * `Ctrl+a` `A` 命名当前窗口
  * `Ctrl+a` `a` 发送到 `Ctrl+a` 当前窗口
  * `Ctrl+a` `c` 创建一个新窗口（带 shell）
  * `Ctrl+a` `S` 将当前区域水平拆分为两个区域
  * `Ctrl+a` `|` 将当前区域垂直拆分为两个区域
  * `Ctrl+a` `tab` 将输入焦点切换到下一个区域
  * `Ctrl+a` `Ctrl+a` 在当前区域和上一个区域之间切换
  * `Ctrl+a` `Esc` 进入复制模式（使用 Enter 选择文本范围）
  * `Ctrl+a` `]` 粘贴文本
  * `Ctrl+a` `Q` 关闭除当前区域之外的所有区域
  * `Ctrl+a` `X` 关闭当前区域
  * `Ctrl+a` `d` 脱离当前 screen 会话，让其继续运行。使用 `screen -r` 恢复

###  命令提示符命令

  * `Ctrl+a` `:quit` 关闭所有窗口并关闭屏幕会话

Closes all windows and closes screen session 

  * `Ctrl+a` `:source ~/.screenrc` 重载 screenrc 配置文件（也可使用 `/etc/screenrc`）

###  命名会话

要创建命名会话，请使用以下命令运行 screen： 
    
    $ screen -S _session_name_
    
要（重新）命名现有会话，请在屏幕运行时运行以下命令： 

`Ctrl+a` `:sessionname _session_name_`

打印标识屏幕会话的 _pid.tty.host_ 字符串列表： 
    
    $ screen -list
    
要附加到已命名的屏幕会话，请运行此命令： 
    
    $ screen -x _session_name_
    
或 
    
    $ screen -r _session_name_
    
###  自定义屏幕

You can modify the default settings for Screen according to your preference either through a personal `.screenrc` file which contains commands to be executed at startup (e.g. `~/.screenrc`) or on the fly in command mode (e.g. `Ctrl+a` `:vbell off`). 

## Tips and tricks

### Autostart with systemd

This service autostarts screen for the specified user (e.g. `systemctl enable screen@florian`). Running this as a system unit is important, because [systemd --user](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "Systemd/User") instance is not guaranteed to be running and will be killed when the last session for given the user is closed. 
    
    /etc/systemd/system/screen@.service
    
    [Unit]
    Description=screen
    After=network.target
    
    [Service]
    Type=simple
    User=%i
    ExecStart=/usr/bin/screen -DmS autoscreen
    ExecStop=/usr/bin/screen -S autoscreen -X quit
    
    [Install]
    WantedBy=multi-user.target
    
### Change the escape key

It can be a good idea to change the default escape key, not only because "a" is usually typed with the left pinky, but also because `Ctrl+a` is mapped to the common command `beginning-of-line` in [GNU Readline](<../zh-cn/Readline.html> "Readline") and [Bash](<../zh-cn/Bash.html> "Bash")-like shells. 

The escape key can be changed with the `escape` option in `~/.screenrc`, or the `-e` option to `screen`. 

For example, if you find that you rarely type `Ctrl+j` in your shell or editor, you could use `escape ^Jj` to set the escape key to `Ctrl+j`. The second "j" means that a literal `Ctrl+j` can be sent to the terminal via the sequence `Ctrl+j` `j`. For [Dvorak](<../zh-cn/Dvorak.html> "Dvorak") keyboard users, `Ctrl+t` (`escape ^Tt`) might be more convenient. 

More exotic options include `escape ``` which sets the escape key to ```, or `escape ^^^` which sets it to `Ctrl+^`. 

The escape key is also called the "command character" in Screen documentation. 

### Start at window 1

By default, the first screen window is 0. If you would rather never have a window 0 and start instead with 1, add the following lines on your configuration: 
    
    ~/.screenrc
    
    bind c screen 1
    bind ^c screen 1
    bind 0 select 10                                                            
    screen 1
    
### Nested Screen Sessions

It is possible to get stuck in a nested screen session. A common scenario: you start an SSH session from within a screen session. Within the SSH session, you start screen. By default, the outer screen session that was launched first responds to `Ctrl+a` commands. To send a command to the inner screen session, use `Ctrl+a` `a`, followed by your command. For example: 

  * `Ctrl+a` `a` `d` Detaches the inner screen session.
  * `Ctrl+a` `a` `K` Kills the inner screen session.

### Start Screen on every shell

For Bash and Zsh, add the following snippet to your `.bashrc` or `.zshrc` before your aliases: 
    
    ~/.bashrc or ~/.zshrc
    
    if [[ -z "$STY" ]]; then
       screen -xRR session_name
    fi
    
### Use 256 colors

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** screen 4.4 sets `$TERM` to `screen.$TERM`, although [the manual](<https://www.gnu.org/software/screen/manual/screen.html#Term>) says something different. There should be no need to modify it in `~/.screenrc`. (在[Talk:GNU Screen](<../zh-cn/Talk:GNU_Screen.html>)讨论)

By default, Screen uses an 8-color terminal emulator. To enable more colors, you need to be using a terminal that supports them and set the correct [term](<http://aperiodic.net/screen/commands:term>) value. This will use [terminfo](<https://en.wikipedia.org/wiki/Terminfo> "wikipedia:Terminfo") to describe how the [ANSI escape codes](<https://en.wikipedia.org/wiki/ANSI_escape_code> "wikipedia:ANSI escape code") will be interpreted. An entry in the terminfo database structure must exist, [ncurses](<https://archlinux.org/packages/?name=ncurses>)包 provides many common descriptions stored under `/usr/share/terminfo/`. 

First try the generic value: 
    
    ~/.screenrc
    
    term screen-256color
    
If that does not work, try setting it based on your terminal. When using [xterm](</wzh/index.php?title=Xterm&action=edit&redlink=1> "Xterm（页面不存在）")-based terminal: 
    
    ~/.screenrc
    
    term xterm-256color
    
When using [rxvt-unicode](<../zh-cn/Rxvt-unicode.html> "Rxvt-unicode"): 
    
    ~/.screenrc
    
    term rxvt-unicode-256color
    
**注意：**`/usr/share/terminfo/r/rxvt-unicode-256color` is provided by [rxvt-unicode-terminfo](<https://archlinux.org/packages/?name=rxvt-unicode-terminfo>)包, which is installed as a dependency of [rxvt-unicode](<https://archlinux.org/packages/?name=rxvt-unicode>)包. However, if you log into a server via [SSH](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH") and run _screen_ there, this terminfo file might not be available on the server. In this case it is recommended to copy `/usr/share/terminfo/r/rxvt-unicode-256color` on the server, it can be saved in `~/.terminfo/`.

As a last resort, try setting [termcapinfo](<http://aperiodic.net/screen/commands:termcapinfo>) instead: 
    
    ~/.screenrc
    
    attrcolor b ".I"    # allow bold colors - necessary for some reason
    termcapinfo xterm 'Co#256:AB=\E[48;5;%dm:AF=\E[38;5;%dm'   # tell screen how to set colors. AB = background, AF=foreground
    defbce on    # use current bg color for erased chars
    
### Informative statusbar

The default statusbar may be a little lacking. You may find this one more helpful: 
    
    ~/.screenrc
    
    hardstatus off
    hardstatus alwayslastline
    hardstatus string '%{= kG}[ %{G}%H %{g}][%= %{= kw}%?%-Lw%?%{r}(%{W}%n*%f%t%?(%u)%?%{r})%{w}%?%+Lw%?%?%= %{g}][%{B} %m-%d %{W} %c %{g}]'
    
Another possibility, taken from [frodfrog's blog](<https://www.fordfrog.com/2012/09/02/71/>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2023-04-23 ⓘ] is: 
    
    ~/.screenrc
    
    hardstatus alwayslastline '%{= G}[ %{G}%H %{g}][%= %{= w}%?%-Lw%?%{= R}%n*%f %t%?%{= R}(%u)%?%{= w}%+Lw%?%= %{= g}][ %{y}Load: %l %{g}][%{B}%Y-%m-%d %{W}%c:%s %{g}]'
    
As of Screen v5 ([master branch](<https://git.savannah.gnu.org/cgit/screen.git>) currently) the escape codes have changed, you could use this instead: 
    
    ~/.screenrc
    
    truecolors on
    hardstatus off
    backtick 0 5 5 "/bin/date" '+%Y-%m-%d'
    backtick 1 5 5 "/bin/date" '+%H:%M'
    hardstatus alwayslastline '%{#00ff00}[ %H ][%{#ffffff}%= %{7}%?%-Lw%?%{1;0}%{1}(%{15}%n%f%t%?(%u)%?%{1;0}%{1})%{7}%?%+Lw%?%? %=%{#00ff00}][ %{#00a5ff}%{6}%0` %{#ffffff}%{7}%1`%{#00ff00} ]'
    
statusbar at top: 
    
    ~/.screenrc
    
    hardstatus firstline 
    
### Turn welcome message off
    
    ~/.screenrc
    
    startup_message off
    
###  Turn your hardstatus line into a dynamic urxvt|xterm|aterm window title

This one is pretty simple; just switch your current `hardstatus` line into a `caption` line with notification, and edit accordingly: 
    
    ~/.screenrc
    
    backtick 1 5 5 true
    termcapinfo rxvt* 'hs:ts=\E]2;:fs=\007:ds=\E]2;\007'
    hardstatus string "screen (%n: %t)"
    caption string "%{= kw}%Y-%m-%d;%c %{= kw}%-Lw%{= kG}%{+b}[%n %t]%{-b}%{= kw}%+Lw%1`"
    caption always
    
This will give you something like `screen (0 bash)` in the title of your terminal emulator. The caption supplies the date, current time, and colorizes your screen window collection. 

### Use X scrolling mechanism

The scroll buffer of GNU Screen can be accessed with `Ctrl+a` `[`. However, this is very inconvenient. To use the scroll bar of e.g. xterm or Konsole, add the following line [[1]](<https://unix.stackexchange.com/a/505703>): 
    
    ~/.screenrc
    
    termcapinfo xterm*|rxvt*|kterm*|Eterm* ti@:te@
    
### Attach an existing running program to screen

If you started a program outside Screen, but now you would like it to be inside, you can use **reptyr** to reparent the process from its current TTY to one inside screen. 

[Install](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") the [reptyr](<https://archlinux.org/packages/?name=reptyr>)包 package. 

Get the PID of the process (you can use `ps ax` for that). Now just enter the PID as argument to reptyr inside a screen window. 
    
    $ reptyr _pid_
    
### Setting a different bash prompt while in screen

If you want a different bash prompt when in a screen session, add the following to your `.bashrc`[[2]](<https://serverfault.com/questions/257975/how-to-check-if-im-in-screen-session>): 
    
    if [ -z $STY ]
    then
            PS1="YOUR REGULAR PROMPT"
    else  
            PS1="YOUR SCREEN PROMPT"
    fi
    
### Turn off visual bell

With this setting, Screen will not make an ugly screen flash instead of a bell sound. 
    
    ~/.screenrc
    
    vbell off
    
### Getting rid of the vertical and horizontal bars

To get rid of the vertical bars: 
    
    $ ~/.screenrc
    
    rendition so =00

To hide the horizontal bar, set the back and foreground color to default (d) and display a blank (" "): 
    
    ~/.screenrc
    
    caption string "%{03} "
    
If this does not work, try `caption string "%{00} "` instead. For the default caption in black and white, use `caption string "%{00}%3n %t"`. 

##  问题解决

###  修复编辑器文本残留问题

在屏幕中打开文本编辑器（如 [nano](<../zh-cn/Nano.html> "Nano")），然后关闭它时，文本可能会在终端中保持可见。要解决这个问题，请执行以下操作： 
    
    ~/.screenrc
    
    altscreen on
    
###  修复窗口列表中名称列仅显示 "bash "的问题

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 应解释一下此命令的作用。 (在 [Talk:GNU Screen](<../zh-cn/Talk:GNU_Screen.html>) 中讨论)

向 `~/.screenrc` 添加以下内容： 
    
    ~/.screenrc
    
    windowlist string "%4n %h%=%f"

##  参见

  * [Wikipedia:GNU Screen](<https://en.wikipedia.org/wiki/GNU_Screen> "wikipedia:GNU Screen")
  * [GNU Screen 用户手册](<https://www.gnu.org/software/screen/manual/screen.html>)
  * [Gentoo:Screen](<https://wiki.gentoo.org/wiki/Screen> "gentoo:Screen")
  * [Arch Forums - 带屏幕截图的 .screenrc 配置](<https://bbs.archlinux.org/viewtopic.php?id=55618>)
  * [Arch Forums - 关于 urxvt 的 256 色问题](<https://bbs.archlinux.org/viewtopic.php?id=50647>)
  * [MacOSX Hints - Automatically using screen in your shell](<https://hints.macworld.com/article.php?story=20021114055617124>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2023-06-17 ⓘ]
