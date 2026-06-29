**翻译状态：**

  * 本文（或部分内容）译自 [gPhoto](<https://wiki.archlinux.org/title/gPhoto> "arch:gPhoto")，最近一次同步于 2018-07-13，若英文版本有所[更改](<https://wiki.archlinux.org/title/gPhoto?diff=0&oldid=529363>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/gPhoto_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

[![](../File:Tango-preferences-desktop-locale.png)](<../File:Tango-preferences-desktop-locale.png>)**本文或本节需要[翻译](<../Project:Contributing_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\).html#%E7%BF%BB%E8%AF%91> "Project:Contributing \(简体中文\)")。要贡献翻译，请访问[简体中文翻译团队](<../Project:%E7%BF%BB%E8%AF%91%E5%9B%A2%E9%98%9F.html> "Project:翻译团队")。**

**附注：** A few updates have happened on the English page since last translation.（在 [Talk:GPhoto#](<../zh-cn/Talk:GPhoto.html>) 中讨论）

相关文章

  * [Jalbum](</wzh/index.php?title=Jalbum&action=edit&redlink=1> "Jalbum（页面不存在）")

[Libgphoto2](<http://www.gphoto.org/proj/libgphoto2/>)是实现访问数码相机的核心库，它为Digikam、gphoto2等应用程序提供接口。当前版本的官方支持列表在[这里](<http://www.gphoto.org/proj/libgphoto2/support.php>)。这份列表比较保守，某些相机其实也能工作。 

本文阐述如何配置`libgphoto2`，以便访问数码相机。某些数码相机可以直接按[U盘模式](<../zh-cn/USB_storage_devices.html> "USB storage devices")挂载，无需libghoto2。 

##  安装

[安装](<../zh-cn/Pacman.html> "Pacman")软件包 [libgphoto2](<https://archlinux.org/packages/?name=libgphoto2>)包。可选的包还有 [gphoto2](<https://archlinux.org/packages/?name=gphoto2>)包，提供了命令行界面。 

###  前端程序

  * **[darktable](<https://en.wikipedia.org/wiki/darktable> "wikipedia:darktable")** — Utility to organize and develop raw images.

     <https://darktable.org/> || [darktable](<https://archlinux.org/packages/?name=darktable>)包

  * **[digiKam](<../zh-cn/Digikam.html> "Digikam")** — Digital photo management application for [KDE](<../zh-cn/KDE.html> "KDE").

     <https://www.digikam.org/> || [digikam](<https://archlinux.org/packages/?name=digikam>)包

  * **Entangle** — Provides a graphical interface for “tethered shooting”, aka taking photographs with a digital camera completely controlled from the computer.

     <https://entangle-photo.org/> || [entangle](<https://aur.archlinux.org/packages/entangle/>)AUR

  * **gphotofs** — [Fuse](</wzh/index.php?title=Fuse&action=edit&redlink=1> "Fuse（页面不存在）") module to mount camera as a filesystem.

     <http://www.gphoto.org/proj/gphotofs/> || [gphotofs](<https://aur.archlinux.org/packages/gphotofs/>)AUR

  * **[gThumb](<https://en.wikipedia.org/wiki/GThumb> "wikipedia:GThumb")** — Image browser and viewer for [GNOME](<../zh-cn/GNOME.html> "GNOME").

     <https://wiki.gnome.org/gthumb> || [gthumb](<https://archlinux.org/packages/?name=gthumb>)包

  * **GTKam** — Graphical [GTK+](<../zh-cn/GTK.html> "GTK+") 2 front-end to gphoto2.

     <http://www.gphoto.org/proj/gtkam/> || [gtkam](<https://aur.archlinux.org/packages/gtkam/>)AUR

  * **gvfs-gphoto2** — gphoto2 backend for GVfs to mount camera as a filesystem from a file manager that supports GVfs such as [GNOME Files](<../zh-cn/GNOME_Files.html> "GNOME Files"), [Nemo](</wzh/index.php?title=Nemo&action=edit&redlink=1> "Nemo（页面不存在）"), [PCManFM](<../zh-cn/PCManFM.html> "PCManFM") and [Thunar](<../zh-cn/Thunar.html> "Thunar").

     <https://wiki.gnome.org/Projects/gvfs> || [gvfs-gphoto2](<https://archlinux.org/packages/?name=gvfs-gphoto2>)包

  * **Kamera** — [KDE](<../zh-cn/KDE.html> "KDE") integration for gphoto2 cameras.

     <https://github.com/KDE/kamera> || [kamera](<https://archlinux.org/packages/?name=kamera>)包

  * **Pantheon Photos** — Image viewer for Pantheon.

     <https://launchpad.net/pantheon-photos> || [pantheon-photos](<https://archlinux.org/packages/?name=pantheon-photos>)包

  * **[Rawstudio](<https://en.wikipedia.org/wiki/Rawstudio> "wikipedia:Rawstudio")** — An open source raw-image converter written in GTK+. Supports tethered shooting with gphoto2.

     <https://rawstudio.org/> || [rawstudio](<https://aur.archlinux.org/packages/rawstudio/>)AUR

  * **[Shotwell](<https://en.wikipedia.org/wiki/Shotwell_\(software\)> "wikipedia:Shotwell \(software\)")** — Digital photo organizer designed for [GNOME](<../zh-cn/GNOME.html> "GNOME").

     <https://wiki.gnome.org/Apps/Shotwell> || [shotwell](<https://archlinux.org/packages/?name=shotwell>)包

##  GPhoto2用法

GPhoto2是libgphoto2的命令行版客户端，它可以让用户从终端或者脚本中访问libgphoto2，从而操作数码相机。另外，GPhoto2也为驱动开发者提供了方便的调试功能。 

**常用操作**

  * `gphoto2 --list-ports`
  * `gphoto2 --auto-detect`
  * `gphoto2 --summary`
  * `gphoto2 --list-files`
  * `gphoto2 --get-all-files`

更高级的文件操作 

  * `gphoto2 --shell`

###  使用 gvfs

用下面命令检测连接的摄像头和端口: 
    
    $ gphoto2 --auto-detect
    Model                          Port                                            
    ----------------------------------------------------------
    Canon Digital IXUS 980 IS      usb:006,011 
    
在文件管理器中使用下面地址进行访问: "gphoto2://[usb:006,011]" - 摄像头会被 gvfs 挂载并通过文件管理器进行管理。 

##  权限问题

有本地会话的用户会通过 [ACLs](<https://en.wikipedia.org/wiki/Access_control_list> "wikipedia:Access control list") 获得摄像头权限，有问题请查看 [General troubleshooting#Session permissions](<../zh-cn/General_troubleshooting.html#Session_permissions> "General troubleshooting")。 

##  参阅

  * [gPhoto 支持的摄像头列表](<http://www.gphoto.org/proj/libgphoto2/support.php>)
  * [更详细的列表](<https://web.archive.org/web/20180820013307/http://www.teaser.fr/~hfiguiere/linux/digicam.html>)
