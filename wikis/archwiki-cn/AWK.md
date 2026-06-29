**翻译状态：**

  * 本文（或部分内容）译自 [AWK](<https://wiki.archlinux.org/title/AWK> "arch:AWK")，最近一次同步于 2025-03-05，若英文版本有所[更改](<https://wiki.archlinux.org/title/AWK?diff=0&oldid=828301>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/AWK_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[AWK](<https://en.wikipedia.org/wiki/AWK> "wikipedia:AWK") 是一种用于文本处理的小型编程语言。其名称源于作者的姓氏：Alfred Aho、Peter Weinberger 和 Brian Kernighan。该语言[已经标准化，在类 Unix 系统上广泛使用](<https://lwn.net/Articles/820829/>)。 

##  安装

在 Arch 上，[awk(1p)](<https://man.archlinux.org/man/awk.1p>) 命令由 [gawk](<https://archlinux.org/packages/?name=gawk>)包 提供。[gawk](<https://archlinux.org/packages/?name=gawk>)包 是[默认安装](<../zh-cn/%E5%85%83%E8%BD%AF%E4%BB%B6%E5%8C%85%E5%92%8C%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%BB%84.html> "元软件包")，支持本地 Unicode，并具有大量[额外](<https://www.gnu.org/software/gawk/manual/html_node/POSIX_002fGNU.html>)[功能](<https://www.gnu.org/software/gawk/manual/html_node/Advanced-Features.html#Part-III_003a-Moving-Beyond-Standard-awk-with-gawk>)。 

**注意：**[gawk](<https://archlinux.org/packages/?name=gawk>)包旨在通过动态加载所谓的 _扩展_ ，在运行时获得额外的语言功能——[捆绑在软件发行版中的](<https://www.gnu.org/software/gawk/manual/html_node/Extension-Samples.html>)扩展是开箱即用的，但单独维护的 [gawkextlib](<https://aur.archlinux.org/packages/gawkextlib/>)AUR-* 插件则需要手动安装。

###  替代方案

与许多其他[核心工具](<../zh-cn/%E6%A0%B8%E5%BF%83%E5%B7%A5%E5%85%B7.html> "核心工具")一样，有几种或多或少符合要求的[实现](<https://www.gnu.org/software/gawk/manual/html_node/Other-Versions.html>)可供使用： 

  * **[BusyBox](<../zh-cn/BusyBox.html> "BusyBox")** — BusyBox 实现的性能不是很好，但占用空间较小，适合内存紧张的环境。

     <https://git.busybox.net/busybox/tree/editors/awk.c> || [busybox](<https://archlinux.org/packages/?name=busybox>)包

  * **GoAWK** — 用 Go 语言实现的 AWK

     <https://github.com/benhoyt/goawk> || [goawk](<https://aur.archlinux.org/packages/goawk/>)AUR

  * **nawk** — _AWK 编程语言_ 中描述的"新" AWK，又名 BWK AWK 或 One-True-AWK，现由 Arnold Robbins 和 B. W. Kernighan 共同维护，支持 UTF-8 和 csv。

     <https://awk.dev/> || [nawk](<https://archlinux.org/packages/?name=nawk>)包

  * **mawk** — 性能相当出色的 AWK 实现。

     <https://invisible-island.net/mawk/> || [mawk](<https://aur.archlinux.org/packages/mawk/>)AUR

##  疑难解答

###  通过 `-v` 选项为 `ARGC` 变量赋值不会在运行时保留

尽管没有文档说明，[[1]](<https://groups.google.com/g/comp.lang.awk/c/WDFnplISdgw/>)但许多实现在处理完命令行指定的 `-v` 选项的变量赋值后，似乎会在内部重置 `ARGC` 变量。因此，要在运行时（例如 `BEGIN` 代码块）获得 `ARGC` 变量的预期值，需要直接在代码块中设置该变量： 
    
    BEGIN {
      ARGC=1;
      ...
    }
    
**注意：** 即将更新的 POSIX [专门记录了这个问题](<https://austingroupbugs.net/view.php?id=974#c3231>)。

##  参见

  * [nawk(1)](<https://man.archlinux.org/man/nawk.1>): [nawk](<https://archlinux.org/packages/?name=nawk>)包的参考卡式手册页面
  * [Gawk: Effective AWK Programming](<https://www.gnu.org/software/gawk/manual/>)[GNU 文档](<https://www.gnu.org/manual/manual.html>)

：[gawk(1)](<https://man.archlinux.org/man/gawk.1>) 的综合教程和典型参考文献 

  * [Alpine Linux's community wiki article on AWK](<https://wiki.alpinelinux.org/wiki/Awk>): 有一些关于 BusyBox 和其他 AWK 实现差异的说明
  * [AWK tech notes](<https://maximullaris.com/awk_tech_notes.html>)：语言的缺陷以及与其他现代编程语言相比在设计上的差异
  * [Idiomatic AWK](<https://backreference.org/category/awk/>)：AWK 程序可以多么简洁
