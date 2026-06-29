**翻译状态：**

  * 本文（或部分内容）译自 [Oil Shell](<https://wiki.archlinux.org/title/Oil_Shell> "arch:Oil Shell")，最近一次同步于 2024/01/27，若英文版本有所[更改](<https://wiki.archlinux.org/title/Oil_Shell?diff=0&oldid=792497>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Oil_Shell_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

**Oil Shell** (OSH) 是一个兼容 Bash 的 UNIX [命令行 shell](<../zh-cn/Command-line_shell.html> "Command-line shell")。OSH 可以在大多数类 UNIX 的操作系统上运行，包括 GNU/Linux。它是用 Python (v2.7) 编写的，但有本地可执行程序。OSH 所支持的 Bash 方言被称为 OSH 语言。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [oil](<https://archlinux.org/packages/?name=oil>)包 包。 

###  冒烟测试

通过在终端中运行以下命令，确保 OSH 已正确安装： 
    
    $ osh
    
这将启动一个 OSH 会话并显示一个 shell 提示： 
    
    osh$
    
识别已安装的二进制文件并尝试在 OSH 会话中调用它以确认输出正确。 

例如： 
    
    osh$ ls
    ...
    
###  使 OSH 成为您的默认 shell

参见[命令行解释器#更改默认 Shell](<../zh-cn/%E5%91%BD%E4%BB%A4%E8%A1%8C%E8%A7%A3%E9%87%8A%E5%99%A8.html#%E6%9B%B4%E6%94%B9%E9%BB%98%E8%AE%A4_Shell> "命令行解释器")。 

##  卸载

参见[命令行解释器#卸载 Shell](<../zh-cn/%E5%91%BD%E4%BB%A4%E8%A1%8C%E8%A7%A3%E9%87%8A%E5%99%A8.html#%E5%8D%B8%E8%BD%BD_Shell> "命令行解释器")。 

##  疑难解答

可以在 [Github](<https://github.com/oilshell/oil/issues>) 上报告可重现的错误/问题。 提交报告时，请包括 OSH 在详细模式下运行时的输出。启用详细模式需要执行以下命令： 
    
    $> export OVM_VERBOSE=1
    
##  参见

  * [Oil Github](<https://github.com/oilshell/oil>)
  * [Oil 项目主页](<https://www.oilshell.org/>)
  * [Oil 推特提要](<https://twitter.com/oilshellblog>)
  * [Oil Subreddit](<https://www.reddit.com/r/oilshell/>)
