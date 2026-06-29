相关文章

  * [Minecraft/Java 版服务端](<../zh-cn/Minecraft/Java_%E7%89%88%E6%9C%8D%E5%8A%A1%E7%AB%AF.html> "Minecraft/Java 版服务端")

**翻译状态：**

  * 本文（或部分内容）译自 [Minecraft](<https://wiki.archlinux.org/title/Minecraft> "arch:Minecraft")，最近一次同步于 2026-03-08，若英文版本有所[更改](<https://wiki.archlinux.org/title/Minecraft?diff=0&oldid=866591>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Minecraft_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Minecraft](<https://minecraft.net/>) 是一个关于破坏和放置方块的游戏。游戏一开始玩家的主要目的是搭建各种结构使自己免遭夜晚出没的怪物的攻击并生存下来，但随着游戏的进行，玩家们可以合作创造出一些不可思议的、富有想象力的事物。 

该游戏有两个版本，Minecraft Java版和基岩版。Java 版是游戏的原始版本，自 2009 年开始开发。该版本可以在 Mac、Windows 和 Linux 上游玩。基岩版原为便携版，但后来被移植到不同的平台上。它当前支持 Windows 10 和 11、移动设备、Amazon FireOS 和 FireTV、Android 和 iOS、Xbox One、Playstation 4、Nintendo Switch 和 Samsung Gear VR 设备。基岩版客户端没有 Linux 的官方支持，但是基岩版服务器软件是可用的。 

##  客户端

###  Java 版

####  安装

Minecraft 客户端可以通过 [minecraft-launcher](<https://aur.archlinux.org/packages/minecraft-launcher/>)AUR 包来安装。它提供了官方游戏启动器，一个用于启动它的脚本和一个特定的 `.desktop` 文件。该 AUR 包已被 Mojang 在官网上推荐。 

您也可以使用功能更强大的第三方启动器，参见下文的[#Minecraft 模组启动器](<#Minecraft_%E6%A8%A1%E7%BB%84%E5%90%AF%E5%8A%A8%E5%99%A8>)。 

####  客户端/局域网的防火墙配置

大部分 Minecraft 联机世界由专门的 Minecraft 服务器托管。若您想开服，请阅读下文的[#服务端](<#%E6%9C%8D%E5%8A%A1%E7%AB%AF>)部分。 

更简单的方法是允许其他人加入您当前的 Minecraft 游戏，您的 Minecraft 客户端允许其他玩家在您游戏时加入。您的客户端会自动将您的游戏在 4445 端口广播，它会监听其他玩家加入的 TCP 连接。该 TCP 端口会在您每次开始 Minecraft 游戏时随机产生。若您未设置防火墙，这是个很有效的方法。但如果您的防火墙阻止传入 TCP 连接，那么连接这个随机端口会很棘手。 

要允许您的客户端主持局域网游戏，您的[防火墙](<../zh-cn/Category:%E9%98%B2%E7%81%AB%E5%A2%99.html> "防火墙")需要允许以下端口： 

  * `4445` UDP 端口，用于广播您的游戏
  * 传入的随机 TCP 端口

**提示：** 当一个世界向局域网开放时，一条确认消息会通过 TCP 端口发送到游戏聊天。例如：`Local game hosted on port _port_number_`。

请参阅[[1]](<https://minecraft.wiki/w/Tutorials/Setting_up_a_LAN_world>)以获取更多信息。 

###  基岩版

您可使用 [mcpelauncher-ui](<https://aur.archlinux.org/packages/mcpelauncher-ui/>)AUR 来安装非官方的 Minecraft 基岩版客户端，这是 [mcpelauncher-linux](<https://aur.archlinux.org/packages/mcpelauncher-linux/>)AUR 的 UI。 

###  教育版

[Minecraft 教育版](<https://minecraft.wiki/w/Minecraft_Education>)是另一种不使用在线功能游玩 Minecraft 的方式，因为它主要基于 Minecraft for Windows 10 （即 win32 代码库）。 

您可以用 [Wine](<../zh-cn/Wine.html> "Wine") 和 [Proton](<../zh-cn/Steam.html#Proton_Steam-Play> "Proton") 手动安装并运行它。 

此外，Minecraft 教育版可以作为使用 [vkd3d](<https://archlinux.org/packages/?name=vkd3d>)包 在 Linux 上运行 Minecraft RTX 的方式（这是 Microsoft store 独有的 Minecraft Education x64 版本）。 

**注意：** 从 1.19.50 版本起，由于登录流程更改，Microsoft Authentication 不再在 [Wine](<../zh-cn/Wine.html> "Wine") 内的 Minecraft 教育版上工作。

##  服务端

###  Java 版

参阅 [Minecraft/Java 版服务端](<../zh-cn/Minecraft/Java_%E7%89%88%E6%9C%8D%E5%8A%A1%E7%AB%AF.html> "Minecraft/Java 版服务端")以获取更多有关开设 Java 版服务器的内容。 

###  基岩版

####  安装

您可以通过 [minecraft-bedrock-server](<https://aur.archlinux.org/packages/minecraft-bedrock-server/>)AUR 包安装基岩版 Minecraft 服务端。它提供了一个 [systemd](<../zh-cn/Systemd.html> "Systemd") 单元文件。该 AUR 包会创建一个单独的 `minecraft-bedrock` 用户。 

有两种方法启动服务端。使用 systemd [启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `minecraft-bedrock-server.service`，或者以 minecraft-bedrock 用户在 `/opt/minecraft-bedrock-server` 目录下运行以下命令： 
    
    $ LD_LIBRARY_PATH=. ./bedrock_server
    
####  配置

配置文件 `server.properties` 包含了服务器配置和额外的文档。最重要的是，`server-port` 用于确定 `UDP` 端口，该端口会监听传入的连接。默认的 IPv4 端口是 `19132`，IPv6 端口是 `19133`。IPv4 的 UDP 端口 `43351` 和 IPv6 的 UDP 端口 `51885` 被用于验证。 

##  Minecraft 模组启动器

您可以用许多不同的启动器启动 Minecraft，这些启动器通常包含一系列的模组和工具，可以增添乐趣和管理[模组](<https://zh.minecraft.wiki/w/%E5%8A%A0%E8%BD%BD%E5%99%A8Mod>)。 

  * **ATLauncher** — 由社区制作的多个不同的模组组成的 Minecraft 模组启动器。

     <https://atlauncher.com/> || [atlauncher](<https://aur.archlinux.org/packages/atlauncher/>)AUR

  * **Badlion Client** — 适用于所有现代版本的 Minecraft 的 PvP 整合包。

     <https://client.badlion.net> || [badlion-client](<https://aur.archlinux.org/packages/badlion-client/>)AUR

  * **CheatBreaker Client** — 适用于 Minecraft 1.7 & 1.8 的 FPS 增强包。

     <https://cheatbreaker.net/> || [cheatbreaker](<https://aur.archlinux.org/packages/cheatbreaker/>)AUR

  * **Console Minecraft Launcher** — 一个在命令行上运行的 Minecraft Java 版启动器

     <https://github.com/MrShieh-X/console-minecraft-launcher> || [cmcl](<https://aur.archlinux.org/packages/cmcl/>)AUR

  * **Feed The Beast** — 起源于 Minecraft 中的挑战地图，由大量科技模组构成并逐渐演变为一个模组启动器。

     <https://www.feed-the-beast.com/> || [ftba](<https://aur.archlinux.org/packages/ftba/>)AUR，[ftba-electron](<https://aur.archlinux.org/packages/ftba-electron/>)AUR，[feedthebeast-classic](<https://aur.archlinux.org/packages/feedthebeast-classic/>)AUR

  * **GDLauncher Carbon** — 用 Electron/React 编写的开源的 Minecraft 启动器。

     <https://gdlauncher.com> || [gdlauncher-carbon-bin](<https://aur.archlinux.org/packages/gdlauncher-carbon-bin/>)AUR

  * **Hello Minecraft Launcher** — 包含许多工具并开源的高级 Minecraft 启动器

     <https://hmcl.huangyuhui.net/> || [hmcl](<https://github.com/archlinuxcn/repo/tree/master/archlinuxcn/hmcl>)[CNRepo](<../zh-cn/Arch_Linux_%E4%B8%AD%E6%96%87%E7%A4%BE%E5%8C%BA%E4%BB%93%E5%BA%93.html> "Arch Linux 中文社区仓库")，[hmcl](<https://aur.archlinux.org/packages/hmcl/>)AUR

  * **Labymod Launcher** — 用于启动 LabyMod，一个包含大量实用特性的 Minecraft 客户端。

     <https://www.labymod.net/> || [labymodlauncher-appimage](<https://aur.archlinux.org/packages/labymodlauncher-appimage/>)AUR 和 [labymodlauncher](<https://aur.archlinux.org/packages/labymodlauncher/>)AUR

  * **LauncherX** — 功能强大、界面优美的下一代 Minecraft 启动器。

     <https://corona.studio/lx> || [launcherx-bin](<https://aur.archlinux.org/packages/launcherx-bin/>)AUR

  * **Lunar Client** — 适用于所有现代版本的 Minecraft 的 PvP 整合包。

     <https://lunarclient.com> || [lunar-client](<https://aur.archlinux.org/packages/lunar-client/>)AUR

  * **Modrinth Launcher** — Modrinth 官方的开源且轻量的启动器。

     <https://modrinth.com/> || [modrinth-app](<https://aur.archlinux.org/packages/modrinth-app/>)AUR

  * **MultiMC** — 用于管理可分离包关联的沙盒环境。

     <https://multimc.org/> || [multimc5](<https://aur.archlinux.org/packages/multimc5/>)AUR，[multimc-git](<https://aur.archlinux.org/packages/multimc-git/>)AUR

  * **PolyMC** — 具有模组管理等功能的高级用户启动器，最初为 MultiMC 的分支。

     <https://polymc.org/> || [polymc](<https://aur.archlinux.org/packages/polymc/>)AUR，[polymc-qt5](<https://aur.archlinux.org/packages/polymc-qt5/>)AUR

  * **portablemc** — 为开发者设计跨平台的命令行 Minecraft 启动器和 API。支持 Fabric，Forge，NeoForge 和 Quilt 等 mod 加载器。

     <https://github.com/mindstorm38/portablemc> || [portablemc](<https://aur.archlinux.org/packages/portablemc/>)AUR

  * **Prism Launcher** — 具有模组管理等功能的高级用户启动器。最初由 MultiMC 分支而来，现在是 PolyMC 的分支。

     <https://prismlauncher.org/> || [prismlauncher-git](<https://github.com/archlinuxcn/repo/tree/master/archlinuxcn/prismlauncher-git>)[CNRepo](<../zh-cn/Arch_Linux_%E4%B8%AD%E6%96%87%E7%A4%BE%E5%8C%BA%E4%BB%93%E5%BA%93.html> "Arch Linux 中文社区仓库")，[prismlauncher](<https://archlinux.org/packages/?name=prismlauncher>)包，[prismlauncher-qt5](<https://aur.archlinux.org/packages/prismlauncher-qt5/>)AUR

  * **SJMC Launcher** — 新一代开源跨平台 Minecraft 启动器。

     <https://github.com/UNIkeEN/SJMCL> || [sjmcl-bin](<https://aur.archlinux.org/packages/sjmcl-bin/>)AUR

  * **SKlauncher** — 支持皮肤和披风的免费 Minecraft 启动器。

     <https://skmedix.pl> || [sklauncher-bin](<https://aur.archlinux.org/packages/sklauncher-bin/>)AUR

  * **Technic Launcher** — 从流行程度排名发掘模组的模组安装程序。

     <https://www.technicpack.net/> || [minecraft-technic-launcher](<https://aur.archlinux.org/packages/minecraft-technic-launcher/>)AUR

##  其他程序和编辑器

有几个[程序和编辑器](<https://zh.minecraft.wiki/w/%E8%BE%85%E5%8A%A9%E7%A8%8B%E5%BA%8F%E4%B8%8E%E7%BC%96%E8%BE%91%E5%99%A8>)可以让您的 Minecraft 之旅更加轻松。其中最常见的是地图生成器。您可以使用它们加载一个 Minecraft 地图文件并将其渲染为 2D 图像，自上而下地为您呈现一个世界。 

  * **AMIDST** — [amidst](<https://aur.archlinux.org/packages/amidst/>)AUR 具有出色的 Minecraft 界面和数据/结构搜寻功能，可以帮助您在 Minecraft 世界中寻找建筑，生物群系和玩家，还可以绘制世界的生物群系、找出一个种子中有趣的地方、生成随机种子或从现有世界读取种子（在这种情况下，它可以显示这个世界的玩家）。该项目有很多分支，其中最引人注目的是 “Amidst Exporter” ([amidstexporter](<https://aur.archlinux.org/packages/amidstexporter/>)AUR) 它包含一个用于计算 1.8+ 世界的海底神殿位置的补丁。

     <https://github.com/toolbox4minecraft/amidst> || [amidst](<https://aur.archlinux.org/packages/amidst/>)AUR

  * **Mapcrafter** — 是一个用 C++ 编写的高性能 Minecraft 地图渲染器，它将世界渲染为具有 3D 等距透视的地图。您可以在任意浏览器中查看这些地图，因此可以轻松地在一台服务器上部署它们。Mapcrafter 用一个简单的配置文件来指定要渲染的世界、不同的渲染模式（如白天/黑夜/洞穴），也可以从不同角度渲染世界。

     <http://mapcrafter.org/>[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-22 ⓘ] || [mapcrafter-git](<https://aur.archlinux.org/packages/mapcrafter-git/>)AUR

  * **MCA Selector** — 为 Minecraft Java 版存档导出或删除所选区块/区域的外部工具。

     <https://github.com/Querz/mcaselector> || [mcaselector](<https://aur.archlinux.org/packages/mcaselector/>)AUR

  * **Minutor** — Minutor 是一个轻量级的 Minecraft 地图生成器。它提供一个简单的基于 GTK 的界面用于查看您的世界。它有多种渲染模式可供使用，并且可以自定义着色模式，还提供从 Z 轴分割的功能。

     <http://seancode.com/minutor/> || [minutor-git](<https://aur.archlinux.org/packages/minutor-git/>)AUR

##  提示和技巧

###  启用 HRTF 定向音频支持

修改以下文件并在游戏内“音乐和声音”设置内开启“定向音频”： 
    
    ~/.alsoftrc
    
    hrtf=true

##  疑难解答

###  Minecraft 客户端或服务器无法启动

这可能是 [Java](<../zh-cn/Java.html> "Java") 版本的问题。不同版本的 Minecraft 需要不同的 JRE 。 

Minecraft 版本 | 最低支持的 JRE 版本   
---|---  
< 1.17 | 8   
1.17 | 16   
<= 1.20.4 | 17   
<= 1.21.11 | 21   
26.1 | 25   
  
**注意：**

  * 客户端和服务器可以使用更高版本的 [Java](<../zh-cn/Java.html> "Java")，例如 [jre-openjdk](<https://archlinux.org/packages/?name=jre-openjdk>)包，但 Minecraft 游戏启动器(以及模组)可能只能使用 [Java](<../zh-cn/Java.html> "Java") 8。
  * 运行旧版本 Minecraft 时，建议使用其兼容的最低版本的 JRE。例如，1.20.1 兼容 JRE 17 和 21，但不兼容 24。

**提示：** 当安装了多个版本的 Java 时，可以使用 `archlinux-java` 进行切换。

###  Minecraft Forge 字体损坏

在语言菜单中启用强制使用 Unicode 字体。 

若您无法阅读菜单选项：在主菜单中，设置按钮位于左下角，语言选项是左侧倒数第二个，强制使用 Unicode 字体位于左侧底部。 

亦可通过主菜单左侧的小按钮进入语言选项。 

###  无法修改 pulseaudio 设置

如果你无法切换音频输出设备 (命令 `pacmd list-sink-inputs` 的输出中具有 `DONT_MOVE` 标记)那么以下 openalsoft 配置可能会有所帮助 
    
    ~/.alsoftrc
    
    [pulse]
    allow-moves=yes

###  PipeWire 上的音频卡顿/缺失或 Java 以 SIGFPE 崩溃

OpenAL 默认以 JACK 作为 Pipewire 的 PulseAudio 后端。若您不希望如此，可以让 OpenAL 使用 Pulse 作为替代: 
    
    ~/.alsoftrc
    
    drivers=pulse

若您不想让所有应用程序的使用该配置，可以仅为 Minecraft 设置环境变量 `ALSOFT_DRIVERS=pulse`。 

###  Minecraft 不在原生 Wayland 上运行

您可能会看到类似 `GLFW error 65548: Wayland: The platform does not support setting the window icon` 的错误。 

这是因为与 Minecraft 一同打包的版本的 GLFW 被默认设为 X 。若您不想使用 [Xwayland](<../zh-cn/Wayland.html#Xwayland> "Xwayland") ，您可以使用系统安装的 [glfw](<https://archlinux.org/packages/?name=glfw>)包 来解决这个问题： 

  * 对于基于 MultiMC 的启动器（例如 [prismlauncher](<https://archlinux.org/packages/?name=prismlauncher>)包），在设置中检查 _Workarounds > Native Settings > Use system GLFW_。
  * 对于其他启动器，在设置中将 `-Dorg.lwjgl.glfw.libname=/usr/lib/libglfw.so` 行添加到到 Java 命令。

**警告：** 官方不支持原生 Wayland ，Forge 和 NeoForge 可能会完全不启动。

**注意：**

  * 有 bug 报告称打开菜单时鼠标会被居中，导致体验不佳，您可安装 [glfw-wayland-minecraft-cursorfix](<https://aur.archlinux.org/packages/glfw-wayland-minecraft-cursorfix/>)AUR 来解决该问题。
  * Wayland 上的 Minecraft 可能无法使用输入法，若要使用输入法，建议使用 Xwayland。

**提示：** 您可使用 [VulkanMod](<https://modrinth.com/mod/vulkanmod>) 来加入对 Wayland 的支持。

###  旧版本上 2 和 6 与 Shift 一同按下时不起作用

这是 LWGLJ2 引发的一个问题，有几种方法可以修复它： 

  * 使用带有更新版本 LWGLJ 的客户端或打补丁
  * 换个键盘布局（例如 German）。
  * 用 mod 修复。在 1.8.9 Forge 上，您可以使用 [mckeyboardfix](<https://github.com/Leo3418/mckeyboardfix>)。

##  参见

  * [Minecraft 官方网站](<https://www.minecraft.net/>)
  * [Minecraft 社区](<https://www.minecraft.net/community>)
  * [Minecraft Wiki](<https://minecraft.wiki/>)
  * [中文 Minecraft Wiki](<https://zh.minecraft.wiki/>)
  * [Minecraft 客户端和服务器下载](<https://minecraft.net/download>)
  * [合成表](<https://www.minecraft.wiki/wiki/Crafting>)
  * [方块和物品数据值](<https://www.minecraft.wiki/wiki/Data_values>)
  * [Reddit Minecraft 社区](<https://www.reddit.com/r/minecraft>)
  * [Minecraft 皮肤](<https://www.minecraftskins.net>)
