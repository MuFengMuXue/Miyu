相关文章

  * [Matlab](<../zh-cn/MATLAB.html> "Matlab")
  * [Octave](<../zh-cn/Octave.html> "Octave")
  * [Mathematica](<../zh-cn/Mathematica.html> "Mathematica")

**翻译状态：**

  * 本文（或部分内容）译自 [SageMath](<https://wiki.archlinux.org/title/SageMath> "arch:SageMath")，最近一次同步于 2025-01-12，若英文版本有所[更改](<https://wiki.archlinux.org/title/SageMath?diff=0&oldid=824963>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/SageMath_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[SageMath](<https://www.sagemath.org>) (原 **Sage**) 是一个使用 [Python](<../zh-cn/Python.html> "Python") 作为主要语言的数值和符号数学计算程序。它旨在提供 Maple、[Matlab](<../zh-cn/MATLAB.html> "Matlab") 和 [Mathematica](<../zh-cn/Mathematica.html> "Mathematica") 等商业程序的替代程序。 

SageMath 支持以下功能： 

  * **微积分** : 使用 [Maxima](<https://en.wikipedia.org/wiki/Maxima_\(software\)> "wikipedia:Maxima \(software\)") 与 [SymPy](<https://en.wikipedia.org/wiki/SymPy> "wikipedia:SymPy")。
  * **线性代数** : 使用 [GSL](<https://en.wikipedia.org/wiki/GNU_Scientific_Library> "wikipedia:GNU Scientific Library")、 [SciPy](<https://en.wikipedia.org/wiki/SciPy> "wikipedia:SciPy") 与 [NumPy](<https://en.wikipedia.org/wiki/NumPy> "wikipedia:NumPy")。
  * **统计** : 使用 [R](<https://en.wikipedia.org/wiki/R_\(programming_language\)> "wikipedia:R \(programming language\)") (通过 RPy) 与 SciPy。
  * **图形** : 使用 [matplotlib](<https://en.wikipedia.org/wiki/matplotlib> "wikipedia:matplotlib").
  * 一个使用 [IPython](<https://en.wikipedia.org/wiki/IPython> "wikipedia:IPython") 的**交互式 shell** 。
  * 访问 **Python 模块** ，如 [PIL](<https://en.wikipedia.org/wiki/Python_Imaging_Library> "wikipedia:Python Imaging Library")、[SQLAlchemy](<https://en.wikipedia.org/wiki/SQLAlchemy> "wikipedia:SQLAlchemy") 等。

##  安装

  * [sagemath](<https://archlinux.org/packages/?name=sagemath>)包 包含命令行版本；
  * [sagemath-doc](<https://archlinux.org/packages/?name=sagemath-doc>)包 从命令行获取 HTML 文档和内联帮助。

**注意：** 许多 Sage 软件包是作为 [sagemath](<https://archlinux.org/packages/?name=sagemath>)包 软件包的[可选依赖](<../zh-cn/Pacman.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Pacman")或 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 软件包提供的。请注意，无需使用 `sage -i` 安装它们，事实上，如果使用 pacman 安装了 SageMath，该命令将不起作用。

##  用法

SageMath 主要使用 Python 作为脚本语言，并进行了一些[修改](<https://doc.sagemath.org/html/en/tutorial/afterword.html#section-mathannoy>)，使其更适合数学计算。 

###  SageMath 命令行

SageMath 可通过命令行启动： 
    
    $ sage
    
有关 SageMath 命令行的信息，请参阅[此页面](<https://doc.sagemath.org/html/en/reference/repl/index.html>)。 

命令行基于 IPython shell，因此您可以在 SageMath 中使用它的所有[技巧](<https://doc.sagemath.org/html/en/tutorial/interactive_shell.html>)。有关 IPython 的详尽教程，请参阅社区维护的 [IPython Cookbook](<https://ipython-books.github.io/>)。 

不过要注意的是，在某些情况下（如绘图），使用它并不十分方便。例如，当您尝试绘制某幅图时： 
    
    sage: plot(sin,(x,0,10))
    
SageMath 会在外部应用程序中打开绘图。 

### Jupyter Notebook

SageMath 还为 [Jupyter](<https://jupyter.org/>) 笔记本提供了内核。要使用它，请使用以下命令启动笔记本 
    
    $ jupyter notebook
    
并在"新建... "下拉菜单中选择 "SageMath"。SageMath Jupyter 笔记本支持通过 `%display latex` 命令输出 [LaTeX](<../zh-cn/TeX_Live.html> "LaTeX")，如果安装了 [jmol](<https://archlinux.org/packages/?name=jmol>)包 则支持 3D 绘图。 

### Sage Notebook

**注意：** SageMath Flask 笔记本已被弃用，改用 Jupyter 笔记本。所有新工作表都推荐使用 Jupyter 笔记本。

Notebook（[sage-notebook](<https://aur.archlinux.org/packages/sage-notebook/>)AUR）是更适合 SageMath 高级使用的界面。 

要从命令行启动笔记本服务器，请执行： 
    
    $ sage -n jupyter
    
您可以从浏览器 <http://localhost:8080> 访问该笔记本，并需要登录。 

不过，如果你只是为个人使用而运行服务器，而不是在互联网上运行，那么登录就会很麻烦。您可以使用以下命令启动笔记本，无需登录，并在浏览器中自动弹出： 
    
    $ sage -c "notebook(automatic_login=True)"
    
### Cantor

[Cantor](<https://apps.kde.org/cantor/>) 是 KDE Edu 项目中的一个应用程序。它是各种数学应用程序（如 Maxima、SageMath、Octave、Scilab 等）的前端。有关如何将其与 SageMath 结合使用的详细信息，请参阅 Sage wiki 上的 [Cantor 页面](<https://wiki.sagemath.org/Cantor>)。 

Cantor 可以通过 [cantor](<https://archlinux.org/packages/?name=cantor>)包 软件包安装，也可以作为 [kde-applications](<https://archlinux.org/groups/x86_64/kde-applications/>)包组 或 [kde-education](<https://archlinux.org/groups/x86_64/kde-education/>)包组 组的一部分安装。 

##  可选附加项目

### SageTeX

如果您的系统上安装了 [TeX Live](<../zh-cn/TeX_Live.html> "TeX Live")，您可能会对[使用 SageTeX](<https://doc.sagemath.org/html/en/tutorial/sagetex.html>) 感兴趣，这是一个可以在 LaTeX 文件中加入 SageMath 代码的软件包。TeX Live 会自动识别 SageTeX，因此您可以立即开始使用它。 

下面举一个简单的例子，说明如何在 TEX 文档中加入 Sage 2D 绘图（假设使用 `pdflatex`）： 

  * 在文件前言中加入 `sagetex` 软件包，并使用常见的

    \usepackage{sagetex}
    
  * 创建一个 `sagesilent` 环境，在其中插入代码：

    \begin{sagesilent}
    dob(x) = sqrt(x^2 - 1) / (x * arctan(sqrt(x^2 - 1)))
    dpr(x) = sqrt(x^2 - 1) / (x * log( x + sqrt(x^2 - 1)))
    p1 = plot(dob,(x, 1, 10), color='blue')
    p2 = plot(dpr,(x, 1, 10), color='red')
    ptot = p1 + p2
    ptot.axes_labels(['$\\xi$','$\\frac{R_h}{\\max(a,b)}$'])
    \end{sagesilent}
    
  * 创建绘图，例如在 `float` 环境中：

    \begin{figure}
    \begin{center}
    \sageplot[width=\linewidth]{ptot}
    \end{center}
    \end{figure}
    
  * 按以下步骤编译您的文件：

    $ pdflatex <doc.tex>
    $ sage <doc.sagetex.sage>
    $ pdflatex <doc.tex>
    
  * 您就可以查看输出文档了。

SageTeX 的完整文档可在 [CTAN](<https://ctan.org/pkg/sagetex>) 上获取。 

##  问题解决

###  TeX Live 无法识别 SageTex

如果 TeX Live 安装程序找不到 SageTex 软件包，可以尝试以下步骤（以根用户身份或使用本地文件夹）： 

  * 将文件复制到 texmf 目录：

    # cp /opt/sage/local/share/texmf/tex/* /usr/share/texmf/tex/
    
  * 刷新 TeX Live：

    # texhash /usr/share/texmf/
    texhash: Updating /usr/share/texmf/.//ls-R... 
    texhash: Done.
    
##  参见

  * [官方网站](<https://www.sagemath.org/>)
  * [SageMath Documentation](<https://doc.sagemath.org/>)
  * [Planet Sage](<https://planet.sagemath.org/>)
  * [SageMath Wiki](<https://wiki.sagemath.org/>)
  * [Software Used by SageMath](<https://www.sagemath.org/links-components.html>)
  * [Kevin Stephen 的 SageMath 学习笔记（简体中文）](<https://blogs.qarks.top/notes/sagemath/index.html>)
    * [视频版](<https://m.bilibili.com/video/BV116HjeKEY9>)
