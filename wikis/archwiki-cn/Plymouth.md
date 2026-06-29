**翻译状态：**

  * 本文（或部分内容）译自 [Plymouth](<https://wiki.archlinux.org/title/Plymouth> "arch:Plymouth")，最近一次同步于 2024-08-30，若英文版本有所[更改](<https://wiki.archlinux.org/title/Plymouth?diff=0&oldid=815520>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Plymouth_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [静默启动](<../zh-cn/%E9%9D%99%E9%BB%98%E5%90%AF%E5%8A%A8.html> "静默启动")

[Plymouth](<https://www.freedesktop.org/wiki/Software/Plymouth>) 是一个来自于 Fedora 社区的提供漂亮的启动界面的项目，现在它被列入了[freedesktop.org 的官方资源](<https://www.freedesktop.org/wiki/Software/#graphicsdriverswindowsystemsandsupportinglibraries>)之中。它依靠 [KMS](<../zh-cn/%E5%86%85%E6%A0%B8%E7%BA%A7%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE.html> "KMS") 尽可能早的设置显示器的原始分辨率显示，之后产生漂亮的启动界面直至出现登录界面。 

##  准备

Plymouth 依靠 KMS（Kernel Mode Setting，内核级显示模式设置）显示图形界面。在 UEFI 系统中，Plymouth 可以使用 EFI 帧缓冲。 

如果使用了私有驱动, 无法启用 KMS，或者只是不想使用 EFI 帧缓冲，那么可以考虑使用支持大屏分辨率的 [Uvesafb](<../zh-cn/Uvesafb.html> "Uvesafb")。如果既没有KMS也没有framebuffer，那么Plymouth将使用文本模式。 

##  安装

需要稳定版本请安装 [plymouth](<https://archlinux.org/packages/?name=plymouth>)包，[plymouth-git](<https://aur.archlinux.org/packages/plymouth-git/>)AUR是开发版本。 

默认情况下，Plymouth 将引导消息记录到 `/var/log/boot.log`，并且不显示启动画面。 

  * 要显示启动画面，将 `splash` 加入[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")。
  * 需要[静默启动](<../zh-cn/%E9%9D%99%E9%BB%98%E5%90%AF%E5%8A%A8.html> "静默启动"), 再添加 `quiet`。
  * 要禁用日志，添加 `plymouth.nolog`。

安装 Plymouth 后，如果想要在启动早期阶段就启用，需要配置 [initramfs](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#initramfs> "Initramfs") 生成器，创建含有Plymouth的镜像。 

### mkinitcpio

把`plymouth`添加到 [mkinitcpio.conf](<../zh-cn/Mkinitcpio.html#%E9%85%8D%E7%BD%AE> "Mkinitcpio.conf") 的 `HOOKS` 列表中： 
    
    /etc/mkinitcpio.conf
    
    HOOKS=(... plymouth ...)

然后使用 `mkinitcpio -P` 命令重新生成 [initramfs](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#initramfs> "Initramfs")。 

如果你正在使用 `systemd` 钩子，它必须在 `plymouth` 之前。 

如果你的系统使用 dm-crypt 加密，请确保将 `plymouth` 钩子置于 `crypt` 钩子之前。 

### dracut

安装 Plymouth 之后，[dracut](<../zh-cn/Dracut.html> "Dracut") 会自动捕获并将其添加到 initramfs 镜像中。如果自动捕获失败，可以在 dracut 配置文件中添加下列几行来强制 dracut 引入 Plymouth： 
    
    /etc/dracut.conf.d/myflags.conf
    
    add_dracutmodules+=" plymouth "

##  配置

通过 `/etc/plymouth/plymouthd.conf` 进行配置，通过 `/usr/share/plymouth/plymouthd.defaults` 文件可以查看配置的默认值。 

###  更改主题

Plymouth 自带了一些主题： 

  1. **BGRT** : Spinner 的一个变种，如果 OEM 的图标可用便会显示。（BGRT 指的是 Boot Graphics Resource Table）
  2. **Fade-in** : "简单的有淡出淡入的星星的主题"
  3. **Glow** : "伴随着新兴标志的饼状引导进度条的企业主题"
  4. **Script** : "脚本案例插件" (漂亮的 Arch Logo 主题)
  5. **Solar** : "带有燃烧的蓝色星球的空间主题"
  6. **Spinner** : "带有加载框的简单主题"
  7. **Spinfinity** : "显示旋转的无穷大标志的主题"
  8. **Tribar** : "带三色进度条的文本模式主题"
  9. _(**Text** : "带三色进度条的文本模式主题")_
  10. _(**Details** : "详细信息回退主题")_

默认选择 **bgrt** ，可以通过修改配置文件设置其它主题, 例如: 
    
    /etc/plymouth/plymouthd.conf
    
    [Daemon]
    Theme=fade-in

或者执行 
    
    # plymouth-set-default-theme -R _theme_
    
每次更换主题，`initrd` 都必须重新构建。`-R`选项可确保其被重建（或者手动重新生成 [initramfs](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#initramfs> "Initramfs")）： 

###  安装新主题

可以通过 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 安装其它[主题](<https://aur.archlinux.org/packages?K=plymouth-theme->)，或者 [plymouth-kcm](<https://archlinux.org/packages/?name=plymouth-kcm>)包 提供与 KDE Plasma 设置的集成，并提供 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 上没有的主题。 

使用以下命令获得已安装的主题列表： 
    
    $ plymouth-set-default-theme -l
    
或是通过： 
    
    $ ls /usr/share/plymouth/themes
    
    bgrt  details  fade-in  glow  script  solar  spinfinity  spinner  text  tribar
    
###  显示延迟

Plymouth 可以配置选项以延迟启动画面显示： 
    
    /etc/plymouth/plymouthd.conf
    
    [Daemon]
    ShowDelay=5

对于启动很快的系统，可能在显示管理器或登录提示准备好前只能看到启动画面闪过。可以设置 `ShowDelay` 为一个比启动时间更长的值（以秒为单位）来避免这种闪烁以及黑屏。默认值为0秒，因此您不需要将其更改为其他值，就可以在引导过程中更早地看到您的启动。 

### HiDPI

编辑配置文件： 
    
    /etc/plymouth/plymouthd.conf
    
    DeviceScale=_an-integer-scaling-factor_

然后重建 initrd。 

##  提示与技巧

###  显示启动消息

启动时按 `Esc` 键可以切换到启动消息。 

###  平滑过渡

[GDM](<../zh-cn/GDM.html> "GDM") 支持开箱即用的 _平滑过渡_ ，无需额外配置。 

对于其他显示管理器，您可以使用 `display-manager.service` 的以下[附加片段](<../zh-cn/Drop-in_snippet.html> "Drop-in snippet")获得平滑过渡： 
    
    /etc/systemd/system/display-manager.service.d/plymouth.conf
    
    [Unit]
    Conflicts=plymouth-quit.service
    After=plymouth-quit.service rc-local.service plymouth-start.service systemd-user-sessions.service
    OnFailure=plymouth-quit.service
    
    [Service]
    ExecStartPost=-/usr/bin/sleep 30
    ExecStartPost=-/usr/bin/plymouth quit --retain-splash

###  预览主题

主题可以在不重新生成 initrd 的情况下预览。按 `Ctrl+Alt+F6` 切换到文本终端，使用 root 登录并键入： 
    
    # plymouthd
    # plymouth --show-splash
    
再按 `Ctrl+Alt+F6` 并输入如下命令退出预览： 
    
    # plymouth --quit
    
您也可以在运行中的 X.Org 会话以 root 身份运行它们，但 Plymouth 窗口会覆盖终端窗口并将本身置顶。所以请准备好虚拟桌面。 

###  更换背景图片

某些主题（如 spinner 和 BGRT）可以改变其背景图像。只需将 `/usr/share/plymouth/themes/spinner/background-tile.png` 替换为你想要的图片。一旦改变主题就要重新生成 initrd。 

###  缺少 BGRT 图片

如果您使用的是 BGRT 主题，但 UEFI 没有提供供应商徽标，则可以将回退镜像放置到 `/usr/share/plymouth/themes/spinner/bgrt-fallback.png` 中以显示它。 

###  放慢启动速度以显示完整的动画

在启动时间非常快的系统上，如果需要显示整个动画，则可能需要使用包含 `ExecStartPre=/usr/bin/sleep 5` 的[附加片段](<../zh-cn/Drop-in_snippet.html> "Drop-in snippet")为 `plymouth-quit.service` 添加延迟。见[这篇 reddit 帖子](<https://www.reddit.com/r/archlinux/comments/u5fjbi/how_do_i_make_my_boot_time_slower/.compact>)。 

也可以使用一个新的 systemd 服务，它与 Plymouth 同时启动，并且等待了完整播放动画所需要的时间。这种方法将确保不会察觉到启动时间不一致，因为**它** 不**在动画开始显示之后** 添加时间，而是一个**在动画期间** 开始的延迟。 
    
    /etc/systemd/system/plymouth-wait-for-animation.service
    
    [Unit]
    Description=Waits for Plymouth animation to finish
    Before=plymouth-quit.service display-manager.service
    
    [Service]
    Type=oneshot
    ExecStart=/usr/bin/sleep _动画所需的时间_
    
    [Install]
    WantedBy=plymouth-start.service

然后启用这个服务。 

**注意：** 如果使用 initramfs 启动了 Plymouth，该方法将不起作用。

##  疑难解答

###  禁用的内核参数

如果在启动过程中遇到问题，可以使用以下[内核参数](<../zh-cn/Kernel_parameters.html> "Kernel parameters")临时禁用 Plymouth： 
    
    plymouth.enable=0 disablehooks=plymouth
    
###  调试

要将调试输出写入 `/var/log/plymouth-debug.log`，请添加以下内核参数： 
    
    plymouth.debug
    
###  密码提示不更新

当在 [Mkinitcpio](<../zh-cn/Mkinitcpio.html> "Mkinitcpio") 中使用 `systemd` 而不是 `udev` 钩子时，在通过 Plymouth 脚本处理它的主题上密码提示可能不会更新。 

您可以尝试切换到开发版本 [plymouth-git](<https://aur.archlinux.org/packages/plymouth-git/>)AUR 或使用来自 [Mkinitcpio#常用钩子](<../zh-cn/Mkinitcpio.html#%E5%B8%B8%E7%94%A8%E9%92%A9%E5%AD%90> "Mkinitcpio")的替代品。 

###  显示未居中

当在启动过程中启用了多个监视器时，某些主题可能无法使显示居中。 

您可以使用[内核级显示模式设置#Forcing modes](<../zh-cn/%E5%86%85%E6%A0%B8%E7%BA%A7%E6%98%BE%E7%A4%BA%E6%A8%A1%E5%BC%8F%E8%AE%BE%E7%BD%AE.html#Forcing_modes> "内核级显示模式设置") 禁用特定的监视器。 

##  另见

  * [原始规范](<https://fedoraproject.org/wiki/Features/BetterStartup> "fedora:Features/BetterStartup")
  * [论坛相关帖子](<https://bbs.archlinux.org/viewtopic.php?id=81406>)
