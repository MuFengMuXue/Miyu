相关文章

  * [Linux 容器](<../zh-cn/Linux_%E5%AE%B9%E5%99%A8.html> "Linux 容器")
  * [LXD](</wzh/index.php?title=LXD&action=edit&redlink=1> "LXD（页面不存在）")

**翻译状态：**

  * 本文（或部分内容）译自 [Incus](<https://wiki.archlinux.org/title/Incus> "arch:Incus")，最近一次同步于 2026-02-26，若英文版本有所[更改](<https://wiki.archlinux.org/title/Incus?diff=0&oldid=860456>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Incus_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[Incus](<https://linuxcontainers.org/incus/introduction/>) 是一个用于管理容器（通过 [LXC](<../zh-cn/Linux_%E5%AE%B9%E5%99%A8.html> "LXC")）和虚拟机（通过 [QEMU](<../zh-cn/QEMU.html> "QEMU")）的管理程序。 

它是由原维护者从 [LXD](<https://ubuntu.com/lxd>) 分叉而来的。[LXD](</wzh/index.php?title=LXD&action=edit&redlink=1> "LXD（页面不存在）") 维基页面中的文档在很大程度上仍然相关，值得阅读。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [incus](<https://archlinux.org/packages/?name=incus>)包 软件包，然后[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `incus.socket`。 

或者，如果您希望实例自动启动, 您可以直接[启用/启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用/启动") `incus.service`。 

要将容器创建委托给用户，请[启用/启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用/启动") `incus-user.socket` 单元。有关组委派，请参阅 [#以非特权用户身份访问 Incus](<#%E4%BB%A5%E9%9D%9E%E7%89%B9%E6%9D%83%E7%94%A8%E6%88%B7%E8%BA%AB%E4%BB%BD%E8%AE%BF%E9%97%AE_Incus>)。 

###  从 LXD 迁移

如果您希望从现有的 LXD 安装迁移，应在此时进行，因为迁移工具只会针对空的目标 Incus 服务器运行。 

在验证 `lxc info` 和 `incus info` 命令都能正确运行后，阅读上游关于该过程的 [文档](<https://linuxcontainers.org/incus/docs/main/howto/server_migrate_lxd/>)，然后运行迁移工具： 
    
    # lxd-to-incus
    
##  配置

###  非特权容器

Incus 默认启动 [非特权容器](<https://linuxcontainers.org/incus/docs/main/explanation/security/#container-security>)（关于区别的解释，请参阅 [Linux 容器#特权或非特权](<../zh-cn/Linux_%E5%AE%B9%E5%99%A8.html#%E7%89%B9%E6%9D%83%E6%88%96%E9%9D%9E%E7%89%B9%E6%9D%83> "Linux 容器")）。 

为此，您需要为 root 用户设置适当的子用户ID和子组ID范围[[1]](<https://linuxcontainers.org/incus/docs/main/installing/#machine-setup>)：与[podman](<../zh-cn/Podman.html> "Podman") 不同，Incus 使用需要以 root 身份运行的守护进程。[[2]](<https://discuss.linuxcontainers.org/t/incus-no-uid-gid-allocation-configured/19002/13>)

验证 `/etc/subuid` 和 `/etc/subgid` 的内容，如果需要，为 root 用户添加一个 [至少 1000 万个 UID/GID 的连续范围](<https://linuxcontainers.org/incus/docs/main/installing/#machine-setup>)： 
    
    # usermod -v 1000000-1000999999 -w 1000000-1000999999 root
    
然后[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `incus`。 

关于替代方法，请参阅 [LXD#特权容器](</wzh/index.php?title=LXD&action=edit&redlink=1> "LXD（页面不存在）")。 

###  以非特权用户身份访问 Incus

来自 [官方文档](<https://linuxcontainers.org/incus/docs/main/tutorial/first_steps/#install-and-initialize-incus>)： 

"对 Incus 的访问由两个组控制： 

• `incus` 允许基本的用户访问，没有配置权限，所有操作限制在每个用户的项目内。 

• `incus-admin` 允许完全控制 Incus。" 

要使普通用户能够启动和操作实例，请将用户添加到 `incus` 组。 

要给普通用户完全控制 Incus 的权限而无需使用 [sudo](<../zh-cn/Sudo.html> "Sudo")，请将用户添加到 `incus-admin`。 

**警告：** 添加到 `incus-admin` 组的任何人都是 root 等效用户。更多信息，请参阅 [[3]](<https://github.com/lxc/incus#security>) 和 [[4]](<https://bugs.launchpad.net/ubuntu/+source/lxd/+bug/1829071>)。

###  初始化 Incus 配置

在使用之前，Incus 的配置需要进行初始化： 
    
    # incus admin init
    
**注意：** 如果没有 root 权限或属于 `incus-admin` 组的用户，此命令无法成功运行。 来自 [官方文档](<https://linuxcontainers.org/incus/docs/main/howto/initialize/#interactive-configuration>)：

这将在终端启动一个交互式配置向导，涵盖存储、网络等不同主题。您可以在官方 [入门指南](<https://linuxcontainers.org/incus/docs/main/tutorial/first_steps/>) 中找到概述。 

###  添加 Web 界面

用于浏览器的前端 [lxd-ui](<https://github.com/canonical/lxd-ui>) 已打补丁以适配 Incus。这些补丁可在 debian 软件包源代码中找到。[[5]](<https://github.com/zabbly/incus/tree/daily/patches>)

要使用此 UI，请安装 [incus-ui](<https://archlinux.org/packages/?name=incus-ui>)包 软件包。 

然后设置 Web 服务器的地址和端口： 
    
    $ incus config set core.https_address=127.0.0.1:8443
    
并[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") Incus。 

另一个可用的选项是使用以下命令运行 Web 服务器： 
    
    $ incus webui
    
关于此选项，请参阅 [incus webui](<https://linuxcontainers.org/incus/docs/main/reference/manpages/incus/webui/>)

##  使用

###  命令概述

您可以通过输入以下命令获取所有可用命令的概述： 
    
    $ incus
    
###  创建容器

容器基于从镜像服务器或远程 LXD 服务器下载的镜像。 

您可以使用以下命令查看已添加服务器的列表： 
    
    $ incus remote list
    
**注意：** 可以通过使用 `NAME` 列左侧显示的名称来引用镜像服务器，例如以下示例中的 `images`。

您可以使用 `incus image list _server-name_ :` 列出服务器上的所有镜像，例如： 

**提示：** 由于可用镜像数量众多，建议将以下命令的输出通过 [less](<https://archlinux.org/packages/?name=less>)包 等分页器管道传输。
    
    $ incus image list images:
    
这将向您显示默认服务器之一上的所有镜像：[images.linuxcontainers.org](<https://images.linuxcontainers.org>)

您还可以通过添加诸如发行版名称之类的术语来搜索镜像： 
    
    $ incus image list images:debian
    
使用特定服务器的镜像启动容器： 
    
    $ incus launch _servername_ :_imagename_
    
例如，从默认服务器的 Ubuntu Noble 镜像创建一个随机命名的容器实例： 
    
    $ incus launch images:ubuntu/noble
    
要为实例指定名称，只需在其后添加，例如： 
    
    $ incus launch images:archlinux/current/amd64 arch
    
将创建一个名为 `arch` 的 amd64 Arch 容器。 

###  Arch Linux 容器配置

####  在非特权容器中禁用 udev

运行非特权 Arch Linux 容器时，systemd 的 udev 服务会在启动和软件包更新期间（特别是当 [mkinitcpio](<https://archlinux.org/packages/?name=mkinitcpio>)包 运行时）生成大量“权限被拒绝”错误。这是因为 udev 尝试写入由主机拥有的 `/sys/devices/*/uevent` 文件。 

这些错误是由于 Arch 容器镜像针对非特权操作的默认配置不当造成的 —— 容器运行正常。 

根据 [systemd 容器接口](<https://systemd.io/CONTAINER_INTERFACE/>)，`systemd-udevd` 不打算在非特权容器中运行。在容器内屏蔽 udev 服务： 
    
    # systemctl mask \
      systemd-udevd.service \
      systemd-udevd-control.socket \
      systemd-udevd-kernel.socket \
      systemd-udevd-varlink.socket \
      systemd-udev-trigger.service \
      systemd-udev-load-credentials.service
    
**注意：** 这仅适用于非特权容器。具有设备直通功能的特权容器可能需要 udev。

屏蔽后，重启容器： 
    
    $ incus restart _容器名称_
    
##  技巧和窍门

###  在主机上通过名称访问容器

这假设您正在使用默认桥接，其名为 `incusbr0`，并且您正在使用 [systemd-resolved](<../zh-cn/Systemd-resolved.html> "Systemd-resolved")。 
    
    # systemd-resolve --interface incusbr0 --set-domain '~incus' --set-dns $(incus network get incusbr0 ipv4.address | cut -d / -f 1)
    
现在您可以通过名称访问容器： 
    
    $ ping _容器名称_.incus
    
要永久保存此更改，请[编辑](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "编辑") `incus.service` systemd 单元，以包含一个 `ExecStartPost` 指令，该指令在启动后运行命令： 

{{hc/etc/systemd/system/incus.service.d/access_by_name.conf 2= [Service] ExecStartPost=/bin/sh -c 'systemd-resolve --interface incusbr0 --set-domain "~incus" --set-dns $(incus network get incusbr0 ipv4.address | cut -d / -f 1)' }} 

##  故障排除

###  启动虚拟机失败

如果您看到错误： 
    
    Error: Couldn't find one of the required UEFI firmware files: [{code:OVMF_CODE.4MB.fd vars:OVMF_VARS.4MB.ms.fd} {code:OVMF_CODE.2MB.fd vars:OVMF_VARS.2MB.ms.fd} {code:OVMF_CODE.fd vars:OVMF_VARS.ms.fd} {code:OVMF_CODE.fd vars:qemu.nvram}]
    
这是因为 Arch Linux 不分发安全启动签名的 ovmf 固件。要启动虚拟机，您需要暂时禁用安全启动： 
    
    $ incus launch ubuntu:18.04 test-vm --vm -c security.secureboot=false
    
这也可以通过以下方式添加到默认配置文件中： 
    
    $ incus profile set default security.secureboot=false
    
###  网络连接问题

官方文档提供了 [如何配置防火墙](<https://linuxcontainers.org/incus/docs/main/howto/network_bridge_firewalld/#how-to-configure-your-firewall>) 的说明。

**提示：** 除了专用防火墙外，多个程序可能会影响单个系统上的 [nftables](<../zh-cn/Nftables.html> "Nftables")，包括 VPN 和其他虚拟化软件。运行 `nft list ruleset` 以显示所有当前活动的规则。

Incus 创建并管理自己的网络接口，而 [NetworkManager](<../zh-cn/NetworkManager.html> "NetworkManager") 在某些情况下可能会干扰。最好添加一个条目来忽略 `lxcbr*` 设备，使用方法参考 [NetworkManager#忽略特定设备](<../zh-cn/NetworkManager.html#%E5%BF%BD%E7%95%A5%E7%89%B9%E5%AE%9A%E8%AE%BE%E5%A4%87> "NetworkManager")。 

[Docker](<../zh-cn/Docker.html> "Docker") 的默认配置会破坏 Incus 中的网络。如果需要在同一台机器上运行 Docker 和 Incus，请查阅 [官方文档](<https://linuxcontainers.org/incus/docs/main/howto/network_bridge_firewalld/#prevent-connectivity-issues-with-incus-and-docker>)。 

###  Incus 不遵守 Shell 的环境代理变量

示例是 `incus launch` 或 `incus image` 命令在下载镜像时不使用 `*_proxy`/`*_PROXY` 变量的值。 

Incus 实现了服务器-客户端模式。这意味着操作是由作为 [Incus 服务器](<https://linuxcontainers.org/incus/docs/main/server>) 的 `incusd` 执行的 —— 通常在后台运行，除非从交互式 shell 调用。而 `incus` 命令行界面用于与作为 [Incus 客户端](<https://linuxcontainers.org/incus/docs/main/client>) 的 Incus 服务器通信。 

这使得 `incusd`（通常作为服务启动）不继承客户端 shell 的环境变量，而是尊重它被调用时所处环境的变量。[[6]](<https://linuxcontainers.org/incus/docs/main/environment>) 在 Arch Linux 中，Incus 服务器由 systemd 启动。 

针对此问题可以有很多变通方法，以下提供一些示例。更多信息，请参阅 Incus 的 [问题#574](<https://github.com/lxc/incus/issues/574>)。 

####  临时方案

#####  将 Shell 变量导入 systemd 的环境

首先，导出 `*_PROXY` 变量： 
    
    $ export _ALL_ _PROXY="socks://_代理服务器地址_ :_端口_ /"
    
将它们导入 systemd 的环境： 
    
    # systemctl import-environment _ALL_ _PROXY
    
[重新启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重新启动") `incus.service` 单元。 

**提示：** 使用 `systemctl unset-environment` 命令取消设置变量并[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启")服务。

####  持久方案

#####  编辑 incus 服务单元

如果您希望 Incus 守护进程始终使用一些静态环境变量（如 `*_proxy`）启动，您可以使用 [systemd](<../zh-cn/Systemd.html> "Systemd") 的 `environment` 指令。`systemctl set-property` 命令无法操作 `environment` 指令。[编辑](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "编辑") `incus.service` 并添加带有适当 `变量=值` 对的 `environment` 键。例如： 
    
    /etc/systemd/system/incus.service.d/environment.conf
    
    [Service]
    Environment=_ALL_ _PROXY="socks://_proxy_server_address_ :_port_ /"

###  使用 Incus core.proxy 选项

可以通过使用 [配置](<https://linuxcontainers.org/incus/docs/main/howto/server_configure/>) Incus 服务器的 [core.proxy](<https://linuxcontainers.org/incus/docs/main/server_config/#server-core:core.proxy_http>) 选项，使 Incus 服务器使用所需的代理。例如： 
    
    # incus config set core.proxy_http "_代理地址_ :_代理端口_ "
    
**注意：**`core.proxy` 选项具有全局作用域。即它们立即适用于集群成员。

##  卸载

[停止](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "停止")并禁用服务。然后[卸载](<../zh-cn/Pacman.html#%E5%88%A0%E9%99%A4%E8%BD%AF%E4%BB%B6%E5%8C%85> "卸载") [incus](<https://archlinux.org/packages/?name=incus>)包 软件包。 

如果您想删除所有数据： 
    
    # rm -r /var/lib/incus
    
如果您使用了任何示例网络配置，也应该删除它们。 

##  另请参阅

• [官方 Incus 主页](<https://linuxcontainers.org/incus/>)

• [官方文档](<https://linuxcontainers.org/incus/docs/main/>)

• [入门指南](<https://linuxcontainers.org/incus/docs/main/tutorial/first_steps/>)

• [官方论坛](<https://discuss.linuxcontainers.org/>)

• [Incus GitHub 仓库](<https://github.com/lxc/incus>)
