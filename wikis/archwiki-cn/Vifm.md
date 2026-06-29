相关文章

  * [文件管理器功能](<../zh-cn/%E6%96%87%E4%BB%B6%E7%AE%A1%E7%90%86%E5%99%A8%E5%8A%9F%E8%83%BD.html> "文件管理器功能")
  * [lf](<../zh-cn/Lf.html> "Lf")
  * [Midnight Commander](<../zh-cn/Midnight_Commander.html> "Midnight Commander")
  * [nnn](<../zh-cn/Nnn.html> "Nnn")
  * [ranger](<../zh-cn/Ranger.html> "Ranger")

**翻译状态：**

  * 本文（或部分内容）译自 [Vifm](<https://wiki.archlinux.org/title/Vifm> "arch:Vifm")，最近一次同步于 2024-11-16，若英文版本有所[更改](<https://wiki.archlinux.org/title/Vifm?diff=0&oldid=820793>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Vifm_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

译自 [Vifm](<https://vifm.info/>) 官方主页： 

    Vifm 是一个带 curses 界面的文件管理器，提供类似 Vim 的文件系统管理环境，并结合了来自 [mutt](<../zh-cn/Mutt.html> "Mutt") 的一些有用想法。
    如果你使用 [vi](<../zh-cn/Vi.html> "Vi")，Vifm 让你无需学习新命令即可完全通过键盘控制你的文件。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [vifm](<https://archlinux.org/packages/?name=vifm>)包 包，或者安装开发版本 [vifm-git](<https://aur.archlinux.org/packages/vifm-git/>)AUR。 

##  帮助文件

Vifm 的基本信息在帮助文件中可以找到。打开 Vifm 并输入以下命令即可查看： 
    
    :h
    
另一个信息来源是 [vifm(1)](<https://man.archlinux.org/man/vifm.1>)。 

##  自定义 Vifm

Vifm 会在 [XDG_CONFIG_HOME](<../zh-cn/XDG_%E5%9F%BA%E6%9C%AC%E7%9B%AE%E5%BD%95.html#%E7%94%A8%E6%88%B7%E7%9B%AE%E5%BD%95> "XDG 基本目录") 中创建并填充一个 `vifm` 目录，包含以下内容： 

  * `vifmrc`——一个注释丰富的配置文件，可根据个人工作风格编辑。
  * `vifm-help.txt`——帮助文本。
  * `vifminfo`——书签和回收站内容——不建议手动编辑此文件。
  * `Trash/` 目录——顾名思义——请在 vifm 中查看 `:h vifm-trash`。
  * `scripts/` 目录——请在 vifm 中查看 `:h vifm-scripts`。
  * `colors/` 目录——颜色主题——请在 vifm 中查看 `:h vifm-colors`。 
    * `Default.vifm`——注释丰富的默认颜色主题，可复制以创建用户自定义的颜色主题。

入门时，建议阅读以下信息来源： 

  * `/usr/share/doc/vifm/`
  * `/usr/share/vifm/vifm-help.txt` 或 `man vifm`
  * `:h` 在 vifm 内输入

###  颜色主题

`~/.vifm/colors` 目录包含颜色主题。其格式在文件中有所概述，遵循 vi/vim 的语法高亮格式。其基本形式如下： 
    
    highlight _组_ cterm=_属性_ ctermfg=_颜色_ ctermbg=_颜色_
    
示例颜色主题如下： 
    
    highlight Win cterm=none ctermfg=white ctermbg=black
    highlight Directory cterm=bold ctermfg=cyan ctermbg=none
    highlight Link cterm=bold ctermfg=yellow ctermbg=none
    highlight BrokenLink cterm=bold ctermfg=red ctermbg=none
    highlight Socket cterm=bold ctermfg=magenta ctermbg=none
    highlight Device cterm=bold ctermfg=red ctermbg=none
    highlight Fifo cterm=bold ctermfg=cyan ctermbg=none
    highlight Executable cterm=bold ctermfg=green ctermbg=none
    highlight Selected cterm=bold ctermfg=magenta ctermbg=none
    highlight CurrLine cterm=bold ctermfg=none ctermbg=blue
    highlight TopLine cterm=none ctermfg=black ctermbg=white
    highlight TopLineSel cterm=bold ctermfg=black ctermbg=none
    highlight StatusLine cterm=bold ctermfg=black ctermbg=white
    highlight WildMenu cterm=underline,reverse ctermfg=white ctermbg=black
    highlight CmdLine cterm=none ctermfg=white ctermbg=black
    highlight ErrorMsg cterm=none ctermfg=red ctermbg=black
    highlight Border cterm=none ctermfg=black ctermbg=white
    
你也可以使用正则表达式高亮不同的文件类型： 
    
    highlight /^.*\.(mp3|ogg|oga|flac|m4a)$/ ctermfg=magenta
    highlight /^.*\.(jpg|jpeg|png|gif|tiff|webp|bmp|svg|svgz)$/ ctermfg=yellow
    highlight /^.*\.(zip|gz|bz2|xz|tar|tgz|tbz2|7z|rar|iso|rpm|deb)$/ ctermfg=red
    
其他颜色主题可以在[这里](<https://vifm.info/colorschemes.shtml>)查看。 

###  键映射

从 0.6.2 版本开始，你可以自定义 Vifm 的键绑定。这些可以通过命令模式使用 `map` 命令设置，如下： 
    
    :map ] :s
    
但这些映射在会话间不会保存。要永久映射键，可以将它们放在 `vifmrc` 文件中。更多示例映射可以在该文件末尾找到。 

###  在 Vifm 中打开文件

你可以在 `vifmrc` 文件中为文件类型指定应用程序，例如： 
    
    filetype *.jpg,*.jpeg,*.png,*.gif feh %f 2>/dev/null &
    filetype *.md5 md5sum -c %f
    
`vifmrc` 中提供了一些默认值，可以按照相同的格式进行编辑或添加。 

####  使用 [feh](<../zh-cn/Feh.html> "Feh") 浏览当前目录的图片
    
    filetype *.jpg,*.jpeg,*.png,*.gif
           \ {View in feh}
           \ feh -FZ %d --start-at %d/%c 2>/dev/null
    
这将显示你选中的图片，并使你能够按默认顺序浏览目录中的其他图片。 

###  自定义命令

你也可以在 `vifmrc` 文件中创建自定义命令，例如： 
    
    command df df -h %m 2> /dev/null
    command diff vim -d %f %F
    
####  创建符号链接
    
    command link ln -s %d/%f %D
    
当你执行 
    
    :link
    
时，将在另一目录中（若处于分屏视图）为选中文件创建一个链接。此功能甚至适用于通过视觉模式（v）或标记（t）选中的多个文件。 

####  创建种子文件

为当前文件在另一个选项卡的目录中创建 .torrent 文件： 
    
    command mkt mktorrent -p -a [你的 announce URL] -o %D/%f.torrent %d/%f
    
###  标记

标记的设置方式与 vi 中相同。 为当前文件设置标记： 
    
    m[a-z][A-Z][0-9]
    
跳转到标记的文件： 
    
    '[a-z][A-Z][0-9]
    
Vifm 会在会话间记住这些标记。 

###  预览

若安装了 [poppler](<https://archlinux.org/packages/?name=poppler>)包，则可通过以下设置预览 PDF 文件： 
    
    fileviewer *.pdf
      \ pdftotext %c -
    
其中 `%c` 是 vifm 中当前光标所在文件的宏。输入以下命令激活预览： 
    
    :view
    
通过 [libcaca](<https://archlinux.org/packages/?name=libcaca>)包 提供的 img2txt 可以实现图像预览： 
    
    fileviewer *.png,*.jpeg,*.jpg
     \ img2txt %c
    
预览 tar 压缩包内容： 
    
    fileviewer *.tar,*.tar.gz
     \ tar -tvf %c
    
HTML 文档的预览可以通过文本浏览器（如 [lynx](<https://archlinux.org/packages/?name=lynx>)包、[links](<https://archlinux.org/packages/?name=links>)包 或 [w3m](<https://archlinux.org/packages/?name=w3m>)包）实现： 
    
    fileviewer *.html
     \ w3m %c
    
对于 Office 文件，可以将其转换为 HTML 格式再通过 w3m 渲染： 
    
    fileviewer *.odt,*.doc,*.docx,*.ods,*.xls,*.xlsx
     \ libreoffice --convert-to html --outdir /tmp/ %c &>/dev/null && w3m /tmp/%c:r.html
    
对于二进制文件等无法直接预览的情况，输出简单的文本信息： 
    
    fileviewer *.exe
     \ echo Binary file: no preview available. %i
    
其中 `%i` 用于覆盖默认使用的 `%c`。 

处理其他未指定的文件类型时，可以在配置文件的最后添加： 
    
    fileviewer * <你的命令>
    
一些常用的预览工具包括： 

  * [tree](<https://archlinux.org/packages/?name=tree>)包 用于目录预览。
  * [mp3info](<https://archlinux.org/packages/?name=mp3info>)包 用于查看 mp3 文件的信息。
  * [mediainfo](<https://archlinux.org/packages/?name=mediainfo>)包 用于查看音视频文件的信息。
  * [highlight](<https://archlinux.org/packages/?name=highlight>)包 用于语法高亮。

####  使用 vifmimg

可以将 [vifmimg](<https://github.com/cirala/vifmimg>) 克隆到 `~/.config/vifm` 目录中。之后需要创建一个别名以运行 `vifmrun` 脚本，准备预览功能： 
    
    alias v="~/.config/vifm/vifmrun ."
    
现在只需输入 `v` 即可启动 `vifm`。 

**注意：**

  * 必须安装 [ueberzug](<https://archlinux.org/packages/?name=ueberzug>)包 否则预览功能无法工作。
  * 如果在浏览文件时切换到 shell，可能会遇到预览未消失的问题。可以添加以下命令解决： 
        
        command! clear vifmimg clear

并将该命令绑定到退出当前 `vifm` 运行时切换到 shell 的按键上，例如：
        
        nmap S :clear

这样按下 `S` 键即可进入 shell 并清除预览。

##  提示与技巧

###  有用的键位映射

####  单击进入命令行
    
    nmap ; :
    
####  更快的移动

按住 Shift 键可以跳跃五个文件 
    
    nnoremap J 5j
    nnoremap K 5k
    
####  面板调整大小

只需输入 `-` 或 `_` 来调整面板大小： 
    
    nnoremap - <C-w>5<
    nnoremap _ <C-w>5>
    
####  复制路径

通过输入 `yd` 来复制父目录路径： 
    
    nnoremap yd :!echo -n %d | xclip -selection clipboard %i<cr>:echo expand('%"d') "is yanked to clipboard"<cr>
    
通过输入 `yf` 来复制选中文件的绝对路径： 
    
    nnoremap yf :!echo -n %c:p | xclip -selection clipboard %i<cr>:echo expand('%"c:p') "is yanked to clipboard"<cr>
    
在 Wayland 环境下，使用 [wl-copy](<../zh-cn/%E4%BB%8E%E7%BB%88%E7%AB%AF%E5%A4%8D%E5%88%B6%E6%96%87%E6%9C%AC.html#Wayland> "从终端复制文本") 代替 `xclip -selection clipboard`。 

###  非 vim 用户

如果你使用 `vi`、`nvim`（[Neovim](<../zh-cn/Neovim.html> "Neovim")）或其他编辑器，可以将 `set vicmd=vi`、`set vicmd=nvim` 或类似命令添加到 `vifmrc` 文件的底部。 

###  获取选中文件的总大小

要获取选中文件的总大小，可以将 `%s` 更改为 `%E`，例如： 
    
    set statusline="  %t%= %A %10u:%-7g %15E %20d  "
    
###  在状态栏中显示外部程序的输出

以下是一个在状态栏中显示当前光标下文件属性的例子，调用了 [lsattr](<../zh-cn/File_permissions_and_attributes.html#File_attributes> "File permissions and attributes")： 
    
    set statusline="%{system('lsattr -l ' . expand('%c'))}"
    
###  打印当前选中的文件

如果你想打印选中的文件，可以创建一个 `lp` 命令： 
    
    command! print lp -n 1 -o sides=two-sided-long-edge %f
    
只需选中文件并输入 `:print` 即可打印。 

###  拖放功能

你需要安装 [dragon-drop](<https://aur.archlinux.org/packages/dragon-drop/>)AUR 并添加一个新命令： 
    
    command! dragon dragon-drop -a -x %f
    
你也可以为这个新命令设置快捷键： 
    
    nmap <C-d> :dragon<CR>
    
这样按下 `Ctrl+d` 会为当前选中的文件创建一个窗口，方便你将文件拖到其他地方。如果要拖放多个文件，只需选中文件并按下 `Ctrl+d`。 

更多信息请参见[表达式语法](<https://vifm.info/manual.shtml#Expression%20syntax>)和可用的[函数](<https://vifm.info/manual.shtml#Functions>)。 
