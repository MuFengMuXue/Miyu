相关文章

  * [窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")

**翻译状态：**

  * 本文（或部分内容）译自 [Cwm](<https://wiki.archlinux.org/title/Cwm> "arch:Cwm")，最近一次同步于 2024-8-5，若英文版本有所[更改](<https://wiki.archlinux.org/title/Cwm?diff=0&oldid=813902>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Cwm_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

**cwm** 是一款 X11 [窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")，它的重点是让你摆脱困境，提高工作效率。 它最初源于 [evilwm](</wzh/index.php?title=Evilwm&action=edit&redlink=1> "Evilwm（页面不存在）")，但代码库已从头开始重新编写。 

cwm 是作为 OpenBSD 基本系统的一部分开发的。此外，还有一个可在 Linux 上运行的 "便携"版本。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")下列软件包之一： 

  * [cwm](<https://aur.archlinux.org/packages/cwm/>)AUR \- 最新版本。
  * [cwm-git](<https://aur.archlinux.org/packages/cwm-git/>)AUR \- 主版本的最新提交

##  配置

cmw 通过编辑 `~/.cwmrc` 进行配置。没有默认的 `cwmrc` 文件；所有默认设置（包括按键绑定）都在 [conf.c](<https://github.com/chneukirchen/cwm/blob/linux/conf.c>) 中定义。[cwm(1)](<https://man.openbsd.org/cwm.1>)列出了默认按键；[cwmrc(5)](<https://man.openbsd.org/cwmrc.5>)列出了所有配置指令。 

不过，您可以使用 `unbind-key all` 和 `unbind-mouse all` 删除所有默认键绑定。 

###  窗口分组

cwm 没有传统的"工作区"，但可以将窗口分配到"组"中。这是一种更灵活的方法，因为可以同时显示两个或多个组，而且与许多平铺窗口管理器的工作区功能相似或相同。 

例如，可以将聊天/IRC 应用程序放在第 4 组，然后指定一个键来切换该组的可见性（`bind-key <k> group-toggle 4`），以便在显示其他窗口/组的**同时** 显示该组。 

您还可以使用 `bind-key <k> group-only <n>` 来显示 _仅_ 该组中的窗口，隐藏其他所有窗口。 

新窗口的默认设置是不归入任何组，这意味着它们将始终显示（许多 WM 将其称为 "粘性 "窗口）。不过，通过使用 `sticky yes` 启用 "粘性组模式"，窗口将默认分配到当前选定的组中。 您还可以使用 `autogroup` 目录对窗口进行自动分组。 

###  移动窗口

没有将窗口移动到预定义位置的操作；但可以使用 [xdotool](<https://archlinux.org/packages/?name=xdotool>)包 解决这个问题；将 `cwm-w-mv` 脚本放到 `PATH` 中： 
    
    #!/bin/sh
    # Move a window to the side of a screen.
    
    case "$1" in
    	"left") xdotool getactivewindow windowmove 0 y ;;
    	"top")  xdotool getactivewindow windowmove x 0 ;;
    
    	"right")
    		screen_width=$(xwininfo -root | grep Width | cut -d: -f2 | tr -d ' ')
    		win_width=$(xdotool getactivewindow  getwindowgeometry --shell | grep WIDTH | cut -d= -f2)
    		xdotool getactivewindow windowmove $(( $screen_width - $win_width )) y
    		;;
    	"bottom")
    		screen_height=$(xwininfo -root | grep Height | cut -d: -f2 | tr -d ' ')
    		win_height=$(xdotool getactivewindow  getwindowgeometry --shell | grep HEIGHT | cut -d= -f2)
    		xdotool getactivewindow windowmove x $(( $screen_height - $win_height ))
    		;;
    	*)
    		echo "Unsupported: \"$1\""
    		exit 1
    esac
    
然后在 cwm 中进行绑定，例如 
    
    bind-key 4-h      cwm-w-mv left   # Move window to side of the screen.
    bind-key 4-j      cwm-w-mv bottom
    bind-key 4-k      cwm-w-mv top
    bind-key 4-l      cwm-w-mv right
    bind-key 4-Left   cwm-w-mv left
    bind-key 4-Down   cwm-w-mv bottom
    bind-key 4-Up     cwm-w-mv top
    bind-key 4-Right  cwm-w-mv right
    
这将使 Mod4（"Windows 键"）加 hjkl 或方向键将窗口移到侧面。 

##  参见

  * [OpenBSD 源](<https://cvsweb.openbsd.org/cgi-bin/cvsweb/xenocara/app/cwm/>)
  * [便携版](<https://github.com/leahneukirchen/cwm>)
  * cwmrc 示例：[[1]](<https://mwl.io/archives/873>)
  * [Absolute OpenBSD](<https://www.nostarch.com/obenbsd2e>) 包含 CWM 简介。
