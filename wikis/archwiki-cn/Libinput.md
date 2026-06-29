**翻译状态：**

  * 本文（或部分内容）译自 [Libinput](<https://wiki.archlinux.org/title/Libinput> "arch:Libinput")，最近一次同步于 2022-05-18，若英文版本有所[更改](<https://wiki.archlinux.org/title/Libinput?diff=0&oldid=729925>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Libinput_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Xorg](<../zh-cn/Xorg.html> "Xorg")
  * [Touchpad Synaptics](<../zh-cn/Touchpad_Synaptics.html> "Touchpad Synaptics")
  * [Wayland](<../zh-cn/Wayland.html> "Wayland")

来自[libinput](<https://freedesktop.org/wiki/Software/libinput/>) wiki 项目 

    libinput 是一个函数库，在 Wayland 上用来接收设备的输入，在 X.Org 上提供输入设备的驱动。它提供对设备事件的检测和接收。对输入设备信号进行处理。它提供了一些列的函数供用户使用。

需要注意的是， X.Org 输入驱动为大多数常规[输入设备](<../zh-cn/Xorg.html#Input_devices> "Xorg")提供了支持，libinput 项目的目标是为触摸板和触摸屏的触摸功能（如多点触控、手势等）提供高级支持。详情请参见 [libinput 文档](<https://wayland.freedesktop.org/libinput/doc/latest/>)。 

##  安装

一般不需要手动安装. 

  * 在 [Wayland](<../zh-cn/Wayland.html> "Wayland") 系统中，[libinput](<https://archlinux.org/packages/?name=libinput>)包 包是所有 Wayland 图形环境的依赖包并且已经安装，不需要其它的输入驱动。
  * 在 [Xorg](<../zh-cn/Xorg.html> "Xorg") 系统中，[xf86-input-libinput](<https://archlinux.org/packages/?name=xf86-input-libinput>)包 包也是默认依赖。这个软件包是 libinput 的一个包装（wrapper），能够使 libinput 用于 X 上的输入设备，可以作为 evdev 和 synaptics 的替代品 [[1]](<https://freedesktop.org/wiki/Software/libinput/>)。代替其他用于 X 输入的软件包（即以 `xf86-input-` 为前缀的软件包）。

[libinput-tools](<https://archlinux.org/packages/?name=libinput-tools>)包软件包带有 `libinput` 命令，无论使用哪种显示服务器，都可以用它来调试函数库与硬件之间的交互。 

##  配置

在 [Wayland](<../zh-cn/Wayland.html> "Wayland") 上, 没有关于 libinput 的配置文件。 可配置内容由你使用的桌面环境对 libinput 的支持情况决定（参见 [#图形工具](<#%E5%9B%BE%E5%BD%A2%E5%B7%A5%E5%85%B7>) 部分），或者使用与桌面环境无关的 [udev](<../zh-cn/Udev.html> "Udev") 规则来实现（参见 [Calibrating Touchscreen#Do it automatically via a udev rule](<https://wiki.archlinux.org/title/Calibrating_Touchscreen#Do_it_automatically_via_a_udev_rule> "en:Calibrating Touchscreen")和 [#使用 udev 规则](<#%E4%BD%BF%E7%94%A8_udev_%E8%A7%84%E5%88%99>)）。要配置那些桌面环境尚未支持的选项（例如 [GNOME](<../zh-cn/GNOME.html> "GNOME") 的触摸板滚动速度），可以先借助 [libinput-config-git](<https://aur.archlinux.org/packages/libinput-config-git/>)AUR，该工具的可选配置项已于 [libinput-config README](<https://gitlab.com/warningnonpotablewater/libinput-config>) 列出。 

对于 [Xorg](<../zh-cn/Xorg.html> "Xorg"), 默认的配置文件安装在 `/usr/share/X11/xorg.conf.d/40-libinput.conf`。一般没有必要使用额外的配置文件来检测键盘，触摸板，指点杆（小红点）和触摸屏。 

###  使用 xinput

首先，执行: 
    
    # libinput list-devices
    
这将会输出系统中的设备和它们被 libinput 支持的具体特性。 

重启图形环境之后，如果没有其它驱动程序被配置为优先，设备应由具有默认配置的 libinput 管理。 

参见 [libinput(4)](<https://man.archlinux.org/man/libinput.4>) 了解可设定的常规选项和一些参数信息。 _xinput_ 工具用于查看或更改运行中的特定设备的设置。例如： 

查看所有设备并确定其名称和编号： 
    
    $ xinput list
    
查看 _device_ 的设置 （在下文中，` _device_` 表示要操作的设备的名称或编号）： 
    
    $ xinput list-props _device_
    
修改 _device_ 的某项设置： 
    
    $ xinput set-prop _device_ _option_ _setting_
    
上文中 `_option_` 既可以是设置项的名称，也可以是其对应编号。 例如，修改“libinput Click Method Enabled (303)”项目的两个值，可以使用以下命令： 
    
    $ xinput set-prop 14 303 {1 1}
    
或者 
    
    $ xinput set-prop 14 "libinput Click Method Enabled" 1 1
    
###  使用 Xorg 配置文件

参见 [Xorg#Using .conf files](<../zh-cn/Xorg.html#Using_.conf_files> "Xorg") 了解永久的选项设置。[Logitech Marble Mouse#libinput](<../zh-cn/Logitech_Marble_Mouse.html#libinput> "Logitech Marble Mouse") 和 [#设置按键映射](<#%E8%AE%BE%E7%BD%AE%E6%8C%89%E9%94%AE%E6%98%A0%E5%B0%84>)中列举了几个例子。 

[Xorg#Input devices](<../zh-cn/Xorg.html#Input_devices> "Xorg") 的替代驱动程序通常可以同时安装。如果您打算将一个设备的驱动程序切换到 libinput，请确保没有在 `/etc/X11/xorg.conf.d/` 的配置文件中为其它驱动程序配置优先。 

**提示：** 如果你同时安装了 libinput 和 synaptics 并使用其默认配置（即 `/etc/X11/xorg.conf.d/` 中没有属于两者中任一的文件），synaptics 将因其在默认安装目录中拥有更高的数字顺序 `70-` 而获得较高优先级。为了避免这种情况，您可以将默认的 libinput 配置文件（`40-libinput.conf`）符号链接到目录搜索顺序优先于 `70-synaptics.conf` 的 `/etc/X11/xorg.conf.d/` 中去取代它： 
    
    # ln -s /usr/share/X11/xorg.conf.d/40-libinput.conf /etc/X11/xorg.conf.d/40-libinput.conf
    
如果在 `/etc/X11/xorg.conf.d/` 目录下这两个配置文件***同时存在***，libinput 的配置一定是处于较低优先级的；参见 [Xorg#Using .conf files](<../zh-cn/Xorg.html#Using_.conf_files> "Xorg")。如果要禁用 libinput（并回退到较旧的驱动程序）， 只需从 `/etc/X11/xorg.conf.d/` 中删除之前创建的符号链接即可。

**提示：** 如果配置文件不起作用，请检查非特权用户是否拥有该文件读取权限

检查哪些设备是由 libinput 管理的一种方法是查看 [xorg 日志文件](<../zh-cn/Xorg.html#General> "Xorg")。以下是一个例子： 
    
    $ grep -e "Using input driver 'libinput'" _/path/to/Xorg.0.log_
    
    [    28.799] (II) Using input driver 'libinput' for 'Power Button'
    [    28.847] (II) Using input driver 'libinput' for 'Video Bus'
    [    28.853] (II) Using input driver 'libinput' for 'Power Button'
    [    28.860] (II) Using input driver 'libinput' for 'Sleep Button'
    [    28.872] (II) Using input driver 'libinput' for 'AT Translated Set 2 keyboard'
    [    28.878] (II) Using input driver 'libinput' for 'SynPS/2 Synaptics TouchPad'
    [    28.886] (II) Using input driver 'libinput' for 'TPPS/2 IBM TrackPoint'
    [    28.895] (II) Using input driver 'libinput' for 'ThinkPad Extra Buttons'

这是一台 `/etc/X11/xorg.conf.d/` 中没有任何配置文件的笔记本电脑，也就是说，设备是被自动检测出来的。 

当然，你可以选择为一个设备使用替代的驱动程序，而为其它设备选择 libinput。许多因素可能会影响到底使用哪个驱动程序。举个例子，与 [Touchpad Synaptics](<../zh-cn/Touchpad_Synaptics.html> "Touchpad Synaptics") 相比，libinput 驱动程序能根据自己的喜好去自定义触摸板行为的选项较少，但处理多点触控事件的程序逻辑要多得多（例如，手掌检测）。因此，如果你在使用某个驱动程序的时候，在硬件上遭遇了问题，那么尝试一下替代驱动程序是合理的。 

自定义配置文件应放在 `/etc/X11/xorg.conf.d/` 中，并且遵循被广泛使用的命名模式，通常选择 `30-touchpad.conf` 作为文件名。 

**提示：** 阅读 `/usr/share/X11/xorg.conf.d/40-libinput.conf` 中的详细配置以获取指导并参考 [libinput(4)](<https://man.archlinux.org/man/libinput.4>) 手册页获取有关可用配置选项的详细说明

一个基本的配置应该遵循以下的结构： 
    
    /etc/X11/xorg.conf.d/30-touchpad.conf
    
    Section "InputClass"
        Identifier "devname"
        Driver "libinput"
        ...
    EndSection
    
你可以在单个配置文件中定义任意多的 Section（通常每个输入设备只配置一个 Section） 要配置你选择的设备，请指定 [xorg.conf(5) § INPUTCLASS SECTION](<https://man.archlinux.org/man/xorg.conf.5#INPUTCLASS_SECTION>) 中的一个过滤器，例如： 

  * `MatchIsPointer "on"` (trackpoint)
  * `MatchIsKeyboard "on"`
  * `MatchIsTouchpad "on"`
  * `MatchIsTouchscreen "on"`

输入设备能够在 CONFIGURATION 中进行配置，详情请看 [libinput(4) § CONFIGURATION](<https://man.archlinux.org/man/libinput.4#CONFIGURATION>)。一些常用的配置选项有： 

  * `Option "Tapping" "on"`: 触摸以点击
  * `Option "ClickMethod" "clickfinger"`: 触摸板不再拥有中右键区域的区分，与之代替的是双指代表右键，三指代表中键。 详情请看[docs](<https://wayland.freedesktop.org/libinput/doc/latest/clickpad-softbuttons.html#clickfinger-behavior>).
  * `Option "NaturalScrolling" "true"`: 自然滚动（反方向滚动）
  * `Option "ScrollMethod" "edge"`: 边缘滚动页面

注意：有的功能只在特定设备中起作用，并且你可能需要重启 “X服务” 来让功能生效。 

###  使用 udev 规则

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** 这不像是通用的配置方法，实际上通过这种方式可以设置的不仅仅是 `LIBINPUT_CALIBRATION_MATRIX`。（在[Talk:Libinput](<../zh-cn/Talk:Libinput.html>)讨论）

[udev](<../zh-cn/Udev.html> "Udev") 和 [Calibrating Touchscreen](<https://wiki.archlinux.org/title/Calibrating_Touchscreen> "en:Calibrating Touchscreen") 给出了更详细的信息，简要总结如下： 
    
    # libinput list-devices
    
该命令打印输入设备的设备名称（Device）和内核路径（Kernel）。例如，内核路径`/dev/input/event0` 的设备 `HID 02eb:114e`。 

下面为该设备创建了一个规则，将所有触摸屏输入旋转 270 度： 
    
    /etc/udev/rules.d/99-mytouchscreen-calibration.rules
    
    # 将输入旋转 270 度
    ENV{ID_USB_SERIAL}=="02eb_114e", ENV{LIBINPUT_CALIBRATION_MATRIX}="0 1 0 -1 0 1"

**提示：** 参考 [Libinput 文档](<https://wayland.freedesktop.org/libinput/doc/latest/device-configuration-via-udev.html>) 中的 _Static Device Configuration Via Udev_ 部分，以了解其他坐标变换方法。

然后，[重新加载规则](<../zh-cn/Udev.html#%E5%8A%A0%E8%BD%BD%E6%96%B0%E8%A7%84%E5%88%99> "Udev")并查看设备是否已经成功注册该规则： 
    
    # udevadm info /dev/input/event0
    
你应该能看到该设备的 `LIBINPUT_CALIBRATION_MATRIX` 已被列出。 

最后，重启你的机器或 Wayland 桌面。 

###  图形工具

下面列出了一些图形工具： 

  * [GNOME](<../zh-cn/GNOME.html> "GNOME"): 
    * 控制中心（Control center）带有一个基础配置页面，详见 [GNOME#Mouse and touchpad](<../zh-cn/GNOME.html#Mouse_and_touchpad> "GNOME").
    * [gnome-tweaks](<https://archlinux.org/packages/?name=gnome-tweaks>)包 提供一些其他设置。
  * [Cinnamon](<../zh-cn/Cinnamon.html> "Cinnamon"): 
    * 与 GNOME 界面相似，可更改选项更多。
  * [KDE Plasma](<../zh-cn/KDE_Plasma.html> "KDE Plasma") 5: 
    * 键盘，鼠标和控制器可以通过系统设置（System Settings）配置。
  * [Xfce](<../zh-cn/Xfce.html> "Xfce")
    * 在 [xfce4-settings](<https://archlinux.org/packages/?name=xfce4-settings>)包 下的“鼠标和触摸板（Mouse and Touchpad）”子菜单中进行配置。

  * [MATE](<../zh-cn/MATE.html> "MATE"): 
    * 你可以在 MATE 的控制面板中配置鼠标相关内容，也可以使用 `mate-mouse-properties`

##  使用技巧

###  交换多指点击动作

本小节以交换触摸板的两指点击与三指点击动作为例进行说明。 

为了使用两指点击来替代三指点击的动作，需要修改 [Xorg](<../zh-cn/Xorg.html> "Xorg") 配置文件中 `TappingButtonMap` 选项。如果希望将单指、两指、三指点击对应的动作分别对应为左键、右键、中键（left/right/middle）点击，将 `TappingButtonMap` 设置为 `lrm` 即可。若想调换两指、三指点击对应动作，将该选项配置为 `lmr` （即单指、两指、三指点击分别对应左键、中键、右键点击）即可。 
    
    /etc/X11/xorg.conf.d/30-touchpad.conf
    
    Section "InputClass"
        Identifier "touchpad"
        Driver "libinput"
        MatchIsTouchpad "on"
        Option "Tapping" "on"
        Option "TappingButtonMap" "lmr"
    EndSection

如果你的设备不是触控板，请记得移除 `MatchIsTouchpad "on"` 选项，并对应修改 `Identifier` 选项。 

###  设置按键映射

设置按键映射可以实现使用鼠标侧键替换鼠标中键（鼠标中键在 X11 中可以用于粘贴内容，一般为按压鼠标滚轮的对应按键）等功能。 

可以通过如下命令查看按键映射情况： 
    
    $ xinput get-button-map _device_
    
其中 _device_ 可以是 `xinput list` 命令返回的设备名或者设备ID。你可以随意交换按钮对应的数字并写回。例如： 
    
    $ xinput set-button-map _device_ 1 6 3 4 5 0 7
    
在上面的例子中，我们将编号为6的按钮设置为了中键，并为原本的中键配置了按键0以禁用该按键。 关于按键映射的内容可以参阅[libinput(4)](<https://man.archlinux.org/man/libinput.4>)的“ButtonMapping”部分。 也许在 [Wayland](<../zh-cn/Wayland.html> "Wayland") 中这种修改方式同样适用，但是需要注意的是， _device_ 的编号与 button-map 也许互不相通。因此在 Xorg 与 Wayland 的设置并不能直接交换。 

**提示：** 你可以使用命令 `xev`（包含于软件包 [xorg-xev](<https://archlinux.org/packages/?name=xorg-xev>)包）来查看物理按键对应的逻辑按键编号。

在列出设备时，某些设备可能会以相同的设备名被多次列出，但是他们往往对应着不同的按键映射，因此准确修改按键映射需要辨别真正需要修改按键映射的设备。下面是一个通过 [xinitrc](<../zh-cn/Xinit.html#xinitrc> "Xinitrc") 来对某款鼠标（Logitech Revolution MX）进行配置的示例。 
    
    ~/.xinitrc
    
    ...
    for i in $(xinput list | grep "Logitech USB Receiver" | perl -n -e'/id=(\d+)/ && print "$1\n"')
    	do if xinput get-button-map "$i" 2>/dev/null| grep -q 20; then
    		xinput set-button-map "$i" 1 17 3 4 5 8 7 6 9 10 11 12 13 14 15 16 2 18 19 20
    	fi
    done
    ...

你也可以用 Xorg 配置文件实现。本例中使用的[轨迹球](<https://zh.wikipedia.org/wiki/%E8%BD%A8%E8%BF%B9%E7%90%83> "wiki-zh:轨迹球")（**Trackball** ）带有一个物理滚轮，没有滚轮的设备可能需要参考 **[Logitech Marble Mouse](<https://wiki.archlinux.org/title/Logitech_Marble_Mouse#X11> "en:Logitech Marble Mouse")** 的配置。Kensington Slimblade 轨迹球的物理按键布局如下： 
    
    -----------
    |2(M)|8(S)|
    -----------
    |1(L)|3(R)|
    -----------
    
因此，对于左手用户，可以使用下面的配置。虽然该设备没有“向上滚动”和“向下滚动”按钮，但你不能在配置中禁用它们，否则某些应用程序将无法响应滚轮操作。 
    
    -----------
    |2(N)|8(M)|
    -----------
    |1(R)|3(L)|
    -----------
    
    /etc/X11/xorg.conf
    
    Section "InputClass"
         Identifier   "Trackball"
         MatchProduct "Kensington Kensington Slimblade Trackball"
         MatchProduct "Trackball"
         Driver       "libinput"
         Option       "ButtonMapping"      "3 0 1 4 5 6 7 8 2"
     EndSection

###  更改触摸板灵敏度

寻找触摸板适合的灵敏度阈值的方法可以参考上游文档[[2]](<https://wayland.freedesktop.org/libinput/doc/latest/touchpad-pressure-debugging.html#touchpad-pressure-hwdb>)

自定义触摸板的按压灵敏度可以通过“temporary local device quirks”实现，参见 device-quirks 文档[[3]](<https://wayland.freedesktop.org/libinput/doc/latest/device-quirks.html>)。 

**注意：**

Quirks 是一组内部API（internal API），并不保证能够在未来版本的 libinput 中正常工作。 在libinput 1.11 到 1.12 版本中，udev规则[[4]](<https://wayland.freedesktop.org/libinput/doc/1.11.3/udev_config.html#hwdb>) 被 `.quirk`文件[[5]](<https://wayland.freedesktop.org/libinput/doc/latest/device-quirks.html>)取代。 

###  禁用触摸板

禁用触摸板需要先使用命令 `xinput list` 获取触摸板名称，之后使用命令 `xinput disable _name_` 来禁用。 

**注意：**

  * 使用设备ID来禁用设备是一种相对较为鲁莽的行为，因为设备ID可能被重新分配。
  * 当设备名中包含空格时，需要使用英文引号将其包含在内。

如果希望其在系统启动时生效，参见[自动启动](<../zh-cn/%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8.html> "Autostarting")相关内容。 

可以编写相应脚本来启用/禁用触摸板[[6]](<https://github.com/lahwaacz/Scripts/blob/master/toggle-touchpad.sh>)。 

###  手势操作

虽然 libinput 已经提供了[手势操作](<https://wayland.freedesktop.org/libinput/doc/latest/gestures.html>)，比如：捏、滑。但部分[桌面环境（DE）](<../zh-cn/Desktop_environment.html> "Desktop environment")和[窗口管理器（WM）](<../zh-cn/Window_manager.html> "Window manager")可能还没有支持这些功能。 

#### libinput-gestures

对于兼容 [EWMH](<https://en.wikipedia.org/wiki/Extended_Window_Manager_Hints> "w:Extended Window Manager Hints")（另见 [wm-spec](<https://www.freedesktop.org/wiki/Specifications/wm-spec/>)）的窗口管理器（WM）, 可以使用 [libinput-gestures](<https://github.com/bulletmark/libinput-gestures>) 。 程序从 libinput 获取触摸板的手势 (通过 `libinput debug-events`) ，然后根据相关配置将其映射成相对应的行为。这个程序提供了相当多了可自定义的功能。 

要使用 [libinput-gestures](<https://github.com/bulletmark/libinput-gestures>), 请安装 [libinput-gestures](<https://aur.archlinux.org/packages/libinput-gestures/>)AUR 。 你能使用很多系统级别的手势操作，也能自定义配置文件，详情请看 [README](<https://github.com/bulletmark/libinput-gestures/blob/master/README.md>) 。 

#### fusuma

[Fusuma](<https://github.com/iberianpig/fusuma>) 是一个使用 [Ruby](<../zh-cn/Ruby.html> "Ruby") 编写的多点手势识别器（multitouch gesture recognizer），可以作为 libinput-gestures 的替代品。 

使用 [Ruby gem](<../zh-cn/Ruby.html#RubyGems> "Ruby") 安装 `fusuma`： 
    
    $ gem install fusuma
    
或者可以从 AUR 安装：[ruby-fusuma](<https://aur.archlinux.org/packages/ruby-fusuma/>)AUR。 

除了 `fusuma` 模块，还需要安装Ruby模块 `fusuma-plugin-sendkey` 或者从 [xdotool](<https://archlinux.org/packages/?name=xdotool>)包（用于X）与 [ydotool](<https://archlinux.org/packages/?name=ydotool>)包 中任选其一。其他可选择的工具可以参见[项目说明](<https://github.com/iberianpig/fusuma#alternatives-to-xdotool>)

**提示：** `fusuma-plugin-sendkey` 模块同时支持 X 和 Wayland.

fusuma 安装完成后可以在配置文件 `~/.config/fusuma/config.yml` 进行配置。例如： 
    
    ~/.config/fusuma/config.yml
    
    swipe:
      3: 
        left: 
          sendkey: 'LEFTALT+RIGHT'
        right: 
          sendkey: 'LEFTALT+LEFT'
        up: 
          sendkey: 'LEFTALT+LEFTSHIFT+TAB'
        down: 
          sendkey: 'LEFTALT+TAB'
    pinch:
      in:
        sendkey: 'LEFTALT+LEFTSHIFT+TAB'
      out:
        sendkey: 'LEFTALT+TAB'
    
    threshold:
      swipe: 0.5
      pinch: 0.2
    
    interval:
      swipe: 0.2
      pinch: 0.2
    
适用于 `xdotool` 的配置： 
    
    ~/.config/fusuma/config.yml
    
    swipe:
      3: 
        left: 
          command: 'xdotool key alt+Right'
        right: 
          command: 'xdotool key alt+Left'
        up: 
          command: 'xdotool key ctrl+shift+plus'
        down: 
          command: 'xdotool key ctrl+minus'
    pinch:
      in:
        command: 'xdotool key ctrl+shift+plus'
      out:
        command: 'xdotool key ctrl+minus'
    
    threshold:
      swipe: 0.5
      pinch: 0.2
    
    interval:
      swipe: 0.2
      pinch: 0.2
    
`ydotool` 适用的配置同上。 

适当配置滑动阈值（swip threshold）可以避免在滚动时划过过多页面。 

需要注意的是该配置仅适用于三指滑动，并不适用于两指滑动[[7]](<https://github.com/iberianpig/fusuma/issues/104#issuecomment-434742767>)

#### Gebaar

[Gebaar](<https://github.com/Coffee2CodeNL/gebaar-libinput>) 是另一个手势识别器（gesture recognizer）。与 Fusuma 相比，gebaar 不支持“捏”的手势（该手势支持已经被加入开发计划中）和阈值配置，但是增加了四指、五指滑动手势与斜线滑动。 

gebaar的[一份fork](<https://github.com/Osleg/gebaar-libinput>)可以使用AUR安装：[gebaar-libinput-git](<https://aur.archlinux.org/packages/gebaar-libinput-git/>)AUR，这一版本的gebaar适配了“捏”的手势以及一些其他功能。该版本当前正处于积极开发的状态，但是配置文件与[gebaar原始版本](<https://github.com/Coffee2CodeNL/gebaar-libinput>)不兼容。 

#### GnomeExtendedGestures

对于 GNOME 环境，可以尝试 [GnomeExtendedGestures](<https://github.com/mpiannucci/GnomeExtendedGestures>)（[gnome-shell-extension-extended-gestures-git](<https://aur.archlinux.org/packages/gnome-shell-extension-extended-gestures-git/>)AUR）。 使用该工具可以将三指水平和垂直滑动对应动作配置为相关 gnome-shell actions（例如切换应用视图或在应用间切换）。 

###  使用鼠标按键实现滚动

通过配置，在按住某个鼠标按键（例如左键或者右键，或者鼠标上的其他按键）的同时移动鼠标，可以实现滚动页面的动作，这对于轨迹球之类没有滚轮的设备十分有帮助。只需要将 `ScrollMethod` 配置为 `button`，并通过 `ScrollButton` 选项配置对应的按键即可。可以参考下面的例子： 
    
    /etc/X11/xorg.conf.d/00-mouse.conf
    
    Section "InputClass"
        Identifier "system-mouse"
        MatchIsPointer "on"
        Option "ScrollMethod" "button"
        Option "ScrollButton" "3"
    EndSection
    
###  调节滚轮滚动速度

对某些鼠标，尤其是使用 [HiDPI](<../zh-cn/HiDPI.html> "HiDPI") 的设备，使用鼠标滚轮时可能会感觉滚动速度较慢。 [相关补丁](<https://gitlab.freedesktop.org/xorg/driver/xf86-input-libinput/-/merge_requests/12>)还没有合并进libinput项目中。另一个第三方 [xf86-input-libinput](<https://github.com/archlinuxcn/repo/tree/d0eb728b38450b47a4913539193a58fb523cc255/archlinuxcn/xf86-input-libinput-oldherl>) 使用了这个补丁。 

这个补丁为鼠标提供了一个新属性 `libinput Scroll Distance Scale`，而且你可以通过如下方法配置滚动缩放（set a scaling factor）： 
    
    $ xinput --set-prop 'RAPOO Rapoo 2.4G Wireless Device' 'libinput Scroll Distance Scale' 2.5 2.5
    
上述命令中，`RAPOO Rapoo 2.4G Wireless Device` 是你的鼠标在 `xinput --list` 输出中展示的设备名，`2.5 2.5` 是缩放比例，分别对应 x 和 y 方向。 

或者你可以选择安装 [libinput-multiplier](<https://aur.archlinux.org/packages/libinput-multiplier/>)AUR 并重启 [Xorg](<../zh-cn/Xorg.html> "Xorg")，之后将y轴滚动距离配置为6倍： 
    
    $ echo 6 > /tmp/libinput_discrete_deltay_multiplier
    
[这个示例](<https://github.com/tkkcc/libinput_patch#change-with-focused-window>)展示了如何在焦点发生变化时调整滚动缩放。 

###  打字时启用触摸板

默认情况下，`libinput` 在打字时会禁用触摸板。这会与某些软件产生冲突，例如 **[Inkscape](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E5%A4%9A%E5%AA%92%E4%BD%93.html#%E7%9F%A2%E9%87%8F%E5%9B%BE%E5%BD%A2%E7%BC%96%E8%BE%91%E5%99%A8> "应用程序列表/多媒体")** ，该软件具有需要在按下按键的同时移动鼠标的快捷键。一种在打字时启用触摸板的方法是将下面几行添加到 `/etc/X11/xorg.conf.d/30-touchpad.conf` 的 `InputClass` 部分： 
    
    Section "InputClass"
        ...
        Option "DisableWhileTyping" "0"
    EndSection
    
也可以使用 **[xinput](<https://wiki.archlinux.org/title/Xinput> "en:Xinput")** 达到同样的效果。属性名称可能类似于 `libinput Disable While Typing Enabled`。 

##  疑难解答

当遇到libinput相关问题时，可以尝试使用 `libinput debug-events` 来帮助你进行调试，相关内容请参考 [libinput-debug-events(1)](<https://man.archlinux.org/man/libinput-debug-events.1>)。 

一些输入事件需要内核支持，查看支持的输入事件可以安装软件包 [evemu](<https://archlinux.org/packages/?name=evemu>)包，使用工具 `evemu-describe` 进行确认。 

###  触摸板在 GNOME 中无法工作

首先需要确认触摸板的事件被正确的发送给了 GNOME 处理，可以执行下面的命令： 
    
    $ gsettings set org.gnome.desktop.peripherals.touchpad send-events enabled
    
此外，GNOME 可能会重载部分行为，例如关闭轻触点击和强制使用自然滚动（Natural Scrolling）。 如果希望进行修改，必须使用 GNOME 的设置命令 `gsettings` 或者你选择的图形前端进行配置。 例如，如果希望为当前用户开启轻触点击（Tapping）以及关闭自然滚动（Natural Scrolling），按照下面的命令修改触摸板的相关配置： 
    
    $ gsettings set org.gnome.desktop.peripherals.touchpad tap-to-click true
    $ gsettings set org.gnome.desktop.peripherals.touchpad natural-scroll false
    
###  惯性滚动在 KDE 中无法工作

该功能尚未实现，参见 [KDE bug 456383](<https://bugs.kde.org/show_bug.cgi?id=456383>)。对于基于 Chromium 的浏览器，可以安装 **[SmoothScroll](<https://chromewebstore.google.com/detail/smoothscroll/nbokbjkabcmbfdlbddjidfmibcpneigj?pli=1>)** 扩展作为临时解决方案**。**

###  进入平板电脑模式后按键卡住

在某些平板电脑（尤其是 Lenovo Yoga 系列）上，进入平板电脑模式时按住键盘按键可能会导致该键一直处于触发状态，直到禁用平板电脑模式。有时可以通过修改 libinput 的 quirks 文件来修复此行为。参见 **[Issue 914](<https://gitlab.freedesktop.org/libinput/libinput/-/issues/914>)** 。 

例如，先找到键盘设备的名称： 
    
    # libinput list-devices
    
    ...
    Device:           AT Translated Set 2 keyboard
    Kernel:           /dev/input/event3
    Capabilities:     keyboard
    ...

然后，创建一个覆盖文件： 
    
    /etc/libinput/local-overrides.quirks
    
    [Lenovo Thinkpad Yoga]
    MatchName=AT Translated Set 2 keyboard
    ModelTabletModeNoSuspend=0

`ModelTabletModeNoSuspend=0`会禁用导致该 bug 的行为。有关配置格式和用于选择待配置设备的 Match 指令，请参考 **[Device quirks](<https://wayland.freedesktop.org/libinput/doc/latest/device-quirks.html>)** 。通常可以根据针对您特定设备的现有 quirks 条目来创建覆盖文件。默认的 quirks 文件可以在 `/usr/share/libinput/` 中找到。 

##  参阅

  * [libinput Wayland documentation](<https://wayland.freedesktop.org/libinput/doc/latest/index.html>)
  * [FOSDEM 2015 - libinput](<https://archive.fosdem.org/2015/schedule/event/libinput/attachments/slides/591/export/events/attachments/libinput/slides/591/libinput_xorg.pdf>) \- Hans de Goede on goals and plans of the project
  * [Peter Hutterer's Blog](<https://who-t.blogspot.com.au/>) \- numerous posts on libinput from one of the project's hackers
  * [Talk by the primary libinput maintainer](<https://www.youtube.com/watch?v=HllUoT_WE7Y>) outlining the history and state (as of 2020) of Linux input device handling
  * [Blog post by the libinput maintainer](<https://who-t.blogspot.com/2018/07/why-its-not-good-idea-to-handle-evdev.html>) outlining the rationale for libinput
