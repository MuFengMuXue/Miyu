**翻译状态：**

  * 本文（或部分内容）译自 [Vim](<https://wiki.archlinux.org/title/Vim> "arch:Vim")，最近一次同步于 2023-02-22，若英文版本有所[更改](<https://wiki.archlinux.org/title/Vim?diff=0&oldid=768313>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Vim_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [应用程序列表/文档#Vi 风格的文本编辑器](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E6%96%87%E6%A1%A3.html#Vi_%E9%A3%8E%E6%A0%BC%E7%9A%84%E6%96%87%E6%9C%AC%E7%BC%96%E8%BE%91%E5%99%A8> "应用程序列表/文档")
  * [Neovim](<../zh-cn/Neovim.html> "Neovim")
  * [Emacs](<../zh-cn/Emacs.html> "Emacs")

[Vim](<https://en.wikipedia.org/wiki/Vim_\(text_editor\)> "wikipedia:Vim \(text editor\)")是一个终端文本编辑器。作为[vi](<../zh-cn/Vi.html> "Vi")的一个扩展版本，它具有以下附加功能：语法高亮，全面的帮助系统，本地脚本（Vim script），文本选择的可视模式和文件比较（[vimdiff(1)](<https://man.archlinux.org/man/vim/vimdiff.1>)）。以及有限功能的工具，如 [rview(1)](<https://man.archlinux.org/man/vim/rview.1>) 和 [rvim(1)](<https://man.archlinux.org/man/vim/rvim.1>)。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")下面两个软件包中的一个： 

  * [vim](<https://archlinux.org/packages/?name=vim>)包——提供[Python](<../zh-cn/Python.html> "Python"), [Lua](<../zh-cn/Lua.html> "Lua"), [Ruby](<../zh-cn/Ruby.html> "Ruby") 和 [Perl](</wzh/index.php?title=Perl&action=edit&redlink=1> "Perl（页面不存在）")解释器支持，但没有 [GTK](<../zh-cn/GTK.html> "GTK")/[X](<../zh-cn/Xorg.html> "X") 支持
  * [gvim](<https://archlinux.org/packages/?name=gvim>)包——除了提供和 _vim_ 一样的功能外，还提供GTK/X支持。

**注意：**

  * _vim_ 包不包含 [Xorg](<../zh-cn/Xorg.html> "Xorg") 支持。具体而言，Vim缺失 `+clipboard` 特性，因而不能够使用 _primary_ 和 _clipboard_ [选择缓冲区](<https://wiki.archlinux.org/title/Clipboard>)。 _gvim_ 同时提供命令行版本带`+clipboard`的Vim。
  * 非官方源[herecura](<../zh-cn/Unofficial_user_repositories.html#herecura> "Unofficial user repositories")也提供数个Vim/gVim变种版本: `vim-cli`、`vim-gvim-common`、`vim-gvim-gtk3`、`vim-rt` 和 `vim-tiny`。

##  用法

有关如何使用Vim的基本概述，请遵循vim教程运行 _vimtutor_ （控制台版本）或 _gvimtutor_ （图形界面版本）。 

Vim包含了一个广泛的帮助系统，可以用`:h _subject_`命令来访问。 _subject_ 可以是命令，配置选项，热键绑定，插件等。使用`:h`命令（不带任何 _subject_ ）来获取帮助系统的相关信息以及在不同的主题之间切换。 

##  配置

Vim的用户特定配置文件位于主目录`~/.vimrc`，当前用户的Vim文件位于`~/.vim/`；全局配置文件为`/etc/vimrc`，全局Vim文件是位于`/usr/share/vim/` 的 `defaults.vim` 和 `archlinux.vim`。 对于 gVim，用户特定的配置文件为 `~/.gvimrc`，全局配置文件为 `/etc/gvimrc`。 

**注意：**

  * 常用的功能，如语法高亮在 `defaults.vim` 中启用，当没有 `~/.vimrc` 时加载。将 `let skip_defaults_vim=1` 添加到 `/etc/vimrc` 以完全禁用加载 `defaults.vim`。[[1]](<https://github.com/vim/vim/issues/1033>)。或者，若要启用 `defaults.vim`，即便 `~/.vimrc` 存在，请参见 vim 中的 `:h defaults`。
  * gVim 同时加载 Vim 和 gVim 的配置文件，而 Vim 只加载 Vim 的配置文件。

###  剪贴板

Vim命令如 `:yank` 或 `:put` 通常使用未命名寄存器，默认情况下对应于 `""` 寄存器。如果 `+clipboard` 功能可用且它的值包含 `unnamed`，那么 Vim yank, delete, change 和 put 操作（通常会转到未命名寄存器）将使用剪贴板寄存器 `"*` 替代，对应于 X 中的 `PRIMARY` 缓冲区。 

要更改默认寄存器，您可以 `:set clipboard=unnamedplus` 使用 `"+` 寄存器。`"+` 剪贴板寄存器对应于X中的 `CLIPBOARD` 缓冲区。应该注意，`clipboard` 选项可以设置为逗号分隔的值。如果您 `:set clipboard=unnamedplus,unnamed`，那么除了 `"+` 寄存器之外，yank 操作还会将被拉取的文本复制到 `"*` 寄存器(但是，delete, change 和 put 操作仍然只在 `"+` 寄存器上操作)。 

欲见更多信息，请参见 `:help 'clipboard'`。 可以为 `clipboard` 功能设置其他值。您可以使用 `:help clipboard-unnamed` 进入帮助主题，查找可为此功能设置的第一个有效值，然后查找所有其他有效值的帮助。 

**提示：**

  * 可以创建复制和粘贴操作的自定义快捷键。参见例如 [[2]](<https://superuser.com/a/189198>) 用于绑定 `ctrl + c`，`ctrl + v` 和 `ctrl + x`。
  * 当 vim 退出时，X 剪贴板会被刷新。要使 vim 选区在 X 剪贴板中持久化，您需要一个[剪贴板管理器](<https://wiki.archlinux.org/title/Clipboard#Managers>)。或者，您可以将 `autocmd VimLeave * call system("echo -n $'" . escape(getreg(), "'") . "' | xsel --input --clipboard")` 添加到你的 `.vimrc`（需要 [xsel](<https://archlinux.org/packages/?name=xsel>)包 包）。

###  语法高亮

启用语法高亮（Vim支持许多语言的语法高亮）： 
    
    :filetype plugin on
    :syntax on
    
###  自动换行显示

`wrap`默认是开启的，这会使Vim在一行文本的长度超过窗口宽度时，自动将放不下的文本显示到下一行。`wrap`只会影响文本的显示，文本本身不会被改变。 

自动换行显示一般在该行窗口能容纳下的最后一个字符发生，即使刚好是在一个单词的中间。更为智能的自动换行显示可以用`linebreak`来控制。当用`set linebreak`开启时，自动换行发生在字符串选项`breakat`中列出来的字符之后。默认情况下，`breakat`包含空格和一些标点符号（参考`:help breakat`）。 

被换行的字符一般在下一行的开头开始显示，没有任何相应的缩进。[breakindent](<https://retracile.net/wiki/VimBreakIndent>) 指示Vim在换行时将缩进考虑在内，因而新行将与原本要显示的文本有相同的缩进。`breakindent`行为可以用`breakindentopt`选项来调整，比如说在Python文件中，新行将在原本缩进的基础上再缩进4个空格（更多细节参考`:help breakindentopt`）： 
    
    autocmd FileType python set breakindentopt=shift:4
    
###  使用鼠标

Vim可以使用鼠标，但只在某些终端上起作用： 

  * 基于[xterm](<https://wiki.archlinux.org/title/Xterm>)/[urxvt](<../zh-cn/Rxvt-unicode.html> "Urxvt")的终端模拟器
  * 带有[gpm](<https://archlinux.org/packages/?name=gpm>)包的Linux控制台（更多细节请参阅[控制台鼠标支持](<../zh-cn/Console_mouse_support.html> "Console mouse support")）
  * [PuTTY](<https://wiki.archlinux.org/title/PuTTY>)。

要开启这个功能，将下面这行代码加入`~/.vimrc`中： 
    
    set mouse=a
    
`mouse=a` 选项在 `defaults.vim` 中已被设置。 

**注意：** 如果可以访问X服务器，复制/粘贴将使用 `"*` 寄存器，参见[剪贴板](<#%E5%89%AA%E8%B4%B4%E6%9D%BF>)。按住`shift key`键可以使用 xterm 处理鼠标按钮。

###  跨行移动光标

默认情况下，在行首按`←`或者在行尾按`→`不能将光标移动至上一行或下一行。 

如要改变默认行为，将`set whichwrap=b,s,<,>,[,]`加至你的`~/.vimrc`文件中。 

##  文件合并

Vim自带了一个文件差异编辑器（一个用来显示多个文件之间的差异还可以方便的将其合并的程序）。用 _vimdiff_ 来启动它——指定所需文件即可：`vimdiff _file1_ _file2_`。以下是 _vimdiff_ -specific命令的清单。 

行为 | 快捷键   
---|---  
下一差异 |  `]c`  
上一差异 |  `[c`  
差异导入 |  `do`  
差异导出 |  `dp`  
打开折叠 |  `zo`  
关闭折叠 |  `zc`  
重新扫描文件 |  `:diffupdate`  
窗口切换 |  `Ctrl+w+w`  
  
##  技巧和建议

###  显示行号

使用`:set number`来显示行号。默认显示绝对行号，可用`:set relativenumber`开启相对行号。当两种显示方式同时开启时，当前行显示绝对行号，其它行显示相对行号。 

使用`:_line number_` or `_line number_ gg`跳转到指定行号。跳转都记录在一个跳转列表中，更多细节参考`:h jump-motions`。 

###  拼写检查

Vim有拼写检查的功能，用下面的命令开启： 
    
    set spell
    
Vim默认只安装了英语字典（在 `/usr/share/vim/vim82/spell/`）。更多字典可以通过搜索 `vim-spell` 在[官方软件仓库](<../zh-cn/Official_repositories.html> "Official repositories")中找到。其他字典可以在[Vim的FTP archive](<http://ftp.vim.org/vim/runtime/spell/>)中找到。把下载的字典文件存入`~/.vim/spell/`中，并使用以下命令启用：`:setlocal spell spelllang=_en_us_`(将` _en_us_` 换成所需的字典的名称)。 

行为 | 快捷键   
---|---  
下一个拼写错误 |  `]s`  
上一个拼写错误 |  `[s`  
拼写纠正建议 |  `z=`  
拼写正确，添加到用户正确字典 |  `zg`  
在会话中当作正确拼写 |  `zG`  
拼写错误，添加到用户错误字典 |  `zw`  
在会话中当作正确拼写 |  `zW`  
重新进行拼写检查 |  `:spellr`  
  
**提示：**

  * 如果需要针对两种语言进行拼写检查（例如英语与德语），在`~/.vimrc`或`/etc/vimrc`中添加`set spelllang=_en,de_`并重启Vim即可。
  * 您可以通过使用FileType插件和用于文件类型检测的自定义规则，为任意文件类型（例如 _.txt_ ）启用拼写检查。 要对以 _.txt_ 结尾的任何文件启用拼写检查，请创建文件 `/usr/share/vim/vimfiles/ftdetect/plaintext.vim`，并将 `autocmd BufRead,BufNewFile *.txt set filetype=plaintext` 插入该文件。接下来，将 `autocmd FileType plaintext setlocal spell spelllang=_en_us_` 插入到`~/.vimrc` 或 `/etc/vimrc` 中，然后重新启动Vim。一定要编辑这一行（特别是 `*.txt`），以包括用于拼写检查的文件类型。

  * 如果想只对LaTeX（或TeX）文档起用拼写检查，在`~/.vimrc`或`/etc/vimrc`添加`autocmd FileType **tex** setlocal spell spelllang=_en_us_`，重启Vim即可。至于非英语语言，替换上述语句中的`en_us`为相应语言代码即可。

###  保存运行状态

通常，退出 `vim` 会丢弃所有不重要的信息，如打开的文件、命令行历史记录、删除的文本等。可以通过以下方式配置保存这些信息。 

####  viminfo 文件

`viminfo` 文件可用于存储命令行历史、查找字符串历史、输入行历史、寄存器内容、文件标记、文件内的位置标记、最后的查找/替换模式（在会话中使用 `n` 和 `&` 的查找模式）、缓冲区列表以及您可能定义的任何全局变量。要使 `viminfo` 模式可用，您安装的 `vim` 版本必须使用 `+viminfo` 功能进行编译。 

通过在 `~/.vimrc` 文件中添加特定内容可以配置保存在 `viminfo` 文件中的内容，以下是一个示例： 
    
    set viminfo='10,<100,:100,%,n~/.vim/.viminfo
    
其中每个参数前面都有一个标识符： 
    
    'q  : q 是记住的编辑过的文件数
    <m  : m 为每个寄存器保存的行数
    :p  : p 是记住的历史命令行数
    %   : 保存和恢复缓冲区列表
    n...: viminfo 文件的完整路径名称（注意，这是一个字面上的 "_n_ "）
    
请参阅官方的 [viminfo 文档](<https://vimdoc.sourceforge.net/htmldoc/options.html#'viminfo'>)，了解当前的 `viminfo` 文件当会话信息更新时如何修改它，比如从当前会话中的几个缓冲区中退出。 

####  会话文件

会话文件可用于保存随时间变化的任意数量的特定会话的状态。一个不同的会话文件可以用于您感兴趣的每个会话或项目。要使该模式可用，您安装的`vim`版本必须使用`+mksession`功能进行编译。 

在会话中，`:mksession[!] [_my_session_name.vim_]` 将 vim 脚本写入当前目录中的 `_my_session_name.vim_`，如果 _不_ 提供文件名，则默认为 `Session.vim`。可选的 `!` 将删除具有相同名称和路径的已经存在的会话文件。 

从终端启动 _vim_ 时，可以恢复 `vim` 会话： 
    
    $ vim -S [_my_session_name.vim_]
    
或者在已经打开的会话缓冲区中运行 vim 命令： 
    
    :source _my_session_name.vim_
    
[vim文档](<https://vimdoc.sourceforge.net/htmldoc/usr_21.html#21.4>)中详细介绍了保存的内容以及会话文件选项的其他细节。此处有注释过的[示例](<https://vim.wikia.com/wiki/Go_away_and_come_back>)。 

####  记录光标位置

Vim可以记录上次打开某一文件时的光标位置，并在下次打开同一文件时将光标移动到该位置。要开启该功能，在配置文件`~/.vimrc`中加入以下内容： 
    
    augroup resCur
      autocmd!
      autocmd BufReadPost * call setpos(".", getpos("'\""))
    augroup END
    
参见 Vim wiki 上的 [Restore cursor to file position in previous editing session](<https://vim.wikia.com/wiki/Restore_cursor_to_file_position_in_previous_editing_session>)

###  用 vim 替代 vi

创建一个[别名](<../zh-cn/Bash.html#%E5%88%AB%E5%90%8D> "Alias")，如下： 
    
    alias vi=vim

或者，如果你想输入`sudo vi`而得到`vim`，安装[vi-vim-symlink](<https://aur.archlinux.org/packages/vi-vim-symlink/>)AUR，它将移除`vi`并用一个符号链接`vim`代替。您还可以自己创建这个符号链接，并将其放置在 path 中比 `/usr/bin` 更高的位置，以使其更为优先。 

###  DOS/Windows回车问题

打开MS-DOS或Windows下创建的文本文件时，经常会在每行行末出现一个`^M`。这是因为Linux使用Unix风格的换行，用一个换行符（LF）来表示一行的结束，但在Windows、MS-DOS中使用一个回车符（CR）接一个换行符（LF）来表示，因而回车符就显示为`^M`。 

可使用下面的命令删除文件中的回车符： 
    
    :%s/^M//g
    
注意，`^`代表控制字符。输入`^M`的方法是按下`Ctrl+v,Ctrl+m`。 

另一个解决方法是，安装 [dos2unix](<https://archlinux.org/packages/?name=dos2unix>)包，然后执行 `dos2unix <文件名>`。 

**注意：** 另一个简单的方法是更改 `fileformat` 设置。`set ff=unix` 以转化DOS/Windows行尾为Unix行尾。要做到相反，只要 `set ff=dos`，就可以将Unix行尾转换成DOS/Windows行尾。

###  gVim窗口底部的空格

如果[窗口管理器](<../zh-cn/Window_manager.html> "Window manager")设置为忽略窗口大小提示，gVim会将非功能区域填充为GTK主题背景色。 

解决方案是调整gVim在窗口底部保留的空间大小。将下面的代码加入 `~/.vimrc`中： 
    
    set guiheadroom=0
    
**注意：** 如果将其设为0，将无法看到底部的水平滚动条。

###  Vim 作为 pager

如果使用脚本，那么 Vim 可以用作 [terminal pager](<../zh-cn/Terminal_pager.html> "Terminal pager")，这样您就可以获得各种Vim功能，如颜色方案。 

Vim 附带了 `/usr/share/vim/vim90/macros/less.sh` 脚本，您可以为其创建[别名](<../zh-cn/Bash.html#%E5%88%AB%E5%90%8D> "Alias")。注意，该脚本不支持 [less(1) § OPTIONS](<https://man.archlinux.org/man/less.1#OPTIONS>) 中提到的任何命令行标志。 

另外，还有 [vimpager](<https://archlinux.org/packages/?name=vimpager>)包 Vim 脚本。要更改默认 pager，请[导出](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量") `PAGER` 环境变量。注意，并非所有命令行标志都受支持；[GitHub上](<https://github.com/rkitover/vimpager#command-line-options>)提供了支持的标志列表。 

###  高亮搜索结果

为了突出显示在搜索中匹配的第一个字符串，请在 `~/.vimrc` 中添加以下行： 
    
    set incsearch
    
为了突出显示在搜索中匹配的所有字符串，在 `~/.vimrc` 中添加以下行： 
    
    set hlsearch
    
**注意：**

  * 设置 `hlsearch` 将突出显示所有匹配项，直到进行更多搜索。这种行为可能是不被希望的，因此要在下次搜索之前暂时禁用高亮显示，请运行 `:nohlsearch`。如果您发现自己经常运行此命令，请考虑将其绑定到按键。
  * 当在其他命令（如 `s` 或 `g`）中匹配正则表达式时，也会观察到这种行为。

##  插件

向Vim添加插件可以提高您的效率。 插件可以改变Vim的界面，添加新命令，代码完成支持，使用Vim集成其他程序和实用程序，添加对其他语言的支持等等。 

**提示：** 有关常用插件的列表，请参阅 [Vim Awesome](<https://vimawesome.com/>)。

###  安装

####  使用内置包管理器

Vim 8增加了原生加载第三方插件的可能性。可以通过在 `~/.vim/pack` 中存储第三方软件包来使用此功能。这个文件夹的结构与典型的插件管理器的结构略有不同，典型的插件管理器通常每个插件只有一个目录。下面是一个典型的安装过程和目录结构(以 [Tim Pope 的 vim-surround 插件](<https://github.com/tpope/vim-surround>)为例) : 
    
    $ mkdir -p ~/.vim/pack/tpope/start
    
需要注意的是，`~/.vim/pack/tpope` 是一个 _包目录_ ，它在 [Vim文档](<https://vimhelp.org/repeat.txt.html#packages>)中被宽松定义为包含一个或多个插件的目录。插件存储库不应下载到此目录。包目录的名称也是任意的。您可以选择将所有插件保存在一个包目录中，或者如我们的示例中所示，使用作者的 GitHub 名称 `tpope`。 

包目录可以包含以下子文件夹: 

  * `start` \- 这个子文件夹中的插件将在 Vim 启动时自动加载。这是最常用的位置。
  * `opt` \- 这个子文件夹中的插件可以按需加载，方法是在 Vim 中发出 `:packadd` 命令。

现在切换到 `start` 文件夹并检出插件存储库： 
    
    $ cd ~/.vim/pack/tpope/start
    $ git clone <https://tpope.io/vim/surround.git>
    
这会创建一个额外的子文件夹 `~/.vim/pack/tpope/start/surround`，插件文件就放在这个子文件夹中。 

接下来，如果插件包含帮助文件，请更新帮助索引： 
    
    $ vim -u NONE -c "helptags surround/doc" -c q
    
启动 Vim 时，插件将自动加载。除了特定于插件的选项外，不需要对 `~/.vimrc` 进行任何更改。 

####  使用插件管理器

插件管理器允许以类似的方式安装和管理插件，而与在何种平台上运行 Vim 无关。它本身是一个插件，其功能是作为其他 Vim 插件包管理器。 

  * [Vundle](<https://github.com/gmarik/Vundle.vim>) 是现在最流行的 Vim 插件管理器，从 [vundle](<https://aur.archlinux.org/packages/vundle/>)AUR 或 [vundle-git](<https://aur.archlinux.org/packages/vundle-git/>)AUR 获取。
  * [Vim-plug](<https://github.com/junegunn/vim-plug>) 是一个极简的 Vim 插件管理器，有许多的特性，比如按需插件加载和并行升级，从 [vim-plug](<https://aur.archlinux.org/packages/vim-plug/>)AUR 或 [vim-plug-git](<https://aur.archlinux.org/packages/vim-plug-git/>)AUR 获取。
  * [pathogen.vim](<https://github.com/tpope/vim-pathogen>) 是一个简单的用于管理 Vim 的 runtimepath 的插件，从 [vim-pathogen](<https://aur.archlinux.org/packages/vim-pathogen/>)AUR 或 [vim-pathogen-git](<https://aur.archlinux.org/packages/vim-pathogen-git/>)AUR 获取。
  * [Dein.vim](<https://github.com/Shougo/dein.vim>) 是一个替代 [NeoBundle](<https://github.com/Shougo/neobundle.vim>) 的插件管理器，从 [vim-dein](<https://aur.archlinux.org/packages/vim-dein/>)AUR 或 [vim-dein-git](<https://aur.archlinux.org/packages/vim-dein-git/>)AUR 获取。

####  使用 Arch 软件库

[vim-plugins](<https://archlinux.org/groups/x86_64/vim-plugins/>)包组包组下有许多插件。 使用`pacman -Sg vim-plugins`来列出可用的插件，然后你可用 pacman [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")。 

###  著名的插件

#### cscope

[Cscope](<https://cscope.sourceforge.net/>)是用于浏览项目的工具。 通过导航到字/符号/函数并调用 cscope（通常使用快捷键），它可以找到：调用函数的函数，函数定义等等。 

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [cscope](<https://archlinux.org/packages/?name=cscope>)包 包。 

将 cscope 默认文件复制到 Vim 将自动读取的位置: 
    
    mkdir -p ~/.vim/plugin
    wget -P ~/.vim/plugin <https://cscope.sourceforge.net/cscope_maps.vim> 
    
**注意：** 在 Vim 的 7.x 版本中，你可能需要在 `~/.vim/plugin/cscope_maps.vim` 中取消下列行的注释来启用 cscope 快捷键： 
    
    set timeoutlen=4000
    set ttimeout

创建一个文件，该文件包含了你希望 cscope 索引的文件的清单（cscope 可以操作很多语言，下面的例子用于寻找 C/C++ 中的 _.c_ 、 _.cpp_ 和 _.h_ 文件）： 
    
    cd _/path/to/projectfolder/_
    find . -type f -print | grep -E '\.(c(pp)?|h)$' > cscope.files
    
创建 cscope 将读取的数据文件： 
    
    cscope -bq
    
**注意：** 必须从当前路径浏览工程文件，也可以设置 `$CSCOPE_DB` 变量指向 `cscope.out` 文件，并导出。

默认快捷键： 
    
     Ctrl-\ and
          c: 查找调用指定函数的函数
          d: 查找指定函数调用的函数
          e: 查找指定 egrep 模式
          f: 查找指定文件
          g: 查找指定定义
          i: 查找指定文件 #including 的文件
          s: 查找指定 C 符号
          t: 查找指定的字符串
    
可随意改变这些快捷键。 
    
    #Maps ctrl-c to find functions calling the function
    nnoremap <C-c> :cs find c <C-R>=expand("<cword>")<CR><CR>
    
#### Taglist

[Taglist](<http://vim-taglist.sourceforge.net/>) 提供源码文件的结构概览，使你能更高效的浏览不同语言的源文件。 

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [vim-taglist](<https://aur.archlinux.org/packages/vim-taglist/>)AUR 包。 

将下列设置添入文件`~/.vimrc`: 
    
    let Tlist_Compact_Format = 1
    let Tlist_GainFocus_On_ToggleOpen = 1
    let Tlist_Close_On_Select = 1
    nnoremap <C-l> :TlistToggle<CR>
    
##  常见问题

###  gVim运行缓慢

GTK 3 GUI 下 vim 可能比 GTK 2 下运行缓慢（参阅 [FS#51366](<https://bugs.archlinux.org/task/51366>)）。可安装[gvim-gtk2](<https://aur.archlinux.org/packages/gvim-gtk2/>)AUR来避免该问题。 

##  参阅

###  官方资源

  * [Vim主页](<https://www.vim.org/>)
  * [Vim文档](<https://vimdoc.sourceforge.net/>)
  * [Vim Wiki](<https://vim.wikia.com>)
  * [Vim脚本](<https://www.vim.org/scripts/>)

###  教程

  * [vim 入门教程](<https://www.danielmiessler.com/study/vim/>)
  * [中文版《A Byte of Vim》](<https://web.archive.org/web/20140322091511/http://swaroopch.com/notes/vim_zh-cn/>)
  * [vi参考指南](<https://web.archive.org/web/20140822135551/http://usalug.com/vi.html>)
  * [vi-Vim 图解教程](<http://www.viemu.com/a_vi_vim_graphical_cheat_sheet_tutorial.html>)
  * [Vim 简介与教程](<https://archive.today/2012.12.20-221858/http://blog.interlinked.org/tutorials/vim_tutorial.html>)
  * [Open Vim](<https://www.openvim.com/>) \- Vim 学习工具集合
  * [Vim 渐进式教程](<https://yannesposito.com/Scratch/en/blog/Learn-Vim-Progressively/>)
  * [学习 Vim 在 2014](<https://benmccormick.org/learning-vim-in-2014/>)
  * [有效率进行文本编辑的七个习惯](<https://www.moolenaar.net/habits.html>)
  * [基本 Vim 技巧](<https://bencrowder.net/files/vim-fu/>)

####  视频

  * [Vimcasts](<http://vimcasts.org/>) \- _.ogg_ 格式的视频教程。
  * [Vim Tutorial Videos](<http://derekwyatt.org/vim/tutorials/>) \- 从入门到精通，各种视频教程

####  速查表

  * <https://devhints.io/vim>
  * <https://vim.rtorr.com/> \- 一个移动友好的 Vim 速查表 - [源代码](<https://github.com/rtorr/vim-cheat-sheet>)

####  游戏

  * [Vim Adventures](<https://vim-adventures.com/>)
  * [VimGolf](<https://vimgolf.com/>)

###  配置范例

  * [nion's](<https://web.archive.org/web/20131020125020/http://nion.modprobe.de/setup/vimrc>)
  * [来自 Amir Salihefendic 的一个详细配置](<https://github.com/amix/vimrc>)
  * [Bart Trojanowski](<https://web.archive.org/web/20131004071740/http://www.jukie.net/~bart/conf/vimrc>)
  * [Steve Francia 的 Vim 发行版](<https://github.com/spf13/spf13-vim>)
  * [Vim Awesome](<https://vimawesome.com/>) \- Vim 插件
  * [W4RH4WK 的 Vim 配置文件](<https://github.com/W4RH4WK/dotVim>)
  * [来自 askapache 的快速 vimrc/色彩方案](<https://www.askapache.com/linux/fast-vimrc/>)
  * [基础 vimrc](<https://gist.github.com/anonymous/c966c0757f62b451bffa>)
  * [Usevim](<https://www.usevim.com/>)

####  色彩方案

  * [Vivify](<http://bytefluent.com/vivify/>)
  * [Vim 色彩方案定制](<https://linuxtidbits.wordpress.com/2014/10/14/vim-customize-installed-colorschemes/>)
