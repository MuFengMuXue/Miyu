相关文章

  * [文件系统](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html> "文件系统")

**翻译状态：**

  * 本文（或部分内容）译自 [FAT](<https://wiki.archlinux.org/title/FAT> "arch:FAT")，最近一次同步于 2024-7-4，若英文版本有所[更改](<https://wiki.archlinux.org/title/FAT?diff=0&oldid=811907>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/FAT_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

摘自 [Wikipedia:File Allocation Table](<https://en.wikipedia.org/wiki/File_Allocation_Table> "wikipedia:File Allocation Table"): 

    File Allocation Table（FAT）是一种计算机文件系统结构，一系列行业标准文件系统都使用它。FAT 文件系统是一种传统的文件系统，简单而强大。即使在轻量级实现中，它也能提供良好的性能，但无法提供与某些现代文件系统相同的性能、可靠性和可扩展性。不过，出于兼容性的考虑，目前几乎所有已开发的个人计算机操作系统以及许多移动设备和嵌入式系统都支持 FAT 文件系统，因此它是一种非常适合在 1981 年至今几乎所有类型和年代的计算机和设备之间进行数据交换的格式。

##  创建文件系统

要创建 FAT 文件系统，请[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [dosfstools](<https://archlinux.org/packages/?name=dosfstools>)包。 

`mkfs.fat` 支持创建 FAT12、FAT16 和 FAT32，有关它们差异的解释，请参阅 [Wikipedia:File Allocation Table#Types](<https://en.wikipedia.org/wiki/File_Allocation_Table#Types> "wikipedia:File Allocation Table") 。 `mkfs.fat` 将根据分区大小选择 FAT 类型，要明确地创建特定类型的 FAT 文件系统，请使用 `-F` 选项。参见 [mkfs.fat(8)](<https://man.archlinux.org/man/mkfs.fat.8>) 以了解更多信息。 

**提示：** 在大多数情况下，你都希望使用 FAT32。为确保分区能格式化为 FAT32，在逻辑扇区大小为 512 字节的硬盘上，分区大小至少应为 36 MiB；在[逻辑扇区大小为 4096 字节的驱动器](<../zh-cn/%E5%85%88%E8%BF%9B%E6%A0%BC%E5%BC%8F%E5%8C%96.html> "先进格式化")上，分区大小至少应为 260 MiB。[[1]](<https://superuser.com/a/1717643>)

将分区格式化为 FAT32： 
    
    # mkfs.fat -F 32 /dev/_partition_
    
**注意：**`mkfs.vfat` 和 `mkfs.msdos` 都是`mkfs.fat`符号链接，它们是相同的工具。

##  内核配置

以下是内核中默认 _挂载_ 配置的示例： 
    
    $ zgrep -e FAT -e DOS /proc/config.gz | sort -r
    
    # DOS/FAT/NT Filesystems
    CONFIG_FAT_FS=m
    CONFIG_MSDOS_PARTITION=y
    CONFIG_FAT_FS=m
    CONFIG_MSDOS_FS=m
    CONFIG_VFAT_FS=m
    CONFIG_FAT_DEFAULT_CODEPAGE=437
    CONFIG_FAT_DEFAULT_IOCHARSET="iso8859-1"
    CONFIG_NCPFS_SMALLDOS=y

选项的简短说明： 

  * 语言设置： `CONFIG_FAT_DEFAULT_CODEPAGE`, `CONFIG_FAT_DEFAULT_IOCHARSET`
  * 如果启用，则在 FAT 分区上把所有文件名转为小写字母： `CONFIG_NCPFS_SMALLDOS`
  * 启用对 FAT 文件系统的支持： `CONFIG_FAT_FS`, `CONFIG_MSDOS_FS`, `CONFIG_VFAT_FS`
  * 在 x86 PC 上启用对 FAT 分区驱动器的支持：`CONFIG_MSDOS_PARTITION`

如果 mount 检测到的分区类型是 VFAT，那么它将运行 `/usr/bin/mount.vfat` 脚本。 
    
    /usr/bin/mount.vfat
    
    #!/bin/bash
    #mount VFAT with full rw (read-write) permissions for all users
    #/usr/bin/mount -i -t vfat -oumask=0000,iocharset=utf8 "$@"
    #The above is the same as
    mount -i -t vfat -oiocharset=utf8,fmask=0000,dmask=0000 "$@"

##  以普通用户身份写入 FAT32

要在 FAT32 分区上写入，必须对 [fstab](<../zh-cn/Fstab.html> "Fstab") 文件进行一些更改。 
    
    /etc/fstab
    
    /dev/sd _xY_    /mnt/some_folder  vfat   **user,rw**

`user` 选项意味着任何用户（即使是非root用户）都可以挂载和卸载分区 `/dev/sd _xY_` ([mount(8) § Non-superuser mounts](<https://man.archlinux.org/man/mount.8#Non-superuser_mounts>))。 `rw` 提供读写访问权限。 

例如，如果您的 FAT32 分区位于 `/dev/sda9`，而您希望将其挂载到 `/mnt/fat32`，则应使用： 
    
    /etc/fstab
    
    /dev/sda9    /mnt/fat32        vfat   user,rw

现在，任何用户都可以使用以下方式挂载它： 
    
    $ mount /mnt/fat32
    
并使用以下命令卸载它： 
    
    $ umount /mnt/fat32
    
请注意，FAT 不支持 Linux 文件权限。每个文件也将显示为可执行文件。您可能希望使用 `showexec` 选项仅将 Windows 可执行文件（com、exe、bat）标记为可执行文件。参见 [mount(8) § Mount options for fat](<https://man.archlinux.org/man/mount.8#Mount_options_for_fat>) 来获得更多选项。 

##  查询 FAT 文件系统类型

如果需要知道分区使用的是哪种[类型的FAT文件系统](<https://en.wikipedia.org/wiki/File_Allocation_Table#Types> "wikipedia:File Allocation Table")，请使用 _file_ 命令： 
    
    # file -s /dev/_partition_
    
    /dev/_partition_ : DOS/MBR boot sector, code offset 0x3c+2, OEM-ID "mkfs.fat", sectors/cluster 4, root entries 512, sectors 4096 (volumes <=32 MB), Media descriptor 0xf8, sectors/FAT 3, sectors/track 32, heads 64, serial number 0x5bc09c21, unlabeled, **FAT (12 bit)**

或者，您可以使用 [mtools](<https://archlinux.org/packages/?name=mtools>)包 包中的 _minfo_ ： 
    
    # minfo -i /dev/_partition_ ::
    
    device information:
    ===================
    filename="/dev/_partition_ "
    sectors per track: 32
    heads: 64
    cylinders: 2
    
    media byte: f8
    
    mformat command line: mformat -t 2 -h 64 -s 32 -i "/dev/_partition_ " ::
    
    bootsector information
    ======================
    banner:"mkfs.fat"
    sector size: 512 bytes
    cluster size: 4 sectors
    reserved (boot) sectors: 1
    fats: 2
    max available root directory slots: 512
    small size: 4096 sectors
    media descriptor byte: 0xf8
    sectors per fat: 3
    sectors per track: 32
    heads: 64
    hidden sectors: 0
    big size: 0 sectors
    physical drive id: 0x80
    reserved=0x0
    dos4=0x29
    serial number: 5BC09C21
    disk label="NO NAME    "
    disk type="**FAT12**   "
    
##  参见

  * [MountFATFileSystems](<https://web.archive.org/web/20190802000917/http://www2.nslu2-linux.org/wiki/pmwiki.php?pagename=HowTo/MountFATFileSystems>)
