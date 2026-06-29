  
**翻译状态：**

  * 本文（或部分内容）译自 [Jupyter](<https://wiki.archlinux.org/title/Jupyter> "arch:Jupyter")，最近一次同步于 2024-04-30，若英文版本有所[更改](<https://wiki.archlinux.org/title/Jupyter?diff=0&oldid=807077>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Jupyter_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Jupyter](<https://en.wikipedia.org/wiki/Project_Jupyter> "wikipedia:Project Jupyter") 是一个为编程、数学和数据科学生成基于浏览器的交互式环境的项目。它通过插件("kernel")支持多种语言，例如[Python](<../zh-cn/Python.html> "Python"), [Ruby](<../zh-cn/Ruby.html> "Ruby"), [Haskell](</wzh/index.php?title=Haskell&action=edit&redlink=1> "Haskell（页面不存在）"), [R](</wzh/index.php?title=R&action=edit&redlink=1> "R（页面不存在）"), [Scala](<../zh-cn/Scala.html> "Scala"), [Julia](<../zh-cn/Julia.html> "Julia") 和 [Kotlin](<https://en.wikipedia.org/wiki/Kotlin_\(programming_language\)> "wikipedia:Kotlin \(programming language\)"). 

JupyterLab 是“Jupyter 的下一代笔记本界面”，而 Jupyter Notebook 是原始版本。请参阅[Jupyter](<https://jupyter.org/>)网站进行比较。 

##  安装

  * 对于 JupyterLab, [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [jupyterlab](<https://archlinux.org/packages/?name=jupyterlab>)包 。
  * 对于 Jupyter Notebook, [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [jupyter-notebook](<https://archlinux.org/packages/?name=jupyter-notebook>)包 。

要为当前用户安装第三方 Jupyter Notebook 扩展，请在执行`jupyter nbextension install`时使用`--user`选项。要对[JupyterLab扩展的安装](<https://jupyterlab.readthedocs.io/en/stable/user/extensions.html?highlight=advanced%20usage#advanced-usage>)执行相同的操作，请设置以下[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")： 
    
    JUPYTERLAB_DIR=$HOME/.local/share/jupyter/lab
    
并通过运行`jupyter lab paths`进行验证。然后按照安装说明进行操作。 

##  运行

要启动JupyterLab，请执行: 
    
    $ jupyter lab
    
要启动Jupyter Notebook，请执行: 
    
    $ jupyter notebook
    
如果 Web 浏览器未自动打开，请手动打开标准输出上给出的 URL。 

若要启动 JupyterLab 而不启动浏览器，并使JupyterLab侦听端口`9999` ，请运行 
    
    $ jupyter lab --no-browser --port 9999
    
若希望更改默认的行为，请编辑 
    
    ~/.jupyter/jupyter_lab_config.py
    
    c.ExtensionApp.open_browser = False
    c.ServerApp.port = 9999

## Kernels

###  C++

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")[cling-jupyter-git](<https://aur.archlinux.org/packages/cling-jupyter-git/>)AUR 。 

### Haskell

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [ihaskell-git](<https://aur.archlinux.org/packages/ihaskell-git/>)AUR ，然后执行`ihaskell install`。 

### Julia

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [julia](<https://archlinux.org/packages/?name=julia>)包 ，执行 `julia` 获得 REPL 提示。然后运行： 
    
    using Pkg
    Pkg.add("IJulia")
    
有关包管理的更多详细信息，请参阅 [Julia](<https://docs.julialang.org/en/v1/stdlib/Pkg/>)手册。 

### Python

默认情况下通过[python-ipykernel](<https://archlinux.org/packages/?name=python-ipykernel>)包使用 Python 3 kernel。 

### Perl

安装kernel并运行交互式[perl](</wzh/index.php?title=Perl&action=edit&redlink=1> "Perl（页面不存在）") shell 至少一次： 
    
    cpanm Devel::IPerl
    iperl
    
然后按下 `Ctrl+d`。现在运行 jupyter，可以看到 perl。 

### R

按照 [IR Kernel](<https://github.com/IRkernel/IRkernel>)中的`Installation`进行操作。 

### Rust

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")[evcxr_jupyter](<https://aur.archlinux.org/packages/evcxr_jupyter/>)AUR 。 

### SageMath

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [sagemath](<https://archlinux.org/packages/?name=sagemath>)包 。 

### Octave

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [jupyter-octave_kernel](<https://aur.archlinux.org/packages/jupyter-octave_kernel/>)AUR。 

### Maxima

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [maxima-jupyter-git](<https://aur.archlinux.org/packages/maxima-jupyter-git/>)AUR。 

### Cadabra

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")[cadabra2](<https://aur.archlinux.org/packages/cadabra2/>)AUR。 

### Kotlin

请参考 [Kotlin Jupyter integration project](<https://github.com/Kotlin/kotlin-jupyter>)。 

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 在Python环境外，不鼓励使用pip。请参阅[Python#Package management](<../zh-cn/Python.html#Package_management> "Python").（在 [Talk:Jupyter](<../zh-cn/Talk:Jupyter.html>) 中讨论）

使用pip安装Kotlin kernel: 
    
    pip install kotlin-jupyter-kernel
    
Kernel自动与jupyter绑定。 

##  JupyterLab 中的交互式小部件

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 链接的 issue 是特定于 [python-matplotlib](<https://archlinux.org/packages/?name=python-matplotlib>)包 的，本节的标题过于笼统。链接的注释说使用 `%matplotlib ipympl` ，而此处的以下说明包含 `%matplotlib widget` 。最好链接到有关 matplotlib 的magic命令的正确文档。（在 [Talk:Jupyter](<../zh-cn/Talk:Jupyter.html>) 中讨论）

为了在 Jupyter Lab 中启用交互式小部件，请根据此[此 github issue](<https://github.com/matplotlib/ipympl/issues/9#issuecomment-341908855>)[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [python-ipympl](<https://archlinux.org/packages/?name=python-ipympl>)包 和 [jupyterlab-widgets](<https://archlinux.org/packages/?name=jupyterlab-widgets>)包。之后，在笔记本中使用： 
    
    %matplotlib widget
    
安装扩展后，不要忘记重新启动 JupyterLab 实例。 

在扩展操作后，执行 **RMB- >Clear Outputs of All Cells**也可能有所帮助。 

##  参见

  * [Official website](<https://jupyter.org/>)
  * [JupyterHub](<../zh-cn/JupyterHub.html> "JupyterHub")
