**翻译状态：**

  * 本文（或部分内容）译自 [Fortran](<https://wiki.archlinux.org/title/Fortran> "arch:Fortran")，最近一次同步于 2025-05-07，若英文版本有所[更改](<https://wiki.archlinux.org/title/Fortran?diff=0&oldid=833417>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Fortran_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Fortran](<https://en.wikipedia.org/wiki/Fortran> "wikipedia:Fortran") 是一门通用型、编译式命令式编程语言，特别适用于数值计算和科学计算。 

来自 [Fortran 社区（fortran-lang）](<https://fortran-lang.org/zh_CN/>)网站的说明： 

    Fortran 是一门成熟且处于积极开发中的语言。其最新修订版本为 Fortran 2023。现有许多的开源与专有 Fortran 编译器。此外，诸如标准库和 Fortran 包管理器（Fortran Package Manager，FPM）等开源项目也正处于活跃开发阶段。

##  编译器

[gcc-fortran](<https://archlinux.org/packages/?name=gcc-fortran>)包 软件包可为 [GCC](<../zh-cn/GNU_Compiler_Collection.html> "GCC") 启用 Fortran 前端。 

其他适用于 Arch Linux 的 Fortran 编译器包括： 

  * **lfortran** — 基于 LLVM 构建的现代交互式 Fortran 编译器。

     <https://lfortran.org> || [lfortran](<https://aur.archlinux.org/packages/lfortran/>)AUR

  * **（LLVM） Flang** — 采用现代 C++ 实现的 Fortran 2018 新 LLVM 前端。

     <https://flang.llvm.org/> || [flang](<https://aur.archlinux.org/packages/flang/>)AUR

  * **Flang（经典版）** — 面向 LLVM 的独立 Fortran 编译器（未来将被新版 Flang 取代）。

     <https://github.com/flang-compiler/flang> || [flang-classic](<https://aur.archlinux.org/packages/flang-classic/>)AUR

另请参阅 [fortran-lang](<https://fortran-lang.org/compilers/>) 获取开源和商业编译器列表。请查阅您所用编译器的文档以确认其符合哪些[标准](<https://fortranwiki.org/fortran/show/Standards>)及提供了哪些语言扩展功能。 

##  附加软件包

  * **Fortran Standard Library** — 旨在为 Fortran 提供社区驱动且达成共识的事实"标准"库（目前处于 alpha 阶段）。

     <https://stdlib.fortran-lang.org/> || [fortran_stdlib](<https://aur.archlinux.org/packages/fortran_stdlib/>)AUR

  * **Fortran Package Manager** — Fortran 的包管理器与构建系统（目前处于 alpha 阶段）。

     <https://fpm.fortran-lang.org/> || [fortran-fpm](<https://aur.archlinux.org/packages/fortran-fpm/>)AUR、[fortran-fpm-bin](<https://aur.archlinux.org/packages/fortran-fpm-bin/>)AUR

  * **fortls** — Fortran [语言服务器](<../zh-cn/%E8%AF%AD%E8%A8%80%E6%9C%8D%E5%8A%A1%E5%99%A8%E5%8D%8F%E8%AE%AE.html> "语言服务器协议")。

     <https://fortls.fortran-lang.org/> || [fortls](<https://aur.archlinux.org/packages/fortls/>)AUR、[fortls](<https://github.com/archlinuxcn/repo/tree/master/archlinuxcn/fortls>)[CNRepo](<../zh-cn/Arch_Linux_%E4%B8%AD%E6%96%87%E7%A4%BE%E5%8C%BA%E4%BB%93%E5%BA%93.html> "Arch Linux 中文社区仓库")

  * **FORD** — 通过代码注释生成文档。

     <https://github.com/Fortran-FOSS-Programmers/ford> || [ford](<https://aur.archlinux.org/packages/ford/>)AUR

  * **f2c** — Fortran 转 C 代码转换器。

     <https://www.netlib.org/f2c/> || [f2c](<https://aur.archlinux.org/packages/f2c/>)AUR

另请参阅 [fortran-lang 软件包索引](<https://fortran-lang.org/packages/>)。 

##  参阅

  * [FortranCon2021/Fortran-lang：Fortran 现状（YouTube 视频）](<https://www.youtube.com/watch?v=EgkQdqJIJU0>)

  * [fortran-lang 现代 Fortran 学习资源](<https://fortran-lang.org/learn/>)

  * [Fortran 维基](<https://fortranwiki.org/>)

  * [J3（美国）](<https://j3-fortran.org/>)与 [WG5（国际）](<https://wg5-fortran.org/>) Fortran 标准委员会

  * [左志华先生所著《Ch27-Fortran 编程》](<https://userzuo.netlify.app/ch27-fortran-%E7%BC%96%E7%A8%8B/>)
