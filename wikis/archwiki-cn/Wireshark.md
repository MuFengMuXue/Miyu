**翻译状态：**

  * 本文（或部分内容）译自 [Wireshark](<https://wiki.archlinux.org/title/Wireshark> "arch:Wireshark")，最近一次同步于 2022-07-03，若英文版本有所[更改](<https://wiki.archlinux.org/title/Wireshark?diff=0&oldid=735848>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Wireshark_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Wireshark](<https://www.wireshark.org/>) 是一款自由且开源的包分析器。可用于网络排错、网络分析、软件和通讯协议开发以及教学等。 

##  安装

Wireshark 软件包分成了 CLI 版本和依赖 CLI 版本的前端界面. 

  * CLI 版本 - [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")软件包 [wireshark-cli](<https://archlinux.org/packages/?name=wireshark-cli>)包。
  * TUI 前端 - [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")软件包 [termshark](<https://archlinux.org/packages/?name=termshark>)包。
  * Qt 前端 - [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")软件包 [wireshark-qt](<https://archlinux.org/packages/?name=wireshark-qt>)包。

**注意：** Wireshark 3.0 已经移除了 GTK 界面

##  以普通用户身份抓包

以 root 身份运行 Wireshark 是不安全的。Arch Linux 官方仓库中的 Wireshark 已经实现了权限分离，其使用的抓包工具 `/usr/bin/dumpcap` 是唯一有权限进行数据包抓取的进程，仅能被 root 或 `wireshark` 群组用户执行[[1]](<https://gitlab.com/wireshark/wireshark/-/wikis/CaptureSetup/CapturePrivileges#most-unixes>)。 

[wireshark-cli](<https://archlinux.org/packages/?name=wireshark-cli>)包 的[安装脚本](<../zh-cn/PKGBUILD.html#install> "PKGBUILD")还会为 `/usr/bin/dumpcap` 设置数据包捕获[能力（capability）](<../zh-cn/Capabilities.html> "Capabilities")，使其无需 root 权限也能进行数据包捕获。 

如果希望普通用户能够正常运行 Wireshark，必须将其添加到 `wireshark` [用户组](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html> "用户和用户组")中（参见[用户和用户组#用户组管理](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E7%94%A8%E6%88%B7%E7%BB%84%E7%AE%A1%E7%90%86> "用户和用户组")）。 

使用如下命令可以将对应用户添加到 `wireshark` 用户组（中文 wiki 注）： 
    
    # usermod -a -G wireshark _用户名_
    
重启或注销对应用户重新登陆即可生效。 

##  一些抓包技巧

你可以通过使用 [capture filters](<https://gitlab.com/wireshark/wireshark/-/wikis/CaptureFilters>) 和 [display filters](<https://gitlab.com/wireshark/wireshark/-/wikis/DisplayFilters>) 准确获取你想抓取的数据包。 

**注意：** capture filters 语法请参考 [pcap-filter(7)](<https://man.archlinux.org/man/pcap-filter.7>) ，display filters 语法参考 [wireshark-filter(4)](<https://man.archlinux.org/man/wireshark-filter.4>)。

###  过滤 TCP 包

只查看所有的 TCP 数据包，在 _Filter_ 栏输入 `tcp`，或者在终端中输入： 
    
    $ tshark -f "tcp"
    
###  过滤 UDP 包

只想查看所有的 UDP 数据包，在 _Filter_ 栏输入 `udp`，或者在终端输入： 
    
    $ tshark -f "udp"
    
###  查看指定 IP 地址的数据包

将 `1.2.3.4` 替换为要查看的 IP 地址。 

  * 只想查看发到某个特定地址的数据包，输入 `ip.dst == 1.2.3.4`。

  * 只想查看从某个特定地址发出的数据包，输入 `ip.src == 1.2.3.4`。

  * 要查看某个特定地址的所有数据包，输入 `ip.addr == 1.2.3.4`。

###  排除特定 IP 地址的数据包

将 `1.2.3.4` 替换为要排除的 IP 地址。 
    
    ip.addr != 1.2.3.4
    
###  查看局域网数据包

如果只想查看局域网数据包，使用 
    
     (ip.src==10.0.0/8 AND ip.dst==10.0.0/8) OR (ip.src==172.16.0.0/12 AND ip.dst==172.16.0.0/12) OR (ip.src==192.168.0.0/16 and ip.dst==192.168.0.0/16)
    
这样可以过滤出所有来自私有网络地址的数据包。 

###  查看指定端口的数据包

查看某两个或更多端口的流量： 
    
    tcp.port==80||tcp.port==3306
    tcp.port==80||tcp.port==3306||tcp.port==443
    
###  使用 dumpcap 捕获数据包

_dumpcap_ 是 Wireshark 的一部分，可以使用该工具在无图形界面的情况下捕获数据包。 _dumpcap_ 可以在 [tmux](<../zh-cn/Tmux.html> "Tmux") 或 [GNU Screen](<../zh-cn/GNU_Screen.html> "GNU Screen") 中使用，以在一个处于 Detached 状态的会话中捕获数据包。 

可以使用 `-h` 参数查看 dumpcap 的所有选项。 

下面的例子展示了如何捕获循环缓冲区（ringbuffer）中内容。下面的命令会以每个文件 100MB 的大小捕获20个`.pcap`文件，并且会在捕获第21个文件时替换最早创建的文件并依次继续。因此此命令会保持运行，而不会持续消耗磁盘空间以致磁盘容量耗尽。 
    
    # dumpcap -i 1 -b filesize:100000 -b files:20 -w _mycapture_.pcapng
    
  * `-i` \- 接口名称或编号（`dumpcat -D` 命令列出的编号）
  * `-b filesize:` \- 创建的`.pcap`文件的大小，以 kB 为单位
  * `-b files:` \- 在输出指定的文件数量后覆盖旧文件
  * `-w` \- 输出文件名，上例中输出会保存到 `mycapture _identifier_.pcapng`
