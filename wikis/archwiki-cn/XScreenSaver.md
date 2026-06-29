**翻译状态：**

  * 本文（或部分内容）译自 [Xscreensaver](<https://wiki.archlinux.org/title/Xscreensaver> "arch:Xscreensaver")，最近一次同步于 2022-05-22，若英文版本有所[更改](<https://wiki.archlinux.org/title/Xscreensaver?diff=0&oldid=730370>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Xscreensaver_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [DPMS](<../zh-cn/Display_Power_Management_Signaling.html> "DPMS")
  * [Xresources](</wzh/index.php?title=Xresources&action=edit&redlink=1> "Xresources（页面不存在）")
  * [Session lock](</wzh/index.php?title=Session_lock&action=edit&redlink=1> "Session lock（页面不存在）")
  * [List of applications#Screen lockers](<../zh-cn/List_of_applications.html#Screen_lockers> "List of applications")

[XScreenSaver](<https://www.jwz.org/xscreensaver/>) 是 X 窗口系统的屏保和锁屏工具。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [xscreensaver](<https://archlinux.org/packages/?name=xscreensaver>)包 包。 

如果安装 [xscreensaver-arch-logo](<https://aur.archlinux.org/packages/xscreensaver-arch-logo/>)AUR 包，可以获得有 Arch Linux 标志的外观。 

##  配置

大多数选项都可以通过运行 _xscreensaver-settings_ 来逐个用户配置的。 _xscreensaver-settings_ 会将所选的配置写入 `~/.xscreensaver`，并丢弃对文件的任何手动修改。 全局选项定义在 `/usr/share/X11/app-defaults/XScreenSaver` 中。 

至少从 XScreenSaver 5.22 开始，有了另一种方法来编辑 XScreenSaver 的用户配置：使用 [Xresources](</wzh/index.php?title=Xresources&action=edit&redlink=1> "Xresources（页面不存在）")。 

###  主题

从 6.0 版本开始，XScreenSaver 预装了一些主题，选择方式： 

  * _xscreensaver-settings_
  * 修改 `~/.xscreensaver` 配置文件中的 `dialogTheme` 选项 (`dialogTheme: _themename_`
  * 使用 X resources: `xscreensaver-auth.dialogTheme: _themename_`).

用 X resources 可以自定义主题，下面的例子修改了颜色和字体。如果使用的是非默认主题，请将 `default` 修改为所选主题的小写名字，使用问号 (`?`) 会影响所有主题: 
    
    ~/.Xresources
    
    ! Font for regular texts.
    	
    ! Font names are case-insensitive.
    	
    ! You can use a comma-separated list of fonts to set a fallback font.
    	
    xscreensaver-auth.default.Dialog.bodyFont: times new roman 12, dejavu serif 12
    	
    ! Window background color. You can use color names.
    	
    xscreensaver-auth.default.Dialog.background: black
    	
    ! Main text color. You can also use HEX color codes.
    	
    xscreensaver-auth.default.Dialog.foreground: #ffffff
    	
在 `/usr/share/X11/app-defaults/XScreenSaver` 中可以查看 X resources. 修改后请记得[重新加载所有资源文件](<../zh-cn/X_resources.html#Load_resource_file> "X resources")。 

###  DPMS 和挂起设置

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** "overrides DPMS" 并不清晰 - _xscreensaver_ 做了相当于 `xset s 0 0` 的工作，并使用自己的定时器来处理各种动画，但将 DPMS timeout 设置为 _Display Power Management_ 中的值。（在[Talk:XScreenSaver](<../zh-cn/Talk:XScreenSaver.html>)讨论）

XScreenSaver 独立于 X 本身进行显示设备的电源管理（[DPMS](<../zh-cn/Display_Power_Management_Signaling.html> "DPMS")），会覆盖 X 本身的设置。要配置挂起、待机、关闭显示器等的时间，请使用 _xscreensaver-demo_ 或手动编辑配置文件，例如 ~/.xscreensaver。 
    
    timeout:	1:00:00
    cycle:		0:05:00
    lock:		False
    lockTimeout:	0:00:00
    passwdTimeout:	0:00:30
    fade:		True
    unfade:		False
    fadeSeconds:	0:00:03
    fadeTicks:	20
    dpmsEnabled:	True
    dpmsStandby:	2:00:00
    dpmsSuspend:	2:00:00
    dpmsOff:	4:00:00
    
可通过启动 _xscreensaver-demo_ _Mode_ 设置，选择 _Disable Screen Saver_ 禁用 DPMS 和屏幕挂起。 

**注意：** 如果 _xscreensaver-demo_ 中的 _Lock Screen After_ 被勾选并设为 0 分钟，则屏幕将在空白后立即锁定。如果不勾选 _Power Manager Enabled_ ，DPMS 将被禁用；这并不意味着 XScreenSaver 会放弃对 DPMS 设置的控制。

##  使用

要启动 XScreenSaver，请使用 `-no-splash` 选项。有关完整的选项列表，请参阅 1}。 

在 [Xfce](<../zh-cn/Xfce.html> "Xfce")， [LXDE](<../zh-cn/LXDE.html> "LXDE") 和 [LXQt](<../zh-cn/LXQt.html> "LXQt") 环境中, 如果 XScreenSaver 可用，XScreenSaver 就会自动启动 - 且无需进一步操作。对于其他环境，请参阅[自动启动](<../zh-cn/%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8.html> "Autostarting")。 

如果要立即触发 _xscreensaver_ ，如果它正在运行，并锁定了屏幕，请执行以下命令： 
    
    $ xscreensaver-command -lock
    
[KDE Plasma](<../zh-cn/KDE_Plasma.html> "KDE Plasma") 中的屏保由 _ksmserver_ 控制，这会和 XScreenSaver 产生冲突，要禁用它，需要[在 KDE 中启动服务](<../zh-cn/KDE.html#systemd_startup> "KDE")并修改 `plasma-ksmserver.service` 为: 
    
    ~/.config/systemd/user/plasma-ksmserver.service.d/override.conf
    
    [Service]
    ExecStart=
    ExecStart=/usr/bin/ksmserver --no-lockscreen

重新登录， XScreenSaver 就会正常工作，更多信息请参考 [xscreensaver(1) § INSTALLING XSCREENSAVER ON KDE](<https://man.archlinux.org/man/xscreensaver.1#INSTALLING_XSCREENSAVER_ON_KDE>)。 

###  锁定挂起

XScreenSaver 提供了一个名为 _xscreensaver-systemd_ 的工具，可以处理来自 [systemd](<../zh-cn/Systemd.html> "Systemd") 的 [D-Bus](<../zh-cn/D-Bus.html> "D-Bus") 信号 `PrepareForSleep`, 并在挂起和休眠的时候自动锁定屏幕。这个程序会和 _xscreensaver_ 一起启动，无需额外设置。详情请参考 [xscreensaver-systemd(6)](<https://man.archlinux.org/man/xscreensaver-systemd.6>)。 

这个工具处理不了 `loginctl lock-session`。要处理这种情况，请参阅 [Power management#xss-lock](<../zh-cn/Power_management.html#xss-lock> "Power management"). 请使用 `--ignore-sleep` 选项，因为 _xscreensaver-systemd_ 已经处理了挂起和休眠事件。 
    
    $ xss-lock --ignore-sleep -- xscreensaver-command -lock
    
请将 XScreenSaver 的淡出时间设置为 0。 

###  从锁屏画面切换登录用户

**警告：** 当使用 GDM 或 LightDM 这样的显示管理器切换用户时，XScreenSaver 不会锁定原始会话，只需将 TTY 切换到相关会话即可，无需密码即可访问。如果你使用的是 LightDM，请安装[light-locker](<https://archlinux.org/packages/?name=light-locker>)包，然后与 XScreenSaver 一起运行。另外，也可以使用其他的屏幕锁定程序——参见 [List of applications/Security#Screen lockers](<../zh-cn/List_of_applications/Security.html#Screen_lockers> "List of applications/Security")。

By default, XScreenSaver's _New Login_ button in the lock screen will call `/usr/bin/gdmflexiserver` to switch users. [Display manager](<../zh-cn/Display_manager.html> "Display manager")s other than [GDM](<../zh-cn/GDM.html> "GDM") that support user switching require a different command. 

默认情况下，XScreenSaver 锁定屏幕中的 _New Login_ 按钮会启动 `/usr/bin/gdmflexiserver` 进行用户切换。除了 [GDM](<../zh-cn/GDM.html> "GDM") 外，其他支持用户切换的[显示管理器](<../zh-cn/Display_manager.html> "Display manager")需要使用不同的命令。 

**提示：** 将 _xscreensensaver.newLoginCommand:_ 添加到 `~/.Xresources`，而将参数留空将使 _New Login_ 按钮消失。

由于 `~/.xscreensensaver` 中的修改被 _xscreensaver-demo_ [丢弃](<#%E9%85%8D%E7%BD%AE>)，故本节中使用了 ~/.Xresources。 

#### LXDM

使用 LXDM 的切换用户功能： 
    
    xscreensaver-auth.default.*.newLoginCommand: lxdm -c USER_SWITCH
    
#### LightDM

使用 [LightDM](<../zh-cn/LightDM.html> "LightDM") 的切换用户功能： 
    
    xscreensaver-auth.default.*.newLoginCommand: dm-tool switch-to-greeter
    
**注意：** 如果你用这个切换到已经登录的用户，你可能需要输入两次密码（一次是为LightDM，一次是为你登录的用户的 XScreenSaver 对话框）。

#### SDDM

[SDDM](<../zh-cn/SDDM.html> "SDDM") 不支持用户切换 [[1]](<https://github.com/sddm/sddm/issues/579>)。可以尝试用 [using dbus-send](<https://github.com/sddm/sddm/issues/824>) 调用 `SwitchToGreeter` 方法，目前可能无法正常工作。 

##  提示和技巧

###  在媒体播放时禁用

Starting from version 5.45, the _xscreensaver-systemd_ utility implements the [D-Bus](<../zh-cn/D-Bus.html> "D-Bus") ScreenSaver interface. It is started automatically with _xscreensaver_ , so most applications should properly disable the screensaver without additional configuration. However, some applications do not support D-Bus or use another interfaces. 

#### mpv

默认情况下，[mpv](<../zh-cn/Mpv.html> "Mpv") 会在启动时关闭屏幕保护程序，并在退出时再次开启。当播放器暂停时，屏幕保护程序总是能被重新启用。该选项可以在 _mpv_ 的配置文件中控制，位于 `~/.config/mpv/mpv/mpv.conf`： 
    
    stop-screensaver = "yes"
    
然而这并不是所有的视频输出或平台都会支持。如果你遇到了一些问题，你可以使用 Lua 脚本来手动关闭屏幕保护程序。在 `~/.config/mpv/scripts/xscreensaver.lua` 中创建一个文件，其中包含以下内容： 
    
    local utils = require 'mp.utils'
    mp.add_periodic_timer(30, function()
        utils.subprocess({args={"xscreensaver-command", "-deactivate"}})
    end)
    
上面的脚本会每隔30秒调用 `xscreensaver-command -deactivate`。 

#### mplayer

在 `~/.mplayer/config` 中添加以下内容： 
    
    heartbeat-cmd="xscreensaver-command -deactivate >&- 2>&- &"
    
#### Kodi

[Kodi](<../zh-cn/Kodi.html> "Kodi") 不支持禁用 XScreenSaver （它使用自己的屏幕保护程序）。为了实现禁用，请[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [kodi-prevent-xscreensaver](<https://aur.archlinux.org/packages/kodi-prevent-xscreensaver/>)AUR 包，或者尝试使用从 <https://sourceforge.net/projects/osscreensavermanager/> 下载的 Kodi 扩展。 

####  浏览 HTML5 video/Flash

[Firefox](<../zh-cn/Firefox.html> "Firefox") supports the D-Bus ScreenSaver interface and should disable the screensaver during HTML5 video playback. 

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** The chromium exception was added without reference and disputed. Is it reproducible?（在 [Talk:XScreenSaver#loginctl, chromium, resources](</wzh/index.php?title=Talk:XScreenSaver&action=edit&redlink=1> "Talk:XScreenSaver（页面不存在）") 中讨论）

[Chromium](<../zh-cn/Chromium.html> "Chromium") also supports it, but uses the GNOME Session interface when available, so XScreenSaver will not be disabled in some [desktop environment](<../zh-cn/Desktop_environment.html> "Desktop environment")s such as [GNOME](<../zh-cn/GNOME.html> "GNOME") and [MATE](<../zh-cn/MATE.html> "MATE"). 

If you are experiencing problems, you can try a script named [lightsonplus](<https://github.com/devkral/lightsonplus>) with support for Firefox's Flash plugin, Chromium's Flash plugin, HTML5 fullscreen video in Firefox and Chromium, MPlayer, and VLC. 

###  动态壁纸

可以在后台运行 `xscreensaver`，就像壁纸一样。首先，中断一切控制背景的进程（根窗口）。 

然后，找到所需的 XScreenSaver 可执行文件（通常在 `/usr/lib/xscreensaver/` 中），并使用 `-root` 选项运行它，例如： 
    
    $ /usr/lib/xscreensaver/glslideshow -root &
    
**注意：** 如果 [xcompmgr](<../zh-cn/Xcompmgr.html> "Xcompmgr") 或 [picom](<../zh-cn/Picom.html> "Picom") 导致问题，请[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [shantz-xwinwrap-bzr](<https://aur.archlinux.org/packages/shantz-xwinwrap-bzr/>)AUR 包，然后运行： 
    
    $ xwinwrap -b -fs -sp -fs -nf -ov -- /usr/lib/xscreensaver/glslideshow -root -window-id WID &
    
###  禁用欢迎屏幕

When the program is started a screen appears which shows the program version and the author name. The screen is displayed every time the program starts which may be annoying. To disable this behavior run the program with the option --no-splash: 
    
    $ xscreensaver --no-splash &
    
##  问题解决

要显示详细的调试信息，启动 _xscreensaver_ 时带上 `--verbose` 命令行选项，修改 `~/.xscreensaver` 配置文件，添加 `verbose: True` 选项，则每次启动都打印详细的调试信息。 

用 `--log` 选项可以将日志记录到文件，此选项隐含了 verbose 配置。(`~/.xscreensaver` 或 X resources 中无对应配置)。 

##  参见

  * [XScreenSaver 的主页](<https://www.jwz.org/xscreensaver/>)
