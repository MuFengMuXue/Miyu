**翻译状态：**

  * 本文（或部分内容）译自 [MongoDB](<https://wiki.archlinux.org/title/MongoDB> "arch:MongoDB")，最近一次同步于 2024-04-03，若英文版本有所[更改](<https://wiki.archlinux.org/title/MongoDB?diff=0&oldid=796971>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/MongoDB_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

MongoDB (词源 hu**mongo** us) 是一个源码公开的，面向文档的数据库系统，由 [MongoDB Inc. (formerly 10gen)](<https://www.mongodb.com/>)开发并提供支持. 它是NoSQL家族中的一员， 替代用表储存数据的经典的关系型数据库， MongoDB的数据储存结构类似于用动态视图（dynamic schemas）储存类JSON文档（JSON-like documents) （MongoDB称这种格式为[BSON](<https://bsonspec.org/>)， 将数据尽早尽快地整合成对应的应用类型. 

##  安装

由于 MongoDB 修改了软件授权协议，[官方软件仓库](<../zh-cn/Official_repositories.html> "Official repositories")已经删除了此软件包 **[[1]](<https://lists.archlinux.org/archives/list/arch-dev-public@lists.archlinux.org/thread/OY2DLNWTZOBPAHFE5FSV4Q6AIWGZO6KV/>)** 。 

对于可用的最新版本，请安装以下软件之一： 

  * [mongodb](<https://aur.archlinux.org/packages/mongodb/>)AUR \- 从源代码构建
  * [mongodb-bin](<https://aur.archlinux.org/packages/mongodb-bin/>)AUR \- 从[官方MongoDB Ubuntu存储库](<https://repo.mongodb.org/apt/ubuntu/>)包中提取的预构建MongoDB二进制文件。使用的编译选项未知。

或者，也可以使用旧版本的MongoDB： 

  * [Mongodb50](<https://aur.archlinux.org/packages/Mongodb50/>)AUR,[mongodb50-bin](<https://aur.archlinux.org/packages/mongodb50-bin/>)AUR
  * [mongodb44](<https://aur.archlinux.org/packages/mongodb44/>)AUR,[mongodb44-bin](<https://aur.archlinux.org/packages/mongodb44-bin/>)AUR
  * [mongodb42-bin](<https://aur.archlinux.org/packages/mongodb42-bin/>)AUR
  * [mongodb40-bin](<https://aur.archlinux.org/packages/mongodb40-bin/>)AUR
  * [mongodb36-bin](<https://aur.archlinux.org/packages/mongodb36-bin/>)AUR
  * [mongodb34-bin](<https://aur.archlinux.org/packages/mongodb34-bin/>)AUR
  * [mongodb32-bin](<https://aur.archlinux.org/packages/mongodb32-bin/>)AUR

### Tools

还可以找到打包的其他MongoDB工具： 

  * **MongoDB Shell** ——新的 _Mongosh tool_ ，它取代了旧的 _MongoDB Shell_ **[[2]](<https://www.mongodb.com/docs/v5.0/reference/program/mongo/>)** 。兼容MongoDB 4.0或更高版本。**<https://www.mongodb.com/docs/mongodb-shell/>** || [mongosh-bin](<https://aur.archlinux.org/packages/mongosh-bin/>)AUR
  * **MongoDB Compass** ——用于查询、优化和分析MongoDB数据的图形用户界面交互工具 **<https://www.mongodb.com/docs/compass/>** || [mongodb-compass](<https://aur.archlinux.org/packages/mongodb-compass/>)AUR,[mongodb-compass-readonly](<https://aur.archlinux.org/packages/mongodb-compass-readonly/>)AUR,[mongodb-compass-isolated](<https://aur.archlinux.org/packages/mongodb-compass-isolated/>)AUR
  * **MongoDB Database Tools** ——提供导入、导出和诊断功能 **<https://www.mongodb.com/docs/database-tools/>** || [mongodb-tools](<https://aur.archlinux.org/packages/mongodb-tools/>)AUR
  * **Mingo** — A proprietary, EULA licensed, MongoDB GUI built on [Electron](</wzh/index.php?title=Electron&action=edit&redlink=1> "Electron（页面不存在）"), designed to aid MongoDB developers with managing their databases.

     <https://mingo.io/> || [mingo](<https://aur.archlinux.org/packages/mingo/>)AUR

##  使用

[**启动**](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Help:阅读")/[**启用**](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Help:阅读") `mongodb.service` 进程。 

**注意：** 在MongoDB服务第一次启动期间，它将通过创建大文件(用于其日志和其他数据)来[预分配空间](<https://docs.mongodb.com/manual/faq/storage/#preallocated-data-files>)。这一步可能需要一段时间，在此期间MongoDB Shell不可用。

启动 Mongo Shell， 在终端输入 **[[3]](<https://docs.mongodb.com/mongodb-shell/>)** : 
    
    $ mongosh
    
如果配置了身份验证： 
    
    $ mongosh -u _userName_
    
**警告：** 旧的mongo shell在MongoDB V5.0中已被弃用，取而代之的是mongosh **[[4]](<https://www.mongodb.com/docs/v5.0/reference/program/mongo/#mongodb-binary-bin.mongo>)** 。虽然它在某些MongoDB包中可用，但强烈建议您从5.0版开始更改它。

##  配置

###  文件格式

MongoDB使用基于YAML的配置文件格式。有关可用的配置选项，请参阅[**https://docs.mongodb.com/manual/reference/configuration-options/**](<https://docs.mongodb.com/manual/reference/configuration-options>)。 
    
    /etc/mongodb.conf
    
    systemLog:
       destination: file
       path: "/var/log/mongodb/mongod.log"
       logAppend: true
    storage:
       journal:
          enabled: true
    processManagement:
       fork: true
    net:
       bindIp: 127.0.0.1
       port: 27017
    setParameter:
       enableLocalhostAuthBypass: false
    ..

###  身份验证

**警告：** 默认情况下，MongoDB不需要任何身份验证！不过，MongoDB默认情况下只监听`localhost`，以防止外部访问。这仍然允许任何本地用户在不经过身份验证的情况下进行连接，并且可能会暴露数据库。建议启用访问控制以防止任何不需要的访问。如果您将MongoDB设置为在`0.0.0.0`上侦听，则**必须** 启用访问控制，否则您的数据将被窃取并被勒索。

创建具有管理员访问权限的MongoDB用户帐户 **[[5]](<https://docs.mongodb.com/manual/tutorial/enable-authentication/>)** : 
    
    $ mongosh
    
    use admin
    db.createUser(
      {
        user: "myUserAdmin",
        pwd: "abc123",
        roles: [ { role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase" ]
      }
    )

将以下内容[**附加**](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Help:阅读")到您的`/etc/mongob.conf`。 
    
    /etc/mongodb.conf
    
    security:
      authorization: "enabled"

[**重启**](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Help:阅读") `mongodb.service`. 

### NUMA

使用非统一访问内存(NUMA)运行MongoDB会显著影响性能 **[[6]](<https://docs.mongodb.com/manual/administration/production-notes/#mongodb-and-numa-hardware>)** 。 

要查看您的系统是否使用NUMA，请执行以下操作： 
    
    # dmesg | grep -i numa
    
此外，如果NUMA正在使用并且MongoDB不是通过`numactl`启动的，则`/var/log/mongodb/mongod.log`将显示警告。(mongo shell也会显示这一点，但前提是您没有启用身份验证。) 

如果您的系统使用NUMA，为了提高性能，您应该让MongoDB通过`numactl`启动。 

根据您安装的包[**编辑**](<../zh-cn/Systemd.html#%E4%BF%AE%E6%94%B9%E7%8E%B0%E5%AD%98%E5%8D%95%E5%85%83%E6%96%87%E4%BB%B6> "Systemd")`mongob.service`。 

如果使用[mongodb](<https://aur.archlinux.org/packages/mongodb/>)AUR，请将其从： 
    
    ExecStart=/usr/bin/mongod $OPTIONS
    
更改为： 
    
    ExecStart=**/usr/bin/numactl --interleave=all** /usr/bin/mongod $OPTIONS
    
如果使用[mongodb-bin](<https://aur.archlinux.org/packages/mongodb-bin/>)AUR，请将其从： 
    
    ExecStart=/usr/bin/mongod --quiet --config /etc/mongodb.conf
    
更改为： 
    
    ExecStart=**/usr/bin/numactl --interleave=all** /usr/bin/mongod --quiet --config /etc/mongodb.conf
    
还需要禁用区域声明，但在Arch上，`/proc/sys/vm/zone_reClaim_mode`默认为`0`。 

根据需要[**重新启用**](<../zh-cn/Systemd.html#%E4%BD%BF%E7%94%A8%E5%8D%95%E5%85%83> "Systemd")并[**重启**](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Help:阅读")mongob.service。 

###  完全的启动和停止

默认情况下，如果在90秒内没有完成启动或停止操作，则[systemd](<../zh-cn/Systemd.html> "Systemd")会在请求启动或停止后立即终止任何内容。 

[mongodb](<https://aur.archlinux.org/packages/mongodb/>)AUR会让systemd等待MongoDB启动所需的时间，但[mongodb-bin](<https://aur.archlinux.org/packages/mongodb-bin/>)AUR不会。这两个包都允许systemd在被要求停止后终止MongoDB，如果它没有在90秒内完成的话。 

大型MongoDB数据库可能需要相当长的时间才能完全关闭，特别是在使用交换的情况下。(使用64GB RAM和16GB交换空间的顶级NVMe上的运行450GB数据库可能需要一个小时才能关闭。) 

默认情况下，MongoDB使用日志记录。**[[7]](<https://docs.mongodb.com/manual/reference/configuration-options/#storage-options>)** 对于日志记录，不彻底的关闭应该不会造成数据丢失的风险。但是，如果不彻底关闭，大型MongoDB数据库可能需要相当长的时间才能启动备份。在这种情况下，选择是否需要彻底关闭就是选择较慢的关机和较慢的启动。**[[8]](<https://groups.google.com/forum/?utm_medium=email&utm_source=footer#!msg/mongodb-user/KjBU_GcNcmw/gR2UxRIFAgAJ>)**

**警告：** 如果禁用日志记录，如果不进行彻底关机，则会有严重的数据丢失风险，因此您确实需要要求彻底关机。[[9]](<https://docs.mongodb.com/manual/tutorial/recover-data-following-unexpected-shutdown/>)

为了防止[**systemd**](<../zh-cn/Systemd.html> "Systemd") 在90秒后停止MongoDB进程，可以编辑`mongob.service`。 

要让MongoDB干净利落地关机，请在[Service]部分[**附加**](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Help:阅读")下面内容：(在大型数据库上，这可能会显著降低系统关机时间，但会加快下一次MongoDB启动时间) 
    
    TimeoutStopSec=infinity
    
如果MongoDB需要很长时间才能启动备份，则对于[**systemd**](<../zh-cn/Systemd.html> "Systemd")来说，每隔90秒持续终止并重新启动它可能是非常有问题的 **[[10]](<https://jira.mongodb.org/browse/SERVER-38086>)** ，所以[mongodb](<https://aur.archlinux.org/packages/mongodb/>)AUR可以防止这种情况发生。如果使用的是**[mongodb-bin](<https://aur.archlinux.org/packages/mongodb-bin/>) AUR**，为了让[systemd](<../zh-cn/Systemd.html> "Systemd")等待MongoDB启动的时间，可以在[Service]部分添加： 
    
    TimeoutStartSec=infinity
    
##  排障

如果MongoDB无法启动，而你刚刚升级到[mongodb](<https://aur.archlinux.org/packages/mongodb/>)AUR 4.0.6-2+，你可能有一个自定义的`/etc/mongodb.conf`。当MongoDB还在[**官方仓库**](<../zh-cn/%E5%AE%98%E6%96%B9%E4%BB%93%E5%BA%93.html> "官方仓库")时，它使用了一个Arch特有的配置文件，使用systemd服务类型的simple。现在它提供了上游的 systemd 服务和配置文件，改用 forking 的 systemd 服务类型。Pacman 会自动升级你的 systemd 服务文件，但[**只有在你从未修改过**](<../zh-cn/Pacman/pacnew_%E4%B8%8E_pacsave.html> "Pacman/pacnew 与 pacsave")`/etc/mongodb.conf` 的情况下才会自动升级。在这种情况下，systemd 会期待 mongod 分叉，但它的配置文件会告诉它不要这样做。你需要：切换到安装在`/etc/mongodb.conf.pacnew`的新配置文件，并复制你对旧文件所做的修改，考虑到新文件现在是YAML格式，而旧文件可能是MongoDB 2.4的格式，你仍然需要；或者修改你现有的配置文件，使分叉生效。(要继续使用旧的2.4文件格式而不是YAML格式，添加`fork: true`应该是需要的）。 

检查`mongodb.service`是否被配置为使用正确的数据库位置。 

在`ExecStart`行中添加`--dbpath /var/lib/mongodb`： 
    
    ExecStart=/usr/bin/numactl --interleave=all mongod --quiet --config /etc/mongodb.conf --dbpath /var/lib/mongodb
    
检查其日志文件是否有至少3GB的可用空间，否则mongodb可能无法启动（不向用户发布消息）： 
    
    $ df -h /var/lib/mongodb/
    
检查`mongod.lock`锁定文件是否为空： 
    
    # ls  -lisa /var/lib/mongodb
    
如果是，则[**停止**](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Help:阅读")`mongob.service`。在数据库上运行修复，指定数据库路径(`/var/lib/mongodb/`是Arch Linux中的默认路径`--dbpath`)： 
    
    # mongod --dbpath /var/lib/mongodb/ --repair
    
完成后，数据库路径应该包含修复的数据文件和一个空的`mongod.lock`文件。 

在紧急情况下，您可以删除该文件，使用可能损坏的文件启动数据库，并尝试从数据库恢复数据。然而，在这些情况下，不可能预测数据库的状态。详细信息请参见[**上游文档**](<https://docs.mongodb.com/manual/tutorial/recover-data-following-unexpected-shutdown/>)。 

**警告：** 在紧急情况下，您可以删除该文件，使用可能损坏的文件启动数据库，并尝试从数据库恢复数据。然而，在这些情况下，不可能预测数据库的状态。详细信息请参见**[上游文档](<https://docs.mongodb.com/manual/tutorial/recover-data-following-unexpected-shutdown/>)** 。

在以root用户身份运行修复之后，文件将归root用户所有，而Arch Linux在另一个用户下运行它。您需要使用chown将文件的所有权更改回正确的用户。有关更多详细信息，请参阅以下链接：[**进一步参考**](<http://earlz.net/view/2011/03/11/0015/mongodb-and-arch-linux>)
    
    # chown -R mongodb: /var/{log,lib}/mongodb/
    
####  部分设备始终无法启动 MongoDB

由于 CPU 架构缺乏必要的指令集，有些设备是无法运行 MongoDB 的。例如，MongoDB 可以被安装在使用 Intel“Gemini Lake Refresh”/[Goldmount Plus](<https://en.wikipedia.org/wiki/Goldmont_Plus> "wikipedia:Goldmont Plus") 微架构的 [GPD MicroPC](<../zh-cn/GPD_MicroPC.html> "GPD MicroPC") 上，但在运行 MongoDB Shell 的时候会出现如下信息： 
    
    $ mongosh 'mongodb://localhost:27017'
    
    Current Mongosh Log ID: 642b48661e2fc4dd5bda05d0
    Connecting to:          mongodb://localhost:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.8.0
    MongoNetworkError: connect ECONNREFUSED 127.0.0.1:27017

另外，使用 `coredumpctl info` 可观察到 `4 (ILL)` 信号，意指尝试执行非法指令集。换句话说，该设备缺乏本地运行该程序所必需的指令集。 

但是，它可以连接到能运行 MongoDB 的远程设备上的 MongoDB Atlas 实例，该操作不需要 `mongodb.service`。 

###  透明大页（THP）相关警告

用户可能希望使用 [**tmpfiles**](<../zh-cn/Systemd.html#%E4%B8%B4%E6%97%B6%E6%96%87%E4%BB%B6> "Systemd") 永久禁用此功能： 
    
    /etc/tmpfiles.d/mongodb.conf
    
    w /sys/kernel/mm/transparent_hugepage/enabled - - - - never
    w /sys/kernel/mm/transparent_hugepage/defrag - - - - never

在运行时使用 [**sysctl**](<../zh-cn/Sysctl.html> "Sysctl") 禁用THP： 
    
    # echo never > /sys/kernel/mm/transparent_hugepage/enabled
    # echo never > /sys/kernel/mm/transparent_hugepage/defrag
    
###  软限制过低的警告

如果您使用的是systemd服务，则编辑单元文件： 
    
    [Service]
    # Other directives omitted
    # (file size)
    LimitFSIZE=infinity
    # (cpu time)
    LimitCPU=infinity
    # (virtual memory size)
    LimitAS=infinity
    # (locked-in-memory size)
    LimitMEMLOCK=infinity
    # (open files)
    LimitNOFILE=64000
    # (processes/threads)
    LimitNPROC=64000
    
有关更多详细信息，请参阅以下链接：**[进一步参考](<https://docs.mongodb.com/manual/reference/ulimit/#review-and-set-resource-limits>)**
