**翻译状态：**

  * 本文（或部分内容）译自 [Tmux](<https://wiki.archlinux.org/title/Tmux> "arch:Tmux")，最近一次同步于 2025-03-12，若英文版本有所[更改](<https://wiki.archlinux.org/title/Tmux?diff=0&oldid=823315>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Tmux_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[tmux](<https://tmux.github.io/>) 是终端多路复用器，可在一个屏幕中创建、访问并控制多个终端（或窗口），每个终端或窗口内都可以运行独立的程序。将 tmux 从当前窗口分离（tmux detach）后，tmux 依然可以在后台运行，直到恢复会话（tmux attach）。 使用 ISC 协议的 tmux 是 [GNU Screen](<../zh-cn/GNU_Screen.html> "GNU Screen") 的替代品。尽管两者相似，但依然有许多不同之处（参考 [tmux FAQ page](<https://github.com/tmux/tmux/wiki/FAQ>)）。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [tmux](<https://archlinux.org/packages/?name=tmux>)包 软件包。 可选择安装 [tmux-bash-completion-git](<https://aur.archlinux.org/packages/tmux-bash-completion-git/>)AUR 软件包用于提供 bash 补全功能。 

##  配置

自 [3.2](<https://github.com/tmux/tmux/blob/a5f99e14c6f264e568b860692b89d11f5298a3f2/CHANGES#L145>) 版本起，tmux 默认从 `$XDG_CONFIG_HOME/tmux/tmux.conf`，然后是 `~/.config/tmux/tmux.conf` 寻找用户配置文件。全局配置文件位于 `/etc/tmux.conf`，但 Archlinux 并无此文件。 

###  快捷键绑定

命令快捷键的前缀默认是 `Ctrl+b`。 

**提示：** 可以使用默认的帮助快捷键 `Ctrl+b ?` 查询所有可用的快捷键绑定。

要垂直分割一个窗口，请按下 `Ctrl+b %`。 

将窗口分割成多个面板（panes）后，通过按下命令前缀（例如 `Ctrl+b`），然后按住 `Ctrl` 不放的同时，按下方向键 `Left`、`Right`、`Up` 或 `Down` 调整面板大小。交换不同的面板与此类似，只需将调整大小环节中所按的方向键改为 `o` 键即可。 

按键绑定可以在 `tmux.conf` 配置文件中通过 bind 与 unbind 命令修改。例如，将下面的示例配置添加到用户配置文件中可将默认的前缀绑定 `Ctrl+b` 更改为 `Ctrl+a`： 
    
    unbind C-b
    set -g prefix C-a
    bind C-a send-prefix
    
**提示：** 使用特殊字符作为前缀时，请用 `Alt`（也被称为 Meta）替换 `Ctrl`，例如：`set -g prefix m-'\'`。

使用 `Ctrl+b c` 创建一个新的窗口（window），通过快捷键 `Ctrl+b n` 与 `Ctrl+b p` 切换到下一个或上一个窗口。 

下面还有一些用于在窗口间移动的其他方法： 
    
    Ctrl+b l（移动到上一个使用的窗口）
    Ctrl+b w（列出所有窗口与窗口编号）
    Ctrl+b <窗口编号>（移动到指定编号的窗口，默认编号是 0 到 9）
    Ctrl+b q（显示面板编号，在面板编号显示的同时按下对应编号可以切换到该面板）
    
tmux 有窗口搜索选项与快捷键绑定，便于在多个窗口之间切换： 
    
    Ctrl+b f <窗口名称>（按名称搜索窗口）
    Ctrl+b w（从交互式窗口列表中选择窗口）
    
####  复制模式

tmux 中的窗口可能会处于几种模式中的一种。默认的模式下可以直接访问窗口中的终端。另一种模式是“复制模式”。在复制模式下用户可以浏览缓冲区、滚动浏览历史。复制模式下所使用的快捷键是 [vi](<../zh-cn/Vi.html> "Vi") 或是 [emacs](<../zh-cn/Emacs.html> "Emacs") 风格的。除非用户在 VISUAL 或是 EDITOR 变量中设置了 vi，否则复制模式中默认的快捷键绑定是 emacs 风格。 

按如下快捷键进入复制模式： 
    
    Ctrl+b [
    
然后就可以像在自己的编辑器里一样浏览缓冲区内容了。 

使用如下之一的快捷键退出复制模式： 

vi 模式下请使用： 
    
    q
    
emacs 模式下则是： 
    
    Esc
    
###  打开 URL

安装并配置好 [urlview](<https://aur.archlinux.org/packages/urlview/>)AUR 后才能在 tmux 中打开 URL。以下是配置示例： 

在一个新的终端中： 
    
    bind-key u capture-pane \; save-buffer /tmp/tmux-buffer \; run-shell "$TERMINAL -e urlview /tmp/tmux-buffer"
    
在一个新的 tmux 窗口中（无需打开新的终端）： 
    
    bind-key u capture-pane \; save-buffer /tmp/tmux-buffer \; new-window -n "urlview" '$SHELL -c "urlview < /tmp/tmux-buffer"'
    
###  设置正确的终端

####  256 色

如果用户使用的是 256 色终端，应在 tmux 中设置正确的终端如：`tmux` 或 `tmux-256color`： 
    
    tmux.conf
    
    set -g default-terminal "tmux-256color"

也可以使用 `tmux -2` 强制让 tmux 认定终端支持 256 色防止显示混乱。 

####  24 位深颜色

tmux 支持 24 位深颜色。如果用户使用的终端支持这一特性（请参考[这个链接](<https://github.com/termstandard/colors/blob/master/README.md>)），请将它添加至 `terminal-features`。 

例如，对于 [Alacritty](<../zh-cn/Alacritty.html> "Alacritty") 终端，请添加以下内容： 
    
    set -as terminal-features ",alacritty*:RGB"
    
对于其他终端，请使用 `$TERM` 的值替换上述的 `alacritty`。 

关于 `RGB` 的详细信息，请查阅 [tmux(1)](<https://man.archlinux.org/man/tmux.1>)。 

#### xterm-keys

将下面这一行内容添加至配置文件以启用 xterm-keys： 
    
    tmux.conf
    
    set-option -g xterm-keys on

注意，如果在 `tmux.conf` 中启用了 xterm-keys，用户需要自行构建一个自定义的 terminfo 用于声明新的转译码，否则应用程序将识别不到。使用 `tic` 编译以下内容之后，就可以将“xterm-screen-256color”作为 TERM 使用了： 
    
    # 一个以 screen- 前缀命名的 TERMINFO，
    # 用于声明由 tmux 配置“set-window-option -g xterm-keys”所启用的转译序列。
    #
    # 以 xterm- 前缀命名，因为一些应用程序除了检查终端功能，
    # 还会检查 TERM 名称。
    xterm-screen-256color|GNU Screen with 256 colors bce and tmux xterm-keys,
    
    # As of Nov'11, the below keys are picked up by
    # .../tmux/blob/master/trunk/xterm-keys.c:
    	kDC=\E[3;2~, kEND=\E[1;2F, kHOM=\E[1;2H,
    	kIC=\E[2;2~, kLFT=\E[1;2D, kNXT=\E[6;2~, kPRV=\E[5;2~,
    	kRIT=\E[1;2C,
    
    # 如果所用的终端不支持 bce，
    # 请将下面的内容改为 screen-256color：
    	use=screen-256color-bce,
    
使用 `tic -c` 检查所使用的终端是否支持 bce： 
    
    $ tic -c xterm-screen-256color 
    "xterm-screen-256color", line 16, terminal 'xterm-screen-256color': resolution of use=screen-256color-bce failed
    
将上述内容保存后使用 tic 编译： 
    
    $ tic xterm-screen-256color 
    
文件编译完成后会被保存到 `$HOME/.terminfo`（若以 root 运行，则会保存到 `/usr/share/terminfo/` 中，可全局使用）。 

###  定制主题

可以为 tmux 定制主题，但首先需要知道颜色代码。在终端中执行以下命令，将输出颜色代码与其对应的颜色示例： 
    
    $ for i in {0..255}; do printf "\x1b[38;5;${i}mcolor${i} - ██████████\n"; done
    
上述命令所输出的颜色代码可用于修改 tmux 的颜色主题。下面是一个修改状态栏颜色的示例： 
    
    # 状态栏颜色
    set -g status-bg "color4"         # 蓝色背景
    set -g status-fg "color7"         # 灰色文字
    set -g status-right "%l:%M %p"    # 时间格式
    set-window-option -g window-status-current-style "bg=color75,fg=color231 bold"    # 当前窗口的背景和前景色
    
面板边框也可以通过以下的方式设置主题颜色： 
    
    # 边框颜色
    set -g pane-border-style        fg="colour255"
    set -g pane-active-border-style fg="colour33"
    
###  其他设置

限制滚动缓冲区上限至最多 10000 行： 
    
    set -g history-limit 10000
    
切换鼠标支持： 
    
    bind-key m set-option -g mouse \; display "Mouse: #{?mouse,ON,OFF}"
    
###  随 systemd 启动

开机启动 tmux 有如下的好处。例如，创建一个新的 tmux 会话时，开机启动的 tmux 服务能缩减启动延迟。 

除此以外，如有特殊需求（例如需要加载大量的 tmux 配置项或是有共享的用户会话），开机启动 tmux 能够在用户不登录的情况下恢复并持续运行这些会话。 

下面这个服务为特定用户（例如，启动或启用 `tmux@_username_.service`）启动 tmux： 
    
    /etc/systemd/system/tmux@.service
    
    [Unit]
    Description=tmux session for user %I
    
    [Service]
    Type=forking
    User=%I
    # 警告：这里请使用 %I 而不要使用 %u，在系统服务中 %u=root。
    ExecStart=/usr/bin/tmux new-session -s %I -d
    ExecStop=/usr/bin/tmux kill-session -t %I
    
    [Install]
    WantedBy=multi-user.target

**提示：**

  * 可以添加 `WorkingDirectory=_自定义路径_` 以自定义工作目录。若设置为 `~`，将使用 `User=` 中指定的用户家目录。
  * 添加 `-v` 参数可在工作目录中生成 tmux 客户端和服务端的日志。
  * 若希望引入图形会话的相关环境变量，例如 `DISPLAY`、`WAYLAND_DISPLAY` 或 `SESSION_MANAGER`，请将 `WantedBy` 选项修改为 `graphical-session.target`，并在 `[Unit]` 下面添加 `After=graphical-session.target`。
  * 也可以创建一个在桌面环境（也可以是窗口管理器或者 Wayland 混成器）启动后自动执行的脚本，并使用 `tmux setenv -g name [value]` 加载并引入相关的环境变量。

也可以将此文件存放至 [systemd/用户](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "Systemd/用户")目录中（此时不需要 `User=%I`，同时还需要将 `WantedBy` 中的 `multi-user.target` 修改为 `default.target`），例如 `~/.config/systemd/user/tmux.service`。此时 tmux 服务会在用户登录时启动，并且由于[这个](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html#%E5%9C%A8%E6%B3%A8%E9%94%80%E5%90%8E%E7%BB%93%E6%9D%9F%E7%94%A8%E6%88%B7%E8%BF%9B%E7%A8%8B> "Systemd/用户")原因，用户服务会保持运行状态，登出并不会停止服务。除此以外还可以设置[随系统自动启动_systemd_用户实例](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html#%E9%9A%8F%E7%B3%BB%E7%BB%9F%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8_systemd_%E7%94%A8%E6%88%B7%E5%AE%9E%E4%BE%8B> "Systemd/用户")。 

##  会话初始化

将下面的内容添加到 `~/.tmux.conf` 中可在打开一个新的 tmux 会话时含有预加载的窗口： 
    
    new  -n WindowName Command
    neww -n WindowName Command
    neww -n WindowName Command
    
要让打开的新会话包含多个分割窗口，请将 `splitw` 命令添加至需要分割的 `neww` 下方，像这样： 
    
    new  -s SessionName -n WindowName Command
    neww -n foo/bar foo
    splitw -v -p 50 -t 0 bar
    selectw -t 1 
    selectp -t 0
    
将会打开两个窗口，其中第二个窗口的名称是 foo/bar，且会被垂直平均分割成 foo 和 bar 上下两个面板，foo 在 bar 的上方。窗口焦点会在窗口 2（foo/bar）内上方的面板（foo）中。 

**注意：** 会话、窗口和面板的序号都是从 0 开始，除非用户在 `.conf` 中指定序号从 1 开始。

在配置文件中 source 不同的会话文件可以实现多个会话的管理： 
    
    # 初始化多个会话
    bind F source-file ~/.tmux/foo
    bind B source-file ~/.tmux/bar
    
##  剪贴板集成

**提示：** tmux 插件 [tmux-yank](<https://github.com/tmux-plugins/tmux-yank>) 提供了类似的功能。

可以将 tmux 中选择的内容复制到显示服务的剪贴板（both primary/secondary selections），再粘贴回 tmux。下面的配置文件片段提供了将 X11 和 Wayland 剪贴板与当前的 tmux 集成的方法： 

**注意：** 下面的 Vim 风格示例中，需要使用 `unbind p` 解除“切换至上一个窗口”的快捷键的绑定，才能正常使用粘贴功能。

###  与 Xorg 集成

首先可以考虑使用 [xsel](<https://archlinux.org/packages/?name=xsel>)包： 

Emacs 风格: 
    
    bind-key -T copy-mode y send-keys -X copy-pipe-and-cancel "xsel -i -p && xsel -o -p | xsel -i -b"
    bind-key C-y run "xsel -o | tmux load-buffer - ; tmux paste-buffer"
    
Vim 风格: 
    
    bind-key -T copy-mode-vi y send-keys -X copy-pipe-and-cancel "xsel -i -p && xsel -o -p | xsel -i -b"
    bind-key p run "xsel -o | tmux load-buffer - ; tmux paste-buffer"
    
也可以使用 [xclip](<https://archlinux.org/packages/?name=xclip>)包 达到相同的目的。与 xsel 不同，xclip 在处理与目前区域设置（locale）不兼容的原始比特流时更好一些。尽管如此，使用 xsel 比 xclip 更干净整洁些，这是因为 xclip 在读取 tmux 缓冲区内容后并不会关闭 `STDOUT`。这样一来，tmux 就无法知道复制是否完成，并一直等待 xclip 终止，看起来就像是 tmux 不响应了一样。解决方法是将 `STDOUT` 重定向到 `/dev/null`： 

Emacs 风格: 
    
    bind-key -T copy-mode y send-keys -X copy-pipe-and-cancel "xclip -i -sel clip > /dev/null"
    bind-key C-y run "xclip -o -sel clip | tmux load-buffer - ; tmux paste-buffer"
    
Vim 风格: 
    
    bind-key -T copy-mode-vi y send-keys -X copy-pipe-and-cancel "xclip -i -sel clip > /dev/null"
    bind-key p run "xclip -o -sel clip | tmux load-buffer - ; tmux paste-buffer"
    
###  与 Wayland 集成

首先请确保安装了 [wl-clipboard](<https://archlinux.org/packages/?name=wl-clipboard>)包。 

Emacs 风格: 
    
    bind-key -T copy-mode y send-keys -X copy-pipe-and-cancel "wl-copy && wl-paste -n | wl-copy -p"
    bind-key C-y run "wl-paste -n | tmux load-buffer - ; tmux paste-buffer"
    
Vim 风格: 
    
    bind-key -T copy-mode-vi y send-keys -X copy-pipe-and-cancel "wl-copy && wl-paste -n | wl-copy -p"
    bind-key p run "wl-paste -n | tmux load-buffer - ; tmux paste-buffer"
    
###  在 Urxvt 中使用中键粘贴

**注意：** 启用鼠标支持后才能使用此功能。

tmux 有一个非官方的 perl 扩展（在 tmux 的官方 [FAQ](<https://github.com/tmux/tmux/wiki/FAQ>) 中有[提到](<https://github.com/tmux/tmux/wiki/FAQ#how-do-i-copy-a-selection-from-tmux-to-the-systems-clipboard>)），可在 urxvt 中通过鼠标中键粘贴剪贴板内容。 

首先，下载 perl 脚本并将其保存到 urxvt 的 perl 库中： 
    
    wget <http://anti.teamidiot.de/static/nei/*/Code/urxvt/osc-xterm-clipboard>
    mv osc-xterm-clipboard /usr/lib/urxvt/perl/

同时还需要在 .Xdefaults 中启用 perl 脚本： 
    
    ~/.Xdefaults
    
    ...
    *URxvt.perl-ext-common:		osc-xterm-clipboard
    ...
    
接下来，需要让 tmux 知道这个新功能，并启用鼠标支持（如果还未启用）： 
    
    ~/.tmux.conf
    
    ...
    set-option -ga terminal-override ',rxvt-uni*:XT:Ms=\E]52;%p1%s;%p2%s\007'
    set -g mouse on
    ...
    
这样就完成了。请结束所有 tmux 进程后再尝试新添加的中键功能。 

在 tmux 中，`Shift+MiddleMouseClick` 会粘贴剪贴板内容，而仅用鼠标中键会粘贴 tmux 缓冲区中的剪贴板内容。 

在 tmux 外部，仅用鼠标中键会粘贴 tmux 缓冲区内容，而标准 `Ctrl+c`用于复制。 

##  提示与技巧

###  以默认的会话布局启动 tmux

像 _tmuxinator_ 和 [tmuxp](</wzh/index.php?title=Tmuxp&action=edit&redlink=1> "Tmuxp（页面不存在）") 这样的会话管理器能简化通常的会话配置。 

要使用 _tmuxinator_ ，请安装 [tmuxinator](<https://aur.archlinux.org/packages/tmuxinator/>)AUR。安装完成后尝试运行以下命令测试安装是否成功： 
    
    $ tmuxinator doctor
    
####  获取默认布局参数

首先，根据个人的喜好启动并配置 tmux 窗口和面板。完成后，在当前会话内，执行下面的命令获取当前的布局参数值： 
    
    tmux list-windows
    
命令的输出可能会像下面这样（比如两个窗口，分别有 3 个和 2 个面板的布局）： 
    
    0: default* (3 panes) [274x83] [layout 20a0,274x83,0,0{137x83,0,0,3,136x83,138,0[136x41,138,0,5,136x41,138,42,6]}] @2 (active)
    1: remote- (2 panes) [274x83] [layout e3d3,274x83,0,0[274x41,0,0,4,274x41,0,42,7]] @3                                         
    
这其中需要复制并在这之后使用到的部分，是从 **[layout...** 之后开始到 **... ] @2 (active)** 之前的部分。对于上面的例子，第一个窗口的布局对应的内容是 **20a0,274x83,0,0{137x83,0,0,3,136x83,138,0[136x41,138,0,5,136x41,138,42,6]}** 。 

####  定义默认的 tmux 布局

在上一节中获取到需要的布局信息后，就可以退出当前的 tmux 会话了。然后编辑 tmuxinator 的配置文件来创建自定义的默认 tmux 会话布局（不要复制示例，用上一节获取到的布局信息）： 
    
    ~/.tmuxinator/default.yml
    
    name: default
    root: ~/
    windows:
      - default:
          layout: 20a0,274x83,0,0{137x83,0,0,3,136x83,138,0[136x41,138,0,5,136x41,138,42,6]}
          panes:
            - clear
            - vim
            - clear && emacs -nw
      - remote:
          layout: 24ab,274x83,0,0{137x83,0,0,3,136x83,138,0,4}
          panes:
            - 
            - 
    
上面的示例定义了两个窗口（名称分别是“default”和“remote”）和用户定义的布局参数值。每个面板设置都需要至少一行 `-`。tmux 启动时，第一个窗口中的第一个面板中执行了“clear”，第二个面板中是“vim”，第三个面板中执行了“clear && emacs -nw”。第二个窗口中的两个面板在启动时都没有执行任何命令。 

使用如下命令测试新的默认布局： 
    
    tmuxinator default
    
####  令 tmux 自启动时使用默认布局

如果希望自启动 tmux 会话时使用自定义的默认布局，请按下面的示例编辑： 
    
    ~/.bashrc
    
     if [ -z "$TMUX" ]; then
       tmuxinator default          
     fi                     
    
####  使用默认会话的其他方法

除了以上的方法，也可以直接编写一个在执行时创建并附加默认会话的 bash 脚本。 

然后就能在终端执行并获得一个预先配置好的 tmux 会话了： 
    
    #!/bin/bash
    tmux new-session -d -n WindowName Command
    tmux new-window -n NewWindowName
    tmux split-window -v
    tmux selectp -t 1
    tmux split-window -h
    tmux selectw -t 1
    tmux -2 attach-session -d
    
###  在 Urxvt 中启动 tmux

使用下面的命令启动一个带 tmux 会话的 urxvt，可以将这段命令保存至 .ratpoisonrc 文件中： 
    
    urxvt -e bash -c "tmux -q has-session && exec tmux attach-session -d || exec tmux new-session -n$USER -s$USER@$HOSTNAME"

###  在每次登录时启动 tmux
    
    if [ -x "$(command -v tmux)" ] && [ -n "${DISPLAY}" ] && [ -z "${TMUX}" ]; then
        exec tmux new-session -A -s ${USER} >/dev/null 2>&1
    fi
    
上面的片段完成了这些操作： 

  1. 测试 tmux 是否是可执行的命令，
  2. 并且图形化会话是否在运行（若希望让 tmux 在任意登录 shell 中启动，请**删除这个条件** ，但这可能会干扰[登录时自动启动 X](<../zh-cn/Xinit.html#%E7%99%BB%E5%BD%95%E6%97%B6%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8_X> "Xinit")），
  3. 并且目前不在某个 tmux 会话中，
  4. 然后尝试加入（attach）已有会话，如果失败，就创建一个新的会话。

如果已配置[ systemd 保留会话](<#%E9%9A%8F_systemd_%E5%90%AF%E5%8A%A8>)，可以用下面的命令替换上面 if 语句块中的内容，这样 tmux 会加入被保留的会话并退出其他所有已加入该会话的客户端。 
    
    if ! systemctl --user is-active --quiet tmux.service; then
        systemctl --user start tmux.service
    fi
    exec tmux attach-session -d -t "${USER}" >/dev/null 2>&1
    
###  启动一个非登录 shell

tmux [默认](<https://www.mail-archive.com/tmux-users@lists.sourceforge.net/msg05901.html>)启动一个[登录 shell](<../zh-cn/%E5%91%BD%E4%BB%A4%E8%A1%8C%E8%A7%A3%E9%87%8A%E5%99%A8.html#%E7%99%BB%E5%BD%95_Shell> "命令行解释器")，这有可能产生许多负面影响： 

  * [fortune](<https://en.wikipedia.org/wiki/fortune_\(Unix\)> "wikipedia:fortune \(Unix\)") 用户可能会注意到在创建新的面板时，引号也被输出到了屏幕上。
  * 每次创建新面板时，为登录 shell 所配置的文件例如 `~/.profile` 都会被重新解析，这也导致了一些本应在会话初始化时才需要执行的命令在创建新面板时再次执行（比如设置音量）。

将下面的内容添加到 `~/.tmux.conf` 中以禁用 tmux 默认启动登录 shell 的行为： 
    
    set -g default-command "${SHELL}"
    
###  将 tmux 窗口用作选项卡

将下面的内容添加到 `~/.tmux.conf` 后就可以像选项卡一样使用 tmux 的窗口了，具体请参考 [urxvt's tabbing 扩展](</wzh/index.php?title=Rxvt-unicode/Tips_and_tricks&action=edit&redlink=1> "Rxvt-unicode/Tips and tricks（页面不存在）")所提供的参考快捷键。这样做的优点是，这些虚拟的“选项卡”是独立于终端模拟器的。 
    
    #urxvt tab like window switching (-n: no prior escape seq)
    bind -n S-down new-window
    bind -n S-left prev
    bind -n S-right next
    bind -n C-left swap-window -t -1
    bind -n C-right swap-window -t +1
    
但要注意这些快捷键不应覆盖其他应用程序的快捷键。例如终端，虽然终端上可能未激活这些快捷键。 

同样也可以很方便地提供用于 tmux detach 所对应的 EOT 快捷键 `Ctrl+d`： 
    
    bind-key -n C-j detach
    
###  客户端同时与会话中的多个窗口交互

Brandur Leach 在 [Practical Tmux](<https://mutelight.org/practical-tmux#section-6>) 中写了这么一段内容： 

    Screen and tmux's behaviour for when multiple clients are attached to one session differs slightly. In Screen, each client can be connected to the session but view different windows within it, but in tmux, all clients connected to one session must view the same window.
    This problem can be solved in tmux by spawning two separate sessions and synchronizing the second one to the windows of the first, then pointing a second new session to the first.

翻译内容如下： 

    Screen 和 tmux 在多个客户端加入同一个会话时的行为稍微有些不同。Screen 中，每个客户端在连接到会话后，可以在各个客户端中浏览不同的窗口，而在 tmux 中，所有连接到同一会话的客户端都只能浏览同一个窗口（即不同的客户端所显示的内容都是一样的）。
    这个问题的解决方法是在 tmux 中创建两个独立的会话，将第二个会话同步到第一个会话的窗口，然后将第二个新会话指向第一个会话。

下面的 `tmx` 脚本实现了上面所说的解决方法。这里的版本稍微进行了一些调整，假设第二个参数是 `1`，那么执行 `tmux new-window`。脚本中调用的 `tmx _base_session_name_ [1]` 用于启动所必需的基础会话。否则，将一个新的“客户端”会话连接到前置会话（可选添加新窗口并加入），并设置其一旦变成僵尸进程就终止。最后记得为脚本[添加可执行权限](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "Help:阅读")。 
    
    ~/bin/tmx
    
    #!/bin/bash
    # Modified TMUX start script from:
    #     http://forums.gentoo.org/viewtopic-t-836006-start-0.html
    
    # Works because bash automatically trims by assigning to variables and by passing arguments
    trim() { echo $1; }
    
    if [[ -z "$1" ]]; then
        echo "Specify session name as the first argument"
        exit
    fi
    
    # Only because I often issue `ls` to this script by accident
    if [[ "$1" == "ls" ]]; then
        tmux ls
        exit
    fi
    
    base_session="$1"
    # This actually works without the trim() on all systems except OSX
    tmux_nb=$(trim `tmux ls | grep "^$base_session" | wc -l`)
    if [[ "$tmux_nb" == "0" ]]; then
        echo "Launching tmux base session $base_session ..."
        tmux new-session -s $base_session
    else
        # Make sure we are not already in a tmux session
        if [[ -z "$TMUX" ]]; then
            echo "Launching copy of base session $base_session ..."
            # Session id is date and time to prevent conflict
            session_id=`date +%Y%m%d%H%M%S`
            # Create a new session (without attaching it) and link to base session 
            # to share windows
            tmux new-session -d -t $base_session -s $session_id
            if [[ "$2" == "1" ]]; then
    		# Create a new window in that session
    		tmux new-window
    	fi
            # Attach to the new session & kill it once orphaned
    	tmux attach-session -t $session_id \; set-option destroy-unattached
        fi
    fi
    
对此，有用的设置是： 
    
    setw -g aggressive-resize on
    
将上面这个添加到 `~/.tmux.conf`。可以让 tmux 基于最小的客户端实际大小来调整窗口大小，而非整个会话中最小的。 

另一种做法是把下面的内容添加到 `~/.bashrc`： 
    
    ~/.bashrc
    
    function rsc() {
      CLIENTID=$1.`date +%S`
      tmux new-session -d -t $1 -s $CLIENTID \; set-option destroy-unattached \; attach-session -t $CLIENTID
    }
    
    function mksc() {
      tmux new-session -d -s $1
      rsc $1
    }
    
引用作者： 

    "mksc foo" creates a always detached permanent client named "foo". It also calls "rsc foo" to create a client to newly created session. "rsc foo" creates a new client grouped by "foo" name. It has destroy-unattached turned on so when I leave it, it kills client.
    Therefore, when my computer looses network connectivity, all "foo.something" clients are killed while "foo" remains. I can then call "rsc foo" to continue work from where I stopped.

###  根据终端类型调整正确的 TERM 变量值

除了可以[在 tmux 中为 TERM 变量设置固定值](<#%E8%AE%BE%E7%BD%AE%E6%AD%A3%E7%A1%AE%E7%9A%84%E7%BB%88%E7%AB%AF>)，还可以根据终端模拟器的类型设置正确的 TERM（`screen` 或 `screen-256color`）： 
    
    ~/.tmux.conf
    
    ## set the default TERM
    set -g default-terminal screen
    
    ## update the TERM variable of terminal emulator when creating a new session or attaching a existing session
    set -g update-environment 'DISPLAY SSH_ASKPASS SSH_AGENT_PID SSH_CONNECTION WINDOWID XAUTHORITY TERM'
    ## determine if we should enable 256-colour support
    if "[[ ${TERM} =~ 256color || ${TERM} == fbterm ]]" 'set -g default-terminal screen-256color'
    
    ~/.zshrc
    
    ## workaround for handling TERM variable in multiple tmux sessions properly (by Nicholas Marriott)
    if [[ -n ${TMUX} && -n ${commands[tmux]} ]];then
            case $(tmux showenv TERM 2>/dev/null) in
                    *256color) ;&
                    TERM=fbterm)
                            TERM=screen-256color ;;
                    *)
                            TERM=screen
            esac
    fi

###  重新加载更新过的配置但无需重启 tmux

tmux 默认只在启动时读取 `~/.tmux.conf`。要让 tmux 在启动后加载配置文件，执行下面的命令： 
    
    tmux source-file _配置文件路径_
    
这条命令也可以添加到 `~/.tmux.conf` 中： 
    
    ~/.tmux.conf
    
     bind r source-file _文件路径_

然后执行下面的命令，效果同上： 
    
    source .tmux.conf
    
###  在新会话或加入会话时运行程序的脚本模板

下面的脚本会检查某个程序是否是已经运行的状态，如果找到该程序，就将它附加到会话并选择该窗口。如果没有找到，那就创建一个新的 tmux 会话，同时创建一个用该程序命名的新窗口，并在该窗口中运行此程序。 
    
    #!/bin/bash
    
    PID=$(pidof $1)
    
    if [ -z "$PID" ]; then
        tmux new-session -d -s main ;
        tmux new-window -t main -n $1 "$*" ;
    fi
        tmux attach-session -d -t main ;
        tmux select-window -t $1 ;
    exit 0
    
[这里有一个](<../zh-cn/Irssi.html> "Irssi")由此派生出的版本，用于配合 _nicklist_ 运行 _irssi_ 。 

###  终端模拟器的窗口标题

如果用户是通过 SSH 登录进的 tmux 窗口，终端模拟器的窗口标题依然会显示 `user@localhost` 而非 `user@server`。要让标题栏自适应显示所连接的远程主机名，请在 `~/.tmux.conf` 中设置以下内容： 
    
    set -g set-titles on
    set -g set-titles-string "#T"
    
对于 `set-titles-string`，`#T` 会显示为 `user@host:~` 并根据用户所连接到的不同主机显示对应的主机名称。 

###  自动设置布局

在创建或销毁分割窗口时，并不会应用当前所选定的布局。将下面的按键绑定添加到配置文件中可以解决这个问题： 
    
    bind-key -n M-c kill-pane \; select-layout
    bind-key -n M-n split-window \; select-layout
    
**提示：**[tmux-xpanes](<https://aur.archlinux.org/packages/tmux-xpanes/>)AUR 可以简化窗口布局管理和 SSH 连接，感兴趣可以尝试。

###  Vim 颜色主题未能加载

如果 tmux 中的 vim 颜色主题没有正常加载，请参阅[[1]](<https://stackoverflow.com/a/47994805>)和[[2]](<https://github.com/vim/vim/issues/993#issuecomment-255651605>)。 

###  对 Vim 用户友好的配置

参考[[3]](<https://gist.github.com/Lartza/6a7a62466a8a3e436234412d9b1c5066>)。 

###  更好的面板分割

默认的分割面板快捷键分别是，垂直分割：`Ctrl+b %`，水平分割：`Ctrl+b "`。对于有些键盘布局而言较难按下，而且也不便于记忆。 

一种对用户而言更友好且方便记忆的的快捷键绑定是使用 `Ctrl+b h` 水平分割，以及用 `Ctrl+b v` 垂直分割面板。 

将下面的内容添加到 `~/.tmux.conf` 中可以实现快捷键更改： 
    
    # 更好的面板分割快捷键：
    bind-key h split-window -h
    bind-key v split-window -v
    
###  防止系统休眠

如果 tmux 所连接到的主机因为进入睡眠模式而挂起，请使用 inhibition lock 运行会话： 
    
    tmux new-session -A "systemd-inhibit --what=idle $SHELL"
    
##  故障排除

###  缓冲区滚动问题

如果在终端内使用 `Shift+Page Up` 或 `Shift+Page Down` 滚动时需要问题，下面的配置项可以禁用任意终端的 _smcup_ 和 _rmcup_ 功能（这些会将所有操作反馈前都添加 `xterm`）： 
    
    set -ga terminal-overrides ',xterm*:smcup@:rmcup@'
    
这样的技巧会使终端模拟器认为 tmux 是一个全屏的应用程序，就像 pico 或 mutt 一样（参考[[4]](<https://superuser.com/questions/310251/use-terminal-scrollbar-with-tmux>)）。这时滚动操作就会被正确记录下来。但要注意，这样做之后，在窗口或面板间切换时可能会引起一些显示混乱。所以请考虑使用 tmux 原生的滚动历史功能。 

###  鼠标滚动

**注意：** 这会干扰剪贴板复制粘贴功能。要复制或粘贴剪贴板，请按住 Shift 键。

要使用鼠标滚轮滚动缓冲区内容，请先确保启用了鼠标： 
    
    set -g mouse on
    
设置最大可回滚历史记录数： 
    
    set -g history-limit 30000
    
自 tmux 2.1 版本开始，请将下面的内容之一或全部添加到 ~/.tmux.conf 中： 
    
       bind -T root WheelUpPane   if-shell -F -t = "#{alternate_on}" "send-keys -M" "select-pane -t =; copy-mode -e; send-keys -M"
       bind -T root WheelDownPane if-shell -F -t = "#{alternate_on}" "send-keys -M" "select-pane -t =; send-keys -M"
    
由于上面的配置每次只能滚动一行，添加下面的配置能让每次滚动时滚动一整页： 
    
       bind -t vi-copy    WheelUpPane   page-up
       bind -t vi-copy    WheelDownPane page-down
       bind -t emacs-copy WheelUpPane   page-up
       bind -t emacs-copy WheelDownPane page-down
    
###  终端模拟器不支持 UTF-8 鼠标事件

已设置 `mouse on` 选项，且终端模拟器不支持 UTF-8 鼠标事件时，在终端窗口中左键点击可能会粘贴如 `[M#` 或 `[Ma` 的字符串。 

配置以下内容可以解决这个问题： 
    
    set -g mouse-utf8 off
    
###  Midnight Commander 中 Shift+F6 无效

请参阅 [Midnight_Commander#快捷键失效](<../zh-cn/Midnight_Commander.html#%E5%BF%AB%E6%8D%B7%E9%94%AE%E5%A4%B1%E6%95%88> "Midnight Commander")。 

##  另见

  * [BBS topic](<https://bbs.archlinux.org/viewtopic.php?id=84157&p=1>)
  * [Screen and tmux feature comparison](<https://www.dayid.org/os/notes/tm.html>)
  * [powerline](<https://github.com/Lokaltog/powerline>)，tmux 动态状态栏。
  * [Plugins for tmux](<https://github.com/tmux-plugins>)
  * [Oh My Tmux!](<https://github.com/gpakosz/.tmux>)
  * [tmux Wiki](<https://github.com/tmux/tmux/wiki>)

**教程**

  * [Practical Tmux](<https://mutelight.org/practical-tmux>)
  * 手册页 [tmux(1)](<https://man.archlinux.org/man/tmux.1>)
  * [Tmux tutorial Part 1](<https://www.hawkhost.com/blog/2010/06/28/tmux-the-terminal-multiplexer/>) 和 [Part 2](<https://www.hawkhost.com/blog/2010/07/02/tmux-the-terminal-multiplexer-part-2/>)
  * [_The Tao of tmux_](<https://leanpub.com/the-tao-of-tmux/read>)，Tony Narlock 所著的电子书，同时也是 [tmuxp](<https://tmuxp.git-pull.com>) 和 [libtmux](<https://libtmux.git-pull.com>) 的作者
