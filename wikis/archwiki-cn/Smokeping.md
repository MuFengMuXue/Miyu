[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** 请提供模板的第一个位置参数以概括原因。 (在[Talk:Smokeping](<../zh-cn/Talk:Smokeping.html>)讨论)

**翻译状态：**

  * 本文（或部分内容）译自 [Smokeping](<https://wiki.archlinux.org/title/Smokeping> "arch:Smokeping")，最近一次同步于 2017-04-07，若英文版本有所[更改](<https://wiki.archlinux.org/title/Smokeping?diff=0&oldid=473199>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Smokeping_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Smokeping](<https://oss.oetiker.ch/smokeping/index.en.html>)允许你监测多台服务器。 Smokeping使用RRDtool来存储数据，另外，其可基于RRDtool输出生成相应的统计图表。 Smokeping由两个部分组成。一个运行在后台、定期收集数据的服务。一个以图表形式展示数据的Web界面。 

这个wiki页面包括安装smokeping后台服务和Web界面的基本步骤。 

##  安装

这一节包括使用[smokeping](<https://archlinux.org/packages/?name=smokeping>)包包安装[Smokeping](<https://oss.oetiker.ch/smokeping/index.en.html>)。 FastCGI的安装步骤可以参见[Apache and FastCGI](</wzh/index.php?title=Apache_and_FastCGI&action=edit&redlink=1> "Apache and FastCGI（页面不存在）")。 

smokeping软件包包括两个部分： 

  * smokeping的后台服务和在`/etc/smokeping/`的配置文件。这个后台服务执行监测任务。
  * 在`/srv/http/smokeping`的“htdocs”。这些文件被Web界面所使用。

除了安装[smokeping](<https://archlinux.org/packages/?name=smokeping>)包包之外，您还需要： 

  * 一个smokeping监测的工具。[fping](<https://archlinux.org/packages/?name=fping>)包 是默认ping探针的最简洁方法。
  * [apache](<https://archlinux.org/packages/?name=apache>)包 和[mod_fcgid](<https://aur.archlinux.org/packages/mod_fcgid/>)AUR 被用于Web界面。
  * 一个图像缓存目录，其可被FastCGI脚本写入，例如：`/srv/smokeping/imgcache`
  * 一个数据存储目录，其可被smokeping后台服务写入，同时可被FastCGI脚本读取，例如：`/srv/smokeping/data`
  * 确保主配置文件可被smokeping后台服务读取。

###  可选的安装

如果你想使用其他探针，例如DNS、http探针，你需要安装如下所示的其他软件包。 这些探针的配置并不包括在这个wiki页面中。 

探针 | 所需软件包   
---|---  
Curl |  [curl](<https://archlinux.org/packages/?name=curl>)包  
DNS |  [bind](<https://archlinux.org/packages/?name=bind>)包 (被用于Dig)   
EchoPing |  [echoping](<https://archlinux.org/packages/?name=echoping>)包  
SSH |  [openssh](<https://archlinux.org/packages/?name=openssh>)包  
TelnetIOSPing |  [perl-net-telnet](<https://archlinux.org/packages/?name=perl-net-telnet>)包  
AnotherDNS |  [perl-net-dns](<https://archlinux.org/packages/?name=perl-net-dns>)包  
LDAP |  [perl-ldap](<https://archlinux.org/packages/?name=perl-ldap>)包  
LDAP (tls) |  [perl-io-socket-ssl](<https://archlinux.org/packages/?name=perl-io-socket-ssl>)包  
Authen |  [perl-authen-radius](<https://archlinux.org/packages/?name=perl-authen-radius>)包  
  
##  配置

Smokeping需要你编辑许多文件。 未编辑的文件的扩展名为`.dist`。将在`/etc/smokeping`目录中以`.dist`结尾的文件去除`.dist`后缀。 _find_ 可以完成这件任务，同时打印出所有被重命名与需要编辑的文件。 
    
    # cd /etc/smokeping
    # find . -name '*.dist' -print -execdir sh -c 'mv {} $(basename {} .dist)' \;
    # mv /srv/http/smokeping/smokeping.fcgi.dist /srv/http/smokeping/smokeping.fcgi
    
###  编辑配置文件

下一步，编辑 `/etc/smokeping/config` 文件。这个文件是smokeping的主配置文件。 下面将用一个完整的配置文件例子简要介绍各节的功用。 

`/etc/smokeping/config` 中 _General_ 节是最容易被编辑的。 根据你个人信息个性化上述的配置文件。相应的条目均有注释。 

注意：如果你没有安装`sendmail`的软件（例如：postfix 或 sendmail），使用一些别的东西代替，例如`/bin/false`。 你编辑的文件必须存在，否则smokeping将会报错。 

_Alerts_ 节。这个最小化的配置文件例子中并不需要 _Alerts_ 节，所以你可以将其注释或删除。 

_Database_ 节不需要做任何改动。 

_Presentation_ 节中，模板文件的路径需要更新。 

_Probes_ 节规定哪些探针被激活。默认情况下，仅 _FPing_ 探针被激活。这一节不需要做任何更改。 

_Slaves_ 节。这个最小化的配置文件例子中并不需要 _Slaves_ 节，所以你可以将其注释或删除。注意：如果你在 _Slaves_ 节中使用`smokeping_secrets`设置，你必须确保那个文件不能被其他用户访问，否则smokeping将会报错。`chmod 600 /etc/smokeping/smokeping_secrets`

_Targets_ 节指定哪些主机将被探测（在这个例子中为ping的目标）。像如下的例子，根据你想要搜集统计数据的主机，个性化 _Targets_ 节。 

你可以在这个网址 <https://oss.oetiker.ch/smokeping/doc/smokeping_examples.en.html> 了解更多关于Smokeping 配置文件的知识。 
    
    /etc/smokeping/config
    
    *** General ***
    
    owner     = Your Name Here                            # 你的名字
    contact   = your.email@host.bla                       # 你的电子邮件地址
    mailhost  = your.smtp.server.bla                      # 你的邮件服务器
    sendmail  = /bin/false                                # sendmail程序路径
    imgcache  = /srv/smokeping/imgcache                   # filesystem directory where we store files
    imgurl    = imgcache                                  # URL directory to find them
    datadir   = /srv/smokeping/data                       # daemon 与 webapp 共享的数据目录
    piddir    = /var/run                                  # filesystem directory to store PID file
    cgiurl    = http://localhost/smokeping/smokeping.fcgi  #  外部URL
    smokemail = /etc/smokeping/smokemail   
    tmail     = /etc/smokeping/tmail
    syslogfacility = local0
    # each probe is now run in its own process
    # disable this to revert to the old behaviour
    # concurrentprobes = no
    
    *** Database ***
    
    step     = 300
    pings    = 20
    
    # consfn mrhb steps total
    
    AVERAGE  0.5   1  1008
    AVERAGE  0.5  12  4320
        MIN  0.5  12  4320
        MAX  0.5  12  4320
    AVERAGE  0.5 144   720
        MAX  0.5 144   720
        MIN  0.5 144   720
    
    *** Presentation ***
    
    template = /etc/smokeping/basepage.html
    
    + charts
    
    menu = Charts
    title = The most interesting destinations
    ++ stddev
    sorter = StdDev(entries=>4)
    title = Top Standard Deviation
    menu = Std Deviation
    format = Standard Deviation %f
    
    ++ max
    sorter = Max(entries=>5)
    title = Top Max Roundtrip Time
    menu = by Max
    format = Max Roundtrip Time %f seconds
    
    ++ loss
    sorter = Loss(entries=>5)
    title = Top Packet Loss
    menu = Loss
    format = Packets Lost %f
    
    ++ median
    sorter = Median(entries=>5)
    title = Top Median Roundtrip Time
    menu = by Median
    format = Median RTT %f seconds
    
    + overview 
    
    width = 600
    height = 50
    range = 10h
    
    + detail
    
    width = 600
    height = 200
    unison_tolerance = 2
    
    "Last 3 Hours"    3h
    "Last 30 Hours"   30h
    "Last 10 Days"    10d
    "Last 400 Days"   400d
    
    *** Probes ***
    
    + FPing
    
    binary = /usr/sbin/fping
    
    *** Targets ***
    
    probe = FPing
    
    menu = Top
    title = Network Latency Grapher
    remark = Welcome to the SmokePing website of Arch User. \
             Here you will learn all about the latency of our network.
    
    + targets
    menu = Targets
    
    ++ ArchLinux
     
    menu = Arch Linux
    title = Arch Linux Website
    host = 66.211.214.131
    
    ++ GoogleDNS
    
    menu = Google DNS
    title = Google DNS server
    host = 8.8.8.8
    
    ++ MultiHost
    
    menu = Multihost example
    title = Arch Wiki and Google DNS
    host = /targets/ArchLinux /targets/GoogleDNS
    
####  有关smokeping配置文件语法的注意事项

每一个 **+** 号定义了一个有着层次等级的节。在节名称中不允许含有空格。英文句号 **.** 和正斜杠 **/** 同样应当尽量避免出现在节名称中。这是因为存储在数据目录下的RRD文件有着和节名称一样的文件名。 

在 _Targets_ 节，你可以用真实的主机名或其他节名称的路径来定义`host`，从而生成含有多个主机结果的图表，具体情况可以参考上面例子中的`MultiHost`。 

###  安装系统中的其他部分

创建配置文件提到的额外目录： 
    
    # mkdir -p /srv/smokeping/data
    # mkdir -p /srv/smokeping/imgcache
    # chown -R smokeping:smokeping /srv/smokeping
    # chown -R http:http /srv/smokeping/imgcache
    # chmod a+rx /srv/smokeping
    # chmod -R a+rx /srv/smokeping/data
    
由于smokeping配置文件同时被smokeping服务和FastCGI脚本读取，所以它应当具有可读取权限： 
    
    # chmod a+rx /etc/smokeping
    # chmod a+r /etc/smokeping/config
    
###  启动服务

启动 [Start](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") `smokeping.service`服务，并且确认它正在运行。 
    
    # systemctl start smokeping.service
    # systemctl enable smokeping.service
    
##  安装Web界面

编辑`/etc/httpd/conf/httpd.conf`，使其包含以下内容： 
    
    /etc/httpd/conf/httpd.conf
    
     LoadModule fcgid_module modules/mod_fcgid.so
     <IfModule fcgid_module>
       AddHandler fcgid-script .fcgi
     </IfModule>
    
     Alias /smokeping/imgcache /srv/smokeping/imgcache
     Alias /smokeping /srv/http/smokeping
    
     <Directory "/srv/smokeping/imgcache">
       AllowOverride all
       Require all granted
     </Directory>
    
     <Directory "/srv/http/smokeping">
      Options FollowSymLinks ExecCGI
      AllowOverride all
      Require all granted
     </Directory>
    
通过 `httpd.service`，启动 [Start](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") Apache 。 

检查 `<http://localhost/smokeping/smokeping.fcgi>` 是否载入。第一批数据将在几分钟后出现。 

如果由于字体原因导致图像不可读，你应当安装[ttf-dejavu](<https://archlinux.org/packages/?name=ttf-dejavu>)包。 

##  高级配置

Smokeping是一个可以被多种方式配置的有力工具。你可以启动许多不同类型的探针。你可以设置发送统计信息的从属smokeping服务器（slave smokeping servers），并显示来自其他服务器的探测结果。 你也可以使用perl创建你自己的探针。这篇教程目前并没有讲解这些选项。如果你对这些内容感兴趣，可以查阅[Smokeping官方网站](<https://oss.oetiker.ch/smokeping/index.en.html>)上的资料。 

## Troubleshooting

The smokeping package is currently broken in several ways. To get the service to run as a daemon, you will need to modify the provided systemd unit file to have this parameter: 
    
       type=forking
    
Smokemail is also not currently included, and is a required file for smokeping to run. You will need to download the file and add it manually from smokeping's github: 
    
       <https://github.com/oetiker/SmokePing/blob/master/etc/smokemail.dist>
    
##  注意

###  Smoketrace (Tr.cgi)

根据[更新记录](<https://oss.oetiker.ch/smokeping/pub/CHANGES>)，v2.5.5版本后[SmokeTraceroute](<https://oss.oetiker.ch/smokeping/doc/smoketrace.en.html>)功能正式上线。 
