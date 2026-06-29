相关文章

  * [软件包降级](<../zh-cn/%E9%99%8D%E7%BA%A7%E8%BD%AF%E4%BB%B6%E5%8C%85.html> "软件包降级")

Arch Linux 存档库（**A** rch **L** inux **Archive** ， _简称 ala_ ），以前称为 _Arch Linux 回滚机（Arch Linux Rollback Machine_ ， _简称 ARM_ ），保存了 _官方仓库快照_ 、 _iso 镜像_ 和 _引导（Bootstrap）程序包_ 的历史版本。 

**用途**

  * 将某个包降级到某个早期版本（最新版本不能用，我需要之前的版本）
  * 将所有包恢复到某个指定的历史时刻（所有包都不能用，我要恢复到两个月之前的状态）
  * 查找某个历史版本的 ISO 镜像

软件包仅会保存几年时间，之后会被移动到 [archive.org](<https://en.wikipedia.org/wiki/archive.org> "wikipedia:archive.org") 的 Arch Linux Historical Archive. 

##  位置

Arch Linux 存档库目前位于 <https://archive.archlinux.org/> 和[全球镜像](<https://gitlab.archlinux.org/archlinux/infrastructure/-/blob/master/docs/servers.md#archive-mirrors>). 

[这里](<https://github.com/seblu/archivetools>)的源代码可以帮助您架设自己的存档库服务器。 

##  目录

**存档库** 分为下列三个主目录： 
    
    ├── iso
    ├── packages
    └── repos
    
###  /repos

[repos](<https://archive.archlinux.org/repos>) 这个目录包含官方仓库镜像的每日快照，按下例结构组织： 
    
    repos
    ├── 2013
    │   ├── 08
    │   │   └── 31
    │   │       ├── community
    │   │       ├── community-staging
    │   │       ├── community-testing
    │   │       ├── core
    │   │       ├── extra
    │   │       ├── gnome-unstable
    │   │       ├── kde-unstable
    │   │       ├── lastsync
    │   │       ├── multilib
    │   │       ├── multilib-staging
    │   │       ├── multilib-testing
    │   │       ├── pool
    │   │       ├── staging
    │   │       └── testing
    │   ├── 09
    │   │   ├── 01
    │   │   ├── 02
    │   │   ├── ...
    │   │   ├── 21
    │   │   └── 22
    │   ├── 10
    │   │   ├── 01
    │   │   ├── 02
    │   │   ├── ...
    │   │
    │   ├── 11
    │   └── 12
    ├── 2014
    │   ├── 01
    │   │   ├── 01
    │   │   ├── 02
    │   │   ├── ...
    │   │
    │   ├── 02
    │   ├── 03
    │   ├── ...
    │   └── 09
    │       ├── 01
    │       ├── ...
    │       └── 28
    ├── last
    ├── month
    └── week
    
注意: 最下面的三个特定目录（**last** 、**week** 和 **month** ）分别链接到**已同步的最新仓库版本** 、**本周星期一版本** 和**本月一日版本** 。 

###  /packages

[packages](<https://archive.archlinux.org/packages>) 这个目录包含每个包的所有版本及其相应的数字签名。每个包一个目录，按首字母排序。 
    
    ├── packages
    │   ├── a
    │   │   ├── awesome
    │   │   │   ├── awesome-3.5.0-1-i686.pkg.tar.xz
    │   │   │   ├── awesome-3.5.0-1-i686.pkg.tar.xz.sig
    │   │   │   ├── awesome-3.5.0-1-x86_64.pkg.tar.xz
    │   │   │   ├── awesome-3.5.0-1-x86_64.pkg.tar.xz.sig
    │   │   │   ├── awesome-3.5.1-1-i686.pkg.tar.xz
    │   │   │   ├── awesome-3.5.1-1-i686.pkg.tar.xz.sig
    │   │   │   ├── ...
    │   │   │ 
    │   │   ├── ...
    │   │   ├── awstats
    │   │   └── axel
    │   │   
    │   ├── b
    │   ├── ...
    │   └── z
    
你可以使用“魔法目录”[.all](<https://archive.archlinux.org/packages/.all>) 按包名访问所有包。这是一个没有子目录的结构。 
    
    ├── packages
    │   ├── .all
    │   │   ├── awesome-3.5.1-1-i686.pkg.tar.xz
    │   │   ├── ...
    │   │   ├── zsh-5.0.2-3-i686.pkg.tar.xz
    │   │   ├── zsh-5.0.2-4-i686.pkg.tar.xz
    │   │   └── ...
    
可以下载一个压缩的索引文件，包含完整的软件包列表 [index.0.xz](<https://archive.archlinux.org/packages/.all/index.0.xz>). 
    
    $ curl https://archive.archlinux.org/packages/.all/index.0.xz | unxz
    
    0ad-a14-1-i686
    0ad-a14-1-x86_64
    0ad-a14-2-i686
    ...
    zziplib-0.13.62-1-x86_64
    zziplib-0.13.62-2-i686
    zziplib-0.13.62-2-x86_64

###  /iso

[iso](<https://archive.archlinux.org/iso>) 目录按发布日期，保存官方 ISO 镜像和启动压缩包。 
    
    ├── 2014.09.03
    ├── 2014.10.01
    ├── 2014.11.01
    ├── 2014.12.01
    ├── 2015.07.01
    ├── 2015.08.01
    ├── 2015.09.01
    └── 2015.10.01
        ├── arch
        ├── archlinux-2015.10.01-dual.iso
        ├── archlinux-2015.10.01-dual.iso.sig
        ├── archlinux-2015.10.01-dual.iso.torrent
        ├── archlinux-bootstrap-2015.10.01-i686.tar.gz
        ├── archlinux-bootstrap-2015.10.01-i686.tar.gz.sig
        ├── archlinux-bootstrap-2015.10.01-x86_64.tar.gz
        ├── archlinux-bootstrap-2015.10.01-x86_64.tar.gz.sig
        ├── md5sums.txt
        └── sha1sums.txt
    
**提示：** 从 2022.10.01 开始 Arch Linux Archive 加入了 BT 种子(非磁力链). 所有种子文件可以从[发布页面](<https://archlinux.org/releng/releases/>) 下载。

##  常见问题

###  如何降级某个包

在 [/packages](<#/packages>) 中找到需要的软件包，用 pacman 获取并安装: 
    
    # pacman -U https://archive.archlinux.org/packages/_path/packagename_.pkg.tar.xz
    
pacman 会自动下载 _.sig_ 文件并根据 `/etc/pacman.conf` 设置进行校验。 

或者手动下载并通过 `pacman -U` 安装. 

[软件包降级#自动化](<../zh-cn/%E9%99%8D%E7%BA%A7%E8%BD%AF%E4%BB%B6%E5%8C%85.html#%E8%87%AA%E5%8A%A8%E5%8C%96> "软件包降级")包含了可以简化这个过程的工具。 

###  如何恢复所有包到指定日期

如果想恢复所有包到指定日期（比如2014年3月30日），你必须如下例所示编辑 `/etc/pacman.conf`，从而让 [pacman](<../zh-cn/Pacman.html> "Pacman") 保持在这个时间点并且直接使用指定的服务器： 
    
    /etc/pacman.conf
    
    [core]
    SigLevel = PackageRequired
    Server=https://archive.archlinux.org/repos/2014/03/30/$repo/os/$arch
    
    [extra]
    SigLevel = PackageRequired
    Server=https://archive.archlinux.org/repos/2014/03/30/$repo/os/$arch
    
    [community]
    SigLevel = PackageRequired
    Server=https://archive.archlinux.org/repos/2014/03/30/$repo/os/$arch
    
或者如下例编辑 `/etc/pacman.d/mirrorlist`： 
    
    /etc/pacman.d/mirrorlist
    
    ##                                                                              
    ## Arch Linux repository mirrorlist                                             
    ## Generated on 2042-01-01                                                      
    ##
    Server=https://archive.archlinux.org/repos/2014/03/30/$repo/os/$arch
    
然后同步包数据库以强制降级： 
    
    # pacman -Syyuu
    
如果抱 PGP 签名错误，软件包损坏(corrupted/invalid packages),请先尝试更新 [archlinux-keyring](<https://archlinux.org/packages/?name=archlinux-keyring>)包 和 [ca-certificates](<https://archlinux.org/packages/?name=ca-certificates>)包. Alternatively, you can decide to temporarily [disable signature checking](<../zh-cn/Pacman/Package_signing.html#Disabling_signature_checking> "Pacman/Package signing") altogether. 

**注意：** 混用归档和更新镜像很不安全。万一降级失败，可能使用的是上游软件包，会出现软件包的 epoch 和系统其它软件不一致的现象。

##  历史存档

维护 Arch Linux Archive 需要很多资源，所以需要定期删除老软件包。 

删除前软件包会被上传到 archive.org 上的 ["Arch Linux Historical Archive"](<https://archive.org/details/archlinuxarchive>). 

此仓库并没有提供某个时间的快照，而是提供了 `archive.archlinux.org` 重定向，老软件包会被重定向到 `archive.org`。除了下载速度慢，用户侧使用上差别不大。 

###  从 Historical Archive 查找软件包

**Arch Linux Historical Archive** 包含所有软件包的索引: <https://archive.org/details/archlinuxarchive>

可以通过 **identifier** 获取软件包，格式是 `archlinux_pkg__sanitized_package_name_`. 

要得到一个**规范化** 的软件包名，将软件包名称中的 `@`, `+` 和 `.` 都替换为下划线 `_`. 

例如 [lucene++](<https://archlinux.org/packages/?name=lucene%2B%2B>)包 的软件包名称是 `archlinux_pkg_lucene__`。 

通过如下页面查找软件包： <https://archive.org/details/archlinux_pkg_lucene__>. 

通过 [archive.org Python 客户端](<https://github.com/jjjake/internetarchive>)查找: 
    
    $ ia search subject:"archlinux package" subject:'mysql'
    
    {"identifier": "archlinux_pkg_ejabberd-mod_mysql"}
    {"identifier": "archlinux_pkg_ejabberd-mod_mysql-svn"}
    {"identifier": "archlinux_pkg_gambas3-gb-db-mysql"}
    {"identifier": "archlinux_pkg_gambas3-gb-mysql"}
    {"identifier": "archlinux_pkg_libgda-mysql"}

###  从 Historical Archive 下载软件包

所有软件包的版本可以通过如下下载页面获取: <https://archive.org/download/archlinux_pkg_lucene__>. 

要通过 [pacman](<../zh-cn/Pacman.html> "Pacman") 下载安装: 
    
    # pacman -U https://archive.org/download/archlinux_pkg_cjdns/cjdns-16.1-3-x86_64.pkg.tar.xz
    
pacman 的 `RemoteFileSigLevel` 选项控制校验方式，注意依赖关系需要自己解决。 

通过 [<https://gi>

  * Moved to [archive.archlinux.org](<https://archive.archlinux.org>) on 2015-12-19.[[1]](<https://lists.archlinux.org/archives/list/arch-dev-public@lists.archlinux.org/message/WFG4Z3CIHOYSEGRP6PRD2WGW2YJB3TFN/>)

  * Old packages from 2013-2016 uploaded to [archive.org](<https://archive.org/details/archlinuxarchive>) on 2018-06-05.thub.com/jjjake/internetarchive archive.org Python 客户端]也能进行下载。

下载某个指定版本： 
    
    $ ia download archlinux_pkg_cjdns cjdns-16.1-3-x86_64.pkg.tar.xz{,.sig}
    
下载某个软件包的所有 x86_64 版本： 
    
    $ ia download archlinux_pkg_cjdns --glob="*x86_64.pkg.tar.xz*"
    
##  历史

  * 最早的 ARM （ _Archlinux 回滚机_ ） 已于 2013-08-18 关闭[[2]](<https://bbs.archlinux.org/viewtopic.php?pid=1313360#p1313360>)。
  * [seblu.net 新站点](<https://seblu.net>)已于 2013-08-31 上线。
  * 2015-10-13 旧站关闭，同时启用新 URL 并导入一个新软件 [agetpkg-git](<https://aur.archlinux.org/packages/agetpkg-git/>)AUR 。
  * 2015-12-19 迁移至 [archive.archlinux.org](<https://archive.archlinux.org>)。[[3]](<https://lists.archlinux.org/archives/list/arch-dev-public@lists.archlinux.org/message/WFG4Z3CIHOYSEGRP6PRD2WGW2YJB3TFN/>)
  * 从 2018-06-05 开始 2013-2016 的老软件包上传到了 [archive.org](<https://archive.org/details/archlinuxarchive>) on .
