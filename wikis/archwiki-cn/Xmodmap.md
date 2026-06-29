**翻译状态：**

  * 本文（或部分内容）译自 [Xmodmap](<https://wiki.archlinux.org/title/Xmodmap> "arch:Xmodmap")，最近一次同步于 2021-4-15，若英文版本有所[更改](<https://wiki.archlinux.org/title/Xmodmap?diff=0&oldid=647793>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Xmodmap_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Xorg](<../zh-cn/Xorg.html> "Xorg")
  * [Keyboard input](</wzh/index.php?title=Keyboard_input&action=edit&redlink=1> "Keyboard input（页面不存在）")
  * [Extra keyboard keys in console](</wzh/index.php?title=Extra_keyboard_keys_in_console&action=edit&redlink=1> "Extra keyboard keys in console（页面不存在）")
  * [Xbindkeys](</wzh/index.php?title=Xbindkeys&action=edit&redlink=1> "Xbindkeys（页面不存在）")

_xmodmap_ 是一个用于修改 [Xorg](<../zh-cn/Xorg.html> "Xorg") 中键位图和指针按钮映射的工具。 

_xmodmap_ 与 [X keyboard extension](<../zh-cn/X_keyboard_extension.html> "X keyboard extension") (XKB)没有直接关系。这两个程序对于X中的如何处理"键码"的理解是不一样的（xmodmap 更早）。一般来说，它只被推荐用于最简单的任务。请参阅 [X keyboard extension](<../zh-cn/X_keyboard_extension.html> "X keyboard extension") 了解高级布局配置。 

**注意：**

  * _xmodmap_ 设置会被 _setxkbmap_ 重置，它不仅将字母数字键改变为映射表中的值，还将所有其他键重置为启动时的默认值。[[1]](<https://wiki.linuxquestions.org/wiki/Configuring_keyboards>)
  * 由于Xorg的限制， _xmodmap_ 设置不会自动应用到热插拔设备上。如果在应用了自定义映射表后，系统中添加了一个新的键盘，则必须重新应用自定义映射表。[[2]](<https://bugs.freedesktop.org/show_bug.cgi?id=25262>)

##  简介

在 [Xorg](<../zh-cn/Xorg.html> "Xorg") 中有两种类型的键盘值：键码和键符。 

键码 keycode
    键码是当按键或鼠标按钮被按下时，内核收到的表示数字。
键符 keysym
    键符是键码所对应的符号表达值。例如，按`a`产生`38`号键码，它被映射到`0×61`号键符，对应 [ASCII表](<https://en.wikipedia.org/wiki/ASCII> "wikipedia:ASCII")中的 `a`。
    在[Xorg](<../zh-cn/Xorg.html> "Xorg")中，键符通过一个定义键码-键符对应关系的表管理。这个表叫做[键映射表](<#%E9%94%AE%E6%98%A0%E5%B0%84%E8%A1%A8>)。可以通过运行`xmodmap`来显示。

##  安装

_xmodmap_ 由 [xorg-xmodmap](<https://archlinux.org/packages/?name=xorg-xmodmap>)包 包提供。 

也可以安装 [xkeycaps](<https://archlinux.org/packages/?name=xkeycaps>)包，这是一个 _xmodmap_ 的图形前端。 

##  键映射表

打印以表达式格式呈现的键映射表： 
    
    $ xmodmap -pke
    
    [...]
    keycode  57 = n N
    [...]

每个键码后面都跟着映射到的键符。上面的例子意思是：键码`57`被映射到小写`n`键符，而大写`N`键符则对应按下`Shift`输入的`57`号键码。 

表中的每一列键符都对应着一个特定的修饰键组合，Key为键码所对应的按键： 

  1. `Key`
  2. `Shift+Key`
  3. `Mode_switch+Key`
  4. `Mode_switch+Shift+Key`
  5. `ISO_Level3_Shift+Key`
  6. `ISO_Level3_Shift+Shift+Key`

并非所有的键符都必须设置，但如果要跳过一个键符，请将其值设为`NoSymbol`。 

要查看一个键对应的键码，请参见[Keyboard input#Identifying keycodes in Xorg](</wzh/index.php?title=Keyboard_input&action=edit&redlink=1> "Keyboard input（页面不存在）")以了解 _xev_ 实用程序的细节，它将在你按下一个键时输出相关的键码与键符信息。 

**提示：** 多媒体键有预定义的描述性键符，例如 `XF86AudioMute` 或 `XF86Mail` 。这些键符可以在`/usr/include/X11/XF86keysym.h` 中找到。许多多媒体程序都被设计成可以直接通过这些键符控制，而不需要配置任何第三方应用程序。 

请注意，xmodmap会受到 xkbd 设置的影响，所以所有8个键符都可以用于美式键盘（国际）的 xkbd 布局，但不能用于默认的美式键盘（它缺少ISO Level3中定义的ralt_switch符号）。为了让所有8个键位都可用，你应该配置把键盘设置为美式键盘（国际）。 以美式键盘布局为例，在调用 xmodmap 之前调用 `$ setxkbmap -layout 'us(intl)'` 以在当前X会话中测试您的更改。要永久地做这个改变，请编辑 xorg 配置或您的 .xprofile 或 .xinitrc 文件。完整解释参见[Xorg/Keyboard configuration#Setting keyboard layout](</wzh/index.php?title=Xorg/Keyboard_configuration&action=edit&redlink=1> "Xorg/Keyboard configuration（页面不存在）")。 

##  自定义映射表

创建一个键映射表（即文件 `~/.Xmodmap`）： 
    
    $ xmodmap -pke > ~/.Xmodmap
    
测试您的更改： 
    
    $ xmodmap ~/.Xmodmap
    
###  激活自定义映射表

对于[GDM](<../zh-cn/GDM.html> "GDM")、[XDM](<../zh-cn/XDM.html> "XDM")或[LightDM](<../zh-cn/LightDM.html> "LightDM")，不需要特别激活`~/.Xmodmap`。对于[startx](<../zh-cn/Xinit.html> "Startx")，请使用： 
    
    ~/.xinitrc
    
    [[ -f ~/.Xmodmap ]] && xmodmap ~/.Xmodmap
    
也可以编辑全局启动脚本 `/etc/X11/xinit/xinitrc`。 

###  测试更改

进行临时修改： 
    
    $ xmodmap -e "keycode 46 = l L l L lstroke lstroke lstroke"
    $ xmodmap -e "keysym a = e E"
    
##  修饰键

_xmodmap_ 也可以用来覆盖[修饰键](<https://en.wikipedia.org/wiki/Modifier_key> "wikipedia:Modifier key")，例如交换`Control`和`Super`（即 [Windows 键](<https://en.wikipedia.org/wiki/Windows_key> "wikipedia:Windows key")）。 

打印当前完整的修饰符表： 
    
    $ xmodmap -pm
    
    xmodmap:  up to 4 keys per modifier, (keycodes in parentheses):
    
    shift       Shift_L (0x32),  Shift_R (0x3e)
    lock        Caps_Lock (0x42)
    control     Control_L (0x25),  Control_R (0x69)
    mod1        Alt_L (0x40),  Meta_L (0xcd)
    mod2        Num_Lock (0x94)
    mod3      
    mod4        Super_R (0x86),  Super_L (0xce),  Hyper_L (0xcf)
    mod5        ISO_Level3_Shift (0x5c),  ISO_Level3_Shift (0x6c),  Mode_switch (0x85),  Mode_switch (0xcb)

###  找到键符的修饰键

ISO_Level3_Shift
    非美式键盘上的AltGr键调用修饰键ISO_Level3_Shift。（在美式键盘上，右alt `Alt_R`与左alt `Alt_L`具有相同的功能，因此将布局设置为美式键盘（国际）会更灵活。参见[#键映射表](<#%E9%94%AE%E6%98%A0%E5%B0%84%E8%A1%A8>)）
Mode_switch
    默认情况下，Mode_switch修饰键可能会被映射到一个虚拟的键。

**注意：** 修饰键`ISO_Level3_Shift`和`Mode_switch`的名称对于xmodmap和[X键盘扩展](<../zh-cn/X_keyboard_extension.html#xmodmap> "X keyboard extension")是不同的。参见[[3]](<https://unix.stackexchange.com/questions/55076/what-is-the-mode-switch-modifier-for>)。

###  重新安排修饰键位

**注意：** xmodmap是 _区分大小写_ 的。使用不正确的大小写，如`Mode_Switch`，（正确的是 `Mode_switch`）会导致错误。

在重排之前，需要清除修饰键。原来的键和新的键都得清除。例如，如果您打算将`Caps_Lock`换到A键，将`B`换成NumLock键，那么`Caps_Lock`,`Num_Lock`,A,B四个键都得清除，然后分配键位，最后再把他们加回来。 
    
    ~/.Xmodmap
    
    [...]
    clear lock
    clear mod2
    keycode  38 = Caps_Lock
    keycode  77 = Num_Lock
    add lock = Caps_Lock
    add mod2 = Num_Lock

`!`用于注释一行，所以在下面的例子中，只有 `Control` 和 `Mod4` 这两个修饰符被清除。然后，键符`Control_L`、`Control_R`、`Super_L`和`Super_R`被分配给对应相反的修饰键。将左键和右键都分配给同一个修饰键意味着两个键会被当成同一个键。 
    
    ~/.Xmodmap
    
    [...]
    !clear Shift
    !clear Lock
    clear Control
    !clear Mod1
    !clear Mod2
    !clear Mod3
    clear Mod4
    !clear Mod5
    !add Shift   = Shift_L Shift_R
    !add Lock    = Caps_Lock
    add Control = Super_L Super_R
    !add Mod1    = Alt_L Alt_R
    !add Mod2    = Mode_switch
    !add Mod3    =
    add Mod4    = Control_L Control_R
    !add Mod5    =

**注意：** 本例假设`Control_L`和`Control_R`键符分配给了`Control`修饰键，`Super_L`和`Super_R`键符分配给了`Mod4`修饰键。如果你得到以下错误信息`X Error of failed request: BadValue (integer parameter out of range for operation)`，您需要进行相应的调整。运行`xmodmap`会产生一个修饰键和分配给它们的键符列表。

下面的例子将`CapsLock`修改为`Control`，将`Shift+CapsLock`修改为`CapsLock`： 
    
    ~/.Xmodmap
    
    clear lock
    clear control
    add control = Caps_Lock Control_L Control_R
    keycode 66 = Control_L Caps_Lock NoSymbol NoSymbol

##  反向滚动

OS X Lion中可用的[自然滚动](<https://who-t.blogspot.com/2011/09/natural-scrolling-in-synaptics-driver.html>)功能（模仿智能手机或平板电脑滚动）可以通过 _xmodmap_ 来[实现](<https://bbs.archlinux.org/viewtopic.php?id=126258>)。由于 synaptics 驱动程序使用 4/5/6/7 按钮进行上/下/左/右滚动，你只需要调换一下 `~/.Xmodmap` 中按钮的声明顺序： 
    
    ~/.Xmodmap
    
    pointer = 1 2 3 **5 4** 7 6 8 9 10 11 12

然后更新 _xmodmap_ ： 
    
    $ xmodmap ~/.Xmodmap
    
##  交换鼠标按钮

鼠标左、中、右按钮分别对应于 synaptics 驱动程序中的按钮 1、2和3。如果要交换鼠标左键和右键，也只需将它们在`~/.Xmodmap`中的顺序颠倒过来即可。 
    
    ~/.Xmodmap
    
    pointer = **3 2 1**

这对于一个简单的鼠标设置来说应该足够了。再次更新 _xmodmap_ 。 
    
    $ xmodmap ~/.Xmodmap
    
##  模板

###  西班牙语
    
    ~/.Xmodmap
    
    keycode  24 = a A aacute Aacute ae AE ae
    keycode  26 = e E eacute Eacute EuroSign cent EuroSign
    keycode  30 = u U uacute Uacute downarrow uparrow downarrow
    keycode  31 = i I iacute Iacute rightarrow idotless rightarrow
    keycode  32 = o O oacute Oacute oslash Oslash oslash
    keycode  57 = n N ntilde Ntilde n N n
    keycode  58 = comma question comma questiondown dead_acute dead_doubleacute dead_acute
    keycode  61 = exclam section exclamdown section dead_belowdot dead_abovedot dead_belowdot
    !Maps the Mode key to the Alt key
    keycode 64 = Mode_switch
    
###  将 CapsLock 换成 Control

将 `CapsLock` 改为 `Control` 的最简单的例子。 
    
    ~/.Xmodmap
    
    clear lock
    clear control
    keycode 66 = Control_L
    add control = Control_L Control_R
    
###  将CapsLock转为Control，将左Control转为Hyper

笔记本用户可能更喜欢将`CapsLock`作为`Control`。`Left Control`键可以作为`Hyper`修饰键（emacs、openbox或i3的附加修饰键）。 
    
    ~/.Xmodmap
    
    clear      lock 
    clear   control
    clear      mod1
    clear      mod2
    clear      mod3
    clear      mod4
    clear      mod5
    keycode      37 = Hyper_L
    keycode      66 = Control_L
    add     control = Control_L Control_R
    add        mod1 = Alt_L Alt_R Meta_L
    add        mod2 = Num_Lock
    add        mod3 = Hyper_L
    add        mod4 = Super_L Super_R
    add        mod5 = Mode_switch ISO_Level3_Shift
    
###  把右 Super 变成右 Hyper

如果用户希望在全键盘布局中使用 Hyper 键，不妨将右 Super 键作为 Hyper 键。 
    
    ~/.Xmodmap
    
    remove  mod4 = Super_R
    keycode  134 = Hyper_R
    add     mod3 = Hyper_R
    
###  将Shift-数字键与数字键对换（克罗地亚语布局）

对于类似克罗地亚语的布局应该也能正常工作。 
    
    ~/.Xmodmap
    
    keycode 10 = exclam 1 1 exclam asciitilde dead_tilde asciitilde
    keycode 11 = quotedbl 2 2 quotedbl dead_caron caron dead_caron
    keycode 12 = numbersign 3 3 numbersign asciicircum dead_circumflex asciicircum
    keycode 13 = dollar 4 4 dollar dead_breve breve dead_breve
    keycode 14 = percent 5 5 percent degree dead_abovering degree
    keycode 15 = ampersand 6 6 ampersand dead_ogonek ogonek dead_ogonek
    keycode 16 = slash 7 7 slash grave dead_grave grave
    keycode 17 = parenleft 8 8 parenleft dead_abovedot abovedot dead_abovedot
    keycode 18 = parenright 9 9 parenright dead_acute apostrophe dead_acute
    keycode 19 = equal 0 0 equal dead_doubleacute doubleacute dead_doubleacute
    
##  另见

  * [xmodmap(1)](<https://man.archlinux.org/man/xmodmap.1>)。
  * Christian Weiske 写的 [.Xmodmap 与多媒体键](<https://cweiske.de/howto/xmodmap/allinone.html>)
  * Pascal Bleser 写的[使用 xmodmap 映射键盘上缺少的键](<https://dev-loki.blogspot.com/2006/04/mapping-unsupported-keys-with-xmodmap.html>)
  * [LinuxQuestions](<https://linuxquestions.org>)上的[Xmodmap识别的键符列表](<https://wiki.linuxquestions.org/wiki/List_of_Keysyms_Recognised_by_Xmodmap>)
