dmenu是一个X下的快速、轻量级的软件启动器，它从stdin读取任意文本，并创建一个菜单，每一行都有一个菜单项。 然后，用户可以通过方向键或键入名称的一部分来选择一个项目，该行就会被输出到stdout。 dmenu_run是 dmenu 发行版附带的包装器，可将其用作应用程序启动器。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [dmenu](<https://archlinux.org/packages/?name=dmenu>)包，或者是开发者版本的 [dmenu-git](<https://aur.archlinux.org/packages/dmenu-git/>)AUR。 

通过以下命令来运行 _dmenu_ ： 
    
    $ dmenu_run
    
##  设置

现在你可以将此命令关联到一个快捷键，很多窗口管理器和桌面环境都有设置工具可以做到，用 [xbindkeys](</wzh/index.php?title=Xbindkeys&action=edit&redlink=1> "Xbindkeys（页面不存在）") 也可以做到，想得到更详细的信息参见 [Hotkeys](</wzh/index.php?title=Hotkeys&action=edit&redlink=1> "Hotkeys（页面不存在）") 条目。 

###  显示自定义项目

自定义项目可以通过用换行符(_\n_)来分隔并输入到 _dmenu_ 来让它们显示出来，比如： 
    
    $ echo -e "第一个\n第二个\n第三个" | dmenu
    
###  手动添加项目

_dmenu_ 会在你的 `$PATH` 路径下的目录里查找可执行文件并生成菜单项。如果要修改 `$PATH`，参见 [environment variables](<../zh-cn/Environment_variables.html> "Environment variables")。 

###  字体

dmenu 4.6 起 XFT 字体渲染默认启用（[4.6 发行注记](<https://lists.suckless.org/dev/1511/27503.html>)）。[fontconfig](<https://archlinux.org/packages/?name=fontconfig>)包的[font.conf 语法](<https://www.freedesktop.org/software/fontconfig/fontconfig-user.html>)会被使用。 

###  shell 别名支持

_dmenu_ 不支持 [shell 别名](<../zh-cn/Bash.html#Aliases> "Bash"). 为了让 _dmenu_ 能够识别别名，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") _dmenu-recent-aliases_ （已从AUR移除） 包然后运行 `dmenu_run_aliases`。 别名必须要在 `~/.bash_aliases` 或者 `~/.zsh_aliases` 文件里面来让 _dmenu_run_aliases_ 识别出来。 

##  延伸
    
    $ pacman -Ql dmenu | grep bin
    dmenu /usr/bin/dmenu
    dmenu /usr/bin/dmenu_path
    dmenu /usr/bin/dmenu_run
    
可见/usr/bin/下有三个文件，其中**dmenu_path** 和**dmenu_run** 是两个shell脚本，真正的执行/显示部分都由**dmenu** 完成，其中**dmenu_path** 用于列出$PATH里的可执行文件，每个文件名一行，然后通过“|”传递给**dmenu** ，具体语法可从**dmenu_run** 里找到。 你也可以在终端里执行： 
    
    $ echo | dmenu
    
然后输入任意字串，这个字串就会被显示在终端里，这其实才是dmenu的核心功能。 

由此配合其他工具可以完成其他任务，比如运行： 
    
    $ notify-send "`exec $(echo | dmenu)`"
    
你可以试着在运行后输入date，之后系统就会借助notify-send弹出日期提示。 

##  其他资源

  * [dmenu](<https://tools.suckless.org/dmenu>) \- dmenu官方网站
  * [Yeganesh](<http://dmwit.com/yeganesh>) \- dmenu的一个前段处理器，可以按照使用频率进行排序
  * [LinuxTOY](<https://linuxtoy.org/archives/dmenu.html>) \- dmenu运行后的效果图
