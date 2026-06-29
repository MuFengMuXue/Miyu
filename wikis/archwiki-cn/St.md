**翻译状态：**

  * 本文（或部分内容）译自 [St](<https://wiki.archlinux.org/title/St> "arch:St")，最近一次同步于 2022-07-29，若英文版本有所[更改](<https://wiki.archlinux.org/title/St?diff=0&oldid=738889>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/St_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[st](<https://st.suckless.org/>) 是一个简单的由 [suckless](<https://suckless.org/>) 制作的用于 [Xorg](<../zh-cn/Xorg.html> "Xorg") 上的终端实现。它被用作 [xterm](</wzh/index.php?title=Xterm&action=edit&redlink=1> "Xterm（页面不存在）") 或 [urxvt](<../zh-cn/Rxvt-unicode.html> "Urxvt") 的轻量替代。它当前支持 256 颜色,真颜色,大多数 VT10X 转义序列,UTF-8,X11 复制/粘贴,抗锯齿字体,备用字体,调整大小,快捷键和线描。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [st](<https://aur.archlinux.org/packages/st/>)AUR 软件包 或 开发版本的 [st-git](<https://aur.archlinux.org/packages/st-git/>)AUR 软件包。 

  * 在 [Wayland](<../zh-cn/Wayland.html> "Wayland") 上, _st_ 使用 Xwayland;如果你想要一个类似的终端来避免 Xwayland 的内存占用,请考虑使用 [wterm-git](<https://aur.archlinux.org/packages/wterm-git/>)AUR。

##  配置

_st_ 是通过它在编译时被复制的 `config.h` 文件来配置的。默认配置保存在源代码中的 `config.def.h`。考虑制作你自己的 `config.h` 和 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD")。 

### Shell

要想修改 _st_ 的默认 shell ,编辑这一行: 
    
    static char *shell = "/bin/sh";
    
或将你想要的 shell 作为最后一个参数启动 _st_ : 
    
    $ st _options_ fish
    
###  终端

要想修改终端的类型, 编辑这一行: 
    
    static char *termname = "st-256color";
    
_st_ 会将 `TERM` 变量的值设置为 `termname`。 

###  字体

根据你的喜好编辑下面这一行: 
    
    static char *font = "Liberation Mono:pixelsize=12:antialias=false:autohint=false";
    
你也可以在命令行中传递使用的字体: 
    
    $ st -f "Liberation Mono:size=12"
    $ st -f 'Liberation Mono-12'
    
字体的名字可以用 `fc-list` 命令显示。 

###  光标

默认的光标指针为难以找到的 `XC_xterm`。要想改为你的光标主题的普通光标,编辑下面这一行: 
    
    static unsigned int mouseshape = XC_left_ptr;
    
###  颜色

编辑下列行来设置前景,背景和光标颜色: 
    
    unsigned int defaultfg = 7;
    unsigned int defaultbg = 0;
    static unsigned int defaultcs = 256;
    
这些值引用配置文件中的 `*colorname[]` 数组。你可以使用默认的颜色或在 `#rrggbb` 中添加你自己的颜色: 
    
    static const char *colorname[] = {
       	/* 8 normal colors */
           "black",
           "red3",
           "green3",
           "yellow3",
           "blue2",
           "magenta3",
           "cyan3",
           "gray90",
     
           /* 8 bright colors */
           "gray50",
           "red",
           "green",
           "yellow",
           "#5c5cff",
           "magenta",
           "cyan",
           "white",
     
           [255] = 0,
     
           /* more colors can be added after 255 to use with DefaultXX */
           "#cccccc",
           "#eeeeee",
           "#111111",
     };
     
    /*
     * Default colors (colorname index)
     * foreground, background, cursor
     */
    unsigned int defaultfg = 257;
    unsigned int defaultbg = 258;
    static unsigned int defaultcs = 256;

有便于创建调色板的工具。举个例子 [terminal.sexy](<https://terminal.sexy>) 有一套预制的颜色并且可以直接导出为 _st_ 的格式(请见 [issue 22 的评论](<https://github.com/stayradiated/terminal.sexy/issues/22#issuecomment-430629424>))。 

有 Solarized 颜色主题的补丁。请见 <https://st.suckless.org/patches/solarized/> 来安装。 

###  补丁

[suckless 网站](<https://st.suckless.org/patches/alpha/>)有许多补丁。要想使用补丁,下载 [diff](<https://www.gnu.org/software/diffutils/manual/html_node/Invoking-diff.html>) 并且使用 `patch -i patch.diff` 命令来安装补丁。这会修改默认的配置文件 `config.def.h`;如果你正在制作你自己的 `config.h`,将你的配置从 `config.h` 复制到一份 `config.def.h` 的副本中并且将它重命名为 `config.h`,然后执行 `make clean install` 命令。 

###  Desktop 条目

要想用在[桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")优美的字体(例如 [adobe-source-code-pro-fonts](<https://archlinux.org/packages/?name=adobe-source-code-pro-fonts>)包)简化 _st_ 的启动,你可以创建一个 [Desktop 条目](<../zh-cn/Desktop_entries.html> "Desktop entries"): 
    
    ~/.local/share/applications/st.desktop
    
    [Desktop Entry]
    Name=Simple Terminal
    GenericName=Terminal
    Comment=Suckless terminal emulator for X
    Exec=st -t "Simple Terminal" -f "Source Code Pro:style=Semibold:size=12"
    Terminal=false
    Type=Application
    Encoding=UTF-8
    Icon=utilities-terminal
    Categories=System;TerminalEmulator;
    Keywords=shell;prompt;command;commandline;cmd;

菜单条目会在 _系统工具_ 应用列表中以 _Simple Terminal_ 出现。 

##  故障排除

###  键盘

将下列内容添加到 `~/.inputrc` 或 `/etc/inputrc` 如果 {{ic}Delete}} 不能在某些应用里正常工作。 
    
    set enable-keypad on
    
如果以上操作后还不能在某些使用 bash 的应用,例如 IPython ,中正常工作,相反,关闭 `enable-keypad` 并且将下列内容加入到你的 `~/.bashrc`,就如在[st FAQ](<https://git.suckless.org/st/file/FAQ.html#l55>)提到的做: 
    
    printf '\033[?1h\033=' >/dev/tty
    
### Vim

####  _vim_ 中非字母的文字的背景颜色不会被填充

试着在你的 `config.h` 设置 `termname` 的值为 `st-256color` 然后重新编译。并且不要在你的 shell 中设置 `TERM` 变量,至少不要设置成 `st-256color` ,因为似乎会造成问题。 

另一个也许更好的解决方法,是在 `.vimrc` 文件中加入下列内容: 
    
    if &term =~ '256color'
        " disable Background Color Erase (BCE) so that color schemes
        " render properly when inside 256-color tmux and GNU screen.
        " see also <https://sunaku.github.io/vim-256color-bce.html>
        set t_ut=
    endif
    
####  256颜色和真颜色在 tmux 或其他终端复用器中不工作

首先,确保你在你的 `~/.bashrc` 没有设置且没有导出 `TERM` 的值,正如在这篇[帖子](<https://bbs.archlinux.org/viewtopic.php?pid=1755862#p1755862>)中提到的。 

**注意：** 请不要显式设置 `TERM` 变量。通过在你的 `tmux.conf` 设置 `default-terminal` 来正确地设置。

接着,确保你使用的 `vim` 版本为 **`>=7.4.1799`**, 该版本加入了 `termguicolors`。 

最后,在 `~/.vimrc` 中添加下列内容: 
    
    set t_8f=^[[38;2;%lu;%lu;%lum        " set foreground color
    set t_8b=^[[48;2;%lu;%lu;%lum        " set background color
    colorscheme Tomorrow-Night-Eighties
    set t_Co=256                         " Enable 256 colors
    set termguicolors                    " Enable GUI colors for the terminal to get truecolor
    
**注意：**`^[` 是 (`Esc`) 的转义字符,它为每个 `t_8f` 和 `t_8b` 的值添加前缀。它是一个单独的字符,可以在 `vim` 中打出来。在 **INSERT** 模式中,按下 `Ctrl+v` 然后按 `Esc`。你还会保持在 **INSERT** 模式;再次按下 `Esc` 来回到 **NORMAL** 模式。 

**提示：** 建议在设置 `colorscheme`, `t_Co` 和 `termguicolors` 之前设置 `t_8f` 和 `t_8b`。

要想获得更多信息,请见 `vim` 中的 `:help`: `xterm-true-color`, `t_8f`, `t_8b`。 

##  请见

  * [主页](<https://st.suckless.org/>)
  * [常见问题](<https://git.suckless.org/st/plain/FAQ>)
  * [官方 git 仓库](<https://git.suckless.org/st/>)
