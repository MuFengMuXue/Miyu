相关文章

  * [TeX Live](<../zh-cn/TeX_Live.html> "TeX Live")

**翻译状态：**

  * 本文（或部分内容）译自 [Tectonic](<https://wiki.archlinux.org/title/Tectonic> "arch:Tectonic")，最近一次同步于 2024-12-22，若英文版本有所[更改](<https://wiki.archlinux.org/title/Tectonic?diff=0&oldid=823619>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Tectonic_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Tectonic](<https://tectonic-typesetting.github.io/>) 是一个基于 [XeTeX](<https://en.wikipedia.org/wiki/XeTeX> "wikipedia:XeTeX") 的 [TeX](<https://en.wikipedia.org/wiki/TeX> "wikipedia:TeX") 发行版。 

它由[TeX Live](<../zh-cn/TeX_Live.html> "TeX Live") 驱动，按需下载编译文档所需的 TeX 软件包。与传统的 TeX 工具不同，Tectonic 的一个优点是在编译文档时避免在工作目录中加入不必要的文件。 

不过，Tectonic 基于的 XeTeX 引擎并没有得到维护，与 [pdfTeX](<https://en.wikipedia.org/wiki/pdfTeX> "wikipedia:pdfTeX") 或 [LuaTeX](<https://en.wikipedia.org/wiki/LuaTeX> "wikipedia:LuaTeX") 等其他引擎（均可通过标准 TeX Live 安装）相比，可能存在兼容性问题和功能缺失。 

##  安装

Tectonic 引擎可通过 [tectonic](<https://archlinux.org/packages/?name=tectonic>)包 软件包安装。 

##  用法

Tectonic 的基本用法是： 
    
    $ tectonic main.tex
    
只需运行一次命令，就能将其编译成完全处理过的 pdf 文件。 

编译时，tectonic 会自动下载必要的 LaTeX 软件包，无需进行配置。 

###  V2 界面

与默认的命令行界面相比，使用 `-X` 标志访问的新界面拥有更多功能。更多相关信息，请参阅官方 [Tectonic Book](<https://tectonic-typesetting.github.io/book/>)。 

##  参见

  * [Tectonic 网站](<https://tectonic-typesetting.github.io>)
  * [Tectonic Book](<https://tectonic-typesetting.github.io/book/>)
