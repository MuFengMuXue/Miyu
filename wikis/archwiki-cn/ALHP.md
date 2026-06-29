第三方的 ALHP 仓库使用优化标志以及先进指令集（如SSE3、AVX512）重新编译了Arch Linux中的core、extra和multilib仓库中的部分软件包，使得设备获得性能提升。 

**警告：** 使用此仓库可能会出现部分包更新不及时、版本不一致从而导致问题的情况。

##  配置

**警告：** 以下步骤为必需步骤。如果不执行此步骤，可能会导致您的系统无法启动，并且您将需要降级任何您可能已经升级的软件包。

执行以下命令以查询CPU支持的特性级别
    
    /lib/ld-linux-x86-64.so.2 --help
    
如果输出为以下内容
    
    Subdirectories of glibc-hwcaps directories, in priority order:
      x86-64-v4（supported, searched)
      x86-64-v3 (supported, searched)
      x86-64-v2 (supported, searched)
    
那么请将 `pacman.conf` 修改为以下样式
    
    # 省略以上内容
    
    [core-x86-64-v4]
    Include = /etc/pacman.d/alhp-mirrorlist
    
    [extra-x86-64-v4]
    Include = /etc/pacman.d/alhp-mirrorlist
    
    [core-x86-64-v3]
    Include = /etc/pacman.d/alhp-mirrorlist
    
    [extra-x86-64-v3]
    Include = /etc/pacman.d/alhp-mirrorlist
    
    [core-x86-64-v2]
    Include = /etc/pacman.d/alhp-mirrorlist
    
    [extra-x86-64-v2]
    Include = /etc/pacman.d/alhp-mirrorlist
    
    [core]
    Include = /etc/pacman.d/mirrorlist
    
    [extra]
    Include = /etc/pacman.d/mirrorlist
    
    # 如果需要 [multilib] 支持
    
    [multilib-x86-64-v4]
    Include = /etc/pacman.d/alhp-mirrorlist
    
    [multilib-x86-64-v3]
    Include = /etc/pacman.d/alhp-mirrorlist
    
    [multilib-x86-64-v2]
    Include = /etc/pacman.d/alhp-mirrorlist
    
    [multilib]
    Include = /etc/pacman.d/mirrorlist
    
    # 省略以下内容
    
如果输出为以下内容
    
    Subdirectories of glibc-hwcaps directories, in priority order:
      x86-64-v4
      x86-64-v3 (supported, searched)
      x86-64-v2 (supported, searched)
    
那么请将pacman.conf修改为以下样式
    
    # 省略以上内容
    
    [core-x86-64-v3]
    Include = /etc/pacman.d/alhp-mirrorlist
    
    [extra-x86-64-v3]
    Include = /etc/pacman.d/alhp-mirrorlist
    
    [core-x86-64-v2]
    Include = /etc/pacman.d/alhp-mirrorlist
    
    [extra-x86-64-v2]
    Include = /etc/pacman.d/alhp-mirrorlist
    
    [core]
    Include = /etc/pacman.d/mirrorlist
    
    [extra]
    Include = /etc/pacman.d/mirrorlist
    
    # 如果需要 [multilib] 支持
    
    [multilib-x86-64-v3]
    Include = /etc/pacman.d/alhp-mirrorlist
    
    [multilib-x86-64-v2]
    Include = /etc/pacman.d/alhp-mirrorlist
    
    [multilib]
    Include = /etc/pacman.d/mirrorlist
    
    省略以下内容
    
以此类推。 

##  安装密钥环和镜像列表

从 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 安装 alhp-keyring 和 alhp-mirrorlist。 

使用 `yay` 安装的示例： 
    
    yay -S alhp-keyring alhp-mirrorlist
    
`alhp-keyring` 提供 ALHP 当前使用的签名密钥，`alhp-mirrorlist` 提供一组镜像列表供选择。 

##  更新软件包数据库并升级
    
    sudo pacman -Syu
    
##  不想用ALHP了？移除ALHP仓库

要禁用 ALHP，删除 `/etc/pacman.conf` 中所有 _x86-64-vX_ 条目，并删除 `alhp-keyring` 和 `alhp-mirrorlist`。 

之后，使用以下命令刷新 pacman 的数据库并降级所有软件包： 
    
    sudo pacman -Syuu
    