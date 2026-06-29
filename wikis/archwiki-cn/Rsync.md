相关文章

  * [系统备份](<../zh-cn/%E7%B3%BB%E7%BB%9F%E5%A4%87%E4%BB%BD.html> "系统备份")
  * [同步和备份程序](<../zh-cn/%E5%90%8C%E6%AD%A5%E5%92%8C%E5%A4%87%E4%BB%BD%E7%A8%8B%E5%BA%8F.html> "同步和备份程序")

**翻译状态：**

  * 本文（或部分内容）译自 [rsync](<https://wiki.archlinux.org/title/rsync> "arch:rsync")，最近一次同步于 2024-05-21，若英文版本有所[更改](<https://wiki.archlinux.org/title/rsync?diff=0&oldid=804175>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/rsync_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[rsync](<https://samba.anu.edu.au/rsync/>) 是一个开源工具，可以进行快速的增量文件传输。 

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [rsync](<https://archlinux.org/packages/?name=rsync>)包 软件包。 

必须在源计算机和目标计算机上都安装 _rsync_ 。 

###  前端

  * **Grsync** — GTK 前端。

     <https://www.opbyte.it/grsync/> || [grsync](<https://archlinux.org/packages/?name=grsync>)包

  * **JotaSync** — 用于 rsync 的 Java Swing GUI，内置计划功能。

     <https://trixon.se/projects/jotasync/> || [jotasync](<https://aur.archlinux.org/packages/jotasync/>)AUR

  * **luckyBackup** — 用 C++ 编写的 Qt 前端。

     <https://luckybackup.sourceforge.net/index.html> || [luckybackup](<https://aur.archlinux.org/packages/luckybackup/>)AUR

其他使用 rsync 的工具是 [rdiff-backup](<https://aur.archlinux.org/packages/rdiff-backup/>)AUR, [osync](<https://aur.archlinux.org/packages/osync/>)AUR 和 [yarsync](<https://aur.archlinux.org/packages/yarsync/>)AUR。 

##  作为 cp/mv 的替代

**注意：** 在不同的文件系统之间使用 rsync 而不是 cp/mv 是高效的，但对于在同一个文件系统上复制或移动文件却不然。参见 [[1]](<https://bbs.archlinux.org/viewtopic.php?id=271953>)

rsync 可以作为 `cp` 或 `mv` 命令的高级替代品，特别是对于较大文件的复制： 
    
    $ rsync -P source destination
    
其中 `-P` 与 `--partial --progress` 选项的作用是相同的，该选项使得文件可以分块传输并显示传输过程中的进度。 

您可能需要使用 `-r`/`--recursive` 选项递归到目录中传输。 

可以像 cp 命令一样本地复制文件，但 rsync 令人激动的用途在于远程复制文件，例如在两个不同的主机之间。远程位置可以用主机加冒号进行指定： 
    
    $ rsync source host:destination
    
或者 
    
    $ rsync host:source destination
    
网络文件传输默认使用[SSH](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH")协议，`host` 可以是真实的主机名或来自于 `.ssh/config` 的预先定义的配置文件/别名。 

无论是本地或远程文件传输，rsync 首先会创建一个文件列表，其中含有接下来会被用于确定各个文件是否需要构建的信息（默认为文件大小和上次修改时间戳）。对于每个需要构建的文件，都会找出其所有块（长度**S** 字节，不重叠，偏移量可由**S** 整除）的一个弱校验和和一个强校验和。使用这一信息，一个大文件就可以由 rsync 构建，而无需传输整个文件。更详细的实际解释和详细的数学解释见 [rsync 如何工作](<https://rsync.samba.org/how-rsync-works.html>)及 [rsync 算法](<https://rsync.samba.org/tech_report/tech_report.html>)。 

要快速使用合理默认值，可以使用一些别名： 
    
    cpr() {
      rsync --archive -hh --partial --info=stats1,progress2 --modify-window=1 "$@"
    } 
    mvr() {
      rsync --archive -hh --partial --info=stats1,progress2 --modify-window=1 --remove-source-files "$@"
    }

  * `-hh`: 以人类可读的格式输出数字
  * `--info=stats1,progress2`: `stats1` 使用详细级别1显示 rsync 传输统计信息。`progress2` 打印总的传输进度，而不是每个文件的传输进度(`progress1`)
  * `--modify-window=1`: 当比较两个文件的时间戳时，如果时间戳的差异小于1秒，则将它们的时间戳视为相等
  * `--remove-source-files`: 成功同步后从源目录中删除文件

**注意：** 此处对 _校验和_ 这一名词的使用与 `--checksum` 选项的行为**不是** 相等价的。`--checksum` 选项影响的是在传输任何文件之前使用的决定是否跳过文件的启发式方法。在基于块的文件构建中一定会使用 _校验和_ ，这是 rsync 传输文件的方法，与 `--checksum` 无关。

###  注意尾部的斜杠

Arch 默认使用 GNU cp ([coreutils](<https://archlinux.org/packages/?name=coreutils>)包 的一部分)。 然而，rsync 遵循 BSD cp 的约定, 源目录后面带有一个斜杠“/”有着特殊的处理。比如命令 
    
    $ rsync -r source destination
    
创建一个包含"source"的内容的"destination/source"目录。而命令 
    
    $ rsync -r source/ destination
    
把"source/"目录下的所有文件全部复制到"destination"目录下，而没有中间的子目录，和以下命令一样： 
    
    $ rsync -r source/. destination
    
这与 GNU cp 的行为是不同的，在 GNU cp 中"source" 与 "source/" 意义相同 ("source/."则不然)。并且，一些shell在Tab补全目录名的时候自动追加尾部下划线。由于这些因素，新手或偶尔使用 rsync 的用户可能倾向于忘记 rsync 的不同行为，在命令行上留下了尾部斜杠，从而无意间弄错，甚至覆盖重要文件。 

谨慎起见，可以使用包装脚本在调用 rsync 之前自动删除尾部斜杠： 
    
    #!/bin/bash
    new_args=()
    for i in "${@}"; do
        case "${i}" in
            /)
                i="/"
            ;;
            */)
                i="${i%/}"
            ;;
            esac
        new_args+=("${i}")
    done
    exec rsync "${new_args[@]}"
    
该脚本可以放在 path 中的某个位置，并在 shell 的 init 文件中指定别名为 rsync。 

##  作为备份工具

rsync 协议可以很容易地用于备份，只传输自上次备份以来已更改的文件。本节将介绍一些简单的基于 rsync 的计划备份脚本，通常用于复制到可移动介质。 

###  自动备份

以下面的脚本为例，该脚本放置于 `/etc/cron.daily` 目录下，如果 cron [守护程序](<../zh-cn/Systemd.html> "守护程序")被正确安装和配置，它将每天运行。配置和使用 [cron](<../zh-cn/Cron.html> "Cron") 是本文的范围之外。 

首先，创建一个包含相应命令选项的脚本： 
    
    /etc/cron.daily/backup
    
    #!/bin/sh
    rsync -a --delete --quiet /path/to/backup /location/of/backup

`-a`
    表示文件应被存档，这意味着他们的大部分特性被保留 (**不** 包括 ACLs, 硬链接或扩展属性，如 capabilities)
`--delete`
    指同步源的删除操作。

在这里，`/path/to/backup` 应该改成需要被备份的路径 (比如 `/home`)，`/location/to/backup` 是备份应存放的位置 (比如 `/media/disk`). 

最后，脚本必须[可执行](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%9D%83%E9%99%90> "可执行")。 

###  通过 SSH 自动备份

如果是通过 [SSH](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH") 备份到远程主机，改为使用此脚本： 
    
    /etc/cron.daily/backup
    
    #!/bin/sh
    rsync -a --delete --quiet -e ssh /path/to/backup remoteuser@remotehost:/location/of/backup
    
`-e ssh`
    告诉rsync的使用SSH
`remoteuser`
    远程主机 `remotehost` 上的用户名
`-a`
    组中的所有这些选项 `-rlptgoD` (recursive, links, perms, times, group, owner, devices)

**注意：** 在每次增量备份的时候，Rsync 都会试着修改目标主机上所有先前备份过的文件以匹配源主机上的文件状态。这意味着在通过 SSH （并且使用 `-a`选项保留权限和所有者的时候）备份属于 root 的文件，需要目标主机的 root 权限。通常的办法是将 SSH 守护程序设置为允许使用[公钥而不是密码](<https://unix.stackexchange.com/a/92397>)登录，并以 root 用户运行 rsync 命令。

###  使用 NetworkManager 自动备份

该脚本在网络连接后开始备份。 

首先，创建一个包含相应命令选项的脚本： 
    
    /etc/NetworkManager/dispatcher.d/backup
    
    #!/bin/sh
    
    if [ x"$2" = "xup" ] ; then
            rsync --force --ignore-errors -a --delete --bwlimit=2000 --files-from=files.rsync /path/to/backup /location/of/backup
    fi

`-a`
    组中的所有选项 `-rlptgoD` recursive, links, perms, times, group, owner, devices
`--files-from`
    从文件中读取到备份路径`/path/to/backup`的相对路径
`--bwlimit`
    限 I/O 带宽；每秒千字节

这个脚本必须属于 root 用户 (参见 [NetworkManager#使用 NetworkManager 调度网络服务](<../zh-cn/NetworkManager.html#%E4%BD%BF%E7%94%A8_NetworkManager_%E8%B0%83%E5%BA%A6%E7%BD%91%E7%BB%9C%E6%9C%8D%E5%8A%A1> "NetworkManager") )。 

###  使用 systemd 和 inotify 自动备份

**注意：**

  * 由于 inotify 和 systemd 的限制， (见 [这个问题和回答](<https://www.quora.com/Linux-Kernel/Inotify-monitoring-of-directories-is-not-recursive-Is-there-any-specific-reason-for-this-design-in-Linux-kernel>))，递归的文件系统监测是不可能的。即使你监测了一个目录和它的内容，它也不会递归子目录并检测其中的内容。你必须明确地指出所有需要检测的目录，就算这些目录是你已经监视的目录的子目录。
  * 以下设置基于一个 [systemd/用户](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "Systemd/用户") 的实例。

相比于执行一个基于时间计划的定时备份，比如使用 [cron](<../zh-cn/Cron.html> "Cron")，在每次文件变动的时候都执行备份也是可行的。`systemd.path` 单元使用 `inotify` 以监测文件系统，并且可以与 `systemd.service` 文件一同使用来在捕获到文件系统事件的时候启动任何进程（如你的 rsync 备份）。 

首先，创建监测备份文件的 `systemd.path` 文件： 
    
    ~/.config/systemd/user/backup.path
    
    [Unit]
    Description=Checks if paths that are currently being backed up have changed
    
    [Path]
    PathChanged=%h/documents
    PathChanged=%h/music
    
    [Install]
    WantedBy=default.target
    
然后创建一个 `systemd.service` 文件，它将会在检测到变化的时候启动。默认情况下一个与 `.path` 单元同名(本例中为 `backup.path`)，但以 `.service` 结尾的服务（本例中为 `backup.service`）将会启动。 

**注意：** 如果你需要运行多个 rsync 命令，使用 `Type=oneshot`。这将允许你指定多个 `ExecStart=` 参数，每个参数对应一个 rsync 命令。更简单的方法是写一个脚本来启动你所有的备份，就像 [cron](<../zh-cn/Cron.html> "Cron") 脚本一样。
    
    ~/.config/systemd/user/backup.service
    
    [Unit]
    Description=Backs up files
    
    [Service]
    ExecStart=/usr/bin/rsync %h/./documents %h/./music -CERrltm --delete ubuntu:
    
现在只需要像普通的 systemd 服务那样，[启动/启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动/启用") `backup.path` 它就会开始监测文件变化并且自动启动 `backup.service` 了。 

###  每周差异备份

这个 rsync 选项很有用，每次运行时创建一个完整备份，并且每天在一个单独的目录中保留已修改文件的差异备份副本。 

首先，创建一个包含相应命令选项的脚本： 
    
    /etc/cron.daily/backup
    
    #!/bin/sh
    
    DAY=$(date +%A)
    
    if [ -e /location/to/backup/incr/$DAY ] ; then
      rm -fr /location/to/backup/incr/$DAY
    fi
    
    rsync -a --delete --quiet --inplace --backup --backup-dir=/location/to/backup/incr/$DAY /path/to/backup/ /location/to/backup/full/

`--inplace` 选项包含 `--partial` ，就地更新目标文件。 

###  快照备份

同样你也可以用这个工具来创建你文件的快照树（即一个有日期顺序的文件副本的目录）。这个快照树是基于硬链接的，这意味着只有修改过的文件才会占用空间。这也是苹果 TimeMachine 的原理。 

实现这个功能的脚本很容易实现，使用 `--link-dest` 选项来创建增量快照，硬链接未改变的文件： 
    
    /usr/local/bin/snapbackup.sh
    
    #!/bin/sh
    
    # 基本的快照式 rsync 备份脚本
    
    # 配置
    OPT="-aPh"
    LINK="--link-dest=/snapshots/username/last/" 
    SRC="/home/username/files/"
    SNAP="/snapshots/username/"
    LAST="/snapshots/username/last"
    date=`date "+%Y-%b-%d:_%T"`
    
    # 运行 rsync 以创建快照
    rsync $OPT $LINK $SRC ${SNAP}$date
    
    # 删除指向上一个快照的符号链接
    rm -f $LAST
    
    # 创建到最新快照的新符号链接，以便下次备份到硬链接
    ln -s ${SNAP}$date $LAST
    
这里必须有一个指向完整备份的符号链接，以作为 `--link-dest` 的目标。如果最近的快照被删除，那么就需要重新创建一个指向新的快照的符号链接。如果 `--link-dest` 没有找到有效的符号链接，rsync将继续复制所有文件，而不只复制变化。 

一个更加复杂一点的版本每次保留一个最新的完整备份到 `$SNAP/latest` 。若自上次完整备份起有一定数量的文件发生了变化，那么脚本将创建一个新的快照到 `$SNAP/$DATETAG` ，并使用 `cp -al` 来硬链接未改变的文件： 
    
    /usr/local/bin/rsnapshot.sh
    
    #!/bin/sh
    
    ## 我自己的基于 rsync 的快照式备份过程
    ## (cc) marcio rps AT gmail.com
    
    # 配置变量
    
    SRC="/home/username/files/" #dont forget trailing slash!
    SNAP="/snapshots/username"
    OPTS="-rltgoi --delay-updates --delete --chmod=a-w"
    MINCHANGES=20
    
    # 以低优先级运行此进程
    
    ionice -c 3 -p $$
    renice +12  -p $$
    
    # 同步
    
    rsync $OPTS $SRC $SNAP/latest >> $SNAP/rsync.log
    
    # 检查是否有足够的变化，如果有
    # 则制作一份以日期命名的硬链接副本
    
    COUNT=$( wc -l $SNAP/rsync.log|cut -d" " -f1 )
    if [ $COUNT -gt $MINCHANGES ] ; then
            DATETAG=$(date +%Y-%m-%d)
            if [ ! -e $SNAP/$DATETAG ] ; then
                    cp -al $SNAP/latest $SNAP/$DATETAG
                    chmod u+w $SNAP/$DATETAG
                    mv $SNAP/rsync.log $SNAP/$DATETAG
                   chmod u-w $SNAP/$DATETAG
             fi
    fi
    
懒得手动运行的话，你也可以让这个脚本作为 [systemd/定时器](<../zh-cn/Systemd/%E5%AE%9A%E6%97%B6%E5%99%A8.html> "Systemd/定时器")单元运行。 

###  全盘系统备份 

本节介绍使用rsync传输整个/树的副本，不包括一些选定的目录。这种方法被认为比使用dd进行磁盘克隆更好，因为它允许使用不同的大小、分区表和文件系统，也比使用cp-a进行复制更好，因为其允许对文件权限、属性、访问控制列表和扩展属性进行更大的控制。 本节是关于使用 _rsync_ 来创建一份整个 `/` 树的副本，其中不包含特定的几个文件夹。此方法相较于使用 `dd` 来进行[硬盘克隆](<../zh-cn/Disk_cloning.html> "Disk cloning")要更佳，因为它允许你在使用不同大小、分区表和文件系统的存储设备间传输；也比 `cp -a` 更好，因为它允许你对文件权限、属性、[访问控制列表](<../zh-cn/%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6%E5%88%97%E8%A1%A8.html> "访问控制列表")和[扩展属性](<../zh-cn/%E6%96%87%E4%BB%B6%E6%9D%83%E9%99%90%E4%B8%8E%E5%B1%9E%E6%80%A7.html#%E6%89%A9%E5%B1%95%E5%B1%9E%E6%80%A7> "文件权限与属性")有更好的掌握。 

_rsync_ 在系统运行时亦可进行备份，但传输期间改变的文件可能不会被备份。这可能会造成使用这些文件的程序的一些未知错误或未定义行为。为缓解这个问题，可以注销所有用户并关闭所有程序和数据库。 

这种方法对于将现有的已安装系统迁移到新的硬盘或[固态硬盘](<../zh-cn/%E5%9B%BA%E6%80%81%E7%A1%AC%E7%9B%98.html> "固态硬盘")上非常有效。 

在 root 权限下运行此命令，以确保 rsync 能访问到所有系统文件，并且保留权限： 
    
     # rsync -aAXHv --exclude='/dev/*' --exclude='/proc/*' --exclude='/sys/*' --exclude='/tmp/*' --exclude='/run/*' --exclude='/mnt/*' --exclude='/media/*' --exclude='/lost+found/' / _/path/to/backup_
    
通过使用 `-aAX` 选项集，文件以归档模式传输，确保符号链接、设备、权限、所有权、修改时间、[ACLs](<../zh-cn/%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6%E5%88%97%E8%A1%A8.html> "访问控制列表")和扩展属性得以保留，前提是目标[文件系统](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html> "文件系统")支持这一功能。选项 `-H` 保留了硬链接，但会使用更多的内存。 

`--exclude` 选项使符合给定模式的文件/文件夹被排除。可以结合使用`--exclude-from=_file_`选项，排除与` _file_`中的模式（每条一个）相匹配的文件/目录。这与[#筛选规则的高级用法](<#%E7%AD%9B%E9%80%89%E8%A7%84%E5%88%99%E7%9A%84%E9%AB%98%E7%BA%A7%E7%94%A8%E6%B3%95>)中描述的例子类似，但不需要`+`/`-`语法。 

在上述命令中，`/dev`、`/proc`、`/sys`、`/tmp`和`/run` 等目录被包括在内，但这些目录的内容被排除在外。这是因为它们在系统启动时才会被填入内容，但这些目录本身不会被创建。 `/lost+found` 是针对文件系统的。为排除模式加上引号可以避免被 [shell](<../zh-cn/Command-line_shell.html> "Command-line shell") 误扩展，例如，在通过 [SSH](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH") 备份时，这是必要的。以 `*` 结尾的排除路径可以确保目录本身在不存在的情况下被创建。 

**注意：**

  * 如果计划将系统备份到 `/mnt` 或 `/media` 以外的其他位置，请不要忘记将其添加到排除的模式列表中，以避免无限循环。
  * 如果系统中有任何绑定挂载，也应排除它们，以便绑定挂载的内容只复制一次。
  * 如果使用[交换文件](<../zh-cn/Swap_file.html> "Swap file")，请确保也将其排除在外。
  * 考虑是否要备份 `/home/` 目录。如果它包含您的数据，它可能比系统大得多。另外，请考虑排除不重要的子目录，例如 `/home/*/.thumbnails/*`, `/home/*/.cache/mozilla/*`, `/home/*/.cache/chromium/*`, 和 `/home/*/.local/share/Trash/*`，具体取决于系统上安装的软件。
  * 如果安装了 [GVFS](<../zh-cn/%E6%96%87%E4%BB%B6%E7%AE%A1%E7%90%86%E5%99%A8%E5%8A%9F%E8%83%BD.html#%E6%8C%82%E8%BD%BD> "GVFS")，则必须排除 `/home/*/.gvfs`，以防止 rsync 错误。
  * 如果安装了 [Dhcpcd](<../zh-cn/Dhcpcd.html> "Dhcpcd") ≥ 9.0.0，请排除 `/var/lib/dhcpcd/*` 目录，因为它将多个系统目录作为子目录挂载在那里。

您可能希望包括其他 rsync 选项，或删除一些选项，例如以下选项。有关完整列表，请见 [rsync(1)](<https://man.archlinux.org/man/rsync.1>)。 

  * 如果您在内存非常低的系统上运行，请考虑删除 `-H` 选项；然而，这在大多数现代机器上应该没有问题。文件系统上可能有许多硬链接，具体取决于使用的软件（例如，如果您使用 [Flatpak](<../zh-cn/Flatpak.html> "Flatpak")）。许多硬链接位于 `/usr/` 目录下。
  * 如果在同一备份目录中多次运行 rsync，则可能需要添加 rsync 的 `--delete` 选项。在这种情况下，请确保源路径不以 `/*` 结尾，否则此选项将仅对源目录子目录中的文件有效，但对直接驻留在源目录内的文件无效。
  * 如果您使用任何稀疏文件，如虚拟磁盘、[Docker](<../zh-cn/Docker.html> "Docker") 映像和类似文件，则应添加 `-S` 选项。
  * `--numeric-ids` 选项将禁止映射到用户名和组名；相反，数字的组和用户 ID 将被直接传输。这在通过 [SSH](<../zh-cn/%E5%AE%89%E5%85%A8%E5%A4%96%E5%A3%B3%E5%8D%8F%E8%AE%AE.html> "SSH") 进行备份或使用 live 系统备份不同的系统盘时非常有用。
  * 选择 `--info=progress2` 选项而不是 `-v` 选项将显示整体进度信息和传输速度，而不是正在传输的文件列表。
  * 为了避免在递归时跨越文件系统边界，请添加选项 `-x`/`--one-file-system`。这将防止备份层次结构中的任何挂载点。

###  还原备份

如果希望还原备份，请使用执行的 rsync 命令，但源和目标相反。 

###  筛选规则的高级用法

rsync 可以从单个过滤器文件中读取所有这些规则，而不是单独指定包含和排除规则。rsync 以自顶向下的顺序处理规则；首先匹配的规则获胜。 
    
    backup.filter
    
    # 排除的模式
    
    - .thumbnails/***
    - node_modules/***
    - venv/***
    
    # 包含的模式
    
    + /Documents/***
    + /Books/***
    + /Music/***
    
    # 排除其他所有内容
    - /**
    
`***` 是一种特殊的 rsync 模式，它递归地匹配文件夹及其所有内容。 

查看 [rsync(1) § PATTERN MATCHING RULES](<https://man.archlinux.org/man/rsync.1#PATTERN_MATCHING_RULES>) 和 [rsync(1) § FILTER RULES IN DEPTH](<https://man.archlinux.org/man/rsync.1#FILTER_RULES_IN_DEPTH>) 获取更多详情。 

然后用此命令运行 rsync： 
    
    $ rsync -aAXHv --filter="merge backup.filter" $SRC $DEST
    
关键字是 `--filter "merge ..."` 参数，它将获取过滤器文件并按顺序解析每个同步文件的规则。 

###  从路径列表复制

除了使用[#筛选规则的高级用法](<#%E7%AD%9B%E9%80%89%E8%A7%84%E5%88%99%E7%9A%84%E9%AB%98%E7%BA%A7%E7%94%A8%E6%B3%95>)外，还可以使用`--files-from` 选项。它可以从包含目录或文件路径列表的文本文件中获取输入，每条路径都以新行分隔。需要注意的是，如果用户想要递归复制目录，即使已经包含 `-a` 选项，也必须手动为该选项指定 `-r` 标志。 

例如，可以使用以下命令归档目录列表和所有递归目录： 
    
    $ rsync -aAXHvr --files-from="dir_list.txt" $SRC $DEST
    
##  文件系统克隆

rsync 提供了一种复制文件系统中所有数据的方法，同时保留尽可能多的信息，包括文件系统元数据。这是一个文件系统级别的数据克隆过程，其中源文件系统和目标文件系统不需要是同一类型。它可以用于备份、文件系统迁移或数据恢复。 

rsync 的 _归档_ 模式接近于适合该工作，但它不备份特殊的文件系统元数据，例如访问控制列表、扩展属性或稀疏文件财产。为了在文件系统级别成功克隆，需要提供一些其他选项： 
    
    rsync -qaHAXS SOURCE_DIR DESTINATION_DIR
    
它们的意思是（来自手册页）： 
    
    --hard-links, -H        保留硬链接
    --acls, -A              保留 ACLs（包含 --perms）
    --xattrs, -X            保留扩展属性
    --sparse, -S            将空序列转换为稀疏块
    
此外，如果要从副本中排除树下挂载的其他文件系统，请使用 `-x`。 

**注意：** 如果您正在使用 rsync 将 Arch 安装迁移到新驱动器，请记住在 `SOURCE_DIR` 末尾添加一个尾随斜杠，原因在[#注意尾随下划](<#%E6%B3%A8%E6%84%8F%E5%B0%BE%E9%9A%8F%E4%B8%8B%E5%88%92>)中提到。

可以使用 `diff` 的递归选项在文件系统级别简单地重新读取和检查生成的副本（例如，在数据恢复尝试之后）： 
    
    diff -r SOURCE_DIR DESTINATION_DIR
    
通过使用 rsync（如本文所述）和更新 [fstab](<../zh-cn/Fstab.html> "Fstab") 和[引导加载程序](<../zh-cn/Arch_%E7%9A%84%E5%90%AF%E5%8A%A8%E6%B5%81%E7%A8%8B.html#%E5%BC%95%E5%AF%BC%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F> "引导加载程序")（如[迁移到新硬件](<../zh-cn/%E8%BF%81%E7%A7%BB%E5%88%B0%E6%96%B0%E7%A1%AC%E4%BB%B6.html> "迁移到新硬件")中所述），可以成功执行文件系统迁移。这本质上提供了一种将任何根文件系统转换为另一个文件系统的方法。 

##  作为守护程序

_rsync_ 可以在侦听TCP端口 `873` 的服务器上作为[守护程序](<../zh-cn/Systemd.html> "守护程序")运行。 

编辑模板 `/etc/rsyncd.conf`，配置共享并[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `rsyncd.service`。 

**注意：** 截至 [rsync](<https://archlinux.org/packages/?name=rsync>)包 3.2.0-1，该软件包采用了上游 systemd 单元文件 `rsyncd.service` 和 `rsyncd@.service`。`ProtectHome` 的更改已被注释，`[Service]` 节下的安全功能 `ProtectSystem=full` 仍处于活动状态。这将使 `/boot/`, `/etc/` 和 `/usr/` 目录只读。如果您需要 rsyncd 写入系统目录，您可以[编辑](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%B7%BB%E5%8A%A0%E3%80%81%E5%88%9B%E5%BB%BA%E3%80%81%E7%BC%96%E8%BE%91%E6%96%87%E4%BB%B6> "Edit")该单元，并在重写代码段的 `[Service]` 节中设置 `ProtectSystem=off`。

来自客户端使用，例如列出服务器内容： 
    
    $ rsync rsync://_server/share_
    
将文件从客户端传输到服务器： 
    
    $ rsync _local-file_ rsync://_server/share/_
    
考虑在[防火墙](<../zh-cn/Category:%E9%98%B2%E7%81%AB%E5%A2%99.html> "防火墙")中打开 TCP 端口 `873`，并使用用户身份验证。 

**注意：** 包括用户身份验证在内的所有传输数据均未加密。

###  示例配置

####  从文件列表共享
    
    /etc/rsyncd.conf
    
    ...
    
    # 跨越文件系统边界时需要。
    #use chroot  = no
    read only = yes
    
    ...
    
    [sync]
        path         = /
    # 要复制的文件列表。
        include from = /backup.list
    # 排除其余部分。
        exclude      = *

在文件列表中，所有 _中间路径_ 都是必需的，除非使用 `***` 通配符： 
    
    /backup.list
    
    /etc/
    /etc/conf.d/
    /etc/conf.d/hwclock
    /etc/fonts/***
    
##  另见

  * 更多用法示例在[社区贡献](<https://bbs.archlinux.org/viewforum.php?id=27>)和 [General Programming](<https://bbs.archlinux.org/viewforum.php?id=33>) 论坛
  * [如何 – 使用带硬链接的 rsync 进行本地和远程快照备份](<https://www.pointsoftware.ch/2012/09/12/howto-local-and-remote-snapshot-backup-using-rsync-with-hard-links/>)包括带硬链接的文件重复数据消除、MD5 完整性签名、'chattr' 保护、过滤规则、磁盘配额、指数分布的保留策略（备份循环，同时保存比旧备份更新的备份）
  * [与 SSH 密钥/身份文件一同使用 rsync](<https://stackoverflow.com/questions/5527068/how-do-you-use-an-identity-file-with-rsync>)
