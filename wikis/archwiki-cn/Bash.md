**翻译状态：**

  * 本文（或部分内容）译自 [Bash](<https://wiki.archlinux.org/title/Bash> "arch:Bash")，最近一次同步于 2024-12-16，若英文版本有所[更改](<https://wiki.archlinux.org/title/Bash?diff=0&oldid=816275>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Bash_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Bash/函数](<../zh-cn/Bash/%E5%87%BD%E6%95%B0.html> "Bash/函数")
  * [Bash/Prompt customization](</wzh/index.php?title=Bash/Prompt_customization&action=edit&redlink=1> "Bash/Prompt customization（页面不存在）")
  * [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")
  * [Readline](<../zh-cn/Readline.html> "Readline")
  * [Fortune](</wzh/index.php?title=Fortune&action=edit&redlink=1> "Fortune（页面不存在）")
  * [Pkgfile](<../zh-cn/Pkgfile.html> "Pkgfile")
  * [命令行解释器](<../zh-cn/%E5%91%BD%E4%BB%A4%E8%A1%8C%E8%A7%A3%E9%87%8A%E5%99%A8.html> "命令行解释器")

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** 文章内许多链接需要调整。（在[Talk:Bash](<../zh-cn/Talk:Bash.html>)讨论）

[Bash](<https://www.gnu.org/software/bash/>) (Bourne-again Shell) 是一个来自 [GNU](<../zh-cn/GNU.html> "GNU") 的[命令行解释器](<../zh-cn/Command-line_shell.html> "Command-line shell")/编程语言。它的名字是向它的前身——很早以前的 Bourne shell 致敬。Bash可以运行在大部分类 UNIX 操作系统中，包括 GNU/Linux。 

Bash是Arch Linux的默认命令行解释器。 

##  调用

Bash 的运行方式会取决于 Bash 被调用的方式。下面是一些不同模式的描述。 

如果 Bash 以TTY中的`login`、[SSH](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH") 守护进程、或者其它类似的方式派生出来，我们称之为登录 (login) shell。你可以使用命令行选项 `-l` 或 `--login` 来使用这种模式。 

如果 Bash 的标准输入输出和标准错误输出都连接到终端(比如说，一个终端模拟器)，并且在启动的时候既没有使用 `-c` 选项和[非选项参数](<https://unix.stackexchange.com/a/96805>)(比如说，`bash **script**`)，我们称之为交互 (interactive) shell。所有的交互式 shell 都会执行`/etc/bash.bashrc` 和 `~/.bashrc` 文件中的配置，而登录shell还会执行`/etc/profile` 和 `~/.bash_profile` 中的配置。 

**注意：** 在 Arch Linux 中 `/bin/sh` (过去是 Bourne shell 的执行文件名) 是 `bash` 的符号链接。如果 Bash 通过 `sh` 方式调用，它会尽量模拟历史上 `sh` 的启动行为，包括 POSIX 兼容能力。

通过在Bash启动时使用 `--posix` 命令行参数或者在启动后执行 ‘`set -o posix`’ 来使Bash在增强的POSIX标准下运行。 

###  配置文件

Bash会在启动时按照不同的启动方式执行一系列启动文件。详细描述请参考GNU Bash指南中`/usr/share/doc/bash/bashref.html` ([Bash启动文件](<https://www.gnu.org/software/bash/manual/bash.html#Bash-Startup-Files>))这一节。 

文件  | 描述  | 登录 shell (见下) | 交互 shell 非登录  
---|---|---|---  
`/etc/profile` |  [加载](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#Source> "Help:Reading")全部储存在 `/etc/profile.d/*.sh` 和 `/etc/bash.bashrc` 中的配置。  | 是  | 否   
`~/.bash_profile` | 针对每个用户，紧接 `/etc/profile` 执行。如果这个文件不存在，会顺序检查 `~/.bash_login` 和 `~/.profile` 文件。框架文件 `/etc/skel/.bash_profile` 同时会引用 `~/.bashrc`。  | 是  | 否   
`~/.bash_logout` | 针对每个用户，退出登录 shell 后。  | 是  | 否   
`/etc/bash.bash_logout` | 取决于 `-DSYS_BASH_LOGOUT="/etc/bash.bash_logout"` 编译标记。退出登录 shell 后。  | 是  | 否   
`/etc/bash.bashrc` | 取决于编译标志 `-DSYS_BASHRC="/etc/bash.bashrc"`。加载 `/usr/share/bash-completion/bash_completion` 配置。  | 否  | 是   
`~/.bashrc` | 针对每个用户，在 `/etc/bash.bashrc` 后加载。  | 否  | 是   
  
**注意：**

  * 如果以 `--login` 调用，登录 shell 可能不是交互式的。
  * 如果可以交互， _非登录_ shell **不会** 加载 `~/.bash_profile`。它会继承调用他们的父进程（可能是一个登录 shell）的环境参数。更多信息，请参考[GregsWiki:ProcessManagement#On processes, environments and inheritance](<https://mywiki.wooledge.org/ProcessManagement#On_processes.2C_environments_and_inheritance> "gregswiki:ProcessManagement")。

###  Shell 与环境变量

Bash的行为和通过它启动的程序会被许多环境变量影响。[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")用于储存有用的值，比如命令搜索路径，或者默认浏览器。当一个新的 shell 或者脚本被启动时，这个 shell 会继承它的父进程的环境变量，从而这个 shell 会带有内部 shell 变量[[1]](<http://www.kingcomputerservices.com/unix_101/understanding_unix_shells_and_environment_variables.htm>)。 

这些内部 shell 变量可以以此导出以变成环境变量： 
    
    VARIABLE=content
    export VARIABLE
    
或者 
    
    export VARIABLE=content
    
环境变量依照惯例放置在`~/.profile`或者`/etc/profile`中，这样其他兼容 Bourne shell 的 shell 也可以使用。 

关于更详尽的内容，您可以参考[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")。 

##  命令行

Bash 的命令行由一个叫做 [Readline](<../zh-cn/Readline.html> "Readline") 的分离库来管理。Readline 提供了[emacs](<../zh-cn/Emacs.html> "Emacs") 和 [vi](<../zh-cn/Vi.html> "Vi") 风格的快捷键用于操作命令行，比如说，以单词为基准前后移动、删除等。管理输入[历史](<../zh-cn/Readline.html#%E5%8E%86%E5%8F%B2> "Readline")也是 Readline 的职责。它还允许你创造[宏](<../zh-cn/Readline.html#%E5%AE%8F> "Readline")。 

###  Tab 键补全

[Tab 键补全](<https://en.wikipedia.org/wiki/Command-line_completion> "wikipedia:Command-line completion")，提供在按下 `tab` 键后自动补全命令的功能（这个功能默认启用）。 

####  Tab 按下的次数

可能最多需要按三次 tab 才能显示所有的补全选项。如果希望减少这个数值，请参考[更快的补全操作](<../zh-cn/Readline.html#Faster_completion> "Readline")。 

####  常用命令的选项补全

通常来讲，Bash 中按下 tab 只会补全命令、文件名和变量。安装 [bash-completion](<https://archlinux.org/packages/?name=bash-completion>)包 包，并加载 `/usr/share/bash-completion/bash_completion` 文件中的配置（这个文件应该已经在Arch的/etc/bash.bashrc中加载了），可以提供更多针对常见命令的选项的 tab 补全。安装这个包后，常规的补全（比如说 `ls file.*` `Tab` `Tab`）可能会表现得不同。但是，您可以通过`compopt -o bashdefault _program_`命令来重新启用。(更多细节，请参考 [[2]](<https://bbs.archlinux.org/viewtopic.php?id=128471>) and [[3]](<https://www.gnu.org/software/bash/manual/html_node/Programmable-Completion-Builtins.html>)。) 

####  自定义命令补全

**注意：** 使用 `complete` 功能可能与 [bash-completion](<https://archlinux.org/packages/?name=bash-completion>)包 冲突。

通常来讲，Bash 中按下 tab 只会补全命令后的文件名。通过`complete -c`命令，Bash 可以规定某些命令后的补全形式为命令，比如： 
    
    ~/.bashrc
    
    complete -c man which
    
或通过`-cf`命令，规定补全形式为命令和文件，比如： 
    
    complete -cf sudo

更多补全形式，请参考手册[bash(1) § Programmable Completion](<https://man.archlinux.org/man/bash.1#Programmable_Completion>)。 

###  历史

####  历史补全

您可以绑定上下键来在 Bash 的历史中查找（请参考 [Readline#历史](<../zh-cn/Readline.html#%E5%8E%86%E5%8F%B2> "Readline") and [Readline 启动文件语法](<https://www.gnu.org/software/bash/manual/html_node/Readline-Init-File-Syntax.html>))： 
    
    ~/.bashrc
    
     bind '"\e[A": history-search-backward'
     bind '"\e[B": history-search-forward'
    
或者所有 Readline 程序： 
    
    ~/.inputrc
    
    "\e[A": history-search-backward
    "\e[B": history-search-forward
    
####  更近的历史记录

`HISTCONTROL`变量可以避免历史记录记录特定的命令。 

不记录连续重复的命令： 
    
    ~/.bashrc
    
    export HISTCONTROL=ignoredups

历史记录中重复命令（无论是否连续）只记录最后一条： 
    
    ~/.bashrc
    
    export HISTCONTROL=erasedups

不记录空格开头的命令： 
    
    ~/.bashrc
    
    export HISTCONTROL=ignorespace

不记录连续重复的命令、空格开头的命令： 
    
    ~/.bashrc
    
    export HISTCONTROL=ignoreboth

重复命令只记录最后一条，且不记录空格开头的命令： 
    
    ~/.bashrc
    
    export HISTCONTROL="erasedups:ignorespace"

更多选项，请参考手册[bash(1) § HISTCONTROL](<https://man.archlinux.org/man/bash.1#HISTCONTROL>)。 

####  禁用历史记录

临时禁用历史记录： 
    
    $ set +o history
    
现在输入的命令将不会存入`$HISTFILE`。 

比如说，你现在可以执行 `printf secret | sha256sum` 来生成密码文件的散列值，或是隐藏您使用GPG的历史，如执行`gpg -eaF secret-pubkey.asc`命令。这些秘密不会被写入磁盘。 

开启历史记录： 
    
    $ set -o history
    
禁用所有的 Bash 历史： 
    
    ~/.bashrc or /etc/profile
    
    export HISTSIZE=0

为了保险（这会永远清除所有的历史记录）： 
    
    $ wipe -i -l2 -x4 -p4 "$HISTFILE"
    $ ln -sv /dev/null "$HISTFILE"
    
###  模仿 Zsh 的帮助功能

[Zsh](<../zh-cn/Zsh.html> "Zsh") 可以在光标指向命令的时候按 `Alt+h` 来调用这个命令的手册。 相同的行为可以通过这个 [Readline](<../zh-cn/Readline.html> "Readline") 绑定在 Bash 中开启： 
    
    ~/.bashrc
    
    run-help() { help "$READLINE_LINE" 2>/dev/null || man "$READLINE_LINE"; }
    bind -m vi-insert -x '"\eh": run-help'
    bind -m emacs -x     '"\eh": run-help'
    
这个操作假设你使用（默认的）Emacs [编辑模式](<../zh-cn/Readline.html#Editing_mode> "Readline")。 

### Share bash history across machines

[atuin](<https://archlinux.org/packages/?name=atuin>)包 replaces your existing shell history with an SQLite database, and records additional context for your commands. Additionally, it provides optional and fully encrypted synchronization of your history between machines, via an Atuin server. 

Enable bash history timestamps (`export HISTTIMEFORMAT="%F %T "`) before syncing. [Atuin](<https://github.com/atuinsh/atuin>) works well with tools like [blesh-git](<https://aur.archlinux.org/packages/blesh-git/>)AUR and [cmd-wrapped](<https://github.com/YiNNx/cmd-wrapped>) to provide an enhanced terminal experience across machines. 

##  别名

[别名](<https://en.wikipedia.org/wiki/alias> "wikipedia:alias")（alias）是可以让您用另一个字符串来替换一个字符串的命令。这个命令常常被用来缩短系统命令，或者用来将默认参数加入到常用命令中。 

针对用户的别名可以保存在`~/.bashrc`, 或任意`~/.bashrc`中[加载](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#Source> "加载")的脚本。系统级的别名(这些会影响所有用户)存放在`/etc/bash.bashrc`。别名示例可参考 [[4]](<https://gist.github.com/anonymous/a9055e30f97bd19645c2>)。 

关于函数，请参考[函数](<../zh-cn/Bash/%E5%87%BD%E6%95%B0.html> "Bash/Functions")。 

##  提示与技巧

###  自定义提示符

参见[自定义提示符](</wzh/index.php?title=Bash/Prompt_customization&action=edit&redlink=1> "Bash/Prompt customization（页面不存在）")。 

###  语法高亮与自动提示

[ble.sh](<https://github.com/akinomyoga/ble.sh>) (Bash Line Editor), packed as [blesh-git](<https://aur.archlinux.org/packages/blesh-git/>)AUR, is a command line editor written in pure Bash, which is an alternative to GNU Readline. It has many enhanced features like syntax highlighting, autosuggestions, menu-completion, abbreviations, [Vim](<../zh-cn/Vim.html> "Vim") editing mode, and hook functions. Other interesting features include status line, history share, right prompt, transient prompt, and xterm title. 

After installing it, [source](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#Source> "Source") it in an interactive session. 
    
    ~/.bashrc
    
    source /usr/share/blesh/ble.sh

Configurations are explained in depth in the [~/.blerc](<https://github.com/akinomyoga/ble.sh#14-user-settings-blerc>) file and at the [wiki](<https://github.com/akinomyoga/ble.sh/wiki>). The stable [blesh](<https://aur.archlinux.org/packages/blesh/>)AUR package is also available. 

###  找不到命令

[pkgfile](<../zh-cn/Pkgfile.html> "Pkgfile") 提供了一个"找不到命令"的钩子，可以在输入未知命令后自动查找官方的软件包。 

你需要[加载](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#Source> "Help:Reading")这个钩子来启用它，如下： 
    
    ~/.bashrc
    
    source /usr/share/doc/pkgfile/command-not-found.bash

现在，运行一个不可用的命令将会显示如下信息： 
    
    $ abiword
    
    abiword may be found in the following packages:
      extra/abiword 3.0.1-2	/usr/bin/abiword
    
**注意：** 需要先更新 pkgfile 的数据库才能运作。更多细节，请参考[pkgfile#安装](<../zh-cn/Pkgfile.html#%E5%AE%89%E8%A3%85> "Pkgfile")。

###  在终端内禁用Ctrl+Z

你可以像这样包装你的命令，来关闭 `Ctrl+Z` 功能（暂停/关闭程序）。通过在这个脚本中包装命令 
    
    #!/bin/bash
    trap "" 20
    _adom_
    
这时如果你在玩 [adom](<https://aur.archlinux.org/packages/adom/>)AUR 要按 `Shift+Z` 组合键时不小心按下了 `Ctrl+Z` 组合键，你的游戏就不会停止运行了，因为我们已经禁用了`Ctrl+Z`。 

###  登出后清空屏幕

当登出虚拟终端时，清空屏幕： 
    
    ~/.bash_logout
    
    clear
    reset
    
###  输入路径自动添加"cd"

Bash 可以自动在输入的一个路径前添加 `cd `。比如说： 
    
    $ /etc
    
    bash: /etc: Is a directory
    
但是如果在 `.bashrc` 文件里添加一行: 
    
    ~/.bashrc
    
    ...
    shopt -s autocd
    ...
    
你会得到： 
    
    [user@host ~]$ /etc
    cd /etc
    [user@host etc]$
    
###  自动跳转

Python脚本[autojump-git](<https://aur.archlinux.org/packages/autojump-git/>)AUR 允许在用户访问最多的路径中搜索文件系统。 

安装完后，[加载](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#Source> "Help:Reading") `/etc/profile.d/autojump.bash` 来启动这项功能。 

[zoxide](<https://archlinux.org/packages/?name=zoxide>)包是`autojump`的功能性能增强版，可直接替代。 

###  防止覆盖文件

在当前的会话中，防止 shell 输出重定向覆盖一个已有的文件： 
    
    $ set -o noclobber
    
这和`set -C`命令是一样的。 

如果想让该用户一直生效： 
    
    ~/.bashrc
    
    ...
    set -o noclobber

在设定 `noclobber` 的情况下强制覆盖文件： 
    
    $ echo "output" >| file.txt
    
###  使用目录堆栈切换目录

`pushd`与`popd`以堆栈的方式控制目录切换，利于“撤销”目录切换动作。 
    
     [user@host ~] pushd /tmp/dir1
     [user@host /tmp/dir1] pushd /var/lib
     [user@host/var/lib] popd
     [user@host/tmp/dir1] popd
     [user@host ~]
    
参见[bash(1) § DIRSTACK](<https://man.archlinux.org/man/bash.1#DIRSTACK>)。 

##  错误排除

###  修正窗口大小调整时的换行

如果您调整了[终端模拟器](<../zh-cn/List_of_applications/Utilities.html#Terminal_emulators> "List of applications/Utilities")的大小，Bash 可能并没有得到大小重调的信号，你键入的文本就不会正确的换行，并且与已输入内容重叠。启用 `checkwinsize` 选项可以在每一个命令后检查窗口的大小，并按需更新 `LINES` 和 `COLUMNS` 的值来调整。 
    
    ~/.bashrc
    
    shopt -s checkwinsize
    
###  设置 ignoreeof 后 shell 仍然退出

如果您设置了 `ignoreeof` 选项，但是如果重复按下 `ctrl-D` shell 仍然会退出。因为这个选项只允许忽略 10 次连续的EOF记号（即 `Ctrl+D`）。 

如果需要将这个次数调的更高，需要使用 IGNOREEOF 变量。 

比如： 
    
    export IGNOREEOF=100
    
###  分析代码以检查错误

包 [shellcheck](<https://archlinux.org/packages/?name=shellcheck>)包 可以分析bash脚本（以及其他脚本），显示可能存在的问题，并对优化代码质量提出意见。 

[shellcheck.net](<https://www.shellcheck.net>) 网站也提供了基于此程序的相同功能。 

##  更多信息 （英语）

  * [Wikipedia:Bash (Unix shell)](<https://en.wikipedia.org/wiki/Bash_\(Unix_shell\)> "wikipedia:Bash \(Unix shell\)")
  * [Bash 参考手册](<https://www.gnu.org/software/bash/manual/bashref.html>)，或是 `/usr/share/doc/bash/bashref.html`
  * [Readline 启动文件语法](<https://www.gnu.org/software/bash/manual/html_node/Readline-Init-File-Syntax.html>)
  * [The Bourne-Again Shell](<https://www.aosabook.org/en/bash.html>) \- _开源软件架构_ 第三章
  * [PS1 生成器](<http://bashrcgenerator.com/>) \- 通过直观的界面生成你的 .bashrc/PS1 脚本
  * [有用的 .bashrc 命令](<https://serverfault.com/questions/3743/what-useful-things-can-one-add-to-ones-bashrc>)

###  教程

  * [Greg's Wiki](<https://mywiki.wooledge.org/> "gregswiki:")
  * [GregsWiki:BashGuide](<https://mywiki.wooledge.org/BashGuide> "gregswiki:BashGuide")
  * [GregsWiki:BashFAQ](<https://mywiki.wooledge.org/BashFAQ> "gregswiki:BashFAQ")
  * [Quote Tutorial](<https://www.grymoire.com/Unix/Quote.html>)

###  社区

  * [一个 Bash 的活跃友好的IRC频道](<ircs://irc.libera.chat/bash>)

###  例子

  * [怎样修改 xterm 的标题](<https://tldp.org/HOWTO/Xterm-Title-4.html>)
