**翻译状态：**

  * 本文（或部分内容）译自 [Nano](<https://wiki.archlinux.org/title/Nano> "arch:Nano")，最近一次同步于 2023-05-24，若英文版本有所[更改](<https://wiki.archlinux.org/title/Nano?diff=0&oldid=771545>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Nano_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[GNU nano](<https://www.nano-editor.org/>) （或 nano）是一个基于控制台的文本编辑器，旨在提供一个简单的界面和直观的命令选项。 _nano_ 支持的功能包括语法高亮、DOS/Mac 文件格式转换、拼写检查和[UTF-8](<https://en.wikipedia.org/wiki/UTF-8> "wikipedia:UTF-8")编码。 用空缓冲区打开的 _nano_ 通常占用少于4MB的驻留内存。 

##  安装

_Nano_ 对应的软件包是 [nano](<https://archlinux.org/packages/?name=nano>)包。 

##  配置

Nano的外观、感觉和功能通常由命令行参数或者配置文件`~/.config/nano/nanorc`控制。 

程序安装时会同时安装一个示例配置文件，位于`/etc/nanorc`。 要自定义配置，首先复制一份配置文件到`~/.config/nano/nanorc`： 
    
    $ cp /etc/nanorc ~/.config/nano/nanorc
    
通过设置`~/.config/nano/nanorc`文件中的参数控制nano的设置。 

**提示：**[nanorc(5)](<https://man.archlinux.org/man/nanorc.5>)列出nano的全部可用配置选项。

**注意：** 命令行参数会优先覆盖配置文件`~/.config/nano/nanorc`中的参数。

###  语法高亮

Nano包含预定义的[语法高亮](<https://en.wikipedia.org/wiki/Syntax_highlighting> "wikipedia:Syntax highlighting")规则，位于文件`/usr/share/nano/*.nanorc` 和 `/usr/share/nano/extra/*.nanorc`。 添加以下配置到`~/.config/nano/nanorc`或者`/etc/nanorc`使语法高亮生效： 
    
    include "/usr/share/nano/*.nanorc"
    include "/usr/share/nano/extra/*.nanorc"
    
可以在 AUR（[nano-syntax-highlighting-git](<https://aur.archlinux.org/packages/nano-syntax-highlighting-git/>)AUR）找到默认语法高亮规则的增强扩展。 参考[[1]](<https://paste.xinu.at/wc17YG/>)，用于[Forth](<https://en.wikipedia.org/wiki/Forth_\(programming_language\)> "w:Forth \(programming language\)")突出显示。 

**提示：** 您也可以安装 [nano-syntax-highlighting-git](<https://github.com/archlinuxcn/repo/tree/master/archlinuxcn/nano-syntax-highlighting-git>)[CNRepo](<../zh-cn/Arch_Linux_%E4%B8%AD%E6%96%87%E7%A4%BE%E5%8C%BA%E4%BB%93%E5%BA%93.html> "Arch Linux 中文社区仓库")。

#### PKGBUILD

  * 将 <https://paste.xinu.at/4ss/> （类似 [svntogit-server](<https://github.com/archlinux/svntogit-packages>)）保存到 `/etc/nano/pkgbuild.nanorc`，引用它：

    include "/etc/nano/pkgbuild.nanorc"
    
  * 还可以选择安装 [nano-syntax-highlighting-git](<https://aur.archlinux.org/packages/nano-syntax-highlighting-git/>)AUR

###  挂起

Nano与大部分交互程序不同，默认情况下关闭挂起功能。 取消`/etc/nanorc`中`set suspend`行的注释以启用挂起功能。 允许用按键`Ctrl+z`使nano挂起到后台。 

###  文本换行

_Nano_ 与大部分文本编辑器不同，默认文本自动换行。 要关闭自动换行，在`~/.config/nano/nanorc`添加以下参数： 
    
    set nowrap
    
##  使用

快捷键提示可以在 _nano_ 中看到。 Nano中可以用`Ctrl+g`打开在线帮助，[nano Command Manual](<https://www.nano-editor.org/dist/latest/nano.html>)可以查看详细说明和帮助。 

###  特殊按键

Nano在屏幕底部两行显示功能快捷键。 

表示方式如下： 

  * `^`表示按住键盘上的`Ctrl`
  * `M-`表示按住键盘上的 _`Meta`_ （通常是`Alt`）或`Esc`

**提示：**[Feature Toggles](<https://www.nano-editor.org/dist/latest/nano.html#Feature-Toggles>)列出nano全部可用快捷键。

##  提示和技巧

###  用nano替换vi

要用nano替换vi作为控制台默认文本编辑器，例如用于[visudo](<../zh-cn/Sudo.html#Using_visudo> "Sudo")，设置`VISUAL`和`EDITOR` [环境变量](<../zh-cn/Environment_variable.html#Defining_variables> "Environment variable")，示例： 
    
    export VISUAL=nano
    export EDITOR=nano
    
##  问题解决

###  快捷键绑定冲突

部分窗口管理器会与nano的快捷键冲突，例如`Alt+Enter`。 删除或重新绑定快捷键例如`Super`（用[mutter](<https://archlinux.org/packages/?name=mutter>)包、[muffin](<https://archlinux.org/packages/?name=muffin>)包和[marco](<https://archlinux.org/packages/?name=marco>)包修改[dconf](<https://archlinux.org/packages/?name=dconf>)包），然后重新启动窗口管理器。 

##  参考

  * [nano (text editor)](<https://en.wikipedia.org/wiki/Nano_\(text_editor\)> "wikipedia:Nano \(text editor\)") \- Wikipedia入口
  * [GNU nano Homepage](<https://www.nano-editor.org/>) \- 官方网页
  * [GNU nano Bugs](<https://savannah.gnu.org/bugs/?group=nano>) 报告bug
  * [Nano语法高亮文件扩展](<https://github.com/scopatz/nanorc>)
