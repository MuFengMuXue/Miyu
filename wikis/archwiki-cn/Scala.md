**翻译状态：**

  * 本文（或部分内容）译自 [Scala](<https://wiki.archlinux.org/title/Scala> "arch:Scala")，最近一次同步于 2021-01-29，若英文版本有所[更改](<https://wiki.archlinux.org/title/Scala?diff=0&oldid=709967>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Scala_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Java](<../zh-cn/Java.html> "Java")

From [Wikipedia](<https://en.wikipedia.org/wiki/Scala_\(programming_language\)> "wikipedia:Scala \(programming language\)"): 

    _Scala is an object-functional programming and scripting language for general software applications. Scala has full support for functional programming (including currying, pattern matching, algebraic data types, lazy evaluation, tail recursion, immutability, etc.) and a very strong static type system. This allows programs written in Scala to be very concise and thus smaller in size than most general purpose programming languages. Many of Scala's design decisions were inspired by criticism over the shortcomings of Java._

##  安装

从 [official repositories](<../zh-cn/Official_repositories.html> "Official repositories") 中[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [scala](<https://archlinux.org/packages/?name=scala>)包。此外您也可以选择安装 [scala-docs](<https://archlinux.org/packages/?name=scala-docs>)包 和 [scala-sources](<https://archlinux.org/packages/?name=scala-sources>)包 。 

因为 scala 运行在 [JVM](<https://en.wikipedia.org/wiki/JVM> "wikipedia:JVM") (Java Virtual Machine) 上，所以为了编译和运行 scala 程序，您也需要一个完整的 [Java Runtime Environment](<../zh-cn/Java.html#Installation> "Java") (JRE)。 

对于 scala3 (也被称作 [dotty](<https://dotty.epfl.ch>)), 您可以从 AUR 中安装 [scala3](<https://aur.archlinux.org/packages/scala3/>)AUR 或者 [scala-dotty](<https://aur.archlinux.org/packages/scala-dotty/>)AUR。 请注意 scala3 **不兼容** scala 2.13 及更早版本. 

###  构建工具

多数构建工具可以在官方 community 仓库中安装: 

  * [sbt](<https://archlinux.org/packages/?name=sbt>)包
  * [maven](<https://archlinux.org/packages/?name=maven>)包
  * [gradle](<https://archlinux.org/packages/?name=gradle>)包

##  使用和 IDE

像 [Python](<../zh-cn/Python.html> "Python") 等语言一样, 您可以在解释器中运行交互程序。 
    
    $ scala
    
    Welcome to Scala version 2.*.* (OpenJDK Server VM, Java 1.*.*).
    Type in expressions to have them evaluated.
    Type :help for more information.
    
    scala>
    
也可以简单地从命令行编译并运行程序。 
    
    $ scalac HelloWorld.scala
    $ scala HelloWorld
    
许多不同的 [IDE](</wzh/index.php?title=IDE&action=edit&redlink=1> "IDE（页面不存在）") 例如 [Eclipse](<../zh-cn/Eclipse.html> "Eclipse") 和 [Netbeans](</wzh/index.php?title=Netbeans&action=edit&redlink=1> "Netbeans（页面不存在）") 都提供 scala 支持。 [scala-ide](<https://aur.archlinux.org/packages/scala-ide/>)AUR package for example is available in the [AUR](<../zh-cn/Arch_%E7%94%A8%E6%88%B7%E8%BD%AF%E4%BB%B6%E4%BB%93%E5%BA%93.html> "AUR"). But you can also download an IDE that is optimized for Scala and also based on Eclipse directly from [the official Scala Website](<https://scala-lang.org>). 

##  参见

  * [Scala Lang](<https://scala-lang.org>) \- 官方网站
  * [Scala Tutorial](<http://tutorials.jenkov.com/scala/index.html>) \- 一系列小型 scala 入门教程
  * [Learn X=Scala in Y minutes](<https://learnxinyminutes.com/docs/scala/>)
