相关文章

  * [Steam/疑难解答](<../zh-cn/Steam/%E7%96%91%E9%9A%BE%E8%A7%A3%E7%AD%94.html> "Steam/疑难解答")
  * [Steam/游戏疑难解答](<../zh-cn/Steam/%E6%B8%B8%E6%88%8F%E7%96%91%E9%9A%BE%E8%A7%A3%E7%AD%94.html> "Steam/游戏疑难解答")
  * [游戏](<../zh-cn/%E6%B8%B8%E6%88%8F.html> "游戏")
  * [游戏手柄](<../zh-cn/%E6%B8%B8%E6%88%8F%E6%89%8B%E6%9F%84.html> "游戏手柄")
  * [游戏列表](<../zh-cn/%E6%B8%B8%E6%88%8F%E5%88%97%E8%A1%A8.html> "游戏列表")
  * [Gamescope](<../zh-cn/Gamescope.html> "Gamescope")

**翻译状态：**

  * 本文（或部分内容）译自 [Steam](<https://wiki.archlinux.org/title/Steam> "arch:Steam")，最近一次同步于 2025-08-03，若英文版本有所[更改](<https://wiki.archlinux.org/title/Steam?diff=0&oldid=834284>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Steam_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Steam](<https://store.steampowered.com/about/>) 是 Valve 公司推出的著名游戏分发平台。 

**注意：** 对于 Linux 平台，Steam 只支持最新的 Ubuntu 或 Ubuntu 的长期支持版本[[1]](<https://help.steampowered.com/en/faqs/view/1114-3F74-0B8A-B784>)[[2]](<https://github.com/ValveSoftware/steam-for-linux>)。如果在 Arch Linux 上使用 Steam 遇到问题，请不要向 Valve 寻求支持。

##  安装

启用 [multilib](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "Multilib") 仓库并[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Help:Reading") [steam](<https://archlinux.org/packages/?name=steam>)包 软件包（推荐），也可以安装 [steam-native-runtime](<https://aur.archlinux.org/packages/steam-native-runtime/>)AUR 以使用由原生系统库驱动的 Steam（通过 `steam-native` 启动），参阅[/疑难解答#Steam runtime](<../zh-cn/Steam/%E7%96%91%E9%9A%BE%E8%A7%A3%E7%AD%94.html#Steam_runtime> "Steam/疑难解答")。 

**注意：** 第一次安装时可能需要选择 32 位 [Vulkan](<../zh-cn/Vulkan.html> "Vulkan") 驱动程序软件包。默认情况下，[pacman](<../zh-cn/Pacman.html> "Pacman") 会按字母顺序选择 [lib32-amdvlk](<https://aur.archlinux.org/packages/lib32-amdvlk/>)AUR，这可能会带来问题，例如：如果不小心为不同厂商的显卡安装了该驱动，会导致 Vulkan 无法使用；或者即使使用了 AMD 显卡，如果没有和 [amdvlk](<https://aur.archlinux.org/packages/amdvlk/>)AUR 一起安装，也可能出问题。请参考 [Vulkan#安装](<../zh-cn/Vulkan.html#%E5%AE%89%E8%A3%85> "Vulkan")来选择适合显卡的正确驱动。

在 Arch Linux 上运行 Steam 需要满足以下需求： 

  * 安装 32 位版本的 [OpenGL 图形驱动](<../zh-cn/Xorg.html#%E9%A9%B1%E5%8A%A8%E5%AE%89%E8%A3%85> "Xorg")。
  * 生成 [en_US.UTF-8](<../zh-cn/Locale.html#Generating_locales> "Locale") 语言环境，以避免非法指针错误。
  * 若您要将库文件夹或非 Steam 游戏添加到您的 Steam 库，请安装一个带有文件选择器的 [XDG Desktop Portal](<../zh-cn/XDG_Desktop_Portal.html> "XDG Desktop Portal") 后端。
  * 因其 GUI 大量使用了 Arial 字体，您需要做以下三者其一： 
    * 使用一个自由（免费，free）的替代品 [ttf-liberation](<https://archlinux.org/packages/?name=ttf-liberation>)包。
    * 按照[微软字体](<../zh-cn/%E5%BE%AE%E8%BD%AF%E5%AD%97%E4%BD%93.html> "微软字体")安装原字体。
    * 按照 [Steam/疑难解答#Text is corrupt or missing](<../zh-cn/Steam/%E7%96%91%E9%9A%BE%E8%A7%A3%E7%AD%94.html#Text_is_corrupt_or_missing> "Steam/疑难解答") 使用一个不同的字体。
  * 安装 [wqy-zenhei](<https://archlinux.org/packages/?name=wqy-zenhei>)包 以支持亚洲地区语言。
  * 若使用 [systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd") 管理网络，安装 [lib32-systemd](<https://archlinux.org/packages/?name=lib32-systemd>)包 才能让Steam连上自己的服务器。
  * 若将 [systemd-resolved](<../zh-cn/Systemd-resolved.html> "Systemd-resolved") 用于 DNS，请按照[这些步骤](<../zh-cn/Systemd-resolved.html#DNS> "Systemd-resolved")修复 `/etc/resolv.conf` 以让 Steam 解析主机名。
  * 若使用大屏幕模式（Steam Deck UI），可能需要 [NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager") 让某些与网络有关面板正常运行。
  * 必须调大 `vm.max_map_count` 以让某些游戏免于崩溃，参见[游戏#增大 vm.max_map_count](<../zh-cn/%E6%B8%B8%E6%88%8F.html#%E5%A2%9E%E5%A4%A7_vm.max_map_count> "游戏")。

### SteamCMD

安装 [steamcmd](<https://aur.archlinux.org/packages/steamcmd/>)AUR 以使用[命令行版本的 Steam](<https://developer.valvesoftware.com/wiki/SteamCMD>)。 

##  目录结构

Steam 的默认安装位置是 `~/.local/share/Steam`。如果 Steam 无法找到该目录，它会指导你重新安装或选择一个新的安装位置。这篇文章使用 `~/.steam/root` 符号链接来表示 Steam 的安装位置。 

###  库文件夹

每一个 Steam 应用都有一个独一无二的应用 ID，你可以通过 [Steam Store](<https://store.steampowered.com/>) 的页面路径或在 [SteamDB](<https://steamdb.info/>) 中来找到它。 

Steam 将游戏安装到 `_LIBRARY_ /steamapps/common/` 目录下。库文件夹 `_LIBRARY_` 一般会是 `~/.steam/root`，但是你依然可以选择拥有多个库文件夹如 (_Steam > Settings > Storage >(+)Add Drive_)。 

为了 Steam 能够正确识别游戏，它需要在 `_LIBRARY_ /steamapps/` 目录下找到 `appmanifest__AppId_.acf` 文件。此清单文件使用了 [KeyValues](<https://developer.valvesoftware.com/wiki/KeyValues>) 格式，并且它的 `installdir` 的内容决定了游戏的目录名称。 

**注意：** 为使从 flathub 安装的 Steam 能够添加另外的驱动器，用户必须授予 Steam 客户端访问该驱动器所在挂载点的权限，可以使用 [flatseal](<https://aur.archlinux.org/packages/flatseal/>)AUR 等工具。

##  用法
    
    steam [ -options ] [ steam:// URL ]
    
对于可用的命令行选择，详见 [Command Line Options article on the Valve Developer Wiki](<https://developer.valvesoftware.com/wiki/Command_Line_Options#Steam_.28Windows.29>)。 

Steam 也可以接受可选的 Steam URL，详见 [Steam browser procotol](<https://developer.valvesoftware.com/wiki/Steam_browser_protocol>)。 

##  启动选项

当你运行一个 Steam 游戏时，Steam 会使用 `/bin/sh` 执行它的**启动命令** 。 为了让你自由修改启动命令，Steam 提供了**启动选项** 。 **启动选项** 可以通过右键点击你的游戏库中的游戏，选择属性后点击**设置启动选项** 进行修改。 

默认情况下 Steam 只是简单的把你设置的参数字符串添加到游戏的启动命令后。想要设置环境变量或者将一个启动命令作为参数传递给另一个命令，你可以使用 `%command%` 以表示原启动命令。 

###  示例

  * 仅设置参数： `-foo`
  * 设置环境变量： `FOO=bar BAZ=bar %command% -baz`
  * 设置与默认完全不同的命令： `othercommand # %command%`

##  提示与技巧

###  最小化启动

在系统启动时，使 Steam 以最小化方式自启在系统托盘处是可以实现的，并且不会占据鼠标焦点。仅仅需要添加 `-silent` 到自启文件的参数列表中。 
    
    ~/.config/autostart/steam.desktop
    
    ...
    Exec=/usr/bin/steam -silent
    ...

###  小模式

Steam 支持一个最小化的替代 UI，仅仅包含您的游戏列表——隐藏了商店、社区和封面合集视图均被隐藏。可通过 _查看_ > _小模式_ 切换到该模式，通过 _查看_ > _大模式_ 回到标准模式。 

###  fsync 补丁

Valve 公司的 [fsync 补丁](<https://steamcommunity.com/app/221410/discussions/0/3158631000006906163/>)为使用Proton或Wine运行的大型应用改进了性能。此补丁自Linux内核5.16版本以来，已经合并到了 vanilla 内核，只需使用最新的 Proton 或修改版 Wine 构建即可。若想使用支持fsync的早期的内核版本： 

  * 安装 [linux-zen](<https://archlinux.org/packages/?name=linux-zen>)包 内核，其从 5.2 版本开始已包括 fsync 补丁。[[3]](<https://github.com/zen-kernel/zen-kernel/commit/f39367fdbc68e8b1e623239d13db6efaa5a67ae1>)
  * 安装 [linux-pf](<https://aur.archlinux.org/packages/linux-pf/>)AUR 或 [linux-pf-git](<https://aur.archlinux.org/packages/linux-pf-git/>)AUR 内核。

### Proton Steam-Play

Valve 公司开发了一个兼容性工具[Proton](<https://en.wikipedia.org/wiki/Proton_\(software\)> "w:Proton \(software\)")，用来使 Steam 可以在 Wine 和其他额外组件上运行。这使得你可以运行很多原本只能在 Windows 平台上运行的游戏（详见 [compatibility list](<https://www.protondb.com/>)）。 

此工具开源并且可以从 [GitHub](<https://github.com/ValveSoftware/Proton/>) 获得。Steam 将在 Steam Play 启用后安装它相适应的 Proton 版本。 

Proton 需要在 Steam 客户端启用： _Steam > 设置 > 兼容性_。你可以为了上述那些没有被 Valve 公司列入白名单的游戏启用 Steam Play。 

如果开发者激活，Proton 支持 _E_ asy _A_ nti _C_ heat 集成，但是 EAC 可能需要某个[特定修补版本](<https://github.com/ValveSoftware/Proton/issues/5214>)的 glibc：如果某个游戏据报告可以运行而在您的设备上却不行，请尝试使用 Steam Flatpak，因为其附带了修补的 glibc。另外，[设置 procfs 挂载选项 `hidepid` 为一个加固值](<../zh-cn/%E5%AE%89%E5%85%A8.html#hidepid> "Security")可能会导致 Easy Anti-Cheat 失败，并显示错误信息“Launch Error: 261”。 

####  强制使用 Proton

如果需要为某个游戏启用 Proton 或某特定版本的 Proton，右键该游戏，选择 _属性 > 兼容性 > 强制使用特定 Steam Play 兼容性工具_，选择需要的版本。这种做法也可以强制使一个具有 Linux 接口的游戏运行 Windows 版本。 

####  使用 Steam 外的 Proton

您可以[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [proton-cachyos](<https://aur.archlinux.org/packages/proton-cachyos/>)AUR，但是需要一些额外的配置才能在 Steam 上良好运行。想要了解 Steam 如何识别已安装的 Proton 的更多细节，请参阅 [Proton GitHub](<https://github.com/ValveSoftware/Proton?#install-proton-locally>)。 

**提示：** archlinuxcn 源包含一个 [proton](<https://github.com/archlinuxcn/repo/tree/master/archlinuxcn/proton>)[CNRepo](<../zh-cn/Arch_Linux_%E4%B8%AD%E6%96%87%E7%A4%BE%E5%8C%BA%E4%BB%93%E5%BA%93.html> "Arch Linux 中文社区仓库") 软件包，不同于 [proton-cachyos](<https://aur.archlinux.org/packages/proton-cachyos/>)AUR，您也可以[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")此软件包以节省时间。

### Steam Input

要启用控制器的 Steam Input 功能，请转到“Steam > 设置 > 控制器 > 外部手柄设置”。在这里，您会找到与您的控制器对应的“启用Steam Input”开关。 

#### Steam Input Configurator

[![](../File:Tango-go-next.png)](<../File:Tango-go-next.png>)**此页面或章节适合移动到[Steam Input Configurator](</wzh/index.php?title=Steam_Input_Configurator&action=edit&redlink=1> "Steam Input Configurator（页面不存在）")。**

**附注：** 没有理由在此处保留如此大的文本，它可以放在自己的文章中（在 [Talk:Steam](<../zh-cn/Talk:Steam.html>) 讨论）

详见[Steam Input Configurator](</wzh/index.php?title=Steam_Input_Configurator&action=edit&redlink=1> "Steam Input Configurator（页面不存在）")以获取配置器使用说明。 

当 SIC 为控制器启用时，会出现几个不同的控制器设备： 

  * 虚拟 Steam 控制器，用于支持 Steam Input API 的游戏。所有重映射和 Steam 特定功能均可用。 
    * 请勿与实体控制器 [Valve Steam Controller](<https://store.steampowered.com/app/353370/Steam_Controller/>) 混淆。
  * 表示模拟 Xbox 360 控制器的 evdev 设备，用于不支持 Steam Input 的游戏。基本重映射生效。
  * 原始控制器 evdev 设备，其输入通过 SIC 传递。重映射未生效，但游戏应默认使用 360 控制器。
  * 上述两个设备的操纵杆模拟设备。

SIC 的行为取决于上下文： 

  * 当启动支持 Steam Input API 的游戏时，SIC 使用原生模式。游戏接收“动作”而非原始输入。 
    * 这适用于在 Proton 中运行且会在 Windows 上使用 Steam Input 的游戏。
    * 理论上不需要，但模拟的 360 控制器仍然存在。
    * 游戏可选择同时支持 Steam Input 和传统输入 API 库（底层使用 evdev 和操纵杆）。当游戏通过 Steam 启动且为控制器启用 SIC 时，Steam Input 优先级更高。
    * 游戏也可选择仅支持 Steam Input。例如在《Among Us》中，除非运行 SIC，否则游戏手柄无法工作。
  * 当启动不支持 Steam Input 的游戏时，它（不知情地）在传统模式下使用 SIC。游戏接收来自看似 360 控制器的原始输入，但这些输入实际由 SIC 伪造以模拟原生模式的行为。 
    * 这适用于使用 evdev 或操纵杆的原生游戏，以及通过 Proton 运行的使用 DirectInput 或 XInput 的 Windows 游戏。
  * 当启动既不支持 Steam Input 也不支持其他游戏手柄 API 的游戏时，SIC 可激活配置文件以模拟游戏手柄支持。
  * 当 Big Picture 获得焦点时，当前 Big Picture 配置文件生效（不可配置）。
  * 当其他任何程序获得焦点时，当前桌面配置文件生效，可通过“Steam > 设置 > 控制器 > 桌面布局”配置。
  * 当任何程序获得焦点时，可通过“Steam > 设置 > 控制器 > 引导按钮和弦布局”配置额外的全局绑定（在 Steam Deck 上不可用）。

游戏根据其手柄支持程度进行评级（取决于控制器型号）： 

  * 支持您的控制器：表示游戏具有完整控制器支持。即使游戏不使用 Steam Input API 也可实现；重点在于无障碍性，无论 API 如何。
  * 大部分可用您的控制器：表示游戏具有部分手柄支持。即使游戏使用 Steam Input API，某些部分（如《军团要塞2》中）仍无法访问，导致此评级。
  * 不支持控制器：表示游戏没有原生手柄支持。
  * 未知控制器支持：表示 Valve 尚未验证该游戏的控制器支持。

当游戏没有完整手柄支持时，SIC 会尝试填补空白。例如在需要点击操作的《Bloons Tower Defense 5》中，Steam 会自动激活“键盘(WASD)和鼠标”配置文件，让您能用游戏手柄移动和点击。 

####  推荐 Steam Input 用法

使用总结： 

  * 启用“配置支持”建议用于增强手柄功能，如自定义重映射或自动修复（如任天堂式按钮重映射或键盘/鼠标）。
  * 对于某些游戏，如果它们不支持传统游戏手柄 API，则启用此功能是必需的。
  * 默认情况下，如果启用此功能，则控制器无法用于非 Steam 游戏，因为 360 控制器优先于原始控制器设备，但默认桌面配置禁用按钮。要修复此问题，您可以： 
    * 让配置更改动作集。某些官方桌面配置在按住开始按钮时会切换到游戏手柄模式。如果您的控制器配置无此功能，可添加新动作集，将其设为包含游戏手柄按钮，向开始按钮添加“额外命令”，设为“更改动作集”，并设置该额外命令在长按时激活。
    * 将桌面配置文件设为“游戏手柄”模板。这将传递输入到 360 控制器，使默认设备可用于其他程序。
    * 让其他程序使用原始设备（如果支持）。注意游戏将无法受益于 Steam Input 重映射。
    * 禁用整个功能，使 Steam 完全不创建 360 控制器。注意 Steam 游戏将无法受益于增强的手柄支持。
    * 使用其他游戏时关闭 Steam。

####  禁用 Steam Input

如果您希望完全禁用 Steam Input，请使用 -nojoy 参数启动 Steam，并单独为每个游戏禁用 Steam Input，因为不存在全局选项。 

### HiDPI

参见 [HiDPI#Steam](<../zh-cn/HiDPI.html#Steam> "HiDPI")。 

###  无窗口管理器的大屏幕模式

欲从[显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")以 [Gamescope](<../zh-cn/Gamescope.html> "Gamescope") 为[混成器](<../zh-cn/Wayland.html#%E6%B7%B7%E6%88%90%E5%99%A8> "Wayland")直接以大屏幕模式启动 Steam： 

  * [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [gamescope](<https://archlinux.org/packages/?name=gamescope>)包
  * 创建具有以下内容的[桌面项](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%A1%B9.html> "桌面项")：

    /usr/share/wayland-sessions/steam-big-picture.desktop
    
    [Desktop Entry]
    Name=Steam 大屏幕模式
    Comment=以大屏幕模式启动 Steam
    Exec=/usr/bin/gamescope -e -- /usr/bin/steam -tenfoot
    Type=Application

**注意：** 其中 `-tenfoot` 选项告诉 Steam 以大屏幕模式启动。

**警告：** “切换到桌面”菜单项会导致会话软锁。要返回显示管理器，需在终端运行 `steam -shutdown`。

###  Steam 皮肤

**注意：** 2023年6月发布了新的Steam UI。未针对此新UI更新的皮肤将无效。

使用皮肤可以自定义 Steam 界面。皮肤可以被位于 `~/.steam/root` 的界面定义文件所覆盖。 

想要安装一个皮肤： 

  1. 将皮肤的目录放于 `~/.steam/root/skins`。
  2. 按照 _Steam > 设置 > 界面_依次点击并选择该皮肤。
  3. 重启 Steam。

你可以在 [Steam 论坛](<https://web.archive.org/web/20170528214751/http://forums.steampowered.com/forums/showthread.php?t=1161035>)获得比较完备的皮肤列表。 

**注意：** 使用一个过期的皮肤可能会引起一些可视化错误。

####  自创皮肤

几乎所有的 Steam 风格会定义在 `~/.steam/root/resource/styles/steam.styles` (此文件超过 3,500 行)。对于一个可以被 Steam 识别的皮肤，它需要自己的 `resource/styles/steam.styles` 文件。 当一个 Steam 的更新改变了官方的 `steam.styles` 文件，你的皮肤可能会过期，会有造成可视化错误的潜在风险。 

详见 `~/.steam/root/skins/skins_readme.txt` 以获得如何创建皮肤的初步指引。 

###  改变 Steam 的通知位置

默认情况下 Steam 的通知会在屏幕底端右侧出现。 

你可以改变 Steam 通知出现的位置，通过更改 `Notifications.PanelPosition` 文件，具体位于 

  * `resource/styles/steam.styles` 以调整桌面通知
  * `resource/styles/gameoverlay.styles` 以调整游戏中通知

以上两个文件都将在 Steam 启动时被覆写，且 `steam.styles` 只会在启动时被读取。 

**注意：** 一些游戏并不遵守位于 `gameoverlay.styles` 里的设置。如《幽浮:未知敌人》。

####  使用一个皮肤

你可以创建一个皮肤去将通知位置改变成你想要的那样。比如你想要将位置设置成顶部右侧： 
    
    $ cd ~/.steam/root/skins
    $ mkdir -p Top-Right/resource
    $ cp -r ~/.steam/root/resource/styles Top-Right/resource
    $ sed -i '/Notifications.PanelPosition/ s/"[A-Za-z]*"/"TopRight"/' Top-Right/resource/styles/*
    
####  实时更新

`gameoverlay.styles` 文件可以在 Steam 运行时更改，这允许你对不同游戏设置不同的通知位置。 
    
    ~/.steam/notifpos.sh
    
    sed -i "/Notifications.PanelPosition/ s/\"[A-Za-z]*\"/\"$1\"/" ~/.steam/root/resource/styles/gameoverlay.styles
    
由此 [#启动选项](<#%E5%90%AF%E5%8A%A8%E9%80%89%E9%A1%B9>)应该像下面这样： 
    
    ~/.steam/notifpos.sh TopLeft && %command%
    
###  Steam 远程同乐

**注意：** Steam 家庭流媒体 [已更新为 Steam 远程同乐](<https://store.steampowered.com/news/51761/>)。

Steam 内置对于[远程同乐](<https://store.steampowered.com/streaming/>)的支持。 

前往 [Steam 社区指南](<https://steamcommunity.com/sharedfiles/filedetails/?id=680514371>)以了解如何在 Linux 上设置无头模式的流媒体服务。 

### Steam Controller

通常一个 Steam Controller 手柄需要使用 Steam 界面。不过在非 Steam 原生的 Linux 游戏中这种界面并不很实用。对此，当 Steam 客户端运行时，其会保持一个“桌面配置”。如果你有 Steam Controller 手柄，请在桌面配置中将其设置为通用 XBOX 控制器。只要 Steam 客户端在运行，你可以在其他游戏中使用 Steam Controller 手柄，例如 GOG 的游戏， 就像一个 XBOX 手柄。请确保在“常规手柄设置”已经选择了你的手柄类型。 

###  使用 Proton 时与 Windows 共用游戏

如果使用 Proton（Steam Play）启动游戏，并且由于某些原因仍然保留在Windows上安装的版本（例如某些游戏的反作弊系统有问题，或是要与Windows对比测试），那么可能会想把游戏存储在同一个分区里，而不是每个操作系统里分别保留一个游戏副本。关于如何配置，详见 <https://github.com/ValveSoftware/Proton/wiki/Using-a-NTFS-disk-with-Linux-and-Windows> 。 

若要在Steam的游戏库中添加其它文件夹，选择 Steam → 设置 → 下载 → STEAM 库文件夹，然后点击加号添加库文件夹。 

有三种文件系统支持被 Windows 和 Linux 读写。 

#### NTFS

更多信息参见 [Proton wiki](<https://github.com/ValveSoftware/Proton/wiki/Using-a-NTFS-disk-with-Linux-and-Windows>)。欲从 NTFS 文件系统启动游戏，请遵循 [Steam/疑难解答#位于 NTFS 分区的 Steam 存储库](<../zh-cn/Steam/%E7%96%91%E9%9A%BE%E8%A7%A3%E7%AD%94.html#%E4%BD%8D%E4%BA%8E_NTFS_%E5%88%86%E5%8C%BA%E7%9A%84_Steam_%E5%AD%98%E5%82%A8%E5%BA%93> "Steam/疑难解答"). 

使用 NTFS 的不足之处在于会经常发生着色器缓存文件夹损坏，报错信息为 `ntfs3: sdb6 ino=1921f, steamapprun_pipeline_cache Looks like your dir is corrupt.` 且无法在 Linux 下修复，需要在 Windows 下使用 `chkdsk` 修复。 

#### exFAT

该文件系统的缺点之一是不区分大小写。可能会出现类似的提示信息：`SteamLibrary has both 'SteamApps' and 'steamapps' directories. This will cause problems. Please fix manually and only keep 'steamapps'`。参见 [issue #7665](<https://github.com/ValveSoftware/steam-for-linux/issues/7665>)。 

此外，在 exFAT 上创建符号链接也存在问题，因此你无法像在 NTFS 方法中那样使用符号链接 compatdata 的方法。 

#### UDF

该文件系统可以几乎无痛使用。唯一要注意的是 Linux 目前不支持 UDF 2.50+ 版本的写入。可以使用 GParted 创建 UDF 文件系统，其会是 2.01 版本。 

###  加速着色器预编译

某些情况下着色器预编译可能仅使用一个核心，用户可以修改此类行为，例如改为 8 个核心： 
    
    ~/.steam/steam/steam_dev.cfg
    
    unShaderBackgroundProcessingThreads 8
    
###  Proton 以外的其它兼容层

除了 Proton/Wine，还有其他兼容工具可用： 

  * **Luxtorpeda** — 使用原生 Linux 引擎运行游戏。

     <https://luxtorpeda-dev.github.io/> || [luxtorpeda-git](<https://aur.archlinux.org/packages/luxtorpeda-git/>)AUR

  * **Boxtron** — 使用原生 Linux 的 DOSBox 运行 DOS 游戏。

     <https://github.com/dreamer/boxtron> || [boxtron](<https://aur.archlinux.org/packages/boxtron/>)AUR

也可以使用 [protonup-qt](<https://aur.archlinux.org/packages/protonup-qt/>)AUR 来管理这些工具： 

  1. 关闭 Steam
  2. [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [protonup-qt](<https://aur.archlinux.org/packages/protonup-qt/>)AUR
  3. 打开 protonup-qt 并安装你想要的兼容工具
  4. 启动 Steam
  5. 在游戏的“属性”窗口中，勾选“强制使用特定的 Steam Play 兼容工具”，然后选择你想要的工具。

###  使用独立显卡运行游戏

在使用[混合图形技术](<../zh-cn/%E6%B7%B7%E5%90%88%E5%9B%BE%E5%BD%A2%E6%8A%80%E6%9C%AF.html> "混合图形技术")的笔记本电脑上，Steam 默认使用集成显卡运行游戏，欲使用性能更为强劲的独立显卡运行游戏，请参阅 [PRIME#PRIME GPU 分载](<../zh-cn/PRIME.html#PRIME_GPU_%E5%88%86%E8%BD%BD> "PRIME")。 

### Flatpak

**注意：** 通过 Flatpak 从 Flathub 安装 Steam 可以修复客户端中遇到的许多问题，但从长远来看，可能需要使用记录较少的不同的故障排除方法。

可以通过 [Flatpak](<../zh-cn/Flatpak.html> "Flatpak") 从 [Flathub](<https://flathub.org/>) 安装 Steam，应用名为 `com.valvesoftware.Steam`。以下是为当前用户安装并运行的最简单方式： 
    
    $ flatpak --user remote-add --if-not-exists flathub <https://dl.flathub.org/repo/flathub.flatpakrepo>
    $ flatpak --user install flathub com.valvesoftware.Steam
    $ flatpak run com.valvesoftware.Steam
    
目前 Flatpak 版 Steam 不支持使用自定义主题。此外，也暂时无法通过 `optirun` 或 `primusrun` 运行游戏，详情参见 [Issue#869](<https://github.com/flatpak/flatpak/issues/869>)。 

通过 Flatpak 安装的 Steam 无法访问主目录，而强行覆盖此限制将导致 Steam 无法运行，因为这不安全。不过，可以自由添加主目录以外的其他目录。如果要添加一个外部游戏库，请运行以下命令添加目录权限： 
    
    $ flatpak override --user com.valvesoftware.Steam --filesystem=/path/to/directory
    
启动 Flatpak 版 Steam 时，可能会提示你安装 `steam-devices` 软件包。该软件包目前并不存在，但可以改为安装 [game-devices-udev](<https://aur.archlinux.org/packages/game-devices-udev/>)AUR，详见[游戏手柄#设备权限](<../zh-cn/%E6%B8%B8%E6%88%8F%E6%89%8B%E6%9F%84.html#%E8%AE%BE%E5%A4%87%E6%9D%83%E9%99%90> "游戏手柄")。 

####  Flatpak 的 CJK 字体问题

如果在游戏中遇到中日韩文字无法显示的问题，这可能是因为 `org.freedesktop.Platform` 默认不包含所需字体。首先尝试挂载本地字体目录： 
    
    $ flatpak run --filesystem=~/.local/share/fonts --filesystem=~/.config/fontconfig com.valvesoftware.Steam
    
如果无效，可以尝试直接将字体文件复制到 `org.freedesktop.Platform` 的目录中来使其可用，例如复制到： 
    
    /var/lib/flatpak/runtime/org.freedesktop.Platform/x86_64/_版本号_ /_哈希值_ /files/etc/fonts/conf.avail
    /var/lib/flatpak/runtime/org.freedesktop.Platform/x86_64/_版本号_ /_哈希值_ /files/etc/fonts/conf.d 
    /var/lib/flatpak/runtime/org.freedesktop.Platform/x86_64/_版本号_ /_哈希值_ /files/share/fonts
    
####  Flatpak 版 Steam 启动（run）问题

启动后，Steam 会尝试下载一些文件，并显示一个进度条。如果此时崩溃，你可以尝试为 Flatpak 软件包授予额外权限： 
    
    $ flatpak permission-set background background com.valvesoftware.Steam yes
    $ flatpak run com.valvesoftware.Steam
    
也可以安装 [flatseal](<https://flathub.org/apps/com.github.tchx84.Flatseal>) 工具控制其权限。 

###  降低显存占用的 Steam 设置

这对显存较小的显卡很有帮助。 

复制一份 Steam [桌面项](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%A1%B9.html> "桌面项")： 
    
    $ cp /usr/share/applications/steam.desktop ~/.local/share/applications/steam_minimal.desktop
    
修改新复制文件的 `Exec=` 和 `Name=` 行： 
    
    ~/.local/share/applications/steam_minimal.desktop
    
    Name=Steam Minimal
    Exec=/usr/bin/steam -cef-disable-gpu-compositing -cef-disable-gpu steam://open/minigameslist %U
    
当启动 `Steam Minimal` 时，您会看到一个索然无味的界面，不过已经足以安装和运行游戏。运行原先标准的 `Steam` 则会启动完整的 Steam 客户端。 

##  疑难解答

参见 [Steam/疑难解答](<../zh-cn/Steam/%E7%96%91%E9%9A%BE%E8%A7%A3%E7%AD%94.html> "Steam/疑难解答")。 

##  另见

  * [Gentoo:Steam](<https://wiki.gentoo.org/wiki/Steam> "gentoo:Steam")
  * PCGamingWiki 中的 [The Big List of DRM-Free Games on Steam](<https://pcgamingwiki.com/wiki/The_Big_List_of_DRM-Free_Games_on_Steam>)
  * Fandom 中的 [List of DRM-free games](<https://steam.fandom.com/wiki/List_of_DRM-free_games>)
  * Steam 中[支持 SteamOS + Linux 的作品](<https://store.steampowered.com/browse/linux>)
  * [Proton](<https://github.com/ValveSoftware/Proton/>)：支持 Steam Play 运行的基于 Wine 以及其他额外组件的兼容性工具
  * [ProtonDB](<https://www.protondb.com/>)：社区维护的 Linux 兼容性数据库
