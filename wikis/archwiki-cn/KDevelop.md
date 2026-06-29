**翻译状态：**

  * 本文（或部分内容）译自 [KDevelop](<https://wiki.archlinux.org/title/KDevelop> "arch:KDevelop")，最近一次同步于 2026-04-08，若英文版本有所[更改](<https://wiki.archlinux.org/title/KDevelop?diff=0&oldid=868297>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/KDevelop_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[KDevelop](<https://www.kdevelop.org/>) 网站上的介绍： 

    KDevelop 是自由和开源软件（FOSS），是一个由 KDE 社区提供的集成开发环境。它支持多种编程语言的编辑、浏览和调试功能，提供自动纠错、代码建议和自动化构建集成工具，支持许多版本控制系统（例如 git）。同时，基于插件的架构提供了足以满足个人需求的功能扩展和定制能力。

KDevelop 5 具有支持 [C](<../zh-cn/C.html> "C")、[C++](<../zh-cn/C.html> "C")、Objective-C、[OpenCL](<https://wiki.archlinux.org/title/GPGPU#OpenCL> "en:GPGPU") 和 [JavaScript](<https://wiki.archlinux.org/title/Programming_languages> "en:Programming languages")/QML 的解析器，在插件的加持下还支持 [PHP](<../zh-cn/PHP.html> "PHP")、[Python](<../zh-cn/Python.html> "Python")3 和 [Ruby](<../zh-cn/Ruby.html> "Ruby")。尽管不支持其他的源码和标记语言的语义分析，但 KDevelop 依然支持基本的语法高亮和代码折叠。 

KDevelop 是 [KDE](<../zh-cn/KDE.html> "KDE") 项目的一部分，基于 KDE 框架和 [Qt](<../zh-cn/Qt.html> "Qt")。C/C++ 后端使用 Clang、clang-tidy 和 heaptrack 来提供准确的信息，应对非常复杂的代码库也没有问题。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [kdevelop](<https://archlinux.org/packages/?name=kdevelop>)包 软件包即可开始使用。 

##  功能

KDevelop 通过 KParts 框架使用嵌入式文本编辑器组件，默认编辑器是 KDE Advanced Text Editor（Kate），可以选择将其替换为基于 Qt Designer 的编辑器。 

下面的列表重点介绍 KDevelop 本身的功能。 

  * 支持语法高亮和自动缩进功能的源代码编辑器（Kate）。
  * 自 KDevelop 5.0 起使用 Clang 后端支持 C/C++。
  * 支持不同项目类型的管理，例如 Automake、CMake、qmake（用于基于 Qt 的项目）和 Ant（用于基于 Java 的项目）。
  * 类查看器。
  * GUI 设计工具。
  * GCC 和 GDB 的前端。
  * 用于生成和更新类定义和应用程序框架的向导。
  * 自动代码补全（C/C++）。
  * 内置 Doxygen 支持。
  * 修订控制（也称为 SCM）支持。支持的系统包括 CVS、Subversion、Perforce、ClearCase、Git、Mercurial 和 Bazaar。

KDevelop 4 是一个完全基于插件的架构。当开发人员进行更改时，他们只需要编译插件。 

代码补全适用于 C 和 C++，符号保存在 Berkeley DB 文件中，以便快速查找而无需重新解析。 

KDevelop 还提供了一个开发者框架，旨在帮助编写其他编程语言的新解析器。 

集成的调试器通过图形化方式进行各种调试，包括断点和回溯。不同于命令行式的 GDB，它可以与动态加载的插件一起工作。 

Quick Open 可在文件之间快速导航。 

###  插件

目前可用的插件大约有 50 到 100 个。 主要的插件可提供整个项目范围的持久化代码书签保留、支持快速扩展文本的代码缩写、保存文件时进行格式化、正则表达式搜索以及有助于重构代码的项目范围内的代码搜索和替换等功能。 

安装插件以提供自动补全和其他特定语言的功能： 

  * 对于 PHP ，安装 [kdevelop-php](<https://archlinux.org/packages/?name=kdevelop-php>)包 软件包。
  * 对于 Python，安装 [kdevelop-python](<https://archlinux.org/packages/?name=kdevelop-python>)包 软件包。
  * 对于 C++， 安装 [gcc](<https://archlinux.org/packages/?name=gcc>)包 或 [clang](<https://archlinux.org/packages/?name=clang>)包，两个软件包都安装的情况下也没有影响。选择其他编译器也是可行的。

##  构建其他插件

KDevelop 解析器生成器（[kdevelop-pg-qt](<https://archlinux.org/packages/?name=kdevelop-pg-qt>)包）是构建额外插件所必需的。如果未事先安装此包，插件将无法编译。 

##  故障排除

### KDevCMakeManager

如遇到 `Could not load project management plugin KDevCMakeManager` 的错误，请安装 [cmake](<https://archlinux.org/packages/?name=cmake>)包。 

###  使用 GDB 进行调试

需要安装 [okteta](<https://archlinux.org/packages/?name=okteta>)包 并重启 KDevelop 后才能使用 [gdb](<https://archlinux.org/packages/?name=gdb>)包 的调试选项。 
