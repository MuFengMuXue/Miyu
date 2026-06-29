**翻译状态：**

  * 本文（或部分内容）译自 [Clang](<https://wiki.archlinux.org/title/Clang> "arch:Clang")，最近一次同步于 2025-11-15，若英文版本有所[更改](<https://wiki.archlinux.org/title/Clang?diff=0&oldid=847843>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Clang_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Clang](<https://clang.llvm.org/>) 是基于 [LLVM](<../zh-cn/LLVM.html> "LLVM") 的 [C](<../zh-cn/C.html> "C")/C++/Objective C/[CUDA](<../zh-cn/GPGPU.html#CUDA> "CUDA") 编译器。最新版本依据 “带有 LLVM 例外条款的 Apache 2.0 许可证” 分发。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [clang](<https://archlinux.org/packages/?name=clang>)包 软件包。 

##  用 Clang 构建软件包

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[makepkg ](<../zh-cn/Makepkg.html> "Makepkg")。**

**附注：** 用于 [makepkg](<../zh-cn/Makepkg.html> "Makepkg") 的编译器标志（在 [Talk:Clang](<../zh-cn/Talk:Clang.html>) 中讨论）

###  通用配置

要更改构建软件包时使用的默认编译器，请 [编辑](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "编辑") 以下文件： 
    
    /etc/makepkg.conf
    
    ...
    export CC=clang
    export CXX=clang++

若要使用 `libc++` 替代 [GCC](<../zh-cn/GNU_Compiler_Collection.html> "GCC") 的 `libstdc++` 作为 [C++ 标准库](<https://en.wikipedia.org/wiki/C%2B%2B_Standard_Library> "wikipedia:C++ Standard Library")：需先安装 [libc++](<https://archlinux.org/packages/?name=libc%2B%2B>)包 软件包，再在 `/etc/makepkg.conf` 的 `CXXFLAGS` 中添加 `-stdlib=libc++`。 

如需支持链接时优化（LTO）：[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [lld](<https://archlinux.org/packages/?name=lld>)包 软件包，再在 `/etc/makepkg.conf` 的 `LDFLAGS` 中添加 `-fuse-ld=lld`。 

若以 `debug` 模式构建，还需从 `DEBUG_CFLAGS` 和 `DEBUG_CXXFLAGS` 中移除 `-fvar-tracking-assignments`，因为 Clang 不支持该选项。 

**注意：** 对于指定了 GCC 专属构建选项的软件包，可能会出现构建错误，此时需编辑源软件包、[PKGBUILD](<../zh-cn/PKGBUILD.html> "PKGBUILD") 文件，或注释掉 `makepkg.conf` 中与 Clang 相关的配置行。

##  Qt 软件包

[Qt](<../zh-cn/Qt.html> "Qt") 软件包可能需要额外配置。Qt 有预定义的构建配置（称为 “mkspecs”），在 Linux 上默认使用 [GCC](<../zh-cn/GNU_Compiler_Collection.html> "GCC")。 

部分情况下，mkspec 会根据 `CC`/`CXX` 变量自动设置为 `linux-clang`；但在其他情况下（如直接调用 `qmake` 的软件包）则不会，因此需手动显式设置：
    
    /etc/makepkg.conf
    
    export QMAKESPEC=linux-clang

**注意：** 部分软件包需要安装 [llvm](<https://archlinux.org/packages/?name=llvm>)包 软件包，因为 `linux-clang` 配置会使用 `llvm-ar` 等工具。

##  Rust 软件包

当 Clang 被设为系统默认编译器时，需配置 Rust 使用 Clang 作为链接器 ——Rust 应用构建过程中，常会编译 C 代码作为依赖。 

配置方法：在 `/etc/makepkg.conf.d/rust.conf` 中指定 Clang（可选指定 lld）。示例（使用 Clang 和 lld）：
    
    /etc/makepkg.conf.d/rust.conf
    
    RUSTFLAGS="-Cforce-frame-pointers=yes -Clinker=clang -Clink-arg=-fuse-ld=lld"

##  使用静态分析工具

要分析项目，只需在构建命令的前面放置` scan-build`。 例如： 
    
    $ scan-build make
    
**提示：** 如果您的项目已经被编译，` scan-build`将不会重建，也不会对其进行分析。如需强制重新编译和分析，请使用` -B`参数： 
    
    $ scan-build make -B

也可针对特定文件进行分析： 
    
    $ scan-build gcc -c t1.c t2.c
    
##  参见

  * [Wikipedia: Clang](<https://en.wikipedia.org/wiki/Clang> "wikipedia:Clang")
  * [scan-build：从命令行运行分析器](<https://clang-analyzer.llvm.org/scan-build.html>)
  * [使用 Clang 编译 CUDA 代码](<https://llvm.org/docs/CompileCudaWithLLVM.html>)
