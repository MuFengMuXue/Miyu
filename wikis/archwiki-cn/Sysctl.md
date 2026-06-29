**翻译状态：**

  * 本文（或部分内容）译自 [Sysctl](<https://wiki.archlinux.org/title/Sysctl> "arch:Sysctl")，最近一次同步于 2025-04-12，若英文版本有所[更改](<https://wiki.archlinux.org/title/Sysctl?diff=0&oldid=830310>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Sysctl_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[sysctl](<https://en.wikipedia.org/wiki/sysctl> "wikipedia:sysctl")是一种用于在运行时检查和更改[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数")的工具。sysctl在[procfs](<https://en.wikipedia.org/wiki/procfs> "wikipedia:procfs")中实现，procfs 是位于`/proc/`的虚拟进程文件系统。 

##  安装

[procps-ng](<https://archlinux.org/packages/?name=procps-ng>)包 包应该已经[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")了，因为它是 [base](<https://archlinux.org/packages/?name=base>)包 [元包](<../zh-cn/%E5%85%83%E8%BD%AF%E4%BB%B6%E5%8C%85%E5%92%8C%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%BB%84.html> "元软件包和软件包组")的依赖项。 

##  配置

**sysctl** 预加载/配置文件可以在 `/etc/sysctl.d/99-sysctl.conf` 中创建。对于 [systemd](<../zh-cn/Systemd.html> "Systemd")，`/etc/sysctl.d/` 和 `/usr/lib/sysctl.d/` 是内核 sysctl 参数的配置目录。命名和源目录决定了处理的顺序，这很重要，因为处理的最后一个参数可能会覆盖前面的参数。例如，`/usr/lib/sysctl.d/50-default.conf` 中的参数将被 `/etc/sysctl.d/50-default.conf` 中的相同参数以及之后从这两个目录处理的任何配置文件覆盖。 

要手动加载所有配置文件，可以执行： 
    
    # sysctl --system 
    
这也将输出应用的层次结构。单个参数文件也可以显式加载： 
    
    # sysctl --load=_filename.conf_
    
有关详细信息，请参阅[新的配置文件](<http://0pointer.de/blog/projects/the-new-configuration-files>)新的配置文件，更具体地说是 [sysctl.d(5)](<https://man.archlinux.org/man/sysctl.d.5>)。 

可用参数列在 `/proc/sys/` 下。 例如，`kernel.sysrq` 参数指的是文件系统上的文件 `/proc/sys/kernel/sysrq`。 `sysctl --all` 命令可用于显示所有当前可用的值。 

**注意：** 如果您安装了内核文档 ([linux-docs](<https://archlinux.org/packages/?name=linux-docs>)包)，您可以在 `/usr/lib/modules/$(uname -r)/build/Documentation/admin-guide/sysctl/` 中找到有关 sysctl 设置的详细信息。在线版本由本文的[#参阅](<#%E5%8F%82%E9%98%85>)部分引用。强烈建议在更改 sysctl 设置之前阅读这些内容。

也可以通过文件操作或使用 [sysctl(8)](<https://man.archlinux.org/man/sysctl.8>) 实用程序更改设置。例如，临时启用[万能SysRq键](<https://en.wikipedia.org/wiki/Magic_SysRq_key> "wikipedia:Magic SysRq key")： 
    
    # sysctl kernel.sysrq=1
    
或者: 
    
    # echo "1" > /proc/sys/kernel/sysrq 
    
有关 `kernel.sysrq` 的详细信息，请参阅 [Linux 内核文档](<https://docs.kernel.org/admin-guide/sysrq.html>)。 

要在重新启动之间保留更改，在`/etc/sysctl.d/99-sysctl.conf` 以及`/etc/sysctl.d/` 中的配置文件中[Help:Reading#添加、创建、编辑文件](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Help:Reading")或修改对应的行。 

**提示：** 一些参数是否生效可能取决于内核模块，而这些内核模块又可能不会被加载。 例如 `/proc/sys/net/bridge/*` 中的参数依赖于 `br_netfilter` 模块。如果`br_netfilter`没有在运行时（或重启后）加载，那么这些参数将 _安静的_ 不生效。参见[内核模块](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html> "内核模块")。

##  安全

参阅[安全#内核加固](<../zh-cn/%E5%AE%89%E5%85%A8.html#%E5%86%85%E6%A0%B8%E5%8A%A0%E5%9B%BA> "安全")，以及本文的其余部分。 

##  网络

###  性能优化

####  增加接收队列的大小

进入系统的网络数据帧在从网卡上的环形缓冲区中取出后，会存放在这个队列中。 

在使用高速网卡时增加系统的这个设定值可能有助于防止数据包丢失： 
    
    net.core.netdev_max_backlog = 16384
    
**注意：** 在 SIP 路由器等实时应用中，此选项需要高速 CPU，否则队列中的数据将过时。

####  增加最大连接数

可以更改设置内核接受的连接数上限（默认 4096）： 
    
    net.core.somaxconn = 8192
    
**警告：** 增加此值可能只会提高高负载服务器的性能，并可能导致处理速度变慢（例如单线程阻塞服务器）或工作线程/进程数量不足。[[1]](<https://serverfault.com/questions/518862/will-increasing-net-core-somaxconn-make-a-difference/519152>).

####  增加专用于网络接口的内存

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 需要解释清楚每个选项的单位是什么（字节、千字节或是内存页？） (在 [Talk:Sysctl](<../zh-cn/Talk:Sysctl.html>) 中讨论)

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 本节似乎受到 Cloudflare 博客文章的启发，但 [Red Hat's tuned profile](<https://github.com/redhat-performance/tuned/blob/master/profiles/network-throughput/tuned.conf#L10>) 建议使用更小的值，并声称“这似乎只在 40Gb 速度下才有必要”。 因此，这些设置似乎对消费级硬件不实用。（在 [Talk:Sysctl](<../zh-cn/Talk:Sysctl.html>) 中讨论）

默认情况下，Linux 网络堆栈未配置为通过 WAN 链接进行高速大文件传输（即处理更多网络数据包），设置正确的值可以节省内存资源： 
    
    net.core.rmem_default = 1048576
    net.core.rmem_max = 16777216
    net.core.wmem_default = 1048576
    net.core.wmem_max = 16777216
    net.core.optmem_max = 65536
    net.ipv4.tcp_rmem = 4096 1048576 2097152
    net.ipv4.tcp_wmem = 4096 65536 16777216
    
也可以增加默认的 `4096` UDP 限制： 
    
    net.ipv4.udp_rmem_min = 8192
    net.ipv4.udp_wmem_min = 8192
    
有关详细信息和推荐值，请参阅以下来源： 

  * <http://www.nateware.com/linux-network-tuning-for-2013.html>
  * <https://blog.cloudflare.com/the-story-of-one-latency-spike/>

####  启用 TCP Fast Open

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 提及"默认情况下使所有侦听器支持快速打开而无需手动显式设置 TCP_FASTOPEN sockect 选项，即值 `1027` (0x1+0x2+0x400)。" (在 [Talk:Sysctl#TCP Fast Open](</wzh/index.php?title=Talk:Sysctl&action=edit&redlink=1> "Talk:Sysctl（页面不存在）") 中讨论)

TCP Fast Open 是传输控制协议 (TCP) 的扩展，它通过在发送方的初始 TCP SYN [[2]](<https://www.keycdn.com/support/tcp-fast-open/>) 时使用值 `3` 而不是默认值 `1` 允许传入和传出连接的 TCP 快速打开： 
    
    net.ipv4.tcp_fastopen = 3
    
####  调整挂起的连接处理

`tcp_max_syn_backlog` 是挂起连接 _等待确认_ 的最大队列长度。 

在碰到 synflood DOS 攻击的情况下，这个队列会很快填满，此时 [TCP SYN cookies](<https://en.wikipedia.org/wiki/SYN_cookies> "wikipedia:SYN cookies") 将开始允许您的系统继续响应合法流量，并允许您获得阻止恶意 IP 的权限。 

如果服务器在高峰时间系统网络过载，您可能需要稍微增加此值： 
    
    net.ipv4.tcp_max_syn_backlog = 8192
    
`tcp_max_tw_buckets` 表示系统内允许处于 TIME_WAIT 状态的最大sockect连接数。 

达到此数字后，系统将开始销毁处于此状态的 socket 连接。 

增加该值可以防止简单的 DOS 攻击： 
    
    net.ipv4.tcp_max_tw_buckets = 2000000
    
`tcp_tw_reuse` 设置当新时间戳严格大于上一个连接记录的最新时间戳时，TCP 是否应该为新的传出连接重用 TIME-WAIT 状态下的现有连接。 

默认值为 `2`，表示仅对回环连接启用。您可以将其设置为 `1` 以对所有连接启用，这有助于避免用完可用的网络 sockets： 
    
    net.ipv4.tcp_tw_reuse = 1
    
指定在强制关闭 socket 之前需要等待的最终 FIN 数据包时间（秒数）。这完全违反了 TCP 规范，但防止拒绝服务攻击需要这个。在 Linux 2.2 中，默认值为 180 [[3]](<https://access.redhat.com/solutions/41776>)： 
    
    net.ipv4.tcp_fin_timeout = 10
    
`tcp_slow_start_after_idle` 设置 TCP 是否应仅对新连接或空闲时间过长的现有连接开启'以默认窗口大小启动连接'。 

此设置会破坏持久的单连接性能，可以将其关闭： 
    
    net.ipv4.tcp_slow_start_after_idle = 0
    
####  更改 TCP 保活参数

[TCP 保活](<https://en.wikipedia.org/wiki/Keepalive#TCP_keepalive> "wikipedia:Keepalive")是一种 TCP 连接机制，有助于确定另一端是否已停止响应。TCP会在一段时间的空闲时间后，多次向网络对端发送包含空数据的保活探测。如果对端没有响应，socket 将自动关闭。默认情况下，TCP 保活进程在发送第一个保活探测之前等待 socket 活动两个小时（7200 秒），然后每75秒重新发送一次。只要有 TCP/IP socket 通信在进行并处于活动状态，就不需要保活数据包。 

**注意：** 使用以下设置，您的应用程序将在120秒后才检测失效 TCP 连接 (60s + 10s + 10s + 10s + 10s + 10s + 10s)。
    
    net.ipv4.tcp_keepalive_time = 60
    net.ipv4.tcp_keepalive_intvl = 10
    net.ipv4.tcp_keepalive_probes = 6
    
####  启用 MTU 探测

[最大传输单元 (MTU)](<https://en.wikipedia.org/wiki/Maximum_transmission_unit> "wikipedia:Maximum transmission unit") 越长，性能越好，但可靠性越差。 

这是因为MTU设置大了一旦发生数据包丢失就意味着需要重新传输的数据更多，而且互联网上的许多路由器并不能传送非常长的数据包： 
    
    net.ipv4.tcp_mtu_probing = 1
    
更多信息，可以参阅[这篇文章](<https://blog.cloudflare.com/path-mtu-discovery-in-practice/>)。 

####  TCP 时间戳

**警告：** TCP 时间戳可以防止 TCP 实现中的（以Gbps速度传输的）序号回绕（sequence numbers wrap-around）问题和时间的重复计算问题，参考 [RFC 1323](<https://www.rfc-editor.org/rfc/rfc1323>)。不建议关闭 TCP 时间戳，因为它可能会导致安全风险[[4]](<https://access.redhat.com/sites/default/files/attachments/20150325_network_performance_tuning.pdf>)。

禁用时间戳生成可以减少低性能尖峰的发生并可能提高千兆网络的性能： 
    
    net.ipv4.tcp_timestamps = 0
    
也可以参考[这篇文章](<https://perthcharles.github.io/2015/08/27/timestamp-intro/>)了解关于 TCP 时间戳的信息。 

####  TCP 选择性确认

TCP 选择性确认 (TCP SACK)，由布尔值 `tcp_sack` 控制，允许接收方向发送方提供有关丢失段的更多详细信息，从而减少重传量。这在延迟较高的网络上非常有用，但在高速局域网上禁用此功能可以提高吞吐量。如果您不发送 SACK，也请禁用 `tcp_dsack`，因为您肯定不希望发送重复数据！前向确认在 SACK 之上工作，如果 SACK 被禁用，它也将被禁用。[[5]](<https://cromwell-intl.com/open-source/performance-tuning/tcp.html>)
    
    net.ipv4.tcp_sack = 1
    
####  启用 BBR

[BBR 拥塞控制算法](<https://en.wikipedia.org/wiki/TCP_congestion_control#TCP_BBR> "wikipedia:TCP congestion control")可以帮助实现更高的带宽和更低的互联网流量延迟。 

启用 BBR 需要先[加载](<../zh-cn/Kernel_module.html#Manual_module_handling> "Kernel module") `tcp_bbr` 模块。 

**注意：**[BBR GitHub says](<https://github.com/google/bbr/blob/master/README.md>), "这不是 Google 的官方产品。"
    
    net.core.default_qdisc = cake
    net.ipv4.tcp_congestion_control = bbr
    
####  增加临时端口范围

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 此更改可以提高性能？原理是什么？（在 [Talk:Sysctl#net.ipv4.ip_local_port_range](</wzh/index.php?title=Talk:Sysctl&action=edit&redlink=1> "Talk:Sysctl（页面不存在）") 中讨论）

通常传输控制协议 (TCP)、用户数据报协议 (UDP) 或流控制传输协议 (SCTP) 会使用[Wikipedia:Ephemeral port](<https://en.wikipedia.org/wiki/Ephemeral_port> "wikipedia:Ephemeral port") 作为客户端与服务器端之间的端口分配协商。 
    
    net.ipv4.ip_local_port_range = 30000 65535
    
###  TCP/IP 协议栈加固

下面指定了一个参数集，用于加强 IPv4 协议内核的网络安全选项，并且也存在等效项的相关 IPv6 参数。 

对于某些用例，例如将系统用作[路由器](<../zh-cn/%E8%B7%AF%E7%94%B1%E5%99%A8.html> "路由器")，其他参数也可能有用或需要。 

####  TCP SYN cookie 保护

此项设置有助于抵御 SYN 洪水攻击。只有访问请求达到 `net.ipv4.tcp_max_syn_backlog` 时才会启动。更多详细信息，例如 [[6]](<https://cateee.net/lkddb/web-lkddb/SYN_COOKIES.html>)。 从 [linux](<https://archlinux.org/packages/?name=linux>)包 5.10 开始，它是默认设置的。 
    
    net.ipv4.tcp_syncookies = 1
    
#### TCP rfc1337

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 这好像不是 TCP 标准的一部分？ 描述可能不准确。[[7]](<https://serverfault.com/questions/787624/why-isnt-net-ipv4-tcp-rfc1337-enabled-by-default>)（在 [Talk:Sysctl#net.ipv4.tcp_rfc1337](</wzh/index.php?title=Talk:Sysctl&action=edit&redlink=1> "Talk:Sysctl（页面不存在）") 中讨论）

可以防止 tcp time-wait assassination 缺陷，丢弃处于 time-wait 状态的 socket 的 RST 数据包。 除 Linux 之外并不广泛支持，但符合 RFC： 
    
    net.ipv4.tcp_rfc1337 = 1
    
####  反向路径过滤

通过启用反向路径过滤，内核将对从机器上所有网络接口接收到的数据包进行来源验证。这可以防止使用 IP 欺骗方法的攻击者破坏系统。 

内核的 `net.ipv4 .conf.all.rp_filter` 默认值为 `0`（关闭来源验证），但 systemd 提供默认 `/usr/lib/sysctl.d/50-default.conf` 将其设置到 `2`（宽松模式）[[8]](<https://github.com/systemd/systemd/pull/10971>)。 

以下配置将反向路径过滤机制设置为值 `1` （严格模式）： 
    
    net.ipv4.conf.default.rp_filter = 1
    net.ipv4.conf.all.rp_filter = 1
    
[ip-sysctl.html 这里](<https://docs.kernel.org/networking/ip-sysctl.html>)解释了 `net.ipv4.conf.default.*`、`net.ipv4.conf._interface_.*` 和 `net.ipv4.conf.all.*` 之间的关系和行为。 

####  记录 martian 数据包

[martian 数据包](<https://en.wikipedia.org/wiki/Martian_packet> "wikipedia:Martian packet")是指那些包内的源地址或目标地址被设置成 [IP 保留地址](<https://en.wikipedia.org/wiki/Reserved_IP_addresses> "wikipedia:Reserved IP addresses")的特殊数据包。IP 保留地址由 [IANA](<https://en.wikipedia.org/wiki/Internet_Assigned_Numbers_Authority> "wikipedia:Internet Assigned Numbers Authority") 为了特殊用途而保留。这些包要么在广域网上要么根本无法传输数据，要么包内的源地址与实际的发包源地址不符（例如特地伪造虚假源地址的数据包）。 
    
    net.ipv4.conf.default.log_martians = 1
    net.ipv4.conf.all.log_martians = 1
    
**注意：** 这可能会导致大量信息填满您的日志，建议仅在测试时启用它。

####  禁用 ICMP 重定向

相关背景知识可以参考[什么是 ICMP 重定向？ 他们应该被阻止吗？](<https://askubuntu.com/questions/118273/what-are-icmp-redirects-and-should-they-be-blocked>)

下面的配置用来禁用 ICMP 重定向的接收功能： 
    
    net.ipv4.conf.all.accept_redirects = 0
    net.ipv4.conf.default.accept_redirects = 0
    net.ipv4.conf.all.secure_redirects = 0
    net.ipv4.conf.default.secure_redirects = 0
    net.ipv6.conf.all.accept_redirects = 0
    net.ipv6.conf.default.accept_redirects = 0
    
下面的配置用来在非路由器上禁用 ICMP 重定向的发送功能： 
    
    net.ipv4.conf.all.send_redirects = 0
    net.ipv4.conf.default.send_redirects = 0
    
####  忽略 ICMP 回应请求

要禁用 ICMP 回应（又叫 ping）请求： 
    
    net.ipv4.icmp_echo_ignore_all = 1
    net.ipv6.icmp.echo_ignore_all = 1
    
**注意：** 请注意，这可能会导致依赖 ICMP 回显（ping）响应的网络记录工具和或应用程序出现问题。

###  其它

####  允许非特权用户创建 IPPROTO_ICMP socket

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** `/usr/lib/sysctl.d/50-default.conf` 会将 `net.ipv4.ping_group_range` 设置为 `0 2147483647`. (在[Talk:Sysctl](<../zh-cn/Talk:Sysctl.html>)讨论)

IPPROTO_ICMP ([icmp(7)](<https://man.archlinux.org/man/icmp.7>)) socket 类型增加了在不打开 [raw(7)](<https://man.archlinux.org/man/raw.7>) socket 的情况下发送 ICMP_ECHO 消息和接收相应 ICMP_ECHOREPLY 消息的功能，该操作需要设置 CAP_NET_RAW [功能权限](<../zh-cn/Capabilities.html> "Capabilities")或具有指定特权用户的 SUID 位。这些 ICMP_ECHO 消息由 [ping](</wzh/index.php?title=Ping&action=edit&redlink=1> "Ping（页面不存在）") 应用程序发送，因此除了 ICMP Echo socket 之外，IPPROTO_ICMP socket 也称为 ping socket。 

`ping_group_range` 确定允许其用户创建 IPPROTO_ICMP socket 的组的 GID 范围。此外，还允许有 CAP_NET_RAW 功能权限的用户创建 IPPROTO_ICMP socket。默认情况下这个范围是 `1 0`，意味着除了 root 之外没有人被允许创建 IPPROTO_ICMP socket。要利用这项设置，当前使用原始 socket 的程序需要移植到使用 IPPROTO_ICMP socket。例如，QEMU 将 IPPROTO_ICMP 用于 SLIRP，即用户模式网络，因此允许运行 QEMU 的用户创建 IPPROTO_ICMP socket，这样就可以在客户机内进行 ping 操作了。 

下面的配置只允许 GID 为 100 的组成员的用户创建 IPPROTO_ICMP 套接字： 
    
    net.ipv4.ping_group_range = 100 100
    
下面的配置允许系统中的所有用户创建 IPPROTO_ICMP 套接字： 
    
    net.ipv4.ping_group_range = 0 65535
    
##  虚拟内存

有几个关键参数可以调整 Linux 内核的[虚拟内存](<https://en.wikipedia.org/wiki/virtual_memory> "wikipedia:virtual memory")子系统的操作以及将脏数据（dirty data）写出到磁盘。有关详细信息，请参阅官方 [Linux 内核文档](<https://docs.kernel.org/admin-guide/sysctl/vm.html>)。 例如： 

  * `vm.dirty_ratio = 10`

    包括占可用内存总量（可用页面和可回收页面）的百分比，和正在发生磁盘写入的进程本身将开始写出脏数据的页数。

  * `vm.dirty_background_ratio = 5`

    包括可用页面和可回收页面的总可用内存的百分比以及后台内核刷新线程将要开始写出脏数据的页数。

如参数注释中所述，在设置这些值时需要考虑 RAM 总量。例如，可以通过用已安装的系统内存而不是可用内存来简化计算： 

**警告：**

  * 较高的比率值可能会提高性能，但也会增加数据丢失的风险。
  * 将此值设置为 `0` 可能会导致更高的磁盘延迟和低性能尖峰。

更多信息请参考 [[9]](<https://lonesysadmin.net/2013/12/22/better-linux-disk-caching-performance-vm-dirty_ratio/>)。 

  * 共识是，如果 RAM 为 1 GB，则将 `vm.dirty_ratio` 设置为 RAM 的 10% 是一个合理的值（10% 也就是 100 MB）。 但是如果机器有更多的 RAM，比如 16 GB（10% 就是 1.6 GB），这个百分比可能因为机械磁盘上旋转回写的几秒钟时间差异而不是线性的。 在这种情况下更合理的值可能是 `3`（16 GB 的 3% 大约是 491 MB）。
  * 同样，将 `vm.dirty_background_ratio` 设置为 `5` 可能只适用于小内存值，所以要考虑并根据特定系统上的内存容量进行相应调整。

###  VFS 缓存

降低[虚拟文件系统](<https://docs.kernel.org/filesystems/vfs.html>) (VFS) 缓存参数值可能会提高系统响应能力： 

  * `vm.vfs_cache_pressure = 50`

    这个值控制内核回收用于缓存目录和 inode 对象（即 VFS 缓存）内存的积极性。 将它从默认值 100 降低会使内核不太愿意回收 VFS 缓存（不要将其设置为 0，这可能会产生内存不足的情况）。

## MDADM

参考 [RAID#修改同步速度限制](<../zh-cn/RAID.html#%E4%BF%AE%E6%94%B9%E5%90%8C%E6%AD%A5%E9%80%9F%E5%BA%A6%E9%99%90%E5%88%B6> "RAID")。 

##  故障排除

###  小周期系统冻结

如果遇到这个问题，可以将脏字节（dirty bytes）设置为足够小的值（例如 4M）： 
    
    vm.dirty_background_bytes = 4194304
    vm.dirty_bytes = 4194304
    
**注意：**`dirty_background_bytes` 和 `dirty_bytes` 参数是 `dirty_background_ratio` 和 `dirty_ratio` 的对应项（如 [#虚拟内存](<#%E8%99%9A%E6%8B%9F%E5%86%85%E5%AD%98>) 中所示）。一次只能指定一个参数。

##  参考资料

  * [sysctl(8)](<https://man.archlinux.org/man/sysctl.8>) 和 [sysctl.conf(5)](<https://man.archlinux.org/man/sysctl.conf.5>)
  * `/proc/sys/` 的[内核文档](<https://docs.kernel.org/admin-guide/sysctl/index.html>)
  * 内核文档: [IP Sysctl](<https://docs.kernel.org/networking/ip-sysctl.html>)
  * [sysctl的内核网络参数](<https://tldp.org/HOWTO/Adv-Routing-HOWTO/lartc.kernel.html>)
  * [sysctl-explorer.net – 促进使用 Linux 的 sysctl 参考文档的倡议](<https://sysctl-explorer.net>)
  * [Disable Source Routing - Red Hat 客户门户](<https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/security_guide/sect-security_guide-server_security-disable-source-routing>)
  * [SUSE 内核安全特性手册](<https://www.suse.com/documentation/sles11/book_hardening/data/sec_sec_prot_general_kernel.html>)
  * [Linux sysctl 调优](<https://enterprise-support.nvidia.com/s/article/linux-sysctl-tuning>)
