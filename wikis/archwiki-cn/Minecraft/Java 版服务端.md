**翻译状态：**

  * 本文（或部分内容）译自 [Minecraft/Java Edition server](<https://wiki.archlinux.org/title/Minecraft/Java_Edition_server> "arch:Minecraft/Java Edition server")，最近一次同步于 2025-03-17，若英文版本有所[更改](<https://wiki.archlinux.org/title/Minecraft/Java_Edition_server?diff=0&oldid=828102>)，则您可以帮助同步与[翻译](<../../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Minecraft_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)/Java_Edition_server_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

Minecraft 是一个[多人游戏](<https://en.wikipedia.org/wiki/Multiplayer_video_game> "w:Multiplayer video game")。它使用[客户端-服务端模型](<https://en.wikipedia.org/wiki/Client-server_model> "w:Client-server model")，游戏本体是一个可以独立游玩的客户端，连接到服务器时也可以和其他玩家一起游玩。 

**注意：** 第三方可以运行 Minecraft 服务端。您应当阅读它们的隐私政策来知晓它们如何处理您的数据。一些服务器需要登录第三方账户，还有一些支持通过小额交易购买物品。即使这可能违反了 [Minecraft 最终用户许可协议 (“EULA”)](<https://www.minecraft.net/zh-hans/eula>)，具体取决于服务器销售的内容。

##  安装

Java 版 Minecraft 服务端可通过 [minecraft-server](<https://aur.archlinux.org/packages/minecraft-server/>)AUR 包来安装。它附带一个 [systemd](<../../zh-cn/Systemd.html> "Systemd") 单元文件和一个小巧的控制脚本。 

请参阅[#可用于替代的服务端](<#%E5%8F%AF%E7%94%A8%E4%BA%8E%E6%9B%BF%E4%BB%A3%E7%9A%84%E6%9C%8D%E5%8A%A1%E7%AB%AF>)来了解一些可替代 Minecraft 服务端的应用的简介。 

##  配置

安装过程会创建 `minecraft` 用户和用户组。出于安全原因，我们推荐创建一个特殊的 minecraft 用户。在一个无特权用户下运行 Minecraft 可以使任何攻破您的服务器的人仅获得该用户的权限，而您自己的则完好无损。 不过，您需要安全地将您的用户添加到 `minecraft` 组，并授予该组 `/srv/minecraft`（默认）目录的写权限以修改 Minecraft 服务端配置。确保`/srv/minecraft` 目录下的所有文件均属于 `minecraft` 用户，或者让其他用户拥有这些文件的读写权。如果服务端无法访问某些文件且没有足够的权限将错误消息写入日志，那么它会出错。 

这个软件包提供了一个 systemd 服务和一个计时器来自动备份。默认情况下，备份位于服务器根目录的 `backup` 文件夹下。为节省磁盘空间，服务端只会保留 10 个最新的备份（可通过 `KEEP_BACKUPS` 进行配置）。相关的 systemd 文件是 `minecraftd-backup.timer` 和 `minecraftd-backup.service`。您可凭喜好[编辑](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Edit")它们，例如遵循自定义的备份周期。 

###  启动服务端

您可以通过 systemd 或命令行来启动服务端。无论使用哪种方式，服务端都被封装在 `minecraft` 用户的 [tmux](<../../zh-cn/Tmux.html> "Tmux") 会话中。使用 systemd，你可以[启动/启用](<../../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用")其包含的 `minecraftd.service`。此外，也可以执行： 
    
    # minecraftd start
    
###  接受 EULA

要运行 Minecraft 服务端，您必须接受 EULA（End User License Agreement，最终用户许可协议），您只需在安装后接受即可。[EULA](<https://en.wikipedia.org/wiki/EULA> "wikipedia:EULA") 文件由服务端软件包创建，位于 `/srv/minecraft/eula.txt`。请编辑该文件来声明您接受 EULA。您只需编辑： 
    
    eula=false
    
将其值改为 `true`。以下是一份被接受的 EULA 的样例： 
    
    /srv/minecraft/eula.txt
    
    #By changing the setting below to TRUE you are indicating your agreement to our EULA (<https://account.mojang.com/documents/minecraft_eula>).
    #Sat Sep 11 11:11:11 PDT 2011
    eula=true

###  防火墙配置

`server.properties` 包含三个设置用于确定您使用的端口： 

`server-port` 用于确定监听传入连接所使用的 `TCP` 端口，默认为 `25565`。 

`query.port` 用于确定共享游戏信息所使用的 `UDP` 端口，默认为 `25565`。 

**注意：** 要注意 `server.port` 是 TCP 而 `query.port` 是 UDP，它们可以共用同一端口。要启用 query，您还需要单独设置 `enable-query=true`。

`rcon.port` 用于确定远程连接管理终端所使用的 TCP 端口， 前提是您需要允许远程连接，默认端口为 `25575`。要启用 rcon，您需要单独设置 `enable-rcon=true` 和 `rcon.password=...`。 

您至少应当开启 `server-port` 以允许传入连接，建议允许 query 并开启 `query.port`。此外，允许远程控制会带来风险，开启前请三思。 

以上是官方服务端的配置方法。若您使用其他替代的服务端，请阅读它们的文档以获取更多细节及配置方法。 

参阅 [[1]](<https://minecraft.wiki/Tutorials/Setting_up_a_server>) 和 [[2]](<https://minecraft.wiki/Server.properties>) 以获取更多信息。 

###  服务端管理脚本

您可以使用软件包提供的 `minecraftd` 脚本来容易地管理服务端。它可以执行一些简单的诸如 `start`、`stop`、`restart` 的基本命令或使用 `console` 连接到会话。更进一步地，您可以使用 `status` 查看状态信息，用 `backup` 备份服务端的世界目录，用 `restore` 从备份恢复您的世界或使用 `command _要执行的命令_` 在服务器控制台上运行单条命令。 

**注意：** 关于服务器控制台（可通过 `minecraftd console` 访问），请知晓您可以使用 `ctrl+b` `d` 快捷键退出任意 [tmux](<../../zh-cn/Tmux.html> "Tmux") 会话。

###  调整

要调整默认设置（如最大 RAM、线程数等），请修改 `/etc/conf.d/minecraft`。 

例如，更多的高级用户可能会想将 `IDLE_SERVER` 设为 `true`，这会使服务端在 `IDLE_IF_TIME` 定义的时长（默认为 20 分钟）内没有玩家后暂停。当服务端被暂停时，一个 `idle_server` 会使用来自 [nmap](<https://archlinux.org/packages/?name=nmap>)包 的 [ncat(1)](<https://man.archlinux.org/man/ncat.1>)（或其他 [netcat](</wzh/index.php?title=Netcat&action=edit&redlink=1> "Netcat（页面不存在）") 实现）监听 Minecraft 端口，当有连接传入时，会立即启动服务端。这可能会推迟暂停后的第一个连入请求，但它可以显著降低 CPU 和内存占用，实现更合理的资源及功耗水平。 

**注意：** 如果在第一次运行时启用该选项，`/srv/minecraft/eula.txt` 将不会被创建，初次启动时您需要禁用它。

##  可用于替代的服务端

###  Spigot（区别于Craftbukkit）

[Spigot（水龙头服）](<https://www.spigotmc.org/>)是世界上使用最广泛的修改版服务端。您可使用 [spigot](<https://aur.archlinux.org/packages/spigot/>)AUR 安装它。spigot 的 PKGBUILD 在 [minecraft-server](<https://aur.archlinux.org/packages/minecraft-server/>)AUR 上构建，这意味着它具有自己的 systemd 单元文件、spigot 脚本和相应的脚本配置文件。其二进制文件名为 `spigot`，与 `minecraftd` 的命令相同。配置文件位于 `/etc/conf.d/spigot`。 

确保您已阅读[#配置](<#%E9%85%8D%E7%BD%AE>)章节，并无论何处都将所有的 `minecraftd` 替换为 `spigot` 。 

它与 [Bukkit（水桶服）](<https://bukkit.org/>)有点故事，且在 bukkit 陨落后越发受到欢迎。 

### Cuberite

[Cuberite](<https://cuberite.org/>) 是一个高性能且可扩展的服务端，由 C++ 和 Lua 编写 ，其性能远超原版 Minecraft 服务端，但其与最新的 Minecraft 客户端不完全兼容（一些游戏特性可能会缺失或不工作）。 

Cuberite Minecraft 服务端可作为 [cuberite](<https://aur.archlinux.org/packages/cuberite/>)AUR 安装，其在 `8080` 端口默认提供一个简单的 web 界面，可以通过浏览器设置大部分的服务器选项，cuberite 的 PKGBUILD 在 [minecraft-server](<https://aur.archlinux.org/packages/minecraft-server/>)AUR 的文件上构建，这意味着 cuberite 服务端提供了它自己的 systemd 单元文件、cuberite 脚本和相应的脚本配置文件。其二进制文件名为 `cuberite`，与 `minecraftd` 的命令相同，配置文件位于 `/etc/conf.d/cuberite`。 

确保您已阅读[#配置](<#%E9%85%8D%E7%BD%AE>)并将您遇到的所有的 `minecraftd` 替换为 `cuberite`。 

### PaperMC

[PaperMC（纸服）](<https://papermc.io>)是一个 Minecraft 服务端，兼容 Spigot 的插件，旨在提供更佳性能。通过 [papermc](<https://aur.archlinux.org/packages/papermc/>)AUR 安装该服务端。 

确保您已阅读[#配置](<#%E9%85%8D%E7%BD%AE>)并将您遇到的所有 `minecraftd` 替换为 `papermc`。 

### Forge

[Forge](<https://minecraftforge.net>) 是一个使用广泛的 Minecraft 模组 API。有以下服务端软件包可用： 

  * [forge-server](<https://aur.archlinux.org/packages/forge-server/>)AUR 最新版本的 Minecraft
  * [forge-server-1.15.2](<https://aur.archlinux.org/packages/forge-server-1.15.2/>)AUR for Minecraft 1.15.2
  * [forge-server-1.14.4](<https://aur.archlinux.org/packages/forge-server-1.14.4/>)AUR for Minecraft 1.14.4
  * [forge-server-1.12.2](<https://aur.archlinux.org/packages/forge-server-1.12.2/>)AUR for Minecraft 1.12.2
  * [forge-server-1.11.2](<https://aur.archlinux.org/packages/forge-server-1.11.2/>)AUR for Minecraft 1.11.2
  * [forge-server-1.10.2](<https://aur.archlinux.org/packages/forge-server-1.10.2/>)AUR for Minecraft 1.10.2
  * [forge-server-1.9.4](<https://aur.archlinux.org/packages/forge-server-1.9.4/>)AUR for Minecraft 1.9.4
  * [forge-server-1.8.9](<https://aur.archlinux.org/packages/forge-server-1.8.9/>)AUR for Minecraft 1.8.9
  * [forge-server-1.7.10](<https://aur.archlinux.org/packages/forge-server-1.7.10/>)AUR for Minecraft 1.7.10

确保您已阅读[#配置](<#%E9%85%8D%E7%BD%AE>)并将遇到的所有 `minecraftd` 替换为 `forged` （若是旧版则还需加上版本号，形同 `forge-x.x.xd`）。 

### Fabric

[Fabric](<https://fabricmc.net/>) 是为 Minecraft 开发的一个轻量化、实验性的模组工具链。通过 [fabric-server](<https://aur.archlinux.org/packages/fabric-server/>)AUR 安装其服务端软件包。 

确保您已阅读[#配置](<#%E9%85%8D%E7%BD%AE>)并将遇到的所有 `minecraftd` 替换为 `fabricd`。 

### Quilt

[Quilt](<https://quiltmc.org/>) 是一个主要为 Minecraft 开发、开源的、社区驱动的模组工具链。通过 [quilt-server](<https://aur.archlinux.org/packages/quilt-server/>)AUR 安装其服务端软件包。 

确保您已阅读[#配置](<#%E9%85%8D%E7%BD%AE>)并将遇到的所有 `minecraftd` 替换为 `quiltd`。 

Quilt 是 Fabric 的一个分支，意味着其可以向下兼容一些 Fabric 模组。 

##  提示和技巧

###  Minecraft 服务器端口

[![](../../File:Tango-view-fullscreen.png)](<../../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** SRV 文档有所记载，支持在使用域名时无需指定端口而使用非默认端口。 (在 [Talk:Minecraft/Java 版服务端](<../../zh-cn/Talk:Minecraft/Java_%E7%89%88%E6%9C%8D%E5%8A%A1%E7%AB%AF.html>) 中讨论)

Minecraft 服务端默认在 `25565` 端口上运行，当输入的地址不带端口时默认使用该端口。 

大部分 Minecraft 服务器提供商需要购买高级服务以使用默认的 Minecraft 端口。因此若您使用的端口不是 `25565`，您需要在域名或地址后加上一个冒号（**:** ）和您的服务器为游戏分配的端口。例如，若您的地址是 `43.12.122.96`，端口是 `28543`，那么您需要连接到`43.12.122.96:28543`。 

##  疑难解答

###  日志

Screen 日志存储在 `/tmp/spigot_spigot_command_dump.txt` 文件中。如果 _systemctl_ 无法启动服务,请检查 _screen_ 日志。 

[Journal](<../../zh-cn/Systemd/Journal.html> "Journal") 日志存储在 `spigot.service`

##  另请参阅

  * 一些打包好的服务端提供从自动备份到多线程服务器等所有功能，请参阅 [Server Wrappers](<https://minecraftservers.gamepedia.com/Server_wrappers>) 以了解更多信息。然而 [AUR](<../../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 提供的管理脚本应当可以满足大部分需求。
  * 您可能会想要设置一个 [systemd 定时器](<../../zh-cn/Systemd_%E5%AE%9A%E6%97%B6%E5%99%A8.html> "Systemd 定时器")，例如与 [mapper](<https://zh.minecraft.wiki/w/%E8%BE%85%E5%8A%A9%E7%A8%8B%E5%BA%8F%E4%B8%8E%E7%BC%96%E8%BE%91%E5%99%A8#Mappers>) 一起使用以为您的世界定时生成地图。
  * 确保定时备份地图，可以使用提供的管理脚本（见阅[#配置](<#%E9%85%8D%E7%BD%AE>)或 [rsync](<../../zh-cn/Rsync.html> "Rsync")）。
  * 另见[架设 Java 版服务器](<https://zh.minecraft.wiki/w/Tutorial:%E6%9E%B6%E8%AE%BEJava%E7%89%88%E6%9C%8D%E5%8A%A1%E5%99%A8>)。
