相关文章

  * [显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")
  * [Wayland](<../zh-cn/Wayland.html> "Wayland")
  * [Sway](<../zh-cn/Sway.html> "Sway")

**翻译状态：**

  * 本文（或部分内容）译自 [Greetd](<https://wiki.archlinux.org/title/Greetd> "arch:Greetd")，最近一次同步于 2025-02-24，若英文版本有所[更改](<https://wiki.archlinux.org/title/Greetd?diff=0&oldid=827637>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Greetd_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[greetd](<https://git.sr.ht/~kennylevinsen/greetd>) is a minimal, agnostic and flexible [login manager](</wzh/index.php?title=Login_manager&action=edit&redlink=1> "Login manager（页面不存在）") daemon which does not make assumptions about what the user wants to launch, should it be console-based or graphical. Any script or program which can be started from the console may be launched by greetd, which makes it particularly suitable for [Wayland compositors](<../zh-cn/Wayland.html#Compositors> "Wayland"). It can also launch a [greeter](<#Greeters>) to start user sessions, like any other display manager. 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [greetd](<https://archlinux.org/packages/?name=greetd>)包 或 [greetd-git](<https://aur.archlinux.org/packages/greetd-git/>)AUR。 

默认配置文件位于 `/etc/greetd/config.toml`。 [PAM](<../zh-cn/PAM.html> "PAM") 相关的配置文件位于 `/etc/pam.d/greetd`。 

###  欢迎界面（Greeters）

Greetd 内置的默认欢迎界面是 greetd-agreety，这是一个最小化的实现。您可以考虑换成其他的欢迎界面： 

  * **greetd-agreety** — 默认的，基于文本的欢迎界面，类似于 [agetty](</wzh/index.php?title=Agetty&action=edit&redlink=1> "Agetty（页面不存在）")

     <https://git.sr.ht/~kennylevinsen/greetd> || [greetd-agreety](<https://archlinux.org/packages/?name=greetd-agreety>)包

  * **cosmic-greeter** — 一个基于 [libcosmic](<../zh-cn/COSMIC.html> "Libcosmic") 的欢迎界面

     <https://github.com/pop-os/cosmic-greeter> || [cosmic-greeter](<https://archlinux.org/packages/?name=cosmic-greeter>)包

  * **dlm** — 一个基于 fbdev 的欢迎界面

     <https://git.sr.ht/~kennylevinsen/dlm> || [greetd-dlm-git](<https://aur.archlinux.org/packages/greetd-dlm-git/>)AUR

  * **ddlm** — 一个基于 fbdev 的欢迎界面。`dlm` 的改进/扩展版本

     <https://github.com/deathowl/ddlm> || [greetd-ddlm-git](<https://aur.archlinux.org/packages/greetd-ddlm-git/>)AUR

  * **gtkgreet** — 一个基于 [GTK](<../zh-cn/GTK.html> "GTK") 的欢迎界面

     <https://git.sr.ht/~kennylevinsen/gtkgreet> || [greetd-gtkgreet](<https://archlinux.org/packages/?name=greetd-gtkgreet>)包，[greetd-gtkgreet-git](<https://aur.archlinux.org/packages/greetd-gtkgreet-git/>)AUR

  * **ReGreet** — 一个基于 [GTK](<../zh-cn/GTK.html> "GTK") 的欢迎界面，支持不同的个性化选项，仅支持 Wayland

     <https://github.com/rharish101/ReGreet> || [greetd-regreet](<https://archlinux.org/packages/?name=greetd-regreet>)包，[greetd-regreet-git](<https://aur.archlinux.org/packages/greetd-regreet-git/>)AUR

  * **wlgreet** — 一个使用 [Wayland](<../zh-cn/Wayland.html> "Wayland") 的欢迎界面

     <https://git.sr.ht/~kennylevinsen/wlgreet> || [greetd-wlgreet](<https://aur.archlinux.org/packages/greetd-wlgreet/>)AUR，[greetd-wlgreet-git](<https://aur.archlinux.org/packages/greetd-wlgreet-git/>)AUR

  * **tuigreet** — 一个使用控制台 UI 的欢迎界面

     <https://github.com/apognu/tuigreet> || [greetd-tuigreet](<https://archlinux.org/packages/?name=greetd-tuigreet>)包

  * **qtgreet** — 一个基于 [Qt](<../zh-cn/Qt.html> "Qt") 的欢迎界面

     <https://gitlab.com/marcusbritanicus/QtGreet> || [greetd-qtgreet](<https://aur.archlinux.org/packages/greetd-qtgreet/>)AUR

  * **nwg-hello** — 一个用 Python 写的基于 GTK3 的欢迎界面

     <https://github.com/nwg-piotr/nwg-hello> || [nwg-hello](<https://archlinux.org/packages/?name=nwg-hello>)包

##  启动 greetd

[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `greetd.service`，以便在启动时启动 greetd。 

参见[显示管理器#加载显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html#%E5%8A%A0%E8%BD%BD%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8> "显示管理器"). 

##  欢迎界面（Greeter）配置

在 `/etc/greetd/config.toml` 的 `default_session` 节中的 `command` 选项配置 greetd 运行的欢迎界面。若没有做出更改，将使用内置的 `agreety` 欢迎界面。另请参阅 [#agreety](<#agreety>)。 

欢迎界面默认由 `greeter` 用户运行，您可在配置文件的 `default_session` 节中的 `user` 选项更改用户。将以下片段中的 _目标用户_ 改为您想使用的用户： 
    
    ...
    [default_session]
    user = "目标用户"
    ...
    
确保该用户具有 `/etc/greetd` 目录的[所有权](<../zh-cn/%E6%96%87%E4%BB%B6%E6%9D%83%E9%99%90%E4%B8%8E%E5%B1%9E%E6%80%A7.html#%E6%9B%B4%E6%94%B9%E6%89%80%E6%9C%89%E8%80%85> "文件权限与属性")。 

### agreety

这是默认的欢迎界面。以下配置文件片段会让 greetd 启动 agreety： 
    
    ...
    [default_session]
    command = "agreety --cmd $SHELL"
    ...
    
一旦用户登录，agreety 可以执行任意命令。例如，要启动 [Sway](<../zh-cn/Sway.html> "Sway")，将上例中的 `$SHELL` 改为 `sway`。 

### gtkgreet

gtkgreet 需要一个混成器才能运行。要获取完整体验需要一个具有 `wlr-layer-shell-unstable` 支持的混成器，当然其他的也能用。例如，推荐使用 [sway](<https://archlinux.org/packages/?name=sway>)包，但是其他的一些如 [cage](<https://archlinux.org/packages/?name=cage>)包 也能用，下文提供了此二者的示例。 

为指定 gtkgreet 可启动的登录环境，请在 `/etc/greetd/environments` 列出它们。 例如： 
    
    sway
    bash
    
您也可以为 gtkgreet 添加 `-c _mycommand_` 参数，将 _mycommand_ 替换为所需程序（例如，`gtkgreet -c bash` 或 `gtkgreet -c sway`）。根据所需在以下两个混成器示例中执行该操作。 

####  使用 cage

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [cage](<https://archlinux.org/packages/?name=cage>)包 并按照以下片段配置 `command` 选项： 
    
    ...
    [default_session]
    command = "cage gtkgreet"
    ...
    
####  使用 sway

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [sway](<https://archlinux.org/packages/?name=sway>)包。请注意，使用 [Sway](<../zh-cn/Sway.html> "Sway") 时，一旦用户登录，其必须被停止，为此您需要创建一个特定的配置文件。例如位于 `/etc/greetd/sway-config`，具有以下内容： 
    
    # `-l` activates layer-shell mode. Notice that `swaymsg exit` will run after gtkgreet.
    exec "gtkgreet -l; swaymsg exit"
    
    bindsym Mod4+shift+e exec swaynag \
    -t warning \
    -m 'What do you want to do?' \
    -b 'Poweroff' 'systemctl poweroff' \
    -b 'Reboot' 'systemctl reboot'
    
    include /etc/sway/config.d/*
    
接下来，greetd 必须被设定为以上述配置文件运行 [Sway](<../zh-cn/Sway.html> "Sway")。按照以下片段设置 `command` 选项： 
    
    ...
    [default_session]
    command = "sway --config /etc/greetd/sway-config"
    ...
    
### ReGreet

ReGreet 和 gtkgreet 一样需要混成器，和 gtkgreet 一样可以使用 Cage 和 Sway。只需将上述配置中的 _gtkgreet_ 命令换成 _regreet_ 。对 sway 配置应当如此： 
    
    # Notice that `swaymsg exit` will run after ReGreet.
    exec "regreet; swaymsg exit"
    
    bindsym Mod4+shift+e exec swaynag \
    -t warning \
    -m 'What do you want to do?' \
    -b 'Poweroff' 'systemctl poweroff' \
    -b 'Reboot' 'systemctl reboot'
    
    include /etc/sway/config.d/*
    
ReGreet 从 `/usr/share/xsession`（X11 会话）和 `/usr/share/wayland-sessions`（Wayland 会话）选取可用的会话，因此无需在`/etc/greetd/environments` 中列出会话。 

ReGreet can be configured through a TOML file in `/etc/greetd/regreet.toml`. A sample file is provided in `/usr/share/doc/greetd-regreet/regreet.sample.toml` with all available options. Copy this to `/etc/greetd/regreet.toml` and make the changes you want, commenting out or deleting the lines you do not need. Any invalid options are ignored. 

### wlgreet

Wlgreet 需要一个具有 `wlr-layer-shell-unstable` 支持的混成器。配置类似于[上文](<#%E4%BD%BF%E7%94%A8_sway>)为 gtkgreet 设定 Sway，如下： 
    
    /etc/greetd/sway-config
    
    exec "wlgreet --command sway; swaymsg exit"
    
    bindsym Mod4+shift+e exec swaynag \
    -t warning \
    -m '君欲何为？' \
    -b '关机' 'systemctl poweroff' \
    -b '重启' 'systemctl reboot'
     
    include /etc/sway/config.d/*

**提示：** 亦如[上文](<#%E4%BD%BF%E7%94%A8_sway>)，该配置文件可以位于任意位置，只要其被 Greetd 用于启动 Sway。

### tuigreet

tuigreet does not require any special setup, just set the `command` option as follows: 
    
    ...
    [default_session]
    command = "tuigreet --cmd sway"
    ...
    
`tuigreet --help` will display customization options. 

### ddlm

ddlm does not require any special setup, just set the `command` option as follows: 
    
    ...
    [default_session]
    command = "ddlm --target sway"
    ...
    
### qtgreet

In order to use qtgreet, you need a WLR based compositor (e.g. [wayfire](<https://aur.archlinux.org/packages/wayfire/>)AUR, [sway](<https://archlinux.org/packages/?name=sway>)包). 

#### Using Wayfire

[Install](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") [wayfire](<https://aur.archlinux.org/packages/wayfire/>)AUR and set the `command` option as follows: 
    
    ...
    [default_session]
    command = "wayfire --config /etc/qtgreet/wayfire.ini"
    ...
    
The Wayfire configuration file referred to is included with qtgreet. 

#### Using Hyprland

Set the `command` option as follows: 
    
    ...
    [default_session]
    command = "Hyprland --config /etc/greetd/hyprland.conf"
    ...
    
Then create `/etc/greetd/hyprland.conf` as: 
    
    /etc/greetd/hyprland.conf
    
    exec-once = qtgreet; hyprctl dispatch exit
    
### nwg-hello

In order to use nwg-hello, you either need [sway](<https://archlinux.org/packages/?name=sway>)包 or [hyprland](<https://archlinux.org/packages/?name=hyprland>)包. 

#### Using Sway

[Install](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") [sway](<https://archlinux.org/packages/?name=sway>)包 and set the `command` option as follows: 
    
    ...
    [default_session]
    command = "sway -c /etc/nwg-hello/sway-config"
    ...
    
The Sway configuration file referred to is included with nwg-hello. 

#### Using Hyprland

[Install](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") [hyprland](<https://archlinux.org/packages/?name=hyprland>)包 and set the `command` option as follows: 
    
    ...
    [default_session]
    command = "Hyprland -c /etc/nwg-hello/hyprland.conf"
    ...
    
The Hyprland configuration file referred to is included with nwg-hello. 

##  提示和技巧

###  自动登录

要让某用户自动登录，请在 `/etc/greetd/config.toml` 中定义 `initial_session` 节： 
    
    ...
    [initial_session]
    command = "sway"
    user = "_myuser_ "
    ...
    
`command` 选项可以是任意可执行文件，在上例中，系统启动后会以 `_myuser_` 用户运行 Sway。 

若您不想用 _greetd_ 且要使用自动登录，请参阅[autologin](<https://git.sr.ht/~kennylevinsen/autologin>)。 

###  运行本地程序

将您的 PATH 添加到 `~/.profile`，否则 greetd 唤起的桌面环境将无法运行本地程序。Greetd 不会访问 `.bashrc` 和 `.zshrc`，因此不要在这两个文件中设置 PATH。 
    
    ~/.profile
    
    export PATH="$HOME/.local/bin:$PATH"

###  设定环境

Greetd 默认不会设定环境变量如 XDG_SESSION_TYPE 和 XDG_CURRENT_DESKTOP 除非欢迎界面基于您设置的会话设定了环境变量（例如 TUI 会基于会话文件选择的区域设定会话类型）。一种方案是在执行实际命令前用一个脚本设定需要的环境变量，例如要启动 sway： 
    
    /usr/local/bin/start-sway
    
    #!/bin/sh
    export XDG_SESSION_TYPE=wayland
    export XDG_SESSION_DESKTOP=sway
    export XDG_CURRENT_DESKTOP=sway
    
    # Wayland stuff
    export QT_QPA_PLATFORM=wayland
    export SDL_VIDEODRIVER=wayland
    export _JAVA_AWT_WM_NONREPARENTING=1
    
    exec sway "$@"

然后让欢迎界面运行该脚本，例如使用 `gtkgreet` 可以如此： 
    
    /etc/greetd/config.toml
    
    ...
    [default_session]
    command = "gtkgreet -c /usr/local/bin/start-sway"
    ...

或将 `start-sway` 置入 `/etc/greetd/environments`。 

参阅 [How to Set XDG_SESSION_TYPE=wayland](<https://man.sr.ht/~kennylevinsen/greetd/#how-to-set-xdg_session_typewayland>)。 

###  设定 logind 会话类型

**注意：** This is necessary for running GNOME on Wayland properly.

The logind session type is set by the XDG_SESSION_TYPE environment variable. However, it must be set **before** the PAM session is opened. Because of this, setting the variable through `~/.profile` or a wrapper script will not work (both happen after session open). 

The correct way to achieve this is through the environment variables sent by greeters (these are set before session open). So if your greeter supports it, just make it send the appropriate `XDG_SESSION_TYPE=xxx.`

If your greeter does not support this, it is also possible to use [pam_env](<../zh-cn/Environment_variables.html#Using_pam_env> "Environment variables") under the auth group. The drawback is that all the sessions spawned by greetd will use that session type, which may or may not be problematic depending on your use case. 

Here is how one could use the pam_env method to have a Wayland session: 
    
    /etc/greetd/config.toml
    
    [general]
    service = "greetd-spawn"
    
    /etc/greetd/greetd-spawn.pam_env.conf
    
    XDG_SESSION_TYPE DEFAULT=wayland OVERRIDE=wayland
    
    /etc/pam.d/greetd-spawn
    
    auth       include      greetd
    auth       required     pam_env.so conffile=/etc/greetd/greetd-spawn.pam_env.conf
    account    include      greetd
    session    include      greetd

###  缺失鼠标指针

若您在一些类似于 `wayfire` 的混成器上使用 `qtgreet`，您通常需要设置某些环境变量以使鼠标指针正常工作，例如 `WLR_NO_HARDWARE_CURSORS=1`。一种方案是创建一个[可执行](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "可执行")脚本并在 `/etc/greetd/config.toml` 中调用它： 
    
    /usr/local/bin/greetd-startup.sh
    
    #!/bin/sh
    export WLR_NO_HARDWARE_CURSORS=1
    exec wayfire --config /etc/qtgreet/wayfire.ini
    
    /etc/greetd/config.toml
    
    ...
    [default_session]
    command = "/usr/local/bin/greetd-startup.sh"
    ...

##  参见

  * [greetd 项目页面](<https://sr.ht/~kennylevinsen/greetd/>)
  * [greetd 源代码](<https://git.sr.ht/~kennylevinsen/greetd/>)
  * [greetd 维基](<https://man.sr.ht/%7Ekennylevinsen/greetd/>)
