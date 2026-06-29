**翻译状态：**

  * 本文（或部分内容）译自 [Acpid](<https://wiki.archlinux.org/title/Acpid> "arch:Acpid")，最近一次同步于 2022-12-17，若英文版本有所[更改](<https://wiki.archlinux.org/title/Acpid?diff=0&oldid=761293>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Acpid_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [ACPI modules](<../zh-cn/ACPI_modules.html> "ACPI modules")
  * [DSDT](<../zh-cn/DSDT.html> "DSDT")

[acpid2](<http://acpid2.sourceforge.net/>)是用于处理电源相关事件的守护进程，它非常灵活且易于扩展。当某个事件发生时，执行相关程序来处理该事件。这些事件是由某些动作触发的，比如： 

  * 按下电源按钮
  * 按下睡眠/挂起按钮
  * 合上笔记本盖子
  * 拔下/插上笔记本外接电源

**警告：** 请注意[桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")比如[GNOME](<../zh-cn/GNOME.html> "GNOME")，[systemd](<../zh-cn/Power_management.html#ACPI_events> "Power management") 和 [额外按键处理进程](<../zh-cn/Extra_keyboard_keys.html> "Extra keyboard keys")会有它自己的一套管理方法。同时运行多套系统可能产生意想不到的结果，比如，当按下电源键时电脑同时执行挂起和关机；或者当按下睡眠按钮时电脑执行了两次挂起操作。所以，使用多套系统时你应只激活一套系统的电源事件管理方法，以免引起冲突。

##  安装

使用[Pacman](<../zh-cn/Pacman.html> "Pacman") 安装 [acpid](<https://archlinux.org/packages/?name=acpid>)包。 然后 [start/enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start/enable") `acpid.service`. 

##  配置

###  确定事件名称

不幸的是计算机上的这些电源事件标识并不统一，比如，在一些计算机上睡眠按钮可能被标识为 _SLPB_ ，而在另一些计算机上为 _SBTN_ 。 

要想确定各种按钮或`Fn`快捷键在你的计算机上是如何定义的： 
    
    # journalctl -f
    
现在在你计算机上按下电源按钮或睡眠按钮（比如`Fn+Esc`），你会得到类似以下的结果： 
    
    logger: ACPI action undefined: PBTN
    logger: ACPI action undefined: SBTN
    
如果这不起作用的话，运行： 
    
    # acpi_listen
    
或者[openbsd-netcat](<https://archlinux.org/packages/?name=openbsd-netcat>)包： 
    
    $ netcat -U /var/run/acpid.socket
    
然后按下电源按钮，你会看到类似以下输出： 
    
    button/power PBTN 00000000 00000b31
    
`acpi_listen`的输出会被作为$1, $2 , $3 & $4参数发送给`/etc/acpi/handler.sh`。 举例： 
    
    $1 button/power
    $2 PBTN
    $3 00000000
    $4 00000b31
    
###  定义事件动作

[acpid](<https://archlinux.org/packages/?name=acpid>)包预置了许多事件触发行为，比如它定义了当你按下电源按钮时应当发生什么。这些触发行为默认在`/etc/acpi/handler.sh`中定义。在`/etc/acpi/events/anything`)规定：任何侦测到的电源事件都会按照`/etc/acpi/handler.sh`中定义的触发行为执行相关动作。 

下面是一个定义触发行为的简单例子。在这个例子中，当按下睡眠按钮时acpid运行命令`echo -n mem >/sys/power/state`，这将会使你的电脑挂起： 
    
    button/sleep)
        case "$2" in
            SLPB) echo -n mem >/sys/power/state ;;
    	 *)    logger "ACPI action undefined: $2" ;;
        esac
        ;;
    
如果睡眠按钮被识别为 _SBTN_ ，而不是 `/etc/acpi/handler.sh`中默认定义的 _SLPB_ （这是标识符）。需要编辑`/etc/acpi/handler.sh`把 _SLPB)_ 替换为 _SBTN)_ 。 

参照上面的例子，你应该可以很容易的通过定制`/etc/acpi/handler.sh`来根据侦测到的电源时间来执行不同的命令。更多例子可参考下面的[小技巧](<#%E5%B0%8F%E6%8A%80%E5%B7%A7>)部分。 

**注意：** Events such as `button/power`, `button/lid`, `button/suspend` and `button/hibernate` are handled by [systemd-logind.service(8)](<https://man.archlinux.org/man/systemd-logind.service.8>) by default, see [Power management#Power management with systemd](<../zh-cn/Power_management.html#Power_management_with_systemd> "Power management"). If handling these events with _acpid_ , the handling of these events by logind should either be disabled first, or inhibited.

###  其它配置方案

默认所有的电源事件都是交由`/etc/acpi/handler.sh`处理的。这是由`/etc/acpi/events/anything`规定的： 
    
    # Pass all events to our one handler script
    event=.*
    action=/etc/acpi/handler.sh %e
    
尽管这样配置工作起来没有任何问题，但一些用户可能更喜欢使用各自独立的脚本来定义不同的电源事件。下面举例说明了如何使用不同的事件定义文件和行为定义文件： 

作为root，创建以下文件： 
    
    /etc/acpi/events/sleep-button
    
    event=button sleep.*
    action=/etc/acpi/actions/sleep-button.sh %e

然后建立以下文件： 
    
    /etc/acpi/actions/sleep-button.sh
    
    #!/bin/sh
    case "$3" in
        SLPB) echo -n mem >/sys/power/state ;;
        *)    logger "ACPI action undefined: $3" ;;
    esac

最后，给脚本加上 [executable 可执行权限](</wzh/index.php?title=Executable_%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90&action=edit&redlink=1> "Executable 可执行权限（页面不存在）")： 并 [reload](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Reload") `acpid.service`。 

这种方法可以简化的独立事件和行为脚本的处理。 

##  小技巧

**注意：** 一些在这里描述的动作，例如无线网络切换和背光控制，可能已经由驱动直接管理。在这种情况下，您应该查询相应的内核模块。

###  脚本示例

下面给出的例子可以用在你的`/etc/acpi/handler.sh`脚本中，只是在使用的时候记得将事件变量更改为`acpi_listen`侦测到的那个。 

实现插拔外接电源时自动设置屏幕亮度（数值可能需要调整，参考`/sys/class/backlight/acpi_video0/max_brightness`）： 
    
    ac_adapter)
        case "$2" in
            AC*|AD*)
                case "$4" in
                    00000000)
                        echo -n 50 > /sys/class/backlight/acpi_video0/brightness
                        ;;
                    00000001)
                        echo -n 100 > /sys/class/backlight/acpi_video0/brightness
                        ;;
                esac
    
