**翻译状态：**

  * 本文（或部分内容）译自 [PKGBUILD](<https://wiki.archlinux.org/title/PKGBUILD> "arch:PKGBUILD")，最近一次同步于 2025-03-22，若英文版本有所[更改](<https://wiki.archlinux.org/title/PKGBUILD?diff=0&oldid=827943>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/PKGBUILD_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Arch 打包准则](<../zh-cn/Arch_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Arch 打包准则")
  * [Arch 构建系统](<../zh-cn/Arch_%E6%9E%84%E5%BB%BA%E7%B3%BB%E7%BB%9F.html> "Arch 构建系统")
  * [Arch 用户软件仓库 (AUR)](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93_\(AUR\).html> "Arch 用户软件仓库 \(AUR\)")
  * [.SRCINFO](<../zh-cn/.SRCINFO.html> ".SRCINFO")

本页面讨论 `PKGBUILD` 中可由维护者定义的变量。若要获取关于 `PKGBUILD` 中的函数和创建软件包的基本信息，请参考[创建软件包](<../zh-cn/%E5%88%9B%E5%BB%BA%E8%BD%AF%E4%BB%B6%E5%8C%85.html> "创建软件包")和 [PKGBUILD(5)](<https://man.archlinux.org/man/PKGBUILD.5>)。 

`PKGBUILD` 是一个 [Bash](<../zh-cn/Bash.html> "Bash") 脚本，包含在构建 [Arch Linux](<../zh-cn/Arch_Linux.html> "Arch Linux") 软件包时需要的信息。 

Arch Linux 使用 [makepkg](<../zh-cn/Makepkg.html> "Makepkg") 构建软件包。当 _makepkg_ 运行时，它会在当前目录寻找 `PKGBUILD` 文件，并依照其中的指令编译或获取所需的文件，并生成 `_pkgname_.pkg.tar.zst` 软件包。生成的包内有二进制文件和安装指令，可以使用 [pacman](<../zh-cn/Pacman.html> "Pacman") 进行安装。 

必须定义的变量有 `pkgname`，`pkgver`，`pkgrel` 和 `arch`。在构建软件包时不强制要求定义 `license`，但若要分享 `PKGBUILD` 文件给其他人，推荐加上该变量，否则 _makepkg_ 会提示相关报错。 

一般来说，建议但不强制要求按照下面的顺序在 `PKGBUILD` 文件中定义这些变量。 

**提示：**

  * 使用 [namcap](<../zh-cn/Namcap.html> "Namcap") 来检查 `PKGBUILD` 文件中的常见打包问题。
  * 可以使用 [shellcheck(1)](<https://man.archlinux.org/man/shellcheck.1>) 来检查 `PKGBUILD` 中的常见语法错误，并排除 [SC2034](<https://www.shellcheck.net/wiki/SC2034>) 和 [SC2154](<https://www.shellcheck.net/wiki/SC2154>)：

    `shellcheck --shell=bash --exclude=SC2034,SC2154 PKGBUILD`

  * [termux-language-server](<https://aur.archlinux.org/packages/termux-language-server/>)AUR 为 `PKGBUILD` 和 `makepkg.conf` 等提供了一个[语言服务器](<../zh-cn/%E8%AF%AD%E8%A8%80%E6%9C%8D%E5%8A%A1%E5%99%A8%E5%8D%8F%E8%AE%AE.html> "语言服务器协议")。

##  软件包名称

### pkgbase

在构建常规的软件包时，不应该在 `PKGBUILD` 文件中显式定义该变量，这个值默认会与 [#pkgname](<#pkgname>) 的值相同。 

构建[拆分包](<https://man.archlinux.org/man/PKGBUILD.5#PACKAGE_SPLITTING>)时，这个变量可用于在 _makepkg_ 的输出和纯源代码包中指定软件包组。此变量不允许以下划线开头。若该变量没有明确定义，则会默认对应到 `pkgname` 数组的第一个元素。 

拆分软件包中的所有选项和指令都默认使用 `PKGBUILD` 中全局定义的值。以下选项可以在拆分包的打包函数中覆写：[#pkgdesc](<#pkgdesc>)、[#arch](<#arch>)、[#url](<#url>)、[#license](<#license>)、[#groups](<#groups>)、[#depends](<#depends>)、[#optdepends](<#optdepends>)、[#provides](<#provides>)、[#conflicts](<#conflicts>)、[#replaces](<#replaces>)、[#backup](<#backup>)、[#options](<#options>)、[#install](<#install>) 和 [#changelog](<#changelog>)。 

### pkgname

对于常规的软件包，这个变量设定软件包的名称，例如 `pkgname='foo'`。对于拆分包则是一个名称的序列，例如 `pkgname=('foo' 'bar')`。名称只能由由小写字母、数字和 `@ . _ + -` (at 符号、英文句点、下划线、加号、连字符)构成，且不能以连字符或英文句点开头。为了保证一致性，`pkgname` 应该与软件的源代码文件相匹配。比如：源文件包名为 `foobar-2.5.tar.gz`，那么应该使用 `pkgname=foobar`。 

##  版本

### pkgver

软件包的版本号，应该与软件上游发布的版本号一致。变量的值可以由字母、数字和英文句点 `.`，下划线 `_` 组成，但**不能** 包含连字符（`-`）。如果上游版本号中使用了连字符，则应该用下划线 `_` 来替代。在之后的 `PKGBUILD` 指令中`pkgver` 中的下划线可以用下面这个方法替换回连字符：`source=("${pkgname}-${pkgver//_/-}.tar.gz")`。 

**注意：** 如果上游使用时间戳格式的版本号，例如 `30102014`，请修改为年份在前的格式 `20141030`（[ISO 8601](<https://zh.wikipedia.org/wiki/ISO_8601> "zhwp:ISO 8601") 格式）。否则新版本可能无法被系统识别出来是新的。

**提示：**

  * 不常用变量的顺序可以通过 [pacman](<../zh-cn/Pacman.html> "Pacman") 软件包提供的 [vercmp(8)](<https://man.archlinux.org/man/vercmp.8>) 进行测试。
  * 在 `PKGBUILD` 中定义 `pkgver()` 函数，[makepkg](<../zh-cn/Makepkg.html> "Makepkg") 就可以自动[更新](<http://allanmcrae.com/2013/04/pacman-4-1-released/>)此变量。详情参阅 [VCS 软件打包准则#pkgver() 函数](<../zh-cn/VCS_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html#pkgver\(\)_%E5%87%BD%E6%95%B0> "VCS 软件打包准则")。

### pkgrel

软件的发布号。这通常是一个正整数，用来区分同一版本软件的多次构建。当软件包的补丁和附加功能被添加进入 `PKGBUILD`，从而导致生成的软件包发生变化时，`pkgrel` 应该增加 1。而当这个软件包发布一个新版本时，发布号重置为 1。在个别情况下，也会有其他的发布号形式。比如 _主版本号.次要版本号_ 。 

### epoch

**警告：** 除了特别、绝对、显式要求需要这样做，否则不允许使用 `epoch` 变量。

用于强制升级软件包。在判定逻辑中，不论版本号如何，只要 `epoch` 值较大，就会被视为更新的软件包。这个值应为非负整数，且默认值为 0。通常当一个软件的版本编号方式改变（或者使用某些字母-数字混编的版本符号），导致正常的版本比较逻辑无法进行时，会使用这个变量来控制升级。比如： 
    
    pkgver=5.13
    pkgrel=2
    epoch=1
    
    1:5.13-2

更多关于版本比较的信息，参见 [pacman(8)](<https://man.archlinux.org/man/pacman.8>)。 

##  一般变量

### pkgdesc

软件包描述。建议最多 80 个字符，并不要自引软件包的名字，除非软件包名和程序名不相同。比如：`pkgdesc='Nedit is a text editor for X11'` 应该被写成 `pkgdesc='Text editor for X11'`。 

合理地在描述中使用关键字，这样可以使软件包在相关的搜索中出现的可能性增加。 

### arch

一个描述能够生成并运行该软件包的架构的数组。Arch 官方仅支持 `x86_64`, 但是其它项目提供了其它架构支持。比如说，[Arch Linux 32](<https://archlinux32.org/>) 提供了 `i686` 和 `pentium4` 支持；[Arch Linux ARM](<https://archlinuxarm.org/>) 项目提供 `armv7h` (带有硬件浮点运算模块的 armv7）和 `aarch64` (64 位 armv8) 的支持。 

这个数组有两种形式： 

  * `arch=('any')` 表明软件包可以在任意架构上生成，并且一旦编译完成，编译时的架构就不再有影响了（例如 shell 脚本、字体、主题、各种扩展、[Java](<../zh-cn/Java.html> "Java") 程序等）。

  * `arch=(...)` 包含一个或更多架构（`any`除外），表明这个软件包可以在上述的任意架构上生成，但生成产物只能在编译它的架构上运行。对于这些软件包，您必须在 `PKGBUILD` 文件中指定所有官方支持的架构。对于官方软件源和 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 软件包，这指的是 `arch=('x86_64')`。不过，AUR 软件包可以选择添加一些已知的兼容架构的支持。

在生成过程中可以通过 `$CARCH` 变量来获知目标架构。 

### url

待打包软件官方站点的网址。 

### license

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[Arch 打包准则#授权协议](<../zh-cn/Arch_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html#%E6%8E%88%E6%9D%83%E5%8D%8F%E8%AE%AE> "Arch 打包准则")。**

**附注：** PKGBUILD 格式并没有强制执行某种打包标准。（在 [Talk:PKGBUILD](<../zh-cn/Talk:PKGBUILD.html>) 中讨论）

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 更多信息请参考 [[1]](<https://lists.archlinux.org/hyperkitty/list/arch-dev-public@lists.archlinux.org/thread/NFSB7734U2VVDULPRY65ECXDE3XGNZXM/>)。 (在 [Talk:PKGBUILD](<../zh-cn/Talk:PKGBUILD.html>) 中讨论)

软件分发所使用的许可证。Arch Linux 使用 [SPDX 许可证标识符](<https://zh.wikipedia.org/wiki/%E8%BD%AF%E4%BB%B6%E5%8C%85%E8%B5%84%E6%96%99%E4%BA%A4%E6%8D%A2%E8%A7%84%E8%8C%83#.E8.AE.B8.E5.8F.AF.E8.AF.81.E8.AF.AD.E6.B3.95> "zhwp:软件包资料交换规范")，所有许可证都需在 `/usr/share/licenses/` 下有对应项。 

[licenses](<https://archlinux.org/packages/?name=licenses>)包 包含了常见许可证（例如 `GPL-3.0-or-later`）的对应文件，默认已作为 [base](<https://archlinux.org/packages/?name=base>)包 [元软件包](<../zh-cn/%E5%85%83%E8%BD%AF%E4%BB%B6%E5%8C%85%E5%92%8C%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%BB%84.html> "元软件包")的依赖之一安装在 `/usr/share/licenses/spdx/` 目录下，使用时只需引用 [SPDX 标识符清单](<https://spdx.org/licenses/>)中的标识符。 

类似 BSD 或 MIT 的许可证族严格来说不是特定的单个许可证，每个实例都需要独立的许可证文件。对于这些许可证，需要在 `license` 中使用通用 SPDX 标识符（例如 `BSD-3-Clause` 或 `MIT`），并像自定义许可证一样提供对应的许可证文件。 

对于自定义许可证，如果其不属于常见许可证族，就需要使用 `LicenseRef-_license-name_` 或 `custom:_license-name_` 作为标识符。对应的许可证文件必须放置在 `/usr/share/licenses/_pkgname_` 目录下。可以在 `package()` 中使用如下代码安装许可证文件： 
    
    install -Dm644 _LICENSE_ "${pkgdir}/usr/share/licenses/${pkgname}/_LICENSE_ "
    
**注意：**`pkgdir` 变量由 _makepkg_ 定义，具体信息请参考 [PKGBUILD(5) § PACKAGING FUNCTIONS](<https://man.archlinux.org/man/PKGBUILD.5#PACKAGING_FUNCTIONS>)。

如果要结合多个许可证或添加例外，需要遵循 [SPDX 语法](<https://spdx.github.io/spdx-spec/v3.0/annexes/SPDX-license-expressions/>)。例如，如果软件包发布于 GNU/GPL 2.0 _或_ GNU/LGPL 2.1，需要使用 `'GPL-2.0-or-later OR LGPL-2.1-or-later'`；如果软件包发布于 Apache 2.0 并带有 LLVM 例外，需要使用 `'Apache-2.0 WITH LLVM-exception'`；如果软件包部分发布于 BSD 3 clause，其它部分发布于 GNU/LGPL 2，还有一部分发布于 GNU/GPL 2.0，就需要使用 `'BSD-3-Clause AND LGPL-2.1-or-later AND GPL-2.0-or-later'`[[2]](<https://gitlab.archlinux.org/archlinux/packaging/packages/musepack/-/blob/main/PKGBUILD?ref_type=heads#L13>)。注意，这需要是单个字符串，因此需要将整个表达式用引号括起来。截至 2023 年 11 月为止，[SPDX 例外列表](<https://spdx.org/licenses/preview/exceptions-index.html>)还非常有限，因此你通常还是需要遵循添加自定义许可证的方式。 

如果在 SPDX 标识符方面遇到问题，可以在过渡期间使用旧标识符（`/usr/share/licenses/common` 中的目录名称）。 

另请参考 [Nonfree applications package guidelines](</wzh/index.php?title=Nonfree_applications_package_guidelines&action=edit&redlink=1> "Nonfree applications package guidelines（页面不存在）")。 

有关自由和开放源码软件许可证的更多信息和观点，请参阅以下网页： 

  * [Wikipedia:Free software licence](<https://en.wikipedia.org/wiki/Free_software_licence> "wikipedia:Free software licence")
  * [zhwp:自由及开放源代码软件许可协议比较](<https://zh.wikipedia.org/wiki/%E8%87%AA%E7%94%B1%E5%8F%8A%E5%BC%80%E6%94%BE%E6%BA%90%E4%BB%A3%E7%A0%81%E8%BD%AF%E4%BB%B6%E8%AE%B8%E5%8F%AF%E5%8D%8F%E8%AE%AE%E6%AF%94%E8%BE%83> "zhwp:自由及开放源代码软件许可协议比较")
  * [开源和自由软件项目法律问题入门指南](<https://www.softwarefreedom.org/resources/2008/foss-primer.html>)
  * [GNU 项目 - 各类许可证及其评论](<https://www.gnu.org/licenses/license-list.html>)
  * [Debian - 许可证信息](<https://www.debian.org/legal/licenses/>)
  * [开放源代码促进会 - 许可证清单](<https://www.opensource.org/licenses/alphabetical>)

### groups

软件包所在的[软件包组](<../zh-cn/%E5%85%83%E8%BD%AF%E4%BB%B6%E5%8C%85%E5%92%8C%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%BB%84.html> "软件包组")。例如：当你安装 [plasma](<https://archlinux.org/groups/x86_64/plasma/>)包组，它会安装组里的所有包。 

##  依赖关系

**注意：** 架构相关的额外依赖可以通过在名称后添加下划线和架构的方式指定，例如 `optdepends_x86_64=()`。

### depends

为了生成**和** 运行软件，而必须安装的包列表。如果是只在运行时才依赖的包，请在 `package()` 函数中定义。 

可以使用比较运算符来描述版本限制。例如 `depends=('foobar>=1.8.0')`。如有多重限制，你可以添加多条，例如 `depends=('foobar>=1.8.0' 'foobar<2.0.0')`。 

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[Arch 打包准则](<../zh-cn/Arch_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "Arch 打包准则")。**

**附注：** PKGBUILD 格式并没有强制执行某种打包标准。（在 [Talk:PKGBUILD](<../zh-cn/Talk:PKGBUILD.html>) 中讨论）

`depends` 应该列出所有的直接依赖，即使已由某个依赖项间接引入时也应该如此。如果不这样做，那可能会发生以下情况：如果一个软件包 _foo_ 依赖 _bar_ 和 _baz_ 两个软件包，而 _bar_ 软件包也依赖于 _baz_ 软件包，当 **bar** 软件包不再依赖于 **baz** 就极有可能会导致意外行为——pacman 不会在安装 **foo** 软件包时安装 **baz** 软件包，也会在清除孤儿软件包时把 **baz** 清理掉。由于 **baz** 软件包被依赖却没有被安装，**foo** 可能崩溃或者发生运行错误。 

但在一些情况下，上面所述的某些依赖是没有必要或者不应该被列出的。比如说 [glibc](<https://archlinux.org/packages/?name=glibc>)包，每个操作系统都需要 C 运行库，因此它是不能够被卸载的。又比如，当软件包已经依赖于一个以 _python-_ 开头的模块，就不需要再单独依赖 [python](<https://archlinux.org/packages/?name=python>)包——因为 _python-_ 开头的模块必定依赖于 [python](<https://archlinux.org/packages/?name=python>)包 软件包，而且不允许从依赖列表中删除。 

通常的依赖应该包括生成所有可选功能所需的依赖。否则，对于任何依赖于额外软件包的可选功能，应显式通过配置选项将其禁用。如果不这样做，会给软件包添加了所谓“[自动魔法依赖](<https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Automagic_dependencies> "gentoo:Project:Quality Assurance/Automagic dependencies")”：一些生成时可选功能因为生成软件包的机器上安装的一些传递依赖或者不相关的软件被意外启用了，但是没有表现在包的依赖中。 

如果依赖的名称写成了库的名称（例如 `depends=('libfoobar.so')`）， _makepkg_ 会在编译完成的包中尝试寻找依赖这个库的二进制文件，并添加二进制文件所需的 [soname](<https://en.wikipedia.org/wiki/soname> "wikipedia:soname") 版本号到依赖列表中。可以自己加上版本号来停用自动检测，比如说 `depends=('libfoobar.so=2')`。 

### makedepends

仅在软件**生成** 时需要的软件包列表。可以像 `depends` 序列一样指定依赖的版本限制。`depends` 序列里面的软件包默认也是生成时需要的，此处不应该重复。 

**注意：**

  * 在使用 _makepkg_ 构建软件包时，默认 [base-devel](<https://archlinux.org/packages/?name=base-devel>)包 已安装。该包的依赖项**不应该** 出现在 `makedepends` 列表中。
  * 如果使用 [VCS 源](<../zh-cn/VCS_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html#VCS_%E6%BA%90> "VCS 软件打包准则")，记得要把对应的 VCS 工具（[git](<https://archlinux.org/packages/?name=git>)包，[subversion](<https://archlinux.org/packages/?name=subversion>)包，[cvs](<https://archlinux.org/packages/?name=cvs>)包 等等）加进去。

**提示：** 用以下命令查看某个依赖项是否已经被 [base-devel](<https://archlinux.org/packages/?name=base-devel>)包 直接依赖：`pactree -rsud1 _package_ | grep base-devel`（需要安装 [pacman-contrib](<https://archlinux.org/packages/?name=pacman-contrib>)包）。

### checkdepends

运行软件的测试组件时需要，而运行时不需要的包列表。该列表中的包遵循 `depends` 相同的格式。这些依赖只在 [check()](<../zh-cn/%E5%88%9B%E5%BB%BA%E8%BD%AF%E4%BB%B6%E5%8C%85.html#check\(\)> "创建软件包") 函数存在，且被 _makepkg_ 执行时会被处理。 

**注意：** 在使用 _makepkg_ 构建软件包时，默认 [base-devel](<https://archlinux.org/packages/?name=base-devel>)包 已安装。该包的依赖项**不应该** 出现在 `checkdepends` 列表中。

### optdepends

可选软件包序列。这些可选软件包不影响软件主要功能，但能提供额外特性。这通常意味着除非安装了对应的可选软件包，该软件包所提供的个别可执行文件可能无法正常使用[[3]](<https://lists.archlinux.org/archives/list/arch-general@lists.archlinux.org/message/ZFBCD2NFFBSOZBI22AYZYHH2PDRCLJWF/>)。如果软件有一些替代依赖，您可以将其在此处全部列出，而不是 `depends` 列表中列出。 

应该简要说明每个包所能提供的额外功能，例如： 
    
    optdepends=('cups: printing support'
                'sane: scanners support'
                'libgphoto2: digital cameras support'
                'alsa-lib: sound support'
                'giflib: GIF images support'
                'libjpeg: JPEG images support'
                'libpng: PNG images support')
    
##  包关系

**注意：** 架构相关的附加列表可以通过在变量名称后添加下划线和架构名字的方式指定，例如 `conflicts_x86_64=()`。

### provides

该列表说明的是本软件包能够提供列表中的包（或者像 _cron_ 、 _sh_ 这样的[虚包](<../zh-cn/Pacman.html#%E8%99%9A%E5%8C%85> "Pacman")和[所有外部共享库](<../zh-cn/Arch_%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html#%E8%BD%AF%E4%BB%B6%E5%8C%85%E5%85%B3%E8%81%94> "Arch 打包准则")）所提供的功能。只要 `provides` 列表中的包都没有声明 `conflicts`，提供相同功能的软件包就可以同时安装。 

**注意：**

  * 该变量中的软件包应当加上版本号（`pkgver`，可能的话还有`pkgrel`），特别是当依赖该软件包的其他软件对版本号特别敏感的时候。就是说，如果一个修改过的 _qt_ 包其版本号为 3.3.8，命名为 _qt-foobar_ ，那么 `provides` 应该写成 `provides=('qt=3.3.8')`。如果忽略了版本号，会导致所有依赖于 _qt_ 的某个特定版本的包编译失败。
  * 不要把 `pkgname` 加入 `provides` 序列。这个操作会自动进行。

### conflicts

这个列表描述的是与当前软件包冲突的包，或者与该包同时存在会产生问题的包。安装此软件时，这个列表中的所有软件包和提供这个功能的软件包都会被删除。可以像 `depends` 那样指定冲突包的版本号。 

需要注意的是，冲突检查的对象是 `pkgname` 以及 `provides` 中的名字。因此，如果你的包 `provides` `_foo_` 功能，在 `conflicts` 中指定 `_foo_` 就会导致你的包和所有其他在 `provides` 中包含了 `_foo_` 的包冲突（也就是说，你不需要一个一个地指定所有冲突的包的名字）。例子是： 

  * [netbeans](<https://archlinux.org/packages/?name=netbeans>)包 提供 `netbeans`（因为 `pkgname` 就是如此）。
  * [netbeans-cpp](<https://aur.archlinux.org/packages/netbeans-cpp/>)AUR 提供 `netbeans` 功能，并和 `netbeans` 冲突。
  * [netbeans-php](<https://aur.archlinux.org/packages/netbeans-php/>)AUR 提供 `netbeans` 功能，而且和 `netbeans` 冲突，但是不需要再说明它与 [netbeans-cpp](<https://aur.archlinux.org/packages/netbeans-cpp/>)AUR 冲突，因为提供相同功能的包隐含了冲突关系。

当不同的包通过在 `provides` 列表中声明的方式提供相同的功能，那么是否特意在 `conflicts` 列表中添加可替换的包会产生不同的结果。特意说明的话，两个包就会被认为是可相互替代的；如果 `conflicts` 列表不存在，那么两个包会被认为是“可能可以同时存在”。在决定是否需要声明 `conflicts` 列表的时候，请忽略 `provides` 列表的内容，独立决策。 

### replaces

会因安装当前包而取代的过时的包的列表。比如：[wireshark-qt](<https://archlinux.org/packages/?name=wireshark-qt>)包 中的 `replaces=('wireshark')`。在**同步** 软件数据库后， _pacman_ 会立刻用软件库中的另一个包替换掉 `replaces` 中已安装的包。如果你只是提供已存在包的一个替代品，或者上传到 AUR, 请不要使用 `replace`，而是使用 `conflicts` 和 `provides` 两个变量——它们仅在安装冲突软件包时被检查。 

##  其它

### backup

当包被升级或卸载时，应当保留的文件（的路径）序列。这些文件一般是用户会更改的文件，如主要放置在 `/etc` 中的配置文件。如果在安装软件包后这些文件没有被修改过，那么它们会随升级和移除软件包时一同被替换或删除。 

列表中的文件应该使用**相对** 路径，即不是以斜杠（`/`）开头的路径（如 `etc/pacman.conf` 而不是 `/etc/pacman.conf`）。`backup` 数组[不支持空目录和类似“*”的通配符](<https://bbs.archlinux.org/viewtopic.php?pid=2187778>)。 

在升级时，新版本会被命名为 `_file_.pacnew` 以避免覆盖原来的被用户修改过的文件。当卸载包时，用户修改过的文件会以 `_file_.pacsave` 为名而保留下来——除非用 `pacman -Rn` 命令卸载。 

参见 [pacnew 和 pacsave 文件](<../zh-cn/Pacman/pacnew_%E4%B8%8E_pacsave.html> "Pacman/pacnew 与 pacsave")获取更多信息。 

### options

参见 [PKGBUILD(5) § OPTIONS AND DIRECTIVES](<https://man.archlinux.org/man/PKGBUILD.5#OPTIONS_AND_DIRECTIVES>) 以获取所有可用选项。 

### install

需要包含在包中的 _.install_ 脚本的名称。 

_pacman_ 可以在安装、卸载或升级一个软件包时存储及执行一些特定的脚本。脚本包含了下面几个函数，并且在特定时刻执行它们： 

  * `pre_install` \- 提取包中文件前运行的脚本。会传递一个参数：新版本号。
  * `post_install` \- 提取包中文件后运行的脚本。安装软件包后输出的提示信息需放置于该函数内。会传递一个参数：新版本号。
  * `pre_upgrade` \- 提取包中文件前运行的脚本。两个参数会按以下顺序传递：新版本号，旧版本号。
  * `post_upgrade` \- 提取包中文件后运行的脚本。两个参数会按以下顺序传递：新版本号，旧版本号。
  * `pre_remove` \- 文件被删除前运行的脚本，会传递一个参数：旧版本号。
  * `post_remove` \- 文件被删除后运行的脚本，会传递一个参数：旧版本号。

每一个函数都是 [chroot](<../zh-cn/Chroot.html> "Chroot") 到 _pacman_ 安装目录下运行的。参见[这个帖子](<https://bbs.archlinux.org/viewtopic.php?pid=913891>). 

**提示：**

  * 可以在 [/usr/share/pacman/proto.install 这里](<https://gitlab.archlinux.org/pacman/pacman/raw/master/proto/proto.install>)找到一个 `.install` 文件的模板（原型）。
  * [Pacman 钩子](<../zh-cn/Pacman.html#%E9%92%A9%E5%AD%90> "Pacman")也提供相似的功能。

**注意：** 脚本不要以 `exit` 结束，否则包含该脚本的函数无法执行。

### changelog

软件包的更新日志的文件名。要查看安装软件的更新日志（如果有）： 
    
    $ pacman -Qc _pkgname_
    
##  源码

### source

构建软件包时需要的文件列表。它必须包含软件源的位置，大多数情况下是一个完整的 HTTP 或 FTP 地址。您可以在此处调用前面提到的变量 `pkgname` 和 `pkgver`，来实现高效的命名（如 `source=("https://example.com/${pkgname}-${pkgver}.tar.gz")`）。 

文件也可以放到与 `PKGBUILD` 文件相同目录，并将文件名添加到这个列表。在实际的编译过程开始之前，所有该列表中引用的文件都会被下载或检查是否存在，如果有文件丢失 _makepkg_ 就不会继续。 

_.install_ 文件会被 _makepkg_ 自动识别，而不应该被包含在这个列表中。 _makepkg_ 会自动把 `source` 中 _.sig_ ， _.sign_ 或 _.asc_ 结尾的文件当成 PGP 签名，并自动验证对应的源文件的完整性。 

**警告：** 因为所有包的 [SRCDEST](<../zh-cn/Makepkg.html#%E5%8C%85%E8%BE%93%E5%87%BA> "Makepkg") 的值可能相同，所以下载的文件的文件名需要唯一。比如说，如果一个项目只用版本号来命名，可能会与其他有相同版本号的不同项目冲突。在这种情况下，你可以为下载的文件指定不同的文件名：`source=('_unique_package_name_**::**_file_uri_ ')`。例如 `source=("${pkgname}-${pkgver}.tar.gz::https://github.com/coder/program/archive/v${pkgver}.tar.gz")`。 

**注意：**

  * 架构相关的文件可以通过在名称后添加下划线和架构的方式指定，例如 `source_x86_64=()`。必须提供对应的完整性校验和序列，例如 `sha256sums_x86_64=()`。
  * 有些服务器通过 _User-Agent_ 或其它方式来筛选并限制下载。这个限制可以通过 [DLAGENTS](</wzh/index.php?title=Nonfree_applications_package_guidelines&action=edit&redlink=1> "Nonfree applications package guidelines（页面不存在）") 规避。
  * 可以使用 `file://` URL 来指向本地目录或文件，例如指定本地 Git 仓库：`"${pkgname}::git+file://_/path/to/repository_ "`。
  * Magnet link support can be added using [transmission-dlagent](<https://aur.archlinux.org/packages/transmission-dlagent/>)AUR as `DLAGENT` and using the `magnet://` URI prefix instead of the canonical `magnet:?`.
  * See [PKGBUILD(5) § USING VCS SOURCES](<https://man.archlinux.org/man/PKGBUILD.5#USING_VCS_SOURCES>) and [VCS 软件打包准则#VCS 源代码](<../zh-cn/VCS_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html#VCS_%E6%BA%90%E4%BB%A3%E7%A0%81> "VCS 软件打包准则") for details on VCS specific options, such as targeting a specific Git branch or commit.

### noextract

一个在 `source` 中列出，但不应该由 [makepkg](<../zh-cn/Makepkg.html> "Makepkg") 解包的文件列表。这通常包括那些不能被 `/usr/bin/bsdtar` 处理的压缩文件，或者本来就不需要解压、按照原样提供的文件。对于前者，需要将额外的解包工具（如 `unzip`，`p7zip`，[lrzip](<https://archlinux.org/packages/?name=lrzip>)包 等）加入 `makedepends` 序列，且 [prepare()](<../zh-cn/%E5%88%9B%E5%BB%BA%E8%BD%AF%E4%BB%B6%E5%8C%85.html#prepare\(\)> "创建软件包") 函数的第一行需进行手动解压。例如： 
    
    prepare() {
      lrzip -d _source_.tar.lrz
    }
    
注意当 `source` 是一些 URL 时，`noextract` **仅仅** 取文件名部分： 
    
    source=("http://foo.org/bar/foobar.tar.xz")
    noextract=('foobar.tar.xz')
    
不提取任何东西时，可以像这样： 

  * 如果 `source` 只包含了纯 URL，而没有自定义的文件名时，将内容从最后一个斜杠之前像这样从 `source` 序列中提出来：

    noextract=("${source[@]##*/}")

  * 如果 `source` 只包含了带自定义文件名的项，将内容从分隔符 `::` 之前像这样从 `source` 序列中提出来（这是从旧版 [firefox-i18n 的 PKGBUILD 中找到的](<https://gitlab.archlinux.org/archlinux/packaging/packages/firefox-i18n/-/blob/46492498ef720353cbb84de5096102de694faf90/PKGBUILD#L132>)）：

    noextract=("${source[@]%%::*}")

### validpgpkeys

PGP 指纹列表。如果使用， _makepkg_ 仅接受这里定义的签名，并且忽略密钥环中的值。如果源代码用子密钥签名， _makepkg_ 仍然会使用主密钥进行比较。 

此处仅接受完整的指纹。它们必须是大写字母而且不能有空白字符。 

**注意：** 可以使用 `gpg --list-keys --fingerprint _KEYID_` 查找密钥的指纹。

请参阅 [makepkg#验证签名](<../zh-cn/Makepkg.html#%E9%AA%8C%E8%AF%81%E7%AD%BE%E5%90%8D> "Makepkg")了解签名验证过程的详细信息。 

##  完整性检验

下面描述的这些序列中的变量是 [source](<#source>) 序列中对应文件的校验和。可以插入 `SKIP` 跳过某个不需要检验的文件。 

校验和的类型和数值应该始终使用上游提供的数值（比如在新版本公告中的）。当存在多种类型的时候，最好选用最强的校验类型。类型按照从强到弱的顺序如下：`b2` > `sha512` > `sha384` > `sha256` > `sha224` > `sha1` > `md5` > `ck`，这样可以最大限度地保证从上游的公告到软件包的生成整个流程中下载文件的完整性。 

**注意：** 另外，当上游具备[数字签名](<https://zh.wikipedia.org/wiki/%E6%95%B0%E5%AD%97%E7%AD%BE%E5%90%8D> "zhwp:数字签名")文件时，这个签名文件应该被添加到 [source](<#source>) 序列中，PGP 密钥添加到 [validpgpkeys](<#validpgpkeys>) 序列中。这样允许在生成软件包时进行验证。

[makepkg](<../zh-cn/Makepkg.html> "Makepkg") 的 `-g`/`--geninteg` 选项可以自动生成校验值，通常可以通过 `makepkg -g >> PKGBUILD` 命令写入。[pacman-contrib](<https://archlinux.org/packages/?name=pacman-contrib>)包 提供的 [updpkgsums(8)](<https://man.archlinux.org/man/updpkgsums.8>) 命令也可以更新 `PKGBUILD` 中的变量。两个工具都会自动检测 PKGBUILD 中的算法, 如果没找到就回滚到 `md5sums`。 

The file integrity checks to use can be set up with the `INTEGRITY_CHECK` option in `/etc/makepkg.conf`. See [makepkg.conf(5)](<https://man.archlinux.org/man/makepkg.conf.5>). 

**注意：** 架构相关的额外完整性检验可以通过在名称后添加下划线和架构的方式指定，例如 `sha256sums_x86_64=()`。

### b2sums

[BLAKE2](<https://zh.wikipedia.org/wiki/BLAKE#BLAKE2> "zhwp:BLAKE") 校验和数组，大小为 512 位。 

###  sha512sums，sha384sums，sha256sums，sha224sums

[SHA-2](<https://zh.wikipedia.org/wiki/SHA-2> "zhwp:SHA-2") 校验和数组，大小分别为 512，384，256 和 224 位。最常见的是 `sha256sums`。 

### sha1sums

`source` 数组中文件的 160 位 [SHA-1](<https://zh.wikipedia.org/wiki/SHA-1> "zhwp:SHA-1") 校验和数组。 

### md5sums

`source` 数组中文件的 128 位 [MD5](<https://zh.wikipedia.org/wiki/MD5> "zhwp:MD5") 校验和数组。 

### cksums

`source` 数组中文件的 [CRC32](<https://zh.wikipedia.org/wiki/%E5%BE%AA%E7%8E%AF%E5%86%97%E4%BD%99%E6%A0%A1%E9%AA%8C> "zhwp:循环冗余校验")（使用 UNIX 标准的 [cksum](<https://zh.wikipedia.org/wiki/cksum> "zhwp:cksum")）校验和数组。 
