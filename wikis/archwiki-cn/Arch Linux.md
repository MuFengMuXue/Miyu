**翻译状态：**

  * 本文（或部分内容）译自 [Arch Linux](<https://wiki.archlinux.org/title/Arch_Linux> "arch:Arch Linux")，最近一次同步于 2025-04-30，若英文版本有所[更改](<https://wiki.archlinux.org/title/Arch_Linux?diff=0&oldid=828859>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Arch_Linux_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

Arch Linux 是一种通用操作系统，它是基于 x86-64 架构的一类 [GNU](<../zh-cn/GNU.html> "GNU")/Linux 发行版。 

Arch Linux 采用滚动升级模式，尽全力为用户提供最新的稳定版软件。初始安装完成的 Arch Linux 只是一个基本系统，随后用户可以根据自己的喜好安装需要的软件并配置成符合自己理想的个性化系统。 

##  核心原则

以下核心原则构成了我们通常所指的 Arch 之道，或者说 Arch 的哲学。或许最好的结词是 Keep It Simple, Stupid（对应中文为“保持简单，且一目了然”）。 

###  简洁

Arch Linux 将简洁定义为：**避免任何不必要的添加、修改和复杂化的增加** 。它提供的软件包都来自原始开发者（以下简称[上游](<https://en.wikipedia.org/wiki/Upstream_\(software_development\)> "wikipedia:Upstream \(software development\)")），且仅进行和本发行版（以下简称下游）相关的最小修改版本。 

  * 不包含上游不愿意接受的补丁。绝大部分 Arch 下游补丁都已经被上游接受，会在下一个正式版本里被包含。
  * 配置文件也是来自上游，它仅包含发行版必须的调整，比如特殊的文件系统路径变动。Arch Linux 不会在安装一个软件包后就自动启动软件包的服务。
  * 软件包通常都和一个上游项目直接对应。仅在极少数情况下才会拆分软件包。
  * 官方不支持图形化配置界面，建议用户使用命令行或文本编辑器修改设置。

###  现代化

Arch Linux 尽全力使软件处于最新的稳定版本，只要没有出现系统软件包损坏，都会尽量使用最新版本的软件包。 

Arch Linux 采用[滚动更新](<https://en.wikipedia.org/wiki/Rolling_release> "wikipedia:Rolling release")的方式，安装之后可以通过命令持续更新系统与软件包。 

Arch Linux 向 [GNU](<../zh-cn/GNU.html> "GNU")/Linux 用户提供了许多新特性，包括 [systemd](<../zh-cn/Systemd.html> "Systemd") 初始化系统、现代化的[文件系统](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html> "文件系统")、LVM2/EVMS、软件磁盘阵列（软 RAID）、[udev](<../zh-cn/Udev.html> "Udev") 支持、initcpio（附带 mkinitcpio）以及最新的 Linux 内核。 

###  实用性

Arch Linux 注重实用性，且尽力避免意识形态之争。最终的设计决策都是由开发者之间的共识决定，开发者依赖基于客观事实的技术分析和讨论，避免国家之间和政治因素的影响，不被世俗流行观点左右。 

Arch Linux 的仓库中包含大量的软件包和编译脚本。用户可以按照需要进行自由选择。仓库中既提供了开源、自由的软件，也提供了闭源软件。即**实用性大于意识形态** 。 

###  以用户为中心

许多 Linux 发行版都试图变得更加“用户友好”，Arch Linux 则一直是，且永远会是“**以用户为中心** ”。本发行版是为了满足贡献者的需求，而不是为了吸引尽可能多的用户。 

Arch Linux 适用于乐于自己动手的用户，因为他们往往更愿意花时间阅读文档，解决自己的问题。 

Arch Linux 鼓励每一个用户[参与](<../zh-cn/%E5%8F%82%E4%B8%8E%E8%B4%A1%E7%8C%AE.html> "参与贡献")和贡献，报告和帮助修复 [bugs](<https://gitlab.archlinux.org/groups/archlinux/packaging/-/issues>)，提供软件包补丁和参加核心[项目](<https://gitlab.archlinux.org/>)：Arch 开发者都是志愿者，通过持续的贡献成为团队中的一员。 _Archers_ 可以自行贡献软件包到 [Arch 用户仓库](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E4%BB%93%E5%BA%93.html> "Arch 用户仓库")，提升 [ArchWiki 文档质量](<../zh-cn/%E9%A6%96%E9%A1%B5.html> "首页")，在[论坛](<https://bbs.archlinux.org/>)、[邮件列表](<https://lists.archlinux.org/mailman3/lists/>)或者 [IRC](<../zh-cn/IRC_channels.html> "IRC channels") 中给其它用户提供技术支持。 

Arch Linux 现在是全球许多 GNU/Linux 用户的选择，已经有许多[国际社区](<../zh-cn/%E5%9B%BD%E9%99%85%E7%A4%BE%E5%8C%BA.html> "国际社区")提供帮助和文档的翻译。 

###  通用性

Arch Linux 作为一种通用 Linux 发行版，它的初始安装仅提供命令行环境：用户不需要删除大量不需要的软件包，而是可以从[官方软件仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方仓库")成千上万的高质量软件包中进行选择，并搭建自己的系统。目前支持 [x86-64](<https://en.wikipedia.org/wiki/x86-64> "wikipedia:x86-64") 架构。( [对 i686 架构的支持已经结束](<https://www.archlinuxcn.org/the-end-of-i686-support/>)） 

Arch Linux 使用 [Pacman](<../zh-cn/Pacman.html> "Pacman") [包管理系统](<https://en.wikipedia.org/wiki/Package_manager> "wikipedia:Package manager")实现系统和软件包的滚动升级。并且 Arch Linux 还提供一个类似 ports 的包构建系统（[Arch Build System](<../zh-cn/Arch_Build_System.html> "Arch Build System")），通过它可以轻松从源码构建和安装软件包，并用一个命令完成同步。您甚至可以用一个命令重新构建整个系统。Arch 还提供 [Arch 用户仓库](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E4%BB%93%E5%BA%93.html> "Arch 用户仓库")，它包含了成千上万个由用户自行维护的 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 脚本，配合 [makepkg](<../zh-cn/Makepkg.html> "Makepkg") 工具，从编译到打包一气呵成。用户还能轻松构建和维护属于自己的自定义软件源。 

##  历史沿革

这些年来，Arch 社区不断成长，最近也收到了大量的[关注和评论](<../zh-cn/Arch_Linux_%E6%96%B0%E9%97%BB%E6%8A%A5%E9%81%93.html> "Arch Linux 新闻报道")。 

除[少数特例](<https://lists.archlinux.org/archives/list/arch-dev-public@lists.archlinux.org/thread/RIZSKIBDSLY4S5J2E2STNP5DH4XZGJMR>)以外，Arch Linux 的开发者大部分是不收工资的志愿者与爱好者，目前也并没有通过 Arch Linux 赚钱的计划。Arch Linux 开发的详细历史可以浏览 [Wayback Machine 的 Arch 部分](<https://web.archive.org/web/*/archlinux.org>)和 [Arch Linux 新闻存档](<https://archlinux.org/news/>)及[Arch Linux CN 首页上的中文版新闻列表](<https://www.archlinuxcn.org/>)。 

###  早期

加拿大程序员、吉他手 Judd Vinet 从 2001 年早期开始开发 Arch Linux ，并在 2002 年 3 月 11 日正式发行 0.1 版。他受到 [Slackware](<http://www.slackware.com/>)、[BSD](<https://en.wikipedia.org/wiki/Berkeley_Software_Distribution> "wikipedia:Berkeley Software Distribution")、[PLD Linux](<https://www.pld-linux.org/>) 和 [CRUX](<https://crux.nu/>) 的启发，但在当时这些发行版普遍缺少软件包管理工具。所以 Vinet 同样以简洁为原则创建了这个发行版，并编写了 [Pacman](<../zh-cn/Pacman.html> "Pacman") 软件包，自动处理软件包的依赖解析、安装、删除和更新。 

###  中期

[这个图表](<https://wiki.archlinux.org/images/6/64/Archstats2002-2011.svg>)见证了Arch Linux 社区的稳步扩大。而且从早期开始，Arch 就树立起了[**开放、友好和社区互助** 的形象](<https://www.osnews.com/story/4827>)。 

###  ArchWiki 的诞生

2005 年 7 月 8 日，用 MediaWiki 搭建的 ArchWiki [开始运行](<../Project:%E5%85%B3%E4%BA%8E.html> "Project:关于")。 

###  A. Griffin 时代

2007 年下半年，Judd Vinet 退出了 Arch Linux 的开发，并[把领导权交给美国程序员 Aaron Griffin](<https://bbs.archlinux.org/viewtopic.php?id=38024>)，也就是 Phrakture，目前他依然是 Arch Linux 开发者。 

###  Arch 安装脚本

在 2012 年 7 月的 Arch Linux 安装介质中[弃用了](<https://www.archlinuxcn.org/install-media-20120715-released/>)基于菜单的 _Arch 安装框架_ （AIF），改为使用 _Arch 安装脚本_ （[arch-install-scripts](<https://archlinux.org/packages/?name=arch-install-scripts>)包）。 

###  Systemd 时代

2012 到 2013 年间， Arch 用 Systemd 替换了 System V init ：[[1]](<https://www.archlinuxcn.org/install-medium-20121006-introduces-systemd/>)[[2]](<https://www.archlinuxcn.org/systemd-is-now-the-default-on-new-installations/>)[[3]](<https://archlinux.org/news/end-of-initscripts-support/>)[[4]](<https://www.archlinuxcn.org/final-sysvinit-deprecation-warning/>)

###  抛弃 i686 支持

鉴于在开发者和社区中对 i686 架构的使用程度逐渐式微，[Arch Linux 对 i686 的支持已经于2017年11月底被抛弃](<https://www.archlinuxcn.org/the-end-of-i686-support/>)。 

###  选举项目的领导角色

2020 年初，Arch 开始用新的流程选择未来的领袖，详情记载在 [DeveloperWiki:Project Leader](<https://wiki.archlinux.org/title/DeveloperWiki:Project_Leader> "en:DeveloperWiki:Project Leader")。 

Aaron Griffin 决定不再担任项目领导，因此 Arch 通过选举方式正式确认 Levente Polyak 为新的领导，结果记录在[这里](<https://www.archlinuxcn.org/the-future-of-the-arch-linux-project-leader/>)。 

###  GitLab 时代

[2023 年 5 月](<https://www.archlinuxcn.org/git-migration-completed/>)，Arch Linux 将其打包基础设施迁移到 GitLab。除了内部更改和创新外，这也导致将 testing 仓库拆分为 core-testing 和 extra-testing，将 staging 仓库拆分为 core-staging 和 extra-staging，最后 community 已合并至 extra。在 [GitLab 博客](<https://about.gitlab.com/blog/2023/09/11/migrating-arch-linux-packaging-infrastructure-gitlab/>)上阅读更多详细信息。 

几个月后，即 [2023 年 11 月](<https://lists.archlinux.org/hyperkitty/list/arch-dev-public@lists.archlinux.org/thread/WYXDTJ3TR2DWRQCDZK44BQDH67IDVGTS/>)，旧的错误跟踪器（Flyspray）已迁移到 GitLab，其协作功能（问题和合并请求）已向公众开放。因为存档问题，保留一个旧错误跟踪器的静态副本，以保证链接（例如随机选择的[FS#56716](<https://bugs.archlinux.org/task/56716>)）仍然有效。 
