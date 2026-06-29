**翻译状态：**

  * 本文（或部分内容）译自 [Common Lisp](<https://wiki.archlinux.org/title/Common_Lisp> "arch:Common Lisp")，最近一次同步于 2024-07-30，若英文版本有所[更改](<https://wiki.archlinux.org/title/Common_Lisp?diff=0&oldid=813387>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Common_Lisp_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Common Lisp](<https://common-lisp.net/>) 是一种高度动态的多范例语言，强调交互性和性能。完全标准化后，其有许多独立的实现可供选择。 

##  安装

[sbcl](<https://archlinux.org/packages/?name=sbcl>)包 (<http://www.sbcl.org/>) 是最受欢迎的 FOSS 实现，总体跨软件生态[兼容度](<https://portability.cl/>)最高。其编译器可生成原生的机器码。该项目每月发布更新。 

配置文件是 `~/.sbclrc`，使用 Lisp 语言编写。但是，基于您选择的依赖管理策略，您可能用不上它。 

###  替代实现

有许多可用的替代实现。除下述外，有两大商用 Lisp 实现：Allegro 和 LispWorks，但它们附有严格的许可条款，也未打包到 Arch Linux 生态中。 

####  活跃

这些功能与现代工具可无缝配合，可用于大型项目。 

  * **[ABCL](<https://en.wikipedia.org/wiki/Common_Lisp#List_of_implementations> "wikipedia:Common Lisp")** — Armed Bear Common Lisp：在 Java 虚拟机上运行。

     <https://common-lisp.net/project/armedbear/> || [abcl](<https://aur.archlinux.org/packages/abcl/>)AUR

  * **[CCL](<https://en.wikipedia.org/wiki/Clozure_CL> "wikipedia:Clozure CL")** — Clozure Common Lisp：基于 Open Machintosh Common Lisp，以极快的编译速度闻名。

     <https://ccl.clozure.com/> || [ccl](<https://aur.archlinux.org/packages/ccl/>)AUR

  * **[Clasp](<https://en.wikipedia.org/wiki/Common_Lisp#List_of_implementations> "wikipedia:Common Lisp")** — Clasp：一种较新的 Common Lisp 实现，可与 C++ 库互操作，并借助 LLVM 编译至机器码。

     <https://clasp-developers.github.io/> || [clasp-cl](<https://aur.archlinux.org/packages/clasp-cl/>)AUR

  * **[ECL](<https://en.wikipedia.org/wiki/Embeddable_Common_Lisp> "wikipedia:Embeddable Common Lisp")** — Embeddable Common Lisp：可编译至 C 代码，从而提供良好的 C 集成和嵌入性。

     <https://common-lisp.net/project/ecl/> || [ecl](<https://archlinux.org/packages/?name=ecl>)包

####  历史

尽管有相应软件包，但库和工具的兼容性令人怀疑，而且有些实现已不再受到积极维护。 

  * **[CLISP](<https://en.wikipedia.org/wiki/CLISP> "wikipedia:CLISP")** — ANSI Common Lisp 解释器、编译器及调试器：提供良好的 C 集成和嵌入性。

     <https://www.gnu.org/software/clisp/> || [clisp](<https://archlinux.org/packages/?name=clisp>)包

  * **[CMUCL](<https://en.wikipedia.org/wiki/CMU_Common_Lisp> "wikipedia:CMU Common Lisp")** — CMU Common Lisp：一个仅 POSIX 的实现，最初在卡内基梅隆大学开发。

     <https://gitlab.common-lisp.net/cmucl/cmucl/-/wikis/home> || [cmucl](<https://archlinux.org/packages/?name=cmucl>)包

  * **[GCL](<https://en.wikipedia.org/wiki/GNU_Common_Lisp> "wikipedia:GNU Common Lisp")** — GNU Common Lisp：80 年代 Kyoto Common Lisp 的后代，ECL 的兄弟。

     <https://www.gnu.org/software/gcl/> || [gcl](<https://aur.archlinux.org/packages/gcl/>)AUR

  * **MKCL** — Mankai Common Lisp：也是 Kyoto Common Lisp 的后代。

     <https://mkcl.common-lisp.dev/> || [mkcl-git](<https://aur.archlinux.org/packages/mkcl-git/>)AUR

##  依赖管理

### Quicklisp

[Quicklisp](<https://www.quicklisp.org/beta/>) 是这样一个系统：获取库，并将其加载到 Common Lisp 程序中。默认情况下，本机所有程序共用单一全局软件包缓存。而且，Quicklisp 从一个保守更新的仓库中提取软件包，该仓库也叫做 Quicklisp（可能引起混淆）。 

安装 [quicklisp](<https://archlinux.org/packages/?name=quicklisp>)包 包后，可通过以下方式，将其作为一个特定编译器注册： 
    
    > sbcl --load /usr/share/quicklisp/quicklisp.lisp
    * (quicklisp-quickstart:install)
    * (ql:add-to-init-file)
    
在此之后，可以在以后所有的 REPL 会话中使用 `(ql:quickload "foo")` 来加载一个依赖项，必要时会下载该依赖项。 

要更新通过 Quicklisp 安装的所有包，在 REPL 中运行以下命令： 
    
    (ql:update-all-dists)
    
**注意：** 一般来说，Quicklisp 假定您创建的所有 Common Lisp 项目都在 `~/common-lisp/` 目录下。

#### Ultralisp

[Ultralisp](<https://ultralisp.org/>) 是一个替代 Quicklisp 的仓库，提供所有包的滚动更新，原则上与 Github 最新发布保持一致。 

要将其注册，在 REPL 中运行： 
    
    (ql-dist:install-dist "http://dist.ultralisp.org/" :prompt nil)
    
如果您 `ql:quickload` 的包在 Ultralisp 中有较新版本，该包将从 Ultralisp 而非 Quicklisp 加载。 

### Qlot

或者，若您需要项目本地依赖，可以采用 [Qlot](<https://github.com/fukamachi/qlot>) ([qlot](<https://aur.archlinux.org/packages/qlot/>)AUR)。 

安装后，项目仓库可以通过以下命令初始化： 
    
    qlot init
    
####  自定义依赖

使用 Qlot、所有自定义依赖的位置都记录在 `qlfile` 中。例如，要声明使用 Ultralisp，只需添加： 
    
    dist http://dist.ultralisp.org
    
或指定本地依赖： 
    
    local foobar /home/you/code/common-lisp/foobar
    
参见 Qlot 的 README 以了解更多选项。 

要安装已经声明的依赖，运行： 
    
    qlot install
    
####  启用 REPL

要在当前 Qlot 环境中加载 REPL，请运行： 
    
    qlot exec sbcl
    
使用 Sly/Slime 的 Emacs 用户，考虑这样配置编辑器内 REPL 的启动方式： 
    
    (setq sly-default-lisp 'qlot-sbcl
          sly-lisp-implementations '((qlot-sbcl ("qlot" "exec" "sbcl") :coding-system utf-8-unix)))
    
Slime 类似，进行必要的调整即可。 

##  开发环境

### Emacs

Common Lisp 开发常常通过 Emacs 完成：借助 [slime](</wzh/index.php?title=Slime&action=edit&redlink=1> "Slime（页面不存在）") 或较新的 [sly](<https://joaotavora.github.io/sly>)。两者都被社区广泛采用且使用方法类似。 

### Lem

[Lem](<https://lem-project.github.io/>) ([lem-editor-git](<https://aur.archlinux.org/packages/lem-editor-git/>)AUR) 是一个较新的 Emacs 风格编辑器，但是完全由 Common Lisp 编写和配置。其拥有终端和图形化前端，并支持许多语言。 

##  提示

###  管理 Init 文件

库的作者经常使用多个编译器实现来测试他们的代码。但是，每个实现都有各自不同的 init 文件，例如 `.sbclrc` 或 `.eclrc`。但这些文件的内容往往是相同的：与其为每个编译器手写这些文件，不如创建一个主文件，并将其他文件链接到该文件。例如，如果您考虑 `.sbclrc` 成为您的 "主配置"，然后： 
    
    ln -s /home/you/.sbclrc .eclrc
    ln -s /home/you/.sbclrc .abclrc
    
等等。这些主要 init 文件是： 
    
    ~/.sbclrc          # for SBCL
    ~/.abclrc          # for ABCL
    ~/.ccl-init.lisp   # for CCL
    ~/.clasprc         # for CLASP
    ~/.eclrc           # for ECL
    ~/.clisprc.lisp    # for CLISP
    ~/.cmucl-init.lisp # for CMUCL
    ~/.mkclrc          # for MKCL
    ~/.clinit.cl       # for Allegro
    
##  疑难解答

###  Quicklisp 不能加载本地项目

`(ql:quickload "...")` 用于加载外部依赖项和本地项目。但若本地项目不位于 `~/common-lisp/`，将无法加载。项目甚至可能被从在线平台上删除，如果已经发布。 

实际上，Quicklisp 只是获取和整理软件包。它内部使用 ASDF 构建系统，以实际加载这些包。也可以通过 `(asdf：load-system "foo")`，默认情况下，ASDF 只在 `~/common-lisp/` 中寻找本地项目。 

虽然可以配置，但更简单的方法是使用符号链接： 
    
    ln -s /home/you/code/common-lisp/ common-lisp
    
**注意：** 如果使用 Qlot，则不需要上述符号链接。只要您执行 `qlot install`，然后 `(asdf：load-package "foo")` 即可。

###  什么是项目、系统、软件包？

本文其余部分使用的“包”一词是其他编程语言通常使用的“库 ”的同义词。不过，虽然 Common Lisp 在 90 年代中期就已标准化，但其最早的形式却是在 80 年代出现的，因此涉及项目管理的术语也有所不同。实质上： 

  * 项目：一组系统。有时在其他语言中被称为“命名空间”。
  * 系统：一组包。既可代表库，也可代表 “可执行文件”。
  * 软件包：一组函数和类型定义。在其他语言中通常称为“模块”，但可跨多个文件。

如您所见，在其他地方通常被称为库的东西，在 Common Lisp 中被称为“系统”。因此有 `asdf:load-system` 的命名。[参见此处](<https://codeberg.org/fosskers/cl-transducers/src/commit/5df2f4b7c66ea4bd8f607e6900f9bdedd7e58061/transducers.asd>)以获得相互依赖、多系统项目的一个例子。 

##  参见

  * [The Common Lisp 使用手册](<https://lispcookbook.github.io/cl-cookbook/>)：许多问题的解决方法。
  * [社区规范](<https://cl-community-spec.github.io/pages/index.html>)：在线 stdlib 文档。
  * [Awesome CL](<https://github.com/CodyReichert/awesome-cl>)：生态概览。
  * [Quickdocs](<https://quickdocs.org/>)：Quicklisp 文档查询。
  * [Portability](<https://portability.cl/>)：编译器实现的兼容性列表。
  * [Wikipedia:Common Lisp](<https://en.wikipedia.org/wiki/Common_Lisp> "wikipedia:Common Lisp")
  * [Cliki：Common Lisp 维基](<https://cliki.net>)
