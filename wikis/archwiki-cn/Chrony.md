**翻译状态：**

  * 本文（或部分内容）译自 [Chrony](<https://wiki.archlinux.org/title/Chrony> "arch:Chrony")，最近一次同步于 2025-01-04，若英文版本有所[更改](<https://wiki.archlinux.org/title/Chrony?diff=0&oldid=824505>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Chrony_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

本文描述了如何配置并运行 [chrony](<https://chrony-project.org/>)，这是一个对漫游友好的 [NTP](<../zh-cn/%E7%B3%BB%E7%BB%9F%E6%97%B6%E9%97%B4.html#%E6%97%B6%E9%92%9F%E5%90%8C%E6%AD%A5> "系统时间") 客户端和服务端实现，专为不常在线的系统环境设计。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [chrony](<https://archlinux.org/packages/?name=chrony>)包。 

##  配置

最小的可用配置（使用了 IP 而不是域名）如下： 
    
    /etc/chrony.conf
    
    server 1.2.3.4 offline
    server 5.6.7.8 offline
    server 9.10.11.12 offline
    driftfile /var/lib/chrony/drift
    rtconutc
    
    # 该选项会同步 RTC 时间，但不跟踪 RTC 偏移。建议的替代值为 rtcfile，详情可参考下文的“RTC 选项”。
    rtcsync
    
更多信息请查阅 `/usr/share/doc/chrony/README`，它对你现有的问题都提供了指向。在网上也可以找到相关[文档](<https://chrony-project.org/documentation.html>)。另外也请查看手册：[chronyc(1)](<https://man.archlinux.org/man/chronyc.1>)，[chrony.conf(5)](<https://man.archlinux.org/man/chrony.conf.5>) 和 [chronyd(8)](<https://man.archlinux.org/man/chronyd.8>)。 

###  NTP 服务器

在 `/etc/chrony.conf` 中定义的第一项就是设备要连接到的服务器地址。 NTP 服务器处于一分层结构中，其中的每一层被称作 _strata_ ：被认定为独立时钟源的设备作为 _stratum 0_ 时间源；直接连接到 _stratum 0_ 的设备为 _stratum 1_ 时间源；连接到 _stratum 1_ 的为 _stratum 2_ 时间源，以此类推。 

但请注意，服务器的层级并不能作为其准确度或可靠性的依据。通常来说，stratum 2 服务器被用于时间同步；如果你还不知道要连到哪个服务器，那建议使用 [pool.ntp.org](<https://www.ntppool.org/en/>) 的服务器（[备用链接](<https://support.ntp.org/bin/view/Servers/NTPPoolServers>)），然后根据你的物理位置选择服务器池。 

下一行告知 chrony 从 NTP 池中选择 4 个源（chrony 使用其特定方式处理服务器池，以防止混淆其服务端测偏移跟踪），然后在启动时使用 burst 特性： 
    
    pool 2.arch.pool.ntp.org iburst maxsources 4
    
####  离线设备

如果你的设备在启动时不会连到网络，那建议使用其 _offline_ 选项。它会让 Chrony 在没有被告知的情况下不要尝试连接到服务器。 
    
    pool 2.arch.pool.ntp.org iburst maxsources 4 offline
    
另外，由于在完成连接前 DNS 解析都将不可用，建议使用 IP 地址而不是域名，或者在 `/etc/hosts` 中将域名固定到对应的 IP 地址。 

####  使用 NTS 服务器

从 4.0 版本开始 [[1]](<https://git.tuxfamily.org/chrony/chrony.git/tree/NEWS?id=4.0#n6>)，chrony 支持使用 [Network Time Security (NTS) 网络时间安全](<https://www.networktimesecurity.org/>)机制，这是 NTP 的安全加密变种。如需使用该功能，请添加一个启用 NTS 的服务器，然后在结尾添加 `nts`，例如： 
    
    server time.cloudflare.com iburst nts
    
可以在[这里](<https://github.com/jauderho/nts-servers>)查看支持 NTS 的服务器列表。 

###  实时时钟

在系统启动时，会从硬件实时时钟（RTC）读取初始时间，并用其设定系统时间，然后在 chrony 守护进程启动后的几分钟内进行一次同步。如果硬件时间脱离同步，那初始系统时间将可能会和真实时间相差数分钟。Chrony.conf 有三种不同机制来处理 RTC： 

  * 第一种是 `rtcsync`，它会简单地定期将当前时间写入到 RTC。这也是 ntpd 选用的方式，但会关闭 RTC 偏移跟踪：这对于间断运行的桌面环境很不利，该环境下会依赖 RTC 进行大量计时工作。
  * 第二种是 `rtcautotrim`，它会在 RTC 时间偏移超过一定量后进行复写。该方式可与 `rtcfile` 搭配，它会启用 RTC 误差跟踪。
  * 最后一种是不操控 RTC，但会将其误差和偏移记录到 `rtcfile`。RTC 时间会一直有误差，但系统时间会保持正常，因为 chrony 记录了其具体的偏移量。chronyc 下的 `rtctrim` _命令_ 还是可以按需同步 RTC：

    # chronyc
    chronyc> trimrtc
    200 OK
    chronyc> quit
    
**注意：**`rtcsync` 和 `rtcfile` 不能同时使用。另外 `rtcfile` 会阻止如 `hwclock` 和 `timedatectl` 之类的工具访问 RTC，详细信息请参考 [chrony.conf(5) § System clock](<https://man.archlinux.org/man/chrony.conf.5#System_clock>)。

另外，`rtconutc` 描述了 RTC 是否以 UTC 时间运行。 

####  案例：间断运行的桌面环境

间断运行的桌面环境将需要使用 `rtcfile` 来跟踪 RTC 误差。装有 Arch Linux 连续运行 5 年的设备上 RTC 可累计有 300 秒的误差，如果使用以上的配置，在重启后 chrony 会需要很长一段时间来调整时间偏移。如果改用如下配置： 

**注意：** 默认不存在 `/etc/sysconfig` 文件夹，需要手动创建。
    
    /etc/sysconfig/chronyd
    
    OPTIONS='-r -s'
    
    /etc/chrony.conf
    
    dumpdir /var/lib/chrony
    rtcfile /var/lib/chrony/rtc
    
有意思的是，RTC 还是会有误差，但在每次重启之后，chrony 都会调整 RTC 的累计误差，就算系统刚刚启动，其时间还能和 NTP 接近同步。 

RTC 仍留存误差的原因是我们忘了添加 `rtcautotrim` 一行到配置中，它会让 chrony 调整 RTC 时间。如果加上了这一行，那 RTC 和系统时间都将变正确。 

###  其它有意思的选项

有用的选项： 

  * `makestep`：允许 chrony 单次大量调整时间，而不是频繁多次调整。可能会对运行中程序造成影响，但有助于修正大量偏移。`makestep 0.1 3` 可能会更适用于经常离线的系统：只有开头三次调整会是阶跃性的，因此影响仅限于系统启动时段。

精确性： 

  * `server` 和 `pool`：`xleave` 和 `presend` 可能会在没有兼容性成本的情况下提升精确度。
  * `hwtimestamp`：有些网卡会给它的包添加时间戳以测量网络栈的延迟。使用 `hwtimestamp *` 可用启用该功能，对于不支持的网卡将不起任何效果。
  * `tempcomp`：跟踪软件时钟偏移（通常由主板晶振温度变化导致）和温度传感器间的关系，适用于要求极致精确度的环境。

##  用法

###  启动 chronyd

软件包提供了 `chronyd.service`，具体信息请参考 [systemd](<../zh-cn/Systemd.html> "Systemd")。 

**注意：**

  * `systemd-timesyncd.service` 会与 `chronyd` 产生冲突，所以如果你要[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `chronyd`，需要先将其[禁用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "禁用")。

###  告知 chronyd 网络连接已可用

如果你连接到了网络，执行： 
    
    # chronyc
    chronyc> online
    200 OK
    chronyc> exit
    
你也可以使用 `activity` 选项来查看状态： 
    
    # chronyc activity
    200 OK
    3 sources online
    0 sources offline
    0 sources doing burst (return to online)
    0 sources doing burst (return to offline)
    0 sources with unknown address
    
Chrony 应该已经连接到配置的时间服务器了，并根据需要更新了你的时钟。使用如下命令告知 chrony 你已经断开网络： 
    
    # chronyc offline
    200 OK
    
    # chronyc activity
    200 OK
    0 sources online
    3 sources offline
    0 sources doing burst (return to online)
    0 sources doing burst (return to offline)
    0 sources with unknown address
    
在线/离线状态可由 [networkmanager](<https://archlinux.org/packages/?name=networkmanager>)包 和 [connman](<https://archlinux.org/packages/?name=connman>)包 的调度服务自动处理，详情请参考下文。 

###  检查已配置的 NTP 服务器

如需查看 chrony 正在使用的 NTP 服务器和其精度，可使用 `chronyc -N 'sources -a -v'`： 
    
    $ chronyc -N 'sources -a -v'
    
      .-- Source mode  '^' = server, '=' = peer, '#' = local clock.
     / .- Source state '*' = current best, '+' = combined, '-' = not combined,
    | /             'x' = may be in error, '~' = too variable, '?' = unusable.
    ||                                                 .- xxxx [ yyyy ] +/- zzzz
    ||      Reachability register (octal) -.           |  xxxx = adjusted offset,
    ||      Log2(Polling interval) --.      |          |  yyyy = measured offset,
    ||                                \     |          |  zzzz = estimated error.
    ||                                 |    |           \
    MS Name/IP address         Stratum Poll Reach LastRx Last sample               
    ===============================================================================
    ^+ ptbnts1.ptb.de                1   6   377    50    -38us[  -13us] +/- 8723us
    ^* ptbnts2.ptb.de                1   6   377    49  +2061ns[  +27us] +/- 7538us
    ^+ nts.ntp.se                    2   6   377    51   +594us[ +619us] +/-   15ms
    ^+ nts.sth1.ntp.se               2   6   377    51   +655us[ +680us] +/-   15ms
    ^+ nts.sth2.ntp.se               2   6   377    53   +991us[+1016us] +/-   15ms
    ^+ time.cloudflare.com           3   6   377    49  -1250us[-1250us] +/-   10ms
    
##  网络状态通知

如果你在 `chrony.conf` 中为你的池配置了 offline 选项，需要将网络状态变更告知 _chrony_ 。 

你可以使用 _chronyc_ 来通知 _chrony_ ，也可以使用你的网络配置管理器对应的调度服务。 

### NetworkManager

_chronyd_ 可以通过 [NetworkManager 调度脚本](<../zh-cn/NetworkManager.html#Network_services_with_NetworkManager_dispatcher> "NetworkManager")随网络连接状态进入在线/离线状态。创建一个软链接来使用上游分发的 NetworkManager 调度脚本： 
    
    ln -s /usr/share/doc/chrony/examples/chrony.nm-dispatcher.onoffline /etc/NetworkManager/dispatcher.d/20-chrony-onoffline.sh
    
你也可以选择安装 [networkmanager-dispatcher-chrony](<https://aur.archlinux.org/packages/networkmanager-dispatcher-chrony/>)AUR。 

### netctl

从 AUR 安装 [netctl-dispatcher-chrony](<https://aur.archlinux.org/packages/netctl-dispatcher-chrony/>)AUR。这会为 netctl 添加一个钩子，随任意网络连接自动运行。 

### dhcpcd

创建如下钩子： 
    
    /etc/dhcpcd.exit-hook
    
    if $if_up; then
    	chronyc online
    elif $if_down; then
    	chronyc offline
    fi
    
详情可参考 [dhcpcd-run-hooks(8)](<https://man.archlinux.org/man/dhcpcd-run-hooks.8>)。 

##  参考

  * [System time](<../zh-cn/System_time.html> "System time") (for more information on computer timekeeping)
  * <https://chrony-project.org/>
  * <https://www.ntp.org/>
  * <https://support.ntp.org/bin/view/Main/WebHome>
  * <https://www.ntppool.org/en/>
  * <https://www.eecis.udel.edu/~mills/ntp/html/index.html>
  * <https://www.akadia.com/services/ntp_synchronize.html>
