相关文章

  * [Arch Linux](<../zh-cn/Arch_Linux.html> "Arch Linux")
  * [核心工具](<../zh-cn/%E6%A0%B8%E5%BF%83%E5%B7%A5%E5%85%B7.html> "核心工具")

摘自 [GNU 系统概览](<https://www.gnu.org/gnu/gnu-history.html>): 

    GNU 系统是一套向上兼容 Unix 的完全自由的操作系统。GNU 代表“GNU's Not Unix”。它的发音是[带有 g 音的单音节](<https://www.gnu.org/gnu/pronunciation.html>)。[理查德·斯托曼](<https://www.stallman.org/>)在 1983 年 9 月做出了 GNU 工程的[初始声明](<https://www.gnu.org/gnu/initial-announcement.html>)。接着在 1985 年 3 月又发表了更长的版本，叫做 [GNU 宣言](<https://www.gnu.org/gnu/manifesto.html>)。它被翻译成多种其他语言。

因为 GNU 自己的 [Hurd](<https://www.gnu.org/software/hurd/hurd.html>) 内核尚不成熟[[1]](<https://www.gnu.org/software/hurd/hurd/status.html>)，GNU 一般使用 Linux 内核。[Arch Linux](<../zh-cn/Arch_Linux.html> "Arch Linux") 就是这类 GNU/Linux 发行版之一，使用了包括 [Bash](<../zh-cn/Bash.html> "Bash") 终端、GNU [核心工具](<../zh-cn/%E6%A0%B8%E5%BF%83%E5%B7%A5%E5%85%B7.html> "核心工具")、GNU [工具链](<#%E5%B7%A5%E5%85%B7%E9%93%BE>)在内的各种工具和库。此页面只列出部分[官方仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方仓库")或 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 中存在的 GNU 软件包，而不会列出所有的[近 400 个](<https://www.gnu.org/software/software.html#allgnupkgs>)软件包。而且，Arch Linux（包括[官方仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方仓库")和 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR")）并没有打包**全部** 的 GNU 软件。 

**提示：** 为了方便排序，本文列表使用各软件包简称而非全称。比如， _GNU GRUB_ 会写作 _GRUB_ 。

##  内核

摘自 [GNU Linux-libre 项目网站](<https://www.fsfla.org/ikiwiki/selibre/linux-libre/>)： 

    由 Linus Torvalds 等人开发和发布的 Linux 内核包含非自由软件，即不尊重你的[基本自由](<https://www.fsfla.org/ikiwiki/about/what-is-free-software.en.html>)的软件，而且它还诱使你安装额外的非自由软件。即使据称从 4.14 版开始将所有固件转移到一个单独的项目中，Torvalds 先生发布的 Linux 所谓“源代码”仍然包含伪装成源代码的非自由固件。

    GNU Linux-libre 是一个维护和发布 100% 自由 Linux 发行版的项目，适合在[自由系统](<https://www.gnu.org/distros/free-system-distribution-guidelines.zh-cn.html>)中使用，删除不含源代码、源代码被混淆或掩盖、使用非自由软件许可、不允许更改软件使其按照你的意愿运行、诱导或要求你安装额外的非自由软件的软件。

GNU Linux-libre 可通过[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [linux-libre](<https://github.com/archlinuxcn/repo/tree/master/archlinuxcn/linux-libre>)[CNRepo](<../zh-cn/Arch_Linux_%E4%B8%AD%E6%96%87%E7%A4%BE%E5%8C%BA%E4%BB%93%E5%BA%93.html> "Arch Linux 中文社区仓库") 或 [linux-libre](<https://aur.archlinux.org/packages/linux-libre/>)AUR 获取。 

为 Linux Libre 内核构建模块的头文件和脚本可通过 [linux-libre-headers](<https://github.com/archlinuxcn/repo/tree/master/archlinuxcn/linux-libre-headers>)[CNRepo](<../zh-cn/Arch_Linux_%E4%B8%AD%E6%96%87%E7%A4%BE%E5%8C%BA%E4%BB%93%E5%BA%93.html> "Arch Linux 中文社区仓库") 或 [linux-libre-headers](<https://aur.archlinux.org/packages/linux-libre-headers/>)AUR [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")。 

Linux Libre 内核文档通过[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [linux-libre-docs](<https://github.com/archlinuxcn/repo/tree/master/archlinuxcn/linux-libre-docs>)[CNRepo](<../zh-cn/Arch_Linux_%E4%B8%AD%E6%96%87%E7%A4%BE%E5%8C%BA%E4%BB%93%E5%BA%93.html> "Arch Linux 中文社区仓库") 或 [linux-libre-docs](<https://aur.archlinux.org/packages/linux-libre-docs/>)AUR 获取。 

## Texinfo

参见 [GNU/文档#Texinfo](<../zh-cn/GNU/%E6%96%87%E6%A1%A3.html#Texinfo> "GNU/文档")。 

##  基本系统组件

  * **[Bash](<../zh-cn/Bash.html> "Bash")** — Bash 是一种与其他 shell 兼容的 shell，它合并了许多 korn shell（ksh）和 C shell（csh）的特性。

     <https://www.gnu.org/software/bash/> || [bash](<https://archlinux.org/packages/?name=bash>)包

  * **[核心工具](<../zh-cn/%E6%A0%B8%E5%BF%83%E5%B7%A5%E5%85%B7.html> "核心工具")** — 核心工具提供了 GNU 系统最基本的文件、shell 和文本操作工具。

     <https://www.gnu.org/software/coreutils/> || [coreutils](<https://archlinux.org/packages/?name=coreutils>)包、[tar](<https://archlinux.org/packages/?name=tar>)包、[less](<https://archlinux.org/packages/?name=less>)包、[findutils](<https://archlinux.org/packages/?name=findutils>)包、[diffutils](<https://archlinux.org/packages/?name=diffutils>)包、[grep](<https://archlinux.org/packages/?name=grep>)包、[sed](<https://archlinux.org/packages/?name=sed>)包、[gawk](<https://archlinux.org/packages/?name=gawk>)包

  * **[GRUB](<../zh-cn/GRUB.html> "GRUB")** — GRUB 是 GNU 项目的引导程序。

     <https://www.gnu.org/software/grub/> || [grub](<https://archlinux.org/packages/?name=grub>)包

  * **[gzip](<https://en.wikipedia.org/wiki/gzip> "wikipedia:gzip")** — gzip 既是一种文件格式，又是一种[压缩和解压](<../zh-cn/%E5%BD%92%E6%A1%A3%E4%B8%8E%E5%8E%8B%E7%BC%A9.html> "归档与压缩")工具。

     <https://www.gnu.org/software/gzip/> || [gzip](<https://archlinux.org/packages/?name=gzip>)包

  * **[tar](<../zh-cn/%E5%BD%92%E6%A1%A3%E4%B8%8E%E5%8E%8B%E7%BC%A9.html> "Tar")** — tar 提供了创建和解压 tar 压缩包的功能，也提供一些其它功能。

     <https://www.gnu.org/software/tar/> || [tar](<https://archlinux.org/packages/?name=tar>)包

##  工具链

大部分 [GNU toolchain](<https://en.wikipedia.org/wiki/GNU_toolchain> "wikipedia:GNU toolchain") 中的工具都是 [base-devel](<https://archlinux.org/packages/?name=base-devel>)包 软件包的依赖, 除了 _glibc_ （[base](<https://archlinux.org/packages/?name=base>)包 的依赖）和 GDB。 

  * **[Binutils](<https://en.wikipedia.org/wiki/GNU_Binutils> "wikipedia:GNU Binutils")** — 一组用来汇编和操作二进制和模板文件的程序。包括 [ld](<https://en.wikipedia.org/wiki/GNU_linker> "wikipedia:GNU linker")。

     <https://www.gnu.org/software/binutils/> || [binutils](<https://archlinux.org/packages/?name=binutils>)包

  * **[Bison](<https://en.wikipedia.org/wiki/GNU_Bison> "wikipedia:GNU Bison")** — GNU 通用解析器生成器。

     <https://www.gnu.org/software/bison/bison.html> || [bison](<https://archlinux.org/packages/?name=bison>)包

  * **[GCC](<../zh-cn/GNU_Compiler_Collection.html> "GNU Compiler Collection")** — GNU 编译器集合-C 和 C++ 前端。

     <https://gcc.gnu.org/> || [gcc](<https://archlinux.org/packages/?name=gcc>)包

  * **[GDB](<https://en.wikipedia.org/wiki/GNU_Debugger> "wikipedia:GNU Debugger")** — GNU 调试器。

     <https://www.gnu.org/software/gdb/> || [gdb](<https://archlinux.org/packages/?name=gdb>)包

  * **[glibc](<https://en.wikipedia.org/wiki/GNU_C_Library> "wikipedia:GNU C Library")** — GNU 的 C 库实现 library。

     <https://www.gnu.org/software/libc/> || [glibc](<https://archlinux.org/packages/?name=glibc>)包 （[base](<https://archlinux.org/packages/?name=base>)包 的依赖）

  * **[GNU m4](<https://en.wikipedia.org/wiki/GNU_m4> "wikipedia:GNU m4")** — GNU 宏处理器。

     <https://www.gnu.org/software/m4/> || [m4](<https://archlinux.org/packages/?name=m4>)包

  * **[make](<https://en.wikipedia.org/wiki/Make_\(software\)> "wikipedia:Make \(software\)")** — GNU make 工具，用于维护程序组。

     <https://www.gnu.org/software/make> || [make](<https://archlinux.org/packages/?name=make>)包

###  构建系统

来自[维基百科](<https://en.wikipedia.org/wiki/GNU_build_system> "wikipedia:GNU build system"): 

    GNU 构建系统，也被叫做自动工具，是一套用来帮助让源码包能移植到类 Unix 系统的编程工具

  * **[Autoconf](<https://en.wikipedia.org/wiki/Autoconf> "wikipedia:Autoconf")** — 用来自动设置源码的工具。

     <https://www.gnu.org/software/autoconf> || [autoconf](<https://archlinux.org/packages/?name=autoconf>)包

  * **[Automake](<https://en.wikipedia.org/wiki/Automake> "wikipedia:Automake")** — 自动创建 make 文件的工具。

     <https://www.gnu.org/software/automake> || [automake](<https://archlinux.org/packages/?name=automake>)包

  * **[GNU Libtool](<https://en.wikipedia.org/wiki/Libtool> "wikipedia:Libtool")** — 支持脚本的通用库。

     <https://www.gnu.org/software/libtool> || [libtool](<https://archlinux.org/packages/?name=libtool>)包

##  其他软件

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 此节内容有待扩充。 (在 [Talk:GNU](<../zh-cn/Talk:GNU.html>) 中讨论)

**注意：**[gnuplot](<https://archlinux.org/packages/?name=gnuplot>)包 不是 GNU 软件。[Gnuplot](<http://www.gnuplot.info/>) 既不是由 FSF 编写，也不是由 FSF 维护。它曾一度由 FSF 发布，但现在已不再如此。整个 Gnuplot 不在 GNU 通用公共许可证 (GPL) 的覆盖范围内。

在[官方仓库](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方仓库")和 [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR") 中可以找到其它可选 GNU 工具： 

  * **a2ps** — 一个 Any to PostScript 过滤器。

     <https://www.gnu.org/software/a2ps/> || [a2ps](<https://archlinux.org/packages/?name=a2ps>)包

  * **acct** — 监控进程活动的工具

     <https://www.gnu.org/software/acct/> || [acct](<https://aur.archlinux.org/packages/acct/>)AUR

  * **adns** — 先进、易用、支持异步的 DNS 客户端库和工具。

     <https://www.gnu.org/software/adns/> || [adns](<https://archlinux.org/packages/?name=adns>)包

  * **alive** — 一个定期 ping 程序。

     <https://www.gnu.org/software/alive/> || [alive](<https://aur.archlinux.org/packages/alive/>)AUR

  * **Anastasis** — 是一个自由软件协议和实施方案，允许用户将核心机密安全地存放在一组开放的托管服务提供商处，并在原始副本丢失时恢复这些机密。

     <https://www.gnu.org/software/anastasis/> || [anastasis](<https://aur.archlinux.org/packages/anastasis/>)AUR

  * **anubis** — SMTP 消息提交守护进程。

     <https://www.gnu.org/software/anubis/> || [anubis](<https://aur.archlinux.org/packages/anubis/>)AUR

  * **apl** — 编程语言 APL 的自由解释器。

     <https://www.gnu.org/software/apl/> || [gnu-apl](<https://aur.archlinux.org/packages/gnu-apl/>)AUR

  * **Archimedes** — 半导体器件模拟。

     <https://www.gnu.org/software/archimedes/> || [archimedes](<https://aur.archlinux.org/packages/archimedes/>)AUR

  * **[Artanis](<../zh-cn/Artanis.html> "Artanis")** — 一个用 Guile Scheme 编写的网络应用程序框架（WAF）。

     <https://www.gnu.org/software/artanis/> || [artanis](<https://aur.archlinux.org/packages/artanis/>)AUR

  * **[Aspell](<../zh-cn/%E8%AF%AD%E8%A8%80%E6%A3%80%E6%9F%A5.html> "Aspell")** — 拼写检查器。

     <http://aspell.net> || [aspell](<https://archlinux.org/packages/?name=aspell>)包

  * **AUCTeX** — 在 Emacs 中制作 TeX 文档的集成环境。

     <https://www.gnu.org/software/auctex/> || [auctex](<https://aur.archlinux.org/packages/auctex/>)AUR

  * **barcode** — 将文本字符串转换为打印条形码的工具。

     <https://www.gnu.org/software/barcode/> || [barcode](<https://archlinux.org/packages/?name=barcode>)包

  * **[bc](<https://en.wikipedia.org/wiki/bc_\(programming_language\)#GNU_bc> "wikipedia:bc \(programming language\)")** — 一种任意精度计算器语言。

     <https://www.gnu.org/software/bc> || [bc](<https://archlinux.org/packages/?name=bc>)包

  * **c-graph** — 展示工程系统和信号分析所依据的卷积理论。

     <https://www.gnu.org/software/c-graph/> || [c-graph](<https://aur.archlinux.org/packages/c-graph/>)AUR

  * **ccd2cue** — 将 CloneCD 提示表（.ccd）转换为兼容性较差的 CDRWIN 提示表（.cue）。

     <https://www.gnu.org/software/ccd2cue/> || [ccd2cue](<https://aur.archlinux.org/packages/ccd2cue/>)AUR

  * **ccRTP** — IETF 的实时传输协议 RTP 的实现。

     <https://www.gnu.org/software/ccrtp/> || [ccrtp](<https://aur.archlinux.org/packages/ccrtp/>)AUR

  * **Cflow** — C 程序流分析器。

     <https://www.gnu.org/software/cflow/> || [cflow](<https://aur.archlinux.org/packages/cflow/>)AUR

  * **Cgicc** — 简化 CGI 应用程序创建的 C++ 库。

     <https://www.gnu.org/software/cgicc/> || [cgicc](<https://aur.archlinux.org/packages/cgicc/>)AUR

  * **Chess** — 国际象棋前端引擎，在终端上与计算机下棋。

     <https://www.gnu.org/software/chess/chess.html> || [gnuchess](<https://archlinux.org/packages/?name=gnuchess>)包

  * **Classpath** — Sun 专有的核心 Java 类库的自由替代。

     <https://www.gnu.org/software/classpath/> || [classpath](<https://aur.archlinux.org/packages/classpath/>)AUR

  * **Clisp** — ANSI Common Lisp 解释器、编译器和调试器。

     <https://www.gnu.org/software/clisp/> || [clisp](<https://archlinux.org/packages/?name=clisp>)包

  * **Complexity** — 测量 C 代码的复杂性。

     <https://www.gnu.org/software/complexity/> || [complexity](<https://aur.archlinux.org/packages/complexity/>)AUR

  * **Cppi** — GNU Cppi 对 C 预处理器指令进行缩进，以反映其嵌套情况，并进行其他规范化处理。

     <https://www.gnu.org/software/cppi/> || [cppi](<https://aur.archlinux.org/packages/cppi/>)AUR

  * **CSSC** — Unix SCCS 工具套件的克隆版。

     <https://www.gnu.org/software/cssc/> || [cssc](<https://aur.archlinux.org/packages/cssc/>)AUR

  * **Cursynth** — GNU ncurses 终端合成器。

     <https://gnu.org/software/cursynth> || [cursynth-git](<https://aur.archlinux.org/packages/cursynth-git/>)AUR

  * **Datamash** — 对输入的文本数据文件执行基本的数字、文本和统计操作。

     <https://www.gnu.org/software/datamash> || [datamash](<https://archlinux.org/packages/?name=datamash>)包

  * **DDD** — 命令行调试器的图形前端，如 GDB、JDB、ydb、perl 调试器...

     <https://www.gnu.org/software/ddd/> || [ddd](<https://aur.archlinux.org/packages/ddd/>)AUR

  * **[ddrescue](</wzh/index.php?title=Ddrescue&action=edit&redlink=1> "Ddrescue（页面不存在）")** — 一个数据恢复工具。

     <https://www.gnu.org/software/ddrescue> || [ddrescue](<https://archlinux.org/packages/?name=ddrescue>)包

  * **DejaGnu** — 测试其他程序的框架。

     <https://www.gnu.org/software/dejagnu/> || [dejagnu](<https://archlinux.org/packages/?name=dejagnu>)包

  * **Denemo** — 乐谱编辑器。

     <https://www.denemo.org/> || [denemo](<https://aur.archlinux.org/packages/denemo/>)AUR

  * **Dia** — 基于 GTK+ 的图表创建程序。

     <https://wiki.gnome.org/Apps/Dia> || [dia](<https://aur.archlinux.org/packages/dia/>)AUR

  * **Dico** — GNU 词典服务器。

     <https://www.gnu.org/software/dico/> || [dico](<https://aur.archlinux.org/packages/dico/>)AUR

  * **Diction** — 用于识别文章中的生词和常见误用短语。

     <https://www.gnu.org/software/diction/> || [diction](<https://aur.archlinux.org/packages/diction/>)AUR

  * **Direvent** — 监控目录事件（如创建、删除或修改文件）的守护进程。

     <https://www.gnu.org/software/direvent/> || [direvent](<https://aur.archlinux.org/packages/direvent/>)AUR

  * **Ed** — 符合 POSIX 标准的行式文本编辑器。

     <https://www.gnu.org/software/ed/> || [ed](<https://archlinux.org/packages/?name=ed>)包

  * **[Emacs](<../zh-cn/Emacs.html> "Emacs")** — 一款可扩展、可定制、自文档化的文本编辑器。

     <https://www.gnu.org/software/emacs> || [emacs](<https://archlinux.org/packages/?name=emacs>)包 或 [emacs-nox](<https://archlinux.org/packages/?name=emacs-nox>)包

  * **[FreeFont](<https://en.wikipedia.org/wiki/GNU_FreeFont> "wikipedia:GNU FreeFont")** — 免费的可缩放轮廓字体系列。

     <https://www.gnu.org/software/freefont> || [gnu-free-fonts](<https://archlinux.org/packages/?name=gnu-free-fonts>)包

  * **gcal** — 在终端中输出日历。

     <https://www.gnu.org/software/gcal/> || [gcal](<https://aur.archlinux.org/packages/gcal/>)AUR

  * **[Ghostscript](<https://en.wikipedia.org/wiki/Ghostscript> "wikipedia:Ghostscript")** — PostScript 和 PDF 的解释器。提供 [gs(1)](<https://man.archlinux.org/man/gs.1>) 命令行界面，另请参阅 `/usr/share/doc/ghostscript/*/Use.htm`（[在线阅读](<https://ghostscript.readthedocs.io/en/latest/Use.html>)），以及许多封装脚本，如 _ps2pdf_ 和 _pdf2ps_ 。

     <https://ghostscript.com/> || [ghostscript](<https://archlinux.org/packages/?name=ghostscript>)包

  * **[GIMP](<../zh-cn/GIMP.html> "GIMP")** — 一款图片编辑器。

     <https://www.gimp.org> || [gimp](<https://archlinux.org/packages/?name=gimp>)包

  * **[GnuCash](<https://en.wikipedia.org/wiki/GnuCash> "wikipedia:GnuCash")** — 一个会计程序。

     <https://www.gnucash.org/> || [gnucash](<https://archlinux.org/packages/?name=gnucash>)包

  * **GNU Go** — 一个玩围棋的自由软件。

     <https://www.gnu.org/software/gnugo/> || [gnugo](<https://archlinux.org/packages/?name=gnugo>)包

  * **[GNU Guix](<../zh-cn/GNU_Guix.html> "GNU Guix")** — 一个独立的软件包管理器。

     <https://guix.gnu.org/> || [guix](<https://aur.archlinux.org/packages/guix/>)AUR 或 [guix-installer](<https://aur.archlinux.org/packages/guix-installer/>)AUR

  * **[Gnumeric](<../zh-cn/Gnumeric.html> "Gnumeric")** — 一款表格处理软件。

     <http://www.gnumeric.org> || [gnumeric](<https://archlinux.org/packages/?name=gnumeric>)包

  * **[GnuPG](<../zh-cn/GnuPG.html> "GnuPG")** — 一款 OpenPGP 实现。

     <https://www.gnupg.org> || [gnupg](<https://archlinux.org/packages/?name=gnupg>)包

  * **Hello** — 打印 “Hello World” 等内容。

     <https://www.gnu.org/software/hello/> || [hello](<https://aur.archlinux.org/packages/hello/>)AUR

  * **[Indent](<https://en.wikipedia.org/wiki/Indent_\(Unix\)#GNU_Indent> "wikipedia:Indent \(Unix\)")** — 一款 C 语言代码格式化工具。

     <https://www.gnu.org/software/indent> || [indent](<https://archlinux.org/packages/?name=indent>)包

  * **Jami** — 一款分布式会议软件。

     <https://jami.net> || [jami-qt](<https://archlinux.org/packages/?name=jami-qt>)包, [jami-daemon](<https://archlinux.org/packages/?name=jami-daemon>)包

  * **[LilyPond](<../zh-cn/LilyPond.html> "LilyPond")** — 一款基于文本输入的制谱软件。

     <https://lilypond.org> || [lilypond](<https://archlinux.org/packages/?name=lilypond>)包

  * **[Mailman](<../zh-cn/Mailman.html> "Mailman")** — 一款用来管理电子邮件讨论和邮件列表的软件。

     <https://www.list.org> || [mailman3](<https://archlinux.org/packages/?name=mailman3>)包

  * **[Midnight Commander](<../zh-cn/Midnight_Commander.html> "Midnight Commander")** — 一款双窗格终端文件管理器。

     <https://midnight-commander.org> || [mc](<https://archlinux.org/packages/?name=mc>)包

  * **[nano](<../zh-cn/Nano.html> "Nano")** — 一个命令行文本编辑器。

     <https://www.nano-editor.org> || [nano](<https://archlinux.org/packages/?name=nano>)包

  * **[Ocrad](<https://en.wikipedia.org/wiki/Ocrad> "wikipedia:Ocrad")** — 一款OCR(光学字符识别)文字识别的实用程序和库。

     <https://www.gnu.org/software/ocrad> || [ocrad](<https://archlinux.org/packages/?name=ocrad>)包

  * **[Octave](<../zh-cn/Octave.html> "Octave")** — 一种科学编程语言。

     <https://octave.org> || [octave](<https://archlinux.org/packages/?name=octave>)包

  * **[Parted](<../zh-cn/Parted.html> "Parted")** — 一个分区管理器。

     <https://www.gnu.org/software/parted> || [parted](<https://archlinux.org/packages/?name=parted>)包

  * **[plotutils](<https://en.wikipedia.org/wiki/plotutils> "wikipedia:plotutils")** — 一套用于绘图的工具和库。

     <https://www.gnu.org/software/plotutils> || [plotutils](<https://archlinux.org/packages/?name=plotutils>)包

  * **[Readline](<../zh-cn/Readline.html> "Readline")** — 一个用于命令行界面的行编辑库。

     <https://tiswww.cwru.edu/php/chet/readline/rltop.html> || [readline](<https://archlinux.org/packages/?name=readline>)包

  * **[Screen](<../zh-cn/GNU_Screen.html> "GNU Screen")** — 一个终端多路复用器。

     <https://www.gnu.org/software/screen> || [screen](<https://archlinux.org/packages/?name=screen>)包

  * **Stow** — 在同一目录树中管理多个软件的安装。

     <https://www.gnu.org/software/stow> || [stow](<https://archlinux.org/packages/?name=stow>)包

  * **[Units](<https://en.wikipedia.org/wiki/GNU_Units> "wikipedia:GNU Units")** — 在不同单位之间进行转换。

     <https://www.gnu.org/software/units> || [units](<https://aur.archlinux.org/packages/units/>)AUR

  * **[Wget](<../zh-cn/Wget.html> "Wget")** — 一款网络下载工具。

     <https://www.gnu.org/software/wget> || [wget](<https://archlinux.org/packages/?name=wget>)包

  * **Zile** — emacs 的轻量级克隆。

     <https://www.gnu.org/software/zile> || [zile](<https://aur.archlinux.org/packages/zile/>)AUR

##  参见

  * <https://www.gnu.org/>
  * [The GNU Manifesto](<https://www.gnu.org/gnu/manifesto>)
  * [Wikipedia:List of GNU packages](<https://en.wikipedia.org/wiki/List_of_GNU_packages> "wikipedia:List of GNU packages")
  * [GNU 软件包基本信息](<https://directory.fsf.org/wiki/GNU/>)
  * [Arch Hurd Project](<https://archhurd.org/>) 致力于将 _Arch Linux_ 移植到 Hurd 内核（目前维护不积极）。
  * Mu Lei 所著《[Hurd, seL4, thoughts](<https://nalaginrut.com/archives/2019/12/11/hurd%2c%20sel4%2c%20thoughts>)》
