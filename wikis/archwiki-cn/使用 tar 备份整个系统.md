相关文章

  * [系统备份](<../zh-cn/%E7%B3%BB%E7%BB%9F%E5%A4%87%E4%BB%BD.html> "系统备份")
  * [Full system backup with SquashFS](</wzh/index.php?title=Full_system_backup_with_SquashFS&action=edit&redlink=1> "Full system backup with SquashFS（页面不存在）")

本篇介绍如何使用 [tar](<../zh-cn/%E5%BD%92%E6%A1%A3%E4%B8%8E%E5%8E%8B%E7%BC%A9.html> "Tar") 进行全系统备份。 

使用 tar 进行备份具有压缩的优点，有助于节省磁盘空间，且使用简单。此过程只需要以下几个步骤： 

  1. 从 LiveCD 启动
  2. Change root 到 Linux 系统安装位置
  3. 装载其他（如有的话）分区/驱动器
  4. 添加排除对象
  5. 使用备份脚本进行备份

为最大限度减少停机时间，如果所有文件系统均驻留在 LVM 卷中，则可以使用[LVM 快照](<../zh-cn/LVM.html#Snapshots> "LVM")在正在运行的系统上进行备份。 

##  从 LiveCD 启动

许多 Linux 可启动 CD、U盘等能够 change root 到系统安装位置。虽然不是必须 change root 才能执行备份，但这提供了运行脚本的功能，而无需将其传输到临时驱动器或必须在文件系统中找到它。Live 媒体必须与已安装的 Linux 系统的架构相同（即 i686 或 x86_64）。 

## Change root

首先，应该在当前的 Linux 安装系统中设置一个脚本环境。如果您不知道这是什么，这表示您可以执行拥有的任意脚本，它们是常规程序一样。如果您的系统未设置好，请参阅这[文档](<https://linuxtidbits.wordpress.com/2009/12/03/setting-up-a-scripting-environment/>)了解如何操作。接下来要做的是 change root，要了解有关 change root 的更多信息，请参阅[此文档](<../zh-cn/Change_root.html> "Change root")。Change root 时，不需要装载任何临时文件系统（`/proc`、`/sys` 和 `/dev`）。临时文件系统在系统启动时填充，实际上不需要备份它们，因为它们会干扰正常（和必要的）填充过程，该过程会在任何升级时更改。要 change root，需要装载当前的 Linux 安装的 root 分区。示例： 
    
    # mkdir /mnt/arch
    # mount /dev/_your-partition-or-drive_
    
使用 `fdisk -l` 查询分区和驱动器。然后 [chroot](<../zh-cn/Chroot.html> "Chroot")： 
    
    # cd /mnt/arch
    # chroot . /bin/bash
    
**警告：** 不要使用 `arch-chroot` 来 chroot 到目标系统 - 备份过程将会失败，因为这将尝试备份临时文件系统、所有系统内存和其他所有东西。请使用普通的 `chroot`。

此示例明显使用 bash，但也可以使用其他可用的 shell。现在，您应处于脚本环境中（前提是您在输入时有获取 `~/.bashrc`）： 
    
    ~/.bash_profile
    
    # 如果使用 bash，获取本地 .bashrc
    source ~/.bashrc
    
##  装载其他分区

要使用的其他分区（如果有的话）需要装载到适当的位置（例如，如果有单独的 `/home` 分区）。 

##  排除文件

_tar_ 能够忽略指定的文件和目录。语法是每行一个定义。 _tar_ 还可以理解正则表达式（regexp）。示例： 
    
    # 排除旧的备份                                                               
    /opt/backup/arch-full*                                                                   
                                                                                    
    # 排除临时文件                                                           
    /tmp/*
    
    # 排除 pacman 的缓存
    /var/cache/pacman/pkg/
    ...
    
##  备份脚本

使用 tar 备份是一个直接过程。以下是一个进行备份的基本脚本，并提供了几项检查。需要修改此脚本以定义备份位置，并排除文件（如果有的话），然后在 `chroot` 和装载所有分区之后运行此脚本。 
    
    #!/bin/bash
    # 全系统备份
    
    # 备份目标位置
    backdest=/opt/backup
    
    # 备份名称标签
    #PC=${HOSTNAME}
    pc=pavilion
    distro=arch
    type=full
    date=$(date "+%F")
    backupfile="$backdest/$distro-$type-$date.tar.gz"
    
    # 排除文件位置
    prog=${0##*/} # 文件名中的程序名称
    excdir="/home/<user>/.bin/root/backup"
    exclude_file="$excdir/$prog-exc.txt"
    
    # 检查 chroot 提示
    echo -n "来自 LiveCD 的第一个 chroot。确定开始备份？ (y/n)："
    read executeback
    
    # 检查排除文件是否存在
    if [ ! -f $exclude_file ]; then
      echo -n "没有排除文件，是否继续？ (y/n)："
      read continue
      if [ $continue == "n" ]; then exit; fi
    fi
    
    if [ $executeback = "y" ]; then
      # -p、--acls 和 --xattrs 存储所有权限、ACL 和扩展属性。如果没有这些属性，许多程序会停止工作！
      # 可以安全地移除详细信息标志（-v）。如果使用的终端速度较慢，这可以加快备份过程。
      tar --exclude-from=$exclude_file --acls --xattrs -cpvf $backupfile /
    fi

##  恢复

要恢复以前的备份，需要装载所有相关分区更改当前工作目录为 root，然后执行 
    
    $ tar --acls --xattrs -xpf _backupfile_
    
_backupfile_ 替换为备份存档文件。必须手动删除备份以来添加的所有文件。最简单的方法是重新创建文件系统。 

##  并行压缩备份

要使用并行压缩（[SMP](<https://en.wikipedia.org/wiki/Symmetric_multiprocessing> "wikipedia:Symmetric multiprocessing")），可以使用 [pbzip2](<https://archlinux.org/packages/?name=pbzip2>)包（Parallel bzip2）： 
    
    # tar -cvf /path/to/chosen/directory/etc-backup.tar.bz2 -I pbzip2 /etc
    
将 `etc-backup.tar.bz2` 文件存储到一个或多个脱机媒体上，如U盘、外置硬盘或光盘。有时，需要通过比较原始文件和目录与其备份文件来验证备份的完整性。可以维护备份文件的 hash 列表，以使比较过程更快速。 

可以通过在临时工作目录中提取 `etc-backup.tar.bz2` 文件，并根据需要复制单个文件和目录来恢复损坏的 `/etc` 文件。要恢复整个 `/etc` 目录及其所有内容，可以以 root 身份执行以下命令： 
    
    # tar -xvf etc-backup.tar.bz2 -C /
    