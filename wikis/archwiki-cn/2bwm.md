相关文章

  * [Window manager](<../zh-cn/Window_manager.html> "Window manager")

[2bwm](<https://github.com/venam/2bwm>) 是一个快速的浮动窗口管理器，其特点是有两个边框，是基于XCB库写的，并派生自Michael Cardell编写的mcwm。在2bwm中，可以通过键盘访问所有功能，但也可以使用指针设备进行移动、调整大小和提升/降低。最近，该软件的名称已从mcwm-beast改为2bwm。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") [2bwm](<https://aur.archlinux.org/packages/2bwm/>)AUR 软件包。虽然安装过程可以自动进行，但如果直接从AUR构建，烈建议阅读并编辑源目录中的[config.h](<https://github.com/venam/2bwm/blob/master/config.h>) 文件。 

##  开始

使用 [xinit](<../zh-cn/Xinit.html> "Xinit") 运行 `2bwm`

##  使用2bwm

在启动2bwm之后，屏幕上只有鼠标光标、背景和终端 (在 [.xinitrc](</wzh/index.php?title=.xinitrc&action=edit&redlink=1> ".xinitrc（页面不存在）") 中指定)。 要打开终端，请使用默认配置，按下 `Super+Enter` 键。可以根据需要使用终端，例如用 `_program_name_ &` 的方式启动程序，更简单方便的做法是使用菜单来启动程序，比如 [dmenu](<../zh-cn/Dmenu.html> "Dmenu") 或 [9menu](<https://aur.archlinux.org/packages/9menu/>)AUR. 

###  通用命令

  * `Super+Ctrl+q` – 退出 2bwm
  * `Super+Ctrl+r` – 重启 2bwm
  * `Super+w` – 启动菜单
  * `Super+Enter` – 启动终端
  * `Super+Arrows` (`+Shift`) – 移动光标 (使用 `Shift` 键快速移动).

###  窗口控制

使用 `Super` 键与下面其中一个键结合，在特定的焦点窗口上操作： 

  * `q` – 关闭窗口.
  * `Tab` 或 `Shift+Tab` – 在当前工作区窗口环中切换到下一个窗口.
  * `f` – 将窗口固定，使其在所有工作区都可见 (切换).
  * `a` – 使一个窗口在按下 `Super+q` 键时无法关闭 (切换).
  * `r` – 提升或降低窗口 (切换).
  * `i` – 将窗口最小化 (或隐藏).

###  移动、调整大小和传送窗口

使用 `Super` 键与下面其中一个键结合，在特定的焦点窗口上操作： 

  * `x` – 最大化 (切换).
  * `m` – 垂直最大化 (切换).
  * `Shift+m` – 水平最大化 (切换).
  * `Shift+h` (`+Ctrl`) – 向左调整大小 (使用 `Ctrl` 键慢速移动).
  * `Shift+j` (`+Ctrl`) – 向下调整大小 (使用 `Ctrl` 键慢速移动).
  * `Shift+k` (`+Ctrl`) – 向上调整大小 (使用 `Ctrl` 键慢速移动).
  * `Shift+l` (`+Ctrl`) – 向右调整大小 (使用 `Ctrl` 键慢速移动).
  * `Home` – 保持纵横比增加大小.
  * `End` – 保持纵横比缩小大小.
  * `h` (`+Ctrl`) – 向左移动 (使用 `Ctrl` 键慢速移动)
  * `j` (`+Ctrl`) – 向下移动 (使用 `Ctrl` 键慢速移动)
  * `k` (`+Ctrl`) – 向上移动 (使用 `Ctrl` 键慢速移动)
  * `l` (`+Ctrl`) – 向右移动 (使用 `Ctrl` 键慢速移动)
  * `y` – 将窗口移动到显示器的左上角位置.
  * `u` – 将窗口移动到显示器的右上角位置.
  * `b` – 将窗口移动到显示器的左下角位置.
  * `n` – 将窗口移动到显示器的右下角位置.
  * `g` – 将窗口移动到显示器的中心位置.
  * `Shift+y`/`Shift+u`/`Shift+b`/`Shift+n` – 移动到左侧/右侧/底部/顶部，同时保持最大化垂直/最大化水平，以及半最大化水平/垂直.

###  工作区

  * `0`–`9` – 前往工作区 `_n_`, 0–9.
  * `Shift+_n_` – 发送到工作区 `_n_`.
  * `c` or `v` – 前往下一个/上一个工作区.
  * `,` or `.` – 将窗口移动到前一个/后一个显示器.

###  鼠标控制

通过按下 `Super` 键，鼠标按钮的操作如下所示： 

  * Button 1 on a window – 移动窗口
  * Button 3 on a window – 调整窗口大小
  * Button 3 + 在桌面上按下`Ctrl`键 – 启动在 `config.h` 中指定的菜单.

请注意，通过键盘激活的所有功能都会在当前焦点窗口上工作，而不管鼠标光标的位置如何。当然，改变工作区与焦点窗口无关。 

您可以从 `config.h` 文件更改键盘映射. 

##  提示和技巧

###  使用脚本获取当前工作区编号

以下命令可获取当前工作空间编号： 
    
    $ xprop -root _NET_CURRENT_DESKTOP | sed -e 's/_NET_CURRENT_DESKTOP(CARDINAL) = //'
    
###  易于记忆的外边框颜色

一个记住外边框颜色含义的简单技巧是将"fixed"设置为蓝色，"unkillable"设置为红色，而"fixed + unkillable"设置为紫色。蓝色和红色的混合将产生紫色！ 

###  左上角方块

将 `borders[0]` 设置为负数将使外边框变成一个位于完整边框的左上角的正方形。现在为外边框设置的颜色将固定在这个正方形上。 

##  参见

  * [2bwm源代码](<https://github.com/venam/2bwm>)
