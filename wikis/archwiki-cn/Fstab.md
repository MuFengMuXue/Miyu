**翻译状态：**

  * 本文（或部分内容）译自 [fstab](<https://wiki.archlinux.org/title/fstab> "arch:fstab")，最近一次同步于 2025-07-31，若英文版本有所[更改](<https://wiki.archlinux.org/title/fstab?diff=0&oldid=838934>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/fstab_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [块设备持久化命名 ](<../zh-cn/%E5%9D%97%E8%AE%BE%E5%A4%87%E6%8C%81%E4%B9%85%E5%8C%96%E5%91%BD%E5%90%8D.html> "块设备持久化命名")
  * [文件系统](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html> "文件系统")
  * [tmpfs](<../zh-cn/Tmpfs.html> "Tmpfs")
  * [swap](<../zh-cn/Swap.html> "Swap")
  * [genfstab](<../zh-cn/Genfstab.html> "Genfstab")

[fstab(5)](<https://man.archlinux.org/man/fstab.5>)文件可用于定义如何挂载硬盘分区以及各种块设备和远程文件系统。 

每个文件系统都分别在单独一行中定义，这些定义将在系统引导或重新加载系统管理器配置时被动态转换为 [systemd](<../zh-cn/Systemd.html> "Systemd") 挂载单元。默认设置将在需要挂载文件系统的服务启动之前自动进行 [fsck](<../zh-cn/Fsck.html> "Fsck") 并挂载文件系统。例如，systemd 会自动确保类似 [NFS](<../zh-cn/NFS.html> "NFS") 和 [Samba](<../zh-cn/Samba.html> "Samba") 的远程文件系统仅在网络可用后才会进行挂载。因此，`/etc/fstab` 中指定的本地和远程文件系统挂载应能开箱即用。具体信息请参考 [systemd.mount(5)](<https://man.archlinux.org/man/systemd.mount.5>)。 

如果仅提供了单个目录或是设备作为参数，那么 `mount` 会调用 fstab 来填充其它参数。在这种情况下，将调用 fstab 中列出的挂载参数。 

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 需解释 [systemd-remount-fs.service(8)](<https://man.archlinux.org/man/systemd-remount-fs.service.8>) 的作用，并建议通过 `rootflags` 调用无法通过重挂载应用的选项。 (在 [Talk:Fstab](<../zh-cn/Talk:Fstab.html>) 中讨论)

##  用法

一个简单的 `/etc/fstab`，使用了文件系统 UUID： 
    
    /etc/fstab
    
    # <device>                                <dir> <type> <options>                                        <dump> <fsck>
    UUID=0a3407de-014b-458b-b5c1-848e92a327a3 /     ext4 defaults                                           0      1
    UUID=CBB6-24F2                            /boot vfat defaults,nodev,nosuid,noexec,fmask=0177,dmask=0077 0      2
    UUID=f9fe0b69-a280-415d-a03a-a32752370dee none  swap defaults                                           0      0
    UUID=b411dc99-f0a0-4c87-9e05-184977be8539 /home ext4 defaults                                           0      2
    
  * `<device>` 描述了要挂载的特定块设备或远程文件系统，详见 [#文件系统标识](<#%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F%E6%A0%87%E8%AF%86>)。
  * `<dir>` 指定了要将文件系统[挂载](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html#%E6%8C%82%E8%BD%BD%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "挂载")到的目录，即挂载点。必须提前创建该目录。
  * `<type>` 是[文件系统](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html> "文件系统")类型。
  * `<options>` 是文件系统挂载选项，详见 [mount(8) § FILESYSTEM-INDEPENDENT MOUNT OPTIONS](<https://man.archlinux.org/man/mount.8#FILESYSTEM-INDEPENDENT_MOUNT_OPTIONS>) 和 [ext4(5) § Mount options for ext4](<https://man.archlinux.org/man/ext4.5#Mount_options_for_ext4>)。
  * `<dump>` 会被 [dump(8)](<https://linux.die.net/man/8/dump>) 工具检查。该字段通常设置为 `0`，以禁用检查。
  * `<fsck>` 设置了引导时检查文件系统的顺序，具体信息请参考 [fsck(8)](<https://man.archlinux.org/man/fsck.8>)。对于根设备，该字段需设置为 `1`。对于其它分区该字段应该设置为 `2`，或设置为 `0` 以禁用检查。

**提示：**

  * `auto` 类型会让 mount 命令猜测设备使用的文件系统。这对于[光学介质](<../zh-cn/%E5%85%89%E7%9B%98%E9%A9%B1%E5%8A%A8%E5%99%A8.html> "光盘驱动器")（CD/DVD/Blu-ray）非常有用。
  * 如果根文件系统是 [btrfs](<../zh-cn/Btrfs.html> "Btrfs") 或 [XFS](<../zh-cn/XFS.html> "XFS")，那么 fsck 顺序应该设置为 `0` 而不是 `1`。具体信息请参考 [fsck.btrfs(8)](<https://man.archlinux.org/man/fsck.btrfs.8>) 和 [fsck.xfs(8)](<https://man.archlinux.org/man/fsck.xfs.8>)。

除非指定 `noauto` 选项，否则在启动以及使用带有 `-a` 标识的 [mount(8)](<https://man.archlinux.org/man/mount.8>) 命令时,所有在 `/etc/fstab` 里指定的设备都会自动被挂载。除非使用 `nofail` 选项，否则在列表中出现但实际不存在的设备会导致错误。 

更多信息请参考 [fstab(5) § DESCRIPTION](<https://man.archlinux.org/man/fstab.5#DESCRIPTION>)。 

##  文件系统标识

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** 除了内核名称外，还有其他类型的设备路径。`/dev/disk/by-*/*`，`/dev/mapper/*` 和 `/dev/md/*` 有着不同程度的持久性，而且使用它们应该是没有问题的。 (在 [Talk:Fstab](<../zh-cn/Talk:Fstab.html>) 中讨论)

在 `/etc/fstab` 配置文件中，有多种方法可用于标识文件系统：内核名称、文件系统标签或者 UUID，对于 GPT 硬盘还可以使用 GPT 分区标签和 UUID。不应使用内核名称，而 UUID 或分区 UUID（PARTUUID）应该优于标签。更多信息请参考[块设备持久化命名](<../zh-cn/%E5%9D%97%E8%AE%BE%E5%A4%87%E6%8C%81%E4%B9%85%E5%8C%96%E5%91%BD%E5%90%8D.html> "块设备持久化命名")。建议在继续阅读本文前先阅读那篇文章。 

在本节中，我们将通过示例描述如何使用所有可用的挂载方法来挂载文件系统。以下示例中使用的命令 `lsblk -f` 和 `blkid` 的输出可在[块设备持久化命名](<../zh-cn/%E5%9D%97%E8%AE%BE%E5%A4%87%E6%8C%81%E4%B9%85%E5%8C%96%E5%91%BD%E5%90%8D.html> "块设备持久化命名")一文中找到。 

###  内核名称

运行 `lsblk -f` 以列出分区，并在 _NAME_ 列中的值的前面加上 `/dev/`。 
    
    /etc/fstab
    
    # <device <dir> <type> <options>                                          <dump> <fsck>
    /dev/sda2 /     ext4   defaults                                           0      1
    /dev/sda1 /boot vfat   defaults,nodev,nosuid,noexec,fmask=0177,dmask=0077 0      2
    /dev/sda3 /home ext4   defaults                                           0      2
    /dev/sda4 none  swap   defaults                                           0      0
    
**警告：**[块设备的内核名称](<../zh-cn/%E8%AE%BE%E5%A4%87%E6%96%87%E4%BB%B6.html#%E5%9D%97%E8%AE%BE%E5%A4%87%E5%90%8D> "设备文件")不是[持久化的](<../zh-cn/%E5%9D%97%E8%AE%BE%E5%A4%87%E6%8C%81%E4%B9%85%E5%8C%96%E5%91%BD%E5%90%8D.html> "块设备持久化命名")，可能在每次启动系统时都不同，因此不能被用在配置文件中（包括 `/etc/fstab`）。

###  文件系统标签

运行 `lsblk -f` 以列出分区，并在 [LABEL](<../zh-cn/%E5%9D%97%E8%AE%BE%E5%A4%87%E6%8C%81%E4%B9%85%E5%8C%96%E5%91%BD%E5%90%8D.html#%E9%80%9A%E8%BF%87%E6%A0%87%E7%AD%BE> "块设备持久化命名") 列中的值的前面加上 `LABEL=`；或者运行 `blkid` 并使用不带引号的 LABEL 的值： 
    
    /etc/fstab
    
    # <device>   <dir> <type> <options>                                          <dump> <fsck>
    LABEL=System /     ext4   defaults                                           0      1
    LABEL=ESP    /boot vfat   defaults,nodev,nosuid,noexec,fmask=0177,dmask=0077 0      2
    LABEL=Data   /home ext4   defaults                                           0      2
    LABEL=Swap   none  swap   defaults                                           0      0
    
**注意：** 如果你的标签中包含空格，请参考 [#路径名有空格](<#%E8%B7%AF%E5%BE%84%E5%90%8D%E6%9C%89%E7%A9%BA%E6%A0%BC>)。

###  文件系统 UUID

运行 `lsblk -f` 以列出分区，并在 [UUID](<../zh-cn/%E5%9D%97%E8%AE%BE%E5%A4%87%E6%8C%81%E4%B9%85%E5%8C%96%E5%91%BD%E5%90%8D.html#%E9%80%9A%E8%BF%87_uuid> "UUID") 列中的值的前面加上 `UUID=`；或者运行 `blkid` 并使用不带引号的 UUID 的值： 
    
    /etc/fstab
    
    # <device>                                <dir> <type> <options>                                        <dump> <fsck>
    UUID=0a3407de-014b-458b-b5c1-848e92a327a3 /     ext4 defaults                                           0      1
    UUID=CBB6-24F2                            /boot vfat defaults,nodev,nosuid,noexec,fmask=0177,dmask=0077 0      2
    UUID=b411dc99-f0a0-4c87-9e05-184977be8539 /home ext4 defaults                                           0      2
    UUID=f9fe0b69-a280-415d-a03a-a32752370dee none  swap defaults                                           0      0
    
###  GPT 分区标签

运行 `blkid` 来列出分区,并使用不带引号的 [PARTLABEL](<../zh-cn/%E5%9D%97%E8%AE%BE%E5%A4%87%E6%8C%81%E4%B9%85%E5%8C%96%E5%91%BD%E5%90%8D.html#%E9%80%9A%E8%BF%87%E5%88%86%E5%8C%BA%E6%A0%87%E7%AD%BE> "块设备持久化命名") 的值： 
    
    /etc/fstab
    
    # <device>                           <dir> <type> <options>                                        <dump> <fsck>
    PARTLABEL=GNU/Linux                  /     ext4 defaults                                           0      1
    PARTLABEL=EFI\040system\040partition /boot vfat defaults,nodev,nosuid,noexec,fmask=0177,dmask=0077 0      2
    PARTLABEL=Home                       /home ext4 defaults                                           0      2
    PARTLABEL=Swap                       none  swap defaults                                           0      0
    
**注意：** 如果你的分区标签中包含空格，请参考 [#路径名有空格](<#%E8%B7%AF%E5%BE%84%E5%90%8D%E6%9C%89%E7%A9%BA%E6%A0%BC>)。

###  GPT 分区 UUID

运行 `blkid` 来列出分区，并使用不带引号的 [PARTUUID](<../zh-cn/%E5%9D%97%E8%AE%BE%E5%A4%87%E6%8C%81%E4%B9%85%E5%8C%96%E5%91%BD%E5%90%8D.html#%E9%80%9A%E8%BF%87%E5%88%86%E5%8C%BA%E6%A0%87%E7%AD%BE> "块设备持久化命名") 的值： 
    
    /etc/fstab
    
    # <device>                                    <dir> <type> <options>                                        <dump> <fsck>
    PARTUUID=98a81274-10f7-40db-872a-03df048df366 /     ext4 defaults                                           0      1
    PARTUUID=d0d0d110-0a71-4ed6-936a-304969ea36af /boot vfat defaults,nodev,nosuid,noexec,fmask=0177,dmask=0077 0      2
    PARTUUID=7280201c-fc5d-40f2-a9b2-466611d3d49e /home ext4 defaults                                           0      2
    PARTUUID=039b6c1c-7553-4455-9537-1befbc9fbc5b none  swap defaults                                           0      0
    
##  提示和技巧

###  通过 systemd 自动挂载

请参考 [systemd.mount(5)](<https://man.archlinux.org/man/systemd.mount.5>) 获取所有 systemd 挂载选项。 

####  本地分区

在使用大分区时，可以在 _fsck_ 进行检查时启动不依赖该分区的服务以提高效率。这可以通过向 `/etc/fstab` 的分区条目中添加以下选项来完成： 
    
    x-systemd.automount
    
这会使分区被首次访问时才运行 fsck 和 mount，并且内核会在它可用前缓冲所有对它的文件访问。 该方法适用于如 `/home` 分区非常大的情况。 

**注意：** 这会将文件系统类型设为 `autofs`，并默认被 [locate](<../zh-cn/Locate.html> "Locate") 忽略。

####  远程文件系统

对于远程文件系统的挂载也是一样的。如果你想让它们只在访问时被挂载，就需要使用 `x-systemd.automount` 参数。另外,你还可以使用 `x-systemd.mount-timeout=` 选项来指定 systemd 应该在命令完成前等待多久。另外，`_netdev` 选项可确保 systemd 明白该挂载需要网络，并且在网络就绪后再执行挂载： 
    
    x-systemd.automount,x-systemd.mount-timeout=30,_netdev
    
####  加密文件系统

如果你有一个使用密钥文件的加密附属文件系统，可以将 `nofail` 参数添加到 `/etc/crypttab` 和 `/etc/fstab` 中的对应项中。 _systemd_ 将不会在启动时等待 cryptsetup 完成解密并挂载，而是等到甚至是抵达 default.target 后再完成挂载。通过忽略无需启动后立即可用的加密附属文件系统，该操作可避免由此带来的启动延迟。cryptsetup 的具体配置请参考 [dm-crypt/系统配置#非阻塞挂载](<../zh-cn/Dm-crypt/%E7%B3%BB%E7%BB%9F%E9%85%8D%E7%BD%AE.html#%E9%9D%9E%E9%98%BB%E5%A1%9E%E6%8C%82%E8%BD%BD> "Dm-crypt/系统配置")。 

由于挂载服务默认仅会为文件系统可用等待 90 秒，因此任何对密钥文件可用性的延迟都可能导致挂载失败。为避免该情况出现，可以在 fstab 中添加 `x-systemd.mount-timeout=0` 选项，以使挂载服务一直等待到分区解锁完成。 
    
    /etc/fstab
    
    UUID=0a3407de-014b-458b-b5c1-848e92a327a3 /data ext4 defaults,nofail,x-systemd.device-timeout=0    0 2

####  自动卸载

可以通过 `x-systemd.idle-timeout` 参数来为挂载设置一个空闲超时时间。举个例子： 
    
    x-systemd.automount,x-systemd.idle-timeout=1min
    
这会使 systemd 在设备空闲 1 分钟后卸载它。 

###  外部设备

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** nofail 选项无法按以下描述工作。（在 [Talk:Fstab#3.2 External Device options](</wzh/index.php?title=Talk:Fstab&action=edit&redlink=1> "Talk:Fstab（页面不存在）") 中讨论）

对于仅在可用时挂载，未找到时忽略的外部设备，需要使用 `nofail` 选项。该选项可在启动时防止出现报错。例如： 
    
    /etc/fstab
    
    LABEL=MyExternalDrive /media/backup    jfs    nofail,x-systemd.device-timeout=5    0  2

建议将 `nofail` 选项搭配 `x-systemd.device-timeout` 选项使用，原因是默认设备超时时间是 90 秒，因此除非按如上进行配置，否则仅包含 `nofail` 选项且未连接的外部设备将使启动时间延长 90 秒。务必确保超时时间没有设为 0 秒，这会将超时时间设为无限。 

###  路径名有空格

因为空格在 `fstab` 中用于划分列，如果任意一列（ _PARTLABEL_ ， _LABEL_ 或挂载点）中含有空格，这些空格必须被替换为转义符 `\` 后面跟着三位数八进制代码 `040`： 
    
    /etc/fstab
    
    UUID=47FA-4071         /home/username/Camera\040Pictures   vfat  defaults      0  0
    LABEL=Storage\040drive /media/100\040GB\040(Storage)       ext4  defaults,user 0  2

###  atime 参数

下列 atime 选项可能影响驱动器性能。 

  * `strictatime` 选项会在文件每次被访问时更新它们的访问时间。这更多用于 Linux 服务器，而对于桌面用户并没有多少价值。`strictatime` 选项的缺点是即使从页面缓存中读取文件（从内存而不是从驱动器读取）也会导致一次写入。
  * `noatime` 选项将在读取文件时不将文件访问时间写入驱动器。开启这个选项对多数应用不会产生影响，除了那些需要知道文件自上次修改后是否被访问的应用。在启用此选项的情况下，只要写入文件，文件的写入时间信息就会更新。
  * `nodiratime` 选项仅对目录禁用文件访问时间的写入，而其他文件仍会写入访问时间。

**注意：**`noatime` 包含了 `nodiratime`。[你不需要同时启用两个选项](<https://lwn.net/Articles/244941/>)。

  * `relatime` 仅当先前访问时间早于当前修改时间时才会更新访问时间。此外，从 Linux 2.6.30 开始，如果与之前的访问时间间隔超过 24 小时，则始终会更新访问时间。在使用 `defaults` 选项，`atime` 选项（即使用内核默认值 `relatime`；具体信息请参考 [mount(8)](<https://man.archlinux.org/man/mount.8>) 和 [Once upon atime](<https://lwn.net/Articles/244829/>)）或没指定任何选项时，将启用该选项。

在使用 [Mutt](<../zh-cn/Mutt.html> "Mutt") 或其它需要知道一个文件自上次修改后是否被读取的应用时，不应该使用 `noatime` 选项；可以使用 `relatime`，同时还能获得性能提升。 

自从内核 4.0 版本起还有另一个相关的选项： 

  * `lazytime` 通过仅在内存中维护对 inode 时间戳的更改（包括访问、修改和创建时间）来减少对磁盘的写入。硬盘上的时间戳仅在以下情况下更新：(1) 文件 inode 需要针对与文件时间戳无关的某些更改进行更新，(2) 发生与硬盘的同步，(3) 从内存中逐出未删除的 inode 或 (4) 自上次将内存中的副本写入硬盘已超过 24 小时。

**警告：** 如果系统崩溃，硬盘上的访问和修改时间可能会距当前时间过时最多 24 小时。

注意， `lazytime` 并不用于替代上述 `*atime` 选项，而是与它们**搭配** 使用。默认会与 `relatime` 搭配，但在搭配 `strictatime` 时的硬盘写入损耗也较纯 `relatime` 选项相同设置更低。 

###  重新挂载根分区

如果出于某些原因根分区被错误挂载为只读，通过以下命令可以将根分区以读写访问重新挂载： 
    
    # mount -o remount,rw /
    
###  GPT 分区自动挂载

在根据[可发现分区规范](<https://uapi-group.org/specifications/specs/discoverable_partitions_specification/>)进行了分区的情况下，使用 UEFI/GPT 时可以在 `/etc/fstab` 中省略部分分区，并让 [systemd-gpt-auto-generator(8)](<https://man.archlinux.org/man/systemd-gpt-auto-generator.8>) 自动进行挂载。具体信息请参考 [systemd#GPT分区自动挂载](<../zh-cn/Systemd.html#GPT%E5%88%86%E5%8C%BA%E8%87%AA%E5%8A%A8%E6%8C%82%E8%BD%BD> "Systemd")。 

可以将 `/dev/gpt-auto-root` 作为设备名称来为根分区指定挂载选项： 
    
    /etc/fstab
    
    /dev/gpt-auto-root  /  ext4  defaults,noatime  0  1

###  Bind 挂载

你可以使用 `bind` 选项链接目录： 
    
    /etc/fstab
    
    # <device>                             <dir>                         <type> <options>     <dump> <fsck>
    UUID=94649E22649E06E0                  /media/user/OS/               ntfs    defaults,rw,errors=remount-ro  0  0
    /media/user/OS/Users/user/Music/       /home/user/Music/             none    defaults,bind 0   0
    /media/user/OS/Users/user/Pictures/    /home/user/Pictures/          none    defaults,bind 0   0
    /media/user/OS/Users/user/Videos/      /home/user/Videos/            none    defaults,bind 0   0
    /media/user/OS/Users/user/Downloads/   /home/user/Downloads/         none    defaults,bind 0   0
    /media/user/OS/Users/user/Documents/   /home/user/Documents/         none    defaults,bind 0   0
    /media/user/OS/Users/user/projects/    /home/user/projects/windows/  none    defaults,bind 0   0

详情请见 [mount(8) § Bind mount operation](<https://man.archlinux.org/man/mount.8#Bind_mount_operation>)。 

###  通过 genfstab 自动生成 fstab

可以使用 _genfstab_ 来创建 fstab 文件，具体信息请参考 [genfstab](<../zh-cn/Genfstab.html> "Genfstab"). 

###  GUI 工具

以下为一系列可用于修改挂载点的工具，它们的 fstab 编辑功能可能不完整，但常用的功能都有，可以简化你的工作流： 

  * **[GNOME Disks](<https://en.wikipedia.org/wiki/GNOME_Disks> "wikipedia:GNOME Disks")** — 用于处理存储设备的 GNOME 工具，是 [gnome](<https://archlinux.org/groups/x86_64/gnome/>)包组 的一部分。

     <https://apps.gnome.org/DiskUtility/> || [gnome-disk-utility](<https://archlinux.org/packages/?name=gnome-disk-utility>)包

  * **KDE Partition Manager** — 可用于管理电脑上的硬盘、分区和文件系统的工具，是 [kde-system](<https://archlinux.org/groups/x86_64/kde-system/>)包组 的一部分。

     <https://apps.kde.org/partitionmanager/> || [partitionmanager](<https://archlinux.org/packages/?name=partitionmanager>)包

###  修改用户权限和所有权

如果你希望所有用户都能挂载某个硬盘，可以考虑在 fstab 的对应项中添加以下挂载选项： 

**注意：** 同样可用于没有文件权限功能的文件系统，效果为硬盘的所有者和权限被设为挂载该盘的用户。

  * `users` \- 允许任意用户挂载和卸载（即使由其他用户挂载）对应的文件系统。该选项隐式包含了 noexec，nosuid 和 nodev 选项（除非被类似 users，exec，dev 和 suid 的选项覆盖）。
  * `user` \- 允许一个普通用户挂载对应的文件系统，且仅允许同一个用户进行卸载。该选项隐式包含了 noexec，nosuid 和 nodev 选项（除非被类似 users，exec，dev 和 suid 的选项覆盖）。

对于没有文件权限功能的文件系统（例如 FAT 和 exFAT），可以显式指定整个硬盘和其中的文件的用户和用户组。可以通过 `/etc/passwd` 查找特定用户的 ID，其中第三列是用户 ID（UID），第四列是组 ID（GID）。 

  * `uid` \- 设置硬盘的所有者 ID
  * `gid` \- 设置硬盘的组 ID

对于 ext4，btrfs 和其他有权限功能的文件系统，其他用户可能没有查看硬盘的权限。请检查硬盘下的文件权限，并根据需要进行修改。 

###  验证修改

可以通过 `findmnt --verify --verbose` 检查 fstab 中的语法错误和无效选项。 

##  参见

  * [完整的设备列表，包括块设备](<https://docs.kernel.org/admin-guide/devices.html>)
  * [文件系统层次标准](<https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html>)
  * [通过 TMPFS 获取 30 倍更快的缓存与网站浏览速度](<https://www.askapache.com/optimize/super-speed-secrets/>)
