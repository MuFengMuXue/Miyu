**翻译状态：**

  * 本文（或部分内容）译自 [pacman](<https://wiki.archlinux.org/title/pacman> "arch:pacman")，最近一次同步于 2024-05-22，若英文版本有所[更改](<https://wiki.archlinux.org/title/pacman?diff=0&oldid=808924>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/pacman_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [创建软件包](<../zh-cn/%E5%88%9B%E5%BB%BA%E8%BD%AF%E4%BB%B6%E5%8C%85.html> "创建软件包")
  * [软件包降级](<../zh-cn/%E9%99%8D%E7%BA%A7%E8%BD%AF%E4%BB%B6%E5%8C%85.html> "软件包降级")
  * [pacman/软件包签名](<../zh-cn/Pacman/%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%AD%BE%E5%90%8D.html> "Pacman/软件包签名")
  * [pacman/pacnew 与 pacsave](<../zh-cn/Pacman/pacnew_%E4%B8%8E_pacsave.html> "Pacman/pacnew 与 pacsave")
  * [pacman/Rosetta](<../zh-cn/Pacman/%E5%90%84%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%AE%A1%E7%90%86%E5%99%A8%E5%91%BD%E4%BB%A4%E5%AF%B9%E5%BA%94%E5%85%B3%E7%B3%BB.html> "Pacman/Rosetta")
  * [pacman/提示和技巧](<../zh-cn/Pacman/%E6%8F%90%E7%A4%BA%E5%92%8C%E6%8A%80%E5%B7%A7.html> "Pacman/提示和技巧")
  * [pacman/恢复本地数据库](<../zh-cn/Pacman/%E6%81%A2%E5%A4%8D%E6%9C%AC%E5%9C%B0%E6%95%B0%E6%8D%AE%E5%BA%93.html> "Pacman/恢复本地数据库")
  * [FAQ](<../zh-cn/%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98.html> "FAQ")
  * [系统维护](<../zh-cn/%E7%B3%BB%E7%BB%9F%E7%BB%B4%E6%8A%A4.html> "系统维护")
  * [Arch 构建系统](<../zh-cn/Arch_%E6%9E%84%E5%BB%BA%E7%B3%BB%E7%BB%9F.html> "Arch 构建系统")
  * [官方仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方仓库")
  * [Arch 用户仓库](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E4%BB%93%E5%BA%93.html> "Arch 用户仓库")

[Pacman](<https://pacman.archlinux.page/>)[软件包管理器](<https://en.wikipedia.org/wiki/Package_management_system> "wikipedia:Package management system")是 Arch Linux 发行版的一大亮点。它将一个简单的二进制包格式和易用的[构建系统](<../zh-cn/Arch_Build_System.html> "Arch Build System")结合了起来。 _Pacman_ 的目标是简化对软件包的管理，无论软件包是来自[官方软件仓库](<../zh-cn/Official_repositories.html> "Official repositories")还是用户自己创建的软件包。 

Pacman 通过和主服务器同步软件包列表来保持系统是最新的。这种服务器/客户端模式可使得用户使用简单的命令，就能下载或安装软件包，并包含其所有必需的依赖包。 

Pacman 用 [C 语言](<../zh-cn/C.html> "C")编写，并使用 [bsdtar(1)](<https://man.archlinux.org/man/bsdtar.1>) [tar](<https://en.wikipedia.org/wiki/tar_\(computing\)> "w:tar \(computing\)") 作为打包格式。 

**提示：**[pacman](<https://archlinux.org/packages/?name=pacman>)包 软件包提供了如 [makepkg](<../zh-cn/Makepkg.html> "Makepkg") 和 [vercmp(8)](<https://man.archlinux.org/man/vercmp.8>) 等工具。其它有用的工具如 [pactree](<#Pactree>)、[checkupdates](<../zh-cn/System_maintenance.html#%E4%B8%8D%E6%94%AF%E6%8C%81%E9%83%A8%E5%88%86%E5%8D%87%E7%BA%A7> "System maintenance") 等则在 [pacman-contrib](<https://archlinux.org/packages/?name=pacman-contrib>)包 软件包中（它[曾是](<https://gitlab.archlinux.org/pacman/pacman/commit/0c99eabd50752310f42ec808c8734a338122ec86>) _pacman_ 的一部分）。运行 `pacman -Ql pacman | grep -E 'bin/.+'` 可查看完整的工具列表。

##  用法

以下只是 _pacman_ 可以执行的操作的一小部分示例。要阅览更多示例可参考 [pacman(8)](<https://man.archlinux.org/man/pacman.8>)。 

**提示：** 对于以前使用过其他 Linux 发行版的用户，[Pacman Rosetta](<../zh-cn/Pacman_Rosetta.html> "Pacman Rosetta") 这篇对比文章将大有帮助。

###  安装软件包

一个软件包就是一个归档包，其中包含： 

  * 该软件所有（编译好的）文件，并按照每个文件的安装位置储存在一个与根目录结构相同的目录中
  * 该软件的元数据，例如软件名称、版本和依赖等
  * 供 pacman 使用的其它描述性文件
  * （可选）在安装、升级、卸载时执行的安装脚本

Arch 的软件包管理器 _pacman_ 可以安装、更新和删除这些软件包。使用软件包而不是自己编译和安装程序有很多好处： 

  * 轻松升级： _pacman_ 会在更新可用时立即更新已安装的软件包
  * 依赖检查： _pacman_ 会为你处理依赖问题，只需要指明程序（名）， _pacman_ 就会将它和它所需的所有其他程序都一起安装。
  * 干净卸载： _pacman_ 持有软件包包含的所有文件的列表。这样一来，当你决定移除软件包时，不会无意留下任何文件。

**注意：**

  * 软件包通常有[可选依赖](<../zh-cn/PKGBUILD.html#optdepends> "PKGBUILD")，它们为软件提供额外的功能，但并不是软件运行所必需的。安装软件时, _pacman_ 会列出软件包的可选依赖, 但这份列表不会记载在 `pacman.log` 中。请使用[#查询包数据库](<#%E6%9F%A5%E8%AF%A2%E5%8C%85%E6%95%B0%E6%8D%AE%E5%BA%93>)命令查询软件包的可选依赖。
  * 当你安装软件包以作为一些其他的软件包的（可选）依赖时（即没有明确要求安装时），推荐使用 `--asdeps` 选项。请参阅[#安装原因](<#%E5%AE%89%E8%A3%85%E5%8E%9F%E5%9B%A0>)一节了解详细内容。

**警告：** 在 Arch 上安装软件包时，请避免在还没有[更新系统](<#%E5%8D%87%E7%BA%A7%E8%BD%AF%E4%BB%B6%E5%8C%85>)前刷新同步软件包列表（例如，当官方软件仓库[不再提供某个软件包](<#%E5%AE%89%E8%A3%85%E6%97%B6%E6%97%A0%E6%B3%95%E8%8E%B7%E5%8F%96%E8%BD%AF%E4%BB%B6%E5%8C%85>)时）。实际操作上，请使用 `pacman -Sy**u** _软件包名_`, 而**不要** 使用 `pacman -Sy _软件包名_`，因为后者可能会导致依赖问题。参见 [系统维护#不支持部分升级](<../zh-cn/%E7%B3%BB%E7%BB%9F%E7%BB%B4%E6%8A%A4.html#%E4%B8%8D%E6%94%AF%E6%8C%81%E9%83%A8%E5%88%86%E5%8D%87%E7%BA%A7> "系统维护")一文和 [BBS#89328 论坛讨论](<https://bbs.archlinux.org/viewtopic.php?id=89328>)。

####  安装指定的包

要安装单个或者一系列软件包（包含软件包的依赖），请使用如下命令： 
    
    # pacman -S _包名_1_ _包名_2_ ...
    
要通过正则表达式安装一系列软件包（参见[这个论坛帖子](<https://bbs.archlinux.org/viewtopic.php?id=7179>)）： 
    
    # pacman -S $(pacman -Ssq _包正则表达式_)
    
有时软件包有多个版本，放在不同的仓库内（例如 _extra_ 和 _testing_ ）。在以下示例中，要安装 _extra_ 仓库的版本，需要在包名称前定义仓库名： 
    
    # pacman -S extra/_包名_
    
要安装多个含有相似名称的软件包，可以使用花括号扩展。例如： 
    
    # pacman -S plasma-{desktop,mediacenter,nm}
    
可以多层扩展到需要的层次： 
    
    # pacman -S plasma-{workspace{,-wallpapers},pa}
    
#####  虚包

虚拟软件包是一个特殊的软件包，它本身并不存在，但由一或多个其它软件包提供。虚拟软件包允许其它软件包不以某一个特定的包为依赖，以应对有多个候选的情况。虚包不能用它们的名称安装，相反它们会在你安装 _提供_ 虚包的软件包时被安装到你的系统中。一个例子是[dbus-units](<../zh-cn/D-Bus.html#%E6%9B%BF%E4%BB%A3%E5%AE%9E%E7%8E%B0> "D-Bus")软件包。 

**提示：** 当存在多个候选的情况下，可选包列表先按照`pacman.conf`中仓库出现的顺序排序，同一个仓库有多个可选再按字母顺序排序。

####  安装包组

一些包属于一个可以同时安装的[软件包组](<../zh-cn/Meta_package_and_package_group.html> "Meta package and package group")。例如，运行下面的命令 
    
    $ pacman -S gnome
    
会提醒用户选择 `gnome` 内需要安装的包。 

有的包组包含大量的软件包，有时用户只需其中几个。除了逐一键入序号外，pacman 还支持选择或排除某个区间内的的软件包： 
    
    Enter a selection (default=all): 1-10 15
    
这将选中序号 1 至 10 和 15 的软件包。而 
    
    Enter a selection (default=all): ^5-8 ^2
    
将会选中除了序号 5 至 8 和 2 之外的所有软件包。 

想要查看哪些包属于 gnome 组，运行： 
    
    # pacman -Sg gnome
    
也可以访问 <https://archlinux.org/groups/> 查看可用的包组。 

**注意：** 如果列表中的包已经安装在系统中，它会被重新安装，即使它已经是最新的。可以用 `--needed` 选项覆盖这种行为。

###  删除软件包

删除单个软件包，保留其全部已经安装的依赖关系 
    
    # pacman -R _package_name_
    
删除指定软件包，及其所有没有被其他已安装软件包使用的依赖关系： 
    
    # pacman -Rs _package_name_
    
**警告：** 删除类似 _gnome_ 这样的软件包组时，将会忽略组中软件包的安装原因，因为实际操作上执行的是逐一删除软件组的每一个软件，依赖软件包的安装原因不会被忽略。

上面这条命令在移除包含其他所需包的组时有时候会拒绝运行。这种情况下可以尝试 
    
    # pacman -Rsu _package_name_
    
要删除软件包和所有依赖这个软件包的程序: 

**警告：** 此操作是递归的，请小心检查，可能会一次删除大量的软件包。
    
    # pacman -Rsc _package_name_
    
要删除一个被其他软件包依赖的软件包，但是不删除依赖这个软件包的其他软件包： 

**警告：** 此操作有破坏系统的能力，应该尽量避免使用。详情请看 [避免某些 Pacman 命令](<../zh-cn/System_maintenance.html#Avoid_certain_pacman_commands> "System maintenance")。
    
    # pacman -Rdd _package_name_
    
_pacman_ 删除某些程序时会备份重要配置文件，在其后面加上*.pacsave扩展名。-n 选项可以避免备份这些文件： 
    
    pacman -Rn _package_name_
    
**注意：** _pacman_ 不会删除软件自己创建的文件（例如主目录中的“[点文件](<../zh-cn/Dotfiles.html> "点文件")”不会被删除。）

###  升级软件包

**警告：**

  * 建议用户遵守[系统维护#更新系统](<../zh-cn/%E7%B3%BB%E7%BB%9F%E7%BB%B4%E6%8A%A4.html#%E6%9B%B4%E6%96%B0%E7%B3%BB%E7%BB%9F> "系统维护")的指导，定期更新系统，并不盲目地执行这些命令。
  * Arch 只支持系统完整升级，详细参见[系统维护#不支持部分升级](<../zh-cn/%E7%B3%BB%E7%BB%9F%E7%BB%B4%E6%8A%A4.html#%E4%B8%8D%E6%94%AF%E6%8C%81%E9%83%A8%E5%88%86%E5%8D%87%E7%BA%A7> "系统维护")和[#安装软件包](<#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85>)。

一个 _pacman_ 命令就可以升级整个系统。花费的时间取决于系统有多老。这个命令会同步非本地(local)软件仓库并升级系统的软件包： 
    
    # pacman -Syu
    
###  查询包数据库

_pacman_ 使用 `-Q` 参数查询本地软件包数据库， `-S` 查询同步数据库，以及 `-F`查询文件数据库。要了解每个参数的子选项，分别参见 `pacman -Q --help`，`pacman -S --help`和`pacman -F --help`。 

_pacman_ 可以在包数据库中查询软件包，查询位置包含了软件包的名字和描述： 
    
    $ pacman -Ss _string1_ _string2_ ...
    
有时，`-s`的内置正则会匹配很多不需要的结果，所以应当指定仅搜索包名，而非描述或其他子段: 
    
    $ pacman -Ss '^vim-'
    
要查询已安装的软件包： 
    
    $ pacman -Qs _string1_ _string2_ ...
    
按文件名查找软件库： 
    
    $ pacman -F _string1_ _string2_ ...
    
显示软件包的详尽的信息： 
    
    $ pacman -Si _package_name_
    
查询本地安装包的详细信息： 
    
    $ pacman -Qi _package_name_
    
使用两个 `-i` 将同时显示备份文件和修改状态： 
    
    $ pacman -Qii _package_name_
    
获取已安装软件包所包含文件路径（比如用来查看软件包提供了什么可执行文件）： 
    
    $ pacman -Ql _package_name_
    
查询远程库中软件包包含的文件： 
    
    $ pacman -Fl _package_name_
    
检查软件包安装的文件是否都存在： 
    
    $ pacman -Qk _package_name_
    
两个参数`k`将会执行一次更彻底的检查。 

查询数据库获取某个文件属于哪个软件包： 
    
    $ pacman -Qo _/path/to/file_name_
    
查询文件属于远程数据库中的哪个软件包： 
    
    $ pacman -F _/path/to/file_name_
    
要罗列所有不再作为依赖的软件包(孤立orphans)： 
    
    $ pacman -Qdt
    
要罗列所有明确安装而且不被其它包依赖的软件包： 
    
    $ pacman -Qet
    
更多例子查看[pacman tips](<../zh-cn/Pacman_tips.html> "Pacman tips")。 

#### Pactree

**注意：**[pactree(8)](<https://man.archlinux.org/man/pactree.8>) 不再是 [pacman](<https://archlinux.org/packages/?name=pacman>)包 的一部分。它现在在 [pacman-contrib](<https://archlinux.org/packages/?name=pacman-contrib>)包 中。

要显示软件包的依赖树： 
    
    $ pactree _package_name_
    
要检查一个 _已安装_ 的软件包被哪些包依赖，可以将递归标识 `-r` 传递给 _pactree_ ，或者使用 [pkgtools](<https://aur.archlinux.org/packages/pkgtools/>)AUR 中的 _whoneeds_

####  数据库结构

pacman 数据库通常位于 `/var/lib/pacman/sync`。对于每一个在 `/etc/pacman.conf` 中指定的软件仓库， 这里都有一个一致的数据库。数据库文件夹里每个 tar.gz 文件都包含着一个仓库的软件包信息。例如 [which](<https://archlinux.org/packages/?name=which>)包 包: 
    
    $ tree which-2.21-5
    
    which-2.21-5
    |-- desc
    
这个 `depends` 项列出了该软件的依赖包， 而 `desc` 有该包的介绍，例如文件大小和MD5值 。 

###  清理软件包缓存

_pacman_ 将下载的软件包保存在 `/var/cache/pacman/pkg/` 并且不会自动移除旧的和未安装版本的软件包。这样做有一些好处： 

  1. 这样允许[降级](<../zh-cn/Downgrading_packages.html> "Downgrading packages")软件包而不需要通过其他方式提取旧版本，例如 [Arch Linux Archive](<../zh-cn/Arch_Linux_Archive.html> "Arch Linux Archive").
  2. 被卸载的软件包可以轻易地直接从缓存文件夹重新安装，不需要重新从软件仓库下载。

然而，需要定期手动清理缓存来避免该文件夹无限制增大。 

[pacman-contrib](<https://archlinux.org/packages/?name=pacman-contrib>)包 提供的 [paccache(8)](<https://man.archlinux.org/man/paccache.8>) 脚本默认会删除所有缓存的版本和已卸载的软件包，除了最近的3个会被保留： 
    
    # paccache -r
    
[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable")和[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") `paccache.timer`来每周删除不使用的包。 

**提示：** 可以使用[#钩子](<#%E9%92%A9%E5%AD%90>)自动执行清理，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [paccache-hook](<https://aur.archlinux.org/packages/paccache-hook/>)AUR 并参考[[1]](<https://bbs.archlinux.org/viewtopic.php?pid=1694743#p1694743>)。

也可以自己设置保留最近几个版本： 
    
    # paccache -rk1
    
添加`-u`/`--uninstalled`开关来限制 _paccache_ 的行为只作用于卸载的包。例如清理所有卸载的包的缓存版本，可以用以下命令: 
    
    # paccache -ruk0
    
更多参数参见`paccache -h`。 

_pacman_ 也有一些内建参数用于清除缓存和那些不再在`/etc/pacman.conf`配置文件中列出的软件仓库残留数据库文件。然而 _pacman_ 并不提供保留一定数量的过去版本的功能，因此它比 _paccache_ 的默认选项更加激进。 

要删除目前没有安装的所有缓存的包，和没有被使用的同步数据库，执行： 
    
    # pacman -Sc
    
要删除缓存中的全部文件，使用两次`-c`开关。这是最为激进的方式，将会清空缓存文件夹： 
    
    # pacman -Scc
    
**警告：** 应当避免从缓存中删除所有过去版本和卸载的包，除非需要更多磁盘空间。这样会导致无法降级或重新安装软件包时需要再次下载。

[pkgcacheclean](<https://aur.archlinux.org/packages/pkgcacheclean/>)AUR以及[pacleaner](<https://aur.archlinux.org/packages/pacleaner/>)AUR是两个进一步清理缓存的替代工具 

###  其它命令

升级系统时安装其他软件包： 
    
    # pacman -Syu _package_name1_ _package_name2_ ...
    
下载包而不安装它： 
    
    # pacman -Sw package_name
    
安装一个**本地** 包(不从源里下载）： 
    
    # pacman -U _/path/to/package/package_name-version.pkg.tar.zst_
    
要将本地包保存至缓存，可执行： 
    
    # pacman -U file:///_path/to/package/package_name-version.pkg.tar.zst_
    
安装一个**远程** 包（不在 _pacman_ 配置的源里面）： 
    
    # pacman -U _http://www.example.com/repo/example.pkg.tar.zst_
    
####  查看软件变动

_pacman_ 会列出需要安装和删除的软件，并在执行动作前要求需要的权限。 

要抑制`-S`，`-U` 和 `-R`，的动作并列出涉及该动作相关软件的列表，可以使用`--print`或缩写`-p`。 

可以添加`--print-format` 参数将输出格式化，例如使用`--print-format %n`将返回不带有版本号的列表。 

###  安装原因

_pacman_ 数据库将软件包按照安装的原因分为两类： 

  * **显式安装** ：那些真正地被传递给通用 _pacman_`-S`和`-U`命令的包；
  * **依赖** ：那些虽然（一般）从未被传递给 _pacman_ 安装命令，但由于被其它显式安装的包[需要](</wzh/index.php?title=Dependency&action=edit&redlink=1> "Dependency（页面不存在）")从而被隐式安装的包

当安装软件包时，可以把安装原因强制设为**依赖** : 
    
    # pacman -S --asdeps _package_name_
    
该命令使用的原因通常是显式安装的包可能会提供[可选安装包](<../zh-cn/PKGBUILD.html#optdepends> "PKGBUILD")，这些包提供了非必须功能，可供用户自由选择。 

**提示：** 用`--asdeps`安装可选依赖将确保如果你[移除孤立包](<../zh-cn/Pacman/%E6%8F%90%E7%A4%BA%E5%92%8C%E6%8A%80%E5%B7%A7.html#%E5%88%A0%E9%99%A4%E6%9C%AA%E4%BD%BF%E7%94%A8%E7%9A%84%E8%BD%AF%E4%BB%B6%E5%8C%85%EF%BC%88%E5%AD%A4%E7%AB%8B%E8%BD%AF%E4%BB%B6%E5%8C%85%EF%BC%89> "Pacman/提示和技巧")， _pacman_ 将会一同移除按照上述方法指定安装的可选依赖。

但是重新安装该软件包，当前安装原因默认会被保留。 

显式安装的软件包列表可用`pacman -Qe`获取, 设置为依赖的软件包可用`pacman -Qd`获取。 

改变某个已安装软件包的安装原因，可以执行： 
    
    # pacman -D --asdeps _package_name_
    
反过来的对应参数`--asexplicit`

**注意：** 在升级时使用`--asdeps`和`--asexplicit`选项，例如`pacman -Syu _package_name_ --asdeps`，是不被推荐的。这会导致不仅改变要被安装的软件包的安装原因，也会改变被升级的软件包的安装原因。

###  查询一个包含具体文件的包名

同步文件数据库: 
    
    # pacman -Fy
    
查询包含某个文件的包名，比如: 
    
    # pacman -F pacman
    core/pacman 5.0.1-4
        usr/bin/pacman
        usr/share/bash-completion/completions/pacman
    extra/xscreensaver 5.36-1
        usr/lib/xscreensaver/pacman
    
**提示：** 可以[启用/启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Help:阅读") `pacman-filesdb-refresh.timer`（该定时器在[pacman-contrib](<https://archlinux.org/packages/?name=pacman-contrib>)包中）来每周同步文件信息数据库。

如果需要高级功能请安装 [pkgfile](<../zh-cn/Pkgfile.html> "Pkgfile")，它使用一个单独的数据库来保存文件和它们所关联的软件包的信息。 

###  安装/更新/删除 软件包时发生了什么

动作成功执行时，事务包含五大步骤和事务钩子程序: 

  1. 如果数据库未被锁定，初始化事务
  2. 确认事务中要添加或删除的软件包
  3. 准备事务，根据参数，对同步数据库、软件包和依赖关系进行校验
  4. 提交事务: 
     1. 如果需要，下载软件包 (`_alpm_sync_load`)
     2. 如果有可以执行的 _pacman_ `PreTransaction` 钩子，执行这些钩子.
     3. 被替换、出现冲突或被指定删除的软件包将会被删除
     4. 如果需要添加软件包，每个软件包都会执行提交 
        1. 如果有安装脚本，执行 `pre_install` 函数(更新时执行 `pre_upgrade`，删除时执行 `pre_remove`).
        2. _pacman_ 删除软件包之前版本的所有文件 (在更新或删除软件包时)。配置文件将会被保留 (请参阅 [Pacman/Pacnew and Pacsave](<../zh-cn/Pacman/Pacnew_and_Pacsave.html> "Pacman/Pacnew and Pacsave")).
        3. _pacman_ 将软件包文件解压到系统(安装或升级软件包时). 会覆盖旧的已被手动修改的配置文件时，配置文件会命名为 (.pacnew).
        4. 如果软件包有安装脚本，执行 `post_install` 函数(更新时执行 `post_upgrade`，删除时执行 `post_remove`).
     5. 如果 _pacman_ `PostTransaction` 钩子可执行，执行这些钩子.
  5. 释放事务及事务资源 (例如，数据库锁)

##  配置

_pacman_ 的配置文件位于`/etc/pacman.conf`。 [man pacman.conf](<https://archlinux.org/pacman/pacman.conf.5.html>) 可以查看配置文件的进一步信息。 

###  通用选项

通用选项都在`[options]`段。阅读 man 手册或者查看默认的 pacman.conf 可以获得有关信息和用法。 

###  升级前对比版本

要查看旧版和新版的有效安装包，请取消`/etc/pacman.conf`中"VerbosePkgLists"的注释。修改后的`pacman -Syu`输出如下： 
    
    Package (6)             Old Version  New Version  Net Change  Download Size
    
    extra/libmariadbclient  10.1.9-4     10.1.10-1      0.03 MiB       4.35 MiB
    extra/libpng            1.6.19-1     1.6.20-1       0.00 MiB       0.23 MiB
    extra/mariadb           10.1.9-4     10.1.10-1      0.26 MiB      13.80 MiB
    
####  启用并行下载

Pacman 6.0 增加了并行下载选项，将 `/etc/pacman.conf` 中 `[options]` 选项 `ParallelDownloads` 设置成正整数，例如 `5`，将会同时下载 5 个软件包，如果未设置此选项，软件包将会被依次下载。 

####  在升级时跳过软件包

**警告：** 在跳过软件包时要小心，因为[部分升级不受支持](<../zh-cn/System_maintenance.html#%E4%B8%8D%E6%94%AF%E6%8C%81%E9%83%A8%E5%88%86%E5%8D%87%E7%BA%A7> "System maintenance")

要想在[升级](<#%E5%8D%87%E7%BA%A7%E8%BD%AF%E4%BB%B6%E5%8C%85>)系统时跳过特定的软件包，用像如下的命令指明： 
    
    IgnorePkg=linux
    
多软件包可以用空格隔开，或者用另外的`IgnorePkg`行。也可使用 [glob](<https://en.wikipedia.org/wiki/glob_\(programming\)> "wikipedia:glob \(programming\)") 模式。如果只打算忽略一次升级，可以使用 `--ignore` 选项，这时使用逗号隔开的列表。 

忽略了的软件包依然可通过 `pacman -S` 升级。这种情况下 _pacman_ 会提醒你这些软件包已经被包含在`IgnorePkg`声明中。 

####  在升级时跳过软件包组

**警告：** 在跳过软件包时要小心，因为[部分升级不受支持](<../zh-cn/System_maintenance.html#%E4%B8%8D%E6%94%AF%E6%8C%81%E9%83%A8%E5%88%86%E5%8D%87%E7%BA%A7> "System maintenance")

和软件包一样，也可以不升级某个软件包组： 
    
    IgnoreGroup = gnome
    
####  在升级时跳过文件

所有在`NoUpgrade`指令中列出的文件都会在软件包被安装/升级时不会被更改，并且新文件会以带有 _.pacnew_ 后缀名的形式安装 
    
    NoUpgrade=_path/to/file_
    
    存在多个跳过文件也可以像这样指定：
    
    NoUpgrade=_path/to/file1 path/to/file2_
    
**注意：** 这个路径指软件包中的文件，所以不要包括开头的斜线。

####  在安装时跳过文件

要总是跳过某些文件夹的安装，可以将它们放到 `NoExtract` 中，例如不想安装 [systemd](<../zh-cn/Systemd.html> "Systemd") 模块： 
    
    NoExtract=usr/lib/systemd/system/*
    
后面的规则覆盖前面的规则，加上 `!` 可以取消跳过效果。 

**提示：** _pacman_ 会在更新locales已经被 _localepurge_ 或者 _bleachbit_ 清除的包时发出警告。注释掉`pacman.conf`中的`CheckSpace`参数能够抑制这种警告，但是要注意space-check功能将会对所有软件包禁用。

###  保留多个配置文件

如果你有多个配置文件（比如，主配置和启用了[测试仓库](<../zh-cn/Official_repositories.html#testing_%E4%BB%93%E5%BA%93> "Official repositories")的配置文件），需要共享一些设置，你可以在配置文件中使用`Include`选项，例如： 
    
    Include = _/path/to/common/settings_
    
`_/path/to/common/settings_`文件中是两个配置文件共享的相同配置。 

###  钩子

_pacman_ 可以在处理前后，运行`/usr/share/libalpm/hooks/`文件夹下的hooks，更多的hooks文件夹可以通过`HookDir`选项在`pacman.conf`中指明，默认`/etc/pacman.d/hooks`。Hook文件必须以 _.hook_ 为后缀。Pacman hooks不是交互式的。 

_pacman_ hooks用于，比如说，和`systemd-sysusers`和`systemd-tmpfiles`结合来在安装包时自动创建系统用户和文件。例如，[tomcat8](<https://archlinux.org/packages/?name=tomcat8>)包指明它想要创建一个叫做`tomcat8`的系统用户和一些属于该用户的文件。当 _pacman_ 确定[tomcat8](<https://archlinux.org/packages/?name=tomcat8>)包包含文件指明用户和临时文件时， _pacman_ hooks `systemd-sysusers.hook`和`systemd-tmpfiles.hook`唤起`systemd-sysusers`和`systemd-tmpfiles`。 

有关 alpm hooks 的更多信息，参见[alpm-hooks(5)](<https://man.archlinux.org/man/alpm-hooks.5>)。 

###  软件仓库

除了特殊的[通用选项](<#%E9%80%9A%E7%94%A8%E9%80%89%E9%A1%B9>)节, 每个`pacman.conf`中的`[section]`都定义了一个使用的软件包仓库， _仓库_ 是多个软件包的 _逻辑_ 上的集合，他们 _物理_ 上存储在一个或多个服务器：这也是为什么每一个服务器都叫做这个仓库的 _镜像_ 。 

仓库区分为[官方仓库](<../zh-cn/Official_repositories.html> "Official repositories")与[非官方仓库](<../zh-cn/Unofficial_user_repositories.html> "Unofficial user repositories")。配置文件中仓库的顺序十分重要；当几个仓库出现同名安装包，不管版本号如何， _pacman_ 将使用配置文件中排前的仓库。要在添加后使用某个仓库，你需要先[升级](<#%E5%8D%87%E7%BA%A7%E8%BD%AF%E4%BB%B6%E5%8C%85>)整个系统 

每个仓库节都可以直接指定镜像列表或者`Include`引用其他的文件：例如，官方镜像引用了`/etc/pacman.d/mirrorlist/`。具体查看[Mirrors](<../zh-cn/%E9%95%9C%E5%83%8F%E6%BA%90.html> "Mirrors")。 

###  软件包的缓存目录

在`pacman.conf`[通用选项](<#%E9%80%9A%E7%94%A8%E9%80%89%E9%A1%B9>)节，`CacheDir`指定了Pacman下载的安装包缓存位置(如果未设置，默认位置为 `/var/cache/pacman/pkg/`)。 

即使只保留最新版本的安装包，缓存目录大小仍然有可能随着时间增长。 

如果要将缓存目录移动到更方便的地方，只需要完成下列方法中的任意一个： 

  * 在`pacman.conf`[通用选项](<#%E9%80%9A%E7%94%A8%E9%80%89%E9%A1%B9>)节，设置`CacheDir`为要使用的缓存目录，并确保目录以"/"结尾。**推荐使用该方法**.
  * 将一个专用分区挂载到默认缓存点`/var/cache/pacman/pkg/`，例如使用[Btrfs 子卷](<../zh-cn/Btrfs.html#%E5%AD%90%E5%8D%B7> "Btrfs")。
  * 将一个目录与 `/var/cache/pacman/pkg/`绑定挂载。

**警告：****不要使用符号链接** 将 `/var/cache/pacman/pkg/` 目录指向其它位置。 **这会导致pacman出现异常** ，特别是当pacman尝试升级自己时。

###  软件包的安全性

_pacman_ 支持软件包签名，会为软件包提供额外的安全性。默认配置，`SigLevel = Required DatabaseOptional` 将启用全局签名验证，但会被每个软件仓库的 `SigLevel` 行所覆盖。有关软件包签名和签名验证的更多细节，参见 [pacman-key](<../zh-cn/Pacman/%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%AD%BE%E5%90%8D.html> "Pacman/软件包签名")。 

##  疑难解答

###  "Failed to commit transaction (conflicting files)" 错误

如果碰到如下错误：[[2]](<https://bbs.archlinux.org/viewtopic.php?id=56373>)
    
    error: could not prepare transaction
    error: failed to commit transaction (conflicting files)
    package: _/path/to/file_ exists in filesystem
    Errors occurred, no packages were upgraded.
    
这是因为 _pacman_ 检测到文件冲突，而且按照设计， _pacman_ 不会覆盖文件。这是设计功能，不是缺陷。 

这个问题通常很容易解决（当然你首先应该尝试搞清楚这些文件是怎么变成这样的）。一个安全的方式是，首先检查是否有另一个软件包提供了这个文件 (`pacman -Qo _/path/to/file_`)。如果文件被另一个软件包所有，请[报告问题](<../zh-cn/%E6%BC%8F%E6%B4%9E%E6%8A%A5%E5%91%8A%E5%87%86%E5%88%99.html> "漏洞报告准则")。如果不是其它软件包提供，将 'exists in filesystem' 的文件重命名并重新运行update命令。如果一切顺利，可以删掉这个文件。 

如果你手动安装了一个软件，没有通过 _pacman_ ，例如用`make install`，你必须将软件连同它的全部文件一起移除/卸载。参见[Pacman/提示和技巧#查找不属于任何软件包的文件](<../zh-cn/Pacman/%E6%8F%90%E7%A4%BA%E5%92%8C%E6%8A%80%E5%B7%A7.html#%E6%9F%A5%E6%89%BE%E4%B8%8D%E5%B1%9E%E4%BA%8E%E4%BB%BB%E4%BD%95%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%9A%84%E6%96%87%E4%BB%B6> "Pacman/提示和技巧")。 

每一个安装的软件包都会提供一个 `/var/lib/pacman/local/_$package-$version_ /files` 文件，包含此软件包的元数据。如果文件损坏或者丢失，将会导致升级时出现`file exists in filesystem` 错误。此错误通常只会影响一个软件包，除了手动删除或移动所有的问题文件，你也可以显式地使用`pacman -S --overwrite _glob package_`让 _pacman_ 强制覆盖匹配` _glob_`的文件。 

**警告：** 尽量避免使用`--overwrite`开关。参见[System maintenance#避免某些 pacman 命令](<../zh-cn/System_maintenance.html#%E9%81%BF%E5%85%8D%E6%9F%90%E4%BA%9B_pacman_%E5%91%BD%E4%BB%A4> "System maintenance")

###  "Failed to commit transaction (invalid or corrupted package)" 错误

看看`/var/cache/pacman/pkg`中是否有`*.part`结尾的文件，它们是没有完全下载的文件，删除它们并重新执行更新。这些程序一般是自定义的`XferCommand` 下载命令造成的。 
    
    # find /var/cache/pacman/pkg/ -iname "*.part" -delete
    
同样的错误也可能是因为 _archlinux-keyring_ 过期所致，阻止了 _pacman_ 验证签名。详情见[Pacman/Package signing#Upgrade system regularly](<../zh-cn/Pacman/Package_signing.html#Upgrade_system_regularly> "Pacman/Package signing")以修复并避免在未来遇到同样问题。 

###  "Failed to init transaction (unable to lock database)" 错误

_pacman_ 在改变软件包数据库前，比如安装软件包时，会创建一个文件锁 `/var/lib/pacman/db.lck`。这会阻止其他 _pacman_ 实例在同一时间修改软件包数据库。 

如果 _pacman_ 在更新数据库时被打断，旧锁可能保留下来。如果确认没有 _pacman_ 实例在运行，那么删掉文件锁： 
    
    # rm /var/lib/pacman/db.lck
    
**提示：** 以root身份运行`fuser /var/lib/pacman/db.lck`可以确认是否有其它进程仍在使用它。

###  安装时无法获取软件包

错误内容包含：`Not found in sync db`, `Target not found` 或 `Failed retrieving file`. 

首先确认软件包确实存在（并注意错别字）。如果确认软件包存在，可能本地数据库过时了或者软件仓库没有配置好，试试 `pacman -Syyu` 强制数据库更新和升级。 

也有可能包含该软件包的软件仓库没有启动。例如，该软件包可能在 _multilib_ 仓库里，但该仓库没有在 _pacman.conf_ 中启用。 

参阅[常见问题#Q) 在官方仓库中，为什么只为每个共享链接库提供一个版本？](<../zh-cn/%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98.html#Q\)_%E5%9C%A8%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93%E4%B8%AD%EF%BC%8C%E4%B8%BA%E4%BB%80%E4%B9%88%E5%8F%AA%E4%B8%BA%E6%AF%8F%E4%B8%AA%E5%85%B1%E4%BA%AB%E9%93%BE%E6%8E%A5%E5%BA%93%E6%8F%90%E4%BE%9B%E4%B8%80%E4%B8%AA%E7%89%88%E6%9C%AC%EF%BC%9F> "常见问题"). 

###  pacman 更新时崩溃

如果 _pacman_ 在删除、重新安装或更新软件包时 "数据库写入" 出错： 

  1. 从 Arch 安装媒体启动，最好用最新的安装媒体
  2. 挂载根文件系统，例如以 root 身份`mount /dev/sdaX /mnt`，通过 `df -h` 确认根文件目录包含足够的空间
  3. 同样挂载 proc, sys 和 dev 文件系统：`mount -t proc proc /mnt/proc; mount --rbind /sys /mnt/sys; mount --rbind /dev /mnt/dev`
  4. 如果系统使用默认的数据库目录位置，可以通过 root 用户执行下面命令`pacman --root=/mnt --cachedir=/mnt/var/cache/pacman/pkg -Syu`来更新系统的 _pacman_ 数据库。
  5. 如果无法更新，可以[重新安装所有软件包](<../zh-cn/Pacman/%E6%8F%90%E7%A4%BA%E5%92%8C%E6%8A%80%E5%B7%A7.html#%E9%87%8D%E6%96%B0%E5%AE%89%E8%A3%85%E6%89%80%E6%9C%89%E8%BD%AF%E4%BB%B6%E5%8C%85> "Pacman/提示和技巧")。
  6. 更新之后，可以通过下面命令确认是否还存在损坏的包：`find /mnt/usr/lib -size 0`
  7. 通过`pacman --root /mnt --cachedir=/mnt/var/cache/pacman/pkg -S _package_`重新安装依然损坏的软件包

#### pacman: command not found

如果`/var/cache/pacman/pkg`是一个符号链接， _pacman_ 在升级自身时会创建该目录并移除符号链接，这会导致升级失败，并产生`/usr/bin/pacman` 与其它 [pacman](<https://archlinux.org/packages/?name=pacman>)包包中内容丢失的后果。 

永远不要为`/var/cache/pacman/pkg`创建软连接，因为该目录受 _pacman_ 控制。使用`CacheDir`选项或通过绑定挂载。参见[#软件包的缓存目录](<#%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%9A%84%E7%BC%93%E5%AD%98%E7%9B%AE%E5%BD%95>)。 

如果你已经遇到这个问题，你可以手动提取安装包中`/usr`的内容恢复，并重新安装 _pacman_ 。详情见[FS#73306](<https://bugs.archlinux.org/task/73306>)和[论坛相关话题](<https://bbs.archlinux.org/viewtopic.php?id=241213>)

###  手动重新安装 pacman

####  使用 pacman-static

[pacman-static](<https://aur.archlinux.org/packages/pacman-static/>)AUR是 _pacman_ 的静态编译版本，因此系统中的库文件失效时依然可以运行它。当[部分升级](<../zh-cn/%E7%B3%BB%E7%BB%9F%E7%BB%B4%E6%8A%A4.html#%E4%B8%8D%E6%94%AF%E6%8C%81%E9%83%A8%E5%88%86%E5%8D%87%E7%BA%A7> "系统维护")后 _pacman_ 无法运行，静态编译版本就能够派上用场。 

置顶评论和PKGBUILD提供了直接下载二进制文件的方法，可以用于重新安装 _pacman_ 或在部分升级情况下升级整个系统。 

####  使用外部 pacman

如果`pacman-static`也无法使用，考虑使用外部 _pacman_ 。 最简单的办法是使用[archiso](<../zh-cn/Archiso.html> "Archiso")并指定`--sysroot`或`--root`参数到系统操作的挂载点。参见[Chroot#使用 arch-chroot](<../zh-cn/Chroot.html#%E4%BD%BF%E7%94%A8_arch-chroot> "Chroot")来挂载`--sysroot`参数需要的文件系统。 

####  手动提取

**警告：** 这种方式极其容易破坏你的系统，把它变得更糟。这个方式只是作为最后的措施，以防万一[#pacman 更新时崩溃](<#pacman_%E6%9B%B4%E6%96%B0%E6%97%B6%E5%B4%A9%E6%BA%83>)不起作用

即使 _pacman_ 严重损坏，你仍可以手动修复它，这需要下载最新的包并把它们解压到正确的目录。大致步骤如下： 

  1. 确定要安装的[pacman](<https://archlinux.org/packages/?name=pacman>)包依赖项
  2. 从你选择的[mirror](</wzh/index.php?title=Mirror&action=edit&redlink=1> "Mirror（页面不存在）")下载每个包
  3. 把每个包解压到 root
  4. 使用`pacman -S --overwrite`重新安装这些包来更新相应的软件包数据库
  5. 进行完整系统更新

如果你拥有一个健康的 Arch 系统，你可以这样查看依赖项的完整列表： 
    
    $ pacman -Q $(pactree -u pacman)
    
但是依据你遇到的问题，你可能只需要更新其中的几个。解压一个包的示例是： 
    
    # tar -xvpwf _package.tar.zst_ -C / --exclude .PKGINFO --exclude .INSTALL --exclude .MTREE --exclude .BUILDINFO
    
注意`w`参数表示交互模式。以非交互方式运行是非常冒险的，因为你可能就此覆盖了一个重要文件。你也要注意以正确的顺序解压软件包（例如先解压依赖）。 [这个帖子](<https://bbs.archlinux.org/viewtopic.php?id=95007>)包含了一些这个过程的例子，这些例子中只有少量 _pacman_ 依赖项损坏。 

###  升级系统重启后，出现"unable to find root device"错误，无法登录

很有可能 [initramfs](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#initramfs> "Initramfs") 在[内核](<../zh-cn/%E5%86%85%E6%A0%B8.html> "Kernel")升级时损坏（例如由错误地使用 _pacman_ 的 `--overwrite` 选项导致）。有两个选择；首先尝试 _Fallback_ 启动项。 

**提示：** 万一你删除了 _Fallback_ 启动项，你总可以在启动加载器菜单显示出来的时候按`Tab`键（对于 Syslinux）或者按`e`键（对于 GRUB 或者 systemd-boot），将它重命名为`initramfs-linux-fallback.img`然后按`Enter`或者`b`（取决于你的[启动加载器](</wzh/index.php?title=%E5%90%AF%E5%8A%A8%E5%8A%A0%E8%BD%BD%E5%99%A8&action=edit&redlink=1> "启动加载器（页面不存在）")以新参数启动的方式）

一旦系统启动，从控制台或终端（为备用[linux](<https://archlinux.org/packages/?name=linux>)包内核）运行这条命令来重建 initramfs 映像： 
    
    # mkinitcpio -p linux
    
如果上面方法不行，从一个最新的 Arch 发行版本（CD/DVD 或者 U盘），分别[挂载](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html#%E6%8C%82%E8%BD%BD%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "挂载")你的根目录和启动分区到`/mnt`和`/mnt/boot`，然后用 _arch-chroot_ [chroot](<../zh-cn/Chroot.html> "Chroot")： 
    
    # arch-chroot /mnt
    # pacman -Syu mkinitcpio systemd linux
    
**注意：**

  * 如果你没有一个当前的发行或者你只有某些其他的 "live" Linux 发行版，你可以用老式的方法[chroot](<../zh-cn/Chroot.html> "Chroot")。显然，这种方式比简单地运行`arch-chroot`脚本需要更多的输入
  * 如果 _pacman_ 伴随`Could not resolve host`运行失败，请[检查你的网络连接](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#%E6%A3%80%E6%9F%A5%E8%BF%9E%E6%8E%A5> "网络配置")
  * 如果无法进入 arch-chroot 或 chroot 环境，但是需要重新安装软件包，可以使用 `pacman --sysroot /mnt -Syu foo bar` 从而在你的根分区下使用 _pacman_

重新安装内核([linux](<https://archlinux.org/packages/?name=linux>)包 软件包)将会自动运行 `mkinitcpio -p linux` 重新生成 initramfs 镜像，不需要单独生成。 

之后建议执行 `exit`, `umount /mnt/{boot,} ` 然后 `reboot`. 

###  'warning: current locale is invalid; using default "C" locale' 错误

错误信息已经很明确了，locale 设置不正确，请阅读[Locale](<../zh-cn/Locale.html> "Locale")进行设置。 

###  Pacman 不使用我的代理设置

正确设置环境变量（`$http_proxy`, `$ftp_proxy` 等）。如果使用 [sudo](<../zh-cn/Sudo.html> "Sudo")，需要让 sudo [将这些变量传递给 pacman](<../zh-cn/Sudo.html#%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F_variables> "Sudo")。另外，在更新密钥前确保`/etc/pacman.d/gnupg/dirmngr.conf`路径的 [dirmngr](<../zh-cn/GnuPG.html#%E5%85%AC%E9%92%A5%E6%9C%8D%E5%8A%A1%E5%99%A8> "GnuPG")配置文件`honor-http-proxy`变量设置正确。 

###  如何重装所有包并保留安装和依赖信息？

重装所有软件包：`pacman -S $(pacman -Qnq)`（`-S` 选项会保留安装缘由）。 

接着需要重装外来包（不在官方仓库里的软件包）。外来包可通过`pacman -Qmq`查看。 

###  "Cannot open shared object file" 错误

有可能是前一次 _pacman_ 事务中删除或者损坏了 pacman 自身需要的一些共享库。 

要修复这种情况，你需要手动解压那些共享库文件到文件系统中合适的地方。首先请查明哪个包中包含有所需的库文件，然后在 _pacman_ 缓存中 (`/var/cache/pacman/pkg/`) 找到对应的包。解压出需要的库文件到文件系统的对应位置，如此可以继续使用 _pacman_ 。 

之后需要重新安装损坏的软件包。注意你可能需要使用 `--overwrite` 选项覆盖掉你刚刚解压出的系统文件，因为 _pacman_ 可能没有跟踪到对应的文件信息。 _pacman_ 随后会使用包中的文件正确替换掉共享库文件。如此能修好您的 pacman ，然后请继续更新系统中剩下的软件包。 

###  软件包下载停滞

一些网络问题可能会报告阻止了 _pacman_ 更新和同步仓库。[[3]](<https://bbs.archlinux.org/viewtopic.php?id=68944>) [[4]](<https://bbs.archlinux.org/viewtopic.php?id=65728>) 在实体机中安装 Arch Linux 时，这些问题已经通过替换默认的 pacman 文件下载器得到了解决 (更多细节请参阅 [Pacman/提示和技巧#性能](<../zh-cn/Pacman/%E6%8F%90%E7%A4%BA%E5%92%8C%E6%8A%80%E5%B7%A7.html#%E6%80%A7%E8%83%BD> "Pacman/提示和技巧") ) 。当在 VirtualBox 中安装 Arch Linux 作为客户操作系统时，这个问题也通过在主机属性中使用主机界面而不是 _NAT_ 来解决。 

###  无法从镜像服务器获取 'core.db'

如果从正确的[镜像服务器](<../zh-cn/%E9%95%9C%E5%83%8F%E6%BA%90.html> "Mirrors")收到此错误，请换一个[域名解析服务器](<../zh-cn/%E5%9F%9F%E5%90%8D%E8%A7%A3%E6%9E%90.html> "Resolv.conf")。 

###  error: 'local-package.pkg.tar': permission denied

如果你想要在一个 sshfs 上使用`pacman -U`安装软件包并遇到了这个错误，将包移动到本地目录，再试一次。 

###  error: could not determine cachedir mount point /var/cache/pacman/pkg

在 chroot 环境中执行 `pacman -Syu` 可能发生此错误: 
    
    error: could not determine cachedir mount point /var/cache/pacman/pkg
    error: failed to commit transaction (not enough free disk space)
    
通常是因为进入 chroot 时，进入的目录不是挂载点。解决方法请参考[从现有 Linux 发行版安装 Arch Linux#下载基本工具](<../zh-cn/%E4%BB%8E%E7%8E%B0%E6%9C%89_Linux_%E5%8F%91%E8%A1%8C%E7%89%88%E5%AE%89%E8%A3%85_Arch_Linux.html#%E4%B8%8B%E8%BD%BD%E5%9F%BA%E6%9C%AC%E5%B7%A5%E5%85%B7> "从现有 Linux 发行版安装 Arch Linux")， [arch-chroot(8)](<https://man.archlinux.org/man/arch-chroot.8>) 解释问题的原因，并提供了一个通过 bind mount 解决问题的方法。 

### error: GPGME error: No data

如果你无法更新包，并遇到了该问题，尝试 

`rm -r /var/lib/pacman/sync/`

后再次更新。 

如果删除sync中的同步文件不能解决问题，请通过`file /var/lib/pacman/sync/*`检查同步文件是否为`gzip compressed data`，使用路由或代理可能会损坏下载的文件。 

如果同步文件是正确的类型，那么问题可能出在镜像源上。使用`pacman-conf -r core`和`pacman-conf -r extra`查询使用的镜像源，将命令输出的第一个URL粘贴到浏览器访问，检查返回的文件。如果返回有问题，在{ic|/etc/pacman.d/mirrorlist}}里修改为其他可用镜像源。 

##  另请参见

  * [Pacman 主页](<https://pacman.archlinux.page/>)
  * [libalpm(3)](<https://man.archlinux.org/man/libalpm.3>)
  * [pacman(8)](<https://man.archlinux.org/man/pacman.8>)
  * [pacman.conf(5)](<https://man.archlinux.org/man/pacman.conf.5>)
  * [repo-add(8)](<https://man.archlinux.org/man/repo-add.8>)
  * [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR")
