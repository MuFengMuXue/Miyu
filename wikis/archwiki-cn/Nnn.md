相关文章

  * [文件管理器功能](<../zh-cn/%E6%96%87%E4%BB%B6%E7%AE%A1%E7%90%86%E5%99%A8%E5%8A%9F%E8%83%BD.html> "文件管理器功能")
  * [lf](<../zh-cn/Lf.html> "Lf")
  * [Midnight Commander](<../zh-cn/Midnight_Commander.html> "Midnight Commander")
  * [ranger](<../zh-cn/Ranger.html> "Ranger")
  * [Vifm](<../zh-cn/Vifm.html> "Vifm")

**翻译状态：**

  * 本文（或部分内容）译自 [Nnn](<https://wiki.archlinux.org/title/Nnn> "arch:Nnn")，最近一次同步于 2024-08-25，若英文版本有所[更改](<https://wiki.archlinux.org/title/Nnn?diff=0&oldid=815311>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Nnn_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[nnn](<https://github.com/jarun/nnn>)（也被样式化为 n³）是一个用 C 语言编写的便携式终端文件管理器。它可以通过扁平文本插件系统轻松扩展，在已有插件（包括 [(neo)vim](<https://github.com/mcchrish/nnn.vim>) 插件）的基础上添加自己的语言脚本。 

_nnn_ features native archiving/decompression to and from commonly installed formats such as _xz_ , disk usage analysis and a fuzzy app launcher, a batch file renamer and a file picker through its plugin architecture. _nnn_ supports instant _search-as-you-type_ with regex (or simple string) filters and a _navigate-as-you-type_ mode for continuous navigation in filter mode with directory auto-select. Also supported are contexts, bookmarks, multiple sorting options, SSHFS, batch operations on selections (a group of selected files) and a lot more. 

尽管 _nnn_ 功能强大，但其设计简单易用，可通过[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")进行配置，无需使用配置文件。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [nnn](<https://archlinux.org/packages/?name=nnn>)包 软件包，或 安装 [nnn-git](<https://aur.archlinux.org/packages/nnn-git/>)AUR 以获取开发版本。 

###  用法

_nnn_ 可以用类 _vi_ 按键 `hjkl` 或 `arrow keys` 控制。请勿记忆按键：箭头、`/` 和 `q` 即可。请随时按 `?` 获取键盘快捷键帮助。 

###  配置

_nnn_ 通过[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")进行配置。有关这些设置的详细信息，请参阅 [nnn(1)](<https://man.archlinux.org/man/nnn.1>) 以及 [nnn wiki](<https://github.com/jarun/nnn/wiki>)。 
    
    NNN_BMS='d:~/Documents;u:/home/user/Cam Uploads;D:~/Downloads/'
    NNN_SSHFS="sshfs -o follow_symlinks"        # make sshfs follow symlinks on the remote
    NNN_COLORS="2136"                           # use a different color for each context
    NNN_TRASH=1                                 # trash (needs trash-cli) instead of delete

**注意：** If you start _nnn_ via `nnn.desktop` from a desktop environment started from a [display manager](<../zh-cn/Display_manager.html> "Display manager"), `.bashrc` may not be sourced. In this case, see the upstream instructions for [desktop integration](<https://github.com/jarun/nnn/wiki/Advanced-use-cases#desktop-integration>).

`NNN_BMS` 变量是比较有用的设置之一，它可以让你选择快捷方式快速跳转到书签目录。您可以使用 `b` 后跟一个您指定的字母。在示例配置中，点击`bD`将导致 _nnn_ 跳转到`~/Downloads`。但所有这些都是可选的， _nnn_ 在所有机器上的表现都是一样的。 

####  在终端中获取选定文件

要获取在 _nnn_ 中选择的文件列表，可以创建以下别名： 
    
    ~/.bashrc
    
    alias ncp="cat ${NNN_SEL:-${XDG_CONFIG_HOME:-$HOME/.config}/nnn/.selection} | tr '\0' '\n'"

随后可将所选文件导入其他工具。 

#### Indicate depth level within nnn shells

If you use `!` to spawn a shell in the current directory, it could be nice to add: 
    
    ~/.bashrc
    
    [ -n "$NNNLVL" ] && PS1="N$NNNLVL $PS1"

To have your prompt indicate that you are within a shell that will return you to _nnn_ when you are done. 

This together with [#cd on quit (Ctrl-G)](<#cd_on_quit_\(Ctrl-G\)>) becomes a powerful combination. 

####  cd on quit (Ctrl-G)

Add the following to your `.bashrc`/`.zshrc`
    
    ~/.bashrc or ~/.zshrc
    
    if [ -f /usr/share/nnn/quitcd/quitcd.bash_sh_zsh ]; then
        source /usr/share/nnn/quitcd/quitcd.bash_sh_zsh
    fi

And run the `n` command instead of `nnn` (more precisely the n bash function). 

另请参阅 [nnn wiki](<https://github.com/jarun/nnn/wiki/Basic-use-cases#configure-cd-on-quit>)。 

####  添加自己的插件

您可以将插件放入 `${XDG_CONFIG_HOME:-$HOME/.config}/nnn/plugins` 中，以运行自己的插件。例如，您可以创建一个可执行的 shell 脚本 
    
    ${XDG_CONFIG_HOME:-$HOME/.config}/nnn/plugins/git-changes
    
    #!/usr/bin/env sh
    git log -p -- "$@"

设置[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量") `NNN_PLUG='R:git-changes'`，然后按 `;R` 键并选择 `git-changes` 来触发它，这样就能方便地显示特定文件的 git 更改日志以及代码，以便快速轻松地查看。 

##  参见

  * [nnn's 官方仓库](<https://github.com/jarun/nnn>)
  * [nnn 的附加配置指南](<https://github.com/jarun/nnn/wiki/Basic-use-cases>)
  * [nnnn 视频简介](<https://www.youtube.com/watch?v=U2n5aGqou9E>)
