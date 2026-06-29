**翻译状态：**

  * 本文（或部分内容）译自 [Systemd-nspawn](<https://wiki.archlinux.org/title/Systemd-nspawn> "arch:Systemd-nspawn")，最近一次同步于 2024-12-18，若英文版本有所[更改](<https://wiki.archlinux.org/title/Systemd-nspawn?diff=0&oldid=822986>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Systemd-nspawn_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Linux Containers](<../zh-cn/Linux_Containers.html> "Linux Containers")
  * [systemd](<../zh-cn/Systemd.html> "Systemd")
  * [systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd")
  * [Docker](<../zh-cn/Docker.html> "Docker")

**systemd-nspawn** 跟 [chroot](<../zh-cn/Chroot.html> "Chroot") 命令类似，是个终极版的 chroot。 

systemd-nspawn 可以在轻量的命名空间容器中运行命令或系统。它比 [chroot](<../zh-cn/Chroot.html> "Chroot") 强大的地方是，它完全虚拟了文件系统层次结构、进程树、各种 IPC 子系统以及主机名。 

systemd-nspawn 将容器中各种内核接口的访问限制为只读，像是 `/sys`, `/proc/sys` 和 `/sys/fs/selinux`。网络接口和系统时钟不能从容器内更改，不能创建设备节点。不能从容器中重启宿主机，也不能加载内核模块。 

相比 [LXC](<../zh-cn/Linux_%E5%AE%B9%E5%99%A8.html> "LXC") 或 [Libvirt](<../zh-cn/Libvirt.html> "Libvirt")， systemd-nspawn 更容易配置。 

##  安装

systemd-nspawn 是 [systemd](<../zh-cn/Systemd.html> "Systemd") 的一部分并被打进 [systemd](<https://archlinux.org/packages/?name=systemd>)包 软件包中。 

##  用例

###  创建并启动一个最小的 Arch Linux 容器

首先创建一个目录来保存容器。在这个示例中我们将使用 `~/MyContainer`. 

接下来，我们使用 [arch-install-scripts](<https://archlinux.org/packages/?name=arch-install-scripts>)包 中的 _pacstrap_ 在容器中安装一个基本的Arch系统。其中至少需要安装包组 [base](<https://archlinux.org/packages/?name=base>)包。 
    
    # pacstrap -K -c ~/MyContainer base _[additional packages/groups]_
    
**提示：**[base](<https://archlinux.org/packages/?name=base>)包 已经不再依赖内核包 [linux](<https://archlinux.org/packages/?name=linux>)包，这已为容器化做好准备。

**注意：** 如果是从一个 _pacstrap_ 不可用的操作系统中创建，可以使用如下方法替代容器镜像 [从现有_Linux_发行版安装_Arch_Linux#方法一：使用_Bootstrap_镜像（推荐）](<../zh-cn/%E4%BB%8E%E7%8E%B0%E6%9C%89_Linux_%E5%8F%91%E8%A1%8C%E7%89%88%E5%AE%89%E8%A3%85_Arch_Linux.html#%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9A%E4%BD%BF%E7%94%A8_Bootstrap_%E9%95%9C%E5%83%8F%EF%BC%88%E6%8E%A8%E8%8D%90%EF%BC%89> "从现有 Linux 发行版安装 Arch Linux")。pacman 密钥环需要在容器中进行初始化，参阅 [从现有_Linux_发行版安装_Arch_Linux#初始化_pacman_密匙环](<../zh-cn/%E4%BB%8E%E7%8E%B0%E6%9C%89_Linux_%E5%8F%91%E8%A1%8C%E7%89%88%E5%AE%89%E8%A3%85_Arch_Linux.html#%E5%88%9D%E5%A7%8B%E5%8C%96_pacman_%E5%AF%86%E5%8C%99%E7%8E%AF> "从现有 Linux 发行版安装 Arch Linux")。

一旦安装完成后，进入容器中并设置root密码： 
    
    # systemd-nspawn -D ~/MyContainer
    # passwd
    # logout
    
**提示：** 设置根密码是可选的。你可以运行 `machinectl shell root@MyContainer` 直接获取一个 root shell ，并不需要登录。

最后, 启动容器: 
    
    # systemd-nspawn -b -D ~/MyContainer
    
参数 `-b` 将会启动这个容器（比如：以 PID=1 运行 `systemd`）, 而不是仅仅启动一个 shell, 而参数 `-D` 指定成为容器根目录的目录。 

容器启动后，输入密码以"root"身份登录。 

**注意：** 如果登录失败显示 "Login incorrect", 问题可能是 `securetty` TTY 设备白名单导致的。 请查看[#Root登录失败](<#Root%E7%99%BB%E5%BD%95%E5%A4%B1%E8%B4%A5>)。

可以在容器内运行 `poweroff` 来关闭容器。在主机端，容器可以通过 [machinectl](<#machinectl>) 工具进行控制。 

**注意：** 要从容器内终止 _session_ ，请按住 `Ctrl` 并快速地按 `]` 三下。

###  创建 Debian 或 Ubuntu 环境

安装 [debootstrap](<https://archlinux.org/packages/?name=debootstrap>)包 以及 [debian-archive-keyring](<https://archlinux.org/packages/?name=debian-archive-keyring>)包 或 [ubuntu-keyring](<https://archlinux.org/packages/?name=ubuntu-keyring>)包 中的一个或两个（当然要安装你想要的发行版的keyring）。 

然后通过以下结构式调用 _deboostrap_ ： 
    
    # debootstrap _codename_ _container-name_ _repository-url_
    
  * _codename_ ：对于 Debian，有效的代码名称要不然是稳定性别名如 `stable`、`testing` 或 `unstable`，要不然就是版本名称如 `bookworm` 或 `sid`。你可以从这里获取名称列表：[[1]](<https://www.debian.org/releases/>)。对于 Ubuntu：只有像是 `jammy` 或 `noble` 这样的名称应该被使用而不是版本号。你可以从 [[2]](<https://wiki.ubuntu.com/Releases>) 或者 [[3]](<https://wiki.ubuntu.com/DevelopmentCodeNames#Release_Naming_Scheme>) 获取一份代码名称与版本号的对应表格。

  * _container-name_ 是会包含操作系统文件树的目录，如果它不存在的话将会被创建。

  * _repository-url_ ：下载操作系统文件树的镜像地址。目前 Debian 发布在任何[有效镜像站](<https://www.debian.org/mirror/list>)，比如说 CDN 支持的 <https://deb.debian.org/debian> 。 Ubuntu 的镜像站在 [[4]](<https://launchpad.net/ubuntu/+archivemirrors>)，比如说 <https://archive.ubuntu.com/ubuntu> 。

**注意：**

  * 如果你需要一个以归档的 Debian 版本（指的是任何在2024年8月，Debian 10/Buster 之前的版本），请使用一个特殊的 [debian-archive](<https://www.debian.org/distrib/archive>) 镜像地址：<https://archive.debian.org/debian/> 。Ubuntu 应该使用 <https://old-releases.ubuntu.com/ubuntu/> 。
  * _systemd-nspawn_ 要求容器中的操作系统使用 _systemd_ 作为其 init 程序（以 PID 1 运行）。从 Debian 8 （“jessie”） [[5]](<https://wiki.debian.org/systemd#Introduction>) 以及 Ubuntu 15.04 （“vivid”）[[6]](<https://wiki.ubuntu.com/SystemdForUpstartUsers#Support_status>) 之后，这是两者的默认 init 程序。但请注意，对于不包含在上述密钥包中的版本，会出现与 “未知签名密钥（unknown signing key）”相关的问题，比如任何早于 Debian 9 （“Stretch”）[[7]](<https://ftp-master.debian.org/keys.html#archivekey>) 的发行版本。这使得后者成为成为无需额外操作即可安装的最老版本。

与 Arch 相同，Debian 和 Ubuntu 不会让您在首次登录时无密码登录。为了设置root密码登录，要不使用"-b"参数并设置密码： 
    
    # cd /var/lib/machines
    # systemd-nspawn -D ./_container-name_
    # passwd
    # logout
    
**提示：** 如果计划使用 [#machinectl](<#machinectl>) 管理容器，请确保使用合适的包名在目标操作系统容器中安装 [dbus](<../zh-cn/D-Bus.html> "Dbus") 包，否则容器将不会工作。可以安装 `systemd-container` 时使用 `--include=` 选项，这始终是 dbus 和 systemd 的依赖项： 
    
    # debootstrap --include=systemd-container _codename_ /var/lib/machines/_container-name_ _repository-url_

### Create a Fedora or AlmaLinux environment

Install [dnf](<https://archlinux.org/packages/?name=dnf>)包, and edit the `/etc/dnf/dnf.conf` file to add the required Fedora repositories. 
    
    /etc/dnf/dnf.conf
    
    [fedora]                                                                                            
    name=Fedora $releasever - $basearch
    metalink=https://mirrors.fedoraproject.org/metalink?repo=fedora-$releasever&arch=$basearch
    gpgkey=https://getfedora.org/static/fedora.gpg
    
    [updates]                                                                                           
    name=Fedora $releasever - $basearch - Updates
    metalink=https://mirrors.fedoraproject.org/metalink?repo=updates-released-f$releasever&arch=$basearch
    gpgkey=https://getfedora.org/static/fedora.gpg

The _fedora.gpg_ file contain the gpg keys for the latest Fedora releases <https://getfedora.org/security/>. To set up a minimal Fedora 37 container: 
    
    # mkdir /var/lib/machines/_container-name_
    # dnf --releasever=37 --best --setopt=install_weak_deps=False --repo=fedora --repo=updates --installroot=/var/lib/machines/_container-name_ install dhcp-client dnf fedora-release glibc glibc-langpack-en iputils less ncurses passwd systemd systemd-networkd systemd-resolved util-linux vim-default-editor
    
**注意：** If you want to install a different Fedora release, keep in mind that different releases will have distinct [package requirements](<https://docs.fedoraproject.org/en-US/fedora-server/containerization/systemd-nspawn-setup/#_2_1_creating_a_container_directory_tree>). 

If you are using btrfs filesystem create a subvolume instead of creating a directory. 

An Enterprise Linux derivative like AlmaLinux has three repositories enabled by default, _BaseOS_ wich contains a core set that provides the basis for all installations, _AppStream_ that includes additional applications, language packages, etc and _Extras_ that contains packages not included in RHEL. So for a minimal container we only need to add the BaseOS repository to `/etc/dnf/dnf.conf`
    
    /etc/dnf/dnf.conf
    
    [baseos]                                                                                            
    name=AlmaLinux $releasever - BaseOS                                          
    mirrorlist=https://mirrors.almalinux.org/mirrorlist/$releasever/baseos       
    gpgkey=https://repo.almalinux.org/almalinux/RPM-GPG-KEY-AlmaLinux-$releasever

To create an AlmaLinux 9 minimal container: 
    
    # dnf --repo=baseos --releasever=9 --best --installroot=/var/lib/machines/_container-name_ --setopt=install_weak_deps=False install almalinux-release dhcp-client dnf glibc-langpack-en iproute iputils less passwd systemd vim-minimal
    
This will install the latest minor version of AlmaLinux 9, you can choose to install a specific point release, but you will need to change the _gpgpkey_ entry to manually point to _RPM-GPG-KEY-AlmaLinux-9_

Just like Arch, Fedora or AlmaLinux will not let you log in as root without a password. To set up the root password, run _systemd-nspawn_ without the `-b` option: 
    
    # systemd-nspawn -D /var/lib/machines/_container-name_ passwd
    
###  编译与测试包

请参阅 [Creating packages for other distributions](<https://wiki.archlinux.org/title/Creating_packages_for_other_distributions> "arch:Creating packages for other distributions") 寻找更多用例. 

##  管理

位于 `/var/lib/machines/` 的容器可以被 _machinectl_ 命令所控制，它可以内部控制 `systemd-nspawn@.service` 单元的实例。 `/var/lib/machines/` 下的子目录对应着容器的名字， 比如 `/var/lib/machines/_container-name_ /`。 

**注意：** 如果因为某些原因容器不能移进 `/var/lib/machines/` ， 可以使用符号链接。 详情看 [machinectl(1) § FILES AND DIRECTORIES](<https://man.archlinux.org/man/machinectl.1#FILES_AND_DIRECTORIES>) 。

###  默认 systemd-nspawn 选项

要明白非常重要的一点是通过 _machinectl_ 与 `systemd-nspawn@.service` 启动的容器所使用的默认选项与通过 _systemd-nspawn_ 命令手动启动的有所不同。 通过服务启动所使用的额外选项有： 

  * `-b`/`--boot` – 管理的容器会自动搜索一个init程序，并以PID 1的形式调用它。
  * `--network-veth` 关联于 `--private-network` – 管理的容器获得一个虚拟网络接口，并与主机网络断开连接。 详情看 [#网络](<#%E7%BD%91%E7%BB%9C>)。
  * `-U` – 如果内核支持，管理的容器默认使用 [user_namespaces(7)](<https://man.archlinux.org/man/user_namespaces.7>) 特性。 解释请看 [#无特权容器](<#%E6%97%A0%E7%89%B9%E6%9D%83%E5%AE%B9%E5%99%A8>)。
  * `--link-journal=try-guest`

这些行为可以在每个容器配置文件中被覆盖， 详情看 [#配置](<#%E9%85%8D%E7%BD%AE>)。 

### machinectl

**注意：** _machinectl_ 工具要求在容器中安装 [systemd](<../zh-cn/Systemd.html> "Systemd") 和 [dbus](<https://archlinux.org/packages/?name=dbus>)包 。有关详细讨论，请参阅 [[8]](<https://github.com/systemd/systemd/issues/685>)。

容器可以被 `machinectl _subcommand_ _container-name_` 命令管理， 比如说，启动容器： 
    
    $ machinectl start _container-name_
    
**注意：** _machinectl_ 要求 container-name 只包含 ASCII 字符，数字与连字符。这样才能保证 [hostname](</wzh/index.php?title=Hostname&action=edit&redlink=1> "Hostname（页面不存在）") 的合法性。比如，如果 container-name 包含了下划线，这将不会被识别并且当你运行 `machinectl start container_name` 时将会报错 `Invalid machine name container_name`。详情请看 [[9]](<https://github.com/systemd/systemd/issues/11765>) 与 [[10]](<https://github.com/systemd/systemd/commit/d65652f1f21a4b0c59711320f34266c635393c89>) 。

相似的， 还有其他的子命令 `poweroff`， `reboot`， `status` 和 `show`. 详细解释请看 [machinectl(1) § Machine Commands](<https://man.archlinux.org/man/machinectl.1#Machine_Commands>) 。 

**提示：** 关机与重启操作可以在容器内通过 `poweroff` and `reboot` 命令执行。

其他常见命令： 

  * `machinectl list` – 显示现在正在运行的容器
  * `machinectl login _container-name_` – 在一个容器中打开一个交互式登录会话
  * `machinectl shell _[username@]container-name_` – 在容器中打开一个交互式shell会话（这将立即调用一个用户进程，而不需要通过容器中的登录进程）
  * `machinectl enable _container-name_` 与 `machinectl disable _container-name_` – 启用或禁用容器的随开机启动，详见 [#启用容器的随开机启动](<#%E5%90%AF%E7%94%A8%E5%AE%B9%E5%99%A8%E7%9A%84%E9%9A%8F%E5%BC%80%E6%9C%BA%E5%90%AF%E5%8A%A8>)

_machinectl_ 也有管理容器（或虚拟机）镜像和镜像传输的子命令。 详情见 [machinectl(1) § Image Commands](<https://man.archlinux.org/man/machinectl.1#Image_Commands>) 与 [machinectl(1) § Image Transfer Commands](<https://man.archlinux.org/man/machinectl.1#Image_Transfer_Commands>) 。 

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 增加一些明确的例子，如何使用镜像传输命令。最重要的是，在哪里可以找到合适的镜像。 (在 [Talk:Systemd-nspawn](<../zh-cn/Talk:Systemd-nspawn.html>) 中讨论)

###  systemd 工具链

大部分核心的 systemd 工具链已更新为对容器有效。工具们通常提供了 `-M, --machine=` 选项并把容器名称作为参数。 用例： 

查看特定容器的 journal 日志： 
    
    # journalctl -M _MyContainer_
    
显示控制组的内容： 
    
    $ systemd-cgls -M _MyContainer_
    
查看容器的启动时间： 
    
    $ systemd-analyze -M _MyContainer_
    
查看资源使用情况的概况： 
    
    $ systemd-cgtop
    
##  配置

###  容器前设置

要指定容器前设置而不是全局覆盖，可以使用 _.nspawn_ 文件。 详情见 [systemd.nspawn(5)](<https://man.archlinux.org/man/systemd.nspawn.5>) 。 

**注意：**

  * 当执行`machinectl remove` 的时候， _.nspawn_ 文件可能会从 `/etc/systemd/nspawn/` 被意外移除。 [[11]](<https://github.com/systemd/systemd/issues/15900>)
  * 当有`--settings=override`（在`systemd-nspawn@.service`文件内被指定）时， _.nspawn_ 内与命令行中所指定的为网络选项的交互不能正常工作。[[12]](<https://github.com/systemd/systemd/issues/12313#issuecomment-681116926>) 作为一个变通方法，你需要引入`VirtualEthernet=on`选项，即使服务指定了`--network-veth`。

###  启用容器的随开机启动

当频繁使用一个容器时，你可能希望在系统启动时启动它。 

首先确保 `machines.target` 已经 [enabled](</wzh/index.php?title=Enabled&action=edit&redlink=1> "Enabled（页面不存在）")。 

容器被 [machinectl](<#machinectl>) 的可发现可以 enabled 或者 disabled。 
    
    $ machinectl enable _container-name_
    
**注意：**

  * 这样做的效果是启用 `systemd-nspawn@_container-name_.service` systemd单元。
  * 如[#默认 systemd-nspawn 选项](<#%E9%BB%98%E8%AE%A4_systemd-nspawn_%E9%80%89%E9%A1%B9>)中提到的，由 _machinectl_ 启动的容器会获得一个虚拟的以太网接口。要禁用私有网络，请参见[#使用主机网络](<#%E4%BD%BF%E7%94%A8%E4%B8%BB%E6%9C%BA%E7%BD%91%E7%BB%9C>)。

###  资源控制

您可以使用控制组来使用 `systemctl set-property` 实现对容器的限制和资源管理，请参阅 [systemd.resource-control(5)](<https://man.archlinux.org/man/systemd.resource-control.5>)。例如，您可能希望限制内存量或 CPU 使用率。要将容器的内存消耗限制为 2 GiB： 
    
    # systemctl set-property systemd-nspawn@_myContainer_.service MemoryMax=2G
    
或者将 CPU 时间使用率限制为大约相当于 2 个内核： 
    
    # systemctl set-property systemd-nspawn@_myContainer_.service CPUQuota=200%
    
这将在 `/etc/systemd/system.control/systemd-nspawn@_myContainer_.service.d/` 中创建常驻文件}。 

根据文档，`MemoryHigh` 是控制内存消耗的首选方法，但也不会像 `MemoryMax` 那样进行强制限制。您可以使用这两个选项将 `MemoryMax` 作为您最后的一道防线。还要考虑到如果您不会限制容器可以“看到”的 CPU 数量，但通过限制容器相对于总 CPU 时间的最大时间，也可以获得类似的结果。 

**提示：** 如果不希望在重新启动后保留此更改，则可以传递选项 `--runtime` 使更改成为临时性的。您可以使用 `systemd-cgtop` 检查其结果。

###  网络

_systemd-nspawn_ 容器可以使用 _主机网络_ 或者 _私有网络_ : 

  * 在主机网络模式下，容器可以完全访问主机网络。这意味着容器将能够访问主机上的所有网络服务，来自容器的数据包将在外部网络中显示为来自主机（即共享同一IP地址）。
  * 在私有网络模式下，容器与主机的网络断开连接，这使得容器无法使用所有网络接口，但环回设备和明确分配给容器的接口除外。为容器设置网络接口有多种不同的方法： 
    * 可以将现有接口分配给容器（例如，如果您有多个以太网设备）。
    * 可以创建一个与现有接口（即[VLAN](<../zh-cn/VLAN.html> "VLAN")接口）相关联的虚拟网络接口，并将其分配给容器。
    * 可以创建主机和容器之间的虚拟以太网链接。

    在后一种情况下，容器的网络是完全隔离的（与外部网络以及其他容器），由管理员来配置主机和容器之间的网络。这通常涉及创建一个网桥[network bridge](<../zh-cn/Network_bridge.html> "Network bridge")来连接多个（物理或虚拟）接口，或者在多个接口之间设置一个NAT[Network Address Translation](<https://en.wikipedia.org/wiki/Network_Address_Translation> "wikipedia:Network Address Translation")。

主机网络模式适用于 _应用程序容器_ ，它不运行任何网络软件来配置分配给容器的接口。当你从shell运行 _systemd-nspawn_ 时，主机联网是默认模式。 

另一方面，私有网络模式适用于应与主机系统隔离的 "系统容器"。创建虚拟以太网链路是一个非常灵活的工具，可以创建复杂的虚拟网络。这是由 _machinectl_ 或`systemd-nspawn@.service`启动的容器的默认模式。 

下面的小节描述了常见的情况。关于可用的 _systemd-nspawn_ 选项，请参见[systemd-nspawn(1) § Networking Options](<https://man.archlinux.org/man/systemd-nspawn.1#Networking_Options>)。 

####  使用主机网络

要禁用私有网络和创建由 _machinectl_ 启动的容器使用的虚拟以太网链接，请添加 _.nspawn_ 文件，其中包含以下选项： 
    
    /etc/systemd/nspawn/_container-name_.nspawn
    
    [Network]
    VirtualEthernet=no

这将覆盖在`systemd-nspawn@.service`中使用的`-n`/`--network-veth`选项，新启动的容器将使用主机网络模式。 

####  使用虚拟以太网链接

如果使用`-n`/`--network-veth`选项启动容器， _systemd-nspawn_ 将在主机和容器之间创建一个虚拟的以太网链接。链接的主机侧将作为名为`ve-_容器名称_`的网络接口提供。链路的容器侧将被命名为`host0`。请注意，这个选项意味着 `--private-network`。 

**注意：**

  * 如果容器名称太长，接口名称将被缩短（例如`ve-long-conKQGh`而不是`ve-long-container-name`），以适应[15个字符的限制](<https://stackoverflow.com/a/29398765>)。全名将被设置为接口的`altname`属性（见[ip-link(8)](<https://man.archlinux.org/man/ip-link.8>)），并且仍然可以用来引用接口。
  * 当检查带有`ip link`的接口时，接口名会显示一个后缀，例如`ve-_容器名_ @if2`和`host0@if9`。`@if _N_`实际上并不是接口名称的一部分，相反，`ip link`附加了这个信息，以指示虚拟以太网电缆连接到另一端的哪个 "槽"。

    例如，显示为`ve-_foo_ @if2`的主机虚拟以太网接口与容器` _foo_`相连，在容器内部与第二个网络接口--在容器内部运行`ip link`时，显示索引为2的接口。同理，容器内名为`host0@if9`的接口连接到主机上的第9个网络接口。

当您启动容器时，必须为两个接口（主机上和容器中）分配一个 IP 地址。如果您在主机上和容器中都使用[systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd")，这就是开箱即用： 

  * 主机上的`/usr/lib/systemd/network/80-container-ve.network`文件与`ve-_container-name_`接口相匹配，并启动一个DHCP服务器，该服务器为主机接口和容器分配IP地址，
  * 容器中的`/usr/lib/systemd/network/80-container-host0.network`文件与`host0`接口相匹配，并启动一个DHCP客户端，该客户端从主机接收一个IP地址。

如果不使用 [systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd")，可以配置静态 IP 地址或在主机接口上启动 DHCP 服务器，在容器中启动 DHCP 客户端。详情请参见[网络配置](<../zh-cn/%E7%BD%91%E7%BB%9C%E9%85%8D%E7%BD%AE.html> "网络配置")。 

要让容器访问外部网络，您可以按照 [Internet sharing#Enable NAT](<../zh-cn/Internet_sharing.html#Enable_NAT> "Internet sharing") 中的描述配置 NAT。如果您使用 [systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd")，这将通过 `/usr/lib/systemd/network/80-container-ve.network` 中的 `IPMasquerade=yes` 选项自动（部分）完成。然而，这只会发出一个[iptables](<../zh-cn/Iptables.html> "Iptables")规则，比如说： 
    
    -t nat -A POSTROUTING -s 192.168.163.192/28 -j MASQUERADE
    
`filter`表必须手动配置，如[Internet sharing#Enable NAT](<../zh-cn/Internet_sharing.html#Enable_NAT> "Internet sharing")所示。您可以使用通配符来匹配所有以`ve-`开头的接口： 
    
    # iptables -A FORWARD -i ve-+ -o _internet0_ -j ACCEPT
    
**注意：** _systemd-networkd_ 使用[libiptc](<https://tldp.org/HOWTO/Querying-libiptc-HOWTO/whatis.html>)库与[iptables](<../zh-cn/Iptables.html> "Iptables")交互。如果您使用[nftables](<../zh-cn/Nftables.html> "Nftables")，请安装 [iptables-nft](<https://archlinux.org/packages/?name=iptables-nft>)包 转译层。参见 [systemd issue 13307](<https://github.com/systemd/systemd/issues/13307>)。

并且，为了接收DHCP服务器的入站连接，你需要在 `ve-+` 接口上开放 UDP 67 端口（由 _systemd-networkd_ 操控）： 
    
    # iptables -A INPUT -i ve-+ -p udp -m udp --dport 67 -j ACCEPT
    
####  使用网络桥接

如果您已在主机系统上配置了网桥[network bridge](<../zh-cn/Network_bridge.html> "Network bridge")，则可以为容器创建一个虚拟以太网链路，并将其主机侧添加到网桥中。这可以通过`--network-bridge=_bridge-name_`选项来完成。请注意，`--network-bridge`意味着`--network-veth`，即虚拟以太网链路是自动创建的。然而，链路的主机端将使用`vb-`前缀而不是`ve-`，因此用于启动DHCP服务器和IP伪装的[systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd")选项将不会被应用。 

网桥的管理由管理员负责。例如，网桥可以用一个物理接口连接虚拟接口，也可以只连接几个容器的虚拟接口。参见[systemd-networkd#Network bridge with DHCP](<../zh-cn/Systemd-networkd.html#Network_bridge_with_DHCP> "Systemd-networkd")和[systemd-networkd#Network bridge with static IP addresses](<../zh-cn/Systemd-networkd.html#Network_bridge_with_static_IP_addresses> "Systemd-networkd")，了解使用[systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd")进行配置的例子。 

还有一个`--network-zone=_zone-name_`选项，它与`--network-bridge`类似，但网桥由 _systemd-nspawn_ 和 _systemd-networkd_ 自动管理。当第一个用`vz-_zone-name_`配置的容器启动时，会自动创建名为`--network-zone=_zone-name_`的网桥接口，当最后一个用`--network-zone=_zone-name_`配置的容器退出时，会自动删除。因此，这个选项可以方便地将多个相关的容器放置在一个共同的虚拟网络上。请注意，`vz-*`接口由[systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd")管理的方式与`ve-*`接口相同，使用`/usr/lib/systemd/network/80-container-vz.network`文件中的选项。 

####  使用 "macvlan" 或者 "ipvlan" 接口

您可以在现有的物理接口（即[VLAN](<../zh-cn/VLAN.html> "VLAN")接口）上创建一个虚拟接口，并将其添加到容器中，而不是创建一个虚拟的以太网链路（其主机端可能被添加到桥接中，也可能没有）。该虚拟接口将与底层主机接口进行桥接，从而使容器暴露在外部网络中，从而使其能够通过DHCP从与主机相连的同一局域网中获得一个独特的IP地址。 

_systemd-nspawn_ 提供两个选项: 

  * `--network-macvlan=_interface_` – 虚拟接口的MAC地址将与底层物理` _interface_`不同，并被命名为`mv-_interface_`。
  * `--network-ipvlan=_interface_` – 虚拟接口的MAC地址将与底层物理` _interface_`相同，并命名为`iv-_interface_`。​

所有选项都意味着 `--private-network`. 

####  使用现有接口

如果主机系统有多个物理网络接口，可以使用`--network-interface=_interface_`将` _interface_`分配给容器（并使它在容器启动时对主机不可用）。请注意，`--network-interface`意味着`--private-network`。 

**提示：** 自 [v256](<https://github.com/systemd/systemd/releases/tag/v256>) 版本起，systemd-nspawn 容器支持传递无线网络接口。

###  端口映射

当启用私有网络时，可以使用`-p`/`-port`选项或使用 _.nspawn_ 文件中的`Port`设置将主机上的各个端口映射到容器上的端口。这可以通过向`nat`表发出[iptables](<../zh-cn/Iptables.html> "Iptables")规则来完成，但需要手动配置`forward`表中的`filter`链，如[#使用虚拟以太网链接](<#%E4%BD%BF%E7%94%A8%E8%99%9A%E6%8B%9F%E4%BB%A5%E5%A4%AA%E7%BD%91%E9%93%BE%E6%8E%A5>)所示。 

例如，将主机上的TCP端口8000映射到容器中的TCP端口80： 
    
    /etc/systemd/nspawn/_container-name_.nspawn
    
    [Network]
    Port=tcp:8000:80

**注意：**

  * _systemd-nspawn_ 在映射端口时明确地排除了`loopback`接口。因此，在上面的例子中，`localhost:8000` 连接到主机而不是容器。只有到其他接口的连接才会受到端口映射的影响。详情请参见 [[13]](<https://github.com/systemd/systemd/issues/6106>)。
  * 端口映射只对IPv4连接有效。[[14]](<https://github.com/systemd/systemd/issues/10254>)。

###  域名解析

容器中的域名解析 [Domain name resolution](<../zh-cn/Domain_name_resolution.html> "Domain name resolution") 可以以主机系统中相同的方式配置。另外， _systemd-nspawn_ 提供了管理容器中 `/etc/resolv.conf` 文件的选项： 

  * `--resolv-conf` can be used on command-line
  * `ResolvConf=` can be used in _.nspawn_ files

这些相应的选项有许多可能的值，在 [systemd-nspawn(1) § Integration Options](<https://man.archlinux.org/man/systemd-nspawn.1#Integration_Options>) 的描述中会提到。 默认值为 `auto`，这意味着： 

  * 如果启用了`--private-network`，`/etc/resolv.conf`就会保持容器中的原样。
  * 否则，如果[systemd-resolved](<../zh-cn/Systemd-resolved.html> "Systemd-resolved")在主机上运行，它的存根文件`resolv.conf`将被复制或绑定到容器中。
  * 否则，`/etc/resolv.conf` 文件就会被从主机复制或绑定到容器上。

在后两种情况下，如果容器根部是可写的，则复制文件，如果是只读的，则绑定挂载。 

对于第二种 [systemd-resolved](<../zh-cn/Systemd-resolved.html> "Systemd-resolved") 在宿主机上运行的情况， _systemd-nspawn_ 希望它也能在容器中运行，所以容器将会从宿主中 `/etc/resolv.conf` 文件建立桩符号链接。如果不是这样，那么默认值 `auto` 将不会生效，你应该使用任意 `replace-*` 选项来替换这个链接。 

##  提示和技巧

###  运行 non-shell/init 命令

来自 [systemd-nspawn(1) § Execution_Options](<https://man.archlinux.org/man/systemd-nspawn.1#Execution_Options>): 

    "[选项] `--as-pid2` [调用] shell 或以进程ID (PID) 2 而不是 PID 1 (init) 来运行特定程序。 [...] 建议使用这种模式来调用容器中的任意命令，除非它们已经被修改为以PID 1的形式正确运行。**或者换句话说：这个改变应该被用于几乎所有的命令** ，除非该命令是指一个init或shell的实现。"

###  无特权容器

_systemd-nspawn_ 支持无特权的容器，不过容器需要以root身份启动。​ 

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** Very little of [Linux Containers#Enable support to run unprivileged containers (optional)](<../zh-cn/Linux_Containers.html#Enable_support_to_run_unprivileged_containers_\(optional\)> "Linux Containers") applies to systemd-nspawn.（在[Talk:Systemd-nspawn](<../zh-cn/Talk:Systemd-nspawn.html>)讨论）

**注意：** 此功能需要 [user_namespaces(7)](<https://man.archlinux.org/man/user_namespaces.7>), 更多信息请参见 [Linux Containers#Enable support to run unprivileged containers (optional)](<../zh-cn/Linux_Containers.html#Enable_support_to_run_unprivileged_containers_\(optional\)> "Linux Containers")。

最简单的方法是通过`-U`选项让 _systemd-nspawn_ 自动选择一个未使用的UID/GID范围。 
    
    # systemd-nspawn -bUD ~/MyContainer
    
如果内核支持用户命名空间，`-U`选项相当于`--private-users=pick --private-users-ownership=auto`。详情请参见[systemd-nspawn(1) § User Namespacing Options](<https://man.archlinux.org/man/systemd-nspawn.1#User_Namespacing_Options>)。 

**注意：** 您也可以手动指定容器的UID/GID范围，但是，这很少有用。

如果一个容器曾使用 `--private-users-ownership=chown` 选项（或者在一个 `-U` 需要 `--private-users-ownership=chown` 的文件系统中）在私有UID/GID范围启动，就需要一直这样使用它以避免权限错误。另外，也可以在一个ID范围从0开始的容器文件系统中撤销`--private-users-ownership=chown`的效果： 
    
    # systemd-nspawn -D ~/MyContainer --private-users=0 --private-users-ownership=chown
    
###  使用 X 环境

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 本节末尾有关 systemd 版本的注释似乎已经过时。对于我（译者注：原作者）来说（systemd 版本为239） 如果 `/tmp/.X11-unix` 权限是 rw，X应用程序可以工作运行。（在 [Talk:Systemd-nspawn#/tmp/.X11-unix contents have to be bind-mounted as read-only - still relevant?](<../zh-cn/Talk:Systemd-nspawn.html#/tmp/.X11-unix_contents_have_to_be_bind-mounted_as_read-only_-_still_relevant?> "Talk:Systemd-nspawn") 中讨论）

详情见 [Xhost](<../zh-cn/Xhost.html> "Xhost") 和 [Change root#Run graphical applications from chroot](<../zh-cn/Change_root.html#Run_graphical_applications_from_chroot> "Change root"). 

您需要设置您容器会话中 `DISPLAY` 以连接到外部 X 服务器。 

X 在 `/tmp` 文件夹中存储一些必要的文件。为了使容器能显示任何内容，它需要访问这些文件。为此，当启动容器时，请追加 `--bind-ro=/tmp/.X11-unix` 选项。 

**注意：** 从 systemd 版本 235 开始, `/tmp/.X11-unix` 的内容 [必须以只读方式装入](<https://github.com/systemd/systemd/issues/7093>)，否则它们将从文件系统中消失。只读挂载标志不会阻止在套接字上使用 `connect()`。如果你还绑定了`/run/user/1000` 那么你有可能希望显式绑定 `/run/user/1000/bus` 为只读，以防止 dbus 套接字被删除。

####  避免 xhost

`xhost` 仅提供对 X 服务器相当粗糙的访问权限。更细节的访问可通过`$XAUTHORITY` 文件控制。遗憾的是, 仅使 `$XAUTHORITY` 文件在容器中可被访问并无法正常的执行工作: 这是因为您的 `$XAUTHORITY` 文件只特定于您的主机，但是容器是另一台主机。 根据 [stackoverflow](<https://stackoverflow.com/a/25280523>) 下面这个技巧可以让你的X服务器接受来自于你容器中的X应用的 `$XAUTHORITY` 文件： 
    
    $ XAUTH=/tmp/container_xauth
    $ xauth nextract - "$DISPLAY" | sed -e 's/^..../ffff/' | xauth -f "$XAUTH" nmerge -
    # systemd-nspawn -D myContainer --bind=/tmp/.X11-unix --bind="$XAUTH" -E DISPLAY="$DISPLAY" -E XAUTHORITY="$XAUTH" --as-pid2 /usr/bin/xeyes
    
上面第二行将连接的组设定为 "FamilyWild"，GID为`65535`，会使输入匹配你的每一个显示。 更多信息请参考 [Xsecurity(7)](<https://man.archlinux.org/man/Xsecurity.7>) 。 

####  使用 X 嵌套/Xephyr

另一个运行X应用程序并避免共享X桌面风险的简单方法是使用X嵌套。 这里的优点是完全避免了容器内应用程序和非容器内应用程序之间的交互，并且能够运行不同的 [desktop environment](<../zh-cn/Desktop_environment.html> "Desktop environment") 或 [window manager](<../zh-cn/Window_manager.html> "Window manager")，缺点是使用 [Xephyr](<../zh-cn/Xephyr.html> "Xephyr") 时性能较差，并且缺乏硬件加速。 在容器外启动 Xephyr： 
    
    # Xephyr :1 -resizeable
    
然后在使用下面的参数启动容器： 
    
    --setenv=DISPLAY=:1 --bind-ro=/tmp/.X11-unix/X1
    
不需要其他绑定。 在某些情况下，你可能仍然需要在容器中手动设置 `DISPLAY=:1`（主要是在与 `b` 一起使用时）。 

###  运行 Firefox

以PID 1运行​ 
    
     # systemd-nspawn --setenv=DISPLAY=:0 \
                  --setenv=XAUTHORITY=~/.Xauthority \
                  --bind-ro=$HOME/.Xauthority:/root/.Xauthority \
                  --bind=/tmp/.X11-unix \
                  -D ~/containers/firefox \
                  --as-pid2 \
                  firefox
                  
**注意：** 因此，如果不使用 [#无特权容器](<#%E6%97%A0%E7%89%B9%E6%9D%83%E5%AE%B9%E5%99%A8>)，firefox会以根用户的身份运行，这就带来了自身的风险。在这种情况下，你可以先选择在容器内 [添加一个用户](<../zh-cn/Users_and_groups.html#Example_adding_a_user> "Users and groups")，然后在 _systemd-nspawn_ 调用中增加 `--user <username>` 选项。

或者你可以启动容器，让[systemd-networkd](<../zh-cn/Systemd-networkd.html> "Systemd-networkd")等设置虚拟网络接口： 
    
    # systemd-nspawn --bind-ro=$HOME/.Xauthority:/root/.Xauthority \
                  --bind=/tmp/.X11-unix \
                  -D ~/containers/firefox \
                  --network-veth -b
    
一旦你的容器被启动，就像这样运行Xorg二进制文件： 
    
    # systemd-run -M firefox --setenv=DISPLAY=:0 firefox
    
####  3D图形加速

为了启用加速的3D图形，可能有必要在 _.nspawn_ 文件中加入以下一行，将 `/dev/dri` 挂载到容器中。 
    
    Bind=/dev/dri
    
上述技巧来自[patrickskiba.com](<https://web.archive.org/web/20190925003151/https://patrickskiba.com/sysytemd-nspawn/2019/03/21/graphical-applications-in-systemd-nspawn.html>)。这将明显解决了以下问题 
    
    libGL error: MESA-LOADER: failed to retrieve device information
    libGL error: Version 4 or later of flush extension not found
    libGL error: failed to load driver: i915
    
你可以通过运行 `glxinfo` 或 `glxgears` 来确认它已经被启用。 

##### Nvidia GPUs

如果你不能在容器上安装与主机上相同的nvidia驱动版本，你可能需要同时绑定驱动库文件。你可以在主机上运行 `pacman -Ql nvidia-utils` 来查看它包含的所有文件。你不需要把所有文件都复制过来。当容器通过 `machinectl start _container-name_` 运行时，下面的systemd覆盖文件将把所有必要的文件绑定过来。 

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 将 `/usr/lib/` 绑定到 `/usr/lib/x86_64-linux-gnu/` 是没有必要的。（在 [Talk:Systemd-nspawn](<../zh-cn/Talk:Systemd-nspawn.html>) 中讨论）

    /etc/systemd/system/systemd-nspawn@.service.d/nvidia-gpu.conf
    
    [Service]
    ExecStart=
    ExecStart=systemd-nspawn --quiet --keep-unit --boot --link-journal=try-guest --machine=%i \
    --bind=/dev/dri \
    --bind=/dev/shm \
    --bind=/dev/nvidia0 \
    --bind=/dev/nvidiactl \
    --bind=/dev/nvidia-modeset \
    --bind=/usr/bin/nvidia-bug-report.sh:/usr/bin/nvidia-bug-report.sh \
    --bind=/usr/bin/nvidia-cuda-mps-control:/usr/bin/nvidia-cuda-mps-control \
    --bind=/usr/bin/nvidia-cuda-mps-server:/usr/bin/nvidia-cuda-mps-server \
    --bind=/usr/bin/nvidia-debugdump:/usr/bin/nvidia-debugdump \
    --bind=/usr/bin/nvidia-modprobe:/usr/bin/nvidia-modprobe \
    --bind=/usr/bin/nvidia-ngx-updater:/usr/bin/nvidia-ngx-updater \
    --bind=/usr/bin/nvidia-persistenced:/usr/bin/nvidia-persistenced \
    --bind=/usr/bin/nvidia-powerd:/usr/bin/nvidia-powerd \
    --bind=/usr/bin/nvidia-sleep.sh:/usr/bin/nvidia-sleep.sh \
    --bind=/usr/bin/nvidia-smi:/usr/bin/nvidia-smi \
    --bind=/usr/bin/nvidia-xconfig:/usr/bin/nvidia-xconfig \
    --bind=/usr/lib/gbm/nvidia-drm_gbm.so:/usr/lib/x86_64-linux-gnu/gbm/nvidia-drm_gbm.so \
    --bind=/usr/lib/libEGL_nvidia.so:/usr/lib/x86_64-linux-gnu/libEGL_nvidia.so \
    --bind=/usr/lib/libGLESv1_CM_nvidia.so:/usr/lib/x86_64-linux-gnu/libGLESv1_CM_nvidia.so \
    --bind=/usr/lib/libGLESv2_nvidia.so:/usr/lib/x86_64-linux-gnu/libGLESv2_nvidia.so \
    --bind=/usr/lib/libGLX_nvidia.so:/usr/lib/x86_64-linux-gnu/libGLX_nvidia.so \
    --bind=/usr/lib/libcuda.so:/usr/lib/x86_64-linux-gnu/libcuda.so \
    --bind=/usr/lib/libnvcuvid.so:/usr/lib/x86_64-linux-gnu/libnvcuvid.so \
    --bind=/usr/lib/libnvidia-allocator.so:/usr/lib/x86_64-linux-gnu/libnvidia-allocator.so \
    --bind=/usr/lib/libnvidia-cfg.so:/usr/lib/x86_64-linux-gnu/libnvidia-cfg.so \
    --bind=/usr/lib/libnvidia-egl-gbm.so:/usr/lib/x86_64-linux-gnu/libnvidia-egl-gbm.so \
    --bind=/usr/lib/libnvidia-eglcore.so:/usr/lib/x86_64-linux-gnu/libnvidia-eglcore.so \
    --bind=/usr/lib/libnvidia-encode.so:/usr/lib/x86_64-linux-gnu/libnvidia-encode.so \
    --bind=/usr/lib/libnvidia-fbc.so:/usr/lib/x86_64-linux-gnu/libnvidia-fbc.so \
    --bind=/usr/lib/libnvidia-glcore.so:/usr/lib/x86_64-linux-gnu/libnvidia-glcore.so \
    --bind=/usr/lib/libnvidia-glsi.so:/usr/lib/x86_64-linux-gnu/libnvidia-glsi.so \
    --bind=/usr/lib/libnvidia-glvkspirv.so:/usr/lib/x86_64-linux-gnu/libnvidia-glvkspirv.so \
    --bind=/usr/lib/libnvidia-ml.so:/usr/lib/x86_64-linux-gnu/libnvidia-ml.so \
    --bind=/usr/lib/libnvidia-ngx.so:/usr/lib/x86_64-linux-gnu/libnvidia-ngx.so \
    --bind=/usr/lib/libnvidia-opticalflow.so:/usr/lib/x86_64-linux-gnu/libnvidia-opticalflow.so \
    --bind=/usr/lib/libnvidia-ptxjitcompiler.so:/usr/lib/x86_64-linux-gnu/libnvidia-ptxjitcompiler.so \
    --bind=/usr/lib/libnvidia-rtcore.so:/usr/lib/x86_64-linux-gnu/libnvidia-rtcore.so \
    --bind=/usr/lib/libnvidia-tls.so:/usr/lib/x86_64-linux-gnu/libnvidia-tls.so \
    --bind=/usr/lib/libnvidia-vulkan-producer.so:/usr/lib/x86_64-linux-gnu/libnvidia-vulkan-producer.so \
    --bind=/usr/lib/libnvoptix.so:/usr/lib/x86_64-linux-gnu/libnvoptix.so \
    --bind=/usr/lib/modprobe.d/nvidia-utils.conf:/usr/lib/x86_64-linux-gnu/modprobe.d/nvidia-utils.conf \
    --bind=/usr/lib/nvidia/wine/_nvngx.dll:/usr/lib/x86_64-linux-gnu/nvidia/wine/_nvngx.dll \
    --bind=/usr/lib/nvidia/wine/nvngx.dll:/usr/lib/x86_64-linux-gnu/nvidia/wine/nvngx.dll \
    --bind=/usr/lib/nvidia/xorg/libglxserver_nvidia.so:/usr/lib/x86_64-linux-gnu/nvidia/xorg/libglxserver_nvidia.so \
    --bind=/usr/lib/vdpau/libvdpau_nvidia.so:/usr/lib/x86_64-linux-gnu/vdpau/libvdpau_nvidia.so \
    --bind=/usr/lib/xorg/modules/drivers/nvidia_drv.so:/usr/lib/x86_64-linux-gnu/xorg/modules/drivers/nvidia_drv.so \
    --bind=/usr/share/X11/xorg.conf.d/10-nvidia-drm-outputclass.conf:/usr/share/X11/xorg.conf.d/10-nvidia-drm-outputclass.conf \
    --bind=/usr/share/dbus-1/system.d/nvidia-dbus.conf:/usr/share/dbus-1/system.d/nvidia-dbus.conf \
    --bind=/usr/share/egl/egl_external_platform.d/15_nvidia_gbm.json:/usr/share/egl/egl_external_platform.d/15_nvidia_gbm.json \
    --bind=/usr/share/glvnd/egl_vendor.d/10_nvidia.json:/usr/share/glvnd/egl_vendor.d/10_nvidia.json \
    --bind=/usr/share/licenses/nvidia-utils/LICENSE:/usr/share/licenses/nvidia-utils/LICENSE \
    --bind=/usr/share/vulkan/icd.d/nvidia_icd.json:/usr/share/vulkan/icd.d/nvidia_icd.json \
    --bind=/usr/share/vulkan/implicit_layer.d/nvidia_layers.json:/usr/share/vulkan/implicit_layer.d/nvidia_layers.json \
    DeviceAllow=/dev/dri rw
    DeviceAllow=/dev/shm rw
    DeviceAllow=/dev/nvidia0 rw
    DeviceAllow=/dev/nvidiactl rw
    DeviceAllow=/dev/nvidia-modeset rw

**注意：** 每当你在主机上升级nvidia驱动时，你将需要重启容器，并可能需要在容器中运行 `ldconfig` 以更新库。

###  访问主机文件系统

请见 `--bind` 和 `--bind-ro` 于 [systemd-nspawn(1)](<https://man.archlinux.org/man/systemd-nspawn.1>). 

如果主机和容器都是 Arch Linux，则例如，可以共享 pacman 缓存： 
    
    # systemd-nspawn --bind=/var/cache/pacman/pkg
    
或许你还可以使用文件来进行指定的先于容器的绑定： 
    
    /etc/systemd/nspawn/_my-container_.nspawn
    
    [Files]
    Bind=/var/cache/pacman/pkg
    
详情见 [#容器前设置](<#%E5%AE%B9%E5%99%A8%E5%89%8D%E8%AE%BE%E7%BD%AE>). 

要将该目录绑定到容器内的不同路径，请添加路径，并用冒号分隔。例如： 
    
    # systemd-nspawn --bind=_/path/to/host_dir:/path/to/container_dir_
    
如果是 [#无特权容器](<#%E6%97%A0%E7%89%B9%E6%9D%83%E5%AE%B9%E5%99%A8>)，产生的挂载点将由nobody用户拥有。这可以通过 `idmap` 挂载选项来修改。 
    
    # systemd-nspawn --bind=_/path/to/host_dir:/path/to/container_dir_ :idmap
    
###  在非systemd系统上运行

详情见 [Init#systemd-nspawn](<../zh-cn/Init.html#systemd-nspawn> "Init")。 

###  使用Btrfs子卷作为容器的根

要使用 [Btrfs subvolume](<../zh-cn/Btrfs.html#Subvolumes> "Btrfs") 作为容器根目录的模板，请使用 `--template` 标志。这将获取子卷的快照，并以它填充容器的根目录。 

**注意：** 如果指定的模板路径不是子卷的根，则会复制**整个** 树。这将非常耗时。​

例如，要使用位于`/.snapshots/403/snapshot`的快照： 
    
    # systemd-nspawn --template=/.snapshots/403/snapshots -b -D _my-container_
    
其中` _my-container_`是将为容器创建的目录的名称。关机后，会保留新创建的子卷。​ 

###  使用容器的临时Btrfs快照

可以使用`--ephemeral`或`-x`标志来创建容器的临时btrfs快照，并将其作为容器的根。在容器中启动时所作的任何更改都将丢失。例如： 
    
    # systemd-nspawn -D _my-container_ -xb
    
其中 _my-container_ 是**现有** 容器或系统的目录。例如，如果`/`是一个btrfs子卷，我们可以通过以下操作创建一个当前运行的主机系统的短暂容器： 
    
    # systemd-nspawn -D / -xb 
    
关闭容器电源后，创建的btrfs子卷会立即被删除。 

###  在 systemd-nspawn 中运行 docker

自 [Docker](<../zh-cn/Docker.html> "Docker") 20.10以来，在启用 _cgroups v2_ （Arch Linux默认）的情况下，可以在无特权的 _systemd-nspawn_ 容器内运行Docker容器，而不会因为禁用cgroups和用户名字空间而破坏安全措施。要做到这一点，请编辑或创建 `/etc/systemd/nspawn/myContainer.nspawn`，并添加以下配置。 
    
    /etc/systemd/nspawn/myContainer.nspawn
    
    [Exec]
    SystemCallFilter=add_key keyctl bpf
    
然后，Docker 应该在容器内按原样工作。 

**注意：** 上述配置将系统调用 _add_key_ 、 _keyctl_ 和 _bpf_ 暴露给容器，而这些调用是没有命名间隔的。这仍然可能是一个安全风险，尽管它比完全禁用用户命名空间要低得多，就像人们在 cgroups v2 之前必须做的那样。

由于 _overlayfs_ 不能用于用户命名空间，并且在 _systemd-nspawn_ 中不可用，默认情况下，Docker 会退回到使用低效的 _vfs_ 作为其存储驱动，每次启动容器都会创建一个镜像的副本。这一点可以通过使用 _fuse-overlayfs_ 作为其存储驱动来解决。要做到这一点，我们需要首先将 _fuse_ 暴露给容器。 
    
    /etc/systemd/nspawn/myContainer.nspawn
    
    [Files]
    Bind=/dev/fuse
    
然后允许容器读取和写入设备节点。 
    
    # systemctl set-property systemd-nspawn@myContainer DeviceAllow='/dev/fuse rwm'
    
最后，在容器中安装 [fuse-overlayfs](<https://archlinux.org/packages/?name=fuse-overlayfs>)包 包。你需要重新启动容器以使所有配置生效。 

###  映射本地用户并将其主目录绑定挂载到容器中

按照[#创建并启动一个最小的 Arch Linux 容器](<#%E5%88%9B%E5%BB%BA%E5%B9%B6%E5%90%AF%E5%8A%A8%E4%B8%80%E4%B8%AA%E6%9C%80%E5%B0%8F%E7%9A%84_Arch_Linux_%E5%AE%B9%E5%99%A8>)中的说明，在 `/var/lib/machines/MyContainer/` 中创建一个容器。 

创建一个包含 `BindUser=` 的配置文件，以将选定的本地用户名映射到容器中。请注意，这需要 `PrivateUsers=`，详见 [systemd-nspawn(1)](<https://man.archlinux.org/man/systemd-nspawn.1>) 手册页。在容器内外绑定挂载的主目录中创建的文件将具有相同的 UID 和 GID。 
    
    /etc/systemd/nspawn/MyContainer.nspawn
    
    [Exec]
    User=_username_
    PrivateUsers=pick
    
    [Files]
    BindUser=_username_

在配置中同时使用 `User=` 指定了用于在容器内运行命令（例如交互式 shell）的默认用户： 
    
    # systemd-nspawn -M MyContainer bash
    
这对于从另一个 Linux 发行版测试 Arch Linux 软件包很有帮助。 

##  疑难解答

###  Root登录失败

如果您在尝试登录时（即使用`machinectl login <name>`）得到以下错误: 
    
    arch-nspawn login: root
    Login incorrect
    
并且容器中`journal`显示: 
    
    pam_securetty(login:auth): access denied: tty 'pts/0' is not secure !
    
[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 用户不应编辑 `/usr/lib` 中的文件，`/usr/lib/tmpfiles.d/arch.conf` 中的改动会在 [filesystem](<https://archlinux.org/packages/?name=filesystem>)包 升级后丢失。（在 [Talk:Systemd-nspawn](<../zh-cn/Talk:Systemd-nspawn.html>) 中讨论）

只删除**容器** 文件系统中的`/etc/securetty`[[15]](<https://unix.stackexchange.com/questions/41840/effect-of-entries-in-etc-securetty/41939#41939>)和`/usr/share/factory/etc/securetty` ，或者也可以根据需要只简单地向 _容器_ 文件系统中 `/etc/securetty` 添加所需的pty终端设备（如 `pts/0`）。 

但是任何改变都会在下一次启动时被覆盖，因此有必要同时在 _容器_ 文件系统上的 `/usr/lib/tmpfiles.d/arch.conf` 文件中删除 `/etc/securetty` 条目，见[FS#63236](<https://bugs.archlinux.org/task/63236>)。如果你选择删除，也可以在 `/etc/pacman.conf` 中选择将这些文件列入黑名单（[NoExtract](<../zh-cn/Pacman.html#Skip_files_from_being_installed_to_system> "Pacman")），以防止它们被重新安装。详见 [FS#45903](<https://bugs.archlinux.org/task/45903>)。 

###  execv(...) failed: Permission denied

当试图通过`systemd-nspawn -bD _/path/to/container_`来启动容器时（或在容器中执行一些东西），出现以下错误： 
    
    execv(/usr/lib/systemd/systemd, /lib/systemd/systemd, /sbin/init) failed: Permission denied
    
即使有关文件的权限（即 `/lib/systemd/systemd`）是正确的，这也可能是由于以非root用户的身份挂载容器所在的文件系统造成的。例如，如果您在[fstab](<../zh-cn/Fstab.html> "Fstab")中手动挂载了具有`noauto,user,...`选项的磁盘， _systemd-nspawn_ 将不允许执行文件，即使它们是由root用户拥有的。 

###  TERM中的终端类型不正确（破损的颜色）

当通过`machinectl login`登录容器时，容器内的终端中的颜色和按键可能会被破坏。这可能是由于`TERM`环境变量中的终端类型不正确。除非明确配置，否则环境变量不会从主机上的 shell 继承，而是回到 systemd 中固定的默认值 (`vt220`)。要配置，在容器内为 `container-getty@.service` systemd 服务创建一个配置覆盖，启动 `machinectl login` 的登录 getty，并将 `TERM` 设置为与您登录的主机终端匹配的值： 
    
    /etc/systemd/system/container-getty@.service.d/term.conf
    
    [Service]
    Environment=TERM=xterm-256color

或者使用`machinectl shell`。它正确地继承了终端的`TERM`环境变量。 

###  在容器内挂载NFS共享

目前（2019年6月）还不可能 

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 下述方法未经过验证，正在讨论 (在 [Talk:Systemd-nspawn#A_trick_way_to_mount_a_NFS_share_with_the_container](<../zh-cn/Talk:Systemd-nspawn.html#A_trick_way_to_mount_a_NFS_share_with_the_container> "Talk:Systemd-nspawn") 中讨论)

曲线救国的方式是使用主机挂载NFS后通过[目录映射](<#%E8%AE%BF%E9%97%AE%E4%B8%BB%E6%9C%BA%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F>)到容器目录，NFS挂载方式请查看 [NFS#Client](<../zh-cn/NFS.html#Client> "NFS")。挂载后会遇到权限错误，这是因为容器的用户ID是通过主机映射过去的，详情请查看：[[16]](<https://systemd.io/UIDS-GIDS/>)， 解决这个问题的方法有很多种，如下面几种： 

  1. 在主机上使用管理员权限将NFS挂载目录所属用户ID修改为容器所对应的实际用户ID。
  2. 在容器启动时使用`--private-users`参数指定使用用户作为特权用户启动。
  3. 在挂载目录时使用`--bind-user`参数指定NFS目录所属用户映射到容器中。

## See also

  * [Automatic console login](<../zh-cn/Getty.html#Nspawn_console> "Getty")
  * [Creating containers with systemd-nspawn](<https://lwn.net/Articles/572957/>)
  * [Presentation by Lennart Poettering on systemd-nspawn](<https://www.youtube.com/results?search_query=systemd-nspawn&aq=f>)
  * [Running Firefox in a systemd-nspawn container](<https://dabase.com/e/12009/>)
  * [Graphical applications in systemd-nspawn](<https://web.archive.org/web/20190925003151/https://patrickskiba.com/sysytemd-nspawn/2019/03/21/graphical-applications-in-systemd-nspawn.html>)
