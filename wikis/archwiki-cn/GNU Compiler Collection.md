**翻译状态：**

  * 本文（或部分内容）译自 [GNU Compiler Collection](<https://wiki.archlinux.org/title/GNU_Compiler_Collection> "arch:GNU Compiler Collection")，最近一次同步于 2025-03-14，若英文版本有所[更改](<https://wiki.archlinux.org/title/GNU_Compiler_Collection?diff=0&oldid=807973>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/GNU_Compiler_Collection_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [LLVM](<../zh-cn/LLVM.html> "LLVM")

[GNU Compiler Collection](<https://en.wikipedia.org/wiki/GNU_Compiler_Collection> "wikipedia:GNU Compiler Collection")（**GCC** ，《GNU 编译器集合》）是 [GNU 工具链](<../zh-cn/GNU.html#%E5%B7%A5%E5%85%B7%E9%93%BE> "GNU")的一部分，并包括 [C](<../zh-cn/C.html> "C") 和 [C++](<../zh-cn/C.html> "C++") 的前端。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [gcc](<https://archlinux.org/packages/?name=gcc>)包 包。 

其他可用的前端有： 

  * [gcc-ada](<https://archlinux.org/packages/?name=gcc-ada>)包 [Ada](<https://wiki.archlinux.org/title/Ada> "en:Ada") 前端
  * [gcc-d](<https://archlinux.org/packages/?name=gcc-d>)包 [D](<https://wiki.archlinux.org/title/D> "en:D") 前端
  * [gcc-fortran](<https://archlinux.org/packages/?name=gcc-fortran>)包 [Fortran](<../zh-cn/Fortran.html> "Fortran") 前端
  * [gcc-go](<https://archlinux.org/packages/?name=gcc-go>)包 [Go](<../zh-cn/Go.html> "Go") 前端
  * [gcc-m2](<https://archlinux.org/packages/?name=gcc-m2>)包 [Modula-2](<https://en.wikipedia.org/wiki/Modula-2> "wikipedia:Modula-2")前端
  * [gcc-objc](<https://archlinux.org/packages/?name=gcc-objc>)包 [Objective-C](<https://en.wikipedia.org/wiki/Objective-C> "wikipedia:Objective-C") 前端
  * [gcc-rust](<https://archlinux.org/packages/?name=gcc-rust>)包 [Rust](<../zh-cn/Rust.html> "Rust")前端

###  旧版本

旧版本的 GCC 适用于以下情况：完成历史探究需求、编译一些无法在当前版本上编译的旧项目，或者是需要测试项目的兼容性： 

  * GCC 4.3: [gcc43](<https://aur.archlinux.org/packages/gcc43/>)AUR
  * GCC 4.4: [gcc44](<https://aur.archlinux.org/packages/gcc44/>)AUR
  * GCC 4.5: [gcc45](<https://aur.archlinux.org/packages/gcc45/>)AUR
  * GCC 4.6: [gcc46](<https://aur.archlinux.org/packages/gcc46/>)AUR
  * GCC 4.7: [gcc47](<https://aur.archlinux.org/packages/gcc47/>)AUR
  * GCC 4.8: [gcc48](<https://aur.archlinux.org/packages/gcc48/>)AUR
  * GCC 4.9: [gcc49](<https://aur.archlinux.org/packages/gcc49/>)AUR
  * GCC 5: [gcc5](<https://aur.archlinux.org/packages/gcc5/>)AUR
  * GCC 6: [gcc6](<https://aur.archlinux.org/packages/gcc6/>)AUR
  * GCC 7: [gcc7](<https://aur.archlinux.org/packages/gcc7/>)AUR
  * GCC 8: [gcc8](<https://aur.archlinux.org/packages/gcc8/>)AUR
  * GCC 9: [gcc9](<https://aur.archlinux.org/packages/gcc9/>)AUR
  * GCC 10: [gcc10](<https://aur.archlinux.org/packages/gcc10/>)AUR
  * GCC 11: [gcc11](<https://aur.archlinux.org/packages/gcc11/>)AUR
  * GCC 12: [gcc12](<https://aur.archlinux.org/packages/gcc12/>)AUR
  * GCC 13: [gcc13](<https://archlinux.org/packages/?name=gcc13>)包

旧版本 GCC 的其他前端可以通过搜索 `gcc<_去掉点的版本号_ >` 在[官方软件仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方软件仓库")和 [AUR](<../zh-cn/Arch_User_Repository.html> "Arch User Repository") 中找到，例如搜索 `gcc9` 查找 GCC 9 前端。 

**提示：** 可通过设置 `CC`（用于 C 语言）[[1]](<https://cmake.org/cmake/help/latest/envvar/CC.html>)和 `CXX`（用于 C++）[[2]](<https://cmake.org/cmake/help/latest/envvar/CXX.html>)[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")，在使用 make 或 cmake 等构建工具时指定特定版本的 GCC。例如：
    
    $ export CC=gcc-12 CXX=g++-12

##  参见

  * [信息手册](<https://gcc.gnu.org/onlinedocs/gcc/>)
  * [官方网站](<https://gcc.gnu.org/>)
  * [gcc(1)](<https://man.archlinux.org/man/gcc.1>)
