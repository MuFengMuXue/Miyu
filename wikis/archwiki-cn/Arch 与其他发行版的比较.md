**翻译状态：**

  * 本文（或部分内容）译自 [Arch compared to other distributions](<https://wiki.archlinux.org/title/Arch_compared_to_other_distributions> "arch:Arch compared to other distributions")，最近一次同步于 2017-03-06，若英文版本有所[更改](<https://wiki.archlinux.org/title/Arch_compared_to_other_distributions?diff=0&oldid=466779>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Arch_compared_to_other_distributions_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Arch Linux](<../zh-cn/Arch_Linux.html> "Arch Linux")
  * [基于 Arch 的发行版](<../zh-cn/%E5%9F%BA%E4%BA%8E_Arch_%E7%9A%84%E5%8F%91%E8%A1%8C%E7%89%88.html> "基于 Arch 的发行版")
  * [Pacman/Rosetta](<../zh-cn/Pacman/%E5%90%84%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%AE%A1%E7%90%86%E5%99%A8%E5%91%BD%E4%BB%A4%E5%AF%B9%E5%BA%94%E5%85%B3%E7%B3%BB.html> "Pacman/Rosetta")

本文在 Arch Linux 、其他流行的 GNU/Linux 发行版和类 UNIX 操作系统之间做了一些比较，以帮助用户判断 Arch Linux 是否能符合他们的需要。虽然对此进行一些描述有助于用户理解这些操作系统之间的不同点，但是比较 Arch Linux 和其他操作系统的最好办法还是由用户自行安装它们并进行亲身体验。 

英文维基百科的[《操作系统比较》](<https://en.wikipedia.org/wiki/Comparison_of_operating_systems> "w:Comparison of operating systems")和[《Linux 发行版比较》](<https://en.wikipedia.org/wiki/Comparison_of_Linux_distributions> "w:Comparison of Linux distributions")这两个页面包含了更详细的比较信息。 

在接下来的部分中，只有 Arch Linux 与其他发行版做了比较。社区适配的支持 x86_64 以外的架构的版本在[基于 Arch 的发行版](<../zh-cn/Arch-based_distributions.html> "Arch-based distributions")中列出。 

##  与基于源码的发行版对比

基于源码的发行版具有高度可移植性，非常容易被移植到不同架构的系统上。它们可以根据特定计算机的体系架构和使用情况，控制和编译整个系统和所有软件包，其优化是最佳的。但缺点是如果计算机系统的配置性能较低，安装系统和软件包的源码编译会极为费时费力。Arch Linux 的基础软件包和其他所有软件包仅为 x86-64 架构进行编译。 

### CRUX

  * [CRUX](<https://crux.nu/>) 是让 Judd Vinet 有了创建 Arch 的灵感的、专注于 [KISS](<../zh-cn/Arch_terminology.html#KISS> "Arch terminology") 法则的一种轻量级发行版。
  * CRUX 使用 BSD 风格的启动脚本，而 Arch Linux 使用 [systemd](<../zh-cn/Systemd.html> "Systemd") 。
  * 尽管 Arch Linux 使用滚动升级机制，CRUX 也差不多每年都会有发行版。
  * 两者都提供了类 Ports 系统，并且和 *BSD 一样都提供了一个基础系统以供用户在其之上进行构建。
  * Arch Linux 使用 [pacman](<../zh-cn/Pacman.html> "Pacman") 来进行二进制包管理，同时还使用 [Arch 构建系统](<../zh-cn/Arch_%E6%9E%84%E5%BB%BA%E7%B3%BB%E7%BB%9F.html> "Arch 构建系统")。CRUX 使用一个叫 _prt-get_ 的社区开发软件和它自己的 Ports 系统来处理依赖关系解析。尽管如此，CRUX 上所有的软件包都需要从源代码进行编译，即使 CRUX 的基础系统是基于二进制包的。
  * Arch Linux 和 CRUX 官方都仅支持 x86_64 架构。
  * Arch Linux 的软件仓库提供大量编译好的二进制软件包。除此之外，还拥有 [Arch 用户软件仓库（AUR）](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93_\(AUR\).html> "Arch 用户软件仓库 \(AUR\)")。CRUX 的软件仓库则比较逊色，并且其 Ports 系统也缺乏官方支持。

### LFS

  * [LFS](<https://www.linuxfromscratch.org/lfs/>)（Linux From Scratch）只是以文档形式存在，它提供的文档指导用户如何从零开始构建一个完全个性化的 GNU/Linux 操作系统：从如何获取构建一个基础操作系统所需的源代码，到如何手动编译，如何打补丁，如何对系统进行配置。总之，LFS 提供了一个构建和定制基础系统的良好教程。
  * LFS 不提供在线软件仓库。它必须由用户手动获取源代码，然后用 _make_ 编译安装它们（这需要一些软件包管理方法，而这些方法在 [LFS Hints](<https://lfs.lug.org.cn/hints/>) 里面提到过）。
  * Arch Linux 基础系统除了提供和 LFS 一样的软件包，还包含 [systemd](<../zh-cn/Systemd.html> "Systemd")、[pacman](<../zh-cn/Pacman.html> "Pacman") 等一些额外的工具，并且这些软件都已经为 x86_64 架构编译过了。Arch 社区和开发者提供了数以千计的软件包，这些软件包可以通过 [pacman](<../zh-cn/Pacman.html> "Pacman") 或者 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 脚本进行安装（PKGBUILD 脚本需要和 [Arch Build System](<../zh-cn/Arch_Build_System.html> "Arch Build System") 一起使用）。除此之外，Arch Linux 还包含了一个名叫 [makepkg](<../zh-cn/Makepkg.html> "Makepkg") 的工具来生成便于 [pacman](<../zh-cn/Pacman.html> "Pacman") 使用的软件包。
  * Judd Vinet 从头开始构建了 Arch，然后用 C 语言编写开发了 [pacman](<../zh-cn/Pacman.html> "Pacman")。所以，Arch Linux 有时候会被幽默的描述为“有一个很好的软件包管理器的 Linux”。

###  Gentoo/Funtoo Linux

  * Arch Linux 和 Gentoo Linux 都是滚动升级的发行版，所以在上游（原始开发者）软件包发布不久，两者就会有软件包可以用。
  * Gentoo Linux 的基础系统和软件包都是根据用户指定的 _USE_ 标识直接从源代码构建。Gentoo Linux 提供了一个类 Ports 系统（ Ports 是 BSD 系统上的一个系统工具）来从源代码编译软件包，而 Arch Linux 基础系统被设计为“直接由预构建好的 x86_64 二进制软件包组成”。一般来说，Arch Linux 更易于构建和升级，而 Gentoo Linux 更易于进行系统化的定制。
  * Arch Linux 只支持 x86_64 架构，而 Gentoo Linux 对 x86（i486/i686）、x86_64、PPC/PPC64、SPARC、Alpha、ARM、MIPS、HPPA、S/390、Itanium、M68K 以及 RISC-V 架构均提供官方支持。
  * Gentoo Linux 的官方包管理工具比 Arch Linux 的更加复杂和“强大”，并且 Gentoo Linux 的某些核心功能特性（比如 [USE 标记](<https://wiki.gentoo.org/wiki/Handbook:X86/Working/USE/zh-cn>)、[SLOTs](<https://wiki.gentoo.org/wiki/Handbook:X86/Working/Portage/zh-cn#.E7.AE.80.E4.BB.8B_.3D>) 等等）在 Arch Linux 中并没有相对应的替代品。究其原因，首先是因为 Arch Linux 主要是一个二进制发行版，其次是因为 Gentoo Linux 和 Arch Linux 在[设计理念](<../zh-cn/Arch_Linux.html#Principles> "Arch Linux")上有些许差别，Arch Linux 在原则上更偏向于架构的简洁性和避免过度设计。
  * 因为 Gentoo Linux 和 Arch Linux 的安装都只包含一个基本系统，所以两者都被认为是需要高度定制化的系统。一般来说，Gentoo Linux 用户如果习惯于 [systemd](<../zh-cn/Systemd.html> "Systemd") 的话，对 Arch Linux 的大多数方面都会比较满意。

### GNU Guix System

  * [GNU Guix System](<https://guix.gnu.org/>) 受到 [NixOS](<https://nixos.org/>) 的启发，类似于 Arch Linux 受到 [CRUX](<https://crux.nu/>) 的启发。
  * Arch Linux 和 Guix System 都是滚动发布发行版，使软件包在上游发布后短时间内可供发行版使用。然而，Guix 系统主要是一个基于源代码的发行版（尽管存在预构建的二进制文件并称为“[替代品](<https://guix.gnu.org/en/manual/en/guix.html#Substitutes>)”），而 Arch Linux 主要是一个二进制发行版。
  * Arch Linux 使用 [pacman](<../zh-cn/Pacman.html> "Pacman") 作为包管理器，而 Guix System 使用 [GNU Guix](<../zh-cn/GNU_Guix.html> "GNU Guix")，它支持其他发行版中不存在的[实验性打包功能](<https://guix.gnu.org/manual/en/html_node/Features.html>)。
  * Arch Linux 只支持 x86_64，而 Guix System 正式支持[多种架构](<https://guix.gnu.org/manual/en/html_node/GNU-Distribution.html>)。
  * Arch Linux 使用 [systemd](<../zh-cn/Systemd.html> "Systemd") 作为 [init](<../zh-cn/Init.html> "Init") 系统，而 Guix System 使用 [GNU Shepherd](<https://www.gnu.org/software/shepherd/>)。
  * Guix System 打破了许多传统的 Unix 概念，包括[文件系统层次结构标准](<https://wiki.archlinux.org/title/Arch_filesystem_hierarchy> "en:Arch filesystem hierarchy")。例如，在传统发行版中分布在不同的目录中的许多文件，在Guix系统中将位于`/gnu/store/`。
  * Arch Linux 偶尔会发布非自由软件（通常是驱动程序），而 Guix System 只发布自由软件，并得到自由软件基金会的认可——尽管存在为 Guix 提供[非自由软件](<https://wiki.archlinux.org/title/Free_Software_Foundation> "en:Free Software Foundation")的替代存储库。
  * Arch Linux 希望用户直接配置已安装的软件包，而 Guix System 鼓励在 Scheme 中进行全局系统配置，进而[实例化](<https://guix.gnu.org/manual/en/html_node/Invoking-guix-system.html>)配置文件。

##  与通用发行版的对比

这些发行版的优点是受众更加广泛，可以满足绝大部分用户对计算机操作系统的需求。 

###  Debian GNU/Linux

  * Debian 是上游最大的发行版，其社区规模更大。它提供稳定（Stable）、测试（Testing）和不稳定（Unstable）三个版本分支，包含超过51000个二进制包。而 Arch Linux 的软件仓库相对较小，但是如果算上 AUR 仓库，那么 Arch Linux 支持的软件数量也差不多。
  * Debian 对自由软件更热情，但也提供非自由软件仓库。Arch Linux 对 GNU 定义的非自由（“non-free”）软件更显宽容。
  * Debian 对稳定分支的测试更加详细彻底，软件基本是上冻结的，并提供[五年](<https://wiki.debian.org/LTS>)官方社区支持。Arch Linux 提供的的软件包会比 Debian Stable 中的软件包更新，但会与 unstable 和 testing 分支里的差不多，而且没有固定发布周期，均以滚动形式发布。
  * Debian 支持许多架构，包括 alpha、arm、hppa、i386、x86_64、ia64、m68k、mips、mipsel、powerpc、s390和sparc。而 Arch Linux 仅对 x86_64 架构提供官方支持，其对 arm 架构的支持则移植自社区项目（例如对 Raspberry Pi 的支持）。
  * Arch Linux 对从源码创建软件包提供更好的支持，有一个类 ports 系统。而 Debian 不提供类 Ports 系统，而是依靠它巨大的二进制软件包仓库。
  * Arch Linux 安装环境只提供最小的基本系统，然后通过编辑文本文件来配置系统。而 Debian 的配置方式则更加自动化，并且还提供多种安装方式，例如使用 _apt_ _任务_ 来安装预先选择的软件包组。
  * 在启动脚本上，Debian（ 8.0 或更高版本）和 Arch Linux 均使用 [Systemd](<../zh-cn/Systemd.html> "Systemd")，因为其总体性能是相当优异的。
  * Arch Linux 一般将 lib 软件库与其头文件一同打包在一起，而在 Debian 中，头文件必须单独下载，并将 lib 软件库与头文件分别打包。
  * Arch Linux 将补丁保持在最低限度，只会在迫不得已的时候才会去打补丁，以避免出现上游无法审阅的问题。而 Debian 的用户众多，所以会经常对软件包打补丁。

### Fedora

  * Fedora Linux 是 Red Hat® Enterprise Linux （红帽企业版 Linux，RHEL）的上游社区发行版，也是一种技术先导发行版，对新技术的使用非常激进。红帽（Red Hat）公司是该项目的主要赞助商，但成千上万的独立开发人员也为 Fedora 做出了贡献。软件包和项目在 Fedora 上发布，通过其自己独特的测试和质量保证流程，这些功能迁移到 CentOS Stream，并最终被合并引入到 Red Hat Enterprise Linux 中，其中一些最终被其他发行版采用。Arch Linux 没有固定版本，也不作为另一个发行版的分支，即使许多其他发行版基于 Arch Linux（例如 Steam Deck 的 SteamOS）。
  * Fedora 使用 [RPM 格式软件包、 DNF 软件包管理器](<https://docs.fedoraproject.org/en-US/fedora/latest/system-administrators-guide/package-management/DNF/>)。而 Arch Linux 使用 [pacman](<../zh-cn/Pacman.html> "Pacman") 管理软件包。这两个项目的许多软件包，特别是桌面环境，都被描述为“原版”，并且没有自定义。
  * Fedora 坚持开源理念，拒绝在官方仓库中包含非自由软件包，默认不提供有专利限制的软件。例如 MP3 支持（从 Fedora 25 开始已重新支持 MP3，而且一些第三方源通常也会提供这些内容）。而 Arch Linux 对于 MP3 及非自由软件则更加宽松，尊重用户的知情权和使用权。
  * Fedora 提供许多不同的安装方式，包括图形化 Anaconda 安装程序、最小化安装和专家安装选项，有助于安装基本系统或是直到安装您选择的成熟桌面环境。Fedora "spins" 还提供许多不同的图形化桌面环境以供用户选择（这些桌面环境都会附带一些默认的软件包）。Arch Linux 被设计为仅提供一些简单脚本来进行最小化系统安装，并且同样可以根据用户个人需要安装使用不同的图形化桌面环境。
  * Fedora 发行周期比较固定，但官方支持通过 dnf-plugin-system-upgrade（适合大部分的版本）或 rpm-ostree（适合 Fedora Atomic Host）工具进行跨版本升级。而 Arch Linux 是通过滚动升级系统。
  * Arch Linux 有 ports 系统，而 Fedora 有 [Fedora Copr](<https://copr.fedorainfracloud.org/>)（一个类 AUR 构建系统）。
  * Arch Linux 和 Fedora 都面向有经验的用户和开发人员，两者都倡导用户积极为项目开发做出贡献。
  * Fedora 在 SELinux 整合，GCJ 编译包（GCJ 的目的是解除对 Oracle JRE 的依赖）等方面是走在各发行版的前列的，并且会积极为上游开发做贡献。和其他项目相比，红帽公司和 Fedora 开发人员贡献的 Linux 内核代码最多。
  * ArchWiki 被认为是各发行版的Wiki中内容最丰富和最易用的。而 Fedora wiki 仅是开发者、测试者和用户间交流信息的平台，并不是和 ArchWiki 一样为最终用户准备。其实它更像一个问题追踪和合作开发的 wiki。

### Slackware

  * Slackware 使用 BSD 风格的 [init](<../zh-cn/Init.html> "Init") 脚本，而 Arch Linux 使用 [systemd](<../zh-cn/Systemd.html> "Systemd")。
  * Arch Linux 有一个强大完整的软件包管理系统 [pacman](<../zh-cn/Pacman.html> "Pacman")。与 Slackware 的标准工具不同，它可以自己处理依赖关系并提供更加自动化的系统升级方式。Slackware 的用户会更喜欢手动处理依赖关系，以尽可能控制自己的系统，而 Slackware 本身也对预编译的库和依赖提供杰出的支持。
  * Arch Linux 是一个滚动升级的系统，而 Slackware 的系统版本和软件包的发布则更为保守，它会更喜欢提供经过验证的稳定软件包。在这个方面，Arch Linux 更为 _“前卫”_ 。
  * Arch Linux 官方软件仓库提供成千上万的二进制软件包，而 Slackware 官方支持的软件包就比较少了。
  * Arch Linux 提供 [Arch Build System](<../zh-cn/Arch_Build_System.html> "Arch Build System")（一个类 Ports 系统）和 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR")（由用户贡献的数以万计的 PKGBUILD 的集合）。Slackware 提供一个类似的系统 [slackbuilds.org](<https://www.slackbuilds.org>)，它是一个半官方支持的 Slackbuilds（和 PKGBUILD 相似）仓库。Slackware 用户一般会对 Arch Linux 的大多数方面非常满意。

##  与新手友好发行版对比

“新手友好版”有时也被叫做“新手发行版”。这些对新手友好的发行版之间有许多相同之处，而 Arch Linux 和它们其中的任何一个发行版都不同。如果您想通过构建极简系统的方式来学习 GNU/Linux ，Arch Linux 或许是一个好选择。因为相比一些“新手发行版”，Arch Linux 只需安装很少的软件包。一些不同的“新手发行版”之间的特点如下所述： 

### Ubuntu

  * Ubuntu 是一个非常流行的基于 Debian 的发行版，由 Canonical 公司提供商业支持。而 Arch Linux 是由志愿者从头开始独立构建开发而成的。
  * Ubuntu 和 Arch Linux 的目标不同，并且面向的用户群体也不一样。Arch Linux 为那些渴望自己动手的用户设计，而 Ubuntu 则提供图形化安装程序自动配置好了的系统，对新手用户来说更“友好”。Arch Linux 从一开始就设计了一个最小化的基础系统，非常依赖有一定知识基础的用户按自己的特定需求进行个性化定制。一般来说，开发者和动手能力强的用户更喜欢 Arch Linux 。不过有许多 Arch Linux用户是从 Ubuntu 开始学习，掌握一定的技巧后最终转向使用 Arch Linux 。
  * Arch Linux 开发不偏向于任何超出其社区提供支持的特定用户界面。此外，Canonical 公司的商业性质导致他们做出了一些有争议的决定，例如在 Unity 的 _Dash_ 菜单中包含广告和收集用户数据。而 Arch Linux 是一个独立的、由社区驱动的项目，没有商业议程。
  * Ubuntu 开发和推广的重心似乎转移到了触摸屏设备上，而 Arch Linux 的开发依然坚持以用户为中心，鼓励社区合作开发客制化的解决方案。
  * Ubuntu 通常每 6 个月发布新版本，而 Arch Linux 通过滚动升级系统。
  * Arch Linux 提供类 Ports 的软件包构建系统和 [Arch User Repository](<../zh-cn/Arch_User_Repository.html> "Arch User Repository")，用户可以分享源代码编译脚本，然后用 [Pacman](<../zh-cn/Pacman.html> "Pacman") 安装管理。Ubuntu 则使用更复杂的 [apt](<https://en.wikipedia.org/wiki/Advanced_Packaging_Tool> "wikipedia:Advanced Packaging Tool")，可以通过 [Personal Package Archives](<https://launchpad.net/ubuntu/+ppas>)重新分发二进制软件包。
  * 这两个发行版的社区在某些方面也有所不同。Arch 社区要小的多，更倾向于鼓励用户为 Arch Linux 奉献一份力量。相比之下，Ubuntu 社区更加庞大，并能容忍其中并没有积极为开发、打包和维护做贡献的大多数用户。

### Linux Mint

  * [Linux Mint](<https://www.linuxmint.com/>) 最初是一个 [Ubuntu](<#Ubuntu>) 的衍生版本。后来又衍生出 LMDE（ Linux Mint Debian Edition ），LMDE 是一个基于 [Debian](<#Debian_GNU/Linux>) 的版本。而 Arch Linux 是一个独立的发行版，它依赖于自己的[构建系统](<../zh-cn/Arch_%E6%9E%84%E5%BB%BA%E7%B3%BB%E7%BB%9F.html> "ABS")和[官方仓库](<../zh-cn/Official_repositories.html> "Official repositories")。
  * 为了方便系统维护，Linux Mint 包含了一些图形化工具，它们叫做 _MintTools_ （Mint 工具），而 Arch Linux 仅提供简单的命令行工具，例如 [Pacman](<../zh-cn/Pacman.html> "Pacman")，因此 Arch Linux 的系统管理工作需要由用户自行组织安排。
  * Linux Mint 主要以 [Cinnamon](<../zh-cn/Cinnamon.html> "Cinnamon") 、 [MATE](<../zh-cn/MATE.html> "MATE") 与 [Xfce4](<../zh-cn/Xfce.html> "Xfce") 作为它的图形界面，不过它也可以由用户自行安装选择 [KDE](<../zh-cn/KDE.html> "KDE") 。Linux Mint 同时支持 Plus codecs、Flash、DVD playback 和 MP3，这其中有一些是有专利限制的私有软件。
  * Linux Mint 半年发布一次新版本。也就是在新版本 Ubuntu 发布一个月之后。Linux Mint 的每一个版本都基于最新的 Ubuntu LTS（长期支持版），并且提供五年技术支持。 Mint 的 Debian 版本 (LMDE) 基于 Debian Stable分支。而且只接收来自 Mint 的软件包更新和安全更新。与之相反，Arch Linux 则完全是一个滚动更新的发行版。

### openSUSE

openSUSE 诞生于最初的 SUSE Linux，由 SUSE（SUSE Enterprise Linux 的制造商）赞助支持。SUSE Linux Enterprise Desktop （SLED） 基于 openSUSE Tumbleweed，与 openSUSE Leap 共享一个通用代码库。 

  * OpenSUSE 使用 Zypp 软件包管理器（终端命令为 _zypper_ ）、RPM 格式软件包以及备受推崇的 YaST2 图形化配置工具。Arch Linux 使用 Pacman 来管理 tar.zstd 包，没有提供此类图形配置工具。一般 openSUSE 更适合经验较少或需要使用图形界面自动完成配置的用户。

  * openSUSE 提供 2 个不同的版本： 
    * Leap 是 openSUSE 的长期支持版本，具有离散版本。Leap 版本一般是每年发布一个版本，软件包会比 Arch Linux 更旧。
    * Tumbleweed 是 openSUSE 的滚动发布版本。Tumbleweed 版本是滚动更新的，软件包版本的新旧和 Arch Linux 差不多。

  * openSUSE 默认不提供有专利限制的软件，比如 MP3 支持。您需要添加第三方源来取得这些内容。而 Arch Linux 对于 MP3 及非自由软件更加宽松，更倾向于将决定权交给用户。
  * 相比之下，Arch Linux 严格来说是一个滚动发布模型，不提供离散发布版本。Arch Linux 默认不是完整的桌面环境，只提供最小的基本系统安装。因此，openSUSE 可能更适合那些想要图形环境、自动配置或开箱即用的功能，同时仍然允许在所有发行版上进行自定义的用户。

###  Mandriva/Mageia

  * Mandriva Linux (以前叫 Mandrake Linux ) 创建于1998年，它的目标是让每个人使用 GNU/Linux 都易如反掌。Mandriva Linux 使用基于 RPM 的 _urpmi_ 软件包管理器，目前已经不再维护。

  * Mageia Linux 是一个由前 Mandriva 员工创建的 Mandriva 分支，它反对 Mandriva 的商业地位。与 Mandriva 不同，Mageia 是一个非盈利的由社区驱动的发行版。然而 Arch Linux 是一个比 Mandriva 或者 Mageia 都要简单的发行版。安装与配置基于文本环境，而且依赖于更多的手动配置，Arch Linux 的受众目标瞄准的是有 Linux 经验的中高级用户。

##  与BSD系列操作系统的对比

  * BSD 系列操作系统都起源于加利福尼亚大学伯克利分校所做的工作，它们致力于提供一个可以自由再分发、免费的 UNIX 系统。它们不是 GNU/Linux 发行版，而是以原始的 AT&T UNIX 系统的代码为基础演进的类 UNIX 操作系统。
  * Arch Linux 和 BSD 都提供紧密集成的基本系统和 Ports 软件包管理系统。但与 GNU/Linux 系统（比如 Arch Linux）不同，BSD 操作系统的内核和用户空间的程序，如 shell 和常用工具（像 ls、cp、cat 和 ps）是集中在单一的源代码仓库中一起开发的。
  * 与 GPL 许可证相反，BSD 许可证比较宽松，GPL 许可证规定衍生品需要在同一许可证下发布。而 Arch Linux 是在 GPL 许可证下发布的。
  * 要获得 BSD 变体的更多信息，请参阅 [Wikipedia:Comparison of BSD operating systems](<https://en.wikipedia.org/wiki/Comparison_of_BSD_operating_systems> "wikipedia:Comparison of BSD operating systems")。

##  参阅

  * [DistroWatch.com- Linux 发行版新闻和评论](<https://distrowatch.com/>)
