**翻译状态：**

  * 本文（或部分内容）译自 [Octave](<https://wiki.archlinux.org/title/Octave> "arch:Octave")，最近一次同步于 2024-03-07，若英文版本有所[更改](<https://wiki.archlinux.org/title/Octave?diff=0&oldid=802433>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Octave_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Matlab](<../zh-cn/MATLAB.html> "Matlab")
  * [Sage-mathematics](</wzh/index.php?title=Sage-mathematics&action=edit&redlink=1> "Sage-mathematics（页面不存在）")
  * [Mathematica](<../zh-cn/Mathematica.html> "Mathematica")

援引自[Octave 官网](<https://www.gnu.org/software/octave/>): 

    GNU Octave 是一种解释性的高级程序设计语言, 主要应用在数值计算领域。其拥有线性和非线性问题求解，以及执行其他数值分析的能力，还为数据可视化与数据操作提供了丰富的图形功能。 Octave通常的使用方式是交互式命令行，但其也可以用来编写非交互式程序。 Octave语言与Matlab非常相似，因此在两个平台编写的大部分程序都可以很容易移植。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [octave](<https://archlinux.org/packages/?name=octave>)包软件包。 

打开GUI界面`octave --gui` ,或者打开命令行界面`octave-cli`

###  其他可供选择的图形界面

默认的 _octave_ 图形界面 已经包含在了 [octave](<https://archlinux.org/packages/?name=octave>)包 软件包中。除此之外，你还可以选择使用下列非官方的图形界面： 

  * **Cantor** — 一个图形用户界面，其后端的数学运算可以由以下软件之一提供 (Scilab, Maxima, Octave, R, Julia and others).

     <https://edu.kde.org/cantor/> || [cantor](<https://archlinux.org/packages/?name=cantor>)包

  * **[JupyterLab](<../zh-cn/Jupyter.html> "Jupyter")** — 一个基于浏览器的交互式环境，支持多种语言作为后端，也包括Octave。

     <https://github.com/jupyterlab/jupyterlab> || [jupyterlab](<https://archlinux.org/packages/?name=jupyterlab>)包+[jupyter-octave_kernel](<https://aur.archlinux.org/packages/jupyter-octave_kernel/>)AUR

###  性能

Octave默认使用[blas](<https://archlinux.org/packages/?name=blas>)包包进行线性代数计算。然而blas的实现并未利用到现代CPU的指令集。[blas-openblas](<https://archlinux.org/packages/?name=blas-openblas>)包作为blas的直接替代，安装该包可提升计算性能。根据硬件配置可选择其它BLAS实现，Intel处理器可安装[intel-oneapi-mkl](<https://archlinux.org/packages/?name=intel-oneapi-mkl>)包包，NVIDIA图形处理器可安装[cuda](<https://archlinux.org/packages/?name=cuda>)包。 

下面的代码估计了不同情况下计算NxN矩阵乘法的性能，以GFLOPS计： 
    
    test_program.m
    
    N = 4096;
     A = single(rand(N, N));
     B = single(rand(N, N));
     start = clock();
     C = A * B;
     elapsedTime = etime(clock(), start);
     gFlops = 2 * N * N * N / (elapsedTime * 1e9)

在Intel Core i7-9750H上运行该代码： 
    
    octave ~/test_program.m
    
    gFlops = 3.7222

安装openblas后，以单线程运行该代码： 
    
    OMP_NUM_THREADS=1 octave ~/test_program.m
    
    gFlops = 121.55

使用全部12个线程运行该代码： 
    
    OMP_NUM_THREADS=12 octave ~/test_program.m
    
    gFlops = 281.33

## Octave-Forge

Octave提供一系列的外部包，类似于Matlab的工具箱, 参见 [Octave-Forge](<https://octave.sourceforge.io/>).完整包列表参见[这里](<https://octave.sourceforge.io/packages.php>). 

这些外部包可以 [#通过Octave自带安装器安装](<#%E9%80%9A%E8%BF%87Octave%E8%87%AA%E5%B8%A6%E5%AE%89%E8%A3%85%E5%99%A8%E5%AE%89%E8%A3%85>)或者 [#通过AUR安装](<#%E9%80%9A%E8%BF%87AUR%E5%AE%89%E8%A3%85>). 

###  通过Octave自带安装器安装

外部包可以通过Octave自带安装器进行管理。 一般情况下他们会被安装到 ~/octave, 当使用`-global`选项的时候会被安装到一个系统目录。 

安装一个外部包： 
    
    octave:1> pkg install -forge packagename
    
**注意：** 一些外部包, 例如 `control`, 需要 [gcc-fortran](<https://archlinux.org/packages/?name=gcc-fortran>)包 包来进行编译和安装

卸载一个外部包: 
    
    octave:3> pkg uninstall packagename
    
一些包可以被Octave自动加载，对于那些没有自动加载的包: 
    
    octave:4> pkg load packagename
    
不推荐加载全部的包，这可能会影响性能并造成命名冲突。如果需要加载全部包，可以调用： 
    
    octave:5> cellfun (@(x) pkg ("load", x.name), pkg ("list"));
    
通过`pkg list`可以查看被加载的包,已加载的包会带有星号. 

一个确保所有包都在Octave启动时加载的方法: 
    
    /usr/share/octave/site/m/startup/octaverc
    
    ## System-wide startup file for Octave.
    ##
    ## This file should contain any commands that should be executed each
    ## time Octave starts for every user at this site. 
     pkg load all

###  通过AUR安装

一些包可以在AUR ([search packages](<https://aur.archlinux.org/packages?O=0&K=octave-&do_Search=Go>))中找到. 

适用于 Arch 的 Octave-forge 可以通过 [Octave-forge helper scripts for Archlinux](<https://github.com/drizzd/octave-forge-archlinux#readme>) 实现半自动更新. 

##  绘制图表

Qt是默认的绘图后端: 
    
    >> available_graphics_toolkits
    ans =
    {
      [1,1] = fltk
      [1,2] = qt
    }
    >> graphics_toolkit
    ans = qt
    
你也可以选择FLTK,或者[gnuplot](<https://archlinux.org/packages/?name=gnuplot>)包然后通过以下命令切换绘图后端: 
    
    >> graphics_toolkit("gnuplot");
    
将它添加进`~/.octaverc`以使变更一直有效. 

##  读取电子表格

你可以使用`odsread`或者`xlsread`打开`.ods`, `.xls`以及`.xlsx`格式的文件,这需要安装[octave-io](<https://aur.archlinux.org/packages/octave-io/>)AUR包: 
    
    octave:1> odsread('myfile.ods');
    octave:1> xlsread('myfile.xls');
    octave:1> xlsread('myfile.xlsx');
    
###  转换成CSV格式

也可以先使用[LibreOffice](<../zh-cn/LibreOffice.html> "LibreOffice") Calc ([不超过1024列](<https://bugs.documentfoundation.org/show_bug.cgi?id=50916>))或[Calligra Sheets](<https://www.calligra.org/sheets/>)([calligra](<https://archlinux.org/packages/?name=calligra>)包,不超过32768列)把电子表格转换`.csv`格式. 

待转换完成后您可以使用Octave内置函数`csvread`来读取`.csv`格式文件: 
    
    octave:1> csvread('myfile.csv');
    
##  疑难解答

### Zsh Undecodable Token

如果显示了下面的错误： 
    
    undecodable token: b(hex)[23m
    
安装[grml-zsh-config](<https://archlinux.org/packages/?name=grml-zsh-config>)包并重新登录。 

### vi Mode Undecodable Token

为vi-mode模式配置`.inputrc`的用户，例如使用下列配置的： 
    
    ~/.inputrc
    
    $include /etc/inputrc
    set editing-mode vi
    $if mode=vi
    
    set show-mode-in-prompt on
    set vi-ins-mode-string \1\e[6 q\2
    set vi-cmd-mode-string \1\e[2 q\2
    
    set keymap vi-command
    # these are for vi-command mode
    Control-l: clear-screen
    Control-a: beginning-of-line
    
    set keymap vi-insert
    # these are for vi-insert mode
    Control-l: clear-screen
    Control-a: beginning-of-line
    
    $endif

可能会遇到Octave图形用户界面命令行提示`q>> undecodable token: \001b(hex)[6\0020(hex)`. 为Octave关闭`show-mode-in-prompt`设置可解决该问题，将上例的`.inputrc`改为： 
    
    ~/.inputrc
    
    $include /etc/inputrc
    set editing-mode vi
    $if mode=vi
    
    $if Octave
    set show-mode-in-prompt off
    $else
    set show-mode-in-prompt on
    set vi-ins-mode-string \1\e[6 q\2
    set vi-cmd-mode-string \1\e[2 q\2
    
    set keymap vi-command
    # these are for vi-command mode
    Control-l: clear-screen
    Control-a: beginning-of-line
    
    set keymap vi-insert
    # these are for vi-insert mode
    Control-l: clear-screen
    Control-a: beginning-of-line
    $endif
    
    $endif

##  另见

  * [Wikipedia:GNU Octave](<https://en.wikipedia.org/wiki/GNU_Octave> "wikipedia:GNU Octave")
