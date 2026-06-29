**翻译状态：**

  * 本文（或部分内容）译自 [C](<https://wiki.archlinux.org/title/C> "arch:C")，最近一次同步于 2023-05-31，若英文版本有所[更改](<https://wiki.archlinux.org/title/C?diff=0&oldid=774857>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/C_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Linux](<../zh-cn/%E5%86%85%E6%A0%B8.html> "Kernel") 内核和 [GNU](<../zh-cn/GNU.html> "GNU") 用户空间主要由 [C](<https://en.wikipedia.org/wiki/C_\(programming_language\)> "wikipedia:C \(programming language\)") 写成。 

Arch Linux 使用[GNU C Library](<https://en.wikipedia.org/wiki/GNU_C_Library> "wikipedia:GNU C Library")（[glibc](<https://archlinux.org/packages/?name=glibc>)包）作为 C 标准库；它是 [base](<https://archlinux.org/packages/?name=base>)包 [元软件包](<../zh-cn/Meta_package_and_package_group.html#%E5%85%83%E8%BD%AF%E4%BB%B6%E5%8C%85> "Meta package and package group")的一个依赖项。 

你可以使用 [GNU 工具链](<../zh-cn/GNU.html#%E5%B7%A5%E5%85%B7%E9%93%BE> "GNU")或者 [LLVM 工具链](<../zh-cn/LLVM.html#%E5%B7%A5%E5%85%B7%E9%93%BE> "LLVM")来用 C、[C++](<https://en.wikipedia.org/wiki/C%2B%2B> "wikipedia:C++") 或 [Objective-C](<https://en.wikipedia.org/wiki/Objective-C> "wikipedia:Objective-C") 开发软件。 

##  实用工具

  * **[Valgrind](<https://en.wikipedia.org/wiki/Valgrind> "wikipedia:Valgrind")** — 用来找到程序里内存管理问题的工具。

     <https://valgrind.org/> || [valgrind](<https://archlinux.org/packages/?name=valgrind>)包

  * **[Distcc](<../zh-cn/Distcc.html> "Distcc")** — 分布式编译的 GCC 前端。

     <https://github.com/distcc/distcc> || [distcc](<https://archlinux.org/packages/?name=distcc>)包

  * **rr** — 针对 C/C++ 的轻量的记录和定性调试工具，用的是 [GDB](<../zh-cn/GNU.html#%E5%B7%A5%E5%85%B7%E9%93%BE> "GDB")。

     <https://rr-project.org/> || [rr](<https://aur.archlinux.org/packages/rr/>)AUR

###  静态代码分析

  * **[Cppcheck](<https://en.wikipedia.org/wiki/Cppcheck> "wikipedia:Cppcheck")** — 静态 C/C++ 代码分析工具。

     <http://cppcheck.sourceforge.net/> || [cppcheck](<https://archlinux.org/packages/?name=cppcheck>)包

  * **[Splint](<https://en.wikipedia.org/wiki/Splint_\(programming_tool\)> "wikipedia:Splint \(programming tool\)")** — 静态检查 C 程序安全问题和代码错误的工具。

     <https://repo.or.cz/splint-patched.git> || [splint](<https://archlinux.org/packages/?name=splint>)包

  * [Clang](<../zh-cn/Clang.html> "Clang") 提供 _scan-build_ 静态分析器。

##  其他的编译器

  * **[TCC](<https://en.wikipedia.org/wiki/Tiny_C_Compiler> "wikipedia:Tiny C Compiler")** — 微型的 C 编译器，声称比 GCC 快。

     <https://bellard.org/tcc/> || [tcc](<https://archlinux.org/packages/?name=tcc>)包

  * **[ACK](<https://en.wikipedia.org/wiki/Amsterdam_Compiler_Kit> "wikipedia:Amsterdam Compiler Kit")** — 阿姆斯特丹编译包。

     <http://tack.sourceforge.net/> || [ack-git](<https://aur.archlinux.org/packages/ack-git/>)AUR

  * **[PCC](<https://en.wikipedia.org/wiki/Portable_C_Compiler> "wikipedia:Portable C Compiler")** — 可移植的 C 编译器。

     <http://pcc.ludd.ltu.se/> || [pcc](<https://aur.archlinux.org/packages/pcc/>)AUR

  * **[SDCC](<https://en.wikipedia.org/wiki/Small_Device_C_Compiler> "wikipedia:Small Device C Compiler")** — 可重定向的 ANSI C 编译器。

     <https://sdcc.sourceforge.net/> || [sdcc](<https://archlinux.org/packages/?name=sdcc>)包

另见 [Wikipedia:List of compilers#C compilers](<https://en.wikipedia.org/wiki/List_of_compilers#C_compilers> "wikipedia:List of compilers")。 

##  其他的 libc 实现

  * **[dietlibc](<https://en.wikipedia.org/wiki/dietlibc> "wikipedia:dietlibc")** — 为尺寸优化的 libc

     <https://www.fefe.de/dietlibc/> || [dietlibc](<https://aur.archlinux.org/packages/dietlibc/>)AUR

  * **[musl](<https://en.wikipedia.org/wiki/musl> "wikipedia:musl")** — C 标准库的轻量实现。

     <https://musl.libc.org/> || [musl](<https://archlinux.org/packages/?name=musl>)包

##  库

  * [FFmpeg](<../zh-cn/FFmpeg.html> "FFmpeg") \- 包含 libav：音视频库（不要与同名的 FFmpeg 分支混淆）。
  * **[GLib](<https://en.wikipedia.org/wiki/GLib> "wikipedia:GLib")** — [GNOME](<../zh-cn/GNOME.html> "GNOME") 的底层库，包括 [GObject](<https://en.wikipedia.org/wiki/GObject> "wikipedia:GObject") 和 [GIO](<https://en.wikipedia.org/wiki/GIO> "wikipedia:GIO")。

     <https://wiki.gnome.org/Projects/GLib> || [glib2](<https://archlinux.org/packages/?name=glib2>)包

  * [GStreamer](<../zh-cn/GStreamer.html> "GStreamer") – 基于流水线的多媒体框架

另请参阅： 

  * [GTK/Development#C](</wzh/index.php?title=GTK/Development&action=edit&redlink=1> "GTK/Development（页面不存在）")
  * [Desktop notifications#C](<../zh-cn/Desktop_notifications.html#C> "Desktop notifications")
  * [Libcanberra#C](</wzh/index.php?title=Libcanberra&action=edit&redlink=1> "Libcanberra（页面不存在）")
  * [Archiving and compression#Compression libraries](<../zh-cn/Archiving_and_compression.html#Compression_libraries> "Archiving and compression")
  * [Wikipedia:Category:C (programming language) libraries](<https://en.wikipedia.org/wiki/Category:C_\(programming_language\)_libraries> "wikipedia:Category:C \(programming language\) libraries")
  * [A list of open source C libraries](<https://en.cppreference.com/w/c/links/libs>)

##  参见

  * [手册页](<../zh-cn/Man_%E6%89%8B%E5%86%8C.html> "手册页")在第二区的系统调用
  * [手册页](<../zh-cn/Man_%E6%89%8B%E5%86%8C.html> "手册页")在第三区的库函数
  * [GCC and Make – Compiling, Linking and Building C/C++ Applications](<https://www3.ntu.edu.sg/home/ehchua/programming/cpp/gcc_make.html>)
  * [SEI CERT C Coding Standard](<https://wiki.sei.cmu.edu/confluence/display/c/SEI+CERT+C+Coding+Standard>)
  * [#C IRC channel](<https://iso-9899.info/>)
