**翻译状态：**

  * 本文（或部分内容）译自 [Systemd-timesyncd](<https://wiki.archlinux.org/title/Systemd-timesyncd> "arch:Systemd-timesyncd")，最近一次同步于 2025-09-13，若英文版本有所[更改](<https://wiki.archlinux.org/title/Systemd-timesyncd?diff=0&oldid=845447>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Systemd-timesyncd_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd")
  * [systemd](<../zh-cn/Systemd.html> "Systemd")
  * [系统时间](<../zh-cn/%E7%B3%BB%E7%BB%9F%E6%97%B6%E9%97%B4.html> "系统时间")

摘自 [systemd 邮件列表](<https://lists.freedesktop.org/archives/systemd-devel/2014-May/019537.html>)： 

     _systemd-timesyncd_ 是一个用于跨网络同步系统时钟的守护服务。它实现了一个 SNTP 客户端。与 [chrony](<../zh-cn/Chrony.html> "Chrony") 或 NTP 参考服务器等 NTP 实现相比，这个服务仅做了客户端实现，摒弃了完整 NTP 实现的复杂性。它只专注于从远程服务器查询然后同步到本地时钟。除非你打算为网络客户端提供 NTP 服务或者连接本地硬件时钟，否则这个简单的 NTP 客户端应该更适合大多数人。守护进程运行只需要最小特权，并且会跟网络服务 networkd 挂钩，仅在网络连接可用时才工作。每次收到一个新的 NTP 同步请求或每 60 秒时，后台服务就把当前时间保存到磁盘，并尽可能在系统启动时修正系统时间，这样处理的目的是为了适应像 Raspberry Pi 和嵌入式设备这种缺少 RTC 的系统，并确保这些系统时单点处理（即使它并不是总是正确的）。如果要使用这个守护进程，需要在安装系统时创建一个新的系统用户和组“systemd-timesync”。

##  配置

_systemd-timesyncd_ 启动时会读取 `/etc/systemd/timesyncd.conf` 配置文件，内容如下: 
    
    /etc/systemd/timesyncd.conf
    
    [Time]
    #NTP=
    #FallbackNTP=0.arch.pool.ntp.org 1.arch.pool.ntp.org 2.arch.pool.ntp.org 3.arch.pool.ntp.org
    #...

要增加或者更改[时间同步服务器](<../zh-cn/Network_Time_Protocol_daemon.html#%E8%BF%9E%E6%8E%A5%E5%88%B0_NTP_%E6%9C%8D%E5%8A%A1%E5%99%A8> "Network Time Protocol daemon"), 取消上文中对应的注释，然后将服务器的域名或 IP 以空格间隔开列出。另外，你也可以将配置文件放入 `/etc/systemd/timesyncd.conf.d/*.conf`，详细信息请参考 [timesyncd.conf(5)](<https://man.archlinux.org/man/timesyncd.conf.5>)。 

例如，可以使用 [NTP 项目](<https://www.pool.ntp.org/>)或者 [Arch 默认](<https://gitlab.archlinux.org/archlinux/packaging/packages/ntp/-/commit/343310b9ddd996220de27a2a35a5c1277a0bec9b>)（NTP 也有这个站点）提供的任何时间服务器： 
    
    /etc/systemd/timesyncd.conf 或者 /etc/systemd/timesyncd.conf.d/local.conf
    
    [Time]
    NTP=0.arch.pool.ntp.org 1.arch.pool.ntp.org 2.arch.pool.ntp.org 3.arch.pool.ntp.org
    FallbackNTP=0.pool.ntp.org 1.pool.ntp.org 0.fr.pool.ntp.org

要验证配置: 
    
    $ timedatectl show-timesync --all
    
    LinkNTPServers=
    SystemNTPServers=
    FallbackNTPServers=0.arch.pool.ntp.org 1.arch.pool.ntp.org 2.arch.pool.ntp.org 3.arch.pool.ntp.org
    ServerName=0.arch.pool.ntp.org
    ServerAddress=103.47.76.177
    RootDistanceMaxUSec=5s
    PollIntervalMinUSec=32s
    PollIntervalMaxUSec=34min 8s
    PollIntervalUSec=1min 4s
    NTPMessage={ Leap=0, Version=4, Mode=4, Stratum=2, Precision=-21, RootDelay=177.398ms, RootDispersion=142.196ms, Reference=C342F10A, OriginateTimestamp=Mon 2018-07-16 13:53:43 +08, ReceiveTimestamp=Mon 2018-07-16 13:53:43 +08, TransmitTimestamp=Mon 2018-07-16 13:53:43 +08, DestinationTimestamp=Mon 2018-07-16 13:53:43 +08, Ignored=no PacketCount=1, Jitter=0 }
    Frequency=22520548

另外，也可以使用 [systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd") _.network_ 文件的 `NTP=` 选项或 DHCP 服务器（需在 `[DHCPv4]` 或 `[DHCPv6]` 部分启用 `UseNTP` 选项）指定 NTP 服务器。 

NTP 服务器的选择会遵循以下规则: 

  * [systemd-networkd.service(8)](<https://man.archlinux.org/man/systemd-networkd.service.8>) 中针对每个接口的配置，或者 DHCP 服务优先。
  * `/etc/systemd/timesyncd.conf` 中定义的 NTP 服务器会在运行时被添加到针对每个接口的服务器列表中，守护进程会轮流连接这些服务器直到某个有应答。
  * 如果上两步没有取到 NTP 服务器， 那么将使用 `FallbackNTP=` 中定义的服务器。

**注意：**

  * 这个服务每次同步或每 60 秒会写入 `/var/lib/systemd/timesync/clock` 本地文件, 这个目录是硬编码的，不可以更换。
  * 这一写入机制在只读的 root 分区或者尝试减少 SD 卡写入量时可能会造成问题。
  * 写入次数可以通过类似 `PollIntervalMinSec=1d` 和 `SaveIntervalSec=infinity` 这样的配置项降低。

##  使用

###  启用并启动

要启用和启动它，执行： 
    
    # timedatectl set-ntp true
    
其他方法（如在使用 chroot 时）有[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `systemd-timesyncd.service`。 

###  检查服务

同步过程可能会很慢，请耐心等一会。要检查服务状态，使用: 
    
    $ timedatectl status
    
                   Local time: Thu 2015-07-09 18:21:33 CEST
               Universal time: Thu 2015-07-09 16:21:33 UTC
                     RTC time: Thu 2015-07-09 16:21:33
                    Time zone: Europe/Amsterdam (CEST, +0200)
    System clock synchronized: yes
                  NTP service: active
              RTC in local TZ: no
    
###  查看详细信息

要查看更多的服务信息，请使用: 
    
    $ timedatectl timesync-status
    
           Server: 103.47.76.177 (0.arch.pool.ntp.org)
    Poll interval: 2min 8s (min: 32s; max 34min 8s)
             Leap: normal
          Version: 4
          Stratum: 2
        Reference: C342F10A
        Precision: 1us (-21)
    Root distance: 231.856ms (max: 5s)
           Offset: -19.428ms
            Delay: 36.717ms
           Jitter: 7.343ms
     Packet count: 2
        Frequency: +267.747ppm
    
###  查看非默认配置

要查看非默认配置选项和文件（即被修改的配置项），使用： 
    
    $ systemd-analyze cat-config systemd/timesyncd.conf --tldr
    
    # /etc/systemd/timesyncd.conf
    [Time]
    
    # /etc/systemd/timesyncd.conf.d/local.conf
    [Time]
    NTP=0.nl.pool.ntp.org 1.nl.pool.ntp.org 2.nl.pool.ntp.org 3.nl.pool.ntp.org
    RootDistanceMaxSec=0.1
    PollIntervalMinSec=1d
    PollIntervalMaxSec=4w
    SaveIntervalSec=infinity
    
###  查看日志

要查看过去 24 小时的事件记录，使用： 
    
    # journalctl -u systemd-timesyncd --no-hostname --since "1 day ago"
    
    Jan 19 15:14:20 systemd[1]: Stopping Network Time Synchronization...
    Jan 19 15:14:20 systemd[1]: systemd-timesyncd.service: Deactivated successfully.
    Jan 19 15:14:20 systemd[1]: Stopped Network Time Synchronization.
    Jan 19 15:14:20 systemd[1]: Starting Network Time Synchronization...
    Jan 19 15:14:20 systemd[1]: Started Network Time Synchronization.
    Jan 19 15:14:20 systemd-timesyncd[1023]: Contacted time server 178.215.228.24:123 (0.nl.pool.ntp.org).
    Jan 19 15:14:20 systemd-timesyncd[1023]: Initial clock synchronization to Fri 2024-01-19 15:14:20.393865 CET.
    
##  参阅

  * [论坛：systemd-timesyncd 没有保持时间同步](<https://bbs.archlinux.org/viewtopic.php?id=182600>)
  * [论坛：使用 systemd-timesync 替代 NTP](<https://bbs.archlinux.org/viewtopic.php?id=182172>)
  * [timesyncd 源码](<https://github.com/systemd/systemd/blob/main/src/timesync/timesyncd.c>)
  * [systemd-timesyncd(8)](<https://man.archlinux.org/man/systemd-timesyncd.8>)
  * [timesyncd.conf(5)](<https://man.archlinux.org/man/timesyncd.conf.5>)
