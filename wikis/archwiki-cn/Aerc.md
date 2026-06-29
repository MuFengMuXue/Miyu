**翻译状态：**

  * 本文（或部分内容）译自 [Aerc](<https://wiki.archlinux.org/title/Aerc> "arch:Aerc")，最近一次同步于 2024-7-30，若英文版本有所[更改](<https://wiki.archlinux.org/title/Aerc?diff=0&oldid=813253>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Aerc_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[aerc](<https://aerc-mail.org/>) 是一款基于终端的电子邮件客户端，具有 [Vim](<../zh-cn/Vim.html> "Vim") 风格的按键绑定和 ex-command 系统。它使用嵌入式模板，允许使用任何终端编辑器作为嵌入式组件来撰写电子邮件。 _aerc_ 内置了 IMAP 和 SMTP 支持，还支持 Maildir 和 [Notmuch](<../zh-cn/Notmuch.html> "Notmuch")。虽然 _aerc_ 提供了一个简单的向导来设置电子邮件账户，但完整的配置是通过 `$XDG_CONFIG_HOME/aerc` 中的文本文件来处理的。 

_aerc_ 是用 [Go](<../zh-cn/Go.html> "Go") 编写的，终端用户界面使用 [Tcell](<https://github.com/gdamore/tcell>) 软件包。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [aerc](<https://archlinux.org/packages/?name=aerc>)包 软件包。 

##  提示与技巧

###  使 Khard 作为通讯录提供者

[khard](<https://archlinux.org/packages/?name=khard>)包 可被配置为通讯录提供程序[[1]](<https://ewintr.nl/devnotes/2020/address-book-in-aerc-with-khard/>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2024-07-30 ⓘ]： 
    
    $XDG_CONFIG_HOME/aerc/aerc.conf
    
    [compose]
    address-book-cmd=khard email --parsable --remove-first-line %s

##  参见

  * [aerc 官方网站](<https://aerc-mail.org/>)
  * [aerc 仓库](<https://git.sr.ht/~rjarry/aerc>)
  * [aerc Wiki](<https://man.sr.ht/~rjarry/aerc>)
