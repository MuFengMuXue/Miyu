**翻译状态：**

  * 本文（或部分内容）译自 [Feh](<https://wiki.archlinux.org/title/Feh> "arch:Feh")，最近一次同步于 2021-04-14，若英文版本有所[更改](<https://wiki.archlinux.org/title/Feh?diff=0&oldid=658581>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Feh_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Nitrogen](<../zh-cn/Nitrogen.html> "Nitrogen")
  * [sxiv](</wzh/index.php?title=Sxiv&action=edit&redlink=1> "Sxiv（页面不存在）")

[feh](<https://feh.finalrewind.org/>) 是一款轻巧而功能强大的图像查看器，也可用于管理缺少此类功能的独立窗口管理器的桌面壁纸。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [feh](<https://archlinux.org/packages/?name=feh>)包 软件包。 

##  用法

feh 是高度可配置的。 有关选项的完整列表，请运行 `feh --help` 或参见 [feh(1)](<https://man.archlinux.org/man/feh.1>) [手册页](<../zh-cn/Man_%E6%89%8B%E5%86%8C.html> "手册页")。 

###  浏览图像

要快速浏览特定目录中的图像，可以使用以下参数启动 feh： 
    
    $ feh -g 640x480 -d -S filename /path/to/directory
    
  * `-g` 标志强制图像显示为不大于640x480
  * `-d` 标志获取文件名
  * `-S filename` 标志按文件名对图像进行排序

这只是一个例子。如果您需要更大的灵活性，还有更多可用的选项。 

**提示：**`--start-at` 选项将让 feh 显示选定的图像，同时也允许以默认顺序浏览目录中的所有其他图像，即好像您已运行“feh *”并循环浏览到选定的图像。 例如，`feh --start-at ./foo.jpg .` 。 查看当前目录中以 `_foo_.jpg` 开头的所有图像。

如果您正在使用具有EXIF数据的现代相机浏览照片，则使用 `--auto-rotate` 选项自动旋转图像很有趣。这不会更改文件。 

###  设置壁纸

`feh` 可用于设置桌面壁纸，例如，对于没有此功能的[窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")（比如，[Openbox](<../zh-cn/Openbox.html> "Openbox")，[Fluxbox](<../zh-cn/Fluxbox.html> "Fluxbox") 和 [xmonad](<../zh-cn/Xmonad.html> "Xmonad"). 

以下命令是设置初始背景的示例： 
    
    $ feh --bg-scale /path/to/image.file
    
其他调整选项包括： 
    
    --bg-tile FILE
    --bg-center FILE
    --bg-max FILE
    --bg-fill FILE
    
要在下一个会话中恢复背景，请在启动文件中添加以下内容（例如 `~/.xinitrc`, `~/.config/openbox/autostart` 等）： 
    
    ~/.fehbg &
    
要更改背景图像，请编辑 `~/.fehbg` 文件，该文件是在运行上述 `feh --bg-scale /path/to/image.file` 命令之后创建的。 

可以通过传递 `--no-fehbg` 标志来显式禁用 `~/.fehbg` 的创建。 

要为不同的显示器设置不同的墙纸，应传递尽可能多的显示器可用的文件路径。例如，对于双显示器设置，它将是： 
    
    $ feh --bg-center path/to/file/for/first/monitor path/to/file/for/second/monitor
    
###  打开 SVG 图像
    
    $ feh --conversion-timeout 1 file.svg
    
请注意，这需要 [imagemagick](<https://archlinux.org/packages/?name=imagemagick>)包 软件包。 

###  随机背景图片

您可以使用 `--randomize` 选项和 `--bg-foo` 选项之一来设置随机壁纸，例如： 
    
    $ feh --bg-fill --randomize ~/.wallpaper/*
    
上面的命令告诉 feh 随机化 `~/.wallpaper/` 目录中的文件列表，并将所有可用桌面的背景设置为随机列表前面的图像（每个桌面一个唯一的图像）。如果将墙纸分为多个子文件夹，则也可以递归执行此操作： 
    
    $ feh --recursive --bg-fill --randomize ~/.wallpaper
    
要在每个会话中从 `~/.wallpaper` 设置不同的随机墙纸，请将以下内容添加到您的 `.xinitrc` 中： 
    
    $ feh --bg-max --randomize ~/.wallpaper/* &
    
在每个 xorg 会话上设置随机墙纸的另一种方法是按照如下编辑 `.fehbg`。 
    
    $HOME/.fehbg
    
    feh --bg-max --no-fehbg --randomize ~/.wallpaper/* 
    
**提示：** 要定期更改墙纸，请使用脚本（请参见 [while 循环](<https://mywiki.wooledge.org/BashGuide/TestsAndConditionals#Conditional_Loops_.28while.2C_until_and_for.29> "gregswiki:BashGuide/TestsAndConditionals")），[cron](<../zh-cn/Cron.html> "Cron") 作业或 [systemd 计时器](<../zh-cn/Systemd/%E5%AE%9A%E6%97%B6%E5%99%A8.html> "Systemd/Timers")以所需的间隔执行命令。
