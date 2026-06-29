**翻译状态：**

  * 本文（或部分内容）译自 [Conky](<https://wiki.archlinux.org/title/Conky> "arch:Conky")，最近一次同步于 2019-01-23，若英文版本有所[更改](<https://wiki.archlinux.org/title/Conky?diff=0&oldid={{{3}}}>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Conky_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Conky/Tips_and_tricks](</wzh/index.php?title=Conky/Tips_and_tricks&action=edit&redlink=1> "Conky/Tips and tricks（页面不存在）")
  * [Lm_sensors](<../zh-cn/Lm_sensors.html> "Lm sensors")
  * [Hddtemp](<../zh-cn/Hddtemp.html> "Hddtemp")

Conky 是一个用于X窗口系统的系统监视软件。它可以运行在 GNU/Linux 和 FreeBSD 上，是一个基于 GPL 协议的自由软件。Conky 可以监控许多系统变量，包括 CPU、内存、交换分区、磁盘空间、温度、top、上传、下载、系统消息以及更多。它具有很高的可配置性，但配置有一些难于理解。Conky 是 torsmo 的一个分支。 

##  安装

  * [官方软件库](<../zh-cn/Official_repositories.html> "Official repositories")中已经包含了[conky](<https://archlinux.org/packages/?name=conky>)包，您可以通过[pacman](<../zh-cn/Pacman.html> "Pacman")来安装它。

除了[官方软件仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方软件仓库")上的 [conky](<https://archlinux.org/packages/?name=conky>)包 软件包, 在 [AUR](<../zh-cn/Arch_User_Repository.html> "Arch User Repository") 上还有很多关于conky的软件包。 

  * Conky基本包，没有X11依赖 [conky-cli](<https://aur.archlinux.org/packages/conky-cli/>)AUR
  * Lua支持： [conky-lua](<https://aur.archlinux.org/packages/conky-lua/>)AUR
  * Nvidia和Lua支持： [conky-lua-nv](<https://aur.archlinux.org/packages/conky-lua-nv/>)AUR

一些在conky变量上的建设需要安装额外的应用才能被使用，例如温度控制的 [Hddtemp](<../zh-cn/Hddtemp.html> "Hddtemp") 和音乐控制的 [MPD](<../zh-cn/MPD.html> "MPD")

你可以编辑`~/.conkyrc`文件来定制您的conky或是使用[homeproject-screenshot](<https://conky.sourceforge.net/screenshots.html>)等其他网站上的范例 

附加应用: 

  * **Conky Manager** — Conky小部件的主题管理器. 它提供开启、关闭选项, 浏览和编辑已经安装的Conky主题.

     <https://teejeetech.com/conky-manager/> || [conky-manager](<https://archlinux.org/packages/?name=conky-manager>)包

##  配置

  * 当您在编辑配置文件时,点击保存命令可立即看到conky界面的变化.您也没有必要重新登录您的X环境.所以您可以尽情尝试每一个设置，保存配置文件并查看conky界面的变化,然后修改不合适的地方.

  * 或者，您可以使用默认配置:

    $ conky -C > ~/.config/conky/conky.conf
    
当然最好还是使用位于当前用户下`~/.conkyrc`的配置文件. 就像其他的应用一样, conky会先查看当前用户下的`.conkyrc`文件.如果检测失败,那么它将使用位于`/etc/conky`的默认配置文件. 

如果您保存配置文件在本地,比如在保存在您的home目录中,您将不能查看任何的日志文件除非您更改一些配置. One of the nice features of conky is to pipe to your desktop some `/var/log/` files to read all kinds of log messages.这些文件只能在`root`身份下查看,然后您需要通过`sudo`来启动conky.用`root`身份来启动conky是不推荐的,所以您需要进行以下设置: 
    
    $ usermod -aG log username
    
将 `username` 加入 `log group`. 现在 `username` 便可以读取日志文件了，您将能够在桌面上使用conky来重定向日志文件。 

  * 如果conky并没有显现应有的效果 -- 比如 minimum_size -- 您需查看是否是因清空了 `/etc/conky/conky.conf`中的内容，或是因注释相关字段所造成。

###  双屏幕

当你使用双屏幕配置时, 你需要进行一些设置来将 _conky_ 放置到你想让它呆在桌面的某个位置. 

通过调整`gap_x`, 假设你设置的是1680x1050像素的分辨率，你希望窗口位于左侧显示器的中间顶部，你应使用 : 
    
    alignment = 'top_left',
    gap_X = 840,
    
`alignment` 的作用是显而易见的， `gap_X`是从屏幕左边框开始的距离（以像素为单位）。. 

`xinerama_head`是一个可替换的选项，下面将在第二个屏幕的右上角放置“conky”窗口: 
    
    alignment = 'top_right',
    xinerama_head = 2,
    
###  配置文件语法更改

从conky 1.10以来，配置文件都是用新的lua语法编写的，比如： 
    
     conky.config = {
       -- Comments start with a double dash
       bool_value = true,
       string_value = 'foo',
       int_value = 42,
     }
     conky.text = [[
     $variable
     ${evaluated variable}
     ]]
    
下面的一些示例可能仍然使用旧语法，例如： 
    
     bool_value yes
     string_value 'foo'
     int_value 42
    
通过Lua脚本可以从旧语法转换为新的Lua语法。 [here](<https://github.com/brndnmtthws/conky/blob/master/extras/convert.lua>). 

##  字体

要用conky显示unicode格式图片和emoji，你需要支持此功能的[font](<../zh-cn/%E5%AD%97%E4%BD%93.html#Emoji_and_symbols> "Fonts") 然后将conky配置为需显示的unicode字体. 例如: 
    
     ${font Symbola:size=48}☺${font}
    
###  符号字体

符号字体常用于更复杂的conky配置，其中一些流行的配置包括； 

  * [ttf-pizzadude-bullets](<https://aur.archlinux.org/packages/ttf-pizzadude-bullets/>)AUR \- PizzaDude Bullets font
  * [otf-font-awesome](<https://archlinux.org/packages/?name=otf-font-awesome>)包
  * [ttf-weather-icons](<https://aur.archlinux.org/packages/ttf-weather-icons/>)AUR \- Erik flowers weather icon font with 222 glyphs

##  自启动

Conky可以通过几种不同的方式自启动, 一如 "[Autostarting](<../zh-cn/%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8.html> "Autostarting")"所述. 请选择最适合您的窗口管理器/桌面环境的方式. 

Conky有一种配置，使它在后台分支运行。这可能对于某些自动启动设置有效。 

In `conky.conf`: 
    
    conky.config = {
        background = true,
    }
    
如果你使用图形桌面环境，并希望通过`conky.desktop` 自启动，请使用以下命令： 
    
    ~/.config/autostart/conky.desktop
    
    [Desktop Entry]
    Type=Application
    Name=conky
    Exec=conky --daemonize --pause=5
    StartupNotify=false
    Terminal=false

`pause=5`参数在“conky”启动时会延时5秒钟，以确保桌面有时间加载并启动。 

##  故障排除

这些是人们在conky发现的问题和他们的解决方案。 

###  Conky启动并且在屏幕上不显示任何内容

首先检查配置文件文本变量中的语法错误。然后再次检查你的用户是否有权运行配置文件中的每个命令，以及是否安装了所有需要的包。 

###  不最小化显示桌面

**Using Compiz:** 如果 'Show Desktop' 选项或键绑定与所有其他窗口一起和condy最小化, 启动compiz配置设置管理器，转到“General Options”并取消选中“Hide Skip Taskbar Windows”选项。. 

如果不使用compiz，请尝试编辑 `conky.conf` 并添加/更改如下: 
    
    own_window_type = 'override',
    
或者 
    
    own_window_type = 'desktop',
    
请参阅“conky”帮助文档了解具体差异。但是，后一个选项允许您使用调整大小键绑定（例如OpenBox）将窗口捕捉到“conky”的边界，而第一个选项则没有。 

###  在GNOME Shell集成

有人在[GNOME](<../zh-cn/GNOME.html> "GNOME")内的 _conky_ 经历了错误. 

在 `conky.conf`添加: 
    
    own_window = true,
    own_window_type = 'desktop',
    
###  避免闪烁

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** Explain the steps to follow if there is no dbe module, probably in [xorg](<../zh-cn/Xorg.html> "Xorg") rather than here with a link (在 [Talk:Conky](<../zh-cn/Talk:Conky.html>) 中讨论)

_Conky_ 需要X服务内的双重缓冲扩展名 _(DBE)_ 支持来避免闪烁，因为没有它，窗口就无法足够快速的更新窗口. 可以通过 在 `/etc/X11/xorg.conf` 里的 [Xorg](<../zh-cn/Xorg.html> "Xorg")通过在`"Module"`中添加`Load "dbe"` 选项来启动. `xorg.conf` 文件已经被包含特定配置文件的`/etc/X11/xorg.conf.d` 所替代(1.8.x 版本以上)。只要 _DBE_ 存在于`/usr/lib/xorg/modules`它就会被自动加载. 加载模块列表可以使用 `grep LoadModule /var/log/Xorg.0.log`查看. 

要启用双重缓冲，请将`double_buffer`选项加入`conky.conf`: 
    
     conky.config = {
         double_buffer = true,
     }
    
##  你还可以看

  * [官方网站](<https://github.com/brndnmtthws/conky>)
  * [官方配置的Conky变量](<https://conky.sourceforge.net/config_settings.html>)
  * [官方Conky对象](<https://conky.sourceforge.net/variables.html>)
  * [Arch论坛中的Conky配置](<https://bbs.archlinux.org/viewtopic.php?id=39906>)
  * [常见问题](<https://github.com/brndnmtthws/conky/wiki/FAQ>)
