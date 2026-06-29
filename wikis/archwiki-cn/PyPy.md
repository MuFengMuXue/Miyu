**翻译状态：**

  * 本文（或部分内容）译自 [PyPy](<https://wiki.archlinux.org/title/PyPy> "arch:PyPy")，最近一次同步于 2024-7-29，若英文版本有所[更改](<https://wiki.archlinux.org/title/PyPy?diff=0&oldid=812973>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/PyPy_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[PyPy](<https://pypy.org/>) 是[Python](<../zh-cn/Python.html> "Python") 2.7、3.9 和 3.10 解释器的替代实现。PyPy 的优势在于速度、内存使用、沙箱和无堆栈性。它与 CPython 兼容，有[一些例外](<https://pypy.org/compat.html>)。PyPy 还可用于将 RPython 程序编译为 C 代码。 

##  安装

对于 Python 2.7，安装 [pypy](<https://archlinux.org/packages/?name=pypy>)包 软件包。对于 Python 3.10，安装 [pypy3](<https://archlinux.org/packages/?name=pypy3>)包 软件包。 

PyPy 安装在 `/opt/pypy/` 或 `/opt/pypy3` 中，主 pypy 可执行文件是 `bin/pypy-c`。 

##  用法

PyPy 的基本用法通过 `pypy` 或 `pypy3` 命令完成，其功能与 CPython 的用法类似。输入 
    
    $ pypy -h
    
以查看 `pypy` 选项列表。 

###  交互式解释器

若要加载 PyPy 交互式解释器，运行 
    
    $ pypy
    
###  从文件运行程序

要在 PyPy 中从文件运行 Python 程序，运行 
    
    $ pypy _example_.py
    
###  创建虚拟环境

用 PyPy 创建虚拟环境： 
    
    $ virtualenv --python=/usr/bin/pypy venv-pypy
    
更多信息，请参见 [Python/虚拟环境](<../zh-cn/Python/%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83.html> "Python/虚拟环境")。 

###  安装 pip

由于 PyPy 的 Python 软件包不作为 Arch 软件包发布，因此最方便的做法是以自己的用户身份安装所需软件： 
    
    $ pypy -m ensurepip --user
    $ pypy -m pip install --user --upgrade pip
    
有了 _pip_ ，你就可以安装任何需要的软件包，例如 `sqlalchemy`： 
    
    $ pypy -m pip install --user sqlalchemy
    
如果你想在全系统范围内安装软件包，只需以 root 用户身份运行前面的命令，而不使用 `--user`。请注意，这将导致软件包被安装到 `/opt/pypy` 中，而软件包管理器并不知道它们的存在。 

## EasyInstall

Python 库和程序可通过 EasyInstall 安装在 PyPy 中。 

###  EasyInstall 安装

EasyInstall 并不与 PyPy 软件包一起提供，而是在安装 **pip** 时自动安装，位于 `/opt/pypy/bin/easy_install` 中。 

###  安装 EasyInstall 软件包

要将 EasyInstall 软件包 `_package_name_` 安装到 PyPy 中，请输入 
    
    # /opt/pypy/bin/easy_install _package_name_
    
软件包位于 `/opt/pypy/site-packages`。安装的库和应用程序将位于 `/opt/pypy/bin`。通过 EasyInstall 安装在 PyPy 上的程序通常可以通过 `/opt/pypy/bin/program_name` 运行，其中 _program_name_ 是 PyPy 程序的名称。 

###  EasyInstall 软件包示例

以下操作将安装 Lamson 电子邮件框架： 
    
    # /opt/pypy/bin/easy_install lamson
    
以下命令将运行框架的 `gen -project` 命令： 
    
    $ /opt/pypy/bin/lamson gen -project _testproject_
    