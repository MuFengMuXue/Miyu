**翻译状态：**

  * 本文（或部分内容）译自 [Snapper](<https://wiki.archlinux.org/title/Snapper> "arch:Snapper")，最近一次同步于 2025-02-08，若英文版本有所[更改](<https://wiki.archlinux.org/title/Snapper?diff=0&oldid=825270>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Snapper_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [Btrfs](<../zh-cn/Btrfs.html> "Btrfs")
  * [mkinitcpio-btrfs](</wzh/index.php?title=Mkinitcpio-btrfs&action=edit&redlink=1> "Mkinitcpio-btrfs（页面不存在）")

[Snapper](<http://snapper.io>) 是一个由 openSUSE 的 Arvin Schnell 开发的工具，用于管理 [Btrfs](<../zh-cn/Btrfs.html> "Btrfs") 子卷和 [LVM](<../zh-cn/LVM.html> "LVM") 精简配置(thin-provisioned)卷。它可以创建和比较快照，在快照间回滚，并支持自动按时间序列创建快照。 

##  安装

[安装](<../zh-cn/Pacman.html> "Pacman") [snapper](<https://archlinux.org/packages/?name=snapper>)包 包。或者安装开发版本 [snapper-git](<https://aur.archlinux.org/packages/snapper-git/>)AUR。 

此外，还可以安装 GUI 前端 [snapper-gui-git](<https://aur.archlinux.org/packages/snapper-gui-git/>)AUR、[btrfs-assistant](<https://archlinux.org/packages/?name=btrfs-assistant>)包 或 [snapper-tools](<https://aur.archlinux.org/packages/snapper-tools/>)AUR。 

##  建立一个新的配置

在为 btrfs 子卷建立一个 snapper 配置前，这个子卷必须已经存在。否则，你应该在建立 snapper 配置前[创建](<../zh-cn/Btrfs.html#%E5%88%9B%E5%BB%BA%E5%AD%90%E5%8D%B7> "Btrfs")它。 

要为位置为 `_/path/to/subvolume_` 的 btrfs 子卷创建一个新的 snapper 配置文件，并命名为 `_config_`： 
    
    # snapper -c _config_ create-config _/path/to/subvolume_
    
这将会： 

  * 根据 `/usr/share/snapper/config-templates/default` 处的默认配置模板创建一个配置文件 `/etc/snapper/configs/_config_`。
  * 在 `_/path/to/subvolume_ /.snapshots` 处创建一个子卷，用于存储未来该配置文件产生的子卷。子卷的路径将会是 `_/path/to/subvolume_ /.snapshots/_#_ /snapshot`，` _#_` 是子卷序号。
  * 将 `_config_` 加入到 `/etc/conf.d/snapper` 的 `SNAPPER_CONFIGS` 中。

例如，要为挂载在 `/` 的子卷创建一个配置文件： 
    
    # snapper -c root create-config /
    
**注意：** 如果你正在使用 [archinstall](<../zh-cn/Archinstall.html> "Archinstall") 推荐的 [btrfs](<../zh-cn/Btrfs.html> "Btrfs") 分区布局，则 `@.snapshots` 子卷已经被挂载到 `/.snapshots`，这会导致 `snapper create-config` 无法正常创建配置 [[1]](<https://github.com/archlinux/archinstall/issues/1808>)。要让 Snapper 使用 `@.snapshots` 来创建备份，需要进行如下操作： 

  * 卸载 `@.snapshots` 子卷并删除已存在的挂载点。

  * 创建 Snapper 配置。

  * 删除 Snapper 创建的子卷。

  * 重新创建 `/.snapshots` 挂载点，重新挂载 `@.snapshots` 子卷。

此时，配置文件已经激活。如果你的 [cron](<../zh-cn/Cron.html> "Cron") 守护进程已经运行， snapper 将会使用 [#自动按时创建快照](<#%E8%87%AA%E5%8A%A8%E6%8C%89%E6%97%B6%E5%88%9B%E5%BB%BA%E5%BF%AB%E7%85%A7>)。否则，你需要使用 systemd 单元文件和定时器。参阅 [#启用/停用](<#%E5%90%AF%E7%94%A8/%E5%81%9C%E7%94%A8>)。 

参阅 [snapper-configs(5)](<https://man.archlinux.org/man/snapper-configs.5>)。 

##  创建快照

###  自动按时创建快照

一个快照时间线(timeline)由可配置数目的每小时/日/月/年快照组成。当自动按时创建启用时，默认每小时创建一个快照。每天由时间线清理算法清理多余快照。详情请参照 [snapper-configs(5)](<https://man.archlinux.org/man/snapper-configs.5>) 中的 `TIMELINE_*` 变量。 

####  启用/停用

如果你拥有一个 [cron](<../zh-cn/Cron.html> "Cron") 守护进程，该特性应该已经自动启用。要停用，编辑你想禁用该特性的子卷对应配置文件为： 
    
    TIMELINE_CREATE="no"

如果你没有 [cron](<../zh-cn/Cron.html> "Cron") 守护进程，你可以使用提供的 systemd 单元文件。[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动")并[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `snapper-timeline.timer` 来启用自动按时创建快照。另外，[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用")并[启动](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启动") `snapper-cleanup.timer` 来定期清理老旧快照。 

**注意：** 如果你有一个 cron 守护进程并同时启用了 systemd 单元，这可能会导致重复创建快照。如果你希望使用 systemd 单元并禁用 cron 集成，一中可行的方法是使用 pacman 的 [NoExtract](<../zh-cn/Pacman.html#%E5%9C%A8%E5%AE%89%E8%A3%85%E6%97%B6%E8%B7%B3%E8%BF%87%E6%96%87%E4%BB%B6> "NoExtract") 配置选项。参见[[2]](<https://unix.stackexchange.com/questions/425570/snapper-has-recently-started-performing-duplicate-snapshots-each-hour>)。

####  设置快照限制

默认配置将保留 10 个每小时快照，10 个每日快照，10 个每月快照和 10 个每年快照。你可以在配置文件中更改这些限制，特别是在繁忙的子卷，例如 `/` 上。参阅 [#避免影响性能](<#%E9%81%BF%E5%85%8D%E5%BD%B1%E5%93%8D%E6%80%A7%E8%83%BD>)。 

这是一份名为 `_config_` 的配置文件的示例片段，它将保留 5 个每小时快照，7 个每日快照，不保留每月和每年快照： 
    
    /etc/snapper/configs/_config_
    
    TIMELINE_MIN_AGE="1800"
    TIMELINE_LIMIT_HOURLY="5"
    TIMELINE_LIMIT_DAILY="7"
    TIMELINE_LIMIT_WEEKLY="0"
    TIMELINE_LIMIT_MONTHLY="0"
    TIMELINE_LIMIT_YEARLY="0"

####  更改创建和清理频率

如果你使用提供的 systemd 定时器，你可以[修改](<../zh-cn/Systemd.html#%E4%BF%AE%E6%94%B9%E7%8E%B0%E5%AD%98%E5%8D%95%E5%85%83%E6%96%87%E4%BB%B6> "Systemd")它们来更改创建和清理频率。 

例如，编辑 `snapper-timeline.timer`，加入下列配置来设定快照频率为间隔五分钟，而不是一小时： 
    
    [Timer]
    OnCalendar=
    OnCalendar=*:0/5
    
在编辑 `snapper-cleanup.timer` 来每小时运行清理，而不是每天的时候, 你需要更改 `OnUnitActiveSec`。 加入: 
    
    [Timer]
    OnUnitActiveSec=1h
    
参阅 [Systemd/定时器](<../zh-cn/Systemd/%E5%AE%9A%E6%97%B6%E5%99%A8.html> "Systemd/定时器")和 [Systemd#附加配置片段](<../zh-cn/Systemd.html#%E9%99%84%E5%8A%A0%E9%85%8D%E7%BD%AE%E7%89%87%E6%AE%B5> "Systemd")。 

###  手动创建快照

####  Single 快照

默认情况下 snapper 创建 _single_ 类型的快照，它们与其他快照没有特别关系。 

要为一个子卷创建快照： 
    
     # snapper -c _config_ create --description _desc_
    
以上命令没有对应的清理算法，因此该快照将会一直存储直到[删除](<#%E5%88%A0%E9%99%A4%E5%BF%AB%E7%85%A7>)它。 

要设置一个清理算法，在 `create` 后使用 `-c` 选项，并在 `number`，`timeline`，`pre` 或 `post` 中选择一个参数。 `number` 使 snapper 定期清理超出配置文件中设置的数量限制的快照。例如，要创建一个使用 `number` 清理算法的快照： 
    
     # snapper -c _config_ create -c number
    
参阅 [#自动按时创建快照](<#%E8%87%AA%E5%8A%A8%E6%8C%89%E6%97%B6%E5%88%9B%E5%BB%BA%E5%BF%AB%E7%85%A7>)查看 `timeline` 是如何工作的。参阅 [#pre/post 快照](<#pre/post_%E5%BF%AB%E7%85%A7>)查看 `pre` `post` 如何工作。 

####  pre/post 快照

另一种快照类型是 _pre/post_ 快照。两个快照会在进行重大更改时先后成对创建（例如进行系统更新时）。 

如果这种重大更改是/可被单个命令调用，那么 `snapper create --command` 可以在调用这个命令的同时创建 pre/post 快照。 

    # snapper -c _config_ create --command _cmd_
    
**提示：** 要在创建 _pre/post_ 快照时执行任何 shell 命令，可以考虑使用 [snp](<https://aur.archlinux.org/packages/snp/>)AUR 脚本。这个脚本相比 Snapper 自身的 `--command` 选项能更好的处理输出重定向。

_pre/post_ 快照也可以被手动创建。 

首先创建一个 _pre_ 快照： 
    
    # snapper -c _config_ create -t pre -p
    
记下被创建快照的序号（在创建 _post_ 快照时需要用到）。 

然后进行想要进行的操作（比如安装一个程序，或是进行升级等）。 

最后创建 _post_ 快照，将下文的 `_N_` 替换为 _pre_ 快照的序号： 
    
    # snapper -c _config_ create -t post --pre-number _N_
    
参阅 [#在进行 pacman 操作时创建快照](<#%E5%9C%A8%E8%BF%9B%E8%A1%8C_pacman_%E6%93%8D%E4%BD%9C%E6%97%B6%E5%88%9B%E5%BB%BA%E5%BF%AB%E7%85%A7>)。 

###  启动时快照

要让 snapper 为 `root` 配置文件创建一个快照，[启用](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E6%8E%A7%E5%88%B6_systemd_%E5%8D%95%E5%85%83> "启用") `snapper-boot.timer`。通过这种方式创建的快照是 _Single_ 快照。 

##  管理快照

###  列出配置

列出所有你已经创建的配置: 
    
     # snapper list-configs
    
###  列出快照

要列出名为 _config_ 的配置文件对应的快照: 
    
     # snapper -c _config_ list
    
###  还原快照

在还原快照时，部分文件可能会保持原样，原因可能是快照中不包含该文件（例如，该文件位于另一个子卷上），也可能是过滤配置排除了该文件。 

####  过滤配置

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** `/etc/mtab` is a symlink to `/proc/self/mounts`, so reverting it has no effect on the system.（在 [Talk:Snapper](<../zh-cn/Talk:Snapper.html>) 中讨论）

部分文件保存着系统的状态信息，例如 `/etc/mtab`。这些文件不应该被还原。Arch Linux 提供的 Snapper 的默认配置已经排除了这些文件。Snapper 支持按照用户排除某些文件或文件夹。`/etc/snapper/filters/*.txt` 和 `/usr/share/snapper/filters/*.txt` 中的每行指定了要排除的项目。当 Snapper 计算快照之间的差别时，会排除这些文件。注意，这些文件仍会包含在快照中，如果不想让这些文件包含在快照中，使用单独的子卷或者挂载点。 

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** How is the list from SLES documentation relevant for Arch Linux?（在 [Talk:Snapper](<../zh-cn/Talk:Snapper.html>) 中讨论）

参见 SUSE 的文档[Directories That Are Excluded from Snapshots](<https://documentation.suse.com/sles/12-SP4/html/SLES-all/cha-snapper.html#snapper-dir-excludes>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2024-03-03 ⓘ]。 

####  还原快照

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** What is the "default layout"? What is the alternative?（在 [Talk:Snapper](<../zh-cn/Talk:Snapper.html>) 中讨论）

如果你使用 Snapper 的默认布局，每个快照是在所指定子卷下的 `.snapshots` 目录的下层子卷，例如 `@home` 的快照位于 `@home/.snapshots`下。 

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** Subvolumes that are not used for `/` can be restored from the system itself. Just log in as root, make sure that the subvolume is not used, and unmount it.（在 [Talk:Snapper](<../zh-cn/Talk:Snapper.html>) 中讨论）

例如要将某个快照恢复到 `home`，首先启动到 Arch Linux 的 LiveCD。 使用[UUID](<../zh-cn/%E5%9D%97%E8%AE%BE%E5%A4%87%E6%8C%81%E4%B9%85%E5%8C%96%E5%91%BD%E5%90%8D.html#%E9%80%9A%E8%BF%87_uuid> "UUID")将 btrfs 的顶层子卷挂载到`/mnt`。 
    
    # mount -t btrfs -o subvol=/ /dev/disk/by-uuid/_UUID_of_root_volume_ /mnt
    # cd /mnt
    
将目前的子卷移动到其他地方，例如将 `@home` 移动到`@home-backup`： 
    
    # mv @home @home-backup
    
找到你想恢复快照的序号（每个快照都单独显示为一行，所以能很方便的按照时间查找序号）： 
    
    # grep -r '<date>'  /mnt/@home-backup/.snapshots/*/info.xml
    
    ...
    /mnt/@home-backup/.snapshots/_number_ /info.xml:  <date>2021-07-26 22:00:00</date>
    ...
    
**注意：** 在`info.xml`记录的时间为 [UTC](<https://en.wikipedia.org/wiki/UTC> "wikipedia:UTC") 时间，请务必将其和本地时间的时差计算在内。

记住 `_number_`。 

使用 `_number_` 快照来创建新快照。 
    
    # btrfs subvolume snapshot @home-backup/.snapshots/_number_ /snapshot @home
    
将 `.snapshots` 移回恢复完成的子卷下，例如`@home`。 

    # mv @home-backup/.snapshots @home/
    
**注意：** 如果在 [fstab](<../zh-cn/Fstab.html> "Fstab")中指定的是 `subvolid` 而不是子卷路径，则需要更改 `/mnt/@/etc/fstab` 中的 `subvolid`（假定把@子卷挂载到了`/`）。 可以使用 `btrfs subvolume list /mnt | grep @home$` 来查询新的 `subvolid`。

重新启动计算机。 

检查计算机运行是否正常。这时可以删除在还原之前创建的快照了——例如`@home-backup`。在删除前记得检查是否有需要保留的数据。 

###  删除快照

要删除序号为 `_N_` 的快照: 
    
     # snapper -c _config_ delete _N_
    
可以一次删除多个快照。例如，要删除 root 配置文件的 65 和 70 号快照： 
    
     # snapper -c root delete 65 70
    
要同时删除多个连续的快照，例如删除 65 到 70 号所有快照： 
    
    # snapper -c root delete 65-70
    
要立即释放快照占用的磁盘空间，使用 `--sync` 选项： 
    
    # snapper -c root delete --sync 65
    
要删除一个 Snapper 配置和其所有快照，包括 `.snapshots` 子卷： 
    
    # snapper -c _config_ delete-config 
    
**注意：** 删除 pre 快照时, 你应该总是删除对应的 post 快照。反之亦然。

###  允许非 root 用户访问

所有配置文件都是由 root 用户创建的，默认情况下，也只有 root 用户可以查看并访问它们。 

要让指定用户可以列出某一配置文件的快照，修改 `/etc/snapper/configs/_config_` 中的 `ALLOW_USERS` 项。现在你应该可以以普通用户权限运行 `snapper -c _config_ list`

最后，如果你想允许某一用户浏览 `.snapshots` 目录，但是该目录的拥有者必须为 root。因此，你应该修改包括该用户的组为组拥有者，以 `users` 为例： 
    
    # chmod a+rx .snapshots
    # chown :users .snapshots
    
##  提示与技巧

###  在进行 pacman 操作时创建快照

下列软件包可以依据 pacman 进行的事务自动创建快照。 

  * **snap-pac** — 使用 [pacman 钩子](<../zh-cn/Pacman.html#%E9%92%A9%E5%AD%90> "Pacman")使 pacman 自动使用 Snapper 创建[#pre/post 快照](<#pre/post_%E5%BF%AB%E7%85%A7>)。类似与 openSUSE 的 YaST 的行为。

     <https://github.com/wesbarnett/snap-pac> || [snap-pac](<https://archlinux.org/packages/?name=snap-pac>)包

  * **grub-btrfs** — 包含了一个名为 _grub-btrfsd_ 的 systemd 单元。可自动查找快照并将其添加到 [GRUB](<../zh-cn/GRUB.html> "GRUB") 菜单中。

     <https://github.com/Antynea/grub-btrfs> || [grub-btrfs](<https://archlinux.org/packages/?name=grub-btrfs>)包

  * **snap-pac-grub** — 在 [snap-pac](<https://archlinux.org/packages/?name=snap-pac>)包 创建快照后自动使用 [grub-btrfs](<https://archlinux.org/packages/?name=grub-btrfs>)包 更新 [GRUB](<../zh-cn/GRUB.html> "GRUB") 启动项。同样使用[pacman 钩子](<../zh-cn/Pacman.html#%E9%92%A9%E5%AD%90> "Pacman")。

     <https://github.com/maximbaz/snap-pac-grub> || [snap-pac-grub](<https://aur.archlinux.org/packages/snap-pac-grub/>)AUR

  * **refind-btrfs** — 在 [snap-pac](<https://archlinux.org/packages/?name=snap-pac>)包 创建快照后自动在 [rEFInd](<../zh-cn/REFInd.html> "REFInd") 中创建启动项。

     <https://github.com/Venom1991/refind-btrfs> || [refind-btrfs](<https://aur.archlinux.org/packages/refind-btrfs/>)AUR

  * **snp** — 包装任何 shell 命令以供创建 pre/post 快照（例如`snp pacman -Syu`）相比 Snapper 自身的 `--command` 选项能更好的处理输出重定向（参见 [#pre/post 快照](<#pre/post_%E5%BF%AB%E7%85%A7>)）。

     <https://gist.github.com/erikw/5229436> || [snp](<https://aur.archlinux.org/packages/snp/>)AUR

  * **limine-snapper-sync** — 在 [snap-pac](<https://archlinux.org/packages/?name=snap-pac>)包 创建快照后自动在 [Limine](</wzh/index.php?title=Limine&action=edit&redlink=1> "Limine（页面不存在）") 中创建启动项。（参见[Limine#Snapper snapshot integration for Btrfs](</wzh/index.php?title=Limine&action=edit&redlink=1> "Limine（页面不存在）")）

     <https://gitlab.com/Zesko/limine-snapper-sync> || [limine-snapper-sync](<https://aur.archlinux.org/packages/limine-snapper-sync/>)AUR

####  启动到只读快照中

使用 [grub-btrfs](<https://archlinux.org/packages/?name=grub-btrfs>)包、[snap-pac-grub](<https://aur.archlinux.org/packages/snap-pac-grub/>)AUR或[limine-snapper-sync](<https://aur.archlinux.org/packages/limine-snapper-sync/>)AUR的用户应该注意：在默认状态下，Snapper 创建的快照是只读的。而在启动到只读快照时会有一些困难。许多服务，例如显示管理器，都需要一个可写的 `/var` 目录。在启动到只读快照时，这些服务将无法正常工作。 

为了避免这个问题，可以使快照设为可写，或者使用 overlayfs 启动到快照中，这也是开发者认可的方法。这种情况下快照像是一个 Live CD 环境。 

**注意：** 任何对快照中文件的更改都不会被保存，因为文件系统只是存在于内存上。

要使用 overlayfs 启动快照： 

  * 确保 [grub-btrfs](<https://archlinux.org/packages/?name=grub-btrfs>)包 已经安装。
  * 添加 `grub-btrfs-overlayfs` 到 `/etc/mkinitcpio.conf` `HOOKS` 的末尾。例如：
        
        HOOKS=(base udev autodetect microcode modconf kms keyboard keymap consolefont block filesystems fsck grub-btrfs-overlayfs)

**注意：** 因为 _grub-btrfs-overlayfs_ 只提供了 [运行时钩子](<../zh-cn/Mkinitcpio.html#%E8%BF%90%E8%A1%8C%E6%97%B6%E9%92%A9%E5%AD%90> "Mkinitcpio")，没有提供 systemd 单元，所以并**不** 支持基于 systemd 的 initramfs。确保你使用的是 [基于 Busybox 的 initramfs](<../zh-cn/Mkinitcpio.html#%E5%B8%B8%E7%94%A8%E9%92%A9%E5%AD%90> "Mkinitcpio")。参见[GitHub issue](<https://github.com/Antynea/grub-btrfs/issues/199>)。

  * [重新生成 initramfs](<../zh-cn/%E9%87%8D%E6%96%B0%E7%94%9F%E6%88%90_initramfs.html> "重新生成 initramfs")。

进一步了解： 

  * [grub-btrfs README](<https://github.com/Antynea/grub-btrfs/blob/master/initramfs/readme.md>) （包含了使用 [dracut](<https://archlinux.org/packages/?name=dracut>)包 而不是 [mkinitcpio](<https://archlinux.org/packages/?name=mkinitcpio>)包 的配置方法）
  * [Github 上的讨论](<https://github.com/Antynea/grub-btrfs/issues/92>)

**提示：** 你可以使用 [Limine](</wzh/index.php?title=Limine&action=edit&redlink=1> "Limine（页面不存在）") 启动到快照中。Limine 和 Snaper 间的集成由 [limine-snapper-sync](<https://aur.archlinux.org/packages/limine-snapper-sync/>)AUR 提供。参见[Limine#Snapper snapshot integration for Btrfs](</wzh/index.php?title=Limine&action=edit&redlink=1> "Limine（页面不存在）")。

####  在进行 pacman 事务时备份非 btrfs /boot 分区

如果你的 `/boot` 分区是在一个非 btrfs 文件系统上（例如一个 [ESP](<../zh-cn/EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA.html> "ESP") 分区），Snapper 无法备份这些分区。 在[系统备份#快照与_/boot_分区](<../zh-cn/%E7%B3%BB%E7%BB%9F%E5%A4%87%E4%BB%BD.html#%E5%BF%AB%E7%85%A7%E4%B8%8E_/boot_%E5%88%86%E5%8C%BA> "系统备份")中提供了一个自动在内核更新时将 `/boot`复制到你的 btrfs 根目录下的方法。这种方法也能和 [snap-pac](<https://archlinux.org/packages/?name=snap-pac>)包 一起使用。 

###  增量备份到外部驱动器

一些工具可以使用 Snapper 进行自动备份。参见 [Btrfs#增量备份到外置设备](<../zh-cn/Btrfs.html#%E5%A2%9E%E9%87%8F%E5%A4%87%E4%BB%BD%E5%88%B0%E5%A4%96%E7%BD%AE%E8%AE%BE%E5%A4%87> "Btrfs")。 

###  建议的文件系统布局

**注意：** 下列布局**不** 是为了与 `snapper rollback` 搭配使用。而是为了缓解[#Restoring / to its previous snapshot](<#Restoring_/_to_its_previous_snapshot>) 中的某些问题。参见 [论坛帖子](<https://bbs.archlinux.org/viewtopic.php?id=194491>)。

这是一种建议的文件系统布局，可以方便的将挂载到 `/` 的 `@` 子卷还原到之前的状态： 

文件系统布局  子卷 | 挂载点   
---|---  
@ | /   
@home | /home   
@snapshots | /.snapshots   
@var_log | /var/log   
      
    subvolid=5
      |
      ├── @ -|
      |     contained directories:
      |       ├── /usr
      |       ├── /bin
      |       ├── /.snapshots
      |       ├── ...
      |
      ├── @home
      ├── @snapshots
      ├── @var_log
      └── @...
    
子卷`@...`应当挂载到任何应有自己子卷的目录。 

**注意：**

  * 当对 `@` 子卷（挂载到`/`）创建快照时，其余子卷的将不会被包含在快照中。即使这些子卷位于 `@` 之下（子卷不是递归包含的）。如果需要为其他子卷创建快照，需要单独为这些子卷创建 Snapper 配置。
  * 由于[Btrfs 的限制](<../zh-cn/Btrfs.html#%E4%BA%A4%E6%8D%A2%E6%96%87%E4%BB%B6> "Btrfs")，需要创建快照的子卷中不能包含[swap 文件](<../zh-cn/Swap.html#%E4%BA%A4%E6%8D%A2%E6%96%87%E4%BB%B6> "Swap")。将 swap 文件放到另外的子卷或者使用 [swap 分区](<../zh-cn/Swap.html#%E4%BA%A4%E6%8D%A2%E5%88%86%E5%8C%BA> "Swap")。

如果你想将`@`子卷恢复到之前的状态，其他的子卷将不会被影响。例如，当你在将`@`恢复到之前的快照时，`/home`将不会受到影响，因为`/home`挂载到了单独的子卷下。 

这个布局能使 Snapper 定期为 `/`创建快照，并能让在出现启动问题时更容易还原快照。 

在这种情况下，进行初始设置之后，Snapper不需要更多配置。 

**提示：**

  * 考虑为其他不想包含在`@`快照中的目录创建子卷。例如 `/var/cache`, `/var/spool`, `/var/tmp`, `/var/lib/machines` ([systemd-nspawn](<../zh-cn/Systemd-nspawn.html> "Systemd-nspawn")), `/var/lib/docker` ([Docker](<../zh-cn/Docker.html> "Docker")), `/var/lib/postgres` ([PostgreSQL](<../zh-cn/PostgreSQL.html> "PostgreSQL"))，或是其他 `/var/lib/` 下的目录。你可以使用类似上面的平行子卷结构，或是创建下层子卷。但是，pacman 数据库 `/var/lib/pacman` 必须位于挂载到`/`的子卷下。
  * 你可以为`@home`或是其他子卷单独创建快照或者还原快照。

####  配置 Snapper 和挂载点

假定`@`挂载到了`/`下，同时 `/.snapshots` 未被挂载，同时也不存在同名目录。可以使用如下命令确认： 
    
    # umount /.snapshots
    # rm -r /.snapshots
    
接下来为`/`[#建立一个新的配置](<#%E5%BB%BA%E7%AB%8B%E4%B8%80%E4%B8%AA%E6%96%B0%E7%9A%84%E9%85%8D%E7%BD%AE>)。Snapper 会自动在`@`下创建 `.snapshots` 子卷。这在建议的布局下是不必要的，可以删除。 
    
    # btrfs subvolume delete /.snapshots
    
删除这个子卷之后，重新创建 `/.snapshots` 目录。 
    
    # mkdir /.snapshots
    
现在将 `@snapshots` 子卷[挂载](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html#%E6%8C%82%E8%BD%BD%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "挂载")到 `/.snapshots` 目录。例如，当文件系统位于 `/dev/sda1` 时： 
    
    # mount -o subvol=@snapshots /dev/sda1 /.snapshots
    
要使此配置永久生效，在 [fstab](<../zh-cn/Fstab.html> "Fstab") 中添加条目。 

若 fstab 中已存在这个条目，重新挂载： 
    
    # mount -a
    
将此文件夹[权限](<../zh-cn/%E6%96%87%E4%BB%B6%E6%9D%83%E9%99%90%E4%B8%8E%E5%B1%9E%E6%80%A7.html#%E6%95%B0%E5%AD%97%E5%BD%A2%E5%BC%8F> "文件权限与属性")设为 `750` 。 

这将使 Snapper 创建的快照储存在 `@` 之外。所以 `@` 被还原或替换时也不会丢失快照。 

####  还原到之前的快照

要将 `/` 还原到某个快照的状态，首先启动到 Arch Linux Live CD。 

[挂载](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html#%E6%8C%82%E8%BD%BD%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "挂载")顶层子卷（subvolid=5）。也就是说，不使用任何 `subvolid` 或 `subvol` 挂载参数。 

找到想还原快照的序号： 

    # grep -r '<date>' /mnt/@snapshots/*/info.xml
    
输出类似这样。每个快照都单独显示为一行，所以能很方便的按照时间查找序号。 
    
    /mnt/@snapshots/_number_ /info.xml:  <date>2021-07-26 22:00:00</date>
    
**注意：** 在`info.xml`记录的时间为 [UTC](<https://en.wikipedia.org/wiki/UTC> "wikipedia:UTC") 时间，请务必将其和本地时间的时差计算在内。

记住` _number_`。 

将`@`移动到其他位置，例如 `/@.broken`来备份当前的系统状态。或是直接删除`@`子卷：`btrfs subvolume delete /mnt/@`。 

为 Snapper 创建的快照创建一个可读写快照： 
    
    # btrfs subvolume snapshot /mnt/@snapshots/_number_ /snapshot /mnt/@
    
将 `_number_` 替换为你想还原的快照序号。 

**注意：** 如果在 [fstab](<../zh-cn/Fstab.html> "Fstab")中指定的是 `subvolid` 而不是子卷路径，则需要更改 `/mnt/@/etc/fstab` 中的 `subvolid`（假定把@子卷挂载到了`/`）。 可以使用 `btrfs subvolume list /mnt | grep @$` 来查询新的 `subvolid`。另外若在启动加载器中使用了 `subvolid`，也需要一并更改。例如 `refind_linux.conf`。

最后，卸载顶层子卷（subvolid=5），[挂载](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html#%E6%8C%82%E8%BD%BD%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "挂载")`@`到`/mnt`以及 [ESP](<../zh-cn/EFI_%E7%B3%BB%E7%BB%9F%E5%88%86%E5%8C%BA.html> "ESP")分区。[chroot](<../zh-cn/Chroot.html> "Chroot")到完成还原的根目录下，并[重新生成 initramfs](<../zh-cn/%E9%87%8D%E6%96%B0%E7%94%9F%E6%88%90_initramfs.html> "重新生成 initramfs")。 

现在`/`已经恢复到了之前快照的状态。重新启动计算机。 

**提示：** 你也可以使用为这种布局设计的自动回滚工具：[snapper-rollback](<https://aur.archlinux.org/packages/snapper-rollback/>)AUR。编辑 `/etc/snapper-rollback.conf` 来匹配系统的实际布局情况。

####  还原其他子卷到之前的状态

参见[#还原快照](<#%E8%BF%98%E5%8E%9F%E5%BF%AB%E7%85%A7>)。 

###  从快照中删除文件

若你想删除指定的文件或文件夹而不想删除整个快照，可以使用 [snappers](<https://aur.archlinux.org/packages/snappers/>)AUR 实现。这个脚本还可用于以 Snapper 目前不支持的其他方式操作过去的快照。 

若你不想使用其他脚本，你可以使[快照变为可读写](<https://unix.stackexchange.com/a/149933>)： 
    
    # btrfs property set /path/to/.snapshots/<snapshot_num>/snapshot ro false
    
验证 `ro=false`： 
    
    # btrfs property get /path/to/.snapshots/<snapshot_num>/snapshot
    ro=false
    
现在可以像平常一样修改 `/path/to/.snapshots/<snapshot_num>/snapshot` 了。你也可以使用 shell 循环批量处理快照。 

###  避免影响性能

在`/`这种繁忙的文件系统中，长时间保留大量快照会占用大量硬盘空间，可能影响文件系统的性能。你可以通过以下方式降低影响： 

  * 为不值得被快照的目录[创建](<../zh-cn/Btrfs.html#Creating_a_subvolume> "Btrfs")单独的子卷，例如`/var/cache/pacman/pkg`，`/var/abs`，`/var/tmp`，`/srv`。
  * 编辑默认创建快照的频率，参见[#自动按时创建快照](<#%E8%87%AA%E5%8A%A8%E6%8C%89%E6%97%B6%E5%88%9B%E5%BB%BA%E5%BF%AB%E7%85%A7>)。

#### updatedb

默认情况下，`updatedb`（参见 [locate](<../zh-cn/Locate.html> "Locate")）也会索引由 snapper 创建的 `.snapshots` 目录，如果快照较多，这可能会导致运行速度严重的性能影响和大量内存占用。你可以编辑`updatedb`，阻止`.snapshots`索引该目录： 
    
    /etc/updatedb.conf
    
    PRUNENAMES = ".snapshots"

####  禁用配额

Btrfs 的配额功能（不是后来引入的“简单配额”（simple quota））可能会导致删除快照时占用大量 CPU 来维护配额信息。 

要确定配额是否已启用，使用如下命令： 
    
    # btrfs qgroup show /
    
可以使用如下命令禁用配额： 
    
    # btrfs quota disable /
    
####  计算快照数量

如果禁用配额没有减缓性能问题，那么计算快照数量可能会有用： 
    
    # btrfs subvolume list -s / | wc -l
    
###  为用户数据和日志创建子卷

如果目录中包含用户数据（如电子邮件或日志），建议将其存储在自己的子卷而不是根子卷 `/` 中。这样，如果恢复 `/` 的快照，用户数据和日志不会受到影响。可以为用户数据使用单独的 timeline。不建议为 `/var/log` 创建日志快照。这可能会导致难以排除故障。 

还可以使用[#过滤配置](<#%E8%BF%87%E6%BB%A4%E9%85%8D%E7%BD%AE>)在还原过程中跳过某些目录。有关跳过某些目录的示例和原因，请参阅 [SLES 文档](<https://documentation.suse.com/sles/12-SP5/html/SLES-all/cha-snapper.html#snapper-dir-excludes>)。 

###  依据磁盘使用量清理快照

[![](../File:Tango-view-fullscreen.png)](<../File:Tango-view-fullscreen.png>)**这篇文章的某些内容需要扩充。**

**原因：** See [[3]](<http://snapper.io/2016/05/18/space-aware-cleanup.html>) for ideas. (在 [Talk:Snapper](<../zh-cn/Talk:Snapper.html>) 中讨论)

##  疑难解答

###  日志

Snapper 将所有活动写入到 `/var/log/snapper.log` 中——在你认为出错时，首先检查该文件。 

当你遇到关于每小时/每日/每周快照的问题时，最常见的原因是由于 cronie 服务（或者你使用的其他 cron 守护进程）没有运行。 

###  IO 错误

如果你在试图创建快照时遇到 'IO Error'，请确认你试图创建快照的子卷对应的 [.snapshots](<https://bbs.archlinux.org/viewtopic.php?id=164404>) 目录是一个子卷。 

另一个可能的原因是 .snapshots 目录的拥有者不是 root。你会在在 `/var/log/snapper.log` 中找到 `Btrfs.cc(openInfosDir):219 - .snapshots must have owner root`。 

###  未被管理的快照导致空间浪费

快照有可能“丢失”，它们仍然存在于磁盘上，但不会被 snapper 管理。这会造成大量磁盘空间浪费。要检查这种情况，请比较： 
    
    # snapper -c <config> list
    
与 
    
    # btrfs subvolume list -o <parent subvolume>/.snapshots 
    
第二个命令列出的子卷但未出现在第一个命令的输出中的都是未被 snapper 管理的快照。可以手动[删除](<../zh-cn/Btrfs.html#%E5%88%A0%E9%99%A4%E5%AD%90%E5%8D%B7> "Btrfs")。 

##  相关资源

  * [Snapper homepage](<http://snapper.io/>)
  * [openSUSE Snapper portal](<https://en.opensuse.org/Portal:Snapper>)
  * [Btrfs homepage](<https://btrfs.wiki.kernel.org/index.php/Main_Page>)
  * [Linux.com: Snapper: SUSE's Ultimate Btrfs Snapshot Manager](<https://www.linux.com/news/snapper-suses-ultimate-btrfs-snapshot-manager/>)
