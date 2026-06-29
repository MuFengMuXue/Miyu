**翻译状态：**

  * 本文（或部分内容）译自 [Qtile](<https://wiki.archlinux.org/title/Qtile> "arch:Qtile")，最近一次同步于 2024-05-16，若英文版本有所[更改](<https://wiki.archlinux.org/title/Qtile?diff=0&oldid=538757>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Qtile_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [平铺式窗口管理器比较](<../zh-cn/%E5%B9%B3%E9%93%BA%E5%BC%8F%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8%E6%AF%94%E8%BE%83.html> "平铺式窗口管理器比较")
  * [窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")

摘自 [Qtile web site](<http://qtile.org/>)： 

    _Qtile 是一个全功能、可轻易修改(骇)的平铺式窗口管理程序。 Qtile 简单、轻巧、扩展性高。 撰写自订的窗口堆叠模式、插件以及指令是轻而易举的事情。程序以及设定均是以[Python](<../zh-cn/Python.html> "Python") 写成，意味着：您可以使用语言所提供的所有能力及弹性来满足您对窗口管理的需求。_

##  安装

从下列软件包中选择一个进行[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")： 

  * [qtile](<https://archlinux.org/packages/?name=qtile>)包 最新正式版
  * [qtile-git](<https://aur.archlinux.org/packages/qtile-git/>)AUR 最新开发版

为了让 Qtile 作为一个 [Wayland](<../zh-cn/Wayland.html> "Wayland") 混成器运行，你将需要安装 [python-pywlroots](<https://archlinux.org/packages/?name=python-pywlroots>)包。 

##  启动

### Xorg

要让 qtile 作为一个 [X11](<../zh-cn/Xorg.html> "X11") 的窗口管理器启动, 可用 [xinit](<../zh-cn/Xinit.html> "Xinit") 执行 `qtile start` 来启动. 

### Wayland

Qtile 同时也可作为一个 [Wayland](<../zh-cn/Wayland.html> "Wayland") compositor 通过执行 `qtile start -b wayland` 来启动. 

关于 Qtile 的 wayland 端开发进度, 可以查看[这个讨论](<https://github.com/qtile/qtile/discussions/2409>). 

##  配置

**注意：** 这个章节只会介绍基本的配置模式，若需更详尽的配置讯息请参见 [官方文档](<http://docs.qtile.org/en/latest/>) 或者 [备选文档](<https://qtile.readthedocs.io/en/stable/>)。

根据[配置查询表](<http://docs.qtile.org/en/latest/manual/config/#configuration-lookup>)（或者[备选文档](<https://qtile.readthedocs.io/en/stable/>)），Qtile 会在路径 `~/.config/qtile/config.py` 提供一个默认的配置文件，它将会在用户没有进行自定义的情况下使用。 

默认配置设置了 `Super+Enter` 作为打开 _终端_ 的快捷键,（终端通过 [hardcoded list](<https://github.com/qtile/qtile/blob/e762cfeda7b65e80fd7c9a5896ac8832475035ab/libqtile/utils.py#L291>) 选择）, 快捷键 `Super+Ctrl+q` 可以退出 Qile. 

最新的配置文件可以在 git 仓库 [libqtile/resources/default_config.py](<https://github.com/qtile/qtile/blob/master/libqtile/resources/default_config.py>) 下载。 

一些更完整的配置文件示例可以在 [qtile-examples](<https://github.com/qtile/qtile-examples>) 仓库找到。 

整个 Qtile 的配置均是以[python](<../zh-cn/Python.html> "Python")写成：为了快速了解 Python 语言可以阅读[这个教程](<https://developers.google.com/edu/python/introduction>)。 

在重新启动 Qtile 之前，你可以用以下指令测试 config.py 文件是否有语法错误: 
    
    $ python -m py_compile ~/.config/qtile/config.py
    
若如果没有其他输出, 此设定文件应该便无重大问题. 

###  组(Groups)

在 Qtile, 工作区(workspaces or views) 被称为**组(Groups)** 。他们可透过下列方式定义： 
    
    from libqtile.config import Group, Match
    ...
    groups = [
        Group("term"),
        Group("irc"),
        Group("web", match=Match(title=["Firefox"])),    #表示标题含此关键字的程序均放置于此组别中
       ]
    ...
    
###  组规则(Group Rules)

下面的例子展示了如何根据属性，如 title 和 wm_class，实现自动移动应用到工作区。如果想在 X 上做到这一点，你可能需要用到 **xprop** 。 
    
    from libqtile.config import Group, Match
    ...
    def is_text_editor(window):
        result = "neovim" in (window.name or "").lower()
        return result
    
    def is_terminal(window):
        result = "kitty" in (window.name or "").lower() and not is_text_editor(window)
        return result
    ...
    groups = [
        Group(name=str(idx), **group)
        for idx, group in enumerate(
            [
                {
                    "label": "term",
                    # restrict layouts since tiling is handled by kitty
                    "layouts": [layout.Max()], 
                    "matches": [
                        Match(func=is_terminal),
                    ],
                },
                {
                    "label": "browser",
                    "matches": [
                        Match(role="browser"),
                    ],
                },
                {
                    "label": "music",
                    "matches": [
                        Match(title="YouTube Music"),
                    ],
                },
                {"label": "text editor", "matches": [Match(func=is_text_editor)]},
                {"label": "other"},
            ],
            start=1,
        )
    ]
    ...
    
###  按键组合(Keys)

你可以配置你的快捷键通过 **Key** 这个类。 底下是一个按键范例, 按下 `Alt+Shift+q` 来退出窗口管理器 
    
    from libqtile.config import Key
    from libqtile.command import lazy
    ...
    keys = [
        Key(
            ["mod1", "shift"], "q",
            lazy.shutdown())
       ]
    ...
    
可执行 [Xmodmap](<../zh-cn/Xmodmap.html> "Xmodmap") 来得知系统按键与 `modX` 之间的对应关系. 

###  声音控制(Sound)

你可以通过添加快捷键来方便地控制声音以及状态. 

将[用户添加进](<../zh-cn/Users_and_groups.html#Group_management> "Users and groups") **audio用户组** 并且使用 `alsamixer` 命令行界面, 该程序包含在 [alsa-utils](<https://archlinux.org/packages/?name=alsa-utils>)包 包内. 
    
    keys= [
        ...
        # Sound
        Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
        Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 1- unmute")),
        Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 1+ unmute"))
       ]
    
###  语言(Language)

你可以使用 [setxkbmap](<https://wiki.archlinux.org/title/Setxkbmap>) 来添加快捷键以便轻松切换不同语言的键盘布局： 
    
    keys= [
        ...
        # Language 
            Key([mod], "F1",
                lazy.spawn("setxkbmap us"), 
                desc= "Change to US layout"),
            Key([mod],"F2",
                lazy.spawn("setxkbmap gr"),
                desc= "Change to Greek layout"),
           ]
    
###  显示器(Screens)

为你的每一台显示器配置 **Screen** 类, 而 任务栏(bar) 则配置于 **Screen** 类中. 
    
    from libqtile.config import Screen
    from libqtile import bar, widget
    import os.path
    ...
    screens = [
        Screen(                       # 一部显示器
            wallpaper=os.path.join(os.path.expanduser("~"), "Photos/Wallpapers/arch_fill.png"),
            wallpaper_mode="fill",
            bottom=bar.Bar([          # 将任务栏(bar)放置于屏幕底部
                widget.GroupBox(),    # 插件，用于显示组的状态
                widget.WindowName()   # 插件，用于显示当前窗口名称
                ], 30))
       ]
    ...
    
####  任务栏和小部件(Bars and Widgets)

可以从[官方文档](<http://docs.qtile.org/en/latest/manual/ref/widgets.html>)（或者[备选文档](<https://qtile.readthedocs.io/en/stable/>)）里找到所有内置小部件的列表. 

若想新增一个小部件, 只需要像上面任务栏设定那样调用即可 (如 `WindowName` 插件). 例如, 要新增一个显示电池状态的小部件, 我们可使用 `Battery`: 
    
    from libqtile.config import Screen
    from libqtile import bar, widget
    ...
    screens = [
        Screen(top=bar.Bar([
            widget.GroupBox(),    # 插件，用于显示组的状态
            widget.Battery()      # 插件，用于显示电池状态
           ], 30))
       ]
    ...
    
###  把Polybar作为主任务栏(Using Polybar as the main bar)

为了用 [Polybar](<https://github.com/polybar/polybar>) 代替默认任务栏，你需要删除 **screen** 类的内容： 
    
    from libqtile.config import Screen
    from libqtile import bar, widget
    ...
    screens = [
        Screen()
    ]
    ...
    
为了通过 Qtile 重新启动 Polybar ,在[#Keys](<https://wiki.archlinux.org/title/Qtile#Keys>) 类的重启快捷键配置处添加通过 `spawn` 命令的 Polybar 启动代码： 
    
    ...
    keys = [
        Key([mod, "control"], "r", lazy.reload_config(), lazy.spawn("~/.config/polybar/launch.sh")),
    ]
    ...

###  启动

你可以使用**钩(hooks)** 来启动程序, 特别是 `startup`. 

`startup` 钩是用于 Qtile 初始化事件的钩, 能够在 Qtile 初始化的时连带启动其他的程序(一次性指令或程序). 

要查看所有可用的钩, 可参考[这个文档](<http://docs.qtile.org/en/latest/manual/ref/hooks.html>)

下面是 _只启动一次程序_ 的示例: 
    
    import os
    import subprocess
    from libqtile import hook
    
    @hook.subscribe.startup_once
    def autostart():
        home = os.path.expanduser('~')
        subprocess.Popen([home + '/.config/qtile/autostart.sh'])
    
##  调试

有时候会因为插件的参数没有完整, 或者设定之间有冲突情形发生, 模组未 import 等问题出现错误. 

需要检查出错位置，可以以如下方式启动一个虚拟的 Xorg 并进行测试: 
    
    echo "exec qtile start" > /tmp/.start_qtile; xinit /tmp/.start_qtile -- :2
    
Qtile 将会输出日志到 `~/.local/share/qtile/qtile.log` 里. 

##  参阅

  * [Qtile 官方网站](<http://qtile.org/>)
  * [官方文档](<http://docs.qtile.org/en/latest/>)
  * [平铺式窗口管理器比较](<../zh-cn/%E5%B9%B3%E9%93%BA%E5%BC%8F%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8%E6%AF%94%E8%BE%83.html> "平铺式窗口管理器比较")
  * [xinitrc](<../zh-cn/Xinit.html#xinitrc> "Xinitrc")
  * [tilenol](<https://github.com/tailhook/tilenol>) \- 受 Qtile 启发，以 Python3 写成的类似窗口管理程序
