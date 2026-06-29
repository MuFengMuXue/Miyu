**翻译状态：**

  * 本文（或部分内容）译自 [abduco](<https://wiki.archlinux.org/title/abduco> "arch:abduco")，最近一次同步于 2024-6-23，若英文版本有所[更改](<https://wiki.archlinux.org/title/abduco?diff=0&oldid=811140>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/abduco_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[abduco](<https://www.brain-dump.org/projects/abduco/>) 是一个轻量级工具，可让程序独立于控制终端运行。在这方面，它类似于 [tmux](<../zh-cn/Tmux.html> "Tmux") 和 [GNU Screen](<../zh-cn/GNU_Screen.html> "GNU Screen")，但它没有多路复用功能。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [abduco](<https://archlinux.org/packages/?name=abduco>)包 软件包。 

##  会话管理

要在名为 `_session_name_` 的会话中启动 `_command..._`（稍后可能会引用该会话），请运行 
    
    $ abduco -c _session_name_ _command..._
    
要退出进程，请按 `Ctrl+\` 或关闭控制终端。在这两种情况下，进程都将保持存活。 

要重新连接到 `_session_name_`，请运行 
    
    $ abduco -a _session_name_
    
在不带任何选项的情况下调用 `abduco` 会打印会话列表。 

##  限制

在 _abduco_ 会话中启动的进程会保留其调用的 `TERM` 变量。重新连接时，必须使用兼容的终端类型。 

_abduco_ 不提供多窗口和多路复用功能。如果需要，可使用 [dvtm](<https://www.brain-dump.org/projects/dvtm/>)、 _tmux_ 或 GNU Screen。 
