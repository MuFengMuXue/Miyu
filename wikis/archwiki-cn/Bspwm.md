**翻译状态：**

  * 本文（或部分内容）译自 [Bspwm](<https://wiki.archlinux.org/title/Bspwm> "arch:Bspwm")，最近一次同步于 2021-02-12，若英文版本有所[更改](<https://wiki.archlinux.org/title/Bspwm?diff=0&oldid=652021>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Bspwm_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")
  * [平铺式窗口管理器比较](<../zh-cn/%E5%B9%B3%E9%93%BA%E5%BC%8F%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8%E6%AF%94%E8%BE%83.html> "平铺式窗口管理器比较")

[bspwm](<https://github.com/baskerville/bspwm>) 是一个平铺窗口管理器，每一个窗口被表达为满二叉树的叶子。bspwm支持多显示器，可通过messages进行配置和控制。bspwm部分支持[EWMH](<https://specifications.freedesktop.org/wm-spec/wm-spec-latest.html>)。 

##  安装

安装 [bspwm](<https://archlinux.org/packages/?name=bspwm>)包 或 [bspwm-git](<https://aur.archlinux.org/packages/bspwm-git/>)AUR (开发版本）。 

##  启动

使用 [xinit](<../zh-cn/Xinit.html> "Xinit") 来启动 `bspwm`。 

##  配置

示例配置文件位于 `/usr/share/doc/bspwm/examples/`。 

复制或安装 `bspwmrc` 和 `sxhkdrc` 分别到 `~/.config/bspwm/` 和 `~/.config/sxhkd/`。 

文件 `bspwmrc` 必须是可执行的，因为默认示例是一个shell脚本,此脚本随后通过 `bspc` 命令配置bspwm。 
    
    $ install -Dm755 /usr/share/doc/bspwm/examples/bspwmrc ~/.config/bspwm/bspwmrc
    $ install -Dm644 /usr/share/doc/bspwm/examples/sxhkdrc ~/.config/sxhkd/sxhkdrc
    
这两个文件会分别被用来设置窗口管理器和按键绑定。 

查看 [bspwm(1)](<https://man.archlinux.org/man/bspwm.1>) 和 [sxhkd(1)](<https://man.archlinux.org/man/sxhkd.1>) 手册获取详细信息。 

###  设置多显示器

以下示例配置将会配置10个桌面在单独的显示器上： 
    
    bspc monitor -d I II III IV V VI VII VIII IX X
    
如果使用多显示器，则需要为每一个显示器配置： 
    
    bspc monitor DVI-I-1 -d I II III IV
    bspc monitor DVI-I-2 -d V VI VII
    bspc monitor DP-1 -d VIII IX X
    
使用 `xrandr -q` 或 `bspc query -M --names` 命令来查看显示器编号。 

在上面的示例中，桌面的总数保持在10个，在 sxhkdrc 中，这样每一个桌面仍然可以使用 `super + {1-9,0}` 来定位。 

###  规则（rules）

有两种方法来设置窗口规则 (截至 [cd97a32](<https://github.com/baskerville/bspwm/commit/cd97a3290aa8d36346deb706fa307f5f8faa2f34>)) 

第一种是通过使用内置的 rule 命令，如示例 bspwmrc 所示： 
    
    bspc rule -a Gimp desktop=^8 follow=on state=floating
    bspc rule -a Chromium desktop=^2
    bspc rule -a mplayer2 state=floating
    bspc rule -a Kupfer.py focus=on
    bspc rule -a Screenkey manage=off
    
第二种是使用外部的 rule 命令。虽然更加复杂，但是这允许你去构造更复杂的桌面规则。参考 [these examples](<https://github.com/baskerville/bspwm/tree/master/examples/external_rules>) 获取示例 rule 命令。 

如果某个特定的窗口似乎没有按照你的规则运行，请检查程序的类名。可以通过运行 `xprop | grep WM_CLASS` 来确保你在使用正确的字符串，这需要 [xorg-xprop](<https://archlinux.org/packages/?name=xorg-xprop>)包 软件包。 

###  面板（Panels）

####  使用lemonbar

在lemonbar的Github页面提供了一个 [lemonbar-git](<https://aur.archlinux.org/packages/lemonbar-git/>)AUR 的示例面板。你也可从 [lemonbar](</wzh/index.php?title=Lemonbar&action=edit&redlink=1> "Lemonbar（页面不存在）") 的维基页面得到了些许启发。面板将通过 bspwmrc 中的 `panel &` 启动。检查在 [bspwm](<https://archlinux.org/packages/?name=bspwm>)包 软件包中的 [optdepends](</wzh/index.php?title=Optdepends&action=edit&redlink=1> "Optdepends（页面不存在）")，以获取可能需要的依赖。 

为了在你的状态栏（status bar）中显示系统信息，你可以使用各种系统调用（system calls）。示例将会展示给你如何编辑你的 `panel` 来使音量状态显示在你的状态栏中： 
    
    panel_volume()
    {
            volStatus=$(amixer get Master | tail -n 1 | cut -d '[' -f 4 | sed 's/].*//g')
            volLevel=$(amixer get Master | tail -n 1 | cut -d '[' -f 2 | sed 's/%.*//g')
            # is alsa muted or not muted?
            if [ "$volStatus" == "on" ]
            then
                    echo "%{Fyellowgreen} $volLevel %{F-}"
            else
                    # If it is muted, make the font red
                    echo "%{Findianred} $volLevel %{F-}"
            fi
    }

之后，我们必须确保它已被调用并且重定向至 `$PANEL_FIFO` ： 
    
    while true; do
    echo "S" "$(panel_volume) $(panel_clock)" > "$PANEL_FIFO"
            sleep 1s
    done &
    
####  使用yabar

使用lemonbar示例面板需要你配置你的环境（.profile），并确保面板脚本在你的路径上。[yabar](<https://aur.archlinux.org/packages/yabar/>)AUR 是更易配置的面板，只有一个配置文件。 

####  使用polybar

通过在你的配置文件中添加 `polybar _example_ &` 来使用 [Polybar](<../zh-cn/Polybar.html> "Polybar")，其中的 `_example_` 就是状态栏的名称。 

###  暂存器/便笺（Scratchpad）

####  使用pid

你可以使用 bspwm 的窗口标签来模仿下拉式终端（例如 i3wm 的便笺功能）。将下面的内容附加到 bspwm 的配置文件末尾（适用于你自己的终端）： 
    
    bspc rule -a scratchpad sticky=on state=floating hidden=on
    # check scratchpad already running
    [ "$(ps -x | grep -c 'scratchpad')" -eq "1" ] && st -c scratchpad -e ~/bin/scratch &
    
`sticky` 标签可确保窗口总是出现在当前的桌面上。 `~/bin/scratch` 是： 
    
    #!/usr/bin/sh
    # only add floating scratchpad window node id to /tmp/scratchid
    bspc query -N -n .floating | xargs -i sh -c 'bspc query  --node {} -T | grep -q scratchpad && echo {} > /tmp/scratchid'
    exec $SHELL
    
切换 Scratchpad 的热键应该绑定到： 
    
    id=$(cat /tmp/scratchid);\
    bspc node $id --flag hidden;bspc node -f $id
    
####  使用类名（class name）

在此示例中我们将使用带有自定义类名的 _termite_ 作为我们的下拉式终端。当然其类名没有必要必须是 _termite_ 。 

首先在你的路径中创建一个有如下内容的文件并确保其可执行。在此示例中我们命其名为 `scratchpad.sh` ： 
    
    #!/usr/bin/bash
    
    if [ -z $1 ]; then
    	echo "Usage: $0 <name of hidden scratchpad window>"
    	exit 1
    fi
        
    pids=$(xdotool search --class ${1})
    for pid in $pids; do
    	echo "Toggle $pid"
    	bspc node $pid --flag hidden -f
    done
    
随后添加这个到你的 bspwm 配置中。 
    
    ...
    bspc rule -a dropdown sticky=on state=floating hidden=on
    termite --class dropdown -e "zsh -i" &
    ...
    
为了切换窗口，一个在 [sxhkd](<../zh-cn/Sxhkd.html> "Sxhkd") 中的自定义规则是必不可少的。给定自定义类名作为参数。 
    
    super + u
            scratchpad.sh dropdown
    
####  其他

对于无需预定义规则就可使用任何窗口类型的Scratchpad，参阅：[[1]](<https://www.reddit.com/r/bspwm/comments/3xnwdf/i3_like_scratch_for_any_window_possible/cy6i585>)

有关支持更多开箱即用的终端，并具有用于执行诸如选择性启动tmuxinator / tmux会话，即时将任何窗口变成便笺本以及自动调整便笺本大小以适合当前显示器的标志的更复杂的便笺本脚本，参阅 [tdrop-git](<https://aur.archlinux.org/packages/tdrop-git/>)AUR 。 

###  不同设备的显示器配置

因为 `bspwmrc` 是一个shell脚本，这允许你做类似如下的操作： 
    
    #! /bin/sh
    
     if [[ $(hostname) == 'myhost' ]]; then
         bspc monitor eDP1 -d I II III IV V VI VII VIII IX X
     elif [[ $(hostname) == 'otherhost' ]]; then
         bspc monitor VGA-0 -d I II III IV V
         bspc monitor VGA-1 -d VI VII VIII IX X
     elif [[ $(hostname) == 'yetanotherhost' ]]; then
         bspc monitor DVI-I-3 -d VI VII VIII IX X
         bspc monitor DVI-I-2 -d I II III IV V
     fi
     
**注意：** 使用hostname命令需要 [inetutils](<https://archlinux.org/packages/?name=inetutils>)包 软件包。

###  设置某一桌面的所有窗口均为浮动模式

下面的示例会将 3 号桌面的所有窗口均设置为浮动窗口。当使用 GIMP 或其他多窗口的应用程序时非常有用。 

把这个脚本放到你的 `$PATH` 的某个位置并从 `.xinitrc` 或类似的（最后带有 `&`）调用： 
    
    #!/bin/bash
    
     # change the desktop number here
     FLOATING_DESKTOP_ID=$(bspc query -D -d '^3')
    
     bspc subscribe node_add | while read -a msg ; do
        desk_id=${msg[2]}
        wid=${msg[4]}
        [ "$FLOATING_DESKTOP_ID" = "$desk_id" ] && bspc node "$wid" -t floating
     done
     
([源](<https://github.com/baskerville/bspwm/issues/428#issuecomment-199985423>)) 

###  键盘

bspwm 不会处理任何键盘输入而是提供 _bspc_ 程序作为接口。 

你必须为快捷键设置一个守护程序例如 [sxhkd](<https://archlinux.org/packages/?name=sxhkd>)包 （开发版本：[sxhkd-git](<https://aur.archlinux.org/packages/sxhkd-git/>)AUR） 

##  故障排除

###  屏幕空白，按键绑定不可用

  * 确保 [sxhkd](<https://archlinux.org/packages/?name=sxhkd>)包 已被安装。
  * 确保 sxhkd 正在运行。
  * 确保 `~/.config/bspwm/bspwmrc` 为可执行文件。

###  鼠标指针主题没有应用到桌面

参阅 [Cursor themes#Change X shaped default cursor](<../zh-cn/Cursor_themes.html#Change_X_shaped_default_cursor> "Cursor themes")

###  窗口大于实际运行的应用程序

若你正在使用GTK3应用程序并且经常用于对话窗口，那么这种情况就会发生。修复方法是创建或添加以下内容到GTK3主题文件（`~/.config/gtk-3.0/gtk.css`）。 
    
    .window-frame, .window-frame:backdrop {
      box-shadow: 0 0 0 black;
      border-style: none;
      margin: 0;
      border-radius: 0;
    }
        
    .titlebar {
      border-radius: 0;
    }
    
(源: [Bspwm forum thread](<https://bbs.archlinux.org/viewtopic.php?pid=1404973#p1404973>)) 

###  Java程序的问题

如果你有例如Java程序窗口无法调整大小，或菜单在点击后立即关闭的问题，参阅[Java#Gray window, applications not resizing with WM, menus immediately closing](<../zh-cn/Java.html#Gray_window,_applications_not_resizing_with_WM,_menus_immediately_closing> "Java")。 

此外，一些基于Java的应用程序显示不出任何窗口内容（例如 Intellij的IDE)。一个解决办法是安装 [wmname](<https://archlinux.org/packages/?name=wmname>)包 软件包并且添加以下内容到你的 `~/.config/bspwm/bspwmrc` ： 
    
    wmname LG3D
    
###  fish shell的按键绑定问题

如果你正在使用 [fish](<../zh-cn/Fish.html> "Fish") ，你会发现你不能切换桌面。这是因为 bspc 的 ^ 字符与 fish 不兼容。你可通过明确告诉 sxhkd 使用 bash 执行命令来解决问题。 
    
    $ set -U SXHKD_SHELL /usr/bin/bash
    
或者，将 ^ 字符在你的 sxhkdrc 中用反斜线(\\)转义。 

###  使用fish shell的性能问题

[sxhkd](<../zh-cn/Sxhkd.html> "Sxhkd") 使用 SHELL 环境变量中的 shell 来执行命令。由于配置文件很大或配置不当，[fish](<../zh-cn/Fish.html> "Fish") 的加载时间可能很长，因此所有 sxhkd 命令的执行时间可能比其他的shell都长。为了在不改变你的默认 shell 情况下修复这个问题，你可以明确地告诉 sxhkd 使用 bash 或其他更快的 shell 来执行命令 （比如sh）： 
    
    $ set -U SXHKD_SHELL sh
    
###  启动时报 "Could not grab key 43 with modfield 68" 错误

要么你尝试绑定同一个键两次，要么你启动了两次 sxhkd ，检查 bspwmrc 和 `~/.profile` 或 `~/.bash_profile`，查看是否在启动 sxhkd 时有多余的命令。 

###  火狐浏览器（Firefox）菜单在右键单击时自动选择第一选项

添加以下内容到 `userChrome.css` Firefox配置文件： 
    
    #contentAreaContextMenu{ margin: 5px 0 0 5px }
    
文件应位于 `~/.mozilla/firefox/_something_.default/chrome/` （如果没有，就创建一个）。在Firefox中，你必须到 `about:config` 页面开启 `toolkit.legacyUserProfileCustomizations.stylesheets` 选项；否则，Firefox会忽略 userChrome.css 文件。 

##  参照

  * Mailing List: bspwm _at_ librelist.com.
  * `#bspwm` \- IRC channel at irc.libera.chat
  * <https://bbs.archlinux.org/viewtopic.php?id=149444> \- Arch BBS thread
  * <https://github.com/baskerville/bspwm> \- GitHub project
  * <https://github.com/windelicato/dotfiles/wiki/bspwm-for-dummies> \- earsplit's "bspwm for dummies"
