相关文章

  * [桌面项](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%A1%B9.html> "桌面项")
  * [桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")
  * [窗口管理器](<../zh-cn/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8.html> "窗口管理器")
  * [默认应用程序](<../zh-cn/%E9%BB%98%E8%AE%A4%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F.html> "默认应用程序")
  * [xdg-utils](<../zh-cn/Xdg-utils.html> "Xdg-utils")

**翻译状态：**

  * 本文（或部分内容）译自 [XDG MIME Applications](<https://wiki.archlinux.org/title/XDG_MIME_Applications> "arch:XDG MIME Applications")，最近一次同步于 2024-11-16，若英文版本有所[更改](<https://wiki.archlinux.org/title/XDG_MIME_Applications?diff=0&oldid=820784>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/XDG_MIME_Applications_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[XDG MIME 应用程序规范](<https://specifications.freedesktop.org/mime-apps-spec/latest/>)基于[#共享 MIME 数据库](<#%E5%85%B1%E4%BA%AB_MIME_%E6%95%B0%E6%8D%AE%E5%BA%93>)和[桌面项](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%A1%B9.html> "桌面项")，提供[默认应用程序](<../zh-cn/%E9%BB%98%E8%AE%A4%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F.html> "默认应用程序")。 

  1. 应用程序通过[桌面项](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%A1%B9.html> "桌面项")描述它们能够处理哪些 MIME 类型。
  2. [desktop-file-utils](<https://archlinux.org/packages/?name=desktop-file-utils>)包 注册了一个 [pacman 钩子](<../zh-cn/Pacman_%E9%92%A9%E5%AD%90.html> "Pacman 钩子")，用于构建由桌面项处理的 MIME 类型的缓存数据库，详见 [update-desktop-database(1)](<https://man.archlinux.org/man/update-desktop-database.1>)。
  3. 应用程序可以通过将 XML 文件放置在 `/usr/share/mime/packages/` 中来安装新的 MIME 类型。
  4. [shared-mime-info](<https://archlinux.org/packages/?name=shared-mime-info>)包 注册了一个 [pacman 钩子](<../zh-cn/Pacman_%E9%92%A9%E5%AD%90.html> "Pacman 钩子")，用于构建共享 MIME 信息数据库缓存，详见 [update-mime-database(1)](<https://man.archlinux.org/man/update-mime-database.1>)。
  5. [桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")和用户可以通过 [mimeapps.list](<#mimeapps.list>) 文件更改默认应用程序并添加或删除 MIME 类型与应用程序的关联。

##  共享 MIME 数据库

[XDG 共享 MIME 信息数据库规范](<https://specifications.freedesktop.org/shared-mime-info-spec/latest/>)促进了桌面环境之间的共享 MIME 数据库，并允许应用程序轻松地在系统范围内注册新的 MIME 类型。 

该数据库是由软件包在 `/usr/share/mime/packages/` 中安装的 XML 文件构建的，使用来自 [shared-mime-info](<https://archlinux.org/packages/?name=shared-mime-info>)包 的工具。 

`/usr/share/mime/` 中的文件不应直接编辑，但可以在 `~/.local/share/mime/` 树中为每个用户维护单独的数据库。 

“URI 方案处理 [...] 通过处理 `x-scheme-handler/foo` MIME 类型的应用程序来进行，其中 foo 是相关的 URI 方案。”[[1]](<https://specifications.freedesktop.org/shared-mime-info-spec/latest/ar01s02.html#id-1.3.18>)

###  新的 MIME 类型

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 将扩展名分配给现有 MIME 类型的过程是否不同？ (在 [Talk:XDG MIME 应用程序](<../zh-cn/Talk:XDG_MIME_%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F.html>) 中讨论)

此示例定义了一个新的 MIME 类型 `application/x-foobar`，并将其分配给任何以 _.foo_ 结尾的文件。只需创建以下文件： 
    
    ~/.local/share/mime/packages/application-x-foobar.xml
    
    <?xml version="1.0" encoding="UTF-8"?>
    <mime-info xmlns="http://www.freedesktop.org/standards/shared-mime-info">
        **< mime-type type="application/x-foobar">**
            <comment>foo 文件</comment>
            <icon name="application-x-foobar"/>
            <glob-deleteall/>
            **< glob pattern="*.foo"/>**
        </mime-type>
    </mime-info>

然后更新 MIME 数据库： 
    
    $ update-mime-database ~/.local/share/mime
    
当然，如果没有桌面条目与 MIME 类型关联，这不会产生任何效果。您可能需要创建新的[桌面项](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%A1%B9.html> "桌面项")或修改 [mimeapps.list](<#mimeapps.list>)。 

## mimeapps.list

[XDG 标准](<https://specifications.freedesktop.org/mime-apps-spec/latest/>)是配置桌面环境最常用的方式。每个 MIME 类型的默认应用程序存储在 `mimeapps.list` 文件中，该文件可以存储在多个位置。它们按照以下顺序搜索，前面的关联优先于后面的关联： 

路径 | 用途   
---|---  
`~/.config/mimeapps.list` | 用户覆盖   
`/etc/xdg/mimeapps.list` | 系统范围的覆盖   
`~/.local/share/applications/mimeapps.list` |  **（已废弃）** 用户覆盖   
`/usr/local/share/applications/mimeapps.list`  
`/usr/share/applications/mimeapps.list` | 分发提供的默认值   
  
此外，还可以在名为 `_桌面环境_ -mimeapps.list` 的文件中定义 [desktop environment](<../zh-cn/Desktop_environment.html> "Desktop environment") 特定的默认应用程序，其中 `_桌面环境_` 是桌面环境的名称（来自 `XDG_CURRENT_DESKTOP` 环境变量）。例如，`/etc/xdg/xfce-mimeapps.list` 定义了 [Xfce](<../zh-cn/Xfce.html> "Xfce") 的系统范围默认应用程序覆盖。这些特定桌面的覆盖优先于相应的非特定桌面文件。例如，`/etc/xdg/xfce-mimeapps.list` 优先于 `/etc/xdg/mimeapps.list`，但仍会被 `~/.config/mimeapps.list` 覆盖。 

**提示：** 虽然已废弃，但许多应用程序仍然读写 `~/.local/share/applications/mimeapps.list`。为了简化维护，可以将其符号链接到 `~/.config/mimeapps.list`： 
    
    $ ln -s ~/.config/mimeapps.list ~/.local/share/applications/mimeapps.list

**注意：** 您还可能会在这些位置找到名为 `defaults.list` 的文件。此文件类似于 `mimeapps.list`，但仅列出默认应用程序（而不是已添加/删除的关联）。它现在已废弃，应手动与 `mimeapps.list` 合并。

要发现所有被扫描的文件，可以通过设置环境变量 `XDG_UTILS_DEBUG_LEVEL=2` 启用调试模式：例如，`xdg-mime query default _类型_` 命令将打印它搜索 MIME 信息的每个配置文件。 

###  格式

考虑以下示例： 
    
    mimeapps.list
    
    [Added Associations]
    image/jpeg=bar.desktop;baz.desktop
    video/H264=bar.desktop
    [Removed Associations]
    video/H264=baz.desktop
    [Default Applications]
    image/jpeg=foo.desktop

每个部分将一个或多个桌面条目分配给 MIME 类型。 

  * **Added Associations** 表示应用程序支持打开该 MIME 类型。例如，`bar.desktop` 和 `baz.desktop` 可以打开 JPEG 图像。这可能会影响您在文件浏览器中右键点击文件时看到的应用程序列表。
  * **Removed Associations** 表示应用程序**不** 支持该 MIME 类型。例如，`baz.desktop` 无法打开 H.264 视频。
  * **Default Applications** 表示该应用程序应为打开该 MIME 类型的默认选择。例如，JPEG 图像应使用 `foo.desktop` 打开。这隐式地在应用程序和 MIME 类型之间添加了一个关联。如果有多个应用程序，它们会按顺序尝试。

每个部分都是可选的，如果不需要可以省略。 

##  工具

虽然可以通过直接编辑 [mimeapps.list](<#mimeapps.list>) 和[#共享 MIME 数据库](<#%E5%85%B1%E4%BA%AB_MIME_%E6%95%B0%E6%8D%AE%E5%BA%93>)来配置默认应用程序和 MIME 类型，但有许多工具可以简化这一过程。这些工具也很重要，因为应用程序可能将文件的打开委托给这些工具，而不是自己尝试实现 MIME 类型标准。 

如果您使用的是[桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境")，应首先检查它是否提供了自己的工具。应该优先使用这些工具，而不是其他替代方案。 

官方的 [xdg-utils](<../zh-cn/Xdg-utils.html> "Xdg-utils") 包含用于根据 XDG 标准管理 MIME 类型和默认应用程序的工具（[xdg-mime](<../zh-cn/Xdg-utils.html#xdg-mime> "Xdg-utils")）。最重要的是，它提供了 [xdg-open](<../zh-cn/Xdg-utils.html#xdg-open> "Xdg-open")，许多应用程序用它来用默认应用程序打开文件。 

### lsdesktopf

[lsdesktopf](<https://aur.archlinux.org/packages/lsdesktopf/>)AUR 提供了几种搜索 MIME 数据库和桌面 MIME 条目的方法。 

例如，要查看系统中所有与 MIME 类型 `video` 相关联的 _.desktop_ 文件的 MIME 扩展名，可以使用 `lsdesktopf --gm -gx video`，或要在 XML 数据库文件中搜索，请使用 `lsdesktopf --gdx -gx video`。要快速了解有多少个且哪些 _.desktop_ 文件可以与某个 MIME 类型关联，请使用 `lsdesktopf --gen-mimeapps`。要查看 XML 数据库文件中的所有文件名扩展名，可以使用 `lsdesktopf --gdx -gfx`。 

### selectdefaultapplication

[selectdefaultapplication-git](<https://aur.archlinux.org/packages/selectdefaultapplication-git/>)AUR 是一个 GUI 应用程序，列出了所有支持各种 MIME 类型的应用程序，并允许您快速将其设置为所有或一些它支持的 MIME 类型的默认应用程序（通过修改 `mimeapps.list`）。 

它还显示了“可读”的名称和文件扩展名，因此您不需要记住 MIME 类型的名称。 

##  故障排除

如果文件未通过您期望的默认应用程序打开，可能有多个原因。您可能需要检查每种情况。 

###  缺少桌面条目

需要一个[桌面项](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%A1%B9.html> "桌面项")来将应用程序与 MIME 类型关联。确保存在这样的条目，并且可以用它来（手动）打开文件。 

###  缺少关联

如果应用程序的桌面条目没有在其 `MimeType` 键下指定 MIME 类型，它在需要打开该类型时将不会被考虑。编辑 [mimeapps.list](<#mimeapps.list>)，将桌面文件与 MIME 类型关联起来。 

###  非默认应用程序

如果桌面条目已与 MIME 类型关联，可能只是没有设置为默认值。编辑 [mimeapps.list](<#mimeapps.list>)，将其设置为默认关联。 

###  非标准关联

应用程序可以忽略或仅部分实现 XDG 标准。检查是否使用了已废弃的文件，如 `~/.local/share/applications/mimeapps.list` 和 `~/.local/share/applications/defaults.list`。如果您尝试从其他应用程序（如 Web 浏览器或文件管理器）打开文件，请检查该应用程序是否有自己的方法来选择默认应用程序。 

###  .desktop 文件中影响应用程序启动的变量

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 此处暗示了 `MimeType` 条目缺失的情况（“即使一个包含必要 MIME 类型描述的应用程序⋯⋯”），尽管这是常见的错误原因。有些启动器可能还会关联在桌面文件中未显式列出的 MIME 类型（例如 [exo](<https://archlinux.org/packages/?name=exo>)包）。其他环境特定的因素也在起作用，例如 `Terminal=true` 是否会产生影响，尽管后者应当在[桌面项](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%A1%B9.html> "桌面项")中进一步扩展。 (在 [Talk:XDG MIME 应用程序](<../zh-cn/Talk:XDG_MIME_%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F.html>) 中讨论)

支持该规范的桌面环境和文件管理器根据 _.desktop_ 文件中的定义启动程序。参见[桌面项#应用程序项](<../zh-cn/%E6%A1%8C%E9%9D%A2%E9%A1%B9.html#%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E9%A1%B9> "桌面项")。 

通常不需要配置打包的 _.desktop_ 文件，但它可能并非没有缺陷。即使一个包含必要 MIME 类型描述的应用程序在 _.desktop_ 文件中的 `MimeType` 变量被用于关联，它也可能无法正确启动，根本无法启动，或者启动时未能打开文件。 

例如，这可能发生在 `Exec` 变量缺少打开文件所需的内部选项，或缺少如何在菜单中显示应用程序的配置。`Exec` 变量通常以 `%` 开头；有关当前支持的选项，请参见 [exec-variables](<https://specifications.freedesktop.org/desktop-entry-spec/latest/exec-variables.html>)。 

以下表格列出了影响应用程序启动的 _.desktop_ 文件中主要的变量条目，如果它与 MIME 类型关联。 

变量名称 | 示例 1 内容 | 示例 2 内容 | 描述   
---|---|---|---  
DBusActivatable | DBusActivatable=true | DBusActivatable=false | 应用程序与 [D-Bus](<https://www.freedesktop.org/wiki/Software/dbus/>) 交互。  
另见配置： [D-Bus](<https://specifications.freedesktop.org/desktop-entry-spec/latest/dbus.html>)。   
MimeType | MimeType=application/vnd.oasis.opendocument.text | MimeType=application/vnd.sun.xml.math | 应用程序支持的 MIME 类型列表   
StartupWMClass | StartupWMClass=google-chrome | StartupWMClass=xpad | 将窗口与拥有该窗口的应用程序关联   
Terminal | Terminal=true | Terminal=false | 在默认终端中启动   
  
###  空的 MIME 关联 / 在 KDE 中打开菜单

[![](../File:Tango-go-next.png)](<../File:Tango-go-next.png>)**此页面或章节适合移动到[KDE#疑难解答](<../zh-cn/KDE.html#%E7%96%91%E9%9A%BE%E8%A7%A3%E7%AD%94> "KDE")。**

**附注：** KDE 特有的故障排除。（在 [Talk:XDG MIME 应用程序](<../zh-cn/Talk:XDG_MIME_%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F.html>) 讨论）

安装 archlinux-xdg-menu 并运行 `XDG_MENU_PREFIX=arch- kbuildsycoca6`，或将 `export XDG_MENU_PREFIX=plasma-` 添加到 `.xinitrc`。 
