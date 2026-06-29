**翻译状态：**

  * 本文（或部分内容）译自 [Podman](<https://wiki.archlinux.org/title/Podman> "arch:Podman")，最近一次同步于 2025-02-14，若英文版本有所[更改](<https://wiki.archlinux.org/title/Podman?diff=0&oldid=826954>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Podman_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [systemd-nspawn](<../zh-cn/Systemd-nspawn.html> "Systemd-nspawn")
  * [Linux Containers](<../zh-cn/Linux_Containers.html> "Linux Containers")
  * [Docker](<../zh-cn/Docker.html> "Docker")
  * [Buildah](</wzh/index.php?title=Buildah&action=edit&redlink=1> "Buildah（页面不存在）")
  * [Vagrant](</wzh/index.php?title=Vagrant&action=edit&redlink=1> "Vagrant（页面不存在）")

Podman 是 [Docker](<../zh-cn/Docker.html> "Docker") 的替代品，提供类似的接口。它支持无根容器和为 _docker-compose_ 提供的垫片服务。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") [podman](<https://archlinux.org/packages/?name=podman>)包 软件包。 

Podman 依赖 [netavark](<https://archlinux.org/packages/?name=netavark>)包 作为有根容器的默认网络后端（参见 [podman-network(1)](<https://man.archlinux.org/man/podman-network.1>)）。Netavark 依赖 [aardvark-dns](<https://archlinux.org/packages/?name=aardvark-dns>)包 实现同一网络中容器间的名称解析。对替代网络后端（CNI，[cni-plugins](<https://archlinux.org/packages/?name=cni-plugins>)包）的支持已弃用。 

若想替代 [Docker](<../zh-cn/Docker.html> "Docker")，可以安装 [podman-docker](<https://archlinux.org/packages/?name=podman-docker>)包 来模拟 docker 二进制文件及手册页。 

与 [Docker](<../zh-cn/Docker.html> "Docker") 不同，Podman 不需要守护进程，但可通过 [cockpit-podman](<https://archlinux.org/packages/?name=cockpit-podman>)包 为 [cockpit](</wzh/index.php?title=Cockpit&action=edit&redlink=1> "Cockpit（页面不存在）") 等服务提供 API。 

关于构建容器的高级用法，请参阅基于 [Buildah](</wzh/index.php?title=Buildah&action=edit&redlink=1> "Buildah（页面不存在）") 的 [podman-build(1)](<https://man.archlinux.org/man/podman-build.1>)。 

##  配置

容器行为配置文件位于 `/usr/share/containers/`。编辑前需将必要文件复制到 `/etc/containers`。要配置 Podman 使用的网络桥接接口，请参阅 `/etc/cni/net.d/87-podman.conflist`。 

###  镜像仓库

Arch Linux 默认未配置容器镜像仓库 [[1]](<https://github.com/containers/podman/issues/8896>)，这意味着类似 `podman search httpd` 这种未限定仓库的搜索命令将无法工作。要使 Podman 行为与 Docker 一致，需配置 [containers-registries.conf(5)](<https://man.archlinux.org/man/containers-registries.conf.5>)： 
    
    /etc/containers/registries.conf.d/10-unqualified-search-registries.conf
    
    unqualified-search-registries = ["docker.io"]

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 由 [containers-common](<https://archlinux.org/packages/?name=containers-common>)包 安装的列表位于 `/etc/containers/registries.conf.d/00-shortnames.conf`。（在 [Talk:Podman](<../zh-cn/Talk:Podman.html>) 中讨论）

**提示：** 为使未限定仓库的搜索对知名镜像更安全，可考虑将 <https://github.com/containers/shortnames> 的 [简称列表](<https://github.com/containers/shortnames/blob/main/shortnames.conf>) 集成到配置中，例如复制到 `/etc/containers/registries.conf.d/shortnames.conf`。

###  用户命名空间模式

默认情况下，Podman 容器中的进程在调用者的用户命名空间中运行，即容器未通过 [user_namespaces(7)](<https://man.archlinux.org/man/user_namespaces.7>) 功能隔离。这是 `--userns=host` 的行为，参见 [podman-run(1)](<https://man.archlinux.org/man/podman-run.1>)。 

`--userns=auto` 标志会自动为容器创建唯一的用户命名空间，使用未分配的 UID 和 GID 范围： 

  * 对于 root 启动的容器，`--userns=auto` 需要在 `/etc/subuid` 和 `/etc/subgid` 文件中指定 `containers` 用户并分配未使用的 ID 范围。例如：`containers:2147483647:2147483648`。
  * 对于其他用户启动的容器，将使用 `/etc/subuid` 和 `/etc/subgid` 中该用户的 ID 范围。参见 [#Rootless Podman](<#Rootless_Podman>) 了解必要配置。

`--userns` 标志还有其他有效值，详见 [podman-run(1)](<https://man.archlinux.org/man/podman-run.1>)。用户命名空间模式也可通过 [containers.conf(5)](<https://man.archlinux.org/man/containers.conf.5>) 在全局或用户级别配置。 

###  无根 Podman

**警告：** 无根 Podman 依赖非特权用户命名空间（`CONFIG_USER_NS_UNPRIVILEGED`），存在严重安全隐患，详见 [安全#沙盒程序](<../zh-cn/%E5%AE%89%E5%85%A8.html#Sandboxing_applications> "Security")。

默认只有 `root` 可运行容器（内核术语中的命名空间）。使用无根 Podman 可提升安全性（攻击者无法获得系统 root 权限），并允许多个非特权用户在同一机器上运行容器。另见 [podman(1) § Rootless mode](<https://man.archlinux.org/man/podman.1#Rootless_mode>) 和官方[无根教程](<https://github.com/containers/podman/blob/main/docs/tutorials/rootless_tutorial.md>)（可能已过时）。 

####  启用 kernel.unprivileged_userns_clone

首先检查 `kernel.unprivileged_userns_clone` 的值： 
    
    $ sysctl kernel.unprivileged_userns_clone
    
若当前值为 `0`，可通过 [sysctl](<../zh-cn/Sysctl.html> "Sysctl") 或[内核参数](<../zh-cn/Kernel_parameters.html> "Kernel parameters")设为 `1` 来启用。 

**注意：**[linux-hardened](<https://archlinux.org/packages/?name=linux-hardened>)包 默认将 `kernel.unprivileged_userns_clone` 设为 `0`。

####  设置 subuid 和 subgid

用户要运行无根 Podman，必须在 [subuid(5)](<https://man.archlinux.org/man/subuid.5>) 和 [subgid(5)](<https://man.archlinux.org/man/subgid.5>) 中为其创建配置条目。使用 [useradd(8)](<https://man.archlinux.org/man/useradd.8>) 创建的[新用户](<../zh-cn/Users_and_groups.html#%E7%94%A8%E6%88%B7%E7%AE%A1%E7%90%86> "Users and groups")默认已有这些条目。 

#####  为 shadow 4.11.1-3 之前版本创建的用户迁移

在 [shadow](<https://archlinux.org/packages/?name=shadow>)包 4.11.1-3 之前版本创建的用户默认没有 `/etc/subuid` 和 `/etc/subgid` 条目。可使用 [usermod(8)](<https://man.archlinux.org/man/usermod.8>) 命令或手动修改文件为其创建条目。 

以下命令允许 `_username_` 用户和组运行 Podman 容器（或其他类型容器），为其分配指定范围的 UID 和 GID： 
    
    # usermod --add-subuids 100000-165535 --add-subgids 100000-165535 _username_
    
上述范围可能已被系统首个用户的默认范围占用。如有疑问，请先查阅 `/etc/subuid` 和 `/etc/subgid` 文件确认已分配范围。 

**注意：** 许多镜像需要 65536 个 UID/GID 进行映射（特别是基础 _busybox_ 和 _alpine_ 镜像）。建议为每个用户至少分配该数量的 UID/GID 以保持与 Docker 的最大兼容性。

#####  为 homed 管理用户的变通方案

Homed 似乎不会为其用户分配 _gid_ 和 _uid_ 条目。可手动运行： 
    
    # usermod --add-subuids 524288-589823 --add-subgids 524288-589823 _username_
    
或直接以 root 身份编辑以下配置文件并添加： 
    
    /etc/subuid
    
    _username_ :524288:65536
    
    /etc/subgid
    
    _username_ :524288:65536

这将为 `_username_` 用户分配 `524288-589823` 的 UID/GID 范围。若范围已被其他用户占用，需相应调整。 

可能需要重启以应用更改。 

**注意：**

  * 此为临时方案，[Podman 未官方支持 homed](<https://github.com/containers/podman/issues/20040#issuecomment-1731335711>)。
  * 这是 _systemd-homed_ 的 [已知问题](<https://github.com/systemd/systemd/issues/29297>)。
  * 使用 Docker [似乎可行](<https://github.com/systemd/systemd/issues/29297#issuecomment-1823566012>)（将用户加入 `docker` 组，但有 [安全隐患](<https://docs.docker.com/engine/security/>)）。

#####  使 subuid 和 subgid 变更生效

无根 Podman 使用暂停进程保持非特权命名空间活动，这会阻止 `/etc/subuid` 和 `/etc/subgid` 的更改在暂停进程运行时生效。要使更改生效需运行： 
    
    $ podman system migrate
    
此后，上述文件中指定的用户/组即可启动和运行 Podman 容器。 

####  启用原生无根 overlay

过去需要使用 [fuse-overlayfs](<https://archlinux.org/packages/?name=fuse-overlayfs>)包 在无根环境中进行 [FUSE](<../zh-cn/FUSE.html> "FUSE") overlay 挂载。但现代 Podman 和 Linux 内核[支持](<https://www.redhat.com/sysadmin/podman-rootless-overlay>) _原生_ 无根 overlay，可获得更好性能。 

**注意：** 当使用修改后的 UID/GID 映射启动无根容器，且尚未用指定容器镜像和 UID/GID 映射创建过容器时， _原生 overlay_ 相比 _fuse-overlayfs_ 会有性能损失，因为必须更新磁盘上容器文件的所有 UID/GID。这对 `--userns auto` 尤其明显，因为每次调用可能使用不同的 UID/GID 映射。详情参见 [Podman 性能指南](<https://github.com/containers/podman/blob/main/docs/tutorials/performance.md#choosing-a-storage-driver>)。

要从 [fuse-overlayfs](<https://archlinux.org/packages/?name=fuse-overlayfs>)包 迁移，运行以下命令（会删除所有已拉取镜像）： 
    
    $ podman system reset
    
同时确保 Podman 使用 `overlay` 驱动且 [containers-storage.conf(5)](<https://man.archlinux.org/man/containers-storage.conf.5>) 中未定义 `mount_program` 参数。遵循 [Docker#启用本地覆盖差异引擎(native overlay diff engine)](<../zh-cn/Docker.html#%E5%90%AF%E7%94%A8%E6%9C%AC%E5%9C%B0%E8%A6%86%E7%9B%96%E5%B7%AE%E5%BC%82%E5%BC%95%E6%93%8E\(native_overlay_diff_engine\)> "Docker") 的说明。 

验证原生无根 overlay 是否启用： 
    
    $ podman info | grep -i overlay
    
应显示 `graphDriverName: overlay` 和 `Native Overlay Diff: "true"`。 

####  网络

Podman 依赖 [passt](<https://archlinux.org/packages/?name=passt>)包，其提供的 [pasta](<https://passt.top/passt/about/#pasta>) 是默认的无根网络后端。 

另一种无根网络后端是 [slirp4netns](<https://archlinux.org/packages/?name=slirp4netns>)包，在 Podman 5 之前是默认选项。 

两者主要区别在 [Podman 5.0 重大变更](<https://blog.podman.io/2024/03/podman-5-0-breaking-changes-in-detail/#:~:text=Pasta%20by%20default%20performs%20no%20Network%20Address%20Translation%20\(NAT\)%20and%20copies%20the%20ip%20addresses%20from%20your%20main%20interface%20into%20the%20container%20namespace.>)中概述： 

    _Pasta 默认不进行网络地址转换（NAT），而是将主接口的 IP 地址复制到容器命名空间。_

上游的[无根 Podman 缺陷](<https://github.com/containers/podman/blob/main/rootless.md>)解释了此变更的影响： 

    _由于 pasta 复制主接口 IP 地址，容器无法通过该 IP 连接宿主机。这意味着除非有多个接口，否则必须显式传递 pasta 网络配置（通过`containers.conf` 或运行时参数）才能实现容器间连接。_

**提示：** 容器到宿主的通信问题已在 Podman 5.3 [修复](<https://blog.podman.io/2024/10/podman-5-3-changes-for-improved-networking-experience-with-pasta/>)。

在 ["Podman 5.0 重大变更"](<https://blog.podman.io/2024/03/podman-5-0-breaking-changes-in-detail/>) 博客中给出了模拟 slirp4netns 行为的示例： 
    
    containers.conf
    
    [network]
    pasta_options = ["-a", "10.0.2.0", "-n", "24", "-g", "10.0.2.2", "--dns-forward", "10.0.2.3"]

此外，可在 `containers.conf` 的 `[network]` 部分通过 `default_rootless_network_cmd` 选择默认无根网络工具，可设为 `pasta` 或 `slirp4netns`。因此遇到问题时，可回退到 slirp4netns（需已安装）： 
    
    containers.conf
    
    [network]
    default_rootless_network_cmd = "slirp4netns"

###  存储

容器镜像和实例的存储配置位于 `/etc/containers/storage.conf`。 

**注意：** 使用 [无根 Podman](<#Rootless_Podman>) 时，可在 `$XDG_CONFIG_HOME/containers/storage.conf` 中按用户覆盖存储设置。

默认的 `overlay` 驱动经过充分测试，支持在具备该功能的文件系统（[Btrfs](<../zh-cn/Btrfs.html> "Btrfs")、[XFS](<../zh-cn/XFS.html> "XFS")、[ZFS](<../zh-cn/ZFS.html> "ZFS") 等）上使用 reflink 复制 [[2]](<https://github.com/containers/podman/issues/6563#issuecomment-659085291>) [[3]](<https://github.com/containers/podman/blob/main/docs/tutorials/performance.md#choosing-a-host-file-system>)。 

有关可用选项和其他配置的详细信息，请参阅 [containers-storage.conf(5) § STORAGE_TABLE](<https://man.archlinux.org/man/containers-storage.conf.5#STORAGE_TABLE>)。 

###  外部架构

Podman 可通过 [Wikipedia:binfmt_misc](<https://en.wikipedia.org/wiki/binfmt_misc> "wikipedia:binfmt misc") 系统运行与宿主机不同 CPU 架构的镜像。 

安装 [qemu-user-static](<https://archlinux.org/packages/?name=qemu-user-static>)包 和 [qemu-user-static-binfmt](<https://archlinux.org/packages/?name=qemu-user-static-binfmt>)包 以启用该功能。 

[systemd](<../zh-cn/Systemd.html> "Systemd") 提供 `systemd-binfmt.service` 服务来启用新规则。 

验证 binfmt 规则是否已添加： 
    
    $ ls /proc/sys/fs/binfmt_misc
    
    DOSWin        qemu-cris        qemu-ppc      qemu-sh4eb        status
    qemu-aarch64  qemu-m68k        qemu-ppc64    qemu-sparc        
    qemu-alpha    qemu-microblaze  qemu-riscv64  qemu-sparc32plus  
    qemu-arm      qemu-mips        qemu-s390x    qemu-sparc64      
    qemu-armeb    qemu-mipsel      qemu-sh4      register
    
现在 Podman 应能运行外部架构镜像。大多数命令通过 `--arch` 选项指定架构。 

示例： 
    
    # podman run --arch arm64 'docker.io/alpine:latest' arch
    
    aarch64
    
### Docker Compose

Podman 的 _compose_ 子命令是 compose 提供器的薄封装层，支持 [docker-compose](<https://archlinux.org/packages/?name=docker-compose>)包 或 [podman-compose](<https://archlinux.org/packages/?name=podman-compose>)包。若两者都安装，优先使用 _docker-compose_ 。可通过 `PODMAN_COMPOSE_PROVIDER` 环境变量覆盖此行为。 

若使用 _docker-compose_ ，需为当前用户[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") `podman.socket` [用户单元](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "Systemd/User")并设置 docker socket 环境变量： 
    
    $ export DOCKER_HOST=unix://$XDG_RUNTIME_DIR/podman/podman.sock
    
使用 _podman-compose_ 时无需此操作，因其直接调用 _podman_ 。 

**注意：**

  * 若在 docker 中启用了 buildkit，集成将无法工作。需通过设置 `DOCKER_BUILDKIT=0` [环境变量](<../zh-cn/Environment_variables.html> "Environment variables") 禁用 buildkit。
  * [podman-compose](<https://archlinux.org/packages/?name=podman-compose>)包 存在兼容性问题，例如 [环境变量传递行为与 docker-compose 不一致](<https://github.com/containers/podman-compose/issues/491>)。

### NVIDIA GPU

[NVIDIA Container Toolkit](<https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#podman>) 为 NVIDIA GPU 提供容器运行时。安装 [nvidia-container-toolkit](<https://archlinux.org/packages/?name=nvidia-container-toolkit>)包 软件包，其包含的 [pacman hook](<../zh-cn/Pacman_hook.html> "Pacman hook") 会生成 GPU 的 CDI 规范并保存至 `/etc/cdi/nvidia.yaml`。 

测试配置： 
    
    $ podman run --rm --gpus all archlinux nvidia-smi -L
    
**注意：** NVIDIA CDI hook 无法与 `--userns nomap` 和 `--userns auto` podman run 参数共同使用 [[4]](<https://github.com/NVIDIA/nvidia-container-toolkit/issues/648>)。

###  带重启策略的容器

要自动启动带重启策略的容器，请[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") `podman-restart.service`。 

## Quadlet

[Quadlet](<https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html>) 允许通过 [systemd](<../zh-cn/Systemd.html> "Systemd") 管理 Podman 容器。 

对于无根(rootless) Podman，将 Quadlet 文件放置于以下目录之一： 

  * `$XDG_CONFIG_HOME/containers/systemd/` 或 `~/.config/containers/systemd/`
  * `/etc/containers/systemd/users/_UID_` 对应指定 `_UID_` 的用户
  * `/etc/containers/systemd/users/` 适用于所有用户

对于有根(rootful) Podman，目录为 `/etc/containers/systemd/`。 

Podman 会读取扩展名为 _.container_ 、 _.volume_ 、 _.network_ 、 _.kube_ 、 _.image_ 和 _.pod_ 的 Quadlet 文件，并通过 [systemd.generator(7)](<https://man.archlinux.org/man/systemd.generator.7>) 生成对应的 _.service_ 文件。Quadlet 文件会在系统启动时读取，或通过运行 [daemon-reload](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Daemon-reload") 手动加载。 

您也可以使用 [podlet](<https://aur.archlinux.org/packages/podlet/>)AUR 从 Podman 命令生成 Quadlet 文件。 

例如，以下命令用于运行 LinuxServer.io 的 [Syncthing](</wzh/index.php?title=Syncthing&action=edit&redlink=1> "Syncthing（页面不存在）") 容器： 
    
    $ podman run \
        --rm \
        --replace \
        --label io.containers.autoupdate=registry \
        --name syncthing \
        --hostname=syncthing \
        --uidmap 1000:0:1 \
        --uidmap 0:1:1000 \
        --uidmap 1001:1001:64536 \
        --env PUID=1000 \
        --env PGID=1000 \
        --env TZ=Etc/UTC \
        --publish 127.0.0.1:8384:8384/tcp \
        --publish 22000:22000/tcp \
        --volume /path/to/syncthing/config:/config \
        --volume /path/to/data1:/data1 \
        lscr.io/linuxserver/syncthing:latest
    
要将其作为 systemd 服务管理，创建以下 Quadlet 文件： 
    
    ~/.config/containers/systemd/syncthing-lsio.container
    
    [Unit]
    Description=Syncthing 容器
    
    # 容器之间可以使用 systemd 依赖项进行关联，但需添加 ".service" 后缀。
    # 例如：若要让另一个容器等待本容器启动，可在其 [Unit] 部分添加 "After=syncthing-lsio.service"
    
    [Container]
    ContainerName=syncthing
    Image=lscr.io/linuxserver/syncthing:latest
    
    # 启用容器自动更新
    AutoUpdate=registry
    
    Volume=/path/to/syncthing/config:/config
    Volume=/path/to/data1:/data1
    
    HostName=syncthing
    PublishPort=127.0.0.1:8384:8384/tcp
    PublishPort=22000:22000/tcp
    
    Environment=PUID=1000
    Environment=PGID=1000
    Environment=TZ=Etc/UTC
    
    # UID 映射是运行 linuxserver.io 无根容器所必需的。
    # 这会将容器内的 _UID=1000_ 映射到中间 _UID=0_ 。
    # 对于无根 Podman，中间 _UID=0_ 将被映射到当前用户的 UID。
    UIDMap=1000:0:1
    UIDMap=0:1:1000
    UIDMap=1001:1001:64536
    
    [Service]
    Restart=on-failure
    
    # 延长超时时间以允许拉取镜像
    TimeoutStartSec=300
    
    # [Install] 部分用于启用生成的服务
    [Install]
    WantedBy=default.target

可通过以下命令验证 Quadlet 文件： 
    
    $ /usr/lib/podman/quadlet -dryrun -user

然后 [reload](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Reload") 并[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start")`syncthing-lsio.service`。 

**注意：**

若无根容器未按预期在启动时运行，请检查 `podman-user-wait-network-online.service` 的状态。若因超时失败，可能是由于缺少激活 `network-online.target` 的服务，此时可[create](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Create")、[reload](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Reload") 并 [enable](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") 一个虚拟服务解决。参考 [[5]](<https://github.com/containers/podman/issues/24796#issuecomment-2527822425>) 和 [[6]](<https://github.com/containers/podman/issues/22197#issuecomment-2078104063>)。 
    
    /etc/systemd/system/podman-network-online-dummy.service
    
    [Unit]
    Description=此服务仅用于激活 network-online.target
    After=network-online.target
    Wants=network-online.target
    
    [Service]
    ExecStart=/usr/bin/echo 激活 network-online.target 中...
    
    [Install]
    WantedBy=default.target

参阅 [Systemd/User#Automatic_start-up_of_systemd_user_instances](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html#Automatic_start-up_of_systemd_user_instances> "Systemd/User") 了解如何在没有开放会话时启动无根容器。

`Container` 部分的可用选项列于 [podman-systemd.unit(5) § Container units [Container]](<https://man.archlinux.org/man/podman-systemd.unit.5#Container_units_%5BContainer%5D>)。`PodmanArgs=` 可用于添加没有对应文件选项的其他 Podman 参数。 

更多示例（包括 `Pod`、`Volume`、`Network` 和 `Image` 单元）请参阅 [podman-systemd.unit(5) § EXAMPLES](<https://man.archlinux.org/man/podman-systemd.unit.5#EXAMPLES>)。 

##  镜像

**注意：** 可以省略镜像的注册表前缀，因为 Podman 会自动在 `/etc/containers/registries.conf` 中 `unqualified-search-registries` 列出的所有注册表中按顺序搜索镜像。以下示例将始终包含前缀，以兼容未配置 `docker.io` 的情况。

### Arch Linux

以下命令从 [Docker Hub](<https://hub.docker.com/>) 拉取 [Arch Linux](<https://hub.docker.com/_/archlinux/>) x86_64 镜像： 
    
    # podman pull docker.io/archlinux
    
完整可用标签列表（包含带/不带构建工具的版本）请参阅 Docker Hub 页面。 

另见 [README.md](<https://gitlab.archlinux.org/archlinux/archlinux-docker/blob/master/README.md>)。 

### Alpine Linux

[Alpine Linux](<https://www.alpinelinux.org/>) 是小型容器镜像的热门选择，尤其适合静态编译的软件。以下命令从 [Docker Hub](<https://hub.docker.com/>) 拉取最新 Alpine Linux 镜像： 
    
    # podman pull docker.io/alpine
    
Alpine Linux 使用 [musl](<https://musl.libc.org/>) 作为 C 库实现，而非大多数 Linux 发行版使用的 [glibc](<https://www.gnu.org/software/libc/>)。由于 Arch Linux 使用 glibc，宿主机与 Alpine Linux 容器间存在许多功能差异，可能影响软件性能和正确性。这些差异列于 <https://wiki.musl-libc.org/functional-differences-from-glibc.html>。 

注意：在 Arch Linux（或其他 glibc 系统）上构建的动态链接软件在 Alpine Linux（或其他不同 C 库系统）上运行时可能出现错误和性能问题。示例参见 [[7]](<https://bugs.python.org/issue32307>)、[[8]](<https://superuser.com/questions/1219609/why-is-the-alpine-docker-image-over-50-slower-than-the-ubuntu-image>) 和 [[9]](<https://pythonspeed.com/articles/alpine-docker-python>)。 

### CentOS

以下命令从 [Docker Hub](<https://hub.docker.com/>) 拉取最新 [CentOS](<https://hub.docker.com/_/centos>) 镜像： 
    
    # podman pull docker.io/centos
    
各 CentOS 版本的完整标签列表请参阅 Docker Hub 页面。 

### Debian

以下命令从 [Docker Hub](<https://hub.docker.com/>) 拉取最新 [Debian](<https://hub.docker.com/_/debian>) 镜像： 
    
    # podman pull docker.io/debian
    
各 Debian 版本的标准版和精简版标签列表请参阅 Docker Hub 页面。 

##  故障排除

###  为进程添加暂停
    
    WARN[0000] Failed to add pause process to systemd sandbox cgroup: Process org.freedesktop.systemd1 exited with status 1 
    
可通过以下方式解决：<https://github.com/containers/crun/issues/704>
    
    # echo +cpu +cpuset +io +memory +pids > /sys/fs/cgroup/cgroup.subtree_control
    
###  容器在 Shell 退出后终止

部分用户在注销后 Podman 容器会停止。要避免此问题，请为运行容器的用户[启用 lingering](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html#%E9%9A%8F%E7%B3%BB%E7%BB%9F%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8_systemd_%E7%94%A8%E6%88%B7%E5%AE%9E%E4%BE%8B> "Systemd/User")。 

也可按 [podman-auto-update(1) § EXAMPLES](<https://man.archlinux.org/man/podman-auto-update.1#EXAMPLES>) 创建用户 systemd 单元。 

###  无根模式提交时报错
    
    Error committing the finished image: error adding layer with blob "sha256:02823fca9b5444c196f1f406aa235213254af9909fca270f462e32793e2260d8": Error processing tar file(exit status 1) permitted operation
    
检查[存储配置](<#%E5%AD%98%E5%82%A8>)中存储驱动是否为 overlay。 

###  在无根模式下使用桥接网络创建容器时报错

[![](../File:Tango-view-refresh-red.png)](<../File:Tango-view-refresh-red.png>)**本文或本节内容已经过时。**

**原因：** CNI 网络后端已弃用。Netavark 后端是否存在此问题？ (在[Talk:Podman](<../zh-cn/Talk:Podman.html>)讨论)

若使用 [AppArmor](<../zh-cn/AppArmor.html> "AppArmor")，在启用 `dnsname` 插件的情况下创建桥接网络容器时可能遇到问题： 
    
    $ podman network create foo
    
    /home/_用户_ /.config/cni/net.d/foo.conflist
    
    $ podman run --rm -it --network=foo docker.io/library/alpine:latest ip addr
    
    Error: command rootless-cni-infra [alloc 89398a9315256cb1938075c377275d29c2b6ebdd75a96b5c26051a89541eb928 foo festive_hofstadter    ] in container 1f4344bbd1087c892a18bacc35f4fdafbb61106c146952426488bc940a751efe failed with status 1, stdout="", stderr="exit status 3\n"

解决方法是在 `/etc/apparmor.d/local/usr.sbin.dnsmasq` 中添加： 
    
    owner /run/user/[0-9]*/containers/cni/dnsname/*/dnsmasq.conf r,
    owner /run/user/[0-9]*/containers/cni/dnsname/*/addnhosts r,
    owner /run/user/[0-9]*/containers/cni/dnsname/*/pidfile rw,
    
然后重新加载 AppArmor 配置： 
    
    # apparmor_parser -R /etc/apparmor.d/usr.sbin.dnsmasq
    # apparmor_parser /etc/apparmor.d/usr.sbin.dnsmasq
    
###  找不到镜像

[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[#Registries](<#Registries>)。**

**附注：** 相关内容应合并至配置章节。（在 [Talk:Podman](<../zh-cn/Talk:Podman.html>) 中讨论）

默认情况下注册表列表未填充（包内文件来自上游）。这意味着若未指定注册表，尝试拉取任何镜像都会出现如下错误： 
    
    Error: short-name "archlinux" did not resolve to an alias and no unqualified-search registries are defined in "/etc/containers/registries.conf"
    
初始配置示例： 
    
    /etc/containers/registries.conf.d/00-unqualified-search-registries.conf
    
    unqualified-search-registries = ["docker.io"]
    
    /etc/containers/registries.conf.d/01-registries.conf
    
    [[registry]]
    location = "docker.io"
    
此配置等价于 Docker 的默认设置。 

另一种兼容性更高但不太便捷的方式是在 `Containerfile` 或 `Dockerfile` 中使用完整注册表路径： 
    
    Containerfile
    
    FROM docker.io/archlinux/archlinux
    
###  权限被拒绝: OCI permission denied
    
    $ podman exec openvas_openvas_1 bash
    
    Error: crun: writing file `/sys/fs/cgroup/user.slice/user-1000.slice/user@1000.service/user.slice/libpod-b3e8048a9b91e43c214b4d850ac7132155a684d6502e12e22ceb6f73848d117a.scope/container/cgroup.procs`: Permission denied: OCI permission denied
    
解决方法见 [BBS#253966](<https://bbs.archlinux.org/viewtopic.php?id=253966>)： 
    
    $ env DBUS_SESSION_BUS_ADDRESS= podman ...
    $ env DBUS_SESSION_BUS_ADDRESS= podman-compose ...
    
###  推送镜像至 Docker Hub: 访问被拒/需身份验证

使用 `podman push` 推送镜像至 Docker Hub 时可能遇到 `Requested access to the resource is denied` 或 `Authentication required` 错误。以下提示可能有助解决： 

  * 标记本地镜像：
        
        # podman tag <本地镜像> docker.io/<DockerHub用户名>/<DockerHub仓库>:<标签>

  * 推送标记的镜像：
        
        # podman push docker.io/<DockerHub用户名>/<DockerHub仓库>:<标签> docker://docker.io/<DockerHub用户名>/<DockerHub仓库>:<标签>

  * 登录相关服务：

    # podman login -u <DockerHub用户名> -p <DockerHub密码> registry-1.docker.io
    # podman login -u <DockerHub用户名> -p <DockerHub密码> docker.io/<DockerHub用户名>/<DockerHub仓库>
    # podman login -u <DockerHub用户名> -p <DockerHub密码> docker.io
    
  * 登录前先登出所有注册表：
        
        # podman logout --all

  * 在 Docker Hub 仓库的 Collaborators 标签页添加 `<DockerHub用户名>` 为协作者

###  WARN[0000] "/" is not a shared mount, this could cause issues or missing mounts with rootless containers

无根 Buildah/Podman 要求绑定挂载为共享模式，检查是否设置为私有： 
    
    $ findmnt -o PROPAGATION /
    
    PROPAGATION
    private
    
若如此，参考 [mount(8) § Shared_subtree_operations](<https://man.archlinux.org/man/mount.8#Shared_subtree_operations>) 并**临时** 设为共享： 
    
    # mount --make-shared /
    
要**永久** 生效，请编辑 [/etc/fstab](<../zh-cn/Fstab.html#Usage> "Fstab") 并为对应挂载点添加 _shared_ 选项后重启。示例条目： 
    
    /etc/fstab
    
    # <设备>                                <目录> <类型> <选项> <dump> <fsck>
    UUID=0a3407de-014b-458b-b5c1-848e92a327a3 /     ext4   defaults,shared   0      1

###  容器内网络问题

####  IP 网络

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 此段关于防火墙影响的描述过于冗长。Netavark 使用 iptables 自动创建防火墙规则，因此 iptables 链的默认 `DROP` 策略不会造成问题。（在 [Talk:Podman](<../zh-cn/Talk:Podman.html>) 中讨论）

Podman 容器默认通过虚拟网络接口桥接到主机。 

例如容器内的虚拟接口 `eth0@if6` 拥有 IP 10.89.0.3（具体 IP 可能不同）： 
    
    容器内# ip addr
    
    ...
    2: eth0@if6: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
        ...
        inet 10.89.0.3/24 brd 10.89.0.255 scope global eth0
           valid_lft forever preferred_lft forever
    
主机上，容器的数据包通过虚拟接口（此处为 `podman1`，路由 IP 10.89.0.1）传出： 
    
    宿主机# ip addr
    
    ...
    4: podman1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
        ...
        inet 10.89.0.1/24 brd 10.89.0.255 scope global podman1
    
尽管使用虚拟 IP，数据包仍需经过内核的包过滤系统，可能被 iptables/nftables 规则拦截。特别是 iptables 过滤链中的默认 `DROP` 策略和运行的防火墙（[ufw](<../zh-cn/Uncomplicated_Firewall.html> "Ufw")、[firewalld](<../zh-cn/Firewalld.html> "Firewalld")）可能影响容器。若怀疑此类问题，请检查配置（如使用 `iptables -L -n -v` 或 `nft list ruleset`）。 

修改 `docker-compose.yml` 后，注意使用 `podman compose down` 销毁环境时，`networks:` 部分创建的网络可能不会被删除。如需删除，请使用 `podman network ls` 和 `podman network rm` 手动操作。 

####  DNS 与名称解析

名称解析由 Podman 子系统（如 [aardvark-dns](<https://archlinux.org/packages/?name=aardvark-dns>)包）处理，既提供外部 DNS（通常通过宿主的 DNS 解析器）也支持容器间名称解析（例如 `webserver.dns.podman` 访问 `database.dns.podman`）。 

上例中，容器通过 `/etc/resolv.conf` 被自动配置为向宿主侧端口 53 发送 DNS 请求： 
    
    容器内# cat /etc/resolv.conf
    
    search dns.podman
    nameserver 10.89.0.1
    
检查宿主是否运行其他占用 53 端口的 DNS 解析器（如 [Systemd-resolved](<../zh-cn/Systemd-resolved.html> "Systemd-resolved") 或 [Unbound](<../zh-cn/Unbound.html> "Unbound")），这可能会干扰 Podman 名称解析。若有此情况，可将 Podman 在宿主上的监听端口更改为其他可用端口，Podman 会自动转发容器请求： 
    
    宿主# # cat /etc/containers/containers.conf
    
    ...
    dns_bind_port = 20053
    
###  内核不支持 overlay 文件系统：'overlay' 不支持在 <文件系统> 上使用

请按照[常规故障排除#内核升级后部分外设无法使用](<../zh-cn/%E5%B8%B8%E8%A7%84%E6%95%85%E9%9A%9C%E6%8E%92%E9%99%A4.html#%E5%86%85%E6%A0%B8%E5%8D%87%E7%BA%A7%E5%90%8E%E9%83%A8%E5%88%86%E5%A4%96%E8%AE%BE%E6%97%A0%E6%B3%95%E4%BD%BF%E7%94%A8> "常规故障排除")中的说明重启系统。 

##  另请参阅

  * [官方网站](<https://podman.io/>)
  * [Podman 教程](<https://github.com/containers/podman/blob/main/docs/tutorials/README.md>)
  * [Podman 与 Docker 对比：你需要知道的一切](<https://phoenixnap.com/kb/podman-vs-docker>)
