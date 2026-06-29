**翻译状态：**

  * 本文（或部分内容）译自 [Mosh](<https://wiki.archlinux.org/title/Mosh> "arch:Mosh")，最近一次同步于 2020-07-23，若英文版本有所[更改](<https://wiki.archlinux.org/title/Mosh?diff=0&oldid=626386>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Mosh_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Mosh](<https://mosh.org/>) 是另一种交互式 [SSH](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH") 终端。它支持漫游和本地回显。它还旨在提高对间歇性和高延迟连接的响应能力。请注意，真彩色支持仅在后者中提供。 

##  安装

**注意：** Mosh 必须同时安装在服务器和客户端上。

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [mosh](<https://archlinux.org/packages/?name=mosh>)包 包，或安装 [mosh-git](<https://aur.archlinux.org/packages/mosh-git/>)AUR 以获得最新版本。 

##  用法

**注意：** Mosh 设计不允许您访问会话历史记录，请考虑安装终端多路复用器，例如 [tmux](<../zh-cn/Tmux.html> "Tmux") 或 [GNU Screen](<../zh-cn/GNU_Screen.html> "GNU Screen")。

要进行连接，请运行： 
    
    $ mosh _user@server-address_
    
发送 ssh 连接选项： 
    
    $ mosh --ssh="ssh -p 2222" _user@server-address_
    
您可以使用通常的 [OpenSSH Client Configuration](<../zh-cn/OpenSSH.html#Configuration> "OpenSSH") 来使选项永久化。 

**注意：** Mosh 有一个未公开的命令行选项 `--predict=experimental`，它可以更积极地响应本地击键。 对键盘输入的低延迟视觉确认感兴趣的用户可能更喜欢此预测模式。
