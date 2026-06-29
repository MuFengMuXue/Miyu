**翻译状态：**

  * 本文（或部分内容）译自 [I2P](<https://wiki.archlinux.org/title/I2P> "arch:I2P")，最近一次同步于 2021-06-14，若英文版本有所[更改](<https://wiki.archlinux.org/title/I2P?diff=0&oldid=662914>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/I2P_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[I2P](<https://geti2p.net/en/about/intro>) 是一个动态的分布式匿名网络，它提供了一个简单的代理层帮助身份敏感的应用程序进行匿名通信。I2P 网络中不存在可信方，经过网络的数据将会被多层加密，很多在公网上可能威胁用户隐私的活动可以在 I2P 中匿名进行。许多支持 I2P 代理接口的应用程序都可用，包括邮件，P2P，IRC聊天等等。 

##  安装

安装使用 C++ 编写的客户端 [i2pd](<https://archlinux.org/packages/?name=i2pd>)包 （或开发版本 [i2pd-git](<https://aur.archlinux.org/packages/i2pd-git/>)AUR ），它可以适应资源有限的硬件。 

标准 I2P 套件位于 [i2p](<https://aur.archlinux.org/packages/i2p/>)AUR 和 [i2p-bin](<https://aur.archlinux.org/packages/i2p-bin/>)AUR 包。两者都需要[Java](<../zh-cn/Java.html> "Java")运行时环境（如[OpenJDK](<../zh-cn/Java.html#OpenJDK> "Java")）。建议在 ARM 平台使用时选择 Oracle Java。 

I2P 主页还提供了[预编译二进制文件](<https://geti2p.net/en/download#unix>)，其中包括命令行（无界面）选项，可以安装到用户的主目录当中。在这种情况下，I2P 将通过 i2p 网络自动更新自身。 

##  使用

如果您安装了 i2pd（C++版本），您需要[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用")服务项 `i2pd.service` 。守护进程的配置文件位于 `/etc/i2pd/i2pd.conf` 。如果安装了 i2p（Java版本），则此时您需要启动或启用服务项 `i2prouter.service`。 

打开（您选择的）浏览器访问 I2P 的欢迎页面， `127.0.0.1:7070` 为守护程序页面， `127.0.0.1:7657` 为路由控制台页面（请参阅[常见问题解答](<https://geti2p.net/en/faq>)）。在这里您将被导航到 I2P 配置和统计页面，以及指向 [Eepsites](<https://en.wikipedia.org/wiki/Eepsite> "wikipedia:Eepsite") 的链接。 请注意，在守护进程引导进入网络之前，匿名站点将不可使用，这可能需要几分钟时间。 

为了访问匿名站点，您需要配置浏览器使用以下本地代理： 
    
    HTTP  127.0.0.1 4444
    SOCKS 127.0.0.1 4447
    
##  匿名站点

要搭建匿名站点请查阅 I2P [说明](<http://127.0.0.1:7658>)。但请记住，i2p（Java版本）用户的主目录位于 `/opt/i2p` ，参阅 AUR 文件 [i2p.install](<https://aur.archlinux.org/cgit/aur.git/tree/i2p.install?h=i2p>) 。 

##  参见

  * [I2P Homepage](<https://www.i2p2.de>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2021-11-11 ⓘ]
  * [I2P Homepage mirror](<http://www.i2pproject.net>)
  * [I2P FAQ](<https://www.i2p2.de/faq.html>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2021-11-11 ⓘ]
  * [I2P on Wikipedia](<https://en.wikipedia.org/wiki/I2p> "wikipedia:I2p")
  * [i2pd daemon homepage](<https://i2pd.website/>)
  * [i2pd documentation](<https://i2pd.readthedocs.io/en/latest/>)
  * [GetI2P](<https://geti2p.net/zh/>)
