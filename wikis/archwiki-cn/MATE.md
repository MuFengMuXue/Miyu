**翻译状态：**

  * 本文（或部分内容）译自 [MATE](<https://wiki.archlinux.org/title/MATE> "arch:MATE")，最近一次同步于 2023-01-09，若英文版本有所[更改](<https://wiki.archlinux.org/title/MATE?diff=0&oldid=763350>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/MATE_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [GNOME](<../zh-cn/GNOME.html> "GNOME")
  * [Cinnamon](<../zh-cn/Cinnamon.html> "Cinnamon")
  * [Desktop environment](<../zh-cn/Desktop_environment.html> "Desktop environment")
  * [Display manager](<../zh-cn/Display_manager.html> "Display manager")
  * [Uniform look for Qt and GTK applications](<../zh-cn/Uniform_look_for_Qt_and_GTK_applications.html> "Uniform look for Qt and GTK applications")

摘自 [MATE 主页](<https://mate-desktop.org/>): 

    The MATE 桌面环境是 GNOME 2 的延续，为 Linux 及其他类 Unix 系统提供直观和有吸引力的桌面。MATE is [开发社区非常活跃](<https://github.com/mate-desktop>)，添加很多新的功能并保留传统使用习惯。

##  安装

可以通过如下方式安装[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") MATE: 

  * [mate](<https://archlinux.org/groups/x86_64/mate/>)包组 包含标准 MATE 需要的核心桌面环境，包含 [marco](<https://archlinux.org/packages/?name=marco>)包, [mate-panel](<https://archlinux.org/packages/?name=mate-panel>)包 and [mate-session-manager](<https://archlinux.org/packages/?name=mate-session-manager>)包 等。
  * [mate-extra](<https://archlinux.org/groups/x86_64/mate-extra/>)包组 包含额外的工具和程序，这些程序可以和 MATE 桌面协同工作。仅安装 [mate-extra](<https://archlinux.org/groups/x86_64/mate-extra/>)包组 时并不会通过依赖引入全部 [mate](<https://archlinux.org/groups/x86_64/mate/>)包组 。要安装全部 MATE 软件包，请同时安装两个软件包组。

###  MATE 应用程序

MATE 大部分由 GNOME 2 软件和更加组成，这些软件会被重命名以避免和 GNOME3 版本冲突，下面是名称对比： 

应用程序  | GNOME 2  | MATE   
---|---|---  
菜单编辑器  | Alacarte  |  [mozo](<https://archlinux.org/packages/?name=mozo>)包  
文件管理器  | Nautilus  |  [caja](<https://archlinux.org/packages/?name=caja>)包  
窗口管理器  | Metacity  |  [marco](<https://archlinux.org/packages/?name=marco>)包  
文本编辑器  | Gedit  |  [pluma](<https://archlinux.org/packages/?name=pluma>)包  
图片  | Eye of GNOME  | Eye of MATE ([eom](<https://archlinux.org/packages/?name=eom>)包)   
Document viewer  | Evince  |  [atril](<https://archlinux.org/packages/?name=atril>)包  
归档管理器  | File Roller  |  [engrampa](<https://archlinux.org/packages/?name=engrampa>)包  
  
其他以 GNOME 开头的核心程序 (比如 GNOME Terminal, GNOME Panel, GNOME Menus 等) 会将前缀改为 MATE, 变成 MATE Panel, MATE Menus 等。 

###  额外的 MATE 软件包

有些非官方 MATE 程序是由 MATE 社区开发维护，并没有包含在 [mate](<https://archlinux.org/groups/x86_64/mate/>)包组 或 [mate-extra](<https://archlinux.org/groups/x86_64/mate-extra/>)包组 中。 

  * **Dock Applet** — MATE面板的应用程序坞。

     <https://github.com/robint99/dock-applet> || [mate-applet-dock](<https://archlinux.org/packages/?name=mate-applet-dock>)包

  * **Online Radio Applet** — 一个用于MATE面板的小程序，可以让您通过单击一次即可播放您最喜欢的在线广播电台。

     <http://www.zavedil.com/online-radio-applet/> || [mate-applet-streamer](<https://archlinux.org/packages/?name=mate-applet-streamer>)包

  * **MATE Menu** — MATE面板的高级菜单，是MintMenu的一个分支。

     <https://github.com/ubuntu-mate/mate-menu> || [mate-menu](<https://aur.archlinux.org/packages/mate-menu/>)AUR

  * **MATE Tweak** — MATE的调整工具，是mintDesktop的一个分支。

     <https://github.com/ubuntu-mate/mate-tweak> || [mate-tweak](<https://aur.archlinux.org/packages/mate-tweak/>)AUR

  * **BriskMenu** — SolusOS分发的MATE桌面环境的现代高效菜单。

     <https://github.com/getsolus/brisk-menu> || [brisk-menu](<https://aur.archlinux.org/packages/brisk-menu/>)AUR

要使用 Caja 的高级功能，需要安装额外的软件包，请参考 [File manager functionality](<../zh-cn/File_manager_functionality.html> "File manager functionality"). 

##  启动

在[显示管理器](<../zh-cn/Display_manager.html> "Display manager")中选择 _MATE_ 即可， 

或者是手动方式，要用 [startx](<../zh-cn/Xinit.html> "Startx") 启动 MATE,将 `exec mate-session` 加入 `~/.xinitrc` 文件. 

##  配置

MATE可以通过其提供的 [mate-control-center](<https://archlinux.org/packages/?name=mate-control-center>)包 包中的 _Control Center_ 应用程序 (_mate-control-center_) 进行配置。要管理某些硬件，您可能需要安装其他工具。 

音频
     [mate-media](<https://archlinux.org/packages/?name=mate-media>)包 包支持 [ALSA](<../zh-cn/ALSA.html> "ALSA") 和 [PulseAudio](<../zh-cn/PulseAudio.html> "PulseAudio") 后端.
蓝牙
    要支持 [Bluetooth](<../zh-cn/%E8%93%9D%E7%89%99.html> "Bluetooth") 设备，请安装 [blueman](<https://archlinux.org/packages/?name=blueman>)包 。 请参见 [Blueman](</wzh/index.php?title=Blueman&action=edit&redlink=1> "Blueman（页面不存在）") 的相关文档。
网络
    要配置网络，请安装 [network-manager-applet](<https://archlinux.org/packages/?name=network-manager-applet>)包 包。请参见 [NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager")。
电源
    UPower 后端受到 [mate-power-manager](<https://archlinux.org/packages/?name=mate-power-manager>)包 包的支持。
打印机
    要配置打印机，请安装 [system-config-printer](<https://archlinux.org/packages/?name=system-config-printer>)包 包。

###  无障碍

MATE非常适合视力或行动受限的个人使用。[Install](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") [orca](<https://archlinux.org/packages/?name=orca>)包, [espeak](<https://aur.archlinux.org/packages/espeak/>)AUR (为盲人或视力受损者设计的屏幕阅读器) 和 [onboard](<https://archlinux.org/packages/?name=onboard>)包 (对于行动受限用户而言非常有用的屏幕键盘) 

在首次启动MATE之前，以需要辅助功能的用户身份输入以下命令： 
    
    $ gsettings set org.mate.interface accessibility true
    
一旦你启动MATE，你可以通过 _System > Preferences > Assistive Technologies_ 配置无障碍应用。 不过，如果你需要使用Orca，你需要在 `Alt-F2` 运行窗口中运行它，以开始获得语音功能。 

###  提醒

电池放电

要禁用电池放电的通知，请运行以下命令： 
    
    $ gsettings set org.mate.power-manager notify-discharging false
    
亮度

请参见 [Backlight#Kernel command-line options](<../zh-cn/%E8%83%8C%E5%85%89.html#Kernel_command-line_options> "Backlight")。 

##  提示与技巧

###  禁用合成

默认情况下，合成功能已启用。要禁用它，您可以在系统偏好设置的 _Look and Feel > Windows > General_ 中勾选 _Enable software compositing window manager_ 。 另外，您也可以从终端运行以下命令来禁用合成功能： 
    
    $ gsettings set org.mate.Marco.general compositing-manager false
    
###  禁用新窗口居中

默认情况下，新窗口将居中显示。要禁用新窗口居中，请在系统偏好设置的 _Windows > Placement_ 中勾选 _Center new windows_ 。您也可以从终端运行以下命令来禁用新窗口居中： 
    
    $ gsettings set org.mate.Marco.general center-new-windows false
    
###  禁用窗口吸附

窗口吸附功能默认已启用。要禁用它，请在系统偏好设置的 _Windows > Placement_ 勾选 _Enable window tiling_ 。另外，您也可以从终端运行以下命令来禁用窗口吸附功能： 
    
    $ gsettings set org.mate.Marco.general allow-tiling false
    
###  取消最大化窗口的装饰

使用 [mate-tweak](<https://aur.archlinux.org/packages/mate-tweak/>)AUR 工具可以隐藏最大化窗口的装饰;安装后，在系统偏好设置的 _Look and Feel > MATE Tweak > Windows_ 并在 _Window Behaviour_ 部分中启用 _Undecorate maximized windows_ 。 

**提示：** 如果此选项变为灰色且不可用，请确保已安装 [mate-netbook](<https://archlinux.org/packages/?name=mate-netbook>)包 包。

###  显示或隐藏桌面图标

默认情况下，MATE在桌面上显示多个图标： 桌面目录的内容、计算机、主目录和网络目录、废纸篓和已挂载的驱动器。您可以使用 `gsettings` 逐个或全部显示或隐藏它们。 

####  隐藏所有桌面图标
    
    $ gsettings set org.mate.background show-desktop-icons false
    
这样做可能会导致辅助显示器上出现一些图形异常。 

####  隐藏个别图标

隐藏电脑图标： 
    
    $ gsettings set org.mate.caja.desktop computer-icon-visible false
    
隐藏用户目录图标： 
    
    $ gsettings set org.mate.caja.desktop home-icon-visible false
    
隐藏网络图标： 
    
    $ gsettings set org.mate.caja.desktop network-icon-visible false
    
隐藏回收站图标 
    
    $ gsettings set org.mate.caja.desktop trash-icon-visible false
    
隐藏已挂载的卷： 
    
    $ gsettings set org.mate.caja.desktop volumes-visible false
    
将 `false` 替换成 `true` ，图标将重新出现。 

###  使用不同的窗口管理器

_marco_ 窗口管理器可以通过以下任一方法被另一个窗口管理器取代： 

使用gsettings（推荐）

执行以下操作以指定MATE的不同窗口管理器： 
    
    $ gsettings set org.mate.session.required-components windowmanager _wm-name_
    
使用MATE会话自动启动

您可以使用 _mate-session-properties_ 自动启动所选择的窗口管理器。这意味着在登录时，自动启动的窗口管理器将替代默认的窗口管理器。 在系统偏好设置中导航到 _Startup Applications_ 。在对话框中点击 _Add._ 。命令应采用以下语法： `_wm-name_ --replace`。 

###  阻止Caja管理桌面

执行以下操作以防止Caja管理桌面： 
    
    $ gsettings set org.mate.background show-desktop-icons false
    $ killall caja  # Caja will be restarted by session manager
    
###  更改窗口装饰按钮顺序

您可以使用图形化的dconf-editor或命令行工具gsettings来更改按钮顺序： 
    
    $ gsettings set org.mate.Marco.general button-layout 'close,maximize,minimize:'
    
将 **menu** , **close** , **minimize** 和 **maximize** 以您希望的顺序使用逗号分隔开。冒号用于指定窗口按钮在标题栏的哪一侧显示，并且必须在更改时使用。 

###  在驱动器挂载后自动打开文件管理器

默认情况下，MATE 在挂载驱动器时会自动打开一个新的文件管理器窗口。要禁用此功能： 
    
    $ gsettings set org.mate.media-handling automount-open false
    
要禁用自动挂载： 
    
    $ gsettings set org.mate.media-handling automount false
    
###  屏幕保护

MATE使用 [mate-screensaver](<https://archlinux.org/packages/?name=mate-screensaver>)包 来锁定您的会话。默认情况下，可用的屏幕保护程序数量有限。要增加更多屏幕保护程序的选择，请安装 [mate-screensaver-hacks](<https://aur.archlinux.org/packages/mate-screensaver-hacks/>)AUR 包。这将允许您在 [mate-screensaver](<https://archlinux.org/packages/?name=mate-screensaver>)包 包中使用 [XScreenSaver](<../zh-cn/XScreenSaver.html> "XScreenSaver") 的屏幕保护程序。 

###  在Caja中的空间视图

为了确保每个新文件夹以新窗口的形式打开（也称为空间视图），打开Caja的首选项对话框，点击行为标签，并选中“在单独窗口中打开每个文件夹”的选项。或者，执行以下命令以达到相同的效果： 
    
    $ gsettings set org.mate.caja.preferences always-use-browser false
    
###  更改字体DPI设置

您可以通过右键单击桌面，选择 _Change desktop background > Fonts > Details > Resolution_ 来更改MATE中字体的DPI（每英寸点数）。在弹出的窗口中，您可以调整字体的分辨率以改变其大小和清晰度。 

###  更改应用程序菜单图标

默认情况下，应用程序菜单图标设置为 `start-here`。要使用其他图标，请将图标复制到 `/usr/local/share/pixmaps` 等文件夹中，并执行以下操作： 
    
    $ gsettings set org.mate.panel.menubar icon-name _icon_
    
其中， _icon_ 是你的图标的名字。在图标名字中不要包括文件扩展名。最后，重新启动MATE面板。 

###  面板速度设置

隐藏/显示延迟

要调整面板在启用自动隐藏时消失或重新出现所需的时间，请执行以下操作： 
    
    $ dconf write /org/mate/panel/toplevels/_panel_ /(un)hide-delay _time_
    
其中， _panel_ 是 _top_ 或 _bottom_ ， _time_ 是以毫秒为单位的值，例如300。 

动画速度

要设置面板动画发生的速度，请执行以下操作： 
    
    $ dconf write /org/mate/panel/toplevels/_panel_ /animation-speed _value_
    
其中 _panel_ 可以是 _top_ 或 _bottom_ ， _value_ 可以是 `"'fast'"`, `"'medium'"` 或 `"'slow'"` 之一。 

###  将终端设置为 caja-open-terminal

`caja-open-terminal` 扩展使用GSettings确定使用哪个终端 - _mate-terminal_ 是默认值。要更改将使用的终端，请运行以下命令。 
    
    $ gsettings set org.mate.applications-terminal exec _my-terminal_
    
其中 _my-terminal_ 是要启动的终端可执行文件的名称，例如： _xterm_ 。 

##  故障排除

###  切换合成特效

在使用NVIDIA专有驱动程序和合成窗口管理器的环境中工作时，某些软件可能会出现渲染图形的问题。 

为了方便切换合成功能，请将以下脚本保存在Home目录中的某个位置： 
    
    ~/.scripts/compositing.sh
    
    #!/bin/sh
    if [ "$(gsettings get org.mate.Marco.general compositing-manager)" = "true" ]
    then
      gsettings set org.mate.Marco.general compositing-manager false
    else
      gsettings set org.mate.Marco.general compositing-manager true
    fi

然后创建一个自定义的键盘快捷键，用于执行该文件，例如 `Ctrl+Alt+C`，将其设置为 `sh ~/.scripts/compositing.sh`。 

###  为合成特效启用垂直同步

MATE的窗口管理器marco通过DRI3/Xpresent支持无撕裂的软件合成。 [[1]](<https://github.com/mate-desktop/marco/issues/326>)

如果您的显卡驱动程序不支持DRI3（例如Nvidia专有驱动程序）， _marco_ 不支持通过 _OpenGL_ 进行垂直同步， 这可能会导致启用合成时出现视频撕裂。 [[2]](<https://github.com/mate-desktop/marco/issues/91>) 在这种情况下，考虑使用 [picom](<../zh-cn/Picom.html> "Picom") 等支持OpenGL的不同的 [composite manager](</wzh/index.php?title=Composite_manager&action=edit&redlink=1> "Composite manager（页面不存在）")。 

###  保持光标主题一致

请参见 [Cursor themes#Desktop environments](<../zh-cn/Cursor_themes.html#Desktop_environments> "Cursor themes"). 

###  在 LightDM 中使用渐变背景

如果您希望将默认的 MATE (1.8) _Stripes_ 背景同时用作 LightDM 的背景，以实现从LightDM到MATE的平滑过渡，您会发现默认背景是根据灰度PNG图像动态生成的，上面再添加了一个从蓝色到绿色的垂直渐变色，而这是LightDM当前不支持的。如果您坚持要做这个操作，可以通过临时设置 `/org/mate/desktop/background/show-desktop-icons` 为 `false` 来解决，可以通过`System Tools` 菜单中的 `dconf-editor` 工具或者通过运行命令来进行设置。 
    
    $ gsettings set org.mate.background show-desktop-icons false
    
从 Alt-F2 `Run Application` 对话框中运行 `killall mate-panel`，并在面板重新出现之前按下 `Print Screen` 键。 然后，您会看到一个 `Save As` 对话框，以保存您所需的完整渲染、屏幕大小的PNG图像，以供LightDM使用。运行 
    
    $ gsettings set org.mate.background show-desktop-icons true
    
会使您的桌面图标重新出现，如果有需要的话。 

###  启用面板阴影

由于竞争条件，在登录到MATE桌面后，即使启用了合成，面板阴影也不会显示。 [[3]](<https://github.com/mate-desktop/mate-panel/issues/193>)

复制到 `/usr/share/applications/marco.desktop` 并添加延迟: 
    
    ~/.local/share/applications/marco.desktop
    
    X-MATE-Autostart-Phase=**Applications**
    **X-MATE-Autostart-Delay=2**
    X-MATE-Provides=windowmanager
    X-MATE-Autostart-Notify=true

**注意：** Delays are only allowed in the applications phase, hence `X-MATE-Autostart-Phase` must be set to `Applications`.

如果没有效果，请增加延迟时间的长度。 

###  禁用任务栏的滚动功能

MATE面板窗口列表的一个功能是可以使用鼠标或触摸板滚动浏览窗口。对于一些人来说，这个功能可能会带来麻烦，因为有可能意外地滚动浏览窗口。 

虽然无法通过MATE的设置禁用此功能，但可以通过使用 [Arch Build System](<../zh-cn/Arch_Build_System.html> "Arch Build System") 来对 [libwnck3](<https://archlinux.org/packages/?name=libwnck3>)包 进行修补来禁用此功能 ; 在这种情况下，使用以下[补丁](<https://pastebin.com/raw/q66p3dtj>)重新构建libwnck3。有关在应用补丁的情况下重新构建软件包的更多信息，请参阅 [Patching in ABS#Applying patches](</wzh/index.php?title=Patching_in_ABS&action=edit&redlink=1> "Patching in ABS（页面不存在）")。 

###  登录注销/关机延迟由 at-spi-registryd 引起

在登出或关机时，您可能会遇到一个弹出窗口，显示 _A program is still running: at-spi-registryd.desktop_ 。作为解决方法，您可以阻止 _at-spi-registryd_ 启动 - 请参见 [GTK#Suppress warning about accessibility bus](<../zh-cn/GTK.html#Suppress_warning_about_accessibility_bus> "GTK") \- 但这可能会影响某些辅助功能。 

###  Caja的文本文件预览

由于迁移到GTK 3，该功能不再起作用。 [[4]](<https://github.com/mate-desktop/caja/issues/1047>)

###  GTK 2 应用似乎忽略了默认的 MATE 主题

[mate-themes](<https://archlinux.org/packages/?name=mate-themes>)包 包附带的主题需要可选依赖项 [gtk-engines](<https://archlinux.org/packages/?name=gtk-engines>)包 包和 [gtk-engine-murrine](<https://archlinux.org/packages/?name=gtk-engine-murrine>)包 包，以使GTK 2主题正常工作。 

###  CSD 应用程序上的额外装饰

当CSD应用程序（如Firefox、Visual Studio Code等）取消最大化时，会出现额外的装饰。 [[5]](<https://github.com/mate-desktop/mate-netbook/issues/14>)

卸载 [mate-netbook](<https://archlinux.org/packages/?name=mate-netbook>)包 包可以解决这个问题。 

###  键盘布局选择器

当启用多个键盘布局时，系统托盘中会显示一个布局选择图标。但是由于一个错误 ([[6]](<https://github.com/mate-desktop/libmatekbd/issues/28>)), 根据当前使用的主题，有时会显示为白色字体在明亮的背景上 (或者在其他几乎无法辨认的配置中，例如绿色字体)。 

可以通过手动设置字体颜色来解决这个问题 (例如，将其设置为黑色的 `'0 0 0'` ): 
    
    $ gsettings set org.mate.peripherals-keyboard-xkb.indicator foreground-color '0 0 0'
    
##  参见

  * [MATE 主页](<https://mate-desktop.org>)
  * [MATE Arch Linux维基](<https://wiki.mate-desktop.org/#!pages/./archlinux_custom_repo.md>)
  * [MATE 桌面截图](<https://mate-desktop.org/gallery/1.8/>)
  * [MATE 桌面环境](<https://bbs.archlinux.org/viewtopic.php?pid=1018647>) \- 关于MATE的Arch Linux论坛讨论（该帖子在2017年1月5日关闭）
