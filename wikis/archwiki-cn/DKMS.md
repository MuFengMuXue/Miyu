**翻译状态：**

  * 本文（或部分内容）译自 [Dynamic Kernel Module Support](<https://wiki.archlinux.org/title/Dynamic_Kernel_Module_Support> "arch:Dynamic Kernel Module Support")，最近一次同步于 2024-06-01，若英文版本有所[更改](<https://wiki.archlinux.org/title/Dynamic_Kernel_Module_Support?diff=0&oldid=801840>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Dynamic_Kernel_Module_Support_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

摘自[维基百科](<https://zh.wikipedia.org/wiki/%E5%8A%A8%E6%80%81%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97%E6%94%AF%E6%8C%81> "zhwp:动态内核模块支持")： 

    动态内核模块支持（DKMS）是用来生成 Linux 的内核模块的一个框架，这种模块的源代码一般不在 Linux 内核源代码树中。当新的内核安装时，DKMS 支持的内核模块会自动重建。

这意味着你不再需要等待某个公司、项目组或者包维护者释出新版本的内核模块。自从 pacman 支持[钩子](<../zh-cn/Pacman.html#%E9%92%A9%E5%AD%90> "Pacman")之后，内核更新时就会自动重新构建模块。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [dkms](<https://archlinux.org/packages/?name=dkms>)包 包和目标内核的头文件。例如，标准 [linux](<https://archlinux.org/packages/?name=linux>)包 内核的头文件可以用软件包 [linux-headers](<https://archlinux.org/packages/?name=linux-headers>)包 安装。其他内核也有其相应的头文件包。 

有许多位于内核源码树之外的内核模块都有 DKMS 变体；有一些位于[官方软件仓库](<https://archlinux.org/packages/?&q=dkms>)，大多数可以在 [AUR](<https://aur.archlinux.org/packages/?SeB=n&K=dkms>) 找到。 

##  升级

虽然在内核升级时，DKMS 的编译自动执行，但是依然有可能编译报错。所以需要特别注意 pacman 的输出。当系统需要这些模块才能启动，或者使用不在[官方软件仓库](<../zh-cn/Official_repositories.html> "Official repositories")中的内核时，需要额外注意。 

若要应用内核中的变化、修复 bug、或是添加特性，请在重启前先升级 DKMS 包。 

##  使用方法

如何手动调用DKMS： 

可以通过执行以下命令来使能使用DKMS时的Tab补全： 
    
    # source /usr/share/bash-completion/completions/dkms
    
###  列出内核模块

列出当前模块的状态，版本，包括源码树内的模块： 
    
    # dkms status
    
###  重新构建模块

为当前内核重新构建所有的模块： 
    
    # dkms autoinstall
    
或者为指定版本的内核构建： 
    
    # dkms autoinstall -k 3.16.4-1-ARCH
    
为当前内核构建一个特定的模块（例如: 对于当前内核）： 
    
    # dkms install -m nvidia -v 334.21
    
或者简单地： 
    
    # dkms install nvidia/334.21
    
###  移除模块

移除一个内核模块（旧的内核模块并不会被自动移除）： 
    
    # dkms remove -m nvidia -v 331.49 --all
    
或者简单的： 
    
    # dkms remove nvidia/331.49 --all
    
如果你卸载了 [dkms](<https://archlinux.org/packages/?name=dkms>)包 包，那么以前构建内核模块使用的相关文件信息就会丢失。如果这样，去 `/usr/lib/modules/kernel_release` 和 `/var/lib/dkms/package_name` 下删除不再需要的文件和目录。 

##  创建 DKMS 包

请参见 [DKMS 包指南](<../zh-cn/DKMS_package_guidelines.html> "DKMS package guidelines")。 

##  相关链接

  * [Linux Journal: 探寻动态内核模块支持](<https://www.linuxjournal.com/article/6896>)
