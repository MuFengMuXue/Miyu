[![](../File:Merge-arrows-2.png)](<../File:Merge-arrows-2.png>)**本文或本章节可能需要合并到[fstab#Tips and tricks](<../zh-cn/Fstab.html#Tips_and_tricks> "Fstab")。**

**附注：** There is not enough content for a separate article. The [genfstab(8)](<https://man.archlinux.org/man/genfstab.8>) man page provides everything besides the warnings and examples.（在 [Talk:Genfstab](<../zh-cn/Talk:Genfstab.html>) 中讨论）

相关文章

  * [fstab](<../zh-cn/Fstab.html> "Fstab")
  * [块设备持久化命名](<../zh-cn/%E5%9D%97%E8%AE%BE%E5%A4%87%E6%8C%81%E4%B9%85%E5%8C%96%E5%91%BD%E5%90%8D.html> "块设备持久化命名")
  * [文件系统](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html> "文件系统")

**翻译状态：**

  * 本文（或部分内容）译自 [Genfstab](<https://wiki.archlinux.org/title/Genfstab> "arch:Genfstab")，最近一次同步于 2024-7-30，若英文版本有所[更改](<https://wiki.archlinux.org/title/Genfstab?diff=0&oldid=813302>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Genfstab_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

_genfstab_ 是一个 [Bash](<../zh-cn/Bash.html> "Bash") 脚本，用于自动检测给定挂载点下的所有挂载，然后将其输出重定向到一个文件中，通常是 `/etc/fstab`。 

##  安装

Arch 安装介质中默认包含该程序，也可作为 [arch-install-scripts](<https://archlinux.org/packages/?name=arch-install-scripts>)包 软件包的一部分安装到已安装的系统中。 

该工具还有一个独立的分支，可以在其他发行版上使用，你可以[在此处](<https://github.com/glacion/genfstab/tree/master>)找到它。 

##  用法

您可以使用以下命令获取当前的挂载的列表： 
    
    $ genfstab /
    
脚本支持通过内核描述符、设备/分区标签或设备/分区 UUID 查找挂载。默认情况下，它将输出 `kernel descriptor`（ kernel descriptor 为 `/dev/_xxx_`），你可以使用 `-L`, `-t PARTLABEL`, `-U` 或 `-t PARTUID` 分别表示文件系统标签、GPT 分区标签、文件系统 UUID 或 GPT 分区 UUID。 

**警告：**[块设备的内核名称描述符](<../zh-cn/%E8%AE%BE%E5%A4%87%E6%96%87%E4%BB%B6.html#%E5%9D%97%E8%AE%BE%E5%A4%87%E5%90%8D> "设备文件")不是[持久的](<../zh-cn/%E5%9D%97%E8%AE%BE%E5%A4%87%E6%8C%81%E4%B9%85%E5%8C%96%E5%91%BD%E5%90%8D.html> "块设备持久化命名")，每次启动都会更改，因此不应在配置文件（包括 `/etc/fstab`）中使用。

更常见的使用情况是为 [chroot](<../zh-cn/Chroot.html> "Chroot") 获取一个 [fstab](<../zh-cn/Fstab.html> "Fstab")，为此你需要执行类似下面的操作： 
    
    # mount /dev/sda3 /mnt
    # mount --mkdir /dev/sda1 /mnt/efi
    
    $ genfstab -U /mnt
    
    # /dev/sda3
    UUID=185aebd2-ce76-47dd-baf4-5ad0a80fa963       /               ext4            rw,noatime      0 1
    
    # /dev/sda1
    UUID=E5C7-6DD7          /efi       vfat             rw,relatime,fmask=0077,dmask=0077,codepage=437,iocharset=ascii,shortname=mixed,utf8,errors=remount-ro   0 2

在这种情况下，`genfstab` 会显示 `/mnt` 下的挂载，并按照设备 `UUID` 列出。 

**提示：** 请注意，我们将设备 `sda3` 挂载到了 `/mnt` 中，但 genfstab 却将其显示为主根挂载点 `/`，这是因为它将给定的挂载点视为根挂载点。

通常情况下，您希望将输出重定向到一个文件，这可以通过以下方法实现： 
    
    # genfstab -U /mnt >> /mnt/etc/fstab
    
**警告：**

  * 确保在覆盖现有 [fstab](<../zh-cn/Fstab.html> "Fstab") 之前创建了一个备份。
  * 注意保存 fstab 文件的位置，例如，如果要为 chroot 创建该文件，则不要覆盖主安装上的文件。

##  参见

  * [genfstab(8)](<https://man.archlinux.org/man/genfstab.8>)
