相关文章

  * [MangoHud](<../zh-cn/MangoHud.html> "MangoHud")

**翻译状态：**

  * 本文（或部分内容）译自 [GameMode](<https://wiki.archlinux.org/title/GameMode> "arch:GameMode")，最近一次同步于 2025-1-19，若英文版本有所[更改](<https://wiki.archlinux.org/title/GameMode?diff=0&oldid=821558>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/GameMode_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[GameMode](<https://github.com/FeralInteractive/gamemode>) 是一个 Linux 下的守护进程和库组合，允许游戏请求一组优化暂时应用于主机操作系统和/或游戏进程。 

##  安装

安装 [gamemode](<https://archlinux.org/packages/?name=gamemode>)包 和 [lib32-gamemode](<https://archlinux.org/packages/?name=lib32-gamemode>)包。 

将自己添加到 `gamemode` [用户组](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E7%94%A8%E6%88%B7%E7%BB%84%E7%AE%A1%E7%90%86> "用户组")。如果没有这个用户组，GameMode 用户守护进程将没有权限更改 CPU 管理器或进程的优先级。 

##  配置

GameMode 通过以下文件进行配置，这些文件按以下顺序读取并合并： 

`/etc/gamemode.ini` 用于系统范围的配置； `$XDG_CONFIG_HOME/gamemode.ini` 用于用户本地配置； `./gamemode.ini` 用于目录本地配置。 

**提示：** 可以在 [FeralInteractive 的 GitHub](<https://github.com/FeralInteractive/gamemode/blob/master/example/gamemode.ini>) 找到带注释的示例配置文件。

**注意：**`/usr/share/gamemode/gamemode.ini` 不应由用户创建，因为它保留给包维护者进行手动配置。有关更多详细信息，请参见 [file-hierarchy(7)](<https://man.archlinux.org/man/file-hierarchy.7>)。

###  改变优先级

GameMode 可以选择性地调整游戏进程的优先级（参见 [renice(1)](<https://man.archlinux.org/man/renice.1>)），可以超出常规用户的下限 `0`。 

这由以下配置选项控制： 
    
    [general]
    renice=0

与使用 `renice` 命令改变进程优先级不同，GameMode 使用正值并在应用到进程之前取其负值，也就是说，值为 `10` 将把游戏进程的优先级改为 `-10`。 

###  超频

GameMode 可以选择性地在运行时超频你的 GPU，但需要用户的特殊配置。 

无论使用什么 GPU，必须适当设置 `apply_gpu_optimizations` 和 `gpu_device` 配置选项。 

#### AMD

要改变 AMD GPU 的性能级别，必须手动启用[超频](<../zh-cn/AMDGPU.html#%E8%B6%85%E9%A2%91> "AMDGPU")，并设置 `amd_performance_level` 配置选项。 

#### NVIDIA

要改变 NVIDIA GPU 的性能级别，必须手动启用[超频](</wzh/index.php?title=NVIDIA/Tips_and_tricks&action=edit&redlink=1> "NVIDIA/Tips and tricks（页面不存在）")，并设置 `nv_powermizer_mode`、`nv_core_clock_mhz_offset` 和 `nv_mem_clock_mhz_offset` 配置选项。 

##  使用

###  测试配置

验证配置文件中的设置是否有效： 
    
    $ gamemoded -t
    
###  运行单个游戏

要运行一个游戏并使用 GameMode，启动方式如下： 
    
    $ gamemoderun ./game
    
####  与 MangoHud 一起使用

参见 [MangoHud#与 GameMode 一起使用](<../zh-cn/MangoHud.html#%E4%B8%8E_GameMode_%E4%B8%80%E8%B5%B7%E4%BD%BF%E7%94%A8> "MangoHud")。 

###  验证 GameMode 是否在运行

当你启动游戏时，可以使用以下命令验证 GameMode 是否运行： 
    
    $ gamemoded -s
    
**注意：**`gamemoded.service` 用户单元是按需通过 [dbus](<../zh-cn/D-Bus.html> "Dbus") 启动的 [[1]](<https://github.com/FeralInteractive/gamemode/pull/62>)。

###  运行单个 Steam 游戏

要使 [Steam](<../zh-cn/Steam.html> "Steam") 启动带有 GameMode 的游戏，右键单击库中的游戏，选择 _属性..._ ，然后在 _启动选项_ 文本框中输入： 
    
    gamemoderun %command%
    
###  使用 GameMode 启动 Steam

为了避免为所有 Steam 游戏都更改启动选项，可以直接使用 GameMode 启动 [Steam](<../zh-cn/Steam.html> "Steam")： 
    
    $ gamemoderun steam-runtime
    
这种方法的缺点是 GameMode 将在 Steam 进程打开的整个时间内运行，而不仅仅是在游戏启动时。 

##  故障排除

###  当设置为小于 -10 时 renicing 失败

默认情况下，GameMode 提供 [PAM](<../zh-cn/PAM.html> "PAM") 限制，允许将调度优先级更改为最大 -10。如果配置文件中的 `renice` 设置为不受支持的值，则进程的 renicing 将完全失败。 

您可以调整请求的值，或通过编辑 `/etc/security/limits.d/10-gamemode.conf` 来调整 GameMode 可设置的最大调度优先级。下面的示例将 -19 配置为 GameMode 可设置的最大调度优先级： 
    
    /etc/security/limits.d/10-gamemode.conf
    
    @gamemode - nice -19
