**翻译状态：**

  * 本文（或部分内容）译自 [Scheme](<https://wiki.archlinux.org/title/Scheme> "arch:Scheme")，最近一次同步于 2025-04-14，若英文版本有所[更改](<https://wiki.archlinux.org/title/Scheme?diff=0&oldid=830768>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Scheme_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

根据 [Scheme.org](<https://www.scheme.org>)： 

    Scheme 是 [Lisp 语言家族](<../zh-cn/Category:Lisp_%E6%96%B9%E8%A8%80.html> "Category:Lisp 方言")中的经典编程语言。它强调[函数式编程](<https://en.wikipedia.org/wiki/Functional_programming> "wikipedia:Functional programming")和[领域特定语言（DSL）](<https://en.wikipedia.org/wiki/Metaprogramming> "wikipedia:Metaprogramming")，同时也能够适应其他编程风格。Scheme 以简洁而极简的设计著称，是最长寿且研究最为深入的[动态编程语言](<https://en.wikipedia.org/wiki/Dynamic_programming_language> "wikipedia:Dynamic programming language")之一，拥有众多快速且可移植的实现方案。

##  实现

  * **Bigloo** — 快速的 Scheme 编译器

     <https://www-sop.inria.fr/mimosa/fp/Bigloo/> || [bigloo](<https://archlinux.org/packages/?name=bigloo>)包

  * **Chez** — Chez Scheme 是针对 Revised^6 Report on Scheme (R6RS) 语言的编译器和运行时系统，具有许多扩展。

     <https://cisco.github.io/ChezScheme/> || [chez-scheme](<https://aur.archlinux.org/packages/chez-scheme/>)AUR

  * **CHICKEN** — 功能丰富的 R5RS/R7RS 编译器和解释器

     <https://call-cc.org/> || [chicken](<https://archlinux.org/packages/?name=chicken>)包

  * **Gambit Scheme** — 高效率的 Scheme 实现

     <https://gambitscheme.org/> || [gambit-c](<https://aur.archlinux.org/packages/gambit-c/>)AUR

  * **Gauche** — R7RS Scheme 实现（包含 gosh）

     <https://practical-scheme.net/gauche/> || [gauche](<https://aur.archlinux.org/packages/gauche/>)AUR

  * **GNU Guile** — 用 C 编写的可移植、可嵌入 Scheme 实现

     <https://www.gnu.org/software/guile/> || [guile](<https://archlinux.org/packages/?name=guile>)包、[guile2.0](<https://aur.archlinux.org/packages/guile2.0/>)AUR、[guile1.8](<https://aur.archlinux.org/packages/guile1.8/>)AUR

  * **Kawa** — 针对 JVM 的 Scheme 实现和框架

     <https://www.gnu.org/software/kawa/> || [kawa](<https://aur.archlinux.org/packages/kawa/>)AUR

  * **Larceny** — Larceny 是 Scheme 编程语言的一种简单有效的实现。

     <https://larcenists.org/> || [larceny-bin](<https://aur.archlinux.org/packages/larceny-bin/>)AUR

  * **MIT/GNU Scheme** — MIT/GNU Scheme

     <https://www.gnu.org/software/mit-scheme/> || [mit-scheme](<https://aur.archlinux.org/packages/mit-scheme/>)AUR

  * **Racket** — 使用 DrRacket IDE 的执行各种任务的语言。前身为 PLT Scheme。

     <https://racket-lang.org/> || [racket](<https://archlinux.org/packages/?name=racket>)包、[racket-minimal](<https://archlinux.org/packages/?name=racket-minimal>)包

  * **Scheme48** — 实验性的 Scheme 解释器。

     <https://s48.org/> || [scheme48](<https://aur.archlinux.org/packages/scheme48/>)AUR

##  包管理

[Akku.scm](<https://akkuscm.org/>) 是 Scheme 语言的一个包管理器。可通过[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [akku](<https://aur.archlinux.org/packages/akku/>)AUR 获取。 

##  开发

###  学习

  * Harold Abelson、Gerald Jay Sussman 与 Julie Sussman 所著的[《计算机程序的构造与解释（第二版）》](<https://sarabander.github.io/sicp/>)（1996）（另提供 [EPUB3](<https://github.com/sarabander/sicp-epub/blob/master/sicp.epub?raw=true>) 和 [PDF](<https://github.com/sarabander/sicp-pdf/raw/master/sicp.pdf>) 格式版本）
  * [Programming Languages: Application and Interpretation（PLAI）](<https://www.plai.org/>)，[lotuc](<https://github.com/lotuc>) 和 [MrMathematica](<https://github.com/mrmathematica>) 提供了[简体中文版本](<http://lotuc.org/PLAI-cn/>)。

###  语言服务器

[Scheme-langserver](<https://codeberg.org/ufo5260987423/scheme-langserver>) 是 Scheme 语言的语言服务器。可通过 [Akku.scm](<#Akku.scm>) 获取。 

参见 [Emacs-China 上的讨论](<https://emacs-china.org/t/scheme-langserver/28125>)。 

##  参见

  * [Scheme.org](<https://www.scheme.org/>)
  * [Scheme 语言标准](<https://standards.scheme.org/>)
  * [Scheme 实现提案（SRFI）](<https://srfi.schemers.org/>)
  * [Scheme 与 Common Lisp 的对比](<https://docs.scheme.org/guide/common-lisp/>)
