相关文章

  * [.SRCINFO](<../zh-cn/.SRCINFO.html> ".SRCINFO")
  * [Arch 构建系统](<../zh-cn/Arch_%E6%9E%84%E5%BB%BA%E7%B3%BB%E7%BB%9F.html> "Arch 构建系统")
  * [Arch 用户软件仓库 (AUR)](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93_\(AUR\).html> "Arch 用户软件仓库 \(AUR\)")
  * [创建软件包](<../zh-cn/%E5%88%9B%E5%BB%BA%E8%BD%AF%E4%BB%B6%E5%8C%85.html> "创建软件包")
  * [GnuPG](<../zh-cn/GnuPG.html> "GnuPG")
  * [官方仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方仓库")
  * [OpenPGP](</wzh/index.php?title=OpenPGP&action=edit&redlink=1> "OpenPGP（页面不存在）")
  * [pacman](<../zh-cn/Pacman.html> "Pacman")
  * [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD")

**翻译状态：**

  * 本文（或部分内容）译自 [makepkg](<https://wiki.archlinux.org/title/makepkg> "arch:makepkg")，最近一次同步于 2026-01-21，若英文版本有所[更改](<https://wiki.archlinux.org/title/makepkg?diff=0&oldid=861950>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/makepkg_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[makepkg](<https://gitlab.archlinux.org/pacman/pacman/blob/master/scripts/makepkg.sh.in>) 是一个软件包自动化构建脚本，使用时需要一个具备构建条件的 [Unix](<https://en.wikipedia.org/wiki/Unix> "wikipedia:Unix") 环境和一个 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 文件。 

_makepkg_ 是由 [pacman](<https://archlinux.org/packages/?name=pacman>)包 包提供的。 

##  配置

全局配置位于 `/etc/makepkg.conf`，还可以通过 `$XDG_CONFIG_HOME/pacman/makepkg.conf` 或 `~/.makepkg.conf` 进行用户特定配置。你还可以添加 `/etc/makepkg.conf.d/makepkg.conf` 文件进行系统全局配置更改。在构建软件包前，建议先检查 makepkg 配置。 

**提示：**[devtools](<https://archlinux.org/packages/?name=devtools>)包 用于[从干净的 chroot 构建软件包](<https://wiki.archlinux.org/title/DeveloperWiki:Building_in_a_clean_chroot>)的助手脚本会使用 `/usr/share/devtools/makepkg.conf.d/_arch_.conf` 配置文件。

更多信息请参考 [makepkg.conf(5)](<https://man.archlinux.org/man/makepkg.conf.5>)。 

###  打包人信息

每个软件包都会有元数据信息，其中就包含 _packager_ 。默认情况下，用户自己打包的软件标记为 `Unknown Packager`。如果多个用户会在系统上编译，或者需要发布软件包给其他人，最好提供真实的联系人。打包人信息可以通过 `makepkg.conf` 中的 `PACKAGER` 变量进行设置。 

要检查已安装软件包的打包人： 
    
    $ pacman -Qi _package_
    
    ...
    Packager       : John Doe <john@doe.com>
    ...
    
要自动化签名过程，请同时在 `makepkg.conf` 中设置 `GPGKEY` 变量. 

###  包输出

_makepkg_ 默认会在工作目录创建软件包，并把源代码下载到 `src/` 目录。可以配置到自定义的路径，比如将所有构建出的软件包放到 `~/build/packages/` 目录，所有源文件放到 `~/build/sources/` 目录下。 

根据需求不同，可以配置 `makepkg.conf` 下的这些变量： 

  * `PKGDEST` \- 软件包构建输出目录
  * `SRCDEST` \- 用于存放[源数据](<../zh-cn/PKGBUILD.html#source> "PKGBUILD")的目录（在指向其它位置的情况下，软链接将被放置到 `src/` 目录下）
  * `SRCPKGDEST` \- 源代码包构建输出目录（通过 `makepkg -S` 构建）

**提示：** 可以参考 [pacman#清理软件包缓存](<../zh-cn/Pacman.html#%E6%B8%85%E7%90%86%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%BC%93%E5%AD%98> "Pacman") 用命令（例如 `paccache -c ~/build/packages/`）清理 `PKGDEST` 目录

你还可以[#在包目录下使用相对路径](<#%E5%9C%A8%E5%8C%85%E7%9B%AE%E5%BD%95%E4%B8%8B%E4%BD%BF%E7%94%A8%E7%9B%B8%E5%AF%B9%E8%B7%AF%E5%BE%84>)。 

###  验证签名

**注意：** _makepkg_ 中的签名验证并不使用 pacman 的密钥环, 而是使用用户的密钥[[1]](<http://allanmcrae.com/2015/01/two-pgp-keyrings-for-package-management-in-arch-linux/>)。

如果签名文件是以 _.sig_ 或 _.asc_ 形式作为 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 源码数组的一部分提供， _makepkg_ 会自动[验证](<../zh-cn/GnuPG.html#%E9%AA%8C%E8%AF%81%E7%AD%BE%E5%90%8D> "GnuPG")软件包。如果用户未提供需要的签名公钥， _makepkg_ 会停止安装过程并提示用户说无法验证 PGP 密钥。 

如果缺少软件包所需的公钥，那么 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 很可能带有 [validpgpkeys](<../zh-cn/PKGBUILD.html#validpgpkeys> "PKGBUILD") 项，其中包含了所需的密钥 ID。你可以[手动进行导入](<../zh-cn/GnuPG.html#%E5%AF%BC%E5%85%A5%E5%85%AC%E5%85%B1%E5%AF%86%E9%92%A5> "GnuPG")，也可以在[在公钥服务器上](<../zh-cn/GnuPG.html#%E4%BD%BF%E7%94%A8%E5%85%AC%E9%92%A5%E6%9C%8D%E5%8A%A1%E5%99%A8> "GnuPG")进行查找，然后导入。运行 _makepkg_ 时使用 `--skippgpcheck` 选项可以临时禁用签名检查。 

##  使用

继续之前，确保已[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")了 [base-devel](<https://archlinux.org/groups/x86_64/base-devel/>)包组 [软件包组](<../zh-cn/%E5%85%83%E8%BD%AF%E4%BB%B6%E5%8C%85%E5%92%8C%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%BB%84.html> "软件包组")。属于这个组的软件包**不会** 被要求列在 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 文件的构建时依赖（ _makedepends_ ）中。 

**注意：**

  * 确保为传入 [pacman](<../zh-cn/Pacman.html> "Pacman") 的命令正确配置了 [sudo](<../zh-cn/Sudo.html> "Sudo")。另外，可以通过 [makepkg.conf(5)](<https://man.archlinux.org/man/makepkg.conf.5>) 配置文件的 `PACMAN_AUTH` 参数指定不同的认证命令。
  * [不允许](<https://lists.archlinux.org/archives/list/pacman-dev@lists.archlinux.org/message/ZLRXMUGXULDHLTGSRYVGVWG3BVATV3OY/>)以根用户（root）身份运行 `makepkg`。[[2]](<https://gitlab.archlinux.org/pacman/pacman/blob/master/NEWS>) 原因除了 `PKGBUILD` 可能包含恶意代码外，以 root 身份构建软件一般都被认为是不安全的。[[3]](<https://bbs.archlinux.org/viewtopic.php?id=67561>) 无法使用普通用户时需以 [nobody 用户](<http://allanmcrae.com/2015/01/replacing-makepkg-asroot/>)的身份运行 `makepkg`（例如 `runuser -u nobody makepkg`）。

要构建软件包，用户必须首先创建一个 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 文件或编译脚本（在[创建软件包](<../zh-cn/%E5%88%9B%E5%BB%BA%E8%BD%AF%E4%BB%B6%E5%8C%85.html> "创建软件包")中有详细描述），或者从 [Arch 构建系统](<../zh-cn/Arch_%E6%9E%84%E5%BB%BA%E7%B3%BB%E7%BB%9F.html> "Arch 构建系统") _（ABS）_ 、[AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 或其他来源获取。获取到 `PKGBUILD` 后，切换到该文件所在文件夹中，然后执行以下命令构建软件包： 
    
    $ makepkg
    
如果需要的依赖不满足， _makepkg_ 会输出一个警告然后失败。想要编译软件包并自动安装必须的依赖，只需添加 `-s`/`--syncdeps` 参数： 
    
    $ makepkg --syncdeps
    
如果添加了 `-r`/`--rmdeps` 选项， _makepkg_ 会在结束后删除不再需要的编译依赖。如果需要持续编译软件包，请考虑定期[删除未使用软件包](<../zh-cn/Pacman/%E6%8F%90%E7%A4%BA%E5%92%8C%E6%8A%80%E5%B7%A7.html#%E5%88%A0%E9%99%A4%E6%9C%AA%E4%BD%BF%E7%94%A8%E7%9A%84%E8%BD%AF%E4%BB%B6%E5%8C%85%EF%BC%88%E5%AD%A4%E7%AB%8B%E8%BD%AF%E4%BB%B6%E5%8C%85%EF%BC%89> "Pacman/提示和技巧")。 

**注意：**

  * 这些依赖必须在已配置的软件源之中存在，具体信息请参考 [pacman#软件仓库](<../zh-cn/Pacman.html#%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93> "Pacman")。另外，用户也可以在编译前手动安装需要的依赖：(`pacman -S --asdeps _dep1_ _dep2_`)。
  * 在安装依赖包时，只使用全局值，即不会使用拆分包打包功能中的任何覆盖值。

在满足所有依赖并成功编译软件包后，一个软件包文件（` _pkgname_ -_pkgver_.pkg.tar.zst`）将会被创建在工作目录下。如需安装，请使用 `-i`/`--install` 参数（与 `pacman -U _pkgname_ -_pkgver_.pkg.tar.zst` 相同）： 
    
    $ makepkg --install
    
要清理残余的文件和目录（如解压到 `$srcdir` 的文件），请使用 `-c`/`--clean` 选项。这对于在使用同一个文件夹多次编译同一个软件包或者升级软件包版本时很有用。它可以防止过期或残余的文件被呈递到新的构建任务中： 
    
    $ makepkg --clean
    
更多信息请阅读 [makepkg(8)](<https://man.archlinux.org/man/makepkg.8>)。 

##  优化

默认选项与 [devtools](<https://archlinux.org/packages/?name=devtools>)包 为[官方仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方仓库")构建软件包使用的选项一致[[4]](<https://gitlab.archlinux.org/archlinux/packaging/packages/pacman/-/issues/23#note_173678>)。因此，用户可以通过调整以下选项来适应本地环境，以获得或多或少的收益。 

###  优化编译结果

通过启用针对主机的编译器优化，可以提高打包后软件的性能。缺点是，为特定处理器架构编译的二进制文件无法在其他机器上正常运行。在 x86_64 机器上，重新构建官方软件包通常不会有显著的性能提升，因此不值得为此投入时间。 

不过，使用 “非标准” 编译器标志很容易降低性能。许多编译器优化仅在某些情况下有用，不应对软件包随意应用。除非有评测数据证明某项优化更快，否则很有可能会导致性能下降！Gentoo 的 [GCC 优化](<https://wiki.gentoo.org/wiki/GCC_optimization>)和[安全的 CFLAGS](<https://wiki.gentoo.org/wiki/Safe_CFLAGS>) 文章提供了有关编译器优化的更多信息。 

####  C 和 C++

传递到 C/C++ 编译器（例如 [gcc](<https://archlinux.org/packages/?name=gcc>)包 或 [clang](<https://archlinux.org/packages/?name=clang>)包）的选项是通过 `CFLAGS`、`CXXFLAGS` 和 `CPPFLAGS` [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")传入的。在使用 Arch 构建系统时， _makepkg_ 会将 `makepkg.conf` 中的配置项作为这些环境变量进行传递。默认值会生成通用的二进制文件，可安装在各种机器上。 

**注意：**

  * 记住，不是所有的构建系统都会使用 `makepkg.conf` 中设置的变量。例如， _cmake_ 不会遵循 `CPPFLAGS` 预处理器选项环境变量。因此，很多 [PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 都包含了针对打包软件所使用的构建系统而设置的选项。
  * 源码提供的 `Makefile` 或编译命令行中指定的参数优先级更高，并有可能会取代掉 `makepkg.conf` 中的配置。

GCC 可以自动检测架构，并应用安全的架构特定优化项。要使用该特性，首先需要移除所有 `-march` 和 `-mtune` 标志，然后添加 `-march=native`，例如： 
    
    /etc/makepkg.conf
    
    CFLAGS="**-march=native** -O2 -pipe ..."
    CXXFLAGS="${CFLAGS} ..."

要查看该操作会启用的选项，执行： 
    
    $ gcc -march=native -v -Q --help=target
    
**注意：** 如果没有指定 `-march=native`，`-Q --help=target` 将**不会** 起作用[[5]](<https://bbs.archlinux.org/viewtopic.php?pid=1616694#p1616694>)。具体启用的选项需要编译后才能知道。详细步骤请参考[[6]](<https://wiki.gentoo.org/wiki/Safe_CFLAGS>)。

进一步优化需要启用对内存占用和编译时间有较大负面影响的选项，做法为将优化级别从 `-O2` 设为 `-O3`。使用该选项一般都能提升二进制文件的性能，但具体效果取决于文件本身。更多信息请参考 [Gentoo:GCC optimization#-O](<https://wiki.gentoo.org/wiki/GCC_optimization#-O> "gentoo:GCC optimization") 和 [GCC 优化选项页](<https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html#Options-That-Control-Optimization>)。 

#### Rust

从 `pacman` 5.2.2 开始，`makepkg.conf` 还包含了对 `RUSTFLAGS` 环境变量的覆写，用于替换 Rust 编译器的标志。通过在 `RUSTFLAGS` 中添加 `-C target-cpu=native`，Rust 编译器还能检测并应用架构特定优化项： 
    
    /etc/makepkg.conf.d/rust.conf
    
    RUSTFLAGS="-C force-frame-pointers=yes **-C target-cpu=native** "

查看该操作会已启用的 CPU 特性： 
    
    $ rustc -C target-cpu=native --print cfg
    
在不包含 `-C target-cpu=native` 的情况下运行 `--print cfg` 将输出默认配置。 

下面为一些可以添加到 `RUSTFLAGS` 的优化参数： 

  * `-C opt-level=3`：可以根据需要将该值更改为 `3`、`s` 或 `z`。针对分发的构建默认使用 `opt-level=3`。
  * `-C codegen-units=_n_`：选择小于 `16` 的 `_n_` 值可以优化二进制文件，但会增加构建耗时。
  * `-C link-arg=-z -C link-arg=pack-relative-relocs` 可以降低二进制文件的大小。

更多信息请参考 [Rust 编译器文档](<https://doc.rust-lang.org/rustc/codegen-options/index.html>)。 

###  减少编译时间

####  并行编译

[make](<https://archlinux.org/packages/?name=make>)包 编译系统使用 `MAKEFLAGS` [环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")指定 _make_ 的额外选项。这个值也可以在 `makepkg.conf` 文件中进行设置。 

使用多核/多处理器系统的用户可以设定同时运行的任务数。可以用 [nproc(1)](<https://man.archlinux.org/man/nproc.1>) 获得可用处理器的个数，例如：`MAKEFLAGS="--jobs=$(nproc)"`。 

有些 `PKGBUILD` 会强制使用 `-j1`，因为某些版本会产生冲突或者软件包本身并不支持。如果出现软件包因为此原因无法编译，请在确认错误是由 `MAKEFLAGS` 引起的前提下，在 bug 跟踪系统中进行[报告](<../zh-cn/%E6%BC%8F%E6%B4%9E%E6%8A%A5%E5%91%8A%E5%87%86%E5%88%99.html> "漏洞报告准则")（如果是 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 包，则向包维护者报告）。 

完整可用选项请参考 [make(1)](<https://man.archlinux.org/man/make.1>)。 

####  使用内存文件系统进行编译

编译过程需要大量的读写操作，要处理很多小文件。将工作目录移动到 [tmpfs](<../zh-cn/Tmpfs.html> "Tmpfs") 可能会减少编译时间。 

使用 `BUILDDIR` 变量可以临时将 _makepkg_ 的编译目录设置到现有 tmpfs，例如： 
    
    $ BUILDDIR=/tmp/makepkg makepkg
    
将 `makepkg.conf` 中的 `BUILDDIR` 选项取消注释可以永久变更编译目录，具体位于 `/etc/makepkg.conf` 文件末尾的 `BUILD ENVIRONMENT` 一节。设置此变量为 `BUILDDIR=/tmp/makepkg` 可以利用 Arch 默认的 `/tmp` 临时文件系统。 

**注意：**

  * 在 [tmpfs](<../zh-cn/Tmpfs.html> "Tmpfs") 中构建大型软件包时可能会内存不足。
  * 挂载 [tmpfs](<../zh-cn/Tmpfs.html> "Tmpfs") 目录时不能使用 `noexec` 选项，否则编译命令无法执行。
  * 在 [tmpfs](<../zh-cn/Tmpfs.html> "Tmpfs") 中构建好的包重启后会消失，设置 [PKGDEST](<#%E5%8C%85%E8%BE%93%E5%87%BA>) 选项可以将构建结果保存到其它目录。

####  使用编译缓存

[ccache](<../zh-cn/Ccache.html> "Ccache") 可以将编译结果缓存起来供下次编译使用，减少编译时间。 

####  使用 mold 链接器

[mold](<https://archlinux.org/packages/?name=mold>)包 是 [ld](<../zh-cn/GNU_Compiler_Collection.html> "GCC")/[lld](<../zh-cn/LLVM.html> "LLVM") 链接器的直接替代，据称其速度稍微较快。 

要使用 _mold_ ，需添加 `-fuse-ld=mold` 到 `LDFLAGS`，例如： 
    
    /etc/makepkg.conf
    
    LDFLAGS="... -fuse-ld=mold"

要向 _mold_ 添加额外选项，可以将它们添加到 `LDFLAGS` 中，例如： 
    
    /etc/makepkg.conf
    
    LDFLAGS="... -fuse-ld=mold -Wl,--separate-debug-file"

要为 Rust 软件包使用 _mold_ ，可以将 `-C link-arg=-fuse-ld=mold` 添加到 `RUSTFLAGS` 中，例如： 
    
    /etc/makepkg.conf.d/rust.conf
    
    RUSTFLAGS="... -C link-arg=-fuse-ld=mold"

####  禁用调试包和 LTO

包含在 [2024 年 2 月 pacman 6.0.2-9 版本](<https://gitlab.archlinux.org/archlinux/packaging/packages/pacman/-/blob/6.0.2-9/makepkg.conf?ref_type=tags>)的 [90bf367e 号提交](<https://gitlab.archlinux.org/archlinux/packaging/packages/pacman/-/commit/90bf367e61b4f77f8351d0412be3d0c4ddadb85a>)默认启用了 `debug` 和 `lto` 选项。 

构建调试包能让官方仓库为用户提供更多的问题排查工具（[archlinux/packaging/packages/pacman#23#note_173528](<https://gitlab.archlinux.org/archlinux/packaging/packages/pacman/-/issues/23#note_173528>)），但在自行构建软件包时，调试包不是必需的，而且会减慢构建进程。参见 [archlinux/packaging/packages/pacman#23#note_173782](<https://gitlab.archlinux.org/archlinux/packaging/packages/pacman/-/issues/23#note_173782>)。 

[链接时优化](<https://en.wikipedia.org/wiki/Link-time_optimization> "wikipedia:Link-time optimization")可以生成更优化的二进制文件，但会增加构建耗时（[archlinux/packaging/packages/pacman#23#note_173678](<https://gitlab.archlinux.org/archlinux/packaging/packages/pacman/-/issues/23#note_173678>)），不一定是一个理想的权衡。 

如需禁用这些选项，可以在 `OPTIONS=()` 数组中的这些选项前直接添加 `!` 符号，例如：`OPTIONS=(...!debug !lto...)`

###  压缩

####  使用其它压缩算法

为了加快打包和安装速度，您可以更改 `PKGEXT`，代价是生成的软件包文件更大。 

例如，以下命令可以跳过压缩步骤，使得[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")时无需解压： 
    
    $ PKGEXT='.pkg.tar' makepkg
    
另一个例子使用 lz4 算法，可以提升速度： 
    
    $ PKGEXT='.pkg.tar.lz4' makepkg
    
要使这些设置之一永久生效，请在 `/etc/makepkg.conf` 中设置 `PKGEXT` 。 

####  在压缩时使用多个 CPU 核心

[zstd](<https://archlinux.org/packages/?name=zstd>)包 支持[对称多处理（SMP）](<https://en.wikipedia.org/wiki/Symmetric_multiprocessing> "wikipedia:Symmetric multiprocessing")，通过添加 `-T`/`--threads` 标志可以加速压缩。默认情况下，`/etc/makepkg.conf` 中的 `COMPRESSZST` 数组包含了 `-T0` 标志，使得 _zstd_ 尽可能使用多的物理 CPU 核心来压缩软件包。可以通过 `--auto-threads=logical` 标志让 _zstd_ 根据逻辑 CPU 核心数进一步提升调用数： 
    
    COMPRESSZST=(zstd -c -T0 **--auto-threads=logical** -)
    
[lz4](<https://archlinux.org/packages/?name=lz4>)包 和 [xz](<https://archlinux.org/packages/?name=xz>)包 默认使用多线程，不需要对 `/etc/makepkg.conf` 进行修改。 

[pigz](<https://archlinux.org/packages/?name=pigz>)包 是 [gzip](<https://archlinux.org/packages/?name=gzip>)包 的一个替代、并行实现，它默认使用所有可用的CPU核心（可以使用 `-p`/`--processes` 标志来使用较少的核心）： 
    
    COMPRESSGZ=(**pigz** -c -f -n)
    
[pbzip2](<https://archlinux.org/packages/?name=pbzip2>)包 是 [bzip2](<https://archlinux.org/packages/?name=bzip2>)包 的一个替代、并行实现，它也默认使用所有可用的CPU核心。可以使用 `-p#` 标志来使用较少的核心（注意：`-p` 和核心数之间没有空格）： 
    
    COMPRESSBZ2=(**pbzip2** -c -f)
    
[lbzip2](<https://archlinux.org/packages/?name=lbzip2>)包 是 [bzip2](<https://archlinux.org/packages/?name=bzip2>)包 的另一个替代、并行实现，它也默认使用所有可用的CPU核心。可以使用 `-n` 标志来使用较少的核心。 
    
    COMPRESSBZ2=(**lbzip2** -c -f)
    
[plzip](<https://aur.archlinux.org/packages/plzip/>)AUR 是 [lzip](<https://archlinux.org/packages/?name=lzip>)包 的一个多线程实现，它也默认使用所有可用的 CPU 核心。可以使用 `-n`/`--threads` 标志来使用较少的核心。 
    
    COMPRESSLZ=(**plzip** -c -f)
    
####  修改压缩等级

有几种压缩算法（包括 zstd 和 xz）支持设定压缩等级，以在速度、内存占用和压缩效率间进行取舍。 

##  小技巧

###  减少下载和解压时间

####  设定源文件位置

特别是在编译 [VCS 软件包](<../zh-cn/VCS_%E8%BD%AF%E4%BB%B6%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "VCS 软件打包准则")时，使用 `SRCDEST` 可以缩短重新构建时获取和解压源代码的时间。 

####  自定义 DLAGENTS

可以使用支持并行下载的下载器，以 [axel](<https://archlinux.org/packages/?name=axel>)包 为例： 
    
    /etc/makepkg.conf
    
    DLAGENTS=('file::/bin/curl -gqC - -o %o %u'
              'ftp::/bin/axel -n 2 -o %o %u'
              'http::/bin/axel -n 2 -o %o %u'
              'https::/bin/axel -n 2 -o %o %u')

另请参考 [Nonfree applications package guidelines#Custom DLAGENTS](</wzh/index.php?title=Nonfree_applications_package_guidelines&action=edit&redlink=1> "Nonfree applications package guidelines（页面不存在）")。 

###  生成新校验和

安装 [pacman-contrib](<https://archlinux.org/packages/?name=pacman-contrib>)包，然后在 PKGBUILD 文件所在目录中执行以下命令来生成新校验和： 
    
    $ updpkgsums
    
`updpkgsums` 使用 `makepkg --geninteg` 生成校验和，查看[此论坛](<https://bbs.archlinux.org/viewtopic.php?pid=1933763#p1933763>)了解详情 

也可以用如 `sha256sum` 命令生成校验和并手动加入到 `sha256sums` 数组中。 

###  从本地源文件生成

如果您想对源代码进行更改，可以使用`-o`、`--nobuild`下载源代码，而无需构建软件包，仅进行下载和解压缩文件选项。 
    
    $ makepkg -o
    
您现在可以对源代码进行更改，然后使用`-e`，`--noextract` 不提取源文件（使用现有的$srcdir/ dir）选项构建软件包。使用`-f`选项覆盖已经生成的和现有的包。 
    
    $ makepkg -ef
    
###  显示具有特定打包程序的包

[expac](<https://archlinux.org/packages/?name=expac>)包 是一个pacman数据库提取工具。此命令显示系统上安装的所有打包程序名为 _packagername_ 的包： 
    
    $ expac "%n %p" | grep "_packagername_ " | column -t
    
这将显示系统上安装的所有软件包， `/etc/makepkg` 变量 `PACKAGER`仅显示在中定义的存储库中的包 `/etc/pacman.conf`。 
    
    $ . /etc/makepkg.conf; grep -xvFf <(pacman -Qqm) <(expac "%n\t%p" | grep "$PACKAGER$" | cut -f1)
    
###  在 64 位系统上构建 32 位软件包

参考[32位软件包打包准则](<../zh-cn/32_%E4%BD%8D%E8%BD%AF%E4%BB%B6%E5%8C%85%E6%89%93%E5%8C%85%E5%87%86%E5%88%99.html> "32位软件包打包准则")。 

###  软件包签名托管

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[GnuPG#Unattended_passphrase](<../zh-cn/GnuPG.html#Unattended_passphrase> "GnuPG")。**

**附注：** 非 _makepkg_ 特定。（在 [Talk:Makepkg](<../zh-cn/Talk:Makepkg.html>) 中讨论）

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 还可以使用 [gpg-preset-passphrase(1)](<https://man.archlinux.org/man/gpg-preset-passphrase.1>) (在 [Talk:Makepkg](<../zh-cn/Talk:Makepkg.html>) 中讨论)

在使用类似 [Jenkins](</wzh/index.php?title=Jenkins&action=edit&redlink=1> "Jenkins（页面不存在）") 的自动构建环境时，用户可能无法为用于软件签名的 gpg 私钥提供密码。另外，不建议在没有密码保护的系统上存放 GPG 私钥。 

使用 _makepkg_ 创建的 zst 软件包可以在创建后通过如下命令进行签名： 
    
    $ gpg --detach-sign --pinentry-mode loopback --passphrase --passphrase-fd 0 --output _NewlyBuilt.pkg.tar.zst.sig_ --sign _NewlyBuilt.pkg.tar.zst_ 
    
其中 GPG 密码由你选择的自动化套件安全地提供和隐藏。 

生成的 `zst` 和 `sig` 文件可被需要有效签名的 [pacman](<../zh-cn/Pacman.html> "Pacman") 客户端和使用 `repo-add --sign` 创建的软件仓库引用。 

###  磁力链接 URI

使用 [transmission-dlagent](<https://aur.archlinux.org/packages/transmission-dlagent/>)AUR 下载器可以支持在 `source` 字段使用磁力链接 URI（前缀为 `magnet://`）。 

### Running makepkg in a systemd control group

If the package you are building takes too many resources to build with your default _make_ flags, which are otherwise set properly for most packages, you can try running it in its own [control group](</wzh/index.php?title=Control_group&action=edit&redlink=1> "Control group（页面不存在）"). [makepkg-cg](<https://aur.archlinux.org/packages/makepkg-cg/>)AUR is a wrapper for _makepkg_ that achieved this via systemd control groups (see [systemd.resource-control(5)](<https://man.archlinux.org/man/systemd.resource-control.5>)). 

### Running with idle scheduling policy

Package build process can lead to high CPU utilization, especially in case of [#Parallel compilation](<#Parallel_compilation>). Under heavy CPU load, the system can issue a significant slowdown up to becoming unusable, even with the highest [nice(1)](<https://man.archlinux.org/man/nice.1>) value. User interface and foreground applications may stutter or even became unresponsive. 

This can be worked around by changing the scheduling policy to `SCHED_IDLE` before running _makepkg_. It ensures that package building process does not interfere with regular tasks and only utilizes remaining unused CPU time. 

From [sched(7) § SCHED_IDLE: Scheduling very low priority jobs](<https://man.archlinux.org/man/sched.7#SCHED_IDLE:_Scheduling_very_low_priority_jobs>): 

    This policy is intended for running jobs at extremely low priority (lower even than a +19 nice value with the `SCHED_OTHER` or `SCHED_BATCH` policies).

The `SCHED_IDLE` policy can be set by running [chrt(1)](<https://man.archlinux.org/man/chrt.1>) command with the `-i` flag, specifying priority 0 (the only valid option for `SCHED_IDLE`) and specifying the PID of the current shell. 

For most shells: 
    
    $ chrt -iap 0 $$
    
**提示：** You can apply this command for every build by placing it into `makepkg.conf`.

For the [fish](<../zh-cn/Fish.html> "Fish") shell, where `$$` is not set: 
    
    $ chrt -iap 0 %self
    
###  在包目录下使用相对路径

Instead of using absolute paths for the [package output options](<#Package_output>), you can also configure relative paths inside each package directory. 

**注意：** The following options might cause problems with some [AUR helpers](<../zh-cn/AUR_helpers.html> "AUR helpers"), as they might use `makepkg.conf` in a context where `$startdir` is not defined. So be careful.

For example, you can define target paths in your `makepkg.conf` file as follows. The `$startdir` variable refers to the directory where a `PKGBUILD` is located when you build a package. 
    
    PKGDEST="$startdir/build/packages/"
    SRCDEST="$startdir/build/sources/"
    SRCPKGDEST="$startdir/build/srcpackages/"
    LOGDEST="$startdir/logs/"
    
This will result in: 

  * Built packages will be stored in: `"package directory"/build/packages/`
  * All downloaded source files will be stored in: `"package directory"/build/sources/`
  * Built source packages will be stored in: `"package directory"/build/srcpackages/`
  * All logs will be stored in: `"package directory"/logs/`

_makepkg_ will still create `src/` and `pkg/` directories as usual, so this is expected behaviour. 

##  问题处理

### Specifying install directory for QMAKE based packages

The makefile generated by _qmake_ uses the environment variable `INSTALL_ROOT` to specify where the program should be installed. Thus this package function should work: 
    
    PKGBUILD
    
    ...
    package() {
    	cd "$srcdir/${pkgname%-git}"
    	make INSTALL_ROOT="$pkgdir" install
    }
    ...

Note, that qmake also has to be configured appropriately. For example put this in the corresponding _.pro_ file: 
    
    YourProject.pro
    
    ...
    target.path = /usr/local/bin
    INSTALLS += target
    ...

###  WARNING: Package contains reference to $srcdir

由于某种原因，有时 `$pkgdir` 或 `$srcdir` 中的字面字符串会进入到软件包中的文件[[7]](<https://lists.archlinux.org/archives/list/arch-general@lists.archlinux.org/thread/Y26ARK6GVXTXSBFRLWNUDPYZV37UQTXH/#DB2RSM6E5UVZKFEGC7JTR6ZDADCVECCT>)。 

可以在 _makepkg_ 构建文件夹中执行以下命令进行检测： 
    
    $ grep -R "$PWD/src" pkg/
    
一个可能是 C/++ 代码使用了 `__FILE__` 宏并将完整路径传递给了编译器。 

Dotnet 二进制文件有时也会在默认配置文件中包含 `.pdb` 文件的完整路径。 

### Makepkg fails to download dependencies when behind proxy

When _makepkg_ calls dependencies, it calls pacman to install the packages, which requires administrative privileges via _sudo_. However, _sudo_ does not pass any [environment variables](<../zh-cn/Environment_variables.html> "Environment variables") to the privileged environment, and includes the proxy-related variables `ftp_proxy`, `http_proxy`, `https_proxy`, and `no_proxy`. 

In order to have _makepkg_ working behind a proxy, invoke one of the following methods. 

#### Enable proxy by setting its URL in XferCommand

The XferCommand can be set to use the desired proxy URL in `/etc/pacman.conf`. Add or uncomment the following line in `pacman.conf`: 
    
    /etc/pacman.conf
    
    ...
    XferCommand = /usr/bin/curl --proxy http://username:password@proxy.proxyhost.com:80 --location --continue-at - --fail --output %o %u
    ...

####  Enable proxy via sudoer's env_keep

Alternatively, one may want to use sudoer's `env_keep` option, which enables preserving given variables the privileged environment. See [Pacman#pacman does not honor proxy settings](<../zh-cn/Pacman.html#pacman_does_not_honor_proxy_settings> "Pacman") for more details. 

###  Makepkg fails, but make succeeds

If something successfully compiles using _make_ , but fails through _makepkg_ , it is almost certainly because `/etc/makepkg.conf` sets an incompatible compilation variable. Try adding these flags to the PKGBUILD `options` array: 

`!buildflags`, to prevent its default `CPPFLAGS`, `CFLAGS`, `CXXFLAGS`, and `LDFLAGS`. 

`!makeflags`, to prevent its default `MAKEFLAGS`. 

`!debug`, to prevent its default `DEBUG_CFLAGS`, and `DEBUG_CXXFLAGS`, in case the PKGBUILD is a debug build. 

If any of these fix the problem, this could warrant an upstream bug report assuming the offending flag has been identified. 

##  参阅

  * [makepkg(8)](<https://man.archlinux.org/man/makepkg.8>)
  * [makepkg.conf(5)](<https://man.archlinux.org/man/makepkg.conf.5>)
  * [Makepkg 流程概览](<https://gist.github.com/Earnestly/bebad057f40a662b5cc3>)
  * [makepkg 源码](<https://gitlab.archlinux.org/pacman/pacman/blob/master/scripts/makepkg.sh.in>)
