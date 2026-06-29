**翻译状态：**

  * 本文（或部分内容）译自 [xinit](<https://wiki.archlinux.org/title/xinit> "arch:xinit")，最近一次同步于 2022-09-04，若英文版本有所[更改](<https://wiki.archlinux.org/title/xinit?diff=0&oldid=733065>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/xinit_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Display manager](<../zh-cn/Display_manager.html> "Display manager")
  * [Start X at Login](<../zh-cn/Start_X_at_Login.html> "Start X at Login")
  * [Xorg](<../zh-cn/Xorg.html> "Xorg")
  * [Xprofile](<../zh-cn/Xprofile.html> "Xprofile")
  * [Xresources](</wzh/index.php?title=Xresources&action=edit&redlink=1> "Xresources（页面不存在）")

摘自 [Wikipedia](<https://en.wikipedia.org/wiki/xinit> "wikipedia:xinit"): 

     _xinit_ 程序允许用户手动启动 [Xorg](<../zh-cn/Xorg.html> "Xorg") 显示服务器。[startx(1)](<https://man.archlinux.org/man/startx.1>) 脚本是 [xinit(1)](<https://man.archlinux.org/man/xinit.1>) 的一个前端。

xinit 通常用于启动[窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")或[桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")。虽然您也可以用 _xinit_ 在没有窗口管理器的情况下运行 GUI 应用程序，但许多图形应用程序期待一个 [EWMH](<https://en.wikipedia.org/wiki/Extended_Window_Manager_Hints> "wikipedia:Extended Window Manager Hints") 兼容的窗口管理器。[显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")一般都依据 [xprofile](<../zh-cn/Xprofile.html> "Xprofile") 为您启动 [Xorg](<../zh-cn/Xorg.html> "Xorg")。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [xorg-xinit](<https://archlinux.org/packages/?name=xorg-xinit>)包 包。 

##  配置

_xinit_ 和 _startx_ 需要一个可选的客户端程序参数，见 [#覆盖 xinitrc](<#%E8%A6%86%E7%9B%96_xinitrc>) 。 如果您没有提供参数，它们会寻找 `~/.xinitrc`，作为一个shell脚本运行，以启动客户程序。 

### xinitrc

`~/.xinitrc` 可以方便地在X服务器启动时运行依赖于X的程序并设置环境变量。如果它存在于用户的主目录中， _startx_ 和 _xinit_ 会执行它。否则 _startx_ 将运行默认的`/etc/X11/xinit/xinitrc`。 

**注意：** _xinit_ 有自己的默认行为，而不是执行该文件。详见 [xinit(1)](<https://man.archlinux.org/man/xinit.1>)。

这个默认的xinitrc将启动一个包含 [Twm](<../zh-cn/Twm.html> "Twm")、[xorg-xclock](<https://archlinux.org/packages/?name=xorg-xclock>)包 和 [Xterm](</wzh/index.php?title=Xterm&action=edit&redlink=1> "Xterm（页面不存在）") 的基本环境（假设安装了必要的软件包）。因此，要启动不同的窗口管理器或桌面环境，首先要在主目录下创建一个默认的 `xinitrc` 副本。 
    
    $ cp /etc/X11/xinit/xinitrc ~/.xinitrc
    
然后[编辑](<../zh-cn/Help:Reading_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Help:Reading \(简体中文\)")该文件，用想要的命令替换默认程序。记住，在使用 `exec` 的命令之后的行会被忽略。例如，要在后台启动 `xscreensaver`，然后启动 [openbox](<../zh-cn/Openbox.html#%E5%8D%95%E7%8B%AC%E8%BF%90%E8%A1%8C> "Openbox")，请使用以下命令。 
    
    ~/.xinitrc
    
    ...
    xscreensaver &
    exec openbox-session

**注意：** 至少要确保 `/etc/X11/xinit/xinitrc` 中的最后一个 `if` 块出现在您的 `~/.xinitrc` 文件中，以确保 `/etc/X11/xinit/xinitrc.d` 中的脚本有源可循。

在窗口管理器之前启动的长期运行的程序，如屏保和墙纸程序，必须自己分叉或通过附加 `&` 符号在后台运行。否则，在执行窗口管理器或桌面环境之前，脚本会停止运行并等待每个程序退出。请注意，有些程序反而不应该被分叉，以避免出现竞争性错误，如 [xrdb](</wzh/index.php?title=Xrdb&action=edit&redlink=1> "Xrdb（页面不存在）") 的情况。在 `exec` 前缀会将脚本进程替换为窗口管理器进程，这样，即使该进程分叉到后台，X也不会退出。 

### xserverrc

`xserverrc` 文件是一个负责启动X服务器的shell脚本。startx "和 "xinit "都会执行 `~/.xserverrc`，如果它存在的话，"startx "会使用 `/etc/X11/xinit/xserverrc`。 

为了保持 `logind`的[会话权限](</wzh/index.php?title=General_troubleshooting_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "General troubleshooting \(简体中文\)（页面不存在）")，并防止通过切换终端绕过屏幕锁定器，[Xorg](<../zh-cn/Xorg.html> "Xorg") 必须在发生登录的同一虚拟终端上启动 [[1]](<http://blog.falconindy.com/articles/back-to-basics-with-x-and-systemd.html>)。因此建议在 `vt$XDG_VTNR`文件中指定 `~/.xserverrc`。 
    
    ~/.xserverrc
    
    }文件：
    #!/bin/sh
    
    exec /usr/bin/Xorg -nolisten tcp "$@" vt$XDG_VTNR
    
参见 [Xserver(1)](<https://man.archlinux.org/man/Xserver.1>) 中的所有命令行选项列表。 

**提示：**`-nolisten local` 可以加在 `-nolisten tcp` 之后，以禁用X11的抽象套接字，帮助隔离。 关于这对X11安全的潜在影响，有一个 [简单背景](<https://tstarling.com/blog/2016/06/x11-security-isolation/>)。

另外，如果您想让X显示在一个独立的控制台，而不是调用服务器的控制台，您可以通过使用 `/usr/lib/systemd/systemd-multi-seat-x` 提供的X服务器包装器实现。为方便起见，可以通过修改 `~/.xserverrc` 设置 "xinit "和 "startx "使用该包装器。 

`-keeptty`选项，重新启用将X会话的输出重定向至Xorg日志文件的功能。详见 [Xorg#重定向Xorg会话日志](<../zh-cn/Xorg.html#%E9%87%8D%E5%AE%9A%E5%90%91Xorg%E4%BC%9A%E8%AF%9D%E6%97%A5%E5%BF%97> "Xorg")。}} 

##  用法

要以普通用户身份运行 Xorg，请输入： 
    
    $ startx
    
或者如果配置了 [#xserverrc](<#xserverrc>)。 
    
    $ xinit -- :1
    
**注意：** _xinit_ 不能处理已启动的另一个X服务器的多个显示。为此，您必须通过附加 `--:_display_number_` 来指定显示，其中 `_display_number_` 为 `1` 或以上。

您选择的窗口管理器（或桌面环境）现在应该可以正确启动了。 

要退出X，请运行您的窗口管理器的退出功能（假设它有的话）。如果它缺乏这样的功能，请运行。 
    
    $ pkill -15 Xorg
    
**注意：** _pkill_ 将杀死所有正在运行的X实例。要指定杀死当前虚拟终端上的窗口管理器，请运行： 
    
    $ pkill -15 -t tty"$XDG_VTNR" Xorg
    
另见 [signal(7)](<https://man.archlinux.org/man/signal.7>)。 

##  技巧和窍门

###  覆盖 xinitrc

如果您有一个正常工作的 `~/.xinitrc`，但只是想试试其他窗口管理器或桌面环境，您可以通过发出 _startx_ ，并在后面加上窗口管理器的路径来运行它，例如。 
    
    $ startx /usr/bin/i3
    
如果二进制文件需要参数，它们需要加引号，以便被识别为 _startx_ 的第一个参数的一部分。 
    
    $ startx "/usr/bin/_application_ --_key value_ "
    
注意，完整的路径是**必须的** 。您也可以为 [#xserverrc](<#xserverrc>) 脚本指定自定义选项，在双破折号 `--` 后加上这些选项。 
    
    $ startx /usr/bin/enlightenment -- -br +bs -dpi 96
    
另请参见 [startx(1)](<https://man.archlinux.org/man/startx.1>)。 

**注意：** 由于 `/etc/X11/xinit/xinitrc.d/` 下的脚本被跳过，环境变量 `DISPLAY` 可能需要被设置。您可以通过执行`DISPLAY=:_display_number_ startx /usr/bin/i3`，在所需的显示器上试用 _i3_ 。

**提示：** 这可用于启动常规GUI程序，但没有任何基本的窗口管理器功能。参见 [#在没有窗口管理器的情况下启动应用程序](<#%E5%9C%A8%E6%B2%A1%E6%9C%89%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8%E7%9A%84%E6%83%85%E5%86%B5%E4%B8%8B%E5%90%AF%E5%8A%A8%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F>) 和 [在独立的X显示屏中运行程序](</wzh/index.php?title=Running_program_in_separate_X_display&action=edit&redlink=1> "Running program in separate X display（页面不存在）")。

###  登录时自动启动 X

确保 _startx_ 是正确的[配置](<#%E9%85%8D%E7%BD%AE>)。 

在您的 [login shell](</wzh/index.php?title=Login_shell&action=edit&redlink=1> "Login shell（页面不存在）") 初始化文件（例如，[Bash](<../zh-cn/Bash.html> "Bash") 的 `~/.bash_profile` 或 [Zsh](<../zh-cn/Zsh.html> "Zsh") 的 `~/.zprofile`）中放置以下内容。 
    
    if [ -z "${DISPLAY}" ] && [ "${XDG_VTNR}" -eq 1 ]; then
      exec startx
    fi
    
您可以用 `-eq` 替换 `-le 3` 这样的比较（用于 vt1 到 vt3），如果您想在一个以上的虚拟终端上使用图形化登录。 

检测虚拟终端的其他条件包括 `"$(tty)" = "/dev/tty1"`，它不允许与 `-le` 比较，以及 `"$(fgconsole 2>/dev/null || echo -1)" -eq 1`，它在[串行控制台](</wzh/index.php?title=Serial_console&action=edit&redlink=1> "Serial console（页面不存在）")不起作用。 

`exec` 命令确保在X服务器退出、崩溃或被攻击者杀死时，用户被注销。如果您想承担风险，在X会话结束时保持登录状态，请删除 `exec`。 

参见 [Fish_(简体中文)#登录_fish_时自动起动_X](</wzh/index.php?title=Fish_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "Fish \(简体中文\)（页面不存在）") 和 [Systemd_(简体中文)/User_(简体中文)#Automatic_login_into_Xorg_without_display_manager](</wzh/index.php?title=Systemd_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)/User_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "Systemd \(简体中文\)/User \(简体中文\)（页面不存在）")。 

**提示：** 此方法可与 [自动登录到虚拟控制台](</wzh/index.php?title=Getty_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "Getty \(简体中文\)（页面不存在）") 相结合。

###  在桌面环境/窗口管理器之间进行切换

如果您经常在不同的桌面环境或窗口管理器之间切换，使用[显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")或扩展 `~/.xinitrc` 来实现切换是很方便的。 

下面的例子展示了如何用一个参数来启动一个特定的桌面环境或窗口管理器。 
    
    ~/.xinitrc
    
    ...
    
    # 这里 Xfce 保持默认
    session=${1:-xfce}
    
    case $session in
        i3|i3wm           ) exec i3;;
        kde               ) exec startplasma-x11;;
        xfce|xfce4        ) exec startxfce4;;
        # No known session, try to run it as command
        *                 ) exec $1;;
    esac
    
要传递参数 _session_ ： 
    
    $ xinit _session_
    
或 
    
    $ startx ~/.xinitrc _session_
    
###  在没有窗口管理器的情况下启动应用程序

可以在没有窗口管理器的情况下只启动特定的应用程序，尽管这很可能只对全屏模式下的单个应用程序有用。比如说： 
    
    ~/.xinitrc
    
    ...
    
    exec chromium
    
另外，也可以像 [#覆盖 xinitrc](<#%E8%A6%86%E7%9B%96_xinitrc>) 中描述的那样，直接从命令提示符中调用二进制。 

使用这种方法，您需要通过自己的配置文件设置每个应用程序的窗口几何形状（如果可能的话）。 

**提示：** 这对启动图形游戏很有用，排除合成器的开销有助于提高游戏的性能。

另请参见[显示管理器#没有窗口管理启动应用程序](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html#%E6%B2%A1%E6%9C%89%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%90%AF%E5%8A%A8%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F> "显示管理器")。 

###  使用 startx 进行输出重定向

参见[Xorg#重定向Xorg会话日志](<../zh-cn/Xorg.html#%E9%87%8D%E5%AE%9A%E5%90%91Xorg%E4%BC%9A%E8%AF%9D%E6%97%A5%E5%BF%97> "Xorg")了解详情。 
