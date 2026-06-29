**翻译状态：**

  * 本文（或部分内容）译自 [Kitty](<https://wiki.archlinux.org/title/Kitty> "arch:Kitty")，最近一次同步于 2025-01-22，若英文版本有所[更改](<https://wiki.archlinux.org/title/Kitty?diff=0&oldid=823413>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Kitty_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[kitty](<https://sw.kovidgoyal.net/kitty/index.html>) 是一个基于 OpenGL 的可编程终端模拟器，具有真彩色，连字支持，键盘输入和图像渲染的协议扩展。它还提供了类似于 [GNU Screen](<../zh-cn/GNU_Screen.html> "GNU Screen") 或 [tmux](<../zh-cn/Tmux.html> "Tmux") 的平铺功能。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [kitty](<https://archlinux.org/packages/?name=kitty>)包；若要获取开发版本，请安装 [kitty-git](<https://aur.archlinux.org/packages/kitty-git/>)AUR。 

##  用法

可以通过各种 `Ctrl+Shift` 快捷键来创建新的选项卡和窗口并调整其大小。布局可通过 `Ctrl+Shift+l` 切换，并可以保存/恢复。 

_全键盘模式_ 可区分 `Ctrl+i` 和 `Tab` 等歧义键。此外，新的文本效果（例如，波浪下划线）也可用于支持它的应用程序。 

### Kitten

kitty 有一个用于创建子程序的框架，称为 [kitten（小猫）](<https://sw.kovidgoyal.net/kitty/kittens_intro/>)。所有 kitten 命令均以 `kitty +kitten` 为前缀，很方便作为 shell 别名。 

#### icat

这个 kitten 基于 [kitty 图形协议](<https://sw.kovidgoyal.net/kitty/graphics-protocol/>)。其依赖 [ImageMagick](<../zh-cn/ImageMagick.html> "ImageMagick")。要在终端内显示图像： 
    
    $ kitty +kitten icat image.jpg
    
其也可以在终端内显示 gif 动图。除了图片文件，您也可以传递目录或图片 URL。这也可以在远程服务器上通过 ssh 显示图片。一些应用程序像 [ranger](<../zh-cn/Ranger.html> "Ranger") 和 [neofetch](<https://aur.archlinux.org/packages/neofetch/>)AUR 使用该协议在终端内显示图片。关于更多信息，请参阅[官方文档](<https://sw.kovidgoyal.net/kitty/kittens/icat/>)。 

#### diff

这个 kitten 需要 [git](<../zh-cn/Git.html> "Git") 或 [diffutils](<https://archlinux.org/packages/?name=diffutils>)包 被安装。此外，您也可以安装 [python-pygments](<https://archlinux.org/packages/?name=python-pygments>)包 来获得语法高亮效果。要显示两个文件的差异： 
    
    $ kitty +kitten diff file1 file2
    
这个 kitten 显示了图形或文本的差异，也可以通过 ssh 使用，您可以用一个目录代替文件来显示递归差异。关于更多信息，参阅[官方文档](<https://sw.kovidgoyal.net/kitty/kittens/diff/>)。 

#### clipboard

这个 kitten 用于读写系统剪贴板，可以跨 ssh 使用。如果要将标准输入复制到剪贴板： 
    
     $ echo "Hello" | kitty +kitten clipboard
    
将当前剪贴板内容输出到标准输出： 
    
     $ kitty +kitten clipboard --get-clipboard
    
默认情况下，这条命令会提示请求权限，要禁用该提示，请在配置文件中编辑 [clipboard_control](<https://sw.kovidgoyal.net/kitty/conf/#opt-kitty.clipboard_control>) 选项： 
    
    ~/.config/kitty/kitty.conf
    
    clipboard_control write-clipboard read-clipboard

关于更多信息，请参阅[官方文档](<https://sw.kovidgoyal.net/kitty/kittens/clipboard/>)。 

##  配置

kitty 在 `~/.config/kitty/kitty.conf` 中存储配置，默认配置位于 `/usr/share/doc/kitty/kitty.conf`。可以调整字体，颜色，光标和回滚行为。您可以在[官方文档](<https://sw.kovidgoyal.net/kitty/conf.html>)或 [kitty.conf(5)](<https://man.archlinux.org/man/kitty.conf.5>) 中查看所有可用的选项。 

**注意：** 若您正在使用 vim 编辑默认配置文件，所有的节开始都会被折叠，每个节默认都可以用 `zo` 展开。

**提示：**

  * 位于 `/usr/share/doc/kitty/kitty.conf` 的默认配置文件自带每个选项的说明。
  * 官方文档在本地具有副本，位于 `/usr/share/doc/kitty/html/index.html`。

##  提示和技巧

###  输入法兼容

Kitty 默认情况下关闭了 [IBus](<../zh-cn/IBus.html> "IBus") 框架。 

请在[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")中启用： 
    
    GLFW_IM_MODULE=ibus
    
由于兼容问题，该环境变量也可解决 kitty 对 [fcitx5](<../zh-cn/Fcitx_5.html> "Fcitx5") 的兼容问题。 

###  单实例模式

这类似于守护进程模式，当以 `--single-instance` 或 `-1` 选项启动 kitty 时，仅会运行一个 kitty 实例，随后以相同选项启动 kitty 时会创建已经存在的 kitty 实例的新窗口。这可以降低内存占用，因为共享了 GPU 缓存，而且会减少启动时间。您可以用 `--instance group _name_` 选项创建多组 kitty 实例。参阅 [kitty(1) § single](<https://man.archlinux.org/man/kitty.1#single>) 以获取更多信息。 

##  疑难解答

###  SSH 连接故障

当 kitty 用于 ssh 连接到没有其 terminfo 的远程主机时，可能会出现各种问题。解决方案通常是复制 terminfo。Kitty 有一个 ssh 小工具来自动化这一过程。 
    
    $ kitty +kitten ssh user@host
    
您可以将其设置为 ssh 的别名。实现这一点的一种方法是检测用户是否在使用 Kitty，如果是，则为 ssh 命令设置别名。为此，您需要将以下行附加到您的 `~/.bashrc` 或`~/.zshrc` 文件中： 
    
    [ "$TERM" = "xterm-kitty" ] && alias ssh="kitty +kitten ssh"
    
###  背景色在 vim 中消失

在 [vim](<../zh-cn/Vim.html> "Vim") 中使用带背景色的配色方案后，滚动时背景色可能会消失或闪烁。欲修复，请确保 `TERM` 环境变量依然被设为 `xterm-kitty`，然后添加以下行到您的 `.vimrc` 文件： 
    
    ~/.vimrc
    
    let &t_ut=''

相关 bug 报告：[Github issue #108](<https://github.com/kovidgoyal/kitty/issues/108>)，[kitty FAQ](<https://sw.kovidgoyal.net/kitty/faq/#using-a-color-theme-with-a-background-color-does-not-work-well-in-vim>)。 

###  无法识别位图字体

因为 kitty 的基本特性是以任意大小显示字体，而位图字体不适合缩放，故 kitty 不支持位图字体，参阅 [Github issue #97](<https://github.com/kovidgoyal/kitty/issues/97>)。 

##  参见

  * [官方网站](<https://sw.kovidgoyal.net/kitty/>)
  * [GitHub 仓库](<https://github.com/kovidgoyal/kitty>)
