**翻译状态：**

  * 本文（或部分内容）译自 [EFI system partition](<https://wiki.archlinux.org/title/EFI_system_partition> "arch:EFI system partition")，最近一次同步于 2025-01-22，若英文版本有所[更改](<https://wiki.archlinux.org/title/EFI_system_partition?diff=0&oldid=824024>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/EFI_system_partition_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Unified Extensible Firmware Interface](<../zh-cn/Unified_Extensible_Firmware_Interface.html> "Unified Extensible Firmware Interface")
  * [引导加载程序](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F> "引导加载程序")

[EFI 系统分区](<https://en.wikipedia.org/wiki/EFI_system_partition> "wikipedia:EFI system partition")（也称为 ESP）是一个与操作系统无关的分区，其中存储了由 UEFI 固件启动的 UEFI 引导加载器、应用程序和驱动，是 UEFI 启动所必须的。 

##  检查现有的分区

如果你正将 Arch Linux 安装到支持 UEFI 且已安装操作系统的计算机上，例如与 [Windows](<../zh-cn/Dual_boot_with_Windows.html> "Dual boot with Windows") 10 双启动，那么你很可能已有 EFI 系统分区。 

要查看磁盘分区表和系统分区，以 root 的身份对你想要启动的磁盘使用 [fdisk](<../zh-cn/Fdisk.html> "Fdisk")： 
    
    # fdisk -l /dev/sd _x_
    
命令将返回： 

  * 磁盘的分区表：如果分区表是 [GPT](<../zh-cn/%E5%88%86%E5%8C%BA.html#GUID_%E5%88%86%E5%8C%BA%E8%A1%A8> "GPT")，则会显示 `Disklabel type: gpt`；如果是 [MBR](<../zh-cn/%E5%88%86%E5%8C%BA.html#%E4%B8%BB%E5%BC%95%E5%AF%BC%E8%AE%B0%E5%BD%95> "MBR")，则会显示 `Disklabel type: dos`。
  * 磁盘上分区的列表：在列表中搜索 EFI 系统分区，它通常大小不小于 100 MiB，且类型为 `EFI System` 或 `EFI (FAT-12/16/32)`。要确认这个分区是 ESP，[mount](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html#%E6%8C%82%E8%BD%BD%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "Mount") 它，然后看看是否包含一个名为 `EFI` 的目录，如果有，那这肯定就是 ESP。

**提示：** 要判断是 FAT12、FAT16 还是 FAT32 文件系统，参阅 [FAT#检测FAT类型](<../zh-cn/FAT.html#%E6%A3%80%E6%B5%8BFAT%E7%B1%BB%E5%9E%8B> "FAT")。

**警告：** 双启动时不要重新格式化 ESP，因为它可能包含启动其他操作系统所需的文件。

如果你找到了现有的 EFI 系统分区，前往[#挂载分区](<#%E6%8C%82%E8%BD%BD%E5%88%86%E5%8C%BA>)，否则，你将需要创建一个，前往[#创建分区](<#%E5%88%9B%E5%BB%BA%E5%88%86%E5%8C%BA>)。 

##  创建分区

下两节介绍如何创建 EFI 系统分区（ESP）。 

**警告：** EFI 系统分区必须是磁盘主要分区表上的物理分区，不能处于 LVM 或软件 RAID 等等之下。

分区大小应足以储存启动加载器和启动所需要的其他文件。 

推荐创建1 GiB大小的EFI系统分区以确保其提供足够的空间存放多个内核或[统一内核镜像](<../zh-cn/%E7%BB%9F%E4%B8%80%E5%86%85%E6%A0%B8%E6%98%A0%E5%83%8F.html> "统一内核镜像")、引导加载器、固件升级文件以及任何其他操作系统或OEM文件。如果还有疑虑，**4 GiB** 应该足够任何人使用，比如有些工具像[Limine 启动引导器带有用于Btrfs的Snapper集成](</wzh/index.php?title=Limine_%E5%90%AF%E5%8A%A8%E5%BC%95%E5%AF%BC%E5%99%A8%E5%B8%A6%E6%9C%89%E7%94%A8%E4%BA%8EBtrfs%E7%9A%84Snapper%E9%9B%86%E6%88%90&action=edit&redlink=1> "Limine 启动引导器带有用于Btrfs的Snapper集成（页面不存在）")（英语：[Limine#Snapper snapshot integration for Btrfs](<https://wiki.archlinux.org/title/Limine#Snapper_snapshot_integration_for_Btrfs> "en:Limine")），支持创建多个可启动的快照。 

**注意：** 当然也可以使用一个较小的分区，但要注意潜在的兼容问题： 

  * 对于早期和/或古怪的 UEFI 实现，可能最少需要 512 MiB。[[1]](<https://www.rodsbooks.com/efi-bootloaders/principles.html>)
  * 如果你打算把分区挂载到[/boot](<../zh-cn/%E5%88%86%E5%8C%BA.html#/boot> "分区")并且只安装一个内核，那么400 MiB足够使用。
  * 如果是[Arch + Windows 双系统](<../zh-cn/Arch_+_Windows_%E5%8F%8C%E7%B3%BB%E7%BB%9F.html> "Arch + Windows 双系统")，逻辑扇区大小为4096（[高级格式化](</wzh/index.php?title=%E9%AB%98%E7%BA%A7%E6%A0%BC%E5%BC%8F%E5%8C%96&action=edit&redlink=1> "高级格式化（页面不存在）")4Kn 设备）的分区应该至少300 MiB[[2]](<https://superuser.com/questions/1310927/what-is-the-absolute-minimum-size-a-uefi-partition-can-be/1310938>)，其他情况应该至少100 MiB。[[3]](<https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/configure-uefigpt-based-hard-drive-partitions#diskpartitionrules>)
  * 为确保分区能够被格式化为FAT32，逻辑扇区大小512字节的分区大小应该至少 36 MiB，4096字节的分区至少 260 MiB。[[4]](<https://superuser.com/a/1717643>)
  * 如果与这些问题都无关，分区大小最小可达 2 MiB，此时只能放得下启动加载器。

###  GPT 分区磁盘

[GUID Partition Table](<../zh-cn/GUID_Partition_Table.html> "GUID Partition Table") 中 EFI 系统分区以[分区类型 GUID](<https://en.wikipedia.org/wiki/GUID_Partition_Table#Partition_type_GUIDs> "wikipedia:GUID Partition Table") `C12A7328-F81F-11D2-BA4B-00A0C93EC93B` 标识。 

从以下方法中**任选其一** 在 GPT 分区的磁盘上创建 ESP： 

  * [fdisk](<../zh-cn/Fdisk.html> "Fdisk")：创建分区，然后使用命令`t`并指定`uefi`别名[将分区类型更改为](<../zh-cn/Fdisk.html#%E4%BF%AE%E6%94%B9%E5%88%86%E5%8C%BA%E7%B1%BB%E5%9E%8B> "Fdisk") `EFI System`。
  * [gdisk](<../zh-cn/GPT_fdisk.html> "Gdisk")：创建分区类型为 `EF00` 的分区。
  * [GNU Parted](<../zh-cn/GNU_Parted.html> "GNU Parted")：创建文件系统类型为 `fat32` 的分区，并设置 `esp` 标志。

创建分区之后，应当格式化为一种文件系统。前往[#格式化分区](<#%E6%A0%BC%E5%BC%8F%E5%8C%96%E5%88%86%E5%8C%BA>)。 

###  MBR 分区磁盘

**警告：** 强烈建议使用 GPT 而不是 MBR 

  * 某些固件可能不支持 UEFI/MBR 启动，因为它不受 [Windows Setup](<../zh-cn/Dual_boot_with_Windows.html> "Dual boot with Windows") 支持。
  * _bootctl_ 不支持将 [systemd-boot](<../zh-cn/Systemd-boot.html> "Systemd-boot") 安装到MBR 分区的磁盘，参见 [systemd issue 1125](<https://github.com/systemd/systemd/issues/1125>)。

另请参阅 [Partitioning#选择 GPT 还是 MBR](<../zh-cn/%E5%88%86%E5%8C%BA.html#%E9%80%89%E6%8B%A9_GPT_%E8%BF%98%E6%98%AF_MBR> "Partitioning") 查看 MBR 的限制和 GPT 的优点。 

[主引导记录](<../zh-cn/%E5%88%86%E5%8C%BA.html#%E4%B8%BB%E5%BC%95%E5%AF%BC%E8%AE%B0%E5%BD%95> "主引导记录")中 EFI 系统分区以[分区类型 ID](<https://en.wikipedia.org/wiki/Partition_type> "wikipedia:Partition type") `EF` 标识。 

从以下方法中**任选其一** 在 MBR 分区的磁盘上创建 ESP： 

  * [fdisk](<../zh-cn/Fdisk.html> "Fdisk"): 创建一个主分区，然后使用命令`t`[将分区类型更改为](<../zh-cn/Fdisk.html#%E4%BF%AE%E6%94%B9%E5%88%86%E5%8C%BA%E7%B1%BB%E5%9E%8B> "Fdisk") `EFI (FAT-12/16/32)`。
  * [GNU Parted](<../zh-cn/GNU_Parted.html> "GNU Parted"): 创建文件系统类型为 `fat32` 的分区，并设置 `esp` 标志。

创建分区之后，应当格式化为一种文件系统。前往[#格式化分区](<#%E6%A0%BC%E5%BC%8F%E5%8C%96%E5%88%86%E5%8C%BA>)。 

##  格式化分区

UEFI 规范要求支持 FAT12、FAT16 和 FAT32 文件系统（参见 [UEFI specification version 2.10, section 13.3.1.1](<https://uefi.org/specs/UEFI/2.10/13_Protocols_Media_Access.html#file-system-format-1>)），但任何合规的厂商都可以支持额外的文件系统。例如，Apple [Mac](<../zh-cn/Mac.html> "Mac") 的固件支持 HFS+ 文件系统。 

为避免与其他操作系统的潜在问题，同时既然 UEFI 规范声称 UEFI "encompasses the use of FAT32 for a system partition, and FAT12 or FAT16 for removable media"[specs/UEFI/2.10/13_Protocols_Media_Access.html#file-system-format]，建议使用 [FAT32](<../zh-cn/FAT.html> "FAT32")。使用 [dosfstools](<https://archlinux.org/packages/?name=dosfstools>)包 中的 [mkfs.fat(8)](<https://man.archlinux.org/man/mkfs.fat.8>) 工具： 
    
    # mkfs.fat -F 32 /dev/sd _xY_
    
如果你收到消息 `WARNING: Not enough clusters for a 32 bit FAT!`并且不能[创建](<#%E5%88%9B%E5%BB%BA%E5%88%86%E5%8C%BA>)更大的EFI系统分区，运行 `mkfs.fat -s2 -F32 ...` 或 `-s1` 减小簇大小。否则 UEFI 可能无法读取分区。参见 [mkfs.fat(8)](<https://man.archlinux.org/man/mkfs.fat.8>) 查看支持的簇大小。 

小于 32 MiB 的分区可能无法使用 FAT32。这种情况下，格式化为 FAT16 甚至是 FAT12。例如，2 MiB 的 ESP 只能支持 FAT12： 
    
    # mkfs.fat -F 12 /dev/sd _xY_
    
##  挂载分区

内核、initramfs 文件，在大多数情况下还有处理器的[微码](<../zh-cn/%E5%BE%AE%E7%A0%81.html> "Microcode")，都需要能被[引导加载程序](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F> "引导加载程序")或 UEFI 本身访问才能成功启动系统。因此，如果想要设置简单，那引导加载程序的选择就会限制 EFI 系统分区可能的挂载点。 

**注意：** 如果EFI系统分区没有挂载到`/boot`，确保在升级内核时，没有使用[systemd自动挂载机制](<../zh-cn/Fstab.html#%E9%80%9A%E8%BF%87_systemd_%E8%87%AA%E5%8A%A8%E6%8C%82%E8%BD%BD> "Fstab")（包括[systemd-gpt-auto-generator](<../zh-cn/Systemd.html#GPT_%E5%88%86%E5%8C%BA%E8%87%AA%E5%8A%A8%E6%8C%82%E8%BD%BD> "Systemd")）。每次系统或内核升级前都要手动挂载EFI系统分区，否则升级后可能会无法挂载，导致你的内核停留在当前版本并无法更新EFI系统分区中的内核文件。 

或者[在启动时预加载需要的内核模块](<../zh-cn/%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97.html#systemd> "内核模块")，例如： 
    
    /etc/modules-load.d/vfat.conf
    
    vfat
    nls_cp437
    nls_ascii
    
###  典型挂载点

有三种挂载EFI系统分区的典型情况： 

  * [挂载](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html#%E6%8C%82%E8%BD%BD%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "挂载") EFI系统分区 到 `/boot`： 
    * 便于系统维护和管理，`/boot`是[微码](<../zh-cn/%E5%BE%AE%E7%A0%81.html> "微码")包安装CPU微码initramfs文件和[mkinitcpio](<../zh-cn/Mkinitcpio.html> "Mkinitcpio")安装[内核](<../zh-cn/%E5%86%85%E6%A0%B8.html> "内核")与[initramfs](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#initramfs> "Arch 的启动流程")镜像的默认位置。
    * FAT在挂载时设置了全局属性，这会阻止设置文件特定的[权限](<../zh-cn/%E6%96%87%E4%BB%B6%E6%9D%83%E9%99%90%E4%B8%8E%E5%B1%9E%E6%80%A7.html> "文件权限与属性")和[拓展属性](<../zh-cn/%E6%96%87%E4%BB%B6%E6%9D%83%E9%99%90%E4%B8%8E%E5%B1%9E%E6%80%A7.html#%E6%89%A9%E5%B1%95%E5%B1%9E%E6%80%A7> "文件权限与属性")
    * 通常安装在`/boot`中的文件与EFI相关文件共享EFI系统分区，提高了EFI系统分区的大小需求
    * 双启动的情况下，系统特定的启动文件会处在被其它系统修改操作的潜在危险中
    * 无法[加密/boot](<../zh-cn/GRUB.html#%E5%8A%A0%E5%AF%86%E7%9A%84/boot> "GRUB")，因为固件需要读取EFI相关文件

  * [挂载](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html#%E6%8C%82%E8%BD%BD%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "挂载") EFI系统分区到`/efi`： 
    * 当EFI系统分区包含其他系统的文件时最好和操作系统相关的文件分开，这确保了操作系统相关和EFI相关文件的分离。
    * 只有EFI二进制文件（引导加载程序（和可选驱动））和（或）统一内核镜像会安装在EFI系统分区，避免了安装在`/boot`中的文件对EFI系统分区的大小需求，节约了EFI系统分区的空间。
    * 允许保留`/boot`中文件的Linux特定的文件系统权限，避免了FAT的限制。
    * 允许根据需求单独挂载EFI系统分区，例如需要升级[引导加载程序](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F> "引导加载程序")时。
    * 如果[加密整个系统](<../zh-cn/Dm-crypt/%E5%8A%A0%E5%AF%86%E6%95%B4%E4%B8%AA%E7%B3%BB%E7%BB%9F.html> "Dm-crypt/加密整个系统")并且配置恰当，除少数需要文件没有被加密，`/boot`中的文件能够被加密保护：内核及其他文件储存在加密分区，[统一内核镜像](<../zh-cn/%E7%BB%9F%E4%B8%80%E5%86%85%E6%A0%B8%E6%98%A0%E5%83%8F.html> "统一内核镜像")或[引导加载程序](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F> "引导加载程序")通过相应的文件系统驱动来访问这些文件。

  * [挂载](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html#%E6%8C%82%E8%BD%BD%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "挂载") EFI系统分区到`/efi`， 然后再挂载一个“拓展引导加载器分区”（XBOOTLDR）分区到 `/boot`。在以前创建的 ESP 太小而无法容纳多个引导加载程序以及内核但 ESP 又无法轻松调整大小时（例如在 Windows 之后将 Linux 安装到[双引导（多引导）](<../zh-cn/Arch_+_Windows_%E5%8F%8C%E7%B3%BB%E7%BB%9F.html> "Arch + Windows 双系统")时），这可能非常有用。至少在 [systemd-boot#使用XBOOTLDR安装](<../zh-cn/Systemd-boot.html#Installation_using_XBOOTLDR> "Systemd-boot")时支持此方法。

**注意：**

  * `/efi`是`/boot/efi`的替代挂载点[[5]](<https://uapi-group.org/specifications/specs/boot_loader_specification/#mount-points>)[[6]](<https://github.com/systemd/systemd/pull/3757#issuecomment-234290236>)，`/boot/efi`在过去被使用但现在不推荐。
  * `/efi`在安装一开始时不存在，需要先用 [mkdir(1)](<https://man.archlinux.org/man/mkdir.1>) 创建再挂载EFI系统分区到该目录。

###  替代挂载点

如果不使用[#典型挂载点](<#%E5%85%B8%E5%9E%8B%E6%8C%82%E8%BD%BD%E7%82%B9>)中的方法，就需要将引导文件复制到 ESP（以下称为 `_esp_`）。 
    
    # mkdir -p _esp_ /EFI/arch
    # cp -a /boot/vmlinuz-linux _esp_ /EFI/arch/
    # cp -a /boot/initramfs-linux.img _esp_ /EFI/arch/
    # cp -a /boot/initramfs-linux-fallback.img _esp_ /EFI/arch/
    
**注意：** 如果你使用了[外部微码镜像](<../zh-cn/%E5%BE%AE%E7%A0%81.html#Microcode_in_a_separate_initramfs_file> "Microcode")，这些文件同样还需要复制到复制到启动项的位置。

此外，还需要使 ESP 中的文件在以后的内核更新中保持最新。否则可能会导致系统无法启动。以下部分讨论了几种自动化的机制。 

####  使用bind挂载

除了将EFI系统分区挂载到`/boot`你也可以使用bind挂载将分区中的目录挂载到`/boot`（参考[mount(8)](<https://man.archlinux.org/man/mount.8>)）。这样[pacman](<../zh-cn/Pacman.html> "Pacman")就可以直接更新内核文件并保持EFI系统分区的规划。 

**注意：** 这需要[内核](<../zh-cn/FAT.html#Kernel_configuration> "FAT")和[引导加载程序](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F> "引导加载程序")兼容FAT32。通常安装的Arch没有这个问题，但可能存在于其他发行版中（也就是说需要在 `/boot`中创建软连接，参见[[7]](<https://bbs.archlinux.org/viewtopic.php?pid=1331867#p1331867>)。

按照[#替代挂载点](<#%E6%9B%BF%E4%BB%A3%E6%8C%82%E8%BD%BD%E7%82%B9>)节内容，复制所有引导文件到你的EFI系统分区，分区挂载点在`/boot`**外面** 。然后bind挂载目录： 
    
    # mount --bind _esp_ /EFI/arch /boot
    
检查生效后，编辑[Fstab](<../zh-cn/Fstab.html> "Fstab")使修改持续有效： 
    
    /etc/fstab
    
    _esp_ /EFI/arch /boot none defaults,bind 0 0
    
####  使用 systemd

[Systemd](<../zh-cn/Systemd.html> "Systemd")具备事件触发型任务能力。在本特定场景中，该系统利用路径监控功能来检测`/boot/`目录下EFISTUB内核与初始化内存盘文件的更新情况，并在文件被更新时执行同步操作。选择监视`initramfs-linux-fallback.img`文件是因为该文件由mkinitcpio最后生成，可确保所有文件构建完成后再启动复制流程。需要创建的 _systemd_ 路径单元文件及服务单元文件包括： 
    
    /etc/systemd/system/efistub-update.path
    
    [Unit]
    Description=Copy EFISTUB Kernel to EFI system partition
    
    [Path]
    PathChanged=/boot/initramfs-linux-fallback.img
    
    [Install]
    WantedBy=multi-user.target
    WantedBy=system-update.target
    
    /etc/systemd/system/efistub-update.service
    
    [Unit]
    Description=Copy EFISTUB Kernel to EFI system partition
    
    [Service]
    Type=oneshot
    ExecStart=/usr/bin/cp -af /boot/vmlinuz-linux _esp_ /EFI/arch/
    ExecStart=/usr/bin/cp -af /boot/initramfs-linux.img _esp_ /EFI/arch/
    ExecStart=/usr/bin/cp -af /boot/initramfs-linux-fallback.img _esp_ /EFI/arch/

随后[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Enable")并[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "Start")`efistub-update.path`。 

**提示：** 若需使用自有密钥实现[安全启动](<../zh-cn/UEFI/%E5%AE%89%E5%85%A8%E5%90%AF%E5%8A%A8.html> "安全启动")，您可以配置该服务，使其额外使用 [sbsigntools](<https://archlinux.org/packages/?name=sbsigntools>)包 对映像进行签署： 
    
    ExecStart=/usr/bin/sbsign --key _/path/to/db.key_ --cert _/path/to/db.crt_ --output _esp_ /EFI/arch/vmlinuz-linux /boot/vmlinuz-linux

####  使用文件系统事件

[文件系统事件](<../zh-cn/%E8%87%AA%E5%8A%A8%E5%90%AF%E5%8A%A8.html#%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F%E4%BA%8B%E4%BB%B6> "Autostarting")可用于在内核更新后运行脚本同步 EFISTUB 内核。下面是一个使用 [incron](</wzh/index.php?title=Incron&action=edit&redlink=1> "Incron（页面不存在）")（英语：[incron](<https://wiki.archlinux.org/title/incron> "en:incron")） 的示例。 
    
    /usr/local/bin/efistub-update
    
    #!/bin/sh
    cp -af /boot/vmlinuz-linux _esp_ /EFI/arch/
    cp -af /boot/initramfs-linux.img _esp_ /EFI/arch/
    cp -af /boot/initramfs-linux-fallback.img _esp_ /EFI/arch/
    
**注意：** 第一个参数 `/boot/initramfs-linux-fallback.img` 是要监视的文件。第二个参数 `IN_CLOSE_WRITE` 是要监视的动作。第三个参数 `/usr/local/bin/efistub-update` 是要执行的脚本。
    
    /etc/incron.d/efistub-update.conf
    
    /boot/initramfs-linux-fallback.img IN_CLOSE_WRITE /usr/local/bin/efistub-update
    
要使用这个方法，[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `incrond.service`。 

####  使用 mkinitcpio preset

因为`/etc/mkinitcpio.d/`中的preset支持shell脚本，编辑presets可以复制内核和initramfs到ESP。 

#####  替换 mkinitcpio 钩子

编辑文件 `/etc/mkinitcpio.d/linux.preset`： 
    
    /etc/mkinitcpio.d/linux.preset
    
    # mkinitcpio preset file for the 'linux' package
    
    # Directory to install the kernel, the initramfs...
    ESP_DIR="_esp_ /EFI/arch"
    
    #ALL_config="/etc/mkinitcpio.conf"
    ALL_kver="${ESP_DIR}/vmlinuz-linux"
    
    PRESETS=('default' 'fallback')
    
    #default_config="/etc/mkinitcpio.conf"
    default_image="${ESP_DIR}/initramfs-linux.img"
    default_options=""
    
    #fallback_config="/etc/mkinitcpio.conf"
    fallback_image="${ESP_DIR}/initramfs-linux-fallback.img"
    fallback_options="-S autodetect"

要测试它，只需运行： 
    
    # rm /boot/initramfs-linux-fallback.img /boot/initramfs-linux.img
    # mv /boot/vmlinuz-linux _esp_ /EFI/arch/
    # mkinitcpio -p linux
    
#####  另一个例子
    
    /etc/mkinitcpio.d/linux.preset
    
    ESP_DIR="_esp_ /EFI/arch"
    #ALL_config="/etc/mkinitcpio.conf"
    ALL_kver="$ESP_DIR/vmlinuz-linux$suffix"
    PRESETS=('default')
    default_config="/etc/mkinitcpio.conf"
    default_image="$ESP_DIR/initramfs-linux$suffix.img"
    
    /etc/mkinitcpio.d/linux-zen.preset
    
    suffix='-zen'
    source /etc/mkinitcpio.d/linux.preset

####  使用 mkinitcpio post 钩子

[mkinitcpio post 钩子](<../zh-cn/Mkinitcpio.html#Post_hooks> "Mkinitcpio")能够在initramfs生成后，复制内核和initramfs镜像到所需的位置。 

[创建](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "创建")下面的文件并使文件[可执行](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "可执行"): 
    
    /etc/initcpio/post/copy-kernel-and-initramfs
    
    #!/usr/bin/env bash
    
    kernel="$1"
    initrd="$2"
    target_dir="_esp_ /EFI/arch"
    files_to_copy=()
    
    for file in "$kernel" "$initrd"; do
    	if [[ -n "$file" ]] && ! cmp -s -- "$file" "${target_dir}/${file##*/}"; then
    		files_to_copy+=("$file")
    	fi
    done
    
    (( ! ${#files_to_copy[@]} )) && exit 0
    
    cp -af -- "${files_to_copy[@]}" "${target_dir}/"

####  使用 pacman 钩子

最后一个选项依赖于在事务结束时运行的 [pacman 钩子](<../zh-cn/Pacman.html#%E9%92%A9%E5%AD%90> "Pacman")。 

第一个文件是一个监控相关文件的钩子，如果文件在前一个事务中被修改，钩子就会运行。 
    
    /etc/pacman.d/hooks/999-kernel-efi-copy.hook
    
    [Trigger]
    Type = Path
    Operation = Install
    Operation = Upgrade
    Target = usr/lib/modules/*/vmlinuz
    Target = usr/lib/initcpio/*
    Target = boot/*-ucode.img
    
    [Action]
    Description = Copying linux and initramfs to EFI directory...
    When = PostTransaction
    Exec = /usr/local/bin/kernel-efi-copy.sh

第二个文件是脚本本身。创建文件并使其[可执行](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "Help:Reading")： 
    
    /usr/local/bin/kernel-efi-copy.sh
    
    #!/bin/sh
    #
    # Copy kernel and initramfs images to EFI directory
    #
    
    ESP_DIR="_esp_ /EFI/arch"
    
    for file in /boot/vmlinuz*
    do
            cp -af "$file" "$ESP_DIR/$(basename "$file").efi"
            [ $? -ne 0 ] && exit 1
    done
    
    for file in /boot/initramfs*
    do
            cp -af "$file" "$ESP_DIR/"
            [ $? -ne 0 ] && exit 1
    done
    
    [ -e /boot/intel-ucode.img ] && cp -af /boot/intel-ucode.img "$ESP_DIR/"
    [ -e /boot/amd-ucode.img ] && cp -af /boot/amd-ucode.img "$ESP_DIR/"
    
    exit 0

##  提示和技巧

###  替换为更大的分区

如果硬盘已经预装操作系统，那么EFI系统分区大小可能会比[#创建分区](<#%E5%88%9B%E5%BB%BA%E5%88%86%E5%8C%BA>)中推荐的小。例如Windows安装程序会在一个非4Kn设备上创建一个很小的100 MiB EFI系统分区。 

这种情况下最好新创建一个更大的EFI系统分区以避免存储空间耗尽。 

####  在Windows里为新分区腾出空间

在Windows下，使用磁盘管理(`diskmgmt.msc`)或在命令行使用`diskpart.exe`工具管理分区。 

以管理员权限运行`diskmgmt.msc`。 

  1. 右键C盘分区，然后选择 _压缩卷_

  1. 输入`4096`作为压缩的空间量，并点击 _压缩_ 。

之后在C盘后方应该会出现4 GiB的未分配空间。 

引导进入Arch Linux或Arch Linux安装介质环境为下一步创建新分区做准备。 

####  删除旧的分区并创建一个新的ESP

首先确保备份好原来EFI系统分区的内容，若EFI系统分区的挂载点为 _esp_ ： 
    
    # cp -a _esp_ /esp_backup
    
卸载EFI系统分区： 
    
    # umount _esp_
    
**注意：** 在本地安装的系统下你可能还需要[停止](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "停止") `_esp_.mount` 和 `_esp_.automount` 单元以防止系统再次自动挂载它。

运行 _blkid_ 并记下旧分区的UUID和PARTUUID，下一步这些将值用于新分区上。 
    
    # blkid
    
    /dev/sd _xY_ : UUID="_**XXXX-XXXX**_ " BLOCK_SIZE="512" TYPE="vfat" PARTLABEL="EFI system partition" PARTUUID="_**YYYYYYYY-YYYY-YYYY-YYYY-YYYYYYYYYYYY**_ "

使用[gptfdisk](<https://archlinux.org/packages/?name=gptfdisk>)包的[sgdisk](<../zh-cn/GPT_fdisk.html> "GPT fdisk")删除旧分区： 
    
    # sgdisk --delete=_Y_ /dev/sd _x_
    
在最大的未分配空间上创建新分区并指定PARTLABEL和使用旧分区的PARTUUID： 
    
    # sgdisk --align-end --largest-new=0 --typecode=0:ef00 --change-name=0:'EFI system partition' --partition-guid=0:_YYYYYYYY-YYYY-YYYY-YYYY-YYYYYYYYYYYY_ /dev/sd _x_
    
使用 _fdisk_ 确认新创建的大小为4 GiB的EFI系统分区： 
    
    # fdisk -l /dev/sd _x_
    
    ...
    Device         Start       End   Sectors  Size Type
    /dev/sd _x_ 1  158099456 166488063   8388608    4G EFI System
    /dev/sd _x_ 2     206848    239615     32768   16M Microsoft reserved
    /dev/sd _x_ 3     239616 158099455 157859840 75.3G Microsoft basic data
    /dev/sd _x_ 4  166488064 167768063   1280000  625M Windows recovery environment
    /dev/sd _x_ 5  167768064 176156671   8388608    4G Linux swap
    /dev/sd _x_ 6  176156672 243265535  67108864   32G Linux root (x86-64)
    Partition table entries are not in disk order.
    
分区编号在删除和创建分区后没有重新排列，所以EFI系统分区编号应该和之前一样。 

将新分区格式化为FAT32，并使用旧的UUID（需要删除UUID中的“-”横线符）： 
    
    # mkfs.fat -F 32 -i _XXXXXXXX_ /dev/sd _xY_
    
最后挂载新分区并恢复原有内容： 
    
    # mount /dev/sd _xY_ _esp_
    # cp -a /esp_backup/. _esp_ /
    
如果你先前停止了` _esp_.automount`，再次[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")它。 

####  通过牺牲相邻的swap分区来扩大ESP

如果swap正好在EFI系统分区后面，你可以牺牲swap空间用于扩大EFI系统分区。例如你的分区布局类似下面的例子： 
    
    # fdisk -l /dev/sd _x_
    
    ...
    Device       Start       End   Sectors  Size Type
    /dev/sd _x_ 1     2048    616447    614400  300M EFI System
    /dev/sd _x_ 2   616448   9005055   8388608    4G Linux swap
    /dev/sd _x_ 3  9005056 125827071 116822016 55.7G Linux root (x86-64)
    
首先[停用swap分区](<../zh-cn/Swap.html#%E5%85%B3%E9%97%AD%E4%BA%A4%E6%8D%A2%E5%88%86%E5%8C%BA> "Swap")，并把它从[fstab](<../zh-cn/Fstab.html> "Fstab")里删除。 

使用[fdisk](<../zh-cn/Fdisk.html> "Fdisk")删除swap分区并增大EFI系统分区。 

  1. 运行： 
         
         # fdisk -l /dev/sd _x_

  2. 使用`d`命令删除swap分区（在示例中swap分区的分区号是`2`）。
  3. 使用`e`命令增大EFI系统分区（在示例中EFI系统分区的分区号是`1`）。使用给出的默认值作为新分区的大小并按下`Enter`确认。
  4. 通过{{ic|w}命令将修改落盘并退出fdisk。

分区大小修改后需要修改分区内的文件系统大小。因为[fatresize(1)](<https://man.archlinux.org/man/fatresize.1>) [存在问题](<https://github.com/ya-mouse/fatresize/issues/18>)并且libparted [不能修改FAT卷的大小为确切的值](<https://superuser.com/a/1717415>)，唯一的办法就是备份文件系统的文件，然后创建新的分区来利用所有分区空间。 

记下文件系统的[UUID](<../zh-cn/%E5%9D%97%E8%AE%BE%E5%A4%87%E6%8C%81%E4%B9%85%E5%8C%96%E5%91%BD%E5%90%8D.html#%E9%80%9A%E8%BF%87_uuid> "UUID")： 
    
    $ lsblk -dno UUID /dev/sd _xY_
    
    _**XXXX-XXXX**_
    
备份好原来EFI系统分区的内容，若EFI系统分区的挂载点为 _esp_ ： 
    
    # cp -a _esp_ /esp_backup
    
卸载EFI系统分区： 
    
    # umount _esp_
    
**注意：** 在本地安装的系统下你可能还需要[停止](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "停止") `_esp_.mount` 和 `_esp_.automount` 单元以防止系统再次自动挂载它。

从分区中擦除文件系统的signature以避免受到旧文件系统的影响： 
    
    # wipefs -af /dev/sd _xY_
    
将新分区格式化为FAT32，并使用旧的UUID（需要删除UUID中的“-”横线符）： 
    
    # mkfs.fat -F 32 -i _XXXXXXXX_ /dev/sd _xY_
    
最后挂载新分区并恢复原有内容： 
    
    # mount /dev/sd _xY_ _esp_
    # cp -a /esp_backup/. _esp_ /
    
如果你先前停止了` _esp_.automount`，再次[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")它。 

由于现在没有了swap分区，将swap放在一个[交换文件](<../zh-cn/Swap.html#%E4%BA%A4%E6%8D%A2%E6%96%87%E4%BB%B6> "Swap")上。 

##  故障排除

###  ESP在软RAID1上

将ESP放在RAID1阵列上是可能的，但这么做也会带来数据损坏的风险，创建ESP时也要做额外的考虑，详情参见[[8]](<https://bbs.archlinux.org/viewtopic.php?pid=1398710#p1398710>)和[[9]](<https://bbs.archlinux.org/viewtopic.php?pid=1390741#p1390741>)还有[UEFI booting and RAID1](<https://outflux.net/blog/archives/2018/04/19/uefi-booting-and-raid1/>)。 

整个方案的关键点是使用`--metadata 1.0`将RAID metadata放在分区尾部，否则固件无法访问ESP： 
    
    # mdadm --create --verbose --level=1 **--metadata=1.0** --raid-devices=2 /dev/md/ESP /dev/sda _X_ /dev/sdb _Y_
    
或者如果你的ESP不会频繁修改，可以在进行相关更新时把主要ESP的修改复制到不同磁盘上的备用ESP上。备用ESP的引导启动项可以用[efibootmgr](<../zh-cn/UEFI.html#efibootmgr> "UEFI")手动添加。参见[debian wiki](<https://wiki.debian.org/UEFI#RAID_for_the_EFI_System_Partition>)。需要注意这个办法虽然避免了RAID方法的风险，但只在使用单系统时有用。 

###  固件看不到 EFI 目录

如果要给 FAT 文件系统一个[卷名（即文件系统标签）](<../zh-cn/Persistent_block_device_naming.html#%E9%80%9A%E8%BF%87%E6%A0%87%E7%AD%BE> "Persistent block device naming")，请不要将其命名为 `EFI`。卷名和 EFI 目录名称相同可能会触发某些固件中的错误，导致固件表现得好像 EFI 目录不存在一样。 

##  参见

  * [EFI 系统分区与默认启动行为](<https://blog.uncooperative.org/uefi/linux/shim/efi%20system%20partition/2014/02/06/the-efi-system-partition.html>)
  * [Multi Boot Linux With One Boot Partition | John Ramsden](<https://ramsdenj.com/posts/2016-04-15-multi-boot-linux-with-one-boot-partition/>)
