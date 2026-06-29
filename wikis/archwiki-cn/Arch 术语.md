相关文章

[Help:术语表](<../zh-cn/Help:%E6%9C%AF%E8%AF%AD%E8%A1%A8.html> "Help:术语表")

**翻译状态：**

  * 本文（或部分内容）译自 [Arch terminology](<https://wiki.archlinux.org/title/Arch_terminology> "arch:Arch terminology")，最近一次同步于 2024-07-16，若英文版本有所[更改](<https://wiki.archlinux.org/title/Arch_terminology?diff=0&oldid=812480>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Arch_terminology_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

本页面试图揭开 Arch Linux 社区术语的神秘面纱。您可以自由的添加或更改任何术语，但是请使用某个章节的编辑选项。如果想添加新术语，请去原文界面编辑，然后翻译到此界面。 

注：本文为规避后续争议，术语权且采用与原文一致的顺序。 

## ABS

ABS 是 [Arch Build System](<../zh-cn/Arch_%E6%9E%84%E5%BB%BA%E7%B3%BB%E7%BB%9F.html> "Arch 构建系统") 的缩写。 

## Arch Linux

应该用下面术语指代 Arch： 

  * **Arch Linux**
  * **Arch** （省略 Linux）
  * **archlinux** （UNIX 名）

Archlinux、ArchLinux、archLinux、aRcHlInUx 等称呼都是不标准的。 

'Arch' 在 "Arch Linux" 中的官方读音是 /ɑːrtʃ/。"arch" 的读音不同于 "ark"：和单词 "archer" 或 "archnemesis" 中的一样，与 "archangel" 中的不同。 近似拼音 "a er qi" 的读音，不读作 "a er ke"。 

##  Arch Linux 档案

[Arch Linux Archive](<../zh-cn/Arch_Linux_Archive.html> "Arch Linux Archive") (ALA)，故称 Arch Linux Rollback Machine (ARM)，保存历史上的官方软件仓库快照、ISO 镜像和 boot straps 压缩包。 

## AUR

[Arch User Repository](<../zh-cn/Arch_User_Repository.html> "Arch User Repository")（Arch 用户仓库） 是一个社区驱动的 Arch 用户仓库。其储存包的描述信息（[PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD")），后者允许您用 [makepkg](<../zh-cn/Makepkg.html> "Makepkg")，从源码构建包并通过 [pacman](<../zh-cn/Pacman.html#Additional_commands> "Pacman") 安装。AUR 的创建是为了整理和分享来自社区的新包，并促使 [extra 仓库](</wzh/index.php?title=Extra_repository&action=edit&redlink=1> "Extra repository（页面不存在）")尽快收录受欢迎的包。 

许多进入官方仓库的新包最先收录于 AUR。AUR 中，用户可以贡献自己的包构建（PKGBUILD 及相关文件）。AUR 社区可以对 AUR 中的包投票。如果一个包足够受欢迎——前提是它要有一个兼容的许可证，和良好的封装——它可能进入 _extra_ 仓库（可以直接通过 [pacman](<../zh-cn/Pacman.html> "Pacman") 或 [ABS](<../zh-cn/Arch_%E6%9E%84%E5%BB%BA%E7%B3%BB%E7%BB%9F.html> "ABS") 访问）。 

您可以[在这里](<https://aur.archlinux.org>)访问 _A_ rch Linux _U_ ser Community _R_ epository。 

## bbs

**B** ulletin **b** oard **s** ystem，在 Arch 中指[用户支持论坛](<https://bbs.archlinux.org>)。 

##  core/[core]

_core_ 仓库包含 Arch linux 的最基本软件包：一个命令行系统的所需都在 [core] 中。 

##  custom/user repository

任何人都可以创建供其它人使用的在线仓库。要这么做，需要一批软件包及对应的兼容 [pacman](<../zh-cn/Pacman.html> "Pacman") 的数据库文件。把这些托管到线上，其他人就可添加你的仓库并使用了。 

参考 [Custom local repository](<../zh-cn/Custom_local_repository.html> "Custom local repository"). 

## Developer

这些半神级的开发者，无偿地为 Arch 持续改进。他们的地位仅次于 Arch 的神祇 Judd Vinet 和 Aaron Griffin，而这两位神祇又只能屈居于“玉米饼（tacos）”之下。 

##  extra/[extra]

Arch 的官方软件包很精简，但是我们提供了更大更完整的 "附加" 软件仓库。其包含大量非 core 的软件包。此仓库在社区的强力支持下日益壮大。桌面软件环境，窗口管理器和常用程序都位于此仓库。 

##  initramfs/initrd

参见 [mkinitcpio](<../zh-cn/Mkinitcpio.html> "Mkinitcpio")。 

## KISS

Keep It Simple, Stupid 的简写。[简约](<../zh-cn/Arch_Linux.html#Simplicity> "Arch Linux")是 Arch Linux 坚持的原则。 

## makepkg

[makepkg](<../zh-cn/Makepkg.html> "Makepkg") 会读取 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 文件，然后按脚本编译软件包。所需的是 Linux 编译环境，[curl](<https://archlinux.org/packages/?name=curl>)包 和一些编译脚本。基于脚本构建的优点是一劳永逸。有了编译脚本后，只需执行 makepkg，它会执行剩余的工作：下载并验证源代码，检查依赖关系，配置构建时间，构建软件包，安装软件包到临时根目录，进行定制，生成元数据，然后打包供 [pacman](<../zh-cn/Pacman.html> "Pacman") 使用。 

## namcap

[namcap](<../zh-cn/Namcap.html> "Namcap") 是软件包分析工具，可以检查 Arch Linux 软件包及其 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 文件。 可以按规则检查文件列表、文件本身或单独的 PKGBUILD 文件。 

规则检查会返回三类消息：错误（error），警告（warning）或信息（information）（类似提示或注释）。错误（'E:'）是 namcap 非常确信错误并需要修复的东西。警告（'W:'）是 namcap 认为应当更改，但如果您清楚您在做什么，就可以忽略的东西。信息（'I:'）只在您使用 info 参数时显示。信息类消息提供无需更改任何东西但可能有用的的信息。 

## package

请参考 [Pacman#安装软件包](<../zh-cn/Pacman.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Pacman")。 

**注意：** 不同 GNU/Linux 发行版使用不同的包和包管理器，这意味着您不能用 pacman 在 Arch 上安装一个 Debian 软件包。

##  软件包维护者

软件包维护者的作用是：当上游新版本可用时，更新包；处理有关指定包中 bug 的支持问题。该术语适用于： 

  * Arch 员工，故称[受信用户（Trusted User，TU）](<https://lists.archlinux.org/archives/list/aur-general@lists.archlinux.org/thread/6UPKMAL2A7FNAUNWMTHWI4EXV2KS5OSC/>)，[管理](<../zh-cn/Package_Maintainers.html> "Package Maintainers") _extra_ 仓库中的包，并监督 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR")。他们由现有软件包维护者以多数票任命，并遵循[ AUR 软件包维护者指南](</wzh/index.php?title=AUR_Package_Maintainer_guidelines&action=edit&redlink=1> "AUR Package Maintainer guidelines（页面不存在）")和[软件包维护者章程](<https://package-maintainer-bylaws.aur.archlinux.org/>)。
  * 在[官方仓库](<../zh-cn/Official_repositories.html> "Official repositories")（尤其是 _core_ ）维护包的开发者。
  * 在 AUR 维护 PKGBUILD 的所有用户。

某个包的维护者是指此人当前对这个包负责。之前的维护者应当在 PKGBUILD 中，与其他对此包有贡献的人一同，作为贡献者列出。 

## pacman

请参考 [pacman](<../zh-cn/Pacman.html> "Pacman")。 

## PKGBUILD

[PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 是构建 Arch Linux 软件包所使用的脚本。详情参考 [Creating packages](<../zh-cn/Creating_packages.html> "Creating packages")。 

##  仓库/repo

软件仓库包含一个或（通常地）多个基于 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 预构建的软件包。[官方仓库](<../zh-cn/Official_repositories.html> "Official repositories")分成多个部分以便管理。Pacman 使用这些仓库查找和安装软件包。一个仓库可以是本地的（在您自己的电脑上），也可以是远程的（先下载软件包再安装）。 

## RTFM

[RTFM](<https://en.wikipedia.org/wiki/RTFM> "wikipedia:RTFM") 代表 "_R_ ead _T_ he _F_ riendly _M_ anual"（参阅友好文档）。很多 Linux/Arch 新用户在询问一个程序文档明确定义的问题时，会收到这个简洁回复。 

通常，在用户在发问前，未曾尝试自己寻找解决方案时，这个缩写会出现。如果有人这么回复您，请注意：这并不是侮辱，只是委婉地请您更细心些，同时对您显现出的疏忽表示略微不满。 

收到这个信息后，最正确的动作是阅读手册页面。要阅读某个特定程序的手册：`man _程序名称_`,。 

如果没有找到需要的信息，还可以查看下面内容： 

  * 搜索 [wiki](<../Special:%E6%90%9C%E7%B4%A2.html> "Special:搜索")
  * 搜索[论坛](<https://bbs.archlinux.org>)
  * 搜索[邮件列表](<https://www.google.com/#hl=en&q=arch+site:archlinux.org%2Fpipermail%2F>)
  * 搜索 [web](<https://www.google.com>)

注：以上链接直接出自英语原文，限于特殊情况，某些可能无法访问。读者请自行变通。 

##  测试仓库

主要的软件包/更新在正式发布前，会放在此仓库进行测试，查看是否有 bug 和升级问题。[默认禁用](<../zh-cn/Official_repositories.html#Testing_repositories> "Official repositories")，可在 `/etc/pacman.conf` 中启用。 

##  Arch 之道

[Arch Linux 原则](<../zh-cn/Arch_Linux.html#Principles> "Arch Linux")的一个非正式传统说法。 

##  受信用户（TU）

参见 [#软件包维护者](<#%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%BB%B4%E6%8A%A4%E8%80%85>)。 

## Wiki

我们的 [wiki](<https://en.wikipedia.org/wiki/Wiki> "wikipedia:Wiki") 一个存放 Arch Linux 文档的地方，任何人都可以对这些文档做贡献。 
