相关文章

  * [软件包降级](<../zh-cn/%E9%99%8D%E7%BA%A7%E8%BD%AF%E4%BB%B6%E5%8C%85.html> "软件包降级")
  * [Arch Linux 中文社区仓库](<../zh-cn/Arch_Linux_%E4%B8%AD%E6%96%87%E7%A4%BE%E5%8C%BA%E4%BB%93%E5%BA%93.html> "Arch Linux 中文社区仓库")
  * [Arch Linux Archive](<../zh-cn/Arch_Linux_Archive.html> "Arch Linux Archive")

Arch Linux 中文社区仓库历史存档（ _[archlinuxcn] 存档_ 或 _archcn-archive_ ），保存了 Arch Linux 中文社区仓库（即 [archlinuxcn] 仓库）的历史版本。 

**用途**

  * 将某个包降级到某个早期版本（最新版本不能用，我需要之前的版本）
  * 将所有包恢复到某个指定的历史时刻（所有包都不能用，我要恢复到两个月之前的状态），此时需要配合 Arch 官方仓库的历史存档 [Arch Linux Archive](<../zh-cn/Arch_Linux_Archive.html> "Arch Linux Archive")

目前该存档仓库由 [User:Oldherl](<../User:Oldherl.html> "User:Oldherl") 维护，每天 UTC 0点钟抓取一次。由于服务器空间有限，预计未来仅保存近几个月（待定）的包，以及之前每个月1日的包。 

##  位置

Arch Linux 中文社区仓库历史存档目前位于 <https://archcn-archive.oldherl.one> ，有下列几个不同的域名，对应不同的线路，可选择较快的使用。如在欧洲、北美等网络互联较好的地区使用，应选择直连线路。 
    
    [archlinuxcn]
    # 直连线路（加拿大）
    Server = <https://archcn-archive.oldherl.one/repos/yyyy/mm/dd/$arch>
    # Cloudflare CDN 转发
    Server = <https://archcn-archive-cf.oldherl.one/repos/yyyy/mm/dd/$arch>
    # HE 隧道，仅 IPv6
    Server = <https://archcn-archive-he.oldherl.one/repos/yyyy/mm/dd/$arch>
    # Route64 隧道，仅 IPv6
    Server = <https://archcn-archive-r6.oldherl.one/repos/yyyy/mm/dd/$arch>
    
存档库服务器由[这里](<https://github.com/oldherl/pkgarchiver>)的源代码搭建。 

##  目录

**存档库** 分为下列两个主目录： 
    
    ├── packages
    └── repos
    
###  /repos

[repos](<https://archcn-archive.oldherl.one/repos>) 这个目录包含 [archlinuxcn] 仓库镜像的每日快照，按下例结构组织： 
    
    ─ repos
      └── 2026
          └── 04
              ├── 07
              │   ├── aarch64
              │   ├── any
              │   └── x86_64
              ├── 08
              │   ├── aarch64
              │   ├── any
              │   └── x86_64
              └── 09
                  ├── aarch64
                  ├── any
                  └── x86_64
    
###  /packages

[packages](<https://archcn-archive.oldherl.one/packages>) 这个目录包含每个包的所有版本及其相应的数字签名。每个包一个目录，按首字母排序。 
    
    ├── packages
    │   ├── a
    │   │   ├── aria2-git
    │   │   │   ├── aria2-git-1.37.0.r38.gdc89cd3d-1-aarch64.pkg.tar.zst
    │   │   │   ├── aria2-git-1.37.0.r38.gdc89cd3d-1-aarch64.pkg.tar.zst.sig
    │   │   │   ├── aria2-git-1.37.0.r38.gdc89cd3da-1-x86_64.pkg.tar.zst
    │   │   │   └── aria2-git-1.37.0.r38.gdc89cd3da-1-x86_64.pkg.tar.zst.sig
    │   │   │ 
    │   │   ├── autojump
    │   │   └── ...
    │   │   
    │   ├── b
    │   ├── ...
    │   └── z
    
你可以使用“魔法目录”[all](<https://archcn-archive.oldherl.one/packages/all>) 按包名访问所有包。这是一个没有子目录的结构。注意：与 [Arch Linux Archive](<../zh-cn/Arch_Linux_Archive.html> "Arch Linux Archive") 不同（它使用 .all 目录） 
    
    ├── packages
    │   ├── all
    │   │   ├── aria2-git-1.37.0.r38.gdc89cd3d-1-aarch64.pkg.tar.zst
    │   │   └── ...
    
##  使用方法

请参阅 [Arch Linux Archive](<../zh-cn/Arch_Linux_Archive.html> "Arch Linux Archive") 并适当修改其中的URL。注意：[archlinuxcn] 应与 Arch 官方仓库一起降级或升级。 

##  历史

  * 2026-04-09 开始服务，更早的包已经遗失无法收录。
