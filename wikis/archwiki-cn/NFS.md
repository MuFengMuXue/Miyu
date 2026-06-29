**翻译状态：**

  * 本文（或部分内容）译自 [NFS](<https://wiki.archlinux.org/title/NFS> "arch:NFS")，最近一次同步于 2024-07-06，若英文版本有所[更改](<https://wiki.archlinux.org/title/NFS?diff=0&oldid=811819>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/NFS_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** Some content is not translated.（在 [Talk:NFS#](<../zh-cn/Talk:NFS.html>) 中讨论）

来自[维基百科](<https://en.wikipedia.org/wiki/Network_File_System> "wikipedia:Network File System")：NFS 网络文件系统（Network File System）是由 Sun 公司 1984 年发布的分布式文件系统协议。它允许客户端上的用户像访问本地文件一样地访问网络上的文件。 

**注意：**

  * 默认情况下，NFS不提供加密功能. 在处理敏感数据时,请使用 [#TLS 加密](<#TLS_%E5%8A%A0%E5%AF%86>) 或 [Kerberos](<../zh-cn/Kerberos.html> "Kerberos")（使用 `sec=krb5p` 提供基于 Kerberos 的加密），也可以使用类似 WireGuard 的加密 [VPN](<../zh-cn/Category:Virtual_Private_Network_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html> "Category:Virtual Private Network \(简体中文\)") 协议传输NFS流量.
  * 与 [Samba](<../zh-cn/Samba.html> "Samba") 不同, NFS默认不提供任何验证用户的方法,客户端访问限制是通过 IP 地址和/或[计算机名](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html#%E8%AE%BE%E7%BD%AE%E8%AE%A1%E7%AE%97%E6%9C%BA%E5%90%8D> "网络配置")实现的。如果需要更强的加密方式，也可以使用 Kerberos。
  * NFS期望[用户](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E7%94%A8%E6%88%B7%E7%AE%A1%E7%90%86> "用户和用户组")和/或[用户组](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E7%94%A8%E6%88%B7%E7%BB%84%E7%AE%A1%E7%90%86> "用户组")的 ID 在客户端与服务端上是相同的（使用 Kerberos 的情况下除外）。使用[启用 NFSv4 ID 映射](<#%E5%90%AF%E7%94%A8_NFSv4_ID_%E6%98%A0%E5%B0%84>),或使用`anonuid`/`anongid`并在`/etc/exports`中启用`all_squash`,手动改变 UID/GID 来解决这一问题.
  * NFS 不支持 [POSIX ACL](<../zh-cn/%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6%E5%88%97%E8%A1%A8.html> "访问控制列表")。NFS 服务器还是会强制应用 ACL 规则，但客户端无法观察或是对其进行修改。

##  安装

客户端和服务端都只需要[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [nfs-utils](<https://archlinux.org/packages/?name=nfs-utils>)包 包。 

强烈建议使用[时间同步守护进程](<../zh-cn/%E7%B3%BB%E7%BB%9F%E6%97%B6%E9%97%B4.html#%E6%97%B6%E9%92%9F%E5%90%8C%E6%AD%A5> "系统时间")以保持客户端/服务器之间的时间同步，如果各个节点上没有精确同步的时钟，NFS 可能产生非预期的延迟。 

##  服务端配置

全局设置选项在 `/etc/nfs.conf` 中被列出.只进行简单配置的用户无需编辑此文件. 

NFS 服务器需要按照 `/etc/exports` 或 `/etc/exports.d/*.exports` 文件中定义的“导出”文件夹列表进行共享(详细介绍参见 [exports(5)](<https://man.archlinux.org/man/exports.5>))。默认情况下，这些目录都会按路径原样导出，例如： 
    
    /etc/exports
    
    /data/music    192.168.1.0/24(rw)

以上配置将把 `/data/music` 暴露到 `MyServer:/data/music` 路径下，可通过 NFSv3 或 NFSv4 进行挂载。 

###  指定导出根目录

共享对象是相对于所谓的“NFS 根目录”的.出于安全考虑，建议定义一个单独的目录为 NFS 根，这可以将用户限制在该挂载点中。绑定的挂载点（bind mounts）将[文件系统](</wzh/index.php?title=File_systems_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)&action=edit&redlink=1> "File systems \(简体中文\)（页面不存在）")上他处的目录与被分享的挂载点连接起来。之前 NFSv4 强制要求使用 NFS 根目录，现在成了可选项（从内核 2.6.33 和 nfs-utils 1.2.2 版本开始实现了虚拟根目录）。 

查看下面的例子。在本例中： 

  1. NFS 根目录是 `/srv/nfs`
  2. 将要共享的目录是 `/srv/nfs/music`，该目录以绑定挂载方式指向了它实际的位置`/mnt/music`。

    # mkdir -p /srv/nfs/music /mnt/music
    # mount --bind /mnt/music /srv/nfs/music
    
**注意：**[ZFS](<../zh-cn/ZFS.html> "ZFS") 文件系统对于 bindmounts 方式挂载要特殊处理，参阅 [ZFS#Bind mount](<../zh-cn/ZFS.html#Bind_mount> "ZFS")。

为了让服务器重启后共享仍旧有效，增加绑定到 `fstab` 文件： 
    
    /etc/fstab
    
    /mnt/music /srv/nfs/music  none   bind   0   0
    
增加允许被挂载的目录和使其只能被属于特定 CIDR 所指定的 IP 范围或拥有特定主机名的客户端所访问的限制至 `/etc/exports` 文件,例如： 
    
    /etc/exports
    
    /srv/nfs        192.168.1.0/24(rw,fsid=root)
    /srv/nfs/music  192.168.1.0/24(rw,sync)
    /srv/nfs/home   192.168.1.0/24(rw,sync)
    /srv/nfs/public 192.168.1.0/24(ro,all_squash,insecure) desktop(rw,sync,all_squash,anonuid=99,anongid=99) # 将访客映射到特定用户组 - 在本例中是 _nobody_

在使用 NFSv4 时，`fsid=root` 或 `fsid=0` 选项指定了导出目录“根”的位置；如果使用这些选项指定了导出目录，那其它文件夹都必须位于该文件夹下。`/etc/nfs.conf` 文件中的 `rootdir` 选项在这种情况下不起效。如果没有指定 `fsid=0`，那默认行为与 NFSv3 一致。 

在上面的实例中，`/srv/nfs` 被指定为根，且可以通过 NFSv4 按 `MyServer:/music` 目录挂载 `/srv/nfs/music` 文件夹 - 注意，根目录前缀被省略了。 

**提示：**

  * 对 NFSv3 而言（不适用于 NFSv4），`crossmnt` 选项使客户端可以访问**所有** 挂载在文件系统上并标记有 `crossmnt` 的文件系统并且客户端不需要单独逐个挂载子共享. 请注意,你可能不希望在子共享同时被共享到另一端地址时使用该选项.
  * 除了 `crossmnt` 之外，你也可以在子共享上使用 `nohide` 选项，这样的话,子共享就会在根共享被挂载时自动挂载。与 `crossmnt` 不同的是，`nohide` 仍然会遵守子共享的地址范围。注意，该选项仅适用于 NFSv3，NFSv4 _永远_ 表现为该选项已启用。
  * `insecure` 选项使客户端可以用高于 1023 的端口进行连接。（大概是只有 root 用户可以使用较低编号的端口，因此阻断其它端口可以作为简单的访问控制方法。在实际使用中，使用 `insecure` 选项与否并不能带来任何安全方面的提升或是下降。）
  * 使用一个通配符（`*`）以允许来自所有接口的访问.

如果服务运行时修改了 `/etc/exports` 文件， 你需要重新导出使其生效: 
    
    # exportfs -arv
    
想要查看已经加载的共享的详细信息,请使用: 
    
    # exportfs -v
    
有关所有可用选项的详细介绍,请参阅[exports(5)](<https://man.archlinux.org/man/exports.5>). 

**提示：**[ip2cidr](<https://ip2cidr.com/>) 是一个可以将 IP 范围转换为 CIDR 的工具.

**注意：** 如果共享是[tmpfs](<../zh-cn/Tmpfs.html> "Tmpfs")文件系统,你需要指定`fsid=1`选项.

###  开始运行服务

  * 要提供 NFSv3 和 NFSv4 服务，[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")和[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `nfs-server.service`。

  * 要仅提供 NFSv4 服务，[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")和[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `nfsv4-server.service`。

v4 版本协议的用户可能需要至少[屏蔽](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Help:Reading")掉 `rpcbind.service` 和 `rpcbind.socket`，以防止不需要的服务自启，详细信息请参考 [[1]](<https://bugs.archlinux.org/task/76453>)。另外，也可以禁用 `nfs-server.service` 以防止其由于某些原因而被拉起。 

**注意：** 在启用ZFS共享的同时，请一并[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")/[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `zfs-share.service`。如果不这么做的话，在重启之后 ZFS 目录不会被共享.参阅 [ZFS#NFS](<../zh-cn/ZFS.html#NFS> "ZFS").

###  限制 NFS 使其只允许来自特定接口/IP 地址的访问

默认情况下，启动 `nfs-server.service` 会忽略 `/etc/exports` 文件的内容，而是在所有网络接口上监听连接。可以通过定义监听的IP和/或主机名来改变这一行为。 
    
    /etc/nfs.conf
    
    [nfsd]
    host=192.168.1.123
    # 或者也可以使用主机名
    # host=myhostname

在修改完后，[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `nfs-server.service` 以应用设置。 

###  防火墙配置

如果要访问[防火墙](<../zh-cn/Category:%E9%98%B2%E7%81%AB%E5%A2%99.html> "防火墙")后的 NFSv4 服务器，就需要开放 `2049` 端口的 TCP 上行连接。（NFSv4 使用静态网络端口；它不使用任何像 mountd 或是 portmapper 这样的辅助服务。） 

如果要访问 NFSv3 服务器，就还需要额外为 portmapper（rpcbind）开放 `111` 端口的 TCP/UDP 连接，还需要为 MOUNT（rpc.mountd）开放端口。默认情况下，rpc.mountd 会动态选择端口，所以如果你要访问防火墙后的服务，就需要通过编辑 `/etc/nfs.conf` 配置来选择一个固定端口。可以使用 `rpcinfo -p` 查看 NFSv3 服务器使用的具体端口信息： 
    
    $ rpcinfo -p
    
    100003    3   tcp   2049  nfs
    100003    4   tcp   2049  nfs
    100227    3   tcp   2049  nfs_acl
    ...
    
##  客户端配置

打算将 NFS4 与 [Kerberos](<../zh-cn/Kerberos.html> "Kerberos") 一起使用的用户需要[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")并[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `nfs-client.target`. 

###  手动挂载

对于NFSv3，请使用以下命令显示服务器分享的文件系统： 
    
    $ showmount -e _servername_
    
对于NFSv4，请挂载NFS根目录，并查看可用的挂载： 
    
    # mount _servername_ :/ _/mountpoint/on/client_
    
然后挂载分享.挂载时省略服务器的NFS分享根目录： 
    
    # mount -t nfs -o vers=4 _servername_ :/music _/mountpoint/on/client_
    
如果挂载失败，请尝试包括服务器的分享根目录（对于Debian/RHEL/SLES是必需的，某些发行版需要使用`-t nfs4`而不是`-t nfs`）： 
    
    # mount -t nfs -o vers=4 _servername_ :/srv/nfs/music _/mountpoint/on/client_
    
**注意：**` _servername_` 必须被替换为有效的主机名（而不仅仅是IP地址）。否则，挂载远程共享将挂起。

###  使用/etc/fstab挂载

对于服务器保持开启，且无论客户端何时启动皆可用的 NFS 共享而言，[fstab](<../zh-cn/Fstab.html> "Fstab") 非常有用。编辑 `/etc/fstab`，然后根据需要添加一行新配置。同样，服务端的 NFS 导出根路径已被缺省。 
    
    /etc/fstab
    
    servername:/music   /mountpoint/on/client   nfs   defaults,timeo=900,retrans=5,_netdev	0 0

**注意：** 更多挂载选项可参考 [nfs(5)](<https://man.archlinux.org/man/nfs.5>) 和 [mount(8)](<https://man.archlinux.org/man/mount.8>)。

以下为一些可参考的挂载选项： 

rsize 和 wsize：`rsize` 指单次请求从服务器读取的字节数，`wsize` 指单次请求向服务器写入的字节数。默认情况下，如果未指定值，客户端和服务端会协商使用它们都支持的最大值（参考 [nfs(5)](<https://man.archlinux.org/man/nfs.5>)）。修改值后，建议进行性能测试（参考[#性能调优](<#%E6%80%A7%E8%83%BD%E8%B0%83%E4%BC%98>)）。

soft 或 hard：决定在 NFS 请求超时后的恢复行为。如果没有指定（或者指定了 `hard` 选项），NFS 会无限重试请求。如果指定了 `soft` 选项，那么 NFS 客户端会在重试 _retrans_ 指定的次数后失败，导致 NFS 客户端向发起应用返回错误。

**警告：**`soft`（软）超时在某些情况下会导致数据静默损坏。因此，建议仅在客户端响应度优先于于数据完整性的情况下使用 `soft` 选项。使用基于 TCP 传输的 NFS 或增加 `retrans` 选项数值有助于降低使用 `soft` 导致的故障风险。

timeo：`timeo` 表示在遇到 RPC 超时后重发前的等待时间，单位为十分之一秒。对基于 TCP 的 NFS 而言默认值为 600（即 60 秒）。在首次超时后，超时值都将加倍，最大不超过 60 秒或是出现重大超时。在连接到慢速服务器或是使用高负载网络时，增加超时值有助于提高连接稳定性。

retrans：NFS 客户端在执行下一步恢复操作前的请求重试次数。如果未指定 `retrans` 值，那 NFS 客户端会为请求重试 3 次。在 _retrans_ 次重试后，NFS 客户端会生成一条“server not responding”消息，然后进行下一步恢复尝试（取决于是否使用了硬挂载选项）。

_netdev：`_netdev` 选项告知系统在网络就绪后再尝试挂载该共享 - [systemd](<../zh-cn/Systemd.html> "Systemd") 会自动为 NFS 使用该项。

**注意：** 将第六项（`fs_passno`）设为非零值可能会导致预期外行为，例如当 systemd 自动挂载等待永不会发生的检查时挂起

###  搭配 /etc/fstab 和 systemd 进行挂载

另一种方法是使用 [x-systemd.automount](<../zh-cn/Fstab.html#%E8%BF%9C%E7%A8%8B%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "Fstab") 选项，它会在访问时挂载文件系统： 
    
    /etc/fstab
    
    servername:/home   _/mountpoint/on/client_  nfs  _netdev,noauto,x-systemd.automount,x-systemd.mount-timeout=10,timeo=14,x-systemd.idle-timeout=1min 0 0

为了让 systemd 意识到 fstab 的更改，需要[重新加载](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重新加载") systemd 并重启 `remote-fs.target` [[2]](<https://bbs.archlinux.org/viewtopic.php?pid=1515377#p1515377>)。 

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 不是所有人都用 NetworkManager。是否可以用[Systemd#在网络已连接后再启动某服务](<../zh-cn/Systemd.html#%E5%9C%A8%E7%BD%91%E7%BB%9C%E5%B7%B2%E8%BF%9E%E6%8E%A5%E5%90%8E%E5%86%8D%E5%90%AF%E5%8A%A8%E6%9F%90%E6%9C%8D%E5%8A%A1> "Systemd")替代？（在 [Talk:NFS](<../zh-cn/Talk:NFS.html>) 中讨论）

**提示：**

  * `noauto` 选项使得在访问 NFS 共享前不会进行挂载；使用 `auto` 会立刻进行挂载。  
如果遇到了网络未拉起/不可用导致的挂载失败，可以[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `NetworkManager-wait-online.service`。它会确保在激活前 `network.target` 已准备好所有链接可用。
  * `users` 选项允许普通用户进行挂载，但请注意，它同时启用了如 `noexec` 等隐藏挂载选项。
  * `x-systemd.idle-timeout=1min` 会在 1 分钟内未使用 NFS 共享的情况下自动将其卸载。该选项对于随时会断网的笔记本环境来说比较有用。
  * 如果由于 NFS 导致关机/重启时间过长，可以[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `NetworkManager-wait-online.service` 来确保 NetworkManager 在 NFS 卷卸载前不会关闭。
  * 不要添加 `x-systemd.requires=network-online.target` 挂载选项，该选项可能会导致 systemd 出现启动顺序循环 [[3]](<https://github.com/systemd/systemd-stable/issues/69>)。systemd 会根据 `_netdev` 选项自动将 `network-online.target` 添加为单元依赖。
  * `nocto` 选项可能会提高只读挂载的性能，但应只用在服务器上数据不经常出现变更的情况下。

###  作为 systemd 单元

在`/etc/systemd/system`目录下创建一个新`.mount` 文件,例如`mnt-home.mount`.有关详细信息，请参见[systemd.mount(5)](<https://man.archlinux.org/man/systemd.mount.5>). 

**注意：** 确保文件名与您要使用的挂载点相对应.例如,仅当要将共享挂载到 `/mnt/home` 时才能使用单元名称 `mnt-home.mount`，否则可能会发生以下错误：`systemd[1]: mnt-myshare.mount: Where= setting does not match unit name. Refusing.`。如果挂载点包含非 ASCII 字符，请使用 [systemd-escape](<../zh-cn/Systemd.html#%E7%BC%96%E5%86%99%E5%8D%95%E5%85%83%E6%96%87%E4%BB%B6> "Systemd")。

`What=` 分享的路径 

`Where=` 分享应当被挂载的路径 

`Options=` 挂载分享的选项 

{{注意| 

  * 网络安装单元会自动获取对 `remote-fs-pre.target`，`network.target` 和 `network-online.target` 的 `After` 依赖，并获得对 `remote-fs.target` 的`Before` 依赖，除非设置了 `nofail` 挂载选项。在后一种情况下,还会添加一个 `Wants` 单元。
  * [添加](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "添加") `noauto` 到 `Options` 可以防止启动时自动挂载（除非被其它单元触发）。
  * 如果你要为共享服务器使用域名而不是 IP 地址，则需要添加 `nss-lookup.target` 到 `After` 下。这可能会避免测试中没有问题，但启动时挂载出错的情况出现。

    /etc/systemd/system/mnt-home.mount
    
    [Unit]
    Description=Mount home at boot
    
    [Mount]
    What=172.16.24.192:/home
    Where=/mnt/home
    Options=vers=4
    Type=nfs
    TimeoutSec=30
    
    [Install]
    WantedBy=multi-user.target

**提示：** 为处理网络出现中断的情况，可[添加](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "添加") `ForceUnmount=true` 到 `[Mount]`，该选项使挂载可以被强制卸载。

要使用 `mnt-home.mount`，[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")该单元，然后将其[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")以在系统启动时进行挂载。 

####  自动挂载

要想自动挂载一个分享,你可以使用下面的自动挂载单元: 
    
    /etc/systemd/system/mnt-home.automount
    
    [Unit]
    Description=Automount home
    
    [Automount]
    Where=/mnt/home
    
    [Install]
    WantedBy=multi-user.target

[禁用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "禁用")/[停止](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "停止") `mnt-home.mount` 单元，然后[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")/[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `mnt-home.automount` 以在路径可用时自动挂载共享。 

**提示：**[添加](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "添加") `TimeoutIdleSec` 以启用自动卸载，详细信息可参考 [systemd.automount(5)](<https://man.archlinux.org/man/systemd.automount.5>)。

###  使用 autofs 挂载

Using [autofs](<../zh-cn/Autofs.html> "Autofs") is useful when multiple machines want to connect via NFS; they could both be clients as well as servers. The reason this method is preferable over the earlier one is that if the server is switched off, the client will not throw errors about being unable to find NFS shares. See [autofs#NFS network mounts](<../zh-cn/Autofs.html#NFS_network_mounts> "Autofs") for details. 

##  提示和技巧

###  启用 NFSv4 ID 映射

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** The instructions are too convoluted. Separate sections for client and server configuration would be better than notes like "Enabling/starting nfs-idmapd.service should not be needed on the client" or "Do not confuse the nfsidmap (only for nfs clients) with nfs-idmapd.service".（在[Talk:NFS](<../zh-cn/Talk:NFS.html>)讨论）

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** Missing lookup information, static binding examples, etc. (在 [Talk:NFS](<../zh-cn/Talk:NFS.html>) 中讨论)

**注意：**

  * NFSv4 ID 映射无法解决默认 `sec=sys` 挂载选项导致的所有问题。更多信息请参考 [NFS#静态映射](<#%E9%9D%99%E6%80%81%E6%98%A0%E5%B0%84>) 和 [[4]](<https://web.archive.org/web/20220602190451/https://dfusion.com.au/wiki/tiki-index.php?page=Why+NFSv4+UID+mapping+breaks+with+AUTH_UNIX>)
  * 在客户端和服务端上**均** 需要启用 NFSv4 ID 映射
  * 另一个选择是确保用户 ID 和组 ID（UID 和 GID）在客户端和服务器上一致。
  * _不_ 需要[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")/[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `nfs-idmapd.service`，因为它已被新的 ID 映射器替换：

    # dmesg | grep id_resolver
    
    [ 3238.356001] NFS: Registering the id_resolver key type
    [ 3238.356009] Key type id_resolver registered
    
**提示：**

  * Do not confuse the `nfsidmap` (only for nfs **clients**) with `nfs-idmapd.service` which is used by the NFS **server** and forks the process `rpc.idmapd`.
  * Both rpc.idmapd and nfsidmap share also some configurations from [idmapd.conf(5)](<https://man.archlinux.org/man/idmapd.conf.5>).
  * 更多信息请参考 [idmapd(8)](<https://man.archlinux.org/man/idmapd.8>) 和 [nfsidmap(8)](<https://man.archlinux.org/man/nfsidmap.8>)。

NFSv4 协议将客户端的 UID 和 GID 值表示为 `_user_ @_domain_` 形式的字符串.将UID和字符串互相转换的过程称为 _ID 映射_ 。 

####  域名

**注意：**

  * By default, the domain part of the string is the system's DNS domain name. It can also be specified in /etc/idmapd.conf if the system is multi-homed, or if the system's DNS domain name does not match the name of the system's Kerberos realm.
  * When the domain is not specified in /etc/idmapd.conf the local DNS server will be queried for the _nfsv4idmapdomain text record. If the record exists that will be used as the domain. When the record does not exist, the domain part of the DNS domain will used.

Display the system's effective NFSv4 domain name on stdout. 
    
    # nfsidmap -d
    
    domain.tld

Edit to match up the Domain on the server and/or client: 
    
    /etc/idmapd.conf
    
    [General]
    Domain = _guestdomain.tld_

####  静态映射

**提示：**

  * 这个映射仅用于客户端本地映射 uid。如果您创建一个属于某个在服务器上不被识别的 uid（例如 1005）的文件。该文件会以 uid 1005 的形式存储在服务器上，但在传输过程中不会再显示正确的 uid。
  * 在与服务器交互（例如列出文件）之后，您可以查看密钥环中的所有条目。

    # nfsidmap -l
    
    7 .id_resolver keys found:
     uid:nobody
     user:1
     uid:bin@domain.tld
     uid:foo@domain.tld
     gid:foo@domain.tld
     uid:remote_user@domain.tld
     uid:root@domain.tld
    
  * 您可以使用命令 `nfsidmap -c` 清除密钥环，但在默认设置中，条目会在 10 分钟后过期，因此并不需要手动清除。

这些步骤只在服务器和客户端具有不同的用户/组名称时才需要进行。 

更改只会在客户端的配置文件中进行。 
    
    /etc/idmapd.conf
    
    [Translation]
    # The default is nsswitch and other methods exist.
    method = static,nsswitch
    
    [Static]
    foo@domain.tld = local_foo
    remote_user@domain.tld = user

####  后备映射

Only in the client configuration. Local user/group name to be used when a mapping cannot be completed: 
    
    /etc/idmapd.conf
    
    [Mapping]
    Nobody-User = nobody
    Nobody-Group = nobody

###  性能调优

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** Mentions 32-bit and 2.6 Linux kernel... (在[Talk:NFS](<../zh-cn/Talk:NFS.html>)讨论)

When using NFS on a network with a significant number of clients one may increase the default NFS threads from _8_ to _16_ or even a higher, depending on the server/network requirements: 
    
    /etc/nfs.conf
    
    [nfsd]
    threads=16

It may be necessary to tune the `rsize` and `wsize` mount options to meet the requirements of the network configuration. 

In recent linux kernels (>2.6.18) the size of I/O operations allowed by the NFS server (default max block size) varies depending on RAM size, with a maximum of 1M (1048576 bytes), the max block size of the server will be used even if nfs clients requires bigger `rsize` and `wsize`. See <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/5/html/5.8_technical_notes/known_issues-kernel> It is possible to change the default max block size allowed by the server by writing to the `/proc/fs/nfsd/max_block_size` before starting _nfsd_. For example, the following command restores the previous default iosize of 32k: 
    
    # echo 32768 > /proc/fs/nfsd/max_block_size
    
**注意：** This is mainly useful for 32-bit servers when dealing with the large numbers of nfsd threads. Lowering the `max_block_size` may decrease NFS performance on modern hardware.

To make the change permanent, create a [systemd-tmpfile](</wzh/index.php?title=Systemd-tmpfile&action=edit&redlink=1> "Systemd-tmpfile（页面不存在）"): 
    
    /etc/tmpfiles.d/nfsd-block-size.conf
    
    w /proc/fs/nfsd/max_block_size - - - - 32768
    
To mount with the increased `rsize` and `wsize` mount options: 
    
    # mount -t nfs -o rsize=32768,wsize=32768,vers=4 servername:/srv/nfs/music /mountpoint/on/client
    
Furthermore, despite the violation of NFS protocol, setting `async` instead of `sync` or `sync,no_wdelay` may potentially achieve a significant performance gain especially on spinning disks. Configure exports with this option and then execute `exportfs -arv` to apply. 
    
    /etc/exports
    
    /srv/nfs        192.168.1.0/24(rw,async,crossmnt,fsid=0)
    /srv/nfs/music  192.168.1.0/24(rw,async)

**警告：** Using `async` comes with a risk of possible data loss or corruption if the server crashes or restarts uncleanly.

###  处理自动挂载

This trick is useful for NFS-shares on a [wireless](</wzh/index.php?title=Wireless&action=edit&redlink=1> "Wireless（页面不存在）") network and/or on a network that may be unreliable. If the NFS host becomes unreachable, the NFS share will be unmounted to hopefully prevent system hangs when using the `hard` mount option [[5]](<https://bbs.archlinux.org/viewtopic.php?pid=1260240#p1260240>). 

Make sure that the NFS mount points are correctly indicated in [fstab](<../zh-cn/Fstab.html> "Fstab"): 
    
    /etc/fstab
    
    lithium:/mnt/data           /mnt/data	        nfs noauto 0 0
    lithium:/var/cache/pacman   /var/cache/pacman	nfs noauto 0 0

**注意：**

  * Use hostnames in [fstab](<../zh-cn/Fstab.html> "Fstab") for this to work, not IP addresses.
  * In order to mount NFS shares with non-root users the `users` option has to be added.
  * The `noauto` mount option tells [systemd](<../zh-cn/Systemd.html> "Systemd") to not automatically [mount](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html#%E6%8C%82%E8%BD%BD%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "Mount") the shares at boot, otherwise this may cause the boot process to stall.

Create the `auto_share` script that will be used by [cron](<../zh-cn/Cron.html> "Cron") or [systemd/Timers](<../zh-cn/Systemd/%E5%AE%9A%E6%97%B6%E5%99%A8.html> "Systemd/Timers") to use ICMP ping to check if the NFS host is reachable: 

**警告：**

  * 如果你在使用 [btrfs](<../zh-cn/Btrfs.html> "Btrfs")，请将 `sed -e '/^.*#/d' -e '/^.*:/!d' -e 's/\t/ /g' /etc/fstab` 替换为如 `sed -n -e '/^[a-zA-Z0-9.-]*\(\.[a-zA-Z]\+\)\{0,1\}:/p' /etc/fstab`，并测试其输出是否仅包含网络共享，以防如压缩选项等参数导致本地分区被包含进 _NET_MOUNTS_ 变量中。[[6]](<https://wiki.archlinux.org/title/Talk:NFS#the_auto_share_script_can_unmount_your_main_partitions>)

    /usr/local/bin/auto_share
    
    #!/bin/bash
    
    function net_umount {
      umount -l -f $1 &>/dev/null
    }
    
    function net_mount {
      mountpoint -q $1 || mount $1
    }
    
    NET_MOUNTS=$(sed -e '/^.*#/d' -e '/^.*:/!d' -e 's/\t/ /g' /etc/fstab | tr -s " ")$'\n'b
    
    printf %s "$NET_MOUNTS" | while IFS= read -r line
    do
      SERVER=$(echo $line | cut -f1 -d":")
      MOUNT_POINT=$(echo $line | cut -f2 -d" ")
    
      # Check if server already tested
      if [[ "${server_ok[@]}" =~ "${SERVER}" ]]; then
        # The server is up, make sure the share are mounted
        net_mount $MOUNT_POINT
      elif [[ "${server_notok[@]}" =~ "${SERVER}" ]]; then
        # The server could not be reached, unmount the share
        net_umount $MOUNT_POINT
      else
        # Check if the server is reachable
        ping -c 1 "${SERVER}" &>/dev/null
    
        if [ $? -ne 0 ]; then
          server_notok[${#server_notok[@]}]=$SERVER
          # The server could not be reached, unmount the share
          net_umount $MOUNT_POINT
        else
          server_ok[${#server_ok[@]}]=$SERVER
          # The server is up, make sure the share are mounted
          net_mount $MOUNT_POINT
        fi
      fi
    done
    
**注意：** Test using a TCP probe instead of ICMP ping (default is tcp port 2049 in NFS4) then replace the line: 
    
    # Check if the server is reachable
    ping -c 1 "${SERVER}" &>/dev/null
    
with: 
    
    # Check if the server is reachable
    timeout 1 bash -c ": < /dev/tcp/${SERVER}/2049"
    
in the `auto_share` script above.

Make sure the script is [executable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "Executable"). 

Next check configure the script to run every X, in the examples below this is every minute. 

#### Cron
    
    # crontab -e
    
    * * * * * /usr/local/bin/auto_share
    
####  systemd/Timers
    
    /etc/systemd/system/auto_share.timer
    
    [Unit]
    Description=Automount NFS shares every minute
    
    [Timer]
    OnCalendar=*-*-* *:*:00
    
    [Install]
    WantedBy=timers.target
    
    /etc/systemd/system/auto_share.service
    
    [Unit]
    Description=Automount NFS shares
    After=network.target
    
    [Service]
    Type=oneshot
    ExecStart=/usr/local/bin/auto_share
    
    [Install]
    WantedBy=multi-user.target

Finally, [enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") and [start](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") `auto_share.timer`. 

#### Using a NetworkManager dispatcher

[NetworkManager](<../zh-cn/NetworkManager.html#Network_services_with_NetworkManager_dispatcher> "NetworkManager") can also be configured to run a script on network status change. 

The easiest method for mount shares on network status change is to symlink the `auto_share` script: 
    
    # ln -s /usr/local/bin/auto_share /etc/NetworkManager/dispatcher.d/30-nfs.sh
    
However, in that particular case unmounting will happen only after the network connection has already been disabled, which is unclean and may result in effects like freezing of KDE Plasma applets. 

The following script safely unmounts the NFS shares before the relevant network connection is disabled by listening for the `down`, `pre-down` and `vpn-pre-down` events, make sure the script is [executable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "Executable"): 
    
    /etc/NetworkManager/dispatcher.d/30-nfs.sh
    
    #!/bin/sh
    
    # Find the connection UUID with "nmcli con show" in terminal.
    # All NetworkManager connection types are supported: wireless, VPN, wired...
    WANTED_CON_UUID="CHANGE-ME-NOW-9c7eff15-010a-4b1c-a786-9b4efa218ba9"
    
    if [ "$CONNECTION_UUID" = "$WANTED_CON_UUID" ]; then
        
        # Script parameter $1: network interface name, not used
        # Script parameter $2: dispatched event
        
        case "$2" in
            "up")
                mount -a -t nfs4,nfs 
                ;;
            "down"|"pre-down"|"vpn-pre-down")
                umount -l -a -t nfs4,nfs -f >/dev/null
                ;;
        esac
    fi
    
**注意：** This script ignores mounts with the `noauto` option, remove this mount option or use `auto` to allow the dispatcher to manage these mounts.

在`/etc/NetworkManager/dispatcher.d/pre-down`中创建一个符号链接以捕获`pre-down`事件: 
    
    # ln -s /etc/NetworkManager/dispatcher.d/30-nfs.sh /etc/NetworkManager/dispatcher.d/pre-down.d/30-nfs.sh
    
###  TLS 加密

NFS traffic can be encrypted using TLS as of Linux 6.5 using the `xprtsec=tls` mount option. To begin, install the [ktls-utils](<https://aur.archlinux.org/packages/ktls-utils/>)AUR package on the client and server, and follow the below configuration steps for each. 

####  服务端

Create a private key and obtain a certificate containing your server's DNS name (see [Transport Layer Security](</wzh/index.php?title=Transport_Layer_Security&action=edit&redlink=1> "Transport Layer Security（页面不存在）") for more detail). These files do not need to be added to the system's trust store. 

**注意：** Using a self-signed certificate that has also been encrypted is currently not supported and will result in a mount failure.

Edit `/etc/tlshd.conf` to use these files, using your own values for `x509.certificate` and `x509.private_key`
    
    /etc/tlshd.conf
    
    [authenticate.server]
    x509.certificate= /etc/nfsd-certificate.pem
    x509.private_key= /etc/nfsd-private-key.pem

Now [start](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") and [enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") `tlshd.service`. 

####  客户端

Add the server's TLS certificate generated in the previous step to the system's trust store (see [Transport Layer Security](</wzh/index.php?title=Transport_Layer_Security&action=edit&redlink=1> "Transport Layer Security（页面不存在）") for more detail). 

[Start](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start") and [enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") `tlshd.service`. 

Now you should be able to mount the server using the server's DNS name: 
    
    # mount -o xprtsec=tls _servername.domain_ :/ _/mountpoint/on/client_
    
Checking journalctl on the client should show that the TLS handshake was successful: 
    
    $ journalctl -b -u tlshd.service
    
    Sep 28 11:14:46 client tlshd[227]: Built from ktls-utils 0.10 on Sep 26 2023 14:24:03
    Sep 28 11:15:37 client tlshd[571]: Handshake with servername.domain (192.168.122.100) was successful
    
##  故障排查

参考单独的 [NFS/Troubleshooting](</wzh/index.php?title=NFS/Troubleshooting&action=edit&redlink=1> "NFS/Troubleshooting（页面不存在）") 页面。 

##  更多参考

  * See also [Avahi](</wzh/index.php?title=Avahi&action=edit&redlink=1> "Avahi（页面不存在）"), a Zeroconf implementation which allows automatic discovery of NFS shares.
  * HOWTO: [Diskless network boot NFS root](</wzh/index.php?title=Diskless_network_boot_NFS_root&action=edit&redlink=1> "Diskless network boot NFS root（页面不存在）")
  * [Microsoft Services for Unix NFS Client info](<https://web.archive.org/web/20201111215940/https://docs.microsoft.com/en-us/archive/blogs/msdn/sfu/all-well-almost-about-client-for-nfs-configuration-and-performance/>)
  * [NFS on Snow Leopard](<https://web.archive.org/web/20151212160906/https://blogs.oracle.com/jag/entry/nfs_on_snow_leopard>)
  * <http://chschneider.eu/linux/server/nfs.shtml>
  * [How to do Linux NFS Performance Tuning and Optimization](<https://www.slashroot.in/how-do-linux-nfs-performance-tuning-and-optimization>)
  * [Linux: Tune NFS Performance](<https://www.cyberciti.biz/faq/linux-unix-tuning-nfs-server-client-performance/>)
  * [Configuring an NFSv4-only Server](<https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/storage_administration_guide/nfs-serverconfig#nfs4-only>)
