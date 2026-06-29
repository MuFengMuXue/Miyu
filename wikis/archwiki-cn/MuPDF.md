相关文章

  * [llpp](</wzh/index.php?title=Llpp&action=edit&redlink=1> "Llpp（页面不存在）")
  * [zathura](</wzh/index.php?title=Zathura&action=edit&redlink=1> "Zathura（页面不存在）")
  * [应用程序列表/文档#阅读器与查看器](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E6%96%87%E6%A1%A3.html#%E9%98%85%E8%AF%BB%E5%99%A8%E4%B8%8E%E6%9F%A5%E7%9C%8B%E5%99%A8> "应用程序列表/文档")

**翻译状态：**

  * 本文（或部分内容）译自 [MuPDF](<https://wiki.archlinux.org/title/MuPDF> "arch:MuPDF")，最近一次同步于 2024-12-22，若英文版本有所[更改](<https://wiki.archlinux.org/title/MuPDF?diff=0&oldid=823618>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/MuPDF_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[MuPDF](<https://en.wikipedia.org/wiki/MuPDF> "w:MuPDF") 是一个用可移植 C 语言编写的轻量级文档查看器和工具包。它支持 [PDF](<../zh-cn/PDF%E3%80%81PS_%E4%B8%8E_DjVu.html> "PDF")、XPS、EPUB、XHTML、CBZ 和各种图像格式，如 PNG、JPEG、GIF 和 TIFF。 

MuPDF 的渲染器专为高质量反锯齿图形而设计。它渲染文本时的度量和间距精确到像素的几分之一，可在屏幕上最逼真地再现印刷页面的外观。 

MuPDF 支持 PDF 1.7 要求的所有静态功能，是基于 poppler 的 pdf 应用程序的轻量级替代品。它还支持标准的 PDF 注释，如高亮显示、形状工具、绘图、注释和文件附件。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [mupdf](<https://archlinux.org/packages/?name=mupdf>)包 软件包或为 OpenGL 后端而[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [mupdf-gl](<https://archlinux.org/packages/?name=mupdf-gl>)包，也可以安装 [mupdf-git](<https://aur.archlinux.org/packages/mupdf-git/>)AUR 来获取开发版本。要使用文档处理工具，请安装 [mupdf-tools](<https://archlinux.org/packages/?name=mupdf-tools>)包 软件包。 

##  用法

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 这两个软件包包含相同的手册页。应注意偏差。 (在 [Talk:MuPDF](<../zh-cn/Talk:MuPDF.html>) 中讨论)

更多信息，请参见 `mupdf --help` 或 [mupdf(1)](<https://man.archlinux.org/man/mupdf.1>) 和 [mutool(1)](<https://man.archlinux.org/man/mutool.1>) 。 

**注意：**[mupdf](<https://archlinux.org/packages/?name=mupdf>)包 和 [mupdf-gl](<https://archlinux.org/packages/?name=mupdf-gl>)包 的选项可能有所不同。

应用程序可以通过命令行 `mupdf _filename_.pdf` 或[文件管理器](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E5%B7%A5%E5%85%B7.html#%E6%96%87%E4%BB%B6%E7%AE%A1%E7%90%86%E5%99%A8> "应用程序列表/工具")启动。 

文档内的导航使用标准键盘快捷键和鼠标交互。例如，`B` 和 `Space` 可以上下滚动。 

### MuPDF

支持的参数有：`-d _password_`表示必填密码，`-z N%` 表示缩放级别，`-p N` 表示第一个选定的页面等。 

放大时，可使用鼠标左键移动文档。移动鼠标的同时按下鼠标右键将标记一个区域，所有文本将被复制，点击鼠标中键即可插入。 

### MuPDF GL

按 `I` 反转颜色。请参阅[[1]](<https://mupdf.readthedocs.io/en/latest/mupdf-command-line.html#mupdf-gl>)获取使用手册，或按 `F1` 获取帮助。 

###  设置为默认 PDF 阅读器
    
    $ xdg-mime default mupdf.desktop application/pdf
    
有关设置默认应用程序的更多信息，请参阅[XDG MIME 应用程序](<../zh-cn/XDG_MIME_%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F.html> "XDG MIME 应用程序")。 

###  注释支持

要访问注释菜单，只需按下 `a`，注释侧边栏就会出现，它支持几乎所有标准 PDF 注释工具（至少在 [mupdf-gl](<https://archlinux.org/packages/?name=mupdf-gl>)包 中可用）。 

##  参见

  * [MuPDF 网站](<https://mupdf.com/>)
  * [Poppler 网站](<https://poppler.freedesktop.org/>)
