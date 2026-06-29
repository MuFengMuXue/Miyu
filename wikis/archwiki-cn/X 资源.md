相关文章

  * [X Logical Font Description](</wzh/index.php?title=X_Logical_Font_Description&action=edit&redlink=1> "X Logical Font Description（页面不存在）")
  * [dotfiles](<../zh-cn/Dotfiles.html> "Dotfiles")

**翻译状态：**

  * 本文（或部分内容）译自 [X resources](<https://wiki.archlinux.org/title/X_resources> "arch:X resources")，最近一次同步于 2024-8-1，若英文版本有所[更改](<https://wiki.archlinux.org/title/X_resources?diff=0&oldid=813650>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/X_resources_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** 请提供模板的第一个位置参数以更详细的指示。（在 [Talk:X 资源#](<../zh-cn/Talk:X_%E8%B5%84%E6%BA%90.html>) 中讨论）

_**X 资源**_ **文件** 是一个用户级配置 _点文件_ ，通常位于 `~/.Xresources`。 它可用于设置[X 资源](<https://en.wikipedia.org/wiki/X_resources> "wikipedia:X resources")，即 X 客户端程序的配置参数。 

除其他用途外，它们可用于： 

  * 配置终端首选项（如终端颜色）
  * 设置 DPI、抗锯齿、hinting 和其他 X 字体设置
  * 更改 [Xcursor 主题](<../zh-cn/%E5%85%89%E6%A0%87%E4%B8%BB%E9%A2%98.html> "光标主题")
  * 主题 [XScreenSaver](<../zh-cn/XScreenSaver.html> "XScreenSaver")
  * 配置低级 X 应用程序，如 [xorg-xclock](<https://archlinux.org/packages/?name=xorg-xclock>)包、[xpdf](<https://archlinux.org/packages/?name=xpdf>)包、[rxvt-unicode](<../zh-cn/Rxvt-unicode.html> "Rxvt-unicode"))

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [xorg-xrdb](<https://archlinux.org/packages/?name=xorg-xrdb>)包 软件包来获得 _X 服务器资源数据库工具_ ，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [xorg-docs](<https://archlinux.org/packages/?name=xorg-docs>)包 来获得 X.org 文档。 

## Configuration

[X(7) § RESOURCES](<https://man.archlinux.org/man/X.7#RESOURCES>) and [XrmGetDatabase(3) § FILE SYNTAX](<https://man.archlinux.org/man/XrmGetDatabase.3#FILE_SYNTAX>) provide detailed information on _X resources_ mechanism and file syntax. 

`~/.Xresources` is a conventional file name, `xrdb` does not claim it. You can use any other file names, like `~/.config/X11/Xresources` and `~/.config/X11/Xresources.d/_application-name_` (also see [#Samples](<#Samples>) and [#Include files](<#Include_files>)). 

### Basic syntax

The syntax of an _X resources_ file is a sequence of _resource lines_ as follows: 
    
    application_name.Class.resourceName: value
          application_name.resourceName: value
                     Class.resourceName: value
          application_name*resourceName: value
                          *resourceName: value
    
`application_name` and `Class` substrings will never contain a dot (`.`), the `resourceName` substring may contain a dot. For example, `Dialog.bodyFont` is a [XScreenSaver](<../zh-cn/XScreenSaver.html> "XScreenSaver") internal resource that is specified to set the body font and fallback font: 
    
    xscreensaver-auth.default.Dialog.bodyFont: times new roman 12, dejavu serif 12
    
application_name
    The name of the application, such as `urxvt`, `xpdf`, `xterm`, etc. Also may be called the _instance name_.

Class
    The classification used to group resources together. Class names are typically uppercase.

resourceName
    The name of the resource whose value is to be set. Resources are typically lowercase with uppercase concatenation.

value
    The actual value of the resource. This can be one of three types: 

  * Integer (whole numbers)
  * Boolean (true/false, yes/no, on/off)
  * String (a string of characters) — for example a word (`white`), a color (`#ffffff`), or a path (`/usr/bin/firefox`)

delimiters

  * A dot (`.`) is a _tight binding_ and is used to separate immediately adjacent components (in other words, to signify each step down into the hierarchy) — in the above example we start at application name, then descend into Class, and finally into the resource itself.
  * An asterisk (`*`) is a _loose binding_ and is used to represent any number of components, including none.
  * A colon (`:`) is used to separate the resource name from the value.

**注意：**

  * From resource file syntax point of view, everything before a colon (`:`) is a resource name. From the user perspective, we often call _resource_ only the rightmost component. In other words, _resource name_ is a string consisted of _application name_ , _Class_ and _resource name_ substrings. That might be the source of confusion.
  * Resource naming schema is totally application-dependent. While one application might use `application_name.Class.resourceName`, another might understand `application_name.resourceName` and `Class.resourceName` only.

### Wildcard matching

Question mark (`?`) and asterisk (`*`) can be used as wildcards, making it easy to write a single rule that can be applied to many different applications or elements. `?` is used to match any single component name, while `*` is used to represent any number of intervening components including none. 

Using the previous example, if you want to apply the same font to all programs (not just XScreenSaver) that contain the class name `Dialog` which contains the resource name `headingFont`, you could write: 
    
    **?**.Dialog.headingFont:     -*-fixed-bold-r-*-*-*-100-*-*-*-*-iso8859-1
    
If you want to apply this same rule to all programs that contain the resource `headingFont`, regardless of its class, you could write: 
    
    ***** headingFont:    -*-fixed-bold-r-*-*-*-100-*-*-*-*-iso8859-1
    
**注意：**

  * Question mark (`?`) is like component name, so _binding character_ — dot (`.`) or asterisk (`*`) — next to it is required.
  * Asterisk (`*`) is a _binding character_ itself, there is no need in placing dot next to it, and a sequence of dot(s) and asterisk(s) is replaced with a single asterisk during file processing.

See [XrmGetResource(3) § MATCHING RULES](<https://man.archlinux.org/man/XrmGetResource.3#MATCHING_RULES>) for more information. 

### Comments

Lines starting with an exclamation mark (`!`) are ignored, for example: 
    
    ! The following rule will be ignored because it has been commented out
    !Xft.antialias: true
    
**注意：**

  * The exclamation mark must be the first character on the line.
  * If you have a [C preprocessor](<https://en.wikipedia.org/wiki/C_preprocessor> "wikipedia:C preprocessor"), such as [GNU CPP](<https://gcc.gnu.org/onlinedocs/cpp/>) ([gcc](<https://archlinux.org/packages/?name=gcc>)包), installed you can use [C](<../zh-cn/C.html> "C")-style (`//` and `/* … */`) comments (also see [#Samples](<#Samples>)).

### Include files

To spread resource configuration across multiple files (e.g. to use its own file for each application), use _C preprocessor_ `#include` _directive_ : 
    
    ~/.config/X11/Xresources
    
    #include "Xresources.d/fonts"
    #include "Xresources.d/rxvt-unicode"
    #include "Xresources.d/xscreensaver"
    #include "Xresources.d/xterm"
    
If files that are referenced with _#include_ are not reachable from the applied configuration file directory, you need to pass a directory to search for: 
    
    $ xrdb -load -I _${HOME}/.config/X11 ~/.Xresources_
    
### Default settings

To see the default settings for your installed X11 applications, look in `/usr/share/X11/app-defaults/`. 

Detailed information on program-specific resources is usually provided in the man page for the program. [xterm(1) § RESOURCES](<https://man.archlinux.org/man/xterm.1#RESOURCES>) is a good example, as it contains a list of X resources and their default values. 

To see the currently loaded resources: 
    
    $ xrdb -query -all
    
### Samples

  * [Color output in console#Terminal emulators](<../zh-cn/Color_output_in_console.html#Terminal_emulators> "Color output in console")
  * [Cursor themes#X resources](<../zh-cn/Cursor_themes.html#X_resources> "Cursor themes")
  * [Font configuration#Applications without fontconfig support](<../zh-cn/Font_configuration.html#Applications_without_fontconfig_support> "Font configuration")
  * [rxvt-unicode#Configuration](<../zh-cn/Rxvt-unicode.html#Configuration> "Rxvt-unicode")
  * [xpdf(1) § OPTIONS](<https://man.archlinux.org/man/xpdf.1#OPTIONS>)
  * [Xterm#Configuration](</wzh/index.php?title=Xterm&action=edit&redlink=1> "Xterm（页面不存在）")
  * [klassiker (mrdotx)](<https://github.com/mrdotx/dotfiles/tree/master/.config/X11>) — [Rxvt-unicode](<../zh-cn/Rxvt-unicode.html> "Rxvt-unicode") patch developer [dotfiles](<../zh-cn/Dotfiles.html> "Dotfiles")

##  用法

###  加载资源文件

资源存储在 X 服务器中，因此只需读取一次。 _远程_ X11 客户端（如[通过 SSH 转发](<../zh-cn/OpenSSH.html#X11_%E8%BD%AC%E5%8F%91> "OpenSSH")）也可以访问这些资源。 

加载资源文件（如传统的 `.Xresources`），替换任何当前设置： 
    
    $ xrdb _~/.Xresources_
    
加载资源文件，并与当前设置合并： 
    
    $ xrdb -merge _~/.Xresources_
    
**注意：**

  * 大多数[显示管理器](<../zh-cn/%E6%98%BE%E7%A4%BA%E7%AE%A1%E7%90%86%E5%99%A8.html> "显示管理器")会在登录时加载 `~/.Xresources` 文件。
  * X11 程序启动时会读取较旧的 `~/.Xdefaults` 文件，但前提是当前会话中未使用过 _xrdb_ 。[[1]](<https://groups.google.com/forum/#!msg/comp.windows.x/hQBEdql8l-Q/hF3DETcIHGwJ>)

### xinitrc

如果使用默认的 [xinitrc](<../zh-cn/Xinit.html#xinitrc> "Xinitrc") 副本作为 `.xinitrc` ，它已经合并了 `~/.Xresources`。 

如果您使用的是自定义的，请添加： 
    
    .xinitrc
    
    [[ -f ~/.Xresources ]] && xrdb -merge -I$HOME ~/.Xresources

**注意：** 请勿在 `~/.xinitrc` 中设置 xrdb 命令的后台。否则，在 xrdb 之后启动的程序可能会在加载完成前查找资源。

###  获取资源值

如果要获取某个资源的值（例如在 bash 脚本中使用），可以使用 [xgetres](<https://aur.archlinux.org/packages/xgetres/>)AUR： 
    
    $ xgetres xscreensaver.Dialog.headingFont
    -*-fixed-bold-r-*-*-*-100-*-*-*-*-iso8859-1
    
## Troubleshooting

### Parsing errors

[Display manager](<../zh-cn/Display_manager.html> "Display manager")s such as [GDM](<../zh-cn/GDM.html> "GDM") may use the `--nocpp` argument for _xrdb_. 

### No output from xrdb -query

It is not rare for `xrdb -query` to output nothing. Try following [#Load resource file](<#Load_resource_file>) and [#xinitrc](<#xinitrc>) from above. And note some of the files mentioned there could be empty. 

##  参见

  * [Using the .Xdefaults File](<https://engineering.purdue.edu/ECN/Support/KB/Docs/UsingTheXdefaultsFil>) 由 Purdue Engineering Computer Network 提供
  * [Overlooked Points of X Resources](<https://unix.stackexchange.com/questions/216723/xterm-or-xterm-in-configuration-file/292992#292992>) 由 Thomas Dickey 提供
