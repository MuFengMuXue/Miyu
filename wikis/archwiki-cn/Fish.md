**翻译状态：**

  * 本文（或部分内容）译自 [Fish](<https://wiki.archlinux.org/title/Fish> "arch:Fish")，最近一次同步于 2024-12-16，若英文版本有所[更改](<https://wiki.archlinux.org/title/Fish?diff=0&oldid=811412>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Fish_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[fish](<https://fishshell.com>)是“ _**f** riendly **i** nteractive **sh** ell_”的缩写，是一个“交互式的、对用户友好的[命令行shell](<../zh-cn/Command-line_shell.html> "Command-line shell")”。 

_fish_ 被有意设计成不完全与 [POSIX](<https://en.wikipedia.org/wiki/POSIX> "wikipedia:POSIX") 兼容。fish 的作者们认为 POSIX 中存在一些缺陷和矛盾，并通过 fish 简化的或不同的语法解决这些问题。因此，即使简单的 POSIX 兼容的脚本也可能需要较多的修改──甚至完全重写──才能在 fish 中运行。 

##  安装

安装 [fish](<https://archlinux.org/packages/?name=fish>)包 软件包。或者安装开发版的 [fish-git](<https://aur.archlinux.org/packages/fish-git/>)AUR。 

安装完成后，输入 `fish` 即可进入 fish shell。 

要查看帮助文档，在 fish 中输入 `help`，文档将会在浏览器中打开。建议用户至少读完文档中“Syntax overview”这一节内容，因为 fish 的语法和其他 shell 的并不一样。 

##  在系统中配置 fish

需要考虑的是：是把 fish 设置为默认 shell，也就是用户登录时直接进入的 shell，还是通过当前的默认 shell 启动 fish，并只在交互模式下使用 fish。这里，我们假设当前的默认 shell 是 [Bash](<../zh-cn/Bash.html> "Bash")。 

  * 把 fish 设为**默认shell** ：这种方式需要用户对 fish 的运行机制及其脚本语言有些基本的了解。用户需要把当前的初始化脚本和环境变量移动到 fish 的环境中。[#将 fish 设为默认 shell](<#%E5%B0%86_fish_%E8%AE%BE%E4%B8%BA%E9%BB%98%E8%AE%A4_shell>) 中有具体的步骤。
  * 只把 fish 用作**交互式shell** ：这种方法“破坏性”较小。Bash 会照常运行所有的初始化脚本，并在此基础上启动 fish。[#仅将 fish 用作交互式 shell](<#%E4%BB%85%E5%B0%86_fish_%E7%94%A8%E4%BD%9C%E4%BA%A4%E4%BA%92%E5%BC%8F_shell>) 中有具体的步骤。

###  将 fish 设为默认 shell

如果你决定把 fish 设为默认的 shell，首先你需要将你的用户的 shell 改为`/usr/bin/fish`。参照 [Command-line shell#Changing your default shell](<../zh-cn/Command-line_shell.html#Changing_your_default_shell> "Command-line shell") 中的步骤。 

下一步是把 Bash 的几个初始化脚本中的操作和配置用 fish 的方法和工具重写，这些脚本分别有`/etc/profile`、`~/.bash_profile`、`/etc/bash.bashrc`和`~/.bashrc`。 

需要特别关注的是，在登录到 fish 中后，你需要尽快检查、调整环境变量`$PATH`的内容。在 fish 中，`$PATH`是一个 _全局环境变量_ ： _全局_ 表示作用范围包含所有函数，并且会在重启的时候被清除； _环境变量_ 则意味着它对 fish 的所有子进程都是可见的。相较于修改直接修改 `$fish_user_path`，现在更推荐在配置文件中使用 [fish_add_path](<https://fishshell.com/docs/current/cmds/fish_add_path.html>) 来设置路径，比如 
    
    $ fish_add_path -p _/路径_1 /路径_2 /路径_3_
    
会将这三个路径添加到搜索路径的头部。 

###  仅将 fish 用作交互式 shell

如果不将 fish 设为默认 shell，就能照常运行 Bash 的初始化脚本。这能够保证用户当前的环境变量不受影响并且在 fish 中也能使用，因为 fish 是作为 Bash 的子进程运行的。下面是几种只把 fish 用作交互式 shell 的方法。 

####  通过 .bashrc 启动 fish

保持默认 shell 为 Bash 不变，然后添加`exec fish`到合适的 [Bash 配置文件](<../zh-cn/Bash.html#Configuration_files> "Bash")中，比如`.bashrc`。用这种方法，Bash 会正常执行`/etc/profile`和`/etc/profile.d`中的所有配置文件。相对于后面的几种方法，这种是最通用的，因为这种方法在本机计算机和 SSH 远程计算机上都能使用。 

**提示：**

  * 在这种配置下，如要使用 Bash 而不是接着启动 fish，需要使用`bash --norc`，以防止Bash加载`~/.bashrc`之后执行`exec fish`。
  * 要让类似于`bash -c 'echo test'`中的命令在 Bash 中执行而不是启动 fish，你可以将`exec fish`换为`if [ -z "$BASH_EXECUTION_STRING" ]; then exec fish; fi`。
  * 为让fish知晓其是否是一个登录shell，您可以在 `~/.bashrc` 检测登录 shell 状态，并给 fish 加上 `--login` 选项。 fish 的 shell 命令 `status` 可用于显示状态。
  * 在父进程不是 fish 的情况下才起动 fish：这种方法可以在更方便地切换到 Bash 的同时继续使用 `~/.bashrc` 中的配置。
        
        if [[ $(ps --no-header --pid=$PPID --format=comm) != "fish" && -z ${BASH_EXECUTION_STRING} && ${SHLVL} == 1 ]]
        then
        	shopt -q login_shell && LOGIN_OPTION='--login' || LOGIN_OPTION=''
        	exec fish $LOGIN_OPTION
        fi

####  使用终端模拟器的选项

另一种方法是在启动终端模拟器时通过添加命令行选项来启动fish。对于大部分的终端，这个选项是 `-e`。比如，要打开 gnome-terminal 并运行fish，可以将 gnome-terminal 的快捷方式改为： 
    
    gnome-terminal -e fish
    
对于不支持设置 shell 的终端模拟器，比如[lilyterm-git](<https://aur.archlinux.org/packages/lilyterm-git/>)AUR，则需要这样： 
    
    SHELL=/usr/bin/fish lilyterm
    
另外，有些终端可以在设置或配置文件中将 fish 设为默认 shell。 

####  使用终端复用器的选项

要将 fish 设为 [tmux](<../zh-cn/Tmux.html> "Tmux") 启动的默认 shell，在`~/.tmux.conf`中加入这行： 
    
    set-option -g default-shell "/usr/bin/fish"
    
当 _tmux_ 启动时，就会自动进入 fish。 

##  配置

fish的配置脚本保存在`~/.config/fish/config.fish`。这个文件与 `.bashrc`相似，当每次启动时，fish会执行这个文件中的命令。需要注意的是，如果需要设置长期保留的变量，应该将这个变量设为一个 _全局变量_ ，而不是将它定义在这些配置脚本中。 

用户定义的函数保存在`~/.config/fish/functions`中，文件名为` _函数名_.fish`。 

###  网页界面

可以在 fish 的交互式网页配置页面中修改配色、提示符、函数、变量、历史记录和快捷键： 
    
    $ fish_config
    
在 IPv6 被完全禁止的环境下，网页配置界面或许不能启动。参见[[1]](<https://github.com/fish-shell/fish-shell/issues/3857#issuecomment-281631629>) 和 [IPv6#Disable IPv6](<../zh-cn/IPv6.html#Disable_IPv6> "IPv6")。 

###  命令补全

fish 可以通过解析 man 的数据生成自动补全规则，这些自动补全规则被保存在`~/.config/fish/generated_completions/`。可以运行下面的命令自动更新补齐规则。 
    
    $ fish_update_completions
    
你也可以在 `~/.config/fish/completions/` 目录下放置自己定义的补全规则。`/usr/share/fish/completions/` 中有更多的例子。 

对 Arch Linux 来说， _pacman_ , _pacman-key_ , _makepkg_ , _pbget_ , _pacmatic_ 这些命令的自动补全规则已经在内置在 fish 中了，因为 fish 在开发的时候就包含了很多命令的补全规则。fish 的内存管理足够智能，不会因为命令补全产生负面影响。 

##  提示与技巧

###  命令替换

_fish_ 没有 Bash 式的历史记录替换功能（如 `sudo !!`）。fish 的开发者在 [fish faq](<https://fishshell.com/docs/current/faq.html#faq-history>) 中建议使用交互式的方式调用历史记录：`上`方向键可以按整条命令回顾历史，而`Alt+上`可以回顾命令的单个参数。`Alt+S` 会在整条命令的最前面加上 `sudo`。 

不过，[fish wiki](<https://github.com/fish-shell/fish-shell/wiki/Bash-Style-Command-Substitution-and-Chaining-\(!!-!$\)>) 中介绍了一些替代方法。虽然这些方法提供的历史替换功能并不完整，但可用的有 `!!`（替换上一条命令）和 `!$`（替换上一条命令的最后一个参数）。 

###  取消问候语

默认情况下，每次启动时 fish 都会打印问候语。如要不显示问候语，可以在 fish 中运行： 
    
    $ set -U fish_greeting
    
###  让 su 默认启动 fish

如果 _su_ 目标用户的默认 shell 是 Bash，但是你想使用 fish 作为 shell 的话，可以添加一个 `su` 函数覆盖默认的 _su_ 命令，在切换用户的时候自动使用 fish： 
    
    function su
        /bin/su --shell=/usr/bin/fish $argv
    end
    
###  登录 fish 时自动启动 X

把下面配置添加到 `~/.config/fish/config.fish`，即可在登录 tty1 的时候自动启动 X。 
    
    # Start X at login
    if status --is-login
        if test -z "$DISPLAY" -a $XDG_VTNR = 1
            exec startx -- -keeptty
        end
    end
    
如果在使用 fish 作为交互 shell，需要把例子中的 `is-login` 换为 `is-interactive`。 

###  在提示符中增加 git 状态

当你处在一个 git 目录中时，如果你想在 fish 的提示符中显示分支和修改的相关信息，可以仿照以下的例子编写 `fish_prompt` 函数： 
    
    ~/.config/fish/functions/fish_prompt.fish
    
    function fish_prompt
      set -l last_status $status
    
      if not set -q __fish_git_prompt_show_informative_status
        set -g __fish_git_prompt_show_informative_status 1
      end
      if not set -q __fish_git_prompt_color_branch
        set -g __fish_git_prompt_color_branch brmagenta
      end
      if not set -q __fish_git_prompt_showupstream
        set -g __fish_git_prompt_showupstream "informative"
      end
      if not set -q __fish_git_prompt_showdirtystate
        set -g __fish_git_prompt_showdirtystate "yes"
      end
      if not set -q __fish_git_prompt_color_stagedstate
        set -g __fish_git_prompt_color_stagedstate yellow
      end
      if not set -q __fish_git_prompt_color_invalidstate
        set -g __fish_git_prompt_color_invalidstate red
      end
      if not set -q __fish_git_prompt_color_cleanstate
        set -g __fish_git_prompt_color_cleanstate brgreen
      end
    
      printf '%s%s %s%s%s%s ' (set_color $fish_color_host) (prompt_hostname) (set_color $fish_color_cwd) (prompt_pwd) (set_color normal) (__fish_git_prompt)
    
      if not test $last_status -eq 0
        set_color $fish_color_error
      end
      echo -n '$ '
      set_color normal
    end
    
然而，fish 已经抛弃了这种方式，参见 [fish-shell git](<https://github.com/fish-shell/fish-shell/blob/master/share/functions/__fish_git_prompt.fish>)。作为替代，fish 现在内置了[Informative Git Prompt](<https://mariuszs.github.io/blog/2013/informative_git_prompt.html>)，该功能可以通过 `fish_config` 启用。 

###  在 SSH 中用彩色显示主机名

如果需要在通过 SSH 登录到 fish 时用不同的颜色标记提示符中的主机名，可以将以下内容添加到函数 `fish_prompt` 中，或者添加到 fish 的配置文件中。这里以红色为例： 
    
    ~/.config/fish/functions/fish_prompt.fish
    
    ...
    if set -q SSH_TTY
      set -g fish_color_host brred
    end
    ...
    
Note that the default fish prompt colors the hostname yellow when connected through SSH; additional modification to the prompt is not required for this functionality. 

###  ssh-agent 问题

在fish中，`eval (ssh-agent)` 会因为变量的设置方式而报错。一个变通的方案是使用 csh 风格的选项`-c`： 
    
    $ eval (ssh-agent -c)
    
###  "command not found" 事件函数

fish 包含了一个响应“命令未找到”（"command not found"）事件的函数 `fish_command_not_found`。当遇到一个当前系统不存在的命令时，这个函数会使用 [pkgfile](<https://archlinux.org/packages/?name=pkgfile>)包 在官方仓库中查找哪个软件包拥有这条命令，而如果 pkgfile 不存在则回落使用 `pacman -F` 作为替代。 

从 fish 3.2.2 开始，因为 `pacman -F` 严重的[卡顿问题](<https://github.com/fish-shell/fish-shell/issues/7841>)，所以 `fish_command_not_found` 不会再使用它作为回落。 

可以写一个 `fish_command_not_found` 函数来替换掉 fish 自带的。比如在“命令未找到”时只打印错误消息，这样就不会有卡顿现象： 
    
    $ function fish_command_not_found
          __fish_default_command_not_found_handler $argv[1]
      end
    
然后保存这个函数： 
    
    $ funcsave fish_command_not_found
    
###  从 jobs 中删除进程

当退出 _fish_ 的时候，所有后台进程也会终止。为了让一个任务即使在 fish 退出了之后也继续运行，需要先输入 `disown` 命令再退出。比如说，这个例子在后台起动 Firefox 然后 `disown` 它： 
    
    $ firefox &
    $ disown
    $ exit
    
这样即使退出了 fish，Firefox 也会继续运行。请查阅 _fish_ 的 disown(1) 了解更多细节。 

###  快速设置别名

如果想要快速设置一个持久化的别名（即使 fish 退出也不会失效），可以使用这种方法： 
    
    $ alias FooAliasName "foo --option"
    $ funcsave FooAliasName
    
而在 fish 3.0 之后的版本中，`alias` 增加了 `-s`/`--save` 选项。 
    
    $ alias -s FooAliasName "foo --option"
    
别名会自动保存，这样就不需要再执行 `funcsave`。如果想查看或者编辑所有的函数，可以运行 `fish_config`，然后在网页界面的 _Function_ 标签下进行配置。 

如要获取更多文档，查阅 [alias - create a function — fish-shell](<https://fishshell.com/docs/current/cmds/alias.html>)。 

###  Source /etc/profile on login

与 `bash` 不同，`fish` 在 tty 登录时不会加载 `/etc/profile`。如果你需要加载这个文件以获取在 `/etc/profile.d` 目录中追加和声明的环境变量，可以将以下内容添加到你的配置文件中： 
    
    ~/.config/fish/config.fish
    
    # 使用 bash 加载 /etc/profile
    if status is-login
    exec bash -c "test -e /etc/profile && source /etc/profile;\
    exec fish"
    end
    
这样，你可以在登录时使用 `fish` 作为你的登录 shell，同时仍然拥有通常在 `bash` 登录会话中所有的环境变量。 

##  另请参阅

  * <https://fishshell.com/> \- 主页
  * <https://fishshell.com/docs/current/> \- 文档
  * <https://hyperpolyglot.org/unix-shells> \- Shell 语法对照表（Shell 的“罗塞塔石碑“）
  * <https://github.com/fish-shell/fish-shell> \- fish 的 GitHub 仓库
