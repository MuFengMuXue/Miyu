**翻译状态：**

  * 本文（或部分内容）译自 [Polybar](<https://wiki.archlinux.org/title/Polybar> "arch:Polybar")，最近一次同步于 2022-07-10，若英文版本有所[更改](<https://wiki.archlinux.org/title/Polybar?diff=0&oldid=737069>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Polybar_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[polybar](<https://github.com/jaagr/polybar>) 是一种能简单快速地创建状态栏的工具。它可以自定义许多功能模块，比如工作区、日期和音量等等。Polybar 对于一些没有状态栏或者状态栏的功能有限的[窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")格外有用，例如 [awesome](<../zh-cn/Awesome.html> "Awesome") 和 [i3](<../zh-cn/I3.html> "I3")。Polybar 也可以用于 [Plasma](<../zh-cn/KDE.html#Plasma_%E6%A1%8C%E9%9D%A2> "KDE") 这样的[桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [polybar](<https://archlinux.org/packages/?name=polybar>)包 包，或者安装它的开发版本 [polybar-git](<https://aur.archlinux.org/packages/polybar-git/>)AUR。 

##  配置

将配置文件样例 `/etc/polybar/config.ini` 复制到 `$XDG_CONFIG_HOME/polybar/config`。polybar 默认按 `~/.config/polybar/config.ini`、`/etc/xdg/polybar/config.ini` 和 `/ etc/polybar/config.ini` 的顺序查找文件，并将最先找到的作为配置文件。 

###  运行 Polybar

Polybar 可以使用以下参数运行： 
    
    Usage: polybar [OPTION]... [BAR]
    
      -h, --help                   显示帮助信息并退出
      -v, --version                显示构建详情并退出
      -l, --log=LEVEL              设置日志的详细级别（默认：notice）
                                   LEVEL 可以是：error, warning, notice, info, trace
      -q, --quiet                  保持安静，不显示日志（会覆盖 -l）
      -c, --config=FILE            配置文件的路径
      -r, --reload                 当配置文件被修改后自动重新加载
      -d, --dump=PARAM             输出参数 PARAM 的值并退出
      -m, --list-monitors          输出可用的显示器列表并退出（不含克隆的显示器）
      -M, --list-all-monitors      输出可用的显示器列表并退出（包含克隆的显示器）
      -w, --print-wmname           输出生成的 WM_NAME 并退出
      -s, --stdout                 将数据打印到标准输出，而不是在图形界面中展示
      -p, --png=FILE               运行3秒后将 png 截图保存到 FILE

你可能想要在你的窗口管理器的引导程序中启动 Polybar，详见[#在窗口管理器中运行](<#%E5%9C%A8%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8%E4%B8%AD%E8%BF%90%E8%A1%8C>)。 

###  配置样例

以下是一份基础的配置： 
    
    [bar/mybar]
    modules-right = date
    
    [module/date]
    type = internal/date
    date = %Y-%m-%d%

它定义了一个 bar `mybar` 并在其中加入了一个模块 `date`。 

Polybar 默认生成了一个包含很多配置好的模块的配置文件 `/usr/share/doc/polybar/config`。 

###  在窗口管理器中运行

创建一个包含启动逻辑的[executable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "Executable")，例如 `$HOME/.config/polybar/launch.sh`： 
    
    #!/bin/bash
    
    # 终止正在运行的 bar 实例
    killall -q polybar
    # 如果你所有的 bar 都启用了 ipc，你也可以使用
    # polybar-msg cmd quit
    
    # 运行 Polybar，使用默认的配置文件路径 ~/.config/polybar/config.ini
    polybar mybar 2>&1 | tee -a /tmp/polybar.log & disown
    
    echo "Polybar launched..."
    
这个脚本会在窗口管理器重启后重新运行 Polybar。 

#### bspwm

如果使用的是 [bspwm](<../zh-cn/Bspwm.html> "Bspwm")，将下面内容添加到 `bspwmrc`： 
    
    $HOME/.config/polybar/launch.sh
    
#### i3

如果使用的是[i3](<../zh-cn/I3.html> "I3")，将下面内容添加到你的 i3 的配置文件： 
    
    exec_always --no-startup-id $HOME/.config/polybar/launch.sh
    
##  参见

  * [Polybar Github Wiki](<https://github.com/jaagr/polybar/wiki/>)
