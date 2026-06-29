相关文章

  * [CrossOver](<../zh-cn/CrossOver.html> "CrossOver")
  * [Deepin-wine](<../zh-cn/Deepin-wine.html> "Deepin-wine")
  * [Wine package guidelines](<../zh-cn/Wine_package_guidelines.html> "Wine package guidelines")

**翻译状态：**

  * 本文（或部分内容）译自 [Wine](<https://wiki.archlinux.org/title/Wine> "arch:Wine")，最近一次同步于 2025-07-28，若英文版本有所[更改](<https://wiki.archlinux.org/title/Wine?diff=0&oldid=840822>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Wine_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Wine](<https://en.wikipedia.org/wiki/Wine_\(software\)> "wikipedia:Wine \(software\)")是一款可以在[类 Unix ](<https://en.wikipedia.org/wiki/Unix-like> "wikipedia:Unix-like") [操作系统](<https://en.wikipedia.org/wiki/Operating_system> "wikipedia:Operating system")中运行[Windows应用程序](<https://en.wikipedia.org/wiki/Microsoft_Windows> "wikipedia:Microsoft Windows")的[兼容层](<https://en.wikipedia.org/wiki/Compatibility_layer> "wikipedia:Compatibility layer")。 

Wine 不进行模拟、转译或虚拟化，而是通过直接提供一组 Win32 API 的对应实现来运行 Windows 应用程序。由于 Wine 的实现与 Windows 的存在一定差异，应用程序运行过程中可能会出现行为、兼容性或性能方面的损失。 

**警告：**

  * Wine **并非** 与你的系统隔离：如果 _你_ 使用你的用户帐户访问某个文件或资源，那么在 Wine 中运行的程序 _也可以_ 。参见[#在单独的用户帐户下运行 Wine](<#%E5%9C%A8%E5%8D%95%E7%8B%AC%E7%9A%84%E7%94%A8%E6%88%B7%E5%B8%90%E6%88%B7%E4%B8%8B%E8%BF%90%E8%A1%8C_Wine>)和[安全#沙盒程序](<../zh-cn/%E5%AE%89%E5%85%A8.html#%E6%B2%99%E7%9B%92%E7%A8%8B%E5%BA%8F> "安全")了解可能的预防措施。
  * Wine 也可以运行恶意软件（参见 [Wine 关于恶意软件兼容性的 FAQ](<https://gitlab.winehq.org/wine/wine/-/wikis/FAQ#is-wine-malware-compatible>)）

##  安装

可以通过 [wine](<https://archlinux.org/packages/?name=wine>)包（开发版），[wine-stable](<https://aur.archlinux.org/packages/wine-stable/>)AUR（稳定版）或 [wine-staging](<https://archlinux.org/packages/?name=wine-staging>)包（测试版本）来[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") Wine。[Wine Staging](<https://wine-staging.com/>) 是 [Wine](<https://www.winehq.org/>) 的修补版本, 其中包含了漏洞修复和尚未集成到稳定或开发分支中的特性。 

**提示：** 可以考虑为依赖于 Internet Explorer 和 .NET 的应用程序分别安装 [wine-gecko](<https://archlinux.org/packages/?name=wine-gecko>)包 和 [wine-mono](<https://archlinux.org/packages/?name=wine-mono>)包。这两个软件包不是一定要安装的，因为 Wine 会根据需要自行下载相关文件。反过来说，如果提前安装了软件包，Wine 就不需要再下载这些文件了。不过无论如何，应[通过 pacman 对其进行管理](<../zh-cn/%E7%B3%BB%E7%BB%9F%E7%BB%B4%E6%8A%A4.html#%E4%BD%BF%E7%94%A8%E5%8C%85%E7%AE%A1%E7%90%86%E5%99%A8%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6> "系统维护")。

其它需求见 [#图形驱动程序](<#%E5%9B%BE%E5%BD%A2%E9%A9%B1%E5%8A%A8%E7%A8%8B%E5%BA%8F>)和 [#声音](<#%E5%A3%B0%E9%9F%B3>)。 

###  可选依赖项

Wine 有许多可选依赖项，简单的应用程序可能不需要这些依赖项，但如果希望使用声音、3D 图形、视频播放等功能，则应安装这些依赖项。 

请注意，许多 Windows 应用程序都是 32 位的，因此需要 32 位版本的相应库，其中有些库仅在 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 上提供。标准（64 位）库可用于 64 位应用程序，如果运行的 Wine 版本采用新的 WoW64 模式（参见[#安装](<#%E5%AE%89%E8%A3%85>)中的说明），则可用于任何应用程序。使用 [file(1)](<https://man.archlinux.org/man/file.1>) 命令可以检查 Windows 可执行文件是否为 64 位。 

**提示：** 常见的依赖项，尤其是与游戏相关的依赖项，可以参考 [Lutris 文档](<https://github.com/lutris/docs/blob/master/WineDependencies.md#archendeavourosmanjaroother-arch-derivatives>) 。

####  图形驱动程序

当你需要安装 32 位版本的图形驱动程序时。请安装 [Xorg#驱动安装](<../zh-cn/Xorg.html#%E9%A9%B1%E5%8A%A8%E5%AE%89%E8%A3%85> "Xorg")页面中 _OpenGL (multilib)_ 一栏列出的软件包。 

当 Wine 在你的终端窗口中报告以下内容时，你的驱动程序可能没有正确安装或配置： 
    
    直接渲染被禁用,很可能是 OpenGL 驱动程序未被正确安装
    
**注意：** 安装正确的库后，您可能需要重新启动 [Xorg](<../zh-cn/Xorg.html> "Xorg") 。

####  声音

在使用 Wine 运行应用时遇到声音问题，您也可以尝试在 `winecfg` 中检查声音设备的配置，确认选择了正确的声音设备。 

根据不同的声音驱动，安装对应的软件包： 

  * **[ALSA](<../zh-cn/ALSA.html> "ALSA")** ：安装 [lib32-alsa-lib](<https://archlinux.org/packages/?name=lib32-alsa-lib>)包 和 [lib32-alsa-plugins](<https://archlinux.org/packages/?name=lib32-alsa-plugins>)包
  * **[PulseAudio](<../zh-cn/PulseAudio.html> "PulseAudio")** ：安装 [lib32-libpulse](<https://archlinux.org/packages/?name=lib32-libpulse>)包
  * **[PipeWire](<../zh-cn/PipeWire.html> "PipeWire")** ：安装 [lib32-pipewire](<https://archlinux.org/packages/?name=lib32-pipewire>)包 以及根据需求安装下面的包： 
    * 安装 [pipewire-pulse](<https://archlinux.org/packages/?name=pipewire-pulse>)包 和 [lib32-libpulse](<https://archlinux.org/packages/?name=lib32-libpulse>)包 以使用 PulseAudio 作为声音前端
    * 安装 [pipewire-alsa](<https://archlinux.org/packages/?name=pipewire-alsa>)包、[lib32-alsa-lib](<https://archlinux.org/packages/?name=lib32-alsa-lib>)包 和 [lib32-alsa-plugins](<https://archlinux.org/packages/?name=lib32-alsa-plugins>)包 以使用 ALSA 作为声音前端
  * **[OSS](<../zh-cn/Open_Sound_System.html> "OSS")** ： 安装 [lib32-alsa-oss](<https://archlinux.org/packages/?name=lib32-alsa-oss>)包

如果 _winecfg_ **仍然** 无法检测到音频驱动程序（Selected driver: (none)）， 请尝试[配置注册表](<https://gitlab.winehq.org/wine/wine/-/wikis/Wine-User's-Guide#using-regedit>)。例如，在一个 wine-1.9.7 的 64 位版本上，如果麦克风在 32 位 Windows 应用程序中无法正常工作，则可以按照以下步骤来手动配置其对声音硬件（扬声器和麦克风）的访问权限：打开 `regedit`，查找路径 `HKEY_CURRENT_USER > Wine > Drivers> Software` ，然后添加一个键名为 `Audio` 的字符串值，并为其指定值 `alsa` 。此外，[重建前缀](<#WINEPREFIX>)也可能有一定帮助。 

#####  MIDI支持

[MIDI](<https://en.wikipedia.org/wiki/MIDI> "wikipedia:MIDI") 是一种从 20 世纪 90 年代开始被广泛使用的音乐系统。如果您使用 Wine 游玩使用了相关技术的老游戏，可能会发现游戏音乐无法正常播放。 

事实上 Wine 提供了非常好的 MIDI 支持，但前提是您的主机系统也支持 MIDI，相关内容请参阅[MIDI](<../zh-cn/MIDI.html> "MIDI")。最后需要注意的是，请确保 Wine 使用了正确的 MIDI 输出。 

若要在游戏中播放 MIDI 轨道，请使用 `winetricks gmdls` 以安装 Microsoft's General MIDI DLS Collection。 

####  其他依赖

部分应用可能会需要其他的依赖（参考 [WineHQ 页面](<https://gitlab.winehq.org/wine/wine/-/wikis/Building-Wine#satisfying-build-dependencies>)） 

  * TLS 的 32 位支持可以安装 [lib32-gnutls](<https://archlinux.org/packages/?name=lib32-gnutls>)包
  * 手柄和游戏杆的 32 位支持可以安装 [lib32-sdl2](<https://aur.archlinux.org/packages/lib32-sdl2/>)AUR
  * 媒体播放的 32 位支持可以根据需求安装 [lib32-gst-plugins-base](<https://archlinux.org/packages/?name=lib32-gst-plugins-base>)包、 [lib32-gst-plugins-good](<https://archlinux.org/packages/?name=lib32-gst-plugins-good>)包、[lib32-gst-plugins-bad](<https://aur.archlinux.org/packages/lib32-gst-plugins-bad/>)AUR、[lib32-gst-plugins-ugly](<https://aur.archlinux.org/packages/lib32-gst-plugins-ugly/>)AUR 和 [lib32-gst-libav](<https://aur.archlinux.org/packages/lib32-gst-libav/>)AUR
  * 对于 [NTLM](<https://en.wikipedia.org/wiki/NTLM> "wikipedia:NTLM") 验证可以安装 [samba](<https://archlinux.org/packages/?name=samba>)包

###  Wine前缀内依赖

除了系统依赖项之外，一些程序还需要额外的字体或 dll 库文件，这时您可以将相关内容复制或安装到 [#WINEPREFIX](<#WINEPREFIX>) 中（参见 [WineHQ 页面](<https://gitlab.winehq.org/wine/wine/-/wikis/FAQ#my-application-says-some-dll-or-font-is-missing-what-do-i-do>)）。 

我们姑且将上面这种依赖情况称为“WINEPREFIX 内部依赖（In-prefix dependencies）”。 

您可以尝试使用 Winetricks 来满足一些程序的依赖。它像一个简陋的“包管理器”，通过安装一些软件及应用相关配置来满足不同程序的运行需求。关于它的安装和使用可以参考下文的 [#Winetricks](<#Winetricks>) 章节。 

由于依赖关系之间的冲突，您可能无法创建可以运行所有程序的“完美”运行环境 [[1]](<https://github.com/Winetricks/winetricks/issues/1580#issuecomment-666604256>) [[2]](<https://github.com/Winetricks/winetricks/issues/469>)。建议您将前缀（Wine Prefix）视为可以随时被销毁的（除非它们包含重要的配置或数据），并为具有不同依赖关系的程序使用单独的前缀。您可以使用 [#WINEPREFIX](<#WINEPREFIX>) 环境变量来指定您期望操作的前缀环境。 

确定某个应用需求所需的依赖往往需要反复试验，您可以参考 [Bottles 的依赖页面](<https://usebottles.com/database/dependencies/>)，了解一些常见的依赖关系。下面的内容对解决一些特定的应用依赖问题可能会有所帮助： 

  * [Wine Application Database](<https://appdb.winehq.org/>)：Wine 的官方资源，但是内容可能比较老旧且相对下面的内容可能相对缺少维护。
  * [Lutris](<https://lutris.net/games>)：您可以在 lutris 的页面上搜索您想游玩的游戏，部分游戏可以在详细页面点击下拉菜单按钮，选择“View install script”来查看 lutris 所使用的 Winetricks 的配置。
  * [Bottles program repository](<https://github.com/bottlesdevs/programs>)：资源规模较小，但不仅仅包括游戏。
  * [ProtonDB](<https://www.protondb.com/>)：虽然 Proton 与 Wine 的兼容性不同（如果您使用该网站资源或在网站创建回复，建议仅使用 Proton），但是评论中可能会搜集到用户所使用的配置。 
    * 您也可以查阅 [protonfixes](<https://github.com/Open-Wine-Components/ULWGL-protonfixes/>) 工具的源代码，以及包含其内容的 [proton-ge-custom](<https://github.com/GloriousEggroll/proton-ge-custom>)。但要注意的是，他们假定您的运行环境中存在 Proton 和 GE 的修复游戏运行补丁。

如果您发现自己在管理游戏运行环境上花费了大量时间，那么使用第三方应用程序代为处理可能会更方便。 

###  第三方程序

以下的程序均有他们自己的社区与官网，Wine的官方社区**不支持** 。详见 [Wine Wiki](<https://gitlab.winehq.org/wine/wine/-/wikis/Third-Party-Applications>) 。 

  * **[Bottles](<../zh-cn/Bottles.html> "Bottles")** — 一个基于GTK图形化的Wine前缀和运行管理器。

     <https://usebottles.com/> || [bottles](<https://aur.archlinux.org/packages/bottles/>)AUR

  * **[CrossOver](<../zh-cn/CrossOver.html> "CrossOver")** — 收费的商用官方 Wine。提供更多的终端用户支援和图形化界面。

     <https://www.codeweavers.com> || [crossover](<https://aur.archlinux.org/packages/crossover/>)AUR

  * **icoextract** — Windows 的可执行程序 (.exe 和 .dll) 的图标生成器。

     <https://github.com/jlu5/icoextract> || [icoextract](<https://aur.archlinux.org/packages/icoextract/>)AUR

  * **[Lutris](<https://en.wikipedia.org/wiki/Lutris> "wikipedia:Lutris")** — 一个游戏启动器(附前缀管理功能），支持Wine上的游戏以及Linux原生游戏。

     <https://lutris.net> || [lutris](<https://archlinux.org/packages/?name=lutris>)包

  * **[PlayOnLinux](<https://en.wikipedia.org/wiki/PlayOnLinux> "wikipedia:PlayOnLinux")** — 图形化 Wine 前缀管理器。包括脚本协助程序的安装与配置。

     <https://www.playonlinux.com> || [playonlinux](<https://aur.archlinux.org/packages/playonlinux/>)AUR

  * **[Proton](<../zh-cn/Steam.html#Proton_Steam-Play> "Proton")** — 为[Steam](<../zh-cn/Steam.html> "Steam")打造的兼容性工具，它基于 Wine 而有很多附加组件。见[ProtonDB](<https://www.protondb.com/>) 获取兼容列表。

     <https://github.com/ValveSoftware/Proton> || [proton](<https://aur.archlinux.org/packages/proton/>)AUR

  * **PyWinery** — 为 Wine 打造的简单前缀管理器。

     <https://github.com/ergoithz/pywinery> || [pywinery](<https://aur.archlinux.org/packages/pywinery/>)AUR

  * **Q4Wine** — 给 Wine 的图形化前缀管理器。为更好地设计统一，可以使用[Qt](<../zh-cn/Qt.html> "Qt")主题到 Wine 设置中。

     <https://sourceforge.net/projects/q4wine/> || [q4wine-git](<https://aur.archlinux.org/packages/q4wine-git/>)AUR

  * **WINEgui** — 用户友好的 wine 图形界面

     <https://gitlab.melroy.org/melroy/winegui> || [winegui](<https://aur.archlinux.org/packages/winegui/>)AUR, [winegui-bin](<https://aur.archlinux.org/packages/winegui-bin/>)AUR

##  配置

配置 Wine 通常使用以下方法： 

  * [control ](<https://gitlab.winehq.org/wine/wine/-/wikis/Commands/control>) \- Wine 对 [Windows 控制面板](<https://en.wikipedia.org/wiki/Control_Panel_\(Windows\)> "wikipedia:Control Panel \(Windows\)")的实现，可以通过运行 `wine control` 启动。
  * [regedit](<https://gitlab.winehq.org/wine/wine/-/wikis/Commands/regedit>) \- 是 Wine 的[注册表编辑工具](<https://en.wikipedia.org/wiki/Windows_Registry> "wikipedia:Windows Registry")，可以通过运行 `regedit` 来启动。另见 WineHQ 关于[有用的注册表键](<https://gitlab.winehq.org/wine/wine/-/wikis/Useful-Registry-Keys>)。
  * [winecfg](<https://gitlab.winehq.org/wine/wine/-/wikis/Commands/winecfg>)——Wine 的 [GUI](<https://en.wikipedia.org/wiki/Graphical_user_interface> "wikipedia:Graphical user interface") 配置工具，可以通过 `winecfg` 运行。

  * 完整列表见 WineHQ 的[命令列表](<https://gitlab.winehq.org/wine/wine/-/wikis/Commands#programs>)。

### WINEPREFIX

默认情况下，Wine 将其配置文件和安装的 Windows 程序存储在 `~/.wine` ，通常会把此目录叫作“Wine prefix”或“Wine bottle”。当您运行 Windows 程序或 Wine 的捆绑程序(如 winecfg)时，它会自动创建/更新。前缀目录还包含一个目录，您的 Windows 程序将其视为 `c:` （ C 盘）。 

**注意：** Wine 前缀不兼容旧版本。新版本的Wine会在必要时自动升级旧前缀，旧版本的 Wine 使用升级后的前缀可能会出错。（[Lutris-GE-7.0-8-LoL 版本说明](<https://github.com/GloriousEggroll/wine-ge-custom/releases/tag/7.0-GE-8-LoL>)中有提到类似问题）

您可以通过 `WINEPREFIX` [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")指定 Wine 使用的前缀位置。如果您希望为不同的 Windows 程序使用单独的配置，这会非常有用。当 Wine 在指定的 `WINEPREFIX` 第一次运行时，Wine 将自动创建一个带有 C 盘和注册表信息的目录。 

例如，如果您分别执行命令 `env WINEPREFIX=~/.win-a wine program-a.exe` 和 `env WINEPREFIX=~/.win-b wine program-b.exe` ，这两个程序将分别在 `~/.win-a` 和 `~/.win-b` 路径下有各自单独的 C 盘目录和注册表配置。 

**警告：** Wine不是[沙盒](<https://en.wikipedia.org/wiki/Sandbox_\(computer_security\)> "wikipedia:Sandbox \(computer security\)")！运行在 Wine 下的程序仍然可以访问外部系统的内容！（例如, Wine 会默认将 `/` 映射到 `Z:`，无论哪个 Wine 前缀）

若要在不运行 Windows 程序或其他图形工具的情况下创建前缀，可以执行： 
    
    $ env WINEPREFIX=~/.customprefix wineboot -u
    
### WINEARCH

Wine默认使用一个64位环境。你可以使用[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量") `WINEARCH` 控制这一行为。 例如您可以删除或重命名 `~/.wine` 目录，之后执行 `$WINEARCH=win32 winecfg` 来创建一个32位的 Wine 环境。不明确配置 `WINEARCH` 会默认创建64位环境。 

我们可以结合 `WINEPREFIX` 来分别创建32位和64位环境 
    
    $ WINEARCH=win32 WINEPREFIX=~/win32 winecfg
    $ WINEPREFIX=~/win64 winecfg
    
`WINEARCH` 也对一些其他程序生效，例如 [#Winetricks](<#Winetricks>)（以 Steam 为例） 
    
    $ WINEARCH=win32 WINEPREFIX=~/.local/share/wineprefixes/steam winetricks steam
    
确认已经创建的 Wine Prefix 是哪种环境需要检查其注册表内容。下面的命令通过查找 `~/.wine` 目录下的注册表文件内容，检查其包含 `#arch-win32` 还是 `#arch=win64` 来确认其架构类型。 
    
    $ grep '#arch' ~/.wine/system.reg
    
###  字体

如果 Wine 应用程序的字体存在丢失、无法正常显示等问题，您可以尝试用软链接的方式，将系统字体文件映射到对应 [#WINEPREFIX](<#WINEPREFIX>) 中： 
    
    $ cd ${WINEPREFIX:-~/.wine}/drive_c/windows/Fonts && for i in /usr/share/fonts/**/*.{ttf,otf}; do ln -s "$i" ; done
    
Wine 使用 FreeType 渲染字体，因此在一些情况下，您可以尝试修改 FreeType 的一些配置。例如您可以尝试设置如下的[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")修改 FreeType 的解析器版本： 
    
    FREETYPE_PROPERTIES="truetype:interpreter-version=35"
    
此外，您也可以尝试在 Wine Prefix 中安装微软的 TrueType 字体，详见[微软字体](<../zh-cn/%E5%BE%AE%E8%BD%AF%E5%AD%97%E4%BD%93.html> "微软字体")。也可以考虑使用 [#Winetricks](<#Winetricks>) ，执行 `winetricks corefonts` ，如果仍存在问题，可以尝试执行 `winetricks allfonts` 。 

您还可以通过修改 Wine 注册表的方式添加字体别名，以便 Wine 使用系统字体。 

以中文用户常用字体 `Noto Sans CJK SC` 为例，将以下文本保存为 `chs.reg`：
    
    REGEDIT4
    
    [HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\FontSubstitutes]
    "MS Shell Dlg"="Noto Sans CJK SC"
    "MS Shell Dlg 2"="Noto Sans CJK SC"
    "SimSun"="Noto Sans CJK SC"
    "Microsoft YaHei"="Noto Sans CJK SC"
    
通过执行 `wine regedit ./chs.reg`即可导入以上条目。 

执行相关操作后，需要关闭所有 Wine 服务并运行 `winecfg` 查看效果。 

如果字体看起来模糊不清，用下面的命令来更改Wine注册表： 
    
     $ wine reg add 'HKEY_CURRENT_USER\Software\Wine\X11 Driver' /v ClientSideWithRender /t REG_SZ /d N
    
对于高分辨率屏幕，可以在 `winecfg` 中尝试调整 dpi 值。 

另见[字体配置#不支持_Fontconfig_的程序](<../zh-cn/%E5%AD%97%E4%BD%93%E9%85%8D%E7%BD%AE.html#%E4%B8%8D%E6%94%AF%E6%8C%81_Fontconfig_%E7%9A%84%E7%A8%8B%E5%BA%8F> "字体配置")及相关页面尝试调整文字渲染问题。 

####  启用字体平滑

启用 ClearType 字体平滑可以提高 Wine 中的字体渲染效果。 若要启用“次像素平滑(ClearType) RGB”请创建文件并执行之后的命令： 
    
    /tmp/fontsmoothing
    
    REGEDIT4
    
    [HKEY_CURRENT_USER\Control Panel\Desktop]
    "FontSmoothing"="2"
    "FontSmoothingOrientation"=dword:00000001
    "FontSmoothingType"=dword:00000002
    "FontSmoothingGamma"=dword:00000578
    EOF
    
    $ WINE=${WINE:-wine} WINEPREFIX=${WINEPREFIX:-$HOME/.wine} $WINE regedit /tmp/fontsmoothing 2> /dev/null
    
如果你已经安装了 [winetricks](<https://archlinux.org/packages/?name=winetricks>)包 ，有更简单的方式： 
    
    winetricks fontsmooth=rgb
    
相关内容详见[[3]](<https://askubuntu.com/a/219795>)。 

###  桌面项（快捷方式）

当使用 Windows 应用的安装程序尝试创建快捷方式时，Wine 会创建对应的 [.desktop](</wzh/index.php?title=.desktop&action=edit&redlink=1> ".desktop（页面不存在）") 文件。Arch Linux 中这些文件的默认位置是： 

  * 桌面快捷方式位于 `~/Desktop` 下。
  * 开始菜单条目位于 `~/.local/share/applications/wine/Programs/` 下。

**注意：** Wine 不支持为所有用户安装 Windows 应用程序，所以 Wine 不会把 `.desktop` 文件放到 `/usr/share/applications` 中。详见 [WineHQ bug 11112](<https://bugs.winehq.org/show_bug.cgi?id=11112>)

**提示：** 如果安装软件时桌面项没有被创建或已经丢失，可以尝试执行 `wine winemenubuilder`。

####  为 Wine 的工具创建桌面项

默认情况下，Wine 附带的软件不会创建桌面项（例如 `winecfg`、` winebrowser` 等）。这可以通过安装 [wine-installer](<https://aur.archlinux.org/packages/wine-installer/>)AUR 或 [wine-installer-git](<https://aur.archlinux.org/packages/wine-installer-git/>)AUR （后者不依赖 [#Winetricks](<#Winetricks>) ）来解决，您也可以根据下面的说明手动创建相关条目。 

下面的文件您可以保存在 `~/.local/share/applications/wine/` 目录下： 
    
    wine-browsedrive.desktop
    
    [Desktop Entry]
    Name=Browse C: Drive
    Comment=Browse your virtual C: drive
    Exec=wine winebrowser c:
    Terminal=false
    Type=Application
    Icon=folder-wine
    Categories=Wine;
    
    wine-uninstaller.desktop
    
    [Desktop Entry]
    Name=Uninstall Wine Software
    Comment=Uninstall Windows applications for Wine
    Exec=wine uninstaller
    Terminal=false
    Type=Application
    Icon=wine-uninstaller
    Categories=Wine;
    
    wine-winecfg.desktop
    
    [Desktop Entry]
    Name=Configure Wine
    Comment=Change application-specific and general Wine options
    Exec=winecfg
    Terminal=false
    Icon=wine-winecfg
    Type=Application
    Categories=Wine;

并在`~/.config/menus/applications-merged/`目录创建如下文件： 
    
    wine.menu
    
    <!DOCTYPE Menu PUBLIC "-//freedesktop//DTD Menu 1.0//EN"
    "http://www.freedesktop.org/standards/menu-spec/menu-1.0.dtd">
    <Menu>
      <Name>Applications</Name>
      <Menu>
        <Name>wine-wine</Name>
        <Directory>wine-wine.directory</Directory>
        <Include>
          <Category>Wine</Category>
        </Include>
      </Menu>
    </Menu>
    
如果这些文件显示的图标存在问题，可能是您使用的图标主题中没有这些程序的图标，或者您也可以手动指定应用的图标文件。一个包含了这些内容的图标主题是 [gnome-colors-icon-theme](<https://aur.archlinux.org/packages/gnome-colors-icon-theme/>)AUR。 

####  删除桌面项（快捷方式）

由 Wine 创建的菜单条目位于 `~/.local/share/applications/wine/Programs/` 目录。 

如果要删除 Wine 绑定的不想使用的扩展，可以执行以下命令（摘自 [Wine FAQ](<https://gitlab.winehq.org/wine/wine/-/wikis/FAQ#how-do-i-clean-the-open-with-list>)，请仔细确认后执行） ： 
    
    $ rm ~/.local/share/mime/packages/x-wine*
    $ rm ~/.local/share/applications/wine-extension*
    $ rm ~/.local/share/icons/hicolor/*/*/application-x-wine-extension*
    $ rm ~/.local/share/mime/application/x-wine-extension*
    
此外您也可以通过移除在 `/.config/menus/` 中的 `wine-*.menu` 文件以移除 KDE 应用菜单中 Wine 子菜单的图标。 

###  主题

类似 Windows XP 外观的主题可以在[这里下载](<https://archive.org/download/zune-desktop-theme/ZuneDesktopTheme.msi>)。可以参考 [Wine 维基页面](<https://gitlab.winehq.org/wine/wine/-/wikis/Wine-User's-Guide#running-msi-files>)进行安装。安装完成后，可以使用 `winecfg` 选择对应的主题。 

**注意：** 上面提到的主题只能安装在32位，系统兼容性配置为 Windows XP 的 [#WINEPREFIX](<#WINEPREFIX>) 中。要将其安装在64位环境上，您需要在的32位 Wine Prefix 环境中安装该主题，之后从32位 Wine Prefix 环境下的 `drive_c/Windows/Resources/Themes` 目录内，将 `Zune` 文件夹和 `Zune.theme` 文件复制到您使用的环境中。

[wine-staging](<https://archlinux.org/packages/?name=wine-staging>)包 用户可以尝试在 `winecfg` 中配置启用“Enable GTK3 Theming”令相关应用适配当前的 GTK 主题。 

###  打印机

为了在32位的 [#WINEPREFIX](<#WINEPREFIX>) 中（例如微软 Word）使用您已经安装的打印机（包括本地打印机和网络打印机），您需要[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [lib32-libcups](<https://archlinux.org/packages/?name=lib32-libcups>)包 ，并在之后重启所有 Wine 服务及您的应用程序。 

###  网络

一些32位的程序可能需要[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [lib32-gnutls](<https://archlinux.org/packages/?name=lib32-gnutls>)包 来创建 TLS 或 HTTPS 连接。 

对于 ICMP（ping 命令），需要为 Wine 配置相关权限（[Capabilities](<../zh-cn/Capabilities.html> "Capabilities"))，详见 [WineHQ FAQ](<https://gitlab.winehq.org/wine/wine/-/wikis/FAQ#failed-to-use-icmp-network-ping-this-requires-special-permissions>)： 
    
    # setcap cap_net_raw+epi /usr/bin/wine-preloader
    
如果执行上述命令后，您遇到了一些问题（例如程序异常、权限问题等），您可以通过下面的命令取消相关权限： 
    
    # setcap -r /usr/bin/wine-preloader
    
##  使用

**警告：** 不要以 root 身份运行 Wine 或安装 Windows 应用程序！详见 [Wine FAQ](<https://gitlab.winehq.org/wine/wine/-/wikis/FAQ#should-i-run-wine-as-root>)。

[Wine 用户手册](<https://gitlab.winehq.org/wine/wine/-/wikis/Wine-User's-Guide#using-wine>)可以为您提供 Wine 使用说明。 

[Wine 程序数据库（AppDB）](<https://appdb.winehq.org/>)可以提供部分特定 Windows 程序在 Wine 中运行的参考信息。 

### Wayland

**警告：** Wine 的 [Wayland](<../zh-cn/Wayland.html> "Wayland") 驱动仍处于实验阶段

目前 Wine 在 Wayland 环境下通过 [XWayland](<../zh-cn/Wayland.html#XWayland> "Wayland") 进行渲染，这可以为大部分用户提供良好的体验。在 9.0rc1 版本后，Wine 在原生 Wayland 支持上取得了较大进展，已经可以在一些情境下使用。 

如果您希望尝试最近加入到 Wine 版本的原生 Wayland 支持，可以尝试以下步骤： 

  * Wine 9.22 后的版本执行下面的命令修改注册表配置：

    $ wine reg add 'HKEY_CURRENT_USER\Software\Wine\Drivers' /v Graphics /t REG_SZ /d 'x11,wayland'

  * 通过取消设置 `DISPLAY` [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")，来强制使用 Wayland 驱动：
        
        $ env -u DISPLAY wine example.exe

如果取消设置 `DISPLAY` 导致 Wine 运行出现问题，请检查您安装的 Wine 版本是否在构建时添加了 Wayland 驱动支持。 

###  停止运行 Wine 程序

在执行 `wine` 的终端按下 Ctrl+Z 或在 `wineconsole` 的终端中按下 Ctrl+C，只是将进程转入了后台运行。 

假设当前进程如下： 
    
    $ ps -xo pid,cmd
        PID CMD
        297 -bash
        933 /usr/bin/wineserver
        939 C:\windows\system32\services.exe
        942 C:\windows\system32\winedevice.exe
        950 C:\windows\system32\explorer.exe /desktop
        954 C:\windows\system32\winedevice.exe
        965 C:\windows\system32\plugplay.exe
        977 C:\windows\system32\svchost.exe -k LocalServiceNetworkRestricted
        984 C:\windows\system32\rpcss.exe
        997 mbserver.exe
       1017 start.exe /exec
       1019 C:\windows\system32\conhost.exe --unix --width 169 --height 40 --server 0x10
       1021 Z:\home\wineuser\mbserver.exe
       1030 ps -xo pid,cmd

所有正在运行中的 `wine` 和 `wineconsole` 进程都可以被 [wineserver -k](<https://gitlab.winehq.org/wine/wine/-/wikis/Wine-User's-Guide#-k-n>) 命令终止。例如： 
    
    $ wineserver -k 15

这个命令可以与 [#WINEPREFIX](<#WINEPREFIX>) 关联，因此当您使用自己配置的 `WINEPREFIX` 时，可以执行： 
    
    $ WINEPREFIX=~/wine/my-prefix wineserver -k

一个与上面操作等价的命令是直接将相关进程终止掉： 
    
    $ kill 997 1021

##  提示与技巧

### Wineconsole

通常情况下，你可能需要运行.exe来修补游戏文件，例如一个老游戏的宽屏 mod，通过 Wine 正常运行.exe可能不会产生任何效果。在这种情况下，你可以打开一个终端，运行以下命令。 
    
    $ wineconsole cmd
    
然后转到该目录，从那里运行 _.exe_ 文件。 

### Winetricks

[Winetricks](<https://gitlab.winehq.org/wine/wine/-/wikis/Winetricks>)是一个可以帮助用户安装一些 Windows 程序所需依赖的脚本。可安装的组件包括 Direct9、MSXML（Office 2007 和 Internet Explorer 所需依赖）、Visual 运行时库和很多其它组件。 

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")[winetricks](<https://archlinux.org/packages/?name=winetricks>)包（或[winetricks-git](<https://aur.archlinux.org/packages/winetricks-git/>)AUR）后，直接执行下面命令即可使用： 
    
    $ winetricks
    
如果希望使用图形界面，需要[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [zenity](<https://archlinux.org/packages/?name=zenity>)包（GTK）或 [kdialog](<https://archlinux.org/packages/?name=kdialog>)包（QT）。 

###  性能

#### CSMT

CSMT 是 Wine 使用的一项技术，它为 OpenGL 调用使用了一个单独的线程，以显著提高性能。从 Wine 3.2 开始，CSMT 被默认启用。 

注意，CSMT可以会在某些应用中损害性能。如果这种情况发生，通过运行 `wine regedit` 并设置 _HKEY_CURRENT_USER - > Software > Wine > Direct3D > csmt_ 的 DOWRD 值为 0x00 （禁用）。 

更多信息： 

  * [Phoronix 论坛讨论](<https://www.phoronix.com/forums/showthread.php?93967-Wine-s-Big-Command-Stream-D3D-Patch-Set-Updated/page3&s=7775d7c3d4fa698089d5492bb7b1a435>)

####  强制使用OpenGL模式运行游戏

有些游戏可能有 OpenGL 模式，其性能可能比其默认的 DirectX 模式更好。虽然启用 OpenGL 渲染的是 "特定应用"，但许多游戏可以使用 `-opengl` 参数。 
    
    $ wine _/path/to/3d_game.exe_ -opengl
    
你应该参考你的应用程序文档和 Wine 的官网 [AppDB](<https://appdb.winehq.org>) 来了解这些应用程序的具体信息。 

#### DXVK

[DXVK](<https://github.com/doitsujin/dxvk>) 是在 Vulkan 上对 DirectX 8,9,10 和 11 的一个可能的新实现。其在大部分游戏上的性能和兼容性优于 WineD3D。其不支持 DirectX 12，另请参阅 [#VKD3D-Proton](<#VKD3D-Proton>)。DXVK 和 VKD3D-Proton 可以且应当一同安装以支持所有 DirectX 版本。 

用 [#Winetricks](<#Winetricks>) 来安装最新的版本： 

安装 [dxvk-bin](<https://aur.archlinux.org/packages/dxvk-bin/>)AUR 以使用它. 然后运行以下命令，在 wine 前缀中激活它（默认为 `~/.wine`): 
    
    $ WINEPREFIX=_your-prefix_ winetricks dxvk
    
你可以安装一个特殊的版本。例如，若要安装一个[对驱动要求较低](<https://github.com/doitsujin/dxvk/wiki/Driver-support#dxvk-1103>)的 DXVK 版本，使用以下命令： 
    
    $ WINEPREFIX=_your-prefix_ winetricks dxvk1103
    
也可以安装 [dxvk-mingw](<https://aur.archlinux.org/packages/dxvk-mingw/>)AUR 或 [dxvk-bin](<https://aur.archlinux.org/packages/dxvk-bin/>)AUR。然后运行下面的指令来在你的 Wine 前缀中激活它（默认是 `~/.wine`）。 
    
    $ WINEPREFIX=_your-prefix_ setup_dxvk install --symlink
    
#### VKD3D-Proton

[VKD3D-Proton](<https://github.com/HansKristian-Work/vkd3d-proton>) 是 [VKD3D](<https://wiki.winehq.org/Vkd3d>) 的一个 fork，这旨在用 Vulkan 实现完整的 Direct3D 12 API。该项目是 Proton 中 Direct3D 12 支持的开发项目，旨在提高 DirectX 12 游戏的性能和兼容性。 

**注意：** 尽管这些 DLL 名称中带有“Proton”，它们在普通版本的 Wine 中也能正常工作，并且可以与 DXVK 一起使用 [#DXVK](<#DXVK>) 。

为使用最新的版本，使用 [#Winetricks](<#Winetricks>)： 
    
    $ WINEPREFIX=_your-prefix_ winetricks vkd3d
    
此外，安装 [vkd3d-proton-mingw](<https://aur.archlinux.org/packages/vkd3d-proton-mingw/>)AUR 或 [vkd3d-proton-bin](<https://aur.archlinux.org/packages/vkd3d-proton-bin/>)AUR 。然后运行下面的指令来在你的 Wine 前缀中激活它（默认是 `~/.wine`）。 
    
    $ WINEPREFIX=_your-prefix_ setup_vkd3d_proton install --symlink
    
**警告：** VKD3D-Proton 会覆盖 DirectX 12 DLL，这也许会被一些在线多玩家游戏认定为作弊，然后你的账户可能会被 **banned** 。用的时候小心！

**提示：****仅** 对于 [AMDGPU](<../zh-cn/AMDGPU.html> "AMDGPU") 用户：当搭配 [Gamescope](<../zh-cn/Gamescope.html> "Gamescope") 使用时，DXVK v2.1 及以上版本支持 [HDR10](<https://en.wikipedia.org/wiki/HDR10> "wikipedia:HDR10") 显示器。详情请参见 [HDR 显示器支持](<../zh-cn/HDR_%E6%98%BE%E7%A4%BA%E5%99%A8%E6%94%AF%E6%8C%81.html> "HDR 显示器支持")

#### Gallium Nine

[![](../File:Tango-edit-cut.png)](<../File:Tango-edit-cut.png>)**这一章节正在考虑移除。**

**原因:** No point in keeping historical details if they have no relevance. (在 [Talk:Wine](<../zh-cn/Talk:Wine.html>) 讨论)

Gallium Nine was available for Mesa users only. But now Gallium Nine have been totally dropped from [Mesa](<../zh-cn/OpenGL.html> "Mesa"). And so, now you cannot use Gallium Nine at all. Now you should use [#DXVK](<#DXVK>) instead. 

#### xSync

Some games heavily use windows sync objects to run multi-threaded workloads, Wine is able to provide a userspace implementation through wineserver, however most of the time the default implementation have major performance impact in CPU bound scenarios. 

Currently there are 3 options available to improve the performance, and you should use only one of it at same time: 

  * ESync - User-space eventfd-based synchronization. 
    * Not included in [wine](<https://archlinux.org/packages/?name=wine>)包. Included in [wine-staging](<https://archlinux.org/packages/?name=wine-staging>)包, but not enabled by default.
    * Enabled by default in [Proton](<../zh-cn/Steam.html#Proton_Steam-Play> "Proton") unless FSync is available. FSync is not available if you use very old release of Linux kernel.

  * FSync - In-kernel Futex2-based implementation of synchronization, should have better performance than ESync. 
    * Enabled by default in [Proton](<../zh-cn/Steam.html#Proton_Steam-Play> "Proton"), however for Wine you will need a patched version.

  * [NTSync](<https://www.youtube.com/watch?v=NjU4nyWyhU8>) \- In-kernel implementation of synchronization, that compared to ESync and FSync, NTsync closely emulates the behavior of MS Windows implementation, which [currently not implemented yet in upstream Wine](<https://gitlab.winehq.org/wine/wine/-/merge_requests/7226>), and not included in [Proton](<../zh-cn/Steam.html#Proton_Steam-Play> "Proton"), but require to be implemented in Wine or/and Proton to NTsync can work. However, out-of-tree [patches exist for both](<https://github.com/Frogging-Family/wine-tkg-git>). Usually is on par with FSync or smoother. NTSync is now implemented in kernel and require [Linux](<../zh-cn/%E5%86%85%E6%A0%B8.html> "Linux") 6.14 or newer. Also you should [manually load](<../zh-cn/Kernel_module.html#Automatic_module_loading> "Kernel module") "**ntsync** " Linux kernel module, because it disabled by default. For example:

    /etc/modules-load.d/ntsync.conf
    
    # Automaticaly load ntsync kernel module at every boot
    
    ntsync
    
**注意：** None of those options are now available in [wine](<https://archlinux.org/packages/?name=wine>)包, but NTsync maybe soon.

To enable ESync [Export](</wzh/index.php?title=Export&action=edit&redlink=1> "Export（页面不存在）") the following [environment variable](<../zh-cn/Environment_variable.html> "Environment variable") before running Wine: 
    
    WINEESYNC=1
    
Or for FSync with patched Wine: 
    
    WINEFSYNC=1
    
NTsync does not require setting an [environment variable](<../zh-cn/Environment_variable.html> "Environment variable"). 

Also [MangoHud](<../zh-cn/MangoHud.html> "MangoHud") can shows the absence or presence of ESync, FSync or NTsync in games if you have enabled an indication of **wsync** in its config file. 

###  取消注册已经存在的Wine档案关联

默认情况下，Wine 接管了许多格式的默认程序。一些（例如 `vbs` 或是 `chm` ）都是 Windows 独有的，并且用 Wine 打开他们是方便的。但是，很多其它的格式（例如 `gif`、`jpeg`、`txt`、`js` 在Wine的模拟 Internet Explorer 或 Notepad 中打开是烦人的 

Wine的档案关联都设定在 `~/.local/share/applications/` 作为 `wine-extension-_extension_.desktop` 档案。删除这些档案对应的就像你想的那样取消注册了。或者，删除所有的 wine 拓展： 
    
    $ rm -f ~/.local/share/applications/wine-extension*.desktop
    $ rm -f ~/.local/share/icons/hicolor/*/*/application-x-wine-extension*
    
接下来，删除旧缓存： 
    
    $ rm -f ~/.local/share/applications/mimeinfo.cache
    $ rm -f ~/.local/share/mime/packages/x-wine*
    $ rm -f ~/.local/share/mime/application/x-wine-extension*
    
并且，升级这些缓存： 
    
    $ update-desktop-database ~/.local/share/applications
    $ update-mime-database ~/.local/share/mime/
    
请注意，如果应用程序再次设置文件关联，Wine仍将创建新的文件关联，甚至重新创建文件关联。 

###  阻止 Wine 创建文件关联

**注意：** 必须对每个 Wine 前缀执行此操作，除非您选择更改 `/usr/share/wine/wine.inf`，否则不应更新文件关联。

这个方法避免建立档案类型关联，但是保留建立的 XDG .desktop 档案（你可能会在选单中看到它们）。 

如果你想阻止 wine 通过 winecfg 创建档案关联，你必须不检查桌面通讯选项卡下的“管理档案关联”复选框，见 [Wine FAQ](<https://gitlab.winehq.org/wine/wine/-/wikis/FAQ#how-can-i-prevent-wine-from-changing-the-filetype-associations-on-my-system-or-adding-unwanted-menu-entriesdesktop-links>)

为了创建相同的更改通过注册表，在以下的路径加入字符串值 `N` 来 `启用`。 
    
    HKEY_CURRENT_USER\Software\Wine\FileOpenAssociations
    
_你也许需要先创建键`FileOpenAssociations`！_

为了在命令行创建相同的改变，运行下面的指令： 
    
    $ wine reg add "HKEY_CURRENT_USER\Software\Wine\FileOpenAssociations" /v Enable /d N
    
如果你想去应用默认设置在新的 Wine 前缀，编辑 `/usr/share/wine/wine.inf` 并加入这一行到 `Services` 段下： 
    
    HKCU,"Software\Wine\FileOpenAssociations","Enable",2,"N"
    
为了防止包升级覆盖设置档案，创建一个 pacman 钩子来让这个变化自动进行： 
    
    /etc/pacman.d/hooks/stop-wine-associations.hook
    
    [Trigger]
    Operation = Install
    Operation = Upgrade
    Type = Path
    Target = usr/share/wine/wine.inf
    
    [Action]
    Description = Stopping Wine from hijacking file associations...
    When = PostTransaction
    Exec = /bin/sh -c '/usr/bin/grep -q "HKCU,\"Software\\\Wine\\\FileOpenAssociations\",\"Enable\",2,\"N\"" /usr/share/wine/wine.inf || /usr/bin/sed -i "s/\[Services\]/\[Services\]\nHKCU,\"Software\\\Wine\\\FileOpenAssociations\",\"Enable\",2,\"N\"/g" /usr/share/wine/wine.inf'

见 [Pacman#Hooks](<../zh-cn/Pacman.html#Hooks> "Pacman") 。 

###  自动使用 Wine 执行 Windows 程序

[wine](<https://archlinux.org/packages/?name=wine>)包 软件包会安装一个 _binfmt_ 文件，这可使你能够直接运行 Windows 程序，例如，` _./myprogram.exe_` 将与 `wine _./myprogram.exe_` 效果相同。服务默认在开机时启动，如果在安装 Wine 之后还没有重启过，[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `systemd-binfmt.service` 即可。 

**注意：** 确保 Windows 程序[可执行](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "Executable")，否则程序将不会运行。

###  双显示器具有不同的分辨率

如果您在双显示器设置与不同的显示分辨率方面有问题，这可能是缺少了 [lib32-libxrandr](<https://archlinux.org/packages/?name=lib32-libxrandr>)包。 

安装 [lib32-libxinerama](<https://archlinux.org/packages/?name=lib32-libxinerama>)包 也许可以解决 wine 中的双头问题（例如，最底部或右侧的显示器的程序中的按钮与选单不可被按下，该区域中应用程序的界面不可重绘，离开应用程序区域后拖动鼠标光标状态受阻）。 

###  烧录光盘

为了烧录 CD 或者是 DVD，你将需要加载`sg`[内核模块](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html> "内核模块")。 

###  正确的挂载光碟

一些程序会将光碟作为一个设备检查。他们可能只检查数据，在这种情况下，可将相应路径配置为“winecfg”中的 CD-ROM 驱动器。 

但是。其它程序将找到媒体名称或/和序列号，在这种情况下映像要用特殊的属性挂载。 

一些虚拟设备无法处理这些元数据，就像是基于 FUSE 的虚拟设备（譬如 Acetoneiso）。 [CDemu](<../zh-cn/CDemu.html> "CDemu") 将会正确的处理它。 

###  游戏内显示帧数

Wine 有一个内置的 FPS 检测器，在环境变量 `WINEDEBUG=fps` 设定的情况下，它会运行在所有图形程序上。这将会输出帧率到标准输出。你可以显示帧率到屏幕最上面通过 [xosd](<https://archlinux.org/packages/?name=xosd>)包 包中的 `osd_cat`。[winefps.sh](<https://gist.github.com/anonymous/844aefd70bb50bf72b35>) 为它的帮助脚本。 

###  在单独的用户帐户下运行 Wine

在一个专门创建的用户账户下运行Wine可能是可取的，以便减少对 Windows 应用程序访问你的主目录的担忧。 

第一步，建立一个[用户账户](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html> "用户账户")给Wine: 
    
    # useradd -m -s /bin/bash wineuser
    
现在切换到另一个 TTY，像平常一样启动你的X WM或DE，或者继续阅读...... 

**注意：** 以下方法仅在为Xorg启用root时有效。关于如何在主用户下执行`xhost`命令的更多信息，请参见[Xorg#Rootless Xorg](<../zh-cn/Xorg.html#Rootless_Xorg> "Xorg") 。

之后，为了使用这个新的用户账户打开Wine应用程序，你需要将这个新用户添加到X服务器的权限列表中。 
    
    $ xhost +SI:localuser:wineuser
    
最后，你可以通过以下命令来运行Wine，该命令使用`env`来启动Wine，并加入它所期望的环境变量。 
    
    $ sudo -u wineuser env HOME=/home/wineuser USER=wineuser USERNAME=wineuser LOGNAME=wineuser wine _arguments_
    
可以使用如下的shell脚本，使用Wine运行Windows应用程序的过程自动化： 
    
    /usr/local/bin/runaswine
    
    #!/bin/bash
    xhost +SI:localuser:wineuser
    sudo -u wineuser env HOME=/home/wineuser USER=wineuser USERNAME=wineuser LOGNAME=wineuser wine "$@"

Wine程序可以被通过以下指令启动： 
    
    $ runaswine _"C:\path\to\application.exe"_
    
为了在每次以其他用户身份运行Wine时不被要求输入密码，可以在sudoers文件中加入以下条目。` _mainuser_ ALL=(wineuser) NOPASSWD: ALL`。更多信息见[Sudo#Configuration](<../zh-cn/Sudo.html#Configuration> "Sudo")。 

建议以Wine用户身份运行`winecfg`，并在配置窗口的 "桌面集成 "部分删除Wine用户主目录以外的所有目录绑定，这样，使用Wine运行的程序就无法读取特殊用户主目录以外的任何文件。 

请记住，如果使用了[PulseAudio](<../zh-cn/PulseAudio.html> "PulseAudio")，那么在以这种方式运行的Wine程序中，音频可能将无法发挥作用。请参阅 [PulseAudio/Examples#Allowing multiple users to share a PulseAudio daemon](</wzh/index.php?title=PulseAudio/Examples&action=edit&redlink=1> "PulseAudio/Examples（页面不存在）") 以了解关于允许Wine用户访问主用户的PulseAudio daemon的信息。 

###  Tmpfs 上的临时目录

为了防止 Wine 将临时文件写到物理硬盘上，需要设置一个另外的位置，例如 _tmpfs_ 。删除 Wine 临时文件的默认目录并建立一个软链接： 
    
    $ rm -r ~/.wine/drive_c/users/$USER/Temp ~/.wine/drive_c/windows/temp
    $ ln -s /tmp/ ~/.wine/drive_c/users/$USER/Temp
    $ ln -s /tmp/ ~/.wine/drive_c/windows/temp
    
###  防止 Mono/Gecko 的安装

如果 Gecko 或/和 Mono 都不在系统或 Wine 前缀中，Wine 将提示从网路上下载他们。如果你并不需要 Gecko 或/和 Mono，你也许希望关闭这个提示，通过设置 `WINEDLLOVERRIDES` [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")为 `mscoree=d;mshtml=d`.。 

### Vulkan

默认的 wine Vulkan ICD 加载器在大多数程序中都工作地很好，但是不支持高级特性，例如 Vulkan 层。为使用这些特性，你需要安装官方的 Vulkan SDK，见原始的Vulkan补丁作者的 [GitHub page](<https://github.com/roderickc/wine-vulkan>) 的第二到四步。 

###  删除Wine文件绑定

因为安全因素，移除 Wine 绑定来让 Windows 程序无法直接从文件管理器或是浏览器（Firefox 提供直接使用 Wine 打开 EXE 文件的方法）或许是有用的。 

假如你想这么做，你需要在 `/etc/pacman.conf` 中加入下面的 [NoExtract](<../zh-cn/Pacman.html#%E5%9C%A8%E5%AE%89%E8%A3%85%E6%97%B6%E8%B7%B3%E8%BF%87%E6%96%87%E4%BB%B6> "NoExtract") 行： 
    
    NoExtract = usr/lib/binfmt.d/wine.conf
    NoExtract = usr/share/applications/wine.desktop
    
### WineASIO

如果你需要 Wine 下的专业的音频支持，你可以使用 [wineasio](<https://aur.archlinux.org/packages/wineasio/>)AUR 来提供一个给 wine 的 ASIO 界面来让你可以使用 [JACK](</wzh/index.php?title=JACK&action=edit&redlink=1> "JACK（页面不存在）")。 

为了使用 wineasio，你必须将自己加入`realtime`[用户组](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E7%94%A8%E6%88%B7%E7%BB%84%E7%AE%A1%E7%90%86> "用户组")。 

然后你需要注册 wineasio 到你的选定的 wine 前缀。注册32位或/和64位版本作为需要的： 
    
    $ regsvr32 /usr/lib32/wine/i386-windows/wineasio.dll
    $ wine64 regsvr32 /usr/lib/wine/x86_64-windows/wineasio.dll
    
##  疑难解答

见[用户指南](<https://gitlab.winehq.org/wine/wine/-/wikis/Wine-User's-Guide#troubleshooting--reporting-bugs>)和 [Wine FAQ](<https://gitlab.winehq.org/wine/wine/-/wikis/FAQ>) (特别注意这个 [Troubleshooting](<https://gitlab.winehq.org/wine/wine/-/wikis/FAQ#troubleshooting>) 选段)以参阅通用指南。 

也请将运行程序的建议也反馈到 [Wine AppDB](<https://appdb.winehq.org/>)。 

###  XWayland问题

如果你在 [XWayland](<../zh-cn/Wayland.html#XWayland> "Wayland") 下使用 wine，你可以在 winecfg 的显示菜单启用“模拟虚拟桌面”来避免以下的问题： 

  * 窗口闪动;
  * 错误的窗口位置;
  * 错误的鼠标位置和点击;
  * 键盘监察错误。

###  键盘输入不工作

这可能是由于窗口管理器没有切换焦点造成的。在 _winecfg_ 的 _图形_ 标签中，禁用'允许窗口管理器...'选项，或者用'模拟虚拟桌面'设置窗口模式。 

  * 有人建议切换所有的 "窗口设置"，点击 "应用"，然后把它们改回来。如果这不起作用，请尝试上述方法。

如果在取消应用程序的焦点后，键盘不能工作，请尝试编辑注册表。 

  * 在 `HKEY_CURRENT_USER\Software\Wine\X11 Driver` 下，添加一个字符串值 `UseTakeFocus` 并将其设置为 `N` 。
  * 另外，你也可以用 winetricks 来设置这个值。

    $ winetricks usetakefocus=n

或者使用wine注册表 
    
    $ wine reg add 'HKEY_CURRENT_USER\Software\Wine\X11 Driver' /t REG_SZ /v UseTakeFocus /d N /f

###  应用程序启动失败

有些旧的游戏和应用程序会假设当前[工作目录](<https://en.wikipedia.org/wiki/Working_directory> "wikipedia:Working directory")与可执行文件所在目录相同。如果从其他位置启动这些可执行文件，可能会导致它们无法正常启动。在运行 Wine 之前，使用 `cd _path_containing_exe_` 来排除这种可能性。 

##  参见

  * [Wine 主页](<https://www.winehq.org/>)
  * [Wine 维基](<https://gitlab.winehq.org/wine/wine/-/wikis/home>)
  * [Wine 程序数据库 (AppDB)](<https://appdb.winehq.org/>) \- 关于运行一些特定的 Windows 程序的讯息 (已知问题、指北、等级、其它关于程序的讯息)
  * [Wine 论坛](<https://forum.winehq.org/>) \- 一个问问题的好地方在你看了 FAQ 和 AppDB 后。
  * [Gentoo:Wine](<https://wiki.gentoo.org/wiki/Wine> "gentoo:Wine")
  * [Darling](<https://www.darlinghq.org/>) \- 一个模拟 MacOS 程序的小项目
  * [WineASIO](<https://github.com/wineasio/wineasio>) \- WineASIO 项目的 Github Page，有更多的讯息。
