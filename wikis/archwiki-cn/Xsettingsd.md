相关文章

  * [X 资源](<../zh-cn/X_%E8%B5%84%E6%BA%90.html> "X 资源")

**翻译状态：**

  * 本文（或部分内容）译自 [Xsettingsd](<https://wiki.archlinux.org/title/Xsettingsd> "arch:Xsettingsd")，最近一次同步于 2024-8-5，若英文版本有所[更改](<https://wiki.archlinux.org/title/Xsettingsd?diff=0&oldid=818082>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Xsettingsd_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Xsettingsd](<https://codeberg.org/derat/xsettingsd>) 是一个轻量级的 **xsettings** 守护进程，通过 [XSETTINGS](<https://specifications.freedesktop.org/xsettings-spec/latest/>) 规范为 [Xorg](<../zh-cn/Xorg.html> "Xorg") 应用程序提供设置。 

某些桌面环境（如默认的 [KDE](<../zh-cn/KDE.html> "KDE") 或[自定义](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html#%E8%87%AA%E5%B7%B1%E6%89%93%E9%80%A0%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83> "桌面环境")）不包含此功能。在这些环境中，运行 _xsettings_ 守护进程对于某些应用程序（主要是基于[GTK](<../zh-cn/GTK.html> "GTK")、[Java](<../zh-cn/Java_%E8%BF%90%E8%A1%8C%E7%8E%AF%E5%A2%83%E5%AD%97%E4%BD%93%E9%85%8D%E7%BD%AE.html#%E8%BF%90%E8%A1%8C_xsettings_%E5%AE%88%E6%8A%A4%E8%BF%9B%E7%A8%8B> "Java 运行环境字体配置") 和 [Wine](<../zh-cn/Wine.html> "Wine")）使用选定的主题、光标、字体和其他设置是必要的。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [xsettingsd](<https://archlinux.org/packages/?name=xsettingsd>)包 或 [xsettingsd-git](<https://aur.archlinux.org/packages/xsettingsd-git/>)AUR。 

##  配置

[xsettingsd(1)](<https://man.archlinux.org/man/xsettingsd.1>) 只包含简要介绍，详情请参见 [README](<https://codeberg.org/derat/xsettingsd#configuration>) 。 

_X FreeType_ 字体渲染配置示例（您可以使用自己喜欢的 [config 文件路径](<https://codeberg.org/derat/xsettingsd/issues/35>)）：: 
    
    ~/.config/xsettingsd/xsettingsd.conf
    
    Xft/Antialias   1
    Xft/DPI         98304
    Xft/Hinting     1
    Xft/HintStyle   "hintfull"
    Xft/lcdfilter   "lcddefault"
    Xft/RGBA        "rgb"
    
**注意：**

  * `Xft/DPI`是您的 DPI 乘以 [1024](<https://docs.gtk.org/gtk4/property.Settings.gtk-xft-dpi.html>)。
  * 使用 [real](<https://dpi.lv/>) DPI（如 _94*1024_ ）的字体可能比使用 artificial DPI（如 _96*1024_ ）的字体更好看，但在应用程序中可能会出现故障（如弹出提示没有边框）。
  * 虽然 _X resources_ 和 _xsettings_ 参数名称看起来相似，但它们都区分大小写。例如，应将 `Xft.dpi: 96` 放在 `~/.Xresources` 中，将 `Xft/DPI 98304` 放在 `~/.xsettingsd.conf` 中。

##  用法

[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `xsettingsd.service` [用户单元](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "用户单元")。 

该单元是 _静态_ 的，因此无法直接[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")。您可以在 [Xorg](<../zh-cn/%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8.html#Xorg> "自动启动")、[桌面环境](<../zh-cn/%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8.html#%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83> "自动启动")或[窗口管理器](<../zh-cn/%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8.html#%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%90%AF%E5%8A%A8> "自动启动")启动时自动启动它（或`xsettingsd`二进制文件）。 

**注意：** 安装了 [kde-gtk-config](<https://archlinux.org/packages/?name=kde-gtk-config>)包 的 [KDE](<../zh-cn/KDE.html> "KDE") 将自动启动[二进制文件](<https://github.com/KDE/kde-gtk-config/blob/f14f9014b7245c8321848d75801a5e1a5582fd48/kded/config_editor/xsettings.cpp#L70>)。

该单元被配置为 `graphical-session.target` 的一部分，因此当 `graphical-session.target` 停止（重启）时，它也会停止（重启），请参阅 [systemd.unit(5) § [UNIT] SECTION OPTIONS](<https://man.archlinux.org/man/systemd.unit.5#%5BUNIT%5D_SECTION_OPTIONS>) 和 [systemd.special(7) § Special Passive User Units](<https://man.archlinux.org/man/systemd.special.7#Special_Passive_User_Units>)。 

##  问题解决

###  无法打开到 X 服务器的连接

检查是否设置了 `DISPLAY` 和 `XAUTHORITY` 环境变量。 

如果正在启动 [systemd](<../zh-cn/Systemd.html> "Systemd") 单元，请检查 `systemctl --user import-environment DISPLAY XAUTHORITY` 是否已执行（可通过从`~/.xinitrc`调用`/etc/X11/xinit/xinitrc.d/50-systemd-user.sh`来完成）。 
