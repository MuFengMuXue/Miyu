**翻译状态：**

  * 本文（或部分内容）译自 [Erlang](<https://wiki.archlinux.org/title/Erlang> "arch:Erlang")，最近一次同步于 2025-07-14，若英文版本有所[更改](<https://wiki.archlinux.org/title/Erlang?diff=0&oldid=799966>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Erlang_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[应用程序列表](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8.html> "应用程序列表")。**

**附注：** 内容不足以单独成文（在 [Talk:Erlang](<../zh-cn/Talk:Erlang.html>) 中讨论）

[Erlang](<https://www.erlang.org/>) 是一种具有不可变数据和分布式计算特性的编程语言。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [erlang](<https://archlinux.org/packages/?name=erlang>)包 软件包。 

##  用法

有关更多信息，您可以阅读 [Erlang 的文档](<https://erlang.org/doc/getting_started/intro.html>)。 

要激活控制台，运行 ： 
    
    $ erl
    
您可以在其中输入如下命令： 
    
    Erlang/OTP 22 [erts-10.7.2] [source] [64-bit] [smp:4:4] [ds:4:4:10] [async-threads:1] [hipe]
    Eshell V10.7.2  (abort with ^G)
    1> 1 + 2 .
    3
    2> (2 + 3) * 4 / 5 .
    4.0
    3>
    
##  提示和技巧

###  Emacs 模式

要设置包含的 [Emacs](<../zh-cn/Emacs.html> "Emacs") 模式， `erlang-mode` ，请遵循[文档](<https://erlang.org/doc/apps/tools/erlang_mode_chapter.html#setup-on-unix>)（OTP 路径为 `/usr/lib/erlang`）。 
