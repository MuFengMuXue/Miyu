**翻译状态：**

  * 本文（或部分内容）译自 [Xephyr](<https://wiki.archlinux.org/title/Xephyr> "arch:Xephyr")，最近一次同步于 2022-11-19，若英文版本有所[更改](<https://wiki.archlinux.org/title/Xephyr?diff=0&oldid=491124>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Xephyr_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

**Xephyr** 是一个嵌套的 X 服务器，作为 X 应用程序运行。 

这对于解决编写不当的应用程序可能很有用。例如，Supermicro 服务器可以通过 java ipmi kvm 查看器应用程序进行控制。当服务器重新启动时，应用程序经常重新创建其窗口。它从当前窗口中窃取焦点。这种情况每分钟发生几次，实际上使您的工作变得不可能。同时，如何制定窗口规则来防止此类应用程序的窗口在创建时获得焦点并不明显，因为您希望它在首次启动时获得焦点。使用 xephyr 可以将这些窗口重新创建保留在单独的窗口中，这不会窃取当前打开的窗口的焦点。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [xorg-server-xephyr](<https://archlinux.org/packages/?name=xorg-server-xephyr>)包 包， xorg-server-xephyr 已收录于[官方仓库](<../zh-cn/Official_repositories.html> "Official repositories")中，可以用 [pacman](<../zh-cn/Pacman.html> "Pacman") 进行安装。 

##  运行

如果希望运行一个嵌套的 X 窗口，你需要指定一个新的 **DISPLAY**`:1`。 
    
    $ Xephyr -br -ac -noreset -screen 800x600 :1
    
这样将会启动一个新的 Xephyr 窗口，这个窗口的 **DISPLAY** 序号是“:1”。为了在这个窗口里运行一个应用，你需要明确指定这个 **DISPLAY** ： 
    
    $ DISPLAY=:1 xterm
    
###  启动窗口管理器

如果想启动其他窗口管理器（例如 [spectrwm](</wzh/index.php?title=Spectrwm&action=edit&redlink=1> "Spectrwm（页面不存在）") ），则输入： 
    
    $ DISPLAY=:1 spectrwm
    
也可以通过 startx 命令让 Xephyr 使用你的 [xinitrc](<../zh-cn/Xinit.html#xinitrc> "Xinitrc") ： 
    
     $ startx -- /usr/bin/Xephyr :1
    
###  切换用户键鼠焦点

如果想释放 Xephyr 窗口的聚焦，在 Xephyr 窗口中按 `Ctrl+Shift` 可以锁定/解锁鼠标指针和键盘输入。 

###  发送Alt+Tab

如果使用 KDE，请创建一个窗口规则以忽略全局快捷方式。然后你可以在 **Xephyr** 中使用 `Alt+Tab`。 非KDE可以使用屏幕键盘 [florence](<https://aur.archlinux.org/packages/florence/>)AUR，也可使用[xorg-xkbcomp](<https://archlinux.org/packages/?name=xorg-xkbcomp>)包工具修改按键映射。 

##  提示和技巧

Xephyr 其他有用的情况示例包括: 

  1. X 应用程序或功能的测试环境，测试人员希望继续在通常的 X 环境中工作，同时保护其他应用程序免受被测应用程序故障的影响。
  2. [OpenSSH#Remote](<../zh-cn/OpenSSH.html#Remote> "OpenSSH") emphasize 3 settings in the sshd server configuration file for [OpenSSH#X11 forwarding](<../zh-cn/OpenSSH.html#X11_forwarding> "OpenSSH") (over ssh). 2 of these, out of 3, are the default settings. When the ssh client can not influence the ssh server administrator to set the 3rd one, `X11Forwarding`, to yes, [Forwarding X11 over ssh](<https://unix.stackexchange.com/questions/12777/forwarding-x11-over-ssh-if-the-server-configuration-doesnt-allow-it>) uses Xephyr as a work around to be installed in the ssh client machine.