### Enabling backlight control

Similar to volume control, acpid also enables you to control screen backlight. To achieve this you write some handler, like this: 
    
    /etc/acpi/handlers/bl
    
    #!/bin/sh
    bl_dev=/sys/class/backlight/acpi_video0
    step=1
    
    case $1 in
      -) echo $(($(< $bl_dev/brightness) - $step)) >$bl_dev/brightness;;
      +) echo $(($(< $bl_dev/brightness) + $step)) >$bl_dev/brightness;;
    esac

and again, connect keys to ACPI events: 
    
    /etc/acpi/events/bl_d
    
    event=video/brightnessdown.*
    action=/etc/acpi/handlers/bl -
    
    /etc/acpi/events/bl_u
    
    event=video/brightnessup.*
    action=/etc/acpi/handlers/bl +

###  音量调整

下面的一系列脚本是用来控制音量的。用上面讲到的方法找到音量键的标识符，然后替换掉下面文件中的事件标识就可以用在自己电脑上了： 
    
    /etc/acpi/events/vol-d
    
    event=button/volumedown
    action=amixer set Master 5-
    
    /etc/acpi/events/vol-m
    
    event=button/mute
    action=amixer set Master toggle
    
    /etc/acpi/events/vol-u
    
    event=button/volumeup
    action=amixer set Master 5+

