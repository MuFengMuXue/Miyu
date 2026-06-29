**翻译状态：**

  * 本文（或部分内容）译自 [Install Arch Linux from existing Linux](<https://wiki.archlinux.org/title/Install_Arch_Linux_from_existing_Linux> "arch:Install Arch Linux from existing Linux")，最近一次同步于 2025-11-12，若英文版本有所[更改](<https://wiki.archlinux.org/title/Install_Arch_Linux_from_existing_Linux?diff=0&oldid=852183>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Install_Arch_Linux_from_existing_Linux_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Install from SSH](<../zh-cn/Install_from_SSH.html> "Install from SSH")

本指南给出了从当前 Linux 发行版安装 Arch Linux 所需的准备步骤。 准备完成后的安装参考 [Installation guide](<../zh-cn/Installation_guide.html> "Installation guide")。 

从当前 Linux 发行版安装 Arch Linux 对以下情形有所帮助： 

  * 远程安装 Arch Linux，如一台（虚拟的）根服务器
  * 无需 LiveCD 替换当前 Linux 发行版（参见[#无 LiveCD 替换当前系统](<#%E6%97%A0_LiveCD_%E6%9B%BF%E6%8D%A2%E5%BD%93%E5%89%8D%E7%B3%BB%E7%BB%9F>)）
  * 创建基于 Arch Linux 的新 Linux 发行版或 LiveCD
  * 创建 Arch Linux 的 chroot 环境，如可为 Docker 基础容器创建
  * [为无盘机器准备 rootfs-over-NFS](</wzh/index.php?title=Diskless_network_boot_NFS_root&action=edit&redlink=1> "Diskless network boot NFS root（页面不存在）")

这些准备步骤的目的在于为搭建一个 [arch-install-scripts](<https://archlinux.org/packages/?name=arch-install-scripts>)包（如 [pacstrap(8)](<https://man.archlinux.org/man/pacstrap.8>) 和 [arch-chroot(8)](<https://man.archlinux.org/man/arch-chroot.8>)）可运行的环境。 

如果当前系统是 Arch Linux，这个目的可通过在当前系统安装 [arch-install-scripts](<https://archlinux.org/packages/?name=arch-install-scripts>)包 达成。如果当前系统不是 Arch Linux，可以构建基于 Arch Linux 的 chroot 环境。 

**注意：** 本指南要求当前系统能够运行目标 Arch Linux 构架的程序。这意味着当前系统必须是 x86_64 架构。

**警告：** 在进行每一步前，确保你理解你在干什么。这些操作很容易毁坏你的系统或造成数据丢失！

##  备份和准备

备份你的所有数据，包括邮件、网页服务器等，把所有数据都放在手边。记录下你的服务器配置、hostname 等数据。 

你可能会用到的数据： 

  * IP 地址
  * hostname(s)，（注意：根服务器可能是域名提供的一部分，在你删除 `/etc/hosts` 前先检查并备份）
  * DNS 服务器（检查 `/etc/resolv.conf`）
  * SSH 密钥（如果其它人也要用你的服务器，如果你删除了 SSH 密钥，他们就需要新的密钥了。这些密钥可能来自：Apache、邮件服务器、SSH 服务器和其它服务）
  * 硬件信息（比如网卡，参考你的 `/etc/modules.conf`）
  * 引导加载程序（Boot Loader）的配置文件。

总之，在本地备份一份原本的 `/etc` 总不会错。 

##  从一个正在运行 Arch Linux 的主机

安装 [arch-install-scripts](<https://archlinux.org/packages/?name=arch-install-scripts>)包。 

参考 [Installation guide#挂载分区](<../zh-cn/Installation_guide.html#%E6%8C%82%E8%BD%BD%E5%88%86%E5%8C%BA> "Installation guide")来挂载用来安装的文件系统根目录，以及其它必要的挂载点。如果 `/mnt` 文件夹已经被占用 , 只要新建一个文件夹，比如 `/mnt/install` 用来替代即可。 

目前，Arch Linux 可以从头安装，或者作为宿主系统的镜像，这两种选项会在下面说明。 

###  进行全新的 Arch Linux 安装

参考 [Installation guide#Installation](<../zh-cn/Installation_guide.html#Installation> "Installation guide")。 

你可以跳过 [Installation guide#选择镜像](<../zh-cn/Installation_guide.html#%E9%80%89%E6%8B%A9%E9%95%9C%E5%83%8F> "Installation guide")，因为主机中应该已经有了合适的镜像列表。 

**警告：**

pacstrap 会使用 **来自宿主机的** `/etc/pacman.conf` 的配置文件以及 pacman 钩子。参见 [archlinux/arch-install-scripts#60](<https://gitlab.archlinux.org/archlinux/arch-install-scripts/-/issues/60>)。 如果你的设置偏离了标准（例如你在你的 pacman 配置中有 `Noextract=`），这也会影响到新安装的系统。 

  * 如果需要，下载[默认的 pacman.conf](<https://gitlab.archlinux.org/archlinux/packaging/packages/pacman/-/raw/main/pacman.conf>) 并通过 _pacstrap_ 的 `-C` 选项来指定这个文件。

**提示：**

  * 要避免重新下载所有软件包，可以参考 [pacman/Tips and tricks#在网络上共享pacman缓存](<../zh-cn/Pacman/Tips_and_tricks.html#%E5%9C%A8%E7%BD%91%E7%BB%9C%E4%B8%8A%E5%85%B1%E4%BA%ABpacman%E7%BC%93%E5%AD%98> "Pacman/Tips and tricks")。或者使用 _pacstrap_ 的 `-c` 选项，来使用宿主系统上的软件包缓存。

###  创建已有的 Arch 的备份

复制宿主系统的文件系统到新分区，再做一些必要的调整，就可以备份已有的 Arch Linux。 

第一步是拷贝宿主文件到新的分区里，可以考虑使用 [Rsync#全盘系统备份](<../zh-cn/Rsync.html#%E5%85%A8%E7%9B%98%E7%B3%BB%E7%BB%9F%E5%A4%87%E4%BB%BD> "Rsync")里展示的方法。 

然后，参考 [Installation guide#配置系统](<../zh-cn/Installation_guide.html#%E9%85%8D%E7%BD%AE%E7%B3%BB%E7%BB%9F> "Installation guide")里的步骤，注意以下几点： 

  * 可以跳过 [Installation guide#时区](<../zh-cn/Installation_guide.html#%E6%97%B6%E5%8C%BA> "Installation guide")、[Installation guide#本地化](<../zh-cn/Installation_guide.html#%E6%9C%AC%E5%9C%B0%E5%8C%96> "Installation guide")和 [Installation guide#Root 密码](<../zh-cn/Installation_guide.html#Root_%E5%AF%86%E7%A0%81> "Installation guide")
  * 如果改变了文件系统，比如从 [ext4](<../zh-cn/Ext4.html> "Ext4") 改为 [Btrfs](<../zh-cn/Btrfs.html> "Btrfs")，必须进行 [Installation guide#Initramfs](<../zh-cn/Installation_guide.html#Initramfs> "Installation guide")
  * 参考 [Installation guide#安装引导程序](<../zh-cn/Installation_guide.html#%E5%AE%89%E8%A3%85%E5%BC%95%E5%AF%BC%E7%A8%8B%E5%BA%8F> "Installation guide")，务必重新安装引导程序
  * 删除 `/etc/machine-id`，并使用 [systemd-machine-id-setup(1)](<https://man.archlinux.org/man/systemd-machine-id-setup.1>) 来创建一个新的。

如果镜像 Arch 必须要使用与宿主系统不同的配置，或者要安装到不同的硬件上，考虑进行以下操作： 

  * 在进行 [Installation guide#安装引导程序](<../zh-cn/Installation_guide.html#%E5%AE%89%E8%A3%85%E5%BC%95%E5%AF%BC%E7%A8%8B%E5%BA%8F> "Installation guide")时，使用目标系统 CPU 的[微码](<../zh-cn/%E5%BE%AE%E7%A0%81.html> "Microcode")
  * 如果宿主系统上有于目标系统上不兼容的 [Xorg#配置](<../zh-cn/Xorg.html#%E9%85%8D%E7%BD%AE> "Xorg")，参考 [Moving an existing install into (or out of) a virtual machine#Disable any Xorg-related files](</wzh/index.php?title=Moving_an_existing_install_into_\(or_out_of\)_a_virtual_machine&action=edit&redlink=1> "Moving an existing install into \(or out of\) a virtual machine（页面不存在）")
  * 其它针对目标系统的配置诸如网络和音频。

##  从一个运行另一个 Linux 发行版的主机

下列是多个可以自动处理大量步骤的工具。具体方法可以参考他们各自主页的相关说明。 

  * [archstrap](<https://github.com/wick3dr0se/archstrap>) (Bash)
  * [digitalocean-debian-to-arch](<https://github.com/gh2o/digitalocean-debian-to-arch>) (需要重新分区，针对 DigitalOcean; **does not perform PGP signature verification**)
  * [image-bootstrap](<https://github.com/hartwork/image-bootstrap>) (Python; **does not perform PGP signature verification**)
  * [vps2arch](<https://gitlab.com/drizzt/vps2arch>) (Bash; **does not perform PGP signature verification**)

以下是介绍手动处理的办法，具体思路要么是直接在宿主系统上运行 [pacman](<../zh-cn/Pacman.html> "Pacman")，要么是在宿主系统里运行一个 Arch 系统，这个嵌套系统位于 chroot 中。 

###  在宿主系统上运行 pacman

[Pacman](<https://gitlab.archlinux.org/pacman/pacman>) 可以在大部分 Linux 发行版上编译运行，可以直接用来在宿主系统上创建 Arch Linux。最近的发行版上 [arch-install-scripts](<https://gitlab.archlinux.org/archlinux/arch-install-scripts>) 应该可以顺利运行。 

一些发行版官方提供 _pacman_ 和 / 或者 _arch-install-scripts_ 的软件包。截止 2020 六月，Void Linux 提供了 _pacman_ 软件包，Apline Linux 和 Fedora 提供了 _pacman_ 和 _arch-install-scripts_ 的软件包。 

###  创建 chroot

从[镜像站](<https://archlinux.org/download>)下载 bootstrap 镜像到 `/tmp`。 从[下载页](<https://archlinux.org/download/#checksums>)下载 bootstrap 的签名文件并把它放在与镜像相同的文件夹下。不要从镜像站下载它。 使用 [GnuPG 验证](<../zh-cn/GnuPG.html#Verify_a_signature> "GnuPG")。 

解压 tarball： 
    
     # tar xf _/path-to-bootstrap-image_ /archlinux-bootstrap-x86_64.tar.zst --numeric-owner
    
留意最后的 `--numeric-owner` 选项。你当前的 Linux 系统使用的 UID 和 GID 可能与 Arch Linux 不同，这个选项可以保留解压出文件的 UID 和 GID。 

然后编辑来 `/tmp/root.x86_64/etc/pacman.d/mirrorlist` 选择软件仓库服务器。 

进入 chroot： 

  * 若安装了4或更高版本的 bash，并且 _unshare_ 支持 `--fork` `--pid` 选项 (util-linux 2.24 or later): 
        
        # /tmp/root.x86_64/bin/arch-chroot /tmp/root.x86_64/

  * 若无，执行：

    # mount --bind /tmp/root.x86_64 /tmp/root.x86_64
    # cd /tmp/root.x86_64
    # cp /etc/resolv.conf etc
    # mount -t proc /proc proc
    # mount --make-rslave --rbind /sys sys
    # mount --make-rslave --rbind /dev dev
    # mount --make-rslave --rbind /run run    # （假设文件系统上存在 /run）
    # chroot /tmp/root.x86_64 /bin/bash
    
###  使用 chroot 环境

初始环境非常基础（没有 [nano](<https://archlinux.org/packages/?name=nano>)包 或者 [lvm2](<https://archlinux.org/packages/?name=lvm2>)包），因此，我们得设置好 pacman 来安装必要的软件包。 

####  初始化 pacman 密钥环

开始安装前，需要设置 pacman 密钥。执行以下命令： 
    
    # pacman-key --init
    # pacman-key --populate
    
更多请参见 [pacman/软件包签名#Initializing the keyring](<../zh-cn/Pacman/%E8%BD%AF%E4%BB%B6%E5%8C%85%E7%AD%BE%E5%90%8D.html#Initializing_the_keyring> "Pacman/软件包签名")。 

####  下载基本工具

[刷新软件包列表](<../zh-cn/%E9%95%9C%E5%83%8F%E6%BA%90.html#%E5%BC%BA%E5%88%B6_pacman_%E5%88%B7%E6%96%B0%E8%BD%AF%E4%BB%B6%E5%8C%85%E5%88%97%E8%A1%A8> "Mirrors")并[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")你需要的软件包：[base](<https://archlinux.org/packages/?name=base>)包、[base-devel](<https://archlinux.org/groups/x86_64/base-devel/>)包组、[parted](<https://archlinux.org/packages/?name=parted>)包 等等。 

[![](../File:Tango-edit-clear.png)](<../File:Tango-edit-clear.png>)**本文或本章节的语言、语法或风格需要改进。参考：[帮助:风格](<../zh-cn/Help:%E9%A3%8E%E6%A0%BC.html> "Help:风格")**

**原因：** This error is explained within [arch-chroot(8) § DESCRIPTION](<https://man.archlinux.org/man/arch-chroot.8#DESCRIPTION>), it should be linked there.（在[Talk:从现有 Linux 发行版安装 Arch Linux](<../zh-cn/Talk:%E4%BB%8E%E7%8E%B0%E6%9C%89_Linux_%E5%8F%91%E8%A1%8C%E7%89%88%E5%AE%89%E8%A3%85_Arch_Linux.html>)讨论）

**注意：** 你在用 pacman 安装软件包时，可能会遇到错误：`error: could not determine cachedir mount point /var/cache/pacman/pkg`。解决办法是在 chroot 前运行：
    
    # mount --bind directory-to-livecd-or-bootstrap directory-to-livecd-or-bootstrap

参考 [FS#46169](<https://bugs.archlinux.org/task/46169>)。

####  安装提示

请按照[Installation guide](<../zh-cn/Installation_guide.html> "Installation guide")中的[挂载分区](<../zh-cn/Installation_guide.html#%E6%8C%82%E8%BD%BD%E5%88%86%E5%8C%BA> "Installation guide")和[安装必须的软件](<../zh-cn/Installation_guide.html#%E5%AE%89%E8%A3%85%E5%BF%85%E9%9C%80%E7%9A%84%E8%BD%AF%E4%BB%B6%E5%8C%85> "Installation guide")小节进行安装。 

一些宿主系统或配置可能需要额外的步骤，参考下面的章节。 

#####  基于 Debian 的当前系统

######  /dev/shm

在基于 Debian 的当前系统上，`pacstrap` 会发生以下错误： 
    
    # pacstrap -K /mnt base
    
    ==> Creating install root at /mnt
    mount: mount point /mnt/dev/shm is a symbolic link to nowhere
    ==> ERROR: failed to setup API filesystems in new root
    
Debian 中，`/dev/shm` 指向 `/run/shm`。而在基于 Arch 的 chroot 中，`/run/shm` 并不存在，因而链接失效。创建 /run/shm 目录可修复此错误： 
    
    # mkdir /run/shm
    
#####  基于Fedora的当前系统

在基于 Fedora 的宿主系统和 live USBs 上时，当你用 _genfstab_ 生成你的 [fstab](<../zh-cn/Fstab.html> "Fstab") 你可能会遇到问题。移除重复的入口和 `seclabel` 选项（如果有），因为它们是针对 Fedora 的。 

##  重启前要检查的

为得到一个成功的安装，重启前请再次检查一些你的安装的细节。 首先 chroot 到你的新系统然后: 

  * [创建一个用户并设置密码](<../zh-cn/Users_and_groups.html#User_management> "Users and groups"), 使得你可以通过 _ssh_ 登录。这很重要因为从 OpenSSH-7.1p2 开始登录 root 被默认禁用。
  * [设置 root 用户密码](<../zh-cn/Installation_guide.html#Root_password> "Installation guide") 以便之后你可以通过 _su_ 切换至 root。
  * [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装")一个 [ssh](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "安全外壳协议") 实现并[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")服务端实例使得它开机自动启动。
  * 设置[网络配置](<../zh-cn/Network_configuration.html> "Network configuration")使得你在启动后能使用网络。
  * 设置 [boot loader](<../zh-cn/Boot_loader.html> "Boot loader") 并配置它使用你之前所挪用的交换分区做为根分区 。 你可能还想让你的 boot loader 能够启动到你的旧系统；对此可复用已存在的 `/boot` 分区来达成这个目的。

##  无 LiveCD 替换当前系统

在硬盘上划分出 ~700 MiB 的空闲空间，如分割交换分区。你可以禁用交换分区并用省下的空间建立新系统。 

###  把旧的交换分区设为新的根分区

检查 `cfdisk`、`/proc/swaps` 或者 `/etc/fstab` 来找到你的交换分区。假设你的硬盘位于 `sda _X_`（` _X_` 是数字）。 

执行下面的操作： 

禁用交换分区： 
    
    # swapoff /dev/sda _X_
    
在上面建立新的文件系统 
    
    # fdisk /dev/sda
    (设置 /dev/sda _X_ ID 为 "Linux" - Hex 83)
    # mke2fs -j /dev/sda _X_
    
创建一个新目录来挂载它 
    
    # mkdir /mnt/newsys
    
最后，挂载新目录并安装过渡系统。 
    
    # mount -t ext4 /dev/sda _X_ /mnt/newsys
    
###  安装

[安装必要软件包](<../zh-cn/Installation_guide.html#Install_essential_packages> "Installation guide")和其它让系统联网和在临时文件系统下运行的必需软件包。注意 ~700 MB 的空间限制。当使用 _pacstrap_ 安装时，考虑加上 `-c` 选项来避免占满宝贵的空间。 

一旦完成安装，修复引导器配置，然后重启进入到新系统并[rsync 整个系统](<../zh-cn/Rsync.html#%E5%85%A8%E7%9B%98%E7%B3%BB%E7%BB%9F%E5%A4%87%E4%BB%BD> "Rsync")至主分区。 
