**翻译状态：**

  * 本文（或部分内容）译自 [Linux console](<https://wiki.archlinux.org/title/Linux_console> "arch:Linux console")，最近一次同步于 2025-08-06，若英文版本有所[更改](<https://wiki.archlinux.org/title/Linux_console?diff=0&oldid=842110>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Linux_console_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [/Keyboard configuration](</wzh/index.php?title=Linux_%E6%8E%A7%E5%88%B6%E5%8F%B0/Keyboard_configuration&action=edit&redlink=1> "Linux 控制台/Keyboard configuration（页面不存在）")
  * [捕获屏幕#虚拟控制台](<../zh-cn/%E5%B1%8F%E5%B9%95%E6%8D%95%E8%8E%B7.html#%E8%99%9A%E6%8B%9F%E6%8E%A7%E5%88%B6%E5%8F%B0> "捕获屏幕")
  * [Color output in console](<../zh-cn/Color_output_in_console.html> "Color output in console")
  * [getty](<../zh-cn/Getty.html> "Getty")

根据[维基百科](<https://en.wikipedia.org/wiki/Linux_console> "wikipedia:Linux console")： 

     **Linux 控制台** 是 [Linux 内核](</wzh/index.php?title=Linux_%E5%86%85%E6%A0%B8&action=edit&redlink=1> "Linux 内核（页面不存在）")内部的一个系统控制台。Linux 控制台为内核和其他进程提供了一种向用户发送文本输出并接收用户文本输入的方式。用户通常用计算机键盘输入文本，并在计算机显示器上阅读输出的文本。Linux 内核支持虚拟控制台——在逻辑上独立的控制台，但它们访问相同的物理键盘和显示器。

本文介绍了 Linux 控制台的基础知识以及如何配置字体显示。[/Keyboard configuration](</wzh/index.php?title=Linux_%E6%8E%A7%E5%88%B6%E5%8F%B0/Keyboard_configuration&action=edit&redlink=1> "Linux 控制台/Keyboard configuration（页面不存在）") 子页面中描述了键盘配置。对于提供更多功能的替代控制台解决方案（完整的 Unicode 字体、现代图形适配器等），请参阅 [KMSCON](<../zh-cn/KMSCON.html> "KMSCON") 或类似项目。 

##  实现

与大多数直接与用户交互的服务不同，控制台是在内核中实现的。这与终端仿真软件形成鲜明对比，如 [Xterm](</wzh/index.php?title=Xterm&action=edit&redlink=1> "Xterm（页面不存在）")，它是一个在用户空间实现的普通的应用程序。控制台一直是发布的 Linux 内核的一部分，但在其历史上经历了一些变化，最明显的是过渡到使用 [framebuffer](<https://en.wikipedia.org/wiki/Linux_framebuffer> "wikipedia:Linux framebuffer") 以及对 [Unicode](<https://en.wikipedia.org/wiki/Unicode> "wikipedia:Unicode") 的支持。 

虽然对控制台进行了许多改进，但它对旧硬件完全的向后兼容性意味着与图形终端仿真器相比它是受限的。Linux 控制台与图形终端仿真器的主要区别在于：Linux 控制台中的 shell 直接连接到 [TTY](<../zh-cn/Getty.html> "Tty") 设备（`/dev/tty*`），而图形终端仿真器中的 shell 则连接到伪 TTY（`/dev/pty*`）。 

此外，图形终端仿真器可以拥有比 Linux 控制台更多的功能，包括更丰富的可用字体集、多标签页/窗口、分屏视图、回滚缓冲区/滑块、背景颜色/图像（可选透明）等。其中一些功能可以通过终端多路复用器（如 [Tmux](<../zh-cn/Tmux.html> "Tmux") 或 [GNU Screen](<../zh-cn/GNU_Screen.html> "GNU Screen")）在 Linux 控制台中使用，或通过依赖 ncurses 等库的文本用户界面程序（TUI）实现，例如 [Vim](<../zh-cn/Vim.html> "Vim")、[nano](<../zh-cn/Nano.html> "Nano") 或 [Emacs](<../zh-cn/Emacs.html> "Emacs")。这些功能也可在图形终端仿真器中使用。 

###  虚拟控制台

控制台以一系列[虚拟控制台](<https://en.wikipedia.org/wiki/Virtual_console> "wikipedia:Virtual console")的形式呈现给用户。这些虚拟控制台给人的印象是几个独立的终端在同时运行；每个虚拟控制台可以用不同的用户登录，运行自己的 shell，并有自己的字体设置。每个虚拟控制台都使用一个 `/dev/ttyX` 设备，可以通过按 `Alt+F _x_`（其中 `_x_` 是虚拟控制台编号，从 1 开始）在它们之间切换。`/dev/console` 设备会被自动映射到活动的虚拟控制台。 

另请参阅 [chvt(1)](<https://man.archlinux.org/man/chvt.1>)、[openvt(1)](<https://man.archlinux.org/man/openvt.1>) 和 [deallocvt(1)](<https://man.archlinux.org/man/deallocvt.1>)。 

###  文本模式

由于 Linux 最初是适用于 PC 硬件的内核，所以控制台是使用标准 IBM [CGA/EGA/VGA](<https://en.wikipedia.org/wiki/VGA> "wikipedia:VGA")图形开发的，当时所有 PC 都支持这种图形。图形在 VGA 文本模式下运行，它提供了一个简单的 16 色 80x25 字符显示。这种传统模式类似于专用文本终端的功能，例如 [DEC VT100](<https://en.wikipedia.org/wiki/VT100> "wikipedia:VT100") 系列。如果系统硬件支持的话，仍可以通过内核参数（`vga=0 nomodeset`）以文本模式启动，但几乎所有的现代发行版（包括 Arch Linux）都使用 framebuffer 控制台来代替。 

###  Framebuffer 控制台

随着 Linux 被移植到其他非 PC 架构上，需要一个更好的解决方案，因为其他架构不使用兼容 VGA 的图形适配器，而且可能根本不支持文本模式。framebuffer 控制台的实现是为了在所有平台上提供一个标准的控制台，因此无论底层的图形硬件如何，都会呈现相同的 VGA 风格界面。因此，Linux 控制台不是一个终端模拟器，它本身就是一个终端。它使用终端类型 `linux`，并与 VT100 基本兼容。 

##  键盘快捷键

键盘快捷键  | 描述   
---|---  
`Ctrl+Alt+Del` | 重新启动系统（由符号链接 `/usr/lib/systemd/system/ctrl-alt-del.target` 指定）   
`Alt+F1`、`F2`、`F3`……  | 切换到第 _n_ 个虚拟控制台（不同于 [Xorg 和 Wayland](<../zh-cn/Keyboard_shortcuts.html#Xorg_and_Wayland> "Keyboard shortcuts") 中使用的 `Ctrl+Alt+F _n_`）   
`Alt+左箭头` | 切换到上一个虚拟控制台   
`Alt+右箭头` | 切换到下一个虚拟控制台   
`Scroll Lock` | 当 Scroll Lock 被激活时，输入/输出被锁定   
`Ctrl+c` | 杀死当前任务   
`Ctrl+d` | 插入 EOF   
`Ctrl+z` | 暂停当前任务   
  
参见 [console_codes(4)](<https://man.archlinux.org/man/console_codes.4>)。 

##  字体

[Linux 控制台](<https://en.wikipedia.org/wiki/Linux_console> "wikipedia:Linux console")默认使用 UTF-8 编码，但由于使用的是标准的兼容 VGA 的 framebuffer，终端字体限定为 256 或 512 个字形。如果字体超出了 256 个字形，那么颜色的数量就会从 16 减少到 8。为了为给定的 Unicode 值分配正确的符号来显示，需要一个特殊的翻译映射，通常称为 _unimap_ 。现在，大多数控制台字体都内置了 "unimap"；在历史上，它必须被单独加载。 

默认情况下，[虚拟控制台](<https://en.wikipedia.org/wiki/Virtual_console> "wikipedia:Virtual console")使用内核的内置字体，其包含 [CP437](<https://en.wikipedia.org/wiki/CP437> "wikipedia:CP437") 字符集[[1]](<https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/tty/vt/Makefile#n5>)，但这个设置很容易改变。内核提供了约 15 种内置字体可供选择，其中[官方支持的内核](<../zh-cn/%E5%86%85%E6%A0%B8.html#Officially_supported_kernels> "Kernel")提供两种：VGA 8x16 字体（`CONFIG_FONT_8x16`）和 Terminus 16x32 字体（`CONFIG_FONT_TER16x32`）。内核根据屏幕分辨率的评估结果选择使用的字体。可以通过[内核参数](<../zh-cn/Kernel_parameters.html> "Kernel parameters")强制使用其他内置字体，例如 `fbcon=font:TER16x32`。 

[kbd](<https://archlinux.org/packages/?name=kbd>)包 包提供改变虚拟控制台字体和字体映射的工具。可用的字体存储在 `/usr/share/kbd/consolefonts/` 目录中，以 _.psfu_ 或 _.psfu.gz_ 结尾的字体内置 Unicode 翻译映射。 

键盘映射是按键和计算机使用的字符的对应关系，位于 `/usr/share/kbd/keymaps/` 的子目录中，详情请参阅 [/Keyboard configuration](</wzh/index.php?title=Linux_%E6%8E%A7%E5%88%B6%E5%8F%B0/Keyboard_configuration&action=edit&redlink=1> "Linux 控制台/Keyboard configuration（页面不存在）")。 

**注意：** 替换字体可能会导致需要标准 VGA 样式字体的程序出现问题，例如使用线条绘图图形的程序。

**提示：** 对于用拉丁/希腊字母书写的欧洲语言，可以使用 `eurlatgr` 字体，它包括广泛的拉丁/希腊字母变化以及特殊字符[[2]](<https://lists.altlinux.org/pipermail/kbd/2014-February/000439.html>)。

###  预览和测试

**提示：** 这里有一个整理过的预览影像数据库：[Linux 控制台字体截图](<https://adeverteuil.github.io/linux-console-fonts-screenshots/>)。
    
    $ showconsolefont
    
显示字体可用字形与字符的列表。 

如果指定（`/usr/share/kbd/consolefonts/` 中的）字体名称，`setfont` 将暂时改变字体： 
    
    $ setfont lat2-16 -m 8859-2
    
字体名称区分大小写。如果不加参数，`setfont` 会将控制台字体重设为默认字体。 

因此，要使用一个**小的 8x8** 字体，在安装字体后，使用类似如下所示的命令： 
    
    $ setfont -h8 /usr/share/kbd/consolefonts/drdos8x8.psfu.gz
    
如果要使用**更大** 的字体，Terminus 字体 ([terminus-font](<https://archlinux.org/packages/?name=terminus-font>)包) 有多种尺寸可供选择，例如 `ter-132b` 就很大。 

你也可以添加 `-d` 选项来使用双倍大小。这将使用 64x64 字体： 
    
    $ setfont -d ter-132n
    
**提示：**

  * 所有更改字体的命令都可以“盲打”。
  * Terminus 字体名称（`ter-*`）的解释见 `/usr/share/terminus-font/README`。

**注意：** _setfont_ 只作用于当前正在使用的控制台。其它终端无论活跃与否都不受影响。

###  持久性配置

`/etc/vconsole.conf` 中的 `FONT` 变量可用于在启动时设置字体，这对于所有控制台都具有持久性作用。详情请参见 [vconsole.conf(5)](<https://man.archlinux.org/man/vconsole.conf.5>)。 

要显示 _Č, ž, đ, š_ 或 _Ł, ę, ą, ś_ 之类的字符，请使用 `lat2-16.psfu.gz` 字体： 
    
    /etc/vconsole.conf
    
    ...
    FONT=lat2-16
    FONT_MAP=8859-2

这代表使用 ISO/IEC 8859 字符的第二部分，尺寸设置为 16。可以使用其它值来更改字体尺寸（如 `lat2-08`）。可以在 [zhwp:ISO/IEC 8859#各种ISO 8859字符集](<https://zh.wikipedia.org/wiki/ISO/IEC_8859#.E5.90.84.E7.A7.8DISO_8859.E5.AD.97.E7.AC.A6.E9.9B.86> "zhwp:ISO/IEC 8859")查询 8859 规范定义的区域。 

自 [mkinitcpio v33](<https://gitlab.archlinux.org/archlinux/mkinitcpio/mkinitcpio/-/blob/v33/mkinitcpio.conf#L52>) 起，`/etc/vconsole.conf` 中指定的字体默认通过 `consolefont` 钩子在早期用户空间自动加载，该钩子将字体添加到 initramfs。详情请参见 [Mkinitcpio#钩子(HOOKS)](<../zh-cn/Mkinitcpio.html#%E9%92%A9%E5%AD%90\(HOOKS\)> "Mkinitcpio")。 

更改 `/etc/vconsole.conf` 后，你可能还需要[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `systemd-vconsole-setup.service`。 

如果启动时字体没有变化，或只暂时变化，则最可能是因为初始化图形驱动时字体被复位，然后控制台切换到 framebuffer。默认情况下，所有树内内核驱动程序都会提前加载。NVIDIA 用户应参阅 [NVIDIA#Early loading](<../zh-cn/NVIDIA.html#Early_loading> "NVIDIA") 以在应用 `/etc/vconsole.conf` 之前加载图形驱动程序。 

##  光标外观

此主题文档较少，建议阅读以下文章： 

  * [Software cursor for VGA](<https://docs.kernel.org/admin-guide/vga-softcursor.html>)（VGA 的软件光标）
  * [Cursor Appearance in the Linux Console](<https://linuxgazette.net/137/anonymous.html>)（Linux 控制台中的光标外观）
  * [Disable Cursor Blinking on Linux Console](<https://web.archive.org/web/20220318101402/https://nutr1t07.github.io/post/disable-cursor-blinking-on-linux-console/>)（在 Linux 控制台上禁用光标闪烁）

光标类型  | 硬件 | 软件   
---|---|---  
形状  | 

    (0) 默认 

    应用 (2) 下划线
    (1) 不可见
    (2) 下划线
    (3) 下三分之一
    (4) 下半部
    (5) 下三分之二
    (6) 全方块
| 

    (16) 全方块 

    形状无法更改，但当背景色和前景色相同时，光标实际上不可见  
闪烁  | 

    闪烁
| 

    取决于驱动程序 

    背景色的最高位可解释为"高亮"或"闪烁"  
颜色  | 

    与控制台文本颜色相同（通常为白色/灰色） 

    无法单独设置
| 

    可由用户设置  
  
控制台光标可通过**设备属性（DA）** 控制函数调整。参数序列**必须** 以单个问号开头（尽管 [console_codes(4)](<https://man.archlinux.org/man/console_codes.4>) 有相反的说法）。 

以下是一个全方块、不闪烁、绿色光标（光标下的符号为黑色）的示例： 
    
    $ printf "\x1b\x5b?16;$((8+4+2+1));$((32+0+8+4+2+1))\x63"
    
也可以使用八进制和字符代替十六进制代码表达： 
    
    $ printf '\033[?16;15;47c'
    
**注意：** 控制函数（转义序列）的完整指南请参阅标准 [ECMA-48 — Control Functions for Coded Character Sets](<https://ecma-international.org/wp-content/uploads/ECMA-48_5th_edition_june_1991.pdf>)。

相同的配置可通过[内核参数](<../zh-cn/Kernel_parameter.html> "Kernel parameter")永久应用： 
    
    vt.cur_default=0x2f0f10
    
**注意：** 转义序列参数（**16, 15, 47** ）以十六进制（**10, 0f, 2f** ）按**相反顺序** 写入。

###  光标大小

第一个参数名为 _光标大小_ ，数字 **16** （内核参数最右侧两位十六进制数字为 **10** ）表示"_使用软件光标_ "。 

**注意：** 你可能需要使用 **48** (32+16)、**80** (64+16) 或 **112** (64+32+16) 代替 **16** 。

如果想更改硬件光标形状，使用对应数字（从 **0** 到 **6** ，见上表）。 

**注意：** _光标大小_ 是唯一适用于 _硬件_ 光标的参数。

###  切换掩码

第二个参数称为 _切换掩码_ ，用于翻转颜色的对应位。 

字符属性位  | 背景 _（光标块）_ | 前景 _（光标下的符号）_  
---|---|---  
|  **高亮** 或闪烁  |  **红** |  **绿** |  **蓝** |  **高亮** 或闪烁  |  **红** |  **绿** |  **蓝**  
十进制  | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1   
十六进制  | 80 | 40 | 20 | 10 | 8 | 4 | 2 | 1   
  
在我们的例子中，第二个参数是 **15** （内核参数中间两位十六进制数字为 **0f** ），因此所有四个前景（符号）位都将被翻转。最重要的规则是：切换（第二个参数）在设置（第三个参数）之后应用。 

**注意：** 如果某个位被第三个参数设置**且** 被第二个参数切换——它实际上会被清除。

###  设置掩码

第三个参数称为 _设置掩码_ 。它设置相应的字符属性位。我们在示例中使用 **47** （内核参数最左侧两位十六进制数字为 **2f** ），这表示两点： 

  * (32) 为光标块使用纯绿色
  * (8+4+2+1) 设置所有四个前景（符号颜色）位。这些位将被第二个参数切换，因此光标下的符号颜色将为黑色（`0000`）。

## HiDPI

参见 [HiDPI#Linux 控制台](<../zh-cn/HiDPI.html#Linux_%E6%8E%A7%E5%88%B6%E5%8F%B0> "HiDPI")。 

##  声音提示

参见 [PC 扬声器#beep](<../zh-cn/PC_%E6%89%AC%E5%A3%B0%E5%99%A8.html#beep> "PC 扬声器")。 

##  参见

  * [The TTY demystified – Linus Åkesson](<https://www.linusakesson.net/programming/tty/>)
