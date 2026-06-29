相关文章

  * [文件管理器功能](<../zh-cn/%E6%96%87%E4%BB%B6%E7%AE%A1%E7%90%86%E5%99%A8%E5%8A%9F%E8%83%BD.html> "文件管理器功能")
  * [Midnight Commander](<../zh-cn/Midnight_Commander.html> "Midnight Commander")
  * [nnn](<../zh-cn/Nnn.html> "Nnn")
  * [ranger](<../zh-cn/Ranger.html> "Ranger")
  * [Vifm](<../zh-cn/Vifm.html> "Vifm")

**翻译状态：**

  * 本文（或部分内容）译自 [lf](<https://wiki.archlinux.org/title/lf> "arch:lf")，最近一次同步于 2024-11-16，若英文版本有所[更改](<https://wiki.archlinux.org/title/lf?diff=0&oldid=820826>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/lf_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[lf](<https://github.com/gokcehan/lf?tab=readme-ov-file#lf>)（意为“list files”即“列出文件”）是一个用 [Go](<../zh-cn/Go.html> "Go") 编写的[终端文件管理器](<https://github.com/gokcehan/lf/wiki/FAQ#why-should-i-use-a-terminal-file-manager>)，受到 _ranger_ 的[强烈启发](<https://github.com/gokcehan/lf/wiki/FAQ#how-is-lf-different-than-ranger>)。 

其突出特点包括服务器/客户端架构（这样你可以在一个终端窗口中剪切，在另一个窗口中粘贴）以及高度可定制性。 

与 _ranger_ 不同的是， _lf_ [故意](<https://github.com/gokcehan/lf?tab=readme-ov-file#non-features>)将标签或窗口这样的功能排除在外，交给[窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")或[终端多路复用器](<../zh-cn/Category:%E7%BB%88%E7%AB%AF%E5%A4%9A%E8%B7%AF%E5%A4%8D%E7%94%A8%E5%99%A8.html> "Category:终端多路复用器")来处理。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [lf](<https://archlinux.org/packages/?name=lf>)包 或其开发版本 [lf-git](<https://aur.archlinux.org/packages/lf-git/>)AUR。 

##  配置

将默认配置文件从 `/usr/share/doc/lf/lfrc.example` 复制到 `~/.config/lf/lfrc`，作为进一步定制的模板。配置示例中的注释包含一些常见功能。 

更多详细配置请参见 [lf(1)](<https://man.archlinux.org/man/lf.1>)，也可参阅项目的 [wiki](<https://github.com/gokcehan/lf/wiki/>)。 

##  使用

默认键位绑定与 [vim](<../zh-cn/Vim.html> "Vim") 类似，与 _ranger_ 的默认设置有所不同，具体请参见 [lf(1) § QUICK REFERENCE](<https://man.archlinux.org/man/lf.1#QUICK_REFERENCE>)。 

另请参阅[录屏教程](<https://github.com/gokcehan/lf/wiki/Tutorial#basics>)。 

##  提示与技巧

###  从 _ranger_ 迁移到 _lf_

对于已经习惯使用 _ranger_ 作为文件管理器的用户，迁移到 _lf_ 意味着默认功能较少，行为略有不同。 

_lf_ 项目的 wiki 包括一个关于如何配置 _lf_ 来添加来自 _ranger_ 的功能和默认设置的逐步[指南](<https://github.com/gokcehan/lf/wiki/Ranger>)。 

###  使用 _rifle_ 打开文件

_lf_ 可以使用包含在 [ranger](<https://archlinux.org/packages/?name=ranger>)包 中的文件打开器 _rifle_ 。 

设置环境变量以自动使用 _rifle_ 在相关应用中打开文件： 
    
    export OPENER='rifle'
    
还可以设置默认编辑器： 
    
    export EDITOR='vim'
    
###  预览文件

要自动预览当前选中文件的内容，可以在 `~/.config/lf/lfrc` 中设置自定义预览脚本。来自 _ranger_ 的 `scope.sh` 脚本作为定制的良好模板，可以通过[添加包装器](<https://github.com/gokcehan/lf/wiki/Ranger#scope>)使用。还有许多其他[预览器](<https://github.com/gokcehan/lf/wiki/Previews>)可以与 _lf_ 一起使用。 

###  沙箱预览

默认的 _lf_ 配置仅预览文本文件，而使用更复杂的预览解析器存在一定风险。如果预览解析器（如 _pdftotext_ ）中存在漏洞，可以使用此简单脚本通过 [bubblewrap](<https://archlinux.org/packages/?name=bubblewrap>)包 将预览器沙箱化： 
    
    ~/.config/lf/previewSandbox.sh
    
    #!/bin/bash
    set -euo pipefail
    (
        exec bwrap \
         --ro-bind /usr/bin /usr/bin \
         --ro-bind /usr/share/ /usr/share/ \
         --ro-bind /usr/lib /usr/lib \
         --ro-bind /usr/lib64 /usr/lib64 \
         --symlink /usr/bin /bin \
         --symlink /usr/bin /sbin \
         --symlink /usr/lib /lib \
         --symlink /usr/lib64 /lib64 \
         --proc /proc \
         --dev /dev \
         --ro-bind /etc /etc \
         --ro-bind ~/.config ~/.config \
         --ro-bind ~/.cache ~/.cache \
         --ro-bind "$PWD" "$PWD" \
         --unshare-all \
         --new-session \
         bash ~/.config/lf/preview.sh "$@"
    )
    
将你的预览器设置为沙箱脚本，并将实际的预览脚本保存在 `~/.config/lf/preview.sh`： 
    
    set previewer ~/.config/lf/previewSandbox.sh
    