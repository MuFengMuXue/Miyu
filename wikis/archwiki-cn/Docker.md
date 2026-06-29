**翻译状态：**

  * 本文（或部分内容）译自 [Docker](<https://wiki.archlinux.org/title/Docker> "arch:Docker")，最近一次同步于 2025-02-14，若英文版本有所[更改](<https://wiki.archlinux.org/title/Docker?diff=0&oldid=826564>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Docker_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Linux Containers](<../zh-cn/Linux_Containers.html> "Linux Containers")
  * [Podman](<../zh-cn/Podman.html> "Podman")
  * [systemd-nspawn](<../zh-cn/Systemd-nspawn.html> "Systemd-nspawn")
  * [Vagrant](</wzh/index.php?title=Vagrant&action=edit&redlink=1> "Vagrant（页面不存在）")

[Docker](<https://en.wikipedia.org/wiki/Docker_\(software\)> "wikipedia:Docker \(software\)") 是一种打包、传输和运行任何程序作为轻量级容器的实用工具。 

##  安装

要拉取Docker镜像并运行Docker容器，你需要安装Docker引擎，其包含包括一个守护进程来管理容器，以及一个`docker`命令行界面前端。[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [docker](<https://archlinux.org/packages/?name=docker>)包 包或 [docker-git](<https://aur.archlinux.org/packages/docker-git/>)AUR 包(开发版本)。下一步[启用/启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用/启动") `docker.service` 或者 `docker.socket`。两者的差距在于`docker.service`将会在开机时启动，而`docker.socket`将会在第一次启动Docker时启动，使用后者[可以减少开机启动时间](<https://github.com/moby/moby/issues/38373#issuecomment-447393517>)。然后验证操作: 
    
    # docker info
    
注意, 如果你有一个活动的 VPN 连接, 那么 docker 服务的启动可能失败, 因为 VPN 和 Docker 的网桥 IP 冲突以及网络覆盖。如果发生了这种事, 尝试在启动 docker 服务之前断开 VPN 连接. 你可以在之后立刻重连 VPN。[你也可以尝试手动解决网络冲突](<https://stackoverflow.com/questions/45692255/how-make-openvpn-work-with-docker>)(也可参见[[1]](<https://stackoverflow.com/questions/45692255/how-make-openvpn-work-with-docker>)或[[2]](<https://github.com/docker/compose/issues/4336#issuecomment-457326123>))。 

你也可以尝试验证是否可以运行容器。以下命令行将会下载一个最新的[Arch Linux image](<#Arch_Linux>)，并使用其在这个容器中运行一个Hello World程序: 
    
    # docker run -it --rm archlinux bash -c "echo hello world"
    
要删除下载的Arch Linux Docker镜像，请参见[#移除 Docker 和镜像](<#%E7%A7%BB%E9%99%A4_Docker_%E5%92%8C%E9%95%9C%E5%83%8F>)。 

如果你想以普通用户身份运行docker的话，添加你自己到 `docker` [用户组](<../zh-cn/User_group.html> "User group")，重新登录并重启`docker.service`

**警告：** 任何加入到 `docker` 组的用户都和root用户等价，因为他们可以通过运行`# docker run --privileged`来以root权限启动容器。 参见 [此处](<https://github.com/moby/moby/issues/9976>) 以及 [此处](<https://docs.docker.com/engine/security/security/>)。

如果你还要使用 Docker 构建容器镜像，请安装[docker-buildx](<https://archlinux.org/packages/?name=docker-buildx>)包以使用新版构建器(否则会使用已弃用的旧版构建器)。 

### Docker Compose

[Docker Compose](<https://docs.docker.com/compose/>)是另一种Docker引擎的CLI前端,它使用`compose.yaml`[YAML](<https://en.wikipedia.org/wiki/YAML> "wikipedia:YAML")文件来指定容器的属性,这样就可以不使用附带指令的`docker run`脚本了。如果你需要经常设置或者使用具有复杂选项的容器,可能使用docker-compose更为方便。你需要[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") [docker-compose](<https://archlinux.org/packages/?name=docker-compose>)包来使用。 

### Docker Desktop

[Docker Desktop](<https://www.docker.com/products/docker-desktop/>)是一个专有的桌面应用程序,它在一个Linux虚拟机中运行Docker。它还包括Kubernetes集群以及一个漏洞扫描器。这个应用程序对于在macOS或Windows上进行开发Docker容器的团队非常友好。Docker Desktop适配的Linux版本相对较新，同时也保持了对Docker CLI的良好兼容[[3]](<https://www.docker.com/blog/the-magic-of-docker-desktop-is-now-available-on-linux/>)。 

Docker直接为Arch Linux提供了一个实验性的软件包（参见其官方文档[手动安装Docker](<https://docs.docker.com/desktop/linux/install/archlinux/>)一节）。需要注意其手动下载的软件包会与[docker-compose](<https://archlinux.org/packages/?name=docker-compose>)包以及[docker-buildx](<https://archlinux.org/packages/?name=docker-buildx>)包冲突，你需要在安装前手动移除这两个包。如果你想保留现有的软件包，你也可以从AUR安装[docker-desktop](<https://aur.archlinux.org/packages/docker-desktop/>)AUR，它将不会与现有软件包发生冲突。 

此外，在运行[Docker Desktop](<https://www.docker.com/products/docker-desktop/>)之前，你需要确保你已经安装了所有的[在Linux上运行的最小系统要求](<https://docs.docker.com/desktop/install/linux-install/>),包括使用[KVM](<../zh-cn/KVM.html> "KVM")进行虚拟化技术支持。对于Gnome用户，你还需要安装[gnome-shell-extension-appindicator](<https://archlinux.org/packages/?name=gnome-shell-extension-appindicator>)包以显示托盘图标。 

最后，请注意文件共享功能是通过`/etc/subuid`和`/etc/subgid`映射用户和组ID完成的。详细参见[Docker Desktop的Linux文件共享说明](<https://docs.docker.com/get-started/docker-concepts/running-containers/sharing-local-files/>)。 

**注意：** 在Linux上的Docker Desktop会在一个虚拟机(VM)上启动，这个虚拟机会单独创建并使用一个自定义的Docker上下文，即`desktop-linux`。 

这意味着在安装前，部署在Linux Docker引擎上的所有镜像与容器都无法在Docker Desktop中使用。[[4]](<https://docs.docker.com/desktop/install/linux-install/>)

更多信息请参见[Docker Desktop for Linux和Docker Engine的区别](<https://docs.docker.com/desktop/setup/install/linux/>)。 

此外，由于Docker Desktop是在VM上启动的，相比直接使用Docker引擎，预期性能会下降并且 CPU 使用率会提高。 

默认情况下，Docker Desktop会启用一个用户级别的systemd服务，该服务会在启动时自动启动应用程序。在Docker Desktop仪表板中禁用“自动启动”设置[并不能](<https://github.com/docker/desktop-linux/issues/182>)阻止此服务启动（链接的页面包含修复方法）。 

###  前端工具

  * **DockStation** — 一个以开发者为中心的应用程序（GUI），用于管理基于Docker的项目。

     <https://github.com/DockStation/dockstation> || [dockstation](<https://aur.archlinux.org/packages/dockstation/>)AUR

  * **Ducker** — 一个用于管理Docker容器的终端应用程序。

     <https://github.com/robertpsoane/ducker> || [ducker](<https://archlinux.org/packages/?name=ducker>)包

  * **goManageDocker** — 一个用于管理Docker对象的TUI工具。

     <https://github.com/ajayd-san/gomanagedocker> || [gomanagedocker](<https://aur.archlinux.org/packages/gomanagedocker/>)AUR

  * **Lazydocker** — 一个简单的终端UI，用于管理docker和docker-compose，使用Go语言编写，基于gocui库。

     <https://github.com/jesseduffield/lazydocker> || [lazydocker](<https://aur.archlinux.org/packages/lazydocker/>)AUR

  * **oxker** — 一个简单的TUI，用于查看和控制Docker容器。

     <https://github.com/mrjackwills/oxker> || [oxker-bin](<https://aur.archlinux.org/packages/oxker-bin/>)AUR

  * **Podman Desktop** — 从单一UI和托盘中管理Podman和其他容器引擎。

     <https://github.com/containers/podman-desktop> || [podman-desktop](<https://aur.archlinux.org/packages/podman-desktop/>)AUR

  * **Portainer** — 一个轻量级的Docker管理UI。

     <https://github.com/portainer/portainer> || [portainer-bin](<https://aur.archlinux.org/packages/portainer-bin/>)AUR

  * **Whaler** — 为Pantheon设计的Docker容器管理工具。

     <https://github.com/sdv43/whaler> || [whaler-git](<https://aur.archlinux.org/packages/whaler-git/>)AUR

##  使用

Docker由多个部分组成: 

  * Docker守护进程(也称Docker引擎),这是一个以`docker.service`形式运行的进程。其提供了Docker API接口并管理Docker容器。

  * `docker` CLI命令,其允许用户使用命令行来与Docker API交互，并控制 Docker 守护进程。

  * Docker容器，这是一种命名进程，由Docker守护进程通过Docker API的请求进行管理。

一般来说，用户通过使用`docker`命令行来对Docker进行操作,命令行又通过Docker API对Docker守护进程发起请求以执行对容器的相关操作。掌握客户端 (`docker`), 服务端(`docker.service`)和容器之间的关系是很必要的。 

请注意，如果Docker守护进程停止/重启，那么当前运行的所有Docker容器也会停止/重启。 

你也可以不借助`docker` CLI来对Docker API发起请求来控制容器，参见[Docker API开发指南](<https://docs.docker.com/engine/api/>)。 

更多使用文档请参见[Docker入门指南](<https://docs.docker.com/get-started/>)。 

##  配置

Docker守护进程可以通过修改配置文件`/etc/docker/daemon.json`或者直接在`docker.service`中添加命令行标志来进行配置。根据[Docker官方文档](<https://docs.docker.com/config/daemon/#configure-the-docker-daemon>), 推荐使用修改配置文件的方法进行配置。如果你想使用添加命令行标志的方法进行配置，使用[Systemd#附加配置片段](<../zh-cn/Systemd.html#%E9%99%84%E5%8A%A0%E9%85%8D%E7%BD%AE%E7%89%87%E6%AE%B5> "Systemd")覆盖`docker.service`中的`ExecStart`部分。 

对于`daemon.json`中的选项，参见[守护进程配置文件参考](<https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-configuration-file>)。 

###  存储驱动程序

[存储驱动程序](<https://docs.docker.com/storage/storagedriver/select-storage-driver/>)控制着Docker主机上的镜像与容器的储存与管理方式。默认的`overlay2`驱动在大部分情况下都具有良好的性能。 

如果你的文件系统使用的是[btrfs](<../zh-cn/Btrfs.html> "Btrfs")或者[ZFS](<../zh-cn/ZFS.html> "ZFS")，你可以使用对应的`btrfs`或者`zfs`驱动,它们可以利用这些文件系统独有的功能，要使用这些驱动请参见[btrfs驱动](<https://docs.docker.com/storage/storagedriver/btrfs-driver/>)或[zfs驱动](<https://docs.docker.com/storage/storagedriver/zfs-driver/>)文档。 

###  启用守护进程TCP套接字

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** [Docker 26 弃用了未经身份验证的TCP连接，并计划在Docker 27中移除。](<https://docs.docker.com/engine/deprecated/#unauthenticated-tcp-connections>) (在[Talk:Docker](<../zh-cn/Talk:Docker.html>)讨论)

默认情况下,Docker守护进程使用位于`/var/run/docker.sock`的[Unix套接字](<https://en.wikipedia.org/wiki/Unix_domain_socket> "wikipedia:Unix domain socket")来提供Docker API。大部分情况下，这是一个合适的选择。 

你可以将设置守护进程设置为额外监听TCP套接字,这样就能使Docker API被远程访问了(参见[允许远程访问Docker API](<https://docs.docker.com/engine/install/linux-postinstall/#allow-access-to-the-remote-api-through-a-firewall>))。如果你在Windows或macOS上使用Arch虚拟机，你可以在完成设置后使用宿主机上直接使用`docker`命令行访问虚拟机中允许的Docker守护进程。 

**警告：** Docker API默认情况下既没有加密也没有身份验证。除非你在附加Docker配置中启用了 [使用SSH或TLS进行连接](<https://docs.docker.com/engine/security/protect-access/>)，否则对Docker守护进程的TCP访问等同于不安全的远程root访问。

注意默认的`docker.service`设置了`-H`标志，如果选项同时存在于标志与`/etc/docker/daemon.json`文件中，Docker将不会启动，因此最简单的更改监听TCP套接字设置的方法是使用一个附加文件。例如，如果你想在端口2376添加一个TCP套接字: 
    
    /etc/systemd/system/docker.service.d/docker.conf
    
    [Service]
    ExecStart=
    ExecStart=/usr/bin/dockerd -H unix:///var/run/docker.sock -H tcp://0.0.0.0:2376

[重载](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Reload")systemd守护进程并[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `docker.service`以应用更改。 

###  HTTP代理

要想在Docker中使用HTTP代理，你需要同时对Docker守护进程以及Docker容器进行配置。 

####  Docker守护进程代理设置

参见[Docker文档：配置Docker守护进程使用HTTP代理](<https://docs.docker.com/config/daemon/systemd/#httphttps-proxy>)。 

####  Docker容器代理设置

参见[Docker文档：如何配置代理](<https://docs.docker.com/network/proxy/#configure-the-docker-client>)，使用`docker`CLI来自动为所有容器配置代理。 

###  配置DNS

参见[Docker中网络配置](<https://docs.docker.com/config/containers/container-networking/#dns-services>)了解Docker容器内部的DNS行为以及如何自定义Docker的DNS配置信息。一般来说，主机上的配置也会直接配置到容器中。 

大部分托管在`127.0.0.0/8`上的DNS解析器都是[不被支持的](<https://github.com/moby/moby/issues/6388#issuecomment-76124221>)(由于容器和主机网络命名空间之间的冲突)。这些解析器会在[容器中的/etc/resolv.conf中删除](<https://github.com/moby/libnetwork/blob/master/resolvconf/resolvconf.go>)。如果这导致了`/etc/resolv.conf`为空文件,容器将会使用Google DNS。 

此外，如果`127.0.0.53`是唯一的名称服务器，在这种特定的情况下Docker会假设解析器是[systemd-resolved](<../zh-cn/Systemd-resolved.html> "Systemd-resolved")并使用来自`/run/systemd/resolve/resolv.conf`的上游DNS解析器。 

如果你使用[dnsmasq](<../zh-cn/Dnsmasq.html> "Dnsmasq")来提供一个本地解析器，考虑为dnsmasq添加一个虚拟接口(使用`169.254.0.0/16`网段的链路本地IP地址来绑定，而不是`127.0.0.1`)以避免网络命名空间冲突。 

###  镜像位置

默认，docker镜像放置在 `/var/lib/docker`。他们可以被移动到其他分区，例如你想将镜像移动到别的磁盘上，在这个例子中，假设我们要将镜像移动到`/mnt/docker`。 

首先, [停止](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Stop")`docker.service`,注意，这也会停止所有当前运行的容器并卸载任何正在运行的镜像。 

如果你正在运行docker镜像，你必须确定镜像被完全解除挂载。一旦这个完成后，你就可以把镜像从 `/var/lib/docker` 移动到你的目标地点。在这个例子中使用指令`cp -r /var/lib/docker /mnt/docker`。 

在`/etc/docker/daemon.json`中配置`data-root`: 
    
    /etc/docker/daemon.json
    
    {
      "data-root": "/mnt/docker"
    }

[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启")`docker.service`以应用更改。 

###  不安全的自建仓库

如果你使用自签名证书的仓库(registries)，或该自建仓库未使用TLS加密（即通过http连接）, docker会拒绝连接。你需要将其添加到信任列表中。 例如，要信任托管于`myregistry.example.com:8443`上的镜像,在文件`/etc/docker/daemon.json`中配置`insecure-registries`的值： 
    
    /etc/docker/daemon.json
    
    {	
      "insecure-registries": [
        "my.registry.example.com:8443"
      ]
    }

随后[重新加载](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Reload") `docker.service`配置。 

### IPv6

为了开启Docker中的IPv6支持,参见[[5]](<https://github.com/moby/moby.github.io/blob/c0eb65aabe4de94d56bbc20249179f626df5e8c3/engine/userguide/networking/default_network/ipv6.md>)与[[6]](<https://github.com/moby/moby/issues/36954>)。 

首先，将`/etc/docker/daemon.json`中的`ipv6`设置为启用并设置一个特定的IPV6子网(即使用私有的`fd00::/80`子网)。请确保至少使用80位的子网，因为这样可以使容器的IPv6地址以容器的MAC地址结尾，这有助于解决NDP邻居缓存失效的问题。 
    
    /etc/docker/daemon.json
    
    {
      "ipv6": true,
      "fixed-cidr-v6": "fd00::/80"
    }
    
[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") `docker.service`以应用更改。 

最后，为了让容器能够访问主机网络，你需要添加IPv6 NAT以解决使用私有IPv6子网时出现的路由问题: 
    
    # ip6tables -t nat -A POSTROUTING -s fd00::/80 ! -o docker0 -j MASQUERADE
    
现在Docker应该已经开启了IPv6支持，你可以使用以下指令来进行测试： 
    
    # docker run curlimages/curl curl -v -6 archlinux.org
    
如果你使用[firewalld](<../zh-cn/Firewalld.html> "Firewalld"),你还需要添加防火墙规则，例如： 
    
    # firewall-cmd --zone=public --add-rich-rule='rule family="ipv6" destination not address="fd00::1/80" source address="fd00::/80" masquerade'
    
如果你使用[ufw](<../zh-cn/Uncomplicated_Firewall.html> "Ufw"),你还需要根据[Uncomplicated Firewall#转发策略](<../zh-cn/Uncomplicated_Firewall.html#%E8%BD%AC%E5%8F%91%E7%AD%96%E7%95%A5> "Uncomplicated Firewall")创建Ipv6转发。 

首先，你需要编辑`/etc/default/ufw`并取消以下几行的注释： 
    
    /etc/ufw/sysctl.conf
    
    net/ipv6/conf/default/forwarding=1
    net/ipv6/conf/all/forwarding=1

现在你可以使用以下命令添加iptables规则: 
    
    # ip6tables -t nat -A POSTROUTING -s fd00::/80 ! -o docker0 -j MASQUERADE
    
如果你使用 _docker-compose_ 来创建的容器,你可能还需要在`networks`中对应的部分设置`enable_ipv6: true`。另外，你可能还需要手动指定IPv6子网，参见[compose-file中的ipv6地址设置](<https://docs.docker.com/compose/compose-file/compose-file-v2/#ipv4_address-ipv6_address>)。 

###  用户命名空间隔离

默认情况下，Docker中的进程和`dockerd`主守护程序运行在同一用户命名空间中，即容器不会通过用户命名空间隔离(参见[user_namespaces(7)](<https://man.archlinux.org/man/user_namespaces.7>))。这将会允许进程根据[用户和用户组#权限与属主](<../zh-cn/%E7%94%A8%E6%88%B7%E5%92%8C%E7%94%A8%E6%88%B7%E7%BB%84.html#%E6%9D%83%E9%99%90%E4%B8%8E%E5%B1%9E%E4%B8%BB> "用户和用户组")在主机上来访问已配置的资源。这样提升了容器运行的兼容性，但是一旦出现了一个允许容器中进程访问非预期资源的漏洞，这会带来很大的安全隐患。(一个这样的漏洞[在2019年2月发布并修补](<https://seclists.org/oss-sec/2019/q1/119>)。) 

启用[用户命名空间隔离](<https://docs.docker.com/engine/security/userns-remap/>)可以降低此类漏洞的影响。其将会在单独的用户命空间中运行每个容器，并将这个空间中的UIDs/GIDs映射到主机上不同的(通常情况下也是非特权的)UIDs/GIDs。 

**注意：**

  * 主`dockerd`守护程序依然是以`root`身份在主机上运行的，在[非root身份下运行docker](<https://docs.docker.com/engine/security/rootless/>)(rootless mode)是另一个功能。
  * 容器中的进程将会以Dockerfile中定义的[USER](<https://docs.docker.com/engine/reference/builder/#user>)指令定义的用户身份启动。
  * 所有容器都会映射到相同的UID/GID范围，这是为了让容器之间的共享卷功能生效。
  * [在一些情况下](<https://docs.docker.com/engine/security/userns-remap/#user-namespace-known-limitations>)无法启用用户命名空间。
  * 由于 Docker 需要调整这些资源的所有权，因此启用用户命名空间隔离会有效屏蔽现有的映像层和容器层，以及 `/var/lib/docker/` 中的其他 Docker 对象。上游文档建议仅在新安装的Docker上启用此功能，而不是在现有的Docker上启用。

在`/etc/docker/daemon.json`中配置`userns-remap`的值。`default`是一个特殊值，其会自动创建名为`dockremap`的用户与用户组用于重映射。 
    
    /etc/docker/daemon.json
    
    {
      "userns-remap": "default"
    }

在`/etc/subuid`和`/etc/subgid`中配置用户名/组名，UID/GID的范围。在这个例子中，`dockremap`用户/用户组分配为从165536开始的65536个UIDs/GIDs。 
    
    /etc/subuid
    
    dockremap:165536:65536
    
    /etc/subgid
    
    dockremap:165536:65536

重启`docker.service`以应用更改。 

应用此更改后，默认情况下所有容器都将在隔离的用户命名空间中运行。你也可以在`docker`命令中加上添加标志`--userns=host`来在特定的容器中禁用用户命名空间隔离，参见[[7]](<https://docs.docker.com/engine/security/userns-remap/#disable-namespace-remapping-for-a-container>)。 

###  非特权模式运行Docker守护程序(Docker rootless)

**注意：** 非特权模式下运行Docker守护程序(Docker rootless)依赖于非特权用户命名空间(`CONFIG_USER_NS_UNPRIVILEGED`)。在[linux](<https://archlinux.org/packages/?name=linux>)包, [linux-lts](<https://archlinux.org/packages/?name=linux-lts>)包, 和[linux-zen](<https://archlinux.org/packages/?name=linux-zen>)包内核中默认启用这一功能。如果你使用其他版本的内核，你可能需要手动启用这一功能。这可能带来一些安全隐患，参见[安全#沙盒程序](<../zh-cn/%E5%AE%89%E5%85%A8.html#%E6%B2%99%E7%9B%92%E7%A8%8B%E5%BA%8F> "安全")。

要将Docker守护程序作为普通用户运行，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [docker-rootless-extras](<https://aur.archlinux.org/packages/docker-rootless-extras/>)AUR软件包。 

随后在`/etc/subuid`与`/etc/subgid`中配置用户名/用户组名，起始 UID/GID 和 UID/GID 范围大小，以分配重新映射的用户和组。以下是一个示例： 
    
    /etc/subuid
    
    your_username:165536:65536
    
    /etc/subgid
    
    your_username:165536:65536

[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `docker.socket` [systemd/用户](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "Systemd/用户")单元: 这将会使用systemd的套接字激活来启动docker。 

最后设置docker套接字的[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量"): 
    
    $ export DOCKER_HOST=unix://$XDG_RUNTIME_DIR/docker.sock
    
###  启用本地覆盖差异引擎(native overlay diff engine)

默认情况下Docker无法在Arch Linux上使用本地覆盖差异引擎(native overlay diff engine),这会导致构建Docker镜像很慢。如果你经常构建镜像，请按照[以下步骤](<https://mikeshade.com/posts/docker-native-overlay-diff/>)配置: 
    
    /etc/modprobe.d/disable-overlay-redirect-dir.conf
    
    options overlay metacopy=off redirect_dir=off

随后[停止](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "停止")`docker.service`, 重新加载`overlay`内核模块: 
    
    # modprobe -r overlay
    # modprobe overlay
    
重载内核模块后，[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")`docker.service`。 

要验证是否成功启用，你可以运行`docker info`检查`Native Overlay Diff`值是否为`true`。 

##  镜像

### Arch Linux

下面的命令会拉取 [archlinux](<https://hub.docker.com/_/archlinux/>) x86_64 image。这是一个arch内核的剥离版本，没有网络等功能。 
    
    # docker pull archlinux
    
另请参阅 [README.md](<https://gitlab.archlinux.org/archlinux/archlinux-docker/blob/master/README.md>)。 

对于完整的arch镜像，可以从下面克隆镜像并且建立你自己的基础镜像。 
    
    $ git clone <https://gitlab.archlinux.org/archlinux/archlinux-docker.git>
    
请确保[devtools](<https://archlinux.org/packages/?name=devtools>)包, [fakechroot](<https://archlinux.org/packages/?name=fakechroot>)包以及[fakeroot](<https://archlinux.org/packages/?name=fakeroot>)包软件包已被安装。 

随后编辑构建文件并运行： 
    
    # make docker-image
    
### Alpine Linux

[Alpine Linux](<https://www.alpinelinux.org/>)是一个热门的小型容器镜像，其比较适合运行静态二进制形式软件。使用以下命令来拉取最新的Alpine Linux镜像: 
    
    # docker pull alpine
    
Alpine Linux使用[musl](<https://musl.libc.org/>) libc实现，这有区别与大部分的Linux发行版使用的[glibc](<https://www.gnu.org/software/libc/>) libc实现。 由于Arch Linux使用的glibc,因此Arch Linux主机与Alpine Linux容器之间存在有功能差异，这可能会影响软件性能或正确性。你可以在[此处](<https://wiki.musl-libc.org/functional-differences-from-glibc.html>)查看存在的差异。 

注意，在Arch Linux(或其他没有使用musl libc实现的发行版)上编译的动态链接软件在Alpine Linux (或其他使用musl libc的镜像)上可能会出现错误或性能问题。参见[[8]](<https://bugs.python.org/issue32307>), [[9]](<https://superuser.com/questions/1219609/why-is-the-alpine-docker-image-over-50-slower-than-the-ubuntu-image>)和[[10]](<https://pythonspeed.com/articles/alpine-docker-python>)。 

### Debian

下面的命令以拉取Debian镜像 [debian x86_64](<https://hub.docker.com/_/debian>)。 
    
    # docker pull debian
    
请参阅[Docker Hub页面](<https://hub.docker.com/_/debian/tags>)查看可用标签的完整列表，包括每个Debian版本的标准版与精简版。 

####  手动

用 [debootstrap](<https://archlinux.org/packages/?name=debootstrap>)包建立Debian镜像: 
    
    # mkdir jessie-chroot
    # debootstrap jessie ./jessie-chroot <http://http.debian.net/debian/>
    # cd jessie-chroot
    # tar cpf - . | docker import - debian
    # docker run -t -i --rm debian /bin/bash
    
### Distroless

Google 维护着[distroless镜像](<https://github.com/GoogleContainerTools/distroless>)，这是没有基本操作系统组件(例如shells和包管理器)的最小化镜像。其最小镜像`gcr.io/distroless/static-debian11`仅有2MiB左右，可以用于打包软件并生成非常小的镜像。 

请参阅GitHub中的README以获得镜像列表以及在不同编程语言中的使用方法。 

##  有用的建议

###  抓取运行容器的IP地址

抓取运行容器的IP地址: 
    
    $ docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container-name OR id> 
    
    172.17.0.37

每个正在运行的容器，它们的名字和相关IP地址都能被列出来在 `/etc/hosts`里用: 
    
    #!/usr/bin/env sh
    for ID in $(docker ps -q | awk '{print $1}'); do
        IP=$(docker inspect --format="{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}" "$ID")
        NAME=$(docker ps | grep "$ID" | awk '{print $NF}')
        printf "%s %s\n" "$IP" "$NAME"
    done

###  运行容器中的图像程序

本节介绍了允许在主机的X服务器上运行图形程序（包括依赖于OpenGL或Vulkan的程序）所需的步骤。 

首先，需要在容器内安装与**主机** 图形硬件兼容的正确驱动程序。如果容器使用的Arch Linux镜像，请参见[OpenGL#安装](<../zh-cn/OpenGL.html#%E5%AE%89%E8%A3%85> "OpenGL")或 [Vulkan#安装](<../zh-cn/Vulkan.html#%E5%AE%89%E8%A3%85> "Vulkan")来安装对应的驱动。 

接下来，你需要授予容器访问主机上X服务的权限。在单用户环境中，你可以通过在主机中运行[Xhost](<../zh-cn/Xhost.html> "Xhost")来完成这一操作。该命令将非网络本地连接添加到访问控制列表： 
    
    $ xhost +local:
    
最后，你需要在`docker run`中传递以下参数: 

  * `-e "DISPLAY=$DISPLAY"`将环境变量`DISPLAY`设置为主机显示器;
  * `--mount type=bind,src=/tmp/.X11-unix,dst=/tmp/.X11-unix`将主机X服务器套接字挂载到相同路径下的容器内;
  * `--device=/dev/dri:/dev/dri`允许容器直接访问主机上的[直接渲染(DRI)](<https://en.wikipedia.org/wiki/Direct_Rendering_Infrastructure> "wikipedia:Direct Rendering Infrastructure") 设备。

为了验证设置是否生效，请在容器中运行[mesa-utils](<https://archlinux.org/packages/?name=mesa-utils>)包中的`glxgears`命令(或者[vulkan-tools](<https://archlinux.org/packages/?name=vulkan-tools>)包中的`vkcube`命令)。 

###  开机启动 Docker Compose 项目

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 没有必要在`compose.yml`中启用`restart: always`(讨论请参见[[11]](<https://wiki.archlinux.org/title/Talk:Docker#%22Start_Docker_Compose_projects_on_boot%22_Spurious?>))。[[12]](<https://docs.docker.com/compose/compose-file/compose-file-v3/#restart>)（在 [Talk:Docker#"开机启动 Docker Compose 项目" 是否多余?](</wzh/index.php?title=Talk:Docker&action=edit&redlink=1> "Talk:Docker（页面不存在）") 中讨论）

首先，创建一个用于Docker Compose的Systemed[单元](<../zh-cn/Systemd.html#%E7%BC%96%E5%86%99%E5%8D%95%E5%85%83%E6%96%87%E4%BB%B6> "Systemd")，并通过服务名称进行参数化(参见[systemd.service(5) § SERVICE TEMPLATES](<https://man.archlinux.org/man/systemd.service.5#SERVICE_TEMPLATES>)): 
    
    /etc/systemd/system/docker-compose@.service
    
    [Unit]
    Description=%i service with docker compose
    Requires=docker.service
    After=docker.service
    
    [Service]
    WorkingDirectory=/opt/%i
    ExecStartPre=-/usr/bin/docker compose pull
    ExecStart=/usr/bin/docker compose up --remove-orphans
    ExecStop=/usr/bin/docker compose down
    ExecReload=/usr/bin/docker compose pull
    ExecReload=/usr/bin/docker compose up --remove-orphans
    
    [Install]
    WantedBy=multi-user.target

随后，对于你想运行的每一个服务，在`/opt/_project_name_`目录下新建一个包含Compose文件以及其他所需文件(例如`.env`文件)[[13]](<https://refspecs.linuxfoundation.org/FHS_3.0/fhs/ch03s13.html>)。 

最后, [启用/启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用/启动") `docker-compose@_project_name_.service`。 

###  使用buildx进行交叉编译

[buildx CLI 插件](<https://docs.docker.com/build/architecture/#buildx>)使用了新的[BuildKit构建工具包](<https://docs.docker.com/build/buildkit/>)。[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")[docker-buildx](<https://archlinux.org/packages/?name=docker-buildx>)包，buildx接口支持构建多平台镜像(包括与主机不同的框架)。 

交叉编译镜像也需要QEMU。如果你想在Docker中设置静态版本的QEMU，请参见[multiarch/qemu-user-static](<https://github.com/multiarch/qemu-user-static>) 镜像。否则请在主机上设置QEMU与Docker共同使用(参见[QEMU#从 x86_64 环境中 Chroot 至 arm/arm64 环境](<../zh-cn/QEMU.html#%E4%BB%8E_x86_64_%E7%8E%AF%E5%A2%83%E4%B8%AD_Chroot_%E8%87%B3_arm/arm64_%E7%8E%AF%E5%A2%83> "QEMU"))。无论哪种情况，你的系统都将配置为对客户端架构进行用户模式模拟。 
    
    $ docker buildx ls
    
    NAME/NODE DRIVER/ENDPOINT STATUS  PLATFORMS
    default * docker                  
      default default         running linux/amd64, linux/386, linux/arm64, linux/riscv64, linux/s390x, linux/arm/v7, linux/arm/v6
    
###  用NVIDIA GPU运行GPU加速的Docker容器

从19.03版本开始，Docker[原生支持](<https://docs.docker.com/config/containers/resource_constraints/>)NVIDIA GPU作为Docker设备。 推荐使用[NVIDIA Container Toolkit](<https://github.com/NVIDIA/nvidia-container-toolkit>)来运行需要操作NVIDIA显卡的容器。 安装 [nvidia-container-toolkit](<https://archlinux.org/packages/?name=nvidia-container-toolkit>)包 包并[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart")Docker。之后可以用`--gpus`选项来运行使用NVIDIA显卡的容器 

####  使用 --gpus 选项（推荐）
    
    # docker run --gpus all nvidia/cuda:12.1.1-runtime-ubuntu22.04 nvidia-smi
    
指定容器内可使用多少GPU： 
    
    # docker run --gpus 2 nvidia/cuda:12.1.1-runtime-ubuntu22.04 nvidia-smi
    
指定使用哪一个GPU： 
    
    # docker run --gpus '"device=1,2"' nvidia/cuda:12.1.1-runtime-ubuntu22.04 nvidia-smi
    
或 
    
    # docker run --gpus '"device=UUID-ABCDEF,1"' nvidia/cuda:12.1.1-runtime-ubuntu22.04 nvidia-smi
    
[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** More information on when the following error happens is needed. It should work, see [[14]](<https://aur.archlinux.org/cgit/aur.git/tree/nvidia-container-toolkit.install?h=nvidia-container-toolkit>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2023-04-23 ⓘ].（在 [Talk:Docker#GPU accelerated Docker Nvidia](</wzh/index.php?title=Talk:Docker&action=edit&redlink=1> "Talk:Docker（页面不存在）") 中讨论）

如果在执行指令时收到错误`Failed to initialize NVML: Unknown Error`,你可以尝试详细指定GPU来解决这个问题: 
    
    # docker run --gpus all --device /dev/nvidiactl:/dev/nvidiactl --device /dev/nvidia-uvm:/dev/nvidia-uvm --device /dev/nvidia0:/dev/nvidia0 nvidia/cuda:12.1.1-runtime-ubuntu22.04 nvidia-smi
    
指定需要的具体功能（图像、计算等） 
    
    # docker run --gpus all,capabilities=utility nvidia/cuda:12.1.1-runtime-ubuntu22.04 nvidia-smi
    
参阅 [container-toolkit文档](<https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/index.html>)与[安装指南](<https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html>)。 

####  使用 NVIDIA Container Runtime

编辑`/etc/docker/daemon.json`以注册NVIDIA运行时环境。 
    
    /etc/docker/daemon.json
    
    {
      "runtimes": {
        "nvidia": {
          "path": "/usr/bin/nvidia-container-runtime",
          "runtimeArgs": []
        }
      }
    }

之后[重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Restart") Docker。 

运行时也可以通过 _dockerd_ 的一个命令行选项来注册。 
    
    # /usr/bin/dockerd --add-runtime=nvidia=/usr/bin/nvidia-container-runtime
    
完成后可通过命令启动GPU加速的容器: 
    
    # docker run --runtime=nvidia nvidia/cuda:9.0-base nvidia-smi
    
或（要求 Docker 版本19.03或更高） 
    
    # docker run --gpus all nvidia/cuda:9.0-base nvidia-smi
    
参阅 [README.md](<https://github.com/NVIDIA/nvidia-container-toolkit/tree/main/cmd/nvidia-container-runtime>)。 

####  有CUDA的 Arch Linux 镜像

可使用以下`Dockerfile` 构建自定义的有CUDA的 Arch Linux 镜像。它使用 [Dockerfile frontend syntax 1.2](<https://github.com/moby/buildkit/blob/master/frontend/dockerfile/docs/syntax.md>) 在宿主机上缓存pacman包。请注意，你必须在构建镜像之前设置[环境变量](<../zh-cn/%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F.html> "环境变量")`DOCKER_BUILDKIT=1`。 
    
    Dockerfile
    
    # syntax=docker/dockerfile:1.2
    
    FROM archlinux:base-devel
    
    # 安装包
    RUN --mount=type=cache,sharing=locked,target=/var/cache/pacman \
        pacman -Syu --noconfirm --needed cuda
    
    # 配置 nvidia container runtime
    # https://github.com/NVIDIA/nvidia-container-toolkit/tree/main/cmd/nvidia-container-runtime#environment-variables-oci-spec
    ENV NVIDIA_VISIBLE_DEVICES=all
    ENV NVIDIA_DRIVER_CAPABILITIES=compute,utility
    
##  移除 Docker 和镜像

如果你想完全移除 Docker，你可以通过下面的步骤完成： 

**注意：** 不要仅仅只是复制粘贴下面的命令而不知道你在干什么！

检查正在运行的容器： 
    
    # docker ps
    
列出在主机运行的所有容器，为删除做准备： 
    
    # docker ps -a
    
停止一个运行的容器： 
    
    # docker stop <CONTAINER ID>
    
杀死还在运行的容器： 
    
    # docker kill <CONTAINER ID>
    
通过 ID 删除列出的所有容器： 
    
    # docker rm <CONTAINER ID>
    
列出所有的 Docker 镜像： 
    
    # docker images
    
通过 ID 删除所有镜像： 
    
    # docker rmi <IMAGE ID>
    
删除所有与容器没有关联的镜像、容器、卷与网络（悬空）： 
    
    # docker system prune
    
要删除所有停止的容器和所有未使用的镜像（而不只是悬空镜像），添加 `-a` 标志： 
    
    # docker system prune -a
    
删除所有 Docker 数据（清除目录）： 
    
    # rm -R /var/lib/docker
    
##  故障排除

###  使用systemd-networkd时,docker0 网桥无法获取 IP / Internet 到容器

Docker会自己启用IP转发，但是默认 [systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd") 会覆盖对应的sysctl设置，在网络配置文件里设置 `IPForward=yes`。查阅[网络分享#启用包转发](<../zh-cn/%E7%BD%91%E7%BB%9C%E5%88%86%E4%BA%AB.html#%E5%90%AF%E7%94%A8%E5%8C%85%E8%BD%AC%E5%8F%91> "网络分享")获取细节。 

当[systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd")尝试管理由Docker创建的网络时，如果你在`Match`部分设置了`Name=*`或`Type=ether`，这可能会导致网络连接出现问题。请更为具体地配置接口，即尽可能避免使用`Name=*`，`Type=ether`等通配符来匹配Docker管理的接口。你可以验证 `networkctl list` 是否在 Docker 创建的所有网络的 SETUP 栏中设置为 `unmanaged`。 

**注意：**

  * 你可能需要在每次 [重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `systemd-networkd.service` 或者 `iptables.service` 之后，再手动重启 `docker.service`。
  * 注意[nftables](<../zh-cn/Nftables.html> "Nftables")默认情况下可能会禁止Docker的连接，你可以使用命令 `nft list ruleset` 来检查规则集。
  * 你可以使用 `nft flush chain inet filter forward` 来临时移除所有转发规则，或者编辑 `/etc/nftables.conf` 文件使其永久生效。在更改了配置文件，请 [重启](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "重启") `nftables.service` 以应用更改。详细了解Docker的nftables支持请参见 [[15]](<https://github.com/moby/moby/issues/26824>)。

###  默认的允许的进程/线程数太少

如果你允许时得到下面的错误信息 
    
    # e.g. Java
    java.lang.OutOfMemoryError: unable to create new native thread
    # e.g. C, bash, ...
    fork failed: Resource temporarily unavailable
    
那么你可能需要调整被systemd允许的进程数, [编辑](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "编辑")并添加下面片段 `docker.service` : 
    
    # systemctl edit docker.service
    
    [Service]
    TasksMax=infinity

对于更多参数,例如 `DefaultLimitNPROC`，请参阅 [systemd-system.conf(5) § OPTIONS](<https://man.archlinux.org/man/systemd-system.conf.5#OPTIONS>)。对于 `TasksMax` 请参阅 [systemd.resource-control(5) § OPTIONS](<https://man.archlinux.org/man/systemd.resource-control.5#OPTIONS>)。 

###  无法创建到某文件的路径: 设备没有多余的空间了

如果你在创建或者运行Docker镜像时获取到类似的错误信息: 
    
    ERROR: Failed to create some/path/to/file: No space left on device
    
如此时磁盘还有多余的空间，请确保: 

  * [Tmpfs](<../zh-cn/Tmpfs.html> "Tmpfs") 被禁用了并且有足够的内存分配. Docker可能会尝试写入文件到 `/tmp` 但是失败了因为内存使用的限制和磁盘空间不足.
  * 如果你在使用 [XFS](<../zh-cn/XFS.html> "XFS"), 你可能得从相关入口移除 `noquota` 挂载选项在 `/etc/fstab`里 (通常是 `/tmp` 和/或 `/var/lib/docker` 在的地方). 查阅 [Disk quota](</wzh/index.php?title=Disk_quota&action=edit&redlink=1> "Disk quota（页面不存在）") 获取更多信息, 特别是你计划使用和调整 `overlay2` Docker 存储驱动.
  * XFS 的配额挂载选项在文件系统重新挂载时 (`uquota`, `gquota`, `prjquota`, 等等.) 失败了. 为了为root文件系统启用配额挂载选项必须作为[内核参数](<../zh-cn/%E5%86%85%E6%A0%B8%E5%8F%82%E6%95%B0.html> "内核参数") `rootflags=`传递到initramfs. 之后, 它就不应该在 `/etc/fstab`中的挂载选项中列出root (`/`) 文件系统.

**注意：** XFS配额和标准Linux[Disk quota](</wzh/index.php?title=Disk_quota&action=edit&redlink=1> "Disk quota（页面不存在）"), [[16]](<https://inai.de/linux/adm_quota>) 是有区别的。这里值得一读。

###  Docker-machine无法使用virtualbox驱动程序创建虚拟机

如果docker-machine 无法使用 virtualbox 驱动程序创建虚拟机并提供了以下信息: 
    
    VBoxManage: error: VBoxNetAdpCtl: Error while adding new interface: failed to open /dev/vboxnetctl: No such file or directory
    
尝试在CLI中使用`vboxreload`重启virtualbox。 

###  启动Docker后会破坏KVM的桥接网络

这是因为启动Docker的脚本会添加一些iptables规则,其会阻止除自身外的其他接口进行转发。这是一个[已知问题](<https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=865975>)。 

您可以尝试以下的解决方案(请将br0替换为您自己的桥接网络名称): 

  * 最快的解决方案(但是这会关闭所有Docker自动添加的iptables规则):

    /etc/docker/daemon.json
    
    {
      "iptables": false
    }

  * 如果您已经配置好了用于KVM的桥接网络，您也可以通过修改Docker的配置文件来解决这个问题，参见[[17]](<https://muthii.com/blog/?p=540>)将配置文件修改为：

    /etc/docker/daemon.json
    
    {
      "bridge": "br0"
    }

  * 如果上述方法无效，或者您希望直接通过iptables或者类似于UFW的管理器来解决问题，请添加以下内容:

    iptables -I FORWARD -i br0 -o br0 -j ACCEPT

更详细的解决方案可以参见[此处](<https://serverfault.com/questions/963759/docker-breaks-libvirt-bridge-network>)。 

###  从Docker Hub拉取的镜像受到速率限制

从2020年11月1日开始，Docker Hub限制了匿名用户以及免费账户用户的下载速率，详细请参见[速率限制文档](<https://docs.docker.com/docker-hub/download-rate-limit/>)。 

匿名用户的速率限制通过IP进行跟踪，免费账户用户的速率限制通过账户进行跟踪。 

如果你需要更高的下载速率，你可以[注册付费计划](<https://www.docker.com/pricing>)或者将你需要的镜像拉取到不同的镜像仓库。你可以[自建镜像仓库](<https://docs.docker.com/registry/>)或者使用云托管的镜像站点，例如 [Amazon ECR](<https://aws.amazon.com/ecr/>), [Google Container Registry](<https://cloud.google.com/container-registry/>), [Azure Container Registry](<https://azure.microsoft.com/en-us/services/container-registry/>) 或 [Quay Container Registry](<https://quay.io/>)。 

使用Docker CLI 中的 `pull`, `tag` 以及 `push` 命令来镜像一个镜像。例如，将 [Nginx](<../zh-cn/Nginx.html> "Nginx") 标签(tag)为 `1.19.3` 的镜像镜像到托管于 `cr.example.com` 上的仓库: 
    
    $ docker pull nginx:1.19.3
    $ docker tag nginx:1.19.3 cr.example.com/nginx:1.19.3
    $ docker push cr.example.com/nginx:1.19.3
    
随后你可以从镜像仓库中拉取并运行镜像: 
    
    $ docker pull cr.example.com/nginx:1.19.3
    $ docker run cr.example.com/nginx:1.19.3
    
###  错误提示：iptables (旧版): 未知选项 "--dport"

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** [Nftables#与 Docker 一起工作](<../zh-cn/Nftables.html#%E4%B8%8E_Docker_%E4%B8%80%E8%B5%B7%E5%B7%A5%E4%BD%9C> "Nftables") 建议不要使用 [iptables-nft](<https://archlinux.org/packages/?name=iptables-nft>)包。（在 [Talk:Docker](<../zh-cn/Talk:Docker.html>) 中讨论）

如果你在运行容器时收到了这样的错误： `iptables (legacy): unknown option "--dport"`

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [iptables-nft](<https://archlinux.org/packages/?name=iptables-nft>)包 而不是 [iptables](<https://archlinux.org/packages/?name=iptables>)包 (旧版) 然后重启[[18]](<https://bbs.archlinux.org/viewtopic.php?id=256709>)。 

**注意：** 使用[iptables-nft](<https://archlinux.org/packages/?name=iptables-nft>)包可能会导致docker 混合 nftables 和 iptables 规则，详细参见[Nftables#与 Docker 一起工作](<../zh-cn/Nftables.html#%E4%B8%8E_Docker_%E4%B8%80%E8%B5%B7%E5%B7%A5%E4%BD%9C> "Nftables")。

###  运行docker login时提示"密码以非加密形式储存"

[默认情况下](<https://docs.docker.com/engine/reference/commandline/login/#credentials-store>) Docker 会尝试使用 `pass` 或者 `secretservice` 的二进制形式文件来储存你的注册表密码。如未能找到这些文件，注册表秘密将以明文形式(base64编码)储存在 `$HOME/.docker/config.json` ，并在登录成功后提示: 
    
    $ WARNING! Your password will be stored unencrypted in /home/_username_ /.docker/config.json.
    
如果你在使用支持 [Secret Service Freedesktop DBUS API](<https://specifications.freedesktop.org/secret-service-spec/latest/>) 的密码管理器,例如KDE的 [kwallet](<https://archlinux.org/packages/?name=kwallet>)包 或着 GNOME的 [gnome-keyring](<https://archlinux.org/packages/?name=gnome-keyring>)包，你可以安装 [docker-credential-secretservice](<https://aur.archlinux.org/packages/docker-credential-secretservice/>)AUR 来让你的注册表密码储存在密码管理器中。 

###  "无法在默认选项中找到可用的，不重叠的IPv4地址池进行分配"

如果你在使用大量的 Docker 项目 (例如使用 docker-compose)，可能会出现Docker容器的可用IP地址不足的情况： 
    
    Could not find an available, non-overlapping IPv4 address pool among the defaults to assign to the network
    
参见[这个 Docker issue](<https://github.com/docker/docs/issues/8663>), 默认选项是: 

Type | Default Size | Default Pool   
---|---|---  
local | /16 | 172.17.0.0/12   
local* | /20 | 192.168.0.0/16   
  
你可以在 `/etc/docker/daemon.json` 文件中修改 `default-address-pools` ，将其中第一个IP范围的值从16改为24解决这个问题。为了避免本地网络发生IP冲突，请不要修改第二个IP范围的值。 
    
    /etc/docker/daemon.json
    
    {
      ...
      "default-address-pools" : [
        {
          "base" : "172.17.0.0/12",
          "size" : 24
        },
        {
          "base" : "192.168.0.0/16",
          "size" : 24
        }
      ]
    }

重启 `docker.service` 以应用更改。 

更多详细信息和技术解释请参见文章: [Docker默认地址池选项的权威指南](<https://straz.to/2021-09-08-docker-address-pools/>)。 

###  Golang编译速度过慢

由于ulimit配置的原因，使用makepkg构建docker镜像以及其依赖时会非常缓慢（会在"Entering fakeroot environment..."处卡住）。 

这是因为[[19]](<https://github.com/moby/moby/issues/45436>) [[20]](<https://github.com/containerd/containerd/pull/7566>)，你可以尝试将 `--ulimit "nofile=1024:524288"` 添加到你的docker构建选项中来解决问题： 
    
    /etc/docker/daemon.json
    
    {
      "default-ulimits": {
        "nofile": {
          "Name": "nofile",
          "Soft": 1024,
          "Hard": 524288
        }
      }
    } 
    
##  另请参阅

  * [官方网站](<https://www.docker.com>)
  * [Arch Linux on docs.docker.com](<https://docs.docker.com/engine/installation/linux/archlinux/>)
  * [Docker 容器真的安全吗？](<https://opensource.com/business/14/7/docker-security-selinux>)——opensource.com
  * [Awesome Docker](<https://github.com/veggiemonk/awesome-docker>)
  * [为什么在 Docker 中运行特权容器是个坏主意](<https://www.trendmicro.com/en_us/research/19/l/why-running-a-privileged-container-in-docker-is-a-bad-idea.html>)
