**翻译状态：**

  * 本文（或部分内容）译自 [MangoHud](<https://wiki.archlinux.org/title/MangoHud> "arch:MangoHud")，最近一次同步于 2025-01-19，若英文版本有所[更改](<https://wiki.archlinux.org/title/MangoHud?diff=0&oldid=825443>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/MangoHud_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [GameMode](<../zh-cn/GameMode.html> "GameMode")

[MangoHud](<https://github.com/flightlessmango/MangoHud>) 是一个 [Vulkan](<../zh-cn/Vulkan.html> "Vulkan") 和 [OpenGL](<../zh-cn/OpenGL.html> "OpenGL") 的覆盖层，用于在应用程序内监控系统性能并记录[基准测试](<../zh-cn/%E5%9F%BA%E5%87%86%E6%B5%8B%E8%AF%95.html> "基准测试")指标。 

##  安装

安装 [mangohud](<https://archlinux.org/packages/?name=mangohud>)包 软件包。如果需要 32 位游戏支持，可以选择安装 [lib32-mangohud](<https://archlinux.org/packages/?name=lib32-mangohud>)包。 

##  配置

MangoHud 通过以下文件进行配置，读取顺序如下： 

`$XDG_CONFIG_HOME/MangoHud/MangoHud.conf` `$XDG_CONFIG_HOME/MangoHud/APPLICATION-NAME.conf`（区分大小写） `$XDG_CONFIG_HOME/MangoHud/wine-APPLICATION-NAME.conf`（用于 [Wine](<../zh-cn/Wine.html> "Wine") 应用程序，区分大小写，不带 `.exe` 扩展名） `./MangoHud.conf` `$MANGOHUD_CONFIGFILE`（通过[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")） 

**提示：** 可以在 [项目仓库](<https://raw.githubusercontent.com/flightlessmango/MangoHud/master/data/MangoHud.conf>) 找到一个带注释的示例配置文件。

###  配置的图形用户界面

可以从 [goverlay](<https://archlinux.org/packages/?name=goverlay>)包 安装配置 MangoHud 的图形用户界面。 

##  使用

###  键盘命令

  * `RShift+F12` – 切换覆盖层
  * `RShift+F11` – 更改覆盖层位置
  * `RShift+F10` – 切换预设
  * `LShift+F2` – 切换日志记录
  * `LShift+F4` – 重新加载配置

###  测试配置

验证程序是否正确设置： 
    
    $ mangohud glxgears
    $ mangohud vkcube
    
###  运行单个游戏

要使用 MangoHud 运行游戏，按以下方式启动它： 
    
    $ mangohud _游戏名称_
    
####  动态钩取

某些应用程序可能需要一种特殊的钩取方法，可以通过 `--dlsym` 参数或 `MANGOHUD_DLSYM` [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")指定： 
    
    $ mangohud --dlsym _游戏名称_
    
####  与 GameMode 一起使用

要同时使用 MangoHud 和 [GameMode](<../zh-cn/GameMode.html> "GameMode") 启动游戏，可以将两个命令链入一个命令，例如： 
    
    $ mangohud gamemoderun _游戏名称_
    
###  运行单个 Steam 游戏

要让 [Steam](<../zh-cn/Steam.html> "Steam") 启动带有 MangoHud 的游戏，右键点击库中的游戏，选择 _属性..._ ，然后在 _启动选项_ 文本框中输入： 
    
    mangohud %command%
    
###  带有 MangoHud 启动 Steam

为避免更改所有游戏的启动选项，可以直接用 MangoHud 启动 [Steam](<../zh-cn/Steam.html> "Steam")： 
    
    $ mangohud steam-runtime
    
MangoHud 将检测到 Steam，并会在启动游戏之前避免加载自身。 

###  为所有 Vulkan 游戏启用

要使 MangoHud 自动与所有 [Vulkan](<../zh-cn/Vulkan.html> "Vulkan") 游戏一起启动，可以设置以下[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")： 
    
    MANGOHUD=1
    