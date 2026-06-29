[BlackArch](<https://blackarch.org/>) 是一个基于 Arch Linux 的渗透测试发行版，提供了大量的网络安全工具。它是专为渗透测试人员和安全研究人员创建的开放源代码的发行版。该存储库包含 3000 多个可以单独或成组安装的工具。BlackArch 与现有的 Arch Linux 安装相容。 

##  安装

###  安装教程可能不完整，请下载blackarch 官方 [PDF](<https://blackarch.org/blackarch-guide-zh.pdf>)

以 `root` 身份运行 <https://blackarch.org/strap.sh> 并按照说明进行操作： 
    
    $ curl -O <https://blackarch.org/strap.sh>
    
验证 `SHA1` ： 
    
    $ echo 26849980b35a42e6e192c6d9ed8c46f0d6d06047 strap.sh | sha1sum -c
    
设置执行权限： 
    
    $ chmod +x strap.sh
    
运行 strap.sh： 
    
    $ sudo ./strap.sh
    
添加中国大陆 blackarch 镜像提高下载速度，在 `/etc/pacman.conf` 文件末尾添加镜像： 
    
    ## 南京大学 (江苏南京) (ipv4, ipv6, http, https)
    [blackarch]
    Server = https://mirrors.nju.edu.cn/blackarch/$repo/os/$arch
    
    ## SJTUG 软件源镜像服务 (上海) (ipv4, ipv6, https)
    [blackarch]
    Server = https://mirror.sjtu.edu.cn/blackarch/$repo/os/$arch
    
    ## 清华大学 (北京) (ipv4, ipv6, http, https)
    [blackarch]
    Server = https://mirrors.tuna.tsinghua.edu.cn/blackarch/$repo/os/$arch
    
    ## 中国科学技术大学 (安徽合肥) (ipv4, ipv6, http, https)
    [blackarch]
    Server = https://mirrors.ustc.edu.cn/blackarch/$repo/os/$arch
    
    ## 阿里云 (Global CDN) (ipv4, ipv6, http, https)
    [blackarch]
    Server = https://mirrors.aliyun.com/blackarch/$repo/os/$arch
    
然后请安装 `blackarch-keyring` 包以导入 GPG key： 
    
    $ pacman -Sy blackarch-keyring
    
按照 [wiki](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方仓库") 启用 multilib 并运行： 
    
    $ sudo pacman -Syu
    
要列出所有可用工具，请运行： 
    
    $ sudo pacman -Sgg | grep blackarch | cut -d' ' -f2 | sort -u
    
安装所有的工具： 
    
    $ pacman -S blackarch
    
按照分类批量安装工具： 
    
    $ sudo pacman -S blackarch-<category>
    
列出 blackarch 的所有分类： 
    
    $ sudo pacman -Sg | grep blackarch
    
###  工具使用方法，请下载 blackarch 官方 [PDF](<https://blackarch.org/blackarch-guide-zh.pdf>)
