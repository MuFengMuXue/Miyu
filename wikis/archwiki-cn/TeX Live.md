**翻译状态：**

  * 本文（或部分内容）译自 [TeXLive](<https://wiki.archlinux.org/title/TeXLive> "arch:TeXLive")，最近一次同步于 2026-01-12，若英文版本有所[更改](<https://wiki.archlinux.org/title/TeXLive?diff=0&oldid=832662>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/TeXLive_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [TeX Live FAQ](</wzh/index.php?title=TeX_Live_FAQ&action=edit&redlink=1> "TeX Live FAQ（页面不存在）")
  * [TeX Live and CJK](</wzh/index.php?title=TeX_Live_and_CJK&action=edit&redlink=1> "TeX Live and CJK（页面不存在）")
  * [TeXstudio](<../zh-cn/TeXstudio.html> "TeXstudio")

根据[Wikipedia](<https://zh.wikipedia.org/wiki/TeX_Live> "wiki-zh:TeX Live"): 

     **TeX Live** 是一种自由的的 TeX 排版系统发行版，包含主要的 TeX 相关程序、宏包和字体。

TeX Live 包括： 

  * 多种 TeX 引擎，例如： 
    * [pdfTeX](<https://zh.wikipedia.org/wiki/PdfTeX>)
    * [XeTeX](<https://zh.wikipedia.org/wiki/XeTeX>)
    * [LuaTeX](<https://zh.wikipedia.org/wiki/LuaTeX>)
  * 基本宏包（在 TeX 术语中称为“格式”），例如： 
    * [LaTeX](<https://zh.wikipedia.org/wiki/LaTeX>)
    * [ConTeXt](<https://en.wikipedia.org/wiki/ConTeXt>)
  * 许多用户制作的包

TeX Live 的替代方案包括 MikTeX 和 [Tectonic](<../zh-cn/Tectonic.html> "Tectonic")，它们采用最小化安装方式，并在运行时按需下载所需的包。 

##  Arch-packaged TeX Live 与原生 TeX Live 的对比

安装 TeX Live 有多种方式。虽然 TeX Live 的一个快照应该可以通过 Arch Linux 包仓库获得（如下所述），但该快照大多数情况下每年只更新一次。相比之下，TeX Live 本身是一个滚动发布的发行版，基于用户每年必须升级一次的模型，但每个软件包可以在子日级别进行更新。 

拥有原生且最新的 TeX Live 安装的优点包括可以访问最新的功能和 bug 修复，以及相关的文档。尽管在没有原生 TeX Live 的情况下（请参见 `TEXMFLOCAL` 和 `TEXMFHOME`），仍然可以升级或安装单独的软件包，但这需要额外的注意——必须确保所有相关软件包的版本彼此兼容。 

与原生 TeX Live 相比，Arch 仓库中的软件包通常不包括文档，这是一个问题，因为来自 CTAN 的文档通常仅适用于 TeX 包的最新版本。 

**注意：** 多个 TeX Live 安装可以在单一系统上和平共存。

###  原生 TeX Live

####  安装

请参见 [quickinstall](<https://tug.org/texlive/quickinstall.html>) 文档，并根据需要查看 [full](<https://tug.org/texlive/doc/texlive-en/texlive-en.html>) 文档。安装过程如下： 

  1. 下载 netinstall [压缩包](<https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz>)
  2. 解压压缩包并进入新创建的目录
  3. 运行安装脚本，`perl ./install-tl`，启动一个交互式安装程序（文本界面） 
     1. 设置所需的安装路径
     2. 可选地选择 TeX Live 提供的某些“集合”包
     3. 可选地选择 Letter 纸张尺寸作为默认，而不是 A4
     4. 等待所有文件下载完毕
  4. 安装脚本会在过程结束时通知您，需要将 TeX Live 安装路径添加到系统可执行文件和文档路径中：`PATH`、`MANPATH`、`INFOPATH`。安装脚本会输出在退出前所需的具体路径。

或者，也可以安装 [texlive-installer](<https://aur.archlinux.org/packages/texlive-installer/>)AUR 包，然后按照上述步骤运行 `install-tl` 。 

####  更新

请参阅 [tlmgr](<https://tug.org/texlive/doc/tlmgr.html>) 文档，`tlmgr update --all` 将升级安装时选择的所有包集合。它还会安装已添加到安装的 TeX Live 包集合中的新包。 

每年一次，当 TeX Live 发布新版本时，`tlmgr update --all` 会失败，这时需要重新安装 TeX Live。 

###  Arch 打包的 TeX Live

  * [texlive](<https://archlinux.org/groups/x86_64/texlive/>)包组 组包含大多数 TeX Live 包，按上游集合分类（见 [[1]](<https://tex.stackexchange.com/questions/356831/tex-live-package-collection-organisation>)）。 
    * [texlive-basic](<https://archlinux.org/packages/?name=texlive-basic>)包，基础安装，基于上游的“中等”安装方案。该包包括 [pacman hook](<../zh-cn/Pacman_hook.html> "Pacman hook") 自动化操作 _mktexlsr_ 、 _fmtutil_ 和 _updmap_ 。
    * [texlive-latex](<https://archlinux.org/packages/?name=texlive-latex>)包 包含必要的 LaTeX 包。（例如，如果您打算使用 `pdflatex`，则需要此包）。
    * [texlive-latexrecommended](<https://archlinux.org/packages/?name=texlive-latexrecommended>)包 和 [texlive-latexextra](<https://archlinux.org/packages/?name=texlive-latexextra>)包 包含许多有用的 LaTeX 包，如 `polyglossia`、`amsmath` 和 `graphicx`。
    * [texlive-fontsrecommended](<https://archlinux.org/packages/?name=texlive-fontsrecommended>)包 包含必需的字体（包括默认的 Latin Modern）。
    * [texlive-fontsextra](<https://archlinux.org/packages/?name=texlive-fontsextra>)包 包含附加字体，可在 [LaTeX 字体目录](<https://www.tug.org/FontCatalogue/>)查看。
    * [texlive-xetex](<https://archlinux.org/packages/?name=texlive-xetex>)包 和 [texlive-luatex](<https://archlinux.org/packages/?name=texlive-luatex>)包 分别包含 XeTeX 和 LuaTeX 的包。
    * [texlive-bibtexextra](<https://archlinux.org/packages/?name=texlive-bibtexextra>)包 包含 [BibLaTeX](<https://ctan.org/pkg/biblatex>) 包和额外的 BibTeX 样式及参考文献数据库。
    * [texlive-mathscience](<https://archlinux.org/packages/?name=texlive-mathscience>)包 包含数学、自然科学和计算机科学所需的基本包。
  * [texlive-lang](<https://archlinux.org/groups/x86_64/texlive-lang/>)包组 组包含为非拉丁字符语言提供字符集和功能的包。
  * [biber](<https://archlinux.org/packages/?name=biber>)包 提供 BibLaTeX 的替代参考文献处理后端。

请注意，[texlive-binextra](<https://archlinux.org/packages/?name=texlive-binextra>)包 中的某些工具有可选依赖项，未自动安装。例如， _latexindent_ 依赖于 [perl-yaml-tiny](<https://archlinux.org/packages/?name=perl-yaml-tiny>)包 和 [perl-file-homedir](<https://archlinux.org/packages/?name=perl-file-homedir>)包。 

**提示：** 如果缺少特定的 _.sty_ 文件，可以运行 `pacman -F` 来查找提供该文件的 Arch 包： 
    
    $ pacman -F soul.sty
    
    extra/texlive-plaingeneric 2023.66594-19 (texlive)
        usr/share/texmf-dist/tex/generic/soul/soul.sty
    
如果需要安装一个可用的 [CTAN](<https://www.ctan.org/>) TeX 包，请运行以下命令来确定它是否包含在 Arch 的 _texlive-_ 包中： 
    
    $ tlmgr info ctan_package_name | grep collection
    
这将列出与 Arch _texlive-_ 包对应的 TeX Live 包集合名称（也可以检查 [texlive](<https://archlinux.org/groups/x86_64/texlive/>)包组 组以确认是否存在此包）。例如，输出 `collection: collection-plaingeneric` 表示该 TeX 包包含在 [texlive-plaingeneric](<https://archlinux.org/packages/?name=texlive-plaingeneric>)包 中。 

另外，可以使用 `tlmgr` 手动安装单个 TeX 包（见下文）。 

**注意：** 某些 TeX Live 包中包含的工具和实用程序依赖于 [ghostscript](<https://archlinux.org/packages/?name=ghostscript>)包、[perl](<https://archlinux.org/packages/?name=perl>)包、[python](<https://archlinux.org/packages/?name=python>)包 或 [ruby](<https://archlinux.org/packages/?name=ruby>)包。有关详细信息，请查看每个包的可选依赖项。

#### tllocalmgr

**警告：** 有建议认为 tllocalmgr 将不再工作。请参阅 [[2]](<https://bbs.archlinux.org/viewtopic.php?id=286197>)。

_tllocalmgr_ 工具由 [tllocalmgr](<https://aur.archlinux.org/packages/tllocalmgr/>)AUR 提供，允许您将来自 CTAN 的包作为 [pacman](<../zh-cn/Pacman.html> "Pacman") 包安装（和更新）。请参见[使用方法](<https://github.com/hv15/tllocalmgr/blob/master/tllocalmgr#L835>)（`-h`）了解详细信息。 

#### tlmgr

使用 [texlive-basic](<https://archlinux.org/packages/?name=texlive-basic>)包 时，`tlmgr` 工具应当开箱即用。 

默认情况下，其需要root权限才可运行。 
    
    # tlmgr install _package_name_
    
如您想在不使用 root 权限的情况下运行程序，请使用内置的用户模式。默认情况下，该功能会将 CTAN 软件包安装到 `~/texmf` 目录。 `tlmgr` 必须先对此目录进行初始化，因此请运行： 
    
    $ tlmgr init-usertree
    
现在，你可以使用用户模式： 
    
    $ tlmgr --usermode install _package_name_
    
要更改包的安装位置，请更改 `TEXMFHOME` 这个环境变量。 
    
    $ export TEXMFHOME="$HOME/.local/texmf"
    $ tlmgr init-usertree
    $ ...
    
`tlmgr` 会自行选择一个合适的镜像。不过，你也可以自行设置首选[镜像网站](<https://www.ctan.org/mirrors>)。需要你在镜像路径末尾添加 `/systems/texlive/tlnet`。例如： 
    
    $ tlmgr option repository http://mirrors.rit.edu/CTAN/systems/texlive/tlnet
    
####  包文档

官方仓库中的包不包含字体/宏包的文档或源文件。 

要使用`texdoc` 离线访问文档，请安装 [texlive-doc](<https://archlinux.org/packages/?name=texlive-doc>)包 包，它包含完整的 TeX Live 文档和源文件。 

您也可以在线访问文档： 

  * <https://tug.org/texlive/Contents/live/doc.html>
  * <https://ctan.org/> – TeX 相关材料的中心
  * <https://texdoc.org/> (`http://texdoc.org/pkg/_packagename_` 可直接获取相关 PDF)

##  用法

请参见以下资源： 

  * [Wikibooks:LaTeX](<https://en.wikibooks.org/wiki/LaTeX> "wikibooks:LaTeX")
  * [《LaTeX 2ε 简明介绍》](<https://tobi.oetiker.ch/lshort/lshort.pdf>)
  * [学习 LaTeX – Andrew Roberts](<https://www.andy-roberts.net/writing/latex>)
  * [TeX FAQ](<https://www.texfaq.org/>)
  * [《GNU TeX for the Impatient》](<https://www.gnu.org/software/teximpatient/>)（中文译本：[《TeX 急就帖》](<http://zoho.is-programmer.com/user_files/zoho/epics/tex-impatient-cn.pdf>)）

有些人使用 [TeX 编辑器](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E6%96%87%E6%A1%A3.html#TeX_%E7%BC%96%E8%BE%91%E5%99%A8> "应用程序列表/文档")来创建文档。 

###  编译文档的高级封装器

通常来说，使用 [latexmk(1)](<https://man.archlinux.org/man/latexmk.1>) 等高级工具，或者使用 [arara(1)](<https://man.archlinux.org/man/arara.1>)，比直接调用 [pdflatex(1)](<https://man.archlinux.org/man/pdflatex.1>) 更有意义，主要是因为较低级的工具通常需要多次运行才能完全编译一个文档。 

###  texmf 树和 Kpathsea

texmf 树（ _texmf_ 代表 TeX 和 [Metafont](<https://en.wikipedia.org/wiki/Metafont> "wikipedia:Metafont")）应遵循 [TeX 目录结构](<https://tug.org/tds/>)，否则可能无法找到文件。[[3]](<https://www.tug.org/texlive/doc/texlive-en/texlive-en.html#x1-110002.3>)

TeX Live 使用 [Kpathsea](<https://tug.org/texinfohtml/kpathsea.html>) 库来通过文件名查找路径，跨越多个 texmf 树和当前工作目录。 

Kpathsea 按逆序搜索以下变量（较晚的树会覆盖较早的树）。 

变量 | Arch 默认值 1) | 由 [[4]](<https://www.tug.org/texlive/doc/texlive-en/texlive-en.html#x1-110002.3>) 使用   
---|---|---  
`TEXMFDIST` | `/usr/share/texmf-dist` | 原始分发文件   
`TEXMFLOCAL` | `/usr/local/share/texmf:/usr/share/texmf` | 系统管理员用于全局安装附加或更新的宏、字体等   
`TEXMFSYSVAR` | `/var/lib/texmf` | updmap 和 fmtutil（用户模式）存储（缓存）运行时数据   
`TEXMFSYSCONFIG` | `/etc/texmf` | updmap 和 fmtutil（用户模式）存储修改后的配置数据   
`TEXMFHOME` | `~/texmf` | 用户用于个别安装附加或更新的宏、字体等   
`TEXMFVAR` | `~/.texlive/texmf-var` | updmap 和 fmtutil（系统模式）存储（缓存）运行时数据   
`TEXMFCONFIG` | `~/.texlive/texmf-config` | 用户模式的配置数据   
`TEXMFCACHE` |  `$TEXMFSYSVAR; ``$TEXMFVAR` | 使用 ConTeXt MkIV 和 LuaLaTeX 存储（缓存的）运行时数据   
  
**注意：** 默认值在`/etc/texmf/web2c/texmf.cnf`[[5]](<https://gitlab.archlinux.org/archlinux/packaging/packages/texlive-texmf/-/blob/main/texmf.cnf.patch>) 中定义；它们可以通过[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")进行覆盖。

Kpathsea 提供了 [kpsewhich(1)](<https://man.archlinux.org/man/kpsewhich.1>) 命令来查找路径。当使用 `--var-brace-value=_VARIABLE_` 参数运行时，它还可以打印变量的值。 

Kpathsea 使用文件名数据库（`ls-R`）来加速在系统级 texmf 树（通过 `TEXMFDBS` 变量配置）中的搜索。这意味着当系统级文件树发生更改时，需要以 [root](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E6%A6%82%E8%A7%88> "Root") 运行 [mktexlsr(1)](<https://man.archlinux.org/man/mktexlsr.1>) 或 `texhash`（符号链接）。[texlive-basic](<https://archlinux.org/packages/?name=texlive-basic>)包 通过 [pacman hook](<../zh-cn/Pacman_hook.html> "Pacman hook") 实现了自动化，该 hook 针对所有默认的系统级 texmf 树，但 `/usr/local/share/texmf`。[[6]](<https://gitlab.archlinux.org/archlinux/packaging/packages/texlive-texmf/-/blob/main/70-mktexlsr.hook>) 因此，只要您通过 [pacman](<../zh-cn/Pacman.html> "Pacman") 安装系统级软件包，就完全不需要运行 _mktexlsr_ 或 _texhash_ 。 

**提示：** 要设置本地存储库，您可以创建`~/texmf/`目录结构`{format} `通常是`latex`），其中自定义类位于 `./{format`}文件夹的根目录中，其他本地文件则放在同名文件夹中（例如，`mycustompackage.sty`放在`./{formats}/mycustompackage/``mycustompackage.sty`文件夹中），然后运行`texhash`来更新用户数据库。

##  窍门与技巧

###  更改默认纸张尺寸

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 可以通过直接编辑配置文件来实现。（在 [Talk:TeX Live](</wzh/index.php?title=Talk:TeX_Live&action=edit&redlink=1> "Talk:TeX Live（页面不存在）") 中讨论）

目前无法使用 texlive 工具设置默认页面大小，因为它们与标准的 Arch 软件包不兼容。 

通常情况下，你会运行 `texconfig` 或 `tlmgr` ，它们还可以更改其他有用的设置。 

您可以按如下方式编辑配置文件。 

  * 要为 _pdftex_ 系列命令（ _pdftex_ 、 _pdflatex_ 等）设置纸张大小，请编辑 `/etc/texmf/tex/generic/tex-ini-files/pdftexconfig.tex` 文件。

也可以通过运行 `kpsewhich pdftexconfig.tex` 来发现。修改指定 `pdfpageheight` 和 `pdfpagewidth` 的两行。例如，要使用信纸大小，请修改 
    
    \pdfpageheight = 297 true mm
    \pdfpagewidth  = 210 true mm
    
到 
    
    \pdfpageheight = 11 true in
    \pdfpagewidth  = 8.5 true in
    
遗憾的是，这只有在 _.fmt_ 二进制文件重新构建后才会生效。您可以使用 `fmtutil-sys` 来完成此操作。使用 pacman 重新安装 texlive-bin 也能达到同样的效果。 

  * 对于 _dvips_ ，您可以使用 `-t` 选项指定纸张尺寸： `dvips -t letter foo.dvi` 。要更改默认值，请编辑 `/etc/texmf/dvips/config/config.ps` 文件。

也可以使用 `kpsewhich config.ps` 命令来查找。该文件的末尾列出了 _dvips_ 已知的所有纸张尺寸。列表中第一个纸张尺寸将作为默认值。只需将您希望设为默认值的纸张尺寸移动到列表顶部即可。一旦该文件发生更改， _dvips_ 的行为就会受到影响。 

###  让字体在Fontconfig下识别

默认情况下，各种 TeX Live 宏包自带的字体不会自动被 Fontconfig 识别 。如果您想在 XeTeX 或 LibreOffice 等软件中使用这些字体，最简单的方法是在字体目录中创建一个指向用户字体路径下子目录的符号链接。对于 OpenType 字体，请运行以下命令： 
    
    $ ln -s /usr/share/texmf-dist/fonts/opentype/public/_some_fonts_you_want_ ~/_font_path_ /OTF/
    
要使 fontconfig 能够访问它们，请运行： 
    
    $ fc-cache ~/_font_path_
    $ mkfontscale ~/_font_path_ /OTF
    $ mkfontdir ~/_font_path_ /OTF
    
TrueType 字体和 Type 1 字体的操作步骤类似。在上面的几行代码中，将 `opentype` 替换为 `truetype` 或 `type1` ，将 `OTF` 替换为 `TTF` 或 `Type1` 。 

或者， texlive-basic 包含文件 `/usr/share/fontconfig/conf.avail/09-texlive-fonts.conf` ，其中包含 TeX Live 使用的字体目录列表。您可以将此文件与以下命令一起使用： 
    
    # ln -s /usr/share/fontconfig/conf.avail/09-texlive-fonts.conf /etc/fonts/conf.d/09-texlive-fonts.conf
    
然后更新系统配置 
    
    $ fc-cache && mkfontscale && mkfontdir
    
**注意：** 如果 TeX 和 Fontconfig 分别使用了相同的字体，即搜索路径上有多个相同的字体副本，则可能会与 XeTeX/XeLaTeX 发生冲突。 LibreOffice 5.3 及更高版本将不再提供 Type 1 字体。

###  更新babelbib语言定义

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** 您不应该更改 `/usr/share/texmf-dist/` 。（在[Talk:TeX Live#Talk:TeX_Live](</wzh/index.php?title=Talk:TeX_Live&action=edit&redlink=1> "Talk:TeX Live（页面不存在）")讨论）

如果您遇到 babelbib 没有您需要的最新语言定义这一特殊问题，并且不想重新编译所有内容，您可以从 https://www.tug.org/texlive/devsrc/Master/texmf-dist/tex/latex/babelbib/ 手动获取这些定义，并将其放入 `/usr/share/texmf-dist/tex/latex/babelbib/` 中。例如： 
    
    $ cd /usr/share/texmf-dist/tex/latex/babelbib/ 
    # wget https://www.tug.org/texlive/devsrc/Master/texmf-dist/tex/latex/babelbib/romanian.bdf
    # wget [...all-other-language-files...]
    # wget https://www.tug.org/texlive/devsrc/Master/texmf-dist/tex/latex/babelbib/babelbib.sty
    
之后，您需要运行 `texhash` 来更新 TeX 数据库： 
    
    # texhash
    
##  相关页面

  * [LaTeX](<../zh-cn/TeX_Live.html> "LaTeX")
  * [TeX](</wzh/index.php?title=TeX&action=edit&redlink=1> "TeX（页面不存在）")
  * TeX Live
  * [pacman](<../zh-cn/Pacman.html> "Pacman")
