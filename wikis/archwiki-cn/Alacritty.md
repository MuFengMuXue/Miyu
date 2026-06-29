**翻译状态：**

  * 本文（或部分内容）译自 [Alacritty](<https://wiki.archlinux.org/title/Alacritty> "arch:Alacritty")，最近一次同步于 2024-11-13，若英文版本有所[更改](<https://wiki.archlinux.org/title/Alacritty?diff=0&oldid=820548>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Alacritty_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Alacritty](<https://github.com/alacritty/alacritty>)，一个用 [Rust](<../zh-cn/Rust.html> "Rust") 语言编写的，简洁、具有 GPU 加速功能的终端模拟器。它支持回滚、24 位颜色（[zhwp:色彩深度](<https://zh.wikipedia.org/wiki/%E8%89%B2%E5%BD%A9%E6%B7%B1%E5%BA%A6> "zhwp:色彩深度")）、复制粘贴、点击 URL 和自定义按键绑定。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [alacritty](<https://archlinux.org/packages/?name=alacritty>)包 包或者开发版本 [alacritty-git](<https://aur.archlinux.org/packages/alacritty-git/>)AUR。 

##  配置

Alacritty 按照以下顺序搜索配置文件： 

  * `$XDG_CONFIG_HOME/alacritty/alacritty.toml`
  * `$XDG_CONFIG_HOME/alacritty.toml`
  * `$HOME/.config/alacritty/alacritty.toml`
  * `$HOME/.alacritty.toml`

0.13.0 以前的版本使用 YAML 配置文件。旧的 YAML 配置文件可通过运行 `alacritty migrate` 转换为 TOML。然而，自动迁移会丢弃所有注释。 

Alacritty 默认不提供配置文件。配置选项可从[项目首页](<https://alacritty.org/config-alacritty.html>)中找到。如果启用了 `live_config_reload` 选项（默认启用），大部分设置将会在配置文件保存后立即生效。 

###  颜色

有关可用配色方案的列表，请参阅 [alacritty 主题仓库](<https://github.com/alacritty/alacritty-theme>)。如果您喜欢的配色方案在列表中，请将提供的代码粘贴到您的配置文件中。 

###  字体

如果不想使用系统默认字体，可以通过更改以下行来指定不同的字体： 
    
    [font]
    size = 12.0
    
    [font.bold]
    family = "monospace"
    style = "Bold"
    
    [font.bold_italic]
    family = "monospace"
    style = "Bold Italic"
    
    [font.italic]
    family = "monospace"
    style = "Italic"
    
    [font.normal]
    family = "monospace"
    style = "Regular"

将 `monospace` 替换为以下输出中的某个字体名称： 
    
    $ fc-list : family style
    
请注意，某些字体不提供 `Italic` 而提供 `Oblique` 样式。 

##  提示和技巧

###  在同一目录中生成新实例

将以下内容添加到配置文件中，之后，通过按下 `Ctrl+Shift+Enter` 使 _Alacritty_ 在当前工作目录中生成一个新的实例： 
    
    [keyboard]
    bindings = [
       { key = "Return", mods = "Control|Shift", action = "SpawnNewInstance" }
    ]
    
###  Vi 模式和复制粘贴

Vi 模式允许使用键盘在 Alacritty 的视口中移动和回滚。默认使用 `Ctrl+Shift+Space` 切换该模式。要复制内容，可使用鼠标选择并按 `Ctrl+Shift+c`，或进入 Vi 模式，用 `v` 开始选择，然后像在 vim 中那样用 `hjkl` 移动，最后按 `y` 复制选择的内容。要粘贴内容，可按 `Ctrl+Shift+v`。要从 X 剪切板中复制或是往其中粘贴内容，可使用鼠标选择进行复制，然后用鼠标中键进行粘贴。 

###  提示（Hints)

终端提示被用于在终端的可视部分寻找文本或超链接，并通过管道将其传至其他应用程序。默认情况下，Alacritty 通过快捷键 `Ctrl+Shift+O` 启用网址链接（URL）提示并使用 [xdg-open](<../zh-cn/Xdg-utils.html#xdg-open> "Xdg-open") 将其打开。参见 [Alacritty TOML 配置手册](<https://alacritty.org/config-alacritty.html>)的 `HINTS` 小节以获取细节信息。 

要使如 `_filename_.rs:_line_ :_character_` 的文件提示（例如 `my_crate/src/server.rs:181:49`）能够被鼠标点击并能使用 [Visual Studio Code](<../zh-cn/Visual_Studio_Code.html> "Visual Studio Code") 打开，可在 Alacritty 的 TOML 配置中添加以下小节： 
    
    alacritty.toml
    
    [[hints.enabled]]
    regex = "[^ ]+\\.rs:\\d+:\\d+"
    command = { program = "code", args = [ "--goto" ] }
    mouse = { enabled = true }
    
基于正则表达式的多种提示类型可通过添加多个 `[[hints.enabled]]` 小节实现。 

###  随时切换主题

要切换主题，例如通过 ssh 连接到一个服务器时，可以使用如下命令： 
    
    $ alacritty msg config "$(cat ~/path/to/theme.toml)"
    
##  故障排除

###  鼠标在 Vim 中无法正常工作

将 `set ttymouse=sgr` 和 `set mouse=a` 添加至 `.vimrc` 中，或换用 [Neovim](<../zh-cn/Neovim.html> "Neovim")。也可以参阅[这个议题](<https://github.com/alacritty/alacritty/issues/803>)。 

###  边框在 dwm 中变成透明

Alacritty 的边框在 [dwm](<../zh-cn/Dwm.html> "Dwm") 中变得透明。将如下那行添加到 [dwm](<../zh-cn/Dwm.html> "Dwm") 源代码目录的 `drw.c` 中并重新编译可修复此问题： 
    
    if (!XftColorAllocName(...))
        die("error, cannot allocate color '%s'", clrname); /* 找到这行代码 */
    **dest- >pixel |= 0xff << 24;**                            /* 添加这行代码 */
    
###  终端功能在远程 shell 中不可用

当使用 Alacritty 终端连接到远程系统（例如 [SSH](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH")）时，可能会发生此问题，系统的 terminfo 数据库中可能没有 Alacritty 的条目(`/usr/share/terminfo/a/alacritty*`)。 因此，所有交互式终端功能都不起作用。如 [termite#Terminal issues with SSH](</wzh/index.php?title=Termite&action=edit&redlink=1> "Termite（页面不存在）")（英语：[termite#Terminal issues with SSH](<https://wiki.archlinux.org/title/termite#Terminal_issues_with_SSH> "en:termite")） 中所述，将 Alacritty 的 terminfo 复制到远程服务器可解决该问题。 

在本地主机上，使用 Alacritty： 
    
    $ infocmp > alacritty.terminfo                # 导出 Alacritty 的 Terminfo
    $ scp alacritty.terminfo user@remote-host:~/  # 或者使用其他方法复制到远程主机上
    
在远程主机上，在与先前复制 `alacritty.terminfo` 文件的相同目录中： 
    
    $ tic -x alacritty.terminfo  # 为当前用户导入 Terminfo
    $ rm alacritty.terminfo      # 可选操作：删除 Terminfo
    
上述过程可简化为以下一行： 
    
    $ infocmp | ssh "$user@$host" 'tic -x /dev/stdin'
    
**注意：** 在此之后，您将需要启动一个新的 SSH 会话以使远程 shell 加载新的 Terminfo。

或者，可以将配置中的 `TERM` 设置为 `xterm-256color` 而不是默认的 `alacritty`： 
    
    [env]
    TERM = "xterm-256color"

###  Wayland GNOME 上没有标题栏

当使用 Wayland GNOME时，标题栏是空的并且有奇怪的图标。有关详细信息，请参阅 <https://github.com/alacritty/alacritty/issues/4739> 以获取详细信息。 

一种解决方案是设置一个空的 `WAYLAND_DISPLAY` [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")，使 Alacritty 以 [Xwayland](<../zh-cn/Wayland.html#Xwayland> "Xwayland") 启动，而不是原生 Wayland。 

###  多显示器上字体大小不同

默认情况下，Alacritty 会在每个显示器上尝试根据 `Device pixel ratio` 将字体缩放到合适的大小。在某些有多个显示屏的设置中，这会使字体的物理尺寸相差巨大，如 [[1]](<https://github.com/alacritty/alacritty/issues/3465>) 和 [[2]](<https://github.com/alacritty/alacritty/issues/1339>)。 

要查看每个监视器的现有设备像素比率值，请运行 `alacritty -v`，将子窗口移动到每个监视器，并注意父窗口中报告的 `Device pixel ratio`。 

使用环境变量 `WINIT_X11_SCALE_FACTOR` 强制设置一个固定的设备像素比应当足以解决字体大小不同的问题： 
    
    $ WINIT_X11_SCALE_FACTOR=1.66 alacritty
    
也可以在配置文件中设置 `WINIT_X11_SCALE_FACTOR` 的值： 
    
    [env]
    WINIT_X11_SCALE_FACTOR = "1.66"

###  无法恢复到先前用 pywal 设置的配色方案

可将以下代码添加至 shell 的执行命令（`.bashrc`）中： 
    
    if command -v wal > /dev/null 2>&1 && [ "$TERM" = "alacritty" ]; then
        wal -Rqe
    fi
    
这比简单地添加 `wal -R` 更好，因为： 

  1. 只需在终端模拟器窗口中执行此操作。
  2. `wal -R` 非常慢，并且不需要在每个子 shell 中执行。
  3. 使用了 `-q` 选项，不需要查看标准输出（StdOut）。
  4. 不需要让桌面的其他组件（例如 gtk、xrdb、polybar、i3）也重新加载颜色。这由 `-e` 标志完成。
