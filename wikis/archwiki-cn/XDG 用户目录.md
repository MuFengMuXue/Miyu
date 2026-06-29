**翻译状态：**

  * 本文（或部分内容）译自 [XDG user directories](<https://wiki.archlinux.org/title/XDG_user_directories> "arch:XDG user directories")，最近一次同步于 2024-11-16，若英文版本有所[更改](<https://wiki.archlinux.org/title/XDG_user_directories?diff=0&oldid=819357>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/XDG_user_directories_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")
  * [默认应用程序](<../zh-cn/%E9%BB%98%E8%AE%A4%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F.html> "默认应用程序")
  * [XDG 基本目录](<../zh-cn/XDG_%E5%9F%BA%E6%9C%AC%E7%9B%AE%E5%BD%95.html> "XDG 基本目录")
  * [xdg-menu](<../zh-cn/Xdg-menu.html> "Xdg-menu")

译自 [freedesktop.org](<https://www.freedesktop.org/wiki/Software/xdg-user-dirs/>)： 

     _xdg-user-dirs_ 是一个帮助管理用户常用目录（如桌面文件夹和音乐文件夹）的工具。它还处理这些文件夹名称的本地化（即翻译）。

    其工作原理是在登录阶段的早期运行 [xdg-user-dirs-update(1)](<https://man.archlinux.org/man/xdg-user-dirs-update.1>) 程序。该程序会读取一个配置文件和一组默认目录，然后在用户的主目录中创建这些目录的本地化版本，并在 `$XDG_CONFIG_HOME/user-dirs.dirs`（`XDG_CONFIG_HOME` 默认为 `~/.config`）中设置一个配置文件，供应用程序读取以找到这些目录。

大多数[文件管理器](<../zh-cn/%E6%96%87%E4%BB%B6%E7%AE%A1%E7%90%86%E5%99%A8%E5%8A%9F%E8%83%BD.html> "文件管理器功能")会使用特殊图标标识 XDG 用户目录。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [xdg-user-dirs](<https://archlinux.org/packages/?name=xdg-user-dirs>)包。 

**注意：** 某些[桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")可能已默认安装，例如 [GNOME](<../zh-cn/GNOME.html> "GNOME")。

##  创建默认目录

可以用以下命令在 `$HOME` 下创建一整套默认的经本地化的用户目录： 
    
    $ xdg-user-dirs-update
    
**提示：** 可以使用 `LC_ALL=C.UTF-8 xdg-user-dirs-update --force` 命令强制创建英文命名的目录。

运行后该命令还会自动地： 

  * 创建一个本地的 `~/.config/user-dirs.dirs` 配置文件：应用程序通过他来查找使用特定帐号指定的用户目录。
  * 创建一个本地的 `~/.config/user-dirs.locale` 配置文件：根据使用的 locale 指定语言。

用户服务 `xdg-user-dirs-update.service` 也将默认安装并启用，以便在每次登录会话开始时运行此命令，保持您的目录是最新的。 

##  创建自定义目录

本地 `~/.config/user-dirs.dirs` 和全局 `/etc/xdg/user-dirs.defaults` 配置文件使用以下环境变量格式指向用户目录：`XDG_DIRNAME_DIR="$HOME/directory_name"`。一个示例配置文件可能如下所示（这些都是模板目录）： 
    
    ~/.config/user-dirs.dirs
    
    XDG_DESKTOP_DIR="$HOME/桌面"
    XDG_DOCUMENTS_DIR="$HOME/文档"
    XDG_DOWNLOAD_DIR="$HOME/下载"
    XDG_MUSIC_DIR="$HOME/音乐"
    XDG_PICTURES_DIR="$HOME/图片"
    XDG_PUBLICSHARE_DIR="$HOME/公共"
    XDG_TEMPLATES_DIR="$HOME/模板"
    XDG_VIDEOS_DIR="$HOME/视频"

因为 [xdg-user-dirs](<https://archlinux.org/packages/?name=xdg-user-dirs>)包 会参照本地配置文件来了解正确的用户目录，所以可以自定义。比如若将 `~/.config/user-dirs.dirs` 下 `XDG_DOWNLOAD_DIR` 变量设为了 `$HOME/Internet`，那么任何参照了该变量的程序都会改用这个目录。 

**注意：** 和其他的配置文件一样，本地设定覆盖全局设定。另外自定义的目录要自己创建。

或者也可以用命令行修改默认目录。下列命令会产生和上面一样的效果： 
    
    $ xdg-user-dirs-update --set DOWNLOAD ~/Internet
    
##  查询配置好的目录

一旦设置完成，任何用户目录都可以通过 [xdg-user-dirs](<https://archlinux.org/packages/?name=xdg-user-dirs>)包 查看。例如，以下命令将显示 `Templates` 目录的位置，该目录当然对应于本地配置文件中的 `XDG_TEMPLATES_DIR` 变量： 
    
    $ xdg-user-dir TEMPLATES
    
**警告：**`xdg-user-dir` 不应从未经检查的输入中获取其参数，因为它会将参数直接传递给 `eval`，而不进行任何有效性检查，代码行如下： 
    
    eval echo \${XDG_${1}_DIR:-$HOME}
    
这意味着 `xdg-user-dir` 会从未经清理的输入中执行任意代码。除非上游修复了这个不安全的实现，否则 `xdg-user-dir` 应仅在使用硬编码或经过严格审核的参数时使用。
