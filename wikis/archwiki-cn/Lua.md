**翻译状态：**

  * 本文（或部分内容）译自 [Lua](<https://wiki.archlinux.org/title/Lua> "arch:Lua")，最近一次同步于 2022-06-05，若英文版本有所[更改](<https://wiki.archlinux.org/title/Lua?diff=0&oldid=687585>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Lua_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

根据其自己的网站 [lua.org](<https://www.lua.org/about.html>)： 

    Lua 是一种功能强大，高效，轻巧，可嵌入的脚本语言。

这也使 Lua 非常适合配置和扩展其他程序，这也是因为它与 [C](<../zh-cn/C.html> "C") 的互操作性强。 基本的 Lua 解释器的大小小于 250K。由于官方实现是用 [ANSI C](<https://en.wikipedia.org/wiki/ANSI_C> "wikipedia:ANSI C") 编写的，因此可用于许多平台和体系结构。 

##  安装

有多个版本可用： 

  * [lua](<https://archlinux.org/packages/?name=lua>)包——Lua 5.4
  * [lua53](<https://archlinux.org/packages/?name=lua53>)包——Lua 5.3
  * [lua52](<https://archlinux.org/packages/?name=lua52>)包——Lua 5.2
  * [lua51](<https://archlinux.org/packages/?name=lua51>)包——Lua 5.1

##  JIT 编译支持

[即时编译](<https://en.wikipedia.org/wiki/Just-in-time_compilation> "wikipedia:Just-in-time compilation")（Just-in-time compilation）是一种在运行时而不是之前编译源代码的方法。[LuaJIT](<https://luajit.org/>) 是 Lua 5.1 的直接替代品。此版本最适合更高性能的约束。 

为了获得 JIT 编译支持，请[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [luajit](<https://archlinux.org/packages/?name=luajit>)包 软件包。 

##  模块

[LuaRocks](<https://luarocks.org/>) 软件包管理器作为 [luarocks](<https://archlinux.org/packages/?name=luarocks>)包 提供。 

[官方存储库](<https://archlinux.org/packages/?&q=lua->)中也提供了一些模块。 

##  参见

  * [Lua 参考手册](<https://www.lua.org/manual/>)。
