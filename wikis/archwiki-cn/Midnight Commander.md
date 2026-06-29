  
相关文章

  * [文件管理器功能](<../zh-cn/%E6%96%87%E4%BB%B6%E7%AE%A1%E7%90%86%E5%99%A8%E5%8A%9F%E8%83%BD.html> "文件管理器功能")
  * [lf](<../zh-cn/Lf.html> "Lf")
  * [nnn](<../zh-cn/Nnn.html> "Nnn")
  * [ranger](<../zh-cn/Ranger.html> "Ranger")
  * [Vifm](<../zh-cn/Vifm.html> "Vifm")

**翻译状态：**

  * 本文（或部分内容）译自 [Midnight Commander](<https://wiki.archlinux.org/title/Midnight_Commander> "arch:Midnight Commander")，最近一次同步于 2024-11-16，若英文版本有所[更改](<https://wiki.archlinux.org/title/Midnight_Commander?diff=0&oldid=820786>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Midnight_Commander_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Midnight Commander](<https://midnight-commander.org/>) 是适用于[类 Unix 系统](<https://zh.wikipedia.org/wiki/%E7%B1%BBUnix%E7%B3%BB%E7%BB%9F> "zhwp:类Unix系统")的可视化 Shell。它是一种[传统](<https://en.wikipedia.org/wiki/Category:Orthodox_file_managers> "wikipedia:Category:Orthodox file managers")（双窗格）文件管理器，支持标准文件操作、虚拟文件系统、外部命令面板化以及用户菜单。它还包含内部查看器 [mcview(1)](<https://man.archlinux.org/man/mcview.1>)、编辑器 [mcedit(1)](<https://man.archlinux.org/man/mcedit.1>) 和可视化差异工具 [mcdiff(1)](<https://man.archlinux.org/man/mcdiff.1>)。 

基于多功能的文本接口⸺[ncurses 或 S-Lang](<https://invisible-island.net/ncurses/ncurses-slang.html>)，它可以运行在[常规控制台](<../zh-cn/Linux_%E6%8E%A7%E5%88%B6%E5%8F%B0.html> "Linux 控制台")、[终端模拟器](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E5%B7%A5%E5%85%B7.html#%E7%BB%88%E7%AB%AF%E6%A8%A1%E6%8B%9F%E5%99%A8> "应用程序列表/工具")、通过[安全外壳协议](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "安全外壳协议")（SSH）连接的远程 Shell 中。 

[文档](<https://midnight-commander.org/wiki/doc>)目前仍处于草稿状态。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [mc](<https://archlinux.org/packages/?name=mc>)包，或安装 [mc-git](<https://aur.archlinux.org/packages/mc-git/>)AUR 开发版本。 

###  皮肤

_Midnight Commander_ 默认附带多种皮肤。可以在“选项 > 外观”中设置皮肤。 

另外也可单独安装第三方皮肤： 

  * **mc-solarized-git** — _Midnight Commander_ 的 Solarized 配色方案

     <https://github.com/nkulikov/mc-solarized-skin> || [mc-solarized-git](<https://aur.archlinux.org/packages/mc-solarized-git/>)AUR

  * **mc-skin-modarin-debian** — _modarin_ 主题的精简版

     <https://launchpad.net/debian/+source/mc/3:4.8.13-3> || [mc-skin-modarin-debian](<https://aur.archlinux.org/packages/mc-skin-modarin-debian/>)AUR

另见 [mc(1) § Skins](<https://man.archlinux.org/man/mc.1#Skins>)。 

##  配置

大部分 _Midnight Commander_ 的设置可以通过菜单更改。然而，少部分设置（如剪贴板命令、字符集检测和外部编辑器参数）只能通过 `~/.config/mc/ini` 修改。详见 [mc(1) § Special Settings](<https://man.archlinux.org/man/mc.1#Special_Settings>) 获取完整的选项描述。 

此外，下列环境变量也会被识别： `MC_SKIN`, `MC_KEYMAP`, `MC_XDG_OPEN`, `MC_COLOR_TABLE`, `MC_DATADIR`, `MC_HOME`, `KEYBOARD_KEY_TIMEOUT_US`, `PAGER`, `EDITOR`, `VIEWER`。 

另见 [mc(1) § FILES](<https://man.archlinux.org/man/mc.1#FILES>)。 

### extfs

_extfs_ 允许为 _Midnight Commander_ 创建新的虚拟文件系统。详情见 `/usr/lib/mc/extfs.d/README`。 

##  使用方法

###  界面

主要视图为两个垂直窗格。窗格可以显示目录内容、文本预览、文件详细信息或目录树（详见 [mc(1) § Directory Tree](<https://man.archlinux.org/man/mc.1#Directory_Tree>)）。文件操作可以通过功能键或鼠标访问。更多选项可通过动态用户菜单（`F2`）和选项菜单（`F9`）查看。高于 `F12` 的键（如 `F13` 到 `F20`）可通过 `Shift` 访问。菜单和对话框选项有一个字母高亮，按下该字母（或在文本框中按 `Alt+_字母_`）即可直接激活相关选项。 

底部显示的是与子 Shell 连接的命令行。此 Shell 通常与启动 _Midnight Commander_ 时使用的类型相同，可以随时切换（`Ctrl+o`），详见 [mc(1) § The subshell support](<https://man.archlinux.org/man/mc.1#The_subshell_support>)。在该命令行上， _cd_ 由 _Midnight Commander_ 解释，而不是传递给 Shell 执行。因此，某些特殊补全功能（如 [Zsh](<../zh-cn/Zsh.html> "Zsh") 提供的功能）不可用。窗格中的文件可与命令行交互，例如，按 `Alt+Enter` 可将（选中的）文件名复制到命令行。 

按键绑定通常类似于 [GNU Emacs](<../zh-cn/GNU_Emacs.html> "GNU Emacs")。可以启用更严格的 emacs 键映射（详见 [mc(1) § Redefine hotkey bindings](<https://man.archlinux.org/man/mc.1#Redefine_hotkey_bindings>)）。新用户也可以使用 [Lynx](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E4%BA%92%E8%81%94%E7%BD%91.html#%E6%8E%A7%E5%88%B6%E5%8F%B0> "应用程序列表/互联网") 样式（箭头）键绑定和鼠标点击进行导航。 

在 Linux 虚拟控制台中，可以通过 [General purpose mouse](<../zh-cn/General_purpose_mouse.html> "General purpose mouse") 启用鼠标支持。 

###  模块

可以通过 _Midnight Commander_ 界面调用这些模块（需在“选项 > 配置”中启用“使用内部模块”），或作为 _mc_ 可执行文件的[符号链接](<https://en.wikipedia.org/wiki/Symbolic_links> "wikipedia:Symbolic links")单独运行。 

  * [mcedit(1)](<https://man.archlinux.org/man/mcedit.1>)——文本和二进制文件编辑器，支持正则替换、语法高亮、宏和 Shell 管道
  * [mcview(1)](<https://man.archlinux.org/man/mcview.1>)——文本和十六进制查看器，带有转到标记和正则搜索
  * [mcdiff(1)](<https://man.archlinux.org/man/mcdiff.1>)——对比并就地编辑两个文件（`Ctrl+x` `d`）

每个 _Midnight Commander_ 实例可以并行运行多个模块，并使用 `Alt+`` 切换，详见 [mc(1) § Screen selector](<https://man.archlinux.org/man/mc.1#Screen_selector>)。也可改用外部编辑器，并相应配置参数。 

##  小技巧

###  从菜单启动

可以通过正确的[桌面项](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%A1%B9.html> "桌面项")从菜单启动 _Midnight Commander_ 。例如： 
    
    [Desktop Entry]
    Type=Application
    Version=1.0
    Name=Midnight Commander
    Comment=Visual file manager
    Exec=mc
    Icon=folder
    MimeType=inode/directory
    Terminal=true
    Categories=Utility;
    
###  垃圾箱支持

_Midnight Commander_ 默认[不支持](<https://midnight-commander.org/ticket/3072>)垃圾箱功能。 

####  使用 libtrash

安装 [libtrash](<https://aur.archlinux.org/packages/libtrash/>)AUR 软件包，并在 Shell 的初始化文件（如 `~/.bashrc` 或 `~/.zshrc`）中创建一个 _mc_ 的别名： 
    
    alias mc='LD_PRELOAD=/usr/lib/libtrash.so mc'
    
应用更改后，重新打开 Shell 会话或使用 `source` 重新加载初始化文件。 

默认设置定义在 `/etc/libtrash.conf.sys`；默认垃圾箱目录为 `~/Trash/`。你可以在 `~/.libtrash` 中为用户覆盖这些设置，例如： 
    
    ~/.libtrash
    
    TRASH_CAN = .Trash
    INTERCEPT_RENAME = NO
    IGNORE_EXTENSIONS= o;exe;com
    UNCOVER_DIRS=/dev

现在，通过 _Midnight Commander_ 删除的文件将会被移动到 `~/.Trash/` 目录。 

**警告：**

  * 从 _Midnight Commander_ 启动的应用程序会继承 `LD_PRELOAD`，这可能会导致某些应用程序出现问题。 [[1]](<http://pages.stern.nyu.edu/~marriaga/software/libtrash/>)
  * 如果设置了 `GLOBAL_PROTECTION = YES`（默认），即使是在不同的分区，删除家目录以外的文件时，文件也会被移动到垃圾箱。视文件大小，此操作可能会导致明显的延迟。

另见 [GNOME 邮件列表上的讨论](<https://mail.gnome.org/archives/mc/2010-March/msg00041.html>)。 

###  mcedit 语法高亮

[mcedit(1) § 语法高亮](<https://man.archlinux.org/man/mcedit.1#%E8%AF%AD%E6%B3%95%E9%AB%98%E4%BA%AE>) 部分[缺失](<https://midnight-commander.org/ticket/4543>)了部分关键内容，可参阅 `man 1 cooledit` 中对应部分。建议同时阅读 _mcedit_ 和 _cooledit_ 的手册页，或应用[补丁](<https://midnight-commander.org/attachment/ticket/4543/merge_cooledit_syntax_highlighting.patch>)。 

##  故障排除

###  退出到当前目录

退出时，Shell 会返回到启动 _Midnight Commander_ 的目录，而不是最后活跃的目录。可以通过添加以下行到 `~/.bashrc` 或 `~/.zshrc` 使用包装脚本解决： 
    
    alias mc=". /usr/lib/mc/mc-wrapper.sh"
    
对于 [fish](<../zh-cn/Fish.html> "Fish") Shell，请使用此包装器：[http://mc-wrapper.fish](<https://gist.github.com/halicki/58cedaf90f3e85277a799cef8217fc72#file-mc-wrapper-fish>)。将其放置于 `~/.config/fish/functions/mc.fish`，或在 `fish` Shell 中执行其内容，然后运行： 
    
    funcsave mc
    
另一种简单的解决方案是使用子 Shell（`Ctrl+o`）。但这可能会与其他终端应用程序产生冲突。 

###  屏幕乱码

按 `Ctrl+l` 重绘显示。这仅会重绘屏幕，但不会刷新文件列表（`Ctrl+r`）。 

###  打开文件

_Midnight Commander_ 通过 `MC_XDG_OPEN` [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")打开文件，默认为 [xdg-open](<../zh-cn/Xdg-utils.html#xdg-open> "Xdg-open") [[2]](<https://github.com/MidnightCommander/mc/blob/master/misc/ext.d/misc.sh.in>)。 

如果 _Midnight Commander_ 被阻塞直到进程结束，或者进程与 mc 一同退出，可使用 `nohup &`： 
    
    ~/bin/nohup-open
    
    #!/bin/bash
    **nohup** xdg-open "$@" **&**
    
并设置 `MC_XDG_OPEN`： 
    
    $ export MC_XDG_OPEN=~/bin/nohup-open
    
**提示：** 当[#使用 libtrash](<#%E4%BD%BF%E7%94%A8_libtrash>)时，在脚本中添加 `unset LD_PRELOAD` 以避免冲突。

###  查找文件无结果

如果“查找文件”对话框（快捷键 `Alt+?`, `Esc+?`, 或 _F9_ 菜单 > _命令_ > _查找文件_ ）未返回结果，检查当前目录下是否存在“符号链接”。“查找文件”不会跟随符号链接，可使用绑定挂载（参见 [mount(8)](<https://man.archlinux.org/man/mount.8>)）或“外部面板化”命令替代。 

###  快捷键失效

某些终端定义（如 `screen-256color` 或 `xterm-termite`）下，快捷键（如 `Shift+F6`）可能失效或表现异常。可以通过“学习按键”对话框手动分配终端序列。 

设置会存储在 `~/.config/mc/ini` 文件中，例如对 `screen-256color` 的设置： 

**注意：** 以下示例假设 `F13`–`F20` 绑定为 `Shift+F3`–`Shift+F10`。
    
    [terminal:screen-256color]
    f1=\\eOP
    f2=\\eOQ
    f3=\\eOR
    f4=\\eOS
    f5=\\e[15~
    f6=\\e[17~
    f7=\\e[18~
    f8=\\e[19~
    f9=\\e[20~
    f10=\\e[21~
    f11=\\e[23~
    f12=\\e[24~
    f13=\\e[1\;2R
    f14=\\e[1\;2S
    f15=\\e[15\;2~
    f16=\\e[17\;2~
    f17=\\e[18\;2~
    f18=\\e[19\;2~
    f19=\\e[20\;2~
    f20=\\e[21\;2~
    complete=\\e^i
    backtab=\\e[Z
    backspace=^?

###  自定义 Xterm 窗口标题

**Xterm 窗口标题** 格式[固定为](<https://github.com/MidnightCommander/mc/blob/ce571933c9f642ff4ef2197a395da9aa2bb14120/src/filemanager/layout.c#L1567>) `mc [_username_ @_hostname_]:_current/path_`，参见[对应问题条目](<https://midnight-commander.org/ticket/1364>)。 

[mc(1) § Screen selector](<https://man.archlinux.org/man/mc.1#Screen_selector>)（“屏幕列表”）文件管理器（“窗格：”）的条目格式也[被固定](<https://github.com/MidnightCommander/mc/blob/ce571933c9f642ff4ef2197a395da9aa2bb14120/src/filemanager/filemanager.c#L439>)。 

[mcdiff(1)](<https://man.archlinux.org/man/mcdiff.1>)、[mcedit(1)](<https://man.archlinux.org/man/mcedit.1>) 和 [mcview(1)](<https://man.archlinux.org/man/mcview.1>) [不会](<https://midnight-commander.org/ticket/4538>)更改 _Xterm 窗口标题_ 。 
