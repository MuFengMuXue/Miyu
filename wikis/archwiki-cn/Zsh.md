**翻译状态：**

  * 本文（或部分内容）译自 [Zsh](<https://wiki.archlinux.org/title/Zsh> "arch:Zsh")，最近一次同步于 2024-10-19，若英文版本有所[更改](<https://wiki.archlinux.org/title/Zsh?diff=0&oldid=819136>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Zsh_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Zsh](<https://www.zsh.org/>) 是一款功能强大的[命令行解释器](<../zh-cn/%E5%91%BD%E4%BB%A4%E8%A1%8C%E8%A7%A3%E9%87%8A%E5%99%A8.html> "命令行解释器")（shell），既可以作为交互式终端来使用，也可以作为脚本语言解释器来使用。它在兼容 POSIX 的 sh 的同时（默认不兼容，仅在使用 `emulate sh` 时兼容），还改进了 [Tab 补全](<https://zsh.sourceforge.io/Guide/zshguide06.html>)和[通配符](<https://zsh.sourceforge.io/Doc/Release/Expansion.html>)等功能。 

[Zsh FAQ](<https://zsh.sourceforge.io/FAQ/zshfaq01.html#l4>) 说明了使用 Zsh 的更多原因。 

##  安装

在开始安装之前，可以查看一下当前正在使用的 Shell 软件： 
    
    $ echo $SHELL
    
[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [zsh](<https://archlinux.org/packages/?name=zsh>)包 包，也可以同时安装 [zsh-completions](<https://archlinux.org/packages/?name=zsh-completions>)包 包以获取更多命令补全规则。 

###  初始配置

在终端里面输入以下命令，确保已经正确安装了 Zsh： 
    
    $ zsh
    
运行后你应该会看到 _zsh-newuser-install_ （新用户安装向导），它可以协助你完成一些基础配置。如果要跳过这一步骤，可以按 `q` 退出。如果你没有看到 _zsh-newuser-install_ ，可以手动运行以下命令： 
    
    $ autoload -Uz zsh-newuser-install
    $ zsh-newuser-install -f
    
**注意：** 确保你的终端尺寸至少为 72×15 大小，否则 _zsh-newuser-install_ 将无法运行。

###  将 Zsh 设为默认 Shell 软件

将 Shell 改为 `/usr/bin/zsh`。参见[命令行解释器#更改默认_Shell](<../zh-cn/%E5%91%BD%E4%BB%A4%E8%A1%8C%E8%A7%A3%E9%87%8A%E5%99%A8.html#%E6%9B%B4%E6%94%B9%E9%BB%98%E8%AE%A4_Shell> "命令行解释器")。 

**提示：** 如果要替换 [bash](<https://archlinux.org/packages/?name=bash>)包，用户可能希望能够将 `~/.bashrc` 文件的某些代码转移到 `~/.zshrc` 文件（例如：命令提示符和[别名](<../zh-cn/Bash.html#%E5%88%AB%E5%90%8D> "Bash")），以及将 `~/.bash_profile` 文件的代码转移到 `~/.zprofile` 文件（例如：[启动 X Window System 的代码](<../zh-cn/Xinit.html#%E7%99%BB%E5%BD%95%E6%97%B6%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8_X> "Xinit")）。

##  启动/关闭文件

**提示：** 有关交互式 shell 和登录 shell 的解释以及在启动文件中放置内容的建议，请参阅 [A User's Guide to the Z-Shell](<https://zsh.sourceforge.io/Guide/zshguide02.html>)（Z-Shell 用户指南，英文）。

**注意：**

  * 如果未设置`$ZDOTDIR`，则使用`$HOME`。
  * 如果在任何文件中取消设置`RCS`选项，那么之后的配置文件将不会被读取。
  * 如果在任何文件中取消设置`GLOBAL_RCS`选项，那么之后的全局配置文件（`/etc/zsh/*`）将不会被读取。

在启动时，Zsh 会按以下顺序读取这些文件（如果存在）： 

  * `/etc/zsh/zshenv` 用于设置所有用户的[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")。不应包含会产生输出或假设 shell 连接到 TTY 的命令。此文件**一旦** 存在就会被读取，且无法跳过。
  * `$ZDOTDIR/.zshenv` 用于设置用户的[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")。不应包含会产生输出或假设 shell 连接到 TTY 的命令。此文件**一旦** 存在就会被读取。
  * `/etc/zsh/zprofile` 在启动为**登录 shell** 时为所有用户执行的命令。在 Arch Linux 中，此文件默认包含[一行引入`/etc/profile`的代码](<https://gitlab.archlinux.org/archlinux/packaging/packages/zsh/-/blob/main/zprofile>)。在删除该行之前，请参阅下方的警告！ 
    * `/etc/profile` 此文件应由所有符合 POSIX 标准的 shell 在登录时引入，用于设置`$PATH`及其他环境变量，以及应用程序相关的设置（`/etc/profile.d/*.sh`）。
  * `$ZDOTDIR/.zprofile` 在启动为**登录 shell** 时执行的用户命令。通常用于自动启动图形会话和设置会话范围的环境变量。
  * `/etc/zsh/zshrc` 用于为所有用户设置交互式 shell 的配置并执行命令，会在启动为**交互式 shell** 时读取。
  * `$ZDOTDIR/.zshrc` 用于为用户设置交互式 shell 配置并执行命令，会在启动为**交互式 shell** 时读取。
  * `/etc/zsh/zlogin` 在初始进程结束时为所有用户执行的命令，会在启动为**登录 shell** 时读取。
  * `$ZDOTDIR/.zlogin` 在初始进程结束时执行的用户命令，会在启动为**登录 shell** 时读取。通常用于自动启动命令行工具，不应用于启动图形会话，因为此时会话可能包含仅适用于交互式 shell 的配置。
  * `$ZDOTDIR/.zlogout` 在**登录 shell** 退出时执行的用户命令。
  * `/etc/zsh/zlogout` 在**登录 shell** 退出时为所有用户执行的命令。

请参阅[图示说明（英文）](<https://web.archive.org/web/20241008050626/https://blog.flowblok.id.au/2013-02/shell-startup-scripts.html#implementation>)。 

**注意：**`$HOME/.profile`不是Zsh的启动文件的一部分，除非 zsh 以`sh`或`ksh`模式运行并作为登录 shell 启动，否则不会被 zsh 引入。有关 sh 和 [ksh](</wzh/index.php?title=Ksh&action=edit&redlink=1> "Ksh（页面不存在）")（英语：[ksh](<https://wiki.archlinux.org/title/ksh> "en:ksh")） 兼容模式的更多详情，请参阅[zsh(1) § COMPATIBILITY](<https://man.archlinux.org/man/zsh.1#COMPATIBILITY>)。

**警告：** 不要删除`/etc/zsh/zprofile`中的[默认代码](<https://gitlab.archlinux.org/archlinux/packaging/packages/zsh/-/blob/main/zprofile>)，否则会破坏某些在`/etc/profile.d/`目录下提供脚本的软件包的完整性。

##  配置 Zsh

尽管 Zsh 开箱即用，但它的默认设置不符合大多数用户的使用习惯。但由于 Zsh 有着大量自定义选项，配置 Zsh 可能是一项艰巨而耗时的体验。有关自动配置，请参阅[#第三方扩展](<#%E7%AC%AC%E4%B8%89%E6%96%B9%E6%89%A9%E5%B1%95>)。 

###  简单的 .zshrc

下面是一个示例配置文件。它提供了一组不错的默认选项，并给出了许多可以自定义 Zsh 的方法的示例。要使用此配置，请将其保存为 `.zshrc`。 

**提示：** 运行 `source ~/.zshrc` 可立即应用更改，无需注销后重新登录。
    
    ~/.zshrc
    
    autoload -Uz compinit promptinit
    compinit
    promptinit
    
    # 将默认命令行提示设置为 walters 主题
    prompt walters
    
有关命令提示主题系统的更多详细信息，请参阅[#提示主题](<#%E6%8F%90%E7%A4%BA%E4%B8%BB%E9%A2%98>)。 

###  配置 $PATH

Zsh 将 `PATH` 变量绑定到 `path` 数组。这样，您只需修改 `path` 数组即可操作 `PATH`。有关详细信息，请参阅 [A User's Guide to the Z-Shell](<https://zsh.sourceforge.io/Guide/zshguide02.html#l24>)（Z-Shell 用户指南，英文）。 

往`PATH`变量中添加`~/.local/bin/`： 
    
    ~/.zshenv
    
    typeset -U path PATH
    path=(~/.local/bin $path)
    export PATH

###  命令补全

也许 Zsh 最引人注目的特性就是它先进的自动补全功能。至少，请在 `.zshrc` 中启用自动完成功能。在 `~/.zshrc` 的最后加入下面的配置开启自动补全： 
    
    ~/.zshrc
    
    autoload -U compinit
    compinit
    
上面的补全配置包括 ssh/scp/sftp 命令中的主机名补全。但是要让这个特性正常工作，不能启用 ssh 的主机名散列（hash，即 ssh 客户端配置中的 `HashKnownHosts` 选项）。 

添加下面的配置可以启动使用方向键控制的自动补全： 
    
    ~/.zshrc
    
    zstyle ':completion:*' menu select

按两次 `Tab` 启动菜单 

为了实现在特权命令中（例如，当你以 [sudo](<../zh-cn/Sudo.html> "Sudo") 开始输入一个命令时，补全脚本也会尝试确定你可以用 sudo 完成的选项）对特权环境的自动补全，添加： 
    
    ~/.zshrc
    
    zstyle ':completion::complete:*' gain-privileges 1
    
**警告：** 这允许 Zsh 补全脚本以 sudo 权限运行命令。如果您使用不受信任的自动补全脚本，则不应启用此功能。

**注意：** 这种特殊的上下文感知补全仅适用于少数命令。

####  自定义补全

可以自己编写自定义补全，参考 [zshcompsys(1)](<https://man.archlinux.org/man/zshcompsys.1>) 手册页。 

请注意，官方文档可能难以阅读，可以考虑尝试更简单的 [zsh-completion-howto](<https://github.com/zsh-users/zsh-completions/blob/master/zsh-completions-howto.org>) 教程（英文），以便轻松入门。 

###  消除历史记录中的重复条目
    
    ~/.zshrc
    
    setopt HIST_IGNORE_DUPS

假如目前的历史记录中已经有重复条目，可以运行下面的命令清除 
    
    $ sort -t ";" -k 2 -u ~/.zsh_history | sort -o ~/.zsh_history
    
###  快捷键绑定

Zsh 不使用 [readline](<../zh-cn/Readline.html> "Readline")，而是使用其自身且更为强大的 Zsh 行编辑器（Zsh Line Editor，ZLE）。它不会读取 `/etc/inputrc` 或 `~/.inputrc` 文件。阅读 [A closer look at the zsh line editor and creating custom widgets](<https://sgeb.io/posts/2014/04/zsh-zle-custom-widgets/>) 以了解 ZLE 配置。 

ZLE 有 [Emacs](<../zh-cn/Emacs.html> "Emacs") 模式和 [vi](<../zh-cn/Vi.html> "Vi") 模式。如果 `VISUAL` 和 `EDITOR` 环境变量之一包含字符串 `vi`，则会使用 vi 模式，否则默认为 Emacs 模式。可以分别使用 `bindkey -e` 或 `bindkey -v` 显式指定 Emacs 模式和 vi 模式。在 vi 模式下按 Esc 键的延迟默认是 0.4 秒，你可以通过设置 `export KEYTIMEOUT=5` 将其缩短至 0.05 秒。 

按键绑定是通过将与按键对应的一个转义序列映射到一个 ZLE 小部件来分配的。可用的小部件及其作用描述和默认的按键绑定可以在 [zshzle(1) § STANDARD WIDGETS](<https://man.archlinux.org/man/zshzle.1#STANDARD_WIDGETS>) 和 [zshcontrib(1) § ZLE FUNCTIONS](<https://man.archlinux.org/man/zshcontrib.1#ZLE_FUNCTIONS>) 中找到。 

在 Zsh 中设置按键绑定的推荐方法是使用来自 [terminfo(5)](<https://man.archlinux.org/man/terminfo.5>) 的字符串功能。例如[[1]](<https://web.archive.org/web/20180704181216/http://zshwiki.org/home/zle/bindkeys>)[[2]](<https://www.zsh.org/mla/users/2010/msg00065.html>)： 
    
    ~/.zshrc
    
    # 创建兼容 zkbd 的哈希表；
    # 要向此哈希表添加其他键，请参阅：man 5 terminfo
    typeset -g -A key
    
    key[Home]="${terminfo[khome]}"
    key[End]="${terminfo[kend]}"
    key[Insert]="${terminfo[kich1]}"
    key[Backspace]="${terminfo[kbs]}"
    key[Delete]="${terminfo[kdch1]}"
    key[Up]="${terminfo[kcuu1]}"
    key[Down]="${terminfo[kcud1]}"
    key[Left]="${terminfo[kcub1]}"
    key[Right]="${terminfo[kcuf1]}"
    key[PageUp]="${terminfo[kpp]}"
    key[PageDown]="${terminfo[knp]}"
    key[Shift-Tab]="${terminfo[kcbt]}"
    
    # 相应地设置键
    [[ -n "${key[Home]}"      ]] && bindkey -- "${key[Home]}"       beginning-of-line
    [[ -n "${key[End]}"       ]] && bindkey -- "${key[End]}"        end-of-line
    [[ -n "${key[Insert]}"    ]] && bindkey -- "${key[Insert]}"     overwrite-mode
    [[ -n "${key[Backspace]}" ]] && bindkey -- "${key[Backspace]}"  backward-delete-char
    [[ -n "${key[Delete]}"    ]] && bindkey -- "${key[Delete]}"     delete-char
    [[ -n "${key[Up]}"        ]] && bindkey -- "${key[Up]}"         up-line-or-history
    [[ -n "${key[Down]}"      ]] && bindkey -- "${key[Down]}"       down-line-or-history
    [[ -n "${key[Left]}"      ]] && bindkey -- "${key[Left]}"       backward-char
    [[ -n "${key[Right]}"     ]] && bindkey -- "${key[Right]}"      forward-char
    [[ -n "${key[PageUp]}"    ]] && bindkey -- "${key[PageUp]}"     beginning-of-buffer-or-history
    [[ -n "${key[PageDown]}"  ]] && bindkey -- "${key[PageDown]}"   end-of-buffer-or-history
    [[ -n "${key[Shift-Tab]}" ]] && bindkey -- "${key[Shift-Tab]}"  reverse-menu-complete
    
    # 最后，确保终端处于应用程序模式，此时 ZLE 处于
    # 活动状态。只有这样，$terminfo 中的值才有效。
    if (( ${+terminfo[smkx]} && ${+terminfo[rmkx]} )); then
    	autoload -Uz add-zle-hook-widget
    	function zle_application_mode_start { echoti smkx }
    	function zle_application_mode_stop { echoti rmkx }
    	add-zle-hook-widget -Uz zle-line-init zle_application_mode_start
    	add-zle-hook-widget -Uz zle-line-finish zle_application_mode_stop
    fi

####  查找历史记录

您需要设置 `key` 数组并确保 ZLE 进入应用程序模式以使用以下说明。请参阅 [#快捷键绑定](<#%E5%BF%AB%E6%8D%B7%E9%94%AE%E7%BB%91%E5%AE%9A>)。 

要启用历史搜索，请将这些行添加到 `.zshrc` 文件中： 
    
    ~/.zshrc
    
    autoload -Uz up-line-or-beginning-search down-line-or-beginning-search
    zle -N up-line-or-beginning-search
    zle -N down-line-or-beginning-search
    
    [[ -n "${key[Up]}"   ]] && bindkey -- "${key[Up]}"   up-line-or-beginning-search
    [[ -n "${key[Down]}" ]] && bindkey -- "${key[Down]}" down-line-or-beginning-search
    
这样，当按下 `Up` 或 `Down` 键时，只会显示与当前光标位置之前匹配的过去命令。 

####  Shift、Alt、Ctrl 和 Meta 修饰键

xterm 兼容终端可以使用 [user_caps(5)](<https://man.archlinux.org/man/user_caps.5>) 中的扩展键定义，即 `Shift`、`Alt`、`Ctrl` 和 `Meta` 与 `Up`、`Down`、`Left`、`Right`、`PageUp`、`PageDown`、`Home`、`End` 或 `Del` 的组合。请参阅 [zkbd 源代码](<https://sourceforge.net/p/zsh/code/ci/master/tree/Functions/Misc/zkbd>)以获取修饰键和组合键的推荐名称列表。 

例如，使用 `Ctrl+Left` 移动到上一个单词的开头，使用 `Ctrl+Right` 移动到下一个单词的开头： 
    
    ~/.zshrc
    
    key[Control-Left]="${terminfo[kLFT5]}"
    key[Control-Right]="${terminfo[kRIT5]}"
    
    [[ -n "${key[Control-Left]}" ]] && bindkey -- "${key[Control-Left]}" behind-word
    [[ -n "${key[Control-Right]}" ]] && bindkey -- "${key[Control-Right]}" front-word

####  另一种方法

该方法会在启动应用之前，将你的输入保存在一行当中。 
    
    ~/.zshrc
    
    ncmpcppShow() { ncmpcpp <$TTY; zle redisplay; }
    zle -N ncmpcppShow
    bindkey '^[\' ncmpcppShow

###  命令提示

Zsh 提供了使用提示主题的选项，而对于对主题不满意（或想要扩展其实用性）的用户，可以构建自定义提示。 

####  提示主题

提示主题是快速轻松地在 Zsh 中设置彩色提示符的方法。有关提示主题以及如何编写自己的主题，请参阅 [zshcontrib(1) § PROMPT THEMES](<https://man.archlinux.org/man/zshcontrib.1#PROMPT_THEMES>)。 

要使用主题，请确保提示主题系统在 `.zshrc` 中设置为自动加载。这可以通过添加以下几行实现： 
    
    ~/.zshrc
    
    autoload -Uz promptinit
    promptinit
    
然后你可以运行下面的命令查看可用的提示主题： 
    
    $ prompt -l
    
例如，要使用 `walters` 主题，请输入： 
    
    $ prompt walters
    
要预览所有可用的主题，请使用以下命令： 
    
    $ prompt -p
    
#####  手动安装提示主题

可以手动安装主题而无需外部配置管理器工具。对于本地安装，首先创建一个文件夹并将其添加到 `fpath` 数组，例如： 
    
    $ mkdir ~/.zprompts
    $ fpath=("$HOME/.zprompts" "$fpath[@]")
    
现在在此文件夹中创建主题文件的符号链接： 
    
    $ ln -s mytheme.zsh ~/.zprompts/prompt_mytheme_setup
    
如果您希望全局安装主题，请执行以下操作： 
    
    # ln -s mytheme.zsh /usr/share/zsh/functions/Prompts/prompt_mytheme_setup
    
现在您应该能够使用以下方法激活它： 
    
    $ prompt mytheme
    
如果一切正常，可以相应地编辑 `.zshrc`。 

#####  添加提示主题而不为每个主题单独创建一个文件

除了通过自己的文件添加提示主题外，还可以从另一个文件（如 `.zshrc`）中添加主题，例如： 
    
    ~/.zshrc
    
    # 加载 promptinit
    autoload -Uz promptinit && promptinit
    
    # 定义主题
    prompt_mytheme_setup() {
    PS1="%~%# "
    }
    
    # 将主题添加到 promptsys
    prompt_themes+=( mytheme )
    
    # 加载主题
    prompt mytheme

###  自定义命令提示符

除了所有 shell 都通用的主要左侧提示符 `PS1`（`PROMPT`、`prompt`）之外，Zsh 还支持右侧提示符 `RPS1`（`RPROMPT`），这两个变量可用于自定义。 

其他特殊用途的提示符，例如 `PS2`（`PROMPT2`）、`PS3`（`PROMPT3`）、`PS4`（`PROMPT4`）、`RPS1`（`RPROMPT`）、`RPS2`（`RPROMPT2`）和 `SPROMPT`，在 [zshparam(1) § PARAMETERS USED BY THE SHELL](<https://man.archlinux.org/man/zshparam.1#PARAMETERS_USED_BY_THE_SHELL>) 中有说明。 

所有提示符都可以使用提示符转义进行自定义。可用的提示转义列在 [zshmisc(1) § EXPANSION OF PROMPT SEQUENCES](<https://man.archlinux.org/man/zshmisc.1#EXPANSION_OF_PROMPT_SEQUENCES>) 中。 

####  彩色

Zsh 设置颜色的方式与 [Bash](</wzh/index.php?title=Bash/%E8%87%AA%E5%AE%9A%E4%B9%89%E6%8F%90%E7%A4%BA%E7%AC%A6&action=edit&redlink=1> "Bash/自定义提示符（页面不存在）")（英语：[Bash/Prompt customization](<https://wiki.archlinux.org/title/Bash/Prompt_customization> "en:Bash/Prompt customization")） 不同；您无需使用 [terminfo(5)](<https://man.archlinux.org/man/terminfo.5>) 中的大量 ANSI 转义序列或终端功能。Zsh 提供了方便的提示转义来设置前景色、背景色和其他视觉效果；请参阅 [zshmisc(1) § Visual effects](<https://man.archlinux.org/man/zshmisc.1#Visual_effects>) 以获取它们的列表及其说明。 

[颜色](<https://zsh.sourceforge.io/FAQ/zshfaq03.html#l42>)可以使用十进制整数、八种最广泛支持的颜色之一的名称或十六进制格式的 # 后跟 RGB 三元组来指定。有关更多详细信息，请参阅 [zshzle(1) § CHARACTER HIGHLIGHTING](<https://man.archlinux.org/man/zshzle.1#CHARACTER_HIGHLIGHTING>) 中 fg=colour 的描述。 

命令 | 描述   
---|---  
`%F{color} [...] %f` | 和前面介绍的 $fg 是一样的，但是更简洁。还可以在 F 前面添加数字。   
`$fg_no_bold[color]` | 设置文本为非粗体同时设定文本颜色   
`$fg_bold[color]` | 设置文本为粗体同时设定文本颜色   
`$reset_color` | 重置文本颜色（改为默认颜色）。不会重置粗体设定。使用 `%b` 来重置粗体设定。可以使用 `%f` 来简化配置。   
`%K{color} [...] %k` | 设置背景颜色。和非粗体文本颜色一样。任何单一数字前缀会设置背景为黑色。   
  
大多数终端支持以下英文颜色名称作为代号： 

中文名称 | 英文名称/代号 | 编号   
---|---|---  
黑色 | `black` |  `0`  
红色 | `red` |  `1`  
绿色 | `green` |  `2`  
黄色 | `yellow` |  `3`  
蓝色 | `blue` |  `4`  
洋红色 | `magenta` |  `5`  
青色 | `cyan` |  `6`  
白色 | `white` |  `7`  
  
**注意：** 粗体文本不一定会和普通文本使用同一种颜色。例如, `$fg['yellow']` 会使用暗一点的黄色, 而 `$fg_bold['yellow']` 可能会使用亮一点的黄色。（译者注：具体是由你的终端模拟器配置决定的）

与 xterm 256 色兼容的终端模拟器的颜色编号 0–255 可在 [xterm-256color 图表](<https://upload.wikimedia.org/wikipedia/commons/1/15/Xterm_256color_chart.svg>)中找到。 

正确设置 TERM 环境变量后，可以使用 `echoti colors` 从 [terminfo(5)](<https://man.archlinux.org/man/terminfo.5>) 数据库中找到终端支持的最大颜色数。对于 [24 位颜色](<https://github.com/termstandard/colors/blob/master/README.md>)，还需使用 `print $COLORTERM` 检查 COLORTERM 环境变量。如果它返回 `24bit` 或 `truecolor`，则即使 terminfo 显示的数字较小，您的终端也支持 16777216（224）种颜色。 

**注意：**

  * 终端模拟器及其使用的配色方案之间的颜色 0–15 可能有所不同。
  * 许多终端仿真器使用更亮的颜色显示粗体。

**提示：**

  * 可以使用命令 `print -P _"prompt escapes"_` 测试提示转义，例如：
        
        $ print -P '%B%F{red}co%F{green}lo%F{blue}rs%f%b'

  * 如果您使用 24 位颜色，您可能需要在不支持它们的终端中加载 `zsh/nearcolor` 模块。例如：
        
        [[ "$COLORTERM" == (24bit|truecolor) || "${terminfo[colors]}" -eq '16777216' ]] || zmodload zsh/nearcolor

有关 `zsh/nearcolor` 模块的详细信息，请参阅 [zshmodules(1) § THE ZSH/NEARCOLOR MODULE](<https://man.archlinux.org/man/zshmodules.1#THE_ZSH/NEARCOLOR_MODULE>)。

####  示例

简单无色提示的示例： 
    
    PROMPT='%n@%m %~ %# '
    
显示方式： 

用户名@主机 ~ % 

带颜色的左右双面提示示例： 
    
    PROMPT='%F{green}%n%f@%F{magenta}%m%f %F{blue}%B%~%b%f %# '
    RPROMPT='[%F{yellow}%?%f]'
    
显示方式如下： 

用户名@主机 ~ % [0]

要使用 16-255 范围内的颜色和 24 位真彩色，您可以分别使用分配给所需颜色的 0 到 255 之间的数字及其十六进制颜色代码： 
    
    PROMPT='%F{2}%n%f@%F{5}%m%f %F{4}%B%~%b%f %# '
    RPROMPT='[%F{3}%?%f]'
    
    PROMPT='%F{#c0c0c0}%n%f@%F{#008000}%m%f %F{#800080}%B%~%b%f %# '
    RPROMPT='[%F{#0000ff}%?%f]'
    
###  示例 .zshrc 文件

  * 要获得与[每月 ISO 版本](<https://archlinux.org/download/>)（默认使用 Zsh）相同的设置，请安装 [grml-zsh-config](<https://archlinux.org/packages/?name=grml-zsh-config>)包。它包括来自 [grml](<https://grml.org/zsh/>) 的许多调整和高级优化。
  * <https://github.com/MrElendig/dotfiles-alice/blob/master/.zshrc> \- 基本设置，带有动态提示和窗口标题/硬信息。
  * <https://github.com/slashbeast/conf-mgmt/blob/master/roles/home_files/files/DOTzshrc> \- 具有多种功能的 zshrc，请务必查看其中的评论。值得注意的功能：确认功能以确保用户想要运行关机、重启或休眠，在提示中支持 GIT（无需 vcsinfo），带菜单的制表符完成，将当前执行的命令打印到窗口的标题栏中等等。

请参阅 [dotfiles#用户仓库](<../zh-cn/Dotfiles.html#%E7%94%A8%E6%88%B7%E4%BB%93%E5%BA%93> "Dotfiles")了解更多。 

##  提示与技巧

###  登录时自动启动 X

请参阅 [xinit#登录时自动启动 X](<../zh-cn/Xinit.html#%E7%99%BB%E5%BD%95%E6%97%B6%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8_X> "Xinit")。 

###  程序异常退出后恢复终端设置

许多程序会更改终端状态，并且通常不会在异常退出时恢复终端设置（例如崩溃或遇到 SIGINT 时）。 

这通常可以通过执行 [reset(1)](<https://man.archlinux.org/man/reset.1>) 来解决： 
    
    $ reset
    
以下部分介绍了避免手动重置终端的方法。 

####  ttyctl 命令

[ttyctl](<https://zsh.sourceforge.io/Doc/Release/Shell-Builtin-Commands.html#index-tty_002c-freezing>) 命令可用于“冻结/解冻”终端。要在启动时冻结交互式 shell，请使用以下命令： 
    
    ~/.zshrc
    
    ttyctl -f

####  使用转义序列重置终端

[替代画线字符集](<https://www.in-ulm.de/~mascheck/various/alternate_charset/>)可能会以 ttyctl 无法阻止的方式搞砸终端。 

一个简单的解决方案是从 `precmd` 钩子函数输出重置终端的转义序列，以便在每次绘制提示之前执行它们。例如，使用[转义序列](<https://www.in-ulm.de/~mascheck/various/alternate_charset/#solution>) `\e[0m\e(B\e)0\017\e[?5l\e7\e[0;0r\e8`: 
    
    ~/.zshrc
    
    autoload -Uz add-zsh-hook
    
    function reset_broken_terminal () {
    printf '%b' '\e[0m\e(B\e)0\017\e[?5l\e7\e[0;0r\e8'
    }
    
    add-zsh-hook -Uz precmd reset_broken_terminal

要测试它是否有效，请运行： 
    
    $ print '\e(0\e)B'
    
###  记住最近的目录

####  目录栈（dirstack）

Zsh 可以配置 DIRSTACK 相关变量来加速 cd 访问常用目录。在你的配置文件中添加下面的配置： 
    
    .zshrc
    
    DIRSTACKFILE="$HOME/.cache/zsh/dirs"
    if [[ -f $DIRSTACKFILE ]] && [[ $#dirstack -eq 0 ]]; then
      dirstack=( ${(f)"$(< $DIRSTACKFILE)"} )
      [[ -d $dirstack[1] ]] && cd $dirstack[1]
    fi
    chpwd() {
      print -l $PWD ${(u)dirstack} >$DIRSTACKFILE
    }
    
    DIRSTACKSIZE=20
    
    setopt autopushd pushdsilent pushdtohome
    
    ## Remove duplicate entries
    setopt pushdignoredups
    
    ## This reverts the +/- operators.
    setopt pushdminus
    
现在你可以使用 
    
    dirs -v
    
来打印目录栈（dirstack）。使用 `cd -<NUM>` 来跳转到以前访问过的目录。你还可以在连字符后面使用自动补全，非常方便。 

**注意：** 如果您打开了多个 zsh 会话并尝试 `cd`，则此操作将不起作用，因为两个会话在写入同一个文件时会发生冲突。

#### cdr

cdr 允许您从自动维护的列表中将工作目录更改为上一个工作目录。它将所有条目存储在跨会话维护的文件中，并且（默认情况下）在当前会话中的终端仿真器之间维护。 

有关设置说明，请参阅 [zshcontrib(1) § REMEMBERING RECENT DIRECTORIES](<https://man.archlinux.org/man/zshcontrib.1#REMEMBERING_RECENT_DIRECTORIES>)。 

#### zoxide

[zoxide](<https://archlinux.org/packages/?name=zoxide>)包 是一个更智能的 cd 命令，只需按几下键，您就可以导航到任何地方。它会记住您经常使用的目录，并使用评分机制来猜测您想要去的地方。 

###  帮助命令

与 [Bash](<../zh-cn/Bash.html> "Bash") 不同，Zsh 没有内置的 `help` 命令，而是提供 `run-help`。默认情况下，`run-help` 是 `man` 的别名，可以通过将其添加到命令前面来手动执行，也可以使用键盘快捷键 `Alt+h` 或 `Esc` `h` 为当前输入的命令调用它。 

由于默认情况下它只是 [man](<../zh-cn/Man_%E6%89%8B%E5%86%8C.html> "Man") 的别名，因此它仅适用于外部命令。为了改进其功能，使其适用于 shell 内置命令和其他 shell 功能，您需要使用 `run-help` 函数。有关 `run-help` 及其辅助函数的更多信息，请参阅 [zshcontrib(1)](<https://man.archlinux.org/man/zshcontrib.1>)。 

首先加载 `run-help` 函数，然后删除现有的 `run-help` 别名。为了方便起见，可以将 `help` 别名为 `run-help`。例如，将以下内容添加到您的 `zshrc`： 
    
    autoload -Uz run-help
    (( ${+aliases[run-help]} )) && unalias run-help
    alias help=run-help
    
必须单独启用助手功能： 
    
    autoload -Uz run-help-git run-help-ip run-help-openssl run-help-p4 run-help-sudo run-help-svk run-help-svn
    
例如，`run-help git commit` 命令现在将打开 [man page](<../zh-cn/Man_page.html> "Man page") [git-commit(1)](<https://man.archlinux.org/man/git-commit.1>)，而不是 [git(1)](<https://man.archlinux.org/man/git.1>)。 

###  持续 rehash

通常情况下，compinit 不会自动找到 `$PATH` 中的新可执行文件。例如，在安装了一个新包之后，`/usr/bin/` 目录下的文件不会立即或自动包含在补全列表中。因此，为了使这些新的可执行文件包含进来，可以运行以下命令： 
    
    $ rehash
    
可以让这个 rehash 自动发生。[[3]](<https://github.com/robbyrussell/oh-my-zsh/issues/3440>) 只需在你的 `zshrc` 文件中包含以下内容： 
    
    ~/.zshrc
    
    zstyle ':completion:*' rehash true
    
###  必要时 rehash

如上所述，但是可以通过配置 [pacman](<../zh-cn/Pacman.html> "Pacman") 使用[钩子](<../zh-cn/Pacman.html#%E9%92%A9%E5%AD%90> "Pacman")来自动请求 `rehash`，这不会像上面的持续 rehash 那样带来性能损失。要启用此功能，需要创建 `/etc/pacman.d/hooks` 目录和一个 `/var/cache/zsh` 目录，然后创建一个钩子文件： 
    
    /etc/pacman.d/hooks/zsh.hook
    
    [Trigger]
    Operation = Install
    Operation = Upgrade
    Operation = Remove
    Type = Path
    Target = usr/bin/*
    [Action]
    Depends = zsh
    When = PostTransaction
    Exec = /usr/bin/install -Dm644 /dev/null /var/cache/zsh/pacman

这样做的目的是保持文件 `/var/cache/zsh/pacman` 的修改日期与上次安装、升级或移除包的时间一致。然后，需要通过在你的 `~/.zshrc` 文件中添加以下内容来促使 `zsh` 在其命令缓存过期时 rehash： 
    
    ~/.zshrc
    
    zshcache_time="$(date +%s%N)"
    
    autoload -Uz add-zsh-hook
    
    rehash_precmd() {
      if [[ -a /var/cache/zsh/pacman ]]; then
        local paccache_time="$(date -r /var/cache/zsh/pacman +%s%N)"
        if (( zshcache_time < paccache_time )); then
          rehash
          zshcache_time="$paccache_time"
        fi
      fi
    }
    
    add-zsh-hook -Uz precmd rehash_precmd
    
如果在 `/var/cache/zsh/pacman` 被更新之前触发了 `precmd` 钩子，则补全可能不会生效，直到启动新的提示符为止。运行一个空命令（例如按 `enter`）应该是足够的。 

###  使用 SIGUSR1 的替代必要时 rehash 方法

如上所述，然而钩子文件看起来是这样的： 
    
    /etc/pacman.d/hooks/zsh-rehash.hook
    
    [Trigger]
    Operation = Install
    Operation = Upgrade
    Operation = Remove
    Type = Path
    Target = usr/bin/*
    
    [Action]
    Depends = zsh
    Depends = procps-ng
    When = PostTransaction
    Exec = /usr/bin/pkill zsh --signal=USR1

**警告：** 这会向所有正在运行的 `zsh` 实例发送 SIGUSR1。请注意，默认情况下 SIGUSR1 的行为是终止进程，所以当你第一次配置这个设置时，如果没有加载下面的 trap，所有用户的（包括登录 shell）所有正在运行的 `zsh` 实例将终止。
    
    ~/.zshrc
    
    TRAPUSR1() { rehash }
    
上面的 _trap 函数_ （function trap）可以用 _trap 列表_ （list trap） `trap 'rehash' USR1` 替换。参见 [zshmisc(1) § Trap Functions](<https://man.archlinux.org/man/zshmisc.1#Trap_Functions>) 了解不同类型的 trap 之间的区别。 

这种方法将即时对所有 `zsh` 实例进行 `rehash`，无需按下回车键来触发 `precmd`。 

###  ncurses 应用的快捷键绑定

将 ncurses 应用程序绑定到按键会导致无法交互。使用 `BUFFER` 变量使其工作。以下示例允许用户使用 `Alt+\` 打开 [ncmpcpp](<../zh-cn/Ncmpcpp.html> "Ncmpcpp"): 
    
    ~/.zshrc
    
    ncmpcppShow() {
    BUFFER="ncmpcpp"
    zle accept-line
    }
    zle -N ncmpcppShow
    bindkey '^[\' ncmpcppShow

另一种方法，它将保留您在调用应用程序之前在行中输入的所有内容: 
    
    ~/.zshrc
    
    ncmpcppShow() {
    ncmpcpp <$TTY
    zle redisplay
    }
    zle -N ncmpcppShow
    bindkey '^[\' ncmpcppShow

###  文件管理器的快捷键绑定

图形化文件管理器中使用快捷键可能很实用（译者注：你也可以在 Zsh 中自定义快捷键达到这样的效果）。第一个使用 `Alt+Left` 让用户撤销最近的 cd 操作，第二个使用 `Alt+Up` 让用户进入上层目录。这两个快捷键同时也会显示目录中的内容。 
    
    ~/.zshrc
    
    cdUndoKey() {
      popd      > /dev/null
      zle       reset-prompt
      echo
      ls
      echo
    }
    
    cdParentKey() {
      pushd .. > /dev/null
      zle      reset-prompt
      echo
      ls
      echo
    }
    
    zle -N                 cdParentKey
    zle -N                 cdUndoKey
    bindkey '^[[1;3A'      cdParentKey
    bindkey '^[[1;3D'      cdUndoKey
    
###  xterm 标题

如果您的终端仿真器支持，您可以从 Zsh 设置其标题。这允许动态更改标题以显示有关 shell 状态的相关信息，例如显示用户名和当前目录或当前正在执行的命令。 

xterm 标题使用 [xterm 控制序列操作系统命令](<https://www.tldp.org/HOWTO/Xterm-Title-3.html#ss3.1>) `\e]2;``\a` 或 `\e]2;``\e\\` 设置。例如： 
    
    $ print -n '\e]2;My xterm title\a'
    
将标题设置为 
    
    My xterm title
    
获得动态标题的一种简单方法是在 `precmd` 和 `preexec` 钩子函数中设置标题。有关可用钩子函数及其说明的列表，请参阅 [zshmisc(1) § Hook Functions](<https://man.archlinux.org/man/zshmisc.1#Hook_Functions>)。 

通过使用 `print -P`，您还可以利用 Zsh 的提示转义。 

**提示：**

  * 标题打印可以拆分为多个命令，只要它们是连续的即可。
  * [GNU Screen](<../zh-cn/GNU_Screen.html> "GNU Screen") 将 xterm 标题发送到硬状态 (`%h`)。如果您想使用 Screen 的 [字符串转义](<https://www.gnu.org/software/screen/manual/html_node/String-Escapes.html>)（例如用于颜色），您应该使用 `\e_``\e\\` 转义序列设置硬状态。否则，如果在 `\e]2;``\a` 中使用字符串转义，终端仿真器将获得乱码标题，因为它无法解释 Screen 的字符串转义。

**注意：**

  * 打印变量时不要使用 `print` 的 `-P` 选项，以防止它们被解析为提示转义符。
  * 打印变量时使用 `q` [参数扩展标志](<https://zsh.sourceforge.io/Doc/Release/Expansion.html#Parameter-Expansion-Flags>)，以防止它们被解析为转义序列。

    ~/.zshrc
    
    autoload -Uz add-zsh-hook
    
    function xterm_title_precmd () {
    	print -Pn -- '\e]2;%n@%m %~\a'
    	[[ "$TERM" == 'screen'* ]] && print -Pn -- '\e_\005{2}%n\005{-}@\005{5}%m\005{-} \005{+b 4}%~\005{-}\e\\'
    }
    
    function xterm_title_preexec () {
    	print -Pn -- '\e]2;%n@%m %~ %# ' && print -n -- "${(q)1}\a"
    	[[ "$TERM" == 'screen'* ]] && { print -Pn -- '\e_\005{2}%n\005{-}@\005{5}%m\005{-} \005{+b 4}%~\005{-} %# ' && print -n -- "${(q)1}\e\\"; }
    }
    
    if [[ "$TERM" == (Eterm*|alacritty*|aterm*|foot*|gnome*|konsole*|kterm*|putty*|rxvt*|screen*|wezterm*|tmux*|xterm*) ]]; then
    	add-zsh-hook -Uz precmd xterm_title_precmd
    	add-zsh-hook -Uz preexec xterm_title_preexec
    fi
    
####  终端仿真器选项卡标题

一些终端仿真器和多路复用器支持设置选项卡的标题。转义序列取决于终端： 

终端  | 转义序列  | 描述   
---|---|---  
[GNU Screen](<../zh-cn/GNU_Screen.html> "GNU Screen") |  `\ek``\e\\` | Screen 的窗口标题 (`%t`)。   
[Konsole](<../zh-cn/Konsole.html> "Konsole") |  `\e]30;``\a` | Konsole 的选项卡标题。   
  
###  Shell 环境检测

请参阅[有关 shell 环境检测的存储库](<https://gitlab.com/jdorel-documentation/shell-environment-detection>)以了解检测 shell 环境的测试。这包括登录/交互式 shell、Xorg 会话、TTY 和 SSH 会话。 

###  /dev/tcp 等效项：ztcp

使用 `zsh/net/tcp` 模块： 
    
    $ zmodload zsh/net/tcp
    
您现在可以建立 TCP 连接： 
    
    $ ztcp example.com 80
    
更多详细信息请参阅 [zshmodules(1) § THE_ZSH/NET/TCP_MODULE](<https://man.archlinux.org/man/zshmodules.1#THE_ZSH/NET/TCP_MODULE>) 和 [zshtcpsys(1)](<https://man.archlinux.org/man/zshtcpsys.1>)。 

###  在部分命令行上退出 shell 的快捷方式

默认情况下，如果命令行已填满，`Ctrl+d` 将不会关闭您的 shell，这可以修复它： 
    
    .zshrc
    
    exit_zsh() { exit }
    zle -N exit_zsh
    bindkey '^D' exit_zsh
    
###  pacman -F“未找到命令”处理程序

[pacman](<../zh-cn/Pacman.html> "Pacman") 包含搜索包含文件的包的功能。以下命令未找到处理程序将在执行未知命令时直接使用 pacman 搜索匹配的包。 
    
    ~/.zshrc
    
    ...
    function command_not_found_handler {
        local purple='\e[1;35m' bright='\e[0;1m' green='\e[1;32m' reset='\e[0m'
        printf 'zsh: 未找到命令：%s\n' "$1"
        local entries=(
            ${(f)"$(/usr/bin/pacman -F --machinereadable -- "/usr/bin/$1")"}
        )
        if (( ${#entries[@]} ))
        then
            printf "${bright}$1${reset} 可能位于以下软件包中：\n"
            local pkg
            for entry in "${entries[@]}"
            do
                # (存储库 软件包 版本 文件)
                local fields=(
                    ${(0)entry}
                )
                if [[ "$pkg" != "${fields[2]}" ]]
                then
                    printf "${purple}%s/${bright}%s ${green}%s${reset}\n" "${fields[1]}" "${fields[2]}" "${fields[3]}"
                fi
                printf '    /%s\n' "${fields[4]}"
                pkg="${fields[2]}"
            done
        fi
        return 127
    }
    ...

**注意：** pacman 的文件数据库与普通同步数据库是分开的，需要使用 `pacman -Fy` 来获取。详情请参阅 [pacman#搜索包含特定文件的包](<../zh-cn/Pacman.html#%E6%90%9C%E7%B4%A2%E5%8C%85%E5%90%AB%E7%89%B9%E5%AE%9A%E6%96%87%E4%BB%B6%E7%9A%84%E5%8C%85> "Pacman")。

有关使用 _pkgfile_ 的替代方法，请参阅 [#pkgfile“未找到命令”处理程序](<#pkgfile%E2%80%9C%E6%9C%AA%E6%89%BE%E5%88%B0%E5%91%BD%E4%BB%A4%E2%80%9D%E5%A4%84%E7%90%86%E7%A8%8B%E5%BA%8F>)。 

###  使用键绑定清除后缓冲区

默认情况下，清除屏幕键绑定不会清除大多数终端仿真器上的后缓冲区（您需要向上滚动才能看到的部分）。此问题的一个可能解决方案如下： 
    
    ~/.zshrc
    
    ...
    function clear-screen-and-scrollback() {
        printf '\x1Bc'
        zle clear-screen
    }
    
    zle -N clear-screen-and-scrollback
    bindkey '^L' clear-screen-and-scrollback
    ...

##  第三方扩展

###  配置框架

**注意：** 框架引入了一定程度的抽象和复杂性。它们可以并且经常会引入未定义的行为。如果 shell 出现故障，则“第一个”调试步骤应该是恢复到普通 shell。

  * **oh-my-posh** — Oh My Posh 是任何 shell 的自定义提示引擎，它能够使用函数或变量调整提示字符串。

     <https://github.com/JanDeDobbeleer/oh-my-posh> || [oh-my-posh](<https://aur.archlinux.org/packages/oh-my-posh/>)AUR

  * **oh-my-zsh** — 一个流行的、社区驱动的框架，用于管理您的 Zsh 配置。它捆绑了大量有用的函数、帮助程序、插件和主题。

     <https://github.com/ohmyzsh/ohmyzsh> || [oh-my-zsh-git](<https://aur.archlinux.org/packages/oh-my-zsh-git/>)AUR

  * **Prezto** — Zsh 的配置框架。它带有模块，通过合理的默认值、别名、函数、自动完成和提示主题丰富了命令行界面环境。

     <https://github.com/sorin-ionescu/prezto> || [prezto-git](<https://aur.archlinux.org/packages/prezto-git/>)AUR

  * **ZIM** — 具有极快速度和模块化扩展的配置框架。Zim 非常易于定制，并且带有一组丰富的模块和功能，而不会影响速度或功能。

     <https://github.com/zimfw/zimfw> || [zsh-zim-git](<https://aur.archlinux.org/packages/zsh-zim-git/>)AUR

###  插件管理器

  * **Antidote** — 功能齐全的 Zsh 旧版 Antibody 插件管理器实现。

     <https://github.com/mattmc3/antidote> || [zsh-antidote](<https://aur.archlinux.org/packages/zsh-antidote/>)AUR

  * **zinit（原“zplugin”)** — 灵活的 Zsh 插件管理器，具有干净的 fpath、报告、完成管理、涡轮模式 [REVIVED](<https://github.com/zdharma-continuum/I_WANT_TO_HELP>)

     <https://github.com/zdharma-continuum/zinit> || [zinit](<https://aur.archlinux.org/packages/zinit/>)AUR

  * **zi（原“zplugin”）** — zplugin 的替代分支，旨在扩展原始项目，而不是像 zinit 那样保存和维护原始项目。

     <https://github.com/z-shell/zi> || 未被打包？[在 AUR 里搜索](<https://aur.archlinux.org/packages/>)

  * **sheldon** — 快速、可配置的 shell 插件管理器，用 Rust 编写 [[4]](<https://github.com/rossmacarthur/sheldon>)

     <https://github.com/rossmacarthur/sheldon> || [sheldon](<https://archlinux.org/packages/?name=sheldon>)包

  * **Antigen** — Zsh 的插件管理器，灵感来自 oh-my-zsh 和 vundle。 [ABANDONED](<https://github.com/zsh-users/antigen/issues/673>)

     <https://github.com/zsh-users/antigen> || [antigen-git](<https://aur.archlinux.org/packages/antigen-git/>)AUR

  * **zgen** — Zsh 的轻量级和简单插件管理器。 [ABANDONED](<https://github.com/tarjoilija/zgen/issues/123>)

     <https://github.com/tarjoilija/zgen> || [zgen-git](<https://aur.archlinux.org/packages/zgen-git/>)AUR

  * **zplug** — Zsh 的下一代插件管理器。 [ABANDONED](<https://github.com/zplug/zplug/issues/403#issuecomment-477520784>)

     <https://github.com/zplug/zplug> || [zplug](<https://aur.archlinux.org/packages/zplug/>)AUR

###  仿 Fish 命令高亮

    译者注：Fish 是一款比较新的终端软件

[Fish](<../zh-cn/Fish.html> "Fish") 提供了非常强大的命令高亮。如果你希望在 zsh 中使用类似的功能，你可以安装 [zsh-syntax-highlighting](<https://archlinux.org/packages/?name=zsh-syntax-highlighting>)包、[zsh-autosuggestions](<https://archlinux.org/packages/?name=zsh-autosuggestions>)包，然后在你的 zshrc 中 [source](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#Source> "Source") 下面的两个脚本或其中之一： 
    
    source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
    source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
    
###  pkgfile“未找到命令”处理程序

[pkgfile](<../zh-cn/Pkgfile.html> "Pkgfile") 包含一个 Zsh 脚本文件，该文件提供了一个 `command_not_found_handler` 函数，该函数将在输入无法识别的命令时自动搜索 pkgfile 数据库。 

您需要 [source](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#Source> "Source") 该脚本才能启用它。例如： 
    
    ~/.zshrc
    
    source /usr/share/doc/pkgfile/command-not-found.zsh

**注意：** 可能需要更新 pkgfile 数据库才能正常工作。有关详细信息，请参阅 [pkgfile#安装](<../zh-cn/Pkgfile.html#%E5%AE%89%E8%A3%85> "Pkgfile")。

有关使用 pacman 本机功能的替代方法，请参阅 [#pacman -F“未找到命令”处理程序](<#pacman_-F%E2%80%9C%E6%9C%AA%E6%89%BE%E5%88%B0%E5%91%BD%E4%BB%A4%E2%80%9D%E5%A4%84%E7%90%86%E7%A8%8B%E5%BA%8F>)。 

##  卸载

在卸载 [zsh](<https://archlinux.org/packages/?name=zsh>)包 之前请先更换默认终端。 

**警告：** 如果不遵循下面的步骤可能会导致用户无法访问任何终端

运行下面的命令： 
    
    $ chsh -s /bin/bash _user_
    
每一个使用 _zsh_ 作为默认终端的用户都需要执行一遍条命令。当完成之后就可以把 [zsh](<https://archlinux.org/packages/?name=zsh>)包 软件包删除了。 

当然你也也可以以 root 身份修改 `/etc/passwd` 文件，来批量更改用户的默认终端。 

**警告：** 强烈建议使用 `vipw` 来修改 `/etc/passwd`，因为它可以帮助你消灭格式错误

例如将下面的配置中的 /bin/zsh 
    
    _username_ :x:1000:1000:_Full Name_ ,,,:/home/_username_ :/bin/zsh
    
改成 /bin/bash 
    
    _username_ :x:1000:1000:_Full Name_ ,,,:/home/_username_ :/bin/bash
    
##  另请参见

  * [zhwp:Zsh](<https://zh.wikipedia.org/wiki/Zsh> "zhwp:Zsh")
  * [An Introduction to the Z Shell](<https://zsh.sourceforge.io/Intro/intro_toc.html>)
  * [A User's Guide to ZSH](<https://zsh.sourceforge.io/Guide/zshguide.html>)
  * [The Z Shell Manual](<https://zsh.sourceforge.io/Doc/Release/index-frame.html>)（[可用的不同格式](<https://zsh.sourceforge.io/Doc/>)）
  * [Zsh FAQ](<https://zsh.sourceforge.io/FAQ/zshfaq01.html>)
  * [zsh-lovers(1)](<https://man.archlinux.org/man/zsh-lovers.1>)（可通过[zsh-lovers](<https://archlinux.org/packages/?name=zsh-lovers>)包使用）
  * [Gentoo: Zsh/Guide](<https://wiki.gentoo.org/wiki/Zsh/Guide> "gentoo:Zsh/Guide")
  * [Bash2Zsh Reference Card](<https://www.bash2zsh.com/zsh_refcard/refcard.pdf>)
