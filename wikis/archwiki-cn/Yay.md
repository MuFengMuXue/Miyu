相关文章

  * [AUR 助手](<../zh-cn/AUR_%E5%8A%A9%E6%89%8B.html> "AUR 助手")
  * [pacman](<../zh-cn/Pacman.html> "Pacman")

[Yay](<https://github.com/Jguer/yay>) 是一个适用于Arch Linux的命令行软件，主要用于帮助用户从Arch User Repository([AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR"))构建和安装软件包。它可以做的事情包括： 

  1. 自动解决软件包间的依赖关系。
  2. 动态地搜索、编译和构建包。
  3. 安装与管理 AUR中的包（ yay 的命令与 pacman 基本一致，例如 yay -S 对应 pacman -S，但 yay 能同时处理官方仓库和 AUR。 ）。

**警告：** Arch Linux 不对 AUR 助手引发的问题提供支持。您应熟悉[自行构建过程](<../zh-cn/Arch_User_Repository.html#%E5%AE%89%E8%A3%85%E4%B8%8E%E6%9B%B4%E6%96%B0%E8%BD%AF%E4%BB%B6%E5%8C%85> "Arch User Repository")以准备好解决遇到的问题。

##  安装

在开始之前，请确保您已安装 [base-devel](<https://archlinux.org/packages/?name=base-devel>)包 [git](<https://archlinux.org/packages/?name=git>)包

安装base-devel, git： 
    
    # pacman -S git base-devel
    
克隆 [yay](<https://aur.archlinux.org/yay.git>) 源码： 
    
    $ git clone <https://aur.archlinux.org/yay.git>
    
如果你在中国构建yay，强烈建议你克隆 [yay-bin](<https://aur.archlinux.org/yay-bin.git>) 而非 [yay](<https://aur.archlinux.org/yay.git>)。这是由于克隆和构建 `yay-bin` 相比 `yay` 不会遇到被墙问题，克隆 `yay-bin` 构建yay是因为 `yay` 是以Go语言构建的yay，可能会受到被墙影响： 
    
    $ git clone <https://aur.archlinux.org/yay-bin.git>
    $ cd yay-bin
    
进入yay文件夹： 
    
    $ cd yay
    
构建 yay 并在构建成功后安装生成的软件包： 
    
    $ makepkg -si
    
如果您想一次完成所有操作，请使用以下命令： 
    
    $ pacman -S git base-devel && git clone <https://aur.archlinux.org/yay.git> && cd yay && makepkg -si
    
如果不想编译安装，也可以添加 [[archlinuxcn]](<../zh-cn/Arch_Linux_%E4%B8%AD%E6%96%87%E7%A4%BE%E5%8C%BA%E4%BB%93%E5%BA%93.html> "Arch Linux 中文社区仓库") 仓库来安装 [yay](<https://github.com/archlinuxcn/repo/tree/master/archlinuxcn/yay>)[CNRepo](<../zh-cn/Arch_Linux_%E4%B8%AD%E6%96%87%E7%A4%BE%E5%8C%BA%E4%BB%93%E5%BA%93.html> "Arch Linux 中文社区仓库")。 

##  命令

命令  | 描述   
---|---  
yay  | 升级系统，相当于yay -Syu   
yay <搜索词> | 显示包安装选择菜单   
yay -Bi <目录> | 安装依赖并构建本地PKGBUILD   
yay -G <AUR Package> | 从ABS或AUR下载PKGBUILD (yay v12.0+)   
yay -Gp <AUR Package> | 打印ABS或AUR的PKGBUILD到stdout   
yay -Ps  | 打印系统统计信息   
yay -Syu --devel  | 执行系统升级，但同时检查开发包的更新   
yay -Syu --timeupdate  | 执行系统升级并使用PKGBUILD修改时间（不是版本号）来确定更新   
yay -Wu <AUR Package> | 取消对包的投票 (需要设置AUR_USERNAME和AUR_PASSWORD环境变量) (yay v11.3+)   
yay -Wv <AUR Package> | 投票支持包 (需要设置AUR_USERNAME和AUR_PASSWORD环境变量) (yay v11.3+)   
yay -Y --combinedupgrade --save  | 使组合升级成为默认模式   
yay -Y --gendb  | 生成用于开发更新的开发包数据库   
yay -Yc  | 清理不需要的依赖   
yay -S 包名  | 安装软件包   
yay -Syu  | 升级所有包（含 AUR）   
yay -Sc  | 清理缓存文件   
yay -Rns 包名  | 删除软件包和依赖及配置   
yay -Rs 包名  | 删除软件包和依赖   
yay -R 包名  | 删除软件包   
  
更多命令请通过 man yay 查看 

如果发现命令介绍有错误请帮忙修改 
