**翻译状态：**

  * 本文（或部分内容）译自 [Help:Reading](<https://wiki.archlinux.org/title/Help:Reading> "arch:Help:Reading")，最近一次同步于 2026-02-17，若英文版本有所[更改](<https://wiki.archlinux.org/title/Help:Reading?diff=0&oldid=866018>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Help:Reading_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Help:浏览](<../zh-cn/Help:%E6%9F%A5%E9%98%85.html> "Help:浏览")
  * [Help:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")

由于对于 Arch Linux（或 GNU/Linux）的新用户来说，绝大多数 ArchWiki 包含的指示可能需要澄清，因此本文通过解释一些基本操作，以避免理解文章时的困惑，并阻止内容本身的重复。 

##  组织结构

ArchWiki 上的页面大多不是要对某个话题进行面面俱到的描述；它们遵守 [DRY](<http://c2.com/cgi/wiki?DontRepeatYourself>) 的原则，假定用户会查阅相关资料以便把不懂的部分弄懂。页面中会尽可能地以特殊格式指出相关资料，请参阅[#格式](<#%E6%A0%BC%E5%BC%8F>)。 

由于这样的组织结构，要看懂一个页面，可能需要查阅数个相关资料。特别需要注意的是，Arch（或 GNU/Linux）的新用户为了解决一个简单的问题很可能会阅读许多页面。在向其他用户寻求帮助之前，一定要阅读相关资料。 

##  格式

  * 链接到当前文章中的某一部分：[#组织结构](<#%E7%BB%84%E7%BB%87%E7%BB%93%E6%9E%84>)
  * 链接到[另一篇 ArchWiki 文章](<../zh-cn/%E9%A6%96%E9%A1%B5.html> "首页")
  * 链接到[外部网页](<https://en.wikipedia.org/wiki/> "wikipedia:")
  * 链接到[手册页](<../zh-cn/Man_%E6%89%8B%E5%86%8C.html> "手册页")：[intro(1)](<https://man.archlinux.org/man/intro.1>)
  * 只能离线阅读的[手册页](<../zh-cn/Man_%E6%89%8B%E5%86%8C.html> "手册页")：foo(1)
  * 链接到[官方软件仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方软件仓库")中的包：[foobar](<https://archlinux.org/packages/?name=foobar>)包
  * 链接到 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "Arch 用户软件仓库") 中的包：[foobar](<https://aur.archlinux.org/packages/foobar/>)AUR

##  root 用户、一般用户或另一用户

有些命令是这样的: 
    
    # mkinitcpio -p linux
    
另外一些命令是这样的： 
    
    $ makepkg -s
    
井号(`#`)表示命令要以 root 权限执行，而美元符号(`$`)表示命令用一般用户权限执行。 

**注意：** 用 `sudo -i` 可以进入 root 终端，在普通终端中使用`sudo _command_`也能让` _command_`以 root 权限执行，但是这个方式不支持 [重定向](<https://en.wikipedia.org/wiki/Redirection_\(computing\)> "wikipedia:Redirection \(computing\)") 和 [替代](<https://en.wikipedia.org/wiki/Command_substitution> "wikipedia:Command substitution")。详情参阅[sudo#Login shell](<../zh-cn/Sudo.html#Login_shell> "Sudo")。

当命令需要以特定用户身份运行时，命令前面会加上带方括号的用户名，例如： 
    
    [postgres]$ initdb -D /var/lib/postgres/data
    
这表示你需要使用[提权](<../zh-cn/List_of_applications/Security.html#%E6%8F%90%E6%9D%83> "List of applications/Security")工具，如[sudo](<../zh-cn/Sudo.html> "Sudo")： 
    
    $ sudo -u postgres initdb -D /var/lib/postgres/data
    
注意有时候 # 表示文件中的注释： 
    
    # This alias makes ls colorize the listing
    alias ls='ls --color=auto'
    
在这个例子中，上下文表明这不是命令，而是需要加入到文件的一部分。在这种情况下，井号表示一个“注释”。注释是解释性的文字，它不会被执行。[Bash](<../zh-cn/Bash.html> "Bash") 脚本的注释符号和 root 的命令提示符相同。 

此外，通常包含大写字母的文字都是注释，而 Unix 命令通常是简短的缩写（例如，“Copy”被缩写成“cp”）。 

当然，大部分文章都会指明这一点： 

向 `~/path/to/file` 添加： 
    
    # This alias makes ls colorize the listing
    alias ls='ls --color=auto'
    
##  添加、创建、编辑文件

当提到“添加”（append to、add to）、“创建”（create）、“编辑”（edit）一个或几个文件，这就表示你应该用以下的某种方法。 

推荐使用[文本编辑器](<../zh-cn/Text_editor.html> "Text editor")来创建或修改多行的文件，例如用 [nano](<../zh-cn/Nano.html> "Nano") 命令来编辑文件 `/etc/bash.bashrc`： 
    
    # nano /etc/bash.bashrc
    
**注意：** 文本文件必须以换行符结束，因为[一行](<https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap03.html#tag_03_185>)是由换行符终止的。大多数文本编辑器会默认在文件末尾插入结尾换行符。

要创建包含简短文本的文件或者覆盖已有的文件，[输出重定向](<https://www.gnu.org/software/bash/manual/html_node/Redirections.html>)是最简单的。下面的命令演示了如何用文本 `myhostname` 创建或覆盖 `/etc/hostname`。 
    
    # echo myhostname > /etc/hostname
    
输出重定向也可以用来向一个文件追加（append）文本。下面的命令演示了如何向 `/etc/pacman.conf` 追加文本 `[custom-repo]`。 
    
    # echo "[custom-repo]" >> /etc/pacman.conf
    
要创建[目录](<https://en.wikipedia.org/wiki/Directory_\(computing\)> "w:Directory \(computing\)")，用 [mkdir](<../zh-cn/%E6%A0%B8%E5%BF%83%E5%B7%A5%E5%85%B7.html#%E5%9F%BA%E7%A1%80> "核心工具") 命令： 
    
    # mkdir /mnt/boot
    
###  添加可执行权限

在创建文件之后，如果这是一个要运行的脚本（手动运行或被其他程序调用），就需要把他设为“可执行”： 
    
    $ chmod +x _script_
    
参阅 [chmod](<../zh-cn/%E6%96%87%E4%BB%B6%E6%9D%83%E9%99%90%E4%B8%8E%E5%B1%9E%E6%80%A7.html#%E4%BF%AE%E6%94%B9%E6%9D%83%E9%99%90> "Chmod")。[文件管理器](<../zh-cn/File_manager.html> "File manager")等应用程序可能会提供一个图形界面完成相同的事情。 

## Source

有些程序，特别是[命令行解释器](<../zh-cn/%E5%91%BD%E4%BB%A4%E8%A1%8C%E8%A7%A3%E9%87%8A%E5%99%A8.html> "命令行解释器")（shell），使用脚本来进行配置：修改配置文件之后，需要使用“source”命令来应用这些修改。以 [bash](<../zh-cn/Bash.html> "Bash") 为例，执行以下命令（也可以把 `source` 换成 `.`）： 
    
    $ source ~/.bashrc
    
当 ArchWiki 建议修改某些配置文件时，它一般不会明确提醒你“source”这个文件，只有某些情况下会给出到本节的链接。 

##  安装软件包

**提示：****“安装”** 重定向至此。关于“安装 Arch Linux 系统”的内容，参见[安装指南](<../zh-cn/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97.html> "安装指南")。

绝大部分文章仅是给出软件包的名字，不会列出详细的软件包安装命令。 

下面介绍一下通用的软件包安装方式。 

###  官方软件包

如果软件包位于[官方软件仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方软件仓库")，在 Wiki 内一般会这么表述要求安装软件包： 

    Install the [foobar](<https://archlinux.org/packages/?name=foobar>)包 package.
    安装 [foobar](<https://archlinux.org/packages/?name=foobar>)包 软件包。

这意味着需要执行： 
    
    # pacman -S foobar
    
[pacman](<../zh-cn/Pacman.html> "Pacman") 和 [pacman(8)](<https://man.archlinux.org/man/pacman.8>) 包含了 Arch 软件包管理的详细内容。 

###  Arch 用户仓库(AUR)

如果软件包来自 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93_\(AUR\).html> "Arch 用户软件仓库 \(AUR\)")，你会看到下面内容： 

    Install the [foobar](<https://aur.archlinux.org/packages/foobar/>)AUR package.
    安装[foobar](<https://aur.archlinux.org/packages/foobar/>)AUR软件包。

这意味这您需要打开[foobar](<https://aur.archlinux.org/packages/foobar/>)AUR 链接，下载 PKGBUILD，解压，**验证内容** ，然后在文件目录执行： 
    
    $ makepkg -sri
    
**注意：** 从 AUR 或[Arch 构建系统](<../zh-cn/Arch_%E6%9E%84%E5%BB%BA%E7%B3%BB%E7%BB%9F.html> "ABS")构建软件包需要安装 [base-devel](<https://archlinux.org/packages/?name=base-devel>)包 元包。

[Arch 用户软件仓库 (AUR)](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93_\(AUR\).html> "Arch 用户软件仓库 \(AUR\)") 包含了 AUR 软件包的详细信息。 

###  [archlinuxcn] 仓库

如果软件包来自 [[archlinuxcn] 仓库](<../zh-cn/%E9%9D%9E%E5%AE%98%E6%96%B9%E7%94%A8%E6%88%B7%E4%BB%93%E5%BA%93.html#archlinuxcn> "非官方用户仓库")，你会看到下面的样子： 

    安装 [archlinuxcn-keyring](<https://github.com/archlinuxcn/repo/tree/master/archlinuxcn/archlinuxcn-keyring>)[CNRepo](<../zh-cn/Arch_Linux_%E4%B8%AD%E6%96%87%E7%A4%BE%E5%8C%BA%E4%BB%93%E5%BA%93.html> "Arch Linux 中文社区仓库") 软件包。

这意味着你需要添加 [archlinuxcn] 仓库之后再使用 [pacman](<../zh-cn/Pacman.html> "Pacman") 进行安装。 

##  控制 systemd 单元

绝大部分文章仅仅要求你“启动”（start）、“启用”（enable）、“停止”（stop）、“禁用”（disable）、“重启”（restart）systemd 单元（例如：服务），不会列出详细的命令。你会看见类似这样的说明： 

     [启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") `example.service`.

这意味着你需要执行 
    
    # systemctl start example.service
    
注意 daemon-reload 命令并不完全遵循这种模式，它的调用不带参数。 

[systemd#使用单元](<../zh-cn/Systemd.html#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83> "Systemd") 章节包含可用操作的结构化列表（如启动 (`start`) 、启用 (`enable`) 、启用并启动 (`enable --now`) 等），以及相应的 systemctl 命令。 

##  全局配置和用户配置

请记住，GNU/Linux 有两种类型的配置。“全局”配置影响所有用户。全局配置文件一般位于 `/etc` 目录，修改它们需要 root 权限。例如，要修改所有用户的 Bash 设置，修改 `/etc/bash.bashrc` 文件。 

“用户”配置仅影响一个用户。文件名以 `.` 开头的文件（dotfiles，例如 `~/**.** bashrc`）是用户配置文件。每个用户都可以定义他们自己的设置（别名、函数、命令提示符等）而不影响其他用户。 

**注意：**`~/` 和 `$HOME` 是用户主目录的简写，一般是 `/home/_用户名_ /`。

###  Shell 通用配置文件

Bash 和其他与 Bourne shell 兼容的 shell（如 [Zsh](<../zh-cn/Zsh.html> "Zsh")），会根据是 “登录 shell” 还是 “交互式 shell” 来执行相应的配置文件。参阅 [Bash#配置文件](<../zh-cn/Bash.html#%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6> "Bash")和 [Zsh#启动/关闭文件](<../zh-cn/Zsh.html#%E5%90%AF%E5%8A%A8/%E5%85%B3%E9%97%AD%E6%96%87%E4%BB%B6> "Zsh")。 

##  示例代码中的伪变量

一些代码块包含“伪变量”，顾名思义，这不是代码中使用的真正的变量。它们只是代码中的占位符，需要在执行或解释**之前** 根据特定的系统配置进行手动替换。[Bash](<../zh-cn/Bash.html> "Bash") 和 [Zsh](<../zh-cn/Zsh.html> "Zsh") 这类终端提供 [Tab 补全](<https://en.wikipedia.org/wiki/Command-line_completion> "w:Command-line completion")功能以补全 `systemctl` 之类的命令。 

根据 [Help:Style/Formatting and punctuation](</wzh/index.php?title=Help:Style/Formatting_and_punctuation&action=edit&redlink=1> "Help:Style/Formatting and punctuation（页面不存在）")，伪变量使用斜体。例如： 

  * 对 `ip link` 命令输出的网卡名称，[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") `dhcpcd@_interface_name_.service`。

在这里，伪变量 `_interface_name_` 是一个 systemd 模板单元的占位符。所有的 systemd 模板单元（带有 `@` 标记）都需要特定系统的名称作为参数。参阅 [Systemd#使用单元](<../zh-cn/Systemd.html#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83> "Systemd")。 

  * 以 root 运行命令 `dd if=_data_source_ of=/dev/sd _X_ bs=_sector_size_ count=_sector_number_ seek=_partitions_start_sector_` 用特定参数来清空一个分区。

在这里，伪变量表示该参数需要被替换。具体怎么替换在[安全擦除磁盘#通过计算块数手动擦除](</wzh/index.php?title=%E5%AE%89%E5%85%A8%E6%93%A6%E9%99%A4%E7%A3%81%E7%9B%98&action=edit&redlink=1> "安全擦除磁盘（页面不存在）")（英语：[Securely wipe disk#Calculate blocks to wipe manually](<https://wiki.archlinux.org/title/Securely_wipe_disk#Calculate_blocks_to_wipe_manually> "en:Securely wipe disk")）有详细描述。 

**警告：** 不要执行上面的 `dd` 命令，这个命令会清除硬盘上的相应扇区。——译者注

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** Mention other examples, ideally from other device categories (e.g. storage), with links to background articles. The examples are meant to avoid duplicating existing explanations in other articles. (在 [Help talk:阅读](<../zh-cn/Help_talk:%E9%98%85%E8%AF%BB.html>) 中讨论)

在配置文件中，如果直接将带伪变量的代码粘贴进去，可能会导致程序出错。 

###  省略

省略号（`...`）一般不是文件内容或命令输出的一部分，它们代表和主题关系不大的文字。 

例如，`HOOKS=(... encrypt ... filesystems ...)` 或者： 
    
    /etc/X11/xorg.conf.d/50-synaptics.conf
    
    Section "InputClass"
        ...
        Option      "CircularScrolling"          "on"
        Option      "CircScrollTrigger"          "0"
        ...
    EndSection
    
请注意，在少数情况下，省略号可能是代码的一部分。细心的用户很容易根据上下文来辨别。 
