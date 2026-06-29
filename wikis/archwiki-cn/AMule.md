**翻译状态：**

  * 本文（或部分内容）译自 [AMule](<https://wiki.archlinux.org/title/AMule> "arch:AMule")，最近一次同步于 2022-05-29，若英文版本有所[更改](<https://wiki.archlinux.org/title/AMule?diff=0&oldid=484054>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/AMule_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[aMule](<https://www.amule.org/>) 是一个类似于 eMule（电骡）的客户端，用于 [eDonkey 网络](<https://zh.wikipedia.org/wiki/EDonkey%E7%BD%91%E7%BB%9C> "zhwp:EDonkey网络")和 [Kademlia](<https://zh.wikipedia.org/wiki/Kademlia> "zhwp:Kademlia") 网络，支持多平台。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")软件包 [amule](<https://archlinux.org/packages/?name=amule>)包。 

**amuled** 是 aMule 的后台守护进程，无界面但功能齐全。其前端有 GTK 的 aMuleGUI、网页版的aMuleWeb、命令行的 aMuleCmd。 

##  服务

软件包提供了两个 _systemd_ [服务](<../zh-cn/Systemd.html> "Daemon")： amuled 和 amuleweb。先进行配置，设置外部访问的密码和 `amuleweb` 管理员密码，然后按照需要启动/启用 `amuled` 和 `amuleweb` 服务。 

**amulweb** 启动后可以在本机通过 `<http://127.0.0.1:4711>` 访问（如果需要外部访问，则要更改监听地址），默认的管理员密码是 **amule** 。 

##  配置

软件安装时会创建用户**amule** ，运行 systemd 服务时会使用此用户。 

配置文件和临时文件位于 amule 的主目录`/var/lib/amule`： 

  * amuled 的配置位于 `/var/lib/amule/.aMule/amule.conf`
  * amuleweb 的配置位于`/var/lib/amule/.aMule/remote.conf`

安装时 pacman 会生成一个带外部访问密码的 amule.conf 文件，amuleweb 配置文件也使用相同的密码。外部配置工具可以使用此密码远程访问。要重新生成密码，可以使用： 
    
    $ echo -n <your password here> | md5sum | cut -d ' ' -f 1
    
生成密码后，通过 **[ExternalConnect]** 参数设置。 
    
    /var/lib/amule/.aMule/amule.conf
    
    [ExternalConnect]
    AcceptExternalConnections=1
    ECPassword=<encrypted password>

注意 `/var/lib/amule` 下的全部文件所有者应当是 **amule** 用户. 
    
    # chown amule:amule -R /var/lib/amule
    
### amuleweb

**注意：** 较之amulegui，amuleweb功能单薄，输出的下载信息也少，而且经常要求输入密码（让浏览器记住密码会好一些）。基于以上原因，建议使用amulegui，并忽略本节。

####  创建配置文件

还是使用之前配置amuled时的那个新用户，启动amuleweb以初始化配置文件： 
    
    $ amuleweb --write-config --password=_< 这里是密码>_ --admin-pass=<这个是网页登录密码>
    
<这里是密码>处填写之前配置 amuled 使用的密码（未加密的），<这个是网页登录密码>处填写登录网页界面时输入的密码。 

**提示：** 如果 Kad nodes.dat 用的默认 URL 无法连接，可以使用在 [[1]](<http://nodes-dat.com>)获取 URL.

## amulegui

Amulegui 是 aMule 的 GTK+ 前端。 

###  配置通知

Settings → Events 包含自动触发的命令. 核心命令是 _notify-send_ (需要安装 [libnotify](<https://archlinux.org/packages/?name=libnotify>)包)，可以用 amule 参数设置通知。例如在 _Download completed_ 中设置如下值会在下载完成后显示下载大小：: 
    
    $ notify-send -i amule "%NAME completed (%SIZE bytes)"
    
"-i amule" 选项是用来设置 amule 图标的（如果想自定义，把图标名 amule 换成自定义的文件，路径用斜线隔开）。 

##  使用 Docker 安装

如果你在使用 [docker](<https://archlinux.org/packages/?name=docker>)包，安装和配置会很简单，用下面模板启动容器 
    
    $ sudo docker run -d \
    --name=amule \
    -e PUID=1000 \
    -e PGID=1000 \
    -e TZ=Asia/Shanghai \
    -p 4711:4711 \
    -p 4712:4712 \
    -p 4662:4662 \
    -p 4665:4665/udp \
    -p 4672:4672/udp \
    -v <fill_amule_configuration_path>:/home/amule/.aMule \
    -v <fill_amule_completed_downloads_path>:/incoming \
    -v <fill_amule_incomplete_downloads_path>:/temp \
    --restart unless-stopped \
    ngosang/amule
    
把 **fill_amule_configuration_path** 替换为配置路径，通常是 _/home/you/.config/amule_ ，把 **ill_amule_completed_downloads_path** , **fill_amule_incomplete_downloads_path** 换成宿主机上的目录（要存放下载文件的目录绝对路径）。 

如果容器成功启动了，会运行 **amuled** 和 **amuleweb** 在里面，使用这个命令查看生成的密码 
    
    $ sudo docker logs amule
    
    Creating group amule with GID 1000 ...
     Creating user amule with UID 1000 ...
     Remote GUI password: Passwd1xxxxxxxxxxxxxxxxxxxxxxxxxx
     Web UI password: Passwd2xxxxxxxxxxxxxxxxxxxxxxxxxx
     /home/amule/.aMule/amule.conf file NOT found. Generating new default configuration ...
     /home/amule/.aMule/amule.conf successfullly generated.

接着打开 `<http://127.0.0.1:4711>` 并输入 _Web UI password_ 。 

##  参阅

  * [Getting_Started at aMule wiki](<http://wiki.amule.org/wiki/Getting_Started>)。
