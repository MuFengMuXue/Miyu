**翻译状态：**

  * 本文（或部分内容）译自 [Dwm](<https://wiki.archlinux.org/title/Dwm> "arch:Dwm")，最近一次同步于 2022-06-03，若英文版本有所[更改](<https://wiki.archlinux.org/title/Dwm?diff=0&oldid=731422>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Dwm_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [dmenu](<../zh-cn/Dmenu.html> "Dmenu")

[dwm](<https://dwm.suckless.org/>)是[X](<../zh-cn/Xorg.html> "X")下的一个动态窗口管理器。它用平铺的、栈式的和全屏的布局方式，借助一些可选的补丁还可以实现其他的布局。布局可以动态得改变，为程序提供最优的环境和性能。dwm特别轻量快速，用C语言编写，被设计的目标是控制在2000行以下的代码。在xrandr和Xinerama支持下可实现multi-head。 

##  安装

dwm可以通过[dwm](<https://aur.archlinux.org/packages/dwm/>)AUR或[dwm-git](<https://aur.archlinux.org/packages/dwm-git/>)AUR安装，可在编译安装前配置所需的更改，参阅[makepkg](<../zh-cn/Makepkg.html> "Makepkg")。 

**注意：** 也可遵循[上游说明](<https://git.suckless.org/dwm/file/README.html>)，但[pacman](<../zh-cn/Pacman.html> "Pacman")将无法对其进行跟踪。

###  配置

dwm通过在编译时修改它的配置文件的一部分源代码来进行配置，特别是`config.h`。有关这些配置的详细信息，请参阅包含的、注释良好的` config.def.h`以及网站上的[自定义部分](<https://dwm.suckless.org/customisation/>)。 

官方网站上有一些[补丁](<https://dwm.suckless.org/patches/>)可以为dwm添加额外功能。这些补丁主要对` dwm.c`文件进行更改，但也会在适当的情况下对` config.h`文件进行更改。有关应用修补程序的信息，请参阅[Patching packages](<../zh-cn/Patching_packages.html> "Patching packages")一文。 

##  启动dwm

从所选[display manager](<../zh-cn/Display_manager.html> "Display manager")的菜单中选择“Dwm”。或者，用[startx](<../zh-cn/Xinit.html> "Startx")将` exec dwm`附加到` ~/.xinitrc`并预先编写其他程序来执行它们，例如： 
    
    redshift -O3500; xset r rate 300 50; exec dwm
    
##  配置状态条

dwm使用根窗口名称来显示状态条信息，可以使用`xsetroot -name`来改变。 

###  基本状态条

这个例子显示[ISO 8601](<https://en.wikipedia.org/wiki/ISO_8601> "wikipedia:ISO 8601")格式的日期。把下边的内容添加到`~/.xinitrc`或者`~/.Xclients`，或者可以从GDM-3的讨论页中获得更多细节： 
    
    while true; do
       xsetroot -name "$( date +"%F %R" )"
       sleep 1m    # Update time every minute
    done &
    exec dwm
    
这是个笔记本使用的，依赖[acpi](<https://archlinux.org/packages/?name=acpi>)包包来显示电池信息： 
    
    while true ; do
        xsetroot -name "$( acpi -b | awk '{ print $3, $4 }' | tr -d ',' )"
        sleep 1m
    done &
    exec dwm
    
这个脚本显示电池剩余电量和充电状态，用awk命令过滤acpi输出的无用信息，然后用tr去除逗号。 

另一个方式是根据电池的状态选择性地输出信息： 
    
    while true; do
            batt=$(LC_ALL=C acpi -b)
    
            case $batt in
            *Discharging*)
                    batt="${batt#* * * }"
                    batt="${batt%%, *} "
                    ;;
            *)
                    batt=""
                    ;;
            esac
    
            xsetroot -name "$batt$(date +%R)"
    
            sleep 60
    done &
    
    exec dwm

最后，要确保在`~/.xinitrc`或者`~/.Xclients`里只有一个dwm实例, 所以把整合起来应该像这样： 
    
    ~/.setbg
    autocutsel &
    termirssi &
    urxvt &
    
    while true; do
       xsetroot -name "$(date +"%F %R")"
       sleep 1m    # Update time every minute
    done &
    **exec dwm**
    
这是另一个显示alsa音量和电池状态的例子。它一直显示到系统退出为止。 
    
    #set statusbar
    while true
    do
       if acpi -a | grep off-line > /dev/null; then
           xsetroot -name "Bat. $( acpi -b | awk '{ print $4 " " $5 }' | tr -d ',' ) | Vol. $(amixer get Master | tail -1 | awk '{ print $5}' | tr -d '[]') | $(date +"%a, %b %d %R")"
       else
           xsetroot -name "Vol. $(amixer get Master | tail -1 | awk '{ print $5}' | tr -d '[]') | $(date +"%a, %b %d %R")"
       fi
       sleep 1s   
    done &
    
###  Conky状态条

Conky可以使用`xsetroot -name`来往状态条里输出信息: 
    
    conky | while read -r; do xsetroot -name "$REPLY"; done &
    exec dwm
    
要想这样做，conky需要只往终端里输出文本。这是个应用于dual core CPU的简单conkyrc，显示几个状态信息： 
    
    out_to_console yes
    out_to_x no
    background no
    update_interval 2
    total_run_times 0
    use_spacer none
    
    TEXT
    $mpd_smart :: ${cpu cpu1}% / ${cpu cpu2}%  ${loadavg 1} ${loadavg 2 3} :: ${acpitemp}c :: $memperc% ($mem) :: ${downspeed eth0}K/s ${upspeed eth0}K/s :: ${time %a %b %d %I:%M%P}
    
###  状态条颜色

可以在`config.def.h`中更改，然后复制到`config.h`中。 
    
    static const char col_gray1[]       = "#000000"; #状态条底色
    static const char col_gray2[]       = "#FFFFFF"; #当static const unsigned int borderpx不为0时，非活动窗口外边框颜色
    static const char col_gray3[]       = "#39C5BB"; #当前非活动的title字体颜色
    static const char col_gray4[]       = "#7FFF00"; #当前活动的title字体颜色
    static const char col_cyan[]        = "#696969"; #title底色

static const unsigned int borderpx也是`config.def.h`的选项，不为0时，会在窗口边缘产生边框 

##  基本用法

###  使用dmenu

Dmenu是dwm的一个有用的扩展。它不是一个单独的列表式菜单，而是生成一个可执行文件的列表并根据输入进行自动补全。比起许多程序启动器，它能与dwm更好地整合。 

可以按 `Mod1` \+ `P` 来启动Dmenu（`Mod1` 缺省是 `Alt` ）。当然你也可以按自己的喜好改变它。然后只需要在上边出现的工具条中输入你想运行的程序的前几个字母，也可以按左右箭头在进行选择，按回车键完成。 

更详细的信息请查阅 [dmenu](<../zh-cn/Dmenu.html> "Dmenu"). 

###  控制窗口

####  将窗口移动到另一个tag

将当前的活动窗口移到其他的标签页：`Shift` \+ `Mod1` \+ `x`, 其中的x是其他的标签页的序号，如果x是5，则表示将当前的活动窗口移到第5号标签页上去。`Mod1` 缺省是 `Alt` 键，这个键值可以在config.h中定义。 

####  关闭窗口

关闭当前的活动窗口： `Shift` \+ `Mod1` \+ `C`. 

####  窗口布局

dwm缺省工作在平铺模式。当新窗口不断出现在同一个标签页时，窗口会越来越小。所有窗口会占满整个屏幕（除了目录条）。然而还有其他两种模式：浮动和单页模式。浮动模式对非平铺窗口管理器用户来说更熟悉，它允许用户重新按自己需要摆放窗口。单页模式会让一个窗口在最上边。 

要切换到浮动模式，只需要按`Mod1` \+ `F`。`Mod1`缺省是 `Alt`。如果你看到标签页右上角有X>这样的标志，就进行了浮动模式。 

切换到单页模式，按 `Mod1` \+ `M`。检查上否在单页模式，你会看到[M]标志（如果当前标签页无窗口），或者[n]（n是打开窗口的编号）。 

回来平铺模式，按`Mod1` \+ `T`，你会看到 []= 这样的标志。 

###  退出dwm

退出dwm（登出）： `Shift` \+ `Mod1` \+ `Q`. 

官方关于默认的快捷键的说明: [dwm tutorial](<https://dwm.suckless.org/tutorial>). 

再次说明，快捷键可以根据自己的喜好自由定义，本维基中的快捷键都是指官方默认的快捷键。 

##  扩展使用

###  补丁和增加窗口布局（tiling modes）

DWM官网上有很多可以给DWM添加功能的[补丁](<https://dwm.suckless.org/patches/>)， 用户可以通过补丁定制DWM。 

[bottomstack](<https://dwm.suckless.org/patches/bottomstack>)补丁能够使DWM由原来的垂直布局变为水平布局，而[gapless grid](<https://dwm.suckless.org/patches/gaplessgrid/>)补丁则可使窗口变为网格状布局. 

####  实现为每个标签定制布局

dwm的缺省行为是将当前选定的布局应用到所有标签上。如果想为每个标签定制布局可以打[pertag](<https://dwm.suckless.org/patches/pertag>)这个补丁。 

###  解决模拟终端窗口缝隙问题

如果你发现模拟终端（例如xterm，Urxvt）的窗口占不满屏幕，这是因为其窗口的大小和字体有关。你可以试图调整字体大小直到恰好合适为止（这也许是很困难的），或者只需要把`config.h` 文件中的 `resizehints` 设置为 False： 
    
    static Bool resizehints = False; /* False means respect size hints in tiled resizals */
    
这样dwm会忽略所有窗口的改变大小的请求，不只是模拟终端的。这样的缺点是一些模拟终端可能会刷新异常，像显示一些错误的内容。 

###  在不登出和退出程序程序的情况下重启dwm

如果你要在在线重启dwm（不关闭它以及其他应用程序），修改启动脚本，并让dwm在一个while循环中运行，像这样： 
    
    while true; do
        # Log stderror to a file 
        dwm 2> ~/.dwm.log
        # No error logging
        #dwm >/dev/null 2>&1
    done
    
这样就可以用Mod-Shift-Q快捷键来实现重启。 

把上边的内容写到一个其他的文件（例如`~/bin/startdwm`）是一个好主意。然后在 `~/.xinitrc` 文件里添加（exec startdwm）。这样我们可以使用 `killall startdwm` 来真正地退出X会话，或者绑定到一个方便的快捷键上。 

###  把右Alt键作为Mod4（Win键）使用

当把Mod4（Win键）作为 `MODKEY` 时，你可能希望右Alt键也可以作为Mod4，这样就两个手都可以按到了 

首先，找到右Alt键对应的键码： 
    
    xmodmap -pke | grep Alt_R
    
然后只需要在启动脚本（比如 `~/.xinitrc`）添加如下内容, 把 _113_ 换成之前`xmodmap` 的结果： 
    
    xmodmap -e "keycode 113 = Super_L"  # reassign Alt_R to Super_L
    xmodmap -e "remove mod1 = Super_L"  # make sure X keeps it out of the mod1 group
    
现在，右Alt键就和Mod4键一样了。 

###  防止鼠标下的程序自动获取焦点

为了防止鼠标下的程序自动获取焦点，可以注释掉dwm.c中的如下代码： 
    
    [EnterNotify] = enternotify,

###  添加自定义的快捷键绑定

`config.h` 文件中的两个地方涉及到创建修改快捷键，一个是"/* */" 注释中，并一个是"static Key keys[] = {"语句中。 
    
    static const char *<keybindname>[]   = { "<command>", "<flags>", "<arguments>", NULL };
    
<keybindname> 可以是任何东西， <command> <-flags> and <arguments> 也是，但要用双引号括起来。 
    
    { MODKEY,            XK_<key>,      spawn,          {.v = <keybindname> } },
    
这会绑定 Mod+<key> 来执行之前定义的命令。 
    
    { MODKEY|ShiftMask,  XK_<key>,      spawn,          {.v = <keybindname> } },
    
这会绑定 Mod+Shift+<key> ，使用要用Ctrl键是 ControlMask 。 

单个按键像Fn或者多媒体键必须要用16进制数来表示，可以用xev程序来获得。或者查看 /usr/include/X11/XF86keysym.h 中的定义。 
    
    { 0,                 0xff00,    spawn,       {.v = <keybindname> } },
    
这会把0xff00键绑定到<keybindname>。 

###  解决Java程序不正常的问题

对于使用JRE 6u20的Java程序在dwm中可能表现异常，因为dwm不是Java的一个已知的窗口管理器，这会导致一些像鼠标释放使菜单消失之类的小问题。可以先安装里的 [community] 里的wmname： 
    
    # pacman -S wmname
    
然后你只需要用wmname来设置一个Java能识别的WM名称： 
    
    $ wmname LG3D
    
这不是永久的，所以你可以把它写进.xinitrc。 

##  资源

  * [dwm's official website](<https://dwm.suckless.org>)
  * [dmenu](<../zh-cn/Dmenu.html> "Dmenu") \- Simple application launcher from the developers of dwm
  * The [dwm thread](<https://bbs.archlinux.org/viewtopic.php?id=57549/>) on the forums
  * [Hacking dwm thread](<https://bbs.archlinux.org/viewtopic.php?id=92895/>)
  * Check out the forums' [wallpaper thread](<https://bbs.archlinux.org/viewtopic.php?id=57768/>) for a selection of dwm wallpapers
  * [HowTo by Snake](<https://web.archive.org/web/20110324200939/http://www.xsnake.net/howto/dwm/dwm-eng.php>)
  * [Moved to dwm](<https://web.archive.org/web/20130529231215/http://0x80.org/blog/moved-to-dwm/>)
