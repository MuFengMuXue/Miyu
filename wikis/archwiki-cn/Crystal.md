**翻译状态：**

  * 本文（或部分内容）译自 [Crystal](<https://wiki.archlinux.org/title/Crystal> "arch:Crystal")，最近一次同步于 2020-07-23，若英文版本有所[更改](<https://wiki.archlinux.org/title/Crystal?diff=0&oldid=626441>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Crystal_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Crystal](<https://en.wikipedia.org/wiki/Crystal_\(programming_language\)> "wikipedia:Crystal \(programming language\)") 是一种静态的编译型编程语言，具有受 [Ruby](<../zh-cn/Ruby.html> "Ruby") 启发的语法和全局类型推断。 

##  安装

要安装 Cryst，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [crystal](<https://archlinux.org/packages/?name=crystal>)包。要安装最新的开发版本，请安装 [crystal-git](<https://aur.archlinux.org/packages/crystal-git/>)AUR。 

##  用法

编译和运行 Crystal 程序： 
    
     $ crystal hello_world.cr
    
要将 Crystal 程序编译为二进制文件： 
    
     $ crystal build hello_world.cr
    
编译为优化的二进制文件： 
    
     $ crystal build --release hello_world.cr
    
有关更多选项，请参见： 
    
     $ crystal help
    
## Shards

仓库中也提供了依赖管理器 shards。要[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")它，请安装 [shards](<https://archlinux.org/packages/?name=shards>)包。要安装最新的开发版本，请安装 [shards-git](<https://aur.archlinux.org/packages/shards-git/>)AUR。 

##  参见

  * [官方网站](<https://crystal-lang.org>)
  * [官方文档](<https://crystal-lang.org/docs/>)
  * [标准库参考](<https://crystal-lang.org/api/>)
  * [官方 GitHub 仓库](<https://github.com/crystal-lang/crystal>)
  * [在线代码评估](<https://play.crystal-lang.org/#/cr>)
  * [#crystal-lang IRC 频道](<ircs://irc.libera.chat/crystal-lang>)
