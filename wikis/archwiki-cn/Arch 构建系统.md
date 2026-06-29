**翻译状态：**

  * 本文（或部分内容）译自 [Arch Build System](<https://wiki.archlinux.org/title/Arch_Build_System> "arch:Arch Build System")，最近一次同步于 2026-01-19，若英文版本有所[更改](<https://wiki.archlinux.org/title/Arch_Build_System?diff=0&oldid=851311>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Arch_Build_System_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Arch 打包准则](<../zh-cn/Arch_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Arch 打包准则")
  * [Arch 用户软件仓库](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "Arch 用户软件仓库")
  * [创建软件包](<../zh-cn/%E5%88%9B%E5%BB%BA%E8%BD%AF%E4%BB%B6%E5%8C%85.html> "创建软件包")
  * [内核/Arch 构建系统](<../zh-cn/%E5%86%85%E6%A0%B8/Arch_%E6%9E%84%E5%BB%BA%E7%B3%BB%E7%BB%9F.html> "内核/Arch 构建系统")
  * [官方仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方仓库")
  * [软件包补丁](<../zh-cn/%E8%BD%AF%E4%BB%B6%E5%8C%85%E8%A1%A5%E4%B8%81.html> "软件包补丁")

Arch 构建系统（[Arch build system](<https://zh.wikipedia.org/wiki/Arch_Linux#Arch_.E7.BC.96.E8.AF.91.E7.B3.BB.E7.BB.9F> "zhwp:Arch Linux")，ABS）是一套从源码构建并打包软件包的系统。在 Arch 中，[pacman](<../zh-cn/Pacman.html> "Pacman") 专门管理二进制软件包（包括那些由 ABS 创建的）；而 ABS 则是一系列工具，负责把源代码编译成可安装的 _.pkg.tar.zst_ 软件包。 

Arch 构建系统类似于 *BSD 上的 [ports](<https://zh.wikipedia.org/wiki/Ports> "zhwp:Ports")，其用于自动化从源码构建软件包的过程。 _Port_ 可以自动下载源代码、解压缩、打补丁、编译和安装软件。一个 _port_ 仅仅是指用户电脑上的一个目录，该目录根据即将安装的软件来命名，它包含一些能指导源码的下载和编译安装的文件。Port 系统让你只需在 port 目录下运行 `make` 或 `make install clean` 就能安装你想要的软件。 

ABS 的概念与 Ports 相似。它由为每个 Arch Linux 可用软件包提供的 git 仓库组成。每个目录中并不包含二进制包或源代码，而是包含一个 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 文件（有时也会有其它文件）。在有 `PKGBUILD` 文件的目录里运行 [makepkg](<../zh-cn/Makepkg.html> "Makepkg") 命令，系统就会在目录中下载软件的源代码、编译并打包在构建文件夹里。然后就可以通过 _pacman_ 进行安装或升级了。 

##  工具链

'ABS' 可以作为一个总括性术语来使用，因为它包含并依赖于若干其他部件。因此，尽管从严格意义上来讲并不精确，ABS可指代包含以下工具的完整工具集： 

Arch 构建系统包含并依赖于数个组件和工具，分别用于从源码到构建出软件包的各个步骤中： 

仓库树
    目录树包含构建所有官方软件包所需的文件，但不包括软件包本身和源代码。这些仓库以 [Git](<../zh-cn/Git.html> "Git") 仓库的形式托管在 [gitlab.archlinux.org](<https://gitlab.archlinux.org/archlinux/packaging/packages>) 上。更多详细信息请参阅[#仓库结构](<#%E4%BB%93%E5%BA%93%E7%BB%93%E6%9E%84>)。

[PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD")
     [Bash](<../zh-cn/Bash.html> "Bash") 脚本，包含软件的源代码的 URL 和编译打包指令。

[makepkg](<../zh-cn/Makepkg.html> "Makepkg")
    一个 shell 命令工具，会读取 PKGBUILD，自动下载源码、编译并创建 _.pkg.tar*_ 包（拓展名由 `makepkg.conf` 中的 `PKGEXT` 指定）。makepkg 也可以用来从 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 或第三方代码构建你自己的自定义软件包，具体细节请参考[创建软件包](<../zh-cn/%E5%88%9B%E5%BB%BA%E8%BD%AF%E4%BB%B6%E5%8C%85.html> "创建软件包")。

[pacman](<../zh-cn/Pacman.html> "Pacman")
    pacman 是完全独立的一个系统，但是它在通过 makepkg 或手动安装或移除软件包、解决依赖关系时都是必需的。

`pkgctl`/[devtools](<https://archlinux.org/packages/?name=devtools>)包
     `devtools` 是用于为 Arch Linux 发行版构建和维护官方仓库软件包的一系列工具。[pkgctl(1)](<https://man.archlinux.org/man/pkgctl.1>) 是一个高层级工具，用于帮助从软件源码仓库构建 Arch Linux 软件包并发布到二进制软件仓库中。

[AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR")
    Arch 用户软件仓库（AUR）的 PKGBUILD 独立于官方仓库，但其中的软件包同样可以使用 ABS 的工具进行打包构建。它包含成千上万的用户贡献的 PKGBUILD，来提供 Arch 官方仓库中没有的软件。如果需要编译官方 Arch 树之外的软件包，AUR 中已经存在的可能性非常大。

**警告：** 官方 PKGBUILD 假定包是[在干净的 chroot 环境中构建](<https://wiki.archlinux.org/title/DeveloperWiki:Building_in_a_clean_chroot>)的。在“脏”的环境中构建可能会失败或者在运行时有意外行为。因为如果编译系统动态检查依赖的话，编译结果会受到当前系统可用包的影响。

###  仓库结构

每个软件包在 [Arch Linux GitLab 服务器](<https://gitlab.archlinux.org/>)的 [archlinux/packaging/packages](<https://gitlab.archlinux.org/archlinux/packaging/packages>) 命名空间下都有其独立的 _源码_ 仓库。每个仓库都包含了官方打包所使用的 PKGBUILD 等文件。另外，这里还存放了开发者在打包过程中所使用的一些文件。 

例如，[acl](<https://archlinux.org/packages/?name=acl>)包 的目录结构是这样的： 
    
    acl
    ├── keys
    │   └── pgp
    │       ├── 259B3792B3D6D319212CC4DCD5BF9FEB0313653A.asc
    │       ├── 600CD204FBCEA418BD2CA74F154343260542DF34.asc
    │       └── B902B5271325F892AC251AD441633B9FE837F581.asc
    ├── PKGBUILD
    └── .SRCINFO
    
源代码并不直接包含在ABS目录中，而是构建时从 `PKGBUILD` 里指定的源代码 URL 下载。 

在构建完官方软件包后，它会被发布到[官方仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方仓库")之一： _core_ ， _extra_ ， _multilib_ 或是先放到测试仓库中。这些仓库存放着 _二进制文件_ ，并不存放在 GitLab 上，而是由[镜像源](<../zh-cn/%E9%95%9C%E5%83%8F%E6%BA%90.html> "镜像源")进行分发。 

##  用例

Arch 构建系统可以将从源码构建出软件包的一些工作自动化，常见用法包括： 

  * 需要编译或重新编译软件包
  * 由开发者和打包人员为 Arch Linux 构建官方二进制软件包
  * 从源代码编译并安装 Arch 官方源里没有的软件（详情请参照[创建软件包](<../zh-cn/%E5%88%9B%E5%BB%BA%E8%BD%AF%E4%BB%B6%E5%8C%85.html> "创建软件包")）
  * 定制现有的软件包以满足你的特定需求（比如开启或禁用相关选项、打补丁）
  * 用你的编译器的 flags 重新构建整个系统，“就像 FreeBSD 那样”
  * 干净地编译安装你自己定制的内核。（参照[内核编译](<../zh-cn/%E5%86%85%E6%A0%B8.html#%E7%BC%96%E8%AF%91> "内核")）
  * 使内核模块（比如某些显卡驱动）在你定制的内核下正常工作
  * 修改 PKGBUILD 中的版本就能方便地编译和安装新的、老的、beta 或者开发版本的 Arch 软件包

##  用法

###  获取 PKGBUILD 源码

要想获取从源代码构建特定软件包所需的 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 文件，可以使用 _pkgctl_ 工具，或者直接使用 [Git](<../zh-cn/Git.html> "Git")。 

####  使用 pkgctl 工具

如需使用 _pkgctl_ ，请先[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [devtools](<https://archlinux.org/packages/?name=devtools>)包。 _pkgctl_ 是一个帮助为 Arch Linux 构建软件包源文件的工具。 

要使用 _pkgctl_ 获取包含软件包 _pkgname_ 最新构建文件的 git 仓库，请使用以下命令： 
    
    $ pkgctl repo clone _pkgname_
    
**提示：** 默认情况下通过 SSH 获取，如果没有在 Arch GitLab 账户中设置 SSH 密钥，则需要通过 HTTPS 获取：`pkgctl repo clone --protocol=https _pkgname_`

请注意，这里所说的构建文件是指 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD")，可能还包括一些其他必要的文件，如密钥。也就是说，是 ABS 所需的基本文件，而不是由包的开发团队编写的源代码文件，例如 C 或 Python 文件。 

该命令不仅会提供当前的构建文件，还会提供它的历史版本。此外，还可以使用其他 [git](<../zh-cn/Git.html> "Git") 命令来签出旧版本或跟踪更改。 

如果想获取特定版本，可以使用以下命令： 
    
    $ pkgctl repo clone --switch="2:1.19.5-1" go
    
如需获取更多详细信息以及其他可用命令，请阅读 [pkgctl-repo-clone(1)](<https://man.archlinux.org/man/pkgctl-repo-clone.1>)

####  直接使用 git

使用以下命令来获取软件包： 
    
    $ git clone https://gitlab.archlinux.org/archlinux/packaging/packages/_pkgname_.git
    
例如获取 Apache 的构建文件： 
    
    $ git clone https://gitlab.archlinux.org/archlinux/packaging/packages/apache.git
    
###  构建软件包

关于如何配置 _makepkg_ 来从 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 构建软件包，请参考 [makepkg#配置](<../zh-cn/Makepkg.html#%E9%85%8D%E7%BD%AE> "Makepkg")。 

然后把 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 所在目录复制到新的位置。在新目录按需要进行修改。 并按照 [makepkg#使用](<../zh-cn/Makepkg.html#%E4%BD%BF%E7%94%A8> "Makepkg")来构建和安装软件包。 

##  技巧

###  保留修改过的软件包

[pacman](<../zh-cn/Pacman.html> "Pacman") 进行升级时会将修改后的软件包升级到仓库中的最新版本，可以通过下面方式避免这个行为： 

在 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 中将软件包加入 `modified` 组： 
    
    PKGBUILD
    
    groups=('modified')

然后将此组加入 `/etc/pacman.conf` 的 `IgnoreGroup`： 
    
    /etc/pacman.conf
    
    IgnoreGroup = modified

当系统升级发现官方仓库中有新版本时，pacman 会显示软件包因为在 _IgnoreGroup_ 中而被忽略的提示，这时需要从 ABS 编译更新的软件包以防止[部分升级](<../zh-cn/%E7%B3%BB%E7%BB%9F%E7%BB%B4%E6%8A%A4.html#%E4%B8%8D%E6%94%AF%E6%8C%81%E9%83%A8%E5%88%86%E5%8D%87%E7%BA%A7> "部分升级")。 
