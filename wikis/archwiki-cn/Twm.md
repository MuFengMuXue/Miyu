**翻译状态：**

  * 本文（或部分内容）译自 [twm](<https://wiki.archlinux.org/title/twm> "arch:twm")，最近一次同步于 2021-07-27，若英文版本有所[更改](<https://wiki.archlinux.org/title/twm?diff=0&oldid=689499>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/twm_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Window manager](<../zh-cn/Window_manager.html> "Window manager")

twm 是 [Xorg](<../zh-cn/Xorg.html> "Xorg") 的窗口管理器。这是一个小程序，是针对 Xlib 构建的，而不是使用窗口小部件库构建的，因此，它对系统资源的需求很小。尽管很简单，但是它是高度可配置的。字体，颜色，边框宽度，标题栏按钮等均可由用户设置。 

twm 由 Tom LaStrange 编写，这个人对 [uwm (Ultrix Window Manager)](<https://en.wikipedia.org/wiki/UWM_\(computing\)> "wikipedia:UWM \(computing\)")[[1]](<http://www.linuxplanet.com/linuxplanet/reports/3000/2/>) 的局限感到沮丧，后者是 X11 首次发布时唯一的窗口管理器。 twm 取代了 uwm 作为 1989 年 X11R4 版本 X11 随附的默认窗口管理器。 

twm 代表 _Tom's Window Manager_ ， _Tab Window Manager_ 和最近的 _Timeless Window Manager_ 。 

##  安装

twm 由 [xorg-twm](<https://archlinux.org/packages/?name=xorg-twm>)包 提供。 

##  启动

使用 `twm` 运行 [xinit](<../zh-cn/Xinit.html> "Xinit")。 

**注意：** 启动时只有黑屏。尝试移动鼠标并单击鼠标左键以获取 twm 菜单，以确保 twm 确实有用。 

您还可以使用显示管理器启动 twm。该 `twm.desktop` 文件不存在，因此我们必须在 `/usr/share/xsessions/` 创建它。在新创建的 `/usr/share/xsessions/twm.desktop` 文件中，复制并粘贴： 
    
    /usr/share/xsessions/twm.desktop
    
    [Desktop Entry]
    Name=twm
    Comment=xorg-twm
    TryExec=twm
    Exec=twm
    Type=Application

##  配置

默认情况下，twm 看起来非常过时且不直观。 通过创建 `~/.twmrc` 文件，您可以自定义 twm 以使其更友好。 

[twm(1)](<https://man.archlinux.org/man/twm.1>) 提供了可以在 `~/.twmrc` 文件中使用的命令的完整详细信息。 许多 `~/.twmrc` 文件已在线发布。[xwinman.org](<http://www.xwinman.org/vtwm.php>) 网站上有多个 `~/.twmrc` 文件，这些文件可能带有启发性的屏幕截图。 用 [Google 搜索“twmrc”](<https://www.google.com/search?q=twmrc>)可以找到新的想法。 

##  提示与技巧

###  修补版本

有一个修补程序版本，不在存储库中，具有更新功能，例如透明度。[xorg 邮件列表](<https://lists.x.org/archives/xorg/2010-January/048401.html>)中提供了描述和构建脚本。可以通过安装 [xcompmgr](<../zh-cn/Xcompmgr.html> "Xcompmgr") 运行构建脚本，将生成的 `twm` 和 `dot.twmrc` 文件放在一个方便的目录中，然后编辑 `~/.xinitrc` 文件来进行尝试，最后两行是 
    
    xcompmgr -o 0.3  -c -r 8 -t -10 -l -12 &
    /path-to-directory/twm -visual TrueColor -depth 32 -f /path-to-directory/dot.twmrc
    
##  故障排除

###  超大的窗口标题和菜单

您可能会发现 TWM 中的标题栏和菜单条目非常大-是人们通常期望的两倍。 这是使用 `UTF-8` [语言环境](</wzh/index.php?title=%E8%AF%AD%E8%A8%80%E7%8E%AF%E5%A2%83&action=edit&redlink=1> "语言环境（页面不存在）")时发生的 TWM 语言环境问题。将语言环境设置为 `C` 可解决此问题。 参见 [[2]](<https://forums.gentoo.org/viewtopic-t-530562-start-0.html>)。 

##  另请参见

  * "[UWM (computing)](<https://en.wikipedia.org/wiki/UWM_\(computing\)> "wikipedia:UWM \(computing\)")", _Wikipedia_. Retrieved October 22, 2009.
  * "[twm](<https://en.wikipedia.org/wiki/twm> "wikipedia:twm")", _Wikipedia_. Retrieved October 22, 2009.
  * [twm(1)](<https://man.archlinux.org/man/twm.1>) man page
  * "[Sample twmrc](<http://www.custompc.plus.com/twm/configs/twmrc09>)", _custompc.plus.com_. Retrieved August 12, 2013.
  * "[Window Managers for X: TWM/VTWM](<http://www.xwinman.org/vtwm.php>)", _xwinman.org_. Retrieved October 22, 2009.
  * Kask, Eeri. "[TWM -- Revised Edition -- Again](<https://lists.x.org/archives/xorg/2010-January/048401.html>)", _lists.x.org_ , January 3, 2010.
