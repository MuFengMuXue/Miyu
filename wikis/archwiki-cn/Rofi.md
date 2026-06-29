**翻译状态：**

  * 本文（或部分内容）译自 [Rofi](<https://wiki.archlinux.org/title/Rofi> "arch:Rofi")，最近一次同步于 2024-09-05，若英文版本有所[更改](<https://wiki.archlinux.org/title/Rofi?diff=0&oldid=806664>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Rofi_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [List of applications/Other#Application launchers](<../zh-cn/List_of_applications/Other.html#Application_launchers> "List of applications/Other")

[Rofi](<https://github.com/DaveDavenport/rofi>) 是一个窗口切换器、运行对话框、ssh 启动器以及 [dmenu](<../zh-cn/Dmenu.html> "Dmenu") 的替代品，是 [simpleswitcher](<https://github.com/seanpringle/simpleswitcher>) 的复制，经 [Sean Pringle](<https://github.com/seanpringle>) 编写并在随后由 [Dave Davenport](<https://github.com/DaveDavenport>) 扩展。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [rofi](<https://archlinux.org/packages/?name=rofi>)包 软件包，rofi 需要在 [Xorg](<../zh-cn/Xorg.html> "Xorg") 显示服务下使用。 

主分支中对 [Wayland](<../zh-cn/Wayland.html> "Wayland") 支持的[合并](<https://github.com/davatorium/rofi/pull/1139>)已无限期停滞。若需 [Wayland](<../zh-cn/Wayland.html> "Wayland") 支持，安装 [wofi](<https://archlinux.org/packages/?name=wofi>)包 或 [rofi-wayland](<https://archlinux.org/packages/?name=rofi-wayland>)包 作为替代。注意，这些软件包需要一个支持 Layer Shell 协议的 Wayland 混成器。包括了基于 wlroots 的混成器，如 Sway，以及一些基于 Mir 的混成器（但如 Gnome 的混成器 mutter 不包括在内）。 

更多关于 rofi 的信息和用法，请参阅 [rofi(1)](<https://man.archlinux.org/man/rofi.1>) 手册页。 

##  配置

设置配置选项有如下方式： 

  * 本地配置。通常依赖于 XDG，位于 `~/.config/rofi/config.rasi` 内。
  * 命令行选项：

    $ rofi -combi-modi window,drun,ssh -theme solarized -font "hack 10" -show combi
    
也可在配置文件中列出： 
    
    configuration {
     modi: "window,drun,ssh,combi";
     font: "hack 10";
     combi-modi: "window,drun,ssh";
     }
    @theme "solarized"
    
运行 `rofi -dump-config` 以获取 `config.rasi` 可用选项的完整列表。也可执行 `rofi -dump-config > ~/.config/rofi/config.rasi` 将输出直接写入配置文件。 

**注意：**[i3](<../zh-cn/I3.html> "I3") 用户需注意， _i3_ 配置文件中的逗号会引起一些问题。要设置绑定按键启动 _rofi_ ，要么使用配置文件，要么将逗号替换为 `#`，例如：`rofi -combi-modi window#drun#ssh`。

###  图标

可以让图标与其对应条目一同显示。假设已安装 [papirus-icon-theme](<https://archlinux.org/packages/?name=papirus-icon-theme>)包，并使用 `-show-icons` 与定义图标主题的选项 `-icon-theme` 令 _rofi_ 显示图标，命令如下所示： 
    
    $ rofi -combi-modi window,drun,ssh -theme solarized -font "hack 10" -show combi -icon-theme "Papirus" -show-icons
    
##  自定义主题

使用如下命令预览并为 _rofi_ 应用主题： 
    
    $ rofi-theme-selector
    
[rofi-theme(5)](<https://man.archlinux.org/man/rofi-theme.5>) 手册页包含了大量使用一种类似 CSS 的自定义语言为 rofi 设置主题的介绍。该页面还包含了 rofi 所使用的布局系统的额外信息，如 rofi 主题所使用的准确语法和绝大多数的主题属性。Rofi 的主题系统很简单（默认的 [dmenu](<../zh-cn/Dmenu.html> "Dmenu") 主题为 30 行左右的 CSS）但足够灵活，可创建出多种可交互、类似小部件的组件和菜单，如 [rofi-advanced](<https://github.com/adi1090x/rofi>)。 

###  社区主题

`/usr/share/rofi/themes` 目录下存放着一些 Rofi 自带的官方主题，更多用户主题可于 [rofi 主题](<https://github.com/DaveDavenport/rofi-themes>)仓库中找到。 

如下所示，使用命令行加载一个官方主题，或是一个下载的 _.rasi_ 格式的用户主题（应置于 `~/.config/rofi/example.rasi` 内）： 
    
    $ rofi _options_ -theme example
    
也可写在 `configuration { }` 代码块外部： 
    
    @theme "example"
    
##  提示与技巧

###  Rofi 用作 dmenu 的替代品

被以 [dmenu](<../zh-cn/Dmenu.html> "Dmenu") 的形式调用时（通过符号链接）， _rofi_ 类似于 _dmenu_ 。通过脚本调用 _dmenu_ 的程序（如 [pass](<../zh-cn/Pass.html> "Pass") 的 _passmenu_ ）将使用 _rofi_ 而非 _dmenu_ 。`rofi` 在 _dmenu_ 模式下的具体行为请参阅 [rofi-dmenu(5)](<https://man.archlinux.org/man/rofi-dmenu.5>)。 

若要使 rofi 贴近 [dmenu](<../zh-cn/Dmenu.html> "Dmenu") 的外观，将 [rofi](<https://archlinux.org/packages/?name=rofi>)包 软件包默认的 `/usr/share/rofi/themes/dmenu.rasi` 文件复制到 rofi 的配置文件目录下（通常是 `~/.config/rofi`）并将 `@theme dmenu` 添加至 `config.rasi` 的末尾或将 `-theme dmenu` 选项附加至命令行命令以启用该主题。 

###  在 rofi 中执行 shell 命令

若要在 rofi 中直接运行 [shell](<../zh-cn/%E5%91%BD%E4%BB%A4%E8%A1%8C%E8%A7%A3%E9%87%8A%E5%99%A8.html> "Shell") 命令或用户脚本并查看输出内容，需确保： 

定义 `-run-shell-command '{terminal} -e _SHELL_ -ic "{cmd} && read"`，其中的 `_SHELL_` 是用户所使用的 shell（例如 bash、zsh）。之后可在输入框中输入命令并按下 `Shift+Enter` 执行。若无后续按键操作，终端将保持开启状态。 

以下是一个包含 _i3_ 所推荐的转义序列的使用示例： 
    
    bindsym $mod+d exec --no-startup-id rofi -show drun -run-shell-command '{terminal} -e zsh -ic "{cmd} && read"'
    
###  集成 Unicode 选择功能

安装 [rofimoji](<https://archlinux.org/packages/?name=rofimoji>)包 以令 _rofi_ 集成 Unicode emoji 与字符选择器的功能。参见[项目说明](<https://github.com/fdw/rofimoji#readme>)以了解[使用方式](<https://github.com/fdw/rofimoji#usage>)和[配置](<https://github.com/fdw/rofimoji#configuration>)。 

###  Emoji 选择菜单

安装 [rofi-emoji](<https://archlinux.org/packages/?name=rofi-emoji>)包 以令 _rofi_ 集成 emoji 选择器的功能。参见[项目说明](<https://github.com/Mange/rofi-emoji#readme>)以了解[使用方式](<https://github.com/Mange/rofi-emoji#usage>)。 

若遇 emoji 相关渲染问题（例如，渲染为方块），应考虑安装 [ttf-symbola](<https://aur.archlinux.org/packages/ttf-symbola/>)AUR、[noto-fonts-cjk](<https://archlinux.org/packages/?name=noto-fonts-cjk>)包 和[noto-fonts-emoji](<https://archlinux.org/packages/?name=noto-fonts-emoji>)包。 

###  Rofi 用作电源管理菜单

Rofi 可与 systemd 一同用于电源管理。[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [rofi-power-menu](<https://aur.archlinux.org/packages/rofi-power-menu/>)AUR。该 AUR 软件包默认会将 rofi-power-menu 脚本的路径添加至 $PATH，因此只需按如下方式使用： 
    
    $ rofi -show p -modi p:rofi-power-menu
    
若不打算使用 AUR 软件包而是将其手动复制到系统中，则需要为 rofi 指定可执行文件 _rofi-power-menu_ 的路径。例如，假设可执行文件位于 `$HOME/.rofi-power-menu`： 
    
    $ rofi -show p -modi p:$HOME/.rofi-power-menu
    
也可将可执行文件置于 PATH 中，使用时仅需要传递该文件的名称即可。 

若要显示默认的符号，需要安装 [ttf-nerd-fonts-symbols](<https://archlinux.org/packages/?name=ttf-nerd-fonts-symbols>)包。 

更多信息请参见项目仓库中的 [README](<https://github.com/jluttine/rofi-power-menu#readme>) 文件。 

###  Rofi 用作剪切板管理器

Rofi 可与 [Greenclip](</wzh/index.php?title=Greenclip&action=edit&redlink=1> "Greenclip（页面不存在）")（英语：[Greenclip](<https://wiki.archlinux.org/title/Greenclip> "en:Greenclip")） 集成并用作 X11 的剪切板管理器。安装 [rofi-greenclip](<https://aur.archlinux.org/packages/rofi-greenclip/>)AUR 软件包。 

###  Rofi 用作计算器

使用 [rofi-calc](<https://archlinux.org/packages/?name=rofi-calc>)包 软件包可将 rofi 用作计算器，用于自然语言输入、单位转换和货币转换。 
