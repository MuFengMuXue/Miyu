[bookget](<https://github.com/deweizhu/bookget>) 是一款数字古籍图书下载工具，已支持约 50+ 个数字图书馆。 

**注意：** 本文及此项目代码仅供学习研究使用。

##  安装

### AUR

有以下三个 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 包可选： 

  * [bookget](<https://aur.archlinux.org/packages/bookget/>)AUR：从 Github 发布获取源代码。
  * [bookget-git](<https://aur.archlinux.org/packages/bookget-git/>)AUR：通过 Git 获取源代码并构建。
  * [bookget-bin](<https://aur.archlinux.org/packages/bookget-bin/>)AUR：从 Github 获取已经编译好的二进制可执行文件，仅支持 x86_64 架构（因为官方仅构建了 amd64 版本）。

###  手动安装

使用官方提供的安装方法，执行： 
    
    $ wget -O bookget https://github.com/deweizhu/bookget/releases/download/_版本号_ /bookget-linux
    $ chmod +x bookget
    # cp bookget /usr/local/bin/
    
例如：对于版本 25.0601，可以执行： 
    
    $ wget -O bookget <https://github.com/deweizhu/bookget/releases/download/v25.0601/bookget-linux>
    $ chmod +x bookget
    # cp bookget /usr/local/bin/
    
或者，使用源代码编译安装（需要 [golang](<../zh-cn/Go.html> "Go") 开发环境）： 
    
    git clone <https://github.com/deweizhu/bookget.git>
    cd bookget
    
    # 本地开发时可直接运行
    make linux-amd64    # 编译Linux版本
    make windows-amd64  # 编译Windows版本
    make release        # 编译所有平台

##  用法

参见 [Wiki](<https://github.com/deweizhu/bookget/wiki>)。 

要通过链接下载一本古籍： 
    
    $ bookget
    
    Enter an URL:
    -> _古籍的 URL_

或执行： 
    
    $ bookget "_古籍 URL_ "

##  参见

  * [Github 仓库](<https://github.com/deweizhu/bookget>)
  * [书格 _bookget 专区_](<https://www.shuge.org/meet/topic/80138/>)
