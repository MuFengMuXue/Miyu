**翻译状态：**

  * 本文（或部分内容）译自 [Doas](<https://wiki.archlinux.org/title/Doas> "arch:Doas")，最近一次同步于 2022-11-27，若英文版本有所[更改](<https://wiki.archlinux.org/title/Doas?diff=0&oldid=757666>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Doas_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Users and groups](<../zh-cn/Users_and_groups.html> "Users and groups")
  * [sudo](<../zh-cn/Sudo.html> "Sudo")
  * [List of applications/Security#Privilege elevation](<../zh-cn/List_of_applications/Security.html#Privilege_elevation> "List of applications/Security")

[OpenDoas](<https://en.wikipedia.org/wiki/doas> "wikipedia:doas") 是 OpenBSD 的 doas 命令的移植版本，与 [sudo](<../zh-cn/Sudo.html> "Sudo") 相比，它以体积小而闻名。与 _sudo_ 一样， _doas_ 用于假定系统中另一个用户的身份。 

##  安装

安装 [opendoas](<https://archlinux.org/packages/?name=opendoas>)包。 

##  使用

要以非特权用户的身份开始使用 _doas_ ，必须对它进行适当配置。参见[#配置](<#%E9%85%8D%E7%BD%AE>)。 

要使用 _doas_ ，只需在命令及其参数前加上 `doas` 和一个空格： 
    
    $ doas _cmd_
    
例如，要使用 [pacman](<../zh-cn/Pacman.html> "Pacman")： 
    
    $ doas pacman -Syu
    
要进入具有 root 提示的交互式 shell： 
    
    $ doas -s
    
更多内容参见 [doas(1)](<https://man.archlinux.org/man/doas.1>)： 

##  配置

安装 OpenDoas 会附带 [PAM](<../zh-cn/PAM.html> "PAM") 模块，但没有包括默认配置或示例。 

为了允许 [wheel](</wzh/index.php?title=Wheel&action=edit&redlink=1> "Wheel（页面不存在）") 组的成员以其他用户的身份运行命令，请创建一份具有以下内容的配置文件： 
    
    /etc/doas.conf
    
    permit :wheel
    
**注意：** 配置文件必须以换行结束。

`/etc/doas.conf` 的所有者和组应均是 `0`，文件权限应设置为 `0400`： 
    
    # chown -c root:root /etc/doas.conf
    # chmod -c 0400 /etc/doas.conf
    
要检查 `/etc/doas.conf`是否存在语法错误，请运行： 
    
    # doas -C /etc/doas.conf && echo "config ok" || echo "config error" 
    
**警告：** 必须保证 `/etc/doas.conf` 没有语法错误！

允许 `plugdev` 组的成员作为[根用户](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E6%A6%82%E8%A7%88> "根用户")无需密码运行 [smartctl](</wzh/index.php?title=Smartctl&action=edit&redlink=1> "Smartctl（页面不存在）")。 
    
    /etc/doas.conf
    
    permit nopass :plugdev as root cmd /usr/bin/smartctl
    
`/etc/doas.conf` 的一般语法形式为： 
    
    permit|deny [options] identity [as target] [cmd command [args ...]]
    
更多细节请阅读 [doas.conf(5)](<https://man.archlinux.org/man/doas.conf.5>)。 

##  提示与技巧

###  doas 持久化

_doas_ 提供持久化支持：在用户成功认证后，在一段时间内不再要求输入密码。默认情况下是禁用的，用 `persist` 选项启用它： 
    
    /etc/doas.conf
    
    permit persist :wheel
    
**注意：** 持久化默认禁用，因为它比较新，有潜在的危险。在最初的 _doas_ 中，一个内核 API 被用来设置和清除超时。这个 API 是 OpenBSD 特有，其他操作系统上没有类似的 API。作为一种变通方法，持久化是使用类似于 _sudo_ 的时间戳文件实现。

###  从 sudo 平滑过渡到 doas

为了从 _sudo_ 平滑过渡到 _doas_ 并保持向下兼容，可以在环境中添加： 
    
    alias sudo='doas'
    alias sudoedit='doas rnano'
    
或者，将 _doas_ 链接到 _sudo_ 通常所在位置（但是它无法提供`sudoedit`命令）： 
    
    # ln -s $(which doas) /usr/bin/sudo
    
[doas-sudo-shim](<https://aur.archlinux.org/packages/doas-sudo-shim/>)AUR 或许可以帮您平滑过渡，可惜无法提供`sudoedit`命令。 

**注意：** 默认情况下 _sudo_ 会保留一些环境变量，而 _doas_ 不会，最明显的是 XAUTHORITY、LANG 和 LC_ALL。这意味着你将无法在 X 下启动图形应用程序，也无法在没有额外配置的情况下访问用户的区域设置。例如，要允许 _wheel_ 组的成员运行图形应用程序，并使用 setenv 访问用户的 locale： 
    
    /etc/doas.conf
    
    permit setenv { XAUTHORITY LANG LC_ALL } :wheel
    
###  Bash tab 补全

默认情况 Bash 只对当前或参考目录下的文件和目录进行 tab 补全。要让 Bash 像完成单独的命令一样完成参数（同时利用其他命令的 tab 补全设置），可以在用户的 `.bashrc` 或全局的 `/etc/bash.bashrc` 中添加以下内容： 
    
    ~/.bashrc
    
    complete -cf doas
    