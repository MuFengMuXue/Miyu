**翻译状态：**

  * 本文（或部分内容）译自 [Clojure](<https://wiki.archlinux.org/title/Clojure> "arch:Clojure")，最近一次同步于 2020-06-30，若英文版本有所[更改](<https://wiki.archlinux.org/title/Clojure?diff=0&oldid=611297>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Clojure_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Clojure](<https://clojure.org/>) 是 Lisp 的方言，它是一种针对 [Java](<../zh-cn/Java.html> "Java") 虚拟机，[CLR](<https://clojure.org/about/clojureclr>) 和 [JavaScript](<https://clojurescript.org/>) 的动态，功能齐全的通用编程语言。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [clojure](<https://archlinux.org/packages/?name=clojure>)包 包，或安装 [clojure-git](<https://aur.archlinux.org/packages/clojure-git/>)AUR 开发版本。 

## REPL

要运行 REPL，请从 [leiningen](<https://archlinux.org/packages/?name=leiningen>)包 安装 [leiningen](<https://leiningen.org/>)。然后在终端运行 
    
    lein repl
    
###  m2 仓库路径

要配置本地 m2 仓库路径，请修改 profiles.clj： 
    
    {:user {:local-repo #=(eval (str (System/getenv "XDG_CACHE_HOME") "/m2"))
            :repositories  {"local" {:url #=(eval (str "file://" (System/getenv "XDG_DATA_HOME") "/m2"))
                                     :releases {:checksum :ignore}}}
            }}
    
##  参见

  * [Wikipedia:Clojure](<https://en.wikipedia.org/wiki/Clojure> "wikipedia:Clojure")
