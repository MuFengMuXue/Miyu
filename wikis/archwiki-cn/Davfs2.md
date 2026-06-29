相关文章

  * [WebDAV](<../zh-cn/WebDAV.html> "WebDAV")

**翻译状态：**

  * 本文（或部分内容）译自 [Davfs2](<https://wiki.archlinux.org/title/Davfs2> "arch:Davfs2")，最近一次同步于 2026-03-09，若英文版本有所[更改](<https://wiki.archlinux.org/title/Davfs2?diff=0&oldid=868468>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Davfs2_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[davfs2](<https://savannah.nongnu.org/projects/davfs2>) 是一个用于[挂载](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html#%E6%8C%82%E8%BD%BD%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "挂载") [WebDAV](<../zh-cn/WebDAV.html> "WebDAV") 资源的 Linux 文件系统。WebDAV 是 HTTP/1.1 的一个扩展，用于远程协作共享网络文件资源。 

##  安装 davfs2

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")软件包 [davfs2](<https://archlinux.org/packages/?name=davfs2>)包。 

##  挂载 WebDAV 资源

###  配置和挂载参数

**配置文件** 分为系统级的 `/etc/davfs2/davfs2.conf` 和用户级的 `~/.davfs2/davfs2.conf`。普通用户调用时，会同时读取两个配置文件，但用户配置的优先级高于系统配置。可以对常规、WebDAV 相关、缓存相关、调试等内容进行配置，具体语法请参见 [davfs2.conf(5)](<https://man.archlinux.org/man/davfs2.conf.5>)。 

**挂载参数** 可以用于定义配置文件路径、文件系统的所有者和用户组，以及其他访问权限相关的选项。要查询所有可用的参数，执行以下命令： 
    
    $ mount.davfs -h
    
也可参见 [mount.davfs(8)](<https://man.archlinux.org/man/mount.davfs.8>) 了解详细。 

###  使用命令行

要挂载 WebDAV 资源，请使用 `mount`，而非直接使用 `mount.davfs`。 
    
    # mount -t davfs http(s)://address:<port>/path /mount/point
    
**注意：** 只有在系统级配置文件中定义的 `dav_group` 用户组内的普通成员才能挂载 davfs2 文件系统。确保系统级配置文件中的 `dav_group` 已经被启用并被指定了可用的用户组。

###  使用 systemd

要使用[Systemd 挂载](<../zh-cn/Systemd.html#systemd.mount_-_%E6%8C%82%E8%BD%BD> "Systemd")： 
    
    /etc/systemd/system/mnt-webdav-service.mount
    
    [Unit]
    Description=Mount WebDAV Service
    After=network-online.target
    Wants=network-online.target
    
    [Mount]
    What=http(s)://address:<port>/path
    Where=/mnt/webdav/service
    Options=uid=1000,file_mode=0664,dir_mode=2775,grpid
    Type=davfs
    TimeoutSec=15
    
    [Install]
    WantedBy=multi-user.target
    
也可以创建一个 systemd 自动挂载单元来设置超时时间。 
    
    /etc/systemd/system/mnt-webdav-service.automount
    
    [Unit]
    Description=Mount WebDAV Service
    
    [Automount]
    Where=/mnt/webdav/service
    TimeoutIdleSec=300
    
    [Install]
    WantedBy=remote-fs.target
    
要了解更多关于 systemd 挂载单元的内容，参见 [Fstab#通过_systemd_自动挂载](<../zh-cn/Fstab.html#%E9%80%9A%E8%BF%87_systemd_%E8%87%AA%E5%8A%A8%E6%8C%82%E8%BD%BD> "Fstab")。 

###  使用 fstab

要定义如何将 WebDAV 资源挂载在文件系统上，请[添加](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "添加")一个以下格式的 [fstab](<../zh-cn/Fstab.html> "Fstab") 条目： 
    
    /etc/fstab
    
    https://_webdav.example/path_ /mnt/_webdav_ davfs rw,user,uid=_username_ ,noauto 0 0

其中， _username_ 是所挂载的文件系统的所有者，可以是数字 ID 或是用户名。仅有 _root_ 用户能以与挂载用户不同的 UID 进行挂载。挂载参数 `_netdev` 可以用于自动挂载网络驱动器。 

##  提示与技巧

###  保存认证信息

创建一个密钥文件以保存 WebDAV 服务的认证信息。对于普通用户，使用 `~/.davfs2/secrets`；对于 _root_ 用户，使用 `/etc/davfs2/secrets`： 
    
    /etc/davfs2/secrets
    
    https://_webdav.example/path_ _davusername_ _davpassword_

请确保密钥文件的[权限](<../zh-cn/%E6%96%87%E4%BB%B6%E6%9D%83%E9%99%90%E4%B8%8E%E5%B1%9E%E6%80%A7.html> "权限")正确。对于 _root_ 用户： 
    
    # chmod 600 /etc/davfs2/secrets
    # chown root:root /etc/davfs2/secrets
    
对于普通用户： 
    
    $ chmod 600 ~/.davfs2/secrets
    
##  常见问题

###  无法创建/复制文件，同时可能卡住

如果无法创建/复制文件，同时可能卡住，请编辑[#配置和挂载参数](<#%E9%85%8D%E7%BD%AE%E5%92%8C%E6%8C%82%E8%BD%BD%E5%8F%82%E6%95%B0>)，将 `use_locks 0` 加入到配置中。默认配置 `1` 会在打开和写入文件时在服务器上加锁。 

###  密码和密钥文件

如果密码中含有如 `\` 或 `"` 这样的特殊字符，请为其添加转义符 `\`。 

###  网络已连通但域名解析失败

有时 `network-online.target` 已经成功但 WebDAV 服务器的域名仍未被解析。可以手动等待域名解析成功。 

首先，配置好[#使用 fstab](<#%E4%BD%BF%E7%94%A8_fstab>)，然后在 15 秒重复使用 ping 测试是否能访问服务器。访问成功时，再进行挂载： 
    
    /etc/systemd/system/mnt-webdav-service.service
    
    [Unit]
    Description=Mount WebDAV Service
    After=network-online.target
    Wants=network-online.target
    
    [Service]
    Type=oneshot
    ExecStart=bash -c 'for i in {1..15}; do if ping -c 1 _mywebdav.server.url_ ; then mount _/path/to/mountpoint_ ; break; else sleep 1; fi; done'
    ExecStop=umount _/path/to/mountpoint_
    RemainAfterExit=true
    
    [Install]
    WantedBy=default.target

建议将其配置为[用户单元](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "用户单元")。 

###  挂载 WebDAV 资源时报错 'different mount options in /etc/fstab'

可能是以下原因导致： 

  1. WebDAV 资源及其挂载点已经在 /etc/fstab 中定义
  2. 挂载点已经被作为一个参数传递给 'mount' 命令（即使挂载点与 /etc/fstab 中相同）

因此，请不要在挂载时传递挂载点，而是自动使用 /etc/fstab 中的值。例如： 
    
    $ mount -t davfs <https://mywebdav> mymountpoint # 错误
    与 /etc/fstab 中的挂载参数不同
    $ mount -t davfs <https://mywebdav> # 正确
    
##  参见

  * <https://ajclarkson.co.uk/blog/auto-mount-webdav-raspberry-pi/>[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2025-03-15 ⓘ]
