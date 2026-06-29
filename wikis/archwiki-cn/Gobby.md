**翻译状态：**

  * 本文（或部分内容）译自 [Gobby](<https://wiki.archlinux.org/title/Gobby> "arch:Gobby")，最近一次同步于 2024-08-23，若英文版本有所[更改](<https://wiki.archlinux.org/title/Gobby?diff=0&oldid=810365>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Gobby_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

从[项目网页](<https://gobby.github.io/>)： 

    Gobby is a collaborative editor supporting multiple documents in one session and a multi-user chat.

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [gobby](<https://archlinux.org/packages/?name=gobby>)包 包。 

要在没有 Gobby 前端的情况下运行 Infininote 服务器协议，请安装 [libinfinity](<https://archlinux.org/packages/?name=libinfinity>)包。 

##  Infininote 的用法

要启动服务器部分，请运行 
    
    $ infinoted-0.7 --security-policy=no-tls
    
该服务器只需要在一台计算机上运行。 

然后，运行 gobby 客户端并通过 IP 或 localhost 连接到服务器。 

如果您希望进行加密，则可以使用 TLS。使用： 
    
    $ infinoted-0.7 --create-key --create-certificate -k key.pem  -c cert.pem
    
密钥创建是自动的，您可以使用以下命令启动服务器： 
    
    $ infinoted-0.7 -k key.pem  -c cert.pem
    
##  参见

  * [Gooby GitHub wiki](<https://github.com/gobby/gobby/wiki>)