**注意：** 这些命令在 PulseAudio 下可能有问题[[1]](<https://lists.freedesktop.org/archives/pulseaudio-discuss/2015-December/025062.html>)。要实现全部功能，以当前用户执行并将设置 `XDG_RUNTIME_DIR` 环境变量 [environment variable](<../zh-cn/Environment_variable.html> "Environment variable"),例如 `# sudo -u _user_ XDG_RUNTIME_DIR=/run/user/_1000_ pactl`.

**提示：** 在 Xorg 中禁用或绑定这些音量按键，以避免和其他程序冲突。详情请参考或 [Xmodmap](<../zh-cn/Xmodmap.html> "Xmodmap").

参阅 [[2]](<https://web.archive.org/web/20150711044207/http://blog.lastlog.de/posts/fixing_volume_change_in_linux>). 

### Disabling ordinary key events

Since [b336c96](<https://sourceforge.net/p/acpid2/code/ci/b336c96e32c959ed3df15eaf5669f47ea589d977/>) acpid generates events for some ordinary key presses, such as arrow keys. This results in event/handler spam, visible in system logs or _top_. Events for these buttons can be dropped in the configuration file: 
    
    /etc/acpi/events/buttons
    
    event=button/(up|down|left|right|kpenter)
    action=<drop>

###  获取当前登录的用户名

你可以使用`getuser`函数来获取当前登录的用户名： 
    
    getuser ()
        {
         export DISPLAY=`echo $DISPLAY | cut -c -2`
         user=`who | grep " $DISPLAY" | awk '{print $1}' | tail -n1`
         export XAUTHORITY=/home/$user/.Xauthority
         eval $1=$user
        }
    
然后这个函数就可以被用在下面的例子中，它可以在你按下电源按钮时正常的关闭[KDE](<../zh-cn/KDE.html> "KDE")： 
    
    button/power)
        case "$2" in
            PBTN)
                getuser "$user"
                echo $user > /dev/tty5
                su $user -c "dcop ksmserver ksmserver logout 0 2 0"
                ;;
              *) logger "ACPI action undefined $2" ;;
        esac
        ;;
    
####  连接到 acpid 套接字

除了规则文件之外，acpid 也接受 UNIX 域套接字连接，默认是 `/var/run/acpid.socket`. 用户程序可以连接到此套接字。 
    
    #!/bin/bash
    coproc acpi_listen
    trap 'kill $COPROC_PID' EXIT
    
    while read -u "${COPROC[0]}" -a event; do
        _handler.sh_ "${event[@]}"
    done
    
_handler.sh_ 可以参考 `/etc/acpi/handler.sh`. 

### Disable keyboard and touchpad while laptop lid is closed under Wayland

This example uses [inhibited](<https://www.phoronix.com/news/Linux-5.11-Inhibited-Input>) property of input device drivers as a replacement for xinput which does not work under Wayland. 
    
    	button/lid)
    		if echo "$3" | grep -iq "open"; then
    			echo 'LID opened'
    			disabled=0
    		fi
    		if echo "$3" | grep -iq "close"; then
    			echo 'LID closed'
    			disabled=1
    		fi
    		find /sys/devices/platform/i8042/serio* -prune -type d | while IFS= read -r serionumber; do
    			find $serionumber/input/* -prune -type d | while IFS= read -r inputdevicepath; do
    				if grep -q -i -e "keyboard" -e "touchpad" $inputdevicepath/name; then
    					logger "found $(cat $inputdevicepath/name) and set to $disabled"
    					echo $disabled > $inputdevicepath/inhibited
    				fi
    			done
    		done
    	;;
    
##  参考

  * <http://acpid.sourceforge.net/> \- acpid 主页
  * [Gentoo:ACPI#Configuration](<https://wiki.gentoo.org/wiki/ACPI#Configuration> "gentoo:ACPI")
