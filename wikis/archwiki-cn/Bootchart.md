[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:Bootchart](<../zh-cn/Talk:Bootchart.html>)讨论)

[![](../File:Tango-preferences-desktop-locale-modified.png)](<../File:Tango-preferences-desktop-locale-modified.png>)**这篇文章或章节的[翻译](<../Project:%E8%B4%A1%E7%8C%AE.html#Translating> "Project:Contributing")质量不佳。**

**原因：** Last updated in 2017 ([490242](<../Special:%E5%B7%AE%E5%BC%82/490242.html> "Special:差异/490242")), out of sync with English page（在 [Talk:Bootchart#](<../zh-cn/Talk:Bootchart.html>) 中讨论）

使用 Bootchart 可以很方便地分析 Linux 启动流程，分析结果可以用来优化启动速度。包含的 bootchartd 服务负责记录及展示分析结果。 

**注意：** Bootchart 已经成为 systemd 的一部分，请参考 [Improve boot performance#Analyzing the boot process](</wzh/index.php?title=Improve_boot_performance&action=edit&redlink=1> "Improve boot performance（页面不存在）") 页面。本文介绍的是合并之前的老版本和bootchart2。

##  安装Bootchart

安装 [bootchart](<https://aur.archlinux.org/packages/bootchart/>)AUR。 

##  运行Bootchart

要运行 bootchart，需要将他添加到引导器的初始化进程选项，或者手动在init脚本（通常是rc.sysinit）中手动添加。不过需要注意的是，如果你是手动添加到init脚本的，那么也要手动停止它，总之，这种情况需要特别留意！ 

###  启动引导器设置

下面我们介绍常用的方法，即将原有引导选项复制一份，并在内核项后面添加`init=/usr/bin/bootchartd`. 方法参阅[kernel parameters](<../zh-cn/Kernel_parameters.html> "Kernel parameters"). 然后通过启动引导器引导bootchart。这样bootchart会在登录提示符出现的时候自动停止。 

##  生成分析结果图表

你可以通过运行下面的命令来生成分析结果图： 
    
    bootchart-render
    
确保运行命令的目录有写权限，程序就会生成一个名为'bootchart.png'的图像，这就是分析结果图。 

你需要事先安装Java运行环境并且在此之前设置正确。 

###  问题解决

Bootchart-render 如果无法生成 'bootchart.png' 图片并显示如下错误信息： 
    
    /var/log/bootchart.tgz not found
    
主要原因是 bootchartd 无法检测到启动过程何时停止。如该使用非 KDM 或 GDM 的启动管理器如 [SLIM](</wzh/index.php?title=SLiM_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "SLiM \(简体中文\)（页面不存在）") 或 entrance 时会发生这个问题。可以打开 `/sbin/bootchartd` 脚本并将这些程序加到 `exit_proc` 变量中： 
    
    # The processes we have to wait for
    local exit_proc="gdmgreeter gdm-binary kdm_greet kdm slim"
    
如果没有使用启动管理器，修改 `exit_proc` 变量为： 
    
    # The processes we have to wait for
    local exit_proc="login"
    
##  参考资料

  * [Bootchart主页](<https://www.bootchart.org/>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2021-11-07 ⓘ]
  * [如何快速启动上网本的 LWN 文章](<https://lwn.net/Articles/299483/>)写得很好，提供了许多快速启动的技巧，尽管许多不适合一般用户使用。(修改 X.org 内核 kernel 等)。
