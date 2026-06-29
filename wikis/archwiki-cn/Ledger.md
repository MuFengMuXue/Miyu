**翻译状态：**

  * 本文（或部分内容）译自 [Ledger](<https://wiki.archlinux.org/title/Ledger> "arch:Ledger")，最近一次同步于 2024-08-08，若英文版本有所[更改](<https://wiki.archlinux.org/title/Ledger?diff=0&oldid=800443>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Ledger_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Ledger](<https://ledger-cli.org/>) 是一个可在命令行中使用的功能强大的复试记账软件。由John Wiegley自2003年起开始编写，并以BSD许可分发。 

##  安装

Ledger拥有多个基于不同语言的移植版本。安装以下版本之一： 

  * [ledger](<https://archlinux.org/packages/?name=ledger>)包：原始实现
  * [hledger](<https://archlinux.org/packages/?name=hledger>)包：一个移植到Haskell语言的分支，也广受欢迎。

##  使用

[在线文档](<https://www.ledger-cli.org/3.0/doc/ledger3.html>)中包含一个[教程](<https://www.ledger-cli.org/3.0/doc/ledger3.html#Ledger-Tutorial>)来帮助新用户快速上手。 

**提示：** 为了避免每次调用ledger时都需要输入`--file /path/to/finances.ledger`，考虑在[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")中设置`LEDGER_FILE`，或在`.ledgerrc`中添加一行`--file /path/to/finances.ledger`。

Emacs用户可能会对使用ledger-mode感兴趣。ledger-mode包含在MELPA中，并附带说明，可通过`C-h i m Ledger mode RET`进入。 

##  提示和技巧

###  在ledger格式转换过程中指定商品（Commodity，通常为货币)

默认情况下，在从csv文件转换到ledger格式时，ledger不会指定商品（Commodity）。当需要在货币缺失时指定一种，你可以将该货币设置为默认商品，只需在ledger文件中添加如下内容： 
    
    commodity $
      note US Dollar
      default
      nomarket
      format $1,000.00
