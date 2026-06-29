相关文章

  * [Python 打包准则](<../zh-cn/Python_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Python 打包准则")
  * [Python/虚拟环境](<../zh-cn/Python/%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83.html> "Python/虚拟环境")
  * [mod_wsgi](</wzh/index.php?title=Mod_wsgi&action=edit&redlink=1> "Mod wsgi（页面不存在）")
  * [Django](<../zh-cn/Django.html> "Django")
  * [应用程序列表/工具#Python IDE](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E5%B7%A5%E5%85%B7.html#Python_IDE> "应用程序列表/工具")

**翻译状态：**

  * 本文（或部分内容）译自 [Python](<https://wiki.archlinux.org/title/Python> "arch:Python")，最近一次同步于 2024-11-30，若英文版本有所[更改](<https://wiki.archlinux.org/title/Python?diff=0&oldid=820064>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Python_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

来自[“什么是 Python？”](<https://docs.python.org/zh-cn/3/faq/general.html#what-is-python>)： 

    Python 是一种解释型、交互式、面向对象的编程语言。 它包含了模块、异常、动态类型、高层级动态数据类型以及类等特性。 在面向对象编程以外它还支持多种编程范式，例如过程式和函数式编程等。 Python 结合了超强的功能和极清晰的语法。 它带有许多系统调用和库以及多种窗口系统的接口，并且能用 C 或 C++ 来进行扩展。 它还可用作需要可编程接口的应用程序的扩展语言。 最后，Python 非常易于移植：它可以在包括 Linux 和 macOS 在内的许多 Unix 变种以及 Windows 上运行。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [python](<https://archlinux.org/packages/?name=python>)包。 

###  其它版本

Python 的旧版本和预发布版本可以通过 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 获得，这对于无法在当前版本上运行的旧应用程序、打算在其他版本上运行的程序，或者仅仅出于好奇，可能会很有用： 

  * Python 3.14：[python314](<https://aur.archlinux.org/packages/python314/>)AUR（预发布版本）

  * Python 3.14：[python314-freethreaded](<https://aur.archlinux.org/packages/python314-freethreaded/>)AUR（自由多线程——移除了[全局线程锁](<https://wiki.python.org/moin/GlobalInterpreterLock> "pythoninfo:GlobalInterpreterLock")，又称 GIL）

  * Python 3.13：[python313-freethreaded](<https://aur.archlinux.org/packages/python313-freethreaded/>)AUR（自由多线程）
  * Python 3.12：[python312](<https://aur.archlinux.org/packages/python312/>)AUR
  * Python 3.11：[python311](<https://aur.archlinux.org/packages/python311/>)AUR
  * Python 3.10：[python310](<https://aur.archlinux.org/packages/python310/>)AUR
  * Python 3.9：[python39](<https://aur.archlinux.org/packages/python39/>)AUR
  * Python 3.8：[python38](<https://aur.archlinux.org/packages/python38/>)AUR（[停止维护](<https://peps.python.org/pep-0569/>)）
  * Python 3.7：[python37](<https://aur.archlinux.org/packages/python37/>)AUR（[停止维护](<https://peps.python.org/pep-0537/>)）
  * Python 3.6：[python36](<https://aur.archlinux.org/packages/python36/>)AUR（[停止维护](<https://peps.python.org/pep-0494/>)）
  * Python 2.7：[python2](<https://aur.archlinux.org/packages/python2/>)AUR（[停止维护](<https://www.python.org/doc/sunset-python-2/>)）

**警告：** Python 3.9 之前的版本都已经停止维护。参见 [Python 版本状态](<https://devguide.python.org/versions/>)。

为实现多版本共存，每个这样的软件包都会安装一个以版本号命名的独立二进制文件，例如 Python 3.9 的二进制文件名为 `python3.9`。[pyenv](<https://archlinux.org/packages/?name=pyenv>)包 可用于轻松安装和切换多个 Python 版本。 

在 AUR 上搜索 `python<版本号（不带小数点）>` 可以找到用于旧版本的额外模块/库，例如搜索 `python39` 可以找到 3.9 版本的模块。 

可以从 <https://www.python.org/downloads/> 下载任意版本的源代码。 

###  替代实现

[python](<https://archlinux.org/packages/?name=python>)包 包会安装 [CPython](<https://github.com/python/cpython>)， 是 Python 的参考实现，而同时还有多种其它的实现。这些实现通常基于旧版本的 Python 而并不完全与 CPython 兼容。 

Arch Linux 官方仓库与 AUR 包含的实现： 

  * **[PyPy](<../zh-cn/PyPy.html> "PyPy")** — 使用 Python 编写的 Python 实现，较 CPython 而言具有速度和内存用量上的优势。

     <https://www.pypy.org> || [pypy](<https://archlinux.org/packages/?name=pypy>)包、[pypy3](<https://archlinux.org/packages/?name=pypy3>)包

  * **Jython** — 使用 Java 编写的 Python 实现，可以用于将 Python 脚本嵌入到 Java 程序中，或是在 Python 程序中使用 Java 库。

     <https://www.jython.org/> || [jython](<https://archlinux.org/packages/?name=jython>)包

  * **micropython** — 用于微控制器的 Python 实现，包含了 Python 标准库的一小块子集，并针对在微控制器或是受限环境中运行进行了优化。

     <https://micropython.org/> || [micropython](<https://aur.archlinux.org/packages/micropython/>)AUR

  * **IronPython** — 与 [.NET](<../zh-cn/.NET.html> ".NET") 紧密集成的 Python 实现，可以调用 .NET 库，同时允许 .NET 程序使用 Python 库。

     <https://ironpython.net> || [ironpython-git](<https://aur.archlinux.org/packages/ironpython-git/>)AUR

Python 还有[其它多种实现](<https://zh.wikipedia.org/wiki/Python#.E5.AE.9E.E7.8E.B0> "wiki-zh:Python")。一些（例如 [Cinder](<https://github.com/facebookincubator/cinder>)）在大型科技公司内部得到使用。还有一些在历史上具有重要意义，但因最流行的实现已有改进而不再维护。 

###  替代 shell

[python](<https://archlinux.org/packages/?name=python>)包 软件包包含一个交互式 Python shell/REPL，可以通过 `python` 命令启动，还可以使用以下 shell： 

  * **bpython** — 为 Python 解释器提供美观界面。

     <https://bpython-interpreter.org/> || [bpython](<https://archlinux.org/packages/?name=bpython>)包

  * **IPython** — 功能强大的交互式 Python Shell。

     <https://ipython.org/> || [ipython](<https://archlinux.org/packages/?name=ipython>)包

  * **[Jupyter](<../zh-cn/Jupyter.html> "Jupyter")** — 由 IPython 提供支持的基于 Web 的计算应用程序。

     <https://jupyter.org/> || [jupyterlab](<https://archlinux.org/packages/?name=jupyterlab>)包、[jupyter-notebook](<https://archlinux.org/packages/?name=jupyter-notebook>)包

  * **ptpython** — 基于 [prompt-toolkit](<https://github.com/prompt-toolkit/python-prompt-toolkit>) 构建的高级 Python REPL。

     <https://github.com/prompt-toolkit/ptpython> || [ptpython](<https://aur.archlinux.org/packages/ptpython/>)AUR

##  软件包管理

在 Arch Linux 上，有多种方法可以安装 Python 软件包。 

###  Arch 官方仓库

大量流行的软件包可以在[官方仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方仓库")和 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 中找到。这是[安装系统范围内软件包的首选方式](<../zh-cn/%E7%B3%BB%E7%BB%9F%E7%BB%B4%E6%8A%A4.html#%E4%BD%BF%E7%94%A8%E5%8C%85%E7%AE%A1%E7%90%86%E5%99%A8%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6> "系统维护")，也是 Arch Linux 官方支持的唯一方法。 

###  第三方软件包

开发者在使用 Python 时，可能需要使用 Arch 仓库中没有的软件包或特定版本。推荐的做法是为每个项目使用单独的[虚拟环境](<#%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83>)隔离环境，避免与 `/usr` 中的系统软件包发生冲突。在虚拟环境中安装软件包可以使用以下工具： 

  * **[pip(1)](<https://man.archlinux.org/man/pip.1>)** — Python 官方的软件包安装工具。

     <https://pip.pypa.io/> || [python-pip](<https://archlinux.org/packages/?name=python-pip>)包

  * **pipx** — 专门的软件包安装工具，仅用于安装具有 CLI 入口点的软件包（而非库包）。

     <https://pypa.github.io/pipx/> || [python-pipx](<https://archlinux.org/packages/?name=python-pipx>)包

  * **Poetry** — 简化 Python 依赖管理和打包的工具。Poetry 是一个集开发、构建、发布和依赖管理于一体的工具。

     <https://python-poetry.org/> || [python-poetry](<https://archlinux.org/packages/?name=python-poetry>)包

  * **Conda** — Conda 提供适用于任何语言的软件包、依赖和环境管理。Conda 最初为 Python 而创建，广泛用于科学计算、数据科学和机器学习。Conda 是 [miniforge](<https://github.com/conda-forge/miniforge>) 社区 Python 发行版以及 [Anaconda](<https://repo.anaconda.com/>) 和 [Miniconda](<https://docs.anaconda.com/miniconda/>) Python 发行版的软件包管理器。

     <https://docs.conda.io> || [python-conda](<https://aur.archlinux.org/packages/python-conda/>)AUR

  * **uv** — 使用 Rust 编写的极快的 Python 软件包安装器和解析器。设计为常见 pip 和 pip-tools 工作流程的直接替代品。

     <https://docs.astral.sh/uv/> || [uv](<https://archlinux.org/packages/?name=uv>)包

`pip`、`pipx`、`poetry` 和 `uv` 从 [Python 软件包索引（PyPI）](<https://pypi.org/>)和其他索引中安装软件包。Conda 和 Miniconda 使用 [Anaconda 仓库](<https://repo.anaconda.com/>)。 

作为虚拟环境的替代方案，可以使用 `pip install --user` 将软件包安装到[用户方案](<https://pip.pypa.io/en/latest/user_guide/#user-installs>)，而不是 `/usr`。这种方法按用户而非项目分隔软件包，但虚拟环境通常是更好的选择。 

软件包管理的官方最佳实践见 [Python 打包用户指南（Python Packaging User Guide）](<https://packaging.python.org/>)。 

**注意：** 还有一些工具将 `pip` 与 `pacman` 集成，通过为指定的 PyPI 软件包自动生成 PKGBUILD 文件来实现，详见[创建软件包#PKGBUILD 生成器](<../zh-cn/%E5%88%9B%E5%BB%BA%E8%BD%AF%E4%BB%B6%E5%8C%85.html#PKGBUILD_%E7%94%9F%E6%88%90%E5%99%A8> "创建软件包")。

**提示：**[pipenv](<https://pipenv.pypa.io>) 提供用于管理 [Pipfile](<https://github.com/pypa/pipfile>)、`pip` 和 [virtualenv](</wzh/index.php?title=Virtualenv&action=edit&redlink=1> "Virtualenv（页面不存在）") 的统一的 CLI，可以通过 [python-pipenv](<https://archlinux.org/packages/?name=python-pipenv>)包 获取。

###  历史说明

之前，`easy_install`（[python-setuptools](<https://archlinux.org/packages/?name=python-setuptools>)包 的一部分）用于安装以 [Egg](<https://packaging.python.org/glossary/#term-Egg>) 格式分发的软件包。`easy_install` 和 Egg 已被 pip 和 [Wheel](<https://packaging.python.org/glossary/#term-Wheel>) 替代。详见 [pip vs easy_install](<https://packaging.python.org/en/latest/discussions/pip-vs-easy-install/>) 和[软件包格式（Package Formats）](<https://packaging.python.org/en/latest/discussions/package-formats/>)。 

早期版本的 `pip` 可以在系统范围内安装第三方软件包，但这导致了 [PEP668](<https://peps.python.org/pep-0668/>) 中提到的诸多问题。现在，系统范围的环境被标记为[外部管理环境（externally managed environment）](<https://packaging.python.org/en/latest/specifications/externally-managed-environments/>)，`pip` 不再允许系统范围的安装。 

##  GUI 绑定

以下是可用的[控件工具包（GUI 工具包）](<https://zh.wikipedia.org/wiki/%E9%83%A8%E4%BB%B6%E5%B7%A5%E5%85%B7%E7%AE%B1> "zhwp:部件工具箱")绑定： 

  * **Tkinter** — [Tk](<https://www.tcl.tk/>) GUI 工具包的标准 Python 接口。

     <https://docs.python.org/3/library/tkinter.html> || [python](<https://archlinux.org/packages/?name=python>)包

  * **Qt for Python (PySide2)** — [Qt](<../zh-cn/Qt.html> "Qt")5 的官方 Python 绑定。

     <https://www.qt.io/qt-for-python> || [pyside2](<https://aur.archlinux.org/packages/pyside2/>)AUR、[pyside2-tools](<https://aur.archlinux.org/packages/pyside2-tools/>)AUR

  * **Qt for Python (PySide6)** — [Qt](<../zh-cn/Qt.html> "Qt")6 的官方 Python 绑定。

     <https://www.qt.io/qt-for-python> || [pyside6](<https://archlinux.org/packages/?name=pyside6>)包、[pyside6-tools](<https://archlinux.org/packages/?name=pyside6-tools>)包

  * **pyQt** — Qt 的 Python 绑定集合。

     <https://riverbankcomputing.com/software/pyqt/intro> || [python-pyqt5](<https://archlinux.org/packages/?name=python-pyqt5>)包、[python-pyqt6](<https://archlinux.org/packages/?name=python-pyqt6>)包

  * **PyGObject** — 用于基于 GObject 的库（如 [GTK](<../zh-cn/GTK.html> "GTK")、[GStreamer](<../zh-cn/GStreamer.html> "GStreamer")、WebKitGTK、GLib 和 GIO）的 Python 绑定。

     <https://pygobject.readthedocs.io/> || [python-gobject](<https://archlinux.org/packages/?name=python-gobject>)包

  * **wxPython** — 封装 [wxWidgets](<https://www.wxwidgets.org/>) 的跨平台 Python GUI 工具包。

     <https://wxpython.org/> || [python-wxpython](<https://archlinux.org/packages/?name=python-wxpython>)包

若要在 Python 中使用它们，可能还需要安装相关的控件工具包软件包（例如，必须同时安装 [tk](<https://archlinux.org/packages/?name=tk>)包 才能使用 Tkinter）。 

##  提示与技巧

###  虚拟环境

Python 提供了创建隔离的**虚拟环境** 的工具，可以在其中安装软件包，而不与其他虚拟环境或系统软件包发生冲突。虚拟环境还可以在同一系统上运行不同版本的 Python。 

详见 [Python/虚拟环境](<../zh-cn/Python/%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83.html> "Python/虚拟环境")。 

###  在 Python Shell 中实现 Tab 补全功能

[Tab 自动补全](<https://docs.python.org/zh-cn/3.13/tutorial/interactive.html>)在交互式 shell 中默认可用。需要注意，readline 补全器只能补全全局命名空间中的名称。[python-jedi](<https://archlinux.org/packages/?name=python-jedi>)包 提供了更丰富的 Tab 自动补全体验 [[1]](<https://jedi.readthedocs.io/en/latest/docs/usage.html#tab-completion-in-the-python-shell>)。 

##  问题解决

###  更新 Python 后找不到模块

在升级 [python](<https://archlinux.org/packages/?name=python>)包 到新版本（例如从 3.10 升级到 3.11）后，基于 Python 的应用程序可能会输出 `No module named _模块名称_` 错误，表示已安装的依赖项 `_模块名称_` 不可用。 

这种情况发生在某个依赖项不支持当前的 Python 版本，或者根本没有安装。Python 软件包在安装时会放置在版本隔离的 site-packages 目录中（如果是全局安装，路径为 `/usr/lib/python _X.Y_ /site-packages`，如果是用户安装，路径为 `~/.local/lib/python _X.Y_ /site-packages/`，其中 `_X.Y_` 是类似“3.11”这样的版本号）。因此，每当 Python 版本进行小版本升级时，使用之前版本构建的基于 Python 的软件包必须重新构建，以便能在新版本中正常使用。 

需要注意，用户有责任重新构建非官方软件包，包括从 AUR 安装的基于 Python 的软件包。请参阅 [AUR#更新包](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html#%E6%9B%B4%E6%96%B0%E5%8C%85> "AUR")和[[常见问题#Q)_执行`pacman -Syu`时，终端显示某个共享库需要升级，但依赖它的程序没有升级，我该怎么做呢？]]。 

##  另见

###  官方

  * [官方 Python 文档](<https://docs.python.org/>)（可以通过 [python-docs](<https://archlinux.org/packages/?name=python-docs>)包 安装以离线阅读。）
  * [官方 Python 教程](<https://docs.python.org/zh-cn/3.13/tutorial/index.html>)

###  第三方

  * [Automate the Boring Stuff with Python](<https://automatetheboringstuff.com/>)⸺知识共享书籍
  * [Awesome Python](<https://github.com/vinta/awesome-python>)⸺精选 Python 资源列表
  * [A Byte of Python](<https://python.swaroopch.com/>)⸺知识共享书籍
  * [Cracking Codes With Python](<http://inventwithpython.com/cracking/>)⸺免费在线书籍
  * [Crash into Python](<https://stephensugden.com/crash_into_python/>)⸺免费教程
  * [Python Debugging With Pdb](<https://realpython.com/python-debugging-pdb/>)⸺`pdb`（Python 官方调试器）教程
  * [Dive Into Python](<https://diveintopython3.net/>)⸺知识共享书籍
  * [Fluent Python](<https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/>)⸺商业书籍
  * [Introducing Python](<https://www.oreilly.com/library/view/introducing-python-2nd/9781492051374/>)⸺商业书籍
  * [Invent Your Own Computer Games with Python](<http://inventwithpython.com/invent4thed/>)⸺免费在线书籍
  * [Learn Python](<https://learnpython.org/>)⸺免费交互式教程
  * [Learn Python the Hard Way](<https://learnpythonthehardway.org/>)⸺商业书籍
  * [Pythonspot Python Tutorials](<https://pythonspot.com>)⸺免费在线教程
  * [Think Python](<https://greenteapress.com/wp/think-python-2e//>)⸺知识共享书籍
