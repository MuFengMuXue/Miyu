**Arch Linux 中文社区仓库** （也可简称为 archlinuxcn 或 archcn 仓库）是由 Arch Linux 中文社区驱动的[非官方软件仓库](<../zh-cn/%E9%9D%9E%E5%AE%98%E6%96%B9%E7%94%A8%E6%88%B7%E4%BB%93%E5%BA%93.html> "非官方软件仓库")，包含许多官方仓库未提供的额外的软件包，以及已有软件的 git 版本等变种。一部分软件包的打包脚本来源于 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR")，但也有许多包与 AUR 不一样。 

查看打包脚本及可用包列表、报告问题、申请打包新软件包，请访问[在 GitHub 上的项目](<https://github.com/archlinuxcn/repo>)。 

仓库主地址：`<https://repo.archlinuxcn.org/>`

（仓库服务器位于欧洲，中国大陆、香港、美国、欧洲等地均有镜像。） 

使用方法：在 `/etc/pacman.conf` 文件末尾添加以下两行（或者从[这里](<https://github.com/archlinuxcn/mirrorlist-repo>)选择一个镜像）： 
    
    /etc/pacman.conf
    
    [archlinuxcn]
    Server = <https://repo.archlinuxcn.org/$arch>

之后安装 [archlinuxcn-keyring](<https://github.com/archlinuxcn/repo/tree/master/archlinuxcn/archlinuxcn-keyring>)CNRepo 包以导入 [GPG 密钥](<../zh-cn/Pacman/%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%AD%BE%E5%90%8D.html> "Pacman/软件包签名")。安装 [archlinuxcn-mirrorlist-git](<https://github.com/archlinuxcn/repo/tree/master/archlinuxcn/archlinuxcn-mirrorlist-git>)CNRepo 包可以获得一份[镜像源](<../zh-cn/%E9%95%9C%E5%83%8F%E6%BA%90.html> "镜像")列表，以便在 `pacman.conf` 中直接引入。推荐同时更新系统： 

  1. 更新数据库并安装 [archlinuxcn-keyring](<https://github.com/archlinuxcn/repo/tree/master/archlinuxcn/archlinuxcn-keyring>)CNRepo：
    
    # pacman -Sy archlinuxcn-keyring
    
  2. 更新系统并安装镜像仓库列表。分为两步是为了让安装的 keyring 生效：
    
    # pacman -Su archlinuxcn-mirrorlist-git
    
  3. 在 `/etc/pacman.conf` 文件`[archlinuxcn]`处添加以下内容，以启用镜像列表 
         
         /etc/pacman.conf
         
         Include = /etc/pacman.d/archlinuxcn-mirrorlist
         
本仓库同时提供 [debuginfod](<https://wiki.archlinux.org/title/Debuginfod> "arch:Debuginfod") 服务（支持部分有调试符号的包；不可用镜像站点的地址），设置以下[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")即可（此环境变量会被 [archlinuxcn-mirrorlist-git](<https://github.com/archlinuxcn/repo/tree/master/archlinuxcn/archlinuxcn-mirrorlist-git>)CNRepo 自动设置，但有些情况可能并不生效）： 
    
    DEBUGINFOD_URLS="<https://debuginfod.archlinux.org> <https://repo.archlinuxcn.org>"
    