**翻译状态：**

  * 本文（或部分内容）译自 [Display Power Management Signaling](<https://wiki.archlinux.org/title/Display_Power_Management_Signaling> "arch:Display Power Management Signaling")，最近一次同步于 2017-11-20，若英文版本有所[更改](<https://wiki.archlinux.org/title/Display_Power_Management_Signaling?diff=0&oldid=497169>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Display_Power_Management_Signaling_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

**[DPMS](<https://en.wikipedia.org/wiki/VESA_Display_Power_Management_Signaling> "wikipedia:VESA Display Power Management Signaling")** (显示电源管理信号，简称DPMS) 可以在计算机一定时间无操作时，将显示器置于节电模式。具体的时间设置可以参考 [[1]](<https://linux.die.net/man/3/dpmssettimeouts>). 注意有些显示器在不同 DPMS 状态下表现不变。 

##  在 X 中设定 DPMS

**注意：** 从 Xorg 1.8 开始，只要内核启用了 ACPI， DPMS 就会自动启用。

在 `/etc/X11/xorg.conf` 的 `Monitor` 段落中加上上: 
    
    Option "DPMS" "true"
    
把下面的配置加入 `ServerLayout` 小节, 必要时改变时间(以分钟计): 
    
    Option "StandbyTime" "10"
    Option "SuspendTime" "20"
    Option "OffTime" "30"
    
**注意：** If the _"OffTime"_ option does not work replace it with the following, (change the _"blanktime"_ to _"0"_ to disable screen blanking) 
    
    Option         "BlankTime" "30"
    
比较新的X推荐使用 `.conf` 文件代替 `xorg.conf`, `/etc/X11/xorg.conf.d/10-monitor.conf` 的一个例子如下： 
    
    Section "Monitor"
        Identifier "LVDS0"
        Option "DPMS" "false"
    EndSection
    
    Section "ServerLayout"
        Identifier "ServerLayout0"
        Option "BlankTime"  "0"
        Option "StandbyTime" "0"
        Option "SuspendTime" "0"
        Option "OffTime" "0"
    EndSection
    
##  用xset修改DPMS和屏保设定

可以用 [xorg-xset](<https://archlinux.org/packages/?name=xorg-xset>)包 提供的`xset`工具关闭屏幕。如果要在shell中关闭显示器，需要在命令前面加上 `sleep 1;` . 例如： 
    
    sleep 1; xset dpms force off
    
命令示例： 

命令  | 描述   
---|---  
xset s off  | 禁用屏保清空   
xset s 3600 3600  | 将清空时间设置到 1 小时   
xset -dpms  | 关闭 DPMS   
xset s off -dpms  | 禁用 DPMS 并阻止屏幕清空   
xset dpms force off  | 立即关闭屏幕   
xset dpms force standby  | 待机界面   
xset dpms force suspend  | 休眠界面   
  
**注意：** 通过 `dpms 0 0 0` 可以将 DPMS 超时都设置成零，这样也可以禁用 DPMS. 这种方式更方便，可以使用 `xset dpms force off` 关闭屏幕。

查看当前设置: 
    
    $ xset q
    
    ...
    
    Screen Saver:
      prefer blanking:  yes    allow exposures:  yes
      timeout:  600    cycle:  600
    DPMS (Energy Star):
      Standby: 600    Suspend: 600    Off: 600
      DPMS is Enabled
      Monitor is On
    
运行 `xset` 可以查看全部可用命令. 

**注意：** 如果在 [xinitrc](<../zh-cn/Xinit.html#xinitrc> "Xinitrc") 中使用 `xset` 无法工作，在配置文件中进行设置。

**警告：**[XScreenSaver](<../zh-cn/XScreenSaver.html> "XScreenSaver") 和 [xfce4-power-manager](<https://archlinux.org/packages/?name=xfce4-power-manager>)包 会使用自己的 DPMS 设置，详情参考 [XScreenSaver#DPMS and blanking settings](<../zh-cn/XScreenSaver.html#DPMS_and_blanking_settings> "XScreenSaver") 和 [Xfce#Display blanking](<../zh-cn/Xfce.html#Display_blanking> "Xfce").

##  Linux 终端和 DPMS 的交互

_setterm_ 工具可以通过终端能够识别的转义字符修改终端。可以写入/echo 终端序列到当前终端设备，包括再显示设备，远程 SSH 终端， 控制台，串口控制台。 

setterm Syntax: (0 disables) 
    
    setterm -blank [0-60|force|poke]
    setterm -powersave [on|vsync|hsync|powerdown|off]
    setterm -powerdown [0-60]
    
###  防止屏幕关闭

可以运行以下命令： 
    
    $ setterm -blank 0 -powerdown 0
    
也可以通过下列命令禁止终端清空: 
    
    # echo -ne "\033[9;0]" >> /etc/issue
    
将分号后的 0 修改为 3 会在 3 分钟后进入休眠模式。 

###  通过 cat 显示输出中的转义
    
    $ setterm -powerdown 2>&1 | exec cat -v 2>&1 | sed "s/\\^\\[/\\\\033/g"
    
###  将转义输出到任意 tty (with write/append perms) 进行终端修改
    
    $ setterm -powerdown 0 >> /dev/tty3
    
**注意：** 使用 `>>` 而不是 `>`. 如果脚本有 _sudo_ 权限问题，tty 可能允许附加但是不允许写入， 可以使用 **tee** 阻止 setterm 输出到 tty 。

####  用循环设置 ttys 0-256
    
    $ for i in {0..256}; do setterm -powerdown 0 >> /dev/tty$i; done; unset i;
    
##  参阅

  * [PC Monitor DPMS specification explanation](<http://webpages.charter.net/dperr/dpms.htm>)
  * [DPMS control in X](<https://ptspts.blogspot.be/2009/10/screen-blanking-dpms-screen-saver.html>)
