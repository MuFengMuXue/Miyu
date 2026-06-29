相关文章

  * [ZFS](<../zh-cn/ZFS.html> "ZFS")
  * [Experimenting with ZFS](</wzh/index.php?title=Experimenting_with_ZFS&action=edit&redlink=1> "Experimenting with ZFS（页面不存在）")

**翻译状态：**

  * 本文（或部分内容）译自 [Install Arch Linux on ZFS](<https://wiki.archlinux.org/title/Install_Arch_Linux_on_ZFS> "arch:Install Arch Linux on ZFS")，最近一次同步于 2025-12-21，若英文版本有所[更改](<https://wiki.archlinux.org/title/Install_Arch_Linux_on_ZFS?diff=0&oldid=858201>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Install_Arch_Linux_on_ZFS_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

这篇文章详细描述了将 Arch Linux 安装在 ZFS 文件系统上所需的步骤。 

**注意：** 盲目地照搬这篇教程上的操作是行不通的。您有必要花时间了解操作系统的启动过程以及创建存储池和数据集的过程。下面是一些可能帮助到您的链接： 

  * [FreeBSD 手册 - ZFS 章节](<https://www.freebsd.org/doc/handbook/zfs.html>)
  * [ZFSOnLinux wiki](<https://github.com/zfsonlinux/zfs/wiki>)
  * [OpenZFS wiki](<http://open-zfs.org/wiki/System_Administration>)
  * [Aaron Toponce 的在 Debian GNU/Linux 上安装 ZFS 的教程](<https://pthree.org/2012/04/17/install-zfs-on-debian-gnulinux/>)
  * [OpenZFS 的 Arch Linux 文档](<https://openzfs.github.io/openzfs-docs/Getting%20Started/Arch%20Linux/>)

由于 ZFS 不是 Linux 的原生文件系统（例如：不包含在主线内核之内）且 Arch Linux 是一个滚动更新发行版，总有些时候外部仓库内的对应一定内核版本的内核模块软件包版本会稍落后于 Arch 仓库中的版本，这有时会导致 ZFS 模块（或其 dkms 变种包）在最新版本的内核上无法编译。如果您想要一直使用最新版本的内核的话，将 Arch 安装在 ZFS 上可能并不是很理想。 

可能的解决方案见 [ZFS#安装](<../zh-cn/ZFS.html#%E5%AE%89%E8%A3%85> "ZFS")。 

##  安装

要在 ZFS 上安装 Arch Linux，您需要使用带有 ZFS 内核模块的安装介质。您可以使用现有的 Arch Linux; 或者，如果您没有现有的 Arch Linux 系统，您也可以使用启用了“共享文件夹”的虚拟机软件，如 VirtualBox 或 VMWare。 

###  在自定义 archiso 安装介质中嵌入 ZFS 模块

要构建自定义的ISO， [安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") [archiso](<https://archlinux.org/packages/?name=archiso>)包。依照 [archiso#准备自定义配置文件](<../zh-cn/Archiso.html#%E5%87%86%E5%A4%87%E8%87%AA%E5%AE%9A%E4%B9%89%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6> "Archiso") 来准备一个自定义的配置文件（下文中以 `archlive` 为例）。 

首先，[编辑](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Edit") 软件包列表 `packages.x86_64` 并在其中加入 [linux-lts](<https://archlinux.org/packages/?name=linux-lts>)包 内核与下列 ZFS 软件包： 
    
    packages.x86_64
    
    ...
    linux-lts
    linux-lts-headers
    libunwind
    zfs-utils
    zfs-dkms
    
请确保从列表中移除 `linux` 与 `broadcom-wl` (后者会拉取 [linux](<https://archlinux.org/packages/?name=linux>)包 包) 。 

您还需要编辑 `pacman.conf` 并在其中加入： 
    
    ...
    [archzfs]
    SigLevel = TrustAll Optional
    Server = https://github.com/archzfs/archzfs/releases/download/experimental
    
您还需要编辑以下文件来将 `vmlinuz-linux` 与 `initramfs-linux.img` 的条目改为 `vmlinuz-linux-lts` 和 `initramfs-linux-lts.img`: 
    
    archlive/airootfs/etc/mkinitcpio.d/linux.preset
    archlive/efiboot/loader/entries/01-archiso-linux.conf
    archlive/efiboot/loader/entries/02-archiso-speech-linux.conf
    archlive/syslinux/archiso_pxe-linux.cfg
    archlive/syslinux/archiso_sys-linux.cfg
    archlive/grub/loopback.cfg
    archlive/grub/grub.cfg
    
**警告：** 如果您未编辑这些文件，您的 ISO 将 **无法** 启动。

接下来我们要创建 `isobuild` 与 `work` 两个目录来开始构建 ISO 镜像: 
    
    # mkdir isobuild
    # mkarchiso -v -r -w /tmp/archiso-tmp -o isobuild ~/archlive
    
现在，您的 `archlive/isobuild` 目录下应该已经出现了`archlinux-_YYYY_._MM_._DD_.x86_64.iso`。 

请将该文件烧录至您选择使用的安装介质。 

**注意：**

  * 如果在系统更新后，`zpool status -v` 的输出显示您的存储池需要升级以支持新的特性，您可能需要重新制作上述安装介质。

  * 在实际安装时，您应该使用 [linux-lts](<https://archlinux.org/packages/?name=linux-lts>)包 与 [linux-lts-headers](<https://archlinux.org/packages/?name=linux-lts-headers>)包 来保证最大兼容性。同时，您应从[非官方的 archzfs 仓库](<../zh-cn/%E9%9D%9E%E5%AE%98%E6%96%B9%E7%94%A8%E6%88%B7%E4%BB%93%E5%BA%93.html#archzfs> "非官方用户仓库")而非 AUR 获取 _zfs-utils_ 与 _zfs-dkms_ 的更新。如果您选择使用 AUR 中的版本，则可能出现当前的主线或 zen 内核不被 ZFS 支持的情况，从而导致您的系统无法启动。因此，在实际操作时，强烈建议您使用 linux-lts 内核。

**警告：** 请勿分发您制作的自定义 ISO，这样做将会违反 GPL 与 CDDL 许可证！

请确保先在虚拟机中测试您的 ISO。只需运行： 
    
    # modprobe zfs
    # zpool status
    
如果命令执行失败，则您的 ZFS 模块并未成功构建，您需要重新尝试。 

##  对目标磁盘驱动器进行分区

ZFS 支持 GUID 分区图与主启动记录分区表。要决定使用哪种分区图，请参考[分区#选择 GPT 还是 MBR](<../zh-cn/%E5%88%86%E5%8C%BA.html#%E9%80%89%E6%8B%A9_GPT_%E8%BF%98%E6%98%AF_MBR> "分区")。 

ZFS 会管理自己的分区，所以只需创建一个最简单的分区类型即可。创建 ZFS 文件系统的分区类型应为类型 `bf00` ，或“ Solaris 根目录分区”。 

###  分区类型

虽然您在一些使用主启动记录的旧式电脑上也能创建出可以启动的 ZFS 根分区，但由于主启动记录与 GUID 分区图的差异，并不建议以这种方式使用 ZFS。为了保证兼容性并避免启动加载器出现问题，建议使用一个单独的 /boot 分区。 

在 BIOS（或一台以 Legacy 模式启动的）设备上使用 GUID 分区图与 [GRUB](<../zh-cn/GRUB.html> "GRUB") 启动引导器的示例： 
    
    Part     Size   Type
    ----     ----   -------------------------
       1       2M   BIOS boot partition (ef02)
       2       1G   Linux Partition (8300)
       3     XXXG   Solaris Root (bf00)
    
在使用[Grub](</wzh/index.php?title=Grub&action=edit&redlink=1> "Grub（页面不存在）") 与 [rEFInd](<../zh-cn/REFInd.html> "REFInd") 时可使用以下这种分区形式。由于其较好的兼容性，这也是作者推荐的分区形式。 
    
    Part     Size   Type
    ----     ----   -------------------------
       1       1G   EFI System Partition (ef00)
       2     XXXG   Solaris Root (bf00)
    
You can choose to separate Linux swap partition, or using a zvol, see [ZFS#Swap volume](<../zh-cn/ZFS.html#Swap_volume> "ZFS"), as swap. 

If you wish to create a traditional swap partition, see [Partitioning#Example layouts](<../zh-cn/%E5%88%86%E5%8C%BA.html#Example_layouts> "Partitioning"). 

##  格式化目标磁盘驱动器

如果您已为启动引导分区以及非 ZFS 文件系统创建了合适的分区，那么现在请将这些分区格式化。不要对刚创建的 Solaris 根分区以及您的 BIOS 启动分区做任何操作。Solaris 根分区将由 ZFS 管理，而 BIOS 启动分区则会由您的启动引导器管理。 

##  设置 ZFS 文件系统

首先，确认 ZFS 内核模块已经被加载， 
    
    # modprobe zfs
    
###  创建根存储池

创建存储池并设置好数据集的默认选项。存储池上新创建的任何数据集都会保留这个存储池创建时使用 `-O` 设定的选项。默认选项在[在 ZFS 上安装 Debian Buster. 第二步: 磁盘格式化](<https://openzfs.github.io/openzfs-docs/Getting%20Started/Debian/Debian%20Buster%20Root%20on%20ZFS.html#step-2-disk-formatting>)中有详细说明。 

**注意：** 物理扇区大小为512字节的磁盘驱动器应使用 `-o ashift=9` 参数，而物理扇区大小为4096字节的磁盘驱动器应使用 `-o ashift=12` 参数。要获得每个 SCSI/SATA 磁盘驱动器的物理扇区大小，可以运行 `lsblk -S -o NAME,PHY-SEC`。如果想查看所有设备的物理扇区大小，可从命令中删去 `-S`。若使用 NVMe 驱动器，使用 `nvme id-ns /dev/nvmeXnY -H | grep "LBA Format"` 来获取正在使用的逻辑块地址。大部分 NVMe 驱动器使用512字节的逻辑块大小，见 [OpenZFS: NVMe low level formatting](<https://openzfs.github.io/openzfs-docs/Performance%20and%20Tuning/Hardware.html#nvme-low-level-formatting>) 以将其大小改为4096字节。

**警告：** 应始终注意现代的大部分设备的物理扇区大小为4096字节，但有些设备会将自己的物理扇区大小报告为512字节，尤其是固态驱动器（SSD）。即使在报告扇区大小为512字节、实际物理扇区大小为4096字节的设备上选择 `ashift=9` 也**一定会** 导致严重的性能下降。在物理扇区大小为512字节的设备上选择 `ashift=12` 不会导致性能下降，但可能使磁盘可用容量减少。如果您不确定的话，对于现代设备，应使用 `ashift=12`，或者您可以搜索您设备对应的正确值。对于有关的讨论，参见 [OpenZFS issue #967](<https://github.com/openzfs/zfs/issues/967>) ；对设置较高的 ashift 值可能出现的问题，见 [OpenZFS issue #2497](<https://github.com/openzfs/zfs/issues/2497>) 。 

**警告：** In this next section, using a standard device name such _/dev/nvme0n1p2_ instead of _/dev/disk/by-id/ <device number>_ to create the zpool, may lead to import problems. If you want to learn your devices correct _by-id_ prior to this section, run: 

`ls -lh /dev/disk/by-id/`

and take note of the correct _by-id_ value to use rather than the standard device naming scheme such as: 

`lrwxrwxrwx 1 root root 9 Aug 12 16:26 ata-ST3000DM001-9YN166_S1F0JKRR -> ../../sdc`
    
    # zpool create -f -o ashift=12         \
                 -O acltype=posixacl       \
                 -O relatime=on            \
                 -O xattr=sa               \
                 -O dnodesize=auto         \
                 -O normalization=formD    \
                 -O mountpoint=none        \
                 -O canmount=off           \
                 -O devices=off            \
                 -R /mnt                   \
                 zroot /dev/disk/by-id/_id-to-partition-partx_

####  压缩与原生加密

以下命令创建的存储池会在所有数据集上默认启用压缩与原生加密： 
    
    # zpool create -f -o ashift=12         \
                 -O acltype=posixacl       \
                 -O relatime=on            \
                 -O xattr=sa               \
                 -O dnodesize=auto         \
                 -O normalization=formD    \
                 -O mountpoint=none        \
                 -O canmount=off           \
                 -O devices=off            \
                 -R /mnt                   \
                 -O compression=lz4        \
                 -O encryption=aes-256-gcm \
                 -O keyformat=passphrase   \
                 -O keylocation=prompt     \
                 zroot /dev/disk/by-id/_id-to-partition-partx_

The options after `-O` control ZFS behavior. A detailed explanation of them can be found in the [zfsprops(7)](<https://openzfs.github.io/openzfs-docs/man/master/7/zfsprops.7.html>) man page. 

**警告：**

  * 使用 ZFS 时应始终使用设备的 by-id 名称，否则导入存储池时会发生错误。
  * 除使用 by-id 名称外，也可以考虑使用 by-partuuid 或 by-uuid名称，因为即使一个内置磁驱动器被移入USB移动硬盘盒，这些名称的值也不会发生改变，反之亦然。（这仅当 ZFS 在磁盘上的某个分区中才有效，若 ZFS 占据整个磁盘则无效）

###  创建您的数据集

ZFS 使用数据集的概念来管理您的存储，而非使用传统的磁盘分区。与磁盘分区不同，数据集没有固定的大小， 每个数据集也可以有各自不同的属性，例如压缩。普通的 ZFS 数据集由 ZFS 自动挂载，而传统的数据集则需由 fstab 或 使用 mount 命令挂载。 

ZFS 最实用的功能之一便是启动环境。启动环境使您可以创建系统的可引导快照，您也可以通过简单地重启到某启动环境来将整个系统回滚到那个快照。这使得系统更新变得更加安全，对软件开发与测试来讲也十分有用。要使用如 [beadm](<https://github.com/b333z/beadm>), [zectl](<https://aur.archlinux.org/packages/zectl/>)AUR (用于 systemd-boot), or [zedenv](<https://aur.archlinux.org/packages/zedenv/>)AUR (用于 GRUB) 等的启动环境管理器来管理启动环境，您的数据集必须有正确的配置。其关键是将您存放数据的目录 (如 `/home`) 与系统数据分别放在相互独立的不同数据集中，且不要在存储池根目录中存放数据，因为放在存储池根目录的数据以后将不能被移动。 

您总是至少应该为您的根目录创建一个数据集，且多数情况下您也会想要把 `/home` 存放在一个单独的数据集中。您也可以自行选择是否要无视启动环境而始终保留完整的日志文件。如果您使用的某些软件会在 `/home` 之外存放数据 (如数据库服务器)，您应整理数据集的结构，使得这些软件的数据目录与根目录数据集分离开来。 

以下的示例命令会创建一个只分根目录数据集与 `/home` 数据集的最基本可用于启动环境使用的配置。数据集使用其所在的存储池在[创建](<../zh-cn/Install_Arch_Linux_on_ZFS_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E5%88%9B%E5%BB%BA%E6%A0%B9%E5%AD%98%E5%82%A8%E6%B1%A0> "Install Arch Linux on ZFS \(简体中文\)")时设定的默认选项。 
    
    # zfs create -o mountpoint=none zroot/data
    # zfs create -o mountpoint=none zroot/ROOT
    # zfs create -o mountpoint=/ -o canmount=noauto zroot/ROOT/default
    # zfs create -o mountpoint=/home zroot/data/home
    
创建根目录数据集时您也可以不指定挂载点，毕竟无论如何 GRUB 启动引导器会将其挂载至 / 。这也使得您可以通过克隆旧版数据集并将其放入 GRUB 启动菜单来直接从旧版的根目录启动。这种情况下，您可以使用以下命令来创建您的根目录数据集： 
    
    # zfs create -o mountpoint=/roots/default zroot/ROOT/default
    
您可以将 `/root` 存储在您的 `zroot/data/home` 数据集中。 
    
    # zfs create -o mountpoint=/root zroot/data/home/root
    
####  系统数据集

为系统目录创建数据集时，使用`canmount=off`选项。 

示例请参见 [Debian-Buster-Root-on-ZFS#step-3-system-installation](<https://openzfs.github.io/openzfs-docs/Getting%20Started/Debian/Debian%20Buster%20Root%20on%20ZFS.html#step-3-system-installation>)。 

**注意：** 若要将如 `zroot/var/log` 的数据集挂载至 `/var/log`，应考虑使用 _zfs-mount-generator_ 而非 `zfs-mount.service`。这会修复文件系统挂载顺序，在 [这里](<https://openzfs.github.io/openzfs-docs/Getting%20Started/Debian/Debian%20Buster%20Root%20on%20ZFS.html#step-5-grub-installation>) 有详细介绍。
    
     # zfs create -o mountpoint=/var -o canmount=off                 zroot/var
    # zfs create                                                    zroot/var/log
    # zfs create -o mountpoint=/var/log/journal -o acltype=posixacl zroot/var/log/journal
    # zfs create -o mountpoint=/var/lib -o canmount=off             zroot/var/lib
    # zfs create                                                    zroot/var/lib/libvirt
    # zfs create                                                    zroot/var/lib/docker
    
**注意：** systemd-journald requires a mountpoint to be created otherwise systemd-journald.service will fail at boot [systemd#systemd-tmpfiles-setup.service fails to start at boot](<../zh-cn/Systemd.html#systemd-tmpfiles-setup.service_fails_to_start_at_boot> "Systemd")

###  导出并导入您的存储池

要验证您的设置，将您所有的 ZFS 存储池先导出后再重新导入。 

**警告：** 不要跳过这一步，否则您再导入存储池时必须使用 `-f` 参数。这会使导入的存储池卸载。

**注意：** 如果您使用交换分区的话，这一步可能会失败。您需要先使用 _swapoff_ 命令将其关闭。
    
    # zpool export zroot
    # zpool import -d /dev/disk/by-id -R /mnt zroot -N
    
**注意：**`-d` 并不是设备的实际 ID，而是包含着软链接的 `/dev/by-id` 目录。 

如果这个命令执行失败并且您被要求使用数字 ID 来导入某个存储池，运行 `zpool import` 来找到您存储池的 ID，然后使用类似下方的命令导入存储池： 
    
    # zpool import 9876543212345678910 (您的设备的 ID) -R /mnt zroot
    
如果您启用了原生加密选项，先加载 ZFS 密钥。 
    
    # zfs load-key zroot
    
由于根目录数据集使用 `canmount=noauto` 参数，您需要先将其手动挂载，然后再挂载其他数据集。 
    
    # zfs mount zroot/ROOT/default
    # zfs mount -a
    
现在 ZFS 文件系统已准备完毕以待使用。 

###  配置根目录文件系统

如果您使用了传统类型的数据集，则您需要将其写入 `/etc/fstab`。 

为根目录所在的子文件系统设置 bootfs（启动文件系统），以便启动引导加载器找到操作系统。 
    
    # zpool set bootfs=zroot/ROOT/default zroot
    
如果您还没有 `/etc/zfs/zpool.cache`，请手动创建： 
    
    # zpool set cachefile=/etc/zfs/zpool.cache zroot
    
切记要将 `zpool.cache` 文件放入您的新系统中。稍后 ZFS 守护进程启动时需要这个文件。 
    
    # mkdir -p /mnt/etc/zfs
    # cp /etc/zfs/zpool.cache /mnt/etc/zfs/zpool.cache
    
##  安装并配置 Arch Linux

按照[安装指南](<../zh-cn/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97.html> "安装指南")安装系统。若有涉及 ZFSonLinux 所需的特殊操作，将会在此列出。 

  * 首先使用 mount 命令挂载所有的传统类型数据集以及非 ZFS 的引导或系统分区。

  * 安装基本系统。

**注意：** You may wish to opt for [linux-lts](<https://archlinux.org/packages/?name=linux-lts>)包 for your kernel of choice during the `pacstrap` portion. Make sure to also add [libunwind](<https://archlinux.org/packages/?name=libunwind>)包 to pacstrap to resolve a dependency for [zfs-utils](<https://aur.archlinux.org/packages/zfs-utils/>)AUR.

  * [安装指南#生成 fstab 文件](<../zh-cn/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97.html#%E7%94%9F%E6%88%90_fstab_%E6%96%87%E4%BB%B6> "安装指南")中所描述的方式对 ZFS 来说绝非必要。通常 ZFS 会自行挂载自己的分区，所以除非用户使用了传统型数据集，`fstab` 文件中不需要任何有关 ZFS 的部分。 要为文件系统生成 `fstab`，运行：

    # genfstab -U -p /mnt >> /mnt/etc/fstab
    
  * 依照[安装指南#chroot 到新安装的系统](<../zh-cn/%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97.html#chroot_%E5%88%B0%E6%96%B0%E5%AE%89%E8%A3%85%E7%9A%84%E7%B3%BB%E7%BB%9F> "安装指南")中的方法将根目录切换至新安装的系统内。

    # arch-chroot /mnt
    
  * 编辑 `/etc/fstab`：

**注意：**

  * 如果您选择为系统目录创建传统数据集，将其在 `fstab` 中保留。
  * 将除交换空间与 EFI 系统分区以外的所有非传统型数据集注释掉。可以使用较简单的 `/dev/zvol/zroot/swap` 来取代交换空间的 UUID。

  * 在更新 ramdisk 并启用 ZFS 支持前，您需要在 `/etc/pacman.conf` 中加入 [Arch ZFS](<../zh-cn/Unofficial_user_repositories.html#archzfs> "Unofficial user repositories") 仓库，将其[签名](</wzh/index.php?title=Package_signing&action=edit&redlink=1> "Package signing（页面不存在）")并在 arch-chroot 环境下[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") [zfs-dkms](<https://aur.archlinux.org/packages/zfs-dkms/>)AUR 和 [zfs-utils](<https://aur.archlinux.org/packages/zfs-utils/>)AUR。

**注意：** For simplicity, and better compatibility, this guide only recommends using the [zfs-dkms](<https://aur.archlinux.org/packages/zfs-dkms/>)AUR package for usage with [linux-lts](<https://archlinux.org/packages/?name=linux-lts>)包.

  * 创建初始 ramdisk 前，先编辑 `/etc/mkinitcpio.conf`，并将 `zfs` 加至 `MODULES`:

    MODULES=(zfs)
    
接下来在 `HOOKS` 中将 `zfs` 加至 filesystems 前。同时也应把 `keyboard` hook 移动至 `zfs` 前，这样如果出现问题，您仍可在终端中输入。若您不使用 Ext3 或 Ext4，您也可以移除 fsck。您的 `HOOKS` 一行看起来应类似如下示例： 
    
    HOOKS=(base udev autodetect microcode modconf kms keyboard keymap consolefont block zfs filesystems)
    
**警告：** Recent installations of Arch Linux uses a [systemd initramfs](<../zh-cn/Mkinitcpio.html> "Mkinitcpio"). The ZFS hook provided by [zfs-utils](<https://aur.archlinux.org/packages/zfs-utils/>)AUR is only compatible with busybox-based initramfs images. Unless you plan to use a different ZFS hook compatible with systemd-based initramfs images, **please make sure that you are using a busybox-based initramfs by putting`base udev` at the beginning of the `HOOKS` array instead of `systemd`.**

  * [重新生成 initramfs](<../zh-cn/Regenerate_the_initramfs.html> "Regenerate the initramfs")。

##  安装并配置启动引导加载器

  * Add ZFS to your kernel command line

You can now set up your [boot loader](<../zh-cn/Boot_loader.html> "Boot loader"). You also need to add a [kernel parameter](<../zh-cn/Kernel_parameter.html> "Kernel parameter") to make ZFS bootable: 
    
    root=ZFS=zroot/ROOT/default rw
    
##  配置 systemd ZFS 挂载

要确保您的系统能够正常地重新启动，您需要启用 `zfs.target` 以便自动挂载存储池与生成 hostid。 

**注意：**

  * 这一节内容的前提是假设您仍在 `arch-chroot` 环境中。
  * Usage of zpool.cache is still required by zfs-utils to achieve a bootable system, although zpool.cache has been considered a candidate for deprecation [See: <https://github.com/openzfs/zfs/issues/1035>], however at this time, it is still the default and recommended method to achieving a bootable system.

分别为每个您想要自动挂载的存储池执行： 
    
    # zpool set cachefile=/etc/zfs/zpool.cache _pool（存储池名）_
    
[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") `zfs.target`

要在系统启动时自动挂载 ZFS 存储池，您需要[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable") `zfs-import-cache.service`、`zfs-mount.service` 与 `zfs-import.target`。 

当根目录文件系统为 ZFS 时，挂载根文件系统的过程中设备的 hostid 将不可用。对此有两个解决方案。 您可以将您的 spl hostid 写入启动引导器的启动[内核参数](<../zh-cn/Kernel_parameters.html> "Kernel parameters")中。例如向内核参数中加入 `spl.spl_hostid=0x00bab10c`。要获取您的 hostid 数字，运行 `hostid` 命令。 

另一个（建议的）解决方案是在 `/etc/hostid` 内写入一个 hostid ，然后重新生成 initramfs，这个过程中您的 hostid 将会被复制到 initramfs 映像中。要安全写入 hostid 文件，您需要运行 `zgenhostid` 命令。 

要使用 libc 生成的 hostid（建议的操作）： 
    
    # zgenhostid $(hostid)
    
要使用自定义的 hostid，运行以下命令。注意，hostid 必须是8个字符的十六进制数字。 
    
    # zgenhostid deadbeef
    
要让 zgenhostid 工具生成一个 hostid ： 
    
    # zgenhostid
    
完成后别忘了[重新生成 initramfs](<../zh-cn/Regenerate_the_initramfs.html> "Regenerate the initramfs")。 

##  卸载文件系统并重新启动

我们离成功不远了！如果您使用传统类型的启动引导分区，先运行： 
    
    # umount /mnt/boot 
    
如果未使用传统的单独引导分区，应直接运行： 
    
    # zfs umount -a
    # zfs umount zroot/ROOT/default
    # zpool export zroot
    
现在，重新启动系统。 

**警告：** 如果您没有正确将存储池导出，重新启动后 ZFS 将拒绝在 ramdisk 环境中导入存储池，从而使您卡在 busybox 终端界面。

###  从 USB 存储设备加载密钥

可以将密钥存储在 USB 存储设备上并在启动时加载： 

在 USB 存储介质的初始字节处存储密钥： 
    
    # dd if=_your_password_file (您的密钥文件)_ bs=32 count=1 of=/dev/disk/by-id/_usb_stick (USB 存储设备)_
    
要创建 ZFS 分区，您可以使用上文所述的输入密钥的方式，或直接使用 [dd](<../zh-cn/Dd.html> "Dd") 命令配合管道写入 USB 存储设备中存储的密钥： 
    
    # dd if=/dev/disk/by-id/_usb_stick_ bs=32 count=1 | zfs create -o encryption=on -o keyformat=_passphrase_ zroot/ROOT
    
下一步就要更改 zfs hook。zfs 默认会询问密钥。您需要将获取密钥的方式改为通过从您存放着密钥的 USB 设备中 dd 来获取。要达成这个目的，将 `/usr/lib/initcpio/hooks/zfs` 中的以下行： 
    
    # ! eval zfs load-key "${encryptionroot}"; do
    
改为： 
    
    # ! eval dd if=/dev/disk/by-id/_usb_stick_ bs=32 count=1 | zfs load-key "${encryptionroot}"; do
    
您刚刚更改了您的 zfs hook，所以不要忘记[重新生成 initramfs](<../zh-cn/Regenerate_the_initramfs.html> "Regenerate the initramfs")。现在 zfs 应该能在启动时从您的 USB 设备中加载密钥。 

##  故障排除

###  系统因 "无法导入 zroot ：存储池不存在（cannot import zroot: no such pool available）" 而无法启动

您可以尝试以下步骤，看看是否有帮助。 

  * 使用 [archzfs 仓库](<../zh-cn/Unofficial_user_repositories.html#archzfs> "Unofficial user repositories")中提供的内核模块，不要使用 dkms 版本。您可以在成功启动后再改为使用 dkms 变种。
  * 移除 `/etc/zfs/zpool.cache` 并运行：

    # zpool set cachefile=none zroot

  * 移除 `/etc/hostid`。
  * [重新生成 initramfs](<../zh-cn/Regenerate_the_initramfs.html> "Regenerate the initramfs")。

###  Zpool refuses to export saying it's busy

Arch-chroot will mount specific kernelspace file systems in the system. If these are not unmounted, the zpool may refuse to dismount properly. If this happens, remount the ZFS partition and run `findmnt -R /mnt`

Then run `umount -f _/path/to/partition_` against the partition still mounted. 

This should allow the zpool to export. 

##  另请参阅

  * [如何在原生 ZFS 根目录上安装 Ubuntu](<https://github.com/dajhorn/pkg-zfs/wiki/HOWTO-install-Ubuntu-to-a-Native-ZFS-Root-Filesystem>)
  * [ZFS 备忘录](<https://lildude.co.uk/zfs-cheatsheet>)
  * [Funtoo 的 ZFS 安装指南](<https://www.funtoo.org/ZFS_Install_Guide> "funtoo:ZFS Install Guide")
  * [在 Arch Linux 上使用 ZFS 的参考教程](<https://kiljan.org/2018/09/23/a-reference-guide-to-zfs-on-arch-linux/>)
  * [Arch Linux On Zfs ](<https://ramsdenj.com/2016/06/23/arch-linux-on-zfs-part-2-installation.html>)
  * [Youtube: Open-ZFS Bootcamp](<https://www.youtube.com/watch?v=mLbtJQmfumI>)
