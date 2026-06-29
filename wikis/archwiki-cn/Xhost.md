**翻译状态：**

  * 本文（或部分内容）译自 [X server](<https://wiki.archlinux.org/title/X_server> "arch:X server")，最近一次同步于 2023-11-21，若英文版本有所[更改](<https://wiki.archlinux.org/title/X_server?diff=0&oldid=767005>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/X_server_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

来自Xhost man页面: 

    xhost程序用于将主机名或用户名添加和删除到允许连接到X服务器的列表中。就主机而言，其提供了一种基本的隐私控制和安全措施。请注意，**它只适用于工作站（单用户）环境** ,尽管它可以限制最严重的滥用行为。需要更复杂措施的环境应该实现基于用户的机制或使用协议中传递其他身份验证数据给服务器的钩子。

参见[xhost(1)](<https://man.archlinux.org/man/xhost.1>)。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")软件包 [xorg-xhost](<https://archlinux.org/packages/?name=xorg-xhost>)包 。 

##  使用方法

**警告：** 此命令将授予任何本地用户对你的X屏幕的访问权限。这在单用户环境上是可以被接受的，但是通常情况下不能在多用户环境下使用。如果你想保留root用户对X屏幕的访问权限，建议设置 `$XAUTHORITY` 环境变量。默认情况下这个变量由 _sudo_ 和 _su_ 保留(但不包括`su -`)。

为了让使用 _sudo_ 或 _su_ 运行的应用程序能够访问图形服务器(X屏幕/电脑屏幕)，在终端中以普通用户身份输入: 
    
    $ xhost +SI:localuser:_username_ 
    
要让一切恢复正常，并控制X屏幕的访问权限，输入以下命令: 
    
    $ xhost -
    
`xhost +` 将完全禁用X身份验证，除非你知道你在做什么，请**不要** 使用这个命令。 

##  提示"无法连接到X服务器:0.0"(cannot connect to X server :0.0)

**警告：** 此命令将会关闭访问控制，这意味着系统上的任何用户，或者网络上的任何用户(如果你打开了X服务器的网络监听)，都可以在没有任何认证的情况下访问你的`$DISPLAY`。这在你的系统上打开了一个安全漏洞，允许其他用户在你的X服务器上启动应用程序(例如键盘记录器)。

你可以使用`xhost +`暂时消除这个提示，或者(在众多方法中)，你也可以选择关闭访问认证来永久解决这个问题,将: 
    
    xhost + > /dev/null
    
添加到`~/.bashrc`文件中。这样每次启动终端都将自动执行该命令。如果在home文件夹中没有`.bashrc`文件请创建它。如果不在命令中添加`> /dev/null`,每次启动终端时你将会收到信息:_access control disabled, clients can connect from any host_(这是提示你将在root下运行任何软件)。 

##  另请参阅

  * [使用cookie和xhost进行X身份验证(错误:"未指定协议(No protocol specified)")](<https://github.com/mviereck/x11docker/wiki/X-authentication-with-cookies-and-xhost-\(%22No-protocol-specified%22-error\)#xhost>)
