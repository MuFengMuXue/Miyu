**翻译状态：**

  * 本文（或部分内容）译自 [Idesk](<https://wiki.archlinux.org/title/Idesk> "arch:Idesk")，最近一次同步于 2020-07-27，若英文版本有所[更改](<https://wiki.archlinux.org/title/Idesk?diff=0&oldid=626927>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Idesk_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Idesk](<http://idesk.sourceforge.net/html/index.html>) 是一个可以让您在您的X桌面上添加图标的简单程序。它还可以通过一个类似于 Windows 7 中的内置更换程序来管理你的壁纸。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [idesk](<https://aur.archlinux.org/packages/idesk/>)AUR。然后通过以下方式来复制必要的配置文件到您的主目录下： 
    
    $ mkdir ~/.idesktop
    $ cp /usr/share/idesk/dot.ideskrc ~/.ideskrc
    
也可以： 
    
    $ cp /usr/share/idesk/default.lnk ~/.idesktop/
    
（这就增加了默认的图标，它用来只是运行 Xdialog 并显示欢迎信息。它可以被用作其他图标的模板。） 

##  配置

[idesk](<https://aur.archlinux.org/packages/idesk/>)AUR 包没有 man 页面，但是有一个 readme 文件：`/usr/share/idesk/README`。在 [**SourceForge.net**](<http://idesk.sourceforge.net/html/usage.html>) 上也有一份文档，但大多数配置选项都应是不言自明的。 

###  背景选项

如果你正在使用其他壁纸设置工具，类似于 [Feh](<../zh-cn/Feh.html> "Feh") 或 [Nitrogen](<../zh-cn/Nitrogen.html> "Nitrogen")，Idesk的背景设置不需要进行修改。 

如果您使用的是 Idesk 自己的背景设置器，它支持包括 JPEG、PNG、GIF 和 XPM 在内的格式。请使用 `Background.File` 或 `Background.Source` 来指定您希望用作墙纸的图像文件路径。 

**提示：**`Background.Source` 似乎优先于 `Background.File` 执行；然而，如果 `Background.Delay` 被设置为 0

，它将会被忽略。 

###  图标

Idesk 将在 `~/.idesktop` 文件夹中以 `.lnk` 为结尾的文件作为图标。每个文件应定义一个图标，如果您试图定义第二个图标，它将被自动忽略。除了以`.lnk`，文件的名称其实并不重要。 

以 Chromium 为例： 
    
    chromium.lnk
    
    table Icon
      Caption: Chromium
      ToolTip.Caption: 谷歌的开源浏览器
      Icon: /usr/share/icons/hicolor/32x32/apps/chromium.png
      Width: 32
      Height: 32
      X: 977
      Y: 369
      Command[0]: chromium
    end

`宽度` 和 `高度` 应符合图标的实际尺寸。 `X` 与 `Y` 将被 Idesk 修改以反映图标的实际位置。 

**提示：**

  * 大多数系统图标可以在 `/usr/share/icons/hicolor`，`/usr/share/icons/gnome` 和 `/usr/share/pixmaps` 中找到。
  * 很多图标主题都提供了不同尺寸的图标 - 48x48是桌面图标常用的尺寸。

### Idesktool

[idesk-extras](<https://aur.archlinux.org/packages/idesk-extras/>)AUR 包提供了一个 Idesk 的图形化配置工具。可以通过执行 `idesktool` 命令以启动。用户可以通过 Idesktool 来创建并移除图标，更改设置和重启 Idesk。 
