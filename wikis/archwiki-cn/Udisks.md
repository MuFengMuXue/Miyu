**翻译状态：**

  * 本文（或部分内容）译自 [Udisks](<https://wiki.archlinux.org/title/Udisks> "arch:Udisks")，最近一次同步于 2023-01-01，若英文版本有所[更改](<https://wiki.archlinux.org/title/Udisks?diff=0&oldid=765525>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Udisks_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [udev](<../zh-cn/Udev.html> "Udev")
  * [Mount](<../zh-cn/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F.html#%E6%8C%82%E8%BD%BD%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F> "Mount")
  * [Polkit](<../zh-cn/Polkit.html> "Polkit")
  * [File manager functionality](<../zh-cn/File_manager_functionality.html> "File manager functionality")

[udisks](<https://www.freedesktop.org/wiki/Software/udisks/>) 提供了 _udisksd_ 守护进程，它实现了用于查询和管理存储设备的 D-Bus 接口；还提供了一个命令行工具 _udisksctl_ ，用于查询和使用该守护进程。 

##  安装

有两个版本的 _udisks_ ，分别称为 [udisks](<https://aur.archlinux.org/packages/udisks/>)AUR 和 [udisks2](<https://archlinux.org/packages/?name=udisks2>)包。为了集中精力开发 _udisks2_ ， _udisks_ 的开发已终止 。[[1]](<https://davidz25.blogspot.be/2012/03/simpler-faster-better.html>)

(_udisks2_ 的) [udisksd(8)](<https://man.archlinux.org/man/udisksd.8>) 和 (_udisks_ 的) `udisks-daemon` 都是由 [D-Bus](<../zh-cn/D-Bus.html> "D-Bus") 在后台启动，不应该被显式地启用。可以通过 [udisksctl(1)](<https://man.archlinux.org/man/udisksctl.1>) 和 udisks(1) 以命令行方式分别进行管控。 

##  配置

###  权限

用户通过 udisks 可执行的动作由 [Polkit](<../zh-cn/Polkit.html> "Polkit") 控制。如果[会话](</wzh/index.php?title=Session&action=edit&redlink=1> "Session（页面不存在）")不活跃或不存在，例如通过 [systemd 用户服务](<../zh-cn/Systemd/%E7%94%A8%E6%88%B7.html> "Systemd/用户")控制 udisks 时，需要手动配置 policykit. 

[这里](<https://github.com/coldfix/udiskie/wiki/Permissions>)包含 `storage` 群组的 udisk 配置，[这里](<https://gist.github.com/grawity/3886114#file-udisks2-allow-mount-internal-js>)有一个更严格的版本。 

###  默认挂载选项

It is possible to define default mount options in `/etc/udisks2/mount_options.conf`. Create the file if it doesn't already exist. The built-in defaults and some examples can be seen in `/etc/udisks2/mount_options.conf.example`.[[2]](<http://storaged.org/doc/udisks2-api/latest/mount_options.html>)

The options can target specific filesystem types. For example, mount [btrfs](<../zh-cn/Btrfs.html> "Btrfs") filesystems with zstd compression enabled: 
    
    [defaults]
    btrfs_defaults=compress=zstd
    
**注意：** Lines override the corresponding built-in defaults. Make sure not to accidentally remove mount options this way.

##  使用

要手动挂载移动设备 `/dev/sdc`: 
    
    $ udisksctl mount -b /dev/sdc1
    
卸载: 
    
    $ udisksctl unmount -b /dev/sdc1
    
参考 `udisksctl help`。 

##  提示与技巧

###  挂载助手

通过 udisk 辅助程序也可以实现挂载，请参考 [List of applications#Mount tools](<../zh-cn/List_of_applications.html#Mount_tools> "List of applications")。 

**注意：**[GNOME](<../zh-cn/GNOME.html> "GNOME") 和 [KDE](<../zh-cn/KDE.html> "KDE") 等 [桌面环境](<../zh-cn/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83.html> "桌面环境") 也提供了 udisk 辅助程序。

  * **bashmount** — A bash script to mount and manage removable media as a regular user with _udisks2_.

     <https://github.com/jamielinux/bashmount> || [bashmount](<https://aur.archlinux.org/packages/bashmount/>)AUR

  * **dolphin-plugins** — uses udisksctl to either mount or unmount the iso in [Dolphin](<../zh-cn/Dolphin.html> "Dolphin").

     <https://apps.kde.org/dolphin_plugins/> || [dolphin-plugins](<https://archlinux.org/packages/?name=dolphin-plugins>)包

  * **udiskie** — _udisks2_ automounter with optional notifications, tray icon and support for password protected [LUKS devices](<../zh-cn/Dm-crypt/Device_encryption.html> "Dm-crypt/Device encryption"). See the [udiskie wiki](<https://github.com/coldfix/udiskie/wiki/Usage>) for details

     <https://github.com/coldfix/udiskie> || [udiskie](<https://archlinux.org/packages/?name=udiskie>)包

  * **udiskie-dmenu** — dmenu interface for _udiskie_.

     <https://github.com/fogine/udiskie-dmenu> || [udiskie-dmenu-git](<https://aur.archlinux.org/packages/udiskie-dmenu-git/>)AUR

  * **udisksvm** — GUI _udisks2_ wrapper written in Python3 and using the Qt5 framework. It uses mouse clicks to mount, unmount removable devices or eject a CD/DVD. See the [README](<https://github.com/berbae/udisksvm/blob/master/README>) file for details.

     <https://github.com/berbae/udisksvm> || [udisksvm](<https://aur.archlinux.org/packages/udisksvm/>)AUR

  * **udevil** — Includes [devmon](<https://igurublog.wordpress.com/downloads/script-devmon>), which is compatible to _udisks_ and _udisks2_.

     <https://github.com/IgnorantGuru/udevil> || [udevil](<https://aur.archlinux.org/packages/udevil/>)AUR

**注意：** _devmon_ only uses _udisks_ or _udisks2_ for mounting (in this order) if _udevil_ or _pmount_ miss the SUID permission. To remove this permission, run `chmod -s /usr/bin/_udevil_` as root.

###  禁止隐藏设备（udisks2）

Udisks2 在默认情况下会隐藏一些设备，如果不希望隐藏，可以将 `/usr/lib/udev/rules.d/80-udisks2.rules` 复制到 `/etc/udev/rules.d/80-udisks2.rules` 并删除不需要隐藏的设备： 
    
    # ------------------------------------------------------------------------
    # ------------------------------------------------------------------------
    # ------------------------------------------------------------------------
    # Devices which should not be display in the user interface
    [...]
    
###  挂载到 /media

默认情况下， udisks2 在 ACL 控制下将可移动设备挂载到 `/run/media/$USER/` 目录下。如果你希望改为挂载到 `/media` 目录下，应用这条规则： 
    
    /etc/udev/rules.d/99-udisks2.rules
    
    # UDISKS_FILESYSTEM_SHARED
    # ==1: mount filesystem to a shared directory (/media/VolumeName)
    # ==0: mount filesystem to a private directory (/run/media/$USER/VolumeName)
    # See udisks(8)
    ENV{ID_FS_USAGE}=="filesystem|other|crypto", ENV{UDISKS_FILESYSTEM_SHARED}="1"
    
###  挂载 loop 设备

要挂载 ISO 镜像，使用下面命令： 
    
    $ udisksctl loop-setup -r -f _image.iso_
    
这条命令会创建 loop 设备并显示可以挂载的 ISO 镜像，卸载后，loop 设备会被 [udev](<../zh-cn/Udev.html> "Udev") 删除. 

**提示：** This mounts a read only image. To mount raw disk images, such as for [QEMU](<../zh-cn/QEMU.html> "QEMU"), remove the `-r` flag, and release the image after use with `udisksctl loop-delete -b _/dev/loop0_`. Substitute `/dev/loop0` with the name of the loop device.

###  隐藏选中的分区

如果要在桌面中隐藏某些分区或设备，可以创建类似下面的 udev 规则 `/etc/udev/rules.d/10-local.rules`: 
    
    KERNEL=="sda1", ENV{UDISKS_IGNORE}="1"
    KERNEL=="sda2", ENV{UDISKS_IGNORE}="1"
    
仅显示 `sda1` 和 `sda2` 之外的分区。 

Because block device names can change between reboots, it is also possible to use UUIDs to hide partitions or whole devices: 

For example: 
    
    # blkid /dev/sdX
    /dev/sdX: LABEL="Filesystem Label" UUID="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXXX" UUID_SUB="YYYYYYYY-YYYY-YYYY-YYYY-YYYYYYYYYYYY" TYPE="btrfs"
    
Then the following line can be used: 
    
    ENV{ID_FS_UUID}=="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXXX", ENV{UDISKS_IGNORE}="1"
    
The above line is also useful to hide multi device btrfs filesystems, as all the devices from a single btrtfs filesystem will share the same UUID across the devices but will have different SUB_UUID for each individual device. 

### Apply ATA settings

在启动和连接驱动器时，udisksd将应用存储在文件 `/etc/udisks2/_IDENTIFIER_.conf` 中的配置，其中 `_IDENTIFIER_` 是驱动器的Drive：Id属性的值。 对于支持ATA设置，有关可用选项，请参阅[udisks(8)](<https://man.archlinux.org/man/udisks.8>)。 这些设置与[hdparm](<../zh-cn/Hdparm.html> "Hdparm")的设置基本上具有相同的效果，但是只要udisks守护程序自动启动，它们就可以保留。 

例如，要将一个驱动器的standby超时设置为240(20分钟)，请添加以下内容： 
    
    /etc/udisks2/_DriveId_.conf
    
    [ATA]
    StandbyTimeout=240

要获取驱动器的DriveId，请使用`udevadm info --query=all --name=_sdx_ | grep ID_SERIAL | sed "s/_/-/g"`。 

或者，使用GUI程序来管理配置文件，例如[gnome-disk-utility](<https://archlinux.org/packages/?name=gnome-disk-utility>)包。 

### udevadm monitor

可以使用 `udevadm monitor` 监测块设备事件并在新的块设备被创建时进行挂载。无用的挂载点会被 _udisksd_ 自动删除，所以删除时不需要额外动作。 
    
    #!/bin/bash
    
    pathtoname() {
        udevadm info -p "/sys/$1" | awk -v FS== '/DEVNAME/ {print $2}'
    }
    
    while read -r _ _ event devpath _; do
            if [[ $event == add ]]; then
                devname=$(pathtoname "$devpath")
                udisksctl mount --block-device "$devname" --no-user-interaction
            fi
    done < <(stdbuf -o L udevadm monitor --udev -s block)
    
##  排错

###  隐藏设备

默认情况下，Udisks2对用户隐藏某些设备。如果这是不希望的或有其他问题，将`/usr/lib/udev/rules.d/80-udisks2.rules`复制到`/etc/udev/rules.d/80-udisks2.rules`，并删除以下内容： 
    
    # ------------------------------------------------------------------------
    # ------------------------------------------------------------------------
    # ------------------------------------------------------------------------
    # Devices which should not be display in the user interface
    [...]
    
### Broken standby timer

The udisks daemon polls [S.M.A.R.T.](</wzh/index.php?title=S.M.A.R.T.&action=edit&redlink=1> "S.M.A.R.T.（页面不存在）") data from drives regularly. Hard drives with a longer standby timeout than the polling interval may fail to enter standby. Drives that are already spun down are usually not affected. There seems no way to disable polling or change the interval as for [udisks2](<https://archlinux.org/packages/?name=udisks2>)包 by now. See [[3]](<https://bugs.launchpad.net/ubuntu/+source/udisks2/+bug/1281588>), [[4]](<https://bugs.freedesktop.org/show_bug.cgi?id=26508>). 

However, Standby timeout applied by udisks2 seems to be unaffected. To set standby timeout via udisks, see [#Apply ATA settings (udisks2)](<#Apply_ATA_settings_\(udisks2\)>). 

Other possible workarounds could be setting the timeout below the polling interval (10 minutes) or forcing a manaul spindown using `hdparm -y /dev/_sdx_`. 

###  NTFS挂载失败

如果挂载ntfs分区失败并显示以下错误： 
    
    Error mounting /dev/sdXY at [...]: wrong fs type, bad option, bad superblock on /dev/sdXY, missing codepage or helper program, or other error
    
以 root 权限执行 `journalctl`/`dmesg` 内核日志中显示下面的信息： 
    
    ntfs: (device sdXY): parse_options(): Unrecognized mount option windows_names.
    
请安装 [NTFS-3G](<../zh-cn/NTFS-3G.html> "NTFS-3G") 来解决这个问题。 

##  参阅

  * [gentoo wiki: udisks](<https://wiki.gentoo.org/wiki/Udisks>)
  * [Udisks 介绍](<http://blog.fpmurphy.com/2011/08/introduction-to-udisks.html?output=pdf>)
