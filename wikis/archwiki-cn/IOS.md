**翻译状态：**

  * 本文（或部分内容）译自 [iOS](<https://wiki.archlinux.org/title/iOS> "arch:iOS")，最近一次同步于 2025-12-21，若英文版本有所[更改](<https://wiki.archlinux.org/title/iOS?diff=0&oldid=856663>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/iOS_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

相关文章

  * [有声书](</wzh/index.php?title=%E6%9C%89%E5%A3%B0%E4%B9%A6&action=edit&redlink=1> "有声书（页面不存在）")
  * [iPhone 网络共享](<../zh-cn/IPhone_%E7%BD%91%E7%BB%9C%E5%85%B1%E4%BA%AB.html> "IPhone 网络共享")
  * [iPod](</wzh/index.php?title=IPod&action=edit&redlink=1> "IPod（页面不存在）")（英语：[iPod](<https://wiki.archlinux.org/title/iPod> "en:iPod")）

[iOS](<https://www.apple.com/ios/>) 是由 Apple Inc. 开发的用于iPhone系列手机的操作系统。虽然Apple官方并不支持将iOS设备连接到Linux，但 [libimobiledevice](<https://libimobiledevice.org/>) 项目提供了连接iOS与Linux设备并传输数据所需的库与工具。 

**提示：** 还可以使用 [KDE Connect](<../zh-cn/KDE_Connect.html> "KDE Connect") 来在iOS和Linux间传输文件。

##  安装

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") [libimobiledevice](<https://archlinux.org/packages/?name=libimobiledevice>)包 与 [usbmuxd](<https://archlinux.org/packages/?name=usbmuxd>)包 包。 

##  连接到设备

###  使用 Usbmux 守护进程

_usbmuxd_ 负责与iOS设备间的底层连接。 _usbmuxd_ 包也包含了一条 [udev](<../zh-cn/Udev.html> "Udev") 规则，使得在设备连接或断开连接时可以自动启动和停止守护进程。 

连接iOS设备并确认 `usbmuxd.service` 已经自动启动。 
    
    $ systemctl status usbmuxd.service
    
    _..._
    Active: active (running) since Sun 2020-01-19 19:23:18 UTC; 22s ago
    _..._
    
###  配对

连接iOS设备后解锁屏幕，您将会在设备上看到“是否信任此电脑？”的弹窗。点击“信任”，然后输入您的设备密码来完成配对过程。 

如果您没有看到上述弹窗，您也可以手动开始配对过程。连接设备，并在解锁屏幕后运行： 
    
    $ idevicepair pair
    
    SUCCESS: Paired with device d8e8fca2dc0f896fd7cb4cb0031ba249
    
如果您同时连接了多台iOS设备，也可以通过传递 `--udid _ios_udid_` 参数来选定一个特定设备。 

要验证配对已成功，可以运行： 
    
    $ idevicepair validate
    
    SUCCESS: Validated pairing with device 00008030-001D3562367A402E
    
###  传输数据

配对后，iOS会在电脑上显示两个不同的文件系统。其一是媒体文件系统，包含了设备的照片、视频与音乐。 第二个文件系统用来直接与特定应用程序共享文件。它有时被称为“iTunes 文档共享”。[[1]](<https://support.apple.com/en-us/HT201301>) [[2]](<https://www.hadess.net/2010/12/house-arrest-or-just-document-sharing.html>)

####  使用图形化文件管理器

使用 [GVFS](<../zh-cn/%E6%96%87%E4%BB%B6%E7%AE%A1%E7%90%86%E5%99%A8%E5%8A%9F%E8%83%BD.html#%E6%8C%82%E8%BD%BD> "GVFS") 的文件管理器可以与iOS设备交互。要访问媒体文件系统，[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") [gvfs-gphoto2](<https://archlinux.org/packages/?name=gvfs-gphoto2>)包。要访问应用程序文档文件系统，需安装 [gvfs-afc](<https://archlinux.org/packages/?name=gvfs-afc>)包。 

**注意：** 访问媒体文件系统时，GVFS 只会显示设备的照片与视频，而不会显示音乐。

[kio-extras](<https://archlinux.org/packages/?name=kio-extras>)包 包中包含有对 [Dolphin](<../zh-cn/Dolphin.html> "Dolphin") 的iOS设备支持，它现在已经是 Dolphin 的依赖之一。[[3]](<https://blog.broulik.de/2022/11/introducing-kio-afc/>)

####  手动挂载

[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "Install") [ifuse](<https://archlinux.org/packages/?name=ifuse>)包 包。您可以通过运行以下命令来挂载您的iPhone上的媒体文件系统： 
    
    $ ifuse _mountpoint（挂载点）_
    
您可以通过此在 `_mountpoint_ /DCIM` 中访问设备中的照片。 

**注意：** 借此，设备的音乐数据库也可以在 `_mountpoint_ /iTunes_Control` 访问。您不能以这种方式向设备添加新的曲目，但可以借此将设备中的歌曲复制到您的电脑。

**警告：** 手动编辑 iTunes_Control 中的数据库会导致其损坏，这将使您已同步的歌曲变为只能通过重置系统（抹掉iPhone）来移除的过时失效数据。

要访问一个应用程序的文档文件系统，您首先需要辨认该应用程序。 
    
    $ ifuse --list-apps
    
    "CFBundleIdentifier","CFBundleVersion","CFBundleDisplayName"
    "org.videolan.vlc-ios","432","VLC"
    "org.wikimedia.wikipedia","1932","Wikipedia"
    "org.kde.kdeconnect","2","KDE Connect"
    [...]
    
然后您便可以使用以下命令挂载一个应用程序的文件： 
    
    $ ifuse --documents _APPID_ _mountpoint（挂载点）_
    
其中，APPID是所需应用程序的包的识别符（包名），例如 `org.videolan.vlc-ios`。 

完成后，卸载文件系统： 
    
    $ fusermount -u _mountpoint_
    
##  导入视频与图像

照片和视频通常都可以在 `_< mountpoint>_/DCIM/100APPLE` 下被找到。 

iOS 倾向于使用一些没有良好支持的文件格式，但您也可以通过手动设置让其使用兼容性更好的文件格式。此外，您可能也会想要将使用兼容性较差的格式存储的文件转为兼容性较好的格式。 

##  备份

###  创建备份

您可以运行以下命令以通过 libimobiledevice 为您的 iOS 设备创建一个完整的备份，其中 `_backup_to_` 是您存放备份文件的文件夹: 
    
    $ idevicebackup2 backup --full _backup_to_
    
您可能需要在您的 iOS 设备上输入设备密码以授权备份操作。 

###  还原备份

您可以使用以下命令还原 `_restore_from_` 中存放的备份: 
    
    $ idevicebackup2 restore _restore_from_
    
###  访问备份中的内容

`idevicebackup2` 提供了 `info` 与 `unback` 等子命令以供访问备份中的内容。 [其中 list 子命令当前不可用。](<https://github.com/libimobiledevice/libimobiledevice/issues/1058>)

一些其他工具，[例如这个](<https://github.com/MaxiHuHe04/iTunes-Backup-Explorer>)，也可以用于查看和导出备份中的内容。 

**提示：** 如果您被要求打开 _iTunes 备份_ 文件，请打开备份文件夹中的 `Manifest.db` 。

##  设备还原

[idevicerestore-git](<https://aur.archlinux.org/packages/idevicerestore-git/>)AUR 可用于更新（重新安装 iOS 并保留用户数据）或还原（重新安装 iOS 并抹掉用户数据）iOS 设备。 

##  疑难解答

###  ifuse 无法挂载应用程序文件目录

使用 _ifuse_ 挂载应用程序目录并尝试列出挂载点下的内容时，您可能会遇到下面的错误： 
    
    ".": Input/output error (os error 5)
    
这是一个[已知问题](<https://github.com/libimobiledevice/ifuse/issues/63>)，已经在现在的 libimobiledevice 开发版本中被修复，但尚未进入稳定版中。解决办法是安装 [libimobiledevice-git](<https://aur.archlinux.org/packages/libimobiledevice-git/>)AUR 。 

###  设备无法被重定向至虚拟机

如果您使用USB来在 Windows 虚拟机中同步设备，尝试将其重定向可能会因 "其他应用程序正在使用该设备" 而失败。这是由于 `usbmuxd.service` 在设备连接后自动启动。这可以通过[停用或屏蔽](<../zh-cn/Systemd.html#Using_units> "Systemd") `usbmuxd.service` 来解决。 

##  参考

  * [Ubuntu 的 iPhone 与 iPod Touch 文档](<https://help.ubuntu.com/community/PortableDevices/iPhone>) (2014年以后未见更新)
