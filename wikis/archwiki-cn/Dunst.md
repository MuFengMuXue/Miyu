相关文章

  * [桌面通知程序](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%80%9A%E7%9F%A5%E7%A8%8B%E5%BA%8F.html> "桌面通知程序")

**翻译状态：**

  * 本文（或部分内容）译自 [Dunst](<https://wiki.archlinux.org/title/Dunst> "arch:Dunst")，最近一次同步于 2026-03-25，若英文版本有所[更改](<https://wiki.archlinux.org/title/Dunst?diff=0&oldid=857932>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Dunst_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Dunst](<https://dunst-project.org/>) 是大多数桌面环境提供的通知守护程序的轻量级替代品。 

dunst 可以在 X11 或 Wayland 下运行。 

##  安装

安装 [dunst](<https://archlinux.org/packages/?name=dunst>)包 软件包。 

示例配置文件位于 `/etc/dunst/dunstrc`。将其复制到 `~/.config/dunst/dunstrc` 并进行编辑。 

启动 `/usr/bin/dunst`，确保您的窗口管理器或桌面环境在启动/登录时启动 Dunst 。 

**注意：** 您似乎无需手动启动 Dunst，因为当应用程序向 D-Bus 发送通知时，dbus-daemon 会自动启动 Dunst。然而，通知服务经常会安装多个守护进程，且无法知晓应当自动启动哪一个。dbus-daemon 的维护者曾明确警告不要依赖自动启动多提供者服务。

##  外观

可为通知内的文本添加样式如粗体、斜体、删除线或下划线。完整参考见 [Pango 标记](<https://docs.gtk.org/Pango/pango_markup.html>)。若 `markup` 被设为 `none`，Pango 就会从通知中被移除。 

通知的格式可被明确规定，选项如下： 
    
    %a  应用名称
    %s  摘要
    %b  主体内容
    %i  图标名称（包含路径）
    %I  图标名称（无需路径）
    %p  进度（需要另外设定，[0%] - [100%]）
    
它们可以与 HTML 标签结合起来使用。例如将 `format` 设为 `<b>%s</b>\n%b` 来显示加粗的摘要、换行和无格式的主体内容。 

###  设定图标

在配置文件的 `global` 节 `icon_path` 项中设定图标。需要状态（status）、设备（device）和传统（legacy）图标。默认情况下，Dunst 会查找 [gnome-icon-theme](<https://aur.archlinux.org/packages/gnome-icon-theme/>)AUR 图标。若要使用 [adwaita-icon-theme](<https://archlinux.org/packages/?name=adwaita-icon-theme>)包替换 gnome-icon-theme，请改为： 
    
    icon_path = /usr/share/icons/Adwaita/16x16/status/:/usr/share/icons/Adwaita/16x16/devices/:/usr/share/icons/Adwaita/16x16/legacy/
    
除了直接指定图标文件夹的路径，您也可以在 `global` 节中直接指定图标主题。若如此，您需要设置 `enable_recursive_icon_lookup=true` 以在主题主文件夹的子文件夹中进行搜索。 

例如： 
    
    icon_theme = Papirus
    enable_recursive_icon_lookup = true
    
##  快捷键

使用 _dunstctl_ 控制 Dunst。您可以更新您的[快捷键](<../zh-cn/%E5%BF%AB%E6%8D%B7%E9%94%AE.html> "快捷键")来使用 _dunstctl_ 。 

例如，关闭所有通知： 
    
    $ dunstctl close-all
    
显示历史记录： 
    
    $ dunstctl history-pop
    
##  规则

你可以在你的 dunstrc 文件中创建匹配某些通知的规则，然后执行某些操作比如运行一个脚本。 

###  匹配通知

要创建新的规则，请在您的配置文件中创建一个自定义命名的节， 您可以使用属性 appname（应用名）、summary（摘要）、body（主体）、icon（图标）、category（类别）、match_transient（瞬态通知）和 msg_urgency（紧急程度）来匹配通知。 支持通配符。请在[#脚本](<#%E8%84%9A%E6%9C%AC>)查看示例。 用 `-print` 选项启动 Dunst 以在通知中寻找有用的信息来编写合适的规则。关于各属性的详细解释，请参阅 [dunst(5) § filtering](<https://man.archlinux.org/man/dunst.5#filtering>)。 

###  修改格式

当匹配到一条通知时，您可以对其格式进行修改，只需修改 `format` 选项。这在您想完全忽略某些特定的通知时尤其有用。若如此做，您只需将 `format=""` 行添加到您的规则（该规则会把匹配到的通知改成空的）。 

另一个有用的特性是您可以完全将某些通知从历史记录中排除，例如您想[将 Dunst 用作音量指示器](<#%E5%B0%86_dunstify_%E7%94%A8%E4%BD%9C%E9%9F%B3%E9%87%8F/%E4%BA%AE%E5%BA%A6%E6%B0%B4%E5%B9%B3%E6%8C%87%E7%A4%BA%E5%99%A8>)，只需将 `history_ignore=yes` 行添加到相应的规则。 

###  脚本

Dunst 可以根据某些通知内容来运行脚本，以下是一个当某来自 [pidgin](<https://aur.archlinux.org/packages/pidgin/>)AUR 的人登录时，Dunst 运行脚本的示例： 
    
    [signed_on]
       appname = Pidgin
       summary = "*signed on*"
       urgency = low
       script = do_something.sh
    
指定的脚本将按以下参数的顺序来匹配：appname（应用名）、summary（摘要）、body（主体内容）、icon（图标）、urgency（紧急程度）。 

##  暂停 Dunst

有两种方法暂停 Dunst： 

使用 `dunstctl`
    您可以执行 `dunstctl set-paused true/false/toggle` 来禁用/重新启用/切换通知状态。执行 `dunstctl is-paused` 来查看 Dunst 是否在运行/暂停。

使用 `killall`
    执行 `killall -SIGUSR1 dunst` 来禁用，执行 `killall -SIGUSR2 dunst` 来重新启用。

一旦暂停，Dunst 会保留所有通知。再次启用 Dunst 后，将显示所有保留的通知。 

## Dunstify

Dunstify 是 [notify-send](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%80%9A%E7%9F%A5%E7%A8%8B%E5%BA%8F.html#Libnotify> "Notify-send") 命令的替代品， 它完全兼容 notify-send 且可以与其一起使用，但它提供了更多功能。 

除了 notify-send 中可用的一些选项，Dunstify 还提供一些其他特性如 ID 和 action（行为）。 

###  替换通知

您可以给 dunstify 加上 `-r ID` 选项来给一条通知分配 ID，其中 `ID` 必须是整数。 如果拥有某 ID 的通知已经存在，那么它将会被具有相同 ID 的新通知替换。 您亦可使用 `dunstify -C ID` 来关闭一条通知。 

然而，在大部分情况下，使用标签（tag）比控制 ID 更可取，因为后者有很多陷阱[[1]](<https://github.com/dunst-project/dunst/issues/672>)。在调试或面对非常复杂的通知发送者时，请考虑替换 ID[[2]](<https://github.com/dunst-project/dunst/issues/672#issuecomment-554530659>)。 

具有相同标签（tag，本例中的 tag 是 test）的通知会被替换且无视 ID。 
    
    $ dunstify -h string:x-dunst-stack-tag:test Test -A 'tested,default'
    $ dunstify -h string:x-dunst-stack-tag:test Testing
    
###  行为

您可以从一个或多个 `--action=action,label` 参数中定义可以直接调用的行为。 例如： 
    
    $ dunstify --action="replyAction,reply" "Message received"
    
然后用户可以通过 Dunst 的上下文菜单来做出某些行为，发送到 dunstify 的某些请求会被阻止除非通知消失或一个行为已被选择。在前一种情况下，若通知超时，则 Dunstify 会返回1；若通知被手动关闭，Dunstidy 会返回2[[3]](<https://specifications.freedesktop.org/notification-spec/latest/protocol.html#signals>)。而在后一种情况下，会返回在上下文菜单中选择的行为。 

除了通过上下文菜单调用行为，您也可以通过鼠标事件调用行为[[4]](<https://github.com/dunst-project/dunst/blob/3f3082efb3724dcd369de78dc94d41190d089acf/dunstrc#L237>)。这可使 Dunst 更具交互性，[这里](<https://github.com/dunst-project/dunst/issues/163#issuecomment-573191650>)也建议这样做。当通知只有一个行为或一个行为被命名为 “default” 时，您可以单击鼠标中键来调用这个行为。（Dunst 默认如此，当然您也可以在 `dunstrc` 中定义 `mouse_middle_click = do_action`). 
    
    reply_action () {}
    forward_action () {}
    handle_dismiss () {}
    
    ACTION=$(dunstify --action="default,Reply" --action="forwardAction,Forward" "Message Received")
    
    case "$ACTION" in
    "default")
        reply_action
        ;;
    "forwardAction")
        forward_action
        ;;
    "2")
        handle_dismiss
        ;;
    esac
    
##  提示与技巧

###  将 dunstify 用作音量/亮度水平指示器

您可以使用替换 ID 功能来实现简单的音量或亮度指示器通知，如图所示 [[5]](<https://i.postimg.cc/j2CDkS1H/screen1712.png>)。 

要实现音量指标，请将以下脚本放在 `PATH` 中的某个位置。 
    
    #!/bin/bash
    # changeVolume
    
    # Arbitrary but unique message tag
    msgTag="myvolume"
    
    # Change the volume using alsa(might differ if you use pulseaudio)
    amixer -c 0 set Master "$@" > /dev/null
    
    # Query amixer for the current volume and whether or not the speaker is muted
    volume="$(amixer -c 0 get Master | tail -1 | awk '{print $4}' | sed 's/[^0-9]*//g')"
    mute="$(amixer -c 0 get Master | tail -1 | awk '{print $6}' | sed 's/[^a-z]*//g')"
    if [[ $volume == 0 || "$mute" == "off" ]]; then
        # Show the sound muted notification
        dunstify -a "changeVolume" -u low -i audio-volume-muted -h string:x-dunst-stack-tag:$msgTag "Volume muted" 
    else
        # Show the volume notification
        dunstify -a "changeVolume" -u low -i audio-volume-high -h string:x-dunst-stack-tag:$msgTag \
        -h int:value:"$volume" "Volume: ${volume}%"
    fi
    
    # Play the volume changed sound
    canberra-gtk-play -i audio-volume-change -d "changeVolume"
    
现在只需将 `changeVolume 2dB+ unmute` 等绑定到某个热键上即可。您可能还想让 dunst 在历史记录中忽略此类通知，请参阅[#修改格式](<#%E4%BF%AE%E6%94%B9%E6%A0%BC%E5%BC%8F>)。 

###  覆盖以前的通知

对于某些通知（例如声音或亮度），你可能希望覆盖之前的通知。你可以使用[#替换通知](<#%E6%9B%BF%E6%8D%A2%E9%80%9A%E7%9F%A5>)中的 Dunst 方法，也可以参考[桌面通知程序#替换之前的通知](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%80%9A%E7%9F%A5%E7%A8%8B%E5%BA%8F.html#%E6%9B%BF%E6%8D%A2%E4%B9%8B%E5%89%8D%E7%9A%84%E9%80%9A%E7%9F%A5> "桌面通知程序")，了解更一般的示例。 

##  疑难解答

###  Dunst 无法通过 systemd 启动

在无登录管理器的情况下使用 Dunst 时，`DISPLAY` 环境变量可能不会被正确设置[[6]](<https://github.com/dunst-project/dunst/issues/347>)。 

欲修复，请添加以下行到您的 `.xinitrc` 文件： 
    
    systemctl --user import-environment DISPLAY
    
**提示：** 这在最近版本的 [systemd](<../zh-cn/Systemd.html> "Systemd") 上会自动作为 `/etc/X11/xinit/xinitrc.d/50-systemd-user.sh` 的一部分被执行。

###  字体大小不匹配（表情比字大）

这是因为 [fontconfig](<https://archlinux.org/packages/?name=fontconfig>)包 没有重新调节位图字体。您通常会在某些表情符号上注意到这个问题。（例如：[noto-fonts-emoji](<https://archlinux.org/packages/?name=noto-fonts-emoji>)包 ） 

要解决这个问题，只需执行： 
    
    # ln -s /etc/fonts/conf.avail/10-scale-bitmap-fonts.conf /etc/fonts/conf.d/
    
并重启 Dunst。 

###  部分应用程序的通知不遵守超时规则

这个问题具体表现为所有紧急级别的通知超时配置为 30 秒，但是来自特定应用如 Discord 、Mattermost 和 GitLab 的通知消失得很快（典型表现为3秒）。 

您可以在上游找到更多细节：[issue #276](<https://github.com/dunst-project/dunst/issues/276>)。 

这是由于通知被强制关闭而发生的。要解决这个问题，您需要引入一个名为 `ignore_dbusclose` 的特殊参数。您可以通过启用该参数来忽略通过 D-Bus 发送的 `closeNotification` 消息。启用该参数可以确保应用程序通知遵循 Dunst 的配置。默认情况下，该参数是关闭（被设定为 false）的。 

##  参见

  * [Dunst 官方网站](<https://dunst-project.org/>)

  * [Dunst Github 仓库](<https://github.com/dunst-project/dunst>)

  * [Dunst FAQ](<https://dunst-project.org/faq/>)

  * [Dunst 文档](<https://dunst-project.org/documentation/>)
